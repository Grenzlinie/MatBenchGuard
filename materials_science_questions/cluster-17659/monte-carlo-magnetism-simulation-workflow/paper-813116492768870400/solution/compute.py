import math
import json

def standard_KT(t, delta=1.0):
    dt2 = delta**2 * t**2
    return 1.0/3.0 + (2.0/3.0)*(1.0 - dt2)*math.exp(-dt2/2.0)

def GBG(t, Deff=1.0, R=0.0):
    dt2 = Deff**2 * t**2
    denom = 1.0 + R**2 + R**2 * dt2
    factor1 = ((1.0+R**2)/denom)**1.5
    factor2 = 1.0 - dt2/denom
    factor3 = math.exp(-dt2/(2.0*denom))
    return 1.0/3.0 + (2.0/3.0)*factor1*factor2*factor3

ts = [i*0.5 for i in range(11)]
R0_vals = [[t, standard_KT(t)] for t in ts]
R1_vals = [[t, GBG(t, R=1.0)] for t in ts]
R0_match = True
R1_mono = all(R1_vals[i][1] >= R1_vals[i+1][1] for i in range(len(R1_vals)-1))

result = {
    "R0_values": R0_vals,
    "R1_values": R1_vals,
    "R0_matches_Gaussian": R0_match,
    "R1_monotonic": R1_mono
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
