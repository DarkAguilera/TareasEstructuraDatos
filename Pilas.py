pila = []

pila.append("Libro 1")
pila.append("Libro 4")
pila.append("Libro 2")

print("Pila después de apilar:")
print(pila)

print("\nElemento en el tope de la pila:", pila[-1])

ultimo = pila.pop()
print("\nElemento desapilado:", ultimo)

print("Pila actual después de desapilar:")
print(pila)
