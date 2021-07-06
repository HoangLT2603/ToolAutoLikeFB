import pandas as pd
import sys

import xlsxwriter
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsDropShadowEffect, QMainWindow, QCheckBox, QLabel, \
    QFileDialog
from PyQt5.QtGui import QIcon, QColor
from formMain import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listName = []
        self.listLink = []

        self.ui.btn_start.clicked.connect(self.likepost)
        self.ui.ckb_all.clicked.connect(self.selectAll)
        self.ui.spb_to.valueChanged.connect(self.select)
        self.ui.spb_from.valueChanged.connect(self.select)
        self.ui.btn_getLink.clicked.connect(self.getListFriend)
        self.ui.btn_choose_file.clicked.connect(self.open_dialog)
        self.show()

    def open_dialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/HOME', "Excel Files (*.xlsx)")
        if filePath != "":
            self.ui.txt_source_file.setText(filePath)
            self.load_list_friend()
    def load_list_friend(self):
        data = pd.read_excel(self.ui.txt_source_file.text(), header=None)
        data = pd.DataFrame(data)
        data.columns = ['Name', 'Link']
        total = len(data)
        for index in range(total):
            name = data.iloc[index]['Name']
            link = data.iloc[index]['Link']
            stt = QLabel()
            stt.setText(str(index))
            lk = QLabel()
            lk.setOpenExternalLinks(True)
            lk.setText("<a href='"+link+"'>"+link+"</a>")
            ckb = QCheckBox()
            ckb.setText(name)
            self.ui.layout.addWidget(stt, index, 0)
            self.ui.layout.addWidget(ckb, index, 1)
            self.ui.layout.addWidget(lk, index, 2)

            self.listName.append(ckb)
            self.listLink.append(link)
    def likepost(self):
        username = self.ui.txt_username.text()
        passW = self.ui.txt_pass.text()
        if username == "" or passW == "":
            self.ui.notify.setText("Email hoặc Password chưa được nhập !!")
        else:
            self.openChrome(username, passW)
            for i in range(0, len(self.listName)):
                try:
                    if self.listName[i].isChecked():
                        self.driver.get(self.listLink[i])
                        sleep(3)
                        post = self.driver.find_element_by_class_name("tvfksri0.ozuftl9m")
                        like = post.find_element_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l")
                        icon = like.get_attribute("aria-label")
                        if icon == 'Thích':
                            like.click()
                        else:
                            like.click()
                            sleep(2)
                            like.click()
                except:
                    continue
                sleep(random.randint(5, 15))
            self.driver.close()

    def selectAll(self):
        if self.ui.ckb_all.isChecked():
            for x in self.listName:
                x.setChecked(True)
        else:
            for x in self.listName:
                x.setChecked(False)

    def select(self):
        fr = int(self.ui.spb_from.text())
        to = int(self.ui.spb_to.text())
        self.ui.ckb_all.setChecked(False)
        if len(self.listName) > 0 and to > fr:
            for x in self.listName:
                x.setChecked(False)
            for i in range(fr, to+1):
                self.listName[i].setChecked(True)

    def openChrome(self, username, passW):
        chromeoption = Options()
        chromeoption.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chromeoption, executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        url = "https://facebook.com/"
        self.driver.get(url)
        sleep(3)
        email = self.driver.find_element_by_id("email")
        email.send_keys(username)
        sleep(0.5)
        passWord = self.driver.find_element_by_id("pass")
        passWord.send_keys(passW)
        btnLogin = self.driver.find_element_by_name("login")
        btnLogin.click()
        sleep(3)

    def getListFriend(self):

        url = self.ui.txt_link.text()
        if url == "":
            self.ui.notify.setText("Chưa nhập link !!")
        else:
            self.openChrome("0328209917", "17133023@ute")
            self.driver.get()
            sleep(2)
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                sleep(random.randint(7, 20))

                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            workbook = xlsxwriter.Workbook('listFriend.xlsx')
            worksheet = workbook.add_worksheet()

            listFriend = self.driver.find_elements_by_xpath(
                "//div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']")
            print(len(listFriend))
            row = 0
            for x in listFriend:
                try:
                    link = x.find_element_by_class_name(
                        "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.q9uorilb.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.wkznzc2l.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l.pioscnbf.etr7akla")
                    name = x.find_element_by_class_name(
                        "d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.mdeji52x.a5q79mjw.g1cxx5fr.lrazzd5p.oo9gr5id")
                except:
                    continue
                _link = link.get_attribute('href')
                print(name.text + "-" + _link)
                worksheet.write(row, 0, str(name.text))
                worksheet.write(row, 1, str(_link))
                row += 1
            workbook.close()
            self.driver.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())



