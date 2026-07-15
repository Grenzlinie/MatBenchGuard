# Compute Sound Velocities and Debye Temperature from Elastic Data

## Problem background
The Debye temperature \(\Theta_D\) is a key solid-state parameter that captures the vibrational properties of a crystal. It can be extracted from low-temperature specific heat measurements, but it can also be estimated independently from the material's single-crystal elastic constants. Such an estimate provides a cross-consistency check between thermal and elastic measurements, especially for substances like lithium fluoride where the calorimetric Debye temperature shows a pronounced temperature variation. This task focuses on computing an elastic Debye temperature for LiF from a published set of single-crystal elastic constants, using standard polycrystalline averaging.

## Approach
The approach is a direct computation using the Voigt–Reuss–Hill averaging scheme to derive polycrystalline elastic moduli from single-crystal stiffness constants.

1. Convert the provided elastic constants \(c_{11}, c_{12}, c_{44}\) (in dyne/cm²) into SI units (Pa).
2. Compute the Voigt (upper) bounds for the polycrystalline bulk modulus \(B_V\) and shear modulus \(G_V\), and the Reuss (lower) bounds \(B_R\) and \(G_R\), using the standard cubic symmetry formulas.
3. Obtain the Voigt–Reuss–Hill averages: \(B = (B_V + B_R)/2\), \(G = (G_V + G_R)/2\).
4. From the average moduli and the mass density \(\rho\), calculate the longitudinal sound velocity \(v_l = \sqrt{(B + \frac{4}{3}G)/\rho}\) and the transverse sound velocity \(v_t = \sqrt{G/\rho}\).
5. Compute the mean sound velocity \(v_m\) defined by \(\frac{3}{v_m^3} = \frac{2}{v_t^3} + \frac{1}{v_l^3}\).
6. Finally, compute the Debye temperature \(\Theta_D\) via the standard formula: \(\Theta_D = \frac{h}{k_B} \left(\frac{3 N_A \rho}{4\pi M}\right)^{1/3} v_m\), where \(h\) is Planck's constant, \(k_B\) is Boltzmann's constant, \(N_A\) is Avogadro's number, and \(M\) is the molar mass with \(n=2\) atoms per formula unit.

All quantities must be in SI units for consistency; use the known physical constants and the given input values.

## Reproduction target
Using the elastic constants \(c_{11} = 10.0 \times 10^{11}\) dyne/cm², \(c_{12} = 4.0 \times 10^{11}\) dyne/cm², \(c_{44} = 5.6 \times 10^{11}\) dyne/cm², the mass density \(\rho = 2.635\) g/cm³, the molar mass \(M = 25.939\) g/mol, and \(n = 2\) atoms per formula unit, compute the polycrystalline bulk and shear moduli by the Voigt–Reuss–Hill method. From these, compute the longitudinal sound velocity \(v_l\), the transverse sound velocity \(v_t\), and the mean sound velocity \(v_m\) (all in m/s). Then compute the Debye temperature \(\Theta_D\) (in K) via the standard formula given in the approach. Write a JSON file `debye_temperature.json` containing the four numbers: `v_l`, `v_t`, `v_m`, and `Theta_D`.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute Sound Velocities and Debye Temperature
- Role: scored (load-bearing)
- Action: Using the provided elastic constants c11=10.0e11, c12=4.0e11, c44=5.6e11 dyne/cm², mass density ρ=2.635 g/cm³, molar mass M=25.939 g/mol and number of atoms per formula unit n=2, compute the polycrystalline bulk modulus B and shear modulus G via the Voigt–Reuss–Hill average. Then compute the longitudinal (v_l), transverse (v_t) and mean sound velocities (v_m) in m/s. Finally compute the Debye temperature Θ_D = (h/k_B) * (3 N_A ρ / (4π M))^(1/3) * v_m. Write the four quantities to a JSON file.
- Output file: `/app/outputs/debye_temperature.json`
- Format: json
- Contract: {"v_l": float, "v_t": float, "v_m": float, "Theta_D": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/debye_temperature.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### debye_temperature.json
- path: `/app/outputs/debye_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Sound velocities (longitudinal, transverse, mean) and Debye temperature computed from elastic constants of LiF.
- schema:
  - `type`: object
  - `required`:
    - `v_l`: float (m/s)
    - `v_t`: float (m/s)
    - `v_m`: float (m/s)
    - `Theta_D`: float (K)

Notes: The hidden checker recomputes Θ_D from the reported sound velocities using the standard Debye formula and compares to the paper's elastic estimate, while also checking internal consistency of v_m derived from v_l and v_t.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "debye_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "v_l": "float (m/s)",
          "v_t": "float (m/s)",
          "v_m": "float (m/s)",
          "Theta_D": "float (K)"
        }
      },
      "description": "Sound velocities (longitudinal, transverse, mean) and Debye temperature computed from elastic constants of LiF."
    }
  ],
  "notes": "The hidden checker recomputes Θ_D from the reported sound velocities using the standard Debye formula and compares to the paper's elastic estimate, while also checking internal consistency of v_m derived from v_l and v_t."
}
```

## How you are scored
A hidden verifier reads your `debye_temperature.json`. It checks that the mean sound velocity \(v_m\) is consistent with \(v_l\) and \(v_t\) according to the relation \(3/v_m^3 = 2/v_t^3 + 1/v_l^3\). It then recomputes the Debye temperature from your reported sound velocities using the same standard formula and physical constants. The recomputed \(\Theta_D\) is compared to an expected value that follows from the given inputs and the Voigt–Reuss–Hill procedure. Your reward depends on the accuracy of the final Debye temperature and on internal consistency; exact agreement is not required, but the result must be within a reasonable tolerance of the correct value. The verifier does not reveal that tolerance or the target value. Submitting numbers alone without a correct reproducible calculation will not yield full credit.
