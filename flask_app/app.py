from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    whatsapp = request.form['whatsapp']
    mensagem = request.form['mensagem']

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER
    msg['Subject'] = 'Novo Registro de Usuário'
    body = f"Nome: {nome}\nEmail: {email}\nWhatsApp: {whatsapp}\nMensagem: {mensagem}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, EMAIL_USER, text)
        server.quit()
        return redirect(url_for('index'))
    except Exception as e:
        return f'Houve um problema ao enviar o email: {e}'

if __name__ == '__main__':
    app.run(debug=True)
