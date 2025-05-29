from flask import Blueprint, jsonify, request
import main.atividade_model as atividade_model
from clients.client import SchoolSystemClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    try:
        atividades = atividade_model.read_atividades()
        return jsonify(atividades), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@atividade_bp.route('/atividades/<int:id_atividade>', methods=['GET'])
def listar_atividade_ID(id_atividade):
    try:
        atividade = atividade_model.read_atividade(id_atividade)
        return jsonify(atividade), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.get_json()
    try:
        nova_atividade = atividade_model.create_atividade(dados)
        if isinstance(nova_atividade, dict) and nova_atividade.get("message") == "Turma não existe":
            return jsonify({'erro': nova_atividade["message"]}), 400
        return jsonify(nova_atividade), 200


    

    except Exception as e:
        return jsonify({'erro': str(e)}), 500        
    
