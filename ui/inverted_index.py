# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inverted_index.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Inverted_index(object):
    def setupUi(self, Inverted_index):
        if not Inverted_index.objectName():
            Inverted_index.setObjectName(u"Inverted_index")
        Inverted_index.resize(777, 642)
        self.title = QLabel(Inverted_index)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(260, 70, 241, 81))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        self.title.setFont(font)
        self.query_heading = QLabel(Inverted_index)
        self.query_heading.setObjectName(u"query_heading")
        self.query_heading.setGeometry(QRect(180, 170, 61, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.query_heading.setFont(font1)
        self.user_query = QLineEdit(Inverted_index)
        self.user_query.setObjectName(u"user_query")
        self.user_query.setGeometry(QRect(260, 170, 381, 41))
        self.query_help_text = QLabel(Inverted_index)
        self.query_help_text.setObjectName(u"query_help_text")
        self.query_help_text.setGeometry(QRect(180, 230, 461, 81))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(9)
        self.query_help_text.setFont(font2)
        self.search_btn = QPushButton(Inverted_index)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(340, 330, 141, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.search_btn.setFont(font3)
        self.output_box = QTextBrowser(Inverted_index)
        self.output_box.setObjectName(u"output_box")
        self.output_box.setGeometry(QRect(270, 410, 371, 121))
        self.output_heading = QLabel(Inverted_index)
        self.output_heading.setObjectName(u"output_heading")
        self.output_heading.setGeometry(QRect(180, 400, 71, 41))
        self.output_heading.setFont(font1)
        self.back_btn = QPushButton(Inverted_index)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 93, 28))
        self.developer_info = QLabel(Inverted_index)
        self.developer_info.setObjectName(u"developer_info")
        self.developer_info.setGeometry(QRect(70, 590, 621, 31))
        self.developer_info.setFont(font2)
        self.developer_info.setLayoutDirection(Qt.LeftToRight)
        self.developer_info.setAutoFillBackground(True)
        self.developer_info.setTextFormat(Qt.RichText)
        self.developer_info.setScaledContents(True)
        self.developer_info.setAlignment(Qt.AlignCenter)
        self.developer_info.setWordWrap(True)
        self.label = QLabel(Inverted_index)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 560, 171, 21))
        font4 = QFont()
        font4.setPointSize(9)
        self.label.setFont(font4)
        self.query_processing_time = QLabel(Inverted_index)
        self.query_processing_time.setObjectName(u"query_processing_time")
        self.query_processing_time.setGeometry(QRect(370, 560, 271, 21))
        self.query_processing_time.setFont(font4)
        self.search_btn.raise_()
        self.title.raise_()
        self.query_heading.raise_()
        self.user_query.raise_()
        self.query_help_text.raise_()
        self.output_box.raise_()
        self.output_heading.raise_()
        self.back_btn.raise_()
        self.developer_info.raise_()
        self.label.raise_()
        self.query_processing_time.raise_()

        self.retranslateUi(Inverted_index)
        self.back_btn.clicked.connect(Inverted_index.close)

        QMetaObject.connectSlotsByName(Inverted_index)
    # setupUi

    def retranslateUi(self, Inverted_index):
        Inverted_index.setWindowTitle(QCoreApplication.translate("Inverted_index", u"Inverted Index", None))
        self.title.setText(QCoreApplication.translate("Inverted_index", u"Inverted Index", None))
        self.query_heading.setText(QCoreApplication.translate("Inverted_index", u"Query", None))
        self.query_help_text.setText(QCoreApplication.translate("Inverted_index", u"Query format: \n"
"NOT W1 AND W2 OR NOT W3\n"
"W1 OR NOT W2 OR NOT W3\n"
"W1 AND NOT W2", None))
        self.search_btn.setText(QCoreApplication.translate("Inverted_index", u"Search", None))
        self.output_heading.setText(QCoreApplication.translate("Inverted_index", u"Output", None))
        self.back_btn.setText(QCoreApplication.translate("Inverted_index", u"Back", None))
#if QT_CONFIG(whatsthis)
        self.developer_info.setWhatsThis(QCoreApplication.translate("Inverted_index", u"developer", None))
#endif // QT_CONFIG(whatsthis)
        self.developer_info.setText(QCoreApplication.translate("Inverted_index", u"Developed by K213459 - Dinesh Dhanjee", None))
        self.label.setText(QCoreApplication.translate("Inverted_index", u"Query Processing Time:", None))
        self.query_processing_time.setText(QCoreApplication.translate("Inverted_index", u"~", None))
    # retranslateUi

