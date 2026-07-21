# Extract Exchange Coupling Constants from DFT Total Energies for MnO

## Problem background
Magnetic materials exhibit structural and magnetic phase transitions driven by spin interactions. First-principles density functional theory (DFT) can compute total energies of different collinear magnetic configurations. From these energies, pairwise exchange coupling constants (J1, J2) can be extracted by mapping the energy differences onto a Heisenberg spin Hamiltonian. The mean‑field Néel temperature is then estimated from these constants. This procedure is a foundational step for validating the accuracy of spin‑dependent machine learning potentials, as it confirms that the underlying DFT reference energies correctly capture magnetic ordering.

## Approach
The core idea is to perform spin‑polarized DFT calculations using the screened hybrid functional HSE06 on a cubic 2×2×2 supercell of MnO (64 atoms) at the experimental lattice constant a = 4.430 Å. Three collinear magnetic configurations are computed: ferromagnetic (FM), antiferromagnetic type I (AFM‑I), and antiferromagnetic type II (AFM‑II, the ground state with alternating ferromagnetic (111) planes). The total energy per atom for each configuration is extracted. These three energies are then used to solve for the nearest‑neighbor exchange constant J1 and the next‑nearest‑neighbor exchange constant J2 via standard Heisenberg mapping formulas (assuming spin S = 5/2 for the high‑spin Mn²⁺ ions). The mean‑field Néel temperature TN is subsequently calculated from J2 using the relation TN = –2 S(S+1) J2. The workflow separates cleanly into generating input structures, running the DFT calculations, and post‑processing the results—the steps detailed below.

## Reproduction target
Perform spin‑polarized HSE06 DFT calculations on a 2×2×2 supercell of cubic rock‑salt MnO (64 atoms) with lattice constant a = 4.430 Å for the three magnetic configurations: FM, AFM‑I, and AFM‑II. Extract the total energy per atom (in eV/atom) for each configuration. Using these energies and assuming spin S = 5/2 with Boltzmann constant k_B = 8.617333262×10⁻⁵ eV K⁻¹, compute the Heisenberg exchange coupling constants J1 and J2 (in Kelvin) and the mean‑field Néel temperature TN (in Kelvin). Report all quantities—the three total energies per atom, J1, J2, and TN—in the JSON file exchange_parameters.json according to the output contract. The hidden verifier will compare your derived J1, J2, and TN against independently established reference values.

## Assets

- Spin-polarized DFT code with HSE06 functional (e.g., Quantum ESPRESSO, ABINIT, GPAW, SIESTA): https://www.quantum-espresso.org
- Cubic rock-salt MnO crystal structure

## Workflow steps

### Step 1: Prepare DFT input files for three magnetic configurations
- Role: process
- Action: Generate input files for a spin-polarized HSE06 DFT calculation of a 2×2×2 MnO supercell (64 atoms) at the experimental lattice constant a = 4.430 Å for three magnetic orders: ferromagnetic (FM), antiferromagnetic type I (AFM-I), and antiferromagnetic type II (AFM-II). The AFM-II ordering is the ground state with alternating ferromagnetic (111) planes; AFM-I is a different antiferromagnetic pattern. Set appropriate spin orientations for each configuration.
- Evidence: `/app/outputs/dft_inputs.log`

### Step 2: Run HSE06 DFT calculations
- Role: process
- Action: Execute the three spin-polarized HSE06 self-consistent-field calculations using the prepared input files. Converge total energies to at least 10⁻⁶ eV. Extract the total energy per atom for each configuration (E_FM, E_AFM-I, E_AFM-II).
- Evidence: `/app/outputs/dft_outputs.log`

### Step 3: Derive exchange parameters and Néel temperature
- Role: scored (load-bearing)
- Action: Using the three total energies per atom, compute the exchange coupling constants J1 and J2 via the standard Heisenberg mapping formulas for the rock-salt antiferromagnet (with spin S = 5/2 and Boltzmann constant k_B), and compute the mean-field Néel temperature TN from J2. Write the three total energies per atom (in eV/atom) and the derived J1, J2 (in Kelvin), and TN (in Kelvin) to exchange_parameters.json.
- Output file: `/app/outputs/exchange_parameters.json`
- Format: json
- Contract: {"type": "object", "required": ["E_FM_per_atom", "E_AFM_I_per_atom", "E_AFM_II_per_atom", "J1", "J2", "TN"], "properties": {"E_FM_per_atom": {"type": "number", "unit": "eV/atom"}, "E_AFM_I_per_atom": {"type": "number", "unit": "eV/atom"}, "E_AFM_II_per_atom": {"type": "number", "unit": "eV/atom"}, "J1": {"type": "number", "unit": "K"}, "J2": {"type": "number", "unit": "K"}, "TN": {"type": "number", "unit": "K"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_parameters.json
- path: `/app/outputs/exchange_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON containing the DFT total energies per atom for the three magnetic configurations and the derived Heisenberg exchange constants J1, J2 (K) and mean-field Néel temperature TN (K). All values are scalars.
- schema:
  - `type`: object
  - `required`: `E_FM_per_atom`, `E_AFM_I_per_atom`, `E_AFM_II_per_atom`, `J1`, `J2`, `TN`
  - `properties`:
    - `E_FM_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `E_AFM_I_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `E_AFM_II_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `J1`:
      - `type`: number
      - `unit`: K
    - `J2`:
      - `type`: number
      - `unit`: K
    - `TN`:
      - `type`: number
      - `unit`: K

Notes: The checker will compare the agent's reported J1, J2, and TN against hidden reference values from the paper using a tolerance suitable for DFT re-runs with a different code base.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "E_FM_per_atom",
          "E_AFM_I_per_atom",
          "E_AFM_II_per_atom",
          "J1",
          "J2",
          "TN"
        ],
        "properties": {
          "E_FM_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "E_AFM_I_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "E_AFM_II_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "J1": {
            "type": "number",
            "unit": "K"
          },
          "J2": {
            "type": "number",
            "unit": "K"
          },
          "TN": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "JSON containing the DFT total energies per atom for the three magnetic configurations and the derived Heisenberg exchange constants J1, J2 (K) and mean-field Néel temperature TN (K). All values are scalars."
    }
  ],
  "notes": "The checker will compare the agent's reported J1, J2, and TN against hidden reference values from the paper using a tolerance suitable for DFT re-runs with a different code base."
}
```

## How you are scored
A hidden verifier reads your exchange_parameters.json file, validates its structure, and then compares your reported J1, J2, and TN to reference values using predefined tolerances. The final reward is a weighted sum of these comparisons. Simply copying numbers from a paper does not satisfy the task; the verifier checks that the submitted values are physically correct and derive from a proper DFT workflow. Each workflow stage is audited by the verifier's automated checks, and the overall score reflects the quality of all scored artifacts.
