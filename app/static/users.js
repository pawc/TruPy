$(document).ready(function() {
    getUsers();

    $('#searchLink').click(() => {
        location.replace('/')
    })
});

function getUsers(){
    loadingDiv(true, 'loadingDivBrowse');
    //var artist = $('#artistName').val();
    $.ajax({
        url: '/getUsers'
    })
    .then(users => {
        $("#users").empty();
        $("#users").append("<tbody>")
        $.each(users, (i, user) => {
            $("#users").append('<tr><td><a href="#">'+user.name+'</a></td></tr>');
        })
        $("#users").append("</tbody>")
        loadingDiv(false, 'loadingDivBrowse')
    })
}