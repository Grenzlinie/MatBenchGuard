# Compute Elastic Constants and Debye Temperatures for Monovalent Metals

## Problem background
Monovalent metals such as Li, Na, K, and Cu owe their cohesive and elastic properties to a delicate balance between electrostatic interactions of the ionic cores plus valence electrons, and the short-ranged exchange (overlap) forces between closed electron shells. The Wigner–Seitz cellular method showed that for volume-preserving distortions the kinetic and Fermi energies of the valence electrons remain essentially unchanged, so that the change in energy arises solely from the electrostatic lattice energy and the exchange interaction between ions. This separation makes it possible to compute two independent shear elastic constants, A = c11 − c12 and 2B = c44, from first principles. Furthermore, using the full set of elastic constants, the low‑temperature Debye characteristic temperature Θ can be derived from the Born–Karman theory of lattice vibrations. The target is to reproduce these quantities for the four metals by implementing the required electrostatic sums, central‑force exchange formulas, and the Born–Karman sound‑velocity integration.

## Approach
The computation proceeds in four conceptual stages, all of which are purely numerical and can be carried out with standard linear‑algebra and summation routines.

1. **Electrostatic lattice contributions.** The energy of a lattice of point charges embedded in a uniform negative background is differentiated analytically for two volume‑preserving deformations (type A, an extension/compression along two axes, and type B, a pure shear). The result is expressed as an Ewald‑type double series over direct and reciprocal lattice vectors. Evaluating these series for the face‑centred cubic (FCC) and body‑centred cubic (BCC) structures gives the dimensionless electrostatic coefficients A^(l) and 2B^(l). These coefficients depend only on the crystal structure, not on the metal.

2. **Exchange interaction contributions.** Closed‑shell overlap and van der Waals interactions between ions are treated as central forces. For the alkali metals the repulsive part is modelled by a Born–Mayer potential, with parameters taken from the literature on ionic crystals, and the attractive part by a London r⁻⁶ term with known van der Waals coefficients. For copper the repulsive force derivatives are taken from a statistical‑atom calculation. Using the nearest‑neighbour and next‑nearest‑neighbour geometries of each structure, one evaluates the central‑force formulas for the same two distortion types, yielding per‑metal exchange contributions A^(I) and 2B^(I).

3. **Total elastic constants.** The electrostatic contributions are scaled from the dimensionless e²/(2δ) units to cgs units using the experimental lattice constant δ and fundamental constants. They are added to the exchange contributions to obtain the total A and 2B for each metal. Using the experimental compressibility (2C) provided below, the cubic‑symmetry relations c11 = (2C + 2A)/3 and c12 = (2C − A)/3 then give the complete set c11, c12, c44 = 2B.

4. **Debye temperatures.** For the alkali metals, the elastic constants are combined with the atomic density to construct the secular equation for long‑wavelength elastic waves. The harmonic mean sound velocity is computed by integrating the three sound velocities over all directions of propagation, following a series‑expansion method truncated at eighth order. The low‑temperature Debye temperature Θ is then obtained from the standard relation Θ = (h/k)(3/(4πΩ))^(1/3) v̄.

## Reproduction target
Produce the following quantities by running your own code, and write them to the specified JSON output files in the `/app/outputs` directory:

- **`electrostatic_contributions.json`** – the dimensionless electrostatic coefficients A^(l) and 2B^(l) for FCC and BCC crystals (units of e²/(2δ)).
- **`exchange_contributions.json`** – for each metal Li, Na, K, Cu, the total exchange interaction contributions A^(I) and 2B^(I) in cgs × 10¹¹, combining repulsive and van der Waals parts.
- **`total_elastic_constants.json`** – for each metal, the total elastic constants A = c11 − c12, 2B = c44, c11, and c12, all in cgs × 10¹¹, derived from the electrostatic, exchange, and compressibility inputs.
- **`debye_temperatures.json`** – for Li, Na, and K, the low‑temperature Debye characteristic temperature Θ in Kelvin, computed from the elastic constants via the Born–Karman theory.

The required experimental lattice constants, compressibilities, interionic potential parameters, and copper force derivatives are listed in the `## Assets` section below. Your code must read these values and implement the Ewald‑sum, central‑force, and harmonic‑mean‑velocity calculations without using any pre‑computed look‑up tables for the electrostatic coefficients or the Debye integral.

## Assets

### Software packages
- numpy: numpy
- scipy: scipy

### Physical constants and input data
- Lattice constants δ (in 10⁻⁸ cm):
  - Li: 3.40 (BCC)
  - Na: 4.22 (BCC)
  - K: 5.15 (BCC)
  - Cu: 3.60 (FCC)
- Compressibilities 2C (in 10¹¹ cgs):
  - Li: 1.30
  - Na: 0.85
  - K: 0.40
  - Cu: 14.1 (theoretical value used in the paper)
- Atomic weights (g mol⁻¹): Li=6.94, Na=22.99, K=39.10, Cu=63.55.
- Avogadro number N_A = 6.02214076 × 10²³ mol⁻¹.
- Fundamental constants:
  - Electron charge (esu) e = 4.8032047 × 10⁻¹⁰
  - Planck constant h = 6.62607015 × 10⁻²⁷ erg s
  - Boltzmann constant k = 1.380649 × 10⁻¹⁶ erg K⁻¹
  - Bohr radius a₀ = 0.529177210903 × 10⁻⁸ cm
  - Rydberg energy R = e²/(2a₀) = 2.1798741 × 10⁻¹¹ erg
- Repulsive potential parameters (Born–Mayer):
  - b = 1.0 × 10⁻¹² erg
  - ρ = 0.345 × 10⁻⁸ cm
  - Ionic radii rᵢ (cm):
    - Li: 0.475 × 10⁻⁸
    - Na: 0.875 × 10⁻⁸
    - K: 1.185 × 10⁻⁸
  - Pauling factor C₁₂:
    - Li: 2.00
    - Na: 1.25
    - K: 1.25
- van der Waals coefficients c (erg cm⁶):
  - Li: 0.55 × 10⁻⁶⁰
  - Na: 2.5 × 10⁻⁶⁰
  - K: 30 × 10⁻⁶⁰
- For Cu, repulsive force derivatives (per ion pair):
  - dw/dr = –0.0051 R a₀⁻¹
  - d²w/dr² = 0.018 R a₀⁻²
  (Use the provided R and a₀ to convert to cgs; the van der Waals interaction for Cu is negligible.)

## Workflow steps

### Step 1: Collect experimental input data
- Role: process
- Action: Extract from the provided instruction the experimental lattice constants (δ), compressibilities (2C), interionic repulsive potential parameters (b, ρ, ionic radii), van der Waals coefficients (c), and repulsive-force derivatives for Cu. Tabulate them for use by subsequent steps. This step is documentation and preparation; no scored output.
- Evidence: none

### Step 2: Compute Electrostatic Lattice Contributions
- Role: scored
- Action: Using the Ewald‑summation second‑derivative formulas for volume‑preserving distortions (type A and B), compute the dimensionless electrostatic coefficients A^(l) and 2B^(l) for the face‑centred cubic (fcc) and body‑centred cubic (bcc) crystal structures. These values are independent of the specific metal and represent the total electrostatic contribution per atom in units of e²/(2δ). The result must match the known values for these structures within numerical precision.
- Output file: `/app/outputs/electrostatic_contributions.json`
- Format: json
- Contract: { "fcc": {"A_l": float, "2B_l": float}, "bcc": {"A_l": float, "2B_l": float} }
- Scoring: scored by hidden verifier

### Step 3: Compute Exchange Interaction Contributions
- Role: scored
- Action: For each metal (Li, Na, K, Cu), compute the exchange contributions A^(I) and 2B^(I) arising from closed‑shell interionic potentials (repulsive Born‑Mayer and attractive van der Waals forces). Use the central‑force formulas, the nearest‑neighbour distances derived from the experimental lattice constants, and the potential parameters (for alkalis: Born‑Mayer and London values; for copper: the repulsive force derivatives). Combine repulsive and van der Waals parts into total A^(I) and 2B^(I) for each metal, expressed in cgs units (×10^11).
- Output file: `/app/outputs/exchange_contributions.json`
- Format: json
- Contract: [{"metal": "Li", "A_I": float, "2B_I": float}, {"metal": "Na", "A_I": float, "2B_I": float}, {"metal": "K", "A_I": float, "2B_I": float}, {"metal": "Cu", "A_I": float, "2B_I": float}]
- Scoring: scored by hidden verifier

### Step 4: Assemble Total Elastic Constants
- Role: scored (load-bearing)
- Action: For each metal, combine the electrostatic contributions (scaled to cgs units using the experimental lattice constant δ) with the exchange contributions to obtain the total A = c11 − c12 and 2B = c44. Then, using the experimental compressibility 2C (provided in the instruction), solve for c11 and c12 via the cubic‑symmetry relations. Report all values in cgs units × 10^11.
- Output file: `/app/outputs/total_elastic_constants.json`
- Format: json
- Contract: [{"metal": "Li", "A": float, "2B": float, "c11": float, "c12": float}, {"metal": "Na", "A": float, "2B": float, "c11": float, "c12": float}, {"metal": "K", "A": float, "2B": float, "c11": float, "c12": float}, {"metal": "Cu", "A": float, "2B": float, "c11": float, "c12": float}]
- Scoring: scored by hidden verifier

### Step 5: Compute Debye Characteristic Temperatures
- Role: scored
- Action: For the alkali metals (Li, Na, K), use the full set of elastic constants from the previous step and the atomic density (derived from atomic weight and lattice constant) to compute the low‑temperature Debye temperature Θ via the Born‑Karman theory. Evaluate the harmonic mean sound velocity using the direction‑resolved elastic wave equations and the provided power‑series expansion for the angular integral, then apply the standard formula for Θ. Report Θ in Kelvin.
- Output file: `/app/outputs/debye_temperatures.json`
- Format: json
- Contract: [{"metal": "Li", "Theta": float}, {"metal": "Na", "Theta": float}, {"metal": "K", "Theta": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electrostatic_contributions.json`
- `/app/outputs/exchange_contributions.json`
- `/app/outputs/total_elastic_constants.json`
- `/app/outputs/debye_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electrostatic_contributions.json
- path: `/app/outputs/electrostatic_contributions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dimensionless electrostatic coefficients A^(l) and 2B^(l) for FCC and BCC crystal structures, in units of e²/(2δ). The checker compares these values to known reference values for these structures.
- schema:
  - `type`: object
  - `required_keys`: `fcc`, `bcc`
  - `fcc`:
    - `type`: object
    - `required_keys`: `A_l`, `2B_l`
  - `bcc`:
    - `type`: object
    - `required_keys`: `A_l`, `2B_l`

### exchange_contributions.json
- path: `/app/outputs/exchange_contributions.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Per‑metal exchange interaction contributions A^(I) and 2B^(I) in cgs × 10^11. Each entry gives the total exchange part (repulsive + van der Waals) for one metal. Checker compares against paper's Table V with relative tolerance; meeting or beating a quality threshold is accepted.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required_keys`: `metal`, `A_I`, `2B_I`

### total_elastic_constants.json
- path: `/app/outputs/total_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Total elastic constants A = c11−c12, 2B = c44, c11, c12 for each metal, in cgs × 10^11. Values are derived from electrostatic, exchange and compressibility inputs. Checker compares to paper's Table IV with relative tolerance, and internally verifies consistency with the preceding step outputs.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required_keys`: `metal`, `A`, `2B`, `c11`, `c12`

### debye_temperatures.json
- path: `/app/outputs/debye_temperatures.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Debye characteristic temperatures Θ for Li, Na, K in Kelvin. Derived from elastic constants via Born‑Karman theory. Checker compares to paper's Table VI with relative tolerance; threshold‑or‑better scoring ensures a better‑than‑paper result is not penalised.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required_keys`: `metal`, `Theta`

Notes: Scored quantities: electrostatic coefficients, exchange contributions, total elastic constants, and Debye temperatures. Tolerances are set based on expected numerical spread from different Ewald summation implementations and potential parameter choices. The load‑bearing step is total_elastic_constants, as it requires genuine execution of the two compute stages it combines.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electrostatic_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "fcc",
          "bcc"
        ],
        "fcc": {
          "type": "object",
          "required_keys": [
            "A_l",
            "2B_l"
          ]
        },
        "bcc": {
          "type": "object",
          "required_keys": [
            "A_l",
            "2B_l"
          ]
        }
      },
      "description": "Dimensionless electrostatic coefficients A^(l) and 2B^(l) for FCC and BCC crystal structures, in units of e²/(2δ). The checker compares these values to known reference values for these structures."
    },
    {
      "file": "exchange_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required_keys": [
            "metal",
            "A_I",
            "2B_I"
          ]
        }
      },
      "description": "Per‑metal exchange interaction contributions A^(I) and 2B^(I) in cgs × 10^11. Each entry gives the total exchange part (repulsive + van der Waals) for one metal. Checker compares against paper's Table V with relative tolerance; meeting or beating a quality threshold is accepted."
    },
    {
      "file": "total_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required_keys": [
            "metal",
            "A",
            "2B",
            "c11",
            "c12"
          ]
        }
      },
      "description": "Total elastic constants A = c11−c12, 2B = c44, c11, c12 for each metal, in cgs × 10^11. Values are derived from electrostatic, exchange and compressibility inputs. Checker compares to paper's Table IV with relative tolerance, and internally verifies consistency with the preceding step outputs."
    },
    {
      "file": "debye_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required_keys": [
            "metal",
            "Theta"
          ]
        }
      },
      "description": "Debye characteristic temperatures Θ for Li, Na, K in Kelvin. Derived from elastic constants via Born‑Karman theory. Checker compares to paper's Table VI with relative tolerance; threshold‑or‑better scoring ensures a better‑than‑paper result is not penalised."
    }
  ],
  "notes": "Scored quantities: electrostatic coefficients, exchange contributions, total elastic constants, and Debye temperatures. Tolerances are set based on expected numerical spread from different Ewald summation implementations and potential parameter choices. The load‑bearing step is total_elastic_constants, as it requires genuine execution of the two compute stages it combines."
}
```

## How you are scored
Your submission is evaluated by a hidden automatic verifier that inspects each of the four scored output files independently. The verifier does not simply look up a single number; it checks internal consistency and range plausibility. For example, it verifies that the total elastic constants can be reconstructed from the scaled electrostatic and exchange contributions, and that the Debye temperatures follow from the submitted elastic constants when the same Born–Karman procedure is applied. The final score is a weighted combination of the checks across all artifacts. Reporting numbers without genuine computation will result in low or zero credit, even if the numbers happen to be close to expected values.
