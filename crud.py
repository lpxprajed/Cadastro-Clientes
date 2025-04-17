from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3

root = Tk()
class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.codigo_entry.focus()
   #criar uma função para conectar ao banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor() 
    #criar uma função para desconectar do banco
    def desconecta_db(self):
        self.conn.close()
    #criar uma função para montar as tabelas
    def montaTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")
        #Criar tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  cliente(
                                cod INTEGER PRIMARY KEY,
                                nome_cliente CHAR(48) NOT NULL,
                                telefone CHAR(20),
                                cidade CHAR(40)
                            );""")  
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_db()
    
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.montaTabelas()
        self.lista_frame2()
        self.menus()
        
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes")#define o titulo da janela
        self.root.configure(background='#1e3743')#define a cor de fundo
        self.root.geometry("700x500")#define o tamanho da janela
        self.root.resizable(True, True)# define se a tela pode ser redimensionada largura e altura
        self.root.maxsize(width= 900, height= 700)#define tamanho máxio
        self.root.minsize(width=500, height=400)#define tamanho minimo
        
        self.icone = PhotoImage(file="C:/Users/lp/Documents/Estudos/projetos/cadastroClientes/icones/cadastro.png")
        self.root.iconphoto(True, self.icone)
        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee',                             
        highlightbackground= '#759feb', highlightthickness=2)  
        self.frame_1.place(relx = 0.02, rely=0.02, relwidth=0.96, relheight=0.46) 
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee',
                    highlightbackground= '#759feb', highlightthickness=2)
        self.frame_2.place(relx = 0.02, rely=0.5, relwidth=0.96, relheight=0.46) 
    def widgets_frame1(self):
        #Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg = '#107db2',
                                fg='white',font = ('verdana',8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely=0.1, relwidth=0.1, 
                             relheight=0.15)
        
         #Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',
                                fg='white' ,font = ('verdana',8, 'bold'))
        self.bt_buscar.place(relx = 0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        #Criação do botão novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg = '#107db2', fg='white'
                                ,font = ('verdana',8, 'bold'))
        self.bt_novo.place(relx = 0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        #Criação do botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg = '#107db2', fg='white'
                                ,font = ('verdana',8, 'bold'))
        self.bt_alterar.place(relx = 0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        #Criação do botão Alterar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg = '#107db2', fg='white'
                                ,font = ('verdana',8, 'bold'))
        self.bt_apagar.place(relx = 0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        #Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = "Código", bg = '#dfe3ee',
                               fg = '#107db2')
        self.lb_codigo.place(relx = 0.05, rely = 0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        #Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome", bg = '#dfe3ee', 
                             fg = '#107db2')
        self.lb_nome.place(relx = 0.05, rely = 0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85)
        #Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text = "Telefone", bg = '#dfe3ee', fg = '#107db2')
        self.lb_telefone.place(relx = 0.05, rely = 0.6)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        #Criação da label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text = "Cidade", bg = '#dfe3ee', fg = '#107db2')
        self.lb_cidade.place(relx = 0.5, rely = 0.6)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, 
                            column=("col1", "col2","col3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)  
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, 
                            relheight=0.85)
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, 
                               relheight=0.85)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.root.destroy()
        
        menubar.add_cascade(label = "Opções", menu=filemenu)
        menubar.add_cascade(label = "Sobre", menu = filemenu2)
        
        filemenu.add_command(label="Sair", command= Quit)
        #filemenu2.add_command(label="Limpa Cliente", command = self.limpa_tela)
Application()
