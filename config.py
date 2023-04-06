from vnstock import*
API_KEY="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"
model="text-davinci-003"
#ham lay ma ngan hang
def get_ticket():
    cp=listing_companies()
    check='ngân hàng thương mại cổ phần'
    ticket=[]
    for n in range(len(cp)):
        if check in cp.loc[n][2].lower():
            ticket.append(cp.loc[n][0])
    return ticket
def get_name_cp():
    cp=listing_companies()
    check='ngân hàng thương mại cổ phần'
    nh=[]
    for n in range(len(cp)):
        if check in cp.loc[n][2].lower():
            nh.append(cp.loc[n][2])
    return nh
def get_trade_code():
    cp=listing_companies()
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
