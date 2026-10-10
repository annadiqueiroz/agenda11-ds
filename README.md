# Agenda 11 - ETEC - Desenvolvimento de Sistemas
# 💧 Controle de Níveis de Água

Este projeto foi desenvolvido como parte da **atividade da Agenda 11**, da disciplina de **Desenvolvimento de Sistemas I**, do curso **Técnico em Desenvolvimento de Sistemas da ETEC**.

A atividade tem como objetivo aplicar conceitos de programação em Python, como listas, funções, estruturas condicionais e utilização de bibliotecas externas, por meio da criação de um sistema simples de monitoramento dos níveis de água de um reservatório.

Este projeto foi desenvolvido em Python com o objetivo de simular o monitoramento dos níveis de água de um reservatório.

O programa utiliza a biblioteca **Colorama** para exibir mensagens coloridas no terminal, facilitando a identificação da situação do reservatório conforme o nível de água.

## 🚀 Funcionalidades

- Armazenamento dos cinco níveis de água em uma lista.
- Identificação da situação do reservatório.
- Utilização de funções para definir as mensagens e suas cores.
- Exibição dos níveis de água com cores diferentes no terminal.
- Restauração da cor padrão do terminal após a execução.

## 🎨 Classificação dos níveis

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🔵 Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento do programa.
- **Colorama:** biblioteca responsável por aplicar cores às mensagens exibidas no terminal.

## 💻 Como funciona

O programa utiliza uma lista chamada `niveis_agua`, que armazena as cinco situações possíveis do reservatório.

A função `definir_cor(nivel)` verifica o nível informado e retorna a cor correspondente utilizando a biblioteca Colorama.

A função `situacao_agua(nivel)` acessa a lista e retorna a mensagem associada ao nível selecionado.

Por fim, o programa simula os cinco níveis de água, exibindo cada situação com sua respectiva cor. Ao terminar, utiliza `Style.RESET_ALL` para restaurar a formatação padrão do terminal.
