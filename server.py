from flask import Flask, redirect

app = Flask(__name__)
new_url = 'http://jarbas.datasciencebr.com/'


@app.route('/')
def root():
    return redirect(new_url, code=301)


@app.route('/<path:page>')
def anypage(page):
    return redirect('{new_url}/{page}'.format(page=page, new_url=new_url),
                    code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
