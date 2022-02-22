from django.core.mail import send_mail
def sendMail(link,email):

    send_mail(
        'Başvuru Linki',
        f'Link: http://127.0.0.1:8000/form{link}',
        "mntsodev@outlook.com",
        [email]
)