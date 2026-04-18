# OlmstedCountyEmergencyGridMap
Olmsted County Emergency Grid Mapping used for SkyWarn/ARES by the Rochester Area Radio Club

During a SkyWarn event, I was reminded that it's not super easy to figure out where you are on the Olmsted Emergency Grid. The Elmers all know where they're at from past experience but newbies are left guessing especially if you're close to intersections of grid lines. It's also hard - maybe it's just me - to match your location to the Emergency Map jpg.

So I took a first stab at creating something to simplify this. Below are the links for how you use the map - a short youtube, the URL of the map and KMZ and KML files if you want to mess around with the data.
Caveat is that my starting point is a Jpeg Olmsted County Emergency Map from the rarchams site at https://www.rarchams.org/wp/wp-content/uploads/2019/01/stormwatcherolmstedco.jpg.
From this I dropped a top left and bottom right placemarks in Google Earth Pro to get GPS coordinates. Within these probably not terribly accurate hand dropped points I wrote a small python script to divide the map into the grid as depicted in the Jpeg file from rarchams.org.

How to use it: https://youtu.be/FX-L3eXPkqA

Map URL : https://www.google.com/maps/d/u/0/viewer?mid=12dEXO-fAB4wVuYCCxGvkwaohL-em2CU

Included in this repo are the generated KML and KMZ.
The KMZ is essentially the rarchams.org jpeg map super imposed over Google Earth Pro and from this I gathered the master corner coordinates for the map. 
Then those coordinates are used in the create_grid.py script to create the grid positions and export the KML.

The create_equal_grids.py was an experiment that came about when I noticed in Google Earth that my grids were getting bigger as they moved south towards the equator. 
Apprarently this is what happens when you take a round world and flatten it on a piece of paper and then draw geometric grids on it. The seemingly equal grids actually encompass a larger area 
closer to the equater and conversely smaller areas approaching the poles. After I generated the KML and looked at the results in Google Earth, it didn't match up to the original jpeg so I'm making an 
assumption that the grid was draw by drawing equidistant lines on a flat map. Though how that works in real life, I'm sure that southerly farmers are getting larger plots of land than northerly farmers...
but I digress.

You can use the included KML in various apps like Organic Maps or GAIA GPS (Look for them in Google Play and Apple's App Store) to map your curent location to the KML grid. 
You can even use aprs.fi to load the KML dynaically and have a APRS enabled map with the grid by going to dynamically linking the KML

eg. https://aprs.fi/#!lat=44.04840&lng=-92.49480&kml=https%3A%2F%2Fgist.github.com%2Ffcfang%2F1ffee5d7ea2ec49d4af8bafc65daabbd.js
Please send feedback as to accuracy and I can make adjustments as needed.
