import json
import os
from random import randint
from string import ascii_lowercase
import flask

app = flask.Flask(__name__)


@app.get("/shorten")
def get_shorten():
    return f'<h1>Укорочиватель ссылок</h1> ' \
           f'<p>Введите ссылку</p> ' \
           f'<form action="/shorten" method="POST">' \
           f'<input type="text" name= "url">' \
           f'<input type="submit" value="Укоротить"> </form>'


@app.get("/<short_url>/stats")
def get_stats(short_url):
    data = read_data_file()
    if short_url in data:
        return f'<h1>Укорочиватель ссылок</h1> ' \
               f'<h3>Короткая ссылка:</h3> ' \
               f'<a href=http://localhost:5000/{short_url}>http://localhost:5000/{short_url}</a>' \
               f'<h3>Ваша ссылка:</h3>' \
               f'<a href={data[short_url]["original_url"]}>{data[short_url]["original_url"]}</a>' \
               f'<h3>Запросов по ссылке: {data[short_url]["request_count"]}</h3>'
    else:
        flask.abort(404)


@app.post("/shorten")
def post_shorten():
    original_url = flask.request.form['url']
    if not original_url:
        flask.abort(400)
    elif original_url[:8] != 'https://' and original_url[:7] != 'http://':
        flask.abort(400)
    data = read_data_file()

    short_url = create_short_url()
    data[short_url] = {"original_url": original_url, "request_count": 0}
    write_data_file(data)

    return flask.redirect(f'/{short_url}/stats')


@app.get('/')
def get_root():
    return flask.redirect('/shorten')


@app.get('/<short_url>')
def get_short_url(short_url):
    data = read_data_file()
    original_url = data[short_url]['original_url']
    data[short_url]['request_count'] += 1
    write_data_file(data)
    return flask.redirect(original_url)


def create_short_url():
    short_url = ''
    for _ in range(3):
        i = randint(0, 25)
        short_url += ascii_lowercase[i]
    return short_url


def read_data_file():
    if os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as file:
            return json.load(file)
    else:
        return {}


def write_data_file(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == '__main__':
    app.run(debug=False, use_debugger=False, use_reloader=False, passthrough_errors=True)
