import sys
from custome_errors import *
sys.excepthook = my_excepthook
import winsound
import threading
import speech_recognition as sr
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.lang=qt.QLineEdit()
        self.lang.setAccessibleName(_("language code"))
        self.say=qt.QPushButton(_("say"))
        self.say.setDefault(True)
        self.say.clicked.connect(self.sayf1)
        self.re=qt.QTextEdit()
        self.re.setReadOnly(True)
        self.re.setAccessibleName(_("result"))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.lang)
        layout.addWidget(self.say)
        layout.addWidget(self.re)
        v=qt.QWidget()
        v.setLayout(layout)
        self.setCentralWidget(v)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def ress(self,audioData):
        recognizer = sr.Recognizer()
        a=""
        try:
            a= recognizer.recognize_google(audioData, language=self.lang.text())
        except sr.UnknownValueError:
            a="Sorry, could not understand audio."
        except sr.RequestError as e:
            a="Error with the API request: {0}".format(e)
        self.re.setText(a)
    def res1(self,audioData):
        t=threading.Thread(target=self.ress(audioData))
        t.start()
    def sayf(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.PlaySound("data/sounds/1.wav",1)
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Listen to the microphone input
        winsound.PlaySound("data/sounds/2.wav",1)
        self.res1(audio)
        self.re.setFocus()
    def sayf1(self):
        threading.Thread(target=self.sayf()).start()


App=qt.QApplication([])
w=main()
w.show()
App.exec()