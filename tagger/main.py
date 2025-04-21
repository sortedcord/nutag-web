import os
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable, Label, Button, TextArea
from textual.containers import Vertical, Horizontal, VerticalScroll, Container, Grid
from textual.screen import ModalScreen
from pathlib import Path
from textual.reactive import reactive

class File():
    def __init__(self, path:Path) -> None:
        self.path:Path = path



class File_list(DataTable):
    def __init__(self):
        super().__init__()

        self.add_columns(*("Track no.", "Title", "Artist", "Album", "Duration"))
    
    def push_file(self, file:File):
        self.add_row((file.path, "1", "q", "w", "w", "w"))

class FilePickerScreen(ModalScreen[str]):
    """Screen to choose file/dir"""
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Locate the file or folder"),
            TextArea(),
            Button("Enter", id="submit"),
            Button("Cancel", id="cancel")
        )
    
    def on_button_pressed(self, event:Button.Pressed) -> None:
        if event.button.id == "submit":
            text_area:TextArea = self.query_one(TextArea)
            self.dismiss(text_area.text)
        else:
            self.dismiss(False)

class MusicManagerApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("o", "add_files", "Add Files")]
    
    OPEN_FILES = []

    def open_files(self, file:File) -> None:
        """
        Called when OPEN_FILES changes
        """
        self.OPEN_FILES.append(file)
        self.query_one(File_list).push_file(file)


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Vertical(
            File_list()
        )
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_add_files(self) -> None:
        """
        An Action to add files to MMA
        """
        def get_path(path: str | None) -> None:
            if path:
                self.open_files(File(Path(path)))
        self.push_screen(FilePickerScreen(), get_path) 


if __name__ == "__main__":
    app = MusicManagerApp()
    app.run()