# Thermal Conductivity of Ni-Coated Tri-Walled Carbon Nanotubes with Vacancies

## Background
A published molecular dynamics study investigated how random vacancies and a nickel (Ni) coating affect the axial thermal conductivity of tri-walled carbon nanotubes (3WCNTs). The paper reports a pristine (defect‑free) 3WCNT thermal conductivity and the percentage changes caused by 0.5 % and 1 % vacancies, as well as the enhancement from a 3 nm Ni coating applied to the defective tubes. Your task is to use the paper‑reported parameters to compute the thermal conductivity for five specific configurations; no molecular dynamics simulation is required.

## Key parameters (extracted from the paper’s Results section)
- **Pristine 3WCNT thermal conductivity**: **820 W/mK** (as plotted in the paper’s Figure 6 and used in its own percentage calculations).
- **Vacancy effect** (relative to pristine):
  - 0.5 % random vacancies → **76 % reduction** in thermal conductivity.
  - 1 % random vacancies → **86 % reduction** in thermal conductivity.
- **Coating effect** (relative to the corresponding defective tube, 3 nm Ni coating):
  - On the **0.5 %** defective tube → **66 % increase** in thermal conductivity.
  - On the **1 %** defective tube → **140 % increase** in thermal conductivity.

> All percentage values are taken directly from the paper (abstract and Sections 3–4). The pristine baseline matches the paper’s value; you do not need to consult any external document.

## Configurations to compute
| Condition name          | Description                                   |
|-------------------------|-----------------------------------------------|
| `pristine`              | Defect‑free 3WCNT                             |
| `vacancy_0.5`           | 3WCNT with 0.5 % random vacancies             |
| `vacancy_1.0`           | 3WCNT with 1 % random vacancies               |
| `coated_0.5_3nm`        | `vacancy_0.5` plus 3 nm Ni coating            |
| `coated_1.0_3nm`        | `vacancy_1.0` plus 3 nm Ni coating            |

## How to compute the thermal conductivities
1. **Defective configurations** (uncoated):  
   \(k_{\text{defective}} = k_{\text{pristine}} \times \left(1 - \frac{reduction\%}{100}\right)\)

2. **Coated configurations**:  
   \(k_{\text{coated}} = k_{\text{defective}} \times \left(1 + \frac{increase\%}{100}\right)\)

Apply the appropriate reduction and increase percentages from the table above. All computed values must be positive, and for each vacancy concentration the coated conductivity must be larger than the corresponding defective uncoated conductivity.

## Output file
- Path: `/app/outputs/thermal_conductivities.csv`
- Format: CSV (comma‑separated) with a header row.
- Required columns exactly:
  - `condition` (string, exactly one of: `pristine`, `vacancy_0.5`, `vacancy_1.0`, `coated_0.5_3nm`, `coated_1.0_3nm`)
  - `thermal_conductivity` (positive float, in W/mK)
- The order of rows does not matter.

**Example of acceptable structure** (the numeric values shown are only placeholders; you must compute the actual values):
```
condition,thermal_conductivity
pristine,820.0
vacancy_0.5,???
vacancy_1.0,???
coated_0.5_3nm,???
coated_1.0_3nm,???
```

## Scoring notes
A hidden checker will compare your reported thermal conductivities against the values that follow from the above parameters (with a generous tolerance of ±25 %). It will also verify that the coated conductivities are strictly higher than the corresponding defective uncoated conductivities. Your file will also be checked for correct column names and allowed condition labels.