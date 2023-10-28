from aqt import mw, gui_hooks
from aqt.qt import qconnect, QMenu, QCursor, QLabel, QPushButton, QDialog
from aqt.utils import tr
from anki.decks import DeckId


class MyPopup(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Pop-Up")
        self.setGeometry(100, 100, 300, 200)  # Set the pop-up window dimensions

        label = QLabel("This is a pop-up window.", self)
        label.setGeometry(50, 50, 200, 30)

        button = QPushButton("Close", self)
        button.setGeometry(100, 100, 100, 30)
        button.clicked.connect(self.close)

        self.show()


def action():
    if mw is None:
        exit(1)
    dlg = MyPopup()
    dlg.exec()


# sourced from https://github.com/ankitects/anki/blob/9600f033f745bfae4e00dd9fa43e44d3b30c22d2/qt/aqt/deckbrowser.py#L289
def article_painter_showOptions(self, did: str) -> None:
    m = QMenu(self.mw)
    a = m.addAction(tr.actions_rename())
    qconnect(a.triggered, lambda b, did=did: self._rename(DeckId(int(did))))  # type: ignore
    a = m.addAction(tr.actions_options())
    qconnect(a.triggered, lambda b, did=did: self._options(DeckId(int(did))))  # type: ignore
    a = m.addAction(tr.actions_export())
    qconnect(a.triggered, lambda b, did=did: self._export(DeckId(int(did))))  # type: ignore
    a = m.addAction(tr.actions_delete())
    qconnect(a.triggered, lambda b, did=did: self._delete(DeckId(int(did))))  # type: ignore
    a = m.addAction('fifth option', action)
    qconnect(a.triggered, lambda b, did=did: print(f'b {b} {did}'))  # type: ignore
    gui_hooks.deck_browser_will_show_options_menu(m, int(did))
    m.popup(QCursor.pos())


def setup_addon():
    print('addon starting')
    if mw is None:
        exit(1)
    # override _showOptions function
    type(mw.deckBrowser)._showOptions = article_painter_showOptions


setup_addon()
