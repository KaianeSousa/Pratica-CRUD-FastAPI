document.getElementById("btnLogin").addEventListener("click", async function () {
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    if (!email || !senha) {
        alert("Preencha todos os campos!");
        return;
    }

    const response = await fetch("/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, senha })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/index";
    } else {
        alert(data.detail || "Erro ao fazer login!");
    }
});
