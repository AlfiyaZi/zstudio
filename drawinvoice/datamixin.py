#set encoding=utf-8
from decimal import Decimal as D
from decimal import getcontext
from datetime import date 
import logging
from babel.numbers import format_decimal

from basedraw import Parameters
logger = logging.getLogger(__name__)

def getVat(amount):
    return amount / D('118.00') * D('18')

def getTax(amount, item=None):
    tax = None
    if item:
        tax = item.get('tax', None)
    if tax is None:
        return getVat(amount)
    return tax

class Item(object):
    def __init__(self, item, pos=None):
        self.units = item.get('units', None) or u'шт'
        self.price = D(item.get('price', 0))
        self.quantity = D(item.get('quantity', 0))
        self.amount =  D(item.get('amount', 0))
        if not self.amount and self.price and self.quantity:
            self.amount = self.price * self.quantity
        elif not self.price and self.amount and self.quantity:
            self.price = self.amount / self.quantity
        elif not self.quantity and self.price and self.amount:
            self.quantity = D(self.amount / self.price).quantize(0)
        self.tax = getTax(self.amount, item)
        self.name = item.get('name', '')
        self.position = pos



class DataMixin(object):
    """Manages requisites and calculations for invoice"""
    def __init__(self):
        logger.debug("initializing")
        self.data = Parameters()
        self.goods = []
        self.totals = Parameters()
        self.date = date.today()

    def setInvoiceNumber(self, num):
        self.data.invoiceNumber = str(num)

    def parseGoods(self):
        logger.debug("parsing goods")
        i= 0
        total = D(0)
        for item in self.data.goods:
            i += 1
            line = Item(item, pos=i)
            self.goods.append(line)
            total += line.amount
        self.totals.total = total
        self.totals.quantity = i
        self.totals.tax = getTax(total, self.data.order)
        self.totals.due = None

    def feed(self, **kwargs):
        self.data.update(kwargs)

    def finalize(self):
        logger.debug('finalizing')
        self.parseGoods()
        logger.debug("original type of beneficiary is %s", type(self.data.beneficiary))

        self.data['beneficiary'] = Parameters(self.data.beneficiary)
        logger.debug("type of beneficiary is %s", type(self.data.beneficiary))

        self.data.customer = Parameters(self.data.customer)
        logger.debug("type of customer is %s", type(self.data.customer))
        self.data.order = Parameters(self.data.order)
        if not self.data.invoiceNumber:
            try:
                self.data.invoiceNumber = self.data.order.number
            except AttributeError:
                pass
        logger.debug('successfully finalized')


