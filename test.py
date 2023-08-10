from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys
import time
import threading

class WorkerSignals(QObject):
    finished = pyqtSignal()

class Worker(QRunnable):
    def __init__(self, stop_event):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            # This is where your long running task goes
            time.sleep(1)
            print("Running")

        self.signals.finished.emit()

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.threadpool = QThreadPool()
        self.stop_event = threading.Event()

        self.button = QPushButton("Start/Stop long task", self)
        self.button.clicked.connect(self.start_stop_long_task)
        self.worker = None

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def start_stop_long_task(self):
        if self.worker is None:  # No task is running
            self.worker = Worker(self.stop_event)
            self.worker.signals.finished.connect(self.task_finished)
            self.threadpool.start(self.worker)
            self.button.setText("Stop long task")
        else:  # A task is running
            self.stop_event.set()

    def task_finished(self):
        print("Long task finished")
        self.button.setText("Start long task")
        self.worker = None
        self.stop_event.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyWindow()
    gui.show()
    sys.exit(app.exec_())