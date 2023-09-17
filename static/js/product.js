$(document).ready(function() {
    $('#productForm').submit(function(event) {
        event.preventDefault();

        var name = $('#name').val();
        var provider = $('#provider').val();
        var value = $('#value').val();

        if (!name.trim()) {
            Swal.fire('Ops!', 'O campo "Nome" não pode estar vazio.', 'error');
            return;
        }
        if (!provider.trim()) {
            Swal.fire('Ops!', 'O campo "Fornecedor" não pode estar vazio.', 'error');
            return;
        }
        if (!value.trim()) {
            Swal.fire('Ops!', 'O campo "Valor" não pode estar vazio.', 'error');
            return;
        }

        $('#value').val(removeMaskMoney(value));

        this.submit();

    });

    $('#value').on('input', function() {
        const value = $(this).val();
        console.log(value);
        $(this).val(addMaskMoney(
            value
        ));
    });
});

function deletar(id) {
    Swal.fire({
        title: 'Realmente deseja deletar item '+id+'?',
        text: "Essa ação é irreversivel!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Excluir!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/produto/deletar/"+id;
        }
    }); 
}