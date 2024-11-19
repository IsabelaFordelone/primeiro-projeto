minhaTupla = (19, "Isabela", 3.14, True, "Livros")

print(minhaTupla)
print(type(minhaTupla))

minhaLista = list(minhaTupla)

print(minhaLista)
print(type(minhaLista))

minhaLista.append("Mais Livros")
print(minhaLista)

minhaLista.pop(0)
minhaLista.pop()
print(minhaLista)

print(minhaLista[0])

if len(minhaLista) > 1:
    print(f"A quantidade de dados são {len(minhaLista)} e os dados são: {minhaLista}")
else:
    print(f"A quantidade de dado é {len(minhaLista)} e o dado é: {minhaLista}")

dicionario1 = {
    'nome': 'Isabela',
    'idade': 19,
    'profissao': 'Tristeza'
}

for valor in dicionario1.values():
    print(valor)