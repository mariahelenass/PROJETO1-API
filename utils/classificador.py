import nltk 
nltk.download('punkt')
nltk.download('mac_morpho')
from nltk.corpus import mac_morpho
from nltk.tag  import UnigramTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

try:
    class classificador_palavras():
        def classificador(self, algo):
            #opcao = True
            #while opcao:
                frase = algo
                print(f"\nSua frase: {frase}")
                tokens = nltk.word_tokenize(frase) # tokenizando palavras 
                x = len(tokens) 
                tokens_sent = nltk.sent_tokenize(frase) # tokenizando sentenças
                x2 = len(tokens_sent)
                freq = nltk.FreqDist(tokens) # frequencias das palavras 
                comuns = freq.most_common(5) # palavras mais comuns 
                print("\nSeu texto está sendo classificado...")
                # etiquetando
                treino = mac_morpho.tagged_sents() 
                etiqt = UnigramTagger(treino)
                etiq = etiqt.tag(tokens) 
                print(f"\n Quantidade de palavras presentes no seu texto: {x}")
                print(f"\nQuantidade de sentenças presentes no seu texto: {x2}")
                print(f"\nFrequência de cada palavra: {freq}")
                print(f"\nPalavras mais comuns no seu texto: {comuns}")
                print(f"\nClassificando as palavras do seu texto: {etiq}")

                # opcao = input("\nDeseja fazer outra classificação (y/n) ? : ").strip().lower()
                
                # if opcao == "y":
                #     continue
                # else:
                #     print("\nObrigado!")
                #     opcao = False
                return etiq

except Exception as error:
        print(error)

        
   









