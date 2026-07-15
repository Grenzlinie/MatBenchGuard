Journal Pre-proofs

DFT Calculations of the Structural, Electronic, Optical and Vibrational Prop-erties of Anhydrous Orthorhombic L-Threonine Crystals

Roniel L. Araújo, Manoel S. Vasconcelos, Carlos A. Barboza, José X. Lima Neto, Eudenilson L. Albuquerque, Umberto L. Fulco

<table>
  <tr>
    <td>PII:</td>
    <td>S2210-271X(19)30317-2</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.comptc.2019.112621</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>COMPTC 112621</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Computational & Theoretical Chemistry</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>16 August 2019</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>14 October 2019</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>15 October 2019</td>
  </tr>
</table>
![](./images/812720531156500480_1.jpg)

Please cite this article as: R.L. Araújo, M.S. Vasconcelos, C.A. Barboza, J.X. Lima Neto, E.L. Albuquerque, U.L. Fulco, DFT Calculations of the Structural, Electronic, Optical and Vibrational Properties of Anhydrous Orthorhombic L-Threonine Crystals, Computational & Theoretical Chemistry (2019), doi: https://doi.org/10.1016/j.comptc.2019.112621

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier B.V.

# DFT Calculations of the Structural, Electronic, Optical and Vibrational Properties of Anhydrous Orthorhombic L-Threonine Crystals

Roniel L. Araújo${}^{\text{a}}$, Manoel S. Vasconcelos${}^{\text{b}}$, Carlos A. Barboza${}^{\text{c}}$, José X. Lima Neto${}^{\text{c}}$, Eudenilson L. Albuquerque${}^{\text{c}}$, Umberto L. Fulco${}^{\text{c},*}$

${}^{\text{a}}$Departamento de Física Teórica e Experimental, Universidade Federal do Rio Grande do Norte, 59072-970, Natal-RN, Brazil.
${}^{\text{b}}$Escola de Ciências e Tecnologia, Universidade Federal do Rio Grande do Norte, 59072-970, Natal-RN, Brazil.
${}^{\text{c}}$Departamento de Biofísica e Farmacologia, Universidade Federal do Rio Grande do Norte, 59072-970, Natal-RN, Brazil.

---

## Abstract

The structural, electronic, optical, vibrational and thermodynamic properties of the anhydrous orthorhombic L-threonine crystals are investigated by ab initio simulation using a pseudopotential approach within the density functional theory (DFT) method. We have considered both the generalized gradient approximation with dispersion correction (GGA+TS) and the local density approximation (LDA), respectively, as our exchange functionals. Within the GGA+TS calculations, an excellent agreement between the measured X-ray and our theoretical unit cell parameters was obtained, with deviations $\Delta a$, $\Delta b$, $\Delta c$ of -0.08 Å, 0.12 Å, and 0.01 Å, respectively, for an 830 eV cutoff energy. Besides, a direct-band gap E($\Gamma \rightarrow \Gamma$)=5.06 eV, was found in agreement with the experimental 4.96 eV result. The optical properties have been calculated considering [001] as the incidence direction of polarization of the incident light. The normal vibration's modes, the infrared and Raman spectra of L-threonine, as well as the thermodynamic properties were also obtained and analyzed.

**Keywords:** DFT, Anhydrous orthorhombic L-threonine, Electronic properties, Optical properties, Vibrational properties
**2010 MSC:** 00-01, 99-00

---

## 1. Introduction

A large proportion of our cells, muscles, and tissues are composed of amino acids. There are 20 canonical amino acids [1], classified according to the type

---

*Corresponding author
Email address: umbertofulco@gmail.com (Umberto L. Fulco)

Preprint submitted to Computational and Theoretical Chemistry
October 11, 2019

of the central structural functional groups. They also play a key role in the transport and the storage of nutrients, with a great influence on the function of organs, tendons and arteries, being essential for healing wounds and repairing tissue, as well as for the removal of all kinds of waste deposits produced in connection with the metabolism [2].

L-threonine (L-Thr, chemical formula $C_4H_9NO_3$) is one (and the last discovered) of the essential proteinogenic amino acids for humans, being an important component in the protein metabolism chain and contributing to the formation of enzymes and hormones [3, 4]. As an essential amino acid, it needs to be ingested for a healthy, balanced life since their absence or deficiency could trigger intestinal infections, difficulty in absorbing nutrients, and fatty liver [5]. Fortu-nately, most proteins contain threonine, and therefore a deficiency is unlikely. High concentrations of L-Thr are found in the skeletal muscles and the central nervous system, been also used as a partial treatment for mental health and emotional agitation. Its DNA codons are ACT, ACC, ACA, and ACG.

L-threonine is a polar amino acid with a crystalline state in the zwitterionic form, arising from the transfer of a proton from the carboxyl to the amino group, whose stabilization in the condensed phases is essentially due to the dipole interaction and intermolecular hydrogen bonds. It presents nonlinear optical properties [6] and two chiral centers in the carbons C2 and C3, the former being an alpha carbon atom bonded to the amino group, the carboxyl group, and the side chain, while the latter is located in the side chain. The nonlinear amino acids have particular characteristics such as the molecular chirality and great transparency in the visible and ultra-violet regions [7, 8].

Recently, there are efforts to employ amino acid molecules and crystals in biosensors and optoelectronic devices [9]. The possibility of using C60-derived nanobaskets bonded to L-alanine was presented by dos Santos *et al.* [10]. As far as the crystalline L-serine form is a concern, studies related to its electronic (band structure, density of states) and optical absorption properties were calculated to explain the light absorption measured at room temperature [11]. The role of water on the monohydrated L-aspartic acid crystal, as well the investigation of its phonon-related properties considering its monoclinic $P2_1$ phase through Raman and infrared spectroscopy were also discussed recently [12, 13]. Furthermore, biomolecules such as medicinal drugs used for a varied of diseases including cancer, forming molecular crystals stabilized by hydrogen bonds, van der Waals interactions, and dipolar electrostatic interactions (known as salt bridges) were recently investigated [14]. Notwithstanding the interest in molecular crystals remained focused mainly on the characterization of their polymorphism, for instance, nuclear magnetic resonance, and electron paramagnetic resonance spectroscopies, very useful in the pharmaceutical domain, few relevant information are being released about their electronic, spintronic and optoelectronic properties. The use of computer simulation to overcome this problem by using a quantum chemistry methodology has imposed stringent limits, as stated by Tulip and Clark [15]. However, advances in computer hardware and more efficient density functional theory (DFT) codes are allowing the simulation of increasingly complex systems [16, 17, 18, 19]. Recent works by Oda and

Nakayama [20, 21], as well as Stroscio and Dutta [22] proposed new types of biodevices tailored by man-made biological molecules nanostructures.

Despite its relevance, however, only few amino acid crystals had their optoelectronic properties measured so far, with results suggesting that some of them are wide band gap semiconductors, while others could be small band gap insulators [15, 23, 24]. It was also demonstrated, by using a DFT framework, that anhydrous crystals of the DNA bases present a wide band gap semiconductor aspect [25]. Thus, it is of paramount importance to understand these fundamental physical aspects of the amino acids looking for the development of sustainable bio-organic electronic and optoelectronic devices [26].

The crystal structure of L-threonine in the room temperature was determined originally by Shoemaker *et al.* in 1950 [27] through X-ray diffraction. However, due to the lack of information on the geometry of hydrogen bonds, as well as the location of the hydrogen atoms, Janczak *et al.* [28] re-determined its crystal structure at a temperature equal to 12 K, also using X-ray diffraction technique, finding an orthorhombic crystalline structure composed by four molecules per unit cell (68 atoms), whose space group is $P2_12_12_1$. Its lattice parameters (angles) of the unit cell were: $a$=13.63 Å, $b$=7.62 Å, and $c$=5.11 Å($\alpha=\beta=\gamma=90^\circ$), giving a unit cell volume equal to 530.5 Å$^3$.

The L-threonine zwitterionic molecule is depicted in Fig. 1(a), while the orthorhombic unit cell of anhydrous L-threonine crystals is shown in Fig. 1(b). Observe the absence of water molecules. Parallel layers of L-threonine molecules can be distinguished, connected through hydrogen bonds occurring between the charged groups ($\text{COO}^-$, $\text{NH}_3^+$ and $\text{COO}$), as can be inferred from Fig. 1(c). Finally, a perspective view of the supercell of L-threonine orthorhombic crystal is shown in Fig. 1(d).

In this work, we intend to present a pseudopotential approach within the density functional theory computations by using the local-density approximation (LDA) and the generalized gradient approximation with scatter correction (GGA+TS), to investigate the structural, electronic, optical, vibrational, and thermodynamic properties of L-threonine anhydrous crystals. The electronic (band structure and density of states) and optical absorption properties were discussed to interpret the calculated light absorption performed at room temperature. The real and imaginary parts of the dielectric function are also presented, as well as the absorption spectrum, refractive index, conductivity, reflectivity, and loss function. The infrared and Raman spectra of L-threonine were also obtained and their normal modes assigned. Our motivation was to study the amino acid L-threonine in an attempt to understand how electrostatic effects, hydrogen bonds, and dispersive interactions affect lattice motion.

## 2. Materials and Methods
### 2.1. Crystal Structures and DFT Computational Approach

Lattice parameters, angles, and atomic positions of L-threonine orthorhombic unit cell obtained by Janczak *et al.* [28] were fully taken into account to


![](./images/812720531156500480_2.jpg)

Figure 1: (color online) The L-threonine orthorhombic crystal structure: (a) its molecular structure in the zwitterionic form; (b) the unit cell; (c) parallel layers connected by hydrogen bonds; (d) a perspective view.

prepare the input structure, and the CASTEP code (version 6.0) was used to perform the DFT calculations [29]. Two exchange-correlation functionals were

adopted for almost all steps of simulation: the local density approximation (LDA) exchange-correlation functional developed by Ceperley-Alder-Perdew-Zunger [30, 31] (CAPZ), and the Perdew-Burke-Ernzerhof (PBE) [32] generalized gradient approximation (GGA). We have chosen these two exchange-correlation functionals over hybrid methods due to a two-fold arguments: i) it shows a good performance for non-covalently bound systems, and ii) it is robust and mainly proposed as a quantum efficient and accurate chemical method for large systems where the forces of dispersion are of great importance. For instance, they were already used in a number of nanomaterial-ligand systems [33], as well as in the evaluation of a large number of data sets proposed by *Li et al.*, presenting a best performance over some of the hybrid methods applied in their work, including the largely used hybrid functional B3LYP [34]. Besides, taking into account the good comparison with experimental data, we see no reason to increase the computational cost without a comparable gain.

In order to improve the description of non-covalent interactions in GGA-PBE calculations, the Tkatchenko and Scheffler semi-empirical dispersion correction scheme was applied (GGA+TS) [35]. To replace the core electrons in each atomic species, we adopted norm-conserving pseudopotentials [36] for both LDA and GGA+TS calculations. The valence electronic configurations considered were O - $2s^22p^4$, N - $2s^22p^3$, C - $2s^22p^2$ and H - $1s^1$. A plane-wave basis set was adopted to represent the Kohn-Sham orbitals, with cutoff energy chosen, after convergence studies, to be 830 eV, and Monkhorst-Pack [37] grid was fixed in $1 \times 2 \times 3$ for the Brillouin zone to perform reciprocal space integrations.

By searching for a minimum total energy, the L-threonine structure was optimized through a plane-wave DFT calculation by using both LDA and GGA+TS functionals [38, 39, 40]. The optimization of the geometry was obtained considering a tolerance of $0.5 \times 10^{-6}$ eV/atom for the self-consistency calculations. Besides, the following convergence thresholds along successive self-consistent steps were adopted: total energy change smaller than $5{\times}10^{-6}$ eV/atom, maximum force per atom below $0.01$ eV/Å, pressure smaller than 0.02 GPa, and maximum atomic displacement below $0.5{\times}10^{-3}$ Å. These parameters were also applied to perform further calculations.

After obtaining the geometries optimization, we evaluated the Kohn-Sham electronic band structure and the density of states (total and partial per orbital and per atom), as well as the dielectric function, the optical absorption, the refractive index, the optical conductivity and loss function for light polarized along the [001] crystal direction, following Refs. [41, 42]. The optical and electronic properties of the L-threonine crystal were individually obtained for both LDA (from LDA optimized structure) and GGA+TS (from GGA one) functionals, adopting a cutoff energy of 830 eV. On the other hand, infrared (IR) and Raman properties were calculated only by the GGA+TS functional, adopting a cutoff of 1000 eV. Similarly, we adopt a cutoff energy of 1000 eV for thermodynamic calculations, as well as a k-point set of $2{\times}2{\times}3$.

## 3. Results and Discussion

### 3.1. Unit Cell Optimization

The optimized lattice and volume parameters, as calculated with the functionals LDA and GGA+TS, are shown in Table I. For the sake of comparison, the experimental values of the parameters measured by Janczak *et al.* [28] are also included. In the LDA approximation, where the values found are generally smaller than the experimental ones, the lattice parameter $a$ ($b$) ($c$) showed a decrease of $0.51$ Å, ($1.14$ Å) ($0.35$ Å), which corresponds to $3.73\%$, ($14.95\%$) ($6.75\%$) of the experimental result. The volume obtained was $405.17$ Å$^3$, less $23.62\%$ than the experimental one. The differences in the lattice parameters are caused by an overestimation of the forces between the atoms, causing a decrease in the lengths of the connections and volume of the crystal. On the other hand, values of lattice parameters were obtained closer to the experimental one when the functional GGA+TS was applied, although an increase of the volume estimate was found. The margin of error found for the lattice parameters $a$, $b$ and $c$ were $0.61\%$, $1.59\%$, and $0.18\%$ respectively. The volume obtained was $536.76$ Å$^3$, higher $1.18\%$ than the experimental one. Unlike the LDA functional, the application of the GGA+TS for geometry optimization usually provides higher values than the experimental data, since it underestimates the forces of interatomic connections, causing an increase in the length of the connections. These results show that the GGA functional corrected with the TS dispersion scheme was significantly better than the LDA functional.

<table>
<caption>Table 1: Unit cell lattice parameters (in Å) and volume V (in Å$^3$) of the orthorhombic L-threonine crystal obtained with the functionals LDA and GGA + TS levels for a 830 eV cutoff energy. Their deviations $\Delta$ from the experimental values of Janczak *et al.* [28] are also shown.</caption>
<thead>
<tr>
<th>approximation</th>
<th>$a$(Å)</th>
<th>$\Delta a$(Å)</th>
<th>$b$(Å)</th>
<th>$\Delta b$(Å)</th>
<th>$c$(Å)</th>
<th>$\Delta c$(Å)</th>
<th>$V$(Å$^3$)</th>
<th>$\Delta V$(Å$^3$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>LDA</td>
<td>13.120</td>
<td>-0.508</td>
<td>6.479</td>
<td>-1.139</td>
<td>4.765</td>
<td>-0.345</td>
<td>405.174</td>
<td>-125.326</td>
</tr>
<tr>
<td>GGA+TS</td>
<td>13.545</td>
<td>-0.083</td>
<td>7.739</td>
<td>0.121</td>
<td>5.119</td>
<td>0.009</td>
<td>536.759</td>
<td>6.259</td>
</tr>
<tr>
<td>Experimental</td>
<td>13.628(2)</td>
<td>—</td>
<td>7.618(1)</td>
<td>—</td>
<td>5.110(1)</td>
<td>—</td>
<td>530.5(1)</td>
<td>—</td>
</tr>
</tbody>
</table>

In order to better describe the structure of the L-threonine crystal, we also calculate the dielectric function, the optical absorption, the refractive index, the optical conductivity, and the polarized light loss function incident on a polycrystalline sample, using the same functionals as before, as described in the following text.

### 3.2. Electronic and Optical Properties

In order to understand better the electronic states at the valence and conduction band of the L-threonine orthorhombic crystal structure, we determine in this section the Kohn-Sham electronic band structure as an image of the electronic self-energies $E(k)$, $k$ being a wave vector in the first Brillouin zone

(BZ). Points of high symmetry were selected in the reciprocal space forming a path within the Brillouin zone of the orthorhombic L-threonine crystal, namely: $\Gamma(0,0,0)$, $Y(-1/2,0,0)$, $T(-1/2,0,1/2)$, $Z(0,0,1/2)$, $S(-1/2,1/2,0)$, $X(0,1/2,0)$, $U(0,1/2,1/2)$ and $R(-1/2,1/2,1/2)$.

The CASTEP code was employed to achieve the band structure characteristics of the orthorhombic L-threonine crystal using the exchange and correlation functionals GGA+TS and LDA, respectively. To do that, a plane wave basis set and atomic pseudopotentials were employed, as described in the previous section, allowing one to easily improve the quality of the calculations without concern with a typical basis set superposition errors found in other codes for dissociation energy estimations. Figure 2 (left) depicts the Kohn-Sham electronic band structures, together with the respective partial density of states (PDOS) per orbital (right), of the orthorhombic L-threonine crystal near its main band gaps. Energy values were defined to ensure that the highest energy for a valence electron is equal to zero eV. At the top of Figs. 2a and 2b, we have plotted the GGA+TS and the LDA contributions, respectively, to the energy bands within the range from -22.5 to 12.5 eV, and defining bands whose features are assigned to specific $s$ and $p$ atomic orbitals. For both contributions, the upper valence bands are dominated by the orbital $p$ states, while the deepest one is mainly due to the $s$ atomic orbitals. Furthermore, the bottom of the conduction band has a strong $p$-like in character, although the levels above have similar contributions from the $s$ and $p$ atomic orbitals.

The bottom of Figs. 2a and 2b show a zoom of the region of the energy gap, separating the conduction band from the valence band. For the GGA+TS contribution, one can see a direct gap of 5.06 eV formed between the $\Gamma$ point in the valence band and the $\Gamma$ point in the conduction band, indicating a good agreement with the experimental 4.96 eV result [43]. On the other hand, for the LDA functional, it was observed four indirect gaps ranging from 4.91 to 5.0 eV. The smallest indirect gap (4.91 eV) is between the X point of the valence band and the S point of the conduction band, 2.97% smaller than those found for the functional GGA+TS. These results indicate that the orthorhombic L-threonine crystal resembles a wide gap semiconductor. It is worth noting that previous analysis of other amino acid crystals shown similar behavior. By studying the monoclinic crystal of glycine, it was obtained, through DFT calculations (experimentally estimated), a band gap of 4.95 eV (5.11 eV) [44]. Likewise, the calculated monoclinic aspartic acid band gap was 4.54 eV (5.02 eV), while the evaluation of the L-serine crystal shown a band gap of 4.75 eV (5.90 eV) [45, 46]. All of these structures also presented a wide gap semiconductor behavior, such as the L-threonine evaluated in this work. On the other hand, calculations of orthorhombic crystal of proline and cysteine, as well as the monoclinic crystal of cysteine have presented a band gap of 5.50 eV (experimental gap of 5.54 eV), 4.52 eV (experimental gap of 4.62 eV) and 4.06 eV, respectively, with cysteine shown a small gap insulators behavior [47, 48].

Notwithstanding their qualitative agreements, the GGA+TS and LDA approaches predict band structures with some differences in the calculated energy band gaps of the L-threonine crystal, the most notable one being the predic-

![](./images/812720531156500480_3.jpg)

Figure 2: (color online) Electronic band structures (left) and the respective partial density of states (PDOS) per orbital (right) of the orthorhombic L-threonine crystal along high symmetry directions in the Brillouin zones: (a) the GGA+TS, and (b) the LDA exchange-correlation functionals.

tion of a direct band gap of 5.06eV for the former, and four indirect band gaps ranging from 4.91 to 5.0 eV for the latter. It is then necessary a further in- vestigation, now considering its optical properties, helping us to obtain a clear concept about its electronic structure.

To do that, let us consider different photons energies to calculated some optical properties of the anhydrous orthorhombic L-threonine crystal, starting with the complex frequency-dependent dielectric function, $\varepsilon(\omega)=\varepsilon_{1}(\omega)+i \varepsilon_{2}(\omega)$, for the incident light polarized along the direction [001]. The dielectric function, $\varepsilon(\omega)$, is a fundamental optical parameter that describes the absorption and polarization properties of the material, where $\varepsilon_{1}(\omega)$ and $\varepsilon_{2}(\omega)$ are respectively the real and imaginary part of the dielectric function. It is plotted in Fig. 3a,

for the GGA+TS functional (left panel) and the LDA approach (right panel).
The imaginary part $\varepsilon_{2}(\omega)$ of the dielectric function $\varepsilon(\omega)$ (shown as a solid red
line in Fig. 3) can be obtained from the momentum matrix elements between
the occupied and unoccupied electronic states, which is given by [49]:

$$
\varepsilon_{2}(\omega)=\frac{2 e^{2} \pi}{V \varepsilon_{0}} \sum_{k, v, c}\left|\left\langle\psi_{k}^{c}|\mathbf{u} \cdot \mathbf{r}| \psi_{k}^{v}\right\rangle\right|^{2} \delta\left(E_{k}^{c}-E_{k}^{v}-\hbar \omega\right), \quad(1)
$$

where $\mathbf{u}$ is the vector that provides the polarization of the electric field of the
incident electromagnetic radiation, $V$ is the volume of the unit cell, $e$ is the
electronic charge, and $\psi_{k}^{v}$ ($\psi_{k}^{c}$) represents the wave function of the valence (con-
duction) band at the wavevector $k$. On the other hand, the real part $\varepsilon_{1}(\omega)$ of
the dielectric function $\varepsilon(\omega)$ (shown as a solid black line in Fig. 3) is calculated
from the imaginary part of $\varepsilon_{2}(\omega)$ according to Kramers-Kronig relations [50]:

$$
\varepsilon_{1}(\omega)=1+\frac{2}{\pi} P \int_{0}^{\infty} \frac{\omega^{\prime} \varepsilon_{2}\left(\omega^{\prime}\right) d \omega^{\prime}}{\left(\omega^{\prime 2}-\omega^{2}\right)}, \quad(2)
$$

where $P$ represents the principle value of the integral.

The dielectric constant $\varepsilon_{1}(0)$ was found to be 2.33 for GGA+TS functional
and 2.87 for the LDA one. For energies above $20 \mathrm{eV}, \varepsilon_{2}(\omega) \rightarrow 0$, while $\varepsilon_{1}(\omega \rightarrow \infty)$
is 0.84 for GGA+TS and 0.78 for LDA.

Through $\varepsilon_{1}(\omega)$ and $\varepsilon_{2}(\omega)$ it is possible obtain all other optical properties,
including the refractive index $n(\omega)$, optical conductivity $\sigma(\omega)$, absorption coef-
ficient $\alpha(\omega)$, reflectivity $R(\omega)$ and loss function $L(\omega)$ by the following equations
[41,42]:

$$
n(\omega)=\frac{1}{\sqrt{2}}\left[\sqrt{\varepsilon_{1}^{2}(\omega)+\varepsilon_{2}^{2}(\omega)}+\varepsilon_{1}(\omega)\right]^{\frac{1}{2}} \quad(3)
$$

$$
\sigma(\omega)=\frac{\omega \varepsilon_{2}}{4 \pi} \quad(4)
$$

$$
\alpha(\omega)=\sqrt{2} \omega\left[\sqrt{\varepsilon_{1}^{2}(\omega)+\varepsilon_{2}^{2}(\omega)}-\varepsilon_{1}(\omega)\right]^{\frac{1}{2}} \quad(5)
$$

$$
R(\omega)=\left|\frac{\sqrt{\varepsilon(\omega)}-1}{\sqrt{\varepsilon(\omega)}+1}\right|^{2} \quad(6)
$$

$$
L(\omega)=\frac{\varepsilon_{2}(\omega)}{\varepsilon_{1}^{2}(\omega)+\varepsilon_{2}^{2}(\omega)} \quad(7)
$$

![](./images/812720531156500480_4.jpg)

Figure 3: (color online) Real (solid black line) and imaginary (solid red line) components of the calculated a) dielectric function; b) refractive index; c) optical conductivity of the orthorhombic L-threonine crystal along the direction [001]. (inset) Close-up of the optical conductivity near to the main band gaps of the structures. Left panel: GGA + TS functional; Right panel: LDA functional.

The refractive index $n$ is a dimensionless complex number that describes how light or other radiation propagates through the medium. Its plot is shown

in Fig. 3b along the direction [001] of the L-threonine crystal. The refractive index $n(0)$ is 1.52 (GGA+TS) and 1.69 (LDA).

The optical conductivity is an optoelectronic phenomenon in which the elec- trical conductivity of a given material increases through the absorption of the electromagnetic radiation. The real part of the optical conductivity begins withthe photon energy $\sim 5.06(\sim 4.91) eV$ , corresponding to the direct (indirect) energy gap found above for the GGA+TS (LDA) functional, as depicted in Fig.3c (inset). The electrical conductivity due to the energy absorption of the pho- tons decreases in the energy range between 20 and 30 eV, being zero when the photon energy is greater than 30eV.

The absorption coefficient provides important information about the solar energy conversion and indicates in which region of the electromagnetic spectrum the material absorbs energy. Fig. 4a depicts the optical absorption spectrum of the L-threonine along the polarization direction [001] for the GGA+TS (solid black line) and LDA (solid red line) approaches. Therefore, in results obtained for both functionals, L-threonine crystal absorbs photon energy in the range5 to 25 eV (see the inset of Figure 4a), i.e. in the ultraviolet region, and is therefore transparent. Kumar et al. [51] (Rodrigues et al. [8)), has obtaineda transparency of approximately $85 \%$ in the range of 250 to 900 (250 to 1500) nm, which corresponds to the energy range of 4.9 to 17.64 (4.9 to 29.40) eV, in a fairly good agreement with our theoretical prediction. This is an important characteristic of the L-threonine crystal, because crystals that do not show op- tical absorption in the visible region are suitable materials for second harmonic generation [7]. It is remarkable that by comparing the absorption energy range in this work to previous studies for aspartic acid, serine, and proline crystals, it is possible to observe a similar behavior, where these amino acids begin to absorb photonic energy from $\sim 5 eV$ to $\sim 20 eV[45,46,47]$ .

The reflectivity spectra as a function of photon energy are shown in Fig. 4b. It starts with a value of $\sim 0.04(0.06)$ for the GGA + TS (LDA) functional. From there, it increases up to a maximum intensity of $\sim 0.74(0.49)$ in the energy range of 5.3 - 6.3 eV. It presents another peak of ~ 0.48 (0.64) in the range of 17.5 - 18.2 (18.8 - 19.6) eV, indicating that the L-threonine crystal is a good candidate to coating material in these energy ranges. It goes to zero at E=30 eV.

The energy loss function as a function of photon energy is shown in Fig.4c. This function is related to the energy loss of an electron crossing a material[52]. It is related to the plasma frequency $\omega_{p}$ , occurring when $\varepsilon_{2}>1$ and $\varepsilon_{1}$ approaches to zero. The energy loss function plotted within the GGA+TS(LDA) calculation considers the effective plasma frequency $\omega_{p}$ as 17.94 (19.69) eV. From this figure, we can conclude that the material becomes transparent(the loss function tends to zero) when the incident photon frequency is greater than $\omega_{p}$ at both functionals.

We used the GGA + TS functional to evaluate these properties, due to the overall better agreement with the experimental lattice parameters, as follows.

![](./images/812720531156500480_5.jpg)

Figure 4: (color online) The GGA+TS (solid black line) and LDA (solid red line) calculated a) absorption function; b) reflectivity; c) loss function of the orthorhombic L-threonine crystal. (inset) Close-up of the optical absorptions near to the main band gaps of the structures.

### 3.3. Infrared and Raman Spectrum

Infrared and Raman spectroscopies are very useful tools to investigate the vibrational, rotational, and other low-frequency modes in molecules, thin films, biological materials, solids, etc., being also complementary techniques used for fingerprinting of molecules and solids [53]. Both come from changes in their vibration modes. In particular, the infrared (IR) spectroscopy provides information on the percentage of the radiation transmission as a function of its wavelength, considering only those vibration modes which result in changes in the dipole moment. The peaks in an infrared spectroscopy plot, called absorption bands, are associated with the energy absorption for a particular wavelength. On the other hand, Raman spectra result from the inelastic scattering of light by vibrating molecules due to changes in their polarizability and are commonly used in physics and chemistry to provide a structural fingerprint by which molecules can be identified.

The diversity of hydrogen bonds observed in molecular crystals gives rise to vibrational signatures, which can be related to the particular way in which intermolecular interactions occur in the lattice. However, the coupling of intermolecular excitons to intramolecular vibrations and the oscillator strength for emission processes in crystals can be very different from those of an isolated molecule [54]. Hydrated crystals, on the other hand, are more likely to display hydrogen bonding patterns and electronic structure changes related to their presence in comparison with the isolated molecules. On the other hand, anhydrous crystals, as the orthorhombic L-threonine crystal considered here, can modify the vibrational spectra by altering the effective strength of the covalent bonds, increasing its stretching elastic constant and shifting the corresponding normal-mode frequency to higher values.

Table II depicts the normal modes together with their respective irreducible representations, as well as the assignment of IR and Raman active modes, for the orthorhombic L-threonine anhydrous crystal. There are 204 normal modes of vibration at the wave vector $\mathbf{k}=0$, three of them being acoustic (inactive) modes (the modes 1, 2, and 3 shown in Table II). The remaining 150 (201) are IR (Raman) active modes, according to the irreducible representation $\Gamma_{IR}$=$50$B$_1$+$50$B$_2$+$50$B$_3$ ($\Gamma_{Raman}$=$51$A+$50$B$_1$+$50$B$_2$+$50$B$_3$).

The infrared and Raman spectroscopy plots obtained for the orthorhombic L-threonine crystal is shown in Fig. 5, considering the wavelength range $\lambda=0$ to $4000\ \text{cm}^{-1}$. In what follows, the assignments of the IR and Raman active modes of vibration are described according to: $\tau$ - torsion, $\rho$ - balance, $\delta$ - deformation, $w$ - wagging, and $\nu$ - stretching.

In the range 0 to $400\ \text{cm}^{-1}$, it is possible to observe the formation of absorption bands in the infrared spectrum. In this interval, apparently, there are no explicit Raman modes. However, the existence of active modes in this region can be found with the help of Table II. From there, we can identify the formation of IR absorption bands and active Raman modes, with a common peak corresponding to the wavelength $68\ \text{cm}^{-1}$ related to the molecular skeletal balance ($\rho$skel) (see the inset of Figure 5). In the IR spectrum, $\rho$skel is responsible for the formation of the peaks at 105, 132 and $161\ \text{cm}^{-1}$. On the other

<table>
<caption>Table 2: Normal modes of orthorhombic L-threonine crystal at $k=0$. Irreducible representations (Irrep) are indicated, as well as the active IR and Raman modes.</caption>
<tbody>
<tr>
<td>N</td>
<td>$\lambda(cm^{-1})$</td>
<td>Irrep</td>
<td>IR</td>
<td>Raman</td>
<td>N</td>
<td>$\lambda(cm^{-1})$</td>
<td>Irrep</td>
<td>IR</td>
<td>Raman</td>
<td>N</td>
<td>$\lambda(cm^{-1})$</td>
<td>Irrep</td>
<td>IR</td>
<td>Raman</td>
<td>N</td>
<td>$\lambda(cm^{-1})$</td>
<td>Irrep</td>
<td>IR</td>
<td>Raman</td>
</tr>
<tr>
<td>1</td>
<td>-0.06</td>
<td>$B_3$</td>
<td>N</td>
<td>N</td>
<td>52</td>
<td>399.03</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>103</td>
<td>1084.67</td>
<td>$B_1$</td>
<td>N</td>
<td>Y</td>
<td>154</td>
<td>1478.75</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>2</td>
<td>-0.05</td>
<td>$B_1$</td>
<td>N</td>
<td>N</td>
<td>53</td>
<td>417.51</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>104</td>
<td>1086.54</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>155</td>
<td>1483.89</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>3</td>
<td>-0.03</td>
<td>$B_2$</td>
<td>N</td>
<td>N</td>
<td>54</td>
<td>423.29</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>105</td>
<td>1089.24</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>156</td>
<td>1492.46</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>4</td>
<td>42.55</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>55</td>
<td>449.54</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>106</td>
<td>1093.03</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>157</td>
<td>1529.06</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>5</td>
<td>55.23</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>56</td>
<td>451.04</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>107</td>
<td>1095.26</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>158</td>
<td>1529.76</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>6</td>
<td>56.57</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>57</td>
<td>474.21</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>108</td>
<td>1098.81</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>159</td>
<td>1590.60</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>7</td>
<td>68.02</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>58</td>
<td>474.45</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>109</td>
<td>1100.06</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>160</td>
<td>1591.61</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>8</td>
<td>69.06</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>59</td>
<td>476.16</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>110</td>
<td>1101.56</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>161</td>
<td>1601.82</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>9</td>
<td>75.87</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>60</td>
<td>477.26</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>111</td>
<td>1104.01</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>162</td>
<td>1601.93</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>10</td>
<td>77.66</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>61</td>
<td>497.90</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>112</td>
<td>1110.12</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>163</td>
<td>1613.61</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>11</td>
<td>87.69</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>62</td>
<td>499.70</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>113</td>
<td>1179.30</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>164</td>
<td>1614.80</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>12</td>
<td>91.37</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>63</td>
<td>501.93</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>114</td>
<td>1182.58</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>165</td>
<td>1638.80</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>13</td>
<td>91.45</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>64</td>
<td>506.33</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>115</td>
<td>1190.97</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>166</td>
<td>1642.67</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>14</td>
<td>98.26</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>65</td>
<td>546.87</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>116</td>
<td>1191.19</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>167</td>
<td>1644.24</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>15</td>
<td>104.59</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>66</td>
<td>549.25</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>117</td>
<td>1225.86</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>168</td>
<td>1652.22</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>16</td>
<td>105.49</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>67</td>
<td>552.68</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>118</td>
<td>1230.06</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>169</td>
<td>2860.91</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>17</td>
<td>107.03</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>68</td>
<td>559.81</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>119</td>
<td>1235.28</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>170</td>
<td>2861.14</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>18</td>
<td>107.93</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>69</td>
<td>679.43</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>120</td>
<td>1236.46</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>171</td>
<td>2884.71</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>19</td>
<td>110.52</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>70</td>
<td>683.45</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>121</td>
<td>1287.34</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>172</td>
<td>2887.32</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>20</td>
<td>116.64</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>71</td>
<td>684.99</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>122</td>
<td>1292.82</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>173</td>
<td>2896.20</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>21</td>
<td>131.76</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>72</td>
<td>689.68</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>123</td>
<td>1295.86</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>174</td>
<td>2896.58</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>22</td>
<td>131.79</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>73</td>
<td>726.31</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>124</td>
<td>1303.84</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>175</td>
<td>2896.71</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>23</td>
<td>132.76</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>74</td>
<td>729.87</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>125</td>
<td>1314.30</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>176</td>
<td>2897.54</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>24</td>
<td>136.63</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>75</td>
<td>733.40</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>126</td>
<td>1318.99</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>177</td>
<td>2964.15</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>25</td>
<td>161.85</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>76</td>
<td>737.00</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>127</td>
<td>1320.48</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>178</td>
<td>2964.27</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>26</td>
<td>170.98</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>77</td>
<td>834.71</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>128</td>
<td>1320.89</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>179</td>
<td>2966.16</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>27</td>
<td>181.92</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>78</td>
<td>839.47</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>129</td>
<td>1325.25</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>180</td>
<td>2966.31</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>28</td>
<td>183.19</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>79</td>
<td>844.67</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>130</td>
<td>1327.82</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>181</td>
<td>2971.60</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>29</td>
<td>192.13</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>80</td>
<td>845.93</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>131</td>
<td>1328.71</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>182</td>
<td>2974.55</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>30</td>
<td>198.73</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>81</td>
<td>858.24</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>132</td>
<td>1333.17</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>183</td>
<td>2982.83</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>31</td>
<td>201.47</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>82</td>
<td>866.16</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>133</td>
<td>1363.01</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>184</td>
<td>2991.94</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>32</td>
<td>214.27</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>83</td>
<td>868.61</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>134</td>
<td>1363.21</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>185</td>
<td>3012.23</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>33</td>
<td>214.73</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>84</td>
<td>868.63</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>135</td>
<td>1366.26</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>186</td>
<td>3020.43</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>34</td>
<td>215.83</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>85</td>
<td>886.54</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>136</td>
<td>1372.37</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>187</td>
<td>3035.92</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>35</td>
<td>225.32</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>86</td>
<td>890.05</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>137</td>
<td>1372.51</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>188</td>
<td>3040.51</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>36</td>
<td>226.81</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>87</td>
<td>898.70</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>138</td>
<td>1374.01</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>189</td>
<td>3040.65</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>37</td>
<td>247.93</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>88</td>
<td>902.78</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>139</td>
<td>1379.31</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>190</td>
<td>3040.83</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>38</td>
<td>252.13</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>89</td>
<td>911.09</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>140</td>
<td>1381.76</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>191</td>
<td>3041.20</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>39</td>
<td>252.98</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>90</td>
<td>911.51</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>141</td>
<td>1389.59</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>192</td>
<td>3048.61</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>40</td>
<td>255.90</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>91</td>
<td>918.12</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>142</td>
<td>1397.67</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>193</td>
<td>3060.35</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>41</td>
<td>313.52</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>92</td>
<td>919.15</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>143</td>
<td>1408.38</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>194</td>
<td>3061.24</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>42</td>
<td>314.04</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>93</td>
<td>1015.29</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>144</td>
<td>1410.42</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>195</td>
<td>3061.36</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>43</td>
<td>314.57</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>94</td>
<td>1020.43</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>145</td>
<td>1441.02</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>196</td>
<td>3061.71</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>44</td>
<td>315.15</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>95</td>
<td>1021.72</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>146</td>
<td>1442.41</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>197</td>
<td>3066.77</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>45</td>
<td>334.89</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>96</td>
<td>1023.00</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>147</td>
<td>1445.55</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>198</td>
<td>3066.83</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>46</td>
<td>338.83</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>97</td>
<td>1024.13</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>148</td>
<td>1445.90</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>199</td>
<td>3067.47</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>47</td>
<td>352.61</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>98</td>
<td>1024.94</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>149</td>
<td>1451.45</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>200</td>
<td>3069.98</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>48</td>
<td>354.50</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>99</td>
<td>1031.33</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>150</td>
<td>1458.86</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>201</td>
<td>3166.58</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>49</td>
<td>373.95</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>100</td>
<td>1031.62</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>151</td>
<td>1460.23</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>202</td>
<td>3175.49</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>50</td>
<td>376.27</td>
<td>$A$</td>
<td>N</td>
<td>Y</td>
<td>101</td>
<td>1079.78</td>
<td>$B_3$</td>
<td>Y</td>
<td>Y</td>
<td>152</td>
<td>1460.61</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>203</td>
<td>3176.39</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>51</td>
<td>386.20</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>102</td>
<td>1081.18</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
<td>153</td>
<td>1467.39</td>
<td>$B_1$</td>
<td>Y</td>
<td>Y</td>
<td>204</td>
<td>3182.18</td>
<td>$B_2$</td>
<td>Y</td>
<td>Y</td>
</tr>
</tbody>
</table>

hand, in the wavelength range from 181 to $198\ \mathrm{cm}^{-1}$, there are IR absorption bands attributed to the torsion of the $\mathrm{COO}^{-}$ ($\tau\mathrm{COO}^{-}$) and $\mathrm{CC}$ ($\tau\mathrm{CC}$) groups, respectively. The molecular skeleton balance ($\rho\mathrm{skel}$), the torsion $\mathrm{CH}_{3}$ ($\tau\mathrm{CH}_{3}$)),
340 deformation $\mathrm{CNH}_{3}$ ($\delta\mathrm{CNH}_{3}$), and $\mathrm{CCH}_{3}$ ($\delta\mathrm{CCH}_{3}$), and the vibration mode of molecular skeletal deformation ($\delta\mathrm{skel}$) are responsible for the absorption bands at $\lambda=214,255,252,315,338,354$ and $399\ \mathrm{cm}^{-1}$. Regarding the active Raman modes, there are peaks at $\lambda=110$ and $170\ \mathrm{cm}^{-1}$, respectively, due to the $\rho\mathrm{skel}$ and the torsion of the carboxyl group ($\tau\mathrm{COO}^{-}$). Besides, vibration modes due
345 to $\rho\mathrm{skel}$, $\delta\mathrm{CCH}_{3}$ and $\delta\mathrm{skel}$ are assigned to the respective wavelengths at 215, 334 and $376\ \mathrm{cm}^{-1}$.

In the region corresponding to the wavelength $\lambda$ between 400 and $1000\ \mathrm{cm}^{-1}$, there are IR absorption bands due to the $\delta\mathrm{skel}$, $\delta\mathrm{COH}$, $\delta\mathrm{CCH}_{3}$ and $\tau\mathrm{NH}_{3}$ vibrations for the frequencies 423, 449, 474 and $497\ \mathrm{cm}^{-1}$, respectively. The torsion
350 of the $\mathrm{NH}_{3}$ group was found for the wavelength corresponding to $489.9\ \mathrm{cm}^{-1}$ (IR) and $497.6,492\ \mathrm{cm}^{-1}$ (Raman) [55, 56]. In this region, the most intense

![](./images/812720531156500480_6.jpg)

Figure 5: Infrared and Raman spectra of orthorhombic L-threonine crystal in the 0 to 4000
cm⁻¹ range. The numbers correspond to the most important normal modes. The insets show
the infrared and Raman spectra in the low-frequency range 0-1000 cm⁻¹.

active Raman modes correspond to the vibration modes $\delta$COH, $\delta$COH, $\delta$CCH₃
and $\delta$CNH₃ for $\lambda = 417, 451, 476$, and $559\ \text{cm}^{-1}$. The IR (Raman) peak at
$\lambda = 679\ (683)\ \text{cm}^{-1}$ is associated with the CH-oscillation vibration mode ($\rho$CH),
while the IR (Raman) peak at $\lambda = 733\ (729)\ \text{cm}^{-1}$ is attributed to the wagging
mode $w$ of $\text{CO}_{2}^{-}$ ($w\text{CO}_{2}^{-}$). The active IR modes for wavelengths 839, 868, and
898 (919) $\text{cm}^{-1}$ correspond to the vibration modes $w$OH (the antisymmetric
balance $\text{CH}_{3}$ - $\rho_{a}\text{CH}_{3}$). In the Raman spectrum, the active modes at 845 and
$911\ \text{cm}^{-1}$ are assigned to $w$OH and $\rho_{a}\text{CH}_{3}$, respectively.

From $\lambda = 1000$ to $1400\ \text{cm}^{-1}$, the Raman peaks at the wavelengths 1110,
1021, 1031, 1182 and $1191\ \text{cm}^{-1}$ are assigned to the modes $\rho$NH₃, CN strain
($\nu$CN), CH strain ($\delta$CH) and CH balance ($\rho$CH), respectively. Besides, modes
associated with $\rho$CH appear also in the Raman spectrum, at $\lambda = 1230, 1314$ and
$1372\ \text{cm}^{-1}$. In the IR spectrum, the wavelengths and their respective modes of
vibration are: $1225\ \text{cm}^{-1}$ due to $\rho$CH; $1295\ \text{cm}^{-1}$ related to $\delta$CH; $1320\ \text{cm}^{-1}$
assigned to $\delta$CH; $1333\ \text{cm}^{-1}$ by $\rho$CH; $1363\ \text{cm}^{-1}$ corresponding to the symmetric
balance vibration mode $\text{CH}_{3}$ ($\delta_{s}\text{CH}_{3}$); and $1389\ \text{cm}^{-1}$ related to $\rho$OH.

From $\lambda = 1400$ to $2000\ \text{cm}^{-1}$ there are identified absorption bands in the
infrared absorption spectrum and more discrete Raman activities. This region is
usually formed due to the double bonds. Between 1400 and $1600\ \text{cm}^{-1}$ we have,
for the IR absorption spectra: the vibration mode of symmetric deformation
$CH_{3}$ ($\delta_{s}\text{CH}_{3}$) which is responsible for the peak at $1458\ \text{cm}^{-1}$; the $1467\ \text{cm}^{-1}$
wavelength peak, associated to the antisymmetric deformation vibration mode
of the $CH_{3}$ group ($\delta_{a}\text{CH}_{3}$); the wavelength $1591\ \text{cm}^{-1}$, associated with the

antisymmetric deformation vibration of the group $NH_3$ ($\delta_a$NH$_3$). On other hand, in the Raman spectrum, more intense modes occur for wavelengths $\lambda =$ 1408 ($\rho$OH) and 1441 ($\delta_a$CH$_3$).

The wavelength range from 2000 to $2500\ \text{cm}^{-1}$ is attributed to triple bonds [57] absent in the L-threonine crystal, explaining the absence of peaks in this region.

Finally, the formation of peaks in the wavelength range between 2500 and $4000\ \text{cm}^{-1}$ of the IR spectrum are usually attributed to the functional groups of the material, where the stretching $\nu$-vibration modes of hydrogen bonds occur. The peaks corresponding to $\lambda = 2861, 2887, 2982, 2992$ and $3166\ \text{cm}^{-1}$, related to the absorption of the IR spectroscopy, are associated with the antisymmetric stretching of the $NH_3$ ($\nu_a$NH$_3$) group, with a contribution due to the stretching of the OH ($\nu$OH) group to form the peak corresponding to the wavelength $2982\ \text{cm}^{-1}$. In the Raman side, the $2860\ \text{cm}^{-1}$ peak is attributed to the $\nu_a$NH$_3$ group, and the peak at $2896\ \text{cm}^{-1}$ is related to the OH stretch. Also, the peak at $\lambda = 2966\ \text{cm}^{-1}$ is associated to the symmetrical stretching of the $CH_3$ group. The peak $3020\ \text{cm}^{-1}$ is attributed to the $\nu$OH and to the $\nu_a$NH$_3$ groups, while the peak at $3035\ \text{cm}^{-1}$ ($3066\ \text{cm}^{-1}$) is formed by the $\nu$OH ($\nu$CH) group. Besides, peaks appear due to the OH and CH stretches at wavelengths 3012 and $3066\ \text{cm}^{-1}$, respectively, and by the antisymmetric NH$_3$ stretch at $3182\ \text{cm}^{-1}$.

### 3.4. Thermodynamic Properties
The thermodynamic properties are closely related to the vibrational properties of a material, providing a guidance for insights about their atomic lattice behavior, as well as essential information for modeling technological processes [58, 59]. It is well known that by increasing the temperature of a material, there is an expansion in its volume, which usually softens the lattice vibrations and enhances (reduces) its entropy (lattice energy) [59, 60, 61]. Besides, this effect is most significant in weakly bound crystals, such as organic crystals.

In this sense, to obtain a better understand about the thermal effect over the anhydrous orthorhombic L-threonine crystal, some thermodynamic properties were obtained by means of phonon calculations within the quasi-harmonic approximation framework. They include the enthalpy (E), entropy (S), free energy (F), lattice heat capacity ($\text{C}_V$) and the Debye temperature ($\Theta_D$), in the range of 7 to 2000 K, using a norm-conserving pseudopotential for the GGA-PBE+D functional and the Baroni relation [62]. They are depicted in Fig. 6.

Fig. 6(a) shows the profiles of the calculated thermodynamic potentials' enthalpy, free energy and the temperature (T) times the entropy (T*Entropy) term, $\text{TS} = \text{U - F}$ (U being the internal energy), as a function of the temperature (in K), for the anhydrous orthorhombic L-threonine crystal. From there one can see that at a temperature below 100 K, the enthalpy, free energy, and the T*Entropy values are almost zero. After that (T> 100 K), T*Entropy and the enthalpy values increase as a function of T, with the latter showing a most linear behavior. On the other hand, the free energy decreases as the T increases.

In Fig. 6(b) we depict the constant lattice heat capacity ($\text{C}_V$), as a function of the temperature (in K). It is easy to see that the heat capacity increases as

![](./images/812720531156500480_7.jpg)

Figure 6: Anhydrous orthorhombic L-threonine crystal (a) enthalpy (black solid line), free energy (red solid line) and T*Entropy (blue solid line), (b) lattice heat capacity (C_V), and (c) Debye temperature (Θ_D), as a function of the temperature.

the temperature increases, reaching the Dulong-Petit limit at around 380 K. According with the Dulong-Petit law, the atoms of a solid crystal vibrate in three-dimensional space with an energy of $k_B$T, at room temperature (300 K) [61]. In this work, the calculated $C_V$ at room temperature was 143.06 cal/cell·K.

Finally, the variation of the Debye temperature as a function of T until 2000 K is depicted in Fig. 6(c). One can observe that $\Theta_D$ shows a higher variation at temperatures until 1000 K, becoming smaller for temperatures higher than that.

The above analysis shows that L-threonine crystal exhibits some instabil- ity in thermodynamic properties. These results can be either compared with the experimental data, or used to predict the phase stability for its different structural modifications.

### 4. Conclusions

As a new contribution to obtain a complete picture of the properties of amino acids in the solid state, the anhydrous orthorhombic L-threonine crystal was investigated in this work by means of the calculated structural, electronic and optical properties using both the DFT-GGA+TS and DFT-LDA approaches, taking advantage of its X-ray diffraction pattern as measured by Janczak et al. [28].

The lattice parameters $a$, $b$, $c$ obtained from LDA calculations are 3.73, 14.95 and 6.75 % smaller than the experimental result (see Table I) due to overestimation of the forces between atoms in the LDA approach. On the other hand, for GGA+TS calculations, where we have underestimate the forces of interatomic connections, we have obtained lattice parameters showing a good agreement among the lattices parameters $a$, $b$ and $c$ (-0.61, 1.59 and 0.18 %) when compared to the experimental results.

The band structure reveals that the L-threonine crystal have a direct (indirect) band gap semiconductor for GGA+TS (LDA), with top valence band at the point $\Gamma$ (X) and bottom of conduction band at point $\Gamma$ (S). The band gap value is 5.06 eV (4.91 eV) according to the GGA+TS (LDA) calculations. Therefore, the result for GGA+TS and LDA approaches are in good agreement with the 4.96 eV experimental estimation of the band gap for L-threonine crystal [43]. Regarding the DOS spectra obtained in both approaches, we can observe that the upper valence bands are dominated by the $p$ states, while the deepest valence bands are mainly originated from the $s$ atomic orbitals.

The calculated complex electronic dielectric constant along the direction [001] of the L-threonine crystal yielded a refractive index $n(0)$ equal to 1.52 (GGA+TS) and 1.69 (LDA). For both functionals, L-threonine crystal absorbs photon energy in the range of 5 to 25 eV, i.e., in the ultraviolet region, an important result since crystals that do not show optical absorption in the visible region are suitable materials for second harmonic generation [7].

The infrared spectrum of L-threonine crystal has its most intense absorption peaks near 1467 (3020) $\text{cm}^{-1}$ of its lower (higher) frequency range. On the other hand, active Raman modes are more intense near 1314 (3012) $\text{cm}^{-1}$ of its lower (higher) frequency interval. Finally, the thermodynamic properties of these crystal systems are presented by its enthalpy, entropy, free energy, heat capacity and Debye temperature.

We hope this work will stimulate further experimental efforts to unveil the rich role of the structural, optoelectronic, vibrational and thermodynamic properties of biomolecules systems in the solid state.

### Declaration of Competing Interest

The authors have not conflict of interest to declare.

### Acknowledgement

This work was partially financed by the Brazilian Research Agencies CAPES (PNPD) and CNPq.

### References

[1] J. M. Bacher, R. A. Hughes, J. T. F. Wong and A. D. Ellington, Evolving new genetic codes. Trends Ecol. Evol. 19 (2004) 69-75.

[2] W. Leuchtenberger, K. Huthmacher, K. Drauz, Biotechnological produc- tion of amino acids and derivatives: current status and prospects. Appl. Microbiology and Biotech. 69 (2005) 1-8.

[3] K. Imura, A. Okada, Amino acid metabolism in pediatric patients. Nutri- tion 14 (1998) 143-148.

[4] P. J. Reeds, Dispensable and indispensable amino acids for humans. J. Nutr. 130 (2000) 1835S-1840S.

[5] G. Walsh, Proteins Biochemistry and Biotechnology (2nd ed.), John Wiley& Sons (2014).

[6] S. A. M. B. Dhas, M. Suresh, P. Raji, K. Ramachandran, S. Natarajan, Photoacoustic studies on two new organic NLO materials: L-threonine and L-prolinium tartrate. Cryst. Res. Technol. 42 (2007) 190-194.

[7] G. R. Kumar, S. G. Raj, R. Mohan, R. Jayavel, Growth, structural and spectral analyses of nonlinear optical L-threonine single crystals. J. Crystal Growth 275 (2005) e1947-e1951.

[8] J. J. Rodrigues, L. Misoguti, F. D. Nunes, C. R. Mendonça, S. C. Zilio, Optical properties of L-threonine crystals. Opt. Mat. 22 (2003) 235-240.

[9] R. L. Willett, K. W. Baldwin, K. W. West, L. N. Pfeiffer, Differential adhesion of amino acids to inorganic surfaces. Proc. Nat. Acad. Sci. USA102 (2005) 7817-7822.

[10] S. G. Santos, M. S. Pires, V. Lemos, V. N. Freire, E. W. S. Caetano, D. S. Galvão, F. Sato, E. L. Albuquerque, C60-derived nanobaskets: stabil- ity, vibrational signatures, and molecular trapping. Nanotech. 20 (2009)395701.

[11] S. N. Costa, F. A. M. Sales, V. N. Freire, F. F. Maia Jr., E. W. S. Caetano, L. O. Ladeira, E. L. Albuquerque, U. L. Fulco, L-serine anhydrous crystals: structural, electronic, and optical properties by first-principles calculations,and optical absorption measurement. Crystal Growth & Design 13 (2013)2793-2802.

[12] A. M. Silva, S. N. Costa, F. A. M. Sales, V. N. Freire, E. M. Bezerra, R. P. Santos, U. L. Fulco, E. L. Albuquerque, E. W. S. Caetano, Vibra- tional spectroscopy and phonon-related properties of the L-aspartic acid anhydrous monoclinic crystal. J. Phys. Chem. A 119 (2015) 11791-11803.

[13] A. M. Silva, B. P. Silva, F. A. M. Sales, V. N. Freire, E. Moreira, U. L. Fulco, E. L. Albuquerque, F. F. Maia Jr., E. W. S. Caetano, Optical absorption and DFT calculations in L-aspartic acid anhydrous crystals: Charge carrier effective masses point to semiconducting behavior. Phys. Rev. B 86 (2012)195201.

[14] A. B. M. L. A. Tavares, J. X. Lima Neto, U. L. Fulco, E. L. Albuquerque,
Inhibition of the checkpoint protein PD-1 by the therapeutic antibody pem-
brolizumab outlined by quantum chemistry. Sci. Rep. 8 (2018) 1840.

[15] P. R. Tulip, S. J. Clark, Structural and electronic properties of L-amino
acids. Phys. Rev. B 71 (2005) 195117.

[16] E. Moreira, J. M. Henriques, D. L. Azevedo, E. W. S. Caetano, V. N. Freire,
U. L. Fulco, E. L. Albuquerque, Structural and optoelectronic properties,
and infrared spectrum of cubic BaSnO3 from first principles calculations.
J. Appl. Phys. 112 (2012) 043703.

[17] R. F. da Costa, V. N. Freire, E. M. Bezerra, B. S. Cavada, E. W. S. Cae-
tano, J. L. de Lima Filho, E. L. Albuquerque, Explaining statin inhibition
effectiveness of HMG-CoA reductase by quantum biochemistry computa-
tions. Phys. Chem. Chem. Phys. 14 (2012) 1389-1398.

[18] S. G. dos Santos, J. Mendes Filho, V. N. Freire, E. W. S. Caetano E. L. Al-
buquerque, Carbon-based nanorings sliding along inner coaxial nanotubes:
Möbius topology effects in damping gigahertz oscillations. J. Appl. Phys.
116 (2014) 124311.

[19] S. N. Costa, V. N. Freire, E. W. S. Caetano, F. F. Maia Jr, C. A. Barboza,
U. L. Fulco, E. L. Albuquerque, DFT calculations with van der Waals
interactions of hydrated calcium carbonate crystals $CaCO_3{\cdot}(H_2O, 6H_2O)$:
structural, electronic, optical, and vibrational properties. J. Phys. Chem.
A 120 (2016) 5752-5765.

[20] M. Oda, T. Nakayama, Charge injection from Si substrate into amino acids.
Jpn. J. Appl. Phys. 45 (2006) 8939.

[21] M. Oda, T. Nakayama, Electronic-state control of amino acids on semicon-
ductor surfaces. Appl. Surf. Sci. 244 (2005) 627-630.

[22] M. A. Stroscio, M. Dutta, Integrated biological-semiconductor devices.
Proc. IEEE 93 (2005) 1772-1783.

[23] M. Z. S. Flores, V. N. Freire, R. P. dos Santos, G. A. Farias, E. W. S.
Caetano, M. C. F. de Oliveira, J. R. L. Fernandez, L. M. R. Scolfaro, M.
J. B. Bezerra, T. M. Oliveira, G. A. Bezerra, B. S. Cavada, H. W. Leite
Alves, Optical absorption and electronic band structure first-principles cal-
culations of $\alpha$-glycine crystals. Phys. Rev. B 77 (2008) 115104.

[24] A. M. Silva, S. N. Costa, B. P. Siva, V. N. Freire, U. L. Fulco, E. L.
Albuquerque, E. W. S. Caetano, F. F. Maia Jr., Assessing the role of water
on the electronic structure and vibrational spectra of monohydrated L-
aspartic acid crystals. Crystal Growth & Design 13 (2013) 4844-4851.

[25] F. F. Maia Jr., V. N. Freire, E. W. S. Caetano, D. L. Azevedo, F. A. M. Sales, E. L. Albuquerque, Anhydrous crystals of DNA bases are wide gap semiconductors. J. Chem. Phys. 134 (2011) 05B601.

[26] V. Parpura, Getting close to the action. Nature Nanotech.7 (2012) 143-145.

[27] D. P. Shoemaker, J. Donohue, V. Schmaker, R. B. Corey, The crystal structure of L-threonine. J. Am. Chem. Soc. 72 (1950) 2328-2349.

[28] J. Janczak, D. Zobel, P. Luger, L-threonine at 12 K. Acta Cryst. C 53 (1997) 1901-1904.

[29] S. J. Clark, M. D. Segall, C. J. Pickard, P. J. Hasnip, M. J. Probert, K. Refson, M. C. Payne, First principles methods using CASTEP. Zeitschrift fur Kristallographie 220 (2005) 567-570.

[30] D. M. Ceperley, B. J. Alder, Ground state of the electron gas by a stochastic method. Phys. Rev. Lett. 45 (1980) 566.

[31] J.P. Perdew, A. Zunger, Self-interaction correction to density-functional approximations for many-electron systems. Phys. Rev. B 23 (1981) 5048-5079.

[32] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple. Phys. Rev. Lett. 77 (1996) 3865.

[33] D. Zhang, Sci. Rep., 7 (2017), 44645.

[34] A. Li, H. S. Muddana and M. K. Gilson, J. Chem. Theory Comput., 10 (2014) 1563-1575.

[35] A. Tkatchenko, M. Scheffler, Accurate molecular van der Waals interactions from ground-state electron density and free-atom reference data. Phys. Rev. Lett. 102 (2009) 073005.

[36] J. S. Lin, A. Qteish, M. C. Payne,V. Heine, Optimized and transferable nonlocal separable ab initio pseudopotentials. Phys. Rev. B 47 (1993) 4174.

[37] H. J. Monkhorst, J. D. Pack, Special points for Brillouin-Zone integrations. Phys. Rev. B 13 (1976) 5188-5192.

[38] P. Hohenberg, W. Kohn, Inhomogeneous electron gas. Phys. Rev. 136 (1964) B864.

[39] W. Kohn, L. J. Sham, Self-consistent equations including exchange and correlations effects. Phys. Rev. 140 (1965) A1133.

[40] E. L. Albuquerque, U. L. Fulco, V. N. Freire, E. W. S. Caetano, M. L. Lyra, F. A. B. F. Moura, DNA-based nanobiostructured devices: The role of quasiperiodicity and correlation effects. Phys. Rep. 535 (2014) 139-209.

[41] M. Zhong, Q. J. Liu, C. L. Jiang, F. S. Liu, B. Tang, X. J. Peng, Structural,elastic, electronic, phonon, dielectric and optical properties of $Bi_3TeBO_9$ from first-principles calculations. J. Phys. Chem. Solids 121 (2018) 139-144.

[42] M. Jubair, A. M. M. T. Karim, M. Nuruzzaman, M. A. K. Zilani, Compar- ison of structural, mechanical and optical properties of tantalum hemicar- bide with tantalum monocarbide: ab initio calculations. J. Phys. Commun.3 (2019) 055017.

[43] D. Subashini,A. R. Prabhakaran, S. N. Jayanthi K. Thamizharasan, Spec- tral, thermal investigation and particle size determination of L-threonine single crystals. Adv. Appl. Sci. Res. 4 (2013) 238-242.

[44] M. Z. S. Flores,V. N. Freire, R. P. dos Santos, G. A. Farias, E. W. S. Cae- tano, M. C. F. de Oliveira, J. R. L. Fernandez, L. M. R. Scolfaro, M. J. B. Bezerra, T. M. Oliveira, G. A. Bezerra, B. S. Cavada, H. W. Leite Alves, Optical absorption and electronic band structure first-principles calcula- tions of $\alpha$-glycine crystals. Phys. Rev. B 77 (2008) 115104-115107.

[45] A. M. Silva,B. P. Silva, F. A. M. Sales, V. N. Freire, E. Moreira, U. L. Fulco, E. L. Albuquerque, F. F. Maia, E. W. S. Caetano, Optical absorption and DFT calculations in L-aspartic acid anhydrous crystals: Charge carrier effective masses point to semiconducting behavior. Phys. Rev. B 86 (2012)195201-195212.

[46] S. N. Costa, F. A. M. Sales, V. N. Freire, F. F. Maia, Jr., E. W. S. Caetano, L. O. Ladeira, E. L. Albuquerque, U. L. Fulco, L-serine anhydrous crystals: structural, electronic, and optical properties by first-principles calculations, and optical absorption measurement. Cryst. Growth Des. 13 (2013) 2793-2802.

[47] E. W. S. Caetano,U. L. Fulco, E. L. Albuquerque, A. H. de Lima Costa, S. N. Costa, A. M. Silva, F. A. M. Sales, V. N. Freire, Anhydrous pro- line crystals: Structural optimization, optoelectronic properties, effective masses and Frenkel exciton energy. J. Phys. Chem. Solids 121 (2018) 36-48.

[48] J. R. Cândido-Júnior,F. A. M. Sales, S. N. Costa, P. de Lima-Neto, D. L. Azevedo, E. W. S. Caetano, E. L. Albuquerque, V. N. Freire, Monoclinic and orthorhombic cysteine crystals are small gap insulators. Chem. Phys. Lett. 512 (2011) 208-210.

[49] D. Li, F. Ling, Z. Zhu, X. Zhang, Theoretical studies on the structural,electronic, and optical properties of $Cu_2CdGeSe_4$. Physica B 406 (2011)3299.

[50] Y. Fang, X. Kong, D. Wang, J. Liu, D. Cui, First principle calculations of electronic, band structural, and optical properties of $Bi_xSr_{1-x}TiO_3$ per- ovskite. J. Phys. Chem. Solids 127 (2019) 107-114.

[51] G. R. Kumar, S. G. Raj, Growth and physiochemical properties of second-order nonlinear optical L-threonine single crystals. Adv. Mat. Sci. Eng. 2009 (2009) 40.

[52] Md. A. Rahman, Md. Z. Rahaman, Md. A. R. Sarker, First principles investigation of structural, elastic, electronic and optical properties of $HgGeB_2$ (B=P, As) chalcopyrite semiconductors. Comp. Condens. Matter. 9 (2016) 19-26.

[53] M. Babiker, D. R. Tilley, E. L. Albuquerque, C. E. T. Goncalves da Silva, Acoustic Green function for superlattices. J. Phys. C: Solid State Phys. 18 (1985) 1269.

[54] C. J. Bardeen, Excitonic processes in molecular crystalline materials. MRS Bull. 38 (2013) 65.

[55] M. R. S. Kumar, H. J. Ravindra, A. Jayarama, S. M. Dharmaprakash, Structural characteristics and second harmonic generation in L-threonine crystals. J. Crystal Growth. 286 (2006) 451-456.

[56] B. L. Silva, P. T. C. Freire, F. E. A. Melo, J. M. Filho, M. A. Pimenta, M. S. S. Dantas, High-pressure Raman spectra of L-threonine crystal. J. Raman Spectrosc. 31 (2000) 519-522.

[57] B. H. Stuart, Infrared Spectroscopy: Fundamentals and Applications, John Wiley and Sons (2004).

[58] E. Moreira, C. A. Barboza, E. L. Albuquerque, U. L. Fulco, J. M. Henriques, A. I. Araújo, Vibrational and thermodynamic properties of orthorhombic $CaSnO_3$ from DFT and DFPT calculations. J. Phys. Chem. Solids 77 (2015) 85-91.

[59] C. Červinka, M. Fulem, R. P. Stoffel, R. Dronskowski, Thermodynamic properties of molecular crystals calculated within the quasi-harmonic approximation. J. Phys. Chem. A 120 (2016) 2022-2034.

[60] J. L. McKinley, G. J. O. Beran, Identifying pragmatic quasi-harmonic electronic structure approaches for modeling molecular crystal thermal expansion. n. Faraday Discuss. 211 (2018) 181.

[61] R. P. Stoffel, C. Wessel, M. W. Lumey, R. Dronskowski, Ab initio thermochemistry of solid-state materials. Angew. Chem., Int. Ed. 49 (2010) 5242.

[62] S. Baroni, S. de Gironcoli, A. dal Corso, P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory. Rev. Mod. Phys. 73 (2001) 515.

![](./images/812720531156500480_8.jpg)

Anhydrous Orthorhombic L-Threonine Crystals

**Authors:** Roniel L. Araújo, Manoel S. Vasconcelos, Carlos A. Barboza, José X. Lima Neto, Eudenilson L. Albuquerque and Umberto L. Fulco

Highlights:

- Characterization of the orthorhombic L-Threonine Crystals.

- A quantum chemistry approach within the density functional theory computations by using the local-density approximation (LDA) and the generalized gradient approximation with scatter correction (GGA+TS).

- Analysis of the electronic, structural, thermodynamical, optical, and vibrational spectra of the orthorhombic L-Threonine crystals.

- Raman and Infrared spectra.

The authors declare that they have no competing interests.

### Declaration of interests

☒ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

☐The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

![](./images/812720531156500480_9.jpg)