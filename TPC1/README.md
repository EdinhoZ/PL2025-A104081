# TPC 1 - Somador
### Edgar Alexandre Capela Pinto - A104081
#### 12 de Fevereiro de 2025
![Foto de identificação](../Photo.png "photo")

Este [programa](somador.py) calcula a soma de todos os dígitos presentes numa string. Para tal a função somar itera pela linha caracter a caracter e verifica se é um digito, uma letra ou se esse caracter e os 2/3 seguintes representam as expressões On/Off respetivamente. Como estas expressões podem ser representadas com maiscúlas e mínusculas, fiz uso do método ```lower``` para ser mais fácil a comparação.

Se o caracter for um digito ele guarda esse digito num buffer para depois quando o próximo caracter não for um dígito ele adicionar os dígitos no buffer à soma que será visível quando o programa encontrar o caracter ```=```.

