# Mössbauer parameters for Fe in BaTiO3 via 4s electric-field polarization

## Problem background
The Mössbauer spectrum of Fe³⁺ ions in ferroelectrics can exhibit abrupt changes in isomer shift and quadrupolar splitting at the Curie temperature. One proposed mechanism is that the strong internal electric field in ferroelectrics polarizes the covalently occupied 4s shell of the Fe³⁺ ion, thereby altering the electron density at the nucleus (affecting the isomer shift) and the electric field gradient (affecting the quadrupolar splitting). This task evaluates that mechanism for Fe³⁺-doped BaTiO₃ by computing the Mössbauer parameters from first principles, using published crystal structures, free-ion wavefunctions, and nuclear constants. The goal is to compute the isomer shift discontinuity at the phase transition, the total and 4s‑contribution to the quadrupolar splitting at 20 °C, and the temperature dependence of the quadrupolar splitting in the ferroelectric phase.

## Approach
The calculations follow a computational model that quantifies the polarization of the Fe³⁺ 4s shell under an electric field. Using publicly available crystal structure data for the cubic and tetragonal phases of BaTiO₃, along with free‑ion wavefunctions for Fe³⁺ and O²⁻, the method proceeds in several stages. First, overlap integrals between the Fe 4s orbital and the ligand 2p orbitals are computed via the α‑function technique; these are used to obtain a normalization constant for the octahedral complex. Second, the two‑level mixing of the 4s and 4p states in an external electric field is parameterized, yielding field‑dependent mixing coefficients. Third, the electric field gradient (EFG) at the iron nucleus is calculated from two sources: (i) the nearest‑neighbour octahedral complex, including overlap effects through Löwdin orthogonalization and Sternheimer screening, and (ii) the remainder of the lattice, obtained by subtracting the nearest‑oxygen monopole/dipole contributions from the total lattice EFG. With these ingredients and the known nuclear constants (isomer shift calibration constant and quadrupole moment), the discontinuous isomer shift change at Tc and the quadrupolar splitting at 20 °C are computed, and the contribution of the polarized 4s shell and the 4p Sternheimer screening factor are extracted. Finally, the temperature dependence of the quadrupolar splitting is modeled by assuming that the local electric field scales with the spontaneous polarization, using published P_s(T) data.

## Reproduction target
Produce the following Mössbauer parameters for Fe³⁺ in BaTiO₃:
(i) the discontinuous change of the isomer shift at the Curie temperature, computed with an internal‑field change of 4.5 × 10⁸ V cm⁻¹;
(ii) the total quadrupolar splitting at 20 °C and the portion contributed by the electrically polarized 4s shell;
(iii) the 4p Sternheimer screening factor R₄ₚ deduced from the 4s contribution;
(iv) the quadrupolar splitting at several temperatures (20, 40, 60, 80, 100 °C) in the tetragonal phase, incorporating the 4s‑polarization contribution.
The work uses published crystal structures, free‑ion wavefunctions, nuclear constants, Sternheimer factors, and spontaneous polarization data. All final quantities are saved in the specified output files.

## Assets

- BaTiO3 crystal structure data (20°C and near Tc): 10.1080/14786440908520316;10.1103/PhysRev.100.745;10.1016/0022-3697(66)90164-3
- Fe3+ and O2- free-ion radial wavefunctions: 10.1103/PhysRev.111.1108;10.1063/1.1704126
- Nuclear constants for 57Fe (isomer shift calibration and quadrupole moment): 10.1103/PhysRevLett.33.480;10.1103/PhysRev.188.1045
- Sternheimer screening factors for Fe3+ (R_3d,R_3p,R_2p): 10.1002/pssb.2220670118;10.1002/pssb.2220760228
- Spontaneous polarization data P_s(T) for BaTiO3: 10.1103/PhysRev.91.513
- Alpha-function technique for overlap integrals: 10.1063/1.1704127

## Workflow steps

### Step 1: Compute overlap integrals and normalization constant
- Role: process
- Action: Using the α-function technique (Sharma 1968) and published Fe3+/O2- wavefunctions, compute the overlap integrals S_ns (n=1..4) between Fe 4s and oxygen 2p orbitals for the octahedral complex in both cubic and tetragonal phases, and derive the normalization constant N. Save the values as evidence.
- Evidence: `/app/outputs/overlap_integrals.json`

### Step 2: Compute 4s-4p electric-field mixing parameters
- Role: process
- Action: Using free-ion Fe3+ wavefunctions and energies, compute the matrix element B = ⟨φ_4s|z|φ_4p⟩, the factor (2eB/Δε)^2, and the field-dependent coefficients a(E), b(E) for the electric fields at Tc (4.5×10⁸ V/cm) and at 20°C (8×10⁸ V/cm). Save the results as evidence.
- Evidence: `/app/outputs/mixing_params.json`

### Step 3: Compute lattice and octahedral complex EFG at 20°C
- Role: process
- Action: Compute the electric field gradient (EFG) at the 57Fe nucleus for BaTiO3 at T=20°C: (a) from the octahedral complex using Löwdin orthogonalization including overlap, with Sternheimer screening; (b) from the remaining lattice by subtracting nearest-oxygen monopole/dipole contributions from the total lattice EFG. Save the two components q_compl and q_latt in atomic units as evidence.
- Evidence: `/app/outputs/efg_components.json`

### Step 4: Compute Mössbauer parameters at 20°C
- Role: scored (load-bearing)
- Action: Using the overlap integrals, mixing coefficients, and EFG components from previous steps, together with the nuclear quadrupole moment Q=+0.21 b, the isomer shift calibration constant α=-0.23 a₀⁻³ mm/s, and an occupation ρ_4s=0.2, compute: (i) the discontinuous isomer shift change at Tc; (ii) the quadrupolar splitting from lattice+complex alone; (iii) the polarized-4s contribution to quadrupolar splitting at 20°C using E=8×10⁸ V/cm; (iv) the total quadrupolar splitting at 20°C; (v) the 4p Sternheimer screening factor R_4p extracted from the attributed 4s contribution. Save all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with required numeric fields: isomer_shift_change (mm/s), quadrupolar_splitting_total (mm/s), quadrupolar_splitting_4s_contribution (mm/s), R_4p (dimensionless), E_para (V/cm), rho_4s.
- Scoring: scored by hidden verifier

### Step 5: Compute temperature dependence of quadrupolar splitting
- Role: scored
- Action: Using the lattice+complex EFG contribution (fixed from previous step), the 4s-polarization formula with the local electric field assumed proportional to the spontaneous polarization P_s(T) from Merz (1953), and the determined R_4p, compute the total quadrupolar splitting at temperatures 20, 40, 60, 80, 100 °C. Save the results as a CSV file temp_dependence.csv with columns T_C and QS_mm_s.
- Output file: `/app/outputs/temp_dependence.csv`
- Format: csv
- Contract: CSV with columns: T_C (int, °C), QS_mm_s (float, mm/s).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/temp_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored values: isomer shift discontinuous change at Tc, quadrupolar splitting decomposition, and deduced 4p screening factor.
- schema:
  - `type`: object
  - `required`:
    - `isomer_shift_change`: number
    - `quadrupolar_splitting_total`: number
    - `quadrupolar_splitting_4s_contribution`: number
    - `R_4p`: number
    - `E_para`: number
    - `rho_4s`: number
  - `units`:
    - `isomer_shift_change`: mm/s
    - `quadrupolar_splitting_total`: mm/s
    - `quadrupolar_splitting_4s_contribution`: mm/s
    - `R_4p`: dimensionless
    - `E_para`: V/cm
    - `rho_4s`: dimensionless

### temp_dependence.csv
- path: `/app/outputs/temp_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature dependence of quadrupolar splitting. Compare each row's QS to reference values and verify monotonic trend.
- schema:
  - `type`: table
  - `required_columns`: `T_C`, `QS_mm_s`
  - `units`:
    - `T_C`: °C
    - `QS_mm_s`: mm/s

Notes: All computed Mössbauer parameters are deterministic given the public inputs and the described procedures. The hidden checker compares the reported values to paper-derived gold values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "isomer_shift_change": "number",
          "quadrupolar_splitting_total": "number",
          "quadrupolar_splitting_4s_contribution": "number",
          "R_4p": "number",
          "E_para": "number",
          "rho_4s": "number"
        },
        "units": {
          "isomer_shift_change": "mm/s",
          "quadrupolar_splitting_total": "mm/s",
          "quadrupolar_splitting_4s_contribution": "mm/s",
          "R_4p": "dimensionless",
          "E_para": "V/cm",
          "rho_4s": "dimensionless"
        }
      },
      "description": "Scored values: isomer shift discontinuous change at Tc, quadrupolar splitting decomposition, and deduced 4p screening factor."
    },
    {
      "file": "temp_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_C",
          "QS_mm_s"
        ],
        "units": {
          "T_C": "°C",
          "QS_mm_s": "mm/s"
        }
      },
      "description": "Temperature dependence of quadrupolar splitting. Compare each row's QS to reference values and verify monotonic trend."
    }
  ],
  "notes": "All computed Mössbauer parameters are deterministic given the public inputs and the described procedures. The hidden checker compares the reported values to paper-derived gold values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. For results.json the verifier compares the reported isomer‑shift change, total quadrupolar splitting, and 4s‑contribution quadrupolar splitting against reference intervals derived from the original computational study. For temp_dependence.csv the verifier compares the quadrupolar splitting at each temperature to reference values and confirms that the values follow a physically expected monotonic trend. Each scored stage contributes a specific weight to the total reward. A solution that merely writes a constant number without executing the described computational pipeline will generally not satisfy the reference checks.
