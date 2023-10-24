# Exemplo de Makefile para um projeto Python

# Defina o nome do ambiente virtual
VENV_NAME = my_venv

# Comandos Python
PYTHON = python
PIP = pip

# Comando para executar o Django
DJANGO_CMD = $(PYTHON) manage.py

# Comando para instalar dependências
INSTALL_DEPENDENCIES = $(PIP) install -r requirements.txt

# Comando para rodar o servidor de desenvolvimento
RUN_SERVER = $(DJANGO_CMD) runserver

# Comando para fazer as migrações
MIGRATE = $(DJANGO_CMD) migrate

# Comando para criar um superusuário
CREATE_SUPERUSER = $(DJANGO_CMD) createsuperuser

# Comando para rodar os testes
RUN_TESTS = $(DJANGO_CMD) test

# Comando para coletar arquivos estáticos
COLLECT_STATIC = $(DJANGO_CMD) collectstatic

# Comando para limpar arquivos temporários
CLEAN = find . -name "*.pyc" -delete

.PHONY: install runserver migrate createsuperuser test collectstatic clean

install:
	$(PYTHON) -m venv $(VENV_NAME)
	$(VENV_NAME)/Scripts/activate
	$(PIP) install -r requirements.txt

runserver:
	$(RUN_SERVER)

migrate:
	$(MIGRATE)

createsuperuser:
	$(CREATE_SUPERUSER)

test:
	$(RUN_TESTS)

collectstatic:
	$(COLLECT_STATIC)

clean:
	$(CLEAN)
