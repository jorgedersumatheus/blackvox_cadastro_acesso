# BLACKVOX Playlists

Este é o aplicativo BLACKVOX Playlists, desenvolvido para gerenciar suas playlists de áudio de maneira simples e eficiente.

## Funcionalidades

- **Escolher Arquivo**: Permite selecionar um arquivo de áudio do seu dispositivo para adicionar à lista de reprodução.
- **Baixar Áudio**: Baixa o áudio selecionado.
- **Salvar Playlist**: Salva a playlist atual no armazenamento local do navegador.
- **Carregar Playlists**: Carrega as playlists salvas do armazenamento local.
- **Importar Playlists**: Importa playlists previamente salvas.

### Como Usar

1. **Adicionar Áudio**:
   - Clique no botão "Escolher Arquivo" e selecione um arquivo de áudio do seu dispositivo.
   - O áudio será adicionado à lista de reprodução exibida na tela.

2. **Baixar Áudio**:
   - Depois de adicionar um arquivo de áudio, clique no botão "Baixar Áudio" para baixar o áudio selecionado.

3. **Salvar Playlist**:
   - Insira um nome para a playlist no campo de texto "Nome da Playlist".
   - Clique no botão "Salvar Playlist" para salvar a playlist no armazenamento local do navegador.
   - Um indicador de progresso será exibido durante o processo de salvamento.

4. **Carregar Playlists**:
   - Clique no botão "Carregar Playlists" para carregar as playlists salvas do armazenamento local.
   - Uma lista de playlists salvas será exibida. Clique no botão "Carregar" ao lado do nome da playlist para carregá-la.

5. **Importar Playlists**:
   - Clique no botão "Importar Playlists" para importar playlists previamente salvas.
   - Um indicador de progresso será exibido durante o processo de importação.

#### Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `index.html`: Contém o código HTML e JavaScript do aplicativo.
- `README.md`: Este arquivo de documentação.

##### Tecnologias Utilizadas

- HTML
- CSS
- JavaScript

###### Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades para o aplicativo. Para contribuir, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça push para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

####### Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

**Autor**: Jorge Luis Aparecido Matheus

Se você tiver alguma dúvida ou sugestão, entre em contato pelo e-mail jorge@jorgematheus.mus.br.

# BLACKVOX Register

Este repositório contém um formulário de cadastro que envia um email com as informações do usuário para o Gmail e concede acesso ao BLACKVOX.

## Configuração

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu_usuario/BLACKVOX-register.git
    cd BLACKVOX-register
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais de email:
    ```
    EMAIL_USER=seu_email@gmail.com
    EMAIL_PASS=sua_senha_do_app
    ```

5. Execute a aplicação:
    ```sh
    python flask_app/app.py
    ```

6. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

BLACKVOX-register/
│
├── flask_app/
│   ├── __init__.py
│   ├── app.py
│   └── templates/
│       └── index.html
├── .gitignore
└── README.md

