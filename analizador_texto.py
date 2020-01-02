def cuenta_caracteres(texto, caracter):
  cuenta = 0
  for c in texto:
    if c == caracter:
      cuenta += 1
  return cuenta

nombre_archivo = input("Introduzca nombre de archivo archivo: ")
with open(nombre_archivo) as nombre_archivo:
  texto = nombre_archivo.read()

for caracter in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * cuenta_caracteres(texto, caracter) / len(texto)
  print("{0} - {1}%".format(caracter, round(perc, 2)))

