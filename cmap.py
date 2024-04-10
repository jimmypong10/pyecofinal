#import folium
import folium
import geopandas as gpd
import pandas as pd
import webbrowser

def cmap(excel_path):
    #Creaate a map object for choropleth map
    #Set location to your location of interest (latitude and longitude )
    map0 = folium.Map(location=[23.9,121.52], zoom_start=7)
    geo_taiwan = gpd.read_file('map/TWD97/COUNTY_MOI_1090820.shp',encoding='utf-8')
    #Dataset = pd.read_excel("test_sub2.xlsx",header=None).T
    Dataset = pd.read_excel(excel_path)
    Dataset[4] = pd.to_numeric(Dataset[4], errors='coerce')
    Dataset = Dataset.replace("－",0)
    Dataset = Dataset[[3,4]]
    print(Dataset)
    Dataset.info()
    
    #Create choropleth map object with key on TOWNNAME
    folium.Choropleth(geo_data = geo_taiwan,#Assign geo_data to your geojson file
        name = "choropleth",
        data = Dataset,#Assign dataset of interest
        columns = [3,4],#Assign columns in the dataset for plotting
        key_on = 'feature.properties.COUNTYNAME',#Assign the key that geojson uses to connect with dataset
        fill_color = 'YlOrRd',
        fill_opacity = 0.7,
        line_opacity = 0.5,
        legend_name = 'Taiwan').add_to(map0)

    #Create style_function
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    
    #Create highlight_function
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}

    #合併geo_taiwan中的資訊和excel檔內資訊
    new_names={3:"COUNTYNAME",4:"CRIMERATE"}
    Dataset.rename(columns = new_names , inplace = True)
    geo_taiwan = geo_taiwan.merge(Dataset, on = "COUNTYNAME" , how='left')

    #Create popup tooltip object
    NIL = folium.features.GeoJson(
        geo_taiwan,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['COUNTYNAME',"CRIMERATE"],
            aliases=['城市',"破獲率"],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))
    
    #Add tooltip object to the map
    map0.add_child(NIL)
    map0.keep_in_front(NIL)
    folium.LayerControl().add_to(map0)
    
    output_file = "map_volacno.html"
    map0.save(output_file)
    webbrowser.open(output_file, new=2)