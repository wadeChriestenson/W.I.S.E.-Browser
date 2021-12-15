# Packages needed to run script
import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Create the class for the main application
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Creating Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        backBtn = QAction('Back', self)
        backBtn.triggered.connect(self.browser.back)
        navbar.addAction(backBtn)

        # Forward button
        forwardBtn = QAction('Forward', self)
        forwardBtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardBtn)

        # Refresh button
        refresh = QAction('Refresh', self)
        refresh.triggered.connect(self.browser.reload)
        navbar.addAction(refresh)

        # Home button
        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.navigate_home)
        navbar.addAction(homeBtn)

        # Url search bar
        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlBar)
        self.browser.urlChanged.connect(self.update_url)

    # Function for Home button action
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    # Function for URL search bar action
    def navigate_to_url(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    # Function for Refresh button
    def update_url(self, q):
        self.urlBar.setText(q.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('W.I.S.E. Browser')
window = MainWindow()
app.exec_()
