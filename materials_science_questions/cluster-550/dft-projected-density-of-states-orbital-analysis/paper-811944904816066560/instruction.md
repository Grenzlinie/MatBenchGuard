# DFT Elastic and Optical Properties of Al₃Sc Intermetallic Compound

## Problem background
Al₃Sc is a cubic L1₂ intermetallic compound that forms as a coherent strengthening precipitate in Al–Sc alloys. Its mechanical and optical properties are important for understanding coherency strengthening and electronic structure. Ab initio density-functional theory (DFT) can predict the ground-state lattice constant, elastic moduli, and frequency-dependent dielectric response. This task reproduces the equilibrium lattice parameter, the independent elastic stiffness constants, the isotropic bulk modulus and Poisson’s ratio, and the complex dielectric function ε(ω) = ε₁(ω) + iε₂(ω) of the compound, including the identification of characteristic absorption peaks from the imaginary part ε₂(ω).

## Approach
The computational approach uses the Kohn–Sham formulation of DFT together with the PBE generalized gradient approximation (GGA) for exchange and correlation. The electron–ion interaction is treated with ultrasoft pseudopotentials, and electronic wavefunctions are expanded in a plane‑wave basis. The workflow proceeds in the following order (detailed in the steps below): (1) full geometry relaxation of the Al₃Sc unit cell to find the equilibrium lattice parameter; (2) application of small homogeneous strains to the relaxed cell and DFT calculation of the resulting stress tensors to extract the independent elastic stiffness constants C₁₁, C₁₂, C₄₄, from which the bulk modulus and Poisson’s ratio are derived; (3) computation of the frequency‑dependent complex dielectric function over 0–40 eV using the electronic band structure and momentum matrix elements within the Ehrenreich–Cohen formalism; (4) location of the dominant absorption peaks in ε₂(ω) in the 0–15 eV and 20–35 eV ranges.

## Reproduction target
Produce the following outputs:
- Equilibrium lattice parameter a₀ (nm).
- Elastic stiffness constants C₁₁, C₁₂, C₄₄ (GPa), together with the bulk modulus B₀ = (C₁₁+2C₁₂)/3 (GPa) and Poisson’s ratio ν = –S₁₂/S₁₁ (dimensionless).
- The complex dielectric function ε₁(ω) and ε₂(ω) as a function of photon energy covering 0–40 eV.
- The energy (eV) of the strongest absorption peak in the 0–15 eV range and the secondary peak in the 20–35 eV range, as identified from ε₂(ω).

## Assets

- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Al and Sc (e.g., GBRV library): https://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored
- Action: Perform DFT geometry relaxation of the cubic L12 Al3Sc unit cell using plane-wave pseudopotential method with PBE-GGA and ultrasoft pseudopotentials. Choose appropriate kinetic energy cutoff and k-point mesh. Extract the equilibrium lattice parameter a0 in nm.
- Output file: `/app/outputs/lattice_parameter.txt`
- Format: txt
- Contract: One line containing the numeric value in nm, e.g., '0.4053393'
- Scoring: scored by hidden verifier

### Step 2: Elastic constants and moduli calculation
- Role: scored (load-bearing)
- Action: From the relaxed geometry, apply small homogeneous strains to the unit cell, compute the resulting stress tensors via DFT, and extract the three independent elastic stiffness constants C11, C12, C44 (in GPa) by fitting the linear stress–strain relation. Then compute the bulk modulus B0 = (C11 + 2C12)/3 and Poisson's ratio v = -S12/S11 after inverting the stiffness matrix to obtain compliance components Sij.
- Output file: `/app/outputs/elastic_constants.txt`
- Format: txt
- Contract: Five whitespace-separated numbers on one line in the order: C11 C12 C44 B0 v
- Scoring: scored by hidden verifier

### Step 3: Dielectric function calculation
- Role: scored (load-bearing)
- Action: Using the relaxed structure and the DFT electronic structure (bands and matrix elements), compute the frequency-dependent complex dielectric function ε(ω)=ε1(ω)+iε2(ω) over the energy range 0–40 eV employing the Ehrenreich-Cohen formalism. Save the data as three columns: energy (eV), ε1, ε2, without a header.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: CSV with three comma-separated columns: energy (eV), ε1, ε2. No header row. Energy in ascending order, at least covering 0–40 eV.
- Scoring: scored by hidden verifier

### Step 4: Optical peak identification
- Role: scored
- Action: From the ε2 column of dielectric_function.csv, locate the energy (eV) of the maximum absorption in the range 0–15 eV (strong peak) and in the range 20–35 eV (small peak). Report the two peak energies as a single line.
- Output file: `/app/outputs/optical_peak_energies.txt`
- Format: txt
- Contract: Single line with two whitespace-separated numbers: strong peak energy (eV) and small peak energy (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameter.txt`
- `/app/outputs/elastic_constants.txt`
- `/app/outputs/dielectric_function.csv`
- `/app/outputs/optical_peak_energies.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameter.txt
- path: `/app/outputs/lattice_parameter.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice parameter a0 of cubic Al3Sc.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: nm

### elastic_constants.txt
- path: `/app/outputs/elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Elastic stiffness constants C11, C12, C44, bulk modulus B0, and Poisson's ratio v.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B0`: GPa
    - `v`: dimensionless

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frequency-dependent complex dielectric function covering 0–40 eV; three columns: energy (eV), ε1, ε2.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `energy`, `epsilon1`, `epsilon2`
  - `units`:
    - `energy`: eV
    - `epsilon1`: dimensionless
    - `epsilon2`: dimensionless

### optical_peak_energies.txt
- path: `/app/outputs/optical_peak_energies.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energies of the strong absorptive peak (0–15 eV) and the small peak (20–35 eV) in the dielectric function.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `strong_peak`: eV
    - `small_peak`: eV

Notes: All values are computed from DFT using a plane-wave pseudopotential method with PBE-GGA. The checker verifies B0 and v consistency from Cij, and checks that the reported peak energies are derivable from the submitted dielectric function ε2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "nm"
        }
      },
      "description": "Equilibrium lattice parameter a0 of cubic Al3Sc."
    },
    {
      "file": "elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B0": "GPa",
          "v": "dimensionless"
        }
      },
      "description": "Elastic stiffness constants C11, C12, C44, bulk modulus B0, and Poisson's ratio v."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "energy",
          "epsilon1",
          "epsilon2"
        ],
        "units": {
          "energy": "eV",
          "epsilon1": "dimensionless",
          "epsilon2": "dimensionless"
        }
      },
      "description": "Frequency-dependent complex dielectric function covering 0–40 eV; three columns: energy (eV), ε1, ε2."
    },
    {
      "file": "optical_peak_energies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "strong_peak": "eV",
          "small_peak": "eV"
        }
      },
      "description": "Energies of the strong absorptive peak (0–15 eV) and the small peak (20–35 eV) in the dielectric function."
    }
  ],
  "notes": "All values are computed from DFT using a plane-wave pseudopotential method with PBE-GGA. The checker verifies B0 and v consistency from Cij, and checks that the reported peak energies are derivable from the submitted dielectric function ε2."
}
```

## How you are scored
Each of the four workflow stages writes a scored artifact under `/app/outputs`. A hidden verifier inspects every artifact and assigns a stage score. The verifier compares the lattice parameter, elastic constants, bulk modulus, Poisson’s ratio, and the identified peak energies to reference values, using tolerances that accommodate the legitimate spread among different DFT implementations, pseudopotential sets, and numerical settings. The dielectric function is checked for structural consistency (energy range, ascending order, no missing bands) and that the reported peak energies can be derived from it. Additionally, the verifier may recompute derived quantities (such as B₀ and ν from the submitted elastic constants) to confirm internal consistency. The final reward is a float in [0, 1] obtained by combining the stage scores with approximately equal weights. Reporting a single number without the required artifacts or fabricating values not supported by the computation will be penalized.
