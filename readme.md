# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto

`git clone https://github.com/redgar1980/ediaristas-python`

#### Instalar dependências

`pip install -r requirements.txt`

#### Alterar configurações do BD no arquivo `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'
    }
}
```

#### Migrar banco de dados

`python manage.py migrate`

#### Iniciar o servidor

`python manage.py runserver`
