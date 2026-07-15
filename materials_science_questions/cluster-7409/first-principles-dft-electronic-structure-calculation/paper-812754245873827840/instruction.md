# Tight‑binding and scattering‑theoretic calculation of TiO₂ surface electronic structure

## Problem background
Rutile TiO₂ is a wide-gap semiconductor important for catalysis, photovoltaics, and electrochemical processes. Understanding the electronic structure of its ideal, defect‑free surfaces is essential for interpreting experimental spectra and device behavior. This task computes the surface band structure, surface‑state energies, and layer‑ and orbital‑resolved densities of states to determine whether surface states appear in the optical band gap, and to characterise their character and localization.

## Approach
The bulk electronic structure of TiO₂ is described by a tight‑binding Hamiltonian including Ti 3d, O 2p, and O 2s orbitals with interactions up to second‑nearest neighbours, using the parameterisation of Vos (1977). The surface electronic structure is obtained with the scattering‑theoretic method (STM). In this approach, the bulk Green's function is first constructed in a layer‑orbital basis adapted to the surface orientation. The surface is created by applying an infinite‑energy perturbation that removes the atomic layers that would lie above the surface; the surface Green's function is then obtained by solving Dyson's equation. Surface bound states are identified from the determinant condition, and local densities of states are derived from the imaginary part of the surface Green's function. The analysis focuses on the (110) surface terminated by the most compact atomic plane (Model I), which contains two Ti and two O atoms per surface unit cell.

## Reproduction target
Reproduce the surface electronic structure for the TiO₂(110) surface terminated by the compact atomic plane (Model I). Specifically:
- Compute the energy of the titanium‑derived surface state at the Γ point (q = 0) relative to the top of the valence band (taken as 0 eV).
- Compute the layer‑ and orbital‑resolved densities of states at Γ for the top three surface layers over the energy range from –5 eV to 8 eV.
The results allow a determination of whether surface states reside in the optical gap and, in particular, whether oxygen‑derived states occupy that energy interval.

## Assets

- Rutile TiO₂ crystal structure (a=4.594 Å, c=2.959 Å, u=0.305): 10.1063/1.1676432
- Vos tight‑binding parameter set for rutile TiO₂: 10.1088/0022-3719/10/19/018
- Scattering‑theoretic method (STM) formalism: 10.1103/PhysRevB.18.5524

## Workflow steps

### Step 1: Construct and diagonalize bulk tight‑binding Hamiltonian
- Role: process
- Action: Construct the spinless tight‑binding Hamiltonian matrix for bulk rutile TiO₂ using the Vos parameterization (on‑site energies E_d=2.9 eV, E_p=–1.2 eV, hopping parameters up to second‑nearest neighbors, basis: Ti 3d, O 2p, O 2s). Diagonalize on a uniform three‑dimensional k‑point mesh to obtain eigenvalues and eigenvectors.
- Evidence: `/app/outputs/bulk_eigenvalues.npy`

### Step 2: Compute bulk Green's function in layer‑orbital basis
- Role: process
- Action: For the (110) surface orientation, transform the bulk eigenstates into the layer‑orbital representation (atomic layer m, orbital α, atom position μ) and compute the bulk Green's function G^b_{l,l'}(q,E) for a discrete set of surface‑parallel wave vectors q and energy points employing the standard spectral representation.
- Evidence: none

### Step 3: Compute surface Green's function for TiO₂(110) Model I
- Role: process
- Action: Construct the perturbation U that removes the layers to create the compact Model I surface (first layer contains Ti₁, Ti₂, O₁, O₂). Solve Dyson's equation to obtain the surface Green's function G^s_{ll}(q,E). Identify surface bound states via the determinant condition and compute local densities of states.
- Evidence: none

### Step 4: Determine Ti‑d surface state energy at Γ
- Role: scored (load-bearing)
- Action: Locate the Ti‑d derived surface bound state at the Γ point (q=0) for the (110) Model I surface, either from the determinant condition or from a dominant Ti‑projected peak in the DOS within the band gap. Write a single floating‑point number (energy in eV relative to the top of the valence band at 0 eV) to a text file.
- Output file: `/app/outputs/surface_state_energy.txt`
- Format: txt
- Contract: A single floating‑point number on one line, e.g. 2.85
- Scoring: scored by hidden verifier

### Step 5: Compute layer‑ and orbital‑resolved DOS at Γ for top layers
- Role: scored
- Action: Compute the local densities of states N_{l}(Γ,E) = –1/π Im G^s_{ll} for the top three layers (indices 0,1,2) of the (110) Model I surface. Output a CSV file covering energies from –5 eV to 8 eV with a step of 0.05 eV. Include all atoms in each layer with appropriate orbital labels.
- Output file: `/app/outputs/layer_dos_gamma.csv`
- Format: csv
- Contract: CSV columns: layer (int), atom (string, e.g. Ti1, Ti2, O1, O2, O3), orbital (string, e.g. x2‑y2, xz, yz, xy, 3z2‑r2, x, y, z), energy (float32, eV), dos (float32, states/eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_state_energy.txt`
- `/app/outputs/layer_dos_gamma.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_state_energy.txt
- path: `/app/outputs/surface_state_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy of the Ti‑d surface bound state at Γ for TiO₂(110) Model I, relative to the valence‑band top.
- schema:
  - `type`: text
  - `description`: A single floating‑point number, energy in eV, on one line.

### layer_dos_gamma.csv
- path: `/app/outputs/layer_dos_gamma.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Orbital‑resolved density of states at Γ for the top three layers of TiO₂(110) Model I. The checker uses this to audit the absence of oxygen‑derived states in the gap.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `atom`, `orbital`, `energy`, `dos`
  - `columns`:
    - `layer`: int
    - `atom`: str (Ti1, Ti2, O1, O2, O3)
    - `orbital`: str (x2‑y2, xz, yz, xy, 3z2‑r2, x, y, z)
    - `energy`: float32, eV
    - `dos`: float32, states/eV
  - `units`:
    - `energy`: eV
    - `dos`: states/eV

Notes: The surface state energy is compared to the paper‑reported value with a hidden tolerance. The layer‑resolved DOS is audited for negligible oxygen projection in the energy interval [0, 3] eV (the band gap).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_state_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number, energy in eV, on one line."
      },
      "description": "Energy of the Ti‑d surface bound state at Γ for TiO₂(110) Model I, relative to the valence‑band top."
    },
    {
      "file": "layer_dos_gamma.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "atom",
          "orbital",
          "energy",
          "dos"
        ],
        "columns": {
          "layer": "int",
          "atom": "str (Ti1, Ti2, O1, O2, O3)",
          "orbital": "str (x2‑y2, xz, yz, xy, 3z2‑r2, x, y, z)",
          "energy": "float32, eV",
          "dos": "float32, states/eV"
        },
        "units": {
          "energy": "eV",
          "dos": "states/eV"
        }
      },
      "description": "Orbital‑resolved density of states at Γ for the top three layers of TiO₂(110) Model I. The checker uses this to audit the absence of oxygen‑derived states in the gap."
    }
  ],
  "notes": "The surface state energy is compared to the paper‑reported value with a hidden tolerance. The layer‑resolved DOS is audited for negligible oxygen projection in the energy interval [0, 3] eV (the band gap)."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden automated verifier. Each scored workflow step carries a weight that contributes to the final reward. The verifier reads `surface_state_energy.txt` and checks that it contains a single floating‑point number; that value is compared against a hidden reference derived from the paper to assess correctness. The file `layer_dos_gamma.csv` is audited for correct structure (required columns, data types) and for the magnitude of the oxygen‑projected density of states in the energy range that corresponds to the optical gap. Simply reporting a number without having genuinely executed the required tight‑binding and STM workflow will not pass these checks.
