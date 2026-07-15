Electronic Properties of Layered $Ba_{0.5}Sr_{0.5}TiO_3$ Heterostructure: Ab initio Hybrid Density Functional Calculations

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2005 Phys. Scr. 2005 276

(http://iopscience.iop.org/1402-4896/2005/T118/072)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.128.216.34
This content was downloaded on 27/04/2015 at 05:22

Please note that terms and conditions apply.

# Electronic Properties of Layered $Ba_{0.5}Sr_{0.5}TiO_{3}$ Heterostructure:
## Ab initio Hybrid Density Functional Calculations

S. Dorfman$^{a,*}$, S. Piskunov$^{b}$, E. A. Kotomin$^{c}$ and D. Fuks$^{d}$

$^{a}$Department of Physics, Technion-Israel Institute of Technology, Haifa, 32000 Israel
$^{b}$Fachbereich Physik, Universität Osnabrück, D-49069 Osnabrück, Germany
$^{c}$Institute of Solid State Physics, University of Latvia, Kengaraga 8, LV-1063 Riga, Latvia; Max Planck Institut für Festkörperforschung, Heisenbergstrasse 1, D-70569 Stuttgart, Germany
$^{d}$Materials Engineering Department, Ben-Gurion University of the Negev, POB 653, Beer-Sheva, Israel

Received October 18, 2003; revised version received July 21, 2004; accepted August 13, 2004

PACS numbers: 71.15.Ap; 71.15.Mb; 71.20.Ps

### Abstract
*Ab initio* calculations of the BST heterostructure with equiatomic constituent of Sr and Ba species has been carried out within *hybrid* functional B3PW involving a hybrid of non-local Fock exchange and Becke's gradient corrected exchange functional combined with the non-local gradient corrected correlation potential by Perdew and Wang. The suggested scheme of calculations reproduces experimental lattice parameters of both pure BaTiO₃ and SrTiO₃. The calculated optical band gap for the pure SrTiO₃ (BaTiO₃) is 3.56 (3.46)eV (expt. 3.25 and 3.20eV, respectively), i.e. agreement is much better than in the standard LDA or HF calculations. In the $Ba_{0.5}Sr_{0.5}TiO_{3}$ solid solution the gap is reduced by 0.2eV. The BST upper valence band consists of O 2p atomic orbitals (AO) with a small admixture of Ti 3d, whereas the conduction band bottom consists mostly of Ti 3d orbitals with a small contribution of O orbitals. The Sr (Ba) atomic orbitals make a significant contribution to the higher part of the conduction band. The electron density maps demonstrate the covalency effects in the Ti-O bonding. The electron density near the Sr atoms is stronger localized, as compared with the Ba ions.

### 1. Introduction
It is well recognized nowadays that the dielectric and piezoelectric properties, response on external excitations, etc. in complex perovskite solid solutions with common formula $(A,A',A'')(B,B',B'')O_{3}$ are entirely linked to the structural properties including compositional ordering and formation of complicated heterostructures. $Ba_{c}Sr_{(1-c)}TiO_{3}$ (BST) is considered as the most promising candidate for memory cell capacitors in dynamic random access memory with extremely high scale integration [1].

For BST solid solutions in the Ba-rich region the dielectric anomalies were associated with the fluctuations of the order parameter [2]. The dielectric and ultrasonic study in Sr-rich BST was reported in [3] where it was shown that the small addition of Ba to SrTiO₃ leads to formation of glassy state at very low Ba concentrations and complicates significantly the sequence of phase transitions near $c = 0.15$. Structural evolution and polar order in BST is reported in [4] on the basis of combination of diffraction and diffusion of neutron and high-resolution X-ray experiments as well as dielectric susceptibility and polarization measurements. It is shown that SrTiO₃-type antiferrodistortive phase exists up to a concentration of Ba $c_{cr}=0.094$, the progressive substitution of Sr by Ba leads to a monotonic decrease and to a vanishing of the oxygen octahedral tilting. The critical concentration $c_{cr}$ separates the phase diagram in two regions, one with a sole antiferrodistortive phase transition $(c < c_{cr})$ and one with the succession of three BaTiO₃-type ferroelectric phase transitions $(c > c_{cr})$. Moreover, inside the nonferroelectric antiferrodistortive phase a local polarization is observed, with a magnitude that is comparable to the values of spontaneous polarization in the ferroelectric phases of the rich in Ba compounds. In [5] the results of Raman study of BST films with the thickness $1\ \mu$m and with Ba atomic fraction $c = 0.05,0.1,$ $0.2,0.35$, and 0.5 show the striking similarity with the behavior of relaxor ferroelectrics and are explained by the existence of polar nanoregions in the BST thin films.

To describe and to explain the ties of the structural and dielectric properties in these materials significant efforts were employed. A simple purely ionic model that accounts for electrostatic interaction was presented in [6] to reproduce the compositional long-range order observed in a large class of perovskite alloys. To go beyond the ground state behavior and to make conclusions on the thermodynamic behavior as a function of temperature Metropolis Monte Carlo simulations were further applied with the energy defined as excess electrostatic energy in heterovalent binaries. *This model does not automatically allow homovalent binary alloys to order*. Account for charge transfer may be performed by direct modeling in the framework of electrostatic model as was reported in [7] or may be carried out by *ab initio* calculation. A rather short but comprehensive review of the very recent use of first-principle-derived approaches to investigate piezoelectricity in simple and complex ferroelectric perovskites may be found in [8]. It is interesting to note that most of these investigations were performed for heterovalent solid solutions and the case of homovalent alloys, such as BST, is much less studied. In this sense it is worth to mention Ref. [9] where Molecular Dynamics calculations have been performed. The interatomic pairwise potential used in these calculations included a Coulomb interaction, Born-Mayer-type repulsive interaction, and a van der Waals attractive interaction. Although the giant dielectric constant in BST for a $c = 0.7$ was explained, other described above fine features of the phase transformations in this system were not found. This clearly demonstrates the importance of *ab initio* calculations for homovalent perovskite alloys.

### 2. Computational details and results
To perform *ab initio* calculations we use the CRYSTAL'98 computer code [10–18]. CRYSTAL is a periodic-structure computer program. It is based on the Linear Combination of Atomic Orbitals (LCAO) technique and uses Gaussian functions localized at atoms as the basis set (BS) for expansion of the crystalline orbitals. The main advantage of this code is the ability

---
*Corresponding author.*

to calculate the electronic structure of materials with both Hartree-Fock (HF) and Kohn-Sham (KS) Hamiltonians, or various hybrid approximations using identical BS and computational parameters. However, in order to employ this code, it is necessary to optimize BSs to make them suitable for electronic structure computations of crystals.

In the present simulations we employ effective core pseudopotentials (ECPs). This approximation allows to account for the chemically inert core electrons with effective pseudopotentials and hence, to focus on more significant calculations of valence electron states and to save significant amount of computational time. The Hay-Wadt small-core ECP's have been adopted for Ti, Sr, and Ba atoms [19-21]. The "small-core" ECP's replace only inner core orbitals, but orbitals for outer core electrons as well as for valence electrons are calculated self-consistently. Light oxygen atoms are left with the full electron BS. The BSs have been adopted in the following forms: O - 8-411(1d)G (the first shell is of s type and is a contraction of eight Gaussian type functions, then there are three sp shells and one d shell), Ti - 411(311d)G, Sr and Ba - 311(1d)G, see Ref. [22] for more details.

In LCAO computational schemes for crystals each crystalline orbital is presented as a linear combination of Bloch functions:
$$
\phi_{\mu}(\boldsymbol{r} ; \boldsymbol{k})=\sum_{\boldsymbol{g}} \mathrm{e}^{\mathrm{i} \boldsymbol{k} \boldsymbol{g}} \phi_{\mu}(\boldsymbol{r} ; \boldsymbol{g}). \tag{1}
$$

The atom-centered basis functions $\phi_{\mu}(\boldsymbol{r} ; \boldsymbol{g})$ are expanded into a linear combination of individually normalized atom-centered Gaussian-type functions (GTF) with fixed coefficients $d_j$ and exponents $\alpha_j$:
$$
\phi_{\mu}(\boldsymbol{r} ; \boldsymbol{g})=\sum_{j}^{n_{G}} d_{\mu j} G(\alpha_{j} ; \boldsymbol{r}-\boldsymbol{A}_{j}-\boldsymbol{g}). \tag{2}
$$

Here $\boldsymbol{g}$ is lattice vector and $\boldsymbol{A}_j$ describes the position of an atom in a unit cell.

We performed calculations on the layered BST equiatomic heterostructure (see Fig. 1) using the so-called hybrid functional B3PW involving a hybrid of non-local Fock exchange and Becke's gradient corrected exchange functional [23] combined with the non-local gradient corrected correlation potential by Perdew and Wang [24, 25]. 20% of non-local Fock energy have been utilized in this scheme. The B3PW hybrid exchange-correlation technique was chosen due to its ability to provide the proper description of basic bulk properties and electronic structure of $\mathrm{BaTiO}_3$ and $\mathrm{SrTiO}_3$ perovskite crystals [22].

![](./images/812137599748538369_1.jpg)

Fig. 1. The selected layered geometry of the BST supercell with equiatomic concentrations of Sr and Ba atoms.

To model the discussed above BST structure we extended the standard cubic $\mathrm{ABO}_3$-type primitive unit cell to a supercell with translation vectors obtained from the simple relation [26]:
$$
A_{j}=\sum_{i=1}^{3} l_{i j} a_{i}, \tag{3}
$$
where $a_i$ are the translation vectors of the primitive cell. In our case $l_{ij}$ is the diagonal matrix:
$$
l=\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}. \tag{4}
$$

The constructed supercell consists of eight primitive unit cells and includes $5 \times 8=40$ atoms. Substitution of some Ba atoms

![](./images/812137599748538369_2.jpg)

Fig. 2. Band structure of the BST supercell (1 a.u. = 27.212 eV).

![](./images/812137599748538369_3.jpg)

Fig. 3. Calculated density of states of the supercell with the selected geometry (see Fig. 1).

![](./images/812137599748538369_4.jpg)
![](./images/812137599748538369_5.jpg)

Fig. 4. Difference electron density maps (the total density minus a superposition of the densities for $Ba^{2+}(Sr^{2+})$, $Ti^{4+}$, and $O^{2-}$ ions in the BST supercell) in the cross-section coinciding with the (001) and (110) planes (Fig. 1). Isodensity curves are drawn from $-0.05$ to $+0.05$ e/a.u. $^{3}$ with increments of $0.001$ e/a.u. $^{3}$.

for Sr atoms allows to construct a layered BST heterostructure. The theoretical lattice constant was optimized for the selected geometry. To obtain the equilibrium value of lattice constants we used a computer code that implements Conjugated Gradients optimization technique [27] with a numerical computation of derivatives. During the lattice constant optimizations all atoms were held fixed in their original positions in the supercell.

The reciprocal space integration was performed by sampling the Brillouin zone of the supercell with an $8 \times 8 \times 8$ Pack- Monkhorst net [28], that provides the balanced summation in direct and reciprocal lattices [29]. To achieve high accuracy, large enough tolerances 7, 8, 7, 7, 14, (i.e. the calculation of integrals with an accuracy of $10^{-N}$) were chosen for the Coulomb overlap, Coulomb penetration, exchange overlap, the first exchange pseudo-overlap, and for the second exchange pseudo-overlap respectively [11].

The suggested scheme allows us to reproduce experimental lattice parameters for cubic $BaTiO_{3}$ and $SrTiO_{3}$ phases with accuracy up to $10^{-3} \AA$, i.e. 3.903 (3.905) for $SrTiO_{3}$ and 4.004(3.996) for $BaTiO_{3}$. The experimental values [31] are given in brackets. The lattice parameter calculated for our heterostructure is $3.963 \AA$. Evidently, this lattice constant lies between lattice constants of pure $BaTiO_{3}$ and $SrTiO_{3}$ perovskites.

The calculated band structure and DOS are presented in Figs. 2 and 3, respectively. The band structure is similar to the previous calculated (see for example [30]). The upper valence band is quite flat, with a top at the $\Gamma$ point. The bottom of the conduction band lies also at the $\Gamma$ point with very close energy to the X point. The energy dispersion between $\Gamma$ and X points is very flat. Such flat bands make available exciton self-trapping. The optical band gap for pure $SrTiO_{3}$ calculated with the hybrid DFT/B3PW method is 3.56 eV. This value slightly overestimates the experimental measured data in 3.25 eV [32]. The band gap calculated for the heterostructure under consideration is 3.54 eVthat is only 0.2 eV smaller than the optical gap for pure $SrTiO_{3}$ (the optical band gap was calculated as the distance between upper valence band and lower conduction band). The upper valence band consists of O 2p atomic orbitals with small admixture of Sr atomic orbitals and negligible input of Ba atomic orbitals (see Fig. 3). The conduction band bottom consists essentially of Ti 3d orbitals with a small contribution of O orbitals. The Sr atomic orbitals make a significant contribution in the higher part of the conduction band. All partial atomic contributions of the conduction band are rather narrow.

Fig. 4 shows difference electron density maps (calculated with respect to a superposition of ionic densities). These maps apparently demonstrate the covalency effect in the Ti-O bonding, which is well known for the pure $SrTiO_{3}$ and $BaTiO_{3}$ perovskites. We would like also to pay attention to the fact that the electron density near the Sr ions is stronger localized in comparison with the Ba ions. These ions do not participate in the chemical bonding in the BST.

### 3. Summary
Summing up, the suggested calculation scheme containing a hy- brid of non-local Fock exchange and generally adopted DFT exchange-correlation functional is able to reproduce lattice pa- rameters of pure $BaTiO_{3}$ and $SrTiO_{3}$ in agreement with experi ment. The calculated band gaps are only slightly overestimated (no more than 10%). The obtained agreements in the gap values are much better than in the standard DFT or HF approaches [33, 34]. In the considered BST heterostructure the gap is reduced by 0.2 eV. The BST solid solutions in the selected geometry are characterized by the same type of bonding as the pure perovskite constituents. We have started already calculations on a number of BST het- erostructures with different geometries and relative atomic con- centrations of Ba and Sr, and we hope that the suggested approach is a good basis for the precise microscopic study of physical prop- erties of the technologically important perovskites.

### References
1. Abe, K. and Komatsu, S., J. Appl. Phys. **77**, 6461 (1995).
2. Singh, N., Singh, A. P., Prasad, Ch. D. and Pandey, D., J. Phys.: Condens. Matter **8**, 7813 (1996).
3. Lemanov, V. V., Smirnova, E. P., Syrnikov, P. P. and Tarakanov, E. A., Phys. Rev. B **54**, 3151 (1996).
4. Mnoret, C. *et al.*, Phys. Rev. B **65**, 224104 (2002).
5. Tenne, D. A., Soukiassian, A., Zhu, M. H. and Klark, A. M., Phys. Rev. B **67**, 012302 (2003).

© Physica Scripta 2005

6. Bellaiche, L. and Vanderbilt, D., Phys. Rev. Lett. **81**, 1318 (1998).

7. Wu, Z. and Krakauer, H., Phys. Rev. B **63**, 184113 (2001).

8. Belaiche, L., Current Opinion Solid State Mater. Sci. **6**, 19 (2002).

9. Tanaka, H., Tabata, H., Ota, K. and Kawai, T., Phys. Rev. B. **53**, 14112 (1996).

10. Pisani, C., (Ed.), "Quantum-Mechanical *Ab-initio* Calculations of the Properties of Crystalline Materials", Vol. 67 of Lecture Notes in Chemistry, (Springer, 1996).

11. Saunders, V. R. *et al.*, CRYSTAL'98 User's Manual, Universita di Torino, (Torino 1998).

12. http://www.chimifm.unito.it/teorica/crystal/crystal.html.

13. http://www.cse.clrc.ac.uk/cmg/crystal.

14. Towler, M. D., Zupan, A. and Causa, M., Comput. Phys. Commun. **98**, 181 (1996).

15. Dovesi, R., Orlando, R., Roetti, C., Pisani, C. and Saunders, V. R., Phys. Status Solidi (b) **217**, 63 (2000).

16. Doll, K., Saunders, V. R. and Harrison, N. M., Int. J. Quantum Chem. **82**, 1 (2001).

17. Civalleri, B., D'Arco, P., Orlando, R., Saunders, V. R. and Dovesi, R., Chem. Phys. Lett. **348**, 131 (2001).

18. Zicovich-Wilson, C. M., Dovesi, R. and Saunders, V. R., J. Chem. Phys. **115**, 9708 (2001).

19. Hay, P. J. and Wadt, W. R., J. Chem. Phys. **82**, 270 (1984).

20. Hay, P. J. and Wadt, W. R., J. Chem. Phys. **82**, 284 (1984).

21. Hay, P. J. and Wadt, W. R., J. Chem. Phys. **82**, 299 (1984).

22. Piskunov, S., Heifets, E., Eglitis, R. I. and Borstel, G., Comp. Mat. Sci. **29**, 165 (2004).

23. Becke, A. D., J. Chem. Phys. **98**, 5648 (1993).

24. Perdew, J. P. and Wang, Y., Phys. Rev. B **33**, 8800 (1986).

25. Perdew, J. P. and Wang, Y., Phys. Rev. B **45**, 13244 (1992).

26. Evarestov, R. A. and Smirnov, V. P., J. Phys.: Condens. Matter **9**, 3023 (1997).

27. Press, W. H., Teukolsky, S. A., Vetterling, W. T. and Flannery, B. P., "Numerical Recipies in Fortran77", 2nd Edition, (Cambridge Univ. Press, Cambridge, MA, 1997).

28. Monkhorst, H. J. and Pack, J. D., Phys. Rev. B **13**, 5188 (1976).

29. Bredow, T., Evarestov, R. A. and Jug, K., Phys. Stat. Solidi. (b) **222**, 495 (2000).

30. Heifets, E., Eglitis, R. I., Kotomin, E. A., Maier, J. and Borstel, G., Surface Sci. **513**, 211 (2002).

31. Mitsui, T., Nomura, S. and Adachi, M., "Numerical Data and Functional Relationships in Science and Technology", New Series, Group III: Crystal and Solid State Physics, vol. 16, Ferroelectrics and Related Substances, sub-volume a: Oxides, (Springer-Verlag, Berlin-Heidelberg-New York, 1981).

32. van Benthem, K., Elsasser, C. and French, R. H., J. Appl. Phys. **90**, 6156 (2001).

33. Padilla, J. and Vanderbilt, D., Phys. Rev. B **418**, 64 (1998) .

34. Cheng, C., Kunc, K. and Lee, M. H., Phys. Rev. B **62**, 10409 (2000).

© Physica Scripta 2005

Physica Scripta T118