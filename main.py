import random

import kivy
from kivy.app import  App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
import qrcode
class Mygridlayout(GridLayout):
    def __init__(self,**kwargs):
        super(Mygridlayout,self).__init__(**kwargs)
        self.cols =1
        self.top_widget=GridLayout()
        self.add_widget(self.top_widget)
        self.top_widget.cols = 1
        self.a=self.top_widget.add_widget(Label(text='ENTER YOUR TEXT BELOW',font_size=35,bold=True,color=(1,0,0,1),italic=True))

        self.user=TextInput(multiline=True)
        self.top_widget.add_widget(self.user)
        self.btn=Button(text='SUBMIT',font_size=35,bold=True,background_normal='',background_color=(252 /255,132/255,3/255,1),color=(0,0,0,1),italic=True)
        self.btn.bind(on_press=self.press)
        self.add_widget(self.btn)
    def press(self,instance):
        users=self.user.text
        code=qrcode.make(users)
        self.qr=code.save('qr.jpg')



        self.add_widget(Image(source=random.choice(["qr.jpg"]), allow_stretch=True,keep_ratio=True))





class Myapp(App):
    def build(self):
        return Mygridlayout()
if __name__=='__main__':
    Myapp().run()
