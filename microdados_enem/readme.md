## Microdados Enem

Desafio baseado no [teste-engenheiro-de-dados](https://github.com/meshatech/teste-engenheiro-de-dados).

O desafio se resume em:

* Fazer o ETL dos dados, modelagem dimensional dos dados e levantar alguns indicadores.

### Sumário

1. [Objetivos](#objetivos)
2. [Resumo](#resumo)
3. [Execução](#execução)


### Objetivos

Foi disponibilizado um arquivo ``.csv`` com microdados do enem de 2020. A fonte original dos dados pode ser encontrada [aqui](https://download.inep.gov.br/microdados/microdados_enem_2020.zip).

Deve ser feita a modelagem utilizando o ``esquema estrela`` e responder os seguintes indicadores:

1. Qual a escola com a maior média de notas?
2. Qual o aluno com a maior média de notas e o valor dessa média?
3. Qual a média geral?
4. Qual o % de Ausentes?
5. Qual o número total de Inscritos?
6. Qual a média por disciplina?
7. Qual a média por Sexo?
8. Qual a média por Etnia?

### Resumo

Tecnologias utilizadas:
* Pyspark
* Jupyter Notebook

### Execução
* ``microdados_enem.ipynb`` contem todo o código e os indicadores respondidos 

