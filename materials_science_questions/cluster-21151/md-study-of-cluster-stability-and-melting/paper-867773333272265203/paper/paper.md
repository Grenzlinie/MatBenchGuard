
# The effect of compression on the global optimization of atomic clusters

Jonathan P. K. Doye

University Chemical Laboratory, Lensfield Road, Cambridge CB2 1EW, UK
(October 24, 2018)

Recently, Locatelli and Schoen proposed a transformation of the potential energy that aids the global optimization of Lennard-Jones clusters with non-icosahedral global minima. These cases are particularly difficult to optimize because the potential energy surface has a double funnel topography with the global minimum at the bottom of the narrower funnel. Here we analyse the effect of this type of transformation on the topography of the potential energy surface. The transformation, which physically corresponds to a compression of the cluster, firstly reduces the number of stationary points on the potential energy surface. Secondly, we show that for a 38-atom cluster with a face-centred-cubic global minimum the transformation causes the potential energy surface to become increasingly dominated by the funnel associated with the global minimum. The transformation has been incorporated in the basin-hopping algorithm using a two-phase approach.

## I. INTRODUCTION

One of the most important types of global optimization problem, and one which is particularly of interest to chemical physicists, is the determination of the lowest energy configuration of a molecular system, such as a protein, a crystal or a cluster. \( ^{1} \)  However, such a task can be very difficult because of the large number of minima that a potential energy surface (PES) can have—it is generally expected that the number of minima of a system will increase exponentially with size. \( ^{2} \)  Therefore, if applications to large systems with realistic descriptions of the interatomic interactions are to be feasible, it is necessary that efficient global optimization algorithms, which scale well with system size, are developed.

A key part of this development is understanding when and why an algorithm is likely to succeed or fail, because, as well as providing useful information about the limitations of an algorithm, this physical insight might be utilised in the design of better algorithms. This is the motivation behind the current paper. Here, we analyse the reasons for the success of a recent algorithm when applied to the global optimization of Lennard-Jones (LJ) clusters for some particularly difficult sizes.

The global optimization of LJ clusters has probably become the most common benchmark for configurational optimization problems. \( ^{1,3} \)  Putative global minima have been obtained for all sizes up to 309 atoms, \( ^{4-17} \)  and up-to-date databases of these structures are maintained on the web. \( ^{18,19} \)  There are two types of difficulty for the LJ cluster problem. First, there is the general increase in the number of minima with cluster size. \( ^{20,21} \)  Second, on top of this effect there are size-specific effects related to the topography of the PES. \( ^{22} \) 

For most of the clusters the topography of the PES aids global optimization. There is a funnel \( ^{23,24} \)  from the high-energy liquid-like clusters to the low energy minima with structures based up on the Mackay \( ^{25} \)  icosahedra. When there is a dominant low-energy icosahedral minimum at the bottom of the funnel, such as when complete Mackay icosahedra can be formed, global optimization is particularly easy.

However, there are some sizes for which the global minimum is not icosahedral. At N=38 the global minimum is a face-centred-cubic (fcc) truncated octahedron \( ^{8-10} \)  (38A in Figure 1), at N=75-77 and 102–104 the global minima are based on Marks \( ^{26} \)  decahedra \( ^{10,11} \)  (e.g. 75A in Figure 1), and at N=98 the global minimum is a Leary tetrahedron \( ^{17} \)  (98A in Figure 1). For these sizes the PES has a fundamentally different character. As well as the wide funnel leading down to the low-energy icosahedral structures, there is a much narrower funnel which leads down to the global minimum. \( ^{22,27} \)  Relaxation down the PES is much more likely to take the system into the wider funnel where it is then trapped. The time scale for interfunnel equilibration is very slow \( ^{28} \)  because of the large energy \( ^{22} \)  and free energy \( ^{27} \)  barriers between the two funnels.

![](./images/867773333272265203_1.jpg)

FIG. 1. The global minima and some low-lying minima of  \( LJ_{34} \) ,  \( LJ_{38} \) ,  \( LJ_{75} \)  and  \( LJ_{98} \) . 34A, 38C, 75C and 98B are based on Mackay icosahedra. 34H and 98A are Leary tetrahedra. 38A is a face-centred-cubic truncated octahedron, and 75A is a Marks decahedron. The letter gives the energetic rank of the minimum, i.e. global minima are labelled with an ‘A’, etc.

As a result these eight clusters are hard to optimize, the larger examples being virtually impossible to optimize by traditional approaches, such as simulated annealing. However, these cases are solvable by a set
 

of methods in which the 'basin-hopping' transformation is applied to the PES. \( ^{13} \)  This transformation is used by the Monte Carlo minimization \( ^{29} \)  or basin-hopping algorithm, \( ^{13} \)  and implicitly by all the most successful genetic algorithms. \( ^{12,30-36} \)  The transformation of the PES works by changing the thermodynamics of the clusters such that the system is now able to pass between the funnels more easily. \( ^{37,38} \)  However, the non-icosahedral global minima still take much longer to find than the icosahedral global minima, \( ^{1} \)  and there is no way of knowing if one has waited long enough to rule out the possibility of a non-icosahedral global minimum. This is illustrated by the Leary tetrahedron at N=98. Despite the fact that powerful optimization techniques had been applied to  \( LJ_{98} \) , \( ^{13,35,36} \)  the global minimum was discovered only very recently. \( ^{17} \)  Subsequently, it was confirmed that this minimum could be found by some of the previously applied methods. \( ^{39,40} \) 

Given this background, it would be useful to develop techniques that are more efficient for these double-funnel examples. Two potential approaches have very recently been put forward. First, Hartke has achieved improvements in the genetic algorithm approach by forcing the system to maintain a diversity of structural types in the population, thus preventing the population becoming concentrated in the icosahedral funnel. \( ^{36} \)  Second, Schoen and Locatelli noted that the exceptions to the icosahedral structural motifs are usually more spherical than the competing icosahedral structures. This is because the exceptions generally occur at sizes where both a particularly stable form for the alternative morphology is possible and the icosahedral structures involve an incomplete overlayer. Therefore, Schoen and Locatelli added a term to the potential energy favouring compact clusters. Using this PES transformation, the non-icosahedral global minima at N=38, 98,102–104 were much more likely to be found by their multi-start minimization algorithm. \( ^{41} \)  An additional transformation had to be applied in order to find the global minima at N=75–77.

It is the reasons for the success of this second approach that we examine in this paper. In particular we show how Schoen and Locatelli’s transformation affects the topography of the PES. We also show how the transformation can be incorporated as an element of an existing algorithm, namely basin-hopping.

## II. METHODS

The atoms in the clusters interact via the Lennard-Jones potential: \( ^{42} \) 

 \[ E_{\mathrm{LJ}}=4\epsilon\sum_{i<j}\left[\left(\frac{\sigma}{r_{ij}}\right)^{12}-\left(\frac{\sigma }{r_{ij}}\right)^6\right], \quad (1) \] 

where  \( \epsilon \)  is the pair well depth and  \( 2^{1/6}\sigma \)  is the equilibrium pair separation. To this, Schoen and Locatelli added a term proportional to  \( \sum_{i<j}r_{ij} \)  which penalizes long pair distances. \( ^{41} \)  Here, we use a slightly different form, which again acts to compress the cluster. The energy for such a compressed Lennard-Jones (CLJ) cluster is given by

 \[ E_{\mathrm{C L J}}=E_{\mathrm{L J}}+\sum_{i}\mu_{\mathrm{c o m p}}\frac{\left|\mathbf{r}_{i}-\mathbf{r}_{\mathrm{c.o.m.}}\right|^{2}}{\sigma^{2}}, \quad (2) \] 

where  \( \mu_{comp} \)  is a parameter that determines the magnitude of the compression acting on the cluster, and  \( r_{c.o.m} \)  is the position of the centre of mass of the cluster. We found the additional term to be approximately proportional to Schoen and Locatelli's expression, and so the effect of the two transformations on the PES topography are virtually identical.

To map the PES topography of these CLJ clusters we use the same methods as those we have applied to  \( LJ^{22,27} \)  and Morse \( ^{43} \)  clusters to obtain large samples of connected minima and transition states that provide good representations of the low-energy regions of the PES. The approach involves repeated applications of eigenvector-following \( ^{44} \)  to find new transition states and the minima they connect.

In the basin-hopping algorithm, \( ^{13,45} \)  the transformed potential energy is given by

 \[ \tilde{E}(\mathbf{x})=\operatorname*{m i n}\left\{E(\mathbf{x})\right\}, \quad (3) \] 

where x represents the vector of nuclear coordinates and min signifies that an energy minimization is performed starting from x. Hence the energy at any point in configuration space is assigned to that of the local minimum obtained by the minimization, and the transformed PES consists of a set of plateaus or steps each corresponding to the basin of attraction surrounding a minimum on the original PES. This PES is then searched by constant temperature Monte Carlo. Additionally, the algorithm has been found to be more efficient for clusters if the configuration is reset to that of the new local minimum at each accepted step. \( ^{46} \) 

There are two ways that one might incorporate a further PES transformation into this algorithm. One could use basin-hopping to first find the global minimum of the transformed PES, then reoptimize the  \( n_{low} \)  lowest energy minima under the original potential. However, if the global minimum of the original PES is not among the  \( n_{low} \)  lowest energy minima of the transformed PES this approach is bound to fail.

Alternatively, at each step one could first optimize a new configuration using the transformed potential, then reoptimize the resulting minimum using the original potential. By incorporating this second minimization the shortcomings of the first approach are avoided. Furthermore, if the energy of this final minimum is used in the Metropolis acceptance criterion, the Boltzmann weight of each minimum is unchanged. However, the occupation probability of a particular minimum will be proportional the area of the basin of attraction of the minimum on the transformed rather than the original PES, i.e.
 

 \[ p_{i}\propto n_{i}\tilde{A}_{i}\exp(-\beta E_{i}), \quad (4) \] 

where  \( n_{i} \)  is the number of permutational isomers of i and  \( \tilde{A}_{i} \)  is the total area of the basins of attraction of the minima on  \( \tilde{E} \)  which when reoptimized on E lead to minimum i. Therefore, if the relative area of the global minimum is larger on the transformed PES, optimization should be easier using this approach. We refer to this version of the basin-hopping algorithm as two-phase basin hopping. This variation is not much more computationally demanding than standard basin-hopping because the starting point for the second minimization is likely to be close to a minimum of the untransformed PES.

There is one further difference from previous implementations of the basin-hopping algorithm. Previously, we had performed the minimization in Equation (3) by conjugate gradient. \( ^{47} \)  However, we have since found a limited memory BFGS algorithm that is more efficient. \( ^{48} \) 

## III. RESULTS

In global optimization the aim of transforming the potential energy surface is to make the global minimum easier to locate. Typically, one therefore wants the transformation to reduce the number of minima and the barriers between them. Furthermore, if the transformation is to change the relative energies of the minima, one wants the energetic bias towards the global minimum to increase.

As the number of minima and transition states on the  \( CLJ_{13} \)  PES is small enough that virtually all can be found, we can examine whether the compressive term has the first of the above effects by examining  \( CLJ_{13} \)  as a function of  \( \mu_{comp} \) . The number of minima and transition states clearly decreases as  \( \mu_{comp} \)  increases (Table I). It is interesting to note that minima with low symmetry preferentially disappear. The PES transformation places the cluster in a harmonic potential about its centre of mass. This potential plays a role similar to a soft spherical box, and so less compact minima disappear from the PES as  \( \mu_{comp} \)  increases. Similar results are found when periodic boundary conditions are applied—the number of minima is much less than for a LJ cluster of equivalent size and the number of minima decreases as the pressure in the cell is increased. \( ^{49,50} \) 

It is also worth noting that the magnitude of the downhill barriers relative to the energy difference between the minima decreases as  \( \mu_{comp} \)  increases (Table I). In the terminology used by Berry and coworkers, \( ^{51} \)  the profiles of the pathways to the global minimum become more staircase-like and less sawtooth-like with increasing  \( \mu_{comp} \) . The combination of the changes to the number of stationary points and the barrier heights act to make relaxation to the icosahedral global minimum easier as the PES is further transformed.

Next, we examine the  \( CLJ_{38} \)  cluster. For a cluster of this size it is not feasible to obtain a complete representation of the PES in terms of stationary points, so instead we obtain a good representation of the lower energy regions of the PES. At each value of  \( \mu_{comp} \)  we obtained a sample of 6000 minima. The effect of  \( \mu_{comp} \)  on the number of stationary points, which we noted for  \( CLJ_{13} \) , is again evident (Table II). As  \( \mu_{comp} \)  increases,  \( n_{search} \) , the number of minima from which we have to perform transition state searches in order to generate the 6000 minima, increases and it becomes more likely that a new transition state does not connect to a new minimum, but rather to one already in our sample.

![](./images/867773333272265203_2.jpg)

FIG. 2.  \( Q_{comp} \)  for the  \( LJ_{N} \)  global minima. To make the size-dependence more clear the zero is taken to be the function,  \( Q_{ave} \) , a four parameter fit to the  \( Q_{comp} \)  values.  \( Q_{ave} = 25.915N - 166.956N^{2/3} + 382.765N^{1/3} - 293.972 \) . Also included in the figure are isolated data points (crosses) corresponding to the non-global minima illustrated in Figure 1 and the second lowest energy minima for N=76, 77 and 102–104.

The second desired effect of a PES transformation is to change the energetics in a manner that makes the global minimum more favourable. We can get a simple guide as to how the energies of the minima depend on  \( \mu_{comp} \)  if we assume there is no structural relaxation in response to changing  \( \mu_{comp} \) . Then  \( E_{CLJ} = E_{LJ} + \mu_{comp}Q_{comp} \)  where the order parameter,  \( Q_{comp} = \sum_{i} |r_{i} - r_{c.o.m.}|^{2}/\sigma^{2} \) , is evaluated at  \( \mu_{comp} = 0 \) . From the values of  \( Q_{comp} \)  we can predict the changes in the relative energies of any two minima.

 \( Q_{comp} \)  is a measure of the compactness of the cluster, and from Figure 2 one can see how the compactness of the global minima depends on size. For the first two shells the icosahedral global minima are most compact when complete Mackay icosahedra can be formed, e.g. N=13 and 55. However, for the third shell the most compact icosahedral structure is at N=135, where twelve vertex atoms of the Mackay icosahedron are missing, rather than at N=147.

If we examine  \( LJ_{38} \)  as an example of a cluster with a non-icosahedral global minimum, we see that this size corresponds to a pronounced minimum in Figure 2—the truncated octahedron is particularly compact compared
 

to the other global minima of similar size. Furthermore, from Figure 3b we can see that the  \( LJ_{38} \)  global minimum has the lowest value of  \( Q_{comp} \)  of all the  \( LJ_{38} \)  minima. Therefore, the energy gap between the global minimum and the lowest-energy icosahedral minimum increases with  \( \mu_{comp} \)  (Table II). To visualize how this deepening of the fcc funnel changes the PES topography we present disconnectivity graphs of  \( CLJ_{38} \)  for a range of  \( \mu_{comp} \)  values in Figure 4.

Disconnectivity graphs provide a representation of the barriers between minima on a PES. \( ^{52,53} \)  In a disconnectivity graph, each line ends at the energy of a minimum. At a series of equally-spaced energy levels we compute which (sets of) minima are connected by paths that never exceed that energy. We then join up the lines in the disconnectivity graph at the energy level where the corresponding (sets of) minima first become connected. In a disconnectivity graph an ideal single-funnel PES would be represented by a single dominant stem associated with the global minimum to which the other minima directly join. For a multiple-funnel PES there would be a number of major stems which only join at high energy.

From the disconnectivity graph of  \( LJ_{38} \)  one can deduce that the cluster has a double-funnel PES (Figure 4a). There is a narrow funnel associated with the global minimum, and a wider funnel associated with the icosahedral minima. There are a number of low-energy minima at the bottom of the icosahedral funnel, which, although they have only small differences in the way the outer layer is arranged (e.g. the second lowest icosahedral minimum, 38C, is depicted in Figure 1), can be separated by moderate-sized barriers. As a result there is a certain amount of fine structure at the bottom of the icosahedral funnel with not all minima joined directly to the stem of the lowest-energy icosahedral minimum. From the data in Table II one can see that there are many more minima associated with the icosahedral funnel.

![](./images/867773333272265203_3.jpg)

![](./images/867773333272265203_4.jpg)

![](./images/867773333272265203_5.jpg)

![](./images/867773333272265203_6.jpg)

FIG. 3. Scatter plots of  \( Q_{comp} \)  against minimum energy for large samples of minima for (a)  \( LJ_{34} \) , (a)  \( LJ_{38} \) , (a),  \( LJ_{75} \)  and (d)  \( LJ_{98} \) . The minima depicted in Figure 1 are labelled by the letter corresponding to their energetic rank. In (d) there are two subsets: diamonds correspond to minima found when the search was started from the tetrahedral global minimum and crosses correspond to the set when started from the lowest energy icosahedral minimum. There is no overlap between these two sets because no pathways connecting the two funnels were located. The patterns of points for  \( Q_{linear} = \sum_{i<j} r_{ij} / \sigma \)  are virtually identical to those of this figure, showing that the current transformation is effectively equivalent to Locatelli and Schoen's.
 
![](./images/867773333272265203_7.jpg)

![](./images/867773333272265203_8.jpg)

![](./images/867773333272265203_9.jpg)

![](./images/867773333272265203_10.jpg)

FIG. 4. Disconnectivity graphs of CLJ \( _{38} \)  for  \( \mu_{comp} = (a) \)  0 (b) 0.25 \( \epsilon \)  (c) 1.0 \( \epsilon \)  and (d) 5 \( \epsilon \) . In (a) the 150 lowest-energy minima are represented in the graph, and in (b)–(d) the 250 lowest-energy minima are represented. The icosahedral and fcc funnels are labelled. The units of energy on the vertical axis are  \( \epsilon \) .
 
![](./images/867773333272265203_11.jpg)

FIG. 5. Heat capacity curves for CLJ \( _{38} \)  with the values of  \( \mu_{comp}/\epsilon \) , as labelled. The curves were calculated from our samples of 6000 minima using the harmonic superposition method. \( ^{54,55} \) 

As the fcc funnel becomes deeper with increasing  \( \mu_{comp} \)  it increases in size relative to the icosahedral funnel (Figure 4). By  \( \mu_{comp}=5e \)  the fcc funnel dominates the PES, and the disconnectivity graph has the form expected for an ideal single funnel with only a very small sub-funnel for the icosahedral minima. These changes are also reflected in the number of minima associated with both funnels (Table II).

These changes to the PES topography of course affect the thermodynamics. For  \( LJ_{38} \)  there are two peaks in the heat capacity curve (Figure 5). The first is due to a transition from the fcc global minimum to the icosahedral minima, which is driven by the greater entropy of the latter. The second corresponds to melting. The first transition hinders global optimization because it is thermodynamically favourable for the cluster to enter the icosahedral funnel on cooling from the molten state, where it can then be trapped. \( ^{37,38} \)  However, as  \( \mu_{comp} \)  increases, the decreasing entropy of the icosahedral funnel can no longer overcome the increasing energy difference between the global minimum and the icosahedral funnel (Table II) and so this first transition is suppressed. Consequently, the heat capacity curves for the  \( CLJ_{38} \)  clusters in Figure 5 show only one peak, indicating that the global minimum is most stable up to melting.

Of course, the changes to the PES topography and thermodynamics mean that on relaxation down the PES the system is more likely to enter the fcc funnel as  \( \mu_{comp} \)  increases. Furthermore, the energy barrier to escape from the icosahedral funnel relative to the energy difference between the bottoms of the two funnels becomes smaller (Table II), thus making escape from the icosahedral funnel easier. To quantify these effects we performed annealing \( ^{56} \)  simulations for CLJ \( _{38} \)  at a number of values of  \( \mu_{comp} \)  (Table III). For LJ \( _{38} \)  80% of the longer annealing runs ended at the bottom of the icosahedral funnel, and only 2% at the global minimum. However, by  \( \mu_{comp}=5e \)  99.5% of the long annealing runs reached the global minimum.

Given the above, it is unsurprising that two-phase basin-hopping finds the global minimum more rapidly as  \( \mu_{comp} \)  increases (Figure 6b). At large  \( \mu_{comp} \)  the first-passage time is 40 times shorter than for LJ \( _{38} \) . Conversely, the first-passage time to reach the icosahedral minimum 38C increases. These changes are driven by changes to  \( \tilde{A}_{i} \)  in Equation (4). The basin of attraction of the global minimum increases in size relative to those of the icosahedral minima as the PES is further transformed.

![](./images/867773333272265203_12.jpg)

![](./images/867773333272265203_13.jpg)

FIG. 6. The  \( \mu_{comp} \) -dependence of the first-passage time (in MC steps) to find the specified minima of (a) LJ \( _{34} \)  and (a) LJ \(_{38} \)  from a random starting configuration in two-phase basin-hopping runs. Each point represents an average over 400 runs. The temperature used is  \( 1.0\epsilon k^{-1} \) .

Locatelli and Schoen’s transformation works for LJ \( _{38} \)  because the global minimum is the most compact spherical minimum. However, this does not necessarily have to be the case, even for those clusters with non-icosahedral global minima. From Figure 2 one can see that the non-icosahedral global minima at N=98 and 102–104 have particularly low values of  \( Q_{comp} \)  and Figure 3d confirms that the Leary tetrahedron, 98A, has the lowest  \( Q_{comp} \)  value of all the LJ \( _{98} \)  minima. Therefore, Locatelli and Schoen were able to locate these global minima. How-
 

ever, for N=75-77 the values of  \( Q_{comp} \)  for the Marks decahedra are not set apart from the nearby icosahedral global minima (Figure 2) and Figure 3c shows that there are a number of  \( LJ_{75} \)  minima which have lower values of  \( Q_{comp} \)  than 75A. In particular, the icosahedral minimum 75C that is third lowest in energy has a lower  \( Q_{comp} \) , and the Marks decahedron is no longer the  \( CLJ_{75} \)  global minimum beyond  \( \mu_{comp}=3.1\epsilon \) .

The geometric root of this behaviour is that the Marks decahedra at N=75-77 are the least spherical of the non-icosahedral global minima. The 75-atom Marks decahedron is somewhat oblate and some of the icosahedral minima with which 75A is competing are prolate by a similar degree, leading to comparable values of  \( Q_{comp} \) . Therefore, although the transformation may aid global optimization by reducing the number of minima and by increasing the energy of many minima relative to the Marks decahedron, unlike for  \( LJ_{38} \)  it does not remove the fundamental double-funnel character of the PES. To locate the global minimum Locatelli and Schoen had to add an additional ‘diameter penalization’ to the potential. \( ^{41} \) 

Locatelli and Schoen found that for many of the clusters their transformation did not aid global optimization. This was not unexpected, but simply reflects the fact that often the icosahedral global minima are not the most compact minima. We analyse one example. At N=34 it is possible to form a compact Leary tetrahedron (34H in Figure 1), which is the eighth lowest-energy  \( LJ_{34} \)  minimum. This structure has a significantly lower value of  \( Q_{comp} \)  than the global minimum (Figure 3a). As a result, the Leary tetrahedron becomes the  \( CLJ_{34} \)  global minimum at  \( \mu_{comp}=0.3\epsilon \) . The results of two-phase basin-hopping runs are similar to those for  \( LJ_{38} \)  in that as  \( \mu_{comp} \)  increases the compact non-icosahedral structure becomes significantly easier to locate and the low-energy icosahedral minima more difficult (Figure 6). The difference, though, is that now this scenario is undesirable, because it is the global minimum that is becoming more difficult to reach.

## IV. CONCLUSIONS

By analysing the effect of a compressive transformation on the PES topography we have obtained insights into the reasons for its success in aiding the optimization of LJ clusters that have non-icosahedral global minima. Firstly, we have shown that the transformation reduces the number of minima and transition states on the PES. Secondly, for examples where, as is often the case, the non-icosahedral global minimum is the most compact structure, the transformation causes the funnel of the global minimum to become increasingly dominant. For  \( LJ_{38} \)  the PES has a double funnel, whilst at large  \( \mu_{comp} \)  the PES has an ideal single-funnel topography, enabling the system to relax easily down the PES to the global minima. However, when as for  \( LJ_{75} \) , the decahedral global minimum is only one of the more compact minima, the transformation is less beneficial for global optimization. By contrast, for sizes with icosahedral global minima the transition is often unhelpful, as we saw for  \( LJ_{34} \) , because the global minimum is much less likely to be the most compact structure. Therefore, the transformation needs to be used in combination with other methods. As the transformation is most likely to be successful for clusters where other methods fail it can act as a good complement to them. For example, when the basin-hopping algorithm is applied, usually a series of runs are performed at each size. If one of the runs used the two-phase approach, this would increase the chance of success for those sizes where the PES had a multiple-funnel topography.

Other PES transformations could also be usefully employed alongside standard basin-hopping runs in this two-phase approach, if they are likely to aid global optimization for some sizes. For example, increasing the range of the potential is another transformation that reduces the number of stationary points on the PES. \( ^{43} \)  Using the transformations alongside standard runs avoids one of the major difficulties associated with PES transformations. They are rarely universally effective, but rather there are likely to be some instances when they destabilize the global minimum, thus making optimization more difficult. This is certainly the case when increasing the range of the potential, where the range-dependence of the most stable cluster structure is well-documented. \( ^{10,57} \) 

Although we have seen how a compressive transformation can be useful in aiding the global optimization of LJ clusters, an important question is how generally useful it will be. Although this question can only be definitively answered through applications to a variety of systems, one would expect it to be useful for metal and simple molecular clusters that form compact structures, particularly those that favour 12-coordination. For these systems, as with LJ clusters, the strength of this approach would be locating those global minima that are not based on the dominant morphology, because the alternative morphologies are only likely to be most stable when they are compact and sherical. It might also be useful in systems such as proteins where there are a large number of less compact unfolded configurations. However, it would not be useful for clusters of substances, such as water and silicon, which form open network structures where the liquid can be denser than the solid.

## ACKNOWLEDGMENTS

J.P.K.D. is the Sir Alan Wilson Research Fellow at Emmanuel College, Cambridge. The author is grateful to David Wales for supplying a modified version of the basin-hopping code, and would also like to thank Marco Locatelli and Fabio Schoen for helpful discussions and for sharing results prior to publication.
 

 \( ^{1} \)  D. J. Wales and H. A. Scheraga, Science 285, 1368 (1999).

 \( ^{2} \)  F. H. Stillinger, Phys. Rev. E 59, 48 (1999).

 \( ^{3} \)  L. T. Wille, in Annual Reviews of Computational Physics VII, edited by D. Stauffer (World Scientific, Singapore, 2000).

 \( ^{4} \)  L. T. Wille, Chem. Phys. Lett. 133, 405 (1987).

 \( ^{5} \)  J. A. Northby, J. Chem. Phys. 87, 6166 (1987).

 \( ^{6} \)  T. Coleman and D. Shalloway, J. Global Optimization 4, 171 (1994).

 \( ^{7} \)  G. L. Xue, J.Global Optimization 4, 425 (1994).

 \( ^{8} \)  S. Gomez and D. Romero, Proceedings of the First European Congress of Mathematics (Birkhauser, Basel, 1994), Vol. III, pp. 503–509.

 \( ^{9} \)  J. Pillardy and L. Piela, J. Phys. Chem. 99, 11805 (1995).

 \( ^{10} \)  J. P. K. Doye, D. J. Wales, and R. S. Berry, J. Chem. Phys. 103, 4234 (1995).

 \( ^{11} \)  J. P. K. Doye and D. J. Wales, Chem. Phys. Lett. 247, 339 (1995).

 \( ^{12} \)  D. M. Deaven, N. Tit, J. R. Morris, and K. M. Ho, Chem. Phys. Lett. 256, 195 (1996).

 \( ^{13} \)  D. J. Wales and J. P. K. Doye, J. Phys. Chem. A 101, 5111 (1997).

 \( ^{14} \)  C. Barrón, S. Gómez, and D. Romero, Appl. Math. Lett. 10, 25 (1997).

 \( ^{15} \)  R. H. Leary, J. Global Optimization 11, 35 (1997).

 \( ^{16} \)  D. Romero, C. Barrón, and S. Gómez, Comp. Phys. Comm. in press (1999).

 \( ^{17} \)  R. H. Leary and J. P. K. Doye, Phys. Rev. E 60, R6320 (1999).

 \( ^{18} \)  D. J. Wales, J. P. K. Doye, A. Dullweber and F. Y. Naumkin, The Cambridge Cluster Database, URL http://brian.ch.cam.ac.uk/CCD.html.

 \( ^{19} \)  URL

http://www.vetl.uh.edu/~cbarron/LJ_cluster/researchpot.html.

 \( ^{20} \)  M. R. Hoare and J. McInnes, Faraday Discuss., Chem. Soc. 61, 12 (1976).

 \( ^{21} \)  C. J. Tsai and K. D. Jordan, J. Chem. Phys. 99, 6957 (1993).

 \( ^{22} \)  J. P. K. Doye, M. A. Miller, and D. J. Wales, J. Chem. Phys. 111, 8417 (1999).

 \( ^{23} \)  P. E. Leopold, M. Montal, and J. N. Onuchic, Proc. Natl. Acad. Sci. USA 89, 8271 (1992).

 \( ^{24} \)  J. D. Bryngelson, J. N. Onuchic, N. D. Socci, and P. G. Wolynes, Proteins: Structure, Function and Genetics 21, 167 (1995).

 \( ^{25} \)  A. L. Mackay, Acta Cryst. 15, 916 (1962).

 \( ^{26} \)  L. D. Marks, Phil. Mag. A 49, 81 (1984).

 \( ^{27} \)  J. P. K. Doye, M. A. Miller, and D. J. Wales, J. Chem. Phys. 110, 6896 (1999).

 \( ^{28} \)  M. A. Miller, J. P. K. Doye, and D. J. Wales, Phys. Rev. E 60, 3701 (1999).

 \( ^{29} \)  Z. Li and H. A. Scheraga, Proc. Natl. Acad. Sci. USA 84, 6611 (1987).

 \( ^{30} \)  D. M. Deaven and K. M. Ho, Phys. Rev. Lett. 75, 288 (1995).

 \( ^{31} \)  S. K. Gregurick, M. H. Alexander, and B. Hartke, J. Chem. Phys. 104, 2684 (1996).

 \( ^{32} \)  J. A. Niese and H. R. Mayne, J. Chem. Phys. 105, 4700 (1996).

 \( ^{33} \)  W. Pullan, Comp. Phys. Comm. 107, 137 (1997).

 \( ^{34} \)  M. D. Wolf and U. Landman, J. Phys. Chem. A 102, 6129 (1998).

 \( ^{35} \)  C. Barrón, S. Gómez, D. Romero, and A. Saavedra, Appl. Math. Lett. 12, 85 (1999).

 \( ^{36} \)  B. Hartke, J. Comp. Chem. 20, 1752 (1999).

 \( ^{37} \)  J. P. K. Doye and D. J. Wales, Phys. Rev. Lett. 80, 1357 (1998).

 \( ^{38} \)  J. P. K. Doye, D. J. Wales, and M. A. Miller, J. Chem. Phys. 109, 8143 (1998).

 \( ^{39} \)  D. J. Wales, personal communication.

 \( ^{40} \)  B. Hartke, personal communication.

 \( ^{41} \)  M. Locatelli and F. Schoen, Computational Optimization and Applications submitted (1999).

 \( ^{42} \)  J. E. Jones and A. E. Ingham, Proc. R. Soc. A 107, 636 (1925).

 \( ^{43} \)  M. A. Miller, J. P. K. Doye, and D. J. Wales, J. Chem. Phys. 110, 328 (1999).

 \( ^{44} \)  C. J. Cerjan and W. H. Miller, J. Chem. Phys. 75, 2800 (1981).

 \( ^{45} \)  A public domain version of the basin-hopping code is available from http://brian.ch.cam.ac.uk/software.html.

 \( ^{46} \)  R. P. White and H. R. Mayne, Chem. Phys. Lett. 289, 463 (1998).

 \( ^{47} \)  W. H. Press, B. P. Flannery, S. A. Teukolsky, and W. T. Vetterling, Numerical Recipes (Cambridge University Press, Cambridge, 1986).

 \( ^{48} \)  D. Liu and J. Nocedal, Mathematical Programming B 45, 503 (1989).

 \( ^{49} \)  T. A. Weber and F. H. Stillinger, J. Chem. Phys. 80, 2742 (1984).

 \( ^{50} \)  A. Heuer, Phys. Rev. Lett. 78, 4051 (1997).

 \( ^{51} \)  K. D. Ball et al., Science 271, 963 (1996).

 \( ^{52} \)  O. M. Becker and M. Karplus, J. Chem. Phys. 106, 1495 (1997).

 \( ^{53} \)  D. J. Wales, M. A. Miller, and T. R. Walsh, Nature 394, 758 (1998).

 \( ^{54} \)  D. J. Wales, Mol. Phys. 78, 151 (1993).

 \( ^{55} \)  G. Franke, E. R. Hilf, and P. Borrmann, J. Chem. Phys. 98, 3496 (1993).

 \( ^{56} \)  S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Science 220, 671 (1983).

 \( ^{57} \)  J. P. K. Doye and D. J. Wales, J. Chem. Soc., Faraday Trans. 93, 4233 (1997).
 

TABLE I. The number of minima,  \( n_{min} \) , and transition states,  \( n_{ts} \) , for CLJ \( _{13} \)  as a function of  \( \mu_{comp} \) . For each minimum 30 transition state searches were performed; these searches were parallel and antiparallel to the eigenvectors with the fifteen lowest eigenvalues.  \( \overline{\Delta E} \) ,  \( \overline{b}_{u} \) ,  \( b_{d} \)  are the average energy difference, uphill barrier and downhill barrier, respectively, where the average is over all the non-degenerate rearrangement pathways. (Degenerate pathways connect different permutational isomers of the same minimum.)  \( \overline{\Delta E} = \overline{b}_{u} - \overline{b}_{d} \) .

<table><tr><td>\( \mu_{\text{comp}}/\epsilon \)</td><td>0</td><td>0.5</td><td>1</td><td>2.5</td><td>5</td><td>10</td><td>25</td></tr><tr><td>\( n_{\text{min}} \)</td><td>1467</td><td>769</td><td>470</td><td>169</td><td>75</td><td>33</td><td>10</td></tr><tr><td>\( n_{\text{ts}} \)</td><td>12435</td><td>5820</td><td>3010</td><td>801</td><td>262</td><td>100</td><td>37</td></tr><tr><td>\( \overline{\Delta E}/\epsilon \)</td><td>1.593</td><td>3.172</td><td>4.501</td><td>7.191</td><td>11.215</td><td>20.701</td><td>40.176</td></tr><tr><td>\( \overline{b}_{u}/\epsilon \)</td><td>2.201</td><td>3.939</td><td>5.396</td><td>8.231</td><td>12.346</td><td>21.759</td><td>42.263</td></tr><tr><td>\( \overline{b}_{d}/\epsilon \)</td><td>0.609</td><td>0.767</td><td>0.896</td><td>1.041</td><td>1.131</td><td>1.058</td><td>2.087</td></tr><tr><td>\( \overline{b}_{d}/\overline{\Delta E} \)</td><td>0.382</td><td>0.242</td><td>0.199</td><td>0.145</td><td>0.101</td><td>0.051</td><td>0.052</td></tr></table>

TABLE II. Properties of the CLJ \( _{38} \)  PES for a sample of 6000 connected minima as a function of  \( \mu_{comp} \) .  \( n_{ts} \)  is the number of transition states connecting these minima.  \( \Delta E \)  is the energy difference between the global minimum and the lowest energy icosahedral minimum and  \( b_{fcc} \)  ( \( b_{icos} \) ) is the energy barrier that has to be overcome to escape from the fcc (icosahedral) funnel and enter the icosahedral (fcc) funnel. Of course,  \( \Delta E = b_{fcc} - b_{icos} \) . For the  \( n_{search} \)  lowest-energy minima 20 transition state searches were performed; these searches were parallel and antiparallel to the eigenvectors with the ten lowest eigenvalues.  \( n_{fcc} \)  and  \( n_{icos} \)  are the numbers of minima in the fcc and icosahedral funnels at the energy at which the two funnels become connected.

<table><tr><td>\( \mu_{\text{comp}}/\epsilon \)</td><td>0</td><td>0.25</td><td>0.5</td><td>1</td><td>2.5</td><td>5</td></tr><tr><td>\( n_{\text{ts}} \)</td><td>8633</td><td>9111</td><td>9911</td><td>11656</td><td>17137</td><td>23270</td></tr><tr><td>\( n_{\text{search}} \)</td><td>1271</td><td>1277</td><td>1491</td><td>1924</td><td>3107</td><td>4253</td></tr><tr><td>\( \Delta E \)</td><td>0.676</td><td>1.550</td><td>2.274</td><td>3.564</td><td>6.120</td><td>9.893</td></tr><tr><td>\( b_{\text{fcc}}/\epsilon \)</td><td>4.219</td><td>4.795</td><td>5.256</td><td>6.143</td><td>8.892</td><td>12.659</td></tr><tr><td>\( b_{\text{icos}}/\epsilon \)</td><td>3.543</td><td>3.245</td><td>2.981</td><td>2.580</td><td>2.772</td><td>2.766</td></tr><tr><td>\( b_{\text{icos}}/\Delta E \)</td><td>9.893</td><td>2.094</td><td>1.311</td><td>0.724</td><td>0.453</td><td>0.280</td></tr><tr><td>\( n_{\text{fcc}} \)</td><td>92</td><td>113</td><td>73</td><td>106</td><td>104</td><td>86</td></tr><tr><td>\( n_{\text{icos}} \)</td><td>912</td><td>439</td><td>194</td><td>27</td><td>5</td><td>6</td></tr><tr><td>\( n_{\text{fcc}}/n_{\text{icos}} \)</td><td>0.11</td><td>0.26</td><td>0.38</td><td>3.93</td><td>20.8</td><td>14.33</td></tr></table>

TABLE III. Results of annealing simulations for CLJ \( _{38} \)  as a function of  \( \mu_{comp} \) .  \( f_{O_{h}}(n_{\text{cycles}}) \)  is the fraction of the annealing runs that terminated at the global minimum, and  \( f_{icos} \)  is the fraction of runs that ended in the lowest five icosahedral minimum. Each annealing run involves a linear decrease in the temperature from the liquid to 0K in  \( n_{cycles} \)  Monte Carlo cycles. The results are averages over 200 annealing runs.

<table><tr><td>\( \mu_{\text{comp}}/\epsilon \)</td><td>0</td><td>0.25</td><td>0.5</td><td>1</td><td>2.5</td><td>5</td></tr><tr><td>\( f_{O_{h}}(10^{6}) \)</td><td>0%</td><td>2.5%</td><td>7.5%</td><td>19.5%</td><td>67%</td><td>79.5%</td></tr><tr><td>\( f_{O_{h}}(10^{7}) \)</td><td>2%</td><td>14%</td><td>31%</td><td>66.5%</td><td>97%</td><td>99.5%</td></tr><tr><td>\( f_{\text{icos}}(10^{6}) \)</td><td>37%</td><td>29.5%</td><td>12.5%</td><td>7.5%</td><td>1%</td><td>0%</td></tr><tr><td>\( f_{\text{icos}}(10^{7}) \)</td><td>80%</td><td>56.5%</td><td>38%</td><td>6.5%</td><td>0%</td><td>0%</td></tr></table>
 
