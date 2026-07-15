# Aluminium Nanocontact PDOS and Orbital Occupancy Analysis

## Problem background
In metallic nanocontacts, electrical transport is determined by a small number of atomic orbitals at the constriction. For aluminium, the bulk material exhibits strong sp hybridization, but spatial confinement at an atomic-sized neck can disrupt this hybridization and lead to directed bonding and local charge redistribution. This task investigates the electronic structure of an aluminium nanocontact using density functional theory, focusing on the central contact atom. The aim is to determine the orbital occupancy of the 3s and 3p states and the net charge transfer at the contact, and to assess whether sp hybridization is suppressed under confinement.

## Approach
The electronic structure is treated with density functional theory in the local density approximation (LDA). The aluminium nanocontact is modelled as a central Al atom connected to two planar hexagonal Al layers (seven atoms each) in the fcc (111) orientation, with the two central atoms of the layers bonded linearly to the contact atom along the c-axis. The structure is periodic in the ab plane and uses bulk fcc Al bond lengths. A self-consistent DFT calculation is performed using an open-source plane-wave code (Quantum ESPRESSO) with an LDA pseudopotential for Al. From the self-consistent charge density, the projected density of states (PDOS) onto the 3s, 3px, 3py, and 3pz orbitals of the central Al atom is computed. The PDOS is then integrated up to the Fermi level to obtain the number of electrons in each orbital. The net charge transfer is derived as the difference between the nominal valence electron count (3) and the total occupied s+p electrons. The occupation numbers are compared among the orbitals to identify the degree of sp hybridization and the directionality of the bonding.

## Reproduction target
Produce two files under /app/outputs:
- `pdos.csv`: Raw projected density of states for the central Al atom, with columns energy (eV, Fermi level at 0), s, px, py, pz (DOS in states/eV/atom).
- `results.json`: Derived orbital occupancies below the Fermi level (s_occupancy, p_occupancy, pz_occupancy, px_occupancy) and the net charge transfer (net_charge_transfer = 3 – (s_occupancy + p_occupancy), positive for electron loss).
The PDOS must be obtained from a self-consistent DFT calculation on the nanocontact geometry described. The occupancy analysis must integrate the PDOS for energy < 0. The output should reflect the electronic structure of a geometry-constrained aluminium contact, quantifying the occupation distribution between s and p orbitals and the charge loss from the contact site.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotential for aluminium: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Geometry construction and SCF calculation
- Role: process
- Action: Build the aluminium nanocontact geometry (central Al atom connected to two planar hexagonal Al layers of 7 atoms each, in fcc (111) orientation, periodic in ab-plane). Perform a self-consistent DFT calculation using Quantum ESPRESSO with LDA exchange-correlation and an Al LDA pseudopotential, using sufficient k-point sampling to converge the electronic ground state.
- Evidence: `/app/outputs/scf.out`

### Step 2: Compute projected density of states
- Role: scored (load-bearing)
- Action: From the self-consistent charge density, compute the projected density of states (PDOS) for the 3s, 3p_x, 3p_y, 3p_z orbitals of the central Al atom. Output the raw PDOS data to /app/outputs/pdos.csv with columns: energy (eV, relative to Fermi level, set to zero), s, px, py, pz (DOS in states/eV/atom).
- Output file: `/app/outputs/pdos.csv`
- Format: csv
- Contract: CSV with header: energy,s,px,py,pz. energy in eV (float); s, px, py, pz are floats (DOS in states/eV/atom).
- Scoring: scored by hidden verifier

### Step 3: Derive occupancies and charge transfer
- Role: scored
- Action: Read pdos.csv, integrate the PDOS for energy < 0 to obtain the number of electrons in 3s, total 3p, pz, and px orbitals. Compute net_charge_transfer = 3 - (s_occupancy + p_occupancy), positive indicating electron loss. Output these values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: s_occupancy (float), p_occupancy (float), net_charge_transfer (float), pz_occupancy (float), px_occupancy (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pdos.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pdos.csv
- path: `/app/outputs/pdos.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw projected density of states for the central Al atom. The Fermi level must be at energy=0. The checker computes orbital occupancies by integrating below the Fermi level and compares to paper-derived tolerances.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `s`, `px`, `py`, `pz`
  - `units`:
    - `energy`: eV
    - `s`: states/eV/atom
    - `px`: states/eV/atom
    - `py`: states/eV/atom
    - `pz`: states/eV/atom

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Derived orbital occupancies and net charge transfer. The checker uses its own recomputation from pdos.csv to verify self-consistency and, indirectly, the suppression of sp hybridization.
- schema:
  - `type`: object
  - `required`: `s_occupancy`, `p_occupancy`, `net_charge_transfer`, `pz_occupancy`, `px_occupancy`
  - `items`:
    - `s_occupancy`: float (number of 3s electrons below Fermi level)
    - `p_occupancy`: float (total 3p electrons below Fermi level)
    - `net_charge_transfer`: float (electrons lost from the contact site, positive)
    - `pz_occupancy`: float (3p_z electrons below Fermi level)
    - `px_occupancy`: float (3p_x electrons below Fermi level)

Notes: The checker recomputes occupancies from pdos.csv using numerical integration and tolerances derived from the paper's reported quantities (3s occupancy ~70%, charge transfer ~0.6 e). The results.json values serve as a cross-check to ensure the agent performed the analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pdos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "s",
          "px",
          "py",
          "pz"
        ],
        "units": {
          "energy": "eV",
          "s": "states/eV/atom",
          "px": "states/eV/atom",
          "py": "states/eV/atom",
          "pz": "states/eV/atom"
        }
      },
      "description": "Raw projected density of states for the central Al atom. The Fermi level must be at energy=0. The checker computes orbital occupancies by integrating below the Fermi level and compares to paper-derived tolerances."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "s_occupancy",
          "p_occupancy",
          "net_charge_transfer",
          "pz_occupancy",
          "px_occupancy"
        ],
        "items": {
          "s_occupancy": "float (number of 3s electrons below Fermi level)",
          "p_occupancy": "float (total 3p electrons below Fermi level)",
          "net_charge_transfer": "float (electrons lost from the contact site, positive)",
          "pz_occupancy": "float (3p_z electrons below Fermi level)",
          "px_occupancy": "float (3p_x electrons below Fermi level)"
        }
      },
      "description": "Derived orbital occupancies and net charge transfer. The checker uses its own recomputation from pdos.csv to verify self-consistency and, indirectly, the suppression of sp hybridization."
    }
  ],
  "notes": "The checker recomputes occupancies from pdos.csv using numerical integration and tolerances derived from the paper's reported quantities (3s occupancy ~70%, charge transfer ~0.6 e). The results.json values serve as a cross-check to ensure the agent performed the analysis."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines them into the final reward. For the raw PDOS file (pdos.csv), the verifier will integrate the DOS for energy < 0 to compute the orbital occupancies and net charge transfer, and compare these recomputed numbers against hidden reference tolerances. For the derived results file (results.json), the verifier will cross-check the reported occupancies and charge transfer against its own recomputation from the PDOS to ensure consistency. Simply reporting the paper’s numbers is not sufficient; the agent must genuinely perform the DFT calculation and derive the PDOS and occupancies from the computation. The final score reflects both the correctness of the PDOS-derived quantities and the self-consistency of the reported analysis.
