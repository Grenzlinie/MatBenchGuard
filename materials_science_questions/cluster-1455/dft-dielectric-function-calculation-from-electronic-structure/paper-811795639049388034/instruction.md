# DFT-LDA structural relaxation and DFPT dielectric & Born effective charge calculation for rutile TiO₂

## Problem background
Rutile TiO₂ is a widely used dielectric material with a tetragonal crystal structure. Its structural parameters (lattice constants a, c and internal oxygen parameter u) and high-frequency dielectric constants along the a and c axes determine its optical behavior. The Born effective charges quantify the dynamical charges carried by each atom in response to lattice vibrations; they can deviate from formal ionic charges due to covalent effects, and their values provide a sensitive indicator of bonding. First-principles density-functional theory (DFT) and density-functional perturbation theory (DFPT) allow a quantitative computation of these properties.

## Approach
The approach is a first-principles computational study. We use density-functional theory (DFT) in the local-density approximation (LDA) with norm-conserving pseudopotentials to perform a structural relaxation of rutile TiO₂, obtaining the equilibrium lattice constants a, c and the internal oxygen parameter u. From the relaxed geometry, density-functional perturbation theory (DFPT) is employed to compute the high-frequency dielectric constant tensor components ε∞_xx (along a) and ε∞_zz (along c), as well as the full Born effective charge tensors Z* for the titanium and oxygen atoms, including their principal values (eigenvalues) that characterize the charge response along different directions. The calculations are carried out with a plane-wave basis set and a suitable k-point mesh; the workflow consists of two stages: a structural relaxation followed by a DFPT property calculation.

## Reproduction target
The objective is to compute and output the following quantities in a JSON file results.json:
- Lattice constants a (Å) and c (Å) and internal oxygen parameter u from a DFT-LDA structural relaxation of rutile TiO₂.
- High-frequency dielectric constant tensor components ε∞_xx (dimensionless) and ε∞_zz (dimensionless) from DFPT.
- Born effective charge tensor components Z*_xx, Z*_xy, Z*_zz for the Ti atom at (0,0,0) and for the O atom at (u,u,0), in units of electron charge (e).
- Principal values (ζ*) of these effective charge tensors: three values for Ti and three for O, obtained by diagonalizing the corresponding tensors.
Write all fields into `/app/outputs/results.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ti LDA norm-conserving pseudopotential (3s,3p,4s,3d valence)
- O LDA norm-conserving pseudopotential (2s,2p valence)

## Workflow steps

### Step 1: DFT-LDA structural relaxation
- Role: process
- Action: Perform DFT-LDA structural relaxation of rutile TiO₂ in the tetragonal space group D₄ₕ¹⁴. Use norm-conserving pseudopotentials for Ti (3s,3p,4s,3d) and O (2s,2p) within LDA, a plane-wave kinetic-energy cutoff of 90 Ryd, and a (4,4,6) Monkhorst-Pack k‑point grid. Minimize total energy with respect to lattice constants a, c, and the internal oxygen parameter u. Write the relaxed geometry to an output file (e.g., Quantum ESPRESSO pw.x output) for use in the next step.
- Evidence: `/app/outputs/relaxed_structure.out`

### Step 2: DFPT calculation of dielectric constants and Born effective charges
- Role: scored (load-bearing)
- Action: From the relaxed geometry obtained in the previous step, extract and report the equilibrium lattice constants a (Å), c (Å), and internal oxygen parameter u. Using the same DFT-LDA setup (90 Ryd cutoff, (4,4,6) k‑mesh) and the relaxed geometry, perform density-functional perturbation theory (DFPT) to compute: (i) the high-frequency dielectric constant tensor components ε∞ along the a axis (ε∞_xx) and c axis (ε∞_zz); (ii) the Born effective charge tensor components Z*ᵢⱼ for Ti at (0,0,0) and O at (u,u,0) (including the off-diagonal xy component); (iii) the principal values ζ* of these tensors by diagonalization where appropriate. Write all computed values into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: a (float, Å), c (float, Å), u (float), epsilon_inf_xx (float, dimensionless), epsilon_inf_zz (float, dimensionless), Zstar_Ti_xx (float, e), Zstar_Ti_xy (float, e), Zstar_Ti_zz (float, e), Zstar_O_xx (float, e), Zstar_O_xy (float, e), Zstar_O_zz (float, e), zeta1_Ti (float, e), zeta2_Ti (float, e), zeta3_Ti (float, e), zeta1_O (float, e), zeta2_O (float, e), zeta3_O (float, e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the DFT-LDA and DFPT calculated results: relaxed lattice constants a and c (Å), internal oxygen parameter u, high-frequency dielectric constants ε∞ along a and c, Born effective charge tensor components for Ti and O, and principal values of the effective charge tensors.
- schema:
  - `type`: object
  - `required`: `a`, `c`, `u`, `epsilon_inf_xx`, `epsilon_inf_zz`, `Zstar_Ti_xx`, `Zstar_Ti_xy`, `Zstar_Ti_zz`, `Zstar_O_xx`, `Zstar_O_xy`, `Zstar_O_zz`, `zeta1_Ti`, `zeta2_Ti`, `zeta3_Ti`, `zeta1_O`, `zeta2_O`, `zeta3_O`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
      - `description`: Lattice constant a
    - `c`:
      - `type`: number
      - `unit`: Å
      - `description`: Lattice constant c
    - `u`:
      - `type`: number
      - `unit`: fractional
      - `description`: Internal oxygen parameter u
    - `epsilon_inf_xx`:
      - `type`: number
      - `unit`: dimensionless
      - `description`: High-frequency dielectric constant along a axis
    - `epsilon_inf_zz`:
      - `type`: number
      - `unit`: dimensionless
      - `description`: High-frequency dielectric constant along c axis
    - `Zstar_Ti_xx`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component xx for Ti
    - `Zstar_Ti_xy`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component xy for Ti
    - `Zstar_Ti_zz`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component zz for Ti
    - `Zstar_O_xx`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component xx for O
    - `Zstar_O_xy`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component xy for O
    - `Zstar_O_zz`:
      - `type`: number
      - `unit`: e
      - `description`: Born effective charge tensor component zz for O
    - `zeta1_Ti`:
      - `type`: number
      - `unit`: e
      - `description`: First principal value (ζ₁*) of effective charge tensor for Ti
    - `zeta2_Ti`:
      - `type`: number
      - `unit`: e
      - `description`: Second principal value (ζ₂*) of effective charge tensor for Ti
    - `zeta3_Ti`:
      - `type`: number
      - `unit`: e
      - `description`: Third principal value (ζ₃*) of effective charge tensor for Ti
    - `zeta1_O`:
      - `type`: number
      - `unit`: e
      - `description`: First principal value (ζ₁*) of effective charge tensor for O
    - `zeta2_O`:
      - `type`: number
      - `unit`: e
      - `description`: Second principal value (ζ₂*) of effective charge tensor for O
    - `zeta3_O`:
      - `type`: number
      - `unit`: e
      - `description`: Third principal value (ζ₃*) of effective charge tensor for O

Notes: Scoring uses exact-match policy with relative tolerances (hidden) applied to each field against the paper's reference values. The DFPT step is load-bearing because its outputs depend on the correct relaxed geometry from the preceding relaxation step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "c",
          "u",
          "epsilon_inf_xx",
          "epsilon_inf_zz",
          "Zstar_Ti_xx",
          "Zstar_Ti_xy",
          "Zstar_Ti_zz",
          "Zstar_O_xx",
          "Zstar_O_xy",
          "Zstar_O_zz",
          "zeta1_Ti",
          "zeta2_Ti",
          "zeta3_Ti",
          "zeta1_O",
          "zeta2_O",
          "zeta3_O"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å",
            "description": "Lattice constant a"
          },
          "c": {
            "type": "number",
            "unit": "Å",
            "description": "Lattice constant c"
          },
          "u": {
            "type": "number",
            "unit": "fractional",
            "description": "Internal oxygen parameter u"
          },
          "epsilon_inf_xx": {
            "type": "number",
            "unit": "dimensionless",
            "description": "High-frequency dielectric constant along a axis"
          },
          "epsilon_inf_zz": {
            "type": "number",
            "unit": "dimensionless",
            "description": "High-frequency dielectric constant along c axis"
          },
          "Zstar_Ti_xx": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component xx for Ti"
          },
          "Zstar_Ti_xy": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component xy for Ti"
          },
          "Zstar_Ti_zz": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component zz for Ti"
          },
          "Zstar_O_xx": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component xx for O"
          },
          "Zstar_O_xy": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component xy for O"
          },
          "Zstar_O_zz": {
            "type": "number",
            "unit": "e",
            "description": "Born effective charge tensor component zz for O"
          },
          "zeta1_Ti": {
            "type": "number",
            "unit": "e",
            "description": "First principal value (ζ₁*) of effective charge tensor for Ti"
          },
          "zeta2_Ti": {
            "type": "number",
            "unit": "e",
            "description": "Second principal value (ζ₂*) of effective charge tensor for Ti"
          },
          "zeta3_Ti": {
            "type": "number",
            "unit": "e",
            "description": "Third principal value (ζ₃*) of effective charge tensor for Ti"
          },
          "zeta1_O": {
            "type": "number",
            "unit": "e",
            "description": "First principal value (ζ₁*) of effective charge tensor for O"
          },
          "zeta2_O": {
            "type": "number",
            "unit": "e",
            "description": "Second principal value (ζ₂*) of effective charge tensor for O"
          },
          "zeta3_O": {
            "type": "number",
            "unit": "e",
            "description": "Third principal value (ζ₃*) of effective charge tensor for O"
          }
        }
      },
      "description": "Contains the DFT-LDA and DFPT calculated results: relaxed lattice constants a and c (Å), internal oxygen parameter u, high-frequency dielectric constants ε∞ along a and c, Born effective charge tensor components for Ti and O, and principal values of the effective charge tensors."
    }
  ],
  "notes": "Scoring uses exact-match policy with relative tolerances (hidden) applied to each field against the paper's reference values. The DFPT step is load-bearing because its outputs depend on the correct relaxed geometry from the preceding relaxation step."
}
```

## How you are scored
A hidden verifier independently checks each scored workflow stage. For the file results.json, the verifier compares every numeric field against reference values using relative tolerances (the tolerances are hidden). The final reward is a weighted combination of these checks; the DFPT-calculated quantities carry the largest weight. Reporting values obtained from any other source does not give credit — you must execute the full structural relaxation and DFPT workflow to compute the numbers yourself.
