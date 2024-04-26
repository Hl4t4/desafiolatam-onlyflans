$(document).ready( function() {
    var modal = document.getElementById('loginErrorModal');
    $("#loginErrorModalClose").on('click', function() {
        modal.classList.remove('show');
        modal.classList.remove('d-block'); 
    });

    // Modificar en caso de encontrar mejor alternativa
    $('.nav-toggle').click(function () {
        var card = document.getElementById($(this).attr('href').substring(1));
        if ($(this).html() == 'Ver menos') {
            card.style.maxHeight = '70%'
            $(this).html('Ver más');
        } else {
            card.style.maxHeight = '100%'
            $(this).html('Ver menos');
        }
    });
});