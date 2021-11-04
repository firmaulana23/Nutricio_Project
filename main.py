from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

class StartingPage(Screen):
    def start(self):
        sm.current = "login"

class LoginPage(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.username.text, self.password.text):
            HomePage.current = self.username.text
            self.reset()
            sm.current = "home"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "signup"

    def reset(self):
        self.username.text = ""
        self.password.text = ""

class SignUpPage(Screen):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    dateofbirth = ObjectProperty(None)
    weight = ObjectProperty(None)
    tall = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.firstname.text != "" and self.lastname.text != "" and self.dateofbirth.text != "" and self.weight.text != "" and self.tall.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.firstname.text, self.lastname.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.firstname.text = ""
        self.lastname.text = ""
        self.date.text = ""
        self.weight.text = ""
        self.height.text = ""

class HomePage(Screen):
    pass

class ScanPage(Screen):
    pass

class ReportPage(Screen):
    pass

class CalculatorPage(Screen):
    pass

class SettingPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid username or password.'), size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'), size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("main.kv")
sm = WindowManager()
db = DataBase("users.txt")

screens = [StartingPage(name="starting"), LoginPage(name="login"), SignUpPage(name="signup")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "starting"

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()