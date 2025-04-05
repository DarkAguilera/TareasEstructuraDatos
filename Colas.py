from collections import deque

cola = deque()

cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")

print("Cola después de encolar:")
print(list(cola))

print("\nPrimer cliente en la cola:", cola[0])

atendido = cola.popleft()
print("\nCliente atendido:", atendido)

print("Cola actual después de atender:")
print(list(cola))
