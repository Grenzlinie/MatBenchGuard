![](./images/813171135356076033_1.jpg)

On factors controlling activity of submonolayer bimetallic catalysts: Nitrogen desorption

Wei Guo and Dionisios G. Vlachos

Citation: *The Journal of Chemical Physics* **140**, 014703 (2014); doi: 10.1063/1.4855235
View online: http://dx.doi.org/10.1063/1.4855235
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/140/1?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Beneficial compressive strain for oxygen reduction reaction on Pt (111) surface
J. Chem. Phys. **141**, 124713 (2014); 10.1063/1.4896604

Mechanism of ammonia decomposition and oxidation on Ir(110): A first-principles study
J. Chem. Phys. **138**, 144703 (2013); 10.1063/1.4798970

Thermodynamics and kinetics of oxygen-induced segregation of 3 d metals in Pt – 3 d – Pt ( 111 ) and Pt – 3 d – Pt ( 100 ) bimetallic structures
J. Chem. Phys. **128**, 164703 (2008); 10.1063/1.2900962

C–H bond activation over metal oxides: A new insight into the dissociation kinetics from density functional theory
J. Chem. Phys. **128**, 051101 (2008); 10.1063/1.2832324

Water desorption from an oxygen covered Pt(111) surface: Multichannel desorption
J. Chem. Phys. **124**, 204712 (2006); 10.1063/1.2200347

![](./images/813171135356076033_2.jpg)

# On factors controlling activity of submonolayer bimetallic catalysts: Nitrogen desorption

Wei Guo and Dionisios G. Vlachos⁽ᵃ⁾

Center for Catalytic Science and Technology, Catalysis Center for Energy Innovation, Department of Chemical and Biomolecular Engineering, University of Delaware, Newark, Delaware 19716, USA

(Received 21 October 2013; accepted 10 December 2013; published online 2 January 2014)

We model $\text{N}_2$ desorption on submonolayer bimetallic surfaces consisting of Co clusters on Pt(111) via first-principles density functional theory-based kinetic Monte Carlo simulations. We find that submonolayer structures are essential to rationalize the high activity of these bimetallics in ammonia decomposition. We show that the $\text{N}_2$ desorption temperature on Co/Pt(111) is about 100 K higher than that on Ni/Pt(111), despite Co/Pt(111) binding N weaker at low N coverages. Co/Pt(111) has substantially different lateral interactions than single metals and Ni/Pt. The lateral interactions are rationalized with the d-band center theory. The activity of bimetallic catalysts is the result of heterogeneity of binding energies and reaction barriers among sites, and the most active site can differ on various bimetallics. Our results are in excellent agreement with experimental data and demonstrate for the first time that the zero-coverage descriptor, used until now, for catalyst activity is inadequate due not only to lacking lateral interactions but importantly to presence of multiple sites and a complex interplay of thermodynamics (binding energies, occupation) and kinetics (association barriers) on those sites. © 2014 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4855235]

## I. INTRODUCTION

Core-shell bimetallic catalysts exhibit properties that are not an interpolation of those of the parent metals.¹ Such emergent behavior provides an opportunity to discover materials with better performance, stability, and/or lower cost. Coreshell structures are often modeled as monolayer bimetallic surfaces. Three ideal configurations may exist in such a model: a subsurface configuration Y-X-Y, where the first layer is the host metal Y, and the admetal X appears only in the second layer; a segregated surface structure X-Y-Y, and an intermixed configuration XY-Y-Y.² Recent *in situ* extended X-ray absorption fine structure (EXAFS) data and molecular dynamics (MD) simulations show that the admetal X may form clusters on the host metal Y (denoted as X/Y) during reaction.³,⁴ Scanning tunneling microscopy (STM) and density functional theory (DFT) studies of bimetallic catalysts have revealed that the surface morphology, i.e., microstructure, defects, or isolated metal atoms may substantially change the binding energy and transition barriers of catalytic reactions on a bimetallic surface.⁵,⁶

DFT aided microkinetic modeling (MKM) and kinetic Monte Carlo (KMC) simulations provide a computational platform towards optimal catalyst selection, whereby coverage effects have been shown to be important.⁷⁻¹³ The results appear in a volcano plot that relates the reaction rate with certain descriptors, such as binding energies of important surface species.¹⁴ These models can greatly reduce the number of candidate materials for experimentation.¹⁵ While these methods have been successful in providing catalyst leads, activity maps that predict catalysts still rely on uniform site models based on the zero coverage limit binding energy, and as we make the case here, catalyst activity does not always correlate well with binding energies. For instance, in ammonia decomposition, Hansgen *et al.* found that Co/Pt and Ni/Pt bind N with nearly the same strength at low coverage, but temperature-programmed desorption (TPD) data indicate that the $\text{N}_2$ desorption temperature is more than 100 K higher on Co/Pt (Figure 1). Redhead's equation¹⁶ describes single metals (Co) well but fails to describe bimetallics. Obviously, there is no apparent trend between the DFT calculated N binding energy and the $\text{N}_2$ desorption temperature found in TPD experiments. As we show below, the reason for this is not just lateral interactions (or so called coverage effects). Microstructure can be a dominant factor when multiple sites are involved in a reaction.

We have recently introduced a multiscale framework that combines DFT and a graph-theoretical KMC simulation to elucidate the effect of microstructure on nitrogen desorption on Ni/Pt.¹⁷ We have found that Ni/Pt plays a bifunctional role for ammonia decomposition where the Ni terraces facilitate dehydrogenation and interfacial sites at Ni steps promote $\text{N}_2$ desorption. As a result, the spatial distribution of active sites controls the catalytic activity.

In this paper, we employ the previously developed DFT/KMC framework¹⁷ to perform TPD simulations of $\text{N}_2$ desorption on Co/Pt bimetallic surface in order to understand the results of Figure 1. First, we compute coveragedependent N binding energies on Co/Pt surfaces. Then the N-N association barriers are calculated. Next, we incorporate the energetics into the KMC code to carry out TPD simulations and compare to the experimental data. We show that aside from microstructure, proper description of lateral interactions is important for predicting catalyst activity quantitatively.

⁽ᵃ⁾Author to whom correspondence should be addressed. Electronic mail: vlachos@udel.edu

![](./images/813171135356076033_3.jpg)

FIG. 1. Temperature programmed desorption (TPD) peak temperature of $N_2$ desorption on Ni/Pt, Co/Pt, Ni, Co, and Pt catalysts as a function of N binding energy. Experimental data are taken from Ref. 11 and theory from the Redhead equation. $^{16}$ No data exist for Pt and Ni.

## II. COMPUTATIONAL METHODS AND MODELS

We performed periodic spin-polarized DFT calculations using the Vienna $ab$ $initio$ simulation package (VASP, version 5.2.12). $^{18,19}$ The Revised Perdew-Burke-Ernzerhof parameterized generalized gradient approximation (GGA-RPBE) functional has been used to describe the exchange-correlation energies. $^{20}$ The valence electron-core interactions were treated by the projector augmented wave (PAW) pseudopotentials. $^{21,22}$ The Kohn-Sham one-electron valence states were expanded in plane wave basis sets with a cutoff of 350 eV. A higher cutoff, 396 eV, has been tested, and we found that the $N_2$ atomization energy and N binding energy on Pt(111) change less than 25 meV. The surface Brillouin zone was sampled using a Monkhorst-Pack grid. $^{23}$ The Fermi partial occupation of the Kohn-Sham state was calculated with a smearing parameter of $k_bT = 0.1$ eV, and all the potential energies have been extrapolated to 0 K. An inter-slab vacuum layer of $14$ Å was used. The convergence criterion for the self-consistent electronic loop and ionic loop were set to $10^{-4}$ eV and $0.1$ eV/Å, respectively. The latter was checked with $0.05$ eV/Å and the total energy change was less than 20 meV. The (111) surface was modeled using p(2 $\times$ 2) or p(4 $\times$ 4) unit cells. All slabs consist of at least four metal layers with the bottom two fixed to their bulk positions. A 4 $\times$ 4 $\times$ 1 k-mesh was used for the p(2 $\times$ 2) surface unit cells and a 2 $\times$ 2 $\times$ 1 k-mesh for the p(4 $\times$ 4) unit cells, following convergence tests of nitrogen binding energies for similar systems. $^{10}$ The Pt lattice constant in our calculation is 3.994 Å, i.e., 2% larger than the experimental value. $^{24}$ The $N_2$ atomization energy is calculated to be 229.4 kcal/mol, in good agreement with the experimental value of 228.5 kcal/mol. $^{25}$ Transition state calculations of association reactions were performed using the constrained minimization technique implemented in Atomic Simulation Environment (ASE). $^{26}$ A drag reaction coordinate was fixed and all the other degrees of freedom were relaxed. This method has been shown to be accurate for dissociation reactions of diatomic molecules, where the reaction coordinate is easy to define, i.e., the bond length. $^{27}$

The DFT calculated energetics were employed as inputs to a recently developed graph-theoretical KMC simulation framework. $^{28}$ Zero-point energy (ZPE) corrections have been applied to the energetics. $N_2$ in the gas-phase was used as the reference state. The pre-exponentials were computed as ratios of partition functions of the transition state to the reactant state. Lateral interactions were included with a lattice-gas model with 1st nearest neighbor N-N pairwise $[(N-N)_{1st}]$ additive interactions, following recent work. $^{28,29}$

KMC simulations were performed on a c(14 $\times$ 24) (centered rectangular lattice) substrate, which had an area of 69.08 $\times$ 68.37 Å$^2$. Periodic boundary conditions were used. The surface had 672 top layer Pt atoms. We considered a total of 2016 sites on Co/Pt surfaces. These sites entail 19 types of sites: 6, 7, 4, and 2 types of fcc hollow, hcp hollow, top, and step sites, respectively. The sites close to the step or corner atoms were modeled as pairs of interfacial sites, each comprised of a step site and a Pt terrace site. To speed up the calculation, we raised the lowest diffusion barriers while keeping these processes well equilibrated and at least 2 orders faster than the slower association processes. The initial nitrogen coverages were 0.2 or 0.3; the heating rate was 3 K/s and at least 100 s were simulated in all the KMC runs. Each TPD result was obtained by averaging 20 KMC calculations employing different initial seeds of the random number generator. The KMC input parameters are listed in the supplementary material. $^{38}$

We have chosen a hexagonal cluster of the guest metal (Co or Ni) on Pt for $N_2$ desorption consisting of 110 and 100 steps. The Ni or Co coverage on Pt is $\sim$0.1. The adlayer cluster consists of 79 Co atoms, and 14 (110) and (100) step sites. The fraction of the edge atoms of the cluster is fixed to 0.35. The stability, i.e., admetal diffusion into bulk vs. Pt segregation to surface, is discussed in our previous work. $^{17}$ Since N binds Co stronger than Ni on Pt at high N coverages (see below), Pt segregation will be more difficult for Co/Pt surfaces, i.e., such structure is a reasonable representation of the catalytic activity.

To model the N binding, diffusion, and association on Co clusters on Pt(111), we have considered three Co/Pt surfaces. The structures and possible N binding sites are shown in Figure 2. Due to the high computational cost of DFT calculations for large systems, the N energetics at the edge of large Co clusters is approximated with the energetics of two small clusters consisting of 6 adatoms of Co on Pt [6adCo(110) and 6adCo(100)]. For N residing in the center of large Co clusters, the energetics is modeled as N adsorption on a full monolayer, Co-Pt-Pt. This approach is reasonable because Co atoms at the center of large admetal clusters are constrained to the substrate lattice and strain release happens mostly at the cluster edge, which is similar to the strain of small admetal clusters as previous calculations have shown. $^{5}$ We have used the N diffusion barrier on Ni/Pt for the Co/Pt surface due to the fact that the $N_2$ desorption temperature is not sensitive to N diffusion barriers as long as diffusion is fast and the overlayer clusters are small.

![](./images/813171135356076033_4.jpg)

FIG. 2. Top and side views of three Co/Pt surfaces considered in DFT calcu-
lations. (a) and (b) six Co adatoms on Pt(111). 6adCo(110) and 6adCo(100)
surfaces consist of six (110) and (100) step sites, respectively. (c) 1ML of Co
on Pt(111), denoted as Co-Pt-Pt. The black circles are for hollow sites on Co
and the red ones are for hollow sites on Pt. The white triangle and rectangle
are for (110) and (100) step sites, respectively. Here “f,” “h,” and “s” stand
for fcc hollow, hcp hollow, and step sites, respectively. Yellow balls are Co
atoms and blue balls are Pt atoms. Interfacial sites are comprised of s1-h5
and s2-h6 sites on 6adCo(110) and 6adCo(100), respectively.

## III. N BINDING ENERGIES

In our previous studies, we have calculated the N binding,
diffusion, and association on Ni/Pt surfaces. $^{5,17}$ At the low
coverage limit ($\theta_{\mathrm{N}}=1/16$), there is a linear correlation ($\mathrm{R}^{2}=$
0.990) between the N binding energy on Co/Pt and Ni/Pt sur-
faces (Figure 3(a)), and Co/Pt and Ni/Pt surfaces show simi-
lar binding strength. For most of the binding configurations,
Co/Pt binds N slightly weaker than Ni/Pt. On the other hand,
Co-Pt-Pt binds O and H slightly stronger than Ni-Pt-Pt. $^{2,10,30}$
The lateral interactions of N on Co/Pt and Ni/Pt are quite dif-
ferent as discussed next.

The coverage dependent N binding energies on close-
packed pure Pt, Ni, Co and bimetallic surfaces Ni-Pt-Pt, Co-
Pt-Pt are shown in Figure 3(b). The ground state lattices for
bulk Pt, Ni and Co are fcc, fcc, and hcp, respectively. The
most favorable N adsorption site on Pt and Ni is fcc hollow
and on Co is hcp hollow. On single metals, the lateral inter-
action is rather weak below $\theta_{\mathrm{N}}=\frac{1}{4}$, but the binding energy
decreases with a high slope of 1.7–2.0 eV/ML at higher cover-
ages. Ni has the largest slope among them. For bimetallic sur-
faces, Ni-Pt-Pt shows a similar trend with single metals and
the repulsive (N-N)$_{1\text{st}}$ pair interaction energy is 0.36 eV. In
contrast, N adsorption on Co-Pt-Pt is different from the trend
mentioned above. The interaction is attractive when $\theta_{\mathrm{N}}$ is be-
low 2/16. For instance, the (N-N)$_{1\text{st}}$ pair is 0.49 and 0.11 eV
more stable than two infinitely separated N atoms on fcc and
hcp hollow sites of Co-Pt-Pt, respectively. When $\theta_{\mathrm{N}}$ is greater
than 2/16, the binding strength decreases with a smaller slope
of $\sim$0.4 eV/ML. As a result, Co-Pt-Pt binds N stronger than
Ni-Pt-Pt for $\theta_{\mathrm{N}}>\sim$0.4. This difference in lateral interactions
is the first distinguishing factor between Ni and Co adlayers
on Pt. Considering the structure similarity in N binding on
these surfaces (3-fold hollow site), such entirely different lat-
eral interaction may mainly be due to electronic effect. This
can be inferred from the fact that, if we fix the metal substrates
and only relax the N atoms, the (N-N)$_{1\text{st}}$ pair interaction is
0.12 eV attractive and 0.31 eV repulsive on fcc hollow sites
of Co-Pt-Pt and Ni-Pt-Pt, respectively.

Electronic structure calculations provide insights into the
coverage effect. According to the d-band model, $^{31}$ a higher d-
band center (the first moment of the density of states (DOS)
with reference to the Fermi level) indicates a stronger bind-
ing of the adsorbate. Upon adsorption, the metal d-band cen-
ter shifts due to the hybridization with the bonding and anti-
bonding adsorbate states (see Fig. 2S in the supplementary
material). $^{38}$ Figure 4 shows that the binding strength is well
described by the d-band center. Upon a single N adsorption,
the d-band center of Ni-Pt-Pt shifts towards a lower energy,
indicating that if a second N adsorbs on 1N/Ni-Pt-Pt to form a
(N-N)$_{1\text{st}}$ pair, the pair interaction energy will be repulsive. Co-
Pt-Pt shows the opposite trend and the d-band center of Co-
Pt-Pt shifts towards a higher value, rationalizing the attrac-
tive (N-N)$_{1\text{st}}$ pair interaction. In terms of modification of the
electronic property of bimetallic surfaces, the heterometal-
lic bonding interaction is termed as ligand effect. $^{32}$ Mean-
while, the metal d-band is also affected by the metal-adsorbate

![](./images/813171135356076033_5.jpg)

FIG. 3. DFT calculated N binding energies at different N coverage, $\theta_{\mathrm{N}}$. (a) Linear correlation between the binding energies of N on Co/Pt and Ni/Pt surfaces at
$\theta_{\mathrm{N}}=1/16$ on various adsorption sites shown in Figure 2. (b) Coverage dependent average binding energies of N on Pt, Co, Ni, Ni-Pt-Pt, and Co-Pt-Pt. Circles
and crosses are for adsorption on fcc and hcp hollow sites, respectively. For N on Co-Pt-Pt, the most stable adsorption configuration for $\theta_{\mathrm{N}}=2/16$ (indicated by
the green arrow) is a pair of 1st-nearest hollow sites, for which the interaction is attractive. Configurations are shown in Fig. 1S of the supplementary material. $^{38}$

![](./images/813171135356076033_6.jpg)

FIG. 4. Linear correlation between the d-band center of various substrates and the N binding energies on the substrates. 1N/Ni-Pt-Pt and 1N/Co-Pt-Pt denote a N atom (indicated as a red sphere) residing in an fcc site of Ni-Pt-Pt and Co-Pt-Pt, respectively (the structure is shown as inset, where the white circle represents the 1st-nearest-neighbor fcc site of the N atom). When it is occupied by a second N and a N-N pair forms, the $\Delta E(\text{N})$ is the average binding energy. The d-band center is calculated from the projected density of states (PDOS) of the metal atoms indexed by 1, 2, 3, 4, and 5. The red arrows indicate the shifts of the d-band center upon adsorption of a N atom on Ni-Pt-Pt and Co-Pt-Pt substrates.

bonding interactions. They contribute to the d-band center shift separately for most cases. $^{33}$ Another interesting effect is the adsorbate-induced surface strain. In a recent computational work of O adsorption on Pt(111), lateral interactions were shown to arise from a combination of the adsorbate-induced surface strain and electronic repulsion. The former is responsible for longer-ranged repulsion but can be attractive at short distances. $^{34}$ Although those effects can be captured with d-band center calculations, the origin of the d-band center shift upon adsorption could possibly differ, depending on how strong the strain is, as compared to the adsorbate hybridization with metal supports. We estimated the Ni-Pt, Co-Pt, Ni-Ni, and Co-Co distances before and after N adsorption on Ni-Pt-Pt and Co-Pt-Pt surfaces. In N adsorption, due to strong N-metal bonds, N atoms are pulling Ni or Co away from Pt and attracting the nearest Ni or Co atoms closer. As a result, the Ni-Pt and Co-Pt bond lengths increase, and the local Ni-Ni and Co-Co bond lengths decrease (see Fig. 3S in the supplementary material). $^{38}$ Single N adsorption on Ni-Pt-Pt induces the largest strain of $-4.3\%$. Different from it, a (N-N)$_{1\text{st}}$ pair on Co-Pt-Pt causes the largest strain of $-1.5\%$. We believe that for a (N-N)$_{1\text{st}}$ pair on Co-Pt-Pt, the net attractive interaction is a result of strain-related attraction overcoming the intrinsic electronic repulsion.

Due to the nonlinear nature of the coverage dependent N binding energy on Co-Pt-Pt (Figure 3(b)), an attractive interaction (0.49 and 0.11 eV/pair on fcc and hcp hollow sites of Co-Pt-Pt, respectively) is suitable to describe the low local $\theta_{\text{N}}$ regime and a weak repulsive N-N lateral interaction (0.01 and 0.07 eV/pair on fcc and hcp hollow sites of Co-Pt-Pt, respectively) is suitable at high local $\theta_{\text{N}}$ (see Fig. 4S in the supplementary material). $^{38}$ Given that Co-Pt-Pt binds N at least 0.5 eV stronger than the Pt terrace, the local $\theta_{\text{N}}$ on the Pt terrace is low and the local $\theta_{\text{N}}$ on the Co terrace is high. As a result, even at low total $\theta_{\text{N}}$ on the crystal, the local $\theta_{\text{N}}$ on a Co terrace is in the high $\theta_{\text{N}}$ regime during most of the TPD simulation. Thus, we employ the high local $\theta_{\text{N}}$ lateral interaction model in the KMC simulations on the islands of Co on Pt.

![](./images/813171135356076033_7.jpg)

FIG. 5. Barriers (top, black bars) and transition-state structures (bottom) of N-N association on Co/Pt. The corresponding barriers on Ni/Pt are also shown as red bars. Red spheres represent N atoms. N-N bond lengths at transition states are in white text. There are potentially two interfacial paths, one at the (110) step of 6adCo(110) and one at the (100) step of 6adCo(100) surface (cf. Figure 2), and two terrace edge paths [only one of them is shown as representative on 6adCo(110)].

## IV. N-N ASSOCIATION BARRIERS

Next we calculate the barriers of N-N association on Co/Pt and compare them with those of Ni/Pt. The results and structures are shown in Figure 5. Although the transition state structures and N-N bond lengths on Co/Pt are close to those on Ni/Pt, the correlation between the barrier and the reaction energy, i.e., the so called Brønsted-Evans-Polanyi (BEP) relation, $^{35}$ is not as good. This is actually a result of the N-N attractive lateral interaction on Co/Pt, where the initial state of the N-N association is more stable on Co/Pt than on Ni/Pt. Thus, the similarity of binding energies of N on Co/Pt and Ni/Pt in the low coverage regime (Figure 3(a)) does not result in similar association barriers in Figure 5. Specifically, the N-N association barriers on Co/Pt are 0.95 and 0.71 eV higher than those of Ni/Pt at the terrace edges and (100) steps. On the (110) step, the N-N association barrier on Co/Pt is 0.37 eV lower than that on Ni/Pt. Although the barrier is coverage dependent, $\theta_{\text{N}}$ is low at interfacial sites, shown in Figure 5, where desorption happens from, as discussed below.

## V. TEMPERATURE-PROGRAMMED DESORPTION SIMULATIONS

Figure 6(a) shows that the simulated $\text{N}_{2}$ desorption peak temperature is $\sim$720 K, which agrees well with the

![](./images/813171135356076033_8.jpg)

FIG. 6. Temperature programmed desorption (TPD) simulations of $N_2$ desorption on a hexagonal Co cluster on Pt(111). (a) Simulated TPD curve. The surface is shown as inset; the black curved arrows indicate N-N association at the (110) and (100) interfacial sites and the terrace edge. The experimental peak temperatures are shown at the top of the panel with arrows. Results for Ni/Pt surface are also provided for comparison. (b) Effect of initial N coverage, $\theta_{\rm N}$. (c) Color map of N local coverage at the peak temperature of $\sim$720 K. (d) Color map of average association rate in the temperature range 600-720 K (events per second per site for each site type). The white dashed lines indicate the edges of the hexagonal Co cluster on Pt(111). (110) and (100) steps are marked in the panels. (e) and (f) Bar graphs of averaged pair occupation probability and N-N association rate on Co/Pt (600-720 K) and Ni/Pt (500-640 K) surfaces. Interfacial and terrace edge sites near (110) and (100) steps are denoted as inter_110, inter_100, edge_110, and edge_100, respectively.

experimental value of 745 K. Without step sites (on a perfect Co-Pt-Pt surface), our simulated desorption temperature is $\sim$950 K. The peak desorption temperature on Ni/Pt with the same structure is $\sim$640 K, which is about 80 K lower than that of Co/Pt. Microstructures in experiments are difficult to obtain. However, based on Auger experiments, $^4$ we expect diffusion of Ni or Co in Pt to occur during the TPD peak. Specifically, at 600-700 K, the Ni signal reduces to 1/3-1/2 of the initial one in seconds, but remains fairly stable after that; see Figure 12 in Ref. 4. So while the admetal coverage changes with time in the TPD experiments, we believe that significant diffusion in Pt occurs prior to significant desorp- tion; during $N_2$ desorption, the Ni or Co coverage is probably between 20% and 50%, i.e., in the range of those used in our simulations. The comparison of Ni and Co at the same cover- age is definitely valid irrespective of the actual coverage in an experiment, i.e., Co is less active for the same microstructure than Ni despite exhibiting a lower zero coverage N binding energy.

Since the N coverage in experiments is not precisely known, it is possible that the initial $\theta_{\rm N}$ on Ni/Pt and Co/Pt is different. We find that the desorption-peak temperature in- creases by only $\sim$15 K when the initial $\theta_{\rm N}$ decreases from 0.3 to 0.2 (Figure 6(b)). In other words, the initial $\theta_{\rm N}$ is probably

not the cause of the difference in $N_2$ desorption temperature of the two bimetallic surfaces.

The active sites are identified in Figures 6(c) and 6(d). Near the peak desorption temperature of $\sim$720 K, the Co terrace and terrace edge sites have high local coverage: $\theta_N$ of the hcp hollow sites of the Co terrace is $\sim$0.9, where the N average binding energy is $\sim$$-$5.2 eV (0.9 eV stronger than on a Ni terrace at the same $\theta_N$). Although occupation of hcp hollow sites is slightly less favorable above $\theta_N = 0.5$, hcp domains form on the Co terrace that lead to a higher desorption temperature; $\theta_N$ at Co edge hollow sites, f1 and h2 (cf. Figure 2), is $\sim$0.9 and 0.6, respectively.

In order to understand association rates at various sites, it is instructive to compute the pair occupation probability. The product of local coverage at a pair of sites measures the probability of pair occupation in the mean-field approach, but is usually an overestimate due to repulsive interactions between N atoms. The probability of pair occupation $p_{\text{pair}}$ can be estimated from KMC simulations using the time-average method. $^{36}$ The occupation probabilities for both surfaces are shown in Figure 6(e) and the association rates in Figure 6(f). N-N associations happen only at the interfacial sites on the Co/Pt surface, and the Co terrace edge is inactive. As a result, the coverage effect is mainly through the pre-exponential factor (affected by the N-N pair occupation) rather than through the reaction barrier. This can be seen in the shape of the TPD curves; the curve is more asymmetric on Ni/Pt than on Co/Pt.

Occupation of interfacial sites is low due to weak binding and low N-N association barriers: once N-N pairs form, they associate and desorb rapidly. $p_{\text{pair}}$ at (110) and (100) step sites of Ni/Pt are $\sim$$10^{-4}$ and $10^{-11}$, respectively. For Co/Pt, $p_{\text{pair}}$ at (110) and (100) step sites is similar ($\sim$$10^{-8}$).

Given the occupation probabilities and association barriers, on Co/Pt, the interfacial (110) step sites are the most active followed by the (100) step sites with other sites not contributing much. On Ni/Pt, one would expect that the (100) steps are most active due to having the lowest association barrier (Figure 5). Yet, cluster edges of (110) steps are most active, followed by steps and to a less extent by edges of (100) steps. This clearly shows that association barriers alone are not sufficient to explain the most active site of bimetallic catalysts; rather, it is a combination of binding energies (occupation) and association barriers that determine activity. Sensitivity analysis often shows that multiple rate determining steps (RDS) may exist, and the RDS may change with conditions, e.g., Ref. 37. Our work clearly shows that multiple sites and catalyst selection cannot be described with a single descriptor, the zero-coverage binding energy, as has been done before.

Overall, our simulations agree with the experimental TPD results for both Ni/Pt and Co/Pt surfaces. Moreover, we demonstrate that not only the reaction barriers but also the site occupations define the active sites. This change in active site among catalysts makes simple DFT-based prediction break down. Finally, we point out that the different electronic structure of Co/Pt gives rise to two effects, namely different lateral interactions and association barriers, which cause different peak temperatures and shapes of the TPD curves. In order to delineate further the dominant effect, we have changed each of them to that of Ni/Pt (one at a time). The results (Fig. 5S in the supplementary material) $^{38}$ show that each reduces the desorption-peak temperature by $\sim$20 K. At low temperatures, the lateral interactions are more important and above $\sim$640 K, the association barriers become more critical in rationalizing the differences of Co overlayers from those of Ni overlayers on Pt(111).

## VI. CONCLUSIONS

We have employed a multiscale DFT-KMC framework to perform TPD simulations of $N_2$ desorption on Co/Pt bimetallic surfaces and compared the results to those on Ni/Pt surfaces. We show that although Co/Pt binds N slightly weaker than Ni/Pt at low coverages, the coverage dependent N binding energy exhibits different trend on the two bimetallic catalysts. Unlike Ni-Pt-Pt and single metals, N shows attractive interaction on Co-Pt-Pt at low coverages. The attractive (N-N)$_{\text{1st}}$ pair interaction on Co/Pt has been rationalized with the d-band center theory. For N coverages greater than 2/16, the binding energy is reduced slightly compared to single metals and Ni/Pt, i.e., at high coverages, Co/Pt binds N considerably stronger.

Our TPD simulations agree with the experimental results that the $N_2$ desorption peak on Ni/Pt is lower than that on Co/Pt surface despite Co/Pt binding N weaker at low coverages. We show that bimetallics exhibit heterogeneity in binding energy and association barriers, with interfacial sites at (110) and (100) steps and edges of the adlayer clusters being generally more active. The most active site differs from one bimetallic to another due to the complex interplay of thermodynamics (binding energies, occupation) and kinetics (association barriers).

Our simulations indicate that the zero-coverage binding energy based descriptor may be too simplistic to predict catalyst activity quantitatively. Over the past a few years, it has become clear that lateral interactions are important and need to be accounted for in predicting catalyst activity. What our work demonstrates is that lateral interactions alone are not sufficient for quantitatively describing catalyst activity. Islands of admetals create multiple types of sites along and across steps. The reaction barriers and site occupations along with proper description of lateral interactions at these multiple sites define the active sites, and prediction of site occupations at the active sites is required for proper description of catalyst activity. While the picture emerging is much more complex than the simple volcano curve, DFT-KMC simulations provide remarkable quantitative description of experimental data and are ideally suited to predict catalyst activity.

## ACKNOWLEDGMENTS

We acknowledge financial support from the National Science Foundation (NSF) (Grant No. CBET-940768). The DFT calculations were carried out at the Center for Functional Nanomaterials, Brookhaven National Laboratory (supported by the U.S. Department of Energy, Office of Basic Energy Sciences, under Contract No. DE-AC02-98CH10886) and the TeraGrid provided by Texas Advanced Computing Center (TACC) of the University of Texas at Austin.

$^1$J. G. Chen, C. A. Menning, and M. B. Zellner, *Surf. Sci. Rep.* **63**(5), 201–254 (2008).

$^2$C. A. Menning and J. G. G. Chen, *J. Chem. Phys.* **130**(17), 174709 (2009).

$^3$S. Tupy, A. Karim, C. Bagia, W. Deng, Y. Huang, D. Vlachos, and J. G. Chen, *ACS Catal.* **2**(11), 2290–2296 (2012).

$^4$H. Y. Wang, M. Stamatakis, D. A. Hansgen, S. Caratzoulas, and D. G. Vlachos, *J. Chem. Phys.* **133**(22), 224503 (2010).

$^5$W. Guo and D. G. Vlachos, *J. Chem. Phys.* **138**(17), 174702 (2013).

$^6$G. Kyriakou, M. B. Boucher, A. D. Jewell, E. A. Lewis, T. J. Lawton, A. E. Baber, H. L. Tierney, M. Flytzani-Stephanopoulos, and E. C. H. Sykes, *Science* **335**(6073), 1209–1212 (2012).

$^7$J. Greeley and M. Mavrikakis, *Nature Mater.* **3**(11), 810–815 (2004).

$^8$C. J. H. Jacobsen, S. Dahl, B. S. Clausen, S. Bahn, A. Logadottir, and J. K. Norskov, *J. Am. Chem. Soc.* **123**(34), 8404–8405 (2001).

$^9$D. A. Hansgen, L. M. Thomanek, J. G. G. Chen, and D. G. Vlachos, *J. Chem. Phys.* **134**(18), 184701 (2011).

$^{10}$D. A. Hansgen, D. G. Vlachos, and J. G. G. Chen, *Nat. Chem.* **2**(6), 484–489 (2010).

$^{11}$D. A. Hansgen, D. G. Vlachos, and J. G. G. Chen, *Surf. Sci.* **605**(23–24), 2055–2060 (2011).

$^{12}$C. Wu, D. J. Schmidt, C. Wolverton, and W. F. Schneider, *J. Catal.* **286**, 88–94 (2012).

$^{13}$A. B. Mhadeshwar, J. R. Kitchin, M. A. Barteau, and D. G. Vlachos, *Catal. Lett.* **96**(1–2), 13–22 (2004).

$^{14}$T. Bligaard, J. K. Nørskov, S. Dahl, J. Matthiesen, C. H. Christensen, and J. Sehested, *J. Catal.* **224**(1), 206–217 (2004).

$^{15}$M. Salciccioli and D. G. Vlachos, *ACS Catal.* **1**(10), 1246–1256 (2011).

$^{16}$P. A. Redhead, *Vacuum* **12**(4), 203–211 (1962).

$^{17}$W. Guo, M. Stamatakis, and D. G. Vlachos, *ACS Catal.* **3**, 2248 (2013).

$^{18}$G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**(16), 11169–11186 (1996).

$^{19}$G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**(1), 15–50 (1996).

$^{20}$B. Hammer, L. B. Hansen, and J. K. Nørskov, *Phys. Rev. B* **59**(11), 7413–7421 (1999).

$^{21}$P. E. Blöchl, *Phys. Rev. B* **50**(24), 17953–17979 (1994).

$^{22}$G. Kresse and D. Joubert, *Phys. Rev. B* **59**(3), 1758–1775 (1999).

$^{23}$H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**(12), 5188–5192 (1976).

$^{24}$P. Haas, F. Tran, and P. Blaha, *Phys. Rev. B* **79**(8), 085104 (2009).

$^{25}$F. Tran, R. Laskowski, P. Blaha, and K. Schwarz, *Phys. Rev. B* **75**(11), 115131 (2007).

$^{26}$S. R. Bahn and K. W. Jacobsen, *Comput. Sci. Eng.* **4**(3), 56–66 (2002).

$^{27}$Z. P. Liu and P. Hu, *J. Am. Chem. Soc.* **125**(7), 1958–1967 (2003).

$^{28}$M. Stamatakis and D. G. Vlachos, *J. Chem. Phys.* **134**(21), 214115 (2011).

$^{29}$M. Stamatakis, Y. Chen, and D. G. Vlachos, *J. Phys. Chem. C* **115**(50), 24750–24762 (2011).

$^{30}$C. A. Menning, H. H. Hwu, and J. G. G. Chen, *J. Phys. Chem. B* **110**(31), 15471–15477 (2006).

$^{31}$B. Hammer and J. K. Norskov, *Surf. Sci.* **343**(3), 211–220 (1995).

$^{32}$J. R. Kitchin, J. K. Norskov, M. A. Barteau, and J. G. Chen, *Phys. Rev. Lett.* **93**(15), 156801 (2004).

$^{33}$N. Inoglu and J. R. Kitchin, *Phys. Rev. B* **82**(4), 045414 (2010).

$^{34}$D. J. Schmidt, W. Chen, C. Wolverton, and W. F. Schneider, *J. Chem. Theory Comput.* **8**(1), 264–273 (2012).

$^{35}$R. A. van Santen, M. Neurock, and S. G. Shetty, *Chem. Rev.* **110**(4), 2005–2048 (2010).

$^{36}$J. S. Reese, S. Raimondeau, and D. G. Vlachos, *J. Comput. Phys.* **173**(1), 302–321 (2001).

$^{37}$H. Meskine, S. Matera, M. Scheffler, K. Reuter, and H. Metiu, *Surf. Sci.* **603**(10–12), 1724–1730 (2009).

$^{38}$See supplementary material at http://dx.doi.org/10.1063/1.4855235 for KMC input parameters, N adsorption configurations and electronic structure calculations, adsorbate-induced metal bond change, repulsive (N-N)$_{\text{1st}}$ pair interaction model, and sensitivity analysis on energetics.