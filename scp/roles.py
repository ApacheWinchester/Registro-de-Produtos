from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {'criar_usuario': True, 'remover_usuario':True, 'editar_usuario':True, 'adicionar_db':True, 'editar_db':True, 'remover_db':True, 'visualizar_db':True}



class Intermediario(AbstractUserRole):
    available_permissions = {'editar_usuario':True, 'criar_usuario': True, 'editar_db':True, 'remover_db':True,'adicionar_db':True, 'visualizar_db':True}




class Padrao(AbstractUserRole):
    available_permissions = {'adicionar_db':True, 'visualizar_db':True}


