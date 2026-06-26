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
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

# PyQt5 buttons
from PyQt5.QtWidgets import QPushButton

# PyQt5 checkboxes
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import Qt

# PyQt5 radio buttons
from PyQt5.QtWidgets import QRadioButton, QButtonGroup

# PyQt5 LineEdit
from PyQt5.QtWidgets import QLineEdit, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setWindowIcon(QIcon("heqeu.jpg"))

        self.setGeometry(700, 300, 500, 500)

        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        # self.radio1 = QRadioButton("Visa", self)
        # self.radio2 = QRadioButton("Mastercard", self)
        # self.radio3 = QRadioButton("Gift Card", self)
        # self.radio4 = QRadioButton("In-Store", self)
        # self.radio5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)

        # self.checkbox = QCheckBox("Do you like food?", self)

        # self.button = QPushButton("Click me!", self)
        # self.label = QLabel("Hello", self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        
        self.line_edit.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.submit)

    
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")


    #     self.radio1.setGeometry(0, 0, 300, 50)
    #     self.radio2.setGeometry(0, 50, 300, 50)
    #     self.radio3.setGeometry(0, 100, 300, 50)
    #     self.radio4.setGeometry(0, 150, 300, 50)
    #     self.radio5.setGeometry(0, 200, 300, 50)
        

    #     self.setStyleSheet("QRadioButton{"
    #                        'font-size: 40px;'
    #                        'font-family: Arial;'
    #                        'padding: 10px'
    #                        "}")
        
    #     self.button_group1.addButton(self.radio1)
    #     self.button_group1.addButton(self.radio2)
    #     self.button_group1.addButton(self.radio3)

    #     self.button_group2.addButton(self.radio4)
    #     self.button_group2.addButton(self.radio5)

    #     self.radio1.toggled.connect(self.radio_button_changed)    
    #     self.radio2.toggled.connect(self.radio_button_changed)  
    #     self.radio3.toggled.connect(self.radio_button_changed)  
    #     self.radio4.toggled.connect(self.radio_button_changed)  
    #     self.radio5.toggled.connect(self.radio_button_changed)  

    # def radio_button_changed(self):
    #     radio_button = self.sender()
    #     if radio_button.isChecked():
    #         print(f"{radio_button.text()} is selected")

    #     self.checkbox.setGeometry(10, 0, 500, 100)
    #     self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Arial;")

    #     self.checkbox.setChecked(False)
    #     self.checkbox.stateChanged.connect(self.checkbox_changed)

    # def checkbox_changed(self, state):
    #     if state == Qt.Checked:
    #         print("You like food")
    #     else:
    #         print("You do not like food")

    #     self.button.setGeometry(150, 200, 200, 100)
    #     self.button.setStyleSheet("font-size: 30px;")
    #     self.button.clicked.connect(self.on_click)

    #     self.label.setGeometry(150, 300, 200, 100)
    #     self.label.setStyleSheet("font-size: 30px;")

    # def on_click(self):
    #     self.label.setText("Goodbye!")
        # self.button.setDisabled(True)
        

        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)

        # label1 = QLabel("1", self)
        # label2 = QLabel("2", self)
        # label3 = QLabel("3", self)
        # label4 = QLabel("4", self)
        # label5 = QLabel("5", self)

        # label1.setStyleSheet("background-color: red;")
        # label2.setStyleSheet("background-color: yellow;")
        # label3.setStyleSheet("background-color: green;")
        # label4.setStyleSheet("background-color: blue;")
        # label5.setStyleSheet("background-color: purple;")

        # grid = QGridLayout()

        # grid.addWidget(label1, 0, 0)
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3, 1, 0)
        # grid.addWidget(label4, 1, 1)
        # grid.addWidget(label5, 1, 2)

        # central_widget.setLayout(grid)

        # label = QLabel(self) # self refers to window **
        # label.setGeometry(0, 0, 250, 250)

        # pixmap = QPixmap("heqeu.jpg")
        # label.setPixmap(pixmap)

        # label.setScaledContents(True)

        # label.setGeometry((self.width() - label.width()) // 2, 
        #                   (self.height() - label.height()) // 2, 
        #                   label.width(), 
        #                   label.height())

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