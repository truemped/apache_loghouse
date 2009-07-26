#
# Copyright (c) 2008 Daniel Truemper truemped@googlemail.com
#
# settings.py 26-Jul-2009
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

COUCHDB_SERVER = "http://localhost:5984/"
COUCHDB_DATABASE = "apache_loghouse"

COUCHDB_QUERIES = {
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


