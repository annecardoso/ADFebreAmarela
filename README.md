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

5. Deste gráfico é possível concluir que houve um surto de febre amarela no Brasil por volta de 2017. De fato, obtemos essa confirmação ao pesquisar sobre o assunto: https://pt.wikipedia.org/wiki/Surto_de_febre_amarela_no_Brasil_em_2016-2017

![Ocorrências de Infectados e óbitos por ano](./img/infec_e_obitos_ano.png)

6. Deste gráfico podemos extrair que há maiores notificações nos meses em que o verão acontece no Brasil.

![Ocorrências de Infectados e óbitos por mês](./img/infec_e_obitos_mes.png)

7. Deste gráfico é possível supor que a letalidade da doença esteja entre 0 e 1%. Além disso, nos últimos anos a taxa esteve por volta de 0.5%, talvez haja influência do aumento da taxa de vacinação.

![Variação da letalidade da febre amarela](./img/variacao_letalidade.png)
