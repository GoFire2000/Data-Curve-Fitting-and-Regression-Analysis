import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readDatFile(inFile):
    with open(inFile, 'r') as f:
        data = f.readlines()
    dataTime = []
    dataQuantity = []
    for s in data:
        lis = s.split()
        dataTime.append(float(lis[0]))
        dataQuantity.append(float(lis[1]))
    return dataTime, dataQuantity

if __name__ == '__main__':
    # ===================(a)=====================
    # 读取数据
    inFile = '.\\yeastGrowth.txt'
    dataTime, dataQuantity = readDatFile(inFile)
    pm = 665

    # ===================(b)=====================
    # 根据数据，绘制ln p/(pm-p) 和 t的关系图
    # 用semilogy
    
    plt.figure()
    plt.title('ln p/(pm-p)  v/s  t')
    dataY = []
    for p in dataQuantity:
        dataY.append( (( p / (pm - p) )) )
    plt.semilogy(dataTime, dataY)
    plt.xlabel('Time')
    plt.ylabel('lnz')
    plt.savefig('problem_b.jpg')
    # plt.show()
    plt.close()

    # ===================(c)=====================
    # ln p/(pm - p) = r * pm * t + C
    # 求r*pm, C(斜率，截距)
    dataY = [math.log(x, math.e) for x in dataY]
    Xsum = 0.0
    X2sum = 0.0
    Ysum = 0.0
    XY = 0.0
    n = len(dataTime)
    for i in range(n):
        Xsum += dataTime[i]
        Ysum += dataY[i]
        XY += dataTime[i] * dataY[i]
        X2sum += dataTime[i] ** 2
    k = (Xsum * Ysum / n - XY) / (Xsum ** 2 / n - X2sum)
    b = (Ysum - k * Xsum) / n
    print('(r * pm) = %f, C = %f' % (k,b) )

    # ===================(d)=====================
    # 求出t* =  -C / (r * pm)，画出p(t)和t的关系图，逻辑斯蒂曲线
    rpm = k
    C = b
    tStar = - C / rpm
    print('t* = -C / (r*m) = %f'%tStar)
    dataPt= [pm / (1 + math.exp(-rpm * (t - tStar))) for t in dataTime]
    plt.xlabel('t')
    plt.ylabel('p(t) = pm / (1 + exp(-r * pm * (t-t*))')
    plt.title('logistic growth model')
    plt.plot(dataTime, dataPt)
    plt.savefig('problem_d_logistic_growth_model.jpg')
    # plt.show()
    plt.close()
    

    

    


    