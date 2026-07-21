# Thermal Interface Conductance Trends in Lennard-Jones Solids

## Problem background
Thermal interface conductance (TIC) is a key property for heat management across material interfaces in nanostructures. The standard harmonic intuition relates TIC to the overlap of the bulk phonon density of states (DoS) of the two materials: the more their vibrational frequencies coincide, the higher the conductance. However, whether this picture holds across a broad range of mass and stiffness mismatches remains an open computational question. This work addresses it by systematically studying a family of lattice-matched Lennard-Jones solid/solid interfaces, where mass and stiffness can be varied independently while avoiding lattice mismatch complications. The investigation involves computing TIC via equilibrium molecular dynamics and comparing the results to several overlap-based descriptors and harmonic models.

## Approach
Construct a grid of FCC LJ interfaces with solid argon on one (constant) side. On the other (varying) side, independently set the atomic mass m and the potential well depth ε from 1× to 10× the argon reference values (at a resolution of 1.0 in each direction), yielding at least 100 distinct interfaces. For each interface, run equilibrium molecular dynamics (EMD) at T = 40 K and compute the TIC from the temporal autocorrelation of the interfacial heat flow (fluctuation‑dissipation relation). Also compute, for each interface, the overlap of the bulk phonon DoS (via lattice dynamics) and the overlap of the interfacial power spectra (IPS) derived from the velocity trajectories of the interfacial atoms. Additional harmonic-model predictions (DMM and AMM) at 40 K are obtained using Debye properties. For the subset of interfaces with ε/ε_Ar > 5 and m/m_Ar < 2, perform the same EMD at T = 5 K to probe temperature-dependent behavior. The pipeline culminates in a single CSV that enables a quantitative comparison between the EMD-derived TIC and the various overlap/model predictions.

## Reproduction target
Produce a single CSV file `/app/outputs/results.csv` with at least 100 rows (one per interface) and exactly these columns:

| Column           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| m_ratio          | Mass ratio: m / m_Ar                                                        |
| eps_ratio        | Stiffness ratio: ε / ε_Ar                                                   |
| TIC_EMD_40K      | EMD TIC at 40 K (MW/m² K)                                                  |
| bulk_DoS_overlap | Bulk phonon DoS overlap (dimensionless)                                     |
| DMM_TIC_40K      | DMM TIC at 40 K (MW/m² K)                                                  |
| AMM_TIC_40K      | AMM TIC at 40 K (MW/m² K)                                                  |
| IPS_overlap      | Interfacial power spectrum overlap (dimensionless)                          |
| IPSA_TIC_40K     | IPSA TIC at 40 K (MW/m² K) — required column; values **not used in scoring** |
| TIC_EMD_5K       | EMD TIC at 5 K (MW/m² K); NaN when not simulated                           |
| high_mismatch    | Boolean: True when ε/ε_Ar > 5 and m/m_Ar < 2, else False                   |

From this table one can compute:
1. the Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap across all interfaces,
2. the Spearman rank correlation between TIC_EMD_40K and IPS_overlap, and
3. for the rows where high_mismatch is True, the ratio of the mean TIC_EMD_40K to the mean TIC_EMD_5K.

These three quantities are what the hidden verifier scores. The **IPSA_TIC_40K column must be present but its numerical values are not evaluated**; you may fill it with any float (e.g., NaN, 0.0, or a physically motivated estimate).

## Key physical parameters (self-contained)
All the parameters needed to run the simulations are given below. No external lookup is necessary.

**Argon reference Lennard-Jones parameters**  
(see, e.g., *Sarkar & Selvam, J. Chem. Phys.* 127, 074702 (2007))  

| Parameter            | Symbol   | Value (real units)           | Value (metal‑like SI)          |
|----------------------|----------|------------------------------|-------------------------------|
| Length parameter     | σ_Ar     | 3.405 Å                      | 3.405 × 10⁻¹⁰ m              |
| Energy parameter     | ε_Ar     | 119.8 K (in energy units: 0.238 kcal/mol) | 0.0103 eV (= 1.65 × 10⁻²¹ J) |
| Mass                 | m_Ar     | 39.948 g/mol                 | 6.634 × 10⁻²⁶ kg             |

**Cross‑species mixing rules**  
σ₁₂ = (σ₁ + σ₂)/2 , ε₁₂ = √(ε₁ · ε₂) .

**Units for LAMMPS**  
Use the `real` unit style: length = Å, energy = kcal/mol, mass = g/mol, time = fs, temperature = K, pressure = atm.  

- Boltzmann constant: k_B = 1.9872 × 10⁻³ kcal/mol·K (or 8.6173 × 10⁻⁵ eV/K).
- Cutoff radius: r_cut = 3 σ_Ar = 10.215 Å.
- Time step: 0.15 fs.

**Cross‑sectional area A**  
The interface normal is the [100] direction (z). The cross section A is the equilibrium transverse area of the simulation box:  
A = Lx × Ly , where Lx, Ly are the final box lengths obtained after the NPT equilibration (step 4).  
The constant and varying sides have the same σ, therefore the same equilibrium lattice constant, so the cross section is uniform.

**Lattice constant approximation**  
To construct the initial FCC lattice you can start with an approximate lattice constant a = 5.26 Å (typical for LJ solid argon at 0 K). The NPT equilibration will adjust the box dimensions to the true zero‑pressure value, from which you must take Lx, Ly and use them in the TIC formula.

## Workflow steps (intermediate files are not required for submission — only results.csv is scored)

### Step 1: System construction
- Action: Generate atomic configurations for a grid of lattice‑matched FCC LJ interfaces. The constant side is solid argon; the varying side independently varies mass m and stiffness ε from 1× to 10× the argon values with a resolution of 1.0, yielding at least 100 interfaces. Use FCC lattice, 3×3×20 unit cells per side, [100] interface normal, periodic boundary conditions, LJ cutoff 3 σ_Ar. Include cross‑species interactions using the mixing rules. Prepare LAMMPS input scripts for each system.  
  (Intermediate output, not scored: a manifest file listing the interface parameters.)

### Step 2: Bulk lattice dynamics and DoS overlap
- Action: For each varying‑side material, compute its bulk phonon DoS via lattice dynamics (e.g., using Dynamical Matrix approach or fix phonon in LAMMPS). Then calculate the bulk DoS overlap
    S = (∫ DoS_const(ω) DoS_vary(ω) dω) / (∫ DoS_const(ω) dω · ∫ DoS_vary(ω) dω)
  between the constant argon side and each varying side.  
  (Not scored; results go into the final table.)

### Step 3: DMM and AMM predictions
- Action: Using Debye parameters derived from the LJ properties, compute DMM and AMM TIC at T = 40 K for every interface. Use an isotropic Debye model, elastic interactions, and evaluate the DMM integral on the softer side.  
  (Not scored.)

### Step 4: EMD at 40 K
- Action: For each interface, run LAMMPS equilibrium molecular dynamics at T = 40 K:
  - Equilibration: 0.5 ns NPT (zero pressure), then 0.5 ns NVT.
  - Production: 3 ns NVE, time step 0.15 fs, LJ cutoff 3 σ_Ar.
  - Average over 20 independent ensembles (different random initial velocities).
  - From the trajectories, compute the interfacial heat flow  
    Q(t) = 1/2 Σ_{i∈A, j∈B} f_ij · (v_i + v_j)
    (can use the `compute heat/flux` command in LAMMPS with appropriate groups).
  - Then compute TIC via the autocorrelation (use the equilibrium (NVE) output):
    G = (1 / (k_B · A · T²)) ∫₀^∞ ⟨Q(0) Q(t)⟩ dt .
    The cross‑sectional area A is obtained from the final NPT box dimensions (A = Lx × Ly).
  - Convert G to MW/m² K before writing to the final table.

### Step 5: Interfacial power spectra overlap
- Action: From the velocity trajectories of interfacial atoms produced in Step 4, for each atom compute the power spectrum
    P_α(ω) = |∫ v_α(t) e^{‑iωt} dt|²
  for each Cartesian direction α, average over atoms and directions to obtain the interfacial power spectrum (IPS). Then compute the overlap between the two sides' IPS using the same overlap formula as in Step 2. Store the IPS overlap for each interface.

### Step 6: EMD at 5 K for high stiffness mismatch
- Action: For interfaces with ε/ε_Ar > 5 and m/m_Ar < 2, run EMD at T = 5 K using the same protocols as Step 4. Compute TIC at 5 K.

### Step 7: IPSA prediction at 40 K (optional for scoring)
- Action: The IPSA (Interfacial Power Spectrum Analysis) predicted TIC at 40 K is a harmonic‑model extension that uses the interfacial power spectra instead of bulk DoS. The column **must exist** in results.csv but its numerical values **do not affect the score**. You may fill the column with NaN (or 0.0) — whichever is easier. If you choose to implement the model from the original study, the general formula is:
    G_IPSA = 1/4 Σ_j v_{1,j} ∫₀^{ω^c_{1,j}} α₁(ω) ℏω D_{1,j}(ω) (∂n/∂T) dω ,
  with α₁(ω) = (Σ_j v_{2,j} D^{int}_{2,j}(ω)) / (Σ_j v_{2,j} D^{int}_{2,j}(ω) + Σ_j v_{1,j} D^{int}_{1,j}(ω)) ,
  where subscripts 1 and 2 denote the softer and stiffer side, v_{i,j} are the bulk Debye velocities (derived from the LJ elastic constants), D^{int}_{i,j} are the IPS, and n(ω,T) is the Bose‑Einstein distribution. Details of the Debye‑velocity calculation and integration limits can be found in the referenced paper.

### Step 8: Compile final results table
- Action (scored, load‑bearing): Combine all computed quantities into a single CSV file. Every interface generated in Step 1 must appear. Include all columns listed in the **Reproduction target** table. Ensure missing TIC_EMD_5K values are written as `NaN` (the string) and the boolean column as `True`/`False`.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Scoring: scored by hidden verifier (checks only columns TIC_EMD_40K, bulk_DoS_overlap, IPS_overlap, TIC_EMD_5K, high_mismatch; the other columns must be present but are ignored).

## Output contract
Every file the hidden verifier reads is described below. Write `/app/outputs/results.csv` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Final table containing all computed quantities for every interface in the grid, from which the checker recomputes Spearman rank correlations and the 40 K/5 K TIC ratio.
- schema:
  - type: table
  - required_columns:
    - m_ratio
    - eps_ratio
    - TIC_EMD_40K
    - bulk_DoS_overlap
    - DMM_TIC_40K
    - AMM_TIC_40K
    - IPS_overlap
    - IPSA_TIC_40K
    - TIC_EMD_5K
    - high_mismatch
  - units:
    - TIC_EMD_40K: MW/m² K
    - DMM_TIC_40K: MW/m² K
    - AMM_TIC_40K: MW/m² K
    - IPSA_TIC_40K: MW/m² K
    - TIC_EMD_5K: MW/m² K

## How you are scored
A hidden verifier reads your `results.csv`. It independently computes:
1. Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap,
2. Spearman rank correlation between TIC_EMD_40K and IPS_overlap,
3. For the high_mismatch subset, the ratio mean(TIC_EMD_40K) / mean(TIC_EMD_5K).

Each quantity is compared to a hidden threshold reflecting the qualitative trend expected from a faithful reproduction (low DoS correlation, high IPS correlation, TIC ratio > 1). The final score is the proportion of checks that pass (range 0–1). The tolerances are set to accept a correctly reproduced trend; you do not need to guess exact numbers from the original paper.

## Assets
- LAMMPS: https://www.lammps.org
- The LJ parameters for argon are provided above (σ_Ar, ε_Ar, m_Ar) — no external reference is needed.

## Self-check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks the output file `results.csv` against the contract: exists, CSV has the required columns. Fix any mismatch before finishing. This checks **shape only**; it does not judge scientific correctness.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m_ratio",
          "eps_ratio",
          "TIC_EMD_40K",
          "bulk_DoS_overlap",
          "DMM_TIC_40K",
          "AMM_TIC_40K",
          "IPS_overlap",
          "IPSA_TIC_40K",
          "TIC_EMD_5K",
          "high_mismatch"
        ],
        "units": {
          "TIC_EMD_40K": "MW/m^2K",
          "DMM_TIC_40K": "MW/m^2K",
          "AMM_TIC_40K": "MW/m^2K",
          "IPSA_TIC_40K": "MW/m^2K",
          "TIC_EMD_5K": "MW/m^2K"
        }
      },
      "description": "Final table containing all computed quantities for every interface in the grid, from which the checker recomputes Spearman rank correlations, the 40K/5K TIC ratio, and IPSA-EMD agreement."
    }
  ],
  "notes": "The checker will compute (1) Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap, (2) Spearman rank correlation between TIC_EMD_40K and IPS_overlap, and (3) for the high_mismatch subset the mean TIC_EMD_40K/mean TIC_EMD_5K ratio. Threshold tolerances are hidden."
}
```