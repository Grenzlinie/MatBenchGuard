# DFT computation of structural, electronic, dielectric, phononic, and elastic properties of MgNB₉

## Problem background
Magnesium nitridoboride (MgNB₉) is a recently discovered boron-rich compound whose crystal structure (space group R-3m, rhombohedral unit cell with a = 7.4096 Å and α = 43.539°) is known, but its electronic, dielectric, phononic, and elastic properties have not been measured or calculated. This task computes those properties from first principles to assess the material's potential for optoelectronic applications.

## Approach
Density functional theory (DFT) calculations are performed with the open-source ABINIT code. The exchange-correlation functional is the PBE generalized gradient approximation, and norm-conserving Troullier–Martins pseudopotentials represent the ion cores. The workflow consists of: (i) relaxing the atomic positions at the experimental lattice parameters; (ii) computing the electronic band structure along the high-symmetry path F–Γ–Z–L–Γ; (iii) obtaining the electronic dielectric permittivity tensor ε^∞ and Born effective charges via density functional perturbation theory (DFPT); (iv) calculating zone‑center phonon frequencies, including LO–TO splitting, using the previously obtained dielectric and charge data; (v) computing the relaxed‑ion elastic constants from DFPT strain perturbations. All quantities are compiled into a single JSON file that covers the targeted physical properties.

## Reproduction target
From the DFT/DFPT runs, extract and report the following quantities in a JSON file: the indirect band gap (energy difference between the valence‑band maximum at Z and the conduction‑band minimum at L); the electronic dielectric permittivity tensor components ε_⊥^∞ and ε_∥^∞; the static dielectric tensor components ε_⊥^0 and ε_∥^0, derived from the TO‑mode oscillator strengths; the six independent elastic constants C11, C12, C13, C14, C33, C44; the Voigt‑averaged bulk modulus B and shear modulus G; and the frequencies of eight selected zone‑center phonon modes (Eu_TO1, Eu_LO1, Eu_TO9, Eu_LO9, A2u_TO1, A2u_LO1, A2u_TO7, A2u_LO7). All calculations use the 22‑atom rhombohedral cell at the experimental lattice parameters.

## Assets

- ABINIT: https://www.abinit.org
- MgNB₉ crystallographic data: 10.1107/S0108270102008765

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Relax the atomic positions of MgNB₉ in the rhombohedral unit cell at the experimental lattice parameters (a_rh = 7.4096 Å, α_rh = 43.539°) using ABINIT. Produce relaxed atomic coordinates.
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 2: Electronic band structure
- Role: process
- Action: Using the relaxed structure, compute the electronic band structure along the high-symmetry path F–Γ–Z–L–Γ. Save the k-point coordinates and the corresponding band energies in a CSV file.
- Evidence: `/app/outputs/band_structure.csv`

### Step 3: Dielectric tensor and Born effective charges
- Role: process
- Action: Compute the electronic dielectric permittivity tensor (ε^∞) and the Born effective charge tensors using density functional perturbation theory (DFPT) in ABINIT.
- Evidence: `/app/outputs/dfpt_dielectric.log`

### Step 4: Zone‑center phonon frequencies
- Role: process
- Action: Compute the dynamical matrix at Γ point via DFPT, including LO‑TO splitting using the previously obtained ε^∞ and Z*. Output the phonon frequencies and eigenvectors.
- Evidence: `/app/outputs/phonon_output.log`

### Step 5: Elastic constants
- Role: process
- Action: Compute the relaxed‑ion elastic constants Cij via DFPT strain perturbations. Derive the six independent constants of the trigonal system.
- Evidence: `/app/outputs/elastic_output.log`

### Step 6: Compile final properties
- Role: scored (load-bearing)
- Action: From the preceding calculations, extract the indirect band gap (valence‑band maximum at Z, conduction‑band minimum at L), the electronic dielectric tensor components ε^∞_⊥ and ε^∞_∥, compute the static dielectric tensor components ε^0_⊥ and ε^0_∥ by summing ε^∞ and the ionic contributions (4π/Ω0) * (oscillator strength tensor) / ω_m^2 over all TO modes, list the selected phonon frequencies (Eu_TO1, Eu_LO1, Eu_TO9, Eu_LO9, A2u_TO1, A2u_LO1, A2u_TO7, A2u_LO7), and report the elastic constants C11, C12, C13, C14, C33, C44 together with the Voigt bulk modulus B and shear modulus G. Write all quantities into a single JSON file according to the output schema.
- Output file: `/app/outputs/reproduced_properties.json`
- Format: json
- Contract: {
  "band_gap_eV": <float>,
  "epsilon_inf_perp": <float>,
  "epsilon_inf_par": <float>,
  "epsilon_0_perp": <float>,
  "epsilon_0_par": <float>,
  "C11": <float>,
  "C12": <float>,
  "C13": <float>,
  "C14": <float>,
  "C33": <float>,
  "C44": <float>,
  "bulk_modulus_GPa": <float>,
  "shear_modulus_GPa": <float>,
  "phonon_frequencies_cm-1": {
    "Eu_TO1": <float>,
    "Eu_LO1": <float>,
    "Eu_TO9": <float>,
    "Eu_LO9": <float>,
    "A2u_TO1": <float>,
    "A2u_LO1": <float>,
    "A2u_TO7": <float>,
    "A2u_LO7": <float>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_properties.json
- path: `/app/outputs/reproduced_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Compiled physical properties from DFT/DFPT calculations. Verified by comparing each value against the paper-reported gold with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `epsilon_inf_perp`: number
    - `epsilon_inf_par`: number
    - `epsilon_0_perp`: number
    - `epsilon_0_par`: number
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C13`: number (GPa)
    - `C14`: number (GPa)
    - `C33`: number (GPa)
    - `C44`: number (GPa)
    - `bulk_modulus_GPa`: number (GPa)
    - `shear_modulus_GPa`: number (GPa)
    - `phonon_frequencies_cm-1`:
      - `type`: object
      - `required`:
        - `Eu_TO1`: number (cm⁻¹)
        - `Eu_LO1`: number (cm⁻¹)
        - `Eu_TO9`: number (cm⁻¹)
        - `Eu_LO9`: number (cm⁻¹)
        - `A2u_TO1`: number (cm⁻¹)
        - `A2u_LO1`: number (cm⁻¹)
        - `A2u_TO7`: number (cm⁻¹)
        - `A2u_LO7`: number (cm⁻¹)

Notes: The reproducibility of the band gap indirect nature (Z-L) is checked by inspecting the band_structure.csv evidence, but that check is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "epsilon_inf_perp": "number",
          "epsilon_inf_par": "number",
          "epsilon_0_perp": "number",
          "epsilon_0_par": "number",
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C13": "number (GPa)",
          "C14": "number (GPa)",
          "C33": "number (GPa)",
          "C44": "number (GPa)",
          "bulk_modulus_GPa": "number (GPa)",
          "shear_modulus_GPa": "number (GPa)",
          "phonon_frequencies_cm-1": {
            "type": "object",
            "required": {
              "Eu_TO1": "number (cm⁻¹)",
              "Eu_LO1": "number (cm⁻¹)",
              "Eu_TO9": "number (cm⁻¹)",
              "Eu_LO9": "number (cm⁻¹)",
              "A2u_TO1": "number (cm⁻¹)",
              "A2u_LO1": "number (cm⁻¹)",
              "A2u_TO7": "number (cm⁻¹)",
              "A2u_LO7": "number (cm⁻¹)"
            }
          }
        }
      },
      "description": "Compiled physical properties from DFT/DFPT calculations. Verified by comparing each value against the paper-reported gold with appropriate tolerances."
    }
  ],
  "notes": "The reproducibility of the band gap indirect nature (Z-L) is checked by inspecting the band_structure.csv evidence, but that check is not scored."
}
```

## How you are scored
A hidden verifier reads your `reproduced_properties.json` file and compares each numeric entry to a reference value. The overall score is a weighted combination of these comparisons, with the largest weights on the band gap, dielectric constants, elastic constants, and phonon frequencies. The verifier applies tolerances that accommodate the expected variation between different DFT implementations; you do not need to match any published number exactly. Honest execution of the full ab‑initio workflow and reporting your computed numbers should yield a high score. The indirect‑gap character is additionally confirmed by checking your band‑structure output, but this check does not contribute to the numeric score.
