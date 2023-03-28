import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random

from clientes.models import Cliente
from faker import Faker


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        p = Cliente(nome=nome, email=email, mensagem='dsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        p.save()

criando_pessoas(50)
print("Sucesso!")