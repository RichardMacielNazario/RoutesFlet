import datetime
import firebase_admin
from firebase_admin import credentials
import flet as ft
import requests.cookies
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin
)
import requests
default_app = firebase_admin.initialize_app()
cred = credentials.RefreshToken('path/to/serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
class Campofluxo():
    def __init__(self, page: Page):
        super().__init__()
        self.title = "fluxo"
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page = page
        self.login_ref = ft.Ref()
        self.senha_ref = ft.Ref()
        self.page.on_route_change = self.route_change

        self.page.update()

    def appbarfunc(self):
        # Definindo a AppBar
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text("Fluxo", ),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.INBOX)
            ]
        )
        return self.appbar

    def verificar(self, e):
        login_value = self.login_ref.current.value
        senha_value = self.senha_ref.current.value

        try:
            requisit = requests.get(f"https://perplan-entradaesaida-default-rtdb.firebaseio.com/.json")
            dic_rrequisicao = requisit.json()
            print(dic_rrequisicao)
        except requests.exceptions.RequestException as error:
            dlg = ft.AlertDialog(
                content=ft.Text(
                    f"Erro na Conexão: {error}",
                    color="black",
                ),
                bgcolor="white"
            )
            self.page.dialog = dlg

        for id_user, user in dic_rrequisicao.items():
            if user['Login'] == login_value and user['Senha'] == senha_value:
                route = "/homeadm" if user['Type'] == 'adm' else '/home'
                dlg = ft.AlertDialog(
                    ft.alignment.center,
                    bgcolor="white",
                    content=ft.Text(
                        "Logado",
                        color="black",
                        )
                )

                self.page.open(dlg)
                self.page.go(route)
                return
        dlg = ft.AlertDialog(
            ft.alignment.center,
            bgcolor="white",
            content=ft.Text(
                "Tente Novamente",
                color="black",
            )
        )
        self.page.open(dlg)
    def route_change(self, route):
        print(f"Route changed to: {self.page.route}")
        self.page.views.clear()
        if self.page.route == "/login":
            self.page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.Container(
                            image_src="img_2.png",
                            image_fit=ft.ImageFit.COVER,
                            expand=True,
                            content=ft.Row([
                            ft.Container(
                                content=ft.Image(src=f"Logo Quadrado 02.png"),
                                width=300,
                                height=500,
                                bgcolor='#547cac',
                                alignment=ft.alignment.center,
                                margin=0,
                                padding=0,
                                border_radius=ft.border_radius.only(top_left=20,bottom_left=20)
                            ),
                            ft.Container(
                                content=ft.Column([
                                ft.Text(value="Login", size=30, color='#547cac'),
                                ft.TextField(label="Seu Login",color='grey',height=50,width=300,prefix_icon=ft.icons.PERSON_OUTLINED,ref=self.login_ref, on_submit=self.verificar),
                                ft.TextField(label="Sua Senha",color='grey',height=50,width=300,prefix_icon=ft.icons.LOCK_OUTLINE,can_reveal_password=True, ref=self.senha_ref, password=True, on_submit=self.verificar),
                                ft.ElevatedButton("Logar",height=50,width=300, on_click=self.verificar,bgcolor='#547cac',color=ft.colors.WHITE)
                                ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor=ft.colors.WHITE,
                                width=700,
                                height=500,
                                alignment=ft.alignment.center,
                                margin=0,
                                padding=0,
                                border_radius=ft.border_radius.only(top_right=20,bottom_right=20)
                            )
                            ],ft.MainAxisAlignment.CENTER,
                            spacing=0
                            )
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif self.page.route == "/homeadm":
            self.page.views.append(
                ft.View(
                    "/homeadm",
                    [
                        self.appbarfunc(),
                        ft.Row([
                            ft.Column([
                                ft.Container(
                                    content= ft.Text(value="Entrada e Saída Campo", color="Red"),
                                    alignment=ft.alignment.center,
                                    bgcolor="yellow",
                                    expand=True,
                                    width=400,
                                    height=400,
                                    border_radius=15,
                                    ink=True,
                                    on_click=lambda e: print("Entrada e Saída Campo"),
                                ),
                                ft.Container(
                                    content=ft.Text(value="Registro de Trabalho Contagem", color="Yellow"),
                                    alignment=ft.alignment.center,
                                    bgcolor="white",
                                    expand=True,
                                    width = 400,
                                    height = 400,
                                    border_radius=15,
                                    ink=True,
                                    on_click=lambda e: self.page.go("/RegistroCont"),
                                )
                            ]),
                            ft.Column([
                                ft.Container(
                                    content=ft.Text(value="Rendimento Contagem", color="Yellow"),
                                    alignment=ft.alignment.center,
                                    bgcolor="red",
                                    expand=True,
                                    width = 400,
                                    height = 400,
                                    border_radius=15,
                                    ink=True,
                                    on_click=lambda e: self.page.go("Rendimento Contagem"),
                                ),
                                ft.Container(
                                    content=ft.Text(value="Gerenciamento", color="Yellow"),
                                    alignment=ft.alignment.center,
                                    bgcolor="grey",
                                    expand=True,
                                    width = 400,
                                    height = 400,
                                    border_radius=15,
                                    ink=True,
                                    on_click=lambda e: print("Gerenciamento"),
                                )
                            ])#final da Column
                        ],alignment=ft.MainAxisAlignment.CENTER,expand=True)#final da ROW
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,

                )
            )
        elif self.page.route == "/home":
            self.page.views.append(
                ft.View(
                    "/home",
                    [
                        self.appbarfunc(),
                        ft.Row([
                            ft.Column([
                                ft.Container(
                                    content= ft.Text(value="Teste", color="RED"),
                                    alignment=ft.alignment.center,
                                    bgcolor="yellow",
                                    expand=True
                                ),
                                ft.Container(
                                    content=ft.Text(value="Teste", color="RED"),
                                    alignment=ft.alignment.center,
                                    bgcolor="white",
                                    expand=True
                                )
                            ]),
                            ft.Column([
                                ft.Container(
                                    content=ft.Text(value="Teste", color="RED"),
                                    alignment=ft.alignment.center,
                                    bgcolor="red",
                                    expand=True
                                ),
                                ft.Container(
                                    content=ft.Text(value="Teste", color="RED"),
                                    alignment=ft.alignment.center,
                                    bgcolor="grey",
                                    expand=True

                                )
                            ])#final da Column
                        ],alignment=ft.MainAxisAlignment.CENTER,expand=True)#final da ROW
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,

                )
            )
        elif self.page.route == "/RegistroCont":
            self.page.views.append(
                ft.View(
                    "/RegistroCont",
                    [
                        self.appbarfunc(),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Codigo",
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Coordenador",
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Ponto",
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Movimentos",
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.Dropdown(
                                        options=[
                                            ft.dropdown.Option("DNIT"),
                                            ft.dropdown.Option("Padrão Perplan"),
                                            ft.dropdown.Option("Pedestre"),
                                            ft.dropdown.Option("Simplificado"),
                                            ft.dropdown.Option("Aproximado"),
                                    ]
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Duração",
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Container(
                                content=ft.ElevatedButton(
                                        "Selecione a Data",
                                        icon=ft.icons.CALENDAR_MONTH,
                                        on_click=lambda e:self.page.open(
                                            ft.DatePicker(
                                                first_date=datetime.datetime(year=2022, month=1, day=1),
                                                last_date=datetime.datetime(year=2030,month=12,day=1),
                                        )
                                    )
                                ),

                            )
                        ],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.ElevatedButton(
                                "Registar",
                                width=100,
                                on_click=lambda e: self.page.open(
                                    ft.AlertDialog(
                                        title=ft.Text("Enviando")
                                    )
                                ),

                                #Chamar function para inserir dados na db
                            )
                    ],alignment = ft.MainAxisAlignment.CENTER)
                    ],vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        self.page.update()
def main(page: ft.Page):
    cf = Campofluxo(page)
    print(page.appbar)
    page.go("/login")

ft.app(target=main)
