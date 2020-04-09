class Cliente:
    def __init__(self, nombres, apellidos, fechaBirthday, correo, celular, rangoEdad, tipoCliente):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fechaBirthday = fechaBirthday
        self.__correo = correo
        self.__celular = celular
        self.__rangoEdad = rangoEdad
        self.__tipoCliente = tipoCliente

        @property
        def nombres(self):
            return self.__nombres

        @nombres.setter
        def nombres(self, name):
            self.__nombres = name

        @property
        def apellidos(self):
            return self.__apellidos

        @apellidos.setter
        def apellidos(self, last):
            self.__apellidos = last

        @property
        def fechaBirthday(self):
            return self.__fechaBirthday

        @fechaBirthday.setter
        def fechaBirthday(self, fecha):
            self.__fechaBirthday = fecha

        @property
        def correo(self):
            return self.__correo

        @correo.setter
        def correo(self, email):
            self.__correo = email

        @property
        def celular(self):
            return self.__celular

        @celular.setter
        def celular(self, cellphone):
            self.__celular = cellphone

        @property
        def rangoEdad(self):
            return self.__rangoEdad

        @rangoEdad.setter
        def rangoEdad(self, edad):
            self.__rangoEdad = edad

        @property
        def tipoCliente(self):
            return self.__tipoCliente

        @tipoCliente.setter
        def tipoCliente(self, tipo):
            self.__tipoCliente = tipo