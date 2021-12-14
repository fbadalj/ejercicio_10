import stats_data as s_d

lista = []
while True:
    numero = input("Introduce numero: ")
    if numero == "fin":
        break
    numero = float(numero)
    lista.append(numero)
calculo_stats = s_d.StatsData(lista)

print("Lista de numeros: ", calculo_stats.l_data)
print("Media: ", calculo_stats.mean)
print("Mediana: ", calculo_stats.median)
print("Varianza: ", calculo_stats.variance)