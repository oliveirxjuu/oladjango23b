# oladjango23b

## Comandos (03/03/2023)
- *criar um projeto*
    -  python -m django startproject 
- *entrar na página manage.py*
    - cd itapira
- *criar um app*
    - python mange.py startapp enquete 
- *iniciar o servidor*
    - python manage.py runserver
- *cria a lista de dependências*
    - pip freeze > requirements.txt
- *instala as dependências*
    - pip install -r requirements.txt 
- *executar migrações iniciais*
    - python manage.py migrate
- *CRIAR SUPER USUÁRIO*
    - cd itapira
    - manage.py createsuperuser
    - usuario admin
    - senha 123mudar
    - email juliaoliveirac2006@gmail.com

- pip freeze mostra quais os pacotes instalados na máquina e suas versões
 






## aula 31/03/2023
- crud: create, read, update e delete
    - são as operações basicas que fazemos no banco de dados

- django contrib: é uma caixa de ferramentas dentro do django que já vem instaladas para facilitar a vida do programador, a mais famosa é o admin, path(cadastrar um caminho de url)
- scarrffold é uma lib para criar models e uma API simples em django rest framework
- o django admin é uma interface de administração automática que fornece uma interface poderosa para produção para adicionar conteúdo ao site

http://127.0.0.1:8000/enquete/mabou
http://127.0.0.1:8000/enquete/ 