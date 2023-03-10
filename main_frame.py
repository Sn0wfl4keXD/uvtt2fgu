import sys
from PyQt5.QtWidgets import *
from GUI import GUI

class APP:
    """Class Containign the main App Object"""
    def __init__(self) -> None:
        self._app = QApplication(sys.argv)
        self._res = self._app.desktop().screenGeometry()
        self.proc = None

    # Getters:

    def get_app(self):
        return self._app
    
    def get_width(self):
        return self._res.width()
    
    def get_height(self):
        return self._res.height()
    

def main():

    APP_INST = APP()
    FRAME = GUI(APP_INST.get_width())
    sys.exit(APP_INST.get_app().exec_())

main()