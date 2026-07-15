
Structural transformations in Cu, Ag, and Au metal nanoclusters

Manoj Settem, \( ^{1} \)  Cesare Roncaglia, \( ^{2} \)  Riccardo Ferrando \( ^{*} \) , \( ^{3} \)  and Alberto Giacomello \( ^{*1} \) 

 \( ^{1} \) Dipartimento di Ingegneria Meccanica e Aerospaziale, Sapienza Università di Roma, via Eudossiana 18, 00184 Roma, Italy.

 \( ^{2} \) Dipartimento di Fisica dell'Università di Genova, via Dodecaneso 33, 16146 Genova, Italy.

 \( ^{3} \) Dipartimento di Fisica dell'Università di Genova and CNR-IMEM, via Dodecaneso 33, 16146 Genova, Italy.

(*Electronic mail: ferrando@fisica.unige.it; alberto.giacomello@uniroma1.it)

Finite-temperature structures of Cu, Ag, and Au metal nanoclusters are calculated in the entire temperature range from 0 K to melting using a computational methodology that we proposed recently [Settem et al., Nanoscale, 2022, 14, 939]. In this method, Harmonic Superposition Approximation (HSA) and Parallel Tempering Molecular Dynamics (PTMD) are combined in a complementary manner. HSA is accurate at low temperatures and fails at higher temperatures. PTMD, on the other hand, effectively samples the high temperature region and melting. This method is used to study the size- and system-dependent competition between various structural motifs of Cu, Ag, and Au nanoclusters in the size range 1 to 2 nm. Results show that there are mainly three types of structural changes in metal nanoclusters depending on whether a solid-solid transformation occurs. In the first type, global minimum is the dominant motif in the entire temperature range. In contrast, when a solid-solid transformation occurs, the global minimum transforms either completely to a different motif or partially resulting in a co-existence of multiple motifs. Finally, nanocluster structures are analyzed to highlight the system-specific differences across the three metals.
 

## I. INTRODUCTION

Metal nanoclusters constitute an important branch of nanotechnology which exhibit size- and shape-dependent properties. Typically, metal nanoclusters adopt \( ^{1} \)  either the non-crystalline icosahedron (Ih) and decahedron (Dh) motifs or the crystalline octahedron (fcc) motif; with the non-crystalline structures being dominant at smaller sizes, but becoming unfavorable at large sizes due to the stress contribution to the energy that is proportional to the volume. \( ^{2-4} \)  Since properties of technological interest (catalytic, optical, etc.) depend on the cluster structure, it is crucial to understand the equilibrium structures of metal nanoclusters. For this purpose, computer simulations can be very useful. Most of the studies available in the literature focus on finding the global energy minimum at a given size. \( ^{3,5-17} \)  Although this information is important, it is limited in the sense that global minima refers to the structures at 0 K. However, metal nanoclusters are expected to be produced and observed at finite temperatures. In addition, various structural motifs coexist \( ^{18,19} \)  at a specific size and temperature. Hence, a method to reliably calculate the equilibrium distribution of various structural motifs in the entire temperature range is essential.

One possible approach is the Harmonic Superposition Approximation (HSA) \( ^{20,21} \)  which has been used to study Lennard Jones, \( ^{22-25} \)  metal, \( ^{18,26} \)  and alloy nanoclusters. \( ^{27,28} \)  Briefly, in this method, a large number ( \( >10^{3} \) ) of low-lying minima are sampled from the potential energy surface (PES) to construct an approximation of the partition function. Subsequently, the temperature-dependent probability of an isomer is calculated based on the partition function. HSA captures the structural distribution at low temperatures fairly accurately. However, at higher temperatures, HSA becomes progressively erroneous. This stems mainly from the failure to accommodate the anharmonic effects which become significant at larger temperatures. Another issue is the difficulty in capturing the melting region. In order to reconstruct the melting region, it is necessary to sample the high energy region of the PES which would require one to collect a prohibitively large number of minima. Due to these constraints melting cannot be reliably captured using HSA.

Alternatively, to sample the phase space effectively, one can simulate several replicas \( ^{29} \)  of the system that are at different temperatures and are allowed to exchange configurations at specific intervals according to a Metropolis-like criterion. This method is referred to as replica exchange or parallel tempering. At higher temperatures, the barriers between various structures are easily overcome ensuring a good sampling at these temperatures. On the other hand, exchange of configurations allows the high temperature configurations to cascade to lower temperatures and, in
 

the process, to improve the phase space exploration at lower temperatures as well. Both Monte Carlo \( ^{30-33} \)  and molecular dynamics \( ^{34,35} \)  can be carried out in conjunction with parallel tempering. In PTMC, generally, random displacement moves are employed to sample configurations; which reduces the likelihood of inter-motif transition with increasing cluster size. \( ^{36} \)  Also, collective atomic rearrangements \( ^{37} \)  are involved during inter-motif transition involving metallic clusters which might not be straightforward to incorporate into Monte Carlo sampling. As a result, in this work, we carry out parallel tempering with molecular dynamics.

Recently, we have proposed a method \( ^{19} \)  that combines HSA and parallel tempering leveraging the advantages offered by these two methods to capture the structural distribution in the entire temperature range (0 K to melting). First, we carry out parallel tempering molecular dynamics (PTMD) with several replicas at temperatures ranging from room temperature to beyond melting. A large collection of local minima are sampled during the PTMD simulations which are then fed into the HSA calculations. This combined method offers several advantages where HSA and PTMD act in a complementary fashion. The conventional HSA calculations require collection of a large number of local minima which are obtained using structure optimization methods. \( ^{18,27} \)  In our case, the minima are directly obtained from PTMD simulations without the need to explicitly search for them. HSA can capture the low temperature solid-solid transitions which might prove to be elusive for PTMD. On the other hand, PTMD captures the high temperature and the melting regions accurately where HSA calculations fail. As a result, the low temperature and the high temperature regions are accurately captured by HSA and PTMD respectively. In the intermediate temperatures, HSA and PTMD have a good agreement.

In this work, we apply this method to study the size- and system-dependent structural changes with temperature in Cu, Ag, and Au metal nanoclusters. This is crucial information given their strong influence on the properties of metal nanoclusters. For example, catalytic activity of metal nanoclusters depends on the structure type and size \( ^{38-41} \)  due to the wide variety of catalytic sites. \( ^{42} \)  In addition, the catalytic activity can be enhanced by an ensemble of different geometrical structures in comparison to homogeneously shaped structures. \( ^{43} \)  Hence, it is essential to gather knowledge on the equilibrium structural distribution where various geometrical motifs coexist.

Several theoretical works have calculated the global minimum structures of Cu, Ag, and Au nanoclusters. Grigoryan et al. \( ^{9} \)  calculated the global minima of Cu clusters up to 150 atoms using the embedded atom method (EAM), \( ^{44} \)  and up to 60 atoms using Gupta \( ^{45} \)  and Sutton-Chen \( ^{46} \)  potentials. Highly stable structures occur at the sizes 13, 19, 55, 92, and 147 with all of them having
 

high symmetry icosahedral structures except 92 which is a chiral structure having T point group symmetry. Most of the structures are icosahedra with the sizes 4, 17, 26, 28, 29, 91–95 having tetrahedral geometry and 75, 78, 81, 101–103 being decahedra. In the case of Ag nanoclusters of sizes larger than 60 atoms, decahedron is found to be the dominant motif. \( ^{7,10,11,15} \)  There are few exceptions where truncated octahedron (fcc) and icosahedron (Ih) are the global minima. Due to the strong relativistic effects, \( ^{47} \)  Au nanoclusters exhibit peculiar structures. At sizes smaller than 40 atoms, Au nanoclusters adopt either planar or hollow cage-like geometries. \( ^{48-54} \)  In comparison to Cu and Ag, Au disfavors icosahedral structures. At the magic sizes of 55, 147, and 309 the icosahedron is not the global minimum. \( ^{14,18,37} \)  This is also evident over larger size range (up to 1000 atoms). \( ^{3} \)  However, when the icosahedral structures are observed in Au nanoclusters, for example, at higher temperatures, \( ^{55,56} \)  they typically have “rosette” \( ^{57,58} \)  defects on the surface. A “rosette” defect appears when a vertex atom is pushed out to form a six-atom ring with the five neighboring surface atoms leaving behind a vacancy at the vertex position.

Cu, Ag, and Au clusters have also been studied using density functional theory (DFT) calculations. Generally, ideal structures are considered since global minimum search becomes prohibitive at the DFT level for clusters larger than  \( \sim \)  50 atoms. \( ^{59} \)  Roldán et al. \( ^{60} \)  carried out structural analysis of several “magic” sized octahedral Cu, Ag, and Au clusters in the range 38 – 225 atoms and identified a correlation to estimate cohesive energies in a large size range. Similarly, Kiss et al. \( ^{61} \)  studied octahedral and icosahedral Ag clusters (consisting of 6 – 600 atoms) and observed that the cohesive energy is linear with inverse of cluster size. Oliveira et al. \( ^{62} \)  showed that Ag icosahedra are energetically stable compared to cuboctahedra through density functional tight binding (DFTB) calculations of “magic” clusters in the range 55 – 561 atoms.

The picture arising from experiments is more complex, since in experiments it is often difficult to disentangle kinetic effects from equilibrium ones. \( ^{1} \)  Electron microscopy has been used to study the structure of metal nanoclusters with varying size and temperature. Langlois et al. \( ^{63} \)  prepared Cu nanoparticles in a broad size range of 1 nm to 12 nm using thermal evaporation. They observed a significant overlap between icosahedra and decahedra at sizes less than 8 nm beyond which fcc structures were observed. Volk et al. \( ^{64} \)  analyzed Ag clusters with size < 7 nm grown in superfluid He droplets. The smallest particles were fcc, with decahedra at intermediate sizes and icosahedra at large sizes. However, theoretical predictions \( ^{2,3} \)  show that icosahedra are energetically favored at smaller sizes while fcc are favored at larger sizes, while large icosahedra are likely to be due to kinetically trapped growth on top of smaller decahedra. \( ^{65,66} \)
 

Recently, the structural distribution of size-selected Ag clusters centered around 309 atoms was measured, \( ^{67} \)  finding an abundance of fcc structures with very little icosahedra (2%). This is in contrast to the prediction that icosahedra is the dominant motif around the size 309. \( ^{3} \)  Wells et al. \( ^{68} \)  calculated the proportion of various motifs of  \( Au_{561} \) ,  \( Au_{742} \) , and  \( Au_{923} \) . At these sizes, fcc and decahedra making up 70% of the structures while icosahedra contribute less than 5%. Finite-temperature distribution of  \( Au_{561} \)  was calculated by Foster et al. \( ^{69} \)  in the temperature range 20°C to 500°C. Again, icosahedra were almost non-existent beyond 100°C with less than 3%. At temperatures greater than 125°C, there is an increase in the proportion of decahedra at the expense of fcc structures. The experiments establish a lack of preference for the icosahedral motif in Au nanoclusters, in agreement with the findings of Gupta potential and DFT calculations. \( ^{70} \) 

From a theoretical and experimental viewpoint, it is essential to have a knowledge of the equilibrium proportion of various structural motifs as a function of temperature. In this work we calculate the structural distribution of Cu, Ag, and Au metal nanoclusters at the sizes 90, 147, and 201 which fall in the size range of 1 nm to 2 nm. These were chosen to highlight the size-and system-dependent structural changes. 147 and 201 are “magic” sizes corresponding to perfect icosahedron (147) and regular truncated octahedron (201). It is generally assumed that “magic” sized structures have energetic stability. Our results show that this assumption is not always true. Finally, we chose 90 to look at non-magic sized structures.

## II. METHODS

We use the tight binding model within the second moment approximation (TBSMA) \( ^{71} \)  which is also referred to as Gupta \( ^{45} \)  potential or Rosato-Guillope-Legrand (RGL) \( ^{72} \)  potential to model the atom-atom interactions in Cu, Ag, and Au nanoclusters. The parameters of the Gupta potential have been taken from Ref. \( ^{2} \) . The interaction potential of Au gives an accurate description of the experimental cluster structures in gas phase \( ^{68} \)  and on MgO substrates. \( ^{73} \)  In addition, this potential agrees well with DFT calculations in the prediction of surface “rosette” defects in icosahedra \( ^{57} \)  and the tendency to disfavor icosahedra. \( ^{70} \)  Coming to Ag and Cu, the Gupta potentials correctly predict the stability of Mackay stacking over anti-Mackay stacking in icosahedral clusters in line with the DFT calculations (see Supporting Information in ref. \( ^{74} \) ). In Ag \( _{586} \) , fcc structure is energetically preferred in comparison to icosahedron which is also the case according to DFT. \( ^{75} \) 

Gupta potential predicts correctly that Ag icosahedra are energetically stable compared to
 

cuboctahedra which agrees with the DFTB calculations \( ^{62} \)  (see the plot of energy difference between cuboctahedron and icosahedron in supplementary figure S1). At the size 147, icosahedra and decahedra are the prominent motifs. In order to assess the competition between these motifs, we have carried out DFT calculations for  \( Cu_{147} \)  and  \( Ag_{147} \) . For  \( Au_{147} \)  clusters, we refer to the calculations done previously. \( ^{70} \)  DFT calculations were carried out using Quantum ESPRESSO \( ^{76} \)  code. Projected augmented wave (PAW) \( ^{77} \)  pseudopotentials were used with Perdew-Burke-Ernzerhof (PBE) \( ^{78} \)  exchange-correlation functional. An energy cutoff of 45 Ry was used for both Ag, Cu; while the charge density cutoff of 181 Ry, 236 Ry were used for Ag, Cu respectively. The calculations were considered to be converged with energy and force tolerance of  \( 1 \times 10^{-4} \)  Ry and  \( 1 \ times 10^{-3} \)  Ry/a.u. respectively. The energy difference between decahedron (Dh) and icosahedron (Ih) defined as,  \( E_{Dh} - E_{Ih} \) , at the DFT/PBE level are +3.87 eV, +2.55 eV, and -2.56 eV for Cu, Ag, and Au respectively. The corresponding values according to Gupta potential are +1.57 eV, +0.46 eV, and -1.86 eV. Both DFT/PBE and Gupta show therefore the same trend: Ih is energetically preferred in Cu and Ag while Dh is favored in Au. Based on these results, we believe that Gupta potentials are reliable for analyzing structural trends between Cu, Ag, and Au metal nanoclusters. The use of this model will allow a thorough sampling of the energy landscape which would be hardly feasible by DFT. A detailed comparison of Gupta potential with DFT calculations is provided in the Results and Discussion section which allows us to assess its performance and limitations.

Before the PTMD simulations, we calculate the global minimum at each size using basin hopping Monte Carlo (BHMC) \( ^{19,37,79} \)  optimization search. For each size, we run five independent search simulations with at least  \( 2.5 \times 10^{5} \)  basin hopping steps.

The detailed procedure of the combined method of PTMD+HSA is described in a previous work \( ^{19} \) . Here we only recapitulate it briefly. In the PTMD simulations, there are two fundamental parameters: the number of replicas (M) and the temperature,  \( T_{m} \)  ( \( m = 1, 2, 3, \ldots, M \) ) of each replica. All the replicas are in a canonical ensemble (NVT) and exchange of configurations between a pair of replicas is attempted at specific intervals. The number of replicas is chosen such that we have at least 20–30% acceptance of the replica swaps. This is achieved by calculating an approximate caloric curve to identify the melting range and then adjusting the number of replicas and their temperatures to achieve the desired swap acceptance rate. All the PTMD simulations have been carried out in LAMMPS. \( ^{80} \)  We use a time step of 5 fs for the molecular dynamics evolution and replica swaps are attempted every 250 ps. They are either accepted or rejected according to a
 

Metropolis-like criterion.

We begin the PTMD simulations with all the replicas having the same structure, either global minimum or a low energy structure. After discarding the initial phase of PTMD ( \( \sim 0.5 \mu s \) ), we sample configuration at 125 ps after a swap attempt for a total time of about 1  \( \mu s \)  to 2  \( \mu s. \) 

The configurations sampled from PTMD simulations are also fed into the HSA analysis. In the HSA \( ^{18,27,28} \)  method, the partition function is given by,

 \[ Z=\sum_{i}\frac{e^{-\beta E_{i}^{0}}Z_{i}^{tr}Z_{i}^{rot}Z_{i}^{vib}}{g_{i}} \quad (1) \] 

where  \( \beta = 1/(k_{B}T) \) . The summation is over all the local minima, i, considered for the HSA.  \( E_{i}^{0} \)  is the energy of the local minimum, i.  \( Z^{tr} \) ,  \( Z^{rot} \) , and  \( Z^{vib} \)  are the translational, rotational, and vibrational contributions to the partition function, respectively. It has been shown that only the vibrational contribution is sufficient to calculate the probability of the local minima. \( ^{27} \)  The denominator,  \( g_{i} \) , is the order of the symmetry group of the local minimum i. The vibrational contribution due to a single minimum is given by

 \[ Z^{v i b}=\prod_{n=1}^{3N-6}\frac{e^{-\beta\hbar\omega_{n}/2}}{1-e^{-\beta\hbar\omega_{\mathrm{n}}/2}} \quad (2) \] 

where  \( \omega_{n} \)  are the  \( 3N-6 \)  (N is the number of atoms in the cluster) frequencies of the normal modes. The probability of a local minimum as a function of temperature is now given by

 \[ p_{i}=\frac{e^{-\beta E_{i}^{0}}Z_{i}^{v i b}/g_{i}}{\sum_{j}e^{-\beta E_{j}^{0}}Z_{j}^{v i b}/g_{j}} \quad (3) \] 

We define the probability of a specific structure type  \( (p^{struct}) \)  by summing up the probabilities of all the minima belonging to that structure type.

 \[ p^{s t r u c t}=\sum_{k}p_{k} \quad (4) \] 

where k represents all the minima having the same structure. Local minima for the HSA analysis were collected from PTMD simulations up to an energy cutoff of 1 eV to 1.5 eV with the exception of  \( Cu_{147} \)  and  \( Ag_{147} \)  where 2.5 eV was used. Two minima were considered to be different if they belonged to different structure types and were separated by at least 0.05 meV in energy. For identifying the geometrical motif of a given configuration, we use common neighbor analysis (CNA) \( ^{81} \)  signatures. The structures are classified using the same scheme that we employed for Au nanoclusters previously \( ^{19,82} \)  and categorize them into decahedron (Dh), icosahedron (Ih), twin,
 

fcc, and amorphous structure classes. A structure that does not fall into any of these categories is classified as a mix structure. Typically, these structures are not well defined or contain structural features of more than one geometrical motif. These structures will be described in more detail while presenting the results. Further details about the parameters used for HSA and PTMD are provided in the Supplementary Information.

## III. RESULTS AND DISCUSSION

We will present the results of Cu and Ag nanoclusters. We note that structural distribution of Au nanoclusters has been previously reported by us \( ^{19} \)  and we use it here to make a comparison with Cu and Ag. Also, we compare in detail the structures of Au, Cu, and Ag which was not reported previously. To begin with, we discuss the finite-temperature structural distributions and then make a comparison to highlight the differences and similarities between Cu, Ag, and Au clusters. The melting point of all the metal nanoclusters in the current work are reported in Table I. We identify the melting point by first constructing the heat capacity  \( (C_{V}) \)  curve from PTMD simulations. Melting point is then calculated as the peak of  \( C_{V} \)  curve.

TABLE I. Melting point (in K) of Cu, Ag, and Au nanoclusters.

<table><tr><td>Cu_{90}</td><td>Cu_{147}</td><td>Cu_{201}</td><td>Ag_{90}</td><td>Ag_{147}</td><td>Ag_{201}</td><td>Au_{90}</td><td>Au_{147}</td><td>Au_{201}</td></tr><tr><td>609</td><td>779</td><td>745</td><td>510</td><td>651</td><td>654</td><td>420</td><td>505</td><td>550</td></tr></table>

## A. Cu

Cu has a strong preference for icosahedral motif as compared to Ag and Au. \( ^{2,3} \)  The global minimum of  \( Cu_{90} \) ,  \( Cu_{147} \) , and  \( Cu_{201} \)  are shown in Fig. 1. The global minimum of  \( Cu_{90} \)  and  \( Cu_{147} \)  are both icosahedra with  \( Cu_{90} \)  having  \( C_{2v} \)  point group symmetry. However, with the EAM potential, the global minimum of  \( Cu_{90} \)  was predicted to be an icosahedron with  \( C_{s} \)  symmetry. \( ^{9} \)  The best structure of  \( Cu_{201} \)  is a decahedron with  \( C_{s} \)  point group symmetry.

In the case of  \( Cu_{90} \) , icosahedron (Ih) is the dominant motif at room temperature with very small amount of twins, decahedra (Dh) and mix structures (Fig. 1a). The mix structures comprise several different geometric types. Predominantly, the mix structures consist of icosahedral-based geometries that either have amorphous regions or the entire structure adopts a configuration similar to
 
![](./images/898633096998420845_1.jpg)

FIG. 1. Structural distribution of (a)  \( Cu_{90} \) , (b)  \( Cu_{147} \) , and (c)  \( Cu_{201} \) . PTMD, HSA results are shown in the top and middle rows. Global minimum structures are shown in the bottom row. In the HSA results, for comparison, we report with vertical lines the range of PTMD temperatures and with a dashed line the fraction of amorphous structures calculated from PTMD simulations.

the 92-atom chiral structure \( ^{9,83} \)  with two missing atoms. The remaining mix structures consist of polydecahedra (p-Dh) which have more than one local fivefold axis. \( ^{19,37,84} \)  With increasing temperature, the proportion of mix structures increases at the expense of Ih and peaks before melting at  \( \sim \)  600 K. Qualitatively, HSA predicts similar structural changes in  \( Cu_{90} \) . The agreement between HSA and PTMD is good at room temperature and thereafter there are quantitative discrepancies. The increase in mix structures is rather slow according to HSA. For example, at 600 K, PTMD predicts 71.2% mix structures, while HSA predicts only 20.6%.

At size 147 (Fig. 1b), the icosahedron, which is the global minimum, dominates in the entire temperature range according to both PTMD and HSA. This indicates a high thermal stability of the icosahedral motif at this size. Moving on to  \( Cu_{201} \)  (Fig. 1c), again, the global minimum structure, a decahedron, dominates at room temperature and its proportion decreases steadily with temperature. Icosahedra compete with decahedra at higher temperatures with maximum proportion of Ih observed at 700 K just before melting. HSA on the other hand, predicts a significantly higher amount of Ih at this temperature (77.2% vs 33.7%). Interestingly, fcc and twin structures are almost absent in  \( Cu_{90} \) ,  \( Cu_{147} \) , and  \( Cu_{201} \)  clusters in the entire temperature range.
 

## B. Ag

The global minimum structures of  \( Ag_{90} \)  and  \( Ag_{201} \)  (Fig. 2) are decahedra with both structures having  \( C_{s} \)  point group symmetry. The ideal icosahedron is the global minimum of  \( Ag_{147} \) . These results are consistent with the previously reported global minima at these sizes for Ag clusters. \( ^{10,11,15} \) 

Ag \( _{90} \)  exhibits interesting structural changes (Fig. 2a). From the HSA results, it is evident that the global minimum decahedron undergoes a partial transition to twin and mix structures with increasing temperature, leading to a combination of Dh + twin + mix structures at 250 K. Considering the PTMD results, the proportion of Dh, twins, and mix structures remains constant up to  \( \sim \)  450 K. This is a case of one-to-many solid-solid transition \( ^{27} \)  where one geometrical motif, the Dh, is replaced by a coexistence of Dh, twins, and mix structures. Above 450 K, the proportion of mix structures increases at the expense of Dh and twins. The mix structures are a combination of polydecahedra \( ^{37} \)  and distorted icosahedra having amorphous regions. The structural changes in Ag \( _{147} \)  and Ag \( _{201} \)  (Figs. 2b, c) are fairly straightforward. In both cases, the global minimum

![](./images/898633096998420845_2.jpg)

![](./images/898633096998420845_3.jpg)

![](./images/898633096998420845_4.jpg)

![](./images/898633096998420845_5.jpg)

![](./images/898633096998420845_6.jpg)

![](./images/898633096998420845_7.jpg)

![](./images/898633096998420845_8.jpg)

![](./images/898633096998420845_9.jpg)

FIG. 2. Structural distribution of (a)  \( Ag_{90} \) , (b)  \( Ag_{147} \) , and (c)  \( Ag_{201} \) . PTMD, HSA results are shown in the top and middle rows. Global minimum structures are shown in the bottom row. In the HSA results, for comparison, we report with vertical lines the range of PTMD temperatures and with a dashed line the fraction of amorphous structures calculated from PTMD simulations.
 

motif (Ih for 147 and Dh for 201) dominates in the entire temperature range, with other motifs nonexistent or in extremely small proportions.

## C. Au

We have recently \( ^{19} \)  reported the structural changes in Au nanoclusters and hence, we will only summarize them briefly here (see supplementary figure S2). The global minimum structures of  \( Au_{90} \) ,  \( Au_{147} \) , and  \( Au_{201} \)  are fcc, decahedron, and fcc (ideal truncated octahedron), respectively. At size 90, the global minimum motif, fcc, is dominant at lower temperatures and competes with twin and mix structures. With increasing temperature, fcc structures decrease along with an increase in mix structures. In the case of  \( Au_{147} \) , the decahedron (global minimum) remains dominant up to melting along with small amounts of twin and fcc structures. Above 400K, Ih and mix structures begin to appear with mix structures dominating close to melting. In  \( Au_{201} \) , there is a solid-solid transition from the fcc global minimum (a truncated octahedron) to a Dh at low temperature around 200 K. Thereafter, the Dh dominates up to melting along with a small amount of twins ( \( \sim 10\% \) ).

## D. Cu, Ag, and Au all together: combined HSA+PTMD

We stitch together HSA and PTMD results in order to get the structural changes in the entire temperature range in a single plot. Data for Au are taken from ref. \( ^{[19]} \) . Figure 3 compares the available results for Cu, Ag, and Au at all temperature and sizes. HSA and PTMD are stitched together at 300 K. At the temperature where HSA and PTMD are joined, their structural distributions have an excellent agreement except for small jumps in the case of  \( Ag_{90} \)  and  \( Au_{90} \) , where the trends are anyway consistent. This shows that our approach of combining HSA and PTMD is fairly robust and validated across various metal systems.

There are broadly three categories of structural changes that can be observed: type-(i) the global minimum remains the dominant motif up to melting, where amorphous takes over; type-(ii) solid-solid transitions occur, either completely or partially, well below melting temperature, resulting in an entirely different dominant motif; type-(iii) solid-solid transitions gradually occur leading to a co-existence of multiple motifs. The cases  \( Cu_{147} \) ,  \( Ag_{147} \)  and  \( Ag_{201} \)  of fall into the first category, while  \( Au_{201} \)  falls into the second category. All other cases fall into the third category, but with some differences. In  \( Au_{147} \)  and  \( Cu_{201} \) , the coexistence between motifs is present in a relatively
 
![](./images/898633096998420845_10.jpg)

FIG. 3. Structural changes in the entire temperature range by combining HSA and PTMD in Cu, Ag, and Au nanoclusters. Vertical line in each plot indicates the temperature at which HSA and PTMD are stitched together. The type of structural transformation is also indicated. Description of the various types of structural transformations is provided in the text.

narrow temperature range close to melting, whereas in all clusters of size 90 coexistence is already found at low temperatures.

The results show that ideal geometries corresponding to the “magic” sizes are not necessarily energetically preferred. Here we considered two “magic” sizes, 147 and 201. At size 201, truncated octahedron has the perfect geometry. However, only Au has truncated octahedron as the global minimum, while decahedron prevails for Cu and Ag. Even in Au, the global minimum transforms to Dh which remains the dominant structure at finite temperatures. On the other hand, at size 147, which corresponds to a perfect icosahedron, both Cu and Ag have this structure as the global minimum. However, decahedron is the global minimum of  \( Au_{147} \)  with some icosahedra appearing only above 400 K. At size 90, all three systems have a different geometrical motif as the global minimum – Ih for  \( Cu_{90} \) , Dh for  \( Ag_{90} \) , and fcc for  \( Au_{90} \)  – which remains dominant (Cu, Au) or competes with other motifs (Ag). The structural distribution of Cu reinforces the strong preference of icosahedral motif in Cu clusters.
 

## E. Structural characterization

We have, so far, discussed how the various geometrical motifs compete with temperature. In this section, we characterize the structural features of the various motifs.

Typical structures of  \( Cu_{90} \)  are shown in Fig. 4 along with their energies relative to the global minimum. The icosahedron is the dominant motif of  \( Cu_{90} \)  along with minor amounts of twin and Dh. The twin structures of  \( Cu_{90} \)  typically have stacking faults (second structure in Fig. 4a). At higher temperatures, icosahedra resembling the 92-atom incomplete Mackay icosahedron having  \( C_{3v} \)  point group symmetry are observed. These structures have two surface vacancies at various positions on the 92-atom cluster resulting in  \( Cu_{90} \)  icosahedra. An example is shown in the third structure in Fig. 4a. As the temperature increases further, some of these icosahedra undergo a twist and transform to mix structures resembling the 92-atom chiral geometry with tetrahedral T symmetry (fourth structure in Fig. 4a). The 92-atom chiral structure is the global minimum \( ^{9,83} \)  of  \( Cu_{92} \)  and has also been experimentally confirmed to have T symmetry from a comparison of the photoelectron spectra of Na and Cu clusters. \( ^{85-87} \)  Again, the chiral-like  \( Cu_{90} \)  clusters have two surface vacancies.

In the case of  \( Ag_{90} \)  (Fig. 4b), along with the conventional decahedron (first structure), we find decahedra with either one (third structure) or two (second structure) hcp islands. When the two hcp islands are adjacent to each other, a local decahedral axis is formed at the intersection which can be considered as a polydecahedron (p-Dh) \( ^{84} \)  which has more than one decahedral axis. The twin motif which competes with Dh consists of either a single hcp plane (fourth structure) or stacking faults (fifth structure). Moving on to  \( Au_{90} \)  (Fig. 4c), the twins predominantly have a single hcp plane unlike  \( Cu_{90} \)  and  \( Ag_{90} \) . Also,  \( Au_{90} \)  decahedra have deeper reentrant grooves (see the arrow in Fig. 4c) compared to decahedra of Cu and Ag. This is consistent with the general trend found in Ref. \( ^{2} \)  The decahedron can undergo surface restructuring resulting in a mix structure (see fourth structure in Fig. 4c). Consider the four atoms (1, 2, 3, and 4) shown before (top) and after (bottom) restructuring. The atoms 2, 4 are pushed apart and the atoms 1, 3 come closer leading to a  \( \{100\} \)  like arrangement.

At size 147, we observe a gradual change in the nature of icosahedra from Cu to Ag to Au. With increasing temperature, the perfect icosahedra becomes defective with, initially, single vertex vacancy (second structure in Fig. 5a) and at still higher temperatures, multiple vacancies (third structure). These same vertex vacancies are also observed in  \( Ag_{147} \)  icosahedra (second and fifth
 
![](./images/898633096998420845_11.jpg)

FIG. 4. Structures of (a)  \( Cu_{90} \) , (b)  \( Ag_{90} \) , and (c)  \( Au_{90} \) . The energy of each structure is relative to the global minimum (0 eV). The arrow in (c) shows the relatively deeper reentrant groove in Au compared to Cu and Ag. Atoms marked 1, 2, 3, and 4 show the surface restructuring in  \( Au_{90} \)  decahedron.

structures in Fig. 5b). However, along with the vertex vacancies, we also observe “rosette” \( ^{57,58} \)  defects where the vertex atom protrude to join the five nearest neighbors on the surface to form a six-atom ring. These are highlighted in blue for  \( Ag_{147} \)  in Fig. 5b where either two or three “rosette” defects occur together. Icosahedra in  \( Au_{147} \) , which appear mainly above 400 K, almost always have “rosette” defects as shown in Fig. 5c.  \( Au_{147} \)  decahedra at higher temperatures exhibit deep reentrant grooves compared to the global minimum (second and third structures in 5c). The twins in  \( Au_{147} \)  predominantly have single hcp planes as shown in 5c.

Finally, at size 201, all three systems have Dh as the dominant motif at room temperature. In  \( Cu_{201} \)  and  \( Ag_{201} \) , the various decahedra that are observed are all obtained by differing arrange-
 
![](./images/898633096998420845_12.jpg)

FIG. 5. Structures of (a)  \( Cu_{147} \) , (b)  \( Ag_{147} \) , and (c)  \( Au_{147} \) . The energy of each structure is relative to the global minimum (0 eV). "Rosette" defects in (b) and (c) are highlighted in blue.

ments of nine additional atoms on magic sized 192-atom Marks decahedron. The nine additional atoms are indicated in red (see Figs. 6a, b). The twins in  \( Cu_{201} \)  have significant amount of hcp regions and are either completely hcp or consist of stacking faults. At higher temperatures, we observe icosahedra which are incomplete 309-atom icosahedra. In  \( Au_{201} \) , Dh is the dominant motif. In this case the best Dh (second structure in Fig. 6c) is different from the typical decahedra observed in Cu and Ag which are formed by adding nine atoms to the 192-atom Decahedron. Instead, the best Dh of  \( Au_{201} \)  is highly asymmetrical with deep reentrant grooves. However, at higher temperatures, we do observe Dh structures similar to those of Cu and Ag (third structure in Fig. 6c).

In addition to the structures discussed above, we also observe structures that are not straightforward to categorize. We refer to these as mix structures which occur in greater proportions at the smallest size of 90. The typical mix structures at the size 90 are shown in Fig. 7. In polydecah
 
![](./images/898633096998420845_13.jpg)

FIG. 6. Structures of (a)  \( Cu_{201} \) , (b)  \( Ag_{201} \) , and (c)  \( Au_{201} \) . The energy of each structure is relative to the global minimum (0 eV). The atoms in red indicate the additional nine atoms that are arranged on 192-atom Marks' decahedron to form various 201-atom decahedra.

dron (p-Dh), \( ^{84} \)  more than one decahedral axis is present within the same nanocluster. Examples of  \( Cu_{90} \)  and  \( Ag_{90} \)  p-Dh consisting of three decahedral axes are shown in the first image of Figs. 7a, b. On the other hand, p-Dh are highly uncommon in  \( Au_{90} \) . Another type of mix structure has icosahedral region along with disordered region. All the three systems exhibit these structures (second image in Figs. 7a, b and first image in 7c). A third type of mix structure occurs when local icosahedral features are observed within fcc/twin (final image in Fig. 7a) or decahedron (final image in Figs. 7b, c). This type of structures are mainly observed in Au and are less common in Cu and Ag clusters. The proportion of mix structures is significantly lower at larger sizes of 147 and 201. We observe structures similar to those at the size 90 with icosahedra mixed with disordered region being more dominant. A detailed analysis of mix structures in Au clusters has been discussed previously. \( ^{19} \)
 
![](./images/898633096998420845_14.jpg)

FIG. 7. Mixed structures of (a)  \( Cu_{90} \) , (b)  \( Ag_{90} \) , and (c)  \( Au_{90} \) . The large red atoms in (a) and (b) indicate the various decahedral axes. In (a) and (b), first image is a polydecahedron (p-Dh), second image is an icosahedron with disordered region. Third image in (a) consists of twin region and icosahedral region. The final image in (b) and (c) are mixed structures with decahedral and icosahedral regions coexisting.

## F. Comparison with DFT

The structural distributions of Cu, Ag, and Au presented so far correspond to Gupta potential which does not account for the electronic interaction between atoms. In order to assess the performance of Gupta potential, we make a comparison with DFT calculations. We used PAW pseudopotentials with three types of exchange-correlation functionals – Perdew-Burke-Ernzerhof (PBE), \( ^{78} \)  local-density approximation (LDA), \( ^{88} \)  and PBE revised for solids (PBEsol). \( ^{89} \) 

We choose highly probable motifs (either two or more structures per each metal per each size) depending on the structural distribution. For instance, Ih and mix are the most dominant motifs of  \( Cu_{90} \) . In the case of  \( Ag_{90} \) , three motifs coexist – Dh, twin, and mix. Hence, we chose the lowest energy Ih, mix for  \( Cu_{90} \)  and Dh, twin, mix for  \( Ag_{90} \) . All the Cu and Ag structures used for DFT calculations are shown in Fig. 8. For a given combination of metal and size, we measure the energy difference of each structure with respect to the global minimum predicted by Gupta potential. These values are reported in Table II for Gupta potential, DFT/PBE, DFT/LDA, and DFT/PBEsol.

In case of  \( Cu_{90} \)  and  \( Cu_{147} \) , Ih has lower energy according to both Gupta and DFT. However, for  \( Cu_{90} \) , Ih wins by only  \( \sim 0.08 \)  eV in comparison to > 1 eV for all three DFT calculations. On the
 
![](./images/898633096998420845_15.jpg)

FIG. 8. Cu and Ag structures used for DFT calculations.

other hand,  \( Cu_{147} \)  has a very good quantitative agreement with DFT. For  \( Cu_{201} \) , Gupta potential predicts Dh to have lower energy than Ih in contrast to DFT. In case of  \( Ag_{90} \) , DFT favours twin in comparison to mix and Dh. According to DFT, the energetic ordering is  \( E_{twin} < E_{Dh} < E_{mix} \) . Gupta potential, on the other hand, predicts Dh to have the lowest energy among the three. There is a good agreement between Gupta potential and DFT for  \( Ag_{147} \)  and  \( Ag_{201} \) .

Moving on to Au, the various structures used for DFT calculations are shown in Fig. 9. In the case of  \( Au_{90} \) , we observe a lack of consistency among the various exchange-correlation functionals. There is a good agreement between Gupta potential, DFT/LDA, and DFT/PBEsol with all three predicting a lower energy for fcc vs. twin. However, DFT/PBE predicts twin to be the lowest energy structure. For  \( Au_{147} \) , we considered all the motifs (other than amorphous) given their co-existence before the melting region. Au icosahedra typically have “Rosette” defects. Hence, we also considered the regular closed-shell 147-atom icosahedron and refer to it as Ih-reg in order to assess the competition between them. The energetic ordering according to Gupta potential is  \( E_{Ih-reg} > E_{Ih} > E_{mix} > E_{fcc} > E_{twin} > E_{Dh} \) . Firstly, Ih-reg has higher energy than Ih according to Gupta potential and DFT calculations confirming that Au favors defective icosahedra consisting
 

TABLE II. Comparison of energy differences ( \( \Delta E \)  in eV) of various motifs for Gupta potential and DFT with different exchange-correlation functional. Also, the values corresponding to embedded atom method (EAM) potentials are provided in the final column.

<table><tr><td>System</td><td>\( \Delta E \)</td><td>Gupta</td><td>DFT/PBE</td><td>DFT/LDA</td><td>DFT/PBEsol</td><td>EAM</td></tr><tr><td>Cu_{90}</td><td>E_{mix}-E_{lh}</td><td>0.0828</td><td>1.09</td><td>1.10</td><td>1.19</td><td>0.2472</td></tr><tr><td>Cu_{147}</td><td>E_{mix}-E_{lh}</td><td>1.5815</td><td>2.14</td><td>-</td><td>-</td><td>1.8238</td></tr><tr><td>Cu_{201}</td><td>E_{lh}-E_{Dh}</td><td>0.9286</td><td>-0.507</td><td>-0.252</td><td>-</td><td>0.9003</td></tr><tr><td>Ag_{90}</td><td>E_{mix}-E_{Dh}</td><td>0.0252</td><td>0.159</td><td>0.139</td><td>0.149</td><td>-0.0043</td></tr><tr><td>Ag_{90}</td><td>E_{twin}-E_{Dh}</td><td>0.0319</td><td>-0.231</td><td>-0.422</td><td>-0.325</td><td>-0.1193</td></tr><tr><td>Ag_{147}</td><td>E_{mix}-E_{lh}</td><td>1.0019</td><td>1.51</td><td>-</td><td>-</td><td>1.3051</td></tr><tr><td>Ag_{201}</td><td>E_{twin}-E_{Dh}</td><td>0.1193</td><td>0.609</td><td>-</td><td>-</td><td>0.0659</td></tr><tr><td>Au_{90}</td><td>E_{twin}-E_{fcc}</td><td>0.0522</td><td>-0.106</td><td>0.0761</td><td>0.0641</td><td>0.1666</td></tr><tr><td>Au_{147}</td><td>E_{twin}-E_{Dh}</td><td>0.0470</td><td>0.114</td><td>-</td><td>-</td><td>0.4785</td></tr><tr><td>Au_{147}</td><td>E_{fcc}-E_{Dh}</td><td>0.1089</td><td>0.616</td><td>-</td><td>-</td><td>0.0819</td></tr><tr><td>Au_{147}</td><td>E_{mix}-E_{Dh}</td><td>0.6411</td><td>-0.348</td><td>-0.330</td><td>-0.209</td><td>0.4746</td></tr><tr><td>Au_{147}</td><td>E_{lh}-E_{Dh}</td><td>0.9104</td><td>-0.176</td><td>0.189</td><td>0.175</td><td>-0.3893</td></tr><tr><td>Au_{147}</td><td>E_{lh-reg}-E_{Dh}</td><td>1.8649</td><td>2.22</td><td>2.07</td><td>1.66</td><td>0.1919</td></tr><tr><td>Au_{201}</td><td>E_{Dh}-E_{fcc}</td><td>0.0524</td><td>0.237</td><td>1.01</td><td>0.798</td><td>0.7491</td></tr><tr><td>Au_{201}</td><td>E_{twin}-E_{fcc}</td><td>0.0677</td><td>0.575</td><td>-</td><td>-</td><td>0.3595</td></tr></table>

of “Rosette” defects. DFT/PBE predicts Ih to have lower energy than Dh while Gupta potential, DFT/LDA, and DFT/PBEsol predict the opposite. When it comes to mix vs. Dh, Gupta potential disagrees with DFT calculations which predict mix to have lower energy than Dh. However, it is interesting to note that the mix structure is indeed a Dh with local rearrangement of a few atoms near one of the reentrant grooves (see bottom of Fig. 9). Hence, we believe that Dh motif will dominate also at the DFT level, in agreement with Gupta results. Finally, for  \( Au_{201} \) , both Gupta potential and DFT predict the same energetic ordering:  \( E_{twin} > E_{Dh} > E_{fcc} \) . However, Gupta potential has lower energy difference compared to DFT. As a result, we anticipate that the solid-solid
 
![](./images/898633096998420845_16.jpg)

FIG. 9. Au structures used for DFT calculations.

transformation from fcc → Dh will be delayed to occur at higher temperature than predicted by Gupta potential.

Overall, we observe the following trends. At the size 147, Gupta potential performs fairly well, the more so for  \( Cu_{147} \)  and  \( Ag_{147} \)  which exhibit excellent quantitative agreement between Gupta potential and DFT. In the case of  \( Au_{147} \) , Gupta potential does a good job. Firstly, it predicts that defective icosahedra are preferred with surface “rosettes”. Secondly, Ih has higher energy than Dh and mix according to both Gupta and DFT. The only difference is mix, which is a distorted Dh with local rearrangement near the reentrant groove, is energetically preferred over Dh at the DFT level. At size 90, there is a qualitative agreement between Gupta potential and DFT for Cu, but not for Ag and Au. In the case of  \( Ag_{90} \) , twin is preferred at the DFT level, while Dh is preferred according to Gupta potential. In  \( Au_{90} \) , there is internal disagreement among DFT exchange-correlation functionals. However, given the very small energy difference (absolute values are about 0.1 eV or lower), we expect a similar competition between fcc and twin as observed with Gupta potential. Finally, at size 201, both Ag and Au exhibit a qualitative agreement with DFT (although they
 

underestimate the energy differences). In the case of  \( Cu_{201} \) , Ih is preferred at the DFT level as opposed to Dh according to Gupta potential.

Finally, in order to understand how the embedded atom method (EAM) pair potential model performs in comparison to Gupta potential, we calculated the energy differences using EAM potentials for  \( Cu,^{90} Ag,^{90} \)  and  \( Au.^{91} \)  The results are reported in the final column of Table II. In the case of Cu, Gupta and EAM exhibit similar performance. On the other hand, EAM seems to perform marginally better in the case of Ag. According to EAM,  \( Ag_{90} \)  predicts twin to have lower energy compared to mix and Dh similar to DFT. In the case of Au, EAM performs poorly in comparison to Gupta. The major drawback with EAM is that it predicts Ih to be the lowest energy structure for  \( Au_{147} \) .

Based on these results, we find that model potentials are still a good guide to select the main structural motifs and for discussing general trends between metals, but in some cases they fail to select the lowest-energy motifs in agreement with DFT. We note however that there is a case,  \( Au_{90} \) , where there is qualitative disagreement even between different types of DFT calculations. Moreover, in general there are quantitative discrepancies between the different exchange-correlation functionals, which would make it difficult to assign precise temperature-dependent isomer probabilities even at the DFT level.

## IV. CONCLUSIONS

In this work, we have applied a computational framework that we proposed recently \( ^{19} \)  to study the size- and system-dependent structural distributions of Cu, Ag, and Au nanoclusters. In this method, we combine harmonic superposition approximation (HSA) and parallel tempering molecular dynamics (PTMD) in a complementary manner and calculate the structures of metal nanoclusters in the entire temperature range from 0 K to melting. We considered three cluster sizes – 90, 147, and 201 in the range 1 to 2 nm of which 147 and 201 are “magic” sizes.

To begin with, “magic” sizes are not necessarily “magic” in that the global minimum is not always the ideal geometrical motif at that size. Perfect icosahedron and truncated octahedron are the ideal geometries at the sizes 147 and 201, respectively. However, only in three out of six cases ( \( Cu_{147} \) ,  \( Ag_{147} \) , and  \( Au_{201} \) ) the global minimum corresponds to the ideal geometrical structure. The global minima of  \( Au_{147} \) ,  \( Cu_{201} \) , and  \( Ag_{201} \)  are all Marks decahedra. At size 90, all the three systems have a different global minimum: icosahedron for  \( Cu_{90} \) , decahedron for  \( Ag_{90} \) , and fcc for
 

 \( Au_{90} \) 

The structural changes in these systems can be categorised broadly into three groups: type-(i) global minimum is also the dominant motif at finite temperatures up to melting; type-(ii) solid-solid transformations lead to a completely different motif; type-(iii) solid-solid transitions lead to a co-existence of two or more motifs. The majority of the cases belong to the second and third groups, which include  \( Cu_{90} \) ,  \( Cu_{201} \) ,  \( Ag_{90} \) ,  \( Au_{90} \) , \( Au_{147} \) , and  \( Au_{201} \) .

Icosahedra are extremely dominant with almost 100% abundance in  \( Cu_{147} \)  and  \( Ag_{147} \)  right up to melting. Similarly, decahedra are the dominant motif in  \( Au_{201} \)  up to melting. In the cases of  \( Cu_{90} \)  and  \( Au_{90} \) , we find find significant proportion of mix structures close to melting. Although decahedra are dominant in  \( Cu_{201} \) , we find significant amount of icosahedra beyond 400 K. Finally, in  \( Au_{147} \) , the proportion of Dh decreases gradually and we find small amounts of twin, fcc, Ih and mix structures co-existing at higher temperatures.

In contrast,  \( Ag_{90} \)  and  \( Au_{201} \)  undergo solid-solid transformations.  \( Ag_{90} \)  exhibits a partial transformation  \( Dh \rightarrow Dh + twin + mix \)  between 100 K to 150 K. Beyond 150 K, the proportion of Dh, twin, and mix structures remains approximately constant up to 450 K indicating a co-existence of multiple motifs. In the case of  \( Au_{201} \) , fcc transforms to Dh below 200 K resulting in almost 100% Dh at room temperature which remains dominant up to melting. In both the instances, the solid-solid transformation occurs well below the room temperature (< 200 K). As a result, it is non-trivial to predict the finite-temperature structures from the global minimum alone.

We also observed system specific differences across the three metals. Cu has a stronger preference for icosahedral structures. This is evident from almost 100% abundance at the sizes 90 and 147. While, at size 201, a significant amount of icosahedra are observed above 400 K which peaks around 700 K with  \( \sim33\% \) . In the case of Ag, icosahedra are mainly observed at the “magic” size of 147 where they occur with almost 100% abundance. Au on the other hand disfavors icosahedra, with icosahedra observed mainly at the size 147 in small proportions beyond 400 K. Another interesting feature is the gradual change in the nature of “rosette” defects in icosahedra at the size 147 from Cu to Au. “Rosette” defects are completely absent in Cu, but appear at higher temperatures in Ag. However, typically, almost all the icosahedra in Au have “rosette” defects. In contrast to Cu and Ag, decahedra in Au have deeper reentrant grooves.

Finally, a comparison of the performance of Gupta potential with DFT reveals few limitations of interatomic pair potentials. We observe a good agreement between Gupta potential and DFT at the size 147. In other cases ( \( Cu_{90} \) ,  \( Ag_{90} \) , Ag \( _{201} \) , and  \( Au_{201} \) ), the energetic ordering of the con-
 

sidered motifs is same according to both Gupta potential and DFT, with Gupta energy differences being underestimated. In the case of  \( Au_{90} \) , Gupta potential agrees with DFT/LDA, DFT/PBEsol but not with DFT/PBE. Finally, Gupta potential fares poorly in the case of  \( Cu_{201} \)  since it predicts Dh to prevail over Ih. However, according to DFT, Ih should prevail over Dh. Notwithstanding these limitations, interatomic pair potentials remain indispensable since the wide exposure of the energy landscape of metal nanoclusters at the DFT level is simply not feasible. It is instructive to first obtain the structural distributions using interatomic pair potentials, e.g., Gupta as done in the current work, followed by DFT calculations to understand the limitations of the structural distributions. For instance, we observed that Gupta potential predicts a complete solid-solid transformation from fcc → Dh below room temperature for  \( Au_{201} \) . However, the energy difference between Dh and fcc is lower than predicted by DFT (0.0524 eV for Gupta potential vs. > 0.2 eV for DFT). Based on this information, it can be inferred that the transformation from fcc → Dh may occur at higher temperature than predicted by Gupta potential. A further check of another model potential, EAM, shows an overall performance of the same quality of the Gupta potential, with a better agreement with DFT for  \( Ag_{90} \)  and a poorer performance for Au clusters.

Our method can be easily applied to any size and system for which reasonable models for atomic interactions are available. As a result, this method enables one to estimate the equilibrium proportion of various geometrical motifs as a function of temperature which can then be used to compare with the experimentally obtained structural distribution. \( ^{67-69} \)  This allows one to verify if the experimentally observed structures are in equilibrium or kinetically trapped metastable structures.

## SUPPLEMENTARY MATERIAL

Supplementary material contains Parameters of HSA, PTMD; Structural distribution of Au nanoclusters.

## ACKNOWLEDGMENTS

This work has been supported by the project “Understanding and Tuning FRiction through nanOstructure Manipulation (UTFROM)” funded by MIUR Progetti di Ricerca di Rilevante Interesse Nazionale (PRIN) Bando 2017 - grant 20178PZCB5. M.S. and A.G. acknowledge finan-
 

cial support from MIUR "Framework per l'Attrazione e il Rafforzamento delle Eccellenze per la Ricerca in Italia (FARE)" scheme, grant SERENA n. R18XYKRW7J. R.F. acknowledges the Progetto di Eccellenza of the Physics Department of the University of Genoa for financial and the International Research Network Nanoalloys of CNRS for networking support. The authors acknowledge PRACE for awarding us access to Marconi100 at CINECA, Italy.

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## AUTHOR DECLARATIONS

The authors have no conflicts to disclose.

## REFERENCES

 \( ^{1} \) F. Baletto and R. Ferrando, Rev. Mod. Phys. 77, 371 (2005).

 \( ^{2} \) F. Baletto, R. Ferrando, A. Fortunelli, F. Montalenti, and C. Mottet, J. Chem. Phys. 116, 3856 (2002).

 \( ^{3} \) J. M. Rahm and P. Erhart, Nano Lett. 17, 5775 (2017).

 \( ^{4} \) D. Nelli, C. Roncaglia, and C. Minnai, Advances in Physics: X 8, 2127330 (2023).

 \( ^{5} \) K. Michaelian, N. Rendon, and I. L. Garzon, Phys. Rev. B 60, 2000 (1999).

 \( ^{6} \) V. G. Grigoryan, D. Alamanova, and M. Springborg, Eur. Phys. J. D 34, 187 (2005).

 \( ^{7} \) X. Shao, X. Liu, and W. Cai, J. Chem. Theory Comput. 1, 762 (2005).

 \( ^{8} \) E. Apra, R. Ferrando, and A. Fortunelli, Phys. Rev. B 73, 205414 (2006).

 \( ^{9} \) V. G. Grigoryan, D. Alamanova, and M. Springborg, Phys. Rev. B 73, 115415 (2006).

 \( ^{10} \) X. Yang, W. Cai, and X. Shao, J. Phys. Chem. A 111, 5048 (2007).

 \( ^{11} \) D. Alamanova, V. G. Grigoryan, and M. Springborg, J. Phys. Chem. C 111, 12577 (2007).

 \( ^{12} \) A. M. Angulo and C. Noguez, J. Phys. Chem. A 112, 5834 (2008).

 \( ^{13} \) M. Itoh, V. Kumar, T. Adschiri, and Y. Kawazoe, J. Chem. Phys. 131, 174510 (2009).

 \( ^{14} \) K. Bao, S. Goedecker, K. Koga, F. Lançon, and A. Neelov, Phys. Rev. B 79, 041405(R) (2009).

 \( ^{15} \) W. Huang, X. Lai, and R. Xu, Chem. Phys. Lett. 507, 199 (2011).
 

 \( ^{16} \) M. Chen, J. E. Dyer, K. Li, and D. A. Dixon, J. Phys. Chem. A 117, 8298 (2013).

 \( ^{17} \) V. G. Grigoryan, M. Springborg, H. Minassian, and A. Melikyan, Comput. Theor. Chem. 1021, 197 (2013).

 \( ^{18} \) D. Schebarchov, F. Baletto, and D. J. Wales, Nanoscale 10, 2004 (2018).

 \( ^{19} \) M. Settem, R. Ferrando, and A. Giacomello, Nanoscale 14, 939 (2022).

 \( ^{20} \) G. Franke, E. R. Hilf, and P. Borrmann, J. Chem. Phys. 98, 3496 (1993).

 \( ^{21} \) F. Calvo, J. P. K. Doye, and D. J. Wales, Chem. Phys. Lett. 366, 176 (2002).

 \( ^{22} \) J. P. K. Doye and F. Calvo, Phys. Rev. Lett. 86, 3570 (2001).

 \( ^{23} \) J. P. K. Doye and F. Calvo, J. Chem. Phys. 116, 8307 (2002).

 \( ^{24} \) V. A. Mandelshtam and P. A. Frantsuzov, J. Chem. Phys. 124, 204511 (2006).

 \( ^{25} \) V. A. Sharapov and V. A. Mandelshtam, J. Phys. Chem. A 111, 10284 (2007).

 \( ^{26} \) V. G. Grigoryan and M. Springborg, Phys. Chem. Chem. Phys. 21, 5646 (2019).

 \( ^{27} \) E. Panizon and R. Ferrando, Phys. Rev. B 92, 205417 (2015).

 \( ^{28} \) D. Bonventre, E. Panizon, and R. Ferrando, Part. Syst. Charact. 35, 1700425 (2018).

 \( ^{29} \) D. J. Earl and M. W. Deem, Phys. Chem. Chem. Phys. 7, 3910 (2005).

 \( ^{30} \) J. P. Neirotti, F. Calvo, D. L. Freeman, and J. D. Doll, J. Chem. Phys. 112, 10340 (2000).

 \( ^{31} \) F. Calvo, J. P. Neirotti, D. L. Freeman, and J. D. Doll, J. Chem. Phys. 112, 10350 (2000).

 \( ^{32} \) A. J. Ballard and D. J. Wales, J. Chem. Theory Comput. 10, 5599 (2014).

 \( ^{33} \) M. N. Guimarães, M. M. de Almeida, J. M. C. Marques, and F. V. Prudente, Phys. Chem. Chem. Phys. 22, 10882 (2020).

 \( ^{34} \) Q. Shu, Y. Yang, Y. Zhai, D. Y. Sun, H. J. Xiang, and X. G. Gong, Nanoscale 4, 6307 (2012).

 \( ^{35} \) N. Tarrat, M. Rapacioli, and F. Spiegelman, J. Chem. Phys. 148, 204308 (2018).

 \( ^{36} \) D. Nelli, C. Mottet, and R. Ferrando, Faraday Discuss. 242, 52 (2023).

 \( ^{37} \) D. Nelli, G. Rossi, Z. Wang, R. E. Palmer, and R. Ferrando, Nanoscale 12, 7688 (2020).

 \( ^{38} \) H. Li, L. Li, A. Pedersen, Y. Gao, N. Khetrapal, H. Jonsson, and X. C. Zeng, Nano Lett. 15, 682 (2015).

 \( ^{39} \) B. Zhao, R. Zhang, Z. Huang, and B. Wang, Appl. Catal. A: Gen. 546, 111 (2017).

 \( ^{40} \) M. Jørgensen and H. Grönbeck, Angew. Chem. Int. Ed. 57, 5086 (2018).

 \( ^{41} \) W. Rong, H. Zou, W. Zang, S. Xi, S. Wei, B. Long, J. Hu, Y. Ji, and L. Duan, Angew. Chem. Int. Ed. 60, 466 (2021).

 \( ^{42} \) K. Rossi, G. G. Asara, and F. Baletto, Phys. Chem. Chem. Phys. 21, 4888 (2019).

 \( ^{43} \) R. Cheula, M. Maestri, and G. Mpourmpakis, ACS Catal. 10, 6149 (2020).
 

 \( ^{44} \) M. S. Daw and M. I. Baskes, Phys. Rev. B 29, 6443 (1984).

 \( ^{45} \) R. P. Gupta, Phys. Rev. B 23, 62 (1981).

 \( ^{46} \) A. P. Sutton and J. Chen, Philos. Mag. Lett. 61, 139 (1990).

 \( ^{47} \) P. Pyykko, Angew. Chem. Int. Ed. 43, 4412 (2004).

 \( ^{48} \) F. Furche, R. Ahlrichs, P. Weis, C. Jacob, S. Gilb, T. Bierweiler, and M. M. Kappes, J. Chem. Phys. 117, 6982 (2002).

 \( ^{49} \) H. Hakkinen, M. Moseler, and U. Landman, Phys. Rev. Lett. 89, 033401 (2002).

 \( ^{50} \) H. Hakkinen, B. Yoon, U. Landman, X. Li, H. Zhai, and L. Wang, J. Phys. Chem. A 107, 6168 (2003).

 \( ^{51} \) M. P. Johansson, D. Sundholm, and J. Vaara, Angew. Chem. Int. Ed. 43, 2678 (2004).

 \( ^{52} \) X. Gu, M. Ji, S. H. Wei, and X. G. Gong, Phys. Rev. B 70, 205401 (2004).

 \( ^{53} \) W. Fa and J. Dong, J. Chem. Phys. 124, 114310 (2006).

 \( ^{54} \) X. Xing, B. Yoon, U. Landman, and J. H. Parks, Phys. Rev. B 74, 165423 (2006).

 \( ^{55} \) C. Mottet, G. Rossi, F. Baletto, and R. Ferrando, Phys. Rev. Lett. 95, 035501 (2005).

 \( ^{56} \) K. Rossi, L. Pavan, Y. Y. Soon, and F. Baletto, Eur. Phys. J. B 91, 33 (2018).

 \( ^{57} \) E. Apra, F. Baletto, R. Ferrando, and A. Fortunelli, Phys. Rev. Lett. 93, 065502 (2004).

 \( ^{58} \) D. Nelli, Eur. Phys. J. Appl. Phys. 97, 18 (2022).

 \( ^{59} \) B. Yin and Z. Luo, Coord. Chem. Rev. 429, 213643 (2021).

 \( ^{60} \) A. Roldán, F. Viñes, F. Illas, J. M. Ricart, and K. M. Neyman, Theor. Chem. Acc. 120, 565 (2008).

 \( ^{61} \) F. D. Kiss, R. Miotto, and A. C. Ferraz, Nanotechnology 22, 275708 (2011).

 \( ^{62} \) L. F. L. Oliveira, N. Tarrat, J. Cuny, J. Morillo, and D. Lemoine, J. Phys. Chem. A 120, 8469 (2016).

 \( ^{63} \) C. Langlois, D. Alloyeau, Y. Bouar, A. Loiseau, T. Oikawa, C. Mottet, and C. Ricolleau, Faraday Discuss. 138, 375 (2008).

 \( ^{64} \) A. Volk, P. Thaler, M. Koch, E. Fisslthaler, W. Grogger, and W. E. Ernst, J. Chem. Phys. 138, 214312 (2013).

 \( ^{65} \) F. Baletto, C. Mottet, and R. Ferrando, Phys. Rev. B 63, 155408 (2001).

 \( ^{66} \) E. y. El koraychy, C. Roncaglia, D. Nelli, M. Cerbelaud, and R. Ferrando, Nanoscale Horiz. 7, 883 (2022).

 \( ^{67} \) D. Loffreda, D. M. Foster, R. E. Palmer, and N. Tarrat, J. Phys. Chem. Lett. 12, 3705 (2021).

 \( ^{68} \) D. M. Wells, G. Rossi, R. Ferrando, and R. E. Palmer, Nanoscale 7, 6498 (2015).
 

 \( ^{69} \) D. M. Foster, R. Ferrando, and R. E. Palmer, Nat. Commun. 9, 1323 (2018).

 \( ^{70} \) J. Palomares-Baez, E. Panizon, and R. Ferrando, Nano Lett. 17, 5394 (2017).

 \( ^{71} \) F. Cyrot-Lackmann and F. Ducastelle, Phys. Rev. B: Condens. Matter Mater. Phys. 4, 2406 (1971).

 \( ^{72} \) V. Rosato, M. Guillope, and B. Legrand, Philos. Mag. A 59, 321 (1989).

 \( ^{73} \) Y. Han, R. Ferrando, and Z. Y. Li, J. Phys. Chem. Lett. 5, 131 (2014).

 \( ^{74} \) D. Bochicchio and R. Ferrando, Nano Lett. 10, 4211 (2010).

 \( ^{75} \) E. Panizon, D. Bochicchio, G. Rossi, and R. Ferrando, Chem. Mater. 26, 3354 (2014).

 \( ^{76} \) P. Giannozzia, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, J. Phys.: Condens. Matter 21, 395502 (2009).

 \( ^{77} \) G. Kresse and J. Furthmüller, Comput. Mat. Sci. 6, 15 (1996).

 \( ^{78} \) J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

 \( ^{79} \) G. Rossi and R. Ferrando, J. Phys.: Condens. Matter 21, 084208 (2009).

 \( ^{80} \) S. Plimpton, J. Comp. Phys. 117, 1 (1995).

 \( ^{81} \) D. Faken and H. Jonsson, Comput. Mater. Sci. 2, 279 (1994).

 \( ^{82} \) C. Roncaglia, D. Rapetti, and R. Ferrando, Phys. Chem. Chem. Phys. 23, 23325 (2021).

 \( ^{83} \) M. Settem, J. Alloys Compd. 844, 155816 (2020).

 \( ^{84} \) G. Rossi and R. Ferrando, Nanotechnology 18, 225706 (2007).

 \( ^{85} \) O. Kostko, N. Morgner, M. A. Hoffmann, and B. von Issendorf, Eur. Phys. J. D 34, 133 (2005).

 \( ^{86} \) O. Kostko, Photoelectron spectroscopy of mass-selected sodium, coinage metal and divalent metal cluster anions, Ph.D. thesis, Albert-Ludwigs-Universität Freiburg (2007).

 \( ^{87} \) O. Kostko, B. Huber, M. Moseler, and B. von Issendorff, Phys. Rev. Lett. 98, 043401 (2007).

 \( ^{88} \) W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

 \( ^{89} \) J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. 100, 136406 (2009).

 \( ^{90} \) P. L. Williams, Y. Mishin, and J. C. Hamilton, Modelling Simul. Mater. Sci. Eng. 14, 817 (2006).

 \( ^{91} \) G. Grochola, S. P. Russo, and I. K. Snook, J. Chem. Phys. 123, 204719 (2005).
 

## SUPPLEMENTARY MATERIAL

![](./images/898633096998420845_17.jpg)

Fig. S 1. Comparison of  \( \Delta E \) , energy difference between cuboctahedron (CO) and icosahedron (Ih) for Ag clusters consisting of 55, 147, 309, and 561 atoms calculated using Gupta potential and density functional tight binding (DFTB) calculations. The values corresponding to DFTB are taken from ref. 62 of the main manuscript.

## Parameters of HSA and PTMD

For the HSA analysis, local minima were selected by applying an energy cutoff ( \( E_{cutoff} \) ) which was adjusted to have roughly 10000 configurations. This resulted in  \( E_{cutoff} \)  values in the range 1.0 eV to 1.5 eV. However, in the case of  \( Cu_{147} \)  and  \( Ag_{147} \) , Ih spans the entire temperature range. Even a high  \( E_{cutoff} \)  of 2.5 eV results in  \( \sim 1700 \) ,  \( \sim 3000 \)  local minima for  \( Cu_{147} \) ,  \( Ag_{147} \)  respectively. The number of local minima used per each motif and the energy cutoffs of Cu, Ag, and Au are provided in the Tables S1, S2, and S3 respectively. PTMD parameters (# of replicas and temperature of replicas) are provided in the Table S4.
 

Table S 1. Number of local minima used for HSA analysis of Cu nanoclusters. At each size, the minima were collected up to an energy ( \( E_{cutoff} \) ) above the global minimum.  \( E_{cutoff } \)  values at the sizes 90, 147, and 201 are 1.2 eV, 2.5 eV, and 1.5 eV respectively.

<table><tr><td rowspan="2">Structure</td><td colspan="3">Size</td></tr><tr><td>90</td><td>147</td><td>201</td></tr><tr><td>amorphous</td><td>22</td><td>-</td><td>-</td></tr><tr><td>fcc</td><td>14</td><td>1</td><td>2</td></tr><tr><td>twin</td><td>2077</td><td>42</td><td>1339</td></tr><tr><td>Ih</td><td>1825</td><td>1629</td><td>2689</td></tr><tr><td>Dh</td><td>1639</td><td>89</td><td>7174</td></tr><tr><td>mix</td><td>5543</td><td>2</td><td>-</td></tr><tr><td>all</td><td>11120</td><td>1763</td><td>11204</td></tr></table>

Table S 2. Number of local minima used for HSA analysis of Ag nanoclusters. At each size, the minima were collected up to an energy ( \( E_{cutoff} \) ) above the global minimum.  \( E_{cutoff } \)  values at the sizes 90, 147, and 201 are 1.0 eV, 2.5 eV, and 1.5 eV respectively.

<table><tr><td rowspan="2">Structure</td><td colspan="3">Size</td></tr><tr><td>90</td><td>147</td><td>201</td></tr><tr><td>amorphous</td><td>-</td><td>-</td><td>\( - \)</td></tr><tr><td>fcc</td><td>117</td><td>-</td><td>32</td></tr><tr><td>twin</td><td>2724</td><td>98</td><td>891</td></tr><tr><td>Ih</td><td>854</td><td>2435</td><td>\( - \)</td></tr><tr><td>Dh</td><td>2882</td><td>444</td><td>8956</td></tr><tr><td>mix</td><td>4019</td><td>53</td><td>\( - \)</td></tr><tr><td>all</td><td>10596</td><td>3030</td><td>9879</td></tr></table>
 

Table S 3. Number of local minima used for HSA analysis of Au nanoclusters. At each size, the minima were collected up to an energy ( \( E_{cutoff} \) ) above the global minimum.  \( E_{cutoff } \)  values at the sizes 90, 147, and 201 are 1.0 eV, 1.5 eV, and 1.0 eV respectively. These data are taken from \( ^{19} \) .

<table><tr><td rowspan="2">Structure</td><td colspan="3">Size</td></tr><tr><td>90</td><td>147</td><td>201</td></tr><tr><td>amorphous</td><td>69</td><td>-</td><td>-</td></tr><tr><td>fcc</td><td>316</td><td>1382</td><td>728</td></tr><tr><td>twin</td><td>3107</td><td>3651</td><td>1316</td></tr><tr><td>Ih</td><td>1</td><td>2444</td><td>-</td></tr><tr><td>Dh</td><td>994</td><td>8554</td><td>8583</td></tr><tr><td>mix</td><td>6632</td><td>1919</td><td>-</td></tr><tr><td>all</td><td>11119</td><td>17950</td><td>10627</td></tr></table>
 

Table S 4. # of replicas and replica temperatures used for PTMD simulations of Cu, Ag, and Au nanoclusters.

<table><tr><td>Metal cluster</td><td># replicas</td><td>Replica temperatures (K)</td></tr><tr><td>Cu90</td><td>37</td><td>300, 315, 331, 347, 365, 383, 402, 423, 444, 466, 490, 514, 540, 550, 558, 567, 575, 584, 592, 601, 609, 617, 626, 634, 643, 651, 659, 668, 676, 685, 693, 702, 710, 720, 746, 772, 800</td></tr><tr><td>Cu147</td><td>40</td><td>300, 310, 321, 332, 343, 355, 367, 379, 392, 405, 419, 433, 448, 463, 479, 495, 512, 530, 548, 566, 586, 605, 626, 647, 669, 692, 716, 740, 750, 758, 767, 775, 783, 792, 800, 810, 832, 854, 877, 900</td></tr><tr><td>Cu201</td><td>40</td><td>300, 311, 322, 333, 345, 357, 369, 382, 396, 410, 424, 439, 455, 471, 488, 505, 523, 541, 560, 580, 601, 622, 644, 666, 690, 700, 709, 718, 727, 736, 744, 753, 762, 771, 780, 790, 816, 843, 871, 900</td></tr><tr><td>Ag90</td><td>30</td><td>250, 264, 280, 296, 313, 331, 350, 370, 392, 414, 438, 463, 471, 479, 486, 493, 500, 507, 513, 520, 527, 533, 540, 547, 553, 560, 570, 596, 622, 650</td></tr><tr><td>Ag147</td><td>32</td><td>300, 313, 326, 339, 354, 369, 384, 400, 417, 435, 453, 472, 492, 513, 534, 557, 580, 605, 630, 640, 647, 654, 661, 669, 676, 683, 690, 700, 724, 748, 774, 800</td></tr><tr><td>Ag201</td><td>36</td><td>300, 312, 324, 337, 351, 365, 379, 394, 410, 426, 443, 461, 479, 498, 518, 539, 560, 583, 606, 630, 640, 646, 652, 658, 664, 670, 676, 682, 688, 694, 700, 710, 732, 754, 776, 800</td></tr><tr><td>Au90</td><td>36</td><td>250, 263, 275, 288, 300, 309, 319, 329, 339, 350, 357, 363, 370, 376, 383, 389, 396, 402, 409, 415, 422, 428, 435, 441, 448, 454, 461, 467, 474, 480, 487, 493, 500, 517, 533, 550</td></tr><tr><td>Au147</td><td>24</td><td>300, 314, 329, 345, 361, 378, 396, 415, 434, 455, 476, 482, 488, 493, 499, 505, 511, 516, 522, 528, 546, 564, 582, 600</td></tr><tr><td>Au201</td><td>32</td><td>300, 312, 324, 336, 349, 363, 377, 391, 406, 422, 438, 455, 473, 491, 510, 516, 521, 527, 533, 539, 544, 550, 556, 561, 567, 573, 579, 584, 590, 610, 630, 650</td></tr></table>
 

## Structural distribution of Au nanoclusters

In Fig. S2, we replot the structural distribution of  \( Au_{90} \) ,  \( Au_{147} \) , and  \( Au_{201} \)  clusters using the data reported previously \( ^{19} \)  for the purpose of comparison with Cu and Ag clusters.

![](./images/898633096998420845_18.jpg)

![](./images/898633096998420845_19.jpg)

![](./images/898633096998420845_20.jpg)

![](./images/898633096998420845_21.jpg)

![](./images/898633096998420845_22.jpg)

![](./images/898633096998420845_23.jpg)

![](./images/898633096998420845_24.jpg)

![](./images/898633096998420845_25.jpg)

![](./images/898633096998420845_26.jpg)

Fig. S 2. Structural distribution of (a)  \( Au_{90} \) , (b)  \( Au_{147} \) , and (c)  \( Au_{201} \) . PTMD, HSA results are shown in the top and middle rows. Global minimum structures are shown in the bottom row. In the HSA results, for comparison, we report with vertical lines the range of PTMD temperatures and with a dashed line the fraction of amorphous structures calculated from PTMD simulations.
 
