# DFT-based phase stability analysis of tantalum at high pressure

## Problem background
Tantalum (Ta) is a key pressure standard in diamond-anvil cell (DAC) and shock-wave experiments, but its high-pressure melting curve is disputed, partly due to unknown solid-solid phase transitions. The possibility of a structural transition before melting has been investigated theoretically and experimentally, with the hexagonal ω phase and other structures proposed as candidates. This work evaluates the stability of an orthorhombic Pnma structure (space group 62) of Ta under high pressure, relative to the well-known body-centered cubic (bcc) phase and the previously reported ω phase. By computing structural, vibrational, and mechanical properties from first principles, the task aims to determine whether Pnma-Ta is a viable metastable phase and to compare its sound velocities with experimental shock-wave data.

## Approach
The computational approach uses density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and an ultrasoft pseudopotential for Ta. All calculations are performed with the Quantum ESPRESSO package. The crystal structures of bcc-Ta, Pnma-Ta, and ω-Ta are relaxed at high pressure (100 GPa for bcc and Pnma, and a range of pressures for ω). From the relaxed total energies, the enthalpy difference between Pnma-Ta and bcc-Ta at 100 GPa is computed. The dynamical stability of Pnma-Ta is assessed by computing its phonon dispersion via density functional perturbation theory (DFPT) and verifying the absence of imaginary frequencies. The mechanical stability is evaluated by calculating the full set of orthorhombic elastic constants for Pnma-Ta and the hexagonal elastic constants for ω-Ta, using a stress-strain method. Finally, the shear and bulk sound velocities of Pnma-Ta are derived from the elastic constants and the relaxed density. These results are compared with the known properties of bcc-Ta and with experimental sound velocity data.

## Crystal structures

### bcc‑Ta
Body‑centered cubic, space group Im‑3m (229). One atom at (0, 0, 0). Standard cubic cell; the agent sets the lattice constant and relaxes at target pressure.

### Pnma‑Ta
Orthorhombic, space group Pnma (No. 62). Four atoms in the primitive cell at Wyckoff position 4c with fractional coordinates (0.132, 0.250, 0.366). At ∼100 GPa the lattice constants are approximately a = 4.98 Å, b = 4.30 Å, c = 2.56 Å (the paper’s relaxed structure). Use these as starting lattice parameters and relax atomic positions and cell at 100 GPa.

### ω‑Ta (hexagonal)
Hexagonal, space group P6/mmm (No. 191). Three atoms per unit cell at the ideal ω positions:
- (0, 0, 0)
- (2/3, 1/3, 1/2)
- (1/3, 2/3, 1/2)
Start with approximate lattice parameters a ≈ 3.0 Å, c ≈ 3.0 Å and relax at the required pressures (80, 100, 120 GPa). The relaxed structures are used for subsequent calculations.

## Reproduction target
Your task is to produce the following scored artifacts:

1. The enthalpy difference H(Pnma) − H(bcc) (in eV/atom) at a pressure of 100 GPa, written to `rel_enthalpy.json`.
2. The phonon dispersion of Pnma-Ta at 96–100 GPa: a set of q‑point labels and the corresponding phonon frequencies (in cm⁻¹) along a high-symmetry path in the first Brillouin zone, written to `phonon_dispersion.json`.
3. The nine orthorhombic elastic constants (C11, C22, C33, C44, C55, C66, C12, C13, C23) of Pnma-Ta at 100 GPa, in GPa, written to `pnma_elastic_constants.json`.
4. The shear (C_l) and bulk (C_b) sound velocities of Pnma-Ta at 100 GPa, in km/s, derived from the elastic constants and density, written to `pnma_sound_velocity.json`.
5. The elastic constants of ω-Ta at several pressures (including C44), written as a list of pressure–constant objects to `omega_elastic_constants.json`.

All output files must reside under `/app/outputs`. The calculations should be self-contained: the required structures, pseudopotential, and DFT settings are public, and the workflow steps that follow guide you through the pipeline.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PBE ultrasoft pseudopotential for Ta: https://www.materialscloud.org/discover/sssp
- Python: python

## Workflow steps

### Step 1: DFT structural relaxations
- Role: process
- Action: Using Quantum ESPRESSO pw.x with PBE ultrasoft pseudopotential for Ta, relax the atomic positions of bcc-Ta and Pnma-Ta at a target pressure of 100 GPa, and relax ω-Ta at several pressures (e.g., 80, 100, 120 GPa). Save the optimized coordinates and total energies for each calculation.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Enthalpy difference Pnma vs bcc
- Role: scored (load-bearing)
- Action: From the relaxed total energies of Pnma and bcc at 100 GPa, compute the enthalpy difference H_rel_bcc = H(Pnma) - H(bcc) in eV/atom. Write the result to rel_enthalpy.json.
- Output file: `/app/outputs/rel_enthalpy.json`
- Format: json
- Contract: {"P": 100, "H_rel_bcc": <float> in eV/atom}
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion of Pnma
- Role: scored
- Action: Perform a density functional perturbation theory (DFPT) phonon calculation for Pnma-Ta at 96 GPa (or 100 GPa) using Quantum ESPRESSO ph.x. Compute the phonon frequencies along a high-symmetry q‑path in the first Brillouin zone. Write the q‑point labels and frequencies to phonon_dispersion.json.
- Output file: `/app/outputs/phonon_dispersion.json`
- Format: json
- Contract: {"qpoints": ["<string>", ...], "frequencies": [[<float>, ...], ...], "unit": "cm^{-1}"}
- Scoring: scored by hidden verifier

### Step 4: Elastic constants of Pnma
- Role: scored
- Action: Compute the full set of nine orthorhombic elastic constants Cij for Pnma-Ta at 100 GPa using a stress‑strain method (e.g., extracting from QE calculations). Write the constants to pnma_elastic_constants.json.
- Output file: `/app/outputs/pnma_elastic_constants.json`
- Format: json
- Contract: {"pressure": 100, "C11": <float>, "C22": <float>, "C33": <float>, "C44": <float>, "C55": <float>, "C66": <float>, "C12": <float>, "C13": <float>, "C23": <float>, "unit": "GPa"}
- Scoring: scored by hidden verifier

### Step 5: Sound velocities of Pnma
- Role: scored
- Action: From the Pnma elastic constants and the density (from the relaxed volume), compute the shear sound velocity C_l and bulk sound velocity C_b at 100 GPa. Output the results in pnma_sound_velocity.json.
- Output file: `/app/outputs/pnma_sound_velocity.json`
- Format: json
- Contract: {"pressure": 100, "C_l": <float>, "C_b": <float>, "unit": "km/s"}
- Scoring: scored by hidden verifier

### Step 6: Elastic constants of omega-Ta
- Role: scored
- Action: For each relaxed ω‑Ta structure at the candidate pressures, compute the elastic constants (including C44) using a stress‑strain method. Write the results as a list of pressure–constant pairs to omega_elastic_constants.json. The C44 values must clearly indicate mechanical instability (negative).
- Output file: `/app/outputs/omega_elastic_constants.json`
- Format: json
- Contract: [{"pressure": <float>, "C11": <float>, "C12": <float>, "C13": <float>, "C33": <float>, "C44": <float>, ...}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rel_enthalpy.json`
- `/app/outputs/phonon_dispersion.json`
- `/app/outputs/pnma_elastic_constants.json`
- `/app/outputs/pnma_sound_velocity.json`
- `/app/outputs/omega_elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rel_enthalpy.json
- path: `/app/outputs/rel_enthalpy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: enthalpy difference H(Pnma)-H(bcc) at 100 GPa, compared to paper gold.
- schema:
  - `type`: object
  - `required`:
    - `P`: number
    - `H_rel_bcc`: number (eV/atom)
  - `description`: Enthalpy difference of Pnma relative to bcc at 100 GPa

### phonon_dispersion.json
- path: `/app/outputs/phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Scored artifact: phonon dispersion of Pnma, checked for absence of imaginary frequencies (>−1 cm⁻¹).
- schema:
  - `type`: object
  - `required`:
    - `qpoints`: array of strings
    - `frequencies`: array of arrays of numbers (cm⁻¹)
  - `description`: Phonon dispersion data: q-point labels and frequency branches

### pnma_elastic_constants.json
- path: `/app/outputs/pnma_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: elastic constants of Pnma, compared to paper values (Table I) within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `pressure`: number (GPa)
    - `C11`: number
    - `C22`: number
    - `C33`: number
    - `C44`: number
    - `C55`: number
    - `C66`: number
    - `C12`: number
    - `C13`: number
    - `C23`: number
    - `unit`: string (GPa)
  - `description`: Orthorhombic elastic constants of Pnma-Ta at 100 GPa

### pnma_sound_velocity.json
- path: `/app/outputs/pnma_sound_velocity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: sound velocities derived from elastic constants, compared to paper gold.
- schema:
  - `type`: object
  - `required`:
    - `pressure`: number (GPa)
    - `C_l`: number
    - `C_b`: number
    - `unit`: string (km/s)
  - `description`: Shear (C_l) and bulk (C_b) sound velocities of Pnma at 100 GPa

### omega_elastic_constants.json
- path: `/app/outputs/omega_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: elastic constants of ω-Ta at several pressures; C44 must be negative to confirm instability.
- schema:
  - `type`: array
  - `items`:
    - `pressure`: number (GPa)
    - `C11`: number
    - `C12`: number
    - `C13`: number
    - `C33`: number
    - `C44`: number
  - `description`: List of elastic constant objects at multiple pressures

Notes: All scored outputs are read by the hidden checker and compared to paper-reported gold values with appropriate tolerances. Process step evidence (relaxation.log) is not scored but required for pipeline integrity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rel_enthalpy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "P": "number",
          "H_rel_bcc": "number (eV/atom)"
        },
        "description": "Enthalpy difference of Pnma relative to bcc at 100 GPa"
      },
      "description": "Scored artifact: enthalpy difference H(Pnma)-H(bcc) at 100 GPa, compared to paper gold."
    },
    {
      "file": "phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "qpoints": "array of strings",
          "frequencies": "array of arrays of numbers (cm⁻¹)"
        },
        "description": "Phonon dispersion data: q-point labels and frequency branches"
      },
      "description": "Scored artifact: phonon dispersion of Pnma, checked for absence of imaginary frequencies (>−1 cm⁻¹)."
    },
    {
      "file": "pnma_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pressure": "number (GPa)",
          "C11": "number",
          "C22": "number",
          "C33": "number",
          "C44": "number",
          "C55": "number",
          "C66": "number",
          "C12": "number",
          "C13": "number",
          "C23": "number",
          "unit": "string (GPa)"
        },
        "description": "Orthorhombic elastic constants of Pnma-Ta at 100 GPa"
      },
      "description": "Scored artifact: elastic constants of Pnma, compared to paper values (Table I) within tolerance."
    },
    {
      "file": "pnma_sound_velocity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pressure": "number (GPa)",
          "C_l": "number",
          "C_b": "number",
          "unit": "string (km/s)"
        },
        "description": "Shear (C_l) and bulk (C_b) sound velocities of Pnma at 100 GPa"
      },
      "description": "Scored artifact: sound velocities derived from elastic constants, compared to paper gold."
    },
    {
      "file": "omega_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "pressure": "number (GPa)",
          "C11": "number",
          "C12": "number",
          "C13": "number",
          "C33": "number",
          "C44": "number"
        },
        "description": "List of elastic constant objects at multiple pressures"
      },
      "description": "Scored artifact: elastic constants of ω-Ta at several pressures; C44 must be negative to confirm instability."
    }
  ],
  "notes": "All scored outputs are read by the hidden checker and compared to paper-reported gold values with appropriate tolerances. Process step evidence (relaxation.log) is not scored but required for pipeline integrity."
}
```

## How you are scored
A hidden verifier scores each scored artifact independently and combines the results into a final reward between 0 and 1. The verifier reads the JSON files you produce and compares the reported numerical values to reference values that fulfill the physical requirements of the problem:

- **Enthalpy difference**: compared to a reference value with an appropriate tolerance.
- **Phonon dispersion**: the verifier checks that all reported frequencies are greater than −1 cm⁻¹ (i.e., no imaginary phonon modes that would indicate dynamical instability).
- **Elastic constants of Pnma**: each constant is compared to a reference set within a tolerance, and the verifier may additionally check that the constants satisfy the orthorhombic mechanical stability criteria.
- **Sound velocities of Pnma**: compared to reference values, again within a tolerance.
- **Elastic constants of ω-Ta**: the verifier verifies that the reported C44 values are negative at all pressures, demonstrating mechanical instability; other constants may also be compared to reference ranges.

Reporting the paper's numbers is not sufficient; your workflow must genuinely execute the DFT calculations to produce the artifacts. The verifier operates on the self-reported values, trusting that they originate from a correct computational pipeline. Artifacts that pass the checks contribute their weight toward the total reward; missing or incorrect outputs reduce the score.
