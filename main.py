from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'title': "Software Developer",
  'Location': "Bengaluru,India",
  'Salary': 1000000
}, {
  'id': 2,
  'title': "Data Analyst",
  'Location': "Bengaluru,India",
  'Salary': 1000000
}, {
  'id': 3,
  'title': "Marketing",
  'Location': "Bengaluru,India",
  'Salary': 1000000
}, {
  'id': 4,
  'title': "Food Analayst",
  'Location': "Delhi,India",
  'Salary': 1000000
}]


@app.route("/")
def func():
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def apipoint():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
