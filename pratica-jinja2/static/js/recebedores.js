const apiUrl = "/recebedores";

document.addEventListener("DOMContentLoaded", () => {
  const btnCadastrar = document.getElementById("btnCadastrar");
  const btnCancelar = document.getElementById("btnCancelar");
  const form = document.getElementById("form");

  const nomeInput = document.getElementById("nome");
  const idadeInput = document.getElementById("idade");
  const tipoSanguineoInput = document.getElementById("tipoSanguineo");
  const motivoDoacaoInput = document.getElementById("motivoDoacao");
  const tabelaRecebedores = document.querySelector(".tabela-recebedores-body");

  let modo = "adicionar";
  let idParaEditar = null;

  async function carregarRecebedores() {
    try {
      const response = await fetch(`${apiUrl}/listar`);
      if (response.ok) {
        const recebedores = await response.json();
        console.log(recebedores);
        tabelaRecebedores.innerHTML = "";
        recebedores.forEach(recebedor => {
          const row = document.createElement("tr");
          row.innerHTML = `
            <td>${recebedor.nome}</td>
            <td>${recebedor.idade}</td>
            <td>${recebedor.tipo_sanguineo}</td>
            <td>${recebedor.necessidades_de_sangue}</td>
            <td>
                <button class="btnEditar" data-id="${recebedor.id}" type="button">Editar</button>
                <button class="btnDeletar" data-id="${recebedor.id}" type="button">Deletar</button>
            </td>
          `;
          tabelaRecebedores.appendChild(row);
        });
        adicionarEventosBotoes();
      }
    } catch (e) {
      alert("Erro ao carregar recebedores: " + e.message);
    }
  }

  function adicionarEventosBotoes() {
    document.querySelectorAll(".btnEditar").forEach(botao => {
      botao.addEventListener("click", async (e) => {
        const id = e.target.getAttribute("data-id");
        try {
          const response = await fetch(`${apiUrl}/${id}`);
          if (response.ok) {
            const recebedor = await response.json();
            nomeInput.value = recebedor.nome;
            idadeInput.value = recebedor.idade;
            tipoSanguineoInput.value = recebedor.tipo_sanguineo;
            motivoDoacaoInput.value = recebedor.necessidades_de_sangue;

            document.getElementById("form-title").textContent = "Editar Recebedor";
            form.style.display = "block";

            modo = "editar";
            idParaEditar = id;
          } else {
            alert("Não foi possível carregar os dados para edição.");
          }
        } catch (e) {
          alert("Erro ao carregar recebedor para edição: " + e.message);
        }
      });
    });

    document.querySelectorAll(".btnDeletar").forEach(botao => {
      botao.addEventListener("click", async (e) => {
        const id = e.target.getAttribute("data-id");
        if (confirm("Tem certeza que deseja deletar este recebedor?")) {
          try {
            const response = await fetch(`${apiUrl}/deletar/${id}`, {
              method: "DELETE",
            });
            if (response.ok) {
              alert("Recebedor deletado com sucesso!");
              await carregarRecebedores();
            } else {
              alert("Erro ao deletar recebedor");
            }
          } catch (e) {
            alert("Erro ao deletar: " + e.message);
          }
        }
      });
    });
  }

  async function submitForm(e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = {
      nome: formData.get("nome"),
      idade: formData.get("idade"),
      tipo_sanguineo: formData.get("tipoSanguineo"),
      necessidades_de_sangue: formData.get("motivoDoacao")
    };

    if (modo === "adicionar") {
      try {
        const response = await fetch(`${apiUrl}/adicionar`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          alert("Recebedor adicionado com sucesso!");
          form.reset();
          form.style.display = "none";
          await carregarRecebedores();
        } else {
          const error = await response.json();
          alert("Erro ao adicionar recebedor: " + (error.detail || JSON.stringify(error)));
        }
      } catch (e) {
        alert("Não foi possível adicionar ao banco: " + e.message);
      }
    } else if (modo === "editar") {
      try {
        const response = await fetch(`${apiUrl}/atualizar/${idParaEditar}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          alert("Recebedor atualizado com sucesso!");
          form.reset();
          form.style.display = "none";
          // Volta o modo para adição
          modo = "adicionar";
          idParaEditar = null;
          await carregarRecebedores();
        } else {
          const error = await response.json();
          alert("Erro ao atualizar recebedor: " + JSON.stringify(error));
        }
      } catch (e) {
        alert("Erro ao atualizar: " + e.message);
      }
    }
  }

  form.addEventListener("submit", submitForm);

  btnCadastrar.addEventListener("click", () => {
    form.reset();
    modo = "adicionar";
    idParaEditar = null;
    document.getElementById("form-title").textContent = "Adicionar Recebedor";
    form.style.display = "block";
  });

  btnCancelar.addEventListener("click", () => {
    form.style.display = "none";
  });

  carregarRecebedores();
});
