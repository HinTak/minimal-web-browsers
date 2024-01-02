#!/usr/bin/env python

# Portions and Adaptations Copyright 2023 Hin-Tak Leung

# Adapted from the accompanying qt5-example.py

import sys
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView

if len(sys.argv) < 2:
    from PyQt4.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
    print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)

app = QApplication(sys.argv)

web = QWebView()
url = "https://pixelambacht.nl/chromacheck/"
if len(sys.argv) > 1:
    url = sys.argv[1]
web.load(QUrl(url))
web.show()

sys.exit(app.exec_())
