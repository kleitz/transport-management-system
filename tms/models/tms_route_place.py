# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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


from openerp import models, fields


class TmsRoutePlace(models.Model):
    _name = 'tms.route.place'
    _description = 'Intermediate Places in Routes'

    route_id = fields.Many2one('tms.route', 'Route', required=True)
    place_id = fields.Many2one('tms.place', 'Place', required=True)
    state_id = fields.Many2one(
        'place_id', 'state_id', relation='res.country.state',
        store=True, readonly=True)
    country_id = fields.Many2one(
        'place_id', 'country_id', relation='res.country',
        store=True, readonly=True)
    sequence = fields.Integer(
        'Sequence', help="Gives the sequence order when displaying this list.")

    _defaults = {
        'sequence': 10,
    }