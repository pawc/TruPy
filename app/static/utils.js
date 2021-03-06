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

        if(record.is_user_authenticated) $('#authControls').show()

        $('#recordTitle').text(record.title + ' (' + record.year + ') ')
        $('#recordLabel').text(record.label)
        $('#favIcon').attr('recordId', id)
        $('#shelfIcon').attr('recordId', id)
        $('#wishIcon').attr('recordId', id)

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

        isFavChecked = $('#favIcon').hasClass('fas')
        isFav = record.is_fav
        if((isFavChecked && !isFav) || (!isFavChecked && isFav)){
            $("#favIcon").toggleClass("far");
            $("#favIcon").toggleClass("fas");
        }

        isShelfChecked = $('#shelfIcon').hasClass('fas')
        isShelf = record.is_shelf
        if((isShelfChecked && !isShelf) || (!isShelfChecked && isShelf)){
            $("#shelfIcon").toggleClass("far");
            $("#shelfIcon").toggleClass("fas");
            $("#shelfIcon").toggleClass("fa-square");
            $("#shelfIcon").toggleClass("fa-check-square");
        }

        isWishChecked = $('#wishIcon').hasClass('fas')
        isWish = record.is_wish
        if((isWishChecked && !isWish) || (!isWishChecked && isWish)){
            $("#wishIcon").toggleClass("far");
            $("#wishIcon").toggleClass("fas");
        }

        loadingDiv(false, 'loadingDivRecord')
    })

}

function toggleFav(){
    isFavChecked = $('#favIcon').hasClass('fas')

    if(!isFavChecked){
        $.ajax({
            type: 'POST',
            url: 'fav/',
            data: {
                id: $("#favIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#favIcon").toggleClass("far");
            $("#favIcon").toggleClass("fas");
        })
    }
    else{
        $.ajax({
            type: 'POST',
            url: 'unfav/',
            data: {
                id: $("#favIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#favIcon").toggleClass("far");
            $("#favIcon").toggleClass("fas");
        })
    }

}

function toggleShelf(){
    isShelfChecked = $('#shelfIcon').hasClass('fas')

    if(!isShelfChecked){
        $.ajax({
            type: 'POST',
            url: 'shelf/',
            data: {
                id: $("#shelfIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#shelfIcon").toggleClass("far");
            $("#shelfIcon").toggleClass("fas");
            $("#shelfIcon").toggleClass("fa-square");
            $("#shelfIcon").toggleClass("fa-check-square");
        })
    }
    else{
        $.ajax({
            type: 'POST',
            url: 'unshelf/',
            data: {
                id: $("#shelfIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#shelfIcon").toggleClass("far");
            $("#shelfIcon").toggleClass("fas");
            $("#shelfIcon").toggleClass("fa-square");
            $("#shelfIcon").toggleClass("fa-check-square");
        })
    }

}

function toggleWish(){
    isWishChecked = $('#wishIcon').hasClass('fas')

    if(!isWishChecked){
        $.ajax({
            type: 'POST',
            url: 'wish/',
            data: {
                id: $("#wishIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#wishIcon").toggleClass("far");
            $("#wishIcon").toggleClass("fas");
        })
    }
    else{
        $.ajax({
            type: 'POST',
            url: 'unwish/',
            data: {
                id: $("#wishIcon").attr('recordId')
            },
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => {
            $("#wishIcon").toggleClass("far");
            $("#wishIcon").toggleClass("fas");
        })
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getFavs(){
    loadingDiv(true, 'loadingDivBrowse');
    $('#searchDiv').hide();
    $('#shelfDiv').hide();
    $('#wishDiv').hide();
    $('#favDiv').show();
    $("#results").empty();
    $.ajax({
        url: 'getFavs'
    })
    .then(response => {
        if(response.length == 0){
            $("#results").append('No records marked as fav yet :(');
        }
        else{
            $("#results").append("<tbody>")
            $.each(response, (i, record) => {
                $("#results").append('<tr><td><a href="#" onclick="setArtist('+record.artistId+');setRecord('+record.recordId+');">'+record.artist+' - '+record.title+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        loadingDiv(false, 'loadingDivBrowse')
    })
}

function getShelf(){
    loadingDiv(true, 'loadingDivBrowse');
    $('#searchDiv').hide();
    $('#favDiv').hide();
    $('#wishDiv').hide();
    $('#shelfDiv').show();
    $("#results").empty();
    $.ajax({
        url: 'getShelf'
    })
    .then(response => {
        if(response.length == 0){
            $("#results").append('No records on shelf yet :(');
        }
        else{
            $("#results").append("<tbody>")
            $.each(response, (i, record) => {
                $("#results").append('<tr><td><a href="#" onclick="setArtist('+record.artistId+');setRecord('+record.recordId+');">'+record.artist+' - '+record.title+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        loadingDiv(false, 'loadingDivBrowse')
    })
}

function getWish(){
    loadingDiv(true, 'loadingDivBrowse');
    $('#searchDiv').hide();
    $('#favDiv').hide();
    $('#shelfDiv').hide();
    $('#wishDiv').show();
    $("#results").empty();
    $.ajax({
        url: 'getWish'
    })
    .then(response => {
        if(response.length == 0){
            $("#results").append('No records on wish list yet :(');
        }
        else{
            $("#results").append("<tbody>")
            $.each(response, (i, record) => {
                $("#results").append('<tr><td><a href="#" onclick="setArtist('+record.artistId+');setRecord('+record.recordId+');">'+record.artist+' - '+record.title+'</a></td></tr>');
            })
            $("#results").append("</tbody>")
        }
        loadingDiv(false, 'loadingDivBrowse')
    })
}