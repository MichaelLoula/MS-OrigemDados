import flet as ft
from flet import *
import pyperclip
from main import file_selected_callback
from plyer import notification

def main(page: ft.Page):
    page.window_maximizable = False
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment='center'
    page.horizontal_alignment = 'center'
    page.title = "MS - Origem Dados"
    page.window_width = 800    
    page.window_height = 700
    page.expand = True
    #page.content = ft.Control()
    page.update()

    inputPath = None
    json_string = None

    success_message = ft.Text(value="", color=ft.colors.WHITE)

    def pick_files_result(e: ft.FilePickerResultEvent):
        nonlocal inputPath
        nonlocal json_string
        nonlocal success_message

        if e.files:
            inputPath = e.files[0].path
            selected_files.value = e.files[0].name
            json_string = file_selected_callback(inputPath)
            success_message.value = "O Json foi Gerado com Sucesso!"
            json_copied_message.value = ""
            json_copied_message.update()
            
        else:
            selected_files.value = "Nenhum Arquivo Selecionado!"
            success_message.value = ""

        page.add(selected_files)    
        selected_files.update()
    

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    
    selected_files = ft.Text()

    def copy_json_to_clipboard():
        if json_string:
            pyperclip.copy(json_string)
            json_copied_message.value = "Json Copiado!"
            success_message.value = ""
            success_message.update()
            json_copied_message.update()

            notification.notify(
                title="MS - Oridem Dados",
                message="O Json foi Copiado!",
                app_name="MS - Oridem Dados"
            )

        else:
            json_copied_message.value = "Nenhum Json Gerado, Escolha um Arquivo!"
            json_copied_message.update()

            notification.notify(
                title="MS - Oridem Dados",
                message="Você Precisa Selecionar um Arquivo",
                app_name="MS - Oridem Dados"
            )

    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE_400))
    json_copied_message = ft.Text(value="", color=ft.colors.WHITE)
    page.overlay.append(pick_files_dialog)
    page.padding = 0
    
    body = Container(

            Stack([
                
                Container(
                    Container(
                        Column([
                            Row([
                                    json_copied_message,success_message
                            ],alignment=MainAxisAlignment.CENTER),
                            Row([
                                ElevatedButton("Buscar Arquivo",
                                               icon=ft.icons.UPLOAD_FILE,
                                               on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False))
                            ],alignment=MainAxisAlignment.CENTER),
                            Row([
                                ElevatedButton(text="Copiar Json",
                                               icon=ft.icons.CONTENT_COPY,
                                               on_click=lambda _: copy_json_to_clipboard()),
                            ],alignment=MainAxisAlignment.CENTER)
                        ],alignment=MainAxisAlignment.CENTER),
                        
                    width=400,
                    height=200,
                    margin=margin.only(top=-30),
                    border_radius=18,
                    blur=Blur(2,3,BlurTileMode.MIRROR), 
                    alignment=alignment.center
                    ),
                    alignment=alignment.center,
                width = 800,    
                height = 700,
                gradient=LinearGradient(['#00008B','#00BFFF'])
                )
            ])
    )
    
    page.add(
        body
    )

ft.app(target=main)
