from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuração da API Detrack
DETRACK_API = "https://app.detrack.com/api/v2/dn/jobs/search"
API_KEY = "2b86acd2ded193cf662b3c843827a65352844a7bdb510b5e"  # Substitua se necessário

@app.route('/track', methods=['POST'])
def proxy_to_detrack():
    try:
        # Encaminha a requisição para a API da Detrack
        response = requests.post(
            DETRACK_API,
            headers={
                "X-API-KEY": API_KEY,
                "Content-Type": "application/json",
                "User-Agent": "RenderProxy/1.0"
            },
            json=request.json  # Repassa os dados recebidos
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
