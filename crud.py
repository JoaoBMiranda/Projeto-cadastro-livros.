import psycopg2
#-------------------------------------------------------------------------------------------------------- 
# Conexão BD Postgresql
#--------------------------------------------------------------------------------------------------------  
class AppBD:
    def __init__(self): 
        print('Método Construtor')
#-------------------------------------------------------------------------------------------------------- 
    def abrirConexao(self):
        try:         
            self.connection = psycopg2.connect(database="postgres", 
                                               host = "localhost", 
                                               user="postgres",
                                               password="271025",
                                               port="5432")
            print("Conexão com o Banco de Dados aberta com sucesso!")
            print("\n--------------------------------------------------------------")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao se conectar ao banco de dados', error)
#--------------------------------------------------------------------------------------------------------     
    def inserirDados(self, codlivro, titulo, editora, autor, preco, precovenda):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public."livros" 
            ("codlivro", "titulo", "editora","autor","preco", "precovenda") VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_isert = (codlivro, titulo, editora, autor, preco, precovenda) 
            cursor.execute(postgres_insert_query, record_to_isert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Registro inserido com sucesso na tabela LIVROS')
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao inserir registro na tabela LIVROS', error)
        finally:
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
#--------------------------------------------------------------------------------------------------------     
    def atualizarDados(self, codlivro, titulo, editora, autor, preco, precovenda):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = """UPDATE public. "livros" set  "titulo" = %s, 
                               "editora"= %s, "autor" = %s, "preco" = %s, "precovenda" = %s WHERE "codlivro" = %s """
            cursor.execute(sql_update_query, ( titulo, editora, autor, preco, precovenda, codlivro))
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Registro Atualizado com Sucesso!')
            print('Registro Depois da Atualização')
            sql_update_query = """select * from public. "livros" where "codlivro" = %s """
            cursor.execute(sql_update_query, (codlivro,))
            record = cursor.fetchone()
            print(record)  
        except(Exception, psycopg2.Error) as error:
            print('Error na Atualização',  error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
    def excluirDados(self, codlivro):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public. "livros" where "codlivro" = %s"""
            cursor.execute(sql_delete_query, (codlivro))
            self.connection.commit()
            count = cursor.rowcount
            print(count,"Registro excluído com Sucesso!")
        except(Exception, psycopg2.Error) as error:
            print('Error na Exclusão', error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
#--------------------------------------------------------------------------------------------------------              
    def localizarLivro(self, codlivro):
        try:
          self.abrirConexao()
          cursor = self.connection.cursor()
          sql_select_query = """SELECT * FROM livros WHERE codlivro = %s"""
          cursor.execute(sql_select_query, (codlivro,))
          livro = cursor.fetchone()
          self.connection.commit()
          count = cursor.rowcount
          print(count,"Livro Localizado com Sucesso!")
          
          if livro:
              column_names = [desc[0] for desc in cursor.description]
              livro_dict = dict(zip(column_names, livro))
              return livro_dict
          else:
              return None
        except(Exception, psycopg2.Error) as error:
          print('Erro ao localizar o livro:', error)
          return None                    
        finally:
          if (self.connection):
              cursor.close()
              self.connection.close()
              print('A conexão com PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
def atualizarPrecoVenda(self, codlivro, preco_venda):
    try:
        self.abrirConexao()
        cursor = self.connection.cursor()
        sql_update_query = """UPDATE public."livros" SET "preco_venda" = %s WHERE "codlivro" = %s"""
        cursor.execute(sql_update_query, (preco_venda, codlivro))
        self.connection.commit()
        count = cursor.rowcount
        print(count, 'Preço de Venda atualizado com sucesso!')
    except (Exception, psycopg2.Error) as error:
        print('Erro ao atualizar o preço de venda:', error)
    finally:
        if self.connection:
            cursor.close()
            self.connection.close()
            print('A conexão com o PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
