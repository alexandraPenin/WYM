import mailbox
import psycopg2

class Metrics:
    def __init__(self, execution_time, word_freq, text_len):
        self.execution_time = execution_time
        self.word_freq = word_freq
        self.text_len = text_len


class User:
    def __init__(self, nom, prenom, mail, telephone):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone

class pgdb :
    def __init__(self, host, port, dbname="postgres", user="wym_admin", password="admin"):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(user=self.user, host=self.host, dbname=self.dbname, port=self.port, password=self.password)

            cur = self.conn.cursor()
            # create a cursor"Hornowski", "Eunice", "0606060606", "e@gmail.com")
            # print(db_version)
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection closed.')
        return conn

    def create_users_table(self):
        print(f"attempting to create table: users (the creation will be skipped if the table already exists)")
        cur = self.conn.cursor()
        res = cur.execute(f"""
                CREATE TABLE IF NOT EXISTS users (
                    nom TEXT,
                    prenom TEXT,
                    telephone TEXT,
                    mail TEXT);
                """)
        self.conn.commit()


    def create_metrics_table(self):
        print(f"attempting to create table: metrics (the creation will be skipped if the table already exists)")
        cur = self.conn.cursor()
        res = cur.execute(f"""
                CREATE TABLE IF NOT EXISTS metrics (
                    execution_time FLOAT,
                    text_len INT,
                    word_freq TEXT);
                """)
        self.conn.commit()

    def insert_metrics(self, metrics):
        print("insertion")
        cur = self.conn.cursor()
        
        res = cur.execute('INSERT INTO metrics (execution_time, word_freq, text_len) VALUES(%s,%s,%s)', (metrics.execution_time, metrics.word_freq, metrics.text_len))
        self.conn.commit()
        print(f"inserted: {res}")

    def insert_user(self, user):
        print("insertion")
        cur = self.conn.cursor()
        res = cur.execute('INSERT INTO users (nom, prenom, telephone, mail) VALUES(%s, %s, %s, %s)', (user.nom, user.prenom, user.mail, user.telephone))
        self.conn.commit()
        print(f"inserted: {res}")
    
    def get_data(self, table_name):
        print("get")
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM {table_name}')
        res = cur.fetchall()
        #print(res)
        return(res)

    #def delete_users(self):
    #    cur = self.conn.cursor()
    #    res = cur.execute('DELETE * FROM users')


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
    mydb.get_data('users')
    mydb.disconnect()
