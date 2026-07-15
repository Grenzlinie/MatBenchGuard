# Defect formation energies of Ti substitution in layered cobaltate approximant cells using DFT+U

## Problem background
Ca3Co4O9 (CCO) is a layered thermoelectric oxide with a high Seebeck coefficient. The material consists of alternating rocksalt-type Ca2CoO3 layers and CdI2-type CoO2 layers, stacked incommensurately along the c-axis. Titanium doping has been explored as a way to modify the carrier concentration and improve thermoelectric performance, but the atomic-scale location of the Ti dopant and its effect on the electronic structure remain unclear. Density functional theory (DFT) calculations can provide insight by determining the relative stability of Ti substitution at different crystallographic sites (Co sites in the rocksalt subsystem, Co sites in the CoO2 subsystem, and Ca sites) and by analyzing the resulting electronic structure. Computing the defect formation energies for these substitution scenarios quantifies which sites are thermodynamically favored and helps explain the observed transport properties.

## Approach
First-principles calculations are performed within the PBE+U framework, where an onsite Hubbard U correction is applied to Co to account for moderate electronic correlations. The incommensurate CCO structure is modeled using two rational approximant unit cells: a 5/3 approximant ([Ca2CoO3]6[CoO2]10, 66 atoms) and a 3/2 approximant ([Ca2CoO3]4[CoO2]6, 36 atoms), whose atomic positions are taken from a published structural model. The chemical potentials of Ti, Co, Ca, and O are determined by enforcing equilibrium with bulk CCO and by avoiding precipitation of secondary phases (CaO, CoO, Co3O4, Ti oxides, CaTiO3, etc.), identifying the Ti-rich point where the Ti chemical potential is maximized within the stability region. Total energies of the pristine and Ti-substituted structures are obtained after geometry optimization, and defect formation energies are computed using the formula E_f = E_doped − E_pristine − Σ ν_i μ_i, where ν_i are stoichiometric coefficients and μ_i the chemical potentials. The formation energies for Ti substituting Co in the rocksalt subsystem, Co in the CoO2 subsystem, and Ca are averaged over inequivalent sites and reported for both approximant cells. Projected density of states (PDOS) is calculated for the relaxed doped structures to analyze the occupancy of Ti 3d and Co 3d orbitals and to infer their valence states.

## Reproduction target
Compute, using DFT with the PBE+U functional, the defect formation energies (in eV) for Ti substitution at Co sites in the rocksalt (RS) subsystem, at Co sites in the CoO2 subsystem, and at Ca sites, for both the 5/3 and 3/2 approximant unit cells of CCO. The calculations must be performed at the Ti-rich chemical potential point. The six averaged formation energies must be written to `/app/outputs/formation_energies.json`, structured as:

{
  "5/3": {
    "Ti_Co_RS": <number>,
    "Ti_Co_CoO2": <number>,
    "Ti_Ca": <number>
  },
  "3/2": {
    "Ti_Co_RS": <number>,
    "Ti_Co_CoO2": <number>,
    "Ti_Ca": <number>
  }
}

## Assets

- Quantum ESPRESSO (or other open-source plane-wave DFT code supporting PBE+U): https://www.quantum-espresso.org
- Rébola et al. Phys. Rev. B 85, 155132 (2012) — CCO approximant structures: https://doi.org/10.1103/PhysRevB.85.155132
- PseudoDojo pseudopotentials (PBE) for Ti, Co, Ca, O: http://www.pseudo-dojo.org
- Materials Project / OQMD — formation energies of bulk competing phases: https://materialsproject.org

## Workflow steps

### Step 1: Build CCO approximant structural models
- Role: process
- Action: Construct the atomic coordinates for the 5/3 approximant ([Ca2CoO3]6[CoO2]10, 66 atoms) and the 3/2 approximant ([Ca2CoO3]4[CoO2]6, 36 atoms) of Ca3Co4O9 based on the published structural model from Rébola et al. (2012). These serve as the pristine unit cells for all subsequent calculations.
- Evidence: `/app/outputs/cco_structures.log`

### Step 2: Determine chemical potential boundaries
- Role: process
- Action: Compute the allowed ranges for the chemical potentials of Ti, Co, Ca, and O by enforcing equilibrium with bulk CCO and avoiding precipitation of secondary phases (CaO, CoO, Co3O4, Ti oxides, CaTiO3, etc.). Identify the Ti-rich chemical potential point where μ_Ti is maximized within the stability region. Use formation energies of these bulk phases from a public materials database (e.g., Materials Project) or compute them with the same DFT framework.
- Evidence: `/app/outputs/chemical_potentials.log`

### Step 3: DFT structural optimization of pristine CCO
- Role: process
- Action: Perform DFT geometry optimization (PBE+U with U-J=4 eV on Co) for the pristine 5/3 and 3/2 approximant unit cells. Relax atomic positions and cell parameters to obtain the reference total energy and equilibrium lattice constants.
- Evidence: `/app/outputs/pristine_relax.log`

### Step 4: DFT structural optimization of Ti-doped CCO
- Role: process
- Action: For each of the two approximant unit cells, generate defect supercells by substituting a single Ti atom for a Co (all inequivalent sites in the RS and CoO2 subsystems) and for a Ca atom. Use DFT (same PBE+U settings) to relax the atomic positions of each doped structure. Collect the total energy of each relaxed defect cell.
- Evidence: `/app/outputs/doped_energies.csv`

### Step 5: Compute defect formation energies
- Role: scored (load-bearing)
- Action: Calculate the defect formation energy Ef for each site using the formula Ef = E_doped - E_pristine - Σ ν_i μ_i, where ν_i are stoichiometric coefficients and μ_i are the chemical potentials at the Ti-rich point. Average the formation energies over all inequivalent sites of the same type (Co_RS, Co_CoO2, Ca). Output the six averaged values for the 5/3 and 3/2 cells in formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {
  "5/3": {
    "Ti_Co_RS": <number>,
    "Ti_Co_CoO2": <number>,
    "Ti_Ca": <number>
  },
  "3/2": {
    "Ti_Co_RS": <number>,
    "Ti_Co_CoO2": <number>,
    "Ti_Ca": <number>
  }
}
- Scoring: scored by hidden verifier

### Step 6: Compute and analyze projected density of states (PDOS)
- Role: process
- Action: For the relaxed Ti-doped structures (Ti in RS and in CoO2), perform a single-point DFT calculation to obtain the site- and orbital-projected density of states (PDOS) for Ti d orbitals and Co d orbitals. Use this to confirm the valence states of Ti (4+) and Co (mixed 3+/4+) and the occupancy of the d orbitals.
- Evidence: `/app/outputs/pdos_analysis.png`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Defect formation energies for Ti substitution at Co (RS), Co (CoO2), and Ca sites, averaged over inequivalent sites, for the 5/3 and 3/2 approximant unit cells computed at the Ti-rich chemical potential point.
- schema:
  - `type`: object
  - `required`: `5/3`, `3/2`
  - `properties`:
    - `5/3`:
      - `type`: object
      - `required`: `Ti_Co_RS`, `Ti_Co_CoO2`, `Ti_Ca`
      - `properties`:
        - `Ti_Co_RS`:
          - `type`: number
          - `units`: eV
        - `Ti_Co_CoO2`:
          - `type`: number
          - `units`: eV
        - `Ti_Ca`:
          - `type`: number
          - `units`: eV
    - `3/2`:
      - `type`: object
      - `required`: `Ti_Co_RS`, `Ti_Co_CoO2`, `Ti_Ca`
      - `properties`:
        - `Ti_Co_RS`:
          - `type`: number
          - `units`: eV
        - `Ti_Co_CoO2`:
          - `type`: number
          - `units`: eV
        - `Ti_Ca`:
          - `type`: number
          - `units`: eV

Notes: The hidden checker compares the six formation energy values to the paper's reported values using an appropriate tolerance to account for differences in DFT implementation. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "5/3",
          "3/2"
        ],
        "properties": {
          "5/3": {
            "type": "object",
            "required": [
              "Ti_Co_RS",
              "Ti_Co_CoO2",
              "Ti_Ca"
            ],
            "properties": {
              "Ti_Co_RS": {
                "type": "number",
                "units": "eV"
              },
              "Ti_Co_CoO2": {
                "type": "number",
                "units": "eV"
              },
              "Ti_Ca": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "3/2": {
            "type": "object",
            "required": [
              "Ti_Co_RS",
              "Ti_Co_CoO2",
              "Ti_Ca"
            ],
            "properties": {
              "Ti_Co_RS": {
                "type": "number",
                "units": "eV"
              },
              "Ti_Co_CoO2": {
                "type": "number",
                "units": "eV"
              },
              "Ti_Ca": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "Defect formation energies for Ti substitution at Co (RS), Co (CoO2), and Ca sites, averaged over inequivalent sites, for the 5/3 and 3/2 approximant unit cells computed at the Ti-rich chemical potential point."
    }
  ],
  "notes": "The hidden checker compares the six formation energy values to the paper's reported values using an appropriate tolerance to account for differences in DFT implementation. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts produced by each workflow step. The principal score comes from `/app/outputs/formation_energies.json`: the six formation energies are compared to hidden reference values with an appropriate tolerance; only a correct DFT calculation will give numbers that fall within the required tolerance. The remaining outputs (`cco_structures.log`, `chemical_potentials.log`, `pristine_relax.log`, `doped_energies.csv`, `pdos_analysis.png`) are checked for presence, internal consistency, and correct structure; they contribute a smaller portion of the overall reward. The final score is a weighted combination of the stage scores. Simply reporting the expected numbers without performing the computation will not pass the verifier.
