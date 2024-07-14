import json
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collabstr_mar.settings')
django.setup()

from content_creator_app.models import Content, Creator

json_file = os.path.join(os.path.dirname(__file__), 'creators.json')

if not os.path.exists(json_file):
    raise FileNotFoundError(f"The file {json_file} does not exist")

with open(json_file, 'r') as f:
    creators_content = json.load(f)


for item in creators_content:
    creator, created = Creator.objects.get_or_create(
        name=item['name'],
        username=item['username'],
        platform=item['platform'],
        rating=item['rating']
    )
    Content.objects.create(
        creator=creator,
        url=item['content']
    )
