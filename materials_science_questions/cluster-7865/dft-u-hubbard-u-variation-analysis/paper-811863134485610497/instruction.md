# Spin Exchange Parameters and Cs 6p/6s DOS Ratio in Cs₂CuCl₄ via DFT+U

## Problem background
Cs₂CuCl₄ is a frustrated triangular antiferromagnet with four distinct Cu–Cl···Cl–Cu super-superexchange (SSE) paths (J₁–J₄) that would naively be expected to form a two-leg spin ladder dominated by J₁ and J₃ based on Cl···Cl contact distances. However, experimental evidence points to a two-dimensional triangular spin lattice governed instead by J₁ and J₂, raising the question of how the intervening Cs⁺ ions modify the exchange interactions. First-principles calculations suggest that the Cs 6p orbitals may selectively weaken J₁ and J₃ when the arrangement of CuCl₄²⁻ and Cs⁺ ions possesses mirror-plane or inversion symmetry, while J₂ and J₄ remain largely unaffected. The task is to compute the four SSE parameters for Cs₂CuCl₄ and for hypothetical A₂CuCl₄ (A = Rb, K, Na) by DFT+U, and to determine the ratio of integrated Cs 6p to Cs 6s partial density of states as a direct measure of 6p orbital involvement.

## Approach
Use an open-source DFT code with the GGA+U functional (U=6 eV on Cu d states) and the experimental room-temperature crystal structure of Cs₂CuCl₄. To extract the exchange parameters, compute the total energies of five ordered spin configurations (ferromagnetic FM, and antiferromagnetic AF1, AF2, AF3, AF4) in the crystallographic cell (or an appropriate supercell). The energy differences between these states are mapped onto the spin Hamiltonian H = –∑ Jᵢⱼ Sᵢ·Sⱼ with S=½ per Cu²⁺, yielding a linear system that solves for J₁, J₂, J₃, J₄. The same procedure is repeated for the hypothetical compounds Rb₂CuCl₄, K₂CuCl₄, and Na₂CuCl₄ by replacing Cs with the corresponding alkali atom at the same fractional coordinates without any structural relaxation. Separately, using the lowest-energy state of Cs₂CuCl₄, compute the projected density of states (PDOS) for the Cs 6p and Cs 6s orbitals. Integrate the PDOS over the occupied region (roughly from −5 eV to the Fermi level) and calculate the ratio of the integrated 6p intensity to the 6s intensity.

## Reproduction target
Produce two scored output files:

1. exchange_parameters.csv — a CSV table with columns Compound, J1, J2, J3, J4 (all in Kelvin) for Cs₂CuCl₄, Rb₂CuCl₄, K₂CuCl₄, and Na₂CuCl₄. The values must be derived from the DFT+U total energies as described.
2. dos_ratio.txt — a plain text file containing a single floating‑point number representing the ratio of integrated Cs 6p PDOS to Cs 6s PDOS for Cs₂CuCl₄.

Additionally, the exchange parameters across the alkali series are expected to exhibit a systematic variation that reflects the underlying physics; the verifier will check for consistency with the scientifically motivated behavior.

## Assets

- Cs₂CuCl₄ room‑temperature crystal structure: 10.1021/ja00779a044
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Cu, Cl, Cs, Rb, K, Na: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT+U total energies and PDOS computation
- Role: process
- Action: Set up input files for Cs₂CuCl₄ using the room‑temperature crystal structure. For each of the five spin configurations (FM, AF1, AF2, AF3, AF4), perform GGA+U self‑consistent field calculations with U=6 eV on Cu. Using the lowest-energy state (AF3), compute the projected density of states for Cs 6p and Cs 6s orbitals. For the hypothetical compounds A₂CuCl₄ (A = Rb, K, Na), replace Cs with each alkali atom without relaxing the structure and compute total energies for the same five spin configurations. Save all total energies to a structured JSON file and the PDOS data to another JSON file.
- Evidence: `/app/outputs/energies.json, pdos_cs.json`

### Step 2: Extract spin exchange parameters
- Role: scored (load-bearing)
- Action: Read total energies from energies.json. For each compound, solve the linear equations derived from the spin Hamiltonian (with N=1 unpaired spin per Cu) to obtain J₁, J₂, J₃, J₄. Express the values in Kelvin and write the results to exchange_parameters.csv.
- Output file: `/app/outputs/exchange_parameters.csv`
- Format: csv
- Contract: Columns: Compound (string), J1 (float, K), J2 (float, K), J3 (float, K), J4 (float, K).
- Scoring: scored by hidden verifier

### Step 3: Compute Cs 6p / 6s DOS ratio
- Role: scored
- Action: Read the projected density of states arrays from pdos_cs.json. Integrate the Cs 6p and Cs 6s DOS over the occupied energy region (approximately −5 eV to the Fermi level). Compute the ratio of the integrated 6p intensity to the integrated 6s intensity and write the result as a floating‑point number to dos_ratio.txt.
- Output file: `/app/outputs/dos_ratio.txt`
- Format: txt
- Contract: A single ASCII floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_parameters.csv`
- `/app/outputs/dos_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_parameters.csv
- path: `/app/outputs/exchange_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spin exchange parameters J₁–J₄ for Cs₂CuCl₄, Rb₂CuCl₄, K₂CuCl₄, and Na₂CuCl₄. The checker compares each value against hidden paper‑reported references with appropriate tolerances and verifies that the exchange parameters across the alkali series follow the expected physical trend.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `J1`, `J2`, `J3`, `J4`
  - `units`:
    - `J1`: K
    - `J2`: K
    - `J3`: K
    - `J4`: K

### dos_ratio.txt
- path: `/app/outputs/dos_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Ratio of integrated Cs 6p to Cs 6s PDOS in the occupied energy region for Cs₂CuCl₄. The checker compares the value against a hidden paper‑derived gold within a tolerance range.
- schema:
  - `type`: text
  - `description`: A single floating‑point number.

Notes: The scoring verifies that the computed J values are consistent with the paper‑reported GGA+U (U=6 eV) results and that the alkaline substitution trend matches the expected physical behavior. The DOS ratio validates the dominance of Cs 6p over Cs 6s orbitals.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "J1",
          "J2",
          "J3",
          "J4"
        ],
        "units": {
          "J1": "K",
          "J2": "K",
          "J3": "K",
          "J4": "K"
        }
      },
      "description": "Spin exchange parameters J₁–J₄ for Cs₂CuCl₄, Rb₂CuCl₄, K₂CuCl₄, and Na₂CuCl₄. The checker compares each value against hidden paper‑reported references with appropriate tolerances and verifies that the exchange parameters across the alkali series follow the expected physical trend."
    },
    {
      "file": "dos_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number."
      },
      "description": "Ratio of integrated Cs 6p to Cs 6s PDOS in the occupied energy region for Cs₂CuCl₄. The checker compares the value against a hidden paper‑derived gold within a tolerance range."
    }
  ],
  "notes": "The scoring verifies that the computed J values are consistent with the paper‑reported GGA+U (U=6 eV) results and that the alkaline substitution trend matches the expected physical behavior. The DOS ratio validates the dominance of Cs 6p over Cs 6s orbitals."
}
```

## How you are scored
A hidden verifier independently inspects the two output files. It recomputes the exchange parameters from the raw total energies (energies.json) you provide and compares them against reference values obtained from the literature — this ensures that your extraction is correct and that the energies themselves are physically sound. It also integrates the Cs PDOS from pdos_cs.json and checks the reported ratio. The verifier additionally tests that the trend across the alkali series matches the expected physical tendency (details undisclosed). The final score is a weighted combination of the individual checks: correct exchange parameter values, correct DOS ratio, and correct chemical trend. Submitting only the final numbers without the underlying energies and PDOS, or producing numbers that do not arise from a genuine DFT+U calculation, will not pass the verifier.
