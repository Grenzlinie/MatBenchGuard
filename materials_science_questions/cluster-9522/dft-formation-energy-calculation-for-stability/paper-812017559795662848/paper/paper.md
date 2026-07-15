# Thermodynamic modelling of the partially ordered solid solution $\mathrm{Hf}_{5-x}\mathrm{Nb}_{x}\mathrm{Ge}_{4}$ supported by ab initio calculations

Piotr Warczok $^{\mathrm{a}}$, Florian Mittendorfer $^{\mathrm{b,c}}$, Georg Kresse $^{\mathrm{b,c}}$, Aleš Kroupa $^{\mathrm{d}}$, Herbert Ipser $^{\mathrm{a}}$, Klaus W. Richter $^{\mathrm{a,*}}$

$^{\mathrm{a}}$ Institute of Inorganic Chemistry/Materialchemistry, University of Vienna, Währinger Strasse 42, A-1090 Wien, Austria
$^{\mathrm{b}}$ Institute of Materialphysics, University of Vienna, Sensengasse 8, A-1090 Wien, Austria
$^{\mathrm{c}}$ Center for Computational Materials Science, Sensengasse 8, A-1090 Wien, Austria
$^{\mathrm{d}}$ Institute of Physics of Materials, Academy of Sciences of the Czech Republic, Zizkova 22, 61622 Brno, Czech Republic

Received 6 July 2006; received in revised form 9 October 2006; accepted 15 November 2006
Available online 26 January 2007

## Abstract
The site preferences in the solid solution phase $\mathrm{Hf}_{5-x}\mathrm{Nb}_{x}\mathrm{Ge}_{4}$ ($0 < x < 3.8$) were modelled with the "Compound Energy Formalism" model. The ground state energies of the end members calculated from ab initio density functional theory were taken as input parameters for the model. These ground state energies were computed for models with either fixed atomic positions or fully relaxed structures. The results of the former computation were used for the construction of a simplified model. Site fractions modelled with both, original and simplified models fit well to the experimental values, confirming the almost stepwise substitution mechanism in this compound. Non-linear trends of the lattice parameters found experimentally could be reproduced very well.

© 2006 Elsevier Masson SAS. All rights reserved.

Keywords: Hafnium niobium germanides; Crystal structure; Differential fractional site occupation; First principles; Compound energy formalism

---

## 1. Introduction
A recent investigation of the Ge–Hf–Nb ternary system [1] revealed that the binary compound $\mathrm{Hf}_{5}\mathrm{Ge}_{4}$ ($\mathrm{Sm}_{5}\mathrm{Ge}_{4}$ type, $oP36$, $Pnma$, Table 1) [2] forms an extended ternary solid solution $\mathrm{Hf}_{5-x}\mathrm{Nb}_{x}\mathrm{Ge}_{4}$ ($0 \leq x \leq 3.8$). The X-ray investigation (single crystal and powder diffraction methods followed by Rietveld refinement) yielded lattice parameters as well as site occupations of hafnium and niobium on metal sites for different samples within this substitutional range. The results showed a strong preference of niobium to substitute hafnium at the three independent metal sites, such that the substitution proceeds in an almost stepwise manner. The observed order of the substituted sites could be explained by analysis of crystal site volumes (Dirichlet domains) and atomic orbital populations obtained by Extended Hückel (EHTB) calculations. For the site occupation (i.e. the mole fraction of substituted sites for each symmetry inequivalent site) description a simple "Compound Energy Formalism" (CEF) model [3] was used. This model belongs to the group of sublattice models where the term "sublattice" refers to a set of atom positions within the structure (defined by one or more independent sites) showing identical occupation. The Gibbs energies for hypothetical "end members" (i.e. compounds with sublattices fully occupied by only one atom type) were derived from extrapolation of experimental values, linear superposition and Gibbs energy minimization [1].

The $\mathrm{Sm}_{5}\mathrm{Ge}_{4}$ structure type, which represents the structure of $\mathrm{Hf}_{5}\mathrm{Ge}_{4}$, is quite common in the binary germanium–lanthanide systems [4] and was also reported for the Ge–Nb–Zr and Ge–Ta–Zr systems as ternary phase [5,6]. The structural features were discussed earlier [1,6,7]. $\mathrm{Hf}_{5}\mathrm{Ge}_{4}$ can be described

* Corresponding author. Tel.: +43 1 4277 52910; fax: +43 1 4277 9529.
E-mail address: klaus.richter@univie.ac.at (K.W. Richter).

1293-2558/$ - see front matter © 2006 Elsevier Masson SAS. All rights reserved.
doi:10.1016/j.solidstatesciences.2006.11.006

<table><thead><tr><td colspan="2">Table 1Structure data of ${\text{Hf}}_{5}{\text{Ge}}_{4}$ according to Ref. [2]</td></tr></thead><tbody><tr><td>Formula</td><td>${\text{Hf}}_{5}{\text{Ge}}_{4}$</td></tr><tr><td>Structure type</td><td>${\text{Sm}}_{5}{\text{Ge}}_{4}$</td></tr><tr><td>Pearson symbol</td><td>$oP36$</td></tr><tr><td>Space group</td><td>Pnma(no. 62)</td></tr><tr><td>Lattice parameters</td><td>$a=7.017(1)$</td></tr><tr><td></td><td>$b=13.434(4)$</td></tr><tr><td></td><td>$c=7.105(1)$</td></tr><tr><td>Atom positions</td><td>Wyckoff position</td><td>$x$</td><td>$y$</td><td>$z$</td></tr><tr><td colspan="5"></td></tr><tr><td>Hf1</td><td>$4c$</td><td>$0.1811$</td><td>$1/4$</td><td>$0.0021$</td></tr><tr><td>Hf2</td><td>$8d$</td><td>$0.1457$</td><td>$0.6239$</td><td>$0.1671$</td></tr><tr><td>Hf3</td><td>$8d$</td><td>$0.0141$</td><td>$0.0946$</td><td>$0.3229$</td></tr><tr><td>Ge1</td><td>$4c$</td><td>$0.0534$</td><td>$1/4$</td><td>$0.6110$</td></tr><tr><td>Ge2</td><td>$4c$</td><td>$0.3212$</td><td>$1/4$</td><td>$0.3540$</td></tr><tr><td>Ge3</td><td>$8d$</td><td>$0.3039$</td><td>$0.5407$</td><td>$0.4648$</td></tr></tbody></table>

by successive layers of germanium octahedra sharing their corners. These octahedra are centered by the metal atoms on the position Hf1 and are face-capped by metal atoms on positions Hf2 and Hf3 (see Fig. 1).

In the present work, we investigate the modelling of the site fractions as a function of the composition using a CEF model relying on ab initio density functional theory calculations. The latter were used to determine the Gibbs energies of the end members which had been estimated in the previous paper [1]. Calculated structural parameters of these end members are also compared with experimental values. The notation of end members is similar to the notation used in Ref. [1], i.e. (M1:M2:M3:Ge) where M1, M2, M3 are elements occupying the Hf1, Hf2 and Hf3 sublattices, respectively.

![](./images/812017559795662848_1.jpg)

Fig. 1. Views along [100] (above) and [010] (below) of the ${\text{Hf}}_{5}{\text{Ge}}_{4}$ (oP36,Pnma) crystal structure. Dark spheres represent the metal atoms on position Hf2 and Hf3, bright spheres represent the germanium atoms. Atoms on position Hf1 are in the center of the octahedra.

## 2. Method

The ground state energies of the end members ($T=0$ K), calculated by theVienna Ab initio Simulation Package(VASP) [8,9], were taken as input for the CEF model. For determination of the ground state energy, the cell volume, the cell and the atomic coordinates were optimized using a conjugate-gradient algorithm [10]. For additional test calculations, only the unit cell shape was allowed to vary freely, while the coordinates of the atoms and the unit cell volume were kept fixed. In both cases, the starting structures (lattice constants, atom positions) were taken from the calculated ${\text{Hf}}_{5}{\text{Ge}}_{4}$ equilibrium structure (i.e. the cell with minimal ground state energy), which itself was determined along the same line starting from the literature data [2]. In order to determine the optimal volume (the volume of the structure with the minimal ground state energy), the energy was computed for a series of volumes covering an interval of $(0.96-1.02)\times V_{{\text{Hf}}_{5}{\text{Ge}}_{4}}$, where $V_{{\text{Hf}}_{5}{\text{Ge}}_{4}}$ is the calculated equilibrium volume, and the final energies were fitted to a polynomial. The potentials for Ge, Hf and Nb were generated with theprojector augmented wavemethod [11,12]. The generalized gradient approximation PBE [13] with a plane wave cut-off energy of 220 eV was applied throughout this work. For the integration of the Brillouin zone, a $4\times 2\times 4$ $\Gamma$-centered Monkhorst–Pack grid [14] was used, and the $k$-point convergence was examined with a $10\times 5\times 10$ grid for the equilibrium ground state structures. The tetrahedron method with Blöchl corrections [15] was used to determine the partial occupancy of each one-electron wave function.

The formation energy of the given end members was calculated by subtraction of the calculated ground state energies of the most stable phases of the corresponding elements at 0 K [germanium (cubic diamond), hafnium (hcp) and niobium (bcc)]. Subsequently, the energy of substitution (substitutional energy) was calculated by referring the calculated formation energies to the formation energy of the (Hf:Hf:Hf:Ge) end member (i.e. ${\text{Hf}}_{5}{\text{Ge}}_{4}$).

Site fraction modelling was done using theThermo-Calcsoftware package [16]. The database used for calculations included a thermodynamic description of the reference state phases (Ge-cd, Hf-hcp, Nb-bcc) taken from the SGTE database [17]. For the thermodynamic description of ${\text{Hf}}_{5-x}{\text{Nb}}_{x}{\text{Ge}}_{4}$, the sublattice model $({\text{Hf}},{\text{Nb}})_{1}({\text{Hf}},{\text{Nb}})_{2}({\text{Hf}},{\text{Nb}})_{2}{\text{Ge}}_{4}$ consistent

with the $Hf_5Ge_4$ structure type (Table 1) was used yielding a total number of eight end members. As in the previous work [1], any excess Gibbs energy contribution was neglected in the used CEF model, and the Gibbs energy of the solid solution was described as a sum of the end member Gibbs energies and the entropy of mixing term, in the form of:

$$
\begin{aligned}
G_{\mathrm{Hf}_{0.555-x} \mathrm{Nb}_{x} \mathrm{Ge}_{0.445}}=& y_{\mathrm{Hf}}^{\mathrm{I}} y_{\mathrm{Hf}}^{\mathrm{II}} y_{\mathrm{Hf}}^{\mathrm{III}} G(\mathrm{Hf}: \mathrm{Hf}: \mathrm{Hf}: \mathrm{Ge}) \\
&+y_{\mathrm{Nb}}^{\mathrm{I}} y_{\mathrm{Hf}}^{\mathrm{II}} y_{\mathrm{Hf}}^{\mathrm{III}} G(\mathrm{Nb}: \mathrm{Hf}: \mathrm{Hf}: \mathrm{Ge}) \\
&+y_{\mathrm{Hf}}^{\mathrm{I}} y_{\mathrm{Nb}}^{\mathrm{II}} y_{\mathrm{Hf}}^{\mathrm{III}} G(\mathrm{Hf}: \mathrm{Nb}: \mathrm{Hf}: \mathrm{Ge}) \\
&+y_{\mathrm{Hf}}^{\mathrm{I}} y_{\mathrm{Hf}}^{\mathrm{II}} y_{\mathrm{Nb}}^{\mathrm{III}} G(\mathrm{Hf}: \mathrm{Hf}: \mathrm{Nb}: \mathrm{Ge}) \\
&+y_{\mathrm{Hf}}^{\mathrm{I}} y_{\mathrm{Nb}}^{\mathrm{II}} y_{\mathrm{Nb}}^{\mathrm{III}} G(\mathrm{Hf}: \mathrm{Nb}: \mathrm{Nb}: \mathrm{Hf}: \mathrm{Ge}) \\
&+y_{\mathrm{Nb}}^{\mathrm{I}} y_{\mathrm{Hf}}^{\mathrm{II}} y_{\mathrm{Nb}}^{\mathrm{III}} G(\mathrm{Nb}: \mathrm{Hf}: \mathrm{Nb}: \mathrm{Ge}) \\
&+y_{\mathrm{Hf}}^{\mathrm{I}} y_{\mathrm{Nb}}^{\mathrm{II}} y_{\mathrm{Nb}}^{\mathrm{III}} G(\mathrm{Hf}: \mathrm{Nb}: \mathrm{Nb}: \mathrm{Ge}) \\
&+y_{\mathrm{Nb}}^{\mathrm{I}} y_{\mathrm{Nb}}^{\mathrm{II}} y_{\mathrm{Nb}}^{\mathrm{III}} G(\mathrm{Nb}: \mathrm{Nb}: \mathrm{Nb}: \mathrm{Ge}) \\
&+R T\left[0.111\left(y_{\mathrm{Hf}}^{\mathrm{I}} \ln y_{\mathrm{Hf}}^{\mathrm{I}}+y_{\mathrm{Nb}}^{\mathrm{I}} \ln y_{\mathrm{Nb}}^{\mathrm{I}}\right)\right. \\
&\left.+0.222\left(y_{\mathrm{Hf}}^{\mathrm{II}} \ln y_{\mathrm{Hf}}^{\mathrm{II}}+y_{\mathrm{Nb}}^{\mathrm{II}} \ln y_{\mathrm{Nb}}^{\mathrm{II}}\right)\right. \\
&\left.+0.222\left(y_{\mathrm{Hf}}^{\mathrm{III}} \ln y_{\mathrm{Hf}}^{\mathrm{III}}+y_{\mathrm{Nb}}^{\mathrm{III}} \ln y_{\mathrm{Nb}}^{\mathrm{III}}\right)\right]
\end{aligned}
$$

$y_{\mathrm{M}}^{\mathrm{I}}$ - Site fraction of the metal M on the site Hf1.
$y_{\mathrm{M}}^{\mathrm{II}}$ - Site fraction of the metal M on the site Hf2.
$y_{\mathrm{M}}^{\mathrm{III}}$ - Site fraction of the metal M on the site Hf3.
$G(\mathrm{M} 1: \mathrm{M} 2: \mathrm{M} 3: \mathrm{Ge})$ - Gibbs energy of the end member with the metal M1 on Hf1 sublattice, M2 on Hf2 sublattice, M3 on Hf3 sublattice.

The thermodynamic simulation of the equilibrium site frac- tions was performed at a temperature of 1673 K, which was the annealing temperature of the experimental investigation reported in Ref. [1].

## 3. Results
### 3.1. Ab initio calculations and thermodynamic analysis

The calculated energies of formation and energies of substi- tution for all fully relaxed end members are listed in Table 2. It is evident that hafnium substitution by niobium is energeti- cally favored at the Hf1 position, where the substitutional en- ergy is only 0.14 kJ/mol. Surprisingly, both (Hf:Nb:Hf:Ge) and (Hf:Hf:Nb:Ge) end members have exactly the same energy of substitution (5.22 kJ/mol). In principle, this could be interpreted as a coincidental energetic equivalence for nio- bium substitution at the sites Hf2 and Hf3. However, in this case one would also expect similar substitutional energies for (Nb:Nb:Hf:Ge) and (Nb:Hf:Nb:Ge) which is not observed by the calculations (compare Table 2). Thus, the results suggest that the final structures of (Hf:Nb:Hf:Ge) and (Hf:Hf:Nb:Ge) obtained after relaxation are symmetry equivalent and this prompted us to a careful investigation of the final structures of these two end members.

<table>
<caption>Table 2<br>Calculated energies of formation and energies of substitution for end member structures with relaxed atom positions</caption>
<thead>
<tr>
<th>End member</th>
<th>Index $x$</th>
<th>Energy of<br>formation<br>[kJ/mol]</th>
<th>Energy of<br>substitution<br>[kJ/mol]</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Hf:Hf:Hf:Ge)</td>
<td>0</td>
<td>−67.66</td>
<td>0.00</td>
</tr>
<tr>
<td>(Nb:Hf:Hf:Ge)</td>
<td>0.111</td>
<td>−67.52</td>
<td>0.14</td>
</tr>
<tr>
<td>(Hf:Nb:Hf:Ge)</td>
<td>0.222</td>
<td>−62.44</td>
<td>5.22</td>
</tr>
<tr>
<td>(Hf:Hf:Nb:Ge)</td>
<td>0.222</td>
<td>−62.44</td>
<td>5.22</td>
</tr>
<tr>
<td>(Nb:Nb:Hf:Ge)</td>
<td>0.333</td>
<td>−59.66</td>
<td>8.00</td>
</tr>
<tr>
<td>(Nb:Hf:Nb:Ge)</td>
<td>0.333</td>
<td>−48.08</td>
<td>19.58</td>
</tr>
<tr>
<td>(Hf:Nb:Nb:Ge)</td>
<td>0.444</td>
<td>−40.58</td>
<td>27.08</td>
</tr>
<tr>
<td>(Nb:Nb:Nb:Ge)</td>
<td>0.555</td>
<td>−37.12</td>
<td>30.54</td>
</tr>
</tbody>
</table>

Index $x$ refers to the composition of $\mathrm{Hf}_{0.555-x} \mathrm{Nb}_{x} \mathrm{Ge}_{0.445}$.

The calculated energies for selected structures with the atoms fixed at the positions of the $Hf_5Ge_4$ structure helped to clarify the issue further (see Table 3). Generally, it is observed that values in this Table are 1−2 kJ/mol larger than those com- puted with relaxed positions. The difference of more than 10 kJ/ mol between the energies for (Hf:Nb:Hf:Ge) (−60.96 kJ/mol) and (Hf:Hf:Nb:Ge) (−49.48 kJ/mol) in Table 3 compared to no difference in Table 2, suggests that (Hf:Hf:Nb:Ge) is the less stable end member, and it transforms to the more stable structure with significant changes of the atom positions, when atoms are allowed to relax. More details regarding all calculated structures are discussed in Section 3.2. The computed substitu- tional energies in Table 3 confirm that the substitution of haf- nium by niobium is favored on the Hf1 position, followed by Hf2 and finally Hf3.

Qualitatively, it is possible to predict the steps of substitu- tion with the aid of the calculated substitutional energies. This is shown in Fig. 2 by plotting these values as a function of the niobium content indicated by the index $x$. By connecting the most stable end members, one can confirm the order of substi- tution found experimentally, which is:

$$
\begin{aligned}
(\mathrm{Hf}: \mathrm{Hf}: \mathrm{Hf}: \mathrm{Ge}) & \rightarrow(\mathrm{Nb}: \mathrm{Hf}: \mathrm{Hf}: \mathrm{Ge}) \rightarrow \\
(\mathrm{Nb}: \mathrm{Nb}: \mathrm{Hf}: \mathrm{Ge}) & \rightarrow(\mathrm{Nb}: \mathrm{Nb}: \mathrm{Nb}: \mathrm{Ge})
\end{aligned}
$$

We note that the instability of (Hf:Hf:Nb:Ge) is of little practical consequence for our simulations, since niobium will always initially occupy the Hf1 site, and the (Nb:Hf:Nb:Ge) configuration is stable and does not relax towards the (Nb:Nb:Hf:Ge) structure.

<table>
<caption>Table 3<br>Calculated energies of formation and energies of substitution for end member structures with atoms fixed at positions of the $Hf_5Ge_4$ structure</caption>
<thead>
<tr>
<th>End member</th>
<th>Index $x$</th>
<th>Energy of<br>formation<br>[kJ/mol]</th>
<th>Energy of<br>substitution<br>[kJ/mol]</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Hf:Hf:Hf:Ge)</td>
<td>0</td>
<td>−67.66</td>
<td>0.00</td>
</tr>
<tr>
<td>(Nb:Hf:Hf:Ge)</td>
<td>0.111</td>
<td>−67.25</td>
<td>0.41</td>
</tr>
<tr>
<td>(Hf:Nb:Hf:Ge)</td>
<td>0.222</td>
<td>−60.96</td>
<td>6.70</td>
</tr>
<tr>
<td>(Hf:Hf:Nb:Ge)</td>
<td>0.222</td>
<td>−49.48</td>
<td>18.18</td>
</tr>
<tr>
<td>(Nb:Nb:Nb:Ge)</td>
<td>0.555</td>
<td>−35.74</td>
<td>31.92</td>
</tr>
</tbody>
</table>

![](./images/812017559795662848_2.jpg)

Fig. 2. Substitutional energies of various end members. The most stable ones are connected by a line.

Using the substitutional energies calculated at 0 K, we obtained plots of equilibrium site fractions for niobium at these positions as a function of the composition parameter $x$ using the compound energy formalism. Two sets of end member energies were used for this modelling. Set A consists of the energies listed in Table 2. For (Hf:Hf:Nb:Ge) which was found to be instable, the value of the calculation with atoms fixed at the $\text{Hf}_5\text{Ge}_4$ positions (i.e. from Table 3) was taken. In set B, a simplified approach was used to obtain the substitutional energies: for end members with only one sublattice occupied by niobium (i.e. (Nb:Hf:Hf:Ge), (Hf:Nb:Hf:Ge) and (Hf:Hf:Nb:Ge)) the values were taken from Table 3, while the others were calculated as their superposition (e.g. $E(\text{Nb:Hf:Nb:Ge}) = E(\text{Nb:Hf:Hf:Ge}) + E(\text{Hf:Hf:Nb:Ge}) = 18.59$ kJ/mol). Both sets are listed in Table 4. Results of CEF calculations are presented in Fig. 3 where the experimental results from Ref. [1] are also displayed. The diagrams show that modelled site fractions fit well to experimental data in both cases. It appears that simulations of site fractions in solid solutions at elevated temperatures based on end member energies for 0 K yield satisfying results. This could mean that the Gibbs energies for all end members rise by a similar amount with temperature, hence their temperature dependence can be neglected for a modelling of site fractions in partially ordered solid solutions. Moreover, there is no significant difference between the observed equilibrium distribution for sets A and B, so that the set with only three computed energy values yields a very satisfactory description of the experimental results. As the computation of structures with no atom relaxation is less time-consuming and the number of calculated end members may be kept small, the approach used for set B allows a relatively fast analysis of partial ordering even in complicated structures, which would otherwise require the calculation of a large number of hypothetical structures.

<table>
<caption>Table 4<br>End member energies used as components in CEF model (see text)</caption>
<thead>
<tr>
<th>End member</th>
<th>Set A<br>[kJ/mol]</th>
<th>Set B<br>[kJ/mol]</th>
</tr>
</thead>
<tbody>
<tr>
<td>(Hf:Hf:Hf:Ge)</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>(Nb:Hf:Hf:Ge)</td>
<td>0.14</td>
<td>0.41</td>
</tr>
<tr>
<td>(Hf:Nb:Hf:Ge)</td>
<td>5.22</td>
<td>6.70</td>
</tr>
<tr>
<td>(Hf:Hf:Nb:Ge)</td>
<td>18.18</td>
<td>18.18</td>
</tr>
<tr>
<td>(Nb:Nb:Hf:Ge)</td>
<td>8.00</td>
<td>7.11</td>
</tr>
<tr>
<td>(Nb:Hf:Nb:Ge)</td>
<td>19.58</td>
<td>18.59</td>
</tr>
<tr>
<td>(Hf:Nb:Nb:Ge)</td>
<td>27.08</td>
<td>24.88</td>
</tr>
<tr>
<td>(Nb:Nb:Nb:Ge)</td>
<td>30.54</td>
<td>25.29</td>
</tr>
</tbody>
</table>

![](./images/812017559795662848_3.jpg)

Fig. 3. Site fractions calculated with set A (a) and set B (compare Table 4) (b). Experimental values are taken from Ref. [1].

### 3.2. Structure analysis

A comparison of calculated and experimental data of the $\text{Hf}_5\text{Ge}_4$ structure (Hf:Hf:Hf:Ge) is presented in Table 5. Calculated atom positions fit very well to the data found in the literature [2], with a maximum difference of 0.001 (fractional coordinate), while the calculated lattice parameters are approximately 1%

<table><caption>Table 5 Comparison of literature and calculated data for the Hf₅Ge₄ structure</caption>
<tbody><tr><th colspan="2"></th><th>Ref. [2]</th><th>Calculated</th></tr>
<tr><td rowspan="3">Lattice parameters [Å]</td><td>$a$</td><td>7.017</td><td>7.092</td></tr>
<tr><td>$b$</td><td>13.434</td><td>13.520</td></tr>
<tr><td>$c$</td><td>7.105</td><td>7.166</td></tr>
<tr><td>Cell volume [Å³]</td><td></td><td>669.8</td><td>687.1</td></tr>
<tr><td rowspan="7">Atom positions</td><td>Hf1</td><td>$x=0.1811$, $y=0.2500$, $z=0.0021$</td><td>$x=0.1811$, $y=0.2500$, $z=0.0020$</td></tr>
<tr><td>Hf2</td><td>$x=0.1457$, $y=0.6239$, $z=0.1671$</td><td>$x=0.1456$, $y=0.6242$, $z=0.1670$</td></tr>
<tr><td>Hf3</td><td>$x=0.0141$, $y=0.0946$, $z=0.3229$</td><td>$x=0.0142$, $y=0.0946$, $z=0.3231$</td></tr>
<tr><td>Ge1</td><td>$x=0.0534$, $y=0.2500$, $z=0.6110$</td><td>$x=0.0527$, $y=0.2500$, $z=0.6116$</td></tr>
<tr><td>Ge2</td><td>$x=0.3212$, $y=0.2500$, $z=0.3540$</td><td>$x=0.3215$, $y=0.2500$, $z=0.3530$</td></tr>
<tr><td>Ge3</td><td>$x=0.3039$, $y=0.5407$, $z=0.4648$</td><td>$x=0.3033$, $y=0.5406$, $z=0.4652$</td></tr>
</tbody></table>

The calculated atom positions (in fractional coordinates) were used as the starting positions for all calculations.

larger than the experimental values, which is common for calculations using gradient corrected functionals (PBE) [18]. It is not possible to compare the calculated structures of the other end members in the same direct way, as they are hypothetical, strictly ordered compounds. However, it is possible to compare the calculated structural data with those found in the X-ray investigation of $\text{Hf}_{5-x}\text{Nb}_x\text{Ge}_4$ [1]. Since the substitution in this solid solution phase is almost stepwise, the hypothetical end members (Nb:Hf:Ge) and (Nb:Nb:Hf:Ge) are roughly realized in the solid solution. Thus, based on the experimental order of substitution, the models for (Hf:Hf:Hf:Ge), (Nb:Hf:Hf:Ge), (Nb:Nb:Hf:Ge) and (Nb:Nb:Nb:Ge) were chosen for the comparison (see Table 6). Although the lattice parameters (Fig. 4) are generally larger than the experimental ones, the general trend is well reproduced by the model compounds. The same is true for the unit cell volume. Fig. 5 presents lattice parameter ratios as a function of the niobium content. It is remarkable that the experimental trends are very well reproduced by these four end members chosen for modelling. One can therefore conclude that the non-linear behaviour of the lattice parameters in the solid solution $\text{Hf}_{5-x}\text{Nb}_x\text{Ge}_4$ is strongly determined by the stepwise substitution at the three different metal positions and that these trends are very well predicted by the ab initio lattice parameters obtained for hypothetical ordered compounds.

<table><caption>Table 6 Calculated structural data for the most stable end members</caption>
<tbody><tr><th>Compound</th><th></th><th></th><td>(Nb:Hf:Hf:Ge)</td><td>(Nb:Nb:Hf:Ge)</td><td>(Nb:Nb:Nb:Ge)</td></tr>
<tr><td rowspan="3">Lattice parameters [Å]</td><td>$a$</td><td></td><td>6.973</td><td>6.816</td><td>6.754</td></tr>
<tr><td>$b$</td><td></td><td>13.506</td><td>13.230</td><td>13.197</td></tr>
<tr><td>$c$</td><td></td><td>7.082</td><td>6.960</td><td>6.829</td></tr>
<tr><td>Cell volume [Å³]</td><td></td><td></td><td>666.9</td><td>627.7</td><td>608.7</td></tr>
<tr><td rowspan="18">Atom positions</td><td rowspan="3">Hf1</td><td>$x$</td><td>0.1762</td><td>0.1663</td><td>0.1719</td></tr>
<tr><td>$y$</td><td>0.2500</td><td>0.2500</td><td>0.2500</td></tr>
<tr><td>$z$</td><td>0.9970</td><td>0.9939</td><td>0.9926</td></tr>
<tr><td rowspan="3">Hf2</td><td>$x$</td><td>0.1508</td><td>0.1583</td><td>0.1537</td></tr>
<tr><td>$y$</td><td>0.6247</td><td>0.6242</td><td>0.6243</td></tr>
<tr><td>$z$</td><td>0.1695</td><td>0.1653</td><td>0.1644</td></tr>
<tr><td rowspan="3">Hf3</td><td>$x$</td><td>0.0164</td><td>0.0128</td><td>0.0192</td></tr>
<tr><td>$y$</td><td>0.0951</td><td>0.0907</td><td>0.0862</td></tr>
<tr><td>$z$</td><td>0.3230</td><td>0.3254</td><td>0.3258</td></tr>
<tr><td rowspan="3">Ge1</td><td>$x$</td><td>0.0473</td><td>0.0395</td><td>0.0462</td></tr>
<tr><td>$y$</td><td>0.2500</td><td>0.2500</td><td>0.2500</td></tr>
<tr><td>$z$</td><td>0.6076</td><td>0.6112</td><td>0.6042</td></tr>
<tr><td rowspan="3">Ge2</td><td>$x$</td><td>0.3179</td><td>0.3094</td><td>0.3198</td></tr>
<tr><td>$y$</td><td>0.2500</td><td>0.2500</td><td>0.2500</td></tr>
<tr><td>$z$</td><td>0.3501</td><td>0.3477</td><td>0.3393</td></tr>
<tr><td rowspan="3">Ge3</td><td>$x$</td><td>0.3076</td><td>0.3158</td><td>0.3109</td></tr>
<tr><td>$y$</td><td>0.5403</td><td>0.5405</td><td>0.5412</td></tr>
<tr><td>$z$</td><td>0.4687</td><td>0.4619</td><td>0.4654</td></tr>
</tbody></table>

![](./images/812017559795662848_4.jpg)

Fig. 4. Variation of lattice parameters (above) and unit cell volume (below) of $\text{Hf}_{5-x}\text{Nb}_x\text{Ge}_4$ and most stable end members. Experimental values are taken from Ref. [1].

![](./images/812017559795662848_5.jpg)

Fig. 5. Variation of lattice parameter ratios of $Hf_{5-x}Nb_xGe_4$ and most stable
end members. Experimental values are taken from Ref. [1].

Finally, the relaxed structures of the (Hf:Nb:Hf:Ge) and
(Hf:Hf:Nb:Ge) end members should be discussed (Table 7).
The equal substitutional energies might suggest that the
two relaxed structures are identical. Actually, the computed
lattice parameters are almost identical for both models but
the internal atom positions differ. While the atom positions of
(Hf:Nb:Hf:Ge) could be easily related to the original positions
of the $Hf_5Ge_4$ structure, the structure of (Hf:Hf:Nb:Ge) is quite
different. A detailed analysis of the coordination spheres and

<table><tbody><tr><td colspan="4">Table 7</td></tr><tr><td colspan="4">Calculated structural data for the (Hf:Nb:Hf:Ge) and (Hf:Hf:Nb:Ge) end members</td></tr><tr><td>Compound</td><td></td><td>(Hf:Nb:Hf:Ge)</td><td>(Hf:Hf:Nb:Ge)</td></tr><tr><td rowspan="3">Lattice parameters [Å]</td><td>$a$</td><td>6.907</td><td>6.906</td></tr><tr><td>$b$</td><td>13.338</td><td>13.332</td></tr><tr><td>$c$</td><td>7.024</td><td>7.029</td></tr><tr><td>Cell volume [Å³]</td><td></td><td>647.1</td><td>647.1</td></tr><tr><td rowspan="3">Atom positions</td><td rowspan="3">Hf1</td><td>0.1695</td><td>0.3296</td></tr><tr><td>0.2500</td><td>0.2500</td></tr><tr><td>0.9939</td><td>0.0058</td></tr><tr><td rowspan="9"></td><td rowspan="3">Hf2</td><td>0.1581</td><td>0.0126</td></tr><tr><td>0.6229</td><td>0.5930</td></tr><tr><td>0.1715</td><td>0.1734</td></tr><tr><td rowspan="3">Hf3</td><td>0.0124</td><td>0.1572</td></tr><tr><td>0.0929</td><td>0.1230</td></tr><tr><td>0.3265</td><td>0.3286</td></tr><tr><td rowspan="3">Ge1</td><td>0.0450</td><td>0.1907</td></tr><tr><td>0.2500</td><td>0.2500</td></tr><tr><td>0.6151</td><td>0.6456</td></tr><tr><td rowspan="6"></td><td rowspan="3">Ge2</td><td>0.3087</td><td>0.4545</td></tr><tr><td>0.2500</td><td>0.2500</td></tr><tr><td>0.3545</td><td>0.3851</td></tr><tr><td rowspan="3">Ge3</td><td>0.3165</td><td>0.1838</td></tr><tr><td>0.5386</td><td>0.5383</td></tr><tr><td>0.4648</td><td>0.5356</td></tr></tbody></table>

coordination numbers reveals that the relaxed (Hf:Hf:Nb:Ge)
is exactly equivalent to the (Hf:Nb:Hf:Ge) structure, if the or-
igin of the former unit cell is shifted such that the niobium
atoms are placed at the positions Hf2 of (Hf:Nb:Hf:Ge). In
this case, the Hf2 positions in (Hf:Hf:Nb:Ge) correspond to
the Hf3 positions in (Hf:Nb:Hf:Ge). A similar "exchange"
of the germanium atoms between the sites Ge1 and Ge2 was
also observed. This implies that the (Hf:Hf:Nb:Ge) structure
can be transformed into (Hf:Nb:Hf:Ge). The large atom migra-
tion observed during the relaxation of (Hf:Hf:Nb:Ge) confirms
the instability of this end member.

### 4. Summary

Niobium site preferences in the solid solution $Hf_{5-x}Nb_xGe_4$ can be well modelled using the compound energy
formalism model based on energies derived directly from
ab initio ground state energy calculations. For the compounds
investigated in this paper, the vibrational contributions to
the energies can be neglected for the modelling of the site
fractions. Moreover, the equilibrium structures of the most
stable end members obtained from these calculations may
be used for a qualitative modelling of the lattice parameter
changes. Further simplifications can be achieved by using
only the energies of the three end members (Nb:Hf:Hf:Ge),
(Hf:Nb:Hf:Ge) and (Hf:Hf:Nb:Ge) in an unrelaxed state and
using their superposition for modelling the other end member
energies. This simplification did not reduce the quality of the
site preference modelling, while it dramatically reduced the
computational costs required for the calculations. It will be
interesting to apply the simplified approach discussed here
to other, more complicated structures, in order to test it on
a broader basis.

### Acknowledgments

Financial support from the Austrian Science Fund (FWF) under the project number FWF P 16946, from the Ministry of Education of the Czech Republic under the project COST 531.002 and from the Scientific-Technical Cooperation Austria-Czech Republic "Kontakt", Projekt No. 2004/03, is gratefully acknowledged. The authors would like to thank Prof. Jan Vřešťál (Masaryk University in Brno) for helpful discussion and comments.

### References

[1] K.W. Richter, R. Picha, H. Ipser, H.F. Franzen, Solid State Sci. 5 (2003) 653.
[2] J.T. Zhao, E. Parthé, J. Less-Common Met. 162 (1990) L27.
[3] B. Sundman, J. Ågren, J. Phys. Chem. Solids 42 (1981) 297.
[4] P. Villars, L.D. Calvert (Eds.), Pearson's Handbook of Crystallographic Data for Intermetallic Phases, second ed., ASM, 1991.

[5] Yu.D. Seropegin, V.V. Tabachenko, M.G. Mys'kiv, Sov. Phys. Crystal- logr. 29 (1984) 95.
[6] K.W. Richter, H.F. Franzen, J. Solid State Chem. 150 (2000) 347.
[7] J. Le Roy, J.-M. Moreau, D. Paccard, E. Parthé, Acta Crystallogr. B 34 (1978) 3315.
[8] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558.
[9] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15.
[10] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes, Cambridge University Press, New York, 1986.
[11] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[12] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.
[13] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. B 46 (1992) 6671.
[14] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[15] P.E. Blöchl, O. Jepsen, O.K. Anderson, Phys. Rev. B 49 (1994) 16223.
[16] Thermo-Calc, version P, Software for Thermodynamic Calculations in Multi-component Systems, Thermo-Calc AB, Stockholm, Sweden, 2003.
[17] A. Dinsdale, Calphad 15 (1991) 317.
[18] J. Paier, M. Marsman, K. Hummer, G. Kresse, I.C. Gerber, J.G. Ángyán, J. Chem. Phys. 124 (2006) 154709.