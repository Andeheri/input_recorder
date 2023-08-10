
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QMainWindow,  QLabel, QProgressBar

download_path = Path.home().joinpath('Downloads')

record_button_path = download_path.joinpath('button.png').__str__()
folder_button_path = download_path.joinpath('folder (1).png').__str__()
play_button_path = download_path.joinpath('play-button-arrowhead.png').__str__()
rounded_square_path = download_path.joinpath('rounded-square.png').__str__()

# Change variables
button_size = 80
icon_size = 40
window_width = 800
window_height = 400


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        self.recording = False
        self.playing = False

    def play_button_clicked(self):
        print("Play button clicked")
        self.playing = not self.playing
        if not self.playing:
            self.play_button.setIcon(QIcon(play_button_path))
        else:
            self.play_button.setIcon(QIcon(rounded_square_path))

    def record_button_clicked(self):
        print("Record button clicked")
        self.recording = not self.recording
        if not self.recording:
            self.record_button.setIcon(QIcon(record_button_path))
        else:
            self.record_button.setIcon(QIcon(rounded_square_path))


    def combo_selected(self):
        print("Combo Item selected: "+self.dd_menu.currentText())

    def browse_folder(self):
        chosen_dir = QFileDialog.getExistingDirectory(self, "Choose Directory")
        if chosen_dir:  # If a directory is chosen
            print("Chosen directory: ", chosen_dir)

    def initUI(self):
        screen = QApplication.desktop().screenGeometry()
        screen_width, screen_height = screen.width(), screen.height()
        self.setGeometry(int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2), window_width, window_height)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Mouse Logger")
        self.setStyleSheet("QWidget { background-color: #d6cec3 ;}")

        # Vertical line
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setGeometry(int(self.width() / 2), 0, 10, self.height())

        # Record side

        # Label
        self.label = QLabel(self)
        self.label.setText("Record")
        font = QFont("Arial", 20)  # Set font and size
        self.label.setFont(font)
        self.label.setStyleSheet("""QLabel {
                                        background-color: white;
                                        border-radius: 5px;
                                        border: 5px solid white;
                                    }""")
        self.label.adjustSize()
        self.label.move(int(window_width / 4 - self.label.size().width() / 2), 10)  # let QLabel take the full space of the window
        
        # Record button
        self.record_button = QtWidgets.QPushButton(self)
        self.record_button.setIcon(QIcon(record_button_path))
        self.record_button.setIconSize(QSize(icon_size, icon_size))
        self.record_button.clicked.connect(self.record_button_clicked)
        self.record_button.move(50, 90)
        self.record_button.setFixedSize(button_size, button_size)
        self.record_button.setStyleSheet("""QPushButton {  
                            border: 2px solid black; 
                            border-radius: 10px;
                        }
                        QPushButton:hover {  
                            background-color: beige; 
                        }""")
        
        # Text Field
        self.text_field = QtWidgets.QLineEdit(self)
        text_field_font = QFont('Arial', 16)
        self.text_field.setFont(text_field_font)
        self.text_field.move(150, int(85 + icon_size / 2))
        self.text_field.setFixedSize(230, 50)
        self.text_field.setPlaceholderText("Enter file name")

        # Directory button
        self.directory_button = QtWidgets.QPushButton(self)
        self.directory_button.setIcon(QIcon(folder_button_path))
        self.directory_button.setIconSize(QSize(icon_size, icon_size))
        self.directory_button.clicked.connect(self.browse_folder)
        self.directory_button.move(50,190)
        self.directory_button.setFixedSize(button_size, button_size)
        self.directory_button.setStyleSheet("""QPushButton {  
                            border: 2px solid black; 
                            border-radius: 10px;
                        }
                        QPushButton:hover {  
                            background-color: beige; 
                        }""")
        
        # Play side

        # Play button
        self.play_button = QtWidgets.QPushButton(self)
        self.play_button.setIcon(QIcon(play_button_path))
        self.play_button.setIconSize(QSize(icon_size, icon_size))
        self.play_button.clicked.connect(self.play_button_clicked)
        self.play_button.move(int(window_width / 2 + icon_size), 90)
        self.play_button.setFixedSize(button_size, button_size)
        self.play_button.setStyleSheet("""QPushButton {  
                            border: 2px solid black; 
                            border-radius: 10px;
                        }
                        QPushButton:hover {  
                            background-color: beige; 
                        }""")
        
        # Label
        self.label_2 = QLabel(self)
        self.label_2.setText("Play")
        font = QFont("Arial", 20)  # Set font and size
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("""QLabel {
                                        background-color: white;
                                        border-radius: 5px;
                                        border: 5px solid white;
                                    }""")
        self.label_2.adjustSize()
        self.label_2.move(int(window_width / 4 * 3 - self.label_2.size().width() / 2), 10)  # let QLabel take the full space of the window
        
        #Combo/DropDown Box
        self.dd_menu = QtWidgets.QComboBox(self)
        dd_font = QFont('Arial', 16)
        self.dd_menu.setFont(dd_font)
        self.dd_menu.addItem("1")
        self.dd_menu.addItem("2")
        self.dd_menu.move(int(window_width / 2 + 150), int(85 + icon_size / 2))
        self.dd_menu.setFixedSize(150, 50)
        self.dd_menu.activated[str].connect(self.combo_selected)

        # # In your initUI method
        # self.progress = QProgressBar(self)
        # self.progress.setGeometry(int(window_width / 2 + 50), 50, int(window_width / 2 - 100), 20)  # adjust position and size as needed

        # # To update the progress value
        # self.progress.setValue(50)  # sets the progress to 50%

def window():
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()

window()