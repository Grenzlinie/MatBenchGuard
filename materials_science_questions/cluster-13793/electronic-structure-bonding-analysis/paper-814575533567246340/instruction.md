# Superconducting Transition Temperatures of Transition Metal Carbides

## Problem background
Transition metal carbides such as CrC and MoC are known for their extreme hardness, corrosion resistance and catalytic activity. This work systematically investigates the structural, electronic and mechanical properties of CrC and MoC using first-principles density functional theory, with a particular focus on their superconducting behaviour. The target is to compute the superconducting transition temperature (Tc) for the two compounds in the hexagonal WC phase and the cubic NaCl phase—quantities that reveal the potential of these materials as superconductors.

## Approach
The reproduction relies on a sequence of electronic-structure calculations. First, density functional theory (DFT) within the generalised gradient approximation is used to relax the crystal structures, compute the electronic density of states at the Fermi level \(N(E_F)\), and obtain the elastic constants. From the elastic constants, the Voigt‑Reuss‑Hill averaging scheme and Anderson’s method yield the Debye temperature \(\theta_D\), which sets the phonon frequency scale. Next, the tight‑binding linear muffin‑tin orbital (TB‑LMTO) method provides the electron‑phonon matrix elements and the Fermi‑surface‑averaged squared matrix element \(\langle I^2\rangle\). Using \(N(E_F)\), \(\langle I^2\rangle\), \(\theta_D\) and the atomic masses, the electron‑phonon coupling constant \(\lambda\) and the Coulomb parameter \(\mu^*\) are computed, and finally the superconducting transition temperature \(T_c\) is obtained from the Allen–Dynes McMillan formula. The workflow is applied independently to four systems: CrC and MoC, each in the WC (hexagonal) and NaCl (cubic) crystal structures.

## Reproduction target
Generate a single JSON file `tc_results.json` that, for each of the four compound/phase combinations—`CrC_WC`, `MoC_WC`, `CrC_NaCl`, `MoC_NaCl`—provides the three derived quantities: (i) superconducting transition temperature `Tc_K` (float, in kelvin), (ii) electron‑phonon coupling constant `lambda` (float), and (iii) effective Coulomb parameter `mu_star` (float). The file must adhere exactly to the JSON schema described in Step 6.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- TB-LMTO implementation

## Workflow steps

### Step 1: DFT structural optimization
- Role: process
- Action: For CrC and MoC in the WC and NaCl phases, run DFT geometry optimization using a GGA-PBE functional to obtain relaxed lattice constants and atomic positions. Record the equilibrium cell volumes and structures.
- Evidence: `/app/outputs/relaxed_structures.txt`

### Step 2: Electronic density of states
- Role: process
- Action: Using the relaxed structures, compute the total density of states (DOS) with a dense k‑point mesh. Extract the density of states at the Fermi level N(EF) in states/eV/unit cell for each compound and phase.
- Evidence: `/app/outputs/dos_n_ef.json`

### Step 3: Elastic constants
- Role: process
- Action: Compute the elastic constants (C11, C12, C44, C13, C33) for the WC and NaCl phases using the energy‑strain method with small symmetry‑adapted distortions of the relaxed cells.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 4: Debye temperature
- Role: process
- Action: Calculate the density of each structure and use the Voigt‑Reuss‑Hill averaged elastic moduli to compute longitudinal, transverse and average sound velocities, and finally the Debye temperature θD following Anderson’s method.
- Evidence: `/app/outputs/debye_temp.json`

### Step 5: LMTO electron–phonon matrix elements
- Role: process
- Action: Carry out tight‑binding LMTO calculations for the WC and NaCl phases of CrC and MoC. Evaluate the electron–phonon matrix elements M_{l,l+1} and compute the Fermi‑surface‑averaged squared electron–phonon matrix element ⟨I²⟩ using the formulas in the paper.
- Evidence: `/app/outputs/lmto_i2.json`

### Step 6: Superconducting parameter analysis
- Role: scored (load-bearing)
- Action: Combine N(EF) from step 2, ⟨I²⟩ from step 5, Debye temperature θD from step 4, and the atomic masses to compute: (a) electron–phonon coupling constant λ = N(EF)⟨I²⟩/(M⟨ω²⟩) with ⟨ω²⟩ = 0.5 θD², (b) effective electron–electron interaction parameter μ* = 0.26 N(EF)/(1+N(EF)), (c) superconducting transition temperature Tc via the Allen–Dynes McMillan formula. Perform this calculation for CrC and MoC in both the WC and NaCl phases. Write the results to tc_results.json.
- Output file: `/app/outputs/tc_results.json`
- Format: json
- Contract: JSON object with keys 'CrC_WC', 'MoC_WC', 'CrC_NaCl', 'MoC_NaCl', each containing 'Tc_K' (float), 'lambda' (float), 'mu_star' (float). Example: {"CrC_WC": {"Tc_K": 31.12, "lambda": 1.41, "mu_star": 0.091}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_results.json
- path: `/app/outputs/tc_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Superconducting transition temperatures Tc (K) and associated electron‑phonon coupling constant λ and Coulomb parameter μ* for CrC and MoC in the WC and NaCl phases.
- schema:
  - `type`: object
  - `required`:
    - `CrC_WC`:
      - `type`: object
      - `Tc_K`: float
      - `lambda`: float
      - `mu_star`: float
    - `MoC_WC`:
      - `type`: object
      - `Tc_K`: float
      - `lambda`: float
      - `mu_star`: float
    - `CrC_NaCl`:
      - `type`: object
      - `Tc_K`: float
      - `lambda`: float
      - `mu_star`: float
    - `MoC_NaCl`:
      - `type`: object
      - `Tc_K`: float
      - `lambda`: float
      - `mu_star`: float

Notes: The hidden checker compares the four reported Tc values to the paper‑reported ground truth with an absolute tolerance. The lambda and mu_star values are checked for internal consistency but are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CrC_WC": {
            "type": "object",
            "Tc_K": "float",
            "lambda": "float",
            "mu_star": "float"
          },
          "MoC_WC": {
            "type": "object",
            "Tc_K": "float",
            "lambda": "float",
            "mu_star": "float"
          },
          "CrC_NaCl": {
            "type": "object",
            "Tc_K": "float",
            "lambda": "float",
            "mu_star": "float"
          },
          "MoC_NaCl": {
            "type": "object",
            "Tc_K": "float",
            "lambda": "float",
            "mu_star": "float"
          }
        }
      },
      "description": "Superconducting transition temperatures Tc (K) and associated electron‑phonon coupling constant λ and Coulomb parameter μ* for CrC and MoC in the WC and NaCl phases."
    }
  ],
  "notes": "The hidden checker compares the four reported Tc values to the paper‑reported ground truth with an absolute tolerance. The lambda and mu_star values are checked for internal consistency but are not scored."
}
```

## How you are scored
A hidden verifier reads your `tc_results.json` and compares each reported `Tc_K` value against reference values. Your score is proportional to the number of these four Tc values that lie within the verifier’s hidden tolerance; each correct value earns 0.25 points, for a maximum reward of 1.0. The `lambda` and `mu_star` fields are checked for internal consistency with the workflow but are not directly scored. All preceding process steps must be correctly executed because the final Tc depends on them, but the intermediate evidence files (relaxed structures, DOS, elastic constants, Debye temperatures, LMTO matrix elements) are required only to document the workflow and are not individually scored.
