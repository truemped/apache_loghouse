function(doc) {
    // !code lib/helpers/parsedate.js
    if( doc.bytes && doc.status_code && doc.status_code == 200 && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes()], doc.bytes );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours()], doc.bytes );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate()], doc.bytes );
        emit( ['M', d.getFullYear(), d.getMonth()], doc.bytes );
        emit( ['Y', d.getFullYear()], doc.bytes );
    }
}
