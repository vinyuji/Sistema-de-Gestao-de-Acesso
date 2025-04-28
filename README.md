# Sistema de gestao de acesso

# Resumo

Este projeto tem como objetivo desenvolver um sistema de controle de acesso utilizando o ESP32-CAM para captura de imagens. As imagens serão enviadas para um servidor dedicado, responsável pelo processamento e reconhecimento facial.

O sistema contará com uma interface de interação para os administradores, permitindo realizar operações de CRUD (criação, leitura, atualização e exclusão) de usuários e informações.

Além disso, o projeto visa reduzir custos, eliminando a necessidade de suporte técnico especializado, exigindo apenas conhecimentos básicos de sistemas de cadastro para sua operação e manutenção.

Linguagem de programacao utilizado Python com Django

# Introducao

# Funcionamento

# Metodologia 

# Resultados

# Bibliografia

# Dicas

gerar o ambiente virtual

    python -m venv venv

entrar no modo venv no Windowns

    .\venv\Scripts\activate

Caso nao ative o ambiente virtual no powershell, rode antes de ativar

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


Instalar o django 

    pip install django

Criar Projeto Python

    django-admin startproject meu_site

# Para rodar o server teste

Entre no diretorio do projeto

    Cd .\Meu_projeto\

Rode no terminal o bash abaixo para rodar o servidor

    python manage.py runserver

Sair do Ambiente virtual

    deactivate

# Para instalar as dependencias em outras maquinas 

    pip install -r requirements.txt

# Criar apps (funcionalidas)

    python manage.py startapp nome_do_app



