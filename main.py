from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
from PyQt5 import uic
from UI import Ui_MainWindow
import sys
import random



class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btnReaction)

    def btnReaction(self):
        self.update()

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        if False:
            qp = QPainter()
        qp.setBrush(QColor(*[random.randrange(0,255) for i in range(3)]))
        w, h = self.geometry().getRect()[:2]
        r = random.randrange(10, 50)
        x, y = random.randrange(r, w - r - 20), random.randrange(r, h - r - 20)
        print(x,y)
        qp.drawEllipse(QPointF(x, y), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
