# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_calc.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 550))
        MainWindow.setMaximumSize(QSize(400, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"QWidget { \n"
"color: white; \n"
"background-color: #121212; \n"
"font-family: Rubick; \n"
"font-size: 16pt; \n"
"font-weight: 600; \n"
"}\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #888;\n"
"}")
        self.lbl_ent = QLineEdit(self.centralwidget)
        self.lbl_ent.setObjectName(u"lbl_ent")
        self.lbl_ent.setGeometry(QRect(20, 80, 331, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_ent.sizePolicy().hasHeightForWidth())
        self.lbl_ent.setSizePolicy(sizePolicy2)
        self.lbl_ent.setStyleSheet(u"border: none;")
        self.lbl_ent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 130, 331, 391))
        self.layout_btns = QGridLayout(self.gridLayoutWidget)
        self.layout_btns.setObjectName(u"layout_btns")
        self.layout_btns.setContentsMargins(0, 0, 0, 0)
        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_5, 3, 1, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_4, 3, 0, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_6, 3, 2, 1, 1)

        self.btn_div = QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy3.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_div, 3, 3, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_is = QPushButton(self.gridLayoutWidget)
        self.btn_is.setObjectName(u"btn_is")
        sizePolicy3.setHeightForWidth(self.btn_is.sizePolicy().hasHeightForWidth())
        self.btn_is.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_is, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_mul = QPushButton(self.gridLayoutWidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy4)

        self.layout_btns.addWidget(self.btn_mul, 2, 3, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy3.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_3, 4, 2, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_2, 4, 1, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_1, 4, 0, 1, 1)

        self.btn_sub = QPushButton(self.gridLayoutWidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy3.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_sub, 4, 3, 1, 1)

        self.btn_add = QPushButton(self.gridLayoutWidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy3.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_add, 5, 3, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy3.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_0, 5, 1, 1, 1)

        self.btn_point = QPushButton(self.gridLayoutWidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy3.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_point, 5, 2, 1, 1)

        self.btn_abs = QPushButton(self.gridLayoutWidget)
        self.btn_abs.setObjectName(u"btn_abs")
        sizePolicy3.setHeightForWidth(self.btn_abs.sizePolicy().hasHeightForWidth())
        self.btn_abs.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_abs, 5, 0, 1, 1)

        self.btn_back = QPushButton(self.gridLayoutWidget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy3.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_back, 0, 2, 1, 1)

        self.btn_clr = QPushButton(self.gridLayoutWidget)
        self.btn_clr.setObjectName(u"btn_clr")
        sizePolicy3.setHeightForWidth(self.btn_clr.sizePolicy().hasHeightForWidth())
        self.btn_clr.setSizePolicy(sizePolicy3)

        self.layout_btns.addWidget(self.btn_clr, 0, 1, 1, 1)

        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setGeometry(QRect(10, 29, 341, 31))
        sizePolicy1.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy1)
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl_ent.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_is.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_abs.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.btn_clr.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.lbl_temp.setText(QCoreApplication.translate("MainWindow", u"640.58 * 10 =", None))
    # retranslateUi

