#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: condensed_phase_thermodynamic_functions.csv ===
cat > /app/outputs/condensed_phase_thermodynamic_functions.csv <<'FFEOF'
compound,phase,T,neg_Gs_over_T,Hs_over_T,Hs,Ss,Cs
Acrylonitrile,crystals II,10,0.017,0.052,0.52,0.070,0.209
Acrylonitrile,crystals II,12,0.030,0.090,1.08,0.120,0.360
Acrylonitrile,crystals II,14,0.048,0.143,1.99,0.190,0.567
Acrylonitrile,crystals II,16,0.071,0.212,3.38,0.283,0.834
Acrylonitrile,crystals II,18,0.101,0.298,5.37,0.399,1.156
Acrylonitrile,crystals II,20,0.138,0.402,8.03,0.539,1.518
Acrylonitrile,crystals II,25,0.260,0.726,18.14,0.986,2.549
Acrylonitrile,crystals II,30,0.427,1.120,33.59,1.547,3.632
Acrylonitrile,crystals II,35,0.632,1.555,54.43,2.187,4.694
Acrylonitrile,crystals II,40,0.869,2.010,80.39,2.879,5.670
Acrylonitrile,crystals II,45,1.132,2.466,110.97,3.598,6.548
Acrylonitrile,crystals II,50,1.415,2.915,145.75,4.330,7.354
Acrylonitrile,crystals II,60,2.024,3.775,226.50,5.799,8.765
Acrylonitrile,crystals II,70,2.666,4.576,320.35,7.243,9.967
Acrylonitrile,crystals II,80,3.327,5.319,425.5,8.646,11.069
Acrylonitrile,crystals II,90,3.994,6.018,541.6,10.012,12.126
Acrylonitrile,crystals II,100,4.662,6.676,667.6,11.339,13.084
Acrylonitrile,crystals II,110,5.328,7.303,803.3,12.631,14.061
Acrylonitrile,crystals II,120,5.990,7.908,948.9,13.898,15.065
Acrylonitrile,crystals II,130,6.646,8.498,1104.7,15.144,16.106
Acrylonitrile,crystals II,140,7.297,9.080,1271.1,16.377,17.173
Acrylonitrile,crystals II,150,7.943,9.654,1448.1,17.597,18.218
Acrylonitrile,crystals II,160,8.584,10.223,1635.7,18.808,19.332
Acrylonitrile,crystals II,162.50,8.744,10.366,1684.4,19.110,19.638
Acrylonitrile,crystals I,162.50,8.744,12.113,1968.4,20.857,16.878
Acrylonitrile,crystals I,170,9.296,12.337,2097.2,21.632,17.474
Acrylonitrile,crystals I,180,10.009,12.644,2275.9,22.654,18.269
Acrylonitrile,crystals I,189.63,10.676,12.949,2455.5,23.625,19.034
Acrylonitrile,liquid,189.63,10.68,20.80,3944,31.48,24.392
Acrylonitrile,liquid,190,10.71,20.81,3953,31.52,24.394
Acrylonitrile,liquid,200,11.79,20.99,4197,32.78,24.436
Acrylonitrile,liquid,210,12.82,21.15,4442,33.97,24.491
Acrylonitrile,liquid,220,13.80,21.31,4687,35.11,24.576
Acrylonitrile,liquid,230,14.76,21.45,4933,36.21,24.688
Acrylonitrile,liquid,240,15.67,21.59,5181,37.26,24.825
Acrylonitrile,liquid,250,16.56,21.72,5430,38.28,24.985
Acrylonitrile,liquid,260,17.41,21.85,5681,39.26,25.165
Acrylonitrile,liquid,270,18.23,21.98,5933,40.21,25.359
Acrylonitrile,liquid,273.15,18.49,22.02,6013,40.51,25.421
Acrylonitrile,liquid,280,19.04,22.10,6188,41.14,25.563
Acrylonitrile,liquid,290,19.82,22.22,6445,42.04,25.798
Acrylonitrile,liquid,298.15,20.43,22.33,6656,42.76,26.003
Acrylonitrile,liquid,300,20.57,22.35,6704,42.92,26.049
Acrylonitrile,liquid,310,21.31,22.47,6966,43.78,26.303
Acrylonitrile,liquid,320,22.02,22.60,7230,44.62,26.567
Acrylonitrile,liquid,330,22.72,22.72,7497,45.44,26.841
Acrylonitrile,liquid,340,23.40,22.84,7767,46.24,27.128
Acrylonitrile,liquid,350,24.06,22.97,8040,47.03,27.430
Acrylonitrile,liquid,360,24.71,23.10,8316,47.81,27.750
1-Aminopropane,crystals,10,0.023,0.069,0.69,0.092,0.275
1-Aminopropane,crystals,12,0.040,0.119,1.42,0.158,0.469
1-Aminopropane,crystals,14,0.063,0.187,2.61,0.249,0.726
1-Aminopropane,crystals,16,0.093,0.273,4.36,0.366,1.033
1-Aminopropane,crystals,18,0.131,0.376,6.76,0.507,1.371
1-Aminopropane,crystals,20,0.177,0.493,9.86,0.670,1.738
1-Aminopropane,crystals,25,0.323,0.841,21.03,1.164,2.744
1-Aminopropane,crystals,30,0.511,1.244,37.33,1.756,3.776
1-Aminopropane,crystals,35,0.735,1.679,58.77,2.415,4.797
1-Aminopropane,crystals,40,0.989,2.131,85.22,3.120,5.768
1-Aminopropane,crystals,45,1.266,2.585,116.33,3.851,6.666
1-Aminopropane,crystals,50,1.562,3.036,151.82,4.598,7.522
1-Aminopropane,crystals,60,2.194,3.917,235.03,6.111,9.092
1-Aminopropane,crystals,70,2.861,4.757,332.98,7.618,10.458
1-Aminopropane,crystals,80,3.549,5.547,443.7,9.095,11.682
1-Aminopropane,crystals,90,4.246,6.293,566.3,10.538,12.814
1-Aminopropane,crystals,100,4.945,6.995,699.5,11.940,13.795
1-Aminopropane,crystals,110,5.643,7.656,842.1,13.299,14.744
1-Aminopropane,crystals,120,6.337,8.286,994.2,14.622,15.676
1-Aminopropane,crystals,130,7.024,8.889,1155.5,15.913,16.571
1-Aminopropane,crystals,140,7.704,9.470,1325.7,17.174,17.472
1-Aminopropane,crystals,150,8.377,10.034,1505.0,18.410,18.402
1-Aminopropane,crystals,160,9.042,10.588,1694.0,19.629,19.399
1-Aminopropane,crystals,170,9.700,11.137,1893.3,20.838,20.494
1-Aminopropane,crystals,180,10.352,11.692,2104.5,22.045,21.779
1-Aminopropane,crystals,188.36,10.894,12.165,2291.3,23.059,22.898
1-Aminopropane,liquid,188.36,10.89,26.09,4914,36.98,36.74
1-Aminopropane,liquid,190,11.12,26.18,4974,37.30,36.80
1-Aminopropane,liquid,200,12.47,26.72,5344,39.19,37.13
1-Aminopropane,liquid,210,13.79,27.22,5716,41.01,37.38
1-Aminopropane,liquid,220,15.07,27.69,6091,42.76,37.59
1-Aminopropane,liquid,230,16.31,28.12,6468,44.43,37.78
1-Aminopropane,liquid,240,17.51,28.53,6847,46.04,37.94
1-Aminopropane,liquid,250,18.69,28.91,7227,47.60,38.08
1-Aminopropane,liquid,260,19.83,29.26,7609,49.09,38.22
1-Aminopropane,liquid,270,20.94,29.60,7992,50.54,38.36
1-Aminopropane,liquid,273.15,21.28,29.70,8113,50.98,38.40
1-Aminopropane,liquid,280,22.02,29.91,8376,51.93,38.51
1-Aminopropane,liquid,290,23.08,30.21,8762,53.29,38.68
1-Aminopropane,liquid,298.15,23.92,30.44,9078,54.36,38.84
1-Aminopropane,liquid,300,24.10,30.50,9150,54.60,38.88
1-Aminopropane,liquid,310,25.11,30.77,9540,55.88,39.10
1-Aminopropane,liquid,320,26.09,31.04,9932,57.13,39.36
1-Aminopropane,liquid,330,27.05,31.29,10327,58.34,39.67
1-Aminopropane,liquid,340,27.99,31.54,10726,59.53,40.04
2-Aminopropane,crystals,10,0.046,0.137,1.368,0.183,0.537
2-Aminopropane,crystals,12,0.079,0.231,2.769,0.310,0.879
2-Aminopropane,crystals,14,0.123,0.352,4.934,0.476,1.281
2-Aminopropane,crystals,16,0.179,0.495,7.914,0.674,1.703
2-Aminopropane,crystals,18,0.247,0.653,11.755,0.900,2.140
2-Aminopropane,crystals,20,0.324,0.824,16.478,1.148,2.584
2-Aminopropane,crystals,25,0.557,1.286,32.153,1.843,3.694
2-Aminopropane,crystals,30,0.834,1.776,53.27,2.610,4.734
2-Aminopropane,crystals,35,1.145,2.267,79.35,3.413,5.688
2-Aminopropane,crystals,40,1.480,2.749,109.97,4.229,6.538
2-Aminopropane,crystals,45,1.830,3.213,144.57,5.043,7.291
2-Aminopropane,crystals,50,2.192,3.656,182.79,5.848,7.989
2-Aminopropane,crystals,60,2.933,4.485,269.11,7.418,9.254
2-Aminopropane,crystals,70,3.682,5.248,367.3,8.931,10.369
2-Aminopropane,crystals,80,4.430,5.954,476.3,10.384,11.424
2-Aminopropane,crystals,90,5.170,6.620,595.7,11.790,12.455
2-Aminopropane,crystals,100,5.900,7.251,725.1,13.152,13.415
2-Aminopropane,crystals,110,6.620,7.856,864.2,14.476,14.403
2-Aminopropane,crystals,120,7.329,8.443,1013.1,15.772,15.392
2-Aminopropane,crystals,130,8.027,9.017,1172.2,17.045,16.428
2-Aminopropane,crystals,140,8.716,9.585,1341.8,18.301,17.516
2-Aminopropane,crystals,150,9.397,10.152,1522.8,19.549,18.697
2-Aminopropane,crystals,160,10.071,10.727,1716.3,20.798,20.034
2-Aminopropane,crystals,170,10.739,11.320,1924.4,22.059,21.639
2-Aminopropane,crystals,177.99,11.270,11.812,2102.4,23.082,22.974
2-Aminopropane,liquid,177.99,11.27,21.64,3853,32.91,34.95
2-Aminopropane,liquid,180,11.52,21.79,3923,33.31,35.09
2-Aminopropane,liquid,190,12.71,22.51,4277,35.22,35.74
2-Aminopropane,liquid,200,13.88,23.19,4637,37.07,36.30
2-Aminopropane,liquid,210,15.03,23.82,5003,38.85,36.78
2-Aminopropane,liquid,220,16.15,24.42,5373,40.57,37.19
2-Aminopropane,liquid,230,17.25,24.98,5747,42.23,37.53
2-Aminopropane,liquid,240,18.33,25.51,6123,43.84,37.80
2-Aminopropane,liquid,250,19.38,26.01,6503,45.39,38.04
2-Aminopropane,liquid,260,20.40,26.48,6884,46.88,38.26
2-Aminopropane,liquid,270,21.41,26.92,7268,48.33,38.48
2-Aminopropane,liquid,273.15,21.73,27.05,7389,48.78,38.55
2-Aminopropane,liquid,280,22.40,27.33,7654,49.73,38.70
2-Aminopropane,liquid,290,23.37,27.73,8042,51.10,38.94
2-Aminopropane,liquid,298.15,24.14,28.04,8360,52.18,39.16
2-Aminopropane,liquid,300,24.31,28.11,8433,52.42,39.21
2-Aminopropane,liquid,310,25.24,28.47,8826,53.71,39.50
2-Aminopropane,liquid,320,26.15,28.82,9223,54.97,39.82
2-Methyl-2-aminopropane,crystals III,10,0.050,0.149,1.49,0.198,0.588
2-Methyl-2-aminopropane,crystals III,12,0.085,0.253,3.03,0.339,0.979
2-Methyl-2-aminopropane,crystals III,14,0.134,0.391,5.47,0.525,1.463
2-Methyl-2-aminopropane,crystals III,16,0.197,0.558,8.92,0.755,1.996
2-Methyl-2-aminopropane,crystals III,18,0.274,0.748,13.47,1.022,2.554
2-Methyl-2-aminopropane,crystals III,20,0.363,0.957,19.14,1.320,3.119
2-Methyl-2-aminopropane,crystals III,25,0.637,1.530,38.24,2.167,4.510
2-Methyl-2-aminopropane,crystals III,30,0.969,2.133,63.98,3.102,5.756
2-Methyl-2-aminopropane,crystals III,35,1.343,2.730,95.54,4.073,6.844
2-Methyl-2-aminopropane,crystals III,40,1.745,3.304,132.16,5.050,7.779
2-Methyl-2-aminopropane,crystals III,45,2.166,3.847,173.11,6.013,8.586
2-Methyl-2-aminopropane,crystals III,50,2.598,4.359,217.96,6.958,9.346
2-Methyl-2-aminopropane,crystals III,60,3.478,5.309,318.54,8.788,10.787
2-Methyl-2-aminopropane,crystals III,70,4.364,6.196,433.7,10.560,12.260
2-Methyl-2-aminopropane,crystals III,80,5.248,7.059,564.7,12.307,13.997
2-Methyl-2-aminopropane,crystals III,90,6.130,7.934,714.0,14.063,15.879
2-Methyl-2-aminopropane,crystals III,91.30,6.244,8.049,734.8,14.293,16.138
2-Methyl-2-aminopropane,crystals II,91.30,6.244,8.346,761.9,14.590,14.364
2-Methyl-2-aminopropane,crystals II,100,7.029,8.904,890.4,15.933,15.178
2-Methyl-2-aminopropane,crystals II,110,7.907,9.525,1047.7,17.432,16.313
2-Methyl-2-aminopropane,crystals II,120,8.762,10.140,1216.7,18.902,17.495
2-Methyl-2-aminopropane,crystals II,130,9.598,10.752,1397.7,20.349,18.690
2-Methyl-2-aminopropane,crystals II,140,10.417,11.362,1590.6,21.779,19.904
2-Methyl-2-aminopropane,crystals II,150,11.222,11.972,1795.8,23.194,21.129
2-Methyl-2-aminopropane,crystals II,160,12.014,12.584,2013.3,24.597,22.399
2-Methyl-2-aminopropane,crystals II,170,12.795,13.200,2243.9,25.995,23.734
2-Methyl-2-aminopropane,crystals II,180,13.567,13.826,2488.6,27.393,25.231
2-Methyl-2-aminopropane,crystals II,190,14.332,14.471,2749.6,28.803,26.999
2-Methyl-2-aminopropane,crystals II,200,15.091,15.148,3029.5,30.239,29.070
2-Methyl-2-aminopropane,crystals II,202.27,15.263,15.307,3096.1,30.570,29.584
2-Methyl-2-aminopropane,crystals I,202.27,15.26,22.46,4543,37.72,39.94
2-Methyl-2-aminopropane,crystals I,206.20,15.70,22.79,4699,38.49,40.24
2-Methyl-2-aminopropane,liquid,206.20,15.70,23.81,4910,39.51,42.30
2-Methyl-2-aminopropane,liquid,220,17.28,25.00,5501,42.28,43.23
2-Methyl-2-aminopropane,liquid,230,18.41,25.81,5936,44.22,43.74
2-Methyl-2-aminopropane,liquid,240,19.52,26.57,6376,46.09,44.13
2-Methyl-2-aminopropane,liquid,250,20.62,27.28,6819,47.90,44.46
2-Methyl-2-aminopropane,liquid,260,21.71,27.94,7265,49.65,44.73
2-Methyl-2-aminopropane,liquid,270,22.77,28.57,7714,51.34,44.99
2-Methyl-2-aminopropane,liquid,273.15,23.10,28.76,7855,51.86,45.08
2-Methyl-2-aminopropane,liquid,280,23.82,29.16,8165,52.98,45.27
2-Methyl-2-aminopropane,liquid,290,24.85,29.72,8619,54.57,45.57
2-Methyl-2-aminopropane,liquid,298.15,25.68,30.16,8992,55.84,45.82
2-Methyl-2-aminopropane,liquid,300,25.87,30.25,9076,56.12,45.88
2-Methyl-2-aminopropane,liquid,310,26.87,30.76,9537,57.63,46.25
2-Methyl-2-aminopropane,liquid,320,27.86,31.25,10002,59.11,46.68
2-Methyl-2-aminopropane,liquid,330,28.82,31.73,10471,60.55,47.14
2-Methyl-2-aminopropane,liquid,340,29.78,32.19,10945,61.97,47.62
FFEOF

# === solve block: ideal_gas_entropy.csv ===
cat > /app/outputs/ideal_gas_entropy.csv <<'FFEOF'
compound,S_ideal_298.15
Acrylonitrile,65.87
1-Aminopropane,77.85
2-Aminopropane,74.66
2-Methyl-2-aminopropane,78.33
FFEOF

# === solve block: ideal_gas_functions_acrylonitrile.csv ===
cat > /app/outputs/ideal_gas_functions_acrylonitrile.csv <<'FFEOF'
T,neg_G_over_T,H_over_T,S,Cp,ΔH_f°,ΔG_f°,log_K_f
0,0,0,0,0,45.4,45.4,Inf
200,50.68,9.64,60.33,12.32,44.3,45.6,-49.8
298.15,54.79,11.02,65.80,15.34,43.9,46.3,-33.9
300,54.86,11.04,65.90,15.40,43.9,46.3,-33.7
400,58.23,12.51,70.74,18.37,43.4,47.1,-25.8
500,61.18,13.95,75.13,20.93,43.0,48.1,-21.0
600,63.84,15.29,79.13,23.07,42.7,49.2,-17.9
700,66.30,16.54,82.84,24.87,42.4,50.3,-15.7
800,68.58,17.68,86.26,26.41,42.2,51.4,-14.0
900,70.72,18.72,89.44,27.72,42.0,52.6,-12.8
1000,72.75,19.68,92.43,28.86,41.8,53.7,-11.7
FFEOF
