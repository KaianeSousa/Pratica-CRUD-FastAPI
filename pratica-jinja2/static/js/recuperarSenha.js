document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const novaSenha = document.getElementById('senha').value;

        fetch('/auth/recuperar-senha', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email, nova_senha: novaSenha }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensagem) {
                alert(data.mensagem);
                window.location.href = '/';
            } else {
                alert('Erro ao redefinir senha.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});