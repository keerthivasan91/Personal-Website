from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about',methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.route('/education',methods=['POST','GET'])
def education():
    return render_template('education.html')

@app.route('/projects',methods=['POST','GET'])
def projects():
    return render_template('projects.html')

@app.route('/skills',methods=['POST','GET'])
def skills():
    return render_template('skills.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Example: print form data to console (replace with email or DB logic)
        print(f"New message from {name} ({email}): {message}")

        # Optionally, save message to a database or send via email here

        # Show success message
        return render_template('contacts.html', success=True)

    return render_template('contacts.html', success=False)

if __name__ == "__main__":
    app.run(debug=True)
