import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tarefa = []

def teste_create_tarefa():
    nova_tarefa_data = {
        "titulo": "Nova Tarefa",
        "descricao":"Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/task", json=nova_tarefa_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tarefa.append(response_json['id'])

def teste_get_allTarefas():

    reponse = requests.get(f"{BASE_URL}/task")
    assert reponse.status_code == 200
    reponse_json = reponse.json()
    assert "task" in reponse_json
    assert "total_task" in reponse_json

def teste_get_byId():
    if tarefa: 
        tarefa_id = tarefa[0]
        response = requests.get(f"{BASE_URL}/task/{tarefa_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert tarefa_id == response_json['id']

def teste_put_tarefa():
    payload = {
            "titulo": "Teste de Atualização",
            "descricao":"Teste da requisição put",
            "status": True
        }
    
    if tarefa:
        tarefa_id = tarefa[0]
        response = requests.put(f"{BASE_URL}/task/{tarefa_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/task/{tarefa_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert tarefa_id == response_json['id']
        assert payload["titulo"] == response_json['titulo']
        assert payload["descricao"] == response_json['descricao']
        assert payload["status"] == response_json['status']

def teste_delete_tarefa():
    if tarefa:
        tarefa_id = tarefa[0]
        response = requests.delete(f"{BASE_URL}/task/{tarefa_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        