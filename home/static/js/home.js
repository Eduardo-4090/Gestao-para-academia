
document.addEventListener('DOMContentLoaded',() =>{
    
    const input = document.getElementById('pesquisa');
    const linhas = document.querySelectorAll('#cores'); // todas as linhas com a classe "cores"

    input.addEventListener('keyup', () => {
        const texto = input.value.toLowerCase();

        linhas.forEach(linha => {
            // pega o nome da 1ª coluna (td[0])
            const nome = linha.getElementsByTagName('td')[0].textContent.toLowerCase();

            // verifica se o nome começa com o texto digitado
            if (nome.startsWith(texto)) {
                linha.style.display = ''; // mostra
            } else {
                linha.style.display = 'none'; // esconde
            }
        });
    });


    setTimeout(() => {
        const mensagens = document.querySelector('.messages');
    
        if (mensagens) {
            mensagens.style.display = 'none';
        }
    },4000 );

       const rows = document.querySelectorAll('#cores');
            
            rows.forEach(row => {
                const dataVencimentoCell = row.querySelector('.data_de_vencimento');
                if (dataVencimentoCell) {
                    
                    const dataVencimento = new Date(dataVencimentoCell.textContent.split('/').reverse().join('-'));
                    const dataAtual = new Date();
                    dataAtual.setHours(0, 0, 0, 0); 
                    
                    const diferencaMilissegundos = dataVencimento - dataAtual;

                    const diasRestantes = Math.floor(diferencaMilissegundos / (1000 * 60 * 60 * 24));

                    if (diasRestantes < 0) {
                        row.style.backgroundColor = 'rgba(228, 0, 0, 0.5)'; 
                    } else if (diasRestantes <= 5) {
                        row.style.backgroundColor = 'rgba(255, 255, 0, 0.5)' 
                    } else {
                        row.style.backgroundColor = ' rgba(2, 199, 2, 0.5)'; 
                    }
                }
            });
        });

