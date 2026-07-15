# DFT electronic structure and optical properties of a layered Aurivillius oxide

## Problem background
CaBi2Ta2O9 is a layered Aurivillius-phase ferroelectric oxide with potential applications in non-volatile memory devices. Its ferroelectricity is thought to originate from strong orbital hybridization between Bi–O and Ta–O atoms, and its optical response is anisotropic—factors critical for device performance. This task aims to computationally determine three first-principles quantities for this compound: the electronic band gap and its nature (direct/indirect), the orbital-resolved density of states revealing hybridization features, and the imaginary part of the dielectric function to evaluate optical isotropy below 4 eV versus anisotropy above 4 eV.

## Approach
Calculations use density-functional theory (DFT) within the generalized gradient approximation (GGA). An open-source plane-wave DFT code (e.g., Quantum ESPRESSO) is employed with standard GGA-PBE pseudopotentials (from SSSP or equivalent). The crystal structure is orthorhombic, space group A2₁am (No. 36), with lattice parameters a = 5.4438 Å, b = 5.4273 Å, c = 24.919 Å. The relaxed atomic positions (fractional coordinates) are:
- Ca: (0, 0.2473, 0)
- Bi: (0.4852, 0.7738, 0.19786)
- Ta: (0.51980, 0.7482, 0.4059)
- O(1): (0.5560, 0.3166, 0)
- O(2): (0.5279, 0.6789, 0.3423)
- O(3): (0.7498, 0.9756, 0.24999)
- O(4): (0.7526, 0.9588, 0.06375)
- O(5): (0.8369, 0.9453, 0.57943)

Use this structure directly; no geometry optimization is performed. After a self-consistent field (SCF) calculation, the band structure is computed along a high‑symmetry k‑path, the density of states is projected onto atomic orbitals, and the imaginary dielectric function ε₂(ω) is obtained from interband transition matrix elements for three polarization directions (xx, yy, zz). The key results are distilled into three JSON artifacts: the band gap and its character, a summary of dominant orbital contributions and the Bi–O hybridization energy window, and the dielectric function components with flags for isotropy below 4 eV and anisotropy above 4 eV.

## Reproduction target
Produce the following three files under /app/outputs:
1. **band_gap.json** — the computed electronic band gap (in eV), a boolean `is_indirect` indicating whether the gap is indirect, and the labels of the k‑points where the valence band maximum (VBM) and conduction band minimum (CBM) occur.
2. **partial_dos_summary.json** — a summary listing the dominant atomic‑orbital contributions in the valence band and in the conduction band (expected types: Bi 6p, Ta 5d, O 2p) and the energy window (a string such as `"0-4 eV"`) where strong Bi 6p–O 2p hybridization is observed.
3. **dielectric_function_imag.json** — arrays of photon energies `energies_eV` and the imaginary part of the dielectric function for the three polarizations `eps_xx`, `eps_yy`, `eps_zz`. Also include two Boolean flags: `isotropic_below_4eV` (true if the maximum relative difference among the three components across 0–4 eV is less than 10%) and `anisotropic_above_4eV` (true if that difference exceeds 10% above 4 eV).

All calculations must be based on the provided crystal structure and GGA‑PBE functionals. The solver must run the DFT workflow without relying on precomputed results.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (GGA-PBE): https://www.quantum-espresso.org/pseudopotentials
- Crystal structure of CaBi2Ta2O9

## Workflow steps

### Step 1: Crystal structure setup
- Role: process
- Action: Construct the orthorhombic CaBi2Ta2O9 crystal structure (space group A2_1am) using the provided lattice parameters and atomic coordinates. Generate the appropriate input file for the DFT code (Quantum ESPRESSO pseudo-potential inputs).
- Evidence: `/app/outputs/structure_setup.log`

### Step 2: Self-consistent field (SCF) calculation
- Role: process
- Action: Perform a self-consistent DFT calculation within the generalized gradient approximation (GGA) using the plane-wave code to converge the charge density and total energy. Save the final wavefunctions and charge density for subsequent steps.
- Evidence: `/app/outputs/scf_convergence.log`

### Step 3: Band structure and band gap
- Role: scored (load-bearing)
- Action: Using the converged SCF results, compute the band structure along the high-symmetry path in the first Brillouin zone. Identify the valence band maximum (VBM) and conduction band minimum (CBM), determine the band gap value in eV, and whether it is direct or indirect. Write the findings to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"band_gap_eV": float, "is_indirect": bool, "vbm_kpoint": string, "cbm_kpoint": string}
- Scoring: scored by hidden verifier

### Step 4: Partial density of states analysis
- Role: scored
- Action: Using the SCF wavefunctions, compute atom- and orbital-projected densities of states. Summarize the dominant orbital contributions in the valence band region and conduction band region, and note the energy window where strong Bi 6p–O 2p hybridization occurs. Save the summary to partial_dos_summary.json.
- Output file: `/app/outputs/partial_dos_summary.json`
- Format: json
- Contract: {"valence_band_dominant_orbitals": [string], "conduction_band_dominant_orbitals": [string], "bi_o_hybridization_energy_window": string, "notes": string}
- Scoring: scored by hidden verifier

### Step 5: Imaginary dielectric function
- Role: scored
- Action: Calculate the imaginary part of the dielectric function for three polarization directions (xx, yy, zz) from interband transitions. Output arrays of photon energies and the three components. Include boolean flags indicating whether the response is isotropic below 4 eV and anisotropic above 4 eV. Write the data to dielectric_function_imag.json.
- Output file: `/app/outputs/dielectric_function_imag.json`
- Format: json
- Contract: {"energies_eV": [float], "eps_xx": [float], "eps_yy": [float], "eps_zz": [float], "isotropic_below_4eV": bool, "anisotropic_above_4eV": bool}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/partial_dos_summary.json`
- `/app/outputs/dielectric_function_imag.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The computed indirect band gap of CaBi2Ta2O9, its direct/indirect nature, and the locations of the VBM and CBM.
- schema:
  - `type`: object
  - `required`: `band_gap_eV`, `is_indirect`, `vbm_kpoint`, `cbm_kpoint`
  - `properties`:
    - `band_gap_eV`:
      - `type`: number
      - `description`: Computed band gap in eV
    - `is_indirect`:
      - `type`: boolean
      - `description`: True if the gap is indirect
    - `vbm_kpoint`:
      - `type`: string
      - `description`: Label of the k-point where the valence band maximum occurs
    - `cbm_kpoint`:
      - `type`: string
      - `description`: Label of the k-point where the conduction band minimum occurs

### partial_dos_summary.json
- path: `/app/outputs/partial_dos_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Summarized partial DOS analysis: dominant orbital contributions in valence and conduction bands and the energy window of strong Bi–O hybridization.
- schema:
  - `type`: object
  - `required`: `valence_band_dominant_orbitals`, `conduction_band_dominant_orbitals`, `bi_o_hybridization_energy_window`, `notes`
  - `properties`:
    - `valence_band_dominant_orbitals`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: List of dominant atomic orbitals in the valence band (e.g., Bi 6p, Ta 5d, O 2p)
    - `conduction_band_dominant_orbitals`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: List of dominant atomic orbitals in the conduction band
    - `bi_o_hybridization_energy_window`:
      - `type`: string
      - `description`: Energy window where strong Bi 6p – O 2p hybridization is observed (e.g., '0-4 eV')
    - `notes`:
      - `type`: string
      - `description`: Brief qualitative note on the hybridization features

### dielectric_function_imag.json
- path: `/app/outputs/dielectric_function_imag.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of the dielectric function for three polarizations, with flags reporting isotropy below 4 eV and anisotropy above 4 eV.
- schema:
  - `type`: object
  - `required`: `energies_eV`, `eps_xx`, `eps_yy`, `eps_zz`, `isotropic_below_4eV`, `anisotropic_above_4eV`
  - `properties`:
    - `energies_eV`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Array of photon energies in eV
    - `eps_xx`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Imaginary part ε₂ for x-polarization
    - `eps_yy`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Imaginary part ε₂ for y-polarization
    - `eps_zz`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Imaginary part ε₂ for z-polarization
    - `isotropic_below_4eV`:
      - `type`: boolean
      - `description`: Whether the dielectric function is isotropic (max component difference <10%) over 0-4 eV
    - `anisotropic_above_4eV`:
      - `type`: boolean
      - `description`: Whether the dielectric function is anisotropic (max component difference >10%) above 4 eV

Notes: Geometry optimization is omitted; the agent uses the relaxed structure from Table 1 directly. The original WIEN2k code is replaced by the open-source Quantum ESPRESSO. All required resources are public and listed in resources.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_eV",
          "is_indirect",
          "vbm_kpoint",
          "cbm_kpoint"
        ],
        "properties": {
          "band_gap_eV": {
            "type": "number",
            "description": "Computed band gap in eV"
          },
          "is_indirect": {
            "type": "boolean",
            "description": "True if the gap is indirect"
          },
          "vbm_kpoint": {
            "type": "string",
            "description": "Label of the k-point where the valence band maximum occurs"
          },
          "cbm_kpoint": {
            "type": "string",
            "description": "Label of the k-point where the conduction band minimum occurs"
          }
        }
      },
      "description": "The computed indirect band gap of CaBi2Ta2O9, its direct/indirect nature, and the locations of the VBM and CBM."
    },
    {
      "file": "partial_dos_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "valence_band_dominant_orbitals",
          "conduction_band_dominant_orbitals",
          "bi_o_hybridization_energy_window",
          "notes"
        ],
        "properties": {
          "valence_band_dominant_orbitals": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of dominant atomic orbitals in the valence band (e.g., Bi 6p, Ta 5d, O 2p)"
          },
          "conduction_band_dominant_orbitals": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of dominant atomic orbitals in the conduction band"
          },
          "bi_o_hybridization_energy_window": {
            "type": "string",
            "description": "Energy window where strong Bi 6p – O 2p hybridization is observed (e.g., '0-4 eV')"
          },
          "notes": {
            "type": "string",
            "description": "Brief qualitative note on the hybridization features"
          }
        }
      },
      "description": "Summarized partial DOS analysis: dominant orbital contributions in valence and conduction bands and the energy window of strong Bi–O hybridization."
    },
    {
      "file": "dielectric_function_imag.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "energies_eV",
          "eps_xx",
          "eps_yy",
          "eps_zz",
          "isotropic_below_4eV",
          "anisotropic_above_4eV"
        ],
        "properties": {
          "energies_eV": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Array of photon energies in eV"
          },
          "eps_xx": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Imaginary part ε₂ for x-polarization"
          },
          "eps_yy": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Imaginary part ε₂ for y-polarization"
          },
          "eps_zz": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Imaginary part ε₂ for z-polarization"
          },
          "isotropic_below_4eV": {
            "type": "boolean",
            "description": "Whether the dielectric function is isotropic (max component difference <10%) over 0-4 eV"
          },
          "anisotropic_above_4eV": {
            "type": "boolean",
            "description": "Whether the dielectric function is anisotropic (max component difference >10%) above 4 eV"
          }
        }
      },
      "description": "Imaginary part of the dielectric function for three polarizations, with flags reporting isotropy below 4 eV and anisotropy above 4 eV."
    }
  ],
  "notes": "Geometry optimization is omitted; the agent uses the relaxed structure from Table 1 directly. The original WIEN2k code is replaced by the open-source Quantum ESPRESSO. All required resources are public and listed in resources.json."
}
```

## How you are scored
A hidden verifier inspects each of the three output files. For `band_gap.json`, the band gap value is compared to a hidden reference with an undisclosed tolerance; the boolean `is_indirect` and the VBM/CBM k‑point labels are checked for correctness. For `partial_dos_summary.json`, the verifier audits that the listed orbitals belong to the expected set (Bi 6p, Ta 5d, O 2p) and that the hybridization window is plausible given the material. For `dielectric_function_imag.json`, the verifier confirms that the arrays are well‑formed and cover a realistic energy range, and it checks that the `isotropic_below_4eV` and `anisotropic_above_4eV` flags are consistent with the supplied ε₂ data using the 10% difference criterion. The final reward (0.0–1.0) is a weighted combination of these checks. Simply reporting values without genuine DFT computation will not satisfy the verifier’s consistency and structural audits.
