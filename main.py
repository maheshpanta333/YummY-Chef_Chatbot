from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
import bot
from datasets import training_data, training_data_more
import os

class MessageBubble(BoxLayout):
    def __init__(self, text, align='left', bgcolor=(0.9, 0.9, 0.9, 1), **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=50, padding=(10, 10))
        self.spacing = 10
        label = Label(
            text=text,
            size_hint_x=1,
            halign=align,
            valign='middle',
            color=(0, 0, 0, 1),
            font_size=16,
            text_size=(900, None)  # Limit width for long texts
        )
        label.bind(size=label.setter('text_size'))
        with label.canvas.before:
            Color(*bgcolor)
            self.rect = RoundedRectangle(radius=[15], pos=label.pos, size=label.size)
        label.bind(pos=self.update_rect, size=self.update_rect)
        self.add_widget(label)
        if align == 'right':
            self.padding = (200, 10, 10, 10)
        else:
            self.padding = (10, 10, 200, 10)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [40, 20, 40, 20]  # left, top, right, bottom
        self.spacing = 10

        # Title section at top center with good size
        title_label = Label(
            text="YummY",
            font_size=32,
            size_hint_y=None,
            height=60,
            halign='center',
            valign='middle',
            color=(0.2, 0.5, 0.8, 1)
        )
        title_label.bind(size=title_label.setter('text_size'))
        self.add_widget(title_label)

        # Scrollable chat area
        self.chat_scroll = ScrollView(size_hint=(1, 1), bar_width=8)
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=12, padding=(0, 10))
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        self.chat_scroll.add_widget(self.chat_box)
        self.add_widget(self.chat_scroll)

        # Prompt input and send button
        input_layout = BoxLayout(size_hint_y=None, height=60, spacing=10, padding=(0, 10))
        self.prompt = TextInput(multiline=True, hint_text="Enter your prompt here...", size_hint_x=0.8, font_size=16)
        self.send = Button(text="Send", font_size=18, size_hint_x=0.2, background_color=(0.2, 0.5, 0.8, 1), color=(1,1,1,1))
        self.send.bind(on_press=self.pressed)
        input_layout.add_widget(self.prompt)
        input_layout.add_widget(self.send)
        self.add_widget(input_layout)

    def pressed(self, instance):
        prompt = self.prompt.text.strip()
        if prompt:
            # User message bubble (right aligned, blue background)
            user_bubble = MessageBubble(
                text=f"You: {prompt}",
                align='right',
                bgcolor=(0.7, 0.85, 1, 1)
            )
            self.chat_box.add_widget(user_bubble)

            # Bot response bubble (left aligned, light gray background)
            bot_response = self.get_bot_response(prompt)
            bot_bubble = MessageBubble(
                text=f"Chef: {bot_response}",
                align='left',
                bgcolor=(0.95, 0.95, 0.95, 1)
            )
            self.chat_box.add_widget(bot_bubble)

            self.chat_box.height = max(self.chat_box.height, self.chat_scroll.height)
            self.chat_scroll.scroll_y = 0
            self.prompt.text = ""

    def get_bot_response(self, prompt):
        response = bot.bot_response(chef, prompt)
        return str(response)


    def add_message_to_chat(self, text, align, bgcolor):
        bubble = MessageBubble(text=text, align=align, bgcolor=bgcolor)
        self.chat_box.add_widget(bubble)
        return bubble

class YummY(App):
    def build(self):
        return MyGrid()



DB_path="db.sqlite3"
chef = bot.create_bot("Chef")


def train():
    if not os.path.exists(DB_path):
        bot.train_bot(chef)
        bot.custom_train(chef, training_data)
        bot.custom_train(chef, training_data_more)

train()

if __name__ == "__main__":
    YummY().run()