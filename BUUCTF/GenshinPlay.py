from time import sleep
from pykeyboard import *
k = PyKeyboard()


data = '''S AS A SDGD S AS A SD SAB
S AS A SDGD S DS AS S
S AS A SDGD S DSAN
DSASA DSASA BDSASA
AS DA HGH SJ HJ JHJD QWQJH
GH GH GH GH GSGD
AS DA HGH SJ HJ JHJD QWQJH
GHEE GHEE GHH
QWE YT YT YT W
E YT YT YT E
WQHQ QWQH QE EW
QWE YT YT YT
W E YT YT YT
EWQH EWQHQQ
HEWQH EWHQQ ​'''


data2 = '''DSDSDGG NASA NASDAN ASDANSD ASDANASDANGDFDG GEWQQQQHGTYY QWETTQW QQQQHGTY QQWETTTEW EWQ QQQHGTYY QQWETTTQW WEQ QQQHTYY QWETTEWW QWE QWET QWE QWET DSDSDGG NASA NASDAN ASDANSD ASDANASDANGDFDG GEWQQQQNGTYY QWETTQW QQQQHGTY QQWETTTEW EWQ QQQHGTYY QQWETTTQW WEQ QQQHTYY WETTEW GEWWQTYY QETT EWW DSDSDGG NA SA NASDA NASDANSD 
'''


data3 = 'DGHGHGHQGHD DGHGHGHEQWH GASDQHE WEWQWH HHH HQWEH HHG GH HHH HQWEH HHRRE HHH HQWEHHHG GH HHH HQWEY HHGG 1-1HGGH GDDGD HHGHJQJHJHG HHG GH GDDGD GGH GGH HJQWH DDG GHEW HHHEW WWQWQHG GGHH DDG GHEW HHHEW WWQWQHDGHHGH DGHHHEEJQ WQWEH GGHEEWQH GHHQW HHHGGHEQWQWEE GHQ G HE EWQJHGGH GHQGH T EQQQET TV '
# data = data + '    ' + data2


data4 = ''' BA DG AM DG GH JQ HG DSA AA DSA AA SOS NM ASA SAGM NMN MN B D GD SA GM NMN M A SDS BA DG AM 
JQ HG DSA AA DSA M SDS NM ASA 
'''

for i in data3:
    if i == ' ':
        sleep(0.3)
    else:
        k.tap_key(i)
        sleep(0.2)
