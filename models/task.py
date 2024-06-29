class Task:
    def __init__(self, id, titulo, descricao, status=False) -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "titulo":self.titulo,
            "status": self.status

        }
