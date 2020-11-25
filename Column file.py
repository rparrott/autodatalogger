import random
import csv
from datetime import datetime
import os
from time import sleep


time=datetime.now().strftime("%y%m%d_%H.%M")
csvname='log'+time+'.csv'
header=["Time","Boost (Psi)","Oil"]
with open (csvname, 'a+', newline='') as f:
    csv_writer=csv.writer(f)

i=0
while i<100:
    i=i+1
    Time=[]
    Boost=[]
    Oil=[]
    
    boost=round(random.uniform(-14.5,43.5),2)
    oil=round(random.uniform(0,100),2)
    
    Boost.append(boost)
    Oil.append(oil)
    Time.append(datetime.now().strftime("%M.%S.%f")[:-3])
    
    row_list=(Time,Boost,Oil)
    with open(csvname, 'a+', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(row_list)
    sleep=(.001)
    
    
    
