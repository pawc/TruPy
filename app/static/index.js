$(document).ready(function() {
    $('#artistName').keyup(function(e){
        if(e.keyCode == 13) getArtists();
    });
    $('#logout').click(() => {
        $.ajax({
            type: 'POST',
            url: '/logout/'
        })
        .then(() => {
            location.reload();
        })
    })
});

function getArtists(){
    $('#artistName').attr('disabled', 'disabled');
    var artist = $('#artistName').val();
    $.ajax({
        url: 'getArtists',
        data: {
            artist : artist
        }
    })
    .then(response => {
        $("#results").empty();
        if(response.length == 0){
            $("#artists").append('Nie znaleziono wyników :(');
        }
        else{
            $("#results").append("<tbody>")
            $.each(response, (i, artist) => {
                $("#results").append('<tr><td><a href="#" onclick="chooseArtist('+artist.id+', 2)">'+artist.name+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        $('#artistName').removeAttr('disabled');

    })
}

function getReleases(){
    $('#artistName').attr('disabled', 'disabled');
    var artist = $('#artistName').val();
    $.ajax({
        url: 'getReleases',
        data: {
            artist : artist
        }
    })
    .then(response => {
        $("#releases").empty();
        if(response.length == 0){
            $("#releases").append('Nie znaleziono wyników :(');
        }
        else{
            $("#releases").append("<tbody>")
            $.each(response, (i, release) => {
                $("#releases").append('<tr><td><a href="#" onclick="loadIframe('+release.id+')">'+release.title+'</a></td></tr>');
            })
            $("#releases").append("</tbody>")
        }
        $('#artistName').removeAttr('disabled');

    })
}

function loadIframe(id, type) {
    var $iframe
    if(type == 1){
        url = 'getRelease/?id='+id
        $iframe = $('#releasePreview');
    }
    else{
        url = 'getArtist/?id='+id
        $iframe = $('#artistPreview');
    }
    if ( $iframe.length ) {
        $iframe.attr('src',url);
        return false;
    }
    return true;
}

function chooseArtist(artistId){
    $("#results").empty();
    loadIframe(artistId, 2)
    $.ajax({
        url: 'getReleasesByArtistsId',
        data: {
            artistId: artistId
        }
    })
    .then(releases => {

        if(releases.length == 0){
            $("#results").append('Not releases found :(');
        }
        else{
            $("#results").append("<tbody>")
            $.each(releases, (i, release) => {
                $("#results").append('<tr><td><a href="#" onclick="loadIframe('+release.id+', 1)">'+release.title+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        console.log(release)

    })
}


