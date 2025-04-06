from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/track', methods=['POST'])
def proxy():
    DETRACK_URL = "https://app.detrack.com/api/v2/dn/jobs/search"
    
    response = requests.post(
        DETRACK_URL,
        headers={
            "X-API-KEY": "2b86acd2ded193cf662b3c843827a65352844a7bdb510b5e",
            "Content-Type": "application/json"
        },
        json=request.json
    )
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
