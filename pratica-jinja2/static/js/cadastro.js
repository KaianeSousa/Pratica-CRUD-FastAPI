document.getElementById("btnCadastrar").addEventListener("click", async function () {
    const nome = document.getElementById("nome").value;
    const idade = document.getElementById("idade").value;
    const tipoSanguineo = document.getElementById("tipo_sanguineo").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const papel = document.getElementById("papel").value;

    if (!nome || !idade || !tipoSanguineo || !email || !senha || !papel) {
        alert("Preencha todos os campos!");
        return;
    }

    const response = await fetch("/auth/cadastrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, idade, tipo_sanguineo: tipoSanguineo, email, senha, papel })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Cadastro realizado com sucesso!");
        window.location.href = "/login";
    } else {
        alert(data.detail || "Erro ao cadastrar!");
    }
});
