# Seta o volume atual de um reservatorio de agua (em metros cubicos)
reservoir_volume = 4.445e8
# Seta a quantidade de chuvas de uma tempestade (precipitacao em metros cubicos)
rainfall = 5e6

# Agora diminuia a variavel rainfall em 10% para explicar o escoamento
rainfall *= 0.9
# Adicione a variavel rainfall a variavel reservory_volume (some uma com a outra)
rainfall += reservoir_volume

# Aumente reservoir_volume em 5% para explicar as aguas pluviais que fluem
# no reservatorio nos dias posteriores a tempestade
reservoir_volume *= 1.05

# Diminua reservoir_volume em 5% para explicar a evaporacao
reservoir_volume *= 0.95

# Subtraia 2.5e5 metros cubicos do reservoir_volume para explicar a agua
# que e encaminhado para regioes aridas.
reservoir_volume -= 2.5e5

# Imprima o novo valor da variavel reservoir_volume
print(reservoir_volume)

print("Resposta: " + str(443138750.0))
