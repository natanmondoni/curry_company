# curry_company

# 1.Problema de negócio
    
    
A Curry Company visa conectar restaurantes, entregadores e pessoas com o objetivo de proporcionar satisfação a todos os envolvidos.
    
Para ajudar a Cury Company a obter uma visão completa de seus KPIs, podemos criar um painel abrangente que rastreia as principais métricas, como tempo de entrega, precisão do pedido, satisfação do cliente e desempenho do motorista de entrega. Para que o CEO possa construir algumas ideias simples nas suas tomadas de decisões. 
    
Ao consolidar essas informações em um só lugar, a empresa pode identificar facilmente áreas que precisam de melhorias e tomar decisões baseadas em dados que impactam positivamente seus negócios.
    
A Cury Company possui um modelo de negócio chamado Marketplace, que faz o intermédio do negócio entre três clientes principais: restaurantes, entregadores e compradores. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:
    
## Do lado da empresa:
  1. Quantidade de pedidos por dia.
  2. Quantidade de pedidos por semana.
  3. Distribuição de pedidos por tipo de tráfego.
  4. Comparação do volume de pedidos por cidade e tipo de tráfego.
  5. A quantidade de pedidos por entregador por semana.
  6. A localização central de cada cidade por tipo de tráfego.
    
## Do lado do entregador:
    
  1. A menor e maior idade dos entregadores.
  2. A pior e a melhor condição de veículos.
  3. A avaliação média por entregador.
  4. A avaliação média e o desvio padrão por tipo de tráfego.
  5. A avaliação média e o desvio padrão por condições climáticas.
  6. Os 10  entregadores mais rápidos por cidade.
  7. Os 10 entregadores mais lentos por cidade.
    
## Do lado do restaurantes:
    
  1. A quantidade de restaurantes unidos.
  2. A distancia média dos restaurantes e dos locais de entrega.
  3. O tempo médio e o desvio padrão de entrega por cidade.
  4. O tempo médio e o desvio padrão de entrega por cidade e tipo de pedido.
  5. O tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego.
  6. O tempo médio de entrega durante os Festivais. 
    
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.
    
    
# 2.Premissas assumidas para análise
1. A análise foi realizada com dados entre 11/02/2022 e 06/04/2022.
2. Assumimos Marketplace como modelo de negócio
3. Os 3 principais visões do negocio foram: Visão transação de pedidos, visão restaurantes e visão entregadores
    
# 3.Estratégia da solução
    
O painel estratégico foi desenvolvido utilizando as métricas que refletem as  3 principais visões do modelo de negócio da empresa:
    
 1. Visão do crescimento da empresa.
 2. Visão do crescimento dos restaurantes.
 3. Visão do crescimento dos entregadores.
    
 Cada visão é representada pelo seguinte conjunto de métricas.
    
 ## 3.1 Visão do crescimento da empresa
    1. Pedidos por dia
    2. Porcentagem de pedidos por condições de trânsito.
    3. Quantidade de pedidos por tipo e por cidade.
    4. Pedidos por semana.
    5. Quantidade de pedidos por tipo de entrega
    6. Quantidade de pedidos por condições de trânsito tipo de cidade.
 ## 3.2 Visão do crescimento dos restaurantes.
    1. Quantidade de pedidos únicos.
    2. Distância média percorrida.
    3. Tempo médio de entrega durante festival e dias normais.
    4. Desvio padrão do tempo de entrega durante festivais e dias normais.
    5. Tempo de entrega médio por cidade.
    6. Distribuição do tempo médio de entrega por cidade.
    7. Tempo médio de entrega por tipo de pedido.
    
 ## 3.3 Visão do crescimento dos entregadores
    
    1. Idade do entregador mais velho e do mais novo.
    2. Avaliação do melhor e do pior veiculo.
    3. Avaliação média por entregadores.
    4. Avaliação média por condições do trânsito.
    5. Avaliação média por condições climáticas.
    6. Tempo médio do entregador mais rápido.
    7. Tempo médio do entregador mais rápido por cidade.
    

# 4. Top 3 Insights de dados.
1.A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximadamente 10% do número de pedidos em dia sequenciais.

2.As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.

3.As maiores variações no tempo de entrega, acontecem durante o clima ensolarado.
    
# 5. O produto final do projeto
    
Painel online, hospedado em um Cloud e disponível para acesso em qualquer disponível conectado à internet.
    
O painel pode ser acessado através desse link: [https://natanmondoni-curry-company-home.streamlit.app/](https://natanmondoni-curry-company-home.streamlit.app/)
    

# 6.Conclusão
    
Para atender a essas visões, foram definidas métricas específicas para cada uma delas, visando oferecer uma análise completa do processo de entrega e permitindo tomadas de decisões mais eficientes.

O painel estratégico resultante do projeto foi desenvolvido com base nessas métricas, e pode ser acessado online por meio de um link disponível para acesso em qualquer dispositivo conectado à internet.

Com isso, a empresa pode facilmente visualizar e compreender os principais KPIs, identificar áreas que precisam de melhorias e tomar decisões embasadas em dados que impactam positivamente seus negócios.
    
# 7.Próximo passos
1. Adicionar mais filtros.
2. Implementar a visão de negócio.
