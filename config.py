from vnstock import*
import requests
import json
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
def get_link_web(ticket):
    data=[]
    smr='tóm tắt bài viết '
    fi='./file/'+ticket+'.txt'
    with open(fi,'r') as fp:
        sd=fp.readlines()
        data=[smr+line.rstrip('\n') for line in sd]
    return data
