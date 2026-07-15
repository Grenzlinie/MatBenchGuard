# DFT band structure eigenvalues and elastic constants of TiN

## Problem background
Titanium nitride (TiN) is a hard, refractory material with metallic conductivity. Accurate first-principles description of its electronic structure and elastic properties is important for understanding its bonding and applications. Various theoretical approaches — including Hartree‑Fock, local density approximation (LDA), and different generalized gradient approximations (GGA) — have been applied to TiN, and it is known that computed band energies can vary substantially depending on the functional. The goal of this task is to use a BLYP‑type GGA density functional method to compute key electronic and mechanical properties of TiN and compare them with available experimental measurements, thereby assessing the reliability of modern DFT approaches for this class of refractory materials.

## Approach
Use density functional theory with a GGA functional that approximates the BLYP exchange‑correlation (e.g., PBE) in an open‑source plane‑wave code (Quantum ESPRESSO) and appropriate pseudopotentials. The workflow consists of three main blocks:

1. **Bulk electronic structure** – Perform a self‑consistent field (SCF) calculation for bulk TiN in the rocksalt structure at the experimental lattice constant. Then run a non‑self‑consistent bands calculation along the Γ→X direction and extract the energy eigenvalues (relative to the Fermi level) for selected high‑symmetry states.

2. **Elastic constants** – Apply a set of small, volume‑conserving deformations to the bulk unit cell, compute the total energy of each strained configuration, and fit the energy‑versus‑strain data to obtain the cubic elastic constants C₁₁, C₁₂, and C₄₄.

3. **Surface state** – Construct a 4‑layer TiN(001) slab model with sufficient vacuum. Perform SCF and band‑structure calculations and identify the non‑dispersive σ‑type surface state (band A) that originates from N 2pz orbitals; record its energy at the Γ point.

In all steps the same BLYP‑type functional and basis set (pseudopotential) are used, and numerical parameters (plane‑wave cutoff, k‑point mesh) must be converged to ensure meaningful results.

## Reproduction target
Compute the BLYP (or equivalent GGA) band eigenvalues at the Γ and X points — specifically the Γ₁₅, X₃, X₅′, and X₄′ states — relative to the Fermi level for bulk TiN in the rocksalt structure (lattice constant 0.4242 nm). Then calculate the cubic elastic constants C₁₁, C₁₂, C₄₄ via total‑energy vs. strain fits. Finally, construct a 4‑layer TiN(001) slab model with vacuum and compute its band structure to extract the energy of the σ‑type surface state (band A) at the Γ point. All calculations must be performed with an open‑source plane‑wave DFT code (Quantum ESPRESSO) using appropriate pseudopotentials and converged numerical parameters.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ti ONCV pseudopotential (SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- N ONCV pseudopotential (SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Setup bulk TiN input files
- Role: process
- Action: Create Quantum ESPRESSO input files for a bulk TiN unit cell in the rocksalt structure (space group Fm-3m, lattice constant a=0.4242 nm). Define a converged k-mesh and plane-wave cutoff suitable for the chosen pseudopotentials. Set up a band structure path along Gamma-Delta-X.
- Evidence: none

### Step 2: Run BLYP bulk SCF and band structure
- Role: process
- Action: Perform a self-consistent field (SCF) calculation for the bulk TiN unit cell using a GGA functional approximating BLYP (e.g., PBE with appropriate parameters) in Quantum ESPRESSO. Then run a non-self-consistent bands calculation along the Gamma-Delta-X path and process the data to obtain eigenvalues at the Gamma and X points.
- Evidence: `/app/outputs/bulk_bands.dat`

### Step 3: Extract bulk eigenvalues at high-symmetry states
- Role: scored (load-bearing)
- Action: From the bulk band structure, identify the energy eigenvalues (in eV, relative to the Fermi level) corresponding to the Gamma15, X3, X5', and X4' states. Output a JSON file with keys 'Gamma15', 'X3', 'X5_prime', 'X4_prime' containing the extracted values.
- Output file: `/app/outputs/bulk_eigenvalues.json`
- Format: json
- Contract: { 'Gamma15': float, 'X3': float, 'X5_prime': float, 'X4_prime': float }
- Scoring: scored by hidden verifier

### Step 4: Compute elastic constants via energy-strain fits
- Role: scored
- Action: Apply a series of small volume-conserving deformations (orthorhombic, monoclinic) to the bulk TiN unit cell. For each deformed configuration, run a DFT total energy calculation with the BLYP functional in Quantum ESPRESSO. Fit the energy vs. strain data to a polynomial and derive the cubic elastic constants C11, C12, C44 (in Mbar). Write these three values to a JSON file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: { 'C11': float, 'C12': float, 'C44': float }
- Scoring: scored by hidden verifier

### Step 5: Setup and run BLYP DFT for 4-layer TiN(001) slab
- Role: process
- Action: Construct a 4-layer TiN(001) slab model (terminated with Ti and N in equal numbers) with a sufficient vacuum layer (e.g., 15 Å). Create Quantum ESPRESSO input files, perform SCF and band structure calculations along the Gamma-Delta-X direction using the same BLYP functional.
- Evidence: `/app/outputs/slab_bands.dat`

### Step 6: Extract surface state energy at Gamma
- Role: scored
- Action: Examine the slab band structure and identify the non-dispersive sigma-type surface state (band A) that originates from N 2pz orbitals near the Fermi level. Record its energy eigenvalue (relative to EF) at the Gamma point. Write this single float value to a plain text file.
- Output file: `/app/outputs/surface_state_gamma_energy.txt`
- Format: txt
- Contract: A plain text file with one float (e.g., '-2.9')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_eigenvalues.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/surface_state_gamma_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_eigenvalues.json
- path: `/app/outputs/bulk_eigenvalues.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk TiN BLYP eigenvalues at Gamma15, X3, X5', and X4' relative to the Fermi energy.
- schema:
  - `type`: object
  - `required`:
    - `Gamma15`: float (eV)
    - `X3`: float (eV)
    - `X5_prime`: float (eV)
    - `X4_prime`: float (eV)

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Cubic elastic constants of TiN computed via BLYP energy-strain fits.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (Mbar)
    - `C12`: float (Mbar)
    - `C44`: float (Mbar)

### surface_state_gamma_energy.txt
- path: `/app/outputs/surface_state_gamma_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy of the sigma-type surface state (band A) at the Gamma point of a 4-layer TiN(001) slab, relative to EF.
- schema:
  - `type`: text
  - `units`:
    - `value`: eV

Notes: The solving agent must use an open-source plane-wave DFT code (Quantum ESPRESSO) and appropriate pseudopotentials. The BLYP functional should be approximated (e.g., using PBE with selected parameters) as exact BLYP may not be directly available. All energies are relative to the Fermi level.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Gamma15": "float (eV)",
          "X3": "float (eV)",
          "X5_prime": "float (eV)",
          "X4_prime": "float (eV)"
        }
      },
      "description": "Bulk TiN BLYP eigenvalues at Gamma15, X3, X5', and X4' relative to the Fermi energy."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (Mbar)",
          "C12": "float (Mbar)",
          "C44": "float (Mbar)"
        }
      },
      "description": "Cubic elastic constants of TiN computed via BLYP energy-strain fits."
    },
    {
      "file": "surface_state_gamma_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "eV"
        }
      },
      "description": "Energy of the sigma-type surface state (band A) at the Gamma point of a 4-layer TiN(001) slab, relative to EF."
    }
  ],
  "notes": "The solving agent must use an open-source plane-wave DFT code (Quantum ESPRESSO) and appropriate pseudopotentials. The BLYP functional should be approximated (e.g., using PBE with selected parameters) as exact BLYP may not be directly available. All energies are relative to the Fermi level."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored artifacts: `bulk_eigenvalues.json`, `elastic_constants.json`, and `surface_state_gamma_energy.txt`. For each artifact, the verifier compares your computed value(s) with reference data (e.g., experimental photoemission energies or measured elastic constants) and awards credit when the result falls within an acceptable tolerance. The final score is a weighted combination of these individual checks; simply reporting literature numbers without executing the DFT workflow will result in a low score.
