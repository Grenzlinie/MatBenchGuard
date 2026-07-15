# Ab initio thermodynamics of zirconium hydrides and deuterides

P.A.T. Olsson $^{a,*}$, A.R. Massih $^{a,b}$, J. Blomqvist $^{a}$, A.-M. Alvarez Holston $^{c}$, C. Bjerkén $^{a}$

$^{a}$ Materials Science and Applied Mathematics, Malmö University, SE-205 06 Malmö, Sweden
$^{b}$ Quantum Technologies, Uppsala Science Park, SE-751 83 Uppsala, Sweden
$^{c}$ Studsvik Nuclear AB, Box 556, SE-611 10 Nyköping, Sweden

---

## ARTICLE INFO

**Article history:**
Received 14 October 2013
Received in revised form 17 January 2014
Accepted 22 January 2014
Available online 20 February 2014

**Keywords:**
Zirconium hydrides
Thermodynamics
Elastic constants
Density functional theory

---

## ABSTRACT

We report the results of a systematic *ab initio* study of the elastic and thermodynamic properties of $\gamma$-ZrH, $\delta$-ZrH$_{1.5}$, $\gamma$-ZrD, and $\delta$-ZrD$_{1.5}$. In addition, pure $\alpha$-Zr as well as the $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$ phases are evaluated for reference. The calculations are performed using quantum mechanical density functional theory (DFT) with the frozen core projector augmented wave (PAW) approach and a generalised gradient approximated (GGA) exchange-correlation functional. To capture the variations of the thermodynamic quantities over a wide range of temperatures ($0 \lesssim T \lesssim 1000$ K), the quasi-harmonic approximation approach is adopted where the influence of the vibrational and electronic free energies are included by means of the phonon and electron densities of state. This allows for quantifying the contributions of the electron density of states, which were not accounted for in the previous studies. All the pertinent elastic constants and phonon properties for the considered hydride/deuteride phases are calculated and compared with experimental data; which were not done before. We have further computed the entropy, heat capacity and enthalpy as well as low temperature thermodynamic properties such as the Debye temperature and the electronic heat capacity constant for all the hydride and deuteride phases. The results of our computations concur well with the corresponding data obtained by measurements that are reported in the literature and offer the necessary data and basis for multiscale modelling of zirconium alloys.

© 2014 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Because of their low thermal neutron capture cross section and good corrosion resistance, zirconium-based alloys are commonly used as fuel cladding material in the core of nuclear power reactors. While in service, the fuel cladding is in contact with water, which promotes the oxidation of Zr. This process releases free hydrogen, a portion of which enters the alloy and gives rise to the formation of hydrides once the solid solubility limit has been exceeded. This can have a detrimental effect on the integrity and longevity of the material, as it can lead to phenomena such as embrittlement and delayed hydride cracking [1–3].

The wide use of zirconium alloys in nuclear power reactors has motivated numerous studies on pure zirconium and zirconium hydrides over the past few decades. At low temperatures and pressures zirconium is known to have a hexagonal-close-packed (HCP) structure that is commonly referred to as the $\alpha$-phase. Increasing the temperature to above 1141 K the $\alpha$-phase transforms into the $\beta$-phase, which is a body-centered-cubic (BCC) phase. With respect to hydrides, it is well established that there are two stable phases present in the Zr–H system: the $\delta$- and $\varepsilon$-phases. The $\delta$-phase is a non-stoichiometric phase with a face-centered-cubic (FCC) structure, in which the regular lattice sites are occupied by the zirconium atoms and the tetrahedral interstitial sites are randomly occupied by hydrogen. Depending on the temperature, the hydrogen content of the $\delta$-ZrH$_x$ phase varies in the interval $1.4 < x < 1.7$. Increasing the hydrogen content beyond this upper limit leads to the formation of $\varepsilon$-ZrH$_x$, which is a face-centered-tetragonal (FCT) structure with a unit cell having $c < a$ [4].

There is one more well known phase, the low temperature stoichiometric $\gamma$-ZrH phase which is an FCT structure with $c > a$. However, one question that remains somewhat controversial is the nature of the $\gamma$-phase, which is still debated in the literature whether it is a stable or metastable phase. There are many contradictory experimental findings concerning the $\gamma$-phase and circumstances that complicate the situation, which to this day divides the scientific community. For instance, the $\gamma$-phase is known to be a low temperature phase and there have been reports of the $\delta$ to $\gamma$ transformation having very slow transformation kinetics [5,6]. Moreover, it has been suggested that the $\gamma$-phase is stable only in high purity zirconium, while in lower purity Zr and alloys it is metastable [7]. In addition to the aforementioned hydride phases, recently an additional metastable phase containing small amounts

---

* Corresponding author. Tel.: +46 40 665 86 37.
E-mail address: Par.Olsson@mah.se (P.A.T. Olsson).

http://dx.doi.org/10.1016/j.commatsci.2014.01.043
0927-0256/© 2014 Elsevier B.V. All rights reserved.

of hydrogen was discovered in Zircaloy-4 specimens. This new phase is coined $\zeta$-ZrH$_x$, which is a hexagonal phase having a stoi-chiometry ranging from $x=0.25$ to $x=0.5$; and it is supposedly fully coherent with the $\alpha$-Zr matrix [8].

To explain the stability of the different phase morphologies a great deal of quantum mechanical *ab initio* investigations have been performed to expand the hydride picture. In particular, stoichiometric $\varepsilon$-ZrH$_2$ has been the subject of numerous *ab initio* studies where a great deal of effort has been devoted to study its bistability properties and explain why the structure is FCT and not FCC, despite its symmetry properties. The first study to address these issues was conducted by Ackland [9-11], who found that ZrH$_2$ has two potential equilibrium configurations where one corresponds to $c < a$ and the other to $c > a$. By studying the electron density of states (EDOS), it was further found that the instability of the FCC phase was related to a peak at the Fermi energy level. Subsequent studies [12-14] have confirmed that this is a consequence of multiple degenerate bands at the Fermi level, which give rise to an instability of the cubic phase. Thus, the tetragonal distortion is interpreted as a Jahn-Teller effect driven by the splitting of degenerate bands at the Fermi level [15]. Moreover, it has been found that the potential energy minimum corresponding to $c > a$ is unstable. This has been confirmed through the discovery of imaginary modes in the calculated phonon frequency spectrum and the evaluation of the tetragonal stability criteria, which are violated [14].

Other *ab initio* works dealing with zirconium hydrides include the seminal work by Domain et al. [16] who studied the influence of hydrogen on the electronic properties of zirconium. They reported that in HCP crystal structures, hydrogen atoms preferentially occupy tetrahedral sites, and that the solution energy and relaxation volume are in accord with results obtained from experimental studies. Moreover, they studied the stability and formation energies of $\gamma$-ZrH, $\delta$-ZrH$_{1.5}$ and $\varepsilon$-ZrH$_2$. By varying the lattice parameters, they found that the ZrH$_{1.5}$ phase had three potential energy minima: two tetragonal and one FCC structure. In contrast to experimental data, their results showed that the tetragonal structure corresponding to $c < a$ has the lowest formation energy. They conjectured that these contradicting results were a result of a lack of vibrational energy contributions and that the considered phase was completely ordered, which is not the case in the real hydride.

To supplement experimental measurement, *ab initio* modelling can serve as a useful numerical tool to predict thermodynamic properties. In such calculations the thermal influence can be accounted for by the inclusion of vibrational and electronic free energies based on the full phonon density of states (PHDOS) and the thermal electron excitations derived from the EDOS. These types of calculations, generally called the quasi-harmonic approximation or QHA [17], have previously been found to accurately predict the thermodynamics of the Ni-Al [18-20], Ti-Zr [21] and W-C [22] systems, to name a few. For pure $\alpha$-Zr, Schnell and Albers [23] studied the pressure and thermal influence on the phase stability using DFT. Based on their calculations they managed to roughly estimate parts of the pressure-temperature (P-T) phase diagram. Nie and Xie [24] studied the thermal influence on the lattice parameters and the specific heat. Assuming the validity of QHA and accounting for both electronic excitations and phonon vibrations they managed to reproduce experimental thermodynamic data very accurately. These works have since been extended by different researchers [25-27] with improved accuracy, who have reproduced the P-T phase diagram and the thermodynamic properties with good agreement with the experimental results.

Concerning thermodynamic modelling of hydrides, in a recent publication Chattaraj and co-workers [28] studied the thermal influence on the thermodynamic properties of $\varepsilon$-ZrH$_2$ using quantum mechanical density functional theory (DFT). To capture the isotopic effects they not only considered hydrogen but also deuterium and tritium. In their investigation they studied among other things, the entropy and the specific heat, and obtained good agreement with experimental data despite only including the vibrational free energy from a full phonon calculation, excluding the contribution of thermal electron excitations. In another work, Zhu et al. [29] studied the thermodynamic properties of the $\zeta$-, $\gamma$-, $\delta$- and $\varepsilon$-phases using DFT calculations. Rather than including the full contribution of the complete phonon and electron densities of states, they limited their study to the gamma point phonon frequencies and neglected the contribution of electron excitations in their calculations. In their paper they published a list of lattice parameters for the four hydrides, however, compared with experimental data there is much discrepancy in the reported lattice parameters. They further reported a full set of calculated values of elastic constants for the hydrides. But in the case of $\varepsilon$-ZrH$_2$ at least one other group [14] has published a full set of elastic constants and there is much discrepancy between the two groups' results, despite both using similar DFT methods. Moreover, a third group [28] has calculated the heat capacity for the $\varepsilon$-hydride and their results differ significantly from those of Zhu et al. [29]. This raises questions concerning the accuracy of the approaches taken. These issues are addressed in this paper.

The purpose of this work is to study the thermodynamic and mechanical properties of the $\gamma$-ZrH and $\delta$-ZrH$_{1.5}$ phases using DFT. In order to capture isotope effects on the thermodynamic properties, we also study the deuterium populated phases, i.e. $\gamma$-ZrD and $\delta$-ZrD$_{1.5}$. For the sake of completeness and benchmarking, we also consider pure $\alpha$-Zr as well as the $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$ phases, since there is a plethora of experimental and first principles data available in the literature for those phases that can be used to examine the accuracy of the DFT model. The motivation for this work is twofold: (i) To provide the necessary input data for multi-scale modelling of hydride forming metals in which mechanical properties such as elastic constants, and thermodynamic properties such as electron and vibrational free energy, enthalpy of formation and heat capacity play central roles. Since there is a lack of such data in the literature, we resort to *ab initio* modelling. (ii) To address the aforementioned inconsistent *ab initio* results concerning the mechanical and thermodynamic properties found in the literature. In order to accomplish this, unlike in previous works, we include both full phonon and electron excitation contributions to the free energy to quantify their respective contributions. Throughout the paper we attempt to conduct meticulous comparisons with various experimental data in a wide range of temperatures to ensure the accuracy of our work.

The paper is organised as follows. In the next section we describe the numerical details of the DFT calculations performed, which is followed by an exhaustive exposition of the mechanical and thermodynamic modelling. Thereafter, we present the results of this work in which we first discuss and benchmark the properties of $\alpha$-Zr, hydrogen and deuterium and then provide a thorough analysis of the mechanical, electronic and vibrational properties of the hydrides and, thereafter, an evaluation of their thermodynamic properties. Finally, the paper ends with a short summary of the work and a digest of the key findings.

### 2. Numerical details

All DFT simulations in this work are performed using the QUAN-TUM-ESPRESSO package, which is a plane wave based DFT package [30]. For the electron-ion interaction we have adopted the frozen core projector augmented wave (PAW) approach [31]. For Zr, an electron description in which the $4s^24p^64d^25s^2$ orbitals are explicitly accounted for as valence electrons is employed, while only the $1s^1$ electron is treated for H. The same core description is used to

model H and D. Thus, the only considered difference between H and D is the mass, which plays a central role only in phonon calcu- lations. The exchange correlation functional used was developed by Perdew and Wang (PW91) within the framework of the gener- alised gradient approximation (GGA) [32].

The Brillouin zone quadrature is peformed on gamma point shifted Monkhorst-Pack meshes [33], where the k-point grid den- sity is converged to less than 1 meV with respect to the ground state energy. Thus, for the primitive cells of $\alpha$-Zr, $\gamma$-ZrH, $\delta$-ZrH$_{1.5}$ and $\varepsilon$-ZrH$_2$ we use $18 \times 18 \times 12$, $14 \times 14 \times 14$, $12 \times 12 \times 12$ and $20 \times 20 \times 20$ k-point grids, respectively. Phonon dispersion and PHDOS curves are calculated using the density functional perturba- tion theory approach [34] where the q-point grid was chosen suf- ficiently large to achieve well converged results. When evaluating the EDOS we double the density in each spatial direction such that the number of k-points is increased by a factor of eight.

The kinetic energy cutoff of 80 Ry (1 Ry = 13.6 eV) is used for all structures and simulations and the energy cutoff for the electron density is set to 1280 Ry. In all simulations, with the exception of EDOS simulations, smearing is employed using the Methfessel and Paxton smearing method with a width corresponding to 5 mRy [35]. For EDOS evaluations we use a tetrahedron based method rather than any smearing [36].

The equilibrium lattice parameters of the different phases and equilibrium ionic positions are found by performing geometry optimisations where both the supercell size and shape as well as the ionic positions are allowed to vary. Thus the stress free super- cell with ionic positions and lattice parameters corresponding to potential energy minima at zero temperature are found. Even though the ionic positions are initially positioned at the ideal lat- tice sites, they do display some movement such that their relaxed positions do not necessarily correspond to the ideal positions. The geometry optimisations are considered to be sufficiently con- verged when all the Hellmann-Feynman force components acting on each atom are less than 2.5 meV/Å and the pressure is less than 50 bar.

## 3. Modelling

### 3.1. Elastic properties

The elastic constants in this work are calculated based on the energy expansion in terms of the Green-Lagrange strain tensor, $\epsilon_{ij}$,
$$
E(\epsilon_{ij}, V_0) = E_0(V_0) + V_0\sigma_{ij}\epsilon_{ij} + \frac{V_0}{2}C_{ijkl}\epsilon_{ij}\epsilon_{kl} + \cdots \tag{1}
$$
where $\sigma_{ij}$ and $C_{ijkl}$ are the stress and bulk elastic tensors, respec- tively and $V_0$ is the supercell volume at zero temperature. Roman indices range from 1 to 3 and repeated indices are summed. The components of the Green-Lagrange strain tensor are related to the deformation gradient tensor, $F_{ij}$, via
$$
\epsilon_{ij} = \frac{1}{2}(F_{ki}F_{kj} - \delta_{ij}) \tag{2}
$$
where $\delta_{ij}$ is the Kronecker delta and the deformation gradient is a linear mapping relating the coordinates of the reference configura- tion, $X_i$, to the deformed configuration, $x_i$, i.e. $x_i = F_{ij}X_j$ [37]. Because the energy expansion (1) is based on formation energy rather than free energy and the reference volume corresponds to that at zero temperature, the obtained elastic constants in this work correspond to those at $T=0$ K.

In general, depending on the symmetry of the crystal, the num- ber of independent elastic constants can be reduced. For tetragonal and hexagonal symmetries the number of independent elastic con- stants are reduced to six ($C_{11}$, $C_{12}$, $C_{13}$, $C_{33}$, $C_{44}$ and $C_{66}$ in Voigt notation [38]) and five ($C_{11}$, $C_{12}$, $C_{13}$, $C_{33}$ and $C_{44}$), respectively.

<table><caption>Table 1
Strain combinations for determining the elastic constants of tetragonal and hexagonal crystals. The rightmost column displays the sums of the square term in Eq. (3).</caption>
<thead>
  <tr>
    <th>Strain state</th>
    <th>$A_2$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Tetragonal</td>
    <td></td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = \epsilon_{22} = \epsilon$</td>
    <td>$2(C_{11}+C_{12})$</td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = -\epsilon_{22} = \epsilon$</td>
    <td>$2(C_{11}-C_{12})$</td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = \epsilon_{33} = \epsilon$</td>
    <td>$C_{11}+C_{33}+2C_{13}$</td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = -\epsilon_{33} = \epsilon$</td>
    <td>$C_{11}+C_{33}-2C_{13}$</td>
  </tr>
  <tr>
    <td>$\epsilon_{12} = \epsilon$</td>
    <td>$4C_{66}$</td>
  </tr>
  <tr>
    <td>$\epsilon_{13} = \epsilon$</td>
    <td>$4C_{44}$</td>
  </tr>
  <tr>
    <td>Hexagonal</td>
    <td></td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = \epsilon_{22} = \epsilon$</td>
    <td>$2(C_{11}+C_{12})$</td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = -\epsilon_{22} = \epsilon$</td>
    <td>$2(C_{11}-C_{12})$</td>
  </tr>
  <tr>
    <td>$\epsilon_{11} = \epsilon_{33} = \epsilon$</td>
    <td>$C_{11}+C_{33}+2C_{13}$</td>
  </tr>
  <tr>
    <td>$\epsilon_{33} = \epsilon$</td>
    <td>$C_{33}$</td>
  </tr>
  <tr>
    <td>$\epsilon_{13} = \epsilon$</td>
    <td>$4C_{44}$</td>
  </tr>
</tbody>
</table>

Thus, to calculate the elastic properties of tetragonal and hexago- nal phases, we use the linearly independent strain combinations given in Table 1. For each strain combination, we apply 25 equally spaced strain increments in the range $-0.03 \leqslant \epsilon \leqslant 0.03$, upon which the atoms are allowed to move in order to find the equilib- rium positions for each increment. These are used in fitting to a quartic polynomial
$$
\frac{E(\epsilon, V_0)}{V_0} = A_0 + A_1\epsilon + \frac{A_2}{2}\epsilon^2 + \frac{A_3}{6}\epsilon^3 + \frac{A_4}{24}\epsilon^4 \tag{3}
$$
from which the elastic constants are extracted through the coeffi- cient $A_2$ as indicated in Table 1.

### 3.2. Thermodynamic properties

As mentioned in the introduction, the free energy can be deter- mined by the QHA method using PHDOS and EDOS. Within this model, the Helmholtz free energy can be expressed as
$$
F(T, V_0) = E_0(V_0) + F_{vib}(T, V_0) + F_{el}(T, V_0) \tag{4}
$$
where $E_0$ denotes the ground state formation energy, $F_{vib}$ is the vibrational energy, $F_{el}$ is the electron free energy and the tempera- ture is denoted by $T$. It should be noted that within this model the electron-phonon interaction is neglected. This contribution may become important at very low temperatures ($T \ll \Theta_{\rm D}$, where $\Theta_{\rm D}$ is the Debye temperature [39]).

Within the framework of QHA, the vibrational energy can be calculated from PHDOS, following the relation
$$
\begin{aligned}
F_{vib}(T, V_0) =& \frac{1}{2} \int_0^\infty g(\omega, V_0)\hbar\omega d\omega + k_BT \int_0^\infty g(\omega, V_0) \\
& \times \ln\left[1-\exp\left(-\frac{\hbar\omega}{k_BT}\right)\right] d\omega
\end{aligned} \tag{5}
$$
where $\omega$ represents the phonon frequency, $g(\omega, V_0)$ is the PHDOS, while $k_B$ and $\hbar = h/2\pi$ are the Boltzmann and the Planck constants, respectively [17]. The electron free energy contribution is calculated from EDOS using $F_{el}=E_{el}-TS_{el}$ where
$$
E_{el}(T, V_0) = \int_{-\infty}^\infty n(\varepsilon, V_0)f(\varepsilon, T)\varepsilon d\varepsilon - \int_{-\infty}^{\varepsilon_F} n(\varepsilon, V_0)\varepsilon d\varepsilon \tag{6}
$$
and
$$
\begin{aligned}
S_{el}(T, V_0) =& -k_B \int_{-\infty}^\infty n(\varepsilon, V_0)[f(\varepsilon, T)\ln f(\varepsilon, T) \\
& + (1-f(\varepsilon, T))\ln(1-f(\varepsilon, T))] d\varepsilon
\end{aligned} \tag{7}
$$
where $n(\varepsilon, V_0)$ is the EDOS, $\varepsilon$ is the energy level, $\varepsilon_F$ denotes the Fermi energy and $f(\varepsilon, T)=[\exp[(\varepsilon-\varepsilon_F)/k_BT]+1]^{-1}$ is the Fermi

function [40,41]. The entropy can be deduced from the free energy as $S = -(\partial F/\partial T)_V$, from which the specific heat is obtained via $C_v = T(\partial S/\partial T)_V$. At zero pressure, using the expression for the entropy and the Helmholtz free energy, the enthalpy, $H_m$, is calculated as

$$
\mathrm{H}_{m}\left(T, V_{0}\right)=F\left(T, V_{0}\right)-T\left(\frac{\partial F\left(T, V_{0}\right)}{\partial T}\right)_{V}
\tag{8}
$$

From the enthalpy of the constituents, it is possible to calculate the enthalpy of formation for the considered hydrides and deuterides via the expression

$$
\begin{aligned}
\Delta_{f} \mathrm{H}_{m}\left(T, V_{0}, \mathrm{ZrH}_{x} / \mathrm{D}_{x}\right)=& \mathrm{H}_{m}\left(T, V_{0}, \mathrm{ZrH}_{x} / \mathrm{D}_{x}\right) \\
&-\left[\mathrm{H}_{m}\left(T, V_{0}, \mathrm{Zr}\right)+\frac{x}{2} \mathrm{H}_{m}\left(T, V_{0}, \mathrm{H}_{2} / \mathrm{D}_{2}\right)\right]
\end{aligned}
\tag{9}
$$

If electron-phonon couplings are neglected, in the low temperature limit the specific heat can be approximated as a combination of the linear free electron gas and cubic phonon contributions following the Debye $T^3$-law

$$
C_{v}=\gamma T+\frac{12 \pi^{4}}{5} N k_{B}\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^{3}
\tag{10}
$$

where $\gamma$ is the electron heat capacity constant and $N$ denotes the number of molecular units in the supercell considered [40,41]. For a free electron gas $\gamma_{ideal}=\pi^{2} k_{B}^{2} n(\varepsilon_{F}, V_{0}) / 3$, however, in practical situations the measured value often deviates from the ideal electron gas value [41]. For an account of such deviations the reader is referred to [40].

The Debye temperature can be determined by fitting the heat capacity to Eq. (10) or alternatively by considering the average sound velocity of polycrystalline aggregates. The Debye temperature can be approximated using the relation

$$
\Theta_{\mathrm{D}}=\frac{h}{k_{B}}\left[\frac{3 q}{4 \pi} \frac{N_{A} \rho}{M}\right]^{1 / 3} v_{m}
\tag{11}
$$

where $q$ is the number of atoms in the molecule, $N_A$ is Avogadro's number, $M$ is the molecular mass of the solid, $\rho$ is the density and $v_m$ is the averaged sound velocity [42]. The average sound velocity for an isotropic medium is approximated as

$$
v_{m}=\left(\frac{1}{3}\left[\frac{2}{v_{T}^{3}}+\frac{1}{v_{L}^{3}}\right]\right)^{-1 / 3}
\tag{12}
$$

where $v_L$ and $v_T$ are the longitudinal and transverse sound velocities, respectively [42]. To approximate these quantities we use the relations $v_{L}=\sqrt{(3 B+4 G) / 3 \rho}$ and $v_{T}=\sqrt{G / \rho}$, where $B$ and $G$ are the isotropic Voight-Reuss-Hill (VRH) approximated averages of the bulk and shear moduli, respectively [42,43].

<table>
<caption>Table 2
Data for the energy minimum configuration for $\alpha$-Zr. The lattice parameters $a$ and $c$ are given in Å and the elastic properties are given in GPa. The experimental lattice parameters are from [41] and the elastic constants are from [46] extrapolated to $T=0$ K.</caption>
<thead>
  <tr>
    <th></th>
    <th>$a$</th>
    <th>$c$</th>
    <th>$C_{11}$</th>
    <th>$C_{12}$</th>
    <th>$C_{13}$</th>
    <th>$C_{33}$</th>
    <th>$C_{44}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>DFT</td>
    <td>3.231</td>
    <td>5.171</td>
    <td>148</td>
    <td>62.1</td>
    <td>68.5</td>
    <td>168</td>
    <td>25.3</td>
  </tr>
  <tr>
    <td>Expt.</td>
    <td>3.23</td>
    <td>5.15</td>
    <td>155</td>
    <td>67</td>
    <td>64</td>
    <td>172</td>
    <td>36</td>
  </tr>
</tbody>
</table>

## 4. Results and discussion

### 4.1. Pure zirconium, hydrogen and deuterium

As a reference for the ground state of pure Zr we have performed DFT simulations of $\alpha$-Zr. We have compared the lattice parameters and the elastic constants with those from experimental data. From Table 2, it is clear that the lattice parameters are in

![](./images/813158645071085569_1.jpg)

Fig. 1. (a) Phonon dispersion and PHDOS curves for $\alpha$-Zr. The experimental data are taken from inelastic neutron scattering experiments [44]. (b) Partial and total EDOS curves for $\alpha$-Zr. The energy reference level is chosen as the Fermi energy. (c) Enthalpy versus temperature. The solid line and markers correspond to DFT results and experimental data [45], respectively. (d) Specific heat as a function of temperature. The black curve is the total heat capacity and the red and green curves correspond to the phonon and electron contributions to the total heat capacity, respectively. The markers correspond to experimental data [45].

![](./images/813158645071085569_2.jpg)

Fig. 2. Unit cells for the (a) $\gamma$-hydride, (b) $\delta$-hydride and (c) $\varepsilon$-hydride. The red and green spheres represent Zr and H/D sites, respectively. The figures are generated using the AtomEye software [53]. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

excellent agreement with experimental data; deviations are less than 1%. Evaluating the elastic constants of $\alpha$-Zr, it is found that they are in good agreement with experimental results: $C_{11}$, $C_{12}$, $C_{33}$ and $C_{13}$ are within 10% of experimental data, while $C_{44}$ is underestimated by 30%.

To benchmark the phonon calculations we have compared the phonon dispersion and PHDOS curves of $\alpha$-Zr obtained from the DFT calculations with those from experimental data obtained from inelastic neutron scattering measurements [44]. From Fig. 1, it is seen that the phonon frequencies obtained from DFT are slightly underestimated compared with experimental results. Nevertheless, the general trends of the experimental findings are accounted for by the DFT model and the overall agreement is good. The calculated total and orbital partially resolved EDOS curves for $\alpha$-Zr are shown in Fig. 1(b). Since the density levels are finite at the Fermi energy level for Zr, this implies that there is no band gap between the valence and conduction bands. Thus, it can be concluded that $\alpha$-Zr has metallic conduction properties, as expected, since Zr is a transition metal.

Using the PHDOS and EDOS curves, we have evaluated the enthalpy and the specific heat for $\alpha$-Zr against experimental data in the temperature range from 0 to 500 K. From Fig. 1(c) it is seen that the enthalpy is in excellent agreement with experimental data, however, for the specific heat the DFT results slightly underestimate the experimental data for $T>200$ K. Only a minor part of this deviation can be explained by the fact that we are comparing $C_{v}$ calculated from DFT with $C_{p}$ from experiments. It is known that $C_{p}$ is always larger than $C_{v}$ by a factor $\alpha^{2}BVT$, where $\alpha$ and $B$ are the thermal volume expansion coefficient and the bulk modulus, respectively [47]. Calculating the VRH average of $B$ using the elastic properties in Table 2 it is found that $B=98.6$ GPa which is in good agreement with experimental data (97.5 GPa [48]). Approximating the thermal volume expansion coefficient from experimental data, it is found that $\alpha(T)\approx10.94\times10^{-6}+17.12\times10^{-9}\times T$ [45], which gives $\alpha^{2}BVT\approx0.26$ J/(mol K) at $T=500$ K. Hence the $\alpha^{2}BVT$ factor can only account for about 10% of the underestimation of $C_{p}$. It should be noted that Nie and Xie [24] used DFT and calculated $C_{p}$ using a strain meshing technique with PHDOS evaluations at each lattice parameter increment and obtained a much improved agreement with experiments. This suggests that the anharmonic effects stemming from lattice variations should be accounted for in order to accurately calculate $C_{p}$. Nevertheless, comparing the vibrational heat capacity with the classical Dulong-Petit limit, $C_{v}=3Nk_{B}=24.95$ J/(mol K), it is seen that the calculated value at 500 K, $C_{v,vib}=24.7$ J/(mol K) is in good agreement with that limit [40,41].

For hydrogen isotopes, we have evaluated the equilibrium bond length of hydrogen and deuterium molecules to be 0.742 Å, which is in good agreement with the experimental value of 0.74 Å. Moreover, within the harmonic approximation, we have calculated the vibrational frequency for hydrogen $v_{H-H}$ to be 131.8 THz, which corresponds well with experimental data (124.7 THz), and deuterium $v_{D-D}=93.2$ THz, which is comparable to the experimental value of 89.8 THz [2].

### 4.2. Hydrides

Three hydrides have been studied in this work: $\gamma$-ZrH, $\delta$-ZrH$_{1.5}$ and $\varepsilon$-ZrH$_{2}$. The $\gamma$-hydride is modelled as a FCT lattice with $c>a$.

<table>
<caption>Table 3<br>Data for the lattice parameters and elastic properties for the considered zirconium hydrides. The lattice parameters $a$ and $c$ are given in Åand the elastic constants $C_{ij}$, Young's $E$, bulk $B$ and shear moduli $G$ are given in GPa.</caption>
<thead>
<tr>
<th>
</th>
<th>
$a$
</th>
<th>
$c$
</th>
<th>
$C_{11}$
</th>
<th>
$C_{12}$
</th>
<th>
$C_{13}$
</th>
<th>
$C_{33}$
</th>
<th>
$C_{44}$
</th>
<th>
$C_{66}$
</th>
<th>
$E$
</th>
<th>
$B$
</th>
<th>
$G$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$\gamma$-ZrH
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
This work
</td>
<td>
4.58
</td>
<td>
5.02
</td>
<td>
122
</td>
<td>
116
</td>
<td>
98.0
</td>
<td>
183
</td>
<td>
47.5
</td>
<td>
61.1
</td>
<td>
69.5
</td>
<td>
116
</td>
<td>
25.3
</td>
</tr>
<tr>
<td>
Expt. [4]
</td>
<td>
4.60
</td>
<td>
4.97
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [16]
</td>
<td>
4.58
</td>
<td>
5.04
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [29]
</td>
<td>
4.59
</td>
<td>
4.98
</td>
<td>
128
</td>
<td>
118
</td>
<td>
93.5
</td>
<td>
187
</td>
<td>
54.6
</td>
<td>
64.3
</td>
<td>
117
</td>
<td>
117
</td>
<td>
43.9
</td>
</tr>
<tr>
<td>
$\delta$-ZrH$_{1.5}$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
This work
</td>
<td>
4.77
</td>
<td>
4.80
</td>
<td>
162
</td>
<td>
103
</td>
<td>
109
</td>
<td>
166
</td>
<td>
69.3
</td>
<td>
66.8
</td>
<td>
127
</td>
<td>
126
</td>
<td>
47.7
</td>
</tr>
<tr>
<td>
Expt. [4,54]
</td>
<td>
4.77
</td>
<td>
4.77
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
138
</td>
<td>
125
</td>
<td>
53
</td>
</tr>
<tr>
<td>
DFT [16]
</td>
<td>
4.79
</td>
<td>
4.79
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [29]
</td>
<td>
4.67
</td>
<td>
4.67
</td>
<td>
63.0
</td>
<td>
27.8
</td>
<td>
44.0
</td>
<td>
65.1
</td>
<td>
93.5
</td>
<td>
101
</td>
<td>
130
</td>
<td>
47.0
</td>
<td>
62.5
</td>
</tr>
<tr>
<td>
$\varepsilon$-ZrH$_{2}$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
This work
</td>
<td>
5.01
</td>
<td>
4.42
</td>
<td>
166
</td>
<td>
149
</td>
<td>
109
</td>
<td>
149
</td>
<td>
26.5
</td>
<td>
55.8
</td>
<td>
70.1
</td>
<td>
133
</td>
<td>
24.9
</td>
</tr>
<tr>
<td>
Expt. [4]
</td>
<td>
4.99
</td>
<td>
4.45
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [16]
</td>
<td>
5.01
</td>
<td>
4.44
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [29]
</td>
<td>
4.72
</td>
<td>
4.21
</td>
<td>
102
</td>
<td>
20.4
</td>
<td>
11.4
</td>
<td>
108
</td>
<td>
35.6
</td>
<td>
23.7
</td>
<td>
86.6
</td>
<td>
44.4
</td>
<td>
36.8
</td>
</tr>
<tr>
<td>
DFT [14]
</td>
<td>
5.03
</td>
<td>
4.41
</td>
<td>
166
</td>
<td>
141
</td>
<td>
107
</td>
<td>
145
</td>
<td>
30.5
</td>
<td>
60.6
</td>
<td>
80
</td>
<td>
130
</td>
<td>
29
</td>
</tr>
<tr>
<td>
DFT [13]
</td>
<td>
5.02
</td>
<td>
4.43
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
DFT [12]
</td>
<td>
5.01
</td>
<td>
4.42
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

The zirconium atoms are located at the FCT sites and the hydrogen atoms are situated at the tetrahedral interstitial sites on a {110} plane. The $\varepsilon$-hydride is similar with the exception that all eight tetrahedral interstitial sites are occupied by hydrogen atoms and $c < a$.

The $\delta$-phase is known to have an FCC structure with tetrahedral interstitial sites being randomly occupied by hydrogen. To accurately model such compounds based on first principles, one can employ configurational cluster expansion techniques, cf. for instance [49-52]. However, for simplicity and consistency with the other considered phases in this work, we approximate the $\delta$-phase to be an ordered alloy. Hence, the $\delta$-ZrH$_{1.5}$ hydride is modelled to be a ZrH$_2$ hydride with a hydrogen divacancy. Thus, there are three possible crystal structures: an FCT ZrH$_2$ structure with either a first, second or third nearest neighbour hydrogen divacancy. Investigating the stability of these configurations, it is found that the unit cell with a third nearest neighbour hydride divacancy transforms from cubic to tetragonal with $c < a$. This structure was observed to have the lowest formation energy of the possible structures, as previously found by Domain et al. [16]. Despite this, we choose to model the $\delta$-ZrH$_{1.5}$ hydride with a nearest neighbour hydrogen divacancy since it is found to be very close to cubic in accordance with experimental observations. The unit cells used in the hydride simulations are shown in Fig. 2.

### 4.2.1. Lattice parameters and elastic properties
The resulting equilibrium lattice parameters at zero pressure and temperature from the geometry optimisations and the elastic constants are assembled in Table 3. For all hydrides, it is seen that the lattice parameters are in good agreement with experimental data obtained from X-ray and neutron diffraction measurements [4,54]. Deviations are typically less than 1%. Interestingly, it is found that the $\delta$-hydride deviates slightly from being perfectly cubic. However, the $c/a$ ratio is 1.006, which implies that the deviation from a cubic crystal is insignificant. Comparing with results from other available DFT works on the considered hydrides, it can be seen that there is overall agreement in terms of lattice parameters, with the exceptions of the $\delta$- and $\varepsilon$-hydrides, where it is seen that the lattice parameters of Zhu et al. [29] are underestimated in comparison with experimental data. The lattice parameters obtained by other researchers are in good agreement with our results [12-14,16].

There is a lack of experimental data concerning the elastic properties of zirconium hydrides. The only available data are Young's, bulk and shear moduli for polycrystalline $\delta$-ZrH$_{1.5}$ derived from ultrasonic pulse measurements [54]. To compare our results with existing data, we have approximated the elastic properties of a polycrystalline aggregate using VRH averaging [43]. In Table 3 we have calculated the VRH averages of Young's, shear and bulk moduli for all Zr-H phases. Comparing our results with those of Yamanaka et al. [54] for $\delta$-ZrH$_{1.5}$, it is found that they are in good agreement, cf. Table 3. The calculated polycrystalline averages are typically within 10% of the experimental data. Thus, in light of the fact that the DFT model reproduces experimental data for both $\alpha$-Zr and $\delta$-ZrH$_{1.5}$ accurately, this implies that our approach is reliable.

Comparing our calculated elastic constants with those from other DFT simulations, it is seen that there is good agreement for the $\gamma$-hydride. It is found that the elastic constants deviate less than 10% from one another. Even though the $\gamma$-hydride satisfies the mechanical stability criteria based on the elastic constants [55], it should be emphasised that the difference between $C_{11}$ and $C_{12}$ is rather small, which could imply that the hydride might lose its stability at higher temperatures. For the $\delta$-hydride, there is much discrepancy between our results and those of Zhu et al. [29]. This is believed to be related to the discrepancy in the lattice parameters. The ratio $C_{12}/C_{13}$ is unity for a cubic phase and is found to be 0.95 in our calculations. This reflects the fact the our optimised $\delta$-phase deviates slightly from a perfectly cubic lattice. It is noteworthy to reflect on the fact that the same ratio reported by Zhu et al. [29] is 0.63. For the $\varepsilon$-phase our calculated elastic constants are in good agreement with those of Zhang et al. [14]. Again we emphasise the significant discrepancy compared with the elastic constants of Zhu et al. [29], which is believed to be a consequence of their underestimated lattice parameters.

![](./images/813158645071085569_3.jpg)

Fig. 3. Calculated total and orbital resolved partial EDOS curves for (a) $\gamma$-ZrH, (b) $\delta$-ZrH$_{1.5}$ and (c) $\varepsilon$-ZrH$_2$. The reference energy level is chosen as the Fermi energy, $\varepsilon_F$, for all hydrides.

### 4.2.2. Electronic structure
The calculated total and partially resolved orbital EDOS curves for $\gamma$-ZrH, $\delta$-ZrH$_{1.5}$ and $\varepsilon$-ZrH$_2$ are shown in Fig. 3. The fact that the density is finite at the Fermi energy level suggests that there is no band gap between the valence and conduction bands. Thus all hydrides are believed to have metallic conduction properties, which implies that they remain metallic despite the increased hydrogen content. These findings are in agreement with experimental observations from X-ray photoemission spectroscopy [54,57-59], nuclear magnetic resonance [60,61] and electrical resistivity measurements [62] reported in the literature. Moreover, comparing the total EDOS behaviour for $\varepsilon$-ZrH$_2$ with those from

![](./images/813158645071085569_4.jpg)

Fig. 4. Calculated phonon dispersion and PHDOS curves for (a) $\gamma$-ZrH, (b) $\delta$-ZrH$_{1.5}$, and (c) $\varepsilon$-ZrH$_2$. The Brillouin zone paths and notation are adopted from [56].

![](./images/813158645071085569_5.jpg)

Fig. 5. Calculated phonon dispersion and PHDOS curves for (a) $\gamma$-ZrD, (b) $\delta$-ZrD$_{1.5}$, and (c) $\varepsilon$-ZrD$_2$. The Brillouin zone paths and notation are adopted from [56].

other $ab$ initio works, it can be seen that there is a striking resemblance [10-14].

Common for all hydrides is the presence of a band gap about 3 eV below the Fermi level. This gap has been observed experimentally [54,57,58] as well as in other DFT works [10-14]. Furthermore, experiments have revealed that a hump is centred about -6.5 eV below the Fermi level for $\delta$-hydrides [54,57]. This hump is well represented in the lower end of the energy spectrum of the $\delta$-ZrH$_{1.5}$ in our calculations and is mainly a result of the fact that the hydrogen s-orbital has its major contribution in that region. Above the band gap, the hydrogen contribution only plays a minor role, since the total EDOS curves are dominated by the zirconium d-orbital contributions.

### 4.2.3. Vibrational properties

For an accurate description of the free energy, it is important to calculate the phonon properties of all Zr-H/D phases, since their contributions represent the major part of the free energy as illustrated by Eq. (5). In Figs. 4 and 5 we show the phonon dispersion and PHDOS curves for the considered hydrides and deuterides calculated from DFT, respectively. In all PHDOS curves, it is seen that there is a large band gap in the vibration frequencies. This is a result of the large difference between the mass of Zr and the other constituents. The low end of the frequency spectrum describes the atomic vibrations of Zr atoms and the high frequency regime is a result of the vibrations of hydrogen and deuterium. Comparing the PHDOS curves for $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$, it can be seen that the low end of the frequency spectrum overlaps, while the optical phonon region differs, cf. Fig. 6. This suggests that the Zr atoms vibrate independently of the H and D atoms. Moreover, the PHDOS curves reveal that the hydrogen and deuterium optical frequencies differ by the factor $\sqrt{2}$. This has also been observed in $\varepsilon$-TiH$_2$, which is explained by the atomic mass ratio of deuterium and hydrogen, i.e. $\sqrt{m_{\rm D}/m_{\rm H}} = \sqrt{2}$ [63]. This observation has also been found for the other phases.

Comparing the calculated phonon dispersion curves with experimental data is fruitless because of the lack of such data for zirconium hydrides. However, for the PHDOS curves some qualitative experimental observations concerning the optical

![](./images/813158645071085569_6.jpg)

Fig. 6. Comparison of calculated PHDOS for $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$.

hydrogen/deuterium vibrations can be used to validate our DFT results. For instance, Kolesnikov and co-workers [64,65], studied the optical modes of $\gamma$-ZrH and $\gamma$-ZrD by means of neutron diffraction and inelastic neutron scattering. They reported peaks in the PHDOS in the range 142–156 meV and 103–113 meV, respectively. Comparing with our DFT results in Figs. 4(a) and 5(a), it can be seen that the optical hydrogen and deuterium vibration frequencies range from 141 to 163 meV and 100 to 115 meV, respectively. This suggests that the optical frequency band is accurately described by our DFT calculations. Close examination of Figs. 4(a) and 5(a) reveal that no imaginary frequencies appear for the $\gamma$-phases in the phonon frequency spectrum. This implies that the $\gamma$-structure is not only mechanically stable, but also dynamically stable. Hence, it is concluded that the DFT model does not predict the $\gamma$-structure to be unstable.

For $\delta$-ZrH$_{1.5}$ it is seen that the optical frequency band is separated by a small band gap, the separate bands span 119–132 meV and 137–158 meV, cf. Fig. 4(b). This band gap has not been observed experimentally, however, from total neutron cross section measurements three Gaussian peaks, with varying widths, have been reported at 132, 137 and 151 meV [66]. This demonstrates qualitative agreement with the current DFT results, despite the absence of a doubly banded optical frequency region. The DFT simulations show that the $\varepsilon$-ZrH$_2$ phase has an optical frequency band spanning 123–162 meV, which is in qualitative agreement with neutron scattering measurements [67–69]. Comparing with previous DFT works in which phonon dispersion curves have been produced for the $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$ phases [14,28], it can be seen that there is an overall good agreement. Hence, it is concluded that the PHDOS curves for all hydrides obtained from DFT capture the experimental observations qualitatively and where applicable, the phonon dispersion curves match those from other computational works accurately.

### 4.3. Thermodynamic properties

To obtain a complete description of the thermodynamic properties of the considered hydrides and deuterides, we study the entropy, the heat capacity, the enthalpy and enthalpy of formation. These are properties that can be derived from the Helmholtz free energy once PHDOS and EDOS have been calculated. For benchmarking purposes we compare our results with available experimental data.

#### 4.3.1. Entropy

In Fig. 7, we show the results of how the entropy of the considered hydrides and deuterides vary in the temperature range 0–1000 K. To illustrate the influence of the electronic excitations, we have compared the total entropy (solid curves) and the vibrational entropic contribution (dashed curves), where the difference can be attributed to entropy resulting from electronic excitations. Even though the electronic contribution becomes increasingly important at high temperatures, it is seen that the two curves are only marginally different. The electronic contribution is found to be most significant for the $\gamma$-phase. This is related to the high d-orbital contribution to EDOS at the Fermi level, which is about twice that of the $\varepsilon$ and $\delta$-phases, cf. Fig. 3.

![](./images/813158645071085569_7.jpg)

Fig. 7. Calculated entropy for (a) $\gamma$-ZrH, $\gamma$-ZrD, (b) $\delta$-ZrH$_{1.5}$, $\delta$-ZrD$_{1.5}$, and (c) $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$. The solid curves correspond to the total entropy and the dashed curves correspond to the phonon contribution to the total entropy. The markers represent experimental data from adiabatic calorimetry measurements [68].

Comparing the curves in Fig. 7, it is seen that the deuterides always have a higher entropic content than the hydrides. Nevertheless, below about 200 K the two curves are essentially indistinguishable. This is because the low ends of the phonon frequency spectra, which are dominated by the Zr atom vibrations, overlap. Comparing the entropy calculations for $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$ with experimental data obtained from adiabatic calorimetry measurements, it is seen that there is an excellent agreement [68].

![](./images/813158645071085569_8.jpg)

Fig. 8. Specific heat for (a) $\gamma$-ZrH, $\gamma$-ZrD, (b) $\delta$-ZrH$_{1.5}$, $\delta$-ZrD$_{1.5}$, and (c) $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$. The solid curves correspond to the total specific heat and the dashed curves correspond to the phonon contribution to the total specific heat. The markers represent experimental data of $C_p$ [68,57].

### 4.3.2. Specific heat capacity
One of the properties that we are particularly interested in studying is the heat capacity. In Fig. 8, we show the calculated specific heat for all considered hydrides and deuterides. As for the entropy calculations, we compare the vibrational contribution with the total specific heat to quantify the contribution emanating from electronic excitations. Comparing the two curves for the $\gamma$-hydrides and deuterides, it can be seen that the difference is small, although it increases with increasing temperature. At 1000 K the electronic contribution constitutes about 5-6% of the total heat capacity, which also reflects the findings for the $\delta$-phase. For the $\varepsilon$-phase, this contribution is smaller, of the order of 3%.

Studying the differences between hydrides and deuterides, it is seen that the hydrides always display a lower heat capacity than the deuterides. Hence, the hydrides converge more slowly to the classical Dulong-Petit limit. The ideally calculated values correspond to 49.9, 62.3 and 74.8 J/(mol K) for $\gamma$-, $\delta$- and $\varepsilon$-phases, respectively, which are in good agreement with 49.6, 58.4 and 69.3 J/(mol K) that are obtained from DFT at the temperature 1000 K for the respective deuterides. If the temperature is increased further, the specific heat is found to approach the Dulong-Petit limit.

![](./images/813158645071085569_9.jpg)

Fig. 9. (a) Evaluation of the enthalpy of formation for hydrides of different hydrogen content at room temperature. The solid lines are linear fits and the experimental data are taken from [45]. In (b and c) the thermal influence on the enthalpy change of ZrH$_x$ and ZrD$_x$ where the experimental data are from [68].

Comparing our results with experimental data, it is found that there is excellent agreement for ZrH$_2$ and ZrD$_2$ [68]. It is noted that the experimental data act as upper bounds compared with the DFT results, as one would expect since $C_p$ is measured in the experiments, whereas we have calculated $C_v$. For the $\delta$-phase, the agreement with experimental data is not as good as for the $\varepsilon$-phase. Nevertheless, it is seen that the experimental data are in qualitative agreement with results from DFT where the deviations are typically about 10% [57].

### 4.3.3. Enthalpy
In addition to the entropy and specific heat, we have also studied the enthalpy of formation as a function of the hydrogen content. For all hydrides and deuterides, we have used Eq. (9) for the numerical evaluation where the reference enthalpy level is chosen to correspond to pure $\alpha$-Zr and H$_2$ or D$_2$ gas. In Fig. 9(a), we show the formation enthalpy as a function of the H/D content. It is seen that the DFT calculated data points lie along a straight line through the origin and by fitting them to the relation $\Delta_fH_m(x)=C_{H/D}\cdot x$, where $x$ is the H/D:Zr-ratio, it is found that $C_H=-75.8$ and

$C_{\mathrm{D}}=-78.5 \mathrm{~kJ} / \mathrm{mol}$ for hydrides and deuterides, respectively. The corresponding experimental value is $C_{\mathrm{H}}=-84.4 \mathrm{~kJ} / \mathrm{mol}$ [45], which deviates by about 10% from the DFT result.

We have further studied the enthalpy change for the hydrides and deuterides caused by thermal variations, cf. Fig. 9(b) and (c). For $\varepsilon-\mathrm{ZrH}_{2}$ and $\varepsilon-\mathrm{ZrD}_{2}$ there is an excellent agreement with experimental results [68].

### 4.3.4. The Debye temperature and the electronic heat capacity constant

When calculating the Debye temperature there are two approximate approaches that can be adopted: (i) use Eq. (10) to fit the low temperature regime of the vibrational $C_{v}$-curves in Figs. 1 and 8 or (ii) use the VRH averages and calculate the Debye temperature using Eq. (11). For evaluation purposes, we have employed both methods in this paper. The electronic heat capacity constant, $\gamma$, is determined by fitting the electronic $C_{v}$-curves to a linear function of the temperature, at low temperatures $(T \ll \Theta_{\mathrm{D}})$.

From Table 4 it is seen that the experimental measurements of the Debye temperature for $\alpha$-Zr span the range 271-328 K. If Eq. (10) is used, then we obtain $\Theta_{\mathrm{D}}=277 \mathrm{~K}$ whereas if we use Eq. (11) for a polycrystalline aggregate, we obtain $\Theta_{\mathrm{D}}=273 \mathrm{~K}$. Comparing these results, it is seen that they are almost identical and that they fall within the range of the experimental values. This implies that both approaches can be used with satisfactory results for pure Zr. Likewise, the evaluated electronic heat capacity constant is found to be $2.50 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$, which is in good agreement with available experimental data that range from 2.79 to $3.08 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$ [70-72]. Moreover, this value is in good agreement with the electronic heat capacity for an ideal free electron gas, $\gamma_{\text {ideal }}=2.19 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$. This suggests that the DFT computations predict these data accurately.

Moving our attention to the $\varepsilon$-hydride, it is found that the Debye temperatures, using Eqs. (10) and (11), are 284 K and 339 K, respectively. Compared with $\alpha$-Zr, the difference between these two values is quite significant. Nevertheless, both are in good agreement with the measured value of 311 K and 286 K found from specific heat capacity measurements [68,73]. The same observation can be made for $\varepsilon-\mathrm{ZrD}_{2}$ where the Debye temperatures according to Eqs. (10) and (11) are 282 and 336 K, respectively, which agree well with the experimental data. For the $\delta$-hydride the difference in the Debye temperature between the single crystal phase and the polycrystalline aggregate is quite significant. Based on Eqs. (10) and (11), the results are found to be 343 and 438 K, respectively, where the lower value is in good agreement with the measured value of $\Theta_{\mathrm{D}}=335 \mathrm{~K}$ [57]. For $\delta-\mathrm{ZrD}_{1.5}$, it is seen that the computed Debye temperatures based on DFT are 340 and 434 K when using Eqs. (10) and (11), respectively. These two values act as lower and upper bounds for the experimental value of 366 K [57]. We note that for hydrides and deuterides Eqs. (10) and (11) give quite different values, while they provide almost the same value for $\alpha$-Zr. Though the reason for this difference is not certain, and we do not intend to investigate this further here, it may be due to the large difference in mass of Zr and H/D atoms.

Compared with pure $\alpha$-Zr and the $\gamma$-hydride, it is found that the electronic heat capacity constants of the $\epsilon$- and $\delta$-phases are lower. This is related to the fact that it is ideally proportional to the electron density of states at the Fermi level. Comparing EDOS for the $\delta$- and $\varepsilon$-phases, it is found that they are smaller in magnitude compared with the $\alpha$-Zr and $\gamma$-ZrH, cf. Figs. 1 and 3. This suggests that increasing the hydrogen content leads to a lowering of the electronic heat capacity constant. The calculated electronic heat capacity constant for $\varepsilon-\mathrm{ZrH}_{2}$ and $\varepsilon-\mathrm{ZrD}_{2}, 1.30 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$, is low in comparison with the corresponding experimental values of $4.10 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$ [68] and $2.2 \mathrm{~mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$ [73]. These high experimental values are somewhat surprising in light of the fact that the density level at the Fermi energy is lower than that of pure $\alpha$-Zr. Hence, theoretically the $\varepsilon$-phase should have a lower specific heat capacity constant than $\alpha$-Zr, as predicted by the DFT computations. However, it should be kept in mind that we have neglected the electron-phonon interaction and it is possible that its contribution can influence the results at low temperatures.

Finally, we have evaluated the same properties for the $\gamma$-phases. Because of the lack of experimental data we cannot benchmark our calculations against measurements, however, it is noticed that many observations made for the other hydrides and deuterides can also be made for the $\gamma$-hydrides and deuterides. For instance, for all hydrides and deuterides, it is found that using Eq. (10) gives

<table>
<caption>Table 4<br>Calculated vs. measured thermodynamic data for $\alpha$-Zr, zirconium hydrides and deuterides. The Debye temperature, $\Theta_{\mathrm{D}}$, is given in K, the electronic heat constant, $\gamma$, is given in $\mathrm{mJ} /\left(\mathrm{mol} \mathrm{K}^{2}\right)$, enthalpy of formation, $\Delta_{f} H_{\mathrm{m}}$, is given in $\mathrm{kJ} / \mathrm{mol}$ and the velocities are given in $\mathrm{km} / \mathrm{s}$.</caption>
<thead>
  <tr>
    <th></th>
    <th>$\gamma$</th>
    <th>$\gamma_{ideal}$</th>
    <th>$\Theta_{\mathrm{D}}$ (Eq. (10))</th>
    <th>$\Theta_{\mathrm{D}}$ (Eq. (11))</th>
    <th>$\nu_{T}$</th>
    <th>$\nu_{L}$</th>
    <th>$\nu_{m}$</th>
    <th>$\Delta_{f} H_{\mathrm{m}}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\alpha$-Zr</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>2.50</td>
    <td>2.19</td>
    <td>277</td>
    <td>273</td>
    <td>2.33</td>
    <td>4.74</td>
    <td>2.62</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Expt. [70]</td>
    <td>2.79–2.83</td>
    <td></td>
    <td>291–293</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Expt. [71]</td>
    <td>2.97</td>
    <td></td>
    <td>271</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Expt. [72]</td>
    <td>3.08</td>
    <td></td>
    <td>328.2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\gamma$-ZrH</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>2.33</td>
    <td>2.49</td>
    <td>228</td>
    <td>298</td>
    <td>2.08</td>
    <td>5.07</td>
    <td>2.36</td>
    <td>–75.6</td>
  </tr>
  <tr>
    <td>$\gamma$-ZrD</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>2.33</td>
    <td>2.49</td>
    <td>227</td>
    <td>296</td>
    <td>2.07</td>
    <td>5.04</td>
    <td>2.35</td>
    <td>–81.0</td>
  </tr>
  <tr>
    <td>$\delta$-ZrH$_{1.5}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>1.15</td>
    <td>1.38</td>
    <td>343</td>
    <td>438</td>
    <td>2.91</td>
    <td>5.80</td>
    <td>3.26</td>
    <td>–112</td>
  </tr>
  <tr>
    <td>Expt. [54,45]</td>
    <td></td>
    <td></td>
    <td></td>
    <td>335</td>
    <td>3.04</td>
    <td>5.87</td>
    <td></td>
    <td>–125</td>
  </tr>
  <tr>
    <td>$\delta$-ZrD$_{1.5}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>1.15</td>
    <td>1.37</td>
    <td>340</td>
    <td>434</td>
    <td>2.89</td>
    <td>5.75</td>
    <td>3.24</td>
    <td>–115</td>
  </tr>
  <tr>
    <td>Expt. [54]</td>
    <td></td>
    <td></td>
    <td></td>
    <td>366</td>
    <td>3.34</td>
    <td>5.78</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\varepsilon$-ZrH$_{2}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>1.30</td>
    <td>1.31</td>
    <td>284</td>
    <td>339</td>
    <td>2.11</td>
    <td>5.45</td>
    <td>2.39</td>
    <td>–153</td>
  </tr>
  <tr>
    <td>Expt. [68]</td>
    <td>4.10</td>
    <td></td>
    <td>311</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>–164</td>
  </tr>
  <tr>
    <td>Expt. [73]</td>
    <td>2.2</td>
    <td></td>
    <td>286</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\varepsilon$-ZrD$_{2}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>This work</td>
    <td>1.30</td>
    <td>1.31</td>
    <td>282</td>
    <td>336</td>
    <td>2.09</td>
    <td>5.39</td>
    <td>2.36</td>
    <td>–158</td>
  </tr>
  <tr>
    <td>Expt. [68]</td>
    <td>4.10</td>
    <td></td>
    <td>311</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

a lower estimate of the Debye temperature than using Eq. (11). On all accounts, it is found that the hydrides and deuterides give almost identical approximate values of the Debye temperature.

## 5. Summary and conclusions

In this paper we have studied the mechanical and thermodynamic properties of zirconium hydrides and deuterides through DFT calculations. The results provide input data for multiscale modelling of Zr hydrides. Specific attention is given to the $\delta$- and $\gamma$-phases because of the lack of experimental data and the fact that the mechanical and thermodynamic properties of these phases have not been modelled satisfactory with *ab initio* methods previously. For completeness and benchmarking purposes we have also considered pure $\alpha$-Zr and the $\varepsilon$-phase. The DFT modelling is performed within the frozen core PAW framework and when calculating the thermodynamic properties, we have evaluated the complete phonon dispersion and PHDOS curves as well as the EDOS curves to capture both vibrational and electronic contributions to the Helmholtz free energy.

The DFT approach adopted here is found to predict the lattice parameters of the hydrides satisfactorily per comparison with experiments and other available *ab initio* works. When evaluating the elastic properties of $\alpha$-Zr and $\delta$-ZrH$_{1.5}$, we obtained very good agreement with experimental data, which suggests that our modelling approach is reliable and predicts the elastic properties accurately. Moreover, from the elastic constants of the hydrides, it was found that all the phases considered are mechanically stable. However, for the $\gamma$-phase, it is noted that the difference between $C_{11}$ and $C_{12}$ is very small, which could imply mechanical instabilities at elevated temperatures.

The calculated EDOS curves for all hydrides reproduce experimental results qualitatively and they all exhibit metallic conduction properties, which is in agreement with experimental findings. When evaluating the calculated phonon dispersion and PHDOS curves, the optical high frequency hydrogen/deuterium vibrations agree well with experimental observations. This indicates that the DFT model accurately reproduces the vibrational properties. Furthermore, it is found that all the zirconium hydride and deuteride phases display real phonon modes, which confirm that the considered hydride and deuteride phases are dynamically stable.

Overall, the results concerning thermodynamic properties of hydrides and deuterides correspond well with reported experimental findings. Specifically for $\varepsilon$-ZrH$_2$ and $\varepsilon$-ZrD$_2$, the entropy, enthalpy and specific heat curves are in excellent agreement with available experimental results obtained below room temperature. The calculated specific heats of $\delta$-ZrH$_{1.5}$ and $\delta$-ZrD$_{1.5}$ are found to be low compared with experimental measurements at room temperature and above. However, this discrepancy is typically about 10%, which implies that there is qualitative agreement between calculations and experiments. Likewise, qualitative agreement is obtained when evaluating the enthalpy of formation as a function of the hydrogen content, where the results obtained from DFT calculations underestimate the experimental results by about 10%.

Based on the thermodynamic and elastic properties we have calculated the Debye temperature using two different approximate methods, and from electronic $C_v$-data we have calculated the electronic heat capacity constant. For $\alpha$-Zr these computations are found to reproduce experimental data satisfactory. Despite the fact that the two different approaches for approximating the Debye temperature give rise to different values, qualitative agreement with experimental data is achieved for both the hydrides and deuterides.

## Acknowledgements

This work was supported by the Knowledge Foundation through Grants 2011-0215 and 2013-0022. The simulations were performed using computational resources provided by the Swedish National Infrastructure for Computing (SNIC) at LUNARC, Lund University, at the National Supercomputer Centre (NSC), Linköping University and at the High Performance Computing Center North (HPC2N), Umeå University.

## References

[1] M.P. Puls, The Effect of Hydrogen and Hydrides on the Integrity of Zirconium Alloy Components, Springer, London, 2012.

[2] Y. Fukai, The Metal-Hydrogen System: Basic Bulk Properties, second ed., Springer, London, 2005.

[3] D.O. Northwood, U. Kosasih U, Int. Metals Rev. 28 (1983) 92.

[4] E. Zuzek, J.P. Abriata, A. San-Martin, F.D. Manchester, in: F.D. Manchester (Ed.), Phase Diagrams of Binary Hydrogen Alloys, ASM International, Materials Park, Ohio, 2000, p. 309.

[5] E. Tulk, M. Kerr, M.R. Daymond, J. Nucl. Mater. 425 (2012) 93.

[6] J.H. Root, W.M. Small, D. Khatamian, O.T. Woo, Acta Mater. 51 (2003) 2041.

[7] L. Lanzani, M.J. Ruch, J. Nucl. Mater. 324 (2004) 165.

[8] Z. Zhao, J.-P. Morniroli, A. Legris, A. Ambard, Y. Khin, L. Legras, M. Blat-Yrieix, J. Microsc. 232 (2008) 410.

[9] G.J. Ackland, Phys. Rev. Lett. 80 (1998) 2233.

[10] M. Gupta, Phys. Rev. Lett. 81 (1998) 3300.

[11] G.J. Ackland, Phys. Rev. Lett. 80 (1998) 3301.

[12] W. Wolf, P. Herzig, J. Phys.: Condens. Matter 12 (2000) 4535.

[13] R. Quijano, R. de Coss, D.J. Singh, Phys. Rev. B 80 (2009) 184103.

[14] P. Zhang, B.-T. Wang, C.-H. He, P. Zhang, Comput. Mater. Sci. 50 (2011) 3297.

[15] H.A. Jahn, E. Teller, Proc. Roy. Soc. A 161 (1937) 220.

[16] C. Domain, R. Besson, A. Legris, Acta Mater. 250 (2002) 3513.

[17] S. Baroni, P. Giannozzi, E. Isaev, Rev. Mineral. Geochem. 71 (2010) 39.

[18] Y. Wang, Z.-K. Liu, L.-Q. Chen, Acta Mater. 52 (2004) 2665.

[19] R. Arroyave, D. Shin, Z.-K. Liu, Acta Mater. 53 (2005) 1809.

[20] S.-L. Shang, Y. Wang, D. Kim, Z.-K. Liu, Comput. Mater. Sci. 47 (2010) 1040.

[21] B.-T. Wang, W.-D. Li, P. Zhang, J. Nucl. Mater. 420 (2012) 501.

[22] X.Y. Cheng, J.H. Zhou, X. Xiong, Y. Du, C. Jiang, Comput. Mater. Sci. 59 (2012) 41.

[23] I. Schnell, R.C. Albers, J. Phys.: Condens. Matter 18 (2006) 1483.

[24] Y. Nie, Y. Xie, Phys. Rev. B 75 (2007) 117417.

[25] Y.-J. Hao, L. Zhang, X.-R. Chen, L.-C. Cai, Q. Wu, D. Alfe, Phys. Rev. B 78 (2008) 134101.

[26] C.-E Hu, Z.-Y. Zeng, L. Zhang, X.-R. Chen, L.-C. Cai, Comput. Mater. Sci. 50 (2011) 835.

[27] S. Zhang, X. Zhang, Y. Zhu, S. Zhang, L. Qi, R. Liu, Comput. Mater. Sci. 61 (2012) 42.

[28] D. Chattaraj, S.C. Parida, S. Dash, C. Majumder, Cond-Mat.Mtrl-Sci (2013) arXiv:1305.610 (Eprint).

[29] W. Zhu, R. Wang, G. Shu, P. Wu, H. Xiao, J. Phys. Chem. C 114 (2010) 22361.

[30] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, A. Sclauzero, A.P. Seitsonen, A. Smogunov, P. Umari, R.M. Wentzcovitch, J. Phys.: Condens. Matter 21 (2009) 395502.

[31] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.

[32] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671.

[33] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.

[34] S. Baroni, S. de Gironcoli, A. Dal Corso, P. Giannozzi, Rev. Mod. Phys. 73 (2001) 515.

[35] M. Methfessel, A.T. Paxton, Phys. Rev. B 40 (1989) 3616.

[36] P.E. Blöchl, O. Jepsen, O.K. Andersen, Phys. Rev. B 49 (1994) 16223.

[37] N.S. Ottosen, M. Ristinmaa, The Mechanics of Constitutive Modeling, Elsevier, Heidelberg, 2005.

[38] M.A. Meyers, K.K. Chawla KK, Mechanical Behavior of Materials, Prentice-Hall, Upper Saddle River, NJ, 1999.

[39] G. Grimwall, Thermophysical Properties of Materials, Elsevier, Amsterdam, 1999.

[40] N.W. Ashcroft, N.D. Mermin, Solid State Physics, Thomson Learning, London, 1976.

[41] C. Kittel, Introduction to Solid State Physics, eigth ed., Wiley, Hoboken, NJ, 2005.

[42] O.L. Anderson, J. Phys. Chem. Solids 24 (1963) 909.

[43] J.M.J. den Toonder, J.A.W. van Dommelen, F.P.T. Baaijens, Model. Simul. Mater. Sci. Eng. 7 (1999) 909.

[44] C. Stassis, J. Zarestky, D. Arch, O.D. McMasters, B.N. Harmon, Phys. Rev. B 18 (1978) 2632.

[45] P.L. Brown, E. Curti, B. Grambow, Chemical Thermodynamics of Zirconium, Elsevier, Amsterdam, 2005.

[46] G. Simmons, H. Wang, Single Crystal Elastic Constants and Calculated Aggregate Properties: A Handbook, second ed., M.I.T. Press, Cambridge, MA, 1971.

[47] R.E. Smallman, R.J. Bishop, Modern Physical Metallurgy and Materials Engineering, Butterworth-Heinemann, Amsterdam, 1999.

[48] E.S. Fisher, C.J. Renken, Phys. Rev. 135 (1964) A482.

[49] J.M. Sanchez, F. Ducastelle, D. Gratias, Physica A 128 (1984) 334.

[50] A. van de Walle, G. Ceder, Rev. Mod. Phys. 74 (2002) 11.

[51] A. van de Walle, Nat. Mater. 7 (2008) 455.

[52] D. Lerch, O. Wieckhorst, G.L.W. Hart, R.W. Forcade, S. Müller, Model. Simul. Mater. Sci. Eng. 17 (2009) 055003.

[53] J. Li, Model. Simul. Mater. Sci. Eng. 11 (2003) 173.

[54] S. Yamanaka, Y. Kazuriho, K. Kurosaki, M. Uno, K. Takeda, H. Anada, T. Matsuda, S. Kobayashi, J. Alloys Compd. 330-332 (2002) 99.

[55] R.A. Cowley, Phys. Rev. B 13 (1976) 4877.

[56] W. Setyawan, S. Curtarolo, Comput. Mater. Sci. 49 (2010) 299.

[57] M. Uno, K. Yamada, T. Maruyama, H. Muta, S. Yamanaka, J. Alloys Compd. 366 (2004) 101.

[58] J.H. Weaver, D.J. Peterman, D.T. Peterson, A. Franciosi, Phys. Rev. B 23 (1981) 1692.

[59] D.W. Veal, D.J. Lam, D.G. Westlake, Phys. Rev. B 19 (1979) 2856.

[60] R.C. Bowman, E.L. Venturini, B.D. Craft, A. Attalla, D.B. Sullenger, Phys. Rev. B 27 (1983) 1474.

[61] C. Korn, Phys. Rev. B 28 (1983) 95.

[62] P.W. Bickel, T.G. Berlincourt, Phys. Rev. B 2 (1970) 4807.

[63] C.H. Hu, D.M. Chen, Y.M. Wang, K. Yang, J. Alloys Compd. 450 (2008) 369.

[64] A.I. Kolesnikov, I.O. Bashkin, A.V. Belushkin, E.G. Ponyatovsky, M. Prager, J. Phys.: Condens. Matter 6 (1994) 8989.

[65] A.I. Kolesnikov, A.M. Balagurov, I.O. Bashkin, A.V. Belushkin, E.G. Ponyatovsky, M. Prager, J. Phys.: Condens. Matter 6 (1994) 8977.

[66] S.S. Malik, D.C. Rorer, G. Brunhart, J. Phys. F 14 (1984) 73.

[67] J.G. Couch, O.K. Harling, L.C. Clune, Phys. Rev. B 4 (1971) 2675.

[68] H.E. Flotow, D.W. Osborne, J. Chem. Phys. 34 (1961) 1418.

[69] A.D.B. Woods, B.N. Brockhouse, M. Sakamoto, R.N. Sinclair, in: Inelastic Scattering of Neutrons in Solids and Liquids, IAEA, Vienna, Austria, 1961, p. 487.

[70] G.D. Kneip, J.O. Betterton, J.O. Scarbrough, Phys. Rev. 130 (1963) 1687.

[71] I. Estermann, S.A. Friedberg, J.E. Goldman, Phys. Rev. 87 (1952) 582.

[72] N.M. Wolcott, Philos. Mag. 2 (1957) 1246.

[73] F. Ducastelle, R. Caudron, P. Costa, J. Phys. (Paris) 31 (1970) 57.