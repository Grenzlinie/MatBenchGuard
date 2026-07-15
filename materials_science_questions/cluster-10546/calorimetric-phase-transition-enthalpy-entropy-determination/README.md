# Calorimetric Phase Transition Enthalpy/Entropy Determination

## Overview

This workflow family addresses the determination of enthalpy (ΔH) and entropy (ΔS) changes associated with first‑order phase transitions (solid‑solid or solid‑liquid) from calorimetric data. The core task is to process heat capacity (Cp) or enthalpy‑versus‑temperature curves, isolate the transition anomaly, define an appropriate baseline, and compute the excess thermodynamic quantities. The computed values are typically compared with literature data or validated against independent relations (e.g., Clausius‑Clapeyron) to confirm reproducibility.

## Common Computational Pattern

The workflow follows a sequence of steps that are consistent across the papers in this family:

1. **Data ingestion** – Experimental heat capacity (or enthalpy) values as a function of temperature are obtained, usually from adiabatic calorimetry, differential scanning calorimetry (DSC), or similar techniques. Data are often provided in tabular form covering a temperature range that spans the transition region.

2. **Transition identification** – The temperature at which the anomaly occurs (onset, maximum, or shoulder) is located, either from a Cp(T) peak or from an isothermal latent‑heat signal.

3. **Baseline construction** – A smooth “normal” heat capacity curve is constructed across the transition region. Common approaches include:  
   - Linear or polynomial interpolation of Cp data from above and below the anomaly.  
   - Extrapolation of low‑temperature and high‑temperature asymptotic behavior.  
   - Subtraction of a smooth background obtained from analogous non‑transitioning systems or theoretical models.

4. **Excess heat capacity extraction** – The baseline is subtracted from the measured Cp to obtain ΔCp_excess(T) = Cp(T) – Cp_baseline(T).

5. **Integration** – The transition enthalpy and entropy are calculated by integrating the excess heat capacity:  
   - ΔH_trans = ∫ ΔCp_excess(T) dT (or directly from the total enthalpy jump if a latent heat is present).  
   - ΔS_trans = ∫ [ΔCp_excess(T) / T] dT  (or ΔH_trans / T_trans if the transition is sharp).  
   For multi‑step transitions or overlapping anomalies, the total enthalpy is partitioned appropriately (e.g., by fitting multiple peaks or by using known transition temperatures).

6. **Uncertainty estimation** – Uncertainties are propagated from the calibration of the calorimeter, baseline choice, and integration errors. Reported values often include both statistical (repeatability) and systematic (baseline arbitrariness) components.

7. **Validation** – The derived ΔH and ΔS are compared with published experimental values or checked for consistency via the Clausius‑Clapeyron relation (ΔS = ΔH/T_trans) and/or by verifying that the reduced Gibbs free energy function Φ(T) = S(T) – [H(T) – H(0)]/T is continuous across the transition.

## Verification Style

The verification for this family is **numeric**: reproducibility is assessed by comparing the calculated ΔH and ΔS with reference values from the literature or, when available, with values inferred from pressure‑dependent transition temperatures via the Clausius‑Clapeyron equation. The verification note supplied with the family states: “通过比较计算出的ΔH和ΔS与文献值（或由Clausius-Clapeyron关系验证）的数值容差来判定复现是否成功” (success is judged by the numerical tolerance between computed and reference values).

## Task Structure

Each subdirectory `paper-*` corresponds to a single published study and is a self‑contained Harbor task. The public interface for every task is the file `instruction.md`, which describes the specific data, equations, and integration procedures required to reproduce the original transition enthalpy and entropy. No separate `TASK.md` is used.

## Required Resources

The workflow is purely computational (lab‑type “dry”) and does not require new experimental data. The necessary inputs—heat capacity tables, transition temperatures, and baseline rules—are provided within each task’s `instruction.md`. Custom software is not mandatory; the steps can be performed with numerical integration tools or spreadsheet programs.
