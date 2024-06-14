import numpy as np

# Define uma semente para garantir a reprodutibilidade dos resultados
np.random.seed(42)

# Gera um array 'a' com 5 números aleatórios uniformemente distribuídos entre 0 e 1
a = np.random.uniform(0, 1, 5)

# Reinicia a semente com o mesmo valor para 'b'
np.random.seed(42)

# Gera um array 'b' com 5 números aleatórios uniformemente distribuídos entre 0 e 1
b = np.random.uniform(0, 1, 5)

# Agora, reinicia a semente novamente para 'a', mas altera para 'b'
np.random.seed(42)

# Gera um array 'a' com 5 números aleatórios uniformemente distribuídos entre 0 e 5
a = np.random.uniform(0, 5, 5)

# Reinicia a semente com um novo valor para 'b'
np.random.seed(8)

# Gera um array 'b' com 5 números aleatórios uniformemente distribuídos entre 0 e 5
b = np.random.uniform(0, 5, 5)

# Imprime os arrays 'a' e 'b' para visualização
print(a)
print(b)
