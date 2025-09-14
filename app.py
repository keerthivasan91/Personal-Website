from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv # type: ignore
from flask_mail import Mail, Message # type: ignore

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

# Flask-Mail configuration
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT", 587))
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html',active_page='home')

@app.route('/about')
def about():
    return render_template('about.html',active_page='about')

@app.route('/education')
def education():
    return render_template('education.html',active_page='education')

@app.route('/projects')
def projects():
    return render_template('projects.html',active_page='projects')

@app.route('/skills')
def skills():
    return render_template('skills.html',active_page='skills')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name') or "Anonymous"
        email = request.form.get('email') or "Not provided"
        message_content = request.form.get('message') or "No message"

        recipient = os.getenv("MAIL_USERNAME")
        if not recipient:
            flash("Mail username not configured!", "error")
            return render_template('contacts.html', success=False, active_page='contacts')

        msg = Message(
            subject=f"New Contact Form Message from {name}",
            recipients=[recipient]
        )
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"

        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
            return render_template('contacts.html', success=True, active_page='contacts')
        except Exception as e:
            print("Mail send error:", e)
            flash("Failed to send message. Try again later.", "error")
            return render_template('contacts.html', success=False, active_page='contacts')

    return render_template('contacts.html', success=None, active_page='contacts')

@app.route("/test-mail")
def test_mail():
    try:
        recipient = os.getenv("MAIL_USERNAME")
        if not recipient:
            return "MAIL_USERNAME not configured in .env"
        msg = Message("Test Mail", recipients=[recipient])
        msg.body = "Hello, this is a test."
        mail.send(msg)
        return "Mail sent!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
