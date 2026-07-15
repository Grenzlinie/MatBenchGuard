# Cluster expansion thermodynamics of Pd-Ru-Te phases

## Problem background
In spent nuclear fuel, the noble metal phase (NMP) particles containing Mo-Tc-Ru-Rh-Pd have long been considered a single metallic alloy. Recent microscopy observations suggest that within these particles, a separate Pd-rich telluride phase can coexist with a Ru-rich metallic phase when tellurium is present. This reproduction focuses on the first-principles thermodynamic analysis that assesses whether Ru can substitute into the PdTe and Pd20Te7 telluride phases, and conversely Pd into the hcp Ru-rich phase, to understand the driving force for phase separation. The computational task is to compute the formation energies of these pseudobinary systems over a wide composition range, fit a cluster expansion model, and determine the equilibrium solubility limits at 1000 K.

## Approach
The thermodynamic analysis uses the cluster expansion formalism, where the energy of any atomic configuration on a fixed crystal lattice is expressed as a linear combination of cluster correlation functions and effective cluster interaction (ECI) coefficients. The workflow is: (1) Generate ordered supercell structures for the hcp, fcc, PdTe, and Pd20Te7 crystal systems, covering the full Ru composition range (0–100%) for the first three, and up to ~10% Ru for Pd20Te7. (2) Compute the total energy of each structure via plane-wave density functional theory (DFT) using the PBE functional and open-source tools, obtaining formation energies per atom relative to pure reference states. (3) Fit the ECI parameters by linear regression of formation energies against cluster correlation functions; for Pd20Te7, only the null and point clusters are used due to the limited composition range. (4) Using the fitted ECI, construct the disordered formation energy as a function of composition, add the ideal configurational entropy, and minimize the free energy at T = 1000 K to obtain the equilibrium Ru mole fraction in (Pd,Ru)Te and (Pd,Ru)20Te7 and the equilibrium Pd mole fraction in hcp metal.

## Reproduction target
Your task is to produce three artifacts:
1. formation_energies.csv: a table of DFT formation energies for all training structures (phase, Ru composition, formation energy in eV/atom).
2. cluster_expansion_coefficients.json: fitted ECI coefficients (J0–J3 where applicable) for each of the four crystal systems.
3. solubility_results.json: the equilibrium atomic fractions of Ru in (Pd,Ru)Te and (Pd,Ru)20Te7 and Pd in hcp metal at 1000 K, computed from the cluster expansion and free-energy minimization.
The results must reflect the full pipeline—from structure enumeration through DFT to solubility—using only public tools and crystal structure data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ATAT (Alloy Theoretic Automated Toolkit): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- QE pseudopotential library: https://pseudopotentials.quantum-espresso.org/
- Crystal structure data for PdTe and Pd20Te7: Kjekshus & Pearson (1965), Wopersnow & Schubert (1977)

## Workflow steps

### Step 1: Generate DFT training structures
- Role: process
- Action: Generate ordered supercells spanning the full composition range of the Pd–Ru pseudobinary sublattice for hcp, fcc, PdTe, and Pd20Te7 crystal systems using a structure-enumeration tool (e.g., ATAT or equivalent). For hcp, fcc, and PdTe, include structures from 0 to 100% Ru on the Pd/Ru sublattice (~50 each). For Pd20Te7, include structures with 0 to ~10% Ru. Write the list of generated structures to a log file.
- Evidence: `/app/outputs/training_structures.log`

### Step 2: Perform DFT formation-energy calculations
- Role: scored
- Action: Compute total energies for all generated training structures using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with the PBE functional and appropriate pseudopotentials for Pd, Ru, and Te. Use convergence parameters sufficient to achieve energy convergence better than 1 meV/atom. Relax ionic positions and cell parameters until forces are below 5 meV/Å. For each structure, obtain the formation energy per atom relative to the pure reference states (hcp Ru, fcc Pd, Te in its standard state). Output all computed formation energies to a CSV file.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: phase (string: 'hcp','fcc','PdTe','Pd20Te7'), composition (float, mole fraction of Ru on the Pd–Ru sublattice), formation_energy (float, eV/atom). One row per relaxed structure.
- Scoring: scored by hidden verifier

### Step 3: Fit cluster expansion effective cluster interactions
- Role: scored
- Action: Using the computed DFT formation energies, fit effective cluster interaction (ECI) parameters for each crystal phase (hcp, fcc, PdTe, Pd20Te7) by linear regression against cluster correlation functions defined by the lattice topology (cluster expansion). For Pd20Te7, restrict fitting to x_Ru ≤ 0.1 and use only the null and point clusters. Output the fitted coefficients in a JSON file.
- Output file: `/app/outputs/cluster_expansion_coefficients.json`
- Format: json
- Contract: JSON object with keys 'hcp','fcc','PdTe','Pd20Te7'. Each value is an object containing the fitted coefficients: J0, J1, J2, J3 (J2, J3 only for hcp, fcc, PdTe) in eV/atom.
- Scoring: scored by hidden verifier

### Step 4: Compute free-energy minima and solubility limits
- Role: scored (load-bearing)
- Action: From the fitted ECI, construct the disordered formation energy as a function of Ru composition for each phase using the cluster expansion model. Add the ideal configurational entropy term and minimize the free energy at T=1000 K to find the equilibrium Ru mole fraction on the transition-metal sublattice for (Pd,Ru)Te and (Pd,Ru)20Te7, and the equilibrium Pd mole fraction in hcp metal. Output the three equilibrium fractions.
- Output file: `/app/outputs/solubility_results.json`
- Format: json
- Contract: JSON object with keys: 'Ru_in_PdTe_1000K' (float, atomic fraction of Ru in (Pd,Ru)Te), 'Ru_in_Pd20Te7_1000K' (float), 'Pd_in_hcp_1000K' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/cluster_expansion_coefficients.json`
- `/app/outputs/solubility_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: DFT formation energies; checked for structural trends (positive, monotonically increasing with Ru in PdTe).
- schema:
  - `type`: table
  - `required_columns`: `phase`, `composition`, `formation_energy`
  - `units`:
    - `formation_energy`: eV/atom

### cluster_expansion_coefficients.json
- path: `/app/outputs/cluster_expansion_coefficients.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Fitted ECI coefficients; checker will recompute formation energies from these coefficients and verify R² > 0.9 against submitted formation energies.
- schema:
  - `type`: object
  - `required`: `hcp`, `fcc`, `PdTe`, `Pd20Te7`

### solubility_results.json
- path: `/app/outputs/solubility_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Equilibrium solubilities at 1000 K; checker will verify that Ru concentration in PdTe is below 1 at.% and recompute concentrations from the submitted ECI to validate consistency.
- schema:
  - `type`: object
  - `required`: `Ru_in_PdTe_1000K`, `Ru_in_Pd20Te7_1000K`, `Pd_in_hcp_1000K`

Notes: The workflow reproduces the paper's cluster expansion thermodynamic analysis using public tools. No proprietary data or software is required. The checkers use structural trends and recomputed consistency, not exact numerical matching to the paper's original VASP values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "composition",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV/atom"
        }
      },
      "description": "DFT formation energies; checked for structural trends (positive, monotonically increasing with Ru in PdTe)."
    },
    {
      "file": "cluster_expansion_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "hcp",
          "fcc",
          "PdTe",
          "Pd20Te7"
        ]
      },
      "description": "Fitted ECI coefficients; checker will recompute formation energies from these coefficients and verify R² > 0.9 against submitted formation energies."
    },
    {
      "file": "solubility_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "Ru_in_PdTe_1000K",
          "Ru_in_Pd20Te7_1000K",
          "Pd_in_hcp_1000K"
        ]
      },
      "description": "Equilibrium solubilities at 1000 K; checker will verify that Ru concentration in PdTe is below 1 at.% and recompute concentrations from the submitted ECI to validate consistency."
    }
  ],
  "notes": "The workflow reproduces the paper's cluster expansion thermodynamic analysis using public tools. No proprietary data or software is required. The checkers use structural trends and recomputed consistency, not exact numerical matching to the paper's original VASP values."
}
```

## How you are scored
A hidden verifier independently scores each of the three scored artifacts and combines them by weight into a final reward. For formation_energies.csv, it checks structural trends: the formation energy for PdTe must be positive and increase with Ru composition. For cluster_expansion_coefficients.json, it recomputes formation energies from your coefficients and checks R² > 0.9 against your submitted energies. For solubility_results.json, it recomputes the equilibrium concentrations from your ECI and verifies that the Ru concentration in (Pd,Ru)Te is consistent with the paper-reported hypothesis (below a very small critical threshold). No numeric target values are provided; the verifier uses hidden tolerances derived from the paper's published result.
