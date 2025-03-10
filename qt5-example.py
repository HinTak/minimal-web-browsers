#!/usr/bin/env python3

# Portions and Adaptations Copyright 2023 Hin-Tak Leung

# Adapted from https://codeloop.org/python-how-to-make-browser-in-pyqt5-with-pyqtwebengine/

# visit https://duckduckgo.com/?q=what+is+my+user+agent to see what chrome version is embedded.

import sys
from PyQt5.Qt import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

if len(sys.argv) < 2:
    from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
    print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)

def callback_function(html):
    try:
        with open(sys.argv[2], "x") as f:
            f.write(html)
        # want to quit even if file-write fails from refusal to overwrite existing file.
    finally:
        app.quit()

def on_load_finished():
    web.page().toHtml(callback_function)

app = QApplication(sys.argv)

web = QWebEngineView()

url = "https://pixelambacht.nl/chromacheck/"
if len(sys.argv) > 1:
    url = sys.argv[1]
web.load(QUrl(url))

# Dump in headless mode if there is anything after the URL
if len(sys.argv) < 3:
    web.show()
else:
    web.loadFinished.connect(on_load_finished)

sys.exit(app.exec_())
