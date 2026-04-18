import simplekml
from pyproj import Transformer

# 1. Define Boundaries (Corrected EPSG 4326)
# Boundaries


top_left = (44.209566, -92.698294)
bottom_right = (43.819472, -92.058010)

cols = 32
rows = 27

# 2. Setup Transformers
to_utm = Transformer.from_crs("epsg:4326", "epsg:26915", always_xy=True)
to_wgs84 = Transformer.from_crs("epsg:26915", "epsg:4326", always_xy=True)

# Convert corners to meters
west_m, north_m = to_utm.transform(top_left[1], top_left[0])
east_m, south_m = to_utm.transform(bottom_right[1], bottom_right[0])

# 3. Calculate steps in meters
# We take the absolute distance and divide by number of cells
width_m = abs(east_m - west_m)
height_m = abs(north_m - south_m)

lon_step_m = width_m / cols
lat_step_m = height_m / rows

kml = simplekml.Kml()
row_labels = [" "] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# 4. Generate the Grid (Moving SOUTH and EAST from top-left)
for r in range(rows):
    for c in range(cols):
        # Calculate cell corners in meters relative to TOP-LEFT
        # To move South, we SUBTRACT from North
        m_north = north_m - (r * lat_step_m)
        m_south = north_m - ((r + 1) * lat_step_m)
        
        # To move East, we ADD to West
        m_west = west_m + (c * lon_step_m)
        m_east = west_m + ((c + 1) * lon_step_m)
        
        # Convert back to Lat/Lon
        sw_lon, sw_lat = to_wgs84.transform(m_west, m_south)
        se_lon, se_lat = to_wgs84.transform(m_east, m_south)
        ne_lon, ne_lat = to_wgs84.transform(m_east, m_north)
        nw_lon, nw_lat = to_wgs84.transform(m_west, m_north)
        
        label = f"{row_labels[r]}{c+1}"
        pol = kml.newpolygon(name=label)
        pol.outerboundaryis = [(nw_lon, nw_lat), (ne_lon, ne_lat), 
                               (se_lon, se_lat), (sw_lon, sw_lat), 
                               (nw_lon, nw_lat)]
        
        pol.style.polystyle.color = '22ffffff' # Very faint white fill
        pol.style.linestyle.color = 'cc0000aa' # Bright red border
        pol.style.linestyle.width = 1

kml.save("fixed_direction_grid.kml")
print("KML generated: Grid now moves South and East from origin.")