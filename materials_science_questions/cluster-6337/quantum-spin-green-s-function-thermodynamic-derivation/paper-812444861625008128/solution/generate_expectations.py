import csv, random

def main():
    targets = {
        0: [0.4404, 0.0004, 0.0002, -0.0002, 0.0000, 0.0002, -0.0001],
        1: [0.3640, 0.0820, -0.0072, -0.0034, -0.0021, -0.0107, 0.0014],
        2: [0.3538, 0.0955, -0.0094, -0.0042, -0.0024, -0.0146, 0.0011],
        3: [0.3542, 0.0970, -0.0099, -0.0054, -0.0022, -0.0129, 0.0040],
    }
    random.seed(42)
    N = 1000
    with open('/app/outputs/expectations.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["level","class_r","J1_coeff","J2_coeff","J3_coeff","J4_coeff","J5_coeff","J6_coeff","J7_coeff","Xi","sigma"])
        for lvl in range(4):
            J = targets[lvl]
            for i in range(7):
                c = [0.0]*7; c[i]=1.0
                w.writerow([lvl,f"id_{i}"]+c+[round(sum(ci*ji for ci,ji in zip(c,J)),8),1.0])
            for r in range(7, N):
                c = [round(random.gauss(0,1),6) for _ in range(7)]
                w.writerow([lvl,f"r_{r}"]+c+[round(sum(ci*ji for ci,ji in zip(c,J)),8),1.0])
if __name__=="__main__":
    main()
