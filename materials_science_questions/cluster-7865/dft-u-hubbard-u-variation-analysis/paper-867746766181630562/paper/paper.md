# Long-range magnetic interaction and frustration in double perovskite $\text{Sr}_2\text{NiIrO}_6$

Xuedong Ou, Zhengwei Li, Fengren Fan, Hongbo Wang, and Hua Wu*

Laboratory for Computational Physical Sciences (MOE), State Key Laboratory of Surface Physics, and Department of Physics, Fudan University, Shanghai 200433, China
(Dated: today)

$\text{Sr}_2\text{NilrO}_6$ would be a ferromagnetic (FM) insulator in terms of the common superexchange mechanism between the first nearest neighboring (1NN) magnetic ions $\text{Ni}^{2+}$ $(t_{2g}^6e_g^2)$ and $\text{Ir}^{6+}$ $(t_{2g}^3)$. However, the observed antiferromagnetic (AF) order questions this viewpoint. In this work, we present first-principles calculations and find that while the 1NN $\text{Ni}^{2+}$-$\text{Ir}^{6+}$ exchange is indeed FM, the 2NN and 3NN couplings in the fcc Ir (and Ni) sublattice are AF. Moreover, the 2NN AF Ir-Ir coupling turns out to be even stronger than the 1NN FM Ni-Ir coupling, thus giving rise to a magnetic frustration. $\text{Sr}_2\text{NiIrO}_6$ hence becomes a distorted low-temperature antiferromagnet. Naturally, a very similar magnetic property in $\text{Sr}_2\text{ZnIrO}_6$ can be explained by the frustrated AF coupling in the fcc $\text{Ir}^{6+}$ sublattice. This work highlights the long-range magnetic interaction of the delocalized $5d$ electrons, and also addresses why the spin-orbit coupling is ineffective here.

PACS numbers: 75.25.Dk, 71.20.-b, 71.70.-d

## I. INTRODUCTION

In the insulating transition-metal (TM) oxides, superexchange (SE) coupling of neighboring magnetic ions via intermediate oxygen, according to the Goodenough-Kanamori-Anderson rules$^1$, commonly plays a leading role in their magnetic order. One simple but useful rule is that for a linear $M$-$O$-$M'$ exchange path, the SE would be antiferromagnetic (AF) [ferromagnetic (FM)] when the active orbitals of $M$ and $M'$ are same [different]. Fig. 1(a) shows two $d^1$ ions each having two orthogonal A-B levels and the same A-level occupation. Taking into account an effective hopping $t$ between two ions associated with the charge fluctuation $(d^1 + d^1 \to d^0 + d^2)$ where the electron correlation Hubbard $U$ is involved, an energy gain of an AF order (relative to a FM one) is proportional to $t^2/U$ in a strong correlation limit ($U \gg t$). Fig. 1(b) shows two different $d^1$ level occupations, and a FM stability against AF is proportional to $t^2J_{\text{H}}/U^2$ where $J_{\text{H}}$ is a Hund exchange. This is the reason why a FM Mott insulator is often associated with orbital physics (e.g., an orbital ordering) and its $T_{\text{C}}$ is much lower (due to the factor $J_{\text{H}}/U \sim 1/5$) than the $T_{\text{N}}$ of many AF Mott insulators.

In practice, it is often sufficient to consider the SE between the nearest neighboring (NN) magnetic ions only. This approach applies with much success to numerous insulating $3d$ TM oxides, where the $3d$ electrons are quite localized due to the strong correlation effect. In recent years, $5d$ TM oxides have received considerable attention due to their significant spin-orbit coupling (SOC) effect and possibly exotic properties$^{2-10}$. The hybrid $3d$-$5d$ TM oxides are also of current great interest for exploration of novel magnetic and electronic properties in this material system, in which new SOC effects add to the common charge-spin-orbital physics appearing in the $3d$ TM oxides. Among them, the double perovskites $A_2BB'O_6$ ($A$ = alkaline earth metal, $B = 3d$ TM, and $B' = 5d$ TM) are an important material platform$^{11-22}$: $\text{Sr}_2\text{FeReO}_6$ is an above room temperature (RT) ferrimagnetic half metal$^{11}$, and $\text{Sr}_2\text{CrOsO}_4$ is a ferrimagnetic insulator with a seemingly highest $T_{\text{C}}$ in the perovskite oxides$^{13,14}$, etc. As $5d$ electrons are moderately or weakly correlated and their orbitals are much delocalized, their magnetic coupling could well be a long-range interaction.

In this work, we study the electronic structure and magnetism of the newly synthesized double perovskite $\text{Sr}_2\text{NiIrO}_6$,$^{17}$ using density functional calculations. This material crystallizes in the monoclinic space group $P2_1/n$ at RT (see Fig. 2) and undergoes two structural phase transitions ($P2_1/n \to I4/m \to Fm\overline{3}m$) upon heating. Magnetic susceptibility measurements$^{17}$ suggest the establishment of AF interactions at $T_{\text{N}} = 58$ K. This oxide has the $\text{Ni}^{2+}$ $(t_{2g}^6e_g^2)$-$\text{Ir}^{6+}$ $(t_{2g}^3)$ charge state as seen below. Taking into account a charge fluctuation into the common $\text{Ni}^{3+}$-$\text{Ir}^{5+}$ state (a reverse $\text{Ni}^+$-$\text{Ir}^{7+}$ is quite unusual), both the Ni up-spin $e_g$ and down-spin $t_{2g}$ electron hopping (the Ni up-spin $t_{2g}$ levels lie lowest due to the crystal field splitting and Hund exchange) would give a FM SE between the $\text{Ni}^{2+}$ and $\text{Ir}^{6+}$ ions, see Figs. 1(c)

![](./images/867746766181630562_1.jpg)

FIG. 1: (a) AF and (b) FM SE between two two-level $d^1$ ions. (c) and (d): $\text{Sr}_2\text{NilrO}_6$ would be FM, according to the SE between the NN $\text{Ni}^{2+}$ and $\text{Ir}^{6+}$ ions. (d) and (e): AF SE in the fcc $\text{Ir}^{6+}$ sublattice.

![](./images/867746766181630562_2.jpg)

FIG. 2: (Color online) Double perovskite structure of Sr₂NiIrO₆. The Ni and Ir ions form their respective fcc sublattices.

and 1(d). As the $e_g$ and $t_{2g}$ levels are orthogonal, the $e_g$ ($t_{2g}$) electron hopping follows the simple SE mechanism plotted in Fig. 1(b) [Fig. 1(a)]. Apparently, this expected FM order contradicts the observed AF in Sr₂NiIrO₆, and thus consideration of only NN Ni²⁺-Ir⁶⁺ coupling would be a mistake here. Then, a possibly long-ranged Ir-Ir coupling within the fcc sublattice should be invoked, which would be AF due to the half-filled $t_{2g}^3$ shells [Figs. 1(d) and 1(e)]. As we calculate below, there is indeed a long-range AF interaction in the fcc Ir⁶⁺ sublattice, and the second NN Ir-Ir AF coupling energy is even bigger than the first NN Ni-Ir FM one, thus giving rise to a magnetic frustration. As a result, Sr₂NiIrO₆ behaves as a distorted low-temperature antiferromagnet¹⁷. Naturally, the frustrated AF couplings in the fcc Ir⁶⁺ sublattice explain a very similar magnetic property in the isostructural Sr₂ZnIrO₆.¹⁷ Note that one could take care of long-range magnetic interaction of the delocalized 5d electrons.

## II. COMPUTATIONAL DETAILS

Our calculations were performed using the full-potential augmented plane waves plus local orbital method (WIEN2K code)²³. We took the structure data of Sr₂NiIrO₆ measured by neutron diffraction at RT¹⁷. The muffin-tin sphere radii are chosen to be 2.8, 2.1, and 1.5 Bohr for Sr, Ni/Ir, and O atoms, respectively. The cutoff energy of 16 Ry is used for plane wave expansion of interstitial wave functions, and 6×6×4 $\mathbf{k}$ mesh for integration over the Brillouin zone, both of which ensure a sufficient numerical accuracy. SOC is included by the second-variational method with scalar relativistic wave functions. We employ the local spin density approximation plus Hubbard $U$ (LSDA+$U$) method²⁴ and use the typical values, $U = 6$ eV and $J_{\text{H}} = 0.9$ eV ($U = 2$ eV and $J_{\text{H}} = 0.4$ eV), to describe electron correlation of the Ni 3d (Ir 5d) electrons. The calculated Mott insulating state of Sr₂NiIrO₆ remains unchanged in a reasonable range of the $U$ values ($U = 4$-$8$ eV for Ni 3d and $U = 1$-$3$ eV for Ir 5d), and the corresponding variation of 1-2 meV for the exchange energy parameters does not affect our discussion and conclusion about the frustrated magnetism.

![](./images/867746766181630562_3.jpg)

FIG. 3: (Color online) Ir 5d and Ni 3d DOS of Sr₂NiIrO₆ calculated by LSDA for the FM state. The solid red (thin blue) curves stand for the up (down) spin channel. Fermi level is set at zero energy. Sr₂NiIrO₆ has the Ni²⁺ ($t_{2g}^6 e_g^2$)-Ir⁶⁺ ($t_{2g}^3$) charge state.

## III. RESULTS AND DISCUSSION

We first study the electronic structure of Sr₂NiIrO₆ and the Ni-Ir charge state. Fig. 3 shows the orbitally resolved density of states (DOS) calculated by LSDA for the FM state. The delocalized Ir 5d electrons have a strong covalency with the ligand oxygens, giving rise to a large bonding-antibonding splitting. The $pd\sigma$ splitting of the Ir $e_g$ electrons is up to 9 eV, and the $pd\pi$ splitting of the Ir $t_{2g}$ electrons is about 6 eV. The Ir 5d electrons have a $t_{2g}$-$e_g$ crystal-field splitting of more than 3 eV. Besides the occupied bonding states (around -6 eV) ascribed to the lower-lying O 2p bands, only the up-spin Ir $t_{2g}$ state is occupied, giving a formal Ir⁶⁺ charge state with a $t_{2g}^3$ ($S = 3/2$) configuration. In contrast, the Ni 3d electrons are confined and have a smaller $pd\sigma$ ($pd\pi$) bonding-antibonding splitting of 4 eV (2 eV) and the $t_{2g}$-$e_g$ crystal-field splitting of 1-1.5 eV. Only the down-spin Ni $e_g$ antibonding state is unoccupied, giving a formal Ni²⁺ charge state with the $t_{2g}^6 e_g^2$ ($S = 1$) configuration. Therefore, Sr₂NiIrO₆ has the Ni²⁺-Ir⁶⁺ charge state. Its closed subshells and a finite electron correlation would certainly make Sr₂NiIrO₆ insulating. However, in the present LSDA calculation, the bandwidth of the Ir $t_{2g}$

![](./images/867746766181630562_4.jpg)

FIG. 4: (Color online) Insulating band structure of $Sr_2NiIrO_6$ in the $Ni^{2+}$ $(t_{2g}^6e_g^2)$-$Ir^{6+}$ $(t_{2g}^3)$ charge state calculated by LSDA+$U$ for the FM state. Other magnetic states have a very similar band structure.

electrons is slightly larger than the exchange splitting, making the Ir $t_{2g}$ bands of two spin directions somewhat overlapping at the Fermi level. As seen below, this metallic solution will turn into a Mott insulating one upon inclusion of the electron correlation.

We now include the static electron correlation by carrying out LSDA+$U$ calculations. The insulating band structure is shown in Fig. 4. It has a small band gap of 0.3 eV within the Ir $t_{2g}$ bands due to the moderate electron correlation of the delocalized Ir $5d$ electrons. The Ni $3d$ bands have a gap of more than 2 eV due to the strong correlation. The electron correlation enhances electron localization and reduces band hybridization and further stabilizes the $Ni^{2+}$-$Ir^{6+}$ charge state$^{25}$. The $Ni^{2+}$ ($S = 1$) ion has a spin moment of $1.76\ \mu_B$ (see Table I), being close to its formal value of $2\ \mu_B$. The $Ir^{6+}$ ($S = 3/2$) ion has a smaller moment of $1.46\ \mu_B$ reduced by the strong covalency with the oxygen ligands.

As both the $Ni^{2+}$ and $Ir^{6+}$ ions are magnetic and form their respective fcc sublattices, their magnetic interactions are of concern. Here we study different magnetic structures using LSDA+$U$ calculations. The G-AF state of $Sr_2NilrO_6$ (FM $Ni^{2+}$ and $Ir^{6+}$ sublattices being AF coupled) turns out to be less stable than the FM state by 89 meV/fu, see Table I. As the FM and G-AF states differ in the exchange energy only by the 1NN Ni-Ir couplings, which are $\pm 6J_{Ni-Ir}$ per formula unit. Then the average exchange energy parameter of the 1NN Ni-Ir pairs can be estimated to be $J_{Ni-Ir} = -89/12 \approx -7.4$ meV. This FM Ni-Ir coupling is readily understood by a SE mechanism, see Fig. 1 and the Introduction. However, the observed AF interaction$^{17}$ at $T_N = 58$ K questions this description. Therefore, we are motivated to study the long-range magnetic interactions, particularly associated with the delocalized Ir $5d$ electrons. To do so, we use two artificial systems with either $Ir^{6+}$ or $Ni^{2+}$ magnetic sublattice only, $Sr_2ZnIrO_6$ [i.e., $Sr_2Zn(Ni)IrO_6$ in Table I] and $La_2NiSiO_6$ both in the $Sr_2NilrO_6$ structure, to calculate the 2NN $Ir^{6+}$-$Ir^{6+}$ and $Ni^{2+}$-$Ni^{2+}$ exchange parameters ($J'_{Ir-Ir}$ and $J'_{Ni-Ni}$ with a reference to the 1NN $J_{Ni-Ir}$). This approach avoids choices of complicate magnetic structures in bigger supercells, and allows to estimate the two parameters separately. For $Sr_2Zn(Ni)IrO_6$, the layered AF state (FM $ab$ planes being AF alternate along the $c$ axis, see also Fig. 2) is more stable than the FM state by 84 meV/fu, see Table I. The layered AF and FM states differ in the exchange energy only by the 2NN Ir-Ir couplings (with a reference to the 1NN Ni-Ir ones), i.e., $-2J'_{Ir-Ir}$ $vs$ $6J'_{Ir-Ir}$. Then the energy difference gives AF $J'_{Ir-Ir} = 84/8 = 10.5$ meV. The corresponding energy difference of 19 meV/fu for $La_2NiSiO_6$ gives AF $J'_{Ni-Ni} = 19/8 \approx 2.4$ meV, see Table I.

As the magnetic $Ir^{6+}$ and $Ni^{2+}$ ions have closed subshells, the SE interactions naturally explain the AF $J'_{Ir-Ir}$ and $J'_{Ni-Ni}$. Note that the $Ni^{2+}$ $3d$ electrons are confined but the $Ir^{6+}$ $5d$ electrons are delocalized, it is therefore not surprising that $J'_{Ir-Ir}$ is about four times as big as $J'_{Ni-Ni}$. However, it is a bit surprising that the 2NN AF $J'_{Ir-Ir}$ is even bigger than the 1NN FM $J_{Ni-Ir}$, thus giving rise to a magnetic frustration in $Sr_2NilrO_6$. This vital role of the strong 2NN AF Ir-Ir coupling is also manifested in the real double perovskite $Sr_2ZnIrO_6$, see

$Sr_2ZnIrO_6$ has a very similar crystal structure and magnetic property to $Sr_2NilrO_6$, and it has AF interactions at $T_N = 46$ K.$^{17}$ We have also calculated different magnetic states of $Sr_2ZnIrO_6$ and find the 2NN AF $J'_{Ir-Ir} = 75/8 \approx 9.4$ meV (see Table I), being close to $J'_{Ir-Ir} =$

<table>
<caption>TABLE I: Relative total energies $\Delta E$ (meV/fu) and spin moments $M$ (in unit of $\mu_B$) calculated by LSDA+$U$ for different systems in different magnetic states. The Ir-Ir magnetic interactions are estimated for $Sr_2ZnIrO_6$ either in $Sr_2NilrO_6$ structure (Zn substitution for Ni) or in its real structure$^{17}$. The Ni-Ni exchange coupling is estimated using the artificial $La_2NiSiO_6$ in $Sr_2NilrO_6$ structure. The derived exchange energy parameters (meV) for the 1NN Ni-Ir, 2NN Ir-Ir and Ni-Ni, and 3NN Ir-Ir pairs are listed in the last two lines.</caption>
<thead>
<tr>
<th>System</th>
<th>Magn.</th>
<th>$\Delta E$</th>
<th>$M$ (Ni$^{2+}$/Ir$^{6+}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Sr_2NilrO_6$</td>
<td>FM</td>
<td>0</td>
<td>1.76/1.46</td>
</tr>
<tr>
<td></td>
<td>G-AF</td>
<td>89</td>
<td>1.64/1.28</td>
</tr>
<tr>
<td>$Sr_2Zn(Ni)IrO_6$</td>
<td>FM</td>
<td>0</td>
<td>/1.39</td>
</tr>
<tr>
<td></td>
<td>layered AF</td>
<td>-84</td>
<td>/1.31</td>
</tr>
<tr>
<td>$La_2NiSiO_6$</td>
<td>FM</td>
<td>0</td>
<td>1.70/</td>
</tr>
<tr>
<td></td>
<td>layered AF</td>
<td>-19</td>
<td>1.69/</td>
</tr>
<tr>
<td>$Sr_2ZnIrO_6$</td>
<td>FM</td>
<td>0</td>
<td>/1.42</td>
</tr>
<tr>
<td></td>
<td>layered AF</td>
<td>-75</td>
<td>/1.34</td>
</tr>
<tr>
<td></td>
<td>bilayered AF</td>
<td>-42</td>
<td>/1.36</td>
</tr>
<tr>
<td>$J_{Ni-Ir}$</td>
<td>$J'_{Ir-Ir}$</td>
<td>$J'_{Ni-Ni}$</td>
<td>$J''_{Ir-Ir}$</td>
</tr>
<tr>
<td>-7.4</td>
<td>9.4, 10.5</td>
<td>2.4</td>
<td>2.2</td>
</tr>
</tbody>
</table>

![](./images/867746766181630562_5.jpg)

FIG. 5: (Color online) The LDA+SOC calculated $Ir^{6+}$ $t_{2g}$ DOS projected onto the SOC basis set, the $J=3/2$ quartet (solid red curves) and the $J=1/2$ doublet (dashed blue curves). (a) In $Sr_{2}ZnIrO_{6}$, the overall mixing of the $J=3/2$ and $J=1/2$ states is due to the band formation of the delocalized Ir $5d$ electrons in the fcc Ir sublattice with twelve Ir-Ir coordination. (b) The SOC splitting of about 0.5 eV between the $J=3/2$ and the $J=1/2$ states is restored upon the reduction of the Ir-Ir coordination to four, which is modeled in the artificial system $Sr_{2}GaIr_{0.5}Si_{0.5}O_{6}$ (in $Sr_{2}ZnIrO_{6}$ structure) with alternating GaIr and SiGa planes.

10.5 meV in $Sr_{2}NiIrO_{6}$. As the delocalized Ir $5d$ electrons produce a long-range magnetic interaction, we also estimate the 3NN AF $J''_{Ir-Ir}$ (the exchange path along the linear Ir-O-Ni-O-Ir bonds with the Ir-Ir distance of 7.8 Å) by calculating the bilayered AF state of $Sr_{2}ZnIrO_{6}$. The bilayered AF state has FM $ab$ planes but AF alternation every bilayer along the $c$ axis, and it is more stable than the FM state by 42 meV/fu. The exchange energy per formula unit can be expressed as $6J'_{Ir-Ir}+3J''_{Ir-Ir}$ for the FM state and $2J'_{Ir-Ir}+J''_{Ir-Ir}$ for the bilayered AF state. Therefore, the AF $J''_{Ir-Ir}$ is estimated to be $(42-4\times9.4)/2=2.2$ meV.

As seen from the above results, apparently the Ir-Ir magnetic interactions are long-ranged and have a non-negligible strength even at a distance of about 8 Å. It is the long-range AF interactions of the $Ir^{6+}$ sublattice which make $Sr_{2}ZnIrO_{6}$ magnetically frustrated. It is the strongest 2NN AF $J'_{Ir-Ir}$ which overwhelms the 1NN FM $J_{Ni-Ir}$ and also makes $Sr_{2}NiIrO_{6}$ magnetically frustrated. In a word, the long-range magnetic interactions and frustration would make the cubic double perovskites $Sr_{2}NiIrO_{6}$ and $Sr_{2}ZnIrO_{6}$ distorted, and this would partially relieve the magnetic frustration and eventually stabilize them into a very similar low-temperature antiferromagnet as experimentally observed$^{17}$.

Finally, we check if the SOC is important or not in the present materials. Normally, SOC is important in heavy $5d$ TMs, and particularly, iridates recently receive great interest$^{2-10}$. Owing to a large crystal-field splitting, iridates are in a low-spin state with only the $t_{2g}$ occupation (e.g., in a cubic crystal field). Then the SOC splits the $t_{2g}$ triplet (with 2-fold spin degeneracy) into the lower $J=3/2$ quartet and the higher $J=1/2$ doublet$^{2,3}$. We have used this SOC basis set to project the $Ir^{6+}$ $t_{2g}$ DOS of $Sr_{2}ZnIrO_{6}$ calculated by LDA+SOC, but we find that the $J=3/2$ and the $J=1/2$ states are completely mixed, see Fig. 5(a). Therefore, the $J=3/2$ and the $J=1/2$ states are not at all eigen orbitals in $Sr_{2}ZnIrO_{6}$ (and in $Sr_{2}NiIrO_{6}$ with the same fcc $Ir^{6+}$ sublattice). This is because the delocalized Ir $5d$ electrons form, with the intersite electron hoppings in the fcc sublattice (the high coordination of twelve), a 'broad' band with its bandwidth being more than 1 eV. Then the SOC effect is 'killed'. In contrast, if the Ir-Ir coordination number is reduced as in the low-dimensional iridates, the SOC effect would be manifested. To check this, we also calculate the artificial system $Sr_{2}GaIr_{0.5}Si_{0.5}O_{6}$ (in $Sr_{2}ZnIrO_{6}$ structure) with alternating GaIr and SiGa planes. The $Ga^{3+}$, $Ir^{6+}$ and $Si^{4+}$ ions have well comparable ionic sizes, and they make charge balanced and the $Ir^{6+}$-$Ir^{6+}$ ions only four-coordinated. In this case, the SOC splitting of about 0.5 eV between the $J=3/2$ and the $J=1/2$ states is well restored as seen in Fig. 5(b), and thus the $J=3/2$ and the $J=1/2$ states would serve as eigen orbitals in a good approximation$^{8}$.

The above results show that in $Sr_{2}ZnIrO_{6}$ and $Sr_{2}NiIrO_{6}$, the delocalized $Ir^{6+}$ $5d$ electrons have an insignificant SOC effect due to the band formation in the fcc sublattice. Moreover, the half filled $t_{2g}^{3}$ subshell of the high-valence $Ir^{6+}$ ion has an intrinsic exchange splitting of about 1 eV, see Fig. 3. Both the band effect and the exchange splitting are stronger than the SOC strength, making the SOC ineffective in $Sr_{2}NiIrO_{6}$ and $Sr_{2}ZnIrO_{6}$. Our LSDA+U+SOC test calculations indeed show that the $Ir^{6+}$ ion has only a small orbital moment of 0.07 $\mu_{B}$, being antiparallel to the spin moment of about 1.3 $\mu_{B}$ reduced from the formal $S=3/2$. Therefore, both $Sr_{2}ZnIrO_{6}$ and $Sr_{2}NiIrO_{6}$ can be described as an $Ir^{6+}$ $S=3/2$ fcc frustrated system, although $Sr_{2}NiIrO_{6}$ itself has an appreciable $Ni^{2+}$-$Ir^{6+}$ FM coupling.

## IV. CONCLUSION

In summary, using density functional calculations, we find that the newly synthesized isostructural double perovskites $Sr_{2}NiIrO_{6}$ and $Sr_{2}ZnIrO_{6}$ are insulating and have the formal $Ir^{6+}$ $S=3/2$ fcc sublattice, in addition to the $Ni^{2+}$ $S=1$ sublattice in the former. The delocalized Ir $5d$ electrons produce long-range magnetic interactions, and the 2NN Ir-Ir AF interaction turns out to be even stronger than the 1NN Ni-Ir FM interaction. Therefore, the leading AF interactions in the fcc Ir sublattice give rise to a magnetic frustration in both $Sr_{2}NiIrO_{6}$ and $Sr_{2}ZnIrO_{6}$. As a result, both the cubic compounds appear as a distorted low-temperature antiferromagnet. Note that the band formation in the high-coordination fcc Ir sublattice and the exchange splitting of the high-valence $Ir^{6+}$ ion both make the

SOC ineffective, and the long-range interactions of the delocalized $5d$ electrons (band formation and magnetic coupling) would be taken care of.

Acknowledgment. This work was supported by the NSF of China (Grant Nos. 11274070 and 11474059), MOE Grant No. 20120071110006, and ShuGuang Pro- gram of Shanghai (Grant No. 12SG06).

* Corresponding author: wuh@fudan.edu.cn
1 J. B. Goodenough, in *Magnetism and the Chemical Bond* (Interscience Publishers, New York-London, 1963).
2 B. J. Kim, Hosub Jin, S. J. Moon, J.-Y. Kim, B.-G. Park, C. S. Leem, J. Yu, T. W. Noh, C. Kim, S.-J. Oh, J.-H. Park, V. Durairaj, G. Cao, and E. Rotenberg, Phys. Rev. Lett. 101, 076402 (2008).
3 B. J. Kim, H. Ohsumi, T. Komesu, S. Sakai, T. Morita, H. Takagi, and T. Arima, Science 323, 1329 (2009).
4 G. Jackeli and G. Khaliullin, Phys. Rev. Lett. 102, 017205 (2009).
5 X. G. Wan, A. M. Turner, A. Vishwanath, and S. Y. Savrasov, Phys. Rev. B 83, 205101 (2011).
6 I. I. Mazin, Harald O. Jeschke, K. Foyevtsova, Roser Va- lentí, and D. I. Khomskii, Phys. Rev. Lett. 109, 197201 (2012).
7 W. G. Yin, X. Liu, A. M. Tsvelik, M. P. M. Dean, M. H. Upton, J. Kim, D. Casa, A. Said, T. Gog, T. F. Qi, G. Cao, and J. P. Hill, Phys. Rev. Lett. 111, 057202 (2013).
8 X. Ou and H. Wu, Phys. Rev. B 89, 035138 (2014).
9 X. Ou and H. Wu, Sci. Rep. 4, 4609 (2014).
10 G. Cao, T. F. Qi, L. Li, J. Terzic, S. J. Yuan, L. E. DeLong, G. Murthy, and R. K. Kaul, Phys. Rev. Lett. 112, 056402 (2014).
11 K.-I. Kobayashi, T. Kimura, Y. Tomioka, H. Sawada, K. Terakura, and Y. Tokura, Phys. Rev. B 59, 11159 (1999).
12 D. Serrate, J. M. De Teresa, and M. R. Ibarra, J. Phys. Condens. Matter 19, 023201 (2007).
13 Y. Krockenberger, K. Mogare, M. Reehuis, M. Tovar, M. Jansen, G. Vaitheeswaran, V. Kanchana, F. Bultmark, A. Delin, F. Wilhelm, A. Rogalev, A. Winkler, and L. Alff, Phys. Rev. B 75, 020404(R) (2007).
14 O. N. Meetei, O. Erten, M. Randeria, N. Trivedi, and P. Woodward, Phys. Rev. Lett. 110, 087203 (2013).
15 A. K. Paul, M. Reehuis, V. Ksenofontov, B. Yan, A. Hoser, D. M. Többens, P. M. Abdala, P. Adler, M. Jansen, and C. Felser, Phys. Rev. Lett. 111, 167205 (2013).
16 R. Morrow, R. Mishra, O. D. Restrepo, M. R. Ball, W. Windl, S. Wurmehl, U. Stockert, B. Büchner, and P. M. Woodward, J. Am. Chem. Soc. 135, 18824 (2013).
17 P. Kayser, M. J. Martínez-Lope, J. A. Alonso, M. Retuerto, M. Croft, A. Ignatov, and M. T. Fernández-Díaz, Inorg. Chem. 52, 11013 (2013).
18 B. Yan, A. K. Paul, S. Kanungo, M. Reehuis, A. Hoser, D. M. Többens, W. Schnelle, R. C. Williams, T. Lancaster, F. Xiao, J. S. Möller, S. J. Blundell, W. Hayes, C. Felser, and M. Jansen, Phys. Rev. Lett. 112, 147202 (2014).
19 H. L. Feng, M. Arai, Y. Matsushita, Y. Tsujimoto, Y. Guo, C. I. Sathish, X. Wang, Y. H. Yuan, M. Tanaka, and K. Yamaura, J. Am. Chem. Soc. 136, 3326 (2014).
20 R. Morrow, J. W. Freeland, and P. M. Woodward, Inorg. Chem. 53, 7983 (2014).
21 H. Wang, S. Zhu, X. Ou, and H. Wu, Phys. Rev. B 90, 054406 (2014).
22 S. Kanungo, B. Yan, M. Jansen, and C. Felser, Phys. Rev. B 89, 214414 (2014).
23 P. Blaha, K. Schwarz, G. Madsen, D. Kvasnicka, and J. Luitz, WIEN2k, 2001. ISBN 3-9501031-1-2.
24 V. I. Anisimov, I. V. Solovyev, M. A. Korotin, M. T. Czyżyk, and G. A. Sawatzky, Phys. Rev. B 48, 16929 (1993).
25 We also test the $Ni^{3+}$-$Ir^{5+}$ state, using constrained LSDA+$U$ calculations. We initialize the corresponding oc- cupation number matrix and the orbital polarized poten- tial, and consider a possible $J=0$ singlet state of the $Ir^{5+}$ ion due to its strong SOC. After a full electronic relax- ation, however, the self-consistent LSDA+$U$+SOC calcu- lations converge also to the $Ni^{2+}$-$Ir^{6+}$ state as reported in the main text.