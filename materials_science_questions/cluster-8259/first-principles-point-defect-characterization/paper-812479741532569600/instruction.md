# DFT defect transition levels and formation energies in 2D Ruddlesden-Popper perovskite

## Problem background
Two-dimensional Ruddlesden-Popper lead iodine perovskites exhibit superior stability compared to their 3D counterparts, but suffer from reduced carrier mobility due to the layered structure. Understanding intrinsic point defect properties—particularly transition energy levels and formation energies—is critical to explaining and improving charge transport. Density functional theory (DFT) calculations can reveal whether defects are shallow donors/acceptors (contributing free carriers) or deep recombination centers, and how surface versus interior defect positions affect these levels. This task focuses on reproducing these defect properties for the single-layer (2D1L) Ruddlesden-Popper perovskite using PBE DFT without spin-orbit coupling.

## Approach
The defect properties are computed using density functional theory (DFT) within the generalized gradient approximation (PBE) without spin-orbit coupling. The organic cations (BA, MA) are replaced by Cs to create a M₂PbI₄ (M=Cs) model perovskite. The workflow begins with geometry relaxation of the host unit cell and construction of a 3×3×1 supercell. Host total energy E(host) and the valence-band maximum eigenvalue ε_VBM(host) are obtained. Elemental reference energies for Pb (fcc), I (I₂ molecule), and Cs (bcc) are computed with the same settings. Defect supercells are then created for V_I and I_i on the outer (LA) and inner (LB) layers, as well as for the deep defects Pb_i, Pb_I, I_M, and I_Pb. Total energies E(α,q) are computed in the relevant charge states: q=0 and +1 for V_I, q=0 and -1 for I_i, and q=0 for the deep defects. Transition energy levels are derived from the standard charged-defect formation energy formalism: ΔE(α,q) = E(α,q) − E(host) + Σ n_i E(i) + q ε_VBM(host), and the transition level ε(q/q′) = [ΔE(α,q) − ΔE(α,q′)]/(q′ − q). Neutral formation energies are computed at chemical potentials μ_i = 0 using ΔE(α,0). All calculations use the open-source plane-wave DFT code Quantum ESPRESSO or an equivalent PBE-capable code.

## Reproduction target
Compute using DFT (PBE, no SOC) the (0/1+) transition energy levels of V_I and I_i defects in the outer (LA) and inner (LB) layers of a 2D1L M₂PbI₄ (M=Cs) perovskite, referenced to the host CBM (for donors) or VBM (for acceptors). Also compute the neutral (q=0) formation energies of deep defects Pb_i, Pb_I, I_M, and I_Pb at chemical potentials μ_i=0. Output the results as two JSON files with the exact schemas specified in the workflow steps and output contract.

## Assets

- Crystal structures of Ruddlesden-Popper perovskites (Stoumpos 2016): 10.1021/acs.chemmater.6b00847
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build and relax 2D1L host unit cell
- Role: process
- Action: Obtain the crystal structure of 2D1L perovskite BA2PbI4 (n=1) from the public dataset (Stoumpos et al. 2016), replace organic cations with Cs to create the M2PbI4 model, and perform geometry relaxation using PBE DFT. Save the relaxed host unit cell structure.
- Evidence: `/app/outputs/relaxed_host_unit_cell.log`

### Step 2: Construct 3×3×1 supercell and compute host reference energies
- Role: process
- Action: From the relaxed M2PbI4 unit cell, construct a 3×3×1 supercell. Perform a Gamma-point PBE calculation to obtain the total energy E(host) and the valence-band maximum eigenvalue ε_VBM(host). Save these energies.
- Evidence: `/app/outputs/host_supercell_energies.json`

### Step 3: Compute elemental reference energies for Pb, I, Cs
- Role: process
- Action: Calculate the total energy per atom of Pb (fcc), I (I2 molecule), and Cs (bcc) in their standard elemental phases using the same PBE settings.
- Evidence: `/app/outputs/elemental_reference_energies.json`

### Step 4: Defect supercell calculations for V_I, I_i, and deep defects
- Role: process
- Action: For each defect type (V_I on outer layer LA and inner layer LB, I_i on LA and LB, Pb_i, Pb_I, I_M, I_Pb) in the 3×3×1 supercell, create the defect by removing/adding atoms as appropriate, relax atomic positions (fixed lattice), and compute total energies in the relevant charge states: V_I in q=0 and +1, I_i in q=0 and -1, and the four deep defects in q=0. Save all defect total energies E(α,q).
- Evidence: `/app/outputs/defect_total_energies.json`

### Step 5: Calculate transition energy levels for V_I and I_i
- Role: scored (load-bearing)
- Action: Using the defect total energies from Step 4 and the standard definitions: ΔE(α,q) = E(α,q) − E(host) + n_Pb·E(Pb) + n_I·E(I) + n_M·E(M) + q·ε_VBM(host), and transition level ε_α(q/q′) = [ΔE(α,q) − ΔE(α,q′)]/(q′ − q). Compute the (0/1+) transition level for V_I (referenced to CBM, i.e., CBM energy assumed known from host calculation) and the (0/1−) transition level for I_i (referenced to VBM), for both LA and LB positions. Write results to transition_levels_2D1L.json.
- Output file: `/app/outputs/transition_levels_2D1L.json`
- Format: json
- Contract: JSON object with keys: V_I_LA, V_I_LB, I_i_LA, I_i_LB; each is an object {"transition_type": "(0/1+)" or "(0/1−)", "value_eV": float, "reference": "CBM" or "VBM"}.
- Scoring: scored by hidden verifier

### Step 6: Calculate neutral formation energies for deep defects
- Role: scored
- Action: For defects Pb_i, Pb_I, I_M, I_Pb in charge state q=0, compute the formation energy ΔH(α,0) = ΔE(α,0) + Σ n_i·μ_i, with ΔE(α,0) defined as in step 5 and chemical potentials μ_Pb = μ_I = μ_M = 0. Use the host and elemental reference energies from earlier steps. Output to deep_defect_formation_energies.json.
- Output file: `/app/outputs/deep_defect_formation_energies.json`
- Format: json
- Contract: JSON object with keys: Pb_i_0, Pb_I_0, I_M_0, I_Pb_0; each value is a float (formation energy in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_levels_2D1L.json`
- `/app/outputs/deep_defect_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_levels_2D1L.json
- path: `/app/outputs/transition_levels_2D1L.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Transition energy levels of V_I and I_i defects on outer (LA) and inner (LB) layers.
- schema:
  - `type`: object
  - `required`:
    - `V_I_LA`: object with transition_type (string), value_eV (float), reference (CBM)
    - `V_I_LB`: object with transition_type (string), value_eV (float), reference (CBM)
    - `I_i_LA`: object with transition_type (string), value_eV (float), reference (VBM)
    - `I_i_LB`: object with transition_type (string), value_eV (float), reference (VBM)
  - `items`:
    - `transition_type`: string, either '(0/1+)' or '(0/1-)'
    - `value_eV`: float, transition energy in eV
    - `reference`: string, 'CBM' or 'VBM'

### deep_defect_formation_energies.json
- path: `/app/outputs/deep_defect_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Neutral formation energies (μ_i=0) of deep defects Pb_i, Pb_I, I_M, I_Pb.
- schema:
  - `type`: object
  - `required`:
    - `Pb_i_0`: float (eV)
    - `Pb_I_0`: float (eV)
    - `I_M_0`: float (eV)
    - `I_Pb_0`: float (eV)
  - `items`:
    - ``: float, formation energy in eV

Notes: The agent must compute these quantities using PBE DFT without spin-orbit coupling. The hidden reference values are derived from the paper's reported results for the 2D1L system.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_levels_2D1L.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V_I_LA": "object with transition_type (string), value_eV (float), reference (CBM)",
          "V_I_LB": "object with transition_type (string), value_eV (float), reference (CBM)",
          "I_i_LA": "object with transition_type (string), value_eV (float), reference (VBM)",
          "I_i_LB": "object with transition_type (string), value_eV (float), reference (VBM)"
        },
        "items": {
          "transition_type": "string, either '(0/1+)' or '(0/1-)'",
          "value_eV": "float, transition energy in eV",
          "reference": "string, 'CBM' or 'VBM'"
        }
      },
      "description": "Transition energy levels of V_I and I_i defects on outer (LA) and inner (LB) layers."
    },
    {
      "file": "deep_defect_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Pb_i_0": "float (eV)",
          "Pb_I_0": "float (eV)",
          "I_M_0": "float (eV)",
          "I_Pb_0": "float (eV)"
        },
        "items": {
          "": "float, formation energy in eV"
        }
      },
      "description": "Neutral formation energies (μ_i=0) of deep defects Pb_i, Pb_I, I_M, I_Pb."
    }
  ],
  "notes": "The agent must compute these quantities using PBE DFT without spin-orbit coupling. The hidden reference values are derived from the paper's reported results for the 2D1L system."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. It compares your computed transition levels and formation energies to hidden reference values (derived from the published literature) using tolerances calibrated for the computational method employed. The verifier also checks that the relative ordering of transition levels (e.g., deeper vs. shallower) is consistent with the expected physical trend. Each scored artifact contributes a portion of the total reward; accurate reproduction of the computed quantities, rather than self-reporting of paper numbers, earns full credit. The final reward is a weighted sum of the individual artifact scores.
