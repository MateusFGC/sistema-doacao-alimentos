# Sistema Simples de Doação de Alimentos (CLI)

Um aplicativo simples de linha de comando (CLI) desenvolvido em Python para gerenciar o registro e a solicitação de doações de alimentos, utilizando TinyDB para armazenamento de dados.

## Objetivo

Este projeto visa criar uma ferramenta básica para facilitar a conexão entre pessoas que desejam doar alimentos e aquelas que precisam recebê-los. Ele permite registrar itens disponíveis, visualizar o estoque, solicitar itens e manter um histórico das doações concluídas, tudo através de uma interface de terminal interativa. Foi desenvolvido como um projeto simples para demonstrar conceitos de Python e o uso do banco de dados NoSQL TinyDB.

## Funcionalidades

* **Doar Alimentos:** Permite que um usuário registre um alimento para doação, informando o nome do doador, tipo de alimento, quantidade e data de validade.
* **Ver Estoque Disponível:** Lista todos os alimentos que foram doados e ainda estão disponíveis para solicitação, exibindo seus detalhes e um ID único.
* **Solicitar Alimentos:** Permite que um usuário solicite um item específico do estoque disponível, informando seu nome, contato e o motivo da necessidade. Ao solicitar, o item é automaticamente marcado como 'doado' e removido do estoque visível.
* **Ver Histórico de Doações:** Exibe um registro de todas as transações concluídas, mostrando qual alimento foi doado, por quem, para quem, o contato do receptor, o motivo e a data da conclusão.

## Tecnologias Utilizadas

* **Python 3:** Linguagem de programação principal.
* **TinyDB:** Banco de dados NoSQL leve, baseado em documentos JSON, para armazenamento dos dados de doações e transações.

## Estrutura do Projeto
food_donation_app/  
├── db/                      # Pasta para o arquivo do banco de dados  
│   └── food_data.json       # Arquivo do TinyDB (criado automaticamente)  
├── main.py                  # Ponto de entrada da aplicação (executa o menu)  
├── database.py              # Contém todas as funções de interação com o TinyDB  
└── actions.py               # Contém a lógica para cada ação do menu (doar, solicitar, etc.)  
## Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/MateusFGC/sistema-doacao-alimentos.git](https://github.com/MateusFGC/sistema-doacao-alimentos.git)
    cd food_donation_app
    ```
2.  **Crie um Ambiente Virtual (Recomendado):**
    Isso isola as dependências do projeto.
    ```bash
    python -m venv venv 
    ou use o py no lugar do python
    ```

<!-- 3.  **Ative o Ambiente Virtual:**
    * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * No Linux/macOS:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as Dependências:**
    O projeto depende apenas do TinyDB.
    ```bash
    pip install -r requirements.txt
    ``` -->

## Como Usar

Após a configuração e instalação, você pode executar o aplicativo diretamente pelo terminal:

1.  Certifique-se de ter o python instalado em seu computador 
2.  Execute o script principal: database/main.py
    ```bash
    python main.py
    ```
3.  Um menu interativo será exibido no terminal. Digite o número da opção desejada e pressione Enter.
4.  Siga as instruções para cada ação (doar, visualizar, solicitar, ver histórico).
5.  Para sair do aplicativo, escolha a opção "0".

## Possíveis Melhorias Futuras

* Implementar um sistema de autenticação de usuários (login/senha).
* Adicionar validação de dados mais robusta (ex: formato de data, quantidade numérica).
* Criar filtros ou busca para o estoque e histórico.
* Desenvolver uma interface gráfica (GUI) usando bibliotecas como Tkinter, Kivy ou PyQt.
* Melhorar o gerenciamento de status (ex: solicitação pendente de aprovação).

