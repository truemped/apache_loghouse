
var viewPageSize = 5;

var currentReferrerStart = 0;
var currentReferrerEnd = 5;

var currentUrisStart = 0;
var currentUrisEnd = 5;

var currentCodesStart = 0;
var currentCodesEnd = 5;

var currentBytesStart = 0;
var currentBytesEnd = 5;

orderResultsPerValue = function( results ) {
    results.rows.sort( function(a,b) {
        return b.value - a.value;
    });
}

updatePicker = function( year, month, day ) {
    $("#picker").empty();
    $("#picker").append( "/ <a href=\"javascript:resetYearView("+year+")\">"+year+"</a>" );
    if( month != null ) {
        var displayMonth = month + 1;
        $("#picker").append( " / <a href=\"javascript:resetMonthView("+year+","+month+")\">"+displayMonth+"</a>" );
        if( day != null ) {
            $("#picker").append( " / <a href=\"javascript:resetDayView("+year+","+month+","+day+")\">"+day+"</a>" );
        }
    }
}

updateView = function( view, startkey, endkey, startItem, endItem, tableId, nextPage ) {
    $.CouchApp( function(app) {
        options = {};
        options.group_level = endkey.length;
        options.startkey = startkey;
        options.endkey = endkey;
        options.success = function( data ) {
            orderResultsPerValue( data );
            for( var i=startItem; i<data.rows.length && i<endItem; i++ ) {
                var key = data.rows[i].key;
                $(tableId+" tbody").append("<tr> <td>"+data.rows[i].value+"</td> <td>"+key[key.length - 1]+"</td> </tr>");
            }
            if( i < data.rows.length ) {
                $(tableId+" tfoot tr").remove();
                $(tableId+" tfoot").append( nextPage );
            }
        };
        app.view( view, options );
    });
}


/*
 * Update all views.
 */
resetDayView = function( year, month, day ) {
    resetReferrerDayView( year, month, day );
    resetUrisDayView( year, month, day );
    resetCodesDayView( year, month, day );
    resetBytesDayView( year, month, day );
}

resetMonthView = function( year, month ) {
    resetReferrerMonthView( year, month );
    resetUrisMonthView( year, month );
    resetCodesMonthView( year, month );
    resetBytesMonthView( year, month );
}

resetYearView = function( year ) {
    resetReferrerYearView( year );
    resetUrisYearView( year );
    resetCodesYearView( year );
    resetBytesYearView( year );
}


/****************************
 * URIs views.
 ****************************/
/*
 * Year view for URIs.
 */
updateUrisYearView = function( year, start, end ) {
    updateView( "uris",
        ["Y",year],
        ["Y",year,{}],
        start,
        end,
        "#urisTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextUrisYearPage("+year+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextUrisYearPage = function( year ) {
    this.currentUrisStart += this.viewPageSize;
    this.currentUrisEnd += this.viewPageSize;
    updateUrisYearView( year, this.currentUrisStart, this.currentUrisEnd );
}

resetUrisYearView = function( year ) {
    this.currentUrisStart = 0;
    this.currentUrisEnd = 5;
    $("#urisTable tbody tr").remove();
    updateUrisYearView( year, this.currentUrisStart, this.currentUrisEnd );
}


/*
 * Month view for URIs.
 */
updateUrisMonthView = function( year, month, start, end ) {
    updateView( "uris",
        ["M",year,month],
        ["M",year,month,{}],
        start,
        end,
        "#urisTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextUrisMonthPage("+year+","+month+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextUrisMonthPage = function( year, month ) {
    this.currentUrisStart += this.viewPageSize;
    this.currentUrisEnd += this.viewPageSize;
    updateUrisMonthView( year, month, this.currentUrisStart, this.currentUrisEnd );
}

resetUrisMonthView = function( year, month ) {
    this.currentUrisStart = 0;
    this.currentUrisEnd = 5;
    $("#urisTable tbody tr").remove();
    updateUrisMonthView( year, month, this.currentUrisStart, this.currentUrisEnd );
}


/*
 * Day view for URIs.
 */
updateUrisDayView = function( year, month, day, start, end ) {
    updateView( "uris",
        ["D",year,month,day],
        ["D",year,month,day,{}],
        start,
        end,
        "#urisTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextUrisDayPage("+year+","+month+","+day+");\">more</a></td> </tr>");
    updatePicker( year, month, day );
}

showNextUrisDayPage = function( year, month, day ) {
    this.currentUrisStart += this.viewPageSize;
    this.currentUrisEnd += this.viewPageSize;
    updateUrisDayView( year, month, day, this.currentUrisStart, this.currentUrisEnd );
}

resetUrisDayView = function( year, month, day ) {
    this.currentUrisStart = 0;
    this.currentUrisEnd = 5;
    $("#urisTable tbody tr").remove();
    updateUrisDayView( year, month, day, this.currentUrisStart, this.currentUrisEnd );
}


/****************************
 * Status Codes views.
 ****************************/
/*
 * Year view for Status Codes.
 */
updateCodesYearView = function( year, start, end ) {
    updateView( "statusCodes",
        ["Y",year],
        ["Y",year,{}],
        start,
        end,
        "#codesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextCodesYearPage("+year+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextCodesYearPage = function( year ) {
    this.currentCodesStart += this.viewPageSize;
    this.currentCodesEnd += this.viewPageSize;
    updateCodesYearView( year, this.currentCodesStart, this.currentCodesEnd );
}

resetCodesYearView = function( year ) {
    this.currentCodesStart = 0;
    this.currentCodesEnd = 5;
    $("#codesTable tbody tr").remove();
    updateCodesYearView( year, this.currentCodesStart, this.currentCodesEnd );
}


/*
 * Month view for URIs.
 */
updateCodesMonthView = function( year, month, start, end ) {
    updateView( "statusCodes",
        ["M",year,month],
        ["M",year,month,{}],
        start,
        end,
        "#codesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextCodesMonthPage("+year+","+month+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextCodesMonthPage = function( year, month ) {
    this.currentReferrerStart += this.viewPageSize;
    this.currentReferrerEnd += this.viewPageSize;
    updateCodesMonthView( year, month, this.currentReferrerStart, this.currentReferrerEnd );
}

resetCodesMonthView = function( year, month ) {
    this.currentCodesStart = 0;
    this.currentCodesEnd = 5;
    $("#codesTable tbody tr").remove();
    updateCodesMonthView( year, month, this.currentCodesStart, this.currentCodesEnd );
}


/*
 * Day view for URIs.
 */
updateCodesDayView = function( year, month, day, start, end ) {
    updateView( "statusCodes",
        ["D",year,month,day],
        ["D",year,month,day,{}],
        start,
        end,
        "#codesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextCodesDayPage("+year+","+month+","+day+");\">more</a></td> </tr>");
    updatePicker( year, month, day );
}

showNextCodesDayPage = function( year, month, day ) {
    this.currentCodesStart += this.viewPageSize;
    this.currentCodesEnd += this.viewPageSize;
    updateCodesDayView( year, month, day, this.currentCodesStart, this.currentCodesEnd );
}

resetCodesDayView = function( year, month, day ) {
    this.currentCodesStart = 0;
    this.currentCodesEnd = 5;
    $("#codesTable tbody tr").remove();
    updateCodesDayView( year, month, day, this.currentCodesStart, this.currentCodesEnd );
}


/****************************
 * Referrer views.
 ****************************/
/*
 * Year view for referrers.
 */
updateReferrerYearView = function( year, start, end ) {
    updateView( "referrer",
        ["Y",year],
        ["Y",year,{}],
        start,
        end,
        "#referrerTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextReferrerYearPage("+year+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextReferrerYearPage = function( year ) {
    this.currentReferrerStart += this.viewPageSize;
    this.currentReferrerEnd += this.viewPageSize;
    updateReferrerYearView( year, this.currentReferrerStart, this.currentReferrerEnd );
}

resetReferrerYearView = function( year ) {
    this.currentReferrerStart = 0;
    this.currentReferrerEnd = 5;
    $("#referrerTable tbody tr").remove();
    updateReferrerYearView( year, this.currentReferrerStart, this.currentReferrerEnd );
}


/*
 * Month view for referrers.
 */
updateReferrerMonthView = function( year, month, start, end ) {
    updateView( "referrer",
        ["M",year,month],
        ["M",year,month,{}],
        start,
        end,
        "#referrerTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextReferrerMonthPage("+year+","+month+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextReferrerMonthPage = function( year, month ) {
    this.currentReferrerStart += this.viewPageSize;
    this.currentReferrerEnd += this.viewPageSize;
    updateReferrerMonthView( year, month, this.currentReferrerStart, this.currentReferrerEnd );
}

resetReferrerMonthView = function( year, month ) {
    this.currentReferrerStart = 0;
    this.currentReferrerEnd = 5;
    $("#referrerTable tbody tr").remove();
    updateReferrerMonthView( year, month, this.currentReferrerStart, this.currentReferrerEnd );
}


/*
 * Day view for referrers.
 */
updateReferrerDayView = function( year, month, day, start, end ) {
    updateView( "referrer",
        ["D",year,month,day],
        ["D",year,month,day,{}],
        start,
        end,
        "#referrerTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextReferrerDayPage("+year+","+month+","+day+");\">more</a></td> </tr>");
    updatePicker( year, month, day );
}

showNextReferrerDayPage = function( year, month, day ) {
    this.currentReferrerStart += this.viewPageSize;
    this.currentReferrerEnd += this.viewPageSize;
    updateReferrerDayView( year, month, day, this.currentReferrerStart, this.currentReferrerEnd );
}

resetReferrerDayView = function( year, month, day ) {
    this.currentReferrerStart = 0;
    this.currentReferrerEnd = 5;
    $("#referrerTable tbody tr").remove();
    updateReferrerDayView( year, month, day, this.currentReferrerStart, this.currentReferrerEnd );
}


/****************************
 * Byte Usage views.
 ****************************/
/*
 * Year view for bytes.
 */
updateBytesYearView = function( year, start, end ) {
    updateView( "byteUsage",
        ["Y",year],
        ["Y",year,{}],
        start,
        end,
        "#bytesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextBytesYearPage("+year+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextBytesYearPage = function( year ) {
    this.currentBytesStart += this.viewPageSize;
    this.currentBytesEnd += this.viewPageSize;
    updateBytesYearView( year, this.currentBytesStart, this.currentBytesEnd );
}

resetBytesYearView = function( year ) {
    this.currentBytesStart = 0;
    this.currentBytesEnd = 5;
    $("#bytesTable tbody tr").remove();
    updateBytesYearView( year, this.currentBytesStart, this.currentBytesEnd );
}


/*
 * Month view for bytes.
 */
updateBytesMonthView = function( year, month, start, end ) {
    updateView( "byteUsage",
        ["M",year,month],
        ["M",year,month,{}],
        start,
        end,
        "#bytesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextBytesMonthPage("+year+","+month+");\">more</a></td> </tr>");
    updatePicker( year, month, null );
}

showNextBytesMonthPage = function( year, month ) {
    this.currentBytesStart += this.viewPageSize;
    this.currentBytesEnd += this.viewPageSize;
    updateBytesMonthView( year, month, this.currentBytesStart, this.currentBytesEnd );
}

resetBytesMonthView = function( year, month ) {
    this.currentBytesStart = 0;
    this.currentBytesEnd = 5;
    $("#bytesTable tbody tr").remove();
    updateBytesMonthView( year, month, this.currentBytesStart, this.currentBytesEnd );
}


/*
 * Day view for bytes.
 */
updateBytesDayView = function( year, month, day, start, end ) {
    updateView( "byteUsage",
        ["D",year,month,day],
        ["D",year,month,day,{}],
        start,
        end,
        "#bytesTable",
        "<tr> <td valign=\"right\" colspan=\"2\"><a href=\"javascript:showNextBytesDayPage("+year+","+month+","+day+");\">more</a></td> </tr>");
    updatePicker( year, month, day );
}

showNextBytesDayPage = function( year, month, day ) {
    this.currentBytesStart += this.viewPageSize;
    this.currentBytesEnd += this.viewPageSize;
    updateBytesDayView( year, month, day, this.currentBytesStart, this.currentBytesEnd );
}

resetBytesDayView = function( year, month, day ) {
    this.currentBytesStart = 0;
    this.currentBytesEnd = 5;
    $("#bytesTable tbody tr").remove();
    updateBytesDayView( year, month, day, this.currentBytesStart, this.currentBytesEnd );
}


