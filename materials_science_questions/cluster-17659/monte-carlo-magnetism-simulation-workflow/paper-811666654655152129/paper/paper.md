# Cluster analysis of an Ising-Preisach interacting particle system

Cristian Rotarescu, Iulian Petrila, Alexandru Stancu*

Alexandru Ioan Cuza University of Iasi, Department of Physics & CARPATH, Blvd. Carol I, nr. 11, Iasi 700506, Romania

---

## ARTICLE INFO

**Article history:**
Received 6 July 2010
Received in revised form
1 March 2011
Accepted 11 March 2011
Available online 17 March 2011

**Keywords:**
Ising model
Preisach model
Magnetic relaxation
Dipolar interactions

## ABSTRACT

The paper deals with the analysis of clusters' size in diverse magnetization states of a system of ferromagnetic particles organized in a perfect 2D array with all the anisotropy axes perpendicular to the plane (perpendicular medium) following the evolution of the clusters in correlation with various parameters like applied field or interaction strength. We present numerical simulations for a two-level Ising-type model each magnetic entity being characterized by a Stoner-Wohlfarth nonlinear energy barrier and a rectangular hysteresis loop (Ising-Preisach hysteron). In the simulations we took into account, the long-range inter-particle magnetostatic interactions in an attempt to mimic as accurately as possible with a still simple model, materials like Bit-Patterned media that are now considered as good candidates for the magnetic memories of the future.

© 2011 Elsevier B.V. All rights reserved.

---

### 1. Introduction

The study of recording materials properties is of paramount importance because these materials should exhibit persistent memory in the technological applications [1,2]. As the physical phenomena involved in a process are really complex there is a significant interest in the development of simple models that can describe the essential aspects of these phenomena, which also allows a numerically efficient implementation.

The simplest physical model of ferromagnetism, the Ising model [3], considers as the fundamental magnetic brick a bistable entity, without hysteresis. This entity can be found in one of the two possible equilibrium states (we can call them "up" and "down"). The magnetic fundamental entities in the Ising model usually have only exchange interactions with the closest neighbors. Due to these interactions the entire ensemble may show hysteresis.

The representation of ferromagnetic materials as a superposition of elementary bistable subsystems was also used by Preisach [4] for the description of history-dependent phenomena like the ferromagnetic hysteresis [5,6]. In this model the simplest magnetic entity is characterized by a rectangular hysteresis loop named hysteron. The intrinsic coercivity of the hysteron is due to anisotropy, which is a fundamental property in ferromagnetism. It has been shown that very small ferromagnetic particles have a hysteretic behavior very similar to the one considered in the Preisach model (e.g. Stoner-Wohlfarth model for single-domain uniaxial particle [7]). When the field is applied along the easy axis of the single-domain particle, the hysteresis loop of the particle is identical with a Preisach hysteron.

In Ising models using Preisach-type hysterons, like the Random Anisotropy (or Coercivity) Ising Model (RAIM/RCIM), the inter-particle interactions taken into account can be ferro or antiferromagnetic in essence [8,9].

In the model we have implemented here (named Ising-Preisach) essentially we consider within an Ising-type model a Preisach-type hysteron as fundamental entity of magnetism; the magnetic moments interact with long-range magnetostatic interactions.

In the evaluation of these very diverse models using similar fundamental bricks with the aim of maintaining the original simplicity of the model we are analyzing the clusters formation during various magnetization processes.

Cluster algorithms [10-12] have been successfully used to overcome slow dynamics in the Monte-Carlo simulations. To identify clusters of spins, algorithms like Swendsen and Wang [10] and Kasteleyn-Fortuin [13] representation have been used.

The problem of critical slowing down of local update algorithms at continuous phase transitions can be overcome by non-local update algorithms in which whole clusters of spins are flipped in a coherent way [14]. This leads to a more efficient sampling of long-wavelength fluctuations than in local update schemes. There are two related formulations available: the Swendsen-Wang formulation, in which the whole lattice is divided into clusters, and Wolff's single cluster (1C) formulation, where the evolution of a single cluster is studied. The tests of these algorithms for the Ising type model showed that the problem of critical slowing down is significantly reduced [15-17].

---

*Corresponding author.
E-mail address: alstancu@uaic.ro (A. Stancu).

0921-4526/$ - see front matter © 2011 Elsevier B.V. All rights reserved.
doi:10.1016/j.physb.2011.03.026

We present the clusters distribution corresponding to several types of demagnetized states and processes starting from these demagnetized states, which are analyzed as a function of temperature and interaction intensity between the magnetic entities.

These results may prove to be of interest in many particular cases. For example, the importance of the demagnetization type in the Henkel plots and deltaM curves that are still extensively used in the evaluation of the intensity and type of magnetic interactions (exchange and/or magnetostatic) has been documented [18]. A physical model, even a simple one, which can account for this effect would be of considerable interest.

In Section 2 we present the model that has been implemented and in Section 3 the simulation results are shown and then discussed.

## 2. The model

As we have already mentioned, the fundamental entity in the Ising-Preisach model is a rectangular hysteron with intrinsic coercivity. The hysteron coercivity can be linked to the particles' anisotropies. When the particles are non-interacting, their hysteresis loop shows a symmetry with respect to the origin of the (H, m) system (see Fig. 1 when $H_S$=0). As a result of the interaction field created by all the neighbor particles the hysteresis loop is shifted along the field axis with a value equal to this field ($H_S$), as it can be seen in Fig. 1.

In Fig. 1 the rectangular hysteresis loop of a Preisach hysteron is shown, where the positive switching field is $H_\alpha$, the negative switching field is $H_\beta$, $H_k$ is the coercive field of particle, $H_S$ is the shift of the rectangular hysteresis loop along the field axis and $m_S$ is the saturation magnetic moment.

In the static case (the zero Kelvin approximation) the switches can occur only at the positive and negative switching fields as shown in Fig. 1. At higher temperatures the time required to overcome an energy barrier $\Delta E$ at temperature $T$ can be estimated in the Arrhenius-Néel approximation as $\tau=\tau_0 \exp (\Delta E / k_B T)$ [19], where $\tau_0$ is a characteristic microscopic time (typically assumed to be between $10^{-12}$ and $10^{-9} \mathrm{~s}$). In the present case the energy barrier can be calculated with the well-known Stoner-Wohlfarth model [7]. In this model based on the idea that under a certain critical volume of one ferromagnetic particle all the microscopic magnetic moments within the particle are acting together in a coherent way (the model is also named "coherent rotations") if the easy axis is aligned to the field direction, the free energy of a particle can be written as

$$
E=-K V \cos ^2 \theta-V P_S H \cos \theta \tag{1}
$$

where $K$ is the anisotropy constant, $V$ is the particle volume, $P_S$ is the saturation polarization, $H$ is the external magnetic field parallel to the easy axis and $\theta$ is the angle between the polarization vector and the easy direction.

The equilibrium positions of the polarization vector of the particle can be determined by minimizing the free energy, i.e. $d E / d \theta=0$, which gives successively

$$
-2 K V \cos \theta(-\sin \theta)+V P_S H \sin \theta=0 \tag{2}
$$

and

$$
V P_S\left(H_k \cos \theta+H\right) \sin \theta=0 \tag{3}
$$

where $H_k=2 K / P_S$ is the anisotropy field. The solutions of Eq. (3) are $\theta_{1,2}=0, \pi$ corresponding to the stable equilibrium positions (polarization vector parallel and antiparallel, respectively, with respect to the applied field direction) and $\theta_m=\arccos \left(-H / H_k\right)$ corresponding to the unstable equilibrium orientation. The particle's free energy in the equilibrium states is given by

$$
E(\theta=0)=-\frac{V H_k P_S}{2}-V H P_S, \quad E(\theta=\pi)=-\frac{V H_k P_S}{2}+V H P_S \tag{4}
$$

$$
E\left(\theta_m\right)=-\frac{V H_k P_S}{2} \frac{H^2}{H_k^2}+V H P_S \frac{H}{H_k}=\frac{V P_S}{2} \frac{H^2}{H_k}
$$

The height of the energy barrier corresponding to the magnetic moment vector orientation out of the field direction and into the field direction is given by

$$
\Delta E_{ \pm}=\frac{V P_S}{2} H_k\left(1 \pm \frac{H_{e f f}}{H_k}\right)^2 \tag{5}
$$

where the energy barrier delimitations can be shown in Fig. 2.

![](./images/811666654655152129_1.jpg)

Fig. 1. Rectangular hysteresis loop (Preisach hysteron).

When a system of interacting single-domain ferromagnetic particles is studied one has to take into account the field acting on each particle magnetic moment given by an effective field $H_{eff}=H+H_{int}$ where $H$ is the external applied field and $H_{int}$ is the interaction field created by the other magnetic particles.

The system we have considered in simulations is characterized by a Gaussian distribution of the hysterons' intrinsic anisotropy.

We have studied a 2D Ising-Preisach system, which is a square lattice with the magnetic moments and easy axes aligned perpendicular to the surface.

The magnetic moment of each particle was calculated as for a Cobalt sphere with the radius $r=5 \mathrm{~nm}$. The system is characterized by a lattice constant " $a$ ". We have used the following values for the material constants of Cobalt: the anisotropy constant $K=4.1 \times 10^5 \mathrm{~J} / \mathrm{m}^3$ and the saturation polarization $P_S=1.78 \mathrm{~T}[20]$.

The particles are interacting magnetostatically and a dipolar approximation was used [21,22] for the interaction field

$$
\vec{H}_p=-\frac{1}{4 \pi} \sum_{q \neq p} \frac{\vec{m}_q}{R_{p q}^3} \tag{6}
$$

where $\vec{R}_{p q}$ is the position vector of the particle " $p$ " with respect to the particle " $q$ ", $m_q=V_q P_S$ is the magnetic moment of " $q$ " particle and $V_q$ is the particle volume.

![](./images/811666654655152129_2.jpg)

Fig. 2. Stoner-Wohlfarth energy barrier.

![](./images/811666654655152129_3.jpg)

Fig. 3. The variation of the magnetization for different types of demagnetizations.

A standard Monte-Carlo-Metropolis procedure was used to simulate the time and the temperature dependence of the magnetic moment of the system considering an algorithm described by Binder [23-25]. The algorithm has the following steps:

- Select randomly one lattice site $i$ at which the moment $m_i$ is considered for flipping $(m_i \to -m_i)$. We calculate the interaction field $H_{int}$ and after the effective field $H_{eff}$.
- Compute the energy barrier $\Delta E_+$ (which correspond to the flip "up" to "down") or $\Delta E_-$ (for the flip "down" to "up") for each particle given by the Stoner-Wohlfarth model (5).
- Calculate the transition probability $P$ for that flip
$$
P=\exp \left(-\frac{\Delta E_{\mp}}{k_{B} T}\right) \tag{4}
$$
- One generates a random number $Z$ with a generator that gives uniformly distributed random numbers between zero and one.
- If $Z < P$ the moment switches, otherwise it maintains the same orientation.
- We repeat these steps typically ten times until the entire lattice obtain the stable equilibrium.

In this manner the Metropolis algorithm was used to calculate the magnetization of the system. In some particular cases which will be described in details we have performed an analysis of the clusters dimension, which is presented in the next section.

First, we have analyzed the most common experimental demagnetization processes like the A.C., thermal, natural and demagnetization in constant field (Fig. 3). For each of the demagnetized state a clusters diagram was calculated. The clusters are counted by the Swendsen-Wang algorithm [26]. A slightly different cluster algorithm has been proposed by Wolff, where a spin is chosen at random and the evolution of a single cluster constructed around it, using same bond probabilities as in the Swendsen-Wang algorithm [27] is followed.

The cluster order, introduced to describe the cluster size and noted with "c", is defined as the number of particles from a cluster and was systematically evaluated in different states during a magnetization process.

One can estimate $m_c=P_c/P_S$ as the normalized total magnetization of clusters, where $P_c$ is the polarization of "c" order clusters.

In the simulations the magnetic field was normalized to the mean anisotropy field $_{HK0}$=$2K/P_S$ by $h=H/H_{K0}$ and the normalized magnetization is $m=P/P_S$. The coercive field distribution is described by the standard deviation $H_{K\sigma}$ that is a fraction of the average coercive field of the particles in the system ($H_{K\sigma}$=$0.1H_{K0}$). All the time evaluation in the simulations was made in Monte-Carlo Steps (MCS). A MCS is the characteristic time for the system updated after a number of steps equal to the number of particles in the system.

### 3. Numerical simulations and the cluster analysis

First we have studied the demagnetized states of the 2D Ising-Preisach system, with a special emphasis on their influence on several magnetization curves. The evolution of the clusters' dimensions was analyzed on equilibrium states calculated with the model.

For a relevant cluster analysis one has to demagnetize the system in different ways and then to analyze at the microscopic level the clusters distributions.

To obtain demagnetization in alternative applied field (known as A.C. demagnetization), a gradually decreasing alternating magnetic field $H^{(A.C.)}=15\times 10^{5}e^{-0.015t}\cos(2\pi ft)$ [A/m] is applied to the system and the magnetization is going to zero as the amplitude of the alternative field tends to zero. In simulations we have considered the lattice constant $a$=10 nm, the temperature $T$=300 K and the A.C. frequency $f$=$0.07\ \text{MCS}^{-1}$.

In the thermal demagnetization the sample is heated up to the Curie temperature (in simulations $T_c$=900 K) in zero field and, after that, one decreases the temperature down to the room temperature ($T$=300 K).

For the D.C. demagnetization one starts in the positive saturation and after that a constant field is applied in order to obtain zero total moment when the applied field is reduced to zero (remanent coercive field of the sample).

Essentially one may also obtain zero magnetic moment in zero field if one waits long enough in this state ($t$=5000 MCS). We have called this type of demagnetization "natural demagnetization".

The different kinds of demagnetizations were done at the temperature $T/T_c$=0.3. We can note that the clusters distributions depend strongly on these parameters.

In Fig. 4 the clusters distributions in the sample in every demagnetized state are represented. One can observe that the A.C. and D.C. demagnetization cause the appearance of smaller clusters when compared with thermal and natural demagnetized states where the probability of bigger clusters appearance is higher.

![](./images/811666654655152129_4.jpg)

Fig. 4. Plot of the clusters diagram in logarithmic scale of the clusters order $c$ for different type of demagnetizations ($T$=300 K).

![](./images/811666654655152129_5.jpg)

Fig. 5. First magnetization curve for different demagnetization types ($T$=300 K).

Also we observe a uniform distribution of the clusters in a natural demagnetization comparison with other types of demagnetizations.

Starting from these demagnetized states one can calculate the first magnetization curve to observe in what degree its shape is influenced by the initial demagnetized state.

As shown in Fig. 5 the demagnetization type are influencing the first part of the magnetization curves practically by increasing the initial susceptibility of the system, especially for the natural demagnetization when the system has the initial susceptibility higher than other types of demagnetizations.

If the A.C. demagnetization is obtained with A.C. fields of different frequency one can also observe that the clusters formation depends on the frequency when the amplitude is decreased with the same factor after one period of time (see Fig. 6).

In Fig. 7 the evolution of the total moment of clusters as a function of their order (logarithmic scale) on the virgin magnetization curve is shown.

![](./images/811666654655152129_6.jpg)

Fig. 6. Clusters formation function of the frequency in the A.C. demagnetization ($T$=300 K, $f_0$=0.07 MCS$^{-1}$).

![](./images/811666654655152129_7.jpg)

Fig. 7. Clusters evaluation for different fields in a first magnetization curve ($T$=300 K).

![](./images/811666654655152129_8.jpg)

Fig. 8. Dependence on the interactions via particles distance in the first magnetization curve (T=300 K).

![](./images/811666654655152129_9.jpg)

Fig. 9. Clusters distribution in zero field for various interactions fields that correspond to different particle distances (T=300 K).

We used A.C. demagnetization as an initial state (in Fig. 7, the $h=0$ line corresponds to the line for the A.C. demagnetization from Fig. 4). The moment is measured for different applied fields to the sample. Obviously, the saturation is obtained if a sufficiently high field is applied.

The diagram of clusters on the virgin magnetization curve shows an increase in the weight of higher order clusters as the system goes towards positive saturation.

As we can identify the intensity of inter-particle interactions as the fundamental physical factor in the distribution of cluster sizes we have also performed a series of simulations in order to evaluate the correlations between interactions and cluster size distribution at the room temperature by modifying the lattice constant $a$ (see Fig. 8). One use in the next figures the normalized form $d=a/a_0$, with $a_0=10$ nm.

The magnetization curves presented in Fig. 8 have started from A.C. demagnetized states. In simulations only the network constant was changed to modify of the inter-particle interaction fields.

The clusters diagram for various interactions fields are shown in Fig. 9. As it is shown in Fig. 9 for strong interactions $(d=1.0)$ the lower order clusters are predominant and for weak interaction field $(d=1.4)$ the bigger clusters are more probable.

As an effect of interactions, we have a switch of neighbor particles. Even if the particles are well separated by various techniques, the long-range magnetostatic interactions can not be avoided and they are essentially influencing the system behavior. As the system simulated and discussed in this paper mimic very well a Bit-Patterned recording medium this aspect of the probability of correlated switches due to interactions is evidenced clearly in our study.

## 4. Conclusions

We have performed a cluster analysis of the Ising-Preisach hysteron systems with magnetostatic interactions. In the first set of simulations one has studied the cluster distribution in demagnetized states obtained in various ways.

The interaction effects on the first magnetization curve give information about the clusterization evolution inside of the system when it advances towards saturation.

The effects of long-range magnetostatic interactions on the magnetization processes in nanostructured materials continue to pose a significant challenge as the technology requires continuously higher and higher densities that can be obtained with smaller magnetic entities in a very dense matrix. In this paper we show how the cluster distribution analysis can be linked to the effect of magnetostatic interactions in a Bit-Patterned like medium.

## Acknowledgments

The authors acknowledge the financial support received from IDEI FASTSWITCH 1994-CNCSIS Romania Grant.

## References

[1] E. Della Torre, L.H. Bennett, C.E. Korman, Physica B 403 (2008) 271.
[2] L.G. Rizzi, N.A. Alves, Physica B 405 (2010) 1571.
[3] E. Ising, Z. F. Phys. 31 (1925) 253.
[4] F. Preisach, Z. Phys. 94 (1935) 277.
[5] M. Enomoto, et al., Physica B 404 (2009) 642.
[6] G. Bertotti, Hysteresis in Magnetism, Academic Press, 1998.
[7] E.C. Stoner, E.P. Wohlfarth, Philos. Trans. R. Soc. A 240 (1948) 599.
[8] C. Enachescu, A. Dobrinescu, A. Stancu, J. Magn. Magn. Mater. 322 (2010) 1368.
[9] O. Hovorka, G. Friedman, J. Magn. Magn. Mater. 290-291 (2005) 449.
[10] R.H. Swendsen, J.S. Wang, Phys. Rev. Lett. 58 (1987) 86.
[11] U. Wolff, Phys. Rev. Lett. 60 (1988) 1461.
[12] Y. Tomita, Y. Okabe, Phys. Rev. Lett. 86 (2001) 4.
[13] P.W. Kasteleyn, C.M. Fortuin, J. Phys. Soc. Jpn. (1969) 11 Suppl. 26.
[14] R.H. Swendsen, R.S. Wang, A.M. Ferrenberg, The Monte Carlo Method in Condensed Matter Physics, Springer, 1992.
[15] W. Janke, M. Katoot, R. Villanova, Phys. Rev. B 49 (1994) 9644.
[16] S. Aktas, O. Gazioglu, Physica B 405 (2010) 678.
[17] L. Jiang, J. Zhang, Z. Chen, Q. Feng, Z. Huang, Physica B 405 (2010) 420.
[18] P. Mitchler, R. Roshko, E. Dahlberg, IEEE Trans. Magn. 34 (1998) 4.
[19] L. Néel, J. Phys. Radium 11 (1950) 49.
[20] B.D. Cullity, C.D. Graham, Introduction to Magnetic Materials, John Wiley & Sons, 2009.
[21] R. Tanasa, C. Enachescu, A. Stancu, J. Linares, F. Varret, Physica B 343 (2004) 314.
[22] S.J. Blundell, Physica B 404 (2009) 581.
[23] N. Metropolis, A.W. Rosenbluth, M.N. Rosenbluth, A.H. Teller, J. Chem. Phys. 21 (1953) 1087.
[24] K. Binder, D.W. Heermann, Monte-Carlo Simulation in Statistical Physics, Springer-Verlag, 1997.
[25] R. Chantrell, A. Lyberatos, M. El-Hillo, K. O'Grady, J. Appl. Phys. 76 (1994) 6407.
[26] J.S. Wang, R.H. Swendsen, Physica A 167 (1990) 565.
[27] U. Wolff, Phys. Rev. Lett. 62 (1989) 361.