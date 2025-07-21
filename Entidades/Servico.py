import streamlit as st

class Servico:
    def __init__(self, id, nome,descricao,preco):
        self.__id = id
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_preco(preco)
    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Informe seu nome")
        self.__nome = nome
    def set_descricao(self,d):
        if d == "":
            raise ValueError(f"Informe a descrição do Serviço")
        self.__descricao = d
    def set_preco(self,p):
        if p <= 0:
            raise ValueError(f"O valor do serviço não pode ser Negativo ou 0")
        self.__preco = p

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao} - {self.__preco}"
    def to_dict(self):
        return {"id": self.__id,"nome": self.__nome,"descricao": self.__descricao, "preco": self.__preco}
    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data['id'],
            nome=data['nome'],
            descricao=data['descricao'],
            preco=data['preco'],
        )
        