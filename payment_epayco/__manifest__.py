# -*- coding: utf-8 -*-
# Copyright 2020 ePayco.co
# - Manuel Marquez <buzondemam@gmail.com>
# - Yan chirino <support@yanchirino.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Epayco Payment Acquirer',
    'summary': 'Epayco Payment Acquirer for the eCommerce.',
    'category': 'Accounting',
    'author': 'ePayco',
    "maintainers": ["mamcode"],
    'development_status': 'Production/Stable',
    'website': 'https://epayco.co/',
    'license': 'AGPL-3',
    'version': '1.0.0',
    'description': """Epayco Payment Acquirer""",
    'depends': ['payment', 'l10n_co', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_icon.xml',
        'views/payment_epayco_templates.xml',
        'data/payment_acquirer.xml',
        'data/epayco_franchise.xml',
        'data/epayco_tx_state.xml',
        'views/payment_acquirer_views.xml',
        'views/payment_transaction_views.xml',
    ],
    'installable': True,
    "pre_init_hook": "pre_init_check",
}
