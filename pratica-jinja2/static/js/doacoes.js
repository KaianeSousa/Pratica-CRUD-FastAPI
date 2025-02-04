document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formDoacao');
    const tabela = document.getElementById('tabelaCompatibilidade').getElementsByTagName('tbody')[0];

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const doadorId = document.getElementById('doador_id').value;
        const recebedorId = document.getElementById('recebedor_id').value;

        fetch('/doacoes/adicionar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                doador_id: parseInt(doadorId),
                recebedor_id: parseInt(recebedorId),
            }),
        })
        .then(response => response.json())
        .then(data => {
        
            tabela.innerHTML = '';

            const row = tabela.insertRow();
            row.insertCell().textContent = data.doador.id;
            row.insertCell().textContent = data.doador.nome;
            row.insertCell().textContent = data.doador.tipo_sanguineo;
            row.insertCell().textContent = data.recebedor.id;
            row.insertCell().textContent = data.recebedor.nome;
            row.insertCell().textContent = data.recebedor.tipo_sanguineo;
            row.insertCell().textContent = data.compativel ? "Sim" : "Não";

            alert(data.mensagem);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});