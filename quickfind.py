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

    def _snt_template(self, keyword, sent, words):
        html = "<li>"
        
        ukey = keyword.decode("utf8")
        usent = sent.decode("utf8")
        
        a = usent.find(ukey)
        b = a + len(ukey)
        
        # color [a, b)
        i = 0
        
        for word, tag in words:
            
            uword = word.decode("utf8")
            j = i + len(uword)

            wordstr = ""
            
            if a <= i and b >= j:
                wordstr = "<span style=\"background-color:#ccc\">%s</span>" % word
            elif a <= i and b > i and b < j:
                word1 = usent[i: b].encode("utf8")
                word2 = usent[b: j].encode("utf8")
                wordstr = "<span style=\"background-color:#ccc\">%s</span>%s" % (word1, word2)
            elif a > i and a < j and b >= j:
                word1 = usent[i: a].encode("utf8")
                word2 = usent[a: j].encode("utf8")
                wordstr = "%s<span style=\"background-color:#ccc\">%s</span>" % (word1, word2)
            elif a > i and b < j:
                word1 = usent[i: a].encode("utf8")
                word2 = usent[a: b].encode("utf8")
                word3 = usent[b: j].encode("utf8")
                wordstr = "%s<span style=\"background-color:#ccc\">%s</span>%s" % (word1, word2, word3)
            else:
                wordstr = word
            
            if keyword == word:
                html += "<strong>%s</strong>(%s) " % (wordstr, tag)
            else:
                html += "%s(%s) " % (wordstr, tag)

            i = j
            
        html += "</li>"
        return html
        
    def _tag_template(self, keytag, tags):
        return "词性查询还在开发中"

    def query(self):

        keyword = self.ui.queryBox.toPlainText()
        keyword = unicode(keyword).encode("utf8").strip()
        
        html = ""
        # if input is a tag, retrieve the tag examples
        if keyword in self.data.tags:
        
            html = self._tag_template(keyword, self.data.tags)
            
        # else the input is a sentence segmentation
        else:
            if len(keyword) == 0 or len(keyword.split()) > 1:
                QMessageBox.about(self,
                        _translate("QuickFind", "出错了", None),
                        _translate("QuickFind", "查询不能为空，也不能有空格哦", None))
                return

            cnt = 0
            html = "<strong>%s</strong><hr />" % keyword
            html += "<ul>"

            num = 0
            #for line, words in self.corpus:
            for sent, words in self.data:

                if keyword in sent:

                    html += self._snt_template(keyword, sent, words)
                    num += 1
                
                if num > 30:
                    break

            html += "</ul>"

        self.ui.exampleBrowser.setText(_translate("QuickFind", html, None))
        self.ui.queryBox.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QuickFind("corpus.db")
    w.show()
    sys.exit(app.exec_())
