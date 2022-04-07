import sys

from PyQt5.QtWidgets import QApplication


from Task5.Service.WidgetService import WidgetService

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetService()
    ex.show()
    sys.exit(app.exec_())
