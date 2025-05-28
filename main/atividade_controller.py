from flask import Blueprint, jsonify, request
import main.atividade_model as atividade_model
from clients.client import SchoolSystemClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    try:
        atividades = atividade_model.read_atividades()
        return jsonify(atividades), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def listar_atividade_ID(id_atividade):
    try:
        atividade = atividade_model.read_atividade(id_atividade)
        return jsonify(atividade), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    dados = request.get_json()

    try:
        resultado_professor = SchoolSystemClient.verificar_professor(dados['id_professor'])
        if not resultado_professor['success']:
            return jsonify(resultado_professor['data']), resultado_professor['status_code']

        nova_atividade = atividade_model.create_atividade(dados)
        return jsonify(nova_atividade), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500        
    
