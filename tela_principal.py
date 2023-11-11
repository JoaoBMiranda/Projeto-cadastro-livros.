import tkinter as tk
import crud as crud
import pandas as pd
import openpyxl

#-------------------------------------------------------------------------------------------------------------------------- 
#Programa Principal
#--------------------------------------------------------------------------------------------------------------------------  
class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()  # Instancia um objeto da classe AppBD para interagir com o banco de dados
        
#--------------------------------------------------------------------------------------------------------------------------
# Definição dos rótulos e campos de entrada     
#--------------------------------------------------------------------------------------------------------------------------        
        self.lblCodigo  = tk.Label(win, text='Código do Livro:', font=("Times New Roman",13))
        self.lblTitulo  = tk.Label(win, text='Titulo:',          font=("Times New Roman",13))
        self.lblAssunto = tk.Label(win, text='Assunto:',         font=("Times New Roman",13))
        self.lblEditora = tk.Label(win, text='Editora:',         font=("Times New Roman",13))
        self.lblAutor   = tk.Label(win, text='Autor:',           font=("Times New Roman",13))
        self.lblPreco   = tk.Label(win, text='Preço de Compra:', font=("Times New Roman",13))
        self.lblPreco2  = tk.Label(win, text='Preço de Venda:',  font=("Times New Roman",13))
#--------------------------------------------------------------------------------------------------------------------------
# Definição dos campos de entrada      
#--------------------------------------------------------------------------------------------------------------------------  
        self.txtCodigo  = tk.Entry(bd=5)
        self.txtTitulo  = tk.Entry(bd=5)
        self.txtAssunto = tk.Entry(bd=5)
        self.txtEditora = tk.Entry(bd=5)
        self.txtAutor   = tk.Entry(bd=5)
        self.txtPreco   = tk.Entry(bd=5)
        self.txtPreco2  = tk.Entry(bd=5)
#--------------------------------------------------------------------------------------------------------------------------
# Definição dos botões e associação com métodos       
#--------------------------------------------------------------------------------------------------------------------------
        self.btnBuscar          = tk.Button(win, text='Localizar', command= self.fLocalizarLivro)
        self.btnCadastrar       = tk.Button(win, text='Cadastrar', command= self.fCadastrarLivro) 
        self.btnAtualizar       = tk.Button(win, text='Atualizar', command= self.fAtualizarLivro) 
        self.btnExcluir         = tk.Button(win, text='Excluir',   command= self.fExcluirLivro) 
        self.btnLimpar          = tk.Button(win, text='Limpar',    command= self.fLimparTela) 
        self.btnCalcular        = tk.Button(win, text='Calcular',  command= self.fCalcularPrecoVenda)
        self.btnExibirRegistros = tk.Button(win, text='Salvar',    command=self.salvarRegistros)      
#--------------------------------------------------------------------------------------------------------------------------
# Posicionamento dos rótulos e campos de entrada na interface gráfica    
#--------------------------------------------------------------------------------------------------------------------------  
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
  
        self.lblTitulo.place(x=100, y=100)
        self.txtTitulo.place(x=250, y=100)

        self.lblAssunto.place(x=100, y=150)
        self.txtAssunto.place(x=250, y=150)
             
        self.lblEditora.place(x=100, y=200)
        self.txtEditora.place(x=250, y=200)
  
        self.lblAutor.place(x=100, y=250)
        self.txtAutor.place(x=250, y=250)
  
        self.lblPreco.place(x=100, y=300)
        self.txtPreco.place(x=250, y=300)
  
        self.lblPreco2.place(x=100, y=350)
        self.txtPreco2.place(x=250, y=350)
#--------------------------------------------------------------------------------------------------------------------------
# Posicionamento dos botões na interface gráfica  
#-------------------------------------------------------------------------------------------------------------------------- 
        self.btnBuscar.place(x=400, y=50)
        self.btnCadastrar.place(x=100, y=400)
        self.btnAtualizar.place(x=200, y=400)
        self.btnExcluir.place(x=300, y=400)
        self.btnLimpar.place(x=400, y=400)
        self.btnCalcular.place(x=400 , y=300)
        self.btnExibirRegistros.place(x=500, y=400)  
#--------------------------------------------------------------------------------------------------------------------------
# Método para ler os dados dos campos de entrada       
#-------------------------------------------------------------------------------------------------------------------------- 
 
    def fLerCampos(self):
        try:    
            codlivro = self.txtCodigo.get()
            titulo   = self.txtTitulo.get()
            assunto  = self.txtAssunto.get()
            editora  = self.txtEditora.get()
            autor    = self.txtAutor.get()
            preco    = self.txtPreco.get()
            preco2   = self.txtPreco2.get()
            print('Leitura dos Dados com Sucesso!')
        except:
            print('Não foi possivel ler os Dados.')
        return codlivro, titulo, assunto, editora, autor, preco, preco2
#--------------------------------------------------------------------------------------------------------------------------
# Método para limpar os campos de entrada       
#-------------------------------------------------------------------------------------------------------------------------- 
    def fLimparTela(self):
        try:
            self.txtCodigo.delete  (0, tk.END)
            self.txtTitulo.delete  (0, tk.END)
            self.txtAssunto.delete (0, tk.END)
            self.txtEditora.delete (0, tk.END)
            self.txtAutor.delete   (0, tk.END)
            self.txtPreco.delete   (0, tk.END)
            self.txtPreco2.delete  (0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')          
#--------------------------------------------------------------------------------------------------------------------------
# Método para cadastrar um novo livro       
#--------------------------------------------------------------------------------------------------------------------------
    def fCadastrarLivro(self):
        try:
            codlivro, titulo, assunto, editora, autor, preco, precovenda = self.fLerCampos()
            self.objBD.inserirDados(codlivro, titulo, assunto, editora, autor, preco, precovenda)
            self.fLimparTela()
            print('Produto Cadastro com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')
#--------------------------------------------------------------------------------------------------------------------------
# Método para atualizar informações de um livro      
#--------------------------------------------------------------------------------------------------------------------------
    def fAtualizarLivro(self):
        try:
            codlivro, titulo, assunto, editora, autor, preco, precovenda = self.fLerCampos()
            self.objBD.atualizarDados(codlivro, titulo, assunto, editora, autor, preco, precovenda)
            self.fLimparTela()
            print('Produto Atualizado com sucesso!')
        except:
            print('não foi poss~ivel fazer a atualização.')    
#--------------------------------------------------------------------------------------------------------------------------
# Método para excluir um livro      
#--------------------------------------------------------------------------------------------------------------------------
    def fExcluirLivro(self):
        try:
            codlivro = self.txtCodigo.get()
            self.objBD.excluirDados(codlivro)
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do livro.')
#--------------------------------------------------------------------------------------------------------------------------
# Método para localizar um livro no banco de dados      
#--------------------------------------------------------------------------------------------------------------------------
    def fLocalizarLivro(self):
        try:
             codlivro = self.txtCodigo.get()
             # Realizar a busca no banco de dados pelo código do livro
             livro = self.objBD.localizarLivro(codlivro)        
             if livro:
                self.txtTitulo.delete (0, tk.END)
                self.txtEditora.delete(0, tk.END)
                self.txtAssunto.delete(0, tk.END)
                self.txtAutor.delete  (0, tk.END)
                self.txtPreco.delete  (0, tk.END)
                self.txtPreco2.delete (0, tk.END)

                self.txtTitulo.insert (0, livro['titulo'])
                self.txtEditora.insert(0, livro['editora'])
                self.txtAssunto.insert(0, livro['assunto'])
                self.txtAutor.insert  (0, livro['autor'])
                self.txtPreco.insert  (0, livro['preco'])
                self.txtPreco2.insert (0, livro['precovenda'])
                
                print('Livro encontrado e detalhes exibidos!')
             else:
                 self.fLimparTela()
                 print('Livro não Encontrado.')    
        except Exception as error:
                print('Erro ao localizar o livro:', error) 
#--------------------------------------------------------------------------------------------------------------------------
# Método para calcular o preço de venda com base no preço de compra      
#--------------------------------------------------------------------------------------------------------------------------
    def fCalcularPrecoVenda(self):
        try:
            preco_compra = float(self.txtPreco.get())
            # Adicione suas regras de cálculo aqui, por exemplo, aplicar uma margem de lucro de 10%
            margem_lucro = 0.10
            preco_venda = preco_compra * (1 + margem_lucro)
            self.txtPreco2.delete(0, tk.END)
            self.txtPreco2.insert(0, str(preco_venda))
            print('Preço de Venda calculado com sucesso!')
        except ValueError:
             print('Por favor, insira um valor válido no campo Preço de Compra.')
        except Exception as error:
             print('Erro ao calcular e atualizar o preço de venda:', error)
#--------------------------------------------------------------------------------------------------------------------------
# Método para salvar registros em uma planilha Excel       
#--------------------------------------------------------------------------------------------------------------------------
    def salvarRegistros(self):
        try:
            # Carrega os registros do banco de dados
            registros = self.objBD.carregarRegistros()

             # Cria um DataFrame com os registros
            df = pd.DataFrame(registros, columns=["Código", "Título", "Assunto", "Editora", "Autor", "Preço de Compra", "Preço de Venda"])

            # Salva o DataFrame em um arquivo Excel no diretório atual
            df.to_excel("registros_livros.xlsx", index=False)

            print("Registros salvos em registros_livros.xlsx com sucesso!")
        except Exception as error:
            print("Erro ao salvar os registros em uma planilha Excel:", error)     
#--------------------------------------------------------------------------------------------------------------------------
#        
#--------------------------------------------------------------------------------------------------------------------------
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Bem Vindo a Tela de Cadastro')
janela.geometry("600x500")
janela.mainloop()  
   
