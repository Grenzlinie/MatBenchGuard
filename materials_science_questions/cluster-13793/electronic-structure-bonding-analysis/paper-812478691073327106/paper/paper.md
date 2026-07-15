# Activation free energies for formation and dissociation of N-N, C-C, and C-H bonds in a Na-Ga melt

Takahiro Kawamura $^{a,b,*}$, Masayuki Imanishi $^{b}$, Masashi Yoshimura $^{b}$, Yusuke Mori $^{b}$, Yoshitada Morikawa $^{b}$

$^{a}$ Graduate School of Engineering, Mie University, 1577 Kurimamachiya-cho, Tsu 514-8507, Japan
$^{b}$ Graduate School of Engineering, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan

---

## ARTICLE INFO

**Keywords:**
First-principles calculation
Gallium nitride
Graphene
Solution
Catalyst

## ABSTRACT

Bonding energies of N-N, C-C, and C-H in Na-Ga melts and C-H in Ga melts were investigated using first-principles calculations. Activation free energies for formation and dissociation of the above bonds were estimated via the blue-moon ensemble method using constrained molecular dynamics simulations. The dissociation activation energies of the N-N, C-C, and C-H bonds in the Na-Ga melt were about 1.13, 2.71, and 1.58 eV, respectively, and that of the C-H bond in the Ga melt was about 1.40 eV.

---

## 1. Introduction

Formation and dissociation energies of related atomic bonds in crystal growth environments are important for investigating the crystal growth mechanism, especially when solution growth includes additives or the solution acts as a catalyst [1,2] for decomposing raw materials. This is because atomic bonding states change according to their surrounding environment. Carbon additives improve the growth rate of Na-flux GaN growth [3] and suppress polycrystal generation [4-6]. We previously found that formation and dissociation of the C-N bond strongly affects the mechanism for enhanced GaN growth via C addition [7-9]. Other additives, such as Li, Ca, Sr, and Ba, also enhance the growth rate and crystal quality [10-13]. For SiC solution growth, Si-Fe, Si-Ti, and Si-Cr alloy melts are used as solvents to increase C solubility [14-16]. In addition, Al and Sn additives suppress surface roughening and polytype instability [17]. Recently, graphene growth with methane (CH₄) and molten Ga at low temperature (50-500 °C) was reported, where molten Ga acts as a catalyst for decomposing CH₄ [18].

In this study, we addressed the atomic bondings related to C-added Na-flux GaN growth and graphene growth with CH₄ and molten Ga. Using first-principles calculations, we investigated the bonding energies of N-N, C-C, and C-H in Na-Ga melts and that of C-H in Ga melts. Investigations of the N-N, C-C, and C-H bondings in Na-Ga melts relate to dissociation of N₂ and C additives in the Na-Ga melt, and that of the C-H bonding in Ga melts focused on the function of Ga melt as a catalyst for decomposing CH₄. Activation free energies for formation and dissociation of the above bonds were estimated via the blue-moon ensemble method [19,20] using constrained molecular dynamics (MD) simulations.

## 2. Simulation methods

We used the first-principles MD simulation program STATE-Senri (Simulation Tool for Atom TEchnology), which is based on density functional theory with norm-conserving/ultrasoft pseudopotentials and plane-wave basis sets [21]. Ultrasoft pseudopotentials were used for the H 1s, while norm-conserving pseudopotentials were used for other states. Ga 3d electrons were treated by partial core correction [22]. We used the generalized gradient approximation of Perdew et al. for the exchange-correlation function (PBE) [23]. The cutoff energies for the wave functions and charge densities were 25 and 225 Ry, respectively.

We calculated the activation free energies for formation and dissociation of (i) N-N, C-C, and C-H bonds in a Na and a Na-Ga melt and (ii) C-H bonds in a Ga melt. The calculations for (i) were related to C-added Na-flux GaN growth [4-6], and those for (ii) were related to graphene growth with CH₄ in a Ga melt [18]. For (i), we used two simulation models composed of about 54 atoms: Na and Na-Ga (Na:Ga ≈ 4:1) melts. Two N atoms and two C atoms were included in the simulation models for the N-N and C-C bond calculations, respectively. Fig. 1(a) and (b) show simulation snapshots of the atomic coordinates of the N-N and C-C

---

* Corresponding author at: Graduate School of Engineering, Mie University, 1577 Kurimamachiya-cho, Tsu 514-8507, Japan.
E-mail address: tkawamura@mach.mie-u.ac.jp (T. Kawamura).

https://doi.org/10.1016/j.commatsci.2021.110366
Received 23 September 2020; Received in revised form 2 February 2021; Accepted 3 February 2021
Available online 5 April 2021
0927-0256/© 2021 Elsevier B.V. All rights reserved.

![](./images/812478691073327106_1.jpg)

Fig. 1. Simulation snapshots of atomic coordinates of the (a) N-N and (b) C-C bond in the Na-Ga melts. Purple, blue, gray, and yellow balls represent Ga, Na, N, and C atoms, respectively.

![](./images/812478691073327106_2.jpg)

Fig. 2. Radial distribution functions of the Na-Ga melt with two N atoms with a N-N bond length of 1.2 Å.

bonds in the Na-Ga melts, respectively. These figures were generated using the visualization program XCrysDen [24]. A set of C and H atoms (CH) or a CH₄ molecule was included in the simulation models for the C-H bond calculations. The size of the simulation cells was about 12.6 × 12.6 × 12.6 Å³, which was based on the density of Na. Periodic boundary conditions were used in all axial directions. The simulation temperature was set to 1073 K, which is the typical temperature for GaN growth. For the calculations for (ii), we used Ga melt models consisting of 53 Ga atoms and a CH₄ molecule. The sizes of the simulation cells were about 10.1 × 10.1 × 10.1 Å³ at 373 K (100 °C) and 10.2 × 10.2 × 10.2 Å³ at 673 K (400 °C), which were based on the density of Ga melt [25].

The calculation procedure is described below taking the N-N bond calculation as an example. We performed constrained MD simulations for 10 ps at 1073 K and at constant volume. The number of k-points for Brillouin zone sampling was 1 × 1 × 1. Because the MD simulations need a long simulation time and strict accuracy is not required, we used the small number of k-points. The N-N interatomic distances were constrained to set values from 1.0 to 3.5 Å during the simulations. Fig. 2 shows radial distribution functions of the Na-Ga melt with a N-N bond length of 1.2 Å calculated using the data from the last one ps of the 10 ps period. We find that the N-N interatomic distance remained at the set value during the simulations. The radial distribution functions almost converged at least 5 ps later, and thus the melt structure reached equi- librium. We therefore used the data from the latter half of the 10 ps period to calculate the mean forces, which are the interatomic forces needed to maintain the atomic distance, via the blue-moon ensemble method [19,20]. The calculated mean forces are shown in Appendix A. Free energy profiles were obtained by integrating the mean forces. When we targeted the C-H bonding of the CH₄ molecule, one C-H interatomic distance was constrained and the other C-H bond lengths were kept constant at about 1.09 Å. Additionally, we calculated the coordination number of the Ga atoms around the N-N bond to examine the effect of surrounding Ga atoms on the N-N bond. We counted the number of Ga atoms within a radius of 2.5 Å from the N atoms. The atomic orbital local density of states (AOLDOS) was also analyzed to discuss the electronic states of the bonds. In the above calculations, we did not consider the influence of spin polarization because our preliminary AOLDOS analysis with reference to C-C bonds confirmed that the spin polarization did not influence the bonding state in Na-Ga melts. We used 5 × 5 × 5 k-points for the AOLDOS calculations.

### 3. Results and discussion

Fig. 3(a)-(d) show the calculated free energy profiles for N-N, C-C, C-H (CH), and C-H (CH₄) in the Na and Na-Ga melts, respectively. Fig. 3 (e) shows those of C-H (CH₄) in the Ga melt at 373 K and 673 K. The horizontal axis is the constrained interatomic distance. The interatomic distance at which the free energies reach a local minimum is a stable bond length. The formation activation energies ($E_f$) were determined from the energy difference between a local maximum and zero, and dissociation activation energies ($E_d$) were determined from the energy difference between a local maximum and a local minimum. The esti- mated values are listed in Table 1. In addition, we calculated the reac- tion velocity $k$ using the first-order reaction kinetics,

$$
k=A \exp \left(\frac{-E}{k_{\mathrm{B}} T}\right) \tag{1}
$$

where $k, A, E, k_{\mathrm{B}}$, and $T$ are the reaction velocity, pre-exponential factor, activation energy, Boltzmann constant, and temperature, respectively. The value of $A$ indicates oscillation frequency. Time variation of the distance between the C and N atoms in the Na-Ga melt was obtained from the first-principles MD simulation at 1073 K for 2 ps [7]. We calculated the oscillation frequency of the C-N bond via Fourier trans- form and found that it was of the order of $10^{13} \mathrm{~s}^{-1}$. Substituting $A=1 \times$ $10^{13} \mathrm{~s}^{-1}$, we determine that activation barriers lower than 2.8 eV cause

![](./images/812478691073327106_3.jpg)

Fig. 3. Free energy profiles for the (a) N-N, (b) C-C, (c) C-H (CH), and (d) C-H (CH₄) bonds in the Na and Na-Ga melts, and (e) the C-H (CH₄) bond in the Ga melt.

<table>
<caption>Table 1<br>Activation free energies for bond formation and dissociation (eV).</caption>
<thead>
<tr>
<th>Bond</th>
<th>Melt</th>
<th>Formation ($E_f$)</th>
<th>Dissociation ($E_d$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>N-N</td>
<td>Na</td>
<td>0.46</td>
<td>3.84</td>
</tr>
<tr>
<td></td>
<td>Na-Ga</td>
<td>0.94</td>
<td>1.13</td>
</tr>
<tr>
<td>C-C</td>
<td>Na</td>
<td>0.07</td>
<td>6.56</td>
</tr>
<tr>
<td></td>
<td>Na-Ga</td>
<td>0.51</td>
<td>2.71</td>
</tr>
<tr>
<td>C-N</td>
<td>Na</td>
<td>0.28ª</td>
<td>6.28ª</td>
</tr>
<tr>
<td></td>
<td>Na-Ga</td>
<td>0.90ª</td>
<td>3.01ª</td>
</tr>
<tr>
<td>C-H (CH)</td>
<td>Na</td>
<td>0.44</td>
<td>1.97</td>
</tr>
<tr>
<td></td>
<td>Na-Ga</td>
<td>0.74</td>
<td>1.34</td>
</tr>
<tr>
<td>C-H (CH₄)</td>
<td>Na</td>
<td>0.90</td>
<td>1.60</td>
</tr>
<tr>
<td></td>
<td>Na-Ga</td>
<td>1.05</td>
<td>1.58</td>
</tr>
<tr>
<td>C-H (CH₄)</td>
<td>Ga (373 K)</td>
<td>0.59</td>
<td>1.40</td>
</tr>
<tr>
<td></td>
<td>Ga (673 K)</td>
<td>0.64</td>
<td>1.37</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4">ª Reference [7].</td>
</tr>
</tfoot>
</table>

a fast reaction at 1073 K. Fig. 4(a)-(c) show the coordination number of Ga atoms around the N-N, C-C, and C-H (CH) bonds in the Na-Ga melts, respectively. Fig. 4(a) and (b) show two kinds of plots because there are two N and C atoms in the simulation models. Figs. 5-7 show the AOLDOS for N-N, C-C, and C-H (CH) bonds in the Na and Na-Ga melts, respectively. Snapshots in the figures are the atomic coordinates used for the AOLDOS calculations. We use these results to examine the existence of Ga atoms around the target bond and discuss the effect of Ga atoms on the bonding states.

First, we discuss the N-N bond energy in the Na and Na-Ga melts. We found from Fig. 3(a) that the stable N-N interatomic distance was about 1.2 Å, which is close to the reported value in the gas phase (1.095 Å [26]). The dissociation activation energy in the Na-Ga melt was about 1.13 eV, lower than that in the Na melt, and was nearly equal to the formation activation energy in the Na-Ga melt. However, because N solubility in Na-Ga melts is quite low (lower than 0.1 at.% [10]), re-coupling of isolated N atoms does not need to be considered. Therefore these results indicate that the N-N bond easily dissociates in the Na-Ga melt. The greater in N solubility in Na-Ga melt than in Ga and Na melts was previously found by Kawahara et al. with first-principles calculations [27,28]. Romanowski et al. estimated the dissociation activation energies of N₂ on liquid Al, Ga, and In surface using density functional theory calculations and the value on the liquid Ga surface is 3.4 eV [29]. This value is comparable to our calculated value of 3.84 eV in the Na melt. In comparing the values in Ref. [29] with ours, there is a difference in reaction environment between in liquid and on liquid surface. However, the phenomenon being discussed is similar. These results indicate that N solubilities in Ga and Na melts are also comparable and it is consistent with the previous study [28].

Fig. 4(a) shows the coordination number of Ga atoms around the N atoms as a function of N-N interatomic distance. We found that Ga atoms existed around the N atoms when the N-N distance was larger than 1.3 Å. Fig. 5(a) and (b) show the AOLDOS for one of the N atoms with a N-N bond length of 1.3 Å for the Na melt and Na-Ga melt models, respectively, and Fig. 5(c) shows that for Ga atoms in the Na-Ga melt. The AOLDOS for Na atoms is not shown here because it shows a broad metallic band, and thus Na atoms do not have strong bonds to other atoms. It was reported that projected density of states (PDOS) for Ga, Na, and Ga-rich Na-Ga melt (Na:Ga = 1:4) show broad metallic bands and

![](./images/812478691073327106_4.jpg)

Fig. 4. Coordination number of Ga atoms within a radius of 2.5 Å from the (a) N atoms of the N-N bond, (b) C atoms of the C-C bond, and (c) C and H atoms of the C-H bond in Na-Ga melts.

interaction between N and Ga atoms is week; that for Na-rich Na-Ga melt (Na melt including two Ga atoms) show sharp peaks indicating the existence of N-Ga bond [28]. In our case, multiple sharp peaks are shown in the results for Ga atoms in the Na-Ga melts (Figs. 5(c), 6(c), and 7(c)). We also confirmed that broad metallic bonds appeared for Ga atoms in the Ga melt with CH₄ (not shown here). We therefore believe that the multiple sharp peaks are due to the fact that Ga atoms dispersedly exist in Na melts, as well as formation of N-Ga and C-Ga bonds. In Fig. 5(a), sharp peaks for the s, $p_x$, and $p_z$ orbitals appear at -5.7 eV, which correspond to the $\sigma$ bonding state; the peaks for $p_x$ and $p_y$ at -6.1 eV are a twofold degenerate $\pi$ bonding state. These peaks form a $N{=}N$ double or $N{\equiv}N$ triple bond. However, for the Na-Ga melt, there are $p_x$ and $p_y$ peaks at about -6.2 eV, and multiple peaks due to the effect of Ga atoms appear at about -8.5 eV and -3.8 eV. The broad peak above the Fermi level is an antibonding $\pi^*$ orbital. As seen in Fig. 5(b), it becomes lower in energy and is occupied in the Na-Ga melt model. From these results, we conclude that the N-N bond weakens owing to the effect of the surrounding Ga atoms.

Here we compare the N-N bond and C-N bond in the Na-Ga melt. The bond energies of isolated N-N and C-N were calculated as 9.76 and 8.35 eV, respectively, using the first-principles calculations. In addition, the calculated values of 10.45 eV for N-N and 8.46 eV for C-N were reported [30]. The binding energy of the N₂ is higher than the CN; however, the CN is stable but the N₂ does not exist in the Na-Ga melt (N₂ is dissolved as N atoms when GaN grows). This is because the dissociation energy for the N-N bond is low enough for the bond dissociation in the Na-Ga melt at 1073 K; however, that for the C-N bond is so high that the C-N bond hardly dissociates in the GaN growth conditions.

Next, we discuss the C-C bond in the Na and Na-Ga melts. The free energy profiles in Fig. 3(b) indicate that the stable C-C interatomic distance was about 1.3 Å. The dissociation activation energy in the Na melt was about 6.56 eV. Our calculated C-C interatomic distance and bonding energy with an isolated C-C bond were about 1.31 Å and 6.85 eV, respectively. These values are respectively comparable to the reported values of 1.2454 Å (experimental value) and 6.16 eV (obtained using first-principles calculations with PBE) [30]. Therefore the Na melt did not affect the C-C bonding state. However, the dissociation activation energy for the C-C bond decreased to about 2.71 eV in the Na-Ga melt. This result indicates that C additives can decompose into C atoms in the Na-Ga melts; however, it is a slow reaction. Therefore pre-growth conditions such as heating temperature and duration influence the crystal quality.

We see in Fig. 4(b) that the coordination number of Ga atoms around the C atoms began to increase at a C-C interatomic distance of 1.3 Å. However, after comprehensively estimating from the results for mean force (see Appendix A, Fig. A.8(b)), the free energy profiles (Fig. 4(b)), and the AOLDOS (not shown here), we determined that the effect of the surrounding Ga atoms on the C-C bond appeared when the C-C interatomic distance was equal to or greater than 1.5 Å. Next, Fig. 6(a) and (b) show the AOLDOS for one of the C atoms with a C-C bond length of 1.5 Å for the Na melt and the Na-Ga melt models, respectively, and Fig. 6(c) shows that for Ga atoms in the Na-Ga melt. Fig. 6(a) shows peaks of $s,p_x,p_y$, and $p_z$ orbitals at about -3.2 eV. We deduce that these orbitals form a C-C single bond. However, we see in Fig. 6(b) that multiple peaks due to the effect of Ga atoms appear in the range of -2.5 to -7.5 eV. In addition, the antibonding $\pi^*$ orbital becomes broader and is partially occupied. We therefore conclude that the C-C bond also weakens owing to the effect of surrounding Ga atoms.

The type of C additive also affects the ease of decomposition. For example, Liu et al. investigated the effect of C types including carbon nanotube, active carbon, graphene, and graphite [31]. Murakami et al. used methane (CH₄) gases as a C source and found they were more effective than graphite additives [6]. They considered that the C concentrations near the gas-liquid interface and around the seed crystal are higher and lower than those in the case of graphite additives, respectively. Next, we discuss the calculated C-H bond energies.

Fig. 3(c) and (d) show the free energy profiles for C-H (CH) and C-H (CH₄), respectively. The stable C-H interatomic distance in C-H (both CH and CH₄) was about 1.1 Å, which agreed well with the reported values of 1.13 (CH) and 1.09 (CH₄) Å [26]. The dissociation activation energies for the C-H bonds were low enough for bond dissociation under the GaN growth conditions. We calculated the C-H bond energy for an isolated CH₄ molecule to be about 4.57 eV. Therefore the C-H bond easily dissociates owing to the influence of the Na-Ga melt. Because the dissociation energy for the C-H bond is lower than that for the C-C bond in the Na-Ga melt, CH₄ gas decomposes more easily than graphite. We consider this to be the reason that CH₄ gas is more effective as a C additive than graphite.

Fig. 4(c) shows the coordination number of Ga atoms around the C and H atoms as a function of C-H interatomic distance. The Ga coordination number began to increase at a C-H interatomic distance of 1.8 Å. We also see that the trend of the mean forces for the Na and Na-Ga melt

![](./images/812478691073327106_5.jpg)

Fig. 5. Atomic orbital local density of states for (a) N in the Na melt, (b) N in the Na-Ga melt, and (c) Ga in the Na-Ga melt with a N-N bond length of 1.3 Å. The z-axis is parallel to the N-N bond. The Fermi level is set to zero.

models changes at a C-H distance $\geqslant$1.8 Å (see Appendix A, Fig. A.8(c)). Fig. 7(a) and (b) show the AOLDOS for the C atom with a C-H bond length of 1.8 Å for the Na melt and Na-Ga melt models, respectively, and Fig. 7(c) shows that for Ga atoms in the Na-Ga melt. Fig. 7(a) shows sharp peaks for s and $p_{z}$ orbitals at $-3.7$ eV. However, because the antibonding $\pi^{*}$ orbital is lower than the Fermi level, the C-H bond is weak even in the Na melt. Moreover, Fig. 7(b) shows multiple peaks due to the effect of Ga atoms in the range of $-2.5$ to $-8.0$ eV, and the antibonding $\pi^{*}$ orbital moves completely below the Fermi level. Thus the C-H bond becomes weaker owing to the effect of Ga atoms.

Finally, we discuss the dissociation of the C-H bond in the Ga melt. Fujita et al. used molten Ga as a catalyst for decomposing CH₄ in graphene growth via chemical vapor deposition and achieved low-temperature (50-500 °C) growth [18]. The activation energy of the CH₄ decomposition, which is important for discussing the usefulness of this technique, was estimated to be 1.22 eV. However, we estimated from the results in Fig. 3(e) that the dissociation activation energies for the C-H (CH₄) bond at 373 K and 673 K were about 1.40 and 1.37 eV, respectively. These values are almost the same as the above reported value. In addition, the C-H bond oscillation frequencies that we calculated from the MD simulation data were about $3.6\times10^{13}$ and $9.9\times10^{13}\ \text{s}^{-1}$. Substituting $A=1\times10^{14}\ \text{s}^{-1}$ and $E=1.40$ eV into Eq. 1, we find that the dissociation of CH₄ in Ga melt quickly occurs above 500 K.

### 4. Conclusions

In conclusion, we estimated formation and dissociation activation energies for N-N, C-C, C-H (CH), and C-H (CH₄) in Na-Ga melts and C-H (CH₄) in Ga melts using first-principles MD simulations. We discussed the obtained bond energies in association with the C-added Na-flux GaN growth and graphene growth using CH₄ and Ga melt. The Na-Ga and Ga melts influence the above bonding states as catalysts. We found that the estimated bond energies in the melts were lower than the commonly known values. For the Na-flux GaN growth, we found evidence for an increase in N solubility in the Na-Ga melt. In addition, CH₄ gas is a more efficient additive than graphite because the C-H bonds

![](./images/812478691073327106_6.jpg)

Fig. 6. Atomic orbital local density of states for (a) C in the Na melt, (b) C in the Na-Ga melt, and (c) Ga in the Na-Ga melt with a C-C bond length of 1.5 Å. The z-axis is parallel to the C-C bond. The Fermi level is set to zero.

![](./images/812478691073327106_7.jpg)

Fig. 7. Atomic orbital local density of states for (a) C in the Na melt, (b) C in the Na-Ga melt, and (c) Ga in the Na-Ga melt with a C-H bond length of 1.8 Å. The z-axis is parallel to the C-H bond. The Fermi level is set to zero.

more easily dissociate than C-C bonds. We estimated that the dissociation activation energy for the C-H bond in the Ga melt was about 1.40 eV, which is comparable with the experimental value of 1.22 eV.

Data availability

The raw/processed data required to reproduce these findings are available from the corresponding author upon reasonable request.

CRediT authorship contribution statement

Takahiro Kawamura: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review & editing, Visualization, Funding acquisition, Project administration. Masayuki Imanishi: Conceptualization, Resources. Masashi Yoshimura: Conceptualization, Resources. Yusuke Mori: Conceptualization, Resources. Yoshitada Morikawa: Methodology, Software, Investigation, Resources, Funding acquisition.

Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Acknowledgements

This work was supported by JSPS KAKENHI Grant Nos. JP15K17459, JP18K04957, JP26105010 and JP16H06418. Mark Kurban from Edanz Group ( https://en-author-services.edanzgroup.com/ac) edited a draft of this manuscript.

Appendix A. Mean forces

Fig. A.8(a)-(d) show the mean forces of the N-N, C-C, C-H (CH), and C-H (CH₄) bonds in the Na and Na-Ga melts, respectively, and Fig. A.8(e) shows the C-H (CH₄) bond in the Ga melt. The interatomic distance at which the mean force is zero equals the stable bond length.

![](./images/812478691073327106_8.jpg)

![](./images/812478691073327106_9.jpg)

![](./images/812478691073327106_10.jpg)

![](./images/812478691073327106_11.jpg)

![](./images/812478691073327106_12.jpg)

Fig. A.8. Mean forces of the (a) N-N, (b) C-C, (c) C-H (CH), and (d) C-H (CH₄) bonds in the Na and Na-Ga melts, and of the (e) C-H (CH₄) bond in the Ga melt.

## References

[1] T. Daeneke, K. Khoshmanesh, N. Mahmood, I.A. de Castro, D. Esrafilzadeh, S. J. Barrow, M.D. Dickey, K. Kalantar-zadeh, Liquid metals: fundamentals and applications in chemistry, Chem. Soc. Rev. 47 (2018) 4073-4111.

[2] S.-T. Liang, H.-Z. Wang, J. Liu, Progress, mechanisms and applications of liquid- metal catalyst systems, Chem. Eur. J. 24 (2018) 17616-17626.

[3] H. Yamane, M. Shimada, S.J. Clarke, F.J. DiSalvo, Preparation of GaN single crystals using a Na flux, Chem. Mater. 9 (1997) 413-416.

[4] F. Kawamura, M. Morishita, M. Tanpo, M. Imade, M. Yoshimura, Y. Kitaoka, Y. Mori, T. Sasaki, Effect of carbon additive on increases in the growth rate of 2 in GaN single crystals in the Na flux method, J. Cryst. Growth 310 (2008) 3946-3949.

[5] M. Imade, Y. Hirabayashi, Y. Konishi, H. Ukegawa, N. Miyoshi, Yoshimura Masashi, T. Sasaki, Y. Kitaoka, Y. Mori, Growth of large GaN single crystals on high-quality GaN seed by carbon-added Na flux method, Appl. Phys. Express 3 (2010), 075501.

[6] K. Murakami, S. Ogawa, M. Imanishi, M. Imade, M. Maruyama, M. Yoshimura, Y. Mori, Increase in the growth rate of GaN crystals by using gaseous methane in the Na flux method, Jpn. J. Appl. Phys. 56 (2017), 055502.

[7] T. Kawamura, H. Imabayashi, Y. Yamada, M. Maruyama, M. Imade, M. Yoshimura, Y. Mori, Y. Morikawa, Structural analysis of carbon-added Na-Ga melts in Na flux GaN growth by first-principles calculation, Jpn. J. Appl. Phys. 52 (2013) 08JA04.

[8] T. Kawamura, H. Imabayashi, M. Maruyama, M. Imade, M. Yoshimura, Y. Mori, Y. Morikawa, First-principles investigation of the GaN growth process in carbon- added Na-flux method, Phys. Status Solidi B 252 (2015) 1084-1088.

[9] T. Kawamura, H. Imabayashi, M. Maruyama, M. Imade, M. Yoshimura, Y. Mori, Y. Morikawa, Mechanism for enhanced single-crystal GaN growth in the C-assisted Na-flux method, Appl. Phys. Express 9 (2016), 015601.

[10] M. Morishita, F. Kawamura, M. Kawahara, M. Yoshimura, Y. Mori, T. Sasaki, Promoted nitrogen dissolution due to the addition of Li or Ca to Ga-Na melt; some effects of additives on the growth of GaN single crystals using the sodium flux method, J. Cryst. Growth 284 (2005) 91-99.

[11] T. Iwahashi, Y. Kitaoka, M. Kawahara, F. Kawamura, M. Yoshimura, Y. Mori, T. Sasaki, R. Armitage, H. Hirayama, Fabrication of a-plane GaN substrate using the Sr-Na flux liquid phase epitaxy technique, Jpn. J. Appl. Phys. 46 (2007) L103-L106.

[12] K. Masumoto, T. Someno, K. Murakami, H. Imabayashi, H. Takazawa, Y. Todoroki, D. Matsuo, A. Kitamoto, M. Maruyama, M. Imade, M. Yoshimura, Y. Kitaoka, T. Sasaki, Y. Mori, The effects of Ba-additive on growth of a-plane GaN single crystals using Na flux method, Jpn. J. Appl. Phys. 51 (2012), 040203.

[13] H. Imabayashi, K. Murakami, D. Matsuo, Y. Todoroki, H. Takazawa, A. Kitamoto, M. Maruyama, M. Imade, M. Yoshimura, Y. Mori, Growth and evaluation of bulk GaN crystals grown on a point seed crystal by Ba-sdded Na flux method, Sens. Mater. 25 (2013) 165-176.

[14] S. Kawanishi, T. Yoshikawa, T. Tanaka, Equilibrium phase relationship between SiC and a liquid phase in the Fe-Si-C system at 1523-1723K, Mater. Trans. 50 (2009) 806-813.

[15] K. Kamei, K. Kusunoki, N. Yashiro, N. Okada, T. Tanaka, A. Yauchi, Solution growth of single crystalline 6H, 4H-SiC using Si-Ti-C melt, J. Cryst. Growth. 311 (2009) 855-858.

[16] K. Danno, H. Saitoh, A. Seki, H. Daikoku, Y. Fujiwara, T. Ishii, H. Sakamoto, Y. Kawai, High-speed growth of high-quality 4H-SiC bulk by solution growth using Si-Cr based melt, Mater. Sci. Forum. 645-648 (2010) 13-16.

[17] N. Komatsu, T. Mitani, Y. Hayashi, T. Kato, S. Harada, T. Ujihara, H. Okumura, Modification of the surface morphology of 4H-SiC by addition of Sn and Al in solution growth with SiCr solvents, J. Cryst. Growth. 458 (2017) 37-43.

[18] J. Fujita, T. Hiyama, A. Hirukawa, T. Kondo, J. Nakamura, S. Ito, R. Araki, Y. Ito, M. Takeguchi, W.W. Pai, Near room temperature chemical vapor deposition of graphene with diluted methane and molten gallium catalyst, Sci. Rep. 7 (2017) 12371.

[19] E.A. Carter, G. Ciccotti, J.T. Hynes, R. Kapral, Constrained reaction coordinate dynamics for the simulation of rare events, Chem. Phys. Lett. 156 (1989) 472-477.

[20] M. Sprik, G. Ciccotti, Free energy from constrained molecular dynamics, J. Chem. Phys. 109 (1998) 7737-7744.

[21] Y. Morikawa, Further lowering of work function by oxygen adsorption on the K/Si (001) surface, Phys. Rev. B 51 (1995) 14802-14805.

[22] S.G. Louie, S. Froyen, M.L. Cohen, Nonlinear ionic pseudopotentials in spin-density functional calculations, Phys. Rev. B 26 (1982) 1738-1742.

[23] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868.

[24] A. Kokalj, Computer graphics and graphical user interfaces as tools in simulations of matter at the atomic scale, Comp. Mater. Sci. 28 (2003) 155-168.

[25] A.S. Basin, A.N. Solv'ev, Investigation of the density of liquid lead, cesium, and gallium by the gamma-method, J. Appl. Mech. Tech. Phys. 8 (1967) 83-87.

[26] G. Glockler, Estimated bond energies in carbon, nitrogen, oxygen, and hydrogen compounds, J. Chem. Phys. 19 (1951) 124.

[27] M. Kawahara, F. Kawamura, M. Yoshimura, Y. Mori, T. Sasaki, S. Yanagisawa, Y. Morikawa, A first-principles study on nitrogen solubility in Na flux toward theoretical search for a novel flux for bulk GaN growth, J. Cryst. Growth 303 (2007) 34-36.

[28] M. Kawahara, F. Kawamura, M. Yoshimura, Y. Mori, T. Sasaki, S. Yanagisawa, Y. Morikawa, A first-principles investigation on the mechanism of nitrogen dissolution in the Na flux method, J. Appl. Phys. 101 (2007), 066106.

[29] Z. Romanowski, S. Krukowski, I. Grzegory, S. Porowski, Surface reaction of nitrogen with liquid group III metals, J. Chem. Phys. 114 (2001) 6353-6363.

[30] K.P. Kepp, Trends in strong chemical bonding in C2, CN, CN-, CO, N2, NO, NO+, and O2, J. Phys. Chem. A 121 (2017) 9092-9098.

[31] Z. Liu, G. Ren, L. Shi, X. Su, J. Wang, K. Xu, Effect of carbon types on the generation and morphology of GaN polycrystals grown using the Na flux method, CrystEngComm. 17 (2015) 1030-1036.