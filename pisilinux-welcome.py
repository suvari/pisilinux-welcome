from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale
from welcome import WelcomeUi, resource
import sys, os



def main():
    app = QApplication(sys.argv)

    locale = QLocale.system().name()
    translator = QTranslator(app)
    translator.load("/usr/share/welcome/languages/{}.qm".format(locale))
    app.installTranslator(translator)

    window = WelcomeUi()
    window.show()

    if os.environ["HOME"] == "live":
        window.setSystem("live")

    else:
        window.setSystem("installed")

    app.exec_()


if __name__ == "__main__":
    main()