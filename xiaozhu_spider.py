from bs4 import BeautifulSoup
import requests

'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Cookie': 'abtest_ABTest4SearchDate=b; OZ_1U_2282=vid=v6e0da7cade0e1.0&ctime=1457576600&ltime=1457576599; OZ_1Y_2282=erefer=-&eurl=http%3A//bj.xiaozhu.com/&etime=1457576572&ctime=1457576600&ltime=1457576599&compid=2282; __utma=29082403.1414901576.1457576573.1457576573.1457576573.1; __utmc=29082403; __utmz=29082403.1457576573.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}
'''
url = 'http://bj.xiaozhu.com/fangzi/1867872234.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
addresses = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
imgs = soup.select('div.pho_show_l > div > div > img') #就是这里要指向img标签
prices = soup.select('div.day_l > span')
landlord_names = soup.select('div.js_box.clearfix > div.w_240 > h6 > a')
landlord_imgs = soup.select('div.js_box.clearfix > div.member_pic > a > img')
sexes = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
#sex = sexes[0] #查看打印的sexes后,发现男性为ico，女性为ico1, sexes又为列表,遂取出第一个也是唯一一个元素

for title, address, img, price, landlord_name, landlord_img, sex in zip(titles, addresses, imgs, prices, landlord_names,landlord_imgs, sexes):
    data = {
        'title': title.get_text(),
        'address': list(address.stripped_strings)[0], #因只有一个元素,用列表取值方法取出
        'img': img.get('src'), #???为什么没图??? 因为imgs没有指向img标签!!!哈哈哈
        'price': price.get_text(),
        'landlord_name': landlord_name.get_text(),
        'landlord_img': landlord_img.get('src'),
        'sex': 'femal' if 'member_ico1' in sex.get('class') else 'male' #sex是sexes列表里一个元素,可以使用get方法
    }
    print(data)

I = open('info.txt', 'w')
I.write(str(list(zip(data.keys(), data.values()))))
I.close()
print('Done!')
print(list(zip(data.keys(), data.values())))

#sex = 'femal' if 'member_ico1' in s else 'male'
#print(s)
'''
print(landlord_imgs)
print(sexes)
print(sex)
print(sex.get('class'))
'''

'''
if 'ico1' in s:
    print('female')
else:
    print('male')
    '''