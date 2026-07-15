# Two-site Hubbard simulator from boron acceptor pairs in silicon

## Problem background
Understanding correlated many-body phenomena in the fermionic Hubbard model is central to condensed matter physics, where non-perturbative interactions can lead to exotic states such as spin liquids and unconventional superconductivity. Subsurface acceptor pairs in silicon have been proposed as a solid-state quantum simulator for the two-site Hubbard Hamiltonian. Their electronic states can be controlled by the inter-acceptor separation, enabling a systematic study of correlations and entanglement. The aim is to predict, via a theoretical model, the ground-state properties of two holes bound to two acceptor impurities and to quantify the effective Hubbard interactions, entanglement entropy, and molecular-orbital occupation amplitudes that emerge from this coupled system.

## Approach
A configuration-interaction (CI) calculation is performed for two holes bound to two acceptor impurities in silicon. The single-particle basis is constructed from hydrogenic s-like acceptor orbitals with an effective Bohr radius a_B = 1.3 nm, within the Luttinger-Kohn effective-mass framework that includes the silicon valence-band structure (heavy-hole, light-hole, split-off bands) and spin-orbit coupling. The two-hole basis consists of all Slater determinants formed from these single-particle states. The Hamiltonian is diagonalized for each inter-acceptor separation d (in units of a_B) along the ⟨100⟩ and ⟨110⟩ crystallographic directions, and the singlet ground state is identified. From the ground-state wavefunction we extract the squared probability amplitudes |γ_ee|^2 and |γ_oo|^2 of the even–even and odd–odd molecular-orbital configurations. These amplitudes directly determine the von Neumann entanglement entropy S = −|γ_ee|^2 log2(|γ_ee|^2) − |γ_oo|^2 log2(|γ_oo|^2). Using the one-to-one mapping between S and the effective Hubbard interaction ratio U/t for a two-site Hubbard model, we derive U/t from the amplitudes. This theoretical pipeline produces curves of entanglement S(d) and interaction U/t(d) for both orientations.

## Reproduction target
Reproduce the theoretical predictions for the two-hole ground state: compute the squared probability amplitudes |γ_ee|^2 and |γ_oo|^2, the von Neumann entanglement entropy S, and the effective Hubbard interaction ratio U/t, as functions of inter-acceptor separation d/a_B for both ⟨100⟩ and ⟨110⟩ orientations. The CI calculation uses the silicon Luttinger parameters γ1=4.285, γ2=0.339, γ3=1.446, a dielectric constant ε=11.7, and an acceptor effective Bohr radius a_B=1.3 nm, following the acceptor binding model of Rahman et al. (2006). Compute these quantities for separations d/a_B = 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0. Output the complete curves as well as the individual probability amplitudes, entropy, and U/t at each separation.

## Assets

- Silicon Luttinger parameters, dielectric constant, and effective Bohr radius
- Acceptor binding model reference (Rahman et al., Phys. Rev. B 73, 035324, 2006): https://doi.org/10.1103/PhysRevB.73.035324
- Python 3 with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Run configuration-interaction calculation
- Role: process
- Action: Implement and execute a full configuration-interaction calculation for two holes bound to two acceptor impurities in silicon. Construct single-particle basis states from hydrogenic s-like acceptor orbitals with effective Bohr radius a_B=1.3 nm, using the Luttinger-Kohn effective mass Hamiltonian for the Si valence band (γ1=4.285, γ2=0.339, γ3=1.446, ε=11.7). Include spin-orbit coupling and the four valence-band Bloch states (heavy-hole, light-hole, split-off). Build the two-hole basis from all Slater determinants within the chosen single-particle space. Diagonalize the Hamiltonian for each inter-acceptor separation d (in units of a_B) for ⟨100⟩ and ⟨110⟩ orientations, for d = 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0, and identify the singlet ground state.
- Evidence: none

### Step 2: Probability amplitudes
- Role: scored (load-bearing)
- Action: From the CI ground state, extract the squared probability amplitudes |γ_ee|^2 and |γ_oo|^2 of the even–even and odd–odd molecular orbital configurations. Save them in step_01_probability_amplitudes.json.
- Output file: `/app/outputs/step_01_probability_amplitudes.json`
- Format: json
- Contract: A JSON object with keys 'amplitude_ee_squared' and 'amplitude_oo_squared', each mapping a separation string (e.g., '2.2') to an object with keys '100' and '110' giving the value as a float.
- Scoring: scored by hidden verifier

### Step 3: Entanglement entropy
- Role: scored
- Action: Compute the von Neumann entanglement entropy S = -|γ_ee|^2 log2(|γ_ee|^2) - |γ_oo|^2 log2(|γ_oo|^2) for each separation and orientation, and write to step_02_entanglement_entropy.json.
- Output file: `/app/outputs/step_02_entanglement_entropy.json`
- Format: json
- Contract: A JSON object mapping each separation string to an object with keys '100' and '110' giving S as a float.
- Scoring: scored by hidden verifier

### Step 4: Hubbard U/t ratio
- Role: scored
- Action: Derive the effective Hubbard interaction ratio U/t from S using the one-to-one mapping between S and U/t for a two-site Hubbard model. A practical form of the mapping is: α = |γ_oo|^2 / |γ_ee|^2, S = - (1/(1+α)) log2(1/(1+α)) - (α/(1+α)) log2(α/(1+α)), and U/t = 2(1/α - 1). Apply this relation to obtain U/t and save to step_03_U_over_t.json.
- Output file: `/app/outputs/step_03_U_over_t.json`
- Format: json
- Contract: A JSON object mapping each separation string to an object with keys '100' and '110' giving U/t as a positive float.
- Scoring: scored by hidden verifier

### Step 5: Full curves
- Role: scored
- Action: Save the complete S(d) and U/t(d) curves as lists of (separation, value) data points for both orientations in step_04_full_curves.json.
- Output file: `/app/outputs/step_04_full_curves.json`
- Format: json
- Contract: A JSON object with keys 'S' and 'U_over_t', each mapping an orientation string ('100' or '110') to a list of objects with keys 'separation' (float) and 'value' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_probability_amplitudes.json`
- `/app/outputs/step_02_entanglement_entropy.json`
- `/app/outputs/step_03_U_over_t.json`
- `/app/outputs/step_04_full_curves.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_probability_amplitudes.json
- path: `/app/outputs/step_01_probability_amplitudes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Squared probability amplitudes of molecular-orbital configurations used for structural checks (sum-to-one, monotonicity).
- schema:
  - `type`: object
  - `required`: `amplitude_ee_squared`, `amplitude_oo_squared`
  - `properties`:
    - `amplitude_ee_squared`:
      - `type`: object
    - `amplitude_oo_squared`:
      - `type`: object

### step_02_entanglement_entropy.json
- path: `/app/outputs/step_02_entanglement_entropy.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Entanglement entropy S per separation and orientation; used for monotonicity check.
- schema:
  - `type`: object

### step_03_U_over_t.json
- path: `/app/outputs/step_03_U_over_t.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Hubbard U/t per separation and orientation; used for monotonicity check.
- schema:
  - `type`: object

### step_04_full_curves.json
- path: `/app/outputs/step_04_full_curves.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Full S and U/t curves for comparison with reference theoretical curves.
- schema:
  - `type`: object
  - `required`: `S`, `U_over_t`
  - `properties`:
    - `S`:
      - `type`: object
    - `U_over_t`:
      - `type`: object

Notes: Only step_04_full_curves.json is compared against digitized reference curves with a relative tolerance; steps 01-03 provide structural checks and consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_probability_amplitudes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "amplitude_ee_squared",
          "amplitude_oo_squared"
        ],
        "properties": {
          "amplitude_ee_squared": {
            "type": "object"
          },
          "amplitude_oo_squared": {
            "type": "object"
          }
        }
      },
      "description": "Squared probability amplitudes of molecular-orbital configurations used for structural checks (sum-to-one, monotonicity)."
    },
    {
      "file": "step_02_entanglement_entropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object"
      },
      "description": "Entanglement entropy S per separation and orientation; used for monotonicity check."
    },
    {
      "file": "step_03_U_over_t.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object"
      },
      "description": "Hubbard U/t per separation and orientation; used for monotonicity check."
    },
    {
      "file": "step_04_full_curves.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "S",
          "U_over_t"
        ],
        "properties": {
          "S": {
            "type": "object"
          },
          "U_over_t": {
            "type": "object"
          }
        }
      },
      "description": "Full S and U/t curves for comparison with reference theoretical curves."
    }
  ],
  "notes": "Only step_04_full_curves.json is compared against digitized reference curves with a relative tolerance; steps 01-03 provide structural checks and consistency."
}
```

## How you are scored
Each workflow stage produces a scored artifact: probability amplitudes (step_01), entanglement entropy (step_02), U/t ratio (step_03), and full curves (step_04). A hidden verifier checks structural consistency (e.g., probability amplitudes must sum to one, |γ_oo|^2 must increase monotonically with separation, and S and U/t must be monotonically increasing) for the intermediate artifacts. The full curves in step_04 are compared against reference theoretical predictions; the verifier measures how well the submitted S(d) and U/t(d) curves reproduce the expected trends and shape. The final reward is a weighted combination of these individual stage scores. Simply reporting a single number from the literature is not sufficient; the scores reflect the correctness of the computed curves and their derived properties.
