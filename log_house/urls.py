#
# Copyright (c) 2008 Daniel Truemper truemped@googlemail.com
#
# urls.py 26-Jul-2009
#
# All programs in this directory and
# subdirectories are published under the GNU General Public License as
# described below.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#
# Further information about the GNU GPL is available at:
# http://www.gnu.org/copyleft/gpl.html
#
#

from datetime import datetime

from django.conf.urls.defaults import *

now = datetime.now()
index_dict = { 'year':now.year, 'month':now.month-1, 'day':now.day }


ajax = {
    'uri': {
        'divid': "uris",
        'caption': "Accessed URIs",
        'titles': [ "#", "URI"],
        'doc': "loghouse/uris"
    },
    'agents': {
        'divid': "agents",
        'caption': "Agents",
        'titles': [ "#", "Agent"],
        'doc': "loghouse/agents"
    },
    'referrer': {
        'divid': "referrers",
        'caption': "Referrers",
        'titles': [ "#", "Referrer"],
        'doc': "loghouse/referral"
    },
    'codes': {
        'divid': "codes",
        'caption': "Status Codes",
        'titles': [ "#", "Status Code"],
        'doc': "loghouse/statusCodes"
    },
}


urlpatterns = patterns('log_house.views',

    # index
    url(r'^$', "day", index_dict, name="index"),

    # by day
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'day', name="day"),

    # by month
#    url(r'^(?P<year>\d{4})/(?P<month>\d{4})/$', 'month', name="month"),

    # by year
#    url(r'^(?P<year>\d{4})/$', 'year', name="year"),

    # ajax: uri by day
    url(r'^dwr/(?P<design>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'ajax', ajax, name="ajax_day"),

)

