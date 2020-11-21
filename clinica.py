from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def conectarBd():
    global conexao
    try:
        conexao = pymysql.connect(
                host='127.0.0.1',
                user='root', #felipeolv
                password='', #5924259242
                db='clinica_gestao',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
    except:
        messagebox.showinfo("Erro","Erro ao conectar ao banco de dados.")
        

class JanelaAtendente():

    def cadastrarCliente(self):
        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")

        cpf1= self.cpf.get()
        nome1= self.nome.get()
        end1= self.end.get()
        dnasc1 = self.dnasc.get()
        sex1 = self.sex.get()
        email1 = self.email.get()
        tel1 = self.tel.get()
        tipo_plano1 = self.tipo_plano.get()
        valor_plano1 = self.valor_plano.get()
        cod1 = self.cod.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO cliente VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cpf1,nome1,end1,dnasc1,sex1,email1,tel1,tipo_plano1,valor_plano1,1,cod1))
                conexao.commit()
                messagebox.showinfo("Sucesso","Cliente cadastrado com sucesso.")
        except:
            messagebox.showinfo("Erro","Erro ao cadastrar cliente no banco de dados.")

    def marcarExames(self):
        self.root=Tk()
        self.root.title("Exames")
        Label(self.root,text="Selecione um exame").grid(row=0,column=0,columnspan=2)

        tree = ttk.Treeview(self.root, selectmode="browse", column=('column1', 'column2', 'column3'), show="headings")
        tree.column("column1", width=200, minwidth=50, stretch=NO)
        tree.heading("#1", text="Exame")
        tree.column("column2", width=200, minwidth=50, stretch=NO)
        tree.heading("#2", text="Valor")
        tree.column("column3", width=200, minwidth=50, stretch=NO)
        tree.heading("#3", text="Código")

        coago = ["COAGULOGRAMA", "R$200,00", "01"]
        tree.insert("", END, values=coago, tag='1')
        hdl = ["COLESTEROL HDL", "R$50,00", "02"]
        tree.insert("", END, values=hdl, tag='2')
        ldl = ["COLESTEROL LDL", "R$60,00", "03"]
        tree.insert("", END, values=ldl, tag='3')
        total = ["COLESTEROL TOTAL", "R$110,00", "04"]
        tree.insert("", END, values=total, tag='4')

        tree.grid(row=1, column=0, padx=5, pady=5)


        self.root.mainloop()

    def __init__(self):
        self.root=Tk()
        self.root.title("Atendente")
        Label(self.root, text="Cadastro de Clientes").grid(row=0,column=0,columnspan=4)

        Label(self.root, text="CPF ").grid(row=1,column=0)
        self.cpf=Entry(self.root)
        self.cpf.grid(row=1,column=1,padx=5,pady=5)

        Label(self.root, text="Nome ").grid(row=2, column=0)
        self.nome = Entry(self.root)
        self.nome.grid(row=2, column=1, padx=5, pady=5)

        Label(self.root, text="Endereço ").grid(row=3, column=0)
        self.end = Entry(self.root)
        self.end.grid(row=3, column=1, padx=5, pady=5)

        Label(self.root, text="Data de Nascimento ").grid(row=4, column=0)
        self.dnasc = Entry(self.root)
        self.dnasc.grid(row=4, column=1, padx=5, pady=5)

        Label(self.root, text="Sexo ").grid(row=5, column=0)
        self.sex = Entry(self.root)
        self.sex.grid(row=5, column=1, padx=5, pady=5)

        Label(self.root, text="Email ").grid(row=1, column=2)
        self.email = Entry(self.root)
        self.email.grid(row=1, column=3, padx=5, pady=5)

        Label(self.root, text="Telefone ").grid(row=2, column=2)
        self.tel = Entry(self.root)
        self.tel.grid(row=2, column=3, padx=5, pady=5)

        Label(self.root, text="Tipo de Plano ").grid(row=3, column=2)
        self.tipo_plano = Entry(self.root)
        self.tipo_plano.grid(row=3, column=3, padx=5, pady=5)

        Label(self.root, text="Valor Plano ").grid(row=4, column=2)
        self.valor_plano = Entry(self.root)
        self.valor_plano.grid(row=4, column=3, padx=5, pady=5)

        Label(self.root, text="Código ").grid(row=5,column=2)
        self.cod = Entry(self.root)
        self.cod.grid(row=5,column=3, padx=5,pady=5)

        Button(self.root,text="Cadastrar", width=20, command=self.cadastrarCliente).grid(row=7,column=1, padx=5,pady=5)
        Button(self.root,text="Exames", width=20, command=self.marcarExames).grid(row=7,column=2,padx=5,pady=5)

        self.root.mainloop()

class AdminJanela():

    def __init__(self):
        self.root = Tk()
        self.root.title("Plataforma ADMIN")
        #self.root.geometry("500x500")
        Button(self.root,text="Cadastrar Atendente", width=20, command=JanelaCadastro).grid(row=0,column=0,padx=5,pady=5)
        Button(self.root,text="Cadastrar Vendedores", width=20, command=CadastroVendedor).grid(row=1,column=0,padx=5,pady=5)
        Button(self.root,text="Cadastrar Médicos", width=20,command=CadastroMedicos).grid(row=0,column=1,padx=5,pady=5)
        Button(self.root, text="Consultar Informações", width=20, command=Relatorio).grid(row=1, column=1, padx=5,pady=5)



        self.root.mainloop()

class JanelaLogin():

  def verificaLogin(self):
       autenticado = False
       usuarioAdmin = False
       atendente = False

       try:
           conectarBd()
           messagebox.showinfo("Sucesso","Conectado com sucesso!")
       except:
           messagebox.showinfo("Erro","Erro ao conectar ao banco de dados")

       usuario = self.login.get()
       senha = self.senha.get()

       try:
          with conexao.cursor() as cursor:
             cursor.execute('SELECT * FROM atendente')
             resultados = cursor.fetchall()
       except:
          print('Erro ao fazer a consulta')

       for linha in resultados:
           if usuario == linha['nome'] and senha == linha['senha']:
               if linha['nivel'] == 1:
                   usuarioAdmin = False
                   atendente = True
               elif linha['nivel'] == 2:
                   usuarioAdmin = True
                   atendente = False
               autenticado = True
               break
           else:
               autenticado = False
       if not autenticado:
           messagebox.showinfo("Erro","Login ou senha invalidos")

       if autenticado:
            if usuarioAdmin:
                self.root.destroy()
                AdminJanela()
            elif atendente:
                self.root.destroy()
                JanelaAtendente()


  def __init__(self):
      self.root = Tk()
      self.root.title("Clinica de Exames")
      Label(self.root, text="Login").grid(row=0,column=0, columnspan=2)

      Label(self.root, text="Usuário").grid(row=1,column=0)

      self.login = Entry(self.root)
      self.login.grid(row=1,column=1, padx=5,pady=5)

      Label(self.root, text="Senha").grid(row=2, column=0)

      self.senha = Entry(self.root, show="*")
      self.senha.grid(row=2, column=1,padx=5,pady=5)

      Button(self.root, text="Entrar", command=self.verificaLogin,width=10).grid(row=3,column=1, padx=5,pady=5)


      self.root.mainloop()

class JanelaCadastro():

    def enviarCadastro(self):
        cpf1 = self.cpf.get()
        nome1 = self.nome.get()
        end1 = self.end.get()
        dnasc1 = self.dnasc.get()
        sex1 = self.sex.get()
        senha1 = self.senha.get()
        email1 = self.email.get()
        tel1 = self.tel.get()

        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")

        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO atendente(cpf,nome,endereco,dnasc,sexo,senha,email,tel,nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cpf1,nome1,end1,dnasc1,sex1,senha1,email1,tel1,1))
                conexao.commit()
                messagebox.showinfo('Sucesso','Cadastro feito com sucesso!')
                self.root.destroy()
        except:
            messagebox.showinfo('ERRO','Erro ao cadastrar usuario')

    def __init__(self):
        self.root = Tk()
        self.root.title("Cadastro")
        #self.root.geometry("800x600")
        Label(self.root, text="Cadastro").grid(row=0,column=0, columnspan=2)
        Label(self.root, text="CPF").grid(row=1,column=0)
        self.cpf = Entry(self.root)
        self.cpf.grid(row=1,column=1, padx=5, pady=5)

        Label(self.root, text="Nome").grid(row=2, column=0)
        self.nome = Entry(self.root)
        self.nome.grid(row=2, column=1, padx=5, pady=5)

        Label(self.root, text="Endereço").grid(row=3, column=0)
        self.end = Entry(self.root)
        self.end.grid(row=3, column=1, padx=5, pady=5)

        Label(self.root, text="Data de Nascimento").grid(row=4, column=0)
        self.dnasc = Entry(self.root)
        self.dnasc.grid(row=4, column=1, padx=5, pady=5)

        Label(self.root, text="Sexo").grid(row=1, column=2)
        self.sex = Entry(self.root)
        self.sex.grid(row=1, column=3, padx=5, pady=5)

        Label(self.root, text="Senha").grid(row=2, column=2)
        self.senha = Entry(self.root)
        self.senha.grid(row=2, column=3, padx=5, pady=5)

        Label(self.root, text="Email").grid(row=3, column=2)
        self.email = Entry(self.root)
        self.email.grid(row=3, column=3, padx=5, pady=5)

        Label(self.root, text="Telefone").grid(row=4, column=2)
        self.tel = Entry(self.root)
        self.tel.grid(row=4, column=3, padx=5, pady=5)

        Button(self.root, text="Enviar", width=10, command=self.enviarCadastro).grid(row=5,column=1,columnspan=2)
        #Button(self.root, text="Cadastrar", width=10, command=self.enviarCadastro()).grid(row=5,column=1,columnspan=2)


        self.root.mainloop()

class Relatorio():

    def gerarPagamentos(self):

        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")

        try:
            with conexao.cursor() as cursor:
                self.linhas = cursor.execute("SELECT tipo_plano FROM cliente")
        except:
            messagebox.showinfo("Erro","Erro ao extrair dados do banco de dados.")

        somaParticular = 0
        somaConvenio = 0

        while True:
            self.total = cursor.fetchone()
            if self.total == None:
                break
            
            
            if self.total['tipo_plano'] == 'Convenio':
                somaConvenio += 1
            elif self.total['tipo_plano'] == 'Particular':
                somaParticular += 1                
        
        
        grupos = ["Convenio","Particular"]
        valores = [somaConvenio,somaParticular]
        plt.bar(grupos,valores)
        plt.show()


    def gerarExames(self):
        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")

        try:
            with conexao.cursor() as cursor:
                self.linhas = cursor.execute("SELECT exames FROM cliente")
        except:
            messagebox.showinfo("Erro", "Erro ao extrair dados do banco de dados.")


        self.coago = 0
        self.hdl = 0
        self.ldl = 0
        self.coltotal = 0
        while True:
            self.total = cursor.fetchone()
            if self.total == None:
                break

            if self.total['exames'] == 1:
                self.coago += 1
            elif self.total['exames'] == 2:
                self.hdl += 1
            elif self.total['exames'] == 3:
                self.ldl += 1
            elif self.total['exames'] == 4:
                self.coltotal +=1                



        labels = ['Coagulograma', 'Colesterol HDL', 'Colesterol LDL', 'Colesterol Total']
        sizes = [self.coago,self.hdl,self.ldl,self.coltotal]
        
        #explosão
        explode = (0.1, 0, 0, 0)
        total = sum(sizes)
        
        #cores
        cores = ['lightblue', 'green', 'pink', 'red']
        
        #aplicando explosion e cores
        plt.pie(sizes, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90) 
        plt.axis('equal')
        
        #mostrando grafico
        plt.show()


    def __init__(self):
        self.root = Tk()
        self.root.title("Relatorios")
        #self.root.geometry("800x600")
        Button(self.root, text="Pagamentos",width=20,command=self.gerarPagamentos).grid(row=0,column=0, padx=5,pady=5)
        Button(self.root, text="Exames", width=20, command=self.gerarExames).grid(row=1,column=0, padx=5, pady=5)
        Button(self.root, text="Associação", width=20).grid(row=0, column=1, padx=5, pady=5)
        Button(self.root, text="Ranking Vendedores", width=20).grid(row=1, column=1, padx=5, pady=5)
        self.root.mainloop()

class CadastroVendedor():
    def enviarCadastro(self):
        cpf1 = self.cpf.get()
        nome1 = self.nome.get()
        end1 = self.end.get()
        dnasc1 = self.dnasc.get()
        sex1 = self.sex.get()
        email1 = self.email.get()
        tel1 = self.tel.get()

        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")

        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO vendedores(cpf,nome,endereco,dnasc,sexo,email,tel,nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(cpf1, nome1, end1, dnasc1, sex1, email1, tel1, 1))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso.")
                self.root.destroy()
        except:
            messagebox.showinfo("Erro", "Erro ao cadastrar o vendedor no banco de dados.")

    def __init__(self):
        self.root = Tk()
        self.root.title("Cadastro de Vendedores")
        #self.root.geometry("800x600")
        Label(self.root,text="Cadastro de Vendedores").grid(row=0,column=0,columnspan=2)
        Label(self.root,text="CPF ").grid(row=1,column=0, padx=5,pady=5)
        self.cpf = Entry(self.root)
        self.cpf.grid(row=1,column=1,padx=5,pady=5)
        Label(self.root, text="Nome ").grid(row=2, column=0, padx=5, pady=5)
        self.nome = Entry(self.root)
        self.nome.grid(row=2, column=1, padx=5, pady=5)
        Label(self.root, text="Endereço ").grid(row=3, column=0, padx=5, pady=5)
        self.end = Entry(self.root)
        self.end.grid(row=3, column=1, padx=5, pady=5)
        Label(self.root, text="Data de Nascimento ").grid(row=4, column=0, padx=5, pady=5)
        self.dnasc = Entry(self.root)
        self.dnasc.grid(row=4, column=1, padx=5, pady=5)
        Label(self.root, text="Sexo ").grid(row=1, column=2, padx=5, pady=5)
        self.sex = Entry(self.root)
        self.sex.grid(row=1, column=3, padx=5, pady=5)
        Label(self.root, text="Email ").grid(row=2, column=2, padx=5, pady=5)
        self.email = Entry(self.root)
        self.email.grid(row=2, column=3, padx=5, pady=5)
        Label(self.root, text="Telefone ").grid(row=3, column=2, padx=5, pady=5)
        self.tel = Entry(self.root)
        self.tel.grid(row=3, column=3, padx=5, pady=5)

        Button(self.root,text="Cadastrar",command=self.enviarCadastro).grid(row=5, column=1)

        self.root.mainloop()

class CadastroMedicos():

    def cadastrarMedico(self):
        crm1 = self.crm.get()
        cpf1 = self.cpf.get()
        nome1 = self.nome.get()
        end1 = self.end.get()
        email1 = self.email.get()
        tel1 = self.tel.get()
        dispo1 = self.disp.get()

        try:
            conectarBd()
        except:
            messagebox.showinfo("Erro", "Erro ao conectar ao banco de dados")


        try:
            with conexao.cursor() as cursor:
                cursor.execute("INSERT INTO medicos VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(crm1,cpf1,nome1,end1,email1,tel1,dispo1,1))
                conexao.commit()
                messagebox.showinfo("Sucesso","O médico foi cadastrado com sucesso.")
                self.root.destroy()
        except:
            messagebox.showinfo("Erro","Não foi possível cadastrar o médico.")

    def __init__(self):
        self.root = Tk()
        self.root.title("Cadastrar Médico")
        #self.root.geometry("800x600")

        Label(self.root,text="Cadastro Médico").grid(row=0,column=0,columnspan=2)
        Label(self.root,text="CRM ").grid(row=1,column=0,padx=5,pady=5)
        self.crm = Entry(self.root)
        self.crm.grid(row=1,column=1,padx=5,pady=5)

        Label(self.root, text="CPF ").grid(row=2, column=0, padx=5, pady=5)
        self.cpf = Entry(self.root)
        self.cpf.grid(row=2, column=1, padx=5, pady=5)

        Label(self.root, text="Nome ").grid(row=3, column=0, padx=5, pady=5)
        self.nome = Entry(self.root)
        self.nome.grid(row=3, column=1, padx=5, pady=5)

        Label(self.root, text="Endereço ").grid(row=4, column=0, padx=5, pady=5)
        self.end = Entry(self.root)
        self.end.grid(row=4, column=1, padx=5, pady=5)

        Label(self.root, text="Email ").grid(row=1, column=2, padx=5, pady=5)
        self.email = Entry(self.root)
        self.email.grid(row=1, column=3, padx=5, pady=5)

        Label(self.root, text="Telefone ").grid(row=2, column=2, padx=5, pady=5)
        self.tel = Entry(self.root)
        self.tel.grid(row=2, column=3, padx=5, pady=5)

        Label(self.root, text="Disposição ").grid(row=3, column=2, padx=5, pady=5)
        self.disp = Entry(self.root)
        self.disp.grid(row=3, column=3, padx=5, pady=5)

        Button(self.root,text="Cadastrar",width=20, command=self.cadastrarMedico).grid(row=5, column=2)



        self.root.mainloop()


Relatorio()