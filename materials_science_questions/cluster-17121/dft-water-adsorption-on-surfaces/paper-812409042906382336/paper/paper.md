![](./images/812409042906382336_1.jpg)

Journal of Electroanalytical Chemistry 381 (1995) 269-273

![](./images/812409042906382336_2.jpg)

Preliminary note

# Adsorption of aromatic hydrocarbons on an electrode:
## a molecular dynamics study

S.-B. Zhu

Molecular Research Institute, 845 Page Mill Road, Palo Alto, CA 94304, USA

Received 8 September 1994; in revised form 29 September 1994

**Keywords:** Adsorption; Aromatic hydrocarbons

## 1. Introduction

Understanding adsorption behavior of aromatic molecules onto an electrode is of great value in electrochemistry and biology since many amino acid residues involve unsaturated organic ring structure. These molecules are typically classified as hydrophobic, though the polarizability of the $\pi$-electron cloud admits hydrophilic hydration above and below the aromatic plane [1,2,3]. One of the most striking manifestations in hydrophobic hydration is large negative and solute-size dependent entropies of solution [4]. Entropy is known as a major contributor to the adsorption process [5]. Therefore, large aromatic systems are expected to behave differently compared with the benzene molecule.

Previous computer simulations of dilute aqueous solutions of aromatic complexes have been focused on bulk states [1,2,3,6]. All these studies indicated a well-defined primary hydration shell around the benzene with a relatively high coordination number ($\approx 23$), as a common characteristic of hydrophobic solvation. However, compared with a typical hydrophobic species, the hydration structure is somewhat altered by the presence of the aromaticity. In particular, two water molecules exist, one on each side of the benzene plane, forming a weak hydrogen bond with the aromatic ring. When the benzene molecule contact adsorbs on an electrode, part of its primary hydration shell is lost. Inclusion of ions further disturbs the solvation structure, creating additional complications. If the electrolyte is neutral, the system is at the potential of zero charge (pzc). No electric double layer is formed. However, the electrode carries net charge if the aqueous subphase is electrically non-neutral. Since the flat wall can be viewed as a solute with an infinitely large radius, as well as a membrane or a macromolecule, the knowledge gained from this study should provide useful information for a wide range of scientific interests.

## 2. Computational details

The molecular dynamics systems described in this note are composed of two ions, one aromatic molecule, and a number of TIP4P water molecules [7]. The basic simulation cell is a cubic of $1.862 \times 1.862 \times 1.862\ \text{nm}^3$, confined between a dielectric wall specified by the 9-3 potential of Lee et al. [8] and a metal wall which is modeled conventionally by adding image interactions to represent the surface polarization. These two walls are placed in parallel at $z = \pm 0.931\ \text{nm}$. Surface corrugations and lattice symmetry are ignored for simplicity. Long range Coulomb interactions between electric charges of different molecules and/or their images are treated by the fast multipole algorithm [9].

There have been several existing ways to model the benzene molecule. Here we adopt an all-atom (12-site) version [6] which is superior in describing the structures of liquid and crystalline phases to the six-site version treating C-Hb as an atomic group [10]. Symbolically, we use Hb to distinguish the hydrogen atoms in benzene from the hydrogen in water. According to the known experimental data [11,12], the C-C bond length for the benzene molecule is set to be $0.14\ \text{nm}$, while the C-Hb bond length is $0.108\ \text{nm}$. In addition to benzene, we also investigate systems containing naphthalene which is composed of two aromatic rings and anthracene consisting of three aromatic rings, all on the same plane. The parameters for these larger aromatic hydrocarbons are taken to be the same as for benzene. However, the fusion carbons, designated as Cf, possess no charge. A common feature for these molecules is that the quadrupole moment is the lowest

0022-0728/95/$09.50 © 1995 Elsevier Science S.A. All rights reserved
SSDI 0022-0728(94)03777-9

nonzero term in the electrostatic multipole expansion. All the molecules considered in this work are treated as being rigid. Their mutual interactions are pairwise additive and the polarization effects are taken into account in an average way by introducing effective charges.

The benzene-water intermolecular potential energy function can be determined from ab initio quantum chemical calculations using the Hartree-Fock self-consistent-field approximation [10,13] or from optimized potential for liquid simulations (OPLS) designed for organic and biomolecular systems [14]. In this work, we adopt the latter scheme and list the potential parameters in Table 1. Also given in Table 1 are $\sigma_{\mathrm{Na}^{+}}$, $\sigma_{\mathrm{Cl}^{-}}$, $\epsilon_{\mathrm{Na}^{+}}$, and $\epsilon_{\mathrm{Cl}^{-}}$optimized by Chandrasekhar et al. [15] for the corresponding bulk aqueous environment. All the intermolecular interactions are described in a Coulomb plus Lennard-Jones format, using the Lorentz-Berthelot combining rule [16] for mixed Lennard-Jones energies and radii.

Altogether five constant $(N, V, T)$ molecular dynamics simulations are performed. The first system consists of one benzene molecule, one sodium ion, one chloride ion, and 154 TIP4P water molecules. The second and third systems are similarly constructed except that the benzene molecule is replaced by a naphthalene (System 2) or an anthracene (System 3). To keep the density approximately invariable the second system is diluted by 152 TIP4P water molecules, while the third by 150 TIP4P water molecules. These model the adsorption of a prototypical neutral organic on an electrode at pzc. The fourth and fifth systems are also similar to system 1. However, the solutions are not neutral. System 4 contains two sodium ions without anions, therefore, the net charge on the electrode is $-2 \mathrm{e}$. In contrast, system 5 contains two chloride ions with no cations. This gives rise to a net image charge of $+2 \mathrm{e}$. Each simulation lasts 1 ns, the first 200 ps of which are used for equilibrating the system at 294 K, while the remainder are for statistical averages. Systems 1-3 are initiated from a lattice structure, while Systems 4 and 5 are started from the final configuration of System 1 by replacing one ion with its counterion. Therefore, the benzene molecule in Systems 4 and 5 is initially in close vicinity to the metal surface.

![](./images/812409042906382336_3.jpg)

Fig. 1. Number density profiles for the center of mass of aromatic molecules and the hydrogen atoms in these molecules. Curves from top to bottom represent systems for $\mathrm{C}_{6} \mathrm{H}_{6} / \mathrm{Na} / \mathrm{Na}, \mathrm{C}_{6} \mathrm{H}_{6} / \mathrm{Cl} / \mathrm{Cl}$, $\mathrm{C}_{6} \mathrm{H}_{6} / \mathrm{Na} / \mathrm{Cl}, \mathrm{C}_{10} \mathrm{H}_{8} / \mathrm{Na} / \mathrm{Cl}$, and $\mathrm{C}_{14} \mathrm{H}_{10} / \mathrm{Na} / \mathrm{Cl}$. The metal wall is placed at $z=0.931 \mathrm{~nm}$.

Nevertheless, the final position of the benzene is independent of its initial position. With a time step of 2 fs, the entire computation takes about 400 h of IBM RS/6000 CPU time.

### 3. Results and discussions

Fig. 1 describes the adsorption behavior of the aromatic molecules. It clearly shows that the tendency for adsorption increases with the molecular size, as indicated by the higher and sharper density profiles. This is an expected entropy effect. These aromatic molecules prefer a flat adsorption, although tilting, rocking, and vibrations of the molecules with respect to the surface are allowed. The amplitude of these motions decrease

Table 1
Potential parameters

<table>
<thead>
<tr>
<th>$\epsilon_{\mathrm{Na}^{+}}$</th>
<th>$\sigma_{\mathrm{Na}^{+}}$</th>
<th>$\epsilon_{\mathrm{Cl}^{-}}$</th>
<th>$\sigma_{\mathrm{Cl}^{-}}$</th>
<th>$\epsilon_{\mathrm{C}}$</th>
<th>$\sigma_{\mathrm{C}}$</th>
<th>$\epsilon_{\mathrm{Hb}}$</th>
<th>$\sigma_{\mathrm{Hb}}$</th>
<th>$q_{\mathrm{C}}$</th>
<th>$q_{\mathrm{Hb}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>6.72</td>
<td>0.190</td>
<td>0.493</td>
<td>0.442</td>
<td>0.293</td>
<td>0.355</td>
<td>0.126</td>
<td>0.242</td>
<td>−0.115</td>
<td>0.115</td>
</tr>
</tbody>
</table>

$\epsilon$ is in units of $\mathrm{kJ} \mathrm{mol}^{-1}$, $\sigma$ is in units of nm, and $q$ is in units of electron charge. The potential parameters for the sodium cation and the chloride anion are from Ref. [15] for C and Hb are from Ref. [6]. The interactions of all the species with the solid wall are identically modeled by the 9-3 potential with the repulsive coefficient $C_{9}=17.447 \times 10^{-6} \mathrm{~kJ} \mathrm{~nm}^{9} \mathrm{~mol}^{-1}$ and the attractive coefficient $C_{3}=76.144 \times 10^{-3} \mathrm{~kJ} \mathrm{~nm}^{3} \mathrm{~mol}$ [8].

![](./images/812409042906382336_4.jpg)

Fig. 2. Number density profiles for the sodium and chloride ions. Curves from top to bottom represent systems for $C_{6}H_{6}/Na/Cl$, $C_{6}H_{6}/Na/Na$, and $C_{6}H_{6}/Cl/Cl$.

as the molecular size increases. When the benzene ring adsorbs flat, one water molecule resides just on top of the adsorbate with an O-H bond pointing at the center of the ring. Probably, the most interesting finding in this figure is that the benzene desorbs from the surface when the solution contains two sodium ions. The adsorption behavior does not change significantly, if both ions are chloride. Figs. 2-4 give a detailed explanation of this phenomenon.

In Fig. 2, the density profiles for the ions are plotted. If the electrolyte is neutral, both the sodium ion and the chloride ion are fully hydrated and are diffusely distributed across the film. This behavior does not seem to depend on the molecular size significantly. For convenience, the curves for the naphthalene and anthracene systems are not plotted. When the electrolyte contains two sodium ions, the hydration structure is still complete. However, the sodium has a considerable propensity to adsorb on the surface, forming a solvent-separated configuration. With about equal probability, the ion extends its existence to the diffuse region. No distribution is observed beyond $z=-0.4$ nm. A very different behavior is found for the system containing two chloride ions. The larger anion spends most of the time in contact with the metal surface, losing part of its hydration shell. There is a small, though non-negligible, probability for the ion to stay in

![](./images/812409042906382336_5.jpg)

Fig. 3. Electric field profiles. Curves from top to bottom represent systems for $C_{6}H_{6}/Na/Na$, $C_{6}H_{6}/Cl/Cl$, $C_{6}H_{6}/Na/Cl$, $C_{10}H_{8}/Na/Cl$, and $C_{14}H_{10}/Na/Cl$.

![](./images/812409042906382336_6.jpg)

Fig. 4. Dipole density profiles. Curves from top to bottom represent systems for $C_{6}H_{6}/Cl/Cl$, $C_{6}H_{6}/Na/Cl$, $C_{10}H_{8}/Na/Cl$, $C_{14}H_{10}/Na/Cl$, and $C_{6}H_{6}/Na/Na$.

the diffuse region. These differences are responsible to the different behavior of the benzene, which is de- scribed in Fig. 1.

The above conclusion becomes more evident from Fig. 3, where the electric field distribution along the surface's normal direction is displayed. Unlike electric fields from uniformly charged plates, the field gener- ated from image charges varies with the position of the ions and is fluctuating. Its time average depends on the charge distribution in solution and the adsorption be- havior of ions. For systems with one pair of unlike ions, the electric field profiles have similar shape, although there are some minor differences in the region near these aromatic molecules. In particular, the depth of the field minimum at $z \approx 0.36$ nm increases with the size of the organic molecule. The orientational order- ing of the water molecules in the top region of the adsorbates is responsive to this change. When the system contains two chloride ions, the electric field distributes differently. However, the difference is sig- nificant only in a small region, near the metal surface on which the anion adsorbs. Because of the strong adsorption tendency of the chloride ions, their influ- ences on orientational ordering of the water molecules are largely cancelled out by their images and, there- fore, are local (see Fig. 4). In the central part of the film, the electrolyte is quasi-neutral and the electric field nearly vanishes, just as the case for the three systems containing sodium-chloride ion pair. Conse- quently, the adsorption behavior of the benzene molecule in System 5 does not change much. There is no such quasi-neutral region if the system contains two sodium ions. As mentioned earlier, the sodium ions are fully hydrated and are diffusely distributed. The elec- tric field decreases from $\sim 7.9 ~V ~nm^{-1}$ at the metal side to zero at the dielectric side. This field is not effectively screened by the electrolyte solution and its derivative leads to strong orientational reorganization of the water molecules, which creates a driving force causing the neutral organic molecule desorb from the metal, as predicted by the simple model of flip-flop water [17,18] and evidenced by many experimental data[18,19]. Fig. 4 describes the dipole density profiles of water in these systems. For System 4, there is a large dipole near the metal surface. The quantity decreases as the distance to the surface increases and changes its sign at $z \approx 0$.

## 4. Conclusions

The adsorption behavior of aromatic hydrocarbons on a metal surface is studied by means of molecular dynamics simulations. It is found that the adsorption strength increases with the molecular size, as expected from the entropy effects. Because of the quadrupole moment and higher order moments, the adsorption is less stable compared with neutral solutes having no internal charge distribution but having similar size [5]. A further decrease of the adsorption strength is ob- served when the metal surface is charged. This finding agrees with theoretical predictions from simple flip-flop models [17,18] and experimental observations [18,19]. In the present work, the surface potential is generated by the net image charge of the nonneutral electrolyte solution. For the system containing two sodium ions, the surface potential is about -5.1 V and has a wide effective range, while for the system containing two chloride ions, the surface potential is $\sim 1.4 ~V$ and rapidly drops to its minimum near $z=0.68$ nm where the first water layer emerges. This leads to the differ- ent adsorption behavior of the benzene molecule in the two solutions. It has been known experimentally that the range of potential accessible on a mercury elec- trode is no more than 2 V. The present model seems to overestimate the electric field and the surface poten- tial, which indicates that the capacity of the interface is much smaller than that found in experiments. Al- though the present study uses a rather simple model, it is the first attempt to investigate the dependences of the adsorption strength on solute size and surface potential through systematic molecular dynamics calcu- lations. The results are quite encouraging and suggest that further efforts would be worthwhile.

## Acknowledgments

This research was supported by IBM Almaden Re- search Center and the Office of Naval Research.

## References

[1] P. Linse, G. Karlström, and B. Jönsson, J. Am. Chem. Soc., 106(1984) 4096.
[2] G. Ravishanker, P.K. Mehrotra, M. Mezei, and D.L. Beveridge, J. Am. Chem. Soc., 106 (1984) 4102.
[3] P. Linse, J. Am. Chem. Soc., 112 (1990) 1744.
[4] H.S. Frank and M.J. Evans, J. Chem. Phys., 13 (1945) 507.
[5] S.-B. Zhu, submitted for publication in Computational Materials Science.
[6] W.L. Jorgensen and D.L. Severance, J. Am. Chem. Soc., 112(1990) 4768.
[7] W.L. Jorgensen, J. Chandrasekhar, J.D. Madura, R.W. Impey, and M.L. Klein, J. Chem. Phys., 79 (1983) 926.
[8] C.Y. Lee, J.A. McCammon, and P.J. Rossky, J. Chem. Phys., 80(1984) 4448.
[9] L. Greengard and V. Rokhlin, J. Comp. Phys., 73 (1987) 325.
[10] G. Karlström, P. Linse, A. Wallqvist, and B. Jönsson, J. Am. Chem. Soc., 105 (1983) 3777.
[11] O. Bastiansen, Acta Crystallogr., 10 (1957) 861.
[12] M.D. Harmony, V.W. Laurie, R.L. Kuczkowski, R.H. Schwen- deman, and D.A. Ramsey, J. Phys. Chem. Ref. Data, 8 (1979)619.

[13] E. Clementi, F. Cavallone, and R. Scordamaglia, J. Am. Chem. Soc., 99 (1977) 5531.

[14] W.L. Jorgensen and J. Tirado-Rives, J. Am. Chem. Soc., 110 (1988) 1657.

[15] J. Chandrasekhar, D.C. Spellmeyer, and W.L. Jorgensen, J. Am. Chem. Soc., 106 (1984) 903.

[16] J.O. Hirschfelder, C.F. Curtiss, and R.B. Bird, Theory of Gases and Liquids, Wiley, New York, 1954.

[17] A.N. Frumkin, Z. Phys., 35 (1926) 792.

[18] J. O'M Bockris and A.K.N. Ready, Modern Electrochemistry, Vol. I, Plenum, New York, 1970.

[19] B.B. Damaskin, O.A. Petrii, and V.V. Batrakov, Adsorption of Organic Compounds on Electrodes, Plenum, New York, 1971.