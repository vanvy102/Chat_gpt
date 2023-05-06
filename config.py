from vnstock import*
import requests
import json
import pandas as pd
import numpy as np
import os 
import datetime
import random
from sklearn.linear_model import LinearRegression
API_KEY="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"
model="text-davinci-003"
#ham lay ma ngan hang
def get_ticket():
   ticket=[]
   with open('MaNH.txt','r') as f:
    h=f.read()
    h=h.splitlines()
    for i in h:
        ticket.append(i)
    return ticket
#lấy tên công ty
def get_name_cp():
    with open('f.json','r',encoding="utf8") as gf:
        h=json.load(gf)
    df = pd.DataFrame(h['items']).drop(columns=['organCode', 'icbCode', 'organTypeCode', 'comTypeCode']).rename(columns={'comGroupCode': 'group_code', 'organName': 'company_name', 'organShortName':'company_short_name'})
    check='ngân hàng thương mại cổ phần'
    nh=[]
    for n in range(len(df)):
        if check in df.loc[n][2].lower():
            nh.append(df.loc[n][2])
    return nh
#
def get_trade_code():
    with open('f.json','r',encoding="utf8") as gf:
        h=json.load(gf)
    cp = pd.DataFrame(h['items']).drop(columns=['organCode', 'icbCode', 'organTypeCode', 'comTypeCode']).rename(columns={'comGroupCode': 'group_code', 'organName': 'company_name', 'organShortName':'company_short_name'})
    check='ngân hàng thương mại cổ phần'
    code=[]
    index=['upcom','hose']
    for n in range(len(cp)):
        if check in cp.loc[n][2].lower():
            if 'VNINDEX' in cp.loc[n][1]:
                code.append(index[1])
            else:
                code.append(index[0])
    return code
#lay các đường link
def get_link_web(ticket):
    data=[]
    smr='tóm tắt bài viết '
    fi='./file/'+ticket+'.txt'
    with open(fi,'r') as fp:
        sd=fp.readlines()
        data=[smr+line.rstrip('\n') for line in sd]
    return data
def get_data_bank(ticker):
    #lay moc thoi gian giao dich trong 30 ngay
    current_time= datetime.date.today()
    thirty_days_ago= current_time+ datetime.timedelta(-30)
    start_time=str(thirty_days_ago)
    end_time=str(current_time)
    df = stock_historical_data(symbol=ticker, 
                            start_date=start_time, 
                            end_date=end_time)
    return df
# def linear_data(ticket):
#cp=listing_companies()
# nh=cf.get_ticket()
# ti=['ACB','ABB']
# for ticket in ti:
    # data=[]
    # df=cf.get_data_bank(ticket)
    # for k in range(len(df)):
    #     temp=[]
    #     for i in range(5):
    #         temp.append(df.loc[k][i])
    #     data.append(temp)
    # # linkfile='./nganhang/'+ticket+'.csv'
    # # with open(linkfile) as file:
    # #     fp=csv.reader(file)
    # #     header=next(fp)
    # #     for row in fp:
    # #         data.append(row)
    # # Tạo dữ liệu giả định
    # K=[]
    # h=[]
    # for i in range(len(data)):
    #     K.append([float(data[i][1]),float(data[i][2])])
    #     h.append(float(data[i][0]))
    # # Tạo mô hình hồi quy tuyến tính
    # model = LinearRegression()
    # x_mean=np.mean(K,axis=0)
    # y_mean=np.mean(h)
    # # Huấn luyện mô hình với dữ liệu
    # model.fit(K,h)
    # r_sq = model.score(K, h)
    # #print('coefficient of determination:', r_sq)
    # # In ra các hệ số của mô hình
    # #print('Coefficients:', model.coef_)
    # # Dự đoán giá trị mới
    # temp=random.randint(0,len(data)-1)
    # #print(temp)
    # x_new = np.array([K[temp]])
    # #print(x_new)
    # y_new = model.predict(x_new)
    # #print('Predicted value:', y_new)
    # return [y_new[0],y_mean]
