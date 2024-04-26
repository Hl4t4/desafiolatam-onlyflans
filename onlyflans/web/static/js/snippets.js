$(document).ready( function() {
    var modal = document.getElementById('loginErrorModal');
    $("#loginErrorModalClose").on('click', function() {
        modal.classList.remove('show');
        modal.classList.remove('d-block'); 
    });
});