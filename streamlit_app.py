import streamlit as st
from PIL import Image
from utils.funcs import dataConstructer, printDensityMap, printBubbleScatter, animatedMap


url = "http://www.koeri.boun.edu.tr/scripts/lst2.asp"

regions = ['All','Marmara', 'Aegean', 'Central Anatolia', 'Black Sea', 'Mediterranean', 'Southeastern Anatolia', 'Eastern Anatolia', 'Other']

def main():
    #Call data
    get_set = dataConstructer(url)

    #Density map
    st.header('Last 500 Earthquakes')
    heatmap = printDensityMap(get_set[1])
    st.plotly_chart(heatmap, use_container_width=True)
    image = Image.open('img/faultline1.jpg')
    with st.expander('Turkey Fault Line Map 🌎'):
        st.image(image, caption="""Squeezed between the Arabian and the Eurasian Plate, the Anatolian Fault escapes towards the West. Friday's quake is marked by a red star. (Modified from Okay et al. 1999)""")
    st.markdown("***")

    #Bubble scatter
    st.header('Buble Scatter - Regional Earthquake Data')
    reg_selected = st.multiselect('Select region', regions, default='Marmara')

    if reg_selected == ['All'] and len(reg_selected) == 1:
        bubblemap = printBubbleScatter(get_set[1])
        st.plotly_chart(bubblemap, use_container_width=True)

    else:
        bubblemap = printBubbleScatter(get_set[1][get_set[1].Region.isin(reg_selected)])
        st.plotly_chart(bubblemap, use_container_width=True)

    st.markdown("***")

    #Animated map
    st.header('Animated Daily Earthquakes')
    st.write("""Please press the play button below to activate the animated map""")
    st.plotly_chart(animatedMap(get_set[1]), use_container_width=True)

    #Sidebar
    logo = Image.open('img/pngegg.png')
    st.sidebar.image(logo)
    st.sidebar.title('Turkey Earthquake Dashboard')
    st.sidebar.write("""In Turkey, earthquakes are nothing out of the ordinary with thousands of tremors taking place all over the country.
    There is a well-known saying in Turkish <q>Coğrafya kaderdir</q> which means <q>Geography is destiny</q> and it perfectly describes Turkey's proneness to earthquakes.<br></br>
    The Anatolian transform fault system is probably the most active in the world. 
    It separates the Eurasian plate from the Anatolian plate in northern Turkey. <br></br>
    Some of the most destructive earthquakes in history have been caused by movement along this fault. 
    Lake Hazar lies along the East Anatolian transform fault.

    """, unsafe_allow_html=True)
    st.sidebar.title('About the data')
    st.sidebar.write("""The data is collected from well-known Kandilli Observatory Regional Earthquake-Tsunami Monitoring Center's website: 
    <href>http://www.koeri.boun.edu.tr/scripts/lst2.asp</href>. This app scrapes the information on KOERI's website and updates the dashboard regularly. The data is restricted to the last 500 recorded earthquakes.
    <br></br>
    <b>ML</b> = Local Magnitude""", unsafe_allow_html=True)

    st.sidebar.markdown('***')

    st.sidebar.write("""This dashboard is designed and built by <a href='https://www.linkedin.com/in/doğukandoğru'> Doğukan Doğru </href>""", unsafe_allow_html=True)

    st.sidebar.title('Sources')
    st.sidebar.markdown("""
    - <a href="http://www.koeri.boun.edu.tr/scripts/lasteq.asp"> KOERI BOUN </href></a>
    - <a href="https://deprem.afad.gov.tr/deprem-tehlike-haritasi?lang=en"> AFAD </href> </a>
    - <a href="https://seismo.berkeley.edu/blog/2020/01/26/quake-in-turkey-highlights-the-hazard-in-the-east-bay.html"> Berkeley Seismology Lab </href> </a>
    - <a href="https://www.dailysabah.com/turkey/why-is-turkey-so-prone-to-earthquakes/news"> Daily Sabah </href> </a>
    """, unsafe_allow_html=True)

if __name__ == "__main__":

    #Here we are setting the page configuration setting
    st.set_page_config(
        page_title="Turkey Earthquake Dashboard",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="auto"
    )

    main()