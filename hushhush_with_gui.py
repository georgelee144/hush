from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QTextEdit,QHBoxLayout,QPushButton,QVBoxLayout,QFileDialog
import sys
import hushhush
from atomicwrites import atomic_write
import os

class MainWindow(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("HushHush")
                self.resize(800,600)

                self.read_filepath_label = QLabel(self)
                self.read_filepath_label.setText('Read File path:')
                self.read_filepath = QFileDialog()

                self.write_filepath_label = QLabel(self)
                self.write_filepath_label.setText('Write File path:')
                self.write_filepath = QLineEdit()

                self.passphrase_label = QLabel(self)
                self.passphrase_label.setText('Passphrase:')
                self.passphrase = QLineEdit()
                self.passphrase.setEchoMode(QLineEdit.Password)

                self.read_button = QPushButton("Read file")
                self.write_button = QPushButton("Write file")

                self.textEdit = QTextEdit()

                main_layout = QVBoxLayout()
                first_row_layout = QHBoxLayout()
                second_row_layout = QHBoxLayout()
                third_row_layout = QHBoxLayout()

                first_row_layout.addWidget(self.read_filepath_label)
                first_row_layout.addWidget(self.read_filepath)

                main_layout.addLayout(first_row_layout)

                second_row_layout.addWidget(self.write_filepath_label)
                second_row_layout.addWidget(self.write_filepath)
                main_layout.addLayout(second_row_layout)

                third_row_layout.addWidget(self.passphrase_label)
                third_row_layout.addWidget(self.passphrase)
                third_row_layout.addWidget(self.read_button)
                third_row_layout.addWidget(self.write_button)

                main_layout.addLayout(third_row_layout)

                main_layout.addWidget(self.textEdit)

                self.setLayout(main_layout)

                self.read_button.clicked.connect(self.read_button_Clicked)
                self.write_button.clicked.connect(self.write_button_Clicked)

        def read_button_Clicked(self):
            """
            when clicked, the button will clear the passphrase try and read the file. 
            If the passphrase is wrong then the app will crash ... will fix it

            If the passphrase is correct then the textfile will be decoded and displayed on the screen
            The write to file field will be filled with the file path that was read
            """

            self.key = hushhush.make_key(self.passphrase.text())
            self.passphrase.setText("")
            print(self.passphrase.text())
            self.chiper_coder = hushhush.Fernet(self.key)

            self.file_selected = self.read_filepath.selectedFiles()[0]
            self.write_filepath.setText(self.file_selected)

            with open(self.file_selected,'r') as f:
                lines = f.readlines()
            
            decoded_text_to_display = ""

            for line in lines:
                decoded_text_to_display += f"{hushhush.decode_message(line,self.chiper_coder)}\n"

            self.textEdit.setText(f"{decoded_text_to_display}")
            del decoded_text_to_display

        def write_button_Clicked(self):
            """
            When clicked, whatever is in the text field will be encrypted and sent to a file
            To decrypt it you will need to remember the passphrase
            If the file doesn't exist then one will be created
            If the file is opened it may not be written to and crash ... will fix it
            """

            text_to_be_hashed = self.textEdit.toPlainText()

            lines_of_text = text_to_be_hashed.split("\n")
            del text_to_be_hashed
            self.textEdit.setText("")

            write_filepath = os.path.realpath(self.write_filepath.text())

            self.key = hushhush.make_key(self.passphrase.text())
            self.passphrase.setText("")

            self.chiper_coder = hushhush.Fernet(self.key)

            with atomic_write(write_filepath, overwrite=True) as writer:  

                for line in lines_of_text:
                    writer.write(f'{hushhush.encode_message(line,self.chiper_coder)}\n')
    
                del lines_of_text


if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())