from flask import url_for, jsonify
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from common.config import KEY

class EnvioEmail(object):

    def __init__(self, email, app):
        self.email = email
        self.app = app
        self.app.config.from_pyfile('./common/config_email.cfg')        
        self.s = URLSafeTimedSerializer(KEY)
        self.mail = Mail(self.app)
        
    def enviar_confirmacao(self):           
        try:    
            token = self.s.dumps(self.email, salt='email-confirm')

            msg = Message('Confirmação de email', sender='foxintegrate@foxintegrate.com', recipients=[self.email])

            link = "https://foxintegrate.com/mercurio/confirmar_email/{}".format(token)
            #  url_for('confirm_email', token=token, _external=True)

            msg.body = 'Link de confirmação: {}'.format(link)

            self.mail.send(msg)
        except Exception as ex: 
            return jsonify({'success': False, 'message': str(ex)}), 500
        else:
            return jsonify({'success': True, 'email': self.email, 'token': token}), 200;

    def validar_email(self, token):
        try:
            self.email = self.s.loads(token, salt='email-confirm', max_age=3600)
        except SignatureExpired:
            return jsonify({'success': False, 'message': "O email de confirmação expirou, solicite um novo cadastro."}), 500            
        else:
            return jsonify({'success': True, 'message': "Email confirmado, aguarde a aprovação do responsável"}), 200;            
    

