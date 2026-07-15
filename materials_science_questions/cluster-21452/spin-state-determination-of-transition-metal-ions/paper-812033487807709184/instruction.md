# Hamiltonian Model for Impurity-to-Conduction-Band Charge-Transfer Excited State

## Problem background
Cobalt doping in the semiconductor ZnSe introduces Co^(2+) impurities that give rise to three sharp absorption bands (L, M, N) near the band gap. These transitions are interpreted as impurity-to-conduction-band charge-transfer excitations: an electron is excited from the Co^(2+) ground state into a bound state derived from the conduction band, leaving behind a Co^(3+) core. The lowest-energy band L (2.361 eV) and its satellite L′ (2.363 eV) are sufficiently narrow to allow detailed magneto-optical and uniaxial stress studies. The L excited state is found to have E′ (Γ₆) symmetry and a negative g-value, while L′ has U′ (Γ₈) symmetry and exhibits an anisotropic stress response. The experimental data constrain a model Hamiltonian for the excited state, which involves spin-orbit coupling within the Co^(3+) core, exchange coupling between the core and the bound electron, and a dynamic Jahn–Teller interaction via an e‑symmetry phonon. The task is to implement this Hamiltonian, fit its four parameters to simultaneously satisfy the observed zero-field energies, symmetries, and g-value of the L and L′ lines, and then predict the Zeeman splitting pattern at a specified magnetic field.

## Approach
The excited state is modeled as [Co^(3+)(d⁶, ⁵E)]·e_b, where the Co^(3+) core is in the high-spin ⁵E ligand-field state and the bound electron occupies an s‑like (A₁) level derived from the conduction band. The Hamiltonian contains four terms:
- **Spin-orbit (H_SO):** acts mainly within the d⁶ core, lifting the degeneracy of the ⁵E state into five spin-orbit components (A₁, A₂, E, T₁, T₂) parameterized by a single energy γ.
- **Exchange (H_EX):** a spin–spin interaction of the form (2/3)D S·s between the total spin S=2 of the core and the electron spin s=1/2, which separates the ⁴E and ⁶E charge-transfer states.
- **Jahn–Teller (H_JT):** coupling of the E-orbital degree of freedom to a single e‑symmetry phonon mode of energy ħω_E, truncated to zero-, one-, and two‑phonon states.
- **Zeeman (H_Z):** interaction with an applied magnetic field.

The overall charge-transfer states are classified by the double-group representations E′, E″, and U′ of T_d. Using the product basis of spin-orbit core states and the electron spin, with vibrational wavefunctions included, the Hamiltonian matrices for each symmetry are constructed. Diagonalization yields the eigenstates and energies. The parameters γ, D, ħω_E, and V/α (the Jahn–Teller coupling strength normalized by the phonon mode constant α) are adjusted to reproduce three key experimental facts: (i) the zero-field energy separation between the L and L′ lines (~2 cm⁻¹), (ii) the symmetry of L as E′ and L′ as U′, and (iii) a negative g-value for the lowest E′ state that matches the measured value for L. Once fitted, the model is used to compute the Zeeman splitting of the ⁴A₂ → E′ (L) and ⁴A₂ → U′ (L′) transitions at a magnetic field of 3.5 T applied along the [001] crystal direction, with the ground-state spin-orbit U′ level (g = 2.27) as the initial state. Only transitions that borrow intensity from the ⁴E charge-transfer component are considered, which determines the expected polarizations (σ or π).

## Reproduction target
1. Construct and fit the model Hamiltonian for the charge-transfer excited state as described, using the vibronic basis truncated to two‑phonon states. Determine the parameters γ, D, ħω_E, and V/α so that the zero-field energies of the L (E′) and L′ (U′) lines, their symmetries, and the g-value of L are simultaneously consistent with the experimental constraints.
2. Output the fitted parameters in a JSON file (hparams.json) with fields `gamma_cm1`, `D_cm1`, `hw_E_cm1`, `V_over_alpha_cm1`, all in units of cm⁻¹.
3. Using the fitted Hamiltonian, compute the Zeeman components for the L and L′ absorption lines at a magnetic field of 3.5 T applied along the [001] crystal direction. The transitions originate from the four magnetic sublevels of the U′(⁴A₂) ground state (g = 2.27) and terminate on the E′(L) and U′(L′) excited states. For each component provide a label, its energy relative to the zero-field L line (in cm⁻¹), and its polarization (σ or π). Write the results to zeeman_splitting.json.

## Assets

- Python 3 standard environment

## Workflow steps

### Step 1: Construct and fit model Hamiltonian
- Role: process
- Action: Implement the Hamiltonian matrices (spin-orbit, exchange, Jahn–Teller, and Zeeman terms) for the [Co³⁺(d⁶,⁵E)]·e_b charge‑transfer excited state in the truncated vibronic basis as described in the paper. Diagonalize the matrices and fit the four parameters γ, D, ħω_E, V/α to reproduce the zero‑field energies of the L and L′ lines, the symmetries E′ and U′, and the negative g‑value of L.
- Evidence: `/app/outputs/fitted_model.pkl`

### Step 2: Output fitted model parameters
- Role: scored
- Action: Write the four fitted model parameters to a JSON file.
- Output file: `/app/outputs/hparams.json`
- Format: json
- Contract: {"type":"object","properties":{"gamma_cm1":{"type":"number"},"D_cm1":{"type":"number"},"hw_E_cm1":{"type":"number"},"V_over_alpha_cm1":{"type":"number"}},"required":["gamma_cm1","D_cm1","hw_E_cm1","V_over_alpha_cm1"]}
- Scoring: scored by hidden verifier

### Step 3: Compute Zeeman splitting for L and L′
- Role: scored (load-bearing)
- Action: Using the fitted Hamiltonian, compute the energies and polarisations of the Zeeman components of the L and L′ absorption lines at a magnetic field of 3.5 T applied along the [001] crystal direction. Write the results to a JSON file.
- Output file: `/app/outputs/zeeman_splitting.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"label":{"type":"string"},"energy_cm1":{"type":"number"},"polarization":{"type":"string","enum":["sigma","pi"]}},"required":["label","energy_cm1","polarization"]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hparams.json`
- `/app/outputs/zeeman_splitting.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hparams.json
- path: `/app/outputs/hparams.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted model parameters: spin–orbit γ, exchange D, Jahn–Teller phonon energy ħω_E, coupling strength V/α, all in cm⁻¹.
- schema:
  - `type`: object
  - `properties`:
    - `gamma_cm1`:
      - `type`: number
    - `D_cm1`:
      - `type`: number
    - `hw_E_cm1`:
      - `type`: number
    - `V_over_alpha_cm1`:
      - `type`: number
  - `required`: `gamma_cm1`, `D_cm1`, `hw_E_cm1`, `V_over_alpha_cm1`

### zeeman_splitting.json
- path: `/app/outputs/zeeman_splitting.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Predicted Zeeman components for the L (E′) and L′ (U′) transitions at B = 3.5 T along [001]; energies relative to the zero‑field L line.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `label`:
        - `type`: string
      - `energy_cm1`:
        - `type`: number
      - `polarization`:
        - `type`: string
        - `enum`: `sigma`, `pi`
    - `required`: `label`, `energy_cm1`, `polarization`

Notes: The checker will compare the submitted hparams.json to the paper‑reported values within tolerance and will recompute the Zeeman splitting from the submitted parameters to verify consistency with the submitted zeeman_splitting.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hparams.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "gamma_cm1": {
            "type": "number"
          },
          "D_cm1": {
            "type": "number"
          },
          "hw_E_cm1": {
            "type": "number"
          },
          "V_over_alpha_cm1": {
            "type": "number"
          }
        },
        "required": [
          "gamma_cm1",
          "D_cm1",
          "hw_E_cm1",
          "V_over_alpha_cm1"
        ]
      },
      "description": "Fitted model parameters: spin–orbit γ, exchange D, Jahn–Teller phonon energy ħω_E, coupling strength V/α, all in cm⁻¹."
    },
    {
      "file": "zeeman_splitting.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            },
            "energy_cm1": {
              "type": "number"
            },
            "polarization": {
              "type": "string",
              "enum": [
                "sigma",
                "pi"
              ]
            }
          },
          "required": [
            "label",
            "energy_cm1",
            "polarization"
          ]
        }
      },
      "description": "Predicted Zeeman components for the L (E′) and L′ (U′) transitions at B = 3.5 T along [001]; energies relative to the zero‑field L line."
    }
  ],
  "notes": "The checker will compare the submitted hparams.json to the paper‑reported values within tolerance and will recompute the Zeeman splitting from the submitted parameters to verify consistency with the submitted zeeman_splitting.json."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently evaluates each output artifact and combines the results into a final reward (weight: 40 % on the fitted parameters, 60 % on the Zeeman predictions).
- For `hparams.json`: the verifier compares your reported parameters to the physically expected values within small tolerances. A parameter that falls within the allowed window receives full credit; the score decreases as the deviation grows.
- For `zeeman_splitting.json`: the verifier recomputes the Zeeman splitting from your submitted parameters using its own reference implementation of the same Hamiltonian. It then checks that the transition energies and polarizations you reported match the recomputed ones within tolerance. It also verifies that the zero-field separation and the g-value derived from your parameters are consistent with the model. Overall, the score reflects how well your numerical results agree with the expected physical behavior; simply guessing or fabricating a number without correctly solving the Hamiltonian and fitting procedure will not yield a high reward.
