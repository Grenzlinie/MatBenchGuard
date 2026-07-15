PHYSICAL REVIEW B 94, 174404 (2016)

# Oscillatory magnetic anisotropy and spin-reorientation induced by heavy-metal cap in $\mathrm{Cu/FeCo/M}$ ($M = \text{Hf}$ or Ta): A first-principles study

P. V. Ong, $^{1,*}$ Nicholas Kioussis, $^{1,\dagger}$ P. Khalili Amiri, $^{2,3}$ and K. L. Wang$^{2}$

$^{1}$Department of Physics and Astronomy, California State University Northridge, Northridge, California 91330, USA
$^{2}$Department of Electrical Engineering, University of California, Los Angeles, California 90095, USA
$^{3}$Inston Inc., Los Angeles, California 90095, USA

(Received 25 April 2016; published 3 November 2016)

Using $ab$ initio electronic structure calculations we have investigated the effect of the thickness of a heavy-metal (HM) cap on the magnetic anisotropy of the $\mathrm{Cu/FeCo/HM}(n)$ thin film where $\mathrm{HM} = \text{Hf}$ and Ta with thicknesses of $n = 0$–10 monolayers (MLs). We find that the Hf cap results in a large perpendicular magnetic anisotropy (PMA), which exhibits quasiperiodic oscillation with a period of two MLs. In contrast, the Ta-capped heterostructure exhibits a spin reorientation from out-of-plane to in-plane magnetization orientation at two MLs of Ta. Moreover, the MA remains negative and depends weakly on the Ta-cap thickness beyond the critical thickness. The underlying mechanism of the PMA oscillation is the periodic change in spin-flip spin-orbit coupling between the minority-spin Fe $d(xz,yz)$ and majority Fe $d(z^{2})$ at $\bar{\Gamma}$, which is induced by the hybridization with Hf at the FeCo/Hf interface. Our results help resolve the contradictory experiments regarding the role of the FeCo/Ta interface on the PMA of the MgO/FeCo/Ta junction. The calculations reveal that the ferromagnet/Hf is promising for spintronic applications and that the capping material and thickness are additional parameters for optimizing the functional properties of spintronic devices.

DOI: 10.1103/PhysRevB.94.174404

## I. INTRODUCTION

Perpendicular magnetic anisotropy (PMA) in trilayers of nonmagnetic metal/ferromagnet/heavy metal (NM/FM/HM) or insulator/ferromagnet/heavy metal (I/FM/HM) is of great interest for spintronic applications, such as spin-transfer-torque random access memory (RAM) [1,2], magnetoelectric RAM [3,4], and spin valves [5–9]. These perpendicularly magnetized heterostructures where the NM and I layers are usually Cu and MgO, respectively, and the HM layer (Ru, Pd, Hf, Ta, Pt, and Au) has strong spin-orbit coupling (SOC), promise a lower critical current for magnetization switching, faster magnetic switching, smaller magnetic bits, and high thermal stability [1,9,10]. Recently, it was shown that the material type and thickness of the HM layer play crucial roles not only on the MA [11–17], but also on the voltage control [18] and magnetotransport behavior [7,14,16,19,20] of these trilayers. In particular, experiments showed that the Hf overlayer enhances the PMA of $\mathrm{MgO/Co_{20}Fe_{60}B_{20}/Hf}$ and $\mathrm{MgO/Co_{40}Fe_{40}B_{20}/Hf}$ over that of $\mathrm{MgO/Co_{20}Fe_{60}B_{20}/W}$ [16] and $\mathrm{MgO/Co_{40}Fe_{40}B_{20}/Ta}$ [17], respectively. Similar results have also been predicted from $ab$ initio calculations on Fe/Hf and Fe/Ta superlattices where the thicknesses of each FM and HM layer is nine monolayers (MLs) [21].

On the other hand, experimental results on the effect of Ta on the MA of MgO/CoFeB remain controversial. Worledge et al. [22] showed that the magnetization orientation of $\mathrm{MgO/Co_{60}Fe_{20}B_{20}/Ru}$ remains in plane for FM thickness down to 0.5 nm whereas that of $\mathrm{MgO/Co_{60}Fe_{20}B_{20}/Ta}$ becomes perpendicular at around 0.9 nm, indicating that the CoFeB/Ta interface provides a PMA contribution. A similar conclusion also was drawn from experiments by Liu et al. [17] In contrast, Yamamoto et al. [13] showed that in $\mathrm{MgO\ (1-nm)/Co_{20}Fe_{60}B_{20}/cap}$ the MA decreases when the cap is successively replaced by 5-nm-thick MgO, Ta, and Ru, respectively. Moreover, these experiments reported that there is no PMA in $\mathrm{Ta/Co_{20}Fe_{60}B_{20}/Ta}$, indicating that the CoFeB/Ta interface yields a negative contribution to the MA. Furthermore, it has been shown that $\mathrm{MgO/Co_{60}Fe_{20}B_{20}/Ta}$ [14] and $\mathrm{MgO/Co_{20}Fe_{60}B_{20}/Ta}$ [23] with a 1.2-nm-thick FM layer exhibit in-plane magnetization orientation when the Ta thickness exceeds 0.45 and 2 nm, respectively.

Besides the Ta thickness, the annealing time and temperature which govern the diffusion of Ta across the interfaces have been shown to have a strong effect on the MA of the MgO/CoFeB/Ta junction [1,7,24,25]. Therefore, given the contradictory results and ill-defined structural characteristics of the I/FM and FM/HM interfaces, current experiments could not provide an unambiguous and consistent interpretation of the role of the FeCoB/Ta interface on the PMA of the magnetic junctions. Furthermore, it is well known that by varying the thickness of the FM thin film or the HM cap can induce shifts of spin-polarized quantum well states, resulting in strong variation of the MA [26] and even a switching of the magnetic easy axis of thin films [27]. This raises another interesting question when comparing the MA of the Hf- and Ta-capped systems, namely, whether the enhancement of the MA of the FM/Hf interface over that of the FM/Ta interface is specific to a certain thickness range of the HM cap, or is it generally true?

In this paper, we report $ab$ initio electronic structure calculations of the effect of the HM-cap thickness on the MA in $\mathrm{Cu/FeCo/HM}$ ($\mathrm{HM} = \text{Ta, Hf}$). Our results show distinct differences in the effect of Ta and Hf cappings on the MA of the trilayers and resolve the above questions. The underlying mechanism is elucidated by mapping the $k$-resolved MA and analyzing the energy and $k$-resolved distributions of the $d$

*phuongvu.ong@csun.edu
†nick.kioussis@csun.edu

2469-9950/2016/94(17)/174404(7) 174404-1 ©2016 American Physical Society

states of the minority- and majority-spin bands. The rest of this paper is organized as follows: Sec. II describes the methodology used to calculate the MA. In Sec. III A we consider the limit of zero-cap thickness, i.e., Cu/FeCo/vacuum and investigate the origin in the electronic structure of the PMA in the uncapped system. In Sec. III B, we demonstrate that the PMA of the Cu/FeCo/Hf trilayer oscillates with Hf thickness and elucidate the mechanism of the oscillatory behavior. In Sec. III C, we show that Ta capping induces a spin reorientation in Cu/FeCo/Ta and discuss the mechanism of the thickness-induced magnetic switching. Finally, conclusions are summarized in Sec. IV.

## II. COMPUTATIONAL METHODS AND MODELS

There are different approaches for calculating the MA in magnetic alloys. For example, one approach for calculating the MA and its thermal variation is based on the relativistic extension of the Korringa-Kohn-Rostoker multiple scattering theory within the coherent potential approximation (CPA) using the magnetic torque [28]. In this paper, the *ab initio* calculations have been carried out within the framework of the projector augmented-wave (PAW) formalism [29] as implemented in the Vienna *ab initio* simulation package [30,31]. It has been shown that MA values calculated from the supercell approach within the PAW methodology with SOC are in good agreement with those calculated within the CPA and other full potential methods and for Fe-Co alloys very well describe experimental data for tetragonally distorted thin films [32]. The generalized gradient approximation (GGA) [33] is employed to treat the exchange-correlation interaction. For $\mathrm{Fe}_{1-x} \mathrm{Co}_{x}$ alloys with $x \sim 0.5$, the MA values calculated at the levels of the local density approximation and GGA exhibit no significant difference [32]. Cu/FeCO/Hf(Ta) trilayers are modeled by a slab supercell approach along [001] consisting of four MLs of fcc Cu rotated by $45^{\circ}$ on the (001) plane, three MLs of $B2$-type FeCo, zero to ten MLs of Hf or Ta, and a $15$-Å-thick vacuum separating the periodic slabs (Fig. 1). In experiment, HM caps grow on the FM layer in an amorphous form [19,34]. In the present paper, we assume the Hf layer has a fcc or bcc structure. We denote with Fe1 and Fe2 the iron atoms at the Fe/Cu and Fe/Hf(Ta) interfaces, respectively. The in-plane lattice constant is fixed at the calculated value of the bulk FeCo lattice constant (2.840 Å). The magnetic and electronic degrees of freedom and atomic-$z$ positions are relaxed until the forces acting on the ions become less than $2 \times 10^{-3} \mathrm{eV} / \AA$ and the change in the total energy between two ionic relaxation steps is smaller than $10^{-6} \mathrm{eV}$. The plane-wave cutoff energy is $500 \mathrm{eV}$, and the Monkhorst-Pack $k$ mesh was $17 \times 17 \times 1$ for the relaxations. SOC of the valence electrons is then included using the second-variation method [35] employing the scalar-relativistic eigenfunctions of the valence states and a $41 \times 41 \times 1 k$-point mesh. The MA per unit interfacial area $A$ is determined from $\mathrm{MA}=\left[E_{[100]}-E_{[001]}\right] / A$, where $E_{[100]}$ and $E_{[001]}$ are the total energies with magnetization along the [100] and [001] directions, respectively. Test calculations with $51 \times 51 \times 1 k$ mesh indicate that the calculated MA values are converged within $10 \%$. For comparison, we also employ the force theorem [36] to calculate the $\mathrm{MA} \approx \sum_{\mathbf{k}} \mathrm{MA}(\mathbf{k}) / A$, where the $k$-resolved $\mathrm{MA} \mathrm{MA}(\mathbf{k})=\sum_{n \in o c c}\left[\varepsilon(n, \mathbf{k})^{[100]}-\varepsilon(n, \mathbf{k})^{[001]}\right]$ with the band index $n$ runs over all occupied (occ) states. Here, the sum with respect to $\mathbf{k}$ is taken over the two-dimensional Brillouin zone (2D BZ), and $\varepsilon(n, \mathbf{k})^{[100]([001])}$ are the eigenvalues of the Hamiltonian for magnetization along the [100] ([001]) directions, respectively.

![](./images/811117963804409857_1.jpg)

FIG. 1. (a) Schematic of the Cu/FeCo/HM($n$) trilayer, where $\text{HM} = \text{Hf}$ or $\text{Ta}$ and $n=0$--10 MLs. (b) Tetragonal pyramidal structure at the FeCo/HM interface.

## III. RESULTS AND DISCUSSION

### A. Perpendicular magnetic anisotropy of Cu/FeCo/vacuum

Figures 2(a) and 2(b) show $\mathrm{MA}(\mathbf{k})$ in the 2D BZ and along $\overline{\Gamma M}$, respectively. We also show in Figs. 2(c) and 2(d) the

![](./images/811117963804409857_2.jpg)

FIG. 2. Cu/FeCo/vacuum: (a) and (b) $\mathrm{MA}(\mathbf{k})$ (in meV) in the 2D BZ and along $\overline{\Gamma M}$, respectively. In (a), I and II indicate the BZ $\mathbf{k}_{\|}$ points where there are large positive contributions to MA. (c) and (d) Energy- and $k$-resolved distributions of the orbital character of minority-spin ($\downarrow$) bands along $\overline{\Gamma M}$ for the Fe1- and Fe2-derived $d_{x y}$ and $d_{x^{2}-y^{2}}$ states, respectively.


![](./images/811117963804409857_3.jpg)

FIG. 3. (a) Cap-thickness dependence of MA of Cu/FeCo/Hf, calculated using the total energy difference (circles) and the force theorem (triangles). The stars indicate MA of MgO/FeCo/Hf($n$) for $n=0$ and three MLs. (b) Cap-thickness dependence of the orbital moment difference $\Delta m_{o}=m_{o}^{[001]}-m_{o}^{[100]}$ of the Fe1 and Fe2 interfacial atoms. (c) MA($\mathbf{k}$) contours (in meV) in the 2D BZ for Hf thickness $n_{\text{Hf}}=1$--4. For the sake of clarity, MA($\mathbf{k}$) is magnified by factors of 6 and 2 for $n_{\text{Hf}}=1$ and 2, respectively.

energy- and $k$-resolved distributions of the minority-spin ($\downarrow$) Fe1 and Fe2 $d$ states, respectively, along $\overline{\Gamma M}$.

The main PMA contributions occur at BZ points I and II [(BZP-I) and (BZP-II), respectively] along $\overline{\Gamma M}$ [Figs. 2(a) and 2(b)]. Within second-order perturbation theory the MA can be expressed as [37]

$$
\begin{aligned}
M C A \propto & \xi^{2} \sum_{\mathbf{k}} \sum_{o, u} \frac{\left|\left\langle\Psi_{\mathbf{k} o}^{\downarrow}\left|\hat{L}_{z}\right| \Psi_{\mathbf{k} u}^{\downarrow}\right\rangle\right|^{2}-\left|\left\langle\Psi_{\mathbf{k} o}^{\downarrow}\left|\hat{L}_{x}\right| \Psi_{\mathbf{k} u}^{\downarrow}\right\rangle\right|^{2}}{E_{\mathbf{k} u}^{\downarrow}-E_{\mathbf{k} o}^{\downarrow}}, \\
& +\xi^{2} \sum_{\mathbf{k}} \sum_{o, u} \frac{\left|\left\langle\Psi_{\mathbf{k} o}^{\uparrow}\left|\hat{L}_{x}\right| \Psi_{\mathbf{k} u}^{\downarrow}\right\rangle\right|^{2}-\left|\left\langle\Psi_{\mathbf{k} o}^{\uparrow}\left|\hat{L}_{z}\right| \Psi_{\mathbf{k} u}^{\downarrow}\right\rangle\right|^{2}}{E_{\mathbf{k} u}^{\downarrow}-E_{\mathbf{k} o}^{\uparrow}} .
\end{aligned}
$$

(1)

Here, $\Psi_{\mathbf{k} o}^{\downarrow}$ ($E_{\mathbf{k} o}^{\downarrow}$), $\Psi_{\mathbf{k} o}^{\uparrow}$ ($E_{\mathbf{k} o}^{\uparrow}$), and $\Psi_{\mathbf{k} u}^{\downarrow}$ ($E_{\mathbf{k} u}^{\downarrow}$) are occupied minority-, occupied majority-, and unoccupied minority-spin states (energies); $\xi$ is the SOC constant, and $\hat{L}_{x(z)}$ is the $x(z)$ component of the orbital angular momentum operator. Note that the contribution from the spin-flip SOC term has an opposite sign from the SOC term between states of the same spin.

The origin of the positive MA at BZP-I and BZP-II is mainly due to the SOC of the occupied Fe1 $\downarrow d(x^{2}-y^{2})$ state to the unoccupied $d(xy)$ states and that of the occupied Fe1 $\downarrow d(xy)$ to the unoccupied $d(x^{2}-y^{2})$ states, respectively, through $\hat{L}_{z}$ [Fig. 2(c)]. At BZP-I, there is also SOC of the occupied Fe2 $\downarrow d(x^{2}-y^{2})$ states to the unoccupied $d(xy)$ states, giving positive MA contributions. The separation in energy between the occupied and the unoccupied Fe2 $\downarrow d$ states is large and out of the energy window at BZP-II [Fig. 2(d)]. Consequently, the MA contribution of the Fe2 atom at this $k$ point is not significant.

### B. Oscillatory magnetic anisotropy in Cu/FeCo/Hf($n$)

Figure 3(a) shows the variation of MA with Hf-cap thickness ($n_{\text{Hf}}$) in the Cu/FeCo/Hf trilayer. The MAs determined from: (i) total energy calculations (circles) and (ii) the force theorem (triangles) are in excellent agreement. For comparison, we also display the MA values of MgO/FeCo/vacuum and MgO/FeCo/Hf(3). The first Hf ML induces a large decrease in MA from $1.49\ \text{erg/cm}^2$ for the Cu/FeCo/vacuum to $0.62\ \text{erg/cm}^2$ for Cu/FeCo/Hf(1). For thin films, the contribution of the shape anisotropy can be estimated by $M A_{\text{shape}}/t=-(\mu_{0}/2)M_{S}^{2}$ (SI units) [38,39], where $t$ is the thickness of the FeCo layer and $\mu_{0}=4\pi\times10^{-7}\ \text{N A}^{-2}$. The saturation magnetization is estimated by $M_{S}=M/V$, where $M=M_{\text{Fe}}+M_{\text{Co}}$ and $V$ are the total magnetic moment and volume of the unit cell of the $B2$-type FeCo, respectively. Using $V\sim23\ \mathring{\text{A}}^{3}$, $M_{\text{Fe}}\sim2.7\mu_{B}$, and $M_{\text{Co}}\sim1.7\mu_{B}$, we find $M_{S}=1774\times10^{3}\ \text{A m}^{-1}$, which is in good agreement with the experimental value of $1950\times10^{3}\ \text{A m}^{-1}$ [40]. Thus, the contribution of the $M A_{\text{shape}}$ of about $-0.6\ \text{erg/cm}^2$ is smaller than the MA values for the range of Hf thickness considered in this paper.

Except for $n_{\text{Hf}}=1$ ML, the MA values are larger for odd numbers of Hf layers, resulting in a quasiperiodic oscillation period of two MLs, which shows no sign of damping up to

![](./images/811117963804409857_4.jpg)

FIG. 4. DOS of minority-spin ($\downarrow$) Fe2-derived $d(xz,yz)$ (left panel) and $d(z^{2})$ (right panel) states. Numerals in the left panel indicate Hf thickness $n_{\text{Hf}}=0$--10 MLs. The Fermi level is set at zero energy. The arrows indicate enhancement of $d(xz,yz)$ and $d(z^{2})$ DOS which occur periodically near the Fermi level for odd and even $n_{\text{Hf}}$'s, respectively.

ten-ML Hf. The MA(k) in the 2D BZ is plotted for $n_{\text{Hf}}=$ 1--4 MLs [Fig. 3(c)]. One can clearly see that the enhancement in MA originates from the hot spot at $\overline{\Gamma}$, which appears periodically for odd values of $n_{\text{Hf}}$.

We have also calculated the effect of cap thickness on the orbital moment difference $\Delta m_{o}=m_{o}^{[001]}-m_{o}^{[100]}$. The results for the interfacial Fe1 and Fe2 atoms are shown in Fig. 3(b). For the Co and Hf atoms the variation of $\Delta m_{o}$ is much weaker and is not shown. Interestingly, the thickness dependence of $\Delta m_{o}$ for Fe1 and Fe2 correlates very well with that of MA and oscillates with the same period of two MLs. Note that $\Delta m_{o}$ is positive and negative for Fe1 and Fe2, respectively. For single atomic species FM with large exchange splitting where the spin-flip SOC between states of opposite spins vanishes, Bruno has shown that the MA is proportional to $\Delta m_{o}$ [41]. However, for the Cu/FeCo/Hf trilayer the spin-flip term cannot be ignored due to hybridization of Fe2 with the nonmagnetic HM cap. Therefore, the fact that $\Delta m_{o}$ is negative for Fe2 does not necessarily imply an in-plane magnetic orientation at the FeCo/Hf interface. On the contrary, we show below the FeCo/Hf interface provides a large contribution to PMA due to the spin-flip SOC induced by hybridization of Fe2 and Hf orbitals.

Figure 4 shows the evolution of density of states (DOS) of the minority-spin Fe2-derived $d(xz,yz)$ and $d(z^{2})$ states with Hf thickness. The data clearly show that the $d(xz,yz)$ DOS around the Fermi level is periodically enhanced for odd values of $n_{\text{Hf}}$, except for $n_{\text{Hf}}=1$ ML (left panel in Fig. 4). On the other hand, the unoccupied $d(z^{2})$ DOS is increased for even $n_{\text{Hf}}$ [right panel in Fig. 4]. This periodic behavior is consistent with the MA oscillation discussed above. The unoccupied Fe2($\downarrow$)$d(z^{2})$ and occupied $d(xz,yz)$ are coupled through the $\hat{L}_{x}$ operator. Therefore, the increase in the unoccupied $d(z^{2})$ DOS leads to a decrease in the negative MA term, giving rise to a trough in the MA variation for even $n_{\text{Hf}}$.

![](./images/811117963804409857_5.jpg)

FIG. 5. DOS of majority-spin ($\uparrow$) Fe2-derived $d(z^{2})$ states (left panel) and Hf1-derived hybridized $d^{2}p^{3}=d(xy)+d(z^{2})+p(x)+$ $p(y)+p(z)$ states, averaged over the number of the component orbitals (right panel). Numerals in the right panel indicate Hf thickness $n_{\text{Hf}}=0$--10 MLs. The Fermi level is set at zero energy. The arrows indicate enhanced DOS of the $d(z^{2})$ or hybridized $d^{2}p^{3}$ states that occur periodically near the Fermi level for odd $n_{\text{Hf}}$. For the sake of clarity, the $d^{2}p^{3}$ DOS is magnified by a factor of 2.

Figure 5 shows the evolution of the DOS of majority-spin Fe2-derived $d(z^{2})$ and Hf1-derived hybridized $d^{2}p^{3}=$ $d(xy)+d(z^{2})+p(x)+p(y)+p(z)$ states, averaged over the number of the component orbitals. Since the FeCo/Hf interface has a tetragonal pyramidal structure [Fig. 1(b)], the Hf1- derived hybrid $d^{2}p^{3}$ state is allowed [42]. The consistency in behavior and peak positions of Fe2 $\uparrow d(z^{2})$ and Hf1 $\uparrow d^{2}p^{3}$ clearly indicates that there is a strong hybridization between the two orbitals. Note that the DOS of Fe2 $\uparrow d(z^{2})$ is enhanced near the Fermi level for odd $n_{\text{Hf}}$, in contrast to that of Fe2 $\uparrow d(z^{2})$, which increases for even Hf thickness. The calculated energy- and $k$-resolved distributions of the orbital characters of majority-spin states shows that the Fe2 $\uparrow d(z^{2})$ states occur exclusively around the $\overline{\Gamma}$ point. The spin-flip SOC between Fe2 $\uparrow d_{z^{2}}$ and Fe2 $\downarrow d_{xz,yz}$ through the $\hat{L}_{x}$ operator, leads to an enhancement in the positive MA contribution. This gives rise to the MA hot spot in MA(k) contours at the $\overline{\Gamma}$ point and explains the peak in MA variation for odd $n_{\text{Hf}}$ [Fig. 3(c)].

### C. Cap-thickness-induced spin reorientation in Cu/FeCo/Ta($n$)

Figure 6(a) shows the variation of MA with Ta-cap thickness ($n_{\text{Ta}}$) in the Cu/FeCo/Ta trilayer. The MA values calculated using the total energy method and the force theorem are in excellent agreement. In contrast to the oscillatory behavior in the Hf-capped system, the MA of Cu/FeCo/Ta($n$) abruptly drops to a negative value at $n_{\text{Ta}}=2$ MLs, leading to a switching of magnetization vector from out-of-plane to in-plane orientation. Using the same method as in Sec. III B, the contribution of the shape anisotropy is calculated to be about $-0.6$ erg/cm$^{2}$, whose absolute value is significantly

![](./images/811117963804409857_6.jpg)

FIG. 6. The same as Fig. 3 but for a Ta cap. In the MA(k) contours for $n_{\text{Ta}}=2$ and 4, points I and II indicate the BZP where there are large negative contributions to MA.

smaller than the MA at $n_{\text{Ta}}=1$ ($1.0\ \text{erg/cm}^2$). Consequently, the spin reorientation still persists. For the one-ML-thick Ta cap the MA increases sharply but remains thereafter negative and exhibits only weak dependence on Ta-cap thickness. For comparison, the MA values of MgO/FeCo/vacuum and MgO/FeCo/Ta(3) also are presented. More specifically, the MA decreases from $2.70\ \text{erg/cm}^2$ for MgO/FeCo/vacuum to $1.43\ \text{erg/cm}^2$ for MgO/FeCo/Ta(3). Note that the MA values of the MgO-supported systems are consistently larger than those of the Cu-supported one. This indicates that MgO/FeCo induces PMA, whereas FeCo/Ta favors in-plane MA. Figure 6(b) shows the orbital moment difference $\Delta m_o$ for the Fe1 and Fe2 atoms versus the thickness of the Ta cap, which correlates well with that of the MA. $\Delta m_o$ rapidly decreases at one and two MLs for Fe1 or Fe2, respectively, and thereafter increases and becomes weakly dependent on $n_{\text{Ta}}$. The MA(k) in the 2D BZ is plotted for $n_{\text{Ta}}=1$--4 MLs [Fig. 6(c)]. In contrast to the MA hot spots found for odd MLs for the Hf cap, we find that the MA vanishes at $\bar{\Gamma}$ for all Ta thicknesses considered in this paper.

The electronic configurations of Hf $(5d^2)$ and Ta $(5d^3)$ differ by one electron. Addition or removal of an electron from the system will lead to an increase or decrease in the Fermi level, respectively. Within the rigid band model, the Fermi-level shift leads to the extinction of certain SOC matrix elements and/or the establishment of new ones. Since the MA energy is determined mainly from spin-orbit-coupled pairs of occupied and unoccupied bands in the vicinity of the Fermi level, these shifts can result in a dramatic change in the MA. Therefore, the distinct behavior of the Hf- and Ta-capped systems can be understood in terms of the band filling effect.

In order to elucidate the underlying mechanisms of the spin-reorientation and in-plane (negative) MAs of the Ta-capped system we have calculated the energy- and $k$-resolved distributions of the orbital characters of minority- and majority-spin bands for the Fe1 and Fe2 interfacial atoms for $n_{\text{Ta}}=1$ which are shown in Fig. 7. The unoccupied Fe2 $\uparrow\ d(z^2)$ states still occur near the Fermi level at $\bar{\Gamma}$, and they couple to the occupied Fe2 $\downarrow\ d(xz,yz)$ states via spin-flip SOC of $\hat{L}_x$ yielding a positive MA contribution. However, this is counterbalanced by the same-spin SOC between the occupied Fe2 $\downarrow\ d(xz,yz)$

![](./images/811117963804409857_7.jpg)

FIG. 7. Energy- and $k$-resolved distributions of orbital character of minority-spin ($\downarrow$) (left panel) and majority-spin ($\uparrow$) bands (right panel), respectively, along $k\parallel\overline{\Gamma X}$ for the interfacial Fe2 atom $d$ states for $n_{\text{Ta}}=1$.

![](./images/811117963804409857_8.jpg)

FIG. 8. Left panel: energy levels of Fe1-derived minority-spin $(\downarrow)$ states at BZPs I and II for $n_{\text{Ta}}=4$. Middle and right panels: energy levels of Fe1- and Fe2-derived minority-spin $(\downarrow)$ states, respectively, at BZP I for $n_{\text{Ta}}=4$. The vertical lines connecting pairs of occupied and unoccupied states denote nonvanishing SOC matrix elements where the line color matches that of the occupied state.

and the unoccupied Fe2 $\downarrow d(xy)$ states and $d(x^2-y^2)$ through $\hat{L}_x$, which yields a negative MA contribution. We find a similar behavior for the thicker Ta cap. The mutual cancellation of MA contributions from the spin-flip and same-spin SOCs is responsible for the disappearance of the hot spots at $\bar{\Gamma}$ in MA(k) for the Ta-cap trilayers [Fig. 6(c)].

Figure 8 shows the energy levels of the Fe1-derived minority-spin states at the BZP-I and BZP-II for $n_{\text{Ta}}=2$ (left panel) and those of Fe1- and Fe2-derived minority-spin states at the BZP-I for $n_{\text{Ta}}=4$ (middle and right panels). The associated nonvanishing SOC matrix elements are represented by vertical lines connecting pairs of occupied and unoccupied states. Because the MA of the Cu/FeCo/Ta system is negative for $n_{\text{Ta}}=2$ and 4 MLs, we only focus on the BZP where MA(k) $<0$ [Fig. 6(c)]. For $n_{\text{Ta}}=2$, the SOC of the occupied Fe1 $\downarrow d(xz)$ states with the unoccupied Fe1 $\downarrow d(z^2)$ states at point I and that of the occupied Fe1 $\downarrow d(yz)$ states with the unoccupied Fe1 $\downarrow d(z^2)$ states at II through $\hat{L}_x$ gives rise to the negative MA(k) at BPZ-I and BPZ-II, respectively [left panel in Fig. 8]. For $n_{\text{Ta}}=4$, the occupied Fe1 $\downarrow d(x^2-y^2)$ states (middle panel in Fig. 8) is coupled to the unoccupied Fe1 $\downarrow d(xz)$ states and $d(yz)$ through $\hat{L}_x$ and to the unoccupied Fe1 $\downarrow d(xy)$ states through $\hat{L}_z$. For the Fe2 site the occupied Fe2 $\downarrow d(yz)$ states at point I is coupled to the unoccupied Fe2 $\downarrow d(xy)$, $d(x^2-y^2)$, and $d(z^2)$ states through $\hat{L}_x$ and to the unoccupied Fe2 $\downarrow d(xz)$ states through $\hat{L}_z$. The competition between the negative and the positive MA contributions due to these SOCs through $\hat{L}_x$ and $\hat{L}_z$, respectively, renders MA(k) $<0$ at the BZP-I [right panel in Fig. 8].

## IV. CONCLUSION

To summarize, using electronic structure calculations we have studied the effects of the HM cap on the MA of a Cu/FeCo/HM($n$) thin film where HM = Hf and Ta with thicknesses $n=0$–10 MLs. We showed that the Hf cap induces large PMA, which exhibits quasiperiodic oscillation with cap thickness. The oscillation has a period of two MLs and shows no sign of damping up to ten MLs of cap thickness. The underlying mechanism of the oscillatory behavior is the periodic change in the spin-flip SOC at $\bar{\Gamma}$ between the minority-spin Fe $d(xz,yz)$ and majority-spin Fe $d(z^2)$ states, which is induced by the hybridization with Hf at the FeCo/Hf interface. On the contrary, the Ta cap induces a spin reorientation from the perpendicular to the in-plane direction at a Ta thickness of two MLs. Moreover, the MA remains negative and exhibits weak thickness dependence for the thicker Ta cap. We showed that the effect of spin-flip SOC is suppressed in the Cu/FeCo/Ta trilayers due to the mutual cancellation of MA contributions from the same-spin SOC at $\bar{\Gamma}$. The results unambiguously indicate that the FeCo/Ta interface favors in-plane MA and helps resolve the contradictory experimental results regarding the roles of the FeCo/Ta and FeCo/MgO interfaces on the PMA of the MgO/FeCo/Ta junctions. Furthermore, our results imply that magnetic multilayers employing the Hf cap have large PMA and hence would be promising for spintronic applications.

## ACKNOWLEDGMENTS

This research was supported by NSF Grant No. 1160504, ERC Translational Applications of Nanoscale Multiferroic Systems (TANMS), by Inston Inc. and by NSF Grant No. DMR-1532249.

[1] S. Ikeda *et al.*, *Nature Mater.* **9**, 721 (2010).

[2] W.-G. Wang, M. Li, S. Hageman, and C. L. Chien, *Nature Mater.* **11**, 64 (2012).

[3] T. Maruyama *et al.*, *Nat. Nanotechnol.* **4**, 158 (2009).

[4] Y. Shiota *et al.*, *Nature Mater.* **11**, 39 (2012).

[5] S. M. Mohseni, R. K. Dumas, Y. Fang, J. W. Lau, S. R. Sani, J. Persson, and J. Åkerman, *Phys. Rev. B* **84**, 174432 (2011).

[6] J. R. Childress, M. J. Carey, M.-C. Cyrille, K. Carey, N. Smith, J. A. Katine, T. D. Boone, A. A. G. Driskill-Smith, S. Maat, K. Mackay, and C. H. Tsang, *IEEE Trans. Magn.* **42**, 2444 (2006).

[7] S. Ikeda, J. Hayakawa, Y. Ashizawa, Y. M. Lee, K. Miura, H. Hasegawa, M. Tsunoda, F. Matsukura, and H. Ohno, *Appl. Phys. Lett.* **93**, 082508 (2008).

[8] H. Kanai, J. Kane, K. Yamada, K. Aoshima, M. Kanamine, J. Toda, and Y. Mizoshita, *IEEE Trans. Magn.* **33**, 2872 (1997).

[9] S. Mangin, D. Ravelosona, J. A. Katine, M. J. Carey, B. D. Terris, and E. E. Fullerton, *Nature Mater.* **5**, 210 (2006).

[10] S. Mangin, Y. Henry, D. Ravelosona, J. A. Katine, and E. E. Fullerton, *Appl. Phys. Lett.* **94**, 012502 (2009).

[11] D.-Y. Lee, T.-H. Shim, and J.-G. Park, *Appl. Phys. Lett.* **102**, 212409 (2013).

[12] J. Sinha, M. Hayashi, A. J. Kellock, S. Fukami, M. Yamanouchi, H. Sato, S. Ikeda, S. Mitani, S.-h. Yang, S. S. P. Parkin, and H. Ohno, Appl. Phys. Lett. 102, 242405 (2013).

[13] H. Yamamoto, J. Hayakawa, K. Miura, K. Ito, H. Matsuoka, S. Ikeda, and H. Ohno, Appl. Phys. Express 5, 053002 (2012).

[14] L. Cuchet, B. Rodmacq, S. Auffret, R. C. Sousa, C. Ducruet, and B. Dieny, Appl. Phys. Lett. 103, 052402 (2013).

[15] M. P. R. Sabino, S. T. Lim, and M. Tran, Appl. Phys. Express 7, 093002 (2014).

[16] C.-F. Pai, M.-H. Nguyen, C. Belvin, L. H. Vilela-Leão, D. C. Ralph, and R. A. Buhrman, Appl. Phys. Lett. 104, 082407 (2014).

[17] T. Liu, J. W. Cai, and Li Sun, AIP Adv. 2, 032151 (2012).

[18] Y. Shiota, F. Bonell, S. Miwa, N. Mizuochi, T. Shinjo, and Y. Suzuki, Appl. Phys. Lett. 103, 082410 (2013).

[19] S. V. Karthik, Y. K. Takahashi, T. Ohkubo, K. Hono, H. D. Gan, S. Ikeda, and H. Ohno, J. Appl. Phys. 111, 083922 (2012).

[20] P. W. T. Pong and W. F. Egelhoff, J. Appl. Phys. 105, 07C915 (2009).

[21] Y. Miura, M. Tsujikawa, and M. Shirai, J. Appl. Phys. 113, 233908 (2013).

[22] D. C. Worledge, G. Hu, D. W. Abraham, J. Z. Sun, P. L. Trouilloud, J. Nowak, S. Brown, M. C. Gaidis, E. J. O'Sullivan, and R. P. Robertazzi, Appl. Phys. Lett. 98, 022501 (2011).

[23] C.-W. Cheng, W. Feng, G. Chern, C. M. Lee, and T.-h. Wu, J. Appl. Phys. 110, 033916 (2011).

[24] N. Miyakawa, D. C. Worledge, and K. Kita, IEEE Magn. Lett. 4, 1000104 (2013).

[25] W.-G. Wang, S. Hageman, M. Li, S. Huang, X. Kou, X. Fan, J. Q. Xiao, and C. L. Chien, Appl. Phys. Lett. 99, 102502 (2011).

[26] M. Przybylski, M. Dąbrowski, U. Bauer, M. Cinal, and J. Kirschner, J. Appl. Phys. 111, 07C102 (2012).

[27] P. V. Ong, N. Kioussis, P. Khalili Amiri, J. G. Alzate, K. L. Wang, G. P. Carman, J. Hu, and R. Wu, Phys. Rev. B 89, 094422 (2014).

[28] J. B. Staunton, L. Szunyogh, A. Buruzs, B. L. Gyorffy, S. Ostanin, and L. Udvardi, Phys. Rev. B 74, 144411 (2006).

[29] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

[30] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[31] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

[32] S. Steiner, S. Khmelevskyi, M. Marsmann, and G. Kresse, Phys. Rev. B 93, 224425 (2016).

[33] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B 46, 6671 (1992).

[34] T. Miyajima, T. Ibusuki, S. Umehara, M. Sato, S. Eguchi, M. Tsukada, and Y. Kataoka, Appl. Phys. Lett. 94, 122501 (2009).

[35] D. D. Koelling and B. N. Harmon, J. Phys. C 10, 3107 (1977).

[36] M. Weinert, R. E. Watson, and J. W. Davenport, Phys. Rev. B 32, 2115 (1985).

[37] D.-S Wang, R. Wu, and A. J. Freeman, Phys. Rev. B 47, 14932 (1993).

[38] P. Bruno, Proceedings of the 24th Ferienkurse des Forschungszentrums, Jülich, Jülich, 1993, edited by P. H. Dederichs, P. Grünberg, and W. Zinn (Forschungszentrum, Jülich, 1993).

[39] The shape anisotropy is caused by the demagnetization field, which is a macroscopic concept and determined only for continuum. Consequently, the shape anisotropy is not strictly valid or fails for an ultrathin film whose thickness is several atomic layers. Therefore, this is only a rough estimation of the contribution of the shape anisotropy to the trilayer.

[40] L. Sun, Y. Hao, C. L. Chien, and P. C. Searson, IBM J. Res. Dev 49, 79 (2005).

[41] C. Andersson, B. Sanyal, O. Eriksson, L. Nordström, O. Karis, D. Arvanitis, T. Konishi, E. Holub-Krappe, and J. H. Dunn, Phys. Rev. Lett. 99, 177207 (2007).

[42] M. Calvin and C. H. Barkelew, J. Am. Chem. Soc. 68, 2267 (1946).