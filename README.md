# jogodavelha
Este projeto corresponde a uma api para um jogo multiplayer de Jogo da Velha, desenvolvido utilizando-se a linguagem Python juntamente com o framework Flask. O código para o projeto foi implementado utilizando-se o paradigma orientado a objetos. 

### Descrição

A classe ```Game``` foi criada com o intuito de representar as partidas. Nela guardamos todas as informações necessárias para que o jogo aconteça. Uma partida precisa ter um tabuleiro que a representa, além de armazenar um código único para si mesma, o primeiro jogador a fazer um movimento, o jogador do turno atual e, por último, um vencedor. ```Game``` é responsável por verificar o jogador que deve fazer o movimento no turno atual e realizar as mudanças de turnos.

Para representar os tabuleiros de cada partida, a classe ```Board``` foi implementada. Um ```Board``` precisa ter uma dimensão e uma matriz, de tal dimensão, que o representa. Em uma determinada partida, ```Board``` fica com a responsabilidade de realizar um movimento para um jogador e verificar se existem vencedores/empate nesse instante de tempo. 

Cada posição na matriz de um tabuleiro é representada pela classe ```Position``` que guarda as coordenadas da posição e o símbolo do jogador que a dominou. Essa classe é responsável apenas por atribuir o símbolo do jogador na posição correspondente. 

A persistência dos dados foi feita in-memory através de uma classe chamada ```GameHistory``` representando o histórico de partidas. ```GameHistory``` possui uma lista de partidas que foram criadas (sejam elas partidas finalizadas ou em andamento). Suas responsabilidades dizem respeito a adição de novas partidas na lista de games e ao retorno da partida solicitada. 

O sistema suporta que todas as partidas estejam acontecendo juntas, basta apenas mudar o ```id``` do jogo desejado. Se uma partida já tiver sido finalizada, ela sempre retornará o seu resultado quando chamada. Se ainda não tiver sido finalizada, ela permanece no turno de um determinado jogador até que ele faça seu movimento.

### Boas práticas 

Falando sobre boas práticas de desenvolvimento de software, este projeto busca respeitar grande parte dos padrões de projetos. O padrão MVC foi seguido de forma bem simples com cada módulo contendo models, controllers e routes. Cada classe e cada método foi desenvolvido de forma a possuir responsabilidades únicas. A nomenclatura de variáveis, classes e métodos foi padronizada para facilitar a legibilidade do código. Além disso, pensando na manutenibilidade e na possível expansão do sistema para futuras funcionalidades, os métodos e classes foram desenvolvidos de forma a serem os mais genéricos possíveis. Cabe mencionar que este projeto foi desenvolvido para ser expansível à tabuleiros maiores e mudança de jogadores. Por isso, contantes foram criadas a fim de poderem ser modificadas.

Finalizando o tópico de boas práticas, o projeto contém um módulo de testes de integração automatizados. Os testes desenvolvidos verificam os seguintes resultados: fazer um único movimento; realizar sequência de movimentos que resultam em uma vitória por linha, coluna e diagonais; realizar sequência de movimentos que resultam em "velha"; erro ao tentar jogar em um turno que não é seu; e por fim, erro ao tentar entrar em uma partida inexistente.

Um arquivo para workflows foi criado com o intuito integrar o código "commitado" e "buildar" o sistema automaticamente para verificar possíveis problemas. Um job para rodar os testes automatizados desenvolvidos também foi criado.

### Instruções de build

Para "buildar" o sistema, precisamos instalar as dependências

```
  python -m pip install --upgrade pip
  pip install -r requirements.txt
```

Para executar o sistema usamos ```python app.py``` e para rodar os testes automatizados usamos ```pytest tests.py```.

### Dependências

As dependências requeridas estão em ```requirements.txt```, arquivo onde encontra-se dependências inclusas no flask e flask-pytest.

### Melhorias

Com mais tempo de desenvolvimento, algumas melhorias poderiam ser aplicadas para garantir maior qualidade de código. Dentre as possíveis melhorias, temos: 
- extração das validações e checagens da rota ```movement``` para métodos separados; 
- separação dos módulos em "blueprints"; 
- melhoria nos testes automatizados com a inserção de testes de unidade; 
- mudança na lógica do método ```checkWinner``` e dos métodos chamados por ele, de forma a diminuir as condições e retornos redundantes e generalizar os métodos para possíveis expansões (para tabuleiros maiores, por exemplo);
- sobrecarga de operadores para indexar a matriz do tabuleiro de forma a tratar os índices como posições cartesianas ```xy```.
