# set encoding=utf-8
from django.db.models import get_model
from oscar.apps.checkout import forms

from oscar.apps.checkout import forms
Country = get_model('address', 'Country')


class ShippingAddressForm(forms.ShippingAddressForm):

    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)

        self.fields['postcode'].blank=False
        self.fields['postcode'].initial=u'614000'

        #self.fields['first_name'].label=u'Ф.И.О.'


        self.fields['line1'].label = u"Улица, дом, корпус, квартира, офис"
 #      self.fields['line2'].label = u"Дом, корпус, квартира, офис"
    class Meta:
        model = get_model('order', 'shippingaddress')
       # exclude = ('postcode',)
        fields = ('first_name',   'line1','postcode',
                 'phone_number', 'notes', 'country')



