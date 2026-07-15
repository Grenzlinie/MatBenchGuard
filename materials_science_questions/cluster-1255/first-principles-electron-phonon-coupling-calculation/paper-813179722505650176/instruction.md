# High-pressure GeH3 enthalpy and superconducting transition temperature from first principles

## Problem background
At high pressures, germanium hydrides can adopt unusual stoichiometries and crystal structures that are stabilized by quantum nuclear effects. In particular, germanium trihydride (GeH₃) has been predicted to become stable beyond ~175 GPa when the zero-point energy of the nuclei is included, with three competing metallic structures: A15 (Pm-3n), P4₂/mmc, and Cccm. This task reproduces the first-principles investigation of the relative enthalpies and the superconducting properties of these three GeH₃ phases at high density. The goal is to compute the static electronic energy, the harmonic zero‑point energy, the resulting enthalpy, the electron‑phonon coupling strength, and the superconducting transition temperature, and to determine which structure is thermodynamically favoured.

## Approach
The reproduction uses density functional theory (DFT) within the generalized gradient approximation. You will construct the three crystal structures at the electron density corresponding to rₛ = 1.52 (approximately 180 GPa) from the published lattice constants and atomic positions, then relax them to equilibrium. Using the relaxed geometries, you will compute the harmonic phonon frequencies (e.g., by the frozen‑phonon method) and extract the zero‑point energy per atom. To obtain the superconducting properties, you will perform density functional perturbation theory (DFPT) to calculate the Eliashberg spectral function α²F(ω), from which the electron‑phonon coupling constant λ, the logarithmic average frequency ω_log, and the superconducting critical temperature T_c (via the Allen‑Dynes modified McMillan formula with Coulomb pseudopotential μ* = 0.13) are derived. The final step compares the enthalpies (static + zero‑point) to establish the relative stability of the three structures.

## Reproduction target
Produce a JSON file `results.json` containing, for each of the three GeH₃ structures (A15, P4₂/mmc, Cccm) computed at rₛ = 1.52, the following quantities: static total energy per atom (in Ry), harmonic zero‑point energy per atom (in Ry), enthalpy per atom (static + ZPE, in Ry), electron‑phonon coupling constant λ (dimensionless), logarithmic average frequency ω_log (in K), superconducting transition temperature T_c evaluated at μ* = 0.13 (in K), and a boolean flag indicating dynamical stability (`true` if no imaginary phonon frequencies exist). Use an open‑source plane‑wave DFT code and pseudopotentials from the SSSP library; the target is to correctly determine these properties and output them in the specified JSON format.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Construct Quantum ESPRESSO input files for the three GeH3 structures (A15, P4_2/mmc, Cccm) at r_s=1.52 using the following crystallographic data. For P4_2/mmc: a=b=3.033 Å, c=3.318 Å; Ge at 2c sites (0.0, 0.5, 0.0); H at 2e sites (0.0, 0.0, 0.25) and 4k sites (0.2244, 0.5, 0.5). For Cccm: a=4.718 Å, b=4.292 Å, c=3.014 Å; Ge at 4e sites (0.25, 0.25, 0.0); H at 4b sites (0.0, 0.5, 0.25) and 8l sites (0.1043, 0.8726, 0.0). For A15 (Pm-3n): the primitive cell contains 2 Ge and 6 H; derive the cubic lattice constant from r_s=1.52 as a = (14 * 4π (r_s a0)^3 / 3)^(1/3) ≈ 3.126 Å (with a0 = 0.52918 Å). Ge atoms occupy Wyckoff positions 2a (0,0,0; 1/2,1/2,1/2); H atoms occupy 6c (1/4,0,1/2; 1/2,1/4,0; 0,1/2,1/4). Select appropriate pseudopotentials for Ge and H from the SSSP library (efficiency set).
- Evidence: none

### Step 2: DFT relaxations
- Role: process
- Action: Perform variable-cell geometry optimizations for each structure at the target density/pressure to obtain relaxed atomic positions and static total energies. Use a suitable k-point density and energy cutoff.
- Evidence: none

### Step 3: Phonon and zero-point energy
- Role: process
- Action: Compute the harmonic phonon frequencies for the relaxed structures using the frozen-phonon or DFPT approach on appropriate supercells, and calculate the zero-point energy per atom. Ensure no imaginary phonon frequencies exist (dynamical stability).
- Evidence: none

### Step 4: Electron-phonon coupling and Tc
- Role: process
- Action: Run DFPT calculations on the relaxed structures with dense k-point and q-point grids to obtain the Eliashberg spectral function α²F(ω). Compute the electron-phonon coupling constant λ = 2∫ α²F/ω dω, the logarithmic average frequency ω_log, and estimate the superconducting transition temperature Tc using the Allen-Dynes modified McMillan formula with Coulomb pseudopotential μ* = 0.13.
- Evidence: none

### Step 5: Output results.json
- Role: scored (load-bearing)
- Action: Assemble the static total energies, harmonic zero-point energies, enthalpies (static+ZPE), λ, ω_log, Tc (at μ*=0.13), and a dynamical-stability flag for each of the three structures into a single JSON file named results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys 'A15', 'P4_2/mmc', 'Cccm'. Each value is an object: {static_energy_per_atom_Ry: float, zpe_per_atom_Ry: float, enthalpy_per_atom_Ry: float, lambda: float, omega_log_K: float, Tc_K_mu0.13: float, dynamically_stable: bool}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed physical properties for the three GeH3 crystal structures at r_s=1.52.
- schema:
  - `type`: object
  - `required`:
    - `A15`: object
    - `P4_2/mmc`: object
    - `Cccm`: object
  - `items`:
    - `static_energy_per_atom_Ry`: float
    - `zpe_per_atom_Ry`: float
    - `enthalpy_per_atom_Ry`: float
    - `lambda`: float
    - `omega_log_K`: float
    - `Tc_K_mu0.13`: float
    - `dynamically_stable`: bool

Notes: The submitted file will be checked for structural correctness and compared against hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A15": "object",
          "P4_2/mmc": "object",
          "Cccm": "object"
        },
        "items": {
          "static_energy_per_atom_Ry": "float",
          "zpe_per_atom_Ry": "float",
          "enthalpy_per_atom_Ry": "float",
          "lambda": "float",
          "omega_log_K": "float",
          "Tc_K_mu0.13": "float",
          "dynamically_stable": "bool"
        }
      },
      "description": "Computed physical properties for the three GeH3 crystal structures at r_s=1.52."
    }
  ],
  "notes": "The submitted file will be checked for structural correctness and compared against hidden reference values."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `results.json`. The verifier independently checks: (i) that each structure is declared dynamically stable (no imaginary phonon modes), (ii) that the relative ordering of the computed enthalpies is physically correct, and (iii) that the reported values of λ, ω_log, and T_c fall within preset tolerances (which account for the typical spread between different DFT codes) of hidden reference values derived from the original study. Credit is assigned primarily by the number of structures for which all three properties (λ, ω_log, T_c) simultaneously agree with the reference within tolerance; a correct enthalpy ordering is required for full credit. Partial credit is granted for fewer matches. The final reward is a weighted sum over all checks.
