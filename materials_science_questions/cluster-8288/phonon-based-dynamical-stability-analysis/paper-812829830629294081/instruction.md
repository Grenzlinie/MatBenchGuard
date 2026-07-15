# First-principles study of trigonally bonded II–IV–N₂ monolayers

## Problem background
Two-dimensional (2D) ternary nitrides with the composition II–IV–N₂, where II represents Zn or Cd and IV represents Si, Ge, or Sn, can form trigonally coordinated planar monolayers with a distorted honeycomb lattice. These materials are of interest because their structural and electronic properties are sensitive to the choice of group‑II and group‑IV elements, offering routes to tunable semiconductors for optoelectronics and photocatalysis. This work uses first-principles density functional theory (DFT) and density functional perturbation theory (DFPT) to compute the equilibrium lattice constants, vibrational stability (phonon spectra), and electronic band gaps of six such monolayers, and to investigate how uniaxial compressive strain along one lattice direction can convert an indirect band gap into a direct one. The results clarify how elemental substitution and strain alter stability and band-edge character in this family of 2D materials.

## Approach
The calculations follow a standard plane‑wave DFT protocol using the generalized gradient approximation (GGA‑PBE) together with optimized norm‑conserving Vanderbilt pseudopotentials. First, an orthorhombic unit cell is chosen to represent each monolayer, with a vacuum layer separating periodic images. Geometry relaxations are performed to obtain the equilibrium in‑plane lattice constants a and b. Dynamical stability is then assessed via DFPT phonon dispersion calculations: a structure with any imaginary (negative‑frequency) phonon mode is considered unstable. Electronic band structures are computed to extract the direct gap at Γ and the indirect gap from the valence band maximum to Γ; these determine whether the gap is direct or indirect. Finally, for ZnSnN₂ a series of uniaxial compressive strains is applied to the b lattice parameter (with internal coordinates relaxed at each strain), and the evolution of the direct and indirect gaps is tracked to locate the strain at which the gap type changes from indirect to direct. All steps use only publicly available tools and pseudopotentials, and no pre‑computed data is required; the agent is expected to install ABINIT and fetch the pseudopotentials at runtime.

## Reproduction target
You must produce the following four scored artifacts, each as a JSON file under /app/outputs:

1. **step_01_lattice_constants.json** – For each of the six II–IV–N₂ monolayers (ZnSiN₂, ZnGeN₂, ZnSnN₂, CdSiN₂, CdGeN₂, CdSnN₂), report the relaxed in‑plane lattice constants a and b (in Å) obtained from GGA‑PBE geometry optimization.
2. **step_02_stability.json** – For each compound, report the minimum phonon frequency (in cm⁻¹) from a DFPT calculation along a representative high‑symmetry path. A negative value indicates imaginary modes and dynamical instability; also provide a boolean stability flag (true if the minimum frequency is non‑negative).
3. **step_03_band_gaps.json** – For each compound, report the direct band gap at Γ (Γ→Γ) and the indirect band gap from the valence‑band maximum to Γ (both in eV), together with a string indicating the gap type: 'direct' if the VBM lies at Γ, otherwise 'indirect'.
4. **step_04_strain_transition.json** – For ZnSnN₂ only, apply uniaxial compressive strain on the b lattice constant in steps from 0 % to −0.5 % (strain as decimal, e.g. −0.001 for −0.1 %). At each strain, report the direct gap at Γ and the indirect gap (X→Γ). The results should reveal the critical strain at which the indirect‑to‑direct gap crossing occurs.

## Assets

- ABINIT DFT package: https://www.abinit.org
- Optimized Norm-Conserving Vanderbilt Pseudopotentials (ONCVPSP) – PBE for Zn, Cd, Si, Ge, Sn, N: http://www.pseudo-dojo.org

## Workflow steps

### Step 1: Geometry relaxation and lattice constants
- Role: scored (load-bearing)
- Action: Perform DFT geometry relaxation for six trigonal II–IV–N₂ monolayers (ZnSiN₂, ZnGeN₂, ZnSnN₂, CdSiN₂, CdGeN₂, CdSnN₂) using GGA-PBE, ONCVPSP pseudopotentials, and appropriate k‑point sampling. Use an orthorhombic unit cell with a vacuum of 10 Å along the c direction. Extract the relaxed lattice constants a and b (in Å).
- Output file: `/app/outputs/step_01_lattice_constants.json`
- Format: json
- Contract: Array of objects; each object has keys: 'compound' (string, e.g. 'ZnSiN2'), 'a' (number, Å), 'b' (number, Å).
- Scoring: scored by hidden verifier

### Step 2: Phonon stability analysis
- Role: scored (load-bearing)
- Action: Using the relaxed structures from step 1, compute phonon dispersions via DFPT (with LO‑TO splitting) along high‑symmetry paths. Determine the minimum phonon frequency (negative values indicate imaginary modes). Record the minimum frequency and a boolean stability flag (true if min ≥ 0, false if min < 0).
- Output file: `/app/outputs/step_02_stability.json`
- Format: json
- Contract: Array of objects; each object has keys: 'compound' (string), 'min_phonon_frequency' (number, cm⁻¹, negative = imaginary), 'stable' (boolean).
- Scoring: scored by hidden verifier

### Step 3: Band gap calculation
- Role: scored
- Action: Compute electronic band structures for all six monolayers using DFT‑GGA‑PBE with appropriate k‑point paths. Extract the direct band gap at Γ and the indirect band gap from the valence band maximum to Γ. Determine the gap type: 'direct' if VBM at Γ, else 'indirect'.
- Output file: `/app/outputs/step_03_band_gaps.json`
- Format: json
- Contract: Array of objects; each object has keys: 'compound' (string), 'direct_gap' (number, eV, Γ→Γ), 'indirect_gap' (number, eV, VBM→Γ), 'gap_type' (string, 'direct' or 'indirect').
- Scoring: scored by hidden verifier

### Step 4: Strain-induced band gap transition for ZnSnN₂
- Role: scored
- Action: Starting from relaxed ZnSnN₂, apply uniaxial compressive strain on lattice constant b (reduce b, relax atomic positions at each strain) and compute the band structure for strains: 0%, −0.05%, −0.1%, −0.15%, −0.2%, −0.25%, −0.3%, −0.35%, −0.4%, −0.45%, −0.5%. For each strain, report the direct gap at Γ and the indirect gap (X→Γ).
- Output file: `/app/outputs/step_04_strain_transition.json`
- Format: json
- Contract: Array of objects; each object has keys: 'strain_b' (number, strain as decimal, e.g. −0.001 for −0.1%), 'direct_gap' (number, eV), 'indirect_gap' (number, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_constants.json`
- `/app/outputs/step_02_stability.json`
- `/app/outputs/step_03_band_gaps.json`
- `/app/outputs/step_04_strain_transition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_constants.json
- path: `/app/outputs/step_01_lattice_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constants a and b for six trigonal II–IV–N₂ monolayers obtained from GGA‑PBE relaxation.
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `compound`: string
    - `a`: number, Å
    - `b`: number, Å
  - `required_columns`:
  - `units`:
    - `a`: Å
    - `b`: Å

### step_02_stability.json
- path: `/app/outputs/step_02_stability.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Minimum phonon frequency and dynamical stability flag for each monolayer; negative frequency indicates imaginary mode (unstable).
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `compound`: string
    - `min_phonon_frequency`: number, cm⁻¹
    - `stable`: boolean
  - `required_columns`:
  - `units`:
    - `min_phonon_frequency`: cm⁻¹

### step_03_band_gaps.json
- path: `/app/outputs/step_03_band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct and indirect band gaps and gap type for the six trigonal monolayers (GGA‑PBE).
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `compound`: string
    - `direct_gap`: number, eV
    - `indirect_gap`: number, eV
    - `gap_type`: string
  - `required_columns`:
  - `units`:
    - `direct_gap`: eV
    - `indirect_gap`: eV

### step_04_strain_transition.json
- path: `/app/outputs/step_04_strain_transition.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct and indirect band gaps of ZnSnN₂ under uniaxial compressive strain on lattice constant b; used to locate the indirect‑to‑direct crossing.
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `strain_b`: number, decimal strain (e.g. −0.001)
    - `direct_gap`: number, eV
    - `indirect_gap`: number, eV
  - `required_columns`:
  - `units`:
    - `strain_b`: dimensionless
    - `direct_gap`: eV
    - `indirect_gap`: eV

Notes: All results are computed with GGA‑PBE and ONCVPSP pseudopotentials. The checker compares the reported values to hidden reference values with appropriate tolerances. Stability is checked by the sign of the minimum phonon frequency. The strain transition is verified by the ordering of direct/indirect gaps at a few key strains.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "compound": "string",
          "a": "number, Å",
          "b": "number, Å"
        },
        "required_columns": [],
        "units": {
          "a": "Å",
          "b": "Å"
        }
      },
      "description": "Equilibrium lattice constants a and b for six trigonal II–IV–N₂ monolayers obtained from GGA‑PBE relaxation."
    },
    {
      "file": "step_02_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "compound": "string",
          "min_phonon_frequency": "number, cm⁻¹",
          "stable": "boolean"
        },
        "required_columns": [],
        "units": {
          "min_phonon_frequency": "cm⁻¹"
        }
      },
      "description": "Minimum phonon frequency and dynamical stability flag for each monolayer; negative frequency indicates imaginary mode (unstable)."
    },
    {
      "file": "step_03_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "compound": "string",
          "direct_gap": "number, eV",
          "indirect_gap": "number, eV",
          "gap_type": "string"
        },
        "required_columns": [],
        "units": {
          "direct_gap": "eV",
          "indirect_gap": "eV"
        }
      },
      "description": "Direct and indirect band gaps and gap type for the six trigonal monolayers (GGA‑PBE)."
    },
    {
      "file": "step_04_strain_transition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "strain_b": "number, decimal strain (e.g. −0.001)",
          "direct_gap": "number, eV",
          "indirect_gap": "number, eV"
        },
        "required_columns": [],
        "units": {
          "strain_b": "dimensionless",
          "direct_gap": "eV",
          "indirect_gap": "eV"
        }
      },
      "description": "Direct and indirect band gaps of ZnSnN₂ under uniaxial compressive strain on lattice constant b; used to locate the indirect‑to‑direct crossing."
    }
  ],
  "notes": "All results are computed with GGA‑PBE and ONCVPSP pseudopotentials. The checker compares the reported values to hidden reference values with appropriate tolerances. Stability is checked by the sign of the minimum phonon frequency. The strain transition is verified by the ordering of direct/indirect gaps at a few key strains."
}
```

## How you are scored
Your submitted artifacts will be evaluated by an automated verifier that compares the values you report against hidden reference data. For each scored step, the verifier applies a directional comparison: for quantities where smaller values are better (e.g., deviation from a reference lattice constant) or larger values indicate correct trends, you receive full credit for matching or surpassing the reference, and the reward decreases smoothly as your result departs from the target range. The verifier does not require your numbers to be exactly identical to any published table; it rewards faithful reproduction of the computational experiment using the prescribed method. The final score is a weighted sum of the four step scores, with the largest weights assigned to the lattice constants and the strain‑transition analysis. Reporting numbers that merely match the paper’s claims without actually performing the calculations will not achieve a high score.
