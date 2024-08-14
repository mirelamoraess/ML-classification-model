# Importando a biblioteca necessária
from sklearn.tree import DecisionTreeClassifier

# Dados de treinamento
# Características: [Envergadura das asas, Peso, Comprimento do bico]
X_train = [
   [120, 3.5, 7],  # Ave 1: Carnívora
   [85, 1.2, 4],   # Ave 2: Herbívora
   [95, 2.1, 6]    # Ave 3: Onívora
]

# Classes correspondentes
y_train = ['Ave Carnívora', 'Ave Herbívora', 'Ave Onívora']


# Criação do modelo de Árvore de Decisão
modelo = DecisionTreeClassifier()

# Treinamento do modelo
modelo.fit(X_train, y_train)

# Dados de teste (nova ave)
X_test = [[90, 1.5, 5]]

# Classificação da ave de teste
resultado = modelo.predict(X_test)

# Exibição da categoria atribuída à ave teste
print(f"A categoria atribuída à ave teste é: {resultado[0]}")