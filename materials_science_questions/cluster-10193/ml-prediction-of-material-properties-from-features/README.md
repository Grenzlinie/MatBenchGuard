# ML Prediction of Material Properties from Features

This workflow family covers papers that apply **machine learning regression models** to predict target properties of materials from **features derived from composition, structure, or electronic structure**. The core modeling task is supervised regression, evaluated through cross-validation (often k‑fold or leave‑one‑out) using standard numerical metrics (`MAE`, `RMSE`, `R²`). Many papers extend the basic pipeline with feature selection, model interpretation, uncertainty quantification, or active learning, and then apply the trained model to **screen large candidate spaces** for novel materials.

## Common Computational Pattern

1. **Data curation or generation**  
   - Assemble a labeled dataset: either from public databases (OQMD, ICSD, Materials Project, QM9, SuperCon, etc.), first‑principles calculations (DFT), or experimental measurements.  
   - Prepare a consistent training/test split, often with stratification by chemical family or composition, or using forward splits for extrapolation evaluation.

2. **Feature engineering**  
   - Map each material to a numeric feature vector using one of:
     - Composition‑based features: weighted averages, differences, max/min, etc. of elemental properties (electronegativity, atomic radius, valence electron concentration, etc.).
     - Structural fingerprints: SOAP, Voronoi tessellation features, bond‑orientational order parameters, XRD pattern descriptors, Coulomb matrices, or pretrained graph embeddings.
     - Spectral or electronic‑structure descriptors: multiscale polynomial featurization of XANES/ELNES spectra, O p‑band center, or DFT‑derived properties.
   - Optionally apply dimensionality reduction (PCA, recursive feature elimination) to obtain a compact input set.

3. **Model selection and training**  
   - Regression algorithms commonly used in the family:
     - Tree‑based: Random Forest, XGBoost, Extra Trees, Gradient Boosted Regression.
     - Kernel methods: Support Vector Regression (SVR) with RBF or linear kernel, Kernel Ridge Regression.
     - Neural networks: Multilayer perceptron (MLP), deep neural networks (MeltNet, WaveTENet), graph neural networks (SchNet, coGN), transformers (CAST, BERTOS), variational Bayesian neural network.
     - Ensembles: shallow ensembles (DPOSE) or bootstrap‑resampled ensembles for uncertainty quantification.
   - Hyperparameters are tuned via grid search, Bayesian optimization, or heuristic sweeps, using internal cross‑validation on the training set.

4. **Evaluation**  
   - Performance is measured by **mean absolute error (MAE)**, **root mean squared error (RMSE)**, and **coefficient of determination (R²)** on held‑out test data or via **k‑fold cross‑validation** (often repeated to get stable statistics).  
   - Some papers employ **forward cross‑validation** (kmFCV) to specifically assess explorative prediction power for materials with property values outside the training domain.
   - Where relevant, uncertainty estimates are validated by computing coverage (fraction of true values within ±nσ).

5. **Interpretation and feature importance**  
   - Models are often interrogated to identify the most predictive descriptors (e.g., SHAP values, permutation importance, Gini importance), linking performance to physically meaningful trends.

6. **Virtual screening and candidate discovery**  
   - The final trained model is applied to a large pool of hypothetical or experimentally known compounds to identify candidates with desirable properties (e.g., high dielectric constant, suitable band‑gap, high oxygen storage capacity, selective catalysts, stable 2D materials).  
   - Top candidates may be further validated with DFT calculations or synthesis/measurement (where those steps are part of a paper’s larger pipeline but are not required by the Harbor task itself).

## Typical Verification Style

This is a **dry‑lab workflow family** with **numeric verification**. Reproducibility is assessed by:
- Comparing the predicted property values (or prediction errors) against reference results from the literature or against a provided baseline model.
- Checking that the reported regression metrics (`MAE`, `RMSE`, `R²`) fall within a **tolerance window** of the expected values (e.g., relative error < 5–10%, or absolute differences compatible with reported cross‑validation uncertainties).
- For tasks that include candidate screening, verifying that the top‑ranked candidates match the paper’s published list.

## Categories of Datasets, Models, and Tools

**Datasets**  
- Public materials databases: OQMD, ICSD, Materials Project, C2DB, QM9, SuperCon  
- DFT‑calculated properties: formation energies, band gaps, oxygen storage capacities, segregation energies, adsorption energies  
- Experimental property collections: cloud point temperatures, thermal quenching temperatures, liquidus temperatures  
- Simulated spectra: ELNES/XANES, XRD patterns  

**Model types**  
- Random Forest, Extra Trees, XGBoost  
- Support Vector Regression (SVR) with linear, RBF, or polynomial kernel  
- Kernel Ridge Regression, Gaussian Process Regression  
- Deep Neural Networks (feedforward, residual, Bayesian)  
- Graph Neural Networks (SchNet, coGN)  
- Multimodal transformers (CAST)  
- Shallow ensembles (DPOSE, bootstrap resampling)  

**Software tools commonly used**  
- Python: scikit‑learn, PyTorch, TensorFlow, Keras  
- Materials informatics: pymatgen, MAST‑ML, ASE, QUIP  
- DFT packages: VASP, SCFT  
- Spectral analysis: custom featurization scripts  

## Harbor Task Structure

Each `paper-*` subdirectory is a **standalone Harbor task** that recreates a specific prediction model, evaluation, or screening experiment from one paper in the family. The public entry point is:

- `instruction.md` – details the exact task to be solved, including required inputs, expected outputs, and any numerical tolerances.

No other bundled resources are provided; the solving agent must retrieve necessary datasets, install software dependencies, and generate any auxiliary files as instructed.

## Notes

- Because all papers rely on **machine learning regression with numeric verification**, tasks will typically require training a model, evaluating it on a specified test split, and reporting the performance metrics.
- Some tasks involve **uncertainty quantification** or **extrapolation evaluation**; in these cases the instruction will specify how to compute and compare the uncertainty metrics or forward‑CV scores.
- This family is entirely computational (**dry lab**); no physical experiments or instrument operation are required by the Harbor tasks.
