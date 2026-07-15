
# Phonon Induced Spin Dephasing Time of Nitrogen Vacancy Centers in Diamond from First Principles

Jacopo Simoni \( ^{1*} \) , Vsevolod Ivanov \( ^{1,2} \) , Thomas Schenkel \( ^{2} \) , Liang Z. Tan \( ^{1} \) 

 \( ^{1} \) Molecular Foundry, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA.
 \( ^{2} \) Accelerator Technology and Applied Physics Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA.

 \( ^{*} \) To whom correspondence should be addressed; E-mail: jsimoni@lbl.gov

Spin qubits with long dephasing times are an essential requirement for the development of new quantum technologies and have many potential applications ranging from quantum information processing to quantum memories and quantum networking. Here we report a theoretical study and the calculation of the spin dephasing time of defect color centers for the negatively charged nitrogen vacancy center in diamond. We employ ab initio density functional theory to compute the electronic structure, and extract the dephasing time using a cumulant expansion approach. We find that phonon-induced dephasing is a limiting factor for  \( T_{2} \)  at low temperatures, in agreement with recent experiments that use dynamical decoupling techniques. This approach can be generalized to other spin defects in semiconductors, molecular systems, and other band gapped materials.

Teaser: We present calculations of dephasing times in nitrogen vacancy centers
 

## 1 Introduction

The coherent manipulation of quantum mechanical systems is of fundamental importance in science and engineering  \( (1,2) \) . Solid state quantum systems, in particular, constitute an interesting and very prominent realization of qubits for quantum information processing  \( (3,4,5) \) . The main issue that needs to be overcome is that in contrast to isolated quantum systems, solid state systems tend to have strong coupling with environmental degrees of freedom with consequent loss of coherence of the quantum mechanical state.

Color centers are fluorescent lattice defects made of one or several impurity atoms or vacant atomic sites embedded in the crystal lattice. A particularly prominent example is given by the Nitrogen-Vacancy (NV) defect center in diamond  \( (6, 7, 8, 9, 10) \) , that has attracted a lot of attention in the recent years thanks to its long coherence time, optical initialization, and read out  \( (11, 12) \) .

The dephasing rate of NV center samples is often controlled by nuclear spin impurities, resulting in coherence times in the range of ms -  \( \mu s \)  (13, 14, 15). However, dynamical decoupling techniques extend coherence time to the order of seconds, where the limiting factor to coherence has been suggested to be spin-phonon interactions instead of nuclear spin impurities (16). While the theory of dephasing from nuclear spin impurities has been recently developed (17), a complete first-principles theory for spin-phonon dephasing is lacking for color centers. With improvements in dynamical decoupling techniques, sample fabrication and purification, and the possibility of room temperature operation, it is desirable to develop a predictive understanding of phonon-induced dephasing. Additionally, indications that phonon-induced dephashing introduce non-Markovianity into the system (18) necessitate further study of phonon-induced processes in these systems.

In this work we demonstrate via first-principles calculations, that phonon-induced dephasing
 

is a limiting factor for  \( T_{2} \)  measured by Hahn echo with dynamical decoupling at low temperatures. This additional contribution arises from phonon-induced fluctuations of color center energy levels. In general, the total decoherence rate  \( \Gamma = 1/T_{2} \)  can be written as a sum of four main contributions

 \[ \Gamma=\frac{1}{T_{2}}=\frac{1}{2T_{1}}+\Gamma[\mathbf{p u r e}]+\Gamma[\mathbf{d i s o r d e r}]+\Gamma[\mathbf{Q Q}], \quad (1) \] 

where  \( T_{1} \)  indicates the population relaxation time and defines the limiting decoherence time due to energy relaxation (19, 20, 21, 22) that results from the mixing of the energy levels. The decoherence rate  \( \Gamma \)  refers to the total coherence of the superposition state  \( (|0\rangle + |1\rangle)/\sqrt{2} \)  and depends on the specific experimental setup used, as some of the remaining contributions can be removed with an appropriate measurement sequence (23). The terms aside from  \( T_{1} \)  in Eq. (1) represent all other contributions to the decoherence without net energy exchange between the qubit and the environment. As such,  \( T_{2} \)  in general demands for a harder theoretical treatment compared to  \( T_{1} \) .

Whereas the  \( T_{1} \)  time for NV centers at cryogenic temperatures can be as long as 8 hr (24),  \( T_{2} \)  was found to be limited, at higher temperatures, to approximately  \( 0.5T_{1} \)  (16) and the reported longest measured  \( T_{2} \)  at low temperature is of the order of 1 second (25). These results indicate that a better understanding of decoherence in solid state qubits requires theoretical methods to directly access the other contributions beyond  \( T_{1} \)  given the importance of accounting for all the different sources of dephasing. The knowledge of  \( T_{1} \)  alone is not sufficient to estimate  \( T_{2} \) .

Several dephasing mechanisms are known to contribute beyond population relaxation  \( (13) \) , here, in order to simplify the problem we distinguish three main groups of dephasing processes and assume that they contribute additively to the total dephasing (Eq. 1).  \( \Gamma \) [pure] is the pure dephasing rate coming exclusively from unavoidable interactions of a single color center with the environment under the assumption of complete homogeneity. This is the case of a single qubit.
 

defect in a perfect crystal lattice with no imperfections and dephasing due only to interactions with atomic vibrations and the radiation field.  \( [QQ] \)  is instead the dephasing of the quantum system due to the interaction with other qubits in its environment (26). This second term can be reduced greatly by isolating the  \( NV^{-} \) center from other nitrogen defects in diamond. Finally, each  \( NV^{-} \) in the ensemble will have a slightly different spin excitation frequency due to local spatial magnetic inhomogeneities causing the qubit to lose coherence during the evolution, a typical example is given by spatial inhomogeneities of the local magnetic field caused by nuclear spin impurities. This term is represented by the  \( \Gamma[disorder] \)  contribution.

NV centers are often employed for high precision magnetometry and sensing (27,28,29), which is usually achieved through the excitation of the spin state evolved under the application of an external magnetic field. Here we consider two quite common methodologies, the Ramsey sequence (30,31) and the Hahn-echo measurements (32,33,34). In the Ramsey sequence of pulses, the qubit is initialized to the superposition state  \( \left(\left|0\right\rangle+\left|1\right\rangle\right)/\sqrt{2} \)  and then rotated through the application of an external magnetic field B for a time interval  \( \tau \) . The quantum superposition state at time  \( \tau \)  is then written as  \( \left(\left|0\right\rangle+e^{i\phi}\left|1\right\rangle\right)/\sqrt{2} \)  and  \( \phi \)  is the phase acquired by the spin qubit. Finally a  \( \pi/2 \)  microwave pulse is applied, projecting the state back to the quantization axis. The Hahn echo sequence instead applies a microwave  \( \pi \)  pulse during the magnetic field evolution phase, flipping the spins and causing a refocusing of the signal. Other decoupling schemes apply several  \( \pi \)  pulses with sensible improvement of the coherence  \( T_{2} \)  time (35,36,37).

Previous calculations of dephasing times were mostly applied to semiconducting systems (38), quantum dots (39, 40), and even biological systems (41). In these works molecular dynamics (MD) simulations are run at different temperatures and the energy gap fluctuations are obtained using density functional theory at specific configurations along the MD trajectories. These results are used to compute the energy fluctuation auto-correlation function that is related to the dephasing function  \( D(t) \)  through the cumulant expansion approximation (42), and used to ex-
 

tract the dephasing time.

In the rest of the paper we will focus on the evaluation of spin dephasing times in the nitrogen vacancy center using constrained Density Functional Theory  \( (43, 44, 45) \)  (cDFT) based calculations. These methods are routinely employed now to study the electronic structure of defects embedded in solids  \( (4, 46, 47) \) .

We use the cumulant expansion approximation to obtain the dephasing function. However, we do not use MD simulations to extract the energy fluctuations and the phonon modes are directly computed from the DFT data. The calculations are performed by means of the VASP package  \( (48, 49) \) , which is used to compute the Zero Field Splitting (ZFS) and Hyperfine Interaction (HFI) coefficients. The paper is organized as follows: in section (2.1) we outline the theoretical formalism. The calculation procedure and the results for NV centers are given in section (2.2), and in section (3) we conclude.

## 2 Results

## 2.1 Theory and formalism

## 2.1.1 Dephasing function calculation

The dephasing function  \( D(t) \)  describes the decay of off-diagonal density matrix components as a function of time after the qubit is initialized in a pure state. Within a second order cumulant approximation (50),  \( D(t) \)  is obtained from the autocorrelation function of the fluctuations in energy level differences.

 \[ C(t)=\left\langle\delta E(t)\cdot\delta E(0)\right\rangle_{\mathrm{T}}, \quad (2) \] 

where  \( \langle\ldots\rangle_{T} \)  indicates a thermal average at the temperature T,  \( \delta E(t) \)  is the fluctuation in the energy level differences. The dephasing function  \( D(t) \)  is then obtained from the knowledge of the auto-correlation function decay time  \( \tau_{c} \)  and from the parameter  \( \Delta^{2}=C(t=0) \) . The
 

following expression is valid in the case of an exponentially decaying autocorrelation function

 \[ g(t)=\Delta^{2}\tau_{c}^{2}\bigg[e^{-t/\tau_{c}}+\frac{t}{\tau_{c}}-1\bigg], \quad (3) \] 

 \[ D(t)=e^{-g(t)}. \quad (4) \] 

The cumulant expansion approximation works well under the assumption of harmonic approximation for the phonons. In the limit of fast modulation ( \( \Delta\tau_{c} << 1 \) ) the dephasing function becomes  \( D(t) \simeq e^{-t/T} \)  with  \( T^{-1} = \Delta^{2}\tau_{c} \) . In the limit of slow modulation, we instead have  \( g(t) \simeq \Delta^{2}t^{2}/2 \)  and the inhomogeneous linewidth is simply  \( \Delta \) . In order to proceed, we need an expression for the energy fluctuation  \( \delta E(t) \) . This can be derived from the knowledge of the spin Hamiltonian of the system.

## 2.1.2 The spin Hamiltonian

The spin Hamiltonian has the following general form

 \[ \hat{H}_{\mathrm{s s}}=\hat{\mathbf{S}}\cdot\stackrel{\leftrightarrow}{\mathcal{D}}\cdot\hat{\mathbf{S}}+\sum_{\mathrm{I}}\mathbf{I}(\mathbf{R}_{\mathrm{I}};t)\cdot\stackrel{\leftrightarrow}{\mathcal{A}}_{\mathrm{h f i}}(\mathbf{R}_{\mathrm{I}})\cdot\hat{\mathbf{S}}+\gamma_{e}\mathbf{B}\cdot\hat{\mathbf{S}}, \quad (5) \] 

The first term on the right hand side is the zero field splitting contribution to the spin Hamiltonian.  \( \hat{S} \)  is the spin operator of the system.  \( \stackrel{\leftrightarrow}{D} \)  is a symmetric and traceless  \( 3 \times 3 \)  tensor that in the case of negligible spin orbit interaction, as in our case, is entirely due to dipolar magnetic interactions (5I)

 \[ D_{i j}=\frac{\mu_{0}g_{e}^{2}\mu_{\mathrm{B}}^{2}}{4\pi}\sum_{a<b}\chi_{a b}\left\langle\Psi_{a b}\right|\frac{r^{2}\delta_{i j}-3r_{i}r_{j}}{r^{5}}|\Psi_{a b}\rangle, \quad (6) \] 

where  \( g_{e} \)  is the Landé factor and  \( \mu_{B} \)  is the Bohr magneton.  \( |\Psi_{ab}\rangle \)  is the Slater determinant of the two-electrons system, that in our case corresponds to the Kohn-Sham Slater determinant obtained from the solution of the DFT set of coupled equations. r is the distance between the two interacting spins. The second term on the right-hand side of Eq. (5) is the hyperfine coupling with nuclear spins  \( \mathbf{I}(\mathbf{R}_{\mathrm{I}}) \) . It defines an effective time dependent magnetic field given that the
 

nuclear spins will also evolve in time under an externally applied magnetic field B.

The hyperfine coupling term  \( \stackrel{\leftrightarrow}{A}_{hfi} \)  is given by the sum of the Fermi contact contribution and a dipolar term (52)

 \[ \mathcal{A}_{\mathrm{h f f}}^{i j}(\mathbf{R}_{\mathrm{I}})=\frac{\mu_{0}g_{e}g_{\mathrm{I}}\mu_{\mathrm{B}}\mu_{\mathrm{J}}}{\langle S_{z}\rangle}\left[\frac{2}{3}\delta_{i j}\rho_{S}(\mathbf{R}_{\mathrm{I}})+\frac{1}{4\pi}\int d\mathbf{r}\frac{\rho_{S}(\mathbf{r}+\mathbf{R}_{\mathrm{I}})}{r^{3}}\frac{3r_{i}r_{j}-{\delta_{i j}}r^{2}}{r^{2}}\right], \quad (7) \] 

 \( \rho_{S}(\mathbf{R}_{\mathrm{I}}) \)  is the spin electron density located around the atom I.  \( g_{I} \)  and  \( \mu_{J} \)  are the nuclear Landé factor and the nuclear magneton. The last term in Eq. (5) is the Zeeman coupling term with  \( \gamma_{e} \)  electron gyromagnetic ratio.

## 2.1.3 Hyperfine and zero field splitting energy fluctuations

Our formalism requires the evaluation of fluctuations in the spin levels  \( \delta E(t) \)  at time t from the different sources of dephasing. We assume that the qubit is evolved from some linear combination of states  \( |0\rangle \)  and  \( |1\rangle \)  of the spin triplet, implying that  \( \delta E(t) = \langle1|\delta\hat{H}_{\mathrm{ss}}(t)|1\rangle - \langle0|\delta\hat{H}_{\mathrm{ss}}(t)|0\rangle \)  is the fluctuation in the energy difference between the two eigenstates of the spin Hamiltonian. The fluctuation can then be expressed as

 \[ \delta\hat{H}_{\mathrm{s s}}=\delta\hat{H}_{\mathrm{S S}}^{\mathrm{s p}-\mathrm{p h}}+\delta\hat{H}_{\mathrm{S S}}^{\mathrm{r s p}-\mathrm{n u}-\mathrm{p h}}+\delta\hat{H}_{\mathrm{S S}}^{\mathrm{s p}-\mathrm{n u}}, \quad (8) \] 

 \[ \delta\hat{H}_{\mathrm{s s}}^{\mathrm{s p}-\mathrm{p h}}=\sum_{\lambda}\sum_{\mathbf{q}}\sum_{j;a}u_{\lambda,\mathbf{q}}(j a;t)\hat{\mathbf{S}}\cdot\nabla_{j a}\stackrel{\leftrightarrow}{D}\cdot\hat{\mathbf{S}}, \] 

 \[ \begin{align*}\delta\hat{H}_{\mathrm{ss}}^{\mathrm{sp-nu-ph}}=\sum_{\lambda,\mathbf{q}}\sum_{j;a}u_{\lambda,\mathbf{q}}(ja;t)\sum_{\mathrm{I}}\mathbf{I}_{0}(\mathbf{R}_{\mathrm{I}})\cdot\nabla_{ja}\stackrel{\leftrightarrow}{\mathcal{A}}_{\mathrm{hfi}}(\mathbf{R}_{\mathrm{I}})\cdot\hat{\mathbf{S}},\\\delta\hat{H}_{\mathrm{ss}}^{\mathrm{sp-nu}}=\sum_{\mathrm{I}}\delta\mathbf{I}(\mathbf{R}_{\mathrm{I}};t)\cdot\stackrel{\leftrightarrow}{\mathcal{A}}_{\mathrm{hfi}}(\mathbf{R}_{\mathrm{I}})\cdot\hat{\mathbf{S}},\end{align*} \] 

where  \( u_{\lambda,\mathbf{q}}(ja;t) \)  is the atomic vibration associated with the mode  \( (\lambda,\mathbf{q}) \)  along atom a and direction j.  \( \delta\mathbf{I}(\mathbf{R}_{\mathrm{I}};t) \)  is the temporal variation of the nuclear spin as a result of the precessional motion with respect to  \( \mathbf{I}_{0}(\mathbf{R}_{\mathrm{I}}) \)  due to the external magnetic field. In Eq. (8) we have defined three main contributions to the fluctuations in the energy levels. The first term describes the phonon-induced fluctuations of the spin-spin coupling tensor  \( \stackrel{\leftrightarrow}{D} \) , and is the most important contribution.
 

to  \( \Gamma \) [pure]. The second term involves the phonon-induced fluctuations of the hyperfine coupling while the last term accounts for the precession of nuclear spins. Due to their dependence on nuclear spin impurities, the second and last terms  \( (\delta\hat{H}_{\mathrm{ss}}^{\mathrm{sp}-\mathrm{nu}-\mathrm{ph}} \)  and  \( \delta\hat{H}_{\mathrm{ss}}^{\mathrm{sp}-\mathrm{nu}}) \)  constitute the main contributions to  \( \Gamma \) [disorder]. From now on we will assume that our system forms a matrix of single  \( NV^{-} \) defects located far enough apart that they do not interact with each other. This assumption is valid in the case of low nitrogen concentration. This means that we can neglect  \( \Gamma \) [QQ] and consider how the three terms in Eq. (8) contribute to  \( \Gamma \) [pure] and  \( \Gamma \)  [disorder]. Their relative importance changes with the particular experimental setup used, and necessitates individual examination in order to predict the experimentally observed  \( T_{2} \)  values. In Tab. (1), we summarize the results of our calculations, which will be discussed in the following sections.

## 2.2 Nitrogen vacancy center calculations

The negatively charged NV center is a paramagnetic ground state defect with quantization axis directed along the nitrogen-vacancy axis. The  \( NV^{-} \) center is characterized by a spin triplet ground state, \( ^{3}A_{2} \) , and a spin triplet excited state  \( ^{3}E \) , with zero field splittings given respectively by  \( D = 2.87 \, GHz \)  and  \( D = 1.42 \, GHz \) , as well as two singlet states,  \( ^{1}A_{1} \)  and  \( ^{1}E \)  (7, 8, 9). Upon optical excitation, the NV center shows strong fluorescence, the intensity of which is spin dependent due to spin dependent relaxation via singlet states (12). All the details of the calculations are given in section (4) while in the next sections we discuss our results in case of a dynamical decoupling sequence and of a Ramsey sequence. From now on we will assume that the system is initialized in its spin triplet ground state configuration.

## 2.2.1 Hahn echo dephasing and dynamical decoupling

A fundamental property of the Hahn echo sequence is the removal of inhomogeneous broadening from static or slowly varying magnetic fields. In general, different points in the  \( NV^{-} \) matrix
 

will be characterized by different local values of the magnetic field, due to different nuclear spin distributions. This causes strong spatial dephasing that can be inhibited by means of the Hahn echo sequence. The result can be systematically improved by means of more complex decoupling techniques, making the coherence time still longer  \( (16) \) . However, for AC magnetic fields, these methods are ineffective for improving the dephasing time. In (Fig. 2) we show the inverse of the  \( \Gamma[pure] \)  values computed for the  \( NV^{-} \) center in diamond over a range of temperatures between  \( T = 10 K \)  and  \( T = 500 K \)  with energy fluctuations caused only by  \( \delta\hat{H}_{ss}^{sp-ph} \)  in Eq. (8). The so obtained dephasing time is close, at least at low temperature, to the  \( T_{2} \)  values reported in Ref. (16) and (25). In both works, the combination of dynamical decoupling techniques and cryogenic cooling leads to a sensible increase in the observed value of  \( T_{2} \)  up to almost 1 s. The blue error bars in (Fig. 2) are determined by the choice of the fitting function model for the energy auto-correlation function. In the case of a simple fit of  \( C(t) \)  to an exponential  \( Ae^{-t/\tau_{c}} + B \)  we obtain the upper limit of the interval, whereas if we use a sinusoidal modulated exponential,  \( A\sin(\omega t + \phi)e^{-t/\tau_{c}} + B \) , we obtain the lower limit.

Although our computed  \( 1/\Gamma[pure] \)  compares remarkably well with the experimental  \( T_{2} \)  from Ref. (16) and (25) at low temperatures ( \( 3 K \)  and  \( 70 K \) ), at higher temperatures theory and experiments diverge. This can be in part explained by the fact that our temperature dependence is underestimated, as most of the computed  \( \Gamma[pure] \)  is a result of quantum zero-point fluctuations of the phonon bath. We are, in fact, only considering the second order term of the cumulant expansion (Eq. 2), and first order variations in the phonon displacement (Eq. 8), leaving out the higher order contributions that account for multi-phonon processes, which are only relevant at high temperatures.

In our calculations, in fact, the temperature dependence enters the expression for the energy fluctuations only through the phonon amplitude with a dependence of the form  \( \sqrt{1 + 2n_{ph}} \) . Most importantly, the measured coherence time  \( T_{2} \)  is not equivalent to  \( 1/\Gamma[pure] \) . Our cal-
 

culations suggest that at low temperatures, thanks to very long spin relaxation times  \( (24) \) ,  \( T_{2} \)  should be dominated by the pure dephasing term. On the other hand, at higher temperatures,  \( T_{1} \)  dominates over  \( 1/\Gamma[\text{pure}] \)  due to its stronger temperature dependence.

(Fig. 3) evaluates the contribution of the different atoms in the super cell and of the different phonon modes to  \( 1/\Gamma[\text{pure}] \) . The upper panel in the figure shows each atom's resolved dephasing time as a function of each atom's distance from the vacancy. This quantity is obtained from Eq. (8) eliminating the sum over the atom's indices  \( (j; a) \) . We observe a clear trend in the figure with the carbon atoms closer to the vacancy having a greater effect on the  \( \Gamma[\text{pure}] \)  linewidth compared to the atoms farther away. This phenomenon can be understood qualitatively by considering that the atom-resolved zero field splitting gradient  \( \nabla_{aj}\overset{\leftrightarrow}{D} \)  is much higher in magnitude for a few carbon atoms located around the vacancy. In (Fig. 1) we can clearly distinguish three carbon atoms corresponding to the three red points of (Fig. 3) with a much higher magnitude of the  \( \nabla_{a}\overset{\leftrightarrow}{D} \)  vectors compared to other atoms (see also (Fig. SM1)). The three vectors are oriented toward the vacancy with the same trigonal symmetry possessed by the defect. This is in agreement with the observation that  \( T_{1} \)  times in NV centers are mostly determined by the local vibrational properties around the defect center (24). We predict that the first shell (red points in (Fig. 3)) and a few carbons in the second shell around the vacancy have equally strong contribution to the overall dephasing, approximately an order of magnitude stronger than the other atoms. The nitrogen atom (blue point in figure), despite being a nearest-neighbor of the vacancy, does not contribute as much because of its comparatively minor electron spin density. The lower panel of the figure shows instead the contribution to  \( \Gamma[\text{pure}] \)  coming from the different phonon modes. Each point in the figure corresponds to a vibrational mode; orange colored points are more localized close to the vacancy compared to darker points. We distinguish two frequency bands which contribute strongly to  \( \Gamma[\text{pure}] \) . The broad band at 10 - 20 THz is the contribution of local-continuum resonances, while the sharp band at 40 THz comes from local
 

modes (53). In general, the contribution to  \( \Gamma[pure] \)  increases with the local character of the mode.

In (Fig. 4) we finally consider the effect of the hyperfine coupling. We separate the contribution of  \( \delta\hat{H}_{ss}^{sp-nu-ph} \)  from that of  \( \delta\hat{H}_{ss}^{sp-ph} \) , as in Eq. (8). Due to the fast vibrational dynamics the effect of  \( \delta\hat{H}_{ss}^{sp-nu-ph} \)  is not mitigated by dynamical decoupling techniques and it disappears only in the limit of very low  \( C^{13} \)  concentrations. In our simulations we apply an external static magnetic field B along the spin quantization axis, which defines a preferential alignment axis for the nuclear spins, and then average over 32 possible spin configurations, enough to converge on the final  \( 1/\Gamma \)  value. In each configuration the nuclear spins are associated to a random set of atoms in the simulation box. At finite temperatures the nuclear spin direction has finite probability of not being aligned with the applied magnetic field. The direction of the nuclear spins, in the different configurations, are selected randomly from a Gaussian distribution centered on the B field direction and with a width proportional to the temperature of the system. This has the effect of making the  \( 1/\Gamma \)  time slightly longer compared to the zero temperature value. However, the most important contribution to  \( 1/\Gamma \)  comes from the concentration of  \( C^{13} \)  isotopes. At low concentrations  \( 1/\Gamma[\text{disorder}] \simeq 10^{8} \)  s, while at higher concentrations  \( 1/\Gamma[\text{disorder}] \)  decreases by a few orders of magnitude, which is not sufficient to make this effect observable compared to the energy fluctuations due to the simple spin-phonon term  \( \delta\hat{H}_{ss}^{sp-ph} \) .

## 2.2.2 Ramsey sequence dephasing times

The Ramsey sequence coherence times (commonly referred to as  \( T_{2}^{*} \) ) are fundamentally determined by the strength of the hyperfine interaction close to the defect center. It depends on two extrinsic parameters, the applied magnetic field strength and the concentration of nuclear spin impurities. This is an overestimate of the experimental  \( T_{2} \)  since other effects could be at play that are not considered here like the magnetic interaction between different defects (I4), temper-
 

ature fluctuations and strains.

In (Fig. 5) we compute the  \( 1/\Gamma[\text{disorder}] \)  time as a function of the concentration of carbon magnetic impurities for different applied magnetic field amplitudes. The calculations are performed in all the different cases by randomly selecting 128 nuclear spin configurations; the nuclear spins in each configuration are evolved under the effect of the externally applied magnetic field and of the electronic spins coupled through the hyperfine tensor. The spin fluctuations are then computed according to Eq. (8) for each configuration by isolating the  \( \delta\hat{H}_{\mathrm{ss}}^{\mathrm{sp}-\mathrm{nu}} \)  term. The  \( 1/\Gamma[\text{disorder}] \)  time of the ensemble is obtained by taking the average of the energy fluctuation functions  \( \delta E \)  from the different configurations. To understand the distribution within the ensemble, we also compute  \( \Gamma[\text{disorder}] \)  for each configuration alone and plot an error bar depicting the standard deviation of the distribution. The standard deviation is bigger at low concentrations due to the low number of nuclear spins contributing to the dynamics. At low concentrations we find the longest dephasing times, approaching  \( 0.1\,ms \) , while at high concentrations we converge to values of  \( 1/\Gamma[\text{disorder}] \)  below  \( 1\,\mu s \) . The application of stronger magnetic fields to the same random configuration of nuclear spins lowers the Ramsey sequence dephasing times due to the higher spin precession frequencies, as seen in (Fig. 5). On the other hand, applied magnetic fields also tend to align nuclear spins, which would counteract this effect. This has been discussed elsewhere (54, 17) and it is not considered here since we assume that our starting spin configuration is randomly distributed and not aligned to the applied field.

## 3 Discussion

We have computed the pure dephasing time (at the second order cumulant approximation) and part of the ensemble dephasing coming from  \( C^{13} \)  isotopic impurities in diamond  \( NV^{-} \) centers. These results indicate the importance of accounting for various dephasing mechanisms in the calculation of the full decoherence time in solid state qubits. The application of dynamical
 

decoupling techniques can improve the decoherence time but we find that at low temperatures the spin-phonon contribution to the pure dephasing time  \( (1/\Gamma[\text{pure}]) \)  sets an upper limit for the decoherence time in agreement with recent experiments. At higher temperatures spin-phonon relaxation becomes the dominant contribution to the decoherence due to the weak temperature dependence of the spin-phonon pure dephasing term. The disorder induced dephasing time is the dominant contribution at high impurity concentrations, while at low concentrations it sets a limit of the order of few milliseconds  \( (1/6) \)  that can be overcome by means of dynamical decoupling techniques. These results suggest that phonon-induced dephasing should be evaluated in the design of new color centers as a potential limiting factor to coherence in particular at low temperatures.

## 4 Materials and Methods

The electronic structure of the negatively charged  \( NV^{-} \) center is computed using VASP (48,49) and PBE functionals (55). The simulations are performed at the  \( \Gamma \)  point using a  \( 3 \times 3 \times 2 \)  super cell with a total of 215 atoms (Figure 1). An increase of the number of k points does not produce any significant change in the zero field splitting or hyperfine tensor values. The ground state is a spin triplet with a zero field splitting D = 2.97 GHz that is in good agreement with previous calculations and the experimentally reported value of 2.87 GHz (10,34,37).

The vibrational modes of the system are then computed using the phonopy package (56) and used into Eq. (8) to extract the energy fluctuations. A  \( 8 \times 8 \times 3 \)  q-vectors grid with 244 irreducible q-points was required to achieve convergence in the summation of the phonon wave vectors. In a supercell with 215 atoms the number of vibrational modes is 645. The hyperfine coupling is also computed using VASP. The ZFS and the HFI gradients,  \( \nabla_{aj} \)   \( \overset{\leftrightarrow}{\mathcal{D}} \)  and  \( \nabla_{aj} \)   \( \overset{\leftrightarrow}{\mathcal{A}}_{\mathrm{hfi}} \) , are obtained by means of a finite difference real space approach where each atom in the simulation box is separately displaced to a new position  \( R_{0,x} \pm dx \)  along each of the three Cartesian directions.
 

The ground state DFT calculation is then repeated for each of these new atomic configurations. The typical displacements employed here are of the order of  \( dx = 10^{-3} \)  Å. Once we computed the gradients we evaluate  \( \delta E(t) \)  and its auto-correlation function. We can then extract the different  \( \Gamma \)  contributions following the procedure outlined in section (2.1.1). The calculation of the energy fluctuations in the spin-nuclear term does not require the knowledge of the phonon modes and it is less computationally demanding.

## References

1. A. Chatterjee, P. Stevenson, S. De Franceschi, A. Morello, N. P. de Leon, F. Kuemmeth, Semiconductors qubits in practice. Nature Reviews Physics 3, 157-177 (2021).

2. M. Kjaergaard, M. Schwartz, J. Braumüller, P. Krantz, J. I.-J. Wang, S. Gustavsson, W. Oliver, Superconducting qubits: Current state of play. Annual Review of Condensed Matter Physics 11, 369-395 (2020).

3. J. Weber, W. Koehl, J. Varley, A. Janotti, B. Buckley, C. van de Walle, D. Awschalom, Quantum computing with defects. Proc. Natl Acad. Sci. USA 107, 8513-8518 (2010).

4. G. Zhang, Y. Cheng, J.-P. Chou, A. Gali, Material platforms for defect qubits and single-photon emitters. Appl. Phys. Rev. 7, 031308 (2020).

5. G. Wolfowicz, F. Heremans, C. Anderson, S. Kanai, H. Seo, A. Gali, G. Galli, D. Awschalom, Quantum guidelines for solid-state spin defects. Nat. Rev. Mat. 6, 906-925 (2021).

6. R. Schirhagl, K. Chang, M. Lorentz, C. Degen, Nitrogen-vacancy centers in diamond: Nanoscale sensors for physics and biology. Annu. Rev. Phys. Chem. 65, 83-105 (2014).
 

7. M. Doherty, N. Manson, P. Delaney, F. Jelezko, J. Wrachtrup, L. Hollenberg, The nitrogen-vacancy colour centre in diamond. Physics Reports 528, 1-45 (2013).

8. A. Lenef, S. Rand, Electronic structure of the n-v center in diamond: Theory. Phys. Rev. B 53, 13441 (1996).

9. J. Larsson, P. Delaney, Electronic structure of the nitrogen-vacancy center in diamond from first principles theory. Phys. Rev. B 77, 165201 (2008).

10. S. Sangtawesin, T. Brundage, Z. Atkins, J. Petta, Highly tunable formation of nitrogen-vacancy centers via ion implantation. Appl. Phys. Lett. 105, 063107 (2014).

11. N. Mizuochi, P. Neumann, F. Rempp, J. Beck, V. Jacques, P. Siyushev, K. Nakamura, D. Twitchen, H. Watanabe, S. Yamasaki, F. Jelezko, J. Wrachtrup, Coherence of single spins coupled to a nuclear spin bath of varying density. Phys. Rev. B 80, 041201(R) (2009).

12. S. Choi, M. Jain, S. Louie, Mechanism for optical initialization of spin in  \( nv^{-} \)  center in diamond. Phys. Rev. B 86, 041202(R) (2012).

13. E. Bauch, C. Hart, J. Schloss, M. Turner, J. Barry, P. Kehayias, S. Singh, R. Walsworth, Ultralong dephasing times in solid-state spin ensembles via quantum control. Phys. Rev. X 8, 031025 (2018).

14. E. Bauch, S. Singh, J. Lee, C. Hart, J. Schloss, M. Turner, J. Barry, L. Pham, N. Bar-Gill, S. Yelin, R. Walsworth, Decoherence of ensembles of nitrogen-vacancy centers in diamond. Phys. Rev. B 102, 134210 (2020).

15. S. Lin, C. Weng, Y. Yang, J. Zhao, Y. Guo, J. Zhang, L. Lou, W. Zhu, G. Wang, Temperature-dependent coherence properties of nv ensemble in diamond up to 600 k. Phys. Rev. B 104, 155430 (2021).
 

16. N. Bar-Gill, L. Pham, A. Jarmola, D. Budker, R. Walsworth, Solid-state electronic spin coherence time approaching one second. Nat. Commun. 4, 1743 (2013).

17. H. Seo, A. Falk, P. Klimov, K. Miao, G. Galli, D. Awschalom, Quantum decoherence dynamics of divacancy spins in silicon carbide. Nat. Commun. 7, 12935 (2016).

18. A. Norambuena, J. Maze, P. Rabl, R. Coto, Quantifying phonon-induced non-markovianity in color centers in diamond. Phys. Rev. A 101, 022110 (2020).

19. A. Norambuena, E. Muñoz, H. Dinani, A. Jarmola, P. Maletinsky, D. Budker, R. Maze, Spin-lattice relaxation of individual solid-state spins. Phys. Rev. B 97, 094304 (2018).

20. A. Jarmola, V. Acosta, K. Jensen, S. Chemerisov, D. Budker, Temperature-and magnetic-field-dependent longitudinal spin relaxation in nitrogen-vacancy ensembles in diamond. Phys. Rev. Lett. 108, 197601 (2012).

21. J. Gugler, T. Astner, A. Angerer, J. Schmiedmayer, J. Majer, P. Mohn, Ab initio calculation of the spin lattice relaxation time  \( t_{1} \)  for nitrogen-vacancy centers in diamond. Phys. Rev. B 98, 214442 (2018).

22. A. Lunghi, Toward exact predictions of spin-phonon relaxation times: An ab initio implementation of open quantum systems theory. Sci. Adv. 8, eabn7880 (2022).

23. J. Zopes, K. Sasaki, K. Cujia, J. Boss, K. Chang, T. Segawa, K. Itoh, C. Degen, High-resolution quantum sensing with shaped control pulses. Phys. Rev. Lett. 119, 260501 (2017).

24. T. Astner, J. Gugler, A. Angerer, S. Wald, S. Putz, N. Mauser, M. Trupke, H. Sumiya, S. Onoda, J. Isoya, J. Schmiedmayer, P. Mohn, J. Majer, Solid-state electron spin lifetime limited by phononic vacuum modes. Nat. Mater. 17, 313-317 (2018).
 

25. M. Abobeih, J. Cramer, M. Bakker, N. Kalb, M. Markham, D. Twitchen, T. Taminiau, One-second coherence for a single electron spin coupled to a multi-qubit nuclear-spin environment. Nat. Commun. 9, 2552 (2018).

26. V. Acosta, E. Bauch, M. Ledbetter, C. Santori, K.-M. Fu, P. Barclay, R. Beausoleil, H. Linget, J. Roch, F. Treussart, S. Chemerisov, W. Gawlik, D. Budker, Diamonds with a high density of nitrogen-vacancy centers for magnetometry applications. Phys. Rev. B 80, 115202 (2009).

27. C. Degen, Scanning magnetic field microscope with a diamond single-spin sensor. Appl. Phys. Lett. 92, 243111 (2008).

28. J. Taylor, P. Cappellaro, L. Childress, L. Jiang, D. Budker, P. Hemmer, A. Yacoby, R. Walsworth, M. Lukin, High-sensitivity diamond magnetometer with nanoscale resolution. Nat. Phys. 4, 810-816 (2008).

29. C. Abeywardana, V. Stepanov, F. Cho, S. Takahashi, Magnetic resonance spectroscopy using a single nitrogen-vacancy center in diamond. Proc. SPIE 9269, Quantum and Nonlinear Optics III, 92690K (2014).

30. E. van Oort, P. Stroomer, M. Glasbeek, Low-field optically detected magnetic resonance of a coupled triplet-doublet defect pair in diamond. Phys. Rev. B 42, 8605 (1990).

31. R. Epstein, F. Mendoza, Y. Kato, D. Awschalom, Anisotropic interactions of a single spin and dark-spin spectroscopy in diamond. Nat. Phys. 1, 94-98 (2005).

32. H. Carr, E. Purcell, Effects on diffusion of free precession in nuclear magnetic resonance experiments. Phys. Rev. 94, 630 (1954).
 

33. S. Meiboom, D. Gill, Modified spin-echo method for measuring nuclear relaxation times. Review of Scientific Instruments 29, 688 (1958).

34. L. Childress, M. Dutt, J. Taylor, A. Zibrov, F. Jelezko, J. Wrachtrup, P. Hemmer, M. Lukin, Coherent dynamics of coupled electron and nuclear spin qubits in diamond. Science 314, 281-285 (2006).

35. C. Ryan, J. Hodges, D. Cory, Robust decoupling techniques to extend quantum coherence in diamond. Phys. Rev. Lett. 105, 200402 (2010).

36. B. Naydenov, F. Dolde, L. Hall, C. Shin, H. Fedder, L. Hollenberg, F. Jelezko, J. Wrachtrup, Dynamical decoupling of a single-electron spin at room temperature. Phys. Rev. B 83, 081201(R) (2011).

37. T. Van der Sar, Z. Wang, M. Blok, H. Bernien, T. Taminiau, D. Toyli, D. Lidar, D. Awschalom, R. Hanson, V. Dobrovitski, Decoherence-protected quantum gates for a hybrid solid-state spin register. Nature 484, 82-86 (2012).

38. J. Liu, A. Neukirch, O. Prezhdo, Phonon-induced pure-dephasing of luminescence, multiple exciton generation, and fission in silicon clusters. J. Chem. Phys. 139, 164303 (2013).

39. H. Kamisaka, S. Kilina, K. Yamashita, O. Prezhdo, Ultrafast vibrationally-induced dephasing of electronic excitations in pbse quantum dots. Nano Lett. 6, 2295-2300 (2006).

40. S. Palato, H. Seiler, P. Nijjar, O. Prezhdo, P. Kambhampati, Atomic fluctuations in electronic materials revealed by dephasing. PNAS 117, 11940-11946 (2020).

41. M. Mallus, M. Aghtar, S. Chandrasekaran, G. Lüdemann, M. Elstner, U. Kleinekathöfer, Relation between dephasing time and energy gap fluctuations in biomolecular systems. J. Phys. Chem. Lett. 7, 1102-1108 (2016).
 

42. O. Prezhdo, P. Rossky, Evaluation of quantum transition rates from quantum-classical molecular dynamics simulations. J. Chem. Phys. 107, 5863 (1997).

43. P. Hohenberg, W. Kohn, Inhomogeneous electron gas. Phys. Rev. 136, 864 (1964).

44. W. Kohn, L. Sham, Self-consistent equations including exchange and correlation effects. Phys. Rev. 140, 1133 (1965).

45. B. Kaduk, T. Kowalczyk, T. van Voorhis, Constrained density functional theory. Chem. Rev. 112, 321-370 (2012).

46. V. Ivády, I. Abrikosov, A. Gali, First principles calculation of spin-related quantities for point defect qubit research. npj Comput. Mater. 4, 76 (2018).

47. V. Ivanov, J. Simoni, Y. Lee, W. Liu, K. Jhuria, W. Redjem, Y. Zhiyenbayev, C. Papapanos, W. Qarony, B. Kante, A. Persaud, T. Schenkel, L. Z. Tan, Effect of localization on photoluminescence and zero-field splitting of silicon color centers (2022).

48. G. Kresse, J. Fürthmuller, Efficiency of ab initio total energy calculations for metals and semiconductors using a plane-wave basis set. Computational Materials Science 6, 15-50 (1996).

49. G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 59, 1758 (1999).

50. S. Schmitt-Rink, S. Mukamel, K. Leo, J. Shah, D. Chemla, Stochastic theory of time-resolved four-wave mixing in interacting media. Phys. Rev. A 44, 2124 (1991).

51. T. Biktagirov, W. Schmidt, U. Gerstmann, Calculation of spin-spin zero-field splitting within periodic boundary conditions: Towards all-electron accuracy. Phys. Rev. B 97, 115135 (2018).
 

52. R. Frosch, H. Foley, Magnetic hyperfine structure in diatomic molecules. Phys. Rev. 88, 1337 (1952).

53. A. Alkauskas, B. Buckley, D. Awschalom, C. van de Walle, First-principles theory of the luminescence lineshape for the triplet transition in diamond NV centres. New J. Phys. 16, 073026 (2014).

54. L. Hall, J. Cole, L. Hollenberg, Analytic solutions to the central-spin problem for nitrogen-vacancy centers in diamond. Phys. Rev. B 90, 075201 (2014).

55. J. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865 (1996).

56. A. Togo, I. Tanaka, First principles phonon calculations in materials science. Scripta Materialia 108, 1-5 (2015).

## Acknowledgments

## Funding

This work was supported by the Office of Science, Office of Fusion Energy Sciences, of the U.S. Department of Energy, under Contract No. DE-AC02-05CH11231. JS, VI and LZT were also supported by the Molecular Foundry, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231. This research used resources of the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231.
 

## Author contributions

JS and LZT worked on the theory and methodologies, JS and VI worked on the calculations and data visualization, LZT and TS supervised the work and JS, VI, LZT, TS wrote the manuscript.

## Competing interests

The authors declare no competing financial interest.

## Data and materials availability

The data supporting the different figures and tables are available from the corresponding author upon reasonable request.
 

## 5 Figures and Tables

![](./images/867759998334140888_1.jpg)

Fig. 1. Structure of the NV defect, with the gradients of the zz zero field splitting component,  \( \nabla_{aj}\otimes_{zz} \) , represented by arrows. The vectors associated to the three carbons surrounding the vacancy have the same trigonal symmetry of the defect.
 
![](./images/867759998334140888_2.jpg)

Fig. 2. Evaluation of the pure dephasing time  \( 1/\Gamma[\text{pure}] \)  due to the first order spin-phonon coupling in absence of nuclear spin impurities. Our result (black line with blue bar indicating the confidence interval) is compared with experimental data from Ref. (A) (16) and Ref. (B) (25).
 
![](./images/867759998334140888_3.jpg)

![](./images/867759998334140888_4.jpg)

Fig. 3. Atoms and phonon resolved  \( 1/\Gamma[pure] \)  times. (Upper panel) atom-resolved  \( 1/\Gamma[pure] \)  is shown as a function of distance from the vacancy, expressed as a fraction of the length of the  \( 3\times3\times3 \)  supercell. (Lower panel) phonon resolved dephasing time as a function of the phonon frequency.
 
![](./images/867759998334140888_5.jpg)

Fig. 4. Comparison between  \( 1/\Gamma \)  due to the spin-phonon term and the HFI-spin-phonon term in seconds at different  \( C^{13} \)  concentrations.
 
![](./images/867759998334140888_6.jpg)

Fig. 5. Calculation of the inhomogeneous dephasing  \( 1/\Gamma[\text{disorder}] \)  in seconds obtained at different magnetic field amplitudes  \( 50 G \)  (circle points),  \( 100 G \)  (squares),  \( 500 G \)  (stars) and  \( 1000 G \)  (triangles). The two additional data points are experimental data from Ref. (C) (I).
 

<table><tr><td>\( \Gamma[\text{pure}]^{-1} \)</td><td>4.8 ± 3.5 s</td><td>homogeneous</td><td>irreversible</td></tr><tr><td>\( \Gamma_{A}[\text{disorder}]^{-1} \)</td><td>\( 10^{8} \)  s</td><td>inhomogeneous</td><td>irreversible</td></tr><tr><td>\( \Gamma_{B}[\text{disorder}]^{-1} \)</td><td>\( 10^{-4} \)  s</td><td>inhomogeneous</td><td>reversible</td></tr></table>

Tab. 1. Summary of dephasing mechanisms considered in this work, together with computed dephasing times and associated properties. Homogeneous dephasing refers to the fast-modulation case where the decay rate of energy level fluctuations is fast compared to the amplitude of fluctuations. The reversible dephasing can be removed by dynamical decoupling. Label (A) indicates (sp-ph-nu) and (B) (sp-nu). We assume a concentration of nuclear spins of 0.5% and for the (sp-nu) term the applied magnetic field has a magnitude of 50 G.
 

## 6 Supplementary materials

![](./images/867759998334140888_7.jpg)

Fig. SM1. Structure of the NV defect, with the gradients of the zz zero field splitting component,  \( \nabla_{aj}\mathcal{D}_{zz} \) , represented by arrows. The gradient for the three carbons close to the vacancy is much larger in magnitude compared to the other atoms.
 
