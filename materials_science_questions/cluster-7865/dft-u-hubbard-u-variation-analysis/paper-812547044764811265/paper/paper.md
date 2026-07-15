NUCLEAR SCIENCE AND ENGINEERING
DOI: https://doi.org/10.1080/00295639.2020.1820826
![](./images/812547044764811265_1.jpg)
![](./images/812547044764811265_2.jpg)

# Generation of the Thermal Scattering Law of Uranium Dioxide with Ab Initio Lattice Dynamics to Capture Crystal Binding Effects on Neutron Interactions

J. L. Wormald, $^{\text{a}*}$ N. C. Fleming, $^{\text{b}}$ A. I. Hawari, $^{\text{b}}$ and M. L. Zerkle $^{\text{c}}$

$^{\text{a}}$Naval Nuclear Laboratory, P.O. Box 1072, Schenectady, New York 12309
$^{\text{b}}$North Carolina State University, Department of Nuclear Engineering, Raleigh, North Carolina 27695
$^{\text{c}}$Naval Nuclear Laboratory, P.O. Box 79, West Mifflin, Pennsylvania 15122

Received July 10, 2020
Accepted for Publication September 3, 2020

Abstract — Scattering of thermal neutrons and Doppler broadening of epithermal neutron resonances in uranium and its compounds may be sensitive to crystal binding. The thermal scattering law (TSL) for uranium dioxide, which captures crystal binding effects, has been reevaluated for ENDF/B-VIII.0. Phonon spectra were generated using ab initio lattice dynamics for the paramagnetic phase and validated against experiment. Improved agreement with the Debye-Waller coefficient as a function of temperature is found relative to the spectrum used for the ENDF/B-VII.1 evaluation. The TSL was generated using the phonon expansion method within the NJOY nuclear data processing package and was found to be in reasonable agreement with inelastic neutron scattering measurements. The present evaluation predicts a reduction in the inelastic scattering cross section relative to ENDF/B-VII.1 and a total scattering cross section consistent with neutron transmission experiments.

Keywords — Uranium dioxide, thermal scattering law, phonons, resonances, ENDF/B-VIII.0.

Note — Some figures may be in color only in the electronic version.

## I. INTRODUCTION

Uranium dioxide ($\text{UO}_2$) is the primary fuel compound used in commercial nuclear power plants. In fission systems, such as nuclear power reactors or spent fuel pools, criticality is dependent on the fission and neutron absorption rates, which are sensitive to the neutron spectrum. At sufficiently low energies, crystal binding influences the neutron cross section, which is an effect that is captured in the thermal scattering law (TSL), $S(\mathbf{Q},\omega)$, also known as the dynamic structure factor. TSLs are widely used to capture the effects of crystal binding on thermal neutron scattering in criticality analysis; however, these effects may also impact the neutron resonance line shape in the epithermal energy range.$^{1–5}$ Within the past decade there has been a renewed interest for quantifying the impact of crystal binding on neutron resonance reactions.$^{6–8}$ Analysis of neutron transmission measurements in $^{238}\text{U}$ (Refs. 9 and 10) has indicated an impact of atomic vibration in $\text{UO}_2$ on the Doppler broadening of uranium epithermal resonances at and below room temperature.$^{6,8}$

*E-mail: jonathan.wormald@unnpp.gov
This material is published by permission of Naval Reactors under DOE Contract No. [DOE-89233018CNR000004]. The US Government retains for itself, and others acting on its behalf, a paid-up, non-exclusive, and irrevocable worldwide license in said article to reproduce, prepare derivative works, distribute copies to the public, and perform publicly and display publicly, by or on behalf of the Government.

The TSL is calculable from the energy spectrum of elementary harmonic vibrations (i.e., phonons) in crystalline materials. The Evaluated Nuclear Data File (ENDF) database contains a sublibrary of TSL evaluations for use in neutron transport analyses. The release of ENDF/B-VIII.0 expanded the available material database.¹¹ Additionally, several TSLs were reevaluated using ab initio methods in an effort to enhance the physics of the phonon spectra. The reevaluation of UO₂, developed in this work, included uranium in UO₂ and oxygen in UO₂ TSLs.

As a binary solid the phonon spectrum of UO₂ has contributions from acoustic and optical modes, which dominate the motion of uranium and oxygen, respectively. The phonon spectrum used in the TSL of UO₂ tabulated in ENDF/B-VII.1 is based on a semiempirical lattice dynamics model.¹² Despite providing reasonable agreement with measured phonon dispersion relations, this model, which describes interatomic forces with a shell potential, does not satisfactorily capture the mean-square displacement of uranium and oxygen vibrational motion as a function of temperature.

In an effort to improve the prediction of vibrational motion and its direct impact on Doppler broadening of neutron resonance and thermal neutron scattering, ab initio lattice dynamics (AILD) were used in this work to calculate the phonon spectrum of UO₂ using spin-polarized density functional theory (DFT) calculations. These methods utilize Hellmann-Feynman forces to predict the partial phonon density of states (DOS) for crystalline systems in the harmonic approximation. Previous DFT studies of UO₂ using a generalized gradient approximation exchange correlational functional with the inclusion of a Hubbard model adequately predict the electronic structure of the low-temperature antiferromagnetic (AFM) ground state.¹³⁻¹⁵ The spin-polarized calculations of this state were used to predict the phonons of the paramagnetic state. TSLs generated using the partial phonon DOS are tabulated as File 7 ENDF evaluations and compared to inelastic neutron scattering (INS) as well as neutron transmission measurements. The potential impact of the ENDF/B-VIII.0 TSL models on the physics of neutron scattering and resonance reactions is discussed.

## II. THEORY OF TSL

Interaction of neutrons with nuclei in crystals is dependent on the spectrum of vibrational excitations described by $S(\mathbf{Q},\omega)$, which corresponds to the momentum-energy space representation of the density-density autocorrelation function.¹⁶ These vibrational excitations have a characteristic momentum $\mathbf{Q}$ and energy $\omega$ ($\hbar=1$). Furthermore, the spectrum is basis position dependent in polyatomic systems, such as UO₂, due to the variation in phonon behavior resulting from changes in the crystal binding at different lattice sites.

For a basis position $g$, $S(\mathbf{Q},\omega)$ may be partitioned into a summation of increasing orders of discrete phonon processes (1-phonon, 2-phonon, 3-phonon, etc.) through the phonon expansion,¹⁷⁻¹⁹

$$
S_{g}(\mathbf{Q},\omega)=\sum_{p=0}^{\infty}S_{g}^{p}(\mathbf{Q},\omega), \tag{1}
$$

where the 0-phonon term corresponds to atomic structure and multiphonon terms correspond to atomic motion. Each phonon order in the expansion has contributions from both noninterference (self) and interference (distinct) effects in atomic motion and structure:

$$
S_{g}^{p}(\mathbf{Q},\omega)=S_{g,s}^{p}(\mathbf{Q},\omega)+S_{g,d}^{p}(\mathbf{Q},\omega). \tag{2}
$$

Methods to capture crystal binding effects on the Doppler broadening of neutron resonance reactions depend only on the self-contribution to the TSL (Refs. 2 and 4); however, thermal neutron scattering is dependent on both distinct and self-effects.¹⁶,¹⁹,²⁰ In the case of absorption resonances, the momentum transfer to the compound nucleus is equivalent to the incident neutron energy¹,⁴ whereas in scattering reactions the momentum transfer is a function of both the incident neutron energy and energy transfer.⁵,¹⁶

The double-differential scattering cross section of thermal neutrons defines the probability of a neutron with energy $E$ scattering to $E'$ through a solid angle $\Omega$ and may be estimated in the first Born approximation for a material as¹⁶,¹⁹,²¹

$$
\begin{aligned}
\frac{\partial^{2}\sigma}{\partial E'\partial \Omega}= \\
\sum_{g}\frac{1}{4\pi}\sqrt{\frac{E'}{E}}\left[\sigma_{g,c}S_{g}(\mathbf{Q},\omega)+\sigma_{g,i}S_{g,s}(\mathbf{Q},\omega))\right]. \tag{3}
\end{aligned}
$$

This scattering rate probability is a summation of the double-differential scattering cross section for each atom in the crystallographic unit cell or primitive cell. The scattering probability with the nucleus at each basis position is defined by its bound coherent and incoherent nuclear potential scattering cross sections, denoted as $\sigma_{g,c}$ and $\sigma_{g,i}$, respectively.

At temperatures relevant to the reactor system, vibra- tional incoherence may be assumed, whereby atoms behave as independent oscillators such that distinct effects may be neglected for inelastic scattering (i.e., $p>0$), and

$$
S_{g}(\mathbf{Q}, \omega)=S_{g}^{0}(\mathbf{Q}, \omega)+S_{g, s}^{\prime}(\mathbf{Q}, \omega). \tag{4}
$$

The inelastic part of the TSL represents a two-particle propagator and obeys the detailed balance condition $^{19,21}$

$$
S_{g, s}^{\prime}(\mathbf{Q},-\omega)=\exp \left(-\frac{\omega}{k_{B} T}\right) S_{g, s}^{\prime}(\mathbf{Q}, \omega). \tag{5}
$$

For nontextured polycrystalline materials the momentum transfer dependence of the TSL is averaged over all momentum directions. The corresponding inelastic con- tribution of cubic crystals may be calculated using the phonon expansion as $^{17,19,21}$

$$
S_{g, s}^{\prime}(Q, \omega)=\exp \left(-2 W_{g} Q^{2}\right) \sum_{p=1}^{\infty} \frac{1}{p!}\left(Q^{2}\right)^{p} F_{p}(\omega), \tag{6}
$$

where the Debye-Waller coefficient $W_{g}$ describes the atom's mean square displacement and is calculated from the partial phonon spectra. Each term in the summation represents a scattering process involving the emission and absorption of $p$ phonons, resulting in a net energy loss $(\omega<0)$ or gain $(\omega>0)$ with a corresponding scalar momentum transfer $Q$. The 1-phonon functional $F_{1}$ is the spectral density function of the phonon Green's function,

$$
F_{1}(\omega)=\frac{k_{B} T}{2 M_{g}} \frac{\rho_{g}(\omega)}{\omega\left(1-\exp \left(-\omega / k_{B} T\right)\right)}, \tag{7}
$$

where $M_{g}$ is the nuclear mass and $\rho_{g}(\omega)$ is the partial phonon DOS. Higher-order phonon functionals are eval- uated with a convolution

$$
F_{p}(\omega)=\int_{-\infty}^{\infty} F_{1}\left(\omega^{\prime}\right) F_{p-1}\left(\omega+\omega^{\prime}\right) d \omega^{\prime} \tag{8}
$$

that iteratively incorporates an additional discrete phonon process. As $Q^{2}$ trends toward zero, $S^{\prime}(Q, \omega) / Q^{2}$ approaches the neutron-weighted phonon spectrum

$$
\rho(\omega)=\frac{1}{N} \sum_{g} \frac{\sigma_{g}}{M_{g}} \rho_{g}(\omega) \tag{9}
$$

for a crystal with $N$ basis positions.

Coherent elastic scattering, or Bragg scattering, is dependent on the crystal structure and may be calculated with a generalized treatment as $^{22}$

$$
S_{g}^{0}=\frac{(2 \pi)^{3}}{V \sigma_{g, c}} \sum_{\mathbf{G}} \delta(\mathbf{Q}-\mathbf{G}) \delta(\omega) f^{*}(\mathbf{Q}) f(\mathbf{Q}) \tag{10}
$$

and

$$
f(\mathbf{Q})=\sum_{g} b_{g, c} \exp \left(i \mathbf{Q} \cdot \mathbf{R}_{g}-\mathbf{Q} \cdot \mathbf{W}_{g} \cdot \mathbf{Q}\right), \tag{11}
$$

where
$V$ = volume of the crystal unit cell
$\mathbf{G}$ = reciprocal lattice vectors
$\mathbf{R}_{g}$ = position of an atom within the unit cell.

The coherent scattering length $b_{g, c}$ measures the magni tude of the coherent neutron scattering potential and is related to the scattering cross section via $4 \pi|b_{g, c}|^{2}=\sigma_{g, c}$. For most nuclei this parameter is positive real but is complex or nega- tive in some nuclides. $^{23}$ The Debye-Waller matrix $\mathbf{W}_{g}$ mea sures the correlated motion of the atom, which is isotropic and diagonal for cubic crystals permitting a reduction of the dot product with momentum transfer to a scalar value depen- dent only on $W_{g}$ ($W_{g}=Tr(\mathbf{W}_{g}) / 3$). Bragg scattering defined in Eq. (10) must be averaged over the $4 \pi$ steradian space of the momentum transfer directions for nontextured polycrystalline materials. Incoherent elastic scattering is dependent only on the self-part of $S_{g}^{0}$ and is estimated as

$$
S_{g, s}^{0}=\delta(\omega) \exp \left(-2 W_{g} Q^{2}\right) \tag{12}
$$

for a cubic crystal, which describes an isotropic structure characterized solely by the Debye-Waller coefficient (i.e., mean-square displacement).

### III. COMPUATATIONAL DETAILS

Uranium dioxide in the paramagnetic state has on aver- age a cubic Fluorite crystal structure, illustrated in Fig. 1, with Fm-3m symmetry (space group 225) (Ref. 24). At room temperature the structure is paramagnetic; however, below the Néel temperature of 30.8 K, the $5 f$ magnetic moments on uranium atoms align in a 3-k AFM structure. $^{25,26}$ Nevertheless, previous DFT studies have demonstrated that the ground state electronic structure and phonons may be reasonably estimated using a 1-k AFM

![](./images/812547044764811265_3.jpg)

Fig. 1. Cubic UO₂ unit cell structure. Dark spheres (red) represent oxygen, and light spheres (gray) represent uranium. The black arrows illustrate the alignment of the 5f magnetic moments in the 1-k AFM structure.

structure, shown in Fig. 1, and neglecting the Jahn-Teller distortions of the oxygen sublattice. $^{14,27-29}$

Electronic structure calculations of UO₂ in a 1-k AFM ground state were performed using the VASP DFT code. $^{30,31}$ UO₂ is Mott-Hubbard insulator that is predicted to behave as a metal without the addition of corrections to on-site coulomb repulsion for localized $5f$ electrons $^{13,32}$; therefore, to capture the 2- eV electronic band gap, $^{33,34}$ a Hubbard model was included with an effective on-site coulomb repulsion energy of 4 eV for $5f$ electrons, consistent with previous DFT studies. $^{13-15}$ These spin-polarized simulations utilized projector augmented wave potentials with an exchange correlation functional in the Perdew-Burke-Ernzerhof formulation of the generalized gradient approximation. $^{35-38}$ Additionally, the calculations used an energy cutoff of 600 eV for the plane-wave basis representation of the electron wave function and a $\Gamma$-point centered $6 \times 6 \times 6$ Monkhorst-Pack k-space mesh to uniformly subdivide the first Brillouin zone for reciprocal space integration. $^{39}$ These convergence parameters were found to ensure that the ground state energy and volume were converged to within 5 meV/atom and 0.1%, respectively. The converged ground state lattice parameter was 0.554781 nm, which is in reasonable agreement with the experimental value of $0.547127 \pm 0.0008$ nm at normal temperature and pressure. $^{40}$

Phonon dispersion relations and partial phonon DOSs were generated with the direct AILD method in the PHONON code. $^{41,42}$ Hellmann-Feynman forces were calculated for the AFM ground state in a $2 \times 2 \times 2$ cubic supercell (64 atoms) using a $3 \times 3 \times 3$ k-space mesh. In the paramagnetic phase the time-dependent average of $5f$ magnetic moments is expected to be isotropic; however, local magnetic moments persist above the Néel temperature. To approximate the isotropic spin-polarization behavior in a paramagnetic cubic crystal with Fm-3m symmetry, Hellmann-Feynman forces were averaged for AFM ordered magnetic moments perpendicular and parallel to the orientation of the atomic displacements with 2/3 and 1/3 weighting, respectively. For a displacement along the $a$-axis of the cubic unit cell, this weighting considers the two orthogonal magnetic polarizations along the $b$-axis or $c$-axis and a single parallel polarization along the $a$-axis.

Partial phonon DOSs of oxygen and uranium were processed using the LEAPR module of the NJOY nuclear data processing system $^{43}$ to evaluate the TSL of uranium in UO₂ and oxygen in UO₂ as separate File 7 materials in ENDF-6 format, $^{44}$ labeled U(UO₂) and O(UO₂), respectively. The inelastic contribution to the TSL ($MT=4$) for each element was calculated in the incoherent approximation using the phonon expansion method defined in Eqs. (6), (7), and (8). A phonon order of 100 was used and is sufficient to mitigate the use of the short collision time approximation relative to ENDF/B-VII.1. The coherent elastic contribution ($MT=2$) was generated utilizing a generalized elastic scattering routine implemented in LEAPR, which follows the formulation in Eqs. (10) and (11). This routine removes the atom site approximation traditionally used in LEAPR such that a unique Debye-Waller matrix is used for each element. $^{22}$ Despite the ENDF restriction to the coherent elastic option on $MT=2$, the 0-phonon contribution to the self-part of the TSL may be recovered from normalization of the self-part to unity as a function of energy transfer.

While uranium in commercial reactors is enriched in $^{235}$U, the present TSL evaluations followed the ENDF/B-VII.1 convention and used an isotopic composition for uranium and oxygen of $^{238}$U and $^{16}$O, respectively. The corresponding bound neutron cross section and mass were set to 4.34234 b and 15.995 u for oxygen and 9.3621 b and 238.05 u for uranium, corresponding to ENDF/B-VII.1 incident neutron evaluations. $^{45,46}$ For both isotopes the nuclear scattering cross section is entirely coherent such that double-differential scattering cross sections calculated with Eq. (3) have no contribution from incoherent nuclear scattering for the present evaluations.

## IV. RESULTS AND DISCUSSION

### IV.A. Phonons

Phonon dispersion relations map the permitted phonon energies to pseudomomentum and are a fundamental

NUCLEAR SCIENCE AND ENGINEERING · VOLUME 00 · XXXX 2020

![](./images/812547044764811265_4.jpg)

Fig. 2. Uranium dioxide phonon dispersion relations predicted with AILD in this work compared to INS and other AILD simulation (Pang et al.²⁸). Measurements were performed at the spallation neutron source at Oak Ridge National Laboratory²⁷,²⁸ (ORNL) as well as at Chalk River Nuclear Laboratories¹² (CRNL). The momentum transfer is in reduced lattice units (r.l.u), calculated as $a \cdot Q/\pi$, where $a$ is the primitive cell lattice parameter. The phonon polarization and mode types are abbreviated, respectively, as Longitudinal (L) or Transverse (T), Acoustic (A) or Optical (O). Numerical indices are appended to the phonon labels to distinguish nondegenerate optical modes.

indicator of the physical accuracy of a lattice dynamics model. Predicted $\mathrm{UO}_2$ dispersion relations of the present AILD calculations, as illustrated in Fig. 2, are found to be in overall good agreement with INS experiments. In addition to capturing the LO/TO splitting (LO and TO are defined in Fig. 2) and observed phonon degeneracies, the paramagnetic model captures the observed complex behavior of the TO1, LO1, and acoustic modes in the $\Gamma$-X direction, along which the phonon group velocity of these branches is discontinuous. While the LO2 branch has some deviation from the experimentally observed behavior, this deviation is not anticipated to significantly impact the phonon DOS, which is the fundamental input to the TSL calculation. Furthermore, the paramagnetic model is found to improve the prediction of the phonon dispersion when compared to other AILD calculations,²⁷,²⁸ which were treated as cubic in the 1-k AFM state but used otherwise similar parameters in the calculation of the Hellmann-Feynman forces.

The neutron-weighted phonon DOS of $\mathrm{UO}_2$, as calculated with Eq. (9), is compared in Fig. 3 to experiment as well as the phonon spectrum used in the ENDF/B-VII.1 TSL evaluation developed by Dolling et al.¹² In the Dolling et al. semiempirical lattice dynamics model, the ionic charge and polarization constant of a shell potential were parameterized to minimize the deviation from experimental phonon dispersion relations in a limited number of high-symmetry directions shown in Fig. 3 (Ref. 12). The present ENDF/B-VIII.0 phonon spectrum is in reasonable agreement with experiment and improves upon the prediction of the energy of the smallest acoustic phonon peak as well as the largest optical phonon peak when compared to ENDF/B-VII.1. These deviations are expected to be manifested in changes to the secondary neutron energy spectrum for neutron scattering with uranium and oxygen.

![](./images/812547044764811265_5.jpg)

Fig. 3. Neutron-weighted phonon DOS of $\mathrm{UO}_2$ predicted in the present work for the ENDF/B-VIII.0 TSL evaluation compared to INS measurements at the Oak Ridge National Laboratory (ORNL) spallation neutron source.²⁷,²⁸ The ENDF/B-VII.1 phonon spectrum is also shown.¹² In the inset is the ENDF/B-VIII.0 neutron-weighted phonon spectrum convolved with experimentally observed phonon linewidths.²⁷,²⁸

Both the ENDF/B-VII.1 and ENDF/B-VIII.0 spectra were calculated in the harmonic approximation. Convolution of the ENDF/B-VIII.0 phonon spectra with recent measurement of the phonon linewidth (i.e., lifetime) as a function of energy demonstrates improved agreement with experiment,²⁷,²⁸ suggesting an importance of anharmonicity due to phonon-phonon interactions. However, neglecting these effects in the AILD model is a reasonable first step toward a physically accurate, predictive model for the TSLs of $\mathrm{UO}_2$.

The partial phonon DOSs for uranium and oxygen used in the ENDF/B-VIII.0 evaluation are compared to those of ENDF/B-VII.1 in Fig. 4. Vibrational characteristics of oxygen and uranium are well characterized by acoustic and optical phonons, respectively, as anticipated due to the large mass disparity between these elements. Overall, the partial phonon spectra are similar in the location of energy peaks, considering the previously noted differences in the acoustic and optical phonon peaks. However, there is a substantial relative change between the models with regard to the weighting of acoustic and optical modes for oxygen and uranium. The present paramagnetic model has a decreased availability of acoustic modes in the oxygen partial DOS and a decrease

![](./images/812547044764811265_6.jpg)

Fig. 4. Partial phonon DOS for uranium and oxygen in UO₂ predicted with the present paramagnetic AILD model used for the ENDF/B-VIII.0 TSL evaluation compared to the classical lattice dynamics model used in the ENDF/B-VII.1 TSL evaluation.

availability of optical modes in the uranium partial DOS compared to the Dolling et al. model.

This bias in the partial phonon DOS elicits a significant change in the Debye-Waller coefficients as a function of temperature, as illustrated in Fig. 5. The respective shift in uranium and oxygen in the paramagnetic model to more acoustic and optical in character results in a significantly improved prediction of the Debye-Waller coefficient, despite the direct use of the phonon dispersion relations as fit data in the generation of the Dolling et al. model. As indicated in Eqs. (10), (11), and (12), the Debye-Waller coefficient influences coherent and incoherent elastic scattering, the former of which is of particular importance to potential scattering of thermal neutrons explored in the present work where there is no contribution from incoherent scattering based on the ²³⁸U and ¹⁶O isotopic composition. Recoil in resonance reactions with no phonon emission, which is an important contribution to Doppler broadening⁴⁷ of low-energy resonances, is also highly sensitive to this parameter for incident neutrons up to energies of a similar order of magnitude (i.e., $E \approx 1/2W_{\text{g}}$).

![](./images/812547044764811265_7.jpg)

Fig. 5. Debye-Waller coefficient for uranium and oxygen in UO₂ predicted with the present AILD model used for the ENDF/B-VIII.0 TSL evaluation and the classical lattice dynamics model used in the ENDF/B-VII.1 TSL evaluation compared to INS measurements.¹²

## IV.B. Thermal Scattering Law

The inelastic contribution to the $S'(Q,\omega)$ for the ENDF/ B-VIII.0 U(UO₂) and O(UO₂) evaluations is illustrated in Figs. 6 and 7, respectively. As anticipated from the partial phonon DOS, neutron scattering with oxygen results in greater energy transfer than uranium. Because of the lower oxygen-to-neutron mass ratio, neutrons scattering with oxygen results in significantly lower momentum transfers than uranium. At 296 K, phonon emission as a consequence of neutron interactions, associated with downscattering, is favored for both elements. For higher temperatures the probability of phonon emission and absorption trend toward equalization at low momentum transfers, corresponding to increased competition between upscattering and downscattering.

The spectrum of energy transfer for the uranium $S'(Q,\omega)$ at momentum transfers of less than 5 eV is highly structured for interactions involving 1-phonon and 2-phonon emission, with peaks in the TSL at integer multiples of the 0.01- and 0.02-eV phonon peaks, but is relatively featureless for energy transfer greater than 0.05 eV. An analogous trend is present for the oxygen $S'(Q,\omega)$ for momentum transfer less than 1 eV and energy transfer up to 0.08 eV corresponding to 1-phonon emission, which is a similar energy range to uranium. For both elements, 1-phonon emission is the dominant contribution for momentum transfers in this range. Consequently, secondary neutron energies resulting from scattering both for thermal and epithermal neutrons will be sensitive to the phonon spectra at these low momentum transfers.

For momentum transfers between 10 and 100 eV, the phonon structure in the U(UO₂) $S'(Q,\omega)$ has subsided, and the behavior transitions to that of a free gas. Nuclear recoil momentum of $(n,f)$ and $(n,\gamma)$ reactions is equivalent to the incident neutron energy. Additionally, the average recoil momentum for scattering with heavy nuclei is nearly twice the incident neutron momentum for a free gas. In this epithermal energy range, the momentum transfer is much larger than the momentum Debye-Waller coefficient. Correspondingly, the 0-phonon contribution to both the U(UO₂) and O(UO₂) TSL diminishes with increasing incident energy, such that neutron interactions result only in phonon emission or absorption (i.e., inelastic processes). As an example, the

NUCLEAR SCIENCE AND ENGINEERING · VOLUME 00 · XXXX 2020

![](./images/812547044764811265_8.jpg)

Fig. 6. ENDF/B-VIII.0 TSL evaluation for U(UO₂) at (a)
296 K and (b) 1200 K. The mesh overlay illustrates the
density of energy and momentum transfers used in the
evaluation, which has the resolution of the phonon DOS
for energy transfer to 1-phonon order in the phonon
expansion.

![](./images/812547044764811265_9.jpg)

Fig. 7. ENDF/B-VIII.0 TSL evaluation for O(UO₂) at (a)
296 K and (b) 1200 K. The mesh overlay illustrates the
density of energy and momentum transfers used in the eva-
luation, which has the resolution of the phonon DOS for
energy transfer to 1-phonon order in the phonon expansion.

probability of no phonon emission for neutron interactions at
the 6.6742-eV $^{238}$U resonance energy$^{46}$ is less than $10^{-4}$ at
296 K and less than $10^{-16}$ at 1200 K.

In a comparative study of the ENDF/B-VIII.0 and
ENDF/B-VII.1 evaluations, Sorrell and Hawari demon-
strate an impact of the differences in the evaluations on
the resonance line shape of the 6.6742-eV $^{238}$U $(n,\gamma)$ reso-
nance, with deviations up to 50 b at 293.7 K and as large as
200 b at a cryogenic temperature of 23.6 K (Ref. 6). A free-
gas treatment for Doppler broadening of this resonance was
found to be inconsistent with neutron transmission
measurements.$^{6,7}$ In contrast, Doppler broadening with the
U(UO₂) ENDF/B-VIII.0 model for $S_{s}(Q,\omega)$ was in good
agreement with these measurements at both temperatures,$^{6,7}$
thereby demonstrating the importance of crystal binding for
both scattering and $(n,x)$ reactions for incident neutrons
near this energy, where $x$ is a secondary particle (e.g., $\gamma$, $\alpha$,
fission fragments).

At the maximum tabulated momentum transfer of 20 eV
in the ENDF/B-VIII.0 evaluation, the uranium $S'(Q,\omega)$ as
a function of energy transfer differs from the free-gas TSL by
less than 0.5% of the maximum probability at 1200 K and
less than 2.5% at 296 K. Consequently, neutron scattering
and resonance reactions with uranium are expected to be
increasingly insensitive to crystal binding effects for incident
neutrons in the 10 to 100 eV epithermal energy range at
elevated temperatures, such that the recoil of the nuclei may
be approximated as a free gas above this range. For interac-
tions with oxygen, crystal binding is anticipated to influence
neutron interactions up to an order-of-magnitude higher ener-
gies as it also transitions to free-gas behavior.

The physics of the TSL may be examined through the
double-differential scattering cross section, which is directly

![](./images/812547044764811265_10.jpg)

Fig. 8. Double-differential scattering cross section of UO₂ at an incident energy of 0.332 eV: (a) and (b) compare the inelastic contribution for ENDF/B-VIII.0 to TOF experiments at the Rensselaer Polytechnic Institute (RPI) LINAC at two different scattering angles,⁴⁸ and (c) compares the inelastic differential cross sections for U(UO₂) and O(UO₂) corresponding to the ENDF/ B-VIII.0 and ENDF/B-VII.1 TSL evaluations. For the selected neutron energy and scattering angles, inelastic scattering is dominant such that elastic scattering presents only a small contribution to the overall experimental signal as a quasi-elastic peak.

measureable and is proportional to $S'(Q, \omega)$ for inelastic scattering. The double-differential scattering cross sections of UO₂ for the ENDF/B-VIII.0 and ENDF/B-VII.1 evaluations are compared in Fig. 8 to assess the impact of the revised phonon model used in the ENDF/B-VIII.0 TSL evaluation. These double-differential cross sections were generated from Eq. (3) using the partial phonon spectra for each ENDF version as an input to the FLASSH code,²² which has the native capability to directly generate the double-differential cross section as a function of scattering angle and secondary energy rather than the energy transfer and momentum trans- fer space of ENDF and NJOY.

The predicted double-differential cross sections for the ENDF/B-VIII.0 and ENDF/B-VII.1 evaluations have similar overall behavior and are in reasonable agreement with time-of -flight (TOF) neutron measurements,⁴⁸ as illustrated for select angles of $5\pi/6$ and $\pi/3$ at 0.332 eV in Figs. 8a and 8b. Experimental resolution (e.g., neutron chopper, detector reso- lution) may cause features of the TOF double-differential cross section to be less pronounced relative to either ENDF evaluation, while a quasi-elastic peak near the incident energy —common for TOF measurements—appears as a broad, smooth central peak at low-energy transfer suppressing low- energy structure in contrast to the elastic delta function pre- dicted by theory. Relative to ENDF/B-VII.1, the ENDF/ B-VIII.0 uranium evaluation has more pronounced structural features arising from narrower peaks in the phonon spectra (see Fig. 4) and predicts an increased likelihood of larger energy downscattering events. Furthermore, the elemental contributions to the total scattering rate differ as a result of the changes in the partial phonon DOS between the evalua- tions, as illustrated in Fig. 8c. For oxygen the decreased availability of acoustic modes in ENDF/B-VIII.0 results in a differential cross section with an increased probability of lower secondary neutron energies (i.e., larger energy transfers). Conversely, ENDF/B-VIII.0 uranium has an increased probability of secondary neutron energies within 0.02 eV of the incident energy that coincides with the range of 1-phonon emission. Nevertheless, the impact on scattering due to changes in the partial DOS is diminished for uranium relative to oxygen.

The impact of the partial DOS on scattering is further exemplified in the integrated thermal neutron scattering cross section. As illustrated in Fig. 9, the ENDF/B-VIII.0 inelastic scattering cross section is less than that of ENDF/B-VII.1 for neutron energies greater than 0.01 eV at all tabulated tempera- tures, although both models yield a total scattering cross section with consistent behavior and reasonable agreement with experiment within the available energy range. The indi- vidual contributions to the UO₂ inelastic scattering cross section from uranium and oxygen, shown in Fig. 10, clearly demonstrate that the primary contributor to differences in the predicted inelastic thermal neutron scattering behavior of this material is due to changes in the partial phonon DOS of oxygen.

The relative difference between the ENDF/B-VIII.0 and ENDF/B-VII.1 inelastic scattering cross sections of O(UO₂), defined as

$$
\Delta=\frac{\sigma_{\mathrm{ENDF} / \mathrm{B}-\mathrm{VIII}.0}(E)-\sigma_{\mathrm{ENDF} / \mathrm{B}-\mathrm{VII}.1}(E)}{\sqrt{\sigma_{\mathrm{ENDF} / \mathrm{B}-\mathrm{VIII}.0}(E) \cdot \sigma_{\mathrm{ENDF} / \mathrm{B}-\mathrm{VII}.1}(E)}},\tag{13}
$$

is as much as 22% at 296 K and 10% at 1200 K, with the maximum occurring near 0.03 eV. The magnitude of this deviation may be attributed to the sensitivity of the acoustic modes to the Bose-Einstein occupation factor for phonons at engineering temperatures compared to the optical phonon energy range of this material. In this case, the decrease in available low-energy phonons for oxygen predicted in the ENDF/B-VIII.0 model results in a disproportionately large

![](./images/812547044764811265_11.jpg)

Fig. 9. Thermal neutron scattering cross section of $\text{UO}_2$ at 296 K compared to transmission measurements by Aktiebolaget Atomenergi$^{49}$ (AE). The inelastic contribution for the ENDF/B-VIII.0 and ENDF/B-VII.1 evaluations is compared for multiple temperatures between 296 K and 1200 K. The elastic contribution is shown for 296 K.

decrease in the probability of scattering with these modes—also observed in Fig. 8c—causing an appreciable decrease in the inelastic scattering cross section. The small positive bias in the cross sections within the $1/\sqrt{E}$ region below $10^{-3}$ eV is due to the use of larger $^{16}\text{O}$ cross section in the ENDF/B-VIII.0 TSL evaluation (4.34234 b) compared to that of ENDF/B-VII.1 (4.2356 b).

While the difference in the inelastic scattering cross sections contributes to the observed deviation in the total scattering cross section, additional contributions arise from the elastic scattering cross section. In $\text{UO}_2$ the interference effects for Bragg scattering (i.e., elastic scattering) are only U-U or U-O in nature, $^{49}$ such that the elastic scattering cross section is dependent on the Debye-Waller coefficient of uranium for all incident energies greater than the Bragg edge (0.002 eV). Consequently, the increased Debye-Waller coefficient of uranium for ENDF/B-VIII.0 (see Fig. 5) results in a lower energy onset to the $1/E$ decrease in the elastic scattering cross section, exemplified in Fig. 9. The combined effect of the reduced elastic scattering due to uranium and inelastic scattering due to oxygen is responsible for the lower total scattering cross section of ENDF/B-VIII.0 relative to that of ENDF/B-VII.1.

## V. CONCLUSION

A phonon model for $\text{UO}_2$ in the paramagnetic phase has been developed using AILD techniques. Subsequently, the ab initio phonon spectrum was used to generate $\text{U(UO}_2)$ and $\text{O(UO}_2)$ TSLs for inclusion in ENDF/B-VIII.0. The ab initio phonon spectra better capture the vibrational behavior of both uranium and oxygen compared with the classical lattice dynamics models previously used in the generation of ENDF TSLs for $\text{UO}_2$, as indicated by agreement with measurements of mean-square displacement. Furthermore, the predicted double-differential cross section as well as integrated scattering and Doppler-broadened resonance cross sections is consistent with experiment, supporting validation of the evaluations.

![](./images/812547044764811265_12.jpg)

Fig. 10. Inelastic thermal neutron scattering cross section for (a) $\text{U(UO}_2)$ and (b) $\text{O(UO}_2)$ at 296 K and 1200 K. The inset plot quantifies the bias between the ENDF/ B-VIII.0 and ENDF/B-VII.1 $\text{O(UO}_2)$ cross sections for these evaluations, trending toward a smaller ENDF/ B-VIII.0 cross section.

Crystal binding effects in $\text{U(UO}_2)$ are found to continue to influence neutron interactions for energies greater than 10 eV and in $\text{O(UO}_2)$ for energies beyond the current evaluation. Although the present evaluations are generated for $^{238}\text{U}$ and $^{16}\text{O}$, the ab initio model may be used to evaluate other isotopic compositions. Nonetheless, the relatively small mass differences between uranium isotopes is expected to have minimal impact on the $\text{U(UO}_2)$ partial phonon DOS; therefore, the self-part of the TSL for any

uranium isotope may be approximated by the ENDF/ B-VIII.0 U(UO₂) evaluation for use in resonance broad- ening or inelastic scattering, following the substitution of the appropriate nuclear scattering cross section for the ura- nium isotope of interest.

The distribution of acoustic and optical phonons for oxygen and uranium in the present evaluation results in reduced inelastic, elastic, and total thermal neutron scattering cross sections when compared to ENDF/B-VII.1. Moreover, the greater energy transfer from scattering with oxygen indicates that the double- differential cross section for the ENDF/B-VIII.0 eva- luation may impact the prediction of neutron thermali- zation in fission systems where moderation in this material is significant. In light water reactors, where moderation in H₂O is dominant, the difference in the evaluations is likely to yield only a minor impact on the thermalization. The refined physics in the present eva- luation is anticipated to most significantly impact the prediction of the effect of Doppler broadening on epithermal resonance reaction rates for uranium iso- topes and the associated resonance integrals that deter- mine resonance escape probabilities. Such resonance effects are important for both criticality and reactor physics analyses of steady-state operation as well as the prompt transient response for thermal and epither- mal reactor systems.

## Acknowledgments
This work was supported by funding from the U.S. Department of Energy's Nuclear Energy University Program, the Nuclear Criticality Safety Program, and the Naval Nuclear Propulsion Program. The submitted manuscript has been authored by contractors of the U.S. Government under contract No. DOE-89233018CNR000004.

The data that support the findings of this work include ENDF evaluations, which are publicly available through the U.S. National Nuclear Data Center (NNDC) using the ENDF web-based retrieval tool: https://www.nndc.bnl.gov/ exfor/endf00.jsp. The ENDF/B-VIII.0 TSL evaluation and input files may also be downloaded from the NNDC within the TSL sublibrary at https://www.nndc.bnl.gov/endf/b8.0/ download.html.

## ORCID
J. L. Wormald http://orcid.org/0000-0001-7727-5967
A. I. Hawari http://orcid.org/0000-0001-8255-7491
M. L. Zerkle http://orcid.org/0000-0001-8627-4712

![](./images/812547044764811265_13.jpg)

## References
1. W. E. LAMB, "Capture of Neutrons by Atoms in a Crystal," *Phys. Rev.*, **55**, 2, 190 (1939); https://doi.org/10.1103/PhysRev.55.190.

2. M. S. NELKIN and D. E. PARKS, "Effects of Chemical Binding on Nuclear Recoil," *Phys. Rev.*, **119**, 3, 1060 (1960); https://doi.org/10.1103/PhysRev.119.1060.

3. B. A. BERNABEI, "The Effects of Crystalline Binding on the Doppler Broadening of a Neutron Resonance," BNL-860 (T-344), Brookhaven National Laboratory (1964).

4. G. M. BORGONOVI et al., "Crystal-Binding Effects on Doppler Broadening of Neutron Absorption Resonances," *Phys. Rev. C*, **1**, 6, 2054 (1970); https://doi.org/10.1103/PhysRevC.1.2054.

5. A. KUWAIFI and G. SUMMERFIELD, "Chemical Binding Effects in Resonance-Potential Interference Scattering for Harmonic Crystals," *Ann. Nucl. Energy*, **18**, 1, 19 (1991); https://doi.org/10.1016/0306-4549(91)90033-T.

6. N. C. SORRELL and A. I. HAWARI, "Impact of the Dynamic Structure Factor on Doppler Broadening of ²³⁸U in UO₂," *Trans. Am. Nucl. Soc.*, **119**, 720 (2018).

7. N. C. SORRELL and A. I. HAWARI, "Structure-Dependent Doppler Broadening Using a Generalized Thermal Scattering Law," *Proc. PHYSOR 2020*, Cambridge, United Kingdom, American Nuclear Society (unpublished).

8. G. NOGUERE, P. MALDONADO, and C. DE SAINT JEAN, "Doppler Broadening of Neutron-Induced Resonances Using Ab Initio Phonon Spectrum," *Eur. Phys. J. Plus*, **133**, 5 (2018); https://doi.org/10.1140/epjp/i2018-12009-y.

9. A. MEISTER et al., "Measurement to Investigate the Doppler- Broadening of ²³⁸U Neutron Resonances," GE/R/ND/01/96, Institute for Reference Materials and Measurements (1996).

10. A. MEISTER et al., "Experimental Study of the Doppler Broadening of Neutron Resonances at GELINA," *Proc. Int. Conf. Nuclear Data for Science and Technology*, Trieste, Italy, 1997, Italian Physical Society (1997).

11. D. A. BROWN et al., "ENDF/B-VIII.0: The 8ᵗʰ Major Release of the Nuclear Reaction Data Library with CIELO-Project Cross Sections, New Standards and Thermal Scattering Data," *Nucl. Data Sheets*, **148**, 1, 1 (2018); https://doi.org/10.1016/j.nds.2018.02.001.

12. G. DOLLING, R. A. COWLEY, and A. D. B. WOODS, "The Crystal Dynamics of Uranium Dioxide," *Can. J. Phys.*, **43**, 8, 1397 (1965); https://doi.org/10.1139/p65-135.

13. S. L. DUDAREV, D. N. MANH, and A. P. SUTTON, "Effect of Mott-Hubbard Correlations on the Electronic Structure and Structural Stability of Uranium Dioxide," *Philos. Mag. B*, **75**, 5, 613 (1997); https://doi.org/10.1080/13642819708202343.

NUCLEAR SCIENCE AND ENGINEERING · VOLUME 00 · XXXX 2020

14. B. DORADO et al., "DFT + U Calculations of the Ground State and Metastable States of Uranium Dioxide," *Phys. Rev. B*, **79**, 23, 235125 (2009); https://doi.org/10.1103/PhysRevB.79.235125.

15. B. DORADO et al., "Stability of Oxygen Point Defects in $\mathrm{UO}_{2}$ by First-Principles DFT + $U$ Calculations: Occupation Matrix Control and Jahn-Teller Distortion," *Phys. Rev. B*, **82**, 3, 35114 (2010); https://doi.org/10.1103/PhysRevB.82.035114.

16. L. VANHOVE, "Correlations in Space and Time and Born Approximation Scattering in Systems of Interacting Particles," *Phys. Rev.*, **95**, 1, 249 (1954); https://doi.org/10.1103/PhysRev.95.249.

17. G. BAYM, "Thermodynamic Green's Function Method in Neutron Scattering by Crystals," *Phys. Rev.*, **121**, 3, 741 (1961); https://doi.org/10.1103/PhysRev.121.741.

18. S. DONIACH and E. H. SONDHEIMER, *Green's Functions for Solid State Physicists*, Imperial College Press, London, United Kingdom (2008).

19. G. L. SQUIRES, *Introduction to the Theory of Thermal Neutron Scattering*, Dover Publications Inc., Mineola, New York (1996).

20. A. I. HAWARI, "Modern Techniques for Inelastic Thermal Neutron Scattering Analysis," *Nucl. Data Sheets*, **118**, 172 (2014); https://doi.org/10.1016/j.nds.2014.04.029.

21. R. E. MacFARLANE, "New Thermal Neutrons Scattering Files for ENDF/B-VI, Release 2," LA-12639-MS, Los Alamos National Laboratory (1994).

22. Y. ZHU and A. I. HAWARI, "Full Law Analysis Scattering System Hub (FLASH)," *Trans. Am. Nucl. Soc.*, **116**, 705 (2017).

23. V. F. SEARS, "Neutron Scattering Lengths and Cross Sections," *Neutron News*, **3**, 29 (1992); https://doi.org/10.1080/10448639208218770.

24. L. DESGRANGES et al., "What Is the Actual Local Crystalline Structure of Uranium Dioxide, $\mathrm{UO}_{2}$? A New Perspective for the Most Used Nuclear Fuel," *Inorg. Chem.*, **56**, 1, 321 (2017); https://doi.org/10.1021/acs.inorgchem.6b02111.

25. J. FABER and G. H. LANDER, "Neutron Diffraction Study of $\mathrm{UO}_{2}$: Antiferromagnetic State," *Phys. Rev. B*, **14**, 3, 1151 (1976); https://doi.org/10.1103/PhysRevB.14.1151.

26. P. SANTINI et al., "Multipolar Interactions in *F*-Electron Systems: The Paradigm of Actinide Dioxides," *Rev. Mod. Phys.*, **81**, 2, 807 (2009); https://doi.org/10.1103/RevModPhys.81.807.

27. J. W. L. PANG et al., "Phonon Lifetime Investigation of Anharmonicity and Thermal Conductivity of $\mathrm{UO}_{2}$ by Neutron Scattering and Theory," *Phys. Rev. Lett.*, **110**, *15*, 157401 (2013); https://doi.org/10.1103/PhysRevLett.110.157401.

28. J. W. L. PANG et al., "Phonon Density of States and Anharmonicity of $\mathrm{UO}_{2}$," *Phys. Rev. B*, **89**, 11, 115132 (2014); https://doi.org/10.1103/PhysRevB.89.115132.

29. J. L. WORMALD and A. I. HAWARI, "*Ab Initio* Generation of the Thermal Neutron Scattering Law for Uranium Dioxide," *Trans. Am. Nucl. Soc.*, **115**, 1156 (2018).

30. G. KRESSE and J. FURTHMÜLLER, "Efficient Interative Schemes for *Ab Initio* Total-Energy Calculations Using a Plane-Wave Basis Set," *Phys. Rev. B*, **54**, 16, 11169 (1996); https://doi.org/10.1103/PhysRevB.54.11169.

31. G. KRESSE and J. FURTHMÜLLER, "Efficiency of Ab-Initio Total Energy Calculations for Metals and Semiconductors Using a Plane-Wave Basis Set," *Comput. Mat. Sci.*, **6**, 1, 15 (1996); https://doi.org/10.1016/0927-0256(96)00008-0.

32. F. JOLLET et al., "The Electronic Structure of Uranium Dioxide: An Oxygen K-Edge X-Ray Absorption Study," *J. Phys.: Condens. Matter*, **9**, 43, 9393 (1997); https://doi.org/10.1088/0953-8984/9/43/022.

33. J. SCHOENES, "Optical Properties and Electronic Structure of $\mathrm{UO}_{2}$," *J. Appl. Phys.*, **49**, 3, 1463 (1978); https://doi.org/10.1103/PhysRevB.1.324978.

34. P. RUELLO et al., "Thermal Variation of the Optical Absorption of $\mathrm{UO}_{2}$: Determination of the Small Polaron Self-Energy," *J. Nucl. Mater.*, **328**, 1, 46 (2004); https://doi.org/10.1016/j.jnucmat.2004.03.002.

35. G. KRESSE and D. JOUBERT, "From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method," *Phys. Rev. B*, **59**, 3, 1758 (1999); https://doi.org/10.1103/PhysRevB.59.1758.

36. J. P. PERDEW, K. BURKE, and M. ERNZERHOF, "Generalized Gradient Approximation Made Simple," *Phys. Rev. Lett.*, **77**, 18, 3865 (1996); https://doi.org/10.1103/PhysRevLett.77.3865.

37. J. P. PERDEW, K. BURKE, and M. ERNZERHOF, "Erratum: Generalized Gradient Approximation Made Simple," *Phys. Rev. Lett.*, **78**, 7, 1396 (1996); https://doi.org/10.1103/PhysRevLett.78.1396.

38. P. E. BLÖCHL, "Projector Augmented-Wave Method," *Phys. Rev. B*, **50**, 24, 17953 (1994); https://doi.org/10.1103/PhysRevB.50.17953.

39. H. J. MONKHORST and J. D. PACK, "Special Points for Brillouin-Zone Integrations," *Phys. Rev. B*, **13**, 12, 5188 (1976); https://doi.org/10.1103/PhysRevB.13.5188.

40. G. LEINDERS et al., "Accurate Lattice Parameter Measurements of Stoichiometric Uranium Dioxide," *J. Nucl. Mater.*, **459**, 135 (2015); https://doi.org/10.1016/j.jnucmat.2015.01.029.

41. K. PARLINSKI, Z. Q. LI, and Y. KAWAZOE, "First-Principles Determination of the Soft Mode in Cubic $\mathrm{ZrO}_{2}$," *Phys. Rev. Lett.*, **78**, 21, 4063 (1997); https://doi.org/10.1103/PhysRevLett.78.4063.

42. K. PARLINSKI, "Calculation of Phonon Dispersion Curves by the Direct Method," *AIP Conf. Proc.*, **479**, 1, 121 (1999); https://doi.org/10.1063/1.59457.

43. R. E. MacFARLANE and D. W. MUIR, "The NJOY Nuclear Data Processing System, Version 91," LA-12740-MS, Los Alamos National Laboratory (1994).

44. A. TRKOV and D. A. BROWN, "ENDF-6 Formats Manual: Data Formats and Procedures for the Evaluated Nuclear Data Files," BNL-203218-2018-INRE, Brookhaven National Laboratory (2018).

45. G. M. HALE et al., Mat 825 ENDF/B-VII.1, Los Alamos National Laboratory (2006).

46. M. B. CHADWICK et al., Mat 9237 ENDF/B-VII.1, Los Alamos National Laboratory (2006).

47. C. D. BOWMAN and R. A. SCHRACK, “Effects of Phonon Transfer on Near-Thermal Neutron Fission Cross Sections,” *Phys. Rev. C*, **17**, 2, 654 (1978); https://doi.org/10.1103/PhysRevC.17.654.

48. S. N. PUROHIT et al., “Inelastic Neutron Scattering in Metal Hydrides, UC and $\text{UO}_2$, and Applications of the Scattering Law,” *Neutron Thermalization and Reactor Spectra*, Vol. I, International Atomic Energy Agency, Ann Arbor, Michigan (1967).

49. S. F. BESHAI, “Total Cross-Sections of U, $\text{UO}_2$ and $\text{ThO}_2$ for Thermal and Subthermal Neutrons,” AE-222, Aktibolaget Atomenergi (1966).
