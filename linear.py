# Import thư viện
from sklearn.linear_model import LinearRegression
import numpy as np
import csv
from vnstock import*
import config as cf
import random
import get_set_data as gsd
def linear_data(ticket,token, shift):
    data=[]
    df=cf.get_data_bank(ticket)
    for k in range(len(df)):
        temp=[]
        for i in range(5):
            temp.append(df.loc[k][i])
        data.append(temp)
    # linkfile='./nganhang/'+ticket+'.csv'
    # with open(linkfile) as file:
    #     fp=csv.reader(file)
    #     header=next(fp)
    #     for row in fp:
    #         data.append(row)
    # Tạo dữ liệu giả định
    K=[]
    h=[]
    for i in range(len(data)):
        K.append([int(data[i][1]),int(data[i][2])])
        h.append(int(data[i][0]))
    # Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    x_mean=np.mean(K,axis=0)
    y_mean=np.mean(h)
    # Huấn luyện mô hình với dữ liệu
    model.fit(K,h)
    #r_sq = model.score(K, h)
    #print('coefficient of determination:', r_sq)
    # In ra các hệ số của mô hình
    #print('Coefficients:', model.coef_)
    # Dự đoán giá trị mới
    
    #print(temp)
    X_train=gsd.get_data(ticket,token,shift)
    x_new = [X_train[len(X_train)-1]]
    #print(x_new)
    y_new = model.predict(x_new)
    #print('Predicted value:', y_new)
    return [int(y_new[0]),int(y_mean)]
