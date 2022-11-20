"""
2022 캡스톤 디자인 Helpiosk
아마존 클라우드 서비스를 사용한 NFC 결제 키오스크

개발 팀원: 정휘성, 김주하
"""



"""
설치 모듈 및 import 정보
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import PyQt5.QtWidgets as qtwid
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
"""
UI import 
"""
form_main = uic.loadUiType("test.ui")[0]
form_secondwindow = uic.loadUiType("on_line.ui")[0]  # 두 번째창 ui
form_secondwindow2 = uic.loadUiType("out_line.ui")[0]  # 세 번째창 ui
form_secondwindow3 = uic.loadUiType("ex_line.ui")[0]  # 네 번째창 ui
form_thirdwindow = uic.loadUiType("time.ui")[0]  # 시간제 선택 ui
form_paywindow = uic.loadUiType("myqt_2.ui")[0] # NFC 결제 확인 ui
form_outwindow = uic.loadUiType("myqt_3.ui")[0] # NFC 인증 ui


"""
시간제 선택 UI 시간제 버튼 정보 
"""
ITEM_INFO = [
    {"name": "1", "price": 1500,"time":1},
    {"name": "2", "price": 3000,"time":2},
    {"name": "3", "price": 5000,"time":3},
    {"name": "4", "price": 6500,"time":4},
    {"name": "5", "price": 15000,"time":10},
    {"name": "6", "price": 20000,"time":20},
]
"""
ADS / EC2 서버 로그인 정보
"""
host = 'database-2.csxt1tjqb6lq.ap-northeast-2.rds.amazonaws.com'
port1 = 3306
username = "admin"
database = "test"
password = "qltmxm1016"

# 각 좌석별 사용 가능 유무 확인



"""
메인 윈도우
"""
class MainWindow(QMainWindow,QWidget,form_main):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.showMaximized()

    def initUI(self):
        self.setupUi(self)
        self.on_line.clicked.connect(self.backbutton_in)
        self.out_line.clicked.connect(self.backbutton_out)
        self.ex_line.clicked.connect(self.backbutton_ex)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)


        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()


    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text= datetime.toString(Qt.DefaultLocaleShortDate)
        self.time_label.setText("   " + text)


    def backbutton_in(self):
        self.hide()  # 메인 윈도우 숨김
        self.first = on_line()
        self.first.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def backbutton_out(self):
        self.hide()  # 메인 윈도우 숨김
        self.first = out_line()
        self.first.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def backbutton_ex(self):
        self.hide()  # 메인 윈도우 숨김
        self.first = ex_line()
        self.first.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized() # 두번째창 닫으면 다시 첫 번째 창 보여 짐

"""
입실 버튼
"""
class on_line(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        super(on_line, self).__init__()
        self.initUI()
        self.showMaximized()  # 두번째창 실행

    def initUI(self):
        self.setupUi(self)
        self.backB_2.clicked.connect(self.Home1)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8', port=port1)
        cur = conn.cursor()
        sql = "SELECT 좌석유무 FROM 테스트 WHERE 좌석번호 = %s"

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (1,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_1.setText("1번 좌석\n사용중")
                        self.pButton_1.setStyleSheet("background-color: gainsboro")
                        self.pButton_1.setDisabled(True)
                    if data == ('무',):
                        self.pButton_1.setText("1번 좌석")
                        self.pButton_1.setStyleSheet("background-color:#eb9f9f")  # 기본 회색
                        self.pButton_1.clicked.connect(self.whktjr1)

            with conn.cursor() as cur:
                cur.execute(sql, (2,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_2.setText("2번 좌석\n사용중")
                        self.pButton_2.setStyleSheet("background-color: gainsboro")
                        self.pButton_2.setDisabled(True)
                    if data == ('무',):
                        self.pButton_2.setText("2번 좌석")
                        self.pButton_2.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_2.clicked.connect(self.whktjr2)
            with conn.cursor() as cur:
                cur.execute(sql, (3,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_3.setText("3번 좌석\n사용중")
                        self.pButton_3.setStyleSheet("background-color: gainsboro")
                        self.pButton_3.setDisabled(True)
                    if data == ('무',):
                        self.pButton_3.setText("3번 좌석")
                        self.pButton_3.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_3.clicked.connect(self.whktjr3)
            with conn.cursor() as cur:
                cur.execute(sql, (4,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_4.setText("4번 좌석\n사용중")
                        self.pButton_4.setStyleSheet("background-color: gainsboro")
                        self.pButton_4.setDisabled(True)
                    if data == ('무',):
                        self.pButton_4.setText("4번 좌석")
                        self.pButton_4.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_4.clicked.connect(self.whktjr4)
            with conn.cursor() as cur:
                cur.execute(sql, (5,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_5.setText("5번 좌석\n사용중")
                        self.pButton_5.setStyleSheet("background-color: gainsboro")
                        self.pButton_5.setDisabled(True)
                    if data == ('무',):
                        self.pButton_5.setText("5번 좌석")
                        self.pButton_5.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_5.clicked.connect(self.whktjr5)
            with conn.cursor() as cur:
                cur.execute(sql, (6,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_6.setText("6번 좌석\n사용중")
                        self.pButton_6.setStyleSheet("background-color: gainsboro")
                        self.pButton_6.setDisabled(True)
                    if data == ('무',):
                        self.pButton_6.setText("6번 좌석")
                        self.pButton_6.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_6.clicked.connect(self.whktjr6)
            with conn.cursor() as cur:
                cur.execute(sql, (7,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_7.setText("7번 좌석\n사용중")
                        self.pButton_7.setStyleSheet("background-color: gainsboro")
                        self.pButton_7.setDisabled(True)
                    if data == ('무',):
                        self.pButton_7.setText("7번 좌석")
                        self.pButton_7.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_7.clicked.connect(self.whktjr7)
            with conn.cursor() as cur:
                cur.execute(sql, (8,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_8.setText("8번 좌석\n사용중")
                        self.pButton_8.setStyleSheet("background-color: gainsboro")
                        self.pButton_8.setDisabled(True)
                    if data == ('무',):
                        self.pButton_8.setText("8번 좌석")
                        self.pButton_8.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_8.clicked.connect(self.whktjr8)
            with conn.cursor() as cur:
                cur.execute(sql, (9,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_9.setText("9번 좌석\n사용중")
                        self.pButton_9.setStyleSheet("background-color: gainsboro")
                        self.pButton_9.setDisabled(True)
                    if data == ('무',):
                        self.pButton_9.setText("9번 좌석")
                        self.pButton_9.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_9.clicked.connect(self.whktjr9)
            with conn.cursor() as cur:
                cur.execute(sql, (10,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_10.setText("10번 좌석\n사용중")
                        self.pButton_10.setStyleSheet("background-color: gainsboro")
                        self.pButton_10.setDisabled(True)
                    if data == ('무',):
                        self.pButton_10.setText("10번 좌석")
                        self.pButton_10.setStyleSheet("background-color: #eb9f9f")  # 기본 회색
                        self.pButton_10.clicked.connect(self.whktjr10)




    def whktjr1(self):
        text1='1'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr2(self):
        text1 = '2'
        self.sw = time_1(text1, '1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr3(self):
        text1 = '3'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized() # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr4(self):
        text1 = '4'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr5(self):
        text1 = '5'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr6(self):
        text1 = '6'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr7(self):
        text1 = '7'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr8(self):
        text1 = '8'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr9(self):
        text1 = '9'
        self.sw = time_1(text1, '1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐
    def whktjr10(self):
        text1 = '10'
        self.sw=time_1(text1,'1')
        self.sw.exec_()
        self.hide()  # 메인 윈도우 숨김
        self.second = time_1()
        self.second.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def Home1(self):
        #sys.exit()
        self.close()
        #self.second = MainWindow()

"""
연장 버튼
"""
class ex_line(QDialog, QWidget, form_secondwindow3):
    def __init__(self):
        super(ex_line, self).__init__()
        self.initUI()
        self.showMaximized()  # 두번째창 실행

    def initUI(self):
        self.setupUi(self)
        self.backB_2.clicked.connect(self.Home)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8', port=port1)
        cur = conn.cursor()
        sql = "SELECT 좌석유무 FROM 테스트 WHERE 좌석번호 = %s"

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (1,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_1.setText("1번 좌석\n사용중")
                        self.pButton_1.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_1.clicked.connect(self.whktjr1)
                    if data == ('무',):
                        self.pButton_1.setText("1번 좌석")
                        self.pButton_1.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_1.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (2,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_2.setText("2번 좌석\n사용중")
                        self.pButton_2.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_2.clicked.connect(self.whktjr2)
                    if data == ('무',):
                        self.pButton_2.setText("2번 좌석")
                        self.pButton_2.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_2.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (3,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_3.setText("3번 좌석\n사용중")
                        self.pButton_3.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_3.clicked.connect(self.whktjr3)
                    if data == ('무',):
                        self.pButton_3.setText("3번 좌석")
                        self.pButton_3.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_3.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (4,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_4.setText("4번 좌석\n사용중")
                        self.pButton_4.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_4.clicked.connect(self.whktjr4)
                    if data == ('무',):
                        self.pButton_4.setText("4번 좌석")
                        self.pButton_4.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_4.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (5,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_5.setText("5번 좌석\n사용중")
                        self.pButton_5.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_5.clicked.connect(self.whktjr5)
                    if data == ('무',):
                        self.pButton_5.setText("5번 좌석")
                        self.pButton_5.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_5.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (6,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_6.setText("6번 좌석\n사용중")
                        self.pButton_6.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_6.clicked.connect(self.whktjr6)
                    if data == ('무',):
                        self.pButton_6.setText("6번 좌석")
                        self.pButton_6.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_6.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (7,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_7.setText("7번 좌석\n사용중")
                        self.pButton_7.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_7.clicked.connect(self.whktjr7)
                    if data == ('무',):
                        self.pButton_7.setText("7번 좌석")
                        self.pButton_7.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_7.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (8,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_8.setText("8번 좌석\n사용중")
                        self.pButton_8.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_8.clicked.connect(self.whktjr8)
                    if data == ('무',):
                        self.pButton_8.setText("8번 좌석")
                        self.pButton_8.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_8.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (9,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_9.setText("9번 좌석\n사용중")
                        self.pButton_9.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_9.clicked.connect(self.whktjr9)
                    if data == ('무',):
                        self.pButton_9.setText("9번 좌석")
                        self.pButton_9.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_9.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (10,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_10.setText("10번 좌석\n사용중")
                        self.pButton_10.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_10.clicked.connect(self.whktjr10)
                    if data == ('무',):
                        self.pButton_10.setText("10번 좌석")
                        self.pButton_10.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_10.setDisabled(True)

    def whktjr1(self):
        seat1 = '1'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr2(self, get):
        seat1 = '2'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr3(self, get):
        seat1 = '3'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr4(self):
        seat1 = '4'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr5(self):
        seat1 = '5'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr6(self):
        seat1 = '6'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr7(self):
        seat1 = '7'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized() # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr8(self):
        seat1 = '8'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr9(self):
        seat1 = '9'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def whktjr10(self):
        seat1 = '10'
        self.swex = exlogin(seat1)
        self.swex.exec_()
        self.ex = exlogin()
        self.ex.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


    def Home(self):
        self.close()  # 창 닫기

"""
퇴실 버튼
"""
class out_line(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        super(out_line, self).__init__()
        self.initUI()
        self.showMaximized()  # 두번째창 실행

    def initUI(self):
        self.setupUi(self)
        self.backB_2.clicked.connect(self.Home)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8', port=port1)
        cur = conn.cursor()
        sql = "SELECT 좌석유무 FROM 테스트 WHERE 좌석번호 = %s"

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (1,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_1.setText("1번 좌석\n사용중")
                        self.pButton_1.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_1.clicked.connect(self.whktjr1)
                    if data == ('무',):
                        self.pButton_1.setText("1번 좌석")
                        self.pButton_1.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_1.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (2,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_2.setText("2번 좌석\n사용중")
                        self.pButton_2.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_2.clicked.connect(self.whktjr2)
                    if data == ('무',):
                        self.pButton_2.setText("2번 좌석")
                        self.pButton_2.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_2.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (3,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_3.setText("3번 좌석\n사용중")
                        self.pButton_3.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_3.clicked.connect(self.whktjr3)
                    if data == ('무',):
                        self.pButton_3.setText("3번 좌석")
                        self.pButton_3.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_3.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (4,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_4.setText("4번 좌석\n사용중")
                        self.pButton_4.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_4.clicked.connect(self.whktjr4)
                    if data == ('무',):
                        self.pButton_4.setText("4번 좌석")
                        self.pButton_4.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_4.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (5,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_5.setText("5번 좌석\n사용중")
                        self.pButton_5.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_5.clicked.connect(self.whktjr5)
                    if data == ('무',):
                        self.pButton_5.setText("5번 좌석")
                        self.pButton_5.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_5.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (6,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_6.setText("6번 좌석\n사용중")
                        self.pButton_6.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_6.clicked.connect(self.whktjr6)
                    if data == ('무',):
                        self.pButton_6.setText("6번 좌석")
                        self.pButton_6.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_6.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (7,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_7.setText("7번 좌석\n사용중")
                        self.pButton_7.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_7.clicked.connect(self.whktjr7)
                    if data == ('무',):
                        self.pButton_7.setText("7번 좌석")
                        self.pButton_7.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_7.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (8,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_8.setText("8번 좌석\n사용중")
                        self.pButton_8.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_8.clicked.connect(self.whktjr8)
                    if data == ('무',):
                        self.pButton_8.setText("8번 좌석")
                        self.pButton_8.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_8.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (9,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_9.setText("9번 좌석\n사용중")
                        self.pButton_9.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_9.clicked.connect(self.whktjr9)
                    if data == ('무',):
                        self.pButton_9.setText("9번 좌석")
                        self.pButton_9.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_9.setDisabled(True)
            with conn.cursor() as cur:
                cur.execute(sql, (10,))  # n번 좌석의 좌석유무 확인
                result = cur.fetchall()

                for data in result:
                    if data == ('유',):
                        self.pButton_10.setText("10번 좌석\n사용중")
                        self.pButton_10.setStyleSheet("background-color: #eb9f9f")
                        self.pButton_10.clicked.connect(self.whktjr10)
                    if data == ('무',):
                        self.pButton_10.setText("10번 좌석")
                        self.pButton_10.setStyleSheet("background-color: gainsboro")  # 기본 회색
                        self.pButton_10.setDisabled(True)

    def Home(self):
        self.close()  # 창 닫기

    def whktjr1(self):
        seat1 = '1'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr2(self):
        seat1 = '2'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr3(self,get):
        seat1 = '3'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr4(self):
        seat1 = '4'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr5(self):
        seat1 = '5'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr6(self):
        seat1 = '6'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr7(self):
        seat1 = '7'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr8(self):
        seat1 = '8'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr9(self):
        seat1 = '9'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def whktjr10(self):
        seat1 = '10'
        self.sw2 = outlogin(seat1)
        self.sw2.exec_()
        self.out = outlogin()
        self.out.exec()  # 두번째창 닫을때까지 기다림
        self.showMaximized()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

"""
시간제 선택
"""
class time_1(QDialog, QWidget, form_thirdwindow):
    def __init__(self,text,num):
        super(time_1, self).__init__()
        self.initUI()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()  # 두번째창 실행
        self.label_s.setText(text)
        self.label_5.setText(num)


    def initUI(self):
        self.setupUi(self)

        self.totalPrice.setText("0")
        self.totaltime.setText("0")
        self.item_selected = []

        self.home.clicked.connect(self.Home)
        self.pushButton.clicked.connect(lambda:self.item_clicked(0))
        self.pushButton_2.clicked.connect(lambda:self.item_clicked(1))
        self.pushButton_3.clicked.connect(lambda:self.item_clicked(2))
        self.pushButton_4.clicked.connect(lambda:self.item_clicked(3))
        self.pushButton_5.clicked.connect(lambda: self.item_clicked(4))
        self.pushButton_6.clicked.connect(lambda: self.item_clicked(5))
        self.btn_reset.clicked.connect(self.item_clearall)
        self.btn_pay.clicked.connect(self.item_pay)

    def Home(self):
        if self.label_5.text() == '1':
            self.three = on_line()
        elif self.label_5.text() == '2':
            self.three = ex_line()



    def item_show(self):
        count_item = []
        for _ in range(len(ITEM_INFO)):
            count_item.append(0)

        for i in self.item_selected:
            count_item[i] += 1

        model = QStandardItemModel()
        for x in range(len(ITEM_INFO)):
            if count_item[x] == 0:
                continue
            temp = QStandardItem("{}시간을 {}개 주문하였습니다.".format(ITEM_INFO[x]["name"], count_item[x]))
            model.appendRow(temp)
        self.timeList.setModel(model)




    def item_clicked(self, item):
        self.item_selected.append(item)
        self.item_show()
        totaltime = int(self.totaltime.text())
        total = int(self.totalPrice.text())

        self.totaltime.setText(str(totaltime + ITEM_INFO[self.item_selected[-1]]['time']))
        self.totalPrice.setText(str(total + ITEM_INFO[self.item_selected[-1]]['price']))



    """
        * item_clearall(self)
        * 모든 선택된 물품 초기화
        """

    def item_clearall(self):
        self.item_selected = []
        self.totalPrice.setText("0")
        self.totaltime.setText("0")
        self.item_show()

    """
    * item_pay(self)
    * 선택된 물품 구매, SecondWindow 클래스 사용
    """

    def item_pay(self):
        global pay_success
        #self.hide()
        paytime=int(self.totaltime.text())
        payprice =int(self.totalPrice.text())
        text1= int(self.label_s.text())

        if self.label_5.text() == '1':
            self.payto = paytoWindow(payprice,paytime,text1)
            self.payto.exec()
            pay_success = False
        elif self.label_5.text() == '2':
            self.exto = paytoex(payprice,paytime,text1)
            self.exto.exec()
            pay_success = False

        if pay_success:
            self.item_clearall()
        self.show()


"""
NFC 결제
"""
class paytoWindow(QDialog, QWidget, form_paywindow):
    def __init__(self, price,time,seat):
        super(paytoWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.label_Ttime.setText(f"{str(time)}시간")
        self.label_price.setText(f"{str(price)}원")
        self.label_seat.setText(f"{str(seat)}번 좌석")

        self.btn_card.clicked.connect(self.card)
        self.show()



    """
    * card(self)
    * 카드결제 진행
    """
    def card(self):
        global pay_success
        ret = QMessageBox.question(self, '결제 확인', '카드결제를 진행하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ret == QMessageBox.Yes:
            QMessageBox.information(self,'알림', 'NFC 태그 해주세요')

            import RPi.GPIO as gpio
            from mfrc522 import SimpleMFRC522

            CardReader = SimpleMFRC522()

            id2, text = CardReader.read()
            random_user = id2
            pay_success = True


            if pay_success == True:
                QMessageBox.information(self, '알림', '결제가 완료되었습니다')
                conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8',
                                  port=3306)
                cur = conn.cursor()

                sql = "INSERT INTO 결제정보(사용자명, 좌석번호, 금액, 구매시간) VALUES(%s, %s, %s, %s)"
                cur.execute(sql,
                            (str(random_user), self.label_seat.text(), self.label_price.text(), self.label_Ttime.text(),))  # 결제 정보 저장

                sql = "UPDATE 테스트 SET 좌석유무 = '유', 사용자명 = %s, 만료시간 =  DATE_ADD(NOW(), INTERVAL %s HOUR) WHERE 좌석번호 = %s"
                cur.execute(sql, (str(random_user), self.label_Ttime.text(), self.label_seat.text(),))
                conn.commit()  # 좌석 번호 4번인 거의 좌석 유무를 유로 바꿈 -> 결제된 후

                self.hide()
                self.off = MainWindow()


"""
연장 NFC 결제
"""
class paytoex(QDialog, QWidget, form_paywindow):
    def __init__(self, price,time,seat):
        super(paytoex, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.label_Ttime.setText(f"{str(time)}시간")
        self.label_price.setText(f"{str(price)}원")
        self.label_seat.setText(f"{str(seat)}번 좌석")

        self.btn_card.clicked.connect(self.card)
        self.show()



    """
    * card(self)
    * 카드결제 진행
    """
    def card(self):
        global pay_success
        ret = QMessageBox.question(self, '결제 확인', '카드결제를 진행하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ret == QMessageBox.Yes:
            QMessageBox.information(self,'알림', 'NFC 태그 해주세요')

            import RPi.GPIO as gpio
            from mfrc522 import SimpleMFRC522

            CardReader = SimpleMFRC522()

            id1, text = CardReader.read()
            random_user = id1

            pay_success = True


            if pay_success == True:
                QMessageBox.information(self, '알림', '결제가 완료되었습니다')
                conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8',
                                  port=3306)
                cur = conn.cursor()

                sql = "INSERT INTO 결제정보(사용자명, 좌석번호, 금액, 구매시간) VALUES(%s, %s, %s, %s)"
                cur.execute(sql,
                            (str(random_user), self.label_seat.text(), self.label_price.text(), self.label_Ttime.text(),))  # 결제 정보 저장

                sql = "UPDATE 테스트 SET 만료시간 = DATE_ADD(만료시간, INTERVAL %s HOUR) WHERE 좌석번호 = %s"
                cur.execute(sql,( self.label_Ttime.text(), self.label_seat.text(),))
                conn.commit()  # 좌석 번호 4번인 거의 좌석 유무를 유로 바꿈 -> 결제된 후

                self.hide()
                self.off = MainWindow()


"""
연장 좌석 인증
"""
class exlogin(QDialog, QWidget, form_outwindow):
    def __init__(self,seat):
        super(exlogin, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_card.clicked.connect(self.card3)
        self.label_id2.setText(str(seat))
        self.show()  # 두번째창 실행

    def card3(self):
        global pay_success
        ret = QMessageBox.question(self, '좌석 인증', '좌석 인증을 진행하시겠습니까?', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)

        if ret == QMessageBox.Yes:
            QMessageBox.information(self, '알림', 'NFC 태그 해주세요')

            import RPi.GPIO as gpio
            from mfrc522 import SimpleMFRC522

            CardReader = SimpleMFRC522()

            id4, text = CardReader.read()
            random_user = id4
            pay_success = True

            if pay_success == True:
                QMessageBox.information(self, '알림', '인증이 완료되었습니다')

                conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8', port=3306)
                cur = conn.cursor()

                sql = "SELECT 사용자명 FROM 테스트 WHERE 좌석번호 = %s"

                # 각 좌석별 사용 가능 유무 확인
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql, (self.label_id2.text(),))  # n번 좌석의 사용자명 확인
                        result = cur.fetchall()
                        for data in result:  # 사용자 ID 확인
                            if data == (str(random_user),):
                                self.off = time_1(self.label_id2.text(), '2')


"""
퇴실 좌석 인증
"""
class outlogin(QDialog, QWidget, form_outwindow):
    def __init__(self,seat):
        super(outlogin, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_card.clicked.connect(self.card2)
        self.label_id.setText(str(seat))

        self.show()  # 두번째창 실행

    def card2(self):
        global pay_success
        ret = QMessageBox.question(self, '퇴실 인증', '퇴실 인증을 진행하시겠습니까?', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)

        if ret == QMessageBox.Yes:
            QMessageBox.information(self, '알림', 'NFC 태그 해주세요')

            import RPi.GPIO as gpio
            from mfrc522 import SimpleMFRC522

            CardReader = SimpleMFRC522()

            id3, text = CardReader.read()
            random_user = id3
            pay_success = True

            if pay_success == True:
                QMessageBox.information(self, '알림', '퇴실이 완료되었습니다')

                conn = mc.connect(host=host, user=username, password=password, db=database, charset='utf8',port=3306)
                cur = conn.cursor()

                sql = "SELECT 사용자명 FROM 테스트 WHERE 좌석번호 = %s"


                # 각 좌석별 사용 가능 유무 확인
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(sql, (self.label_id.text(),))  # n번 좌석의 사용자명 확인
                        result = cur.fetchall()
                        for data in result:  # 사용자 ID 확인
                            if data == (str(random_user),):
                                sql = "UPDATE 테스트 SET 좌석유무 = '무', 사용자명 = NULL, 만료시간 = NULL, 잔여시간 = NULL WHERE 좌석번호 = %s"
                                cur.execute(sql, (self.label_id.text(),))
                                conn.commit()  # 좌석 번호 n번인 거의 좌석 유무를 무로 바꿈 -> 퇴실시

                #self.close()
                self.off = MainWindow()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())