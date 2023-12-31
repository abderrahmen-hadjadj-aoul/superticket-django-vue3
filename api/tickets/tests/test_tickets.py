
from django.test import TestCase

class TicketTest(TestCase):

    def test_create_ticket(self):
        body = {
            "title": "Clean room",
            "description": "Start with the bedroom, then toilets and the rest in any order",
        }
        response = self.client.post("/api/tickets/", body)

        self.assertEqual(response.status_code, 201)
        created_ticket = response.json()
        ticket_id = created_ticket["id"]
        self.assertEqual(type(ticket_id), int)

        response = self.client.get(f"/api/tickets/{ticket_id}/")
        self.assertEqual(response.status_code, 200)
        retrieved_ticket = response.json()
        self.assertEqual(retrieved_ticket["id"], ticket_id)
        self.assertEqual(retrieved_ticket["title"], body["title"])
        self.assertEqual(retrieved_ticket["description"], body["description"])
