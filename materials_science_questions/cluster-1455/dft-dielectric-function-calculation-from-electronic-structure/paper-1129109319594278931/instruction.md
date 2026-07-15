# First-principles calculation of resonant EUV self-diffraction spectrum of a metal thin film

## Problem background
Resonant self-diffraction (SD) of extreme ultraviolet (EUV) femtosecond pulses in a thin metal film is a non-collinear four-wave mixing process. Two coherent EUV pulses are crossed at the sample, and their interference creates a spatially periodic electronic excitation that acts as a transient diffraction grating for the same pulses. This work investigates the SD signal near the M_{2,3} absorption edge of cobalt, where the refractive index is expected to be highly sensitive to electronic temperature changes. The theoretical model assumes that the EUV excitation quickly thermalizes the electronic subsystem, raising the electronic temperature and thereby altering the occupancy near the Fermi level, which modulates the complex refractive index. Understanding the SD signal as a function of photon energy is important because the spectrum may contain features not present in conventional absorption measurements. The goal is to compute the normalized SD spectrum from first principles, capturing both the resonant enhancement and any fine structure above the edge.

## Approach
We compute the electronic density of states (DOS) of hcp cobalt using density functional theory (DFT). From the DOS, we determine the chemical potential for two electronic temperatures: a baseline (e.g., 300 K) and an elevated temperature (e.g., 400 K) representative of the EUV-induced heating. We then use the Bethe-Salpeter equation (BSE) to compute the complex dielectric function at these two temperatures, accounting for the modified occupation numbers via the chemical potential. The complex refractive index (real part δ and imaginary part β) is derived from the dielectric function. The differences Δδ and Δβ between the two temperatures quantify the refractive-index modulation. Assuming the modulation amplitude scales with the absorbed energy density, we form a function A(hν) = (Δδ)^2 + (Δβ)^2 that captures the photon-energy dependence of the grating strength. Using published EUV absorption lengths for cobalt and parameters of the thin-film transmission geometry (sample thickness, incident and detection angles), we evaluate the normalized SD signal expression. Finally, we compute the normalized signal for photon energies from 54 to 72 eV and normalize the spectrum so its maximum equals 1.

## Reproduction target
Compute the normalized self-diffraction signal (I_SD / I_0^3) versus photon energy for hcp cobalt over the range 54–72 eV using the electronic-temperature-modulated refractive-index model. The output must be a CSV file named sd_spectrum.csv containing two columns: photon_energy (eV) and normalized_signal (dimensionless). The signal values are normalized such that the maximum signal equals 1. The computation chain includes DFT density-of-states, temperature-dependent chemical potential, BSE refractive index at 300 K and 400 K, modulation amplitude A(hν), and final SD signal using the thin-film transmission-geometry formula with literature absorption lengths.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- OCEAN (Obtaining Core Excitations from Ab initio electronic structure and NIST BSE): https://github.com/nist-oc/OCEAN
- Co pseudopotential (Troullier-Martins, PBE): Quantum ESPRESSO pseudopotential library
- Optical constants of cobalt near M_{2,3} edge from Saadeh et al. (2023): 10.1016/j.ijleo.2022.170455

## Workflow steps

### Step 1: DFT electronic density of states calculation
- Role: process
- Action: Compute the spin-polarized electronic density of states g(E) of hcp Co using Quantum ESPRESSO: lattice constants a=4.736 Bohr, c=7.693 Bohr, norm-conserving Troullier-Martins pseudopotential (PBE), plane-wave kinetic energy cutoff 100 Ry, 12×12×6 Monkhorst-Pack k-point grid, Gaussian smearing. Save the DOS data.
- Evidence: none

### Step 2: Temperature-dependent chemical potential
- Role: process
- Action: Using the DOS from step_0, determine the chemical potential μ(Te) at Te=300 K and Te=400 K by requiring that the integral of g(E)·f(E,μ,Te) equals the total number of valence electrons (N=9).
- Evidence: none

### Step 3: BSE calculation of complex refractive index at Te=300 K
- Role: process
- Action: Run OCEAN (BSE) for hcp Co at Te=300 K using the μ(300 K) from step_1, with parameters: ground-state k-grid 10×10×1, final-state k-grid 16×16×1, screening k-grid 4×4×1, 100 bands, Slater integral scaling 0.8, Lorentzian broadening 0.3 eV. Compute the complex dielectric function ε(ω) and convert to complex refractive index (1−δ+iβ).
- Evidence: none

### Step 4: BSE calculation of complex refractive index at Te=400 K
- Role: process
- Action: Repeat the OCEAN calculation from step_2 but at Te=400 K, using μ(400 K) from step_1, to obtain the refractive index of the electronically excited state.
- Evidence: none

### Step 5: Refractive-index modulation and A(hν) function
- Role: process
- Action: Calculate the differences Δδ = δ(400 K) − δ(300 K) and Δβ = β(400 K) − β(300 K). Form A(hν) = (Δδ)^2 + (Δβ)^2, assuming the modulation amplitude scales linearly with absorbed energy density (the squared amplitude scales with ρ^2). Save A(hν) as a function of photon energy.
- Evidence: none

### Step 6: Normalized self-diffraction signal
- Role: scored (load-bearing)
- Action: Using A(hν) from step_4, the EUV absorption length L(hν) from Saadeh et al. (2023) optical constants, sample thickness d=20 nm, detection angle ψ=28.7°, half-crossing angle θ=9.2°, and wave vector k=2π/λ, compute the normalized SD signal according to the thin-film transmission-geometry expression. Compute for photon energies from 54 to 72 eV with a step ≤1 eV. Normalize the resulting signal so that its maximum is 1.
- Output file: `/app/outputs/sd_spectrum.csv`
- Format: csv
- Contract: Two columns: photon_energy (eV), normalized_signal (dimensionless). Values are normalized such that the maximum signal equals 1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sd_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sd_spectrum.csv
- path: `/app/outputs/sd_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized self-diffraction signal as a function of photon energy. The hidden checker compares the agent's curve to a digitized reference from the paper using structural checks and relative tolerances on specific energy points.
- schema:
  - `required_columns`: `photon_energy`, `normalized_signal`
  - `units`:
    - `photon_energy`: eV
    - `normalized_signal`: dimensionless (normalized to max=1)

Notes: The agent must perform the full DFT+BSE pipeline and compute the SD signal curve. Only the theoretical model reproduction is targeted; the experimental measurement is excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sd_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "photon_energy",
          "normalized_signal"
        ],
        "units": {
          "photon_energy": "eV",
          "normalized_signal": "dimensionless (normalized to max=1)"
        }
      },
      "description": "Normalized self-diffraction signal as a function of photon energy. The hidden checker compares the agent's curve to a digitized reference from the paper using structural checks and relative tolerances on specific energy points."
    }
  ],
  "notes": "The agent must perform the full DFT+BSE pipeline and compute the SD signal curve. Only the theoretical model reproduction is targeted; the experimental measurement is excluded."
}
```

## How you are scored
A hidden verifier independently evaluates the final scored artifact, sd_spectrum.csv, by comparing it to a reference spectrum using structural checks (such as the location of the peak and the signal level at low energies) and relative tolerance comparisons at a set of hidden photon energies. The verifier combines these checks into a reward that reflects the fidelity of the computed spectrum to the expected shape. The intermediate process steps (density of states, chemical potential, refractive indices, and the A(hν) function) are required to produce the final signal but are not individually scored; however, the final signal depends on them. The verifier does not require exact replication of any particular published figure, but assesses whether the computed spectrum faithfully captures the resonant enhancement and fine structure expected from the model. No specific reference values are disclosed in this instruction.
