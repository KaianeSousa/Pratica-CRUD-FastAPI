document.addEventListener('DOMContentLoaded', () => {
  const formulario = document.getElementById('formulario');

  formulario.addEventListener('submit', async (event) => {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const dadosCadastro = {
      nome: nome,
      email: email,
      senha: password,
    };

    try {
      const response = await fetch('http://localhost:8000/admin/admin', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosCadastro),
      });

      if (response.ok) {
        alert('Cadastro realizado com sucesso!');
        const data = await response.json();
        localStorage.setItem('access_token', data.access_token);
        window.location.href = '/home';
      } else {
        const erro = await response.json();
        alert(`Erro ao realizar cadastro: ${erro.message || 'Erro desconhecido'}`);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      alert('Erro ao realizar cadastro. Por favor, tente novamente mais tarde.');
    }
  });
});
