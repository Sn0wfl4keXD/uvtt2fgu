from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import uvtt2fgu as uvt

import os.path
import sys
import pathlib


class handler(QWidget):
    def __init__(self, gui) -> None:
        super().__init__()

        self.file = None
        self.gui = gui
        self._draw_main(500, 500)
        self.output = None
        self.name = "None"
        self.max_image_filesize=89478485
        self.objects_are_terrain=True
        self.remove=False
        self.force=False
        self.jpg_optimize=True
        self.jpg_quality=75
        self.jpg_subsampling=2
        self.write_jpg=True
        self.write_png=True
        self.jpgpath=False
        self.pngpath=False 
        self.xmlpath=False
        self.portalwidth="25%"
        self.portallength="0px"

    def set_file(self, file):
        if os.path.isfile(file):
            self.file = file

    def get_file(self):
        return self.file
    

    
    def _draw_main(self, width, height):
        layout = QHBoxLayout()
        self._draw_button(layout)




        self.setLayout(layout)
    
    def convert(self):
        output = self.output
        if self.output == None:
            output = self.gui.output
        if self.gui.file != None:
            uvt.converter(self.gui.file, 
                        output,
                        self.name,
                        max_image_filesize=self.max_image_filesize,
                        objects_are_terrain=self.objects_are_terrain,
                        remove=self.remove,
                        force=self.force,
                        jpg_optimize=self.jpg_optimize,
                        jpg_quality=self.jpg_quality,
                        jpg_subsampling=self.jpg_subsampling,
                        write_jpg=self.write_jpg,
                        write_png=self.write_png,
                        jpgpath=self.jpgpath,
                        pngpath=self.pngpath,
                        xmlpath=self.xmlpath,
                        portalwidth=self.portalwidth,
                        portallength=self.portallength)
    

    def _draw_button(self, grid):
        """
        Draws Buttons
        :return:
        """
        QToolTip.setFont(QFont('Arial', 14))

        _calc_button = QPushButton('Convert')
        _calc_button.move(self.width() - 300, 0)
        _calc_button.setToolTip('Converts into Fantasy Groudn File')
        _calc_button.clicked.connect(self.convert)
        grid.addWidget(_calc_button)

        _exit_button = QPushButton('Exit')
        _exit_button.move(self.width() - 100, 0)
        _exit_button.setToolTip('Exit Programm')
        _exit_button.clicked.connect(QCoreApplication.instance().quit)
        grid.addWidget(_exit_button)