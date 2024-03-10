# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'positional_index.ui'
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

class Ui_PositionalIndex(object):
    def setupUi(self, PositionalIndex):
        if not PositionalIndex.objectName():
            PositionalIndex.setObjectName(u"PositionalIndex")
        PositionalIndex.resize(777, 642)
        self.back_btn = QPushButton(PositionalIndex)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 93, 28))
        self.title = QLabel(PositionalIndex)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 60, 771, 81))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.search_btn = QPushButton(PositionalIndex)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(340, 340, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.search_btn.setFont(font1)
        self.developer_info = QLabel(PositionalIndex)
        self.developer_info.setObjectName(u"developer_info")
        self.developer_info.setGeometry(QRect(70, 590, 621, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(9)
        self.developer_info.setFont(font2)
        self.developer_info.setLayoutDirection(Qt.LeftToRight)
        self.developer_info.setAutoFillBackground(True)
        self.developer_info.setTextFormat(Qt.RichText)
        self.developer_info.setScaledContents(True)
        self.developer_info.setAlignment(Qt.AlignCenter)
        self.developer_info.setWordWrap(True)
        self.user_query = QLineEdit(PositionalIndex)
        self.user_query.setObjectName(u"user_query")
        self.user_query.setGeometry(QRect(260, 160, 381, 41))
        self.output_heading = QLabel(PositionalIndex)
        self.output_heading.setObjectName(u"output_heading")
        self.output_heading.setGeometry(QRect(180, 410, 71, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.output_heading.setFont(font3)
        self.query_heading = QLabel(PositionalIndex)
        self.query_heading.setObjectName(u"query_heading")
        self.query_heading.setGeometry(QRect(180, 160, 61, 41))
        self.query_heading.setFont(font3)
        self.query_help_text = QLabel(PositionalIndex)
        self.query_help_text.setObjectName(u"query_help_text")
        self.query_help_text.setGeometry(QRect(180, 220, 461, 101))
        self.query_help_text.setFont(font2)
        self.output_box = QTextBrowser(PositionalIndex)
        self.output_box.setObjectName(u"output_box")
        self.output_box.setGeometry(QRect(270, 420, 371, 121))
        self.label = QLabel(PositionalIndex)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 560, 171, 21))
        font4 = QFont()
        font4.setPointSize(9)
        self.label.setFont(font4)
        self.query_processing_time = QLabel(PositionalIndex)
        self.query_processing_time.setObjectName(u"query_processing_time")
        self.query_processing_time.setGeometry(QRect(360, 560, 271, 21))
        self.query_processing_time.setFont(font1)

        self.retranslateUi(PositionalIndex)

        QMetaObject.connectSlotsByName(PositionalIndex)
    # setupUi

    def retranslateUi(self, PositionalIndex):
        PositionalIndex.setWindowTitle(QCoreApplication.translate("PositionalIndex", u"Positional Index", None))
        self.back_btn.setText(QCoreApplication.translate("PositionalIndex", u"Back", None))
        self.title.setText(QCoreApplication.translate("PositionalIndex", u"Positional Index", None))
        self.search_btn.setText(QCoreApplication.translate("PositionalIndex", u"Search", None))
#if QT_CONFIG(whatsthis)
        self.developer_info.setWhatsThis(QCoreApplication.translate("PositionalIndex", u"developer", None))
#endif // QT_CONFIG(whatsthis)
        self.developer_info.setText(QCoreApplication.translate("PositionalIndex", u"Developed by K213459 - Dinesh Dhanjee", None))
        self.output_heading.setText(QCoreApplication.translate("PositionalIndex", u"Output", None))
        self.query_heading.setText(QCoreApplication.translate("PositionalIndex", u"Query", None))
        self.query_help_text.setText(QCoreApplication.translate("PositionalIndex", u"Query format: \n"
"W1 W2 / k\n"
"where\n"
"       k is a positive number less than 10\n"
"       Kindly remove any extra space.", None))
        self.label.setText(QCoreApplication.translate("PositionalIndex", u"Query Processing Time:", None))
        self.query_processing_time.setText(QCoreApplication.translate("PositionalIndex", u"~", None))
    # retranslateUi

