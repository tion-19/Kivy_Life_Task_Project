from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.icon_definitions import md_icons

from kivy.config import Config
from kivy.lang import Builder

from kivy.properties import StringProperty, ListProperty

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Example(MDApp):
    icons = list(md_icons.keys())[15:30]
    Config.set('graphics', 'width', '1200')
    Config.set('graphics', 'height', '1200')

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.root = Builder.load_file('app_interface.kv')


    def on_start(self):
        for tab_name in self.icons:
            self.root.ids.tabs.add_widget(Tab(icon=tab_name))

        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

    def on_tab_switch(

        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):

        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        count_icon = instance_tab.icon  # get the tab icon
        print(f"Welcome to {count_icon}' tab'")



Example().run()