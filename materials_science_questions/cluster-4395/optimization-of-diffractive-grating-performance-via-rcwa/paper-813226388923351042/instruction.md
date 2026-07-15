# Phase-dependent DBR grating performance characterization using RCWA

## Problem background
Distributed Bragg reflector (DBR) gratings are widely used in photonic integrated circuits as wavelength-selective reflectors and filters. This task investigates a phase‑dependent, double‑input DBR grating. Two counter‑propagating optical input signals, each with controlled phase and equal amplitude, are launched into opposite ends of the grating. The interference between them can steer the output power to either side, making the structure a potential building block for optical switching and routing. The central question is how the phase difference between the two inputs and the grating length together determine the output power efficiencies at the left and right ends.

## Approach
The analysis relies on rigorous electromagnetic simulation. First, the waveguide layer structure that hosts the grating is obtained from a published reference. The fundamental guided‑mode propagation constant β at the free‑space wavelength of 1550 nm is computed by solving the slab‑waveguide eigenvalue problem. Next, a rigorous coupled‑wave analysis (RCWA) or an equivalent coupled‑mode / transfer‑matrix method is used to model the first‑order grating, which has a period of 0.23886 μm. For equal‑amplitude counter‑propagating inputs, the reflected and transmitted powers are calculated as functions of the relative phase difference between the two inputs and the grating length L. The resulting power‑efficiency curves reveal the conditions for direction‑controlled transmission and reflection.

## Reproduction target
Produce a single JSON results file containing the following seven quantities:
- For a 50 μm long grating, the normalized output power efficiencies at the left and right ends when the two input waves are in phase (0° phase difference) and when they are out of phase (180° phase difference).
- The grating length that causes a 2π phase shift, L_2π, computed as 2π/β.
- For a 200 μm long grating, the phase differences (in degrees) that yield 100% transmission and 100% reflection, together with the corresponding power efficiencies at the right and left ends, respectively.

## Assets

- Butler et al., J. Lightwave Technol. 16, 1038 (1998): 10.1109/50.678614
- NumPy: https://numpy.org
- SciPy: https://scipy.org

## Workflow steps

### Step 1: Extract waveguide structure parameters
- Role: process
- Action: Retrieve the layer thicknesses and refractive indices of the waveguide structure from Butler et al., J. Lightwave Technol. 16, 1038 (1998).
- Evidence: `/app/outputs/waveguide_params.txt`

### Step 2: Compute propagation constant and 2π length
- Role: process
- Action: Solve the waveguide eigenvalue problem for the fundamental mode at free‑space wavelength 1550 nm using the extracted waveguide parameters to obtain the propagation constant β. Compute the characteristic 2π length L = 2π/β.
- Evidence: `/app/outputs/beta.json`

### Step 3: Simulate double-input DBR grating
- Role: process
- Action: Implement RCWA (or an equivalent transfer‑matrix/coupled‑mode method) for the double‑input DBR grating with period 0.23886 μm, using the waveguide structure and propagation constant from previous steps. Sweep grating lengths in the range of interest (e.g., 0–500 μm) and input phase differences (0° to 360°) for equal‑amplitude counter‑propagating inputs, and record the reflected and transmitted powers at both ends. Save the simulation data for later processing.
- Evidence: `/app/outputs/simulation_output.npz`

### Step 4: Compute key performance metrics
- Role: scored (load-bearing)
- Action: From the simulation data and the propagation constant, extract the following quantities: (a) output power efficiencies at left and right ends for a 50 μm grating at 0° and 180° phase difference; (b) the grating length L that causes a 2π phase shift (L = 2π/β); (c) the phase differences that yield 100% transmission and 100% reflection for a 200 μm grating. Write these values to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"efficiency_50um_0deg_left": float, "efficiency_50um_0deg_right": float, "efficiency_50um_180deg_left": float, "efficiency_50um_180deg_right": float, "L_2pi_um": float, "phase_200um_transmission_deg": float, "efficiency_200um_transmission_right": float, "phase_200um_reflection_deg": float, "efficiency_200um_reflection_left": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final computed performance metrics of the phase-dependent DBR grating.
- schema:
  - `type`: object
  - `required`: `efficiency_50um_0deg_left`, `efficiency_50um_0deg_right`, `efficiency_50um_180deg_left`, `efficiency_50um_180deg_right`, `L_2pi_um`, `phase_200um_transmission_deg`, `efficiency_200um_transmission_right`, `phase_200um_reflection_deg`, `efficiency_200um_reflection_left`
  - `items`: object
  - `units`:
    - `efficiency_50um_0deg_left`: fraction (0-1)
    - `efficiency_50um_0deg_right`: fraction (0-1)
    - `efficiency_50um_180deg_left`: fraction (0-1)
    - `efficiency_50um_180deg_right`: fraction (0-1)
    - `L_2pi_um`: micrometers
    - `phase_200um_transmission_deg`: degrees
    - `efficiency_200um_transmission_right`: fraction (0-1)
    - `phase_200um_reflection_deg`: degrees
    - `efficiency_200um_reflection_left`: fraction (0-1)

Notes: The hidden verifier compares these fields against reference values derived from the paper, with appropriate absolute tolerances. The phase fields are required to ensure the solver actually discovers the optimal phase conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "efficiency_50um_0deg_left",
          "efficiency_50um_0deg_right",
          "efficiency_50um_180deg_left",
          "efficiency_50um_180deg_right",
          "L_2pi_um",
          "phase_200um_transmission_deg",
          "efficiency_200um_transmission_right",
          "phase_200um_reflection_deg",
          "efficiency_200um_reflection_left"
        ],
        "items": {},
        "units": {
          "efficiency_50um_0deg_left": "fraction (0-1)",
          "efficiency_50um_0deg_right": "fraction (0-1)",
          "efficiency_50um_180deg_left": "fraction (0-1)",
          "efficiency_50um_180deg_right": "fraction (0-1)",
          "L_2pi_um": "micrometers",
          "phase_200um_transmission_deg": "degrees",
          "efficiency_200um_transmission_right": "fraction (0-1)",
          "phase_200um_reflection_deg": "degrees",
          "efficiency_200um_reflection_left": "fraction (0-1)"
        }
      },
      "description": "Final computed performance metrics of the phase-dependent DBR grating."
    }
  ],
  "notes": "The hidden verifier compares these fields against reference values derived from the paper, with appropriate absolute tolerances. The phase fields are required to ensure the solver actually discovers the optimal phase conditions."
}
```

## How you are scored
A hidden verifier checks each workflow stage’s artifact against reference values derived from the original work. The final score is a weighted combination of the individual stage scores. Only the quantities written to the scored output file (`results.json`) are compared; intermediate evidence files are audited for process completeness. The verifier uses a fixed absolute tolerance for each numeric field. Reporting the paper’s numbers without executing the described workflow will not succeed, because the verifier expects the results to emerge from the required simulation and analysis steps.
