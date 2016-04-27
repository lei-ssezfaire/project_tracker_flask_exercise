from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html", first=first, last=last, github=github)
    return html
    # return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/student-search")
def get_student_form():
	"""SHow form for searching for a student."""

	return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add new student"""

    return render_template("new_student.html")


@app.route("/student-results", methods=['POST'])
def student_results():
	"""Show form for searching for a student."""

	first = request.form.get('first-name')
	last = request.form.get('last-name')
	github = request.form.get('github')
	hackbright.make_new_student(first, last, github)

	return render_template("new_student_results.html",first=first, last=last, github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
