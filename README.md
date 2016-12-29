# multi-btc-address-create
Creación de direcciones bitcoin y comprobar su saldo y total recibido en entorno gráfico.

Programa creado en Python 3.4, de uso libre.

Para la creación de direcciones bitcoin tenenos 2 opciones:

1) Entrar una palabra o frase de la longitud que queramos(Cuanto más larga sea, más segura será la dirección creada)

2) Crear una dirección de forma aleatoria (Mucho cuidado con esta opción ya que la aleatoriedad del sistema puede no siempre ser correcta).

El sistema crea la clave PRIVADA, y la clave WIF (Para importar en nuestra billetera) junto con la dirección bitcoin asociada a ellas.
Una vez creada la dirección, o poniendo nosotros mismos una dirección válida en el campo ADDR, podemos saber su saldo actual y el saldo acumulado de dicha dirección.

Para que funcione correctamente el programa se necesitan las librerias tkinter y bitcoin.

Agradecimientos a la estupenda libreria creada por vbuterin:

https://github.com/vbuterin/pybitcointools

NOTA:
Este programa es para uso y experimentación... El creador no se hace responsable de la pérdida de bitcoins depositados en las direcciones creadas con dicho programa.
