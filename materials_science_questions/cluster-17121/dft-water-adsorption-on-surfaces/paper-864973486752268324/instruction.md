# Reproduce DFT-computed surface adsorption properties of Pt(111)–water interfaces with alkali cations

## Problem background
The hydrogen evolution reaction (HER) on platinum is a critical process for water electrolysis and renewable hydrogen production. In alkaline electrolytes the HER kinetics are substantially slower than in acid, and the fundamental reasons for this are still debated. Additional complexity comes from the presence of alkali metal cations (e.g., Li⁺, Na⁺, K⁺) in the electrolyte. Experiments have shown that the HER activity depends on the identity of the cation, but the underlying microscopic mechanism — whether the cations directly interact with the platinum surface, modify the interfacial water structure, or alter the coverage and chemical state of surface hydroxyl (OHad) species — remains unresolved. Understanding how different cations influence the adsorption properties of OHad on Pt(111) at the electrode–water interface is an open scientific question with direct implications for designing more efficient alkaline electrolysers.

## Approach
The computational approach models the Pt(111)–water interface using density functional theory (DFT) with explicit solvation. A three-layer 4×4 Pt(111) slab is covered by an explicit water layer (~22 water molecules) to represent the near‑surface liquid. An OH group is placed at an fcc hollow site on the Pt surface to produce an adsorbed hydroxyl (OHad), and one water molecule is replaced by a hydrated alkali cation (Li⁺, Na⁺, or K⁺ separately). This setup allows systematic study of how each cation modifies the OHad properties.

The workflow consists of three analysis stages, each carried out for the three cations:
1. **Static DFT and adsorption energy:** Geometry optimization of the interface (with the bottom two Pt layers frozen) yields total energies. The OHad adsorption energy is computed as E_ad^OH = E(slab+water+OHad+cation) – E(slab+water+cation) – E(OH), using a consistent OH reference.
2. **Bader charge and dipole analysis:** From the optimized charge density, Bader charges are obtained. The net charge on the O atom in OHad is recorded, and the dipole moments of the OHad group and of the Pt–O bond are calculated.
3. **Potential-dependent free energy (grand canonical DFT):** The electronic free energy G(U) of the interface is mapped as a function of applied potential U by varying the number of electrons (surface-charging method). The OHad adsorption free energy G_ad^OH(U) = G(U; with OHad) – G(U; without OHad) – E(OH) is computed for at least five potentials between −1.0 and 1.0 V_RHE.

The calculations may be performed with any plane-wave DFT code that supports the PBE functional, dispersion corrections, and explicit water layers, using open‑source tools (e.g., Quantum ESPRESSO, CP2K, GPAW) in place of the proprietary code originally used. The Bader analysis uses the Henkelman code. Optional pre‑built interface geometries are available on Zenodo, or the agent may construct the interfaces from standard Pt(111) slabs and water molecules.

## Reproduction target
Produce the following three artifacts for the Pt(111)–water interface in the presence of each alkali cation (Li⁺, Na⁺, K⁺):

- **adsorption_energies.json**: a JSON object with keys `Li`, `Na`, `K`, each giving the OHad adsorption energy (in eV) computed from the static DFT protocol.
- **bader_charges_dipoles.json**: a JSON object with keys `Li`, `Na`, `K`, each containing the fields `O_charge` (net Bader charge on the oxygen of OHad, in |e|), `OH_dipole_D` (dipole moment of the OHad group in Debye), and `PtO_dipole_D` (dipole moment of the Pt–O bond in Debye).
- **free_energy_vs_potential.csv**: a CSV with columns `potential_V`, `G_ad_OH_Li`, `G_ad_OH_Na`, `G_ad_OH_K`. Each row corresponds to one applied potential (at least five points between −1.0 and 1.0 V_RHE), and the adsorption free energies are given in eV.

The quantities must be obtained by running DFT calculations as described in the workflow steps; reporting pre‑existing literature values without computation is not acceptable. The target is to determine the relative ordering of these quantities across the three cations and to produce consistent numerical values that reflect the physics of the cation–OHad interaction.

## Assets

- DFT-optimized interface geometries (Zenodo): 10.5281/zenodo.7026971
- Open-source DFT code (Quantum ESPRESSO, CP2K, GPAW, etc.): quantum-espresso | cp2k | gpaw
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- GOCIA – Python package for interface configuration sampling: https://github.com/zishengz/gocia
- Pt(111) slab structure
- Water molecule and alkali cation species

## Workflow steps

### Step 1: Build Pt(111)–water interface models with OHad and cation
- Role: process
- Action: Construct a periodic Pt(111) slab (three-layer 4×4 supercell), add an explicit water layer (~22 water molecules), place an adsorbed OH at an fcc hollow site on the surface, and replace one water molecule by a hydrated cation (Li⁺, Na⁺, K⁺ in separate models). The agent may use the optional GOCIA tool for sampling water configurations. Alternatively, use the pre-built geometries from the Zenodo resource.
- Evidence: `/app/outputs/interface_structures.zip`

### Step 2: Static DFT optimization and OHad adsorption energy calculation
- Role: scored (load-bearing)
- Action: For each cation (Li⁺, Na⁺, K⁺), perform a static DFT geometry optimization of the interface (with the bottom two Pt layers frozen). From the total energies, compute the OHad adsorption energy E_ad^OH = E(*OHad) – E(*) – E(OH), using the same OH reference energy for all cations. Report the three adsorption energies.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {'Li': float, 'Na': float, 'K': float}
- Scoring: scored by hidden verifier

### Step 3: Bader charge and dipole moment analysis
- Role: scored
- Action: Using the optimized charge densities from Step 02, perform Bader charge analysis to obtain the net charge on the O atom in OHad. From the Bader charges and atomic positions, compute the dipole moment of the OHad group and the Pt–O bond for each cation. Report the O charge, OHad dipole moment, and Pt–O dipole moment for Li⁺, Na⁺, and K⁺.
- Output file: `/app/outputs/bader_charges_dipoles.json`
- Format: json
- Contract: {'Li': {'O_charge': float, 'OH_dipole_D': float, 'PtO_dipole_D': float}, 'Na': {...}, 'K': {...}}
- Scoring: scored by hidden verifier

### Step 4: Potential-dependent OHad adsorption free energy via grand canonical DFT
- Role: scored
- Action: For each cation, perform grand canonical DFT calculations by varying the number of electrons in the system to sample the relation between electronic energy and applied potential. Use the surface-charging method to fit the free energy G(U) as a function of potential U. Compute G_ad^OH(U) = G(U; *OHad) – G(U; *) – E(OH) for at least five potentials evenly spaced between -1.0 and 1.0 V_RHE. Report the free energies for all cations in a CSV file.
- Output file: `/app/outputs/free_energy_vs_potential.csv`
- Format: csv
- Contract: CSV header: potential_V, G_ad_OH_Li, G_ad_OH_Na, G_ad_OH_K. Numeric values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/bader_charges_dipoles.json`
- `/app/outputs/free_energy_vs_potential.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: OHad adsorption energies for Li, Na, K evaluated from static DFT. The ordering and values should be consistent with the paper's findings.
- schema:
  - `type`: object
  - `required`:
    - `Li`: float
    - `Na`: float
    - `K`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Li`: eV
    - `Na`: eV
    - `K`: eV

### bader_charges_dipoles.json
- path: `/app/outputs/bader_charges_dipoles.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Bader charges and dipole moments of OHad for each cation. The ordering should reflect increased polarization for smaller cations.
- schema:
  - `type`: object
  - `required`:
    - `Li`:
      - `O_charge`: float
      - `OH_dipole_D`: float
      - `PtO_dipole_D`: float
    - `Na`:
      - `O_charge`: float
      - `OH_dipole_D`: float
      - `PtO_dipole_D`: float
    - `K`:
      - `O_charge`: float
      - `OH_dipole_D`: float
      - `PtO_dipole_D`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Li.O_charge`: |e|
    - `Li.OH_dipole_D`: Debye
    - `Li.PtO_dipole_D`: Debye

### free_energy_vs_potential.csv
- path: `/app/outputs/free_energy_vs_potential.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Potential-dependent OHad adsorption free energies. The correct trend (Li > Na > K) should be maintained over the potential window.
- schema:
  - `type`: table
  - `required_columns`: `potential_V`, `G_ad_OH_Li`, `G_ad_OH_Na`, `G_ad_OH_K`
  - `items`: object
  - `required`: object
  - `units`:
    - `potential_V`: V_RHE
    - `G_ad_OH_Li`: eV
    - `G_ad_OH_Na`: eV
    - `G_ad_OH_K`: eV

Notes: All outputs are numeric results from DFT calculations. The checker will recompute error metrics against hidden paper reference values and verify the required ordering. No further transformations are needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Li": "float",
          "Na": "float",
          "K": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Li": "eV",
          "Na": "eV",
          "K": "eV"
        }
      },
      "description": "OHad adsorption energies for Li, Na, K evaluated from static DFT. The ordering and values should be consistent with the paper's findings."
    },
    {
      "file": "bader_charges_dipoles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Li": {
            "O_charge": "float",
            "OH_dipole_D": "float",
            "PtO_dipole_D": "float"
          },
          "Na": {
            "O_charge": "float",
            "OH_dipole_D": "float",
            "PtO_dipole_D": "float"
          },
          "K": {
            "O_charge": "float",
            "OH_dipole_D": "float",
            "PtO_dipole_D": "float"
          }
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Li.O_charge": "|e|",
          "Li.OH_dipole_D": "Debye",
          "Li.PtO_dipole_D": "Debye"
        }
      },
      "description": "Bader charges and dipole moments of OHad for each cation. The ordering should reflect increased polarization for smaller cations."
    },
    {
      "file": "free_energy_vs_potential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "potential_V",
          "G_ad_OH_Li",
          "G_ad_OH_Na",
          "G_ad_OH_K"
        ],
        "items": {},
        "required": {},
        "units": {
          "potential_V": "V_RHE",
          "G_ad_OH_Li": "eV",
          "G_ad_OH_Na": "eV",
          "G_ad_OH_K": "eV"
        }
      },
      "description": "Potential-dependent OHad adsorption free energies. The correct trend (Li > Na > K) should be maintained over the potential window."
    }
  ],
  "notes": "All outputs are numeric results from DFT calculations. The checker will recompute error metrics against hidden paper reference values and verify the required ordering. No further transformations are needed."
}
```

## How you are scored
A hidden verifier automatically evaluates your submitted artifacts. For each of the three scored output files, the verifier reads the file, compares your reported numbers to hidden reference values (derived from the scientific literature reporting the original study), and checks that required qualitative trends (relative ordering among Li⁺, Na⁺, K⁺) are satisfied. The comparison uses tolerances that account for differences in DFT codes, pseudopotentials, and numerical settings, so an independent re‑run with a different but reasonable choice of code and parameters will still receive credit if the physics is correctly captured.

Each artifact contributes to the overall reward with a predefined weight. The adsorption energies carry the largest weight, followed by the Bader/dipole quantities and the potential‑dependent free energies. The verifier does not require exact reproduction of a specific published figure; it evaluates your computed values and trends independently. Your goal is to execute the described workflow faithfully and produce physically meaningful results consistent with the expected cation‑dependent behavior of the Pt(111)–OHad interface.
