"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""
import json
infile = open('univ.json','r')
#outfile = open('readable_uni_data.json', 'w')

uni_data = json.load(infile)

#json.dump(uni_data, outfile, indent=4)

unis = []
power_five = [102,107,108,127,130]

#map 1
size1 = []
lats1 = []
lons1 = []
display1 = []

for i in uni_data:
    if i['NCAA']['NAIA conference number football (IC2020)'] in power_five:
        if i['Graduation rate  women (DRVGR2020)'] > 50:
            name1= i['instnm']
            mapsize= .001* float(i["Total  enrollment (DRVEF2020)"])
            size1.append(mapsize)
            lons1.append(i['Longitude location of institution (HD2020)'])
            lats1.append(i['Latitude location of institution (HD2020)'])
            grad_rate1 = i["Graduation rate  women (DRVGR2020)"]
            display1.append(f'{name1}, {grad_rate1}%')

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

map1= [
    {'type':'scattergeo',
    'lon':lons1, 
    'lat': lats1,
    'text': display1,
    'marker': {'size': size1, 'color': 'blue'}}]

my_layout1 = Layout(title = 'Universities with Graduation rate for Women over 50%')

fig1 = {'data': map1, 'layout': my_layout1}

offline.plot(fig1,filename= 'WomenGrads.html')


#map 2
size2 = []
lats2 = []
lons2 = []
display2 = []

for i in uni_data:
    if i['NCAA']['NAIA conference number football (IC2020)'] in power_five:
        if i['Percent of total enrollment that are Black or African American (DRVEF2020)'] > 10:
            name2= i['instnm']
            mapsize= .001* float(i["Total  enrollment (DRVEF2020)"])
            size2.append(mapsize)
            lons2.append(i['Longitude location of institution (HD2020)'])
            lats2.append(i['Latitude location of institution (HD2020)'])
            total_enroll = i['Percent of total enrollment that are Black or African American (DRVEF2020)']
            display2.append(f'{name2}, {total_enroll}%')


map2= [
    {'type':'scattergeo',
    'lon':lons2, 
    'lat': lats2,
    'text': display2,
    'marker': {'size': size2, 'color': 'red'}}]

my_layout2 = Layout(title = 'Universities with Black or African American Enrollment over 10%')

fig2 = {'data': map2, 'layout': my_layout2}

offline.plot(fig2,filename= 'BlackGrads.html')

#map 3
size3 = []
lats3 = []
lons3 = []
display3 = []

for i in uni_data:
    if i['NCAA']['NAIA conference number football (IC2020)'] in power_five:

        try:
            price = int(i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'])
        except TypeError:
            print("Error found")
        else:

            if price> 50000:
                name3= i['instnm']
                mapsize= .001* float(i["Total  enrollment (DRVEF2020)"])
                size3.append(mapsize)
                lons3.append(i['Longitude location of institution (HD2020)'])
                lats3.append(i['Latitude location of institution (HD2020)'])
                total_price = i['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']
                display3.append(f'{name3}, {total_price}%')



map3= [
    {'type':'scattergeo',
    'lon':lons3, 
    'lat': lats3,
    'text': display3,
    'marker': {'size': size3, 'color': 'green'}}]

my_layout3 = Layout(title = 'Universities that have a Total price for in-state students living off campus over $50,000')

fig3 = {'data': map3, 'layout': my_layout3}

offline.plot(fig3,filename= 'TotalPrice')




