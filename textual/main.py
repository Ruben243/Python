from textual.app import App, ComposeResult
from textual.widgets import Button, Label,TextArea
 
class MyApp(App):
    CSS_PATH = "app.css"
 
    def compose(self) -> ComposeResult:
        self.close_button = Button("Cerrar", id="close")
        yield Label("Este es un tutorial de aplicación Texual", id="tutorial")
        yield self.close_button
 
    def on_mount(self) -> None:
        self.screen.styles.background = "blue"
        self.close_button.styles.background = "red"
 
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)
 
if __name__ == "__main__":
    app = MyApp()
    app.run()