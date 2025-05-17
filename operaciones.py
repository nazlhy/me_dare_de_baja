from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

#guardar en archivo
logging.basicConfig(filename='resultados.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/operacion', methods=['GET', 'POST'])
def operacion():
    try:
        if request.method == 'POST':
            data = request.get_json()
            num1 = float(data.get('num1'))
            num2 = float(data.get('num2'))
            operacion = data.get('operacion')
        else:
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))
            operacion = request.args.get('operacion')

        if operacion not in ['suma', 'resta', 'multiplicacion', 'division']:
            return jsonify({"error": "Operación no válida. Usa: suma, resta, multiplicacion o division"}), 400

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 == 0:
                return jsonify({"error": "No se puede dividir entre 0"}), 400
            resultado = num1 / num2

        logging.info(f"Operación: {operacion}, num1: {num1}, num2: {num2}, resultado: {resultado}")

        return jsonify({
            "num1": num1,
            "num2": num2,
            "operacion": operacion,
            "resultado": resultado
        })

    except ValueError:
        return jsonify({"error": "Parámetros inválidos. Asegúrate de enviar números válidos y la operación."}), 400
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

