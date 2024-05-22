# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QStatusBar, QTableView, QWidget)

from plotwidget import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1000, 600)
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
        self.graph.setMinimumSize(QSize(0, 400))

        self.gridLayout_4.addWidget(self.graph, 0, 0, 2, 2)

        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_4.addWidget(self.tableView, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 2, 1)

        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.file_name = QLineEdit(self.page_3)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.file_name, 1, 1, 1, 8)

        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 6, 1, 1)

        self.predict_line = QLineEdit(self.page_3)
        self.predict_line.setObjectName(u"predict_line")

        self.gridLayout_2.addWidget(self.predict_line, 4, 7, 1, 3)

        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 3, 6, 1, 1)

        self.slider = QSlider(self.page_3)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider, 2, 4, 1, 5)

        self.play_btn = QPushButton(self.page_3)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.play_btn, 2, 1, 1, 1)

        self.time_label = QLabel(self.page_3)
        self.time_label.setObjectName(u"time_label")

        self.gridLayout_2.addWidget(self.time_label, 2, 9, 1, 1)

        self.stop_btn = QPushButton(self.page_3)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.stop_btn, 2, 3, 1, 1)

        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 8)

        self.file_btn = QPushButton(self.page_3)
        self.file_btn.setObjectName(u"file_btn")

        self.gridLayout_2.addWidget(self.file_btn, 1, 9, 1, 1)

        self.pause_btn = QPushButton(self.page_3)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pause_btn, 2, 2, 1, 1)

        self.start_btn = QPushButton(self.page_3)
        self.start_btn.setObjectName(u"start_btn")

        self.gridLayout_2.addWidget(self.start_btn, 3, 7, 1, 2)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_2.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        self.menuMENU = QMenu(self.menubar)
        self.menuMENU.setObjectName(u"menuMENU")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMENU.menuAction())
        self.menuMENU.addAction(self.actionZapisz_do_Excela)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.actionZapisz_do_Excela.setText(QCoreApplication.translate("MainWindow", u"Zapisz do Excela", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wynik rozpoznania:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"\u25a0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plik .mp3/.wav", None))
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"Wybierz", None))
        self.pause_btn.setText(QCoreApplication.translate("MainWindow", u"\u23f8\ufe0e", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.menuMENU.setTitle(QCoreApplication.translate("MainWindow", u"MENU", None))
    # retranslateUi

