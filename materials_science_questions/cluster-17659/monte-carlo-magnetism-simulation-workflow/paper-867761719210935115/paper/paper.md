
# Simulation of Magnetization Switching in Biaxial Single-Domain Ferromagnetic Particles

Xuekun Kou \( ^{1,2} \) , M. A. Novotny \( ^{1,2,} \)  and Per Arne Rikvold \( ^{1,3} \) 

 \( ^{1} \) Supercomputer Computations Research Institute, Florida State University, Tallahassee, Florida 32306-4130

 \( ^{2} \) Dept. of Electrical Engineering, FAMU–FSU College of Engineering, Tallahassee, FL 32310-2870

 \( ^{3} \) Center for Materials Research and Technology, and Department of Physics, Florida State University, Tallahassee, Florida 32306-4350

(November 19, 2018)

The magnetization switching dynamics of biaxial single-domain homogeneous ferromagnetic particles, in which the two easy axes are perpendicular to each other, is simulated using a 4-state clock model. A zero-field mapping of the statics between the symmetric 4-state clock model and two decoupled Ising models is extended to non-zero field statics and to the dynamics. This significantly simplifies the analysis of the simulation results. We measure the magnetization switching time of the model and analyze the results using droplet theory. The switching dynamics in the asymmetric model is more complicated. If the easy axis is perpendicular to the stable magnetization direction, the system can switch its magnetization via two different channels, one very fast and the other very slow. A maximum value for the switching field as a function of system size is obtained. The asymmetry affects the switching fields differently, depending on whether the switching involves one single droplet or many droplets of spins in the stable magnetization configuration. The angular dependence of the switching field in symmetric and asymmetric models is also studied.

PACS Number(s): 75.40.Mg, 05.50.+q, 02.70.Lq, 02.50.-r

## I. INTRODUCTION

Biaxial media have recently attracted much research interest as potential materials for applications in high-density magnetic recording. This is a consequence of their good thermal stability, high coercivity and coercivity squareness, and low medium noise  \( [1] \) - \( [4] \) . With the current rapid increase in recording density, the size of a magnetic particle used to store a single bit may soon become so small that it can only contain one single magnetic domain. Understanding the dynamics of magnetization switching in individual single-domain particles is therefore essential. Biaxial media may be obtained, for example, by sputtering a Co-based alloy onto a Cr substrate  \( [5,6] \) , by fabricating perovskite superlattices consisting of different ferromagnetic metallic oxides  \( [7] \) , or by epitaxially growing Fe on GaAs(001)  \( [8] \) . By applying lithographic patterning techniques to precisely control the particle shape, a uniaxial medium may also exhibit biaxial properties due to competition between the magneto-crystalline and shape anisotropies  \( [9,10] \) . The two easy axes in biaxial media are often perpendicular to each other, and they may have the same or different magnetic anisotropies. In thin films, these two axes can both be in-plane, or one of them can be out-of-plane, often perpendicular to the plane of the film. New techniques, such as nanolithography and ultra-high resolution scanning microscopies, have recently made the synthesis and experimental observation of isolated single-domain particles possible. For instance, the magnetization switching of individual barium ferrite nanoscale particles has been observed using Magnetic Force Microscopy (MFM), and a maximum switching field was observed for particles of diameter near 55 nm  \( [11] \) . For other particles, the angular dependence of the switching (or coercive) field has been measured  \( [12,13] \) , the switching dynamics investigated  \( [12] \) , and the switching statistics measured  \( [13] \) . In Refs.  \( [14] \)  and  \( [15] \) , arrays of single-domain Co dots were fabricated, and the magnetization switching was observed by MFM. Depending on the shape of the Co dot, both in-plane and out-of-plane magnetic moments were observed.

A powerful non-perturbative theoretical method to study models of magnetization switching dynamics is Monte Carlo simulation. One standard model used to study uniaxial magnets is the kinetic Ising model  \( [16,17] \) . However, the Ising model can only be used as a reasonably realistic representation of extremely anisotropic uniaxial magnets, and a different model is required to capture the unique properties of biaxial materials. In this work we study a 4-state clock model with two perpendicular axes. In the most symmetric case there is no applied field and four states are equivalent. Suzuki has found a mapping between this symmetric 4-state clock model and two superimposed Ising models  \( [18] \) . When a field is applied, this symmetry is lost and o the results of extensive simulations of the switching dynamics. In order to simplify the analysis of the simulation results, we extend Suzuki's mapping to non-zero applied field and to the dynamics.

The rest of this paper is organized as follows. In Sec. II we describe the model used in the simulations. In Sec. III we briefly review the aspects of droplet theory used to analyze the numerical results. In Sec. IV and Sec. V we present and analyze our numerical results for lifetime and switching field, respectively. Finally, conclusions are
 

drawn in Sec. VI.

## II. MODEL DESCRIPTION

The 4-state clock model is defined by the microscopic Hamiltonian

 \[ \mathcal{H}=-J\sum_{\langle i,j\rangle}\vec{\mu}_{i}\cdot\vec{\mu}_{j}-\vec{H}\cdot\sum_{i}\vec{\mu}_{i}-A\sum_{i}(\vec{\mu}_{i}\cdot\vec{e}_{0})^{2}. \quad (1) \] 

The unit vector  \( \vec{\mu}_{i} \)  is the orientation of the spin at site i, which can be in one of 4 directions:  \( \vec{e}_{0} \) ,  \( \vec{e_{1}} \) ,  \( \bar{e_{2}} \) , and  \( \bar{e}_{3} \) , as shown in Fig. 1. The angle between the applied magnetic field  \( \vec{H} \)  and  \( \vec{e}_{0} \)  is  \( \theta \) . The dimensionless system magnetization is given by

 \[ \vec{m}=L^{-2}\sum_{i}\vec{\mu}_{i}. \quad (2) \] 

We consider a two-dimensional square lattice with L spins on each side, and periodic boundary conditions are applied in both directions to suppress boundary effects. (Boundary effects for the Ising model are discussed in Ref. [19].) The lattice constant is set to unity. In Eq. (1),  \( \sum_{i} \)  runs over all  \( L^{2} \)  sites, and  \( \sum_{\langle i,j\rangle} \)  runs over all nearest-neighbor pairs on the lattice. The first term in Eq. (1) is the energy due to exchange interactions between nearest-neighbor spins, and J > 0 is the ferromagnetic exchange interaction. The second term is the energy,  \( L^{2}\vec{H} \cdot \vec{m} \)  due to the applied field  \( \vec{H} \) . The third term represents the energy due to a different preference for one of the two axes,  \( \vec{e}_{0} - \vec{e}_{2} \)  and  \( \vec{e}_{1} - \vec{e}_{3} \) . If A = 0, the model has 4-fold symmetry for  \( \vec{H} = 0 \) , and the statics of this model is equivalent to two decoupled Ising models [18]. In Appendix A, this mapping is extended to non-zero fields and to the dynamics. A nonzero value of A destroys this 4-fold symmetry. Therefore, throughout this paper we refer to the model with  \( A \neq 0 \)  as asymmetric. (In the statistical mechanics literature, clock models with  \( A \neq 0 \)  are often referred to as “anisotropic.” However, in this paper we use the terms “anisotropy” and “anisotropic” as they are customarily understood in the literature on magnetic materials.) For A > 0 and  \( \vec{H} = 0 \) , the  \( \vec{e}_{0} - \vec{e}_{2} \)  axis is favorable energetically, while the  \( \vec{e}_{1} - \vec{e}_{3} \)  axis is preferred for A < 0.

![](./images/867761719210935115_1.jpg)

FIG. 1. Vector representation of the 4-state clock model.

The critical temperature,  \( T_{c} \) , of the model with A = 0 and  \( \vec{H} = 0 \)  is known exactly. Its value is  \( k_{\mathrm{B}}T_{c}/J = 1/\ln(1 + \sqrt{2}) \approx 1.135 \)  [18], exactly that of a two-dimensional square-lattice Ising model with interaction constant J/2. Here  \( k_{B} \)  is Boltzmann's constant. The simulation temperature is chosen to be  \( T = 0.8T_{c} \) . This simulation temperature is high enough to get a reasonable Monte Carlo acceptance rate, while it is low enough to avoid complications near the critical point such as critical slowing-down and finite-size effects [20]. Based on studies of the kinetic Ising model [16,21,22], simulation results at other moderately low temperatures should be qualitatively similar to those obtained here.

The initial configuration of the system is ordered, with  \( \vec{\mu}_{i} = \vec{e}_{0} \)  for all spins. This may be achieved by applying a strong field in the  \( \vec{e}_{0} \)  direction for time t < 0. Then at t = 0 the external magnetic field is changed to  \( \vec{H} \)  (Fig. 1). During the simulation, first one spin is selected at random, then a new candidate state is chosen. At low temperatures, large orientational changes of the spin ( \( \vec{e}_{0} \leftrightarrow \vec{e}_{2} \)  and  \( \vec{e}_{1} \leftrightarrow \vec{e}_{3} \) ) are very unlikely [23]. Consequently, the candidate state is obtained by rotating the spin by  \( 90^{\circ} \)  or  \( -90^{\circ} \) . The a priori probabilities of clockwise and anti-clockwise rotations are each set to 1/2.

The probability that the spin flips to the chosen state is given by Glauber dynamics [24]

 \[ W=\frac{\exp(-\beta\Delta E)}{1+\exp(-\beta\Delta E)}, \quad (3) \] 

where  \( \Delta E \)  gives the change in the energy of the system that would result if the spin flip were accepted, and  \( \beta = 1/k_{B}T \) . The Glauber dynamic is chosen because it can be derived from quantum mechanics under certain stringent conditions [25]. Here time is reported in the unit of one Monte Carlo steps per spin (MCSS).

The lifetime is defined as the average time,  \( \langle\tau\rangle \) , needed to satisfy a specific stopping criterion (discussed below), where  \( \tau \)  is the first-passage time to the stopping criterion for an individual Monte Carlo run. The average is taken over at least 1000 independent Monte Carlo runs in order to obtain good statistics. In addition to the mean, we also measure the relative standard deviation

 \[ r=\sqrt{\langle\tau^{2}\rangle-\langle\tau\rangle^{2}}/\langle\tau\rangle. \quad (4) \] 

The switching field is measured by observing whether on average the system magnetization has reversed after a fixed waiting time, here chosen as  \( t_{w} = 200 \)  MCSS. As Ising model studies have demonstrated [16,21], the switching fields for different waiting times are qualitatively similar.

To measure the lifetime of a metastable state, a criterion for escape from the metastable state must be chosen. In studies of the kinetic Ising model, the usual criterion is that an escape is registered and the simulation stopped the first time the magnetization reaches a fixed cutoff.
 

value,  \( m_{stop} \) . (In other words: the stopping time is the first-passage time to  \( m_{stop} \) .) Results for different values of  \( m_{stop \)  are significantly different only in the deterministic regime, and even in this regime the results are qualitatively similar [26].

In some experimental studies of magnetization switching, the sign of the magnetization along a particular direction is much easier to measure than its magnitude  \( [11,12] \) . The stopping criterion most directly relevant to these experiments is therefore to use  \( m_{stop} = 0 \) . For the Ising model, this is obtained by stopping the simulation when half of the spins have entered the stable state (and half have left the metastable state). For other experimental situations, a different criterion might be easier to measure. However the stopping criterion chosen should not have a large effect on the results.

In order to completely map the 4-state clock model onto two superimposed Ising systems (see Appendix A), the stopping criterion for the 4-state clock model must map onto the stopping criteria for the two individual Ising systems. If the stopping criteria for both Ising systems are given by  \( m_{stop} = 0 \) , two different stopping criteria for the 4-state clock model can be naturally envisioned. Denoting these by  \( S_{U} \)  and  \( S_{\cap} \) , they are given in terms of the first passage to the stopping parameter  \( \mu_{stop} \)  by

 \[ S_{\cup}\mathrm{h a s}\quad\mu_{\mathrm{s t o p}}=m_{I0}m_{I1} \quad (5) \] 

 \[ S_{\cap}\mathrm{h a s}\mu_{\mathrm{s t o p}}=1-\eta(-m_{I0})\eta(-m_{I1}), \quad (6) \] 

where each  \( m_{I\alpha} \)  for  \( \alpha = 0, 1 \)  is the time-dependent magnetization of one of the Ising systems and  \( \eta(x) \)  is the unit step function. The criterion  \( S_{\cup} \)  is to stop when the first Ising system reaches zero magnetization, while for  \( S_{\cap} \)  the simulation is continued until the last of the two Ising systems reaches zero magnetization.

The mapping between the clock model and the two Ising models illustrates that in order for a clock spin to escape from the initial state, only one of the two Ising spins on the site needs to flip, while both Ising spins on the same site must flip in order for the clock spin to enter the stable state. Therefore, for the clock model the  \( S_{\cup} \)  stopping criterion implies that  \( \geq \frac{1}{2} \)  of the clock spins have escaped from the initial state. The  \( S_{\cap} \)  stopping criterion means a certain fraction  \( (\leq \frac{1}{2}) \)  of the clock spins have entered the stable state. For the symmetric clock model, the two Ising models are decoupled, and their switching processes are independent of each other. Therefore, for  \( S_{\cap} \)  on average 1/4 of the clock spins will have entered the stable state at the time the simulation is stopped. In this paper, we use only the  \( S_{\cap} \)  stopping criterion since it more closely models an experimental stopping criterion of zero magnetization. For the asymmetric model, we also use this stopping criterion in order to observe the effects of A and  \( \bar{H} \)  consistently. In this case the average fraction of clock spins in the stable state at the end of the simulation is between 1/4 and 1/2, depending on A. A more detailed discussion of the quantitative differences between different stopping criteria is given in Ref. [27].

## III. DROPLET THEORY

During magnetization switching in single-domain particles, small “droplets” of the stable phase are continually created and destroyed by thermal fluctuations [16]. The fate of a droplet is determined by the competition between its total surface free energy, which is proportional to its surface area, and the coupling of its magnetization with the applied field, which is proportional to its volume. If the droplet is small, further growth produces an increase of the free energy due to the surface tension. Therefore, the droplet will be destroyed with high probability. If the droplet is sufficiently large, this free-energy penalty is offset by the benefit obtained from increasing the number of spins parallel to the applied magnetic field. Therefore the droplet is very likely to grow further. For a droplet with a critical radius  \( R_{c} \) , the tendencies towards growth and shrinkage balance, and the droplet will grow or shrink with equal probability. By comparing  \( R_{c} \)  with the system size L, the lattice spacing a, and the average distance between supercritical droplets  \( R_{0} \) , the magnetization switching dynamics is divided into four regimes [16,21,26,28]:

- The Coexistence (CE) regime  \( [a < L < R_{c}] \) , in which the switching is governed by subcritical fluctuations on the scale of the system size.

- The Single-droplet (SD) regime  \( [a < R_{c} < L < R_{0}] \) , characterized by switching via a single critical droplet. Once a supercritical droplet is nucleated, it will most likely grow to occupy the entire system before another droplet is nucleated.

- The Multi-droplet (MD) regime  \( [a < R_{c} < R_{0} < L] \) , characterized by switching via a finite density of critical droplets.

- The Strong-field (SF) regime  \( [a \simeq R_{c} \simeq R_{0} < L] \) , in which the concept of a droplet is no longer applicable.

Since the symmetric 4-state clock model is equivalent to two decoupled Ising models, we can simplify the analysis of the clock model based on extensive studies of kinetic Ising models  \( [16,21,28,26] \) . Here a brief review of the droplet theory for the Ising model is given. For more details, see the references listed above.

In the SD regime, the lifetime is given by

 \[ \tau_{\mathrm{I}}\approx\left[L^{d}\Gamma(T,H_{\mathrm{I}})\right]^{-1}, \quad (7) \] 

where  \( H_{I} \)  is the field in the Ising Hamiltonian, and the nucleation rate per unit volume  \( \Gamma(T, H_{\mathrm{I}}) \)  is [21]

 \[ \Gamma(T,H_{\mathrm{I}})\approx A(T)|H_{\mathrm{I}}|^{K}\exp\left[-\frac{\beta\Xi(T)}{|H_{\mathrm{I}}|^{d-1}}(1+O(H_{\mathrm{I}}^{2}))\right]. \quad (8) \]
 

Here  \( A(T) \)  is a non-universal prefactor, and K is believed to be 3 for two dimensional  \( (d=2) \)  Ising systems [21]. At  \( T=0.8T_{c} \) ,  \( \Xi(T)/J_{I}^{2}\approx0.92 \)  [21], where  \( J_{I} \)  is the exchange interaction in the Ising Hamiltonian.

In the MD regime, the system can be approximately partitioned into  \( (L/R_{0})^{d} \gg 1 \)  cells, each of which decays via an independent Poisson process with rate  \( R_{0}^{d}\Gamma \) . Therefore, the volume fraction is self-averaging, and the average lifetime  \( \langle\tau_{I}\rangle \) , defined as the average first-passage time to zero magnetization, is given by the well-known Avrami theory of metastable decay as [16,26]

 \[ \langle\tau_{\mathrm{I}}\rangle\propto\left[|H_{\mathrm{I}}|^{d}\Gamma(T,H_{\mathrm{I}})\right]^{-1/(d+1)}. \quad (9) \] 

By taking the derivative of the logarithm of  \( \langle\tau_{I}\rangle \)  with respect to  \( |J_{I}/H_{I}|^{d-1} \) , one obtains

 \[ \frac{\Lambda_{\mathrm{I e f f}}}{J_{\mathrm{I}}^{d-1}}\equiv\frac{d\ln\langle\tau_{\mathrm{I}}\rangle}{d(|\boldsymbol{J}_{\mathrm{I}}/H_{\mathrm{I}}|^{d-1})}=\lambda|H_{\mathrm{I}}/J_{\mathrm{I}}|^{d-1}+\frac{\Lambda}{J_{\mathrm{I}}^{d-1}}, \quad (10) \] 

with  \( \lambda = K/(d - 1) \)  and  \( \Lambda = \beta\Xi(T) \)  in the SD regime, while  \( \lambda = (K + d)/(d^{2} - 1) \)  and  \( \Lambda = \beta\Xi(T)/(d + 1) \)  in the MD regime [21,26].

For the symmetric 4-state clock model, if the applied field is along the  \( \vec{e}_{2} \)  direction, the applied field  \( H_{I} \)  and the exchange interaction  \( J_{I} \)  of the Ising model are related to the corresponding parameters for the clock model by  \( H_{I} = H/2 \)  and  \( J_{I} = J/2 \)  (Table I). By replacing the parameters for the Ising model by the corresponding ones for the clock model in the above analysis, we get the dimensionless value  \( \Lambda_{eff}/J^{d-1} \)  for the clock model, which is

 \[ \frac{\Lambda_{\mathrm{e f f}}}{J^{d-1}}=\frac{d\ln\langle\tau\rangle}{d(|\boldsymbol{J}/H|^{d-1})}=\lambda|H/J|^{d-1}+\frac{\Lambda}{(J/2)^{d-1}}, \quad (11) \] 

Since  \( J_{I} = 1/2J \) , comparing Eq. (10) and Eq. (11), we have

 \[ \Lambda_{\mathrm{e f f}}/J^{d-1}=\Lambda_{\mathrm{I e f f}}/J_{\mathrm{I}}^{d-1}. \quad (12) \] 

Therefore we can compare the simulation results for the symmetric 4-state clock model directly with the theoretical predictions for the Ising models. For the asymmetric clock model, we calculate the same derivative.

## IV. LIFETIME MEASUREMENTS

The statistical properties of the lifetime depend on the switching regime of the system. For an Ising system in the SD regime, the probability density of the lifetime is exponential  \( [16,21,26,28] \) 

 \[ p_{\mathrm{I}}(\tau)=\langle\tau_{\mathrm{I}}\rangle^{-1}\exp(-\tau/\langle\tau_{\mathrm{I}})\rangle, \quad (13) \] 

where  \( \langle\tau_{I}\rangle \)  is the mean lifetime. As discussed in Sec. II, for the 4-state clock model, magnetization switching, as defined by the stopping criterion used in this paper, implies that both constituent Ising lattices must have reached zero magnetization. Therefore, the lifetime of the clock model is the longer of the lifetimes of the two Ising models. If the applied field is in the  \( \vec{e}_{2} \)  direction, the two Ising systems are identical, and the probability density of the lifetime for the clock model can be simply written as

 \[ p_{\mathrm{c}}(\tau)=\langle\tau_{\mathrm{I}}\rangle^{-1}\exp(-\tau/2\langle\tau_{\mathrm{I}}\mathrm{)}\rangle[1-\exp(-\tau/2\langle\tau_{\mathrm{I}}\rangle)]\;. \quad (14) \] 

The mean and relative standard deviation of this distribution are  \( \langle\tau\rangle=3\langle\tau_{\mathrm{I}}\rangle \)  and  \( r=\sqrt{5}/3 \) , respectively. The derivation of  \( p_{\mathrm{c}}(\tau) \)  for the general case that  \( \vec{H} \)  is not parallel to  \( \vec{e}_{2} \)  is detailed in Appendix B with the general result given as Eq. (26).

In the MD regime, since the switching process of the Ising model is deterministic, based on the mapping between the Ising model and the 4-state clock model, the switching dynamics of the 4-state clock models is also deterministic. By “deterministic” we mean that the lifetime distribution is characterized by a very small relative standard deviation,  \( r \ll 1 \) . Figure 2 and Fig. 3 show  \( \langle\tau\rangle \)  and r as functions of the inverse applied field,  \( J/|H| \) , for different lattice sizes. In these measurements, the applied field  \( \vec{H} \)  is always parallel to  \( \vec{e}_{2} \) . In the panels showing r, the horizontal solid and dashed lines correspond to r = 1 and  \( r = \sqrt{5}/3 \) , respectively. As predicted, for the isotropic clock model, r approaches  \( \sqrt{5}/3 \)  as  \( |H| \)  decreases. Also shown in these figures are results for the asymmetric clock model. When the easy axis is along  \( \vec{e}_{0} - \vec{e}_{2} \)  (A > 0), the lifetime is longer than that of the symmetric model with the same applied field because a stronger field is needed to flip the spins from the metastable state  \( \vec{e}_{0} \)  to the intermediate states,  \( \vec{e}_{\perp} \)  and  \( \vec{e}_{3} \) . When the easy axis is along  \( \vec{e}_{1} - \vec{e}_{3} \)  (A < 0), however, the lifetime is shorter than that for the symmetric model in the MD regime, and longer in the SD regime. The lifetime distribution is wider in the SD regime, and r has a system size-dependent maximum for A < 0. In either case, as  \( |H| \)  decreases, the asymmetry dominates, and the two states along the easy axis are strongly favored over the other two states. Therefore for weak H we expect the asymmetric clock model to behave essentially like a single Ising model, so that r will approach unity.
 
![](./images/867761719210935115_2.jpg)

(a)

![](./images/867761719210935115_3.jpg)

(b)

FIG. 2.  \( \langle\tau\rangle \)  and r vs. J/ \( |H| \)  for L = 100.

![](./images/867761719210935115_4.jpg)

(a)

![](./images/867761719210935115_5.jpg)

(b)

FIG. 3.  \( \langle\tau\rangle \)  and r vs. J/ \( |H| \)  for L = 32.

In order to understand the switching process for the asymmetric model better, we show selected snapshots of the model during the simulations in Figs. 4-6. The darkest regions represent the initial state, the lightest ones represent the stable state, and the two intermediate shades of gray represent the intermediate states. The applied field is chosen so that r is near its maximum for A < 0 (Fig.2). For A > 0 (Fig. 4), there is only one channel for the model to switch the magnetization: first a droplet of one intermediate state is nucleated and grows quickly. Then a droplet of the stable state nucleates and grows on this intermediate background. This process is similar to single-droplet decay in the Ising model, except that there is no intermediate phase in the Ising model. For A < 0, however, two channels exist. In the slow channel (Fig. 5), the system first enters a uniform intermediate state, from which it takes a long time to nucleate a stable droplet. In the fast channel (Fig. 6), droplets in different intermediate states are formed simultaneously. As they meet, a stable droplet is quickly nucleated on their common boundary to decrease the free energy. Because of the existence of these two channels, the relative standard deviation of the lifetime becomes very large, exceeding unity, which is the maximum value for a single Ising model.
 
![](./images/867761719210935115_6.jpg)

(a)

![](./images/867761719210935115_7.jpg)

(b)

![](./images/867761719210935115_8.jpg)

(c)

![](./images/867761719210935115_9.jpg)

(d)

FIG. 4. One typical switching event for A/J = 0.025, L = 100,  \( |H|/J = 0.09 \) .  \( \tau = 66000 \)  MCSS.  \( \langle\tau\rangle = 25886 \)  MCSS, r = 0.82. The times for these four snap shots are t = 62010, 62681, 65130, and 65980 MCSS, respectively.

![](./images/867761719210935115_10.jpg)

![](./images/867761719210935115_11.jpg)

(a)

(b)

![](./images/867761719210935115_12.jpg)

(c)

![](./images/867761719210935115_13.jpg)

(d)

FIG. 5. One typical realization of decay via the slow channel for A/J = -0.025, L = 100,  \( |H|/J = 0.09 \) .  \( \tau = 44542 \)  MCSS.  \( \langle\tau\rangle = 5659 \)  MCSS, r = 3.02. The times for these four snap shots are t = 1100, 39960, 43130, and 44400 MCSS, respectively.

![](./images/867761719210935115_14.jpg)

(a)

![](./images/867761719210935115_15.jpg)

(b)

![](./images/867761719210935115_16.jpg)

(c)

![](./images/867761719210935115_17.jpg)

(d)

FIG. 6. One typical realization of decay via the fast channel for A/J = -0.025, L = 100,  \( |H|/J = 0.09 \) .  \( \tau = 1649 \)  MCSS.  \( \langle\tau\rangle = 5659 \)  MCSS, r = 3.02. The times for these four snap shots are t = 410, 820, 1230, and 1640 MCSS, respectively.

Figure 7 shows the derivatives of the logarithm of the lifetime with respect to  \( J/|H| \) ,  \( \Lambda_{eff} \)  of Eq. (10), for different system sizes. In this figure, the straight lines are the theoretical results obtained from Eq. (10). Indeed, for the symmetric clock model, our numerical results show good agreement with the theory. Note that there are no adjustable parameters used in obtaining the theoretical results. In the asymmetric cases, when the applied field is strong the effect of the asymmetry is small. For weak fields, the asymmetry dominates the switching process, and the results for the clock model cannot be mapped onto those for the Ising model. Unfortunately, we could not extend the simulations deep into this regime, due to the prohibitive computer resources required: it takes at least two months to simulate 1000 individual realizations for L = 100 and  \( J/|H| > 12.5 \)  (Fig. 2) on a single node of an IBM sp2 computer.
 
![](./images/867761719210935115_18.jpg)

(a)

![](./images/867761719210935115_19.jpg)

(b)

FIG. 7.  \( \Lambda_{eff}/J \)  vs.  \( |H|/J \) . The solid lines are the theoretical predictions for the Ising model from Eq. (10).

## V. SWITCHING-FIELD MEASUREMENTS

We define the switching field as follows. We apply a field  \( \vec{H} \)  to the system in the initial state for a chosen waiting time  \( t_{w} = 200 \)  MCSS. If the magnetization has switched N/2 times in N simulations, then the magnitude of the applied field is called the switching field,  \( H_{\mathrm{sw}}(t_{\mathrm{w}}) \) . We choose this definition in order to simulate qualitatively the experiment discussed in Ref. [11]. The relationship between the switching field and the coercivity is that in coercivity measurements, the applied field is changed sinusoidally or linearly [29], while in our simulation the applied field is reversed abruptly.

First we compare the switching field for the symmetric clock model and the Ising model. The switching field as a function of the system size L is illustrated in Fig. 8. Since the time scale of the clock model is twice that for the Ising model, the switching field for the Ising model is measured with waiting time  \( t_{w} = 100 \)  MCSS. In the MD regime, the lifetime for the symmetric clock model is twice that for the Ising model, thus the switching fields for the clock model and the Ising model are the same. In the stochastic regime, from Eq. (13) and Eq. (14), the lifetime for the clock model is three times that of the Ising model. Therefore, the switching field for the clock model is larger than that for the Ising model. Here we emphasize that the maximum shown in Fig. 8 is the result of different switching mechanisms dominating the decay in the CE, SD and MD regimes. It is not the effect of demagnetization since there are no dipole-dipole interactions in our Hamiltonian. For more detailed discussions of the dependence of  \( H_{sw} \)  on L,  \( t_{w} \)  and T in the Ising model, see Ref. [16].

![](./images/867761719210935115_20.jpg)

FIG. 8. Switching fields for the symmetric clock model and the Ising model.

Next we consider the effects of the asymmetry A on the switching field. The results are shown in Fig. 9. Again,  \( \vec{H} \)  is in the  \( \vec{e}_{2} \)  direction. When the easy axis is along  \( \vec{e}_{0}-\vec{e}_{2} \)  (A > 0), increasing A leads to a monotonic increase of the switching field. When A < 0, on the other hand, making A more negative decreases the switching field in the MD regime. However, in the SD regime different A shows little effect on the switching field.

![](./images/867761719210935115_21.jpg)

FIG. 9. Effect of A on  \( H_{sw} \)  for  \( \theta = 180^{\circ} \) 

The effect of the direction of the applied field on the
 

switching field is shown in Fig. 10. Here  \( H_{sw} \)  is shown as a function of L for different  \( \theta \)  at A = 0. The symmetric clock model is equivalent to two decoupled Ising models, and the field components acting on these two Ising systems change with  \( \theta \) . Thus the switching behaviors of the two Ising systems are different, and the switching of the clock model is determined by the slower one. Therefore  \( H_{sw} \)  increases as  \( \vec{H} \)  deviates further away from the  \( e_{2}^{c} \)  direction.

![](./images/867761719210935115_22.jpg)

FIG. 10. Effect of  \( \theta \)  on  \( H_{sw} \)  for A = 0.

Finally we have measured the  \( \theta \) -dependence of  \( H_{sw} \)  for two system sizes (L = 8 and L = 40) with different values of A. The results are shown in Fig. 11. When the direction of  \( \vec{H} \)  is close to  \( \vec{e}_{2} \) , the energetic preference for the two intermediate states is similar and mainly determined by the asymmetry. Therefore  \( H_{sw} \)  is governed by A. As  \( \theta \)  approaches  \( 135^{\circ} \) ,  \( \vec{H} \)  increases the stability of one intermediate state and decreases that of the stable state. When A < 0, this tendency is further amplified, therefore the switching field increases. For A > 0,  \( \vec{H} \)  makes the flip from  \( \vec{e}_{0} \)  to the favored intermediate state easier, whereafter A acts like an applied field in flipping the spin to  \( \vec{e}_{2} \) . Thus  \( H_{sw} \)  decreases compared with the isotropic model.

![](./images/867761719210935115_23.jpg)

(a)

![](./images/867761719210935115_24.jpg)

(b)

FIG. 11.  \( \theta \) - and A- dependence of the switching field for L = 8 and 40.

## VI. CONCLUSION

In this work we have studied magnetization switching in biaxial magnetic media by large-scale Monte Carlo simulation and theoretical analysis of a kinetic 4-state clock model. The model reduces the infinite anisotropy in the kinetic Ising model by introducing two intermediate magnetization directions between the magnetization states parallel and antiparallel to the applied field. If the two perpendicular axes are equivalent, the switching process is equivalent to that of two decoupled Ising models. With asymmetry, the clock model shows a more complicated switching behavior. When the axis along the initial state is favored (A > 0), the model becomes Ising-like. On the other hand, if the other easy axis is favored, the system can switch its magnetization via two different channels, which can lead to a wider distribution of the lifetimes in the SD regime. Another factor affecting the switching process is the direction of the applied field. We studied the direction dependence of the switching field in the isotropic model. With the applied field deviating further from the stable state, a stronger switching field is needed. The different switching mechanisms in the CE, SD, and MD regimes lead to a maximum switching field for a specific system size, in agreement with experimental results. We conclude that the 4-state clock model is a simple but informative platform to study the magnetization switching in biaxial magnetic particles.

## ACKNOWLEDGMENT

The authors wish to thank Dr. Howard L. Richards for proposing this study. We also thank Dr. S. M. Durbin, Dr. S. W. Sides, Dr. G. Korniss, Dr. H. L. Richards,
 

Dr. M. Kolesik and Dr. G. Brown for useful comments. This work is supported in part by the US National Science Foundation Grant No. DMR-9520325, and by Florida State University through the Supercomputer Computations Research Institute (US Department of Energy Contract No. DE-FC05-85ER25000) and the Center for Materials Research and Technology.

## APPENDIX A

In this appendix, the dynamical mapping between the Ising model and the symmetric 4-state clock model is derived.

First we define two unit vectors,  \( \vec{s}_{0} \)  and  \( \vec{s_{1}} \) , such that the angle between  \( \vec{s}_{0} \)  ( \( \vec{s_{1}} \) ) and  \( \vec{e}_{0} \)  is  \( -45^{\circ} \)  ( \( +45^{\circ} \) ) (Fig. 12). Let  \( \vec{\mu}_{i} \)  denote the direction of the clock spin at site i, which can be  \( \vec{e}_{0} \) ,  \( \vec{e_{1}} \) ,  \( \ell_{2} \) , or  \( \ell_{3} \) . The unit vector  \( \vec{\mu}_{i} \)  can be expressed in terms of  \( \vec{s}_{0} \)  and  \( \vec{s_{1}} \)  as

 \[ \vec{\mu}_{i}=\frac{1}{\sqrt{2}}(\omega_{0i}\vec{s}_{0}+\omega_{1i}\vec{s}_{1}), \quad (15) \] 

where  \( \omega_{0i} \)  and  \( \omega_{1i} \)  can take the values  \( \pm1 \) . The applied field can also be decomposed as

 \[ \vec{H}=H_{0}\vec{s}_{0}+H_{1}\vec{s}_{1}, \quad (16) \] 

where

 \[ H_{0}=|\vec{H}|\cos(45^{\circ}+\theta), \quad (17) \] 

 \[ H_{1}=|\vec{H}|\sin(45^{\circ}+\theta). \quad (18) \] 

![](./images/867761719210935115_25.jpg)

FIG. 12. Mapping of the 4-state clock model onto a superposition of two Ising models.

Substituting Eqs. (15)-(17) into Eq. (1), we get

 \[ \mathcal{H}=\mathcal{H}_{0}+\mathcal{H}_{1}, \quad (19) \] 

 \[ \mathcal{H}_{0}=-\frac{J}{2}\sum_{\langle i,j\rangle}\omega_{0i}\omega_{0j}-\frac{H_{0}}{\sqrt{2}}\sum_{i}\omega_{0i}, \quad (20) \] 

 \[ \mathcal{H}_{1}=-\frac{J}{2}\sum_{\langle i,j\rangle}\omega_{1i}\omega_{1j}-\frac{H_{1}}{\sqrt{2}}\sum_{i}\omega_{1i}. \quad (21) \] 

From these equations, it is clear that the Hamiltonian of the symmetric 4-state clock model is equivalent to the sum of two decoupled Ising Hamiltonians with exchange interactions J/2. The applied field in each Ising Hamiltonian equals the field component times  \( 1/\sqrt{2} \) . Therefore, the 4-state clock model in equilibrium can be treated as two superimposed Ising systems, with two Ising spins at each site [18].

The next step is to construct a mapping of the spin-flip dynamics between the 4-state clock model and the Ising models. Since each spin can only flip to its neighboring state, this can be done by choosing one of the two Ising systems randomly and flipping the corresponding Ising spin. Because each time only one Ising lattice is selected, the change of the energy due to the spin flip is obtained by updating either  \( H_{0} \)  or  \( H_{1} \)  in Eq. (19).

With the above analysis, it follows that the dynamics of the symmetric 4-state clock model is equivalent to that of two decoupled Ising models. Not only are the spin-flip mechanisms interchangeable, but also only one Ising Hamiltonian in Eq. (19) is affected in each flip because  \( H_{0} \)  and  \( H_{1} \)  are decoupled. Since each clock spin can be thought to be composed of two Ising spins, during the simulation the time scale for the 4-state clock model is twice that for the Ising model. The mapping of the parameters between the symmetric 4-state clock model and Ising models is summarized in Table I. In this table, t is the time measured in Monte Carlo steps per spin (MCSS).

TABLE I. Mapping between the symmetric 4-state Clock and Ising Models

<table><tr><td>Clock</td><td>Ising system #0</td><td>Ising system  \( \#1 \)</td></tr><tr><td>J</td><td>J/2</td><td>J/2</td></tr><tr><td>H</td><td>\( \frac{1}{\sqrt{2}}|H|\cos(45^{\circ}+\theta) \)</td><td>\( \frac{1}{\sqrt{2}}|H|\sin(45^{\circ}+\theta) \)</td></tr><tr><td>t</td><td>t/2</td><td>t/2</td></tr></table>
 

## APPENDIX B

In this appendix, the lifetime distribution for the isotropic 4-state clock model is derived. We denote the lifetimes of the two Ising models by  \( \tau_{0} \)  and  \( \tau_{1} \) , and the lifetime of the 4-state clock model by  \( \tau_{c} \) . With the stopping criterion used in this work, we have

 \[ \tau_{c}=2\max(\tau_{0},\tau_{1}). \quad (22) \] 

Thus, for a given value  \( \tau \)  of the lifetime, the probability that  \( \tau_{c} < \tau \)  can be written as

 \[ P(\tau_{c}<\tau)=P(\max(\tau_{0},\tau_{1})<\tau/2). \quad (23) \] 

Here the factor 2 comes from the mapping of the time scale between the clock and the Ising models given in Table I. Since the two Ising models are decoupled, the lifetime distributions are independent. Therefore

 \[ P(\tau_{c}<\tau)=P(\tau_{0}<\tau/2)\cdot P(\tau_{1}<\tau/2). \quad (24) \] 

In the SD regime, the lifetime of each Ising model is exponentially distributed,

 \[ P(\tau_{k}<\tau)=1-\exp(-\tau/\langle\tau_{k}\rangle), \quad (25) \] 

where k = 0, 1. Substituting Eq. (25) into Eq. (24) and differentiating with respect to  \( \tau \) , we obtain the probability density of the lifetime of the clock model as

 \[ \begin{aligned}p_{c}(\tau)=&\frac{\exp(-\tau/2\langle\tau_{0}\rangle)\left[1-\exp(-\tau/2\langle\tau_{1}\rangle)\right]}{2\langle\tau_{0}\rangle}\\&+\frac{\exp(-\tau/2\langle\tau_{1}\rangle)\left[1-\exp(-\tau/2\langle\tau_{0}\rangle)\right]}{2\langle\tau_{1}\rangle}.\end{aligned} \quad (26) \] 

If  \( \langle\tau_{0}\rangle=\langle\tau_{1}\rangle=\langle\tau\rangle \) , we get Eq. (14).

In the MD regime, since the magnetic switching is deterministic, the lifetime probability density of the Ising model is well approximated by a  \( \delta \) -function. Thus for the Ising model,

 \[ P(\tau_{1}<\tau)\approx\eta(\tau-\tau_{1}), \quad (27) \] 

where  \( \eta \)  is the unit step function. Following the same procedure as above we get the lifetime distribution for the clock model,

 \[ p_{c}(\tau)\approx\delta(\tau-2\max[\langle\tau_{0}\rangle,\langle\tau_{1}\rangle]). \quad (28) \] 

Finally we consider the case that the field is applied in such a direction that one Ising system is in the MD regime with average lifetime  \( \langle\tau_{MD}\rangle \) , and the other in the SD region with the average lifetime  \( \langle\tau_{SD}\rangle \) . Starting from Eq. (24), we then have

 \[ P_{c}(\tau_{c}<\tau)=\eta(\tau-2\tau_{\mathrm{M D}})[1-\exp(-\tau/2\langle\tau_{\mathrm{S D}}\rangle)], \quad (29) \] 

which yields

 \[ \begin{aligned}p_{c}(\tau)=&\left[1-\exp(-\langle\tau_{\mathrm{MD}}\rangle/2\langle\tau_{\mathrm{SD}}\rangle)\right]\delta(\tau-2\langle\tau_{\mathrm{MD}}\rangle)\\&+\frac{\exp(-\tau/2\langle\tau_{\mathrm{SD}}\rangle)}{2\langle\tau_{\mathrm{{SD}}}\rangle}\eta(\tau-2\langle\tau_{\mathrm{MD}}\rangle).\end{aligned} \quad (30) \] 

A more detailed calculation for the MD cases would replace the  \( \delta \) -functions by Gaussians and the step functions by the corresponding error functions [16], with no essential change from the approximate results given here.

[1] I. Klik, Y. D. Yao, and C. R. Chang, J. Appl. Phys. vol. 79, p. 4919 (1996).

[2] X. G. Ye and J. G. Zhu, IEEE Trans. Magn. vol. 28, p. 3087 (1992).

[3] J. G. Zhu, X. G. Ye, and T. C. Arnoldussen, IEEE Trans. Magn. vol. 29, p. 324 (1994).

[4] X. G. Ye and J. G. Zhu, J. Appl. Phys. vol. 75, p. 6135 (1994).

[5] B. Y. Wong, D. E. Laughlin, and D. N. Lambeth, IEEE Trans. Magn. vol. 27, p. 4733 (1991).

[6] M. Mirazamaani, C. V. Jahnes, and M. A. Russak, J. Appl. Phys. vol. 69, p. 5169 (1991).

[7] G. Q. Gong, A. Gupta, G. Xiao, P. Lecoeur, and R. McGuire, Phys. Rev. B vol. 54, p. 3742 (1996).

[8] U. Ebels et al, Phys. Rev. B vol. 56, p. 770 (1997).

[9] R. M. H. New, R. F. W. Pease and R. L. White, IEEE Trans. Magn. vol. 31, p. 3805 (1995).

[10] R. M. H. New, R. F. W. Pease, and R. L. White, J. Magn. Magn. Mater. vol. 155, p. 140 (1996).

[11] T. Chang, J. Zhu, and J. H. Judy, J. Appl. Phys. vol. 73, p. 6716 (1993).

[12] W. Wernsdorfer et al., J. Magn. Magn. Mater. vol. 151, p. 38 (1995).

[13] M. Lederman, S. Schultz, and M. Ozaki, Phys. Rev. Lett. vol. 73, p. 1986 (1994)

[14] A. Fernandez et al., IEEE Trans. Magn. vol. 32, p. 4472 (1996).

[15] M. Löhndorf et al., Z. Phys. B vol. 101, p. 1 (1996).

[16] H. L. Richards, S. W. Sides, M. A. Novotny, P. A. Rikvold, J. Magn. Magn. Mater. vol. 150, p. 37 (1995).

[17] R. Mélin, J. Magn. Magn. Mater. vol. 162, p. 2211 (1996).

[18] M. Suzuki, Prog. Theor. Phys. vol. 37, p. 770 (1967).

[19] H. L. Richards et al., Phys. Rev. B vol. 55, p. 11521 (1997).

[20] K. K. Mon and D. Jasnow, Phys. Rev. Lett. vol. 59, p. 2983 (1987).

[21] P. A. Rikvold and B. M. Gorman, in Annual Reviews of Computational Physics I., ed. by D. Stauffer, p. 149, World Scientific, Singapore (1994).

[22] P. A. Rikvold, M. A. Novotny, M. Kolesik, H. L. Richards, in Dynamical Properties of Unconventional Magnetic Systems, ed. by A. T. Skjeltorp and D. Sherrington, p. 307, Kluwer Academic, Netherlands (1998).

[23] K. Kaski, J. D. Gunton, Phys. Rev. B vol. 28, p. 5371 (1983).

[24] R. J. Glauber, J. Math. Phys. vol. 4, p. 294 (1963).
 

[25] Ph. A. Martin, J. Stat. Phys. vol. 16, p. 149 (1977).

[26] P. A. Rikvold, H. Tomita, S. Miyashita, S. W. Sides, Phys. Rev. E vol. 49, p. 5080 (1994).

[27] X. Kou, MS Thesis, Florida State University (1997).

[28] H. Tomita and S. Miyashita, Phys. Rev. B vol. 46, p. 8886 (1992).

[29] C. D. Mee and E. Denails eds., Magnetic Recording vol. 1: Technology. McGraw-Hill, New York (1986).
 
