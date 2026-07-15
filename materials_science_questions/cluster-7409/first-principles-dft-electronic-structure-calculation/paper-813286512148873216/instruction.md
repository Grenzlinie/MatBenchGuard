# Spin-polarized DFT calculation of oxygen vacancy on TiO2-terminated PbTiO3 surface

## Problem background
Ferroelectric PbTiO3 is normally non‑magnetic. Recent experimental observations, however, hint that vacancies—especially on the TiO2‑terminated (001) surface—may introduce a net magnetic moment and stabilize a ferromagnetic state in this material. This task uses first‑principles density‑functional theory (DFT) to investigate whether an oxygen vacancy at the surface layer of a TiO2‑terminated PbTiO3 thin film gives rise to spontaneous magnetism and, if so, how strongly the ferromagnetic state is favored over the non‑magnetic one.

## Approach
The investigation is carried out with spin‑density‑functional theory on a 2×2 periodic supercell that models a 9‑layer PbTiO3 thin film with a TiO2‑terminated (001) surface and a vacuum gap. An O1 oxygen atom is removed from the surface TiO2 layer to create an oxygen vacancy. Two total‑energy calculations are performed on this defective structure: (i) a spin‑polarized (collinear, ferromagnetic) calculation to obtain the ground‑state total energy E_FM and the integrated magnetic moment per vacancy; (ii) a non‑spin‑polarized (spin‑restricted) calculation to obtain the total energy E_NM of the non‑magnetic reference state. Atomic coordinates are fully relaxed until the forces on all atoms are converged. From the two energies the ferromagnetic stabilization energy ΔE_mag = E_FM − E_NM is computed. All calculations are done with an open‑source plane‑wave DFT code (Quantum ESPRESSO) and PAW pseudopotentials for Pb, Ti, and O, using appropriate plane‑wave cut‑off and k‑point sampling to ensure well‑converged results.

## Reproduction target
Compute, for the O1 vacancy on the TiO2‑terminated (001) surface, (a) the magnetic moment per vacancy in Bohr magnetons (µB) obtained from the spin‑polarized ground state, and (b) the total energy difference ΔE_mag = E_FM − E_NM in eV between the ferromagnetic and non‑magnetic states. Both values must be written to the JSON file `vacancy_properties.json` in the exact format specified by the output contract. These two numbers constitute the main numerical result of the reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary PAW pseudopotentials (Pb, Ti, O): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Build defective supercell
- Role: process
- Action: Construct a 2x2 periodic in-plane supercell of a 9-atomic-layer PbTiO3 thin film with TiO2-terminated (001) surface and a 12 Å vacuum layer. Use tetragonal lattice constants a=3.905 Å, c=4.154 Å and ideal perovskite atomic positions. Remove one O1 atom from the surface TiO2 layer to create the oxygen vacancy. Save the final atomic coordinates to a POSCAR-format file.
- Evidence: `/app/outputs/poscar_vacancy.txt`

### Step 2: Compute magnetic moment and ferromagnetic stability
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with PAW pseudopotentials for Pb, Ti, O, perform two total-energy calculations on the defective supercell: (i) a spin-polarized (collinear, ferromagnetic) run to obtain the ground-state total energy E_FM and the integrated magnetic moment per vacancy; (ii) a non-spin-polarized (spin-restricted) run to obtain total energy E_NM. Fully relax atomic positions (fixed lattice) until Hellmann-Feynman forces are below a tight threshold. Compute ΔE_mag = E_FM − E_NM. Write the magnetic moment (in μB) and ΔE_mag (in eV) to vacancy_properties.json.
- Output file: `/app/outputs/vacancy_properties.json`
- Format: json
- Contract: {
  "magnetic_moment_mu_B": float,
  "Delta_E_mag_eV": float
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_properties.json
- path: `/app/outputs/vacancy_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: magnetic moment per surface O1 vacancy and total energy difference between ferromagnetic and non-magnetic DFT states. The checker compares both values to hidden paper-reported references with appropriate tolerances; ΔE_mag must be negative.
- schema:
  - `type`: object
  - `required`:
    - `magnetic_moment_mu_B`: float (Bohr magnetons)
    - `Delta_E_mag_eV`: float (eV)

Notes: Only the main numeric result of the paper is reproduced: the magnetic moment and ΔE_mag for the O1 vacancy on the TiO2-terminated surface. The checker performs a result-level comparison (T0) against hidden paper values using tolerance windows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "magnetic_moment_mu_B": "float (Bohr magnetons)",
          "Delta_E_mag_eV": "float (eV)"
        }
      },
      "description": "Scored artifact: magnetic moment per surface O1 vacancy and total energy difference between ferromagnetic and non-magnetic DFT states. The checker compares both values to hidden paper-reported references with appropriate tolerances; ΔE_mag must be negative."
    }
  ],
  "notes": "Only the main numeric result of the paper is reproduced: the magnetic moment and ΔE_mag for the O1 vacancy on the TiO2-terminated surface. The checker performs a result-level comparison (T0) against hidden paper values using tolerance windows."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's output artifact. For the scored artifact `vacancy_properties.json`, the verifier reads the submitted `magnetic_moment_mu_B` and `Delta_E_mag_eV` and compares them against the values that a correct execution of the protocol should yield. The comparison uses numeric tolerances that account for the expected differences between DFT codes and implementations; it does not require bit‑identical agreement. Simply reporting a number without running the required calculations is unlikely to succeed, because the tolerances are tight enough to exclude arbitrary guesses. The final reward is a weighted combination of the per‑stage scores. Execute all steps described in the workflow, produce every required output, and ensure the reported values are computed from your own DFT runs.
