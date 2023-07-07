from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.icon_definitions import md_icons

from kivy.config import Config
from kivy.lang import Builder

kv = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        elevation: 4
                        pos_hint: {"top": 1}
                        md_bg_color: "#8bc34a"
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        md_bg_color: "#e9f9f5"
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        Tab:
                            title: "Tab 1"
                            content_text: f"This is an example text for {self.title}"



                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                MDScrollView:


                                    MDList:
                                        id: container


                        Tab:
                            title: "Tab 2"
                            content_text: f"This is an example text for {self.title}"


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"



<Tab>
    MDIconButton:
        id: icon
        icon: root.icon
        icon_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Example(MDApp):
    icons = list(md_icons.keys())[15:30]
    Config.set('graphics', 'width', '1200')
    Config.set('graphics', 'height', '1200')

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        return Builder.load_string(kv)
        # self.root = Builder.load_file('app_interface.kv')


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