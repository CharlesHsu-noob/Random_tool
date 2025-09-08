from statsmodels.sandbox.stats.runs import runstest_1samp
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import psutil
while True:
    true=1
    putintoans=n=0
    print('按ctrl+c結束程式\n亂輸入會crash')
    while true==1:
        try:
            i=int(input('請問要生成幾個數:'))*2
            true=0
        except ValueError:
            print('輸入的不是整數!請重新輸入')
    true=1
    while true==1:
        mode=0
        try:
            range_=int(input('範圍(最大9999)='))
            true=0
        except ValueError:
            print('輸入的不是整數!請重新輸入')
    if range_>=10000:
        print("範圍過大!自動設為9999")
        range_=9999
    true=1
    print("1:[a,b,c,d...]\n2:a\n  b\n  c\n  d...")
    while true==1:
        try:
            display=int(input("請輸入顯示模式:"))
            true=0
        except ValueError:
            print('輸入的不是整數!請重新輸入')
    if display!=1 and display !=2:
        print("無效的模式!自動設定為1")
        display=1
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
        random_factor = d*c
        mode = (mode + random_factor * 1000) % 10000
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
        ans=round(ans%range_)
        putintoans+=1
        if n>500:
            n=0
        n+=d
        if putintoans%2==1:
            if n%2==1:
                displayprint.insert(1,ans)
            else:
                displayprint.insert(n,ans)
        #displayprint.append(ans)
    if display==1:
        print(displayprint)
    else:
        for num in displayprint:
            print(num)
    # 使用游程檢驗
    z_stat, p_value = runstest_1samp(displayprint, correction=False)

    # 結果
    print(f"Z 統計量: {z_stat}")
    print(f"P 值: {p_value}")

    # 判斷結果
    if p_value > 0.05:
       print("無法拒絕隨機性假設，數據似乎是隨機的。")
    else:
        print("拒絕隨機性假設，數據中存在趨勢或模式。")
    #print(type(displayprint))
    displayprint = list(map(int, displayprint))
    lenght=len(displayprint)
    result=[]
    for k in range(lenght):
        result.insert(k,k)
    #result = ", ".join(str(k) for k in range(1, lenght+ 1))
    plt.plot(displayprint,result)
    plt.show