from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"status": "ConstruPreco OK"})

@app.route("/vanar/manifest")
def manifest():
    return jsonify({
        "name": "ConstruPreco",
        "version": "1.0",
        "endpoints": {
            "products": "/vanar/products",
            "customers": "/vanar/customers",
            "orders": "/vanar/orders",
            "support": "/vanar/support"
        }
    })

@app.route("/vanar/products")
def products():
    return jsonify([
        {"id": "1", "name": "Cimento CIF 50kg", "price": 6500, "currency": "AOA", "stock": 200},
        {"id": "2", "name": "Bloco 15cm", "price": 280, "currency": "AOA", "stock": 1000},
        {"id": "3", "name": "Areia Fina m3", "price": 15000, "currency": "AOA", "stock": 50}
    ])

@app.route("/vanar/customers")
def customers():
    return jsonify([])

@app.route("/vanar/orders")
def orders():
    return jsonify([])

@app.route("/vanar/support")
def support():
    return jsonify([])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
