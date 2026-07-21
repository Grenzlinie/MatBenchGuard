# Compute polarization and domain wall tunneling frequencies using instanton method

## Problem background
Quantum tunneling of polarization in hydrogen-bonded order–disorder ferroelectrics offers a mechanism for spontaneous switching of macroscopic electric polarization at low temperatures. In these materials, microscopic proton tunneling between double-well hydrogen-bond potentials can trigger a “double tunneling” effect: the collective polarization of a nanoscale ferroelectric grain tunnels between two opposite orientations, and domain walls may also tunnel between nearby positions. The rate of this quantum switching determines memory retention in ultra-small nonvolatile ferroelectric memory elements. The task is to compute the tunnel splitting frequencies (the tunneling rates) for two specific processes in the prototypical crystal $\ce{KH2PO4}$: polarization reversal in a single-domain grain and domain wall motion. All required material parameters and formulas are known; you will re-implement the instanton-based calculation and numerically evaluate the frequencies under given grain dimensions and temperature conditions.

## Approach
The instanton (semi-classical) method is used to calculate the tunnel splitting $\Delta$ for a particle in a double-well free energy density. The free energy of a uniaxial ferroelectric grain is modeled by a standard quartic Landau expansion $F = -A P^2/2 + B P^4/4$, where $P$ is the polarization, and $A$, $B$ are positive Landau coefficients. The classical action $S$ for the optimal tunneling path (instanton) is obtained from the barrier height $V_0$ and the characteristic oscillation frequency $\omega$ (attempt frequency). The tunnel splitting is then $\Delta = 4\sqrt{3}\,\omega \, (S/(2\pi\hbar))^{1/2}\exp(-S/\hbar)$, with $S = 16 V_0 / (3\omega)$. For polarization reversal in a grain of volume $V$, the barrier is $V_0 = A^2 V / (4B)$. The attempt frequency $\omega$ is not taken from the long-wavelength pseudo-spin mode but from the four-particle cluster model appropriate for $\ce{KH2PO4}$: $\omega = (\Gamma/\hbar) \sqrt{1 - 4\langle S^x\rangle w/\Gamma + 4\langle S^x\rangle \varepsilon/\Gamma}$, where $\langle S^x\rangle = (1/2)\tanh(\Gamma/(2 k_B T))$, and $\Gamma$, $w$, $\varepsilon$ are the proton tunneling integral and cluster energies. For domain wall tunneling, the free energy is augmented with a gradient term $\frac{1}{2}K(\nabla P)^2$, where $K = \delta^2/4$ and $\delta$ is the proton double-well distance. The effective barrier becomes $V_0 = 2^{3/2} A^{3/2} K^{1/2} V / (3 B d)$, with $d$ the domain wall width. The same $\omega$ is used. The computation involves substituting the given numeric parameters (all stated below) and performing unit conversions (from cgs to SI where necessary) to obtain frequencies in hertz. The two required steps are: (1) polarization tunneling for a 1 nm grain, and (2) domain wall tunneling for a grain of volume $(2.1\times 10^{-9}\,\text{m})^3$, both at cryogenic temperature $T \approx 0.1\,\text{K}$.

## Reproduction target
Implement the instanton formulas using the parameters provided below. Compute the tunnel splitting frequency in hertz for:
- Polarization reversal: grain volume $V = (1\,\text{nm})^3$, barrier $V_0 = A^2 V/(4B)$, attempt frequency $\omega$ from the cluster model.
- Domain wall motion: grain volume $V = (2.1\times 10^{-9}\,\text{m})^3$, barrier $V_0$ from the gradient term using proton double-well distance $\delta = 0.34\times 10^{-8}\,\text{cm}$ and domain wall width $d = 8\times 10^{-8}\,\text{cm}$.
Use the same $\omega$ for both cases. Handle unit conversions consistently. Output each computed frequency as a single positive number (floating point) in Hz to the files `polarization_tunneling_freq.txt` and `domain_wall_tunneling_freq.txt` under `/app/outputs`.

## Assets
No external datasets, models, or tools are required. All needed physical constants ($\hbar$, $k_B$) and material parameters ($A$, $B$, $\Gamma$, $w$, $\varepsilon$, $T_c$, $\delta$, $d$) are provided in the parameter list below. You only need a standard Python or scientific computing environment to evaluate the formulas.

## Workflow steps

### Step 1: Compute polarization tunneling frequency
- Role: scored
- Action: Compute the tunnel splitting frequency for polarization reversal in a single-domain grain of KH2PO4 using the instanton method with the four-particle cluster approximation for the attempt frequency. Use the given material parameters (Landau coefficients A, B, proton tunneling integral, cluster energies, grain volume, temperature) and convert units consistently to obtain the final frequency in Hz. Output the result as a single positive number in the file.
- Output file: `/app/outputs/polarization_tunneling_freq.txt`
- Format: txt
- Contract: A single positive float number representing the tunnel splitting Δ in Hz.
- Scoring: scored by hidden verifier

### Step 2: Compute domain wall tunneling frequency
- Role: scored
- Action: Compute the tunnel splitting frequency for domain wall motion in a KH2PO4 grain using the same instanton formula as in step 1, but with the effective barrier derived from the gradient term of the free energy. Use the same attempt frequency ω as in step 1, and the given domain wall parameters (width, proton double-well distance, grain volume). Convert units consistently and output the frequency in Hz as a single positive number.
- Output file: `/app/outputs/domain_wall_tunneling_freq.txt`
- Format: txt
- Contract: A single positive float number representing the domain wall tunnel splitting Δ in Hz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarization_tunneling_freq.txt`
- `/app/outputs/domain_wall_tunneling_freq.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarization_tunneling_freq.txt
- path: `/app/outputs/polarization_tunneling_freq.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Scored result for polarization tunneling frequency. The checker will compare the numeric value to the paper-reported reference within a hidden tolerance.
- schema:
  - `type`: text
  - `value_type`: float
  - `unit`: Hz
  - `description`: The file contains one line with a single positive float number representing the tunnel splitting frequency in Hz.

### domain_wall_tunneling_freq.txt
- path: `/app/outputs/domain_wall_tunneling_freq.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Scored result for domain wall tunneling frequency. The checker will compare the numeric value to the paper-reported reference within a hidden tolerance.
- schema:
  - `type`: text
  - `value_type`: float
  - `unit`: Hz
  - `description`: The file contains one line with a single positive float number representing the domain wall tunneling frequency in Hz.

Notes: The two output files contain the two headline frequencies reported in the paper. The agent must implement the cluster approximation for the attempt frequency and perform unit conversions from cgs to SI. No external data files are needed; all required parameters are provided in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarization_tunneling_freq.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value_type": "float",
        "unit": "Hz",
        "description": "The file contains one line with a single positive float number representing the tunnel splitting frequency in Hz."
      },
      "description": "Scored result for polarization tunneling frequency. The checker will compare the numeric value to the paper-reported reference within a hidden tolerance."
    },
    {
      "file": "domain_wall_tunneling_freq.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value_type": "float",
        "unit": "Hz",
        "description": "The file contains one line with a single positive float number representing the domain wall tunneling frequency in Hz."
      },
      "description": "Scored result for domain wall tunneling frequency. The checker will compare the numeric value to the paper-reported reference within a hidden tolerance."
    }
  ],
  "notes": "The two output files contain the two headline frequencies reported in the paper. The agent must implement the cluster approximation for the attempt frequency and perform unit conversions from cgs to SI. No external data files are needed; all required parameters are provided in the instruction."
}
```

## How you are scored
A hidden verifier will independently read each output file and compare the reported frequency to a reference value. Your submission will earn a combined score based on how close each result is to the expected value (a tolerance will be applied). The verifier does not have access to your intermediate work; only the final numbers in the two text files matter. Note that simply copying a known number from a publication is not the goal; the task is to implement the calculation faithfully and produce the correct result through the described procedure.
