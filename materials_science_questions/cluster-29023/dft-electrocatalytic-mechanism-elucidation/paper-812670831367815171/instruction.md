# DFT Stability and Reactivity Trends of Pt and Au Single-Atom Catalysts on Carbon Defects

## Problem background
Vinyl chloride monomer (VCM), used in PVC production, is manufactured via acetylene hydrochlorination, a process that still relies on toxic mercury-based catalysts. Single-atom catalysts (SACs) based on platinum (Pt) and gold (Au) supported on carbon have emerged as promising mercury-free alternatives. A key open question is the relative stability and reactivity of Pt versus Au single atoms on carbon defects, which governs their practical performance. This task addresses that question by computing the energetic properties of these catalytic systems using density functional theory (DFT).

## Approach
The approach uses periodic DFT calculations with the PBE-D3 dispersion-corrected functional and PAW pseudopotentials, as provided by the open-source Quantum ESPRESSO code. The carbon support is modeled by specific defect structures containing nitrogen and oxygen functional groups: a 4×N6 cavity, a di-epoxide (2×Ep) defect, and a tri-pyrrolic (3×N5) defect. Atomic coordinates for these defects and for the metal-containing configurations are obtained from a public dataset.

Three sets of calculations are performed:
1. Formation energies: total energies of Pt, Au, PtCl, and AuCl single-atom species on each defect are computed, along with isolated reference species (Pt, Au, Cl₂) and the bare defects. Formation energies are then derived as energy differences.
2. Acetylene adsorption energies: for PtCl species on the 2×Ep and 3×N5 defects, with increasing number of additional chlorine ligands (0 to 4), the adsorption energy of acetylene is determined from geometry optimizations followed by single-point calculations.
3. Reaction profiles: the full reaction pathway for acetylene hydrochlorination over PtCl/2×Ep and PtCl/3×N5 is mapped using the climbing-image nudged elastic band (CI-NEB) method, identifying intermediates and transition states and recording their energies relative to the initial state.

All computed energies are assembled into a structured JSON file.

## Reproduction target
Produce a file `dft_results.json` containing the following computed DFT energies (all in eV) for the specified systems:

- **formation_energies**: formation energies of Pt, Au, PtCl, AuCl single atoms on 4×N6, 2×Ep, and 3×N5 defects.
- **adsorption_energies**: acetylene adsorption energies on PtCl single-atom species on 2×Ep and 3×N5 defects with 0, 1, 2, 3, and 4 chlorine ligands.
- **reaction_profile**: reaction energy profiles (list of intermediates and transition states, each with a label and relative energy) for acetylene hydrochlorination over PtCl/2×Ep and PtCl/3×N5, with energies referenced to the initial state (IS = 0.0 eV).

The exact keys and structure are specified in the output contract. The results will be evaluated against hidden reference values.

## Assets

- ioChem-BD collection for defect structures: 10.19061/iochem-bd-1-74
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Retrieve DFT input structures
- Role: process
- Action: Download the atomic structures for defect models (4×N6, 2×Ep, 3×N5) and Pt/Au species from the ioChem-BD collection. Prepare Quantum ESPRESSO input files for single-point energy calculations (pw.x) with appropriate periodic boundary conditions.
- Evidence: `/app/outputs/input_structures.tar.gz`

### Step 2: Calculate formation energies
- Role: process
- Action: Compute total energies for Pt, Au, PtCl, AuCl species on 4×N6, 2×Ep, and 3×N5 defects, as well as isolated Pt, Au, Cl2 reference molecules and the bare defects. Run DFT single-point calculations with pw.x, then compute formation energies using the standard formula (difference of total energies).
- Evidence: `/app/outputs/formation_energies.log`

### Step 3: Calculate acetylene adsorption energies
- Role: process
- Action: For PtCl single-atom species on 2×Ep and 3×N5 defects with 0 to 4 additional Cl ligands, compute total energies of isolated C2H2, the clean PtCl/defect systems, and the systems with adsorbed C2H2. Perform geometry optimizations followed by single-point calculations, then calculate adsorption energies.
- Evidence: `/app/outputs/adsorption_energies.log`

### Step 4: Calculate reaction energy profiles
- Role: process
- Action: Perform CI-NEB calculations with Quantum ESPRESSO (neb.x) to locate the reaction path for acetylene hydrochlorination on PtCl/2×Ep and PtCl/3×N5. Identify relevant intermediates and transition states, compute their energies relative to the initial state. Refine using the climbing image method.
- Evidence: `/app/outputs/reaction_profile.log`

### Step 5: Compile DFT results
- Role: scored (load-bearing)
- Action: Gather all computed formation energies, acetylene adsorption energies, and reaction energy profiles from the preceding calculations. Assemble them into a single JSON file (dft_results.json) according to the output schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"formation_energies": {"Pt_4xN6": 0.0, "Au_4xN6": 0.0, "PtCl_4xN6": 0.0, "AuCl_4xN6": 0.0, "Pt_2xEp": 0.0, "Au_2xEp": 0.0, "PtCl_2xEp": 0.0, "AuCl_2xEp": 0.0, "Pt_3xN5": 0.0, "Au_3xN5": 0.0, "PtCl_3xN5": 0.0, "AuCl_3xN5": 0.0}, "adsorption_energies": {"PtCl_2xEp_0Cl": 0.0, "PtCl_2xEp_1Cl": 0.0, "PtCl_2xEp_2Cl": 0.0, "PtCl_2xEp_3Cl": 0.0, "PtCl_2xEp_4Cl": 0.0, "PtCl_3xN5_0Cl": 0.0, "PtCl_3xN5_1Cl": 0.0, "PtCl_3xN5_2Cl": 0.0, "PtCl_3xN5_3Cl": 0.0, "PtCl_3xN5_4Cl": 0.0}, "reaction_profile": {"PtCl_2xEp": [{"label": "IS", "energy": 0.0}, ...], "PtCl_3xN5": [{"label": "IS", "energy": 0.0}, ...]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled DFT results: formation energies, acetylene adsorption energies, and reaction energy profiles for the specified defect and metal species combinations.
- schema:
  - `type`: object
  - `required`:
    - `formation_energies`: object mapping configuration names (e.g., Pt_4xN6) to float values in eV
    - `adsorption_energies`: object mapping configuration names (e.g., PtCl_2xEp_0Cl) to float values in eV
    - `reaction_profile`: object with keys 'PtCl_2xEp' and 'PtCl_3xN5', each containing a list of objects with 'label' (string) and 'energy' (float, eV relative to initial state)

Notes: All energies are in eV. Configuration naming convention for formation_energies: {Species}_{Defect} (e.g., Pt_4xN6). For adsorption_energies: {Species}_{Defect}_{N}Cl. Reaction profile labels include intermediates (IS, FS, etc.) and transition states (TS).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "formation_energies": "object mapping configuration names (e.g., Pt_4xN6) to float values in eV",
          "adsorption_energies": "object mapping configuration names (e.g., PtCl_2xEp_0Cl) to float values in eV",
          "reaction_profile": "object with keys 'PtCl_2xEp' and 'PtCl_3xN5', each containing a list of objects with 'label' (string) and 'energy' (float, eV relative to initial state)"
        }
      },
      "description": "Compiled DFT results: formation energies, acetylene adsorption energies, and reaction energy profiles for the specified defect and metal species combinations."
    }
  ],
  "notes": "All energies are in eV. Configuration naming convention for formation_energies: {Species}_{Defect} (e.g., Pt_4xN6). For adsorption_energies: {Species}_{Defect}_{N}Cl. Reaction profile labels include intermediates (IS, FS, etc.) and transition states (TS)."
}
```

## How you are scored
Your solution is scored by a hidden automated verifier that reads your `dft_results.json`. The verifier checks two aspects:

- **Trend checks:** whether your computed energies follow physically expected structural relationships (e.g., relative ordering of formation energies for different metal/defect combinations, monotonic behavior of adsorption energies with chlorine count, correct shape of reaction profiles). These checks verify the qualitative correctness of your results.
- **Tolerance checks:** whether your absolute energy values are within an acceptable tolerance of hidden reference values, which are derived from the original study. The tolerances are set to account for differences between DFT implementations.

The final reward is a weighted combination of the trend and tolerance checks. Simply reporting plausible numbers without performing the DFT calculations is insufficient; the verifier expects physically consistent energies that can only be obtained by running the specified computational workflow.
