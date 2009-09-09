function(doc) {
    // !code _attachments/lib/helper/parsedate.js
    if( doc.browser && doc.browserVersion && doc.time ) {
        var d = new Date();
        d.setISO8601( doc.time );
        emit( ['m', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), doc.browser+" "+doc.browserVersion], 1 );
        emit( ['H', d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), doc.browser+" "+doc.browserVersion], 1 );
        emit( ['D', d.getFullYear(), d.getMonth(), d.getDate(), doc.browser+" "+doc.browserVersion], 1 );
        emit( ['M', d.getFullYear(), d.getMonth(), doc.browser+" "+doc.browserVersion], 1 );
        emit( ['Y', d.getFullYear(), doc.browser+" "+doc.browserVersion], 1 );
    }
}
