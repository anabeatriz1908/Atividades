import requests

API_PRINCIPAL_URL = "http://localhost:5000"

class SchoolSystemClient:
    @staticmethod
    def verificar_professor(id_professor):
        url = f"{API_PRINCIPAL_URL}/professores/{id_professor}"
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return {
                    "success": True,
                    "status_code": 200,
                    "data": response.json()
                }
            elif response.status_code == 404:
                return {
                    "success": False,
                    "status_code": 404,
                    "data": {"erro": "Professor não encontrado"}
                }
            else:
                return {
                    "success": False,
                    "status_code": response.status_code,
                    "data": {"erro": "Erro inesperado ao verificar professor"}
                }

        except requests.RequestException as e:
            return {
                "success": False,
                "status_code": 503,
                "data": {"erro": f"Erro de comunicação com a API de professores: {str(e)}"}
            }
