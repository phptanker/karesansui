# -*- coding: utf-8 -*-
#
# This file is part of Karesansui.
#
# Copyright (C) 2010 HDE, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#

import web

import karesansui
from karesansui.lib.rest import Rest, auth

class HostBy1Report(Rest):

    @auth
    def _GET(self, *param, **params):
        host_id = self.chk_hostby1(param)
        if host_id is None: return web.notfound()

        self.view.host_id = host_id
        return True

urls = (
    '/host/(\d+)/report/?(\.part)$', HostBy1Report,
    )