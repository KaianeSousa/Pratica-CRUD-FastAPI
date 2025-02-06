document.addEventListener('DOMContentLoaded', () => {
  const formulario = document.getElementById('formulario');

  formulario.addEventListener('submit', async (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const dadosLogin = {
      email: email,
      senha: password
    };

    try {
      const response = await fetch('http://localhost:8000/admin/admin/login', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosLogin)
      });

      if (response.ok) {
        const data = await response.json();

        localStorage.setItem('access_token', data.access_token);

        alert('Login realizado com sucesso!');

        window.location.href = '/home';
      } else {
        const error = await response.json();
        alert(`Erro ao realizar login: ${error.detail || 'Erro desconhecido'}`);
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      alert('Erro ao realizar login. Por favor, tente novamente mais tarde.');
    }
  });
});
