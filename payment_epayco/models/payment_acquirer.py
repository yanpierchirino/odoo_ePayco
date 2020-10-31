# -*- coding: utf-8 -*-
# Copyright 2020 ePayco.co
# - Manuel Marquez <buzondemam@gmail.com>
# - Yan chirino <support@yanchirino.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from werkzeug import urls

from odoo import fields, models
from odoo.addons.payment_epayco.controllers.main import EpaycoController


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('epayco', 'ePayco')])
    epayco_p_cust_id = fields.Char(
        'P_CUST_ID_CLIENTE',
        required_if_provider='epayco',
        help='Customer ID that identifies you in ePayco.'
        'You can find it in your dashboard in the configuration option.')
    epayco_p_key = fields.Char(
        'P_KEY',
        required_if_provider='epayco',
        help='Key to sign the information sent and received from ePayco.'
        'You can find it in your dashboard in the configuration option.')
    epayco_public_key = fields.Char(
        'PUBLIC_KEY',
        required_if_provider='epayco',
        help='Key to authenticate and consume ePayco services.'
        'You can find it in your dashboard in the configuration option.')
    epayco_checkout_type = fields.Selection(
        selection=[('onpage', 'Onpage Checkout'),
                   ('standard', 'Standard Checkout')],
        required_if_provider='epayco',
        string='Checkout Type',
        default='onpage')
    epayco_franchise_ids = fields.One2many(
        comodel_name='epayco.franchise',
        inverse_name='payment_acquirer_id',
        string='Franchises')
    epayco_tx_state_ids = fields.One2many(
        comodel_name='epayco.tx.state',
        inverse_name='payment_acquirer_id',
        string='Transaction States',
        help='Mapping of ePayco transaction states according to'
        'odoo transaction states.')

    def epayco_get_form_action_url(self):
        """Return url for form action of template form button."""
        return '/payment/epayco/checkout/'

    def epayco_form_generate_values(self, values):
        """Generate values to use in template qweb of form button."""
        self.ensure_one()
        epayco_checkout_external = (
            'false' if self.epayco_checkout_type == 'onpage' else 'true')
        env_test = 'true' if self.state == 'test' else 'false'
        partner_lang = values.get('partner') and values['partner'].lang
        lang = 'es' if 'es' in partner_lang else 'en'

        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        epayco_tx_values = dict(values)
        split_reference = epayco_tx_values.get('reference').split('-')
        order = ''
        if split_reference:
            order = split_reference[0]
        epayco_tx_values.update({
            'currency_code': values.get('currency') and values[
                'currency'].name.lower(),
            'epayco_public_key': self.epayco_public_key,
            'epayco_checkout_external': epayco_checkout_external,
            'country_code': values.get('partner_country') and values[
                'partner_country'].code.lower(),
            'epayco_env_test': env_test,
            'epayco_lang': lang,
            'response_url': urls.url_join(
                base_url, EpaycoController._response_url),
            'confirmation_url': urls.url_join(
                base_url, EpaycoController._confirmation_url),
            'order': order,
        })
        return epayco_tx_values
