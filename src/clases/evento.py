class Evento:
    def __init__(self, fecha, hora, duracion, numeroPersonas, eventoCorporativo, lugar, opinion):
        self.__fecha = fecha
        self.__hora = hora
        self.__duracion = duracion
        self.__numeroPersonas = numeroPersonas
        self.__eventoCorporativo = eventoCorporativo
        self.__lugar = lugar
        self.__opinion = opinion

        @property
        def fecha(self):
            return self.__fecha

        @fecha.setter
        def fecha(self, date):
            self.__fecha = date

        @property
        def hora(self):
            return self.__hora

        @hora.setter
        def hora(self, hour):
            self.__hora = hour

        @property
        def duracion(self):
            return self.__duracion

        @duracion.setter
        def duracion(self, dura):
            self.__duracion = dura

        @property
        def numeroPersonas(self):
            return self.__numeroPersonas

        @numeroPersonas.setter
        def numeroPersonas(self, numero):
            self.__numeroPersonas = numero

        @property
        def eventoCorporativo(self):
            return self.__eventoCorporativo

        @eventoCorporativo.setter
        def eventoCorporativo(self, corp):
            self.__eventoCorporativo = corp

        @property
        def lugar(self):
            return self.__lugar

        @lugar.setter
        def lugar(self, place):
            self.__lugar = place

        @property
        def opinion(self):
            return self.__opinion

        @opinion.setter
        def opinion(self, op):
            self.__opinion = op