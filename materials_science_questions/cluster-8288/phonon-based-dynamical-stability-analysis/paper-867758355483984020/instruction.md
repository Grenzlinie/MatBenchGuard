# Phonon-based dynamical stability analysis of Heusler compounds

## Problem background
Heusler alloys crystallize in the cubic L2₁ structure (space group Fm-3m) and are of interest for magnetic shape-memory applications. The structural stability of the L2₁ phase is sensitive to composition and magnetic order. First-principles phonon dispersion calculations can reveal dynamical instabilities, manifested as imaginary phonon frequencies, that drive structural phase transitions. An additional anomaly—an inversion of the optical phonon modes—has been observed in some of these compounds. Reproducing the phonon dispersions along the [110] direction for a set of eight representative Heusler compounds allows one to classify each compound as dynamically stable or unstable and to investigate the optical-mode behaviour.

## Approach
Use spin-polarized density-functional theory (DFT) with a plane-wave basis and an appropriate exchange–correlation functional. For each compound, perform a variable-cell relaxation to obtain the theoretical lattice constant in the cubic L2₁ structure. Next, construct a 1×5×1 periodic supercell based on the conventional tetragonal cell (aₜ = a/√2, cₜ = a) with the long axis along [110]; this supercell contains ten consecutive (110) atomic planes. Displace each symmetrically independent atom by 0.03 Å along each Cartesian direction (±x, ±y, ±z) and compute the Hellmann–Feynman forces on all atoms via static DFT. From these forces, build the harmonic force-constant matrix, truncating the force constants beyond five atomic planes. Form the dynamical matrix for the five wave vectors along [110] given by q = [ζ, ζ, 0] with ζ = 0.0, 0.25, 0.5, 0.75, 1.0, and diagonalise it to obtain the phonon frequencies and eigenvectors. Identify the TA₂ branch (the lowest transverse acoustic mode with [1-10] polarisation) and the optical T₂g mode at Γ (the mode with [1-10] polarisation that involves only the atoms on the 8c Wyckoff sites).

## Reproduction target
For the eight compounds Ni₂MnGa, Ni₂MnAl, Ni₂MnIn, Ni₂MnGe, Co₂MnGa, Co₂MnGe, Ni₂TiGa, and Fe₂MnGa, compute the phonon frequencies along [110] at the reduced wave-vector coordinates ζ = 0.0, 0.25, 0.5, 0.75, 1.0. For each compound, report the frequencies of the TA₂ branch at these five ζ points and the frequency of the T₂g optical mode at the Γ point. A compound is classified as unstable if any TA₂ frequency is negative (imaginary); otherwise it is stable. The objective is to produce an accurate phonon_data.json file that contains these frequencies, from which the stability of each compound and the ordering of the optical mode can be inferred.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (PBE): https://www.quantum-espresso.org/pseudopotentials/
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT lattice optimization for each compound in L2₁ structure
- Role: process
- Action: For each of the eight Heusler compounds (Ni₂MnGa, Ni₂MnAl, Ni₂MnIn, Ni₂MnGe, Co₂MnGa, Co₂MnGe, Ni₂TiGa, Fe₂MnGa), set up the cubic L2₁ structure (space group Fm-3m, Wyckoff positions 4a (0,0,0) for Y, 4b (1/2,1/2,1/2) for Z, 8c (1/4,1/4,1/4) for X). Perform spin-polarized DFT variable-cell relaxation using PAW/GGA until forces are converged. Save the optimized lattice constant (a), total magnetic moment per formula unit, and magnetic order type.
- Evidence: `/app/outputs/lattice_constants.json`

### Step 2: Supercell displacement force calculations
- Role: process
- Action: For each compound, using the optimized lattice constant from step 1, construct a 1×5×1 periodic supercell based on the conventional tetragonal cell (aₜ = a/√2, cₜ = a) with the long axis along [110], containing ten consecutive (110) atomic planes. For each symmetrically independent atom, displace the atom by a small amplitude along each Cartesian direction (±x, ±y, ±z) and compute the Hellmann–Feynman forces on all atoms via static DFT. Store the displacement vectors and resulting force tensors for every atom.
- Evidence: `/app/outputs/forces_data.json`

### Step 3: Phonon dispersion analysis and output generation
- Role: scored (load-bearing)
- Action: From the stored forces, build the force-constant matrix within the harmonic approximation. Truncate force constants beyond five atomic planes (set to zero). Construct the dynamical matrix for the five allowed wave vectors along [110]: q = [ζ, ζ, 0] with ζ = 0.0, 0.25, 0.5, 0.75, 1.0. Diagonalize the dynamical matrix to obtain phonon frequencies and eigenvectors. Identify the TA₂ branch (lowest transverse acoustic mode with [1‑10] polarization) and extract its frequencies at each ζ. Identify the optical T₂g mode at Γ (the mode with [1‑10] polarization involving only the X atoms) and record its frequency. Write a single JSON file containing these results for all eight compounds.
- Output file: `/app/outputs/phonon_data.json`
- Format: json
- Contract: A JSON object where each key is a compound name (e.g., "Ni2MnGa"). The value is an object with: "zeta" (list of five floats), "TA2" (list of five floats; imaginary frequencies as negative values), and "T2g_at_Gamma" (float, frequency of the T₂g optical mode at ζ=0 in THz).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_data.json
- path: `/app/outputs/phonon_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Phonon dispersion data along [110] for all eight compounds, with TA₂ branch frequencies at five ζ points and the Γ-point T₂g optical mode frequency. The checker recomputes stability classification (compound unstable if any TA₂ frequency is negative) and the optical-mode anomaly trend, comparing against the paper's reported classification and T₂g ordering.
- schema:
  - `type`: object
  - `required`:
    - `<compound_name>`:
      - `zeta`: array of floats
      - `TA2`: array of floats
      - `T2g_at_Gamma`: float
  - `units`:
    - `zeta`: dimensionless
    - `TA2`: THz
    - `T2g_at_Gamma`: THz

Notes: The lattice constants and force data produced in earlier process steps are not scored but serve as evidence. The final scored artifact is phonon_data.json. The checker will recompute stability and trend from the frequencies, not from any self-reported classification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "<compound_name>": {
            "zeta": "array of floats",
            "TA2": "array of floats",
            "T2g_at_Gamma": "float"
          }
        },
        "units": {
          "zeta": "dimensionless",
          "TA2": "THz",
          "T2g_at_Gamma": "THz"
        }
      },
      "description": "Phonon dispersion data along [110] for all eight compounds, with TA₂ branch frequencies at five ζ points and the Γ-point T₂g optical mode frequency. The checker recomputes stability classification (compound unstable if any TA₂ frequency is negative) and the optical-mode anomaly trend, comparing against the paper's reported classification and T₂g ordering."
    }
  ],
  "notes": "The lattice constants and force data produced in earlier process steps are not scored but serve as evidence. The final scored artifact is phonon_data.json. The checker will recompute stability and trend from the frequencies, not from any self-reported classification."
}
```

## How you are scored
A hidden verifier reads your phonon_data.json. It extracts the TA₂ frequencies to determine the stability classification of each compound (unstable if any TA₂ frequency is negative). The verifier compares your stability assignments to a hidden reference and checks that the T₂g_at_Gamma frequency is lower in all unstable compounds than in all stable compounds. The final reward is based on the correctness of the stability labels and the consistency of the optical-mode trend. The exact tolerances and weighting are not disclosed.
