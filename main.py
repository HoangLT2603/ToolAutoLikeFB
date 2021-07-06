
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chromeoption = Options()
chromeoption.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chromeoption, executable_path="./chromedriver.exe")
driver.maximize_window()
url = "https://facebook.com/"
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

driver.get('https://www.facebook.com/hoanglaghi/')
sleep(3)
driver.execute_script("window.scrollTo(0,100);")
sleep(3)
post = driver.find_element_by_class_name("tvfksri0.ozuftl9m")
print(post)
like = post.find_element_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l")
print(like)
icon = like.get_attribute("aria-label")
print(icon)
# if icon == 'Thích':
#     like.click()
# else:
#     like.click()
#     sleep(2)
#     like.click()

