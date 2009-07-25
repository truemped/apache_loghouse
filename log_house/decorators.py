#
# Copyright (c) 2008 Daniel Truemper truemped@googlemail.com
#
# decorators.py 26-Jul-2009
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


#
# downloaded from http://www.djangosnippets.org/snippets/771/
#
from django.http import HttpResponseBadRequest

def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....
    """    
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

