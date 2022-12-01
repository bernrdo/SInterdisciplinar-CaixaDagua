import pymysql.cursors

connection = pymysql.connect(host='bhtaiaprnvjzaehn22ua-mysql.services.clever-cloud.com',
                             user='u8jj1p6lowhnxuwc',
                             password='yitsCNC8bqZ9wvXdwczR',
                             database='bhtaiaprnvjzaehn22ua')

try:
    with connection.cursor() as cursor:

        sql = '''
            INSERT INTO GastoUnitario(numero_apartamento, uso_litros)
            VALUES
                (101, 680),
                (102, 930),
                (201, 400),
                (202, 810),
                (301, 650),
                (302, 650),
                (401, 600),
                (402, 770),
                (501, 900),
                (502, 800);
            '''
        cursor.execute(sql)

        sql2 = '''
            INSERT INTO GastoTotal(total_apart, uso_total)
                SELECT COUNT(*), SUM(uso_litros) FROM GastoUnitario;
        '''
        cursor.execute(sql2)

except Exception as error:
    print(error)
    connection.rollback()

finally:
    connection.close()
