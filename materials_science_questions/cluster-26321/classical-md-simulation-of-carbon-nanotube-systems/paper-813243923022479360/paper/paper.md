# Dynamic mechanism of HIV replication inhibitor peptide encapsulated into carbon nanotubes

Bao-Dong Chen, Chuan-Lu Yang*, Jun-Sheng Yang, Mei-Shan Wang, Xiao-Guang Ma

School of Physics and Optoelectronic Engineering, Ludong University, Yantai 264025, China

---

## A R T I C L E I N F O
**Article history:**
Received 3 November 2012
Received in revised form
3 February 2013
Accepted 5 February 2013
Available online 19 February 2013

**Keywords:**
Molecular dynamics simulation
Drug delivery
Peptide-CNT interaction
Spontaneous encapsulation
Conformational change

---

## A B S T R A C T
Biomolecules encapsulated in carbon nanotubes (CNTs) have attracted much interest and facilitated exciting opportunities for biological and biomedical applications of CNTs. Understanding the fundamental interaction and change in biomolecules during encapsulation is indispensable but remains a challenge for both theoretical and experimental investigations. This paper focuses on the interaction between HIV replication inhibitor peptide (HRIP) and CNTs in a neutral solution with molecular dynamics simulation. We observed that HRIP spontaneously inserts into the CNTs and oscillates around the center of the tube, where the non-covalent interaction is minimum. The effects of the diameters of the CNTs on HRIP were investigated. The optimal diameter of the CNT that can provide the most effective encapsulation and causes minimum conformational change in HRIP was found. The present results provide valuable valuable insights in the understanding of nanoscale drug delivery using CNT-based devices.

© 2013 Elsevier B.V. All rights reserved.

---

### 1. Introduction
In recent years, carbon nanotubes (CNTs) have attracted the attention of various researchers because of their intrinsic structure [1] and desirable properties [2]. The open-ended single-walled CNT (SWCNT) has a hollow cylindrical structure and consists of rolled graphene sheets with carbon atoms as backbone. With its deep potential well inside, SWCNT has been proven as an excellent transport candidate for many molecules. Many applications of nanotubes have been reported in physical, biotechnological, and biomedical fields, such as hydrogen storage [3,4], fullerene encapsulation ($C_{20}$, $C_{28}$) [5], biosensors [6,7], biocatalysts [8], and biomedical devices [9]. Although the original CNTs are insoluble and aggregated, covalent [10] or non-covalent [11] functionalization makes the CNTs highly soluble in aqueous biological media and provides great opportunities for biological and biomedical applications. Furthermore, the functionalized CNTs are experimentally found to be noncytotoxic [12] and capable of transporting various molecules into mammalian cells through phagocytosis without causing cell damage or death [13,14]. Using the intrinsic near-infrared fluorescence of the nanotubes [15], the functionalized CNTs can be easily tracked in living parts, which is advantageous in the research of complex biological mechanisms.

Hence, both experimental studies and molecular simulations are focused on the investigations where CNTs are regarded as carriers of biomolecules (e.g., DNA [16,17], peptide [18], proteins [19], amylase [20], and drugs [21,22]). Meanwhile, many recent studies have also shown that the effects of CNTs on intrinsic biomolecular behavior can be useful [23-25]. The characteristics of the biological molecules are still retained even after appropriate encapsulation. In addition, Ajima et al. found a four to six times enhancement of the in vivo anticancer effects of cisplatin by incorporating it inside single-walled carbon nanohorns [26]. The non-covalent interactions of biomolecules with the CNT system, and their correlations with changes in biomolecules have become important. Understanding these effects on the transportation of biomolecules into the CNTs is therefore important.

In this paper, we report the molecular dynamic (MD) simulation results of the dynamic process of the insertion of HIV replication inhibitor peptide (HRIP) into the SWCNTs in neutral aqueous environment. HRIP can provide an efficient way of preventing virus penetration in T4 lymphocytes by blocking the viral life cycle. Thus, HRIP is regarded as an effective agent in treating HIV infection and AIDS-related complex in the biomedical industry [27,28]. The MD simulations are considered one of the powerful approaches in exploring biomolecule-CNT interactions, and the dynamic mechanism needs to be systematically studied and further investigated

---

* Corresponding author. Tel./fax: +86 535 6672870.
E-mail addresses: scuycl@gmail.com, yangchuanlu@263.net (C.-L. Yang).

1567-1739/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.cap.2013.02.004
![](./images/813243923022479360_1.jpg)
![](./images/813243923022479360_2.jpg)
![](./images/813243923022479360_3.jpg)

at the molecular level [29]. The results of the present study show that HRIP is capable of spontaneous insertion into CNTs with different diameters. In addition, an optimal tube size for HRIP similar to the ellipsoidal SmtA molecule recently investigated by Kang et al. [30,31] has been found. A suitable SWCNT diameter not only effectively encapsulates but also causes minimum conformational change in a particular peptide/protein. In this work, MD simulations were performed to provide in-depth understanding on the interactions and the dynamic mechanisms of the HRIP-CNT system at the molecular level.

## 2. Models and methods

HRIP (entry code 1RPB) from the Protein Data Bank was chosen as the model peptide [32]. HRIP has a molecular weight of 2185.53 Da and 21 amino acids, shown as LGIGSCNDFAGC-GYAVVCFW. In this work, all MD simulations were performed in the isothermal-isobaric (NPT) ensemble with NAMD 2.8 [33], and VMD 1.9 [34] was used for the visualization and analysis of data. In the simulations, HRIP was first solvated in water molecules of TIP3P [35]. Prior to the simulation for the interaction of the HRIP-CNT systems, a 1 ns MD simulation was performed on the HRIP-water system to stabilize the HRIP structure. The HRIP-CNT system consisted of HRIP and various uncapped armchair SWCNTs. Five series of uncapped armchair single-walled $(n,n)$ CNTs were selected with indices $n=16,17,18,19,20$, yielding tube diameters of 2.17, 2.30, 2.44, 2.57, and 2.71 nm, respectively. The tube length is 3.19 nm according to the peptide size, taking the boundary effect into consideration. In the initial configurations of the MD simulation, the HRIP and CNT were aligned along the nanotube axis and separated by approximately 2 Å (Fig. 1). Then, each HRIP-CNT complex was immersed in a rectangular periodic box of TIP3P water molecules in which the shortest distances between the complex surface and the box walls were larger than half of the cutoff distance. Sodium ions were added to neutralize the system. The CHARMM27 All-atom force field [36] was used with the CNT parameters supplemented with those of graphite [37]. The carbon atoms in the CNTs were all modeled as uncharged and fixed. The instantaneous van der Waals interaction between HRIP and the CNT is defined similarly to Ref. [30], i.e, $E_{\text{vdw-int}}(t)=E_{\text{hrip+cnt}}(t)-E_{\text{hrip}}(t)-E_{\text{cnt}}(t)$. The van der Waals parameters among the different types of atoms were determined using the Lorentz-Berthelot combination rules [38].

$$
\sigma_{ij}=\frac{\left(\sigma_{ii}+\sigma_{jj}\right)}{2} \tag{1}
$$

$$
\varepsilon_{ij}=\sqrt{\varepsilon_{ii}\varepsilon_{jj}} \tag{2}
$$

The cutoff distance of the pairwise LJ nonbonded interactions was set at 12 Å with the pair list distance extended to 13.5 Å. The particle mesh Ewald summation [39] was used to calculate the full-system periodic electrostatic interactions, with a cutoff of 12 Å to separate the direct and reciprocal space summation. During the simulations with NPT ensemble, a temperature of 310 K was maintained using the Langevin dynamics, which only affected the nonhydrogen atoms, and the damping coefficient was set at $5\ \text{ps}^{-1}$. The pressure was set as 101.3 kPa and controlled using the Nosé-Hoover Langevin barostat [40]. The simulation time step was set as 2.0 fs. The center of mass (COM) of the peptide or the CNT was used as the reference point for the matter movement. The distance between the HRIP and CNT COMs is defined as $d$ in Eq. (5), and the initial value of the distance is defined as $d_0$.

$$
\vec{r}=\left(\sum \vec{r}_{i}\cdot m_{i}\right)/\sum m_{i} \tag{3}
$$

$$
\vec{r}_{i}=x_{i}\vec{i}+y\vec{j}+z\vec{k} \tag{4}
$$

$$
d=|\vec{r}_{\text{CNT}}-\vec{r}_{\text{HRI}}| \tag{5}
$$

where $m_i$ and $x_i$, $y_i$, and $z_i$ are the mass and the three Cartesian coordinate components of atom $i$, respectively, and the sums run over all the atoms. Root-mean-square deviation (RMSD) is a numerical measure of the difference between two structures. In this paper, the RMSD values were calculated for the backbone atoms (N, C_alpha, C, and O) of the HRIP as follows:

$$
\text{RMSD}_{\alpha}=\sqrt{\frac{\sum_{j=1}^{N_{t}} \sum_{\alpha=1}^{N_{\alpha}}\left[\vec{r}_{\alpha}\left(t_{j}\right)-\left\langle\vec{r}_{\alpha}\right\rangle\right]^{2}}{N_{\alpha}}} \tag{6}
$$

$$
\left\langle\vec{r}_{\alpha}\right\rangle=\frac{1}{N_{t}} \sum_{j=1}^{N_{t}} \vec{r}_{\alpha}\left(t_{j}\right) \tag{7}
$$

where $N_t$ is the number of time steps, $N_\alpha$ is the number of atoms, $\vec{r}_{\alpha}(t_j)$ is the position of atom $\alpha$ at time $t_j$, and $\langle\vec{r}_\alpha\rangle$ is the average value of the position of atom $\alpha$ with which the positions $\vec{r}_{\alpha}(t_j)$ are being compared.

![](./images/813243923022479360_4.jpg)

Fig. 1. MD simulation snapshots of the initial configuration of the investigated HRIP-CNT system. The colors in the new cartoon model for the secondary structure of the peptide represent the coil (white), β-sheet (yellow), and turn (teal). The line model for the peptide shows the details of the residues. The water molecules and ions are not displayed. (a) Front elevation of the peptide with a`rmchair (17, 17) CNT. (b) Cross-sectional graph of the peptide with armchair (16, 16), (17, 17), (18, 18), (19, 19), and (20, 20) CNTs. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/813243923022479360_5.jpg)

Fig. 2. MD simulation snapshots of the spontaneous insertion of HRIP into an armchair (17, 17) CNT at 0, 2.5, 6, and 27.5 ns. The water molecules and ions are not displayed.

## 3. Results and discussion

### 3.1. Encapsulation of HRIP

We tested the spontaneous insertion of HRIP into the (16, 16) CNT because the size of HRIP is close to the diameter of the CNT, and found that the HRIP configuration was changed by the CNT. Inter- estingly, the (17, 17) CNT absorbed the HRIP and only slightly changed its configuration. Fig. 2 shows the spontaneous insertion of the HRIP-CNT system with four snapshots at important points. The normalized distances ($d/d_0$) between the COM of the HRIP and the CNT can be used to indicate quantitatively the insertion of the HRIP. Fig. 3(a) shows the $d/d_0$ of the whole process, and Fig. 3(b) shows the change in the interaction strength between the HRIP and CNT, which shows a similar trend to that of the ellipsoidal SmtA molecule in CNT reported by Kang [30]. Fig. 3(a) shows that the small peak in the curve after 1 ns represents the self-adjustment of the HRIP before it begins to enter the CNT. Correspondingly, Fig. 3(b) demonstrates no obvious change interaction strength for the HRIP-CNT system. $d/d_0$ begins to drop after 1 ns. The decrease of $d/d_0$ is slower during the interval of $2.3$ ns $< t < 3.3$ ns. This phenomenon indicates that HRIP encountered a resistance at the mouth of the CNT after approaching the end of the CNT and un- derwent self-adjustment. Fig. 2 illustrates that one-third of the HRIP has entered the CNT at this point. Then, $d/d_0$ decreases more quickly, indicating that the adjusted HRIP smoothly entered the CNT. At 6.0 ns, the HRIP arrived at the center of the CNT. The snapshot at this point is shown in Fig. 2. During the insertion, as shown in Fig. 3, the interaction strength of HRIP-CNT decreased with the decrease in $d/d_0$. The interaction strength of HRIP-CNT at this point decreased to $216.2$ kcal mol$^{-1}$ compared with that in the initial configuration. Hence, the interaction strength between the HRIP and CNT plays an important role in the encapsulation process, similar to the results from previous reports on the biomolecule- CNT complex [16,18]. Subsequently, the HRIP moved to and from the center of the CNT, and the amplitudes of the oscillations

![](./images/813243923022479360_6.jpg)

Fig. 3. (a) Normalized COM distance $d/d_0$ between the peptide and the CNT as a function of simulation time, where $d_0$ is the initial COM distance. (b) Interaction strength between the HRIP and (17, 17) CNT as a function of simulation time.

![](./images/813243923022479360_7.jpg)

Fig. 4. RMSD of the HRIP as a function of simulation time corresponding to the (17,17) CNT system.

increasingly became smaller. Fig. 3(b) also shows that the interaction strength of the HRIP-CNT system has a low value. More intuitive illustration for the interaction strength between HRIP and CNT as a function of $d/d_0$, which can be used to assess qualitatively the stable area of the HRIP in the CNT, has been presented in the Supporting Information. The denser curve corresponding to a certain value of $d/d_0$ indicates that the HRIP remained at this point for a longer period. The figure shows that the $d/d_0$ range from 0.0 to 0.4 is the densest of the curve and the lowest interaction strength of HRIP-CNT, which indicates the encapsulation region of the HRIP into the CNT.

### 3.2. Conformational changes in HRIP

The RMSD of the peptide/protein in the dynamic process can be used to describe its conformational changes. Fig. 4 shows that the RMSD of the HRIP evolves with time, which indicates that the HRIP underwent a process, including two dramatic and one gradual period of conformational changes (marked in yellow, cyan, and green). During the first period, the HRIP undergoes a rapid self-adjusting conformational change because of the attraction from the CNT. In the next period, the HRIP undergoes a dramatic conformational change because the near and far parts of the HRIP from the end of the CNT are subjected to different interactions from the CNT, which corresponds to the HRIP insertion to the CNT. After the HRIP is entirely encapsulated, the difference in the aforementioned interactions quickly decreases, which results in the decrease in RMSD. However, the HRIP also undergoes conformational change along the radial direction because of the attraction from the CNT wall. The effects of the two kinds of changes decrease the RMSD

Table 1
Secondary-structure changes in HRIP. Here, the codes C, E, T, and B stand for the coil, $\beta$-sheet, turn, and isolated bridge, respectively. ResID indicates the sequence ID number of amino acid, and resName represents the abbreviation of each residue.

<table>
<thead>
<tr>
<th>resID</th>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
<th>11</th>
</tr>
</thead>
<tbody>
<tr>
<td>resName</td>
<td></td>
<td>C</td>
<td>L</td>
<td>G</td>
<td>I</td>
<td>G</td>
<td>S</td>
<td>C</td>
<td>A</td>
<td>A</td>
<td>P</td>
<td>A</td>
</tr>
<tr>
<td>Secondary structure</td>
<td>0 ns</td>
<td>C</td>
<td>B</td>
<td>C</td>
<td></td>
<td></td>
<td></td>
<td>E</td>
<td></td>
<td>C</td>
<td>T</td>
<td></td>
</tr>
<tr>
<td></td>
<td>27.5 ns</td>
<td>C</td>
<td>B</td>
<td>C</td>
<td></td>
<td></td>
<td></td>
<td>E</td>
<td></td>
<td></td>
<td>T</td>
<td></td>
</tr>
<tr>
<td>resID</td>
<td></td>
<td>12</td>
<td>13</td>
<td>14</td>
<td>15</td>
<td>16</td>
<td>17</td>
<td>18</td>
<td>19</td>
<td>20</td>
<td>21</td>
<td></td>
</tr>
<tr>
<td>resName</td>
<td></td>
<td>G</td>
<td>C</td>
<td>G</td>
<td>T</td>
<td>A</td>
<td>V</td>
<td>V</td>
<td>C</td>
<td>P</td>
<td>T</td>
<td></td>
</tr>
<tr>
<td>Secondary structure</td>
<td>0 ns</td>
<td></td>
<td>C</td>
<td>C</td>
<td>E</td>
<td></td>
<td>T</td>
<td></td>
<td></td>
<td>C</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>27.5 ns</td>
<td></td>
<td></td>
<td>E</td>
<td></td>
<td></td>
<td>T</td>
<td></td>
<td></td>
<td>C</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/813243923022479360_8.jpg)

Fig. 5. (a) Normalized COM distance $d/d_0$ between the HRIP and the CNTs with different sizes as a function of simulation time. (b) Interaction strength between the HRIP and the CNTs with different sizes as a function of simulation time.

![](./images/813243923022479360_9.jpg)

Fig. 6. RMSD of the HRIP as a function of simulation time corresponding to CNTs with different size systems.

rapidly first but gradually increase in the next period. The two kinds of conformational changes reach equilibrium when the HRIP reaches the central range of CNT. Finally, the RMSD remains oscillating slightly at approximately 1.7 Å, which implies that the HRIP reaches conformational stability in the CNT, although the conformational change is not large. The secondary structure of the HRIP is also used to show the change in the encapsulation. Table 1 lists the initial and final results of the secondary structures of the HRIP evaluated using the VMD sequence viewer. Only a small peptide coil (specified by C) transforms into a $\beta$-sheet (marked by E), which confirms that the change in the HRIP structure is small after encapsulation in the (17, 17) CNT. The change also suggests that the $\beta$-sheets and the coil are unstable because they can easily transform into each other. The conclusion that an enzyme undergoes a dramatic decrease in its $\beta$-sheets content after adsorption in the CNTs can be used to explain the experimental results [41]. The encapsulation effect on the CNT is different from the adsorption effect on the hydrophobic graphite surfaces, which usually cause large conformational changes and breakdown of the secondary structures of proteins/peptides [42-44]. The (17, 17) CNT can offer a balanced attractive interaction with the cylindrical wall of the CNT, preventing severe conformational change in the spheroidal HRIP. However, the hydrophobic graphite surface exerts a strong attraction from one side of the protein/peptide, which easily results in changes in the conformations of the protein/peptide.

### 3.3. Effect of diameter of CNT on HRIP

To investigate the effect of the diameters of CNTs on the HRIP, we employed armchair (16, 16), (17, 17), (18, 18), (19, 19), and (20, 20) CNTs to encapsulate the HRIP. Fig. 1 shows that all the considered CNTs can successfully absorb HRIP. However, they exert different effects on the conformational changes of the HRIP.

Fig. 5(a) shows that the insertion time is approximately the same for the considered CNTs except that of the (16,16) CNT. Larger

![](./images/813243923022479360_10.jpg)

Fig. 7. Cross-sectional snapshots of the final configuration of the HRIP with the armchair (17, 17), (18, 18), (19, 19), and (20, 20) CNT systems.

interaction strength of the HRIP-CNT system indicates more stability. Comparing the three curves corresponding to (19, 19), (18, 18), and (17, 17) CNTs in Fig. 5(b), all the interaction strength are large and increase as the CNT becomes smaller, which indicates that these HRIP-CNT systems have higher stable energy.

Fig. 5(a) shows that the insertion process for the (16, 16) CNT requires the longest time because the HRIP must self-adjust its conformation to a greater degree to satisfy the small diameter of the CNT. Fig. 5(b) also shows that HRIP-(16,16) CNT has the largest interaction strength. To evaluate the interaction strength quantitatively, we calculated the mean values and deviations in 15.0-27.5 ns. They are $-231.2 \pm 3.9$, $-216.1 \pm 4.1$, $-179.7 \pm 5.7$, $-150.3 \pm 2.8$, $-216.3 \pm 6.2$ kcal/mol for (16, 16) to (20, 20) CNTs, respectively. It confirms that the interaction of HRIP-(16,16) CNT is the strongest.

However, Fig. 6 shows that its RMSDs are much larger than those of the HRIP in the (17, 17) CNT, which implies that the structure of the HRIP in the (16, 16) CNT has changed. The insertion processes for the (18, 18) and (19, 19) CNTs are smooth, but the weaker interaction shown in Fig. 5(b) indicate that the two HRIP-CNT complexes are less stable. Moreover, Fig. 6 shows that the RMSDs of the HRIP in the two CNTs are larger than that in the (17, 17) CNT. In addition, the interaction strength for the HRIP-(20,20) CNT are low, whereas the RMSDs are very large (Fig. 6), which implies that the HRIP conformation may have been significantly changed. The large conformational change in the CNTs with large diameters is due to the tendency of HRIP to approach one side of the CNT wall with large diameter as a result of the attraction of the CNT. Fig. 7 shows that when the HRIP is close to one part of the (20, 20) CNT wall, it is also far from the other part of the wall. The effect on the CNT is similar to the adsorption on the graphite surface, which causes the HRIP to suffer unbalanced attractions from the wall. Then, obvious conformational change in the spheroidal HRIP occurs. Considering the insertion time, energy stability, and conformational changes, we can conclude that the (17, 17) CNT is the optimal candidate for encapsulating HRIP.

To understand the overall size of HRIP in the SWNT, we calculated the radii of gyration ($R_g$) of HRIP. $R_g$ is defined as:

$$
R_{g}=\sqrt{\frac{1}{N}\left\langle\sum_{i=1}^{N}\left(r_{i}-r_{\mathrm{com}}\right)^{2}\right\rangle}
\tag{8}
$$

where $r_i$ and $r_{\text{com}}$ indicate the position vector of each atom and the vector of center-of-mass. If $R_g$ increases, it shows the expansion. The $R_g$ vs. simulation time of protein in each of the HRIP-CNT simulations is presented in Supporting Information. The mean values of $R_g$ in 15-27.5 ns are $10.78 \pm 2.12, 11.78 \pm 1.18, 11.86 \pm 1.07$, $12.16 \pm 1.17, 14.16 \pm 1.29\mathring{\text{A}}$, respectively. Comparing the $R_g$s of HRIP in the different CNTs with the $7.86 \pm 0.21 \mathring{\text{A}}$ of $R_g$ in pure water, we can find that all the CNTs bring the HRIP stretching. The smallest $R_g$ but largest deviation is found for the case of (16, 16) CNT, which means the HRIP fluctuates more intensively in this CNT. Meanwhile, the largest stretch is found in the case of (20,20) CNT. The $R_g$ is near two times of that in pure water, which implies the geometry of HRIP has obviously changed. Combining $R_g$ and its deviation, one can conclude (17, 17) CNT should be the best candidate for encapsulation of HRIP.

## 4. Conclusions

In summary, the spontaneous insertion process of HRIP into CNTs with different diameters has been investigated using MD simulation. The results of the present study showed that the driving force of the spontaneous movement of HRIP is the van der Waals attraction force between the CNT and HRIP. The HRIP undergoes a conformational adjustment to enter the CNTs. After encapsulation into the CNTs, the HRIP maintains an oscillatory behavior around the center of the tubes. The interaction strength between the HRIP and CNT, as well as the conformational changes in the HRIP, is remarkably influenced by the CNT diameter. The (17, 17) CNT was able to encapsulate the HRIP with a deeper interaction energy well and caused less conformational change in the HRIP. This condition enabled this CNT to be the most appropriate candidate for encapsulating HRIP. More investigations will be performed to manufacture practical CNT-based devices for the delivery of inhibitor, vaccine, and drugs in the future.

## Acknowledgments

This work was supported in part by the National Science Foundation of China under Grant Nos. NSFC-11174117 and NSFC-10974078 and in part by the Shandong Province Natural Science Foundation of China (ZR2011AL010).

## Appendix A. Supplementary data

Supplementary data related to this article can be found at http://dx.doi.org/10.1016/j.cap.2013.02.004.

## References

[1] S. Iijima, Nature (London) 354 (1991) 56.
[2] Y. Lin, S. Taylor, H.P. Li, K.A.S. Fernando, L.W. Qu, W. Wang, L.R. Gu, B. Zhou, Y.P. Sun, J. Mater. Chem. 14 (2004) 527.
[3] A.C. Dillon, K.M. Jones, T.A. Bekkedahl, C.H. Kiang, D.S. Bethune, M.J. Heben, Nature (London) 386 (1997) 377.
[4] K.A. Park, K. Seo, Y.H. Lee, J. Phys. Chem. B 109 (2005) 8967.
[5] L. Zhou, Z.Y. Pan, Y.X. Wang, J. Zhu, T.J. Liu, X.M. Jiang, Nanotechnology 17 (2006) 1891.
[6] B.R. Azamian, J.J. Davis, K.S. Coleman, C.B. Bagshaw, M.L. Green, J. Am. Chem. Soc. 124 (2002) 12664.
[7] J.V. Veetil, K. Ye, Biotechnol. Prog. 23 (2007) 517.
[8] D.T. Mitchell, S.B. Lee, L. Trofin, N. Li, T.K. Nevanen, H. Söderlund, C.R. Martin, J. Am. Chem. Soc. 124 (2002) 11864.
[9] N.W.S. Kam, M. O'Connell, J.A. Wisdom, H. Dai, Proc. Natl. Acad. Sci. 102 (2005) 11600.
[10] A. Hirsch, Angew. Chem. Int. Edit 41 (2002) 1853.
[11] R.J. Chen, Y. Zhang, D. Wang, H. Dai, J. Am. Chem. Soc. 123 (2001) 3838.
[12] L. Lacerda, A. Bianco, M. Prato, K. Kostarelós, Adv. Drug Deliv. Rev. 58 (2006) 1460.
[13] N.W.S. Kam, T.C. Jessop, P.A. Wender, H. Dai, J. Am. Chem. Soc. 126 (2004) 6850.
[14] N.W.S. Kam, H. Dai, J. Am. Chem. Soc. 127 (2005) 6021.
[15] P. Cherukuri, S.M. Bachilo, S.H. Litovsky, R.B. Weisman, J. Am. Chem. Soc. 126 (2004) 15638.
[16] H. Gao, Y. Kong, D. Cui, C.S. Ozakan, Nano Lett. 3 (2003) 471.
[17] Q.X. Pei, C.G. Lim, Y. Cheng, H. Gao, J. Chem. Phys. 129 (2008) 125101.
[18] Y. Kong, Q. Wang, Y.C. Liu, T. Wu, Q. Chen, W.J. Guan, J. Phys. Chem. B 112 (2008) 4801.
[19] S.C. Tsang, J.J. Davis, M.L.H. Green, H.A.O. Hill, Y.C. Leung, P.J. Sadler, Chem. Commun. 17 (1995) 1803.
[20] Y.H. Xie, A.K. Soh, Mater. Lett. 59 (2005) 971.
[21] T.A. Hilder, J.M. Hill, Micro & Nano Lett. 3 (2008) 41.
[22] Q. Chen, Q. Wang, Y.C. Liu, T. Wu, Y. Kong, J.D. Moore, K.G. Gubbins, J. Chem. Phys. 131 (2009) 015101.
[23] A.K. Jana, N. Sengupta, Biophys. J. 102 (2012) 1889.
[24] Z.M. Fu, Y. Luo, P. Derreumaux, G.H. Wei, Biophys. J. 97 (2009) 1795.
[25] R.R. Johnson, B.J. Rego, A.T.C. Johnson, M.L. Klein, J. Phys. Chem. B 113 (2009) 11589.
[26] K. Ajima, T. Murakami, Y. Mizoguchi, K. Tsuchida, T. Ichihashi, M. Yudasaka, ACS Nano 2 (2008) 2057.
[27] R.V. Duyne, J. Cardenas, R. Easley, W.L. Wu, K. Kehn-Hall, Z. Klase, S. Mendez, C. Zeng, H. Chen, M. Saifuddin, F. Kashanchi, Virology 376 (2008) 308.
[28] E. Agbottah, N.G. Zhang, S. Dadgar, A. Pumfery, J.D. Wade, C. Zeng, F. Kashanchi, Virology 345 (2006) 373.
[29] J.W. Shen, T. Wu, Q. Wang, H.H. Pan, Biomaterials 29 (2008) 513.
[30] Y. Kong, Y.C. Liu, Q. Wang, T. Wu, W.J. Guan, Biomaterials 30 (2009) 2807.
[31] Y. Kang, Q. Wang, Y.C. Liu, J.W. Shen, T. Wu, J. Phys. Chem. B 114 (2010) 2869.
[32] D. Fréchet, J.D. Guitton, F. Herman, D. Faucher, G. Helynck, B.M.D. Sorbier, J.P. Ridoux, E. James-Surcouf, M. Vuilhorgne, Biochemistry 33 (1994) 42.

[33] J.C. Phillips, R. Braun, W. Wang, J. Gumbart, E. Tajkhorshid, E. Villa, C. Chipot, R.D. Skeel, L. Kalé, K. Schulten, Comput. Chem. 26 (2005) 1781.

[34] W. Humphrey, A. Dalke, K. Schulten, J. Mol. Graphics 14 (1996) 33.

[35] W.L. Jorgensen, J. Chandrasekhar, J.D. Madura, R.W. Impey, M.L. Klein, J. Chem. Phys. 79 (1983) 926.

[36] A.D. MacKerell, D. Bashford, M. Bellott, R.L. Dunbrack, J.D. Evanseck, M.J. Field, S. Fischer, J. Gao, H. Guo, S. Ha, D. Joseph-McCarthy, L. Kuchnir, K. Kuczera, F.T.K. Lau, C. Mattos, S. Michnick, T. Ngo, D.T. Nguyen, B. Prodhom, W.E. Reiher, B. Roux, M. Schlenkrich, J.C. Smith, R. Stote, J. Straub, M. Watanabe, J. Wiorkiewicz-Kuczera, D. Yin, M. Karplus, J. Phys. Chem. B 102 (1998) 3586.

[37] J.H. Walther, R. Jaffe, T. Halicioglu, P. Koumoutsakos, J. Phys. Chem. B 105 (2001) 9980.

[38] J.O. Hirschfelder, C.F. Curtiss, R.B. Brid, Molecular Theory of Gases and Liquids, Wiley, New York, 1964.

[39] T. Darden, D. York, L. Pedersen, J. Chem. Phys. 98 (1993) 10089.

[40] D.J. Evans, B.L. Holian, J. Chem. Phys. 83 (1985) 4069.

[41] S.S. Karajanagi, A.A. Vertegel, R.S. Kane, J.S. Dordick, Langmuir 20 (2004) 11594.

[42] G. Raffaini, F. Ganazzoli, Langmuir 26 (2010) 5679.

[43] Y.B. Sheng, W. Wang, P. Chen, Protein Sci. 19 (2010) 1639.

[44] C. Mücksch, H.M. Urbassek, Chem. Phys. Lett. 510 (2011) 252.