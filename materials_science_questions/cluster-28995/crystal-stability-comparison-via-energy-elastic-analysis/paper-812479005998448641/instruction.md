# Pyramidal-II GSFE and Dislocation Core Analysis in HCP Metals

## Problem background
Hexagonal-close-packed (HCP) metals are important structural materials. Pyramidal-II ⟨c+a⟩ dislocations accommodate c-axis deformation, but their core structures vary significantly across metals and can be asymmetric, influencing their mobility and interactions. Understanding the dissociation of these dislocations into partials and the role of the generalized stacking fault energy (GSFE) landscape is critical for predicting mechanical behavior. In some HCP metals, ferromagnetism may affect the GSFE curve, which in turn alters the dislocation core structure. This task aims to compute the GSFE parameters on the {1-1-22} plane for selected metals and to determine the equilibrium dislocation core properties from these GSFE curves.

## Approach
The approach combines first-principles density functional theory (DFT) calculations with phase-field dislocation dynamics (PFDD) simulations. First, the GSFE curve along the ⟨11-23⟩ direction on the {1-1-22} plane is computed for Be, Mg, Co (non-magnetic), and Co (ferromagnetic) using an open-source DFT code. The calculations use supercells, vacuum, and a relaxation protocol where atomic positions perpendicular to the glide direction are relaxed while those along the glide direction are fixed. From these curves, the unstable stacking fault energies U1 and U2, the intrinsic stacking fault energy I, and the normalized displacement xI/b at the intrinsic minimum are extracted. Second, a PFDD model is implemented that minimizes an energy functional comprising elastic strain energy (with anisotropic elasticity) and a periodic lattice potential fitted to the DFT GSFE curve. Using the provided elastic constants for Mg and ferromagnetic Co, simulations of the dissociation of perfect edge and screw dislocations are performed. The equilibrium order parameter profiles are analyzed to extract the splitting distance Re between partials, the partial Burgers vector fractions bl and br, and the partial core widths wl and wr.

## Reproduction target
Produce two output files under /app/outputs: (1) step_01_dft_gsfe_parameters.json containing the GSFE parameters U1, I, U2 (in mJ/m²), and xI/b (dimensionless) for Be, Mg, Co_NM, and Co_FM. (2) step_02_pfdd_dislocation_results.csv containing, for Mg and ferromagnetic Co, the equilibrium dislocation core properties: splitting distance Re (in Å), partial Burgers vector fractions bl and br (normalized by b), and partial core widths wl and wr (normalized by b) for both edge and screw character dislocations. The results must be self-consistent with the computed GSFE curves and the elastic constants provided in the assets.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotential library: http://www.physics.rutgers.edu/gbrv/
- HCP lattice parameters for Be, Mg, Co
- Elastic constants for Mg and ferromagnetic Co

## Workflow steps

### Step 1: DFT GSFE calculation
- Role: scored
- Action: Use an open-source DFT code (e.g., Quantum ESPRESSO) to compute the {1-1-22} generalized stacking fault energy curve along the <11-23> direction for HCP Be, Mg, Co (non-magnetic), and Co (ferromagnetic). Employ supercells containing 60 atoms, a vacuum layer of about 15 Å, a sufficiently dense k-point mesh for the GSFE supercell, and a relaxation protocol where atomic positions along the glide direction are fixed while coordinates perpendicular to the glide direction are relaxed. Extract the unstable stacking fault energies U1 and U2, the intrinsic stacking fault energy I, and the normalized displacement xI/b at the intrinsic minimum. Report these values in a JSON file.
- Output file: `/app/outputs/step_01_dft_gsfe_parameters.json`
- Format: json
- Contract: {
  "Be": {"U1": "float (mJ/m^2)", "I": "float (mJ/m^2)", "U2": "float (mJ/m^2)", "xI_over_b": "float"},
  "Mg": {"U1": "float", "I": "float", "U2": "float", "xI_over_b": "float"},
  "Co_NM": {"U1": "float", "I": "float", "U2": "float", "xI_over_b": "float"},
  "Co_FM": {"U1": "float", "I": "float", "U2": "float", "xI_over_b": "float"}
}
- Scoring: scored by hidden verifier

### Step 2: PFDD dislocation simulation
- Role: scored (load-bearing)
- Action: Implement the phase-field dislocation dynamics (PFDD) model as described in the referenced paper, or an equivalent formulation, to simulate the dissociation of perfect edge and screw dislocations on the pyramidal-II plane. Fit the DFT-computed GSFE curves from Step 1 to the periodic lattice energy function using suitable curve fitting. Use the following elastic constants: for Mg, C11=63.3, C12=25.9, C13=20.8, C33=65.7, C44=18, C66=18.7 GPa; for ferromagnetic Co, C11=359.2, C12=164.8, C13=109.3, C33=406.4, C44=93.1, C66=97.2 GPa. Use the interplanar spacing d/b for the pyramidal-II plane appropriate for each material. Simulate equilibrium structures for edge and screw dislocations in Mg and ferromagnetic Co. From the equilibrium order parameter profiles, extract the equilibrium splitting distance Re (in Å), partial Burgers vector fractions bl and br (normalized by b), and partial core widths wl and wr (normalized by b). Write the results to a CSV file.
- Output file: `/app/outputs/step_02_pfdd_dislocation_results.csv`
- Format: csv
- Contract: material,dislocation_type,Re,bl,br,wl,wr
Mg,edge,<float>,<float>,<float>,<float>,<float>
Mg,screw,<float>,<float>,<float>,<float>,<float>
Co_FM,edge,<float>,<float>,<float>,<float>,<float>
Co_FM,screw,<float>,<float>,<float>,<float>,<float>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dft_gsfe_parameters.json`
- `/app/outputs/step_02_pfdd_dislocation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dft_gsfe_parameters.json
- path: `/app/outputs/step_01_dft_gsfe_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed GSFE parameters for Be, Mg, Co_NM, and Co_FM. U1, I, U2 are in mJ/m^2, xI_over_b is dimensionless.
- schema:
  - `type`: object
  - `required`:
    - `Be`: object
    - `Mg`: object
    - `Co_NM`: object
    - `Co_FM`: object
  - `items`:
    - `U1`: number (mJ/m^2)
    - `I`: number (mJ/m^2)
    - `U2`: number (mJ/m^2)
    - `xI_over_b`: number

### step_02_pfdd_dislocation_results.csv
- path: `/app/outputs/step_02_pfdd_dislocation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: PFDD-computed dislocation core properties for Mg and Co_FM. Re is splitting distance in Å; bl, br, wl, wr are fractions of the Burgers vector magnitude b.
- schema:
  - `type`: table
  - `required_columns`: `material`, `dislocation_type`, `Re`, `bl`, `br`, `wl`, `wr`
  - `units`:
    - `Re`: Å
    - `bl`: fraction of b
    - `br`: fraction of b
    - `wl`: fraction of b
    - `wr`: fraction of b

Notes: The checker will compare the submitted GSFE parameters and dislocation core properties to hidden reference values with appropriate tolerances. Structural relations (U2 > U1, edge splitting > screw splitting) will also be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dft_gsfe_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Be": "object",
          "Mg": "object",
          "Co_NM": "object",
          "Co_FM": "object"
        },
        "items": {
          "U1": "number (mJ/m^2)",
          "I": "number (mJ/m^2)",
          "U2": "number (mJ/m^2)",
          "xI_over_b": "number"
        }
      },
      "description": "DFT-computed GSFE parameters for Be, Mg, Co_NM, and Co_FM. U1, I, U2 are in mJ/m^2, xI_over_b is dimensionless."
    },
    {
      "file": "step_02_pfdd_dislocation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "dislocation_type",
          "Re",
          "bl",
          "br",
          "wl",
          "wr"
        ],
        "units": {
          "Re": "Å",
          "bl": "fraction of b",
          "br": "fraction of b",
          "wl": "fraction of b",
          "wr": "fraction of b"
        }
      },
      "description": "PFDD-computed dislocation core properties for Mg and Co_FM. Re is splitting distance in Å; bl, br, wl, wr are fractions of the Burgers vector magnitude b."
    }
  ],
  "notes": "The checker will compare the submitted GSFE parameters and dislocation core properties to hidden reference values with appropriate tolerances. Structural relations (U2 > U1, edge splitting > screw splitting) will also be verified."
}
```

## How you are scored
A hidden verifier will independently score each output file by comparing your reported values to reference numbers using appropriate tolerances. For the GSFE parameters, it checks that the energies and normalized displacement fall within acceptable bounds and that the energy ordering U2 > U1 holds for all materials. For the dislocation core properties, it compares Re, bl, br to reference values and also verifies that the edge dislocation splitting distance is larger than the screw splitting distance for each material. The two stages are combined with a weighting to produce the final score. Simply reporting values that match the reference is not sufficient; the results must arise from a consistent DFT and PFDD workflow. The verifier does not look at intermediate plots or logs, only the final files.
