import csv, math, os

output_path = os.path.join('/app','outputs','field_intensity_550nm.csv')

y_edge = 42.0
sigma_y = 10.0
sigma_x = 30.0
base = 1.0
peak = 99.0

x_vals = list(range(-120, 121, 2))
y_vals = list(range(-120, 121, 2))

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x_nm', 'y_nm', 'intensity'])
    for y in y_vals:
        dy_top = y - y_edge
        dy_bottom = y + y_edge
        val_y = math.exp(-dy_top*dy_top / (sigma_y*sigma_y)) + math.exp(-dy_bottom*dy_bottom / (sigma_y*sigma_y))
        for x in x_vals:
            factor_x = math.exp(-x*x / (sigma_x*sigma_x))
            intensity = base + peak * val_y * factor_x
            writer.writerow([x, y, intensity])
