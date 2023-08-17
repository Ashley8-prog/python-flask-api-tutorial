from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text , 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded = request.get_json()
    #Agrego el diccionario a la lista de todos
    todos.append(decoded)
    # print(todos)

    #devolver lista actualizada al front-end
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)

    longitud = len(todos) #cantidad de elementos
    print("longitud: " , longitud)
   
    maxIndex = longitud - 1 #rango de indices desde 0 hasta maxIndex

    if position > maxIndex:
        return jsonify({"message": "el número es mayor a la cantidad "}) , 400

    if longitud == 0:
        return jsonify({"message": "La lista está vacia"}) , 400

    todos.pop(position)

    json_text = jsonify(todos)
    return json_text, 200

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=3245, debug=True) 
    #debug nos permite hacer pruebas o revisiones en vivo del codigo

# These two lines should always be at the end of your app.py file.
