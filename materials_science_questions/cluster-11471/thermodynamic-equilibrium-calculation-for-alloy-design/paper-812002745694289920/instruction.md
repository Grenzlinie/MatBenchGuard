# Microstructural Evolution Simulation for Directional Solidification of Ductile Iron

## Problem background
Directional solidification of ductile cast iron produces a spatially varying microstructure — including graphite, ferrite, pearlite, and iron carbide — that determines the mechanical properties of the casting. A coupled heat flow and microstructural evolution model has been proposed to predict these as-cast phase fractions as a function of distance from the chilled end, using only the alloy composition and melt treatment parameters. The goal is to implement this model for a reference casting and evaluate its predictions.

## Approach
The computation couples a 1‑D finite‑difference heat conduction solver, a fading‑based nodule count predictor, and a set of state‑variable ordinary differential equations (ODEs) to simulate microstructural evolution during directional solidification. The cooling curves at each position are obtained by solving the transient heat conduction equation (Eq. 1) with temperature‑dependent thermal properties and boundary conditions. The local graphite nodule count is computed from the fading model (Eq. 2). The four state variables Φ, X, Y, Z are integrated using the local cooling rate, nodule count, and material‑specific time constants. Finally, response equations (Eqs. 3‑6) convert the terminal state‑variable values into volume fractions of graphite, ferrite, pearlite, and iron carbide. All required numerical parameters are listed in Tables 1 and 2.

## Model equations

### 1. Heat conduction
The temperature $T(x,t)$ is governed by the 1‑D heat equation with latent heat release:

$$\frac{\partial T}{\partial t} = \frac{1}{\rho c} \frac{\partial}{\partial x}\left(\lambda \frac{\partial T}{\partial x}\right) + \frac{L}{\rho c} \frac{\partial f}{\partial t} \qquad (1)$$

where $\lambda$ is the thermal conductivity, $\rho c$ the volume heat capacity, $L$ the latent heat of transformation, and $f$ the volume fraction of transformation product.  
Boundary conditions:
- At the chilled end ($x=0$): a temperature‑dependent heat transfer coefficient $h(T)$ is applied.
- At the top of the bar ($x=140$ mm): insulated (adiabatic) boundary.
The latent heat is released in three steps associated with the graphite/austenite eutectic ($L_1$), the ledeburite eutectic ($L_2$), and the eutectoid transformation ($L_3$). $f$ is the fraction of the respective phase that has transformed during the ongoing reaction.

### 2. Fading model (inclusion coarsening)
The local number density of graphite nodules $N(l)$ relative to the reference density $N_r$ at the chilled end follows:

$$\frac{N}{N_r} = \left(\frac{d_0}{d}\right)^3 \qquad (2)$$

where $d_0$ is the inclusion diameter at the chilled end and $d$ is the inclusion diameter at position $l$. The inclusion diameter evolves according to the coarsening law

$$\frac{\mathrm{d} d}{\mathrm{d} t} = \frac{2 k_i}{d},$$

with $k_i = 0.011\;\mu\text{m}^3\text{s}^{-1}$ (coarsening constant). The total growth is integrated over the time from pouring until the start of solidification, using the thermal history.

### 3. State‑variable ODEs
The microstructural state is described by four variables $\Phi$, $X$, $Y$, $Z$, whose time evolution is given by simple first‑order kinetics:

$$
\frac{\mathrm{d}\Phi}{\mathrm{d}t} = \frac{1}{\tau_1}(1-\Phi) \quad \text{if } T < T_{e,s} \text{ and } \Phi < 1, \quad \text{else } 0
$$
$$
\frac{\mathrm{d}X}{\mathrm{d}t} = \frac{1}{\tau_2}(1-X) \quad \text{if } T < T_{e,m} \text{ and } X < 1, \quad \text{else } 0
$$
$$
\frac{\mathrm{d}Y}{\mathrm{d}t} = \frac{1}{\tau_3}(1-Y) \quad \text{if } T < T_{e,s} \text{ and after solidification, else } 0
$$
$$
\frac{\mathrm{d}Z}{\mathrm{d}t} = \frac{1}{\tau_4}(1-Z) \quad \text{if } T < T_{eu} \text{ and } Z < 1, \quad \text{else } 0
$$

The time constants $\tau_i$ depend on the local nodule count $N$ and cooling rate:

$$\tau_1 = \frac{A_1}{N^{1/3} \, (-\dot{T})}, \quad \tau_2 = \frac{A_2}{N^{1/3} \, (-\dot{T})}, \quad \tau_3 = \frac{A_3}{N^{1/3} \, (-\dot{T})}, \quad \tau_4 = \frac{A_4}{N^{1/3} \, (-\dot{T})}$$

with $A_1 = 1.2\times10^9\;\text{s}^{2/3}$, $A_2 = 1.0\times10^9\;\text{s}^{2/3}$, $A_3 = 0.8\times10^9\;\text{s}^{2/3}$, $A_4 = 4.5\times N_r^{1/3}\;\text{s}^{2/3}$ (where $N_r$ is the reference nodule count). The cooling rate $-\dot{T}$ is evaluated locally at the start of the transformation from the heat‑flow solution. The critical temperatures are:
- $T_{e,s} = 1154\;^\circ\text{C}$ (stable eutectic temperature)
- $T_{e,m} = 1148\;^\circ\text{C}$ (metastable eutectic temperature)
- $T_{eu} = 740\;^\circ\text{C}$ (eutectoid temperature)
- Graphite nucleation temperature $T_{n,s} = 1160\;^\circ\text{C}$.

### 4. Response equations
The final volume fractions (in vol%) are obtained from the terminal values of the state variables after cooling to room temperature:

$$
\begin{aligned}
G &= 100 \cdot (\Phi_{\text{end}} + 0.1\,Y_{\text{end}}) \\
F &= 100 \cdot (0.95\,(1-X_{\text{end}}) - 0.5\,Z_{\text{end}}) \\
P &= 100 \cdot (0.95\,(1-X_{\text{end}}) - F/100) \\
C &= 100 \cdot X_{\text{end}}
\end{aligned}
$$

where $\Phi_{\text{end}}$, etc., are the values at the end of the simulation. These relations ensure that the phase fractions sum to approximately 100 vol% and reflect the physical constraints imposed by the Fe‑C phase diagram.

### 5. Thermal and process parameters (Tables 1–2)

**Table 1. Heat transfer coefficients**
| Symbol | Value (J s⁻¹ m⁻² K⁻¹) | Regime |
|--------|------------------------|--------|
| h₁a    | 1200 | liquid metal |
| h₁b    | 1000 | solidification (primary) |
| h₂a    | 800  | austenite regime |
| h₂b    | 400  | post‑eutectoid |

**Table 2. Thermal properties**
| Property | Symbol | Value |
|----------|--------|-------|
| Liquid thermal conductivity | λ* | 200 J s⁻¹ m⁻¹ K⁻¹ |
| Solid thermal conductivity | λ  | 35 J s⁻¹ m⁻¹ K⁻¹ |
| Volume heat capacity (liquid) | ρc | 6.125 × 10⁶ J m⁻³ K⁻¹ |
| Volume heat capacity (solid) | ρc_s | 6.110 × 10⁶ J m⁻³ K⁻¹ |
| Latent heat, stable eutectic | L₁ | 1.23 × 10⁹ J m⁻³ |
| Latent heat, metastable eutectic | L₂ | 1.0 × 10⁹ J m⁻³ |
| Latent heat, eutectoid | L₃ | 1.53 × 10⁸ J m⁻³ |

**Other parameters**
- Reference nodule count $N_r = 9.1\; \times 10^9\;\text{m}^{-3}$ (9100 mm⁻³)
- Initial inclusion diameter $d_0 = 1\;\mu\text{m}$
- Coarsening constant $k_i = 0.011\;\mu\text{m}^3\text{s}^{-1}$
- Graphite nucleation temperature $T_{n,s} = 1160\;^\circ\text{C}$
- Bar geometry: length 140 mm, diameter 40 mm; one‑dimensional model with cross‑sectional area corresponding to the mould diameter (approximate as a slab of equal volume).
- Pouring temperature $T_{\text{pour}} = 1350\;^\circ\text{C}$, mould initial temperature 30 °C, time step 0.1 s.

## Reproduction target
Implement the coupled heat‑flow and microstructural model for the reference casting: a 40‑mm‑diameter, 140‑mm‑long insulated mold cooled from the bottom by a water‑cooled copper chill, using the reference iron composition (C 3.51, Si 2.13, Mn <0.03, S 0.007, P 0.025, Mg 0.042, Ti 0.016, Al 0.014, Pb <0.006 wt%). Compute the final volume fractions of graphite, ferrite, pearlite, and iron carbide at positions l = 10, 15, 35, 55, and 95 mm from the chilled end. Write the predictions to `/app/outputs/step_01_predictions.csv` with columns `l` (mm), `graphite` (vol%), `ferrite` (vol%), `pearlite` (vol%), and `iron_carbide` (vol%); one row per position. The intermediate cooling curves, nodule counts, and state‑variable trajectories must be saved as evidence in `/app/outputs/temperature_profiles.csv`, `/app/outputs/nodule_count.csv`, and `/app/outputs/state_variables.csv`, respectively, but only the final volume‑fraction predictions will be scored.

## Assets
No external datasets or pre‑trained models are required. All numerical parameters (thermal properties, heat transfer coefficients, nucleation temperature, time constants, inclusion coarsening constant) are fully specified in the problem description and the reference casting conditions above. The implementation is expected to be in Python (≥3.8) using standard scientific libraries such as NumPy and SciPy.

## Workflow steps

### Step 1: Numerical heat flow simulation
- Role: process
- Action: Solve the 1‑D heat conduction equation with latent heat release using the finite difference method, applying the paper‑specified thermal properties, heat transfer coefficients, and boundary conditions. Obtain temperature‑time profiles at the bar positions of interest.
- Evidence: `/app/outputs/temperature_profiles.csv`

### Step 2: Graphite nodule count prediction (fading model)
- Role: process
- Action: Compute the inclusion diameter and resulting graphite nodule count as a function of position using the paper’s fading/inclusion coarsening model with the given coarsening constant and initial diameter.
- Evidence: `/app/outputs/nodule_count.csv`

### Step 3: Microstructural state variable integration
- Role: process
- Action: Solve the coupled ordinary differential equations for the four primary state variables (Φ, X, Y, Z) at each spatial position, using the local cooling curves, the nodule count, and the paper‑specified time constants and nucleation temperature.
- Evidence: `/app/outputs/state_variables.csv`

### Step 4: Convert to volume fractions and output predictions
- Role: scored (load-bearing)
- Action: Apply the response equations to the terminal values of the state variables to obtain the volume fractions of graphite, ferrite, pearlite, and iron carbide. Write the predictions for positions 10, 15, 35, 55, and 95 mm to a CSV file.
- Output file: `/app/outputs/step_01_predictions.csv`
- Format: csv
- Contract: l (mm), graphite (vol%), ferrite (vol%), pearlite (vol%), iron_carbide (vol%); one row per position.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_predictions.csv
- path: `/app/outputs/step_01_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted volume fractions of graphite, ferrite, pearlite, and iron carbide at five positions along the bar, to be compared against hidden experimental reference values.
- schema:
  - `type`: table
  - `required_columns`: `l`, `graphite`, `ferrite`, `pearlite`, `iron_carbide`
  - `units`:
    - `l`: mm
    - `graphite`: vol%
    - `ferrite`: vol%
    - `pearlite`: vol%
    - `iron_carbide`: vol%

Notes: The hidden checker compares each predicted value to the corresponding measured volume fraction from the paper’s Table II, applying per‑phase tolerances (wider for iron carbide at 10 mm to accommodate known model underestimation). The three required process steps (heat flow, nodule count, state variable integration) are not scored but are enforced because the downstream scored step is load‑bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l",
          "graphite",
          "ferrite",
          "pearlite",
          "iron_carbide"
        ],
        "units": {
          "l": "mm",
          "graphite": "vol%",
          "ferrite": "vol%",
          "pearlite": "vol%",
          "iron_carbide": "vol%"
        }
      },
      "description": "Predicted volume fractions of graphite, ferrite, pearlite, and iron carbide at five positions along the bar, to be compared against hidden experimental reference values."
    }
  ],
  "notes": "The hidden checker compares each predicted value to the corresponding measured volume fraction from the paper’s Table II, applying per‑phase tolerances (wider for iron carbide at 10 mm to accommodate known model underestimation). The three required process steps (heat flow, nodule count, state variable integration) are not scored but are enforced because the downstream scored step is load‑bearing."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/step_01_predictions.csv` and compare each predicted volume fraction to a hidden experimental measurement for the same position and phase. The reward is the fraction of the 20 predicted values (5 positions × 4 phases) that fall within a per‑phase absolute tolerance. Tolerances are not disclosed. The result is a single float between 0 and 1. Your output file must strictly follow the specified format; any deviation may prevent the verifier from parsing it correctly.
