# Atomic Arrangements in AuPt/Pt(100) and AuPd/Pd(100) Surface Alloys: A Monte Carlo Study Using First Principles-Based Cluster Expansions

J. Adam Stephens and Gyeong S. Hwang*

Department of Chemical Engineering, The University of Texas at Austin, Austin, Texas 78712, United States

ABSTRACT: We have constructed model Hamiltonians for AuPt/Pt(100) and AuPd/Pd(100) surface alloys based on the cluster expansion method and density functional theory. The cluster expansion Hamiltonians were used in Monte Carlo simulations to study the equilibrium arrangements of surface atoms in these two systems for a range of compositions and temperatures. We report on and explain results from these simulations in terms of the differing interatomic interactions present in each alloy. In AuPt surface alloys, homonuclear Pt−Pt interactions are favored over heteronuclear Au−Pt interactions, whereas in AuPd the opposite is true. Accordingly, our simulations show that Pt prefers to agglomerate, whereas Pd prefers to form smaller contiguous ensembles, such as monomers and dimers. Our simulations also reveal that the AuPd surface alloy can adopt c(2 × 2) ordering at low temperatures and 50% Pd coverage and exhibits a tendency for Pd monomers to occupy sites at the second nearest-neighbor distance from one another. Finally, we compare experimental data available in the literature to our results and find them in good qualitative agreement.

![](./images/813375281183064064_1.jpg)

## I. INTRODUCTION

Alloys often exhibit catalytic properties superior to those of their pure constituent metals. A number of recent articles have reported enhanced activity and selectivity of certain gold-based bimetallic alloys. Au−Pd surface alloys, for instance, have been shown to promote CO oxidation,¹,² the direct synthesis of hydrogen peroxide,³⁻⁵ vinyl acetate synthesis,⁶,⁷ and the hydrogen evolution reaction,⁸ among others. CO oxidation is also promoted by Au−Pt alloys,⁹ as well as n-hexane isomerization.¹⁰

Attempts to explain enhancements in the catalytic properties of alloys are usually marshaled in terms of two related phenomena: the geometric (ensemble) effect and the electronic (ligand) effect.¹¹⁻¹³ The ensemble effect is a change in the activity of a surface site due to particular arrangements of the two alloyed species in the site’s vicinity. The ligand effect acts through modification of the local electronic structure that results from interactions between the different metallic species. Clearly, both effects depend on the arrangement of atoms in and near the surfaces of alloys. Unraveling and exploiting the synergistic catalytic properties of alloys will require characterizing and controlling them at the atomic scale.

A number of experimental and theoretical studies have been undertaken to image or otherwise infer details about the surfaces of alloys with atomic resolution and also to explain catalytic function in terms of these details. Maroun et al.² examined monolayer AuPd surface alloys on Au(111) substrates and concluded that ensembles containing at least one Pd atom are necessary for CO oxidation, whereas hydrogen adsorption occurs on Pd ensembles no smaller than dimers. Chen et al.⁶ offered evidence that second nearest neighbor pairs of Pd atoms are responsible for the enhanced activity of the AuPd(100) surface toward vinyl acetate synthesis. Calculations reported by Hwang and co-workers¹⁴ suggest that Pd monomers surrounded by less active Au atoms are responsible for the heightened activity of AuPd surfaces toward direct H₂O₂ synthesis by suppressing O−O bond cleavage.

While studies such as these have been critical in advancing our understanding of catalysis on surface alloys, the difficulty of sample preparation and characterization has perhaps hindered efforts to systematically understand surface atomic arrangements using experiments. Theoretical efforts to supplement the available experimental data include the work of Boscoboinik et al., who examined AuPd(111) surfaces using a nearest-neighbor pair model,¹⁵ and that of Bergbreiter et al. on AuPt(111) surfaces using longer range pairs.¹⁶ Most recently, Stephens et al.¹⁷ compared the effects of differing interatomic interactions on atomic arrangement in AuPd and AuPt(111) surface alloys, taking into consideration multibody interactions. However, to the best of

Received: June 24, 2011
Revised: September 15, 2011
Published: September 26, 2011

our knowledge, no comparable reports have appeared in the literature that address atomic arrangement in fcc(100) surfaces.

In this article, we report the influence of temperature and surface composition on atomic arrangement in AuPd and AuPt-(100) surface alloys. We begin by describing a method for using density function theory calculations to construct cluster expansion Hamiltonians for use in Monte Carlo simulations. We then report and discuss the results of these simulations, specifically the populations of small ensembles of contiguous Pd or Pt atoms (monomers and dimers). We explain these in terms of the interatomic interactions present in AuPd and AuPt surface alloys. We also compare some of our predictions to available experimental data.

## II. COMPUTATIONAL METHODS

### A. Density Functional Theory.
Quantum mechanical calculations reported herein were performed on the basis of spin polarized density functional theory (DFT) within the generalized gradient approximation (GGA-PW91¹⁸), as implemented in the Vienna ab-initio simulation package (VASP).¹⁹ The projector augmented wave (PAW) method with a planewave basis set was employed to describe the interaction between ion cores and valence electrons. The PAW method is in principle an all-electron frozen-core approach that considers exact valence wave functions.²⁰ Valence configurations employed are 5d¹⁰ 6s¹ for Au, 4d⁹ 5s¹ for Pd, and 5d⁹ 6s¹ for Pt. An energy cutoff of 350 eV was applied for the planewave expansion of the electronic eigenfunctions. To model the fcc(100) surface, we used supercell slabs that consist of a square $4 \times 4$ surface unit cell. The cell includes four atomic layers, each of which contains 16 atoms. The bottom three layers are pure Pd(100) or Pt(100) slabs, and the topmost is a monolayer alloy of the same species with Au. A slab is separated from its periodic images in the vertical direction by a vacuum space corresponding to seven atomic layers. The upper two layers of each slab were fully relaxed using the conjugate gradient method until residual forces on all the constituent atoms became smaller than $5 \times 10^{-2}$ eV/Å, while the bottom two layers were fixed at corresponding Pd or Pt bulk positions. The lattice constants for bulk Pd, Pt, and Au are predicted to be 3.95, 3.98, and 4.18 Å, respectively, virtually identical to previous DFT-GGA calculations and also in good agreement with the experimental values of 3.89, 3.92, and 4.08 Å.²¹ For Brillouin zone integration, we used a $(2 \times 2 \times 1)$ Monkhorst-Pack mesh of k points to determine the optimal geometries. We increased the k-point mesh size up $(4 \times 4 \times 1)$ to refine the total energies for use in the training sets described in section II.B. Previous calculations suggest that the chosen parameters are sufficient for describing the surface properties of the model systems considered.¹⁴,²²

### B. Cluster Expansion and Monte Carlo.
The arrangement of atoms in AuPd or AuPt surface alloys at thermodynamic equilibrium is a function of both temperature and composition. We examined these arrangements for a range of conditions by carrying out Monte Carlo (MC) simulations (based on the cluster expansion method) in the canonical (constant NVT) ensemble.

In an MC simulation,²³ attempts to transition from one microstate to another are accepted with a probability related to the difference in their energy $\Delta E$ by the Boltzmann factor. That is, after a trial microstate is generated in a simulation at temperature $T$, a random number $\lambda$ is selected from the uniform distribution between 0 and 1, and the transition to the new microstate is accepted if $\lambda \leq \exp(-\Delta E/k_{\text{B}}T)$. After each attempt (successful or not), we collected several pieces of information about the current microstate, including a snapshot of the configuration, the size and number of ensembles of contiguous Pd or Pt atoms, and statistics related to the short-range order. In our simulations, we generated trial microstates by swapping two randomly chosen atoms of opposite types.

![](./images/813375281183064064_2.jpg)

Figure 1. Parity plots showing discrepancies between CE and DFT predictions. Filled, red circles are for the AuPd cluster expansion, and open, blue circles are for AuPt. The mean errors $(\bar{\varepsilon})$ are averages of the discrepancies over all surfaces in the training sets, each of which has 16 surface atoms.

The surfaces we simulated contained 900 surface atoms. In order to adequately sample the configuration space of a binary alloy, it is not unusual to attempt on the order of $10^{4}$ swaps per lattice site. Hence, we required a fast and accurate means of calculating how energy varies with atomic configuration. The cluster expansion (CE) method²⁴⁻³⁰ is a well-established technique for calculating the energies of crystalline, binary alloys. Lattice sites are assigned "spins" corresponding to the chemical species that occupy them (i.e., for Au and Pd, $s = +1$ and $-1$, respectively). The total energy of a system with $N$ lattice sites $[E(\hat{s}),\hat{s} = \{s_1, s_2, ..., s_N\}]$ is expanded in terms of clusters of these spins, which form a complete basis

$$
E(\hat{s}) = J_0 + \sum_{i} J_i s_i + \sum_{i<j} J_{ij} s_i s_j + \sum_{i<j<k} J_{ijk} s_i s_j s_k + \cdots \tag{1}
$$

where $J_o$, $J_i$, $J_{ij}$, and $J_{ijk}$ are the interaction coefficients [called effective cluster interactions (ECIs)] for the empty, point, pair, and three-body spin clusters. The complete expansion contains all possible clusters, but in practice it can be truncated to just a few of the most important terms without a great loss of fidelity.

The terms to be included and their associated ECIs can be determined by fitting to experimental data or to higher-order theory results. We constructed CE Hamiltonians by fitting to DFT-based training sets of small model surfaces meeting the description in section II.A. The training sets initially contained 30 model surfaces, but to help guard against the possibility of bias, they were iteratively expanded during the fitting procedure. In each iteration, a trial cluster expansion was created by identifying the subset of terms in a pool which included pairs and multibody interactions up to the third nearest-neighbor (3NN) distance that minimized the cross validation score³¹ with respect to the training set. The trial CE was used to predict new minimum-energy surfaces, which were then added to the training set. The trial CE was considered to be converged when it predicted no new minimum-energy surfaces. The AuPt training set was expanded by this procedure to contain a total of 49 model surfaces, and the AuPd training set contained 42. Figure 1 shows the discrepancies between the final CE- and DFT-predicted

![](./images/813375281183064064_3.jpg)

Figure 2. Ensemble sizes in a random fcc(100) surface alloy of two fictitious, noninteracting species. The unbroken plots show the fractions of atoms of one species which belong to ensembles of size n, as a function of that species' surface coverage in units of atomic percent. The dashed plot is for the monomer (n = 1) in the fcc(111) surface alloy, which has six first nearest-neighbors instead of four.

energies for the alloy surfaces in the training sets. The expansions themselves have been included in the online Supporting Information. A more detailed description of this method is available in ref 17.

## III. RESULTS AND DISCUSSION

### A. Atomic Arrangements in the Random, AuPd, and AuPt
Alloys. For the purpose of comparison, we first considered a random alloy, in which there are no interatomic interactions. Because there are no interactions, all microstates of a random alloy have the same energy, and therefore, regardless of the simulation temperature, the Boltzmann factor calculated for any given pair of microstates is equal to unity. The Boltzmann factor also approaches unity as $T \to \infty$ in nonrandom alloys, so the random alloy can be seen as representing the high temperature behavior of the AuPd and AuPt surface alloys.

Figure 2 shows the size distribution of ensembles of samespecies atoms which are contiguous through first nearest-neighbor (1NN) relationships as a function of coverage in units of atomic fraction $(\theta)$. Monomers ($n = 1$; that is, a single atom of one species that has four first nearest-neighbors of the opposite species) are seen to monotonically decrease with increasing $\theta$, while trends for larger-sized ensembles all pass through maxima. This can be understood by considering that the likelihood of creating a dimer or larger ensemble by placing an atom next to a monomer of the same species increases with $\theta$. For the same reason, the trends for the dimers and other, larger ensembles initially rise as $\theta$ increases and then begin to fall as they themselves are converted to still larger ensembles. The monomer trend for the (111) surface (dashed line), which is also included for comparison, lies significantly below the monomer trend for the (100) surface. This is due to the fact that every atom has six first nearest-neighbors with which to form larger ensembles in the (111) surface but only four first nearest-neighbors in the (100) surface.

The random alloy is a helpful guide to understanding qualitatively the arrangement of atoms in the AuPd and AuPt(100) surface alloys, to which we now turn. Snapshots (single microstates) from simulations of the random, AuPd, and AuPt alloys with $\theta = 0.15$ at $T = 300$ K are shown in Figure 3. Figure 4, panels a and b, shows the monomer and dimer trends in AuPd as a function of temperature and $\theta$, and Figure 5, panels a and b,

![](./images/813375281183064064_4.jpg)

Figure 3. Snapshots from simulations of (a) AuPd, (b) the random alloy, and (c) AuPt at $\theta = 0.15$ and $T = 300$ K. Note the tendency of Pt to agglomerate while the 1NN shells of most Pd atoms are filled entirely by Au.

![](./images/813375281183064064_5.jpg)

Figure 4. Average fraction of surface Pd atoms in (a) monomers and (b) dimers in AuPd surface alloys at several levels of coverage and temperature. As temperature increases, the monomer population declines, and the dimer population increases.

shows the same for AuPt. The corresponding random alloy ("infinite" temperature) results are also included on each plot.

In the AuPd alloy, all of the finite temperature monomer trends lie above the infinite temperature trend. In general, as temperature is lowered, an increasing number of Pd atoms are surrounded entirely by Au. The higher temperature trends decrease monotonically, just as the infinite temperature trend does, but at lower temperature, this ceases to be the case. A shoulder is apparent in the 300 K trend, the 200 K trend has a maximum, and the 100 K trend is nearly constant until it drops off suddenly, all at $\theta \approx 0.5$. The dimer plots for the AuPd alloy exhibit the opposite behavior in that they all lie beneath the infinite temperature plots, and the population of dimers is reduced as the temperature is lowered.

The temperature-dependent trends for the monomer and dimer populations in the AuPt alloy are quite different from those in the AuPd alloy. The populations of monomers at all finite temperatures are lower than in the random alloy and appear to increase with increasing temperature, the opposite of what was

![](./images/813375281183064064_6.jpg)

Figure 5. Average fraction of surface Pt atoms in (a) monomers and (b) dimers in AuPt surface alloys at several levels of coverage and temperature. As temperature increases, the monomer population also increases, and the peak in the dimer population shifts toward lower coverage.

![](./images/813375281183064064_7.jpg)

Figure 6. c(2 × 2) ordered surface. Every Pd (blue) atom has four Au (yellow) nearest neighbors, and vice versa.

found for AuPd. Although the populations of the dimers are also typically lower than in the infinite temperature case (except at low Pt coverage, where the trends cross), reducing the temperature appears mainly to have shifted the trends to lower $\theta$ rather simply reducing them as in the AuPd alloy.

Many of these observations can be explained in terms of the contrasting interatomic interactions in the AuPd and AuPt surface alloys. $^{17}$ In the AuPt alloy, homonuclear (Pt-Pt) interactions are energetically more favorable than heteronuclear (Pt-Au). This explains the relative scarcity of Pt monomers, which are completely surrounded by Au nearest neighbors. The AuPt dimer trends appear shifted to lower $\theta$ because of the tendency of Pt atoms to cluster into larger ensembles which contain more Pt-Pt interactions. As the temperature is reduced, dimers may be more readily formed from monomers available in the surface (resulting in a shift in the initial rise in the dimer population trends), but also more readily converted into trimers and other larger ensembles (resulting in a shift in the decline).

In contrast to AuPt, heteronuclear interactions dominate in the AuPd surface alloy, which leads to the energetic favorability of Pd monomers and, to a lesser extent, dimers at the expense of larger ensembles. The preference for Au-Pd interactions also leads to long-range ordering at low temperatures, which explains the unusual features centered around $\theta=0.5$ in the AuPd monomer plot. In the $c(2 \times 2)$ ordered surface (Figure 6), which is the ground state for this level of Pd coverage, every atom is surrounded by atoms of the opposite type, and the number of heteronuclear interactions is maximized. A related set of features occurs in the $AuPd(111)$ ensemble distributions due to the $(\sqrt{3} \times \sqrt{3}) R 30^{\circ}$ ordered surface. $^{17}$

B. Comparison of AuPd(100) Simulation Results to Experiment. Goodman and co-workers $^{32}$ have experimentally ascertained atomic arrangements in the (100) surface of one AuPd alloy sample. They prepared the (1:1 atomic ratio) sample by repeated cycles of $Ar^{+}$ sputtering and annealing, followed by annealing without sputtering at $550^{\circ} C$ for $30 ~min$. The sample was then permitted to cool to room temperature prior to STM imaging. Sample preparation and imaging were conducted in UHV conditions. The surface Pd coverage was determined by LEISS to be $\theta=0.1$. Statistics were collected from images of three separate locations on the surface. Rather than counting contiguous groups of atoms as we have in Figures 2, 4, and 5, unique arrangements of the 8 nearest neighbors (4 first nearest-neighbors plus 4 second nearest-neighbors; see the labels on the horizontal axis of Figure 7) surrounding every surface Pd atom were tallied. The totals from the images were compared to their corresponding

![](./images/813375281183064064_8.jpg)

Figure 7. Frequency of occurrence of different Pd site-types as predicted by simulation and reported by Goodman and co-workers based on their experimental observations. The site-types depicted on the horizontal axis are among the most probable in a random fcc(100) surface alloy with $\theta=0.1$. One site-type with a probability equal to that of the 4th has not been included because no experimental results were reported for it. The empty bars are an average of the site counts taken from three STM images and the error bars show the maximum and minimum. The filled gray bars are for the random alloy and the points are the simulation predictions for temperatures between 300 and $800 ~K$.

![](./images/813375281183064064_9.jpg)

Figure 8. (a) Short-range order parameter $(\alpha)$ at the 1st, 2nd, and 3rd nearest neighbors distances for a AuPd surface with $\theta=0.1$. The horizontal, dotted reference line is for the random alloy, which has no SRO $(\alpha=0)$. $\alpha<0$ indicates heteronuclear correlation and $\alpha>0$ indicates homonuclear. The inset shows $\alpha$ for the AuPt surface alloy at the same $\theta$. In (b) (lower left) and (c) (lower right), arrows indicate some small regions of 2NN Pd-Pd correlation in snapshots from simulations of the AuPd surface at $T=300$ and $600 \mathrm{~K}$.

expectation values in the random alloy, which were analytically calculated.

In Figure 7, we have reproduced some of the results they reported along with our MC predictions for a AuPd surface alloy with $\theta=0.1$. Simulation results for a range of temperatures (300-800 K) have been included since it is difficult to know unambiguously the equilibration temperature that the experimental results represent. Although the alloy we modeled differs from the experimental sample in that it was confined to the topmost layer of a pure Pd substrate, the two sets of results are in basic agreement with regard to the direction of the deviation from the random alloy. That is, in both the experimental results and the MC predictions, site-type 1 was encountered somewhat less frequently than would be expected in a random alloy, site-type 2 also less, site-type 3 more, and so on. Site-types 4 and 5 are exceptions; however, together they account for only a small fraction of Pd sites, and in both cases, the simulation results and the random probabilities are within the window of experimental observations. The correspondence between experiment and simulation helps to validate our approach, the uncertainty in the equilibration temperature, relatively small number of STM images included in the analysis, and confinement of Au atoms to the surface layer notwithstanding. We further believe that our findings lend support to the proposal that, "the thermodynamic properties of AuPd alloys can be used to tailor surface ordering", $^{32}$ at least in some cases.

C. Additional Short-Range Order in AuPd(100): 2NN Pairs of Pd Monomers. Examination of both the 1NN and 2NN shell around every surface Pd atom highlights a manifestation of AuPd interatomic interactions which is not readily apparent from the plots of monomers and dimers in Figures 4 and 5 and which extends beyond the distinction between homo- and heteronuclear interactions which we have so far employed. The central atoms in site-types 1,3 , and 6 in Figure 7 are all Pd monomers which have four Au first-nearest neighbors. It is in their 2NN shells that the three site-types differ from one another. It is apparent that Pd monomers with no Pd second nearest neighbors (site-type 1) are somewhat less likely than in the random alloy, while those with one or two (site-types 3 and 6) are a great deal more likely. The short-range order (SRO) parameter $^{33}$ $\alpha(r)=1-p_{\mathrm{AB}}(r) / x_{\mathrm{B}}$, where $x_{\mathrm{B}}$ is the overall fraction of the surface atoms which are species $\mathrm{B}$, and $p_{\mathrm{AB}}(r)$ is the probability of finding a B atom a distance of $r$ from an A atom, shows this as well [Figure 8a]. In a completely random alloy, $\alpha(r)$ is always 0 . In the simulated AuPd alloys, at the 1NN distance, $\alpha$ is negative, indicating a surplus of $\mathrm{Pd}-\mathrm{Au} 1 \mathrm{NN}$ pairs. At the $2 \mathrm{NN}$ distance, $\alpha$ is positive, showing $\mathrm{Pd}-\mathrm{Pd}$ correlation. Some SRO persists at the $3 \mathrm{NN}$ neighbor distance, but it is much lower. The simulation snapshots in Figure 8, panels b and c, help to illustrate these more quantitative measures of atomic arrangement. White arrows indicate a few of the small patches of Pd monomers standing at the second and third nearest neighbor distance from one another. A plot of $\alpha(r)$ for a AuPt surface alloy at the same temperature and level of coverage is included in the inset of Figure 8a for comparison.

It is instructive to compare the DFT-predicted formation energies of an isolated Pd monomer and the $c(2 \times 2)$ ordered surface, in which all 1NN interactions are heteronuclear and all $2 \mathrm{NN}$ interactions are homonuclear. The formation energies were calculated using $E_{\mathrm{f}}=\left\{E_{\mathrm{AuPd}}-E_{\mathrm{Au}}+N_{\mathrm{Pd}}\left(E_{\mathrm{Au}-\text { bulk }}-E_{\mathrm{Pd}-\text { bulk }}\right)\right\} /$ $N_{\mathrm{Pd}}$, where $E_{\mathrm{AuPd}}, E_{\mathrm{Au}}, E_{\mathrm{Au}-\text { bulk }}$, and $E_{\mathrm{Pd}-\text { bulk }}$ represent the total energies of $\mathrm{AuPd} / \mathrm{Pd}(100), \mathrm{Au} / \mathrm{Pd}(100)$, bulk $\mathrm{Au}$ (per atom), and bulk Pd (per atom), respectively, and $N_{P d}$ indicates the number of Pd atoms in the AuPd surface alloy. We found that the formation energy per Pd atom of a monomer is about $0.02 \mathrm{eV}$ higher than that of the $c(2 \times 2)$ ordered surface.

The lower $E_{\mathrm{f}}$ of the $c(2 \times 2)$ ordered surface helps explain the abundance of sites that include $2 \mathrm{NN} \mathrm{Pd}-\mathrm{Pd}$ pairs in Figure 7, the degree of $2 \mathrm{NN}$ SRO seen in Figure 8a, and the visible patches of ordered monomers in Figure 8, panels b and c. It also highlights the danger of neglecting longer range (>1NN) interactions when modeling surface alloys. A Hamiltonian that includes only $1 \mathrm{NN}$ pair interactions would yield the same $E_{\mathrm{f}}$ for the Pd monomer and the $c(2 \times 2)$ ordered surface and thus would be expected to incorrectly predict their relative contributions to ensemble averaged properties of AuPd surface alloys. It is true that heteronuclear, $1 \mathrm{NN}$ pair interactions can produce some degree of SRO at longer range because they in effect "push" like atoms out of the 1NN shell into longer range shells which they consequently enrich. However, when we adjusted a $1 \mathrm{NN}$ pair model to yield the same SRO at the $1 \mathrm{NN}$ distance as our cluster expansion at $T=500 \mathrm{~K}$ and $\theta=0.1$, it predicted negligible $2 \mathrm{NN}$ SRO, in sharp contrast to both the experimental and cluster expansion-based simulation results. Since correctly predicting $2 \mathrm{NN}$ SRO may be important in explaining the catalytic properties of surface alloys, $^{6}$ this discrepancy argues against the use of $1 \mathrm{NN}$ pair models for this purpose.

## IV. SUMMARY

Using density-functional theory calculations, we created two cluster expansion Hamiltonians, one for $\mathrm{AuPd} / \mathrm{Pd}(100)$ surface alloys and the other for $\mathrm{AuPt} / \mathrm{Pt}(100)$. Pair and multibody interactions up to the $3 \mathrm{NN}$ distance were considered for inclusion in the models. The cluster expansions were used in canonical

ensemble Monte Carlo simulations of AuPd and AuPt surface alloys over a range of temperature and Pd or Pt coverage. The simulations show that the differing interatomic interactions present in the two alloys result in dramatically different arrange- ments of atoms. In the AuPt alloy, in which homonuclear (Pt−Pt) interactions prevail, the population of isolated Pt monomers is depressed compared to the random alloy, but increases with temperature. The population of Pt dimers exhibits a maximum which is shifted toward lower coverage as the temperature decreases. Heteronuclear (Au−Pd) interactions are stronger in the AuPd alloy, which favors the formation of monomers and, to a lesser extent, dimers. The population of Pd monomers decreases with temperature, while the dimer popula- tion increases. At low temperature and a Pd coverage of $\theta = 0.5$, heteronuclear interactions also lead to the formation of a $c(2 \times 2)$ ordered surface, in which the four first nearest-neighbors of every atom is of the opposite species. We also compared some of the results from our simulations of the AuPd surface alloy to the reported experimental findings of Goodman and co-workers. The two were found to be in substantial agreement, lending sup- port to our approach and also to their proposal that the thermo- dynamics of AuPd alloys might be used to tailor their surface atomic arrangements. One observation common to both our simulations and their experiments is the existence of a greater- than-expected number of 2NN pairs of Pd monomers; the catalytic importance of this ensemble has already been demon- strated experimentally. It is noteworthy that Hamiltonians based only on 1NN pair interactions would appear to be inadequate to account for the frequency with which 2NN Pd pairs are encountered in the AuPd (100) surface. These results increase our confidence that our approach, Monte Carlo simulation based on cluster expansions, is capable of providing insight into the atomic arrangements of surface alloys for the purpose of eluci- dating their catalytic properties.

## ASSOCIATED CONTENT

Supporting Information. Table of cluster expansions. This material is available free of charge via the Internet at http:// pubs.acs.org.

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: gshwang@che.utexas.edu.

## ACKNOWLEDGMENT

We acknowledge the Robert A. Welch Foundation (F-1535) and the National Science Foundation (NSF-IGERT Grant DGE- 0549417) for the support of this work. All our calculations were performed using supercomputers at the Texas Advanced Com- puting Center at the University of Texas.

## REFERENCES

(1) Gao, F.; Wang, Y.; Goodman, D. W. *J. Phys. Chem. C* 2009, 113, 14993−15000.
(2) Maroun, F.; Ozanam, F.; Magnussen, O. M.; Behm, R. J. *Science* 2001, 293, 1811−1814.
(3) Edwards, J. K.; Carley, A. F.; Herzing, A. a; Kiely, C. J.; Hutchings, G. J. *Faraday Discuss* 2008, 138, 225−239.
(4) Abate, S.; Centi, G.; Melada, S.; Perathoner, S.; Pinna, F.; Strukul, G. *Catal. Today* 2005, 104, 323−328.
(5) Samanta, C. *Appl. Catal., A* 2008, 350, 133−149.
(6) Chen, M.; Kumar, D.; Yi, C.-W.; Goodman, D. W. *Science (New York, N.Y.)* 2005, 310, 291−293.
(7) Yi, C.-W.; Luo, K.; Wei, T.; Goodman, D. W. *J. Phys. Chem. B* 2005, 109, 18535−18540.
(8) Pluntke, Y.; Kibler, L. A.; Kolb, D. M. *Phys. Chem. Chem. Phys.* 2008, 10, 3684−3688.
(9) Auten, B. J.; Lang, H.; Chandler, B. D. *Appl. Catal., B* 2008, 81, 225−235.
(10) Sachtler, J. W. A.; Somorjai, G. A. *J. Catal.* 1983, 81, 77−94.
(11) Liu, P.; Nørskov, J. K. *Phys. Chem. Chem. Phys.* 2001, 3, 3814−3818.
(12) Groß, A. *Top. Catal.* 2006, 37, 29−39.
(13) Burch, R. *Acc. Chem. Res.* 1982, 15, 24−31.
(14) Ham, H. C.; Hwang, G. S.; Han, J.; Nam, S. W.; Lim, T. H. *J. Phys. Chem. C* 2009, 113, 12943−12945.
(15) Boscoboinik, J. a; Plaisance, C.; Neurock, M.; Tysoe, W. T. *Phys. Rev. B* 2008, 77, 1−6.
(16) Bergbreiter, A.; Alves, O. B.; Hoster, H. E. *ChemPhysChem* 2010, 11, 1505−1512.
(17) Stephens, J. A.; Ham, H. C.; Hwang, G. S. *J. Phys. Chem. C* 2010, 21516−21523.
(18) Perdew, J. P.; Wang, Y. *Phys. Rev. B* 1992, 45, 13244−13249.
(19) Kresse, G.; Furthmüller, J. *VASP the Guide*; Vienna University of Technology: Vienna, Austria, 2001.
(20) Blöchl, P. E. *Phys. Rev. B* 1994, 50, 17953−17979.
(21) Campbell, C. T. *Annu. Rev. Phys. Chem.* 1990, 41, 775−837.
(22) Ham, H. C.; Hwang, G. S.; Han, J.; Nam, S. W.; Lim, T. H. *J. Phys. Chem. C* 2010, 114, 14922−14928.
(23) Frenkel, D.; Smit, B. *Understanding Molecular Simulation: From Algorithms to Applications*; Academic Press: San Diego, CA, 1996.
(24) Connolly, J.; Williams, A. *Phys. Rev. B* 1983, 27, 5169−5172.
(25) Ferreira, L.; Wei, S.; Zunger, A. *Phys. Rev. B* 1989, 40, 3197−3231.
(26) Laks, D. B.; Ferreira, L.; Froyen, S.; Zunger, A. *Phys. Rev. B* 1992, 46, 12587−12605.
(27) Blum, V.; Zunger, A. *Phys. Rev. B* 2004, 70, 155108.
(28) Blum, V.; Zunger, A. *Phys. Rev. B* 2004, 69, 020103.
(29) Barabash, S. V.; Blum, V.; Müller, S.; Zunger, A. *Phys. Rev. B* 2006, 74, 035108.
(30) Yuge, K.; Seko, A.; Kuwabara, A.; Oba, F.; Tanaka, I. *Phys. Rev. B* 2007, 76, 045407.
(31) van De Walle, A.; Ceder, G. J. *Phase Equilib.* 2002, 23, 348−359.
(32) Han, P.; Axnanda, S.; Lyubinetsky, I.; Goodman, D. W. *J. Am. Chem. Soc.* 2007, 129, 14355−14361.
(33) Cowley, J. *Phys. Rev.* 1950, 77, 669−675.