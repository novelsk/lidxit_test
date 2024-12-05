import json
import random

from faker import Faker

types = ['date', 'phone', 'email', 'text']
fake = Faker('en_US')


def generate_forms(count):
    forms = []
    random_names = ['_'.join(fake.words(2)) for _ in range(count // 2)]
    for _ in range(count):
        document = {
            'name': f'{fake.word().capitalize()}Form',
            random.choice(random_names): random.choice(types),
            random.choice(random_names): random.choice(types),
            random.choice(random_names): random.choice(types),
            random.choice(random_names): random.choice(types),
        }
        forms.append(document)
    return forms


if __name__ == '__main__':
    with open('fixture.json', 'w') as f:
        json.dump(generate_forms(10), f)
