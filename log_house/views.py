# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.http import HttpResponseBadRequest

from couchdbkit.client import Server, Database, View, ViewResults
from couchdbkit.session import create_session

from log_house.decorators import ajax_required
from log_house.snippets import render_block_to_string


def generateStartKey( kwargs ):
    """
    Method for generating the startkey parameter to the CouchDB views.
    """
    key = []
    pk = []
    params = []

    params.append( kwargs['year'] )
    if kwargs.has_key( 'month' ):
        params.append( kwargs['month'] )
        if kwargs.has_key( 'day' ):
            params.append( kwargs['day'] )
            if kwargs.has_key( 'hours' ):
                params.append( kwargs['hours'] )
                if kwargs.has_key( 'minutes' ):
                    params.append( kwargs['minutes'] )

    if len(params) == 1:
        key.append( 'Y' )
        pk = ['year']
    elif len(params) == 2:
        key.append( 'M' )
        pk = ['year','month']
    elif len(params) == 3:
        key.append( 'D' )
        pk = ['year','month','day']
    elif len(params) == 4:
        key.append( 'H' )
        pk = ['year','month','day','hours']
    elif len(params) == 5:
        key.append( 'm' )
        pk = ['year','month','day','hours','minutes']

    l = [ int(kwargs[k]) for k in pk ]
    key.extend( l )
    return key


def generateEndKey( params ):
    """
    Method for generating the endkey parameter to the CouchDB views.
    """
    endkey = generateStartKey( params )
    endkey.append( {} )
    return endkey


def generalView( request, templatename,  **kwargs ):
    """
    The general view.
    """
    startkey = generateStartKey( kwargs )
    endkey = generateEndKey( kwargs )

    return render_to_response( templatename,
        kwargs,
        context_instance=RequestContext(request)
        )


def day( request, **kwargs ):
    """
    The view for day analysis.
    """
    return generalView( request, 'loghouse/dayanalysis.html', kwargs )


def getTemplateRow( row ):
    """
    Convert the CouchDB row to the one used in the templates.
    """
    result = {}
    result['payload'] = row['key'][-1]
    result['value'] = row['value']
    return result


def genericAjaxViewResult( request, viewname, divid, caption, titles, kwargs ):
    """
    A generic method for the standard couchdb views.
    """
    startkey = generateStartKey( kwargs )
    endkey = generateEndKey( kwargs )

    s = Server()
    db = create_session( s, "apache_loghouse" )
    result = db.view( viewname, wrapper=getTemplateRow, startkey=startkey, endkey=endkey, group=True )

    context = RequestContext( request, { "couchdbview": result, 
        "divid": divid, "caption": caption, "titles": titles } )

    return HttpResponse(
        render_block_to_string( 'loghouse/ajax/uris.html', 'results', context )
    )


#@ajax_required
def ajax( request, **kwargs ):
    """
    Ajax view for the uri analysis.
    """
    design = kwargs[ kwargs['design'] ]
    return genericAjaxViewResult( request,
        design['doc'],
        design['divid'],
        design['caption'],
        design['titles'],
        kwargs )


