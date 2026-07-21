# Thermodynamic Model of Carbothermal Oxide Reduction

## Problem background
Carbothermal reduction of FeO, CoO, NiO, and Cu₂O by carbon is a longstanding metallurgical process. A proposed mechanism suggests that the oxide decomposes via dissociative evaporation: the oxide separates into gaseous products while the low-volatile metal simultaneously condenses at the oxide/metal interface. Part of the condensation energy is transferred back to the reactant, accelerating the decomposition. This thermodynamic model can, in principle, predict the initial temperature at which decomposition begins, the activation energy for different evaporation regimes, and the equilibrium partial pressures of metal vapour and oxygen. Your task is to implement this dissociative-evaporation model with condensation-energy transfer and compute these quantities, then compare the results with the experimental reference data provided.

## Approach
The model extends Hertz–Langmuir evaporation theory to dissociative evaporation of a compound

```
S(s) → a A(g) + b B(g)                                         (9)
```

For the oxides considered:

- FeO, CoO, NiO: a = 1, b = ½  (oxide → M(g) + ½ O₂)
- Cu₂O: a = 2, b = ½            (Cu₂O → 2 Cu(g) + ½ O₂)

### Flux and partial pressure equations
The effusion flux of product A is given by

```
J_A = γ M P_A / (2π M_A R T)^{1/2}                             (10)
```

where M and M_A are the molar masses of the reactant oxide and product A, γ = 101325 Pa atm⁻¹ is the conversion factor, and R = 8.314 J mol⁻¹ K⁻¹.  The molar mass of the gaseous product B is M_B; values for all relevant species are listed in Section **Molar masses for flux calculations**.

The hypothetical equilibrium partial pressure of product A depends on the evaporation mode.

**Equimolar mode** (no excess of any product in the gas phase)

```
P_A^e = a (K_p / F)^{1/v} (M_A / M_B)^{b/(2v)}
       = (a / F^{1/v}) (M_A / M_B)^{b/(2v)} exp(Δ_r S_T⁰ / (v R)) exp(-Δ_r H_T⁰ / (v R T))   (11)
where
F = a^a × b^b                                            (12)
v = a + b                                                (13)
K_p = P_A^a · P_B^b                                      (14)
```

**Isobaric mode** (one gaseous product, here O₂, is maintained at a constant external pressure P_B′)

```
P_A^i = K_p^{1/a} / (P_B′)^{b/a}
      = 1 / (P_B′)^{b/a} exp(Δ_r S_T⁰ / (a R)) exp(-Δ_r H_T⁰ / (a R T))   (15)
```

### Activation energies
For the equimolar and isobaric modes the activation energies are

```
E_a^e = Δ_r H_T⁰ / v                                       (16)
E_a^i = Δ_r H_T⁰ / a                                       (17)
```

### Condensation energy transfer
When the low-volatile product (metal vapour) condenses, a fraction τ = 0.5 of the condensation energy is transferred back to the reactant. This modifies the reaction enthalpy according to

```
Δ_r H_T⁰ = a ΔH_T⁰(A) + b ΔH_T⁰(B) − ΔH_T⁰(S) + τ a Δ_c H_T⁰(A)   (18)
```

where Δ_c H_T⁰(A) is the condensation enthalpy of A, which equals −Δ_r H_T⁰ of the metal evaporation reaction M(s) → M(g). The values of Δ_r H_T⁰ for metal evaporation are given in the thermodynamic constants table.

### Thermodynamic data
All required thermodynamic functions (Δ_r H_T⁰ in kJ mol⁻¹, Δ_r S_T⁰ in J mol⁻¹ K⁻¹) are tabulated below at 1000, 1300, and 1600 K (Cu species at 1500 instead of 1600). Interpolation may be used for intermediate temperatures; however, the calculations can be performed using the 1300 K values for FeO, CoO, NiO and the 1500 K values for Cu₂O without noticeable loss of accuracy for the required outputs.

### Experimental reference file
A bundled CSV file **experimental_reference.csv** is provided at the path `/home/user/experimental_reference.csv`. It contains the experimental values from the paper (Tables 2 and 5) that must be copied into the output tables. The file has the following columns:

- `Oxide` – e.g., FeO, CoO, NiO, Cu2O
- `T_expt_vacuum_K` – experimental initial decomposition temperature under vacuum (K); blank if absent
- `T_expt_1atm_Ar_K` – experimental initial decomposition temperature under 1 atm Ar (K); blank if absent
- `T_K` – temperature for Knudsen-cell measurements (K); blank for initial-temperature rows
- `P_O2_experimental_atm` – experimental oxygen pressure from Knudsen cell (atm); blank if unavailable

Rows without a `T_K` value belong to the initial temperature table; rows with a `T_K` correspond to equilibrium pressure data. Load this file and merge the appropriate columns into your output.

## Reproduction target
Using the supplied thermodynamic constants and the dissociative evaporation model with τ = 0.5:

1. Compute the theoretical initial decomposition temperature for each oxide under an oxygen partial pressure of 1×10⁻⁷ atm. Merge the computed temperatures with the experimental values from the bundled experimental-reference CSV file and write the full table to `/app/outputs/initial_temperatures.csv`.

2. Calculate the activation energies for the equimolar and isobaric modes for FeO, the equimolar mode for NiO, and the equimolar mode for Cu₂O. Output the results as `/app/outputs/activation_energies.csv`.

3. Evaluate the equilibrium metal-vapour pressures for gaseous dissociation of each oxide and for evaporation of the corresponding metal at 1700 K (FeO, CoO, NiO) and at 1500 K and 1300 K (Cu₂O). Then compute the equilibrium oxygen partial pressure for the condensate dissociation MO(s) → M(s) + ½ O₂ at the same temperatures, and merge with the experimental Knudsen-cell oxygen pressures from the bundled experimental-reference CSV. Save this table as `/app/outputs/equilibrium_pressures.csv`.

## Assets

- Experimental reference CSV at `/home/user/experimental_reference.csv`
- Python 3: python3

## Thermodynamic constants

The following thermodynamic functions are used in all calculations.  
Values of ΔrH_T^0 (kJ mol⁻¹) and ΔrS_T^0 (J mol⁻¹ K⁻¹) are given at 1000 K, 1300 K, and 1600 K (except Cu species at 1500 K).

| Reaction | ΔrH (1000 K) | ΔrH (1300 K) | ΔrH (1600 K) | ΔrS (1000 K) | ΔrS (1300 K) | ΔrS (1600 K) |
|----------|--------------|--------------|--------------|--------------|--------------|--------------|
| Fe (s) = Fe (g) | 409.5 | 402.1 | 398.0 | 143.4 | 136.7 | 131.0 |
| FeO (s) = Fe (g) + ½ O₂ | 675.7 | 669.4 | 662.6 | 205.2 | 199.7 | 195.0 |
| FeO (s) = Fe (s) + ½ O₂ | 266.1 | 267.4 | 264.6 | 61.8 | 63.0 | 64.1 |
| Co (s) = Co (g) | 424.5 | 419.9 | 414.7 | 143.8 | 139.7 | 136.1 |
| CoO (s) = Co (g) + ½ O₂ | 662.9 | 659.1 | 654.0 | 213.5 | 210.0 | 206.8 |
| CoO (s) = Co (s) + ½ O₂ | 238.4 | 239.2 | 239.3 | 69.7 | 70.3 | 70.6 |
| Ni (s) = Ni (g) | 424.2 | 421.3 | 417.7 | 144.7 | 142.0 | 139.6 |
| NiO (s) = Ni (g) + ½ O₂ | 663.5 | 659.5 | 653.6 | 230.4 | 226.8 | 223.4 |
| NiO (s) = Ni (s) + ½ O₂ | 239.3 | 238.2 | 236.8 | 85.7 | 84.8 | 83.8 |
| Cu (s) = Cu (g) | 332.8 | 330.8 | 315.8* | 126.2 | 124.0 | 113.1* |
| Cu₂O (s) = 2 Cu (g) + ½ O₂ | 838.8 | 830.5 | 822.8* | 319.2 | 313.5 | 308.3* |
| Cu₂O (s) = 2 Cu (s/l) + ½ O₂ | 172.8 | 168.8 | 187.8* | 66.0 | 65.5 | 82.2* |

*At 1500 K.

## Molar masses for flux calculations

The flux equation (Eq. 10) requires the molar mass of the reactant oxide (M), the metal vapour product (M_A), and gaseous O₂ (M_B).  Use the following values (g mol⁻¹):

| Species | Molar mass (g mol⁻¹) |
|---------|----------------------|
| FeO (s) | 71.844              |
| Fe (g)  | 55.845              |
| CoO (s) | 74.932              |
| Co (g)  | 58.933              |
| NiO (s) | 74.692              |
| Ni (g)  | 58.693              |
| Cu₂O (s)| 143.091             |
| Cu (g)  | 63.546              |
| O₂ (g)  | 31.998              |

These values can be derived from standard atomic weights (Fe 55.845, Co 58.933, Ni 58.693, Cu 63.546, O 15.999) and the stoichiometric formulas of the oxides; they are provided here to remove ambiguity.