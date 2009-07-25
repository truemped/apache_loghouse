function(doc) {
    // !code lib/helpers/parsedate.js
    if( doc.agent && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.agent], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.agent], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.agent], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.agent], 1 );
        emit( ['Y', d.getFullYear(), doc.agent], 1 );
    }
}
