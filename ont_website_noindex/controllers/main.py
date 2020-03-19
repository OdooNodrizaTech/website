# -*- coding: utf-8 -*-
from openerp import _, api, exceptions, fields, models
from openerp.http import request

from odoo import http
from odoo.http import request

import logging

from odoo.addons.website.models.website import slug
from odoo.addons.web.controllers.main import WebClient, Binary, Home

_logger = logging.getLogger(__name__)

class Website(Home):

    @http.route(['/website/index_noindex'], type='json', auth="public", website=True)
    def index_noindex(self, index):
        if index == 'index':
            request.website.write({
                'no_index': False
            })
        else:
            request.website.write({
                'no_index': True
            })
        return True
