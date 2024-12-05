import json

import httpx


if __name__ == '__main__':
    example = {
        'date': '2024-01-01',
        'phone': '+7 999 999 99 99',
        'email': 'mail@mail.mail',
        'text': 'some text',
    }

    with open('fixture.json') as f:
        fixture = json.load(f)

    for template in fixture:
        response = httpx.post(
            'http://127.0.0.1:8000/get_form',
            params={
                k: example[v] for k, v in template.items() if k != 'name'
            }
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert template['name'] == data['name']
