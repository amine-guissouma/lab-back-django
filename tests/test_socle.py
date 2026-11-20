from django.test import TestCase


class SocleApiTests(TestCase):
    def test_lab(self):
        response = self.client.get("/api/lab")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "lab": "lab-back-django",
                "experience": "socle",
            },
        )

    def test_unknown_route(self):
        response = self.client.get("/api/unknown")

        self.assertEqual(response.status_code, 404)

    def test_lab_content_type(self):
        response = self.client.get("/api/lab")

        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )
