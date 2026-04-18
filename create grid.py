import simplekml

# Boundaries
north = 44.209566
south = 43.819472
west = -92.698294
east = -92.058010

cols = 32
rows = 27  

lat_step = (north - south) / rows
lon_step = (east - west) / cols

kml = simplekml.Kml()
row_labels = [" "] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Longitude overrides for Row Y
y1_left_side_lon = -92.68933   
y13_right_side_lon = -92.44899 

for r in range(rows):
    row_letter = row_labels[r]
    
    for c in range(cols):
        col_num = c + 1
        
        # --- REMOVAL CRITERIA ---
        
        # 1. Remove Column 1 for all rows up to Row X (index 24)
        if col_num == 1 and r <= 24:
            continue

        # 2. Remove the entire VERY TOP row (the empty label row)
        if r == 0:
            continue

        # 3. Remove A20 down to F32
        # (Row index 1 is A, index 6 is F)
        if 1 <= r <= 6 and col_num >= 20:
            continue
            
        # 4. Remove Row Y columns 14-32
        if row_letter == 'Y' and col_num >= 14:
            continue
            
        # 5. Remove all of Row Z
        if row_letter == 'Z':
            continue
        
        # ------------------------

        # Base Coordinate Calculation
        c_north = north - (r * lat_step)
        c_south = north - ((r + 1) * lat_step)
        c_west = west + (c * lon_step)
        c_east = west + ((c + 1) * lon_step)
        
        current_west_lon = c_west
        current_east_lon = c_east

        # Modify Longitudes for Y1 and Y13
        if row_letter == 'Y':
            if col_num == 1:
                current_west_lon = y1_left_side_lon
            elif col_num == 13:
                current_east_lon = y13_right_side_lon
        
        # Create Polygon
        label = f"{row_letter.strip()}{col_num}"
        pol = kml.newpolygon(name=label)
        
        pol.outerboundaryis = [
            (current_west_lon, c_north), 
            (current_east_lon, c_north), 
            (current_east_lon, c_south), 
            (current_west_lon, c_south), 
            (current_west_lon, c_north)
        ]
        
        pol.style.polystyle.color = '22ffffff' 
        pol.style.linestyle.color = 'ff0000ff' 
        pol.style.linestyle.width = 1

kml.save("Olmsted County Emergency Grid Map.kml")
print("KML created: A2-F19 are now present; A20-F32 and Top Row are removed.")