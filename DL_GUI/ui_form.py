# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QStatusBar, QWidget)

from plotwidget import PlotWidget
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/main.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionZapisz_do_Excela = QAction(MainWindow)
        self.actionZapisz_do_Excela.setObjectName(u"actionZapisz_do_Excela")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graph = PlotWidget(self.page)
        self.graph.setObjectName(u"graph")
        self.graph.setMinimumSize(QSize(0, 300))

        self.gridLayout_4.addWidget(self.graph, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 5, 8)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"            border: 1px solid black;\n"
"            padding: 10px;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton::hover {\n"
"            background-color: rgb(220, 220, 220);\n"
"        }")

        self.gridLayout.addWidget(self.start_btn, 4, 9, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(10000, 60))

        self.gridLayout.addWidget(self.label_2, 6, 4, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 200))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.slider = QSlider(self.groupBox_2)
        self.slider.setObjectName(u"slider")
        self.slider.setMinimumSize(QSize(250, 0))
        self.slider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider, 3, 4, 1, 8)

        self.play_btn = QPushButton(self.groupBox_2)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMaximumSize(QSize(50, 16777215))
        self.play_btn.setStyleSheet(u"border: 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QSize(20, 20))

        self.gridLayout_6.addWidget(self.play_btn, 3, 1, 1, 1)

        self.time_label = QLabel(self.groupBox_2)
        self.time_label.setObjectName(u"time_label")

        self.gridLayout_6.addWidget(self.time_label, 3, 12, 1, 1)

        self.pause_btn = QPushButton(self.groupBox_2)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setMaximumSize(QSize(50, 16777215))
        self.pause_btn.setStyleSheet(u"border: 0px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon2)
        self.pause_btn.setIconSize(QSize(20, 40))

        self.gridLayout_6.addWidget(self.pause_btn, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 12)

        self.file_name = QLineEdit(self.groupBox_2)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout_6.addWidget(self.file_name, 1, 1, 1, 10)

        self.stop_btn = QPushButton(self.groupBox_2)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(24, 24))
        self.stop_btn.setStyleSheet(u"border: 0px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon3)
        self.stop_btn.setIconSize(QSize(42, 42))
        self.stop_btn.setFlat(False)

        self.gridLayout_6.addWidget(self.stop_btn, 3, 3, 1, 1)

        self.file_btn = QPushButton(self.groupBox_2)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"            border: 1px solid black;\n"
"            padding: 5px;\n"
"            border-radius: 10px;\n"
"        }\n"
"\n"
"QPushButton::hover {\n"
"            background-color: rgb(220, 220, 220)\n"
"        }")

        self.gridLayout_6.addWidget(self.file_btn, 1, 11, 1, 1)

        self.warning = QLabel(self.groupBox_2)
        self.warning.setObjectName(u"warning")
        self.warning.setMinimumSize(QSize(0, 30))
        self.warning.setMaximumSize(QSize(16777215, 30))
        self.warning.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_6.addWidget(self.warning, 2, 1, 1, 12)


        self.gridLayout.addWidget(self.groupBox_2, 0, 8, 3, 3)

        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 100))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(10000, 60))
        font = QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 4, 1, 2)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_7 = QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_15 = QLabel(self.page_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(10000, 60))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_2, 3, 8, 1, 3)

        self.left_btn = QPushButton(self.centralwidget)
        self.left_btn.setObjectName(u"left_btn")
        self.left_btn.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_btn.setIcon(icon4)
        self.left_btn.setIconSize(QSize(40, 20))

        self.gridLayout.addWidget(self.left_btn, 4, 8, 1, 1)

        self.right_btn = QPushButton(self.centralwidget)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setStyleSheet(u"border:none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.right_btn.setIcon(icon5)
        self.right_btn.setIconSize(QSize(40, 20))

        self.gridLayout.addWidget(self.right_btn, 4, 10, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 160))
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 2, 2, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 6, 2, 1)

        self.metal = QLineEdit(self.groupBox)
        self.metal.setObjectName(u"metal")
        self.metal.setFocusPolicy(Qt.NoFocus)
        self.metal.setStyleSheet(u"border: 1px solid black;")
        self.metal.setReadOnly(True)

        self.gridLayout_5.addWidget(self.metal, 1, 11, 1, 1)

        self.hiphop = QLineEdit(self.groupBox)
        self.hiphop.setObjectName(u"hiphop")
        self.hiphop.setFocusPolicy(Qt.NoFocus)
        self.hiphop.setStyleSheet(u"border: 1px solid black;")
        self.hiphop.setReadOnly(True)

        self.gridLayout_5.addWidget(self.hiphop, 1, 8, 1, 1)

        self.classical = QLineEdit(self.groupBox)
        self.classical.setObjectName(u"classical")
        self.classical.setFocusPolicy(Qt.NoFocus)
        self.classical.setStyleSheet(u"border: 1px solid black;")
        self.classical.setReadOnly(True)

        self.gridLayout_5.addWidget(self.classical, 1, 4, 1, 2)

        self.jazz = QLineEdit(self.groupBox)
        self.jazz.setObjectName(u"jazz")
        self.jazz.setFocusPolicy(Qt.NoFocus)
        self.jazz.setStyleSheet(u"border: 1px solid black;")
        self.jazz.setReadOnly(True)

        self.gridLayout_5.addWidget(self.jazz, 2, 8, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 2, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 7, 1, 1)

        self.rock = QLineEdit(self.groupBox)
        self.rock.setObjectName(u"rock")
        self.rock.setFocusPolicy(Qt.NoFocus)
        self.rock.setStyleSheet(u"border: 1px solid black;")
        self.rock.setReadOnly(True)

        self.gridLayout_5.addWidget(self.rock, 2, 14, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 13, 1, 1)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 1, 12, 2, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 2, 10, 1, 1)

        self.blues = QLineEdit(self.groupBox)
        self.blues.setObjectName(u"blues")
        self.blues.setFocusPolicy(Qt.NoFocus)
        self.blues.setStyleSheet(u"border: 1px solid black;")
        self.blues.setReadOnly(True)

        self.gridLayout_5.addWidget(self.blues, 1, 1, 1, 1)

        self.disco = QLineEdit(self.groupBox)
        self.disco.setObjectName(u"disco")
        self.disco.setFocusPolicy(Qt.NoFocus)
        self.disco.setStyleSheet(u"border: 1px solid black;")
        self.disco.setReadOnly(True)

        self.gridLayout_5.addWidget(self.disco, 2, 4, 1, 1)

        self.pop = QLineEdit(self.groupBox)
        self.pop.setObjectName(u"pop")
        self.pop.setFocusPolicy(Qt.NoFocus)
        self.pop.setStyleSheet(u"border: 1px solid black;")
        self.pop.setReadOnly(True)

        self.gridLayout_5.addWidget(self.pop, 2, 11, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 1, 3, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 9, 2, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 10, 1, 1)

        self.reggae = QLineEdit(self.groupBox)
        self.reggae.setObjectName(u"reggae")
        self.reggae.setFocusPolicy(Qt.NoFocus)
        self.reggae.setStyleSheet(u"border: 1px solid black;")
        self.reggae.setReadOnly(True)

        self.gridLayout_5.addWidget(self.reggae, 1, 14, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 15)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 13, 1, 1)

        self.country = QLineEdit(self.groupBox)
        self.country.setObjectName(u"country")
        self.country.setFocusPolicy(Qt.NoFocus)
        self.country.setStyleSheet(u"border: 1px solid black;")
        self.country.setReadOnly(True)

        self.gridLayout_5.addWidget(self.country, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 1, 7, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 11)

        self.predict_line = QLineEdit(self.centralwidget)
        self.predict_line.setObjectName(u"predict_line")
        self.predict_line.setMinimumSize(QSize(150, 0))
        self.predict_line.setMaximumSize(QSize(120, 16777215))
        self.predict_line.setStyleSheet(u"border: 1px solid black;")
        self.predict_line.setReadOnly(True)

        self.gridLayout.addWidget(self.predict_line, 6, 5, 1, 1)

        self.confidence_line = QLineEdit(self.centralwidget)
        self.confidence_line.setObjectName(u"confidence_line")
        self.confidence_line.setMinimumSize(QSize(120, 0))
        self.confidence_line.setMaximumSize(QSize(120, 16777215))
        self.confidence_line.setStyleSheet(u"border: 1px solid black;")
        self.confidence_line.setReadOnly(True)

        self.gridLayout.addWidget(self.confidence_line, 6, 8, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 9, 1, 2)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 6, 7, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 6, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionZapisz_do_Excela.setText(QCoreApplication.translate("MainWindow", u"Zapisz do Excela", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wynik rozpoznania:", None))
        self.groupBox_2.setTitle("")
        self.play_btn.setText("")
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.pause_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz plik w formacie .mp3 lub .wav do przeprowadzenia analizy:", None))
        self.stop_btn.setText("")
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"Wybierz", None))
        self.warning.setText(QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MODEL SZYMKA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MODEL MFCC", None))
        self.left_btn.setText("")
        self.right_btn.setText("")
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blues:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Disco:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Jazz:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Country:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Rock:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pop:", None))
        self.pop.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Klasyczna:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Metal:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Detekcja gatunku muzyki - procentowe warto\u015bci dla obecnego utworu", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reggae:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hiphop:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Pewno\u015b\u0107:", None))
    # retranslateUi

