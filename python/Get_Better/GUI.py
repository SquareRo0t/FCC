# PyQt5 introduction
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# PyQt5 QLabels
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# PyQt5 images
from PyQt5.QtGui import QPixmap

# PyQt5 layouts

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("heqeu.jpg"))

        label = QLabel(self) # self refers to window **
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("heqeu.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2, 
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())

        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 40))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: blue;" 
        #                     "background-color: gray;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignRight) # Horizontally right
        # label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        # label.setAlignment(Qt.AlignLeft) # Horizontally left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        # label.setAlignment(Qt.AlignCenter) # Center & Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow() # <- This one **
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()