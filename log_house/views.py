# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.http import HttpResponseForbidden

from couchdbkit.client import Server, Database, View, ViewResults
from couchdbkit.session import create_session

from decorators import ajax_required
from snippets import render_block_to_string
from settings import COUCHDB_SERVER, COUCHDB_DATABASE, COUCHDB_QUERIES


def generateStartKey( kwargs ):
    """
    Method for generating the startkey parameter to the CouchDB views.
    """
    params = []

    pk = "Y"
    params.append( int(kwargs['year']) )
    if kwargs.has_key( 'month' ):
        pk = "M"
        params.append( int(kwargs['month']) )
        if kwargs.has_key( 'day' ):
            pk = "D"
            params.append( int(kwargs['day']) )
            if kwargs.has_key( 'hours' ):
                pk = "H"
                params.append( int(kwargs['hours']) )
                if kwargs.has_key( 'minutes' ):
                    pk = "m"
                    params.append( int(kwargs['minutes']) )

    key = []
    key.append( pk )
    key.extend( params )
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
    kwargs["couchdbqueries"] = COUCHDB_QUERIES.keys()

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

    server = Server( COUCHDB_SERVER )
    db = create_session( server, COUCHDB_DATABASE )
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
    if kwargs['design'] not in COUCHDB_QUERIES:
        return  HttpResponseForbidden()

    design = kwargs[ kwargs['design'] ]
    return genericAjaxViewResult( request,
        design['doc'],
        design['divid'],
        design['caption'],
        design['titles'],
        kwargs )


