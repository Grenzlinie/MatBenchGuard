Mat. Res. Soc. Symp. Vol. 650 © 2001 Materials Research Society

# Computer Simulation Of Energy Dependence Of Primary Damage States In SiC

R. Devanathan*, F. Gao**, and W. J. Weber**
* Department of Metallurgical Engineering, Indian Institute of Technology Madras, Chennai 600036, India
** Pacific Northwest National Laboratory, MS K8-93, P. O. Box 999, Richland, WA 99352, USA

## ABSTRACT
The primary damage state in 3C-SiC has been comprehensively studied by molecular dynamics using a modified Tersoff potential. The simulations examined damage produced by Si and C primary knock-on atoms (PKA) with energies from 0.25 to 30 keV. The study also generated statistics of defect production by simulating a number of PKAs at each energy. The defect production efficiency decreases with increasing PKA energy, as observed previously in metals. However, the cascade lifetime is very short (less than 1 ps), localized melting does not occur, the defect arrangements are highly dispersed, and the tendency for defects to form clusters is much less compared to the case of metals. Frenkel pairs on the C sublattice are more numerous than Si Frenkel pairs, and 10-20% of the displacements are in the form of anti-site defects.

## INTRODUCTION
Silicon carbide is a high temperature and radiation resistant semiconductor with potential applications in industries where direct process monitoring is required under adverse environments [1]. SiC-based composite materials are also promising candidates for structural applications in fission [2] and fusion [3] reactors. Both high-dose ion-implantation and neutron irradiation result in the accumulation of non-equilibrium concentrations of point defects. The microstructural changes brought about by these defects need to be understood in order to realize the full potential of SiC-based materials.

Direct experimental observation of defect creation processes is not possible because the processes take place on small time (ps) and distance (nm) scales. Realistic molecular dynamics simulations performed in conjunction with experiments are needed to fill the gaps in the current knowledge of defect creation and evolution in SiC. Recently, molecular dynamics simulations using the Tersoff potential [4] have been employed to study displacement events and low-energy cascades in SiC [5-9]. The present study extends understanding of the primary damage state in SiC to higher energies and provides statistics of defect production in displacement cascades.

## DETAILS OF THE SIMULATION
Molecular dynamics simulations were performed at 300 K using a version of the MDCASK code [10]. The interatomic potential used was a combination of the Tersoff potential and a first principles repulsive potential and has been described previously [6]. Periodic boundary conditions were imposed along with a damping force at the boundaries to prevent energy leaving the simulation cell from re-entering it at the opposite face. The size of the cell varied from 8000 atoms for damage energies of 0.25 and 0.5 keV to 2 million atoms for 30 keV. The cascades with damage energy less than 1 keV were simulated using a desktop workstation, while the higher energy cascades were simulated using a massively parallel Cray T3E at the

R3.22.1

National Energy Research Supercomputer Center.  The cascades were initiated by giving a randomly chosen Si or C atom a velocity with magnitude appropriate for the damage energy of interest and direction along [001], [110] or [111].  For each damage energy and PKA type, 15 cascades were simulated at energies below 1 keV and 5 cascades at higher energies. The damage energy range simulated corresponds to an actual recoil energy range of 0.5-125 keV, which covers most of the fission spectrum.

# RESULTS AND DISCUSSION

Fig. 1 shows the mean-square displacement of displaced atoms as a function of time subsequent to PKA introduction for a 10 keV Si cascade in SiC.  An atom is considered to be displaced if it becomes separated from its lattice site by a distance greater than one-half of the nearest neighbor distance and does not return to its original site during the simulation.  The cascade lifetime is of the order of 0.1 ps.

![](./images/811669861431246853_1.jpg)

Fig.1. Mean square displacement as a function of time for a 10 keV Si PKA in 3C-SiC.

Fig. 2 shows the primary damage state produced by a 10 keV Si cascade in SiC.  The dimensions of the box shown are 15 nm x 9 nm x 9 nm.  The cascade morphology shown here is typical of high energy cascades (5-30 keV) examined in the present work.  C defects are shown as smaller spheres than Si defects.  C mono-vacancies and mono-interstitials are the predominant defects produced and C Frenkel pairs outnumber Si Frenkel pairs by a factor of about 5. Interstitial and vacancy clusters in which each defect has at least one defect within the nearest neighbor distance account for less than 10% of interstitials and vacancies present.  After examining nearly a 100 cascades, no interstitial cluster containing more than three interstitials

R3.22.2

was observed. In addition to the above defects, anti-site defects are also observed, but correspond to only 10-20% of displacements.

The cascade lifetime in SiC is an order of magnitude smaller than that reported in metals for the same energy [11-13]. In SiC, large clusters are not observed and the size of the largest cluster does not change significantly with increasing energy (1-30 keV). This is in contrast to the case of metals where large clusters containing tens of defects have been observed at the corresponding energies and the size of the largest cluster increases with increasing damage energy [13]. The cascade morphology is linear as opposed to the spherical morphology reported in metals [14]. Local melting does not occur in the cascade and subcascades branch off from the path of the PKA. Interstitials outnumber anti-site defects in SiC in contrast to intermetallic compounds such as $\mathrm{Ni}_{3} \mathrm{Al}$ where the opposite is true [12]. The differences between cascades in SiC and metallic systems may be attributed to the high thermal stability of the SiC crystal and inefficient energy transfer between atoms due to poor atomic packing and the large ratio of masses of Si and C.

![](./images/811669861431246853_2.jpg)

Fig. 2. A 10 keV Si cascade in 3C-SiC

Fig.3 shows the total number of displacements, defined as the sum of the numbers of Frenkel pairs and anti-site defects, as a function of damage energy for Si PKA. Fig. 4 shows the corresponding values for C PKA. The number of displacements increases with damage energy, but the slope decreases on a linear scale (decreasing efficiency). These plots provide information about the statistics of displacement production in cascades. C PKAs produce 10-20% fewer displacements than Si PKAs and the former also produce more C displacements. The ratio of C interstitials to Si interstitials was found to be about 5 for Si PKA and 8 for C PKA.

The decrease in defect production efficiency with increasing damage energy is shown in Fig. 5. This efficiency has been defined as the ratio of displacements determined by the present simulation to that given by $\mathrm{N}_{\text {disp }}$ in the modified Kinchin-Pease equation [15] as

$$
N_{\text {disp }}=\frac{0.4 \cdot E_{P K A}}{E_{d}} \tag{1}
$$

R3.22.3

![](./images/811669861431246853_3.jpg)

Fig. 3. Number of displacements produced by Si PKA for various damage energies

![](./images/811669861431246853_4.jpg)

Fig. 4. Number of displacements produced by C PKA for various damage energies

R3.22.4

where $E_{\text{PKA}}$ is the damage energy and $E_{\text{d}}$ is the displacement threshold energy. $E_{\text{d}}$ has been determined, in the present work, for more than 30 different crystallographic directions for Si and C in both 3C- and 6H-SiC[9]. The displacement threshold energy surface is similar in both these polytypes and is highly anisotropic. The smallest values of $E_{\text{d}}$ observed in the present work are 20 eV for C and 35 eV for Si. Recent, experimental evidence suggests corresponding values of 20 and 24 eV [16]. Analysis of available experimental data [16,17] and the results of the present work suggest that $E_{\text{d}}$ values of 20 and 30 eV, respectively, for C and Si are appropriate for use in the above equation. Since the ratio of C displacements to Si displacements is about 5 for Si PKA, a weighted average $E_{\text{d}}$ of 22 eV was used in eq. (1). The defect production efficiency decreases from 1 for damage energy of 0.25 keV to about 0.37 for 30 keV.

![](./images/811669861431246853_5.jpg)

Fig. 5. Defect production efficiency for Si PKA in 3C-SiC

The extent of atomic mixing in the cascade was determined as a function of damage energy for Si and C PKA by means of the mixing parameter, Q, given by

$$
Q=\frac{\sum_{i=1}^{N} r_{i}^{2}}{6 n_{o} E}. \tag{2}
$$

Here $n_{o}$ is the atomic density, $E$ is the damage energy, and the summation of displacements $r_{i}$ is over all $N$ displaced atoms except the PKA. Q increases from 0.5 at a damage energy of 250 eV to about 2.3 at 5 keV, but saturates thereafter. This saturation was observed for damage energies from 5 to 50 keV and corresponds to a recoil energy range of 12-280 keV. This is much smaller than the mixing parameter of 16 for 10 keV Si in Si and 60 for 10 keV Au in Au reported in the

literature [18]. Within the limits of the error bars, no difference in mixing was observed between Si and C PKA cascades.

## CONCLUSIONS

The primary damage state in displacement cascades produced by C and Si PKA for recoil energies from 0.5 to 280 keV consists predominantly of C Frenkel pairs that outnumber Si Frenkel pairs. Unlike the case of metals and intermetallic compounds, large defect clusters are not observed, most of the defects are mono-vacancies and mono-interstitials, Frenkel pairs outnumber anti-site defects, the mixing parameter is small, and local melting does not take place in the cascade. This indicates minimal rearrangement of atoms in the cascades. The displacement threshold energy surface is highly anisotropic and $E_d$ values of 20 and 30 eV, respectively, are recommended for C and Si.

## ACKNOWLEDGEMENTS

This work is sponsored by the Division of Materials Sciences, Office of Basic Energy Sciences, U.S. Department of Energy under Contract DE-AC06-76RLO 1830 (PNNL).

## REFERENCES

1. M. A. Capano and R. J. Trew, MRS Bull. **22** (3), 19 (1997).
2. J. C. Zink, Power Engineering, October, 10, (1998).
3. L. Giancarli, J. P. Bonal, A. Caso, G. Le Marois, N. B. Morley, and J. F. Salavy, Fusion. Eng. Des. **41**, 165 (1998).
4. J. Tersoff, Phys. Rev. B **39**, 5566 (1989); *ibid*. **49**, 16349 (1994).
5. H. Huang, N. M. Ghoniem, J. K. Wong, and M. I. Baskes, Modell. Simul. Mater. Sci. Eng. **3**, 615 (1995).
6. R. Devanathan, T. Diaz de la Rubia, and W. J. Weber, J. Nucl. Mater. **253**, 47 (1998).
7. R. Devanathan, W. J. Weber, and T. Diaz de la Rubia, Nucl. Instr. and Meth. B **141**, 118 (1998).
8. J. M. Perlado, L. Malerba, A. Sanchez Rubio, and T. Diaz de la Rubia, J. Nucl. Mater. **276**, 235 (2000).
9. R. Devanathan and W. J. Weber, J. Nucl. Mater. **278**, 258 (2000).
10. T. Diaz de la Rubia and M. W. Guinan, J. Nucl. Mater. **174**, 151 (1990).
11. D. J. Bacon, A. F. Calder, F. Gao, V. G. Kapinos, and S. J. Wooding, Nucl. Instr. and Meth. B **102**, 37 (1995).
12. F. Gao and D. J. Bacon, Phil. Mag. A **71(1)**, 43 (1995).
13. D. J. Bacon, F. Gao and Yu. N. Osetsky, J. Comp.-Aid. Mat. Des. **6**, 225 (1999).
14. D. J. Bacon and T. Diaz de la Rubia, J. Nucl. Mater. **216**, 275 (1994).
15. M. J. Norgett, M. T. Robinson, I. M. Torrens, Nucl. Eng. Des. 33 (1975) 50.
16. J. W. Steeds, F. Carosella, G. A. Evans, M. M. Ismail, L. R. Danks, and W. Voegeli, Proceedings of the European Conference on Silicon Carbide and Related Materials 2000.
17. S. J. Zinkle and C. Kinsohita, J. Nucl. Mater. **251**, 200 (1997).
18. K. Nordlund, M. Ghaly, R. S. Averback, M. Caturla, T. Diaz de la Rubia, and J. Tarus, Phys. Rev. B **57(13)**, 7556 (1998).

R3.22.6