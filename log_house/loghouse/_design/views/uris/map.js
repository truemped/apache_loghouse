function(doc) {
    // !code lib/helpers/parsedate.js
    if( doc.uri && doc.status_code && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.uri], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.uri], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.uri], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.uri], 1 );
        emit( ['Y', d.getFullYear(), doc.uri], 1 );
    }
}
