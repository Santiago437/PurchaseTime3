import flet as ft
from database import create_connection





def main(page):

    def cadastro(e):
        nome = entrada_nome.value
        senha = entrada_senha.value

    # Conectando ao banco de dados
        conn = create_connection()
        cursor = conn.cursor()

    # Inserindo dados na tabela
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()

    # Limpando os campos de texto
        entrada_nome.value = ""
        entrada_senha.value = ""

        ft.SnackBar(page, "Usuário cadastrado com sucesso!")


    def login(e):
        nome = entrada_nome.value
        senha = entrada_senha.value
        conn = create_connection()
        cursor = conn.cursor()

    # Inserindo dados na tabela
        
        try:
            cursor.execute("SELECT nome, senha FROM usuarios WHERE nome = ?", (nome,))
            linha_filtrada = cursor.fetchone()
            item = list(linha_filtrada)
            if item[1] == senha:
                print("usuario logado com sucesso")
            else:
                print("senha incorreta")
        except TypeError:
            print("usuario não encontrado")
        
        
        

        
   
    entrada_nome = ft.TextField(prefix_icon=ft.icons.PEOPLE,border_radius=100,bgcolor='blue',color='white',width=300)
    entrada_senha = ft.TextField(prefix_icon=ft.icons.LOCK,border_radius=100,bgcolor='blue', width=300,)
    
    logo = ft.Image(src="logo.jpg" , width=300 , height=300)
    container = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
   
    page.add(
        container,
        entrada_nome,
        entrada_senha,
        
           ft.ElevatedButton("Entrar",width=300,on_click=login),
           ft.ElevatedButton("Cadastre - se",width=300 ,on_click=cadastro)
        )


ft.app(target=main)