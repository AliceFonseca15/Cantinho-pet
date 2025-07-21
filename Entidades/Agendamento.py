import streamlit as st

class Agendamento:
    def __init__(self, id, id_cliente,id_pet,id_funcionario,id_motorista,status,status_transporte,data_pedido,servicos,endereco,data_finalizado):
        self.set_id = id
        self.set_id_cliente(id_cliente)
        self.set_id_pet(id_pet)
        self.set_senha(id_funcionario)
        self.set_fone(id_motorista)
        self.set_status(status)
        self.set_status_transporte(status_transporte)
        self.set_data_pedido(data_pedido)
        self.set_servicos(servicos)
        self.set_endereco(endereco)
        self.set_data_finalizado(data_finalizado)
    def set_id(self,id):
        self.__id = id
    def set_id_cliente(self,id):
        self.__id_cliente = id  
    def set_id_pet(self,id):
        self.__id_pet = id
    def set_id_funcionario(self,id):
        self.__id_funcionario = id
    def set_id_motorista(self,id):
        self.__id_motorista = id    
    def set_status(self,s):
        ss = s.lower()
        if ss == "" or ss !=  "aguardando início" or ss != "em andamento" or ss != "concluído":
            raise ValueError("Informe o status do Serviço") 
        self.__status = s
    def set_status_transporte(self,s):
        ss = s.lower()
        if ss == "" or ss !=  "não iníciado" or ss != "em rota" or ss != "entregue":
            raise ValueError("Informe o status do Transporte") 
        self.__status_transporte = s
    def set_data_pedido(self,d):
        if d == "":
            raise ValueError("A data do pedido não pode está vazia")
        self.__data_pedido = d
    def set_servicos(self,id):
        self.__servicos = id
    def set_endereco(self,e):
        if e == "":
            raise ValueError("Informe o endereço")
        self.__endereco = e
    def set_data_finalizado(self,d):
        if d == "":
            raise ValueError("A data de entrega não pode está vazia")
        self.__data_finalizado = d
    def get_id(self):
        return self.__id
    def get_id_cliente(self):
        return self.__id_cliente
    def get_id_pet(self):
        return self.__id_pet
    def get_id_funcionario(self):
        return self.__id_funcionario
    def get_id_motorista(self):
        return self.__id_motorista
    def get_status(self):
        return self.__status
    def get_status_transporte(self):
        return self.__status_transporte
    def get_data_pedido(self):
        return self.__data_pedido
    def get_servicos(self):
        return self.__servicos
    def get_endereco(self):
        return self.__endereco
    def get_data_finalizado(self):
        return self.__data_finalizado
    def __str__(self):
        return f"{self.__id} - {self.__id_cliente} - {self.__id_pet} - {self.__id_funcionario} - {self.__id_motorista} - {self.__status} - {self.__status_transporte} - {self.__data_pedido} - {self.__servicos} - {self.__endereco} - {self.__endereco} - {self.__data_finalizado}"
    def to_dict(self):
        return {"id": self.__id,"id_clinete": self.__id_cliente,"id_pet": self.__id_pet, "id_funcionario": self.__id_funcionario, "id_motorista": self.__id_motorista,"status":self.__status, "status_transporte":self.__status_transporte, "data_pedido":self.__data_pedido,"servicos":self.__servicos, "endereco":self.__endereco, "data_finalizado":self.__data_finalizado}
    @classmethod
    def from_dict(cls, data):
        
        return cls(
            id=data['id'],
            id_cliente=data['id_cliente'],
            id_pet=data['id_pet'],
            id_funcionario=data['id_funcionario'],
            id_motorista=data['id_motorista'],
            status=data['status'],
            status_transporte=data['status_transporte'],
            data_pedido=data["data_pedido"],
            servicos=data['servicos'],
            endereco=data['endereco'],
            data_finalizado=data['data_finalizado'],
        )