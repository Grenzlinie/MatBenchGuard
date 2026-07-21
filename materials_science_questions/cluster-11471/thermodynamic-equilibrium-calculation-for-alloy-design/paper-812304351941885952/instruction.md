# Carbon Potential and Equilibrium Atmosphere Calculation for Carburizing

## Problem background
In gas carburizing and cyaniding of steel parts, uncontrolled carbon potential in the furnace atmosphere can lead to the deposition of carbon black and the formation of carbide networks in the surface layer, which seriously degrades mechanical properties. This work analyzes why, under the same treatment regime in a multi‑zone continuous furnace, carbides appear in some steels but not in others. It aims to determine the safe carbon potential range and to compute equilibrium atmosphere compositions that avoid carbide formation.

## Approach
The analysis proceeds in three stages.

### 1. Carbon activity and carbon potential
The carbon activity \(A_C\) in each furnace zone is calculated from the partial pressures (approximated by the volume percentages) of CO, H₂, and H₂O using the water‑gas equilibrium relation:

\[
A_C = \frac{[\mathrm{CO}] \cdot [\mathrm{H_2}]}{100 \cdot [\mathrm{H_2O}] \cdot K}
\tag{1}
\]

where \[[\mathrm{CO}], [\mathrm{H_2}], [\mathrm{H_2O}]\] are the volume percentages of the respective components, and \(K\) is the equilibrium constant of the heterogeneous reaction

\[
\mathrm{CO} + \mathrm{H_2} \rightleftharpoons [\mathrm{C}] + \mathrm{H_2O},
\]

whose values at the three zone temperatures are given in the **Input data** section.

Given \(A_C\) and the furnace temperature \(t\) (in °C), the carbon potential \(C_b\) (the carbon content of unalloyed austenite in equilibrium with the atmosphere, in mass percent) is evaluated by the empirical formula

\[
C_b = \frac{A_C \cdot 100}{1.07 \cdot \exp\!\left(\dfrac{4796.6}{t+273}\right) + 19.5\,A_C}.
\tag{2}
\]

The **carbon‑black deposition boundary** (the limiting carbon potential above which carbon black precipitates in the furnace or carbides form in unalloyed austenite) is defined as the value of \(C_b\) obtained from (2) when \(A_C = 1\).

### 2. Surface carbon concentration and alloying effect
Carbon transfer into the steel is modelled by one‑dimensional diffusion in unalloyed austenite, driven by the difference between the atmosphere carbon potential \(C_b\) and the instantaneous surface carbon content \(C_{\text{surf}}\).

The mass flux at the surface is described by a boundary condition of the third kind:

\[
J = b_t \, \bigl(C_b - C_{\text{surf}}\bigr),
\tag{3}
\]

where \(b_t = 0.2\ \text{mm h}^{-1}\) is the mass‑transfer coefficient (determined experimentally for the Holcroft furnace).

Inside the steel, carbon diffusion obeys Fick’s second law in one dimension, with the diffusion coefficient \(D\) (in \(\text{cm}^2\!/\text{s}\)) given by the Arrhenius relation

\[
D = D_0 \exp\!\left(-\frac{E}{R\,T}\right),
\tag{4}
\]

where \(D_0 = 0.05\ \text{cm}^2\!/\text{s}\), \(E = 121\,000\ \text{J mol}^{-1}\), \(R = 8.314\ \text{J mol}^{-1}\text{K}^{-1}\), and \(T\) is the absolute temperature (in K) of the zone.

**Geometry and initial condition.**  
The steel specimen is a plate of thickness \(2\ \text{mm}\); diffusion occurs symmetrically from both faces. Therefore the simulation can be performed on a half‑thickness domain \(0 \le x \le L\) with \(L = 1\ \text{mm}\).  
At time zero, the carbon concentration is uniform and equal to the nominal carbon content of the steel (\(C_0 = 0.08\ \%\) for steel 08kp, \(C_0 = 0.35\ \%\) for steel 35G2).  
At the outer boundary \(x = 0\) (the surface) the flux is given by (3). At the symmetry plane \(x = L\) the flux is zero (i.e. \(\partial C/\partial x = 0\)).

**Treatment schedule.**  
The parts pass consecutively through three furnace zones, each operating at a fixed temperature \(T_i\) and with a constant carbon potential \(C_{b,i}\) (computed from the zone’s atmosphere). The residence times \(\tau_i\) (in hours) are prescribed. The simulation advances through the zones sequentially: the concentration profile at the end of zone \(i\) serves as the initial condition for zone \(i+1\).  
The final surface carbon concentration of the unalloyed steel, \(C_{\text{surf}}\), is the value at the surface node after completion of the third zone.

**Alloying correction.**  
For alloyed steels the actual surface carbon content \(C_a\) is obtained from the unalloyed value \(C_{\text{surf}}\) by

\[
C_a = \frac{C_{\text{surf}}}{f},
\]

where \(f\) is an experimentally determined alloying coefficient. The paper reports \(f = 0.97\) for steel 35G2 and \(f = 0.99\) for steel 08kp. These values must be used for all regimes and steels.

### 3. Optimum equilibrium atmospheres
Using gas‑equilibrium relations (water‑gas and Boudouard reactions) and the carbon‑potential formula (2), several equilibrium gas compositions are determined that keep the carbon potential within the safe range \(0.75\ \%\ – 0.94\ \%\) at \(820\ \mathrm{°C}\). Each composition is characterised by its carbon activity \(A_C\), carbon potential \(C_b\), and the corresponding dew point \(t_d\) (the dew point is obtained from the H₂O content via the saturation vapour pressure of water at a total pressure of \(1 \times 10^5\ \text{Pa}\)).

## Input data

The numerical values listed below are extracted from the paper and must be used exactly in all computations.  
All gas compositions are given in volume percent (equivalent to partial pressure percentages at \(1 \times 10^5\ \text{Pa}\)).

### Zone operating parameters

| Zone | Temperature (°C) | CO (vol%) | H₂ (vol%) | CO₂ (vol%) | CH₄ (vol%) | H₂O (vol%) | N₂ (vol%) | Dew point (°C) | Hold time τ (h) |
|------|-------------------|-----------|-----------|------------|------------|------------|-----------|----------------|-------------------|
| 1    | 810               | 12.0      | 15.0      | 0.20       | 5.3        | 0.228      | 67.272    | -11            | 0.83333           |
| 2    | 830               | 15.0      | 16.0      | 0.22       | 5.35       | 0.256      | 63.174    | -14            | 0.50              |
| 3    | 820               | 17.2      | 18.0      | 0.18       | 5.6        | 0.189      | 58.831    | -15            | 0.33333           |

The H₂O content has been computed from the dew point using the saturation vapour pressure of water at the total pressure \(1 \times 10^5\ \text{Pa}\); the N₂ content is obtained as the balance to 100 %. The hold times for zones 1 and 2 are the same in all regimes; the hold time for zone 3 may differ depending on the regime (see **Cyaniding regimes** below).

### Equilibrium constants

- Water‑gas reaction \(\mathrm{CO} + \mathrm{H_2} \rightleftharpoons [\mathrm{C}] + \mathrm{H_2O}\):
  - \(K = 10.25\) at \(810\ \mathrm{°C}\)
  - \(K = 10.36\) at \(820\ \mathrm{°C}\)
  - \(K = 11.85\) at \(830\ \mathrm{°C}\)
- Boudouard reaction \(2\mathrm{CO} \rightleftharpoons \mathrm{CO_2} + [\mathrm{C}]\):
  - \(K = 10.337\) at \(820\ \mathrm{°C}\)

### Mass‑transfer coefficient
\[
b_t = 0.2\ \text{mm h}^{-1}
\]

### Diffusion parameters (carbon in austenite)
\[
D_0 = 0.05\ \text{cm}^2\!/\text{s},\qquad E = 121\,000\ \text{J mol}^{-1},\qquad R = 8.314\ \text{J mol}^{-1}\text{K}^{-1}
\]

### Steel compositions

| Steel | Initial C (%) | Si (%) | Mn (%) | Ni (%) | Cr (%) |
|-------|---------------|--------|--------|--------|--------|
| 08kp  | 0.08          | 0.03   | 0.305  | 0      | 0      |
| 35G2  | 0.35          | 0.29   | 1.50   | 0      | 0      |

### Cyaniding regimes

**Actual regime** – the hold times are exactly those given in the zone table; the carbon potential in each zone is the one computed from the zone’s atmosphere using Eq. (1) and (2).

**Calculated regime** – for steel 35G2: zone 1 and 2 as in the actual regime, zone 3 hold time = 0.33 h and its carbon potential is set to \(1.20\ \%\). For steel 08kp: zone 1 and 2 as in the actual regime, zone 3 hold time = 0.50 h and its carbon potential remains at the actual value (i.e. the value computed from the zone‑3 atmosphere).

### Alloying coefficients
- \(f = 0.97\) for steel 35G2
- \(f = 0.99\) for steel 08kp

## Workflow steps

### Step 1: Compute carbon‑black boundaries and actual carbon potentials
- **Role:** scored
- **Action:** Using the gas compositions, zone temperatures, and equilibrium constants \(K\) from the **Input data** section, compute for each furnace zone:
  - the carbon deposition boundary \(C_b\) at \(A_C = 1\) (using Eq. (2));
  - the actual carbon activity \(A_C\) (Eq. (1));
  - the actual carbon potential \(C_b\) (Eq. (2)).
- Write the results to a CSV file.
- **Output file:** `/app/outputs/table2_results.csv`
- **Format:** csv
- **Schema:** `zone` (int), `temperature_C` (float), `boundary_Cb` (float), `A_C` (float), `C_b` (float).

### Step 2: Compute surface carbon concentrations for unalloyed and alloyed steels
- **Role:** scored (load‑bearing)
- **Action:** Perform one‑dimensional diffusion simulations as described in Section 2 of the **Approach** for both steels (initial carbon 0.08 % and 0.35 %) under both the **Actual** and **Calculated** cyaniding regimes. For each simulation:
  - Use the appropriate zone temperatures, carbon potentials, and hold times.
  - Apply the mass‑transfer boundary condition (3) and the Arrhenius diffusion coefficient (4) at each zone temperature.
  - After the final zone, record the surface carbon concentration \(C_{\text{surf}}\).
  - Compute the alloyed surface carbon content \(C_a = C_{\text{surf}} / f\) using the appropriate \(f\).
  - Record the alloying coefficient \(f\) itself.
- The numerical method (e.g. finite differences) must be implemented by you; the results must correspond to the mathematical model described above.
- **Output file:** `/app/outputs/table3_results.csv`
- **Format:** csv
- **Schema:** `steel` (string), `regime` (string), `C_surf` (float), `C_a` (float), `f` (float).

### Step 3: Compute optimum equilibrium atmosphere compositions
- **Role:** scored
- **Action:** Using the gas‑equilibrium relations (water‑gas and Boudouard equilibria) together with Eq. (2) for the carbon potential, determine six equilibrium atmosphere compositions at \(820\ \mathrm{°C}\) that yield a carbon potential in the range \(0.75\ \%\ – 0.94\ \%\). For each composition, compute the corresponding carbon activity \(A_C\), carbon potential \(C_b\), and dew point \(t_d\).
- **Output file:** `/app/outputs/table5_results.json`
- **Format:** json (array of 6 objects)
- **Schema (each object):** `atmosphere` (int), `CO` (float), `CO2` (float), `CH4` (float), `H2` (float), `H2O` (float), `N2` (float), `A_C` (float), `C_b` (float), `t_d` (float).

## Output files

Write all result files under `/app/outputs`:

| File | Purpose | Format |
|------|---------|--------|
| `table2_results.csv` | scored – zone carbon boundaries and potentials | csv |
| `table3_results.csv` | scored – surface carbon concentrations (unalloyed/alloyed) | csv |
| `table5_results.json`| scored – optimum equilibrium atmospheres | json |

The exact schemas are repeated below for easy machine reading.

### table2_results.csv
- **required columns:** `zone`, `temperature_C`, `boundary_Cb`, `A_C`, `C_b`
- **units:** temperature in °C, `boundary_Cb` and `C_b` in mass percent, `A_C` dimensionless.

### table3_results.csv
- **required columns:** `steel`, `regime`, `C_surf`, `C_a`, `f`
- **units:** `C_surf` and `C_a` in mass percent, `f` dimensionless.

### table5_results.json
JSON array of six objects. Each object must contain the keys:
`atmosphere`, `CO`, `CO2`, `CH4`, `H2`, `H2O`, `N2`, `A_C`, `C_b`, `t_d`.
- All gas fractions in volume percent, `A_C` dimensionless, `C_b` in mass percent, `t_d` in °C.

## Self‑check (optional, not scored)

```json
{
  "outputs": [
    {
      "file": "table2_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["zone", "temperature_C", "boundary_Cb", "A_C", "C_b"],
        "units": {
          "temperature_C": "degree Celsius",
          "boundary_Cb": "percent",
          "A_C": "dimensionless",
          "C_b": "percent"
        }
      },
      "description": "Reproduce the computed carbon black deposition boundary (at A_C=1) and the actual carbon activity and potential for each of the three furnace zones."
    },
    {
      "file": "table3_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["steel", "regime", "C_surf", "C_a", "f"],
        "units": {
          "C_surf": "percent",
          "C_a": "percent",
          "f": "dimensionless"
        }
      },
      "description": "Reproduce the computed surface carbon concentrations for unalloyed (C_surf) and alloyed (C_a) steels under the actual and calculated cyaniding regimes, together with the alloying coefficient f."
    },
    {
      "file": "table5_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["atmosphere", "CO", "CO2", "CH4", "H2", "H2O", "N2", "A_C", "C_b", "t_d"],
          "units": {
            "CO": "percent",
            "CO2": "percent",
            "CH4": "percent",
            "H2": "percent",
            "H2O": "percent",
            "N2": "percent",
            "A_C": "dimensionless",
            "C_b": "percent",
            "t_d": "degree Celsius"
          }
        }
      },
      "description": "Reproduce six optimum equilibrium atmosphere compositions that yield a carbon potential between 0.75% and 0.94% at 820°C, together with their carbon activity, carbon potential, and dew point."
    }
  ],
  "notes": "The verifier recomputes the required quantities from the public inputs using the same thermodynamic formulas and diffusion equations, and compares the agent's reported values to the expected values within appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes the thermodynamic and diffusion quantities from the same input data and compares your output values against reference values. For each numeric field in the three output files the verifier checks whether your computed value matches the expected value within predetermined tolerances. The