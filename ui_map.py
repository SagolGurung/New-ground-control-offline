# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Map_UI(object):
    def setupUi(self, Map_UI):
        if not Map_UI.objectName():
            Map_UI.setObjectName(u"Map_UI")
        Map_UI.resize(2197, 1170)
        Map_UI.setStyleSheet(u"QPushButton#menu{\n"
"background-color:qlineargradient(spread:pad, x1:0.49, y1:1, x2:1, y2:0, stop:0 rgba(25, 112, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(Map_UI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mapframe = QFrame(self.centralwidget)
        self.mapframe.setObjectName(u"mapframe")
        self.mapframe.setGeometry(QRect(-10, 0, 1981, 1111))
        self.mapframe.setStyleSheet(u"")
        self.rightframe = QFrame(self.mapframe)
        self.rightframe.setObjectName(u"rightframe")
        self.rightframe.setGeometry(QRect(1410, 90, 491, 951))
        self.rightframe.setStyleSheet(u"QFrame#rightframe{font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"background-color:qlineargradient(spread:pad, x1:0.526, y1:1, x2:1, y2:0, stop:0 rgba(179, 179, 179, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QLabel#north{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#south{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#east{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QLabel#west{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel#pointer{\n"
"border:none;\n"
"}\n"
"QProgressBar#pbfuel{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"\n"
"QProgressBar#barleft{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QProgressBar#barright{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QLabel#speed{\n"
"border:2px solid black;\n"
"}\n"
"QLabel{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"\n"
"Line#point{\n"
"\n"
"background-color: red;\n"
"}\n"
"QPushButton{\n"
"border:2px solid black;\n"
"}\n"
"\n"
"QSlider{\n"
"border:2px solid black;\n"
"}")
        self.monitor = QPushButton(self.rightframe)
        self.monitor.setObjectName(u"monitor")
        self.monitor.setGeometry(QRect(0, 10, 71, 31))
        self.monitor.setCheckable(True)
        self.control = QPushButton(self.rightframe)
        self.control.setObjectName(u"control")
        self.control.setGeometry(QRect(70, 10, 71, 31))
        self.control.setCheckable(True)
        self.ident = QPushButton(self.rightframe)
        self.ident.setObjectName(u"ident")
        self.ident.setGeometry(QRect(340, 10, 61, 31))
        self.ident.setStyleSheet(u"")
        self.speed = QLabel(self.rightframe)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(0, 60, 71, 31))
        self.speed.setStyleSheet(u"")
        self.speed.setTextFormat(Qt.PlainText)
        self.speed.setWordWrap(False)
        self.start = QPushButton(self.rightframe)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(20, 680, 89, 81))
        self.start.setLayoutDirection(Qt.LeftToRight)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet(u"")
        self.stop = QPushButton(self.rightframe)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(20, 850, 89, 81))
        self.meter = QDial(self.rightframe)
        self.meter.setObjectName(u"meter")
        self.meter.setGeometry(QRect(150, 730, 161, 131))
        self.slideleft = QSlider(self.rightframe)
        self.slideleft.setObjectName(u"slideleft")
        self.slideleft.setGeometry(QRect(40, 150, 22, 251))
        self.slideleft.setOrientation(Qt.Vertical)
        self.slideright = QSlider(self.rightframe)
        self.slideright.setObjectName(u"slideright")
        self.slideright.setGeometry(QRect(370, 150, 22, 251))
        self.slideright.setOrientation(Qt.Vertical)
        self.barleft = QProgressBar(self.rightframe)
        self.barleft.setObjectName(u"barleft")
        self.barleft.setGeometry(QRect(350, 670, 51, 161))
        self.barleft.setLayoutDirection(Qt.LeftToRight)
        self.barleft.setValue(24)
        self.barleft.setOrientation(Qt.Vertical)
        self.barleft.setTextDirection(QProgressBar.TopToBottom)
        self.barright = QProgressBar(self.rightframe)
        self.barright.setObjectName(u"barright")
        self.barright.setGeometry(QRect(410, 670, 51, 161))
        self.barright.setLayoutDirection(Qt.LeftToRight)
        self.barright.setValue(24)
        self.barright.setOrientation(Qt.Vertical)
        self.barright.setTextDirection(QProgressBar.TopToBottom)
        self.overrideleft = QLabel(self.rightframe)
        self.overrideleft.setObjectName(u"overrideleft")
        self.overrideleft.setGeometry(QRect(0, 110, 101, 31))
        self.overrideleft.setStyleSheet(u"")
        self.overrideleft.setTextFormat(Qt.PlainText)
        self.overrideleft.setWordWrap(False)
        self.overrideright = QLabel(self.rightframe)
        self.overrideright.setObjectName(u"overrideright")
        self.overrideright.setGeometry(QRect(340, 110, 111, 31))
        self.overrideright.setStyleSheet(u"")
        self.overrideright.setTextFormat(Qt.PlainText)
        self.overrideright.setWordWrap(False)
        self.lcdNumber = QLCDNumber(self.rightframe)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(200, 780, 64, 23))
        self.ovl1 = QLabel(self.rightframe)
        self.ovl1.setObjectName(u"ovl1")
        self.ovl1.setGeometry(QRect(70, 150, 61, 31))
        self.ovl1.setWordWrap(False)
        self.ovl2 = QLabel(self.rightframe)
        self.ovl2.setObjectName(u"ovl2")
        self.ovl2.setGeometry(QRect(70, 220, 61, 31))
        self.ovl2.setWordWrap(False)
        self.ovl3 = QLabel(self.rightframe)
        self.ovl3.setObjectName(u"ovl3")
        self.ovl3.setGeometry(QRect(70, 290, 61, 31))
        self.ovl3.setWordWrap(False)
        self.ovl4 = QLabel(self.rightframe)
        self.ovl4.setObjectName(u"ovl4")
        self.ovl4.setGeometry(QRect(70, 360, 61, 31))
        self.ovl4.setWordWrap(False)
        self.ruler_2 = QLabel(self.rightframe)
        self.ruler_2.setObjectName(u"ruler_2")
        self.ruler_2.setGeometry(QRect(340, 150, 21, 251))
        self.ruler_2.setWordWrap(False)
        self.ov1 = QLabel(self.rightframe)
        self.ov1.setObjectName(u"ov1")
        self.ov1.setGeometry(QRect(400, 150, 71, 31))
        self.ov1.setWordWrap(False)
        self.ov2 = QLabel(self.rightframe)
        self.ov2.setObjectName(u"ov2")
        self.ov2.setGeometry(QRect(400, 220, 71, 31))
        self.ov2.setWordWrap(False)
        self.ov3 = QLabel(self.rightframe)
        self.ov3.setObjectName(u"ov3")
        self.ov3.setGeometry(QRect(400, 290, 71, 31))
        self.ov3.setWordWrap(False)
        self.ov4 = QLabel(self.rightframe)
        self.ov4.setObjectName(u"ov4")
        self.ov4.setGeometry(QRect(400, 360, 71, 31))
        self.ov4.setWordWrap(False)
        self.ruler_3 = QLabel(self.rightframe)
        self.ruler_3.setObjectName(u"ruler_3")
        self.ruler_3.setGeometry(QRect(10, 150, 21, 251))
        self.ruler_3.setWordWrap(False)
        self.speed1 = QLabel(self.rightframe)
        self.speed1.setObjectName(u"speed1")
        self.speed1.setGeometry(QRect(70, 60, 71, 31))
        self.speed1.setStyleSheet(u"")
        self.speed1.setTextFormat(Qt.PlainText)
        self.speed1.setWordWrap(False)
        self.speed1_2 = QLabel(self.rightframe)
        self.speed1_2.setObjectName(u"speed1_2")
        self.speed1_2.setGeometry(QRect(400, 10, 61, 31))
        self.speed1_2.setStyleSheet(u"")
        self.speed1_2.setTextFormat(Qt.PlainText)
        self.speed1_2.setWordWrap(False)
        self.msl = QLabel(self.rightframe)
        self.msl.setObjectName(u"msl")
        self.msl.setGeometry(QRect(340, 50, 61, 31))
        self.msl.setStyleSheet(u"")
        self.msl.setTextFormat(Qt.PlainText)
        self.msl.setWordWrap(False)
        self.speed_3 = QLabel(self.rightframe)
        self.speed_3.setObjectName(u"speed_3")
        self.speed_3.setGeometry(QRect(400, 50, 61, 31))
        self.speed_3.setStyleSheet(u"")
        self.speed_3.setTextFormat(Qt.PlainText)
        self.speed_3.setWordWrap(False)
        self.gs = QLabel(self.rightframe)
        self.gs.setObjectName(u"gs")
        self.gs.setGeometry(QRect(0, 550, 41, 31))
        self.gs.setStyleSheet(u"")
        self.gs.setTextFormat(Qt.PlainText)
        self.gs.setWordWrap(False)
        self.ws = QLabel(self.rightframe)
        self.ws.setObjectName(u"ws")
        self.ws.setGeometry(QRect(0, 590, 41, 31))
        self.ws.setStyleSheet(u"")
        self.ws.setTextFormat(Qt.PlainText)
        self.ws.setWordWrap(False)
        self.gs1 = QLabel(self.rightframe)
        self.gs1.setObjectName(u"gs1")
        self.gs1.setGeometry(QRect(40, 550, 31, 31))
        self.gs1.setStyleSheet(u"")
        self.gs1.setTextFormat(Qt.PlainText)
        self.gs1.setWordWrap(False)
        self.climb = QLabel(self.rightframe)
        self.climb.setObjectName(u"climb")
        self.climb.setGeometry(QRect(80, 550, 61, 31))
        self.climb.setStyleSheet(u"")
        self.climb.setTextFormat(Qt.PlainText)
        self.climb.setWordWrap(False)
        self.ws1 = QLabel(self.rightframe)
        self.ws1.setObjectName(u"ws1")
        self.ws1.setGeometry(QRect(40, 590, 31, 31))
        self.ws1.setStyleSheet(u"")
        self.ws1.setTextFormat(Qt.PlainText)
        self.ws1.setWordWrap(False)
        self.temp = QLabel(self.rightframe)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(80, 590, 91, 31))
        self.temp.setStyleSheet(u"")
        self.temp.setTextFormat(Qt.PlainText)
        self.temp.setWordWrap(False)
        self.gps = QLabel(self.rightframe)
        self.gps.setObjectName(u"gps")
        self.gps.setGeometry(QRect(290, 550, 71, 31))
        self.gps.setStyleSheet(u"")
        self.gps.setTextFormat(Qt.PlainText)
        self.gps.setWordWrap(False)
        self.agl = QLabel(self.rightframe)
        self.agl.setObjectName(u"agl")
        self.agl.setGeometry(QRect(290, 590, 71, 31))
        self.agl.setStyleSheet(u"")
        self.agl.setTextFormat(Qt.PlainText)
        self.agl.setWordWrap(False)
        self.climb1 = QLabel(self.rightframe)
        self.climb1.setObjectName(u"climb1")
        self.climb1.setGeometry(QRect(140, 550, 61, 31))
        self.climb1.setStyleSheet(u"")
        self.climb1.setTextFormat(Qt.PlainText)
        self.climb1.setWordWrap(False)
        self.temp1 = QLabel(self.rightframe)
        self.temp1.setObjectName(u"temp1")
        self.temp1.setGeometry(QRect(170, 590, 71, 31))
        self.temp1.setStyleSheet(u"")
        self.temp1.setTextFormat(Qt.PlainText)
        self.temp1.setWordWrap(False)
        self.compass = QWidget(self.rightframe)
        self.compass.setObjectName(u"compass")
        self.compass.setGeometry(QRect(140, 120, 191, 181))
        self.compass.setStyleSheet(u"")
        self.north = QLabel(self.compass)
        self.north.setObjectName(u"north")
        self.north.setGeometry(QRect(81, 10, 20, 20))
        self.north.setWordWrap(False)
        self.south = QLabel(self.compass)
        self.south.setObjectName(u"south")
        self.south.setGeometry(QRect(80, 150, 21, 20))
        self.south.setWordWrap(False)
        self.west = QLabel(self.compass)
        self.west.setObjectName(u"west")
        self.west.setGeometry(QRect(0, 80, 21, 20))
        self.west.setWordWrap(False)
        self.east = QLabel(self.compass)
        self.east.setObjectName(u"east")
        self.east.setGeometry(QRect(160, 80, 20, 20))
        self.east.setWordWrap(False)
        self.pointer = QLabel(self.compass)
        self.pointer.setObjectName(u"pointer")
        self.pointer.setGeometry(QRect(30, 60, 131, 51))
        self.course = QPushButton(self.rightframe)
        self.course.setObjectName(u"course")
        self.course.setGeometry(QRect(90, 460, 71, 31))
        self.course.setCheckable(True)
        self.launch = QPushButton(self.rightframe)
        self.launch.setObjectName(u"launch")
        self.launch.setGeometry(QRect(170, 460, 71, 31))
        self.launch.setCheckable(True)
        self.route = QPushButton(self.rightframe)
        self.route.setObjectName(u"route")
        self.route.setGeometry(QRect(250, 460, 71, 31))
        self.route.setCheckable(True)
        self.loiter = QPushButton(self.rightframe)
        self.loiter.setObjectName(u"loiter")
        self.loiter.setGeometry(QRect(170, 500, 71, 31))
        self.loiter.setCheckable(True)
        self.autolanding = QPushButton(self.rightframe)
        self.autolanding.setObjectName(u"autolanding")
        self.autolanding.setGeometry(QRect(250, 500, 121, 31))
        self.autolanding.setCheckable(True)
        self.mode = QLabel(self.rightframe)
        self.mode.setObjectName(u"mode")
        self.mode.setGeometry(QRect(90, 420, 61, 31))
        self.mode.setStyleSheet(u"")
        self.mode.setTextFormat(Qt.PlainText)
        self.mode.setWordWrap(False)
        self.mode1 = QLabel(self.rightframe)
        self.mode1.setObjectName(u"mode1")
        self.mode1.setGeometry(QRect(170, 420, 151, 31))
        self.mode1.setStyleSheet(u"")
        self.mode1.setTextFormat(Qt.PlainText)
        self.mode1.setWordWrap(False)
        self.gps1 = QLabel(self.rightframe)
        self.gps1.setObjectName(u"gps1")
        self.gps1.setGeometry(QRect(370, 550, 91, 31))
        self.gps1.setStyleSheet(u"")
        self.gps1.setTextFormat(Qt.PlainText)
        self.gps1.setWordWrap(False)
        self.agl1 = QLabel(self.rightframe)
        self.agl1.setObjectName(u"agl1")
        self.agl1.setGeometry(QRect(370, 590, 91, 31))
        self.agl1.setStyleSheet(u"")
        self.agl1.setTextFormat(Qt.PlainText)
        self.agl1.setWordWrap(False)
        self.point_2 = QFrame(self.rightframe)
        self.point_2.setObjectName(u"point_2")
        self.point_2.setGeometry(QRect(0, 530, 491, 16))
        self.point_2.setFrameShape(QFrame.HLine)
        self.point_2.setFrameShadow(QFrame.Sunken)
        self.point_4 = QFrame(self.rightframe)
        self.point_4.setObjectName(u"point_4")
        self.point_4.setGeometry(QRect(0, 90, 491, 16))
        self.point_4.setFrameShape(QFrame.HLine)
        self.point_4.setFrameShadow(QFrame.Sunken)
        self.mapwidget = QWidget(self.mapframe)
        self.mapwidget.setObjectName(u"mapwidget")
        self.mapwidget.setGeometry(QRect(-11, -11, 1941, 1131))
        self.mapwidget.raise_()
        self.rightframe.raise_()
        self.minimize_button = QPushButton(self.centralwidget)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(1830, 10, 21, 21))
        self.minimize_button.setStyleSheet(u"QPushButton {\n"
"    background-color:rgb(0, 191, 0);\n"
"\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(1890, 10, 21, 21))
        self.close_button.setStyleSheet(u"QPushButton {\n"
"    background-color: red;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.maximize_button = QPushButton(self.centralwidget)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(1860, 10, 21, 21))
        self.maximize_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(232, 232, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icon/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.menu = QPushButton(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(1790, 50, 89, 27))
        self.menu.setStyleSheet(u"")
        self.menu.setCheckable(True)
        Map_UI.setCentralWidget(self.centralwidget)

        self.retranslateUi(Map_UI)
        self.menu.toggled.connect(self.rightframe.setVisible)

        QMetaObject.connectSlotsByName(Map_UI)
    # setupUi

    def retranslateUi(self, Map_UI):
        Map_UI.setWindowTitle(QCoreApplication.translate("Map_UI", u"MainWindow", None))
        self.monitor.setText(QCoreApplication.translate("Map_UI", u"Monitor", None))
        self.control.setText(QCoreApplication.translate("Map_UI", u"Control", None))
        self.ident.setText(QCoreApplication.translate("Map_UI", u"Ident", None))
        self.speed.setText(QCoreApplication.translate("Map_UI", u"SPEED", None))
        self.start.setText(QCoreApplication.translate("Map_UI", u"START", None))
        self.stop.setText(QCoreApplication.translate("Map_UI", u"STOP", None))
        self.overrideleft.setText(QCoreApplication.translate("Map_UI", u"OVERRIDE", None))
        self.overrideright.setText(QCoreApplication.translate("Map_UI", u"OVERRIDE", None))
        self.ovl1.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>50.6</p></body></html>", None))
        self.ovl2.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>50.2</p><p><br/></p></body></html>", None))
        self.ovl3.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>50</p><p><br/></p></body></html>", None))
        self.ovl4.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>49.6</p></body></html>", None))
        self.ruler_2.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p>\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p><br/></p><p><br/></p></body></html>", None))
        self.ov1.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>3450</p><p><br/></p></body></html>", None))
        self.ov2.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>3350</p></body></html>", None))
        self.ov3.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>3250<br/></p></body></html>", None))
        self.ov4.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p>3150</p></body></html>", None))
        self.ruler_3.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p>\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p> \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550</p><p><br/></p><p><br/></p></body></html>", None))
        self.speed1.setText(QCoreApplication.translate("Map_UI", u"50.2", None))
        self.speed1_2.setText(QCoreApplication.translate("Map_UI", u"3731", None))
        self.msl.setText(QCoreApplication.translate("Map_UI", u"MSL", None))
        self.speed_3.setText(QCoreApplication.translate("Map_UI", u"3300", None))
        self.gs.setText(QCoreApplication.translate("Map_UI", u"GS", None))
        self.ws.setText(QCoreApplication.translate("Map_UI", u"WS", None))
        self.gs1.setText(QCoreApplication.translate("Map_UI", u"50", None))
        self.climb.setText(QCoreApplication.translate("Map_UI", u"Climb", None))
        self.ws1.setText(QCoreApplication.translate("Map_UI", u"50", None))
        self.temp.setText(QCoreApplication.translate("Map_UI", u"Air Temp", None))
        self.gps.setText(QCoreApplication.translate("Map_UI", u"GPS", None))
        self.agl.setText(QCoreApplication.translate("Map_UI", u"AGL", None))
        self.climb1.setText(QCoreApplication.translate("Map_UI", u"0ft", None))
        self.temp1.setText(QCoreApplication.translate("Map_UI", u"29.9 C", None))
        self.north.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">N</span></p></body></html>", None))
        self.south.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">S</span></p></body></html>", None))
        self.west.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">W</span></p></body></html>", None))
        self.east.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">E</span></p></body></html>", None))
        self.pointer.setText(QCoreApplication.translate("Map_UI", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">\u25c1-------</span></p></body></html>", None))
        self.course.setText(QCoreApplication.translate("Map_UI", u"Course", None))
        self.launch.setText(QCoreApplication.translate("Map_UI", u"Launch", None))
        self.route.setText(QCoreApplication.translate("Map_UI", u"Route", None))
        self.loiter.setText(QCoreApplication.translate("Map_UI", u"Loiter", None))
        self.autolanding.setText(QCoreApplication.translate("Map_UI", u"Autolanding", None))
        self.mode.setText(QCoreApplication.translate("Map_UI", u"Mode", None))
        self.mode1.setText(QCoreApplication.translate("Map_UI", u"yoyo", None))
        self.gps1.setText("")
        self.agl1.setText("")
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.maximize_button.setText("")
        self.menu.setText(QCoreApplication.translate("Map_UI", u"\ud83d\udd3a", None))
    # retranslateUi

