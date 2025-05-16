from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

#  guardar en archivo
logging.basicConfig(filename='resultados.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/operacion', methods=['GET', 'POST'])
def operacion():
    try:
        if request.method == 'POST':
            data = request.get_json()
            num1 = data.get('num1')
            num2 = data.get('num2')
        else:
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))

        # Validación
        if num1 is None or num2 is None:
            raise ValueError("Falta insertar  num1 o num2")

        resultados = {
            "suma": num1 + num2,
            "resta": num1 - num2,
            "multiplicacion": num1 * num2,
            "division": num1 / num2 if num2 != 0 else "No se puede dividir entre 0"
        }

        # Guardar resultado en archivo
        logging.info(f"num1: {num1}, num2: {num2}, resultados: {resultados}")

        return jsonify({
            "num1": num1,
            "num2": num2,
            "resultados": resultados
        })

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
