# Calculation of vertical excitation energies for TiO2 ring structures using DFT and configuration interaction

## Problem background
Titanium dioxide nanoparticles are widely studied for photocatalysis and solar energy conversion because their electronic bandgap can shift with particle size—a quantum size effect that alters light absorption and charge dynamics. A central open question is whether the lowest excited states of these particles are best described as delocalized across the structure or as localized electron–hole pairs (excitons). Resolving this is important because localization can dramatically affect excitation energies, carrier lifetimes, and subsequent chemical reactivity. The present task investigates a series of perfect ring structures, (TiO2)2n with n = 3–9, using ab initio many-electron theory. The goal is to determine vertical excitation energies for different spatial locations of the oxygen hole and to assess whether a localized electron–hole description yields significantly lower energy than a delocalized, symmetry-constrained description.

## Approach
The computational approach follows a two-stage strategy: geometry determination and subsequent excited-state calculations. First, the ground-state geometries of each (TiO2)2n ring are optimised by restricted Hartree–Fock (RHF) with a double-zeta quality Gaussian basis set and an effective core potential (ECP) that replaces the Ti 1s–2p core. Titanium nuclei are constrained coplanar and equally spaced; oxygen positions are fully relaxed. The adequacy of the RHF geometries is validated by a configuration interaction (CI) geometry relaxation for a representative small ring.

Excited states are obtained from restricted open-shell RHF (ROHF) followed by multireference CI expansions. For each ring size, three distinct oxygen hole locations are considered: out-of-plane, in-plane/outside the Ti ring, and in-plane/inside. Two orbital descriptions are explored: a delocalised (symmetry-constrained) picture and a localised (symmetry-broken) picture that allows an electron–hole pair to form on a single Ti–O unit. The CI wavefunctions correlate a fixed number of electrons in a localised orbital space to ensure a consistent treatment across all ring sizes. The calculations yield vertical (Franck–Condon) excitation energies for the lowest triplet and singlet states of each hole type. The isolated TiO2 molecule is also computed as a reference monomer. All computations are performed with an open-source quantum chemistry package that supports RHF, ROHF, CI methods, and ECPs.

## Reproduction target
Produce the file `/app/outputs/excitation_energies.csv` containing the vertical excitation energies (in eV) for:
- the isolated TiO2 molecule (no hole location);
- all ring sizes n = 3–9, each with the three hole locations (out-of-plane, in-plane/outside, in-plane/inside) and for both triplet and singlet spin states;
- the delocalised triplet state of (TiO2)8.

The CSV must have columns: `system` (e.g. `TiO2`, `(TiO2)_6`), `hole_location` (`none`, `out-of-plane`, `in-plane/outside`, `in-plane/inside`, `delocalized`), `spin_state` (`triplet`, `singlet`), and `excitation_energy_eV` (float). The final verifier will compare your reported energies to the paper’s published reference values and will also check internal consistency: excitation energies should increase monotonically with ring size for each hole location and spin state, singlet energies must be higher than triplet energies for every entry, and for (TiO2)8 the localised triplet excitation energy must be lower than the delocalised triplet excitation energy.

## Assets

- Open-source quantum chemistry package (e.g., PySCF, Psi4, NWChem): https://pyscf.org
- Gaussian basis set and effective core potential for Ti: https://www.basissetexchange.org

## Workflow steps

### Step 1: RHF geometry optimisation of (TiO2)2n rings
- Role: process
- Action: Using RHF with a suitable basis set and effective core potential, optimise the geometry of (TiO2)2n ring structures for n=3–9. Titanium nuclei are constrained coplanar and equally spaced; oxygen positions are fully relaxed. Generate equilibrium coordinates for use in subsequent excited‑state calculations.
- Evidence: `/app/outputs/optimized_ring_geometries.xyz`

### Step 2: CI geometry validation for (TiO2)6
- Role: process
- Action: Perform a configuration‑interaction energy minimisation for the smallest ring (TiO2)6 and compare the resulting ring radius and O–O distances with those from the RHF optimisation to validate that RHF geometries are adequate.
- Evidence: `/app/outputs/validation_comparison.csv`

### Step 3: TiO2 monomer reference calculation
- Role: process
- Action: Compute RHF total energy and CI vertical excitation energies (triplet and singlet) for the isolated TiO2 molecule using the same basis set and correlation treatment as for the rings. This provides the baseline molecular benchmark required for Table I.
- Evidence: `/app/outputs/tio2_monomer_energies.json`

### Step 4: Multireference CI calculations for ring excited states
- Role: process
- Action: For each optimised ring geometry, perform restricted open‑shell Hartree‑Fock (ROHF) followed by a multireference configuration‑interaction expansion (or an equivalent method such as CASCI/RASCI) to obtain vertical excitation energies. Carry out calculations for both the delocalised (symmetry‑constrained) and localised (symmetry‑broken) orbital descriptions. For each ring size, compute the three hole types—out‑of‑plane, in‑plane/outside, in‑plane/inside—for both triplet and singlet states. Additionally calculate the delocalised triplet state for (TiO2)8 to enable the energy‑lowering comparison.
- Evidence: `/app/outputs/ci_ring_raw_energies.json`

### Step 5: Compile excitation energies and energy lowering
- Role: scored (load-bearing)
- Action: Collect all computed vertical excitation energies into a single CSV file. Include the isolated TiO2 molecule, all ring sizes (n=3–9) with the three hole locations, and the delocalised triplet state of (TiO2)8. Report all energies in eV.
- Output file: `/app/outputs/excitation_energies.csv`
- Format: csv
- Contract: Columns: system (e.g., 'TiO2', '(TiO2)_6', ...), hole_location ('none', 'out-of-plane', 'in-plane/outside', 'in-plane/inside', 'delocalized'), spin_state ('triplet', 'singlet'), excitation_energy_eV (float). The '(TiO2)_8' delocalised triplet row enables the checker to compute the energy difference (localised triplet minus delocalised triplet) and verify it exceeds 1 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/excitation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### excitation_energies.csv
- path: `/app/outputs/excitation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV of computed vertical excitation energies. The checker compares each row's energy against a hidden paper‑derived reference with tolerance and verifies trends (monotonic increase with ring size, singlet energy > triplet energy) and the energy‑lowering threshold for (TiO2)8.
- schema:
  - `type`: table
  - `required_columns`: `system`, `hole_location`, `spin_state`, `excitation_energy_eV`
  - `units`:
    - `excitation_energy_eV`: eV

Notes: The task reproduces the main quantifiable claim from Table I of the source paper: vertical excitation energies for three hole locations and the localized‑vs‑delocalized energy difference. The molecule TiO2 row and the delocalised (TiO2)8 triplet are included in the same CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "excitation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "hole_location",
          "spin_state",
          "excitation_energy_eV"
        ],
        "units": {
          "excitation_energy_eV": "eV"
        }
      },
      "description": "CSV of computed vertical excitation energies. The checker compares each row's energy against a hidden paper‑derived reference with tolerance and verifies trends (monotonic increase with ring size, singlet energy > triplet energy) and the energy‑lowering threshold for (TiO2)8."
    }
  ],
  "notes": "The task reproduces the main quantifiable claim from Table I of the source paper: vertical excitation energies for three hole locations and the localized‑vs‑delocalized energy difference. The molecule TiO2 row and the delocalised (TiO2)8 triplet are included in the same CSV."
}
```

## How you are scored
A hidden verifier independently evaluates your submission by reading `/app/outputs/excitation_energies.csv`. It compares each numerical entry to the paper’s hidden reference values using an appropriate tolerance; meeting or beating the tolerance earns full credit for that comparison, and the reward decreases as the deviation grows. The verifier also checks structural trends: monotonic increase of excitation energy with ring size for each hole/spin combination, the condition that every singlet energy exceeds the corresponding triplet energy, and that for (TiO2)8 the localised triplet excitation energy is lower than the delocalised triplet excitation energy. Each of these checks carries a fraction of the total weight, with the numerical comparison carrying the largest share. The final reward is a single float in [0,1] written to the output log.
