# Importa toda a biblioteca de matemática
import math
# A biblioteca math esta chamando a ferramenta factorial para calcular o fatorial de um parâmetro.
calc = math.factorial(2)
print(calc)


# Importa somente a função fatorial da biblioteca math
from math import factorial, sqrt
import datetime
calc2 = factorial(10)
raiz = sqrt(25)
print(calc2,raiz)


data_hora = datetime.date.today()
print(data_hora)