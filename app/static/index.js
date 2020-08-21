$(document).ready(function() {
    $('#artistName').keyup(function(e){
        if(e.keyCode == 13) getReleases();
    });
});

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
            $.each(response, (i, release) => {
                $("#releases").append('<li><a href="#" onclick="loadIframe('+release.id+')">'+release.title+'</a></li>');
            })
        }
        $('#artistName').removeAttr('disabled');

    })
}

function loadIframe(id) {
    url = 'getRelease/?id='+id
    var $iframe = $('#releasePreview');
    if ( $iframe.length ) {
        $iframe.attr('src',url);
        return false;
    }
    return true;
}

