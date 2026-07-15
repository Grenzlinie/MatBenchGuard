# Structural and Electronic Properties of Hydrogen-passivated Silicon Quantum Dots: Density Functional Calculations

Muhammad Mus-'ab Anas¹,ᵃ, Ahmad Puaad Othman¹,ᵇ and Geri Gopir ¹,ᶜ

¹ School of Applied Physics, Faculty of Science and Technology, Universiti Kebangsaan Malaysia, 43600 Bangi, Malaysia.
ᵃmus_physics@yahoo.com, ᵇpuaad@ukm.my, ᶜgerigopir@gmail.com

**Keywords:** Density Functional Theory (DFT), Quantum Dots (QDs), HOMO-LUMO gap, LDA-PZ, DOS plot

**Abstract.** Density functional theory (DFT) by numerical basis-set calculations of silicon quantum dots (Si-QDs) passivated by hydrogen, ranging in size up to 1.9 nm are presented. These DFT computation results are used to examine and deduce the properties of 14 spherical Si-QDs including its density of state (DOS), and energy gap from the HOMO-LUMO results. The atomistic model of each silicon QDs was constructed by repeating crystal unit cell of face-centered cubic (FCC) structure, then the QDs surface was passivated by hydrogen atoms. The model was relaxed and optimized using Quasi-Newton method for each size of Si-QDs to get an ideal structure. Exchange-correlation potential ($V_{xc}$) of electrons were approximated in this system using the Local Density Approximation (LDA) functional and Perdew-Zunger (PZ) functional. Finally, all results were compared with previous experimental data and other similar theoretical approaches, and these results augured well.

## Introduction

One of the most outstanding problem in the current rapidly growing field of nano-science is the prediction of nanostructure semiconductor energy gap. Predicting the optical gap of silicon quantum dots is very challenging, since it is dependence on the size of crystal nanostructure. Based on literatures, there are theoretical approaches found to explain this phenomena [1]. Producing samples of pure, crystalline, mono dispersed silicon quantum dots are intensively difficult. Consistent experimental data is another challenge, thus, it is highly desirable to develop an accurate theoretical model to assist in the development of silicon QDs in order to support future technologies. Theoretical researchers need to develop a consistent description of the exchange and correlation (XC) interaction between electrons. This consistent description of XC interactions will then be applied in the systems, ranging from highly inhomogeneous molecules, such as silane ($\text{SiH}_4$), to large clusters approaching the bulk limit.

Computationally, mean-field methods such as density functional theory (DFT), can be applied throughout <2 nm size regime, relying on approximate exchange-correlation function which are well known to yield accurate ground state properties, but slightly underestimating the optical gaps. In this paper we will demonstrate the ability of DFT to predict the optical energy gap of silicon nanostructures ranging in size from a few to several hundred atoms. The DFT approach includes exchange and correlation interactions between all the electrons in the quantum dot on its ground state condition. Results of this computation provide us the basis for understanding of the size dependence on the optical energy gap in silicon quantum dots, and thus enable us to fill some missing structure on previous theoretical approaches. Our DFT-LDA computations were performed using the OpenMX [2] numerical atomic orbitals (NAOs).

## Methodological Background

In this paper, we revisited the accuracy of quantitative estimates on Silicon Quantum-Dots from DFT implementations using numerical atomic orbitals (NAOs). In order to perform the

electronic structure calculation in studying the ground state and other physical properties, there is always a compromise between accuracy and efficiency. Fundamentally, selection of the basis-set play an important role on providing such efficient computation. Iteration convergence of the physical properties with plane waves (PWs) and real-space grids are well controlled by increasing the size of the basis-set, hence, providing a foundation for the electronic structure calculation. However, this approach demands massive computational time and memory requirements [3].

On the other perspective, basis-set that made of atomic orbitals (AOs) can be much smaller. For instance, a dozen of AOs is required per atom instead of hundreds of PWs per atom for a similar quality of the calculation result. Atomic orbitals are routinely used in calculations of atomic and molecular spectra since it is a reasonable starting point. Their convergence properties have been intensively studied for decades [4,5]. Implementations also exist for extended solid-state systems [6] but by comparison, the use of AOs actually is less established. The transferability of tabulated AOs in different environments is an old problem which the construction of numerical atomic orbitals (NAOs) promises improvement in particular, under various schemes of its optimization [6].

In this paper we choose to use the method proposed by Ozaki et al. [6] as implemented in the OpenMX package [2], towards understanding electronic structure of Si-QDs. The selection of silicon basis-set were corresponding to the early studies in bulk-Si which have indicated that a double-zeta polarized (DZP) basis-set may suffice for converged forces in atomic relaxations [7]. This foundation of basis-set is used in our Si-QDs calculation.

## Computational Detail

Hydrogenated Si-QDs with diameter ranging from the lowest until 1.9 nm were constructed by repeating silicon FCC unit cell from its crystal lattice constant until the desired repetition was achieved. Subsequently the remainder atoms will be excluded until the sphere shape formed. Next, the structure will be passivated with hydrogen atom on each surface of the QDs. After the Si-QDs was constructed, we performed a geometry optimization using Quasi-Newton method to get an ideal relaxation structure. The Quasi-Newton method used were the Broyden-Fletcher-Goldfarb-Shanno (BFGS) method [8,9,10,11] all in Cartesian coordinate. An optimized structure then were used to calculate the energy gap, analyzed from HOMO-LUMO data. All the computational methods were done using numerical atomic orbital basis-set in the OpenMX implementation of Ozaki et al. [6]. Norm-conserving pseudopotentials were also used for this simulation.

For density of state (DOS) plotting, the Monkhorst-Pack k-point sampling was set on k=1 for Gamma ($\Gamma$) direction only, while the energy at zero eV was set as Fermi level. An exchange-correlation were treated as Local Density Approximation (LDA) where Perdew-Zunger (PZ) [12] functional was applied. For pseudopotential parameter, as mentioned before, the norm-conserving pseudopotentials have been used throughout the simulations. All the structure of the relaxed Si-QD is shown in Fig. 2.

For the SCF field, the electron temperature was set to 300K as closed to room temperature. Linear Combination Atomic Orbitals (LCAO) basis-set used in the simulation was a double-zeta polarised (DZP) basis-set for Si element while single-zeta for H.

## Result & Discussion

At the beginning of our simulation, the DOS plot was studied to examine the effect of hydrogen passivation on a selected structure. Comparison between DOS on two different type of silicon quantum dots lead us to understand the main role of passivation with hydrogen on the quantum dots surface. Figure 1a & 1b below show the gap shift and enhanced confinement effect on electron at the surface of quantum dot. The dangling bond seems terminated while the confinement of electron increased.

![](./images/814620522485645313_1.jpg)

Figure 1a : DOS plot for bare $Si_{10}$ Silicon Quantum Dot.

![](./images/814620522485645313_2.jpg)

Figure 1b : DOS plot for hydrogen passivated $Si_{10}H_{16}$ Silicon Quantum Dot.

Figure 2 below shows all the 14 structures modelled and visualized using VESTA [13]. All the silicon quantum dots were passivated by hydrogen. Importantly, they were optimized using Quasi-Newton method before continued with an electronic calculation.

![](./images/814620522485645313_3.jpg)

Figure 2 : Atomistic model of relaxed Hydrogenated Silicon Quantum Dots.

Initially, the accuracy of the calculation details were confirmed by implementing selected parameters on the calculation of bulk silicon semiconductor. Using the same parameters as mentioned above, except for hydrogen (since there is no hydrogen element in the pure bulk Si), the crystal lattice structure taken for bulk Si was Face-Centered-Cubic.

![](./images/814620522485645313_4.jpg)

Figure 3 : Bandstructure of bulk Silicon ( Γ-K-X direction ).

From our calculation, the ground state energy gap (E₉) for bulk silicon only result to 0.55eV, far from experimental value. However, we accounted LDA well-known discontinuity issues on Exchange-Correlation as reported by Godby et al. [14] by adding 0.58eV, as correction value will give us the result 1.13eV, which is much closed to the reference, E₉=1.12eV at 300k [15]. Hence, this indicate that our computational details are acceptable to be extended on electronic properties of silicon crystal.

Theoretically, the value of the energy gap from the energy spectrum decreases, as the size of the dot increases implying weaker confinement for larger sizes. As we increase the number of atoms in the dot and change its geometry of size, the degeneracies should be increasingly lifted. As one saturates the surface dangling bonds with hydrogen atoms, there is an enhancement of the gap energy ~ 2.3 eV for 10 atom cluster as presented on Fig. 1b.

The degeneracies are lifted because the presence of hydrogen at the surface imparts an interaction potential that acts as a perturbation. For relatively larger dot due to $sp^{2}$ and $sp^{3}$ hybridization, de-localization of the electron is more and the energy spectrum is more non-degenerate. For smaller dots this effect of de-localization near the surface is less and hence the degeneracies are more pronounced.

![](./images/814620522485645313_5.jpg)

Figure 4: Present result were compared with other theoretical data and reported experimental work.

In Figure 4, we presented the results of our simulation for the variation of energy gap on different sizes of the Si-QD with hydrogen-passivation. At first, we noticed that our computational results were exactly same with DFT-LDA PWs calculation by Williamson et al. However, as mentioned earlier, we had accounted the discontinuity issues on Exchange-Correlation correction by 0.58eV for each size of QDs, leading us closer to the experimental value. The bigger energy gap is due to the localization of electron cloud arising from the $sp^{3}$ hybridization of the silicon-dangling

bond with the hydrogen atom. These results are in conformity with the earlier observation[1]. Finally, we verify our atomistic model by comparing our HOMO-LUMO energy gap with the previous theoretical LDA result by Williamson et al.[16] and experimental study [17,18,19] as shown in figure 4. Our atomistic model augured well with the others.

## Conclusion
This paper explained the used of numerical atomic orbitals method to calculate electronic structure of silicon quantum dots of different sizes, up to almost 2 nm , occupying 5 to 147 of Silicon atoms in order to examine the quantum size effects on energy gap. Our results is in agreement that the energy gap increases as the size of the dot decreases, where stronger confinement implies on the smaller dots. This result is also in conformity with the earlier observations by Wang and Zunger [20] and others. The energy gap seems to increase accordingly reaching the ultraviolet region of 3.10eV under 1.6nm diameter of Si-QDs. The presence of hydrogen on the surface of quantum dots, lifts the degeneracies of the eigenvalue spectrum and results in the enhancement of the energy gap. Wolkin et al.[19] reported that the photoluminescence characteristics are determined by both quantum confinement and surface passivation. This implies that passivated surface state has significant impact on energy gap, besides finite size of quantum dots.

Our computational results shows that the use of NAOs could be an efficient method, alternative to plane waves, in calculating the electronic properties of silicon quantum dots. We also confirm that, although the LDA calculations underestimated the band gap, our results are consistent with the trend that quantum confinement effect depends on the function of quantum dot size. The highest relative deviation of the LDA calculated band gap difference, compared with the corresponding experimental result is only below 30% for 1.9nm Si-QD. Based on our research, it is also noticed that microscopic approach to study QDs electronic structure are only sufficient for small size of quantum dots calculation. However, in this aspect, it require a lot of computational power, high time-consume and difficult to be applied on the large size of quantum dots.

## Acknowledgement
We would like to thank the Ministry of Education Malaysia (Higher Education) for financial support through grant of ERGS funding ERGS/1/2012/STG02/UKM/02/3 and MyBrain15 scholarship for candidate financial support.

## References
[1] C. S. Garoufalis, A. D. Zdetsis, and S. Grimme, High Level Ab Initio Calculations of the Optical Gap of Small Silicon Quantum Dots, Phys. Rev. Lett. 87 (2001) 276402

[2] Information on http://www.openmx-square.org/.

[3] S. Goedecker, Linear scaling electronic structure methods, Rev. Mod. Phys. 71 (1999) 1085-1123.

[4] S. Huzinaga, Basis sets for molecular calculations, Comput. Phys. Rep. 2 (1985) 281-339.

[5] V. Blum, R. Gehrke, F. Hanke, P. Havu, V. Havu, X. Ren, K. Reuter, M. Scheffler, Ab initio molecular simulations with numeric atom-centered orbitals, Comput. Phys. Commun. 180 (2009) 2175–2196.

[6] T. Ozaki, Variationally optimized atomic orbitals for large-scale electronic structures, Phys. Rev. B 67 (2003) 155108.

[7] J.S. Nelson, E.B. Stechel, A.F. Wright, S.J. Plimpton, P.A. Schultz, M.P. Sears, Basis-set convergence of highly defected sites in amorphous carbon, Phys. Rev. B 52 (1995) 9354-9359.

[8] C. G. Broyden, The convergence of a class of double rank minimization algorithms, J. Inst. Math. Appl. 6 (1970) 76;

[9] R. Fletcher, A new approach to variable metric algorithms, Comput. J. 13 (1970) 317;

[10] D. Goldrarb, A family of variable metric methods derived by variational means, Math. Comp. 24 (1970) 23;

[11] D. F. Shanno, Conditioning of quasi-Newton methods for functional minimization, Math. Comp. 24 (1970) 647.

[12] J. P. Perdew and A. Zunger , Self-interaction correction to density-functional approximations for many-electron systems, Phys. Rev. B 23 ( 1981) 5048-5079

[13] Information on http://jp-minerals.org/vesta/en/

[14]R. W. Godby, M. Schlüter, and L. J. Sham, Accurate exchange-correlation potential for silicon and its discontinuity on addition of an electron, Phys. Rev. Lett. 56 (1986) 2415-2418

[15] Bart J. Van Zeghbroeck, Principles of Electronic Devices, 1996, digital ebook available at http://www.eletrica.ufpr.br/graduacao/e- books/Principles%20Of%20Semiconductor%20Devices.pdf .

[16] A. J. Williamson et al., Quantum Monte Carlo Calculations of Nanostructure Optical Gaps: Application to Silicon Quantum Dots, Phys. Rev. Lett. 89 (2002) 196803

[17] F. Fehér, *Forschungsbericht des Landes NRW* (Westdeutscher Verlag, Köln, 1977).

[18] J. P. Wilcoxon, G. A. Samara, and P. N. Provencio, Optical and electronic properties of Si nanoclusters synthesized in inverse micelles, Phys. Rev. B 60 (1999) 2704-2714.

[19] M.V. Wolkin, J. Jorne, P. M. Fauchet, G. Allan, and C. Delerue., Electronic States and Luminescence in Porous Silicon Quantum Dots: The Role of Oxygen, Phys. Rev. Lett. 82 (1999) 197-200

[20] Wang L W & Zunger A, Electronic Structure Pseudopotential Calculations of Large (.apprx.1000 Atoms) Si Quantum Dots, J. Phys. Chem. 98 (1994) 2158-2165.

SOLID STATE SCIENCE & TECHNOLOGY Towards an Immersive Breakthrough
10.4028/www.scientific.net/AMR.1107

Structural and Electronic Properties of Hydrogen-Passivated Silicon Quantum Dots: Density Functional Calculations
10.4028/www.scientific.net/AMR.1107.571

DOI References

[1] C. S. Garoufalis, A. D. Zdetsis, and S. Grimme, High Level Ab Initio Calculations of the Optical Gap of Small Silicon Quantum Dots, Phys. Rev. Lett. 87 (2001) 276402.
http://dx.doi.org/10.1103/PhysRevLett.87.276402

[3] S. Goedecker, Linear scaling electronic structure methods, Rev. Mod. Phys. 71 (1999) 1085- 1123.
http://dx.doi.org/10.1103/RevModPhys.71.1085

[4] S. Huzinaga, Basis sets for molecular calculations, Comput. Phys. Rep. 2 (1985) 281-339.
http://dx.doi.org/10.1016/0167-7977(85)90003-6

[5] V. Blum, R. Gehrke, F. Hanke, P. Havu, V. Havu, X. Ren, K. Reuter, M. Scheffler, Ab initio molecular simulations with numeric atom-centered orbitals, Comput. Phys. Commun. 180 (2009) 2175-2196.
http://dx.doi.org/10.1016/j.cpc.2009.06.022

[6] T. Ozaki, Variationally optimized atomic orbitals for large-scale electronic structures, Phys. Rev. B 67 (2003) 155108.
http://dx.doi.org/10.1103/PhysRevB.67.155108

[7] J.S. Nelson, E.B. Stechel, A.F. Wright, S.J. Plimpton, P.A. Schultz, M.P. Sears, Basis-set convergence of highly defected sites in amorphous carbon, Phys. Rev. B 52 (1995) 9354-9359.
http://dx.doi.org/10.1103/PhysRevB.52.9354

[8] C. G. Broyden, The convergence of a class of double rank minimization algorithms, J. Inst. Math. Appl. 6 (1970) 76.
http://dx.doi.org/10.1093/imamat/6.1.76

[9] R. Fletcher, A new approach to variable metric algorithms, Comput. J. 13 (1970) 317.
http://dx.doi.org/10.1093/comjnl/13.3.317

[10] D. Goldrarb, A family of variable metric methods derived by variational means, Math. Comp. 24 (1970) 23.
http://dx.doi.org/10.1090/S0025-5718-1970-0258249-6

[11] D. F. Shanno, Conditioning of quasi-Newton methods for functional minimization, Math. Comp. 24 (1970) 647.
http://dx.doi.org/10.1090/S0025-5718-1970-0274029-X

[14] R. W. Godby, M. Schlüter, and L. J. Sham, Accurate exchange-correlation potential for silicon and its discontinuity on addition of an electron, Phys. Rev. Lett. 56 (1986) 2415-2418.
http://dx.doi.org/10.1103/PhysRevLett.56.2415

[16] A. J. Williamson et al., Quantum Monte Carlo Calculations of Nanostructure Optical Gaps: Application to Silicon Quantum Dots, Phys. Rev. Lett. 89 (2002) 196803.
http://dx.doi.org/10.1103/PhysRevLett.89.196803

[18] J. P. Wilcoxon, G. A. Samara, and P. N. Provencio, Optical and electronic properties of Si nanoclusters synthesized in inverse micelles, Phys. Rev. B 60 (1999) 2704-2714.
http://dx.doi.org/10.1103/PhysRevB.60.2704

[19] M.V. Wolkin, J. Jorne, P. M. Fauchet, G. Allan, and C. Delerue., Electronic States and Luminescence in

Porous Silicon Quantum Dots: The Role of Oxygen, Phys. Rev. Lett. 82 (1999) 197-200.

http://dx.doi.org/10.1103/PhysRevLett.82.197