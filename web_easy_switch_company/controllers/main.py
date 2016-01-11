# -*- encoding: utf-8 -*-
# #############################################################################
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
#############################################################################
import openerp
from openerp import api
from openerp.http import Controller, request, route


class ControllerName(Controller):

    @route(
        '/web_easy_switch_company/switch/change_current_company',
        type='json', auth='user')
    def change_current_company(self, company_id):
        with openerp.api.Environment.manage():
            with openerp.registry(request.env.cr.dbname).cursor() as new_cr:
                new_env = api.Environment(
                    new_cr, request.env.uid, request.env.context)
                return request.env['res.users'].with_env(
                    new_env).change_current_company(company_id)
