from guizero import App, Text, PushButton

app = App(title='guizero test')
intro = Text(app, text='this is the text box for testing GUIZero')
ok = PushButton(app, text='ok')

app.display()