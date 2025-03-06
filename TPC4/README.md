# TPC 4 - Analisador Léxico de Queries
### Edgar Alexandre Capela Pinto - A104081
#### 06 de Março de 2025
![Foto de identificação](../Photo.png "photo")

Este programa recebe como input uma query e divide a mesma por tokens e distinguíveis pela sua "classe", como ``SELECT`` e ``IDENTIFIER`` que resgatam as operçaões de SELECT na query e identificadores.

Recebendo como input a query:
```
SELECT ?nome ?desc WHERE {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

O programa cria este output: [Resultado](/TPC4/outputs/output.txt)