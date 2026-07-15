# Rn Atom Inside a Carbon Nanotube Like a Clock

Antônio Maia de Jesus Chaves Neto

Departamento de Física-CCEN, Universidade Federal do Pará, C.P. 479, 66075-110, Belém, PA, Brasil

This system consists of a relaxing Rn atom inside of the rigid and static nanotube. We calculated temporal thermodynamic properties of these devices as molar specific heat and entropy variation at 300 K. The simulation was made by classic molecular dynamics with standard parameterization. These facts could be useful for the construction of new molecular motor and clock.

**Keywords:** Molecular Motor, Molecular Dynamics, Thermodynamics.

## 1. INTRODUCTION

The molecular motor study is still in the beginning and there is a few works about it, besides the importance to the nanomedicine and nanorobots. There is many molecular motor at the nature, for example, the kinesin motor. $^{1,2}$ There are linear molecular motors $^{3-6}$ and rotatory motors. $^{7}$ Brouwer et al. $^{8}$ and Komura et al. $^{9}$ found molecular motor controlled by light $^{10,11}$ and Cumings and Zettl $^{3}$ did a nanopiston. Zheng and Jiang $^{4}$ did a study of van der Waals potential energy versus the diameter of the internal nanotube. Otherwise Legoas et al. $^{5}$ did the first theoretical classical molecular dynamics simulation of the molecular motor. Guo et al. $^{6}$ showed that energy dissipation exists in the molecular motor. There was Brownian motors, $^{12,13}$ trying to explain molecules, for example ATP. $^{14}$ Also, was calculated thermodynamics property like entropy and efficiency. $^{18-20}$ Del Nero and Chaves Neto $^{21}$ simulated molecular motor made by two concentric nanotubes, one inside of the other.

In this work, we propose to simulate one molecular motor using a Radonium atom (Rn) and zigzag carbon nanotube (CNT) to study molar specific heat, molar entropy variation, efficiency changing with the time at 300 K.

## 2. METHODOLOGY

We propose a computational system with the Rn relaxing inside of the CNT (Fig. 1). We also verified that the initial position very close of the extremity results a strong van der Waals gradient of energy potential, i.e., occurs a acting force in the probe.

The CNT has 192 atoms, 23.96 Angstroms of length and 6.04 Angstroms of diameter. The Rn has 1.34 Angstroms of atomic radius.

We did the simulation at vacuum and a run time of 8000 ps, with no cool time and step size equal to 1 fs and temperature of 300 K with the same methodology as Guo et al. $^{6}$ and Chaves Neto. $^{21-23}$

## 3. RESULTS AND DISCUSSION

The Figure 2 shows the energies and temperature *in situ* (TEMP) behavior of molecular motor at 300 K. We can see that when the kinetic energy (EKIN) decreases with the time, the energy potential (EPOT) goes down. The EKIN varies directly proportional to the temperature for all time, as expected for the high temperature systems. There are many oscillations and the CNT almost stops several times. The EPOT is almost constant for all time. The EKIN maximum is 250 kcal/mol, EPOT maximum is 150 kcal/mol, ETOT is 750 kcal/mol and TEMP maximum is 1280 K. The energy lost ($\text{ETOT} - (\text{EKIN} + \text{EPOT})$) is 350 kcal/mol. We observe that the energies decrease very slowly with the time because the energy and TEMP values at 0 ps is smaller than at 6 ps.

Figure 3 shows the molar specific heat of this molecular motor versus time at 300 K. There is one peak at 0 ps and it decreases because there is a lost of energy lost by atoms of this system. After time 120 ps, the molar specific heat turns on asymptotically constant.

Figure 4 presents the molar entropy variation versus time at initial temperature of 300 K. There are many oscillations because of the repulsion between atoms of the $\text{CNT} + \text{Rn}$ system. There is a period of increase of the molar entropy variation. It is caused by the thermal energy gain by external temperature received by this motor.

Figure 5 displays the efficiency (EKIN/ETOT) of this motor at initial temperature of 300 K. The efficiency oscillates a lot because of the collisions between $\text{CNT} + \text{Rn}$ atoms. The efficiency decreases at the collisions of CNT

![](./images/811890244080107524_1.jpg)

Fig. 1. The initial position of the Rn atom probe (Rn) and the carbon nanotube (CNT), which oscillates like a molecular motor.

![](./images/811890244080107524_2.jpg)

Fig. 2. Kinetic energy (EKIN), potential energy (EPOT), total energy (ETOT) (kcal/mol) and temperature in situ (TEMP) (Kelvin) versus time at initial temperature 300 K.

with the branch at 37 ps and 100 ps. At 0; 65 and 140 ps there are an efficiency maximum gained by the external heat.

Figure 6 shows the rate EKIN/TEMP of Rn at 300 K. It has a oscillating form and this rate change with the time and it is zero when the Rn stops at the extreme of the CNT during 0.1 ps. The maximum value is 0.19 kcal/(mol K).

Comparing the Figures 2, 4, 5 and 6, when the Rn stops at the extremity oscillates the molar entropy variation, the efficiency and the rate EKIN/TEMP. The molar entropy variation is inversely proportional to the efficiency; it

![](./images/811890244080107524_3.jpg)

Fig. 3. Molar specific heat versus time at initial temperature 300 K.

![](./images/811890244080107524_4.jpg)

Fig. 4. Molar entropy variation (kcal/(mol K)) versus time at initial temperature 300 K.

![](./images/811890244080107524_5.jpg)

Fig. 5. Efficiency versus time at initial temperature 300 K.

![](./images/811890244080107524_6.jpg)

Fig. 6. EKIN/TEMP versus time at initial temperature 300 K.

means that there is a delay of the efficiency and the exchange of information of the atoms.

## 4. CONCLUSIONS

We conclude that the external temperature gives EKIN to the probe in this motor. There is a lost much energy before time 80 ps, after this time try to have a constant value. The oscillating efficiency found here is very low and far from of the Carnot motor. The EPOT decrease and the EKIN increase like a harmonic oscillator. Also, we see that there is a delay of the efficiency and the exchange of information of the atoms. Here, the rate EKIN/TEMP changes with the initial temperature. This system could be used like a specific clock to work at picoseconds to nanoseconds because the period does not vary with very much and there is few lost of energy with the time.

**Acknowledgments:** Antônio Maia de Jesus Chaves Neto thanks the UFPA-PROINT 2006/2007 (Programa Integrado de Apoio ao Ensino, Pesquisa e Extensão).

### References

1.  F. J. Kull, E. P. Sablin, R. Lau, R. J. Fletterick, and R. D. Vale, *Nature* 380, 550 (1996).
2.  M. Kickawa, E. P. Sablin, Y. Okada, H. Yajima, R. J. Fletterick, and N. Hirokawa, *Nature* 411, 439 (2001).
3.  J. Cumings and A. Zettl, *Science* 289, 602 (2000).
4.  Q. Zheng and Q. Jiang, *Phys. Rev. Let.* 88, 45503-1 (2002).
5.  S. B. Legoas, V. R. Coluci, S. F. Braga, P. Z. Braga, P. Z. Coura, S. O. Dantas, and D. S. Galvão, *Phys. Rev. Let.* 90, 55504-1 (2003).
6.  W. Guo, Y. Guo, H. Gao, Q. Zheng, and W. Zhong, *Phys. Rev. Let.* 91, 125501-1 (2003).
7.  H. Miki, M. Sato, and M. Kohmoto, *Phys. Rev. E* 68, 61906 (2003).
8.  A. M. Brouwer, C. Frochot, F. G. Gatti, D. A. Leigh, L. Mottier, F. Paolucci, S. Roffia, and G. W. H. Wurpel, *Science* 291, 2124 (2001).
9.  N. Koumura, R. W. J. Zijistra, R. A. van Delden, N. Harada, and B. L. Feringa, *Nature* 401, 152 (1999).
10. R. A. van Delden, N. Koumura, A. Schoevaars, A. Meetsma, and B. L. Feringa, *Org. Bio. Chem.* 1, 33 (2003).
11. R. A. van Delden, M. K. J. ter Wiel, H. de Jong, A. Meetsma, and B. L. Feringa, *Org. Bio. Chem.* 2, 1531 (2004).
12. D. Dan, A. M. Jayannavar, and G. I. Menon, *Physica A* 318, 40 (2003).
13. K. Sasaki, *J. Phys. Soc. Jpn.* 72, 2497 (2003).
14. H. Y. Moon and Y. Park, *Phys. Rev. E* 67, 51918 (2003).
15. P. P. de Tombe, *J. Biomech.* 36, 721 (2003).
16. H. C. Loebl and C. C. Matthai, *Physica A* 342, 612 (2004).
17. X. Ping, S. X. Dou, and W. Peng-Ye, *Chin. Phys.* 13, 1569 (2004).
18. C. Maes and M. H. van Wieren, *J. Stat. Phys.* 112, 329 (2003).
19. Y. Zhou and J. D. Bao, *Physica A* 343, 515 (2004).
20. A. Igarashi, H. Goko, and S. Tsukamoto, *Physica A* 325, 62 (2003).
21. J. Del Nero and A. M. J. C. Neto, *J. Comput. Theor. Nanosci.* 4, 606 (2007).
22. A. M. J. Chaves and J. Del Nero, *J. Comput. Theor. Nanosci.* 4, 107 (2007).
23. A. M. J. C. Neto, *J. Comput. Theor. Nanosci.* 4, 611 (2007).

Received: 25 May 2007. Accepted: 14 June 2007.