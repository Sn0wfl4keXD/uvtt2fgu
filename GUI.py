import sys
from PyQt5.QtWidgets import *
import os

import qt_handler as handler


class GUI(QMainWindow):
    def __init__(self, width) -> None:
        super().__init__()

        self._width = width // 3
        self._main_frame = handler.handler(self)
        self.setAcceptDrops(True)
        self._draw_main(700)
        self.file = None
        self.output = None

    def _draw_main(self, height):

        self.setGeometry(50, 50, self._width, height)
        self.setWindowTitle("Big Chad")
        self.setCentralWidget(self._main_frame)
        self.show()
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file = event.mimeData().urls()[0]
        self.file = file.path()[1:]
        self.output = os.path.dirname(os.path.realpath(self.file))
        
