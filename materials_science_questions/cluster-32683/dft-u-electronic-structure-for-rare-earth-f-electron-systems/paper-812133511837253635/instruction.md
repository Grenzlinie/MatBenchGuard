# Reproduce LDA+DMFT spectral properties of SrVO3 and CaVO3 perovskite metals

## Problem background
Transition metal oxides are prototypical strongly correlated electron systems. The perovskite vanadates $\mathrm{SrVO_3}$ (cubic) and $\mathrm{CaVO_3}$ (orthorhombically distorted) have a $3d^1$ electronic configuration, making them clean realizations of correlated metallic behavior. A long-standing question is whether the orthorhombic distortion in $\mathrm{CaVO_3}$ drives the system close to a Mott metal–insulator transition and significantly enhances correlation effects compared to $\mathrm{SrVO_3}$. The key physical quantities that quantify correlation strength are the $t_{\mathrm{2g}}$ bandwidth, the positions of the lower and upper Hubbard bands in the single-particle spectral function, the coherent quasiparticle weight at the Fermi level, and the resulting effective mass enhancement $m^*/m_0$. Reproducing these quantities from first-principles LDA+DMFT calculations provides a direct test of the theoretical description.

## Approach
We employ a combined local-density approximation plus dynamical mean-field theory (LDA+DMFT) approach specifically targeting the V-$3d$ $t_{\mathrm{2g}}$ orbitals. First, density-functional theory calculations in the LDA are performed for the cubic $\mathrm{SrVO_3}$ and orthorhombic $\mathrm{CaVO_3}$ structures to obtain the non-interacting $t_{\mathrm{2g}}$ projected density of states (DOS). This DOS serves as input to a three-orbital DMFT self-consistency loop that uses a rotationally invariant on-site Coulomb interaction with intra-orbital $U$, inter-orbital $U'$, and Hund's exchange $J$; the numerical values of these interaction parameters are fixed as part of the task specification. The impurity problem is solved at a temperature of approximately $300\,\mathrm{K}$ with a continuous-time quantum Monte Carlo (CT-QMC) solver that computes the local Green function and self-energy on the Matsubara axis. Those imaginary-frequency quantities are analytically continued to the real-frequency axis via the maximum entropy method, yielding the many-body spectral function $A(\omega)$. From $A(\omega)$ we locate the lower and upper Hubbard band peaks and extract the quasiparticle peak weight. The slope of the real part of the self-energy at zero frequency gives the quasiparticle weight $Z$, from which the effective mass ratio $m^*/m_0 = 1/Z$ follows. The whole procedure is carried out independently for $\mathrm{SrVO_3}$ and $\mathrm{CaVO_3}$, and the structural trend $-$ whether $\mathrm{CaVO_3}$ exhibits stronger correlations $-$ is explicitly verified.

## Reproduction target
1. Compute the $t_{\mathrm{2g}}$ projected LDA DOS for $\mathrm{SrVO_3}$ (space group $Pm\bar{3}m$) and for $\mathrm{CaVO_3}$ (space group $Pbnm$) from published crystal structures.
2. Using those DOS as inputs, perform a three-orbital LDA+DMFT calculation for each compound with $U=5.55\,\mathrm{eV}$, $U'=3.55\,\mathrm{eV}$, $J=1.0\,\mathrm{eV}$ at $T\approx 300\,\mathrm{K}$ and a CT-QMC impurity solver. Apply maximum-entropy analytic continuation to obtain the real-frequency spectral functions.
3. From the spectral functions extract, for each compound, the following quantities:
   - LDA $t_{\mathrm{2g}}$ bandwidth (eV), defined as the energy interval where the DOS is non-zero,
   - lower Hubbard band peak position (eV),
   - upper Hubbard band peak position (eV),
   - quasiparticle peak weight,
   - effective mass ratio $m^*/m_0$.


## Assets

- SrVO3 crystal structure (cubic Pm-3m): 10.1006/jssc.1990.1125
- CaVO3 crystal structure (orthorhombic Pbnm): 10.1016/0022-4596(71)90033-3
- Quantum ESPRESSO: https://www.quantum-espresso.org
- TRIQS: https://triqs.github.io
- CTQMC impurity solver (triqs_cthyb): triqs_cthyb
- Maximum entropy analytic continuation (MaxEnt): https://github.com/ALPsim/maxent

## Workflow steps

### Step 1: LDA calculation for SrVO3
- Role: process
- Action: Perform DFT (LDA) calculation for cubic SrVO3 (space group Pm-3m) using a plane-wave pseudopotential method (Quantum ESPRESSO) to obtain the V-3d t2g projected density of states (DOS). Save the t2g DOS as a two-column CSV file (energy in eV, DOS).
- Evidence: `/app/outputs/srvo3_t2g_dos.csv`

### Step 2: LDA calculation for CaVO3
- Role: process
- Action: Perform DFT (LDA) calculation for orthorhombic CaVO3 (space group Pbnm) using a plane-wave pseudopotential method (Quantum ESPRESSO) to obtain the V-3d t2g projected density of states (DOS). Save the t2g DOS as a two-column CSV file (energy in eV, DOS).
- Evidence: `/app/outputs/cavo3_t2g_dos.csv`

### Step 3: Compute SrVO3 LDA+DMFT results
- Role: scored (load-bearing)
- Action: Using the t2g DOS from step s1 and the interaction parameters U=5.55 eV, U′=3.55 eV, J=1.0 eV, set up a three-orbital LDA+DMFT calculation. Solve the impurity problem with a continuous-time QMC solver at T≈300 K. Analytically continue the self-energy using the maximum entropy method to obtain the real-frequency spectral function. Extract: LDA t2g bandwidth (eV, defined as the energy interval where DOS>0), lower Hubbard band peak position (eV), upper Hubbard band peak position (eV), quasiparticle peak weight, and effective mass ratio m*/m0 = 1/Z. Write these values to 'srvo3_results.json'.
- Output file: `/app/outputs/srvo3_results.json`
- Format: json
- Contract: {"lda_bandwidth": "float (eV)", "lower_hubbard_band_peak": "float (eV)", "upper_hubbard_band_peak": "float (eV)", "quasiparticle_peak_weight": "float", "effective_mass_ratio": "float"}
- Scoring: scored by hidden verifier

### Step 4: Compute CaVO3 LDA+DMFT results
- Role: scored (load-bearing)
- Action: Using the t2g DOS from step s2 and the interaction parameters U=5.55 eV, U′=3.55 eV, J=1.0 eV, set up a three-orbital LDA+DMFT calculation. Solve the impurity problem with a continuous-time QMC solver at T≈300 K. Analytically continue the self-energy using the maximum entropy method to obtain the real-frequency spectral function. Extract: LDA t2g bandwidth (eV), lower Hubbard band peak position (eV), upper Hubbard band peak position (eV), quasiparticle peak weight, and effective mass ratio m*/m0 = 1/Z. Write these values to 'cavo3_results.json'.
- Output file: `/app/outputs/cavo3_results.json`
- Format: json
- Contract: {"lda_bandwidth": "float (eV)", "lower_hubbard_band_peak": "float (eV)", "upper_hubbard_band_peak": "float (eV)", "quasiparticle_peak_weight": "float", "effective_mass_ratio": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/srvo3_results.json`
- `/app/outputs/cavo3_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### srvo3_results.json
- path: `/app/outputs/srvo3_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: SrVO3 LDA+DMFT results: t2g bandwidth, Hubbard band positions, quasiparticle weight, effective mass ratio.
- schema:
  - `type`: object
  - `required`:
    - `lda_bandwidth`: float (eV)
    - `lower_hubbard_band_peak`: float (eV)
    - `upper_hubbard_band_peak`: float (eV)
    - `quasiparticle_peak_weight`: float
    - `effective_mass_ratio`: float

### cavo3_results.json
- path: `/app/outputs/cavo3_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: CaVO3 LDA+DMFT results: t2g bandwidth, Hubbard band positions, quasiparticle weight, effective mass ratio.
- schema:
  - `type`: object
  - `required`:
    - `lda_bandwidth`: float (eV)
    - `lower_hubbard_band_peak`: float (eV)
    - `upper_hubbard_band_peak`: float (eV)
    - `quasiparticle_peak_weight`: float
    - `effective_mass_ratio`: float

Notes: Interaction parameters U=5.55 eV, U′=3.55 eV, J=1.0 eV are fixed input for the LDA+DMFT steps. The Hubbard band peaks are the local maxima of the lower and upper Hubbard bands in the spectral function. Quasiparticle peak weight quantifies the coherent spectral weight at the Fermi level; effective mass ratio is derived from the quasiparticle weight as m*/m0 = 1/Z.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "srvo3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lda_bandwidth": "float (eV)",
          "lower_hubbard_band_peak": "float (eV)",
          "upper_hubbard_band_peak": "float (eV)",
          "quasiparticle_peak_weight": "float",
          "effective_mass_ratio": "float"
        }
      },
      "description": "SrVO3 LDA+DMFT results: t2g bandwidth, Hubbard band positions, quasiparticle weight, effective mass ratio."
    },
    {
      "file": "cavo3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lda_bandwidth": "float (eV)",
          "lower_hubbard_band_peak": "float (eV)",
          "upper_hubbard_band_peak": "float (eV)",
          "quasiparticle_peak_weight": "float",
          "effective_mass_ratio": "float"
        }
      },
      "description": "CaVO3 LDA+DMFT results: t2g bandwidth, Hubbard band positions, quasiparticle weight, effective mass ratio."
    }
  ],
  "notes": "Interaction parameters U=5.55 eV, U′=3.55 eV, J=1.0 eV are fixed input for the LDA+DMFT steps. The Hubbard band peaks are the local maxima of the lower and upper Hubbard bands in the spectral function. Quasiparticle peak weight quantifies the coherent spectral weight at the Fermi level; effective mass ratio is derived from the quasiparticle weight as m*/m0 = 1/Z."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage’s output artifact (the two JSON files). For each scored quantity the verifier compares your submitted value to a reference obtained from the paper's reported results and, where applicable, checks the structural trend. The per-stage scores are combined with pre‑determined weights to yield a final reward in [0, 1]. Reporting numbers copied from the paper without actually executing the computational pipeline is not sufficient; the reward reflects the correctness of your *computed* spectral features and the effective mass ratio.
