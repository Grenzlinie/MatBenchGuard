# Compute and Analyze Thermoelectric Power Factor

## Overview
This workflow family encompasses tasks that compute the thermoelectric power factor (PF) from experimentally measured Seebeck coefficient and electrical conductivity (or resistivity) data, and then analyze the power factor's dependence on temperature and material composition/processing parameters. The goal is to identify optimal conditions that maximize PF.

## Common Computational Pattern
Across the family, the typical steps are:
1. **Input Data**: Collect measured Seebeck coefficient \(S(T)\) (or thermopower \(\alpha\)) and electrical conductivity \(\sigma(T)\) (or resistivity \(\rho(T)\)) for a series of samples that differ in composition or processing conditions.
2. **Calculate Power Factor**: Compute PF using the relation \(PF = S^2 \sigma = \alpha^2 / \rho\).
3. **Analyze Dependencies**: Plot PF as a function of temperature and as a function of the controlled parameter (e.g., doping level, annealing temperature, film thickness).
4. **Optimization**: Determine the temperature where PF is maximized and identify the material conditions that yield the highest PF.
5. **Reporting**: Provide PF curves, maximum PF values, and the corresponding optimal parameters.

## Typical Resources
- **Input Data**: Tabulated Seebeck coefficient and electrical conductivity/resistivity as functions of temperature and sample identifier.
- **Output Artifacts**: Computed PF(T) curves, comparison plots showing parameter dependence, and a summary of the optimal PF and conditions.

## Verification
Verification is numeric. The computed PF(T) curves and their maxima are compared against values reported in peer-reviewed literature. Successful reproduction requires agreement within a specified tolerance.

## Domains
- 热电材料
- 材料科学
- 凝聚态物理

## Lab Type
This is a dry-lab workflow. All steps involve numerical computation, plotting, and analysis of existing experimental data without new laboratory measurements.
