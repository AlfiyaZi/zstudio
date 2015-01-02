#set encoding=utf-8

from oscar.apps.shipping import repository 
from apps.shipping.methods import (
    Pickup, Express, RusPost)


class Repository(repository.Repository):
    methods = (Pickup, Express)

    def get_shipping_methods(self, user, basket, shipping_addr=None, **kwargs):

        if shipping_addr is not None:
            city = shipping_addr.line4
            shipping_addr.line4= u"Пермь"
            if city not in (u"Пермь", u"Perm"):
                self.methods = (self.methods[0], self.methods[1])
        methods = super(Repository, self).get_shipping_methods(
                        user, basket, shipping_addr, **kwargs)
        for m in methods:
            if hasattr(m, 'set_shipping_addr'):
                m.set_shipping_addr(shipping_addr)
        return methods


