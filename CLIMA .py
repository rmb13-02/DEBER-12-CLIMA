import numpy as np

num_ciudades = 5
num_dias_semana = 7
num_semanas = 4

# DATOS
temperaturas = np.random.randint(5, 35, size=(num_ciudades, num_dias_semana, num_semanas))

# CALCULAR EL PROMEDIO
def promedio_semanal_ciudad(ciudad):
  promedios = np.mean(temperaturas[ciudad], axis=1)
  return promedios

# PROMEDIO DE CADA CIUDAD
for ciudad in range(num_ciudades):
  promedios_ciudad = promedio_semanal_ciudad(ciudad)
  print(f"Ciudad {ciudad+1}:")
  for semana in range(num_semanas):
    print(f"  Semana {semana+1}: {promedios_ciudad[semana]:.2f}°C")