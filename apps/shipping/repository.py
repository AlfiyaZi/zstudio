#set encoding=utf-8

from oscar.apps.shipping import repository 
from apps.shipping.methods import (
    Pickup, Express, RusPost)


class Repository(repository.Repository):
    methods = (Pickup, Express)

    def get_available_shipping_methods(
            self, basket, user=None, shipping_addr=None,
            request=None, **kwargs):

        methods = (Pickup,Express)
        if shipping_addr:
            shipping_addr and shipping_addr.country.code == 'RU'
        #    # Express is only available in the UK
            methods = (Pickup, Express)
        return methods