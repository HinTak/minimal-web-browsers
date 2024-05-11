#!/usr/bin/env python3

# Portions and Adaptations Copyright 2023 Hin-Tak Leung

# Adapted from the accompanying qt5-example.py

# Visiting url 'chrome://qt' (since 6.6) gives all the versions.

import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QStyleFactory

from PyQt6.QtWebEngineCore import qWebEngineVersion, qWebEngineChromiumVersion, \
qWebEngineChromiumSecurityPatchVersion

#qWebEngineVersion() and qWebEngineChromiumVersion() requires 6.2
# qWebEngineChromiumSecurityPatchVersion() requires 6.3
if len(sys.argv) < 2:
    print("WE: ", qWebEngineVersion(), "\tChrome based: ", qWebEngineChromiumVersion(),
          "\tChrome patched: ", qWebEngineChromiumSecurityPatchVersion())

    from PyQt6.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
    print("Qt: ", QT_VERSION_STR, "\tPyQt: ", PYQT_VERSION_STR)
    print(QStyleFactory.keys())

app = QApplication(sys.argv)

# In QT 6.5 onwards,
app.setStyle('Fusion')

web = QWebEngineView()

url = "https://pixelambacht.nl/chromacheck/"
if len(sys.argv) > 1:
    url = sys.argv[1]
web.load(QUrl(url))

web.show()

sys.exit(app.exec())
