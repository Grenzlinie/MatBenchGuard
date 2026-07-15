# Influence of the aggregate state on band structure and optical properties of C60 computed with different methods

Amrita Pal, Saeid Arabnejad, Koichi Yamashita, and Sergei Manzhos

Citation: *The Journal of Chemical Physics* **148**, 204301 (2018); doi: 10.1063/1.5028329

View online: https://doi.org/10.1063/1.5028329

View Table of Contents: http://aip.scitation.org/toc/jcp/148/20

Published by the American Institute of Physics

---

## Articles you may be interested in

[First-order symmetry-adapted perturbation theory for multiplet splittings](https://aip.scitation.org/doi/10.1063/1.5021891)
*The Journal of Chemical Physics* **148**, 164110 (2018); 10.1063/1.5021891

[A general range-separated double-hybrid density-functional theory](https://aip.scitation.org/doi/10.1063/1.5025561)
*The Journal of Chemical Physics* **148**, 164105 (2018); 10.1063/1.5025561

[Communication: Biological applications of coupled-cluster frozen-density embedding](https://aip.scitation.org/doi/10.1063/1.5026651)
*The Journal of Chemical Physics* **148**, 141101 (2018); 10.1063/1.5026651

[Low-lying excited states by constrained DFT](https://aip.scitation.org/doi/10.1063/1.5018615)
*The Journal of Chemical Physics* **148**, 144103 (2018); 10.1063/1.5018615

[Publisher's Note: "Multiconfiguration pair-density functional theory investigation of the electronic spectrum of MnO₄⁻" [J. Chem. Phys. 148, 124305 (2018)]](https://aip.scitation.org/doi/10.1063/1.5036528)
*The Journal of Chemical Physics* **148**, 169901 (2018); 10.1063/1.5036528

[Reference dependence of the two-determinant coupled-cluster method for triplet and open-shell singlet states of biradical molecules](https://aip.scitation.org/doi/10.1063/1.5025170)
*The Journal of Chemical Physics* **148**, 164102 (2018); 10.1063/1.5025170

---

![](./images/813034716172124161_1.jpg)

THE JOURNAL OF CHEMICAL PHYSICS 148, 204301 (2018)
![](./images/813034716172124161_2.jpg)

# Influence of the aggregate state on band structure and optical properties of C60 computed with different methods

Amrita Pal, $^{1}$ Saeid Arabnejad, $^{2}$ Koichi Yamashita, $^{2}$ and Sergei Manzhos $^{1,a)}$

$^{1}$ Department of Mechanical Engineering, National University of Singapore, Block EA #07-08,
9 Engineering Drive 1, Singapore 117576, Singapore
$^{2}$ Department of Chemical System Engineering, School of Engineering, University of Tokyo, 7-3-1,
Hongo, Bunkyo-ku, Tokyo 113-8656, Japan

(Received 9 March 2018; accepted 4 May 2018; published online 22 May 2018)

C60 and C60 based molecules are efficient acceptors and electron transport layers for planar perovskite solar cells. While properties of these *molecules* are well studied by *ab initio* methods, those of *solid* C60, specifically its optical absorption properties, are not. We present a combined density functional theory–Density Functional Tight Binding (DFTB) study of the effect of solid state packing on the band structure and optical absorption of C60. The valence and conduction band edge energies of solid C60 differ on the order of 0.1 eV from single molecule frontier orbital energies. We show that calculations of optical properties using linear response time dependent-DFT(B) or the imaginary part of the dielectric constant (dipole approximation) can result in unrealistically large redshifts in the presence of intermolecular interactions compared to available experimental data. We show that optical spectra computed from the frequency-dependent real polarizability can better reproduce the effect of C60 aggregation on optical absorption, specifically with a generalized gradient approximation functional, and may be more suited to study effects of molecular aggregation. *Published by AIP Publishing.* https://doi.org/10.1063/1.5028329

## I. INTRODUCTION

C60 based materials are widely used in photoelectrochemical/solar cells such as organic solar cells $^{1,2}$ and planar inverted perovskite solar cells. $^{3,4}$ While in bulk heterojunction cells, addends are used to control the solubility and the morphology of the heterojunction (PC60BM is the most widely used example), $^{5,6}$ in planar perovskite cells, bare C60 (and C70) performs well. $^{7}$ Planar perovskite cells have now achieved conversion efficiencies about $20\%^{8}$ and are most promising given their advantages in fabrication. $^{9,10}$ Therefore, characterization of fullerene layers, both experimental and theoretical/computational, is highly technologically relevant. The main role of these materials is to ensure charge separation at the interface with the donor and electron transport to the electrodes. Their electron affinity/conduction band minimum (CBM) are critical determinants of the efficiency of charge separation. To avoid voltage losses, one strives to achieve a minimal offset from the conduction band minimum (or LUMO, lowest unoccupied molecular orbital, of the corresponding molecules) of the donor at which charge separation is still efficient. Therefore, the precise position of the CBM is important.

The CBM is determined by the energy of the LUMO of the fullerene molecule (conversely, the VBM, valence band maximum, is determined by the energy of the HOMO, highest occupied molecular orbital) and by its interaction with the environment, which is made mostly of other fullerene molecules in the case of solid layers. Single-molecule HOMO/LUMO estimates can be quite accurate both by experiments (e.g., by cyclic voltammetry $^{11}$ in solution) and by modeling as highly accurate *ab initio* methods (using hybrid functionals or even wavefunction-based methods with large basis sets) are feasible for single molecules. In solids, characterization is more difficult. For example, the onset points of the PESA (photoelectron spectroscopy in the air $^{12}$ ) signal (for HOMO analysis) have rather wide tolerances. $^{13,14}$ Optical bandgaps (often used for LUMO estimates $^{15,16}$ of organic molecules) are also not effective as absorption spectra of fullerenes are not dominated by HOMO$\rightarrow$LUMO transitions as they are, e.g., in most organic dyes. $^{17}$ Highly accurate computational methods are typically also unfeasible in solids. It is therefore important to have computed estimates of the change in LUMO/CBM and HOMO/VBM due to the aggregate state to gauge their effect on band alignment in solar cells. While C60 and C70 molecules have been characterized by *ab initio* methods in multiple studies, $^{17,18}$ this has not been the case for solids, specifically as far as optical properties are concerned, with only a handful of studies available. $^{19,20}$

C60 does not possess significant visible absorption but can absorb some of the solar flux in the blue and UV parts of the spectrum. $^{21-23}$ This can be of importance especially when illumination is from the fullerene layer side, i.e., in non-inverted configurations. Other fullerene derivatives do have significant solar absorption (most notably those based on C70) $^{24}$ and can help generate additional photocurrent. It is therefore important to be able to compute optical properties of fullerenes, and that, in the aggregate state. Absorption properties of C60 and other fullerene derivatives in molecular

a)Author to whom correspondence should be addressed: mpemanzh@nus.edu.sg

0021-9606/2018/148(20)/204301/9/$30.00
148, 204301-1
Published by AIP Publishing.

form (solution) have been reported $^{17,23}$ as well as approximate calculations in molecular solids. $^{19,20}$ How much does the aggregate state affect the shape and the intensity of the absorption spectrum? This is not trivial to answer for any molecular solid; specifically for fullerenes, this question is further complicated by the fact that the absorption spectrum is not dominated by HOMO $\rightarrow$ LUMO transitions but involves contributions from transitions between many orbitals, necessitating the inclusion of *hundreds* of states even in a single molecule calculation and proportionally more for molecular aggregates. $^{17}$ Such calculations would therefore be costly with TD-DFT (Time-Dependent Density Functional Theory). $^{25,26}$ Furthermore, TD-DFT is very sensitive to the exact shape of orbitals which contribute to the transitions and to errors in them. $^{27}$

In this paper, we present a combined DFT-DFTB (Density Functional Tight Binding) $^{28}$ study of the effect of solid state packing on the band structure and optical absorption of C60. We use DFT/TD-DFT as well as DFTB and its time-dependent extension, TD-DFTB, $^{29}$ to compute C60 in crystalline form and to compute its optical properties. DFTB is an approximate DFT method that is about three orders of magnitude faster than DFT and is therefore attractive for molecular solid calculations due to its ability to treat large system sizes (such as C60 clusters considered here) and for optical property calculations due to the feasibility of considering large numbers of transitions in TD-DFTB, which is especially important for fullerenes. Is the quality of the orbitals computed with DFT(B) for aggregated fullerene molecules sufficient to produce a reasonable absorption spectrum?

We show that absorption spectra computed with TD-DFT (using different functionals) and TD-DFTB show a redshift in C60 molecular clusters, which in the case of DFTB and DFT with a GGA (generalized gradient approximation) functional is unrealistically large. This is on top of TD-DFT's sensitivity to the approximation of the exchange and correlation functional which results, e.g., in underestimated excitation energies with GGA. This follows directly from linear response TD-DFT's strong dependence on orbital energies and shapes, suggesting that the quality of the orbitals, which are delocalized by DFT (and DFTB) over more than one molecular unit, is insufficient to produce a quality spectrum with TD-DFT.

In solid state calculations, the dipole approximation has been popular $^{20,30}$ as it is well amenable to periodic calculations. In it, the absorption spectrum is computed based on the imaginary part of the frequency dependent dielectric function $\varepsilon(\omega)$. Although a different ansatz, the dipole approximation, similar to TD-DFT, also relies on orbital energies and shapes and critically depends on integrals over overlapping orbitals. We show that in the case of C60 aggregates, it also leads to unrealistically large redshifts.

In an attempt to overcome the shortcomings of both TD-DFT and the dipole approximation, we test an alternative approach in which we estimate the real polarizability from which the real and then imaginary part of $\varepsilon(\omega)$ and the spectrum are computed. We show that this approach (i) is less dependent on the choice of the exchange-correlation functional; specifically, the redshift of the spectrum with PBE compared to B3LYP is only about 10% of the excitation energy (compared to about 20% with TD-DFT) and (ii) appears to produce much more reasonable spectra of molecular aggregates than GGA TD-DFT or the dipole approximation, compared to available experimental data. The approach is also found to be costlier than TD-DFT, but on the other hand, it is perfectly parallelizable.

## II. COMPUTATIONAL METHODS

The DFT calculations on molecules and clusters were performed using Gaussian $09.^{31}$ The PBE, $^{32}$ B3LYP, $^{33,34}$ and $\omega$B97XD$^{35}$ functionals with the LanL2DZ$^{36}$ basis set were used. The HOMO and LUMO energies obtained with LanL2DZ were compared to those obtained with larger basis sets 6-311g and 6-311++g(2d,2p) to ensure that the basis is appropriate. The absorption spectra were computed using TD-DFT$^{26}$ considering 150, 150, and 100 lowest singlet-singlet transitions for C60 monomer, dimer, and tetramer, respectively. TD-DFT, which implements Casida equations, $^{25}$ is extremely sensitive to the shape and localization of orbitals. The excitation spectrum $\omega$ is obtained from the eigenvalue problem

$$
\begin{bmatrix}
A & B \\
B & A
\end{bmatrix}
\begin{bmatrix}
X \\
Y
\end{bmatrix}
= \omega
\begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}
\begin{bmatrix}
X \\
Y
\end{bmatrix}. \tag{1}
$$

The elements of matrices $A$ and $B$ depend on the integrals

$$
\begin{aligned}
K_{ia\mu,jb\nu} &= \iint \phi_{i\mu}^{*}(\boldsymbol{r}) \phi_{a\mu}(\boldsymbol{r}) \left( \frac{1}{|\boldsymbol{r}-\boldsymbol{r}'|} + \frac{\delta^2 E_{XC}}{\delta \rho_{\mu}(\boldsymbol{r}) \delta \rho_{\nu}(\boldsymbol{r}')} \right) \\
&\quad \times \phi_{j\nu}(\boldsymbol{r}') \phi_{b\nu}^{*}(\boldsymbol{r}') dr dr',
\end{aligned} \tag{2}
$$

where indices $i, j$ and $a, b$ label occupied and virtual orbitals $\phi$, respectively, and indices $\mu$ and $\nu$ denote spin, $\rho$ is the density, and $E_{XC}$ is the exchange-correlation energy. $^{25}$ Equation (2) is very sensitive to the quality of the orbitals and to any errors in the orbitals, in particular, because it involves overlap integrals with a kernel. For example, the effect of errors in orbitals is much stronger on Eq. (2) than it is on orbital energies. $^{27}$

Periodic DFT calculations of the C60 molecules and crystal were performed using SIESTA$^{37}$ with the PBE$^{32}$ functional. A DZP (double-$\zeta$ polarized) basis set was used and the density was expanded in plane waves with a cut-off frequency of 150 Ry. Grimme D2 type dispersion corrections were used to simulate the molecular crystal. $^{38}$ Structures were optimized until forces on all atoms were below $0.02\ \text{eV/\AA}$ and stress (for solid state calculations) was below 0.01 GPa. In crystal structure calculations, the Brillouin zone was sampled with $2 \times 2 \times 2$ Monkhorst-Pack$^{39}$ $k$ points. Molecular and cluster calculations were performed at the $\Gamma$ point in a $20 \times 20 \times 20\ \text{\AA}$ cell for molecules and $20 \times 20 \times 30\ \text{\AA}$ for dimers (whose axis was along the $z$ axis).

DFTB calculations were performed employing the self-consistent charge density functional tight binding scheme (SCC-DFTB)$^{28}$ using the DFTB+ 1.3 code. $^{40}$ SCC-DFTB is an approximate DFT approach derived from a second-order expansion of energy obtained by DFT. This method has been shown to provide near-DFT accuracy for systems for which it is has been parameterized. One of the best parameterized

sets for DFTB for organic materials is the set (of Slater-Koster files) 3ob-3-1 with DFTB-3 capability.⁴¹ This parameter set was benchmarked for organic systems and shows good accuracy.⁴²,⁴³ The 3ob-3-1 parameter set is used in this study with dispersion corrections using the Grimme parameters.⁴⁴,⁴⁵ For crystals, the Brillouin zone was sampled with $3×3×3$ $k$-points. For the light absorption properties computed with TD-DFTB,²⁹ 300, 600, 800, and 200 excited states were considered for the C60 monomer, dimer, tetramer, and octamer, respectively.

The states' excitation energies $E_i^{exc}$ and oscillator strengths $f_i$ obtained with TD-DFT and TD-DFTB were used to calculate the molar absorptivity $\mu$ as a continuous function of the excitation energy $E$ using

$$
\mu = \frac{1.35 \times 10^4}{\sigma} \sum_{i} f_i \exp\left[-2.772\left(\frac{E - E_i^{exc}}{2\sigma}\right)^2\right] \tag{3}
$$

with the HWHM (half width half maximum) broadening $\sigma = 0.25$ eV.

The molecular polarizability $\alpha(\omega)$ was computed as a function of excitation frequency $\omega$ with DFT⁴⁶ in Gaussian 09 for monomers (with PBE and B3LYP functionals) and dimers (with PBE). Due to a high CPU cost and convergence issues at high values of $\omega$ with DFT, calculations of $\alpha(\omega)$ for tetramers (as well as dimers) were done using the semi-empirical PM6 method,⁴⁷ which allowed us to compare absorption spectra between a dimer and a tetramer. That is, we compare monomer to dimer in DFT and dimer to tetramer in PM6 to estimate redshifts with increasing cluster size. The real part of the dielectric constant $\epsilon_r$ was computed from the molecular polarizability $\alpha(\omega)$ using the Clausius-Mossotti relation⁴⁸,⁴⁹

$$
\frac{\epsilon_r - 1}{\epsilon_r + 2} = \frac{N \alpha}{3\epsilon_0}, \tag{4}
$$

where $N$ is the number density of molecules and $\epsilon_0$ is the permittivity of vacuum. The Clausius-Mossotti relation makes the so-called Lorentz local field approximation, i.e., it is based on the assumption that the long-range interactions are isotropic and that there is no charge transfer between molecules, which is a reasonable approximation for neutral C60 in the ground state, as is confirmed by numeric results below. Equation (4) has been used to compute real dielectric constants for optical materials.⁵⁰

The imaginary part of the frequency-dependent dielectric function $\epsilon_i(\omega)$ was computed with DFT in SIESTA using

$$
\epsilon_i(\omega) = \frac{2e^2\pi}{\Omega \epsilon_0} \sum_{k,\nu,c} |\psi_k^c|\hat{\boldsymbol{q}} \cdot \boldsymbol{r}|\psi_k^\nu|^2 \delta(E_k^c - E_k^\nu - \hbar\omega), \tag{5}
$$

where $\Omega$ is the cell volume, indices $\nu$ and $c$ scan occupied and unoccupied $\psi_k^{c,\nu}$ orbitals (whose eigenstates are $E_k^{c,\nu}$), respectively, $k$ is the wavevector, and $\boldsymbol{q}$ is the photon polarization vector. This is the dipole approximation and the calculation is done in the "polycrystal" regime effectively averaging over $\boldsymbol{q}$. The calculation of $\epsilon_i(\omega)$, which has been used in the literature to compute spectra of fullerenes,²⁰ therefore also critically relies on the shape of Kohn-Sham orbitals due to an overlap integral with a kernel and is very sensitive to errors/approximations. The SIESTA calculations necessarily use a non-hybrid functional (PBE). Comparison to Gaussian calculations of $\epsilon(\omega)$, for which hybrid functionals can be used, also allows us to study the effect of the choice of the functional.

The real and imaginary parts of $\epsilon(\omega)$ computed with these two methods [i.e., either Eq. (4) or (5)] were used to compute, respectively, the imaginary and real parts using the Kramers-Kronig relations⁵¹,⁵²

$$
\begin{aligned}
\epsilon_{i} &=\frac{2}{\pi} \mathrm{P} \int_{0}^{\infty} \frac{\omega^{\prime} \epsilon_{r}\left(\omega^{\prime}\right)}{\omega^{2}-\omega^{\prime 2}} d \omega^{\prime}, \\
\epsilon_{r} &=-\frac{2}{\pi} \mathrm{P} \int_{0}^{\infty} \frac{\omega^{\prime} \epsilon_{i}\left(\omega^{\prime}\right)}{\omega^{2}-\omega^{\prime 2}} d \omega^{\prime},
\end{aligned} \tag{6}
$$

where P stands for the principal value.⁵³ The absorption spectrum (molar absorptivity $\mu$) is then computed as

$$
M \mu(\omega)=\frac{\sqrt{2} \omega}{c}\left(\sqrt{\epsilon_{r}(\omega)^{2}+\epsilon_{i}(\omega)^{2}}-\epsilon_{r}(\omega)\right)^{\frac{1}{2}}, \tag{7}
$$

where $M$ is the molar concentration and $c$ is the speed of light. The molar concentration is assumed to be that of the C60 crystal (i.e., even when computing the spectrum from single-molecule calculations) to highlight effects of molecular aggregation.

## III. RESULTS AND DISCUSSION

### A. Structures, band structures, and effect of aggregate state on band structure

Figure 1 shows the crystal structure of C60 optimized with DFT in SIESTA. The initial structure (fcc-like with four molecular units per unit cell) was taken from Ref. 54. The structure optimized with DFTB is visually similar. The lattice constant obtained with both DFT in SIESTA and DFTB+ is $13.8$ Å. Figure 1 also shows clusters of two, four, and eight units cut out of the crystal structure. The densities of states (DOS) around HOMO/VBM and LUMO/CBM states are shown in Fig. 2, where the DOS of a single molecule, clusters, and the solid computed with different methods are compared. In Ref. 17, we already established that the solid state leads to differences in energies between VBM/CBM of the solid and HOMO/LUMO of individual molecules on the order of 0.1 eV; here, we can see that the effect of the aggregate state on the DOS of C60 is well reproduced with about eight molecular units. This can have a significant effect on charge separation in donor-acceptor pairs with small driving force to charge separation, as a change of 0.1 eV in the driving force can change the separation rate by about a factor of two.⁵⁵ On the other hand, this magnitude of change in HOMO/VBM, LUMO/CBM, and the bandgap is not expected to have a major effect on the light absorption spectrum at a single-molecule level (through changes in excitation energies of transitions); however, optical properties could be affected by changes in the molecular environment and this is studied next.

![](./images/813034716172124161_3.jpg)

FIG. 1. The crystal structure of C60 and clusters with increasing numbers of units cut out from the crystal structure.

### B. Visible absorption computed with linear response TD-TDFT

#### 1. TD-DFTB vs TD-DFT for single molecule absorption spectrum

We first compute and compare TD-DFT and TD-DFTB absorption spectra in that the former is expected to be quanti-tatively accurate (with a hybrid functional)¹⁷ and can be used to benchmark the TD-DFTB spectrum. The TD-DFT and TD-DFTB absorption spectra of the C60 molecule are compared in Fig. 3. The excitation energies of absorption peaks appear to be underestimated by about 20% by TD-DFTB vs TD-DFT using the B3LYP functional. Figure 3 also includes TD-DFT spectra computed with the PBE functional (on which the DFTB param-eterization relies). We see that the absorption is also red-shifted vs PBE. This is largely due to redistribution of intensities among transitions rather than to lower energies of those tran-sitions; indeed, the bandgap with DFTB (1.79 eV) is slightly larger than with PBE (1.74) and is smaller than with B3LYP (2.83 eV), as expected.

#### 2. Effect of intermolecular interactions

Figure 3 also shows the TD-DFTB spectra computed on the clusters shown in Fig. 1. These spectra show a noticeable effect of molecular environment which mostly manifests itself in a red shift. The environment effect converges at about 8 molecular units; however, most of the effect is captured already at the dimer level. To confirm this conclusion at the TD-DFT level, we also computed absorption spectra of clusters (dimers and tetramers) with TD-DFT. In this case, to account for the fact that the hybrid-functional DFT is not expected to result in

![](./images/813034716172124161_4.jpg)

FIG. 2. The densities of states (DOS) of the C60 molecule, the clusters of dif-ferent sizes, and crystal computed with different methods. The ordinate axis is located between HOMO/VBM and LUMO/CBM.

![](./images/813034716172124161_5.jpg)

FIG. 3. Absorption spectra of the C60 molecule and clusters computed with TD-DFT (with PBE and B3LYP functionals) and TD-DFTB. Note the logarithmic scale used here to better highlight the redshift due to aggregation.

the same optimal interatomic arrangements as with dispersion-corrected DFTB and to prevent effects due to stress, DFT calculations are performed by using DFT-optimized molecules at the same intermolecular distance as in the DFTB-optimized crystal. The results show that a similar effect of the presence of neighboring molecules is seen in both TD-DFTB and TD-DFT. We also computed the effect of changing the monomer orientation at the same inter-molecular distance; the effect is relatively minor compared to the effect of the distance. Note that even though hundreds of transitions are included in TD-DFT and TD-DFTB calculations (see Sec. II), the spectrum of clusters does not extend much in energy due the very high density of transitions; this highlights difficulties of using TD-DFT to model effects of molecular aggregation.

The results of Fig. 3 imply a significant redshift of the absorption spectrum due to molecular aggregation. The redshift is so severe that it makes the spectra of clusters look unrealistic. Specifically, by comparing the experimental spectrum of C60 in Ref. 23 measured in a non-polar solvent, which can serve as an estimate of single-molecule absorption, to that of Ref. 56, which was measured in thin film, one observes that aggregation is expected to cause a mild redshift and an appearance of a shoulder (compare Fig. 1 of Ref. 23 with absorption onset around 3 eV and Fig. 2 of Ref. 56 which has an additional shoulder peaking at around 2.75 eV). The aggregation effect on the spectrum computed with B3LYP, where the spectrum of a single molecule is in semi-quantitative agreement with the experiment,23 is relatively reasonable but appears exaggerated vs experiment, while that computed with PBE is unreasonable.56 This is likely a method failure. TD-DFTB shows largely the same trend with cluster size as GGA TD-DFT, that is to say, this issue is not due to TD-DFTB but due to the underlying DFT approximation. This issue is addressed in Sec. III B 3.

### 3. Orbital delocalization

We have seen above that the effect of aggregation on the DOS is on the order of 0.1 eV (Fig. 2). The redshift observed in Fig. 3 is achieved not through a contraction of the gap but through amplification of transition intensities of low-energy transitions. This has to do with orbital shapes. Figure 4 shows frontier orbitals of the C60 molecule and clusters computed with DFTB and DFT with different functionals: GGA (PBE) and hybrid (B3LYP). They are delocalized over all molecular units; we have checked that delocalization persists even with the range-separated functional (ωB97XD). The orbitals are delocalized over neighboring molecular units with all these methods. Specifically, in periodic calculations, they are delocalized over all C60 units of the supercell. This is inconsistent with the formation of small excitons in C60 and with the hopping mechanism of electron transport which holds for C60.57 Although it has been argued that nuclear vibrations lead to barrierless electron transfer,58 they are not part of the present, 0K, model with which the TD-DFT spectra are computed. The delocalization therefore appears unphysical (i.e., not corresponding to the density distribution of real electrons). We note here that Kohn-Sham orbitals need not have physical meaning and need not have shapes equal to the electron charge distribution of real photoexcited electrons; within the DFT formalism, Eqs. (1) and (2) are exact. However, as argued above, they are prone to strong sensitivity to the shape of orbitals and to any errors/approximations affecting them. An alternative route to compute the effect of molecular aggregation on the spectrum is therefore desirable and this is considered next.

### C. Visible absorption computed from the frequency-dependent dielectric function

#### 1. Calculations of absorption spectra from the imaginary part of the dielectric function

Figure 5 shows the real and imaginary parts of the frequency dependent dielectric function and absorption spectra

![](./images/813034716172124161_6.jpg)

of the C60 crystal and C60 molecule computed based on the imaginary part of the dielectric function computed in SIESTA with the PBE functional. Similar to TD-DFT, the spectrum computed with the GGA functional even for one molecule is severely redshifted (compared to the spectrum computed with B3LYP above) due to the dependence of the dipole approximation on the Kohn-Sham spectrum. In this calculation, one observes a similarly large redshift of the absorption spectrum due to aggregation as in the GGA TD-DFT calculation. The absorption coefficient that we obtain for the crystal is of similar magnitude as that computed in Ref. 20 with a similar approach (N.B. for comparison, that paper applied the scissor operator). The severe redshift, however, indicates that also with this method, the effect due to aggregation is overstated. This is not surprising considering the critical dependence of Eq. (5) on the shape of the orbitals

![](./images/813034716172124161_7.jpg)

FIG. 5. Real and imaginary parts of the dielectric function (left) and absorption spectra (right) of C60 in molecular and crystalline state, where the imaginary part of the dielectric constant is computed by DFT in SIESTA. The dielectric function for the molecule is multiplied by the ratio of densities of molecules per simulation cell. The difference in the curves therefore shows the effect of aggregation.

(overlap with a kernel), which makes this approach very sensitive to the approximations used. Therefore, the method of computing optical properties via Eq. (5), often used in the solid state literature, is not accurate for C60 and likely for other fullerene based materials in solid state or other organic solids.

## 2. Calculations of absorption spectra from the real polarizability

Figure 6 shows the real and imaginary parts of the frequency dependent dielectric function and absorption spectra of the C60 molecule computed based on the real part of the dielectric function computed from polarizability in Gaussian with the PBE and B3LYP functionals. The absorption spectrum shows the following remarkable features:

(i) Absorption peaks' energies computed with PBE and B3LYP functionals of the C60 molecules only differ by about 10%. While the spectrum computed with PBE is redshifted vs that computed with B3LYP, the amount of redshift is smaller than the typical underestimation of the excitation energies with PBE when using TD-DFT or the dipole approximation.⁵⁹ This is because this formalism,⁴⁶ although does depend on integrals over occupied and unoccupied Kohn-Sham orbitals of the sort $\langle\phi_a\phi_j|\phi_b\phi_i\rangle$, $\langle\phi_a\phi_b|\phi_i\phi_j\rangle$,⁴⁶ does not depend on them in the same extremely sensitive way as TD-DFT or the dipole approximation in which the dependence (and therefore any errors) is amplified due to the kernel in the overlap integral. The spectrum computed with B3LYP is comparable with that computed with TD-DFT, which appears to be quantitively accurate¹⁷˒²³ for both the onset of absorption (from about 3 eV) and magnitude of the extinction coefficient of the first peak around 4 eV (on the order of 20 000 l mol⁻¹ cm⁻¹).

(ii) Absorption spectra, computed with the same GGA functional, of the molecule and the dimer differ much less from each other than spectra computed with GGA TD-DFT and the dipole approximation, as is also shown in Fig. 6; there is also a relatively small change in the spectrum between the dimer and the tetramer. There is a small-intensity feature in the dimer spectrum (based on PBE) around 1.75 eV, but the main absorption peak is overall similar to that of the monomer, with a much more modest redshift and a shoulder appearing at around 2.75 eV. This appears to be much more realistic than the large redshift obtained with GGA TD-DFT and the dipole approximations (Figs. 3 and 5). Specifically, experimental spectra measured in non-polar solvents (expected to be comparable to single-molecule spectra computed in a vacuum)²³ and in thin film⁵⁶ show similar change of spectral features due to aggregation, as explained in Sec. III B.

This approach therefore appears to work well for C60. The cost of the calculation, however, was higher than that of TD-DFT, and we also faced convergence problems for tetramers at higher excitation energies. We also had to limit ourselves to a GGA functional for dimer calculations and calculations of larger clusters were costly even with GGA. On the other hand, this approach is perfectly parallelizable as $\epsilon_r(\omega)$ can be independently computed for each frequency.

![](./images/813034716172124161_8.jpg)

FIG. 6. Real and imaginary parts of the dielectric function and absorption spectra of C60 molecules and clusters, where the real part of the dielectric constant is estimated from polarizability computed by DFT in Gaussian with PBE and B3LYP functionals for monomers and dimers, as well as with PM6 for dimers and tetramers. On the plots of the spectra, the dashed curves follow from Eqs. (4), (6), and (7) and correspond to the left ordinate axes and the smoothened curves are Gaussian-broadened with HWHM = 0.25 eV and correspond to the right ordinate axes.

## IV. CONCLUSIONS

We considered the effect of aggregation of C60 molecules on the band structure and optical properties. We studied changes in band structure when going from a single molecule to clusters of different sizes to the solid. Aggregation causes contraction of the bandgap via stabilization of the LUMO and destabilization of the HOMO on the order of 0.1 eV. Clusters of eight C60 units mimic the effect of the solid on the band structure well. This effect was considered using DFT with a hybrid functional for clusters and a GGA functional for clusters and the solid as well as using DFTB for clusters and in solid state. All methods showed qualitatively similar results with expected errors in the gap due to the use of specific approximations. Dispersion-corrected DFTB predicted similar lattice parameters of solid C60 as dispersion corrected DFT. We previously showed that DFTB also provides accurate molecular structures of fullerenes.¹⁷ DFTB can therefore be recommended as a fast and accurate method to model fullerene structures in aggregate state.

We then considered optical absorption spectra computed with (linear response) TD-DFT (using PBE and B3LYP functionals) and TD-DFTB. At the single molecule level, the spectra are qualitatively similar with quantitative differences which can be attributed to the use of specific functionals and parameterizations; i.e., single molecule spectra computed with all these methods can be practically useful as long as one accounts for unrealistic bandgap changes by using, e.g., the scissor operator. However, spectra computed with TD-DFT(B) for C60 clusters showed significant redshifts vs the single molecule; specifically, redshifts due to aggregation computed with a GGA functional and with DFTB were unrealistically large. The redshifts were stronger for larger clusters with the convergence of the spectra around eight molecular units, but most of the effect is already seen at the dimer level. This is a qualitative error which can be attributed to the strong dependence of linear response TD-DFT on shapes and energies of Kohn-Sham orbitals, which makes it very sensitive to errors and approximations (such as those due the choice of the functional). The orbitals of clusters and in the periodic solid state were found to be delocalized over multiple (or infinite number of) C60 units, which may not reflect real spatial distributions of densities of photogenerated electrons and holes of this excitonic material.

We also computed the absorption spectrum from the imaginary part of the complex dielectric function using the popular dipole approximation. This approach was also found to lead to an unrealistic redshift upon aggregation and much for the same reason of its critical dependence on Kohn-Sham orbital energies and shapes via overlap integrals with a kernel. Both TD-DFT and the dipole approximation therefore fail to account quantitatively for aggregation effects on the absorption spectrum. Their use is also complicated by the need to include multiple transitions as the absorption of fullerenes is not dominated by HOMO-to-LUMO transitions but transitions among many orbitals (very many in the case of clusters and solids).

We therefore considered an alternative approach, which appears to depend less critically on Kohn-Sham orbitals. We computed the real frequency-dependent polarizability from which the real part of the complex dielectric function is computed, then the imaginary part, and finally the absorption spectrum. We find that this approach (i) does not suffer from severe underestimation of the excitation energies when using the cheaper GGA approximation and (ii) leads to a realistic change in the spectrum when C60 molecules aggregate, even with a GGA functional. The cost of the calculation was higher than that of TD-DFT, and we also faced convergence problems for tetramers at higher excitation energies; however, this approach is perfectly parallelizable as $\epsilon_r(\omega)$ can be independently computed for each frequency. This therefore may be a promising approach to compute optical properties of organic crystals and clusters of molecules and possibly of other types of materials. This also highlights the utility of developing methods to compute frequency dependent polarizability which would be more stable and less dependent on the quality of the Kohn-Sham spectrum and orbital shapes.

## ACKNOWLEDGMENTS

This work was supported by the Ministry of Education of Singapore (AcRF Tier 1 grant). We thank Dr. Johann Lüder for assistance on parts on this work.

There are no conflicts of interest to declare.

¹T. Ameri, N. Li, and C. J. Brabec, *Energy Environ. Sci.* **6**, 2390–2413 (2013).
²J.-L. Brédas, J. E. Norton, J. Cornil, and V. Coropceanu, *Acc. Chem. Res.* **42**, 1691–1699 (2009).
³M. I. H. Ansari, A. Qurashi, and M. K. Nazeeruddin, *J. Photochem. Photobiol. C: Photochem. Rev.* **35**, 1–24 (2018).
⁴S. Yang, W. Fu, Z. Zhang, H. Chen, and C.-Z. Li, *J. Mater. Chem. A* **5**, 11462–11482 (2017).
⁵L. Lu, T. Zheng, Q. Wu, A. M. Schneider, D. Zhao, and L. Yu, *Chem. Rev.* **115**, 12666–12731 (2015).
⁶H. Kang, G. Kim, J. Kim, S. Kwon, H. Kim, and K. Lee, *Adv. Mater.* **28**, 7821–7861 (2016).
⁷W. Ke, D. Zhao, C. R. Grice, A. J. Cimaroli, J. Ge, H. Tao, H. Lei, G. Fang, and Y. Yan, *J. Mater. Chem. A* **3**, 17971–17976 (2015).
⁸Q. Jiang, Z. Chu, P. Wang, X. Yang, H. Liu, Y. Wang, Z. Yin, J. Wu, X. Zhang, and J. You, *Adv. Mater.* **29**, 1703852 (2017).
⁹W. Zhang, J. Xiong, L. Jiang, J. Wang, T. Mei, X. Wang, H. Gu, W. A. Daoud, and J. Li, *ACS Appl. Mater. Interfaces* **9**, 38467–38476 (2017).
¹⁰H. Tan, A. Jain, O. Voznyy, X. Lan, F. P. García de Arquer, J. Z. Fan, R. Quintero-Bermudez, M. Yuan, B. Zhang, Y. Zhao, F. Fan, P. Li, L. N. Quan, Y. Zhao, Z.-H. Lu, Z. Yang, S. Hoogland, and E. H. Sargent, *Science* **355**, 722–726 (2017).
¹¹P. T. Kissinger and W. R. Heineman, *J. Chem. Educ.* **60**, 702 (1983).
¹²H. Kirihata and M. Uda, *Rev. Sci. Instrum.* **52**, 68–70 (1981).
¹³H. D. Pham, H. Hu, K. Feron, S. Manzhos, H. Wang, Y. M. Lam, and P. Sonar, *Solar RRL* **1**, 1700105 (2017).
¹⁴T. T. Do, K. Rundel, Q. Gu, E. Gann, S. Manzhos, K. Feron, J. Bell, C. R. McNeill, and P. Sonar, *New J. Chem.* **41**, 2899–2909 (2017).
¹⁵T.-T. Do, Y. Takeda, S. Manzhos, J. Bell, S. Tokito, and P. Sonar, *J. Mater. Chem. C* **6**, 3774–3786 (2018).
¹⁶Q. Liu, A. Surendran, K. Feron, S. Manzhos, X. Jiao, C. R. McNeill, S. E. Bottle, J. Bell, W. L. Leong, and P. Sonar, *New J. Chem.* **42**, 4017–4028 (2018).
¹⁷A. Pal, L. K. Wen, C. Y. Jun, I. Jeon, Y. Matsuo, and S. Manzhos, *Phys. Chem. Chem. Phys.* **19**, 28330–28343 (2017).
¹⁸A. Rodríguez-Fortea, S. Irie, and J. M. Poblet, *Wiley Interdiscip. Rev.: Comput. Mol. Sci.* **1**, 350–367 (2011).
¹⁹W. Y. Ching, M.-Z. Huang, Y.-N. Xu, W. G. Harter, and F. T. Chan, *Phys. Rev. Lett.* **67**, 2045–2048 (1991).
²⁰H.-T. Xue, G. Boschetto, M. Krompiec, G. E. Morse, F.-L. Tang, and C.-K. Skylaris, *Phys. Chem. Chem. Phys.* **19**, 5617–5628 (2017).

$^{21}$J. P. Hare, H. W. Kroto, and R. Taylor, *Chem. Phys. Lett.* **177**, 394–398 (1991).

$^{22}$J. W. Arbogast, A. P. Darmanyan, C. S. Foote, F. N. Diederich, R. L. Whetten, Y. Rubin, M. M. Alvarez, and S. J. Anz, *J. Phys. Chem.* **95**, 11–12 (1991).

$^{23}$V. S. Pavlovich and E. M. Shpilevsky, *J. Appl. Spectrosc.* **77**, 335–342 (2010).

$^{24}$J. W. Arbogast and C. S. Foote, *J. Am. Chem. Soc.* **113**, 8886–8889 (1991).

$^{25}$M. E. Casida, *J. Mol. Struct.: THEOCHEM* **914**, 3–18 (2009).

$^{26}$M. A. L. Marques and E. K. U. Gross, *Annu. Rev. Phys. Chem.* **55**, 427–455 (2004).

$^{27}$S. Manzhos, H. Segawa, and K. Yamashita, *Chem. Phys. Lett.* **527**, 51–56 (2012).

$^{28}$M. Elstner, D. Porezag, G. Jungnickel, J. Elsner, M. Haugk, T. Frauenheim, S. Suhai, and G. Seifert, *Phys. Rev. B* **58**, 7260–7268 (1998).

$^{29}$T. A. Niehaus, S. Suhai, F. Della Sala, P. Lugli, M. Elstner, G. Seifert, and T. Frauenheim, *Phys. Rev. B* **63**, 085108 (2001).

$^{30}$L. E. Ratcliff and P. D. Haynes, *Phys. Chem. Chem. Phys.* **15**, 13024–13031 (2013).

$^{31}$M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone, B. Mennucci, G. A. Petersson, H. Nakatsuji, M. Caricato, X. Li, H. P. Hratchian, A. F. Izmaylov, J. Bloino, G. Zheng, J. L. Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J. A. Montgomery, Jr., J. E. Peralta, F. Ogliaro, M. Bearpark, J. J. Heyd, E. Brothers, K. N. Kudin, V. N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, N. Rega, J. M. Millam, M. Klene, J. E. Knox, J. B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R. E. Stratmann, O. Yazyev, A. J. Austin, R. Cammi, C. Pomelli, J. W. Ochterski, R. L. Martin, K. Morokuma, V. G. Zakrzewski, G. A. Voth, P. Salvador, J. J. Dannenberg, S. Dapprich, A. D. Daniels, Ö. Farkas, J. B. Foresman, J. V. Ortiz, J. Cioslowski, and D. J. Fox, *GAUSSIAN 09*, Revision D.01, Gaussian, Inc., Wallingford CT, 2009.

$^{32}$J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865–3868 (1996).

$^{33}$A. D. Becke, *J. Chem. Phys.* **98**, 5648–5652 (1993).

$^{34}$C. Lee, W. Yang, and R. G. Parr, *Phys. Rev. B* **37**, 785–789 (1988).

$^{35}$J.-D. Chai and M. Head-Gordon, *J. Chem. Phys.* **128**, 084106 (2008).

$^{36}$P. J. H. T. H. Dunning, Jr., *Modern Theoretical Chemistry*, edited by H. F. Schaefer III (Plenum, New York, NY, USA, 1976), Vol. 3, pp. 1–28.

$^{37}$J. M. Soler, E. Artacho, J. D. Gale, A. García, J. Junquera, P. Ordejón, and D. S. Portal, *J. Phys.: Condens. Matter* **14**, 2745 (2002).

$^{38}$S. Grimme, *J. Comput. Chem.* **27**, 1787–1799 (2006).

$^{39}$H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188–5192 (1976).

$^{40}$B. Aradi, B. Hourahine, and T. Frauenheim, *J. Phys. Chem. A* **111**, 5678–5684 (2007).

$^{41}$M. Gaus, Q. Cui, and M. Elstner, *J. Chem. Theory Comput.* **7**, 931–948 (2011).

$^{42}$M. Gaus, A. Goez, and M. Elstner, *J. Chem. Theory Comput.* **9**, 338–354 (2013).

$^{43}$M. Gaus, X. Lu, M. Elstner, and Q. Cui, *J. Chem. Theory Comput.* **10**, 1518–1537 (2014).

$^{44}$S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, *J. Chem. Phys.* **132**, 154104 (2010).

$^{45}$S. Grimme, S. Ehrlich, and L. Goerigk, *J. Comput. Chem.* **32**, 1456–1465 (2011).

$^{46}$J. E. Rice and N. C. Handy, *J. Chem. Phys.* **94**, 4959–4971 (1991).

$^{47}$J. J. P. Stewart, *J. Mol. Model.* **13**, 1173–1213 (2007).

$^{48}$O. F. Mossotti, *Mem. di Math. e di Fis. della Soc. Ital. della Sci. Resid. Modena* **24**, 49–74 (1850).

$^{49}$R. Clausius, *Abhandlungungen über die Mechanische Wärmetheorie* (Friedrich Vieweg und Sohn, Braunschweig, 1867), Vol. 2, p. 143.

$^{50}$G. Giorgi, T. Yoshihara, and K. Yamashita, *Phys. Chem. Chem. Phys.* **18**, 27124–27132 (2016).

$^{51}$R. de L. Kronig, *J. Opt. Soc. Am.* **12**, 547–557 (1926).

$^{52}$H. A. Kramers, *Atti Cong. Intern. Fisici* (Transactions of Volta Centenary Congress) Como **2**, 545–557 (1927).

$^{53}$A. D. Polyanin and A. V. Manzhirov, *Handbook of Mathematics for Engineers and Scientists* (Chapman & Hall/CRC, 2006).

$^{54}$W. I. F. David, R. M. Ibberson, J. C. Matthewman, K. Prassides, T. J. S. Dennis, J. P. Hare, H. W. Kroto, R. Taylor, and D. R. M. Walton, *Nature* **353**, 147 (1991).

$^{55}$S. E. Koops, B. C. O'Regan, P. R. F. Barnes, and J. R. Durrant, *J. Am. Chem. Soc.* **131**, 4808–4818 (2009).

$^{56}$S. Pfuetzner, J. Meiss, A. Petrich, M. Riede, and K. Leo, *Appl. Phys. Lett.* **94**, 223307 (2009).

$^{57}$H. Yang, F. Gajdos, and J. Blumberger, *J. Phys. Chem. C* **121**, 7689–7696 (2017).

$^{58}$D. L. Cheung and A. Troisi, *J. Phys. Chem. C* **114**, 20479–20488 (2010).

$^{59}$H. Jacquemin, E. A. Perpète, G. E. Scuseria, I. Ciofini, and C. Adamo, *J. Chem. Theory Comput.* **4**, 123–135 (2008).