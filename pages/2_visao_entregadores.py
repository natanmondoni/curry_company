# Libraries


import pandas as pd
import plotly.express as px

import streamlit as st
from PIL import Image
import folium


st.set_page_config(page_title = 'Visão Entregadores', page_icon='🛵', layout='wide')

#Funcões
#-----------------------------------------------

def top_delivers(df1, top_asc):
    df2=df1[['time_taken(min)','city','delivery_person_id']].groupby(['city','delivery_person_id']).mean().sort_values(['city','delivery_person_id'],
                                                                                                                                       ascending=False).reset_index()


    df3 = df2.loc[df2['city'] == 'Metropolitian'].head(10)
    df4 = df2.loc[df2['city'] == 'Urban'].head(10)
    df5 = df2.loc[df2['city'] == 'Semi-Urban'].head(10)

    df_entregadores_lentos = pd.concat([df3,df4,df5]).reset_index(drop=True)
                    
    return df_entregadores_lentos





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

# Import Cleaning dataset
df1 = clean_code(df)


#=========================================
#Barra lateral
#=========================================
st.header('Marketplace - Visão Entregadores 🛵')
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

tab1,tab2,tab3 = st.tabs(['Visão Gerencial','_','_'])

with tab1:
    with st.container():
        st.title('Overall Metrics')
        
        col1,col2,col3,col4 = st.columns(4,gap="large")
        
        with col1:
            # Maior idade dos entregadores
            st.subheader('Maior de idade')
            
            maior_idade = df1.loc[:,"delivery_person_age"].max()
            col1.metric('Maior de idade',maior_idade)
            
        
        
        with col2:
            
            # Menor idade dos entregadores
            st.subheader('Menor de Idade')
            
            menor_idade = df1.loc[:,"delivery_person_age"].min()
            col2.metric('Menor de idade',menor_idade)
        
        
        with col3:
            
            st.subheader('Melhor condição de veiculos')
            
            melhor_condicao = df1.loc[:,'vehicle_condition'].max()
            col3.metric('Melhor condição do veiculo', melhor_condicao)
            
            
        with col4:
            
            st.subheader('Pior condição de veiculos')
            
            pior_condicao = df1.loc[:,'vehicle_condition'].min()
            col4.metric('Pior condição de veiculo', pior_condicao)
            
    
    with st.container():
        st.markdown("""___""")
        st.title('Avaliações')
        
        col1,col2 = st.columns(2)
        with col1:
            st.caption('Avalição media por Entregadores 🧮')
            
            df_entregadores = df1[['delivery_person_id','delivery_person_ratings']].groupby('delivery_person_id').mean().reset_index()
            
            st.dataframe(df_entregadores)
        
        
        with col2:
            st.caption('Avalição media por transito 🧮')
            
            # agrupando por tipos de trafegos e buscando a media de avaliacoes de entregas
            df_transito =  df1[['road_traffic_density','delivery_person_ratings']].groupby('road_traffic_density').mean().reset_index()
            
            #Ploty da tabela
            st.dataframe(df_transito)
            
            #---------------------------------------------------------------------------------------------------------------------------------
            st.caption('Avalição media por clima 🧮')
            
            # agrupando por tipos de condicoes climaticas e buscando a media de avaliacoes de entregas
            df_clima = df1[['delivery_person_ratings','weatherconditions']].groupby('weatherconditions').mean().reset_index()
            
            #Ploty da tabela
            st.dataframe(df_clima)
        
        
        with st.container():
            st.markdown("""___""")
            st.title('Velocidade de Entrega')
            
            
            col1,col2 = st.columns(2)
            
            
            with col1:
                st.caption('Top Entregadores mais rapidos 🛵⚡')
                
                df_entregadores_lentos= top_delivers(df1, top_asc=True)
                st.dataframe(df_entregadores_lentos)
                
                
            with col2:
                
                st.caption('Entregadores mais lentos 🛵🐢')
                df_entregadores_lentos= top_delivers(df1, top_asc=False)
                
                st.dataframe(df_entregadores_lentos)
                
                
                
                
                