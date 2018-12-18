class Tarefas
@app.route('/')
# @check_authorization
def listar():
    return jsonify(tarefas)


@app.route('/<codigo>', methods=['GET'])
def obter(codigo):
    tarefa = encontrar(codigo)

    try:
        tarefa
    except:
        return jsonify({'success': False, 'message': "Não encontrado"}), 400
    else:
        return jsonify(tarefa), 200


@app.route('/', methods=['POST'])
def inserir():
    descricao = request.json['descricao']
    codigo = int(tarefas[len(tarefas) - 1]['codigo']) + 1
    tarefa = {'codigo': codigo, 'descricao': descricao}
    tarefas.append(tarefa)

    return jsonify({'success': True}), 200;


@app.route('/<codigo>', methods=['PUT'])
def editar(codigo: int):
    descricao = request.json['descricao']
    tarefa = encontrar(codigo)

    try:
        tarefa['descricao'] = descricao
    except:
        return jsonify({'success': False, 'message': "Não encontrado"}), 400
    else:
        return jsonify({'success': True}), 200;


@app.route('/<codigo>', methods=['DELETE'])
def excluir(codigo: int):
    try:
        if remover(codigo) == False:
            raise Exception("Não encontrado")
    except:
        return jsonify({'success': False, 'message': "Não encontrado"})
    else:
        return jsonify({'success': True})


@app.route('/index')
def index():
    return "Hello world"
