from sklearn.datasets import load_iris,load_wine,load_digits,load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from knn import KNN


def Treinar(database,database_name):
    print(f"\n------------------Base de dados {database_name}----------------------")

    #Separa em x as feature e y os rotulos
    X, y = database(return_X_y=True)

    #Dividir em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    #Treinamento dos modelos
    def train(model,name):
        print(f'Algoritmo: {name}')
        model.fit(X_train,y_train)
        print(model.score(X_test,y_test), end='\n\n')

    #Chama-se a função para cada algoritmo
    train(SVC(),"SVC")
    train(DecisionTreeClassifier(),"DecisionTreeClassifier")
    train(GaussianNB(),"GaussianNB")
    train(KNN(),"KNN")
    
if __name__ == '__main__':

    #Carrega as base de dados para rodar os algoritmos
    Treinar(load_iris,"Iris")
    Treinar(load_wine,"Wine")
    Treinar(load_breast_cancer,"Breast Cancer")
    Treinar(load_digits,"Digits")
