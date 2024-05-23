from django.core.management.base import BaseCommand
from faker import Faker
from realtors.models import Realtor
import random

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        # fake = Faker('uk_UA')
        fake = Faker()
        print('---------------------->')
        items = list(Realtor.objects.all());
        random_items = random.sample(items, 3)
        print(random.choice(items))
        print('---------------------->')
        print(f'Address:', fake.address())
        print(f'Bulding Number:', fake.building_number())
        print(f'City:', fake.city())
        print(f'Country:', fake.country())
        # print(f'Region:', fake.region())
        print(f'Post Code:', fake.postcode())
        print(f'Text:', fake.text())
        print(f'Color:', fake.color())
        print(f'Company:', fake.company())
        print(f'Credit Card:', fake.credit_card_full())
        print(f'Currency:', fake.currency())
        print(f'Crypto:', fake.cryptocurrency())
        print(f'Date Time:', fake.date_time())
        print(f'Emoji:', fake.emoji())
        print(f'GEO:', fake.local_latlng())
        # print(f'', fake.internet())
        print(f'ISBN', fake.isbn10())
        print(f'Job:', fake.job())
        print(f'Paragraphs: ')
        print('-----------------')
        for _ in range(2):
            print(fake.paragraph(nb_sentences=10))
            print('-----------------')
        print(f'Words: ')
        print('-----------------')
        for _ in range(2):
            print(fake.words())
            print('-----------------')
        # print(f'', fake.misc())
        # print(f'', fake.passport())
        print(f'First Name:', fake.first_name())
        print(f'Last Name:', fake.last_name())
        print(f'Phone Number:', fake.phone_number())
        print(f'Profile:', fake.profile())

        self.stdout.write(self.style.SUCCESS('Successfully generated test data'))
