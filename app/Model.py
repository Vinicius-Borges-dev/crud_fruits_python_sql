from . import db

class Fruta(db.Model):
    
    __tablename__ = 'frutas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    dataColheita = db.Column(db.Date, nullable=False)
    dataVencimento = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return self.nome