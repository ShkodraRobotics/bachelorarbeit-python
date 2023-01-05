import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        button = QPushButton("Klick mich!", self)
        button.clicked.connect(self.on_button_click)
        button.resize(button.sizeHint())
        button.move(50, 50)

    def on_button_click(self):
        print("Button geklickt!")


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
