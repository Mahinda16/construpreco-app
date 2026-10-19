from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"status": "ConstruPreco OK"})

@app.route("/vanar/manifest")
def manifest():
    return jsonify({
        "name": "ConstruPreco",
        "version": "1.0.0",
        "endpoints": {
            "products": "/vanar/products",
            "customers": "/vanar/customers",
            "orders": "/vanar/orders",
            "support": "/vanar/support",
            "inventory": "/vanar/inventory"
        }
    })

@app.route("/vanar/products")
def products():
    return jsonify([
        {"id": "cem-cif-50", "name": "Cimento CIF 50kg", "title": "Cimento CIF 50kg", "price": 6500, "currency": "AOA", "stock": 200, "in_stock": True},
        {"id": "bloco-15", "name": "Bloco 15cm", "title": "Bloco 15cm", "price": 280, "currency": "AOA", "stock": 1000, "in_stock": True},
        {"id": "areia-fina", "name": "Areia Fina m3", "title": "Areia Fina m3", "price": 15000, "currency": "AOA", "stock": 50, "in_stock": True}
    ])

@app.route("/vanar/customers")
def customers():
    return jsonify([
        {"id": "cust-1", "name": "João Silva", "email": "joao@construpreco.ao", "phone": "+244923000001"},
        {"id": "cust-2", "name": "Construtora Luanda Lda", "email": "compras@construtora.ao", "phone": "+244923000002"}
    ])

@app.route("/vanar/orders")
def orders():
    return jsonify([
        {"id": "ord-1", "customer_id": "cust-1", "status": "completed", "total": 65000, "currency": "AOA", "items": [{"product_id": "cem-cif-50", "quantity": 10, "price": 6500}]},
        {"id": "ord-2", "customer_id": "cust-2", "status": "pending", "total": 28000, "currency": "AOA", "items": [{"product_id": "bloco-15", "quantity": 100, "price": 280}]}
    ])

@app.route("/vanar/support")
def support():
    return jsonify([
        {"id": "tick-1", "customer_id": "cust-1", "subject": "Entrega atrasada", "status": "open", "message": "Pedido de cimento com atraso de 2 dias"},
        {"id": "tick-2", "customer_id": "cust-2", "subject": "Dúvida sobre blocos", "status": "closed", "message": "Qual a resistência do bloco 15cm?"}
    ])

@app.route("/vanar/inventory")
def inventory():
    return jsonify([
        {"product_id": "cem-cif-50", "quantity": 200},
        {"product_id": "bloco-15", "quantity": 1000}
    ])

@app.route("/vanar/<path:path>", methods=["HEAD", "OPTIONS"])
def head(path):
    return "", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
