import time

tempoantigo = time.time()

tempolocal = time.localtime(tempoantigo)

horas = tempolocal.tm_hour
minutos = tempolocal.tm_min
segundos = tempolocal.tm_sec

diferencadetempo = tempoantigo // (24 * 3600)

print(f"Hora atual: {horas:02d}:{minutos:02d}:{segundos:02d}")
print(f"Número de dias desde a época: {int(diferencadetempo)}")