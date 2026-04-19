# Olmsted County Emergency Grid Map
Olmsted County Emergency Grid Mapping used for SkyWarn/ARES by the Rochester Area Radio Club

During a SkyWarn event, I was reminded that it's not super easy to figure out where you are on the Olmsted Emergency Grid. The Elmers all know where they're at from past experience but newbies are left guessing especially if you're close to intersections of grid lines. It's also hard - maybe it's just me - to match your location to the Emergency Map jpg.

So I took a first stab at creating something to simplify this. Below are the links for how you use the map - a short youtube, the URL of the map and KMZ and KML files if you want to mess around with the data.
Caveat is that my starting point is a Jpeg Olmsted County Emergency Map from the rarchams site at https://www.rarchams.org/wp/wp-content/uploads/2019/01/stormwatcherolmstedco.jpg.
From this I dropped a top left and bottom right placemarks in Google Earth Pro to get GPS coordinates. Within these probably not terribly accurate hand dropped points I wrote a small python script to divide the map into the grid as depicted in the Jpeg file from rarchams.org.

How to use it: https://youtu.be/FX-L3eXPkqA

Map URL : https://www.google.com/maps/d/u/0/viewer?mid=12dEXO-fAB4wVuYCCxGvkwaohL-em2CU

If you use this on an Android or Apple IOS device, be aware that if you have chosen to open map links with the Google Maps app, this will likely not go great for you. When you arrive at the web page and click on the icon that looks like a "fullscreen" icon, tapping that will open the Google Maps app which is fully locked down and will not display the grid. If you want the web functionality, you have have to disable the Open by Default setting in your App settings. On Samsung phones, it is under Settings > Apps > Maps > Open by Default and you have to uncheck the setting that says "Open map links with this App". Similarly on Pixels, it is under Settings > All Apps > See All XXX Apps > Maps > Open by Default > Choose "in your browser" instead of "In the app". Something similar on IOS devices but I don't have one to test.

Included in this repo are the generated KML and KMZ.
The KMZ is essentially the rarchams.org jpeg map super imposed over Google Earth Pro and from this I gathered the master corner coordinates for the map. Then those coordinates are used in the create_grid.py script to create the grid positions and export the KML. If you like to use Google Earth for your mapping, simply open it and choose File > Import and choose the kmz file. It will show up on your left navigation bar. If you want to make changes, create a branch and go for it. Ping me and I'll be happy to merge the changes in if they add to the project. For those who might be looking at the code and wondering why it's so complexly weird, I actually modify the grid to remove a bunch of them and modify Y1 and Y13 statically because, well, they're weird. So it's not just a matter of changing the north, south, east and west coords and it'll work for your grid. Lemme know if you need a more generic create a rectangular grid type of script.

For those that don't want to mess with your Google Maps settings, GAIA GPS is one good alternative. You can install the app from the Google Play Store or Apple App Store and once you have it installed and opened, you can simply link by clicking this link from your device : 
https://www.gaiagps.com/map/?loc=9.3/-92.3737/44.0133&pubLink=Dylivm9uFxiTmYJSnP3C2UdN&folderId=68454cfb-5354-4d96-9672-67d2fb9f60ac
The grid will become magically become available to you. No, I do not have the premium version of Gaia GPS but for those who might be averse to signing up for stuff, you will have to create an Gaia GPS account. One caveat here is that I've noticed that GAIA GPS sometimes has issues rendering the KML grid. It seems to come and go with varying levels of zoom. However, if you zoom in all the way, the grid always seems to render. Maybe something to fix in my KML.

Another alternative for a Mapping App on your phone is obviously, the origin of the coordinates themselves. I started this project mapping the jpg in Google Earth. You can import the KML into Google Earth on your phone/tablet while you're out and about and find your grid squares that way too. The downside of Google Earth is that it relies on an active data connection which may make it less desirable in ARES situations than GAIA GPS which allows you to download offline maps. I've read that you can import APRS data into Google Earth from aprs.fi also but I'm unable to see any data points after importing their KML into Google Earth. I'll keep working on that as it might be nice for Net Control to have during an active event.

The create_equal_grids.py was an experiment that came about when I noticed in Google Earth that my grids were getting bigger as they moved south towards the equator. 
Apprarently this is what happens when you take a round world and flatten it on a piece of paper and then draw geometric grids on it. The seemingly equal grids actually encompass a larger area closer to the equator and conversely smaller areas approaching the poles. After I generated the KML and looked at the results in Google Earth, it didn't match up to the original jpeg so I'm making an 
assumption that the grid was draw by drawing equidistant lines on a flat map. Though how that works in real life, I'm sure that southerly farmers aren't getting larger plots of land than their northerly bretheren...
but I digress.

Please send feedback as to accuracy and I can make adjustments as needed.
