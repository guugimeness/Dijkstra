# Dijkstra's Algorithm

O problema dos caminhos mínimos em grafos é um dos problemas clássicos da teoria dos grafos e consiste em encontrar o caminho de menor custo ou menor distância entre dois vértices de um grafo ponderado. Cada aresta do grafo possui um peso que pode representar a distância, o custo, o tempo ou qualquer outra medida associada ao trajeto entre dois vértices. O objetivo é determinar o caminho que minimiza a soma dos pesos ao viajar de um vértice de origem para um vértice de destino.

O Algoritmo de Dijkstra é uma solução eficiente para o problema dos caminhos mínimos em grafos com pesos não negativos. Ele foi desenvolvido por Edsger W. Dijkstra em 1956 e é amplamente utilizado em diversas aplicações, como redes de computadores, sistemas de navegação e planejamento de rotas.

Esse algoritmo trabalha da seguinte maneira:
- Para o vértice atual, examinamos todos os seus vizinhos não visitados.
- Para cada vizinho, calculamos a distância total da origem até ele passando pelo vértice atual.
- Se a distância calculada for menor do que a distância registrada atualmente para esse vizinho, atualizamos a distância.
- Após avaliar todos os vizinhos do vértice atual, marcamos o vértice atual como visitado e o removemos do conjunto de não visitados.

### Execução

Neste projeto, a ideia era implementar o grafo proposto:
<p align="center">
  <img src="https://github.com/guugimeness/Dijkstra/blob/e58ac58fd08e0f13dfd2495accfcea8ccac16ff1/assets/graph.png" alt="Image">
</p>
e aplicar o algoritmo de Dijkstra nele, obtendo a árvore de caminhos mínimos:
<p align="center">
  <img src="https://github.com/guugimeness/Dijkstra/blob/e58ac58fd08e0f13dfd2495accfcea8ccac16ff1/assets/tree.png" alt="Image">
</p>
Para isso, foram utilizadas as bibliotecas NetworkX e Matplotlib.

##  Status: Finalizado
