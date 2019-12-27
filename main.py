from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
from PyQt5 import uic
import sys
import random


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.btnReaction)

    def btnReaction(self):
        self.start_draw = 1
        self.update()

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        if False:
            qp = QPainter()
        qp.setBrush(QColor(255, 255, 0))
        w, h = self.geometry().getRect()[:2]
        r = 10
        x, y = random.randrange(r, w - r), random.randrange(r, h - r)
        qp.drawEllipse(QPointF(x, y), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
