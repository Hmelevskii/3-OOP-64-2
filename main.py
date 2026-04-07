import flet as ft
from datetime import datetime
def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    greeting_history = []

    history_text = ft.Text(value='История приветствий: ')


    text_hello.value = 'Hello Geeks'
    # text_hello = 'Hello world'


    def on_button_click(_):
        print(name_input.value)
        name = name_input.value

        if name:
            text_hello.color = None
            now = datetime.now().replace(microsecond=0)
            text = f'{now} - Привет, {name}'
            text_hello.value = text
            # text_hello.value = "Hello " + name 

            name_input.value = None

            greeting_history.append(text)
            # print(greeting_history)

            history_text.value = "История приветствий\n" + '\n'.join(greeting_history)
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
            print('Ничего не ввели')

    def switch_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    elavated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED, 
                                        icon_color=ft.Colors.GREEN, on_click=on_button_click)
    

    switch_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=switch_theme) 

    main_object = ft.Row([name_input, elavated_button, switch_button])

    page.add(text_hello, main_object, history_text)


ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)