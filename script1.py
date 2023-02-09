import os

#utilizando o caminho relativo:
arquivo1 = open("documentos\dados2.txt")

print(os.path.abspath(arquivo1.name)) #imprime o caminho absoluto
print(os.path.relpath(arquivo1.name)) #imprime o caminho relativo

print(arquivo1)
#<_io.TextIOWrapper name='documentos\\dados2.txt' mode='r' encoding='cp1252'>
#Desmembrando essa saída, temos: o tipo do objeto: TextIOWrapper, que trata de arquivos de texto; 
# o nome do arquivo, name='dados.txt'; 
# o modo de acesso ao arquivo, mode='r'; 
# e a codificação do arquivo, encoding='cp1252'.