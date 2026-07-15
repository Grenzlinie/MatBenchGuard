# Thermoelectric Transport Modeling of Sm-doped CaMnO3

## Problem background
Thermoelectric materials directly convert waste heat into electricity. Calcium manganate (CaMnO₃) is an n-type perovskite oxide whose thermoelectric figure of merit ZT can be affected by rare‑earth doping at the calcium site. This task investigates how substituting 8 % and 17 % of the Ca atoms with samarium (Sm) changes the electronic band gap and the temperature‑dependent thermoelectric transport coefficients — Seebeck coefficient, electrical conductivity per relaxation time, electronic thermal conductivity per relaxation time, and ZT — using first‑principles density functional theory and semi‑classical Boltzmann transport theory.

## Approach
The study combines density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation and semi‑classical Boltzmann transport theory under the constant relaxation time approximation. Starting from the experimental orthorhombic Pbnm unit cell of CaMnO₃, 3×1×1 supercells are built for the pristine compound and for the two Sm‑doped compositions Ca₀.₉₂Sm₀.₀₈MnO₃ and Ca₀.₈₃Sm₀.₁₇MnO₃. The workflow consists of variable‑cell relaxation, determination of the magnetic ground state by comparing total energies of several magnetic configurations, electronic band structure calculation, extraction of the indirect band gap for pristine CaMnO₃, and transport calculations using BoltzTraP to obtain the temperature‑dependent Seebeck coefficient, electrical conductivity per relaxation time, electronic thermal conductivity per relaxation time, and the figure of merit ZT = S²σT/κ for all three materials. The results are compared across the three doping levels over the temperature range 300–800 K to assess the influence of Sm substitution.

## Reproduction target
Compute the indirect electronic band gap of pristine CaMnO₃ (in eV) and write it to a text file. Compute the temperature‑dependent Seebeck coefficient (μV/K), electrical conductivity over relaxation time (1/(Ω·m·s)), electronic thermal conductivity over relaxation time (W/(m·K·s)), and dimensionless ZT for pristine CaMnO₃, Ca₀.₉₂Sm₀.₀₈MnO₃ (8 % Sm), and Ca₀.₈₃Sm₀.₁₇MnO₃ (17 % Sm) at exactly the temperatures 300, 400, 500, 600, 700, and 800 K. Collect all transport data into a single CSV file with the columns: temperature (K), material (pristine / Sm8 / Sm17), Seebeck, sigma_over_tau, kappa_over_tau, ZT.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- BoltzTraP2: https://www.simpa.epfl.ch/boltzman/wien2k/boltzman.html
- PBE pseudopotentials (SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- CaMnO3 crystal structure (Pbnm): 10.1016/j.jpcs.2006.01.110

## Workflow steps

### Step 1: Supercell generation
- Role: process
- Action: Construct 3×1×1 supercells of CaMnO3, Ca0.92Sm0.08MnO3, and Ca0.83Sm0.17MnO3 from the experimental Pbnm unit cell. Sm replaces Ca atoms to achieve 8% and 17% doping.
- Evidence: `/app/outputs/supercells.cif`

### Step 2: Variable-cell relaxation
- Role: process
- Action: Relax atomic positions and lattice parameters of each supercell using Quantum ESPRESSO (GGA-PBE, plane-wave cutoff and k-mesh) until forces are below a tight convergence threshold.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 3: Magnetic ground state determination
- Role: process
- Action: Perform total-energy SCF calculations for pristine CaMnO3 in ferromagnetic, nonmagnetic, A-type antiferromagnetic, C-type antiferromagnetic, and G-type antiferromagnetic configurations. For the doped compounds, perform spin-polarized calculations to confirm nonmagnetic ground state. Use the relaxed structures from step 2.
- Evidence: `/app/outputs/magnetic_energies.json`

### Step 4: Electronic band structure calculations
- Role: process
- Action: Compute band structures and eigen-energies for the stable phases: G-type AFM for pristine CaMnO3, nonmagnetic for the two Sm-doped compounds. Use Quantum ESPRESSO with the relaxed structures and a suitable k-path. Save eigen-energies in a format readable by BoltzTraP.
- Evidence: `/app/outputs/bands.gnu`

### Step 5: Extract band gap of pristine CaMnO3
- Role: scored
- Action: From the band structure computed in step 4, determine the indirect band gap of pristine CaMnO3 and write the value (in eV) to the output file.
- Output file: `/app/outputs/pristine_band_gap.txt`
- Format: txt
- Contract: A single line with a floating-point number.
- Scoring: scored by hidden verifier

### Step 6: BoltzTraP transport calculations
- Role: process
- Action: Run BoltzTraP using the eigen-energies from step 4 and a constant relaxation time τ = 0.8×10⁻¹⁴ s. Compute temperature-dependent Seebeck coefficient S, electrical conductivity σ/τ, and electronic thermal conductivity κₑ/τ over the range 300–800 K for all three compounds.
- Evidence: `/app/outputs/boltztrap.condtens`

### Step 7: Compute ZT and compile transport table
- Role: scored (load-bearing)
- Action: Calculate ZT = S²σT/κ from the coefficients output by step 6. Write a CSV file with columns: temperature (K), material (pristine/Sm8/Sm17), Seebeck (μV/K), sigma_over_tau (1/(Ω·m·s)), kappa_over_tau (W/(m·K·s)), ZT (dimensionless). Include rows for temperatures 300, 400, 500, 600, 700, 800 K only.
- Output file: `/app/outputs/transport_properties.csv`
- Format: csv
- Contract: CSV with header: temperature,material,Seebeck,sigma_over_tau,kappa_over_tau,ZT. material values: pristine, Sm8, Sm17. All numeric fields as decimals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_band_gap.txt`
- `/app/outputs/transport_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_band_gap.txt
- path: `/app/outputs/pristine_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed band gap of pristine CaMnO3. Compared to the paper-reported value with a small tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the indirect band gap of pristine CaMnO3 in eV.

### transport_properties.csv
- path: `/app/outputs/transport_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent transport coefficients and ZT for pristine, 8% and 17% Sm-doped CaMnO3. Compared to digitized reference data from the paper with relative tolerances and structural trend checks.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `material`, `Seebeck`, `sigma_over_tau`, `kappa_over_tau`, `ZT`
  - `units`:
    - `Seebeck`: μV/K
    - `sigma_over_tau`: 1/(Ω·m·s)
    - `kappa_over_tau`: W/(m·K·s)
    - `ZT`: dimensionless

Notes: The band gap output is scored but not load-bearing. The transport properties output is load-bearing, forcing execution of the full DFT pipeline. Structural trends (e.g., negative Seebeck, temperature dependence of conductivity) are also verified on this artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the indirect band gap of pristine CaMnO3 in eV."
      },
      "description": "Computed band gap of pristine CaMnO3. Compared to the paper-reported value with a small tolerance."
    },
    {
      "file": "transport_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "material",
          "Seebeck",
          "sigma_over_tau",
          "kappa_over_tau",
          "ZT"
        ],
        "units": {
          "Seebeck": "μV/K",
          "sigma_over_tau": "1/(Ω·m·s)",
          "kappa_over_tau": "W/(m·K·s)",
          "ZT": "dimensionless"
        }
      },
      "description": "Temperature-dependent transport coefficients and ZT for pristine, 8% and 17% Sm-doped CaMnO3. Compared to digitized reference data from the paper with relative tolerances and structural trend checks."
    }
  ],
  "notes": "The band gap output is scored but not load-bearing. The transport properties output is load-bearing, forcing execution of the full DFT pipeline. Structural trends (e.g., negative Seebeck, temperature dependence of conductivity) are also verified on this artifact."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact and combines the scores by weight to produce the final reward (a float between 0 and 1). The band gap is compared to a reference value within a predefined tolerance. The transport table is scored on correctness of the computed numbers against a hidden reference and on physical consistency: the Seebeck coefficient must be negative for all materials; the temperature dependence of electrical conductivity must follow the expected semiconducting (increase) or metallic (decrease) trend; ZT must increase with temperature for all compositions; and the relative ZT ordering among the three doping levels must satisfy the physically expected relationship. The computational pipeline must be fully executed — simply reporting numbers is not enough.
