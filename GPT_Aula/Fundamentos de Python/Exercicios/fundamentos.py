# Escreva um programa em Python que:

# Peça ao usuário para digitar o nome e a idade.
# Verifique se a pessoa é maior de idade (18 anos ou mais).
# Imprima uma mensagem apropriada com base na idade.
name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 18:
    print(f"{name}, você já é de maior!")
else:
    print(f"{name}, você ainda é de menor!")
    
# Exercício 2: Lista de Denúncias
# Imagine que você está criando uma funcionalidade para registrar denúncias. Vamos criar um programa que:

# Permita ao usuário registrar várias denúncias.
# Armazene essas denúncias em uma lista.
# Permita ao usuário visualizar todas as denúncias registradas.
from datetime import datetime
import pytz

fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
report = []

while True:
    newReport = input("Nova denúncia ou 'sair' para terminar: ")
    if newReport.lower() == 'sair':
        break
    timestamp_brasilia = datetime.now(fuso_horario_brasilia).strftime("%d-%m-%Y %H:%M:%S")
    report.append({"denuncia": newReport, "timestamp": timestamp_brasilia})

print("\nDenúncias registradas:")
for i, entry in enumerate(report, 1):
    print(f"{i}. {entry['denuncia']} (registrada em: {entry['timestamp']})")