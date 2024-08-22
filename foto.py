from error import DimensionError


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > self.MAX or ancho < 1:
            raise DimensionError('Error en ancho', ancho, self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > self.MAX or alto < 1:
            raise DimensionError('Error en ancho', alto, self.MAX)
        self.__alto = alto


if __name__ == '__main__':
    # Se ingresan los dato de la foto que se creará
    ancho = 1000
    alto = 1000
    ruta = 'www.mifoto.com/mifoto'

    # Se crea una instancia de Foto
    foto_pedro = Foto(ancho, alto, ruta)

    # Moficación
    try:
        # asignamos nuevos valores via setter:
        foto_pedro.ancho = 2000
        foto_pedro.alto = 2000
    except DimensionError as e:
        print('Error en la modificación de datos:')
        print(e)
    else:
        print('Se modificaron las dimensiones de la foto')
    finally:
        print('>>> Programa terminado. FIN <<<<')