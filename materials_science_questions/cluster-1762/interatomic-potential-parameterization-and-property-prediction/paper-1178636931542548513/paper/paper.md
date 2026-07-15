# Molecular dynamics simulations of oxide ion migration in $La_2Ga_3O_{7.5}$ with completely ordered interstitial oxide ions

![](./images/1178636931542548513_1.jpg)

Lei Zhao $^{a}$, Shipeng Geng $^{a}$, Jie Feng $^{b}$, Congling Yin $^{a,*}$, Xiaojun Kuang $^{a,b,**}$

$^{a}$ MOE Key Laboratory of New Processing Technology for Nonferrous Metal and Materials, Guangxi Key Laboratory of Optical and Electronic Materials and Devices,
College of Materials Science and Engineering, Guilin University of Technology, Guilin, 541004, PR China
$^{b}$ College of Chemistry and Bioengineering, Guilin University of Technology, Guilin, 541004, PR China

---

## ARTICLE INFO

**Keywords:**
Melilite
Molecular dynamics simulation
Interstitial oxide ion conductor
Layered tetrahedral network

## ABSTRACT

Molecular dynamics simulations were performed on metastable $La_2Ga_3O_{7.5}$ melilite ceramics, which were synthesized previously by direct crystallization of an under-cooled melt. $La_2Ga_3O_{7.5}$ possesses the theoretically maximum content of interstitial oxide ions featuring complete ordering but ~3 orders of magnitude lower oxide ion conductivities compared with disordered $La_{1.54}Sr_{0.46}Ga_3O_{7.27}$ within 573-773 K. One dimensional diffusion paths of interstitial oxide ion was identified in $La_2Ga_3O_{7.5}$ based on the molecular dynamics simulations, which shows that the interstitial oxide ions can migrate from the pentagonal ring containing $GaO_5$ pyramid unit to its neighboring pentagonal ring free of interstitial oxide ion mainly along the a axis through a synergic mechanism involving continuous breaking and reformation of $Ga_2O_8$ units assisted by rotation and deformation of $GaO_n$ polyhedra and knock-on process between interstitial and framework oxygen atoms. Such constrained dimensionality on the diffusion paths arising from the confining effect for a large number of oxygen interstitials in the highly relaxed and ordered melilite superstructure accounts for the lower oxide ion conductivity in $La_2Ga_3O_{7.5}$.

---

## 1. Introduction

Oxide ion conductors are key components for various technologies including solid oxide fuel cells, oxygen sensors and pumps, gas separation/permeation, and syn-gas production from the oxidation of natural gas [1-4]. For lowering the operating temperatures for the oxide ion conductor based devices, a deep understanding of the fundamental oxide-ion migration mechanisms is a crucial step, which may prompt the design and discovery of new oxide ion conductors with high oxide ion mobility as well as tailoring the oxide ion conductivity for the known oxide ion conductors. During the past three decades, oxide ion conductors adopting the tetrahedra-based structural types have received considerable interest owing to their structural flexibility on rotation and deformation for accommodation and transportation of oxide ion defects even within the low symmetric networks [5-10]. Among the tetrahedra-based structural types, the layered tetrahedral network melilite (Fig. 1a - d) has been attracting continuously ascending attentions since Rozumek et al. synthesized the gallate-melilite-based oxide ion conductors in 2004 [11,12] and Kuang et al. identified the charge carrier as interstitial oxide ions and elucidated the interstitial oxide ion migration mechanism for the gallate melilites in 2008 [5].

The gallate melilite has a general formula of $A^{3+}B^{2+}Ga_3O_7$, which is composed of $GaO_4$ tetrahedra layers alternating with A/B cationic layers (Fig. 1a and b) [13]. In the tetrahedral layers, the $GaO_4$ tetrahedra connect by sharing three and four apexes (respectively shaded in yellow and purple in Fig. 1a and b), resulting in pentagonal tunnels along the layer stacking direction [13]. The donor-substitution of $La^{3+}$ for $Sr^{2+}$ in $LaSrGa_3O_7$ induces excess oxygen atoms, leading to high oxide ion conductivity (~0.02 S/cm at 873 K) at composition $x = 0.54$ [5]. Neutron powder diffraction (NPD) data revealed that the excess oxide ions enter the pentagonal tunnels between two La/Sr cations and are incorporated into the bonding environment of one of the tetrahedra with terminal oxygen (shaded in yellow in Fig. 1a and b) within the pentagonal rings [5]. Initially, the interstitial oxide ion migration was proposed to occur through a direct 2-dimensional hopping mechanism among the pentagonal rings based on the structural analysis using the high-temperature NPD data [5]. However, later in 2010, molecular dynamics (MD) simulations revealed a cooperative mechanism involving the concerted knock-on motion of interstitial and framework oxide ions along the two-dimensional direction within the tetrahedral layers for the gallate

---

* Corresponding author.
** Corresponding author. College of Chemistry and Bioengineering, Guilin University of Technology, Guilin, 541004, PR China.
E-mail addresses: congling.yin@glut.edu.cn (C. Yin), kuangxj@glut.edu.cn (X. Kuang).

https://doi.org/10.1016/j.jssc.2021.122370
Received 9 April 2021; Received in revised form 24 May 2021; Accepted 19 June 2021
Available online 24 June 2021
0022-4596/© 2021 Elsevier Inc. All rights reserved.

![](./images/1178636931542548513_2.jpg)

Fig. 1. The crystal structures of (a, b) LaSrGa₃O₇ and (c, d) La₂Ga₃O₇.₅: projections along (a, c) [010] and (b, d) [100] axes in the tetragonal melilite cell. O_int denotes the interstitial oxide ion.

melilites, instead of direct hopping of oxygen interstitials [14]. Recently, Density function theory (DFT) calculation and Kinetic Monte Carlo simulations also proved the transport of interstitial ions following an interstitialcy mechanism rather than a direct interstitial migration and found two distinct migration paths with low energy barriers of 0.15 and 0.35 eV in the La₁₊ₓSr₁₋ₓGa₃O₇ melilite [15]. Such synergic mechanism was also evidenced in the metastable aluminate melilites elaborated from the crystallization of glass [16].

The incorporation of oxygen interstitials into the pentagonal rings expands the ring size while contracts all the neighboring ring sizes, making them disfavoring oxygen interstitials [5,17]. Therefore the stabilization and migration of oxygen interstitials in the gallate melilites are highly dependent on the cationic sizes of A³⁺ and B²⁺ and the maximum oxygen interstitial content in gallate melilites was theoretically predicted as one-quarter loading in the pentagonal rings [18]. Through the preparation using the traditional ceramic route, the smaller lanthanide cations in the gallate melilites were found to be unfavorable for the accommodation and transport of interstitial oxide ions [9,19,20]. However, using novel glass-ceramic synthesis on an aerodynamic levitation (ADL)-Laser heating system, in 2018 Boyer et al. [21] successfully isolated a series of interstitial oxide ion conducting gallate melilites Ln₁₊ₓSr₁₋ₓGa₃O₇₊₀.₅ₓ containing smaller lanthanides Gd³⁺, Eu³⁺, and Tb³⁺ with the x values up to 0.6 and with the transparency of glass retained partially. Inspired by the advantage of the glass-ceramic route on stabilizing oxygen interstitials affording the metastable melilite oxide ion conductors, Fan et al. [22] successfully elaborated a metastable melilite on the La₂Ga₃O₇.₅ composition containing the theoretically maximum content of interstitial oxide ions through the glass crystallization method. In La₂Ga₃O₇.₅, the interstitial oxide ions are completely ordered forming $\sqrt{2}$a × $\sqrt{2}$b × 2c orthorhombic superstructure of the simple tetragonal melilite (Fig. 1c and d). Although the highest content of oxygen interstitials, its oxide ion conductivities only reached the level of La₁.₁Sr₀.₉Ga₃O₇.₀₅ and are ~3 orders of magnitude lower than those of disordered La₁.₅₄Sr₀.₄₆Ga₃O₇.₂₇ (with the highest oxide ion conductivity among the melilites [5]) within 573-773 K [22]. This much low oxide ion conductivity of La₂Ga₃O₇.₅ has not been fully understood although it was explained based on the interstitial oxide ion ordering and the blocking effects.

In this study, molecular dynamics simulations based on the interatomic potential method were performed on La₂Ga₃O₇.₅ to probe insight into the migration process of interstitial oxygen atoms in the ordered melilite superstructure. It was elucidated that the decrease of conductivity with the content increase of charge carriers in La₂Ga₃O₇.₅ is due to the transition of interstitial oxide ion migration paths from two dimensions to one dimension within the polyhedral layers.

## 2. Methods

The molecular dynamics simulations for interstitial oxygen migration in La₂Ga₃O₇.₅ were performed with the DL_POLY code [23], and the Buckingham potential function [24] was used to model interactions between ions, with the shell model [24] to describe the electronic polarizability of oxide ions. The Buckingham potential describing the interatomic forces are represented by the ionic, pairwise potential in the form

$$
\varnothing_{i j}\left(r_{i j}\right)=\frac{q_{i} q_{j}}{4 \pi \varepsilon_{0} r_{i j}}+A_{i j} \exp \left(-\frac{r_{i j}}{\rho_{i j}}\right)-\left(\frac{C_{i j}}{r_{i j}^{6}}\right) \tag{1}
$$

where $r_{ij}$ is the distance between ion i and j, $q_{i(j)}$ is the charge of ion i(j), $A_{ij}$, $\rho_{ij}$, and $C_{ij}$ are the Buckingham pair potential parameters, and $\varepsilon_{0}$ is the permittivity of free space. This potential includes a long-range Coulombic interaction and a short-range interaction to model the repulsion and van der Waals attractions between electron-charge clouds. The cutoff distance for the summation of the Buckingham pair potential was 10 Å, as it is significant only at short range. The interatomic potential parameters for La³⁺-O²⁻, Ga³⁺-O²⁻ and O²⁻-O²⁻ used for the atomistic simulations are listed in Table 1, which were obtained from previous MD simulations

by Woodley [25] and Girard [26] et al. Before the MD simulations, the crystal structure of $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ was optimized using the General Utility Lattice Program (GULP) [27,28]. In order to check the size effect, preliminary MD simulations based on one larger $5 \times 2 \times 4$ and one smaller 3 $\times$ 3 $\times$ 3 supercells were performed at 1473 K, which led to nearly identical diffusion coefficients and scatter diagrams of atomic positions. This indicates that the smaller $3 \times 3 \times 3$ supercell is enough for the MD simulations. Therefore considering the efficiency and the computational cost, further simulations on different temperatures were performed on the smaller $3 \times 3 \times 3$ supercell, which contains 2700 atoms, including 648 Ga atoms, 432 La atoms, and 1512 framework oxygen atoms, and 108 interstitial oxygen atoms, corresponding to the $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ composition. The systems were equilibrated under ambient pressure (1 atm) within the temperature range of 1473–2273 K for $2 \times 10^5$ time steps with a time interval of 0.05 fs before carrying out the main MD simulations in the NVT (constant volume and temperature) ensemble for 200 ps with 4 $\times 10^6$ time steps. The Visual Molecular Dynamics (VMD) package [29] was used to analyze the MD data and the mean square displacements (MSDs) were calculated with the nMoldyn code [30].

## 3. Results and discussion

To elucidate how the oxygen interstitials migrate in the melilite structure, atomistic static lattice and MD simulations based on the interatomic potential method were performed, which were previously successfully applied in the gallate ($\text{La}_{1.5}\text{Sr}_{0.5}\text{Ga}_3\text{O}_{7.25}$ [14]) and aluminate ($\text{La}_{1.5}\text{Sr}_{0.5}\text{Al}_3\text{O}_{7.25}$ [16]) melilites and other structural types containing the tetrahedral units e.g., apatite [31], scheelites [10,32,33] and $\text{LaBaGaO}_4$ [7] -based oxide ion conductors. The potential parameters listed in Table 1 reproduced well the experimental melilite structure of $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ (Table 2 and S1), e.g. the discrepancies between calculated and experimental cell parameters and average Ga–O bond lengths vary within 1%, the most Ga–O bond lengths are reproduced within 6% except for one bond with a large discrepancy ~13% (Table S1). The good agreement between the experimental and calculated structure validates these potential parameters for further investigation on the ionic conduction of $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ by molecular dynamics simulations. No other physical parameters are available for further validating the potential parameters as $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ was recently synthesized by melt crystallization with only crystal structure and conductivity reported [22].

Fig. 2 shows the mean square displacement (MSD) plots of La, Ga, interstitial ($\text{O}_{\text{int}}$) and framework ($\text{O}_{\text{fram}}$) oxygen atoms. With the growth of simulation time, La and Ga atoms always vibrate around the initial positions in the crystal structure, and oxygen atoms have long-range migration. Examination on the individual MSD values of interstitial and framework oxygen atoms indicates that both interstitial and framework oxygen atoms are involved in the oxide ion diffusion event while the oxygen atoms initially placed on the interstitial sites have predominant contribution over those placed on the framework sites, as indicated by the inset of Fig. 2. The gradual upturn in the MSD values of the oxide ions initially placed at the normal interstitial sites compared with those for the oxide ions initially placed at the framework sites from 170 ps could probably be related to more disordered structure after such long time scale thermal relaxation, as evidenced by the subtle increase of slope for the total oxygen MSD values within the 170–200 ps range, indicating slightly higher oxide ion mobility. Due to the site exchange between the interstitial and framework oxides (which will be discussed later), the divergence between the MSD curves at the long time scale for the oxide ions initially placed at the interstitial and framework sites is not very meaningful as it did not change the total oxygen MSD values very much.

<table>
<caption>Table 1<br>Buckingham interatomic potentials and shell model parameters for the atomistic simulations.</caption>
<thead>
<tr>
<th>Interactions</th>
<th>A (eV)</th>
<th>$\rho$ (Å)</th>
<th>$C$ (eVÅ$^6$)</th>
<th>$Y$ (e)</th>
<th>$k$ (eVÅ$^{-2}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{La}^{3+}$-$\text{O}^{2-}$</td>
<td>4317.17</td>
<td>0.2987</td>
<td>0.0</td>
<td>/</td>
<td>/</td>
</tr>
<tr>
<td>$\text{Ga}^{3+}$-$\text{O}^{2-}$</td>
<td>2399.776</td>
<td>0.2742</td>
<td>0.0</td>
<td>/</td>
<td>/</td>
</tr>
<tr>
<td>$\text{O}^{2-}$-$\text{O}^{2-}$</td>
<td>25.41</td>
<td>0.6937</td>
<td>0.0</td>
<td>–2.513</td>
<td>0</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Calculated and experimental structural parameters of $\text{La}_2\text{Ga}_3\text{O}_{7.5}$.</caption>
<thead>
<tr>
<th>Parameters</th>
<th>Experimental [22]</th>
<th>Calculated</th>
<th>$\Delta$(Calc. - Exp.)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ (Å)</td>
<td>11.4701</td>
<td>11.5045</td>
<td>0.30%</td>
</tr>
<tr>
<td>$b$ (Å)</td>
<td>11.2676</td>
<td>11.1983</td>
<td>–0.61%</td>
</tr>
<tr>
<td>$c$ (Å)</td>
<td>10.4803</td>
<td>10.5370</td>
<td>0.54%</td>
</tr>
<tr>
<td>Average Ga–O length (Å)</td>
<td>1.8748</td>
<td>1.8862</td>
<td>0.61%</td>
</tr>
<tr>
<td>Average La–O length (Å)</td>
<td>2.6384</td>
<td>2.5009</td>
<td>–2.55%</td>
</tr>
</tbody>
</table>

![](./images/1178636931542548513_3.jpg)

Fig. 2. Calculated MSD values of La, Ga, and O atoms as a function of time from the MD simulation at 1473 K. The inset shows the MSD values of oxygen atoms at different crystallographic sites.

The migration pathway of the interstitial oxygen atoms in $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ at 1473 K was explored based on the scatter diagrams of atomic positions in $\text{La}_2\text{Ga}_3\text{O}_{7.5}$ from the MD simulations. Viewing along the $a$ axis (Fig. 3a and S1a) and the $b$ axis (Figures S1b), we can intuitively see that the migration of oxygen atoms are confined in the $\text{Ga}_3\text{O}_{7.5}$ layers in parallel with the $ab$ plane (Fig. 3b and c), consistent with the existence of La cations above and below the pentagonal rings, blocking the interlayer migration of oxygen atoms. Careful observation on these scatter diagrams reveals a discontinuous diffusion chain along the $b$ axis (Fig. 3a and S1a), in contrast with the continuous diffusion chain along the $a$ axis (Fig. 3b and S1b) in the $\text{Ga}_3\text{O}_{7.5}$ layers. The scatter plot viewed along the $c$ axis (Fig. 3b) shows that the positions of oxygen atoms initially placed at the interstitial and the neighboring framework oxygen sites are overlapping, suggesting the site exchange among these oxygen atoms, i.e. the oxygen interstitials could knock out and replace the original framework oxygen atoms, which move into the adjacent five-membered rings. The streaming and overlapping of positions for the interstitial and framework oxygen atoms indicate essentially one-dimensional curved pathways for the oxide ion migration within the limited simulation time, as highlighted by dashed lines in Fig. 3b.

To elucidate the dynamic process of oxide ion migration, trajectory analysis was performed on the MD simulation data and typical snapshots (Fig. 4) were taken to illustrate the intermediate polyhedral formation during the oxide ion migration. The analysis of the trajectories confirms that both the interstitial and framework oxygen atoms participate in the migration event via a cooperative mechanism involving continuous reforming and breaking of the intermediate state of edge-sharing $\text{Ga}_2\text{O}_8$ units that are assisted by the $\text{GaO}_n$ polyhedral rotation and deformation. The oxygen ions initially placed on the $\text{O}_{\text{int}}$ positions can knock out a framework oxygen ion off the regular position and therefore transform

![](./images/1178636931542548513_4.jpg)

Fig. 3. The scatter diagrams of atomic positions in $La_2Ga_3O_{7.5}$ from the MD simulation at 1473 K viewed along (a) $a$ and (b) $c$ axes in comparison with (c) the polyhedral plot of the crystal structure viewed along the $c$ axis. The dots in red, green, blue, and purple represent the atoms initially placed at skeleton oxygen, interstitial oxygen, La, and Ga sites. (b–c) shows one polyhedral layer only. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

two $GaO_n$ polyhedra into an edge-sharing $Ga_2O_8$ unit. This unit breaks and releases one oxygen into the regular interstitial sites in the neigh- boring pentagonal ring which was originally empty. Therefore these originally-empty pentagonal rings also participate in the interstitial oxide ion migration as they provide key room for the relaxation of the frame- work and interstitial oxide ions. This is consistent with the scatter plot (Fig. 3b) that also shows some visiting of oxide ions to the central posi- tions of the originally-empty pentagonal rings (marked by black thin- dash lines) between the main one-dimensional migration pathways (marked by black thick-dash lines with arrows).

The MSD values of oxygen atoms were used to calculate the oxygen diffusion coefficients (Fig. 5), which are in the range of $10^{-5}$-$10^{-7}\ cm^2/s$ within 1473-2273 K. The calculated activation energy from the oxygen diffusion coefficients, 0.78(1) eV, is smaller than the experimental values (1.21 eV) in the low-temperature region for the $La_2Ga_3O_{7.5}$ from the conductivity measurements [22] (the activation energy in the high-temperature region is even superficially higher owing to the extra energy required for disordering of interstitial oxide ions). Similar dis- crepancies between experimental and calculated activation energies were also observed in the $La_{1.5}Sr_{0.5}Ga_3O_{7.25}$ composition [5,14]. As the calculated value relates to the intrinsic defect migration and does not include the energy terms from the defect trapping [7], it is not unusual that the MD simulations here gave lower activation energy than the experimental values. Finally, it is worth noting here that the calculated activation energy (0.78 eV) for oxide ion migration in $La_2Ga_3O_{7.5}$ is higher than that (0.70 eV) for $La_{1.5}Sr_{0.5}Ga_3O_{7.25}$ [14], which is consistent with that the ordering of interstitial oxide ions indeed lowers the oxide ion mobility.

The ionic conductivity is related to the activation energy and carrier concentration as the dominant factors in solid-state materials. The ionic migration involves the relaxation of the lattice and the ionic hopping from one site to another. Compared with the disordered structure, the structures around the interstitial oxide ions in the ordered structure are well-relaxed thus have a lower energy level and therefore the interstitial oxide ions are more difficult to move, leading to lower conductivity than that in the disordered structure. Such phenonium has been observed inthe many oxide ion conductors [10,18,34,35], e.g. $La_2Mo_2O_9$ [34,35] and the oxygen hyperstoichiometric $CeNbO_{4+\delta}$ phases [10]. In the $La_2Ga_3O_{7.5}$ system, the interstitial oxide ions reach the maximum loading and are completely ordered forming a curved infinite chain of -$GaO_5$- $GaO_4$- in the polyhedral layers along the $a$ axis [22]. These ordered interstitial oxide ions could be easily trapped and therefore localized owing to their low energy levels. On the other hand, the ionic migration pathway often has reduced dimensions in ordered structures compared with disorder structures. The dimensionality reduction on the oxide ion migration pathways owing to the confining effect in the highly relaxed and ordered structure further decreases the ionic conductivity of $La_2Ga_3O_{7.5}$, as the one-dimensional migration might be easily blocked by some impurity ions or planar defects (e.g. grain boundary) on the pathway. While the two and three-dimensional migrations have more tolerance of defects and allow faster ionic transport.

### 4. Conclusion

In summary, molecular dynamics simulations on the interstitial oxide ion ordered melilite superstructure of metastable $La_2Ga_3O_{7.5}$ elucidated a

![](./images/1178636931542548513_5.jpg)

Fig. 4. Snapshots of the $Ga_3O_{7.5}$ layers during the oxide ion migration. The green and red spheres represent ions originally placed on interstitial and framework oxygen sites, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

![](./images/1178636931542548513_6.jpg)

Fig. 5. The Arrhenius plot of oxide ion diffusion coefficients calculated from the MSD values.

cooperative mechanism involving knock-on process between interstitial and framework oxygen atoms but one-dimensional migration pathways for the interstitial oxide ions, in contrast with the two-dimensional migration event in the disordered compositions. Such dimensionality-constrained diffusion paths arise from the confining effect of the large number of oxide interstitials in the highly relaxed and ordered melilite superstructure, which accounts for the lower oxide ion conductivity in $La_2Ga_3O_{7.5}$.

### CRediT authorship contribution statement
Lei Zhao: Methodology, Software, Data curation, Formal analysis, Writing - original draft. **Shipeng Geng**: Methodology, Software. **Jie Feng**: Validation, Software, Investigation. **Congling Yin**: Conceptuali- zation, Writing - review & editing. **Xiaojun Kuang**: Conceptualization, Supervision, Methodology, Writing - review & editing.

### Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgments
The National Natural Science Foundation of China (Nos. 22090043 and 21622101), Guangxi Natural Science Foundation (No. 2019GXNSFGA245006 and AD19245097), Guangxi Program for Hun- dred Talents for Returned Scholars, and High level Innovation Team and Outstanding Scholar Program of Guangxi Institute are acknowledged for financial support.

### Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi.org/10.1016/j.jssc.2021.122370.

### References

[1] B.C.H. Steele, A. Heinzel, Materials for fuel-cell technologies, Nature 414 (2001) 345-352.

[2] E.D. Wachsman, K.T. Lee, Lowering the temperature of solid oxide fuel cells, Science 334 (2011) 935-939.

[3] H.J.M. Bouwmeester, Dense ceramic membranes for methane conversion, Catal. Today 82 (2003) 141-150.

[4] H.Q. Jiang, H.H. Wang, S. Werth, T. Schiestel, J. Caro, Simultaneous production of hydrogen and synthesis gas by combining water splitting with partial oxidation of methane in a hollow-fiber membrane reactor, Angew. Chem. Int. Ed. 47 (2008) 9341-9344.

[5] X.J. Kuang, M.A. Green, H.J. Niu, P. Zajdel, C. Dickinson, J.B. Claridge, L. Jantsky, M.J. Rosseinsky, Interstitial oxide ion conductivity in the layered tetrahedral network melilite structure, Nat. Mater. 7 (2008) 498-504.

[6] E. Kendrick, M.S. Islam, P.R. Slater, Developing apatites for solid oxide fuel cells: insight into structural, transport and doping properties, J. Mater. Chem. 17 (2007) 3104-3111.

[7] E. Kendrick, J. Kendrick, K.S. Knight, M.S. Islam, P.R. Slater, Cooperative mechanisms of fast-ion conduction in gallium-based oxides with tetrahedral moieties, Nat. Mater. 6 (2007) 871-875.

[8] X.Y. Yang, A.J. Fernandez-Carrion, J.H. Wang, F. Porcher, F. Fayon, M. Allix, X.J. Kuang, Cooperative mechanisms of oxygen vacancy stabilization and migration in the isolated tetrahedral anion scheelite structure, Nat. Commun. 9 (2018) 11.

[9] L.J. Zhou, J.G. Xu, M. Allix, X.J. Kuang, Development of melilite-type oxide ion conductors, Chem. Rec. 20 (2020) 1117-1128.

[10] J. Li, F.J. Pan, S.P. Geng, C. Lin, L. Palatinus, M. Allix, X.J. Kuang, J.H. Lin, J.L. Sun, Modulated structure determination and ion transport mechanism of oxide-ion conductor CeNbO₄+δ, Nat. Commun. 11 (2020) 4751.

[11] M. Rozumek, P. Majewski, H. Schluckwerder, F. Aldinger, K. Kunstler, G. Tomandl, Electrical conduction behavior of La₁₊ₓSr₁₋ₓGa₃O₇₋δ melilite-type ceramics, J. Am. Ceram. Soc. 87 (2004) 1795-1798.

[12] M. Rozumek, P. Majewski, L. Sauter, F. Aldinger, La₁₊ₓSr₁₋ₓGa₃O₇₋δ melilite-type ceramics: preparation, composition, and structure, J. Am. Ceram. Soc. 87 (2004) 662-669.

[13] M. Steins, W. Schmitz, R. Uecker, J. Doerschel, Crystal structure of strontium lanthanum trigallium heptoxide, (Sr₀.₅La₀.₅)₂Ga₃O₇, Z. Kristallogr. 212b (1997) 76.

[14] C. Tealdi, P. Mustarelli, M.S. Islam, Layered LaSrGa₃O₇-based oxide-ion conductors: cooperative transport mechanisms and flexible structures, Adv. Funct. Mater. 20 (2010) 3874-3880.

[15] J. Schutt, T.K. Schultze, S. Grieshammer, Oxygen ion migration and conductivity in LaSrGa₃O₇ melilites from first principles, Chem. Mater. 32 (2020) 4442-4450.

[16] J.G. Xu, J.H. Wang, A. Rakhmadullin, S. Ory, A.J. Fernandez-Carrion, H.B. Yi, X.J. Kuang, M. Allix, Interstitial oxide ion migration mechanism in aluminate melilite La₁₊ₓCa₁₋ₓAl₃O₇₊₀.₅ₓ ceramics synthesized by glass crystallization, ACS Appl. Energy Mater. 2 (2019) 2878-2888.

[17] J.G. Xu, J.H. Wang, X. Tang, X.J. Kuang, M.J. Rosseinsky, La₁₊ₓBa₁₋ₓGa₃O₇₊₀.₅ₓ oxide ion conductor: cationic size effect on the interstitial oxide ion conductivity in gallate melilites, Inorg. Chem. 56 (2017) 6897-6905.

[18] M.R. Li, X.J. Kuang, S.Y. Chong, Z.L. Xu, C.I. Thomas, H.J. Niu, J.B. Claridge, M.J. Rosseinsky, Interstitial oxide ion order and conductivity in La₁.₆₄Ca₀.₃₆Ga₃O₇.₃₂ melilite, Angew. Chem. Int. Ed. 49 (2010) 2362-2366.

[19] C.I. Thomas, X.J. Kuang, Z.Q. Deng, H.J. Niu, J.B. Claridge, M.J. Rosseinsky, Phase stability control of interstitial oxide ion conductivity in the La₁₊ₓSr₁₋ₓGa₃O₇₊ₓ/₂ melilite family, Chem. Mater. 22 (2010) 2510-2516.

[20] B.B. Liu, D. Ding, Z.B. Liu, F.L. Chen, C.R. Xia, Synthesis and electrical conductivity of various melilite-type electrolytes Ln₁₊ₓSr₁₋ₓGa₃O₇₊ₓ/₂, Solid State Ionics 191 (2011) 68-72.

[21] M. Boyer, X.Y. Yang, A.J. Fernandez-Carrion, Q.C. Wang, E. Veron, C. Genevois, L. Hennet, G. Matzen, E. Suard, D. Thiaudiere, C. Castro, D. Pelloquin, L.B. Kong, X.J. Kuang, M. Allix, First transparent oxide ion conducting ceramics synthesized by full crystallization from glass, J. Mater. Chem. 6 (2018) 5276-5289.

[22] J.T. Fan, V. Sarou-Kanian, X.Y. Yang, M. Diaz-Lopez, F. Fayon, X.J. Kuang, M.J. Pitcher, M. Allix, La₂Ga₃O₇.₅: a metastable ternary melilite with a super- excess of interstitial oxide ions synthesized by direct crystallization of the melt, Chem. Mater. 32 (2020) 9016-9025.

[23] I.T. Todorov, W. Smith, K. Trachenko, M.T. Dove, DL_POLY_3: new dimensions in molecular dynamics simulations via massive parallelism, J. Mater. Chem. 16 (2006) 1911-1918.

[24] B.G. Dick, A.W. Overhauser, Theory of the dielectric constants of alkali halide crystals, Phys. Rev. 112 (1958) 90-103.

[25] S.M. Woodley, C.R.A. Catlow, J.D. Gale, P.D. Battle, Development of a new force field for open shell ions: application to modelling of LaMnO₃, Chem. Commun. (J. Chem. Soc. Sect. D) (2000) 1879-1880.

[26] S. Girard, J.D. Gale, C. Mellot-Draznieks, G. Ferey, Derivation of interatomic potentials for gallophosphates from the GaPO₄-quartz structure: transferability study to gallosilicates and zeotype gallophosphates, Chem. Mater. 13 (2001) 1732-1738.

[27] J.D. Gale, GULP: a computer Program for the symmetry-adapted simulation of solids, J. Chem. Soc.-Faraday Trans. 93 (1997) 629-637.

[28] J.D. Gale, A.L. Rohl, The general utility lattice Program (GULP), Mol. Simulat. 29 (2003) 291-341.

[29] W. Humphrey, A. Dalke, K. Schulten, VMD: visual molecular dynamics, J. Mol. Graph. 14 (1996) 33-38.

[30] T. Rog, K. Murzyn, K. Hinsen, G.R. Kneller, NMoldyn: a Program package for a neutron scattering oriented analysis of molecular dynamics simulations, J. Comput. Chem. 24 (2003) 657-667.

[31] P.M. Panchmatia, A. Orera, G.J. Rees, M.E. Smith, J.V. Hanna, P.R. Slater, M.S. Islam, Oxygen defects and novel transport mechanisms in apatite ionic conductors: combined 17O NMR and modeling studies angew, Chem. Int. Ed. 50 (2011) 9328-9333.

[32] S.S. Pramana, T. Baikie, T. An, M.G. Tucker, J. Wu, M.K. Schreyer, F.X. Wei, R.D. Bayliss, C.L. Kloc, T.J. White, A.P. Horsfield, S.J. Skinner, Correlation of local structure and diffusion pathways in the modulated anisotropic oxide ion conductor CeNbO₄.₂₅, J. Am. Chem. Soc. 138 (2016) 1273-1279.

[33] C. Ferrara, A. Mancini, C. Ritter, L. Malavasi, C. Tealdi, Interstitial oxide ion migration in scheelite-type electrolytes: a combined neutron diffraction and computational study, J. Mater. Chem. 3 (2015) 22258-22265.

[34] P. Lacorre, F. Goutenoire, O. Bohnke, R. Retoux, Y. Laligant, Designing fast oxide- ion conductors based on La₂Mo₂O₉, Nature 404 (2000) 856-858.

[35] I.R. Evans, J.A.K. Howard, J.S.O. Evans, The crystal structure of α-La₂Mo₂O₉ and the structural origin of the oxide ion migration pathway, Chem. Mater. 17 (2005) 4074-4077.