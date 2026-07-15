PHYSICAL REVIEW B 91, 205433 (2015)

# Phonon properties, thermal expansion, and thermomechanics of silicene and germanene

Liang-Feng Huang, $^{1,2}$ Peng-Lai Gong, $^{1}$ and Zhi Zeng $^{1,3,*}$

$^{1}$ Key Laboratory of Materials Physics, Institute of Solid State Physics, Chinese Academy of Sciences, Hefei 230031, China
$^{2}$ Department of Materials Science and Engineering, Northwestern University, Evanston, Illinois 60208, USA
$^{3}$ University of Science and Technology of China, Hefei 230026, China

(Received 24 February 2015; revised manuscript received 1 May 2015; published 26 May 2015)

We report a hierarchical first-principles investigation on the entangled effects of lattice dimensionality and bond characteristics in the lattice dynamics of silicene and germanene. It is found that bond bending (stretching) negatively (positively) contributes to Grüneisen constant $\gamma$, which results in the negative acoustic (positive optical) $\gamma$. The layer thickening (bond weakening) caused by chemical functionalization tends to increase (decrease) the acoustic (optical) $\gamma$, due to the increased (decreased) bond-stretching effect. The excitation of the negative-$\gamma$ modes results in negative thermal expansion, while mode excitation and thermal expansion compete with each other in thermomechanics. The sensitive structural and electronic responses of silicene and germanene to functionalization help us to derive a generic physical picture for two-dimensional lattice dynamics.

DOI: 10.1103/PhysRevB.91.205433
PACS number(s): 68.35.bg, 63.22.-m, 65.40.De

## I. INTRODUCTION

Two-dimensional silicon and germanium (silicene and germanene) [1] have attracted great interest after the advent of graphene [2]. The low dimensionality of graphene [3] renders its charge density, electronic states, and various physical and chemical properties readily controllable [3-6], which is highly helpful for advanced materials and devices. Apart from having these low-dimensional benefits, silicene (Si) and germanene (Ge) are also expected to be easily incorporated into existing silicon-based industry [7,8].

Si and Ge have buckled hexagonal lattices [9,10], where quantum Hall effects, valley polarization, tunable band gap, and fast intrinsic mobility have been discovered [11-17]. This indicates their promising applications in electronics, optics, and fundamental-physics research. Si has been synthesized on various substrates (Ag [18-20], Ir [21], and $ZrB_2$ [22]), while Ge is still under exploration. Monolayer Si transistors operating at room temperature have been fabricated recently [23]. Si and Ge can be easily functionalized in various environments. Chemical functionalizations (e.g., hydrogenation) can controllably open a band gap in Si and Ge by changing the orbital hybridization [24-29], and hydrogenated germanene (HGe) with a band gap of 1.53 eV has been synthesized [30]. The supporting substrates also have similar functionalization effects on Si and Ge [31-35]. These fast synthesis and fabrication progresses lead to an urgent demand for the knowledge of the thermal expansion and thermomechanics of pristine/functionalized Si and Ge, because the accumulated thermal strain and stress may influence the performance and lifetime of devices working at finite temperatures.

In this paper the phonon spectra, Grüneisen constants, thermal expansion, and temperature-dependent stiffness of Si and Ge are investigated by first-principles simulation. The roles of low dimensionality, layer thickness, and bond strength are disentangled by analyzing the effects of chemical functionalization. The revealed physical picture is useful for understanding the lattice dynamics of various two-dimensional systems.

## II. METHODOLOGY

The electronic structure and phonon spectra are calculated using density functional theory and density functional perturbation theory, respectively, which are implemented in the Quantum Espresso code [36,37]. The ultrasoft [38] PBE functional [39] is used to describe the electronic exchange and correlation. The cutoff energy for wave function (charge density) is 80 (800) Ry. Monkhorst-Pack [40] reciprocal grids of $24 \times 24 \times 1$, $12 \times 12 \times 1$, $30 \times 30 \times 1$, and $300 \times 300 \times 1$ are used for the calculations of electronic structure, lattice dynamical matrices, thermodynamic properties, and phonon density of states, respectively. The dense reciprocal grid for electronic structure $(24 \times 24 \times 1)$ is required to accurately calculate the phonon anharmonicity of Ge and HGe, which have low dynamical stability. The convergence thresholds for electronic energy and phonon perturbation potential also need to be as low as $10^{-12}$ and $10^{-8}$ Ry [42]. The interlayer distance is $16$ Å. Ubiquitous intrinsic ripples of $\gtrsim 30$ Å have been observed in various two-dimensional systems [41,42], which destroy the long-wavelength vibrations. Thus, the phonon modes with wavelength $>30$ Å are neglected in the thermodynamic simulation.

The temperature dependent lattice constant ($a$) is calculated using the self-consistent quasiharmonic approximation (SC-QHA) method [41]

$$
a(T)=\left(\frac{d E^{e}(a)}{d a}\right)^{-1} \frac{1}{N_{k}} \sum_{k, \lambda} U_{k, \lambda}(T) \gamma_{k, \lambda}, \tag{1}
$$

where $k$ and $\lambda$ are the wave vector and branch indices for a phonon mode; $N_k$ is the $k$-point number; and $E^{e}$, $U_{k,\lambda}$, and $\gamma_{k,\lambda}$ are the total electronic energy, the internal energy, and Grüneisen constant $\left(\gamma=-\frac{a}{\omega} \frac{d \omega}{d a}\right)$ of a phonon mode, respectively. To guarantee that $\gamma$ is calculated between two modes with the same symmetry, the phononic $k\cdot p$ theory [42] is used to sort the phonon branches. Equation (1) is self-consistently solved, and the phonon frequencies are updated after each

*zzeng@theory.issp.ac.cn

1098-0121/2015/91(20)/205433(6)
205433-1
©2015 American Physical Society

iteration step $(\Delta \omega \doteq -\gamma \frac{\Delta a}{a}\omega)$. The thermal-expansion coefficient $(\alpha = \frac{1}{a}\frac{da}{dT})$ can be re-expressed as [41]

$$
\begin{aligned}
\alpha(T) & =\frac{1}{\sum_{i=1}^{3} s_{i}} \frac{1}{N_{k}} \sum_{k, \lambda} C_{V}^{k, \lambda}(T) \gamma_{k, \lambda} \\
& \approx \frac{2 \sqrt{3} a^{2}}{B_{2 \mathrm{D}} N_{k}} \sum_{k, \lambda} C_{V}^{k, \lambda}(T) \gamma_{k, \lambda},
\end{aligned}
\tag{2}
$$

where $C_V$ is the isovolumme heat capacity and $B_{2\mathrm{D}}$ is the two-dimensional bulk modulus

$$
B_{2 \mathrm{D}}(T)=A \frac{\partial^{2} F_{\mathrm{tot}}}{\partial A^{2}}=\frac{1}{2 \sqrt{3} a^{2}}\left[s_{1}-s_{2}+s_{3}+s_{4}\right], \tag{3}
$$

where $A\left(=\frac{\sqrt{3}}{2} a^{2}\right)$ is the unit area and

$$
\begin{aligned}
& s_{1}=a^{2} \frac{d^{2} E^{e}(a)}{d a^{2}}, \quad s_{2}=a \frac{d E^{e}(a)}{d a}, \\
& s_{3}=\frac{1}{N_{k}} \sum_{k, \lambda}\left[U_{k, \lambda}-T C_{V}^{k, \lambda}\right] \gamma_{k, \lambda}^{2}, \quad s_{4}=\frac{2}{N_{k}} \sum_{k, \lambda} U_{k, \lambda} \gamma_{k, \lambda}.
\end{aligned}
\tag{4}
$$

The contributions of thermal expansion and phonon excitation to $B_{2\mathrm{D}}$ are included in $(s_1 - s_2)$ and $(s_3 + s_4)$, respectively, and the phonon excitation is omitted in the quasistatic bulk modulus $(B_{2\mathrm{D}}^*)$ [43]. Temperatures higher than 600 K are not considered here, due to the low thermodynamic/kinetic stability of these systems found in experiments [19,30,44], as well as to the appearance of high-order anharmonicity that not included in QHA [45,46].

## III. RESULTS AND DISCUSSION

Hydrogenated Si and Ge (HSi and HGe) are used to study the effects of chemical functionalization. The structures are shown in Fig. 1(a), and the calculated equilibrium lattice constants $(a)$, buckling heights $(\Delta_z)$, and bond lengths $(d)$ are listed in Table I, which are consistent with other experimental [19,22,30,44] and theoretical results [9,10,24,25,28]. The differential electron densities between the pre- and post-bonding states $(\Delta \rho)$ are projected onto the $z$ direction $(\Delta \rho_z)$, which are shown in Figs. 1(b) and 1(c). The $\sigma$ and $\pi$ bonds coexist and compete with each other in buckled Si and Ge due to the partial $sp^3$ orbital hybridization [9,10]. Therefore, apart from the space between the Si/Ge atoms $(|z| < \Delta_z)$, the electrons also have some observable accumulation $(\Delta \rho_z > 0)$ outside $(|z| > \Delta_z)$ due to the $\pi$ bonding [Figs. 1(b) and 1(c), left panels]. Si has a smaller $\Delta_z$ (0.22 Å) than Ge (0.34 Å), indicating the less $sp^3$ hybridization in the former. Hydrogenation heightens $\Delta_z$ (Table I) and removes the $\pi$ electrons [Fig. 1(b) and 1(c), right panels], due to the increased $sp^3$ hybridization. The bond energy $(\epsilon_b)$ is defined to be the energy cost to break a Si-Si/Ge-Ge bond, which is used to indicate the bond strength. Although the $\sigma$ bond is strengthened by hydrogenation, the total strength $(\epsilon_b)$ of a Si-Si/Ge-Ge bond is decreased (Table I), due to the removal of the $\pi$ bond. On the other hand, hydrogenation increases the dynamical stability of the bond, due to the removal of the $\sigma$-$\pi$ competition. These changes in the bond characteristics (hybridization, geometry, strength, and dynamical stability) by hydrogenation will have profound effects on the lattice dynamics.

<table>
<caption>TABLE I. Equilibrium lattice constant $(a)$, zero-point expansion $(\delta_{zp})$, buckling height $(\Delta_z)$, bond lengths $(d_{\text{X-X}}$ and $d_{\text{X-H}}$, X = Si or Ge), and bond energy $(\epsilon_b)$ of Si, HSi, Ge, and HGe.</caption>
<thead>
  <tr>
    <th></th>
    <th>$a$ (Å)</th>
    <th>$\delta_{zp}$ (%)</th>
    <th>$\Delta_z$ (Å)</th>
    <th>$d_{\text{X-X}}$ (Å)</th>
    <th>$d_{\text{X-H}}$ (Å)</th>
    <th>$\epsilon_b$ (eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Si</td>
    <td>3.87</td>
    <td>0.13</td>
    <td>0.224</td>
    <td>2.28</td>
    <td>–</td>
    <td>2.91</td>
  </tr>
  <tr>
    <td>HSi</td>
    <td>3.89</td>
    <td>0.11</td>
    <td>0.359</td>
    <td>2.36</td>
    <td>1.501</td>
    <td>2.51</td>
  </tr>
  <tr>
    <td>Ge</td>
    <td>4.04</td>
    <td>0.12</td>
    <td>0.340</td>
    <td>2.43</td>
    <td>–</td>
    <td>2.41</td>
  </tr>
  <tr>
    <td>HGe</td>
    <td>4.07</td>
    <td>0.13</td>
    <td>0.367</td>
    <td>2.46</td>
    <td>1.552</td>
    <td>2.00</td>
  </tr>
</tbody>
</table>

![](./images/814627781475303425_1.jpg)

FIG. 1. (Color online) (a) Structures and (b) and (c) $\Delta \rho_z$ of pristine/hydrogenated Si and Ge. The origin ($\sigma$ and/or $\pi$ bondings) of the electron accumulation $(\Delta \rho_z > 0)$ near the Si/Ge atoms are indicated in shades.

A detailed knowledge of the vibrational states is a prerequisite for understanding various phononic and thermodynamic properties. The phonon dispersions and density of states $(g_{\text{ph}})$ of Si, HSi, Ge, and HGe are shown in the left and middle panels of Fig. 2, where the phonon branches are labeled according to their initial symmetries at the $\Gamma$ point, and the amplitudes of the in-plane (XY) and out-of-plane (Z) vibrations are indicated by the linewidths. The evolution of the phononic eigenvectors of Si along the $\Gamma K$ path are visualized in Fig. 3. The TA, TO, and LO branches in Si/Ge only consist of the XY vibration, and the ZA branch of the Z vibration [Figs. 2(a) and 2(c)]. Thus, the atomic displacements in these four modes (Fig. 3) are only modulated by the Bloch phase factor $(e^{-i\mathbf{k}\cdot\mathbf{r}})$. However, in the LA and ZO branches, the XY and Z vibrations hybridize and swap with each other at $k \sim 0.22\Gamma K/\Gamma M$ in Si ($0.40\Gamma K/\Gamma M$ in Ge). This vibrational hybridization is caused by the nonorthogonal covalent bonds, which also have been observed in functionalized graphene [47] and $\text{MoS}_2$ [42] with nonorthogonal C-C and Mo-S bonds, respectively. In planar graphene, the XY modes (TA, LA, TO, and LO) are completely decoupled with the Z modes (ZA and ZO) [47], because the C-C bonds in the XY plane are orthogonal to the Z direction. The LA-ZO vibrational hybridization changes the LA mode from XY to Z symmetry, which renders the LA branch able to couple with the ZA branch at the Brillouin zone boundary

![](./images/814627781475303425_2.jpg)

FIG. 2. (Color online) Phonon dispersions $g_{ph}$ and $\gamma$ dispersions of (a) Si, (b) HSi, (c) Ge, and (d) HGe. The linewidths in the phonon dispersions are scaled by the amplitudes of XY and Z vibrations, and the antisymmetric H modes in (b) and (d) are labeled with the superscript $^{*}$.

[Figs. 2(a) and 2(c)], where they are similar in both frequency and symmetry. The LA-ZO and LA-ZA couplings result in the flat dispersion of the LA branch at $110\ \text{cm}^{-1}$ in Si (60 $\text{cm}^{-1}$ in Ge). The acoustic/optical modes with Z vibration have lower frequencies than their counterparts with XY vibration, because the former ones mainly consist of the out-of-plane bending of the Si-Si/Ge-Ge bonds, which are softer than the later ones consisting of the in-plane bond bending/stretching. This is a low-dimensional effect in phonon spectra. Ge has a larger buckling height $\Delta_{z}$ than Si, and the contribution of bond stretching in the ZO branch is larger in a more buckled layer, which tends to stiffen the ZO modes. This is a thickness effect in the lattice dynamics of low-dimensional systems [41]. Therefore, the LA-ZO coupling in Ge is smaller than that in Si, resulting in more XY (Z) vibration in the LA (ZO) branch and larger dispersive LA branch in Ge [Fig. 2(c)]. Hydrogenation additionally introduces four bending (TB, TB*, LB, and LB*) and two stretching modes (ZS and ZS*), and the H atoms also have some resonating displacements in the acoustic and optical modes [Figs. 2(b) and 2(d)]. Hydrogenation increases the layer thickness ($\Delta_{z}$, Table I), which stiffens the ZO modes and enlarges the LA-ZO frequency gap. The $\frac{\omega_{ZO}-\omega_{LA}}{(\omega_{ZO}+\omega_{LA})/2}$ ratio is increased from 0.51 (0.51) in Si (Ge) up to 0.69 (0.65) in HSi (HGe), which significantly decreases the LA-ZO coupling, and then increases XY (Z) vibration in the LA (ZO) branch. With less Z vibration in the LA branch after hydrogenation, the LA-ZA coupling at the zone boundary is then decreased due to their enlarged symmetry difference, making the LA branch there more dispersive. In addition, the ZA branches in both Ge and HGe have wiggles near the $\Gamma$ point, which indicates their low dynamical stability (originating from weak $\sigma$ bond and $\sigma$-$\pi$ competition). This agrees with the facts that Ge still has not be synthesized due to the preferred germanium-substrate alloying [20], and that HGe has a low amorphodization/decomposition temperature ($\lesssim348$ K) [30]. HGe is synthesized prior to Ge, which may be due to the dynamical-stability enhancement by hydrogenation.

![](./images/814627781475303425_3.jpg)

FIG. 3. (Color online) The phonon modes in Si at different $k$ points.

The Grüneisen-constant ($\gamma$) dispersions are shown in the right panels of Fig. 2. $\gamma$(ZA) has large negative values, which is ubiquitous for the bending ZA modes in two- dimensional systems [42]. These bending ZA modes resemble the flexural vibration in guitar string, where a tensile makes the lattice/string stiffer to such bending vibration, resulting in a higher frequency and then a negative $\gamma$. This is called guitar-string analogy [48] or membrane effect [49]. Apart from $\gamma$(ZA), $\gamma$(TA) and $\gamma$(LA) also have negative values in Si and Ge. In a TA mode, the lattice is transversely distorted in the XY plane (Fig. 3), and the restoring force comes from both the in-plane bending and stretching of the covalent bonds. Bond bending negatively contributes to $\gamma$

due to the guitar-string analogy, while bond stretching has a normal positive contribution to $\gamma$. When the bond is not strong enough, the effect of bond stretching cannot compete with that of bond bending, resulting in negative net $\gamma$(TA). Diamond and graphene only have positive $\gamma$(TA) [47,49] due to the strong C-C bonds, while bulk silicon and germanium have negative $\gamma$(TA) [50,51] due to the relatively weak Si-Si and Ge-Ge bonds. Through the LA-ZO and LA-ZA couplings, the weight of Z vibration in the LA branch increases when leaving the $\Gamma$ point [Figs. 2(a) and 2(c), left panels], which increases the contribution of out-of-plane bond bending, and then results in negative $\gamma$(LA), especially at the zone boundary. All the optical branches only have positive $\gamma$, due to the dominating effect of bond stretching, which is similar in functionalized graphene [47,49]. However, the $\gamma$(ZO) in planar graphene is negative, because of the dominating bond-bending effect in those ZO modes. Except for the rippling part of the $\gamma$(ZA) dispersion in Ge, hydrogenation increases the $\gamma$ of ZA, TA, and LA modes in Si and Ge, because the layer thickening increases the positive contribution of bond stretching in these acoustic modes. The abnormal rippling part of the $\gamma$(ZA) in Ge is caused by the low bond dynamical stability, and those ripples in $\gamma$(ZA) are largely suppressed by hydrogenation, because the related ZA modes become closer to normal two-dimensional bending modes. The $\gamma$(ZO) of Si is exceptionally high $(=9)$ near the $\Gamma$ point, due to the stretching of the nonorthogonal strong $\pi$ bonds in the lowly buckled Si lattice (Table I). Hydrogenation more or less decreases the $\gamma$ of ZO, TO, and LO modes in Si and Ge, because the elimination of the $\pi$ bond decreases the bond strength and then the effect of bond stretching. The bending and stretching hydrogen modes (TB, $\text{TB}^*$, LB, $\text{LB}^*$, ZS, and $\text{ZS}^*$) in HSi and HGe all have near-zero $\gamma$, because the restoring forces on those perpendicular C-H bonds are insensitive to the lateral-size variation. This means that hydrogenation is an ideal approach to study the effect of chemical functionalization on the lattice dynamics of Si and Ge, because those modes specific to H atoms have negligible effects on the lattice anharmonicity.

The above analyzed phononic properties can help understand various thermodynamic properties of Si and Ge, as well as the effects of functionalization. The calculated thermal-expansion coefficient $(\alpha)$, isovolume heat capacity $(C_V)$, and quasiharmonic/quasistatic bulk modulus $(B_{2\text{D}}/B_{2\text{D}}^*)$ of Si, HSi, Ge, and HGe are shown in Fig. 4. A fully excited phonon branch contributes $1.0\ k_B$ to $C_V$, and the nominal number of excited branches is about three at 100 (50) K in both Si and HSi (Ge and HGe) [Fig. 4(b)]. This means that the excitation of the three acoustic branches (ZA, TA, and LA) dominates at temperatures lower than 100 (50) K, and the optical modes (ZO, TO, and LO) are only considerably excited at higher temperatures. Acoustic modes mostly have negative $\gamma$, while optical modes only have positive $\gamma$ (Fig. 2, right panels). Due to the subsequent excitation of these negative- and positive-$\gamma$ modes, $\alpha$ first decreases with increasing temperature until 100 (50) K [Fig. 4(a)], and then increases. However, $\alpha$ is still consistently negative, due to the dominating contribution from the negative-$\gamma$ modes. Although the excitation of the additional H modes makes the $C_V$ of HSi (HGe) larger than that of Si (Ge) above 120 K [Fig. 4(b)], its effect on the minimum-$\alpha$ temperature is negligible due to their near-zero $\gamma$ of these modes [Figs. 2(b) and 2(d), right panels], and hydrogenation also has a negligible effect on the expansion caused by the zero-point vibrations $(\delta_{\text{zp}}$, Table I). Therefore, the hydrogenation effect on the lattice anharmonicity only comes from the chemical functionalization on the Si-Si/Ge-Ge bond. Although the hydrogenation-induced decreases of $B_{2\text{D}}$ [by 30%, Fig. 4(c)] and optical $\gamma$ [Figs. 2(a) and 2(b)] tend to further decrease the negative $\alpha$ [Eq. (2)], $\alpha$(HSi) is still close to $\alpha$(Si), due to the canceling effect from the increase of acoustic $\gamma$ [Figs. 2(a) and 2(b)]. $\alpha$(Ge) is much higher than $\alpha$(HGe) (by $4\times10^{-6}\ \text{K}^{-1}$ above 300 K), because $\gamma$(ZA) is significantly decreased by hydrogenation [Figs. 2(c) and 2(d)], which negatively contributes to $\alpha$.

![](./images/814627781475303425_4.jpg)

FIG. 4. (Color online) Temperature dependence of (a) $\alpha$, (b) $C_V$, and (c) and (d) $B_{2\text{D}}$ and $B_{2\text{D}}^*$ of Si, HSi, Ge, and HGe. In (c) and (d), the curve slopes (in $10^{-5}\ \text{eV}\ \mathring{\text{A}}^{-2}\text{K}^{-1}$) at 300 K are indicated.

Thermal expansion is caused by the excitation of anharmonic phonons, while both thermal expansion and phononic excitation have individual contributions to the thermomechanics [Eqs. (3) and (4)]. Both contributions are considered in the temperature dependence of $B_{2\text{D}}$, while only the former in that of $B_{2\text{D}}^*$. The negative thermal expansion results in the increase of $B_{2\text{D}}^*$ under heating, due to the increased curvature of the potential-energy surface under lattice contraction (i.e., $\frac{dB_{2\text{D}}^*}{dT}<0$). The stiffening effect from the zero-point vibrations makes $B_{2\text{D}}$ larger than $B_{2\text{D}}^*$ at low temperatures. However, $B_{2\text{D}}(T)$ curves have lower increasing rates than their $B_{2\text{D}}^*(T)$ counterparts, and the $B_{2\text{D}}$ of Si even decreases under heating, which is due to the softening effect from the excitation of negative-$\gamma$ modes [$s_4$ term in Eq. (3)]. Therefore, thermal expansion and phonon excitation have reverse effects on $B_{2\text{D}}$, which also has been observed in positively expanding $\text{MoS}_2$ [42]. Although hydrogenation decreases $B_{2\text{D}}$ and $B_{2\text{D}}^*$ due to the bond weakening (Table I), hydrogenation increases both the slopes of $B_{2\text{D}}(T)$ and $B_{2\text{D}}^*(T)$ curves ($\frac{dB_{2\text{D}}}{dT}$ and $\frac{dB_{2\text{D}}^*}{dT}$). $\frac{dB_{2\text{D}}}{dT}$ equals $a\frac{dB_{2\text{D}}}{da}\alpha$, and the $\frac{dB_{2\text{D}}}{dT}$ of Si at 300 K is increased by $5.0\times10^{-5}\ \text{eV}\ \mathring{\text{A}}^{-2}\text{K}^{-1}$. As Si and HSi have the same $\alpha$, this increase is only ascribed to the enlargement of potential-surface anharmonicity, namely, to the decrease in


$a \frac{d B_{2 \mathrm{p}}^{*}}{d a}$ (from $-6.3$ to $-13.3$ eV $\AA^{-2}$). The increase in the $\frac{d B_{2 \mathrm{p}}}{d T}$ of Si by hydrogenation is even larger (by $6.7 \times$ $10^{-5}$ eV $\AA^{-2} \mathrm{~K}^{-1}$) than $\frac{d B_{2 \mathrm{p}}^{*}}{d T}$, due to the increased acoustic $\gamma\left(\frac{d B_{2 \mathrm{p}}}{d T} \sim \sum C_{V}^{k, \lambda} \gamma_{k, \lambda}\right)$. The decrease in the negative $\alpha$ of Ge by hydrogenation contributes to the increase of $\frac{d B_{2 \mathrm{p}}}{d T}$ (by $3.1 \times 10^{-5}$ eV $\AA^{-2} \mathrm{~K}^{-1}$ at 300 K), which is partially canceled by the increase in $a \frac{d B_{2 \mathrm{p}}^{*}}{d a}$ (from $-18.6$ to $-13.8$ eV $\AA^{-2}$). The increase in $\frac{d B_{2 \mathrm{p}}}{d T}$ (by $2.4 \times 10^{-5}$ eV $\AA^{-2} \mathrm{~K}^{-1}$) is smaller than that of $\frac{d B_{2 \mathrm{p}}^{*}}{d T}$, due to the decrease in $\gamma(\mathrm{ZA})$ after the dynamical-stability enhancement by hydrogenation [Figs. 2(c) and 2(d)].

## IV. SUMMARY
In summary, the roles of lattice dimensionality and bond characteristics in the lattice dynamics of silicene and germanene, as well as in the chemical functionalization effects, have been revealed. For the substrate-supported silicene and germanene [31-35], as well as other two-dimensional materials, the environmental interactions may bring some complicated structural and electronic influences [52-54]. The physical picture and analysis methods established here for the correlation between structure, electronics, and lattice dynamics will be useful for studying the corresponding lattice anharmonicity therein.

## ACKNOWLEDGMENTS
This work is supported by the National Science Foundation of China under Grant No. 11204305 and U1230202(NSAF), and the special Funds for Major State Basic Research Project of China (973) under Grant No. 2012CB933702. The calculations were performed in Center for Computational Science of CASHIPS and on the ScGrid of Supercomputing Center, Computer Network Information Center of CAS.

[1] K. Takeda and K. Shiraishi, Theoretical possibility of stage corrugation in Si and Ge analogs of graphite, *Phys. Rev. B* **50**, 14916 (1994).

[2] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Electric field effect in atomically thin carbon films, *Science* **306**, 666 (2004).

[3] A. K. Geim, Nobel lecture: Random walk to graphene, *Rev. Mod. Phys.* **83**, 851 (2011).

[4] V. Singh, D. Joung, L. Zhai, S. Das, S. I. Khondaker, and S. Seal, Graphene based materials: Past, present and future, *Prog. Mater. Sci.* **56**, 1178 (2011).

[5] A. K. Geim and K. S. Novoselov, The rise of graphene, *Nat. Mater.* **6**, 183 (2007).

[6] L. F. Huang, T. F. Cao, P. L. Gong, Z. Zeng, and C. Zhang, Tuning the adatom-surface and interadatom interactions in hydrogenated graphene by charge doping, *Phys. Rev. B* **86**, 125433 (2012).

[7] M. Xu, T. Liang, M. Shi, and H. Chen, Graphene-like two- dimensional materials, *Chem. Rev.* **113**, 3766 (2013).

[8] D. Jose and A. Datta, Structures and chemical properties of silicene: Unlike graphene, *Acc. Chem. Res.* **47**, 593 (2014).

[9] S. Cahangirov, M. Topsakal, E. Aktürk, H. Şahin, and S. Ciraci, Two- and one-dimensional honeycomb structures of silicon and germanium, *Phys. Rev. Lett.* **102**, 236804 (2009).

[10] H. Şahin, S. Cahangirov, M. Topsakal, E. Bekaroglu, E. Akturk, R. T. Senger, and S. Ciraci, Monolayer honeycomb structures of group-IV elements and III-V binary compounds: First-principles calculations, *Phys. Rev. B* **80**, 155453 (2009).

[11] C. C. Liu, W. Feng, and Y. Yao, Quantum spin hall effect in silicene and two-dimensional germanium, *Phys. Rev. Lett.* **107**, 076802 (2011).

[12] M. Ezawa, Valley-polarized metals and quantum anomalous hall effect in silicene, *Phys. Rev. Lett.* **109**, 055502 (2012).

[13] W. F. Tsai, C. Y. Huang, T.-R. Chang, H. Lin, H.-T. Jeng, and A. Bansil, Gated silicene as a tunable source of nearly 100% spin-polarized electrons, *Nat. Commun.* **4**, 1500 (2013).

[14] N. D. Drummond, V. Zólyomi, and V. I. Fal'ko, Electrically tunable band gap in silicene, *Phys. Rev. B* **85**, 075423 (2012).

[15] Z. Ni, Q. Liu, K. Tang, J. Zheng, J. Zhou, R. Qin, Z. Gao, D. Yu, and J. Lu, Tunable bandgap in silicene and germanene, *Nano Lett.* **12**, 113 (2012).

[16] H. Pan, Z. Li, C.-C. Liu, G. Zhu, Z. Qiao, and Y. Yao, Valley- polarized quantum anomalous hall effect in silicene, *Phys. Rev. Lett.* **112**, 106802 (2014).

[17] X. Li, J. T. Mullen, Z. Jin, K. M. Borysenko, M. Buongiorno Nardelli, and K. W. Kim, Intrinsic electrical transport properties of monolayer silicene and $\mathrm{MoS}_{2}$ from first principles, *Phys. Rev. B* **87**, 115418 (2013).

[18] B. Lalmi, H. Oughaddou, H. Enriquez, A. Kara, S. Vizzini, B. Ealet, and B. Aufray, Epitaxial growth of a silicene sheet, *Appl. Phys. Lett.* **97**, 223109 (2010).

[19] P. Vogt, P. De Padova, C. Quaresima, J. Avila, E. Frantzeskakis, M. C. Asensio, A. Resta, B. Ealet, and G. Le Lay, Silicene: Compelling experimental evidence for graphenelike two- dimensional silicon, *Phys. Rev. Lett.* **108**, 155501 (2012).

[20] A. Kara, H. Enriquez, A. P. Seitsonen, L. C. Lew Yan Voon, S. Vizzini, B. Aufray, and H. Oughaddou, A review on silicene— New candidate for electronics, *Surf. Sci. Rep.* **67**, 1 (2012).

[21] L. Meng, Y. Wang, L. Zhang, S. Du, R. Wu, L. Li, Y. Zhang, G. Li, H. Zhou, W. A. Hofer et al., Buckled silicene formation on Ir(111), *Nano Lett.* **13**, 685 (2013).

[22] A. Fleurence, R. Friedlein, T. Ozaki, H. Kawai, Y. Wang, and Y. Yamada-Takamura, Experimental evidence for epitaxial silicene on diboride thin film, *Phys. Rev. Lett.* **108**, 245501 (2012).

[23] L. Tao, E. Cinquanta, D. Chiappe, C. Grazianetti, M. Fanciulli, M. Dubey, A. Molle, and D. Akinwande, Silicene field-effect transistors operating at room temperature, *Nat. Nanotechnol.* **10**, 227 (2015).

[24] M. Houssa, E. Scalise, K. Sankaran, G. Pourtois, V. V. Afanas'ev, and A. Stesmans, Electronic properties of hydrogenated silicene and germanene, *Appl. Phys. Lett.* **98**, 223107 (2011).

[25] F.-B. Zheng and C.-W. Zhang, The electronic and magnetic properties of functionalized silicene: A first-principles study, *Nanoscale Res. Lett.* **7**, 422 (2012).

[26] N. Gao, W. T. Zheng, and Q. Jiang, Density functional theory calculations for two-dimensional silicene with halogen functionalization, *Phys. Chem. Chem. Phys.* **14**, 257 (2012).

[27] Y. Ding and Y. Wang, Electronic structures of silicene fluoride and hydride, *Appl. Phys. Lett.* **100**, 083102 (2012).

[28] S. Trivedi, A. Srivastava, and R. Kurchania, Silicene and germanene: A first principle study of electronic structure and effect of hydrogenation-passivation, *J. Comput. Theor. Nanosci.* **11**, 781 (2014).

[29] B. van den Broek, M. Houssa, E. Scalise, G. Pourtois, V. V. Afanas'ev, and A. Stesmans, First-principles electronic func- tionalization of silicene and germanene by adatom chemisorp- tion, *Appl. Surf. Sci.* **291**, 104 (2014).

[30] E. Bianco, S. Butler, S. Jiang, O. D. Restrepo, W. Windl, and J. E. Goldberger, Stability and exfoliation of germanene: A germanium graphane analogue, *ACS Nano* **7**, 4414 (2013).

[31] C.-L. Lin, R. Arafune, K. Kawahara, M. Kanno, N. Tsukahara, E. Minamitani, Y. Kim, M. Kawai, and N. Takagi, Substrate- induced symmetry breaking in silicene, *Phys. Rev. Lett.* **110**, 076801 (2013).

[32] L. Chen, H. Li, B. Feng, Z. Ding, J. Qiu, P. Cheng, K. Wu, and S. Meng, Spontaneous symmetry breaking and dynamic phasetransition in monolayer silicene, *Phys. Rev. Lett.* **110**, 085504(2013).

[33] A. Acun, B. Poelsema, H. J. W. Zandvliet, and R. van Gastel, The instability of silicene on Ag(111), *Appl. Phys. Lett.* **103**,263119 (2013).

[34] S. Cahangirov, M. Audiffred, P. Tang, A. Iacomino, W. Duan, G. Merino, and A. Rubio, Electronic structure of silicene onAg(111): Strong hybridization effects, *Phys. Rev. B* **88**, 035432(2013).

[35] Y. Yuan, R. Quhe, J. Zheng, Y. Wang, Z. Ni, J. Shi, and J.Lu, Strong band hybridization between silicene and Ag(111) substrate, *Physica E* **58**, 38 (2014).

[36] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, *Rev. Mod. Phys.* **73**, 515 (2001).

[37] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo *et al.*, QUANTUM ESPRESSO: A modular and open- source software project for quantum simulations of materials, *J.Phys. Condens. Matter* **21**, 395502 (2009).

[38] D. Vanderbilt, Soft self-consistent pseudopotentials in a gener- alized eigenvalue formalism, *Phys. Rev. B* **41**, 7892(R) (1990).

[39] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation, *Phys. Rev. B* **46**,6671 (1992).

[40] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, *Phys. Rev. B* **13**, 5188 (1976).

[41] L. F. Huang and Z. Zeng, Lattice dynamics and disorder-induced contraction in functionalized graphene, *J. Appl. Phys.* **113**,083524 (2013).

[42] L. F. Huang, P. L. Gong, and Z. Zeng, Correlation between struc- ture, phonon spectra, thermal expansion, and thermomechanics of single-layer MoS₂, *Phys. Rev. B* **90**, 045409 (2014).

[43] Y. Wang, J. J. Wang, H. Zhang, V. R. Manga, S. L. Shang, L.-Q. Chen, and Z.-K. Liu, A first-principles approach to finite temperature elastic constants, *J. Phys. Condens. Matter* **22**,225404 (2010).

[44] H. Enriquez, S. Vizzini, A. Kara, B. Lalmi, and H. Oughaddou, Silicene structures on silver surfaces, *J. Phys. Condens. Matter* **24**, 314211 (2012).

[45] A. van de Walle and G. Ceder, The effect of lattice vibrations on substitutional alloy thermodynamics, *Rev. Mod. Phys.* **74**, 11(2002).

[46] K. V. Zakharchenko, M. I. Katsnelson, and A. Fasolino, Finite temperature lattice properties of graphene beyond thequasiharmonic approximation, *Phys. Rev. Lett.* **102**, 046808(2009).

[47] L. F. Huang, T. F. Cao, P. L. Gong, and Z. Zeng, Isotope effects on the vibrational, Invar, and Elinvar properties of pristine and hydrogenated graphene, *Solid State Commun.* **190**, 5 (2014).

[48] B. Fultz, Vibrational thermodynamics of materials, *Prog. Mater. Sci.* **55**, 247 (2010).

[49] N. Mounet and N. Marzari, First-principles determination of the structural, vibrational and thermodynamic properties ofdiamond, graphite, and derivatives, *Phys. Rev. B* **71**, 205214(2005).

[50] C. H. Xu, C. Z. Wang, C. T. Chan, and K. M. Ho, Theory of the thermal expansion of Si and diamond, *Phys. Rev. B* **43**, 5024(1991).

[51] S. Wei, C. Li, and M. Y. Chou, Ab initio calculation of thermodynamic properties of silicon, *Phys. Rev. B* **50**, 14587(1994).

[52] N. Gao, J. C. Li, and Q. Jiang, Bandgap opening in silicene: Effect of substrates, *Chem. Phys. Lett.* **592**, 222 (2014).

[53] H. Liu, J. Gao, and J. Zhao, Silicene on substrates: A way to preserve or tune its electronic properties, *J. Phys. Chem. C* **117**,10353 (2013).

[54] Y. Cai, C. P. Chuu, C. M. Wei, and M. Y. Chou, Stability and electronic properties of two-dimensional silicene and germanene on graphene, *Phys. Rev. B* **88**, 245408 (2013).