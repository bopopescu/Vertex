class Gafa:
    def __init__(self, fechaCompra, versionSoftware, vidaUtil, horasUsada, serialFabrica, serialInterno, serialOculus, tipoGafa):
        self.__fechaCompra = fechaCompra
        self.__versionSoftware = versionSoftware
        self.__vidaUtil = vidaUtil
        self.__horasUsada = horasUsada
        self.__serialFabrica = serialFabrica
        self.__serialInterno = serialInterno
        self.__serialOculus = serialOculus
        self.__tipoGafa = tipoGafa

        @property
        def fechaCompra(self):
            return self.__fechaCompra

        @fechaCompra.setter
        def fechaCompra(self, fecha):
            self.__fechaCompra = fecha

        @property
        def versionSoftware(self):
            return self.__versionSoftware

        @versionSoftware.setter
        def versionSoftware(self, soft):
            self.__versionSoftware = soft

        @property
        def vidaUtil(self):
            return self.__vidaUtil

        @vidaUtil.setter
        def vidaUtil(self, vida):
            self.__vidaUtil = vida

        @property
        def horasUsada(self):
            return self.__horasUsada

        @horasUsada.setter
        def horasUsada(self, uso):
            self.__horasUsada = uso

        @property
        def serialFabrica(self):
            return self.__serialFabrica

        @serialFabrica.setter
        def serialFabrica(self, fabrica):
            self.__serialFabrica = fabrica

        @property
        def serialInterno(self):
            return self.__serialInterno

        @serialInterno.setter
        def serialInterno(self, interno):
            self.__serialInterno = interno

        @property
        def serialOculus(self):
            return self.__serialOculus

        @serialOculus.setter
        def serialOculus(self, oculus):
            self.__serialOculus = oculus

        @property
        def tipoGafa(self):
            return self.__tipoGafa

        @tipoGafa.setter
        def tipoGafa(self, tipo):
            self.__tipoGafa = tipo