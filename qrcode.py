import pyqrcode
import validators

print('Enter link to transform into QR code')
url = str(input())

while validators.url(url) != True:
  print('Invalid. E.g: Https://gogogle.com')
  print('Enter link to transform into QR code')
  url = str(input())
else:
  url = pyqrcode.create(url)
  url.svg('customQR.svg', scale = 8)
  url.eps('customQR.eps', scale = 2)
  print(url.terminal(quiet_zone = 1))

url = pyqrcode.create('https://github.com/Elry')
url.svg('authorQR.svg', scale = 8)
url.eps('authorQR.eps', scale = 2)
print(url.terminal(quiet_zone = 1))