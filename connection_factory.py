
import MySQLdb


class ConnectionFactory(object):
    
    def get_connection(self):
        connection = MySQLdb.connect(host='localhost',
                                     user='root',
                                     passwd='root',
                                     db='alura')
        if connection:
            print(f"A conexão foi realizada com sucesso: {connection}.")
            return connection
        else:
            print(f"A conexão não foi realizada.")
            return None
