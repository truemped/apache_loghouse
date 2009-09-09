function(doc) {
    // !code _attachments/lib/helper/parsedate.js
    if( doc.bot && doc.botVersion && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.bot+" "+doc.botVersion], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.bot+" "+doc.botVersion], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.bot+" "+doc.botVersion], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.bot+" "+doc.botVersion], 1 );
        emit( ['Y', d.getFullYear(), doc.bot+" "+doc.botVersion], 1 );
    }
}
