# Orientational ordering and layering transitions of hard plates in narrow slit pores via Parsons-Lee DFT

## Problem background
Hard platelike particles having edge lengths L, D, D (L < D) are confined in a narrow slit pore formed by two parallel hard walls. The pore width H is chosen such that L < H ≤ L + D, which forces the plates to form only a single layer when their long axes lie parallel to the walls (edge‑on) but allows several layers when the plates stand perpendicular to the walls (face‑on). This extreme confinement creates a competition between orientational and positional entropy, leading to a rich phase behaviour that may include multiple face‑on layers, an edge‑on monolayer, and various orientational ordering transitions as a function of packing fraction (η) and pore width. Understanding these ordering phenomena is important for colloidal science and liquid‑crystal technology. In this task, you will compute the equilibrium structures and the packing fractions at which transitions between them occur.

## Approach
The system is modelled using the Parsons–Lee density functional theory combined with a three‑state restricted orientation approximation: the main axes of the rectangular plates can point only along the x, y, or z Cartesian axes (the walls are perpendicular to the z‑axis). The grand potential functional for this ternary mixture of orientations is

βΩ = Σ_{i=x,y,z} ∫ dz ρ_i(z) [ln ρ_i(z) − 1 + βV_i^{ext}(z) − βμ]
      − (c/2) Σ_{i,j} ∫∫ dz dz′ ρ_i(z) ρ_j(z′) A_{ij}^{exc}(z,z′),

where ρ_i(z) is the number density of plates with orientation i at distance z from one wall, V_i^{ext}(z) is infinite if the plate overlaps with a wall, μ is the chemical potential, and A_{ij}^{exc}(z,z′) is the excluded area between two plates of orientations i and j located at z and z′. The prefactor c(η) = (1 − 3η/4)(1−η)^{−2} depends on the packing fraction η = ρ v_0 with v_0 = D^2 L the volume of one plate.

Minimisation yields the self‑consistent equations for the density profiles:

ρ_k(z) = H ρ exp[−c Σ_i ∫ dz′ ρ_i(z′) A_{ik}^{exc}(z,z′)] 
         / Σ_{j} ∫ dz″ exp[−c Σ_i ∫ dz′ ρ_i(z′) A_{ij}^{exc}(z′,z″)]  (k = x, y, z).

From the converged density profiles you obtain the orientational mole fractions X_i = ∫ ρ_i(z) dz / Σ_j ∫ ρ_j(z) dz and the equilibrium grand potential, pressure, and chemical potential. Different structures (e.g., n face‑on layers, an edge‑on monolayer, biaxial edge‑on) correspond to distinct solutions of these equations. First‑order phase transitions between structures are located by equating pressure and chemical potential. Continuous structural changes (e.g., a gradual swap from face‑on to edge‑on dominance) are characterised by the crossing of X_z = 0.5 or the emergence of biaxiality (X_x > X_y > X_z). You must implement this theory from scratch, using only the public resources listed.

## Reproduction target
For the prescribed (L/D, H/D) combinations listed below, compute the first‑order phase‑transition packing fractions η (and, where applicable, the η values marking continuous structural changes) and write them to `/app/outputs/transitions.json`.

1. L/D = 0.6, H/D = 1.1.  Report the packing fraction at which the dominant orientation changes from face‑on to edge‑on (X_z crosses 0.5) as a "1LFO" → "1LEO" transition, and the packing fraction at which biaxial edge‑on order emerges (X_x > X_y > X_z) as a "1LEO" → "1LBO" transition.

2. L/D = 0.3, H/D = 1.0, 1.04, 1.2, 1.3.  For each H/D, report any first‑order layering transition between n‑layer face‑on structures ("2L" ↔ "3L", "3L" ↔ "4L", etc.) and any first‑order transition between an n‑layer face‑on structure and a biaxial edge‑on monolayer ("1LBO").

3. L/D = 0.2, H/D = 1.1.  Report the layering transition(s) that occur, e.g., "3L" ↔ "4L".

4. L/D = 0.15, H/D = 0.9.  Report the layering transition(s), e.g., "3L" ↔ "4L".

5. L/D = 0.1, H/D = 0.775.  Report the layering transition(s), e.g., "5L" ↔ "6L".

Each entry in transitions.json must have keys `L_over_D`, `H_over_D`, `phase_A`, `phase_B`, and `transition_eta`. Use the phase labels exactly as indicated here: "1LFO", "1LEO", "1LBO", "2L", "3L", "4L", "5L", etc.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Excluded Area Kernels
- Role: process
- Action: Set up a discretized z-grid and compute the excluded area matrices A_{ij}^{exc}(z, z') for hard plates with the given aspect ratio L/D and pore width H/D. The matrices are needed for all subsequent DFT calculations.
- Evidence: `/app/outputs/excluded_area.npz`

### Step 2: DFT Solver and Thermodynamic Calculation
- Role: process
- Action: For a dense grid of packing fractions eta, solve the orientation-resolved self-consistent equations to obtain the equilibrium density profiles rho_x(z), rho_y(z), rho_z(z) and mole fractions X_i. Using these profiles and the Parsons-Lee prefactor, compute the grand potential, pressure, and chemical potential. Save the thermodynamic data (eta, P, mu, X_i, and a structure label) to an intermediate file for phase coexistence analysis.
- Evidence: `/app/outputs/thermodynamics.npz`

### Step 3: Determine Phase Transition Points
- Role: scored (load-bearing)
- Action: From the thermodynamic data, locate first-order phase transitions by equating pressure and chemical potential between competing structures (e.g., 2L <-> 3L, 3L <-> 4L, 1LBO <-> 3L, 1LBO <-> 4L). For each prescribed combination of L/D and H/D, output the transition packing fraction. If a continuous structural change occurs (e.g., 1LFO -> 1LEO -> 1LBO), include the corresponding eta where the change occurs, using the phase labels consistent with the paper.
- Output file: `/app/outputs/transitions.json`
- Format: json
- Contract: A JSON array of objects. Each object must have: "L_over_D" (float), "H_over_D" (float), "phase_A" (string), "phase_B" (string), "transition_eta" (float). Phase labels use the notation: "1LFO", "1LEO", "1LBO", "2L", "3L", "4L", "5L", ...
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transitions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transitions.json
- path: `/app/outputs/transitions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Array of phase transition points; each entry gives the plate aspect ratio, pore width, the two coexisting or structurally changing phases, and the packing fraction at the transition.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `L_over_D`, `H_over_D`, `phase_A`, `phase_B`, `transition_eta`
    - `properties`:
      - `L_over_D`:
        - `type`: number
      - `H_over_D`:
        - `type`: number
      - `phase_A`:
        - `type`: string
      - `phase_B`:
        - `type`: string
      - `transition_eta`:
        - `type`: number

Notes: The numeric values are scored against hidden reference data from the paper's phase diagrams with a tolerance on transition_eta. The ordering of continuous structural changes (e.g., 1LFO->1LEO->1LBO) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transitions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "L_over_D",
            "H_over_D",
            "phase_A",
            "phase_B",
            "transition_eta"
          ],
          "properties": {
            "L_over_D": {
              "type": "number"
            },
            "H_over_D": {
              "type": "number"
            },
            "phase_A": {
              "type": "string"
            },
            "phase_B": {
              "type": "string"
            },
            "transition_eta": {
              "type": "number"
            }
          }
        }
      },
      "description": "Array of phase transition points; each entry gives the plate aspect ratio, pore width, the two coexisting or structurally changing phases, and the packing fraction at the transition."
    }
  ],
  "notes": "The numeric values are scored against hidden reference data from the paper's phase diagrams with a tolerance on transition_eta. The ordering of continuous structural changes (e.g., 1LFO->1LEO->1LBO) is also verified."
}
```

## How you are scored
A hidden verifier will independently score your `/app/outputs/transitions.json` against reference transitions obtained from the original study. For each first‑order transition point, your reported `transition_eta` is compared to the expected value; a correct entry (within a pre‑defined tolerance) earns full credit, and the score degrades as the discrepancy grows. For continuous structural changes (L/D = 0.6), the verifier checks that the sequence of phases you report is correct and that the associated packing fractions fall within a reasonable window. The final reward is the weighted combination of these scores; simply writing a JSON file without having performed the actual DFT calculation will not yield a high score.
