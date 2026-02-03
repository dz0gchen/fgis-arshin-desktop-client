# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaseWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(848, 268)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")

        self.verticalLayout_2.addWidget(self.date)

        self.number = QLineEdit(self.centralwidget)
        self.number.setObjectName(u"number")

        self.verticalLayout_2.addWidget(self.number)

        self.check = QPushButton(self.centralwidget)
        self.check.setObjectName(u"check")

        self.verticalLayout_2.addWidget(self.check)

        self.org_title = QLineEdit(self.centralwidget)
        self.org_title.setObjectName(u"org_title")

        self.verticalLayout_2.addWidget(self.org_title)

        self.valid_date = QLineEdit(self.centralwidget)
        self.valid_date.setObjectName(u"valid_date")

        self.verticalLayout_2.addWidget(self.valid_date)

        self.mit_title = QLineEdit(self.centralwidget)
        self.mit_title.setObjectName(u"mit_title")

        self.verticalLayout_2.addWidget(self.mit_title)

        self.mit_notation = QLineEdit(self.centralwidget)
        self.mit_notation.setObjectName(u"mit_notation")

        self.verticalLayout_2.addWidget(self.mit_notation)

        self.applicability = QLineEdit(self.centralwidget)
        self.applicability.setObjectName(u"applicability")

        self.verticalLayout_2.addWidget(self.applicability)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"\u0424\u0413\u0418\u0421 \u0410\u0440\u0448\u0438\u043d (\u043a\u043b\u0438\u0435\u043d\u0442)", None))
        self.date.setText("")
        self.date.setPlaceholderText(QCoreApplication.translate("main_window", u"\u0434\u0430\u0442\u0430 \u043f\u043e\u0432\u0435\u0440\u043a\u0438 (\u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \u0433\u043e\u0434-\u043c\u0435\u0441\u044f\u0446-\u0447\u0438\u0441\u043b\u043e) *", None))
        self.number.setText("")
        self.number.setPlaceholderText(QCoreApplication.translate("main_window", u"\u0437\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440 \u0441\u0438 (\u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430) *", None))
        self.check.setText(QCoreApplication.translate("main_window", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.org_title.setPlaceholderText(QCoreApplication.translate("main_window", u"\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f-\u043f\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c", None))
        self.valid_date.setText("")
        self.valid_date.setPlaceholderText(QCoreApplication.translate("main_window", u"\u0441\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u0432\u0435\u0440\u043a\u0438 \u0434\u043e", None))
        self.mit_title.setPlaceholderText(QCoreApplication.translate("main_window", u"\u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0438", None))
        self.mit_notation.setPlaceholderText(QCoreApplication.translate("main_window", u"\u0442\u0438\u043f \u0441\u0438", None))
        self.applicability.setPlaceholderText(QCoreApplication.translate("main_window", u"\u043f\u0440\u0438\u0433\u043e\u0434\u043d\u043e\u0441\u0442\u044c", None))
    # retranslateUi

