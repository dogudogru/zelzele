import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

@st.cache
def dataConstructer(url):

    df = pd.read_table(url, skiprows=[0, 1, 2, 3, 5], delimiter='/n', encoding='ISO-8859-1')
    df = df[66:566]
    df.columns = ['row']
    df = df['row'].str.split('\s+', n=8, expand=True)
    df = df.rename(columns={0:"Date",1:"Local Time",2:"Latitude",3:"Longtitude", 4:"Depth", 5:"MD", 6:"ML",7:"Mw",8:"tobecut"})
    df[['Location','Characteristic']] = df['tobecut'].str.split('Ýlks',expand=True)
    df['Characteristic'] = df['Characteristic'].replace(['el'],'İlksel')
    df = df.drop(['tobecut'], axis=1)
    df = df.dropna()
    df.Latitude = pd.to_numeric(df.Latitude, errors='coerce')
    df.Longtitude = pd.to_numeric(df.Longtitude, errors='coerce')
    df.Depth = pd.to_numeric(df.Depth, errors='coerce')
    df.MD = pd.to_numeric(df.MD, errors='coerce')
    df.ML = pd.to_numeric(df.ML, errors='coerce')
    df.Mw = pd.to_numeric(df.Mw, errors='coerce')
    df['Time'] = df.Date + " " + df["Local Time"]
    df['Time'] = pd.to_datetime(df['Time'], format='%Y.%m.%d %H:%M:%S')
    df['Day'] = df['Time'].dt.strftime("%d %B, %Y")
    df = df.sort_values(by=['Time'])
    data = df.fillna('-').astype(str)
    data = data.drop(['Date','Time'], axis=1)
    data = data.reindex(['Day','Local Time','Latitude', 'Longtitude', 'Depth', 'MD','ML','Mw','Location','Characteristic'], axis=1)
    df['Region'] = pd.np.where(df.Location.str.contains("EDIRNE"), "Marmara",
                   pd.np.where(df.Location.str.contains("KIRKLARELI"), "Marmara",
                   pd.np.where(df.Location.str.contains("ISTANBUL"), "Marmara",
                   pd.np.where(df.Location.str.contains("KOCAELI"), "Marmara",
                   pd.np.where(df.Location.str.contains("YALOVA"), "Marmara",
                   pd.np.where(df.Location.str.contains("SAKARYA"), "Marmara",
                   pd.np.where(df.Location.str.contains("BILECIK"), "Marmara",
                   pd.np.where(df.Location.str.contains("BURSA"), "Marmara",
                   pd.np.where(df.Location.str.contains("BALIKESIR"), "Marmara",
                   pd.np.where(df.Location.str.contains("CANAKKALE"), "Marmara",
                   pd.np.where(df.Location.str.contains("AKSARAY"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("ANKARA"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("CANKIRI"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("ESKISEHIR"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("KARAMAN"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("KIRIKKALE"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("KIRSEHIR"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("KONYA"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("NEVSEHIR"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("NIGDE"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("SIVAS"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("YOZGAT"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("KAYSERI"), "Central Anatolia",
                   pd.np.where(df.Location.str.contains("IZMIR"), "Aegean",
                   pd.np.where(df.Location.str.contains("MANISA"), "Aegean",
                   pd.np.where(df.Location.str.contains("AYDIN"), "Aegean",
                   pd.np.where(df.Location.str.contains("DENIZLI"), "Aegean",
                   pd.np.where(df.Location.str.contains("KUTAHYA"), "Aegean",
                   pd.np.where(df.Location.str.contains("AFYON"), "Aegean",
                   pd.np.where(df.Location.str.contains("USAK"), "Aegean",
                   pd.np.where(df.Location.str.contains("MUGLA"), "Aegean",
                   pd.np.where(df.Location.str.contains("ADANA"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("OSMANIYE"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("ANTALYA"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("BURDUR"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("HATAY"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("ISPARTA"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("MERSIN"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("KAHRAMANMARAS"), "Mediterranean",
                   pd.np.where(df.Location.str.contains("RIZE"), "Black Sea",
                   pd.np.where(df.Location.str.contains("TRABZON"), "Black Sea",
                   pd.np.where(df.Location.str.contains("ARTVIN"), "Black Sea",
                   pd.np.where(df.Location.str.contains("SINOP"), "Black Sea",
                   pd.np.where(df.Location.str.contains("TOKAT"), "Black Sea",
                   pd.np.where(df.Location.str.contains("CORUM"), "Black Sea",
                   pd.np.where(df.Location.str.contains("AMASYA"), "Black Sea",
                   pd.np.where(df.Location.str.contains("SAMSUN"), "Black Sea",
                   pd.np.where(df.Location.str.contains("ZONGULDAK"), "Black Sea",
                   pd.np.where(df.Location.str.contains("BOLU"), "Black Sea",
                   pd.np.where(df.Location.str.contains("DUZCE"), "Black Sea",
                   pd.np.where(df.Location.str.contains("KARABUK"), "Black Sea",
                   pd.np.where(df.Location.str.contains("BARTIN"), "Black Sea",
                   pd.np.where(df.Location.str.contains("KASTAMONU"), "Black Sea",
                   pd.np.where(df.Location.str.contains("BAYBURT"), "Black Sea",
                   pd.np.where(df.Location.str.contains("GIRESUN"), "Black Sea",
                   pd.np.where(df.Location.str.contains("GUMUSHANE"), "Black Sea",
                   pd.np.where(df.Location.str.contains("ORDU"), "Black Sea",
                   pd.np.where(df.Location.str.contains("AGRI"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("ARDAHAN"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("BINGOL"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("BITLIS"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("ELAZIG"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("ERZINCAN"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("ERZURUM"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("HAKKARI"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("IGDIR"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("KARS"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("MALATYA"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("(MUS)"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("TUNCELI"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("(VAN)"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("SIRNAK"), "Eastern Anatolia",
                   pd.np.where(df.Location.str.contains("ADIYAMAN"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("BATMAN"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("DIYARBAKIR"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("GAZIANTEP"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("""(KILIS)"""), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("MARDIN"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("SIIRT"), "Southeastern Anatolia",
                   pd.np.where(df.Location.str.contains("SANLIURFA"), "Southeastern Anatolia", "Other"))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

    return data, df



def printDensityMap(data_selected_province):
    fig = px.density_mapbox(data_selected_province, lat="Latitude", lon="Longtitude", z="ML", hover_name ="Location",hover_data=["Date","Local Time"] , radius=10, mapbox_style="stamen-watercolor", zoom=4)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    
    return fig

def printBubbleScatter(data_selected_province):
    fig = px.scatter(data_selected_province, x="Time", y="ML",hover_name="Location",hover_data=["Depth","Date","Local Time"], size="ML", color="ML", opacity=0.7)
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',    
    })

    return fig

def animatedMap(data_selected_province):

    fig = px.scatter_geo(data_selected_province,  lat="Latitude",lon="Longtitude", color="ML",
                        hover_name="Location", size="ML",
                        animation_frame="Day",
                        projection="kavrayskiy7")

    fig.update_traces(marker=dict(size=50))
    fig.update_geos(fitbounds="locations")
    fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})

    return fig