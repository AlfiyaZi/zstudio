#set encoding=utf-8
import os
import logging

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4 
from reportlab.lib.units import mm

logging.basicConfig(
        format = "%(name)s:%(levelname)s:\t%(message)s",
        level=logging.ERROR)
logger = logging.getLogger(__name__)

location = lambda x: os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        x)

rl_config.TTFSearchPath.append(location('fonts'))

pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('Sans', 'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Sans Bold', 'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sans Italic', 'LiberationSans-Italic.ttf'))

class Parameters(dict): 
    def __getattr__(self, attr):
        return self.get(attr, '')
    def __setattr__(self, attr, value):
        self[attr] = value

class BaseDraw(object):

    def __init__(self, filename):
        logger.debug('initializing')
        super(BaseDraw, self).__init__()
        self.param = Parameters(
            baseFont = "Sans",
            boldFont = "Sans Bold",
            italicFont = "Sans Italic",
            digitsFont = "DejaVu",
            pageSize = A4,
            normalSize = 9,
            minSize = 6,
            bigSize = 12,
            lineColor = colors.black,
            leading = 6 * mm
            )
        self.templates = Parameters(
                entities = dict(
                    laquo =  u'\u00AB',
                    raquo = u'\u00BB'
                    )
                )
        self.filename = filename
        self.setup()
        self.setupTemplates()
        logger.debug("self.date is set to %s", self.date)
    def write(self):
        super(BaseDraw, self).finalize()
        logger.debug('type of beneficiary is %s', type(self.data.beneficiary))
        self.instanceWrite()
    def setup(self): pass
    def setupTemplates(self): pass
    def finalize(self): pass
    def instanceWrite(self): pass




