# Thermoelectric Transport Properties of Ga1-xInxN Alloys

## Problem background
Gallium indium nitride (Ga1-xInxN) alloys in the cubic zinc-blende phase are of significant interest for optoelectronic and thermoelectric applications because their electronic band gap and transport coefficients can be tuned by adjusting the composition x. The zinc-blende modification is thermodynamically stable and offers large optical gain and low threshold current, making it a suitable candidate for high-performance devices. The electronic structure, optical response, and thermoelectric properties of this alloy system are not fully characterized over the full composition range, and a systematic computational investigation can reveal how the direct band gap, dielectric constant, Seebeck coefficient, and thermoelectric figure of merit depend on the In fraction.

## Approach
The reproduction is carried out by constructing atomic supercells for four compositions (x = 0, 0.25, 0.50, 0.75) in the zinc-blende structure. The electronic band structure is calculated using density functional theory (DFT) with the modified Becke–Johnson (mBJ) exchange-correlation potential, which provides accurate band gaps for semiconductors. From the converged electronic structure, the frequency-dependent dielectric function is computed to obtain the static dielectric constant; for the pure GaN case, the static refractive index is derived. The semiclassical Boltzmann transport equation is then solved using the constant relaxation time approximation to extract the Seebeck coefficient (at 100 K) and, for pure GaN, the dimensionless figure of merit ZT (at 300 K). The entire workflow builds on open-source tools: Quantum ESPRESSO for DFT and BoltzTrap for transport, with publicly available pseudopotentials and lattice parameters for the zinc-blende GaN and InN endpoints.

## Reproduction target
For the four compositions Ga1-xInxN with x = 0, 0.25, 0.50, and 0.75 in the zinc-blende structure, compute the following quantities:

- the direct band gap (at the Gamma point) in eV,
- the static dielectric constant (dimensionless),
- the Seebeck coefficient at 100 K (in μV/K).

Additionally, for the pure GaN composition (x = 0) only, compute:
- the static refractive index (dimensionless),
- the thermoelectric figure of merit ZT at 300 K (dimensionless).

All computed values must be written into a single CSV file at `/app/outputs/computed_properties.csv` with the columns:
`composition`, `band_gap_eV`, `static_dielectric_constant`, `n0_static`, `Seebeck_100K_uV_K`, `ZT_300K`.
For the columns `n0_static` and `ZT_300K`, fill the entries for non‑pure GaN compositions with `NaN`; all other columns must contain a valid float for every composition.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTrap: https://www.icams.de/content/research/boltzTraP/
- mBJ pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Zinc-blende GaN and InN lattice parameters

## Workflow steps

### Step 1: Build zinc-blende supercells for all compositions
- Role: process
- Action: Construct 8-atom cubic supercells for Ga1-xInxN at compositions x = 0, 0.25, 0.50, 0.75 in the zinc-blende structure. Use publicly known lattice constants for GaN (~4.50 Å) and InN (~4.98 Å), linearly interpolated for intermediate compositions. Arrange the atoms to substitute Ga by In while preserving cubic symmetry.
- Evidence: `/app/outputs/supercell_build.log`

### Step 2: DFT band structure calculation with mBJ potential
- Role: process
- Action: For each composition, perform DFT calculations using an open-source code (e.g., Quantum ESPRESSO) with the modified Becke–Johnson (mBJ) exchange-correlation potential. Converge the self-consistent field cycle and obtain the Kohn–Sham eigenvalues along high-symmetry k-paths, including the Gamma point. Identify the direct band gap (E_g^{Gamma-Gamma}) for each x.
- Evidence: `/app/outputs/dft_bands.dat`

### Step 3: Compute optical constants and static dielectric constant
- Role: process
- Action: From the DFT band structure and momentum matrix elements, calculate the frequency-dependent dielectric function. Apply the Kramers–Kronig transformation to obtain the real part and extract the static dielectric constant epsilon(0). For the pure GaN composition (x=0), also compute the static refractive index n(0) from n(0) = sqrt(epsilon(0)).
- Evidence: `/app/outputs/optical_results.txt`

### Step 4: Thermoelectric transport simulation using BoltzTrap
- Role: process
- Action: Feed the DFT band dispersion into the BoltzTrap code. For each composition, compute the transport tensors assuming a constant relaxation time (temperature‑ and energy‑dependent). Extract the Seebeck coefficient S at a temperature of 100 K. For the pure GaN (x=0) case, extract the dimensionless figure of merit ZT at 300 K. (For other compositions, ZT is not required.)
- Evidence: `/app/outputs/transport_output.log`

### Step 5: Compile final property CSV
- Role: scored (load-bearing)
- Action: Gather the computed direct band gaps, static dielectric constants, static refractive index (for x=0), Seebeck coefficients at 100 K, and ZT at 300 K (for x=0) from the preceding steps. Write them into a single CSV file /app/outputs/computed_properties.csv with the columns: composition, band_gap_eV, static_dielectric_constant, n0_static, Seebeck_100K_uV_K, ZT_300K. For values that are not applicable (n0_static and ZT_300K for non‑pure GaN compositions), fill the cells with NaN.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: CSV with columns: composition (string, one of 'GaN','Ga0.75In0.25N','Ga0.5In0.5N','Ga0.25In0.75N'), band_gap_eV (float), static_dielectric_constant (float), n0_static (float, only required for 'GaN', NaN otherwise), Seebeck_100K_uV_K (float), ZT_300K (float, only required for 'GaN', NaN otherwise).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing computed electronic, optical, and thermoelectric properties for each Ga1-xInxN composition (x = 0, 0.25, 0.50, 0.75). The checker will compare these values to hidden paper‑reported reference values with tolerances and verify the monotonic decrease of band gap with increasing In content.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `band_gap_eV`, `static_dielectric_constant`, `n0_static`, `Seebeck_100K_uV_K`, `ZT_300K`
  - `units`:
    - `band_gap_eV`: eV
    - `static_dielectric_constant`: dimensionless
    - `n0_static`: dimensionless
    - `Seebeck_100K_uV_K`: uV/K
    - `ZT_300K`: dimensionless

Notes: Computed properties must be derived from the preceding DFT, optical, and Boltzmann transport steps. The checker uses the paper‑reported values as a hidden reference; tolerances are not disclosed. Invalid or missing values for mandatory entries (all except n0_static and ZT_300K when not applicable) result in a zero score for that property.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "band_gap_eV",
          "static_dielectric_constant",
          "n0_static",
          "Seebeck_100K_uV_K",
          "ZT_300K"
        ],
        "units": {
          "band_gap_eV": "eV",
          "static_dielectric_constant": "dimensionless",
          "n0_static": "dimensionless",
          "Seebeck_100K_uV_K": "uV/K",
          "ZT_300K": "dimensionless"
        }
      },
      "description": "CSV file containing computed electronic, optical, and thermoelectric properties for each Ga1-xInxN composition (x = 0, 0.25, 0.50, 0.75). The checker will compare these values to hidden paper‑reported reference values with tolerances and verify the monotonic decrease of band gap with increasing In content."
    }
  ],
  "notes": "Computed properties must be derived from the preceding DFT, optical, and Boltzmann transport steps. The checker uses the paper‑reported values as a hidden reference; tolerances are not disclosed. Invalid or missing values for mandatory entries (all except n0_static and ZT_300K when not applicable) result in a zero score for that property."
}
```

## How you are scored
A hidden verifier will independently score the required output artifact (`computed_properties.csv`). The verifier compares each of the reported numerical entries against reference values for the same quantity, conditions, and units, using appropriate tolerances. It also checks that the band gap values satisfy a physically expected structural trend with respect to composition (without revealing the exact reference values). Missing, incorrectly typed, or invalid entries will receive zero credit for that property. The overall reward is a weighted combination of the individual property scores, where the band gap, dielectric constant, Seebeck coefficient, and ZT carry the main weight, and the static refractive index provides a smaller contribution. The reward is strictly monotonic in quality: a result that is consistent with the expected physical behaviour and matches the hidden references will earn the highest score. No gold values or tolerances are disclosed in these instructions.
