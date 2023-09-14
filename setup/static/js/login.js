$(document).ready(function () {
    console.log("here");
    $("#form_login").submit(function (event) {
        // Impedir o envio do formulário por padrão
        event.preventDefault();

        // Coloque suas validações aqui
        var username = $("#username").val();
        var password = $("#password").val();

        if (username === "") {
            alert("Por favor, insira um nome de usuário.");
            return;
        }

        if (password === "") {
            alert("Por favor, insira uma senha.");
            return;
        }

        // Se as validações passarem, envie o formulário
        this.submit();
    });
});