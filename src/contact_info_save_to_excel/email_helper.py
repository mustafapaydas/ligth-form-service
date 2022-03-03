from django.core.mail import send_mail, EmailMessage

from src.save_to_excel_for_contact_info import EMAIL_HOST_USER


def send_to_mail(link, email):

    send_mail(
        'Başvuru Linki',
        f'Link: http://127.0.0.1:8000/form{link}',
        EMAIL_HOST_USER,
        [email]
)
def send_to_file(email,file):
    mail = EmailMessage('Başvuru Dosyası', 'Başvurunuz Alınmıştır.',EMAIL_HOST_USER, [email])
    mail.attach(file.name, file.read(), file.content_type)
    mail.send()