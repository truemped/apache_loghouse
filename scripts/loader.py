#
# Copyright (c) 2008 Daniel Truemper truemped@googlemail.com
#
# loader.py 23-Jul-2009
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

import sys
import re
import md5
import datetime

from couchdbkit.client import Server
from couchdbkit.schema import Document
from couchdbkit.schema.properties import *
from couchdbkit.session import create_session

import datetime
from httpagentparser import DetectorBase
import httpagentparser

month_map = {'Jan': 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 
        'Aug':8, 'Oct':9, 'Nov': 11, 'Dec': 12}

def apachetime(s):
    " see: http://blog.client9.com/2007/11/fast-datetime-parsing-in-python.html"
    global month_map
    return datetime.datetime(int(s[7:11]), month_map[s[3:6]], int(s[0:2]), \
        int(s[12:14]), int(s[15:17]), int(s[18:20]))


class Access(Document):
    ip = StringProperty()
    uri = StringProperty()
    time = DateTimeProperty()
    status_code = IntegerProperty()
    referral = StringProperty()
    agentString = StringProperty()
    bytes = IntegerProperty()


def parse(filename):
    'Return tuple of dictionaries containing file data.'
    def make_entry(x):
        a = Access ( ip = x.group('ip'),
                uri = x.group('uri'),
                time = apachetime( x.group('time') ),
                status_code = int( x.group('status_code') ),
                referral = x.group('referral'),
                agentString = x.group('agent'),
                bytes = int( x.group('bytes') ),
                )

        if x.group('agent') is not None:
            agentInfo = httpagentparser.detect( x.group('agent') )

            if 'flavor' in agentInfo:
                a['os'] = agentInfo['flavor'].keys()[0]
                a['osVersion'] = agentInfo['flavor'][a['os']]['version']

            if 'browser' in agentInfo:
                a['browser'] = agentInfo['browser'].keys()[0]
                a['browserVersion'] = agentInfo['browser'][a['browser']]['version']

            if 'bot' in agentInfo:
                a['bot'] = agentInfo['bot'].keys()[0]
                a['botVersion'] = agentInfo['bot'][a['bot']]['version']

            if 'rss_reader' in agentInfo:
                a['rssReader'] = agentInfo['rss_reader'].keys()[0]
                a['rssReaderVersion'] = agentInfo['rss_reader'][a['rssReader']]['version']

        return a

    log_re = '(?P<ip>[.\d]+) - - \[(?P<time>.*?)\] "GET (?P<uri>.*?) HTTP/1.\d" (?P<status_code>\d+) (?P<bytes>\d+) "(?P<referral>.*?)" "(?P<agent>.*?)"'
    search = re.compile(log_re).search
    for line in open( filename, 'r'):
        x = search(line)
        if x:
            yield make_entry(x)


class Bot(DetectorBase):
    info_type = "bot"
    can_register = False

class Google(Bot):
    look_for = "Googlebot"

class Netcraft(Bot):
    look_for = "NetcraftSurveyAgent"

class Yahoo(Bot):
    look_for = "Yahoo! Slurp"

class RssReader(DetectorBase):
    info_type = "rss_reader"
    can_register = False

class AideRss(RssReader):
    look_for = "AideRSS"

class NetNewsWire(RssReader):
    look_for = "NetNewsWire"


def loadDb( uri, db, filename ):
    httpagentparser.detectorshub.register( Google() )
    httpagentparser.detectorshub.register( Netcraft() )
    httpagentparser.detectorshub.register( Yahoo() )
    httpagentparser.detectorshub.register( AideRss() )
    httpagentparser.detectorshub.register( NetNewsWire() )

    s = Server( uri )
    database = s.get_or_create_db( db )
    session = create_session( s, db )

    for document in parse(filename):
        id = str( md5.new( ''.join( [document['time'].isoformat(), document['uri'], document['ip']] ) ).hexdigest() )
        document['_id'] = id
        if document['_id'] not in database:
            session(document).save()

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage="usage: %prog options")
    parser.add_option("-d", "--db", dest="db", help="The database to store the log file in")
    parser.add_option("-u", "--url", dest="url", help="The url to the couchdb")
    parser.add_option("-f", "--file", dest="file", help="The filename of the logfile to import")
    (options, args) = parser.parse_args()

    if options.db is None or options.url is None or options.file is None:
        parser.print_help()
    else:
        loadDb( options.url, options.db, options.file )

