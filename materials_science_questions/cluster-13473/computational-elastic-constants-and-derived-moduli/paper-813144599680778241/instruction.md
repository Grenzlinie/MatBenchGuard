# Mesoscale Elastic Stiffness Tensor from Gay‑Berne Simulations of Clay Nanoplatelets

## Problem background
Clay minerals form aggregates whose mechanical properties control the behaviour of soils, shales, and industrial suspensions. Understanding how nanoscale platelet interactions translate into mesoscale stiffness requires bridging length scales. This work uses an upscaling strategy: atomistic potential-of-mean-force calculations are distilled into Gay‑Berne (GB) potential parameters for oblate ellipsoidal particles, and mesoscale molecular dynamics simulations of 1000 platelets are performed to generate jammed configurations. From these, a quasi‑static stress‑strain protocol extracts the full 6×6 elastic stiffness tensor (Voigt notation). The aim of the reproduction is to obtain the mean stiffness tensor for three representative simulation cases and evaluate how well it approximates cubic symmetry, as well as whether the stiffness components increase with confining pressure — all of which characterise the mechanical response of clay platelet assemblies.

## Approach
The core concept is to treat each clay platelet as an oblate ellipsoid interacting via a Gay‑Berne potential that has been calibrated against atomistic free‑energy profiles. The GB parameters (shape radii, interaction radius σ, and energy well depths εₐ, ε_b, ε_c) for different platelet diameters are provided in the assets below.

Simulations are run in LAMMPS using the GB pair style. First, NPT simulations at T = 300 K compress an initial random simple‑cubic lattice of 1000 particles until the system reaches a jammed state (potential energy and density have stabilised). At least 10 independent samples per case are required. Second, for each jammed configuration, a quasi‑static stress‑strain protocol is applied: six independent small homogeneous strain modes are imposed, and the system is relaxed under NVT (T ≈ 0.01 K) to extract the linear‑elastic response. The internal stress tensor is computed from particle velocities and forces using the standard atomic‑level virial formula, and a central‑difference fit over symmetric positive and negative strains yields the 6×6 stiffness matrix in Voigt notation. The mean matrix over the 10 samples per case is the final output. The checker will then compute cubic‑averaged elastic constants and a normalised Euclidean distance metric from the submitted mean tensors, comparing them to hidden reference values and verifying a pressure trend.

## Reproduction target
Produce the mean full 6×6 elastic stiffness tensor (Voigt notation, in GPa) for three simulation cases:
- D = 500 Å platelets at confining pressure P = 1 atm
- D = 1000 Å platelets at confining pressure P = 1 atm
- D = 1000 Å platelets at confining pressure P = 10 atm

The hidden verifier will independently compute from the submitted tensors:
- cubic‑averaged elastic constants C̄₁₁ = (C₁₁+C₂₂+C₃₃)/3, C̄₁₂ = (C₁₂+C₁₃+C₂₃)/3, C̄₄₄ = (C₄₄+C₅₅+C₆₆)/3;
- the Euclidean distance between the full tensor and its cubic approximation divided by the norm of the cubic approximation.
These derived quantities will be compared to hidden reference values. Additionally, the verifier will check that for D = 1000 Å, each of C̄₁₁, C̄₁₂, C̄₄₄ is larger at P = 10 atm than at P = 1 atm. Submit the three mean matrices as a single JSON file `/app/outputs/elastic_tensors.json` with the format described under the output contract.

## Assets

- **LAMMPS** (Large‑scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/
- **Gay‑Berne potential parameters** (first face‑to‑face minimum, adapted from a published mesoscale study of clay platelets).

### For D = 500 Å
- Diameter (2a, 2b): 504.12 Å
- Thickness (2c): 9.62 Å
- Interaction radius σ: 11.00 Å
- Energy parameters ε_a, ε_b: 12.88
- Energy parameter ε_c: 551.81

### For D = 1000 Å
- Diameter (2a, 2b): 1004.12 Å
- Thickness (2c): 9.62 Å
- Interaction radius σ: 11.00 Å
- Energy parameters ε_a, ε_b: 12.94
- Energy parameter ε_c: 1108.46

**Units in LAMMPS:** Use the “real” unit style (distances in Å, energies in kcal/mol, time in fs). Convert the above GB parameters to LAMMPS‑compatible values as follows:

- **Particle shape:** Use `set type 1 shape D/2 D/2 h/2` where D is the diameter and h the thickness. For example, D = 500 Å → shape = 252.06 252.06 4.81.
- **Pair coefficients:** The LAMMPS Gay‑Berne pair style requires five parameters per pair type:
  ```
  pair_coeff type1 type2 ε σ ε_a' ε_b' ε_c' [cutoff]
  ```
  where:
  - `ε` is the overall energy scale (kcal/mol),
  - `σ` is the length scale (Å),
  - `ε_a'`, `ε_b'`, `ε_c'` are **dimensionless** relative well depths that encode the anisotropy.

  To map the paper’s absolute well depths to these dimensionless parameters, use the largest energy parameter (ε_c) as the overall energy scale and divide the others by it:
  - `ε = ε_c`
  - `σ = 11.00`
  - `ε_a' = ε_a / ε_c`
  - `ε_b' = ε_b / ε_c`
  - `ε_c' = 1.0`

  This ensures that the face‑to‑face well depth corresponds to ε_c while the edge‑to‑edge depths are correctly scaled.
  For D = 500 Å: ε = 551.81, ε_a' = 0.02333, ε_b' = 0.02333, ε_c' = 1.0
  For D = 1000 Å: ε = 1108.46, ε_a' = 0.01167, ε_b' = 0.01167, ε_c' = 1.0

- **Cutoff:** A global cutoff large enough to capture the interaction (e.g. 4.0 σ, i.e. 44.0 Å) can be set in the `pair_style` command. It is also allowed to specify a per‑pair cutoff as the last argument of `pair_coeff`.

Example LAMMPS commands for the 500 Å case:
```
units real
atom_style ellipsoid
set type 1 shape 252.06 252.06 4.81
pair_style gayberne 44.0
pair_coeff * * 551.81 11.00 0.02333 0.02333 1.0
```

**Mass/Density for ellipsoid particles:** The ellipsoid atom style requires a mass or density for each particle type to integrate the equations of motion. Set the density of particle type 1 as follows (in “real” units, density is g/cm³):
```
set type 1 density 2.65
```
A value of 2.65 g/cm³ is typical for Na‑montmorillonite, ensuring physically meaningful dynamics during NPT equilibration.

## Detailed simulation protocol

### Step 1: Generate jammed configurations via NPT simulations
- **Role:** process
- **Action:** For each of the three required cases (D=500 Å, P=1 atm; D=1000 Å, P=1 atm; D=1000 Å, P=10 atm) run a separate set of NPT simulations in LAMMPS using the Gay‑Berne parameters given above.
  - **Initial configuration:** 1000 oblate ellipsoids arranged on a simple cubic lattice (spacing large enough to avoid overlaps). Assign random orientations (quaternion randomisation).
  - **Thermostat/barostat:** NPT ensemble with a Nosé‑Hoover thermostat (T₀ = 300 K) and a Parrinello‑Rahman barostat at the target pressure P₀ (1 atm or 10 atm). Use a time step of 1 fs. Include the mass/density setting described in Assets.
  - **Jamming criterion:** Continue the simulation until the potential energy and density have converged. A practical criterion is to run until the standard deviation of the instantaneous potential energy over the last 100 000 time steps is less than 10⁻⁵ of the mean energy and the standard deviation of the instantaneous density is less than 0.1 % of the mean density. If this condition is not met after 2 000 000 steps, stop and use the last configuration; at this point the system is considered jammed.
  - **Independent samples:** Run at least 10 independent simulations per case, each with a different random seed (e.g. seeds 1, 2, …, 10, used for both the initial velocity assignment and the thermostat/barostat random number stream).
  - **Evidence:** After each sample has jammed, write a one‑line summary to `/app/outputs/jammed_configs.log` containing the sample id, the final potential energy and the final density. The exact format is free; the file only needs to exist as proof of execution.
- **Evidence file:** `/app/outputs/jammed_configs.log`

### Step 2: Compute elastic stiffness tensor
- **Role:** scored (load‑bearing)
- **Action:** For each jammed configuration sample (obtained from Step 1) perform a quasi‑static stress‑strain protocol.
  - **Strain protocol:** Apply six independent homogeneous strains (Voigt indices 1‑to‑6). For each strain mode, impose two symmetric small strains: +ε₀ and –ε₀ with **ε₀ = 0.001** (this corresponds to the linear‑elastic regime). The strain is applied by rescaling the simulation box and remapping the atom coordinates accordingly under periodic boundary conditions. After each strain application, allow the system to relax in the **NVT** ensemble at **T ≈ 0.01 K** (use a Nosé‑Hoover thermostat with a very low temperature to suppress thermal fluctuations). Run for 10 000 time steps after relaxation; collect the stress tensor over this window.
  - **Stress calculation:** Use the standard atomic‑level stress (virial) formula. In LAMMPS this can be obtained with the commands:
    ```
    compute stress all stress/atom NULL virial
    compute peratom all stress/atom
    fix ave all ave/time 1 1000 10000 c_stress[...] ...
    ```
    The six independent components (xx, yy, zz, yz, xz, xy) are converted to Voigt order (σ₁,…,σ₆). The average stress over the production window yields a stress vector for each strain, **σ**(ε).
    **Unit conversion:** LAMMPS “real” units report stress in atmospheres. Multiply each component by 1.01325 × 10⁻⁴ (1 atm = 1.01325 × 10⁻⁴ GPa) to obtain values in GPa before building the stiffness matrix.
  - **Elastic constants:** For each mode `i` (1‑to‑6), compute the stiffness coefficient from the central‑difference formula:
    ```
    C_{i\,j} = [σ_i(+ε₀) - σ_i(-ε₀)] / (2ε₀)
    ```
    where `j` is the index of the applied strain mode (the same as `i` for the diagonal components; for off‑diagonal components the mixed derivative is used). This builds the 6×6 stiffness matrix in Voigt notation (C₁₁→C₁₁, C₂₂→C₂₂, …, C₂₃→C₂₃ as C₂₃, C₁₃ as C₁₃, C₁₂ as C₁₂, with the usual mapping 11→1, 22→2, 33→3, 23→4, 13→5, 12→6). All entries must be in GPa.
  - **Averaging:** For each case (D, P) average the 10 stiffness matrices element‑wise to obtain the **mean** matrix. If desired, also compute the element‑wise standard deviation (optional field “std”).
  - **Output:** Write the three mean matrices to `/app/outputs/elastic_tensors.json`.
- **Output file:** `/app/outputs/elastic_tensors.json`
- **Format:** json
- **Contract:** A JSON object with keys `"D500_P1"`, `"D1000_P1"`, `"D1000_P10"`. Each key maps to an object containing a required field `"mean"`: a list of 6 lists (each of length 6) of floats representing the matrix **C** in Voigt order (C₁₁, C₂₂, C₃₃, C₂₃, C₁₃, C₁₂ for the upper‑triangular part; symmetry is assumed, i.e., C_{ji} = C_{ij}). An optional field `"std"` of the same shape may be included.
- **Scoring:** scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/jammed_configs.log` (evidence)
- `/app/outputs/elastic_tensors.json` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_tensors.json
- **path:** `/app/outputs/elastic_tensors.json`
- **format:** json
- **purpose:** scored
- **target_policy:** metric_recompute
- **description:** Mean full 6×6 elastic stiffness tensor (Voigt notation) in GPa for each of the three simulation conditions. The checker recomputes cubic‑averaged constants and Euclidean distance from the submitted raw matrices and compares them against the paper’s reference values.
- **schema:**
  - `type`: object
  - `required`:
    - `D500_P1`: object
    - `D1000_P1`: object
    - `D1000_P10`: object
  - `properties`:
    - `D500_P1`:
      - `type`: object
      - `required`: `mean`
      - `properties`:
        - `mean`:
          - `type`: array
          - `items`:
            - `type`: array
            - `minItems`: 6
            - `maxItems`: 6
            - `items`:
              - `type`: number
              - `unit`: GPa
          - `minItems`: 6
          - `maxItems`: 6

### jammed_configs.log
- **path:** `/app/outputs/jammed_configs.log`
- **format:** log
- **purpose:** evidence
- **description:** A log file recording the final state of each jamming simulation (sample id, potential energy, density). The content is free‑form; the file only needs to exist to prove that the NPT jamming step was executed.

**Notes:** The elastic tensors are the core scored artifact. The checker does not rely on any other agent‑written file. All derived quantities (C̄₁₁, C̄₁₂, C̄₄₄, Euclidean distance) are recomputed deterministically from the submitted tensors.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks **SHAPE ONLY** (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_tensors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "D500_P1": "object",
          "D1000_P1": "object",
          "D1000_P10": "object"
        },
        "properties": {
          "D500_P1": {
            "type": "object",
            "required": ["mean"],
            "properties": {
              "mean": {
                "type": "array",
                "items": {
                  "type": "array",
                  "minItems": 6,
                  "maxItems": 6,
                  "items": {
                    "type": "number",
                    "unit": "GPa"
                  }
                },
                "minItems": 6,
                "maxItems": 6
              }
            }
          }
        }
      },
      "description": "Mean full 6×6 elastic stiffness tensor (Voigt notation) in GPa for each of the three simulation conditions. The checker recomputes cubic‑averaged constants and Euclidean distance from the submitted raw matrices and compares them against the paper’s reference values."
    },
    {
      "file": "jammed_configs.log",
      "format": "log",
      "purpose": "evidence",
      "description": "Log of jammed configurations from NPT runs (sample id, energy, density)."
    }
  ],
  "notes": "The elastic tensors are the core scored artifact. The checker does not rely on any other agent‑written file. All derived quantities (C11_avg, C12_avg, C44_avg, Euclidean distance) are recomputed deterministically from the submitted tensors."
}
```

## How you are scored
Your reward is determined by a hidden verifier that reads `/app/outputs/elastic_tensors.json`. For each of the three simulation cases, it extracts the 6×6 mean stiffness matrix, recomputes the cubic‑averaged elastic constants (C̄₁₁, C̄₁₂, C̄₄₄) and the normalised Euclidean distance metric, and compares them against hidden reference values using predetermined tolerances. The verifier also checks the monotonic pressure trend for D=1000 Å (all three constants must increase with pressure). The total reward, a float between 0.0 and 1.0, is proportional to the fraction of cases and checks that pass all requirements. Simply reporting the paper’s numbers is not sufficient; the verifier recomputes the quantities from your submitted tensor to ensure genuine reproduction. No other artifacts are scored.