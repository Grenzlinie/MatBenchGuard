# PM3 Lattice Energy Calculation for Carbohydrate Crystals

## Problem background
The PM3 semiempirical quantum‑mechanics method has been applied to evaluate intermolecular hydrogen bonding in condensed carbohydrate systems. To test its accuracy, miniature crystal (minicrystal) models comprising 27 sugar residues are built from published crystal‑structure coordinates. The central residue is embedded in a shell that approximates short‑range crystalline forces. The protocol aims to find a stable minicrystal geometry and extract the lattice energy, which quantifies the net stabilization due to packing and H‑bonding. This task focuses on six small carbohydrate crystals and asks: what PM3 lattice energies result from this protocol?

## Approach
The workflow follows an iterative partial‑optimization‑and‑reconstruction scheme. First, for each carbohydrate, a 27‑residue minicrystal is generated from published atomic coordinates and the space group P2₁2₁2₁ such that one residue sits in the centre of a three‑layered shell. The PM3 Hamiltonian (via an open‑source implementation such as MOPAC, ORCA, or GAMESS) is then used to optimise only the central residue while the 26 shell residues remain frozen. After the central residue is optimised, a new minicrystal is constructed with the updated geometry; this cycle is repeated until the gradient norm (GNORM—the root‑mean‑squared energy derivative) stabilises. The iterative procedure begins with a GNORM termination threshold of 10.0 and is later tightened to 5.0. After geometry convergence, the lattice energy is obtained as the difference between the total PM3 energy of the full minicrystal and the sum of the energies of the isolated central residue and the isolated outer shell.

## Reproduction target
For the following six carbohydrate crystals — α‑D‑glucose, β‑D‑glucose, α‑L‑xylose, β‑L‑arabinose, methyl‑α‑D‑glucopyranoside, and methyl‑α‑D‑mannopyranoside — construct 27‑residue minicrystals from their published crystal‑structure coordinates (available via the cited neutron and X‑ray diffraction studies). Run the iterative PM3 partial‑optimization protocol until the central residue geometry becomes stationary (GNORM thresholds 10.0 then 5.0, no more than about 16 reconstruction cycles unless GNORM exhibits persistent fluctuations). Compute the final lattice energy for each crystal as E_lattice = E_minicrystal − (E_central + E_shell). Write a CSV file `/app/outputs/lattice_energies.csv` with header `crystal, lattice_energy_kcal` and one row per carbohydrate, giving the name and the computed lattice energy in kcal/mol.

## Assets

- Open-source PM3 semiempirical quantum chemistry program: https://github.com/openmopac/mopac
- Crystal structure of α-D-glucose (Brown & Levy, 1979): 10.1107/S0567740879003560
- Crystal structure of β-D-glucose (Chu & Jeffrey, 1968): 10.1107/S0567740868002230
- Crystal structure of α-L-xylose (Jeffrey et al., 1980): 10.1107/S0567740880002813
- Crystal structure of β-L-arabinose (Jeffrey et al., 1980): 10.1107/S0567740880002813
- Crystal structure of methyl-α-D-glucopyranoside (Jeffrey et al., 1977): 10.1107/S0567740877005629
- Crystal structure of methyl-α-D-mannopyranoside (Jeffrey et al., 1977): 10.1107/S0567740877005629

## Workflow steps

### Step 1: Construct 27-residue minicrystal models
- Role: process
- Action: For each of the six carbohydrate crystals (α-D-glucose, β-D-glucose, α-L-xylose, β-L-arabinose, methyl-α-D-glucopyranoside, methyl-α-D-mannopyranoside), build a 27-residue minicrystal from the published atomic coordinates, unit-cell dimensions, and space group P2₁2₁2₁. Assemble three stacked layers so that one central residue is surrounded by 26 residues. If multiple candidate assemblies are possible, select the one with the lowest initial lattice energy.
- Evidence: `/app/outputs/minicrystal_construction.log`

### Step 2: Iterative PM3 optimisation of minicrystals
- Role: process
- Action: For each minicrystal, run the iterative partial-optimisation protocol using the PM3 semiempirical Hamiltonian: (1) Optimise only the central residue with PM3 while the 26 surrounding residues are held fixed. (2) Reconstruct the minicrystal with the optimised central residue. (3) Repeat until the GNORM (RMS of energy derivatives) stabilises. Use GNORM termination thresholds of 10.0 in early runs and 5.0 in later runs. Do not exceed 16 reconstruction cycles unless GNORM is clearly fluctuating; continue until the central residue geometry becomes stationary. Record the total PM3 energy and GNORM at each cycle.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Calculate lattice energies
- Role: scored
- Action: For each optimised minicrystal, compute the lattice energy as E_lattice = E_minicrystal – (E_central + E_shell). Report the results in the output CSV file.
- Output file: `/app/outputs/lattice_energies.csv`
- Format: csv
- Contract: CSV with header: crystal, lattice_energy_kcal. Rows for: α-D-glucose, β-D-glucose, α-L-xylose, β-L-arabinose, methyl-α-D-glucopyranoside, methyl-α-D-mannopyranoside.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.csv
- path: `/app/outputs/lattice_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: PM3 lattice energies for the six carbohydrate minicrystals. Each row names a crystal and gives its computed lattice energy in kcal/mol.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `lattice_energy_kcal`
  - `units`:
    - `lattice_energy_kcal`: kcal/mol

Notes: Only the lattice energy results are scored. The checker compares each submitted lattice_energy_kcal against the paper-reported values with an appropriate tolerance. The optimization evidence files are optional and not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "lattice_energy_kcal"
        ],
        "units": {
          "lattice_energy_kcal": "kcal/mol"
        }
      },
      "description": "PM3 lattice energies for the six carbohydrate minicrystals. Each row names a crystal and gives its computed lattice energy in kcal/mol."
    }
  ],
  "notes": "Only the lattice energy results are scored. The checker compares each submitted lattice_energy_kcal against the paper-reported values with an appropriate tolerance. The optimization evidence files are optional and not scored."
}
```

## How you are scored
A hidden verifier scores each workflow stage independently and combines the scores into the final reward. The primary scored artifact is `/app/outputs/lattice_energies.csv`. The verifier compares each lattice energy against a hidden reference and awards credit based on agreement. Optional process evidence, such as an optimization log, may also be inspected for procedural consistency and contributes a smaller weight to the overall reward. Stating paper‑reported numbers without executing the protocol will not earn full credit; the verifier requires the computation to be performed as described.
