#import MySQLdb
from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()
cursor = connection.cursor()
