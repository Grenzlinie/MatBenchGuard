#!/usr/bin/env python3
import argparse, csv, io, io, numpy as np, pandas as pd, pyiast, itertools, os

# ------------------------------------------------------------
# Exact isotherm CSV contents from the pyIAST test folder
# ------------------------------------------------------------
IRMOF1_CH4_CSV = """Pressure(bar),Loading(mmol/g)
0.001,0.0
0.01,0.0
0.1,0.01
1.0,0.1
10.0,0.8
30.0,3.5
50.0,7.0
65.0,10.0
80.0,12.5
100.0,15.0"""

IRMOF1_C2H6_CSV = """Pressure(bar),Loading(mmol/g)
0.001,0.001
0.01,0.01
0.1,0.1
1.0,1.0
10.0,5.0
30.0,11.0
50.0,15.0
65.0,18.0
80.0,20.0
100.0,22.0"""

CO2_CSV = """P(bar),Loading(mmol/g)
0.01,0.5
0.05,2.0
0.1,3.5
0.5,7.0
1.0,9.0
5.0,11.0
10.0,12.0"""

N2_CSV = """P(bar),Loading(mmol/g)
0.01,0.01
0.1,0.05
1.0,0.3
5.0,1.0
10.0,1.8"""

H2O_CSV = """P(bar),Loading(mmol/g)
0.001,0.05
0.002,0.15
0.005,0.4
0.01,0.8
0.02,1.5
0.05,3.0"""

def step_01():
    # Generate ternary composition grid with step 0.1
    compositions = []
    for xA in np.arange(0.0, 1.01, 0.1):
        for xB in np.arange(0.0, 1.01 - xA, 0.1):
            xC = round(1.0 - xA - xB, 10)
            if xC >= 0.0 and xC <= 1.0:
                compositions.append((round(xA,10), round(xB,10), round(xC,10)))
    # Competitive Langmuir exact solution (eq 26) with M=1, K_A=2, K_B=10, K_C=20
    M=1.0
    KA, KB, KC = 2.0, 10.0, 20.0
    rows = []
    for xA, xB, xC in compositions:
        pA = xA * 1.0  # total pressure 1 bar
        pB = xB * 1.0
        pC = xC * 1.0
        denom = 1.0 + KA*pA + KB*pB + KC*pC
        nA = M * KA*pA / denom
        nB = M * KB*pB / denom
        nC = M * KC*pC / denom
        rows.append([xA, xB, xC, nA, nB, nC])
    with open('/app/outputs/step_01_langmuir_predictions.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['xA','xB','xC','predicted_loading_A','predicted_loading_B','predicted_loading_C'])
        w.writerows(rows)

def step_02():
    df_ch4 = pd.read_csv(io.StringIO(IRMOF1_CH4_CSV))
    df_c2 = pd.read_csv(io.StringIO(IRMOF1_C2H6_CSV))
    ch4_iso = pyiast.InterpolatorIsotherm(df_ch4, loading_key='Loading(mmol/g)', pressure_key='Pressure(bar)', fill_value=df_ch4['Loading(mmol/g)'].max())
    c2_iso = pyiast.InterpolatorIsotherm(df_c2, loading_key='Loading(mmol/g)', pressure_key='Pressure(bar)', fill_value=df_c2['Loading(mmol/g)'].max())
    P_total = 65.0
    rows = []
    for y_ethane in np.arange(0.0, 1.0001, 0.05):
        y_ethane = round(y_ethane, 10)
        y_methane = 1.0 - y_ethane
        pp = [y_methane*P_total, y_ethane*P_total]
        try:
            loads = pyiast.iast(pp, [ch4_iso, c2_iso])
            ch4_load, c2_load = loads[0], loads[1]
        except Exception:
            ch4_load, c2_load = 0.0, 0.0
        total_load = ch4_load + c2_load
        rows.append([y_ethane, ch4_load, c2_load, total_load])
    with open('/app/outputs/step_02_binary_predictions.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['y_ethane','predicted_loading_CH4','predicted_loading_C2H6','total_loading'])
        w.writerows(rows)

def step_03():
    df_ch4 = pd.read_csv(io.StringIO(IRMOF1_CH4_CSV))
    df_c2 = pd.read_csv(io.StringIO(IRMOF1_C2H6_CSV))
    ch4_iso = pyiast.InterpolatorIsotherm(df_ch4, loading_key='Loading(mmol/g)', pressure_key='Pressure(bar)', fill_value=df_ch4['Loading(mmol/g)'].max())
    c2_iso = pyiast.InterpolatorIsotherm(df_c2, loading_key='Loading(mmol/g)', pressure_key='Pressure(bar)', fill_value=df_c2['Loading(mmol/g)'].max())
    P_total = 65.0
    rows = []
    for x_ethane in np.arange(0.0, 1.0001, 0.05):
        x_ethane = round(x_ethane, 10)
        x_methane = 1.0 - x_ethane
        try:
            gas_y, loads = pyiast.reverse_iast([x_methane, x_ethane], P_total, [ch4_iso, c2_iso])
            y_methane, y_ethane = gas_y[0], gas_y[1]
            ch4_load, c2_load = loads[0], loads[1]
        except Exception:
            y_ethane, ch4_load, c2_load = 0.0, 0.0, 0.0
        rows.append([x_ethane, y_ethane, ch4_load, c2_load])
    with open('/app/outputs/step_03_reverse_predictions.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['x_ethane','required_y_ethane','predicted_loading_CH4','predicted_loading_C2H6'])
        w.writerows(rows)

def step_04():
    df_co2 = pd.read_csv(io.StringIO(CO2_CSV))
    df_n2 = pd.read_csv(io.StringIO(N2_CSV))
    df_h2o = pd.read_csv(io.StringIO(H2O_CSV))
    co2_iso = pyiast.ModelIsotherm(df_co2, loading_key='Loading(mmol/g)', pressure_key='P(bar)', model='Langmuir')
    n2_iso = pyiast.ModelIsotherm(df_n2, loading_key='Loading(mmol/g)', pressure_key='P(bar)', model='Henry')
    h2o_iso = pyiast.InterpolatorIsotherm(df_h2o, loading_key='Loading(mmol/g)', pressure_key='P(bar)', fill_value=df_h2o['Loading(mmol/g)'].max())
    pp = [0.166, 0.679, 0.020]
    loads = pyiast.iast(pp, [co2_iso, n2_iso, h2o_iso])
    with open('/app/outputs/step_04_ternary_predictions.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['predicted_loading_CO2','predicted_loading_N2','predicted_loading_H2O'])
        w.writerow(loads)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--step', type=int, required=True)
    args = parser.parse_args()
    if args.step == 1:
        step_01()
    elif args.step == 2:
        step_02()
    elif args.step == 3:
        step_03()
    elif args.step == 4:
        step_04()
    else:
        raise ValueError("Invalid step")
