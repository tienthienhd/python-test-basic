import requests

import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator

schema = {
    "$schema": "https://json-schema.org/schema#",

    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "employee": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "firstName": {"type": "string"},
                "middleName": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ]},
                "lastName": {"type": "string"}
            },
            "required": ["id", "firstName", "lastName"]
        }
    }
}


def test_get_employee_details_check_status_code_equals_200():
    response = requests.get("http://demo.example.com/employee/employee1")
    assert response.status_code == 200


def test_get_employees_validates_json_resonse_schema():
    response = requests.get("http://demo.example.com/employee")

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    resp_body = response.json()

    # Validate will raise exception if given json is not
    # what is described in schema.
    validate(instance=resp_body, schema=schema)
