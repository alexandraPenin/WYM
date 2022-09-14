import mailbox
import psycopg2

#!/usr/bin/python



class User:
    def __init__(self, nom, prenom, mail, telephone):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone

class pgdb :
    def __init__(self, host, port, dbname="postgres", user="Eunice", password="mysecretpassword"):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user=user
        self.password=password
        self.conn = None

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(user=self.user, host=self.host, dbname=self.dbname, port=self.port, password=self.password)
            self.conn = conn
            # create a cursor"Hornowski", "Eunice", "0606060606", "e@gmail.com")
            print(db_version)
        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection closed.')
        return conn

    def insert_user(self, user):
        print("insertion")
        cur = self.conn.cursor()
        res = cur.execute('INSERT INTO users (nom, prenom, telephone, mail) VALUES(%s, %s, %s, %s)', (user.nom, user.prenom, user.mail, user.telephone))
        self.conn.commit()
        print(res)
    
    def get_users(self):
        print("get")
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM users')
        res=cur.fetchall()
        #print(res)
        return(res)

    def delete_users(self):
        cur = self.conn.cursor()
        res = cur.execute('DELETE * FROM users')


    def disconnect(self):
        self.conn.close()
    
if __name__ == '__main__':
    # params = {'user':'Eunice', 'password':'mysecretpassword', 'port':5432, 'host':'172.17.0.2'}
    # conn = psycopg2.connect(**params)
    # cur = conn.cursor()
    mydb = pgdb("localhost",5432)
    mydb.connect()
    user = User('bou','ra','boura@mail.org','06000000')
    mydb.insert_username(user=user)
    mydb.get_users()
    mydb.disconnect()