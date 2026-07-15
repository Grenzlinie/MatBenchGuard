# Dynamical characterization of active regions environments for ion dynamics in Lithium metasilicate glasses

C. Balbuena, M.A. Frechero, R.A. Montani *

Universidad Nacional del Sur, Departamento de Química – INQUISUR, Av. Alem 1253, 8000-Bahía Blanca, Argentina

---

## ARTICLE INFO

**Article history:**
Received 14 January 2013
Available online 15 April 2013

**Keywords:**
Silicate glasses;
Ionic conductivity;
Molecular Dynamics;
Isoconfigurational Ensemble Method

---

## ABSTRACT

Surprisingly, there is not a complete and general working theory for the ionic conduction on structurally disordered inorganic solids at present. In this context, lithium metasilicate glasses appear as paradigmatic and they have been extensively used for investigation in order to identify the main ingredients for a working theory of ionic conducting glasses. In particular among one of these main ingredients, the interaction among the mobile cations appears relevant, especially after recent results showing the existence of preferred pathways for ionic migration. We have performed Molecular Dynamics simulations on lithium metasilicate to better understand the ion-ion interactions. We introduce a very useful tool developed by Harrowell and co-workers (2004) [1] to study propensity to movement and the use of the Pearson's coefficient to characterize the correlation among the different kinds of ion. Our study allows us to support – from an alternative point of view – the idea of a landscape of energy for lithium ions with high propensity to movement (which eventually belongs to a high propensity cluster as defined in our previous work) and strongly dependent on the interaction among them. On the contrary, in the same window of time, these lithium ions do not strongly correlate with their nearest oxygen ions.

© 2013 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Even taking into account the long story of experimental and theoretical work there is not a complete and acceptable theory for ionic conduction in inorganic oxide glasses. To accomplish this task, it seems at present that the main work to be done goes in the direction of increasing the experimental and theoretical evidence, involving the main potential ingredients to elaborate a working theory of ionic transport.

Many of the ionic conducting glasses present universal behavior in their *dc* and *ac* conductivity: on the one hand, the Arrhenius temperature dependence of the *dc* conductivity and on the other hand the fact that *ac* conductivity data can be scaled onto a master curve for different temperatures. This universality strongly encourages the research to find a universal mechanism for ionic conduction.

In this direction, and at least from a theoretical point of view, three main lines of exploration appear as pertinent: the percolative transport given by jumps over the random energy barriers, the (mobile) ion-ion interaction/correlation and the interaction between the mobile ions with the glassy matrix.

The percolative transport here refers to the hopping of a non-interacting charge carrier having only nearest jumps allowed. In this scenario, the distribution of activation energies represents the disordered structure of glasses. Typical work in this direction mainly includes the study of the universality of the *a.c.* conduction in disordered solids done (among others) by Dyre [2], Svare et al. [3] and Hunt [4].

The second class of models – those mainly based on the ion-ion interaction – has its extreme expression in the Coulomb gas lattice model of Maass et al. [5]. This model shows that the Coulombic interactions provide a mechanism for understanding the non-Debye relaxation mainly *via* the backward correlations among the subsequent hop of the ions. These authors also show that the local structure disorder reinforces these backward correlations. A later extension of the model is included in the work by P. Maass, M. Meyer and A. Bunde [6] and confirms that the Coulomb interactions and structural disorder are needed to find the typical dispersion behavior observed in experiments.

The third class of models includes the interaction of the glassy matrix and the traveling ions. The paradigmatic ones here are the Coupling Model (CM) by Ngai [7] and the Jump Relaxation Model (JRM) introduced by K. Funke [8]. The intrinsic nature of the Coupling Model implies an interaction between ions and the glassy matrix: the moving ion and the potential energy of the hosting site, but no microscopic mechanical detail is included. The JRM is mainly based on the reorganization of the local environment of the moving ions and includes a mathematical description of the involved processes at the microscopic scale. This model includes a mechanism for the Mixed Alkali effect and yields a logarithmic dependence of the activation energy and the charge carrier concentration, but this model is essentially limited to the *dc* transport. The JRM has been the starting point for later modifications [9–11].

* Corresponding author.
E-mail address: rmontani@criba.edu.ar (R.A. Montani).

0022-3093/$ – see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.jnoncrysol.2013.03.017

In addition – and from a classical computational experiment of Molecular Dymanics (MD) – the crudest evidence supporting the cou- pling between ion and network dynamics is given perhaps by the recent computational experiment of Sunyer et al. [12] in $Na_{2}O-4SiO_{2}$ and in $(Li_{2}O)_{x}(SiO_{2})_{1-x}$ by Heuer et al. [13].

Moreover, using MD simulations it was shown for $Li_{2}SiO_{3}$ [14,15] that the number density of sites is slightly greater than the number den- sity of mobile ions. For these authors these results strongly suggest that the macroscopic transport requires the existence of some cooperative mechanism even including mobile vacancies [15]. More recently, Rao et al. [16] and Montani et al. [17] have respectively shown in two different ways the existence of preferred transport pathways.

In the present work we report our results on the ion-ion interaction studied by using an alternative tool developed by Harrowell and co-workers: the IC ensemble method [1]. The output from the IC meth- od give us the adequate quantity to be studied (by using Pearson's coef- ficient), that is: the ion displacement calculated at the time in which the dynamics of the lithium ions becomes highly heterogeneous $(t^{*})$ . Our procedure gives an alternative characterization of the ion dynamics with respect to the existing previous ones in the literature, and, the emerging results allow to reinforce the idea that a mechanism for ionic conduction involving a cooperative movement among the lithium ions should be highly probable.

## 2. The Molecular Dynamics simulations and calculations

Molecular Dynamics calculations were performed on a system of 3456 particles (1152 Li, 570 Si and 1728 O) in the same way as in our previous studies [17]. Briefly, the containing box ensures that the density corresponds to the experimental density of the glass [18]. The system $Li_{2}O-SiO_{2}$ we employed consists of a three-dimensional ensem ble of particles interacting by the pair potential of Gilbert-Ida type [19] including the $r^{-6}$ term:

$$
U_{ij}(r)=\frac{q_{i}q_{j}e^{2}}{4\pi \varepsilon_{0}r}-\frac{c_{i}c_{j}}{r^{6}}+f_{0}\left(b_{i}+b_{j}\right)\exp\left(\frac{a_{i}+a_{j}-r}{b_{i}+b_{j}}\right). \tag{1}
$$

The first term in Eq. (1) is the Coulomb interaction with the effec- tive charge numbers $q_{i}$ . The second term is a dispersive interaction and is present for interactions involving only oxygen ions. The last term is a Born-Meyer type potential and takes into account the repul- sive short-range interactions. The parameters of the potentials used were derived on the basis of ab-initio molecular orbital calculations by Habasaki [18].

The system was prepared by putting the atoms on a cubic box and assigning to each atom velocities drawn from a Maxwell-Boltzmann distribution corresponding to a temperature of 3000 K. The Verlet Algorithm with a time step of 1 fs was used to integrate the equations of motion. Simulations were performed on a cubic box with periodic boundary conditions using the LAMMPS package [20].

The system was then firstly equilibrated at 3000 K in a 2 ns run using the NVE ensemble. Then, to reach the working temperature, it was cooled down from 3000 K to its final temperature 700 K in 2 suc- cessive cooling steps. Each cooling step (from 3000 K to 2000 K, and from 2000 K to 700 K respectively) consists of a 2 ns run using a ther- mostat to decrease the temperature linearly in the NPT ensemble. Two intermediate periods of equilibration consisting of a 2 ns run in the NPT ensemble were included at 2000 K and at 700 K to verify no pressure and temperature drifts. After cooling the system, alternate runs of 100 ps each in the NVE and NVT ensemble were successively repeated to complete 2 ns. After that, the system was equilibrated in a 2 ns run using the NVE ensemble. Finally, after this carefuly equilibra- tion procedure, trajectories of 2 ns length were generated in the NVE ensemble for analysis [17].

The calculated mean square displacement $<r^{2}(t)>$ is defined as:

$$
\left\langle r^{2}(t)\right\rangle=\mathrm{N}^{-1}\sum_{j=1}^{\mathrm{N}}\left\langle\left|\vec{r}_{j}(t)-\vec{r}_{j}(0)\right|^{2}\right\rangle \tag{2}
$$

where $\vec{r}_{j}(t)$ is the position vector of particle $j$ at instant $t$ and $N$ is the number of the $j$-particles. The non-Gaussian parameter $\alpha_{2}(t)$ was introduced by Rahman and it characterizes the deviation of the dynamics from the Gaussian behavior and it is defined as:

$$
\alpha_{2}(t)=\frac{3}{5}\frac{\left\langle r^{4}(t)\right\rangle}{\left\langle r^{2}(t)\right\rangle^{2}}-1. \tag{3}
$$

The time when $\alpha_{2}(t)$ reaches its maximum value $t^{*}$ defines a time interval $[0,t^{*}]$ in which the behavior of the system is dynamically het- erogeneous [21,22]. This quantity is located roughly at the crossover from the caging to the diffusive regime.

The Isoconfigurational Ensemble Method developed by Harrowell and co-workers [1] was used through the present work. Briefly, a series of equal length MD runs from the same initial configuration is performed; that is, starting always with the same structure, but with different initial particle momenta chosen at random from the Maxwell-Boltzmann distribution at the appropriate temperature. In this ensemble, the propensity of a particle for motion in the initial configuration for a fixed time interval t, has been defined as [1]:

$$
\left\langle\Delta r_{i}^{2}\right\rangle_{IC}=\left\langle\left|\vec{r}_{i}(t)-\vec{r}_{i}(0)\right|^{2}\right\rangle \tag{4}
$$

where $|\vec{r}_{i}(t)-\vec{r}_{i}(0)|^{2}$ is the squared displacement of particle $i$ (in such time interval) and < > indicates the average over the ensemble.

## 3. Results and discussion

As was pointed out in our previous work [17], lithium ion dynamics reaches its diffusive regime at ca. 400 ps, whereas oxygen and silicon ions remain localized even in the nanosecond scale. For lithium ions,40 ps corresponds to the so called $t^{*}$ time, and it defines an interval[0,t*] where their behavior is dynamically heterogeneous. It can be seen that in a logarithmic plot of the mean square displacement(MSD) vs time, $t^{*}$ is roughly located at the crossover from the caging to the diffusive regime of lithium ions (of course, the "cage" effect over lithium ions is due to their nearest oxygen ions) [17].

Fig. 1 presents the propensities for oxygen atoms at 4 ps and 40 ps respectively. Propensity is heterogeneously distributed over the differ- ent ions, with some of the oxygen ions having values larger than the mean value. Besides, it is also clear from this figure that propensities for oxygen ions remain unchanged even at 40 ps, i.e. the time when the dynamics of lithium ions abandon the caging regime [17]. Moreover, propensities in both time regimes are similarly distributed, or in other words, the long-time behavior (40 ps) copies the short-time behavior(4 ps) suggesting that longer time dynamics of these oxygen atoms is implicit in the short-time dynamics. The mean value for the propensity at 40 ps is equal to $0.14 \mathring{A}^{2}$ .

Next, we consider the high propensity lithium ions (LiHPs) which are defined as those lithium ions that at time $t^{*}$ have a displacement greater than one half of the distance of the first maximum of the radi- al distribution function for Li-Li: ca. $1.4 \mathring{A}$ [23]. In our previous paper[17] we showed the formation of clusters of high propensity (HPC) which put into evidence the existence of extended topological regions of the structure with a high ability to promote the faster motion of lithium ions. Those regions of the sample can be detected at very low times and will remain even at the diffusional scale ( $t=400$ ps).

Now, we define three limiting values for the oxygen ion propensity: "low" for propensity values lower than $0.8 \mathring{A}^{2}$ , "medium" for propensity

![](./images/813231719460110337_1.jpg)

Fig. 1. Propensity (in $\mathring{A}^2$) of a collection of 240 oxygen ions chosen at random, at the time interval [0,t*].

values between 0.8 $\mathring{A}^2$ and 0.16 $\mathring{A}^2$, and "high" for propensity values larger than 0.16 $\mathring{A}^2$. Then, we will explore the qualitative behavior of the oxygen ions surrounding lithium ions. In Fig. 2(a) we show the propensity of the nearest oxygen ions for "high" propensity and "low" propensity lithium ions. In this plot we take the LiHPs as defined above and the same number of lithium having the lowest propensity values (the LiLPs).

In other words: from a list ranging from the highest to the lowest propensity for the lithium ions, we take the same number of lithium ions $n_{Li}$ from the top and from the bottom of the list (of course, the value of $n_{Li}$ is dictated by the definition of LiHP given above). In Fig. 2(a) we plot the results for those oxygen ions considered as Bridging Oxygens (BO) whereas in Fig. 2(b) the same analysis is performed for the Non Bridging Oxygens (NBO). We learn from Fig. 2a and b that, in both cases, lithium ions having highest values of propensity are preferentially surrounded by oxygen atoms of high propensity, whereas lithium ions, having the lowest values of propensity, are preferentially surrounded by oxygen ions having low values of propensity. Again, we remark this important result here: for the highest (relevant) values of oxygen ion propensity, the qualitative difference between those oxygen surrounding LiHPs and those oxygen surrounding LiLPs becomes evident.

This result suggests that fluctuations of the oxygen ions are necessary to enable the lithium ions (LiHPs) pass from its present position to a next available position, which in terms of the energy landscape, means that these fluctuations are reflected by fluctuations of the saddle energy [13].

Next we consider the Mean Square Displacement (MSD) of lithium ions and its relationship with the displacement of the oxygen ions. To do that we proceed in the same manner as Sunyer et al. [12]. We generate three trajectories in which the mass of the oxygen atoms has been artificially changed. Of course, the mass of the ions affects their displacement in the time unit and consequently, the infinite value for the oxygen mass keeps the oxygen atoms fixed.

In Fig. 3 we show the MSD of lithium ions versus time, for three different masses of the oxygen atom: 16, 5000 and infinite, respectively. From this figure we learn that the diffusion of lithium ions involves a necessary oxygen ion dynamics.

Moreover, we have shown in Fig. 6 of our previous work that LiHPs are responsible for the increase of the global MSD to its final values, that is for the relevant window of time (from 0 to 400 ps) the MSD of the LiHPs reaches the diffusive behavior (slope 1 in that

![](./images/813231719460110337_2.jpg)

Fig. 2. a) Distribution of the nearest bridging oxygen ions (BO) for LiHPs (red bar) and LiLPs (black bar). Propensity of the oxygen ions is grouped as "low", "medium" and "high" respectively. b) Distribution of the nearest non-bridging oxygen ions (NBO) for LiHPs (red bar) and LiLPs (black bar).

![](./images/813231719460110337_3.jpg)

Fig. 3. The mean square displacement of lithium ions for the three different values of
the oxygen mass.

figure) well before the 400 ps, whereas the LiLPs do not [17]. It is
also clear from the same figure that even in the case of a kind of
exchange - if any - between these two populations (those LiHPs
belonging to the HPC and the LiLPs respectively), it is irrelevant in
the time window of interest.

Then, in light of these strong evidence, we can conclude that even
when the displacement of oxygen ions is irrelevant compared with
the lithium ion displacement (as is shown in Fig. 1 of our previous
work [17]), it is necessary for the diffusion of lithium ions. When
oxygen mass is infinite - or equivalently the oxygen ions remain
fixed in their positions - the mobility of lithium ions goes dra-
matically to zero.

Now we will analyze the kinetic correlation between lithium ions
with the glassy matrix or equivalently with its coordinated oxygen
ions. To do that we will use the Pearson's correlation coefficient, K
[24,25]. The value of K lies in the [-1,1] interval. It takes the value
of 1 in the case of a "complete positive correlation" and on the con-
trary, it takes the value of -1 for the case of a "complete negative cor-
relation"; a value near zero indicates that the involved variables are
uncorrelated.For our particular case, we consider two particles (i, j)
of the system separated by a distance $r_{ij}$ and calculate their mean
displacement in an isoconfigurational (IC) ensemble: $<r_{i}>_{IC}$ and
$<r_{j}>_{IC}$ respectively, and then compare in each w-trajectory of the
ensemble their displacement with respect to the corresponding
mean value. Of course this analysis is performed at a given time; in
our case, the relevant value is 40 ps. Then, for the two particles i, j
separated at a given distance $d_{ij}$, in the w-ensemble, the analytical
expression of K takes the following form:

$$
K_{i-j}\left(r_{i j}\right)=\frac{\sum_{w=1}^{N_{I C}}\left(\left\langle r_{i}\right\rangle_{I C}-r_{i}(w)\right) \cdot\left(\left\langle r_{j}\right\rangle_{I C}-r_{j}(w)\right)}{S_{i} \cdot S_{j}} \tag{5}
$$

where $N_{IC}$ is the total number of trajectories in the isoconfigurational
ensemble (typically 1000 trajectories) and $S_{i}$ and $S_{j}$ are the standard
deviation of the displacement in the calculated trajectory of the en-
semble. In the following discussion we will consider the summation
index "i" over lithium ions, whereas the index "j" addresses the lithi-
um ions or oxygen ions depending on the correlation under study,
namely Li-Li correlation or Li-O correlation.

In Fig. 4 we show the radial distribution function for lithium-lithium
ions, and $K_{Li-Li}$, both as a function of the distance from the reference
ion $r_{ij}$. In this figure we have discriminated $K_{Li-Li}$ for both LiHPs and
LiLPs respectively. It becomes clear from this figure that for LiHPs the
higher values of $K_{Li-Li}$ are concentrated under the first peak of the $g_{(r)}$
and then we can conclude from this figure that for lithium-lithium
interactions, correlation is mainly restricted between the nearest ions.

Then using the Pearson's coefficient we will study the lithium ion
correlation with its nearest lithium and oxygen ions respectively. As
previously, we will define the nearest neighbors as all these ions (lithi-
um or oxygen) standing at a lower distance than the one corresponding
to the first peak in the respective partial pair distribution function (Li-Li
or Li-O). Then, we calculate the mean value of the Pearson's coefficient
for each i-lithium ion: $<K_{i}>_{Li}$ and $<K_{i}>_{O}$ respectively, as follows:

$$
\left\langle K_{i}\right\rangle_{j}=\frac{\sum_{j=1}^{N_{j-N N}} K_{i-j}}{N_{j-N N}} \tag{6}
$$

![](./images/813231719460110337_4.jpg)

Fig. 4. The radial distribution function for lithium-lithium ions, and $K_{Li-Li}$, both as a function of the distance from the reference ion.

![](./images/813231719460110337_5.jpg)

Fig. 5. The calculated $K_{i-j}^*$ as a function of lithium ion propensity.

where $j$ is lithium or oxygen, and $N_{j-NN}$ is the number of the nearest $j$ neighbors to the $i$-ion.

Now we can calculate a mean value of correlation to the nearest ions as follows:

$$
\overline{K}_{j} = \frac{\sum_{i=1}^{N_{Li}} \langle K_{i} \rangle_{j}}{N_{Li}} \tag{7}
$$

where $N_{Li}$ is the number of lithium ions, and the index $j$ refers to the chosen nearest species: lithium or oxygen.

Now, using Eqs. (6) and (7) we calculate the particular cases of interest:

$$
K_{Li-Li}^* = \frac{\langle K_{i} \rangle_{j}}{\overline{K}_{j}} \tag{8}
$$

(where $i$ and $j$ refers to the lithium ions) and,

$$
K_{Li-O}^* = \frac{\langle K_{i} \rangle_{j}}{\overline{K}_{j}} \tag{9}
$$

(where $i$ refers to lithium ions and $j$ to oxygen ions).

In Fig. 5 we show the calculated $K_{i-j}^*$ as a function of lithium ion propensity. The vertical dashed line in the figure indicates the threshold value of propensity from which a lithium ion is to be considered a LiHP. All $K_{i-j}^*$ values above 1 in Fig. 5 are higher than the average. In the inset of Fig. 5 we show the relative distribution below and above the average of $K_{i-j}^*$'s. Then we learn from this figure that LiHPs (again: those lithium ions having a propensity value higher than $1.96\ \mathring{A}^2$ and responsible for the increase of the global MSD to its final value) have a marked tendency to be correlated with its nearest lithium ions (black points on the top right quadrant). On the contrary, the tendency of the nearest oxygen ions is not relevant.

From Fig. 5, we learn that about 85% of the high mobile LiHP is correlated with their first neighbors whereas the remaining 15% does not. Then, if tacking into account that the number density of sites is slightly greater than the number density of mobile ions [14,15], our findings allow us to support in an alternative way that the idea of a mechanism for ionic conduction involving a cooperative movement among the lithium ions should be highly probable. In this direction, a recent paper by Heuer et al. suggest to better look at the vacancy dynamics rather than that of mobile ions [26].

## 4. Conclusion

We have studied the correlation among lithium ions using an alternative way of employing the IC ensemble method. The emerging results from the IC method give us the adequate quantity to be studied: the displacement calculated at $t^*$ (the time in which the dynamics of the lithium ions becomes highly heterogeneous).

Our findings allow us to suggest that a mechanism for ionic conduction should involve a cooperative movement among the lithium ions should be highly probable (but perhaps not exclusive).

But, on the contrary, the LiHPs (which eventually can belong to a HPC as defined in our previous work [17]) does not strongly correlate with their nearest neighbor oxygen ions. The existence of such a heterogeneous dynamics for lithium ions is due to their different dynamical environments which are governed by the oxygen ion fluctuations. In fact - and as was pointed out previously - fluctuations of the oxygen ions are necessary to enable the lithium ions (LiHPs) pass from its present position to a next available position, which in terms of the energy landscape means that these fluctuations are reflected by fluctuations of the saddle energy [13].

## Acknowledgment

Financial support from UNS, ANPCyT, SeCyT and CONICET is gratefully acknowledged. R.A.M. is a research fellow of the C.I.C and M.A.F is a research fellow of CONICET. C.B would like to thank CONICET for a fellowship.

## References

[1] A. Widmer-Cooper, P. Harrowell, H. Fynewever, Phys. Rev. Lett. 93 (2004) 135701.
[2] J. Dyre, T.B. Schroder, Rev. Mod. Phys. 72 (2000) 873.
[3] I. Svare, F. Borsa, D.R. Torgeson, S.W. Martin, J. Non-Cryst. Solids 172-172 (1994) 1300.
[4] A.G. Hunt, Philos. Mag. B 81 (2001) 875.
[5] P. Maass, J. Petersen, A. Bunde, W. Dieterich, H.E. Roman, Phys. Rev. Lett. 66 (1991) 52.
[6] P. Maass, M. Meyer, A. Bunde, Phys. Rev. B 51 (1995) 8164.

[7] K. Ngai, J. Chem. Phys. 98 (1993) 6424.
[8] K. Funke, Prog. Solid State Chem. 22 (1993) 111.
[9] M.D. Ingram, B. Roling, J. Phys. Condens. Matter 14 (2002) 1-11.
[10] R.D. Banhatti, C. Cramer, D. Zielniok, A.H. Jean Robertson, Z. Phys. Chem. 223 (2009) 1201.
[11] M.D. Ingram, Z. Phys. Chem. 223 (2009) 1201-1215.
[12] Sunyer, P. Jund, R. Jullien, J. Phys. Condens. Mater 15 (2003) L431-L437.
[13] A. Heuer, H. Lammert, M. Kunow, Z. Phys. Chem. 218 (2004) 1429-1438.
[14] J. Habasaki, K. Ngai, Y. Hiwatari, J. Chem. Phys. 120 (2004) 8195.
[15] H. Lammert, M. Kunow, A. Heuer, Phys. Rev. Lett. 90 (2003) 215901.
[16] R. Prasada Rao, T.D. Tho, S. Adams, Solid State Ionics 181 (2010) 1.
[17] R.A. Montani, C. Balbuena, M.A. Frechero, Solid State Ionics 209-210 (2012) 5-8.

[18] J. Habasaki, I. Okada, Mol. Simul. 9 (1992) 319.
[19] Y. Ida, Phys. Earth Planet. Inter. 13 (1976) 97.
[20] J. Plimpton, J. Comput. Phys. 117 (1995) 1.
[21] Rahman, Phys. Rev. 136 (1964) A405.
[22] J. Habasaki, K. Ngai, J. Chem. Phys. 129 (2008) 034503.
[23] J. Habasaki, Y. Hiwatari, Phys. Rev. E 65 (2002) 21604.
[24] A. Widmer-Cooper, P. Harrowell, J. Chem. Phys. 126 (2007) 154503.
[25] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes. The Art of Scientific Computing, Cambridge University Press, 1986.
[26] H. Lammert, A. Heuer, Phys. Rev. Lett. 104 (2010) 125901.