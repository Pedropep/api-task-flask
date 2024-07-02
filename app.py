from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

task = []
task_id_controle = 1
@app.route('/task', methods=['POST'])
def creat():
    global task_id_controle
    data = request.get_json()
    new_task = Task(id=task_id_controle, titulo=data.get('titulo'), descricao=data.get('descricao'))
    task_id_controle += 1
    task.append(new_task)
    print(task)
    return jsonify({"message":"Nova tarefa criada com sucesso", "id":new_task.id})

#Busca todas as tarefas
@app.route('/task', methods=['GET'])
def get_all():
    task_list = [task.to_dict() for task in task]

    output = {
                "task": task_list,
                "total_task": len(task_list)
            }   
    return jsonify(output)

@app.route('/task/<int:id>', methods=['GET'])
def busca_task_id(id):
    for tarefa in task:
        if tarefa.id == id:
            return jsonify(tarefa.to_dict())
    
    return jsonify({'message':'Não foi possivel encontrar a tarefa'}), 404

#Atualiza tarefa
@app.route('/task/<int:id>', methods=["PUT"])
def atualiza_task_id(id):

    tarefa = None
    for t in task:
        if t.id == id:
            tarefa = t
            print(t)
            break            
    
    if tarefa is None:
        return jsonify({"message":"Não foi possível encontrar a atividade!"}), 404    
   
    data = request.get_json()
    tarefa.titulo = data['titulo']
    tarefa.descricao = data['descricao'] 
    tarefa.status = data['status']   
    
    print(tarefa)

    return jsonify({"message":"Tarefa atualiza com sucesso!"})

#Deleta tarefa por id
@app.route('/task/<int:id>', methods=["DELETE"])
def deleta_tarefa(id):

    tarefa = None
    for t in task:
        if t.id == id:
            tarefa = t
            break

    if not tarefa:
        return jsonify({"message":"Não foi possivel encontrar a tarefa!"}), 404
    
    task.remove(tarefa)
    return jsonify({"message":"Tafera excluida com sucesso"})

    
    
if __name__ == "__main__":
    app.run(debug=True)