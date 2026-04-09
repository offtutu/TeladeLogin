# Projeto Lazarus

Projeto de tela de login dividido em `Front` e `Back`, com base preparada para uso com Django e Django Unicorn.

## Estrutura

- `Front/`
  - Contem o HTML e o CSS da tela de login.
- `Back/`
  - Contem os arquivos Python do projeto.
  - Inclui a estrutura do Django.
- `.venv/`
  - Ambiente virtual local com as bibliotecas instaladas.

## Arquivos principais

- `Front/index.html`
- `Front/style.css`
- `Back/Login.py`
- `Back/Conta.py`
- `Back/manage.py`

## Tecnologias

- Python
- Django
- Django Unicorn
- HTML
- CSS

## Como rodar

Abra o terminal na pasta `Back` e execute:

```powershell
& "d:\Estudos de programação\Estagio\Logica\Tela de Login\.venv\Scripts\python.exe" "d:\Estudos de programação\Estagio\Logica\Tela de Login\Back\manage.py" runserver
```

Se preferir, use o caminho completo do Python da virtualenv.

Depois abra no navegador:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/unicorn-preview/`

## Rotas

- `/`
  - Exibe o front atual do projeto.
- `/unicorn-preview/`
  - Exibe um exemplo básico usando Django Unicorn.
 
## Futuras adições

- uma falando que o login foi bem sucedido
- uma tela para criação de conta
- uma tela para recuperação de senha
