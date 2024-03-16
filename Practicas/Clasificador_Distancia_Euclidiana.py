# Importamos las bibliotecas necesarias
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Generamos un conjunto de datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=2, n_classes=2, n_clusters_per_class=1, n_redundant=0, random_state=42)

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Imprimimos los conjuntos de entrenamiento y prueba para verificación
print("Conjunto de entrenamiento (X_train):", X_train.shape)
print("Conjunto de prueba (X_test):", X_test.shape)
print("Etiquetas de entrenamiento (y_train):", y_train.shape)
print("Etiquetas de prueba (y_test):", y_test.shape)

# Implementamos la función de distancia euclidiana
def euclidian_distance(point1, point2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Implementamos la función de clasificación por distancia euclidiana
def euclidean_classifier(train_data, train_labels, test_point):
    """Clasifica un punto de prueba basándose en el vecino más cercano del conjunto de entrenamiento."""
    distances = [euclidian_distance(train_point, test_point) for train_point in train_data]
    nearest_neighbor_index = np.argmin(distances)
    return train_labels[nearest_neighbor_index]

# Clasificamos el conjunto de prueba y evaluamos la precisión
predictions = [euclidean_classifier(X_train, y_train, test_point) for test_point in X_test]
accuracy = accuracy_score(y_test, predictions)
print(f"Precision del clasificador: {accuracy * 100:.2f}%")
