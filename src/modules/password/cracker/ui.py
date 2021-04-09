from guizero import App, Box, PushButton, Slider, Text, TextBox

#
# GuiZero components
#

app = App(title="password cracker")

prompt = """
this is a multiline string.
i hope that it works in the UI
"""

promptLabel = Text(app, text=prompt)

app.display()