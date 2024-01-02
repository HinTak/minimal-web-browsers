#!/usr/bin/env python

# Portions and Adaptations Copyright 2023 Hin-Tak Leung

# This was originally written by Julita Inca AFAIK, first posted in
# https://lleksah.wordpress.com/2017/07/31/writing-my-first-web-browser-in-python-with-gtk/

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')

from gi.repository import Gtk, WebKit2, GLib

HISTORY_FILE = "/home/" + GLib.get_user_name() + "/browser1_history.html"
HOME_PAGE = "https://gnome.org"

webview = WebKit2.WebView()
entry = Gtk.Entry()

def open_page(url):
    entry.set_text(url)
    webview.load_uri(url)

def open_history(button):
    open_page("file://" + HISTORY_FILE)

def on_load_changed(webview, event):
    url = webview.get_uri ()
    history_file = open(HISTORY_FILE, "a+")
    history_file.writelines("* <a href=\"" + url + "\">" + url + "</a><br>")
    history_file.close()

def on_enter(entry):
    url = entry.get_text()
    webview.load_uri(url)
    if (url == "about:history"):
        open_history(webview)
        return

    open_page(url)

def on_go_back(button):
    webview.go_back()

def on_go_forward(button):
    webview.go_forward()

import sys
if len(sys.argv) > 1:
    open_page(sys.argv[1])
else:
    open_page(HOME_PAGE)
webview.connect("load-changed", on_load_changed)

history_button = Gtk.Button()
history_button_image = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
history_button.add(history_button_image)
history_button.connect("clicked", open_history)

window = Gtk.Window()
window.set_title("GUADEC 2017")
window.connect("destroy", Gtk.main_quit)
window.set_default_size(1280,720)

headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)
window.set_titlebar(headerbar)
headerbar.pack_end(history_button)

#scrolled_window = Gtk.ScrolledWindow()

go_back_button = Gtk.Button()
go_back_arrow = Gtk.Image.new_from_icon_name("go-previous", Gtk.IconSize.SMALL_TOOLBAR)
go_back_button.add(go_back_arrow)
go_back_button.connect("clicked", on_go_back)

go_forward_button = Gtk.Button()
go_forward_arrow = Gtk.Image.new_from_icon_name("go-next", Gtk.IconSize.SMALL_TOOLBAR)
go_forward_button.add(go_forward_arrow)
go_forward_button.connect("clicked", on_go_forward)

headerbar.pack_start(go_back_button)
headerbar.pack_start(go_forward_button)

entry.connect("activate", on_enter)
headerbar.set_custom_title(entry)

#scrolled_window.add(webview)

window.add(webview)
window.show_all()

Gtk.main()
