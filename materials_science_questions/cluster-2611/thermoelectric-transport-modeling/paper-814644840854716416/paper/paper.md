# Impact of Ferroelectric Distortion on Thermopower in $BaTiO_3$

Hiroaki Saijo, Kunihiko Yamauchi*, Koun Shirai, and Tamio Oguchi

ISIR-SANKEN, Osaka University, Ibaraki, Osaka 567-0047, Japan

(Received December 15, 2014; accepted February 16, 2015; published online April 2, 2015)

We present a strategy for increasing thermoelectric performance by invoking ferroelectric distortion in a transition-metal oxide. By using an ab initio calculation approach with the Boltzmann transport equation, large Seebeck coefficients are calculated for $n$-type $BaTiO_3$. The polar structural distortion causes the peculiar dispersion of the lowest conduction band, which enhances the Seebeck coefficients along the polar direction. A microscopic mechanism of carrier concentration dependence of the Seebeck coefficients is discussed in terms of the band velocity distribution in the Brillouin zone.

## 1. Introduction

Owing to the recent growth in concern about energy issues, thermoelectric power has been attracting much attention since it can recover waste heat and be used as a Peltier cooler without producing greenhouse gas emissions. Motivated by the advances in the thermoelectric applications, a key issue in the material science research field has been to improve thermoelectric efficiency. The maximum thermoelectric performance at a temperature $T$ is determined by a dimensionless figure of merit, $ZT = S^2\sigma T/\kappa$, which depends on the Seebeck coefficients ($S$), the electrical conductivity ($\sigma$), and the thermal conductivity ($\kappa$) including the electronic and lattice contributions. By assuming a parabolic electronic band and an energy-independent scattering approximation, $^{1)}$ $S$ is described as $S = (8\pi k_{\text{B}}^2/3eh^2)m^*T(\pi/3n)^{2/3}$, where $n$ is the carrier concentration and $m^*$ is the effective mass of the carriers. The thermal conductivity is further decomposed into the electronic and phonon contributions: $\kappa = \kappa_{\text{el}} + \kappa_{\text{ph}}$. Since $S (\propto n^{-2/3})$ and $\sigma (\propto n)$ show a trade-off dependence on $n$, it is not easy to optimize the thermoelectric performance in the range of $n$ limited for practical use. Moreover, $m^*$ may cause another conflict; a larger effective mass produces a higher $S$ but a lower $\sigma$. Therefore, the design of highly thermoelectric materials involves finding the optimized balance of $S$, $\sigma$, and $\kappa.^{2,3)}$ The conventional strategy for enhancing $ZT$ is to employ heavy elements and narrow-gap semiconductors to reduce $\kappa$. For example, $Bi_2Te_3$ — now widely considered as a representative topological insulator $^{4)}$ — shows $ZT \gtrsim 1$ at appropriate temperatures. $^{5)}$ These materials are in practical use, however, are toxic to humans.

Since the noteworthy finding of large Seebeck coefficients for $Na_xCoO_2,^{6)}$ transition-metal oxides have emerged as another category of thermoelectrics. Electron-doped $SrTiO_3$ and $KTaO_3$ have been found to have large Seebeck coefficients $S,^{7,8)}$ which are comparable to that of $Bi_2Te_3$, while also having high (metallic) conductivity $\sigma$. Several density functional theory (DFT) calculations have been performed on thermoelectric transition-metal oxides, which have mostly concluded that narrow $t_{2g}$ bands with the large $m^*$ are responsible for the large Seebeck coefficients. $^{9,10)}$ Later on, Kuroki and co-workers pointed out that a particular pudding-mold $a_{1g}$ band may enhance both $S$ and $\sigma$ in the dumbbell-type structure in $Na_xCoO_2$ and $CuAlO_2.^{11,12)}$ For $SrTiO_3$ and $KTaO_3$, they claimed that the multiplicity of the threefold $t_{2g}$ state plays a role in enhancing $S$ and $\sigma$. When electrons are doped into the empty $t_{2g}$ bands, the multiple bands can maintain a low Fermi level, which in turn results in large Seebeck coefficients, while the doped electrons increase the conductivity. $^{13)}$ Recently, Shirai and Yamanaka gave another interpretation of the large thermopower of $SrTiO_3$ as follows. $^{14)}$ It is often considered that the $t_{2g}$ components of $d$ electrons form dispersion-less and threefold degenerate bands. However, the lift of the degeneracy upon leaving the $\Gamma$ point should not be overlooked. As far as electron doping is concerned, only the lowest band is relevant. More importantly, even a single band can have electrons of considerably different masses in different regions of the Brillouin zone. A light electron leads to a large $\sigma$, whereas a heavy electron results in a large $S$, increasing the power factor $S^2\sigma$. If this idea is valid, it is more critical to have a strongly anisotropic $m^*$ in a single band than multiply degenerate bands for enhancement of the thermopower in oxides. In this context, we focus on the $t_{2g}$ bandstructure in $BaTiO_3$, in which the ferroelectric crystal distortion is expected to enhance the anisotropy of $m^*$ and to enhance the thermoelectric properties. In fact, an early experimental finding of the anisotropic Seebeck coefficients of $BaTiO_3$ was reported in $1967,^{15)}$ before accurate theoretical approaches to understanding the electronic properties had been developed. In the present study, we aim to confirm the effect of the polar distortion on the $t_{2g}$ band and the resulting thermoelectric properties of $BaTiO_3$. We discuss the microscopic mechanism of the enhancement of $S$ and $\sigma$ by means of first-principles DFT calculations.

## 2. Bandstructure and Wannier Interpolation

Perovskite $BaTiO_3$ is a well-known ferroelectric oxide that undergoes a ferroelectric transition at 393 K. To obtain the electronic structure of ferroelectric $BaTiO_3$, we performed DFT calculations using the VASP code $^{16)}$ with the generalized gradient approximation Perdew-Burke-Ernzerhof (GGA-PBE) potential. $^{17)}$ The tetragonal lattice constants of $a = 3.991$ Å and $c = 4.035$ Å were taken from an experimental result at room temperature. $^{18)}$ The internal atomic coordinates were optimized until the forces acting on atoms were less than $1 \times 10^{-3}$ eV/Å for both the paraelectric (centrosymmetric) structure and the ferroelectric (polar) structure as shown in Fig. 1. A $(12, 12, 12)$ $k$-point mesh was used for the Brillouin zone integration. Although the actual crystal structure at the paraelectric phase ($T > 393$ K) is known to be cubic, we used the same tetragonal lattice for both para-

![](./images/814644840854716416_1.jpg)

Fig. 1. (Color online) Tetragonal unit cell of BaTiO₃ in the (a) paraelectric (PE) structure and (b) ferroelectric (FE) structure. Apical and side oxygens are denoted as Oᵃᵖ and Oˢ, respectively. The directions of the polar atomic distortions and the polarization are shown by block arrows. The polar displacements are exaggerated by a factor of two for clarity.

![](./images/814644840854716416_2.jpg)

Fig. 2. Polar ionic displacement, defined as the change in the bond length between Ti and Oᵃᵖ ions in BaTiO₃, as a function of the electron doping rate x.

![](./images/814644840854716416_3.jpg)

Fig. 3. (Color online) Bandstructures of BaTiO₃ in (a) paraelectric and (b) ferroelectric phases. (c) and (d) are magnified versions. The Wannier-interpolated Ti-t₂g bands are superposed on the DFT bandstructure, as highlighted by (red) solid lines in (a) and (b).

electric and ferroelectric structures to discuss the effect purely caused by the polar ionic displacement. The ferroelectric polarization in nondoped BaTiO₃ was calculated by the Berry phase approach¹⁹ to be $P^{\text{DFT}} = 26\ \mu\text{C/cm}^2$ along the c axis, which is in good agreement with the experimental value of $P^{\text{exp}} = 27\ \mu\text{C/cm}^2$²⁰ and the previously calculated values of $P^{\text{DFT}} = 22$–$29\ \mu\text{C/cm}^2$.²¹,²² The polarization can be decomposed into the ionic and electronic contributions; $P^{\text{DFT}} = P^{\text{ion}} + P^{\text{elec}}$, where the ionic contribution was calculated by a point-charge model assuming nominal ionic valences of +2, +4, −2 for Ba, Ti, and O ions, respectively. The calculated $P^{\text{ion}}$ of $14\ \mu\text{C/cm}^2$, which is almost half of the total polarization, originates from the ionic displacement of Ti and O due to the strong hybridization between occupied O-p and unoccupied Ti-$d^0$ states, known as the $d^0$-ness mechanism.²³ Figure 2 shows the polar ionic displacement as a function of electron doping. When an electron is doped in BaTiO₃, the Fermi energy moves in the unoccupied Ti-t₂g bands. This screens the electric potential of the ionic charge and interferes with the ferroelectricity. Nevertheless, the polar ionic displacement (i.e., the ionic contribution to P) is rather robust and remains almost 90% even for 0.05 e of electron doping in the Ti-$d^0$ state, consistent with a previous theoretical study in Ref. 24. This result ensures that the crystal structure maintains the polar distortion up to a certain amount of electron doping (e.g., $x \lesssim 0.1$), which is sufficient for the following discussion on the electron-doped BaTiO₃ with the ferroelectric structure. Technically speaking, the cubic-tetragonal (centrosymmetric-polar) transition temperature may decrease upon electron doping, although the polar ionic distortion will persist below the transition temperature. It was reported that the transition temperature remains above room temperature until 0.022 e/u.c. doping, while higher doping may lead to a lower transition temperature.²⁵ For the thermoelectric application of BaTiO₃, tuning of the polar property under electron doping will be required. For example, both the polar distortion and the transition temperature can be largely increased by applying epitaxial strain in a BaTiO₃ thin film.²⁶,²⁷

Figure 3 shows the bandstructures of BaTiO₃ in the paraelectric and ferroelectric phases. They consist of nine O-p bands below the Fermi energy, and three Ti-t₂g and two e_g bands above the Fermi energy. The three Ti-t₂g bands lying at the conduction band bottom are well isolated from the other bands. Owing to the tetragonal symmetry of the crystal structure, the t₂g bands are split into (yz, zx) and xy bands at the Γ point. The former can be further split along the Γ–X line, where the fourfold rotation symmetry is broken. The symmetry-lowering effect is significantly enhanced in the ferroelectric structure. It is intriguing that the (yz, zx)

![](./images/814644840854716416_4.jpg)

Fig. 4. (Color online) Isosurface of MLWF for Ti-$d_{zx}$ orbital state hybridized with the surrounding O-$p$ states in the ferroelectric structure.
The hopping integrals between the $d_{zx}$ and the side (s) and apical (ap) oxygen
$p$ states are shown by arrows.

<table>
<caption>Table I. Calculated hopping integrals $t$ (eV) and bond lengths $l$ (Å) between Ti-$d_{(yz,zx)}$ and side (s) and apical (ap) O-$p$ orbital states in the paraelectric (PE) and ferroelectric (FE) structures.</caption>
<thead>
<tr>
<th></th>
<th>$t^{\rm s}$</th>
<th>$t_1^{\rm ap}$</th>
<th>$t_2^{\rm ap}$</th>
<th>$l^{\rm s}$</th>
<th>$l_1^{\rm ap}$</th>
<th>$l_2^{\rm ap}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>PE</td>
<td>1.03</td>
<td>0.98</td>
<td>0.98</td>
<td>2.00</td>
<td>2.02</td>
<td>2.02</td>
</tr>
<tr>
<td>FE</td>
<td>1.03</td>
<td>1.34</td>
<td>0.72</td>
<td>2.00</td>
<td>1.89</td>
<td>2.15</td>
</tr>
</tbody>
</table>

bands are at the conduction bottom in the paraelectric structure, whereas the $xy$ band is at the bottom in the ferroelectric structure. This is caused by strong Ti-O$^{\rm ap}$ hybridization, which pushes up the antibonding $(yz,zx)$ bands in the ferroelectric structure. In Fig. 3(d), it can be observed that the $xy$ and $zx$ bands (which belong to the same irreducible representation $\Delta_2$) repel each other along the $\Gamma$-X line, resulting in the particularly nonparabolic band shape. The lowest $t_{2g}$ band is responsible for the thermoelectric properties since the electrons will be doped into this band. For the further analysis of the thermoelectric properties, the $t_{2g}$ bands were interpolated by means of maximally localized Wannier functions (MLWFs) using the Wannier90 code. $^{28,29)}$

Figure 4 shows one example of the calculated MLWF for the Ti-$d_{zx}$ state. Table I shows the related hopping integrals between the Ti-$d_{zx}$ and O-$p$ states calculated via the off-diagonal Hamiltonian element for the MLWF basis together with the Ti-O bond length. In the ferroelectric structure, a Ti ion is slightly displaced toward one of the apical oxygens by $0.13\,\mathring{\text{A}}$, which considerably enhances the hopping integral. Therefore, the MLWF of Ti-$d_{zx}$ has a larger weight at the top apical oxygen site than at the bottom apical oxygen site. As shown in Table I, the calculated hopping with the closer O-$p$ state is almost double that for the other state ($t_1^{\rm ap} \gg t_2^{\rm ap}$). The anisotropic enhancement of $t$ is directly related to the $d^0$-ness microscopic origin of the ferroelectric distortion, by which the energy gap is increased to lower the band energy and to stabilize the ferroelectric structure. $^{23)}$ The anisotropic hopping integral slightly modulates the bandstructure but has a major impact on the thermoelectric properties.

## 3. Thermoelectric Properties

The standard Boltzmann transport approach was adopted in the present study to calculate the Seebeck coefficients. $^{30)}$ In this approach, the Seebeck coefficients are given by

$$
S(\mu, T)=\frac{1}{e T} \frac{\boldsymbol{K}_{1}(\mu, T)}{\boldsymbol{K}_{0}(\mu, T)},\qquad(1)
$$

where $e$ is the electron charge, $T$ is the temperature, and $\boldsymbol{K}_{0}$ and $\boldsymbol{K}_{1}$ are given by

$$
\boldsymbol{K}_{i}(\mu, T)=\int_{-\infty}^{\infty} d \varepsilon \sum_{n \boldsymbol{k}} \tau \boldsymbol{v}_{n \boldsymbol{k}} \boldsymbol{v}_{n \boldsymbol{k}}\left[-\frac{\partial f(\varepsilon, \mu, T)}{\partial \varepsilon}\right]\left(\varepsilon_{n \boldsymbol{k}}-\mu\right)^{i}\ (2)
$$

for $i=0,1$. Here, $\varepsilon_{n \boldsymbol{k}}$ is the band energy, $\boldsymbol{v}_{n \boldsymbol{k}}$ is the band velocity, $\tau$ is the quasiparticle lifetime assumed to be constant, $f(\varepsilon)$ is the Fermi distribution function, and $\mu$ is the chemical potential. To accurately calculate the band velocity (with band index $n$)

$$
\boldsymbol{v}_{n \boldsymbol{k}}=\frac{1}{\hbar} \frac{\partial \varepsilon_{n \boldsymbol{k}}}{\partial \boldsymbol{k}},\qquad(3)
$$

the Wannier function approach implemented in the BoltzWann$^{31)}$ code was employed. The $\boldsymbol{k}$-point mesh was increased to $(160,160,160)$ to reach convergence. The electrical conductivity $\boldsymbol{\sigma}$ was also calculated as

$$
\boldsymbol{\sigma}(\mu, T)=\frac{e^{2} \tau}{V} \int_{-\infty}^{\infty} d \varepsilon\left(-\frac{\partial f(\varepsilon, \mu, T)}{\partial \varepsilon}\right) \sum_{n, \boldsymbol{k}} \boldsymbol{v}_{n \boldsymbol{k}}^{2} \delta\left(\varepsilon-\varepsilon_{n, \boldsymbol{k}}\right).\ (4)
$$

In Fig. 5(a), we show the calculated Seebeck coefficients as a function of temperature $T$ at a fixed doping rate of $x=0.03$. In this calculation, the rigid band approximation was assumed. In the paraelectric structure, $S_{xx}$ and $S_{zz}$ have similar values. $S_{xx}$ reaches $-122\,\mu\text{V/K}$ at $T=300\,\text{K}$ and $x=0.03$, consistent with the previously calculated value for $\text{SrTiO}_{3}$ of $S_{xx}=-87\,\mu\text{V/K}$ at $T=300\,\text{K}$ and $x=0.05$. $^{13)}$ However, as discussed in Ref. 13, the calculated $S$ value for $\text{SrTiO}_{3}$ is reduced almost half compared with the experimental result. This is due to the strong correlation effect of the $3d$ state, whose band width is usually overestimated in DFT calculations. To improve the correspondence to the actual value of $S$, we should note that the $S$ value predicted by DFT calculations is underestimated by roughly a factor of two. In the ferroelectric case, the calculated Seebeck coefficients show strong anisotropy, $S_{zz} \gg S_{xx}$. At $T=300\,\text{K}$ and $x=0.03$, $S_{zz}$ is calculated to be $-230\,\mu\text{V/K}$, which is almost four times larger than $S_{xx}=-74\,\mu\text{V/K}$. This value may be comparable to the experimentally measured $S \approx 300\,\mu\text{V/K}$ for epitaxial La-doped $\text{BaTiO}_{3}$. $^{32)}$ Figure 5(b) shows the calculated Seebeck coefficients as functions of the doping rate $x$. $S_{zz}$ behaves anomalously with increasing $x$, exhibiting a large "bump" at $x=0.03$. This is caused by the anisotropic property of the Fermi surfaces and the effective mass due to the ferroelectric ionic displacement, as explained in Sect. 4. This results in the remarkable crossover of the power factor $(S^2 \sigma)$ between the paraelectric and ferroelectric phases at $x \sim 0.05$ as shown in Fig. 5(c).

## 4. Effect of Ferroelectric Distortion

Here, we discuss the microscopic origin of the enhancement and the anisotropic behavior of the Seebeck coefficients $S$ for ferroelectric $\text{BaTiO}_{3}$. We note that the enhancement of

![](./images/814644840854716416_5.jpg)

Fig. 5. (Color online) (a) Calculated Seebeck coefficients for $x = 0.03$ plotted as a function of temperature for ferroelectric (FE) and paraelectric (PE) crystal structures. (b) Calculated Seebeck coefficients and (c) power factor (PF) (divided by $\tau$) as a function of the doping rate $x$ at $T = 300$ K. The diagonal matrix elements $zz$ (polar axis) and $xx$ are plotted by solid and dotted lines, where broad and narrow lines correspond to FE and PE structures, respectively.

$S_{zz}$ originates from a single-band contribution. In the energy region of $0 < \mu < 0.5$ eV, most of the electron density of states originates from the $xy$ band at the conduction bottom, whereas the contribution from the $(yz, zx)$ bands is less than $5\%$, meaning that it does not affect the trend of $S(\mu)$. This is in clear contrast to the case of cubic $SrTiO_3$, where the three $t_{2g}$ bands have an equal contribution to $S(\mu)$. $^{11)}$

As already discussed by Usui et al., the magnitude of the Seebeck coefficients is mainly determined by the energy dependence of the electron velocity $\boldsymbol{v}_{nk}$. $^{13)}$ By making a rough approximation, $K_0$ and $K_1$ in Eq. (2) are described as

$$
K_{0} \approx \sum\left(\boldsymbol{v}_{\text {high }}^{2}+\boldsymbol{v}_{\text {low }}^{2}\right), \quad K_{1} \approx k_{\mathrm{B}} T \sum\left(\boldsymbol{v}_{\text {high }}^{2}-\boldsymbol{v}_{\text {low }}^{2}\right), \quad(5)
$$

where the summation is over the states in the range of $|\varepsilon_{\boldsymbol{k}} - \mu| \lesssim k_{\mathrm{B}}T$ and $\boldsymbol{v}_{\text{high}}$ and $\boldsymbol{v}_{\text{low}}$ are typical velocities for the states above and below $\mu$, respectively. Therefore, the case of $\boldsymbol{v}_{\text{high}} \gg \boldsymbol{v}_{\text{low}}$ leads to large Seebeck coefficients.

![](./images/814644840854716416_6.jpg)

Fig. 6. (Color online) Contour plot of $\varepsilon(\boldsymbol{k}) = \mu$ surfaces with several $\mu$ values (the origin of the chemical potential $\mu$ is taken as the bottom of the conduction bands) and the squared band velocity plotted by color for (a) $v_{x}^{2}$ and (b) $v_{z}^{2}$ for the lowest conduction band ($xy$ band) in ferroelectric $BaTiO_3$. The three-dimensional energy surfaces are shown in the right panels (i)–(iii). (c) Squared band velocity $\langle v_{x}^{2}\rangle$ and $\langle v_{z}^{2}\rangle$ integrated in the $k$-space using $\langle v_{ij}^{2}\rangle(\mu) = (1/V)\sum_{n,\boldsymbol{k}} v_{nk}v_{jnk}\delta(\mu - \varepsilon_{nk})$ for the lowest conduction band. (d) Chemical potential $\mu$ as a function of the doping rate $x$ at $T = 300$ K.

Figures 6(a) and 6(b) show the calculated $\boldsymbol{v}_{nk}^{2}$ superimposed on the sections of isoenergy surfaces $\varepsilon_{nk}$ with several $\mu$ values. With increasing $\mu$, the ellipsoidal energy isosurface is elongated along the $k_{z}$ direction for $\mu < 0.2$ eV, and then lobes develop along the $k_{x}$ and $k_{y}$ directions for $\mu > 0.2$ eV. By taking a close look at Figs. 6(a) and 6(b), it can be seen that the ellipsoidal energy surface has some amount of $v_{x}^{2}$ but almost zero $v_{z}^{2}$. When $\mu > 0.2$ eV, the energy surface starts to have a finite $v_{z}^{2}$ value. Therefore, the expectation value of $\langle v_{z}^{2}\rangle(\mu)$ is shifted rightward by 0.2 eV with respect to $\langle v_{x}^{2}\rangle(\mu)$ as shown in Fig. 6(c). For $\mu \approx 0.2$ eV, the situation $\boldsymbol{v}_{z}^{\text{high}} \gg \boldsymbol{v}_{z}^{\text{low}}$ is realized, which significantly increases $S_{zz}$. This can explain the "bump" behavior of $S_{zz}(x)$ in Fig. 5(b) at $x = 0.03$ [the relation between $\mu$ and $x$ is shown in Fig. 6(d)].

The "bump" behavior of $S(x)$ has recently been reported for SnTe on the basis of experimental observation. $^{33)}$ SnTe is now known as a topological crystalline insulator, where the

Sn-$p$ and Te-$p$ orbital characters are *inverted* at the R point between the valence-band top and conduction-band bottom. $^{34,35)}$ When a hole carrier is doped, this band inversion causes warping in the Fermi surfaces of the valence band, which in turn leads to the enhancement of $S(x).^{10,36)}$ In short, in SnTe and related systems, the strong spin-orbit coupling, which mixes the orbital character between the narrow gap, causes nonparabolic Fermi surfaces, which are responsible for the high thermoelectric performance. This is related to the present case of $BaTiO_3$, where the polar crystal distortion asymmetries the Fermi surfaces and results in the sizable enhancement of $S(x)$ along the polar direction. Using this unique property, it may be possible to control the thermoelectric performance by the piezoelectric effect. When one imposes uniaxial strain on $BaTiO_3$, both the polar axis and the thermoelectrically favored direction may be manipulated as one wishes. This effect needs to be confirmed by further theoretical and experimental studies.

## 5. Conclusions
Within Boltzmann transport theory we calculated the anisotropic Seebeck coefficients for ferroelectric $BaTiO_3$. The polar displacements of Ti and O ions cause the $t_{2g}$ band to split into the $(yz,zx)$ and the $xy$ states: the latter band in turn results in the strong anisotropy and enhancement of the Seebeck coefficients. Such a structural distortion in perovskite oxides can provide a way to asymmetrize the constant-energy surfaces and the unusual energy dependence of the band velocity. This finding may pave the way for exploring novel thermoelectrics in various ferroelectric oxides. For example, $PbTiO_3$ may have large Seebeck coefficients owing to its huge electric polarization.

## Acknowledgment
This work was supported by a Grant-in-Aid for Young Scientists (B) from the Japan Society for the Promotion of Science (No. 26800186) and by JST-CREST project "Creation of Innovative Functions of Intelligent Materials on the Basis of the Element Strategy". The computation in this work was done using the facilities of the Supercomputer Center, Institute for Solid State Physics, University of Tokyo.

*kunihiko@sanken.osaka-u.ac.jp

1) M. Cutler, J. F. Leavy, and R. L. Fitzpatrick, Phys. Rev. **133**, A1143 (1964).
2) G. J. Snyder and E. S. Toberer, Nat. Mater. **7**, 105 (2008).
3) T. Takabatake, K. Suekuni, T. Nakayama, and E. Kaneshta, Rev. Mod. Phys. **86**, 669 (2014).
4) D. Hsieh, Y. Xia, D. Qian, L. Wray, J. H. Dil, F. Meier, J. Osterwalder, L. Patthey, J. G. Checkelsky, N. P. Ong, A. V. Fedorov, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, Nature **460**, 1101 (2009).
5) T. M. Tritt, Science **272**, 1276 (1996).
6) I. Terasaki, Y. Sasago, and K. Uchinokura, Phys. Rev. B **56**, R12685 (1997).
7) T. Okuda, K. Kakanishi, S. Miyasaka, and Y. Tokura, Phys. Rev. B **63**, 113104 (2001).
8) A. Sakai, T. Kanno, S. Yotsuhashi, H. Adachi, and Y. Tokura, Jpn. J. Appl. Phys. **48**, 097002 (2009).
9) G. B. Wilson-Short, D. J. Singh, M. Fornari, and M. Suewattana, Phys. Rev. B **75**, 035121 (2007).
10) X. Chen, D. Parker, and D. J. Singh, Sci. Rep. **3**, 3168 (2013).
11) K. Kuroki and R. Arita, J. Phys. Soc. Jpn. **76**, 083707 (2007).
12) K. Mori, H. Sakakibara, H. Usui, and K. Kuroki, Phys. Rev. B **88**, 075141 (2013).
13) H. Usui, S. Shibata, and K. Kuroki, Phys. Rev. B **81**, 205121 (2010).
14) K. Shirai and K. Yamanaka, J. Appl. Phys. **113**, 053705 (2013).
15) C. N. Berglund and W. S. Baer, Phys. Rev. B **157**, 358 (1967).
16) G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).
17) J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).
18) G. H. Kwei, A. C. Lawson, S. J. L. Billinge, and S. W. Cheong, J. Phys. Chem. **97**, 2368 (1993).
19) R. D. King-Smith and D. Vanderbilt, Phys. Rev. B **47**, 1651 (1993); R. Resta, Rev. Mod. Phys. **66**, 899 (1994).
20) H. H. Wieder, Phys. Rev. **99**, 1161 (1955).
21) M. Fechner, S. Ostanin, and I. Mertig, Phys. Rev. B **77**, 094112 (2008).
22) J. J. Wang, F. Y. Meng, X. Q. Ma, M. X. Xu, and L. Q. Chen, J. Appl. Phys. **108**, 034107 (2010).
23) N. A. Hill, J. Phys. Chem. B **104**, 6694 (2000).
24) Y. Wang, X. Liu, J. D. Burton, S. S. Jaswal, and E. Y. Tsymbal, Phys. Rev. Lett. **109**, 247601 (2012).
25) T. Kolodiazhnyi, M. Tachibana, H. Kawaji, J. Hwang, and E. Takayama-Muromachi, Phys. Rev. Lett. **104**, 147602 (2010).
26) H. Miyazawa, E. Natori, T. Shimoda, H. Kishimoto, F. Ishii, and T. Oguchi, Jpn. J. Appl. Phys. **40**, 5809 (2001).
27) A. R. Damodaran, E. Breckenfeld, Z. Chen, S. Lee, and L. W. Martin, Adv. Mater. **26**, 6341 (2014).
28) N. Marzari and D. Vanderbilt, Phys. Rev. B **56**, 12847 (1997).
29) A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, Comput. Phys. Commun. **178**, 685 (2008).
30) T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding, and J. O. Sofo, Phys. Rev. B **68**, 125210 (2003).
31) G. Pizzi, D. Volja, B. Kozinsky, M. Fornari, and N. Marzari, Comput. Phys. Commun. **185**, 422 (2014).
32) S. R. Gilbert, L. A. Wills, B. W. Wessels, J. L. Schindler, J. A. Thomas, and C. R. Kannewurf, J. Appl. Phys. **80**, 969 (1996).
33) M. Zhou, Z. M. Gibbs, H. Wang, Y. Han, C. Xin, L. Li, and G. J. Snyder, Phys. Chem. Chem. Phys. **16**, 20741 (2014).
34) T. H. Hsieh, H. Lin, J. Liu, W. Duan, A. Bansil, and L. Fu, Nat. Commun. **3**, 982 (2012).
35) P. Barone, D. D. Sante, and S. Picozzi, Phys. Status Solidi: Rapid Res. Lett. **7**, 1102 (2013).
36) D. Parker, X. Chen, and D. J. Singh, Phys. Rev. Lett. **110**, 146601 (2013).