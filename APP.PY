from flask import Flask, render_template, request

app = Flask(__name__)

assignments = []

@app.route('/')
def index():
    return render_template('index.html', assignments=assignments)

@app.route('/grade', methods=['POST'])
def grade():
    student_name = request.form['student_name']
    assignment_name = request.form['assignment_name']
    grade = int(request.form['grade'])
    assignments.append({'student_name': student_name, 'assignment_name': assignment_name, 'grade': grade})
    # After adding a new assignment, we redirect to the index page to render the updated assignment list
    return render_template('index.html', assignments=assignments)

if __name__ == '__main__':
    app.run(debug=True)
