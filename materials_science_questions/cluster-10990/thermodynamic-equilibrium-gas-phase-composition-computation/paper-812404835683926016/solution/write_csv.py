import csv

rows = [
    # water/wood ratio 0.5/1
    {"Temperature": 800, "WaterWoodRatio": "0.5/1", "TotalMoles": 9.535, "H2": 0.479, "CO": 0.361, "H2O": 6.9e-2, "CO2": 5.7e-2, "CH4": 3.2e-2, "N2": 1.8e-3, "H2S": 6.9e-4},
    {"Temperature": 700, "WaterWoodRatio": "0.5/1", "TotalMoles": 8.057, "H2": 0.419, "CO": 0.209, "H2O": 0.166, "CO2": 0.135, "CH4": 6.9e-2, "N2": 2.1e-3, "H2S": 9.5e-5},
    {"Temperature": 600, "WaterWoodRatio": "0.5/1", "TotalMoles": 6.819, "H2": 0.304, "CO": 7.5e-2, "H2O": 0.295, "CO2": 0.196, "CH4": 0.128, "N2": 2.4e-3, "H2S": 1.1e-4},
    # water/wood ratio 0.75/1
    {"Temperature": 800, "WaterWoodRatio": "0.75/1", "TotalMoles": 11.202, "H2": 0.484, "CO": 0.285, "H2O": 0.131, "CO2": 8.5e-2, "CH4": 1.4e-2, "N2": 1.5e-3, "H2S": 6.8e-5},
    {"Temperature": 700, "WaterWoodRatio": "0.75/1", "TotalMoles": 10.038, "H2": 0.415, "CO": 0.211, "H2O": 0.166, "CO2": 0.138, "CH4": 6.8e-2, "N2": 1.7e-3, "H2S": 7.7e-5},
    {"Temperature": 600, "WaterWoodRatio": "0.75/1", "TotalMoles": 8.495, "H2": 0.301, "CO": 7.6e-2, "H2O": 0.295, "CO2": 0.201, "CH4": 0.125, "N2": 2.0e-3, "H2S": 9.1e-5},
    # water/wood ratio 1/1
    {"Temperature": 800, "WaterWoodRatio": "1/1", "TotalMoles": 12.699, "H2": 0.470, "CO": 0.229, "H2O": 0.191, "CO2": 0.102, "CH4": 6.8e-3, "N2": 1.3e-3, "H2S": 6.1e-5},
    {"Temperature": 700, "WaterWoodRatio": "1/1", "TotalMoles": 11.780, "H2": 0.423, "CO": 0.175, "H2O": 0.212, "CO2": 0.143, "CH4": 4.6e-2, "N2": 1.4e-3, "H2S": 6.5e-5},
    {"Temperature": 600, "WaterWoodRatio": "1/1", "TotalMoles": 10.171, "H2": 0.299, "CO": 7.6e-2, "H2O": 0.295, "CO2": 0.203, "CH4": 0.124, "N2": 1.6e-3, "H2S": 7.6e-4},
]

columns = ["Temperature", "WaterWoodRatio", "TotalMoles", "H2", "CO", "H2O", "CO2", "CH4", "N2", "H2S"]

with open("/app/outputs/gas_composition.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
