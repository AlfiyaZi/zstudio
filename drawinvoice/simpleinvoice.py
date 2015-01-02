#set encoding=utf-8
import logging
from collections import namedtuple
from babel.numbers import format_decimal

from reportlab.platypus import PageTemplate
from reportlab.platypus import Frame
from reportlab.lib.units import mm
from reportlab.platypus import Table
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

from datamixin import DataMixin
from basedraw import BaseDraw 
debug = False
logger = logging.getLogger(__name__)

class Invoice(BaseDraw, DataMixin):
    """draws the invoice"""
    def setup(self):
        self.Line = namedtuple("Line", 
            ('position', 'name', 'quantity', 'units', 'price', 'amount'))
        self.story = []

        p = self.param
        p.tablePadding = 1
        p.normalSize = 9
        p.minSize = 8
        p.bigSize = 14

        p.firstFrameWidth = 175*mm
        p.firstFrameHeight = 210*mm

        p.normalStyle = getSampleStyleSheet()['Normal']
        p.normalStyle.fontName = p.baseFont

        p.minStyle = getSampleStyleSheet()['Normal']
        p.minStyle.fontName = p.baseFont
        p.minStyle.fontSize = p.minSize
        p.minStyle.leading = p.minSize * 1.2

        self.setupDoc()
        self.setupTableStyles()

    def setupTemplates(self):
        _D = lambda x: format_decimal(x, locale="ru_RU")
        _C = lambda x: format_decimal(x, format='#,##0.00', locale="ru_RU")

        self.templates.warn = u"""Внимание! Оплата данного счета означает согласие с условиями поставки товара. Уедомление об оплате
        обязательно. В противном случае не гарантируется наличие товара на складе. Товар отпускается по факту
        прихода денег на р/с Поставщика. самовывозом при наличии доверенности и паспорта"""

        def memberTemplate(m):
            res = u"<b>{m.name}"
            if m.INN:
                res += u", ИНН {m.INN}"
            if m.KPP:
                res += u", КПП {m.KPP}"
            res += u", {m.address}"
            if m.tel:
                res += u", тел.: {m.tel}</b>" 
            return res.format(m=m)
        self.templates.memberTemplate = memberTemplate

        def itemTemplate(item):
            pStyle = self.param.minStyle
            return self.Line(
                    item.position,
                    Paragraph(item.name, pStyle),
                    _D(item.quantity),
                    item.units,
                    _C(item.price),
                    _C(item.amount)
                    )
        self.templates.itemTemplate = itemTemplate

        self.templates.amountTemplate = lambda amount, due: Paragraph(
                u"Всего наименований {amount}, на сумму {due} руб.".format(
                    amount=_D(amount), due=_C(due)), self.param.normalStyle)

        def spellTotal(total):
            template = u"{rubles} {kopnum:02d} {kopstr}"
            from pytils import numeral
            n = {}
            n['rubles'] = numeral.rubles(int(total)).capitalize()
            n['kopnum'] = int(total * 100) - int(total)*100
            n['kopstr'] = numeral.choose_plural(
                    n['kopnum'], 
                    (u"копейка", u"копейки", u"копеек")
                    )
            return template.format(**n)

        self.templates.spellTotal = lambda due: Paragraph(
                u"<b>{}</b>".format(spellTotal(due)), 
                self.param.normalStyle)

        self.templates.totalsTableTemplate = lambda total, vat, due: (
                        ("", u"Итого:", _C(total)),
                        ("", u"В том числе НДС:", _C(vat) if vat else u"Без НДС"),
                        ("", u"Всего к оплате:", _C(due)),
                        )
        
        from pytils.dt import ru_strftime
        self.templates.invoiceTitle = lambda invoiceNum: \
                u"Счет на оплату №{} от {}".format(str(invoiceNum), 
                        ru_strftime(u"%d %B %Y", inflected=True, 
                            date=self.date))


    def setupDoc(self):
        self.doc = BaseDocTemplate(
            self.filename,
            pagesize = self.param.pageSize,
            leftMargin = 15*mm,
            bottomMargin = 10*mm,
            rightMargin = 20*mm,
            topMargin = 10*mm
            )

        firstFrame = Frame(self.doc.leftMargin, self.doc.bottomMargin, 
            self.param.firstFrameWidth, self.param.firstFrameHeight,
            id='first', showBoundary=debug)
        laterFrame = Frame(self.doc.leftMargin, self.doc.bottomMargin, 
            self.doc.width, self.doc.height, id='later')

        def changeTemplate(canvas, document):
            document.handle_nextPageTemplate('Later')

        def writeHead(canvas, document):
            self.writeHead(canvas)

        self.doc.addPageTemplates((
            PageTemplate(id='First', frames=firstFrame, onPage=writeHead,
                onPageEnd=changeTemplate),
            PageTemplate(id='Later', frames=laterFrame)
            ))

    def setupTableStyles(self):
        from reportlab.platypus import TableStyle
        base = TableStyle((
            ('FONTNAME', (0,0), (-1,-1), self.param.baseFont),
            ('LEFTPADDING', (0,0), (-1,-1), self.param.tablePadding + 1),
            ('RIGHTPADDING', (0,0), (-1,-1),self.param.tablePadding + 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), self.param.tablePadding),
            ('TOPPADDING', (0,0), (-1,-1), self.param.tablePadding),
            ('VALIGN', (0,0), (-1,-1), "BOTTOM")
            ))
        self.param.signaturesTableStyle = TableStyle((
            ('FONTNAME', (0,0), (0,0), self.param.boldFont),
            ('FONTNAME', (2,0), (2,0), self.param.boldFont),
            ('FONTNAME', (1,0), (1,0), self.param.baseFont),
            ('FONTNAME', (3,0), (3,0), self.param.baseFont),
            ('ALIGN', (0,0), (0,0), "LEFT"),
            ('ALIGN', (2,0), (2,0), "LEFT"),
            ('ALIGN', (1,0), (1,0), "RIGHT"),
            ('ALIGN', (3,0), (3,0), "RIGHT"),
            ('FONTSIZE', (1,0), (1,0), self.param.minSize),
            ('FONTSIZE', (3,0), (3,0), self.param.minSize),
            ('LINEABOVE', (0,0), (-1,0), 2, self.param.lineColor),
            ('LINEBELOW', (1,0), (1,0), 1, self.param.lineColor),
            ('LINEBELOW', (3,0), (3,0), 1, self.param.lineColor),
            ('TOPPADDING', (0,0), (0,-1), 5 * mm),
            ('LEFTPADDING', (2,0), (2,0), 10*mm)
            ), parent=base)
        self.param.totalsTableStyle = TableStyle((
            ('TOPPADDING', (0,0), (-1, 0), 3*mm),
            ('FONTNAME', (0, 0), (-1, -1), self.param.boldFont),
            ('ALIGN', (1,0), (-1, -1), "RIGHT"),
            ), parent=base)
        self.param.goodsTableStyle = TableStyle(
            (('FONTNAME', (0,0), (-1,-1), self.param.baseFont),
            ('FONTNAME', (0,0), (-1,0), self.param.boldFont),
            ('FONTSIZE', (0,1), (-1, -1), self.param.minSize),
            ('LEADING', (0,1), (-1, -1), self.param.minSize * 1.2),
            ('ALIGN', (0,0), (-1, 0), "CENTRE"),
            ('ALIGN', (0,1), (0,-1), "CENTRE"),
            ('ALIGN', (2,1), (2,-1), "RIGHT"),
            ('ALIGN', (4,1), (-1,-1), "RIGHT"),
            ('INNERGRID', (0,0), (-1,-1), 1, self.param.lineColor),
            ('BOX', (0,0), (-1,-1), 2, self.param.lineColor)), parent=base)
        self.param.memberTableStyle = TableStyle((
                ('FONTNAME',(0,0), (-1,-1), self.param.baseFont),
                ('VALIGN', (0,0), (0,-1), "TOP"),
                ('BOTTOMPADDING', (0,0), (-1, 0), 4 * mm),
                ('ALIGN', (0,0), (0,-1), "LEFT")
                ), parent=base)

    def writeHead(self, canvas): 

        canvas.setFont(self.param.baseFont, self.param.normalSize)

        def writeWarn(warn):
            c = canvas
            c.saveState()
            c.setFontSize(self.param.minSize)
            warnsplit = warn.split('\n')
            count = 1
            start = 275*mm
            x = self.doc.pagesize[0] / 2
            for line in warnsplit:
                y = start-count*self.param.minSize
                c.drawCentredString(x, y, line)
                count += 1
            c.restoreState()

        writeWarn(self.templates.warn)

        def writeName(x, y, name):
            c = canvas
            text = c.beginText()
            text.setTextOrigin(x, y)
            text.setLeading(self.param.normalSize + 1)
            text.textLines(name)
            return text

        def writeRequisites(req):
            c = canvas
            c.saveState()
            c.translate(self.doc.leftMargin, 235*mm)
            x = (0, 43*mm, 86*mm, 100*mm, 175*mm)
            y = (0, 11*mm, 15*mm, 23*mm, 27*mm)
            c.grid((x[0], x[2], x[3], x[4]), (y[0], y[2], y[4]))
            c.grid((x[0], x[1], x[2]), (y[1], y[2]))
            c.line(x[2], y[3], x[3], y[3])
            c.setFontSize(self.param.minSize)
            c.drawString(mm, y[2] + mm, u"Банк получателя")
            c.drawString(mm, mm, u"Получатель")
            c.setFontSize(self.param.normalSize)
            c.drawString(x[2] + mm, y[3] - self.param.normalSize, u"Сч. №")
            c.drawString(x[2] + mm, y[2] - self.param.normalSize, u"Сч. №")
            c.drawString(mm, y[1]+0.5*mm, u"ИНН   %s" % req.INN)
            c.drawString(x[1] + mm, y[1]+0.5*mm, u"КПП   %s" % req.KPP)
            c.drawString(x[2] + mm, y[3] + mm, u"БИК")
            c.drawString(x[3] + mm, y[3] + mm, req.BIK)
            c.drawString(x[3] + mm, y[3] - self.param.normalSize, req.correspondentAccount)
            c.drawString(x[3] + mm, y[2] - self.param.normalSize, req.beneficiaryAccount)
            c.drawText(writeName(mm, y[-1] - self.param.normalSize, req.bankName))
            c.drawText(writeName(mm, y[1] - self.param.normalSize, req.name))
            c.restoreState()


        writeRequisites(self.data.beneficiary)

        x = (self.doc.leftMargin, self.doc.width / 2, self.doc.pagesize[0] - self.doc.rightMargin)

        def writeInvoiceTitle(invoiceNum):
            c = canvas
            c.saveState()
            c.setFont(self.param.boldFont, self.param.bigSize)
            c.drawString(x[0], 225*mm, self.templates.invoiceTitle(invoiceNum))
            c.setLineWidth(0.5*mm)
            c.line(x[0], 222*mm, x[-1], 222*mm)
            c.restoreState()

        writeInvoiceTitle(self.data.invoiceNumber)



#========================================
    def writeSignatures(self):
        manager = self.data.beneficiary.get('manager', '')
        accountant = self.data.beneficiary.accountant or manager
        signaturesTable = Table(
                ((u"Руководитель", manager, u"Бухгалтер", accountant),),
                colWidths = (29*mm, 61*mm, 30*mm, 55*mm),
                style = self.param.signaturesTableStyle)
        self.story.append(signaturesTable)

    def writeMembers(self):
        beneficiaryData = self.templates.memberTemplate(
                m=self.data.beneficiary)
        customerData = self.templates.memberTemplate(
                m=self.data.customer)
        data = (
                (u"Поставщик:", Paragraph(beneficiaryData, self.param.normalStyle)),
                (u"Покупатель:", Paragraph(customerData, self.param.normalStyle))
                )
        self.story.append(Table(data, 
                colWidths=(30*mm, 145*mm),
                style=self.param.memberTableStyle))

    def writeGoods(self):
        header = (u"№", u"Товары (работы, услуги)", u"Кол-во", u"Ед.", u"Цена", u"Сумма")
        goodsTable = [self.templates.itemTemplate(item) for item in self.goods]
        goodsTable.insert(0, header)

        t = Table(goodsTable, colWidths=(10*mm, 100*mm, 15*mm, 8*mm, 17*mm, 25*mm))
        t.setStyle(self.param.goodsTableStyle)
        self.story.append(t)

    def writeTotals(self):
        quantity = self.totals.quantity
        total = self.totals.total
        vat = self.totals.tax
        due = self.totals.due or total
        totalsTable = self.templates.totalsTableTemplate(total = total,
                vat = vat, due = due)
        t = Table(totalsTable, 
                colWidths=(125*mm, 25*mm, 25*mm), 
                style=self.param.totalsTableStyle)
        self.story.append(t)
        self.story.append(self.templates.amountTemplate(quantity, due))
        self.story.append(self.templates.spellTotal(due))

    def instanceWrite(self):
        logger.debug("============= writing ===========")
        spacer = Spacer(0, self.param.normalSize)
        self.writeMembers()
        self.story.append(spacer)
        self.writeGoods()
        self.writeTotals()
        self.story.append(spacer)
        self.writeSignatures()
        self.doc.build(self.story)
