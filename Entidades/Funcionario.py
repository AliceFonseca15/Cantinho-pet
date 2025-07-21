import streamlit as st

class Funcionario:
    def __init__(self, id, nome, email,senha):
        self.__id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Informe seu nome")
        self.__nome = nome
    def set_email(self, email):
        e = email.lower()
        self.__email = e
    def set_senha(self,s):
        if len(s) < 4 : raise ValueError(f"Senha deve ter no mínimo 4 caracteres")
        self.__senha = s
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha}"
    def to_dict(self):
        return {"id": self.__id,"nome": self.__nome,"email": self.__email, "senha": self.__senha}
    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data['id'],
            nome=data['nome'],
            email=data['email'],
            senha=data['senha'],
        )