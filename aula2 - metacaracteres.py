# Metacaracteres: . ^ $ * + ? { } [ ] \ | ( )
# . = Qualquer caracteres(com excessão da quebra de linha)
# | = ou
# [] = conjunto de caracteres

import re

texto = '''

Alice e o Tempo

O Tempo: -Sim?
Alice: -Eu sei que você tentou me avisar e eu não escutei, me desculpe. Eu pensava que o tempo era um ladrão, 
        que roubava tudo que eu amava, mas agora eu vejo que você dá antes de tomar e cada dia um presente, 
        a cada hora, a cada minuto, a cada segundo.
O Tempo: -Ah o soldado caído, você quer que eu o concerte?
Alice: -Não, eu quero que fique com ele, ele dizia que a única coisa que valia a pena era o que fazíamos pelos outros, 
        ele teria gostado de você...
O Tempo: -Huum... Mas dizem que o tempo não é amigo de ninguém, mas eu lembrarei de você sempre e por favor não volte mais.

Alice Através Do Espelho -  Charles Lutwidge Dogson (Lewis Carroll)
'''

print(re.findall(r'Tempo|Alice|Charles', texto))
print(re.findall(r'[Tt]empo|Alice', texto)) # para buscar a mesma palavra entre maiusculas e minusculas
print(re.findall(r'[a-zA-Z]ice', texto))# usando range de a - z tanto maiusculo como minusculo
print(re.findall(r'Tempo', texto, flags=re.I)) # flag para ignorar maiuscula e minusculas (tras todas)
