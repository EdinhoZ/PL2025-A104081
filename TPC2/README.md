# TPC 2 - Obras Musicais
### Edgar Alexandre Capela Pinto - A104081
#### 20 de Fevereiro de 2025
![Foto de identificação](../Photo.png "photo")

Este programa está dividido em duas partes:

- O parser do CSV
- O tratamento dos dados do CSV

A parte do parser foi feita iterando por cada linha do csv tendo em atenção campos que estão distríbuidos por várias linhas e criando uma lista de listas. Cada lista da lista principal corresponde a cada peça do CSV.

Depois esse método é chamado pelos outros três métodos que resolvem os 3 problemas propostos com os resultados obtidos na pasta de [outputs](/outputs/).

- Compositores ordernados: [resultado](/outputs/ordered_composers.txt)
- Distribuição por período: [resultado](/outputs/distribution_per_period.txt)
- Títulos em cada período: [resultado](/outputs/titles_per_period.txt)
