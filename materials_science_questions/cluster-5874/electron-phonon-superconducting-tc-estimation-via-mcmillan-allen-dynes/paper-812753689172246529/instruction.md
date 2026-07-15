# Electron spectral function and quasiparticle analysis in electron-doped monolayer MoS2

## Problem background
Electron-phonon interactions in two-dimensional materials can strongly renormalize electronic states, potentially producing multiple quasi-particle branches with distinct lifetimes. Monolayer MoS2 under electron doping is a prime system for studying such many-body effects because intervalley scattering by optical and acoustic phonons is strong and the Fermi level can be tuned to populate specific conduction-band valleys. Understanding the resulting electronic spectral function—whether it deviates from a single quasi-particle picture, how many quasi-particle poles appear, and what their energies and lifetimes are—is key for interpreting spectroscopic measurements and for predicting transport and superconducting properties. This task investigates the electron-phonon renormalization of the outer spin-up band near the K point of the Brillouin zone in electron-doped monolayer MoS2 at a carrier density of n2D = 9 × 10^13 cm^-2.

## Approach
We use first-principles density functional theory (DFT) and density functional perturbation theory (DFPT) to obtain the ground-state electronic structure, phonon dispersions, and electron-phonon matrix elements of the doped monolayer. Starting from a self-consistent DFT calculation with a jellium background to simulate doping, we compute phonon properties and the electron-phonon coupling on a coarse mesh. Wannier interpolation is then employed to transfer these quantities to extremely dense momentum grids, enabling precise evaluation of the Fan-Migdal electron self-energy. From the self-energy we construct the spectral function A(k,ω) for the outer spin-split conduction band. To identify genuine quasi-particle excitations, we analytically continue the self-energy to the lower complex half-plane and solve the Dyson equation for the poles of the electron Green's function, which directly yield the quasi-particle energies, lifetimes, and spectral weights. The analysis focuses on the outer spin-up band near the K point, where the strongest electron-phonon effects are expected.

## Reproduction target
For electron-doped monolayer MoS2 (carrier density n2D = 9 × 10^13 cm^-2), produce the following three quantities for the outer spin-up band:

1. The imaginary part of the electron-phonon self-energy ImΣ(ω) at momentum k_A (a point close to K) as a function of binding energy.
2. The electron spectral function A(k,ω) along a k-path near the K point, covering binding energies from -100 meV to 0 meV.
3. The complex quasi-particle poles obtained by solving the Dyson equation for the same band and k-path: for each momentum, report the pole energies, lifetimes, and residues.

The goal is to characterize the renormalized electronic spectrum, determine the number of quasi-particle branches, and extract their dispersion and lifetimes.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: http://www.wannier.org/
- Norm-conserving fully relativistic pseudopotentials for Mo and S (SSSP library): https://www.materialscloud.org/discover/sssp
- Python with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: DFT ground-state calculation
- Role: process
- Action: Perform self-consistent noncollinear DFT calculation for monolayer MoS2 with electron doping n2D=9e13 cm^-2 using Quantum ESPRESSO, LDA functional, and jellium background. Obtain charge density and electronic eigenvalues on a 36x36 k-mesh.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: DFPT phonon calculation
- Role: process
- Action: Using the ground-state charge density, run DFPT on a coarse 9x9 q-grid to compute phonon frequencies, eigenvectors, and electron-phonon matrix elements on the coarse (k,q) grids.
- Evidence: `/app/outputs/dfpt_output.log`

### Step 3: Wannier interpolation to dense grids
- Role: process
- Action: Use Wannier90 to interpolate electronic and vibrational quantities to dense grids (up to 1e7 k-points, 1e6 q-points) and generate dense electron-phonon matrix elements.
- Evidence: `/app/outputs/wannier_interpolation.log`

### Step 4: Electron self-energy on real axis
- Role: scored (load-bearing)
- Action: From the dense electron-phonon matrix elements, compute the Fan-Migdal electron self-energy for the outer spin-up band at momentum k_A (near K). Output the imaginary part ImΣ as a function of energy.
- Output file: `/app/outputs/self_energy_imag.dat`
- Format: tsv
- Contract: Two tab-separated columns: energy (eV), ImSigma (eV). No header.
- Scoring: scored by hidden verifier

### Step 5: Spectral function calculation
- Role: scored
- Action: Using the self-energy from the previous step, compute the electron spectral function A(k,ω) for the same outer spin-up band along a k-path near the K point covering binding energies from -100 meV to 0 meV. Output a table with k_index, k_path_coordinate, energy, and spectral weight.
- Output file: `/app/outputs/spectral_function.dat`
- Format: tsv
- Contract: Four tab-separated columns: k_index (int), k_path_coordinate (float, Å−1), energy (eV), spectral_weight (a.u.). No header.
- Scoring: scored by hidden verifier

### Step 6: Complex-plane quasiparticle pole analysis
- Role: scored (load-bearing)
- Action: Perform analytic continuation of the self-energy to the lower half-plane and solve the Dyson equation for complex quasiparticle poles for the same outer spin-up band along the same k-path. Output a JSON file with the poles for each k-point.
- Output file: `/app/outputs/quasiparticle_poles.json`
- Format: json
- Contract: Array of objects: { 'k_index' (int), 'k_path_coordinate' (float), 'poles': [ { 'n' (int 1-3), 'E_qp' (float, eV), 'Gamma_qp' (float, eV positive), 'residue_real' (float), 'residue_imag' (float) } ] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/self_energy_imag.dat`
- `/app/outputs/spectral_function.dat`
- `/app/outputs/quasiparticle_poles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### self_energy_imag.dat
- path: `/app/outputs/self_energy_imag.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of electron-phonon self-energy for the outer spin-up band at momentum k_A; used to check the double-plateau shape with onsets near the two phonon energies and a dip near 42 meV.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `ImSigma`
  - `units`:
    - `energy`: eV
    - `ImSigma`: eV

### spectral_function.dat
- path: `/app/outputs/spectral_function.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Spectral function A(k,ω) for the outer spin-up band along a path near K; used to verify two band-splittings at the acoustic and optical phonon energies (~16 meV and ~46 meV).
- schema:
  - `type`: table
  - `required_columns`: `k_index`, `k_path_coordinate`, `energy`, `spectral_weight`
  - `units`:
    - `k_path_coordinate`: Å^{-1}
    - `energy`: eV
    - `spectral_weight`: a.u.

### quasiparticle_poles.json
- path: `/app/outputs/quasiparticle_poles.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Complex quasiparticle poles for the outer spin-up band; used to verify exactly three poles per momentum, correct energy ordering, and a long-lived n=2 pole (Gamma < 1 meV) near k_F.
- schema:
  - `type`: array
  - `items`:
    - `k_index`: int
    - `k_path_coordinate`: float
    - `poles`:
      - `type`: array
      - `items`:
        - `n`: int (1-3)
        - `E_qp`: float (eV)
        - `Gamma_qp`: float (eV positive)
        - `residue_real`: float
        - `residue_imag`: float

Notes: The scoring is structural: the checker will verify the characteristic shapes, number of poles, and energy/lifetime windows, not exact numeric values. The McMillan-Allen-Dynes Tc estimation and electron-electron scattering are excluded per task scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "self_energy_imag.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "ImSigma"
        ],
        "units": {
          "energy": "eV",
          "ImSigma": "eV"
        }
      },
      "description": "Imaginary part of electron-phonon self-energy for the outer spin-up band at momentum k_A; used to check the double-plateau shape with onsets near the two phonon energies and a dip near 42 meV."
    },
    {
      "file": "spectral_function.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_index",
          "k_path_coordinate",
          "energy",
          "spectral_weight"
        ],
        "units": {
          "k_path_coordinate": "Å^{-1}",
          "energy": "eV",
          "spectral_weight": "a.u."
        }
      },
      "description": "Spectral function A(k,ω) for the outer spin-up band along a path near K; used to verify two band-splittings at the acoustic and optical phonon energies (~16 meV and ~46 meV)."
    },
    {
      "file": "quasiparticle_poles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "k_index": "int",
          "k_path_coordinate": "float",
          "poles": {
            "type": "array",
            "items": {
              "n": "int (1-3)",
              "E_qp": "float (eV)",
              "Gamma_qp": "float (eV positive)",
              "residue_real": "float",
              "residue_imag": "float"
            }
          }
        }
      },
      "description": "Complex quasiparticle poles for the outer spin-up band; used to verify exactly three poles per momentum, correct energy ordering, and a long-lived n=2 pole (Gamma < 1 meV) near k_F."
    }
  ],
  "notes": "The scoring is structural: the checker will verify the characteristic shapes, number of poles, and energy/lifetime windows, not exact numeric values. The McMillan-Allen-Dynes Tc estimation and electron-electron scattering are excluded per task scope."
}
```

## How you are scored
A hidden verifier will independently assess your three output files. For `self_energy_imag.dat`, it checks that the imaginary part of the self-energy exhibits a characteristic double-plateau shape with a pronounced dip where ImΣ nearly vanishes; this indicates a restricted phonon-scattering phase space. For `spectral_function.dat`, it verifies that the spectral function shows two distinct band-splitting signatures at energies corresponding to the dominant phonon modes. For `quasiparticle_poles.json`, it confirms that the correct number of complex poles per momentum is found, that the pole energies are physically ordered, and that one of the poles exhibits a very small lifetime broadening (nearly ballistic) near the Fermi momentum. Scoring is structural: your artifacts are evaluated on the presence and approximate positions of these features, not on exact numeric matches. Each stage carries a weight, and the combined score must meet a minimum threshold for full credit.
