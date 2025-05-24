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
    return f"Thank you, {name}! Your application has been submitted."

if __name__ == '__main__':
    app.run(debug=True)

    def check_scholarship_eligibility():
    try:
        # Input GPA
        gpa = float(input("Enter your GPA: "))
        
        # Determine eligibility
        if gpa >= 3.5:
            print("Congratulations, you're eligible for a scholarship!")
