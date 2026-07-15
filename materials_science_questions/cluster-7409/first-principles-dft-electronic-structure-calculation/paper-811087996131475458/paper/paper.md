# Formation mechanism of conduction path in titanium dioxide with Ti-interstitials-doped: Car–Parrinello molecular dynamics
Jianfeng Yang, Lei Li, Wenshi Li, and Lingfeng Mao

Citation: *AIP Conference Proceedings* **1794**, 020024 (2017); doi: 10.1063/1.4971906
View online: http://dx.doi.org/10.1063/1.4971906
View Table of Contents: http://aip.scitation.org/toc/apc/1794/1
Published by the American Institute of Physics


# Formation Mechanism of Conduction Path in Titanium Dioxide with Ti-Interstitials-Doped: Car–Parrinello Molecular Dynamics

Jianfeng Yang $^{1)}$, Lei Li $^{2, a)}$, Wenshi Li $^{1)}$ and Lingfeng Mao $^{2, b)}$

$^{1)}$Institute of Intelligent Structure and System, School of Electronics & Information Engineering, Soochow University, Suzhou, 215006, P.R. China;
$^{2)}$Institute of Intelligent Structure and System, Soochow University, Suzhou, 215006, P.R. China.

${}^{\text{a)}}$lei_li56@163.com
${}^{\text{b)}}$Corresponding author: mai_lingfeng@aliyun.com

Abstract. The formation mechanism of conduction path in the defected titanium dioxide with two Ti-interstitials is discussed in Car-Parrinello molecular dynamics. In the equilibrated structure, we find the aggregated O-ions where the electrons delocalized. Besides, a belt-like conduction path is produced as the formation of the Ti-Ti bonds at [010] direction. Our work provides the novel view to clarify the resistive switching mechanism in the resistive random access memory device.

Key words: Conduction path; Titanium dioxide; Car-Parrinello molecular dynamics; Ti-interstitials.

## INTRODUCTION

Nonvolatile resistive random access memory (ReRAM) has attracted great attention in recent years [1]. ReRAMs, composed of the metal-insulator-metal structure, and are switched at high or low resistance states under external electric field [2]. Generally, these resistance states are attributed to the formation or disruption of the conductive filament [3]. Titanium dioxide ($\text{TiO}_2$), a transition metal oxide, could successfully present resistive switching phenomena due to the doping of various defects, such as oxygen vacancies and Ti interstitials [4]. The conductive filaments are mainly consisted of the reduced $\text{Ti}_n\text{O}_{2n-1}$ structure with amounts of oxygen vacancies [5, 6].The electrons released during the formation of oxygen vacancies are always captured by the adjacent Ti-ions which are reduced to $\text{Ti}^{3+}$-ions with the metallic characteristics. Therefore, the conductivity of defect $\text{TiO}_{2-x}$ is improved as the increasing of the oxygen vacancies concentrations. Moreover, the Ti interstitials could also produce the reduced $\text{Ti}_{1+x}\text{O}_2$ where $\text{Ti}^{3+}$-ions are found. Different experimental studies have focus on the nature of oxygen vacancy or Ti interstitial on the reduced $\text{TiO}_2$. Henderson *et. al.* reported that the major species diffusing in the ion-sputtered $\text{TiO}_2$ surfaces are Ti interstitials rather than oxygen vacancies [7]. Wendt *et. al.* proposed Ti interstitials in the near-surface region largely contribute to the defect state in the band gap [8]. Therefore, these two defects could probably coexist but with different concentrations. Here, we use Car–Parrinello molecular dynamics to investigate the conduction mechanism of atom-level on $\text{TiO}_2$ with two Ti-interstitials doped. It leads to the diffusion of the partial intrinsic Ti-ions or the O-ions, which determines the formation of the conduction path.

## METHODS

We construct 2×2×4 supercells (a = b = 9.188 Å, c = 11.836 Å) as the initial structure based on the primitive cell of perfect rutile $\text{TiO}_2$ (a = b = 4.594 Å, c = 2.959 Å). Two Ti interstitials are doped in the 2×2×4 supercells at (7.258,

2016 International Conference on Materials Science, Resource and Environmental Engineering
AIP Conf. Proc. 1794, 020024-1–020024-6; doi: 10.1063/1.4971906
Published by AIP Publishing. 978-0-7354-1460-0/$30.00

020024-1

7.258, 4.248) and (7.258, 7.258, 10.166), as two blue-balls shown in Fig. 1(a). These calculations are performed in Car-Parrinello molecular dynamics (CPMD) [9, 10]. Total energies are calculated using Perdew-Burke-Ernzerh function (PBE) in generalized gradient approximation (GGA) [11]. The Kohn-Sham orbitals are expanded by plane wave basis and the energy cutoff is set up to 70 Ry. We used a fictitious mass of 500 a. u. and a time step of 4 a. u. (0.1fs) [12-14]. Troullier-Martin type norm-conserving pseudopotentials are used for each O-ions and Ti-atoms. The target temperature of the ions is firstly set to 300K with the tolerance of 50K in 2000 steps. We use '0 ps' to indicate the structure after the pre-heated calculation above. Then, Nose-Hoover thermostat method (the frequency of ions in 3000 cm⁻¹ and the constant temperature of 300K) is used to run 30000 steps (3ps) [15]. Root-mean-squared deviations (RMSDs) of O-ions are used to determine the equilibration of the structure as shown in Fig. 1(b). The structure finally equilibrates at 1ps. Fig. 1(c) shows the temperature evolution. During 1ps-3ps, the temperatures are fluctuated around 300K, which also shows the equilibrated structure at 1ps.

Properties calculations, such as band structure, density of states, deformation electron density, and Mulliken charges, are performed in Dmol³ package [16]. The exchange-correlation energy in PBE formulation of GGA is also used. Double-numeric quality basis set with the polarization functions (DNP) is set to 3.5. Spin-polarization method is necessary for TiO₂ to produce the realistic characteristics. Monkhorst-Pack k-points of 3×3×2 mesh are sampled to make the whole system converged [17].

![](./images/811087996131475458_1.jpg)

FIG. 1 (a) Schematic diagram of the initial structure; (b) RMSDs of O-ions in 30000 steps (3ps); (c) Temperatures of ions in 30000 steps (3ps).

## RESULTS AND DISCUSSIONS

Fig. 2 depicts the isosurface of the deformation electron density for the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f). The balls in gray and red indicate Ti-ions and O-ions, respectively. The deficiencies of electrons are indicated in yellow, and the enrichment electrons in blue. In Fig. 2(a), the electron enrichment in blue almost locates at each O-ion. However, in Figs. 2(b) -2(f), some O-ions with yellow isosurface are found as dark arrows pointed, which means the electron deficiency around these O-ions. The O-ions pairs with yellow isosurface are increased as the time evolution. At 2ps or 3ps, we find three yellow-sphere-like electron deficiency areas which show three O-ions pairs.

Table 1 shows the detailed positive Mulliken charges of O-ions in the structures at 0ps, 0.5ps, 1ps, 2ps, and 3ps. They are corresponding to one O-ions pairs at 0ps, two O-ions pairs at 1ps, and three O-ions pairs at 2ps or 3ps. It needs to note that one O-ions pairs in the structure at 0.5 ps contains O-ions of 1.859 $e$ and -0.004 $e$ (not indicated in Table 1). So two O-ions pairs are also observed in the structure at 0.5ps. These characteristics are also consistent with results of the isosurface of deformation electron density in Fig. 2.

![](./images/811087996131475458_2.jpg)

FIG. 2 Isosurface of the deformation electron density of the structures for the initial structure (a), and the structure at 0ps (b),
0.5ps (c), 1ps (d), 2ps (e), 3ps (f).

TABLE 1. Detailed positive Mulliken charges of O-ions in the structures at 0ps, 0.5ps, 1ps, 2ps, and 3ps.

<table>
  <thead>
    <tr>
      <th></th>
      <th>0ps</th>
      <th>0.5ps</th>
      <th>1ps</th>
      <th>2ps</th>
      <th>3ps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.15</td>
      <td>0.051</td>
      <td>0.459</td>
      <td>0.412</td>
      <td>0.492</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.041</td>
      <td>0.206</td>
      <td>0.653</td>
      <td>0.554</td>
      <td>0.558</td>
    </tr>
    <tr>
      <td>3</td>
      <td>-</td>
      <td>1.859</td>
      <td>0.487</td>
      <td>0.555</td>
      <td>0.683</td>
    </tr>
    <tr>
      <td>4</td>
      <td>-</td>
      <td>-</td>
      <td>1.277</td>
      <td>0.8</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.874</td>
      <td>0.787</td>
    </tr>
    <tr>
      <td>6</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>1.153</td>
      <td>1.255</td>
    </tr>
  </tbody>
</table>

The slices of the deformation electron density would be discussed in Fig. 3 and 4, which are cleaved at the dash-lines as shown in Fig. 2. We only mark the dash-line in Fig. 2(a). The other dash-lines locate at the same positions in Figs. 2(b)-2(f). Fig. 3 shows the slices of the deformation electron density in (100) facet cleaved at the dash-lines of 'I' in the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f). We set the deformation electron density spectrum to the blue-green-red from -0.08 to 0.01 electron/$\mathring{A}^3$; the deficiencies of electrons are indicated in blue, while the electrons enrichment in red. In Fig. 3(a), the blue areas are corresponding to Ti-ions, while the red ones to O-ions. As the time evolutes, some irregular red areas are produced, which implies the occurrence of the delocalized electron. The irregular red regions around the dark dash circles of Figs. 3(e, f) locate among the two yellow-spheres in Figs. 2(e, f). Here, we conclude that the Ti-interstitials induces the occurrence of O-pairs, this is to say that the aggregation of O-ions.

Fig. 4 shows the slices of the deformation electron density in (001) facet cleaved at the dash lines of 'II' for the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f). As the time evolutes, the irregular red areas are also found in Fig. 4. At 0.5ps, the irregular red areas begin to aggregate as shown at the left side of Fig. 4(c). At 2ps, the aggregated red regions are connected to produce the belt-like red regions as the dash-line shown in Fig. 4(e, f). Thus it illustrates the formation of the conduction path. In comparison of Figs. 4(e, f) and Figs. 2(e, f), we attribute the formation of the conduction path to the occurrence of the Ti-Ti bonds as shown in the dark dash-rectangles of Figs. 2(e, f). Next, we extract the partial structure along the dash-line of 'II' in Fig. 2(e) to build a 3×3×1 supercell as shown in Fig. 5. The slice of the deformation electron density of the fine structure is also shown in Fig. 5. Accordingly, it is clearly seen that the continuous Ti-Ti bonds induces the formation of conductive path due to the doping of two Ti-interstitials.

![](./images/811087996131475458_3.jpg)

FIG. 3 Slices of deformation electron density in (100) facet cleaved at the dash lines of 'I' for the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f).

![](./images/811087996131475458_4.jpg)

FIG. 4 Slices of deformation electron density in (001) facet cleaved at the dash lines of 'II' for the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f).

Fig. 6 shows Mulliken charges of the Ti-ions in the initial structure and the structures at 0ps, 0.5ps, 1ps, 2ps, and 3ps, respectively. As shown in Fig. 6, Mulliken charges of the Ti-ions are mainly less than $1.5\ e$ in the structures at 0.5ps, 1ps, 2ps, and 3ps except those in the structure at 0ps. It means the occurrence of the Ti-ions in the lower valence, such as $\text{Ti}^{3+}$ or $\text{Ti}^{2+}$.

Fig. 7 shows the partial density of states (PDOS) for the initial structure (a), and 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f). The curves in green, red, and blue indicate the p-states, d-states, and sum-states, respectively. In Fig. 7(a), it's clearly seen that these defect energy levels lie at the bottom of the conduction band minimum (CBM). The minimum of the density of states for the defect energy levels equals to 2.24 electrons/eV. So, there is little band gap in the initial structure. As time evolutes, the defect energy levels fill in the bandgap and the corresponding density of states are also increased, which originate from the Ti-3d states and O-2p states. The minimum of the density of states for these defect energy levels are marked in Fig. 7(b-f). Consequently, these band gaps all equal to 0 eV, which means the metallic characteristics in these structures. These defect energy levels also indicate the occurrence of the Ti-ions and O-ions with the lower valence. They are corresponding to the formation of the Ti-Ti bonds and the occurrence of the O-ions pairs.

![](./images/811087996131475458_5.jpg)

FIG. 5 The 3×3×1 supercell of the fine structure along the dash line of ‘II’ of Fig. 2(e).

![](./images/811087996131475458_6.jpg)

FIG. 6 Mulliken charges of the Ti-ions in the initial structure and the structures at 0ps, 0.5ps, 1ps, 2ps, and 3ps.

![](./images/811087996131475458_7.jpg)

FIG. 7 Partial density of states (PDOS) for the initial structure (a), and the structure at 0ps (b), 0.5ps (c), 1ps (d), 2ps (e), 3ps (f).

020024-5

## CONCLUSION

We have studied the formation of conduction path in titanium dioxide with the doping of Ti-interstitials by Car-Parrinello molecular dynamics. In the equilibrated structure at 2ps–3ps, we find the aggregated O-ions pairs with the delocalized electrons. Moreover, the conduction paths composed of Ti-Ti bonds are observed at [010] direction. Therefore, we propose that the Ti interstitials produce the conduction path in titanium dioxide. These works provides helpful guidance to design the resistive random access memory.

## ACKNOWLEDGMENTS

The authors acknowledge the support from the National Natural Science Foundation of China under Grant Nos. 61076102 and 61272105, Natural Science Foundation of Jiangsu Province of China under Grant Nos. BK2012614 and BK20141196.

## REFERENCES

1.  R. Waser, R. Dittmann, G. Staikov, et al. Redox-based resistive switching memories-nanoionic mechanisms, prospects, and challenges. *Advanced Materials*. Vol. 21 (2009) No. 25-26, p. 2632-2663.
2.  D. H. Kwon, K. M. Kim, J. H. Jang, et al. Atomic structure of conducting nanofilaments in TiO2 resistive switching memory. *Nature nanotechnology*. Vol. 5 (2010) No. 2, p. 148-153.
3.  Q. Liu, J. Sun, H. Lv, et al. Real-Time Observation on Dynamic Growth/Dissolution of Conductive Filaments in Oxide-Electrolyte-Based ReRAM. *Advanced Materials*. Vol. 24 (2012) No. 14, p. 1844-1849.
4.  J. J. Yang, F. Miao, M. D. Pickett, et al. The mechanism of Electroforming of Metal Oxide Memristive Switches. *Nanotechnology*. Vol. 20 (2009) No. 21, p. 215201.
5.  K. M. Kim, D. S. Jeong, C. S. Hwang. Nanofilamentary Resistive Switching in Binary Oxide system: a review on the present status and outlook. *Nanotechnology*. Vol. 22 (2011) No. 25, p. 254002.
6.  K. Szot, M. Rogala, W. Speier, et al. TiO2—A Prototypical Memristive material. *Nanotechnology*. Vol. 2 (2011) No. 25, p. 254001.
7.  M. A. Henderson. A Surface perspective on Self-diffusion in Rutile TiO2. *Surface Science*. Vol. 419 (1999) No. 2, p. 174-187.
8.  S. Wendt, P. T. Sprunger, E. Lira, et al. The role of Interstitial Sites in the Ti3d Defect state in the Band Gap of Titania. *Science*. Vol. 320 (2008) No. 5884, p. 1755-1759.
9.  Information on:www.cpmd.org
10. R. Car and M. Parrinello. Unified approach for Molecular Dynamics and Density-Functional Theory. *Physical Review Letters*. Vol. 55 (1985) No. 22, p. 2471-2474.
11. J. P. Perdew, K. Burke, and M. Ernzerhof. Generalized Gradient Approximation made simple. *Physical Review Letters*. Vol. 77 (1996) No. 18, p. 3865.
12. I. F. W. Kuo and C. J. Mundy. An ab initio Molecular Dynamics study of the Aqueous Liquid-vapor Interface. *Science*. Vol. 303 (2004) No. 5658, p. 658-660.
13. P. L. Geissler, C. Dellago, D. Chandler, et al. Autoionization in Liquid Water. *Science*. Vol. 291 (2001) No. 5511, p. 2121-2124.
14. E. Schwegler, J. C. Grossman, F. Gygi, et al. Towards an assessment of the accuracy of Density Functional Theory for First Principles simulations of Water. II. *Journal of Chemical Physics*. Vol. 121 (2004) No. 11, p. 5400-5409.
15. S. Nosé. A Unified Formulation of the Constant Temperature Molecular Dynamics methods. *Journal of Chemical Physics*. Vol. 81 (1984) No. 1, p. 511-519.
16. L. Li, W. Li, A. Ji, et al. Anisotropic Relaxation of a CuO/TiO2 Surface under an Electric Field and its impact on Visible Light Absorption: ab initio calculations. *Physical Chemistry Chemical Physic*. Vol. 17 (2015) No. 27, p. 17880-17886.
17. H. J. Monkhorst and J. D. Pack. Special points for Brillouin-zone Integrations. *Physical Review B*. Vol. 13 (1976) No. 12, p. 5188.

020024-6