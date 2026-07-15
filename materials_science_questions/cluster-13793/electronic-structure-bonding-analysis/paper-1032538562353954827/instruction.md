# First-Principles Study of Hole Effective Mass and Chemical Bonding in Monoclinic Gallium Oxide

## Problem background
Wide-bandgap oxides such as β-Ga₂O₃ suffer from extremely low hole mobility, which limits their use in electronic devices. The valence band maximum (VBM) is known to be dominated by oxygen 2p states, yet the reason for the unusually heavy hole effective masses and the formation of self-trapped holes remains a subject of debate. Recent first-principles work suggests that anion-anion antibonding coupling (AAAC) between certain oxygen pairs—rather than the conventional Ga–O bonding—dominates the orbital coupling at the VBM, narrowing the VBM bandwidth and enhancing the hole mass. It has further been proposed that applying tensile strain along the b-axis can weaken this AAAC, thereby reducing the hole effective masses. The goal of this task is to reproduce and verify these key computational findings: the effective masses for pristine and strained β-Ga₂O₃, and the COHP analysis that reveals the AAAC mechanism.

## Approach
The reproduction follows a first-principles computational approach using open-source tools. The monoclinic β-Ga₂O₃ crystal structure (conventional 20-atom cell) is obtained from the Materials Project and fully relaxed with a hybrid density functional (HSE06 or equivalent). From the relaxed structure, the electronic band structure is computed and hole effective masses are extracted by parabolic fitting at the global VBM and at the Γ point. The orbital-projected density of states is calculated to confirm the oxygen-dominated VBM. Crystal orbital Hamilton population (COHP) analysis is performed using LOBSTER on the pristine wavefunctions to decompose the coupling into Ga–O and O–O contributions within the VBM energy window, and to identify the dominant O–O pairs and their orbital character. The procedure is then repeated for a structure under 2% uniaxial tensile strain along the b-axis (applied to the relaxed pristine cell, followed by a relaxation of the atomic positions with fixed lattice parameters). The key comparisons are between the unstrained and strained effective masses, and between the total Ga–O and O–O COHP values, to verify the AAAC mechanism.

## Reproduction target
Produce two scored artifacts:
1. Hole effective masses (in units of the free-electron mass m₀) for pristine β-Ga₂O₃ and for β-Ga₂O₃ under 2% uniaxial tensile strain along the b-axis, reporting the directional masses along a*, b*, c* and the conductivity mass.
2. A COHP summary containing the total integrated Ga–O and total integrated O–O COHP within the VBM energy window (−2 to 0 eV) from the pristine calculation, and the identity (oxygen pair, orbital character, and COHP matrix element value) of the dominant O–O antibonding coupling at the VBM at Γ and at the global VBM (I point on the M₂–D path).
All values must be written to the specified JSON files under /app/outputs.

## Assets

- Crystal structure of β-Ga₂O₃: https://materialsproject.org/materials/mp-886/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- LOBSTER: https://www.cohp.de/

## Workflow steps

### Step 1: Relax pristine β-Ga₂O₃ structure
- Role: process
- Action: Obtain the monoclinic β-Ga₂O₃ crystal structure (e.g., from Materials Project) and fully relax it using an open-source DFT code (e.g., Quantum ESPRESSO) with a hybrid functional (e.g., HSE06) until forces and total energy are converged.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Band structure and effective masses (pristine)
- Role: process
- Action: Using the relaxed structure, perform a self-consistent and non-self-consistent band structure calculation to obtain eigenvalues along high-symmetry paths. Fit parabolas at the VBM at Γ and at the global VBM (I point on M₂–D) to extract hole effective masses along a*, b*, c*, and compute the conductivity mass.
- Evidence: `/app/outputs/band_structure_pristine.dat`

### Step 3: Projected density of states (pristine)
- Role: process
- Action: Calculate orbital-projected density of states using the wavefunctions from the pristine calculation, confirming that the VBM is oxygen-dominated.
- Evidence: `/app/outputs/pdos_pristine.dat`

### Step 4: COHP analysis (pristine)
- Role: process
- Action: Use LOBSTER to compute crystal orbital Hamilton populations from the pristine wavefunctions. Output total Ga–O and total O–O COHP, k‑resolved COHP at VBM at Γ and I, and COHP matrix elements.
- Evidence: `/app/outputs/cohp_raw_pristine.txt`

### Step 5: Generate 2% uniaxial tensile strain along b
- Role: process
- Action: Apply +2% strain along the b lattice vector to the relaxed pristine cell, creating the strained structure used for the main result.
- Evidence: `/app/outputs/strained_structure.cif`

### Step 6: Relax strained structure
- Role: process
- Action: Relax the atomic positions in the strained cell (fixed lattice parameters) using the same DFT settings as step 1.
- Evidence: `/app/outputs/relaxed_strained_structure.cif`

### Step 7: Band structure and effective masses (strained)
- Role: process
- Action: Perform band structure calculation for the relaxed strained cell, extract hole effective masses along a*, b*, c*, and compute conductivity mass in the same way as step 2.
- Evidence: `/app/outputs/band_structure_strained.dat`

### Step 8: Write effective masses artifact
- Role: scored (load-bearing)
- Action: Collect the fitted effective masses from steps 2 and 7 and output them in a JSON file containing the two sets (unstrained and strained) with keys a_star, b_star, c_star, conductivity. All masses are in units of the free-electron mass m₀.
- Output file: `/app/outputs/effective_masses.json`
- Format: json
- Contract: { "unstrained": { "a_star": <float>, "b_star": <float>, "c_star": <float>, "conductivity": <float> }, "strained": { "a_star": <float>, "b_star": <float>, "c_star": <float>, "conductivity": <float> } }
- Scoring: scored by hidden verifier

### Step 9: Write COHP summary artifact
- Role: scored (load-bearing)
- Action: From the COHP data obtained in step 4, extract the integrated total Ga–O and total O–O COHP values within the VBM energy window (−2 to 0 eV) and identify, from the COHP matrix elements, the oxygen pair with the strongest antibonding coupling at Γ and at I (the global VBM), along with the orbital character and COHP value. Write the results to COHP_summary.json.
- Output file: `/app/outputs/COHP_summary.json`
- Format: json
- Contract: { "total_COHP_GaO_integrated_VBM": <float>, "total_COHP_OO_integrated_VBM": <float>, "dominant_pair_at_Gamma": { "pair": "O_x-O_y", "orbitals": "p_z-p_z", "COHP_value": <float> }, "dominant_pair_at_I": { "pair": "O_x-O_y", "orbitals": "p_x-p_x", "COHP_value": <float> } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_masses.json`
- `/app/outputs/COHP_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_masses.json
- path: `/app/outputs/effective_masses.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hole effective masses along a*, b*, c* and conductivity mass for pristine β-Ga₂O₃ and under 2% uniaxial tensile strain along the b-axis.
- schema:
  - `type`: object
  - `required`:
    - `unstrained`: object containing a_star, b_star, c_star, conductivity (all floats in m₀)
    - `strained`: object containing a_star, b_star, c_star, conductivity (all floats in m₀)

### COHP_summary.json
- path: `/app/outputs/COHP_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Integrated total Ga–O and O–O COHP in the VBM energy window, and the strongest O–O antibonding pair at Γ and I.
- schema:
  - `type`: object
  - `required`:
    - `total_COHP_GaO_integrated_VBM`: float (eV)
    - `total_COHP_OO_integrated_VBM`: float (eV)
    - `dominant_pair_at_Gamma`:
      - `pair`: string (e.g., O2-O5)
      - `orbitals`: string (e.g., pz-pz)
      - `COHP_value`: float (eV)
    - `dominant_pair_at_I`:
      - `pair`: string (e.g., O1-O4)
      - `orbitals`: string (e.g., px-px)
      - `COHP_value`: float (eV)

Notes: All masses are in units of the free-electron mass m₀. COHP values are in eV. The VBM energy window is defined as [−2 eV, 0 eV] with the VBM at 0 eV. The checker compares the reported masses to paper-derived reference values (±20% relative tolerance) and verifies COHP sign/relative magnitude and correct dominant pair identification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "unstrained": "object containing a_star, b_star, c_star, conductivity (all floats in m₀)",
          "strained": "object containing a_star, b_star, c_star, conductivity (all floats in m₀)"
        }
      },
      "description": "Hole effective masses along a*, b*, c* and conductivity mass for pristine β-Ga₂O₃ and under 2% uniaxial tensile strain along the b-axis."
    },
    {
      "file": "COHP_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_COHP_GaO_integrated_VBM": "float (eV)",
          "total_COHP_OO_integrated_VBM": "float (eV)",
          "dominant_pair_at_Gamma": {
            "pair": "string (e.g., O2-O5)",
            "orbitals": "string (e.g., pz-pz)",
            "COHP_value": "float (eV)"
          },
          "dominant_pair_at_I": {
            "pair": "string (e.g., O1-O4)",
            "orbitals": "string (e.g., px-px)",
            "COHP_value": "float (eV)"
          }
        }
      },
      "description": "Integrated total Ga–O and O–O COHP in the VBM energy window, and the strongest O–O antibonding pair at Γ and I."
    }
  ],
  "notes": "All masses are in units of the free-electron mass m₀. COHP values are in eV. The VBM energy window is defined as [−2 eV, 0 eV] with the VBM at 0 eV. The checker compares the reported masses to paper-derived reference values (±20% relative tolerance) and verifies COHP sign/relative magnitude and correct dominant pair identification."
}
```

## How you are scored
Each workflow stage’s output artifact is independently evaluated by a hidden verifier. The verifier compares the computed effective masses and COHP summary to reference values derived from the published study, using appropriate tolerances that account for the spread expected from different implementations of the same methodology. The individual scores are combined according to a predetermined weighting to yield the final reward. Reporting the expected numbers without genuinely executing the computational steps is not sufficient; the artifacts must be produced by the full DFT and COHP workflow described above.
