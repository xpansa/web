# -*- encoding: utf-8 -*-
##############################################################################
#
#    Web Easy Switch Company module for OpenERP
#    Copyright (C) 2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models
from openerp.tools import image_resize_image


class ResCompany(models.Model):

    _inherit = 'res.company'

    # Fields function Section
    @api.one
    @api.depends('partner_id', 'partner_id.image')
    def _get_logo_topbar(self):
        size = (48, 48)
        self.logo_topbar = image_resize_image(self.partner_id.image, size)

    logo_topbar = fields.Binary(
        string='Logo displayed in the switch company menu',
        compute='_get_logo_topbar',
        store=True,
    )
