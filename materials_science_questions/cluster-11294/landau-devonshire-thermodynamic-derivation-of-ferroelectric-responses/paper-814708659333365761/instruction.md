# Landau-Devonshire thermodynamic modeling of ferroelectric thin film dielectric and piezoelectric responses

## Problem background
Ferroelectric thick films, such as PbTiO3, are used in sensors, actuators, and tunable devices. Their dielectric and piezoelectric properties are strongly affected by internal stress. Thermal stress, arising from the mismatch in thermal expansion coefficients between the film and the substrate during deposition and cooling, can dominate in films thicker than the critical thickness where misfit strain relaxes. Understanding how deposition temperature and substrate choice influence polarization, dielectric constant, piezoelectric response, and tunability is essential for optimizing device performance.

## Approach
This work uses a Landau-Devonshire phenomenological thermodynamic model for (001)-oriented PbTiO3 films. The in-plane thermal strain is computed by integrating the difference between the film's and substrate's temperature-dependent thermal expansion coefficients from room temperature to the growth temperature. For substrates with isotropic in-plane thermal expansion (Si, c-sapphire, MgO), the free energy density incorporates the thermal strain through renormalized dielectric stiffness coefficients. For the anisotropically expanding a-sapphire substrate, a modified free energy expression accounts for unequal in-plane strains along the two axes. At each growth temperature, the equilibrium out-of-plane polarization is found by minimizing the free energy. From the equilibrium polarization, the out-of-plane dielectric constant, piezoelectric coefficient, and their field-induced tunabilities (at E=1000 kV/cm) are calculated. The procedure is repeated for four commercially relevant substrates, spanning growth temperatures from 25 °C to 800 °C.

## Model parameters and equations
### Material constants (from the reference paper, Table II)
- Curie–Weiss temperature: T₀ = 479 °C
- Landau coefficients (dielectric stiffness):
  - α₁(T) = 3.8 × 10⁵ (T − T₀) [J·m/C²]   (T in °C)
  - α₁₁ = −7.3 × 10⁷ [J·m⁵/C⁴]
  - α₁₁₁ = 2.6 × 10⁸ [J·m⁹/C⁶]
- Elastic compliances (at constant dielectric displacement):
  - s₁₁ = 8.0 × 10⁻¹² m²/N
  - s₁₂ = −2.5 × 10⁻¹² m²/N
- Electrostrictive coefficients:
  - Q₁₁ = 0.089 m⁴/C²
  - Q₁₂ = −0.026 m⁴/C²
- Permittivity of free space: ε₀ = 8.854 × 10⁻¹² F/m

### Thermal expansion coefficients (Table I)
All values in units of /°C.  T is the temperature in °C.

- PbTiO₃ film (constant):
  α_PTO = 11.86 × 10⁻⁶
- MgO substrate (constant):
  α_MgO = 13.47 × 10⁻⁶
- Si substrate (isotropic in‑plane):
  α_Si(T) = [3.725(1 − exp(−5.88×10³ (T+149))) + 5.548×10⁻⁴ (T+273)] × 10⁻⁶
- c‑sapphire substrate (isotropic in‑plane):
  α_c(T) = [8.026 + 8.17×10⁻⁴ T − 3.279 exp(−2.91×10⁻³ T)] × 10⁻⁶
- a‑sapphire substrate (anisotropic in‑plane; two unequal axes):
  α_a1(T) = α_c(T)   (one axis, same as c‑sapphire)
  α_a2(T) = [7.419 + 6.43×10⁻⁴ T − 3.211 exp(−2.59×10⁻³ T)] × 10⁻⁶   (second axis)

### Room temperature
RT = 25 °C.  All thermal strain integrations are carried out from RT to the growth temperature T_G.

### Thermal strain
For a substrate with isotropic in‑plane thermal expansion coefficient α_S(T), the in‑plane thermal strain is:
```
u_T = ∫_{RT}^{T_G} (α_PTO − α_S(T)) dT                          (1)
```
For the anisotropic a‑sapphire substrate, two different in‑plane strains arise:
```
u_T1 = ∫_{RT}^{T_G} (α_PTO − α_a1(T)) dT
u_T2 = ∫_{RT}^{T_G} (α_PTO − α_a2(T)) dT
```

### Renormalized thermodynamic potentials
All energies are free energy densities (units J/m³).  The out‑of‑plane polarization P (C/m²) and electric field E (V/m) are directed along the [001] axis.

**Isotropic in‑plane substrates (Si, c‑sapphire, MgO):**
```
G̃ = α₁* P² + α₁₁* P⁴ + α₁₁₁ P⁶ + u_T² / (s₁₁ + s₁₂) − E P       (2)
```
with renormalized coefficients
```
α₁*  = α₁(T) − (2 Q₁₂ u_T) / (s₁₁ + s₁₂)                         (3)
α₁₁* = α₁₁ + Q₁₂² / (s₁₁ + s₁₂)                                 (4)
```
Note: α₁(T) is evaluated at RT (25 °C), i.e., α₁(25 °C) = 3.8×10⁵ (25 − 479) = −1.7252×10⁸ J·m/C².

**Anisotropic in‑plane substrate (a‑sapphire):**
```
G̃ = α₃* P² + α₃₃* P⁴ + α₁₁₁ P⁶ + (s₁₁ (u_T1² + u_T2²)) / (2 (s₁₁² − s₁₂²)) − E P   (9)
```
with
```
α₃*  = α₁(25) − (Q₁₂ / (s₁₁ + s₁₂)) (u_T1 + u_T2)               (10)
α₃₃* = α₁₁ + Q₁₂² / (s₁₁ + s₁₂)                                 (11)
```

### Determination of equilibrium polarization
For a given electric field E (0 or 1×10⁸ V/m, see below), the equilibrium out‑of‑plane polarization P(E) is obtained by minimizing G̃ with respect to P.  This can be done, for instance, by solving dG̃/dP = 0 numerically (bounded minimization in the interval [−5, 5] C/m² is safe).

### Dielectric and piezoelectric properties
The relative (out‑of‑plane) dielectric constant is obtained from the curvature of G̃:
```
ε₃₃ = [ε₀ × (2 α₁* + 12 α₁₁* P² + 30 α₁₁₁ P⁴)]⁻¹               (5)
```
(In the anisotropic case, α₁* and α₁₁* are replaced by α₃* and α₃₃*.)
The out‑of‑plane piezoelectric coefficient is:
```
d₃₃ = 2 ε₀ ε₃₃ [Q₁₁ − (2 s₁₂ Q₁₂) / (s₁₁ + s₁₂)] P               (6)
```

### Tunabilities under an applied electric field
All tunabilities are defined relative to the zero‑field values.  The electric field strength is E = 1000 kV/cm = 1×10⁸ V/m.

Dielectric tunability:
```
φ (%) = (ε₃₃(0) − ε₃₃(E)) / ε₃₃(0) × 100                            (7)
```
Piezoelectric tunability:
```
φ′ (%) = [1 − (ε₃₃(E)/ε₃₃(0)) × (P(E)/P(0))] × 100                (8)
```

## Reproduction target
Compute the out‑of‑plane polarization (P in C/m²), relative dielectric constant (ε₃₃, dimensionless), piezoelectric coefficient (d₃₃ in m/V), and the dielectric and piezoelectric tunabilities (φ and φ′ in %) for PbTiO₃ films on Si, c‑sapphire, a‑sapphire, and MgO substrates as functions of growth temperature T_G. Cover T_G from 25 °C to 800 °C. For each substrate, produce a CSV file with these quantities.

## Workflow steps

### Step 1: Compute properties for PTO on Si substrate
- **Role**: scored (load‑bearing)
- **Action**: Using the model and parameters given above, compute the in‑plane thermal strain u_T for the Si substrate (isotropic TEC α_Si(T)) at each T_G from 25 °C to 800 °C.  Obtain the renormalized coefficients α₁* and α₁₁*.  Minimize the free energy G̃ (Eq. (2)) to find the equilibrium polarization P at E = 0 and at E = 1×10⁸ V/m.  From these, compute ε₃₃, d₃₃, φ and φ′ using Eqs. (5)–(8).  Write the results to `pto_on_si.csv`.
- **Output file**: `/app/outputs/pto_on_si.csv`
- **Format**: csv
- **Contract**: Required columns: `TG`, `P`, `epsilon33`, `d33`, `phi`, `phi_prime`.  Data types: float.  Units: `TG` in °C, `P` in C/m², `epsilon33` dimensionless, `d33` in m/V, `phi` and `phi_prime` in %.  One row per T_G from 25 to 800 °C.
- **Scoring**: scored by hidden verifier

### Step 2: Compute properties for PTO on c‑sapphire substrate
- **Role**: scored (load‑bearing)
- **Action**: Same as Step 1, but using the isotropic TEC function α_c(T) for c‑sapphire.  Write to `pto_on_c_sapphire.csv`.
- **Output file**: `/app/outputs/pto_on_c_sapphire.csv`
- **Format**: csv
- **Contract**: Same as for `pto_on_si.csv`.
- **Scoring**: scored by hidden verifier

### Step 3: Compute properties for PTO on a‑sapphire substrate
- **Role**: scored (load‑bearing)
- **Action**: Same procedure, but for a‑sapphire use the two anisotropic TEC functions α_a1(T) and α_a2(T).  Compute the two in‑plane strains u_T1, u_T2 from Eq. (1) variants, then use the anisotropic free energy (Eq. (9)) with coefficients α₃*, α₃₃*.  Minimize, compute properties, and write to `pto_on_a_sapphire.csv`.
- **Output file**: `/app/outputs/pto_on_a_sapphire.csv`
- **Format**: csv
- **Contract**: Same as for `pto_on_si.csv`.
- **Scoring**: scored by hidden verifier

### Step 4: Compute properties for PTO on MgO substrate
- **Role**: scored (load‑bearing)
- **Action**: Use the constant TEC α_MgO = 13.47×10⁻⁶ /°C for MgO (isotropic case).  Compute u_T with Eq. (1), then follow the isotropic free‑energy procedure.  Write to `pto_on_mgo.csv`.
- **Output file**: `/app/outputs/pto_on_mgo.csv`
- **Format**: csv
- **Contract**: Same as for `pto_on_si.csv`.
- **Scoring**: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pto_on_si.csv`
- `/app/outputs/pto_on_c_sapphire.csv`
- `/app/outputs/pto_on_a_sapphire.csv`
- `/app/outputs/pto_on_mgo.csv`

## Output contract
Every file the hidden verifier reads is described below.  Write each file under `/app/outputs` and follow its schema exactly.

### pto_on_si.csv
- path: `/app/outputs/pto_on_si.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermodynamic properties of PTO on Si
- schema:
  - `type`: table
  - `required_columns`: `TG`, `P`, `epsilon33`, `d33`, `phi`, `phi_prime`
  - `units`:
    - `TG`: C
    - `P`: C/m^2
    - `epsilon33`: dimensionless
    - `d33`: m/V
    - `phi`: %
    - `phi_prime`: %

### pto_on_c_sapphire.csv
- path: `/app/outputs/pto_on_c_sapphire.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermodynamic properties of PTO on c‑sapphire
- schema:
  - `type`: table
  - `required_columns`: `TG`, `P`, `epsilon33`, `d33`, `phi`, `phi_prime`
  - `units`:
    - `TG`: C
    - `P`: C/m^2
    - `epsilon33`: dimensionless
    - `d33`: m/V
    - `phi`: %
    - `phi_prime`: %

### pto_on_a_sapphire.csv
- path: `/app/outputs/pto_on_a_sapphire.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermodynamic properties of PTO on a‑sapphire
- schema:
  - `type`: table
  - `required_columns`: `TG`, `P`, `epsilon33`, `d33`, `phi`, `phi_prime`
  - `units`:
    - `TG`: C
    - `P`: C/m^2
    - `epsilon33`: dimensionless
    - `d33`: m/V
    - `phi`: %
    - `phi_prime`: %

### pto_on_mgo.csv
- path: `/app/outputs/pto_on_mgo.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermodynamic properties of PTO on MgO
- schema:
  - `type`: table
  - `required_columns`: `TG`, `P`, `epsilon33`, `d33`, `phi`, `phi_prime`
  - `units`:
    - `TG`: C
    - `P`: C/m^2
    - `epsilon33`: dimensionless
    - `d33`: m/V
    - `phi`: %
    - `phi_prime`: %

Notes: All quantities are computed at room temperature with an applied electric field E = 1000 kV/cm for tunabilities.  The checker will compare each column against hidden reference values derived from the same thermodynamic model, using threshold_or_better for directional metrics and trend checks.  No gold values are disclosed here.

## How you are scored
A hidden verifier independently reads each of your four CSV output files.  It compares the columns P, epsilon33, d33, phi, and phi_prime against hidden reference values derived from the same thermodynamic model, using threshold_or_better scoring where a better (higher) value for directional metrics earns full credit, and appropriate relative tolerances.  The verifier also checks that the trends of these quantities with increasing T_G match expected physical behavior (e.g., monotonic increases or decreases depending on tensile or compressive thermal strain).  Each scored artifact contributes a portion of the total reward; simply reporting values that happen to match a published table is not enough — the workflow must be executed genuinely.