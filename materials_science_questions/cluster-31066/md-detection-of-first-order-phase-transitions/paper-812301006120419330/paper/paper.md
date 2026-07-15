Journal of the Physical Society of Japan
Vol. 67, No. 3, March, 1998, pp. 899-902

# Molecular Dynamics Study of Structures and Phase Transitions in $C_{76}(D_{2})$ Crystals

Takeshi NISHIKAWA and Kohei YOKOI¹

Department of Instrumentation Engineering, Faculty of Science and Technology, Keio University,
3-14-1 Hiyoshi, Kohoku-ku, Yokohama 223
¹Department of Applied Physics and Physico-Informatics, Faculty of Science and Technology, Keio University,
3-14-1 Hiyoshi, Kohoku-ku, Yokohama 223

(Received December 12, 1996)

Crystal structures of $C_{76}$ with $(D_{2})$ symmetry were calculated by molecular dynamics simulation using reliable potential function. We observed three phases in the crystal structure, a face center cubic ($fcc$) and two hexagonal ($hex1$, and $hex2$). The lattice constants and transition temperatures of $fcc$ and $hex2$ were good in agreement with experiments. The lattice constants of the crystals were $a = 15.50$ Å for the $fcc$ and $a = 10.93$, $c = 17.50$ Å for the $hex2$, respectively, at room temperature. The transition temperatures were about 200 K for the $fcc$, and about 350 and 500 K for the $hex2$. However any phase corresponding to the $hex1$ has not been reported in experiments. The lattice constants were $a = 10.50$, $c = 18.42$ Å at room temperature and transition temperatures were about 100 and 400 K. The calculated lattice stabilizing energy and density of $hex1$ were greater than those of $hex2$.

KEYWORDS: C76, molecular dynamics, MD, crystal, phase transition

## §1. Introduction

The discovery of methods to mass-produce fullerene has contributed to the experimental investigation of the crystal structures of fullerene solids.¹,²) The subtle difference of the molecular shapes and sizes, depending on molecular weight, is the cause of different characteristics in the crystal structures and phase transitions. These differences in characteristics are closely related to the anisotropic molecular rotation as follows. The crystal structure of nearly spherical $C_{60}$ molecules is a $fcc$ structure at room temperature, because of the quasi-free molecular rotation at a speed of over $10^{9}$ revolutions per second, but transforms to a simple cubic structure at 260 K by a molecular orientational ordering.³⁻⁸) Though the shape of $C_{70}$ molecules is spheroid, the crystal is also a $fcc$ structure at high temperatures, because of the quasi-free rotation. However, the $fcc$ structure transforms to a monoclinic structure via a rhombohedral structure by cooling. In the case of $C_{70}$, the rotation around the twofold short axes freezes at 340 K, followed by freezing around the fivefold long axis at 280 K. The crystal structure of the next higher fullerene, $C_{76}$, is a $fcc$ or hexagonal close packed ($hcp$) structure, depending on the conditions of experiments.¹⁴,¹⁵) However, the investigation is not as complete compared with that of $C_{60}$ and $C_{70}$, since $C_{76}$ is still a minor product. $C_{76}$ has a couple of optical isomers with $D_{2}$ symmetry. However the mixture of them has been used in all the experiments ever reported because of the difficulty of separation. We and other groups have succeeded in representing these orientational freezing phase transitions in the crystal of $C_{60}$ and $C_{70}$ by the method of Molecular Dynamics (MD).⁹⁻¹³) The MD simulation of $C_{76}$ crystal has not been reported.

In this paper, we report the results of MD simulations of the crystals of one-handed chiral $C_{76}$ molecules with $D_{2}$ symmetry. The phase transitions of $C_{76}(D_{2})$ resulting from molecular orientational orderings were observed by lowering temperature, in good agreement with the results of NMR¹⁶) and X-ray experiments.¹⁵) However, in contrast to the experimental results and the results on $C_{60}$ and $C_{70}$, two different hexagonal phases were observed, depending on the simulations. The mechanism of the phase transitions are proposed.

## §2. Simulation and Model

The molecule is a single chiral isomer of $C_{76}$ which geometry was optimized by a MNDO-PM3¹⁷) quantum chemistry calculation with the initial geometry calculated by FULLER.¹⁸) The molecular structure, shown in Fig. 1, is comparable to the results of the ab initio calculation.¹⁹) The molecule was treated as a rigid-body in this work. The initial position of the molecules in this work was $fcc$ or $hcp$ for the center of molecules, but with random orientations. The crystal $a$ axis parallel to $x$ axis in the Cartesian coordinate, and $c$ axis is parallel to $z$ axis at first.

The intermolecular potential was represented by the atom-atom method. The Buckingham type interatomic potential, $-A/r^{6} + B\exp(-Cr)$, was used with the modified MM3²⁰) parameters: $A = 1.9128 \times 10^{6}$ $\mathrm{\mathring{A}}^{6}$ J/mol, $B = 4.3112 \times 10^{7}$ J/mol, $C = 3.0612$ $\mathrm{\mathring{A}}^{-1}$. The same potential was applied to all atoms of the molecule. The cutoff distance of the interatomic potential was taken as 15 Å. The potential function was good enough to reproduce the crystal structures of $C_{60}$ and $C_{70}$ in the previous calculations.¹³) The periodic boundary condition

![](./images/812301006120419330_1.jpg)
Fig. 1. Molecular structure of $C_{76}(D_{2})$. The principal molecular axes L, M, and N correspond to the longest, middle, and the shortest axis, respectively.

<table>
  <caption>Table I. Calculated lattice constants at 300 K.</caption>
  <thead>
    <tr>
      <th>phase</th>
      <th>$a$ (Å)</th>
      <th>$c$ (Å)</th>
      <th>$c/a$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$fcc$</td>
      <td>15.50</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$hex1$</td>
      <td>10.50</td>
      <td>18.42</td>
      <td>1.754</td>
    </tr>
    <tr>
      <td>$hex2$</td>
      <td>10.93</td>
      <td>17.50</td>
      <td>1.601</td>
    </tr>
  </tbody>
</table>

was applied in each direction of the simulation cell with the period of 4 times longer than the crystallographic unit.

The Newton-Euler equations were integrated numerically by the Gear's predictor-corrector method. $^{21)}$ The pressure was controlled to 1 atm by the Parrinello-Rahman method. $^{22)}$ The temperature was controlled by a velocity scaling method, $^{23)}$ and changed from 900 K to 100 K ($hcp$) or 50 K ($fcc$) in steps. The simulation time step was 2 fs. The data in equilibrium states were collected more than 90 ps after the relaxation during over 30 ps.

§3. Results and Discussion

We observed two hexagonal phases when the initial structure was $hcp$. The ratio of the lattice constants, $c/a$ as shown in Fig. 2, began to increase from 1.633, corresponding to the ideal $hcp$ structure, at about 400 K upon cooling and saturated at 1.673 corresponding to an hexagonal structure at about 100 K in a phase labeled as $hex1$.

The ratio of the lattice constants, $c/a$, began to increase from 1.633, corresponding to the ideal $hcp$ structure, at about 400 K upon cooling and saturated at 1.673 corresponding to a hexagonal structure at about 100 K in a phase labeled as $hex1$. In the other phase labeled as $hex2$, the ratio began to decrease upon cooling from 1.633 ($hcp$) at about 500 K and saturated at 1.599 corresponding to another hexagonal structure at about 350 K. In both phases, the change of the $c/a$ ratio is determined by the change of $c$, since $a$ remains almost constant in this calculation. The calculated lattice constants of $hex1$ and $hex2$ are $a = 10.50, c = 18.42$ and $a = 10.93, c = 17.50$ Å, respectively, at 300 K. The results for $hex2$ are comparable to the experimental results of $a = 10.93$ and $c = 17.72$ Å. $^{15)}$ Although any experimental result corresponding to $hex1$ has not been reported, the changes at 500 and 350 K observed in the $hex2$ phase would correspond to the changes at 420 and 200 K in the X-ray diffraction experiment. $^{15)}$ The phases were also observed on the characteristics of the potential energy, the molecular volume in the crystals, the radial distribution function of molecules at 100 K and the distribution of Euler angle $\theta$ at 100 K, as shown in Figs. 3, 4, 5, and 6, respectively. Though it is preferable to calculate the Gibbs free energy of the crystal to determine which phase is more stable, it is difficult to estimate the contribution of molecular orientation to the entropy. Then we discuss by the potential energy instead of the Gibbs free energy. Representing the molecular orientation, the longest molecular axis, L axis, is parallel to the $z$ axis in the Cartesian coordinate, the middle molecular axis, M axis, parallel to $y$ axis, and the shortest molecular axis, N axis, parallel to $x$ axis. The molecular orientation was given by Euler angles, $(\phi, \theta, \psi)$: first counterclockwise rotation of $\phi$ around $z$ axis, and next $\theta$ around new $x$ axis, and then $\psi$ around new $z$ axis.

![](./images/812301006120419330_2.jpg)
Fig. 2. Ratio of lattice constants, $c/a$, in the hexagonal crystal system.

<table>
  <caption>Table II. Calculated phase transition temperatures and the $c/a$ ratio.</caption>
  <thead>
    <tr>
      <th>phase</th>
      <th>$T_1$ (K)</th>
      <th>$c/a$ at $T_1$</th>
      <th>$T_2$ (K)</th>
      <th>$c/a$ at $T_2$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$fcc$</td>
      <td>200</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$hex1$</td>
      <td>100</td>
      <td>1.673</td>
      <td>400</td>
      <td>1.633</td>
    </tr>
    <tr>
      <td>$hex2$</td>
      <td>350</td>
      <td>1.599</td>
      <td>500</td>
      <td>1.633</td>
    </tr>
  </tbody>
</table>

The $hex1$ phase has a lower potential energy and a smaller volume than $hex2$. However, contrary to the expectation from these results, calculations repeated with different initial conditions generated with the $hex1$ and $hex2$ phases almost the same percentage. In Fig. 6, the molecular L axis aligned with the crystallographic $c$ axis at about $30^\circ$, or $70^\circ$ in the $hex1$, and aligned with that at about $75^\circ$ in the $hex2$. The distribution of Euler angle $\phi$ and $\psi$ in the phases is still random at low temperature.

![](./images/812301006120419330_3.jpg)

Fig. 3. Molecular potential energy in the crystals.

![](./images/812301006120419330_4.jpg)

Fig. 4. Volume per molecule. The experimental data are taken from the results of X-ray diffraction.¹⁵)

![](./images/812301006120419330_5.jpg)

Fig. 5. Radial distribution function (RDF) of the centers of molecules. There are subtle differences at first and second peak in RDF. But the third and forth peak is different from hex1 and hex2.

![](./images/812301006120419330_6.jpg)

Fig. 6. Distribution of Euler angle $\theta$ at 100 K.

![](./images/812301006120419330_7.jpg)

Fig. 7. Schematic picture of the structures of hex1 and hex2 phases. Molecules have random orientations at high temperatures. The $hcp$ structure (...ABAB... stacking) transforms to hex1 or hex2 by lowering temperature.

The schematic picture is given in Fig. 7.

When the initial structure is $fcc$, a phase transition was observed at 200 K on the characteristics of the potential energy in Fig. 3 and the auto-correlation time of molecular rotation in Fig. 8, which would correspond to that observed by the NMR experiment at 150 K.¹⁶) However, it could not be found explicitly on the characteristics of molar volume in Fig. 4. The calculated lattice constant is $a = 15.50$ Å at room temperature, which is comparable to the experimental result 15.42 Å. Until the structure becomes $fcc$ through the calculated temperature range it would be pseudo-$fcc$ at low temperatures, since the molecules have random orientations under 200 K and hardly rotate.

In conclusion, we reproduced the experimentally-observed crystal structures and phase transitions in both the $fcc$ and the hexagonal crystals of $C_{76}(D_2)$ by MD simulations. The explanation for the lack of the experimental observation of the hex1 phase may require further investigations on the calculation using chiral isomer mixtures or experiments using only one-handed chiral isomer.

![](./images/812301006120419330_8.jpg)

Fig. 8. Auto-correlation time of the rotation around the molecular L axis.

### Acknowledgements
We thank the Computer Center, Institute for Molecular Science, Okazaki National Research Institutes, for the use of HP workstations and IBM SP2 computers.. The computation was carried out with the use of PVM and TCGMSG parallel computing environments. $^{24,25)}$

1) H. W. Kroto, J. R. Heath, S. C. O'Brien, R. F. Curl and R. E. Smalley: Nature (London) 318 (1985) 162.
2) W. Krätschmer, L. D. Lamb, K. Fostiropoulous and D. R. Hoffman: Nature (London) 347 (1990) 354.
3) P. A. Heiney, J. E. Fischer, A. R. McGhie, W. J. Romanow, A. M. Denensiein, J. P. McCauley, Jr., A. B. Smith III and D. E. Cox: Phys. Rev. Lett. 66 (1991) 2911.
4) R. Tycko, G. Dabbagh, R. M. Fleming, R. C. Haddon, A. V. Makhija and S. M. Zahurak: Phys. Rev. Lett. 67 (1991) 1886.
5) R. D. Johnson, C. S. Yannoni, H. C. Dorn, J. R. Salem and D. S. Bethune: Science 255 (1992) 1235.
6) Y. Maniwa, M. Nagasaka, A. Ohi, K. Kume, K. Kikuchi, K. Saito, I. Ikemoto, S. Suzuki and Y. Achiba: Jpn. J. Appl. Phys. (Part 2) 33 (1994) L173.
7) G. B. M. Vaughan, P. A. Heiney, J. E. Fischer, D. E. Luzzi, D. A. Ricketts-Foot, A. R. McGhie, Y. W. Hui, A. L. Smith, D. E. Cox, W. J. Romanow, B. H. Allen, N. Coustel, J. P. McCauley, Jr. and A. B. Smith III: Science 254 (1991) 1350.
8) Y. Maniwa, A. Ohi, K. Mizoguchi, K. Kume, K. Kikuchi, K. Saito, I. Ikemoto, S. Suzuki and Y. Achiba: J. Phys. Soc. Jpn. 62 (1993) 1131.
9) A. Cheng and M. L. Klein: J. Phys. Chem. 95 (1991) 6750.
10) A. Cheng and M. L. Klein: Phys. Rev. B 45 (1992) 889.
11) A. Cheng and M. L. Klein: Phys. Rev. B 46 (1992) 4958.
12) M. Sprik, A. Cheng and M. L. Klein: Phys. Rev. Lett. 69 (1992) 1660.
13) T. Nishikawa: Master thesis, Keio University, 1994 [in Japanese].
14) Y. Saito, N. Fujimoto, K. Kikuchi and Y. Achiba: Phys. Rev. B 49 (1994) 14794.
15) H. Nakao: Master Thesis, Tokyo University, 1996 [in Japanese].
16) Y. Maniwa, K. Kume, K. Kikuchi, K. Saito, I. Ikemoto, S. Suzuki and Y. Achiba: Phys. Rev. B 53 (1996) 14196.
17) J. J. P. Stewart: Reviews in Computational Chemistry, ed. K. B. Lipkowitz and D. B. Boyd (VCH Publishers, New York, 1990) Vol. I; J. J. P. Stewart: Semi-empirical molecular orbital calculation using the NDDO (Neglect of Diatomic Differential Overlap) approximation performed with MOPAC Ver. 6.0, QCPE Bull. 9 (1989) 10; revised as Ver. 6.0.1 by K. Nishida (Fujitsu): for Sun SPARC station.
18) M. Yoshida and E. Osawa: Fullerene Science and Technology 1 [1] (1993) 55.
19) S. Nagase and K. Kobayashi: (private communication).
20) J. H. Lii and N. L. Allinger: J. Am. Chem. Soc. 111 (1989) 8576.
21) C. G. Gear: Numerical Initial Value Problems in Ordinary Differential Equations (Prentice-Hall, Englewood Cliffs, NJ, 1971).
22) M. Parrinello and A. Rahmann: Phys. Rev. Lett. 45 (1980) 1196; J. Appl. Phys. 52 (1981) 7182.
23) M. P. Allen and D. J. Tildesley: Computer Simulation of Liquids (Clarendon Press, Oxford, 1989).
24) A. Geist, A. Beguelin, J. Dongarra, R. Manchek, W. Jiang and V. Sunderam: PVM: A Users' Guide and Tutorial for Networked Parallel Computing (MIT Press, Cambridge, Massachusetts, 1994).
25) R. J. Harrison: Int. J. Quant. Chem. 40 (1991) 847.