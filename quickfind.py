# -*- coding: utf-8 -*-
import sys
import time
from PyQt4.QtGui import QMessageBox, QApplication, QDialog
from ui_quickfind import Ui_QuickFind
from data import Data

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class QuickFind(QDialog):
    def __init__(self, filename=None):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_QuickFind()
        self.ui.setupUi(self)

        self.data = Data()
        self.data.load(filename)

        # Connect up the buttons.
        self.ui.queryButton.clicked.connect(self.query)

    def query(self):

        keyword = self.ui.queryBox.toPlainText()
        keyword = unicode(keyword).encode("gb18030")

        if len(keyword) == 0:
            QMessageBox.about(self,
                    _translate("QuickFind", "出错了", None),
                    _translate("QuickFind", "查询不能为空", None))
            return

        cnt = 0
        html = "<strong>%s</strong><hr />" % keyword
        html += "<ul>"

        num = 0
        #for line, words in self.corpus:
        for sent, words in self.data:

            if keyword in sent:
                html += "<li>"
                i = 0

                for word, tag in words:
                    if keyword == word:
                        html += "<strong>%s</strong>(%s) " % (word, tag)
                    else:
                        html += "%s(%s) " % (word, tag)

                    i += 1
                html += "</li>"

                num += 1
                if num > 10:
                    break

        html += "</ul>"

        html = html.decode("gb18030").encode("utf8")
        self.ui.exampleBrowser.setText(_translate("QuickFind", html, None))
        self.ui.queryBox.clear()

    def load(self, filename):
        try:
            fp=open(filename, "r")
        except:
            print >> sys.stderr, "Failed to open file"
            exit(1)

        self.corpus = []
        for line in fp:
            words=[word.rsplit("_", 1) for word in line.strip().split()]
            sentence = "".join(word[0] for word in words)
            self.corpus.append((sentence, words))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QuickFind("corpus.db")
    w.show()
    sys.exit(app.exec_())
