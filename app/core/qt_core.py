from datetime import datetime

from PySide6.QtCore import QThread, Slot
from PySide6.QtWidgets import QLineEdit, QMainWindow

from app.core.data_logic import DataLogic
from app.core.signals import Signals
from app.ui.BaseWindow import Ui_main_window


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.signals: Signals = Signals()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.data_logic_prepare()
        self.ui.check.clicked.connect(self.process_entered_data)
        self.signals.signal_connection(self.signals.signal_to_interface, self.data_event)

    def process_entered_data(self) -> None:
        date = self.ui.date.text()
        number = self.ui.number.text()
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            self.ui.date.setText("дата введена некорректно")
            return
        if len(number) < 1 or len(number) > 40:
            self.ui.number.setText("номер введен некорректно")
            return

        for child in self.ui.centralwidget.children():
            if isinstance(child, QLineEdit) and child.objectName() not in ("date", "number"):
                child.clear()
        self.signals.signal_to_data_logic.emit({"number": number, "date": date})

    def data_logic_prepare(self) -> None:
        self.data_thread = QThread()
        self.data_logic = DataLogic(signals=self.signals)
        self.data_logic.moveToThread(self.data_thread)
        self.data_thread.start()

    @Slot(dict)
    def data_event(self, data: dict) -> None:
        data = data["data"]
        if isinstance(data, str):
            self.ui.org_title.setText(data)
        else:
            self.ui.org_title.setText(data["org_title"])
            self.ui.valid_date.setText(data["valid_date"])
            self.ui.mit_title.setText(data["mit_title"])
            self.ui.mit_notation.setText(data["mit_notation"])
            self.ui.applicability.setText("не пригоден")
            if data["applicability"]:
                self.ui.applicability.setText("пригоден")

    def closeEvent(self, event) -> None:
        self.data_thread.quit()
        self.data_thread.wait()
        print("Data Logic deleted")
        super().closeEvent(event)
