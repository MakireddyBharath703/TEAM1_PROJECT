om flask import Flask, render_template, request, redirect

app = Flask(_name_)

# In-memory list to simulate database
applications = []

@app.route('/')
def form():
    return render_template('application_form.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    gpa = float(request.form['gpa'])
    essay = request.form['essay']
    # Save to "database"
    applications.append({
        'name': name,
        'email': email,
        'gpa': gpa,
        'essay': essay
    })
