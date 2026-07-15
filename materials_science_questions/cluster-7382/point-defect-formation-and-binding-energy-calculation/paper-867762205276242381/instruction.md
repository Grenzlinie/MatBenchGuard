# Charge-Corrected Jellium Model for Defect Ionization Energy in 2D BN

## Problem background
Defect ionization energies (IEs) in low-dimensional semiconductors are critical for understanding doping, carrier generation, and device performance. Standard DFT calculations with the jellium model add a uniform background charge to neutralize the supercell, but in slab models with vacuum this leads to divergent formation energies and unreliable IEs. The divergence arises because the artificial jellium charge spreads into the vacuum, creating unphysical electrostatic interactions. Consequently, a physically motivated correction is needed to obtain meaningful, convergent IE values for two-dimensional and other low-dimensional materials.

## Approach
The charge corrected jellium model replaces the unphysical uniform background charge with the band-edge charge density of the host material. For an acceptor defect (negative charge), the background charge is set to the valence band maximum (VBM) charge density; for a donor (positive charge), it is set to the conduction band minimum (CBM) charge density. This correction is applied inside the self-consistent loop of a DFT code: at each electronic iteration, the standard jellium background density is substituted by the appropriate band-edge charge density from a pristine host calculation. The corrected charged-defect total energy is then used together with the neutral defect total energy and the host VBM eigenvalue to compute the ionization energy as IE = E_charged_corrected - E_neutral - epsilon_VBM. The method requires no tunable parameters and converges with supercell size, eliminating the divergence problem.

## Reproduction target
Compute the defect ionization energies for the nitrogen vacancy V_N (donor, charge +1) and the carbon substitution on a nitrogen site C_N (acceptor, charge -1) in monolayer BN using the charge corrected jellium model implemented in Quantum Espresso. Report the IE values along with the intermediate total energies and the host VBM eigenvalue in a JSON file.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- Norm-conserving PBE pseudopotentials for B and N: http://www.pseudo-dojo.org/
- Monolayer BN crystal structure

## Workflow steps

### Step 1: Supercell construction and structural relaxation
- Role: process
- Action: Create a 12x12x1 supercell of monolayer BN with 15 Å vacuum. Introduce a nitrogen vacancy (V_N) and a carbon substitution at a nitrogen site (C_N) in separate supercells. Relax atomic positions using DFT (PBE, norm-conserving pseudopotentials, single Gamma-point sampling, 90 Ry cutoff) until forces are below suitable threshold. Also relax the pristine host supercell of the same size.
- Evidence: `/app/outputs/relaxed_coords.log`

### Step 2: Compute host band-edge properties
- Role: process
- Action: Perform a DFT calculation on the relaxed pristine host supercell (same parameters). Extract the valence band maximum (VBM) eigenvalue, the conduction band minimum (CBM) eigenvalue, and the corresponding charge densities (rho_VBM(r) and rho_CBM(r)). Save the charge density files and the eigenvalues for later use.
- Evidence: `/app/outputs/host_properties.json`

### Step 3: Compute neutral defect total energies
- Role: process
- Action: For each of the relaxed neutral defect supercells (V_N and C_N), perform a standard DFT calculation (no jellium background) to obtain the ground-state total energy E^N(alpha,0). Use the same computational parameters.
- Evidence: `/app/outputs/neutral_energies.json`

### Step 4: Charge-corrected DFT calculations
- Role: process
- Action: Implement the charge correction in Quantum Espresso: modify the self-consistent loop to replace the uniform jellium background charge density with the appropriate band-edge charge density (rho_VBM for acceptor C_N, rho_CBM for donor V_N) at each electronic iteration. Using the relaxed neutral defect supercell geometries, add/remove one electron to obtain the charged state (C_N^- , V_N^+) and run the corrected DFT calculation to obtain the corrected total energies E_{corr}^{N+1}(alpha,q). Keep all other parameters the same.
- Evidence: `/app/outputs/corrected_energies.json`

### Step 5: Calculate and report defect ionization energies
- Role: scored (load-bearing)
- Action: For each defect, compute the ionization energy as IE = E_{corr}^{N+1} - E^N(alpha,0) - epsilon_VBM, using the energies from the previous steps. Write the results to a JSON file with the fields: defect, charge_state, E_neutral, E_charged_corrected, epsilon_VBM, IE. All energies in eV.
- Output file: `/app/outputs/defect_results.json`
- Format: json
- Contract: A JSON array of two objects. Each object has keys: 'defect' (string, e.g. 'C_N' or 'V_N'), 'charge_state' (integer, -1 for acceptor, +1 for donor), 'E_neutral' (float, eV), 'E_charged_corrected' (float, eV), 'epsilon_VBM' (float, eV), 'IE' (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_results.json
- path: `/app/outputs/defect_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect ionization energies and intermediate total energies for C_N and V_N in monolayer BN computed with the charge-corrected jellium model. The verifier recomputes IE from the component energies and compares to the correct reference values.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `charge_state`, `E_neutral`, `E_charged_corrected`, `epsilon_VBM`, `IE`
    - `properties`:
      - `defect`:
        - `type`: string
      - `charge_state`:
        - `type`: integer
      - `E_neutral`:
        - `type`: number
        - `units`: eV
      - `E_charged_corrected`:
        - `type`: number
        - `units`: eV
      - `epsilon_VBM`:
        - `type`: number
        - `units`: eV
      - `IE`:
        - `type`: number
        - `units`: eV

Notes: The verifier checks internal consistency by recomputing IE from the reported component energies, then compares the IE to the expected physical values. Only the two defects C_N and V_N are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "charge_state",
            "E_neutral",
            "E_charged_corrected",
            "epsilon_VBM",
            "IE"
          ],
          "properties": {
            "defect": {
              "type": "string"
            },
            "charge_state": {
              "type": "integer"
            },
            "E_neutral": {
              "type": "number",
              "units": "eV"
            },
            "E_charged_corrected": {
              "type": "number",
              "units": "eV"
            },
            "epsilon_VBM": {
              "type": "number",
              "units": "eV"
            },
            "IE": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Defect ionization energies and intermediate total energies for C_N and V_N in monolayer BN computed with the charge-corrected jellium model. The verifier recomputes IE from the component energies and compares to the correct reference values."
    }
  ],
  "notes": "The verifier checks internal consistency by recomputing IE from the reported component energies, then compares the IE to the expected physical values. Only the two defects C_N and V_N are required."
}
```

## How you are scored
A hidden verifier inspects your submitted `defect_results.json`. It first recomputes each IE from the reported `E_neutral`, `E_charged_corrected`, and `epsilon_VBM` to verify internal arithmetic consistency. It then compares the computed IEs to reference physical values with an appropriate tolerance. The reward is monotonic: matching or beating the reference yields full credit; larger deviations reduce the reward linearly. Correct intermediate energies are essential; if the component energies are inconsistent or missing, the verifier will detect it and the score will be low. Only the final `defect_results.json` is scored, but the upstream process steps must be faithfully executed to reach those numbers.
