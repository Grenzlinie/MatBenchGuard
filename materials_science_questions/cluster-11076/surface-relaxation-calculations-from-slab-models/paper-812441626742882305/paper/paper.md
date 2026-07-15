![](./images/812441626742882305_1.jpg)

# How to affect stacking fault energy and structure by atom relaxation

J. Cai, C. Lu, P. H. Yap, and Y. Y. Wang

Citation: *Applied Physics Letters* **81**, 3543 (2002); doi: 10.1063/1.1519106
View online: http://dx.doi.org/10.1063/1.1519106
View Table of Contents: http://scitation.aip.org/content/aip/journal/apl/81/19?ver=pdfcov
Published by the AIP Publishing

---

## Articles you may be interested in

[Atomic structure of prismatic stacking faults in nonpolar a-plane GaN epitaxial layers](https://doi.org/10.1063/1.4750238)
Appl. Phys. Lett. **101**, 112102 (2012); 10.1063/1.4750238

[Mismatch relaxation by stacking fault formation of AlN islands in AlGaN/GaN structures on m-plane GaN substrates](https://doi.org/10.1063/1.3622642)
Appl. Phys. Lett. **99**, 061901 (2011); 10.1063/1.3622642

[Configurational correlations in the coverage dependent adsorption energies of oxygen atoms on late transition metal fcc(111) surfaces](https://doi.org/10.1063/1.3561287)
J. Chem. Phys. **134**, 104709 (2011); 10.1063/1.3561287

[Interaction of dopant atoms with stacking faults in silicon crystals](https://doi.org/10.1063/1.3490753)
J. Appl. Phys. **108**, 073514 (2010); 10.1063/1.3490753

[Boron retarded self-interstitial diffusion in Czochralski growth of silicon crystals and its role in oxidation-induced stacking-fault ringdynamics](https://doi.org/10.1063/1.124749)
Appl. Phys. Lett. **75**, 1544 (1999); 10.1063/1.124749

---

![](./images/812441626742882305_2.jpg)

# How to affect stacking fault energy and structure by atom relaxation

J. Cai, $^{a)}$ C. Lu, P. H. Yap, and Y. Y. Wang
Institute of High Performance Computing, The Capricorn, Science Park II, Singapore 117528

(Received 21 May 2002; accepted 13 September 2002)

By a simulated annealing method with a parameterized tight-binding potential, the properties of structure and energy of a generalized stacking fault are investigated. It is shown that for metal Pd, the second-layer spacing from the stacking fault plane expands initially and then contracts with the variation of the stacking fault variable from 0 to 1. The effect of atom relaxation on stacking fault energy is shown to be small. For another metal Pt, the second-layer spacing contracts and the effect of atom relaxation on the stacking fault energy is found to be obvious. In addition, the calculated stacking fault energy is in agreement with experimental results for the two metals. © 2002 American Institute of Physics. [DOI: 10.1063/1.1519106]

As is well known, the generalized stacking fault (GSF) has a strong effect on the mechanical properties of materials. Although it is possible to use the GSF to characterize the various kinds of mechanical properties of materials, little is known about its structural behaviors when atom relaxation is considered. On the other hand, for a long time, the effect of atom relaxation on the stacking fault energy (SFE) is considered negligible without justice.

In recent works, Zimmerman et al. $^{1}$ used embedded-atom potentials to calculate the GSF energies of Al, Ni, and Cu, and found that, in most cases, the SFE and unstable SFE were underestimated. The unstable SFE refers to the lowest-energy barrier encountered when one half of a crystal slips along the other one. $^{1}$ In their work, there is no discussions about the relaxed GSF structures, although the effect of atom relaxation on the GSF energies is considered. At the same time, Mehl et al. used a tight-binding (TB) potential to study the SFE and unstable SFE of face-centered-cubic (fcc) metals Al, Cu, Rh, Pd, Ag, Ir, Au, and Pb. Good agreement between their results and $ab$ initio calculations was reported. $^{2}$ However, in Mehl et al.'s study, the atom relaxation was not considered, except for the case of unstable SFE of Au and Ir. In fact, a detailed picture about the GSF structure considering atom-scale relaxation is lacking. In the present work, the GSF structures of metals Pt and Pd are studied by a simulated annealing method $^{3}$ combined with a TB potential. $^{4}$ The effect of atom relaxation on the GSF is thus revealed.

The TB potential is developed from density-functional theory $^{5}$ and is constructed based on the two-center Slater–Koster formulation $^{6}$ with a nonorthogonal basis. The potential parameters are determined by requiring that the TB potential reproduce first-principle total energies and electronic band structures of fcc and body-centered-cubic (bcc) as a function of volume. $^{4}$ This method has provided reliable representation of structural behaviors, elastic constants, phonon frequencies, vacancy formation energies, and surface energies for fcc metals. $^{4}$ Presently, the method is used to study the GSF of Pd and Pt. The potential parameters are obtained from Ref. 7. The program used is the static version 111 from Mehl. In order to take account of atom relaxation, a simulated annealing code is added.

As performed by Mehl et al., $^{2}$ we model the $\langle 112\rangle$ slip on a $(11-1)$ slip plane in Pd and Pt metals by constructing a supercell comprising twelve close-packed $(11-1)$ planes of atoms. One atom in each plane is part of the supercell. The primitive vectors of the supercell take the form of
$$
\begin{aligned}
& a_{1}=\frac{1}{2} a_{0} \vec{y}+\frac{1}{2} a_{0} \vec{z}, \\
& a_{2}=\frac{1}{2} a_{0} \vec{x}+\frac{1}{2} a_{0} \vec{z}, \\
& a_{3}=\left(4+\frac{q}{6}\right) a_{0} \vec{x}+\left(4+\frac{q}{6}\right) a_{0} \vec{y}-\left(4-\frac{q}{3}\right) a_{0} \vec{z},
\end{aligned}
\tag{1}
$$
where $a_0$ is the lattice constant, $q$ is the stacking fault variable, and represents a displacement of atoms in the boundary plane along the stacking fault vector of the $\langle 112\rangle$ direction. When $q=0$, the periodic crystal is a perfect fcc system of $ABC|ABC$, where $|$ denotes a "boundary plane." When $q$ $=1$, the atoms at the interface are hexagonal-close-packed (hcp) ordered, i.e., the stacking at the interface is $ABC|BCA$ rather than $ABC|ABC$. In this calculation, the relaxation of atoms along the direction of $\langle 11-1\rangle$ is considered. The atoms in the three nearest atomic layers to each side of the boundary plane are allowed to relax. There are six atom layers in total. The first interlayer spacing is the spacing between two atomic layers on either side and nearest to the boundary plane, the second interlayer spacing is the spacing between the atom layers first and second nearest to the boundary plane, and the third interlayer spacing is the spacing between the atom layers second and third nearest to the boundary plane.

The simulated annealing procedure is run for 1000 steps at an initial temperature of 50 K, and then the program is run again for 1000 steps at temperature of 0 K. In calculations, a large number of $k$ points (4808) in the irreducible part of the Brillouin zone of Eq. (1) is used to ensure convergence. The calculated total energy is determined by summing the eigenvalues with a weight of a Fermi distribution over the Bril-

$^{a)}$Electronic mail: caij@ihpc.nus.edu.sg

![](./images/812441626742882305_3.jpg)

FIG. 1. Generalized SFE as a function of parameter $q$ in Eq. (1): (a) for metal Pd and (b) for metal Pt. The lines are guides for the eyes.

louin zone. In the Fermi distribution, a temperature of 5 mRy is set and then extrapolated to zero. The results are shown in Figures 1 and 2.

The unrelaxed and relaxed GSF energy per unit area versus displacement variable $q$ for Pd and Pt are plotted in Fig. 1. The curves, for both the relaxed and the unrelaxed cases, have skewed sinusoidal shapes, which is in agreement with the predictions of the models by Frenkel, $^{8}$ Mackenzie, $^{9}$ and Rice. $^{10}$ It is also in agreement with the first-principle calculations. $^{1}$ In addition, in the present calculations the unstable SFE is found to be located at $q \approx 1/2$ in the GSF curve for metal Pd. For metal Pt, the unstable SFE is located at $q=0.6$. It is in agreement with previous first-principle calculations for Cu, Al, and Ni, where the unstable SFEs were predicted to locate at the position of $q=0.5$, 0.6, 0.6(0.55), respectively. $^{1}$

The relaxed SFE and relaxed unstable SFE for metals Pd and Pt, together with the results from first-principle calculations and experiments are tabulated in Table I. From Table I,

<table>
<caption>TABLE I. SFE and unstable SFE for metals Pd and Pt.</caption>
<tr>
<th>Energy (mJ/m²)</th>
<th>Pd</th>
<th>Pt</th>
</tr>
<tr>
<td>SFE (this work)</td>
<td>225</td>
<td>339</td>
</tr>
<tr>
<td>(experiment)ª</td>
<td>180</td>
<td>322</td>
</tr>
<tr>
<td>(ab initio)ª</td>
<td>161 225</td>
<td>393</td>
</tr>
<tr>
<td>Unstable SFE (this work)</td>
<td>383</td>
<td>432</td>
</tr>
<tr>
<td colspan="3">ªSee Ref. 11.</td>
</tr>
</table>

it is seen that for SFE of Pd and Pt, good agreement can be found among our numerical results, the experimental data and first-principles calculations. For unstable SFE, the present relaxed values are 383 and 432 mJ/m², and the unrelaxed values are 452 and 490 mJ/m² for metals Pd and Pt, respectively. It is somewhat different from the results given by Mehl et al.² In the calculations by Mehl et al., the supercell consists of five atom layers and its size is close to the cutoff distance of the TB potential. In the present calculations, the cell consists of 12 atom layers and its size is far larger than the cutoff distance. Thus, the present results are more reliable than those of Mehl et al. From the present numerical results, it is seen that, with atom relaxation, the SFE is reduced by 5% and 12% while the unstable SFE is reduced by 15% and 12% for Pd and Pt, respectively. In previous calculations for Ag and Au, it was also found that the SFEs were reduced by 1% and 6%, and the unstable SFEs were reduced over 10% and 20%, respectively, due to atom relaxation.¹² Thus, the effect of atom relaxation on SFE is far smaller than that on unstable SFE for metals Pd, Au, and Ag, whereas the effect is large on both SFE and unstable SFE for metal Pt. This is a very interesting result. In early calculations for SFEs, atom relaxation was often neglected because the effect of atom relaxation was considered negligible. From present numerical calculations, it is seen that for Pd, the effect on SFE is found to be small, while for Pt this effect is very obvious on both SFE and unstable SFE.

![](./images/812441626742882305_4.jpg)

FIG. 2. The changes of interlayer spacings as a function of parameter $q$ in Eq. (1): (a) for metal Pd and (b) for metal Pt. Negative values express contraction in the interlayer spacings.

Thus, in order to obtain an accurate SFE and unstable SFE, it is necessary to include an atom-scale relaxation, especially for an alloy system where the radii difference between two constituting elements is large.

Figures 2(a) and 2(b) show the respective change of atom layer spacings in metals Pd and Pt due to atom relaxation. It can be seen that for Pd the first interlayer spacing has the largest change and contracts within the whole range of $q$ considered, while the third interlayer spacing expands. The second interlayer expands initially and then contracts. The largest relaxation occurs at the place of unstable SFE ($q \approx 1/2$). In previous calculations by the authors for metals Au and Ag, similar conclusions have been drawn. $^{12}$ However, it is a different situation for metal Pt. From Fig. 2(b), it is seen that in Pt the first- and second-interlayer spacings change similarly to those in Pd, while, the second interlayer contracts in the whole range of $q$ considered. Unlike in metal Pd, large relaxation also occurs at the place of SFE in Pt for the three spacings. This corresponds to a large relaxed energy in the position of stacking fault for Pt. In addition, it is also found that for metals Pd and Pt at the site of stacking fault ($q=1$), the interface structure is hcp-like. The calculated $c/a$ values are 1.632 and 1.620, respectively, which are smaller than the ideal value of 1.633. These results are helpful for further testing of the accuracy of the potential model.

In summary, we use the TB potential of Mehl *et al.* to study the GSF. The calculated SFEs for metals Pd and Pt are in agreement with experimental values and first-principle calculations. The predictions for skewed sinusoidal shape of the GSF energy versus displacement variable $q$ agree with the theoretical results by Frenckle, Mackle, and Rice. The site of unstable SFE is found to be close to the ideal value of $q=1/2$ for metal Pd. For metal Pt, this site is at the displacement of $q=0.6$. More importantly, two different patterns are detected for atom relaxation in the two metals. In Pd, the first interlayer spacing contracts for all the $q$ considered, while the third interlayer spacing expands. The second-interlayer spacing expands first and then contracts with the variation of $q$ from 0 to 1. The effect of atom relaxation on SFE is small. In Pt, although the first- and third-interlayer spacings change with $q$ in the similar pattern as those for Pd, the second interlayer contracts. The atom relaxation yields a large variation of the SFE and structure in Pt. Thus, in order to obtain an accurate SFE and unstable SFE, it is necessary to include atom-scale relaxation, especially for an alloy system, where the radii difference between two constituting elements is large.

The authors thank Professor Michael J. Mehl at the Naval Research Laboratory, Washington, D. C., for his providing the TB program of static version 111. One of the authors, C.J., thanks Y. M. Low and Dr. F. Wang for proofreading the manuscript.

$^{1}$J. A. Zimmerman, H. Gao, and F. F. Abraham, Modell. Simul. Mater. Sci. Eng. **8**, 103 (2000).
$^{2}$M. J. Mehl, D. A. Papaconstantopoulos, N. Kioussis, and M. Herbranson, Phys. Rev. B **61**, 4894 (2000).
$^{3}$W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, *Numerical Recipes in Fortran 77: The Art of Scientific Computing*, Fortran Numerical Recipes Vol. 1 (Cambridge University Press, Cambridge, 1997), p. 443.
$^{4}$M. J. Mehl and D. A. Papaconstantopoulos, Phys. Rev. B **54**, 4519 (1996).
$^{5}$P. Hohenberg and W. Kohn, Phys. Rev. **136**, B864 (1964); W. Kohn and L. J. Sham, Phys. Rev. **140**, A1133 (1965).
$^{6}$J. C. Slater and G. F. Koster, Phys. Rev. **94**, 1498 (1954).
$^{7}$The potential parameters were obtained from the website http://cst-www.nrl.navy.mil/bind/
$^{8}$J. Frenkel, Z. Phys. **37**, 572 (1926).
$^{9}$J. K. Mackenzie, Ph.D. thesis, Bristol University, 1949.
$^{10}$J. R. Rice, J. Mech. Phys. Solids **40**, 239 (1992).
$^{11}$N. M. Rosengaard and H. L. Skiver, Phys. Rev. B **47**, 12865 (1993).
$^{12}$J. Cai and J.-S. Wang, Eur. Phys. J. B **28**, 45 (2002); Modell. Simul. Mater. Sci. Eng. **10**, 469 (2002).