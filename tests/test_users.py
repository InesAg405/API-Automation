from utils.api_client import get_users
from jsonschema import validate
import json

def test_users_schema():
    response = get_users()
    schema = json.load(open("schemas/user_schema.json"))
    validate(instance=response.json(), schema=schema)