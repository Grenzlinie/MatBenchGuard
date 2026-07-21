# PTA-based MD simulation of uniaxial tension in Al nanocrystals

## Problem background
Molecular dynamics (MD) simulations of crystalline solids under slow loading are severely limited by the huge separation between atomic vibration timescales (femtoseconds) and experimentally relevant deformation rates (seconds). The Practical Time Averaging (PTA) framework overcomes this limitation by defining slow variables as running-time averages of fast atomistic state functions and evolving them on the loading timescale, avoiding explicit integration of the full fast dynamics. This work applies PTA to MD simulations of face‑centered cubic (FCC) aluminum nanocrystals to obtain stress–strain curves and yield strengths at quasi‑static strain rates, and to examine how mechanical response depends on sample size.

## PTA algorithm – detailed implementation

The PTA algorithm treats the MD system as a singularly perturbed evolution with a fast (atomistic) time scale and a slow (loading) time scale. The small parameter \(\epsilon = T_f / T_s\) (order \(10^{-15}\)) reflects the enormous timescale separation. The slow loading is the applied engineering strain \(\varepsilon(t)\), which evolves at constant rate \(\dot\varepsilon = 10^{-3}\,\text{s}^{-1}\).

### H‑observables
For a state function of the fast dynamics \(m(x)\) (e.g., normal stress, kinetic energy, potential energy), the corresponding slow variable – called an H‑observable – is defined as

\[
v_m(t) = \frac{1}{\Delta} \int_{t-\Delta}^{t} \langle m \rangle_{\mu(s)} \, ds,
\]

where \(\langle m \rangle_{\mu(s)}\) is the instantaneous time average of \(m\) from a short MD burst at the slow time \(s\), and \(\Delta\) is the averaging window length on the slow time scale.

### Slow time stepping
Discretise the slow time into steps indexed by \(n = 0,1,2,\dots\) with a prescribed strain increment \(\Delta\varepsilon\):

\[
t_n = n\,\Delta t_s,\qquad \varepsilon_n = n\,\Delta\varepsilon,
\]

where \(\Delta t_s = \Delta\varepsilon / \dot\varepsilon\). A typical choice is \(\Delta\varepsilon = 0.001\) (0.1% strain), giving \(\Delta t_s = 1\,\text{s}\).

At each slow step \(n\):

1. **Apply strain** – Enforce the current strain \(\varepsilon_n\) by displacing the right boundary atoms while keeping the left boundary fixed.

2. **Short MD burst** – Run a short MD simulation (fast dynamics) with the current atomic configuration, using LAMMPS, the Mishin EAM potential, a time step \(\delta t = 1\,\text{fs}\), and an NVE (or NVT) ensemble. The burst consists of:
   - \(N_{\text{eq}}\) equilibration steps,
   - \(N_{\text{avg}}\) sampling steps.
   During the sampling phase, record instantaneous values of the state functions:
   - \(\sigma_{xx}(k)\) – the normal stress in the loading direction (computed via the virial and divided by the sample volume),
   - \(KE(k)\) – total kinetic energy,
   - \(PE(k)\) – total potential energy.

   The instantaneous time average \(\langle \sigma_{xx} \rangle_n\) for this slow step is taken as the arithmetic mean over the sampling steps:
   \[
   \langle \sigma_{xx} \rangle_n = \frac{1}{N_{\text{avg}}} \sum_{k=1}^{N_{\text{avg}}} \sigma_{xx}(k).
   \]
   (Analogous averages are computed for KE and PE, but only the stress is required for the stress–strain curve.)

3. **Maintain a buffer** – Keep a circular buffer of the last \(M\) values of \(\langle \sigma_{xx} \rangle\) (one for each completed slow step). The averaging window on the slow scale is \(\Delta = M\,\Delta t_s\).

4. **Compute the current H‑observable** – Approximate the integral using the composite trapezoidal rule over the buffer:
   \[
   v_n = \frac{1}{\Delta} \sum_{i=n-M+1}^{n} w_i \langle \sigma_{xx} \rangle_i \, \Delta t_s,
   \]
   where \(w_i\) are trapezoidal weights (equal spacing). This yields the slow‑scale averaged stress at step \(n\), denoted \(v_n\).

5. **Extrapolation** – Once at least two H‑observable values are known (\(n\ge 2\)), linearly extrapolate to predict the value at step \(n+1\):
   \[
   v_{n+1}^{\text{pred}} = 2 v_n - v_{n-1}.
   \]

6. **Reconstruction (Simpson’s rule)** – Every \(K\) steps (e.g., \(K = 5\)), perform a higher‑order reconstruction of \(v_{n+1}\) using the last \(L\) values of \(\langle \sigma_{xx} \rangle\) from the buffer (choose an odd number, e.g. \(L = 5\)) and Simpson’s \(1/3\) rule. Compare the extrapolated prediction with the reconstructed value. If the relative deviation exceeds a tolerance \(\tau\) (e.g., \(\tau = 0.05\)), replace the prediction by the reconstruction:
   \[
   v_{n+1} = v_{n+1}^{\text{recon}}.
   \]
   This detects and corrects for nonlinear drifts that linear extrapolation misses.

7. **Jump detection** – Compute the standard deviation \(\sigma_{\text{buffer}}\) of the recent \(\langle \sigma_{xx} \rangle\) values in the buffer. If the newest value \(\langle \sigma_{xx} \rangle_n\) deviates from the linear trend (i.e., from the extrapolation line) by more than \(N_\sigma \sigma_{\text{buffer}}\) (e.g., \(N_\sigma = 3\)), a jump is declared. In that case, discard the extrapolated/reconstructed \(v_{n+1}\) and instead use the direct average \(\langle \sigma_{xx} \rangle_n\) as the accepted stress value for step \(n\) (and reset the H‑observable history to the post‑jump values, including this one).

8. **Accept slow step** – The stress–strain data point \((\varepsilon_n, \sigma_n^{\text{pta}})\) is recorded, where \(\sigma_n^{\text{pta}}\) is the final accepted value (\(v_n\) from step 4, possibly corrected by steps 6 or 7). Update the atomic configuration to the one at the end of the burst (or to the pre‑jump configuration if a jump was detected – in that case re‑run a short burst from the pre‑jump structure to obtain a consistent post‑jump state).

9. **Advance strain** and go to step 1.

This loop continues until a terminal strain of at least 20 % is reached.

### Recommended parameter values
These values are informed by the original PTA literature and the timescales of the problem; they are starting points that may be tuned slightly:

| Parameter                     | Symbol     | Value            |
|-------------------------------|------------|------------------|
| MD time step                  | \(\delta t\) | 1 fs            |
| Burst equilibration steps     | \(N_{\text{eq}}\) | 2000         |
| Burst sampling steps          | \(N_{\text{avg}}\)| 10000       |
| Buffer size (slow steps)      | \(M\)       | 20               |
| Strain increment              | \(\Delta\varepsilon\) | 0.001  |
| Extrapolation/reconstruction period | \(K\)  | 5                |
| Reconstruction window length  | \(L\)       | 5                |
| Reconstruction tolerance      | \(\tau\)    | 0.05 (5%)        |
| Jump threshold (sigma‑multiple)| \(N_\sigma\) | 3              |

## Reproduction target
Perform the PTA‑guided MD simulations described above for both the 8 nm and 20 nm Al nanocrystals under uniaxial tension at a strain rate of \(10^{-3}\,\text{s}^{-1}\). From each simulation, produce a stress–strain curve (strain vs. averaged normal stress in GPa) and determine the yield strength – the stress at which the first significant load drop associated with dislocation nucleation occurs. Save the two stress–strain curves as CSV files and the two yield strengths as a JSON file (keys `"8nm"` and `"20nm"`). The results should reveal the mechanical response and allow assessment of the size effect on yield strength.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/download.html
- Mishin EAM potential for Al: https://www.ctcms.nist.gov/potentials/entry/1999--Mishin-Y-Farkas-D-Mehl-M-J-Papaconstantopoulos-D-A--Al/

## Workflow steps

### Step 1: Generate initial atomistic configurations
- Role: process
- Action: Create FCC Al blocks of side length 8 nm and 20 nm with lattice parameter 4.05 Å, crystal orientation [100] along x, y, z. Assign initial atomic velocities from a Maxwell–Boltzmann distribution at 300 K. Produce initial LAMMPS data files for each sample.
- Evidence: none

### Step 2: Thermal relaxation to stress-free state
- Role: process
- Action: For each sample, run MD with left boundary atoms fixed and right boundary free until the reaction force on the right boundary vanishes, using the Mishin EAM potential. Output stress‑free atomic configurations (LAMMPS restart files) for later loading.
- Evidence: none

### Step 3: PTA-guided MD simulation under uniaxial tension
- Role: process
- Action: For each sample (8 nm and 20 nm), apply uniaxial tensile loading at a constant strain rate of \(10^{-3}\,\text{s}^{-1}\) along the x‑direction using the Practical Time Averaging algorithm detailed in the **PTA algorithm** section above. Simulate up to at least 20 % strain. During the simulation, record at each accepted slow step the strain \(\varepsilon_n\) and the corresponding PTA‑averaged normal stress \(\sigma_n^{\text{pta}}\) (in GPa).
- Evidence: none

### Step 4: Extract stress–strain curve for 8 nm sample
- Role: scored (load‑bearing)
- Action: From the PTA simulation output of the 8 nm sample, collect the strain and the corresponding averaged normal stress at every accepted slow step. Write a CSV file with columns `strain`, `stress_GPa`.
- Output file: `/app/outputs/step_04a_stress_strain_8nm.csv`
- Format: csv
- Contract: CSV with header: `strain,stress_GPa`. Each row contains a strain value (dimensionless) and the averaged normal stress in GPa (float).
- Scoring: scored by hidden verifier

### Step 5: Extract stress–strain curve for 20 nm sample
- Role: scored (load‑bearing)
- Action: From the PTA simulation output of the 20 nm sample, collect the strain and the corresponding averaged normal stress at every accepted slow step. Write a CSV file with columns `strain`, `stress_GPa`.
- Output file: `/app/outputs/step_04b_stress_strain_20nm.csv`
- Format: csv
- Contract: CSV with header: `strain,stress_GPa`. Each row contains a strain value (dimensionless) and the averaged normal stress in GPa (float).
- Scoring: scored by hidden verifier

### Step 6: Determine yield strengths
- Role: scored
- Action: From the two stress–strain curves, determine the yield strength for each sample as the stress value (in GPa) at the first significant load drop (corresponding to dislocation nucleation). Write a JSON file with keys `"8nm"` and `"20nm"` and their respective yield strengths.
- Output file: `/app/outputs/step_05_yield_strengths.json`
- Format: json
- Contract: JSON object: `{"8nm": <yield stress in GPa> (float), "20nm": <yield stress in GPa> (float)}`
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04a_stress_strain_8nm.csv`
- `/app/outputs/step_04b_stress_strain_20nm.csv`
- `/app/outputs/step_05_yield_strengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04a_stress_strain_8nm.csv
- path: `/app/outputs/step_04a_stress_strain_8nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress–strain curve for 8 nm sample under uniaxial tension at \(10^{-3}\,\text{s}^{-1}\). Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.).
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_GPa`
  - `units`:
    - `strain`: dimensionless
    - `stress_GPa`: GPa

### step_04b_stress_strain_20nm.csv
- path: `/app/outputs/step_04b_stress_strain_20nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress–strain curve for 20 nm sample under uniaxial tension at \(10^{-3}\,\text{s}^{-1}\). Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.).
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_GPa`
  - `units`:
    - `strain`: dimensionless
    - `stress_GPa`: GPa

### step_05_yield_strengths.json
- path: `/app/outputs/step_05_yield_strengths.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Yield strengths for 8 nm and 20 nm samples. Scored by checking that the values fall within hidden reference ranges and that the size ordering is physically plausible.
- schema:
  - `type`: object
  - `required`: `8nm`, `20nm`
  - `properties`:
    - `8nm`:
      - `type`: number
      - `units`: GPa
    - `20nm`:
      - `type`: number
      - `units`: GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04a_stress_strain_8nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_GPa"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_GPa": "GPa"
        }
      },
      "description": "Stress–strain curve for 8 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.)."
    },
    {
      "file": "step_04b_stress_strain_20nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_GPa"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_GPa": "GPa"
        }
      },
      "description": "Stress–strain curve for 20 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.)."
    },
    {
      "file": "step_05_yield_strengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "8nm",
          "20nm"
        ],
        "properties": {
          "8nm": {
            "type": "number",
            "units": "GPa"
          },
          "20nm": {
            "type": "number",
            "units": "GPa"
          }
        }
      },
      "description": "Yield strengths for 8 nm and 20 nm samples. Scored by checking that the values fall within hidden reference ranges and that the size ordering is physically plausible."
    }
  ]
}
```

## How you are scored
Each scored artifact – the two CSV stress–strain curves and the JSON yield strengths – is evaluated independently by a hidden verifier. For the stress–strain curves, the verifier performs a structural audit of the curve shape (non‑negative stress, elastic rise, peak, load drop, etc.) rather than a pointwise comparison against a reference. The yield strengths are checked against hidden reference ranges and additionally verified to obey a size ordering that is consistent with the underlying physics. The weighted sum of these checks yields the overall reproduction reward. Reporting a number without genuinely executing the PTA pipeline will not suffice; the verifier expects physically plausible stress–strain curves that can only be obtained by running the described simulations.