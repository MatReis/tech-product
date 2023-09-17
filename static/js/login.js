$(document).ready(function() {
    $("#login-form").submit(function(event) {
        var username = $("#username").val();
        var password = $("#password").val();

        if (!username || !password) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Por favor, preencha o usario e a senha.'
            });
            event.preventDefault();
        }
    });
});