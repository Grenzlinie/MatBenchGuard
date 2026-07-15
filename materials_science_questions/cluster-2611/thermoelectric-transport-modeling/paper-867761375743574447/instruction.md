# Triboelectric Series Quantification from First-Principles Thermoelectric Modeling

## Problem background
Triboelectric charging — the static electrification produced by rubbing two materials together — has been observed for centuries, yet a rigorous quantitative model that predicts the resulting charge polarity and the triboelectric series has remained elusive. A recent theoretical proposal suggests that friction-induced heat at the interface generates a temperature gradient, which in turn induces a thermoelectric voltage. According to this model, the triboelectric behaviour of a material is governed by a single triboelectric factor ξ = S / √(ρ c k), where S is the material's Seebeck coefficient and ρ, c, k are its density, specific heat, and thermal conductivity. The central open question is whether this ξ, computed from first-principles Seebeck coefficients and experimentally measured thermal properties, can reproduce the experimentally observed triboelectric series.

**Your objective** is to compute the Seebeck coefficients S for the 14 triboelectric materials listed below, derive the triboelectric factor ξ for each, and then determine how well the resulting ξ ordering matches established experimental triboelectric series. Additionally, you will validate the computed Seebeck coefficients for two well-characterised reference materials, Al and Si, against their known experimental values.

## Approach
The core idea is that a material with a higher positive ξ will tend to charge positively when rubbed against a material with a lower (or more negative) ξ. The quantity ξ depends on the Seebeck coefficient S, which is computed from the electronic density of states (DOS) using density-functional theory (DFT), and on the bulk thermophysical properties ρ, c, k that must be obtained from experimental references.

**1. Compute the Seebeck coefficient S for 14 materials**

You are given the following list of 14 triboelectric materials:
- wool (α-keratin)
- polypropylene (PP)
- silk (fibroin)
- nylon (nylon66)
- NR (polyisoprene, natural rubber)
- cellulose (Iβ-cellulose)
- Al (aluminium metal)
- Si (silicon)
- quartz (trigonal SiO₂)
- sulfur (orthorhombic α-sulfur)
- PE (polyethylene)
- PTFE (polytetrafluoroethylene)
- PDMS (polydimethylsiloxane)
- PVC (polyvinyl chloride)

For each material, perform a DFT calculation to obtain the electronic density of states N(E). The calculation should use the PBE exchange-correlation functional, with HSE06 hybrid corrections applied via a screened exchange term. The mixing parameter for the hybrid functional is obtained from the reciprocal of the macroscopic dielectric constant computed at the PBE level. The slab vacuum alignment method is used to set the absolute energy scale. The Fermi energy EF is set universally to -4.44 eV relative to the vacuum level, which corresponds to the redox potential of the H₂/H⁺ couple and approximates the effect of ambient moisture.

From N(E) compute the Seebeck coefficient at 300 K using the Mott formula:

S = -(1 / (e T)) * ∫ (E - EF) N(E) (-df/dE) dE  /  ∫ N(E) (-df/dE) dE

where e is the elementary charge and f(E) is the Fermi-Dirac distribution at temperature T = 300 K.

You may use an open-source plane-wave DFT code such as Quantum ESPRESSO for all calculations.

**2. Compute the triboelectric factor ξ**

For each material, combine the computed S with the experimental values of density ρ (in g/cm³), specific heat c (in J/g·K), and thermal conductivity k (in W/m·K) listed below. These values are taken from published measurements and should be used directly:

| Material   | ρ (g/cm³) | c (J/g·K) | k (W/m·K) |
|------------|-----------|-----------|-----------|
| wool       | 0.026     | 1.37      | 0.034     |
| PP         | 0.9       | 1.68      | 0.22      |
| silk       | 1.4       | 1.24      | 0.256     |
| nylon      | 1.24      | 1.50      | 0.27      |
| NR         | 0.96      | 1.89      | 0.35      |
| cellulose  | 1.6       | 1.40      | 5.7       |
| Al         | 2.70      | 0.95      | 238       |
| Si         | 2.33      | 0.70      | 130       |
| quartz     | 2.5       | 0.78      | 1.4       |
| sulfur     | 2.07      | 0.72      | 0.27      |
| PE         | 0.93      | 1.83      | 0.46      |
| PTFE       | 2.20      | 1.05      | 0.26      |
| PDMS       | 0.97      | 1.6       | 0.2       |
| PVC        | 1.38      | 0.96      | 0.15      |

Compute ξ = S / √(ρ c k) for each material, with ξ expressed in units of V·s^(1/2)/(J·cm⁻²).

**3. Compare the ξ ordering with experimental triboelectric series**

Sort the materials in descending order of ξ to obtain your computed triboelectric series.

You will compare this ordering against the following five experimental triboelectric series reported in the literature. In these lists, materials appear from most positive (left) to most negative (right). The original material names have been mapped to the standard names used in this task as follows:

Series A (mapped from 1955):
wool → nylon → cellulose → silk → PVC → PE → PTFE

Series B (mapped from 1962):
nylon → wool → silk → cellulose → NR → sulfur → PE → PVC → PTFE

Series C (mapped from 1987):
nylon → wool → silk → cellulose → PE → PP → PVC → Si → PTFE

Series D (mapped from 1998):
quartz → nylon → wool → silk → cellulose → Al → PDMS → PTFE → PVC

Series E (mapped from 2019):
cellulose → nylon → PP → quartz → PE → PDMS → PTFE → PVC

For each experimental series, compute the average pairwise order similarity with your computed ξ ordering using the following similarity function:

- For every unordered pair of materials that appear in both the computed ξ ordering and the experimental series, define the similarity s = 1 if the order of the two materials is the same in both lists (i.e., the material with higher ξ appears before the other in the experimental series), and s = 0 if the order differs.
- The average similarity for a given experimental series is the mean of s over all such common material pairs.

Compute the overall average similarity by taking the mean of the per-series similarities.

**4. Validate the Seebeck coefficients for Al and Si**

Compute the relative error of your DFT-calculated Seebeck coefficients against the experimental references:
- Al experimental S: -1.8 μV/K
- Si experimental S: -673 μV/K (n-type Si at 2e18 cm⁻³ and 325 K)

Relative error = 100% × (S_computed - S_experimental) / |S_experimental|. Report these as Al_rel_error and Si_rel_error.

## Reproduction target
Produce a fully self-contained computational workflow that:

1. Obtains crystal structures for the 14 materials from public databases (e.g., Crystallography Open Database or Materials Project) and runs DFT calculations to compute the Seebeck coefficients S at 300 K.
2. Computes the triboelectric factor ξ for each material from S and the provided experimental ρ, c, k values.
3. Determines the ξ ordering and computes the average pairwise similarity against the five experimental series listed under Approach.
4. Calculates the relative errors of the computed S for Al and Si with respect to the reference experimental values.

All computations must be performed by the solver; the deliverables are the following three files written to `/app/outputs`:
- `seebeck_coefficients.csv` – a CSV with columns: material, S_muV_per_K, xi_V_s0p5_per_J_cm2. One row per material, 14 rows.
- `similarity_score.txt` – a single line containing the overall average similarity score (a float between 0 and 1).
- `validation_Al_Si.txt` – a text file with two lines:
  Al_rel_error: <value>%
  Si_rel_error: <value>%

The primary objective is to demonstrate that the ξ ordering yields a non-trivial agreement with experimental series as measured by the similarity score.

## Assets

- Crystal structures for 14 triboelectric materials
- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency library): https://www.materialscloud.org/discover/sssp/
- Python packages (numpy, scipy, pymatgen, ase, matplotlib): pip

## Workflow steps

### Step 1: DFT calculation of electronic structure and Seebeck coefficients
- Role: process
- Action: For each of the 14 triboelectric materials (wool, PP, silk, nylon, NR, cellulose, Al, Si, quartz, sulfur, PE, PTFE, PDMS, PVC), perform density-functional theory (DFT) calculations using an open-source plane-wave code (e.g., Quantum ESPRESSO). Use PBE functional with HSE06 hybrid corrections based on the macroscopic dielectric constant, slab vacuum alignment, and a universal Fermi energy alignment. Compute the electronic density of states N(E) and evaluate the Seebeck coefficient S at 300 K via the standard Mott formula. Collect all S values.
- Evidence: `/app/outputs/dft_summary.json`

### Step 2: Compute triboelectric factor ξ
- Role: scored (load-bearing)
- Action: Using the Seebeck coefficients from step 1 and the experimental density ρ, specific heat c, and thermal conductivity k values (as listed in the paper's Table II) for each material, compute the triboelectric factor ξ = S/√(ρ c k). Output a CSV with material name, S (μV/K), and ξ (V·s^(1/2)/(J·cm^-2)).
- Output file: `/app/outputs/seebeck_coefficients.csv`
- Format: csv
- Contract: Columns: material (string), S_muV_per_K (float, μV/K), xi_V_s0p5_per_J_cm2 (float, V·s^(1/2)/(J·cm^-2)). One row per material, 14 rows total.
- Scoring: scored by hidden verifier

### Step 3: Compute similarity with experimental triboelectric series
- Role: scored
- Action: From the ξ values determine the triboelectric series ordering (descending ξ). For each of the five experimental triboelectric series described in the Approach section, compute the average pairwise order similarity: for every unordered pair of materials that appear in both lists, s = 1 if the relative order is the same in both, else s = 0. Compute the overall average similarity by taking the mean of the per‑series similarities. Output this overall average similarity as a single float.
- Output file: `/app/outputs/similarity_score.txt`
- Format: txt
- Contract: A single floating-point number between 0 and 1 (e.g., 0.83).
- Scoring: scored by hidden verifier

### Step 4: Validate Seebeck coefficients for Al and Si
- Role: scored
- Action: For aluminum and silicon, compute the relative error (in %) between the DFT-calculated Seebeck coefficient and the experimental reference values (-1.8 μV/K for Al, -673 μV/K for n-type Si at 2e18 cm^-3 and 325 K). Output the two relative errors.
- Output file: `/app/outputs/validation_Al_Si.txt`
- Format: txt
- Contract: Two lines in format: Al_rel_error: <float>%; Si_rel_error: <float>%.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/seebeck_coefficients.csv`
- `/app/outputs/similarity_score.txt`
- `/app/outputs/validation_Al_Si.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### seebeck_coefficients.csv
- path: `/app/outputs/seebeck_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of computed Seebeck coefficients and triboelectric factors for the 14 triboelectric materials.
- schema:
  - `type`: table
  - `required_columns`: `material`, `S_muV_per_K`, `xi_V_s0p5_per_J_cm2`
  - `units`:
    - `S_muV_per_K`: μV/K
    - `xi_V_s0p5_per_J_cm2`: V·s^(1/2)/(J·cm⁻²)
  - `description`: material: string, S_muV_per_K: float, xi_V_s0p5_per_J_cm2: float

### similarity_score.txt
- path: `/app/outputs/similarity_score.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Overall average pairwise order similarity between the computed ξ series and the experimental series.
- schema:
  - `type`: text
  - `description`: A single floating-point number between 0 and 1.

### validation_Al_Si.txt
- path: `/app/outputs/validation_Al_Si.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Validation relative errors for Al and Si Seebeck coefficients against known experimental values.
- schema:
  - `type`: text
  - `description`: Two lines: Al_rel_error: <float>%; Si_rel_error: <float>%.

Notes: The similarity score is scored against a hidden threshold; the Seebeck coefficients are compared against reference values with generous tolerances. The verification ensures that the computed numbers are derived from the specified DFT calculations and are self-consistent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "seebeck_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "S_muV_per_K",
          "xi_V_s0p5_per_J_cm2"
        ],
        "units": {
          "S_muV_per_K": "μV/K",
          "xi_V_s0p5_per_J_cm2": "V·s^(1/2)/(J·cm⁻²)"
        },
        "description": "material: string, S_muV_per_K: float, xi_V_s0p5_per_J_cm2: float"
      },
      "description": "CSV table of computed Seebeck coefficients and triboelectric factors for the 14 triboelectric materials."
    },
    {
      "file": "similarity_score.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number between 0 and 1."
      },
      "description": "Overall average pairwise order similarity between the computed ξ series and the experimental series."
    },
    {
      "file": "validation_Al_Si.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "Two lines: Al_rel_error: <float>%; Si_rel_error: <float>%."
      },
      "description": "Validation relative errors for Al and Si Seebeck coefficients against known experimental values."
    }
  ],
  "notes": "The similarity score is scored against a hidden threshold; the Seebeck coefficients are compared against reference values with generous tolerances. The verification ensures that the computed numbers are derived from the specified DFT calculations and are self-consistent."
}
```

## How you are scored
A hidden verifier will independently score each of the above output files.

- **seebeck_coefficients.csv**: The verifier checks that the signs of the Seebeck coefficients match those expected from the theory and that the absolute values of S and ξ are within generous tolerances that account for legitimate DFT toolchain variations.
- **similarity_score.txt**: The verifier recomputes the average similarity using the same five experimental series (hidden) and compares the result against a pre-defined threshold. Meeting or exceeding the threshold earns full credit for this stage.
- **validation_Al_Si.txt**: The verifier checks that the relative errors for Al and Si do not exceed a reasonable tolerance.

Each artifact carries a weight, and the final reward is the weighted sum of the individual scores. Reporting a number that happens to be close to a hidden reference without the underlying computation is not sufficient; the submitted numbers must be derived from the computational steps described above and must be self-consistent.
