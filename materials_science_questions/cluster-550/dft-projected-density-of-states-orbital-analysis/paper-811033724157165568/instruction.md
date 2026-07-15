# DFT Intermediate-Band Density of States and Effective Mass Analysis

## Problem background
Intermediate-band (IB) solar cells can surpass the efficiency limit of single-junction cells by using a material whose electronic structure includes a narrow, partially filled band inside the fundamental gap. This allows the absorption of sub-gap photons through two-step transitions, potentially reaching theoretical efficiencies above 60%. Identifying stable bulk materials that naturally exhibit such an IB is therefore an important but challenging computational screening problem. This task reproduces the density-of-states (DOS) analysis and effective mass evaluation for three candidate IB materials, to determine whether they possess a well-defined intermediate band, quantify its energy window, identify the dominant orbital character, and assess the carrier effective masses that govern charge transport.

## Approach
The core method is first-principles density-functional theory (DFT) within the generalised-gradient approximation (GGA-PBE). Three compounds—Au2Cs2I6, Ag2GeBaS4, and Ag2ZnSnS4—are studied. Their crystal structures are obtained from public databases (Materials Project or ICSD). For Au2Cs2I6 a Hubbard U correction is applied to treat Au d-states (U = 5 eV, J = 0.5 eV). For each compound, a self-consistent field (SCF) calculation is performed to obtain the ground-state charge density, followed by non-self-consistent calculations for the band structure along a high-symmetry k-path and for the total and site-projected density of states. From the computed DOS, the intermediate-band energy window is identified as the energy interval between the valence-band maximum and conduction-band minimum where the total DOS remains non-zero. Integrating the site-projected DOS in that window reveals which atomic orbitals dominate the IB. The band structure is used to extract electron, light-hole, and heavy-hole effective masses along the [110] direction via finite differences on the band curvature. The entire workflow uses the open-source Quantum ESPRESSO package with standard PBE pseudopotentials.

## Reproduction target
Produce two scored artifacts:
- A CSV file containing the raw total and site-projected DOS as a function of energy for all three compounds.
- A JSON file reporting, for each compound, the intermediate-band energy window (as a string e.g. '0.64‑1.34 eV'), the list of dominant orbitals obtained from the integrated site-projected DOS within that window, and the effective masses (m_lh, m_hh, m_e) in units of the free-electron mass.
The verifier will independently recompute the IB window from your raw DOS data, verify that the reported dominant orbitals are indeed those with the highest integrated PDOS in the identified window, and compare your effective masses against independently derived reference values. The results are evaluated based on the physical consistency and accuracy of these quantities, without requiring exact numerical match to any specific published table.

## Assets

- Quantum ESPRESSO v7.0+: https://www.quantum-espresso.org/
- SSSP efficiency library (PBE pseudopotentials): https://www.materialscloud.org/discover/sssp
- Materials Project: https://next-gen.materialsproject.org/
- Bilbao Crystallographic Server: https://www.cryst.ehu.es/

## Workflow steps

### Step 1: Retrieve crystal structures
- Role: process
- Action: Obtain crystal structures for Au2Cs2I6 (space group 139), Ag2GeBaS4 (space group 121), and Ag2ZnSnS4 (space group 121) from a public crystal structure database (e.g., Materials Project or ICSD).
- Evidence: none

### Step 2: DFT calculations
- Role: process
- Action: For each compound, perform DFT calculations using Quantum ESPRESSO with GGA-PBE functional. Compute self-consistent field (SCF), band structure along a high‑symmetry k‑path, and non‑self‑consistent total and site‑projected DOS. For Au2Cs2I6, apply GGA+U with U=5 eV, J=0.5 eV.
- Evidence: none

### Step 3: Extract raw DOS data
- Role: scored
- Action: From the DFT outputs, extract total DOS and site‑projected DOS (per orbital/atom) as a function of energy for all three compounds. Concatenate into a single CSV file.
- Output file: `/app/outputs/total_dos_data.csv`
- Format: csv
- Contract: CSV with columns: compound (str), energy_ev (float), total_dos (float), plus per‑orbital PDOS columns (float) named as <element>_<orbital> (e.g., S_3p, Sn_5s, I_5p, Ge_4s, Ba_4d).
- Scoring: scored by hidden verifier

### Step 4: Analyze DOS and effective masses
- Role: scored (load-bearing)
- Action: Identify the intermediate‑band energy window from the total DOS as the energy range between VBM and CBM where DOS is above a small threshold. Determine dominant orbital contributions by integrating site‑projected DOS in that window. Compute electron, light‑hole, and heavy‑hole effective masses along the [110] direction using finite differences on the band structure. Assemble results into a JSON file.
- Output file: `/app/outputs/dos_results.json`
- Format: json
- Contract: JSON object with compound names as top‑level keys. Each value is an object with mandatory fields: 'ib_energy_range' (string, e.g. '0.64‑1.34 eV'), 'dominant_orbitals' (array of strings), 'effective_masses' (object with float keys 'm_lh', 'm_hh', 'm_e').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_dos_data.csv`
- `/app/outputs/dos_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_dos_data.csv
- path: `/app/outputs/total_dos_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw total and site‑projected DOS for all three compounds, used by the checker to independently recalculate the intermediate‑band energy window and verify dominant orbital contributions.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `energy_ev`, `total_dos`
  - `description`: Required columns plus any number of per‑orbital columns named as <element>_<orbital> (float). The checker recomputes the IB energy range from this data.

### dos_results.json
- path: `/app/outputs/dos_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent's analysed results: IB energy window, dominant orbital contributions, and effective masses for the three representative intermediate‑band compounds. The checker will recompute the IB window from the raw DOS and compare, and verify effective masses against the paper‑reported values.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: object
    - `required`: `ib_energy_range`, `dominant_orbitals`, `effective_masses`
    - `properties`:
      - `ib_energy_range`:
        - `type`: string
      - `dominant_orbitals`:
        - `type`: array
        - `items`:
          - `type`: string
      - `effective_masses`:
        - `type`: object
        - `required`: `m_lh`, `m_hh`, `m_e`
        - `properties`:
          - `m_lh`:
            - `type`: number
          - `m_hh`:
            - `type`: number
          - `m_e`:
            - `type`: number
  - `description`: Keys are the three compound names. Each value contains the IB energy range, list of dominant orbitals, and effective masses. The checker compares these reported values to recomputed/predicted gold values with monotonic tolerance.

Notes: The checker recomputes the intermediate‑band energy range from total_dos_data.csv and compares it to the agent's reported range; it also checks that the reported dominant orbitals are the ones with highest integrated PDOS in that window, and compares effective masses to paper‑reported values with appropriate tolerances. All comparisons are monotonic (meeting or beating the reference earns full credit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "energy_ev",
          "total_dos"
        ],
        "description": "Required columns plus any number of per‑orbital columns named as <element>_<orbital> (float). The checker recomputes the IB energy range from this data."
      },
      "description": "Raw total and site‑projected DOS for all three compounds, used by the checker to independently recalculate the intermediate‑band energy window and verify dominant orbital contributions."
    },
    {
      "file": "dos_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "required": [
            "ib_energy_range",
            "dominant_orbitals",
            "effective_masses"
          ],
          "properties": {
            "ib_energy_range": {
              "type": "string"
            },
            "dominant_orbitals": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "effective_masses": {
              "type": "object",
              "required": [
                "m_lh",
                "m_hh",
                "m_e"
              ],
              "properties": {
                "m_lh": {
                  "type": "number"
                },
                "m_hh": {
                  "type": "number"
                },
                "m_e": {
                  "type": "number"
                }
              }
            }
          }
        },
        "description": "Keys are the three compound names. Each value contains the IB energy range, list of dominant orbitals, and effective masses. The checker compares these reported values to recomputed/predicted gold values with monotonic tolerance."
      },
      "description": "Agent's analysed results: IB energy window, dominant orbital contributions, and effective masses for the three representative intermediate‑band compounds. The checker will recompute the IB window from the raw DOS and compare, and verify effective masses against the paper‑reported values."
    }
  ],
  "notes": "The checker recomputes the intermediate‑band energy range from total_dos_data.csv and compares it to the agent's reported range; it also checks that the reported dominant orbitals are the ones with highest integrated PDOS in that window, and compares effective masses to paper‑reported values with appropriate tolerances. All comparisons are monotonic (meeting or beating the reference earns full credit)."
}
```

## How you are scored
A hidden verifier inspects every scored output. For the DOS CSV, it recomputes the intermediate-band energy window and checks that the PDOS columns are correctly formatted and non-trivial. For the results JSON, it recomputes the IB window from the CSV, verifies that your listed dominant orbitals correspond to the largest integrated PDOS contributions, and compares your reported effective masses to hidden reference values with predefined tolerances. Each stage contributes a predefined weight toward the final reward, which is a number between 0 and 1. Simply reporting the paper's published numbers without producing genuine DFT outputs will not satisfy the verifier; the reward is based on independently re-derivable quantities extracted from your submitted raw artifacts.
