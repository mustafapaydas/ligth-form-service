
from django.test import TestCase

from src import contact_info_save_to_excel as email
from django.core.mail import send_mail, EmailMessage

class ProjectTest(TestCase):

    def test_email_check(self):
        self.assertTrue(email.send_to_mail,send_mail)
    def test_email_with_file_check(self):
        self.assertTrue(email.send_to_file,EmailMessage)

    def test_url_check(self):
        response = self.client.get("/generate")
        self.assertEqual(response.status_code, 200)

    def test_url_check_send(self):
        response = self.client.get("/send")
        self.assertEqual(response.status_code, 200)
