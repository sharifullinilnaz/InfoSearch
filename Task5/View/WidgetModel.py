from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt


class WidgetModel(object):

    def showWindow(self, Window):
        Window.resize(1920, 1080)
        self.setWindowTitle("Векторный поиск")

        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 579))
        self.centralwidget.setAutoFillBackground(True)
        p = self.centralwidget.palette()
        p.setColor(self.centralwidget.backgroundRole(), Qt.black)
        self.setPalette(p)


        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.query_text = QtWidgets.QLineEdit(self.centralwidget)
        self.query_text.setObjectName("query_text")
        self.query_text.setPlaceholderText(QtCore.QCoreApplication.translate("MainWindow", "Введите поисковый запрос"))
        self.verticalLayout.addWidget(self.query_text)

        self.items_list = QtWidgets.QListWidget(self.centralwidget)
        self.items_list.setObjectName("items_list")
        self.verticalLayout.addWidget(self.items_list)

    
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setObjectName("button_submit")
        self.button_submit.setGeometry(0, 0, 100, 50)
        self.verticalLayout.addWidget(self.button_submit)
        self.button_submit.setText(QtCore.QCoreApplication.translate("MainWindow", "Искать"))


        Window.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Window)





