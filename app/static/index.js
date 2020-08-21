$(document).ready(function() {
    $('#artistName').keyup(function(e){
        if(e.keyCode == 13) getReleases();
    });
});

function getReleases(){
    var artist = $('#artistName').val();
    $.ajax({
        url: '/trupy/getReleases',
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
                $("#releases").append('<li>'+release+'</li>');
            })
        }

    })
}