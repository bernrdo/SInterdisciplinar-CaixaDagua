from flask import Flask, render_template
import pymysql
import calc.otimizacao

connection = pymysql.connect(host='bhtaiaprnvjzaehn22ua-mysql.services.clever-cloud.com',
                             user='u8jj1p6lowhnxuwc',
                             password='yitsCNC8bqZ9wvXdwczR',
                             database='bhtaiaprnvjzaehn22ua')

cursor = connection.cursor(pymysql.cursors.DictCursor)
app = Flask(__name__)


@app.route('/')
def otimizacao():
    cursor.execute('SELECT uso_total FROM GastoTotal')
    data = cursor.fetchone()
    volume_em_litros = float(data['uso_total'])

    altura, largura = calc.otimizacao.minimo(volume_em_litros)
    altura = round(altura/100, 2)
    largura = round(largura, 2)

    return render_template('otimizado.html', altura=altura, largura=largura, volume_em_litros=volume_em_litros)


app.run(debug=True)

connection.close()
