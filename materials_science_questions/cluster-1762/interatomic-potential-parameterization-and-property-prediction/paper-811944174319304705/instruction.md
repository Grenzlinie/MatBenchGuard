# First-Order Displacive Phase Transition in VO2

## Problem background
Vanadium dioxide (VO₂) undergoes a first‑order displacive phase transition from a high‑temperature metallic rutile (R) phase to a low‑temperature insulating monoclinic (M₁) phase. The transformation involves a Peierls distortion along chains of edge‑sharing VO₆ octahedra and is of interest both for fundamental condensed‑matter physics and for potential applications (thermochromics, sensing, optical switching). A central challenge is to predict the critical transition temperature T_c and the energetic driving force between the two phases from atomistic simulations. In this task, you will use an empirical interatomic potential model and lattice‑dynamics calculations to map the free‑energy landscape over the soft‑phonon order parameters and determine these quantities.

## Approach
Use the General Utility Lattice Program (GULP). The interatomic interactions are described by a combination of Buckingham potentials (for V–O and O–O), a shell model for oxygen polarisability, and a Morse potential for V–V bonding along the chains. The potential parameters are listed below. You will relax the rutile structure, compute Γ‑point phonons, identify two degenerate soft modes, and find orthogonal displacement vectors e₁, e₂ that define order parameters L₁, L₂. By imposing L₁·e₁ + L₂·e₂ displacements and relaxing the cell parameters and oxygen shells, you will map the lattice energy surface. Then, within the quasi‑harmonic approximation, you will compute the phonon free energy at various temperatures over a grid of (L₁, L₂) values, excluding the soft modes. From these free energy surfaces locate the minima for the R and M₁ phases and obtain the temperature‑dependent free energy difference ΔF(T). The workflow culminates in two key results: the lattice energy difference ΔE between the M₁ and R phases, and the temperature T_c where the free energy difference crosses zero.

The interatomic potential parameters are:

| Interaction   | A (eV)   | ρ (Å)  | C (eV Å⁶) |
|---------------|----------|--------|------------|
| V–O           | 15585.5  | 0.1941 | 27.25      |
| O–O           | 23090.8  | 0.2342 | 29.80      |

Morse V–V parameters:

| Parameter | Value       |
|-----------|-------------|
| D (eV)    | 0.5270      |
| α (Å⁻¹)   | 11.720      |
| r₀ (Å)    | 2.620       |

Shell model: oxygen core charge +2.2 |e|, oxygen shell charge –2.32 |e| (q = 2.2, c = 0.12, s = 1.22), harmonic spring constant k = 9.85 keV Å⁻².

## Reproduction target
Produce the following two artifacts under `/app/outputs`:

* `lattice_energy_minimum_difference.json` – a JSON object with the key `"delta_E_eV_per_fu"`, containing the lattice energy difference per VO₂ formula unit (E_M₁ − E_R, in eV) computed from the energy landscape.
* `free_energy_difference.csv` – a CSV table with columns `"Temperature_K"` (float) and `"Delta_F_eV"` (float). This table must contain at least 10 temperature points covering a range that includes the expected transition region. The hidden checker will interpolate these data to find the temperature where ΔF ≈ 0 (T_c) and compare it against a reference.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Interatomic potential parameters for VO2 (Buckingham+Shell+Morse)
- Crystal structures of VO2 rutile (R) and monoclinic (M1) phases

## Workflow steps

### Step 1: Phonon calculation for rutile phase
- Role: process
- Action: Using GULP, relax the rutile structure of VO2 with the given interatomic potential parameters, then compute the Γ-point phonon frequencies and eigenvectors. Save the phonon output as evidence.
- Evidence: `/app/outputs/phonon_R.log`

### Step 2: Identify and orthogonalise soft phonon modes
- Role: process
- Action: From the phonon calculation, identify the two degenerate soft modes with dominant vanadium motion. Perform a circular-path energy scan in the subspace of these modes near the R phase to find the orthogonal displacement vectors e1 and e2 that correspond to the shallowest energy-increase directions. Record these eigenvectors as the basis for the order parameters L1, L2.
- Evidence: `/app/outputs/e1_e2_vectors.txt`

### Step 3: Map lattice energy and compute ΔE
- Role: scored (load-bearing)
- Action: For a grid of (L1, L2) values, impose the displacement pattern L1·e1 + L2·e2, relax the lattice parameters and oxygen shell positions with GULP, and record the minimized lattice energy for each point. From the resulting energy surface, identify the four symmetry-equivalent M1 minima (|L1|=|L2|>0) and the R phase origin (L1=L2=0). Compute the lattice energy difference ΔE = E(M1) − E(R) per VO2 formula unit. Save the value as a JSON file.
- Output file: `/app/outputs/lattice_energy_minimum_difference.json`
- Format: json
- Contract: {"delta_E_eV_per_fu": <float>}
- Scoring: scored by hidden verifier

### Step 4: Compute quasi‑harmonic free energy and extract Tc
- Role: scored (load-bearing)
- Action: For each (L1, L2) grid point from the previous step, compute phonon frequencies over the Brillouin zone (excluding soft modes), evaluate the harmonic free energy at several temperatures using the quasi-harmonic expression (standard formula). For each temperature, locate the free-energy minima corresponding to the R and M1 regions, compute the difference ΔF(T) = F(M1) − F(R). Output a CSV file with columns Temperature_K and Delta_F_eV. The critical temperature Tc is derived later by the checker from the ΔF(T) curve.
- Output file: `/app/outputs/free_energy_difference.csv`
- Format: csv
- Contract: Two columns: Temperature_K (float), Delta_F_eV (float). At least 10 temperature points.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energy_minimum_difference.json`
- `/app/outputs/free_energy_difference.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energy_minimum_difference.json
- path: `/app/outputs/lattice_energy_minimum_difference.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The lattice energy difference between the R and M1 phases, per formula unit.
- schema:
  - `type`: object
  - `required`: `delta_E_eV_per_fu`
  - `properties`:
    - `delta_E_eV_per_fu`:
      - `type`: number
      - `description`: Lattice energy difference per VO2 formula unit (eV)

### free_energy_difference.csv
- path: `/app/outputs/free_energy_difference.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Free energy difference ΔF(T) between the M1 and R phases at several temperatures. The checker interpolates to find the temperature where ΔF ≈ 0 (Tc).
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Delta_F_eV`
  - `row_count`: at least 10

Notes: The agent must run GULP for phonon calculations and many energy minimisations. All required inputs are public or provided inline. The scored artifacts are the lattice energy difference (JSON) and the free energy difference curve (CSV). The checker compares the ΔE value to the paper's gold and extracts Tc from the CSV to compare with the gold Tc.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energy_minimum_difference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_E_eV_per_fu"
        ],
        "properties": {
          "delta_E_eV_per_fu": {
            "type": "number",
            "description": "Lattice energy difference per VO2 formula unit (eV)"
          }
        }
      },
      "description": "The lattice energy difference between the R and M1 phases, per formula unit."
    },
    {
      "file": "free_energy_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Delta_F_eV"
        ],
        "row_count": "at least 10"
      },
      "description": "Free energy difference ΔF(T) between the M1 and R phases at several temperatures. The checker interpolates to find the temperature where ΔF ≈ 0 (Tc)."
    }
  ],
  "notes": "The agent must run GULP for phonon calculations and many energy minimisations. All required inputs are public or provided inline. The scored artifacts are the lattice energy difference (JSON) and the free energy difference curve (CSV). The checker compares the ΔE value to the paper's gold and extracts Tc from the CSV to compare with the gold Tc."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier. The verifier reads `lattice_energy_minimum_difference.json`, extracts the reported ΔE, and compares it to a reference value. For `free_energy_difference.csv`, the verifier interpolates the ΔF(T) data, locates the zero‑crossing temperature T_c, and compares that to a reference. Both comparisons use tolerances that accommodate legitimate implementation differences while requiring that you genuinely re‑execute the simulation workflow described in the steps. A naive constant guess will not be within the allowed ranges. The final score is a weighted combination of the two checks; partial credit is possible if one artifact is valid and the other is not.
