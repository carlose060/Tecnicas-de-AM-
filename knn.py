from ponto import Ponto


class KNN():        

    #Contrutor de KNN(), usando os k vizinho como numero impar para evitar conflitos
    def __init__(self,k = 3):
        self.data = []
        self.k = k

    def predicao(self,feature):
        data = [] 
        tipos = []
        featur = Ponto(feature)
        for itens in self.data:
            data.append((Ponto.distancia(featur,itens), itens))
        #Pega todas as distancias e ordenas elas
        data.sort(key=lambda x: x[0])
        for j in data[0:self.k]:
            tipos.append(j[1].tipo)
        tipo = max(tipos, key = tipos.count)
        self.data.append(Ponto(feature,tipo))
        return tipo        

    def score(self,X_test,y_test):
        z = 0
        #Quantidade de teste 
        y_tam = y_test.size
        for i,j in zip(X_test,y_test):
            #Faz a comparação conforme está na lista y_teste
            if self.predicao(i) == j:
                z = z + 1
        #Faz a divisão de todos acertos pela quantitade total de item que foi testado            
        return z/y_tam

    #fit/treino do KNN
    def fit(self,X_train,y_train):
        for feature,rotulo in zip(X_train,y_train):
            #Salva os itens no data
            self.data.append(Ponto(feature,rotulo))    