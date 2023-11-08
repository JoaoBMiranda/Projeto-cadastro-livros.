# Importação das bibliotecas tkinter e crud
#-------------------------------------------------------------------------------------------------------------------------- 
import tkinter as tk 
import crud as crud 
#-------------------------------------------------------------------------------------------------------------------------- 
#Programa Principal
#--------------------------------------------------------------------------------------------------------------------------  
class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
#--------------------------------------------------------------------------------------------------------------------------  
# Rótulo das colunas BD
#--------------------------------------------------------------------------------------------------------------------------         
        self.lblCodigo  = tk.Label(win, text='Código do Livro:')
        self.lblTitulo  = tk.Label(win, text='Titulo:')
        self.lblEditora = tk.Label(win, text='Editora:')
        self.lblAutor   = tk.Label(win, text='Autor:')
        self.lblPreco   = tk.Label(win, text='Preço de Compra:')
        self.lblPreco2  = tk.Label(win, text='Preço de Venda:')
#-------------------------------------------------------------------------------------------------------------------------- 
# Entrada de Dados
#--------------------------------------------------------------------------------------------------------------------------          
        self.txtCodigo  = tk.Entry(bd=5)
        self.txtTitulo  = tk.Entry(bd=5)
        self.txtEditora = tk.Entry(bd=5)
        self.txtAutor   = tk.Entry(bd=5)
        self.txtPreco   = tk.Entry(bd=5)
        self.txtPreco2  = tk.Entry(bd=5)
#--------------------------------------------------------------------------------------------------------------------------  
# Botão de Rádio
#--------------------------------------------------------------------------------------------------------------------------  
        self.btnLocalizar = tk.Button(win, text='Localizar', command= self.fLocalizarLivro)
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command= self.fCadastrarLivro) 
        self.btnAtualizar = tk.Button(win, text='Atualizar', command= self.fAtualizarLivro) 
        self.btnExcluir   = tk.Button(win, text='Excluir',   command= self.fExcluirLivro) 
        self.btnLimpar    = tk.Button(win, text='Limpar',    command= self.fLimparTela) 
        self.btnCalcular  = tk.Button(win, text='Calcular',  command= self.fCalcularPrecoVenda) 
#-------------------------------------------------------------------------------------------------------------------------- 
# Estrutura
#--------------------------------------------------------------------------------------------------------------------------          
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
#--------------------------------------------------------------------------------------------------------------------------  
        self.lblTitulo.place(x=100, y=100)
        self.txtTitulo.place(x=250, y=100)
#--------------------------------------------------------------------------------------------------------------------------          
        self.lblEditora.place(x=100, y=150)
        self.txtEditora.place(x=250, y=150)
#--------------------------------------------------------------------------------------------------------------------------  
        self.lblAutor.place(x=100, y=200)
        self.txtAutor.place(x=250, y=200)
#--------------------------------------------------------------------------------------------------------------------------  
        self.lblPreco.place(x=100, y=250)
        self.txtPreco.place(x=250, y=250)
#--------------------------------------------------------------------------------------------------------------------------  
        self.lblPreco2.place(x=100, y=300)
        self.txtPreco2.place(x=250, y=300)
#-------------------------------------------------------------------------------------------------------------------------- 
        self.btnLocalizar.place(x=400, y=50)
        self.btnCadastrar.place(x=100, y=400)
        self.btnAtualizar.place(x=200, y=400)
        self.btnExcluir.place(x=300, y=400)
        self.btnLimpar.place(x=400, y=400)
        self.btnCalcular.place(x=400 , y=300)
#-------------------------------------------------------------------------------------------------------------------------- 
# Funções de Interação
#--------------------------------------------------------------------------------------------------------------------------      
    def fLerCampos(self):
        try:    
            codlivro = self.txtCodigo.get()
            titulo   = self.txtTitulo.get()
            editora  = self.txtEditora.get()
            autor    = self.txtAutor.get()
            preco    = self.txtPreco.get()
            preco2   = self.txtPreco2.get()
            print('Leitura dos Dados com Sucesso!')
        except:
            print('Não foi possivel ler os Dados.')
        return codlivro, titulo, editora, autor, preco, preco2
#--------------------------------------------------------------------------------------------------------------------------  
    def fLimparTela(self):
        try:
            self.txtCodigo.delete  (0, tk.END)
            self.txtTitulo.delete  (0, tk.END)
            self.txtEditora.delete (0, tk.END)
            self.txtAutor.delete   (0, tk.END)
            self.txtPreco.delete   (0, tk.END)
            self.txtPreco2.delete  (0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')          
#--------------------------------------------------------------------------------------------------------------------------  
    def fCadastrarLivro(self):
        try:
            codlivro, titulo, editora, autor, preco, precovenda = self.fLerCampos()
            self.objBD.inserirDados(codlivro, titulo, editora, autor, preco, precovenda)
            self.fLimparTela()
            print('Produto Cadastro com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')
#--------------------------------------------------------------------------------------------------------------------------
    def fAtualizarLivro(self):
        try:
            codlivro, titulo, editora, autor, preco, precovenda = self.fLerCampos()
            self.objBD.atualizarDados(codlivro, titulo, editora, autor, preco, precovenda)
            self.fLimparTela
            print('Produto Atualizado com sucesso!')
        except:
            print('não foi poss~ivel fazer a atualização.')    
#--------------------------------------------------------------------------------------------------------------------------
    def fExcluirLivro(self):
        try:
            codlivro = self.txtCodigo.get()
            self.objBD.excluirDados(codlivro)
            self.fLimparTela
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do livro.')
#--------------------------------------------------------------------------------------------------------------------------
    def fLocalizarLivro(self):
        try:
             codlivro = self.txtCodigo.get()
             # Realizar a busca no banco de dados pelo código do livro
             livro = self.objBD.localizarLivro(codlivro)        
             if livro:
                self.txtTitulo.delete(0, tk.END)
                self.txtEditora.delete(0, tk.END)
                self.txtAutor.delete(0, tk.END)
                self.txtPreco.delete(0, tk.END)
                self.txtPreco2.delete(0, tk.END)

            # Usar nomes de coluna em vez de índices numéricos
                self.txtTitulo.insert(0, livro['titulo'])
                self.txtEditora.insert(0, livro['editora'])
                self.txtAutor.insert(0, livro['autor'])
                self.txtPreco.insert(0, livro['preco'])
                self.txtPreco2.insert(0, livro['precovenda'])
                
                print('Livro encontrado e detalhes exibidos!')
             else:
                 self.fLimparTela()
                 print('Livro não Encontrado.')    
        except Exception as error:
                print('Erro ao localizar o livro:', error) 
#--------------------------------------------------------------------------------------------------------------------------
    def fCalcularPrecoVenda(self):
        try:
            preco_compra = float(self.txtPreco.get())
            # Adicione suas regras de cálculo aqui, por exemplo, aplicar uma margem de lucro de 30%
            margem_lucro = 0.30
            preco_venda = preco_compra * (1 + margem_lucro)
            self.txtPreco2.delete(0, tk.END)
            self.txtPreco2.insert(0, str(preco_venda))
            print('Preço de Venda calculado com sucesso!')
        except ValueError:
             print('Por favor, insira um valor válido no campo Preço de Compra.')
        except Exception as error:
             print('Erro ao calcular e atualizar o preço de venda:', error)
#--------------------------------------------------------------------------------------------------------------------------
# Estrutura da Interface
#--------------------------------------------------------------------------------------------------------------------------  
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Bem Vindo a Tela de Cadastro')
janela.geometry("600x500")
janela.mainloop()  
   
