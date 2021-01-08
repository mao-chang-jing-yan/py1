import re

import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, quote


class Book:
    search_base_url = "http://book.ucdrs.superlib.net/search?"
    book_detail_url = "http://book.ucdrs.superlib.net"
    search_word = "math"
    sw = ""
    kw = {
        "sw": sw,
        "allsw": "",
        "bCon": "",
        "ecode": "utf-8",
        "channel": "search",
        "Field": "all"
    }

    def __init__(self, sw):
        self.sw = sw
        self.kw = Book.kw
        self.kw["sw"] = sw
        s = ""
        for i, j in zip(self.kw.keys(), self.kw.values()):
            s = s + str(i) + "=" + str(j) + "&"

        self.s = s[:-1]
        self.book_list = []

        self.keys = {'name', 'content', 'url', '原书定价', '主题词', '出版项', 'groupid', '丛书名', 'ISBN号', '形态项', 'adid', '参考文献格式',
                     'img_url',
                     '作者',
                     '中图法分类号'}

    # print(search_base_url + s)
    # print(search_base_url + quote(s))
    # print(quote(search_base_url + s))

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "__dxca=26971eac-0030-4c63-8648-d79ff3fd0725; msign_dsr=1609157760479; UM_distinctid=176a946d9a79d7-0ca520a716be41-5a301e44-144000-176a946d9a838a; CNZZDATA2088844=cnzz_eid%3D188578588-1609156231-null%26ntime%3D1609205379; nopubuser_abo=0; groupenctype_abo=1; DSSTASH_LOG=C%5f35%2dUN%5f%2d1%2dUS%5f0%2dT%5f1609157760479; userIPType_abo=1; userName_dsr=""; enc_abo=A8A4B0A033E2E8462153267F85A75FB0; groupId=431; conter_abo=1; td_cookie=847914857; JSESSIONID=AEC1D5F28B3FAD1D7B3AA8026484D0FD.tomcat217; duxiu=userName%5fdsr%2c%3d0%2c%21userid%5fdsr%2c%3d%2d1%2c%21char%5fdsr%2c%3d%2c%21metaType%2c%3d0%2c%21logo%5fdsr%2c%3dareas%2fucdrs%2fimages%2flogo%2ejpg%2c%21logosmall%5fdsr%2c%3darea%2fucdrs%2flogosmall%2ejpg%2c%21title%5fdsr%2c%3d%u5168%u56fd%u56fe%u4e66%u9986%u53c2%u8003%u54a8%u8be2%u8054%u76df%2c%21url%5fdsr%2c%3d%2c%21compcode%5fdsr%2c%3d%2c%21province%5fdsr%2c%3d%2c%21isdomain%2c%3d0%2c%21showcol%2c%3d0%2c%21isfirst%2c%3d0%2c%21og%2c%3d0%2c%21ogvalue%2c%3d0%2c%21cdb%2c%3d0%2c%21userIPType%2c%3d1%2c%21lt%2c%3d0%2c%21enc%5fdsr%2c%3dB2C28BA4F1CB4E90749A4F0B42A17004; AID_dsr=689; userId_abo=%2d1; schoolid_abo=689; user_enc_abo=B5AB06A2BD20A0BC011FBFEE2B9757CB; idxdom=www%2eucdrs%2esuperlib%2enet; route=baa7aa364b46f263616ef900bc384022; searchcount=13",
        "Host": "book.ucdrs.superlib.net",
        "Referer": "http://book.ucdrs.superlib.net/search?Field=all&channel=search&sw=231",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",

    }

    def search(self):
        response = requests.get(
            Book.search_base_url + self.s, headers=Book.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for i in soup.find_all("table", {"class": "book1"}):
            # url = re.compile(r'<h2.*?><a\b[^>]+\bhref=\\"([^"]*)"[^>]*>.+?</a></h2>').findall(str(i.a))
            url = re.compile(r'<a.+?href=\"(.+?)\".*>').findall(str(i.a))
            b = re.sub(r'&amp;', '&', url[0])  # 前面是正则表达式，匹配多种字符（串）
            # print(i.a)
            # print(book_detail_url + b)
            # print(url, "\n\n\n")
            res = requests.get(Book.book_detail_url + b, headers=Book.headers)

            book_detail_soup = BeautifulSoup(res.text, "html.parser")
            for j in book_detail_soup.find_all("div", {"class": "leftnav_tu"}):
                url = re.compile(r'<a.+?href=\"(.+?)\".*>').findall(str(j))
                name = j.find_all("div", {"class": "tutilte"})[0].text
                content = j.find_all("div", {"class": "tu_content"})[0].text
                content = "".join(content.split())
                content = content.replace("内容提要:", "")
                # print()
                x = url[0].replace("×tr", "&amp;timestr")
                # print(url[0].replace("×tr", "&amp;timestr"))
                book_detail = {'url': "http://book.ucdrs.superlib.net" + x, "name": name, "content": content}
                s = ""
                for k in j.find_all("dd"):
                    # bd = re.compile(r'【[\w\W]+】[\w\W]+').findall(str(k))
                    bd = k.text.replace(" ", "")
                    ko = "".join(bd.split())
                    ko = ko.replace("【", "")
                    ko = ko.split("】")
                    # print(ko)
                    book_detail[ko[0]] = ko[1]
                # print(j)
                img_url = re.compile(r'<img.+?src=\"(.+?)\".*>').findall(str(j))[1]
                book_detail["img_url"] = img_url
                # print(img_url[1])
                # print(book_detail)

                scs = book_detail_soup.find_all("script")
                # print(scs[4])
                adid = re.compile(r'var.+?adid=(.+?);.*').findall(str(scs[4]))[0]
                groupid = re.compile(r'var.+?groupid = (.+?);.*').findall(str(scs[4]))[0]

                book_detail['adid'] = adid
                book_detail['groupid'] = groupid
                # book_detail['script_var'] = scs[4]
                # book_detail["script_fun"] = scs[-1]
                self.book_list.append(book_detail)
        return self.beautiful_book_list(self.book_list)

    def beautiful_book_list(self, book_list):
        for i in range(len(book_list)):
            for j in self.keys:
                if j not in book_list[i]:
                    book_list[i][j] = ""
        new_book_list = []

        for i in book_list:
            j = {"name": i["name"], "content": i["content"], "url": i["url"], "price": i["原书定价"], "main_word": i["主题词"],
                 "public_library": i["出版项"], "group_id": i["groupid"], "books_name": i["丛书名"], "isbn_card": i["ISBN号"],
                 "state_card": i["形态项"], "adid": i["adid"], "base_content_type": i["参考文献格式"], "img_url": i["img_url"],
                 "maker": i["作者"], "type_card": i["中图法分类号"]}
            new_book_list.append(j)
        return new_book_list

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()

    """
    http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000001236435&amp;d=6CB862DD12F4968717965A694C43310B&amp;fenlei=10020101
    http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000004823871&d=1D61D5F56AFFC05D1D67BCA8183A290D&fenlei=1035
    """
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    # print(response.text)

    # 查看响应内容，response.content返回的字节流数据
    # print(response.content)

    # 查看完整url地址
    # print(response.content)

    # 查看响应头部字符编码
    # print(response.encoding)

    # 查看响应码
    # print(response.status_code)
    #

    #


# print(book_detail_soup.find_all("script")[4])
# print(book_detail_soup.find_all("script")[-1])

# print(book_list)
# sw = ""
# for j in book_list:
#     for i in j.keys():
#         sw = sw + str(i) + ","
#     sw = sw + "\n"
# for i in book_list:
#     for j in i.values():
#         sw = sw + str(j) + ","
#     sw = sw + "\n"
#
# with open("a.csv", "w", encoding="utf-8") as f:
#     f.write(sw)
#
# for i in soup.find_all("div", {"class": "book1"}):
#     print(i, "\n\n\n")


# for i in soup.find_all("table", {"class": "book1"}):
#     # url = re.compile(r'<h2.*?><a\b[^>]+\bhref=\\"([^"]*)"[^>]*>.+?</a></h2>').findall(str(i.a))
#     url = re.compile(r'<a.+?href=\"(.+?)\".*>').findall(str(i.a))
#     b = re.sub(r'&amp;', '&', url[0])  # 前面是正则表达式，匹配多种字符（串）
#     # print(i.a)
#     # print(book_detail_url + b)
#     # print(url, "\n\n\n")
#     res = requests.get(book_detail_url+b, headers=headers)
#     book_detail_soup = BeautifulSoup(res)
#     book_detail_soup.find_all("div",{"class":"tubox"})

"http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000030231246&d=C2762B1E844D5A986C4BE4FD8AA63306&fenlei=0705170301"
"http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000007489420&d=CCEE8770E5977BE7C2BE10EA1E788E2F&fenlei=0804010834"
"""
【作　者】王晓川编著
						
			
【ISBN号】978-7-5544-1682-2
【中图法分类号】G622.0
【原书定价】39.00
【主题词】小学教育-教学研究
"""

""" search params
    channel: search
    gtag: 
    sw: 12
    ecode: utf-8
    Field: all
    Sort: 
    adminid: 
    btype: 
    seb: 0
    pid: 0
    year: 
    sectyear: 
    showc: 0
    fenleiID: 
    searchtype: 
    authid: 0
    exp: 0
    expertsw: 
    Pages: 23
    
    """
