$(document).ready(function() {

    $('#searchLink').click(() => {
        $('#searchDiv').show();
        $('#favDiv').hide();
        $('#wishDiv').hide();
        $('#shelfDiv').hide();
        $('#results').empty();
    })

    loadingDiv(false, 'loadingDivBrowse')
    loadingDiv(false, 'loadingDivArtist')
    loadingDiv(false, 'loadingDivRecord')
    $('#favDiv').hide();
    $('#shelfDiv').hide();
    $('#wishDiv').hide();

    $('#artistName').keyup(function(e){
        if(e.keyCode == 13) getArtists();
    });

    $('#logout').click(() => {
        $.ajax({
            type: 'POST',
            url: '/logout/',
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            location.reload();
        })
    })

    $('#favIcon').click(() => {toggleFav();})
    $('#wishIcon').click(() => {toggleWish();})
    $('#shelfIcon').click(() => {toggleShelf();})

    $('#favLink').click(() => {getFavs();})
    $('#wishLink').click(() => {getWish();})
    $('#shelfLink').click(() => {getShelf();})

    chooseArtist(1439605)
    setArtist(1439605)
    setRecord(670664)

});