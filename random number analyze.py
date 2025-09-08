import psutil
import statistics
import time
import math
import matplotlib.pyplot as plt
from scipy.stats import chisquare
import numpy as np
i=3
while i==1:#長條圖
    one=two=three=four=five=six=seven=eight=nine=ten=0
    mode=0
    for i in range(101):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==1:
            ans=1000*a+100*d+10*b+c
        elif mode%4==2:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        print(ans,a,b)
        mode+=d
        if ans<= 1000:
            one+=1
        elif ans>1000 and ans<=2000:
            two+=1
        elif ans>2000 and ans<=3000:
            three+=1
        elif ans>3000 and ans<=4000:
            four+=1
        elif ans>4000 and ans<=5000:
            five+=1
        elif ans>5000 and ans<=6000:
            six+=1
        elif ans>6000 and ans<=7000:
            seven+=1
        elif ans>7000 and ans<=8000:
            eight+=1
        elif ans>8000 and ans<=9000:
            nine+=1
        else :
            ten+=1
    y_count=[one,two,three,four,five,six,seven,eight,nine,ten]
    print(y_count)
    x_number=[0,1,2,3,4,5,6,7,8,9]
    fig = plt.figure(figsize=(18,8))
    plt.bar(x_number,y_count)
    #plt.subplot(211)
    i=0
    plt.show()
while i==2:#核心
    mode=0
    displayprint=[]
    for k in range(i):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        #time=int(time.time()*1000*1000)%1000
        if mode >= 100:
           mode = 0
        if d != 0:  # 防止d為0的情況
            if mode % 4 == 0:
                 mode += d
            elif mode % 4 == 1:
                mode += c
            elif mode % d == 2:
                mode += b
            elif mode % 4 == 3:
                mode += a
        else:  # d為0的情況下，不進行mode計算
            if mode % 4 == 0:
                mode += 1
            elif mode % 4 == 1:
                mode += c
            elif mode % 4 == 2:
                mode += b
            elif mode % 4 == 3:
                mode += a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==2:
            ans=1000*a+100*d+10*b+c
        elif mode%4==1:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        ans=round(ans%9999)
        displayprint.append(ans)
while i==3:#次數->值
    x_times=[]
    y_number=[]
    mode=0
    x=0
    for i in range(1001):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==1:
            ans=1000*a+100*d+10*b+c
        elif mode%4==2:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        mode+=d
        x+=1
        x_times.append(x)
        y_number.append(ans)
    fig = plt.figure(figsize=(10,6),num=1)
    #plt.subplot(212)
    plt.suptitle('analyze')                       #第一個圖表--- \
    plt.plot(x_times,y_number,color='#0000FF',linewidth=0.5)#    \
    plt.title('mine')                             #--------------\
    plt.xlabel('n times',{'fontsize':20,'color':'blue'})
    plt.ylabel('number',{'fontsize':20,'color':'blue'})
    plt.show()
    i=0
while i==4:#卡方檢測
    y_number=[]
    mode=0
    for i in range(101):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==1:
            ans=1000*a+100*d+10*b+c
        elif mode%4==2:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        mode+=d
        y_number.append(ans)
    n =sum(y_number)  # 总样本数
    expected_freq = np.full_like(y_number, fill_value=n / len(y_number))
    statistic, p_value = chisquare(y_number, expected_freq)
    print("卡方检验统计量：", statistic)
    print("P 值：", p_value)
while i==5:#在cmd輸出
    x_times=[]
    y_number=[]
    mode=0
    x=0
    for i in range(101):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==1:
            ans=1000*a+100*d+10*b+c
        elif mode%4==2:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        mode+=d
        x+=1
        print(ans)
        x_times.append(x)
        y_number.append(ans)
    #print(x_times)
    #print("\n",y_number)
while i==6:#相關係數
    displayprint=[]
    i=10000#int(input("i:"))
    range_=9999#int(input("range:"))
    mode=0
    for k in range(i):
        s1,s2,s3,s4=psutil.cpu_stats()         #xxxxxxxxabcd-->dbca  adbc  cadb bcad
        part=math.floor(s4/10)*10              
        d=s4-part                              #d
        part=math.floor(s4/100)*100       
        c=(s4-part-d)/10                       #c
        part=math.floor(s4/1000)*1000
        b=(s4-part-10*c-d)/100                 #b
        part=math.floor(s4/10000)*10000
        a=(s4-part-100*b-10*c-d)/1000          #a
        if d==0:
            d+=1
        if mode>=100:
            mode=0
        if mode%4==0:
            mode+=d
        elif mode%4==1:
            mode+=c
        elif mode%d==2:
            mode+=b
        elif mode%4==3:
            mode+=a
        if mode%4==0:
            ans=1000*d+100*b+10*c+a
        elif mode%4==2:
            ans=1000*a+100*d+10*b+c
        elif mode%4==1:
            ans=1000*c+100*a+10*d+b
        elif mode%4==3:
            ans=1000*b+100*c+10*a+d
        ans=round(ans%range_)
        displayprint.append(ans)
    print(displayprint)
    sigma=statistics.pvariance(displayprint)
    print(sigma)