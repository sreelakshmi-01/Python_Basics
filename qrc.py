import pyqrcode
g = "Good Night"
url = pyqrcode.create(g)
url.svg("qrcc.svg")
