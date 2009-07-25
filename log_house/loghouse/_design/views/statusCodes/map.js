function(doc) {
    // !code lib/helpers/parsedate.js
    if( doc.status_code && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.status_code], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.status_code], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.status_code], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.status_code], 1 );
        emit( ['Y', d.getFullYear(), doc.status_code], 1 );
    }
}
