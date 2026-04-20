import flet as ft
from datetime import datetime
import random

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    greeting_history = []
    names = []
    random_names = ["Алексей", "Мария", "Иван", "Ольга"]
    history_text = ft.Text(value='История приветствий: ')
    names_text = ft.Text(value='Любимые имена: ')
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
            greeting_history[:] = greeting_history[-5:]


            # print(greeting_history)

            history_text.value = "История приветствий\n" + '\n'.join(greeting_history)
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
            print('Ничего не ввели')
    
    def add_favorit_names(_):
        if greeting_history:
            favorit_name = greeting_history[-1]
            if "Привет, " in favorit_name: 
                name = favorit_name[favorit_name.find('Привет, ') + len('Привет, '):]
                if name not in names:
                    names.append(name)
                    names_text.value = 'Любимые имена:\n'+'\n'.join(names)


    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий: '
        
    def switch_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
    
    def set_random_names(_):
        name_input.value = random.choice(random_names)

    def delete_history(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветсвий\n' + '\n'.join(greeting_history)
        
    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    elavated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED, 
                                        icon_color=ft.Colors.GREEN, on_click=on_button_click)
    
    favorit_button = ft.ElevatedButton('Добавить в избранное', on_click=add_favorit_names)
    clear_button = ft.ElevatedButton('Очистить историю', on_click=clear_history)
    switch_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=switch_theme) 
    random_button = ft.ElevatedButton("Рандомное имя", color=ft.Colors.RED, on_click=set_random_names)
    delete_button = ft.ElevatedButton("Удалить задачу", on_click=delete_history)
    main_object = ft.Row([name_input, elavated_button, switch_button, random_button])
    history_row = ft.Row([history_text, clear_button, favorit_button, delete_button])
    favorit_row = ft.Row([names_text])
    
    page.add(text_hello, main_object, history_text, history_row, favorit_row)

ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)