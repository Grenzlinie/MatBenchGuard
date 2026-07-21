# Compute thermodynamic descriptors for (CuFeMnNi)₁₋ₓCrₓ high-entropy alloys

## Problem background
High-entropy alloys (HEAs) are multicomponent alloys that can form simple solid solution phases (FCC, BCC) rather than complex intermetallics. Their phase stability and microstructure are often predicted by empirical thermodynamic descriptors: mixing enthalpy (ΔH_mix), configurational entropy (ΔS_mix), the stability parameter Ω, atomic-size difference (δ), and valence electron concentration (VEC). This task computes these five descriptors for a series of (CuFeMnNi)₁₋ₓCrₓ alloys with varying Cr content, providing the quantitative basis to assess whether solid solution phases are expected to form.

## Approach
The computation follows standard HEA empirical formulas using the alloy's atomic fractions and tabulated elemental properties.

- ΔH_mix = Σ_{i<j} c_i c_j · Ω_ij, where Ω_ij (kJ mol⁻¹) is the binary mixing enthalpy parameter for the i–j pair.
- ΔS_mix = –R Σ c_i ln c_i, with the gas constant R = 8.314 J K⁻¹ mol⁻¹.
- Ω = (T · ΔS_mix) / |ΔH_mix|, where T is the composition-averaged melting temperature T_m = Σ c_i T_{m,i}. The elemental melting points T_{m,i} are given in the Assets.
- δ = 100 · √( Σ c_i (1 – r_i / ⟨r⟩)² ), where ⟨r⟩ = Σ c_i r_i is the average atomic radius.
- VEC = Σ c_i · (VEC)_i.

The alloy compositions are (CuFeMnNi)₁₋ₓCrₓ with x = 0, 0.05, 0.10, 0.15, 0.20, 0.25. The atomic fractions are: Cr = x, and Cu = Fe = Mn = Ni = (1 – x) / 4. All required elemental data (Ω_ij, atomic radii, VEC numbers, melting points) are provided in the Assets section.

## Important: your final output must be a CSV file, not JSON
You must save one CSV file: `/app/outputs/thermodynamic_parameters.csv`. Do **not** output any JSON files. Do **not** confuse the shape‑check contract below with a requirement to write JSON. The contract is for automated validation of the CSV’s column names; you only need to produce the CSV.

## Reproduction target
Produce a CSV file containing the five thermodynamic parameters for all six alloy compositions, ordered by increasing Cr content. The output must follow the exact format described in the workflow step: columns Alloy, Cr_content, Delta_H_mix_kJ_mol, Delta_S_mix_J_K_mol, Omega, delta_percent, VEC. Your computed values will be compared to independently obtained reference values using a relative error metric.

## Assets
The elemental data needed for the calculations are given below; no external download is required.

**Binary mixing enthalpy parameters Ω_ij (kJ mol⁻¹)**  
Cu–Fe: 52, Cu–Mn: 16, Cu–Ni: 16, Cu–Cr: 48  
Fe–Mn: 0, Fe–Ni: –8, Fe–Cr: –4  
Mn–Ni: –32, Mn–Cr: 8  
Ni–Cr: –28

**Atomic radii (pm)**  
Cu: 128, Fe: 124, Mn: 135, Ni: 125, Cr: 128

**Valence electron counts**  
Cu: 11, Fe: 8, Mn: 7, Ni: 10, Cr: 6

**Elemental melting points (K)**  
Cu: 1358, Fe: 1811, Mn: 1519, Ni: 1728, Cr: 2180

**Gas constant**  
R = 8.314 J K⁻¹ mol⁻¹.

## Workflow steps

### Step 1: Compute thermodynamic parameters
- Role: scored (load-bearing)
- Action: Given the alloy compositions (atomic fractions: for (CuFeMnNi)₁₋ₓCrₓ, Cu=Fe=Mn=Ni=(1-x)/4, Cr=x, with x=0, 0.05, 0.1, 0.15, 0.2, 0.25) and the elemental data (binary mixing enthalpies, atomic radii, valence electron counts, melting points, and gas constant R=8.314 J/K/mol) provided in the instruction, compute for each alloy: mixing enthalpy ΔH_mix as sum over all i,j of c_i*c_j*ΔH_ij_mix (with ΔH_ij_mix for the Cu-Fe-Mn-Ni-Cr system given), configurational entropy ΔS_mix = -R Σ c_i ln c_i, stability parameter Ω = T_m ΔS_mix / |ΔH_mix| where T_m = Σ c_i T_{m,i} using the elemental melting points in the Assets, atomic-size difference δ = 100 * sqrt( Σ c_i (1 - r_i / ⟨r⟩)² ), and valence electron concentration VEC = Σ c_i VEC_i. Write the results to a CSV file.
- Output file: `/app/outputs/thermodynamic_parameters.csv`
- Format: csv (not JSON)
- Contract: The CSV must have exactly the following header row:
  `Alloy,Cr_content,Delta_H_mix_kJ_mol,Delta_S_mix_J_K_mol,Omega,delta_percent,VEC`

  Each of the six rows corresponds to one alloy, ordered by increasing Cr content.
  - `Alloy`: string, one of `'0%Cr'`, `'5%Cr'`, `'10%Cr'`, `'15%Cr'`, `'20%Cr'`, `'25%Cr'`.
  - `Cr_content`: the x value as a float.
  - All other columns: numeric values as floats, written with sufficient precision (e.g. 6 decimal places) so that the scoring check can read them.

  Example of one row (the actual numbers are computed by you, shown here only to illustrate the required shape):
  `0%Cr,0.0,2.750000,11.530000,6.720000,3.400000,9.000000`

  **Never** write the file as JSON or any other format; it must be plain CSV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_parameters.csv`

## How you are scored
A hidden verifier will read your thermodynamic_parameters.csv and compare each entry to a hidden reference (derived from the original research). It will compute a relative error metric across all alloys and all five parameters, then convert the overall deviation into a reward between 0 and 1. Smaller errors yield higher rewards.