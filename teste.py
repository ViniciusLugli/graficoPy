import matplotlib.pyplot as plt

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
valor = [5, 13, 2, 18, 29]

plt.plot(produtos, valor, 'k--')
plt.plot(produtos, valor, 'go')
plt.show()