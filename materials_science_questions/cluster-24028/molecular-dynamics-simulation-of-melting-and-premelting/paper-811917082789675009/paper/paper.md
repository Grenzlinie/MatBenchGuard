PHYSICAL REVIEW E 77, 061801 (2008)

# Crystal nucleation enhanced at the diffuse interface of immiscible polymer blends

Yu Ma, $^{1,2}$ Liyun Zha, $^{1}$ Wenbing Hu, $^{1, *}$ Günter Reiter, $^{2}$ and Charles C. Han $^{3}$

$^{1}$ Department of Polymer Science and Engineering, State Key Laboratory of Coordination Chemistry,
School of Chemistry and Chemical Engineering, Nanjing University, 210093 Nanjing, China
$^{2}$ Institut de Chimie des Surfaces et Interfaces, CNRS-UHA, 15 rue Jean Starcky, Boîte Postale 2488, 68057 Mulhouse Cedex, France
$^{3}$ State Key Laboratory of Polymer Physics and Chemistry, Institute of Chemistry, Chinese Academy of Sciences,
100080 Beijing, China

(Received 28 December 2007; published 2 June 2008)

We report dynamic Monte Carlo simulations of immiscible binary polymer blends, which exhibit weakly enhanced crystal nucleation near interfaces between two phase-separated polymers. We found that this enhancement is not accompanied by any preferred crystal orientation, implying its origin is mainly of enthalpic rather than entropic nature. Mean-field theory of polymer blends predicts that for immiscible polymers the melting point of the crystallizable component increases upon dilution in the other component, while it normally decreases for miscible blends. A local dilution is forced to occur at the diffuse interface of immiscible polymers; therefore the melting point of crystallizable polymers rises, which, in turn, enhances the thermodynamic driving force for crystal nucleation near the interface.

DOI: 10.1103/PhysRevE.77.061801
PACS number(s): 61.25.hk, 64.60.Q−, 82.60.Nh, 83.80.Tc

## I. INTRODUCTION

Blending of different types of polymers is a common process to realize materials having complementary advantages of these polymers and/or with a lower cost. The miscibility of different polymer species is determined by the mixing free energy, which has been well-described by the Flory- Huggins-Scott equation [1–4]. In addition, consideration of the system's compressibility [5] and the asymmetry in chemical details [6] grants an even stronger power for predicting the precise boundary of liquid-liquid-coexistence in polymer blends.

Both liquid-liquid phase separation (LLPS) and crystallization are basic phase transitions in polymer blends. The interplay of these two processes opens up various pathways within thermodynamic phase diagrams to control polymer morphologies. For instance, binary blends of polyolefins may crystallize either directly from a homogenous state or, after prior LLPS on cooling, from a phase-separated state [7,8]. The resulting morphologies of crystallites differ significantly and depend upon the detailed pathway of temperature and time followed during crystallization [9].

The development of a theoretical interpretation on the basis of Flory-Huggins mean-field lattice theory has provided us a better understanding of the thermodynamic interplay between these two kinds of phase transitions [10]. For instance, with athermal mixing contacts between two components, LLPS of a polymer blend may still occur, driven solely by the crystallizability of one component [11]. In addition, at high temperatures in the vicinity of the melting point of a crystallizable component, LLPS can be enhanced in the melt by thermal fluctuations toward the crystalline state of this component [12]. On the other hand, for high-molecular-weight polymer blends, the mixing entropy, which scales inversely with chain length, has an almost negligible effect in the melting point depression [13,14]. Thus compared to the behavior in polymer solutions, where crystal nucleation can be triggered by the prior LLPS due to a much higher melting point of the phase rich in the crystallizable polymer, i.e., significant melting point depression upon dilution [15,16], crystallization in polymer blends shall be less affected by prior LLPS.

Recently, experimental observations on a blend of two immiscible polyolefins revealed a reduction in crystal nucleation rate with the temporal evolution of liquid-liquid spinodal decomposition at high temperatures [17,18], suggesting fluctuation-assisted heterogeneous crystal nucleation near the interface. At high temperatures, where homogeneous crystal nucleation is very unlikely, heterogeneous nucleation is usually initiating polymer crystallization. Heterogeneous nucleation is often triggered by interfaces provided, e.g., by foreign species (impurities) such as catalysts, dust particles, and additives [19]. Up to now, it is still unclear whether interface-induced heterogeneous crystal nucleation in an immiscible polymer blend is an intrinsic behavior of polymers or just an effect of impurities accumulated at the interfacial area due to their lower affinities to one of the polymer components. To address this issue, we launched dynamic Monte Carlo simulations of lattice polymer blends containing no impurities. We will provide evidence for an intrinsically enhanced polymer crystal nucleation at the diffuse interface of immiscible polymers. A theoretical explanation for this observation will be provided based on the developed mean-field lattice theory.

In this paper, after the Introduction, we first make a detailed description of the simulation techniques employed here, followed by a presentation of the observations obtained in these simulations as well as a theoretical interpretation of the enhanced crystal nucleation at the interface of immiscible polymers. The paper ends with a summary of our conclusions.

*Corresponding author. wbhu@nju.edu.cn

1539-3755/2008/77(6)/061801(5)
061801-1
©2008 The American Physical Society

## II. SIMULATION TECHNIQUES

The bulk sample system of a binary polymer blend was constituted by 15 360 chains with uniform chain lengths of 16 lattice units in a space of $64^3$ cubic lattices. As demonstrated by the present simulations, the chain length 16 is large enough to reflect the characteristic of multiple chain folding on polymer crystallization. The chains were performing microrelaxations with periodic boundary conditions of the lattice (for the details of the microrelaxation model, see the Appendix of Ref. [10]). In each step of microrelaxations, we forbade double occupations and bond crossings to mimic the hard-core volume exclusions of bulk polymers. A small amount of void sites were necessary for microrelaxation and played the role of free volume in the bulk polymer phase. The initial state of a homogeneous melt was prepared by a long-term athermal microrelaxation toward an equilibrium bulk amorphous phase. The time unit in the simulations was defined as one Monte Carlo (MC) cycle, representing the total amount of microrelaxation steps equal to the number of monomers in the sample system.

The well-known Metropolis-sampling method was employed in each step of microrelaxation with a potential energy barrier of $(cE_c + pE_p + bB)/kT$, where $c$, $p$, and $b$ are the net numbers of collinear connections of bonds along a given chain of crystallizable bonds which are packed in parallel, and of mixed pairs of lattice sites occupied by different components, respectively, $E_c$, $E_p$, and $B$ are the corresponding potential energy changes, $k$ is the Boltzmann constant, and $T$ the absolute temperature. In practice, $E_p/E_c$ was fixed at the value of one in order to reflect the driving forces for crystallization and to maintain the chain flexibility in the temperature range of crystallization, $B/E_c$ was variable between zero and positive values to represent the driving forces for LLPS, and $kT/E_c$ represented the reduced system temperature. With respect to experimental conditions, we created a contrast of $B/E_c$ between the situation of an athermal solvent and that of a poor solvent to visualize the effect of poor solvent on the enhancement of crystal nucleation at the interface. Half of the chains were assigned to the crystallizable component $C$ that allowed for the interactions of bonds with an energy $E_p$, while the other half represented the noncrystallizable component $NC$ that did not allow for such interactions.

In the following, we first present simulations which follow the procedure reported by the previous experiments on the observation of crystallization near the interface generated by prior LLPS. We then go on by studying the influence of thermal fluctuations on crystal nucleation at high temperatures. Finally, we provide a theoretical interpretation to the observed enhancement of crystal nucleation near the interface.

## III. RESULTS AND DISCUSSION

### A. Observations of crystal initiation near the interface

We first chose $B/E_c$=0.3 that represented immiscible polymers in the binary blend, and then quenched the homogeneous sample to a temperature of $4.0\ E_c/k$ for a period of 50 000 MC cycles, where phase separation occurred but crystallization had not happened yet. This phase-separated sample was then further quenched to a slightly lower temperature, e.g., $3.95\ E_c/k$, where the crystallization was slowly initiated. This allowed us to identify the locations of small crystallites generated by primary crystal nucleation at the early stage of crystallization.

![](./images/811917082789675009_1.jpg)

FIG. 1. (Color online) Snapshot (a) for a sample at the temperature of $3.95\ E_c/k$ and the time period of 80 000 MC cycles after having been annealed at a slightly higher temperature of $4.0\ E_c/k$ for a time period of 50 000 MC cycles. $E_p/E_c$=1 and $B/E_c$=0.3. Snapshots (b)–(d) for samples exhibiting typical edge-on (b), flat-on (c), and tilted (d) small crystallites initiated near the flat interfaces, taken at $3.95\ E_c/k$ and 22 000, 29 400, and 43 400 MC cycles, respectively, after having annealed the sample at $4.0\ E_c/k$ for 200 000 MC cycles. $E_p/E_c$=1 and $B/E_c$=0.5. The bonds of component $NC$ are shown as tiny blue (dark) cylinders, while the bonds of component $C$ that have more than 11 parallel neighbors of $C$ are drawn in tiny yellow (bright) cylinders. All other bonds of $C$ are not shown for clarity.

A snapshot is shown in Fig. 1(a) demonstrating an example that crystal nucleation occurs near the interfaces between two immiscible polymers generated by the prior LLPS. The half-half composition of the symmetric blend dictated spinodal decomposition of LLPS and after a relatively short time period of LLPS a fairly bicontinuous morphology with nonuniformly oriented interfaces between two components was produced.

In order to obtain a more regular phase-separated geometry, we increased both the period of time (200 000 MC cycles) and the strength of demixing interactions ($B/E_c$=0.5) to complete LLPS at $4.0\ E_c/k$ before allowing for crystal nucleation at the lower temperature. This procedure resulted in a half space occupied by only one component, with a flat interface whose orientation can be used as a reference for defining the orientation of crystals. The snapshots of Figs. 1(b)–1(d) display crystals near the interfaces located around $Z$=15 and 45, with several typical crystal orientations. However, in the present visual inspections, some crystals are quite large and it is difficult to judge directly whether

![](./images/811917082789675009_2.jpg)

FIG. 2. (Color online) Distributions of the largest crystalline clusters with their mass centers as a function of the distance along the direction normal to the blend interface for variable $B/E_c$ values as labeled, at the temperature $4.0\ E_c/k$ after having annealed the sample for 200 000 MC cycles with $E_p/E_c=1$ and $B/E_c=0.5$ for the completion of LLPS. The largest cluster was defined as the cluster containing the maximum number of parallel bonds of component $C$, and its location was represented by the $Z$ position of its center of mass. 10 000 observations were collected with 20 MC cycle intervals, and the center positions of the $C$ phase were calibrated back to the same position to eliminate blurring of distributions due to the floating of phase boundaries.

they are initiated near the interface or not. So the statistical results at a very early stage of crystal nucleation will provide more convincing evidence for the locations of crystal initiation.

### B. Statistical results of crystal nucleation upon thermal fluctuations
In principle, homogeneous crystal nucleation is initiated by thermal fluctuations in the supercooled liquid. According to the classical nucleation theory, the cluster containing the maximum parallel (i.e., crystalline) bonds has the highest probability to survive as a nucleus in the course of thermal fluctuations. Therefore we focus our attention on these largest clusters generated by thermal fluctuations at the relatively high temperature, i.e., $4.0\ E_c/k$, after parallel flat interfaces have been prepared. In the case of $B=0$, the interfaces are still stable due to the driving force for LLPS provided by the crystallizability of one component [11].

The distributions of the largest clusters as a function of the distance along the direction normal to the flat interfaces are shown in Fig. 2. One can see that the distributions change from the single wide peak for $B=0$ to the double peak for $B>0$, indicating an interface-enhanced crystal nucleation under a stronger tendency of demixing ($B>0$). On the peak for $B=0$, the maximum at the middle site is deduced from a quite isolated event which may be due to weak fluctuations. Therefore we considered the profile of the peak as a wide plateau representing about equal nucleation probability within this region.

![](./images/811917082789675009_3.jpg)

FIG. 3. (Color online) Size distributions of the largest crystalline clusters with variable $B/E_c$ values as labeled. The cluster size was defined by the total amount of bonds connected by parallel neighbors. The data were collected under the same conditions described in Fig. 2.

In addition, we observed that with the increase of $B/E_c$ the size distributions of the largest clusters as summarized in Fig. 3 shift to larger values, implying an enhancement of crystal nucleation with high values of $B/E_c$. The differences between cases for various values of $B>0$ appear rather small in comparison to their differences to the case of $B=0$ where the interface has already been present. This result implies that the enhancement of crystal nucleation in the cases of $B>0$ cannot be simply attributed to the existence of such an interface. Additional factors must come into play.

We further defined the interfacial zone as a function of the distance along the normal direction of the interface by finding the interceptions of the lines extrapolated from the phase transition zones, as demonstrated in Fig. 4(a). With this definition of the interfacial zone, we calculated the orientational-order parameters of the largest crystalline clusters with at least one of their bonds located in the interfacial zone, and the results are shown in Fig. 4(b). One can see from the figure that the orientational-order parameters are close to zero. Only when $B/E_C$ values become large, a weak edge-on preference of crystal orientations occurs.

Polymer chains are forced to make contact with the flat repulsive interface of another component when the segregation strength becomes large enough. The conformation of these chains will be preferentially aligned in parallel with the interface, as has been evidenced by both experiments [20] and simulations [21-25]. These aligned chains will have less entropy change upon crystallization, and due to this thermodynamic advantage they will enhance the probability of crystal nucleation and most likely generate edge-on crystals [26]. However, this entropy effect is not so strong in the present cases, where the random crystal orientations are dominant. The randomness of crystal orientations implies that, when $B$ is not large, the priority of crystal nucleation at the diffuse interface can be attributed to an enthalpic rather than entropic origin. An entropic effect, for example, as a result of coil deformation, would dictate a strong edge-on preference of crystal orientations.

![](./images/811917082789675009_4.jpg)

FIG. 4. (a) Depiction for the definition of the interfacial zone along the normal direction of flat interfaces for the sample system at $4.0\ E_c/k$ and 10 000 MC cycles with $B/E_c$=0.1 after the LLPS has been completed at the same temperature for 200 000 MC cycles with $B/E_c$=0.5. (b) Orientational-order parameters of the largest crystalline clusters located in the vicinity of the interfacial zone with variable $B/E_c$ values as labeled. The order parameter of orientation is defined by $P$=($3(\cos^2\theta)-1$)/2, summed over the projections of all the orientations of the largest clusters in the direction normal to the flat interface. $\theta$ is the angle between the orientation of chain axes in the largest clusters and the direction normal to the flat interface $<...>$ represents an ensemble average. According to this definition, edge-on crystals (chain axes lay down on the interface) give a result of $P$=-0.5, the corresponding order parameter for flat-on crystals (chain axes stand up) is $P$=1, and randomly oriented crystals have $P$=0. The data were collected from 2000 samples under the same conditions described in Fig. 2. The lines between the data points are drawn to guide the eyes.

### C. Theoretical interpretation

The enthalpic contributions to the enhancement of crystal nucleation can be attributed to the fact that the immiscible component $NC$ tends to reject $C$ polymers detaching from the crystal. As such an effective repulsion of crystallizable polymers by the component $NC$ contributes to the stability of crystals, we conclude that the melting point of polymer crystals embedded in a mixture with $NC$ increases with the increase in the fractions of the component $NC$, i.e., upon dilution of the component $C$. This conclusion can be quantitatively verified by the calculations on the basis of the developed mean-field lattice theory of polymer blends.

We assume the homogeneous phase of a polymer blend with a total volume of $n$ lattice sites that contains two polymeric species of uniform chain length $r$ and of separate molecular numbers $n_1$ and $n_2$. This volume is in a regular lattice with the coordination number $q$, the first species $(C)$ is crystallizable $(E_p\neq0)$ while the second one $(NC)$ is noncrystallizable $(E_p=0)$. The partition function for such a homogeneous mixing state of the symmetric binary polymer blend is thus given by [10]
$$
Z=\left(\frac{n}{n_{1}}\right)^{n_{1}}\left(\frac{n}{n_{2}}\right)^{n_{2}}\left(\frac{q}{2}\right)^{n_{1}+n_{2}} z_{c}^{\left(n_{1}+n_{2}\right)(r-2)} e^{-\left(n_{1}+n_{2}\right)(r-1)} z_{p}^{n_{2}(r-1)} z_{m}^{n_{2} r},
\tag{1}
$$
where
$$
z_{c}=1+(q-2) \exp \left(-\frac{E_{c}}{k T}\right),
$$

$$
z_{p}=\exp \left\{-\frac{q-2}{2}\left[1-\frac{2 n_{2}(r-1)}{q n}\right] \frac{E_{p}}{k T}\right\},
$$

$$
z_{m}=\exp \left[-\frac{n_{1} r}{n} \frac{(q-2) B}{k T}\right].
$$

Here, $z_c$ represents a partition function for polymer microconformation, $z_m$ signifies a mean-field treatment of the mixing interactions between two species, and $z_p$ denotes a similar mean-field treatment of the anisotropic interactions between crystallizable bonds, while the other terms result from the combinational and partially conformational entropy for the homogeneous binary blends of symmetric polymers. At the melting point, the chemical potential equivalence between liquid and crystalline states applies, as given by
$$
\mu^{S}-\mu^{0}=\mu^{L}-\mu^{0}, \tag{2}
$$
where $\mu^0$ is the chemical potential of polymers at the fully ordered ground state. Since polymers in the crystal have a free energy $\Delta F$ close to those in the ground state, we have
$$
\mu^{S}-\mu^{0}=\frac{\partial \Delta F^{S}}{\partial n_{2}}=\frac{\Delta F^{S}}{n_{2}} \approx 0. \tag{3}
$$

The chemical potential of the liquid phase can be derived from the partition function expressed in Eq. (1). So, according to Eq. (2), one can obtain the equilibrium melting points for variable compositions of the crystallizable component $C$, as shown in Fig. 5.

From Fig. 5, one can see that, indeed, the melting points increase upon dilution of crystallizable polymers by the immiscible counterpart in the binary blends with $B>0$, while the melting-point curve is almost horizontal in the binary blends with $B=0$. In the theoretical calculations, crystallization is supposed to occur in homogeneous solutions without the coexistence of another phase transition. In real polymer systems, however, LLPS will set in before the melting-point curve has been reached on cooling, which turns the course of crystallization from initiated in a homogeneous phase to that occurring in a heterogeneous phase. For such a phase-separated system, dilution is forced to occur only at the diffuse interface, although at the interface the concentration of crystallizable polymers decreases quickly as the bulk phase of the noncrystallizable component has been approached. Thus in the cases of $B>0$, due to the rising up of the effec-

CRYSTAL NUCLEATION ENHANCED AT THE DIFFUSE ...
PHYSICAL REVIEW E 77, 061801 (2008)

![](./images/811917082789675009_5.jpg)

FIG. 5. Equilibrium melting temperatures of 16-mer crystals in the homogeneous phase of binary symmetric blends with variable volume fractions of crystallizable component at various $B/E_c$ values as denoted nearby, calculated from the developed mean-field lattice theory with $E_p/E_c$=1.

tive melting point at the interface and thus an increase in the depth of supercooling, crystal nucleation near such an interface will be thermodynamically enhanced.

The increase of melting points also depends upon the extent of dilution for $B>0$, as revealed in Fig. 5. Since more crystallizable polymers will be expelled from the interface with the increase of $B$, the thermodynamic enhancement for crystal nucleation will be less pronounced if the dilution of the crystallizable component at the interface becomes weak, i.e., for relatively narrower and sharper interfaces at higher values of $B$. This explains why the differences between various cases of $B>0$ are much smaller when they are compared to the differences of these cases from the case of $B$ =0.

## IV. CONCLUSIONS

By means of dynamic Monte Carlo simulations of binary polymer blends, a weak enhancement of crystal nucleation at the diffuse interface between two immiscible polymers can be evidenced, in accordance with the previously reported experimental observations. The developed mean-field lattice theory offers a reasonable interpretation to this intrinsic behavior of polymer blends.

The above theoretical conclusions do not rule out the effect of impurities commonly existing in real polymer blends, which could be mainly responsible for initiating the heterogeneous crystal nucleation at high temperatures. Nevertheless, at low temperatures when homogeneous crystal nucleation becomes fast and dominant, such an intrinsic preference of crystal nucleation may give rise to a relatively high density of crystal nuclei at the interface, and thus plays an important role in the determination of the structure-property relationship for immiscible or partially immiscible blends of semicrystalline polymers.

## ACKNOWLEDGMENTS

W.H. thanks Professor M. Muthukumar at the University of Massachusetts and Dr. Jamie Hobbs at the University of Sheffield for enlightening discussions. The funding from the Chinese Ministry of Education (Grant No. NCET-04-0448) and the National Natural Science Foundation of China (NSFC Grants No. 20474027 and No. 20674036) is appreciated. Y.M. and G.R. acknowledge partial financial support from the European Community's "Marie-Curie Actions" under Contract No. MRTN-CT-2004-504052 [POLYFILM].

[1] P. J. Flory, J. Chem. Phys. 10, 51 (1942).
[2] M. L. Huggins, Ann. N. Y. Acad. Sci. 43, 1 (1942).
[3] R. L. Scott, J. Chem. Phys. 17, 279 (1949).
[4] H. Tompa, Trans. Faraday Soc. 45, 1142 (1949).
[5] I. C. Sanchez and M. T. Stone, in *Polymer Blends: Formulation & Performance*, edited by D. R. Paul and C. B. Bucknall (Wiley, New York, 2000), Vol. 1, Chap. 2.
[6] K. F. Freed and J. Dudowicz, Adv. Polym. Sci. 183, 63 (2005).
[7] H. Wang, K. Shimizu, E. K. Hobbie, Z. G. Wang, J. C. Meredith, A. Karim, E. J. Amis, B. S. Hsiao, E. T. Hsieh, and C. C. Han, Macromolecules 35, 1072 (2002).
[8] G. Matsuba, K. Shimizu, H. Wang, Z. G. Wang, and C. C. Han, Polymer 44, 7459 (2003).
[9] X.-H. Zhang, Z.-G. Wang, R.-R. Zhang, and C. C. Han, Macromolecules 39, 9285 (2006).
[10] W.-B. Hu and D. Frenkel, Adv. Polym. Sci. 191, 1 (2005).
[11] W.-B. Hu and V. B. F. Mathot, J. Chem. Phys. 119, 10953 (2003).
[12] Y. Ma, W.-B. Hu, and H. Wang, Phys. Rev. E 76, 031801 (2007).
[13] T. Nishi and T. T. Wang, Macromolecules 8, 909 (1975).
[14] P. B. Rim and J. P. Runt, Macromolecules 17, 1520 (1984).
[15] W.-B. Hu and D. Frenkel, Macromolecules 37, 4336 (2004).
[16] L.-Y. Zha and W.-B. Hu, J. Phys. Chem. B 111, 11373 (2007).
[17] X.-H. Zhang, Z.-G. Wang, M. Muthukumar, and C. C. Han, Macromol. Rapid Commun. 26, 1285 (2005).
[18] X.-H. Zhang, Z.-G. Wang, X. Dong, D.-J. Wang, and C. C. Han, J. Chem. Phys. 125, 024907 (2006).
[19] R. L. Cormia, F. P. Price, and D. Turnbull, J. Chem. Phys. 37, 1333 (1962).
[20] J. Kraus, P. Mueller-Buschbaum, T. Kuhlmann, D. W. Schubert, and M. Stamm, Europhys. Lett. 49, 210 (2000).
[21] G. ten Brinke, D. Ausserre, and G. Hadziioannou, J. Chem. Phys. 89, 4374 (1988).
[22] S. K. Kumar, M. Vacatello, and D. Y. Yoon, J. Chem. Phys. 89, 5206 (1988).
[23] I. Bitsanis and G. Hadziioannou, J. Chem. Phys. 92, 3827 (1990).
[24] P. Doruker and W. L. Mattice, Macromolecules 31, 1418 (1998).
[25] C. Mischler, J. Baschnagel, and K. Binder, Adv. Colloid Interface Sci. 94, 197 (2001).
[26] P. J. Flory, J. Chem. Phys. 15, 397 (1947).

061801-5