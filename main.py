from clases.rectangulo import rectangulo
from clases.circulo import circulo      
from clases.cuadrado import cuadrado
from clases.elipse import elipse



if __name__ == "__main__":
    R1= rectangulo(5,10,'rojo')
    C1= circulo('azul',7)
    CU1= cuadrado(4,'verde')
    E1= elipse(6,3,'amarillo')
    print(R1)
    print(C1)      
    print(CU1)
    print(E1)