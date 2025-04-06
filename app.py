from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurações da API Detrack
DETRACK_API = "https://app.detrack.com/api/v2/dn/jobs/search"
API_KEY = "2b86acd2ded193cf662b3c843827a65352844a7bdb510b5e"  # 👈 Mantenha isso seguro!

@app.route('/track', methods=['POST'])
def proxy():
    """Rota principal que faz o proxy para a API Detrack"""
    try:
        response = requests.post(
            DETRACK_API,
            headers={
                "X-API-KEY": API_KEY,
                "Content-Type": "application/json"
            },
            json=request.json,
            timeout=10
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def health_check():
    """Rota simples para verificar se o serviço está online"""
    return jsonify({"status": "online", "service": "Detrack Proxy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # ⚠️ Porta OBRIGATÓRIA para o Render
