# Electrocaloric effect in PbZrO₃ thin films from effective Hamiltonian simulations

## Problem background
Antiferroelectric thin films such as PbZrO₃ can exhibit a competition between antiferroelectric (AFE) and ferroelectric (FE) phases. The electrocaloric effect – a reversible temperature change ΔT under adiabatic application of an electric field, or an isothermal entropy change ΔS – in such materials is not fully understood when the material undergoes an AFE‑FE phase transition. The sign, magnitude, and tunability of the electrocaloric response across the transition region remain open questions. This task investigates the electrocaloric behaviour of a 5 nm PbZrO₃ film by computing ΔT and ΔS as functions of temperature and applied electric field, for a stress‑free film and for a film under compressive epitaxial strain.

## Approach
The method uses a first‑principles‑based effective Hamiltonian for PbZrO₃. The film is modelled as a 12×12×12 supercell with thickness 5 nm, growth direction [001], in‑plane periodic boundary conditions, and partial surface charge screening. Simulated annealing Metropolis Monte Carlo is run from 955 K down to 5 K in steps of 25 K; at each temperature an external electric field is applied along the growth direction to record polarisation‑electric field hysteresis loops. From these loops the upper‑branch polarisation P(T) is extracted for each field, starting from E=0 (i.e., the zero‑field polarisation point is included as the baseline for integration). The P(T) data are smoothed using Bezier interpolation and numerically differentiated to obtain (∂P/∂T)_E, which is then integrated using the Maxwell relations

ΔT = −(1/ρ) ∫₀^E (T/C) (∂P/∂T)_E dE,

ΔS = −(1/ρ) ∫₀^E (∂P/∂T)_E dE,

with mass density ρ = 8.3 g/cm³ and heat capacity C = 302 J/(kg·K). Two configurations are studied: a stress‑free film with screening parameter β=0.975, and a film under −1.5 % compressive epitaxial strain with β=0.98.

### From local modes to macroscopic polarization
The effective Hamiltonian’s primary degrees of freedom are the local modes **u_i**, which are proportional to the dipole moment of the unit cell *i*. To obtain the macroscopic polarization **P** (in C/m²) that enters the Maxwell relations, use the relation

**P** = (e / a₀³) (1 / N) Σ_i **u_i**,

where
- N = 12³ = 1728 is the total number of unit cells in the 12×12×12 supercell,
- a₀ = 4.1 Å = 4.1×10⁻¹⁰ m is the reference cubic lattice constant of PbZrO₃ at zero Kelvin,
- e = 1.602×10⁻¹⁹ C is the elementary charge.

The film thickness of 5 nm corresponds to the *z*‑direction containing 12 unit cells, each of size a₀, giving a total thickness of 12 × 4.1 Å ≈ 4.9 nm ≈ 5 nm. The polarization component along the growth direction, P_z, is the quantity used for the hysteresis loops and the subsequent P(T) curves. After each Monte Carlo sweep at a given temperature and field, compute the instantaneous **P** from the above formula; the reported polarization is the configurational average over the sweeps used for equilibration/production.

### Effective Hamiltonian
The total energy is expanded as

E^tot = E^AFE({u_i}) + E^AFD({ω_i}) + E^elas({η_i}) + E^AFE-elas({u_i,η_i}) + E^AFD-elas({ω_i,η_i}) + E^AFE-AFD({u_i,ω_i}),

where u_i are local modes (proportional to the dipole moment of unit cell i), ω_i are antiferrodistortive rotation vectors of the oxygen octahedra, and η_i are local strain tensors. The explicit forms and parameters are as follows:

- **E^AFE** (antiferroelectric Σ₂ mode energy):
  - On‑site self‑energy: Σ_i [κ₂|u_i|² + κ₄|u_i|⁴], with κ₂ = 1.543 eV/Å², κ₄ = 3.086 eV/Å⁴.
  - Short‑range interaction: Σ_{i,j} J_{ij} u_i u_j, with J_{ij} non‑zero only for first and second in‑plane neighbours and first out‑of‑plane neighbours. Values (in eV/Å²): J₁ (in‑plane nearest) = −0.128, J₂ (in‑plane next‑nearest) = 0.032, Jₒ (out‑of‑plane nearest) = −0.072.
  - Dipole‑dipole interaction: (1/2) Σ_{i,j} D_{ij} u_i u_j, where D_{ij} = (1/4πϵ₀ϵ_r)[δ_{αβ}/|r_{ij}|³ − 3 r_{ij,α} r_{ij,β}/|r_{ij}|⁵] using a background dielectric constant ϵ_r = 10 and Ewald sums for periodic boundary conditions.

- **E^AFD** (antiferrodistortive mode energy):
  - On‑site self‑energy: Σ_i [α₂|ω_i|² + α₄|ω_i|⁴], with α₂ = 2.0 eV/rad², α₄ = 1.0 eV/rad⁴.
  - Short‑range interaction: Σ_{i,j} K_{ij} ω_i ω_j, with K₁ (in‑plane nearest) = 0.05 eV/rad², K₂ (in‑plane next‑nearest) = −0.02 eV/rad², Kₒ (out‑of‑plane) = 0.03 eV/rad².
  - No dipole‑dipole term (ω_i are non‑polar).

- **E^elas** (elastic energy):
  - Linear elastic energy: Σ_i [a₁(η_{i,xx}+η_{i,yy}+η_{i,zz})² + a₂(η_{i,xx}²+η_{i,yy}²+η_{i,zz}²) + a₃(η_{i,xy}²+η_{i,yz}²+η_{i,zx}²)] with a₁ = 220 eV, a₂ = 30 eV, a₃ = 30 eV.
  - Higher‑order contributions: b₁(η_{i,xx}³+...) with b₁ = 500 eV.

- **E^AFE-elas** (AFE‑strain coupling):
  - Σ_i [g₁₁ η_{i,xx} u_{i,x}² + g₁₂ η_{i,yy} u_{i,x}² + …], with g₁₁ = −8 eV/Å², g₁₂ = −2 eV/Å², g₄₄ = −1 eV/Å² (only diagonal couplings listed; apply symmetries for all components).

- **E^AFD-elas** (AFD‑strain coupling):
  - Σ_i [h₁₁ η_{i,xx} ω_{i,x}² + h₁₂ η_{i,yy} ω_{i,x}² + …], with h₁₁ = −3 eV/rad², h₁₂ = −1 eV/rad², h₄₄ = −0.5 eV/rad².

- **E^AFE-AFD** (AFE‑AFD coupling):
  - Σ_i [c₁ (u_i·ω_i)² + c₂ |u_i|²|ω_i|²], with c₁ = 4 eV/Å²rad², c₂ = 2 eV/Å²rad².

### Simulation details
- Supercell: 12×12×12, each unit cell cubic with lattice constant a₀ = 4.1 Å. Film thickness ≈ 5 nm (12 × a₀ ≈ 4.9 nm).
- Depolarising field: Compensated by a fraction β of the ideal compensating field: E_comp = −β E_dep.
- Strain condition: For the stress‑free film, the in‑plane strain components adjust freely; for the strained film, an in‑plane epitaxial strain of −1.5 % is imposed (compressive).
- Monte Carlo: 40,000 sweeps for equilibration at each temperature during annealing. The electric field (applied along z, i.e., growth direction) is varied from 0 to 600 kV/cm to obtain hysteresis loops.

## Reproduction target
For each of the two film configurations, compute and report the electrocaloric temperature change ΔT and isothermal entropy change ΔS as functions of temperature for applied electric fields E = 50, 100, 200, 300, 400, 500, 600 kV/cm, over the temperature range 5 K to 955 K in steps of 25 K. Provide the results as two CSV files, one for the stress‑free film and one for the strained film, with columns: temperature (K), field (kV/cm), deltaT (K), deltaS (J/kg·K).

## Workflow steps

### Step 1: Monte Carlo simulation for stress‑free film
- Role: process
- Action: Construct the effective Hamiltonian using the parameters listed above. Set up a 12×12×12 supercell film with 5 nm thickness, growth direction [001], in‑plane periodic boundary conditions, and surface charge screening parameter β=0.975. Run simulated annealing Metropolis Monte Carlo from 955 K down to 5 K in steps of 25 K, equilibrating each temperature with 40,000 sweeps. For each temperature, apply an external electric field along the growth direction at values 0, 50, 100, 200, 300, 400, 500, 600 kV/cm and record the polarisation hysteresis loop (P–E). Store the raw data internally; they are not part of the scored output, but you may keep them for subsequent steps.

### Step 2: Monte Carlo simulation for strained film
- Role: process
- Action: Run the same simulated annealing Metropolis Monte Carlo protocol as step 1, but for a film under −1.5 % compressive epitaxial strain (in‑plane strain imposed) and screening parameter β=0.98. Store the raw data internally.

### Step 3: Electrocaloric ΔT and ΔS for stress‑free film
- Role: scored (load-bearing)
- Action: For each electric field and temperature, extract the upper branch (P>0) of the hysteresis loop to obtain P(T), ensuring that the zero‑field point (P₀ at E=0) is included as the starting value. Smooth the P(T) curves using Bezier interpolation. Numerically differentiate to obtain (∂P/∂T)_E. Integrate the Maxwell relations ΔT = −(1/ρ) ∫₀^E (T/C)(∂P/∂T)_E dE and ΔS = −(1/ρ) ∫₀^E (∂P/∂T)_E dE using ρ=8.3 g/cm³, C=302 J/(kg·K). Write the resulting ΔT and ΔS for all temperatures (5 K to 955 K in steps of 25 K) and all fields (50,100,200,300,400,500,600 kV/cm) to `/app/outputs/deltaT_stress_free.csv`.
- Output file: `/app/outputs/deltaT_stress_free.csv`
- Format: csv
- Contract: CSV with columns: temperature (K), field (kV/cm), deltaT (K), deltaS (J/kg·K). Rows: all temperatures 5–955 K in 25 K steps (39 values) for each field, sorted by temperature then field.
- Scoring: scored by hidden verifier

### Step 4: Electrocaloric ΔT and ΔS for strained film
- Role: scored (load-bearing)
- Action: Load the raw polarisation data from the strained simulation and perform exactly the same extraction, smoothing, differentiation, and integration as step 3. Write the ΔT and ΔS results to `/app/outputs/deltaT_strained.csv`.
- Output file: `/app/outputs/deltaT_strained.csv`
- Format: csv
- Contract: Same format as `deltaT_stress_free.csv`: temperature (K), field (kV/cm), deltaT (K), deltaS (J/kg·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deltaT_stress_free.csv`
- `/app/outputs/deltaT_strained.csv`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deltaT_stress_free.csv
- path: `/app/outputs/deltaT_stress_free.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electrocaloric temperature change ΔT and isothermal entropy change ΔS for the stress‑free 5 nm PbZrO₃ film (β=0.975) under electric fields of 50,100,200,300,400,500,600 kV/cm, at all temperatures from 5 K to 955 K in steps of 25 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `field`, `deltaT`, `deltaS`
  - `units`:
    - `temperature`: K
    - `field`: kV/cm
    - `deltaT`: K
    - `deltaS`: J/kg·K

### deltaT_strained.csv
- path: `/app/outputs/deltaT_strained.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electrocaloric temperature change ΔT and isothermal entropy change ΔS for the compressively strained (−1.5 %) PbZrO₃ film (β=0.98) under the same electric fields and temperature grid.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `field`, `deltaT`, `deltaS`
  - `units`:
    - `temperature`: K
    - `field`: kV/cm
    - `deltaT`: K
    - `deltaS`: J/kg·K

Notes: The hidden checker compares the submitted ΔT and ΔS curves against the paper‑reported results, using absolute tolerances and a relative tolerance on the peak ΔT at 500 kV/cm. Qualitative sign checks are also performed.

## Self-check before finishing (optional, not scored)
A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deltaT_stress_free.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "field",
          "deltaT",
          "deltaS"
        ],
        "units": {
          "temperature": "K",
          "field": "kV/cm",
          "deltaT": "K",
          "deltaS": "J/kg·K"
        }
      },
      "description": "Electrocaloric temperature change ΔT and isothermal entropy change ΔS for the stress‑free 5 nm PbZrO₃ film (β=0.975) under electric fields of 50,100,200,300,400,500,600 kV/cm, at all temperatures from 5 K to 955 K in steps of 25 K."
    },
    {
      "file": "deltaT_strained.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "field",
          "deltaT",
          "deltaS"
        ],
        "units": {
          "temperature": "K",
          "field": "kV/cm",
          "deltaT": "K",
          "deltaS": "J/kg·K"
        }
      },
      "description": "Electrocaloric temperature change ΔT and isothermal entropy change ΔS for the compressively strained (−1.5 %) PbZrO₃ film (β=0.98) under the same electric fields and temperature grid."
    }
  ],
  "notes": "The hidden checker compares the submitted ΔT and ΔS curves against the paper‑reported results, using absolute tolerances and a relative tolerance on the peak ΔT at 500 kV/cm. Qualitative sign checks are also performed."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently evaluates each scored artifact. The verifier compares the submitted ΔT and ΔS curves against the correct results (derived from the paper’s methodology) using a combination of checks that assess curve shape, peak magnitude, and qualitative sign. The final reward is a weighted combination of these checks across both film configurations. Simply reporting known numbers is not sufficient; you must implement the full workflow and produce the artifacts from your simulation. The verifier does not inspect your simulation code directly – it only scores the final CSV outputs.