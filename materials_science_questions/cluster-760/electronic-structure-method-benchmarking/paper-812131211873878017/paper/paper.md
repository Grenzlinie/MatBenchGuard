PHYSICAL REVIEW B 72, 155428 (2005)

# Molecular hydrogen confined within nanoporous framework materials: Comparison of density functional and classical force-field descriptions

A. W. C. van den Berg, $^{1}$ S. T. Bromley, $^{2, *}$ J. C. Wojdel, $^{1}$ and J. C. Jansen $^{1}$ 

$^{1}$ Ceramic Membrane Centre "The Pore," Delft University of Technology, Julianalaan 136, 2628 BL, Delft, The Netherlands
$^{2}$ Department Quimica Fisica and Centre Especial de Recerca en Quimica Teorica, Universitat de Barcelona and Parc Cientific, c/Marti i Franques 1, E-08028 Barcelona, Spain

(Received 21 July 2005; published 24 October 2005)

The effect of confinement on the energetics, structure, and absorption of molecular hydrogen is calculated via systematically increasing the $H_{2}$ loading in the relatively inert nanoporous siliceous material sodalite (SOD). Treatments of both the $H_{2}-H_{2}$ and $H_{2}$-SOD interactions by both periodic density functional theory (DFT) employing four different functionals (LDA, PW91, PBE, and BLYP) and by two accurately parameterized force-field (FF) sets are critically compared. We find for all loadings of $H_{2}$ molecules the results differ significantly depending on the method employed. Through a detailed analysis of the $H_{2}-H_{2}$ and $H_{2}$-SOD interactions in each case we assess the performance of each method employed. We find that none of the tested functionals appear to give a good overall description of our confined $H_{2}$ cluster system and the use of well-parameterized FFs is recommended for obtaining a reasonable physical description of such systems.

DOI: 10.1103/PhysRevB.72.155428
PACS number(s): 82.75.Mj

## I. INTRODUCTION

Understanding the behavior of molecular hydrogen at high densities, either through nanoscale confinement or via high pressures applied to the bulk phase, is extremely important from a fundamental physical perspective. It is also increasingly important recently, due to the application potential of efficient storage of hydrogen as a clean portable energy resource. For the purposes of studying both bulk and clusters of $H_{2}$ molecules numerous $H_{2}-H_{2}$ interaction potentials have been developed through the consideration of experimental data, $^{1-5}$ and via high level $ab$ initio calculations of $H_{2}$ dimers. $^{6-9}$ Such potentials have been extensively used and range in complexity from simple two parameter Lennard-Jones forms to more accurate multiparameter potential forms (e.g., Buck et al., Silvera-Goldman). $^{1,4,10}$ Many such potentials describe the weak intermolecular hydrogen interaction in a spherically symmetric manner, which is found to be an excellent approximation when the results of their usage are compared with experimental data. The accuracy of such centrosymmetric $H_{2}-H_{2}$ potentials is also evidenced by their use in the setup of high level quantum mechanical calculations of $H_{2}$ cluster systems, $^{11,12}$ the calculation of the properties of bulk dense $H_{2}$ phases, $^{2,3}$ and also for larger scale classical molecular dynamics calculations. $^{13-15}$ More recently the use of density functional theory (DFT) has been widespread for estimating the properties of $H_{2}$ in confined systems. $^{15-21}$ In such studies the binuclear aspect of the $H_{2}$ molecule is explicit and the $H_{2}-H_{2}$ interaction is provided in an $ab$ initio electronic manner albeit indirectly via the choice of functional. In particular, the DFT method has been often applied to systems of interacting $H_{2}$ molecules within the confines of inorganic and organic fullerene cages, $^{16,17}$ and of carbon nanotubes, $^{15,18-20}$ between graphene sheets, $^{21}$ and also to solid phase bulk $H_{2} \cdot^{22,23}$

In this study we investigate the effects of increasing the hydrogen loading of the confining nanopores of the framework silica material sodalite (SOD) both with classical calculations employing two different specifically parameterized force-field (FF) sets, and further by first principles calculations employing periodic DFT with four different functionals. The agreement between FF and DFT results is generally found to be poor with the choice of functional having a strong influence on the results. We ascribe this discrepancy between classical and quantum approaches mainly on the apparent inability of the functionals employed to accurately describe both the $H_{2}$-framework and the $H_{2}-H_{2}$ interactions simultaneously.

## II. COMPUTATIONAL METHODOLOGY

### A. General considerations

In both the classical FF and the quantum DFT calculations a deliberate effort was made to treat the systems in a similar manner as possible in order to facilitate a comparison of the results. In particular, in both sets of calculations (i) the same cell parameters were employed for the SOD framework, (ii) all optimizations were performed at constant cell volume, (iii) all $H_{2}$ loading is within one isolated SOD cage, and (iv) the same pattern of $H_{2}$ molecular loading was employed. For SOD cubic symmetry implies that all cell vectors are of equal length, and that all angles between them are $90^{\circ}$. Following van den Berg, $^{14}$ in all calculations the lattice constant was taken to be that obtained from a constant pressure energy minimization of the empty sodalite framework using the BFGS algorithm and the FF developed by Sanders et al. $^{24,25}$ This FF utilizes a Buckingham potential form for Si-O and O-O interactions, a harmonic O-Si-O three body term, and a spring constant to define a negative shell around a positive oxygen core, and has been proven to accurately reproduce various zeolite structures, $^{26-29}$ their relative energies, $^{26}$ and zeolite vibrational properties in energy minimization calculations. $^{30}$ The resulting cell parameter of $8.77\ \mathring{A}$ can

1098-0121/2005/72(15)/155428(7)/$23.00
155428-1
©2005 The American Physical Society

<table>
<caption>TABLE I. The difference in total system energy and in unit cell volume between constant pressure and constant volume loading calculations for both FFs employed.</caption>
<thead>
<tr>
<th rowspan="3">No. of H₂<br>molecules per<br>SOD cage (-)</th>
<th colspan="2">Total system energy<br>difference [$\Delta E$]<br>($10^{-3}$ eV)</th>
<th colspan="2">Unit cell volume<br>difference [$\Delta V$] (vol %)</th>
</tr>
<tr>
<th>FF (Bruce⁸)</th>
<th>FF (Buckᵇ)</th>
<th>FF (Bruce⁸)</th>
<th>FF (Buckᵇ)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0.21</td>
<td>−0.009</td>
<td>−0.009</td>
</tr>
<tr>
<td>2</td>
<td>1.76</td>
<td>0.10</td>
<td>−0.008</td>
<td>−0.010</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>0.21</td>
<td>−0.006</td>
<td>−0.013</td>
</tr>
<tr>
<td>4</td>
<td>0</td>
<td>−0.83</td>
<td>−0.006</td>
<td>−0.020</td>
</tr>
<tr>
<td>5</td>
<td>0.93</td>
<td>0</td>
<td>0.071</td>
<td>0.012</td>
</tr>
<tr>
<td>6</td>
<td>3.32</td>
<td>−1.55</td>
<td>0.104</td>
<td>0.023</td>
</tr>
<tr>
<td>7</td>
<td>2.80</td>
<td>−2.18</td>
<td>0.195</td>
<td>0.064</td>
</tr>
<tr>
<td>8</td>
<td>6.11</td>
<td>3.42</td>
<td>0.293</td>
<td>0.130</td>
</tr>
<tr>
<td>9</td>
<td>19.38</td>
<td>12.23</td>
<td>0.530</td>
<td>0.264</td>
</tr>
</tbody>
</table>
ᵃReference 1.
ᵇReference 4.

also be considered well optimized with respect to periodic DFT optimizations of the SOD framework.³¹ For the subsequent FF and DFT H₂-loaded SOD calculations the cell parameters were fixed but the positions of all atoms were allowed to vary. In Table I we report the extremely small difference in total system energy and unit cell volume if we also allow for the SOD unit cell to respond to the loading of confined H₂ molecules during the FF calculations. In order to avoid the complication of interactions of H₂ with other molecules in neighboring cages we only consider loading of H₂ within a relatively isolated SOD cage (rather than the homogeneous loading of all periodic cages). The assumption that the loading of an isolated cage has little influence on the energy and the volume per cage as a function of loading as compared to the homogeneous case is verified in van den Berg.³² The pattern of H₂ loading in both FF and DFT calculations follows that in van den Berg,³² which was obtained through extensive FF based searches for low energy loading arrangements. For the DFT calculations the centers of mass of the H₂ molecules were placed at the FF derived positions and then their positions were fully optimized. It was found in DFT calculations that the FF derived H₂ arrangements were stable minima and that the H₂ molecules would simply rotate to achieve their most favorable pattern of interaction. Starting from the same H₂ arrangement but with different internal H₂ orientations was nearly always found to yield the same resulting pattern of H₂-H₂ interactions. When found to differ, the lowest energy arrangement was taken although the energy difference between differently oriented arrangements was always found to be almost negligible and is not likely to be a significant factor in explaining the differences between the FF and DFT results obtained.

### B. Force-field methodology

The FFs representing the interactions between the hydrogen molecule and the atoms of the SOD framework are based on experimental data and are of a Lennard-Jones (LJ) form:³³

$$
E_{\mathrm{LJ}}=4 \varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right]. \tag{1}
$$

Here, $E_{\mathrm{LJ}}$ represents the nonbonding Lennard-Jones energy [eV], $\varepsilon$ represents the minimum energy of the potential curve [eV], $\sigma$ represents the atom-atom distance at zero energy [Å], and $r$ represents the atom-atom distance [Å]. The $\varepsilon$ and $\sigma$ values are [0.002254531 eV, 1.8175 Å] and [0.005270509 eV, 2.8330 Å] for the Si-H₂ and the O-H₂ interactions, respectively.³³

The cutoff employed for all nonbonding interactions is 13 Å. For further validation of this potential with respect to H₂ loading and diffusion within nanoporous silica frameworks we refer to van den Berg.¹⁴,³²

For the H₂-H₂ interaction FF we have employed two different potentials together with the Si-H₂ and O-H₂ FFs described above. The first H₂-H₂ FF is simply represented by the LJ potential form [Ref. 1] given in Eq. (1) (employing $\varepsilon$ and $\sigma$ parameters: 0.003165375 eV and 2.958 Å) and has been successfully used in path integral Monte Carlo calculations of solid and liquid bulk parahydrogen.²,³ The second potential form employed for the H₂-H₂ interaction is that developed by Buck⁴,⁵ through consideration of experimental D₂+H₂ scattering experiments and ab initio calculations:

$$
\begin{gathered}
E_{\text {Buck }}=A \exp \left[-\beta r-\gamma r^{2}\right]-\left(\frac{C_{6}}{r^{6}}+\frac{C_{8}}{r^{8}}+\frac{C_{10}}{r^{10}}\right) D(r) \\
\text { for } r \leqslant G ; \quad D(r)=\exp \left[-(G / r-1)^{2}\right] \\
\text { for } r \geqslant G ; \quad D(r)=1. \tag{2}
\end{gathered}
$$

Here, $E_{\text {Buck }}$ represents the nonbonding energy [eV] between H₂ molecules, $A$, $G$, $\beta$, $\gamma$, $C_{6}$, $C_{8}$, and $C_{10}$ are the empirical potential parameters (101.4 eV, 5.102 Å, 2.779 Å⁻¹, 0.08 Å⁻², 7.254 eV Å⁶, 36.008 eV Å⁸, and 225.56 eV Å¹⁰) and $r$ represents the atom-atom distance [Å]. This potential takes a considerably more complicated form than the LJ FF [Eq. (1)] and has been employed in accurate quantum Monte Carlo calculations of small, (H₂)_N$N$<10, hydrogen clusters.¹¹,¹²

Both complete sets of potentials were implemented in the computer code GULP (General Utility Lattice Program),³⁴ which was used to calculate the optimized system energy and unit cell volume of a SOD system loaded with $N$ hydrogen molecules ($N$=0–10). The SOD structure was represented by two cages (overall composition: Si₁₂O₂₄) per cell with periodic boundary conditions, and with hydrogen only loaded within one cage.³⁵

### C. DFT methodology

For the DFT calculations we employed the pseudopotentials-plane-wave (PP-PW) method for solving the Kohn-Sham equations as implemented in the CPMD code³⁶ using the (PW91) functional due to Perdew and Wang,³⁷ the Perdew, Burke and Ernzerhof (PBE) functional,³⁸ the local density approximation (LDA)

![](./images/812131211873878017_1.jpg)

FIG. 1. Total system energies of molecular hydrogen loadings in SOD as calculated by periodic FF calculations using the FFs due to Bruce et al. (Ref. 1) and Buck et al. (Ref. 4). Energies are given relative to the empty SOD cage.

functional, $^{39}$ and the BLYP functional (the exchange correction of Becke and the correlation function of Lee, Yang, and Parr). $^{40}$

The PP-PW formalism employs the use of pseudopotentials in order to smooth the wave function for the efficient representation with plane waves. In our calculations we used ultrasoft pseudopotentials (USPP), which achieve their efficiency by significantly smoothing the wave function in the core region and relaxing the norm conserving constraint of harder PPs. The employed Vanderbilt USPPs were generated using version 7.3.4 of the USPP generation code. $^{41,42}$ Since in this study we are employing a moderately large supercell with localized $H_{2}$ absorption, together with the fact that SOD is a wide band gap insulator having a rather flatband structure, calculations were performed at the gamma point only. The energy cutoff for the calculations was set to 60 Rb (816 eV) at which it was found that energy of the unit cell with $13 H_{2}$ molecules inside was fully converged. The SOD structure was again represented by a cubic unit cell, containing two sodalite cages, with periodic boundary conditions. All calculations were performed in only one of the cages in order to stay as consistent with the FF calculations as possible.

## III. RESULTS AND DISCUSSION

For both the FF and DFT calculations the absorption energy $(E_{abs})$ of $H_{2}$ molecules within a SOD cage was calculated using

$$
E_{a b s}=E_{L C}-E_{E C}-N_{\mathrm{H}_{2}} E_{\mathrm{H}_{2}}. \tag{3}
$$

$E_{LC}$ is the energy of the loaded system as obtained from the respective calculation, $E_{EC}$ is the energy of the empty SOD system, $N_{\mathrm{H}_{2}}$ is the number of hydrogen molecules in the cage, and $E_{\mathrm{H}_{2}}$ is the energy of an isolated $H_{2}$ molecule.

The nonbonding interaction energy between a single hydrogen molecule and the SOD framework is found to be of a very similar order of magnitude for both FF based calculations and the PW91 based DFT calculations, giving $-65$ $\times 10^{-3}$ eV (PW91) and $-57 \times 10^{-3}$ eV (FFs), respectively. For the other three functionals employed the agreement with the FF calculations is somewhat worse with interaction energies of $-124 \times 10^{-3}$ eV (LDA), $-25 \times 10^{-3}$ eV (PBE), $+41 \times 10^{-3}$ eV (BLYP). For higher $H_{2}$ loading $E_{abs}$, as calculated via Eq. (3), involves increasing contributions to the system energy from $H_{2}$-$H_{2}$ interactions and as such $E_{abs}$ then gives an average total interaction energy per $H_{2}$ molecule.

The dependence of the system energy on $H_{2}$ cage loading is given in Fig. 1 as calculated with the two FFs. Here in each case the $H_{2}$-SOD interaction is dealt with using the same interaction potential and thus differences in the two graphs are solely due to the different representations of the internal $H_{2}$-$H_{2}$ interaction. For both FFs the quantitative and qualitative similarities are striking showing that, despite the differences in apparent sophistication of their respective potential forms, both FF models give a consistent prediction of the energetics of $H_{2}$ loading in SOD.

The total system energy change as a function of hydrogen loading as calculated via the periodic DFT method for the four different functionals is given in Fig. 2. For comparison, the system energies calculated using the Buck *et al.* FF are given again. $^{4,5}$ Figure 2 shows that the agreement between the $H_{2}$ loading curves for all methods becomes increasingly worse for loadings from two to six $H_{2}$ molecules. For loadings above eight $H_{2}$ molecules, the FF calculations indicate that $H_{2}$-$H_{2}$ repulsion becomes so large that energetically fa-

![](./images/812131211873878017_2.jpg)

FIG. 2. Total system energies of molecular hydrogen loadings in SOD as calculated by periodic DFT (BLYP, PW91, PBE, LDA) and FF [Buck et al. (Ref. 4)] calculations. Energies are given relative to the empty SOD cage.

vorable storage is not possible any more (the uptake of more hydrogen molecules would be an endothermic process). The DFT calculations, however, display a range of behaviors de- pending on the type of functional employed. For the LDA calculations, starting from the empty SOD cage, the $H_2$ load- ing curve immediately drops below that of the FFs, showing an energetically more favored description of $H_2$ absorption. The system energy per $H_2$ molecule continues to fall until a loading of six $H_2$ molecules where upon the system energy levels off until at least $13 H_2$ molecules are energetically favorably confined with the SOD cage. For loadings larger than 13 hydrogen molecules it was not possible to find a cluster configuration that was stable within the SOD cage(during the optimizations for $N>13, H_2$ molecules are found to spontaneously force themselves through $Si_6O_6$ six-ring ap ertures into a neighboring cage). For PW91 and PBE the behavior is strikingly different with only a small range ofweakly negative system energies observed for up to two $H_2$ molecules. Thereafter, for loadings of three and more $H_2$  molecules, the system energies are increasingly positive showing unfavorable energetics for $H_2$ confinement in the SOD cage. For the BLYP functional the energy vs loading behavior is found to be always positive and increasingly so with increasing $H_2$ loading.

In both the FF and DFT energy minimization calculations described above there is no account made of zero point mo- tion which can be significant for condensed hydrogen phases. However, as this factor is absent in both sets of calculations it cannot be the cause of the large observed difference be- tween the two approaches. Moreover, considering that the discrepancy between the two methods becomes increasingly prominent with increasing confinement (or at higher pres- sures) and that the structure and energy of the $H_2$ phase at such conditions is then predominantly determined by the in- teractions between hydrogen molecules with each other and/or the SOD cage wall atoms, the observed differences can be ascribed to the differing representations of these in- teractions.

In order to assess the influence of the $H_2$ - $H_2$ interaction on the total system energy, the optimized SOD-confined hy- drogen clusters (see Fig. 3) from both the FF and DFT cal- culations were isolated and their energies were separately calculated via single point calculations using the respective methodology. Subtracting $N$ times the energy of an isolated $H_2$ molecule from the $(H_2)_N$ cluster energy gives the energy term resulting from the $H_2$ - $H_2$ interaction ( $H_2$ - $H_2$ energy) in the cluster (see Fig. 4). The interaction energy between the $(H_2)_N$ cluster as a whole and the SOD cage (cluster-SOD energy) can be also be estimated by subtracting the total free cluster energy and the energy of the empty system from the total system energy (see Fig. 5). In this way the $H_2$ - $H_2$ en ergy and the cluster-SOD energy are simply a partitioning of the total system energy into two physically important contri- butions.

For a $(H_2)_N$ loading of approximately $N<5$ the cluster SOD energies (Fig. 5) for both the FF and DFT calculatedsystems are very similar to the total system energies (Fig. 2) and the $H_2$ - $H_2$ energies (Fig. 4) are correspondingly rela tively small. Here the differences in the $H_2$ interactions with the framework are thus mainly responsible for the discrepan- cies in total system energy between the two methods. For N>5 the differences between the cluster-SOD energies and total system energies becomes significant for both FF and DFT calculations indicating that the different representation

![](./images/812131211873878017_3.jpg)

FIG. 3. Geometries of the confined $(H_2)_N$ clusters up to $N=10$ as optimized within a SOD cage using the FF due to Buck et al.[Refs. 4 and 5] (left of the vertical bars: each $H_2$ molecule repre sented by a single sphere) and with DFT employing the PW91functional (right of the vertical bars: each $H_2$ molecule representedby the two connected $H$ atoms). As an example of how the $(H_2)_N$  clusters look like as confined within a SOD cage, the figure in the right lower corner shows the Buck et al. FF optimized cluster of N=8 within the skeleton of a SOD cage.

![](./images/812131211873878017_4.jpg)

FIG. 4. The energies resulting from the interactions between the $H_2$ molecules in the optimized confined $H_2$ clusters within a SOD cage as calculated by periodic DFT (BLYP, PW91, PBE, LDA) and FF [Buck, Refs. 4 and 5] calculations.

![](./images/812131211873878017_5.jpg)

FIG. 5. The energies resulting from the interactions between the $\text{H}_2$ clusters and the SOD cage as calculated by periodic DFT (BLYP, PW91, PBE, LDA) and FF [Buck et al. (Ref. 4)] calculations.

of the $\text{H}_2$-$\text{H}_2$ interaction in each case is responsible. For the FF calculations and the DFT calculations employing the BLYP, PBE, and PW91 functionals, the cluster-SOD energy is lower than the total system energy (indicating a repulsive $\text{H}_2$-$\text{H}_2$ interaction) whereas for the LDA DFT calculations the cluster-SOD energies become relatively higher (indicating an attractive $\text{H}_2$-$\text{H}_2$ interaction). This pattern of behavior is also easily seen in Fig. 4, where the $\text{H}_2$-$\text{H}_2$ interaction energies show the FF and the PW91, PBE, BLYP functionals always with positive values and the LDA results always with negative values. It is further interesting to note that the $\text{H}_2$-$\text{H}_2$ energies given by the FFs match very well with the DFT results obtained with the PW91 and PBE functionals indicating a consistent representation of the $\text{H}_2$-$\text{H}_2$ interaction. Noting the absolute values of the cluster-SOD energies also tells us that in the case of the PW91 and PBE functionals it is only the very weak interaction of $\text{H}_2$ with the framework for low loadings that gives the corresponding negative total system energy (the $\text{H}_2$-$\text{H}_2$ interaction being almost purely repulsive). For the LDA and FF results, however, the cluster-SOD energies for all loadings are very close together and always negative indicating a consistent attractive interaction between the $\text{H}_2$ cluster and the confining framework. Considering the similarities and differences between the various DFT results it is instructive to examine the known limitations and strengths of the DFT approach for other systems relevant to that studied herein.

The application of DFT to systems exhibiting weak interactions remains an issue of concern without a systematic general solution. The PW91, PBE, and BLYP functionals all employ the generalized gradient approximation (GGA). Such have been shown to be able to capture at least some of the attractive character of nonbonding interactions in studies of weakly interacting dimer species, $^{43,44}$ and rare gases interacting with metal surfaces, $^{45}$ but have also been criticized for giving purely repulsive interactions in many other weakly bonded systems. $^{46}$ LDA functionals, although generally known to exhibit overbinding in many chemical systems, have often been shown to outperform GGA functionals for describing weakly interacting systems (e.g., $\text{H}_2$-carbon systems $^{47,48}$ and rare gas/metal surface studies $^{49,50}$). In fact although both LDA and GGA functionals can give a surprisingly reasonable account of weak attractive interactions, this capacity is only provided through favorable error correction with the attraction coming from the exchange energy contribution to the respective functional. $^{51}$ In the BLYP functional, perhaps due to a better description of the exchange energy, $^{51}$ even this effect is diminished thus often giving purely repulsive interactions as observed herein. $^{49}$

![](./images/812131211873878017_6.jpg)

FIG. 6. Nearest neighbor distances of the $\text{H}_2$ molecules in the optimized $(\text{H}_2)_N$ clusters confined within a SOD cage as calculated by periodic DFT (BLYP, PW91, PBE, LDA) and FF [Buck et al. (Ref. 4)] calculations. The horizontal lines show the nearest neighbor distance in crystalline solid hydrogen at 300 K at the indicated pressure conditions (Refs. 52 and 53).

Our calculations appear to verify the known erroneous repulsive description of weakly bonded systems for GGA based functionals with respect to the $\text{H}_2$-SOD interaction for which the empirically derived FF and LDA both predict a similarly attractive interaction strength (see Fig. 5). Although the true nature of the weak interaction of confined $\text{H}_2$ clusters with the siliceous framework is difficult to accurately assess (other than perhaps by currently prohibitively expensive, highly correlated calculations) it is strongly persuasive that both an experimentally parameterized interaction potential (Ref. 33) and a functional (LDA) recognized to very often provide good representation of weak interactions (Refs. 47–50) agree so well.

For the $\text{H}_2$-$\text{H}_2$ interaction energies the rigorously parameterized $\text{H}_2$-$\text{H}_2$ FFs (Refs. 1 and 4) are very well matched by the results of the PBE and PW91 functionals (see Fig. 4) whereas the LDA results are in very poor agreement, respectively. The quality of the representation of the $\text{H}_2$-$\text{H}_2$ interaction for each method can also be assessed by comparison to the known properties of dense bulk hydrogen. In this extreme of high densities and pressures, where repulsive Pauli interactions generally dominate, both LDA and GGA functionals have been successfully employed to calculate the properties of solid parahydrogen. $^{22,23}$ The nearest neighbor distances for all optimized confined $\text{H}_2$ clusters are calculated and shown in Fig. 6. Additionally the distances in crystalline solid $\text{H}_2$ at different pressures are indicated, $^{52,53}$ showing that the higher loading corresponds to extremely high

pressures. Perhaps surprisingly all calculation methods give a rather consistent description of the variation in average nearest neighbor $\text{H}_2$-$\text{H}_2$ distances with increasing $\text{H}_2$ loading. Although for nearly all methods a similarly repulsive $\text{H}_2$-$\text{H}_2$ interaction dominates in this regime, for the LDA calculations the $\text{H}_2$-$\text{H}_2$ interaction is still attractive. The prediction of attractive $\text{H}_2$-$\text{H}_2$ interactions at such extreme conditions appears to be a result of the unphysical overbinding that LDA is known to exhibit. Considering the probable erroneous prediction of the attractive confined $\text{H}_2$-$\text{H}_2$ interaction by LDA and the excellent correspondence between the sophisticated Buck *et al.* FF and the GGA functionals, it is convincing that the latter two methods give an accurate account of the $\text{H}_2$-$\text{H}_2$ interaction within confined $(\text{H}_2)_N$ clusters.

Our analysis thus indicates that, although different functionals can adequately describe various interactions in confined $\text{H}_2$ systems, it is likely that none of those tested can accurately describe all of the important interactions in such systems. In the absence of more generally appropriate functionals for confined $\text{H}_2$ systems we thus advocate the use of accurately parameterized interatomic potentials as employed herein and further justified in other studies. $^{2-5,14}$ Considering the large number of reported DFT studies on the storage of $\text{H}_2$ within various confining nanostructures and materials using one of the functionals tested herein, $^{15-21}$ it is important that subsequent predictions of $\text{H}_2$ storage capacity and energetics based upon such calculations are viewed critically. To show how the different methods can lead to disparate estimates of $\text{H}_2$ storage capacity we show in Table II the $\text{H}_2$ storage expressed as a weight percentage corresponding to the number of hydrogen molecules per SOD cage as calculated with

$$
\text{Loading} = \frac{N_{\text{H}_2}M_{\text{H}_2}}{6M_{\text{Si}} + 12M_{\text{O}} + N_{\text{H}_2}M_{\text{H}_2}}100 \ \%. \tag{4}
$$

$N_{\text{H}_2}$ is the number of $\text{H}_2$ atoms in the SOD cage, $M_{\text{H}_2}$ is the molar mass of a hydrogen molecule [kg/mol], $M_{\text{Si}}$ is the molar mass of a silicon atom [kg/mol], and $M_{\text{O}}$ is the molar mass of an oxygen atom [kg/mol]. The skeleton of a single SOD cage consists of 24 Si atoms and 36 O atoms. The Si atoms are all shared by four cages and the O atoms are all shared by three cages, therefore the weight of a single cage is based upon $\text{Si}_6\text{O}_{12}$.

As all calculations are effectively performed at zero Kelvin and no zero point energy correction is applied these results should not be thought to give a realistic estimate for the maximum practically achievable $\text{H}_2$ storage capacity in

<table>
<caption>TABLE II. Loading in no. $\text{H}_2$ and wt %.</caption>
<thead>
<tr>
<th>No. $\text{H}_2$ per cage (-)</th>
<th>Loading (wt %)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.56</td>
</tr>
<tr>
<td>2</td>
<td>1.11</td>
</tr>
<tr>
<td>3</td>
<td>1.65</td>
</tr>
<tr>
<td>4</td>
<td>2.19</td>
</tr>
<tr>
<td>5</td>
<td>2.72</td>
</tr>
<tr>
<td>6</td>
<td>3.25</td>
</tr>
<tr>
<td>7</td>
<td>3.77</td>
</tr>
<tr>
<td>8</td>
<td>4.28</td>
</tr>
<tr>
<td>9</td>
<td>4.79</td>
</tr>
<tr>
<td>10</td>
<td>5.30</td>
</tr>
<tr>
<td>11</td>
<td>5.79</td>
</tr>
<tr>
<td>12</td>
<td>6.29</td>
</tr>
<tr>
<td>13</td>
<td>6.78</td>
</tr>
<tr>
<td>14</td>
<td>7.26</td>
</tr>
</tbody>
</table>

SOD. Instead the number of $\text{H}_2$ molecules for which the total system energy is equal to that of the empty SOD framework is taken as a thermodynamic upper limit for storage. $^{32}$ Using this basis for comparison, the FF methods give an upper limit of nine hydrogen molecules (4.3 wt %), the functionals PW91 and PBE give a limit of two $\text{H}_2$ molecules (1.1 wt %), LDA gives a lower limit of 13 $\text{H}_2$'s (6.8 wt %), and the BLYP functional gives zero storage.

## IV. CONCLUSIONS

By a detailed comparative study we show that commonly used density functionals (LDA, PW91, PBE, BLYP) are not generally applicable to $\text{H}_2$ in confined systems. By partitioning the energy of our system into contributions due to $\text{H}_2$-$\text{H}_2$ interactions and $\text{H}_2$-framework interactions the performance of each functional and two accurately parameterized interatomic potentials could be assessed showing explicitly the deficiencies and advantages of each method. In the absence of more generally appropriate functionals for confined $\text{H}_2$ systems we advocate the use of accurately parameterized interatomic potentials for such studies. In light of our results we advise that predictions of technologically relevant data (e.g., $\text{H}_2$ storage capacities) based on the use of DFT calculations using one of the functionals tested herein be critically assessed.

## ACKNOWLEDGMENT

We thank Alexey Sokol for useful discussions.

*Corresponding author. Electronic address: s.bromley@qf.ub.es

$^{1}$T. A. Bruce, Phys. Rev. B 5, 4170 (1972).

$^{2}$M. Zoppi and M. Neumann, Phys. Rev. B 43, 10242 (1991).

$^{3}$M. Zoppi and M. Neumann, Physica B 180&181 (Pt. B), 825 (1992).

$^{4}$U. Buck, F. Huisken, A. Kohlhase, D. Otten, and J. Schaefer, J. Chem. Phys. 78, 4439 (1983).

$^{5}$M. J. Norman, R. O. Watts, and U. Buck, J. Chem. Phys. 81, 3500 (1984).

$^{6}$G. A. Gallup, Mol. Phys. 33, 943 (1977).

$^{7}$F. H. Ree and C. F. Bender, J. Chem. Phys. 71, 5362 (1977).

$^{8}$J. Schaefer and W. Meyer, J. Chem. Phys. 70, 344 (1979).

$^{9}$P. G. Burton and U. E. Senf, J. Chem. Phys. 76, 6073 (1982); 97, 526 (1983).

$^{10}$I. F. Silvera and V. V. Goldman, J. Chem. Phys. 69, 4209 (1978).

$^{11}$M. A. McMahon and K. B. Whaley, Chem. Phys. 182, 119 (1994).

$^{12}$M. A. McMahon, R. N. Barnett, and K. B. Whaley, J. Chem. Phys. 99, 8816 (1993).

$^{13}$A. W. C. van den Berg, S. T. Bromley, E. Flikkema, J. Wojdel, Th. Maschmeyer, and J. C. Jansen, J. Chem. Phys. 120, 10285 (2004).

$^{14}$A. W. C. van den Berg, S. T. Bromley, N. Ramsahye, and Th. Maschmeyer, J. Phys. Chem. B 108, 5088 (2004).

$^{15}$Y. Xia, M. Zhao, Y. Ma, X. Liu, M. Ying, and L. Mei, Phys. Rev. B 67, 115117 (2003).

$^{16}$Q. Sun, Q. Wang, and P. Jena, Nano Lett. 5, 1273 (2005).

$^{17}$J. Soullard, R. Santamaria, and S. A. Cruz, Chem. Phys. Lett. 391, 187 (2004).

$^{18}$S. M. Lee and Y. H. Lee, Appl. Phys. Lett. 76, 2877 (2000).

$^{19}$S. M. Lee, K. H. An, Y. H. Lee, G. Seifert, and T. Frauenheim, J. Am. Chem. Soc. 123, 5059 (2001).

$^{20}$Y. Xia, M. Zhao, F. Li, B. Huang, Z. Tan, X. Liu, Y. Ji, and L. Mei, J. Phys. Chem. B 108, 4711 (2004).

$^{21}$S. P. Chan, M. Ji, X. G. Gong, and Z. F. Liu, Phys. Rev. B 69, 092101 (2004).

$^{22}$H. Nagara, K. Nagao, and T. Takezawa, J. Phys.: Condens. Matter 10, 11191 (1998).

$^{23}$S. Scandolo, Proc. Natl. Acad. Sci. U.S.A. 100, 3051 (2003).

$^{24}$W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flan- nery, *Numerical Recipes* (Cambridge University Press, Cam- bridge, England, 1992).

$^{25}$M. J. Sanders, M. Leslie, and C. R. A. Catlow, J. Chem. Soc., Chem. Commun. 19, 1271 (1984).

$^{26}$N. J. Henson, A. K. Cheetham, and J. Gale, Chem. Mater. 6, 1647 (1994).

$^{27}$R. Grau-Crespo, E. Acuay, and A. R. Ruiz-Salvador, Chem. Commun. (Cambridge) 21, 2544 (2002).

$^{28}$M. A. Camblor and M.-J. Diaz-Cabanas, Chem. Mater. 11, 2878 (1999).

$^{29}$G. D. Price, I. G. Wood, and D. E. Akporiaye, in *Modelling of Structure and Reactivity in Zeolites*, edited by C. R. A. Catlow (Academic Press, San Diego, 1992), p. 38.

$^{30}$D. W. Lewis and G. Sastre, Chem. Commun. (Cambridge) 4, 349 (1999).

$^{31}$R. Astala, S. M. Auerbach, and P. A. Monson, J. Phys. Chem. B 108, 9208 (2004).

$^{32}$A. W. C. van den Berg, S. T. Bromley, and J. C. Jansen, Mi- croporous Mesoporous Mater. 78, 63 (2005).

$^{33}$K. Watanabe, N. Austin, and M. R. Stapleton, Mol. Simul. 15, 197 (1995).

$^{34}$J. D. Gale, J. Chem. Soc., Faraday Trans. 93, 629 (1997).

$^{35}$D. I. Kopelevich and H.-C. Chang, J. Chem. Phys. 115, 9519 (2001).

$^{36}$CPMD, Copyright IBM Corp. 1990–2004, Copyright MPI für Festkörperforschung Stuttgart 1997–2001.

$^{37}$J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B 13, 5188 (1976).

$^{38}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

$^{39}$S. Goedecker, M. Teter, and J. Hutter, Phys. Rev. B 54, 1703 (1996).

$^{40}$A. D. Becke, Phys. Rev. A 38, 3098 (1988).

$^{41}$D. Vanderbilt, Phys. Rev. B 41, R7892 (1990).

$^{42}$http://www.physics.rutgers.edu/~dhv/uspp/

$^{43}$X. Xu and W. A. Goddard III, Proc. Natl. Acad. Sci. U.S.A. 101, 2673 (2004).

$^{44}$S. Tsuzuki and H. P. Lüthi, J. Chem. Phys. 114, 3949 (2001).

$^{45}$M. Petersen, S. Wilke, P. Ruggerone, B. Kohler, and M. Scheffler, Phys. Rev. Lett. 76, 995 (1996).

$^{46}$M. B. Nardelli, Solid State Commun. 97, 215 (1996).

$^{47}$J. S. Arellano, L. M. Molina, A. Rubio, M. J. Lopez, and J. A. Alonso, J. Chem. Phys. 117, 2281 (2002).

$^{48}$Y. Okamoto and Y. Miyamoto, J. Phys. Chem. B 105, 3470 (2001).

$^{49}$M. I. Trioni, S. Marcotulio, G. Santoro, V. Bortolani, G. Palumbo, and G. P. Brivio, Phys. Rev. B 58, 11043 (1998).

$^{50}$A. E. Betancourt and D. M. Bird, J. Phys.: Condens. Matter 12, 7077 (2000).

$^{51}$X. Wu, M. C. Vargas, S. Nayak, V. Lotrich, and G. Scoles, J. Chem. Phys. 115, 8748 (2001).

$^{52}$H. K. Mao, A. P. Jephcoat, R. J. Hemley, L. W. Finger, C. S. Zha, R. M. Hazen, and D. E. Cox, Science 239, 1131 (1988).

$^{53}$R. M. Hazen, H. K. Mao, L. W. Finger, and R. J. Hemley, Phys. Rev. B 36, 3944 (1987).