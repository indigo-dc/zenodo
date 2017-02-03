# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2016 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Page cache module."""

from __future__ import absolute_import, print_function

from functools import wraps

from flask_security import current_user

from .proxies import current_cache as cache


def cached(timeout=50, key_prefix='default'):
    """Cache anonymous traffics."""
    def caching(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cache_fun = cache.cached(
                timeout=timeout, key_prefix=key_prefix,
                unless=lambda: current_user.is_authenticated)
            return cache_fun(f)(*args, **kwargs)
        return wrapper
    return caching
