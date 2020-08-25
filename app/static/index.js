$(document).ready(function() {

    loadingDiv(false, 'loadingDivBrowse')
    loadingDiv(false, 'loadingDivArtist')
    loadingDiv(false, 'loadingDivRecord')

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

    setArtist(1439605)
    setRecord(670664)

    $('#favIcon').click(() => {toggleFav();})
    $('#wishIcon').click(() => {toggleWish();})
    $('#shelfIcon').click(() => {toggleShelf();})
});

function getArtists(){
    loadingDiv(true, 'loadingDivBrowse');
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
        loadingDiv(false, 'loadingDivBrowse')
    })
}

function chooseArtist(artistId){
    loadingDiv(true, 'loadingDivBrowse')
    setArtist(artistId)
    $("#results").empty();

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
                $("#results").append('<tr><td><a href="#" onclick="setRecord('+release.id+')">'+release.title+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        loadingDiv(false, 'loadingDivBrowse')
    })
}

function loadingDiv(isOn, loadingDivId){
    if(isOn){
        $('#artistName').attr('disabled', 'disabled');
        $('#'+loadingDivId).show();
    }
    else{
        $('#artistName').removeAttr('disabled');
        $('#'+loadingDivId).hide();
    }
}

function setArtist(id){
    loadingDiv(true, 'loadingDivArtist')
    $.ajax({
        url: 'getArtist',
        data: {
            id : id
        }
    })
    .then(artist => {
        $('#artistName').val(artist.name)
        $('#artistTitle').text(artist.name)
        $('#artistProfile').text(artist.profile)
        $('#artistImg').attr('src', artist.img_url);
        loadingDiv(false, 'loadingDivArtist')
    })

}

function setRecord(id){
    loadingDiv(true, 'loadingDivRecord')
    $.ajax({
        url: 'getRecord',
        data: {
            id : id
        }
    })
    .then(record => {
        $('#recordTitle').text(record.title + ' (' + record.year + ') ')
        $('#recordLabel').text(record.label)

        if(record.img_url != 'not found'){
            $('#recordImg').attr('src', record.img_url);
        }
        else{
            $('#recordImg').removeAttr('src');
        }

        $('#recordTracks').empty()
        if(record.tracks != 'not found'){
            $.each(record.tracks, (i, track) => {
                $('#recordTracks').append('<li>'+track+'</li>')
            })
        }

        loadingDiv(false, 'loadingDivRecord')
    })

}

function toggleFav(){
    $("#favIcon").toggleClass("far");
    $("#favIcon").toggleClass("fas");
}

function toggleShelf(){
    $("#shelfIcon").toggleClass("far");
    $("#shelfIcon").toggleClass("fas");
    $("#shelfIcon").toggleClass("fa-square");
    $("#shelfIcon").toggleClass("fa-check-square");
}

function toggleWish(){
    $("#wishIcon").toggleClass("far");
    $("#wishIcon").toggleClass("fas");
}