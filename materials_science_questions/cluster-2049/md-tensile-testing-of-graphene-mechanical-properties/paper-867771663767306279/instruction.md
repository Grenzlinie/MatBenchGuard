# Inverse quality factor of graphene nanoresonators: dissipation mechanisms

## Problem background
Graphene nanoresonators are promising for high-sensitivity detection due to their high elastic modulus and small mass, allowing for high resonance frequencies. However, their performance is limited by mechanical energy dissipation, which broadens the resonance and reduces sensitivity. Several dissipation mechanisms may contribute: electrostatic coupling to static charges in the SiO₂ substrate, ohmic losses in the graphene sheet and the metallic gate, breaking and healing of surface bonds (Velcro effect), coupling to two-level systems in the substrate, attachment losses, and thermoelastic losses. This task aims to compute the inverse quality factor \(Q^{-1}\) at room temperature (300 K) for each of these six mechanisms using analytic expressions and the system parameters of a typical graphene nanoresonator described in the literature.

## Approach
Compute \(Q^{-1}\) for each mechanism by evaluating the following analytic expressions at \(T = 300\,\text{K}\) with the resonator parameters listed below. All required constants are provided; no external lookup is needed.

**System parameters** (adapted from a representative device):
- Dimensions: length \(L = 1\,\mu\text{m}\), width \(w = 1\,\mu\text{m}\), thickness \(t = 10\,\text{nm}\).
- Height above gate: \(d = 300\,\text{nm}\).
- Resonance frequency: \(f_0 = 100\,\text{MHz}\) (\(\omega_0 = 2\pi f_0\)).
- Vibration amplitude: \(A = 0.5\,\text{nm}\).
- Carrier (charge) density in graphene: \(\rho_C = 10^{12}\,\text{cm}^{-2}\).
- Graphene mass density: \(\rho_M^C = 2200\,\text{kg/m}^3\).
- Young's modulus of graphene: \(E = 10^{12}\,\text{Pa}\).
- Poisson ratio of graphene: \(\nu = 0.16\).
- Debye temperature: \(\theta_D \approx 570\,\text{K}\).
- Specific heat of graphite: \(C_p = 700\,\text{J/(kg·K)}\).
- Thermal conductivity: \(\kappa = 390\,\text{W/(m·K)}\).
- Fermi velocity of graphene: \(v_F \approx 10^6\,\text{m/s}\).
- For the Si gate: assume \(D^C \nu^C = D^G \nu^G = 10^3\), and that the gate's electronic compressibility \(\nu^G\) is analogous to that of graphene.
- SiO₂ properties for attachment losses: mass density \(\rho_M^O = 2200\,\text{kg/m}^3\), Young's modulus \(E^O = 70\,\text{GPa}\), Poisson ratio \(\nu^O = 0.17\).
- Thermal expansion coefficient of graphene (in-plane, at 300 K): \(\alpha \approx 5 \times 10^{-6}\,\text{K}^{-1}\).
- For the two-level system calculation: density of TLS states \(P \approx 2 \times 10^{32}\,\text{J}^{-1}\text{m}^{-3}\), coupling energy \(\gamma \approx 1\,\text{eV}\), assume symmetrical TLSs \(\Delta_0^x/\epsilon \approx 1\), and maximum TLS energy \(\epsilon_{\text{max}} \approx 5\,\text{K} \times k_B\).

**Mechanism formulas**

1. **Static charges in SiO₂**: For a single graphene layer, the inverse quality factor per charge is
   \[
   Q^{-1}_{\text{charge}} \approx \frac{1}{k_F d}\,\frac{2\hbar}{M\omega_0 d^2},
   \]
   with \(k_F = \pi \sqrt{\rho_C}\) and \(M = \rho_M^C L w t\) the mass. Multiply by the total number of static charges \(N_{\text{ch}} = \rho_{\text{ch}} L w\), where an upper bound for the charge density is \(\rho_{\text{ch}} \approx 10^{12}\,\text{cm}^{-2}\). At finite temperature, this mechanism is ohmic, so \(Q^{-1}(T) \approx Q^{-1}(0) \times (k_B T / \hbar \omega_0)\).

2. **Ohmic losses in graphene and gate**:
   \[
   Q^{-1}(\omega_0) = \frac{\hbar Q_C^2}{2M\omega_0 d^2}\left(\frac{1}{\nu^C D^C} + \left(\frac{\nu^G}{\nu^C}\right)^2\frac{1}{\nu^G D^G}\right),
   \]
   where \(Q_C = L w \rho_C\). The compressibility for a single layer is \(\nu^C = E_F / (2\pi\hbar^2 v_F^2)\) with \(E_F = \hbar v_F k_F\). Use the given \(D\nu\) products and \(\nu^G = \nu^C\). The result is again ohmic and scales linearly with \(T\).

3. **Velcro effect**: Considered absent in the relevant regime; set \(Q^{-1}_{\text{velcro}} = 0\).

4. **Two-level systems**:
   \[
   \alpha = 4\left(\gamma\frac{\Delta_0^x}{\epsilon}\right)^2 \frac{(\rho_M^C)^{1/2}(1+\nu)^{3/2}(1-\nu)^{1/2}}{\hbar\,t^2\,E^{3/2}\left(9 + \frac{3\nu}{1-2\nu}\right)}.
   \]
   Then for \(k_B T > \epsilon_{\text{max}}\):
   \[
   Q^{-1}(\omega,T) \approx \frac{P\gamma^2}{E\,k_B T}\left(\frac{4\pi}{3}\alpha\,\epsilon_{\text{max}} + \frac{\pi^2}{3}\alpha^2 k_B T\right).
   \]
   At 300 K this applies; evaluate with the given constants.

5. **Attachment losses**:
   \[
   Q^{-1} \approx \frac{w}{L}\left(\frac{t}{d}\right)^2 \sqrt{\frac{\rho_M^C E^C\bigl(1-(\nu^O)^2\bigr)}{\rho_M^O E^O}}.
   \]
   Use the SiO₂ properties and graphene constants above.

6. **Thermoelastic losses**:
   \[
   Q^{-1}_Z(T) = \frac{E\,\alpha^2 T}{C_p}\,\frac{\omega_0\tau_Z}{1 + (\omega_0\tau_Z)^2},\qquad \tau_Z = \frac{t^2 C_p}{\pi^2\kappa}.
   \]
   Evaluate at \(T = 300\,\text{K}\) using the graphene parameters; for a 10 nm beam \(\omega_0\tau_Z \ll 1\).

## Reproduction target
Compute the inverse quality factor \(Q^{-1}\) at \(T=300\,\text{K}\) for each of the six dissipation mechanisms using the analytic expressions and system parameters described above. Determine which mechanism yields the largest \(Q^{-1}\). Write the results to a JSON file `results_Q_inv.json` with keys `static_charges_SiO2`, `ohmic_graphene_gate`, `velcro_effect`, `two_level_systems`, `attachment_losses`, `thermoelastic_losses` (numeric values), and `dominant_mechanism` (a string equal to one of the keys). The Velcro effect value must be 0.0 (or null).

## Assets
No external datasets, models, or tools are required beyond standard Python 3 with numpy for numerical computation. All necessary physical constants and material parameters are provided in the instruction.

## Workflow steps

### Step 1: Compute all dissipation contributions
- Role: scored
- Action: Implement the analytic expressions for the six dissipation mechanisms (static charges in SiO₂, ohmic losses in graphene and gate, Velcro effect, two-level systems, attachment losses, thermoelastic losses) from the paper's method description. Use the system parameters provided in the instruction (resonator dimensions, material constants, charge densities, etc.) and any needed publicly known standard constants. Evaluate each inverse quality factor Q⁻¹ at T=300 K. Set the Velcro effect contribution to 0 as the paper deems it absent. Determine which mechanism yields the largest Q⁻¹. Write the computed values and the dominant mechanism name to a JSON file.
- Output file: `/app/outputs/results_Q_inv.json`
- Format: json
- Contract: JSON object with keys: "static_charges_SiO2" (float), "ohmic_graphene_gate" (float), "velcro_effect" (float, must be 0.0 or null), "two_level_systems" (float), "attachment_losses" (float), "thermoelastic_losses" (float), and "dominant_mechanism" (string, one of the mechanism keys).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_Q_inv.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_Q_inv.json
- path: `/app/outputs/results_Q_inv.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Inverse quality factors Q^{-1} at 300 K for each dissipation mechanism and the dominant mechanism name.
- schema:
  - `type`: object
  - `required`: `static_charges_SiO2`, `ohmic_graphene_gate`, `velcro_effect`, `two_level_systems`, `attachment_losses`, `thermoelastic_losses`, `dominant_mechanism`
  - `properties`:
    - `static_charges_SiO2`:
      - `type`: number
    - `ohmic_graphene_gate`:
      - `type`: number
    - `velcro_effect`:
      - `type`: number
    - `two_level_systems`:
      - `type`: number
    - `attachment_losses`:
      - `type`: number
    - `thermoelastic_losses`:
      - `type`: number
    - `dominant_mechanism`:
      - `type`: string
      - `enum`: `static_charges_SiO2`, `ohmic_graphene_gate`, `velcro_effect`, `two_level_systems`, `attachment_losses`, `thermoelastic_losses`

Notes: The Velcro effect value must be 0.0 (or null) as deemed absent. The dominant_mechanism should be the key of the mechanism with the largest Q^{-1} value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_Q_inv.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "static_charges_SiO2",
          "ohmic_graphene_gate",
          "velcro_effect",
          "two_level_systems",
          "attachment_losses",
          "thermoelastic_losses",
          "dominant_mechanism"
        ],
        "properties": {
          "static_charges_SiO2": {
            "type": "number"
          },
          "ohmic_graphene_gate": {
            "type": "number"
          },
          "velcro_effect": {
            "type": "number"
          },
          "two_level_systems": {
            "type": "number"
          },
          "attachment_losses": {
            "type": "number"
          },
          "thermoelastic_losses": {
            "type": "number"
          },
          "dominant_mechanism": {
            "type": "string",
            "enum": [
              "static_charges_SiO2",
              "ohmic_graphene_gate",
              "velcro_effect",
              "two_level_systems",
              "attachment_losses",
              "thermoelastic_losses"
            ]
          }
        }
      },
      "description": "Inverse quality factors Q^{-1} at 300 K for each dissipation mechanism and the dominant mechanism name."
    }
  ],
  "notes": "The Velcro effect value must be 0.0 (or null) as deemed absent. The dominant_mechanism should be the key of the mechanism with the largest Q^{-1} value."
}
```

## How you are scored
A hidden verifier independently reads your submitted `results_Q_inv.json` and compares each computed \(Q^{-1}\) value to the reference result, using appropriate tolerances that account for numerical implementation differences. It also checks that the identified dominant mechanism matches the expected one. Each mechanism carries a different weight in the final score. Full credit is awarded when every computed value lies within its tolerance and the dominant mechanism is correct; partial credit is given for near misses. Reporting the paper's numbers without genuine computation will not pass, because the tolerances are chosen to require a correct implementation of the formulas.
