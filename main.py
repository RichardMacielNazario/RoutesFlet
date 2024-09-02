import flet as ft
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
import json
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

        requisit = requests.get(f"https://perplan-entradaesaida-default-rtdb.firebaseio.com/.json")
        dic_rrequisicao = requisit.json()
        print(dic_rrequisicao)
        for id_user in dic_rrequisicao:
            user = dic_rrequisicao[id_user]
            if user['Type'] == 'adm':
                if user['Login'] == login_value and user['Senha'] == senha_value:
                    dlg = ft.AlertDialog(ft.alignment.center,bgcolor="white",content=ft.Text("Logado"))
                    self.page.open(dlg)
                    self.page.go("/homeadm")
                else:
                    dlg = ft.AlertDialog(ft.alignment.center,content=ft.Text("Tente Novamente"))
                    self.page.open(dlg)
            else:
                if user['Login'] == login_value and user['Senha'] == senha_value:
                    dlg = ft.AlertDialog(ft.alignment.center,bgcolor="white",content=ft.Text("Logado"))
                    self.page.open(dlg)
                    self.page.go("/home")
                else:
                    dlg = ft.AlertDialog(ft.alignment.center,content=ft.Text("Tente Novamente"))
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
                        ]),
                        ft.Row([
                            ft.Container(
                                content=ft.TextField(
                                    label="Codigo",
                                ),

                            )
                        ])
                    ]
                )
            )
        self.page.update()
def main(page: ft.Page):
    cf = Campofluxo(page)
    print(page.appbar)
    page.go("/login")

ft.app(target=main)