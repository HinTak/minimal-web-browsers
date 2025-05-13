This repository is a collection of Minimal Web Browser implementations written in Python. It is an educational or experimental project aimed at showcasing the basics of building a web browser. This project is aimed at providing a lightweight demonstration or reference for constructing simple web browsers.

# Minimal Web Browser implementations

This is a collection of minimal web browser implementations. Each of them will
go to an URL if supplied as a first argument, or to a default URL (google, gnome, [Chroma Check](https://pixelambacht.nl/chromacheck/) respectively)
if run without arguments.

Point one of these script to [Chroma Check](https://pixelambacht.nl/chromacheck/) to see what
color fonts which implementation supports. Visit [Color Font Demo](https://yoksel.github.io/color-fonts-demo/)
for the same purpose.

The oldest (GtkSharp WebKit) is about a decade old, as part of the
[Font Validator](https://github.com/HinTak/Font-Validator) work. The python WebKitGTK example
was written in mid-2023 to replace that; the python QT examples were written to look at OT-SVG support
in [Chromium](https://github.com/HinTak/chromium-mod-CI) and [QT WebEngine](https://github.com/HinTak/Qt6WE-OT-SVG).


# Misc

There is a minimal example elsewhere:
https://github.com/qutebrowser/qutebrowser/blob/main/scripts/testbrowser/testbrowser_webengine.py
