
# Doping a correlated band insulator: A new route to half metallic behaviour

Arti Garg \( ^{1} \) , H. R. Krishnamurthy \( ^{2} \)  and Mohit Randeria \( ^{3} \) 

 \( ^{1} \) Theoretical Condensed Matter Physics Division,

Saha Institute of Nuclear Physics, 1/AF Bidhannagar, Kolkata 700 064, India

 \( ^{2} \)  Centre for Condensed Matter Theory, Department of Physics, Indian Institute of Science, Bangalore 560 012, and JNCASR, Jakkur, Bangalore 560 064, India
 \( ^{3} \) Department of Physics, The Ohio State University, Columbus, OH 43210, USA

We demonstrate in a simple model the surprising result that turning on an on-site Coulomb interaction U in a doped band insulator leads to the formation of a half-metallic state. In the undoped system, we show that increasing U leads to a first order transition between a paramagnetic, band insulator and an antiferromagnetic Mott insulator at a finite value  \( U_{AF} \) . Upon doping, the system exhibits half metallic ferrimagnetism over a wide range of doping and interaction strengths on either side of  \( U_{AF} \) . Our results, based on dynamical mean field theory, suggest a novel route to half-metallic behavior and provide motivation for experiments on new materials for spintronics.

PACS numbers: 71.10.Fd, 71.30.+h, 71.27.+a, 71.10.Hf, 75.10.Lp

Turning on strong electron correlations in a normal metallic system is generally believed to result in interesting phases like anti-ferromagnetic Mott Insulator, high  \( T_{c} \)  superconductor, pseudogap phase and non fermi-liquid phases. But the effect of e-e interactions in a band insulator have not been explored in detail so far. In this paper we study effects of onsite interaction U on a band insulator and present a novel interaction driven route to half-metal phase. We show that doping a correlated band insulator results in the formation of half-metallic (HM) ferrimagnet. HMs are an interesting class of materials in which electrons with one spin direction behave as in a metal and electrons with the opposite spin direction behave as in an insulator, and have applications in spintronics as they can generate spin-polarized currents [1].

Specifically, in this paper we study a simple tight-binding model with two bands, arising from a staggered potential  \( \Delta \)  on the sites of a bipartite lattice, in the presence of an on-site Coulomb repulsion, the Hubbard U. At half filling, when one band is filled and the other is empty, this system is a paramagnetic band insulator (BI). When U is turned on, as we show, an anti-ferromagnetic (AFM) order sets in with a first order phase transition at some threshold  \( U = U_{AF} \) . Upon doping, this system becomes a ferrimagnetic HM over a range of doping and U values.

Intuitively the formation of a HM upon doping can be understood as follows. Due to the staggered potential, the band gaps for the two spin components in the antiferromagnetic insulator (AFMI) phase are different, e.g.  \( Eg_{l} < Eg_{f} \) . On hole doping, in a rigid band picture, one would expect that it will be energetically favourable to put all the holes in the down spin band. This will make the down spin band conducting while the up-spin will remain insulating, resulting in a HM phase. Similarly for  \( U < U_{AF} \) , consider the BI in presence of a small staggered magnetic field  \( h \rightarrow 0 \)  such that the band gap in the

![](./images/867752695409148774_1.jpg)

FIG. 1: Zero temperature phase diagram of the model in Eq. (1) obtained within DMFT for the Bethe lattice of infinite connectivity. Circles show the data points and the lines are guides to the eye. At half filling, the system is a band insulator at weak U and becomes an AFMI with a first order phase transition at  \( U_{AF} \) . Upon doping, it becomes a ferrimagnetic half-metal (HM) over a large range of doping and U values.

single particle excitation spectrum of the two spin components is different, being  \( Eg_{\uparrow} = Eg + h \)  and  \( Eg_{\downarrow} = Eg - h \) . Following the argument mentioned above, doping this BI with holes of density x will result in the formation of a HM with a net moment  \( \sim x \)  which, due to a molecular field arising from U, will self consistently cause the staggered magnetisation to be non zero. The simple rigid band picture used in this argument will hold only for small doping and weak coupling regime. The question of interest is whether the HM phase exists on finite amount of doping at intermediate and large U values. In this paper we show that it is possible to get the HM phase for a finite doping over a range of U values as shown in the phase diagram of Fig. 1. In the HM phase, there occurs a full redistribution of the degrees of freedom as compared
 

to the half filled case as shown in detail in later sections. The HM phase survives for the widest range of doping in the intermediate coupling regime where  \( U \sim 2\Delta \) .

The model we consider has tight-binding electrons moving on a bipartite lattice (sub-lattices A and B) described by

 \[ \begin{align*}H=-t\sum_{i\in A,j\in B,\sigma}[c_{i\sigma}^{\dagger}c_{j\sigma}+h.c]+&\Delta\sum_{i\in A}n_{i}-\Delta\sum_{i\in B}n_{i}\\&+U\sum_{i}n_{i\uparrow}n_{i\downarrow}-\mu\sum_{i}n_{i}(1)\end{align*} \] 

where t is the nearest neighbor hopping, U the Hubbard repulsion and  \( \Delta \)  a staggered one-body potential which doubles the unit cell. The chemical potential  \( \mu \)  is fixed so that the average occupancy is  \( \langle\langle n_{A}\rangle+\langle n_{B}\rangle\rangle/2=n=1-x \) . The Hamiltonian (1) is sometimes called the “ionic Hubbard model” (IHM) with  \( \Delta \)  the “ionic” potential. In an earlier work, using a dynamical mean field theory (DMFT) approach employing iterated perturbation theory (IPT) as the impurity solver, we studied this model at half filling in the spin-symmetric case and showed how strong correlations dynamically close the gap in a band insulator resulting in an intermediate metallic phase [2]. This result was reproduced qualitatively by many other groups [3]. Here we study this model using the same DMFT approach in the spin asymmetric case [4]. Once we allow for the magnetic order, the system at half-filling undergoes a first order phase transition from a PM BI to AFMI (see Fig. 3). In the spin asymmetric phase there are some earlier works at half filling [5] and for the doped case [6] but to the best of our knowledge the existence of a HM phase has not been suggested so far.

The DMFT approximation is exact in the limit of large dimensionality [7, 8] and has been demonstrated to be quite successful in understanding the metal-insulator transition [7, 8] in the usual Hubbard model, which is the  \( \Delta = 0 \)  limit of eq. (1). We focus in this paper on the anti-ferromagnetic sector of eq. (1), for which it is convenient to introduce the matrix Green's function

 \[ \hat{G}_{\alpha\beta}^{\sigma}(\mathbf{k},i\omega_{n})=\left(\begin{array}{c c}{\zeta_{A\sigma}(\mathbf{k},i\omega_{n})}&{-\epsilon_{\mathbf{k}}}\\ {-\epsilon_{\mathbf{k}}}&{\zeta_{B\sigma}(\mathbf{k},i\omega_{n})}\\ \end{array}\right)^{-1} \quad (2) \] 

where  \( \alpha,\beta \)  are sub-lattice  \( (A,B) \)  indices,  \( \sigma \)  is the spin index, k belongs to the first Brillouin Zone (BZ) of one sub-lattice,  \( i\omega_{n}=(2n+1)\pi T \)  and T is the temperature. The kinetic energy is described by the dispersion  \( \epsilon_{k} \)  and  \( \zeta_{A(B)\sigma}\equiv i\omega_{n}\mp\Delta+\mu-\Sigma_{A(B)\sigma}(i\omega_{n}) \) . Within the DMFT approach the self energy is purely local [7]. Thus the diagonal self-energies  \( \Sigma_{\alpha\sigma}(i\omega_{n}) \)  are k-independent and the off-diagonal self-energies vanish (since the latter would couple the A and B sub-lattices). The DMFT approach includes local quantum fluctuations by mapping [7, 8] the lattice problem onto a single-site or “impurity” with local interaction U hybridizing with a self-consistently determined bath as follows. (i) We start with a guess for  \( \Sigma_{\alpha\sigma}(i\omega_{n}) \) ,  \( n_{\alpha\sigma} \) , and compute the local  \( G_{\alpha\sigma}(i\omega_{n})=\sum_{\mathbf{k}}G_{\alpha\alpha\sigma}(\mathbf{k},i\omega_{n}) \)  rewritten as

 \[ G_{\alpha\sigma}(i\omega_{n})=\zeta_{\bar{\alpha}\bar{\sigma}}(i\omega_{n})\int_{-\infty}^{\infty}d\epsilon\frac{\rho_{0}(\epsilon)}{\zeta_{A\sigma}(i\omega_{n})\zeta_{B\sigma}(i\omega_{ n})-\epsilon^{2}} \quad (3) \] 

with  \( \alpha = A(B) \) ,  \( \sigma = \uparrow \) ,  \( \downarrow \)  and  \( \bar{\alpha} = B(A) \)  with  \( \rho_{0}(\epsilon) \)  is the bare DOS for the lattice considered (see below). (ii) We next determine the “host Green’s function” [7, 8]  \( G_{0\alpha\sigma} \)  from the Dyson equation  \( \mathcal{G}_{0\alpha\sigma}^{-1}(i\omega_{n}) = G_{\alpha\sigma}^{-1}(i\dot{\omega}_{n}) + \Sigma_{\alpha\sigma}(i\omega_{n}) \) . (iii) We solve the impurity problem to obtain  \( \Sigma_{\alpha\sigma}(i\omega_{n}) = \Sigma_{\alpha\sigma}[\mathcal{G}_{0\alpha\sigma}(i\omega_{n})] \)  (iv) We iterate steps (i), (ii) and (iii) till a self-consistent solution is obtained. We use as our “impurity solver” in step (iii) a generalization of the iterated perturbation theory (IPT) [7, 9] scheme which has the merit of giving semi-analytical results directly in the real frequency domain.

For simplicity, here we present the results for the T = 0 solution of DMFT equations on a Bethe lattice of connectivity  \( z \rightarrow \infty \) . The hopping amplitude is rescaled as  \( t \rightarrow t / \sqrt{z} \)  to get a non-trivial limit and the bare DOS is then given by  \( \rho_{0}(\epsilon) = \sqrt{4t^{2} - \epsilon^{2}} / (2\pi t^{2}) \)  which greatly simplifies the integral in eq. (3). The phase diagram in Fig. 1 has been obtained from an analysis of various physical quantities which we describe in detail below. We believe that the results obtained will be qualitatively similar in case of other generic compact DOS. In the discussion below, first we describe the detailed results for the half-filled case followed by the results for the doped case.

![](./images/867752695409148774_2.jpg)

FIG. 2: Left panel: Staggered magnetization  \( m_{s} \)  plotted as a function of U/t at half-filling. A first order phase transition takes place with the onset of  \( m_{s} \)  at  \( U_{AF} \) . Right Panel: Staggered occupancy, i.e., the difference in the filling factor of the two sublattices  \( \delta n \)  plotted as a function of U/t at half-filling.  \( \delta n \)  is non zero for all values of U/t. For  \( U < U_{AF} \) ,  \( \delta n \)  decreases monotonically and a discontinuity occurs in  \( \delta n_{A} \)  at  \( U_{AF} \) .

Half-Filling: The left panel of Fig. 2 shows our results for the staggered magnetization  \( m_{s} \) , defined as  \( m_{s}=(m_{zB}-m_{zA})/2 \)  where  \( m_{z\alpha}=n_{\uparrow\alpha}-n_{\downarrow\alpha} \)  is the sublattice magnetization. For a given value of  \( \Delta \) , there exists a threshold value  \( U_{AF} \)  at which the staggered magnetisation turns on with a jump resulting in a first order phase transition. Due to the presence of the staggered potential, the AFM instability does not occur at arbitrarily small U, and a finite value of U is required to turn
 

on the magnetisation. Both  \( U_{AF} \)  and the jump in  \( m_{s} \)  at  \( U_{AF} \)  are increasing functions of  \( \Delta \) . Note that since at half filling  \( n_{A\sigma} + n_{B\sigma} = 1 \) , the uniform magnetisation  \( m_{F} = n_{\uparrow} - n_{\downarrow} = (m_{zA} + m_{zB})/2 = 0 \)  in the half filled case. The right panel of Fig. 2 shows the staggered occupancy, i.e., the difference in the filling factor of the two sublattices, defined as  \( \delta n = (n_{B} - n_{A})/2 \) . Due to the staggered on site potential,  \( \delta n \)  is always non zero, even though the Hubbard U tries to suppress it.  \( \delta n \)  decreases monotonically as a function of U. At  \( U_{AF} \) ,  \( \delta n \)  also shows a discontinuity.

![](./images/867752695409148774_3.jpg)

FIG. 3: Left panel: Spin-resolved spectral gaps  \( E_{g\uparrow} \)  and  \( E_{g\upharpoonright} \)  plotted as a function of U/t for  \( \Delta = 1.0t \)  at half-filling. For  \( U < U_{AF} \) , in the BI phase,  \( E_{g\uparrow} = E_{g\uplus} \)  and the gaps decrease with increasing U/t. At  \( U = U_{AF} \) , there occurs a jump separating the two gaps such that  \( E_{g\downarrow} < E_{g\uparrow} \) . For  \( U > U_{HM} \) , in the AFMI phase, both the gaps increase with increasing U/t. Right panel: T = 0 phase diagram at half-filling. For  \( U < U_{AF} \) , the system is a PM BI. At  \( U_{AF} \) , a first order transition occurs with the onset of an AFM order. A HM AFM point is seen at  \( U = U_{HM} > U_{AF} \) . For all  \( U > U_{HM} \) , the system is an AFMI.

Next we discuss the single particle DOS  \( \rho_{\alpha,\sigma}(\omega) = -\sum_{k}Im\hat{G}_{\alpha\sigma}(k,\omega^{+})/\pi \)  where  \( \sigma \)  represents the sublattice A, B and  \( \sigma \) is the spin. The spectral gap  \( E_{g\sigma} \)  in the single particle DOS  \( \rho_{\sigma}(\omega) \)  is shown in Fig. 3. For  \( U < U_{AF} \) , the spectral gap is same for both the spin components due to the spin symmetry of the paramagnetic BI phase and  \( E_{g\sigma} \)  reduces with increase in U/t. This is because the Hubbard U suppresses the effect of the staggered potential  \( \Delta \) , which is responsible for a non-zero gap in the BI phase. At  \( U = U_{AF} \) , there occurs a jump separating the spectral gaps such that  \( E_{g\downarrow} < E_{g\uparrow} \) . For  \( U > U_{AF} \) ,  \( E_{g\downarrow} \)  keeps decreasing with increase in U/t and vanishes at  \( U_{HM} > U_{AF} \) , while  \( E_{g\uparrow} \)  starts increasing with increase in U/t and stays non zero at  \( U_{HM} \) . Thus at half-filling we have an HM AFM point at  \( U = U_{HM} \) , details of which will be published elsewhere [10]. For  \( U > U_{HM} \) , the system is an AFMI in which both the gaps increase with increase in U. The phase diagram on

![](./images/867752695409148774_4.jpg)

![](./images/867752695409148774_5.jpg)

FIG. 4: Spin-resolved single particle DOS  \( \rho_{\sigma}(\omega) \)  vs  \( \omega \)  for x = 0.17 and  \( \Delta = 1.0t \) . [a] For  \( U < U_{1} \) , in the metallic phase, the system has spin symmetry with the DOS for both the spin components being non zero at  \( \omega = 0 \) . For  \( U > U_{1} \) , e.g. at U = 2.1t and 2.5t,  \( \rho_{\uparrow}(\omega = 0) = 0 \)  while  \( \rho_{\downarrow}(\omega = 0) \neq 0 \) . This is the HM phase shown in [b] and [c]. For  \( U > U_{2} \) , the spin symmetry is restored with  \( \rho_{\sigma}(\omega = 0) \neq 0 \)  and the system is a regular metal as shown in [d].

the basis of above analysis is shown in the right panel of Fig. 3. Note that the spectral gaps are different for the up and down spin components (which is a key feature to get the HM phase) in this model because of the presence of the staggered potential  \( \Delta \) . In the next section we discuss the formation of the Ferrimagnetic HM in the doped case.

Doped Case: The phase diagram (Fig. 1) in the doped case has a broad Ferrimagnetic HM phase for  \( U_{1} < U < U_{2} \) . Below we discuss our results in detail explaining how we determine  \( U_{1} \)  and  \( U_{2} \)  from an analysis of the single particle DOS and the magnetic properties.

Single particle DOS in the doped case: Fig. 4 shows the single particle DOS  \( \rho_{\sigma}(\omega)=\rho_{A,\sigma}(\omega)+\rho_{B,\sigma}(\omega) \)  for both the spin components where  \( \omega \)  is measured from the chemical potential  \( \mu \) . For  \( U<U_{1} \) , the DOS for both the spin components is same. In this regime the system is a PM metal since the chemical potential lies inside the lower band for both the spin components (Fig. [4a]). For  \( U>U_{1} \) , magnetic order sets in making the two gaps and the DOS different for the two spin components (Fig. [4b,4c]). The Fermi level lies inside the lower band for the down-spin component making  \( \rho_{\downarrow}(\omega=0)\neq0 \)  while the up-spin DOS  \( \rho_{\uparrow}(\omega=0)=0 \)  as shown in Fig. 5; hence the system is a HM. For  \( U>U_{2} \) , the Fermi level lies inside the lower band for both the spin components. This makes both the spin components conducting, with equal density of up and down spins, and the system becomes a
 
![](./images/867752695409148774_6.jpg)

![](./images/867752695409148774_7.jpg)

FIG. 5: Plot of  \( \rho_{\uparrow}(\omega=0) \)  vs U/t for x=0.05 and x=0.17 at  \( \Delta=1.0t \) . At x=0.05 there exists a broad HM phase in which  \( \rho_{\uparrow}(\omega=0)=0 \)  while  \( \rho_{\downarrow}(\omega=0)\neq0 \) . The width of the HM phase shrinks in U space as x increases.

paramagnetic metal (Fig. [4d]). Note that there is still a small band gap (at energies higher then  \( \mu \) ). At even larger values of U, this gap will open up again separating the lower and the upper Hubbard band with the chemical potential being inside the lower Hubbard band.

Magnetisation: The curves for  \( U_{1} \)  and  \( U_{2} \)  in Fig. 1 are consistent with the magnetic properties as well which are shown in Fig. 6. For small U values, magnetic order is not favoured. As U increases, a first order transition occurs at  \( U_{1} \)  when both the sublattices acquire non zero magnetisation  \( m_{zA} \)  and  \( m_{zB} \)  with a jump at  \( U_{1} \) . Since the system is doped, these magnetisations are not equal and opposite to each other. This results in a non-zero staggered magnetisation  \( m_{s} = (m_{zB} - m_{zA})/2 \)  as well as a non-zero uniform magnetisation  \( m_{F} = (m_{zA} + m_{zB})/2 \) . Within the HM phase  \( m_{F} \)  and  \( m_{s} \)  increase with increasing x. This is because, in the HM phase, the up-spin band is fully occupied implying  \( n_{+} = 1/2 \)  and all the holes are doped in the down-spin band making  \( n_{\downarrow} = n - 1/2 \) . Therefore, the uniform magnetisation  \( m_{F} \) , which can also be written as  \( n_{\uparrow} - n_{\downarrow} \) , goes as  \( 1 - n = x \)  and is independent of the interaction strength U/t. This is in agreement with our results in Fig. 6, within the numerical error-bars. The staggered magnetisation  \( m_{s} \) , however, increases with increasing U/t. At  \( U_{2} > U_{1} \)  there occurs another first order transition and the system becomes a paramagnetic metal with both  \( m_{F} = m_{s} = 0 \)  for  \( U > U_{2} \) .

It is interesting to compare our DMFT phase diagram with the phase diagram within Hartree-Fock (HF) theory, details of which will be published elsewhere [10]. One can get a HM phase within a HF theory, but it overestimates the tendency to the formation of the HM, and also predicts qualitatively wrong results. Within HF theory for all  \( U > U_{1} \) , the system is a HM, the reason being the lack of quantum fluctuations in the HF theory which are

![](./images/867752695409148774_8.jpg)

FIG. 6: The left panel shows the staggered magnetisation  \( m_{s} \)  vs U/t and the right panel shows the uniform magnetisation  \( m_{F} \)  vs U/t. At  \( U_{1} \)  there occurs a first order jump in both  \( m_{s} \)  and  \( m_{F} \)  making them non zero. Note that in the HM phase,  \( m_{F} \sim x \) , as explained in the text. At  \( U_{2} > U_{1} \)  there occurs another 1st order transition with  \( m_{s} \)  and  \( m_{F} \)  dropping to zero.  \( \Delta = 1.0t \)  in both the panels.

captured within DMFT.

![](./images/867752695409148774_9.jpg)

FIG. 7: The width  \( (U_{2}-U_{1})/t \)  of the HM phase in U space as a function of the hole doping x. Inset shows the phase boundaries of the HM phase for  \( \Delta = 1.0t \)  and  \( 0.5t \) . Note that the HM phase gets wider with increases in the staggered potential  \( \Delta \) .

We note that, as shown in Fig. 7, the HM phase gets wider with increase in the staggered potential  \( \Delta \) . This will be useful from the application point of view. One should look for correlated band insulators with large bare band gap, and an appropriately larger U, to get a robust HM phase.

Conclusions: In conclusion, we have studied a theoretical model in which e-e interactions in a doped band insulator give rise to HM ferrimagnetic phase. Specifically, we studied an extension of the Hubbard model which includes a staggered potential that makes the system a band insulator for U = 0 at half filling. As we
 

turn on the on-site repulsion U, an AFM order sets in with a first order transition at some threshold value of  \( U = U_{AF} \) . The AFM phase has different spectral gaps for the two spin components and on doping away from half filling it becomes a HM ferrimagnet. In the doped system the HM phase survives for  \( U < U_{AF} \)  as well. The width of the HM phase in x space is largest for  \( U \sim 2\Delta \)  and increases with increase in  \( \Delta \) .

We emphasize that the new mechanism for half-metallicity described in our paper is quite distinct from the mechanisms in well-known materials that exhibit this phenomenon like the manganites, double-perovskites, or Heusler alloys, all of which have both local moments and itinerant electrons. Recently, there have been other theoretical discussions of half-metallic behavior as well  \( [11] \) . However, in all of these works either the HM phase exists only for some special doping values or requires an external electric or magnetic field. The HM phase we discuss exists for a broad range of doping and is not dependent on application of external fields.

Although our finding is based on the study of a specific model, we expect that for any system where the AFM phase at half filling has different spectral gaps for the two spin components and AFM order survives on doping, one should expect to see a HM phase. We hope that our study will motivate a search for materials along this direction and open up new possibilities in the area of spintronics.

M.R. would like to acknowledge support from DOE-BES de-sc0005035 and his collaboration with H.R.K. was made possible by NSF MRSEC DMR-0820414. HRK would like to acknowledge support from the DST, India.

[1] W. E. Pickett and H. Eschrig, J. Phys.: Condens. Matter 19, 315203 (2007); Xiao Hu, Adv. Materials 24, 294

(2012), Half-metallic Alloys: Fundamentals and Applications, Lecture Notes in Physics, Vol. 676, I. Galanakis, and P.H. Dederichs, Springer (2005).

[2] A. Garg, H. R. Krishnamurthy, and M. Randeria, Phys. Rev. Lett. 97, 046403 (2006).

[3] L. Craco, P. Lombardo, R. Hayn, G. I. Japaridze and E. Muller-Hartmann, Phys. Rev. B 78, 075121 (2008); N. Paris, K. Bouadim, F. Herbert, G. G. Batrouni, and R. T. Scalettar, Phys. Rev. Lett. 98, 046403 (2007); A. T. Hoang, J. Phys.: Conden. Matt 22, 095602 (2010).

[4] The true ground state for the IHM for large U indeed has AFM order and the metallic phase we found is typically overwhelmed by AFMI. However, if we can frustrate AFM order, then the metallic ground state will win.

[5] S. S. Kancharla and E. Dagotto, Phys. Rev. Lett. 98, 016402 (2007); K. Byczuk, M. Sekania, W. Hofstetter, and A. P. Kampf, Phys. Rev. B 79, 121103 (2009).

[6] K. Bouadim, N. Paris, F. Herbert, G. G. Batrouni and R. T. Scalettar, Phys. Rev. B, 76, 085112 (2007)

[7] A. Georges, G. Kotliar, W. Krauth, and M.J. Rozenberg, Rev. of Modern Phys. 68, 13 (1996)

[8] T. Pruschke, M. Jarrell, and J. K. Freericks, Adv. Phys. 44, 187 (1995).

[9] H. Kajueter and G. Kotliar, Phys. Rev. Lett. 77, 131 (1996).

[10] A. Garg, H. R. Krishnamurthy, and M. Randeria (unpublished).

[11] R. Nandkishore, G. Chern, and A. V. Chubukov, Phys. Rev. Lett. 108, 227204 (2012); Z. Hao, and O. A. Starykh, Phys. Rev. B 87, 161109(R) (2012); J. Yuan, D. Xu, H. Wang, Y. Zhou, J. Gao, and F. Zhang, arXiv:1302.7123.
 
