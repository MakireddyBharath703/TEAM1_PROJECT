om flask import Flask, render_template, request, redirect

app = Flask(_name_)

# In-memory list to simulate database
applications = []

@app.route('/')
def form():
    return render_template('application_form.html')

