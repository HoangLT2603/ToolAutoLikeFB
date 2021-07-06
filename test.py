import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import xlsxwriter

chromeoption = Options()
chromeoption.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chromeoption, executable_path="./chromedriver.exe")
driver.maximize_window()
url = "https://www.facebook.com"
driver.get(url)

sleep(3)

email = driver.find_element_by_id("email")
email.send_keys("0328209917")

sleep(0.5)

passWord = driver.find_element_by_id("pass")
passWord.send_keys("17133023@ute")

btnLogin = driver.find_element_by_name("login")
btnLogin.click()

sleep(3)

driver.get("https://www.facebook.com/profile.php?id=100033153854649&sk=friends")

sleep(2)
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(random.randint(7, 20))

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


workbook = xlsxwriter.Workbook('Example.xlsx')
worksheet = workbook.add_worksheet()

listFriend = driver.find_elements_by_xpath("//div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']")
print(len(listFriend))
row = 0
for x in listFriend:
    try:
        link = x.find_element_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.q9uorilb.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.wkznzc2l.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l.pioscnbf.etr7akla")
        name = x.find_element_by_class_name("d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.mdeji52x.a5q79mjw.g1cxx5fr.lrazzd5p.oo9gr5id")
    except:
        continue
    _link = link.get_attribute('href')
    print(name.text +"-"+ _link)
    worksheet.write(row, 0, str(name.text))
    worksheet.write(row, 1, str(_link))
    row +=1
workbook.close()