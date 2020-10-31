# -*- coding: utf-8 -*-
# Copyright 2020 ePayco.co
# - Manuel Marquez <buzondemam@gmail.com>
# - Yan chirino <support@yanchirino.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from . import controllers
from . import models
from odoo.service import common
from odoo.exceptions import Warning


def pre_init_check(cr):
    version_info = common.exp_version()
    server_serie = version_info.get('server_serie')

    if server_serie != '13.0':
        raise Warning('Module support Odoo series 13.0 found {}.'.format(server_serie))

    return True
