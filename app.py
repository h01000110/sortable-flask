from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sortable(db.Model):
    __tablename__ = 'sortables'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String)

    def __init__(self, data):
        self.data = data


db.create_all()


@app.route('/')
def index():
    sort = Sortable.query.filter_by(id=1).first()
    ordem = str(sort.data)
    return render_template('index.html', ordem=ordem)


@app.route('/post', methods=['GET', 'POST'])
def post():
    json = request.json
    x = json.replace('item[]=', ',')
    y = x.replace('&,', '')
    final = y.replace(',', '')

    sort = Sortable.query.filter_by(id=1).first()
    sort.data = final

    db.session.commit()

    return str('')


if __name__ == '__main__':
    app.run(debug=True)
