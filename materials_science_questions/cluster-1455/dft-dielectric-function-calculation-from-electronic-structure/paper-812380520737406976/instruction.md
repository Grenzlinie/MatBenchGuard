# IR-active TO/LO phonon frequencies and bulk modulus of Dy3Al5O12 using rigid ion model

## Problem background
Rare earth aluminum garnets (RE3Al5O12) are widely used as host crystals for solid-state lasers. Understanding their vibrational properties through infrared (IR) spectroscopy and lattice dynamics calculations is crucial for designing optical materials. This work combines experimental IR reflectance with rigid-ion model (RIM) computations to assign IR-active phonon modes, determine partial phonon density of states, and estimate elastic properties. The core computational challenge is to compute the IR-active transverse-optical (TO) and longitudinal-optical (LO) phonon frequencies from the RIM and derive the bulk modulus via a semiempirical relation based on zone-centre phonon frequencies, enabling comparison with experiment and assessment of the model’s accuracy.

## Approach
The rigid-ion model treats the crystal as an array of point ions with long-range Coulomb interactions and short-range repulsive Born–Mayer-type pair potentials. For Dy3Al5O12, the short-range interactions are parametrized by bond-stretching and bond-bending force constants for Al–O (tetrahedral and octahedral) and Dy–O bonds, along with effective ionic charges. The workflow builds the dynamical matrix at the Brillouin zone centre (Γ point) by summing short-range contributions derived from the force constants and the long-range Coulomb contribution computed via Ewald summation. Diagonalizing this matrix yields all zone-centre phonon eigenfrequencies and eigenvectors. The 17 IR-active modes (triply degenerate T1u symmetry) are identified, and their TO frequencies taken directly; LO frequencies are obtained by applying a macroscopic electric field along the ⟨100⟩ direction, which lifts the degeneracy. Finally, the bulk modulus is evaluated from all zone-centre frequencies and the structural bond lengths using a formula that extends Brout's relation to multi-atom cubic crystals.

## Reproduction target
Implement the rigid-ion model using the provided force constants and effective charges for Dy3Al5O12 and the crystal structure from Euler & Bruce (1965). Compute all zone-centre phonon frequencies, then extract the 17 TO and 17 LO infrared-active mode frequencies (34 values total). Save these as a JSON array where each entry contains a mode index (1–17), a frequency_type ("TO" or "LO"), and the frequency in cm⁻¹. Using the full set of zone-centre frequencies together with the structural parameters (bond lengths r_tetr-O, r_oct-O, r_dod-O, unit-cell volume, atomic masses), evaluate the bulk modulus KT and write the result as a single floating-point number in GPa. All artifacts must be placed under /app/outputs.

## Assets

- Crystal structure of Dy3Al5O12 from Euler & Bruce (1965): 10.1107/S0365110X65003758

## Workflow steps

### Step 1: Prepare Dy3Al5O12 crystal structure
- Role: process
- Action: Obtain the crystal structure of Dy3Al5O12 from Euler and Bruce (1965). Build the lattice vectors and atomic fractional coordinates for the primitive cell (80 atoms) and save the structure in a file (structure.cif or equivalent).
- Evidence: `/app/outputs/structure.cif`

### Step 2: Run RIM zone-center phonon calculation
- Role: process
- Action: Implement the rigid ion model (RIM) using Born–Mayer-type pair potentials with the force constants and effective charges specified for Dy3Al5O12. Build the short-range force-constant matrix from bond-stretching and bond-bending contributions, compute the long-range Coulomb contribution via Ewald summation, construct the full dynamical matrix at the Γ point, diagonalize to obtain all phonon eigenfrequencies, and save the complete list of zone‑centre mode frequencies.
- Evidence: `/app/outputs/all_frequencies.json`

### Step 3: Extract IR TO/LO frequencies
- Role: scored
- Action: From the zone‑centre phonon frequencies and eigenvectors, select the 17 IR‑active modes (T1u symmetry). Obtain TO frequencies directly from the eigenvalues. Compute LO frequencies by applying the macroscopic electric field along ⟨100⟩ (or through Born effective charges). Save the results as an array of 34 objects, each with mode_index (integer, 1–17), frequency_type (string, 'TO' or 'LO'), and frequency (float, cm⁻¹).
- Output file: `/app/outputs/dy_ir_frequencies.json`
- Format: json
- Contract: Array of 34 objects, each with keys: mode_index (int), frequency_type (string 'TO' or 'LO'), frequency (float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 4: Compute bulk modulus using Brout formula
- Role: scored (load-bearing)
- Action: Using all zone‑centre phonon frequencies from all_frequencies.json and structural parameters (bond lengths r_tetr-O, r_oct-O, r_dod-O, unit‑cell volume Vc, atomic masses m_tetr, m_oct, m_dod, m_o), evaluate the bulk modulus KT using the formula:

KT = (8 π^2 r_tetr-O^2 / (9 Vc)) * (Σ_i ν_i^2) * (1 + 0.89 r_oct-O/r_tetr-O + 1.30 r_dod-O/r_tetr-O) / ( (1/m_tetr + 1/m_o) + 0.89 r_tetr-O/r_oct-O (1/m_oct + 1/m_o) + 1.30 r_tetr-O/r_dod-O (1/m_dod + 1/m_dod) )

where ν_i are all zone‑centre phonon frequencies. Write the result as a single floating-point number (unit GPa).
- Output file: `/app/outputs/dy_bulk_modulus.txt`
- Format: txt
- Contract: A single float (GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dy_ir_frequencies.json`
- `/app/outputs/dy_bulk_modulus.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dy_ir_frequencies.json
- path: `/app/outputs/dy_ir_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Array of IR-active TO and LO phonon frequencies for Dy3Al5O12. Each entry has mode_index, frequency_type, and frequency.
- schema:
  - `type`: array
  - `minItems`: 34
  - `maxItems`: 34
  - `items`:
    - `type`: object
    - `required`: `mode_index`, `frequency_type`, `frequency`
    - `properties`:
      - `mode_index`:
        - `type`: integer
        - `minimum`: 1
        - `maximum`: 17
      - `frequency_type`:
        - `type`: string
        - `enum`: `TO`, `LO`
      - `frequency`:
        - `type`: number
        - `unit`: cm-1

### dy_bulk_modulus.txt
- path: `/app/outputs/dy_bulk_modulus.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Bulk modulus of Dy3Al5O12 computed with the modified Brout formula.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the bulk modulus of Dy3Al5O12 in GPa.

Notes: The scored artifacts are the computed IR frequencies and the bulk modulus. The checker will compare each TO/LO frequency to reference values and the bulk modulus to the paper-reported number, with appropriate hidden tolerances. No experimental IR spectra or PDOS are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dy_ir_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "minItems": 34,
        "maxItems": 34,
        "items": {
          "type": "object",
          "required": [
            "mode_index",
            "frequency_type",
            "frequency"
          ],
          "properties": {
            "mode_index": {
              "type": "integer",
              "minimum": 1,
              "maximum": 17
            },
            "frequency_type": {
              "type": "string",
              "enum": [
                "TO",
                "LO"
              ]
            },
            "frequency": {
              "type": "number",
              "unit": "cm-1"
            }
          }
        }
      },
      "description": "Array of IR-active TO and LO phonon frequencies for Dy3Al5O12. Each entry has mode_index, frequency_type, and frequency."
    },
    {
      "file": "dy_bulk_modulus.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the bulk modulus of Dy3Al5O12 in GPa."
      },
      "description": "Bulk modulus of Dy3Al5O12 computed with the modified Brout formula."
    }
  ],
  "notes": "The scored artifacts are the computed IR frequencies and the bulk modulus. The checker will compare each TO/LO frequency to reference values and the bulk modulus to the paper-reported number, with appropriate hidden tolerances. No experimental IR spectra or PDOS are required."
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact. The array of IR frequencies is compared to reference values with appropriate tolerances to assess correctness; the bulk modulus is checked similarly against an expected value. The final reward is a weighted combination of both checks, with higher weight on the frequency reproduction. Reporting a claimed number without executing the computation is not sufficient—the verifier evaluates the actual submitted results against its hidden reference. The exact tolerances and reference values are not disclosed, so you must faithfully implement the model and derive the quantities.
