# Theoretical calculations on the structural, electronic and optical properties of bulk silver nitrides

Mohammed S. H. Suleiman$^{1,2,*}$ and Daniel P. Joubert$^{1,\dagger}$

$^{1}$School of Physics, University of the Witwatersrand, Johannesburg, South Africa.
$^{2}$Department of Physics, Sudan University of Science and Technology, Khartoum, Sudan.
(Dated: January 1, 2013)

We present a first-principles investigation of structural, electronic and optical properties of bulk crystalline $\text{Ag}_3\text{N}$, $\text{AgN}$ and $\text{AgN}_2$ based on density functional theory (DFT) and many-body perturbation theory. The equation of state (EOS), energy-optimized geometries, cohesive and formation energies, and bulk modulus and its pressure derivative of these three stoichiometries in a set of twenty different structures have been studied. Band diagrams and total and orbital-resolved density of states (DOS) of the most stable phases have been carefully examined. Within the random-phase approximation (RPA) to the dielectric tensor, the single-particle spectra of the quasi electrons and quasi holes were obtained via the GW approximation to the self-energy operator, and optical spectra were calculated. The results obtained were compared with experiment and with previously performed calculations.

## CONTENTS

| I. Introduction | 1 |
| --- | --- |
| II. Calculation Methods | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;A. Stoichiometries and Crystal Structures | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;B. Electronic Relaxation Details | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;C. Geometry Relaxation and EOS | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;D. Formation Energy | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;E. GWA Calculations and Optical Properties | 3 |
| III. Results and Discussion | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;A. EOS and Relative Stabilities | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;B. Volume per Atom and Lattice Parameters | 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;C. Bulk Modulus and its Pressure Derivative | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;D. Formation Energies | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;E. Electronic Properties | 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;F. Optical Properties | 12 |
| IV. Conclusions | 12 |
| Acknowledgments | 12 |
| References | 13 |

## I. INTRODUCTION

It is well-known now that late transition-metal nitrides (TMNs) usually possess interesting properties leading to a variety of potential technological applications$^{1-3}$. Hence, a significant number of quantum mechanical $ab$ $initio$ calculations of the structural and physical properties of this family of materials have appeared in the literature.

Since Juza and Hahn$^{4}$ succeeded to synthesize $\text{Cu}_3\text{N}$ in 1939, copper nitrides have been produced through various techniques and their properties and applications have been the subject of many theoretical and experimental published works$^{5}$. Due to its early discovery, copper nitride may now be considered as the most investigated among the late TMNs$^{6}$.

On the other hand, the nitride of silver, the next element to copper in group 11 of the periodic table, has been known for more than two centuries$^{7,8}$. However, despite its earlier discovery, silver nitride may be the least theoretically studied solid in the late TMNs family. Experimental efforts to investigate structural$^{8,9}$, electronic$^{8}$ and formation$^{7,9-11}$ properties of silver nitrides have been made by some researchers.

In 1949, Hahn and Gilbert$^{9}$ carried out the first$^{8}$ structural study on the reported stoichiometry, $\text{Ag}_3\text{N}$. They claimed an fcc structure with $a = 4.369$ $\mathring{\text{A}}$ and $Z = 4/3$ (i.e. 4 Ag atoms in the unit cell). A long time later in 1982, Haisa$^{12}$ suggested that the Ag atoms are located at the corners and face centers of the unit cell, while the N atoms, which may be statistically distributed in the octahedral interstices, were given no definite positions$^{12}$.

According to the calculated N radius, $\text{Ag}_3\text{N}$ can be described as an ionic compound, and recent $ab$ $initio$ calculations on the proposed structure revealed insulating characteristics with a fundamental band gap close to $1.35\ eV$. On the other hand, due to the similar lattice of the parent Ag and the easily separated N as $\text{N}_2$, it can also be argued that this compound is a metal, supporting its black color$^{8}$.

Under ordinary conditions$^{7}$, it was found that silver can form $\text{Ag}_3\text{N}^{13}$ from ammoniacal solutions of silver oxide$^{7,8}$. The black metallic-looking solid outcome, $\text{Ag}_3\text{N}$, is an extremely sensitive explosive compound$^{7,14}$. It may explode due to the slightest touch, even from the impact of a falling water droplet$^{14}$, but it is relatively easy to handle under water or ethanol$^{8}$. The explosive power is due to the energy released during the decomposition reaction:
$$2\text{Ag}_3\text{N} \longrightarrow 6\text{Ag} + \text{N}_2. \tag{1}$$

Even in storage at room temperature, this solid compound decomposes slowly according to Eq. 1 above$^{8,14}$.

From a thermochemical point of view, it was found that there is no stable intermediate stage in this decomposi- tion, but there may be a metastable intermediate species (phase) with a remarkably low decomposition rate $^{7}$. At this point, it may be worth mentioning that the ther- mochemistry of silver nitride systems is not fully docu- mented in standard handbook data $^{7}$.

In their 1991 work, Shanley and Ennis $^{7}$ stated: "Many of the samples ... did not survive the minimum han- dling required to move them, container and all, to the X-ray stage. ... More vigorously explosive samples prop- agated throughout their mass leaving no visible residue. Even among supersensitive materials, silver nitride is a striking example of a compound "teetering on the edge of existence". Under the circumstances, we did not suc- ceed in developing data on the proportion of silver nitride required for explosive behavior in these mixtures."

Thus, beside the potential hazard to lab workers due to its sensitive explosive behavior, characterization of silver nitride is hindered by its extremely unstable (endother- mic) nature $^{7,8}$, and we are presented with an incomplete picture of structural, electronic and optical properties of this material. Surprisingly, this lack of detailed knowl- edge of many physical properties of silver nitride stimu- lated only very few published ab initio studies.

In the present work, first-principles calculations were carried out to investigate the lattice parameters, equation of state, relative stabilities, phase transitions, electronic and optical properties of silver nitrides in three different chemical formulae and in various crystal structures. Cal- culation methods are described in Sec. II. In Sec. III, results are presented, discussed and compared with ex- periment and with previous calculations. The article is concluded with some remarks in Sec. IV.

## II. CALCULATION METHODS
### A. Stoichiometries and Crystal Structures
To the best of our knowledge, the only experimen- tally reported stoichiometries of Ag-N compounds are $Ag_{3}N^{7}$ and $AgN_{3}^{7}$. However, previous ab initio stud ies on Ag-N compounds considered $Ag_{4}N^{8}$, $Ag_{3}N^{8,15}$, $Ag_{2}N^{15}$, $AgN^{15,16}$ and $AgN_{2}^{15,17}$ in some cubic struc tures only. Consideration of stoichiometries other than the reported ones is probably due to the fact that many transition metals nitrides (TMs) are known to form more than one nitride $^{18}$. Hence, our interest in investigating AgN and $AgN_{2}$ is based on this fact.

For $Ag_{3}N$, we consider the following seven structures: the face-centered cubic structure of $AlFe_{3}$ (D0₃), the sim ple cubic structure of $Cr_{3}Si$ (A15), the simple cubic struc ture of the anti-$ReO_{3}$ (D0₉), the simple cubic structure of $Ag_{3}Au$ (L1₂), the body-centered cubic structure of $CoAs_{3}$ (D0₂), the hexagonal structure of $\epsilon$-$Fe_{3}N$, and the trigonal (rhombohedric) structure of $RhF_{3}$.

For AgN, the following four structures were considered: the face-centered cubic structure of NaCl (B1), the sim- ple cubic structure of CsCl (B2), the face-centered cubic structure of ZnS zincblende (B3), the hexagonal structure of NiAs (B8₁), the hexagonal structure of BN (Bₖ), the hexagonal structure of WC (Bₕ), the hexagonal structure of ZnS wurtzite (B4), the simple tetragonal structure of PtS cooperite (B17), and the face-centered orthorhombic structure of TlF (B24).

$AgN_{2}$ was studied in the following nine structures: the face-centered cubic structure of $CaF_{2}$ fluorite (C1), the simple cubic structure of $FeS_{2}$ pyrite (C2), the simple orthorhombic structure of $FeS_{2}$ marcasite (C18) and the simple monoclinic structure of $CoSb_{2}$ (CoSb₂).

### B. Electronic Relaxation Details
In this work, electronic structure spin density func- tional theory (SDFT) $^{19,20}$ calculations as implemented in the VASP code $^{21-26}$ have been employed. To self consistently solve the Kohn-Sham (KS) equations $^{27}$

$$
\left\{-\frac{\hbar^{2}}{2m_{e}}\nabla^{2}+\int d\mathbf{r}'\frac{n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}+V_{ext}(\mathbf{r})+V_{XC}^{\sigma,\mathbf{k}}[n(\mathbf{r})]\right\}\psi_{i}^{\sigma,\mathbf{k}}(\mathbf{r})=\epsilon_{i}^{\sigma,\mathbf{k}}\psi_{i}^{\sigma,\mathbf{k}}(\mathbf{r}), \tag{2}
$$

where $i$, $\mathbf{k}$ and $\sigma$ are the band, k-point and spin in- dices, receptively, VASP expands the pseudo part of the KS one-particle spin orbitals $\psi_{i}^{\sigma,\mathbf{k}}(\mathbf{r})$ on a basis set of plane-waves (PWs). Only those PWs with cut-off en- ergy $E_{cut}\leq 600$ eV have been included. The Brillouin zones were sampled using $\Gamma$-centered Monkhorst-Pack $^{28}$ $17\times 17\times 17$ meshes. Any increase in the $E_{cut}$ value or in the density of the k-mesh produces a change in the total energy less than 3 meV/atom. For static calcula- tions, partial occupancies were set using the tetrahedron method with Blöchl corrections $^{29-31}$, while the smearing method of Methfessel-Paxton (MP) $^{32}$ was used in the ionic relaxation, and Fermi surface of the metallic phases has been carefully treated. The Perdew-Burke-Ernzerhof (PBE) parametrization $^{33-35}$ of the generalized gradi- ent approximation (GGA) $^{36-38}$ was employed for the exchange-correlation potentials $V_{XC}^{\sigma,\mathbf{k}}[n(\mathbf{r})]$. The implemented projector augmented wave (PAW) method $^{26,39}$ was used to describe the core-valence interactions $V_{ext}(\mathbf{r})$, where the $4d^{10}5s^{1}$ electrons of Ag and the $2s^{2}2p^{3}$ elec- trons of N are treated explicitly as valence electrons. While for these valence electrons only scalar kinematic relativistic effects are incorporated, the PAW potential treats the core electrons in a fully relativistic fashion $^{25}$. No spin-orbit interaction of the valence electrons has been considered.

### C. Geometry Relaxation and EOS

At a set of externally imposed lattice constants, ions with free internal parameters were relaxed until all force components on each ion were less than $0.01\ eV/\mathring{A}$. This is done following the implemented conjugate-gradient (CG) algorithm. After each ion relaxation step, static total energy calculation with the tetrahedron method was performed, and the cohesive energy per atom $E_{coh}$ was calculated from

$$
E_{coh}^{\mathrm{Ag}_{m} \mathrm{N}_{n}}=\frac{E_{\text {solid }}^{\mathrm{Ag}_{m} \mathrm{N}_{n}}-Z \times\left(m E_{\text {atom }}^{\mathrm{Ag}}+n E_{\text {atom }}^{\mathrm{N}}\right)}{Z \times(m+n)}, \quad(3)
$$

where $Z$ is the number of $\mathrm{Ag}_{m} \mathrm{N}_{n}$ formulas per unit cell, $E_{\text {atom }}^{\mathrm{Ag}}$ and $E_{\text {atom }}^{\mathrm{N}}$ are the energies of the isolated nonspherical spin-polarized atoms, and $m, n=1,2$ or 3 are the stoichiometric weights. The obtained $E_{coh}$ as a function of volume $V$ per atom were then fitted to a BirchMurnaghan 3rd-order equation of state (EOS) $^{40}$ and the equilibrium volume $V_{0}$, the equilibrium cohesive energy $E_{0}$, the equilibrium bulk modulus

$$
B_{0}=-\left.V \frac{\partial P}{\partial V}\right|_{V=V_{0}}=-\left.V \frac{\partial^{2} E}{\partial V^{2}}\right|_{V=V_{0}} \quad(4)
$$

and its pressure derivative

$$
B_{0}^{\prime}=\left.\frac{\partial B}{\partial P}\right|_{P=0}=\left.\frac{1}{B_{0}}\left(V \frac{\partial}{\partial V}\left(V \frac{\partial^{2} E}{\partial V^{2}}\right)\right)\right|_{V=V_{0}} \quad(5)
$$

were determined.

### D. Formation Energy

Beside the cohesive energy, another measure of relative stability is the formation energy $E_{f}$. Assuming that silver nitrides $\mathrm{Ag}_{m} \mathrm{N}_{n}$ result from the interaction between the $\mathrm{N}_{2}$ gas and the solid $\mathrm{Ag}(\mathrm{A} 1)$ via the reaction (compare with Eq. 1)

$$
m \mathrm{Ag}^{\text {solid }}+\frac{n}{2} \mathrm{~N}_{2}^{\text {gas }} \rightleftharpoons \mathrm{Ag}_{m} \mathrm{~N}_{n}^{\text {solid }}, \quad(6)
$$

$E_{f}$ can be given by

$$
\begin{aligned}
E_{f}\left(\mathrm{Ag}_{m} \mathrm{~N}_{n}^{\text {solid }}\right) & =E_{\mathrm{coh}}\left(\mathrm{Ag}_{m} \mathrm{~N}_{n}^{\text {solid }}\right) \\
& -\frac{m E_{\mathrm{coh}}\left(\mathrm{Ag}^{\text {solid }}\right)+\frac{n}{2} E_{\mathrm{coh}}\left(\mathrm{N}_{2}^{\text {gas }}\right)}{m+n}. \quad(7)
\end{aligned}
$$

Here $m, n=1,2,3$ are the stoichiometric weights and $E_{\mathrm{coh}}\left(\mathrm{Ag}_{m} \mathrm{~N}_{n}^{\text {solid }}\right)$ is the cohesive energy per atom as in Eq. 3. The cohesive energy $E_{\mathrm{coh}}\left(\mathrm{Ag}^{\text {solid }}\right)$ and other equilibrium properties of the elemental metallic silver are given in Table I. The cohesive energy of the diatomic nitrogen $\left(E_{\mathrm{coh}}\left(\mathrm{N}_{2}^{\text {gas }}\right)\right)$ was found to be $-5.196\ eV/$ atom corresponding to an equilibrium $\mathrm{N}-\mathrm{N}$ bond length of $1.113\ \mathring{A}$ (For more details, see Ref. 5).

### E. GWA Calculations and Optical Properties

Although a qualitative agreement between DFTcalculated optical properties and experiment is possible, accurate quantitative description requires treatments beyond the level of $\mathrm{DFT}^{41}$. Another approach provided by many-body perturbation theory (MBPT) leads to a system of quasi-particle (QP) equations, which can be written for a periodic crystal as $^{42-44}$

$$
\begin{gathered}
\left\{-\frac{\hbar^{2}}{2 m} \nabla^{2}+\int d \mathbf{r}^{\prime} \frac{n\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}+V_{\text {ext }}(\mathbf{r})\right\} \psi_{i, \mathbf{k}}^{Q P}(\mathbf{r}) \\
+\int d \mathbf{r}^{\prime} \Sigma\left(\mathbf{r}, \mathbf{r}^{\prime} ; \epsilon_{i, \mathbf{k}}^{Q P}\right) \psi_{i, \mathbf{k}}^{Q P}\left(\mathbf{r}^{\prime}\right)=\epsilon_{i, \mathbf{k}}^{Q P} \psi_{i, \mathbf{k}}^{Q P}(\mathbf{r}).
\end{gathered}
$$

Practically, the wave functions $\psi_{i, \mathbf{k}}^{Q P}(\mathbf{r})$ are taken from the DFT calculations. However, in consideration of computational cost, we used a less dense mesh of $\mathbf{k}$-points $(10 \times 10 \times 10)$. The term $\Sigma\left(\mathbf{r}, \mathbf{r}^{\prime} ; \epsilon_{i, \mathbf{k}}^{Q P}\right)$ is the selfenergy which contains all the exchange and correlation effects, static and dynamic, including those neglected in our DFT-GGA reference system. In the so-called $G W$ approximation $^{45}, \Sigma$ is given in terms of the Green's function $G$ as

$$
\Sigma_{G W}=j \int d \epsilon^{\prime} G\left(\mathbf{r}, \mathbf{r}^{\prime} ; \epsilon, \epsilon^{\prime}\right) W\left(\mathbf{r}, \mathbf{r}^{\prime} ; \epsilon\right), \quad(9)
$$

where the dynamically (frequency dependent) screened Coulomb interaction $W$ is related to the bare Coulomb interaction $v$ through

$$
W\left(\mathbf{r}, \mathbf{r}^{\prime} ; \epsilon\right)=j \int d \mathbf{r}_{1} \varepsilon^{-1}\left(\mathbf{r}, \mathbf{r}_{1} ; \epsilon\right) v\left(\mathbf{r}_{1}, \mathbf{r}^{\prime}\right), \quad(10)
$$

with $\varepsilon$, the dielectric matrix, calculated within the so-called random phase approximation (RPA). We followed the $G W_{0}$ self-consistent routine on $G$, in which the QP eigenvalues

$$
\epsilon_{i, \mathbf{k}}^{Q P}=\operatorname{Re}\left(\left\langle\psi_{i, \mathbf{k}}^{Q P}\left|H_{\mathrm{KS}}-V_{X C}+\Sigma_{G W_{0}}\right| \psi_{i, \mathbf{k}}^{Q P}\right\rangle\right)(11)
$$

are updated in the calculations of $G$, while $W$ is kept at the DFT-RPA level. Four updates were performed, and after the final iteration in $G, \varepsilon$ is recalculated within the RPA using the updated QP eigenvalues ${ }^{43,44,46}$. From the real $\varepsilon_{\mathrm{re}}(\omega)$ and the imaginary $\varepsilon_{\mathrm{im}}(\omega)$ parts of this frequency-dependent microscopic dielectric tensor, one can derive all the other frequency-dependent dielectric response functions, such as reflectivity $R(\omega)$, transmittivity $T(\omega)=1-R(\omega)$, refractive index $n(\omega)$, extinction

coefficient $\kappa(\omega)$, and absorption coefficient $\alpha(\omega)^{47-49}$:

$$
R(\omega)=\left|\frac{\left[\varepsilon_{\mathrm{re}}(\omega)+j \varepsilon_{\mathrm{im}}(\omega)\right]^{\frac{1}{2}}-1}{\left[\varepsilon_{\mathrm{re}}(\omega)+j \varepsilon_{\mathrm{im}}(\omega)\right]^{\frac{1}{2}}+1}\right|^{2}
\tag{12}
$$

$$
n(\omega)=\frac{1}{\sqrt{2}}\left(\left[\varepsilon_{\mathrm{re}}^{2}(\omega)+\varepsilon_{\mathrm{im}}^{2}(\omega)\right]^{\frac{1}{2}}+\varepsilon_{\mathrm{re}}(\omega)\right)^{\frac{1}{2}}
\tag{13}
$$

$$
\kappa(\omega)=\frac{1}{\sqrt{2}}\left(\left[\varepsilon_{\mathrm{re}}^{2}(\omega)+\varepsilon_{\mathrm{im}}^{2}(\omega)\right]^{\frac{1}{2}}-\varepsilon_{\mathrm{re}}(\omega)\right)^{\frac{1}{2}}
\tag{14}
$$

$$
\alpha(\omega)=\sqrt{2} \omega\left(\left[\varepsilon_{\mathrm{re}}^{2}(\omega)+\varepsilon_{\mathrm{im}}^{2}(\omega)\right]^{\frac{1}{2}}-\varepsilon_{\mathrm{re}}(\omega)\right)^{\frac{1}{2}}
\tag{15}
$$

## III. RESULTS AND DISCUSSION

The energy-volume equation of state (EOS) for the different structures of $\mathrm{Ag}_{3} \mathrm{~N}, \mathrm{AgN}_{2}$ and $\mathrm{AgN}$ are depicted in Figs. 1, 2 and 3, respectively. The corresponding calculated equilibrium properties are given in Table I. In this table, we ordered the studied phases according to the increase in the nitrogen content; then within each series, structures are ordered in the direction of decreasing structural symmetry. For the sake of comparison, we also presented results from experiment and from previous $a b$ initio calculations; and, whenever appropriate, the calculation method and the $X C$ functional are also given in footnotes of the Table.

The calculated equilibrium properties: cohesive energies, formation energies, volume per atom, volume per $\mathrm{Ag}$ atom, and bulk modulus and its pressure derivative which are given Table I, are visualized in Fig. 4. This kind of visualization allows us to study the effect of nitridation on the parent $\mathrm{Ag}(\mathrm{A} 1)$, since all quantities in this figure are given relative to the corresponding ones of the elemental $\mathrm{Ag}(\mathrm{A} 1)$ given in the first row of Table I. Moreover, one can easily compare the properties of these phases relative to each other.

### A. EOS and Relative Stabilities

Considering $E_{\text {coh }}$ in the $\mathrm{Ag}_{3} \mathrm{~N}$ series, Fig. 1 shows clearly that the $E(V)$ relations of $\mathrm{Ag}_{3} \mathrm{~N}$ in $\mathrm{D} 0_{9}, \mathrm{D} 0_{2}$ and $\mathrm{RhF}_{3}$ phases are almost identical, corresponding to equilibrium cohesive energy (Table I) of $-2.513,-2.514$ and $-2.514 \mathrm{eV} /$ atom, respectively. This behavior in the EOS could be traced back to the structural relationships between these three structures, since both $\mathrm{D0}_{2}$ and $\mathrm{RhF}_{3}$ can simply be derived from the more symmetric $\mathrm{D0}_{9}$ (see Ref. 5 and references therein). These structural relations may reflect in the EOS's and in other physical properties, and the three phases may co-exist during the $\mathrm{Ag}_{3} \mathrm{~N}$ synthesis process. Relative to the elemental $\mathrm{Ag}$, these three phases tend not to change the $E_{\text {coh }}$ (Fig. 4), lowering it only by $\sim 0.03 \mathrm{eV} /$ atom, as can been seen from Table I. It may be worth to mention here that the simple

![](./images/867748054407578313_1.jpg)

FIG. 1. (Color online.) Cohesive energy $E_{coh}(eV /$ atom $)$ versus atomic volume $V(\AA^{3} /$ atom $)$ for $Ag_{3} ~N$ in seven different structural phases.

![](./images/867748054407578313_2.jpg)

FIG. 2. (Color online.) Cohesive energy $E_{coh}(eV /$ atom $)$ versus atomic volume $V(\AA^{3} /$ atom $)$ for $AgN$ in nine different structural phases.

![](./images/867748054407578313_3.jpg)

FIG. 3. (Color online.) Cohesive energy $E_{c o h}(eV /$ atom $)$ versus atomic volume $V(\AA^{3} /$ atom $)$ for $AgN_{2}$ in four different structural phases.

<table><caption>TABLE I. Calculated and experimental zero-pressure properties of the twenty studied phases of $\text{Ag}_3\text{N}$, $\text{AgN}$ and $\text{AgN}_2$: Lattice constants $(a(\text{Å})$, $b(\text{Å})$, $c(\text{Å})$, $\alpha(^\circ)$ and $\beta(^\circ))$, equilibrium atomic volume $V_0(\text{Å}^3/\text{atom})$, cohesive energy $E_{\text{coh}}(eV/\text{atom})$, bulk modulus $B_0(GPa)$ and its pressure derivative $B_0'$, and formation energy $E_f(eV/\text{atom})$. The presented data are of the current work $(Pres.)$, experimentally reported $(Expt.)$ and of previous calculations $(Comp.)$.</caption>
<tbody>
<tr>
<td>Structure</td>
<td></td>
<td>$a(\text{Å})$</td>
<td>$b(\text{Å})$</td>
<td>$c(\text{Å})$</td>
<td>$\alpha(^\circ)$ or $\beta(^\circ)$</td>
<td>$V_0(\text{Å}^3/\text{atom})$</td>
<td>$E_{\text{coh}}(eV/\text{atom})$</td>
<td>$B_0(GPa)$</td>
<td>$B_0'$</td>
<td>$E_f(eV/\text{atom})$</td>
</tr>
<tr>
<td colspan="11">$\text{Ag}$</td>
</tr>
<tr>
<td rowspan="3">A1</td>
<td>Pres.</td>
<td>4.164</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>18.06</td>
<td>$-2.484$</td>
<td>88.188</td>
<td>5.793</td>
<td></td>
</tr>
<tr>
<td>Expt.</td>
<td>$(4.08570\pm0.00018)^\text{a}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td>$-2.95^\text{b}$</td>
<td>$100.7^\text{b}$, $101^\text{c}$</td>
<td>$6.12^\text{d}$</td>
<td></td>
</tr>
<tr>
<td>Comp.</td>
<td>$4.01^\text{f}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td>$-3.59^\text{g}$, $-2.66^\text{h}$, $142^\text{f}$<br>$-2.67^\text{i}$</td>
<td></td>
<td>$5.00^\text{l}$, $5.70^\text{j}$, $5.97^\text{k}$</td>
<td></td>
</tr>
<tr>
<td colspan="11">$\text{Ag}_3\text{N}$</td>
</tr>
<tr>
<td>D03</td>
<td>Pres.</td>
<td>6.322</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>15.79</td>
<td>$-2.055$</td>
<td>98.356</td>
<td>5.457</td>
<td>1.107</td>
</tr>
<tr>
<td>A15</td>
<td>Pres.</td>
<td>5.065</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>16.24</td>
<td>$-1.976$</td>
<td>92.280</td>
<td>5.470</td>
<td>1.186</td>
</tr>
<tr>
<td rowspan="2">D09</td>
<td>Pres.</td>
<td>4.328</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>20.27</td>
<td>$-2.513$</td>
<td>71.980</td>
<td>5.386</td>
<td>0.649</td>
</tr>
<tr>
<td>Comp.</td>
<td>$3.995^\text{q}$, $4.169^\text{r}$, $4.292^\text{s}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$95.7^\text{r}$, $87.1^\text{s}$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>L12</td>
<td>Pres.</td>
<td>3.972</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>15.67</td>
<td>$-2.081$</td>
<td>100.743</td>
<td>5.530</td>
<td>1.081</td>
</tr>
<tr>
<td>D03</td>
<td>Pres.</td>
<td>8.662</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>20.31</td>
<td>$-2.514$</td>
<td>72.230</td>
<td>5.335</td>
<td>0.648</td>
</tr>
<tr>
<td>c-Fe3N</td>
<td>Pres.</td>
<td>5.967</td>
<td>–</td>
<td>5.560</td>
<td>–</td>
<td>21.43</td>
<td>$-2.469$</td>
<td>64.737</td>
<td>2.335</td>
<td>0.692</td>
</tr>
<tr>
<td>RhF3</td>
<td>Pres.</td>
<td>6.126</td>
<td>–</td>
<td>–</td>
<td>$\alpha=59.989$</td>
<td>20.31</td>
<td>$-2.514$</td>
<td>72.237</td>
<td>5.396</td>
<td>0.648</td>
</tr>
<tr>
<td>fec</td>
<td>Expt.</td>
<td>$4.369^\text{u}$, $4.29^\text{v}$, $4.378^\text{x}$</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$2.587\pm0.364^\text{w}$</td>
</tr>
<tr>
<td colspan="11">$\text{AgN}$</td>
</tr>
<tr>
<td rowspan="3">B1</td>
<td>Pres.</td>
<td>4.617</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>12.30</td>
<td>$-2.253$</td>
<td>147.600</td>
<td>5.145</td>
<td>1.587</td>
</tr>
<tr>
<td>Comp.</td>
<td>$4.57^\text{q}$, $4.506^\text{r}$, $4.619^\text{s}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$219.2^\text{r}$, $162.3^\text{s}$</td>
<td>$4.653^\text{P}$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>$4.476^\text{o}$, $4.606^\text{P}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$197.18^\text{o}$, $147.40^\text{P}$</td>
<td>$4.883^\text{o}$</td>
<td></td>
</tr>
<tr>
<td rowspan="2">B2</td>
<td>Pres.</td>
<td>2.873</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>11.86</td>
<td>$-2.021$</td>
<td>146.157</td>
<td>5.260</td>
<td>1.819</td>
</tr>
<tr>
<td>Comp.</td>
<td>$2.833^\text{q}$, $2.806^\text{r}$, $2.876^\text{s}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$138.96^\text{P}$</td>
<td>$4.823^\text{P}$</td>
<td></td>
</tr>
<tr>
<td rowspan="2">B3</td>
<td>Pres.</td>
<td>4.950</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>15.16</td>
<td>$-2.122$</td>
<td>109.639</td>
<td>5.210</td>
<td>1.718</td>
</tr>
<tr>
<td>Comp.</td>
<td>$4.88^\text{q}$, $4.816^\text{r}$, $4.946^\text{s}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$100.11^\text{P}$</td>
<td>$5.825^\text{P}$</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$4.79^\text{o}$, $4.94^\text{P}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$151.05^\text{o}$</td>
<td>$4.542^\text{o}$</td>
<td></td>
</tr>
<tr>
<td>B81</td>
<td>Pres.</td>
<td>3.544</td>
<td>–</td>
<td>4.929</td>
<td>–</td>
<td>13.40</td>
<td>$-1.996$</td>
<td>130.485</td>
<td>5.240</td>
<td>1.844</td>
</tr>
<tr>
<td>B</td>
<td>Pres.</td>
<td>3.521</td>
<td>–</td>
<td>9.368</td>
<td>–</td>
<td>25.15</td>
<td>$-1.891$</td>
<td>57.077</td>
<td>5.110</td>
<td>1.949</td>
</tr>
<tr>
<td>Bh</td>
<td>Pres.</td>
<td>3.096</td>
<td>–</td>
<td>3.023</td>
<td>–</td>
<td>12.55</td>
<td>$-2.121$</td>
<td>141.385</td>
<td>5.285</td>
<td>1.719</td>
</tr>
<tr>
<td rowspan="2">B4</td>
<td>Pres.</td>
<td>3.501</td>
<td>–</td>
<td>5.734</td>
<td>–</td>
<td>15.22</td>
<td>$-2.113$</td>
<td>105.992</td>
<td>5.467</td>
<td>1.727</td>
</tr>
<tr>
<td>Comp.</td>
<td>$3.41^\text{o}$, $3.54^\text{P}$</td>
<td>–</td>
<td>$5.52^\text{o}$, $5.69^\text{P}$</td>
<td>–</td>
<td></td>
<td></td>
<td>$143.68^\text{o}$, $110.12^\text{P}$</td>
<td>$4.82^\text{o}$, $4.663^\text{P}$</td>
<td></td>
</tr>
<tr>
<td>B17</td>
<td>Pres.</td>
<td>3.158</td>
<td>–</td>
<td>5.560</td>
<td>–</td>
<td>13.86</td>
<td>$-2.517$</td>
<td>132.556</td>
<td>5.185</td>
<td>1.323</td>
</tr>
<tr>
<td>B24</td>
<td>Pres.</td>
<td>4.337</td>
<td>4.601</td>
<td>5.091</td>
<td>–</td>
<td>12.70</td>
<td>$-2.202$</td>
<td>138.704</td>
<td>5.132</td>
<td>1.638</td>
</tr>
<tr>
<td colspan="11">$\text{AgN}_2$</td>
</tr>
<tr>
<td rowspan="2">C1</td>
<td>Pres.</td>
<td>5.157</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>11.43</td>
<td>$-1.959$</td>
<td>164.844</td>
<td>4.996</td>
<td>2.333</td>
</tr>
<tr>
<td>Comp.</td>
<td>$5.124^\text{q}$, $5.055^\text{r}$, $5.172^\text{s}$<br>$5.013^\text{m}$, $5.141^\text{n}$</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
<td></td>
<td>$181.3^\text{r}$, $164.5^\text{s}$<br>$215^\text{m}$ $164^\text{n}$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>C2</td>
<td>Pres.</td>
<td>5.617</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>14.77</td>
<td>$-3.626$</td>
<td>30.058</td>
<td>6.894</td>
<td>0.666</td>
</tr>
<tr>
<td>C18</td>
<td>Pres.</td>
<td>3.440</td>
<td>4.513</td>
<td>5.508</td>
<td>–</td>
<td>14.25</td>
<td>$-3.680$</td>
<td>35.878</td>
<td>7.269</td>
<td>0.612</td>
</tr>
<tr>
<td>CoSb2</td>
<td>Pres.</td>
<td>5.976</td>
<td>5.651</td>
<td>10.261</td>
<td>$\beta=151.225$</td>
<td>13.90</td>
<td>$-3.699$</td>
<td>35.117</td>
<td>7.822</td>
<td>0.593</td>
</tr>
</tbody>
</table>

a Ref.50. This is an average of 56 experimental values, at $20^\circ C$.
b Ref.51. Cohesive energies are given at $0K$ and $1atm=0.00010$ GPa; while bulk mudulii are given at room temperature.
c Ref. (25) in 52: at room temperature.
d See Refs. (8)–(11) in 52.
f Ref.53. using the full-potential linearized augmented plane waves (LAPW) method within LDA.
g Ref.54: using projector augmented wave (PAW) method within LDA.
h Ref.54: using projector augmented wave (PAW) method within GGA(PW91).
i Ref.54: using projector augmented wave (PAW) method within GGA(PBE).
j Ref.52: using semiempirical estimate based on the calculation of the slope of the shock velocity vs. particle velocity curves obtained from the dynamic high-pressure experiments. The given values are estimated at $\sim298K$.
k Ref.52: using a semiempirical method in which the experimental static $P-V$ data are fitted to an EOS form where $B_0$ and $B_0'$ are adjustable parameters. The given values are estimated at $\sim298K$.
l Ref.52: using the so-called method of transition metal pseudopotential theory; a modified form of a method proposed by Wills and Harrison to represent the effective interatomic interaction.
m Ref. [17]: using the full-potential linearized augmented plane waves (LAPW) method within LDA.
n Ref. [17]: using the full-potential linearized augmented plane waves (LAPW) method within GGA.
o Ref. [16]: using full-potential (linearized) augmented plane waves plus local orbitals (FP-LAPW+lo) method within LDA.
p Ref. [16]: using using full-potential (linearized) augmented plane waves plus local orbitals (FP-LAPW+lo) method within GGA(PBE).
q Ref. [15]: using pseudopotential (PP) method within LDA.
r Ref. [15]: using linear combinations of atomic orbitals (LCAO) method within LDA. $B_0$’s are calculated from elastic constants.
s Ref. [15]: using linear combinations of atomic orbitals (LCAO) method within GGA. $B_0$’s are calculated from elastic constants.
t This is the face centered cubic (fcc) structure with $Z=4/3$ (i.e. 4 Ag atoms in the unit cell) suggested by Hahn and Gilbert according to some measurements (Ref. 9).
u Ref. 9.
v Ref. 8.
w This is the average of the experimental values: $(+314.4\mp2.5)\text{kJ/mol}^7=(3.25853\pm0.02591)eV/\text{atom}$, $+199\text{kJ/mol}^{11}=2.062eV/\text{atom}$, $+255\text{kJ/mol}^9=2.643eV/\text{atom}$, and $+230\text{kJ/mol}^{10}=2.384eV/\text{atom}$. We used the conversion relation: $1eV/\text{atom}=96.521\text{kJ/mol}$ or equivalently $1\text{kJ/mol}=0.010364eV/\text{atom}$.
x Ref. 12.

cubic D09 phase is the stable phase of the synthesized Cu₃N⁵⁵.

The odd behavior of the EOS of Ag₃N(Fe₃N) with the existence of two minima (Fig. 1) shows that the first minima (to the left) is a metastable local minimum that cannot be maintained as the system is decompressed. Ag ions are in the 6g Wyckoff positions: $(x,0,0),(0,x,0),(-x,-x,0),(-x,0,\frac{1}{2}),(0,-x,\frac{1}{2})$


![](./images/867748054407578313_4.jpg)

FIG. 4. (Color online.) Calculated equilibrium properties of the twenty studied phases of silver nitrides. All quantities are given relative to the corresponding ones of the fcc crystalline elemental silver given in the first row of Table I. The vertical dashed lines separate between the different stoichoimetries.

![](./images/867748054407578313_5.jpg)

FIG. 5. (Color online.) Enthalpy $H$ vs. pressure $P$ equation of state (EOS) for some ${\rm Ag_3N}$ phases in the range where D0$_9$ $\rightarrow$ A15, D0$_9$ $\rightarrow$ D0$_3$ and D0$_9$ $\rightarrow$ L1$_2$ phase transitions occur.

and $(x,x,\frac{1}{2})$; with $x \sim \frac{1}{3}$ to the left of the potential barrier (represented by the sharp peak at $\sim 18.2$ $\mathring{\rm A}^3$/atom), and $x = \frac{1}{2}$ to the right of the peak. It may be relevant to mention here that ${\rm Cu_3N(Fe_3N)}$ was found to behave in a similar manner$^5$.

The crossings of the less stable A15, D0$_3$ and L1$_2$ EOS curves with the more stable D0$_9$, D0$_2$ and RhF$_3$ ones at the left side of their equilibrium points reveals pressure-induces phase transitions from the latter phases to the former. To show this, we plotted the corresponding relation between enthalpy $H = E(V)+PV$ and the imposed pressure $P$ in Fig. 5. Since D0$_9$, D0$_2$ and RhF$_3$ phases have identical $E(V)$ curves, the corresponding $H(P)$ curves are also identical. Hence, only the $H(P)$ of D0$_9$ is displayed in Fig. 5. A point where the enthalpies of two phases are equal determine the phase transition pressure $P_t$; and, indeed, the direction of the transition is from the higher $H$ to the lower $H^{56}$. As depicted in Fig. 5, $P_t({\rm D0_9 \rightarrow L1_2}) = 17.8$ GPa, $P_t({\rm D0_9 \rightarrow D0_3}) = 19.5$ GPa and $P_t({\rm D0_9 \rightarrow A15}) = 26.0$ GPa. Thus, D0$_9$, D0$_2$ and RhF$_3$ would not survive behind these $P_t$'s and A15, D0$_3$ and L1$_2$ are preferred at high pressure.

Fig. 4 reveals that the AgN group contains the least stable phase among all the twenty studied phases: the hexagonal B$_k$. Fig. 2 and Table I show that the simple tetragonal structure of cooperite (B17) is the most stable phase in this AgN series. In fact, one can see from Fig. 4 and Table I that all the considered AgN phases possess less binding than their parent Ag(fcc), except AgN(B17) which is slightly more stable, with 0.033 $eV$/atom lower $E_{\rm coh}$. It is interesting to notice that AgN(B17) is $\sim 0.003$ $eV$/atom more stable than the ${\rm Ag_3N}$ most stable phases. Moreover, this B17 structure was theoretically predicted to be the ground-state structure of CuN$^5$, AuN$^{57}$, PdN$^{58}$ and PtN$^{59}$.

Using the full-potential (linearized) augmented plane waves plus local orbitals (FP-LAPW+lo) method within LDA and within GGA, Kanoun and Said$^{16}$ studied the $E(V)$ EOS for AgN in the B1, B2, B3 and B4 structures. The equilibrium energies they obtained from the $E(V)$ EOS revealed that B1 is the most stable phase, and the relative stability they arrived at is in the order B1–B3–B4–B2, with a significant difference in total energy between B3 and B4 (see Fig. 2(b) in that article). Within this subset of structures, the numerical values of $E_{\rm coh}$ in Table I do have the same order. However, the difference between the equilibrium $E_{\rm coh}$(B3) and $E_{\rm coh}$(B4) is only $\sim 0.009$ $eV$, and the $E(V)$ EOS of B3 and B4 match/overlap over a wide range of volumes around the equilibrium point. This discrepancy may be attributed to the unphysical/ill-defined measure of stability that Kanoun and Said used, the total energy, while the number of the AgN formula units per unit cell in the B4 structure differs from that in the others$^{60}$. Nevertheless, it may be worth mentioning here that AgN(B3) was found to be elastically unstable$^{15}$.

In the CuN$_2$ nitrogen-richest phase series, we can see from Table I and from Fig. 4 that the phases of this group are significantly more stable than all the other studied phases, except C1, which is, in contrast, the second least stable among the twenty studied phases, with 0.017 $eV$/atom more than ${\rm AgN(B_k)}$. From Fig. 3, Fig. 4 and Table I, one can see that in this series, the lower the structural symmetry, the more stable is the phase. It was found that CuN$_2$ phases have the same trend$^5$.

Comparing the relative stability of ${\rm Ag_3N}$, AgN and AgN$_2$, we find from Table I and from Fig. 4 that AgN$_2$ in its least symmetric phase, the simple monoclinic structure of CoSb$_2$, is the most energetically stable phase with $E_{\rm coh} = -3.699$ $eV$/atom.

### B. Volume per Atom and Lattice Parameters

The numerical values of the lattice parameters and the average equilibrium volume per atom $V_0$ for the twenty modifications are presented in Table I. The middle subwindow of Fig. 4 depicts the $V_0$ values relative to the Ag(fcc). To measure the average of the Ag–Ag bond length in the silver nitride, the equilibrium average volume per Ag atom ($V_0^{Ag}$), which is simply the ratio of the volume the unit cell to the number of Ag atoms in the unit cell, is visualized in the same subwindow.

From the $V_0$ curve in Fig. 4, we can see that, all AgN and AgN$_2$ modifications, except the open AgN(B$_k$) phase, decrease $V_0$; while the ${\rm Ag_3N}$ phases tend, on average, not to change the number density of the parent Ag(A1).

On the other hand, the $V_0^{Ag}$ curve in Fig. 4 reveals that, relative to the elemental Ag and to each other, $V_0^{Ag}$ tends to increase with the increase in the nitrogen content. Thus, in all these nitrides, the introduced N ions displace apart the ions of the host lattice causing longer Ag-Ag bonds than in the elemental Ag. This cannot be seen directly from the $V_0$ values depicted in the same figure.

For AgN in the B1, B2, B3 and B4 structures, Ka- noun and Said (Ref. 16 described in Sec. III A above) obtained GGA equilibrium lattice parameters which are in very good agreement with ours. Their obtained LDA lattice parameter values show the common underestima- tion with respect to their and our GGA values (see Table I).

Gordienko and Zhuravlev $^{15}$ studied the structural, me chanical and electronic properties of AgN(B1) , AgN(B2), $AgN(B 3), AgN_{2}(C 1)$ and $Ag_{3} N(D 0_{9})$ cubic phases. TheirDFT calculations were based on pseudopotential (PP) method within LDA, and on linear combinations of atomic orbitals (LCAO) method within both LDA and GGA. For comparison, some of their findings are included in Table I. Within the parameter subspace they consid- ered, our GGA values of the $a$ lattice parameter agree very well with theirs. On the other hand, although their PP $a$ values are closer to the GGA ones (ours and theirs), all their LDA values are less than the GGA ones. This confirms the well-known behavior of LDA compared to GGA $^{61-63}$ . Gordienko and Zhuravlev also found that theAg-Ag interatomic distance increases in the order $Ag_{3} N-$  AgN-AgN2. This agrees with the general trend shown in Fig. 4, since the $V_{0}^{A g}$ curve shows an average increase in the same direction.

### C. Bulk Modulus and its Pressure Derivative
Fig. 4 reveals that $Ag_{3} N$ phases tend, on average, to preserve the $B_{0}$ value of the parent $Ag(A 1)$ . Increasing the nitrogen content to get $AgN$ phases will increase the $B_{0}$ value of the parent $Ag(A 1)$ , except in the case of $B_{k}$ . While the nitrogen in $AgN_{2}$ tends to lower the $B_{0}$ value of the parent $Ag(A 1)$ , the cubic $C 1$ phase posses the highest Bo value. This could be seen from Fig. 3, where the curvature of the $E_{coh }(V)$ curve of $C 1$ is higher compared to the shallow minima of the $C 2, C 18$ and $CoSb_{2}$ curves.
From the definition of the equilibrium bulk modulus(Eq. 4), one would expect $B_{0}$ to increase as $E_{coh }$ or $V_{0}$  decreases. This is because of the minus sign of the for- mer and the inverse proportionality of the latter. That is, roughly speaking, the $B_{0}$ curve should have a mirrorreflection-like behavior with respect to the $E_{coh }$ and $V_{0}$  curves. Nevertheless, if $E_{coh }$ or $V_{0}$ are increasing and the other is decreasing, then the dominant net effect will be of the one with the higher change $^{64}$ . For example,Fig. 4 shows that in going from $D_{9}$ to $A 15$ , both $E_{coh }$  and $V_{0}$ increase resulting in a negative change in $B_{0}$ . In going from $A 15$ to $D 0_{9}, E_{coh }$ is decreasing while $V_{0}$ is in creasing, but, in the end, the latter won the competition and lowered the value of $B_{0}$ . This argument stays true throughout the three series. When there is no significant change in both $E_{coh }$ and $V_{0}$ , there is no significant change in $B_{0}$ . This is the case when one goes from $C 18$ to $CoSb_{2}$ . A close look at the $B_{0}$ curve in Fig. 4, reveals that the huge decrease in $E_{coh }$ between $C 1$ and $C 2$ defeats the relatively small increase in $V_{0}$ . This is simply because, according to Eq. 4, the value of $B_{0}$ is proportional to the absolute change in $E_{coh }$ , while it is far more sensitive to any change in $V_{0}$ because it is proportional to $(\Delta V_{0})^{-1}$ .
It is common to measure the pressure dependence of $B_{0}$ by its derivative $B_{0}^{\prime}$ (Eq. 5). Fig. 4 shows that the $B_{0}$ value of the $C 2, C 18$ and $CoSb_{2}$ phases increases as these phases are put under pressure. While the $B_{0}$ val ues of the rest of the phases shows very low sensitivity to pressure and they tend to slightly lower the bulk modu- lus, the $Fe_{3} ~N$ phase is the most sensitive phase and tends to significantly lower its $B_{0}$ upon application of pressure. This high sensitivity may indicate that the correspond- ing minimum on the potential surface is not global, but another local minimum as the one at $16.2 \AA^{3} /$ atom (Fig.1).
From the elastic constants they obtained, Gordienko and Zhuravlev $^{15}$ calculated the corresponding macro scopic bulk moduli (included in Table I). They found the highest LDA $B_{0}$ value for $AgN(B 1)$ among all phases they considered, but, in agreement with the present work, they obtained the highest GGA $B_{0}$ value for $AgN_{2}(C 1)$ . Since LDA relative to GGA overestimates $E_{coh }$ and thus underestimates $V_{0}$ , each of these two factors (see Subsec tion III C) would separately lead to the odd LDA value of $219.2 GPa$ which they obtained. Nevertheless, due to this fact, Gordienko and Zhuravlev argued that one should consider the LDA and GGA average value of $B_{0}$ .

### D. Formation Energies
Formation energies in the present work are used as a measure of the relative thermodynamic stabilities of the phases under consideration. That is, the lower the formation energy, the lower the tendency to dissociate back into the constituent components $Ag$ and $N_{2}$ .
The obtained formation energies $E_{f}$ of the twenty re laxed phases are given in Table I and depicted graphically in Fig. 4. The latter shows that, relative to each other and within each series, the formation energy $E_{f}$ (defined by Eqs. 6 and 7) of the studied phases has the same trend as the cohesive energy $^{65}$ . That is, all phases havethe same relative stabilities in the $E_{f}$ space as in the $E_{coh }$  space. However, while $Ag_{3} ~N$ phases tend to have equal $E_{coh }$ as the AgN phases, all $Ag_{3} ~N$ modifications have a lower $E_{f}$ than the AgN ones. Hence, silver nitride is more likely to be formed in the former stoichiometry. However, all the twenty obtained $E_{f}$ values are positive; which, in principle, means that all these phases are thermodynam- ically unstable (endothermic) $^{66}$ .
Some of the experimental values of $E_{f}$ for the syn thesized $Ag_{3} ~N$ phase (which is claimed to be in an fcc structure) are $+199 ~kJ / mol^{11}=2.062 eV /$ atom,+230 kJ/mol10= 2.384 eV/atom, +255 kJ/mol= $2.643 eV /$ atom and $(+314.4 \mp 2.5) kJ / mol^{7}=(3.25853 \pm$  $0.02591) eV$ ; with an average value of $2.587 \pm 0.364 eV$ . Among the considered phases in the present work, there is only one phase wich has $E_{f}$ value that fits in this range,

the AgN₂(C1). Interestingly, this C1 structure has an fcc underlying Bravia lattice; however, the chemical formula differs from that of the synthesized phase.

## E. Electronic Properties

The DFT(GGA) calculated band diagrams (i.e. $\epsilon_i^\sigma(\mathbf{k})$ curves) and spin-projected total and orbital resolved (i.e. partial) density of states (DOS) of the most stable phases: D0₉, RhF₃, D0₂, B17, and C18 are presented in Figs. 6, 7, 8, 9 and 10, respectively. Spin-projected total density of states (TDOS) are shown in sub-figure (b) in each case. In all the six considered cases, electrons occupy the spin-up and spin-down bands equally, resulting in zero spin-polarization density of states: $\zeta(\epsilon)=n_\uparrow(\epsilon)-n_\downarrow(\epsilon)$. Thus, it is sufficient only to display spin-up (or spin-down) density of states (DOS) and spin-up (or spin-down) band diagrams. In order to investigate the details of the electronic structure of these phases, energy bands are plotted along densely sampled high-symmetry string of neighboring $\mathbf{k}$-points. Moreover, to extract information about the orbital character of the bands, the $\text{Ag}(s,p,d)$ and $\text{N}(s,p)$ partial DOS are displayed at the same energy scale.

Fig. 6(a) shows the band structure $\epsilon_i^\sigma(\mathbf{k})$ of Ag₃N(D0₉). With its valence band maximum (VBM) at $(R, -0.086\ eV)$ and its conduction band minimum (CBM) at $(\Gamma, 0.049\ eV)$, Ag₃N(D0₉) presents a semiconducting character with a narrow indirect band gap $E_g$ of $0.134\ eV$. From sub-figures 6(c) and (d), it is seen clearly that the $\text{Ag}(d)$-$\text{N}(p)$ mixture in the region from $-7.286\ eV$ to $-0.086\ eV$ beneath $E_F$, with two peaks: a low density peak around $1.5\ eV$ and a high density peak around $4.0\ eV$ steaming mainly from the bands of silver $d$ electrons.

Our obtained PDOS, TDOS and band structure of Ag₃N(D0₉) agree qualitatively well with Gordienko and Zhuravlev¹⁵; however, using LCAO method within GGA, the value of the indirect $E_g$ of Ag₃N(D0₉) they predicted is $0.25\ eV$.

To the best of our knowledge, there is no experimentally reported $E_g$ value for Ag₃N. However, Tong⁸ prepared Ag₃₊ₓN samples, and carried out XRD measurements to confirm the fcc symmetry of the prepared samples. Using a TB-LMTO code within LDA, Tong then calculated the band structure of Ag₃N and obtained an indirect energy gap of $1.35\ eV$. Nevertheless, we could not figure out the positions of the N ions Tong's model.

It is a well known drawback of Kohn-Sham DFT-based calculations to underestimate the band gap. Thus the more demanding $GW$ calculations were carried out, and the obtained $E_g$ value will be presented in Sec. III F.

Calculated electronic properties of Ag₃N(D0₂) are displayed in Fig. 8. sub-figure 8(a) shows the energy bands $\epsilon_i^\sigma(\mathbf{k})$ of Ag₃N(D0₂). With its valence band maximum (VBM) at $(H, -0.091\ eV)$ and its conduction band minimum (CBM) at $(\Gamma, 0.039\ eV)$, Ag₃N(D0₉) presents semiconducting character with a narrow indirect band gap $E_g$ of $0.130\ eV$. From sub-figures 8(c) and (d), one can notice clearly the $\text{Ag}(d)$-$\text{N}(p)$ mixture in the region from $-7.249\ eV$ to $-0.091\ eV$ below $E_F$, with two peaks: a low density peak around $-1.3\ eV$ steaming from an almost equal mixture of $\text{Ag}(d)$ and $\text{N}(p)$, and a high density peak around $-4.3\ eV$ steming mainly from the bands of silver $d$ electrons plus a relatively very low contribution from the $\text{N}(p)$ states.

Fig. 7 depicts the band diagram and DOS's of Ag₃N(RhF₃). In contrast to Ag₃N(D0₉) and Ag₃N(D0₂), sub-figure 7(a) shows that Ag₃N(RhF₃) is a semiconductor with a narrow direct band gap of $0.129\ eV$ of width located at $\Gamma$ point. The VBM is at $-0.089\ eV$ and the CBM is at $0.040\ eV$. From sub-figures 7(c) and (d), one can see the $\text{Ag}(d)$-$\text{N}(p)$ mixture is in the region from $-7.286\ eV$ to $-0.089\ eV$ below $E_F$, with two peaks: a low density peak around $-1.366\ eV$ steaming from an almost equal mixture of $\text{Ag}(d)$ and $\text{N}(p)$, and a high density peak around $-4.382\ eV$ steaming mainly from the bands of silver $d$ electrons plus a relatively very low contribution from the $\text{N}(p)$ states.

The relationship between D0₉, D0₂ and RhF₃ structures manifests itself in many common features between the electronic structure of these three Ag₃N nitrides: (i) equal $E_g$ of $\sim 0.13\ eV$; (ii) a deep bound band around $\sim -14.6\ eV$ below $E_F$ consists mainly of the $\text{N}(2s)$ states; (iii) a broad valence band with $\sim 7.2\ eV$ of width that comes mostly from the $4d$ electrons of Ag plus a very small contribution from $\text{N}(2p)$; and (iv) the relatively low TDOS of the conduction bands.

Energy bands $\epsilon_i^\sigma(\mathbf{k})$, total density of states (TDOS) and partial (orbital-resolved) density of states (PDOS) of AgN(B17) are shown in Figs. 9. It is clear that AgN(B17) would be a true metal at its equilibrium. The major contribution to the very low TDOS around Fermi energy $E_F$ comes from the $2p$ states of the N atoms as it is evident from sub-figure 9(d). Beneath $E_F$ lies a band with $\sim 7.3\ eV$ of width, in which the main contribution is due to the $\text{Ag}(4d)$ states plus a small contribution from the $\text{N}(2p)$ states. While the $\text{N}(2s)$ states dominate the deep lowest region around $13.5\ eV$, the low density unoccupied bands stem mainly from the $\text{N}(2p)$ states. The Fermi surface crosses two partly occupied bands: a lower one in the $X-M$, $\Gamma-Z-A$ and $\Gamma-X-R$ directions, and a higher band in the $X-M-\Gamma$ and $M-A$ directions. Thus, $E_F$ is not a continuous surface contained entirely within the first BZ.

It may be worth mentioning here that AgN(B1)¹⁶,⁶⁸ and AgN(B3)¹⁶,⁶⁹ phases were also theoretically predicted to be metallic.

Although AgN₂(CoSb₂) is the most stable phase, but the difference in cohesive energy between AgN₂(CoSb₂) and AgN₂(C18) is less than $0.02\ eV$/atom, and we decided to examine the electronic structure of both phases. With $E_F$ crossing the finite TDOS, Fig. 10 shows that AgN₂(C18) is metallic at $0\ K$. The orbital resolved DOS's reveal that the major contribution to the low TDOS at $E_F$ comes from the $\text{N}(2p)$ states with tiny

![](./images/867748054407578313_6.jpg)

FIG. 6. (Color online.) DFT calculated electronic structure for $Ag_3N$ in the D0₉ structure: (a) band structure along the high-symmetry $\mathbf{k}$-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $M(0.5,0.5,0.0)$, $\Gamma(0.0,0.0,0.0)$, $X(0.0,0.5,0.0)$, $R(0.5,0.5,0.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in $Ag_3N$; and (d) PDOS of $\text{N}(s,p)$ orbitals in $Ag_3N$.

![](./images/867748054407578313_7.jpg)

FIG. 7. (Color online.) DFT calculated electronic structure for $Ag_3N$ in the $RhF_3$ structure: (a) band structure along the high-symmetry $\mathbf{k}$-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $F(0.5,0.5,0.0)$, $Q(0.375,0.625,0.0)$, $B(0.5,0.75,0.25)$, $Z(0.5,0.5,0.5)$, $\Gamma(0.0,0.0,0.0)$, $L(0.0,0.5,0.0)$, $Y(0.25,0.5,-.25)$, $\Sigma(0.0,0.5,-.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in $Ag_3N$; and (d) PDOS of $\text{N}(s,p)$ orbitals in $Ag_3N$.

![](./images/867748054407578313_8.jpg)

FIG. 8. (Color online.) DFT calculated electronic structure for $Ag_3N$ in the D0₂ structure: (a) band structure along the high-symmetry $\mathbf{k}$-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $\Gamma(0.0,0.0,0.0)$, $N(0.0,0.0,0.5)$, $P(0.25,0.25,0.25)$, $H(0.5,-.5,0.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in $Ag_3N$; and (d) PDOS of $\text{N}(s,p)$ orbitals in $Ag_3N$.

![](./images/867748054407578313_9.jpg)

FIG. 9. (Color online.) DFT calculated electronic structure for AgN in the B17 structure: (a) band structure along the high-symmetry k-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $X(0.0,0.5,0.0)$, $M(0.5,0.5,0.0)$, $\Gamma(0.0,0.0,0.0)$, $Z(0.0,0.0,0.5)$, $A(0.5,0.5,0.5)$, $R(0.0,0.5,0.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in AgN; and (d) PDOS of $\text{N}(s,p)$ orbitals in AgN.

![](./images/867748054407578313_10.jpg)

FIG. 10. (Color online.) DFT calculated electronic structure for $\text{AgN}_2$ in the C18 structure: (a) band structure along the high-symmetry k-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $\Gamma(0.0,0.0,0.0)$, $X(0.0,0.5,0.0)$, $S(-.5,0.5,0.0)$, $Y(-.5,0.0,0.0)$, $Z(0.0,0.0,0.5)$, $U(0.0,0.5,0.5)$, $R(-.5,0.5,0.5)$, $T(-.5,0.0,0.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in $\text{AgN}_2$; and (d) PDOS of $\text{N}(s,p)$ orbitals in $\text{AgN}_2$.

![](./images/867748054407578313_11.jpg)

FIG. 11. (Color online.) DFT calculated electronic structure for $\text{AgN}_2$ in the $\text{CoSb}_2$ structure: (a) band structure along the high-symmetry k-points which are labeled according to Ref. [67]. Their coordinates w.r.t. the reciprocal lattice basis vectors are: $\Gamma(0.0,0.0,0.0)$, $B(-.5,0.0,0.0)$, $A(-.5,0.5,0.0)$, $E(-.5,0.5,0.5)$, $Z(0.0,0.0,0.5)$, $Y(0.0,0.5,0.5)$, $D(-.5,0.0,0.5)$ and $C(0.0,0.5,0.5)$; (b) spin-projected total density of states (TDOS); (c) partial density of states (PDOS) of $\text{Ag}(s,p,d)$ orbitals in $\text{AgN}_2$; and (d) PDOS of $\text{N}(s,p)$ orbitals in $\text{AgN}_2$.

contributions from the 5s, 4d and 3p states of Ag, respectively. As one can see from sub-figure 10(a), the $E_F$ surface crosses the edges of the first Brillouin zone in the $Z$-$U$-$R$-$S$-$T$-$X$ and $T$-$Z$ directions.

The calculated electronic properties of ${\rm AgN_2(CoSb_2)}$ are displayed in Fig. 11. Band structure, TDOS and orbital resolved DOS's have almost the same features as the corresponding ones of ${\rm AgN_2(C18)}$. It may be worth to mention here that C1 phase of ${\rm AgN_2}$ was also theoretically predicted to be metallic$^{15}$.

Compared to the metallic AgN(B17), three new features of these 1:2 nitrides are evident: (i) Deep at $\sim -22.7$ $eV$ there is a highly-localized mixture of the N($s$)-N($p$) states. However, the variation in N($2s$) energy with respect to $\mathbf{k}$ is smaller than the variation of N($2p$) states, resulting in a narrower and higher PDOS. (ii) Below the band that is crossed by $E_F$ there are four bands separated by $\sim 11.4$ $eV$, $\sim 1.6$ $eV$, $\sim 0.38$ $eV$ and $\sim 0.28$ $eV$ energy gaps, respectively. (iii) The very tiny contribution of the N($p$) states to the N($2p$)-Ag($4d$) band.

A common feature of all the studied cases is that Ag($p$)-orbitals do not contribute significantly to the hybrid bands. Another common feature is the highly structured, intense and narrow series of peaks in the TDOS valance band corresponding to the superposition of N($2p$) and Ag($4d$) states. In their $\mathbf{k}$-space, Ag($4d$) energies show little variation with respect to $\mathbf{k}$; hence the Van Hove singularities-like sharp features.

To summarize, we have found that the most stable phases of AgN and ${\rm AgN_2}$ are metallic, while those of ${\rm Ag_3N}$ are semiconductors. A close look at Fig. 9 up to Fig. 6 reveals that as the nitrogen to silver ratio increases from $x=1$ to $x=1/2$, the TDOS at $E_F$ decreases; and by arriving at $x=1/3$ a gap opens. This finding agrees well with Gordienko and Zhuravlev$^{15}$. Moreover, it may be worth mentioning here that such behavior was theoretically predicted to be true for copper nitrides as well$^{5,70}$.

### F. Optical Properties

Fig. 12 depicts the $GW$ calculated real and imaginary parts of the frequency-dependent dielectric function $\varepsilon_{\rm RPA}(\omega)$ of ${\rm Ag_3N(D0_9)}$ and the corresponding derived optical constants. The optical region$^{71}$ is shaded in each sub-figure.

The real part $\varepsilon_{\rm re}(\omega)$ (sub-figure 12(a)) shows an upward trend before $\sim 2.3$ $eV$, where it reaches its maximum value and generally decreases after that. The imaginary part $\varepsilon_{\rm im}(\omega)$ (same sub-figure 12(a)) shows an upward trend before $\sim 1.0$ $eV$ and it has three main peaks located at $\sim 2.6$ $eV$ in the optical region, $\sim 3.3$ $eV$ at the right edge of the optical region, and at $\sim 4.1$ $eV$ in the UV range.

Calculated reflectivity $R(\omega)$ and transmittivity $T(\omega)$ are displayed in sub-figure 12(b). With $0.6 \leq R(\omega) \leq 0.8$, it is evident that ${\rm Ag_3N(D0_9)}$ is a good reflector, specially in the red and the infrared regions. In the visible range, the maximum transmittivity $T(\omega)$ is at $\sim 2.54$ $eV$ $\equiv$ 489 nm, which is at the blue-green edge.

sub-figure 12(c) depicts the calculated refraction $n(\omega)$ and extinction $\kappa(\omega)$ coefficients. As they should, these two spectra have, in general, the same qualitative frequency dependence as the real $\varepsilon_{\rm re}(\omega)$ and the imaginary $\varepsilon_{\rm im}(\omega)$ dielectric functions, respectively.

From the absorption coefficient $\alpha(\omega)$ spectrum (sub-figure 12(d)), it can be seen that ${\rm Ag_3N(D0_9)}$ starts absorbing photons with $\sim 0.9$ $eV$ energy. Hence, it is clear that $GW_0$ calculations give a band gap of $\sim 0.9$ $eV$, which is a significant improvement over the value obtained from DFT. The non-vanishing $\alpha(\omega)$ in the whole optical region agrees with the experiment, since it may explain the observed black color of the synthesized ${\rm Ag_3N}$.

To the best of our knowledge, the present work is the first trial to theoretically investigate the optical properties of silver nitride. However, for more accurate optical characterization (e.g. more accurate positions and amplitudes of the characteristic peaks), electron-hole excitations should be calculated. This can be done by evaluating the two-body Green function $G_2$ on the basis of our obtained GW one-particle Green function $G$ and QP energies, then solving the so-called Bethe-Salpeter equation, the equation of motion of $G_2^{72}$.

### IV. CONCLUSIONS

We have succesfully employed first-principles calculation methods to investigate the structural, stability, electronic and optical properties of ${\rm Ag_3N}$, AgN and ${\rm AgN_2}$. Within the accuracy of the employed methods, the obtained structural parameters, EOS, $B_0$, $B_0'$ and electronic properties show good agreement with the few avialable previous calculations. On the other hand, our obtained results show, at least, partial agreement with three experimental facts: (i) the lattice parameter of ${\rm Ag_3N(D0_9)}$ is close to the experimentally reported one; (ii) the positive formation energies reveals the endothermic (unstable) nature of silver nitrides, and (iii) absorption spectrum explains its observed black color. Moreover, the present work may be considered as the first trial to theoretically investigate the optical properties of silver nitride. We hope that some of our obtained results will be confirmed in future experimentally and/or theoretically.

### ACKNOWLEDGMENTS

All GW calculations and some DFT calculations were carried out using the infrastructure of the Centre for High Performance Computing (CHPC) in Cape Town. Suleiman would like to acknowledge the support he received from Wits, DAAD, AIMS, SUST and the AS-ESMA group. Many thanks to the Scottish red pen of

![](./images/867748054407578313_12.jpg)

FIG. 12. (Color online.) The $GW$ calculated frequency-dependent optical spectra of $\text{Ag}_3\text{N}(\text{D0}_9)$: (a) the real $\varepsilon_{\text{re}}(\omega)$ and the imaginary $\varepsilon_{\text{im}}(\omega)$ parts of the dielectric function $\varepsilon_{\text{RPA}}(\omega)$; (b) reflectivity $R(\omega)$ and transmittivity $T(\omega)$; (c) refraction $n(\omega)$ and extinction $\kappa(\omega)$ coefficients; and (d) absorption coefficient $\alpha(\omega)$. The shaded area highlights the optical region.

Ross McIntosh!

---

* Corresponding author: suleiman@aims.ac.za
$\dagger$ Homepage: http://www.wits.ac.za/staff/daniel.joubert2.htm
$^{1}$ D. Åberg, P. Erhart, J. Crowhurst, J. M. Zaug, A. F. Goncharov, and B. Sadigh, Physical Review B $\mathbf{82}$, 104116 (Sep 2010), http://link.aps.org/doi/10.1103/PhysRevB.82.104116
$^{2}$ X. P. Du and Y. X. Wang, Journal of Applied Physics $\mathbf{107}$, 053506 (2010), http://link.aip.org/link/?JAP/107/053506/1
$^{3}$ M. G. Moreno-Armenta, W. L. Prez, and N. Takeuchi, Solid State Sciences $\mathbf{9}$, 166 (2007), ISSN 1293-2558, http://www.sciencedirect.com/science/article/pii/S1293255806002858
$^{4}$ R. Juza and H. Hahn, Zeitschrift fr anorganische und allgemeine Chemie $\mathbf{241}$, 172 (1939), ISSN 1521-3749, http://dx.doi.org/10.1002/zaac.19392410204
$^{5}$ M. S. H. Suleiman, M. P. Molepo, and D. P. Joubert, ArXiv e-prints(Nov. 2012), arXiv:1211.0179 [cond-mat.mtrl-sci]
$^{6}$ Y. Du, A. Ji, L. Ma, Y. Wang, and Z. Cao, Journal of Crystal Growth $\mathbf{280}$, 490 (2005), ISSN 0022-0248, http://www.sciencedirect.com/science/article/pii/S0022024805004264
$^{7}$ E. S. Shanley and J. L. Ennis, Industrial & Engineering Chemistry Research $\mathbf{30}$, 2503 (1991), http://pubs.acs.org/doi/pdf/10.1021/ie00059a023, http://pubs.acs.org/doi/abs/10.1021/ie00059a023
$^{8}$ J. Tong, Darstellung, Strukturen und Eigen- schaften ausgewählter Perowskit-Materialien und Molekülkristalle, Ph.D. thesis, Max-Planck- Institut für Festkörperforschung, Stuttgart (2010), http://elib.uni-stuttgart.de/opus/volltexte/2010/5816/
$^{9}$ H. Hahn and E. Gilbert, Zeitschrift fr anorganische Chemie $\mathbf{258}$, 77 (1949), ISSN 1521-3749, http://dx.doi.org/10.1002/zaac.19492580109
$^{10}$ R. Anderson and N. Parlee, High Temperature Science $\mathbf{2}$, 289 (1970), http://www.osti.gov/energycitations/product.biblio.jsp?osti_id=4085291
$^{11}$ R. Juza and H. Hahn, Zeitschrift fr anorganische und allgemeine Chemie $\mathbf{244}$, 133 (1940), ISSN 1521-3749, http://dx.doi.org/10.1002/zaac.19402440205
$^{12}$ M. Haisa, Acta Crystallographica Section A $\mathbf{38}$, 443 (Jul 1982), http://dx.doi.org/10.1107/S0567739482000990
$^{13}$ $\text{Ag}_3\text{N}$, formerly termed fulminating silver by its discoverers, can be formed from ammoniacal solutions of silver oxide according to the following reaction
$$3\text{Ag}_2\text{O} + 2\text{NH}_3^{(\text{aq})} \longrightarrow 2\text{Ag}_3\text{N} + 5\text{H}_2\text{O}. \tag{16}$$
It can also be formed by means of other reactions$^{7,8}$.
$^{15}$ A. Gordienko and Y. Zhuravlev, Journal of Structural Chemistry $\mathbf{51}$, 401 (2010), ISSN 0022-4766, http://dx.doi.org/10.1007/s10947-010-0061-8
$^{16}$ M. Kanoun and S. Goumri-Said, Physics Letters A $\mathbf{362}$, 73 (2007), ISSN 0375-9601, http://www.sciencedirect.com/science/article/pii/S03759601060106
$^{17}$ X. F. Zhang, Physical Review B $\mathbf{72}$, 054103 (Aug 2005), http://link.aps.org/doi/10.1103/PhysRevB.72.054103
$^{18}$ A. F. Wells, Structural Inorganic Chemistry, 5th ed. (Oxford University Press, 1984) ISBN 9780198553700, http://books.google.co.za/books?id=lQfwAAAAMAAJ
$^{19}$ U. von Barth and L. Hedin, Journal of Physics C: Solid State Physics $\mathbf{5}$, 1629 (Feb 1972), http://iopscience.iop.org/0022-3719/5/13/012/
$^{20}$ M. Pant and A. Rajagopal, Solid State Communications $\mathbf{10}$, 1157 (1972), ISSN 0038-1098, http://www.sciencedirect.com/science/article/pii/00381098729
$^{21}$ G. Kresse and J. Hafner, Physical Review B $\mathbf{47}$, 558 (Jan 1993), http://link.aps.org/doi/10.1103/PhysRevB.47.558
$^{22}$ G. Kresse and J. Hafner, (May 1994), http://link.aps.org/doi/10.1103/PhysRevB.49.14251

http://link.aps.org/doi/10.1103/PhysRevB.49.14251

23 G. Kresse and J. Furthm-
ller, Computational Materials Science
6, 15 (1996), ISSN 0927-0256,
http://www.sciencedirect.com/science/article/pii/0927025696000888), http://othes.univie.ac.at/2622/

24 G. Kresse and J. Furthmüller,
Physical Review B 54, 11169 (Oct 1996),
http://link.aps.org/doi/10.1103/PhysRevB.54.11169

25 J. Hafner, Journal of Computational Chemistry
29, 2044 (2008), ISSN 1096-987X,
http://dx.doi.org/10.1002/jcc.21057

26 G. Kresse and D. P. Joubert,
Physical Review B 59, 1758 (Jan 1999),
http://link.aps.org/doi/10.1103/PhysRevB.59.1758

27 W. Kohn and L. J. Sham,
Physical Review 140, A1133 (Nov 1965),
http://link.aps.org/doi/10.1103/PhysRev.140.A1133

28 H. J. Monkhorst and J. D. Pack,
Physical Review B 13, 5188 (Jun 1976),
http://link.aps.org/doi/10.1103/PhysRevB.13.5188

29 O. Jepson and O. Anderson, Solid State Communications
9, 1763 (1971), ISSN 0038-1098,
http://www.sciencedirect.com/science/article/pii/0038109871903139

30 G. Lehmann and M. Taut, physica status solidi (b)
54, 469 (1972), ISSN 1521-3951,
http://dx.doi.org/10.1002/pssb.2220540211

31 P. E. Blöchl, O. Jepsen, and O. K. Ander-
sen, Physical Review B 49, 16223 (Jun 1994),
http://link.aps.org/doi/10.1103/PhysRevB.49.16223

32 M. Methfessel and A. T. Paxton,
Physical Review B 40, 3616 (Aug 1989),
http://link.aps.org/doi/10.1103/PhysRevB.40.3616

33 J. P. Perdew, K. Burke, and M. Ernzerhof,
Physical Review Letters 77, 3865 (Oct 1996),
http://link.aps.org/doi/10.1103/PhysRevLett.77.3865

34 J. P. Perdew, K. Burke, and M. Ernzerhof,
Physical Review Letters 78, 1396 (Feb 1997),
http://link.aps.org/doi/10.1103/PhysRevLett.78.1396

35 M. Ernzerhof and G. E. Scuseria,
The Journal of Chemical Physics 110, 5029 (1999),
http://link.aip.org/link/?JCP/110/5029/1

36 A. D. Becke, Physical Review A 38, 3098 (Sep 1988),
http://link.aps.org/doi/10.1103/PhysRevA.38.3098

37 J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A.
Jackson, M. R. Pederson, D. J. Singh, and C. Fi-
olhais, Physical Review B 46, 6671 (Sep 1992),
http://link.aps.org/doi/10.1103/PhysRevB.46.6671

38 J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A.
Jackson, M. R. Pederson, D. J. Singh, and C. Fi-
olhais, Physical Review B 48, 4978 (Aug 1993),
http://link.aps.org/doi/10.1103/PhysRevB.48.4978.2

39 P. E. Blöchl, Physical Review B 50, 17953 (Dec 1994),
http://link.aps.org/doi/10.1103/PhysRevB.50.17953

40 F. Birch, Physical Review 71, 809 (Jun 1947),
http://link.aps.org/doi/10.1103/PhysRev.71.809

41 M. Gajdoš and K. Hummer and G. Kresse
and J. Furthmüller and F. Bechstedt,
Physical Review B 73, 045112 (Jan 2006),
http://link.aps.org/doi/10.1103/PhysRevB.73.045112

42 W. G. Aulbur, L. Jönsson, and J. W.
Wilkins (Academic Press, 1999) pp. 1 - 218,
http://www.sciencedirect.com/science/article/pii/S0081194708602829

43 J. Kohanoff, Electronic Structure Calculations for Solids
and Molecules : Theory and Computational Methods
(Cambridge University Press; Cambridge, 2006)

44 J. Harl, The Linear Response Function in Density Func-
tional Theory: Optical Spectra and Improved Description
of the Electron Correlation, Ph.D. thesis, University of Vi-
enna (2008)

45 L. Hedin, Phys. Rev. 139, A796 (Aug 1965),
http://link.aps.org/doi/10.1103/PhysRev.139.A796

46 G. Kresse, M. Marsman, and J. Furthmuller,
"Vasp the guide," (2011), available on-line at
http://cms.mpi.univie.ac.at/vasp/vasp/. Last ac-
cessed October 2012.

47 M. Fox, Optical Properties of Solids, Oxford Master Se-
ries in Physics: Condensed Matter Physics (Ox-
ford University Press, 2010) ISBN 9780199573363,
http://books.google.co.za/books?id=-5bVBbAoaGoC

48 M. Dressel and G. Grüner,
Electrodynamics of solids : optical properties of electrons in matter
(Cambridge University Press, Cambridge New York, 2002)
ISBN 0521592534

49 A. Miller, in Handbook of Optics, Volume 1: Fundamentals, Techniques
Optical Society of America (McGraw-Hill, Inc., New York,
NY, USA, 2010) ISBN 0070479747, 9780070479746

50 Donohue, The structures of the elements,
A Wiley-interscience publication (John Wi-
ley & Sons Inc., 1974) ISBN 0471217883,
http://books.google.co.za/books?id=Q-rvAAAAAAJ

51 C. Kittel, Introduction to Solid State Physics, eigth ed.
(John Wiley & Sons, Inc., 2005) ISBN 9780471415268,
http://books.google.co.za/books?id=kym4QgAACAAJ

52 S. Raju, E. Mohandas, and V. Raghunathan, J. Phys.
Chem Solids 58, 1367 (1997)

53 M. J. Mehl and D. A. Papaconstantopou-
los, Physical Review B 54, 4519 (Aug 1996),
http://link.aps.org/doi/10.1103/PhysRevB.54.4519

54 E. Zarechnaya, N. Skorodumova, S. Simak, B. Johans-
son, and E. Isaev, Computational Materials Science
43, 522 (2008), ISSN 0927-0256,
http://www.sciencedirect.com/science/article/pii/S0927025608

55 U. Hahn and W. Weber,
Physical Review B 53, 12684 (May 1996),
http://link.aps.org/doi/10.1103/PhysRevB.53.12684

56 G. Grimvall, Thermophysical Properties of Materials
(North Holland, 1986) http://books.google.co.za/books?id=TCWZ1g

57 M. S. H. Suleiman and D. P. Joubert, in
South African Institute of Physics $57^{th}$ An-
nual Conference (SAIP 2012), No. 298 (2012)
http://indico.saip.org.za/confSpeakerIndex.py?view=full&lette

58 M. S. H. Suleiman and D. P. Joubert, in
South African Institute of Physics $57^{th}$ An-
nual Conference (SAIP 2012), No. 299 (2012)
http://indico.saip.org.za/confSpeakerIndex.py?view=full&lette

59 J. von Appen, M.-W. Lumey, and R. Dron-
skowski, Angewandte Chemie International Edition
45, 4365 (2006), ISSN 1521-3773,
http://dx.doi.org/10.1002/anie.200600431

60 In their original article$^{16}$, Kanoun and Said stated
that "... there are two atom in wurtzite unit cell, and
one in all the other cases." which is a clear typo!

61 Z. Wu and R. E. Cohen,
Physical Review B 73, 235116 (Jun 2006),
http://link.aps.org/doi/10.1103/PhysRevB.73.235116

62 Scuseria, G. E. Scuseria, J. Tao, and J. P.
Perdew, Physical Review B 69, 075102 (Feb 2004),
http://link.aps.org/doi/10.1103/PhysRevB.69.075102

$^{63}$ J. P. Perdew and S. Kurth, in
*A Primer in Density Functional Theory*, Lecture Notes
in Physics (Springer, 2003) ISBN 9783540030836,
http://books.google.co.za/books?id=mX793GABep8C

$^{64}$ *Since Eq. 4 does not refer to any stoichiometry or
any species (that is, it does not consider the way
that the change in energy or volume was done), we
may take the change in volume (or energy) with re-
spect to itself, with respect to the parent $Ag(A1)$, or
with respect to any of the other nineteen considered
modifications.*

$^{65}$ *Surely, this needs not to be so. Compare the defini-
tion 3 with the definition 6.*

$^{66}$ *It is common that one obtains positive DFT for-
mation energy for (even the experimentally synthe-
sized) transition-metal nitrides. Moreover, the zero-
pressure zero-temperature DFT calculations have to
be corrected for the conditions of formation of these
nitrides. Another source of this apparent shortcom-
ing stems from the PBE-GGA underestimation of
the cohesion in $N_2$. We have discussed this point
further in Ref. 5.*

$^{67}$ C. J. Bradley and A. P. Cracknell, *The Mathematical
Theory of Symmetry in Solids: Representation Theory
for Point Groups and Space Groups* (Oxford: Clarendon
Press, 1972)

$^{68}$ D. Engin, C. Kemal, and C. Y. Oztekin,
Chinese Physics Letters **25**, 2154 (2008),
http://stacks.iop.org/0256-307X/25/i=6/a=063

$^{69}$ R. de Paiva, R. A. Nogueira, and J. L. A.
Alves, Physical Review B **75**, 085105 (Feb 2007),
http://link.aps.org/doi/10.1103/PhysRevB.75.085105

$^{70}$ M. G. Moreno-Armenta and G. Soto,
Solid State Sciences **10**, 573 (2008), ISSN 1293-2558,
http://www.sciencedirect.com/science/article/pii/S1293255807

$^{71}$ *Recall that the optical region (i.e. the visible spec-
trum) is about (390 $\sim$ 750) nm which corresponds to
(3.183 $\sim$ 1.655) $eV$.*

$^{72}$ M. Rohlfing and S. G. Louie,
Physical Review B **62**, 4927 (Aug 2000),
http://link.aps.org/doi/10.1103/PhysRevB.62.4927