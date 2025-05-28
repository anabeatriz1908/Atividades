from config import db
import requests
import clients.client as client

class AtividadeNotFound(Exception):
    pass

class Atividades(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome_atividade = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=True)
    peso_porcento = db.Column(db.Integer, nullable=True)
    data_entrega = db.Column(db.String(20), nullable=True)
    professor_id = db.Column(db.Integer, nullable=False)

    def __init__(self, nome_atividade, descricao, peso_porcento, data_entrega, professor_id):
        self.nome_atividade = nome_atividade
        self.descricao = descricao
        self.peso_porcento = peso_porcento
        self.data_entrega = data_entrega
        self.professor_id = professor_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome_atividade": self.nome_atividade,
            "descricao": self.descricao,
            "peso_porcento": self.peso_porcento,
            "data_entrega": self.data_entrega,
            "professor_id": self.professor_id
        }
    
def create_atividade(dados_atividade):
    url = f"{client.API_PRINCIPAL_URL}/professores/{dados_atividade["professor_id"]}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"message": "Professor não encontrado"}
    
    nova_atividade = Atividades(
        nome_atividade = dados_atividade['nome_atividade'],
        descricao = dados_atividade['descricao'],
        peso_porcento = int(dados_atividade['peso_porcento']),
        data_entrega = dados_atividade['data_entrega'],
        professor_id = int(dados_atividade['professor_id'])
    )

    db.session.add(nova_atividade)
    db.session.commit()
    return{'message': 'Atividade cadastrada'}

def read_atividades():
    atividades = Atividades.query.all()
    return [atividade.to_dict() for atividade in atividades]

def read_atividade(id_atividade):
    atividade = Atividades.query.get(id_atividade)

    if not atividade:
        raise AtividadeNotFound(f"Atividade não encontrada.")
    return atividade.to_dict()

