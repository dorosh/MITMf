#!/usr/bin/env python2.7

# Copyright (c) 2014-2016 Marcello Salvati
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

import logging
from plugins.plugin import Plugin

mitmf_logger = logging.getLogger("mitmf")

class XFFor(Plugin):
    name        = "XFFor"
    optname     = "xffor"
    desc        = "Update remote address to use the address from the X-Forwarded-For header"
    version     = "0.1"

    def initialize(self, options):
        self.bad_headers = ['X-Forwarded-For']

    def serverHeaders(self, response, request):
        '''Handles all response headers'''
        print response.headers.get('Remote Address'), response.headers.get('X-Forwarded-For')

    def clientRequest(self, request):
        '''Handles outgoing request'''
        try:
            ip_addresses = request.headers['X-Forwarded-For']
        except KeyError:
            pass
        else:
            for ip_address in ip_addresses.split(', '):
                try:
                    ipaddress.ip_address(ip_address)
                except ValueError:
                    pass
                else:
                    request.headers['Remote Address'] = ip_address
                    break
