from PySide6.QtCore import QObject, Slot

from app.core.config import get_config
from app.core.requests import FGISArshinAPI
from app.core.signals import Signals


class DataLogic(QObject):
    def __init__(self, signals: Signals):
        super().__init__()
        self.signals = signals
        self.cfg = get_config()
        self.requests: FGISArshinAPI = FGISArshinAPI()
        self.signals.signal_connection(self.signals.signal_to_data_logic, self.data_event)
        print("Data Logic start")

    @Slot(dict)
    def data_event(self, data: dict) -> None:
        response = self.requests.send(data)
        if not response:
            self.signals.signal_to_interface.emit(
                {"data": "нет подключения или поменялся url api или api не доступно или изменился формат ответа api"}
            )
        elif not response["result"]["items"]:
            self.signals.signal_to_interface.emit({"data": "данные о поверке не найдены"})
        else:
            self.signals.signal_to_interface.emit({"data": response["result"]["items"].pop()})
