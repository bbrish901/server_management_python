import psycopg2
#connecting to database
def connectdb():
    filename = "db.config"
    contents = open(filename).read()
    config = eval(contents)
    try:
        dbase =  psycopg2.connect(
            host=config['host'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            port=config['port']
        )
        return dbase
    except Exception as error:
        print('check database details',error)

if __name__ == "__main__":
    connectdb()
