from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/britecore2"
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.app = app
db.init_app(app)

'''Configure model'''
class FeatureRequest(db.Model):
    __tablename__ = 'feature_requests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    client = db.Column(db.String(10))
    priority = db.Column(db.Integer)
    tdate = db.Column(db.DateTime)
    parea = db.Column(db.String(30))

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/requests', methods=['GET', 'POST'])
def requests():
	if request.method == 'POST':
		fr = FeatureRequest( title = request.form['title'], description = request.form['description'],
			client = request.form['client'], priority = request.form['priority'],
			tdate = request.form['date'], parea = request.form['area']   )
		db.session.add(fr)
		db.session.commit()

		return jsonify({"status": 200, "message": "New Feature Request Created"})

	elif request.method == 'GET':
		fs = FeatureRequest.query.all()
		r = []
		for req in fs:
			frequest = {}
			frequest['title'] = req.title
			frequest['description'] = req.description
			frequest['client'] = req.client
			frequest['priority'] = req.priority
			frequest['date'] = req.tdate
			frequest['area'] = req.parea

			r.append(frequest)

		return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)