
# Effect of next-nearest neighbor interactions on the dynamic order parameter of the Kinetic Ising model in an oscillating field

William D. Baez \( ^{1} \)  and Trinjanan Datta \( ^{1} \) 

 \( ^{1} \) Department of Chemistry and Physics, Augusta State University, Augusta, GA 30904 (Dated: September 11, 2021)

We study the effects of next-nearest neighbor (NNN) interactions in the two-dimensional ferromagnetic kinetic Ising model exposed to an oscillating field. By tuning the interaction ratio  \( (p = J_{NNN} / J_{NN}) \)  of the NNN  \( (J_{NNN}) \)  to the nearest-neighbor (NN) interaction  \( (J_{NN}) \)  we find that the model undergoes a transition from a regime in which the dynamic order parameter Q is equal to zero to a phase in which Q is not equal to zero. From our studies we conclude that the model can exhibit an interaction induced transition from a deterministic to a stochastic state. Furthermore, we demonstrate that the systems' metastable lifetime is sensitive not only to the lattice size, external field amplitude, and temperature (as found in earlier studies) but also to additional interactions present in the system.

PACS numbers: 64.60.Ht, 64.60.Qb, 75.10.Hk, 75.40.Gb, 05.40.-a

## I. INTRODUCTION

The two-dimensional (2D) ferromagnetic nearest-neighbor kinetic Ising (NNKI) model in an oscillating field has been used extensively to study non-equilibrium (NEQ) properties [1, 2]. The presence of an oscillatory field introduces an explicit time dependence in the Hamiltonian. This causes the system to exhibit a hysteretic response. Below the critical temperature ( \( T_{c} \) ) the system exhibits a dynamic phase transition (DPT) or stochastic resonance (SR) [1-5] based upon the strength of the field amplitude ( \( h_{0} \) ), frequency (f), temperature (T) of the system, and the lattice size (L). These parameters dictate whether the system will be in a deterministic or a stochastic regime. These regimes are further subdivided into one of the four possible regions: strong field (SF) and multi-droplet (MD) for deterministic, single-droplet (SD) and co-existence (CE) for stochastic. The SF and the MD regions exist for strong fields/large system sizes and the SD exists for weak fields/small system sizes [2]. The MD and SD regions have been studied exhaustively for metastability mechanisms, finite-size scaling effects, DPT, SR, hysteresis exponents, universality, critical exponents, and effect of square-wave oscillating external field with a soft Glauber dynamics [3-8].

A measure of the DPT is given by the dynamic order parameter, Q, which is the period-averaged magnetization. The DPT occurs between an ordered dynamic phase with  \( \langle|Q|\rangle\neq0 \)  and a disordered dynamic phase with  \( \langle|Q|\rangle=0 \)  [2] (only in the MD region). The DPT in the NNKI model is of second order [2–4]. Recently, evidence for a dynamic phase transition has been investigated experimentally in  \( [Co/Pt]_{3} \)  magnetic multilayers [9]. Furthermore, Monte Carlo simulations and mean-field studies of hysteresis in the NNKI model show that the loop area undergoes a transition from a symmetric shape to an asymmetric shape or vice-versa [1, 10]. The breakdown in the shape of the hysteresis loop has also been attributed to a DPT with a spontaneously broken symmetric phase [1]. The scaling relations for the hysteresis loop area have been measured in ultrathin and thin ferromagnetic film systems such as Fe/Au(001) [11],  \( Fe_{20}Ni_{80} \)  [12], and Co/Cu(001) [13]. In the SR region the magnetization switches through random nucleation of a single droplet of spins aligned with the applied field. This region has been studied for stochastic hysteresis using time-dependent nucleation theory and a variable rate Markov processes [6].

In this paper we extend the NNKI model to include next-nearest neighbor (NNN) ferromagnetic interactions. We term this model the next-nearest neighbor kinetic Ising (NNNKI) model (see Eq. 1). The motivation behind this investigation is to study the effects of additional (NNN) interactions in the system. In Sec. II we state the NNNKI model and describe the Monte Carlo method used. In Sec. III we present our results on the NNNKI model. In Sec. IV we discuss the results and state the main conclusions of our paper.

## II. MODEL AND METHOD

The model used in this study is the kinetic NNN Ising ferromagnet on a square lattice with periodic boundary conditions. The NNNKI Hamiltonian is given by

 \[ H=-J_{n n}\sum_{\langle i,j\rangle}S_{i}S_{j}-J_{n n n}\sum_{[i,j]}S_{i}S_{j}-h_{o}\sin(2\pi f t)\sum_{i}S_{i}, \quad (1) \] 

where  \( S_{i} \)  is the ith spin and can have values of  \( S_{i} = \pm 1 \) ,  \( J_{nn} \)  is the NN coupling,  \( J_{nnn} \)  is the NNN coupling,  \( h_{o} \)  is the external field amplitude, and f is the frequency of the external field. The sums  \( \sum_{\langle i,j\rangle} \)  and  \( \sum_{[i,j]} \)  run over all NN and NNN pairs, respectively. Both the couplings are ferromagnetic,  \( J_{nn} > 0 \)  and  \( J_{nnn} > 0 \) . The ratio of the couplings is defined as  \( p = J_{nnn}/J_{nn} \) . The spin-flip dynamics used is the Metropolis algorithm with the Monte Carlo step per spin (MCSS) as the unit time step [14]. The system is allowed to be in contact with a
 

heat bath at temperature T, and each attempted spin flip from  \( S_{i} \rightarrow -S_{i} \)  is accepted with the probability  \( W(S_{i} \rightarrow -S_{i}) = \exp(-\beta \Delta E_{i}) \) . Here  \( \Delta E_{i} \)  is the change in energy of the system that would result if the spin flip were accepted and  \( \beta = 1/k_{B}T \)  where the Boltzmann constant  \( k_{B} \)  is set equal to one. Using the above Hamiltonian (Eq. 1) and the Monte Carlo method we compute the dynamic order parameter Q

 \[ Q=\frac{\omega}{2\pi}\oint m(t)d t, \quad (2) \] 

![](./images/867749545851749097_1.jpg)

![](./images/867749545851749097_2.jpg)

FIG. 1: For L = 128,  \( h_{o} = 0.5J_{nn} \)  (where  \( J_{nn} = 1 \) ),  \( f = 10^{-3} \) , and  \( T = 0.8T_{c}^{NN} \)  we have (a) Magnetization time series data demonstrating the deterministic to stochastic transition for interaction ratio p = 0 - 0.4. The solid line represents the systems magnetization and the dashed line is the external field. (b) Spontaneous symmetry breaking of the hysteresis loops for the same set of interaction ratios as in part (a).

## III. RESULTS

## A. Interactions and their effects

In all the previous studies involving the NNKI model the frequency, magnetic field or temperature was used as the tuning parameter to demonstrate a transition between the stochastic to deterministic region. This allowed the study of SR or DPT based upon the system size and field amplitude. Our goal in this section is to demonstrate that the deterministic to stochastic transition can also be achieved by tuning the interactions. In our computation we choose a set of  \( (h_{o}, f, T) \)  values so that the system is in the deterministic MD region in the NN model. We take  \( h_{o} = 0.5J_{nn} \) ,  \( f = 10^{-3} \) , and  \( T = 0.8T_{c}^{NN} \) . A choice of  \( (h_{o}, f, T) \)  so that the system is in stochastic region is also equally valid. We then change the values of interaction ratio, p, and compute the magnetization time series data for several values of p (see Fig. 1(a)). In our calculations we take p to range from 0 to 0.4. This range of parameters is sufficient to high-where  \( m(t) \)  is the time dependent magnetization per unit site. In the next two sections we study the physics of the NNNKI model.

![](./images/867749545851749097_3.jpg)

![](./images/867749545851749097_4.jpg)

![](./images/867749545851749097_5.jpg)

light the physics of the problem. From the magnetization time series data we see that the system makes a transition from a deterministic to a stochastic region. For the same values of p we plot the hysteresis loops which show the spontaneous symmetry breaking (see Fig. 1(b)). We also track the values of the dynamic order parameter  \( \langle|Q|\rangle \)  (see Fig. 2) and we find that the value of  \( \langle|Q|\rangle \)  changes from zero to a non-zero number with increasing p. The system is therefore sensitive to NNN interactions. This sensitivity can be physically explained by considering the effect of interactions on the metastable lifetime.

## B. Metastable lifetime, \(\tau(h_{0}, T, L, p)\)

The key to understanding the observed phenomena in the NNNKI model is to study the metastable lifetime. To determine  \( \tau \)  for this model we performed several instantaneous field reversal simulations [15]. The system was initially prepared in an all up spin configuration. The field was instantaneously reversed and the relaxation of the system then studied. The metastable lifetime is the
 
![](./images/867749545851749097_6.jpg)

FIG. 2: Tracking the dynamic order parameter,  \( \langle|Q|\rangle \) , as the interaction ratio,  \( p = J_{nnn}/J_{nn} \) , is changed. The value of  \( \langle|Q|\rangle \)  changes from a zero to a non-zero number. The lattice sizes are  \( L=64, 72, 96, \)  and 128. The computations were done at  \( h_{o} = 0.5J_{nn} \)  (where  \( J_{nn} = 1 \) ),  \( f = 10^{-3} \) , and  \( T = 0.8T_{c}^{NN} \) . Each run is of length 100,000 MCSS. The dashed lines are a guide to the eye.

number of MCSS needed for the system to decay to a net zero magnetized state  \( (m(t)=0) \)  from a completely magnetized state  \( (m(t)=\pm1) \) . The average metastable lifetime,  \( \langle\tau(h_{o},T,L,p)\rangle \) , is calculated after 1000 repeated trials. The simulations were performed for L=128 at  \( T=0.8T_{c}^{NN} \)  for various ratios of the interaction strength p=0, 0.5, 0.7, and 1. The results are shown in Fig. 3. From Fig. 3 we see that the NNNKI model's average  \( \langle\tau(h_{o},T,L,p)\rangle \)  is much greater than the NNKI model's  \( \langle\tau(h_{o},T,L,p)\rangle \) . The lifetime is sensitive to the ratio of the interaction strengths. Since the metastable lifetime dictates the underlying metastable mode decay this in turn causes the system to exhibit a transition from the deterministic to the stochastic region.

![](./images/867749545851749097_7.jpg)

FIG. 3: Variation of the average metastable lifetime,  \( \langle\tau(h_{0},T,L,p)\rangle \) , as a function of interaction strength ratio  \( p = J_{nnn}/J_{nn} \)  on a log-linear scale. The average lifetime was computed using the first passage of time to zero magnetization for 1000 repeated trials for different values of the external magnetic field amplitude  \( h_{o} \) . The calculations were performed for L=128 at  \( T = 0.8T_{c}^{NN} \) . We see from the plot that the value of  \( \langle\tau\rangle \)  is sensitive to additional interactions present in the system. The computed error bars (standard deviation) are displayed. For some of the computed data points the error bars are smaller than the symbol size.

## IV. DISCUSSION AND CONCLUSION

The computations in this article demonstrate that interactions have an important role to play in the kinetic Ising model in an oscillating applied field. While we have established that the system undergoes a transition from a deterministic to a stochastic regime our computations do not highlight the DPT or SR possible in the system. Some of the magnetization time series data (p = 0.22 to 0.25) show an inkling of a MD region as seen in the “wandering” time series graphs. However, the response of the system eventually becomes stochastic. Our choice of a small lattice size (L = 128) and system parameters ( \( L, h_{o} \) , and T) may have caused the MD region to be less prominent compared to SR since the SR phenomenon is a finite-size effect. Investigating the model further for a DPT and/or SR for changing interaction strengths will be a topic of future investigation to be reported elsewhere. Another important conclusion of this article is that the metastable lifetime,  \( \tau \) , which dictates the physics of the kinetic Ising model is sensitive to additional interactions. Finally, it is our hope that this work will motivate experimentalists to investigate the interaction induced transition observed in the NNNKI model in real material systems.

## Acknowledgments

TD and WDB thank Per Arne Rikvold and Mark A. Novotny for many helpful discussions. WDB thanks Tom Colbert, Andy Hauger, and Pamplin Student Research Funds (ASU). TD thanks Faculty Research Faculty Development Funds (ASU).
 

[1] B. K. Chakrabarti and M. Acharyya, Rev. Mod. Phys. 71, 847 (1999).

[2] S. W. Sides, P. A. Rikvold, and M. A. Novotny, Phys. Rev. Lett. 81, 834 (1998).

[3] S. W. Sides, P. A. Rikvold, and M. A. Novotny, Phys. Rev. E 59, 2710 (1999).

[4] G. Korniss, C. J. White, P. A. Rikvold, and M. A. Novotny, Phys. Rev. E 63, 016120 (2000).

[5] G. Korniss, P. A. Rikvold, and M. A. Novotny, Phys. Rev. E 66, 056127 (2002).

[6] S. W. Sides, P. A. Rikvold, and M. A. Novotny, Phys. Rev. E 57, 6512 (1998).

[7] G. M. Buendía and P. A. Rikvold, Phys. Rev. E 78, 051108 (2008).

[8] K. Park, P. A. Rikvold, G. M. Buendía, and M. A. Novotny, Phys. Rev. Lett. 92, 015701 (2004).

[9] D. T. Robb, Y. H. Xu, O. Hellwig, J. McCord, A. Berger,

M. A. Novotny, and P. A. Rikvold, Phys. Rev. B 78, 134422 (2008).

[10] H. Zhu, S. Dong, and J.-M. Liu, Phys. Rev. B 70, 132403 (2004).

[11] Y.-L. He and G.-C. Wang, Phys. Rev. Lett. 70, 2336 (1993).

[12] B. C. Choi, W. Y. Lee, A. Samad, and J. A. C. Bland, Phys. Rev. B 60, 11906 (1999).

[13] Q. Jiang, H.-N. Yang, and G.-C. Wang, Phys. Rev. B 52, 14911 (1995).

[14] D. P. Landau and K. Binder, A Guide to Monte Carlo Simulations in Statistical Physics (Cambridge University Press, 2000).

[15] P. A. Rikvold, H. Tomita, S. Miyashita, and S. W. Sides, Phys. Rev. E 49, 5080 (1994).
 
