# Libraries


import pandas as pd
import numpy as np
import plotly.express as px
from haversine import haversine
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go

st.set_page_config(page_title = 'Visão Restaurante', page_icon='🍽', layout='wide')


#----------------------------------------------
#Funções
#----------------------------------------------

def mean_std_time_on_traffic(df1):
    
    """
       Esta função calcula o tempo médio e o desvio padrão do tempo de entrega por tipo de cidade e condição de tráfegos. 
       Parâmetros:
            Input:
                 - df: DataFrame com os dados necessários para o cálculo
                 - Tipo de operação que precisa ser calculado
                     'mean_time': Calcula o tempo médio
                     'std_time': Calcula o desvio padrão do tempo.
                 
                 - Usei a função GROUPBY para agrupar os tipos de cidades e tráfegos e realisar a operação em cima da coluna TIME_TAKEN(MIN).
                 - Plotly de um gráfico de sunburst separado por tipo de cidade e densidade de trafego. Mostrando a média e o desvio padrão do tempo de entrega.
                            
                     
            Output: 1 Gráfico
    """
    
    df_aux = df1[['time_taken(min)','city','road_traffic_density']].groupby(['city','road_traffic_density']).agg({'time_taken(min)':['mean','std']})

    df_aux.columns = ['mean_time','std_time']

    df_aux = df_aux.reset_index()

            
    fig = px.sunburst(df_aux, path=['city','road_traffic_density'], values='mean_time',
                      color='std_time', color_continuous_scale='reds',
                      color_continuous_midpoint=np.average(df_aux['std_time']))
    fig.update_layout(autosize=False,width=400,height=400,margin=dict(l=70,r=0,b=0,t=100,pad=4 ))
    
    return fig


def mean_std_time_graph(df1):
    """
       Esta função calcula o tempo médio e o desvio padrão do tempo de entrega
       Parâmetros:
            Input:
                 - df: DataFrame com os dados necessários para o cálculo
                 - Tipo de operação que precisa ser calculado
                     'mean_time': Calcula o tempo médio
                     'std_time': Calcula o desvio padrão do tempo.
                 
                 - Usei a função GROUPBY para agrupar e realisar a operação em cima.
                 - Plotly de um gráfico de barras com a média e o desvio padrão em relação as entregas. Agrupado por tipo de cidade.
                            
                     
            Output: Dataframe com 2 colunas e 1 linha.
    """
    
    
    
    df_aux = df1[['city','time_taken(min)']].groupby('city').agg({'time_taken(min)':['mean','std']})


    df_aux.columns = ['mean_time','std_time']
    df_aux = df_aux.reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar ( name='Control',
                           x=df_aux['city'],
                           y=df_aux['mean_time'],
                           error_y=dict(type='data',array=df_aux['std_time']))) 
    fig.update_layout(autosize=False,width=300,height=400,margin=dict(l=0,r=0,b=0,t=100,pad=4 ))
                
    return fig




def time_festival(df1,condition,col):
     
    
    """
       Esta função calcula o  tempo médio e o desvio padrão do tempo de entrega
       Parâmetros:
            Input:
                 - df: DataFrame com os dados necessários para o cálculo
                 - col: Tipo de operação que precisa ser calculado
                     'mean_time': Calcula o tempo médio
                     'std_time': Calcula o desvio padrão do tempo.
                 
                 - condition: Recebe a condição
                              'Yes': Será mostrado apenas os dados com festival.
                              'No': Será mostrado apenas os dados sem festival.
                            
                     
            Output: Dataframe com 2 colunas e 1 linha.
    """
               
    
    
    ##  6. O tempo médio de entrega durante os Festivais
    resposta = df1[['time_taken(min)','festival']].groupby('festival').agg({'time_taken(min)':['mean','std']})

    resposta.columns = ['mean_time','std_time']

    resposta = resposta.reset_index()

    resposta = np.round(resposta.loc[resposta['festival'] == condition, col],2)
            
    return resposta



def distance_delivery(df1, fig):
    
    """
       Esta função calcula o tempo médio do restaurante ao destino final
       Parâmetros:
            Input:
                 - fig: É a condição para mostrar determinado valor
                      fig = False: Será mostrado uma metric da distancia média das entregas ao restaurante
                      fig = True: Será mostrado um gráfico com a distancia média do restaurante ao destino final e a porcentagem de pedidos que sairam daquela área 
                                  específica, relacionando os tipos de cidades.
                 
                
                     
            Output: Uma metric com a distancia média do restaurante ao destino final.
                    Um gráfico com a distancia média do restaurante ao destino final agrupado ao tipo de cidade. 
    """
    
    
    if fig== False:
        
        cols = ['restaurant_latitude','restaurant_longitude','delivery_location_latitude','delivery_location_longitude']
        df1['distancia'] = df1.loc[:,cols].apply(lambda x:
                                                 haversine( (x['restaurant_latitude'],x['restaurant_longitude']),
                                                            (x['delivery_location_latitude'], x['delivery_location_longitude'])),axis=1)
        avg_distancia = np.round(df1['distancia'].mean(),2)
        
        return avg_distancia
        
    else:
        
        cols = ['restaurant_latitude','restaurant_longitude','delivery_location_latitude','delivery_location_longitude']
        df1['distancia'] = df1.loc[:,cols].apply(lambda x:
                                                 haversine((x['restaurant_latitude'],x['restaurant_longitude']),
                                                           (x['delivery_location_latitude'], x['delivery_location_longitude'])),axis=1)

        avg_distancia = df1.loc[:,['city','distancia']].groupby('city').mean().reset_index()
        fig = go.Figure(data=[go.Pie(labels=avg_distancia['city'] ,values=avg_distancia['distancia'],pull=[0,0.1,0])])
        fig.update_layout(autosize=False,width=360,height=400,margin=dict(l=0,r=0,b=0,t=100,pad=4 ))
        
        return fig




def clean_code(df1):
    """Esta função tem a responsabilidade de limpar o dataframe
       
       Tipos de limpeza:
       1. Remoção dos dados NaN
       2. Mudança do tipo da coluna de dados
       3. Remoção dos espaços das variaveis de textos
       4. Formatação da coluna de datas
       5. Limpeza da coluna de tempo ( remoc1ão do texto da variavel númerica
       
       Input: DataFrame
       Output: DataFrame

    """

    

    #Limpeza de Dados

    # Removendo espaço da string

    df1.loc[:,'ID'] =  df1.loc[:,'ID'].str.strip()    
    
    df1.loc[:,'Delivery_person_ID'] =  df1.loc[:,'Delivery_person_ID'].str.strip()
    
    df1.loc[:,'Road_traffic_density'] = df1.loc[:,'Road_traffic_density'].str.strip()
    
    df1.loc[:,'multiple_deliveries'] = df1.loc[:,'multiple_deliveries'].str.strip()
    
    df1.loc[:,'Type_of_order'] = df1.loc[:,'Type_of_order'].str.strip()
    
    df1.loc[:,'Type_of_vehicle'] = df1.loc[:,'Type_of_vehicle'].str.strip()
    
    df1.loc[:,'Festival'] = df1.loc[:,'Festival'].str.strip()
    
    df1.loc[:,'City'] = df1.loc[:,'City'].str.strip()

    # Apagando as linhas vazias da coluna idade_entregador
    linhas_vazias = df1['Delivery_person_Age'] !='NaN ' 
    df1 = df1.loc[linhas_vazias, :].copy()

    # Removendo valores NaN
    df1= df1.loc[df1['City'] != 'NaN', :]

    # Removendo valores NaN
    df1= df1.loc[df1['Festival'] != 'NaN', :]

    # Apagando valores NaN
    df1= df1.loc[df1['Road_traffic_density'] != 'NaN', :]

    # Covertendo a coluna Order_Date de texto para DATA
    df1['Order_Date'] = pd.to_datetime(df1['Order_Date'],format='%d-%m-%Y')



    # Removendo linhas com os valores "NaN "
    linhas_selecionadas =  df1['multiple_deliveries'] != 'NaN'
    df1 = df1.loc[linhas_selecionadas, :].copy()

    # Convertendo 
    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype( 'int64' )



    # Convertendo a Coluna Age de texto para numero
    df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype( 'int64' )


    # Convertendo a coluna Ratings de texto para numero decimal

    df1['Delivery_person_Ratings'] = df1['Delivery_person_Ratings'].astype(float)

    #  Removendo os espaços dentro dos valores das variaveis


    # Retirando o texto do valor
    df1['Time_taken(min)'] = df1['Time_taken(min)'].apply(lambda x: x.split('(min) ')[1])
    df1['Time_taken(min)'] = df1['Time_taken(min)'].astype('int64') 


    #convertendo os nomes das colunasn covertendo os nomes das colunas
    df1.columns = ['id','delivery_person_id','delivery_person_age','delivery_person_ratings','restaurant_latitude','restaurant_longitude','delivery_location_latitude','delivery_location_longitude','order_date','time_orderd','time_order_picked','weatherconditions','road_traffic_density','vehicle_condition','type_of_order','type_of_vehicle','multiple_deliveries','festival','city','time_taken(min)']


    # Transformando e criando variavel por semana do ano 
    df1['week_of_year'] = df1['order_date'].dt.strftime('%U')
    
    return df1


#import dataset
df = pd.read_csv('datasets/train.csv.download/train.csv')

# cleanding Dataset

df1 = clean_code(df)





#=========================================
#Barra lateral
#=========================================
st.header('Marketplace - Visão Restaurantes 🍽️')
st.sidebar.image('https://icones.pro/wp-content/uploads/2021/08/icone-cible-orange.png')



st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")



st.sidebar.markdown('## Selecione uma data limite')
date_slider = st.sidebar.slider(
    'Até qual valor?',
    value= pd.datetime(2022,4,13),
    min_value=pd.datetime(2022,2,11),
    max_value=pd.datetime(2022,4,6),
    format='DD-MM-YYYY')


st.sidebar.markdown("""---""")


traffic_options = st.sidebar.multiselect(
    'Quais as condições de trânsito?',
    ['Low','Medium','High','Jam'],
    default='Low')


clima_options = st.sidebar.multiselect(
    'Quais as condições climaticas?',
    ['conditions Cloudy','conditions Fog','conditions Sandstorms','conditions Stormy','conditions Sunny','conditions Windy'],
    default='conditions Cloudy')



st.sidebar.markdown("""---""")
st.sidebar.markdown('### Powered by Comunidade DS')

# Filtro de data
linhas_selecionadas = df1['order_date'] < date_slider 

df1 = df1.loc[linhas_selecionadas, :]

#Filtro de transito

linhas_selecionadas = df1['road_traffic_density'].isin(traffic_options)


#Filtro de clima
linhas_selecionadas = df1['weatherconditions'].isin(clima_options)

df1 = df1.loc[linhas_selecionadas, :]

#=========================================
# Layout do Streamlit
#=========================================


tab1,tab2,tab3 = st.tabs(['Visão Gerencial','',''])

with tab1:
    
    with st.container():
        st.title('Overal Metrics')
        
        col1,col2,col3,= st.columns(3)
        col4,col5,col6 = st.columns(3)
        

            
        with col1:
            avg_distancia = distance_delivery(df1, fig = False)
            
            col1.metric('A distancia média das entregas',avg_distancia)
            
            
          
            
            
            
        with col2:
            
            resposta = time_festival(df1, condition='Yes',col= 'mean_time')
            
            col2.metric('Tempo Médio de Entrega c/ Festival',resposta)
            
            
        
        with col3:
            
            resposta = time_festival(df1, condition='Yes',col= 'std_time')
            
            col3.metric('STD da Entrega c/ Festival',resposta)
            
        
        with col4:
            
            resposta = time_festival(df1, condition='No',col= 'mean_time')
            
            col4.metric('Médio da Entrega s/ Festival',resposta)
                       
                
        with col5:
            resposta = time_festival(df1, condition='No',col= 'std_time')
            col5.metric('STD da Entrega s/ Festival',resposta)
           
        
            
        with col6:
            delivery_unique = len(df1['delivery_person_id'].unique())
            col6.metric('Entregadores Únicos',delivery_unique)
        
    
    
    with st.container():
        st.markdown("""___""")
        st.title('Metricas dos Tempos de Entregas')
        col1,col2 = st.columns(2)
        
        
        with col1:
            st.caption('Metricas Por Tipos De Cidades')
            fig = mean_std_time_graph(df1)
            st.plotly_chart(fig)

        with col2:
            
            
            
            st.caption('Metricas Por Tipos De Cidades/Trafegos')
            df_aux = df1[['time_taken(min)','city','road_traffic_density']].groupby(['city','road_traffic_density']).agg({'time_taken(min)': ['mean','std']})

            df_aux.columns = ['mean_time','std_time']

            df_aux = df_aux.reset_index()

            st.dataframe(df_aux)
    
    with st.container():
        st.markdown("""___""")
        st.title('Distribuição do tempo')
        
        
        
        col1 , col2= st.columns(2)
        
        
        with col1:
            fig = distance_delivery(df1, fig=True)
            
            st.plotly_chart(fig)
           

            
        with col2:
                fig = mean_std_time_on_traffic(df1)
                st.plotly_chart(fig)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        