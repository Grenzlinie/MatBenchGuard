# Experimental and quantum-chemical determination of the $^2$H quadrupole coupling tensor in deuterated benzenes

Anu M. Kantola, $^{ab}$ Susanna Ahola, $^{a}$ Juha Vaara, $^{b}$ Jani Saunavaara $^{a}$ and
Jukka Jokisaari $^{a}$

Received 22nd September 2006, Accepted 14th November 2006
First published as an Advance Article on the web 4th December 2006
DOI: 10.1039/b613830f

Deuterium Quadrupole Coupling Constant (DQCC) in benzene was determined both experimentally by Nuclear Magnetic Resonance spectroscopy in Liquid Crystalline solutions (LC NMR) and theoretically by *ab initio* electronic structure calculations. DQCCs were measured for benzene-$d_1$ and 1,3,5-benzene-$d_3$ using several different liquid crystalline solvents and taking vibrational and deformational corrections into account in the analysis of experimental dipolar couplings, used to determine the orientational order parameter of the dissolved benzene. The experimental DQCC results for the isotopomers benzene-$d_1$ and 1,3,5-benzene-$d_3$ are found to be 187.7 kHz and 187.3 kHz, respectively, which are essentially equal within the experimental accuracy ($\pm$0.4 kHz). Theoretical results were obtained at different C–D bond lenghts, and by applying corrections for electron correlation and rovibrational motion on top of large-basis-set Hartree–Fock results. The computations give a consistent DQCC of *ca*. 189 kHz for three different isotopomers; benzene-$d_1$, 1,3,5-benzene-$d_3$, and benzene-$d_6$, revealing that isotope effects are not detectable within the present experimental accuracy. Calculations carried out using a continuum solvation model to account for intermolecular interaction effects result in very small changes as compared to the data obtained *in vacuo*. The comparison of theoretical and experimental results points out the selection of the underlying molecular geometry as the most likely source of the remaining discrepancy of less than 2 kHz. Such an agreement between the calculated and the experimental DQCC results can only be achieved if rovibrational effects are considered on one hand in the experimental direct dipolar coupling data, and on the other hand in the theoretical property calculation, as is done presently.

## 1. Introduction

The electric quadrupole moment of a quadrupolar nucleus (nuclear spin $\geq 1$) interacts with the Electric Field Gradient (EFG) at the nuclear site. For a molecule in an anisotropic environment, this leads to splitting of the resonance lines in the Nuclear Magnetic Resonance (NMR) spectrum. Provided that the Nuclear Quadrupole Coupling Constant (NQCC) of the nucleus is known, the observed quadrupole splitting can be utilized to obtain information about the orientation of the molecule, as the spectrum is directly related to the second-rank orientational order parameter. On the other hand, NMR relaxation measurements can be used as a probe to investigate dynamic processes in molecules and solutions, but to extract this kind of information from the experiments, one needs prior knowledge about the NQCC.

Deuterium (spin = 1) NMR spectroscopy has, over the years, proven to be a particularly powerful method of studying the orientational order, due to the fact that the spectrum is simple compared to the conventional proton NMR spectrum.$^1$ The Deuterium Quadrupole Coupling Constant (DQCC) of the benzene molecule is commonly applied to the determina- tion of the orientational order of Liquid Crystal (LC) mole- cules containing aromatic rings, and of related molecules dissolved in LCs.$^1$ Hence, it is necessary to know the DQCC as well as the asymmetry parameter $\eta$ of the quadrupole coupling tensor for this system as accurately as possible. Furthermore, reliable experimental results are in demand for comparison with theoretical calculations. Data for DQCC in deuterated benzenes have been previously reported by liquid crystal NMR (LC NMR),$^{2–7}$ NMR relaxation measurements,$^8$ solid state NMR$^{9–12}$ and MicroWave Fourier Transform (MWFT)$^{13,14}$ techniques, as well as theoretical calcula- tions.$^{13,15,16}$ The results vary widely from 180.7 to 223 kHz, which does not represent sufficient accuracy for further appli- cations. Consequently, it appears necessary to revisit the subject.

In LC NMR spectroscopy, molecules are dissolved into LC solvents and the observed direct dipolar couplings together with quadrupole splittings are utilized to extract information about the nuclear quadrupole coupling tensor. However, it has been observed that the chosen LC solvent can have a sub- stantial influence on the apparent NQCC obtained from the NMR data$^{17}$ and a careful consideration is in place to

$^{a}$ NMR Research Group, Department of Physical Sciences, P.O. Box 3000, University of Oulu, FIN-90014, Finland. E-mail: jukka.jokisaari@oulu.fi
$^{b}$ Laboratory of Physical Chemistry, Department of Chemistry, P.O. Box 55 (A. I. Virtasen aukio 1), University of Helsinki, FIN-00014, Finland. E-mail: juha.t.vaara@helsinki.fi

minimize the solvent effects. In addition, vibrational and rotational motions of the molecule affect the observable NMR parameters and should be taken into account if reliable results are desired.

In this study, the DQCC in benzene is determined experimentally from the NMR spectra of benzene-$d_1$ and 1,3,5-benzene-$d_3$ measured at various temperatures in several LC solvents, as well as calculated theoretically by *ab initio* methods. A thorough consideration is devoted to the rovibrational and solvent effects as well as the influence of the geometry, in both the experimental analysis and the electronic structure calculations.

## 2. Theory

### 2.1. Anisotropic interactions in a liquid crystal environment

The LC state is a mesophase between the solid and the liquid phases. In a LC, molecules undergo both translational and rotational motion, but they also exhibit orientational order. A molecule dissolved into a LC is partially oriented and the intramolecular anisotropic interactions become observable, whereas the intermolecular interactions average to zero as in a normal isotropic sample. The elements of the Saupe order tensor $S^{18}$ with respect to the external magnetic field, $B_0$, describe the orientation of a molecule dissolved in a LC. $S$ is usually presented as

$$
S_{\alpha\beta} \equiv \langle s_{\alpha\beta} \rangle = \frac{1}{2} \langle 3\cos\theta_{\alpha}\cos\theta_{\beta} - \delta_{\alpha\beta} \rangle, \tag{2.1}
$$

where $\theta_{\alpha}$ is the angle between the magnetic field direction and the $\alpha$ axis of the Cartesian coordinate system ($\alpha, \beta = x, y, z$) attached to the molecule. The angular brackets denote averaging over molecular motion. The orientation of a general molecule can be unambiguously described with five independent orientation parameters, $S_{zz}, (S_{xx} - S_{yy}), S_{xy}, S_{xz}$ and $S_{yz}$, as the order tensor is traceless and symmetric by definition. However, the order tensor must be invariant in all symmetry operations of the molecule, thus the number of independent order parameters reduces as the molecular symmetry increases.

In addition to isotropic spin–spin couplings and nuclear shieldings, anisotropic spectra are characterized by dipolar and quadrupolar interactions. The direct dipolar coupling $D_{ij}$ between nuclei $i$ and $j$ can be obtained from the observable splitting, $2D_{ij} + J_{ij}$, and in a molecule dissolved into a uniaxial LC, $D_{ij}$ can be written as

$$
D_{ij} = -P_2(\cos\beta)\frac{\mu_0 \hbar \gamma_i \gamma_j}{8\pi^2} \left\langle \frac{s_{ij}^D}{r_{ij}^3} \right\rangle, \tag{2.2}
$$

where $P_2(\cos \beta)$ is the second-order Legendre polynomial, $\beta$ is the angle between the LC director and the external magnetic field ($\beta = 0^\circ$ or $90^\circ$ depending on the sign of the anisotropy of the magnetizability tensor of the molecules constituting the LC phase$^{19}$), $\hbar$ is Planck's constant divided by $2\pi$, $\mu_0$ is the permeability of a vacuum, $\gamma_i$ is the gyromagnetic ratio of nucleus $i$, $r_{ij}$ is the distance between the nuclei and $S_{ij}^D = \langle s_{ij}^D \rangle$ is the order parameter of the internuclear vector $\mathbf{r}_{ij}$ with respect to the LC director. Placement of the quotient $s_{ij}^D / r_{ij}^D$ within the angular brackets manifests the fact that the re-orientational and vibrational motions of the molecule are interdependent and can not, in general, be treated separately. Thus, when analyzing experimental dipolar couplings to extract orientation parameters, contributions arising from small-amplitude molecular motions should be carefully considered. The experimental dipolar coupling can be subdivided into separate contributions

$$
D_{ij}^{\exp} = D_{ij}^e + D_{ij}^h + D_{ij}^{ah} + D_{ij}^d + \frac{1}{2}J_{ij}^{\text{aniso}}, \tag{2.3}
$$

where $D_{ij}^e$ corresponds to the dipolar coupling at the equilibrium geometry while $D_{ij}^h$ and $D_{ij}^{ah}$ arise from the harmonic$^{20}$ and anharmonic$^{21}$ vibrations, respectively. The contribution $D_{ij}^d$ is the deformation term caused by the aforementioned correlation between the vibration and the rotation of the molecule. This can be described with a solvent-induced, traceless and symmetric interaction tensor, $A$, which represents the intermolecular interaction potential that couples with the intramolecular force field.$^{22–24}$ As indicated in eqn (2.3), the anisotropic part of the spin–spin coupling, $J_{ij}^{\text{aniso}}$, also contributes to the observed $D$ coupling. However, the anisotropy of the spin–spin coupling tensor has been shown to be insignificant for CH and HH couplings ($J_{ij}^{\text{aniso}} / D_{ij}^{\exp} \simeq 10^{-4} - 10^{-3}$)$^{19,25}$ and can be ignored in the analysis of these couplings.

For deuterium, the quadrupolar interaction further splits the spectrum into a doublet. Because benzene-$d_1$ has a two-fold symmetry axis along the CD bond, its order tensor is completely described by two orientation parameters, $S_{zz}$ and $(S_{xx} - S_{yy})$, and the observed quadrupolar splitting $2B$ can be expressed as

$$
2B = \frac{3}{2}\chi_{zz} \left[ S_{zz} + \frac{1}{3}\eta(S_{xx} - S_{yy}) \right], \tag{2.4}
$$

where $\chi_{zz}$ is DQCC, *i.e.*, the quadrupole coupling tensor element along the CD bond

$$
\chi_{zz} = eqQ/h, \tag{2.5}
$$

and $\eta$ is the asymmetry parameter of the quadrupole coupling tensor

$$
\eta = \frac{\chi_{xx} - \chi_{yy}}{\chi_{zz}}. \tag{2.6}
$$

The coordinate system is chosen to have its $z$ axis along the C–D bond and $y$ axis perpendicular to the benzene ring. In eqn (2.5), $Q$ is the nuclear quadrupole moment and $eq$ is the EFG tensor element along the C–D bond. As 1,3,5-benzene-$d_3$ possesses a three-fold symmetry axis, only one independent orientation parameter, $S_{zz}$, is necessary and eqn (2.4) further reduces to

$$
2B = \frac{3}{2} \chi_{zz} S_{zz}(1 + \eta). \tag{2.7}
$$

### 2.2. Quantum-chemical calculations

From the point of view of electronic structure theory, NQCC and the associated tensor can be obtained straightforwardly by combining the nuclear electric quadrupole moment$^{26}$ with the

calculated EFG. The latter can be obtained as an expectation value, by first-order perturbation theory, if a variational quantum-chemical model such as the Hartree-Fock Self-Con- sistent Field (SCF) wave function is used. With non-varia- tional models such as second-order Møller-Plesset perturbation theory (MP2), Coupled Cluster Singles and Doubles (CCSD) or CCSD with perturbative Triples [CCSD(T)], additional response theory calculation must be performed to obtain a relaxed one-particle density matrix. In all cases, the property demands a rather good one-particle basis set for converged results. Due to the form of the quantum mechanical operator for EFG, the basis needs to be saturated in particular with high-exponent ("tight") p-type functions.

Quadrupole coupling is sensitive to molecular geometry; the DQCC in particular depends on the length of X-D bond involving the deuterium in question. $^{27-29}$ Hence, this property obtains important contributions from the quantum mechan- ical zero-point vibrational motion of the nuclear framework, as well as thermal excitations. When dealing with rigid mole- cules featuring small-amplitude motion, the rovibrational contributions to molecular properties may be obtained by using a perturbational approach (see, e.g., ref. 30). This corresponds to expanding the investigated property as a Taylor series expansion in terms of the vibrational normal coordinates $Q_{k}$ around a suitable reference geometry, followedby thermal averaging of the expansion:

$$
\begin{aligned}
\langle\chi\rangle^{T} & =\chi_{e}+\sum_{k}\left(\frac{\partial \chi}{\partial Q_{k}}\right)_{e}\left\langle Q_{k}\right\rangle^{T} \\
& +\frac{1}{2} \sum_{k l}\left(\frac{\partial^{2} \chi}{\partial Q_{k} \partial Q_{l}}\right)_{e}\left\langle Q_{k} Q_{l}\right\rangle^{T}+\ldots.
\end{aligned}\qquad(2.8)
$$

This expansion converges rapidly in rigid molecules $^{31}$ and, when using the equilibrium geometry $r_{e}$ as the expansion point, typically one retains only the linear and quadratic termsof the expansion. To the leading order, $\langle Q_{k} Q_{l}\rangle^{T}$ can beobtained from the harmonic force field, whereas the $\langle Q_{k}\rangle^{T}$  are determined by the cubic anharmonic terms in the force field perturbing the harmonic oscillator state, as well as centrifugal distortion. $^{32}$ The effects of anharmonic vibrations as well as centrifugal distortion can, to a good accuracy, be accommodated by carrying out the molecular property calcu- lation at an effective $r_{\alpha}(T)$ geometry, where the nuclei of a specific isotopomer are placed in their average positions at thetemperature in question. $^{21}$ 

If, instead of $r_{e}$ , the $r_{\alpha}(T)$ geometry is chosen as the expan sion point in eqn (2.8), one only needs to calculate the harmonic vibrational contribution to obtain the full leading- order rovibrational effect. $^{21,33-35}$ It has furthermore been shown that by performing the harmonic corrections at this effective geometry, a smaller truncation error in the expansion occurs. $^{36}$ This approach has been implemented $^{37}$ to the DAL TON quantum-chemical software package $^{38}$ that uses a combi nation of analytic and finite difference techniques to obtain the property derivatives $(\partial^{2} \chi / \partial Q_{k} Q_{l})_{\alpha}$ . A more detailed account of the theory and implementation of the rovibrational correc-tions will be published elsewhere. $^{37}$ 

Besides rovibrational motion and electron correlation ef- fects, the experimental deuterium quadrupole coupling tensor may also be influenced by solvation effects. In the Self-Con- sistent Reaction Field (SCRF) model, $^{39}$ the solute is placed in a spherical cavity cut into a linear and continuous dielectric medium, with the dielectric constant appropriate to the solvent in question. The electric multipoles of the solute polarize the dielectric medium with the result that secondary fields induced back to the cavity affect the charge distribution of the solute. The method is able to treat long-range electrostatic interac- tions, whereas specific short-range solvation effects would require the inclusion of explicit solvent molecules in super- molecular calculations.

## 3. NMR experiments
Samples containing $ca.10 mol\%$ of benzene- $d_{1}$ were prepared to LCs Phase IV, ZLI 2806, Phase 1083, and to the magic mixture of ZLI 1132 (55 wt $\%$ ) and EBBA (45 wt $\%$ ) (referred to as MIX M), for which the contribution from the LC solvent-induced external EFG is minimized. $^{40}$ The samples of 1,3,5-benzene- $d_{3}$ were prepared to LCs Phase 1083, ZLI2806, Phase IV, and to the good mixture of Phase IV (40 wt $\%$ ) and ZLI 1132 (60 wt $\%$ ) (referred to as MIX G) for which the geometric distortions of the solute molecules are minimized. It has been observed that this kind of mixture of LCs also yieldsvirtually deformation-free values for the NMR parameters. $^{41}$  All the LC solvents used in this work have a positive aniso- tropy of the magnetizability tensor, rendering the director to orient along the external magnetic field, except for ZLI 2806, which orients perpendicular to the field. All the presently considered LC phases are thermotropic, nematic, and uniaxial.

The $^{1} H$ and $^{2} D$ NMR spectra of benzene- $d_{1}$ and 1,3,5 benzene- $d_{3}$ were measured at various temperatures within the nematic temperature range of each solvent. Each spectrumyielded a total of nine (for benzene- $d_{1}$ ) or four (for benzene- $d_{3}$ ) HH and HD couplings. To obtain more information on the effective geometry of benzene in the solution state, a satellite spectrum arising from the one-bond CH couplings for ben- zene- $d_{3}$ in the LCs MIX G and Phase IV was measured with astandard 1D heteronuclear Double Quantum Filter (DQF) pulse sequence optimized for that coupling. The coherence selection was carried out with phase cycling. The spectra weremeasured on Bruker DSX300, DPX400 (the sample MIX G)and DRX500 (samples MIX G, and $C_{6} H_{3} D_{3}$ in Phase IV) spectrometers. Typically 128, 2 k and 128 scans with 8 k, 32 k, and 16 k data points were accumulated to cover spectral widths of 3 kHz, 38.5 kHz, and 7 kHz for proton, deuterium, and DQF spectra, respectively. The temperature was measured with the temperature unit of the spectrometer, which in turn had been calibrated with standard calibration samples(ethylene glycol and methanol). The spectra were analyzed with PERCH NMR software $^{42,43}$ using the "integral trans form" and "total line shape fitting" modes. Spin-spin cou- pling constants were taken from ref. 44 and kept fixed during the iterations. The relative magnitudes of the dipolar couplings were adopted from ref. 5 and adjusted to fit the experimental proton spectrum in an iterative process. Quadrupole cou- plings, 2B, were determined from the deuterium spectra.

The orientation tensors were calculated from vibrationally- and deformationally-corrected dipolar couplings using the program MASTER⁴⁵ and an experimental harmonic force field by Goodman et al.⁴⁶ As there is not enough independent information to derive both the DQCC and the asymmetry parameter of the quadrupole coupling tensor from the LC NMR data alone, a previously determined experimental value of 0.041 from ref. 11 was adopted for the asymmetry parameter. The experimental data were also analyzed using the present theoretical ab initio value of 0.056 (MP2 with rovibrational corrections, see below) for the asymmetry parameter. The observed quadrupole splittings were then utilized to solve for the DQCCs from eqn (2.4) and (2.7) for benzene-$d_1$ and 1,3,5-benzene-$d_3$, respectively. In the program MASTER, the harmonic corrections are calculated using a specified harmonic force field and the anharmonic effects are taken into account either by including geometry parameters as adjustable parameters (in case there are enough independent experimental data) or fixing the geometry into a pre-determined $r_\alpha$ geometry during the analysis.

The bond additivity model is used to represent the interaction tensor, $A$, as a sum of bond interaction tensors, $A_{ij}$, describing torques acting on separate bonds of the molecule.²²⁻²⁴ These tensors are utilized to calculate the orientation parameters and adjusted in an iterative manner—in conjunction with the optional free geometry parameters—to reproduce the experimental dipolar couplings. If a cylindrically symmetric bond interaction tensor and a rigid bond is assumed, only one parameter, e.g., the anisotropy $\Delta A_{ij}$, is necessary to fully describe the interaction tensor for each bond type. Within the accuracy of the deformation theory, these assumptions are reasonable for benzene, leading to three interaction parameters for each spectrum, $\Delta A_{CC}$, $\Delta A_{CH}$ and $\Delta A_{CD}$, to be varied in the iterative process. The orientational order parameters can then be calculated from the interaction parameters. With these presuppositions, the number of independent dipolar couplings exceeds the number of adjustable parameters, leaving the problem well-defined even for benzene-$d_3$.

Only a relative geometry can be obtained from the dipolar couplings. Thus, the C–C bond length was fixed to the theoretical $r_z$ value [the $r_z$ geometry equals $r_\alpha(0\ \text{K})$ for $\text{C}_6\text{H}_6$ (1.3964 Å at the CCSD(T) level of theory with cc-pVQZ basis set⁴⁷) and only the CH and CD bond lengths were fitted. The relative bond lengths were determined from the spectra of the 1,3,5-$\text{C}_6\text{H}_3\text{D}_3$ in the good mixture, taking into account only the harmonic vibrations, as the geometry should be undisturbed and the analysis can, to a good accuracy, be done without considering the deformational corrections. This way the number of adjustable parameters reduces to one per spectrum (orientation parameter $S_{zz}$) and two common parameters for all the spectra measured in the good mixture (relative bond lengths $r_{CD}/r_{CC}$ and $r_{CH}/r_{CC}$), allowing fitting of the bond lengths. This analysis led to relative bond lengths $r_{CD}/r_{CC}=0.774$ and $r_{CH}/r_{CC}=0.776$ that are in good agreement with the previously found value of 0.777 for $r_{CH}/r_{CC}$.⁴⁸,⁴⁹ The relative bond lengths were fixed to these values in the analysis of the rest of the spectra, and also for benzene-$d_1$.

As an example of the 32 data sets obtained at various temperatures, in various LC solvents and for the two isotopomers, two sets of experimental data, one for each isotopomer, are represented in Table 1. Orientation parameters, the measured quadrupolar and dipolar couplings as well as different contributions to the calculated dipolar couplings obtained from the analysis of the experimental data are listed in the table. The data for benzene-$d_3$ is from one of the experimental sets measured in the good mixture (solvent MIX G), which were utilized for the geometry optimization, thus excluding the deformational corrections (see the text above). The data for benzene-$d_1$ is from one of the experimental sets in the

<table>
<thead>
<tr>
<th>Molecule</th>
<th>Coupling</th>
<th>$D^{\text{exp}}$</th>
<th>$D^{\text{e}}$</th>
<th>$D^{\text{h}}$</th>
<th>$D^{\text{d}}$</th>
<th>$D^{\text{calc}}$</th>
<th>$\Delta D^{b}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{C}_6\text{H}_5\text{D}$</td>
<td>$D_{\text{HD}}^{7-8}$</td>
<td>$-99.101$</td>
<td>$-100.318$</td>
<td>$1.269$</td>
<td>$-0.088$</td>
<td>$-99.136$</td>
<td>$0.035$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HD}}^{7-9}$</td>
<td>$-18.987$</td>
<td>$-19.221$</td>
<td>$0.118$</td>
<td>$-0.002$</td>
<td>$-19.105$</td>
<td>$0.118$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HD}}^{7-10}$</td>
<td>$-12.294$</td>
<td>$-12.457$</td>
<td>$0.043$</td>
<td>$0.002$</td>
<td>$-12.412$</td>
<td>$0.118$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{8-9}$</td>
<td>$-639.917$</td>
<td>$-648.364$</td>
<td>$9.296$</td>
<td>$-0.837$</td>
<td>$-639.905$</td>
<td>$-0.012$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{8-10}$</td>
<td>$-123.886$</td>
<td>$-125.055$</td>
<td>$0.980$</td>
<td>$-0.090$</td>
<td>$-124.165$</td>
<td>$0.279$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{8-11}$</td>
<td>$-81.384$</td>
<td>$-81.585$</td>
<td>$0.370$</td>
<td>$-0.016$</td>
<td>$-81.231$</td>
<td>$0.153$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{8-12}$</td>
<td>$-125.169$</td>
<td>$-125.886$</td>
<td>$0.946$</td>
<td>$-0.071$</td>
<td>$-125.011$</td>
<td>$0.158$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{9-10}$</td>
<td>$-644.223$</td>
<td>$-652.682$</td>
<td>$9.405$</td>
<td>$-0.949$</td>
<td>$-644.227$</td>
<td>$0.004$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{9-11}$</td>
<td>$-125.032$</td>
<td>$-125.886$</td>
<td>$0.946$</td>
<td>$-0.071$</td>
<td>$-125.011$</td>
<td>$-0.021$</td>
</tr>
<tr>
<td></td>
<td colspan="7">$2B = 24.122\ \text{kHz},\ S_{zz}=0.0823,\ S_{xx}-S_{yy}=0.2483$</td>
</tr>
<tr>
<td>1,3,5-$\text{C}_6\text{H}_3\text{D}_3$</td>
<td>$D_{\text{HD}}^{7-8}$</td>
<td>$-97.325$</td>
<td>$-98.637$</td>
<td>$1.312$</td>
<td>—</td>
<td>$-97.325$</td>
<td>$0.000$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HD}}^{7-9}$</td>
<td>$-2.518$</td>
<td>$-2.918$</td>
<td>$0.014$</td>
<td>—</td>
<td>$-2.903$</td>
<td>$0.385$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HD}}^{7-10}$</td>
<td>$-12.281$</td>
<td>$-12.330$</td>
<td>$0.044$</td>
<td>—</td>
<td>$-12.286$</td>
<td>$0.005$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{HH}}^{8-10}$</td>
<td>$-122.532$</td>
<td>$-123.505$</td>
<td>$1.015$</td>
<td>—</td>
<td>$-122.491$</td>
<td>$-0.041$</td>
</tr>
<tr>
<td></td>
<td>$D_{\text{CH}}^{2-8}$</td>
<td>$-1787.037$</td>
<td>$-1935.941$</td>
<td>$148.820$</td>
<td>—</td>
<td>$-1787.120$</td>
<td>$0.083$</td>
</tr>
<tr>
<td></td>
<td colspan="7">$2B = 23.754\ \text{kHz},\ S_{zz}=0.0814$</td>
</tr>
</tbody>
</table>

$^{a}$ All dipolar couplings are in Hz. Data for benzene-$d_1$ were measured at 300 K and for benzene-$d_3$ at 310 K. For the nomenclature used for different contributions to the calculated dipolar couplings see eqn (2.3) and the text thereafter. The anharmonic contributions were included in the analysis by utilising $r_\alpha$-geometry. In the notation $D_{xy}^{i-j}$, $i$ and $j$ refer to atom numbers; carbon atoms are numbered successively from 1 to 6 and the first/only deuterium (atom number 7) is attached to carbon number 1. The rest of the experimental coupling data can be supplied by the authors on request. $^{b}$ $\Delta D$ is the difference between the experimental and the calculated dipolar coupling.

magic mixture (solvent MIX M). These data portray fairly well the experimental data sets in general, although the deforma- tional corrections in some LC solvents, especially for benzene- $d_{1}$ in the LC Phase IV, are somewhat larger than those shown in the table.

## 4. Ab initio calculations
Ab initio calculations of the deuterium quadrupole coupling tensor in $C_{6} H_{5} D$ were carried out for the in vacuo situation using SCF, MP2, CCSD and CCSD(T) wave functions with the quantum-chemical packages DALTON, GAUSSIAN03 $^{50}$ and ACES II. $^{51}$ All estimates of solvent effects and rovibrational corrections were obtained at the SCF level with the DALTON software.

Two kinds of basis sets were used. The initial estimates of electron correlation effects were obtained using the balanced HII (IGLO-II) $^{52,53}$ basis set which is of polarized triple-zeta quality and consists of, in the [primitive/contracted] notation,[9s5p1d/5s4p1d] functions for carbon as well as [5s1p/3s1p] for hydrogen. Both HII and HIII (IGLO-III) $^{52,53}$ were used in the solvent calculations and rovibrational corrections, both best carried out using a balanced basis set definition. The structure of the HIII set is [11s7p2d/7s6p2d] for carbon and [6s2p/4s2p] for hydrogen.

By a uniform-quality basis set, it is difficult to reach a basis- set limit for molecular properties that obtain large contribu- tions from regions close to the atomic nuclei in molecules of the size of benzene. Therefore, a thorough basis set search wascarried out starting from HII, HIII and HIV (IGLO-IV, $^{52,53}$  C:[11s7p3d1f/8s7p3d1f]; H: [6s3p1d/5s3p1d]) basis sets. The final calculations were done using an essentially converged, locally dense $^{54,55}$ basis of 348 spherical Gaussian functions. In locally dense basis sets, the flexibility is very large on the nucleus for which the hyperfine properties are calculated, whereas a smaller basis set-chosen in a controlled fashion-is used for the other parts of the molecule. The final basis set(denoted by "LD" in the following) is close to the SCF-level basis set limit and has the structure [6s6p4d1f/6s6p4d1f] forthe NMR nucleus D, [5s/3s] for H, and [11s7p3d1f/7s6p3d1f] for carbon. The carbon basis is otherwise the HIII set, but with the polarization exponents adopted from the HIV set. The hydrogen basis is HII but with the d function removed. Finally, to obtain a converged basis for D, the HIV set for hydrogen was augmented with three successive sets of tight pd primitives, the exponents of which were obtained by multi- plication of the largest already-existing exponent of the /-shell in question by a factor of three. In this context, the addition of tight s primitives on the resonant nucleus was observed to have a negligible effect. Finally, the LD basis for deuterium was supplemented with an f primitive with exponent 1.397 adoptedfrom the cc-pVQZ set. $^{56}$ 

We carried out calculations at the best available, empiricallycorrected theoretical $r_{e}$ geometry of benzene, where $r_{CC}=$  $1.3914 \AA$ and $r_{CH}=1.0802 \AA,^{47}$ at the zero-point-vibrationally averaged $r_{z}$ geometry for the $C_{6} D_{6}$ isotopomer $(r_{CC}=$  $1.3961 \AA$ and $r_{CD}=1.0837 \AA^{47,57}$ ), and at geometries where one $r_{CD}$ bond length was varied while the other geometricalparameters were kept at their $r_{z}(C_{6} H_{6})$ values $(r_{CC}=1.3964 \AA$  and $r_{CH}=1.0846 \AA^{47,57}$ ).

The rovibrational corrections to the results were obtainedfor the isotopomers $C_{6} H_{5} D, 1,3,5-C_{6} H_{3} D_{3}$ and $C_{6} D_{6}$ at $T=$ 300 K, using the recently implemented theoretical procedure. $^{37}$  The solvent calculations with the SCRF model used a sphe- rical cavity with 13.82 a.u. diameter; large enough to house the benzene molecule, including the van der Waals radii of the hydrogen atoms at the perimeter of the molecule. Dielectric constants of 1.0, 2.0, 4.0, and 8.0 were chosen. This range covers the typical conditions prevailing in LC solutions, as the characteristic structural elements of LC molecules, aliphatic hydrocarbons, cyclohexane, and benzene all have their di- electric constants in this range. The multipolar expansion of the SCRF model was carried out to $l_{max }=10$ .

## 5. Results
### 5.1. Experiments
The results obtained in this study together with previously reported results are listed in Table 2. The experimental results for the DQCCs of benzene- $d_{1}$ and 1,3,5-benzene- $d_{3}$ obtained in the different LCs and at different temperatures are given in Tables 3 and 4, respectively. The experimental error of the DQCC from a single experiment is 1.8 kHz or less. This error is dominated by the reported error margin of the asymmetry parameter $(\eta=0.041 \pm 0.007)$ , which gives rise to an uncertainty of ca. 1.3 kHz in the final result for the DQCC, with the residual 0.5 kHz arising from the actual uncertainty of the NMR measurement. The standard deviations of the average values for DQCCs calculated from all the experimen- tal results for benzene- $d_{1}$ and benzene- $d_{3}$ obtained from the different solvents and at different temperatures are 0.4 kHz and 0.3 kHz, respectively. This is somewhat smaller than the aforementioned 0.5 kHz for a single experiment and also gives a decent estimate of the accuracy of the experimental method itself, excluding the uncertainties of the asymmetry parameter and the geometry.

For a non-hydrogen bonded system (such as in this study) a slight decrease of the DQCC could be expected with increasing temperature due to the anharmonicity of the vibrational potential, but the results obtained at different temperatures merely vary within the error range and no significant systema- tic temperature behavior is detected. The results displayed in Tables 3 and 4 amount to an average of 187.7 kHz for benzene- $d_{1}$ and 187.3 kHz for 1,3,5-benzene- $d_{3}$ , which are essentially the same within the experimental accuracy. If the theoretical MP2 value (vide infra, with rovibrational correc-tions at the SCF level) for the asymmetry parameter $(\eta=$ 0.056) is utilized in the experimental analysis, the correspond- ing numbers are 185.0 kHz and 184.7 kHz, revealing a larger, ca. 5 kHz, deviation from the rovibrationally corrected theo- retical MP2 values of roughly 189.5 kHz, depending slightly on the isotopomer.

It has been stated that the deformation contribution of the observed quadrupolar splitting vanishes at the same concen- tration (of the good mixture) as the deformation contribution of the dipolar couplings. Then, the residual solvent effect arises

<table>
<caption>Table 2 Deuterium quadrupole coupling constant in deuterated benzenes</caption>
<thead>
<tr>
<th>Year</th>
<th>Molecule</th>
<th>Method</th>
<th>DQCC (kHz)</th>
<th>$\eta$</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>1965</td>
<td>C₆D₆</td>
<td>NMR polycrystal</td>
<td>$193 \pm 2.6$</td>
<td>0</td>
<td>9</td>
</tr>
<tr>
<td>1966</td>
<td>C₆D₆</td>
<td>NMR single crystal</td>
<td>$186.6 \pm 1.6$</td>
<td>0</td>
<td>10</td>
</tr>
<tr>
<td>1969</td>
<td>C₆H₅D</td>
<td>LC NMR</td>
<td>$188.4 \pm 1.3^a$</td>
<td>$0.041^a$</td>
<td>2</td>
</tr>
<tr>
<td>1969</td>
<td>C₆D₆</td>
<td>LC NMR</td>
<td>$194 \pm 4$</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td>1972</td>
<td>C₆D₆</td>
<td>LC NMR</td>
<td>$183 \pm 10$</td>
<td>0.06 (assumed)</td>
<td>4</td>
</tr>
<tr>
<td>1972</td>
<td>C₆D₆</td>
<td>NMR polycrystal</td>
<td>$180.7 \pm 1.5$</td>
<td>$0.041 \pm 0.007$</td>
<td>11</td>
</tr>
<tr>
<td>1974</td>
<td>C₆D₆</td>
<td>NMR polycrystal</td>
<td>$193.0 \pm 1.3$</td>
<td>0</td>
<td>12</td>
</tr>
<tr>
<td>1978</td>
<td>1,4-C₆H₄D₂</td>
<td>LC NMR</td>
<td>$190.5 \pm 1.2$</td>
<td>$0.041^b$</td>
<td>5</td>
</tr>
<tr>
<td></td>
<td>1,3,5-C₆H₃D₃</td>
<td>LC NMR</td>
<td>$192.4 \pm 1.2$</td>
<td>$0.041^b$</td>
<td>5</td>
</tr>
<tr>
<td>1978</td>
<td>C₆H₅D</td>
<td>LC NMR</td>
<td>$207.2 \pm 2$</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td>1980</td>
<td>C₆H₅D</td>
<td>LC NMR</td>
<td>$189.6 \pm 2^c$</td>
<td>$0.041^b$</td>
<td>7</td>
</tr>
<tr>
<td>1985</td>
<td>C₆H₅D</td>
<td>MWFT</td>
<td>$223 \pm 12$</td>
<td>—</td>
<td>13</td>
</tr>
<tr>
<td></td>
<td>C₆H₅D</td>
<td>Ab initiocalculation</td>
<td>218.2</td>
<td>0.03</td>
<td>13</td>
</tr>
<tr>
<td>1989</td>
<td>C₆H₅D</td>
<td>MWFT</td>
<td>$186.1 \pm 1.8$</td>
<td>$-0.045 \pm 0.012^d$</td>
<td>14</td>
</tr>
<tr>
<td>1989</td>
<td>Benzene</td>
<td>Ab initio(MP4)</td>
<td>194</td>
<td>0.062</td>
<td>15</td>
</tr>
<tr>
<td>1998</td>
<td>C₆D₆</td>
<td>NMR relaxation</td>
<td>$185 \pm 3$</td>
<td>—</td>
<td>8</td>
</tr>
<tr>
<td>1998</td>
<td>C₆H₅D</td>
<td>B3LYP calculation</td>
<td>192.2</td>
<td>0.056</td>
<td>16</td>
</tr>
<tr>
<td>2006</td>
<td>C₆H₅D</td>
<td>LC NMR</td>
<td>$187.7 \pm 0.4^e$</td>
<td>$0.041^b$</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>1,3,5-C₆H₃D₃</td>
<td>LC NMR</td>
<td>$187.3 \pm 0.3^e$</td>
<td>$0.041^b$</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>C₆H₅D</td>
<td>LC NMR</td>
<td>$185.0 \pm 0.4^e$</td>
<td>$0.056^f$</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>1,3,5-C₆H₃D₃</td>
<td>LC NMR</td>
<td>$184.7 \pm 0.3^e$</td>
<td>$0.056^f$</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>C₆H₅D</td>
<td>Ab initio(SCF/MP2)$^g$</td>
<td>191.60/189.54</td>
<td>0.0662/0.0557</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>1,3,5-C₆H₃D₃</td>
<td>Ab initio(SCF/MP2)$^g$</td>
<td>191.69/189.63</td>
<td>0.0669/0.0564</td>
<td>This study</td>
</tr>
<tr>
<td></td>
<td>C₆D₆</td>
<td>Ab initio(SCF/MP2)$^g$</td>
<td>191.50/189.44</td>
<td>0.0660/0.0555</td>
<td>This study</td>
</tr>
</tbody>
</table>

$^{a}$ Later corrected for $\eta = 0.041$, adopted from ref. 11. $^{b}$ $\eta$ adopted from ref. 11. $^{c}$ Vibrational and asymmetry corrections to the values from ref. 6. $^{d}$ Defined as $(\chi_{yy} - \chi_{xx})/\chi_{zz}$ using the coordinate system defined in the text. $^{e}$ Error margin from one standard deviation of the results obtained in different LC solvents. $^{f}$ Adopted from current ab initiocalculations. $^{g}$ SCF and MP2 calculations using the LD basis (see text) at the $r_e$ geometry, including added SCF/HIII-level rovibrational corrections at 300 K (Tables 5 and 6).

<table>
<caption>Table 3 Experimental results for benzene-$d_1$ $^{a}$</caption>
<thead>
<tr>
<th>Liquid Crystal</th>
<th colspan="5">Phase IV</th>
<th colspan="4">ZLI 2806</th>
<th colspan="2">Phase 1083</th>
<th colspan="2">MIX M$^b$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T$/K</td>
<td>300</td>
<td>310</td>
<td>313</td>
<td>320</td>
<td>330</td>
<td>300</td>
<td>313</td>
<td>323</td>
<td>330</td>
<td>295</td>
<td>300</td>
<td>300</td>
<td>315</td>
</tr>
<tr>
<td>DQCC/kHz</td>
<td>188.0</td>
<td>187.8</td>
<td>187.7</td>
<td>187.8</td>
<td>187.8</td>
<td>187.8</td>
<td>187.4</td>
<td>187.3</td>
<td>187.1</td>
<td>187.4</td>
<td>187.3</td>
<td>187.7</td>
<td>188.6</td>
</tr>
</tbody>
</table>

$^{a}$ Assumed $\eta = 0.041$. $^{b}$ Magicmixture of ZLI 1132 and EBBA liquid crystals (see the experimental section for details).

solely from the external EFG produced by the LC solvents.⁵⁸
According to this, the result obtained from the goodmixture should yield a deformation-free value for the DQCC. In the same study, it was also discovered that the deformation contribution to the EFG is of minor importance compared with the effect on the dipolar couplings. This statement is supported by the results presented here; after considering the vibrational and deformational effects on the dipolar couplings there seems to be negligible remaining influence of the solvent on the experimental quadrupole coupling constant, at least in the systems used in these studies. Essentially the same results are obtained in pure LC solvents as in the goodmixture. On the other hand, the contribution arising from the external EFG produced by the LC solvent also seems to be of minor importance for the systems under investigation, as the experi- mental results from all the solvents yield virtually the same result as the one obtained from the magicmixture, which is used to minimize this effect.

### 5.2. Calculations
Table 5 includes the calculated quadrupole coupling tensor at different correlation levels, at the $r_e$ geometry using the uni- form-quality HII basis set. Electron correlation is observed to decrease both the DQCC and $\eta$. The correlation-induced change is at its largest (DQCC 2.74 kHz below the SCF datum) at the MP2 level, and the coupled-cluster results stabilize at values intermediate to the SCF and MP2 data,

<table>
<caption>Table 4 Experimental results for 1,3,5-benzene-$d_3$$^{a}$</caption>
<thead>
<tr>
<th>Liquid crystal</th>
<th colspan="2">ZLI 2806</th>
<th colspan="2">Phase 1083</th>
<th colspan="3">Phase IV</th>
<th colspan="12">MIX G$^b$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T$/K</td>
<td>300</td>
<td>315</td>
<td>295</td>
<td>300</td>
<td>300</td>
<td>305</td>
<td>310</td>
<td>315</td>
<td>320</td>
<td>295</td>
<td>300</td>
<td>300</td>
<td>305</td>
<td>305</td>
<td>310</td>
<td>315</td>
<td>315</td>
<td>320</td>
<td>325</td>
</tr>
<tr>
<td>DQCC/kHz</td>
<td>187.4</td>
<td>187.3</td>
<td>187.4</td>
<td>187.1</td>
<td>187.7</td>
<td>187.6</td>
<td>187.6</td>
<td>187.6</td>
<td>187.6</td>
<td>186.9</td>
<td>187.3</td>
<td>187.2</td>
<td>187.3</td>
<td>187.3</td>
<td>186.9</td>
<td>187.2</td>
<td>187.3</td>
<td>187.1</td>
<td>187.1</td>
</tr>
</tbody>
</table>

$^{a}$ Assumed $\eta = 0.041$. $^{b}$ Goodmixture of Phase IV and ZLI 1132 liquid crystals (see experimental section for details). Results are from two separate sets of experiments measured on two different NMR spectctrometers.

<table>
<caption>Table 5 Electron correlation, geometry, and basis set effects on the deuterium quadrupole coupling tensor in benzene</caption>
<thead>
<tr>
<th>Method</th>
<th>Geometryª</th>
<th>Basisᵇ</th>
<th>DQCCᶜ/kHz</th>
<th>ηᶜ</th>
</tr>
</thead>
<tbody>
<tr>
<td>SCF</td>
<td>rₑ</td>
<td>HII</td>
<td>222.75</td>
<td>0.0710</td>
</tr>
<tr>
<td></td>
<td>rₑ</td>
<td>HIII</td>
<td>216.91</td>
<td>0.0670</td>
</tr>
<tr>
<td></td>
<td>rₑ</td>
<td>LD</td>
<td>201.30</td>
<td>0.0715</td>
</tr>
<tr>
<td></td>
<td>r_z (C₆D₆)</td>
<td>LD</td>
<td>197.26</td>
<td>0.0726</td>
</tr>
<tr>
<td></td>
<td>r_z (C₆H₆)</td>
<td>LD</td>
<td>196.22</td>
<td>0.0729</td>
</tr>
<tr>
<td>MP2</td>
<td>rₑ</td>
<td>HII</td>
<td>220.01</td>
<td>0.0648</td>
</tr>
<tr>
<td></td>
<td>rₑ</td>
<td>HIII</td>
<td>215.40</td>
<td>0.0562</td>
</tr>
<tr>
<td></td>
<td>rₑ</td>
<td>LD</td>
<td>199.24</td>
<td>0.0610</td>
</tr>
<tr>
<td></td>
<td>r_z (C₆D₆)</td>
<td>LD</td>
<td>195.26</td>
<td>0.0620</td>
</tr>
<tr>
<td></td>
<td>r_z (C₆H₆)</td>
<td>LD</td>
<td>194.24</td>
<td>0.0622</td>
</tr>
<tr>
<td>CCSD</td>
<td>rₑ</td>
<td>HII</td>
<td>220.66</td>
<td>0.0666</td>
</tr>
<tr>
<td></td>
<td>rₑ</td>
<td>HIII</td>
<td>215.91</td>
<td>0.0595</td>
</tr>
<tr>
<td>CCSD(T)</td>
<td>rₑ</td>
<td>HII</td>
<td>220.87</td>
<td>0.0662</td>
</tr>
</tbody>
</table>

$^{a}$ Calculations at the equilibrium geometry ($r_e$) or the zero-point average geometry ($r_z$) of the $C_6D_6$ and $C_6H_6$ isotopomers. $^{b}$ Using the uniform-quality HII/HIII or LD basis sets (see the text). $^{c}$ The DQCC and the asymmetry parameter $\eta$ are defined as in eqn (2.5) and (2.6), respectively.

but closer to the latter. Further calculations using the larger HIII basis set (Table 5) confirm this finding. Hence, MP2 provides the upper limit of the electron correlation effects and will be used in the following.

Also listed in Table 5 are the SCF and MP2 results corresponding to the Locally Dense (LD) basis set that is close to the basis-set-limit for the deuterium quadrupole coupling tensor. The use of the LD basis instead of the HII set is observed to decrease the DQCC by more than 20 kHz at both theoretical levels. The changes of $\eta$ are in opposite directions: at the SCF level it experiences a small increase and at the MP2 level a slightly larger decrease takes place.

Illustrating the sensitivity of the property tensor to the molecular structure, the DQCC obtained at the $r_z$(C₆D₆) geometry is 4 kHz smaller than at the $r_e$ geometry. At the $r_z$(C₆D₆) geometry, the CD bond is elongated by 0.0035 Å in comparison to $r_e$. At the zero-point average geometry corresponding to the $C_6H_6$ isotopomer, the bond length to the resonant deuterium nucleus is further elongated by 0.0009 Å, with DQCC reduced by 1 kHz. The opposite, i.e., increasing trend is observed for the asymmetry parameter.

We next calculated the CD bond length dependence of DQCC and $\eta$ using the LD basis set at both SCF and MP2 levels. The results are displayed in Fig. 1 and 2, respectively. DQCC (the component of the tensor along the C–D bond) decreases linearly due to the extension of $r_{CD}$, both at the SCF and MP2 levels. The opposite trend prevails for the asymmetry parameter. The in-plane principal value of the deuterium quadrupole coupling tensor (perpendicular to the C–D bond in question) is the smallest in magnitude. While electron correlation is seen to decrease the DQCC slightly at all bond lengths, its relative effect is larger for the asymmetry parameter of the tensor, as observed earlier in a related study.²⁹ As MP2 is found to overestimate electron correlation effects (vide supra), the true values are expected to reside between the SCF and MP2 results, close to MP2.

The coincidence of the values calculated with the whole molecule at the $r_z$(C₆D₆) geometry with the linear trend where $r_z$(C₆H₆) was otherwise used but $r_{CD}$ varied, reveals that the quadrupole coupling tensor is expectedly²⁹ only dependent on single geometrical parameter, $r_{CD}$.

![](./images/812036619426070531_1.jpg)

Fig. 1 Calculated DQCC in $C_6H_5D$. Results at the SCF and MP2 levels at estimated⁴⁷,⁵⁷ equilibrium ($r_e$) as well as zero-point average [$r_z$(C₆D₆) and $r_z$(C₆H₆)] geometries, and as a function of the CD bond length while the molecule is otherwise at the $r_z$(C₆H₆) geometry.

The calculated rovibrational effects at the SCF level are given in Table 6. At the rovibrationally-averaged structure corresponding to the temperature in question, $r_\alpha$(300 K), DQCC adopts a value that is 3.5 kHz below that at the $r_e$ geometry corresponding to each basis set. The difference is slightly smaller than between $r_e$ and $r_z$ geometries, due to the fact that the distance between the average positions of the C and attached D nuclei decreases in $r_\alpha$ geometry as compared to $r_z$, due to the thermal excitation of the bending modes involving the D atom. The results at the effective geometry also display small isotopic differences of DQCC of 0.04–0.06 kHz between the calculated isotopomers.

Harmonic corrections on top of the average structure bring a further 6 kHz decrease to the DQCC. There are differences

![](./images/812036619426070531_2.jpg)

Fig. 2 As in Fig. 1, but for the asymmetry parameter $\eta$ of the deuterium quadrupole coupling tensor in $C_6H_5D$.

<table>
<caption>Table 6 Rovibrationally-averaged deuterium quadrupole coupling tensor in isotopomers of benzene at 300 K<sup>a</sup></caption>
<thead>
<tr>
<th colspan="5">Optimized $r_e$ geometry</th>
<th rowspan="2">Isotopomer</th>
<th colspan="2">Effective $r_\alpha$ (300 K) geometry</th>
<th colspan="2">Rovibrationally averaged</th>
<th colspan="2">Change w.r.t. $r_e$</th>
</tr>
<tr>
<th>Basis</th>
<th>$r_{CC}$/Å</th>
<th>$r_{CH}$/Å</th>
<th>DQCC/kHz</th>
<th>$\eta$</th>
<th>DQCC/kHz</th>
<th>$\eta$</th>
<th>DQCC/kHz</th>
<th>$\eta$</th>
<th>$\Delta$DQCC/kHz</th>
<th>$\Delta\eta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>HII</td>
<td>1.3829</td>
<td>1.0747</td>
<td>229.281</td>
<td>0.069 59</td>
<td>C₆H₅D</td>
<td>225.782</td>
<td>0.070 37</td>
<td>219.268</td>
<td>0.063 48</td>
<td>−10.013</td>
<td>−0.006 11</td>
</tr>
<tr>
<td/>
<td/>
<td/>
<td/>
<td/>
<td>1,3,5-C₆H₃D₃</td>
<td>225.819</td>
<td>0.070 33</td>
<td>219.479</td>
<td>0.064 30</td>
<td>−9.802</td>
<td>−0.005 29</td>
</tr>
<tr>
<td/>
<td/>
<td/>
<td/>
<td/>
<td>C₆D₆</td>
<td>225.883</td>
<td>0.070 32</td>
<td>219.397</td>
<td>0.063 82</td>
<td>−9.884</td>
<td>−0.005 77</td>
</tr>
<tr>
<td>HIII</td>
<td>1.3821</td>
<td>1.0725</td>
<td>226.112</td>
<td>0.064 52</td>
<td>C₆H₅D</td>
<td>222.545</td>
<td>0.065 49</td>
<td>216.409</td>
<td>0.059 25</td>
<td>−9.703</td>
<td>−0.005 27</td>
</tr>
<tr>
<td/>
<td/>
<td/>
<td/>
<td/>
<td>1,3,5-C₆H₃D₃</td>
<td>222.580</td>
<td>0.065 46</td>
<td>216.499</td>
<td>0.059 95</td>
<td>−9.613</td>
<td>−0.004 57</td>
</tr>
<tr>
<td/>
<td/>
<td/>
<td/>
<td/>
<td>C₆D₆</td>
<td>222.643</td>
<td>0.065 45</td>
<td>216.313</td>
<td>0.059 01</td>
<td>−9.799</td>
<td>−0.005 51</td>
</tr>
</tbody>
</table>

<sup>a</sup> Calculations at the SCF level.

of 0.1–0.3 kHz in the total rovibrational correction to DQCC between the HII and HIII basis sets. Isotope effects of a magnitude similar to the basis set effect are also observed, but they are just below the experimental detection accuracy in this case. While the anharmonic corrections (accounted for by calculations at the $r_\alpha$ geometry) increase the asymmetry parameter slightly, the harmonic corrections decrease it a lot more. Summarizing, the total rovibrational corrections to the DQCC and $\eta$ at 300 K amount to $-10$ kHz and $-0.006\ldots-0.005$, respectively.

The results of our solvent calculations using the SCRF model are listed in Table 7. The bonds are, as expected, elongated in the solution and the DQCC and $\eta$ experience concomitant decrease and increase, respectively. However, the solvent-induced changes at this level are small enough to render the results completely insignificant for the present purposes of comparing experiment and theory for the DQCC and $\eta$ in benzene. We omit the solvation effects and add the rovibrationally-induced changes, $\Delta$DQCC and $\Delta\eta$ at the SCF/HIII level, on top of the SCF and MP2 values at $r_e$ where the LD basis set was used, and give the final estimate for the quadrupole coupling tensor in vacuo in Table 2.

## 6. Discussion
As seen in the experiments in several different LC solvents described in section 5, consistent values for benzene DQCCs are obtained, averaging at 187.7 and 187.3 kHz for benzene-$d_1$ and 1,3,5-benzene-$d_3$, respectively. This can be seen as an evidence that, after a thorough consideration of vibrational and deformational effects, LC NMR can be valued as a reliable tool to obtain DQCCs. The largest uncertainty of the method arises from the fact that the asymmetry parameter has to be adopted from elsewhere. The reported values of $\eta$ vary from 0.03 to 0.062 (Table 2), which would give rise to an almost 6 kHz difference in the resulting DQCCs were these extreme values used in the experimental analysis. To obtain the aforementioned results, a widely utilized experimental value, $\eta = 0.041$, was adopted from ref. 11.

Compared to calculations performed with standard basis sets at the SCF level and at a fixed optimized geometry corresponding to the in vacuo situation, the use of a locally dense basis set, electron correlation corrections, and rovibrational corrections significantly improves the agreement of theory and experiment for the deuterium quadrupole coupling tensor in benzene. There remains, however, a discrepancy between the theoretical and experimental values, the former overestimating the latter by about 2 kHz. Relativistic effects were not considered in the present modeling but are very likely to be insignificant for the deuterium quadrupole coupling tensor.⁵⁹ While solvent effects considered in the simple reaction field model were found small, specific short-range solvation effects in the LC solution cannot be ruled out. Their inclusion would require dynamic modeling of benzene in LC phases, which would be a rather challenging endeavour given the necessarily large system size in such simulations.

The remaining basis set error of the calculations can be estimated based on the observed changes in the DQCC at the SCF level, when: (1) the tight function space is extended (error remaining at the LD level $-0.28$ kHz or below); (2) the diffuse function space is extended ($+0.32$ kHz or below); (3) more high $l$-type polarization functions are added ($+0.27$ kHz or below); and (4) the locally dense approximation is abandoned ($+0.07$ kHz). As there exists significant error cancellation among the various possible ways of improving the basis set, the total basis set error is likely to be less than 0.5 kHz. This is not negligible, but distinctly below the magnitude of the present gap remaining between the experimental and theoretical results.

The actual geometry in the solution is unknown. Normally, when a molecule is moved from a gaseous to a liquid environment its bonds stretch due to a net attractive interaction with the solvent. This is demonstrated as a downward shift of the vibrational stretching frequencies⁶⁰ and is visible also in the tiny solvent-induced elongation found in our SCRF calculations. From Fig. 1, it can be deduced that an average stretch of

<table>
<caption>Table 7 Calculated solvent-induced changes in the equilibrium bond lengths, DQCC, and the associated asymmetry parameter in benzene<sup>a</sup></caption>
<thead>
<tr>
<th>$\varepsilon_r$</th>
<th>Basis</th>
<th>$\Delta r_{CC}$/$10^{-3}$ Å</th>
<th>$\Delta r_{CH}$/$10^{-3}$ Å</th>
<th>$\Delta$DQCC/kHz</th>
<th>$\Delta\eta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>2.0</td>
<td>HII</td>
<td>0.008</td>
<td>0.001</td>
<td>−0.009</td>
<td>0.00008</td>
</tr>
<tr>
<td/>
<td>HIII</td>
<td>0.007</td>
<td>0.002</td>
<td>−0.010</td>
<td>0.000015</td>
</tr>
<tr>
<td>4.0</td>
<td>HII</td>
<td>0.013</td>
<td>0.002</td>
<td>−0.015</td>
<td>0.000014</td>
</tr>
<tr>
<td/>
<td>HIII</td>
<td>0.012</td>
<td>0.002</td>
<td>−0.016</td>
<td>0.000025</td>
</tr>
<tr>
<td>8.0</td>
<td>HII</td>
<td>0.016</td>
<td>0.002</td>
<td>−0.019</td>
<td>0.000017</td>
</tr>
<tr>
<td/>
<td>HIII</td>
<td>0.015</td>
<td>0.003</td>
<td>−0.020</td>
<td>0.000032</td>
</tr>
</tbody>
</table>

<sup>a</sup> Calculations using the self-consistent reaction field model with the dielectric constant equal to $\varepsilon_r$. The changes are reported relative to the in vacuo values ($\varepsilon_r = 1$), as $\Delta r_{CC} = r_{CC}(r_e$, solvent) $- r_{CC}(r_e$, vacuum) and similarly for the other properties. The in vacuo values at equilibrium geometry are listed in Table 6.

![](./images/812036619426070531_3.jpg)

Fig. 3 The effect of the choice of the $r_{\text{CD}}$ bond length on experimental DQCC in $C_6H_5D$. The results are shown both assuming the experimental asymmetry parameter $\eta = 0.041$ from ref. 11 and $\eta = 0.056$ from the present rovibrationally-corrected MP2 calculations. The dashed line represents the $r_{\text{CD}}$ bond length used in the experimental analysis.

$0.0017\ \text{\AA}$ in the CD bond corresponds to a 1.9 kHz decrease in the calculated DQCC, which would lead to a full agreement of the computational and experimental results. Even a smaller extension of the bond length would converge the calculated and the experimental results within the combined computational and experimental error limits. This indicates the crucial role of the accuracy of the underlying geometry in theoretical calculations, at least when the present level of precision is sought. In this work, the presumably best available theoretical equilibrium geometry for benzene is used for obtaining the $r_e$ results with locally dense basis sets, and rovibrationally-induced changes calculated using lower level methods are then added. We surmise that the most significant sources of error in the current calculations are the selection of the $r_e$ geometry and specific solvation effects, in that order.

As only a relative $r_\alpha$ geometry is obtained from the experimental analysis, it is also useful to consider the influence of the geometry on the experimental results. The effects of the $r_{\text{CD}}$ bond length on the results obtained from the NMR measurements for benzene-$d_1$ are illustrated in Fig. 3. It reveals a trend similar to the one obtained computationally, *i.e.*, a decrease of the DQCC with an increase of the $r_{\text{CD}}$ bond length, although the slope is significantly steeper for the theoretical value. The dashed vertical line shows the value of $r_{\text{CD},\alpha} = 1.0810\ \text{\AA}$ obtained from the experimental analysis of direct dipolar couplings. It is also seen from the figure that a small inaccuracy in the procedure of finding the experimental reference geometry may also contribute significantly to the present deviation of theory and experiment. Finally, the choice of the asymmetry parameter is critical: a change of DQCC of the order of 2 kHz results from switching between two motivated choices of $\eta$.

In conclusion, we have reached an agreement of theory and experiment for the DQCC in benzene to within 2 kHz by careful consideration of various experimental and theoretical factors affecting such comparisons. The remaining discrepancy cannot be attributed to either theoretical or experimental analysis alone, but most likely the choice of the underlying geometrical parameters is responsible. Consequently, when compared to the previously reported results extending over a 42 kHz range, we have substantially narrowed down the possible value of the DQCC in benzene, and also considered the possible remaining sources of error and their effects on the final result.

### Acknowledgements

We are grateful to Prof. J. Gauss for unpublished information related to the work of ref. 47. Dr J. Lounila is acknowledged for the enlightening discussions on the deformation theory and solvent effects. Prof. K. Ruud is thanked for collaboration in developing the rovibrational correction scheme. The authors are grateful to the Academy of Finland (grant 43979, JJ), the national graduate school of 'Computational Chemistry and Molecular Spectroscopy' (AK and SA), the Vilho, Yrjö and Kalle Väisälä Foundation (AK), the Tauno Tönning Foundation (AK), the Emil Aaltonen Foundation (JV), and the Finish Cultural Foundation (JS) for financial support. JV is an Academy Research Fellow of the Academy of Finland and with the Finnish Center of Excellence in Computational Molecular Science (CMS). Computational resources were partially provided by the Center for Scientific Computing, Ltd (CSC, Espoo, Finland).

### References

1 J. W. Emsley, in *Nuclear Magnetic Resonance of Liquid Crystals*, ed. J. W. Emsley, Reidel, Dordrecht, 1985, pp. 379–412.
2 P. Diehl and C. L. Khetrapal, *Can. J. Chem.*, 1969, **47**, 1411.
3 W. J. Caspary, F. Millet, M. Reichback and B. P. Dailey, *J. Chem. Phys.*, 1969, **51**, 623.
4 F. Millet and B. P. Dailey, *J. Chem. Phys.*, 1972, **56**, 3249.
5 P. Diehl and M. Reinhold, *Mol. Phys.*, 1978, **36**, 143.
6 J. B. Wooten, J. Jacobus, A. L. Beyerlein and G. B. Savitsky, *J. Magn. Reson.*, 1978, **31**, 347.
7 K. Seidman, J. F. McKenna, G. B. Savitsky and A. L. Beyerlein, *J. Magn. Reson.*, 1980, **38**, 229.
8 E. H. Hardy, R. Witt, A. Dölle and M. D. Zeidler, *J. Magn. Reson., Ser. A*, 1998, **134**, 300.
9 J. Rowell, W. Phillips, L. Melby and M. Panar, *J. Chem. Phys.*, 1965, **41**, 3442.
10 P. Pyykkö and U. Lähteenmäki, *Ann. Univ. Turku A*, 1966, **88**, 93.
11 R. G. Barnes and J. W. Bloom, *J. Chem. Phys.*, 1972, **57**, 3082.
12 M. Rinné and J. Depireux, in *Advances of Nuclear Quadrupole Resonance*, ed. J. A. S. Smith, Heyden, London, UK, 1974, Vol. 1, p. 357.
13 M. Oldani, T.-K. Ha and A. Bauder, *Chem. Phys. Lett.*, 1985, **115**, 317.
14 S. Jans-Bürli, M. Oldani and A. Bauder, *Mol. Phys.*, 1989, **68**, 1111.
15 S. Gerber and H. Huber, *J. Mol. Spectrosc.*, 1989, **138**, 315.
16 W. C. Bailey, *J. Mol. Spectrosc.*, 1998, **190**, 318.
17 J. Jokisaari, P. Diehl, J. Amrein and E. Ijäs, *J. Magn. Reson.*, 1983, **52**, 193.
18 A. Saupe, *Angew. Chem., Int. Ed. Engl.*, 1968, **7**, 97.
19 J. Lounila and J. Jokisaari, *Prog. Nucl. Magn. Reson. Spectrosc.*, 1982, **15**, 249.
20 S. Sýkora, J. Vogt, H. Bösiger and P. Diehl, *J. Magn. Reson.*, 1979, **36**, 53.
21 J. Lounila, R. Wasser and P. Diehl, *Mol. Phys.*, 1987, **62**, 19.
22 J. Lounila and P. Diehl, *J. Magn. Reson.*, 1984, **56**, 254.
23 J. Lounila and P. Diehl, *Mol. Phys.*, 1984, **52**, 827.
24 J. Lounila, *Mol. Phys.*, 1986, **58**, 897.
25 J. Vaara, J. Jokisaari, R. E. Wasylishen and D. L. Bryce, *Prog. Nucl. Magn. Reson. Spectrosc.*, 2002, **41**, 233.
26 P. Pyykkö, *Mol. Phys.*, 2001, **99**, 1617.
27 H. Huber and P. Diehl, *Mol. Phys.*, 1985, **54**, 725.

28 R. Eggenberger, S. Gerber, H. Huber, D. Searles and M. Welker, *J. Chem. Phys.*, 1992, **97**, 5898.

29 J. Vaara and Y. Hiltunen, *J. Chem. Phys.*, 1997, **107**, 1744.

30 J. Vaara, J. Lounila, K. Ruud and T. Helgaker, *J. Chem. Phys.*, 1998, **109**, 8388.

31 C. J. Jameson, in *Theoretical Models of Chemical Bonding, Part 3. Molecular Spectroscopy, Electronic, Structure and Intramolecular Interactions*, ed. Z. B. Maksic, Springer, Berlin, 1991, p. 457.

32 M. Toyama, T. Oka and Y. Morino, *J. Mol. Spectrosc.*, 1964, **13**, 193.

33 P.-O. Åstrand, K. Ruud and P. R. Taylor, *J. Chem. Phys.*, 2000, **112**, 2655.

34 K. Ruud, P.-O. Åstrand and P. R. Taylor, *J. Chem. Phys.*, 2000, **112**, 2668.

35 T. A. Ruden and K. Ruud, in *Calculation of NMR and EPR Parameters. Theory and Applications*, ed. M. Kaupp, M. Bühl and V. G. Malkin, Wiley, Weinheim, 2004, p. 153.

36 P.-O. Åstrand, K. Ruud and D. Sundholm, *Theor. Chem. Acc.*, 2000, **103**, 365.

37 K. Ruud, J. Lounila and J. Vaara, to be published.

38 DALTON, a molecular electronic structure program, Release 1.2 (2001), written by T. Helgaker, H. J. Aa. Jensen, P. Jørgensen, J. Olsen, K. Ruud, H. Ågren, A. A. Auer, K. L. Bak, V. Bakken, O. Christiansen, S. Coriani, P. Dahle, E. K. Dalskov, T. Enevoldsen, B. Fernandez, C. Hättig, K. Hald, A. Halkier, H. Heiberg, H. Hettema, D. Jonsson, S. Kirpekar, R. Kobayashi, H. Koch, K. V. Mikkelsen, P. Norman, M. J. Packer, T. B. Pedersen, T. A. Ruden, A. Sanchez, T. Saue, S. P. A. Sauer, B. Schimmelpfennig, K. O. Sylvester-Hvid, P. R. Taylor and O. Vahtras.

39 K. V. Mikkelsen, H. Ågren, H. J. Aa. Jensen and T. Helgaker, *J. Chem. Phys.*, 1988, **89**, 3086.

40 P. B. Barker, A. J. Van der Est, E. E. Burnell, G. N. Patey, C. A. de Lange and J. G. Snijders, *Chem. Phys. Lett.*, 1984, **107**, 426.

41 J. Jokisaari, Y. Hiltunen and J. Lounila, *J. Chem. Phys.*, 1986, **85**, 3198.

42 R. Laatikainen, *J. Magn. Reson.*, 1991, **92**, 1.

43 R. Laatikainen, M. Niemitz, U. Weber, J. Sundelin, T. Hassinen and J. Vepsäläinen, *J. Magn. Reson., Ser. A*, 1996, **120**, 1.

44 J. M. Read, Jr, R. E. Mayo and J. H. Goldstein, *J. Mol. Spectrosc.*, 1967, **22**, 419.

45 R. Wasser, M. Kellerhals and P. Diehl, *Magn. Reson. Chem.*, 1989, **27**, 335.

46 L. Goodman, A. G. Ozkabak and S. N. Thakur, *J. Phys. Chem.*, 1991, **95**, 9044.

47 J. Gauss and J. F. Stanton, *J. Phys. Chem. A*, 2000, **104**, 2865.

48 K. Tamagava, T. Iijima and M. Kimura, *J. Mol. Struct.*, 1976, **30**, 243.

49 J. Lounila and P. Diehl, *Mol. Phys.*, 1984, **52**, 827.

50 M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, J. A. Montgomery, Jr, T. Vreven, K. N. Kudin, J. C. Burant, J. M. Millam, S. S. Iyengar, J. Tomasi, V. Barone, B. Mennucci, M. Cossi, G. Scalmani, N. Rega, G. A. Petersson, H. Nakatsuji, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, M. Klene, X. Li, J. E. Knox, H. P. Hratchian, J. B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R. E. Stratmann, O. Yazyev, A. J. Austin, R. Cammi, C. Pomelli, J. W. Ochterski, P. Y. Ayala, K. Morokuma, G. A. Voth, P. Salvador, J. J. Dannenberg, V. G. Zakrzewski, S. Dapprich, A. D. Daniels, M. C. Strain, O. Farkas, D. K. Malick, A. D. Rabuck, K. Raghava- chari, J. B. Foresman, J. V. Ortiz, Q. Cui, A. G. Baboul, S. Clifford, J. Cioslowski, B. B. Stefanov, G. Liu, A. Liashenko, P. Piskorz, I. Komaromi, R. L. Martin, D. J. Fox, T. Keith, M. A. Al-Laham, C. Y. Peng, A. Nanayakkara, M. Challacombe, P. M. W. Gill, B. Johnson, W. Chen, M. W. Wong, C. Gonzalez and J. A. Pople, *GAUSSIAN03 (Revision C.02)*, Gaussian, Inc., Wall- ingford CT, 2004.

51 ACES II is a program product of the Quantum Theory Project, University of Florida. Authors: J. F. Stanton, J. Gauss, J. D. Watts, M. Nooijen, N. Oliphant, S. A. Perera, P. G. Szalay, W. J. Lauderdale, S. A. Kucharski, S. R. Gwaltney, S. Beck, A. Balková, D. E. Bernholdt, K. K. Baeck, P. Rozyczko, H. Sekino, C. Hober and R. J. Bartlett. Integral packages included are VMOL (J. Almlöf and P. R. Taylor); VPROPS (P. R. Taylor) ABACUS; (T. Helgaker, H. J. Aa. Jensen, P. Jørgensen, J. Olsen and P. R. Taylor).

52 S. Huzinaga, *Approximate Atomic Functions*, University of Alberta, Edmonton, 1971.

53 W. Kutzelnigg, U. Fleischer and M. Schindler, in *NMR Basic Principles and Progress* 23, ed. P. Diehl, E. Fluck, H. Guenther, R. Kosfeld and J. Seelig, Springer, Berlin, 1990.

54 D. B. Chesnut and K. D. Moore, *J. Comput. Chem.*, 1985, **10**, 648.

55 D. B. Chesnut, B. E. Rusiloski, K. D. Moore and D. A. Egolf, *J. Comput. Chem.*, 1993, **14**, 1364.

56 T. H. Dunning, Jr, *J. Chem. Phys.*, 1989, **90**, 1007.

57 J. Gauss, private communication.

58 J. Jokisaari and Y. Hiltunen, *J. Magn. Reson.*, 1984, **60**, 307.

59 P. Pyykkö and M. Seth, *Theor. Chem. Acc.*, 1997, **96**, 92.

60 M. R. Zakin and D. R. Herschbach, *J. Chem. Phys.*, 1988, **89**, 2380.
