import psycopg2

#-------------------------------------------------------------------------------------------------------- 
# Conexão BD Postgresql
#--------------------------------------------------------------------------------------------------------  
class AppBD:
    def __init__(self): 
        print('Método Construtor')
#-------------------------------------------------------------------------------------------------------- 
# Estabelece a conexão com o banco de dados PostgreSQL
#-------------------------------------------------------------------------------------------------------- 
    def abrirConexao(self):
        try:      
            self.connection = psycopg2.connect(database="postgres", 
                                               host="localhost", 
                                               user="postgres",
                                               password="271025",
                                               port="5432")
            print("Conexão com o Banco de Dados aberta com sucesso!")
            print("\n--------------------------------------------------------------")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao se conectar ao banco de dados', error)
#-------------------------------------------------------------------------------------------------------- 
# Método para inserir dados na tabela 
#-------------------------------------------------------------------------------------------------------- 
    def inserirDados(self, codlivro, titulo, assunto, editora, autor, preco, precovenda):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Query SQL para inserir dados na tabela "livros"
            postgres_insert_query = """ INSERT INTO public."livros" 
            ("codlivro", "titulo", "assunto", "editora","autor","preco", "precovenda") VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            # Parâmetros a serem inseridos na query
            record_to_insert = (codlivro, titulo, assunto, editora, autor, preco, precovenda) 
            cursor.execute(postgres_insert_query, record_to_insert)
            # Confirma a transação
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Registro inserido com sucesso na tabela LIVROS')
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print('Falha ao inserir registro na tabela LIVROS', error)
        finally:
            if(self.connection):
                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
#-------------------------------------------------------------------------------------------------------- 
# Método para atualizar dados na tabela 
#-------------------------------------------------------------------------------------------------------- 
    def atualizarDados(self, codlivro, titulo, assunto, editora, autor, preco, precovenda):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Query SQL para atualizar dados na tabela "livros"
            sql_update_query = """UPDATE public. "livros" set  "titulo" = %s, 
                              "assunto"=%s, "editora"= %s, "autor" = %s, "preco" = %s, "precovenda" = %s WHERE "codlivro" = %s """
            cursor.execute(sql_update_query, (titulo, assunto, editora, autor, preco, precovenda, codlivro))
            # Confirma a transação
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Registro Atualizado com Sucesso!')
            print('Registro Depois da Atualização')
            # Query SQL para selecionar o registro atualizado
            sql_update_query = """select * from public. "livros" where "codlivro" = %s """
            cursor.execute(sql_update_query, (codlivro,))
            record = cursor.fetchone()
            print(record)  
        except (Exception, psycopg2.Error) as error:
            print('Error na Atualização',  error)
        finally:
            if (self.connection):
                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
# Método para excluir dados na tabela 
#-------------------------------------------------------------------------------------------------------- 
    def excluirDados(self, codlivro):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Query SQL para excluir dados na tabela "livros"
            sql_delete_query = """Delete from public. "livros" where "codlivro" = %s"""
            cursor.execute(sql_delete_query, (codlivro,))
            # Confirma a transação
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com Sucesso!")
        except (Exception, psycopg2.Error) as error:
            print('Error na Exclusão', error)
        finally:
            if (self.connection):
                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
# Método para localizar um livro na tabela 
#--------------------------------------------------------------------------------------------------------       
    def localizarLivro(self, codlivro):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Query SQL para selecionar dados na tabela "livros" pelo código
            sql_select_query = """SELECT * FROM "livros" WHERE codlivro = %s"""
            cursor.execute(sql_select_query, (codlivro,))
            livro = cursor.fetchone()
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Livro Localizado com Sucesso!")

            if livro:
                # Obtem nomes de coluna
                column_names = [desc[0] for desc in cursor.description]
                # Cria um dicionário usando nomes de coluna e valores
                livro_dict = dict(zip(column_names, livro))
                return livro_dict
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print('Erro ao localizar o livro:', error)
            return None                    
        finally:
            if (self.connection):
                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
#-------------------------------------------------------------------------------------------------------- 
# Método para carreagar todo o registro na tabela para salvar em um aqrquivo excel 
#-------------------------------------------------------------------------------------------------------- 
    def carregarRegistros(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Query SQL para selecionar todos os registros na tabela "livros"
            sql_select_query = """SELECT * FROM public."livros" """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print("Registros Exibidos com Sucesso!")
            print(registros)
            return registros
        except (Exception, psycopg2.Error) as error:
            print('Erro ao exibir registros:', error)
            return None
        finally:
            if self.connection:
                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                self.connection.close()
                print('A conexão com PostgreSQL foi fechada.')
