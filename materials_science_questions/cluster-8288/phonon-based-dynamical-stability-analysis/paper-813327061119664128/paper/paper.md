PHYSICAL REVIEW B 85, 094104 (2012)

# Transmutation in $^{90}$SrF$_2$: A density functional theory study of phase stability in ZrF$_2$

M. Sassi, $^{1}$ B. P. Uberuaga, $^{2}$ C. R. Stanek, $^{2}$ and N. A. Marks $^{1,*}$

$^{1}$Nanochemistry Research Institute, Curtin University, P.O. Box U1987, Perth, WA 6845, Australia
$^{2}$Material Science and Technology Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

(Received 24 October 2011; revised manuscript received 23 February 2012; published 13 March 2012)

The stability of multiple possible phases of ZrF$_2$ is computed using density-functional theory. Motivated by radioactive samples of fluorite $^{90}$SrF$_2$ stored at the Hanford site, we consider $\beta^-$ radioactive decay as the route by which the $^{90}$ZrF$_2$ is generated. To find suitable structures for the ZrF$_2$ compound two methodologies are used. The first follows imaginary phonon modes from the fluorite ZrF$_2$ while the second employs random structure searching. Six possible ZrF$_2$ phases are identified; however, none of the structures resemble the lone experimentally reported orthorhombic structure for ZrF$_2$. Although we predict these phases to be less stable ($\approx$0.3 eV/f.u.) than a phase-decomposed mixture of $\beta$-ZrF$_4$ and Zr metal, they still may be relevant due to the kinetics of formation via radioactive decay and raise questions as to the nature of the ZrF$_2$ structure and the state of the samples at Hanford.

DOI: 10.1103/PhysRevB.85.094104
PACS number(s): 61.66.Fn, 28.41.Kw, 71.15.Mb, 71.20.$-$b

## I. INTRODUCTION

In the 1970s and 1980s large quantities of $^{137}$Cs ($t_{1/2} = 30$ yr) and $^{90}$Sr ($t_{1/2} = 29$ yr) were extracted from spent nuclear fuel at Hanford in Washington state, and synthesized into capsules of CsCl and SrF$_2$. Even though many of the capsules have aged for more than one half-life, they still account for around one-third of the radioactivity at the Hanford site$^{1}$ and are the most significant source of radiation in the United States outside of a reactor. Stored underwater due to the radiation field, monitoring primarily consists of engineering-type “clunk-tests” (see Ref. 1) which assess swelling associated with radiation damage, gas evolution, and/or phase decomposition.

Aside from health-and-safety considerations, the Hanford capsules are scientifically interesting from a solid-state chemistry viewpoint, since the stable daughter isotopes differ markedly in oxidation state and size to the parent.$^{2,3}$ In the case of $^{137}$Cs$\rightarrow$$^{137}$Ba, the formal oxidation state changes from $+1$ to $+2$ and the ionic radius decreases by 20%, while for $^{90}$Sr$\rightarrow$$^{90}$Y$\rightarrow$$^{90}$Zr the changes are even greater, with the oxidation state changing from $+2$ to $+4$ and the ionic radius decreasing by 29%. These large changes in local chemistry have the potential to compromise a nuclear waste form over time by inducing large volume changes and disrupting the crystalline lattice. This so-called “transmutation problem” has been known for many years,$^{2,3}$ but studies have been rare as experiments are highly challenging and a solution to the problem is not obvious. Experiments on Cs$\rightarrow$Ba transmutation$^{2,4-7}$ suggest that the daughter species are retained within the crystalline matrix, but the critical question of how the host matrix accommodates the daughter species has received relatively little attention.

Recently we have shown by computational means that the $^{137}$CsCl structure can transform via radioactive decay to a novel $^{137}$BaCl phase possessing the rocksalt structure.$^{8,9}$ This unique process, which we term radioparagenesis, occurs when $\beta$ decay of a major lattice constituent leads to a new daughter phase. Experimental confirmation of the process is a tantalizing prospect, but as yet no analytic measurements have been performed on the CsCl capsules at Hanford. Further calculations$^{10}$ on other systems such as $^{90}$SrO$\rightarrow$$^{90}$ZrO and $^{177}$Lu$_2$O$_3$$\rightarrow$$^{177}$Hf$_2$O$_3$ have demonstrated the utility of the radioparagenesis concept as a potential pathway to create novel materials not accessible to conventional synthesis. A further corollary of the radioparagenesis principle is the concept of “backwards design” in which a nuclear waste form is tailored to a specific isotope in such a way that chemical evolution over time increases the stability of the crystalline host.$^{11}$

This study employs density-functional theory (DFT) calculations on the $^{90}$ZrF$_2$ system, arising as a daughter phase from the decay of the parent $^{90}$SrF$_2$ phase which adopts the fluorite structure. We do not consider the intermediate yttrium species as the half-life for decay from $^{90}$Y to $^{90}$Zr is very short (64 h), and hence Y is present only as a transient trace element relative to the ever-increasing quantity of $^{90}$Zr. To the best of our knowledge this system has never been studied by computational methods, either in a radioparagenesis or conventional synthesis context. The only experimental information on the ZrF$_2$ compound is a brief article dating from 1964 by McTaggart and Turnbull$^{12}$ which reports the synthesis of this material through the reduction of ZrF$_4$ with atomic hydrogen. The resultant ZrF$_2$ compound is reported as black in color and stable up to $800^\circ$C against the disproportionation reaction into ZrF$_4$ and metallic Zr. Only limited crystallographic analysis was performed, with x-ray-diffraction experiments showing an orthorhombic structure. In this work, we assess the dynamical stability of potential ZrF$_2$ daughter phases by exploring all the imaginary vibrational modes appearing in the phonon spectra of fluorite ZrF$_2$. We also use the USPEX code (universal structure predictor: evolutionary xtallography),$^{13,14}$ based on an evolutionary algorithm, to perform random structure searches for additional low-energy structures with the ZrF$_2$ stoichiometry. To quantify the effects of $^{90}$Sr$\rightarrow$$^{90}$Zr transmutation we analyze the Bader charges, structural modifications, and density of states (DOS). We also calculate the formation enthalpy of the ZrF$_2$ structures as well as the reaction enthalpy of ZrF$_2$ with respect to a phase-decomposed mixture of ZrF$_4$ and Zr metal. Our results differ considerably from those of McTaggart and Turnbull, motivating further computational and experimental investigation.

1098-0121/2012/85(9)/094104(11)
094104-1
©2012 American Physical Society

## II. COMPUTATIONAL DETAILS

Our calculations employ DFT using the VASP package. $^{15,16}$ The exchange and correlation part of the density functional was treated within the generalized gradient approximation of Perdew and Wang. $^{17}$ The cutoff energies of the projector augmented wave $^{18}$ potentials for $ZrF_{2}$ compounds were all fixed to 520 eV, which guarantees that absolute energies were converged to a few meV and gives us more accurate results with respect to the lattice constants. Lattice constants, cell shapes, and internal atomic positions in the unit cells were relaxed together, at least twice, using the tetrahedron method with Blöchl corrections. In all cases, the total energy was converged to $10^{-6}$ eV/cell and the force components were relaxed to at least $10^{-5}$ eV/Å. During the structural relaxation of each phase a suitable $k$-point mesh was used to sample the Brillouin zone of the unit cell; these were based on the Monkhorst-Pack scheme, $^{19}$ and the specific values are shown in Table I. The cohesive energies of all structures were calculated as described in Ref. 20: the atomic reference energy and spin-polarization energy, obtained from the calculation of a spin-polarized atom, were taken into account.

Phonon-dispersion curves and structural instabilities of the crystalline structures were computed using a direct approach to the lattice dynamics, $^{21}$ as implemented in the Phonopy code. $^{22}$ The direct method involves the construction of $N+1$ supercells: $N$ perturbed supercells and one unperturbed supercell, where $N$ is the number of crystallographically independent displacements of the atoms in the supercell. In each of the perturbed supercells, a single atom was displaced by $\pm 0.01$ Å in a Cartesian direction. The supercell size was chosen such that interactions between the displaced atom and its periodic image were negligible. The supercell size for each structure is shown in Table I. During phonon calculations, the $k$-point mesh was set to $4 \times 4 \times 4$ for all the structures. Born effective charges were not included in our calculations, as it has been demonstrated that the splitting of the longitudinal and transverse optical modes (LO and TO, respectively) at the $\Gamma$ point has essentially no effect on thermodynamics. $^{20}$

Bader charges $^{23}$ were computed to assess the spatial distribution of the electron density using the methodology developed by Henkelman et al. $^{24}$ In this method the Bader partitioning is performed using the sum of the valence and core charge, with the latter being computed via a special flag in VASP. Once the Bader regions are determined, integration is performed using the valence charge (CHGCAR within VASP). All of our Bader charges are expressed relative to neutral atoms, implying positive charges for cations and negative charges for anions.

In addition to the phonon calculations, we also searched for low-energy $ZrF_{2}$ structures using the USPEX code $^{13,14}$ in conjunction with VASP structural relaxations. The $k$-point grid is automatically set by the USPEX program and changes in accordance with the cell parameters, enhancing the comparability of the energies. The optimization scheme was performed in four stages, as described in the USPEX manual. In an evolutionary algorithm, as implemented in the USPEX code, the first generation of structures is produced randomly, with the worst ones being immediately rejected. All of the remaining structures participate in creating the next generation through heredity, atomic permutation, and mutation. In our study, we performed three searches with $ZrF_{2}$ stoichiometry, employing unit cells containing 6, 9, and 12 atoms. The number of structures created in each generation was set to 20. From the second generation onward, each subsequent generation was produced using the 12 lowest-energy structures of the previous generation as parents, with 60% of the new structures created through heredity, 20% created by permutation, and 20% created by lattice mutation. In addition, the four lowest-energy structures of the previous generation survive into the next generation. Convergence was reached when the same lowest-energy structure remained the lowest-energy structure for eight consecutive generations.

<table>
<caption>Table I. Size of the $k$-point mesh used for the optimization of each structure and the supercell size used to compute the phonon calculations.</caption>
<thead>
<tr>
<th>System</th>
<th>$k$-point mesh for relaxation</th>
<th>Supercell size for phonons</th>
</tr>
</thead>
<tbody>
<tr>
<td>$f$-SrF₂</td>
<td>$8 \times 8 \times 8$</td>
<td>$2 \times 2 \times 2$</td>
</tr>
<tr>
<td>$f$-ZrF₂</td>
<td>$8 \times 8 \times 8$</td>
<td>$2 \times 2 \times 2$</td>
</tr>
<tr>
<td>$t139$-ZrF₂</td>
<td>$8 \times 8 \times 6$</td>
<td>$2 \times 2 \times 1$</td>
</tr>
<tr>
<td>$o70$-ZrF₂</td>
<td>$8 \times 4 \times 6$</td>
<td>$2 \times 1 \times 2$</td>
</tr>
<tr>
<td>$m11$-ZrF₂</td>
<td>$10 \times 8 \times 10$</td>
<td>$3 \times 2 \times 3$</td>
</tr>
<tr>
<td>$m14$-ZrF₂</td>
<td>$10 \times 10 \times 8$</td>
<td>$3 \times 2 \times 2$</td>
</tr>
<tr>
<td>$m12$-ZrF₂</td>
<td>$10 \times 6 \times 8$</td>
<td>$4 \times 3 \times 2$</td>
</tr>
<tr>
<td>$\beta$-ZrF₄</td>
<td>$4 \times 4 \times 4$</td>
<td>$2 \times 1 \times 1$</td>
</tr>
</tbody>
</table>

## III. RESULTS

The parent structure in the Hanford capsules is $SrF_{2}$, a highly ionic solid which adopts the fluorite structure. As expected, our computed lattice parameter for $f$-SrF₂, 5.852 Å, is in close agreement with the experimental value of 5.799 Å. $^{25,26}$ We also computed the phonon-dispersion relations of the $f$-SrF₂ structure and found no imaginary frequencies indicative of unstable modes. With the exception of the LO-TO splitting, the phonon spectra is very similar to reported values in the literature. $^{27,28}$

As mentioned earlier, the transmutation of $^{90}$Sr into $^{90}$Zr leads to drastic changes in the local chemical environment and overall stability of the crystal. Although there are many possible effects to study, such as stability as a function of Zr concentration and defect generation through energetic recoil (see Ref. 29 for more details), here we concentrate on the well-defined problem of a parent structure containing 100% $^{90}$Sr decaying to a daughter phase containing only $ZrF_{2}$. Conceptually we consider this change by first substituting all of the Sr atoms in the parent fluorite structure with Zr, although in practice this change is gradual due to the 29-yr half-life of $^{90}$Sr. In the second stage of our investigations we consider structures with $ZrF_{2}$ stoichiometry, providing an additional test of the orthorhombic structure reported by McTaggart and Turnbull. $^{12}$

### A. Exploring soft modes

The starting structure for our analysis of $ZrF_{2}$ is the fluorite phase, which is characterized in Table II. Although the volume of $f$-ZrF₂ decreases by 20% relative to $f$-SrF₂, the cohesive

<table>
<caption>TABLE II. Calculated structural parameters, cohesive energy, and volume ($V$) for the fluorite $f$-SrF₂ and four ZrF₂ phases: $f$-ZrF₂, $m$14-ZrF₂, $o$70-ZrF₂, and $m$12-ZrF₂. For each structure the lattice parameters correspond to the Bravais lattice in which the unit cell of $f$-SrF₂, $f$-ZrF₂, $m$14-ZrF₂, and $m$12-ZrF₂ contains 12 atoms, while the unit cell of $o$70-ZrF₂ contains 48 atoms.</caption>
<tbody><tr><td>High symmetry point</td><td colspan="2">X</td><td>X</td><td>W</td><td>L</td></tr>
<tr><td>Structure</td><td>$f$-SrF₂</td><td>$f$-ZrF₂</td><td>$m$14-ZrF₂</td><td>$o$70-ZrF₂</td><td>$m$12-ZrF₂</td></tr>
<tr><td>space group</td><td>$Fm\overline{3}m$</td><td>$Fm\overline{3}m$</td><td>$P2_1/c$</td><td>$Fddd$</td><td>$C2/m$</td></tr>
<tr><td colspan="6"></td></tr>
<tr><td>$E_{\text{coh}}$ (eV/f.u.)</td><td>−16.232</td><td>−16.144</td><td>−17.500</td><td>−17.226</td><td>−17.521</td></tr>
<tr><td>$a$ (Å)</td><td>5.852</td><td>5.425</td><td>4.283</td><td>5.867</td><td>3.162</td></tr>
<tr><td>$b$ (Å)</td><td>5.852</td><td>5.425</td><td>5.632</td><td>12.596</td><td>7.914</td></tr>
<tr><td>$c$ (Å)</td><td>5.852</td><td>5.425</td><td>7.066</td><td>7.972</td><td>6.532</td></tr>
<tr><td>$\alpha$ (°)</td><td>90.0</td><td>90.0</td><td>90.0</td><td>90.0</td><td>85.12</td></tr>
<tr><td>$\beta$ (°)</td><td>90.0</td><td>90.0</td><td>100.46</td><td>90.0</td><td>90.0</td></tr>
<tr><td>$\gamma$ (°)</td><td>90.0</td><td>90.0</td><td>90.0</td><td>90.0</td><td>90.0</td></tr>
<tr><td>$V$ (Å³/f.u.)</td><td>50.101</td><td>39.915</td><td>41.906</td><td>36.822</td><td>40.711</td></tr>
</tbody></table>

energies of $f$-SrF₂ and $f$-ZrF₂ are very similar. The volume reduction is to be expected since the ionic radius of Zr is considerably smaller than that of Sr. Unsurprisingly, the phonon spectra of $f$-ZrF₂ reveals several imaginary modes as seen in Fig. 1. Hence, this ZrF₂ structure is at a saddle point on the potential-energy surface and is unstable against a variety of lattice distortions. Analysis of the $f$-ZrF₂ phonon spectra reveals that the largest imaginary frequency, $4.55i$ THz, obtained at the $X$ point of the Brillouin zone, is two times degenerate. At the $W$ point, three imaginary modes are present: the lowest mode (which we denote band 1) has an imaginary frequency of $1.70i$ THz and is twice degenerate, while the upper imaginary mode (denoted band 3) has an imaginary frequency of $1.70i$ THz. At the $L$ point of the Brillouin zone, one doubly degenerate imaginary mode appears with an imaginary frequency of $2.21i$ THz.

We searched for dynamically stable ZrF₂ structures by exploring all four of the imaginary vibrational modes appearing in the phonon spectra $f$-ZrF₂ in Fig. 1. Our approach is essentially the same as that used by Herbst and Hector, Jr., in studies of relaxation via soft modes in hydrides.³⁰

![](./images/813327061119664128_1.jpg)

FIG. 1. (Color online) Phonon-dispersion relation of $f$-ZrF₂ along high-symmetry directions in the Brillouin zone. The presence of many imaginary modes shows that the structure is dynamically unstable.

Similarly, we lowered the crystal symmetry and displaced the coordinates according to the eigenvector of each imaginary frequency. Figures 2 and 3 show all of the structures, and their corresponding phonon spectra, that were obtained by following the imaginary vibrational modes at the $X$, $W$ and $L$ point of the $f$-ZrF₂ phonon spectra.

The creation and relaxation of a distorted structure according to the eigenvector of the imaginary frequency at the $X$ point ($f = 4.55i$ THz) yield to a monoclinic structure with the space group 11, denoted $m$11-ZrF₂. In Fig. 2, the polyhedral representation of this structure shows that each Zr atom is coordinated to eight F atoms and the cohesive energy is 0.725 eV/f.u. lower than that of $f$-ZrF₂. However, the $m$11-ZrF₂ phase remains dynamically unstable. Indeed, its phonon spectra, shown in Fig. 3, reveal five imaginary vibrational modes. In this phonon spectra we see that the branches between $\Gamma$ and B are very similar to those between $\Gamma$ and Y. This resemblance is due to symmetry as seen in the coordinates and the lattice parameters of the $m$11-ZrF₂ structure ($a = 4.014$ Å, $b = 4.847$ Å, $c = 4.014$ Å and $\alpha = 90.0^\circ$, $\beta = 102.87^\circ$, $\gamma = 90.0^\circ$). Indeed, the $a$ and $c$ vectors have the same length and the relative position of each atom along these two directions is similar. As shown in the polyhedral representation in Fig. 2, the polyhedron around each Zr atom is a flattened cube. Thus, the imaginary modes at the B and Y points are identical, and hence the number of inequivalent imaginary modes in the phonon spectra of $m$11-ZrF₂ is reduced to three: one at the $\Gamma$ point and two at the Y point. Creating a distorted structure according to the eigenvectors of the upper and lower imaginary mode at the Y point yields, after relaxation, the same structure which is monoclinic, having the space group 14, denoted $m$14-ZrF₂. We note that investigating the imaginary vibrational mode at the $\Gamma$ point is not appropriate in this case since there is no imaginary branch which spans all the high-symmetry points of the $m$11-ZrF₂ phonon spectra. The $m$14-ZrF₂ structure is dynamically stable since no imaginary frequencies appear in its phonon spectra shown in Fig. 3. In Fig. 2, the polyhedral representation of $m$14-ZrF₂ shows that each Zr atom is coordinated to six F atoms. The lattice parameters of a 12-atom unit cell, describing the Bravais lattice of this structure, are shown in Table II. The primitive cell of $m$14-ZrF₂ contains 12 atoms and corresponds to the Bravais

![](./images/813327061119664128_2.jpg)

FIG. 2. (Color online) Polyhedral representation of the structures obtained by following all the imaginary modes of the $f$-ZrF$_2$ phonon spectra at the $X$, $W$, and $L$ point. The cations and anions are symbolized by dark and yellow spheres, respectively.

lattice. In this structure, the volume occupied by each formula unit is $41.91$ $\AA^3$, which is $5\%$ bigger than that of $f$-ZrF$_2$. The cohesive energy of $m14$-ZrF$_2$ is lowered by $1.36$ eV/f.u. relative to that of $f$-ZrF$_2$.

The next imaginary vibrational mode that we investigate is that located at the $L$ point of the phonon spectra of $f$-ZrF$_2$ (Fig. 1). The creation and relaxation of a distorted structure according to the eigenvector of the imaginary frequency $f=2.21i$ THz directly yield to a monoclinic structure with the space group 12, denoted $m12$-ZrF$_2$. This structure is dynamically stable since no imaginary frequencies appear in its phonon spectra shown in Fig. 3. In the polyhedral representation of Fig. 2, we can see that each Zr atom is coordinated to six F atoms. We also remark that the structure of $m12$-ZrF$_2$ consists of a series of planes formed by adjacent rows of ZrF$_2$ linked together by F atoms, so that between two planes the Zr atoms are facing each other. The lattice parameters of a 12-atom unit cell, describing the Bravais lattice of the $m12$-ZrF$_2$ phase, are shown in Table II. It should be noted that the primitive cell of this structure contains only six atoms. In the configuration of the $m12$-ZrF$_2$ structure, each formula unit occupies a volume of $40.711$ $\AA^3$/f.u., which is only $2\%$ bigger than that in $f$-ZrF$_2$. Although the cohesive energy of $m12$-ZrF$_2$ is slightly more favorable than that of $m14$-ZrF$_2$ (by $0.021$ eV/f.u.), it is the lowest-energy structure of all the phases found by following the imaginary vibrational modes of the $f$-ZrF$_2$ phonon spectra.

From the investigation of the imaginary vibrational modes at the $W$ point in the phonon spectra of $f$-ZrF$_2$ (Fig. 1), two different structures can be found. The first structure is obtained by following the doubly degenerate imaginary mode of band 1 ($f=1.74i$ THz). Relaxing the distorted $f$-ZrF$_2$ structure along this eigenvector directly yields an orthorhombic structure with the space group 70, denoted $o70$-ZrF$_2$. In this structure each Zr atom is coordinated to eight F atoms, as shown in the polyhedral representation in Fig. 2. The $o70$-ZrF$_2$ phase is dynamically stable since no imaginary frequencies appear in its phonon spectra, shown in Fig. 3, except for a small imaginary excursion at the $\Gamma$ point. The direct method occasionally obtains unexpected softening of a long-wavelength phonon owing to the limitation of the supercell size.$^{31}$ Such problems can be resolved by a sufficiently larger supercell. However, it should be noted that this error is very small ($0.28i$ THz). The lattice parameters of a 48-atom unit cell, corresponding to the Bravais lattice of the $o70$-ZrF$_2$ phase, are shown in Table II. In this case, we should note that the primitive cell of this structure contains 12 atoms. In the configuration of the $o70$-ZrF$_2$ structure, each formula unit occupies a volume of $36.822$ $\AA^3$/f.u., which is almost $8\%$ smaller than that in $f$-ZrF$_2$. Lowering the symmetry of $f$-ZrF$_2$ to obtain the $o70$-ZrF$_2$ structure allows a energetic gain of $1.082$ eV/f.u.

A second structure can be obtained by following the upper imaginary vibrational mode at the $W$ point. Relaxing the

![](./images/813327061119664128_3.jpg)

FIG. 3. (Color online) Phonon spectra of the $m11$-ZrF$_2$, $m14$-ZrF$_2$, $o70$-ZrF$_2$, $t139$-ZrF$_2$, and $m12$-ZrF$_2$ structures. The phonon spectra of $m11$-ZrF$_2$ and $t139$-ZrF$_2$ reveal the presence of imaginary modes, indicating that the structure is dynamically unstable. In the phonon spectra of $m14$-ZrF$_2$, $o70$-ZrF$_2$, and $m12$-ZrF$_2$ no imaginary modes appear, indicating that these structures are dynamically stable.

distorted structure according to the eigenvector of band 3 ($f = 1.70i$ THz) yields a tetragonal phase of ZrF$_2$ with the space group 139. The structure of this phase, denoted $t139$-ZrF$_2$, is shown in Fig. 2 and corresponds to a tetragonal distortion of the $f$-ZrF$_2$ structure. We remark that a similar structure corresponds to the ground state of the ZrH$_2$ compound, which is chemically analogous to ZrF$_2$ since the hydrogen atom in ZrH$_2$ is negatively charged and acts as a halogen. Indeed, the ZrH$_2$ material adopts a face-centered-tetragonal structure (space group 139) in which the c/a ratio is less than unity. $^{32-34}$ By comparison, in our case the cation-anion ratio of the $t139$-ZrF$_2$ structure is 1.838 ($a = 5.659$ Å and $c = 10.402$ Å). Although the cohesive energy in the $t139$-ZrF$_2$ phase is lowered by 0.736 eV/f.u. compared to that of $f$-ZrF$_2$, this structure is highly dynamically unstable. Indeed, its phonon spectra, shown in Fig. 3, reveal 17 inequivalent imaginary vibrational modes.

Upon discovering that the $t139$-ZrF$_2$ phase contained so many inequivalent modes we chose to terminate our hitherto exhaustive search. Exploring all of these modes would be prohibitively expensive with regard to computational time and resources. Indeed, we estimate that to relax the distorted structure obtained from each of the 17 imaginary modes of the $t139$-ZrF$_2$ phonon spectra and subsequently perform phonon calculations for all these structures we would need around 250 000 CPU hours. Furthermore, this estimated computational time is a lower bound since some of the 17 daughter structures may themselves be dynamically unstable and require additional mode following.

Table II lists the properties of the various daughter phases and shows that the two monoclinic structures found are more stable than the orthorhombic structure. This result suggests that the ground state of the ZrF$_2$ compound would have monoclinic symmetry rather than orthorhombic symmetry as reported by McTaggart and Turnbull in 1964. $^{12}$ However, we remark that exploring all the imaginary vibrational modes of a dynamically unstable structure, such as $f$-ZrF$_2$, opens up a large variety of low-symmetry structures having different cohesive energies and which are dynamically stable. Further, a large number of other low-energy and low-symmetry ZrF$_2$ structures which are dynamically stable might be obtained by exploring all the imaginary vibrational modes of the $t139$-ZrF$_2$ phonon spectra shown in Fig. 3. However, as previously noted, performing such calculations would be very expensive in computational time and resources. In the absence of extra experimental data, trying to locate the orthorhombic structure of McTaggart and Turnbull by exploring every single imaginary mode is long and tedious since the number of structures to investigate can increase exponentially. Furthermore, phonon mode following cannot locate any phases for which an energy barrier separates the parent and daughter structure. Thus, in order to extend our search for low-energy ZrF$_2$ structures, we chose to use a random structure searching code based on an evolutionary algorithm as implemented in the USPEX code. $^{13,14}$ The results obtained are presented in the following section. While this is an important aspect of the concept of radioparagenetic daughter phases, it has no bearing on identifying the structure reported by McTaggart and Turnbull.

### B. Random structure searching

In order to test the input parameters chosen in the USPEX code, we first performed a search of the lowest-energy structure for SrF$_2$. The ground state, having a cubic fluorite

structure, was found at the fifth generation (105th structure generated). The lattice parameters (5.85 Å) and cohesive energy $(-16.24$ eV/f.u.) are in excellent agreement with the values in Table II obtained for the relaxed fluorite $SrF_2$ structure from experimental data.

In their study, McTaggart and Turnbull$^{12}$ do not report either atomic positions or the number of atoms in the orthorhombic cell. In that context, the ability to predict low-energy crystal structures, on the basis of only the chemical composition, represents a considerable advantage. Starting from the lattice parameters reported by McTaggart and Turnbull ($a=4.09$ Å, $b=4.91$ Å, and $c=6.56$ Å), we performed three searches of low-energy $ZrF_2$ structures for unit cells containing 6 atoms (two formula units), 9 atoms (three formula units), and 12 atoms (four formula units). In Fig. 4 we show the polyhedral representation of the lowest-energy structure obtained in each of the three cases, as well as a graph summarizing the progress of the six-atom calculation. This graph shows the cohesive energy (in eV/f.u.) of each structure created over all the generations (small red squares). The solid black line with small dark circles highlights the position of the lowest-energy structure in each generation.

For the unit cell containing six atoms, 213 structures were created over ten generations. As is shown in the energy structure graph in Fig. 4(a), the lowest-energy structure, denoted random-6, was found in the third generation. The cohesive energy of random-6 is $-17.635$ eV/f.u. and it was kept as the "best" (i.e., lowest-energy) structure for all of the seven following generations. As shown in the polyhedral representation [Fig. 4(b)], the structure of the random-6 phase contains $ZrF_2$ planes where the Zr atoms between each neighbor plane face each other. We note that the general aspect of the random-6 structure presents some resemblance with $m12$- $ZrF_2$, shown in Fig. 2. Both are a stack of $ZrF_2$ sheets and the local motifs in both cases have some similar features; indeed, in random-6 each Zr atom is also coordinated by six F atoms and the distribution of the fluorine atoms around each zirconium is identical. However, the volume occupied by a formula unit in the random-6 structure is $4.7\%$ larger than that of $m12$-$ZrF_2$.

The search for the lowest-energy structure in a unit cell with nine atoms presented the largest number of structures created for the three cases studied. A total of 313 structures were created over 14 generations and the lowest-energy structure, denoted random-9, first appeared at the seventh generation. In the polyhedral representation of random-9 in Fig. 4(c), we can see that one of the three Zr atoms [denoted Zr1 in Fig. 4(c)] is coordinated to five F atoms while the two other Zr atoms [denoted Zr2 and Zr3 in Fig. 4(c)] are coordinated to six F atoms. As shown in Table III, the cohesive energy of random-9 is $-17.827$ eV/f.u. The volume occupied by a formula unit, $46.598$ Å$^3$/f.u., is the largest of all the structures studied in this work.

In the case of a unit cell containing 12 atoms, 177 structures were created over eight generations. The lowest-energy structure, denoted random-12, appeared in the first generation and was kept as the "best" (i.e., lowest-energy) structure during all subsequent generations. With a cohesive energy of $-17.891$ eV/f.u., random-12 is the lowest-energy phase of all the structures studied in this work. As shown in Fig. 4(d), the polyhedral representation of this structure reveals that the four Zr atoms are facing each other. In the structure of random-12, two Zr atoms [denoted Zr1 in Fig. 4(d)] are coordinated to five F atoms while the two other Zr atoms [denoted Zr2 in Fig. 4(d)] are surrounded by six F atoms. The volume occupied by a formula unit in random-12 is only

![](./images/813327061119664128_4.jpg)

TABLE III. Calculated structural parameters of the 6-atom (random-6), 9-atom (random-9), and 12-atom (random-12) unit cells predicted by the USPEX code. The cohesive energy ($E_{\text{coh}}$) and volume ($V$) are reported for a formula unit.

|  | Random-6 | Random-9 | Random-12 |
| :--- | :---: | :---: | :---: |
| $E_{\text{coh}}$ (eV/f.u.) | $-17.635$ | $-17.827$ | $-17.891$ |
| $a$ (Å) | $3.163$ | $3.474$ | $5.146$ |
| $b$ (Å) | $6.280$ | $5.442$ | $5.720$ |
| $c$ (Å) | $5.652$ | $7.468$ | $6.476$ |
| $\alpha$ (°) | $130.62$ | $81.87$ | $90.0$ |
| $\beta$ (°) | $90.0$ | $90.0$ | $106.50$ |
| $\gamma$ (°) | $90.0$ | $90.0$ | $90.0$ |
| $V$ (Å$^3$/f.u.) | $42.625$ | $46.598$ | $45.703$ |

$2\%$ smaller than that of random-9 and $7\%$ bigger than that of random-6.

As shown in Table III, the lattice parameters of the three USPEX structures reveal that each phase has monoclinic symmetry. This result is in agreement with the lowest-energy structures, $m14$-ZrF$_2$ and $m12$-ZrF$_2$, found by following the imaginary vibrational modes at the $X$ and $L$ point of the $f$-ZrF$_2$ phonon spectra. Accordingly, by either the imaginary mode-following method or structures predicted by an evolutionary algorithm, our results suggest that the lowest-energy structure is monoclinic in symmetry with lattice vectors having length very different from that of the orthorhombic cell reported by McTaggart and Turnbull. None of these monoclinic structures have previously been suggested for ZrF$_2$. As a part of our random structure search, we observed that for a six-atom unit cell the volumes of all the structures created varied between 76 and $133$ Å$^3$. For the 9-atom and 12-atom unit cells, the ranges in volume were $121$–$166$ and $155$–$206$ Å$^3$, respectively. With the volume of the orthorhombic cell reported by McTaggart and Turnbull being $131.73$ Å$^3$, this suggests that their purported orthorhombic cell should not contain more than nine atoms (three formula units).

### C. Structural analysis and electronic properties

To characterize the changes associated with the transmutation of $^{90}$Sr into $^{90}$Zr, we analyzed the structural and electronic properties of the parent SrF$_2$ material and the principal ZrF$_2$ phases. In Table IV, we report the bond lengths and Bader charge for the atoms in the dynamically stable ZrF$_2$ structures found by mode following and the ZrF$_2$ structures found by random structure searches. In this table, we give the shortest cation-cation distance and an average value of the cation-anion bond length (with averages denoted by brackets) calculated between all the anions that coordinate a cation. The fluorine Bader charges, denoted $\overline{\text{q}}_{\text{F}}$, are also an average value deduced from the charges of all the coordinated anions around a cation.

Considering first the distances shown in Table IV, we see that the three largest cation-cation distances are obtained for the two fluorite structures ($f$-SrF$_2$ and $f$-ZrF$_2$) and the monoclinic $m14$-ZrF$_2$. Smaller cation-cation bonds, in the range of $2.957$–$3.329$ Å, are obtained for the four monoclinic structures: $m12$-ZrF$_2$, random-6, random-9, and random-12. We note that compared to the $m12$-ZrF$_2$ structure the Zr$-$Zr distance between two ZrF$_2$ planes in the random-6 structure is only $0.4\%$ shorter. The cation-cation bond in the orthorhombic $o70$-ZrF$_2$ structure is the shortest with a distance of $2.727$ Å. Altogether, the Zr-Zr distances in all the ZrF$_2$ structures vary up to $0.9$ Å. The differences between trends are less drastic for the cation-anion distances. Indeed, most of the cation-anion bonds vary from $2.215$ Å, in the $m14$-ZrF$_2$ structure, to $2.373$ Å in the $o70$-ZrF$_2$ structure. The only exception was one very long cation-anion distance of $2.925$ Å in $m14$-ZrF$_2$ which was not included in the average value, as it is around $30\%$ longer than typical Zr-F distances.

TABLE IV. Shortest cation-cation and average cation-anion bond lengths of the local structural environment for Sr and Zr atoms in the fluorite structures, in the three dynamically stables phases obtained by mode following and in the three random structures obtained by USPEX. The Bader charges for the anions are an average value between all the F atoms surrounding a cation. A positive Bader charge value indicates loss of an electron, while a negative value indicates gain.

| Structure | Pairing | Bond length (Å) | Bader charge ($e$) |
| :--- | :--- | :---: | :---: |
| $f$-SrF$_2$ | Sr$-$Sr | $4.138$ | $\text{q}_{\text{Sr}} = +1.70$ |
|  | Sr$-$F | $2.534$ | $\text{q}_{\text{F}} = -0.85$ |
| $f$-ZrF$_2$ | Zr$-$Zr | $3.838$ | $\text{q}_{\text{Zr}} = +1.78$ |
|  | Zr$-$F | $2.350$ | $\text{q}_{\text{F}} = -0.89$ |
| $m14$-ZrF$_2$ | Zr$-$Zr | $3.561$ | $\text{q}_{\text{Zr}} = +1.56$ |
|  | Zr$-$F | $\langle 2.215 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.78$ |
| $o70$-ZrF$_2$ | Zr$-$Zr | $2.727$ | $\text{q}_{\text{Zr}} = +1.60$ |
|  | Zr$-$F | $\langle 2.373 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.80$ |
| $m12$-ZrF$_2$ | Zr$-$Zr | $3.201$ | $\text{q}_{\text{Zr}} = +1.55$ |
|  | Zr$-$F | $\langle 2.352 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.77$ |
| Random-6 | Zr$-$Zr | $3.189$ | $\text{q}_{\text{Zr}} = +1.54$ |
|  | Zr$-$F | $\langle 2.291 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.77$ |
| Random-9 | Zr1$-$Zr2 | $3.084$ | $\text{q}_{\text{Zr1}} = +1.12$ |
|  | Zr2$-$Zr3 | $3.163$ | $\text{q}_{\text{Zr2}} = +1.67$ |
|  | Zr3$-$Zr1 | $3.189$ | $\text{q}_{\text{Zr3}} = +1.86$ |
|  | Zr$-$F | $\langle 2.244 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.78$ |
| Random-12 | Zr1$-$Zr1 | $2.957$ | $\text{q}_{\text{Zr1}} = +1.55$ |
|  | Zr1$-$Zr2 | $3.329$ | $\text{q}_{\text{Zr2}} = +1.54$ |
|  | Zr$-$F | $\langle 2.276 \rangle$ | $\overline{\text{q}}_{\text{F}} = -0.77$ |

The relationship between the various Bader charges in Table IV provides an intuitive picture of the changing ionicity of the system following transmutation. In the parent $f$-SrF$_2$ structure the charges are close to the formal ionic values of $+2$ and $-1$ for Sr and F, respectively. In the unstable $f$-ZrF$_2$ structure the fluorine is even more negatively charged than in SrF$_2$, while in the other ZrF$_2$ phases the fluorine charge is approximatively $-0.78$ $e$ for all positions, which is slightly less negative than the $-0.85$ $e$ charge for the parent SrF$_2$. This suggests that fluorine atoms in the stable ZrF$_2$ phases are still somewhat ionic, but less strongly so than in SrF$_2$, which can be considered as a formal ionic solid. A similar behavior is obtained for the cation where the positive charge, $1.78$ $e$ in $f$-ZrF$_2$, is even more positive than in $f$-SrF$_2$. In the other ZrF$_2$ structures, the average charge of Zr is about $1.55$ for all the positions, which is less positive than the charge of Sr ($1.69$ $e$) in the parent SrF$_2$. However, we should note that in the random-9 structure the charge of each Zr atom is very different. Indeed, for the atom Zr1, Zr2, and Zr3 [Fig. 4(c)] the charge is $1.12$,

<table>
  <thead>
    <tr>
      <th></th>
      <th>$f$-SrF₂</th>
      <th>$f$-ZrF₂</th>
      <th>$o70$-ZrF₂</th>
      <th>$m12$-ZrF₂</th>
      <th>Random-6</th>
      <th>Random-9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cation-Cation Plane</td>
      <td>![](./images/813327061119664128_5.jpg)</td>
      <td>![](./images/813327061119664128_6.jpg)</td>
      <td>![](./images/813327061119664128_7.jpg)</td>
      <td>![](./images/813327061119664128_8.jpg)</td>
      <td>![](./images/813327061119664128_9.jpg)</td>
      <td>![](./images/813327061119664128_10.jpg)</td>
    </tr>
    <tr>
      <td>Cation-Anion Plane</td>
      <td>![](./images/813327061119664128_11.jpg)</td>
      <td>![](./images/813327061119664128_12.jpg)</td>
      <td>![](./images/813327061119664128_13.jpg)</td>
      <td>![](./images/813327061119664128_14.jpg)</td>
      <td>![](./images/813327061119664128_15.jpg)</td>
      <td>![](./images/813327061119664128_16.jpg)</td>
    </tr>
  </tbody>
</table>

FIG. 5. (Color online) Charge-density difference slices for the $f$-SrF₂, $f$-ZrF₂, $o70$-ZrF₂, $m12$-ZrF₂, random-6, and random-9 structures. Two planes are shown: the plane described by cations and the plane along cation-anion contacts. Isovalues range from $-0.356$ e⁻/Å³ (blue) to $0.160$ e⁻/Å³ (red). Polyhedral representations of each structure are also given, with cations shown in gray and anions in yellow.

1.67, and 1.86 $e$, respectively. Such differences suggest that the three zirconium atoms in random-9 have different oxidation states.

In Fig. 5 we show charge-density difference slices for the $f$-SrF₂, $f$-ZrF₂, $o70$-ZrF₂, $m12$-ZrF₂, random-6, and random-9 structures; cuts are present in the cation-cation and cation-anion planes. Consistent with the trends in bond length seen in Table IV, the charge-density difference slices in the cation-anion plane reveal a slightly increased electron density between Zr and F relative to that seen for Sr and F. This is consistent with the reduction in ionicity inferred from the Bader charge. Except for the $m14$-ZrF₂ structure, all the charge-density difference slices in the cation-cation plane show stronger Zr-Zr interactions compared to $f$-ZrF₂. The strongest Zr-Zr interaction is obtained in the $o70$-ZrF₂ structure, where the cation-cation distance is the shortest. The charge-density difference slices for the $m12$-ZrF₂ and random-6 structures present very similar behavior along the cation-cation and the cation-anion planes. In these structures we see that the interplane interaction between Zr atoms (cation-cation plane) is stronger than that between Zr atoms in the cation-anion plane. The charge-density difference slice in the cation-cation plane for the random-9 structure shows an interaction between the three cations. From these interactions we can see that there are more electrons around the Zr1 atom than around Zr2 and Zr3, and hence the positive charge of Zr1 is reduced by the presence of these electrons in its atomic basin. This is in agreement with the low Bader charge value of Zr1 in Table IV. Except for the $f$-SrF₂, $f$-ZrF₂, and $m14$-ZrF₂ structures, all the charge-density difference slices reveal cation-cation interactions stronger than cation-anion interactions. Similar interactions and trends are observed for the random-12 structure. Altogether, these results suggest that the Zr-F interactions are slightly less ionic than Sr-F but the cation-cation interactions have a more covalent character.

To evaluate the effect of structural modifications on the electronic properties of ZrF₂, we analyzed the density of states (DOS) of the different ZrF₂ phases. The total DOS of $f$-ZrF₂, $o70$-ZrF₂, $m14$-ZrF₂, $m12$-ZrF₂, random-6, random-9, and random-12 phases are presented in Fig. 6. In contrast with the parent $f$-SrF₂ structure, which is a wide-gap insulator, we see that $f$-ZrF₂, random-9, and random-12 are metallic phases. The DOS of the $o70$-ZrF₂, $m14$-ZrF₂, $m12$-ZrF₂, and

![](./images/813327061119664128_17.jpg)

FIG. 6. (Color online) Electron density of states of $f$-ZrF₂, $o70$-ZrF₂, $m14$-ZrF₂, $m12$-ZrF₂, random-6, random-9, and random-12 structures. The position of the Fermi level ($\varepsilon_{f}$) is shown by the blue dashed line at 0 eV.

random-6 phases show semiconductor behavior since they posses small energy gaps. A comparison between the DOS of these four structures reveals that the smallest energy gap, 0.12 eV, is obtained for the $m14$-ZrF$_2$ phase. The largest energy gaps are obtained for the $o70$-ZrF$_2$ and random-6 structures with a similar value of 0.53 eV. Although the $m12$-ZrF$_2$ phase presents some structural similarities with random-6, its energy gap is 0.39 eV, which is slightly lower than that of random-6. However, since the two lowest-energy structures found in this work, random-9 and random-12, exhibit metallic behavior, we suspect that the ZrF$_2$ compound is a metal. Further analysis on the electronic states was performed by projecting the DOS onto the $s$, $p$, and $d$ atomic orbitals of each chemical species. This showed that for all the ZrF$_2$ phases the $d$ orbital of Zr atoms is the major contributor to the states near $\varepsilon_f$ (from $-2$ to 6 eV), while the $p$ orbital of F atoms is the main contributor to the states located between $-10$ and $-5$ eV.

### D. Formation and reaction enthalpies
Finally, we investigate the thermodynamic stability of all the ZrF$_2$ phases of interest by calculating the reaction enthalpy relative to a phase-decomposed mixture of ZrF$_4$ and Zr metal. We also evaluate the formation enthalpies of ZrF$_2$ and ZrF$_4$ compounds by calculating their formation enthalpies from separate constituents. Assuming that Eqs. (1) and (2) are the formation reactions of the ZrF$_2$ and $\beta$-ZrF$_4$ compounds, respectively, we performed structural optimization via energy minimization of metallic Zr in the hexagonal-close-packed structure, denoted hcp-Zr, as well as $\beta$-ZrF$_4$ in the monoclinic structure and molecular F$_2$:
$$\mathrm{hcp-Zr_{(c)}} + \mathrm{F_{2(g)}} \rightarrow \mathrm{ZrF_{2(c)}},\tag{1}$$

$$\mathrm{hcp-Zr_{(c)}} + 2\,\mathrm{F_{2(g)}} \rightarrow \beta\text{-}\mathrm{ZrF_{4(c)}}.\tag{2}$$

The symmetry of the hcp-Zr structure is $P6_3/mmc$ (space-group number 194) and that of the $\beta$-ZrF$_4$ structure is $I2/c$ (space-group number 15). In Table V we present the lattice parameters of the relaxed hcp-Zr and $\beta$-ZrF$_4$ structures. Our calculated lattice parameters for hcp-Zr give a $c/a$ ratio of 1.604 which is in very good agreement with the experimental value of 1.593. We note that both ratios are smaller than the value of 1.633 corresponding to an ideal hexagonal-close-packed structure. The computed lattice parameters for the monoclinic $\beta$-ZrF$_4$ structure are within $2\%$ of the experimental parameters determined by NMR. The calculated bond length of the F$_2$ molecule, $1.424\ \mathring{\mathrm{A}}$, is also very similar to the experimental value of $1.417\ \mathring{\mathrm{A}}$.

Generally, the enthalpy of each constituent in a solid at $T=0$ K is given by the following equation:
$$H = E_{\text{tot}} + E_{\text{ZPE}},\tag{3}$$
where $E_{\text{tot}}$ is the electronic total energy and $E_{\text{ZPE}}$ is the zero-point energy obtained from phonon calculations. Hector *et al.*$^{20}$ used the same approach (and software) in a recent comprehensive study of the alkaline-earth halides and found excellent agreement with the experiment; this similarity gives

<table>
<caption>Table V. Lattice parameters of the hcp-Zr and the monoclinic $\beta$-ZrF$_4$ structures.</caption>
<tbody>
<tr>
<td>Compound</td>
<td></td>
<td>$a$ ($\mathring{\mathrm{A}}$)</td>
<td>$b$ ($\mathring{\mathrm{A}}$)</td>
<td>$c$ ($\mathring{\mathrm{A}}$)</td>
<td>Angle ($^\circ$)</td>
</tr>
<tr>
<td>hcp-Zr</td>
<td>This work</td>
<td>3.225</td>
<td>3.225</td>
<td>5.175</td>
<td>$\alpha=60.0$</td>
</tr>
<tr>
<td></td>
<td>Experiment$^{35}$</td>
<td>3.230</td>
<td>3.230</td>
<td>5.145</td>
<td>$\alpha=60.0$</td>
</tr>
<tr>
<td>$\beta$-ZrF$_4$</td>
<td>This work</td>
<td>9.73</td>
<td>10.04</td>
<td>7.83</td>
<td>$\beta=94.67$</td>
</tr>
<tr>
<td></td>
<td>Experiment$^{36}$</td>
<td>9.57</td>
<td>9.93</td>
<td>7.73</td>
<td>$\beta=94.47$</td>
</tr>
</tbody>
</table>

confidence in the values obtained in the present work. In Table VI we present the total and zero-point energies obtained for all the chemical compounds involved in reactions (1) and (2), as well as the formation and reaction enthalpies, denoted $\Delta H_f^{0\text{K}}$ and $\Delta H_r$, respectively. However, no zero-point energies are available for the random-6, random-9, and random-12 structures since no phonon calculations were performed for them, but we should note that for the other structures $\Delta E_{\text{ZPE}}$ represents only a small amount of $\Delta H_f$ with only 0.05 eV/f.u. The formation enthalpies have been calculated using the following equation:
$$\begin{aligned}
\Delta H_f^{0\text{K}} &= \left(E_{\text{tot}}[\mathrm{ZrF}_n] - E_{\text{tot}}[\mathrm{hcp-Zr}] - \frac{n}{2}\,E_{\text{tot}}[\mathrm{F}_2]\right) \\
&\quad+ \left(E_{\text{ZPE}}[\mathrm{ZrF}_n] - E_{\text{ZPE}}[\mathrm{hcp-Zr}] - \frac{n}{2}\,E_{\text{ZPE}}[\mathrm{F}_2]\right),
\end{aligned}\tag{4}$$
where $n$ is the number of fluorine atoms in the Zr-F compound. For the ZrF$_2$ and $\beta$-ZrF$_4$ compounds we obtain negative formation enthalpy values, showing that the formation of these phases is more favorable than separated constituents.

A comparison between our calculated formation enthalpies at 0 K and those found in the literature at a temperature of 298 K (Table VI) reveals large differences which we suspect relate to error and/or uncertainty in the experiments. In the case of ZrF$_2$, our calculated formation enthalpies are from 0.7 to 1.5 eV/f.u., more positive than the values estimated by McTaggart and Turnbull$^{12}$ and by van der Vis *et al.*$^{38}$ Regarding the $\beta$-ZrF$_4$ structure we should note that the formation enthalpy originates from experiments performed over 50 years ago involving fluorine combustion calorimetric measurements.$^{37}$ This value was in turn used by van der Vis *et al.*$^{38}$ to calculate the formation enthalpy of the ZrF$_2$ compound using the boundary condition $\Delta G\geqslant0$ for the phase-decomposition reaction of ZrF$_2$ into ZrF$_4$ and Zr [see Eq. (5)]. Hence, this condition gives an upper value of $\Delta H_f$, suggesting that the real value of the formation enthalpy for ZrF$_2$ is more negative than $-9.908$ eV/f.u. This result is not consistent with the experimental formation enthalpy of $\Delta H_f=-9.713$ eV/f.u. inferred by McTaggart and Turnbull in 1964 using an empirical relation.$^{12}$ We suspect that further experimental work employing modern techniques would resolve these ambiguities.

Having computed the formation enthalpies, we can, as a corollary, calculate the reaction enthalpy for the phase decomposition of ZrF$_2$ into $\beta$-ZrF$_4$ and metallic Zr, a reaction that may be crucial in the evolution of nuclear waste material; this process is described by the reaction
$$\mathrm{ZrF_{2(c)}} \rightarrow \frac{1}{2}\mathrm{ZrF_{4(c)}} + \frac{1}{2}\mathrm{Zr_{(c)}}.\tag{5}$$

<table>
<caption>TABLE VI. The total and zero-point energies, respectively denoted $E_{\text{tot}}$ and $E_{\text{ZPE}}$, are given in eV/f.u, as well as the formation enthalpies at 0 K ($\Delta H_{f}^{0\,\text{K}}$) and 298 K ($\Delta H_{f}^{298\,\text{K}}$) and the reaction enthalpy ($\Delta H_{r}$). For $\text{ZrF}_{2}$, $\Delta H_{f}^{298\,\text{K}}$ has been estimated using an empirical equation$^{12}$ and the condition $\Delta G{\geqslant}0$ for the phase-decomposition reaction (5).$^{38}$ Data for $\beta\text{-ZrF}_{4}$ was determined from fluorine combustion calorimetric measurements.$^{37}$</caption>
<thead>
  <tr>
    <th>Compound</th>
    <th>$m14\text{-ZrF}_{2}$</th>
    <th>$o70\text{-ZrF}_{2}$</th>
    <th>$m12\text{-ZrF}_{2}$</th>
    <th>Random-6</th>
    <th>Random-9</th>
    <th>Random-12</th>
    <th>$\beta\text{-ZrF}_{4}$</th>
    <th>hcp-Zr</th>
    <th>$\text{F}_{2}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$E_{\text{tot}}$</td>
    <td>$-20.608$</td>
    <td>$-20.334$</td>
    <td>$-20.628$</td>
    <td>$-20.743$</td>
    <td>$-20.935$</td>
    <td>$-20.998$</td>
    <td>$-34.185$</td>
    <td>$-8.433$</td>
    <td>$-3.588$</td>
  </tr>
  <tr>
    <td>$E_{\text{ZPE}}$</td>
    <td>$0.141$</td>
    <td>$0.141$</td>
    <td>$0.140$</td>
    <td>$-$</td>
    <td>$-$</td>
    <td>$-$</td>
    <td>$0.188$</td>
    <td>$0.023$</td>
    <td>$0.064$</td>
  </tr>
  <tr>
    <td>$\Delta H_{f}^{0\,\text{K}}$</td>
    <td>$-8.533$</td>
    <td>$-8.259$</td>
    <td>$-8.544$</td>
    <td>$-8.722$</td>
    <td>$-8.914$</td>
    <td>$-8.977$</td>
    <td>$-18.539$</td>
    <td>$-$</td>
    <td>$-$</td>
  </tr>
  <tr>
    <td>$\Delta H_{f}^{298\,\text{K}}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td>$-9.713^{12}$</td>
    <td></td>
    <td></td>
    <td>$-19.808^{37}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>$-9.908^{38}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\Delta H_{r}$</td>
    <td>$-0.736$</td>
    <td>$-1.010$</td>
    <td>$-0.715$</td>
    <td>$-0.566$</td>
    <td>$-0.374$</td>
    <td>$-0.311$</td>
    <td>$-$</td>
    <td>$-$</td>
    <td>$-$</td>
  </tr>
</tbody>
</table>

For each $\text{ZrF}_{2}$ phase, the reaction enthalpy ($\Delta H_{r}$) associated with the chemical reaction (5) has been calculated using Eq. (6):

$$
\begin{aligned}
\Delta H_{r} &= \left(\frac{1}{2} E_{\text{tot}}[\text{ZrF}_{4}]+\frac{1}{2} E_{\text{tot}}[\text{Zr}] - E_{\text{tot}}[\text{ZrF}_{2}]\right) \\
&+ \left(\frac{1}{2} E_{\text{ZPE}}[\text{ZrF}_{4}]+\frac{1}{2} E_{\text{ZPE}}[\text{Zr}] - E_{\text{ZPE}}[\text{ZrF}_{2}]\right).
\tag{6}
\end{aligned}
$$

As shown in Table VI, depending on the $\text{ZrF}_{2}$ structure, $\Delta H_{r}$ varies from $-1.010$ eV/f.u., obtained for $o70\text{-ZrF}_{2}$, to $-0.311$ eV/f.u., for random-12. However, we should note that in the calculation of the reaction enthalpy $\Delta E_{\text{ZPE}}$ is small ($-0.03$ eV/f.u.) but contributes with a negative sign which lowers the value of $\Delta H_{r}$, which is already negative. In all cases, the reaction enthalpy is substantially negative, with a lowest value of $-0.3$ eV/f.u., indicating that the reaction is exothermic with respect to phase decomposition into $\text{ZrF}_{4}$ and metallic Zr. This result is difficult to reconcile with the experimental observation by McTaggart and Turnbull that $\text{ZrF}_{2}$ is stable up to $800^\circ\text{C}$. One possibility is that their $\text{ZrF}_{2}$ compound has a different structure to the six phases we highlight in this work. This is certainly possible, but in the absence of experimental atomic coordinates we are limited in what we can calculate and compare. Another possibility is that the experiments themselves are suspect; the data are from many years ago and very little information on the structure is provided. In either case, there is clearly a need for further experimental work on $\text{ZrF}_{2}$; such studies would clarify the experimental situation and provide a starting point for further computational work.

## IV. SUMMARY

The primary motivation in this study is to analyze the possible formation of $\text{ZrF}_{2}$ arising from the decay of a radioactive $^{90}\text{SrF}_{2}$ parent phase. We report a number of new phases with monoclinic and orthorhombic symmetry which have not previously been discussed. Our observation that these phases are thermodynamically unstable with respect to phase decomposition implies that radioparagenesis within $^{90}\text{SrF}_{2}$ pellets could lead to formation of metallic Zr and $\text{ZrF}_{4}$. For this to happen, however, significant mass diffusion would need to occur which may not be accessible on kinetic grounds. All the same, 0.3 eV/f.u. is a non-negligible thermodynamic driving force and cannot be easily dismissed. Radiation damage leads to a variety of processes including radiolysis (which modifies the structure via electronic excitation) and energetic displacement (associated with both the decay event itself and beam damage due to the passage of the $\beta$ particle). Further work quantifying defect kinetics associated with both of these processes would be necessary to conclusively address this issue.

As mentioned in previous sections, another possibility is that $\text{ZrF}_{2}$ phases exist which are more stable than those discovered in this work, and perhaps these phases are stable with respect to $\text{ZrF}_{4}$ and Zr as suggested by McTaggart and Turnbull. However, should such phases exist, they would only be important within a radioparagenesis context if the structures were somehow structurally related to the parent phase via simple displacive-type changes in structure.

Based on these observations we see reason to cautiously question some of the conclusions regarding the $^{90}\text{SrF}_{2}$ pellets stored at Hanford. A number of reports on these pellets have been published$^{39-46}$ but all of them fundamentally rely on the experiments of McTaggart and Turnbull from 1964. Given that our computations do not reinforce the conclusions of McTaggart and Turnbull, and noting that no further experiments have been performed on $\text{ZrF}_{2}$ since, we feel that further investigations are required. Only by understanding the stability of $\text{ZrF}_{2}$ in general, and radioparagenetic $\text{ZrF}_{2}$ in particular, will it be possible to predict the time evolution of the Hanford material. To this end, there may be merit in reanalyzing representative samples at Hanford since around half of the original $^{90}\text{Sr}$ has now decayed to $^{90}\text{Zr}$. Although the analysis would require an active handling facility due to the intense residual radiation field, such experiments would provide an excellent opportunity to directly observe radioparagenesis in action and thereby inform future development of technology for storing radioactive material.

## ACKNOWLEDGMENTS

N.A.M. and M.S. gratefully acknowledge financial support from the Australia Research Council under Project No. DP1097076 and computational support from National Computational Infrastructure. B.P.U. and C.R.S. gratefully acknowledge the support of the US Department of Energy through the Los Alamos National Laboratory/Laboratory Directed Research Development (LDRD) program for this work.

094104-10

$^{*}$N.Marks@curtin.edu.au

$^{1}$Board on Radioactive Waste Management and Earth and Life Studies, *Improving the Scientific Basis for Managing DOE's Excess Nuclear Materials and Spent Nuclear Fuel* (National Academies Press, Washington, DC, 2003) .

$^{2}$W. J. Gray, *Nature (London)* **296**, 547 (1982).

$^{3}$E. R. Vance, R. Roy, J. G. Pepin, and D. K. Agrawal, J. Mater. Sci. **17**, 947 (1982).

$^{4}$D. M. Strachan, E. C. Buck, J. A. Fortner, and N. J. Hess, Deter- mination of Transmutation Effects in Crystalline Waste Forms, FY Annual Report, 1997, doi: 10.2172/13677.

$^{5}$J. A. Fortner, D. T. Reed, A. J. Kropf, and N. J. Hess, Determination of Transmutation Effects in Crystalline Waste Forms, US DOE Report No. 55382, 1999, doi: 10.2172/828342.

$^{6}$N. J. Hess, F. J. Espinosa, S. D. Conradson, and W. J. Weber, J. Nucl. Mater. **281**, 22 (2000).

$^{7}$J. Fortner, S. Aase, and D. Reed, Mater. Res. Soc. Symp. Proc.**713**, JJ11.37.1 (2002).

$^{8}$C. Jiang, C. R. Stanek, N. A. Marks, K. E. Sickafus, and B. P. Uberuaga, *Phys. Rev. B* **79**, 132110 (2009).

$^{9}$B. P. Uberuaga, C. Jiang, C. R. Stanek, K. E. Sickafus, N. A. Marks, D. J. Carter, and A. L. Rohl, *Nucl. Instrum. Methods Phys. Res.*, Sect. B **268**, 3261 (2010).

$^{10}$C. Jiang, C. R. Stanek, N. A. Marks, K. E. Sickafus, and B. P. Uberuaga, *Philos. Mag. Lett.* **90**, 435 (2010).

$^{11}$C. Jiang, B. P. Uberuaga, K. E. Sickafus, F. M. Nortier, J. J. Kitten, N. A. Marks, and C. R. Stanek, *Energy Environ. Sci.* **3**, 130 (2010).

$^{12}$F. K. McTaggart and A. G. Turnbull, *Aust. J. Chem.* **17**, 727 (1964).

$^{13}$A. R. Oganov and C. W. Glass, *J. Chem. Phys.* **124**, 244704 (2006).

$^{14}$C. W. Glass, A. R. Oganov, and N. Hansen, *Comput. Phys. Commun.* **175**, 713 (2006).

$^{15}$G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

$^{16}$G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**, 15 (1996).

$^{17}$Y. Wang and J. P. Perdew, *Phys. Rev. B* **44**, 13298 (1991).

$^{18}$P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

$^{19}$H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188 (1976).

$^{20}$L. G. Hector, Jr., J. F. Herbst, W. Wolf, P. Saxe, and G. Kresse, *Phys. Rev. B* **76**, 014121 (2007).

$^{21}$K. Parlinski, Z.-. Q. Li, and Y. Kawazoe, *Phys. Rev. Lett.* **78**, 4063 (1997).

$^{22}$A. Togo, F. Oba, and I. Tanaka, *Phys. Rev. B* **78**, 134106 (2008).

$^{23}$R. F. W. Bader, *Atoms in Molecules: A Quantum Theory*, The International Series of Monographs on Chemistry (Clarendon Press, Oxford, 1990).

$^{24}$G. Henkelman, A. Arnaldsson, and H. Jónsson, *Comput. Mater. Sci.* **36**, 254 (2006).

$^{25}$K. G. Subhadra, K. A. Hussain, W. Hussain, and D. B. Sirdeshmukh, J. Mat. Sci. Lett. **4**, 777 (1985).

$^{26}$W. Hayes, *Crystals with the Fluorite Structure* (Clarendon Press, Oxford, 1974).

$^{27}$M. M. Elcombe, *J. Phys. C: Solid State Phys.* **5**, 2702 (1972).

$^{28}$P. Denham, G. R. Field, P. L. R. Morse, and G. R. Wilkinson, *Proc. Roy. Soc. Lond.* **A.317**, 55 (1970).

$^{29}$C. R. Stanek, B. P. Uberuaga, B. L. Scott, R. K. Feller, and N. A. Marks, Current Opinion in Solid State and Materials Science (in press).

$^{30}$J. F. Herbst and L. G. Hector Jr., *Phys. Rev. B* **79**, 155113 (2009).

$^{31}$G. Kresse, J. Furthmüller, and J. Hafner, *Europhys. Lett.* **32**, 729 (1995).

$^{32}$H. L. Yakel, *Acta Crystallogr.* **11**, 46 (1958).

$^{33}$W. Wolf and P. Herzig, J. Phys. Condens. Matter **12**, 4535 (2000).

$^{34}$R. Quijano, R. de Coss, and D. J. Singh, *Phys. Rev. B* **80**, 184103 (2009).

$^{35}$E. S. Fisher and C. J. Renken, *Phys. Rev.* **135**, A482 (1964).

$^{36}$C. Legein, F. Fayon, C. Martineau, M. Body, J.-Y. Buzaré, D. Massiot, E. Durand, A. Tressaud, A. Demourgues, O. Péron, and B. Boulard, *Inorg. Chem.* **45**, 10636 (2006).

$^{37}$E. Greenberg, J. L. Settle, H. M. Feder, and W. N. Hubbard, *J. Phys. Chem.* **65**, 1168 (1961).

$^{38}$M. G. M. van der Vis, E. H. P. Cordfunke, and R. J. M. Konings, *Thermochim. Acta* **302**, 93 (1997).

$^{39}$J. E. Hansen, Battelle, Pacific Northwest Laboratory Report No. BNWL-1308-6, 1971, doi: 10.2172/4752319.

$^{40}$J. H. Jarrett, Battelle, Pacific Northwest Laboratory Report No. BNWL-1308-10, 1972, doi: 10.2172/4646237.

$^{41}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. BNWL-1673, 1972, doi: 10.2172/4579539.

$^{42}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. BNWL-1845-4, 1974, doi: 10.2172/4232043.

$^{43}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. BNWL-2101, 1976, doi: 10.2172/7235763.

$^{44}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. BNWL-2284, 1977, doi: 10.2172/5344218.

$^{45}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. PNL-3846, 1981, doi: 10.2172/6323477.

$^{46}$H. T. Fullam, Battelle, Pacific Northwest Laboratory Report No. PNL-3833, 1981, doi: 10.2172/6258105.