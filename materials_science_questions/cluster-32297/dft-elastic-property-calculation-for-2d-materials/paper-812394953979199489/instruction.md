# First-principles reproduction of electronic and piezoelectric properties of monolayer and few-layer GaInS3

## Problem background
Two-dimensional (2D) GaInS3 nanosheets are a candidate wide-bandgap semiconductor with highly tunable electronic structure and in-plane piezoelectricity. First-principles calculations suggest that these nanosheets retain a stable non-centrosymmetric structure, leading to electronic and piezoelectric properties that may differ substantially from other layered materials. Understanding how the electronic bandgap, band-edge locations, and piezoelectric stress coefficients vary with the number of atomic layers and with in-plane strain is critical for evaluating the material's potential in nanoelectronic and nanomechanical devices. The task asks you to compute these quantities using density functional theory and to report results that can be compared against independently determined reference values.

## Approach
The problem is approached with first-principles density functional theory (DFT) calculations using an open-source plane-wave code (Quantum ESPRESSO). The workflow proceeds in several stages:
- Construct the monolayer unit cell of GaInS3 in the orthorhombic space group Pmn21 with given lattice constants, and relax the atomic positions and cell parameters.
- Compute the electronic band structure along the high-symmetry path Γ–X–S–Y–Γ using both the PBE and the HSE hybrid functionals. From these calculations extract the bandgap, the type of gap (direct vs. indirect), the valence- and conduction-band extremum locations, and the quasi-direct gap at the Γ point.
- Apply uniaxial tensile and compressive strains to the monolayer and recomputed the HSE bandgap to quantify the strain sensitivity.
- Build bilayer and trilayer models by stacking the relaxed monolayer with a fixed interlayer distance, relax them, and compute their HSE bandgaps to examine layer-dependent electronic structure.
- For each thickness (1, 2, and 3 layers) compute the polarization as a function of small uniaxial strains using the Berry-phase formalism. From the linear slope obtain the two-dimensional piezoelectric stress coefficients e11^2D and e12^2D, then renormalize by the effective layer thickness to obtain the equivalent three-dimensional coefficients e11^3D and e12^3D.
All structures and calculations are built from publicly available specifications and open-source pseudopotentials; no precomputed data is required beyond what is described in the steps below.

## Reproduction target
You are to produce four scored artifacts that capture the key electronic and piezoelectric properties of monolayer and few-layer GaInS3:
- `bandstructure_results.json`: the PBE and HSE bandgaps of the relaxed monolayer, whether the bandgap is indirect, the HSE quasi-direct gap at Γ, and the k-point labels of the CBM and VBM.
- `strain_bandgap.csv`: the HSE bandgap of the monolayer under three in-plane uniaxial strains (ε_xx = -0.04, 0.00, +0.04).
- `layer_bandgap.csv`: the HSE bandgap of the relaxed monolayer, bilayer, and trilayer structures.
- `piezoelectric_coefficients.csv`: the 2D and 3D piezoelectric stress coefficients e11 and e12 for 1, 2, and 3 layers, obtained from Berry-phase polarization calculations under small uniaxial strains.
Each artifact must conform exactly to the output schema described in the corresponding workflow step and must be written to the specified path under `/app/outputs`.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/download
- SSSP pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- GaInS3 monolayer structure specification

## Workflow steps

### Step 1: Build and relax monolayer, bilayer, and trilayer structures
- Role: process
- Action: Construct the monolayer GaInS3 unit cell using the given space group Pmn21 and lattice constants a=6.21 Å, b=3.78 Å, then relax atomic positions and cell parameters using PBE functional. Generate the bilayer and trilayer structures by stacking the relaxed monolayer with the experimentally known interlayer distance, then relax the atomic positions for each stacking.
- Evidence: `/app/outputs/relaxed_structures.tar.gz`

### Step 2: Electronic band structure of monolayer GaInS3
- Role: scored
- Action: Using the relaxed monolayer structure, compute the electronic band structure along Γ–X–S–Y–Γ with both PBE and HSE functionals. Determine the PBE and HSE bandgap, identify the conduction band minimum (CBM) and valence band maximum (VBM) k-point labels, decide whether the gap is indirect, and report the Γ-point HSE gap. Write the results as a JSON file.
- Output file: `/app/outputs/bandstructure_results.json`
- Format: json
- Contract: JSON object with keys: pbe_bandgap (eV, float), hse_bandgap (eV, float), bandgap_type (string, 'indirect' or 'direct'), quasi_direct_gap (eV, HSE gap at Γ), cbm_location (string, k-point label), vbm_location (string, k-point label)
- Scoring: scored by hidden verifier

### Step 3: Strain-dependent HSE bandgap of monolayer
- Role: scored
- Action: Apply uniaxial in-plane strain ε_xx = -0.04, 0.00, +0.04 to the relaxed monolayer (scale the a lattice parameter while allowing b and atomic positions to relax). For each strain, compute the HSE bandgap. Output a CSV file with the strain and bandgap.
- Output file: `/app/outputs/strain_bandgap.csv`
- Format: csv
- Contract: CSV with columns: strain_x (fraction, e.g., -0.04, 0.0, 0.04), hse_bandgap (eV)
- Scoring: scored by hidden verifier

### Step 4: Layer-dependent HSE bandgap
- Role: scored
- Action: Using the relaxed monolayer, bilayer, and trilayer structures, compute the HSE bandgap for each. Output a CSV file with number of layers and corresponding gap.
- Output file: `/app/outputs/layer_bandgap.csv`
- Format: csv
- Contract: CSV with columns: n_layers (int), hse_bandgap (eV)
- Scoring: scored by hidden verifier

### Step 5: Piezoelectric coefficients for monolayer and few-layer
- Role: scored (load-bearing)
- Action: For each of the relaxed monolayer, bilayer, and trilayer structures, calculate the polarization along the x-direction as a function of uniaxial strain (ε_xx from -0.01 to 0.01, step 0.005) and along the y-direction (ε_yy similarly). Fit linear slopes to obtain e11^2D and e12^2D (C/m). Renormalize by the effective thickness to obtain 3D coefficients e11^3D and e12^3D (C/m²). Report all values in a CSV.
- Output file: `/app/outputs/piezoelectric_coefficients.csv`
- Format: csv
- Contract: CSV with columns: n_layers (int), e11_2D (C/m), e12_2D (C/m), e11_3D (C/m²), e12_3D (C/m²)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandstructure_results.json`
- `/app/outputs/strain_bandgap.csv`
- `/app/outputs/layer_bandgap.csv`
- `/app/outputs/piezoelectric_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandstructure_results.json
- path: `/app/outputs/bandstructure_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Monolayer GaInS3 bandgap values, gap type, and band-edge locations computed with PBE and HSE functionals.
- schema:
  - `type`: object
  - `required`:
    - `pbe_bandgap`: float (eV)
    - `hse_bandgap`: float (eV)
    - `bandgap_type`: string
    - `quasi_direct_gap`: float (eV)
    - `cbm_location`: string (k-point label)
    - `vbm_location`: string (k-point label)

### strain_bandgap.csv
- path: `/app/outputs/strain_bandgap.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: HSE bandgap at three uniaxial strains (-4%, 0%, +4%); checks that bandgap decreases under compressive and increases under tensile strain.
- schema:
  - `type`: table
  - `required_columns`: `strain_x`, `hse_bandgap`
  - `units`:
    - `strain_x`: fraction
    - `hse_bandgap`: eV

### layer_bandgap.csv
- path: `/app/outputs/layer_bandgap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: HSE bandgaps for monolayer (1), bilayer (2), and trilayer (3) GaInS3.
- schema:
  - `type`: table
  - `required_columns`: `n_layers`, `hse_bandgap`
  - `units`:
    - `n_layers`: integer
    - `hse_bandgap`: eV

### piezoelectric_coefficients.csv
- path: `/app/outputs/piezoelectric_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 2D and 3D piezoelectric stress coefficients for 1, 2, and 3 layers; verifies the absence of an odd-even effect and layer-independent e11^3D.
- schema:
  - `type`: table
  - `required_columns`: `n_layers`, `e11_2D`, `e12_2D`, `e11_3D`, `e12_3D`
  - `units`:
    - `n_layers`: integer
    - `e11_2D`: C/m
    - `e12_2D`: C/m
    - `e11_3D`: C/m²
    - `e12_3D`: C/m²

Notes: The checker will compare each artifact against the reference values reported in the paper, using appropriate tolerances for DFT re-runs. For strain_bandgap.csv the trend (gap reduction under compression, increase under tension) is evaluated by threshold_or_better logic.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandstructure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pbe_bandgap": "float (eV)",
          "hse_bandgap": "float (eV)",
          "bandgap_type": "string",
          "quasi_direct_gap": "float (eV)",
          "cbm_location": "string (k-point label)",
          "vbm_location": "string (k-point label)"
        }
      },
      "description": "Monolayer GaInS3 bandgap values, gap type, and band-edge locations computed with PBE and HSE functionals."
    },
    {
      "file": "strain_bandgap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_x",
          "hse_bandgap"
        ],
        "units": {
          "strain_x": "fraction",
          "hse_bandgap": "eV"
        }
      },
      "description": "HSE bandgap at three uniaxial strains (-4%, 0%, +4%); checks that bandgap decreases under compressive and increases under tensile strain."
    },
    {
      "file": "layer_bandgap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_layers",
          "hse_bandgap"
        ],
        "units": {
          "n_layers": "integer",
          "hse_bandgap": "eV"
        }
      },
      "description": "HSE bandgaps for monolayer (1), bilayer (2), and trilayer (3) GaInS3."
    },
    {
      "file": "piezoelectric_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_layers",
          "e11_2D",
          "e12_2D",
          "e11_3D",
          "e12_3D"
        ],
        "units": {
          "n_layers": "integer",
          "e11_2D": "C/m",
          "e12_2D": "C/m",
          "e11_3D": "C/m²",
          "e12_3D": "C/m²"
        }
      },
      "description": "2D and 3D piezoelectric stress coefficients for 1, 2, and 3 layers; verifies the absence of an odd-even effect and layer-independent e11^3D."
    }
  ],
  "notes": "The checker will compare each artifact against the reference values reported in the paper, using appropriate tolerances for DFT re-runs. For strain_bandgap.csv the trend (gap reduction under compression, increase under tension) is evaluated by threshold_or_better logic."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines each of the four scored artifact files. For absolute quantities (e.g., bandgaps, piezoelectric coefficients) the verifier compares your computed value against a hidden reference within an appropriate tolerance. For strain-dependent behavior, the verifier checks the expected trend (e.g., whether the bandgap decreases under compressive strain and increases under tensile strain). For layer-dependent piezoelectric coefficients, the verifier audits the structural constancy of the 3D coefficients across different layer numbers. The scores from the individual artifacts are combined according to predetermined weights to produce a final reward between 0.0 and 1.0. Simply reporting a numeric result that matches the reference without performing the DFT workflow is not sufficient: the verifier may also check for the presence of intermediate evidence (e.g., relaxed structure files) to confirm that the computational steps were genuinely executed.
