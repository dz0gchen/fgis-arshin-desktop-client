import sys

from PySide6.QtWidgets import QApplication

from app.core.qt_core import BaseWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    base = BaseWindow()
    base.show()
    sys.exit(app.exec())
