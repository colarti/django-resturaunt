import qrcode
import os

os.chdir('./App18-Django-Resturaunt/django-resturaunt/')

img = qrcode.make('https://127.0.0.1:8000')
img.save('qr.png')
