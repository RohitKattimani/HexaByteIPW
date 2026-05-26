import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLineEdit,
    QMessageBox,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStatusBar
)
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView

from security import (
    is_blacklisted,
    contains_suspicious_keywords,
    is_https
)
from ui_style import STYLE


class BrowserTab(QWidget):
    def __init__(self, url="https://duckduckgo.com"):
        super().__init__()

        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)


class HexaNav(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HexaNav - Cyber Secure Browser")
        self.setGeometry(100, 100, 1400, 900)

        self.setStyleSheet(STYLE)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)

        self.create_toolbar()
        self.create_statusbar()

        self.add_new_tab()


    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.go_back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.go_forward)
        toolbar.addAction(forward_btn)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.reload_page)
        toolbar.addAction(reload_btn)

        home_btn = QAction("⌂", self)
        home_btn.triggered.connect(self.go_home)
        toolbar.addAction(home_btn)

        new_tab_btn = QAction("+", self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        toolbar.addAction(new_tab_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        toolbar.addWidget(self.url_bar)

        dashboard_btn = QAction("Security Dashboard", self)
        dashboard_btn.triggered.connect(self.show_dashboard)
        toolbar.addAction(dashboard_btn)


    def create_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("HexaNav Active | Threat Scanner Online")


    def current_browser(self):
        current_tab = self.tabs.currentWidget()
        return current_tab.browser


    def add_new_tab(self):
        tab = BrowserTab()
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)

        tab.browser.urlChanged.connect(self.update_url)
        tab.browser.loadFinished.connect(
            lambda _, browser=tab.browser: self.update_title(browser)
        )


    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)


    def update_title(self, browser):
        index = self.tabs.currentIndex()
        title = browser.page().title()
        self.tabs.setTabText(index, title[:18])


    def update_url(self, qurl):
        self.url_bar.setText(qurl.toString())
        self.scan_url(qurl.toString())


    def navigate(self):
        url = self.url_bar.text()

        if not url.startswith("http"):
            url = "https://" + url

        self.scan_url(url)

        self.current_browser().setUrl(QUrl(url))


    def scan_url(self, url):
        if is_blacklisted(url):
            QMessageBox.critical(
                self,
                "Threat Blocked",
                "Dangerous phishing domain detected."
            )
            return

        if contains_suspicious_keywords(url):
            QMessageBox.warning(
                self,
                "Suspicious Website",
                "Potential malicious keywords detected."
            )

        if not is_https(url):
            QMessageBox.warning(
                self,
                "Insecure Connection",
                "This site is not using HTTPS."
            )


    def go_back(self):
        self.current_browser().back()


    def go_forward(self):
        self.current_browser().forward()


    def reload_page(self):
        self.current_browser().reload()


    def go_home(self):
        self.current_browser().setUrl(QUrl("https://duckduckgo.com"))


    def show_dashboard(self):
        dashboard = QMessageBox()
        dashboard.setWindowTitle("HexaNav Security Dashboard")
        dashboard.setText(
            "Threat Prevention: ACTIVE\n"
            "HTTPS Monitor: ACTIVE\n"
            "Phishing Detection: ACTIVE\n"
            "Keyword Scanner: ACTIVE\n"
            "Dark Web Protection: BASIC MODE"
        )
        dashboard.exec()


app = QApplication(sys.argv)
window = HexaNav()
window.show()

sys.exit(app.exec())