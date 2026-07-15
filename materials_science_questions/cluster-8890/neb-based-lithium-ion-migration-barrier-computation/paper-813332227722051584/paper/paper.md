PHYSICAL REVIEW B 85, 064115 (2012)

# Mechanisms for the decomposition and dehydrogenation of Li amide/imide

Khang Hoang, $^{*}$ Anderson Janotti, and Chris G. Van de Walle $^{\dagger}$

Materials Department, University of California, Santa Barbara, California 93106-5050, USA
(Received 16 August 2011; revised manuscript received 6 December 2011; published 22 February 2012)

Reversible reaction involving Li amide $(LiNH_{2})$ and Li imide $(Li_{2} NH)$ is a potential mechanism for hydrogen storage. Recent synchrotron x-ray diffraction experiments [W. I. David et al., J. Am. Chem. Soc. 129, 1594(2007)] suggest that the transformation between $LiNH_{2}$ and $Li_{2} NH$ is a bulk reaction that occurs through nonstoichiometric processes and involves the migration of $Li^{+}$ and $H^{+}$ ions. In order to understand the atomistic mechanisms behind these processes, we carry out comprehensive first-principles studies of native point defects and defect complexes in the two compounds. We find that both $LiNH_{2}$ and $Li_{2} NH$ are prone to Frenkel disorder on the Li sublattice. Lithium interstitials and vacancies have low formation energies and are highly mobile, and therefore play an important role in mass transport and ionic conduction. Hydrogen interstitials and vacancies, on the other hand, are responsible for forming and breaking N-H bonds, which is essential in the Li amide/imide reaction. Based on the structure, energetics, and migration of hydrogen-, lithium-, and nitrogen-related defects, we propose that $LiNH_{2}$ decomposes into $Li_{2} NH$ and $NH_{3}$ according to two competing mechanisms with different activation energies: one mechanism involves the formation of native defects in the interior of the material, the other at the surface. As a result, the prevailing mechanism and hence the effective activation energy for decomposition depend on the surface-to-volume ratio or the specific surface area, which changes with particle size during ball milling. These mechanisms also provide an explanation for the dehydrogenation of $LiNH_{2}+LiH$ mixtures.

DOI: 10.1103/PhysRevB.85.064115
PACS number(s): 61.72.J-, 66.30.hd, 82.30.Lp, 88.30.R-

## I. INTRODUCTION

Hydrogen is a promising energy carrier in future energy systems, but storage of hydrogen is still a major challenge. $^{1}$ Lithium amide $(LiNH_{2})$ is a promising material due to its high hydrogen density. Lithium imide $(Li_{2} NH)$ is known for its high ionic conductivity $(3 ×10^{-4} S / cm$ at $25^{\circ} C)^{2}$ These two compounds have attracted a lot of attention ever since Chen et al. $^{3}$ demonstrated that $Li_{3} N$ can absorb/desorb hydrogen atreasonable pressures following the reversible reaction:

$$
\begin{aligned}
\mathrm{Li}_{3} \mathrm{~N}+2 \mathrm{H}_{2} \leftrightarrow \mathrm{Li}_{2} \mathrm{NH}+\mathrm{LiH}+\mathrm{H}_{2} \leftrightarrow \mathrm{LiNH}_{2}+2 \mathrm{LiH}.
\end{aligned}
$$

The theoretical amount of reversible hydrogen storage in this reaction is $11.5 wt \%$ (expressed per mole of $Li_{3} N$ ). At temperatures below $300^{\circ} C, LiNH_{2}$ was observed to reversibly store $6.5 wt \%$ hydrogen during desorption and absorptionunder 0.04 and 20 bar, respectively, following the reaction: $^{3}$ 

$$
\mathrm{LiNH}_{2}+\mathrm{LiH} \leftrightarrow \mathrm{Li}_{2} \mathrm{NH}+\mathrm{H}_{2}. \quad (2)
$$

The drawback of this Li amide/imide reaction is that the dehydrogenation temperature and hydrogenation pressure are relatively high for practical applications. Yet, the fundamental mechanisms behind the decomposition and (de)hydrogenation processes are not fully understood, and we expect that once such understanding has been established, one can provide solutions for speeding up the reaction kinetics and lowering the dehydrogenation temperature and hydrogenation pressure.

Regarding the dehydrogenation reaction in Eq. (2), it has been suggested that $LiNH_{2}$ may react directly with LiH at the $LiNH_{2} / LiH$ interface according to a polar mechanism to produce $H_{2} \cdot^{3-5}$ The mechanism is explained in terms of thestrong affinity between protonic hydrogen $(H^{\delta+})$ in $LiNH_{2}$  and hydridic hydrogen $(H^{\delta-})$ in LiH where the redox reaction of $H^{\delta+}$ and $H^{\delta-}$ produces molecular hydrogen $(H_{2})^{4}$ Thermal desorption measurements carried out on a $LiNH_{2}+2 LiD$  mixture, however, showed that it produces mainly $H_{2}$ in addition to HD and $D_{2}$ (instead of mainly HD as one would have expected). $^{4}$ This seems to be contrary to the redox hypothesis.

Others have proposed that $NH_{3}$ necessarily evolves as a transient gas and the dehydrogenation of $LiNH_{2}+LiH$ mixtures involves an intermediate step: $^{6-13}$ 

$$2 \mathrm{LiNH}_{2} \to \mathrm{Li}_{2} \mathrm{NH}+\mathrm{NH}_{3}, \quad (3)$$

$$\mathrm{NH}_{3}+\mathrm{LiH} \to \mathrm{LiNH}_{2}+\mathrm{H}_{2}. \quad (4)$$

The first reaction releases $37 wt \% NH_{3}$ and was suggested to be diffusion-controlled, whereas the second reaction releases5.8 wt% H2 and is supposedly ultrafast. The decomposition of $LiNH_{2}$ into $Li_{2} NH$ and $NH_{3}$ is well known, $^{4,7,8}$ and it was Hu and Ruckenstein who pointed out that $NH_{3}$ reacts quickly with $LiH^{6,7}$ The activation energy for the decomposition of LiNH2 was estimated to be 2.53 eV (before ball milling), andit was found to decrease with increasing ball-milling time. $^{14}$  The above two-step pathway is supported by recent studiesusing variable-temperature in situ $^{1} H$ NMR spectroscopy. $^{15}$ 

As noted by David et al., $^{16}$ there are very close structural similarities between the tetragonal $LiNH_{2}$ and the antifluo rite $Li_{2} NH$ . Through structural refinement from synchrotron x-ray diffraction data, they suggested that the transformation between $LiNH_{2}$ and $Li_{2} NH$ is a bulk reaction that occurs through nonstoichiometric processes within the cubic Li-N-H structure. David et al. further proposed a mechanism for the Li amide/imide decomposition and hydrogenation processes(within the abovementioned ammonia-mediated two-step re-action) that involves the migration of both $Li^{+}$ and $H^{+}$ ions; they also suggested that the nonstoichiometry observed in the Li-N-H system is a direct result of the ionic mobility. The most important step in this mechanism would be the movement of

1098-0121/2012/85(6)/064115(12)
064115-1
©2012 American Physical Society

a lithium ion to an interstitial site, forming a lithium Frenkel defect pair. $^{16}$

In addition to the polar mechanism and the ammonia- mediated mechanism, Aguey-Zinsou et al. $^{17}$ have recently suggested that the reaction between $LiNH_{2}$ and $LiH$ below $300\ ^{\circ}\text{C}$ is a heterogeneous solid-state reaction, controlled by the diffusion of $Li^{+}$ from $LiH$ to $LiNH_{2}$ across the interface. In this mechanism, the reaction is direct rather than ammonia-mediated. $^{17}$

Theoretical studies of $LiNH_{2}$ and $Li_{2}NH$ to date have focused mainly on structural, electronic, and thermodynamic properties of the bulk compounds. $^{18-24}$ Experimental data, $^{16}$ on the other hand, suggest that the rate-limiting process in the Li amide/imide reaction involves mass transport mediated by point defects. This scenario motivated us to perform first- principles calculations for point defects and defect complexes in $LiNH_{2}$ and $Li_{2}NH$ in order to explore possible defect related mechanisms that can explain the decomposition of $LiNH_{2}$ [reaction (3)] and the hydrogenation of $Li_{2}NH$. Some preliminary results and partial conclusions of our work have been reported elsewhere. $^{25}$ Other research groups have also recently started investigating native defects, $^{26-28}$ but our study goes much further in identifying specific mechanisms that can explain the experimental observations. A detailed comparison with the previous papers will be addressed in Secs. $\text{IV A} 3$ and $\text{V B}$.

Indeed, we show that $LiNH_{2}$ decomposes into $Li_{2}NH$ and $NH_{3}$ via two competing mechanisms with different activation energies: one mechanism involves the formation of native defects in the interior of the material and the other at the surface. As a result, the prevailing mechanism and hence the effective activation energy for decomposition depend on the surface-to-volume ratio or the specific surface area, which changes with particle size during ball milling. The dehydrogenation of $LiNH_{2}+LiH$ mixtures can be explained in terms of the two-step reaction [see Eqs. (3) and (4)] and the mechanisms we propose for $LiNH_{2}$ decomposition. However, $NH_{3}$ is not necessarily formed and released from a $LiNH_{2}+LiH$ mixture if $LiNH_{2}$ and $LiH$ are in intimate contact.

We also show that lithium interstitials and vacancies in $LiNH_{2}$ and $Li_{2}NH$ can be formed in the interior of the materials via a Frenkel-pair mechanism and are highly mobile, and that Li amide (imide) units can be locally formed inside the bulk Li imide (amide). Our results support David et al.'s proposal that the Li amide/imide is a bulk reaction, and that there is a continuous transformation between $LiNH_{2}$ and $Li_{2}NH$ via nonstoichiometric intermediates. $^{16}$ It is, however, not the formation and migration of lithium-related defects that is the rate-limiting step in the kinetics of the Li amide/imide reaction, but the formation and migration of hydrogen interstitials and vacancies that are responsible for forming and breaking N-H bonds in $LiNH_{2}$ (and $Li_{2}NH$).

The remainder of this paper is arranged as follows: in Sec. $\text{II}$, we provide technical details of the calculations and present the theoretical approach. Bulk properties of $LiNH_{2}$ and $Li_{2}NH$ are discussed in Sec. $\text{III}$. In Secs. $\text{IV}$ and $\text{V}$, we present the results for native defects and discuss their relevance to ionic conduction in $LiNH_{2}$ and $Li_{2}NH$, decomposition of $LiNH_{2}$, dehydrogenation of $LiNH_{2}+LiH$ mixtures, and hydrogenation of $Li_{2}NH$. A summary in Sec. $\text{VI}$ concludes the paper.

## II. METHODOLOGY

### A. Computational details

Our calculations were based on density-functional theory within the generalized-gradient approximation (GGA) $^{29}$ and the projector augmented wave method, $^{30,31}$ as implemented in the VASP code. $^{32-34}$ Calculations for bulk $LiNH_{2}$ (tetragonal $I\overline{4}$, 32 atoms/unit cell) were performed using a $10\times10\times5$ Monkhorst-Pack $\mathbf{k}$-point mesh, $^{35}$ and for $Li_{2}NH$ (orthorhombic $Pbca$, 32 atoms/unit cell) we used a $10\times5\times10$ $\mathbf{k}$-point mesh. For defect calculations, we used a $(2\times2\times1)$ supercell for $LiNH_{2}$ and a $(2\times1\times2)$ supercell for $Li_{2}NH$, both corresponding to 128 atoms/cell, and a $2\times2\times2$ $\mathbf{k}$-point mesh and plane-wave basis set cutoff of 400 eV. In these calculations, the lattice parameters were fixed to the calculated bulk values, but all the internal coordinates were fully relaxed. Convergence with respect to self-consistent iterations was assumed when the total energy difference between cycles was less than $10^{-4}$ eV and the residual forces were better than $0.01\ \text{eV}/\mathring{A}$. The migration of selected native point defects in $LiNH_{2}$ and $Li_{2}NH$ was studied using the climbing image nudged elastic band method (NEB). $^{36}$

### B. Defect formation energies

Throughout the paper, we will use defect formation energies to characterize different native defects in $LiNH_{2}$ and $Li_{2}NH$. The formation energy $(E^{f})$ of a defect is a crucial factor in determining its concentration. In thermal equilibrium, the concentration of the defect X at temperature $T$ can be obtained via the relation $^{37,38}$

$$
c(\mathrm{X})=N_{\text{sites}}N_{\text{config}}\exp[-E^{f}(\mathrm{X})/k_{B}T],\qquad(5)
$$

where $N_{\text{sites}}$ is the number of high-symmetry sites in the lattice per unit volume on which the defect can be incorporated, and $N_{\text{config}}$ is the number of equivalent configurations (per site). Note that the energy in Eq. (5) is, in principle, a free energy; however, the entropy and volume terms are often neglected because they are negligible at relevant experimental conditions. $^{38}$ It emerges from Eq. (5) that defects with low formation energies will easily form and occur in high concentrations.

The formation energy of a defect X in charge state $q$ is defined as $^{37,39}$

$$
\begin{aligned}
E^{f}(\mathrm{X}^{q})= & E_{\text{tot}}(\mathrm{X}^{q})-E_{\text{tot}}(\text{bulk})-\sum_{i}n_{i}\mu_{i} \\
& +q(E_{\text{v}}+\Delta V+\mu_{e}),\qquad(6)
\end{aligned}
$$

where $E_{\text{tot}}(\mathrm{X}^{q})$ and $E_{\text{tot}}$(bulk) are, respectively, the total energies of a supercell containing the defect X and of a supercell of the perfect bulk material, $\mu_{i}$ is the atomic chemical potential of species $i$ (referenced to the standard state), and $n_{i}$ denotes the number of atoms of species $i$ that have been added ($n_{i}>0$) or removed ($n_{i}<0$) to form the defect. $\mu_{e}$ is the electron chemical potential, i.e., the Fermi level, referenced to the valence-band maximum in the bulk $(E_{\text{v}})$. $\Delta V$ is the "potential alignment" term, i.e., the shift in the

band positions due to the presence of the charged defect and the neutralizing background, obtained by aligning the average electrostatic potential in regions far away from the defect to the bulk value. $^{37}$

### C. Chemical potentials
We note that the atomic chemical potentials $\mu_i$ are variables and can be chosen to represent experimental conditions. Given the reported continuous transformation between $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$, $^{16}$ for reactions (2) and (3), it is reasonable to assume that the two compounds are in equilibrium, i.e., the chemical potentials simultaneously satisfy:

$$
\mu_{\mathrm{Li}}+\mu_{\mathrm{N}}+2 \mu_{\mathrm{H}}=\Delta H_{f}\left(\mathrm{LiNH}_{2}\right),\qquad(7)
$$

$$
2 \mu_{\mathrm{Li}}+\mu_{\mathrm{N}}+\mu_{\mathrm{H}}=\Delta H_{f}\left(\mathrm{Li}_{2} \mathrm{NH}\right),\qquad(8)
$$

where $\Delta H_f$ is the enthalpy of formation. The calculated formation enthalpies (at $T=0$ K) are $-2.065$ and $-2.091$ eV for $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$, respectively, in good agreement with previously reported values. $^{18,22,40,41}$

From Eqs. (7) and (8), the chemical potentials of Li and N can be expressed in terms of $\mu_{\mathrm{H}}$, which is now the only variable. The temperature and pressure values at which the dehydrogenation and hydrogenation processes occur then determine the chemical potential of H through equilibrium with $\text{H}_2$ gas. In the following discussion, we employ a set of conditions used by David *et al.* in their experiments, i.e., we use $10^{-3}$ bar and $260~^\circ\text{C}$ for hydrogen desorption, and 3 bar and $260~^\circ\text{C}$ for absorption. $^{16}$ These conditions correspond to $\mu_{\mathrm{H}}=-0.49$ and $-0.31$ eV, respectively. $^{42}$ Two different sets of experimental conditions will be analyzed. $\mu_{\mathrm{H}}=-0.49$ eV corresponds to the dehydrogenation process and is therefore appropriate for analysis of defects in $\text{LiNH}_2$. $\mu_{\mathrm{H}}=-0.31$ eV, on the other hand, corresponds to the hydrogen absorption process, and is therefore the value we will use for analysis of defects in $\text{Li}_2\text{NH}$.

One can, of course, choose a different set of atomic chemical potentials which corresponds to different experimental conditions, and this may affect the relative formation energy between different defects. These formation energies can easily be obtained from the data we report. However, we have checked that the details of the choice we made here do not affect the physics of the mechanisms we are presenting.

## III. BULK PROPERTIES
$\text{LiNH}_2$ was reported to crystallize in the tetragonal space group $I\overline{4}.^{20}$ The crystal structure of $\text{Li}_2\text{NH}$ was, however, difficult to resolve. Using x-ray diffraction, Juza and Opp proposed that $\text{Li}_2\text{NH}$ had an antifluorite structure with the $Fm\overline{3}m$ symmetry, $^{43}$ but they were unable to obtain the positions of the hydrogen ions. More recent experimental studies suggested that hydrogen randomly occupies one of the sites around the nitrogen ion. $^{44,45}$

On the theory side, significant efforts have been focused on finding low-energy ordered structures for $\text{Li}_2\text{NH}$ and several structural models have been proposed. $^{18,22,23}$ Among these models, the orthorhombic structure with the $Pbca$ symmetry proposed by Mueller and Ceder was shown to have the lowest energy. $^{22}$ We therefore employ this structure for our current studies of $\text{Li}_2\text{NH}$.

![](./images/813332227722051584_1.jpg)

FIG. 1. (Color online) Relaxed structures of (a) tetragonal $\text{LiNH}_2$ and (b) orthorhombic $\text{Li}_2\text{NH}$. Large (gray) spheres are Li, medium (blue) spheres N, and small (red) spheres H. Inequivalent atoms are labeled as H1, H2, Li1, Li2, and Li3.

The optimized structures of $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$ are shown in Figs. 1(a) and 1(b). For $\text{LiNH}_2$, the calculated lattice parameters are $a=b=5.053$ Å, and $c=10.304$ Å, in satisfactory agreement with experimental values ($a=b=5.034$ Å, $c=10.256$ Å).$^{20}$ For $\text{Li}_2\text{NH}$, we find $a=5.134$ Å, $b=10.461$ Å, and $c=5.28$ Å, in good agreement with the values reported by Mueller and Ceder. $^{22}$

We can consider the bonding in $\text{LiNH}_2$ as composed of $(\text{Li})^+$ and $(\text{NH}_2)^-$ units, like the ionic bonding in NaCl; the $(\text{NH}_2)^-$ units are surrounded by $(\text{Li})^+$ and vice versa. Similarly, $\text{Li}_2\text{NH}$ can be regarded as composed of $(\text{Li})^+$ and $(\text{NH})^{2-}$ units, where for each $(\text{NH})^{2-}$ unit there are two $(\text{Li})^+$ units. This picture will be useful when we discuss the energetics and local geometry of various defects in $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$.

Figure 2 shows the calculated band structure of tetragonal $\text{LiNH}_2$ along the high-symmetry directions of the Brillouin zone (BZ). We find an indirect band gap of 3.17 eV with the valence-band maximum (VBM) at the $M$ point and the conduction-band minimum (CBM) at the $\Gamma$ point. Band-gap values ranging from $\sim$3 to 3.48 eV have been reported for $\text{LiNH}_2$. $^{18-20}$ An analysis of the wave functions shows that the VBM is composed of N-related unbonded states from the $(\text{NH}_2)^-$ units, whereas the CBM is composed of a mixture of N $p$ and H $s$ states.

Figure 3 shows the calculated band structure of orthorhombic $\text{Li}_2\text{NH}$ along the high-symmetry directions of the orthorhombic BZ. We find a direct band gap of 2.26 eV at the $\Gamma$ point. Similar to $\text{LiNH}_2$, the VBM of $\text{Li}_2\text{NH}$ is composed mostly of N-related unbonded states from the $(\text{NH})^{2-}$ units, whereas the CBM is composed of N $p$ and H $s$ states. Previous studies reported a band gap of 2.65 eV for $\text{Li}_2\text{NH}$. $^{24}$ To the best of our knowledge, no experimental information on the band gaps of $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$ is available. As we illustrate

![](./images/813332227722051584_2.jpg)

FIG. 2. (Color online) Band structure of tetragonal LiNH₂ along the high-symmetry directions of the tetragonal BZ. The VBM is at the M point, whereas the CBM is at the Γ point. The zero of energy is set to the highest occupied state.

in Sec. IV, knowing the nature of the electronic states near the VBM and CBM is extremely helpful in understanding the formation of defects in these systems.

## IV. POINT DEFECTS AND COMPLEXES

We investigated hydrogen-, lithium-, and nitrogen-related point defects in all the possible charge states in LiNH₂ and Li₂NH. Defect complexes were also considered, with special attention to Frenkel pairs, i.e., interstitial-vacancy pairs of the same species. Defect formation energies and migration barriers were obtained using the methods described in Sec. II. We also discuss the role of these native defects in mass transport and ionic conduction in LiNH₂ and Li₂NH.

### A. LiNH₂
#### 1. Hydrogen-related defects

Figure 4 shows the calculated formation energies for hydrogen vacancies ($V_{\text{H}}$), interstitials ($H_{i}$), and interstitial molecules $(\text{H}_{2})_{i}$ in LiNH₂. Among these native defects, the negatively charged hydrogen vacancy ($V_{\text{H}}^{-}$) and positively charged hydrogen interstitial ($H_{i}^{+}$) have the lowest formation energies over the entire range of Fermi-level values. The neutral hydrogen vacancy ($V_{\text{H}}^{0}$) and interstitial ($H_{i}^{0}$) are high in energy. The formation energy of $(\text{H}_{2})_{i}$ is also higher than that of $V_{\text{H}}^{-}$ and $H_{i}^{+}$. The positively charged hydrogen vacancy ($V_{\text{H}}^{+}$, not included in Fig. 4) is unstable, i.e., a locally stable configuration of this defect cannot be stabilized. If we try to create $V_{\text{H}}^{+}$, it decays to a situation where the positive charge is not associated with the point defect but corresponds to free carriers in the valence band.

![](./images/813332227722051584_3.jpg)

FIG. 3. (Color online) Band structure of orthorhombic Li₂NH along the high-symmetry directions of the orthorhombic BZ. The VBM and CBM are at the Γ point. The zero of energy is set to the highest occupied state.

In order to understand the energetics of different hydrogen-related defects in LiNH₂, it is useful to refer back to the electronic structure and bonding geometry of LiNH₂. For example, the creation of $V_{\text{H}}$ involves breaking an N-H bond from the $(\text{NH}_{2})^{-}$ unit, resulting in an NH unit. Since the NH unit is most favorable in the $(\text{NH})^{2-}$ configuration due to the high electronegativity of the N atom, it is expected that $V_{\text{H}}$ will be most stable in the $V_{\text{H}}^{-}$ configuration. Formation of $V_{\text{H}}^{0}$, on the other hand, would involve removing one electron from the resulting $(\text{NH})^{2-}$ unit, which is energetically highly unfavorable. Figure 4 indeed shows $V_{\text{H}}^{-}$ to be the most stable configuration.

The creation of $H_{i}^{0}$ or $H_{i}^{+}$ leads to the formation of an $\text{NH}_{3}$ unit, which is an $(\text{NH}_{2})^{-}$ unit with an extra H atom. Since $\text{NH}_{3}$ forms a closed-shell unit, the interstitial is expected to be most stable in the $H_{i}^{+}$ configuration, in which the additional electron [which stabilized $(\text{NH}_{2})^{-}$ but is now superfluous] is removed. $H_{i}^{-}$, on the other hand, prefers to stay in an interstitial void, with distances of 1.91 and 2.14 Å to the two nearest Li atoms. Finally, the creation of $(\text{H}_{2})_{i}$ involves adding an $\text{H}_{2}$ molecule to the system. This interstitial molecule prefers to stay near the center of the octahedron formed by six $\text{NH}_{2}$ units, with the calculated H-H bond length being 0.75 Å, very close to that calculated for an isolated $\text{H}_{2}$ molecule.

For the migration of $H_{i}^{+}$, $H_{i}^{-}$, $V_{\text{H}}^{-}$, and $(\text{H}_{2})_{i}$, we find energy barriers of 0.61, 0.34, 0.71, and 0.19 eV, respectively. The energy barriers for $H_{i}^{+}$ and $V_{\text{H}}^{-}$ are relatively high because the migration of these two defects involves breaking N—H bonds. For $H_{i}^{+}$, an H atom in the $\text{NH}_{3}$ unit moves to the nearest $\text{NH}_{2}$.

![](./images/813332227722051584_4.jpg)

FIG. 4. (Color online) Calculated formation energies of hydrogen-related defects in LiNH₂, plotted as a function of Fermi energy with respect to the VBM.

![](./images/813332227722051584_5.jpg)

FIG. 5. (Color online) Structure of (a) $(H_i^+,V_H^-)$, (b) $Li_H^0$, and (c) $(Li_i^+,V_{Li}^-)$ in $LiNH_2$. Large (gray) spheres are Li, medium (blue) spheres N, and small (red) spheres H. The vacancies are represented by an empty sphere.

The saddle-point configuration consists of an H atom located midway between two $NH_2$ units (i.e., $NH_2$-$H$-$NH_2$). Similarly, the migration of $V_H^-$ involves moving an H atom from a nearby $NH_2$ unit to the vacancy. The saddle-point configuration in this case consists of a hydrogen atom located midway between two NH units (i.e., $NH$-$H$-$NH$). $H_i^-$ and $(H_2)_i$, on the other hand, can migrate without breaking and forming bonds, explaining their relatively low migration barriers. We note that the bond length of the $H_2$ dimer is preserved along the migration path of $(H_2)_i$.

We also investigated the formation of Frenkel pairs composed of $H_i$ and $V_H$. The possible hydrogen-related Frenkel pairs are $(H_i^+,V_H^-)$ and $(H_i^-,V_H^+)$; the latter is not considered, since $V_H^+$ is unstable. Figure 5(a) shows the structure of $(H_i^+,V_H^-)$ in $LiNH_2$. The configurations of the individual defects are preserved in this complex, i.e., $H_i^+$ forms an $NH_3$ unit and the creation of $V_H^-$ leaves an $(NH)^{2-}$ unit. The distance between the two N ions in the pair is $3.37$ Å, very close to the N-N distance in the bulk ($3.38$ Å). This Frenkel pair has a formation energy of $1.54$ eV and a binding energy of $0.38$ eV (with respect to the isolated constituents). We note that these quantities are independent of the choice of chemical potentials.

## 2. Lithium-related defects

Figure 6 shows the calculated formation energies for lithium vacancies ($V_{Li}$), interstitials ($Li_i$), $Li_H^0$ (Li replacing an H atom), and $H_{Li}^0$ (H replacing an Li atom) in $LiNH_2$. Among the lithium-related defects, $Li_i^+$ and $V_{Li}^-$ have the lowest formation energies for all the Fermi-level values, except for a very small range near $\mu_e=2.49$ eV, where $Li_H^0$ has a slightly lower formation energy. $V_{Li}^+$ and $Li_i^-$ are unstable, $V_{Li}^0$ and $Li_i^0$ and not shown in Fig. 6.

In the case of $V_{Li}^-$, a $Li^+$ ion was removed from the Li3 site (cf. Fig. 1), whereas for $Li_i^+$, a $Li^+$ ion was placed in the void formed by two $NH_2$ units where one of the two N-H bonds in each $NH_2$ unit points toward the interstitial Li atom. We find that these defects lead to structural relaxations such that the neighboring Li atoms and $NH_2$ units are slightly displaced and rotated.

The formation of $Li_H^0$, on the other hand, results in an NH unit and a Li atom in the nearby region; see Fig. 5(b). $Li_H^0$ can indeed be regarded as a complex of $V_H^-$ and $Li_i^+$. The formation energy of $Li_H^0$ is lower than the sum of the formation energies of $Li_i^+$ and $V_H^-$ by 0.66 eV. In addition, considering the presence of the $(NH)^{2-}$ unit and the additional $Li^+$ ion, the region that includes $Li_H^0$ can be locally considered as $Li_2NH$ inside bulk $LiNH_2$.

Finally, $H_{Li}^0$ was created by replacing a Li atom with an H atom. This leaves the system with an $NH_3$ unit and a Li vacancy. $H_{Li}^0$ can be regarded as a complex of $H_i^+$ and $V_{Li}^-$ with a binding energy of 0.62 eV. Note that, if equilibrium between $LiNH_2$ and $Li_2NH$ is assumed, the formation energies of $Li_H^0$ and $H_{Li}^0$ are independent of the chemical potentials because the chemical potential terms in their formation energies occur as $(-\mu_{Li}+\mu_H)$, which is a constant, as seen from Eqs. (7) and (8).

The migration of $Li_i^+$ involves moving the $Li^+$ ion between two ground-state configurations, giving an energy barrier as low as 0.30 eV. For $V_{Li}^-$, the migration involves moving $Li^+$ from a nearby lattice site to the vacancy and this gives a barrier of 0.20 eV. These values are relatively small, suggesting that $Li_i^+$ and $V_{Li}^-$ are highly mobile. For $Li_H^0$, which is a complex of $Li_i^+$ and $V_H^-$, a lower bound on the migration barrier is given by the migration barrier of the least mobile constituent,⁴⁶ i.e., 0.71 eV, the value for $V_H^-$. Similarly, the migration barrier of $H_{Li}^0$ is estimated to be 0.61 eV, the value for $H_i^+$.

We also investigated possible formation of lithium Frenkel pairs. Since $Li_i^-$ and $V_{Li}^+$ are unstable, the only possibility is $(Li_i^+,V_{Li}^-)$, whose structure is shown in Fig. 5(c). The distance between $Li_i^+$ and $V_{Li}^-$ is $0.85$ Å. This pair has a formation energy of 0.65 eV and a binding energy of 0.36 eV. The formation energy is, therefore, much lower than that of the hydrogen

![](./images/813332227722051584_6.jpg)

FIG. 6. (Color online) Calculated formation energies of lithium-related defects in $LiNH_2$, plotted as a function of Fermi energy with respect to the VBM.

![](./images/813332227722051584_7.jpg)

FIG. 7. (Color online) Calculated formation energies of nitrogen-related defects in $LiNH_2$, plotted as a function of Fermi energy with respect to the VBM.

Frenkel pair, i.e., $(H_i^+,V_H^-)$. This result indicates that $LiNH_2$ is likely to exhibit Frenkel disorder on the Li sublattice.

### 3. Nitrogen-related defects

Figure 7 shows the calculated formation energies of nitrogen vacancies $(V_N)$, NH vacancies $(V_{NH})$, and $NH_2$ vacancies $(V_{NH_2})$ in $LiNH_2$. We find that $V_{NH_2}$ is stable as $V_{NH_2}^+$, and $V_{NH}$ is stable in the neutral charge state $(V_{NH}^0)$. $V_N$ is stable as $V_N^+$ and $V_N^-$. We also investigated interstitial $NH_3$ molecules but found them to have a very high formation energy (not included in Fig. 7), $E^f=2.54$ eV for the chosen set of chemical potentials. This suggests that ammonia is unlikely to form and diffuse through bulk $LiNH_2$ in the form of interstitial molecules.

$V_{NH_2}^+$ corresponds to the removal of an entire $(NH_2)^-$ unit from bulk $LiNH_2$. We find that there is very little change in the local lattice structure surrounding this defect. The formation of $V_{NH}^0$, on the other hand, leaves one H atom in the resulting void. This isolated H atom is surrounded by four Li atom with the Li-H distances in the range 1.95–2.15 Å. $V_{NH}^0$ can then be regarded as a complex of $V_{NH_2}^+$ and $H_i^-$ with a binding energy of 1.56 eV. Similarly, $V_N^+$ can be regarded as a complex composed of $V_{NH_2}^+$ and $(H_2)_i$ with a binding energy of 0.74 eV, and $V_N^-$ as a complex of $V_{NH_2}^+$ and two $H_i^-$ defects with a binding energy of 1.53 eV.

The migration of $V_{NH_2}^+$ involves moving a nearby $(NH_2)^-$ unit to the vacancy, with an energy barrier of 0.87 eV. For $V_{NH}^0$, which can be considered as a complex of $V_{NH_2}^+$ and $H_i^-$, a lower bound on the barrier is 0.87 eV, determined by the least mobile species, i.e., $V_{NH_2}^+$.

Other groups have recently reported first-principles calculations for native defects in $LiNH_2$, using methodologies similar to ours. $^{26-28}$ The calculated formation energies and migration barriers of individual hydrogen-, lithium-, and nitrogen-related defects reported by Wang et al. $^{28}$ are in close agreement with our results (to within 0.1 eV for most defects, with a maximum deviation of 0.2 eV in the case of $V_H^-$, our value being lower). Comparing to the results of Hazrati et al., $^{27}$ the deviations are somewhat larger (up to 0.4 eV), for which we cannot offer an explanation. Hazrati et al. did include vibrational zero-point energy corrections for those defects that involve hydrogen. However, while zero-point energies can be significant, a large degree of cancellation always occurs between the terms in the solid and in the reservoirs and the effect on formation energies is typically small. Miceli et al. did not report calculated formation energies of individual point defects. For the $(H_i^+,V_H^-)$ Frenkel pair, Hazrati et al. and Wang et al. reported formation energies of 1.66 and 1.93 eV, respectively, compared to 1.54 eV in our calculations. For the $(Li_i^+,V_{Li}^-)$ Frenkel pair, their reported values are 0.72 and 0.79 eV, whereas our calculated value is 0.65 eV. Miceli et al., on the other hand, reported a formation energy of 0.97 eV for the lithium Frenkel pair. We attribute the differences in the results for the Frenkel pairs to differences in the atomic configuration of the pairs. Our lower energies indicate that the configurations we identified are more stable.

![](./images/813332227722051584_8.jpg)

FIG. 8. (Color online) Calculated formation energies of hydrogen-related defects in $Li_2NH$, plotted as a function of Fermi energy with respect to the VBM.

### B. $Li_2NH$

#### 1. Hydrogen-related defects

Figure 8 shows the calculated formation energies for $H_i$, $V_H$, and $(H_2)_i$ in $Li_2NH$. Among the hydrogen-related defects, $H_i^+$ and $H_i^-$ have the lowest formation energies for the chosen set of chemical potentials. Neutral defects such as $V_H^0$ and $H_i^0$ are high in energy, and the formation energy of $(H_2)_i$ is also significantly higher than that of $H_i^+$ and $H_i^-$. The positively charged $V_H^+$ is unstable.

In $Li_2NH$, the removal of one H atom from an $(NH)^{2-}$ unit to form $V_H$ results in an isolated N atom. Since N has high electronegativity, it is expected that $V_H$ would be most stable in the $V_H^-$ configuration, consistent with our results shown in Fig. 8. The formation of $H_i^+$ results in an $(NH_2)^-$ unit. $H_i^-$, on the other hand, prefers to stay in an interstitial site near three Li atoms with the Li-H distances in the range 1.78–1.87 Å. Finally, $(H_2)_i$ stays in an interstitial void, with a calculated H-H bond length of 0.77 Å, comparable to but slightly larger than that calculated for an isolated $H_2$ molecule (0.75 Å).

Regarding the migration of the hydrogen-related defects, we find energy barriers of 0.95, 0.65, and 1.66 eV for $H_i^+$, $H_i^-$,

![](./images/813332227722051584_9.jpg)

FIG. 9. (Color online) Structure of (a) $(H_i^+,V_H^-)$, (b) $H_{Li}^0$, and (c) $(Li_i^+,V_{Li}^-)$ in $Li_2NH$. Large (gray) spheres are Li, medium (blue) spheres N, and small (red) spheres H. The vacancies are represented by an empty sphere.

and $V_H^-$, respectively. The migration barriers for $H_i^+$ and $V_H^-$ are again high, even higher than in $LiNH_2$, because the migration of these two defects involves breaking of N-H bonds. For $H_i^+$, the H attached to an NH unit moves to the nearest NH unit. The saddle-point configuration consists of an H atom located midway between two NH units, i.e., NH-H-NH. Likewise, the migration of $V_H^-$ involves moving an $H_i^+$ from an NH unit to the vacancy. The saddle-point configuration in this case consists of an H atom located midway between two N atoms, i.e., N-H-N.

Figure 9(a) shows the structure of the $(H_i^+,V_H^-)$ Frenkel pair in $Li_2NH$. Similar to the $(H_i^+,V_H^-)$ pair in $LiNH_2$, the configurations of individual defects are also preserved in this complex, i.e., $H_i^+$ forms an $NH_2$ unit and $V_H^-$ leaves the system with an isolated N atom. The distance between the two N atoms in the pair is $3.39\ \mathring{A}$, comparable to the N-N distance in the bulk $(3.31\ \mathring{A})$. $(H_i^+,V_H^-)$ has a formation energy of 1.32 eV and a binding energy of 0.14 eV. This low value of the binding energy suggests that, once created, the pair will easily dissociate.

### 2. Lithium-related defects
Figure 10 shows the calculated formation energies for $V_{Li}$, $Li_i$, $H_{Li}^0$ (H replacing a Li atom), and $Li_H^0$ (Li replacing a H atom) in $Li_2NH$. Among these defects, $Li_i^+$ and $V_{Li}^-$ have the lowest formation energies. $H_{Li}^0$ also has a relatively low formation energy. $V_{Li}^+$, $V_{Li}^0$, $Li_i^-$, and $Li_i^0$ are unstable. Note that, if equilibrium between $LiNH_2$ and $Li_2NH$ is assumed, the formation energies of $H_{Li}^0$ and $Li_H^0$ are independent of the chemical potentials, similar to the equivalent defects in $LiNH_2$.

$V_{Li}^-$ in $Li_2NH$ corresponds to the removal of a $(Li)^+$ unit from the system, whereas $Li_i^+$ can be thought of as the addition of a $Li^+$ ion to the system. These two defects result in relatively small local perturbations in the $Li_2NH$ lattice. The creation of $H_{Li}^0$, on the other hand, leaves the system with an $NH_2$ unit and a Li vacancy, as seen in Fig. 9(b). Thus, $H_{Li}^0$ can be regarded as a complex of $H_i^+$ and $V_{Li}^-$. The formation energy of $H_{Li}^0$ is lower than the sum of the formation energies of $H_i^+$ and $V_{Li}^-$ by 0.55 eV. Since the resulting defects are an $NH_2$ unit and a Li vacancy, the region that includes $H_{Li}^0$ can be considered as locally $LiNH_2$ inside bulk $Li_2NH$.

Finally, $Li_H^0$ was created by replacing an H atom with a Li atom. This results in an N atom standing near seven Li atoms with Li-N distances of less than $2.2\ \mathring{A}$. $Li_H^0$ can actually be considered as a complex of $Li_i^+$ and $V_H^-$ with a binding energy of 0.45 eV. This defect can act as a nucleation site for $Li_3N$ formation in the dehydrogenation reaction of $Li_2NH$. For comparison, the Li-N bonds are 1.94 and $2.11\ \mathring{A}$ in bulk $Li_3N$.

The migration barriers of $Li_i^+$ and $V_{Li}^-$ are 0.29 and 0.14 eV, respectively. For $H_{Li}^0$, which is a complex of $H_i^+$ and $V_{Li}^-$, we estimate a migration barrier of 0.95 eV, the value for $H_i^+$. Similarly, the migration barrier of $Li_H^0$ is estimated to be 1.66 eV, the value for $V_H^-$.

Figure 9(c) shows the structure of the $(Li_i^+,V_{Li}^-)$ Frenkel pair in $Li_2NH$. The distance between $Li_i^+$ and $V_{Li}^-$ is $3.13\ \mathring{A}$. The $(Li_i^+,V_{Li}^-)$ pair has a formation energy of 0.68 eV and a binding energy of 0.38 eV. The formation energy is much lower than that of the $(H_i^+,V_H^-)$ pair. This suggests that $Li_2NH$, like $LiNH_2$, is also prone to Frenkel disorder on the Li sublattice.

### 3. Nitrogen-related defects
Figure 11 shows the calculated formation energies for $V_N$ and $V_{NH}$ in $Li_2NH$. Of all the possible nitrogen-related defects, $V_N^+$ has the lowest formation energy for almost all Fermi-level values. $V_N^+$ can be regarded as a complex of $V_{NH}^{2+}$ and $H_i^-$ with a binding energy of 2.09 eV. The isolated H atom (i.e., $H_i^-$) is surrounded by six Li atom with the Li-H distances in the range $2.00$-$2.36\ \mathring{A}$. $V_N^0$ and $V_N^-$ have high formation energies and are thus unlikely to form.

$V_{NH}^{2+}$ in $Li_2NH$ is similar to $V_{NH_2}^+$ in $LiNH_2$, meaning they are both created by removing an entire anionic unit, i.e., $(NH_2)^-$ or

![](./images/813332227722051584_10.jpg)

FIG. 10. (Color online) Calculated formation energies of lithium-related defects in $Li_2NH$, plotted as a function of Fermi energy with respect to the VBM.

![](./images/813332227722051584_11.jpg)

FIG. 11. (Color online) Calculated formation energies of nitrogen-related defects in $\text{Li}_2\text{NH}$, plotted as a function of Fermi energy with respect to the VBM.

$(\text{NH})^{2-}$, from the bulk compounds. But, unlike $V_{\text{NH}_2}^{+}$ in $\text{LiNH}_2$, which was stable over a wide range of Fermi levels (see Fig. 7), $V_{\text{NH}}^{2+}$ in $\text{Li}_2\text{NH}$ is stable only over a very narrow range of Fermi levels near the VBM (see Fig. 11). Likewise, $V_{\text{N}}^{+}$ in $\text{Li}_2\text{NH}$ is similar to $V_{\text{NH}}^{0}$ in $\text{LiNH}_2$ because they both have a $\text{H}_{i}^{-}$ in the interstitial void formed by removing an anionic unit.

For the migration of $V_{\text{NH}}^{2+}$ in $\text{Li}_2\text{NH}$, we find an energy barrier of 0.91 eV. For $V_{\text{N}}^{+}$, the estimated energy barrier is also 0.91 eV, the energy barrier for $V_{\text{NH}}^{2+}$.

We have also investigated interstitial $\text{NH}_3$ molecules in $\text{Li}_2\text{NH}$ and find that they have relatively high formation energies if the $\text{NH}_3$ unit is preserved. Instead, we find that the $\text{NH}_3$ molecule prefers to combine with a host $(\text{NH})^{2-}$ unit to form two $(\text{NH}_2)^{-}$ units, lowering the energy by 0.54 eV. Even with this lower-energy configuration, the formation energy of 2.60 eV is still too high for it to be a relevant defect. Our results clearly indicate that $\text{NH}_3$ is unlikely to form and diffuse as interstitial molecules in bulk $\text{Li}_2\text{NH}$ (as we already found in the case of $\text{LiNH}_2$).

## V. DISCUSSION

Table I lists formation energies and migration barriers for all relevant native defects in $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$. For charged defects in $\text{LiNH}_2$, we set $\mu_{e}=2.49$ eV, where the formation energies of $\text{Li}_{i}^{+}$ and $V_{\text{Li}}^{-}$ are equal. This choice of Fermi level is based on the assumption that electrically active impurities are either absent or present in lower concentrations than the native point defects. In this case, the Fermi level is determined by oppositely charged defects with lowest formation energies, i.e., $\text{Li}_{i}^{+}$ and $V_{\text{Li}}^{-}$ for the chosen set of chemical potentials in $\text{LiNH}_2$ that represents the dehydrogenation conditions $(\mu_{\text{H}}=-0.49$ eV). The charge neutrality condition then requires these defects to be present in equal concentrations. $^{39,46,47}$ Similarly, in the case of $\text{Li}_2\text{NH}$ the defect formation energies are taken at $\mu_{e}=1.59$ eV, i.e., the Fermi level value at which the formation energies of $V_{\text{N}}^{+}$ and $V_{\text{Li}}^{-}$ are equal, where the chemical potentials are chosen to represent the hydrogenation conditions $(\mu_{\text{H}}=-0.31$ eV).

TABLE I. Calculated formation energies $(E^{f})$ and migration barriers $(E_{m})$ for native defects in $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$. Atomic chemical potentials were chosen to reflect equilibrium with $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$, and the experimental conditions at which the (de)hydrogenation processes occur (see text). Migration energies denoted by an asterisk $(^{*})$ are estimated by considering the defect as a complex (last column in the table) and taking the higher of the migration energies of the constituents.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Defect</th>
      <th>$E^{f}$ (eV)</th>
      <th>$E_{m}$ (eV)</th>
      <th>Complex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="13">$\text{LiNH}_2$</td>
      <td>$\text{H}_{i}^{+}$</td>
      <td>1.28</td>
      <td>0.61</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{H}_{i}^{-}$</td>
      <td>1.34</td>
      <td>0.34</td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{\text{H}}^{-}$</td>
      <td>0.63</td>
      <td>0.71</td>
      <td></td>
    </tr>
    <tr>
      <td>$(\text{H}_2)_{i}$</td>
      <td>1.75</td>
      <td>0.19</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{Li}_{i}^{+}$</td>
      <td>0.51</td>
      <td>0.30</td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{\text{Li}}^{-}$</td>
      <td>0.51</td>
      <td>0.20</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{Li}_{\text{H}}^{+}$</td>
      <td>0.48</td>
      <td>0.71*</td>
      <td>$\text{Li}_{i}^{+} + V_{\text{H}}^{-}$</td>
    </tr>
    <tr>
      <td>$\text{H}_{\text{Li}}^{0}$</td>
      <td>1.17</td>
      <td>0.61*</td>
      <td>$\text{H}_{i}^{+} + V_{\text{Li}}^{-}$</td>
    </tr>
    <tr>
      <td>$V_{\text{NH}_2}^{+}$</td>
      <td>0.62</td>
      <td>0.87</td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{\text{NH}}^{0}$</td>
      <td>0.40</td>
      <td>0.87*</td>
      <td>$V_{\text{NH}_2}^{+} + \text{H}_{i}^{-}$</td>
    </tr>
    <tr>
      <td>$V_{\text{N}}^{+}$</td>
      <td>1.64</td>
      <td>0.87*</td>
      <td>$V_{\text{NH}_2}^{+} + (\text{H}_2)_{i}$</td>
    </tr>
    <tr>
      <td>$V_{\text{N}}^{-}$</td>
      <td>1.77</td>
      <td>0.87*</td>
      <td>$V_{\text{NH}_2}^{+} + 2\text{H}_{i}^{-}$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="9">$\text{Li}_2\text{NH}$</td>
      <td>$\text{H}_{i}^{+}$</td>
      <td>0.74</td>
      <td>0.95</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{H}_{i}^{-}$</td>
      <td>0.65</td>
      <td>0.65</td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{\text{H}}^{-}$</td>
      <td>0.72</td>
      <td>1.66</td>
      <td></td>
    </tr>
    <tr>
      <td>$(\text{H}_2)_{i}$</td>
      <td>1.47</td>
      <td>–</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{Li}_{i}^{+}$</td>
      <td>0.66</td>
      <td>0.30</td>
      <td></td>
    </tr>
    <tr>
      <td>$V_{\text{Li}}^{-}$</td>
      <td>0.39</td>
      <td>0.14</td>
      <td></td>
    </tr>
    <tr>
      <td>$\text{H}_{\text{Li}}^{0}$</td>
      <td>0.58</td>
      <td>0.95*</td>
      <td>$\text{H}_{i}^{+} + V_{\text{Li}}^{-}$</td>
    </tr>
    <tr>
      <td>$\text{Li}_{\text{H}}^{0}$</td>
      <td>0.93</td>
      <td>1.66*</td>
      <td>$\text{Li}_{i}^{+} + V_{\text{H}}^{-}$</td>
    </tr>
    <tr>
      <td>$V_{\text{NH}}^{2+}$</td>
      <td>1.83</td>
      <td>0.91</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>$V_{\text{N}}^{+}$</td>
      <td>0.39</td>
      <td>0.91*</td>
      <td>$V_{\text{NH}}^{2+} + \text{H}_{i}^{-}$</td>
    </tr>
  </tbody>
</table>

It emerges from our analysis in the previous sections that the structure and energetics of all relevant native defects in $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$ can be interpreted in terms of basic building blocks, which include $\text{H}_{i}^{+}$, $\text{H}_{i}^{-}$, $V_{\text{H}}^{-}$, $(\text{H}_2)_{i}$, $\text{Li}_{i}^{+}$, $V_{\text{Li}}^{-}$, and $V_{\text{NH}_2}^{+}$ (or $V_{\text{NH}}^{2+}$). Understanding the electronic and structural properties of these elementary defects is, therefore, crucial for understanding these defect complexes and the role these defects play in mass transport and ionic conduction. Based on the results presented in Sec. IV, in the following, we discuss Li-ion conduction in $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$, and propose mechanisms for the decomposition of $\text{LiNH}_2$ and hydrogenation of $\text{Li}_2\text{NH}$. We also discuss the dehydrogenation of $\text{LiNH}_2 + \text{LiH}$ mixtures and the effects of ball milling.

### A. Li-ion conduction

Let us first discuss ionic mobility on the Li sublattice and its consequences for ionic conduction. It is evident from Table I that, in both $\text{LiNH}_2$ and $\text{Li}_2\text{NH}$, $\text{Li}_{i}^{+}$ and $V_{\text{Li}}^{-}$ have a low formation energies and are highly mobile. The $(\text{Li}_{i}^{+}, V_{\text{Li}}^{-})$ pair that is composed of these two defects also has a low formation energy, 0.65 eV in $\text{LiNH}_2$ and 0.68 eV in $\text{Li}_2\text{NH}$, suggesting that $\text{Li}_{i}^{+}$ and $V_{\text{Li}}^{-}$ can be created in the interior of the materials via a Frenkel pair mechanism. Our results are therefore in agreement with recent studies by Ludueña *et al.* using first-principles path integral molecular

dynamics simulations and solid-state $^1$H NMR experiments where they observed significant disorder on the Li sublattice. $^{48}$

Experimentally, $Li_2NH$ was found to be a good ionic conductor, with an activation energy of 0.58 eV. $^2$ This conductivity has been ascribed to the high mobility of Li ions. Our calculations show that both $Li_i^+$ and $V_{Li}^-$ can contribute to the ionic conductivity. However, since the calculated migration barrier of $V_{Li}^-$ is lower than that of $Li_i^+$, we expect that in $Li_2NH$ (and $LiNH_2$) lithium diffusion by the vacancy mechanism is dominant. The calculated activation energy for self-diffusion of $V_{Li}^-$ in $Li_2NH$ is estimated to be 0.53 eV (the formation energy plus the migration barrier, cf. Table I), which is very close to the experimental activation energy. $^2$ Similarly, we estimate the activation energy for self-diffusion of $V_{Li}^-$ in $LiNH_2$ to be 0.71 eV, somewhat lower than the reported experimental value (0.94 eV). $^{49,50}$ As discussed in the next sections, the highly mobile $Li_i^+$ and $V_{Li}^-$ also play an important role in the decomposition of $LiNH_2$ and hydrogenation of $Li_2NH$.

### B. Decomposition of $LiNH_2$

Here, we address the decomposition of $LiNH_2$ into $Li_2NH$ and $NH_3$ according to reaction (3). The transformation from $LiNH_2$ to $Li_2NH$ involves breaking N-H bonds. This can be accomplished through the formation of $V_H^-$, which, in turn, can occur in the interior of the material or at the surface. The required energies are not necessarily the same. The creation of $V_H^-$ in the interior of $LiNH_2$, for instance, is necessarily accompanied by the creation of $H_i^+$ so that mass and charge are conserved. At the surface, one can create $V_H^-$ by removing a proton ($H^+$) from $LiNH_2$ and this $H^+$ could be accommodated as an adsorbed atom or react with nearby species. These two possibilities, namely forming $V_H^-$ in the interior of $LiNH_2$ or at the surface, can be interpreted as two different possible mechanisms for the reaction. As discussed below, the difference in the activation energies of these two mechanisms will lead to an effective dependence on the surface-to-volume ratio or the specific surface area (SSA), which can be measured experimentally. First, we describe the mechanisms in more detail.

Mechanism 1. $V_H^-$ and $H_i^+$ are created simultaneously in the interior of $LiNH_2$ through forming a $(H_i^+,V_H^-)$ Frenkel pair, i.e., moving $H^+$ from a lattice site to an interstitial site. This results in an $(NH)^{2-}$ next to an $NH_3$ unit representing $V_H^-$ and $H_i^+$, respectively, as shown in Fig. 5(a). Next, $V_H^-$ and $H_i^+$ become separated as $H_i^+$ jumps from one $(NH_2)^-$ unit to another. This is equivalent to displacing the $NH_3$ unit away from the $(NH)^{2-}$ unit, leaving two $Li^+$ next to $(NH)^{2-}$, i.e., a formula unit of $Li_2NH$ is locally formed inside $LiNH_2$. $H_i^+$ then migrates to the surface and is released as $NH_3$. Note that here we assume that as $H_i^+$ migrates from one $(NH_2)^-$ unit to the next, a corresponding $Li^+$ moves in the opposite direction in the form of $Li_i^+$ (see more below). The overall activation energy ($E_a$) for this mechanism then consists of the formation energy of the $(H_i^+,V_H^-)$ Frenkel pair (1.28 eV), the cost for separating the species in this Frenkel pair (0.63 eV), plus the migration barrier of $H_i^+$ (0.61 eV), i.e., $E_a = 1.28 + 0.63 + 0.61 = 2.52$ eV. This activation energy is in very good agreement with the experimental value of 2.53 eV for the activation energy related to the decomposition of $LiNH_2$ before ball milling. $^{14}$

Mechanism 2. $V_H^-$ is created at the surface by removing an $H^+$ from $LiNH_2$. This $H^+$ ion can combine with a surface $(NH_2)^-$ unit to form $NH_3$ that is subsequently released. Given the ionic nature of the bonding between $Li^+$ and $(NH_2)^-$, we believe that such a process will be possible, irrespective of the details of the surface structure. Note that the rate-limiting step in this mechanism is not the formation of $V_H^-$ at the surface, but the hydrogen mass transport to the surface, i.e., in order to maintain this reaction, hydrogen atoms have to be transported to the surface. Here, our only assumption is that the formation energy of $V_H^-$ on the surface is lower than (or equal to) the formation energy in the bulk, which is a safe assumption given that the bonding environment at the surface is less constrained than in the bulk. In this mechanism, the activation energy is given by hydrogen self-diffusion mediated by $V_H^-$, the sum of its formation energy and migration barrier: $E_a = 0.63 + 0.71 = 1.34$ eV. The $Li^+$ unit that was left with after the surface $(NH_2)^-$ unit was released with the $H^+$ (in form of $NH_3$) assists the hydrogen self-diffusion in the form of $Li_i^+$, as required by the charge neutrality condition. Note also that the complex formed by $V_H^-$ and $Li_i^+$ corresponds to a formula unit of $Li_2NH$ inside $LiNH_2$. The calculated activation energy of 1.34 eV is also in good agreement with experimentally determined activation energies for the decomposition of ball-milled $LiNH_2$, ranging from 1.33 to 1.43 eV. $^{10,14}$

Since mechanism 1 starts with the formation of defects in the bulk and mechanism 2 with the formation of defects at the surface, we expect the prevalent mechanism and hence the effective activation energy for decomposition to be dependent on the surface-to-volume ratio. In samples composed of sufficiently large particles of $LiNH_2$, the surface-to-volume ratio is small and mechanism 1 prevails. On the other hand, in samples composed of relatively small particles, i.e., with large surface-to-volume ratio, mechanism 2 prevails. Indeed, it has been observed that in $LiNH_2$ samples subjected to ball milling, the activation energy for decomposition decreases with milling time, from 2.53 eV (before ball milling, SSA: $3.72\ \text{m}^2/\text{g}$) to 2.30 eV (after 45min of milling, SSA: $40.71\ \text{m}^2/\text{g}$) to 1.43 eV (after 3h, SSA: $46.65\ \text{m}^2/\text{g}$), $^{14}$ i.e., as the milling time increases the particle size is decreased and the SSA increased, and we expect the prevalent mechanism to change from 1 to 2. These experimental activation energy values are within the range (1.34-2.52 eV) established by the calculated activation energies for mechanisms 1 and 2. It should be noted that the increase in SSA upon ball milling not only increases the likelihood of point defect formation at the surface, it also increases the chance that the point defects can reach all parts of the "bulk" within a given amount of time. While surfaces are of course present even in mechanism 1, they simply fail to make enough of a difference to modify the observed activation energy.

In both mechanisms, the highly mobile and low-formation-energy $Li_i^+$ and $V_{Li}^-$ provide local charge neutrality and additional mass transport. Without the accompanying $Li_i^+$ defect, for example, $V_H^-$ would not be able to diffuse into the bulk because local charge neutrality has to be maintained. On the other hand, $Li_H^0$ (a complex of $Li_i^+$ and $V_H^-$) in $LiNH_2$ and $H_{Li}^0$ (a complex of $H_i^+$ and $V_{Li}^-$) in $Li_2NH$ have very

low formation energies, suggesting that Li amide (imide) can be locally formed within the bulk Li imide (amide). Our results therefore support David *et al.*'s observations that the Li amide/imide reaction is a bulk reaction and that there is a continuous transformation between LiNH₂ and Li₂NH via nonstoichiometric intermediates.¹⁶

We acknowledge that mechanisms 1 and 2, which are based on calculations of point defects in the dilute limit, do not present a complete picture of the decomposition process. However, the formation and migration of point defects is an initial, but essential and critical, step toward decomposition. In this initial step, the concentration of point defects will be low, thus justifying our focus on the dilute limit. Other processes certainly play a role as well in the ultimate decomposition, but the agreement with experiment indicates that these other processes have activation energies that are either lower than, or comparable to, the point-defect-related mechanisms we are describing. In addition, the fact that we predict different activation energies for different particle sizes, in agreement with experiment, provides support for the point-defect mechanisms indeed being the rate-limiting step.

As mentioned in Sec. I, other research groups have also tried to understand the decomposition of LiNH₂ into Li₂NH and NH₃ based on first-principles defect calculations. Although not clearly stated, Miceli *et al.*²⁶ seemed to suggest that for small LiNH₂ particles the decomposition process occurs at the surface with the formation of $(H_i^+,V_H^-)$ Frenkel pairs, and for larger particles, the formation of $(H_i^+,V_H^-)$ would also occur in the bulk. This is somewhat similar to the two mechanisms we described above. However, Miceli *et al.* suggested further that, in the former case, the rate-limiting step at the early stage of decomposition is the formation of $(H_i^+,V_H^-)$ at the surface in the presence of lithium Frenkel pairs. This is different from our mechanism 2 where the rate-limiting step is self-diffusion of $V_H^-$. Hazrati *et al.*²⁷ also proposed that the decomposition process occurs at the surface with the formation of $(H_i^+,V_H^-)$ Frenkel pairs. Wang *et al.*²⁸ on the other hand, did not provide any specific mechanism but suggested that the formation of $H_i^+$ is the rate-limiting step in hydrogen mass transport.

### C. Dehydrogenation of LiNH₂ + LiH mixtures
The mechanisms we have proposed can also provide an understanding of the dehydrogenation of LiNH₂ + LiH mixtures, i.e., reaction (2). In these systems, one expects that LiNH₂ and LiH are in intimate contact if the reactants are carefully mixed. At the LiNH₂/LiH interface, LiH can provide $H^-$ ions. Our calculated formation energy for $V_H^+$ vacancies in LiH is 0.69 eV, and since indiffusion of $V_H^+$ is equivalent to outdiffusion of $H_i^-$, this result confirms that LiH can indeed supply the $H^-$ ions that we invoke. These $H^-$ ions can combine with $H_i^+$ (that is created in the bulk of LiNH₂ and migrates to the LiNH₂/LiH interface via mechanism 1) or $H^+$ (that is liberated from LiNH₂ when creating $V_H^-$ via mechanism 2) to form H₂ without releasing any NH₃. This explains the formation of H₂ in reaction (2). If LiNH₂ and LiH are not in intimate contact, NH₃ can still be produced from LiNH₂ according to reaction (3) because the $H^-$ (from LiH) is not immediately available to combine with $H_i^+$ or $H^+$ before the latter is released from LiNH₂ in the form of NH₃. In this case, the resulting NH₃ can be captured by LiH according to reaction (4) and/or released as one of the products.

It has been demonstrated that the activation energy for the dehydrogenation of LiNH₂ + LiH mixtures also decreases with increasing ball-milling time.⁵¹,⁵² Shaw *et al.* reported activation energies of 1.70 eV (SSA: 4.65 m²/g), 1.36 eV (SSA: 47.36 m²/g), 1.18 eV (SSA: 51.32 m²/g), and 0.65 eV (SSA: 62.35 m²/g) for the dehydrogenation of the LiNH₂ + LiH mixture before ball milling and after the samples were ball-milled for 1.5, 3, and 24 h, respectively.⁵¹ Varin *et al.*, on the other hand, reported a different set of activation energies: 2.46 eV (before milling, SSA: 16.5 m²/g), 0.98 eV (after 1h, SSA: 26.4 m²/g), 0.88 eV (after 25h, SSA: 59.6 m²/g), and 0.91 eV (after 100h, SSA: 45.6 m²/g).⁵² Both sets of experimental values show the same trend: the activation energy is reduced significantly with ball milling and there is a correlation with the measured SSA.

We suggest that the activation energy for the dehydrogenation of LiNH₂ + LiH mixtures with relatively short milling times is predominantly determined by that for the decomposition of LiNH₂. The above mentioned experimental data can therefore be explained in terms of our discussion in Sec. V B about LiNH₂ decomposition, meaning the dehydrogenation of the mixtures is expected to proceed via mechanisms 1 and/or 2, and the extent to which one mechanism dominates over the other depends on the surface-to-volume ratio (or the SSA). This provides an explanation for the observed activation energies in the range from 1.34 to 2.52 eV. For those samples that exhibit activation energies lower than that of mechanism 2 (1.34 eV), produced after long milling times, we suggest that the milling process may have created a high degree of damage in the LiNH₂ + LiH mixtures, even to the point of local amorphization. Formation energies for defects in these damaged regions would be lower than in the pristine bulk, resulting in defect concentrations well above the equilibrium concentrations; this lowering of the cost of forming the rate-limiting defects results in a lowering of the activation energy for dehydrogenation.

Shaw *et al.* suggested that NH₃ diffusion through a Li₂NH product layer outside a LiNH₂ shrinking core is the rate-limiting step in the kinetics of the dehydrogenation of LiNH₂ + LiH mixtures.¹⁴,⁵³ We find that this is very unlikely if the Li₂NH layer is thick enough. As presented in Sec. IV, our results clearly indicate that NH₃ is not likely to form (and diffuse) as interstitial molecules in either LiNH₂ or Li₂NH because the formation energy is too high. In Li₂NH, interstitial NH₃ molecules are even unstable toward forming $(NH_2)^-$ units, by combining with host $(NH)^{2-}$ units.

Note that the calculated activation energy of mechanism 2 reported in Sec. V B depends on the formation energy of $V_H^-$ at the Fermi-level value $\mu_e$ determined by the charge neutrality condition, which in turn depends on the chemical potentials of Li, N, and H. However, we have checked several possible scenarios and found that the calculated activation energy is not sensitive to the choice of chemical potentials. In the case of LiNH₂ + LiH mixtures, for example, if the two reactants are carefully mixed, one can assume equilibrium between LiNH₂, Li₂NH, and LiH, which gives rise to a different set of chemical potentials where $\mu_H=-0.40$ eV. The Fermi level of LiNH₂ is then at $\mu_e=2.58$ eV where $Li_i^+$ and $V_{Li}^-$ have equal formation


energies. We find that in this case the activation energy of mechanism 2 is still 1.34 eV.

### D. Hydrogenation of $Li_2NH$
Before discussing the hydrogenation mechanism of $Li_2NH$, let us summarize what is known about the hydrogenation process in metals. The absorption of hydrogen to form a metal hydride includes several steps: $^{54}$ (i) the applied $H_2$ is physisorbed on the surface of the metal, (ii) the physisorbed $H_2$ is dissociated at the surface and becomes chemisorbed, (iii) H atoms move to subsurface sites and diffuse through the metal, and (iv) as the hydrogen concentration increases, a metal hydride phase nucleates. In this process, the rate-limiting step changes from the dissociation and penetration of hydrogen at the metal/$H_2$ interface to the nucleation of the hydride phase, and possibly the diffusion of hydrogen through the metal hydride layer that forms around the metal particle. $^{54}$ We expect to see similar processes in $Li_2NH$.

For the hydrogenation reaction in Eq. (2), the highly mobile $Li_i^+$ and $V_{Li}^-$ in $Li_2NH$ are expected to play an important role. These two defects can be created at the surface or simultaneously in the interior of the material via a Frenkel pair mechanism. $Li_i^+$ is likely to interact with the applied $H_2$ gas at the surface, or with the chemisorbed H that diffuses into the material, and form LiH and $H_i^+$, i.e., $Li_i^+ + H_2 \rightarrow LiH + H_i^+$. This $H_i^+$ will then be attracted toward the $V_{Li}^-$ defect to form $H_{Li}^0$ (a complex of $H_i^+$ and $V_{Li}^-$), which provides $(NH_2)^+$ units for the formation of $LiNH_2$. This is similar to the mechanism proposed by David *et al.*$^{16}$ for Li amide/imide hydrogenation. The rate-limiting step in this process could be the diffusion of $H_i^+$ in the bulk of $Li_2NH$. However, this cannot be claimed with certainty without explicit investigations of all other possible steps involved in the hydrogenation process.

---

### VI. SUMMARY
We have carried out comprehensive first-principles studies of native defects in $LiNH_2$ and $Li_2NH$. Both compounds are found to be prone to Frenkel disorder on the Li sublattice, which is consistent with experimental observations. Lithium interstitials and vacancies have low formation energies and are highly mobile; they can therefore participate in ionic conduction and mass transport, and act as accompanying defects for hydrogen-related defects in mass transport. Hydrogen interstitials and vacancies, on the other hand, are responsible for forming and breaking N-H bonds, which are essential in the Li amide/imide reaction. Based on the structure, energetics, and migration of hydrogen-, lithium-, and nitrogen-related point defects and defect complexes, we have proposed that $LiNH_2$ decomposes into $Li_2NH$ and $NH_3$ according to two competing mechanisms, one involving the formation of native defects in the interior of the material, and the other at the surface. As a result, the prevalent mechanism and hence the effective activation energy for decomposition depend on the surface-to-volume ratio or the specific surface area, which changes with particle size during ball milling. These mechanisms also provide an explanation for the particle-size dependence of the activation energy of the decomposition of $LiNH_2$ and that of the dehydrogenation of $LiNH_2 + LiH$ mixtures.

### ACKNOWLEDGMENTS
K.H. was supported by General Motors Corporation, and A.J. by the US Department of Energy (Grant No. DE-FG02-07ER46434). We acknowledge the use of the CNSI Computing Facility under NSF Grant No. CHE-0321368, NERSC resources supported by the DOE Office of Science under Contract No. DE-AC02-05CH11231, and the Ranger supercomputer from the TeraGrid computing resources supported by the NSF under Grant No. DMR070072N.

---

$^*$Current address: Naval Research Laboratory, Washington, DC 20375, USA and George Mason University, Fairfax, VA 22030, USA; hoang@dave.nrl.navy.mil.
$^\dagger$vandewalle@mrl.ucsb.edu

$^1$U. Eberle, M. Felderhoff, and F. Schüth, *Angew. Chem. Int. Ed.* **48**, 6608 (2009).
$^2$B. A. Boukamp and R. A. Huggins, *Phys. Lett. A* **72**, 464 (1979).
$^3$P. Chen, Z. Xiong, J. Luo, J. Lin, and K. L. Tan, *Nature (London)* **420**, 302 (2002).
$^4$P. Chen, Z. Xiong, J. Luo, J. Lin, and K. L. Tan, *J. Phys. Chem. B* **107**, 10967 (2003).
$^5$J. Lu, Z. Z. Fang, and H. Y. Sohn, *Inorg. Chem.* **45**, 8749 (2006).
$^6$Y. H. Hu and E. Ruckenstein, *Ind. Eng. Chem. Res.* **42**, 5135 (2003).
$^7$Y. H. Hu and E. Ruckenstein, *J. Phys. Chem. A* **107**, 9737 (2003).
$^8$T. Ichikawa, S. Isobe, and H. Fujii, *J. Alloys Compd.* **365**, 271 (2004).
$^9$T. Ichikawa, N. Hanada, S. Isobe, H. Leng, and H. Fujii, *J. Phys. Chem. B* **108**, 7887 (2004).
$^{10}$F. E. Pinkerton, *J. Alloys Compd.* **400**, 76 (2005).

$^{11}$G. P. Meisner, F. E. Pinkerton, M. S. Meyer, M. P. Balogh, and M. D. Kundrat, *J. Alloys Compd.* **404-406**, 24 (2005).
$^{12}$T. Ichikawa, N. Hanada, S. Isobe, H. Y. Leng, and H. Fujii, *J. Alloys Compd.* **404-406**, 435 (2005).
$^{13}$S. Isobe, T. Ichikawa, S. Hino, and H. Fujii, *J. Phys. Chem. B* **109**, 14855 (2005).
$^{14}$T. Markmaitree, R. Ren, and L. L. Shaw, *J. Phys. Chem. B* **110**, 20710 (2006).
$^{15}$J. Z. Hu, J. H. Kwak, Z. Yang, W. Osborn, T. Markmaitree, and L. L. Shaw, *J. Power Sources* **181**, 116 (2008).
$^{16}$W. I. David, M. O. Jones, D. H. Gregory, C. M. Jewell, S. R. Johnson, A. Walton, and P. P. Edwards, *J. Am. Chem. Soc.* **129**, 1594 (2007).
$^{17}$K.-F. Aguey-Zinsou, J. Yao, and Z. Xiao Gua, *J. Phys. Chem. B* **111**, 12531 (2007).
$^{18}$J. F. Herbst and L. G. Hector Jr., *Phys. Rev. B* **72**, 125120 (2005).
$^{19}$K. Miwa, N. Ohba, S. I. Towata, Y. Nakamori, and S.-i. Orimo, *Phys. Rev. B* **71**, 195109 (2005).
064115-11

$^{20}$J. B. Yang, X. D. Zhou, Q. Cai, W. J. James, and W. B. Yelon, Appl. Phys. Lett. **88**, 041914 (2006).

$^{21}$Y. Song and Z. X. Guo, Phys. Rev. B **74**, 195120 (2006).

$^{22}$T. Mueller and G. Ceder, Phys. Rev. B **74**, 134104 (2006).

$^{23}$B. Magyari-Köpe, V. Ozolins, and C. Wolverton, Phys. Rev. B **73**, 220101 (2006).

$^{24}$T. Tsumuraya, T. Shishidou, and T. Oguchi, J. Alloys Compds. **446-447**, 323 (2007).

$^{25}$K. Hoang, A. Janotti, and C. G. Van de Walle, Angew. Chem. Int. Ed. **50**, 10170 (2011).

$^{26}$G. Miceli, C. S. Cucinotta, M. Bernasconi, and M. Parrinello, J. Phys. Chem. C **114**, 15174 (2010).

$^{27}$E. Hazrati, G. Brocks, B. Buurman, R. A. de Groot, and G. A. de Wijs, Phys. Chem. Chem. Phys. **13**, 6043 (2011).

$^{28}$J. Wang, Y. Du, H. Xu, C. Jiang, Y. Kong, L. Sun, and Z.-K. Liu, Phys. Rev. B **84**, 024107 (2011).

$^{29}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

$^{30}$P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994).

$^{31}$G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

$^{32}$G. Kresse and J. Hafner, Phys. Rev. B **47**, 558 (1993).

$^{33}$G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).

$^{34}$G. Kresse and J. Furthmüller, Comput. Mat. Sci. **6**, 15 (1996).

$^{35}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B **13**, 5188 (1976).

$^{36}$G. Henkelman, B. P. Uberuaga, and H. Jónsson, J. Chem. Phys. **113**, 9901 (2000).

$^{37}$C. G. Van de Walle and J. Neugebauer, J. Appl. Phys. **95**, 3851 (2004).

$^{38}$A. Janotti and C. G. Van de Walle, Rep. Prog. Phys. **72**, 126501 (2009).

$^{39}$A. Peles and C. G. Van de Walle, Phys. Rev. B **76**, 214101 (2007).

$^{40}$D. J. Siegel, C. Wolverton, and V. Ozolins, Phys. Rev. B **75**, 014101 (2007).

$^{41}$J. F. Herbst and L. G. Hector Jr., Appl. Phys. Lett. **88**, 231904 (2006).

$^{42}$H. Hemmes, A. Driessen, and R. Griessen, J. Phys. C **19**, 3571 (1986).

$^{43}$R. Juza and K. Opp, Z. Anorg. Allg. Chem. **266**, 325 (1951).

$^{44}$T. Noritake, H. Nozaki, M. Aoki, S. Towata, G. Kitahara, Y. Nakamori, and S.-i. Orimo, J. Alloys Compd. **393**, 264 (2005).

$^{45}$K. Ohoyama, Y. Nakamori, S.-i. Orimo, and K. Yamada, J. Phys. Soc. Jpn. **74**, 483 (2005).

$^{46}$G. B. Wilson-Short, A. Janotti, K. Hoang, A. Peles, and C. G. Van de Walle, Phys. Rev. B **80**, 224102 (2009).

$^{47}$K. Hoang and C. G. Van de Walle, Phys. Rev. B **80**, 214109 (2009).

$^{48}$G. A. Ludueña, M. Wegner, L. Bjålie, and D. Sebastiani, Chem. Phys. Chem. **11**, 2353 (2010).

$^{49}$M. Matsuo, A. Remhof, P. Martelli, R. Caputo, M. Ernst, Y. Miura, T. Sato, H. Oguchi, H. Maekawa, H. Takamura, A. Borgschulte, A. Züttel, and S.-i. Orimo, J. Am. Chem. Soc. **131**, 16389 (2009).

$^{50}$M. Matsuo and S.-i. Orimo, Adv. Energy Mater. **1**, 161 (2011).

$^{51}$L. L. Shaw, R. Ren, T. Markmaitree, and W. Osborn, J. Alloys Compds. **448**, 263 (2008).

$^{52}$R. A. Varin, M. Jang, and M. Polanski, J. Alloys Compds. **491**, 658 (2010).

$^{53}$L. L. Shaw, W. Osborn, T. Markmaitree, and X. Wan, J. Power Sources **177**, 500 (2008).

$^{54}$V. Bérubé, G. Radlke, M. Dresselhaus, and G. Chen, Int. J. Energy Res. **31**, 637 (2007).