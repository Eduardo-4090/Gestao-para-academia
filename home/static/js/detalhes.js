document.addEventListener('DOMContentLoaded',() => {
    const form = document.getElementById('form_edicao');
    const campos =form.querySelectorAll('input ,textarea');
    const btnSalvar = document.getElementById('Salvar');
    const btnEditar = document.getElementById('Editar')

    campos.forEach(campo => campo.disabled = true);
    btnSalvar.style.display = 'none';
    
    btnEditar.addEventListener('click', () => {
        campos.forEach(campo => campo.disabled = false);
        btnSalvar.style.display = 'inline';
        btnEditar.style.display = 'none';
   
         const cpf = document.querySelector('.cpf_rg');
         const celular = document.querySelector('.celular');
    
         celular.disabled = true
         cpf.disabled = true
         
    });
    document.querySelector('.Excluir').addEventListener('click', (e) => {
    if (!confirm("Tem certeza que deseja excluir este aluno?")) {
        e.preventDefault();
    }
});
});