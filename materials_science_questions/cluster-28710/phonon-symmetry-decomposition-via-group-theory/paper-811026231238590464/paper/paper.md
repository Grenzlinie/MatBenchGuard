Lattice dynamics properties of chalcopyrite ZnSnP₂: Density-functional calculations by using
a linear response theory

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2017 Chinese Phys. B 26 046302

(http://iopscience.iop.org/1674-1056/26/4/046302)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 137.207.120.173
This content was downloaded on 09/05/2017 at 07:25

Please note that terms and conditions apply.

You may also be interested in:

Ab initio vibrational and dielectric properties of CuGaS
Mustafa Akdogan and Resul Eryigit

First-principles studies of the electronic and dynamical properties of monosilicides MSi (M = Fe,
Ru, Os)
Y. N. Zhao, H. L. Han, Y. Yu et al.

Mechanical and Vibrational Properties of ZnS with Wurtzite Structure: A First-Principles Study
Yu You, Chen Chun-Lin, Zhao Guo-Dong et al.

Ab initio volume-dependent elastic and lattice dynamical properties of chalcopyriteCuAlSe2
Tanju Gürel and Resul Eryiit

Lattice dynamics and elastic properties of LiPN2 and NaPN2
A V Kosobutsky

Lattice Dynamics Study of Magnesium Chalcogenides
Zhang Xu-Dong, Li Zhi-Jie and Shi Gui-Mei

First-principles elastic and thermal properties of TiO2: a phonon approach
E Shojaee and M
R Mohammadizadeh
First-principles study of filled and unfilled antimony skutterudites
Philippe Ghosez and Marek Veithen

# Lattice dynamics properties of chalcopyrite ZnSnP₂: Density-functional calculations by using a linear response theory*

You Yu(虞游)¹,†, Yu-Jing Dong(董玉静)², Yan-Hong Shen(沈艳红)¹, Guo-Dong Zhao(赵国栋)¹, Xiao-Lin Zheng(郑小林)¹, and Jia-Nan Sheng(盛佳南)¹

¹College of Optoelectronic Technology, Chengdu University of Information Technology, Chengdu 610225, China
²School of Science and Technology, Xinyang University, Xinyang 464000, China

(Received 10 December 2016; revised manuscript received 20 January 2017; published online 20 February 2017)

We present a first-principles study of the structural, dielectric, and lattice dynamical properties for chalcopyrite semiconductor ZnSnP₂. The structural properties are calculated using a plane-wave pseudopotential method of density-functional theory. A linear response theory is used to derive Born effective charge tensors for each atom, dielectric constants in low and high frequency limits, and phonon frequencies. We calculate all zone-center phonon modes, identify Raman and infrared active modes, and report LO-TO splitting of the infrared modes. The results show an excellent agreement with experiment and propose several predictive behaviors.

**Keywords**: phonon, Born effective charge, dielectric permittivity, linear response theory

PACS: 63.20.dk, 63.20.–e, 63.20.D–
DOI: 10.1088/1674-1056/26/4/046302

## 1. Introduction

Ternary ABC₂ semiconducting crystals having chalcopyrite structure have been synthesized from I–III–VI₂ and II–IV–V₂ elements. They are derived from their binary analog zincblende II–VI and III–V semiconductors, respectively. ZnSnP₂ is a relatively little studied ternary chalcopyrite semiconductor material of the II–IV–V₂ family. Recently, ZnSnP₂ has received a great deal of attention as a photovoltaic material.¹¹¹ It is a promising candidate, given that its direct band gap of 1.68 eV¹²¹ yields a high theoretical photovoltaic conversion efficiency close to 30% in AM1.5G sunlight at the Shockley–Queisser limit.¹³¹ Undoped ZnSnP₂ typically shows p-type conductivity.¹⁴,⁵¹

Born effective charges, low frequency dielectric constants, and the phonon frequencies provide important information about the properties of the materials. The vibrational properties of ZnSnP₂ have been widely investigated for the past 40 years by a number of experimental and theoretical methods.¹⁶⁻¹⁰¹ Experimentally, the infrared (IR) reflectivity of ZnSnP₂ (at 295 K) was measured by Zlatkin *et al.*¹⁶¹ in 1969, and the corresponding optical constants and vibrational frequencies are determined. However, no Raman-active modes are given. Employing Raman (R) spectroscopy and an infrared spectrometer, Mintairov *et al.*¹⁷¹ measured the Raman scattering and infrared reflectivity, respectively. Both Raman-active and infrared-active modes are reported in Ref. [7]. Nevertheless, some modes have not been found in previous experiments.

Several earlier calculations have been performed to study the dynamical properties of ZnSnP₂ by using phenomenological models, such as rigid ion and Keating’s models. The phonon dispersion relations over the entire Brillouin zone of ZnSnP₂ were calculated using the rigid ion model by Mintairov *et al.*¹⁷¹ The zone-centered phonons of ZnSnP₂ have been studied using Keating’s models by Bettini.¹¹⁰¹ In addition, the phonon frequencies values have been calculated by transfer of the spectral pattern.¹⁹¹ The theoretical research mentioned above has a limitation, that is to say, the potentials in the calculations depend on experimental value. Identification of vibration modes in experimental measurements is sometimes incomplete, partly because of the complexity of the dispersion scheme in the chalcopyrite structure and partly because of experimental errors.

Nowadays the first-principles calculation has proved to be a powerful tool for the study of lattice dynamical properties. First-principles calculations of dynamical properties of ZnSnP₂ have been studied by Lazewski *et al.*¹⁸¹ The calculations were done by the direct method¹¹¹,¹²¹ from HF forces arising when a single atom is displaced from its equilibrium position. Generally, the first-principles investigation of phonon frequencies is mainly divided into two categories: the direct method and the linear-response method.¹¹³,¹⁴¹ The longitudinal–optical/transverse–optical (LO–TO) splitting of

---

*Project supported by the Open Research Fund of Computational Physics Key Laboratory of Sichuan Province, Yibin University (Grant No. JSWL2014KFZ01), the Scientific Research Fund of Sichuan Provincial Education Department, China (Grant No. 16ZB0209), the Scientific Research Foundation of Chengdu University of Information Technology, China (Grant No. J201611), and the National Natural Science Foundation of China (Grant No. 11547224).
†Corresponding author. E-mail: yy2012@cuit.edu.cn
© 2017 Chinese Physical Society and IOP Publishing Ltd
http://iopscience.iop.org/cpb http://cpb.iphy.ac.cn
046302-1

the infrared active modes based on effective charges and di- electric tensors are not directly given for the direct method. However, the two quantities can be calculated directly by a linear response method based on density functional perturba- tion theory (DFPT). $^{[15,16]}$ Although there are some studies of lattice dynamical properties for $ZnSnP_{2}$ , they are still an im portant part of a full understanding of the phonon in the mate- rial.

In this paper we present first-principles linear response theory to investigate the lattice dynamics properties, such as Born effective charge tensors for each atom, dielectric con- stants in low and high frequency limits, and phonon frequen- cies. This paper is organized as follows. In Section 2, we briefly review the underlying theoretical methods. In the fol- lowing sections, results are presented and discussed for geom- etry parameters (Subsection 3.1), Born effective charge tensor(Subsection 3.2), phonon frequencies (Subsection 3.3), and di- electric tensor (Subsection 3.4), respectively. Finally, conclu- sions are given in Section 4.

## 2. Computational method

Our calculations were performed with the ABINIT package, $^{[17]}$ which is based on density-functional theory(DFT) using the pseudopotential method and a plane-wave expansion of the wave functions. The interactions between the ions and valence electrons were described using norm- conserving local density approximation (LDA) pseudopoten- tials which are generated in the scheme of Troullier-Martins(TM). $^{[18-21]}$ For the exchange-correlation potential we have used the local density approximation data of Ceperly-Alder, as parametrized by Perdew and Wang. $^{[22]}$ The $Zn(3 d^{10}, 4 s^{2})$ , $Sn(5 s^{2}, 5 p^{2})$ , and $P(3 s^{2}, 3 p^{3})$ orbitals are treated as va lence states. The pseudopotentials used in the present cal- culations are soft potentials of the TM type, available on the ABINIT website. The density-functional perturbation theory is the basis of the linear-respond approach. Phonon frequen- cies and atoms displacements are obtained using the linear- respond method, which avoids the use of supercells and al- lows the calculation of dynamical matrix at arbitrary $q$ vectors. Technical details on the computation of responses to atoms displacements can be found in Refs. [23] and [24], while ref- erence [14] presents the subsequent computation of phonon frequencies, Born effective charge tensors for each atom, and dielectric constants.

The calculations were carried out with a 36-hartree plane- wave energy cutoff, and the tetragonal Brillouin zone (BZ) was sampled with a regular and shifted $4 \times 4 \times 4 k$ -point mesh. Convergence tests show that the BZ sampling and the kinetic energy cutoff are sufficient to insure an excellent convergence within $1 ~cm^{-1}$ for the calculated phonon frequencies.

## 3. Results and discussion
### 3.1. Structural optimization

The body-centered tetragonal chalcopyrite structure of ZnSnP2 is shown in Fig. 1. Each unit cell contains four for- mula units and the point group is $\overline{4} 2 m(D_{2 d})$ . The chalcopyrite structure is deduced from that of the zinc-blende by the re- placement of the cationic sublattice by two different atomic species. In general, II-V and IV-V bond lengths, denoted by $d_{II-V}$ and $d_{IV-V}$ , respectively, are not equal, which is men tioned in the substitution results in two different structural deformations: the first one is the relocation of anions in the $x-y$ plane which is characterized by parameter $u=0.25+$  $(d_{II-V}^{2}-d_{IV-V}^{2}) / a^{2}$ . Here, $a$ is the lattice constant in the $x$  or $y$ direction. The second consequence of differing anion cation bond lengths is a deformation of the unit cell along the $z$ direction to a length $c$ , which is generally different from $2 a$ . This tetragonal distortion is characterized by the quantity $c / a$ . For real compounds of pnictide II-IV- $V_{2}$ groups in most cases $c / a=1.769-2.016$ and $u=0.214-0.304.^{[25]}$ The unit vectors of the primitive cell are $(a, 0,0),(0, a, 0),(a / 2, a / 2, c / 2)$ . The cations are located at $4 a$ and $4 b$ while anions are located at $8 d$ Wyckoff positions. Ion positions can be generated using the following minimum set of $(x, y, z)$ coordinates expressed in units of the $a$ and $c$ constants.

Group II: $(0,0,0),(0,1 / 2,1 / 4)$ ;
Group IV: $(0,0,1 / 2),(0,1 / 2,3 / 4)$ ;
Group V: $(u, 1 / 4,1 / 8),(-u, 3 / 4,1 / 8),(3 / 4, u, 7 / 8),(1 / 4$ , -u,7/8).

![](./images/811026231238590464_1.jpg)

Fig. 1. (color online) Crystal structure of $ZnSnP_{2}$ (chalcopyrite-type; body-centered tetragonal- $\overline{4} 2 d$ ).

The ground state structural properties are obtained by minimization of the total energy with respect to the unit cell volume. The structural parameters are obtained by optimizing lattice constants and atomic coordinates un- til all force components are below $5 \times 10^{-5}$ hartree/Bohr(1 hartree $=27.2114 eV$ ). Table 1 summarizes our results ob tained after relaxation of the lattice constants, as well as the available calculated $^{[8,26,27]}$ and experimental values. $^{[5,28]}$ For ZnSnP2, optimization of unit cell geometry within LDA leads to $a=5.622 \AA, c=11.233 \AA$ . The calculated lattice constants are underestimated with the maximal error of $0.7 \%$ , which is

typically the expected precision for the LDA. Even compari- son with experimental values at the lowest temperatures avail- able is, strictly speaking, not correct, since it neglects the an- harmonic effect of the zero-point vibrations. Even so, the cal- culated lattice parameters are found to be in good agreement with the experimental ones. The optimized results show our calculation method is feasible and we will adopt the optimized structure parameters to calculate other properties.

Table 1. The equilibrium lattice constant $a$ ($c$) (in unit $\mathring{A}$), axial ratio $c/a$ and internal parameter for ZnSnP₂.

| Method                     | $a$    | $c$    | $c/a$  | $u$    |
|----------------------------|--------|--------|--------|--------|
| ABINIT-LDA (Present work ) | 5.622  | 11.233 | 1.998  | 0.231  |
| VASP-LDA (Ref. [8])        | 5.606  | 11.089 | 1.978  | 0.227  |
| VASP-GGA+U (Ref. [26])     | 5.706  | 11.443 | 2.005  | 0.228  |
| VASP-HSE06 (Ref. [26])     | 5.671  | 11.352 | 2.002  | 0.232  |
| CASTEP-LDA (Ref. [27])     | 5.638  | 11.228 | 1.991  | 0.25   |
| Exp. (Ref. [5])            | 5.651  | 11.302 | 2.000  | 0.239  |
| Exp. (Ref. [28])           | 5.652  | 11.305 | 2.000  | 0.229  |

### 3.2. Born effective charge tensors

The Born effective charge tensor quantifies the macro- scopic electric response of a crystal to the internal displace- ments of its atoms. They are important quantities in obtaining the LO-TO phonon splitting, also they provide some informa- tion about the ionicity of the material. For atom $\kappa$, the Born effective charge tensor $Z_{\kappa,\beta\alpha}^{*}$ is defined as the proportionality coefficient relating, at linear order, the polarization per unit cell, created along the direction $\beta$, and the displacement along the direction $\alpha$ of the atoms belonging to the sublattice $\kappa$, under the condition of a zero electric field. $^{[14]}$ In this work, the Born effective charge tensors $Z_{\kappa,\beta\alpha}^{*}$ for each atom of ZnSnP₂ are calculated by DFPT.

Values of the calculated Born effective charge of ZnSnP₂ are presented in Table 2. To the best of our knowledge, no other first-principles calculations of the Born effective charge for ZnSnP₂ exist. The form of $Z_{\kappa,\beta\alpha}^{*}$ for atom $\kappa$ depends on the site symmetry of the ions. The point symmetries at the site of Zn ion and Sn ion are $S_4$ ($4a$ sites) and $S_4$ ($4b$ sites), re- spectively. For P ion, the point symmetry at the site is $C_2$ ($8d$ sites). The effective charge tensors for cations are diagonal and obey $Z_{xx}^{*}=Z_{yy}^{*}\neq Z_{zz}^{*}$, as required by symmetry for a tetragonal crystal. According to the calculation results, cations have diagonal Born effective charges with $Z_{\text{Zn},xx}^{*}=Z_{\text{Zn},yy}^{*}=1.76$, $Z_{\text{Zn},zz}^{*}=1.73$, and $Z_{\text{Sn},xx}^{*}=Z_{\text{Sn},yy}^{*}=2.50$, $Z_{\text{Sn},zz}^{*}=2.64$. $Z^{*}$ of cations are almost diagonal with an anisotropy of $2\%$ for Zn and $5\%$ for Sn, respectively. The effective charge tensors have nearly spherical symmetry, with small tetragonal distor- tion caused by $c/2a\neq1$. P ions, located at lower symmetry sites, have nondiagonal and anisotropic $Z^{*}$. For all anions, $Z_{\text{P},zz}^{*}=-2.18$ while $Z_{\text{P},xx}^{*}$ and $Z_{\text{P},yy}^{*}$ take the value $-1.99$ or $-2.27$ depending on the distortion of $u$. Also, depending on the $u$ distortion being along the $x$ or $y$ direction, the nondiago- nal components $Z_{\text{P},zx}^{*}=\pm0.02$, $Z_{\text{P},xz}^{*}=\pm0.13$ or $Z_{\text{P},yz}^{*}=\pm0.13$, $Z_{\text{As},zy}^{*}=\pm0.02$ are different than zero. We can see that the shape of $Z^{*}$ for P ions is far from a sphere. This behav- ior has also been observed in the case of other chalcopyrite semiconductors. $^{[29-32]}$

The average eigenvalues for cations and anions are com- parable to the values in Ref. [10]. The calculated average eigenvalues $(Z^{*}(\bar{\lambda}))$ in our work for Zn, Sn, and P are 1.75, 2.55, and $-2.15$, respectively. Obviously, the three atoms have smaller effective charges than their formal charges, $+2$, $+4$, and $-3$ for Zn, Sn, and P, respectively. Such difference can be derived from the strong covalent characteristic for bonds. To the best of our knowledge, no other first-principle calculations and experimental data of $Z^{*}$ for ZnSnP₂ exist. We have com- pared our results with other literature data calculated with a different force-field model. $^{[10]}$ This discrepancy is pronounced for the effective charges in Ref. [10] obtained by a least square fit of the phonon energies and Coulomb splittings, probably because of the use of approximate eigenvectors and assump- tions about the dynamical charges. Earlier results by Akdogan $et$ $al.^{[31]}$ gave Born effective charges of CuGaS₂ with the same linear response as ours, and average of eigenvalues $Z^{*}(\bar{\lambda})$ dis- played a good agreement with experimental data.

Table 2. Calculated Born effective charge tensors, $Z^{*}$, eigenvalues of the symmetric part of $Z^{*}(\lambda)$, average of eigenvalues $Z^{*}(\bar{\lambda})$, and force-field model effective charges of Ref. [10].

| Atom   | $Z^{*}$                                                                 | $Z^{*}(\lambda)$               | $Z^{*}(\bar{\lambda})$ | Point charge of Ref. [10] |
|--------|-------------------------------------------------------------------------|--------------------------------|------------------------|---------------------------|
| $Z_{\text{Zn}}^{*}$ | $\begin{pmatrix}1.76 & 0.13 & 0.00 \ -0.13 & 1.76 & 0.00 \ 0.00 & 0.00 & 1.73\end{pmatrix}$ | $\begin{bmatrix}1.76 \ 1.76 \ 1.73\end{bmatrix}$ | 1.75                   | 0.9                       |
| $Z_{\text{Sn}}^{*}$ | $\begin{pmatrix}2.50 & -0.31 & 0.00 \ 0.31 & 2.50 & 0.00 \ 0.00 & 0.00 & 2.64\end{pmatrix}$ | $\begin{bmatrix}2.64 \ 2.50 \ 2.50\end{bmatrix}$ | 2.55                   | 0.4                       |
| $Z_{\text{P}_1}^{*}$ | $\begin{pmatrix}-1.99 & 0.00 & 0.00 \ 0.00 & -2.27 & 0.13 \ 0.00 & 0.02 & -2.18\end{pmatrix}$ | $\begin{bmatrix}-2.29 \ -2.16 \ -1.99\end{bmatrix}$ | $-2.15$                | $-0.65$                   |
| $Z_{\text{P}_2}^{*}$ | $\begin{pmatrix}-2.27 & 0.00 & 0.13 \ 0.00 & -1.99 & 0.00 \ 0.02 & 0.00 & -2.18\end{pmatrix}$ | $\begin{bmatrix}-2.29 \ -2.16 \ -1.99\end{bmatrix}$ | $-2.15$                | $-0.65$                   |

### 3.3. Phonons

The crystal symmetry of ZnSnP₂ is body-centered tetrag- onal with a centro-symmetric space group $I\overline{4}2d$ and a corre- sponding $\overline{4}2m$ point group. Positions of nonequivalent atoms are indicated in Fig. 2. There are four distinct P, two Zn, and two Si atoms. Transformation properties of these atoms under symmetry operations of the space group are noted in Table 3. As a tetragonal crystal, ZnSnP₂ has phonon dispersion rela- tions consisting of 24 branches whose group theoretical anal- ysis at the BZ center $(\Gamma)$ yields a decomposition into

$$
\Gamma=1A_1+2A_2+3B_1+4B_2+7E, \tag{1}
$$

where $E$ is a double degenerate mode. The acoustic modes correspond to one $B_2$ and one $E$ mode. For optical modes, the irreducible representation is

$$
\Gamma_{\mathrm{opt}}=1 A_{1}+2 A_{2}+3 B_{1}+3 B_{2}+6 E. \tag{2}
$$

The $A_1$ and $B_1$ modes are Raman-active, $B_2$ and $E$ modes are both Raman- and IR-active, and the $A_2$ mode is silent. These IR modes are polar modes and subject to an LO-TO splitting. Symmetry coordinates for the onefold $A$ and $B$ representations are given in Figs. 2 and 3, respectively, and for the twofold $E$ representations in Fig. 4. A detailed discussion can be found in Ref. [33].

Table 3. Character table for the $D_{2d}$ point group (tetragonal).

<table>
  <thead>
    <tr>
      <th>$D_{2d}(\bar{4}2m)$</th>
      <th>$E$</th>
      <th>$2S_4$</th>
      <th>$C_2$</th>
      <th>$2C_2'$</th>
      <th>$2\sigma_d$</th>
      <th>Symmetry</th>
      <th>Activity</th>
      <th colspan="2">Number</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>Optical</th>
      <th>Acoustic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$A_1$</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>$x^2+y^2,z^2$</td>
      <td>R</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$A_2$</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>$-1$</td>
      <td>$-1$</td>
      <td>$-$</td>
      <td>silent</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$B_1$</td>
      <td>1</td>
      <td>$-1$</td>
      <td>1</td>
      <td>1</td>
      <td>$-1$</td>
      <td>$x^2-y^2$</td>
      <td>R</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$B_2$</td>
      <td>1</td>
      <td>$-1$</td>
      <td>1</td>
      <td>$-1$</td>
      <td>1</td>
      <td>$xy$</td>
      <td>R, IR</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>$E$</td>
      <td>2</td>
      <td>0</td>
      <td>$-2$</td>
      <td>0</td>
      <td>0</td>
      <td>$(x,y),(xz,yz)$</td>
      <td>R, IR</td>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

![](./images/811026231238590464_2.jpg)

Fig. 2. (color online) (001) projection of unit cell showing positions of four nonequivalent P atoms, the two nonequivalent Zn atoms and the two nonequivalent Sn atoms. Symmetry coordinates for $A$ modes $(1A_1+2A_2)$; displacements in the $xy$ plane are represented by arrows and displacements in the $z$ direction by open and closed circles.

![](./images/811026231238590464_3.jpg)

Fig. 3. (color online) Symmetry coordinates for $B$ modes $(3B_1+4B_2)$; displacements in the $xy$ plane are represented by arrows and displacements in the $z$ direction by open and closed circles.

Complete phonon branches of $ZnSnP_2$ are plotted for the high-symmetry lines in the BZ together with the corresponding phonon density of states (DOS) in Fig. 5. An interesting feature of acoustic branches around the $\Gamma$ point is observed, especially along $\Gamma-X$ and $\Gamma-Z$ directions. In order to obtain the phonon dispersion curves throughout the BZ, the dynamical matrices are obtained $4×4×4$ grid of $q$ points, and real space force constants are then found by Fourier transform of the dynamical matrices. The acoustic sum rule is applied to force the three acoustic phonon frequencies at the $\Gamma$ point equal to zero strictly as being implied by translation symmetry.

![](./images/811026231238590464_4.jpg)

Fig. 4. (color online) Symmetry coordinates for $E$ modes $(7E)$; displacements in the $xy$ plane are represented by arrows and displacements in the $z$ direction by open and closed circles.

In Table 4, we compare calculated phonon frequencies of $ZnSnP_2$ at the $\Gamma$ point with the measured Raman$^{[7]}$ and infrared$^{[6,7]}$ values. For comparison, we cite also the phonon frequencies from theoretical calculations through direct methods$^{[8]}$ and a classical model.$^{[7,9,10]}$ As shown in Fig. 5 and Table 4, three groups of modes can be identified. A clear gap exists between the twelve upper energy branches and the remaining twelve branches. The low frequency group of modes has a range of values from $82\ \mathrm{cm}^{-1}$ to $115\ \mathrm{cm}^{-1}$ and the medium frequency group of modes has a range of values from $180\ \mathrm{cm}^{-1}$ to $207\ \mathrm{cm}^{-1}$. The highest frequency group of modes can be up to $370\ \mathrm{cm}^{-1}$. Unfortunately, some vibration modes have not been observed in previous experiments, including infrared and Raman measurements. To get more accurate measurements, inelastic neutron scattering experiments should be adopted, but it is not available in previous works. Otherwise, for some of the modes there are large differences among the reported theoretical frequencies, for example the highest frequency $B_2$ mode ranges from $350\ \mathrm{cm}^{-1}$ to $375\ \mathrm{cm}^{-1}$. Our calculation shows that the mode is at $365\ \mathrm{cm}^{-1}$, which is in very good agreement with experiments.$^{[6,7]}$ It makes us very confident in the prediction of the frequencies for the others.

![](./images/811026231238590464_5.jpg)

Fig. 5. Calculated phonon dispersion curves along symmetry lines in the Brillouin zone and the corresponding phonon density of states (DOS) for ZnSnP₂.

It should be noted that the direct method was performed to calculate the phonon frequencies of ZnSnP₂ by Lazewski et al. $^{[8]}$ Although the calculated frequencies show a better agreement with ours, the LO-TO splittings are not discussed. This is because the splitting depends on the effective charges and dielectric tensors of the system, which are not directly acces- sible to the direct method. The IR modes group into modes with displacements either in the x, y plane or along the z di- rection. The $E$ mode has a displacement pattern in the x, y plane, and the $B_{2}$ mode has displacements along the z direc tion. The LO-TO splittings for $B_{2}$ and $E$ modes are presented in Table 4 and the values of LO-TO splitting agree well the experimental results. $^{[6,7]}$ The missing modes in the experiment are predicted successfully. For ZnSnP₂, the LO-TO splitting is small, ranging from $0\ \text{cm}^{-1}$ to $10\ \text{cm}^{-1}$. The splitting is even zero in the low frequency region, because the low fre- quency modes are essentially the folded acoustic modes, they correspond to whole molecular units moving relative to each other. The largest difference appears on the $E$ mode with the highest frequency. The large LO-TO splittings of these modes suggest they involve large effective charges and make large contributions to the static dielectric tensor of ZnSnP₂. A sim- ilar splitting case occurs for CuGaSe₂ and the results can be found in Ref. [29].

<table><caption>Table 4. A comparison of calculated phonon frequencies (in unit $\text{cm}^{-1}$) at the $\Gamma$ point with Raman and infrared data as well as with other theory values. Two numbers in a row correspond to LO/TO frequencies.</caption>
  <thead>
    <tr>
      <th colspan="2">Mode</th>
      <th>Theory/present</th>
      <th colspan="3">Experiment</th>
      <th colspan="4">Theory</th>
    </tr>
    <tr>
      <th colspan="2"></th>
      <th></th>
      <th>IR$^{[6]}$</th>
      <th>IR$^{[7]}$</th>
      <th>R$^{[7]}$</th>
      <th>$Ab\ initio^{[8]}$</th>
      <th>Estimated$^{[9]}$</th>
      <th>Keating's model$^{[10]}$</th>
      <th>Rigid ion model$^{[7]}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$A_{1}$</td>
      <td>R</td>
      <td>313</td>
      <td></td>
      <td></td>
      <td>309</td>
      <td>298</td>
      <td>309</td>
      <td>304</td>
      <td>307</td>
    </tr>
    <tr>
      <td>$A_{2}$</td>
      <td>silent</td>
      <td>311</td>
      <td></td>
      <td></td>
      <td>295</td>
      <td>308</td>
      <td></td>
      <td></td>
      <td>292</td>
    </tr>
    <tr>
      <td></td>
      <td>silent</td>
      <td>345</td>
      <td></td>
      <td></td>
      <td>333</td>
      <td>332</td>
      <td></td>
      <td></td>
      <td>331</td>
    </tr>
    <tr>
      <td>$B_{1}$</td>
      <td>R</td>
      <td>105</td>
      <td></td>
      <td></td>
      <td></td>
      <td>106</td>
      <td>106</td>
      <td>138</td>
      <td>124</td>
    </tr>
    <tr>
      <td></td>
      <td>R</td>
      <td>207</td>
      <td></td>
      <td></td>
      <td></td>
      <td>205</td>
      <td>191</td>
      <td>214</td>
      <td>208</td>
    </tr>
    <tr>
      <td></td>
      <td>R</td>
      <td>362</td>
      <td></td>
      <td></td>
      <td>353</td>
      <td>358</td>
      <td>333</td>
      <td>346</td>
      <td>352</td>
    </tr>
    <tr>
      <td>$B_{2}$</td>
      <td>R, IR</td>
      <td>101/100</td>
      <td></td>
      <td></td>
      <td></td>
      <td>105/101</td>
      <td>98</td>
      <td>149/148</td>
      <td>140/139</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>330/328</td>
      <td>-/327</td>
      <td></td>
      <td>347/-</td>
      <td>353/321</td>
      <td>331</td>
      <td>345/335</td>
      <td>329/324</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>365/364</td>
      <td>-/368</td>
      <td></td>
      <td>365/-</td>
      <td>360/359</td>
      <td>350</td>
      <td>375/354</td>
      <td>372/348</td>
    </tr>
    <tr>
      <td>$E$</td>
      <td>R, IR</td>
      <td>82/82</td>
      <td></td>
      <td></td>
      <td></td>
      <td>77/77</td>
      <td>85</td>
      <td>125/125</td>
      <td>115/115</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>115/115</td>
      <td></td>
      <td></td>
      <td></td>
      <td>119/116</td>
      <td>108</td>
      <td>165/164</td>
      <td>154/153</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>180/180</td>
      <td></td>
      <td></td>
      <td></td>
      <td>182/179</td>
      <td>157</td>
      <td>188/187</td>
      <td>190/189</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>328/325</td>
      <td></td>
      <td>318/313</td>
      <td>317/-</td>
      <td>325/321</td>
      <td>318</td>
      <td>312/311</td>
      <td>317/315</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>340/335</td>
      <td>-/327</td>
      <td>339/328</td>
      <td>328/-</td>
      <td>331/327</td>
      <td>321</td>
      <td>329/328</td>
      <td>334/333</td>
    </tr>
    <tr>
      <td></td>
      <td>R, IR</td>
      <td>353/343</td>
      <td>-/368</td>
      <td>360/342</td>
      <td>342/-</td>
      <td>354/331</td>
      <td>337</td>
      <td>375/345</td>
      <td>378/350</td>
    </tr>
  </tbody>
</table>

### 3.4. Lattice dielectric properties

The dielectric tensor for a tetragonal system such as this will be diagonal with two distinct elements. For ZnSnP₂, the calculated electronic $(\varepsilon_{\infty})$ and static $(\varepsilon_{0})$ dielectric tensors are diagonal and have two independent components $\varepsilon^{\perp}$ and $\varepsilon^{\parallel}$ perpendicular to and along the c axis, respectively. In Ta- ble 5 we compare the values calculated for the dielectric ten- sor of ZnSnP₂ with theoretical and experimental data avail- able. The electronic dielectric constants are calculated to be $\varepsilon_{\infty}^{\perp} = \varepsilon_{\infty}^{xx} = \varepsilon_{\infty}^{yy} = 11.91$ and $\varepsilon_{\infty}^{\parallel} = \varepsilon_{\infty}^{zz} = 12.01$. The static di- electric tensor can be decomposed into contributions of differ- ent modes and calculated by the generalized Lyddane-Sachs- Teller (LST) relation: $^{[34]}$

$$
\varepsilon_{0}=\varepsilon_{\infty} \prod_{m} \frac{\omega_{\mathrm{LO}, m}^{2}}{\omega_{\mathrm{TO}, m}^{2}}, \qquad(3)
$$

where the frequencies $\omega_{\mathrm{LO}, m}$ and $\omega_{\mathrm{TO}, m}$ are the long wave- length limits for longitudinal and transverse vibrations, re- spectively. According to the LST relation, the static dielec- tric constants of $\varepsilon_{0}$ both directions are $\varepsilon_{0}^{\perp} = \varepsilon_{0}^{xx} = \varepsilon_{0}^{yy} = 13.74$ and $\varepsilon_{0}^{\parallel} = \varepsilon_{0}^{zz} = 13.86$, respectively, showing a nearly isotropic character. The averages of $\varepsilon_{\infty}$ and $\varepsilon_{0}$, obtained from the ex- pression $\varepsilon_{\infty}\ (\text{or}\ \varepsilon_{0})=(2\varepsilon_{\infty}^{\perp}+\varepsilon_{\infty}^{\parallel})/3$ are also shown in Ta- ble 5. The components of $\varepsilon_{0}$ are much larger than those of $\varepsilon_{\infty}$ as a consequence of the significant contribution to the low-

frequency dielectric permittivity tensor due to ionic displacements.

Table 5. Static and high frequency dielectric tensor components of ZnSnP₂.

|                | $\varepsilon_{\infty}^{\parallel}$ | $\varepsilon_{\infty}^{\perp}$ | $\varepsilon_{\infty}$ | $\varepsilon_{0}^{\parallel}$ | $\varepsilon_{0}^{\perp}$ | $\varepsilon_{0}$ |
|----------------|------------------------------------|--------------------------------|------------------------|-------------------------------|---------------------------|-------------------|
| This work      | 12.01                              | 11.91                          | 11.94                  | 13.86                         | 13.74                     | 13.78             |
| Exp. (Ref. [6])|                                    |                                | 8.1±0.2                |                               |                           | 10.0±0.4          |
| Calc. (Ref. [35])|                                   |                                |                        |                               |                           | 9.90              |
| Calc. (Ref. [36])|                                   |                                |                        | 12.68                         | 12.75                     | 12.73             |
| Calc. (Ref. [27])|                                   |                                |                        |                               |                           | 10.08             |

The dielectric properties of ZnSnP₂ have not been studied very much experimentally. We are only aware of the measurement of the dielectric constant of ZnSnP₂ in which a value of $\varepsilon_{\infty} \approx 8.1$ (or $\varepsilon_{0} \approx 10.0$) has been reported in Ref. [6]. On the theoretical side, the dielectric constant has been calculated by Verma *et al.*$^{[34]}$ using a plasma oscillations theory. $\varepsilon_{0}$ from Ref. [35] is 9.90 and seems to be more consistent with the experimental value 10.0. Our calculated values and previous theoretical values$^{[27,36]}$ are calculated by using the DFT and larger than the experimental results. The overestimation of the calculation is a well-known fact of the DFT due to the underderestimation of the band gap.$^{[34,37,38]}$ We note that a smaller energy gap $E_{\text{g}}$ yields a larger $\varepsilon_{0}$ value. This can be explained on the basis of the Penn model.$^{[39]}$ The Penn model is based on the expression $\varepsilon_{0} \approx 1 + (\hbar \omega_{\text{p}}/E_{\text{g}})^{2}$. It is clear that $\varepsilon_{0}$ is inversely proportional to $E_{\text{g}}$. The dielectric constants calculated in our work deviate from other theoretical data$^{[27,35]}$ because a small band gap was adopted in the calculation.

## 4. Conclusions

To summarize, we have presented first-principles calculations of the structural, dielectric, and, in particular, of the lattice dynamical properties of the chalcopyrite semiconductor ZnSnP₂within the density-functional theory and pseudopotential methods. The optimal ground state structure is studied within the LDA approaches. The relaxed lattice constants are found to be in good agreement with the experimental ones with the maximal error of 0.7%. Born effective charge and dielectric constants are calculated within the linear response theory. The calculated average eigenvalues $Z^{*}(\bar{\lambda})$ for Zn, Sn, and P are 1.75, 2.55, and $-2.15$, respectively. They are smaller than their formal charges because of the strong covalent characteristic for bonds. Our theoretical values of dielectric constants tend to be overestimated in LDA calculations due to the underestimation of the band gap. The phonon frequencies at the $\Gamma$ point of the BZ are calculated and their assignments are given.

The LO–TO splittings for $B_2$ and $E$ modes are presented and the values of LO–TO splitting agree well the infrared and Raman measurements. We believe that our theoretical predictions should be highly valuable for the experimental community in the framework of the characterization of ZnSnP₂.

## References

[1] Folmer J C W, Tuttle J R, Tu J A and Parkinson B A 1985 *J. Electrochem. Soc.* **132** 1608

[2] St-Jean P, Seryogin G A and Francoeur S 2010 *Appl. Phys. Lett.* **96** 231913

[3] Shockley W and Queisser H J 1961 *J. Appl. Phys.* **32** 510

[4] Rubenstein M and Ure R W 1968 *J. Phys. Chem. Solids* **29** 551

[5] Vaipolin A A, Goryunova N A, Kleshchinskii L I, Loshakova G V and Osmanov E O 1968 *Phys. Status Solidi B* **29** 435

[6] Zlatkin L B, Markov Yu F, Stekhanov A I and Shur M S 1969 *Phys. Stat. Solidi* **32** 473

[7] Mintairov A M, Sadchikov N A, Sauncy T and Holtz M 1999 *Phys. Rev. B* **59** 15197

[8] Lazewski J and Parlinski K 2001 *J. Alloys Compd.* **328** 162

[9] Ohrendorf F W and Haeuseler H 1999 *Cryst. Res. Technol.* **34** 339

[10] Bettini M 1975 *Phys. Stat. Solidi* **69** 201

[11] Parlinski K, Li Z Q and Kawazoe Y 1997 *Phys. Rev. Lett.* **78** 4063

[12] Kunc K and Martin R M 1982 *Phys. Rev. Lett.* **48** 406

[13] Giannozzi P, Gironcoli S de, Pavone P and Baroni S 1991 *Phys. Rev. B* **43** 7231

[14] Gonze X and Lee C 1997 *Phys. Rev. B* **55** 10355

[15] Baroni S, Giannozzi P and Testa A 1987 *Phys. Rev. Lett.* **58** 1861

[16] Baroni S, Gironcoli S de, Dal Corso A and Giannozzi P 2001 *Rev. Mod. Phys.* **73** 515

[17] Gonze X, Beuken J M, Caracas R, Detraux F, Fuchs M, Rignanese G -M, Sindic L, Verstraete M, Zerah G, Jollet F, Torrent M, Roy A, Mikami M, Ghosez Ph, Raty J Y and Allan D C 2002 *Comput. Mater. Sci.* **25** 478

[18] Goedecker S 1997 *SIAM J. Sci. Comput.* **18** 1605

[19] Payne M C, Teter M P, Allan D C, Arias T A and Joannopoulos J D 1992 *Rev. Mod. Phys.* **64** 1045

[20] Gonze X 1996 *Phys. Rev. B* **54** 4383

[21] Fuchs M, and Scheffler M 1999 *Comput. Phys. Commun.* **119** 67

[22] Perdew J P and Wang Y 1992 *Phys. Rev. B* **45** 13244

[23] Gonze X 1997 *Phys. Rev. B* **55** 10337

[24] Hamann D R, Wu X, Rabe K M and Vanderbilt D 2005 *Phys. Rev. B* **71** 035117

[25] Jaffe J E and Zunger A 1984 *Phys. Rev. B* **29** 1882

[26] Hinuma Y, Oba F, Nose Y and Tanaka I 2013 *J. Appl. Phys.* **114** 043718

[27] Sahin S, Cifici Y O, Colakoglu K and Korozlu N 2012 *J. Alloys Compd.* **529** 1

[28] Shaposhnikov V L, Krivosheeva A V and Borisenko V E 2012 *Phys. Rev. B* **85** 205201

[29] Parlak C and Eryigit R 2006 *Phys. Rev. B* **73** 245217

[30] Lazewski J, Jochym P T and Parlinski K 2002 *J. Chem. Phys.* **117** 2726

[31] Akdogan M and Eryigit R 2002 *J. Phys.: Condens. Matter* **14** 7493

[32] Yu Y, Zhao B J, Zhu S F, Gao T and Hou H J 2011 *Solid State Sci.* **13** 422

[33] Kaminow I P, Buehler E and Wernick J H 1970 *Phys. Rev. B* **2** 960

[34] Martin R M and Ortiz G 1997 *Phys. Rev. B* **56** 1124

[35] Verma A S and Bhardwaj S R 2006 *Phys. Stat. Solidi* **243** 2858

[36] Chiker F, Abbar B, Bresson S, Khelifa B, Mathieu C and Tadjer A 2004 *J. Solid State Chem.* **177** 3859

[37] Gonze X, Ghosez Ph and Godby R W 1995 *Phys. Rev. Lett.* **74** 4035

[38] Ghosez Ph, Michenaud J P and Gonze X 1998 *Phys. Rev. B* **58** 6224

[39] Penn D R 1962 *Phys. Rev.* **128** 2093