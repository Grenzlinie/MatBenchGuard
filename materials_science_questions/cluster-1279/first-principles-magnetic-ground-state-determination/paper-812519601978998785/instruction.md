# Magnetization Plateaus and Magnetocaloric Effect via Monte Carlo Simulation of an Ising Model Perovskite

## Problem background
This task is based on a published study of the magnetic properties of a simple perovskite material using an effective Ising model. The system contains two magnetic sublattices: Mn spins (S=2, treated as five‑state Ising variables) and Nd spins (S=3/2, four‑state Ising variables). The Nd–Nd exchange is strong enough to maintain ferromagnetic alignment, so the Nd sublattice is treated as a fully polarised background that nevertheless contributes to the total magnetisation and magnetic entropy. Monte Carlo simulations reveal that the magnetisation of the Mn sublattice exhibits plateaus with first‑order transitions as the crystal field is varied, and that the magnetocaloric effect (quantified by the relative cooling power, RCP) can be tuned by the external magnetic field, crystal field, and exchange interactions.  

Your task is to reproduce the key numerical results by performing Monte Carlo simulations of the Hamiltonian described below.

## Model Hamiltonian (Ising model)

The system is described by the following Hamiltonian, written in dimensionless reduced units (*t*, *R2*, *R1*, *d_s*, *He*):

```
H = - R2  Σ_{⟨i,j⟩} Sᵢ Sⱼ
    - R1  Σ_{i} Sᵢ σᵢ
    - d_s Σ_{i} (Sᵢ)²
    - He  Σ_{i} (Sᵢ + σᵢ)
```

### Spin variables

- **Mn spins** *Sᵢ* are located on every site of a simple cubic lattice of linear size **L = 32**. Each *Sᵢ* can take five values: `{-2, -1, 0, +1, +2}` (the local moment of Mn³⁺, S=2).
- **Nd spins** *σᵢ* occupy the same lattice sites (one Nd atom per unit cell). Each *σᵢ* can take four values: `{-3/2, -1/2, +1/2, +3/2}` (the moment of Nd³⁺, S=3/2).  The Nd–Nd exchange is assumed to be strong enough to keep all Nd spins perfectly aligned ferromagnetically; therefore the Nd–Nd term is omitted and the Nd sublattice acts as an effective field through the *R1* term.  The Nd spins are still dynamical variables that can flip under the influence of the Mn–Nd exchange and the external field, so they contribute to the total magnetisation and to the magnetic entropy.

### Lattice and interactions

- The Mn spins sit on a simple cubic lattice of linear size **L = 32**.  Nearest‑neighbour sites are defined by the vectors (±1,0,0), (0,±1,0), (0,0,±1) with periodic boundary conditions.
- **R2** is the dimensionless Mn–Mn exchange parameter.  For antiferromagnetic coupling **R2 < 0**; for ferromagnetic coupling **R2 > 0**.  In all simulations we use negative values.
- **R1** is the dimensionless Mn–Nd exchange parameter (positive or negative).
- **d_s** is the dimensionless crystal‑field strength that acts only on the Mn spins (the term `-d_s Sᵢ²`).
- **He** is the dimensionless external magnetic field.
- **t = k_B T / |J|** is the dimensionless temperature, where the energy scale *J* = 1 is used for convenience (so *R2*, *R1*, *d_s* and *He* are directly the quantities that appear in the Hamiltonian above).

### Magnetisations

- **Sublattice magnetisation** (for the Mn plateau study):  Because the Mn lattice is bipartite (simple cubic), one can define two interpenetrating sub‑lattices **A** and **B** (e.g. sites where x+y+z is even and odd).  The magnetisations per Mn site are:
  ```
  M_Mn_plus  = (1 / (L³/2)) Σ_{i∈A} Sᵢ
  M_Mn_minus = (1 / (L³/2)) Σ_{i∈B} Sᵢ
  ```
- **Total magnetisation** (for the magnetocaloric study):
  ```
  M_t = (1 / L³) Σ_{i} (Sᵢ + σᵢ)
  ```

## Monte Carlo details

- **Algorithm**: single‑spin‑flip heat‑bath (or Metropolis) algorithm.
- **Lattice**: L = 32, total number of sites = 32768 (each site hosts one Mn and one Nd spin).
- **Equilibration**: 20000 Monte Carlo steps per spin (MCS) for equilibration.
- **Measurement**: 20000 MCS for averaging magnetisations and energy.
- **Temperature scan for RCP**: Temperature *t* is swept from 0.2 to 6.0 in steps of 0.1 (you may extend the range slightly if the peak of ΔSₘ lies near the boundary).  For each temperature the simulation is equilibrated for 5000 MCS (a shorter equilibration is sufficient because the scan proceeds in small steps and the configuration at the previous temperature serves as a good starting point) followed by 5000 measurement MCS.

## Reproduction targets

### 1) Magnetisation plateaus

Sweep the reduced crystal field **d_s** from -80 to 0 (inclusive) with a step of Δd_s = 0.1 at temperature **t = 1.2**, fixed **R2 = -4.2**, **He = 0**.  Perform the sweep twice:

- **R1 = 0.5**
- **R1 = 5.0**

For each parameter point record the sublattice magnetisations `M_Mn_plus` and `M_Mn_minus` (both are floating‑point numbers).

From the curves of M_Mn_plus and M_Mn_minus versus d_s, identify the three **first‑order transition points** where the magnetisations undergo a discontinuous jump.  The jumps occur at the boundaries between four plateau regions.  Output the six critical d_s values (three for each R1) as described below.

### 2) Magnetocaloric effect – RCP

For each of the following parameter scans, compute the temperature‑dependent total magnetisation *M_t(t)* by Monte Carlo simulation.  From *M_t(t)* obtain the magnetic entropy change ΔSₘ via the Maxwell relation:

```
ΔSₘ(T) = ∫₀^He (∂M/∂T)_H dH
```

Since only one He value per scan is available, you can evaluate ΔSₘ by comparing the magnetisation curves at two nearby fields (the given He and He*=0, or a very small field) and using a numerical derivative.  Many implementations simply compute ΔSₘ from the thermal average of the internal energy, but the Maxwell‑relation route is the standard method.

**Recommended implementation**:
1. Run Monte Carlo at the desired He and at He* = 0 (or He* = 0.1, small enough) over the temperature grid.
2. For each temperature, compute *M*(He,t) and *M*(He*,t).
3. Numerically integrate ∂M/∂T with respect to H using the trapezoidal rule.  With only two field points one can use:
   ```
   ΔSₘ(T) ≈ ( M(He, T) - M(0, T) ) * (He - 0) ... no, that is not correct.
   Better: use the formula
   ΔSₘ(T) = ∫₀^He (∂M/∂T)_H dH  ≈  ∑_{H_i} [ M(H_i, T+ΔT) - M(H_i, T-ΔT) ] / (2ΔT) ΔH_i
   ```
   but with only two fields you can approximate the derivative by finite differences and integrate.

For simplicity you may compute **RCP = |ΔSₘ_max| × δT_FWHM**, where ΔSₘ_max is the maximum absolute value of ΔSₘ (in units of k_B, i.e. dimensionless) and δT_FWHM is the full width at half maximum of the |ΔSₘ(T)| curve.

**Parameter scans** (each done at the given parameters, with the same temperature grid and field values):

- **He scan**: He = 3, 6, 9, 12  (fixed R2 = -1, d_s = 0, R1 = 1)
- **d_s scan**: d_s = -15, 0, 15  (fixed R2 = -1, R1 = 1, He = 1)
- **R1 scan**: R1 = 1.5, 2.5, 3.5  (fixed R2 = -1, d_s = -15, He = 1)
- **R2 scan**: R2 = -1.5, -2, -2.5  (fixed R1 = 1, d_s = 0, He = 1)

For each scan output the RCP value (a single float) for each parameter value.

## Workflow steps

### Step 1: Simulate magnetisation plateaus
- **Action**: Implement the Ising model Hamiltonian described above.  Perform Monte Carlo simulations (heat‑bath algorithm, L=32, t=1.2, R2=-4.2, He=0) with the two values of R1 (0.5 and 5.0).  Sweep d_s from -80 to 0 in steps of 0.1.  Record the sublattice magnetisations M_Mn_plus and M_Mn_minus at each d_s.
- **Output file**: `/app/outputs/magnetization_plateaus.csv`
- **Format**: csv
- **Columns**: `R1` (float), `d_s` (float), `M_Mn_plus` (float), `M_Mn_minus` (float).  Rows sorted by R1 then d_s.

### Step 2: Determine critical crystal fields
- **Action**: From the magnetisation vs d_s data, locate the three first‑order transition points where the sublattice magnetisations jump, for each R1 value.  Output the critical d_s values.
- **Output file**: `/app/outputs/critical_ds.txt`
- **Format**: txt
- **Details**: Two lines: first line for R1=0.5 with three comma‑separated floats (d_sc1, d_sc2, d_sc3); second line for R1=5.0 with three comma‑separated floats (d_s1, d_s2, d_s3).

### Step 3: Compute RCP vs applied field
- **Action**: For He = 3, 6, 9, 12 at fixed R2=-1, d_s=0, R1=1, simulate the temperature‑dependent total magnetisation M_t(t) over t = 0.2–6.0 (step 0.1).  Compute ΔSₘ(T) and RCP.  Output RCP for each He.
- **Output file**: `/app/outputs/rcp_vs_field.csv`
- **Format**: csv
- **Columns**: `He` (float), `RCP` (float).  One row per He value.

### Step 4: Compute RCP vs crystal field
- **Action**: For d_s = -15, 0, 15 at fixed R2=-1, R1=1, He=1, repeat the simulations and compute RCP.  Output RCP for each d_s.
- **Output file**: `/app/outputs/rcp_vs_ds.csv`
- **Format**: csv
- **Columns**: `d_s` (float), `RCP` (float).  One row per d_s value.

### Step 5: Compute RCP vs Nd-Mn exchange
- **Action**: For R1 = 1.5, 2.5, 3.5 at fixed R2=-1, d_s=-15, He=1, repeat the simulations and compute RCP.  Output RCP for each R1.
- **Output file**: `/app/outputs/rcp_vs_R1.csv`
- **Format**: csv
- **Columns**: `R1` (float), `RCP` (float).  One row per R1 value.

### Step 6: Compute RCP vs Mn-Mn exchange
- **Action**: For R2 = -1.5, -2, -2.5 at fixed R1=1, d_s=0, He=1, repeat the simulations and compute RCP.  Output RCP for each R2.
- **Output file**: `/app/outputs/rcp_vs_R2.csv`
- **Format**: csv
- **Columns**: `R2` (float), `RCP` (float).  One row per R2 value.

## Output files

All artifacts are placed under `/app/outputs`:

- `/app/outputs/magnetization_plateaus.csv`
- `/app/outputs/critical_ds.txt`
- `/app/outputs/rcp_vs_field.csv`
- `/app/outputs/rcp_vs_ds.csv`
- `/app/outputs/rcp_vs_R1.csv`
- `/app/outputs/rcp_vs_R2.csv`

## Output contract

Every file the hidden verifier reads is described below.  Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_plateaus.csv
- **path**: `/app/outputs/magnetization_plateaus.csv`
- **format**: csv
- **purpose**: scored
- **description**: Magnetisation values of the Mn sublattice as a function of reduced crystal field for two Nd-Mn exchange strengths.
- **schema**:
  - `type`: table
  - `required_columns`: `R1`, `d_s`, `M_Mn_plus`, `M_Mn_minus`
  - **description**: Raw magnetisation data showing plateau structure.

### critical_ds.txt
- **path**: `/app/outputs/critical_ds.txt`
- **format**: txt
- **purpose**: scored
- **target_policy**: exact_match
- **description**: Critical crystal fields where first-order transitions occur in the Mn sublattice magnetisation.
- **schema**:
  - `type`: text
  - **description**: Two lines: first line for R1=0.5 with three comma‑separated floats (d_sc1,d_sc2,d_sc3); second line for R1=5.0 with three comma‑separated floats (d_s1,d_s2,d_s3).

### rcp_vs_field.csv
- **path**: `/app/outputs/rcp_vs_field.csv`
- **format**: csv
- **purpose**: scored
- **description**: Relative cooling power for different applied magnetic field strengths.
- **schema**:
  - `type`: table
  - `required_columns`: `He`, `RCP`
  - **description**: RCP values as a function of reduced external field.

### rcp_vs_ds.csv
- **path**: `/app/outputs/rcp_vs_ds.csv`
- **format**: csv
- **purpose**: scored
- **description**: Relative cooling power for different crystal field values.
- **schema**:
  - `type`: table
  - `required_columns`: `d_s`, `RCP`
  - **description**: RCP values as a function of reduced crystal field.

### rcp_vs_R1.csv
- **path**: `/app/outputs/rcp_vs_R1.csv`
- **format**: csv
- **purpose**: scored
- **description**: Relative cooling power for different Nd-Mn exchange strengths.
- **schema**:
  - `type`: table
  - `required_columns`: `R1`, `RCP`
  - **description**: RCP values as a function of reduced Nd-Mn exchange.

### rcp_vs_R2.csv
- **path**: `/app/outputs/rcp_vs_R2.csv`
- **format**: csv
- **purpose**: scored
- **description**: Relative cooling power for different Mn-Mn exchange strengths.
- **schema**:
  - `type`: table
  - `required_columns`: `R2`, `RCP`
  - **description**: RCP values as a function of reduced Mn-Mn exchange.

**Notes**: Artifacts are scored based on structural features (plateaus, monotonic trends) and critical field values compared against paper‑reported reference (tolerance ±1.0).  You do **not** need to know the reference values; the verifier compares your output to hidden gold data.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is provided below.  Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns.  Fix any mismatch before finishing.

This checks **shape only** (files, keys, columns) — it does NOT judge scientific correctness.

```json
{
  "outputs": [
    {
      "file": "magnetization_plateaus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["R1","d_s","M_Mn_plus","M_Mn_minus"],
        "description": "Raw magnetisation data showing plateau structure."
      },
      "description": "Magnetisation values of the Mn sublattice as a function of reduced crystal field for two Nd-Mn exchange strengths."
    },
    {
      "file": "critical_ds.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines: first line for R1=0.5 with three comma-separated floats (d_sc1,d_sc2,d_sc3); second line for R1=5.0 with three comma-separated floats (d_s1,d_s2,d_s3)."
      },
      "description": "Critical crystal fields where first-order transitions occur in the Mn sublattice magnetisation."
    },
    {
      "file": "rcp_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["He","RCP"],
        "description": "RCP values as a function of reduced external field."
      },
      "description": "Relative cooling power for different applied magnetic field strengths."
    },
    {
      "file": "rcp_vs_ds.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["d_s","RCP"],
        "description": "RCP values as a function of reduced crystal field."
      },
      "description": "Relative cooling power for different crystal field values."
    },
    {
      "file": "rcp_vs_R1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["R1","RCP"],
        "description": "RCP values as a function of reduced Nd-Mn exchange."
      },
      "description": "Relative cooling power for different Nd-Mn exchange strengths."
    },
    {
      "file": "rcp_vs_R2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["R2","RCP"],
        "description": "RCP values as a function of reduced Mn-Mn exchange."
      },
      "description": "Relative cooling power for different Mn-Mn exchange strengths."
    }
  ],
  "notes": "Artifacts are scored based on structural features (plateaus, monotonic trends) and critical field values compared against paper-reported reference (tolerance ±1.0)."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact.  The `magnetization_plateaus.csv` is checked for correct columns, row count, and the presence of step‑like plateaus.  The `critical_ds.txt` file is compared against reference transition values (within an appropriate tolerance).  Each RCP CSV file is examined for correct columns and for the expected qualitative dependence of RCP on the varied parameter (monotonic trend or otherwise) against hidden reference patterns.  The verifier also confirms that all required files exist and contain the expected number of rows.  The final reward is a weighted sum of these checks, with the greatest weight on the critical crystal fields and the RCP trends.