#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Abaixo está o código da Tela de Login

#Importa o modulo pyodbc para conexão com banco de dados
import pyodbc

#Importa o módulo tkinter para construção de interfaces gráficas
from tkinter import *

#Importa a classe ttk do módulo tkinter
from tkinter import ttk

#Função que verificas se as credenciais do usuário estão corretas
def verifica_credenciais():
    
    #Driver - Drive
    #Server - Servidor
    #Database - Nome do Banco de Dados
    conexao = pyodbc.connect ("Driver={SQLite3 ODBC Driver};Server = localhost;Database=Sistema_Controle_Patrimonial.db")
    
    # cursor- Ferramenta para executar os comandos em SQL
    cursor = conexao.cursor()
    
    #Executando uma query que seleciona os usuários que possuem o nome de usúario e senha inderidos pelo usuário
    cursor.execute("SELECT * FROM usuarios WHERE Nome = ? AND Senha = ?",(nome_usuario_entry.get(),senha_usuario_entry.get()))
   
    #Recebendo o resultado da query               
    usuario =cursor.fetchone()
                   
        
    if usuario :
        
        #Fechando a Janela de Login  
        janela_principal.destroy()
                 

        #Driver - Drive
        #Server - Servidor
        #Database - Nome do Banco de Dados

        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server = localhost;Database=Sistema_Controle_Patrimonial.db")

        #UID - Login
        #PWD - Senha

        # Criando a conexão
        conexao = pyodbc.connect(dadosConexao)

        #Cria um objeto cursor para executar os comandos SQL no banco de dados
        cursor= conexao.cursor()

        #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
        conexao.execute("Select * From BensPatrimoniais")

        print("Conectado com sucesso!")

        def listar_dados():

            #Limpar os valores da treeview
            for i in treeview.get_children():
                treeview.delete(i)

            #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
            cursor.execute("Select * From BensPatrimoniais")

            #Armazena os valores retornados pelo comando SQL em uma variável
            valores = cursor.fetchall()

            #Adicionar valores na treeview
            for valor in valores:

                #Preencher linha por linha
                treeview.insert("","end", values=(valor[0], valor[1], valor[2], valor[3], valor[4]))


        #Criando uma janela tkinter com o título "Cadastro de Bens Patrimoniais"
        janela = Tk()
        janela.title("Cadastro de Bens Patrimoniais")

        #Definindo a cor de fundo para a janela
        janela.configure(bg= "#FFD700")

        #Deixando a janela em tela cheia
        janela.attributes("-fullscreen" , True)

        Label(janela, text="IDUsuarioResponsavel: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        Id = Entry(janela, font="Arial 16")
        Id.grid(row=0, column=3, padx=10, pady=10)

        Label(janela, text="Plaqueta: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        plaqueta = Entry(janela, font="Arial 16")
        plaqueta.grid(row=0, column=6, padx=10, pady=10)

        Label(janela, text="Bens Patrimoniais: ", font="Arial 25", fg="blue",bg="#F5F5F5").grid(row=2, column=0, columnspan=10,padx=10, pady=10)


        #Função para cadastrar o produto
        def cadastrar():

            #Cria uma nova janela para cadastrar o produto
            janela_cadastrar = Toplevel(janela)

            janela_cadastrar.title("Cadastro de Bens Patrimoniais")

            #bg - backgroud (cor do fundo)
            #Defindo a cor de fundo da janela
            janela_cadastrar.configure(bg="#B0E0E6")

            #Define a altura e largura da janela
            largura_janela = 700
            altura_janela = 500

            #Obtem a largua e a ltura da tela do computador
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()


            #Calcula a posição da janlea para centraliza-la na tela
            """ Essa linhas calculam a posição em que a janela deve ser exibida na tela do computador de forma centralizada. a posição
            x é definida pela diferença entre a largura da tela e a largura da janlea, dividia por 2. Já a posição y é definida pela 
            diferença entre a altura da tela e a altura da janela, também dividida por 2. O operador "//" é utilizado para realizar a divisão
            interia, ou seja, retornar apenas o resultado inteiro da divisão"""

            pos_x = (largura_tela // 2) - (largura_janela //2)
            pos_y = (altura_tela // 2) - (altura_janela //2)


            #Definir a posição da janela

            """definir a geometria da janela principal, especificando a largura e altura da janela, bem como a posição onde a janela será
            exibida na tela, usando as variáveis previamente definidas para a posição x e y da janela. O formato utilizado é uma string que
            contém os valores de largura, altura, posição y da janela separados por"x" e "+" e passados como argumentos para o método 
            geometry() da janela principal.
            O formato '{}x{}+{}+{}' é uma string de formatação que espera quatro valores, que correspondem à largura da janela, altura da janela,
            posição x da janela e posição y da janela, respectivamente. 
            Esses valores são passados na ordem especificada para a string de formatação e, em seguida, são utilizados para definir a geometria 
            da janela através do método geometry do objeto janela_principal"""

            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)


            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth":2,"relief": "groove"}

            Label(janela_cadastrar, text="Id:", font=("Arial", 12),bg="#E0FFFF").grid(row=0,column=0, padx=10, pady=10, stick="W")
            id_cadastrar = Entry(janela_cadastrar, font=("Arial", 12),**estilo_borda)
            id_cadastrar.grid(row=0,column=1, padx=10, pady=10)

            Label(janela_cadastrar, text="Plaqueta:", font=("Arial", 12),bg="#E0FFFF").grid(row=1,column=0, padx=10, pady=10, stick="W")
            plaqueta_cadastrar = Entry(janela_cadastrar, font=("Arial", 12),**estilo_borda)
            plaqueta_cadastrar.grid(row=1,column=1, padx=10, pady=10)

            Label(janela_cadastrar, text="Descricao:", font=("Arial", 12),bg="#E0FFFF").grid(row=2,column=0, padx=10, pady=10, stick="W")
            descricao_cadastrar = Entry(janela_cadastrar, font=("Arial", 12),**estilo_borda)
            descricao_cadastrar.grid(row=2,column=1, padx=10, pady=10)

            Label(janela_cadastrar, text="Valor:", font=("Arial", 12),bg="#E0FFFF").grid(row=3,column=0, padx=10, pady=10, stick="W")
            valor_cadastrar = Entry(janela_cadastrar, font=("Arial", 12),**estilo_borda)
            valor_cadastrar.grid(row=3,column=1, padx=10, pady=10)


            Label(janela_cadastrar, text="IDUsuarioResponsavel:", font=("Arial", 12),bg="#E0FFFF").grid(row=4,column=0, padx=10, pady=10, stick="W")
            IDUsuarioResponsavel_cadastrar = Entry(janela_cadastrar, font=("Arial", 12),**estilo_borda)
            IDUsuarioResponsavel_cadastrar.grid(row=4,column=1, padx=10, pady=10)


           #Cria uma função para salvar os dados no Banco de Dados

            def salvar_dados():

                   #Cria uma tupla coom os valores dos campos de texto
                novo_bem_cadastrar = ( id_cadastrar.get(),plaqueta_cadastrar.get(), descricao_cadastrar.get(), valor_cadastrar.get(), IDUsuarioResponsavel_cadastrar.get())


                #Executa um comando SQL para inserir os dados na tabela Produtos no Banco de dados
                cursor.execute("INSERT INTO BensPatrimoniais (Id,Plaqueta,Descricao,Valor,IDUsuarioResponsavel) Values (?, ?, ?, ?, ?)", novo_bem_cadastrar)
                conexao.commit()#Gravando no BD

                print("Dados do Bem cadastrados com sucesso !" )

                #Fecha a janela de cadastro
                janela_cadastrar.destroy()

                #Chamar a função para listar os valores do banco de dados na treeview
                listar_dados()

            #columnspan - quantas colunas vai ocupar no grid
            botao_salvar_dados = Button(janela_cadastrar,text="Salvar", font=("Arial",16), command=salvar_dados)
            botao_salvar_dados.grid(row=5,column=0,columnspan =2, padx=0, pady=0,stick="NSEW") 

             #columnspan - quantas colunas vai ocupar no grid
            botao_cancelar = Button(janela_cadastrar,text="Cancelar", font=("Arial",16), command= janela_cadastrar.destroy)
            botao_cancelar.grid(row=6,column=0,columnspan =2, padx=0, pady=0,stick="NSEW") 

        #Cria um botão para gravar(Cadastrar) os dados na tabela Bens Patrimoniais do banco de dados
        botao_gravar = Button(janela, text="Cadastrar novo bem", command=cadastrar, font="Arial 26")
        botao_gravar.grid(row=4, column=0, columnspan=4, stick="NSEW", padx=10, pady=5)

            #Define o estilo da TREEVIEW
        style = ttk.Style(janela)   
            #Criando a treeview
        treeview = ttk.Treeview(janela, style="mystyle.Treeview")

        style.theme_use("default")

        #Configurando    
        style.configure("mystyle.Treeview", font=("Arial",14))  

        treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("Id","Plaqueta", "Descricao","Valor","IDUsuarioResponsavel"),show="headings",height=20)

        treeview.heading("Id", text="Id do Bem")
        treeview.heading("Plaqueta", text="Plaqueta")
        treeview.heading("Descricao", text="Descrição do Bem")
        treeview.heading("Valor", text="Valor do Bem")
        treeview.heading("IDUsuarioResponsavel", text="Responsavel pelo Bem")


        #A primeira coluna, identificada como "#0"
        #Stretch=NO, indica que a coluna não deve esticar para preeencher o espaço disponível
        treeview.column("#0",width=0,stretch=NO)
        treeview.column("Id",width=100)
        treeview.column("Plaqueta",width=200)
        treeview.column("Descricao",width=500)
        treeview.column("Valor",width=200)
        treeview.column("IDUsuarioResponsavel",width=200)



        treeview.grid(row=3,column=0,columnspan=10,stick="NSEW")

        #Chamar a função para listar os valores do banco de dados na treeview
        listar_dados()

        def editar_dados(event):

            #Obtem o item selecionado na Treeview
            item_selecionado = treeview.selection()[0]

            #Obtem os  valores do item selecionado na Treeview
            valores_selecionados = treeview.item(item_selecionado)['values']

            #Cria uma nova janela para cadastrar o produto
            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Cadastro")

            #bg - backgroud (cor do fundo)
            #Defindo a cor de fundo da janela
            janela_edicao.configure(bg="#B0E0E6")

            #Define a altura e largura da janela
            largura_janela = 600
            altura_janela = 400

            #Obtem a largua e a ltura da tela do computador
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()


            #Calcula a posição da janlea para centraliza-la na tela
            pos_x = (largura_tela // 2) - (largura_janela //2)
            pos_y = (altura_tela // 2) - (altura_janela //2)


            #Definir a posição da janela
            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

            for i in range(5):
                janela_edicao.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)


            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth":2,"relief": "groove"}

            Label(janela_edicao, text="Id:", font=("Arial", 16),bg="#E0FFFF").grid(row=0,column=0, padx=10, pady=10, stick="W")
            id_edicao = Entry(janela_edicao, font=("Arial", 16),**estilo_borda,bg="#E0FFFF", textvariable=StringVar(value=valores_selecionados[0]))
            id_edicao.grid(row=0,column=1, padx=10, pady=10)

            Label(janela_edicao, text="Plaqueta:", font=("Arial", 16),bg="#E0FFFF").grid(row=1,column=0, padx=10, pady=10, stick="W")
            plaqueta_edicao =  Entry(janela_edicao, font=("Arial", 16),**estilo_borda,bg="#E0FFFF", textvariable=StringVar(value=valores_selecionados[1]))
            plaqueta_edicao.grid(row=1,column=1, padx=10, pady=10)

            Label(janela_edicao, text="Descricao do Bem:", font=("Arial", 16),bg="#E0FFFF").grid(row=2,column=0, padx=10, pady=10, stick="W")
            descricao_edicao =  Entry(janela_edicao, font=("Arial", 16),**estilo_borda,bg="#E0FFFF", textvariable=StringVar(value=valores_selecionados[2]))
            descricao_edicao.grid(row=2,column=1, padx=10, pady=10)

            Label(janela_edicao, text="Valor:", font=("Arial", 16),bg="#E0FFFF").grid(row=3,column=0, padx=10, pady=10, stick="W")
            valor_edicao =  Entry(janela_edicao, font=("Arial", 16),**estilo_borda,bg="#E0FFFF", textvariable=StringVar(value=valores_selecionados[3]))
            valor_edicao.grid(row=3,column=1, padx=10, pady=10)

            Label(janela_edicao, text="IDUsuarioResponsavel:", font=("Arial", 16),bg="#E0FFFF").grid(row=4,column=0, padx=10, pady=10, stick="W")
            IDUsuarioResponsavel_edicao =  Entry(janela_edicao, font=("Arial", 16),**estilo_borda,bg="#E0FFFF", textvariable=StringVar(value=valores_selecionados[4]))
            IDUsuarioResponsavel_edicao.grid(row=4,column=1, padx=20, pady=10)



           #Cria uma função para salvar os dados no Banco de Dados

            def salvar_edicao():

                #Obtem os novos valores selecionados na Treeview
                nova_id = id_edicao.get()
                nova_plaqueta = plaqueta_edicao.get()
                nova_descricao = descricao_edicao.get()
                novo_valor = valor_edicao.get()
                novo_IDUsuarioResponsavel = IDUsuarioResponsavel_edicao.get()

                #Atualiza os valores do item selecionado
                treeview.item(item_selecionado, values=(nova_id,nova_plaqueta, nova_descricao, novo_valor,novo_IDUsuarioResponsavel ))

                #Executa um comando SQL para ALTERAR os dados na tabela BENS PATRIMONIAIS no Banco de dados
                cursor.execute("UPDATE BensPatrimoniais SET Id = ?, Plaqueta = ?, Descricao = ?, Valor = ?, IDUsuarioResponsavel = ?  WHERE Id = ?",
                (nova_id,nova_plaqueta,nova_descricao,novo_valor,novo_IDUsuarioResponsavel, valores_selecionados[0]))

                conexao.commit()#Gravando no BD

                print("Alteração de dados do Bem realizada com sucesso !!" )

                #Fecha a janela de cadastro
                janela_edicao.destroy()

                #Chamar a função para listar os valores do banco de dados na treeview
                 #listar_dados()

            #columnspan - quantas colunas vai ocupar no grid
            botao_salvar_edicao = Button(janela_edicao,text="Alterar", font=("Arial",16), bg="#008000",fg="#FFFFFF",command=salvar_edicao)
            botao_salvar_edicao.grid(row=5,column=0, padx=20, pady=20,stick="NSEW") 

            def deletar_registro():
                #Recuperar a Plaqueta de identificação selecionada na treeview
                selected_item = treeview.selection()[0]
                Id = treeview.item(selected_item)['values'][0]

                #Deletando o registro do Banco de Dados
                cursor.execute("DELETE FROM BensPatrimoniais WHERE Id = ?",(Id,))

                conexao.commit()

                #Fecha a janela de cadastro
                janela_edicao.destroy()

                #Atualizar o dados sem o novo registro
                listar_dados()


             #columnspan - quantas colunas vai ocupar no grid
            botao_deletar_edicao = Button(janela_edicao,text="Baixar Bem", font=("Arial",18), bg="#FF0000",fg="#FFFFFF",command=deletar_registro)
            botao_deletar_edicao.grid(row=5,column=1, padx=20, pady=20,stick="NSEW") 


        #Adiciona o evento de duplo clique na Treeview para editar os dados do Bem
        treeview.bind("<Double-1>", editar_dados)

        #Configura a janela para utilizar a barra de menus criada
        menu_barra = Menu(janela)
        janela.configure(menu=menu_barra)

        #Cria menu chamado arquivo
        """o parâmetro "tearoff=0" é utilizado no tkinter para controlar a exibição de uma linha pontilhada no ínicio de menus cascata
        Ao definir "tearoff=0", a linha pontilhada  não será exibida e o menu cascata fivará fixo na janela, não podendo ser destacado 
        ou movido para outra posição."""


        menu_arquivo = Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label= "Arquivo", menu= menu_arquivo)

        #Cria uma opção no menu "Arquivo"chamado "Cadastrar"
        menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

        #Cria uma opção no menu "Arquivo"chamado "Sair"
        menu_arquivo.add_command(label="Sair", command=janela.destroy)

         #Limpo os dados da treeview
        def limparDados():

                    #Limpanda os valores da treeview
            for i in treeview.get_children():

                        #Deleto linha por linha
                        treeview.delete(i)

        def filtrar_dados(IDUsuarioResponsavel,Plaqueta):

                    #if - se
                    #Verifica se os campos estão vazio
                    if not IDUsuarioResponsavel.get() and not Plaqueta.get():

                        listar_dados()

                        #Se ambos os campos estiverem vazios, não faz nada
                        return

                        sql = "SELECT * FROM BensPatrimoniais"

                        params = []

                    if IDUsuarioResponsavel.get():

                        sql += " WHERE IDUsuarioResponsavel LIKE ?"

                        params.append('%' + IDUsuarioResponsavel.get() + '%')

                        if Plaqueta.get():

                            if IDUsuarioResponsavel.get():
                                sql += " AND"
                        else:
                            sql += " WHERE"
                        sql += " Plaqueta LIKE ?"
                        params.append('%' + Plaqueta.get() + '%')


                    if params:
                        cursor.execute(sql, tuple(params))
                        BensPatrimoniais = cursor.fetchall()
                    else:
                # Tratar o caso em que não há parâmetros para evitar o erro
                        BensPatrimoniais = []


                    #Limpa os dados da treeview
                    limparDados()

                      #Preenche treeview com os dados filtrados
                    for dado in Id:

                      treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3], dado[4]))

                    IDUsuarioResponsavel.bind('<KeyRelease>', lambda e: filtrar_dados(IDUsuarioResponsavel,Plaqueta))
                    Plaqueta.bind('<KeyRelease>', lambda e: filtrar_dados(IDUsuarioResponsavel,Plaqueta))

         #Deleta registro
        def deletar():
                #Recuperar a Plaqueta de identificação selecionada na treeview
                selected_item = treeview.selection()[0]
                Id = treeview.item(selected_item)['values'][0]

                #Deletando o registro do Banco de Dados
                cursor.execute("DELETE FROM BensPatrimoniais WHERE Id = ?",(Id,))

                conexao.commit()

                #Atualizar o dados sem o novo registro
                listar_dados()


        #Cria um botão para deletar os dados na tabela Bens Patrimoniais do banco de dados
        botao_deletar = Button(janela, text="Baixar Bens", command=deletar, font="Arial 26")
        botao_deletar.grid(row=4, column=4, columnspan=4, stick="NSEW", padx=25, pady=5)

        #Inicia a janela Tkinter
        janela.mainloop()

         #Fechar o cursor e a conexao
        cursor.close()
        conexao.close()

                   
    else: 
                   
                mensagem_lbl = Label(janela_principal, text="Nome de usuário ou senha incorrretos",fg="red")
                mensagem_lbl.grid(row=3, column=0, columnspan=2)
                   

 #Criando a janela principal para a tela de login
janela_principal =Tk()
janela_principal.title("Tela de Login")

#bg - backgroud (cor do fundo)
#Defindo a cor de fundo da janela
janela_principal.configure(bg="#F5F5F5")

#Define a altura e largura da janela
largura_janela = 450
altura_janela = 300

#Obtem a largua e a ltura da tela do computador
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()


#Calcula a posição da janlea para centraliza-la na tela
""" Essa linhas calculam a posição em que a janela deve ser exibida na tela do computador de forma centralizada. a posição
x é definida pela diferença entre a largura da tela e a largura da janlea, dividia por 2. Já a posição y é definida pela 
diferença entre a altura da tela e a altura da janela, também dividida por 2. O operador "//" é utilizado para realizar a divisão
interia, ou seja, retornar apenas o resultado inteiro da divisão"""

pos_x = (largura_tela // 2) - (largura_janela //2)
pos_y = (altura_tela // 2) - (altura_janela //2)


#Definir a posição da janela

"""definir a geometria da janela principal, especificando a largura e altura da janela, bem como a posição onde a janela será
exibida na tela, usando as variáveis previamente definidas para a posição x e y da janela. O formato utilizado é uma string que
contém os valores de largura, altura, posição y da janela separados por"x" e "+" e passados como argumentos para o método 
geometry() da janela principal.
O formato '{}x{}+{}+{}' é uma string de formatação que espera quatro valores, que correspondem à largura da janela, altura da janela,
posição x da janela e posição y da janela, respectivamente. 
Esses valores são passados na ordem especificada para a string de formatação e, em seguida, são utilizados para definir a geometria 
da janela através do método geometry do objeto janela_principal"""

janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))


#fg - foreground (cor da letra)
tiulo_lbl =Label(janela_principal, text ="Tela de Login", font= "Arial 20",fg="blue", bg="#F5F5F5")

#row -linha
#column - coluna
#columnspan -quantas colunas vai ocupar no grid
#pady - espaço
tiulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

#Campo label
nome_usuario_lbl = Label(janela_principal, text="Nome de Usuário", font="Arial 14 bold",bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, stick="e")#Norte,Sul,E,W

#Campo label

senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold",bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, stick="e")#Norte,Sul,E,W

#Criando um entry para o Nome de Usuario com a fonte Arial 14
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10)

#Criando um entry para o Senha de Usuario com a fonte Arial 14
senha_usuario_entry = Entry(janela_principal, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10)

#STICK - PREENCHE AS LATERAIS NSEW(Norte, Sul,Leste,Oeste)
entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

#STICK - PREENCHE AS LATERAIS NSEW(Norte, Sul,Leste,Oeste)
sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

"""esse código está dentro de um laço "for" que executa 5 vezes e serve para configurar o comportamento de uma grade (ou "grid")
no tkinter. A função "grid_rowconfigure()" permite definir as configurações de uma determinada linha na grade, com dois parâmetros:
o índice da linha e um peso (ou "weight") que determina como essa linha deve se comportar em relação as outras linhas da grade.

No código em questão, o laço "for" está configurado as 5 linhas da grade da janela_principal com um peso igual a 1.
Isso significa que todas as linhas terão a mesma altura e que a altura da janela será dividida igualmente entre elas."""

for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)
    
    
"""Este código é usado para definir a configuração das colunas da grade na janela principal.Ele utiliza um loop"for" para iterar 
através de duas colunas da grade e chama o método "grid_columnconfigure" do objeto" janela_principal" para definir o "weight"
(peso)como 1.

O parâmetro "weigth" é uma propriedade do gerenciador de layout do Tkinter que define a prioridade de expansão das colunas (ou linhas)
quando a janela é redimensionada. valores mais altos de "weight" significam que a coluna irá expandir mais do que as outras que possuem 
valores mais baixos de "weight". Ao configurar as colunas com um "weigth" de 1,a janela principal será capaz de expandir uniformemente 
as colunas em toda a largura da janela quando ela for redimensionada."""

for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

#Inicia a janela Tkinter
janela_principal.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




