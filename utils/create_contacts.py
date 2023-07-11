import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'agenda.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contatos.models import Category, Contato
    Contato.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categorias = ['Amigos', 'Familia', 'Conhecidos']

    django_categorias = [Category(name=name) for name in categorias]

    for categoria in django_categorias:
        categoria.save()

    django_contatos = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categorias)

        django_contatos.append(
            Contato(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contatos) > 0:
        Contato.objects.bulk_create(django_contatos)
