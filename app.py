from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
from flask_mail import Mail, Message # type: ignore

load_dotenv()  # loads variables from .env


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

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

mail = Mail(app)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_content = request.form.get('message')

        # Create the email
        msg = Message(subject=f"New Contact Form Message from {name}",
                      recipients=['keerthivasan1617@gmail.com'])  # Your receiving email
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"

        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
            return render_template('contacts.html', success=True)
        except Exception as e:
            print(e)
            flash("Failed to send message. Try again later.", "error")
            return render_template('contacts.html', success=False)

    return render_template('contacts.html', success=False)

if __name__ == "__main__":
    app.run(debug=True)
