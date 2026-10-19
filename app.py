from flask import Flask, request, jsonify
import os

app = Flask(__name__)

MATERIAIS = [
  {"id": "1", "name": "Cimento CIF 32.5N 50kg - Luanda", "price": 6500, "currency": "Kz", "category": "Cimento"},
  {"id": "2", "name": "Bloco 15cm", "price": 180, "currency": "Kz", "category": "Blocos"},
  {"id": "3", "name": "Varao 12mm 12m", "price": 8500, "currency": "Kz", "category": "Ferro"},
  {"id": "4", "name": "Chapa Zincada", "price": 12500, "currency": "Kz", "category": "Cobertura"},
  {"id": "5", "name": "Tinta Branca 20L", "price": 28500, "currency": "Kz", "category": "Tintas"},
  {"id": "6", "name": "Areia Fina m3", "price": 18000, "currency": "Kz", "category": "Inertes"},
  {"id": "7", "name": "Brita 1 m3", "price": 22000, "currency": "Kz", "category": "Inertes"},
  {"id": "8", "name": "Porta Madeira", "price": 35000, "currency": "Kz", "category": "Madeira"},
]

# Gera até 80
for i in range(9, 81):
  MATERIAIS.append({"id": str(i), "name": f"Material {i} Luanda", "price": 1000 + i*150, "currency": "Kz", "category": "Geral"})

@app.route('/')
def home():
  return jsonify({"status": "CONSTRUPRECO ONLINE", "total": len(MATERIAIS)})

@app.route('/vanar/products')
def vanar_products():
  limit = int(request.args.get('limit', 100))
  cursor = int(request.args.get('cursor', 0)) if request.args.get('cursor') else 0
  page = MATERIAIS[cursor:cursor+limit]
  next_cursor = str(cursor+limit) if cursor+limit < len(MATERIAIS) else None
  return jsonify({"data": page, "next_cursor": next_cursor, "total": len(MATERIAIS)})

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
