# Isosteric Heat of Adsorption for Polar Molecules on Graphite via Static Molecular Simulation

## Problem background
The isosteric heat of adsorption at zero surface coverage, denoted \(q_{\mathrm{st}}^\mathrm{o}\), quantifies the interaction strength between a single adsorbate molecule and an adsorbent surface in the limit of negligible adsorbate–adsorbate interactions. For polar molecules such as water, ammonia, methanol, and ethanol on graphitic carbon materials, this quantity reveals the hydrophilic/hydrophobic character of the surface and is crucial for designing carbon adsorbents for adsorption cooling and gas separation. A static molecular simulation that combines multiple interaction potentials (Lennard‑Jones dispersion/repulsion, electrostatic dipole‑quadrupole interactions, and polarisation‑induced dipole effects) can predict \(q_{\mathrm{st}}^\mathrm{o}\) as a function of slit‑pore width without requiring expensive Monte Carlo or molecular dynamics runs. The present task implements such a model to compute \(q_{\mathrm{st}}^\mathrm{o}(H)\) for four polar adsorbates on a graphite slit pore.

## Approach
The calculation proceeds in three conceptual stages:

1. **Construction of the graphite slab** – A simulation box containing 10 layers of a hexagonal graphite lattice is built. Each layer comprises 41×41 carbon atoms. The in‑plane C–C bond length is 1.421 Å and the interlayer spacing is 3.354 Å. The surface is large enough that the adsorbate experiences a bulk‑like interaction when positioned near the centre of the slab.

2. **Molecule–surface interaction potential** – For a given adsorbate molecule held in a fixed orientation, the total interaction energy \(U_{\mathrm{mM}}(z)\) as a function of the perpendicular distance \(z\) between the molecule’s centre of mass and the topmost graphitic layer is evaluated. Three physical contributions are summed:
   - **Anisotropic Lennard‑Jones (LJ) potential** – Pairwise additive over all carbon atoms, with site‑site well depths \(\varepsilon_{ij}\) and collision diameters \(\sigma_{ij}\) obtained from Lorentz–Berthelot combining rules, and anisotropy coefficients \(\gamma_{\mathrm{A}}\) (attraction) and \(\gamma_{\mathrm{R}}\) (repulsion) that depend on the angle between the inter‑site vector and the graphite surface normal.
   - **Electrostatic potential** – The interaction between the permanent dipole and quadrupole moments of the adsorbate and the electric field (and field gradient) produced by the carbon atoms. A screening factor of 1 is used for the first carbon layer and \(2/(2.8+1)\) for deeper layers.
   - **Dipole‑induction potential** – The mutual polarisation of the adsorbate molecule and the carbon atoms, computed from their polarisability tensors and the electric fields created by permanent and induced dipoles.

   The evaluation is performed for \(z\) ranging from 2 Å to 10 Å at a resolution sufficient to capture the well depth.

3. **Slit‑pore model and isosteric heat** – The external potential in a slit pore of width \(H\) is given by \(V_{\mathrm{ext}}(z)=U_{\mathrm{mM}}(z)+U_{\mathrm{mM}}(H-z)\), where \(H\) is the effective pore width corrected for the carbon atom size. The isosteric heat of adsorption at zero coverage is calculated from Henry’s law:
   \[
   q_{\mathrm{st}}^\mathrm{o} = kT - \frac{\int_0^H V_{\mathrm{ext}}(z)\,\exp[-V_{\mathrm{ext}}(z)/kT]\,\mathrm{d}z}{\int_0^H \exp[-V_{\mathrm{ext}}(z)/kT]\,\mathrm{d}z},
   \]
   with \(T=300\,\mathrm{K}\) and \(k\) the Boltzmann constant. The integration is repeated for \(H\) from 2 Å to 10 Å to yield the \(q_{\mathrm{st}}^\mathrm{o}(H)\) curve.

**Required parameters** – The LJ parameters (well depth \(\varepsilon\), collision diameter \(\sigma\), and anisotropy coefficients \(\gamma_{\mathrm{A}},\gamma_{\mathrm{R}}\)) for the relevant atom pairs are:

| atom pair | \(\varepsilon\) (meV) | \(\sigma\) (Å) | \(\gamma_{\mathrm{A}}\) | \(\gamma_{\mathrm{R}}\) |
|-----------|------------------------|-------------------|---------------------------|---------------------------|
| C–H       | 2.265                  | 2.965             | 0.4                       | −0.54                     |
| C–C       | 2.981                  | 3.305             | 0.4                       | −1.05                     |
| C–N       | 2.811                  | 3.390             | 0.4                       | −1.05                     |
| C–O       | 3.450                  | 3.141             | 0.4                       | −1.05                     |

The electrostatic and induction parameters (dipole moments, polarisability tensor components, quadrupole moments) are:

| molecule | \(\mu\) (D) | \(\alpha_{xx}\) | \(\alpha_{yy}\) | \(\alpha_{zz}\) | \(\Theta_{xx}\) (D Å) | \(\Theta_{yy}\) (D Å) | \(\Theta_{zz}\) (D Å) |
|----------|-------------|-------------------|-------------------|-------------------|--------------------------|--------------------------|--------------------------|
| carbon   | –           | 1.44 Å³          | 1.44 Å³          | 0.41 Å³          | −0.5                     | −0.5                     | 1                        |
| water    | 1.855       | 1.53 Å³          | 1.42 Å³          | 1.47 Å³          | 2.63                     | −2.50                    | −0.13                    |
| ammonia  | 1.42        | 13.8 bohr³       | 13.8 bohr³       | 13.93 bohr³      | 1.16                     | 1.16                     | −2.32                    |
| methanol | 1.69        | 3.69 Å³          | 3.25 Å³          | 3.06 Å³          | (neglected)              | (neglected)              | (neglected)              |
| ethanol  | 1.69        | 30.37 bohr³      | 33.61 bohr³      | 38.87 bohr³      | (neglected)              | (neglected)              | (neglected)              |

*Polarisability conversions:* 1 Å³ = 1.11265 × 10⁻⁴⁰ C·m²/V, 1 bohr³ = 1.648773 × 10⁻⁴¹ C·m²/V.

**Molecular geometries and orientations** (only the orientations required for the scored outputs are described):
- **Water (orientation 1):** Oxygen at the origin, one hydrogen lies on the \(X\)-axis, the H–O–H plane coincides with the \(XY\) plane (molecule parallel to the surface). O–H bond length 0.95728 Å, H–O–H angle 104.5°. Partial charges: H = +0.4238 e, O = −0.8476 e.
- **Ammonia (orientation 2):** N at the origin; molecule is rotated +90° about the \(X\)-axis so that one N–H bond points toward the surface. N–H bond length 1.017 Å, H–N–H angle 107°.
- **Methanol (orientation 2):** The C–O bond lies parallel to the surface; the whole CH₃OH molecule is rotated +90° about the \(X\)-axis. Use standard bond lengths and angles for methanol (C–O ≈ 1.43 Å, O–H ≈ 0.96 Å, tetrahedral geometry).
- **Ethanol (orientation 3):** The C–C–O skeleton is parallel to the surface; the molecule is rotated −90° about the \(X\)-axis. Standard bond lengths and angles for ethanol (C–C ≈ 1.54 Å, C–O ≈ 1.43 Å, O–H ≈ 0.96 Å, tetrahedral geometry).

*Note:* Only the LJ, electrostatic, and induction interactions between the adsorbate and the graphite slab are considered; adsorbate–adsorbate interactions are negligible at zero coverage.

## Reproduction target
Using the static molecular simulation described above, compute the isosteric heat of adsorption at zero coverage, \(q_{\mathrm{st}}^\mathrm{o}\), as a function of slit pore width \(H\) (in Å) for four polar molecules on graphite at \(T = 300\,\mathrm{K}\). The required molecule–orientation pairs are:

- **Water** orientation 1
- **Ammonia** orientation 2
- **Methanol** orientation 2
- **Ethanol** orientation 3

For each molecule, produce a CSV file containing the computed \(q_{\mathrm{st}}^\mathrm{o}(H)\) curve for \(H\) ranging from 2 Å to 10 Å (a regular sampling with at least 80 points is recommended). The CSV must have two columns: `H (Å)` and `q_st^o (eV)`. The files must be written to:

- `/app/outputs/water_qst.csv`
- `/app/outputs/ammonia_qst.csv`
- `/app/outputs/methanol_qst.csv`
- `/app/outputs/ethanol_qst.csv`

No other output files are required for scoring.

## Assets

- Graphite lattice structure
- Interaction parameters

## Workflow steps

### Step 1: System setup
- Role: process
- Action: Construct the graphite slab (10 layers, 41×41 carbon atoms per layer with the hexagonal lattice) and define the molecular geometries and the required orientations: water orientation 1, ammonia orientation 2, methanol orientation 2, ethanol orientation 3. Assemble all interaction parameters (Lennard‑Jones, electrostatic, induction) from the provided tables.
- Evidence: none

### Step 2: Compute interaction potentials
- Role: process
- Action: For each molecule in the specified orientation, compute the Lennard‑Jones potential (anisotropic correction form), the electrostatic potential (dipole and quadrupole contributions), and the induction potential (dipole‑induced dipole) as a function of the molecule–surface distance z from 2 Å to 10 Å. Sum them to obtain the total interaction potential U_mM(z) for each molecule.
- Evidence: `/app/outputs/potential_curves.npy`

### Step 3: Compute isosteric heat for water
- Role: scored (load-bearing)
- Action: For water (orientation 1), construct the external slit‑pore potential V_ext(z) = U_mM(z) + U_mM(H−z), and compute the isosteric heat of adsorption at zero coverage (q_st^o) at T = 300 K by numerical integration of the Henry’s law expression for H from 2 Å to 10 Å. Write the results to water_qst.csv.
- Output file: `/app/outputs/water_qst.csv`
- Format: csv
- Contract: {"type": "table", "columns": [{"name": "H (Å)", "type": "float"}, {"name": "q_st^o (eV)", "type": "float"}]}
- Scoring: scored by hidden verifier

### Step 4: Compute isosteric heat for ammonia
- Role: scored (load-bearing)
- Action: For ammonia (orientation 2), construct V_ext(z) and compute q_st^o at T = 300 K for H from 2 Å to 10 Å; write to ammonia_qst.csv.
- Output file: `/app/outputs/ammonia_qst.csv`
- Format: csv
- Contract: {"type": "table", "columns": [{"name": "H (Å)", "type": "float"}, {"name": "q_st^o (eV)", "type": "float"}]}
- Scoring: scored by hidden verifier

### Step 5: Compute isosteric heat for methanol
- Role: scored (load-bearing)
- Action: For methanol (orientation 2), construct V_ext(z) and compute q_st^o at T = 300 K for H from 2 Å to 10 Å; write to methanol_qst.csv.
- Output file: `/app/outputs/methanol_qst.csv`
- Format: csv
- Contract: {"type": "table", "columns": [{"name": "H (Å)", "type": "float"}, {"name": "q_st^o (eV)", "type": "float"}]}
- Scoring: scored by hidden verifier

### Step 6: Compute isosteric heat for ethanol
- Role: scored (load-bearing)
- Action: For ethanol (orientation 3), construct V_ext(z) and compute q_st^o at T = 300 K for H from 2 Å to 10 Å; write to ethanol_qst.csv.
- Output file: `/app/outputs/ethanol_qst.csv`
- Format: csv
- Contract: {"type": "table", "columns": [{"name": "H (Å)", "type": "float"}, {"name": "q_st^o (eV)", "type": "float"}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/water_qst.csv`
- `/app/outputs/ammonia_qst.csv`
- `/app/outputs/methanol_qst.csv`
- `/app/outputs/ethanol_qst.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### water_qst.csv
- path: `/app/outputs/water_qst.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Isosteric heat of adsorption at zero coverage for water (orientation 1) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `H (Å)`, `q_st^o (eV)`

### ammonia_qst.csv
- path: `/app/outputs/ammonia_qst.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Isosteric heat of adsorption at zero coverage for ammonia (orientation 2) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `H (Å)`, `q_st^o (eV)`

### methanol_qst.csv
- path: `/app/outputs/methanol_qst.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Isosteric heat of adsorption at zero coverage for methanol (orientation 2) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `H (Å)`, `q_st^o (eV)`

### ethanol_qst.csv
- path: `/app/outputs/ethanol_qst.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Isosteric heat of adsorption at zero coverage for ethanol (orientation 3) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `H (Å)`, `q_st^o (eV)`

Notes: Each CSV must contain at least one row. The hidden checker will extract the maximum q_st^o and the associated H value for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "water_qst.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H (Å)",
          "q_st^o (eV)"
        ]
      },
      "description": "Isosteric heat of adsorption at zero coverage for water (orientation 1) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference."
    },
    {
      "file": "ammonia_qst.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H (Å)",
          "q_st^o (eV)"
        ]
      },
      "description": "Isosteric heat of adsorption at zero coverage for ammonia (orientation 2) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference."
    },
    {
      "file": "methanol_qst.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H (Å)",
          "q_st^o (eV)"
        ]
      },
      "description": "Isosteric heat of adsorption at zero coverage for methanol (orientation 2) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference."
    },
    {
      "file": "ethanol_qst.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H (Å)",
          "q_st^o (eV)"
        ]
      },
      "description": "Isosteric heat of adsorption at zero coverage for ethanol (orientation 3) on graphite slit pore. The maximum q_st^o and its corresponding H will be compared to a hidden reference."
    }
  ],
  "notes": "Each CSV must contain at least one row. The hidden checker will extract the maximum q_st^o and the associated H value for scoring."
}
```

## How you are scored
The submission is evaluated exclusively on the four CSV files listed above. A hidden verifier reads each file and performs the following checks:

1. **Maximum isosteric heat** – The maximum value of \(q_{\mathrm{st}}^\mathrm{o}\) in the file is extracted and compared to a hidden reference value for that molecule–orientation combination. The comparison uses an appropriate tolerance that accounts for numerical differences between independent implementations.

2. **Pore width at the maximum** – The value of \(H\) at which the maximum occurs is compared to a hidden expected range.

3. **Curve shape** – The \(q_{\mathrm{st}}^\mathrm{o}(H)\) curve must be unimodal (a single well‑defined peak) over the scanned \(H\) range.

A molecule passes if both the maximum heat and the peak position are within tolerance and the curve is unimodal. Each of the four molecules carries equal weight (0.25). The final reward is the fraction of molecules that pass all checks, reported as a number between 0 and 1. There is no partial credit per molecule beyond the pass/fail of these criteria.
