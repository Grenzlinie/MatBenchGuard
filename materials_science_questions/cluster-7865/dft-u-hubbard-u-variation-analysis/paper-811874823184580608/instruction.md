# Oxygen Vacancy Transition Levels in BiFeO3 by LDA+U and Hybrid DFT

## Problem background
BiFeO3 (BFO) is a multiferroic material with a large remnant polarization, promising for ferroelectric memories, but it often exhibits high electrical leakage currents that obscure its ferroelectric response. Oxygen vacancies have been implicated as a primary source of this leakage, and understanding their energy levels within the band gap is key to explaining the observed conduction and to guiding defect engineering. In a computational study, density functional theory (DFT) was used to determine the formation energies and charge-state transition levels of the oxygen vacancy in the R3c phase of BFO. The calculations employed a two‑stage protocol: geometry relaxation with LDA+U (to open the band gap of the correlated oxide) followed by total energy evaluation with a hybrid functional for improved energetics. The central quantities that emerged—the vacancy’s transition levels relative to the conduction band edge and its formation energies under oxidising and reducing conditions—establish the defect’s electronic behaviour and its link to leakage. Independently reproducing these defect properties with open‑source DFT tools serves as a stringent test of the computational protocol and provides a quantitative validation of the reported defect model.

## Approach
This task implements the core two‑stage DFT approach used in the referenced work, relying entirely on open‑source software. First, the atomic geometry of a 120‑atom supercell containing an oxygen vacancy is relaxed for each relevant charge state (neutral, +1, +2) using a DFT+U method with a Hubbard U correction applied to Fe 3d states; the on‑site U is taken as 4.7 eV, a value that was calibrated to match the screened‑exchange band gap. The relaxations use a plane‑wave basis and a converged k‑point sampling. Next, single‑point total energies are computed for the relaxed defect supercells, a perfect supercell, and the pristine bulk unit cell using a hybrid functional (such as HSE06 or PBE0), which yields accurate total energies and a correct bulk band gap. From these energies, the defect formation energies are evaluated as a function of the Fermi level (referenced to the valence‑band maximum) and for two oxygen chemical‑potential extremes — O‑rich (μ<sub>O</sub> = 0 eV, i.e., the O<sub>2</sub> molecule reference) and O‑poor (μ<sub>O</sub> = –1.97 eV, corresponding to Bi<sub>2</sub>O<sub>3</sub>/Bi equilibrium). The formation‑energy data allow extraction of the charge‑state transition levels, ε(+/2+) and ε(0/+), defined as the Fermi‑level positions where the formation energies of adjacent charge states are equal, and also the formation energy of the neutral vacancy under the O‑poor condition.

## Reproduction target
Reproduce the defect‑formation and transition‑level analysis for the oxygen vacancy in the R3c phase of BiFeO3 using a two‑stage DFT protocol: LDA+U (U=4.7 eV on Fe 3d) for geometry relaxation of a 120‑atom supercell, followed by hybrid‑functional total‑energy calculations on the relaxed structures. Compute the bulk band gap of pristine BFO with the same hybrid functional. Evaluate the defect formation energies for charge states 0, +1, +2 as a function of the Fermi level (relative to the valence‑band maximum) under both O‑rich (μ<sub>O</sub> = 0 eV) and O‑poor (μ<sub>O</sub> = –1.97 eV) conditions. From the formation‑energy results, determine the transition levels ε(+/2+) and ε(0/+) in eV below the conduction‑band minimum (CBM = VBM + bulk band gap) and the formation energy of the neutral vacancy under O‑poor conditions. Summarise all results in a single JSON file (`computed_properties.json`) that contains: the bulk band gap, the two transition levels, the neutral‑vacancy formation energy (O‑poor), and the full formation‑energy arrays (one per charge state) giving the energies at a fine grid of Fermi levels for both O‑rich and O‑poor regimes. The workflow and intermediate checks must be documented in the logging evidence files listed in the workflow steps.

## Assets

- Open‑source DFT package (e.g., CP2K, GPAW, Quantum ESPRESSO): https://www.cp2k.org
- BiFeO3 R3c crystal structure (bulk unit cell): https://materialsproject.org/materials/mp-644069/
- Pseudopotential library: bundled with chosen DFT code or from public repositories (GTH for CP2K, SSSP for Quantum ESPRESSO)

## Workflow steps

### Step 1: Build 120‑atom supercell with oxygen vacancy
- Role: process
- Action: Construct a 120‑atom supercell of R3c BiFeO3 (3×2√2×2√2) with lattice parameters fixed to bulk values, introduce an oxygen vacancy, and prepare input files for DFT+U (U=4.7 eV on Fe 3d) geometry relaxations for charge states q=0,+1,+2 and for the defect‑free perfect cell.
- Evidence: `/app/outputs/supercell_input.log`

### Step 2: Relax defect geometries with LDA+U
- Role: process
- Action: Perform geometry relaxation for each charge state (q=0,+1,+2) using DFT+U with U=4.7 eV on Fe 3d, a plane‑wave kinetic energy cutoff equivalent to 800 eV, a suitable k‑point sampling (e.g., a single k‑point at (1/4,1/4,1/4) or a converged mesh) until forces are below 0.01 eV/Å. Save the relaxed atomic coordinates.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Compute total energies with hybrid functional
- Role: process
- Action: Using the relaxed geometries, perform single‑point total energy calculations with a hybrid functional (e.g., HSE06 or PBE0) for the defect supercells (q=0,+1,+2), the perfect supercell, and the pristine bulk R3c cell (to obtain the band gap). Ensure convergence of total energies and the band gap with respect to k‑point sampling and basis set.
- Evidence: `/app/outputs/hybrid_energies.log`

### Step 4: Calculate formation energies and transition levels
- Role: scored (load-bearing)
- Action: From the hybrid total energies, compute defect formation energies as a function of Fermi level (relative to VBM) for O‑rich (μ_O=0 eV) and O‑poor (μ_O=−1.97 eV) conditions using the standard supercell formation energy formula. Determine the transition levels ε(+/2+) and ε(0/+) (Fermi positions where formation energies of two charge states intersect) and express them in eV below the conduction band minimum (CBM = VBM + computed bulk band gap). Also compute the formation energy of the neutral vacancy under O‑poor conditions. Write all results to 'computed_properties.json' with the specified schema.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: JSON object with keys:
- bulk_band_gap (float, eV)
- transition_level_plus2plus (float, eV below CBM)
- transition_level_0plus (float, eV below CBM)
- neutral_formation_energy_O_poor (float, eV)
- formation_energies (array of objects, each with: charge (int, 0/1/2), fermi_levels (list of floats, eV relative to VBM), O_rich (list of float formation energies in eV), O_poor (list of float formation energies in eV))
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Main scored artifact: reproduced defect energetics—band gap, transition levels, neutral formation energy, and formation energy arrays—computed from the hybrid total energies. The checker validates the quantities against hidden paper‑reported reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `bulk_band_gap`: float (eV)
    - `transition_level_plus2plus`: float (eV below CBM)
    - `transition_level_0plus`: float (eV below CBM)
    - `neutral_formation_energy_O_poor`: float (eV)
    - `formation_energies`: array of objects
  - `items`:
    - `formation_energies_item`:
      - `charge`: int (0/1/2)
      - `fermi_levels`: list of floats (eV relative to VBM)
      - `O_rich`: list of floats (formation energies in eV)
      - `O_poor`: list of floats (formation energies in eV)

Notes: Tolerances are chosen to absorb legitimate functional and code spread (e.g., HSE06 vs the original screened exchange).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_band_gap": "float (eV)",
          "transition_level_plus2plus": "float (eV below CBM)",
          "transition_level_0plus": "float (eV below CBM)",
          "neutral_formation_energy_O_poor": "float (eV)",
          "formation_energies": "array of objects"
        },
        "items": {
          "formation_energies_item": {
            "charge": "int (0/1/2)",
            "fermi_levels": "list of floats (eV relative to VBM)",
            "O_rich": "list of floats (formation energies in eV)",
            "O_poor": "list of floats (formation energies in eV)"
          }
        }
      },
      "description": "Main scored artifact: reproduced defect energetics—band gap, transition levels, neutral formation energy, and formation energy arrays—computed from the hybrid total energies. The checker validates the quantities against hidden paper‑reported reference values with appropriate tolerances."
    }
  ],
  "notes": "Tolerances are chosen to absorb legitimate functional and code spread (e.g., HSE06 vs the original screened exchange)."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage’s main artifact. The primary scoring is based on `computed_properties.json`. The checker reads this file, verifies that it is well‑formed and contains all required fields, and then evaluates the reproduced quantities against a set of hidden reference values that correspond to the paper‑reported results. The comparison uses numerical tolerances that accommodate the legitimate spread arising from using a different open‑source code and functional (e.g., HSE06 versus the original screened‑exchange method). For the transition levels and the neutral‑vacancy formation energy, the checker checks how closely the computed values match the hidden references. The formation‑energy arrays are additionally examined for internal consistency: the checker independently interpolates the arrays to find the Fermi‑level positions where formation energies of adjacent charge states cross, and compares the resulting transition levels to the reported ones. The bulk band gap is also assessed against an expected range. Each scored quantity contributes a share of the total reward, with the transition levels and neutral formation energy carrying the largest weight. Simply writing the paper’s published numbers into the JSON file is not sufficient; the agent must execute the DFT workflow and let the checker validate the resulting output signals.
