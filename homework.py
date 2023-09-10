from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/trousers/')
def trousers():
    trousers_block = [
        {'type': 'adidas Брюки спортивные SQ21 SW PNT',
         'cost': '8 400.00',
         'pict': url_for('static', filename='trousers1.png')},
        {'type': 'adidas Брюки спортивные REAL TR PNT',
         'cost': '1 800.00',
         'pict': url_for('static', filename='trousers2.png')},
        {'type': 'adidas Брюки спортивные CORE18 TR PNT',
         'cost': '2 200.00',
         'pict': url_for('static', filename='trousers3.png')},
        {'type': 'adidas Брюки спортивные EQT TK PNT',
         'cost': '4 800.00',
         'pict': url_for('static', filename='trousers4.png')},
        {'type': 'adidas Брюки спортивные JUVE TR PNT',
         'cost': '1 500.00',
         'pict': url_for('static', filename='trousers5.png')},
        ]
    return render_template('trousers.html', content_block=trousers_block)


@app.route('/jacket/')
def jacket():
    jacket_block = [
        {'type': 'adidas Куртка утепленная QUILTED SST TT',
         'cost': '3 400.00',
         'pict': url_for('static', filename='jacket1.png')},
        {'type': 'adidas Куртка утепленная UTILITAS HO PKA',
         'cost': '10 800.00',
         'pict': url_for('static', filename='jacket2.png')},
        {'type': 'adidas Ветровка M XPLORIC RR J',
         'cost': '4 600.00',
         'pict': url_for('static', filename='jacket3.png')},
        {'type': 'adidas Куртка утепленная XPLORIC Parka',
         'cost': '5 200.00',
         'pict': url_for('static', filename='jacket4.png')},
        {'type': 'adidas Куртка утепленная TXMS PRIMA HDJ',
         'cost': '6 100.00',
         'pict': url_for('static', filename='jacket5.png')}
    ]
    return render_template('jacket.html', content_block=jacket_block)


@app.route('/shoes/')
def shoes():
    shoes_block = [
        {'type': 'adidas Кеды MIDCITY MID',
         'cost': '5 600.00',
         'pict': url_for('static', filename='shoes1.png')},
        {'type': 'adidas Кеды GRAND COURT BASE 2.0',
         'cost': '1 300.00',
         'pict': url_for('static', filename='shoes2.png')},
        {'type': 'adidas Кеды GRAND COURT BASE 2.0',
         'cost': '6 500.00',
         'pict': url_for('static', filename='shoes3.png')},
        {'type': 'adidas Кеды FORUM LOW',
         'cost': '9 300.00',
         'pict': url_for('static', filename='shoes4.png')},
        {'type': 'adidas Кеды HOOPS 3.0 MID',
         'cost': '7 900.00',
         'pict': url_for('static', filename='shoes5.png')}
    ]
    return render_template('shoes.html', content_block=shoes_block)


if __name__ == '__main__':
    app.run(debug=True)