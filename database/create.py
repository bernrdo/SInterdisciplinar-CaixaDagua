import pymysql.cursors

connection = pymysql.connect(host='bhtaiaprnvjzaehn22ua-mysql.services.clever-cloud.com',
                             user='u8jj1p6lowhnxuwc',
                             password='yitsCNC8bqZ9wvXdwczR',
                             database='bhtaiaprnvjzaehn22ua')

try:
    with connection.cursor() as cursor:

        cursor.execute('DROP TABLE IF EXISTS GastoUnitario, GastoTotal')

        sql = '''
            CREATE TABLE GastoUnitario(
                uso_litros int NOT NULL,
                numero_apartamento int(4) NOT NULL,
                PRIMARY KEY(numero_apartamento)
            );
            '''

        cursor.execute(sql)

        sql2 = '''
            CREATE TABLE GastoTotal(
                uso_total int NOT NULL,
                total_apart int NOT NULL,
                PRIMARY KEY(total_apart)
            );
        '''

        cursor.execute(sql2)

except Exception as error:
    print(error)
    connection.rollback()

finally:
    connection.close()
