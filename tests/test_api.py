import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPIValidation(unittest.TestCase):

    def test_invalid_data_types(self):
        response = client.post("/data", json={"close": "invalid_string"})
        self.assertEqual(response.status_code, 422) 

    def test_missing_required_fields(self):
        response = client.post("/data", json={})
        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    unittest.main()
