# Calorimetric Enthalpy, Entropy, and Heterophase‑Fluctuation Model for a Spin‑Crossover Compound

## Background
Certain octahedral iron(II) complexes exhibit a cooperative spin‑transition between a low‑spin (LS) and a high‑spin (HS) electronic ground state. High‑precision heat‑capacity measurements reveal a sharp anomaly that contains information about the enthalpy and entropy of the transition. The observed entropy change is too large to be purely magnetic, pointing to a substantial coupling between the electronic state and the phonon system.  
In this task you will analyse such data for two related compounds and evaluate a phenomenological “heterophase‑fluctuation” model that treats the system as a mixture of LS and HS domains.

## Objective
For two compounds – called **NCS** and **NCSe** – you must:
1. Separate the experimental heat capacity into a “normal” (non‑transition) baseline and an excess contribution.
2. Determine the transition temperature, transition enthalpy, and transition entropy from the excess heat capacity.
3. Use the excess peak height to estimate the number of cells per mole (`N`) and molecules per cell (`n`) in the heterophase‑fluctuation model.
4. Compute the full model heat‑capacity curve across the transition.

## Physical model and formulas

### 1. Normal heat capacity baseline
The measured molar heat capacity is assumed to consist of three terms (in the absence of the transition):

\[
C_{p}(\text{normal})=C_{\rm Debye}(\nu_{\rm cut})+\sum_i g_i\,C^{\rm E}(\tilde{\nu}_i)+C_{\rm mag}
\]

- **Debye term** – approximates the acoustic lattice vibrations. Its cut‑off wavenumber \(\nu_{\rm cut}\) is fixed for a given phase (see below).  
  The Debye heat capacity is

  \[
  C_{\rm Debye}(T)=9R\left(\frac{T}{\theta_D}\right)^3\int_0^{\theta_D/T}\frac{x^4 e^x}{(e^x-1)^2}\,dx
  \]
  where \(\theta_D = \dfrac{h c}{k_B}\,\nu_{\rm cut}\) is the Debye temperature, \(R=8.314\;\mathrm{J\,K^{-1}\,mol^{-1}}\) is the gas constant,  
  \(h = 6.62607015\times10^{-34}\;\mathrm{J\,s}\), \(c = 2.99792458\times10^{10}\;\mathrm{cm\,s^{-1}}\), and \(k_B = 1.380649\times10^{-23}\;\mathrm{J\,K^{-1}}\).

  **Important:** The Debye term is the only adjustable part of the baseline. The cut‑off wavenumber \(\nu_{\rm cut}\) is **not** varied during fitting; instead, it is prescribed for each baseline curve (see §2). The fit determines only the amplitude (the effective number of Debye oscillators per mole) and, optionally, a **small constant background** (see below).

- **Einstein terms** – for each internal molecular vibration (IR‑active mode) with wavenumber \(\tilde{\nu}_i\) and degeneracy \(g_i\),

  \[
  C^{\rm E}(\tilde{\nu}_i,T)=R\left(\frac{\theta_i}{T}\right)^2\frac{e^{\theta_i/T}}{(e^{\theta_i/T}-1)^2},
  \qquad
  \theta_i=\frac{h c}{k_B}\,\tilde{\nu}_i\,.
  \]
  The file `resources/ir_wavenumbers.csv` lists the wavenumbers, degeneracies, and phase assignments (low‑temperature / high‑temperature) required to calculate this term.

- **Magnetic / electronic term** – arises from thermal population of the low‑lying electronic levels.  
  The file `resources/energy_params.json` contains, for each compound, the energies (in \(\mathrm{cm}^{-1}\)) and degeneracies of the electronic states that contribute in the temperature range of interest.  
  The partition function is  

  \[
  Z=\sum_j g_j\,e^{-E_j/k_B T}
  \]
  with \(E_j = h c\,\tilde{\nu}_j\) (where \(\tilde{\nu}_j\) is the energy level expressed as a wavenumber).  
  The mean energy per mole is \(\langle E\rangle = R\,T^2\,\dfrac{\partial\ln Z}{\partial T}\), and the magnetic heat capacity is

  \[
  C_{\rm mag} = \frac{\partial \langle E\rangle}{\partial T}
  = \frac{R}{T^2}\Big(\langle E^2\rangle - \langle E\rangle^2\Big),
  \]
  where \(\langle E^2\rangle = Z^{-1}\sum_j g_j E_j^2 e^{-E_j/k_B T}\).

### 2. Constructing the normal baseline
The Debye term is the only unknown part. It is obtained separately for the low‑temperature (LT) and high‑temperature (HT) phases, each with two different cut‑off wavenumbers (30 cm⁻¹ and 50 cm⁻¹), giving four baseline curves:

- Curve A: LT phase, \(\nu_{\rm cut}=30\;\mathrm{cm}^{-1}\)
- Curve B: LT phase, \(\nu_{\rm cut}=50\;\mathrm{cm}^{-1}\)
- Curve C: HT phase, \(\nu_{\rm cut}=30\;\mathrm{cm}^{-1}\)
- Curve D: HT phase, \(\nu_{\rm cut}=50\;\mathrm{cm}^{-1}\)

For a given phase and \(\nu_{\rm cut}\):
1. Choose temperature windows sufficiently far from the anomaly where the excess contribution is negligible.  
   Suggested windows (adapt to the actual compound’s data if needed):  
   – LT phase: 13 K to 140 K  
   – HT phase: 240 K to 375 K  
   (For NCSe, the anomaly is centred higher; adjust the HT window accordingly, e.g. 290–375 K, and similarly for the LT window.)
2. In those windows, subtract the already‑computed Einstein and magnetic heat capacities from the experimental \(C_p\) to obtain the lattice (Debye) contribution.
3. Fit these lattice points with the Debye formula \(C_{\rm Debye}(T)\) **plus an optional constant background** \(C_{\rm bg}\).  
   The amplitude of \(C_{\rm Debye}\) (effective number of oscillators) and \(C_{\rm bg}\) are the only free parameters.  
   **Constraint on the constant background:** \(|C_{\rm bg}|\) must not exceed 5% of the average lattice contribution in the fitting window. If a fit without a constant background already yields a good match (mean squared error within a few percent of the data variance), prefer that fit.
4. Use the fitted Debye curve (without the background) to evaluate the lattice contribution at **all** temperatures, including through the transition region. (The constant background is used only during fitting to improve the high‑temperature tail; it is not propagated into the final lattice curve.)
5. Add back the Einstein and magnetic contributions to obtain the full normal heat capacity for that phase and cut‑off.

The four resulting normal heat‑capacity curves are used as follows:

- **Average baseline for excess calculation:** Average curves A, B, C, D at every temperature to obtain a single smooth baseline \(C_{p,\mathrm{normal}}(T)\) valid over the entire temperature range.  
  This averaged baseline is used to compute the excess heat capacity and the transition thermodynamic quantities.
- **Pure‑phase baselines for the model:**  
  – Low‑spin phase baseline \(C_{p,L}(T)\) = average of curves A and B (the two LT‑based curves).  
  – High‑spin phase baseline \(C_{p,H}(T)\) = average of curves C and D (the two HT‑based curves).

### 3. Excess heat capacity and thermodynamic quantities
The excess heat capacity due to the transition is

\[
\Delta C_{p,\mathrm{excess}}(T)=C_{p,\mathrm{exp}}(T)-C_{p,\mathrm{normal}}(T),
\]

where \(C_{p,\mathrm{normal}}(T)\) is the averaged baseline (A–D average).

The transition temperature \(T_c\) is taken as the temperature at which the **experimental** \(C_{p,\mathrm{exp}}\) reaches its maximum.  
Record the experimental peak value \(C_{p,\max}\) and evaluate the normal baseline at \(T_c\) to obtain \(C_{p,\mathrm{normal}}(T_c)\).

The transition enthalpy and entropy are obtained by numerical integration of the excess heat capacity:

\[
\Delta H_{\text{trans}} = \int_{T_1}^{T_2} \Delta C_{p,\mathrm{excess}}(T)\,\mathrm{d}T,
\qquad
\Delta S_{\text{trans}} = \int_{T_1}^{T_2} \frac{\Delta C_{p,\mathrm{excess}}(T)}{T}\,\mathrm{d}T,
\]

where the integration limits \(T_1\) and \(T_2\) must be chosen well outside the anomaly such that the integrals are converged (for instance, \(T_1 = T_c - 30\text{ K}\) and \(T_2 = T_c + 30\text{ K}\), adapted to the data range). Use trapezoidal or Simpson integration on the experimental temperature grid; if necessary, interpolate \(\Delta C_{p,\mathrm{excess}}\) onto a uniform fine grid to improve accuracy.

### 4. Heterophase‑fluctuation model
The system is divided into cells, each containing \(n\) molecules. Every cell is either in the LS phase (L) or the HS phase (H). The molar Gibbs free energy is

\[
G = x\,G_H + (1-x)\,G_L + N k_{\mathrm{B}} T\big[x\ln x + (1-x)\ln(1-x)\big],
\]

with \(x\) the fraction of HS cells, \(N\) the number of cells per mole, and \(G_H,G_L\) the molar free energies of the pure phases.  
Minimisation with respect to \(x\) yields the equilibrium condition

\[
\ln\frac{x}{1-x} = -\frac{\Delta H - T\Delta S}{N k_{\mathrm{B}} T},
\]

where \(\Delta H = H_H - H_L\) and \(\Delta S = S_H - S_L\) are the enthalpy and entropy differences of the **pure** phases.  
These pure‑phase differences are obtained from the pure‑phase baselines \(C_{p,L}\) and \(C_{p,H}\) constructed in §2:

\[
H_L(T) = \int_{T_{\text{ref}}}^{T} C_{p,L}(T')\,\mathrm{d}T', \qquad
H_H(T) = \int_{T_{\text{ref}}}^{T} C_{p,H}(T')\,\mathrm{d}T',
\]
\[
S_L(T) = \int_{T_{\text{ref}}}^{T} \frac{C_{p,L}(T')}{T'}\,\mathrm{d}T', \qquad
S_H(T) = \int_{T_{\text{ref}}}^{T} \frac{C_{p,H}(T')}{T'}\,\mathrm{d}T',
\]
where \(T_{\text{ref}}\) is a common reference temperature (e.g., the lowest experimental temperature). Then

\[
\Delta H = H_H(T_c) - H_L(T_c), \qquad
\Delta S = S_H(T_c) - S_L(T_c).
\]

(Any constant baseline shift that cancels in the differences is harmless; the key point is to evaluate the pure‑phase enthalpies/entropies at the transition temperature.)

The model heat capacity is

\[
C_{p}(T)=x\,C_{p,H}(T)+(1-x)\,C_{p,L}(T)+\frac{(\Delta H)^2}{N k_{\mathrm{B}} T^{2}}\,x(1-x),
\]

where \(C_{p,H}\) and \(C_{p,L}\) are the pure‑phase baselines, each used over the **full** temperature range (extrapolate the pure‑phase Debye+Einstein+mag terms if the pure‑phase fit only covered a restricted temperature interval).

At \(T_c\), \(x=1/2\) and the excess heat capacity peaks at

\[
\Delta C_{p,\max} = \frac{(\Delta H)^2}{4 N k_{\mathrm{B}} T_c^{2}}.
\]

The measured total heat capacity at the peak is

\[
C_{p,\max} = C_{p,\mathrm{normal}}(T_c) + \Delta C_{p,\max}.
\]

Using the experimental \(C_{p,\max}\), the normal baseline value \(C_{p,\mathrm{normal}}(T_c)\), the transition \(\Delta H\) (the pure‑phase enthalpy difference computed above), and \(T_c\), one obtains

\[
N = \frac{(\Delta H)^2}{4 k_{\mathrm{B}} T_c^{2}\big[C_{p,\max} - C_{p,\mathrm{normal}}(T_c)\big]}.
\]

The number of molecules per cell is then

\[
n = \frac{N_A}{N},
\]

where \(N_A = 6.02214076\times10^{23}\ \mathrm{mol^{-1}}\). Round \(n\) to the nearest integer.

Finally, the full model heat‑capacity curve \(C_p(T)\) is computed over a dense temperature grid around \(T_c\) (e.g. \(\pm 30\ \mathrm{K}\) at 0.1 K steps) using the expression above. The mole fraction \(x(T)\) at each temperature must be obtained by solving the equilibrium condition numerically (e.g., by root‑finding or by evaluating the logistic form \(x = 1 / (1 + \exp[(\Delta H - T\Delta S) / (N k_{\mathrm{B}} T)])\)).

## Assets
All data files are located under `/app/resources/` (or `/resources/`):

- **Experimental heat capacity**  
  `cp_NCS.csv` and `cp_NCSe.csv` – two columns: `T(K)`, `Cp(J/K/mol)`.
- **IR vibration data**  
  `ir_wavenumbers.csv` – contains wavenumber (cm⁻¹), degeneracy, and phase assignment (LT or HT) for internal modes.
- **Electronic energy levels**  
  `energy_params.json` – for each compound, the low‑lying electronic energies (as wavenumbers in cm⁻¹) and corresponding degeneracies needed to compute \(C_{\mathrm{mag}}\). (The file also lists the literature values of the axial field splitting, spin‑orbit coupling, etc., for reference; the energy levels themselves are given explicitly and are the ones to be used in the partition function.)

## Workflow

### Pre‑processing (not scored)
1. Read the raw \(C_p\) data, IR wavenumbers, and electronic level file.
2. Compute \(C^{\mathrm{E}}\) and \(C_{\mathrm{mag}}\) across the full temperature range using the formulas above.
3. For each of the four baseline curves (A–D), select the appropriate temperature windows, isolate the lattice part, fit the Debye model (with optional small constant background, constrained as described), and reconstruct the full normal \(C_p\).
4. Compute the average baseline \(C_{p,\mathrm{normal}}(T)\) as the mean of curves A–D. Compute the pure‑phase baselines \(C_{p,L}\) (average of A,B) and \(C_{p,H}\) (average of C,D).
5. Identify \(T_c\) as the temperature of maximum experimental \(C_p\), and record the corresponding \(C_{p,\max}\) and \(C_{p,\mathrm{normal}}(T_c)\).
6. Compute the pure‑phase enthalpy and entropy differences \(\Delta H\) and \(\Delta S\) by numerically integrating \(C_{p,L}\) and \(C_{p,H}\) from the lowest available temperature up to \(T_c\) and taking the difference.
7. Compute the transition excess heat capacity \(\Delta C_{p,\mathrm{excess}}(T) = C_{p,\mathrm{exp}}(T) - C_{p,\mathrm{normal}}(T)\), and integrate it to obtain \(\Delta H_{\text{trans}}\) and \(\Delta S_{\text{trans}}\) (these are the values that will be reported in Step 1).

### Step 1a (scored) — Transition quantities for NCS
- Compute \(\Delta C_{p,\mathrm{excess}}(T)\) and integrate to obtain \(\Delta H_{\text{trans}}\) (kJ mol⁻¹) and \(\Delta S_{\text{trans}}\) (J K⁻¹ mol⁻¹). Report \(T_c\) as well.
- Output `/app/outputs/step_01a_thermo_NCS.json` with:
  ```json
  {
    "compound": "[Fe(phen)2(NCS)2]",
    "Tc_K": <float>,
    "Delta_H_kJ_mol": <float>,
    "Delta_S_J_K_mol": <float>
  }
  ```

### Step 1b (scored) — Transition quantities for NCSe
- Same as 1a but for the NCSe compound.  
  Output `/app/outputs/step_01b_thermo_NCSe.json` with `compound` set to `"[Fe(phen)2(NCSe)2]"`.

### Step 2a (scored) — Model parameters for NCS
- Using the measured \(C_{p,\max}\), \(C_{p,\mathrm{normal}}(T_c)\), and the pure‑phase enthalpy difference \(\Delta H\) computed from the baselines, calculate \(N\) and \(n\) using the formulas in §4.  
  Output `/app/outputs/step_02a_model_NCS.json`:
  ```json
  {
    "compound": "[Fe(phen)2(NCS)2]",
    "N_mol-1": <float>,
    "n": <int>
  }
  ```

### Step 2b (scored) — Model parameters for NCSe
- Same as 2a for NCSe. Output `/app/outputs/step_02b_model_NCSe.json`.

### Step 3a (scored) — Model \(C_p\) curve for NCS
- Generate the model heat capacity \(C_p(T)\) using the heterophase‑fluctuation model over a dense grid from \(T_c-30\ \mathrm{K}\) to \(T_c+30\ \mathrm{K}\) (step 0.1 K).  
  Output `/app/outputs/step_03a_cp_anomaly_NCS.csv` with columns exactly:
  ```
  T(K),Cp_model(J/K/mol)
  ```
  (floating‑point values).

### Step 3b (scored) — Model \(C_p\) curve for NCSe
- Same as 3a for NCSe. Output `/app/outputs/step_03b_cp_anomaly_NCSe.csv`.

## Important notes
- The Einstein and magnetic terms are fixed by the supplied data; the only adjustable part of the baseline is the Debye contribution.
- The four baseline curves are averaged to produce one smooth normal \(C_p\) for excess calculation; the pure‑phase baselines are obtained by averaging the two LT curves and the two HT curves, respectively.
- All integrations (enthalpy, entropy, model quantities) must use numerical methods (trapezoidal or Simpson) and should be tested for convergence by varying the grid spacing.
- When fitting the Debye curves, use the temperature windows suggested, but you may adjust the boundaries slightly to avoid residual anomaly tails; document your window choices in comments if possible.
- The constant background allowed in the Debye fit is strictly limited (≤5% of the average lattice value in the window) and must not be propagated into the final baseline curves.
- The pure‑phase enthalpy/entropy differences \(\Delta H, \Delta S\) used in the model are computed from the pure‑phase baselines \(C_{p,L}\) and \(C_{p,H}\), evaluated at \(T_c\).
- The model heat capacity in Steps 3a/3b must be computed with the equilibrium \(x(T)\) from the free‑energy minimisation, using the \(\Delta H,\Delta S\) derived from the pure‑phase baselines and the \(N\) obtained in Steps 2a/2b.

## Output files
All final artifacts must be written under `/app/outputs/`:

```
/app/outputs/step_01a_thermo_NCS.json
/app/outputs/step_01b_thermo_NCSe.json
/app/outputs/step_02a_model_NCS.json
/app/outputs/step_02b_model_NCSe.json
/app/outputs/step_03a_cp_anomaly_NCS.csv
/app/outputs/step_03b_cp_anomaly_NCSe.csv
```

The JSON files must contain the required keys; the CSV files must have the exact header `T(K),Cp_model(J/K/mol)` and contain numerical data.  
No other formats or filenames will be accepted.