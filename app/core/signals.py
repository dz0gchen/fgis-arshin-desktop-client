from typing import Any, Callable, ClassVar

from PySide6.QtCore import QObject, Qt, Signal, SignalInstance


class Signals(QObject):
    signal_to_data_logic: ClassVar[Signal] = Signal(dict)
    signal_to_interface: ClassVar[Signal] = Signal(dict)

    def signal_connection(
        self,
        input_signal: SignalInstance,
        event_handler: Callable[[dict[Any, Any]], Any],
    ) -> None:
        input_signal.connect(event_handler, type=Qt.ConnectionType.QueuedConnection)  # type: ignore
