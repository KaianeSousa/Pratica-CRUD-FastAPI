document.getElementById("btnEnviar").addEventListener("click", async function (event) {
    event.preventDefault();
    
    const email = document.getElementById("email").value;

    if (!email) {
        alert("Preencha o e-mail!");
        return;
    }

    const response = await fetch("/auth/recuperar_senha", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Um link de redefinição foi enviado para seu e-mail.");
        window.location.href = "/login";
    } else {
        alert(data.detail || "Erro ao solicitar recuperação de senha!");
    }
});
