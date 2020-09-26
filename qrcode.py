import pyqrcode
import validators

def createQR(url = 'https://www.github.com/Elry', qrName = 'author'):
  url = pyqrcode.create(url)
  url.svg(qrName+'.svg', scale = 8)
  url.eps(qrName+'.eps', scale = 2)
  print(url.terminal(quiet_zone = 1))

def getUrl():
  print('Enter link to transform into QR code')
  url = str(input())

  while validators.url(url) != True:
    print('Invalid url. E.g: https://www.google.com')
    print('Enter link to transform into QR code')
    url = str(input())
  else:
    createQR(url, 'customQR')

  createQR()

getUrl()