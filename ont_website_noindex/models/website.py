# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields

class Website(models.Model):
    _inherit = "website"

    no_index = fields.Boolean(
        string="No permitir que el sitio aparezca en los motores de busqueda como Google y Bing."
    )


class WebsiteConfigSettings(models.TransientModel):
    """Settings Website"""

    _inherit = 'website.config.settings'

    no_index = fields.Boolean(
        related='website_id.no_index',
        string="No permitir que el sitio aparezca en los motores de busqueda como Google y Bing."
    )
