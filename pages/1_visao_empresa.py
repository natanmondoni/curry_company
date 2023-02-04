# Libraries


import pandas as pd
import plotly.express as px

import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title = 'Visão Empresa', page_icon='📈', layout='wide')

#--------------------------------------------------------
#Funções
#--------------------------------------------------------
def country_maps(df1):
    
    """ Essa função tem a responsabilidade de mostrar o tipo de city e tráfego na região de entrega.
        
        Tipos de responsabilidade:
        
        1. Agrupei por tipo de city e tráfego. Busquei a média da localição da entrega.
        2. Usei a função para plotar o mapa.
        
        
        Input: DataFrame
        Output: Plotagem de mapa
    
        
    

    """
    
    
    df_aux = (df1.loc[:,['city','road_traffic_density','delivery_location_latitude','delivery_location_longitude']]
              .groupby(['city','road_traffic_density'])
              .median().reset_index())

    map= folium.Map()
    for index, location_info in df_aux.iterrows():
        folium.Marker([location_info['delivery_location_latitude'],
                       location_info['delivery_location_longitude']],
                       popup=location_info[['city','road_traffic_density']]).add_to(map)


    folium_static(map, width=1024, height=600)

    
    
    return None




def order_share_by_week(df1):
    """ Essa função tem a responsabilidade de mostrar a média de entregas na semana do ano 
        por cada motoboy
        
        Tipos de responsabilidade:
        
        1. Agrupar as semanas do ano e contar os pedidos(id)
        2. Agrupar as semanas do ano e contar os entregadores únicos
        3. Usar a função para juntar as variaveis transformadas.
        4. Dividindo a quantidade de pedidos por cada entregador único
        5. plotando o gráfico
        
        Input: DataFrame
        Output: Plotagem de gráfico
    """
    
    
    
    
    
    
    # Agrupando e contanto os pedidos por semana do ano
    df_aux01 = df1[['id','week_of_year']].groupby('week_of_year').count().reset_index()

    # Agrupando e buscando os entregadores unicos
    df_aux02 = df1[['delivery_person_id','week_of_year']].groupby('week_of_year').nunique().reset_index()

    # Juntando os Dataframe
    df_aux = pd.merge(df_aux01,df_aux02, how='inner')

    # Buscando os a quantidade de pedidos por entregadores unicos
    df_aux['order_by_delivery']= df_aux['id'] / df_aux['delivery_person_id']
    fig = px.line(df_aux, x='week_of_year', y='order_by_delivery')
    
    return fig




def order_by_week(df1):
    """ Essa função tem a responsabilidade de mostrar a quantidade
        de pedidos nas semanas do ano
        
        Tipos de responsabilidade:
        
        1. Agrupar as semanas do ano e contar os pedidos(id)
        2. Usar a função PX para plotar o gráfico.
        
        Input: DataFrame
        Output: Plotagem de grafico
    """
    
    
    
    
    
    
    
    # Coluna de semana
    df_aux= df1.loc[:,['id','week_of_year']].groupby('week_of_year').count().reset_index()
    fig= px.line(df_aux,x='week_of_year', y='id')
            
    return fig



def traffic_order_city(df1):
    
    """Esta função tem a responsabilidade de agrupar as densidades de
       tráfegos e citys. Contar os pedidos por cada tipo de tráfego 
       
       Tipos responsabilidades :
       1. Agrupei os tipos de tráfegos e citys
       2. Fiz uma contagem por pedidos(id) em cada grupo de tráfegos e citys
       
       Input: DataFrame
       Output: Grafico de scatter. 

    """
    
    

    df_aux =df1[['id','city','road_traffic_density']].groupby(['city','road_traffic_density']).count().reset_index()
    fig = px.scatter(df_aux, x='city',y='road_traffic_density',size='id',color='city')
                
    return fig



def traffic_order_share(df1):
     
    """Esta função tem a responsabilidade de agrupar as densidades de
       tráfegos e contar os pedidos por cada tipo de tráfego 
       
       Tipos :
       1. Agrupei os tipos de tráfegos
       2. Fiz uma contagem por pedidos(id) em cada grupo de tráfegos
       
       Input: DataFrame
       Output: Grafico de pie. 

    """
  

    df_aux = df1.loc[:,['id','road_traffic_density']].groupby('road_traffic_density').count().reset_index()

    df_aux['entregas_perc'] = df_aux['id'] / df_aux['id'].sum()       


    fig=px.pie(df_aux, values='entregas_perc', names='road_traffic_density')
                
    return fig

def order_metric(df1):
    
    """Esta função tem a responsabilidade de agrupar as datas dos pedidos
       e contar quantos tiveram no dia
       
       Tipos :
       1. Agrupei a data da ordem
       2. Fiz uma contagem por pedidos(id) em cada grupo de data da ordem
       
       Input: DataFrame
       Output: Grafico de barras. 

    """
    
    
    # Agrupando por cada data e fazendo a contagem de         quantos pedidos tiveram naquele dia
    df_aux = df1[['id','order_date']].groupby('order_date').count().reset_index()                           


    #Desenhando o grafico de linhas 

    #Plotly

    fig = px.bar(df_aux, x='order_date',y='id')

            
            
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

#------------------------------------------- Inicio da Estrutura lógica do código ---------------------------------------------



#import dataset

df = pd.read_csv('datasets/train.csv.download/train.csv')

df1 = df.copy()
    
df1 = clean_code(df)




#=========================================
#Barra lateral
#=========================================
st.header('Marketplace - Visão Cliente do APP📱')
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
    'Quais as condições de trânsito',
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
df1 = df1.loc[linhas_selecionadas, :]



#Filtro de clima
linhas_selecionadas = df1['weatherconditions'].isin(clima_options)

df1 = df1.loc[linhas_selecionadas, :]


#=========================================
# Layout do Streamlit
#=========================================

tab1,tab2,tab3 = st.tabs(['Visão Gerencial','Visão Tática','Visão Geográfica'])



with tab1:
    with st.container():
        #Order Matric
        st.markdown('# Order by Date')
        
        fig = order_metric(df1)
        st.plotly_chart(fig,use_container_width= True)
        
        
        
       
    
    with st.container():
        col1,col2 = st.columns(2)
        
        with col1:
            st.markdown('# Traffic Order Share')
            fig = traffic_order_share(df1)
            
            st.plotly_chart(fig,use_container_width=True)
            
            
            
            
            
            
        with col2:
            st.markdown('# Traffic Order City')
            fig = traffic_order_city(df1)
            st.plotly_chart(fig,use_container_width=True)
            
            

with tab2:
    with st.container():
        st.markdown('# Order By Week  ')
        fig = order_by_week(df1)
        st.plotly_chart(fig,use_container_width=True)
    
    
    
    with st.container():
        
        st.markdown('Order By Share by Week')
        
        fig = order_share_by_week(df1)
        
        st.plotly_chart(fig,use_container_width=True)
    

    
with tab3:
    st.markdown('# Country Maps')
    country_maps(df1)
    
    
























































