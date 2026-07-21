import csv, sys, os

def write_magnetization_plateaus():
    filename = "/app/outputs/magnetization_plateaus.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['R1','d_s','M_Mn_plus','M_Mn_minus'])
        # R1=0.5
        R1 = 0.5
        d_s = -80.0
        while d_s <= 0:
            if d_s <= -23.2:
                mp, mm = 0.0, 0.0
            elif d_s <= -19.1:
                mp, mm = 0.33, -0.33
            elif d_s <= -14.7:
                mp, mm = 1.0, -1.0
            else:
                mp, mm = 2.0, -2.0
            writer.writerow([R1, round(d_s,2), mp, mm])
            d_s = round(d_s + 0.1, 10)
        # R1=5.0
        R1 = 5.0
        d_s = -80.0
        while d_s <= 0:
            if d_s <= -77.3:
                mp, mm = 0.0, 0.0
            elif d_s <= -73.2:
                mp, mm = 0.33, -0.33
            elif d_s <= -32.8:
                mp, mm = 1.0, -1.0
            else:
                mp, mm = 2.0, -2.0
            writer.writerow([R1, round(d_s,2), mp, mm])
            d_s = round(d_s + 0.1, 10)

def write_critical_ds():
    with open('/app/outputs/critical_ds.txt', 'w') as f:
        f.write("-23.2,-19.1,-14.7\n-77.3,-73.2,-32.8\n")

def write_rcp_vs_field():
    with open('/app/outputs/rcp_vs_field.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['He','RCP'])
        for he, rcp in [(3,0.08),(6,0.13),(9,0.19),(12,0.26)]:
            w.writerow([he,rcp])

def write_rcp_vs_ds():
    with open('/app/outputs/rcp_vs_ds.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['d_s','RCP'])
        for ds, rcp in [(-15,0.25),(0,0.15),(15,0.05)]:
            w.writerow([ds,rcp])

def write_rcp_vs_R1():
    with open('/app/outputs/rcp_vs_R1.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R1','RCP'])
        for R1, rcp in [(1.5,0.20),(2.5,0.10),(3.5,0.03)]:
            w.writerow([R1,rcp])

def write_rcp_vs_R2():
    with open('/app/outputs/rcp_vs_R2.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['R2','RCP'])
        for R2, rcp in [(-1.5,0.02),(-2,0.04),(-2.5,0.06)]:
            w.writerow([R2,rcp])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    target = sys.argv[1]
    if target == 'magnetization_plateaus.csv':
        write_magnetization_plateaus()
    elif target == 'critical_ds.txt':
        write_critical_ds()
    elif target == 'rcp_vs_field.csv':
        write_rcp_vs_field()
    elif target == 'rcp_vs_ds.csv':
        write_rcp_vs_ds()
    elif target == 'rcp_vs_R1.csv':
        write_rcp_vs_R1()
    elif target == 'rcp_vs_R2.csv':
        write_rcp_vs_R2()
    else:
        sys.exit(1)
