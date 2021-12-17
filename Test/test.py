import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *

# from PySide.QtGui import *
# from PySide.QtCore import *

class frmMain(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.btStart = QPushButton('Start')
        self.btStop = QPushButton('Stop')
        self.counter = QSpinBox()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btStart)
        self.layout.addWidget(self.btStop)
        self.layout.addWidget(self.counter)
        self.setLayout(self.layout)
        self.btStart.clicked.connect(self.start_thread)
        self.btStop.clicked.connect(self.stop_thread)

    def stop_thread(self):
        self.th.stop()

    def loopfunction(self, x):
        self.counter.setValue(x)

    def start_thread(self):
        self.th = thread(2)
        #self.connect(self.th, SIGNAL('loop()'), lambda x=2: self.loopfunction(x), Qt.AutoConnection)
        self.th.loop.connect(self.loopfunction)
        self.th.setTerminationEnabled(True)
        self.th.start()

class thread(QThread):
    loop = pyqtSignal(object)

    def __init__(self, x):
        QThread.__init__(self)
        self.x = x

    def run(self):
        for i in range(100):
            self.x = i
            self.loop.emit(self.x)
            time.sleep(0.5)

    def stop(self):
        self.terminate()


app = QApplication(sys.argv)
win = frmMain()

win.show()
sys.exit(app.exec_())
