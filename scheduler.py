from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1,hour=8,minute=0,second=0,microsecond=0)
delta_t=y-x

secs = delta_t.seconds+1

def runscript():
    return function #add function from Tripadvisor.py

t = Timer(secs,runscript)
t.start()
