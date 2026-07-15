# DFT-based phonon transport and elastic properties of cubic graphene

## Problem background
Cubic graphene is a three-dimensional carbon allotrope formed entirely of sp²-hybridized carbon atoms, arranged in a hollow crystal structure with space group Pn-3m. Understanding its ability to conduct heat is critical for potential applications in thermal management and thermoelectrics. In this task, we use first-principles density functional theory (DFT) and the phonon Boltzmann transport equation (PBTE) to determine how efficiently cubic graphene transports heat at room temperature, characterize its mechanical response through elastic constants and derived moduli, and identify its Raman-active vibrational fingerprints.

## Approach
We model phonon transport from the ground up using open-source DFT and lattice-dynamics tools. The approach works in three stages: (1) Relax the cubic graphene crystal with Quantum ESPRESSO using the GGA-PBE exchange-correlation functional to obtain the equilibrium geometry. (2) Compute the harmonic (second-order) force constants, verify dynamical stability through the phonon dispersion, and calculate anharmonic (third-order) force constants via finite displacements — all with Phonopy. (3) Feed the force constants into ShengBTE to solve the full phonon Boltzmann transport equation and extract the isotropic lattice thermal conductivity at 300 K. In parallel, compute the single-crystal elastic stiffness constants (C11, C12, C44) from stress-strain calculations and derive polycrystalline moduli (bulk, shear, Young’s moduli, Poisson’s ratio) using Voigt–Reuss–Hill averaging. Finally, obtain the frequencies of the three Raman-active modes (T2g, A1g, Eg) at the Γ point from the harmonic phonon results, using either direct eigenvector analysis or the Phonopy-Spectroscopy tool. The reference material is diamond, whose known thermal and elastic properties serve as a baseline for interpreting the results.

## Reproduction target
Produce the following quantities for cubic graphene, all computed from a full re-run of the workflow (not from pre-existing data):
- Lattice thermal conductivity at 300 K (in W/mK).
- Single-crystal elastic constants C11, C12, C44 (in GPa).
- Polycrystalline elastic moduli derived via Voigt–Reuss–Hill averaging: bulk modulus B, shear modulus G, Young’s modulus E, and Poisson’s ratio ν (all in GPa, ν dimensionless).
- Raman-active phonon mode frequencies: the T2g, A1g, and Eg modes at the Γ point (in cm⁻¹).
Each quantity must be written to its designated text file following the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- ShengBTE: https://www.shengbte.org/
- Phonopy-Spectroscopy: https://github.com/JMSkelton/Phonopy-Spectroscopy
- Carbon pseudopotential (PBE, SSSP library)
- Cubic graphene crystal structure description

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Relax the cubic graphene crystal structure using Quantum ESPRESSO with GGA-PBE to obtain the equilibrium lattice constant and atomic positions.
- Evidence: `/app/outputs/relax.log`

### Step 2: Harmonic force constants and phonon dispersion
- Role: process
- Action: Compute harmonic (second-order) interatomic force constants and phonon dispersion using Phonopy with finite displacements or DFPT on a 2x2x2 supercell, and verify dynamical stability (no imaginary modes).
- Evidence: `/app/outputs/harmonic_ifcs.log`

### Step 3: Anharmonic (third-order) force constants
- Role: process
- Action: Compute anharmonic (third-order) force constants using finite displacements on a 2x2x2 supercell, applying translational invariance constraints.
- Evidence: `/app/outputs/anharmonic_ifcs.log`

### Step 4: Lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Run ShengBTE with the harmonic and anharmonic IFCs to solve the phonon Boltzmann transport equation, extract the isotropic lattice thermal conductivity at 300 K, and write the numeric value.
- Output file: `/app/outputs/thermal_conductivity_300K.txt`
- Format: txt
- Contract: A single floating-point number on one line, representing the isotropic lattice thermal conductivity in W/mK.
- Scoring: scored by hidden verifier

### Step 5: Elastic constants
- Role: scored
- Action: Compute the single-crystal elastic stiffness constants C11, C12, C44 (GPa) for the relaxed cubic structure, e.g., via stress-strain method in Quantum ESPRESSO. Write the three values.
- Output file: `/app/outputs/elastic_constants.txt`
- Format: txt
- Contract: Three space-separated floating-point numbers: C11 C12 C44 (GPa).
- Scoring: scored by hidden verifier

### Step 6: Elastic moduli (Voigt–Reuss–Hill)
- Role: scored
- Action: From the elastic constants, derive polycrystalline bulk modulus B, shear modulus G, Young’s modulus E, and Poisson’s ratio ν using Voigt–Reuss–Hill averaging formulas. Write the four values.
- Output file: `/app/outputs/elastic_moduli.txt`
- Format: txt
- Contract: Four space-separated floats: BulkModulus (GPa) ShearModulus (GPa) YoungsModulus (GPa) PoissonRatio.
- Scoring: scored by hidden verifier

### Step 7: Raman-active phonon frequencies
- Role: scored
- Action: Using the harmonic phonon data and a Raman spectrum tool (e.g., Phonopy-Spectroscopy or direct Γ-point analysis), extract the frequencies of the Raman-active modes T2g, A1g, Eg at the Γ point in cm⁻¹. Write the three frequencies.
- Output file: `/app/outputs/raman_frequencies.txt`
- Format: txt
- Contract: Three space-separated floats: f_T2g f_A1g f_Eg (cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_300K.txt`
- `/app/outputs/elastic_constants.txt`
- `/app/outputs/elastic_moduli.txt`
- `/app/outputs/raman_frequencies.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_300K.txt
- path: `/app/outputs/thermal_conductivity_300K.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity of cubic graphene at 300 K.
- schema:
  - `type`: text
  - `description`: A single floating-point number in W/mK.

### elastic_constants.txt
- path: `/app/outputs/elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic stiffness constants.
- schema:
  - `type`: text
  - `description`: Three space-separated floats: C11 C12 C44 (GPa).

### elastic_moduli.txt
- path: `/app/outputs/elastic_moduli.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Polycrystalline elastic moduli from Voigt–Reuss–Hill averaging.
- schema:
  - `type`: text
  - `description`: Four space-separated floats: B(GPa) G(GPa) E(GPa) ν(dimensionless).

### raman_frequencies.txt
- path: `/app/outputs/raman_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Raman-active phonon mode frequencies at the Γ point.
- schema:
  - `type`: text
  - `description`: Three space-separated floats: T2g A1g Eg frequencies (cm⁻¹).

Notes: All scoring uses result-level comparison against paper reference values with appropriate tolerances for a DFT re-run.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number in W/mK."
      },
      "description": "Lattice thermal conductivity of cubic graphene at 300 K."
    },
    {
      "file": "elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Three space-separated floats: C11 C12 C44 (GPa)."
      },
      "description": "Single-crystal elastic stiffness constants."
    },
    {
      "file": "elastic_moduli.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Four space-separated floats: B(GPa) G(GPa) E(GPa) ν(dimensionless)."
      },
      "description": "Polycrystalline elastic moduli from Voigt–Reuss–Hill averaging."
    },
    {
      "file": "raman_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Three space-separated floats: T2g A1g Eg frequencies (cm⁻¹)."
      },
      "description": "Raman-active phonon mode frequencies at the Γ point."
    }
  ],
  "notes": "All scoring uses result-level comparison against paper reference values with appropriate tolerances for a DFT re-run."
}
```

## How you are scored
A hidden verifier inspects the four scored output files: thermal_conductivity_300K.txt, elastic_constants.txt, elastic_moduli.txt, and raman_frequencies.txt. For each file, the verifier reads the numeric values and compares them against reference values obtained from the original study, applying tolerances that account for legitimate differences arising from the use of a different DFT code (Quantum ESPRESSO instead of VASP) and normal computational spread. Each of the four artifacts contributes a quarter of the total reward; the magnitude of the reward decays smoothly from full credit when the reported result is within the expected tolerance, to zero for completely incorrect values. Reporting the paper’s numbers without executing the underlying calculations will not pass, because the verifier enforces a check that rewards only results consistent with a genuine re-run of the prescribed computational pipeline.
