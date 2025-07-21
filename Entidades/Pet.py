import streamlit as st

class Pet:
    def __init__(self,id,nome,sexo,tipo,raca,id_dono):
        self.set__id = id
        self.set_nome(nome)
        self.set_sexo(sexo)
        self.set_tipo(tipo)
        self.set_raca(raca)
        self.set_id_dono(id_dono)
    def set_id(self,id):
        self.__id = id
    def set_nome(self,n):
        if n == "":
            raise ValueError("Informe ser nome")
    def set_sexo(self,s):
        sx = s.lower()
        if sx == "" or sx != "feminino" or sx != "masculino":
            raise ValueError("Informe o sexo do seu Pet, Feminino ou Masculino")
        self.__sexo = s
    def set_tipo(self,t):
        if t == "":
            raise ValueError("Informe o tipo do seu Pet, EX: Cachorro, gato,etc...")
        self.__tipo = t
    def set_raca(self,r):
        if r == "":
            raise ValueError("Informe a raca do seu Pet, se não souber, preencha SRD")
        self.__raca = r
    def set_id_dono(self,id_dono):
        self.__id_dono = id_dono
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_sexo(self):
        return self.__sexo
    def get_tipo(self):
        return self.__tipo
    def get_raca(self):
        return self.__raca
    def get_id_dono(self):
        return self.__id_dono
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__sexo} - {self.__tipo} - {self.__raca} - {self.__id_dono}"
    def to_dict(self):
        return {"id": self.__id,"nome": self.__nome,"sexo": self.__sexo, "tipo": self.__tipo, "raca": self.__raca,"dono":self.__id_dono}
    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data['id'],
            nome=data['nome'],
            sexo=data['sexo'],
            tipo=data['tipo'],
            raca=data['raca'],
            dono=data['dono']
        )