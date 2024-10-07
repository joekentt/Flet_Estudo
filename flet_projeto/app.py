import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()


def main(page: ft.Page):
    page.title = "App Cadastro"

    lista_produtos = ft.ListView()



    def cadastrar_produto(prod):
        novo_produto = Produto(titulo=produto.value, preco=preco_produto.value)
        session.add(novo_produto)
        session.commit()
        lista_produtos.controls.append(
                ft.Container(
                ft.Text(produto.value),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
                )
        )
        page.update()
        print("Produto Cadastrado com sucesso")
        print(preco_produto.value)
        print(produto.value)

    txt_titulo = ft.Text("Titulo do Produto")
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text("Preço do produto")
    preco_produto = ft.TextField(value= "0", label="Digite o preço do produto...", text_align=ft.TextAlign.LEFT)
    botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar_produto)
    
    
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco_produto,
        botao_cadastrar
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
                )
        #print(p)
            )
    page.add(
        lista_produtos,
    )

ft.app(target=main)