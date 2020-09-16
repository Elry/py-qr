import pyqrcode

url = pyqrcode.create('https://github.com/Elry')
url.svg('github.svg', scale = 8)
url.eps('github.eps', scale = 2)
print(url.terminal(quiet_zone = 1))