# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(807, 642)
        MainWindow.setMinimumSize(QSize(807, 642))
        MainWindow.setMaximumSize(QSize(807, 642))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inverted_index_btn = QPushButton(self.centralwidget)
        self.inverted_index_btn.setObjectName(u"inverted_index_btn")
        self.inverted_index_btn.setGeometry(QRect(220, 290, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.inverted_index_btn.setFont(font1)
        self.positional_index_btn = QPushButton(self.centralwidget)
        self.positional_index_btn.setObjectName(u"positional_index_btn")
        self.positional_index_btn.setGeometry(QRect(430, 290, 141, 41))
        self.positional_index_btn.setFont(font1)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 180, 801, 81))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(22)
        self.title.setFont(font2)
        self.title.setTabletTracking(True)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.developer_info = QLabel(self.centralwidget)
        self.developer_info.setObjectName(u"developer_info")
        self.developer_info.setGeometry(QRect(10, 570, 781, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Light"])
        font3.setPointSize(9)
        self.developer_info.setFont(font3)
        self.developer_info.setLayoutDirection(Qt.LeftToRight)
        self.developer_info.setAutoFillBackground(True)
        self.developer_info.setTextFormat(Qt.RichText)
        self.developer_info.setScaledContents(True)
        self.developer_info.setAlignment(Qt.AlignCenter)
        self.developer_info.setWordWrap(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 380, 101, 51))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 430, 221, 71))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 430, 221, 71))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 807, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.inverted_index_btn, self.positional_index_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Boolean Retrieval ", None))
        self.inverted_index_btn.setText(QCoreApplication.translate("MainWindow", u"Inverted Index", None))
        self.positional_index_btn.setText(QCoreApplication.translate("MainWindow", u"Positional Index", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Select a Boolean Model", None))
#if QT_CONFIG(whatsthis)
        self.developer_info.setWhatsThis(QCoreApplication.translate("MainWindow", u"developer", None))
#endif // QT_CONFIG(whatsthis)
        self.developer_info.setText(QCoreApplication.translate("MainWindow", u"Developed by K213459 - Dinesh Dhanjee", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inverted Index Entries\n"
"Positional Index Entries\n"
"Database Loading Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"14021\n"
"413546\n"
"323s", None))
    # retranslateUi

