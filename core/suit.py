
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):

    layout = 'vertical'

    menu = (
        ParentItem(
            app='products',
            children=[
                ChildItem(model='products.product'),
                ChildItem(
                    label='Import products',
                    url='products:import'
                ),
                ChildItem(
                    label='Export products in ccv',
                    url='products:csv_export'
                ),
                ChildItem(
                    label='Export products in xls',
                    url='products:xls_export'
                ),
            ]
        ),
    )
