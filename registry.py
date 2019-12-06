from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from kivy.core.window import Window

import DataBase

def hashing(string:str) -> str:
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(string.encode('utf-8'))
    dataHash = digest.finalize()
    return str(dataHash)

class Notification(Popup):
    pass


class Root(FloatLayout):
    firstName = ObjectProperty(None)
    secondName = ObjectProperty(None)
    password = ObjectProperty(None)
    post = ObjectProperty(None)
    popup = ObjectProperty(None)
    Window.size = (646, 375)
    
    def clean(self):
        self.firstName.text = ''
        self.secondName.text = ''
        self.password.text = ''
        self.post.text = ''

    def write(self, firstName:str, secondName:str, password:str, post:str) -> None:
        hashName = hashing(firstName + ' ' + secondName)
        hashPass = hashing(password)
        data = [hashName, hashPass, firstName, secondName, post]
        DataBase.writeToBase(data)
        non = Notification()
        non.open()
        Root.clean(self)
    
class RegistryApp(App):
    def build(self):
        self.title = 'Регистрация'

if __name__ == "__main__":
    RegistryApp().run()

