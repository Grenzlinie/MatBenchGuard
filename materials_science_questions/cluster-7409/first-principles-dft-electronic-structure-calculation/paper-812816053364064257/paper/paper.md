First principles investigation of electronic properties and high refractive index of rutile
TiO₂ for photovoltaic applications

A. Eddiouane, H. Chaib, A. Nafidi, M. Najjaoui, and T. Ait-Taleb

Citation: AIP Conference Proceedings 2056, 020005 (2018); doi: 10.1063/1.5084978
View online: https://doi.org/10.1063/1.5084978
View Table of Contents: http://aip.scitation.org/toc/apc/2056/1
Published by the American Institute of Physics

![](./images/812816053364064257_1.jpg)

# First Principles Investigation of Electronic Properties and High Refractive Index of Rutile TiO₂ for Photovoltaic Applications

A. Eddiouane¹,ᵃ, H. Chaib¹, A. Nafidi², M. Najjaoui¹, T. Ait-Taleb¹

¹Research group materials and energy, Polydisciplinary Faculty, Ibn Zohr University, P.O. Box 638, 45000, Ouarzazate, Morocco
²Laboratory of condensed matter and nanomaterials for renewable energy, Ibn Zohr University, 80000, Agadir, Morocco

ᵃE-mail address: abderrahim.eddiouane@edu.uiz.ac.m

**Abstract** Anti-reflective layer is an essential component of photovoltaic devices, used to reduce the well-known problem of light reflection. Deposed on the silicon wafers, this glass cover significantly contributes to raise the photovoltaic solar cells efficiency. For this purpose we used different dielectric materials, namely titanium dioxide TiO₂. In the present work, we report the optimized structure, electronic band structure, density of states (DOS), partial density of states (PDOS) and optical properties of bulk rutile phase of titanium dioxide (TiO₂). The density functional theory based upon the pseudo-potentials method as implemented in the first principle Quantum Espresso (QE) code has been employed. We performed a plane wave self-consistent field calculation of the ground state energy with both local density approximation (LDA) and generalized gradient approximation (GGA).

Optical properties such as refractive indices, depending on the ordinary and extraordinary polarization directions, have been evaluated from the frequency-dependent complex dielectric function. Moreover, the obtained band structures, DOS and PDOS confirm that the valence and conduction bands of rutile are mainly formed by O₂ₚ and Ti₃d states respectively. This substantiates the existence of high interactions between titanium and oxygen atoms. The large optical anisotropy has been studied through the calculation of the band structure and DOS. Our results are in good agreement with previous theoretical and experimental measurements.

**Keywords**: Anti-reflective layer; Density functional theory, Quantum Espresso, TiO₂, Electronic band structure, Refractive indices.

## INTRODUCTION

In the last few decades, TiO₂ has attracted a great deal of interest, due to its important electronic and optical properties such as refractive indices, optical anisotropy, high dielectric constants as well as significant photocatalycal properties [1]–[3]. Besides these remarkable properties and regarding its non-toxicity [4] and low cost and stability [5], TiO₂ is largely used in solar cell technologies [6],[7], as a protective and anti-reflective film for optical coating [8],[9].

TiO₂ has been also classified as an incipient ferroelectric material, thanks to its high dielectric constant that increases as the temperature decreases; on other hand no ferroelectric transition has been observed [10]. It has been considered as a wide band gap semiconductor of n-type (3.0 eV) and an insulator material at temperatures under 200°C [11]. Among all polymorphs of TiO₂ (i.e. anatase, rutile and brookite), the rutile phase is the most abundant in nature and has the most thermodynamic stability [4],[12]. Moreover, it has the highest index of refraction which makes it useful as material of great importance for filters, dielectric mirrors of lasers and optical anti-reflective thin layers [13]. Regarding their interesting performance in solid state calculations, the density functional theory (DFT) methods have been successfully applied to the study of various phases of TiO₂ especially the tetragonal rutile [14]–[16]. Landmann et al. have investigated the electronic and optical properties of the three amorphous of TiO₂ via the projected augmented wave (PAW) approach [17].

In this context, the present paper aims to apply the DFT approach, as implemented in QE formalism, in the study of the electronic and optical properties of rutile Those calculations have been performed with two different exchange correlation energies under either LDA or GGA. For this purpose, our work is ordered as follows: in section 0, we give

---
1st International Congress on Solar Energy Research, Technology and Applications (ICSERTA 2018)
AIP Conf. Proc. 2056, 020005-1–020005-8; https://doi.org/10.1063/1.5084978
Published by AIP Publishing. 978-0-7354-1784-7/$30.00

020005-1

details about the computational method processed within the used formalism. Then, section 0 discusses the obtained results using both GGA and LDA functional.

## COMPUTATIONAL METHOD

Here, theoretical calculations based on the DFT method have been carried out using the QE package [18] and taking into account the plane wave self-consistent (PWscf) method. We consider that the interactions electron-ions have been described by the norm-conserving pseudo-potentials [19] as supplied in the package's database. Moreover, O atoms have been treated by 2s and 2p valence states, and Ti atoms by 3s, 3p, 4s, and 3d orbitals. The exchange correlation potential is based on the Perdew, Berke and Ernzerof (PBE) functional approximation, as implemented in the GGA approximation [20]. Whereas, the LDA was employed under the Perdew and Wang (PW) functional approximation [21].

The calculations consist on solving Kohn-Sham equations [22] in the case of rutile single crystals. We satisfactorily obtained convergence results by using 80 Ry as kinetic cutoff energy for plane waves, $10^{-12}$ eV/atom as convergence threshold energy and a set of grid of 5×5×10 k-points in the irreducible Brillouin zone according to Monkhorst-Pack scheme [23].

## RESULTS AND DISCUSSIONS

### Optimization of Structure

We first optimized our tetragonal structure, using experimental data of lattice parameters under the LDA and GGA approximations and the VC-relax method as given by QE code. This method consists on configuring the ground state of the total energy. For accuracy, we used experimental data of the lattice parameters given in the literature [14]. The calculated values of lattice parameters $a$, $c$ and the internal crystal parameter $u$, as well as their experimental values, are listed in Table 1.

Table 1. Various values of structural parameters of rutile

<table>
  <tr>
    <th></th>
    <th>a=b (Å)</th>
    <th>c (Å)</th>
    <th>u</th>
  </tr>
  <tr>
    <td>Present pbe-GGA</td>
    <td>4.733</td>
    <td>3.072</td>
    <td>0.306</td>
  </tr>
  <tr>
    <td>pw-LDA</td>
    <td>4.522</td>
    <td>2.905</td>
    <td>0.304</td>
  </tr>
  <tr>
    <td>Experiment<sup>a</sup></td>
    <td>4.593</td>
    <td>2.959</td>
    <td>0.305</td>
  </tr>
  <tr>
    <td rowspan="2">Other DFT works</td>
    <td>4.534<sup>b</sup></td>
    <td>2.920</td>
    <td>0.303</td>
  </tr>
  <tr>
    <td>4.631<sup>c</sup></td>
    <td>2.980</td>
    <td>0.305</td>
  </tr>
</table>

<sup>a</sup> Reference [24].
<sup>b</sup> Reference [25],
<sup>c</sup> Reference [26].

It is noteworthy that the rutile has a tetragonal structure, with the P42/mnm space group and its primitive cell contains two $TiO_2$ units, in which $Ti^{4+}$-ions are at (0,0,0) and (0.5,0.5,0.5) positions, and $O^{2-}$-ions are at ±(u,u,0) and ±(0.5+u,0.5-u,0) positions [14] as schematically represented in FIGURE 1.

Then, the optimized lattice parameters are slightly different compared with the experiment and are found to be in good accord using LDA (underestimated by 1.6%) than using GGA (overestimated by about 4%). Next, the electronic and optical properties of rutile are investigated for both sets of lattice parameters, corresponding to the used exchange and correlation functional, which is described by either LDA or GGA approximations.


![](./images/812816053364064257_2.jpg)

**FIGURE 1.** The primitive unit cell of rutile TiO₂

# Electronic Band Structure

Along the high-symmetry points of Brillouin zone, the band structure of the rutile has been calculated. The corresponding results are presented in FIGURE 2.

We found that the bottom of the conduction band (CB) occurred to the top of the valence band (VB). This correspondence is located exactly at Gamma high symmetry point ($\Gamma$). This proves also that the tetragonal rutile is a semiconductor material with wide direct bandgap.

![](./images/812816053364064257_3.jpg)

**FIGURE 2.** pw-LDA (left) and pbe-GGA (right) calculated band structure of rutile along high-symmetry points within the first Brillouin zone. The horizontal line at 0 eV is the Fermi energy level

The fundamental pw-LDA and pbe-GGA band gap energies at $\Gamma$-point are calculated to be 2.14 eV and 2.34 eV respectively and the experimental value is around 3.0 eV [24] . The obtained values of band gap are reported in TABLE 2 with some theoretical and experimental results.

**TABLE 2.** Calculated and measured band gap energy of rutile

<table>
  <thead>
    <tr>
      <th></th>
      <th>Method</th>
      <th>Band gap energy (eV)</th>
      <th>Band gap nature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Present work</td>
      <td>pbe-GGA</td>
      <td>2.34</td>
      <td>$\Gamma$-$\Gamma$ direct</td>
    </tr>
    <tr>
      <td>pw-LDA</td>
      <td>2.14</td>
      <td>$\Gamma$-$\Gamma$ direct</td>
    </tr>
    <tr>
      <td rowspan="3">Other works</td>
      <td>pbe-GGA</td>
      <td>$1.88^{\text{a}}$; $2.10^{\text{b}}$, $1.94^{\text{c}}$</td>
      <td>$\Gamma$-$\Gamma$ direct</td>
    </tr>
    <tr>
      <td>Experiments</td>
      <td>$3.00^{\text{d}}$, $3.05^{\text{e}}$</td>
      <td>-</td>
    </tr>
    <tr>
      <td>OLCAO-LDA$^{\text{g}}$</td>
      <td>$1.78^{\text{f}}$</td>
      <td>$\Gamma$-$\Gamma$ direct</td>
    </tr>
  </tbody>
</table>

$^{\text{a}}$ Reference [27].
$^{\text{b}}$ Reference [28].
$^{\text{c}}$ Reference [29].
$^{\text{d}}$ Reference [24].

020005-3

$^\text{e}$Reference [30].
$^\text{f}$Reference [2].
$^\text{g}$First principle method named: Orthogonalized-linear-combinations of atomic orbitals.

Please note that the underestimation of the bandgap energy is principally because of the well-known problem of DFT [31]. In fact, both LDA and GGA are insufficiently able to describe all interactions via either their produced exchange and correlation energies or their derivative energies.

In addition, our DFT calculations are done at a temperature of 0K, while the experiment was performed at room temperature [32]. This fact is proved by the band gap found above.

To investigate the total and partial densities of states for both functional, we have used the tetrahedron method as proposed by Blochl et al. [33]. The results are reported in
FIGURE 3 and
FIGURE 4.

![](./images/812816053364064257_4.jpg)

FIGURE 3. pbe-GGA (left) and pw-LDA (right) calculated total densities of states of rutile

![](./images/812816053364064257_5.jpg)

![](./images/812816053364064257_6.jpg)

FIGURE 4. pbe-GGA (left) and pw-LDA (right) calculated partial Ti₃d, O₂d, O₂p and Ti₂p densities of states of rutile

Based on our DOS and PDOS results, we note that the width of the top VB is found to be 5.28 eV (GGA) and 5.65 eV (LDA). These values are in good agreement with the experimental value of 5.4 eV as reported by Kowalczyk et al. [34]. In the case of the width of the bottom CB, it is found to be 5.8 eV (GGA) and 7.1 eV (LDA). It appears that only GGA is in a good line with the value of 5.9 eV reported by Shang di-Mo et al. [2].

The calculated PDOS proves that the VB is mainly formed by O₂ₚ states and CB is consisting of Ti₃d orbitals. Moreover, these contributions indicate the presence of remarkable hybridization between Ti₃d and O₂ₚ states inside the material.

# Optical Properties

As previously mentioned, rutile phase has a tetragonal structure. This particularity makes it a uniaxial birefringent crystal with anisotropic optical behavior. Consequently, the optical properties are perceived to be dramatically dependent on the polarization direction of the incident light.

The frequency-dependent imaginary and real parts of dielectric function in one-, two- (ordinary) and three-direction (extraordinary) are carried out. The dielectric function is defined as:
$\varepsilon_{ij}(\omega)=\varepsilon_{ij1}(\omega)+\mathrm{i}\varepsilon_{ij2}(\omega)$, where $\varepsilon_{ij1}(\omega)$ and $\varepsilon_{ij2}(\omega)$ are respectively the real and imaginary parts. We note that the electronic polarizability is associated to $\varepsilon_{ij1}(\omega)$ part while the absorption, i.e. the response of the material to the incident photon, is associated to $\varepsilon_{ij2}(\omega)$ term.

According to the band theory, and taking into consideration that no interaction exists between electrons and holes inside the material, the complex dielectric function is determined relating to random phase approximation (RPA) and can be expressed as [35]:

$$
\varepsilon_{ij}(\omega)=\left[1+\frac{\mathrm{e}^{2}}{\varepsilon_{0}\Omega\mathrm{m}_{\mathrm{e}}^{2}}\sum\frac{\mathrm{M}_{ij}^{nn'}\left[f\left(E_{kn}\right)-f\left(E_{kn'}\right)\right]}{\left[\left(E_{kn}\right)-\left(E_{kn'}\right)\right]^{2}}\right]+\left[\frac{1}{\left(\omega_{kn'}-\omega_{kn}\right)+\omega+i\omega\Gamma}+\frac{1}{\left(\omega_{kn'}-\omega_{kn}\right)-\omega-i\omega\Gamma}\right] \tag{1}
$$

Where: e denotes the electron charge; $\mathrm{m}_{e}$ is the mass of electron, $\Omega$ is the volume of the primitive cell, $\omega$ is the frequency of incident light, $E_{kn'}$ and $E_{kn}$ represent the energy of the final (empty CB) and initial (occupied VB) states respectively. We denote by $f(E_{kn'})$ and $f(E_{kn})$ the functions of Fermi-Dirac distribution for the both states respectively.

The term $M_{ij}^{nn'}$ denotes the transition moment from $n$ (valence with energy $E_{kn}$) to $n'$ (conduction with energy $E_{kn'}$) transitions, for the $ij^{th}$ direction.

The imaginary part of dielectric function is found by means of the Drude-Lorentz equations as given by the following formula [36]:

$$
\varepsilon_{i j 2}(\omega)=\frac{\omega_{p}^{2}}{\mathrm{~N} \Omega \mathrm{m}_{\mathrm{e}}}\left[\sum_{n, k} \frac{d f\left(E_{k n}\right)}{d E_{k n}} \frac{\omega \eta \mathrm{M}_{i j}^{n n^{\prime}}}{\omega^{4}+\eta^{2} \omega^{2}}+2 \sum_{n, n^{\prime}} \sum_{k} \frac{f\left(E_{k n}\right)}{\left(E_{k n^{\prime}}\right)-\left(E_{k n}\right)} \frac{\Gamma \eta \mathrm{M}_{i j}^{n n^{\prime}}}{\Delta}\right] \text { (2) }
$$

Where: $\Delta=\left[\left(\omega_{k n^{\prime}}-\omega_{k n}\right)^{2}-\omega^{2}\right]^{2}+\Gamma^{2} \omega^{2}$, $\omega_{p}=\sqrt{\left(e^{2} \mathrm{~N}\right) /\left(\varepsilon_{0} \mathrm{~m}_{\mathrm{e}}\right)}$ is the plasma frequency of free-electron and N is the number of electrons within the unit cell volume. The coefficient $\Gamma=2 \eta / \hbar$ is a factor due to the scattering and $k$ indicates the wave vector. Note that the validity of Drude-Lorentz approximation requires that the coefficients $\Gamma$ and $\eta$ must be as smaller as possible. Equation (1) is partitioned into two terms as follows: the real term treats the intra-band transitions i.e. either conduction-to-conduction or valence-to-valence transitions and the imaginary term accounts for inter-band transitions i.e. transitions from VBs (indexed by $n$) to CBs (indexed by $n$'). The summation of all these transitions, over $n$ and $n$' states, is the contribution to the complex dielectric function.

The real part is determined by applying the Kramer-Kronig transformations [37] to the equation (2) and can be written as [36]:

$$
\varepsilon_{i j 1}(\omega)=1-\frac{\omega_{\mathrm{p}}^{2}}{\mathrm{~N} \Omega m_{\mathrm{e}}}\left[\sum_{n, k} \frac{d f\left(E_{k n}\right)}{d E_{k n}} \frac{\omega^{2} \mathrm{M}_{i j}^{n n^{\prime}}}{\omega^{4}+\eta^{2} \omega^{2}}-\left(2 \sum_{n, n^{\prime}} \sum_{k} \frac{f\left(E_{k n}\right)}{\left(E_{k n^{\prime}}\right)-\left(E_{k n}\right)} \frac{\left(\Delta-\Gamma^{2} \omega^{2}\right) \mathrm{M}_{i j}^{n n^{\prime}}}{\Delta}\right)\right] \text { (3) }
$$

Based on the above equations, the optical properties are computed by taking into account the calculated band structures. The obtained results for the photon energy ranging from 0 to 15 eV are reported in FIGURE 5.

![](./images/812816053364064257_7.jpg)

FIGURE 5. Frequency-dependent real and imaginary parts of the complex dielectric function, along the ordinary and extraordinary polarization directions using LDA (left) and GGA (right) calculations

From the imaginary part curve of $\varepsilon_{2}(\omega)$ , there are notably two principal peaks: the first one is located in the range between 4 - 5 eV and 4.1 - 4.9 eV for both polarization directions and under LDA and GGA approximation respectively. The second is higher 8.5 eV for LDA approximation. The origin of these peaks is as follows: the first peak is mainly due to the inter-band optical transitions between the top VB and the bottom CB (direct transitions) and the second one is the result of transitions (higher incident photon energies) between the same top VB and other conduction bands (indirect transitions).

These results correspond to results of Uchida et al. [38], obtained by using the two-oscillator model to compute optical properties. They similarly found that the two types of transitions are in 4-6 eV and 9-11 eV regions. Through the
020005-6

real parts curves of **FIGURE 5**, the high-frequency dielectric constants are determined depending on the polarization direction, as listed in TABLE 3.

**TABLE 3.** Calculated high-frequency dielectric constants of rutile

<table>
  <thead>
    <tr>
      <th colspan="2">Method</th>
      <th>$\varepsilon_{11}(\infty)$=$\varepsilon_{22}(\infty)$</th>
      <th>$\varepsilon_{33}(\infty)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Present work</td>
      <td>GGA</td>
      <td>7.20</td>
      <td>8.33</td>
    </tr>
    <tr>
      <td>LDA</td>
      <td>5.44</td>
      <td>6.23</td>
    </tr>
    <tr>
      <td rowspan="3">Other works</td>
      <td>pbe-GGA</td>
      <td>7.80<sup>a</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>LDA</td>
      <td>7.53<sup>b</sup></td>
      <td>8.66</td>
    </tr>
    <tr>
      <td>OLCAO-LDA</td>
      <td>6.46<sup>c</sup></td>
      <td>6.95</td>
    </tr>
  </tbody>
</table>

<sup>a</sup> Reference [29].
<sup>b</sup> Reference [25].
<sup>c</sup> Reference [2].

We note that the GGA calculated electronic (high frequency) dielectric constant is closer to the results of other theoretical works as illustrated in the

Across the large band gap of rutile, no carries are excited at room temperature, which means that there is no absorption of free IR photons. The inter-bands transitions are essentially considered for high energies of incident photon (i.e. visible and IR frequencies). Consequently, insulators, such as rutile, are transparent in the optical spectra.

Refractive indices as function of energy of incident photon are further calculated using the following equation, according to the Maxwell model [39]:

$$
\mathrm{n}_{i j}(\omega)=\frac{1}{\sqrt{2}} \sqrt{\overline{\varepsilon_{i j 1}(\omega)+\varepsilon_{i j 2}(\omega)}+\varepsilon_{i j 1}(\omega)} \tag{4}
$$

**FIGURE 6** shows the calculated refractive indices for both polarization directions as a function of the incident photon energy.

![](./images/812816053364064257_8.jpg)

**FIGURE 6.** Ordinary and extraordinary refractive indices of rutile, corresponding to GGA (top) and LDA (bottom) calculations as a function of the energy of the incident photon

The two spectra indicate that the highest values of refractive indices are located in the visible and infrared ranges especially between 2 eV and 4 eV for both used approximations. These values increase as the energy decreases.

Moreover, the optical birefringence which is defined as the difference between extraordinary and ordinary refractive indices, is calculated to be 0.23 (GGA) and 0.269 (LDA) respectively at 633 nm (1.96 eV). These value agree well with the measured value of 0.27 reported by Rams et al [1]. This large optical birefringence leads to the high optical anisotropy of the material.

# CONCLUSION

In summary, our DFT calculations based upon the plane waves self-consistent field and norm-conserving pseudo- potentials show that the optimized lattice parameters of rutile are more reasonable using GGA than with LDA. The calculated electronic properties such as band gap, total and partial densities of states predicted that the pure rutile is a wide direct gap semiconductor material. Besides, it is proved that remarkable hybridization exists between Ti₃d states,

which form the $CB$, and $O_{2p}$ states, which form the $VB$. These states are mainly responsible for the bonding formation within the crystal.

Compared to experiments and other DFT studies, our calculations based on GGA show a good agreement than the LDA method. The results show that the rutile has high refractive indices and optical anisotropy, especially in the visible and near-IR light.

The majority of discrepancies are attributed to underestimating nature of band gap, because of the well-known problem of DFT methods, which doesn't take into consideration the many body effects. Regardless, the LDA and GGA approximations are successfully used to investigate the electronic and optical behavior of insulator materials, namely $TiO_2$.

Furthermore, our study predicted that the choice of exchange correlation functional within the DFT has a considerable effect on electronic and optical calculations.

## REFERENCES

1.  J. Rams, A. Tejeda, and J.M. Cabrera, *J. Appl. Phys.* **82**, 994 (1997).
2.  S. Di Mo and W.Y. Ching, *Phys. Rev. B* **51**, 13023 (1995).
3.  G. Liu, L. Wang, H.G. Yang, H.-M. Cheng, and G.Q. (Max) Lu, *J. Mater. Chem.* **20**, 831 (2010).
4.  J. Houska, S. Mraz, and J.M. Schneider, *J. Appl. Phys.* **112**, 073527 (2012).
5.  A. Fahmi, C. Minot, B. Silvi, and M. Causá, *Phys. Rev. B* **47**, 11717 (1993).
6.  A. Fujishima and K. Honda, *Nature* **238**, 37 (1972).
7.  M. Grätzel, *Comments Inorg. Chem.* **12**, 93 (1991).
8.  A. Bouaine, G. Schmerber, D. Ihiawakrim, and A. Derory, *Mater. Sci. Eng. B* **177**, 1618 (2012).
9.  K.L. Siefering and G.L. Griffin, *J. Electrochem. Soc.* **137**, 1206 (1990).
10. A. Grünebohm, P. Entel, and C. Ederer, *Phys. Rev. B - Condens. Matter Mater. Phys.* **87**, 1 (2013).
11. B.S. Richards and U. of New South Wales. Centre for Photovoltaic Engineering, (2002).
12. S. Sekiya, Takao Yagisawa, Takatoshi Kurita, *J. Ceram. Soc. Japan* **109**, 672 (2001).
13. H. Selhofer and R. Müller, *Thin Solid Films* **351**, 180 (1999).
14. J. Muscat, V. Swamy, and N.M. Harrison, *Phys. Rev. B - Condens. Matter Mater. Phys.* **65**, 2241121 (2002).
15. R. Asahi, Y. Taga, W. Mannstadt, and A. Freeman, *Phys. Rev. B* **61**, 7459 (2000).
16. F.M. Hossain, L. Sheppard, J. Nowotny, and G.E. Murch, *J. Phys. Chem. Solids* **69**, 1820 (2008).
17. M.L. and E.R. and W.G. Schmidt, *J. Phys. Condens. Matter* **24**, 195503 (2012).
18. P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A.P. Seitsonen, A. Smogunov, P. Umari, and R.M. Wentzcovitch, *J. Phys. Condens. Matter* **21**, 395502 (2009).
19. D.R. Hamann, M. Schlüter, and C. Chiang, *Phys. Rev. Lett.* **43**, 1494 (1979).
20. J.P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).
21. J.P. Perdew and Y. Wang, *Phys. Rev. B* **45**, 13244 (1992).
22. W. Kohn and L.J. Sham, *Phys. Rev.* **140**, A1133 (1965).
23. H.J. Monkhorst and J.D. Pack, *Phys. Rev. B* **13**, 5188 (1976).
24. D. Reyes-Coronado, G. Rodríguez-Gattorno, M.E. Espinosa-Pesqueira, C. Cab, R. d de Coss, and G. Oskam, *Nanotechnology* **19**, 145605 (2008).
25. C. Lee and X. Gonze, *Phys. Rev. B* **49**, 14730 (1994).
26. M.M. Islam, T. Bredow, and A. Gerson, *Phys. Rev. B - Condens. Matter Mater. Phys.* **76**, 1 (2007).
27. M. Landmann, T. Köhler, S. Köppen, E. Rauls, T. Frauenheim, and W. Schmidt, *Phys. Rev. B* **86**, 064201 (2012).
28. R. Faccio, L. Fernández-werner, H. Pardo, and Á.W. Mombrú, 46 (2011).
29. M. Mohamad, B.U. Haq, R. Ahmed, A. Shaari, N. Ali, and R. Hussain, *Mater. Sci. Semicond. Process.* **31**, 405 (2015).
30. H. Tang, K. Prasad, R. Sanjinès, P.E. Schmid, and F. Lévy, *J. Appl. Phys.* **75**, 2042 (1994).
31. P. Dufek, P. Blaha, and K. Schwarz, *Phys. Rev. B* **50**, 7279 (1994).
32. J.H. Park, Y.Y. Choi, H.K. Kim, H.H. Lee, and S.I. Na, *J. Appl. Phys.* **108**, (2010).
33. P.E. Blöchl, O. Jepsen, and O.K. Andersen, *Phys. Rev. B* **49**, 16223 (1994).
34. S.P. Kowalczyk, F.R. McFeely, L. Ley, V.T. Gritsyna, and D.A. Shirley, *Solid State Commun.* **23**, 161 (1977).
35. H. Ehrenreich and M.H. Cohen, *Phys. Rev.* **115**, 786 (1959).
36. T. Tsafack, E. Piccinini, B.-S. Lee, E. Pop, and M. Rudan, *J. Appl. Phys.* **110**, 63716 (2011).
37. R. de L. Kronig, *JOSA* **12**, 547 (1926).
38. N. Uchida, *J. Appl. Phys.* **44**, 2072 (1973).
39. S. Saha, T. Sinha, and A. Mookerjee, *Phys. Rev. B* **62**, 8828 (2000).
40.

020005-8