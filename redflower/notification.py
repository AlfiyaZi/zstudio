__author__ = 'alya'

from smsaero.utils import send_sms
from smsaero.utils import get_sms_status
from smsaero.utils import get_balance
from smsaero.utils import get_signatures_name
from smsaero.models import SMSMessage




# Send SMS
sms = send_sms('+79526646699', 'hello green') # sms has SMSMessage type
