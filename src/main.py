from fastapi import FastAPI
from typing import Union

from services.Database import buscar_aluno, adicionar_aluno, deletar_aluno, listar_alunos

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/list")
async def get_list(len_list : int):
    list = []
    for i in range(len_list):
        list.append(i+1)
    return list

@app.get("/aluno")
async def get_aluno(matricula : int):
    result = buscar_aluno(matricula)
    mensagem = f"Não havia nenhum aluno com a matricula {matricula}"
    aluno = None
    if result:
        mensagem = 'Sucesso ao obter aluno.'
        aluno = result
    return {'mensagem': mensagem, 'aluno': aluno}

@app.get("/todos_alunos")
async def get_all_alunos():
    alunos = listar_alunos()
    if len(alunos) > 0:
        return {'mensagem': f'Foram obtidos {len(alunos)} alunos.', 'alunos':alunos}
    else:
        return {'mensagem': f'Não foi encontrado nenhum aluno no banco de dados.', 'alunos':alunos}

@app.delete("/deletar_aluno")
async def delete_aluno(matricula:int):
    mensagem = deletar_aluno(matricula)
    return {'mensagem': mensagem}

@app.post("/adicionar_aluno")
async def delete_aluno(matricula:int, nome:str, data:str=None, curso:str=None):
    return {'mensagem': adicionar_aluno(matricula, nome, data, curso)}