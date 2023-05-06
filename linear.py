# Import thư viện
from sklearn.linear_model import LinearRegression
import numpy as np
import csv
from vnstock import*
import config as cf
import random
def linear_data(ticket):
#cp=listing_companies()
# nh=cf.get_ticket()
# ti=['ACB','ABB']
# for ticket in ti:
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
        K.append([float(data[i][1]),float(data[i][2])])
        h.append(float(data[i][0]))
    # Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    x_mean=np.mean(K,axis=0)
    y_mean=np.mean(h)
    # Huấn luyện mô hình với dữ liệu
    model.fit(K,h)
    r_sq = model.score(K, h)
    #print('coefficient of determination:', r_sq)
    # In ra các hệ số của mô hình
    #print('Coefficients:', model.coef_)
    # Dự đoán giá trị mới
    temp=random.randint(0,len(data)-1)
    #print(temp)
    x_new = np.array([K[temp]])
    #print(x_new)
    y_new = model.predict(x_new)
    #print('Predicted value:', y_new)
    return [y_new[0],y_mean]
j=linear_data('ACB')
