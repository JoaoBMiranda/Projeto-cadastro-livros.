Projeto de cadastro de livros.

O projeto consiste em desenvolver um sistema de cadastro de livros usando a metodologia RAD (rapid application development). A metodologia RAD é um método de desenvolvimento de software iterativo e incremental, é uma abordagem que coloca um foco significativo na entrega rápida de protótipos funcionais.
O código implementado refere-se a uma aplicação de gerenciamento de cadastro de livros usando Python e Tkinter para a interface gráfica, PostgreSQL como banco de dados e Pandas para manipulação de dados. A aplicação realiza operações CRUD (Create, Read, Update, Delete) em registros de livros, permitindo o cadastro, atualização, exclusão, localização e exibição dos registros.
O projeto foi dividido em quatro fases:
Requisitos: Nesta fase, foram coletados os requisitos do sistema, qual linguagem a ser usada, incluindo as funcionalidades, como os dados seriam armazenados e como os usuários queriam a interação com a interface.
Desenvolvimento: 
Nesta fase, o sistema foi desenvolvido usando a linguagem Python e o framework tkinter, foi feito um estudo breve de como montar a interface. A interface gráfica é criada usando a biblioteca Tkinter. Campos para inserção de informações sobre o livro, como código, título, assunto, editora, autor, preço de compra e preço de venda, são fornecidos. Botões para ações como cadastrar, atualizar, excluir, localizar, limpar campos, calcular preço de venda e salvar registros em um arquivo Excel estão presentes. 
A Classe AppBD é responsável pela conexão com o banco de dados PostgreSQL, e também cria uma tabela caso ela não exista no banco de dados. Métodos para operações CRUD, incluindo inserção, atualização, exclusão, localização e carregamento de registros. Cada método abre uma conexão, executa a operação e fecha a conexão, seguindo boas práticas de manipulação de banco de dados.
Testes:
Nesta fase, o sistema foi testado para garantir que atendesse aos requisitos. Durante alguns testes foi observado que seria interessante um botão para localizar o livro já cadastrado no BD (banco de dados), isso facilita também para caso seja necessário, atualizar ou corrigir uma informação do livro ou até mesmo exclui-lo.  E foi implementado o botão de salvar o todos os registros da tabela em um arquivo excel. 
Implantação: 
Nesta fase, o sistema foi implantado no ambiente de produção.
O sistema possui as seguintes funcionalidades:
Criar Tabela:
Médoto criarTabelaLivros na classe AppBD. Abre uma conexão com o banco de dados, e cria uma tabela no banco de dados, a tabela so é criada se ela não existir no banco de dados. 
Cadastro de livros: 
Método inserirDados na classe AppBD. Abre uma conexão com o banco de dados, e executa o cadastro do livro usando o comando de “insert into” do SQL.
Atualização de livros:
Método atualizarDados na classe AppBD. Abre uma conexão com o banco de dados, executa uma consulta SQL para atualizar os dados do livro e imprime o registro atualizado.
Exclusão de livros:
Método excluirDados na classe AppBD. Abre uma conexão com o banco de dados, executa uma consulta SQL para excluir um livro pelo código e imprime a quantidade de registros excluídos.
Localização de livros:
Método localizarLivro na classe AppBD. Abre uma conexão com o banco de dados, executa uma consulta SQL para localizar um livro pelo código e retorna os dados do livro, para facilitar a busca por um livro. 
Cálculo do preço de venda:
Método fCalcularPrecoVenda na classe PrincipalBD. Calcula o preço de venda com base no preço de compra e uma margem de lucro de 10%.
Salvar Registros em Excel: 
Método salvarRegistros na classe PrincipalBD. Carrega os registros do banco de dados, cria um DataFrame Pandas e salva em um arquivo Excel chamado "registros_livros.xlsx".

O projeto combina duas partes distintas: um sistema de gerenciamento de banco de dados PostgreSQL e uma interface gráfica de usuário (GUI) criada com Tkinter. Utilizando a metodologia Rapid Application Development (RAD), o projeto se concentra na rápida iteração entre a análise, design, desenvolvimento e testes, priorizando a agilidade na entrega de funcionalidades e na adaptação às necessidades do usuário.

A parte do banco de dados é construída com a classe AppBD, que fornece operações CRUD (Create, Read, Update, Delete) para manipular registros na tabela "livros". Isso permite ao sistema armazenar e gerenciar informações sobre livros, como código, título, assunto, editora, autor, preço de compra e preço de venda. Essa estrutura de dados é escalável, possibilitando futuras expansões do sistema.

A interface gráfica, implementada na classe PrincipalBD, oferece uma maneira intuitiva de interagir com o banco de dados. Os elementos visuais, como rótulos, campos de entrada e botões, são dispostos de forma organizada na janela, tornando a experiência do usuário mais amigável. As ações disponíveis, como cadastrar, atualizar, excluir, localizar livros e calcular o preço de venda, são de fácil acesso e uso.

Com a abordagem RAD, a flexibilidade do Tkinter permite que as mudanças no design da interface sejam feitas rapidamente, possibilitando a adaptação a novos requisitos e melhorias de usabilidade. Ao mesmo tempo, as operações de banco de dados são encapsuladas na classe AppBD, o que facilita a manutenção e evita a complexidade desnecessária na interface. Isso garante uma separação clara de responsabilidades no sistema, facilitando a escalabilidade.

A rápida iteração entre a interface e as funcionalidades do banco de dados acelera o desenvolvimento do projeto e permite a entrega de valor de forma ágil. Essa abordagem é ideal para projetos que precisam se ajustar a mudanças constantes ou requisitos não totalmente definidos no início. O projeto demonstra como o RAD pode ser aplicado com sucesso para criar uma aplicação de gerenciamento de livros eficiente, intuitiva e adaptável.
