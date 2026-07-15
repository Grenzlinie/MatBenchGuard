PHYSICAL REVIEW B 94, 054507 (2016)

# Electron-phonon superconductivity in the ternary phosphides $BaM_2P_2$ ($M$ = Ni, Rh, and Ir)

Ertuğrul Karaca, $^{1}$ H. M. Tütüncü, $^{1,2}$ G. P. Srivastava, $^{3}$ and S. Uğur $^{4}$

$^{1}$Sakarya Üniversitesi, Fen-Edebiyat Fakültesi, Fizik Bölümü, 54187 Adapazarı, Turkey
$^{2}$Sakarya Üniversitesi, BIMAYAM Biyomedikal, Manyetik ve Yarıiletken Malzemeler Araştırma Merkezi, 54187 Adapazarı, Turkey
$^{3}$School of Physics, University of Exeter, Stocker Road, Exeter EX4 4QL, United Kingdom
$^{4}$Gazi Üniversitesi, Fen Fakültesi, Fizik Bölümü, Ankara, Turkey

(Received 30 May 2016; published 8 August 2016)

$Ab$ initio plane-wave pseudopotential calculations of electronic and vibrational properties have been carried out for the ternary phosphides $BaM_2P_2$ ($M$ = Ni, Rh and Ir) with a $ThCr_2Si_2$-type structure. The calculated electronic results show the metallic character of $BaM_2P_2$, and the plots of total and partial density of states of $BaM_2P_2$ exhibit strong hybridization between the $d$ states of the $M$ atom and the $p$ states of the P atom below the Fermi energy. Differences in the phonon spectrum and density of states both in the acoustical and optical ranges for these compounds are presented and discussed. The Eliashberg spectral function for these compounds has been calculated by using a linear response approach based on the density functional theory. By integrating the Eliashberg spectral function, the average electron-phonon coupling parameter ($\lambda$) is determined to be 0.61 for $BaNi_2P_2$, 0.55 for $BaIr_2P_2$, and 0.43 for $BaRh_2P_2$. Using the calculated values of $\lambda$ and the logarithmically averaged phonon frequency $\omega_{\text{ln}}$ the superconducting critical temperature ($T_c$) values for $BaNi_2P_2$, $BaIr_2P_2$, and $BaRh_2P_2$ are obtained to be 2.80, 1.97, and 0.70 K, respectively, which compare very well with their experimental values of 3.0, 2.1, and 1.0 K.

DOI: 10.1103/PhysRevB.94.054507

## I. INTRODUCTION

Body-centered tetragonal $ThCr_2Si_2$ is a crystal structure with the highest number of representatives. More than 700 different compounds [1] of $AM_2X_2$ stoichiometry have been found to crystallize in this type of crystal structure. The main reasons for this large number are its high capability to adjust to strongly different atomic sizes as well as a broad range of electron counts. Thus, the intermetallic $AM_2X_2$ ($A$ = rare earth metal, alkaline earth or alkali element, $M$ = transition metals, $X$ = B, P, Si, As, Ge) have been studied for a long time because of their exotic properties, such as heavy fermion behavior, superconductivity, curious magnetic order, and quantum criticality [2–12]. In particular, superconductivity is found for ruthenium phosphide $LaRu_2P_2$ with the low transition temperature ($T_c$) of 4.0 K [13], while the compounds $Ba(K)Fe_2As_2$ exhibit the high transition temperature ($T_c$) of 38 K [14]. In 2008, Ronning and co-workers [15] synthesized single crystals of $BaNi_2As_2$, which exhibit both a first order transition at 130 K (likely to be a combined structural and magnetic transition) and superconductivity at 0.7 K. Furthermore, Kurita and co-workers [16] carried out magnetothermal conductivity experiments on $SrNi_2P_2$ to identify the structure of the superconducting gap. Both from the temperature and field dependence of thermal conductivity, they emphasized that $SrNi_2P_2$ is a fully gapped superconductor, as is the case in $BaNi_2As_2$. On the theoretical side, based on first-principles full-potential linearized augmented plane wave method-generalized gradient approximation calculations, Shein and Ivanovskii [17] studied structural and electronic properties of low-temperature superconductors $SrNi_2As_2$, $BaNi_2As_2$, as well as $SrNi_2P_2$. This theoretical work showed that the near-Fermi valence bands in these materials are derived basically from Ni $3d$ states with some admixture of antibonding P (As) $p$ states. Moreover, the linear-response calculations were used to calculate phonon modes and electron-phonon interaction properties of $BaNi_2As_2$ [18]. Results for the phonon spectrum and electron-phonon coupling are consistent with a classification of this material as a conventional phonon-mediated superconductor [18]. Superconductivity was also discovered for nickel phosphide $BaNi_2P_2$ with the $T_c$ of $\sim$3.0 K [19]. The structural properties of this material have been known since the early experimental work of Keimes *et al* [20]. Terashima and co-workers [21] have reported measurements of the de Haas van Alphen (dHvA) oscillation for the pnictide superconductor $BaNi_2P_2$. Furthermore, Ideta and co-workers [22] have carried out an angle-resolved photoemission spectroscopy (ARPES) study of $BaNi_2P_2$. They found hole and electron Fermi surfaces (FSs) around the Brillouin zone center and corner, respectively. The shape of the hole FS strikingly changed with photon energy, showing strong three dimensionality. On the theoretical side, the electronic structure of $BaNi_2P_2$ has been studied by several groups [17,21,23,24]. The band structure calculations using a full potential linearized augmented plane wave (FLAPW) method, both within the local density approximation (LDA) [21] and the generalized gradient density functional approximation (GGA) [17,23]. Furthermore, the electronic properties of $BaNi_2P_2$ have been investigated using the tight binding linear muffin-tin orbital method within the local density approximation [24]. These theoretical works [17,21,23,24] clarify that the near-Fermi valence bands in $BaNi_2P_2$ are derived basically from Ni $3d$ states with considerable admixture of P $p$ states.

Since most of $ThCr_2Si_2$-type (or 122) superconductors include the strong magnetic element Fe, magnetic order is present to possibly weaken or interfere with the superconducting state in these materials. Thus, it is interesting to find compounds that adopt the $ThCr_2Si_2$-type structure but do not include Fe or Ni. In 2009, heat capacity, resistivity, and magnetic susceptibility measurements suggested bulk superconductivity in single crystals of $BaIr_2P_2$ ($T_c = 2.1$ K) and $BaRh_2P_2$ ($T_c = 1.0$ K) [25,26]. These two materials,

2469-9950/2016/94(5)/054507(11)
054507-1
©2016 American Physical Society

![](./images/811166912649101312_1.jpg)

FIG. 1. Tetragonal unit cell for ${\rm BaNi_2P_2}$, ${\rm BaIr_2P_2}$, and ${\rm BaRh_2P_2}$ crystallizing in the ${\rm ThCr_2Si_2}$ structure. One $M$ ($M$ = Ni, Rh, and Ir) atom is bonded by four P atoms generating the ${\rm MP_4}$-tetrahedron layers while Ba cations lie between them connecting these layers together. The $\alpha$ angle is a good marker of distortion in ${\rm MP_4}$ tetrahedra while $d_{P-P}$ is the interlayer P-P distance.

negatively charged layers of ${\rm MP_4}$ tetrahedra and positively charged Ba layers, alternately stacked along the $z$ direction. The ${\rm MP_4}$ layers include strong covalent $M$-P bonds and weaker $M$-$M$ interactions, while the interaction between Ba and the ${\rm MP_4}$ layers is rather ionic. Thus we can state that only one of covalent, metallic, and ionic bonding schemes alone cannot provide a proper depiction of bonding in ternary phosphides. All of these three kinds of bondings co-exist in these materials.

Structural parameters were obtained from total energy minimization and acceptable level of zero-force conditions. The determined equilibrium lattice constants ($a$ and $c$), the internal parameter ($z$), the closest $M$-$M$ distance ($d_{M-M}$), the closest $M$-P distance ($d_{M-P}$), the interlayer P-P distance ($d_{P-P}$), and the bond angle ($\alpha$) are reported in Table I. In general, the calculated lattice parameters and internal parameters for all the ternary phosphides ${\rm BaM_2P_2}$ are in good accordance with previous experimental [20,25,27,28,32] and theoretical [17,24,30] results. The maximum difference in the lattice parameters is around 2.0% for all the studied compounds, while the maximum difference in the internal parameter $z$ is around 0.7% for ${\rm BaNi_2P_2}$. This level of disagreement in the lattice parameters is routinely noted from theories based on the generalized gradient approximation.

The closest $M$-P distance is calculated to be 2.273 Å, 2.370 Å, and 2.387 Å for ${\rm BaNi_2P_2}$, ${\rm BaRh_2P_2}$, and ${\rm BaIr_2P_2}$, respectively. These distances are smaller than the sum of the covalent radii ($R^{{\rm Ni}} = 1.24$ Å, $R^{{\rm Rh}} = 1.42$ Å, $R^{{\rm Ir}} = 1.41$ Å, and $R^{{\rm P}}$$= 1.07$ Å) and thus confirm strong $M$-P bonding within the ${\rm MP_4}$ layers. The closest $M$-$M$ separation is found to be 2.816 Å and 2.810 Å for ${\rm BaNi_2P_2}$ and ${\rm BaRh_2P_2}$, respectively. We have to mention that these values are much longer than the corresponding values of 2.49 Å and 2.69 Å in the fcc metals Ni and Rh, respectively. This result clearly indicates weak $M$-$M$ bonding within the ${\rm MP_4}$ layers. Table I clearly shows that the variation of the interlayer distance $d_{P-P}$ by changing the $M$ atoms is quite small. This observation is in agreement with previous theoretical calculations [24,29] which show that the interlayer distance $d_{P-P}$ strongly depends on the size of the Ba atom rather than the size of the $M$ atom. Finally, when a small Ni atom is replaced by a larger atom (Rh or Ir), the value of the vertical P-$M$-P angle ($\alpha$) becomes closer to $109.5^\circ$ for an ideal tetrahedron.

As electrons near the Fermi surface are involved in the formation of the superconducting state, it is inevitable to investigate their nature. Thus, near-Fermi band structures of the ternary phosphides ${\rm BaM_2P_2}$ are illustrated in Fig. 2. The overall band profiles for all the studied materials are found

<table>
<caption>TABLE I. Structural parameters for body-centered tetragonal ${\rm BaM_2P_2}$ ($M$ = Ni, Rh and Ir) and their comparison with available experimental and theoretical results.</caption>
<thead>
<tr>
<th>Material</th>
<th>$a$(Å)</th>
<th>$c$(Å)</th>
<th>$z$</th>
<th>$d_{M-M}$(Å)</th>
<th>$d_{M-P}$(Å)</th>
<th>$d_{P-P}$(Å)</th>
<th>$\alpha(^\circ$C)</th>
</tr>
</thead>
<tbody>
<tr>
<td>${\rm BaNi_2P_2}$</td>
<td>3.983</td>
<td>12.079</td>
<td>0.3407</td>
<td>2.816</td>
<td>2.273</td>
<td>3.848</td>
<td>122.34</td>
</tr>
<tr>
<td>Experimental [20]</td>
<td>3.947</td>
<td>11.820</td>
<td>0.3431</td>
<td>2.791</td>
<td>2.260</td>
<td>3.709</td>
<td>121.71</td>
</tr>
<tr>
<td>GGA [17]</td>
<td>3.956</td>
<td>11.995</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>LDA [24]</td>
<td>3.945</td>
<td>11.814</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>118.42</td>
</tr>
<tr>
<td>${\rm BaRh_2P_2}$</td>
<td>3.974</td>
<td>12.858</td>
<td>0.3504</td>
<td>2.810</td>
<td>2.370</td>
<td>3.845</td>
<td>113.94</td>
</tr>
<tr>
<td>Experimental [27]</td>
<td>3.939</td>
<td>12.576</td>
<td>0.3514</td>
<td>2.785</td>
<td>2.346</td>
<td>3.737</td>
<td>114.15</td>
</tr>
<tr>
<td>Experimental [25]</td>
<td>3.931</td>
<td>12.574</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Experimental [32]</td>
<td>3.939</td>
<td>12.576</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>GGA [30]</td>
<td>3.981</td>
<td>12.780</td>
<td>0.3510</td>
<td>2.815</td>
<td>2.371</td>
<td>3.814</td>
<td>114.17</td>
</tr>
<tr>
<td>${\rm BaIr_2P_2}$</td>
<td>4.001</td>
<td>12.865</td>
<td>0.3511</td>
<td>2.829</td>
<td>2.387</td>
<td>3.830</td>
<td>113.93</td>
</tr>
<tr>
<td>Experimental [28]</td>
<td>3.946</td>
<td>12.572</td>
<td>0.3523</td>
<td>2.790</td>
<td>2.355</td>
<td>3.714</td>
<td>113.80</td>
</tr>
<tr>
<td>Experimental [25]</td>
<td>3.947</td>
<td>12.559</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Experimental [32]</td>
<td>3.946</td>
<td>12.572</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>GGA [30]</td>
<td>3.992</td>
<td>12.724</td>
<td>0.3520</td>
<td>2.823</td>
<td>2.383</td>
<td>3.759</td>
<td>113.78</td>
</tr>
</tbody>
</table>

![](./images/811166912649101312_2.jpg)

FIG. 2. Calculated near-Fermi band structures of (a) BaNi₂P₂, (b) BaRh₂P₂, and (c) BaIr₂P₂ in the energy range −2.5 eV to 4.5 eV. The Fermi level is chosen to be 0 eV. The high-symmetry points in the body-centered tetragonal Brillouin zone in cartesian coordinates are: $G1 = \frac{2\pi}{a}((\frac{1}{2}+\frac{a^2}{2c^2}),0.00,0.00)$, $Z = \frac{2\pi}{a}(0.00,0.00,\frac{a}{c})$, $X = \frac{2\pi}{a}(0.50,0.50,0.00)$, $P = \frac{2\pi}{a}(0.50,0.50,\frac{a}{2c})$, and $N = \frac{2\pi}{a}(0.0,0.50,\frac{a}{2c})$.

to be similar to each other. However, the number of bands crossing the Fermi level is not the same for the three ternary phosphides $BaM_2P_2$. For BaNi₂P₂ and BaRh₂P₂, there are two bands crossing the Fermi level along the [100] direction ($\Gamma$-$G1$-$Z$), whereas only one band crosses the Fermi level along this symmetry direction for BaIr₂P₂. For BaIr₂P₂, we observe two bands crossing the Fermi level along the $\Gamma$-$X$ direction, while this number is increased to three for the remaining ternary phosphides. For BaNi₂P₂, the Fermi level is crossed by three bands along the $P$-$\Gamma$ direction, while this number is reduced to two for the other ternary phosphides. For BaIr₂P₂, we find only one band to cross the Fermi level along the $\Gamma$-$N$ symmetry direction while there are two bands crossing the Fermi level along this symmetry direction for the remaining ternary phosphides. Furthermore, for BaNi₂P₂, there is a flat band around −1.2 eV along the $\Gamma$-$Z$ symmetry direction. This flat band is shifted close to the Fermi level and above the Fermi level for BaRh₂P₂ and BaIr₂P₂, respectively. These differences may effect the superconducting properties of these ternary phosphides since the electron-phonon coupling constant $\lambda$ can be given in the following form [38]

$$
\lambda=\frac{N\left(E_{F}\right)\left\langle I^{2}\right\rangle}{M\left\langle\omega^{2}\right\rangle},\qquad(1)
$$

where $M$ represents the mass of the atoms and $\langle\omega^{2}\rangle$ denotes the average of squared phonon frequencies. Further, $\langle I^{2}\rangle$ is the Fermi surface average of squared electron-phonon coupling interaction. According to the above McMillan-Hopfield expression, the electron-phonon coupling constant increases with the increase in the total DOS at the Fermi level $N(E_F)$.

In order to analyze the electronic properties of the studied ternary phosphides in detail, their total and partial density of states (DOS) are calculated and presented in Fig. 3. The gross features of our DOS results are in good accordance with those found in previous theoretical calculations [17,21,23,24,30]. First, we will discuss our results for BaNi₂P₂ in detail. The valence DOS region for BaNi₂P₂ can be mainly divided into two parts separated by a gap of 4 eV: the lower part extending from −12.4 to −10.1 eV and the upper part (of chemical importance) from about −6.1 eV up to the Fermi level. There is only one peak at −10.4 eV in the lower part, which consists mainly of P $3s$ states with negligible contribution from Ni $3d$ states. In the upper part the DOS features are characterized by P $3p$ states with some admixture of the transition metal $3d$ character. The peak at −3.6 eV largely arises from the strong hybridization between Ni $d$ and P $p$ states, which is indicative of strong covalent Ni-P bonding. There are two peaks with energies of −1.9 and −0.7 eV in the energy window from −3.1 to −0.4 eV. Ni $3d$ orbital states make the largest contribution to these two peaks, while much lesser contributions to these peaks come from P electronic states. These states participate in metalliclike Ni-Ni bonds. We can thus emphasize that the valence DOS region of BaNi₂P₂ is mainly formed by the states of NiP layers, while the contribution from the electronic states states of Ba is quite small. This result is not surprising because Ba atoms are in the charge state close to $Ba^{2+}$. Thus, the analysis based on the electronic DOS confirms that the bonding nature in ternary phosphide BaNi₂P₂ is a combination of covalent, ionic, and metallic bonds. Clear identification of the origin of DOS at $E_F$ is essential for understanding the superconducting properties because Cooper pairs in the BCS theory can be generated by electrons which have energies close to the Fermi

![](./images/811166912649101312_3.jpg)

FIG. 3. Calculated total and partial density of states for (a) BaNi₂P₂, (b) BaRh₂P₂, and (c) BaIr₂P₂.

level. In our calculations, the total DOS at the Fermi level ($N(E_F)$) for BaNi₂P₂ is calculated to be 3.64 states/eV, a value slightly lower than a previous GGA value of 3.82 states/eV [23]. Calculations of partial DOS suggest that the total $N(E_F)$ is contributed roughly by 12% from Ba electronic states, 47% from Ni electronic, and 41% P electronic states.

It is noteworthy to mention that Ni $d$ and P $p$ states alone contribute to $N(E_F)$ up to 44% and 30%, respectively. With these results and using the McMillan-Hopfield expression, we can emphasize that Ni $d$ and P $p$ electrons are most influential in the development of the superconducting properties of BaNi₂P₂.

<table><caption>TABLE II. Calculated total and partial density of states at the Fermi level (in states/eV) for the ternary phosphides Ba$M_2$P$_2$ ($M=$ Ni, Rh and Ir).</caption>
<thead>
  <tr>
    <th>Material</th>
    <th>Total</th>
    <th>Ba</th>
    <th>$M$</th>
    <th>P</th>
    <th>Ba($5d$)</th>
    <th>$M(d)$</th>
    <th>P($3p$)</th>
    <th>P($3d$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BaNi$_2$P$_2$</td>
    <td>3.64</td>
    <td>0.429</td>
    <td>1.710</td>
    <td>1.501</td>
    <td>0.289</td>
    <td>1.608</td>
    <td>1.100</td>
    <td>0.350</td>
  </tr>
  <tr>
    <td>BaRh$_2$P$_2$</td>
    <td>3.05</td>
    <td>0.470</td>
    <td>1.440</td>
    <td>1.140</td>
    <td>0.340</td>
    <td>1.200</td>
    <td>0.700</td>
    <td>0.400</td>
  </tr>
  <tr>
    <td>BaIr$_2$P$_2$</td>
    <td>2.65</td>
    <td>0.490</td>
    <td>0.990</td>
    <td>1.170</td>
    <td>0.380</td>
    <td>0.700</td>
    <td>0.600</td>
    <td>0.520</td>
  </tr>
</tbody>
</table>

Now, we compare the electronic DOS for BaNi$_2$P$_2$ with the corresponding DOS for BaRh$_2$P$_2$ and BaIr$_2$P$_2$ in detail. The variation of the total and partial density of states at the Fermi level for the studied ternary phosphides Ba$M_2$P$_2$ are presented in Table II. When Ni is replaced by Rh or Ir, the lowest peak at around $-10.1$ eV for BaNi$_2$P$_2$ is shifted down by around 1.0 eV for BaRh$_2$P$_2$ and BaIr$_2$P$_2$. Furthermore, this peak for both BaRh$_2$P$_2$ and BaIr$_2$P$_2$ contains significant contributions from $M$ $d$ and $p$ states. This means that the $M$ $d$ and P $s$ interaction becomes stronger when Ni is replaced by Rh or Ir. The energy of the forbidden gap in the DOS of BaNi$_2$P$_2$ is found to be 4.0 eV which is reduced to 3.6 and 3.2 eV for BaRh$_2$P$_2$ and BaIr$_2$P$_2$, respectively. However, the upper valence band region in BaRh$_2$P$_2$ (6.9 eV) and BaIr$_2$P$_2$ (8.0 eV) is extended as compared to the corresponding region in BaNi$_2$P$_2$ (6.1 eV) due to the the replacement of the $3d$ Ni atom by the $4d$ Rh and $5d$ Ir atoms. Furthermore, the energy range of $M$ $d$ and P $p$ hybridization in BaRh$_2$P$_2$ (3.6 eV) and BaIr$_2$P$_2$ (3.8 eV) is extended as compared to BaNi$_2$P$_2$ (3.0 eV). Thus, we can emphasize that the partial DOS of $M$ $d$ and P $p$ states for BaRh$_2$P$_2$ and BaIr$_2$P$_2$ are distributed in a larger energy range than the corresponding partial DOS for BaNi$_2$P$_2$. Thus, the contributions of $M$ $d$ and P $p$ states to the total density of states at the Fermi level for BaRh$_2$P$_2$ and BaIr$_2$P$_2$ are decreased as compared to the corresponding contributions for BaNi$_2$P$_2$. Consequently, the total DOS at the Fermi level decreases from the Ni compound to Rh and Ir compounds (see Table II).

### B. Phonons and electron-phonon interaction

We first analyze the zone-center phonon modes of Ba$M_2$P$_2$ classified by the irreducible representations of the point group $\text{D}_{4h}(4/mmm)$. As obtained from group theory, the symmetries of the zone-center optical phonon modes are presented as:

$$
\Gamma=2E_u + 2E_g + 2A_u + B_{1g} + A_{1g}.
$$

The one-dimensional $A$ and $B$ modes contain the vibrations of relevant atoms along the $z$ direction while the doubly degenerate $E$ modes are derived from the motion of relevant atoms in the $x$-$y$ plane. The ungerade ($u$) and gerade ($g$) modes are infrared (IR) and Raman active, respectively. We have presented a comparison of the zone-center phonon frequencies and their electron-phonon coupling parameters for Ba$M_2$P$_2$ in Table III. A critical inspection of Table III reveals that all the zone-center optical phonon modes for ternary phosphides contribute little to the electron-phonon coupling parameter, except for the lowest $E_g$, $B_{1g}$, and $A_{1g}$ phonon modes. Figure 4 displays the atomic displacement patterns of these phonon modes for BaNi$_2$P$_2$. For the lowest $E_g$ mode, different type

<table><caption>TABLE III. The calculated zone-center optical phonon frequencies ($\nu$ in THz) and their electron-phonon coupling parameters ($\lambda$) for Ba$M_2$P$_2$ ($M=$ Ni, Rh and Ir).</caption>
<thead>
  <tr>
    <th>Material</th>
    <th>$E_u$</th>
    <th>$E_g$</th>
    <th>$A_{2u}$</th>
    <th>$B_{1g}$</th>
    <th>$A_{2u}$</th>
    <th>$A_{1g}$</th>
    <th>$E_g$</th>
    <th>$E_u$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BaNi$_2$P$_2$ ($\nu$)</td>
    <td>3.002</td>
    <td>3.263</td>
    <td>3.738</td>
    <td>4.968</td>
    <td>8.351</td>
    <td>8.651</td>
    <td>9.436</td>
    <td>9.461</td>
  </tr>
  <tr>
    <td>BaNi$_2$P$_2$ ($\lambda$)</td>
    <td>0.030</td>
    <td>0.183</td>
    <td>0.009</td>
    <td>0.067</td>
    <td>0.012</td>
    <td>0.155</td>
    <td>0.026</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>BaIr$_2$P$_2$ ($\nu$)</td>
    <td>2.349</td>
    <td>4.543</td>
    <td>3.110</td>
    <td>3.656</td>
    <td>9.622</td>
    <td>12.453</td>
    <td>8.710</td>
    <td>8.865</td>
  </tr>
  <tr>
    <td>BaIr$_2$P$_2$ ($\lambda$)</td>
    <td>0.003</td>
    <td>0.191</td>
    <td>0.004</td>
    <td>0.190</td>
    <td>0.003</td>
    <td>0.043</td>
    <td>0.043</td>
    <td>0.002</td>
  </tr>
  <tr>
    <td>BaRh$_2$P$_2$ ($\nu$)</td>
    <td>2.620</td>
    <td>5.955</td>
    <td>3.429</td>
    <td>4.843</td>
    <td>8.805</td>
    <td>11.371</td>
    <td>9.095</td>
    <td>8.983</td>
  </tr>
  <tr>
    <td>BaRh$_2$P$_2$ ($\lambda$)</td>
    <td>0.004</td>
    <td>0.079</td>
    <td>0.03</td>
    <td>0.122</td>
    <td>0.009</td>
    <td>0.133</td>
    <td>0.015</td>
    <td>0.002</td>
  </tr>
</tbody>
</table>

Ni and P atoms oscillate against each other along the [010] direction. The Ni-related $B_{1g}$ phonon mode consists of the opposing motion of different type Ni atoms along the [001] direction while the P-related $A_{1g}$ phonon mode is characterized by the opposing vibrations of different type P atoms along the [001] direction. We have to mention that the lowest $E_g$, $B_{1g}$, and $A_{1g}$ phonon modes of BaRh$_2$P$_2$ and BaIr$_2$P$_2$ have

![](./images/811166912649101312_4.jpg)

FIG. 4. Eigenvector representations and electron-phonon coupling parameters of zone-center lower $E_g$, $B_{1g}$, and $A_{1g}$ phonon modes for BaNi$_2$P$_2$.

![](./images/811166912649101312_5.jpg)

FIG. 5. (a) The calculated phonon spectrum along high symmetry lines in the Brillouin zone for the body-centered tetragonal ${\rm BaNi_2P_2}$. (b) Total and partial phonon density of states for ${\rm BaNi_2P_2}$.

similar atomic displacement patterns to their counterpatterns of ${\rm BaNi_2P_2}$. The eigenvector representation suggests that these phonon modes dynamically modify the tetrahedral bond angles in ${\rm MP_4}$, which leads to the overlap of $M$ and P electronic states. This overlap makes electron-phonon coupling parameters of these phonon modes larger than the remaining zone-center phonon modes. As can be seen from Table III, electron-phonon coupling parameters of these phonon modes increase with decreasing frequency. This observation is in agreement with the McMillan-Hopfield expression which shows that a soft phonon mode can lead to the larger electron-phonon coupling parameter.

The calculated phonon dispersion relations along the high-symmetry directions in the Brillouin zone and the total and partial density of states of ${\rm BaNi_2P_2}$ are displayed in Figs. 5(a) and 5(b). The phonon dispersion curves can be grouped into two apparent regions: low-frequency region (LFR) (0–5.3 THz), and high-frequency region (HFR) (7.6–9.6 THz). There are three acoustic and six optical phonon bands in the LFR while HFR consists of six optical phonon bands. There is a large gap of 2.3 THz between these two regions. The acoustic and the optical bands in the LFR exhibit considerable dispersive character, with significant overlap between the acoustic and optical phonon branches. The optical phonon modes in the HFR are relatively less dispersive. The doubly degenerate $E_u$ and $E_g$ phonon branches lie above the singly degenerate $A_{2u}$ and $A_{1g}$ branches. The $A_{2u}$ and $A_{1g}$ branches are clearly separated from each other while the $E_u$ and $E_g$ branches show considerable overlap between each other. The nature of the phonon spectrum can be understood more clearly by examining the total and partial phonon DOS in Fig. 5(b). Vibrations involving the three atomic species are located below 4.0 THz. In particular, Ba vibrations are dominant below 2.8 THz, and disappear above 4.0 THz, due to its heavy mass. The Ni-related and P-related phonon densities are quite dispersive, contributing to lattice vibrations over the whole range of phonon frequencies due to their smaller masses as compared to the mass of the Ba atom. In particular, significant Ni-P hybridization has been observed between 2.8 and 4.0 THz. In the frequency region from 4.0 THz to 5.3 THz, the main contribution arises from Ni atoms with a smaller contribution coming from P atoms. Lattice vibrations above the gap region are mainly contributed by the P atom due to its lightest atomic mass. It is noteworthy to mention that Ni atoms do make a considerable contribution to these lattice vibrations.

The calculated phonon dispersion curves for ${\rm BaIr_2P_2}$ along the high symmetry directions of the Brillouin zone are displayed in Fig. 6(a). The calculated phonon spectrum for this compound is 12.5 THz which is 2.9 THz larger than that for ${\rm BaNi_2P_2}$. Similar to the phonon dispersion curves of ${\rm BaNi_2P_2}$, the phonon dispersion curves of ${\rm BaIr_2P_2}$ can be divided into two distinct regions. The LFR lies from 0 to 4.9 THz while the HFR lies from 8.6 to 12.5 THz. Thus, there is 3.7 THz gap between these regions. Different from ${\rm BaNi_2P_2}$, the lowest $E_g$ phonon branch lies above $B_{1g}$ and the lowest $A_{2u}$ branches at the zone center. However, away from the zone center these phonon branches strongly overlap with each other, as we have observed for ${\rm BaNi_2P_2}$. Two highest phonon branches in ${\rm BaIr_2P_2}$ have $A_{2u}$ and $A_{1g}$ characters. Different from ${\rm BaNi_2P_2}$, these two branches cross each other. Figure 6(b) presents the total and partial density of states of ${\rm BaIr_2P_2}$. The frequency region below 2.9 THz is dominated by the vibrations of the heaviest Ba atoms, with a lesser contribution coming from the motion of the remaining atoms. Ba vibrations almost vanish above 3.0 THz. Thus, we can conclude that Ba related vibrations in ${\rm BaIr_2P_2}$ are confined to the lower frequency region than the corresponding vibrations in ${\rm BaNi_2P_2}$. The partial DOS depicts a dominance of Ir atoms with smaller contribution from P atoms in the frequency region between 2.9 and 3.8 THz. Strong Ir-P hybridization exists in the frequency region between 3.8 and 4.9 THz. As expected, P, as the lightest element in the compound, dominates the HFR. We have to emphasize that the contribution of Ir atoms to the HFR is much smaller than that of Ni atoms.

The calculated phonon spectra for ${\rm BaRh_2P_2}$ along several high symmetry lines are shown in Fig. 7(a). Again, two clear regions can be seen in the phonon spectrum. There is 2.2 THz gap between these two regions. Phonon branches in these regions considerably overlap between each other. Figure 7(b) illustrates the total and partial density of states of ${\rm BaRh_2P_2}$. Based on our analysis of the eigenvectors for each atom in the

![](./images/811166912649101312_6.jpg)

FIG. 6. (a) The calculated phonon spectrum along high symmetry lines in the Brillouin zone for the body-centered tetragonal $BaIr_{2}P_{2}$. (b) Total and partial phonon density of states for $BaIr_{2}P_{2}$.

![](./images/811166912649101312_7.jpg)

FIG. 7. (a) The calculated phonon spectrum along high symmetry lines in the Brillouin zone for the body-centered tetragonal $BaRh_{2}P_{2}$. (b) Total and partial phonon density of states for $BaRh_{2}P_{2}$.

unit cell, we find that the low frequency region below 2.8 THz consists of the acoustical and optical vibrations of heaviest Ba atoms with lesser contributions coming from the remaining atoms. Considerable contributions from the three atoms are found between 2.8 and 4.0 THz. The contribution of Rh atoms is strongest between 4.0 and 5.0 THz. The partial DOS reveals a significant Rh-P hybridization between 5.0 and 6.2 THz. Again, the contribution of P atoms is strongest above the gap region. Rh atoms make a lesser contribution to this frequency region than Ni atoms made.

The main goal of this paper is to examine the strength of the electron-phonon interaction in the studied ternary phosphides $BaM_{2}P_{2}$ in order to overtly understand the origin of superconductivity in these materials. The Eliashberg spectral function ($\alpha^{2}F(\omega)$) for $BaNi_{2}P_{2}$, $BaIr_{2}P_{2}$, and $BaRh_{2}P_{2}$ are presented in Fig. 8. We can further determine frequency dependent electron-phonon coupling constant $\lambda(\omega)=\frac{\alpha^{2}F(\omega)}{\omega}$ and average electron-phonon coupling constant $\lambda_{av}\equiv\lambda=2\int\frac{\alpha^{2}F(\omega)}{\omega}d\omega$. The value of the average electron-phonon coupling parameter is obtained to be 0.61, 0.55, and 0.43 for $BaNi_{2}P_{2}$, $BaIr_{2}P_{2}$, and $BaRh_{2}P_{2}$, respectively. This result emphasizes that the electron-phonon interaction in $BaNi_{2}P_{2}$ is slightly stronger than that in the remaining ternary phosphides. Furthermore, $BaNi_{2}P_{2}$ is more likely to exhibit superconductivity with a higher superconducting critical temperature ($T_{c}$) than the other ternary phosphides. Our calculated result $\lambda=0.61$ reveals that the electron-phonon interaction in the ternary phosphide $BaNi_{2}P_{2}$ is of medium strength. Our calculated contributions for $\lambda$ from the LFR and HFR are 75% (0.46) and 25% (0.15), respectively. Thus, the contribution to the electron-phonon interaction is mainly dominated by the phonons in the LFR but considerable contribution comes from the phonons in the HFR. Considerable contribution from high frequency phonons can be related to the light mass of P atom and significant presence of the P electronic states near the Fermi level (see also the McMillan-Hopfield expression). A similar observation has been made for the remaining ternary phosphides.

The electron-phonon coupling constant $\lambda$ makes a positive contribution to the electronic specific heat coefficient $\gamma$, which is given as

$$
\gamma=\frac{1}{3}\pi^{2}k_{B}^{2}N(E_{F})(1+\lambda). \tag{2}
$$

![](./images/811166912649101312_8.jpg)

FIG. 8. The electron-phonon spectral function $\alpha^{2}\text{F}(\omega)$ (solid line) and the average electron-phonon coupling parameter $\lambda$ (dashed line) for $\text{Ba}M_2\text{P}_2$ ($M =$ Ni, Rh and Ir) superconductors.

The electron-phonon coupling constant $\lambda$ leads us to calculate the logarithmically averaged phonon frequency $\omega_{\text{ln}}$

$$
\omega_{\text{ln}} = \exp\left(2\lambda^{-1}\int_{0}^{\infty}\frac{d\omega}{\omega}\alpha^{2}F(\omega)\ln\omega\right). \tag{3}
$$

Finally, the superconducting transition temperature $T_{c}$ can be derived from the Allan-Dynes modification of the McMillian formula [38]

$$
T_{c} = \frac{\omega_{\text{ln}}}{1.2}\exp\left(-\frac{1.04(1+\lambda)}{\lambda-\mu^{*}(1+0.62\lambda)}\right), \tag{4}
$$

where $\mu^{*}$ represents an effective screened Coulomb repulsion constant. It is well known that the value of the

<table>
<caption>TABLE IV. The calculated parameters related to superconductivity in $\text{Ba}M_2$($M =$ Ni, Rh and Ir)$\text{P}_2$. The value of $\mu^{*}$ is equal to 0.13 for all the studied compounds.</caption>
<thead>
<tr>
<th>Compound</th>
<th>$N(E_{F})$ (States/eV)</th>
<th>$\omega_{\text{ln}}$(K)</th>
<th>$\lambda$</th>
<th>$T_{C}$ (K)</th>
<th>$\gamma\left(\frac{mJ}{molK^{2}}\right)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{BaNi}_{2}\text{P}_{2}$</td>
<td>3.64</td>
<td>163.10</td>
<td>0.61</td>
<td>2.80</td>
<td>13.80</td>
</tr>
<tr>
<td>Experimental [19]</td>
<td></td>
<td></td>
<td></td>
<td>3.0</td>
<td></td>
</tr>
<tr>
<td>Experimental [33]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>14</td>
</tr>
<tr>
<td>$\text{BaIr}_{2}\text{P}_{2}$</td>
<td>2.65</td>
<td>176.28</td>
<td>0.55</td>
<td>1.97</td>
<td>9.65</td>
</tr>
<tr>
<td>Experimental [25]</td>
<td></td>
<td></td>
<td></td>
<td>2.1</td>
<td>9.3</td>
</tr>
<tr>
<td>Experimental [32]</td>
<td></td>
<td></td>
<td></td>
<td>2.1</td>
<td>6.86</td>
</tr>
<tr>
<td>$\text{BaRh}_{2}\text{P}_{2}$</td>
<td>3.05</td>
<td>224.43</td>
<td>0.43</td>
<td>0.71</td>
<td>10.26</td>
</tr>
<tr>
<td>Experimental [25]</td>
<td></td>
<td></td>
<td></td>
<td>1.0</td>
<td>9.2</td>
</tr>
<tr>
<td>Experimental [32]</td>
<td></td>
<td></td>
<td></td>
<td>1.0</td>
<td>9.75</td>
</tr>
</tbody>
</table>

Coulomb pseudopotential ($\mu^{*}$) changes between 0.10 and 0.13 [38,41–46]. In our calculations, the value of $\mu^{*}$ is chosen to be 0.13. The calculated values of $N(E_{F})$, $\omega_{\text{ln}}$, $\lambda$, $T_{c}$, and $\gamma$ for the ternary phosphides $\text{Ba}M_2\text{P}_2$ are reported in Table IV, along with available experimental results [19,25,32]. In general, our calculated superconducting parameters for all the presently studied compounds compare very well with available experimental results [19,25,32]. In particular, the value of the superconducting transition temperature $T_{c}$ is found to be 2.80, 1.97, and 0.71 K for $\text{BaNi}_{2}\text{P}_{2}$, $\text{BaIr}_{2}\text{P}_{2}$, and $\text{BaRh}_{2}\text{P}_{2}$, respectively. These values are in gratifying accordance with their experimental values of 3.0, 2.1, and 1.0 K [19,25,32]. It is also interesting to see the value of $T_{c}$ for the ternary phosphides $\text{Ba}M_2\text{P}_2$ when the value of $(\mu^{*})$ is over the range of reasonable choices. When the value of $\mu^{*}$ is equal to 0.16, the value of the superconducting transition temperature $T_{c}$ is determined to be 2.17, 1.79, and 0.281 K for $\text{BaNi}_{2}\text{P}_{2}$, $\text{BaIr}_{2}\text{P}_{2}$, and $\text{BaRh}_{2}\text{P}_{2}$, respectively. This result shows that the value of $T_{c}$ for the ternary phosphides $\text{Ba}M_2\text{P}_2$ decreases when the value of $(\mu^{*})$ is over the range of reasonable choice.

Now, it will be meaningful to make a comparison between superconducting parameters of $\text{BaNi}_{2}\text{P}_{2}$ and its isostructural ternary phosphides $\text{BaIr}_{2}\text{P}_{2}$ and $\text{BaRh}_{2}\text{P}_{2}$. Before starting any discussion, we have to emphasize that the main effect on the value of $T_{c}$ for BCS-type superconductors comes from the strength of the electron-phonon coupling parameter $\lambda$. Furthermore, the density of states at the Fermi level ($N(E_{F})$) and the logarithmic average phonon frequency $\omega_{\text{ln}}$ may influence the value of $T_{c}$. As regards the electronic and phononic structures, the largest value of $N(E_{F})$ and the smallest value of $\omega_{\text{ln}}$ are found to be 3.64 states/eV and 163.10 K for $\text{BaNi}_{2}\text{P}_{2}$ which both increase the value of $\lambda$ according to the McMillan-Hopfield expression. As a result, the value of the electron-phonon coupling parameter for $\text{BaNi}_{2}\text{P}_{2}$ is larger than the corresponding parameter for $\text{BaIr}_{2}\text{P}_{2}$ and $\text{BaRh}_{2}\text{P}_{2}$. Thus, $\text{BaNi}_{2}\text{P}_{2}$ shows superconductivity with a higher superconducting critical temperature $T_{c}$ than the other ternary phosphides. When comparing our results for $\text{BaIr}_{2}\text{P}_{2}$ and $\text{BaRh}_{2}\text{P}_{2}$, we see that the value of $N(E_{F})$ for $\text{BaRh}_{2}\text{P}_{2}$ is larger than that for $\text{BaIr}_{2}\text{P}_{2}$. However, the situation is opposite for their electron-phonon coupling parameters. This is linked to the hardening of logarithmically averaged phonon frequency

$\omega_{\text{ln}}$ for $\text{BaRh}_2\text{P}_2$ which reduces the electron-phonon coupling parameter of this material according to the McMillan-Hopfield expression. Accordingly, the value of $T_c$ for $\text{BaIr}_2\text{P}_2$ is nearly three times larger than that for $\text{BaRh}_2\text{P}_2$ due to the larger electron-phonon coupling parameter of the former as compared to that of the latter.

## IV. SUMMARY

We have investigated the structural, electronic, and vibra- tional and the electron-phonon interaction properties of the ternary phosphides $\text{Ba}M_2\text{P}_2$ ($M =$ Ni, Rh and Ir) adopting the body-centered tetragonal $\text{ThCr}_2\text{Si}_2$ structure by using the generalized gradient approximation of the density functional theory and the plane wave $ab$ $initio$ pseudopotential method. Our calculated electronic structures can be described as a mixture of metallic, ionic and covalent contributions. These contributions are identified, respectively, to originate primary from $M$ $d$ and P $p$ states, due to a substantial charge transfer from the Ba atom to the $\text{MP}_4$ tetrahedra, and from the hybridization of the $M$ $d$ and P $p$ states.

The phonon spectrum in these materials shows a low- frequency region (LFR) and a high-frequency region (HFR), separated by a large gap of 2.3 THz for $\text{BaNi}_2\text{P}_2$, 3.7 THz for $\text{BaIr}_2\text{P}_2$, and 2.2 THz for $\text{BaRh}_2\text{P}_2$. A detailed examination of the Eliashberg function for these materials indicates that the acoustic and low-frequency optical phonon branches make a large contribution, within around 75%, to the average electron-phonon coupling parameter $\lambda$. The average electron- phonon coupling parameter is calculated to be 0.61, 0.55, and 0.43 for $\text{BaNi}_2\text{P}_2$, $\text{BaIr}_2\text{P}_2$, and $\text{BaRh}_2\text{P}_2$, respectively. These results indicate that all the studied ternary phosphides are phonon-mediated superconductors with medium electron- phonon coupling strength. Using the Allen-Dynes modified McMillian equation with the screened Coulomb pseudopoten- tial parameter $\mu^*=0.13$, the superconducting temperature is found to be 2.80 K for $\text{BaNi}_2\text{P}_2$, 1.97 K for $\text{BaIr}_2\text{P}_2$, and 0.70 K for $\text{BaRh}_2\text{P}_2$. These values are in good accordance with their experimental values of 3.0, 2.1, and 0.70 K, respectively.

## ACKNOWLEDGMENTS

This work was supported by the Scientific and Technical Research Council of Turkey (TÜBİTAK) (Project Number MFAG-114F192). Some of the calculations for this project were carried out using the computing facilities on the Intel Nehalem (i7) cluster (ceres) in the School of Physics, Univer- sity of Exeter, United Kingdom.

[1] P. Villars and L. D. Calvert, *Pearsons Handbook of Crys- tallographic Data for Intermetallic Phases*, 2nd ed. (ASM International, Materials Park, OH, 1991).
[2] F. Steglich, J. Aarts, C. D. Bredl, W. Lieke, D. Meschede, W. Franz, and H. Schäer, *Phys. Rev. Lett.* **43**, 1892 (1979).
[3] E. Morsen, B. D. Mosel, W. Müller-Warmuth, M. Reehuis, and W. Jeitschko, *J. Phys. Chem. Solids* **49**, 785 (1988).
[4] M. Reehuis and W. J. Jeitschko, *Phys. Chem. Solids* **51**, 961 (1990).
[5] T. Kanomata, T. Kawashima, T. Kaneko, H. Takahashi, and T. Mori, *Phys. Stat. Sol. (a)* **120**, K117 (1990).
[6] M. Reehuis, C. Ritter, R. Ballou, and W. Jeitschko, *J. Magn. Mater.* **138**, 85 (1994).
[7] Y. Jinhua, T. Shishido, T. Kimura, T. Matsumoto, and T. Fukuda, *Acta Crystallogr. C* **52**, 2652 (1996).
[8] T. Fukunara, K. Maezawa, H. Ohkuni, T. Kagayama, and G. Oomi, *Physica B* **230-232**, 198 (1997).
[9] A. Szytula, S. Baran, J. Leciejewicz, B. Peno, N. Stusser, Y. F. Ding, A. Zygmunt, and J. Zukrowski, *J. Phys.: Condens. Matter* **9**, 6781 (1997).
[10] O. Trovarelli, C. Geibel, S. Mederle, C. Langhammer, F. M. Grosche, P. Gegenwart, M. Lang, G. Sparn, and F. Steglich, *Phys. Rev. Lett.* **85**, 626 (2000).
[11] H. Q. Yuan, J. Singleton, F. F. Balakirev, S. A. Baily, G. F. Chen, J. L. Luo, and N. L. Wang, *Nature (London)* **457**, 565 (2009).
[12] P. Vilmercati, A. Fedorov, I. Vobornik, U. Manju, G. Panaccione, A. Goldoni, A. S. Sefat, M. A. McGuire, B. C. Sales, R. Jin, D. Mandrus, D. J. Singh, and N. Mannella, *Phys. Rev. B* **79**, 220503(R) (2009).
[13] W. Jeitschko, R. Glaum, and L. Boonk, *Solid State Chem.* **69**, 93 (1987).

[14] M. Rotter, M. Tegel, and D. Johrendt, *Phys. Rev. Lett.* **101**, 107006 (2008).
[15] F. Ronning, N. Kurita, E. D. Bauer, B. L. Scott, T. Park, T. Klimczuk, R. Movshovich, and J. D. Thompson, *J. Phys.: Condens. Matter* **20**, 342203 (2008).
[16] N. Kurita, F. Ronning, C. F. Miclea, E. D. Bauer, K. Gofryk, J. D. Thompson, and R. Movshovich, *Phys. Rev. B* **83**, 094527 (2011).
[17] I. R. Shein and A. L. Ivanovskii, *Phys. Rev. B* **79**, 054510 (2009).
[18] A. Subedi and D. J. Singh, *Phys. Rev. B* **78**, 132511 (2008).
[19] T. Mine, H. Yanagi, T. Kamiya, Y. Kamihara, M. Hirano, and H. Hosono, *Solid State Commun.* **147**, 111 (2008).
[20] V. Keimes, D. Johrendt, A. Mewis, C. Hujnt, and W. Schlabitz, *Z. Anorg. Allg. Chem.* **623**, 1699 (1997).
[21] T. Terashima, M. Kimata, H. Satsukawa, A. Harada, K. Hazama, M. Imai, S. Uji, H. Kito, A. Iyo, H. Eisaki, and H. Harima, *J. Phys. Soc. Jpn.* **78**, 033706 (2009).
[22] S. Ideta, T. Yoshida, M. Nakajima, W. Malaeb, H. Kito, H. Eisaki, A. Iyo, Y. Tomioka, T. Ito, K. Kihou, C. H. Lee, Y. Kotani, K. Ono, S. K. Mo, Z. Hussain, Z.-X. Shen, H. Harima, S. Uchida, and A. Fujimori, *Phys. Rev. B* **89**, 195138 (2014).
[23] D. S. Jayalakshmi and M. Sundareswari, *Indian J. Phys.* **89**, 201 (2015).
[24] I. B. Shameem Banu, M. Rajagopalan, Mohammed Yousuf, and P. Shenbagaraman, *J. Alloys Compd.* **288**, 88 (1999).
[25] N. Berry, C. Capan, G. Seyfarth, A. D. Bianchi, J. Ziller, and Z. Fisk, *Phys. Rev. B* **79**, 180502(R) (2009).
[26] D. Hirai, T. Takayama, R. Higashinaka, H. Aruga-Katori, and H. J. Takagi, *J. Phys. Soc. Jpn.* **78**, 023706 (2009).

054507-10

[27] A. Wurth, D. Johrendt, A. Mewis, C. Huhnt, G. Michels, M. Roepke, and W. Z. Schlabitz, *Anorg. Allg. Chem.* **623**, 1418 (1997).

[28] A. Löhken, C. Lux, D. Johrendt, and A. Z. Mewis, *Anorg. Allg. Chem.* **628**, 1472 (2002).

[29] I. B. Shameem Banu, M. Rajagopalan, and G. Vaitheeswaran, *Solid State Comm.* **116**, 451 (2000).

[30] I. R. Shein and A. L. Ivanovskii, *JETP Lett.* **89**, 357 (2009).

[31] E. Razzoli, M. Kobayashi, V. N. Strocov, B. Delley, Z. Bukowski, J. Karpinski, N. C. Plumb, M. Radovic, J. Chang, T. Schmitt, L. Patthey, J. Mesot, and M. Shi, *Phys. Rev. Lett.* **108**, 257005 (2012).

[32] D. Hirai, T. Takayama, D. Hashizume, R. Higashinakac, A. Yamamoto, H. A. Katori, and H. Takagi, *Physica C* **470**, S296 (2010).

[33] D. Hirai, F. vonRohr, and R. J. Cava, *Phys. Rev. B* **86**, 100505(R) (2012).

[34] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, *J. Phys.: Condens. Matter* **21**, 395502 (2009).

[35] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[36] R. Stumpf, X. Gonge, and M. Scheffler, *A List of Separable, Norm-conserving, Ab Initio Pseudopotentials* (Fritz-Haber- Institut, Berlin, 1990).

[37] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).

[38] P. B. Allen and R. C. Dynes, *Phys. Rev. B* **12**, 905 (1975).

[39] R. Bauer, A. Schmid, P. Pavone, and D. Strauch, *Phys. Rev. B* **57**, 11276 (1998).

[40] H. M. Tütüncü, H. Y. Uzunok, Ertuğrul Karaca, G. P. Srivastava, S. Özer, and Ş. Uğur, *Phys. Rev. B* **92**, 054510 (2015).

[41] P. Morel and P. W. Anderson, *Phys. Rev.* **125**, 1263 (1962).

[42] W. L. McMillan, *Phys. Rev.* **167**, 331 (1968).

[43] P. P. Singh, *Phys. Rev. B* **75**, 125101 (2007).

[44] I. Errea, M. Martinez-Canales, and A. Bergara, *Phys. Rev. B* **78**, 172501 (2008).

[45] E. Svanidze and E. Morosan, *Phys. Rev. B* **85**, 174514 (2012).

[46] B. Wiendlocha, M. J. Winiarski, M. Muras, C. Zvoriste-Walters, J.-C. Griveau, S. Heathman, M. Gazda, and T. Klimczuk, *Phys. Rev. B* **91**, 024509 (2015).