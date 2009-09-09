function(doc) {
    // !code _attachments/lib/helper/parsedate.js
    if( doc.os && doc.osVersion && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.os + " " + doc.osVersion], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.os + " " + doc.osVersion], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.os + " " + doc.osVersion], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.os + " " + doc.osVersion], 1 );
        emit( ['Y', d.getFullYear(), doc.os + " " + doc.osVersion], 1 );
    }
}
