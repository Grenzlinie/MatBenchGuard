# Thermal Interface Conductance Trends in Lennard-Jones Solids

## Problem background
Thermal interface conductance (TIC) is a key property for heat management across material interfaces in nanostructures. The standard harmonic intuition relates TIC to the overlap of the bulk phonon density of states (DoS) of the two materials: the more their vibrational frequencies coincide, the higher the conductance. However, whether this picture holds across a broad range of mass and stiffness mismatches remains an open computational question. This work addresses it by systematically studying a family of lattice-matched Lennard-Jones solid/solid interfaces, where mass and stiffness can be varied independently while avoiding lattice mismatch complications. The investigation involves computing TIC via equilibrium molecular dynamics and comparing the results to several overlap-based descriptors and harmonic models.

## Approach
Construct a grid of FCC LJ interfaces with solid argon on one (constant) side. On the other (varying) side, independently set the atomic mass m and the potential well depth ε from 1× to 10× the argon reference values (at a resolution of 1.0), yielding at least 100 distinct interfaces. For each interface, run equilibrium molecular dynamics (EMD) at T=40 K and compute the TIC from the temporal autocorrelation of the interfacial heat flow (fluctuation-dissipation relation). Also compute, for each interface, the overlap of the bulk phonon DoS (via lattice dynamics) and the overlap of the interfacial power spectra (IPS) derived from the velocity trajectories of the interfacial atoms. Additional harmonic-model predictions (DMM and AMM) at 40 K are obtained using Debye properties. For the subset of interfaces with ε/ε_Ar > 5 and m/m_Ar < 2, perform the same EMD at T=5 K to probe temperature-dependent behavior. The pipeline culminates in a single CSV that enables a quantitative comparison between the EMD-derived TIC and the various overlap/model predictions.

## Reproduction target
Produce a single CSV file `/app/outputs/results.csv` with at least 100 rows (one per interface) and exactly these columns: m_ratio, eps_ratio, TIC_EMD_40K (MW/m²K), bulk_DoS_overlap, DMM_TIC_40K (MW/m²K), AMM_TIC_40K (MW/m²K), IPS_overlap, TIC_EMD_5K (MW/m²K; NaN when not simulated), high_mismatch (boolean, True when ε/ε_Ar>5 and m/m_Ar<2, else False). From this table one can compute: (1) the Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap across all interfaces, (2) the Spearman rank correlation between TIC_EMD_40K and IPS_overlap, and (3) for the rows where high_mismatch is True, the ratio of the mean TIC_EMD_40K to the mean TIC_EMD_5K.

## Assets

- LAMMPS: https://www.lammps.org
- LJ parameters for solid argon (Sarkar & Selvam 2007): 10.1063/1.2771242

## Workflow steps

### Step 1: System construction
- Role: process
- Action: Generate atomic configurations for a grid of lattice-matched FCC Lennard-Jones interfaces: the constant side is solid argon; the varying side independently varies mass m and stiffness ε from 1× to 10× the argon values with a resolution of 1.0 in each direction, yielding at least 100 distinct interfaces. Use FCC lattice, 3×3×20 unit cells per side, [100] interface normal, periodic boundary conditions, LJ cutoff 3σ_Ar. Prepare LAMMPS input scripts for each system.
- Evidence: `/app/outputs/systems_manifest.csv`

### Step 2: Bulk lattice dynamics and DoS overlap
- Role: process
- Action: For each varying-side material, compute its bulk phonon DoS via lattice dynamics. Then calculate the bulk DoS overlap S = (∫ DoS_const(ω) DoS_vary(ω) dω) / (∫ DoS_const(ω) dω · ∫ DoS_vary(ω) dω) between the constant argon side and each varying side.
- Evidence: `/app/outputs/bulk_dos_overlap.csv`

### Step 3: DMM and AMM predictions
- Role: process
- Action: Using Debye parameters derived from the LJ properties, compute DMM and AMM TIC at T=40 K for every interface. Use isotropic Debye model, elastic interactions, and evaluate the DMM integral on the softer side.
- Evidence: `/app/outputs/dmm_amm_predictions.csv`

### Step 4: EMD at 40 K
- Role: process
- Action: For each interface, run LAMMPS equilibrium molecular dynamics at T=40 K: equilibration 0.5 ns NPT, 0.5 ns NVT, production 3 ns NVE, timestep 0.15 fs, LJ cutoff 3σ_Ar. Average over 20 ensembles (different initial random velocities). From the trajectories, compute the interfacial heat flow Q(t) = (1/2) Σ_{i∈A, j∈B} f_ij · (v_i + v_j). Then compute TIC via the autocorrelation: G = (1 / (k_B · A · T^2)) · ∫₀^∞ ⟨Q(0) Q(t)⟩ dt. Save per-system TIC values.
- Evidence: `/app/outputs/tic_40K_per_system.csv`

### Step 5: Interfacial power spectra overlap
- Role: process
- Action: From the velocity trajectories of interfacial atoms produced in step 04, for each atom compute the power spectrum P_α(ω) = |∫ v_α(t) e^{-iωt} dt|² for each Cartesian direction α, average over atoms and directions to obtain the interfacial power spectrum (IPS). Then compute the overlap between the two sides' IPS using S = (∫ IPS_1(ω) IPS_2(ω) dω) / (∫ IPS_1(ω) dω · ∫ IPS_2(ω) dω). Store the IPS overlap for each interface.
- Evidence: `/app/outputs/ips_overlap_per_system.csv`

### Step 6: EMD at 5 K for high stiffness mismatch
- Role: process
- Action: For interfaces with ε/ε_Ar > 5 and m/m_Ar < 2 (high stiffness mismatch), run EMD at T=5 K using the same protocols as step 04. Compute TIC at 5 K.
- Evidence: `/app/outputs/tic_5K_per_system.csv`

### Step 7: IPSA prediction at 40 K
- Role: process
- Action: Using the interfacial power spectra (IPS) from step 05 and the DMM formulation, compute IPSA TIC at T=40 K for every interface. The formula is G_IPSA = (1/4) Σ_j v_{1,j} ∫₀^{ω^c_{1,j}} α_1(ω) ℏ ω D_{1,j}(ω) (∂n/∂T) dω, with α_1(ω) = (Σ_j v_{2,j} D^{int}_{2,j}(ω)) / (Σ_j v_{2,j} D^{int}_{2,j}(ω) + Σ_j v_{1,j} D^{int}_{1,j}(ω)), where indices 1 and 2 refer to the softer and stiffer sides, v_{i,j} are the bulk Debye velocities from step 03, D^{int}_{i,j} are the interfacial power spectra, and n(ω,T) is the classical distribution. Save the IPSA TIC for each interface.
- Evidence: `/app/outputs/ipsa_tic_40K.csv`

### Step 8: Compile final results table
- Role: scored (load-bearing)
- Action: Combine all computed quantities into a single CSV file. Include columns: m_ratio, eps_ratio, TIC_EMD_40K (MW/m^2K), bulk_DoS_overlap (dimensionless), DMM_TIC_40K (MW/m^2K), AMM_TIC_40K (MW/m^2K), IPS_overlap (dimensionless), IPSA_TIC_40K (MW/m^2K). For the subset simulated at 5 K, also include TIC_EMD_5K (MW/m^2K; NaN for others) and a boolean column high_mismatch (True if ε/ε_Ar>5 and m/m_Ar<2, else False). Every interface generated in step 01 must appear in this file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: m_ratio (float), eps_ratio (float), TIC_EMD_40K (float, MW/m^2K), bulk_DoS_overlap (float), DMM_TIC_40K (float, MW/m^2K), AMM_TIC_40K (float, MW/m^2K), IPS_overlap (float), IPSA_TIC_40K (float, MW/m^2K), TIC_EMD_5K (float, NaN if not simulated), high_mismatch (boolean, True/False).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Final table containing all computed quantities for every interface in the grid, from which the checker recomputes Spearman rank correlations, the 40K/5K TIC ratio, and IPSA–EMD agreement.
- schema:
  - `type`: table
  - `required_columns`: `m_ratio`, `eps_ratio`, `TIC_EMD_40K`, `bulk_DoS_overlap`, `DMM_TIC_40K`, `AMM_TIC_40K`, `IPS_overlap`, `IPSA_TIC_40K`, `TIC_EMD_5K`, `high_mismatch`
  - `units`:
    - `TIC_EMD_40K`: MW/m^2K
    - `DMM_TIC_40K`: MW/m^2K
    - `AMM_TIC_40K`: MW/m^2K
    - `IPSA_TIC_40K`: MW/m^2K
    - `TIC_EMD_5K`: MW/m^2K

Notes: The checker will compute (1) Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap, (2) Spearman rank correlation between TIC_EMD_40K and IPS_overlap, (3) for the high_mismatch subset the mean TIC_EMD_40K/mean TIC_EMD_5K ratio, and (4) Spearman rank correlation between TIC_EMD_40K and IPSA_TIC_40K. Threshold tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
      "description": "Final table containing all computed quantities for every interface in the grid, from which the checker recomputes Spearman rank correlations, the 40K/5K TIC ratio, and IPSA–EMD agreement."
    }
  ],
  "notes": "The checker will compute (1) Spearman rank correlation between TIC_EMD_40K and bulk_DoS_overlap, (2) Spearman rank correlation between TIC_EMD_40K and IPS_overlap, (3) for the high_mismatch subset the mean TIC_EMD_40K/mean TIC_EMD_5K ratio, and (4) Spearman rank correlation between TIC_EMD_40K and IPSA_TIC_40K. Threshold tolerances are hidden."
}
```

## How you are scored
A hidden verifier reads your `results.csv`. It independently computes the two Spearman rank correlations (TIC_EMD_40K vs bulk_DoS_overlap, TIC_EMD_40K vs IPS_overlap) and, for the high_mismatch subset, the mean TIC ratio (40K / 5K). Each of these quantities is compared to a hidden threshold that reflects the qualitative relationship expected from a faithful re-derivation (e.g., a correlation below a low threshold, or above a high threshold, or a ratio exceeding a value). The final score is the proportion of checks that pass (range 0–1). You do not need to guess the original paper's exact numbers; the tolerance bands are set to accept a correctly reproduced trend.
