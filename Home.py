import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon= "👨🏽‍💻")


#image_path = '/Users/natanferreiralima/repos_mac/ftc_lab/'

image = Image.open( 'visao_empresa.png')
st.sidebar.image( image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")


st.write("# Curry Company Growth Dashboard")

st.markdown(
    
    """
    Growth Dashboard foi construída para acompanhar as métricas de crescimento dos Entregadores, Restaurantes e     Empresa.
    
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
       - Visão Gerencial: Métricas gerais de comportamento.
       - Visão Tática: Indicadores semanais de crescimento.
       - Visão Geográfica: Insights de geolocalização.
       
    - Visão Entregador:
       - Acompanhamento dos indicadores semanais de crescimento
       
    - Visão Restaurantes:
       - Indicadores semanais de crescimento dos restaurantes
    ### Ask for Help
    - https://www.linkedin.com/in/natã-ferreira-lima-13300193/
      
      
    """)