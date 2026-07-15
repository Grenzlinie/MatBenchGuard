# DFT binding energy and electronic structure of iron-nitride/carbide phases

## Problem background
Ion implantation of nitrogen or carbon into pure iron is known to increase surface hardness and modify wear behavior. However, traditional hardening mechanisms (solid-solution strengthening, dislocation pinning, dispersion hardening) do not fully explain the observed effects, especially the difference between reactive species (N, C) and inert species (Ne, Ar). This work focuses on the micro-mechanism of hardening by studying the bonding between implanted ions and iron atoms in various iron-nitride and iron-carbide phases that form during implantation. The task is to compute binding energies and orbital/overlap populations for representative clusters of these phases, to investigate how bonding changes across phases and whether covalent bonding plays a role.

## Approach
We model the iron‑nitride and iron‑carbide phases as small atomic clusters cut from the known bulk crystal structures. Using an open‑source plane‑wave DFT code with a GGA functional and appropriate pseudopotentials, we perform spin‑polarised total energy calculations for each cluster. The binding energy of a cluster is obtained as the difference between its total energy and the sum of energies of the isolated constituent atoms, computed under the same DFT settings. In addition, for the γ‑Fe₆ and γ′-Fe₆N clusters we compute atomic orbital populations and overlap populations between N (or C) and Fe orbitals, to quantify the extent of covalent bonding. The computed binding energies and orbital populations are then compared across the different phases to reveal trends.

## Reproduction target
Compute and report:
- Binding energies (eV) for nine clusters: α-Fe₆, α′-Fe₆N, α′-Fe₆C, γ′-Fe₆N, γ′-Fe₆C, ε′-Fe₆N (representing Fe₃N), ε′-Fe₆N (representing Fe₂N), ε′-Fe₆C (representing Fe₃C), and ε′-Fe₆C (representing Fe₂C).
- Orbital populations for the γ-Fe₆ cluster and the γ′-Fe₆N cluster, and the N–Fe overlap populations for the γ′-Fe₆N cluster.

Using these results, determine:
(a) whether all nitride and carbide phases exhibit higher binding energy than pure iron,
(b) what the relative ordering of binding energies among the phases is, and
(c) whether a significant covalent bond exists between N and Fe, as indicated by a large total overlap population.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (or Pslibrary): https://www.materialscloud.org/discover/sssp/
- Atomic Simulation Environment (ASE): ase
- Materials Project: https://next-gen.materialsproject.org/

## Workflow steps

### Step 1: Build cluster geometries
- Role: process
- Action: Construct the 3D geometries of nine clusters: α-Fe6, α'-Fe6N, α'-Fe6C, γ-Fe6, γ'-Fe6N, γ'-Fe6C, ε'-Fe6N (for both Fe3N and Fe2N compositions), and ε'-Fe6C (for both Fe3C and Fe2C compositions). Use lattice parameters and atomic positions from public crystallographic databases (e.g., Materials Project, ICSD) for the corresponding bulk phases. Cut clusters from bulk and terminate appropriately. Write the atomic coordinates to a text file for later use.
- Evidence: `/app/outputs/cluster_geometries.txt`

### Step 2: Compute orbital populations and overlap populations
- Role: scored
- Action: Perform spin-polarized DFT calculations on the γ-Fe6 and γ'-Fe6N clusters (e.g., using Quantum ESPRESSO with a GGA functional) to obtain Löwdin or Mulliken atomic orbital populations and overlap populations between N and Fe orbitals. Report the populations as a JSON object with three keys: 'gamma_Fe6_orbital_population' (containing Fe 3d, 4s, 4p populations), 'gamma_prime_Fe6N_orbital_population' (containing N 2s, 2p and Fe 3s, 3p, 3d, 4s, 4p populations), and 'N_Fe_overlap_population' (containing N-Fe 3s, 3p, 3d, 4s, 4p and total overlap populations). All values are floats.
- Output file: `/app/outputs/orbital_populations.json`
- Format: json
- Contract: Keys: 'gamma_Fe6_orbital_population' (object with Fe_3d, Fe_4s, Fe_4p), 'gamma_prime_Fe6N_orbital_population' (object with N_2s, N_2p, Fe_3s, Fe_3p, Fe_3d, Fe_4s, Fe_4p), 'N_Fe_overlap_population' (object with N_Fe_3s, N_Fe_3p, N_Fe_3d, N_Fe_4s, N_Fe_4p, N_Fe_total).
- Scoring: scored by hidden verifier

### Step 3: Compute binding energies
- Role: scored (load-bearing)
- Action: Perform DFT total energy calculations on all nine clusters: α-Fe6, α'-Fe6N, α'-Fe6C, γ'-Fe6N, γ'-Fe6C, ε'-Fe6N (Fe3N), ε'-Fe6N (Fe2N), ε'-Fe6C (Fe3C), ε'-Fe6C (Fe2C). Compute the isolated atom energies for Fe, N, C consistently. For each cluster, binding energy = cluster total energy - sum of isolated atom energies. Output a CSV file with columns phase (string), cluster (string), binding_energy (float, eV). The file must contain exactly 9 rows, one per phase/cluster combination.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Columns: phase (str), cluster (str), binding_energy (float, eV). Must contain exactly 9 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/orbital_populations.json`
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### orbital_populations.json
- path: `/app/outputs/orbital_populations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed orbital populations for γ-Fe6 and γ'-Fe6N, and N-Fe overlap populations, used to verify covalent bonding and quantitative agreement with reported values.
- schema:
  - `type`: object
  - `required`: `gamma_Fe6_orbital_population`, `gamma_prime_Fe6N_orbital_population`, `N_Fe_overlap_population`
  - `properties`:
    - `gamma_Fe6_orbital_population`:
      - `type`: object
      - `required`: `Fe_3d`, `Fe_4s`, `Fe_4p`
    - `gamma_prime_Fe6N_orbital_population`:
      - `type`: object
      - `required`: `N_2s`, `N_2p`, `Fe_3s`, `Fe_3p`, `Fe_3d`, `Fe_4s`, `Fe_4p`
    - `N_Fe_overlap_population`:
      - `type`: object
      - `required`: `N_Fe_3s`, `N_Fe_3p`, `N_Fe_3d`, `N_Fe_4s`, `N_Fe_4p`, `N_Fe_total`

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energies of the nine clusters, used to confirm that all nitride/carbide phases have higher binding energy than pure iron and follow the reported trend.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `cluster`, `binding_energy`
  - `units`:
    - `binding_energy`: eV

Notes: The hidden checker will verify the total N-Fe overlap population > 0.5 (covalent bond) and compare individual populations within tolerance. For binding energies, it will check that all Fe-N and Fe-C phases exceed α-Fe binding energy and follow the ordering trends from the paper's Table 2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "orbital_populations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma_Fe6_orbital_population",
          "gamma_prime_Fe6N_orbital_population",
          "N_Fe_overlap_population"
        ],
        "properties": {
          "gamma_Fe6_orbital_population": {
            "type": "object",
            "required": [
              "Fe_3d",
              "Fe_4s",
              "Fe_4p"
            ]
          },
          "gamma_prime_Fe6N_orbital_population": {
            "type": "object",
            "required": [
              "N_2s",
              "N_2p",
              "Fe_3s",
              "Fe_3p",
              "Fe_3d",
              "Fe_4s",
              "Fe_4p"
            ]
          },
          "N_Fe_overlap_population": {
            "type": "object",
            "required": [
              "N_Fe_3s",
              "N_Fe_3p",
              "N_Fe_3d",
              "N_Fe_4s",
              "N_Fe_4p",
              "N_Fe_total"
            ]
          }
        }
      },
      "description": "Computed orbital populations for γ-Fe6 and γ'-Fe6N, and N-Fe overlap populations, used to verify covalent bonding and quantitative agreement with reported values."
    },
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "cluster",
          "binding_energy"
        ],
        "units": {
          "binding_energy": "eV"
        }
      },
      "description": "Binding energies of the nine clusters, used to confirm that all nitride/carbide phases have higher binding energy than pure iron and follow the reported trend."
    }
  ],
  "notes": "The hidden checker will verify the total N-Fe overlap population > 0.5 (covalent bond) and compare individual populations within tolerance. For binding energies, it will check that all Fe-N and Fe-C phases exceed α-Fe binding energy and follow the ordering trends from the paper's Table 2."
}
```

## How you are scored
Your outputs will be evaluated by a hidden verifier. Each scored artifact is checked independently, and a weighted combination of the scores gives the final reward. The verifier will compare your computed binding energies to the expected trend (all nitride/carbide phases must have higher binding energy than pure iron, and there is a specific ordering among the phases). It will also check that the total N‑Fe overlap population exceeds a threshold indicative of covalent bonding. Quantitative comparisons may be performed within generous tolerances to accommodate differences in DFT implementations. Simply reporting numbers without correct physical trends will not earn full credit.
