from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep
from re import sub
import datetime

def login():
    dr = webdriver.Chrome()
    dr.get('http://net.citycheb.ru/')

    UN = dr.find_element_by_css_selector('#message > div > div > div:nth-child(8) > input')
    PW = dr.find_element_by_css_selector('#message > div > div > div:nth-child(9) > input')

    UN.send_keys('СамаринН1')
    PW.send_keys('123457')

    sleep(1)


    school = Select(dr.find_element_by_id('schools'))

    school.select_by_visible_text('Лицей №3')

    sleep(1)


    CB = dr.find_element_by_css_selector('#message > div > div > div.row-center.row-submit > a > span')
    CB.click()

    sleep(3)

    try:
        but = dr.find_element_by_css_selector('body > div.block-content > div > div > div > div > div:nth-child(5) > div > div > div > div > button:nth-child(2) > span:nth-child(2)')
        but.click()
    except:
        f = None

    sleep(3)

    return dr

dr = login()

def last_add():


    h = dr.find_element_by_css_selector('body > div.block-content > div.content > div > div > div > form > div > div > div > div:nth-child(1) > div.adver-body')
    text = BeautifulSoup(h.get_attribute("outerHTML"))

    head = text.find_all('h3')[0]
    txt = dr.find_element_by_css_selector('body > div.block-content > div.content > div > div > div > form > div > div > div > div:nth-child(1) > div.adver-body > div.adver-content')
    txt = BeautifulSoup(txt.get_attribute("outerHTML"))

    return head.text + '\n' + txt.text


def get_diary():


    gl = dr.find_element_by_css_selector('body > div.header > div.navbar.navbar-default > nav > ul > li:nth-child(1) > a')
    gl.click()

    sleep(2)

    diar = dr.find_element_by_xpath('//*[@id="1"]/div[4]')
    diar.click()

    sleep(4)

    return dr

dr = get_diary()

d = dr.find_elements_by_class_name('day_table')


def today_tomorow(td):
    m = datetime.datetime.today()

    a = m.weekday()
    if td == 0 and a != 6:
        return a

    elif td == 0 and a == 6:
        return 0

    if td == 1 and a != 6 and a != 5:
        return a+1

    elif td == 1 and a == 6 or a == 5:
        return 0




def parse_homework(dn):

    days = BeautifulSoup(d[dn].get_attribute("outerHTML"))

    l = []
    ans = ''

    table = days.find_all('table')[1]
    lessons = table.find_all('tr')[2:]

    for i in lessons:
        k = i.find_all('td')

        try:
            les = k[1].a.text
        except:
            les = ' '


        try:
            hw = k[2].div.a.text
        except:
            hw = ' '




        dict = {
            'num' : k[0].text,
            'les' : les,
            'hw' : hw
        }
        l.append(dict)

    for i in l:
        n = i['num']
        les = i['les']
        hw = i['hw']
        ans = ans + n + '. ' + les + ': ' + hw + '\n' +'\n'



    return ans

def parse_tt(dn):

    days = BeautifulSoup(d[dn].get_attribute("outerHTML"))

    l = []
    ans = ''

    table = days.find_all('table')[1]
    lessons = table.find_all('tr')[2:]

    for i in lessons:
        k = i.find_all('td')

        try:
            les = k[1].a.text
        except:
            les = ' '

        try:
            time = k[1].div.text
        except:
            time = ' '



        time = sub(r'\n\t\t\t\t\t\t', '', time)
        time = sub(r'\n', '', time)

        dict = {
            'num': k[0].text,
            'les': les,
            'time': time,

        }
        l.append(dict)

    for i in l:
        n = i['num']
        les = i['les']
        time = i['time']
        ans = ans + n + '. ' + les + ': ' + time + '\n' + '\n'

    return ans

