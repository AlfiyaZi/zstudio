from oscar.apps.address.abstract_models import *


class AbstractAddress(models.Model):
    def clean(self):
        # Strip all whitespace
        for field in ['first_name', 'last_name', 'line1', 'line2', 'line3',
                      'line4', 'postcode']:
            if self.__dict__[field]:
                self.__dict__[field] = self.__dict__[field].strip()

