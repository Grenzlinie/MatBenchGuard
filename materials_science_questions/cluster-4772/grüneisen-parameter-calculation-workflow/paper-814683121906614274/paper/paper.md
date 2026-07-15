# Mechanism of negative thermal expansion in $LaC_2$ from first-principles prediction

Yaming Liu $^{a,b}$, Yu Jia $^{a,*}$, Qiang Sun $^{a}$, Erjun Liang $^{a}$

$^{a}$ International Joint Research Laboratory for Quantum Functional Materials of Henan, and School of Physics and Engineering, Zhengzhou University, Zhengzhou 450001, China
$^{b}$ Henan Institute of Science and Technology, Xinxiang 453003, China

---

## ARTICLE INFO
**Article history:**
Received 12 September 2014
Received in revised form 27 October 2014
Accepted 30 October 2014
Available online 6 November 2014

Communicated by R. Wu

**Keywords:**
Negative thermal expansion (NTE)
$LaC_2$
Phonon
Grüneisen parameter

## ABSTRACT
Based on density functional theory and quasiharmonic approximation, the coefficients of thermal expansion (CTE) and negative thermal expansion (NTE) mechanism of tetragonal $LaC_2$ are studied. Numerical results show that there is an obvious NTE parallel to c-axis, and the CTE is approximately $\alpha_c = -1.67 \times 10^{-6}\ \text{K}^{-1}$, which coincides with the experimental data $-1.0 \times 10^{-6}\ \text{K}^{-1}$. In particular, a tiny NTE phenomenon along a-axis below 10 K has been predicted. The vibrational modes $E_{\text{u}}$ and $E_{\text{g}}$ at $\Gamma(0,0,0)$, and other three modes at $M(0.5,0.5,0)$ and $Z(0,0,0.5)$, give rise to negative Grüneisen parameters and therefore contribute to the NTE along a- and c-axis. Additionally, the bulk CTE was calculated to be positive, our CTE values and temperature intervals agree well with the presented experiments.

© 2014 Elsevier B.V. All rights reserved.

---

## 1. Introduction
The unusual phenomenon of negative thermal expansion (NTE), that materials expand with cooling and contract upon heating, has been studied actively after the discovery of $ZrW_2O_8$ in 1996 [1]. From the application point of view, NTE materials can be used to fabricate composites with precisely tailored CTE, even exhibiting an overall CTE nearly zero [2], which are useful in precision optics, thermo-mechanical actuators and space applications. The isotropic NTE in $ZrW_2O_8$, expanding isotropically in volume on cooling, is considered as the rotation [3] and translation [4] of polyhedrons induced by low-energy rigid unit modes (RUMs), which lead to a reduction of the total void volume. In addition to the well-known $ZrW_2O_8$ family, NTE behavior and mechanisms have also been reported in other compounds, such as structural phase transitions in ferroelectric $PbTiO_3$ [5,6], magnetostrictive effects in antiperovskite manganese nitride [7,8] and electronic phase transitions in perovskite $BiNiO_3$ [9,10]. Among the present NTE materials, almost all of them are either insulator or semiconductor, and the NTE behavior is rarely found in metallic materials, which seriously restrict the applications of NTE compounds in electrical and thermodynamic fields.

Recently, Babizhetskyy et al. [11] have synthesized and investigated the polycrystalline samples of lanthanum dicarbides ($LaC_2$). The magnetic susceptibility measurements and heat capacity data show these tetragonal transition-metal carbides to be a BCS-type superconductor below $\sim$1.8 K. Moreover, a negative thermal expansion phenomenon along c-axis was observed in the temperature range $T < \sim$50 K, and it shows metallic character in this temperature range. Focusing on the superconducting property, the origin of NTE wasn't discussed in this work.

Due to the excellent mechanical properties and as a candidate for searching for high transition temperature ($T_c$) superconductors [12,13], too many works about lanthanum carbides are focused on $La_2C_3$ [13-16]. However, the theoretical study about $LaC_2$ is still limited. To our knowledge, the lattice dynamics and thermal properties of $LaC_2$, such as phonon dispersion curve, heat capacity and coefficient of thermal expansion, are rarely studied. Thus, systematic study on lattice dynamics and thermodynamic properties of $LaC_2$ are of great importance and imperative, since it plays a crucial role in determining materials properties and provides useful information for the potential applications.

In this work, with the help of quasiharmonic approximation (QHA), the thermodynamic properties, especially the thermal expansion coefficients are given for the first time. To clarify the NTE mechanism, we reproduced the NTE behavior parallel to c-axis, and have identified the phonon modes responsible for NTE phenomenon of $LaC_2$. Our results show that the negative thermal

---
* Corresponding author. Fax: +86 371 67767758.
E-mail address: jiayu@zzu.edu.cn (Y. Jia).

http://dx.doi.org/10.1016/j.physleta.2014.10.041
0375-9601/© 2014 Elsevier B.V. All rights reserved.

expansion along c-axis is caused by the transverse vibration of C and La atoms perpendicular to the c-axis. Additionally, a tiny NTE effect has been predicted in a-axis.

## 2. Computational details

In the present first-principles DFT calculations, total energy and geometry optimization are done by means of VASP code [17-19]. The ion-electron interaction is described by projector augmented wave (PAW) method [20,21], and the exchange and correlation effects are depicted by the scheme of GGA-PBE functional [22]. A 9×9×9 Monkhorst-Pack k-point meshes and a 520 eV energy cutoff of the plane-wave basis set are used to guarantee the accurate calculation. Because of the metallic property, Methfessel-Paxton scheme with a smearing width of 0.05 eV is employed to deal with this compound.

For discussing the thermodynamic properties of LaC₂, the Helmholtz free energy $F(V,T)$ has been calculated in the following formula [23,24].

$$
F(V, T)=E_{0}(V)+F_{e l}(V, T)+F_{v i b}(V, T) \tag{1}
$$

Where $E_{0}$ is the 0 K total energy of this compound, $F_{el}$ represents thermal electronic contribution to the $F(V,T)$, which can be obtained from the electronic excitation energy and the bare electronic entropy. Usually, its contribution to total free energy can be negligible. $F_{vib}$ is the vibrational free energy that comes from phonon contribution. The vibrational free energy can be obtained using the quasiharmonic approximation (QHA). When temperature is away from the melting point, the QHA has been proved to be a good approximation. Within QHA, it is given by

$$
F_{v i b}=\int_{0}^{\infty} g(\omega) d \omega\left[\hbar \omega / 2+k_{B} T \ln \left(1-\exp \left(-\hbar \omega / k_{B} T\right)\right)\right] \tag{2}
$$

$\omega$ and $g(\omega)$ are the harmonic phonon frequency and the phonon density of states (PhDOS), respectively. In our previous works [23-25], this method gained intriguing success.

Phonon dispersions and PhDOS are calculated using the supercell method implemented in PHONOPY package [26]. A 108-atom supercell containing $3 \times 3 \times 2$ unit cell is chosen and the displacement in the supercell for phonon calculations is 0.01 Å. To consider the thermal expansion, we calculate the volume-dependent phonon frequency at 15 volume points. At each volume point, internal atomic positions are optimized with a $\Gamma$-centered $3 \times 3 \times 3$ k-mesh, energy cutoff of 520 eV and total energy convergence threshold of $10^{-8}$ eV. Phonon vibrational modes in the first Brillouin zone (BZ) of these volumes are all no imaginary parts, which indicate that they are all dynamically stable. The equilibrium volume was obtained by minimizing free energy $F(V,T)$ with respect to $V$ from fitting the integral form of the Vinet equation of state (EOS) [27]. The volume thermal expansion coefficient $\alpha_{V}(T)=\frac{1}{V} \frac{d V}{d T}$ in QHA can be expressed as

$$
\alpha_{V}(T)=\frac{1}{B V} \sum_{i} \gamma_{i} C_{i}(T) \tag{3}
$$

Where $\gamma_{i}$ and $C_{i}(T)$ are mode Grüneisen parameter and specific heat of the $i$th vibrational mode at temperature $T$. $B(T)=$ $-\frac{1}{V} \frac{\partial^{2} F(V, T)}{\partial V^{2}}$ is the bulk modulus at finite temperature. In the case of anisotropic thermal expansion compounds, the coefficient of linear thermal expansion is given by $\alpha_{l}(T)=\frac{1}{a_{i}} \frac{d a_{i}}{d T}, a_{i}$ represents the lattice parameter $a$ or $c$. As for the anisotropic crystal structure, the relationship between $\alpha_{V}$ and $\alpha_{l}$ for tetragonal structure is $\alpha_{V}=2 \alpha_{a}+\alpha_{c}$ [28].

![](./images/814683121906614274_1.jpg)

Fig. 1. The schematic of primitive cell (a) and conventional unit cell (b) of LaC₂. Blue and gray balls represent La and C atoms respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<table><caption>Table 1 Comparison of calculated and experimental lattice constants of LaC₂. z is the inner parameter.</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>$a=b$ (Å)</th>
<th>$c$ (Å)</th>
<th>$z$</th>
<th>Volume (Å³)</th>
</tr>
</thead>
<tbody>
<tr>
<td>This work</td>
<td></td>
<td>3.9789</td>
<td>6.5824</td>
<td>0.4026</td>
<td>104.214</td>
</tr>
<tr>
<td>Expt [29]</td>
<td></td>
<td>3.937(1)</td>
<td>6.579(2)</td>
<td>0.4024(5)</td>
<td>101.974(3)</td>
</tr>
<tr>
<td>Expt [11]</td>
<td>4 K</td>
<td>3.9268</td>
<td>6.5748</td>
<td>0.4031</td>
<td>101.383</td>
</tr>
<tr>
<td></td>
<td>300 K</td>
<td>3.9364</td>
<td>6.5783</td>
<td>0.4031</td>
<td>101.933</td>
</tr>
</tbody>
</table>

## 3. Results and discussions

### 3.1. Structural and electronic properties of LaC₂

To check the applicability and accuracy of the density functional calculations methods used in this work, the optimized lattice constants and electronic structures of bulk LaC₂ are investigated by calculating the total energies and electronic density of states (DOS). The modeled bulk LaC₂ unit cells crystallizes in tetragonal structure with the I4/mmm (No. 139) space group symmetry, point group is $4/mmm$ ($D_{4h}$ in Schoenflies notation). Each conventional unit cell contains two formula units ($Z=2$), and two La atoms are located at $2a$ $(0,0,0)$ Wyckoff position, while four C atoms are in $4e$ Wyckoff position at $(0,0,z)$, the four C atoms forming two C-C dimmers (denoted as C2) parallel along the c-axis, as shown in Fig. 1(b). Fig. 1(a) shows the primitive cell ($Z=1$) of LaC₂, which includes one La and two C atoms. The optimized lattice parameters and previous experimental data are presented in Table 1. Though the lattice constants optimized in GGA scheme are little bigger, the errata are less than 2% and acceptable.

The electronic DOS is shown in Fig. 2. One can see that there are three parts are separated by gaps. Below $-30$ eV the peaks are completely the localized La-s states. In the energy range of $(-12)-(-18)$ eV, the DOS originates from C and La atoms, the hybridization of La-p with C-s and C-p states corresponding to a weak bonding between La and C-C dimmer. Around $-4$ eV, the DOS are composed of C-s and C-p states. The C-2p and La-d electronic states mixed in the range around the Fermi level $E_{F}$. There is no gap at the Fermi energy, which implies the metallic character, agree well with the experimental measurement [30]. Above the Fermi level, the DOS are dominated by La-d and C-p electronic states.

To analysis the bonds quantitatively and revealing the bond nature, the charge density on the (110) plane of LaC₂ unit cell is shown in Fig. 3. We can see that strong covalent bonding between

![](./images/814683121906614274_2.jpg)

Fig. 2. The electronic density of states (DOS) and atom-resolved DOS of LaC₂. Vertical black dashed line at 0 eV indicates the Fermi level.

![](./images/814683121906614274_3.jpg)

Fig. 3. Charge density on (110) plane of LaC₂.

C–C atoms is evidenced by the high charge density distribution along the C–C direction. Around the La atoms, there are spherical- like charge density contours and is non-zero in the midpoints be- tween La and C2 dimmer, confirming the ionic bonding nature of La–C2. The stiffer C–C dimmer and the weaker La–C2 bonds ac- count for the possibility of flexing of the La–C2–La linkage during the transverse motion of C2 perpendicular to c-axis.

### 3.2. Phonon dispersion

As mentioned above, PhDOS are required as an input in pre- dicting the thermodynamic properties. Based on QHA, the phonon dispersion curves and PhDOS were calculated. The primitive cell of tetragonal LaC₂ contains three atoms, i.e. there are nine normal modes, of which three are acoustic modes and six are optical ones. Using factor group analysis, the phonon modes can be described by the irreducible representations in zone-center $\Gamma$ as follows:

$$
\Gamma_{a c}=A_{2 u}+E_{u} \quad \text { and }
$$

$$
\Gamma_{o p t}=E_{u}(\mathrm{IR})+A_{2 u}(\mathrm{IR})+E_{g}(\mathrm{R})+A_{2 g}(\mathrm{R})
$$

where IR and R represent IR-active and Raman-active modes, re- spectively. La atoms occupied the inversion center of I4/mmm, they do not contribute to the Raman scattering process, and the Raman- active modes originate only from the vibrations of C atoms.

By means of the optimized lattice constants, the full phonon dispersion curves along high symmetry direction $\Gamma$-X-M-$\Gamma$-Z-R-A for tetragonal LaC₂ at 0 K are shown in Fig. 4(a). Due to numerical errors, slightly imaginary of acoustic phonon modes (~0.006 THz) was found in the vicinity of $\Gamma$ point. According to previous calcu- lations [23–25], the tiny effects of these imaginary are found to be negligible.

![](./images/814683121906614274_4.jpg)

Fig. 4. (a) Phonon dispersion curves along high symmetry directions. (b) Phonon DOS of tetragonal LaC₂, where black solid, red dotted and blue solid curves rep- resent total phonon DOS and partial phonon DOS of C and La, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

The partial phonon DOS together with the total phonon DOS were also plotted in Fig. 4(b). Judging from Fig. 4(a) and (b), one can find that the profiles could be divided into 3 regions. The low frequency part (<3.96 THz) is due to the collective vibrations of La and C atoms and almost entirely contributed by La atoms; the intermediate region around 10 THz is mainly from the mixed vi- brations of lanthanum and carbide atoms, which corresponds to the bonding of La–C; the high frequency part above 46.1 THz is originated only from the vibrational mode of carbon atoms. Huge mass difference between La and C atoms caused the significant discrepancies of the vibrational modes distribution.

### 3.3. Coefficients of thermal expansion

Now we turn to investigate the thermodynamic properties, es- pecially the coefficients of thermal expansion along c- and a-axis. In Fig. 5(a), the free energy, heat capacity and vibrational en- tropy are investigated as a function of temperature. Taken into ac- count the zero point energy (about 6.81 kJ/mol per atom), the free

![](./images/814683121906614274_5.jpg)

Fig. 5. Temperature dependent free energy $F(V,T)$, vibrational entropy $S$, and heat capacity $C_V$. The horizontal dashed line is guide for eyes.

![](./images/814683121906614274_6.jpg)

Fig. 6. Temperature dependence of lattice parameter $c$ and $a$. Inset: the tiny NTE along $a$-axis up to $\sim 10$ K.

energy $F(V,T)$ was found to decrease monotonously with increasing temperature. While, vibrational entropy $S$ tends to increase with temperature elevating. In the low temperature region ($T < \sim 50$ K), heat capacity $C_V$ follows the Debye $T^3$ law, and in high temperature part (above 400 K), it is close to a fixed value approximate 150 J mol/K, which is agree well with the Dulong-Petit law.

Fig. 6 illustrates the temperature-dependent lattice parameter $c$ and $a$. From Fig. 6(a), an intriguing NTE phenomenon is clearly seen in the low temperature region $T < \sim 42$ K. Using the formula indicated in part II, the average thermal expansion coefficient along $c$-axis in the low temperature region (up to $\sim 42$ K) is about $\alpha_c = -1.67 \times 10^{-6}\ \text{K}^{-1}$. Babizhetskyy et al. [11] does not give the coefficients of thermal expansion (CTE) directly. Based on the experimental data proved by Babizhetskyy et al., the coefficient of thermal expansion along $c$-axis estimated to be $\sim -1.0 \times 10^{-6}\ \text{K}^{-1}$ in the temperature range below 60 K. Because the temperature-dependent experimental lattice constants was provided only at 4 K, 30 K and 60 K. Our results, NTE temperature region as well as thermal expansion coefficient along $c$-axis, agree well with the experimental results.

To be compared, CTE in $ab$ plane were shown in Fig. 6(b). One can find a tiny NTE phenomenon along $a$-axis in the ultra-low temperature region (below 10 K), and the CTE is nearly zero, approximately $-3.0 \times 10^{-7}\ \text{K}^{-1}$, too small to be observed. The missing in experiments may come from the big measuring temperature steps ($\Delta T_{step} \sim 26$ K). We hope a precise measurement in future may clarify the difference. The average coefficient of thermal expansion up to 42 K along $a$-axis is positive, about $\alpha_a = 2.55 \times 10^{-6}\ \text{K}^{-1}$. Thus, the bulk coefficient of thermal expansion can be expressed as $\alpha_V = 2\alpha_a + \alpha_c = 3.43 \times 10^{-6}\ \text{K}^{-1}$. Based on the experimental data proved by Babizhetskyy et al., the CTE of bulk $\text{LaC}_2$ is about $\sim 3.346 \times 10^{-6}\ \text{K}^{-1}$ below 60 K, which coincides with the experiment statement that "$a$-parameter and cell volume behave rather normally showing a continuous contraction with decreasing temperature" [11].

<table><caption>Table 2 Calculated optical phonon modes frequencies and Grüneisen parameters at Brillouin zone center $\Gamma$ point.</caption>
<thead>
<tr>
<th>Symmetry</th>
<th>Frequency (THz)</th>
<th>$\gamma_i$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A_{2u}$</td>
<td>0</td>
<td>/</td>
</tr>
<tr>
<td>$E_u$</td>
<td>0</td>
<td>/</td>
</tr>
<tr>
<td>$E_u$</td>
<td>8.15</td>
<td>$-1.969$</td>
</tr>
<tr>
<td>$A_{2u}$</td>
<td>9.23</td>
<td>6.439</td>
</tr>
<tr>
<td>$E_g$</td>
<td>10.51</td>
<td>$-1.401$</td>
</tr>
<tr>
<td>$A_{2g}$</td>
<td>49.74</td>
<td>0.392</td>
</tr>
</tbody>
</table>

### 3.4. Mechanism of the negative thermal expansion along $c$-axis

After the detailed analysis of the CTE along $c$- and $a$-axis, we now turn our attention to the mechanisms of the negative thermal expansion. Since $C_i(T)$ in Eq. (3) is always positive (see Fig. 5), the thermal expansion coefficient being positive or negative is only governed by Grüneisen parameter $\gamma_i$. Table 2 lists the optical phonon modes frequencies and Grüneisen parameters at Brillouin zone center. It is noteworthy that two double-degenerate optical modes, $E_u$ and $E_g$, possess negative Grüneisen parameters.

According to group theory analysis, we illustrate the displacement patterns of the phonon modes contributing to NTE in $\text{LaC}_2$ in Fig. 7.

For materials with a flexible network, the transverse vibration of the bridge atoms, known as tension-effect, allows the contraction along the vertical direction [31,32]. The crystal structure of tetragonal $\text{LaC}_2$ contains close-packed La-atom double layer with C-C dimmer occupied the $\text{La}_6$ octahedral voids (see Fig. 7). These connect via van der Waals forces in stacks along $c$-axis. So, the C-C dimmer has a larger degree of freedom in La-C2-La chain, forming a flexible network.

The phonon mode $E_u$ in 8.15 THz corresponds to an opposite vibration between C-C dimmer and La atoms, while $E_g$ mode represents a relative-motion among C atoms perpendicular to C-C dimmer and La atoms keep still. In these two phonon modes, pull-up effects are expected, and a NTE phenomenon appeared along $c$-axis.

Rechecking these two modes, we should expect a positive thermal expansion along $a$-axis, because the transverse vibrations of bridge-C2 atoms may result in an increasing of average length in $a$-axis. Contradicting with our expectation, there is a tiny NTE along $a$-axis in the ultra-low temperature region (below 10 K). To clarify this conflict, we qualitatively discussed the vibrational modes of non-center points on the boundary of Brillouin zone (BZ). Fig. 8 shows the Grüneisen parameter along several high symmetry directions. At the $M(0.5, 0.5, 0)$ and $Z(0, 0, 0.5)$ points, several pronounced negative $\gamma_i$ can be seen.

Due to the frequency of acoustic modes at $\Gamma$ point being zero, we chose the adjacent point $\Gamma_\infty$ near $\Gamma$ as the limit. The Grüneisen parameters of the three acoustic modes at $\Gamma_\infty$ point are $-0.007$ and $-0.005$ respectively. In spite of relatively smaller contribution

![](./images/814683121906614274_7.jpg)

Fig. 7. Schematic of the vibrational modes responsible for the negative thermal expansion, $E_{\text{u}}$ (a), $E_{\text{g}}$ (b) and $\text{La}_{6}$ octahedra (c).

compared with optical phonons, the acoustic modes also affect the NTE at low temperature.

Except for NTE-related tension-effect, there exists a bond-stretching effect [32], relative motion between atoms or component along the bond direction, which tend to lower the frequencies and contribute to positive thermal expansion. Both mechanisms occur simultaneously with opposite effects. In Fig. 8, along several high-symmetry directions, we pictured another three vibrational modes possessing negative Grüneisen parameters. In Fig. 8(b), an obvious bond-stretching effect can be seen in the vibrational mode with 2.40 THz at $M$ (0.5, 0.5, 0). This mode has the lowest frequency and the absolute value of negative Grüneisen parameter is bigger than that of $E_{\text{u}}$ and $E_{\text{g}}$ modes at BZ center. In low temperature region, for example, $<10$ K, the tension-effect surpass the bond-stretching effect, a NTE phenomenon along $a$-axis emerges. Raising temperature, the bond-stretching effect exceeds the tension-effect gradually, $\text{LaC}_{2}$ will expand upon heating in $a$-axis, and NTE disappears. The other two modes, 3.08 THz at $M(0.5,0.5,0)$ and 3.61 THz at $Z(0,0,0.5)$, have the larger negative $\gamma_{i}$ approximately $-14$ and these two vibrational modes (see Fig. 8(c), (d)) show the similar vibrational motion with the $E_{\text{u}}$ and $E_{\text{g}}$ modes at BZ center. Thus, these modes contribute to the NTE along $c$-axis.

![](./images/814683121906614274_8.jpg)

Fig. 8. (a) Mode Grüneisen parameters along high-symmetry directions. A, B, C denote acoustic modes, D–I belong to optical modes. (b), (c), (d) The vibrational modes with negative Grüneisen parameters at $M(0.5,0.5,0)$ and $Z(0,0,0.5)$.

## 4. Conclusions

In summary, based on DFT and QHA, a detailed theoretical study for the electronic and thermal properties of $\text{LaC}_{2}$ has been determined. The electronic DOS show that $\text{LaC}_{2}$ is metallic and the charge density indicates that La–C2–La linkage is flexing for the vibrational motion perpendicular to $c$-axis. We reproduced the negative thermal expansion along $c$-axis, and the NTE temperature region $(T < \sim42$ K) coincides with experiment measurement $(T < \sim50$ K). The calculated CTE is approximately $\sim -1.67 \times 10^{-6}$ K$^{-1}$, agreeing with the estimated one $(\sim -1.0 \times 10^{-6}$ K$^{-1})$. A tiny NTE $(\alpha_{a}=-3 \times 10^{-7}$ K$^{-1})$ was also predicted along $a$-axis, and the missing in experiment was contributed to the big temperature measuring step. At last, we calculate the Grüneisen parameters along high symmetry direction to clarify the mechanism of the anisotropic NTE phenomenon. The negative $\gamma_{i}$ are found at $\Gamma$, $M$ and $Z$ points. At BZ, $E_{\text{u}}$ and $E_{\text{g}}$ modes contribute to the NTE along $c$-axis, which corresponding to the transverse vibrational motions and was attributed to the tension-effect. On the BZ boundary, the vibrational modes are more complicated, both tension-effect and bond-stretching are found simultaneously with opposite effects. The modes with the frequencies of 3.08 THz at $M(0.5,0.5,0)$ and 3.09 THz, 3.61 THz at $Z(0,0,0.5)$ have the similar effect with $E_{\text{u}}$ and $E_{\text{g}}$ modes at $\Gamma$, and contribute to the NTE along $c$-axis. The mode of 2.40 THz at $M(0.5,0.5,0)$ shows stronger tension-effect, and surpass the bond-stretching in low temperature region $(<10$ K), thus, NTE in $a$-axis emerges. Raising temperature, the bond-stretching exceeds and NTE phenomenon in $a$-axis disappears.

This work reproduced the anisotropic NTE phenomenon in $\text{LaC}_{2}$ and clarified the mechanism of NTE, hoping this work would be useful for guidance in experiments in future.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant Nos. 11274280, 10974183) and the

Ministry of Education of the People's Republic of China (Nos. 20114101110003, 20114101110003). All the calculations were performed on the High Performance Clusters of Zhengzhou University.

## Appendix A. Supplementary material

Supplementary material related to this article can be found online at http://dx.doi.org/10.1016/j.physleta.2014.10.041.

## References

[1] T.A. Mary, J.S.O. Evans, T. Vogt, A.W. Sleight, Science 272 (1996) 90-92.
[2] E.-J. Liang, Rec. Patents Mater. Sci. 3 (2010) 106.
[3] M.G. Tucker, A.L. Goodwin, M.T. Dove, D.A. Keen, S.A. Wells, J.S.O. Evans, Phys. Rev. Lett. 95 (2005) 255501.
[4] F. Bridges, T. Keiber, P. Juhas, S.J.L. Billinge, L. Sutton, J. Wilde, G.R. Kowach, Phys. Rev. Lett. 112 (2014) 045505.
[5] X. Xing, J. Deng, J. Chen, G. Liu, Rare Met. 22 (2003) 294-297.
[6] J. Chen, L. Fan, Y. Ren, Z. Pan, J. Deng, R. Yu, X. Xing, Phys. Rev. Lett. 110 (2013) 115901.
[7] K. Takenaka, H. Takagi, Appl. Phys. Lett. 87 (2005) 261902.
[8] X. Song, Z. Sun, Q. Huang, M. Rettenmayr, X. Liu, M. Seyring, G. Li, G. Rao, F. Yin, Adv. Mater. 23 (2011) 4690-4694.
[9] M. Azuma, W.T. Chen, H. Seki, M. Czapski, S. Olga, K. Oka, M. Mizumaki, T. Watanuki, N. Ishimatsu, N. Kawamura, S. Ishiwata, M.G. Tucker, Y. Shimakawa, J.P. Attfield, Nat. Commun. 2 (2011) 347.
[10] K. Oka, K. Nabetani, C. Sakaguchi, H. Seki, M. Czapski, Y. Shimakawa, M. Azuma, Appl. Phys. Lett. 103 (2013) 061909.

[11] V. Babizhetskyy, O. Jepsen, R.K. Kremer, A. Simon, B. Ouladdiaf, A. Stolovits, J. Phys. Condens. Matter 26 (2014) 025701.
[12] T. Mochiku, T. Nakane, H. Kito, H. Takeya, S. Harjo, T. Ishigaki, T. Kamiyama, T. Wada, K. Hirata, Physica C, Supercond. 426 (431) (2005) 421-425.
[13] S. Kuroiwa, Y. Saura, J. Akimitsu, M. Hiraishi, M. Miyazaki, K.H. Satoh, S. Takeshita, R. Kadono, Phys. Rev. Lett. 100 (2008) 097002.
[14] J.S. Kim, W. Xie, R.K. Kremer, V. Babizhetskyy, O. Jepsen, A. Simon, K.S. Ahn, B. Raquet, H. Rakoto, J.M. Broto, B. Ouladdiaf, Phys. Rev. B 76 (2007) 014516.
[15] X. Wang, I. Loa, K. Syassen, R.K. Kremer, A. Simon, M. Hanfland, K. Ahn, Phys. Rev. B 72 (2005) 064520.
[16] J.S. Kim, R.K. Kremer, O. Jepsen, A. Simon, Curr. Appl. Phys. 6 (2006) 897-902.
[17] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15-50.
[18] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558-561.
[19] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169-11186.
[20] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953-17979.
[21] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758-1775.
[22] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.
[23] L. Wang, P.-F. Yuan, F. Wang, Q. Sun, E.-J. Liang, Y. Jia, Mater. Res. Bull. 47 (2012) 1113-1118.
[24] Z. Wang, F. Wang, L. Wang, Y. Jia, Q. Sun, J. Appl. Phys. 114 (2013) 063508.
[25] P. Ding, E.J. Liang, Y. Jia, Z.Y. Du, J. Phys. Condens. Matter 20 (2008) 275224.
[26] A. Togo, F. Oba, I. Tanaka, Phys. Rev. B 78 (2008) 134106.
[27] P. Vinet, J.H. Rose, J. Ferrante, J.R. Smith, J. Phys. Condens. Matter 1 (1989) 1941.
[28] H.-Y. Wang, H. Xu, T.-T. Huang, C.-S. Deng, Eur. Phys. J. B 62 (2008) 39-43.
[29] D.W. Jones, I.J. McColm, J. Yerkess, J. Solid State Chem. 92 (1991) 301-311.
[30] M. Atoji, K. Gschneidner, A.H. Daane, R.E. Rundle, F.H. Spedding, J. Am. Chem. Soc. 80 (1958) 1804-1808.
[31] K. Takenaka, Sci. Technol. Adv. Mater. 13 (2012) 013001.
[32] G.D. Barrera, J.A.O. Bruno, T.H.K. Barron, N.L. Allan, J. Phys. Condens. Matter 17 (2005) R217.