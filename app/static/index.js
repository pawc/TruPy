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
            url: '/logout/',
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            location.reload();
        })
    })

    chooseArtist(1439605)
    setArtist(1439605)
    setRecord(670664)

    $('#favIcon').click(() => {toggleFav();})
    $('#wishIcon').click(() => {toggleWish();})
    $('#shelfIcon').click(() => {toggleShelf();})

});