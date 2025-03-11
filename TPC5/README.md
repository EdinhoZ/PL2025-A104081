# TPC 5 - Máquina de Vendas
### Edgar Alexandre Capela Pinto - A104081
#### 11 de Março de 2025
![Foto de identificação](../Photo.png "photo")

Tal como pedido no enunciado, este programa recria o funcionamento de uma máquina de vendas recebendo o stock do ficheiro [`stock.json`](/TPC5/stock.json) e permite ao utilizador executar operações relacionados com a máquina.

Essas operações são as seguintes:

- `LISTAR`: Permite ao utilizador saber quais os produtos que estão na máquina, a quantidade e o preço por unidade.
- `MOEDA`: Ao inserir este comando seguido de um montante válido (todas as moedas existentes do Euro), este é acrescentado ao saldo do utilizador que pode depois ser utilizado para comprar algum produto.
- `SELECIONAR`: Este comando, acompanhado de um código de produto válido, permite ao utilizador comprar esse produto se este tiver o saldo suficiente.
- `SAIR`: Fecha o programa e guarda o stock atual no ficheiro JSON.

Estas operações são consideradas tokens que o programa passa por um analisador léxico e decide qual a ação a tomar.
Tal como as operações, os códigos dos produtos também são tokens pois é necessário o analisador léxico verificar se o código introduzido pelo utilizador é válido.