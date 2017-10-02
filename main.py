
#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################
# KivyCalendar 
###########################################################

from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.popup import Popup
from kivy.app import App
from calendar_widget import *

class LoginScreen(GridLayout):

    pHint_x = NumericProperty(0.7)
    pHint_y = NumericProperty(0.7)
    pHint = ReferenceListProperty(pHint_x ,pHint_y)

    def __init__(self, touch_switch=False, *args, **kwargs):
        super(LoginScreen, self).__init__(*args, **kwargs)
        
        self.touch_switch = touch_switch
        self.cols = 2
        self.add_widget(Label(text='Select Date'))
        self.startdate = TextInput(multiline=False)
        self.add_widget(self.startdate)
        self.init_ui()
       
    def init_ui(self):
        self.startdate.text = today_date()
        # Calendar
        self.cal = CalendarWidget(as_popup=True, 
                                  touch_switch=self.touch_switch)
        # Popup
        self.popup = Popup(content=self.cal, on_dismiss=self.update_value, 
                           title="")
        self.cal.parent_popup = self.popup
        
        self.startdate.bind(focus=self.show_popup)
       
    def show_popup(self, isnt, val):
        """ 
        Open popup if textinput focused, 
        and regardless update the popup size_hint 
        """
        self.popup.size_hint=self.pHint        
        if val:
            # Automatically dismiss the keyboard 
            # that results from the textInput 
            Window.release_all_keyboards()
            self.popup.open()
        
    def update_value(self, inst):
        """ Update textinput value on popup close """
        self.startdate.text = "%s-%s-%s" % tuple(self.cal.active_date)
        self.focus = False

class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
