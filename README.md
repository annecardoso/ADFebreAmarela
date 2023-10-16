# Repositório da Avaliação A1 - Linguagens de Programação

## Descrição

Bem-vindo ao nosso repositório da Avaliação A1 da disciplina de Linguagens de Programação! Este repositório contém o código-fonte e análise de dados relacionados à ocorrência de febre amarela no Brasil. Nossa equipe é composta por Anne, Beatriz e Murilo.
## Objetivo

O objetivo principal deste projeto é analisar os dados relacionados à febre amarela no Brasil, fornecendo insights valiosos sobre sua incidência, distribuição geográfica e tendências ao longo do tempo. Nosso projeto envolve a coleta, limpeza e visualização de dados para uma melhor compreensão da situação da febre amarela no país.

## Conteúdo

O repositório contém os seguintes elementos:

1. **Códigos-Fonte**: Nossos códigos-fonte estão organizados de forma clara e compreensível. Você encontrará scripts Python que abordam a coleta e processamento de dados, análise estatística e visualização. Cada membro da equipe contribuiu de maneira significativa para o desenvolvimento desses códigos.

2. **Conjunto de Dados**: Incluímos o conjunto de dados que utilizamos em nosso projeto. Os dados são provenientes de fontes confiáveis (https://dados.gov.br/dados/conjuntos-dados/febre-amarela-em-humanos-e-primatas-no-humanos---1994-a-2021, https://censo2022.ibge.gov.br/panorama/ e https://github.com/giuliano-oliveira/geodata-br-states/tree/main) e foram tratados para garantir sua qualidade e integridade.

3. **Documentação**: Sphinx

4. **Resultados e Visualizações**: Apresentamos visualizações gráficas atraentes e resultados de análises de dados para fornecer uma visão completa da febre amarela no Brasil.

## Equipe

- **Anne Beatriz Cardoso de Sousa**: Responsável pela filtragem e análise da 
- **Beatriz Miranda Bezerra**: Encarregada da análise da distribuição por unidade federativa de infecções e óbitos.
- **Gustavo Murilo Cavalcante Carvalho**: Encarregado da análise da distribuição mensal, anual e variação da letalidade ao longo dos anos.
  
## Resultados e visualização

1. Neste gráfico é possível observar a maior ocorrência de febre amarela nos estados que compõem a região sudeste. Porém, uma das causas relacionadas a isso pode ser a quantidade populacional que é maior nesses estados.

![Infecções por Unidade Federativa](./img/infec_uf.png)

2. Para os óbitos registrados, o cenário é semelhante ao gráfico anterior.

![Óbitos por Unidade Federativa](./img/obitos_uf.png)

3. Entretanto, quando analisamos de forma relativa, levando em consideração os dados populacionais de cada Estado de acordo com o censo do IBGE de 2010, observamos um maior destaque de incidência para o Espírito Santo. Além disso, observamos Roraima ficando em maior evidência do que nas análises anteriores. 

![Infecções (relativa) por Unidade Federativa](./img/infec_rel_uf.png)

4. Em relação aos óbitos a cada cem mil habitantes do respectivo estado, percebemos as regiões Norte e Centro-Oeste ganhando um pouco mais de destaque, enquanto Roraima se destaca ainda mais.

![Óbitos (relativo) por Unidade Federativa](./img/obitos_rel_uf.png)

5. Nesta plotagem vemos a doença esteve sobre controle na maior parte do tempo, mas não completamente, pois na metade da última década houve um pico de infecções e mortes, correspondente à epidemia de febre amarela que ocorreu entre 2017 e 2019.

![Ocorrências de Infectados e óbitos por ano](./img/infec_e_obitos_ano.png)

6. O clima quente é favorável à reprodução dos mosquitos, os vetores da doença. Assim, a relação presente no gráfico faz muito sentido, pois é os meses com maior número de infeções, fazem parte do verão, o período mais quente do ano. 

![Ocorrências de Infectados e óbitos por mês](./img/infec_e_obitos_mes.png)

7. A variação da letalidade da doença ao longo dos anos não possui nenhuma tendência. Ainda assim, podemos ver que os anos com muitos infectados, ou seja, nos quais há uma amostra significativa, os pontos estão na mesma faixa. Tomando esse ponto como norma, temos que a letalidade está por volta de 35%

![Variação da letalidade da febre amarela](./img/variacao_letalidade.png)
etalidade da febre amarela](./img/variacao_letalidade.png)
