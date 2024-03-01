from os import system
from sklearn import datasets
import matplotlib.pyplot as plt #Importación para la gráfica de dispersión
from sklearn.decomposition import PCA #Importación para la representacion PCA

'''
Definimos una clase llamada Practica que encapsulara toda la funcionalidad relacionada con
la carga, manejo y visualización de los conjuntos de datos.'''
class Practica:
    def __init__(self): # Inicializador
        self.dataset = None
    
    #Cargamos los datos dependiendo del nombre proporcionado
    def load_dataset(self, nombre):
        if nombre == 'cancer':
            self.dataset = datasets.load_breast_cancer()
        elif nombre == 'iris':
            self.dataset = datasets.load_iris()
        elif nombre == 'diabetes':
            self.dataset = datasets.load_diabetes()
        elif nombre == 'vino':
            self.dataset = datasets.load_wine()
        else:
            print("Nombre de dataset no reconocido.")
            return
    
    #Imprimimos la información o visualización (Gráficas)
    def print_dataset_info(self, opd):
        if self.dataset is not None:
            if opd == '1':
                print(self.dataset)
            elif opd == '2':
                print(self.dataset.keys())
            elif opd == '3':
                print(self.dataset.DESCR)
            elif opd == '4':
                self.plot_dataset()
            elif opd == '5':
                self.plot_pca_representation()
        else:
            print("No hay un dataset cargado.")
            
    #Generamos una gráfica de dispersión.
    def plot_dataset(self):
        if hasattr(self.dataset, 'feature_names') and hasattr(self.dataset, 'target_names') and self.dataset.data.shape[1] >= 2:
            X = self.dataset.data
            y = self.dataset.target
            feature_names = self.dataset.feature_names
            target_names = self.dataset.target_names
            
            # Define colores para las clases (por lo solicitado en la grafica de Iris)
            colors = ['red' if target == 0 else 'blue' if target == 1 else 'yellow' for target in y]
            
            plt.figure(figsize=(10, 6))
            for target, color in zip(range(len(target_names)), ['red', 'blue', 'yellow']):
                plt.scatter(X[y == target, 0], X[y == target, 1], c=color, label=target_names[target])
            
            plt.xlabel(feature_names[0] + ' (cm)')
            plt.ylabel(feature_names[1] + ' (cm)')
            plt.title(f'Scatter plot for {feature_names[0]} vs {feature_names[1]}')
            
            plt.legend(loc="lower right", title="Classes")
            plt.show()
        else:
            print("El dataset no es adecuado para un gráfico de dispersión. ")
    
    #Generamos la representacián tridimensional de los datos utilizando PCA
    def plot_pca_representation(self):
        if hasattr(self.dataset, 'data') and self.dataset.data.shape[1] >= 3:
            X_reduced = PCA(n_components=3).fit_transform(self.dataset.data)
            fig = plt.figure(1, figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d', elev=-150, azim=110)
            ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=self.dataset.target, s=40)
            ax.set_title("First three PCA dimensions")
            ax.set_xlabel("1st Eigenvector")
            ax.set_ylabel("2nd Eigenvector")
            ax.set_zlabel("3rd Eigenvector")
            plt.show()
        else:
            print("Se necesitan al menos 3 dimensiones para la representación PCA.")


#Menú Principal
menu = '''
        Análisis de conjuntos de datos.
1] Cáncer de seno.
2] Iris.
3] Diabetes.
4] Vino.
5] Salir.
'''

#Menú para las opciones de los Datasets
opcionesDatasets = '''
                Seleccione una opción:
1] Imprimir Dataset completo.
2] Imprimir Keys (Información en el conjunto de entrada).
3] Imprimir DESCR (Descripción total del conjunto).
4] Obtener gráficas.
5] Representación PCA.
6] Salir.
'''


if __name__ == "__main__":
    p = Practica()
    op = '1'
    #Bucle principal para seleccionar el dataset con el que se trabajará
    while op != '5':
        system('cls')
        print(menu)
        op = input("Seleccione la opción deseada menú = ")
        if op in ['1', '2', '3', '4']:
            dataset_names = ['cancer', 'iris', 'diabetes', 'vino']
            p.load_dataset(dataset_names[int(op)-1])
            opd = '1'
            while opd != '6':
                system('cls')
                print(opcionesDatasets)
                opd = input("Seleccione la opción deseada datasets = ")
                if opd != '6':
                    p.print_dataset_info(opd)
                    input("Presione cualquier tecla para continuar...")
        elif op == '5':
            print("Fin del programa . . . ")
        else:
            print("Opción no válida.")
            input("Presione cualquier tecla para continuar...")
