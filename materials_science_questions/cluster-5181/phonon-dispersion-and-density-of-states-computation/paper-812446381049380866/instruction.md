# RHF Cluster Calculations of Oxygen Adsorption on Cu(110)

## Problem background
The low-temperature adsorption of oxygen on Cu(110) has been controversial: some experiments suggest molecular chemisorption while others indicate dissociative adsorption. This study uses self-consistent restricted Hartree–Fock (RHF) total-energy calculations on a Cu12 cluster to compare molecular and atomic oxygen adsorption, with the aim of determining which adsorption mechanism is energetically favoured.

## Approach
A fixed 12-atom copper cluster representing the unreconstructed Cu(110) surface is built using the bulk fcc lattice constant (3.61 Å). The GAMESS quantum chemistry package is used to perform RHF calculations with Gaussian basis sets taken from the Huzinaga library. For molecular O₂ (bond length 1.208 Å), a series of single-point energies is computed at different adsorbate–surface distances above a high-symmetry site to check for the existence of a bound state. For atomic oxygen, geometry relaxations of the oxygen height are performed at four high-symmetry surface sites (long bridge, short bridge, atop first-layer Cu, atop second-layer Cu) while keeping the metal cluster rigid. The most stable site is identified and used to compute the harmonic Cu–O vertical vibrational mode by displacing the oxygen atom and evaluating the resulting energy change (frozen-phonon approximation).

## Reproduction target
Produce three scored artifacts:
(1) A CSV file listing total energies for molecular O₂ at distances 1.5, 2.0, 2.5, 3.0, and 3.5 Å above the atop first-layer site; verify that no local energy minimum exists (monotonic increase with decreasing distance).
(2) A CSV file reporting the relative total energies of atomic oxygen at the long-bridge, short-bridge, atop first-layer, and atop second-layer sites, with the long-bridge site taken as the zero reference.
(3) A text file containing the harmonic vibrational energy (in meV) of the Cu–O stretch for oxygen in the long-bridge site.

## Assets

- GAMESS quantum chemistry package: https://www.msg.chem.iastate.edu/gamess/
- Huzinaga Gaussian basis sets: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Build Cu12 cluster model
- Role: process
- Action: Construct the Cartesian coordinates of an unrelaxed 12‑atom Cu cluster representing the Cu(110) surface. Use the bulk Cu fcc lattice constant (3.61 Å) and the (110) surface termination geometry. The atomic positions are kept fixed.
- Evidence: `/app/outputs/cu12_cluster.xyz`

### Step 2: Molecular O₂ adsorption energy scan
- Role: scored
- Action: Perform RHF single‑point energy calculations with GAMESS and Huzinaga basis sets for intact O₂ (O–O bond length fixed at 1.208 Å, axis parallel to the surface) placed above the atop‑first‑layer Cu site. Sample surface–adsorbate distances of 1.5, 2.0, 2.5, 3.0, and 3.5 Å. Output the distance and total energy for each point.
- Output file: `/app/outputs/molecular_O2_adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: distance_angstrom (float), total_energy_hartree (float). Rows sorted by distance ascending.
- Scoring: scored by hidden verifier

### Step 3: Atomic oxygen adsorption relative energies
- Role: scored (load-bearing)
- Action: For each of the four high‑symmetry sites (long bridge, short bridge, atop first layer, atop second layer), perform RHF geometry relaxation of the oxygen‑surface distance while keeping the Cu atoms fixed. For the atop‑second‑layer site, fix the O distances at 1.7 Å to the second‑layer Cu and 2.0 Å to the first‑layer Cu. Report the relative total energy of each site with respect to the long‑bridge site.
- Output file: `/app/outputs/atomic_adsorption_relative_energies.csv`
- Format: csv
- Contract: CSV with columns: site (string), relative_energy_eV (float). Rows: long_bridge, short_bridge, atop_first_layer, atop_second_layer. Long‑bridge relative energy must be 0.0 eV.
- Scoring: scored by hidden verifier

### Step 4: Cu–O vibrational frequency
- Role: scored
- Action: Using the equilibrium geometry of atomic oxygen at the long‑bridge site obtained in step 3, compute the harmonic vibrational energy of the vertical Cu–O mode by displacing the oxygen atom vertically about the equilibrium position while keeping the Cu atoms rigid. Report the energy in meV.
- Output file: `/app/outputs/vibrational_frequency_meV.txt`
- Format: txt
- Contract: A single numeric value (float) in meV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/molecular_O2_adsorption_energies.csv`
- `/app/outputs/atomic_adsorption_relative_energies.csv`
- `/app/outputs/vibrational_frequency_meV.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### molecular_O2_adsorption_energies.csv
- path: `/app/outputs/molecular_O2_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energies for molecular O2 adsorption at several distances. The checker will verify a monotonic increase as distance decreases, indicating no bound state.
- schema:
  - `type`: table
  - `required_columns`: `distance_angstrom`, `total_energy_hartree`
  - `units`:
    - `distance_angstrom`: angstrom
    - `total_energy_hartree`: hartree

### atomic_adsorption_relative_energies.csv
- path: `/app/outputs/atomic_adsorption_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Relative adsorption energies of atomic oxygen at high‑symmetry sites. Each value is compared to a hidden reference with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `site`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

### vibrational_frequency_meV.txt
- path: `/app/outputs/vibrational_frequency_meV.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Harmonic vibrational energy of the Cu–O mode on the long‑bridge site. Compared to a hidden reference with tolerance.
- schema:
  - `type`: text
  - `units`:
    - `value`: meV

Notes: All gold values and tolerances are hidden; the instruction only requires the agent to compute and report the quantities. The molecular scan is scored by structural audit (monotonicity); atomic relative energies and vibrational frequency are scored by threshold_or_better against the paper's reported numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "molecular_O2_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_angstrom",
          "total_energy_hartree"
        ],
        "units": {
          "distance_angstrom": "angstrom",
          "total_energy_hartree": "hartree"
        }
      },
      "description": "Total energies for molecular O2 adsorption at several distances. The checker will verify a monotonic increase as distance decreases, indicating no bound state."
    },
    {
      "file": "atomic_adsorption_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "relative_energy_eV"
        ],
        "units": {
          "relative_energy_eV": "eV"
        }
      },
      "description": "Relative adsorption energies of atomic oxygen at high‑symmetry sites. Each value is compared to a hidden reference with tolerance."
    },
    {
      "file": "vibrational_frequency_meV.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": {
          "value": "meV"
        }
      },
      "description": "Harmonic vibrational energy of the Cu–O mode on the long‑bridge site. Compared to a hidden reference with tolerance."
    }
  ],
  "notes": "All gold values and tolerances are hidden; the instruction only requires the agent to compute and report the quantities. The molecular scan is scored by structural audit (monotonicity); atomic relative energies and vibrational frequency are scored by threshold_or_better against the paper's reported numbers."
}
```

## How you are scored
Each output file is evaluated automatically by a hidden verifier. For artifact (1), the verifier inspects the energy trend to confirm that there is no local minimum (energies must increase as distance decreases). For artifact (2), each relative energy is compared to a hidden set of reference values; if the computed energy differences are within the allowed tolerance, full credit is awarded. For artifact (3), the reported meV value is compared to a hidden reference, and closeness within tolerance yields credit. The three artifacts contribute with predefined weights to a final reward between 0 and 1. Your goal is to compute these quantities from the described setup rather than to guess the paper’s numbers; the verifier checks the scientific output of your calculations.
