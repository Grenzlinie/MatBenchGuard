PHYSICAL REVIEW B 99, 214504 (2019)

# Superconductivity by doping in alkali-metal hydrides without applied pressure: An ab initio study

M. A. Olea-Amezcua, $^{1,2, *}$ O. De la Peña-Seaman, $^{1}$ and R. Heid $^{3}$

$^{1}$ Instituto de Física, Benemérita Universidad Autónoma de Puebla, Apartado Postal J-48, 72570, Puebla, Puebla, México
$^{2}$ Escuela de Artes Plásticas y Audiovisuales, Benemérita Universidad Autónoma de Puebla,
Vía Atlixcáyotl No. 2499, 72810, Puebla, Puebla, México
$^{3}$ Institut für Festkörperphysik, Karlsruher Institut für Technologie (KIT), P.O. Box 3640, D-76021 Karlsruhe, Germany

![](./images/812766265281085441_1.jpg)
(Received 16 January 2019; revised manuscript received 28 May 2019; published 12 June 2019)

The electronic, lattice dynamical, electron-phonon coupling, and superconducting properties of alkali-metal hydrides LiH, NaH, and KH, metalized through doping with alkaline-earth metals Be, Mg, and Ca, respectively, are investigated within the framework of density functional perturbation theory. The alloys were modeled by the self-consistent virtual crystal approximation, and the effect of zero-point energy contribution is consistently taken into account. For all three alloys, a steady increase of the electron-phonon coupling constant $\lambda$ is found with progressive alkaline-earth metal doping, reaching values as high as 0.47 for (Li/Be)H, 1.26 for (Na/Mg)H, and 1.69 for (K/Ca)H. The growth of $\lambda$ with doping is the result of two effects: the softening of the phonon spectrum, mainly of the H-optical modes, and the increase of the density of states at the Fermi level. Estimates of the superconducting critical temperature reach values of 2.1 K for $Li_{0.95}Be_{0.05}H$, 28 K for $Na_{0.8}Mg_{0.2}H$, and even 49 K for $K_{0.55}Ca_{0.45}H$, demonstrating that doping is an alternative route to high transition temperatures in this material class without the need to apply high external pressure.

DOI: 10.1103/PhysRevB.99.214504

## I. INTRODUCTION

The search for high-temperature superconductors has ex- perienced a renewal since 2015 with the discovery of phonon- mediated superconductivity on $H_{3}S$ (produced by the synthe sis or decomposition of $H_{2}S$ ), with a critical temperature $(T_{c})$ of 203 K under pressures as high as 200 GPa by Drozdov et al. [1]. Such a breakthrough was achieved by a synergy between experiments and theoretical studies, which predicted the transformation of $H_{2}S$ to a metal and a superconductor at high pressure $(\approx 100$ GPa) with a $T_{c} \approx 80$ K prior to the experimental verification [2].

However, the general idea of applying pressure to metalize hydrides and to convert them into superconductors is not new [3]. In fact, several theoretical reports and calculations have been published years ago predicting high $T_{c}$ values for systems like $SiH_{4}$ (166 K at 202 GPa) [4-6] or $GeH_{4}$ (64 K at 220 GPa) [7], among others [8]. Yet, only for a small subset of them, superconductivity with rather low $T_{c}$ values could be confirmed experimentally [9]. Thus, Drozdov's publication [1] led to intensified theoretical activities, aiming to find new families of high- $T_{c}$ superconductor hydrides. Examples are $H_{4}Te$ with $T_{c}$ of 104 K at 170 GPa [10], $AcH_{10}$ with $T_{c}$ in the range of 204-251 K at 200 GPa [11], $MgH_{12}$ with $T_{c} \sim$ 47-60 K at 140 GPa [12], and also in some ternary hydrides like $MgSiH_{6}$ with a $T_{c} \sim 63$ K at 250 GPa [13]. In most cases, however, metalization and superconductivity occurs only at very high applied pressure.

A promising criterion to achieve a high $T_{c}$ in hydride mate rials is a particular combination of strong covalent bonding between H and other elements of the compound, and the presence of high-frequency modes in the phonon spectrum [1]. However, hydrogen-rich solids are typically insulators at ambient pressure, and thus have to be compressed under high pressure in order to reach a metallic state and ultimately to become superconducting.

One group of materials, the alkali-metal hydrides, pos- sesses the above mentioned prerequisites. At atmospheric conditions this group crystallizes in the NaCl (B1) structure and adopts a stoichiometry MH, with $M=$ Li, Na, K, Rb, or Cs. The band gap of this family is rather large and ranges between 4 and 6 eV [14], thus high pressures are required for metalization. According to ab initio calculations, the gap closes between 300 and 1000 GPa [15,16], but the resulting band overlap is unlikely to generate a sufficiently high density of states at the Fermi level $[N(E_{F})]$, suggesting that these compounds are not good candidates for high- $T_{c}$ superconduc tors [17]. Still, besides pressurization there are other proce- dures to turn insulators into a metallic state, like doping or gating [1]. Doping has been studied before in superconducting hydrogen chalcogenides $H_{3}M$ ( $M=$ S, Se) by substitutions with group-V and group-VII elements (representing hole and electron doping, respectively), but only in the superconduct- ing phase, i.e., under high pressure conditions [18]. One example for an investigation of metalizing hydrides by doping without applied pressure, is the paper of Zhang et al. [19], where the electron-phonon (e-ph) coupling and superconduc- tivity of n-doped LiH was studied by first-principles methods. When substituting Li with Be, Mg, or Ca, the dopant acts as a donor which delivers electrons to the system, obtaining a n-doped material. In that study, for an electron content as high as 2.06 a $T_{c}=7.78$ K is calculated at ambient pressure, while the e-ph coupling $(\lambda=0.86)$ is dominated by the optical

*monica.olea@correo.buap.mx

2469-9950/2019/99(21)/214504(9) 214504-1 ©2019 American Physical Society

phonon modes on the system [19]. Although the predicted $T_c$ value for $n$-doped LiH is far smaller compared to the one of $H_3S$ or other hydrides proposed as possible high- superconducting materials, it represents a different approach worth exploring in the search for superconductivity on very well known metal hydrides and related systems.

In this paper we present a systematic study of the structural and electronic properties, lattice dynamics, e-ph coupling, and superconductivity of the alkali-metal hydrides LiH, NaH, and KH doped with alkaline-earth metals Be, Mg, and Ca, respectively, in order to obtain electron ($n$)-doped metal hy- drides, within the framework of density functional theory (DFT) [20] and the self-consistent virtual crystal approxima- tion [21]. In all cases, the crystal structure was optimized and the electronic band structure and density of states obtained applying DFT methods at several concentrations for each compound. Lattice-dynamical properties are studied using density functional perturbation theory (DFPT) [22–24]. The quantities determined by DFPT allow us in a straightforward way to evaluate the microscopic e-ph interaction, like the Eliashberg function $\alpha^2F(\omega)$, and the e-ph coupling constant $\lambda$, which is required as an input to the strong-coupling Eliashberg theory [25]. Superconducting critical temperatures for the dif- ferent studied systems are obtained by solving the linearized Eliashberg gap equations in the isotropic limit. The effect of zero-point energy (ZPE) on these quantities is analyzed.

The paper is organized as follow: In Sec. II the details of the computational method are described. Results for structural and electronic properties are given in Secs. III A and III B, respectively, while lattice dynamical properties are discussed in Sec. III C. Finally, e-ph coupling properties and supercon- ducting critical temperature are analyzed and discussed in Sec. III D, followed by concluding remarks in Sec. IV.

## II. METHODOLOGY

$Ab$ initio calculations were performed within the frame- work of density functional theory (DFT) [20] and the mixed- basis pseudopotential method (MBPP) [26,27] to obtain the structural and electronic ground-state properties. The MBPP uses a combination of plane waves and localized functions centered at atomic sites as a basis set for the expansion of the valence wave functions. This improves the description of more localized orbitals with respect to the standard plane- wave approach, allowing a reduction of the size of the ba- sis set. For H, Li/Be, Mg/Na, and K/Ca norm-conserving pseudopotentials were built applying the Vanderbilt descrip- tion [28]. Alloys were simulated using the virtual crystal approximation (VCA), where the ionic potential at an alloy atomic site at a given concentration $x$ is represented by the pseudopotential generated for a virtual atom with fractional nuclear charge [21]. $2p^6$ semicore states of K and Ca were treated as valence electrons. The Perdew-Burke-Ernzerhof (PBE) functional [29] was employed to take into account the exchange and correlation contributions. As energy cutoff for the plane waves we used 20 Ry for the system $Li_{1-x}Be_xH$, 28 Ry for $Na_{1-x}Mg_xH$, and 30 Ry for $K_{1-x}Ca_xH$, supplemented by local functions of $s$ type at the H, Li/Be, and Na/Mg sites, as well as of $s$ and $p$ type for K/Ca sites. A $16\times16\times16$ Monkhorst-Pack special $k$-point set was used for the Brillouin zone (BZ) integration with a Gaussian smearing of 0.2 eV [30].

The lattice dynamics were computed within the framework of density functional perturbation theory (DFPT) [22,23] as implemented in the MBPP code [24]. Complete phonon spec- tra are obtained from a Fourier interpolation of dynamical matrices calculated on a $8\times8\times8$ $q$-point mesh. Calculated phonon density of states (PDOS) are used to evaluate the zero-point energy (ZPE) correction within the quasiharmonic approximation [31,32]. Structural optimization is then per- formed either without ZPE (static scheme) or with ZPE (ZPE scheme), and electronic, phonon, and electron-phonon coupling properties are subsequently investigated for the opti- mized structures of both schemes.

The perturbative method also provides access to the mi- croscopic screened e-ph matrix elements $g_{\mathbf{k}+\mathbf{q}v',\mathbf{k}v}^{\mathbf{q}j}$, which are needed in the strong-coupling Eliashberg theory [25] to analyze the superconducting properties. The above mentioned matrix elements describe the scattering of an electron from a Bloch state with momentum $\mathbf{k}v$ to another Bloch state $\mathbf{k}+\mathbf{q}v'$ by a phonon mode $\mathbf{q}j$ and they are given by
$$
g_{\mathbf{k}+\mathbf{q}v',\mathbf{k}v}^{\mathbf{q}j} = \sqrt{\frac{\hbar}{2\omega_{\mathbf{q}j}}} \sum_{\kappa a} \frac{1}{\sqrt{M_{\kappa}}} \eta_{\kappa a}^{\mathbf{q}j} \langle \mathbf{k} + \mathbf{q}v' | \delta_{\kappa a}^{\mathbf{q}} V | \mathbf{k}v \rangle, \quad (1)
$$
where $M_{\kappa}$ is the mass of the $\kappa$th atom in the unit cell, $\eta_{a}^{\mathbf{q}j}$ is the normalized eigenvector of the phonon mode $\mathbf{q}j$, and $\omega_{\mathbf{q}j}$ is its frequency. The term $\delta_{\kappa a}^{\mathbf{q}} V$ denotes the first-order change in the total crystal potential with respect to the displacement of the atom $\kappa$ in the $a$ direction.

The phonon linewidth of the $\mathbf{q}j$ phonon mode $\gamma_{\mathbf{q}j}$ arising from the e-ph interaction is given by [33–35]
$$
\gamma_{\mathbf{q}j} = 2\pi \omega_{\mathbf{q}j} \sum_{\mathbf{k}v v'} \left| g_{\mathbf{k}+\mathbf{q}v',\mathbf{k}v}^{\mathbf{q}j} \right|^2 \delta(\varepsilon_{\mathbf{k}v} - E_F) \delta(\varepsilon_{\mathbf{k}+\mathbf{q}v'} - E_F),
\tag{2}
$$
where $\varepsilon_{\mathbf{k}v}$ represent the one-electron band energies with momentum $\mathbf{k}$ and band index $v$, and $E_F$ is the Fermi energy.

The Eliashberg spectral function in the isotropic limit $\alpha^2F(\omega)$ is described as
$$
\alpha^2 F(\omega) = \frac{1}{2\pi \hbar N(E_F)} \sum_{\mathbf{q}j} \delta(\omega - \omega_{\mathbf{q}j}) \frac{\gamma_{\mathbf{q}j}}{\omega_{\mathbf{q}j}},
\tag{3}
$$
where $N(E_F)$ is the electronic density of states (DOS) per atom and spin at $E_F$. The average e-ph coupling constant $\lambda$, which quantifies the coupling strength, is related to the Eliashberg function as
$$
\lambda = 2 \int_0^\infty \frac{\alpha^2 F(\omega)}{\omega} d\omega = \frac{1}{\pi \hbar N(E_F)} \sum_{\mathbf{q}j} \frac{\gamma_{\mathbf{q}j}}{\omega_{\mathbf{q}j}^2}.
\tag{4}
$$

Finally, the superconducting transition temperature $T_c$ was estimated for each case by numerically solving the Eliashberg gap equations on the imaginary axis [25,36–39], using the respective $\alpha^2F(\omega)$ for each doping. The Coulomb pseudopo- tential was treated as a phenomenological parameter (see discussion below).

<table>
<caption>TABLE I. Calculated lattice constants (in a.u.), for the static and ZPE schemes, of the pristine alkali-metal hydrides and its respective percentage difference with respect to the experimental values.</caption>
<thead>
<tr>
<th>System</th>
<th colspan="2">Static</th>
<th colspan="2">ZPE</th>
<th>Expt.</th>
</tr>
</thead>
<tbody>
<tr>
<td>LiH</td>
<td>7.5546</td>
<td>$( - 1.45\% )$</td>
<td>7.7021</td>
<td>$(0.44\% )$</td>
<td>$7.6685^{\mathrm{a}}$</td>
</tr>
<tr>
<td>NaH</td>
<td>9.2194</td>
<td>$(0.18\% )$</td>
<td>9.3630</td>
<td>$(1.73\% )$</td>
<td>$9.2029^{\mathrm{b}}$</td>
</tr>
<tr>
<td>KH</td>
<td>10.8423</td>
<td>$(0.59\% )$</td>
<td>10.9831</td>
<td>$(1.89\% )$</td>
<td>$10.7789^{\mathrm{b}}$</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$Reference [40].
$^{\mathrm{b}}$Reference [41] at 293 K.

### III. RESULTS AND DISCUSSION
#### A. Structural properties

We performed structural optimizations of the rock-salt type structure (B1, space group $Fm-3m$) with a primitive cell of two atoms (one metal and one hydrogen) for the three alloy systems at different values of alkaline-earth metal content $x$. Our structural results for the pristine alkali-metal hydrides under the ZPE and static schemes are in good agreement with the experimental data, [40,41] as we show in Table I, indicating the proper construction of the current pseudopotentials.

In all cases, we find that the unit cell expands as the ZPE contributions to the energy are taken into account, giving a larger lattice parameter for the ZPE scheme than for the static one. On doping, the lattice parameter for $\mathrm{Na_{1-x}Mg_{x}H}$ remains practically unchanged as the Mg content increases (this result was reported in a previous work [42]), while for both $\mathrm{Li_{1-x}Be_{x}H}$ [43] and $\mathrm{K_{1-x}Ca_{x}H}$ (see Fig. 1), the increasing electron content leads to a monotonous reduction of the lattice parameter. These trends are the same for both schemes (with or without ZPE). The contraction on doping can be attributed to extra-charge redistribution in the interstitial zone.

With the optimized lattice parameter for each system at different doping content, we proceeded to calculate the electronic and vibrational properties. As a general trend for all three alloys investigated, the phonon spectrum continuously softens with increasing doping level. At a certain threshold concentration, modes with imaginary frequencies occur, indicating a dynamical instability of the alloy. The threshold doping levels are 10% Be, 25% Mg, and 50% Ca, respectively. We therefore confine the following analysis to doping levels smaller than these thresholds. Furthermore, we will focus mainly on the ZPE scheme. The reason is, that while we have investigated both the static and ZPE scheme, their results are qualitatively very similar. The main difference lies in the lattice parameters, which give softer phonon spectra for the ZPE scheme. Results for the static scheme are presented at the end for the estimated critical temperatures only.

![](./images/812766265281085441_2.jpg)

FIG. 1. $\mathrm{K_{1-x}Ca_{x}H}$ optimized lattice parameter as a function of Ca content for the static and ZPE schemes. Experimental data was taken from Ref. [41].

![](./images/812766265281085441_3.jpg)

FIG. 2. Electronic band structure and density of states (DOS), calculated within the ZPE scheme, for (a) $\mathrm{Li_{0.95}Be_{0.05}H}$, (b) $\mathrm{Na_{0.8}Mg_{0.2}H}$, and (c) $\mathrm{K_{0.55}Ca_{0.45}H}$.

#### B. Electronic properties

The pristine metal hydrides are all insulators with a sizable experimental band gap of 4.94 eV for the LiH [44] (no experimental reports are available in the literature for NaH and KH). On doping, the extra electrons provided by the alkaline-earth atoms fill the valance bands, leading to a metallic state without the need to apply external pressure. In Fig. 2 the electronic band structures and the corresponding density of states (DOS) are displayed for each alloy at the threshold dopings. In each case, doping generates ellipsoidal Fermi surfaces, which are centered at the $X$ point for $\mathrm{Li_{1-x}Be_{x}H}$ and at the $L$ point for

![](./images/812766265281085441_4.jpg)

FIG. 3. Evolution of the total density of states at the Fermi level $N(E_F)$ as a function of the alkaline-earth metal content ($x$) for $\text{Na}_{1-x}\text{Mg}_x\text{H}$ [42] and $\text{K}_{1-x}\text{Ca}_x\text{H}$.

$\text{Na}_{1-x}\text{Mg}_x\text{H}$ and $\text{K}_{1-x}\text{Ca}_x\text{H}$. The occupied valence states are primarily derived from states of the alkaline metal: $p$ for Li, mainly $s$ for Na, and $s$, $d$ for K.

The density of states at the Fermi level $N(E_F)$ increases monotonously with $x$ (see Fig. 3), indicating a steady improvement of the metalization with increasing electron doping.

### C. Lattice dynamics
We now discuss the lattice dynamics properties as a function of doping within the stability range of each alloy system. In Figs. 4, 5, and 6 we present the phonon dispersions including their respective phonon linewidth $\gamma_{\mathbf{q}j}$ and the phonon density of states (PDOS) for $\text{Li}_{1-x}\text{Be}_x\text{H}$, $\text{Na}_{1-x}\text{Mg}_x\text{H}$, and $\text{K}_{1-x}\text{Ca}_x\text{H}$, respectively, at selected $x$ values.

In all three cases, as $x$ increases the optical branches soften, whereas the acoustic region of the phonon dispersions remains rather unaffected. In addition, phonon anomalies appear next to the $\Gamma$ point, which strengthen with increasing $x$. These anomalies at small wave vectors originate from intrapocket coupling, i.e., from a coupling to electronic states within an electron pocket (centered at $X$ for $\text{Li}_{1-x}\text{Be}_x\text{H}$ and at $L$ for $\text{Na}_{1-x}\text{Mg}_x\text{H}$ and $\text{K}_{1-x}\text{Ca}_x\text{H}$). Interestingly, although such anomalies indicate the presence of e-ph interaction close to the center of the Brillouin zone (BZ) [45], more pronounced e-ph coupling occurs far from $\Gamma$, as can be deduced from the calculated phonon linewidth [46] (vertical lines along the phonon branches). Larger values of $\gamma_{\mathbf{q}j}$ are located mainly along the high-symmetry path between $X$ and $W$ points for the optical branches which involve H vibrational modes. This resembles other high-$T_c$ hydride superconductors, where the optical hydrogen high-frequency phonon modes are responsible for the large e-ph coupling [1,17,47,48]. For the studied alloys, linewidth values monotonously increase with $x$, which is a clear sign of growing e-ph coupling with doping. The coupling of these phonons with large wave vectors essentially involves electronic states on distinct electron pockets (interpocket coupling).

![](./images/812766265281085441_5.jpg)

FIG. 4. Phonon dispersion, linewidths (vertical lines on top of the phonon branches), and phonon density of states (PDOS) for $\text{Li}_{0.95}\text{Be}_{0.05}\text{H}$, calculated for the ZPE scheme.

![](./images/812766265281085441_6.jpg)

FIG. 5. Evolution of the phonon dispersion, linewidths, and related PDOS for $\text{Na}_{1-x}\text{Mg}_x\text{H}$ at (a) $x=0.05$, (b) $x=0.1$, and (c) $x=0.2$ for the ZPE scheme.

As mentioned above, the anomalies near $\Gamma$ are located in the hydrogen optical branches, but because of avoided crossings, they drive similar anomalies in acoustic branches of the same symmetry. When the doping level reaches the threshold concentration, they induce dynamical instabilities, observed as imaginary frequencies in the phonon dispersion of $\text{Li}_{0.9}\text{Be}_{0.1}\text{H}$, $\text{Na}_{0.75}\text{Mg}_{0.25}\text{H}$, and $\text{K}_{0.5}\text{Ca}_{0.5}\text{H}$ (not shown). Phonon softening and instabilities in metal hydrides induced by alloying have been also observed in other studies, [49,50] where such dynamical properties have been linked to an increase of the heat of formation (i.e., the alloys become less stable), suggesting a correlation between chemical instability

![](./images/812766265281085441_7.jpg)

FIG. 6. Evolution of the phonon dispersion, related linewidths, and PDOS for $K_{1-x}Ca_xH$ at (a) $x=0.05$, (b) $x=0.25$, and (c) $x=0.45$ within the ZPE scheme.

and phonon softening by doping. In order to corroborate such a statement, we calculated the cohesive energy ($E_{\text{coh}}$) for the three different systems within their respective range of dynamical stability. This quantity is used to characterize alloying stability, and is given by [51]
$$
E_{\text{coh}}=E_{MNH}^{\text{tot}}-(1-x)E_M^a-xE_N^a-E_{\text{H}}^a, \tag{5}
$$
where $E_{MNH}^{\text{tot}}$ is the total energy of the $M_{1-x}N_x\text{H}$ alloy at $x$ content, while $E_M^a$, $E_N^a$, and $E_{\text{H}}^a$ are the calculated total energies of an isolated atom $M=\text{Li}, \text{Na}, \text{K}$; atom $N=\text{Be}, \text{Mg}, \text{Ca}$; and hydrogen atom, respectively [52]. Results are collected in Table II. In general, for the three alloys, the doped systems are less stable than the pristine ones ($x=0$) (the larger the $E_{\text{coh}}$ absolute value, the more stable the system), but still in the range of stability (negative $E_{\text{coh}}$), as can be observed from Table II.

<table>
<caption>TABLE II. Calculated cohesive energy (eV) of the alkali-metal hydrides at $x=0$ and at its maximum $x$ content ($x_{\text{max}}$).</caption>
<thead>
<tr>
<th>System</th>
<th>$x=0$</th>
<th colspan="2">$x_{\text{max}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>LiH</td>
<td>$-7.30$</td>
<td>$-6.72$</td>
<td>($x=0.05$)</td>
</tr>
<tr>
<td>NaH</td>
<td>$-5.67$</td>
<td>$-4.09$</td>
<td>($x=0.20$)</td>
</tr>
<tr>
<td>KH</td>
<td>$-4.55$</td>
<td>$-0.77$</td>
<td>($x=0.45$)</td>
</tr>
</tbody>
</table>

![](./images/812766265281085441_8.jpg)

FIG. 7. Eliashberg spectral function $\alpha^2F(\omega)$ and e-ph coupling constant $\lambda(\omega)$ for $\text{Li}_{0.95}\text{Be}_{0.05}\text{H}$, calculated under the ZPE scheme.

### D. Electron-phonon and superconducting properties

In this section we analyze the e-ph coupling and superconducting properties of the alloys within the Eliashberg formalism. The Eliashberg spectral functions $\alpha^2F(\omega)$ and e-ph coupling parameters $\lambda(\omega)$, calculated by the partial integration of $\alpha^2F(\omega)$, for various $x$ contents are shown in Figs. 7, 8, and 9. For the (Na/Mg)H and (K/Ca)H alloys, with increasing alkaline-earth metal content ($x$), the Eliashberg function shifts to lower frequencies. Simultaneously, its total weight increases, in particular in the optical high-frequency region. Both changes enhance the e-ph coupling, and result in a large growth of the e-ph coupling parameter $\lambda(\omega)$ with $x$.

For the (Li/Be)H alloy, which has only a small stability range, we find medium coupling strength of $\lambda=0.473$ (ZPE scheme) for $\text{Li}_{0.95}\text{Be}_{0.05}\text{H}$. Both $\text{Na}_{1-x}\text{Mg}_x\text{H}$ and $\text{K}_{1-x}\text{Ca}_x\text{H}$ exhibit a remarkable increase in $\lambda$ with doping, shown in Figs. 10(a) and 11(a), respectively, which culminate in strong-coupling values as high as 1.26 for the (Na/Mg)H hydride, and even 1.69 for (K/Ca)H.

What are the important factors behind this increase in the coupling with doping? Essentially, the value of $\lambda$ is determined by three sources: the density of states at the Fermi level $N(E_F)$, the phonon frequencies $\omega$, and the e-ph coupling matrix elements [through the linewidths, see Eq. (4)]. In order to judge the importance of these factors, we performed additional evaluations of $\lambda(x)$ replacing the doping-dependent phonon spectrum with the one of the lowest concentration ($x=0.05$). This procedure keeps the phonon frequencies unchanged, ignoring its doping dependence, while it takes into account the changes of $N(E_F)$ and the e-ph matrix elements with doping [45]. These results are shown in Figs. 10 and 11 as $\lambda_\omega$, for (Na/Mg)H and (K/Ca)H hydrides, respectively. In both cases, $\lambda_\omega$ is strongly reduced with respect to $\lambda$ for the entire studied doping region. This clearly shows that the progressive phonon softening with doping (see Figs. 5 and 6) is a significant factor for the growth of $\lambda$. However, the other two sources do also play a role, as $\lambda_\omega$ still steadily increases as a function of $x$.

![](./images/812766265281085441_9.jpg)

FIG. 8. Evolution of Eliashberg function and $\lambda(\omega)$ for $\mathrm{Na}_{1-x} \mathrm{Mg}_{x} \mathrm{H}$ at (a) $x=0.05$, (b) $x=0.1$, and (c) $x=0.2$ (ZPE scheme).

![](./images/812766265281085441_10.jpg)

FIG. 9. Evolution of $\alpha^{2} F(\omega)$ and $\lambda(\omega)$ for the $\mathrm{K}_{1-x} \mathrm{Ca}_{x} \mathrm{H}$ alloy at (a) $x=0.05$, (b) $x=0.25$, and (c) $x=0.45$ within the ZPE scheme.

Next we analyze the contribution from the density of states (see Fig. 3), which increases on doping. To first approximation, $\lambda$ scales linearly with $N\left(E_{F}\right)$. We therefore plot the ratio $\lambda / N\left(E_{F}\right)$ in Figs. 10(b) and 11(b) for both $\lambda$ and $\lambda_{\omega}$. Only the ratio $\lambda_{\omega} / N\left(E_{F}\right)$ stays approximately constant as a function of $x$. These results taken together demonstrate that the doping dependence of both phonon softening and density of states are the decisive factors for the rise of $\lambda$. On contrast, the size of the e-ph matrix elements remains rather constant on doping.

Finally, the calculated Eliashberg functions $\alpha^{2} F(\omega)$ can be used to obtain estimates for the superconducting critical temperature $T_{c}$ as a function of doping. When numerically solving the isotropic Eliashberg gap equations, two different values of the Coulomb pseudopotential $\left(\mu^{*}\right)$ were employed: 0 and 0.1 (see Fig. 12). The reason to use $\mu^{*}=0$ is that it provides an upper limit for $T_{c}$, while $\mu^{*}=0.1$ is a typical value for many superconductors and gives a more realistic estimate for $T_{c}$. Results are shown for all three alloy systems and both schemes (static and ZPE) in Fig. 12. In general, $T_{c}$ shows a steady increase as a function of $x$, all the way up to the stability threshold. Values for the ZPE scheme are always larger than for the static scheme. This has its origin in the softer phonon spectra, which on the other hand is a consequence of the larger lattice constants found when the ZPE correction is included.

For each alloy system, the highest $T_{c}$ value is obtained close to the doping threshold. With $\mu^{*}=0.1$ we get $2.1 \mathrm{~K}$ for $\mathrm{Li}_{0.95} \mathrm{Be}_{0.05} \mathrm{H}, 28 \mathrm{~K}$ for $\mathrm{Na}_{0.8} \mathrm{Mg}_{0.2} \mathrm{H}$, and $49 \mathrm{~K}$ for $\mathrm{K}_{0.55} \mathrm{Ca}_{0.45} \mathrm{H}$. Although these values are far smaller than current $T_{c}$'s of other superconducting hydrides (up to $200 \mathrm{~K}$ ), the latter can only be reached by applying extremely high pressures (between 200 and $300 \mathrm{GPa}$ ). The present estimates of $T_{c}$ with values up to $50 \mathrm{~K}$ suggest that metalizing insulating hydrides by doping could be an attractive alternative route

![](./images/812766265281085441_11.jpg)

FIG. 10. (a) e-ph coupling parameters $\lambda$ and $\lambda_{\omega}$ (where the $x$-dependent phonon spectrum was replaced with the one from $x=0.05$), as a function of Mg-content ($x$) for the $\text{Na}_{1-x}\text{Mg}_x\text{H}$ alloy (ZPE scheme). (b) Ratio $\lambda/N(E_F)$ for the quantities shown in (a).

![](./images/812766265281085441_12.jpg)

FIG. 11. (a) e-ph coupling parameters $\lambda$ and $\lambda_{\omega}$ (obtained with a fixed phonon spectrum taken from $x=0.05$ instead of the $x$ dependent one), as a function of Ca-content ($x$) for the $\text{K}_{1-x}\text{Ca}_x\text{H}$ alloy (ZPE scheme). (b) Ratio $\lambda/N(E_F)$ for the quantities shown in (a).

![](./images/812766265281085441_13.jpg)

FIG. 12. Estimates for the superconducting critical temperature $T_c$ as a function of alkaline-earth metal content ($x$) calculated with $\mu^*=0$ (solid lines) and $\mu^*=0.1$ (dashed lines), respectively, for (a) $\text{Na}_{1-x}\text{Mg}_x\text{H}$ and (b) $\text{K}_{1-x}\text{Ca}_x\text{H}$. Results for both the ZPE (blue) and the static scheme (red) are shown for comparison. $T_c$ smaller than 0.1 K, with $\mu^*=0$, is obtained for $x(\text{Ca})<0.1$, and with $\mu^*=0.1$ for $x(\text{Mg})<0.1$ and $x(\text{Ca})<0.15$.

to achieve high-temperature superconductivity under easily accessible conditions.

## IV. SUMMARY

We performed a systematic study of the electronic, lattice dynamical, electron-phonon coupling, and superconducting properties of three alkali-metal hydrides, metalized through doping with earth-alkaline elements $\text{Li}_{1-x}\text{Be}_x\text{H}$, $\text{Na}_{1-x}\text{Mg}_x\text{H}$, and $\text{K}_{1-x}\text{Ca}_x\text{H}$, within density functional perturbation theory combined with the virtual-crystal approximation. Doping results in the creation of electron pockets at $X$ for ($\text{Li/Be}$)H and at $L$ for ($\text{Na/Mg}$)H and ($\text{K/Ca}$)H, and evokes a sizable e-ph coupling, which is carried largely by optical hydrogen modes along the $X$-$W$ high symmetry path at the BZ boundary due to scattering of electrons between different pockets. Simultaneously, the phonon spectrum softens and eventually the lattice becomes dynamically unstable, which correlates with the reduction of stability as the alloy content increases, as indicated by the cohesive energy. $\lambda$ exhibits a significant growth with doping, which can be attributed to both the softening of the phonons, mainly of the optical hydrogen vibrations, and

an increase of the electronic density of states at the Fermi level. The stability range and maximum achievable coupling increases significantly for the heavier alkaline elements. Maximum values for $\lambda$ are 0.47 for (Li/Be)H, 1.26 for (Na/Mg)H, and 1.69 for (K/Ca)H, which in turn results in $T_c$ estimates of 2.1, 28, and 49 K, respectively (for $\mu^* = 0.1$). This constitutes a clear tendency for enhanced superconducting properties with increasing mass of the alkaline metal. It will be the task of future work to reveal if this trend continues to the alloys (Rb/Sr)H and (Cs/Ba)H with even higher transition temperatures.

The prediction of such sizable transition temperatures under ambient pressure conditions indicates that metalization of metal hydrides by doping could be an alternative or even complementary route to high-temperature superconductivity, which is much easier to implement than application of high external pressure.

## ACKNOWLEDGMENTS
This research was partially supported by the Consejo Nacional de Ciencia y Tecnología (CONACyT, México) under Grant No. CB2013-221807-F; Vicerrectoría de Investigación (VIEP), Benemérita Universidad Autónoma de Puebla under Grant No. 100517450-VIEP2018, and the Karlsruher Institut für Technologie (KIT), Germany. The authors thankfully acknowledge computer resources, technical advise, and support provided by Laboratorio Nacional de Supercómputo del Sureste de México (LNS), a member of the CONACYT national laboratories.

[1] A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, *Nature (London)* **525**, 73 (2015).

[2] Y. Li, J. Hao, Y. Li, and Y. Ma, *J. Chem Phys.* **140**, 174712 (2014).

[3] N. W. Ashcroft, *Phys. Rev. Lett.* **21**, 1748 (1968).

[4] J. Feng, W. Grochala, T. Jaron, R. Hoffmann, A. Bergara, and N. W. Ashcroft, *Phys. Rev. Lett.* **96**, 017006 (2006).

[5] C. J. Pickard and R. J. Needs, *Phys. Rev. Lett.* **97**, 045504 (2006).

[6] M. Martinez-Canales, A. R. Oganov, Y. Ma, Y. Yan, A. O. Lyakhov, and A. Bergara, *Phys. Rev. Lett.* **102**, 087005 (2009).

[7] G. Gao, A. R. Oganov, A. Bergara, M. Martinez-Canales, T. Cui, T. Iitaka, Y. Ma, and G. Zou, *Phys. Rev. Lett.* **101**, 107002 (2008).

[8] Y. Wang and Y. Ma, *J. Chem. Phys.* **140**, 040901 (2014).

[9] M. I. Eremets, I. A. Trojan, S. A. Medvedev, J. S. Tse, and Y. Yao, *Science* **319**, 1506 (2008).

[10] X. Zhong, H. Wang, J. Zhang, H. Liu, S. Zhang, H.-F. Song, G. Yang, L. Zhang, and Y. Ma, *Phys. Rev. Lett.* **116**, 057002 (2016).

[11] D. V. Semenok, A. G. Kvashnin, I. A. Kruglov, and A. R. Oganov, *J. Phys. Chem. Lett.* **9**, 1920 (2018).

[12] D. C. Lonie, J. Hooper, B. Altintas, and E. Zurek, *Phys. Rev. B* **87**, 054107 (2013).

[13] Y. Ma, D. Duan, Z. Shao, H. Yu, H. Liu, F. Tian, X. Huang, D. Li, B. Liu, and T. Cui, *Phys. Rev. B* **96**, 144518 (2017).

[14] M. J. van Setten, V. A. Popa, G. A. de Wijs, and G. Brocks, *Phys. Rev. B* **75**, 035204 (2007).

[15] S. Lebègue, M. Alouani, B. Arnaud, and W. E. Pickett, *Europhys. Lett.* **63**, 562 (2003).

[16] J. Hooper, P. Baettig, and E. Zurek, *J. Appl. Phys.* **111**, 112611 (2012).

[17] T. Bi, N. Zarifi, T. Terpstra, and E. Zurek, arXiv:1809.00163.

[18] Y. Ge, F. Zhang, and Y. Yao, *Phys. Rev. B* **93**, 224513 (2016).

[19] J. Y. Zhang, L. J. Zhang, T. Cui, Y. L. Niu, Y. M. Ma, Z. He, and G. T. Zou, *J. Phys.: Condens. Matter* **19**, 425218 (2007).

[20] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).

[21] O. De la Peña-Seaman, R. de Coss, R. Heid, and K. P. Bohnen, *Phys. Rev. B* **79**, 134523 (2009), and references therein.

[22] P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, *Phys. Rev. B* **54**, 7231 (1991).

[23] S. Baroni S. de Gironcoli, and A. Dal Corso, *Rev. Mod. Phys.* **73**, 515 (2001).

[24] R. Heid and K.-P. Bohnen, *Phys. Rev. B* **60**, R3709(R) (1999).

[25] G. M. Eliashberg, *Sov. Phys. JETP* **11**, 696 (1969).

[26] S. G. Louie, K. M. Ho, and M. L. Cohen, *Phys. Rev. B* **19**, 1774 (1979).

[27] B. Meyer, F. Lechermann, C. Elsässer, and M. Fähnle, FORTRAN90 Program for Mixed-Basis Pseudopotential Calculations for Crystals, Max-Planck-Institut für Metallforschung, Stuttgart (unpublished).

[28] D. Vanderbilt, *Phys. Rev. B* **32**, 8412 (1985).

[29] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[30] C.-L. Fu and K. M. Ho, *Phys. Rev. B* **28**, 5480 (1983).

[31] M. Born and K. Huang, *Dynamical Theory of Crystal Lattices* (Clarendon/Geoffrey Cumberlege, Oxford, 1954).

[32] S. Baroni, P. Giannozzi, and E. Isaev, *Rev. Mineral. Geochem.* **71**, 39 (2010).

[33] P. B. Allen, *Phys. Rev. B* **6**, 2577 (1972).

[34] P. B. Allen and R. Silberglitt, *Phys. Rev. B* **9**, 4733 (1974).

[35] J. R. Schrieffer, *Theory of Superconductivity* (Benjamin, New York, 1964).

[36] J. P. Carbotte, *Rev. Mod. Phys.* **62**, 1027 (1990).

[37] V. Z. Kresin and S. A. Wolf, *Phys. Rev. B* **46**, 6458 (1992).

[38] S. Y. Savrasov, D. Y. Savrasov, and O. K. Andersen, *Phys. Rev. Lett.* **72**, 372 (1994).

[39] O. De la Peña-Seaman, R. de Coss, R. Heid, and K. P. Bohnen, *Phys. Rev. B* **82**, 224508 (2010).

[40] A. K. M. A. Islam, *Phys. Status Solidi B* **180**, 9 (1993).

[41] V. G. Kuznetsov and M. M. Shkrabkina, *Zh. Strukt. Khim.* **3**, 553 (1962).

[42] M. A. Olea-Amezcua, O. De la Peña-Seaman, J. F. Rivas Silva, R. Heid, and K. P. Bohnen, *J. Phys.: Condens. Matter* **29**, 145401 (2017).

[43] At $x=0.05$ we obtained $a_0=7.48390$ a.u and $a_0=7.6256$ a.u. for the static and ZPE schemes, respectively.

[44] Y. Kondo and K. Asaumi, *J. Phys. Soc. Jpn.* **57**, 367 (1988).

[45] O. De la Peña-Seaman, R. Heid, and K. P. Bohnen, *Phys. Rev. B* **86**, 184507 (2012).

[46] X. L. Zhang and W. M. Liu, *Sci. Rep.* **5**, 8964 (2015).

214504-8

[47] A. Shamp and E. Zurek, Nov. Supercond. Mater. **3**, 14 (2017).

[48] H. M. Syed, C. J. Webb, and E. MacA. Gray, *Prog. Solid State Chem.* **44**, 20 (2016).

[49] Y. Song, Z. X. Guo, and R. Yang, *Phys. Rev. B* **69**, 094205 (2004).

[50] X. Q. Zeng, L. F. Cheng, J. X. Zou, W. J. Ding, H. Y. Tian, and C. Buckley, *J. Appl. Phys.* **111**, 093720 (2012).

[51] W. Zhang, C. Chai, Q. Fan, K. Weng, and Y. Yang, *J. Mater. Sci.* **53**, 9611 (2018).

[52] The calculations of the single atoms (Li, Be, Na, Mg, K, Ca, and H) were done on a cube with sides of 10 Å long, using an $8 \times 8 \times 8k$-point mesh, and 30 Ry for the plane-waves energy cutoff. ZPE accounts for corrections of less than 0.1 eV on the cohesive energy.