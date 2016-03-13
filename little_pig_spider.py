from bs4 import BeautifulSoup
import requests

url_list = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 26)]

def get_url_detail(url): #定义函数从列表页抓取每个详情页的地址,url为列表页
    wb_data = requests.get(url) #请求页面
    soup = BeautifulSoup(wb_data.text, 'lxml') #做汤,解析网页信息
    url = soup.select('#page_list > ul > li > a') #定位得到含有房源网址的a标签信息
    return url #返回包含网址信息的列表

url_detail = [get_url_detail(url)[x].get('href') for url in url_list for x in range(12)]

def house_detail(url_detail):
    wb_data = requests.get(url_detail)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    imgs = soup.select('div.pho_show_l > div > div > img')
    prices = soup.select('div.day_l > span')
    landlord_names = soup.select('div.js_box.clearfix > div.w_240 > h6 > a')
    landlord_imgs = soup.select('div.js_box.clearfix > div.member_pic > a > img')
    sexes = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for title, address, img, price, landlord_name, landlord_img, sex in zip(titles, addresses, imgs, prices, landlord_names,landlord_imgs, sexes):
        data = {
            'title': title.get_text(),
            'address': list(address.stripped_strings),
            'img': img.get('src'), #???为什么没图??? 因为imgs没有指向img标签!!!哈哈哈
            'price': price.get_text(),
            'landlord_name': landlord_name.get_text(),
            'landlord_img': landlord_img.get('src'),
            'sex': 'femal' if 'member_ico1' in sex.get('class') else 'male' #sex是sexes列表里一个元素,可以使用get方法
        }
        print(data)


for url in url_detail:
    print(house_detail(url))