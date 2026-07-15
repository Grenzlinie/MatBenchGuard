
# Light-induced shear phonon splitting and instability in bilayer graphene

Habib Rostami \( ^{1,2,*} \) 

 \( ^{1} \) Department of Physics, University of Bath, Claverton Down, Bath BA2 7AY, United Kingdom  
 \( ^{2} \) Nordita, KTH Royal Institute of Technology and Stockholm University, Hannes Alfuvéns väg 12, 10691 Stockholm, Sweden  
(Dated: January 4, 2023)

Coherent engineering of landscape potential in crystalline materials is a rapidly evolving research field. Ultrafast optical pulses can manipulate low-frequency shear phonons in van der Waals layered materials through the dynamical dressing of electronic structure and photoexcited carrier density. In this work, we provide a diagrammatic formalism for nonlinear Raman force and implement it to shear phonon dynamics in bilayer graphene. We predict a controllable splitting of double degenerate shear phonon modes due to light-induced phonon mixing and renormalization according to a coherent nonlinear Raman force mechanism. Intriguingly, we obtain a light-induced shear phonon softening that facilitates structural instability at a critical field amplitude for which the shear phonon frequency vanishes. The phonon splitting and instability strongly depend on the laser intensity, frequency, chemical potential, and temperature of photoexcited electrons. This study motivates future experimental investigation of the optical fine-tuning and regulation of shear phonons and layer stacking order in layered van der Waals materials.

## I. INTRODUCTION

Exotic emergent phenomena in quantum systems can be generated via photoexcitation by ultrafast optical drives  \( [1-5] \) . Depending on the intensity of the pump laser, we can excite and disentangle collective modes, switch the macroscopic phase of the system, dynamically engineer critical phenomena, and render robust nonlinear couplings among the different degrees of freedom in the quantum materials  \( [6-8] \) . Optical switching and photoinduced transitions correspond to the dynamical modification of the free energy landscape that is not accessible in thermal equilibrium. Photoinduced non-thermal and coherent control of correlated and topological quantum materials  \( [9] \)  is being under investigation in multiple ways, such as Floquet-Bloch dressed single-particle states  \( [10] \)  and optical dressing of many-body interaction couplings  \( [11, 12] \) . Manipulating and fine-tuning the structural phase of quantum materials by ultrashort laser pulses open a pathway to regulate quantum devices. For instance, substantial lattice deformations are reported induced by intense mid-infrared optical pulse irradiation, e.g., dynamically generated ferroelectricity and shear strain  \( [13, 14] \) . Large photoinduced deformations are due to resonance with a vibration mode, strong Raman force, and nonlinear phonon couplings  \( [8, 13-17] \) .

Shear phonons in bilayer and multi-layer of 2D materials, such as the family of graphene, transition metal dichalcogenides (TMDs) and hexagonal Boron Nitride (hBN), correspond to the lateral sliding of atomic layers on each other \( ^{[18-26]} \) . Shear phonon excitation can coherently alter the staking order of layers  \( [27, 28] \) , and the electronic topology  \( [29] \) . Light-induced displacive dynamics  \( [30-41] \)  of coherent shear phonons in van der Waals (vdW) layered materials such as multilayer graphene,  \( WTe_{2} \) , and  \( MoTe_{2} \)   \( [27-29, 42-45] \)  is a promising nondestructive mechanism for controlling 2D materials properties. The shear mode in bilayer graphene is a double degenerate Raman-active optical mode and it has a low-frequency  \( \hbar\Omega_{0} \approx 3.9meV \)  due to the weak vdW interlayer force  \( [18] \) . The energy and the intensity of the Raman peak for the shear mode (the C peak) strongly depend on the number of layers and inter-layer coupling. Accordingly, the spectroscopy of interlayer Raman modes is an effective method for determining layer numbers and stacking configurations, and it provides a unique opportunity to explore interlayer couplings. Driving coherent shear phonon in  \( MoTe_{2} \)  causes a first-order phase transition from an inversion symmetric  \( 1T' \)  structure to the non-centrosymmetric  \( 1T_{d} \)  phase  \( [27, 44] \) . Time and angle-resolved photoemission spectroscopy (tr-ARPES) of the Weyl semimetal  \( T_{d}-WTe_{2} \) , indicates coherent shear phonon-mediated control of the electronic structure  \( [45] \) . An optical switching from an ABA to ABC stacking is experimentally obtained by laser irradiation on trilayer graphene  \( [42] \)  that might be because of the coherent shear phonon excitation.

This paper studies the dynamical engineering of lattice potential for the shear dynamics in vdW layered materials caused by a linear polarised light field  \( \mathbf{E}(t) \) . The impact of second and third-order Raman susceptibilities gives rise to light-induced corrections to the lattice potential:

 \[ U=\frac{1}{2}\sum_{\alpha\beta}[\Omega_{0}^{2}\delta_{\alpha\beta}-\mathcal{G}_{\alpha\beta}(\mathbf{E})]Q_{\alpha}Q_{\beta}-\sum_{\alpha}\mathcal{F}_{\alpha}^{(2)}(\mathbf{E})Q_{\alpha}, \quad (1) \] 

where  \( \mathbf{Q} = (Q_{x}, Q_{y}) \)  is the shear phonon displacement with  \( \Omega_{0} \)  being the unperturbed phonon frequency. Displacive Raman shear force described as a second-order effect  \( \mathcal{F}^{(2)} \propto EE^{*} \)  in bilayer graphene has been previously investigated [46]. Here, we define the third-order Raman
 

shear force as  \( \mathcal{F}^{(3)} = \stackrel{\leftrightarrow}{\mathcal{G}} \cdot \mathbf{Q} \propto Q E E^{*} \)  which can renormalize shear phonons and lead to a mode splitting. In particular, it can cause the instability of atomic layers to slide and form stable or metastable phases with different layer-stacking orders due to the softening of shear phonon frequency under the influence of the light field. The  \( G_{\alpha\beta} \)  coupling can be interpreted as a light-induced self-energy correction  \( \Sigma_{\alpha\beta}(\mathbf{E}) = -\mathcal{G}_{\alpha\beta}(\mathbf{E}/2\Omega_{0} \)  to the phonon's dynamical matrix. As the central result, here, we develop a diagrammatic formalism to model the impact of third-order Raman force (or light-induced phonon self-energy) on the displacive dynamics of shear phonons in layered materials. We obtain a dynamical renormalization of the shear phonons by incident light intensity leading to the splitting of the double degenerate shear phonons. We predict a lattice instability where the shear phonon frequency vanishes at a critical field amplitude. We show that the field-induced phonon splitting and instability are highly tunable by the incident laser intensity, frequency at given electronic doping, and temperature. Our theoretical model based on the non-equilibrium Green's function can be systematically employed in ab initio computations to study the optical engineering of shear phonon in layered materials.

The rest of the paper is structured in four sections. In Section II, we provide details of the diagrammatic method for the third-order Raman force and develop a perturbative theory for optically dressed phonon's dynamical matrix. In Section III, we summarize the mixed couplings of electrons, phonons, and photons in addition to light-matter and electron-phonon couplings in bilayer graphene. In Section IV, we discuss numerical results for the light-induced phonon renormalization and, thus, its effect on the optical modulation of the shear phonon spectral function, shear mode splitting, and the light-induced shear instability. Finally, we summarize our theoretical finding, discuss it in connection with experiments, and highlight the implication of light-induced phonon renormalization in other heterostructures of 2D materials.

## II. METHOD

Stimulated Raman effect is an efficient mechanism to excite Raman-active vibrational modes [47]. The dipole moment of Raman-active phonon is linearly proportional to the light field  \( \mu_{b} = \alpha_{bc}E_{c} \)  where the polarizability tensor  \( \alpha_{bc} \)  depends on the phonon displacement vector Q. The electromagnetic potential energy thus follows  \( U = -\mu_{b}E_{b} = -\alpha_{bc}E_{b}E_{c} \) . The corresponding Raman force driving atoms to oscillate follows a second-order nonlinear process [47]

 \[ \mathcal{F}_{a}^{(2)}=-\left[\frac{\partial U}{\partial Q_{a}}\right]_{Q\rightarrow0}=\sum_{b c}\left[\frac{\partial\alpha_{b c}}{\partial Q_{a}}\right]_{Q\rightarrow0}E_{b}E_{c}. \quad (2) \] 

Therefore the lowest-order Raman force is finite as long as the Raman susceptibility is non-vanishing, i.e.,  \( \sigma_{abc}^{(2)} = \partial\alpha_{bc}/\partial Q_{a} \neq 0 \) . For large displacement, the higher-order Raman force should also be considered, which can dramatically impact phonon renormalization and lattice dynamics. The leading higher-order Raman force depends linearly on the phonon displacement and quadratically on the light field. Therefore, it is described by a third-order nonlinear mechanism.

 \[ \mathcal{F}_{a}^{(3)}=\sum_{b c d}\left[\frac{\partial^{2}\alpha_{c d}}{\partial Q_{a}\partial Q_{b}}\right]_{Q\rightarrow0}Q_{b}E_{c}E_{d}. \quad (3) \] 

Formally, we have  \( \mathcal{F}_{a}^{(3)} = \mathcal{G}_{ab}Q_{b} \)  in which  \( G_{ab} \)  generates a phonon self-energy in terms of a third-order Raman susceptibility  \( \sigma_{cbd}^{(3)} = \partial^{2}\alpha_{cd}/\partial Q_{a}\partial Q_{b} \)  and the incident light intensity. An anisotropic  \( G_{ab} \)  breaks the degeneracy of Cartesian shear modes and renormalizes the phonon's frequency and linewidth.

To model coherent shear phonons in bilayer systems, we first provide a general theory for the Raman force and phonon self-energy using the Green's function method and diagrammatic framework. We decompose the total Hamiltonian of the system in different parts  \( H = H_{e} + H_{p} + H_{e-p} + H_{lm} \)  which consists of electronic kinetic Hamiltonian  \( H_{e} \) , harmonic phonon Hamiltonian  \( H_{p} \) , electron-phonon interaction  \( H_{ep} \)  and finally the light-matter interaction  \( H_{lm} \) . The electronic kinetic Hamiltonian reads  \( \hat{H}_{e} = \sum_{\mathbf{p}} \hat{\psi}_{\mathbf{p}}^{\dagger} \hat{\mathcal{H}}(\mathbf{p}) \hat{\psi}_{\mathbf{p}} \)  where  \( \hat{\psi}_{\pmb{p}} \)  is the fermion annihilation spinor field at momentum p. The harmonic shear phonon Hamiltonian with zero momentum q = 0 can be written in terms of ladder operators  \( \hat{H}_{p} = \sum_{\lambda} \hbar \Omega_{0} \hat{b}_{\lambda}^{\dagger} \hat{b}_{\bar{\lambda}} \)  where  \( \hat{b}_{\lambda} \)  is the phonon annihilation operator. We only consider the zone center phonon modes with a vanishing wave vector q = 0, and thus the phonon displacement vector is defined as

 \[ \hat{Q}_{\lambda}=\sqrt{\frac{\hbar}{\rho S\Omega_{0}}}(\hat{b}_{\lambda}+\hat{b}_{\lambda}^{\dagger}) \quad (4) \] 

in which  \( \lambda = x, y \)  indicates two Cartesian mode components, note that S stands for the area of 2D material, and  \( \rho \)  is the mass density. Including both one-phonon and two-phonon couplings to electrons, the electron-phonon interaction Hamiltonian follows

 \[ \begin{align*}\hat{\mathcal{H}}_{e-p}=\sum_{\mathbf{p}}\sum_{a}\hat{\psi}_{\mathbf{p}}^{\dagger}\hat{\mathcal{M}}_{a}^{(1)}(\mathbf{p})\hat{\psi}_{\mathbf{p}}\hat{Q}_{a}\\+&\sum_{\mathbf{p}}\sum_{a b}\hat{\psi}_{\mathbf{p}}^{\dagger}\hat{\mathcal{M}}_{a b}^{(2)}(\mathbf{p})\hat{\psi}_{\mathbf{p}}\hat{Q}_{a}\hat{Q}_{b}.\end{align*} \quad (5) \] 

Note that  \( \hat{\mathcal{M}}_{a}^{(1)} \)  and  \( \hat{\chi}_{ab}^{(2)} \)  stand for the one- and two-phonon-electron couplings' matrix elements, respectively. Utilizing this effective lattice potential and the Heisenberg equation of motion, we obtain the equation of motion for coherent phonon displacement amplitude  \( Q_{a} \) :

 \[ \begin{aligned}&\frac{\partial^{2}Q_{a}(t)}{\partial t^{2}}+\Gamma_{p}\frac{\partial Q_{a}(t)}{\partial t}+\Omega_{0}^{2}Q_{a}(t)=\frac{\mathcal{F}_{a}(t)}{\rho}\\&+\frac{1}{\rho}\sum_{b}\mathcal{G}_{a b}^{i n s.}(t)Q_{b}(t)+\frac{1}{\rho}\sum_{b}\int d t^{\prime}\mathcal{G}_{a b}^{r e t.}(t,t^{\prime})Q_{b}(t^{\prime})\end{aligned} \quad (6) \]
 

where  \( \Omega_{0} \)  is the shear phonons frequency,  \( \Gamma_{p} \)  stands for the phenomenological damping frequency of phonons. The leading-order Raman force is given as the expectation value of the one-phonon coupling to electrons:

 \[ \mathcal{F}_{a}^{(2)}(t)=-\frac{1}{S}\sum_{\mathbf{p}}\left\langle\hat{\psi}_{\mathbf{p}}^{\dagger}\hat{\mathcal{M}}_{a}^{(1)}(\mathbf{p})\hat{\psi}_{\mathbf{p}}\right\rangle\big|_{\mathbf{Q}\rightarrow\mathbf{0}}. \quad (7) \] 

The nonlinear force reveals two different dynamical forms of the light-induced phonon self-energy term  \( G_{ab} \)  that we label as instantaneous  \( \mathcal{G}_{ab}^{ins.}(t) \)  and retarded  \( \mathcal{G}_{ab}^{ret.}(t,t') \)  couplings. The instantaneous coupling is obtained as the expectation value of the two-phonon coupling matrix element

 \[ \mathcal{G}_{a b}^{i n s.}(t)=-\frac{1}{S}\left[\sum_{\mathbf{p}}\left\langle\hat{\psi}_{\mathbf{p}}^{\dagger}\hat{\mathcal{M}}_{a}^{(2)}(\mathbf{p})\hat{\psi}_{\mathbf{p}}\right\rangle\right]_{\mathbf{Q}\rightarrow\mathbf{0}}. \quad (8) \] 

While the retarded coupling is given by the variational derivative of the Raman force versus the phonon displacement field:

 \[ \mathcal{G}_{a b}^{r e t.}(t,t^{\prime})=-\frac{1}{S}\left[\frac{\delta}{\delta Q_{b}(t^{\prime})}\sum\left\langle\hat{\psi}_{\mathbf{p}}^{\dagger}\hat{\mathcal{M}}_{a}^{(1)}(\mathbf{p})\hat{\psi}_{\mathbf{p}}\right\rangle\right]_{\mathbf{Q}\rightarrow\mathbf{0}}. \quad (9) \] 

Note that  \( \langle\ldots\rangle \)  indicates quantum statistical averaging. In centrosymmetric systems, Raman-active phonons are infrared-inactive; therefore, they couple to light indirectly. The direct light-matter interaction is only through the coupling to electrons. The coupling of incident light field to electrons can be modeled by Peierls substitution  \( p \rightarrow p + eA(t) \)  in the kinetic and the electron-phonon interaction Hamiltonian terms. Considering the homogeneous vector potential  \( \mathbf{A}(t) \) , the electric field reads  \( \mathbf{E}(t) = -\partial_{t}\mathbf{A}(t) \)  and thus  \( \mathbf{E}(\omega) = i\omega\mathbf{A}(\omega) \) . Formally, the light-matter interaction Hamiltonian consists of two parts: photon-electron term and photon-electron-phonon term  \( \hat{\mathcal{H}}_{lm} = \hat{\mathcal{H}}_{\mathbf{p}h-e} + \hat{\mathcal{H}}_{p\mathbf{h}-e-p} \) . The photon-electron term follows

 \[ \begin{align*}\mathcal{H}_{ph-e}=&-\sum_{\mathbf{p}}\hat{\psi}_{\mathbf{p}}^{\dagger}\Big\{\sum_{a}\hat{j}_{a}(\mathbf{p})A_{a}(t)\\&+\frac{1}{2}\sum_{ab}\hat{\gamma}_{ab}(\mathbf{p})A_{a}(t)A_{b}(t)+\cdots\Big\}\hat{\psi}_{\mathbf{p}}\end{align*} \quad (10) \] 

where  \( \hat{j}_{a} \)  is called the paramagnetic current operator, and  \( \hat{\gamma}_{ab} \)  is known as the diamagnetic current operator as well as the Raman vertex [48, 49]. The photon-electron-phonon interaction Hamiltonian is given by the light field dependence of the electron-phonon interaction,  \( \mathcal{M}_{a}^{(1)}(\mathbf{p} + e\mathbf{A}(t)) \)  and  \( \mathcal{M}_{ab}^{(2)}(\mathbf{p} + e\mathbf{A}(t)) \) . By expanding electron-phonon matrix elements up to second-order in  \( \mathbf{A}(t) \) , we obtain the photon-electron-phonon (PEP) interaction Hamiltonian  \( \hat{\mathcal{H}}_{ph-e-p} = \sum_{\mathbf{p}} \hat{\psi}_{\mathbf{p}}^{\dagger} \hat{\Xi}_{\mathbf{p}} \hat{\psi}_{\mathbf{p}} \)  where
 \[ \hat{\Xi}_{\mathbf{p}} = \sum_{ab} A_{a}(t) Q_{b}(t) \left\{ \hat{\Theta}_{ab}^{(1)}(\mathbf{p}) + \sum_{c} \hat{\Theta}_{abc}^{(2)}(\mathbf{p}) Q_{c}(t) \right\} + \frac{1}{2} \sum_{abc} A_{a}(t) A_{b}(t) Q_{c}(t) \left\{ \hat{\Delta}_{abc}^{(1)}(\mathbf{p}) + \sum_{d} \hat{\Delta}_{abcd}^{(2)}(\mathbf{p}) Q_{d}(t) \right\}. \] 

(11)

Having defined all vertex couplings, we are equipped to evaluate the Raman force and the light-induced phonon self-energy. Because the Raman phonon is even under parity, the leading contribution to the Raman force is second order in the light field, which follows

 \[ \mathcal{F}_{a}^{(2)}(t)=\sum_{b c}\sum_{\omega_{1},\omega_{2}}e^{i(\omega_{1}+\omega_{2})t}\sigma_{a b c}^{(2)}(\omega_{1},\omega_{2})E_{b}(\omega_{1})E_{c}(\omega_{2}). \quad (12) \] 

Similarly, the light-induced instantaneous coupling is given by

 \[ \mathcal{G}_{a b}^{i n s.}(t)=\sum_{c d}\sum_{\omega_{1},\omega_{2}}e^{i(\omega_{1}+\omega_{2})t}\Pi_{a b c d}^{r e t.}(\omega_{1},\omega_{2})E_{c}(\omega_{1})E_{d}(\omega_{2}). \quad (13) \] 

Finally, one can evaluate the light-induced retarded coupling as follows

 \[ \begin{align*}\mathcal{G}_{a b}^{r e t.}(t,t^{\prime})&=\sum_{c d}\sum_{\omega_{1},\omega_{2}}e^{i(\omega_{1}+\omega_{2})t}\Pi_{a b c d}^{r e t.}(\omega_{1},\omega_{2},t-t^{\prime})\\&\quad\times E_{c}(\omega_{1})E_{d}(\omega_{2}).\end{align*} \quad (14) \] 

Notice that  \( \Pi_{abcd}^{ret.}(\omega_{1},\omega_{2},\tau)=\sum_{\omega_{3}}e^{i\omega_{3}\tau}\Pi_{abcd}^{ret.}(\omega_{1},\omega_{2},\omega_{3}) \)  where  \( \omega_{3} \)  is the phonon frequency. Response function  \( \Pi_{abcd}^{ins.} \)  contributes to the instantaneous phonon self-energy since it originates from the simultaneous coupling of two phonons to electrons. On the other hand, the retarded response function  \( \Pi_{abcd}^{ret.} \)  contains memory effects where the past dynamics of phonons can influence their future motion.

The light-induced rigid displacement directly depends on the displacive Raman force that is the rectified part of the force in a second-order nonlinear process [46]. We consider monochromatic incident light-field  \( \mathbf{E}(t)=E_{0}\hat{\mathbf{e}}e^{-i\omega t}+c.c. \)  with  \( \hat{\varepsilon} \)  being the linear polarization unit vector. The displacive force is thus given by the rectification process (i.e.,  \( \omega_{1}^{2}=-\omega_{2}^{2}=\omega \) ) that leads to the following time-independent Raman force:

 \[ \mathcal{F}_{a}^{\mathrm{D}}=\sum_{b c}\sigma_{a b c}^{(2)}(\omega,-\omega)E_{b}(\omega)E_{c}^{*}(\omega). \quad (15) \] 

Similarly, the rectified component of the instantaneous phonon-phonon coupling reads

 \[ \mathcal{G}_{a b}^{i n s.}=\sum_{c d}\Pi_{a b c d}^{i n s.}(\omega,-\omega)E_{c}(\omega)E_{d}^{*}(\omega), \quad (16) \] 

and the retarded light-induced phonon-phonon coupling follows

 \[ \mathcal{G}_{a b}^{r e t.}(t-t^{\prime})=\sum_{c d}\Pi_{a b c d}^{r e t.}(\omega,-\omega,t-t^{\prime})E_{c}(\omega)E_{d}^{*}(\omega). \quad (17) \]
 
![](./images/867774263942185493_1.jpg)

FIG. 1. Feynman diagrams for light-induced phonon self-energy. Diagrams given in panel (a-e) and (f-i) for  \( G^{ins.} \)  and  \( G^{ret.} \)  couplings, respectively. Dashed and wave lines represent external phonon and photon fields, respectively. The solid lines represent electron propagators.

It is worth highlighting that the second harmonic parts of  \( G_{ab}^{ins.} \)  and  \( G_{ab}^{\prime\prime} \sim e^{i2\omega t} \)  do not contribute noticeably due to its convolution with the slow oscillation of the ion displacement  \( Q_{a} \sim e^{i\Omega_{0}t} \)  since  \( \omega \gg \Omega_{0} \) . In this regard, the rectified parts of  \( G_{ab}^{ins.} \)  and  \( G_{ab}^{\prime\prime} \)  play the dominant role. Eventually, the phonon equation of motion coherently dressed by the light field is given by

 \[ \begin{aligned}&\frac{\partial^{2}Q_{a}(t)}{\partial t^{2}}+\Gamma_{p}\frac{\partial Q_{a}(t)}{\partial t}+\Omega_{0}^{2}Q_{a}(t)=\frac{\mathcal{F}_{\mathrm{D}}^{\mathrm{I}}}{\rho}+\frac{1}{\rho}\sum_{b}\mathcal{G}_{a b}^{i n s.}Q_{b}(t)\\&+\frac{1}{\rho}\sum_{b}\int d t^{\prime}\mathcal{G}_{a b}^{\prime\prime t.}(t-t^{\prime})Q_{b}(t^{\prime}).\\ \end{aligned} \quad (18) \] 

We employ a diagrammatic formalism to estimate numerical values of the Raman force [46] and phonon self-energy. Here, the main focus is on the light-induced renormalization and mixing of shear phonons. The Feynman diagrams for the instantaneous and retarded couplings thus are given in Fig. 1a-d and Fig. 1e-i, respectively. To quantitatively analyze the spectral function and the splitting of shear phonons, we microscopically explore the coherent dynamics of shear modes in bilayer graphene in the remaining part of the paper.

## III. LIGHT-MATTER AND ELECTRON-PHONON COUPLINGS

Bilayer graphene consists of two single layers of graphene sheets offset from each other in the xy plane. The low-energy quasiparticles follow a two-band Hamiltonian around the corners of the hexagonal Brillouin zone [50]

 \[ \hat{H}_{\mathbf{P}}=-\frac{1}{2m}\{(p_{x}^{2}-p_{y}^{2})\hat{\sigma}_{x}+2\tau p_{x}p_{y}\hat{\sigma}_{y}\}-\mu\hat{I}. \quad (19) \] 

Note that  \( p = \hbar k \)  is the momentum vector,  \( \tau = \pm \)  indicates two K and  \( K' \)  valley points, the identity matrix  \( \hat{I} \)  and Pauli matrices  \( \hat{\sigma}_{x} \)  and  \( \hat{\gamma}_{y} \)  are in the layer pseudospin basis, and  \( \mu \)  is the chemical potential. In our convention, the x-direction shows a zigzag orientation of the honeycomb lattice [51]. The effective mass is given by  \( 1/2m \approx v^{2}/|\gamma_{1}| \)  with  \( v \approx 10^{6}m/s \)  and vertical inter-layer hopping energy  \( \gamma_{1} \approx -0.4eV \)  [52]. Having the in-plane displacement  \( \mathbf{Q}^{(\ell)}(\mathbf{r}) \)  of two layers  \( \ell = 1, 2 \) , the shear phonon displacement is the asymmetric component:

 \[ \mathbf{Q}=\frac{\mathbf{Q}^{(1)}-\mathbf{Q}^{(2)}}{\sqrt{2}}. \quad (20) \] 

The shear displacement vector is even under parity  \( \mathcal{P} \)  since  \( \mathcal{P}\{\mathbf{Q}^{(1)},\mathbf{Q}^{(2)}\}\mathcal{P}^{-1}=-\{\mathbf{Q}^{(2)},\mathbf{Q}^{(1)}\} \)  leading to  \( \mathcal{PQP}^{-1}=Q \) . Therefore, the shear mode is a Raman-active but IR-inactive phonon. We consider the coupling of electrons to one and two photons given by  \( \hat{j}_{\alpha}=-e\partial_{p_{\alpha}}\hat{H}_{\mathbf{P}} \)  and  \( \hat{\gamma}_{\alpha\beta}=-e^{2}\partial_{p_{\alpha}}\partial_{p_{\beta}}\hat{H}_{\mathbf{P}} \) , respectively. The coupling of electrons to one and two photons are thus given by

 \[ \begin{align*}(\hat{j}_{x},\hat{j}_{y})&=\frac{e}{m}(p_{x}\hat{\sigma}_{x}+\tau p_{y}\hat{\sigma}_{y},-p_{y}\hat{\gamma}_{x}+\tau p_{x}\sigma_{y}),\\(\hat{\gamma}_{xx}&=-\hat{\gamma}_{yy},\hat{\gamma}_{xy}=\hat{\gamma}_{yx})=\frac{e^{2}}{m}(\hat{\sigma}_{x},\tau\hat{\sigma}_{y}).\end{align*} \quad (21) \] 

The electron-phonon couplings are obtained using a four-band tight-binding model following the approach developed in Ref. [46] providing the detailed analysis of electron coupling to shear phonons in bilayer graphene using tight-binding and  \( k \cdot p \)  models– see also Refs. [53–55]. Accordingly, the couplings of electrons to shear phonons in the low-energy model read [46]

 \[ \begin{align*}(\hat{\mathcal{M}}_{x}^{(1)},\hat{\mathcal{M}}_{y}^{(1)})&\approx\mathcal{M}^{(1)}(\tau\hat{\sigma}_{y},\hat{\sigma}_{x}),\ $ \hat{\mathcal{M}}_{xx}^{(2)}&=-\hat{\mathcal{M}}_{yy}^{(2)},\hat{\mathcal{M}}_{xy}^{(2)}=\hat{\mathcal{M}}_{yx}^{(2)})\approx\mathcal{M}^{(2)}(\hat{\sigma}_{x},\tau\hat{\sigma}_{y}).\end{align*} \quad (22) \] 

Electron-phonon coupling can depend on the light field, and this leads to mixed PEP couplings which are ob-
 
![](./images/867774263942185493_2.jpg)

![](./images/867774263942185493_3.jpg)

![](./images/867774263942185493_4.jpg)

FIG. 2. Light-induced retarded self-energy coupling versus the laser frequency. Panel (a) indicates the imaginary and real parts of  \( \Pi_{I}^{ret} \)  versus the incident laser frequency at zero electronic temperature  \( T_{e}=0 \)  and  \( \Gamma_{e}=0.001meV \) . Panel (b) and (c) respectively illustrate the imaginary and real parts of  \( \Pi_{I}^{ret} \) . at  \( \Gamma_{e}=1meV \)  and different values of electronic temperature  \( T_{e} \) . We set  \( \mu=200meV \) , and  \( \hbar\Omega_{0}=3.9meV \)  in this figure.

of the instantaneous coupling is obtained analytically using the effective low-energy Hamiltonian, and it reads  \( \Pi^{ins.}(\bar{\omega}_{1},\bar{\omega}_{2})=\Pi_{0}^{ins.}\Lambda(\bar{\omega}_{1},\bar{\omega}_{2}) \)  with (see Appendix A)

 \[ \begin{aligned}\Lambda(\bar{\omega}_{1},\bar{\omega}_{2})&=\left\{\frac{(\bar{\omega}_{1}+2\bar{\omega}_{2})}{\bar{\omega}_{2}^{2}(\bar{\omega}_{1}+\bar{\omega}_{2})}\ln\left[\frac{4-\bar{\omega}_{1}^{2}}{4-(\omega_{1}+\omega_{2})^{2}}\right]\right.\\&\left.+\frac{(\bar{\omega}_{2}+2\bar{\omega}_{1})}{\bar{\omega}_{1}^{2}(\bar{\omega}_{1}+\bar{\omega}_{2})}\ln\left[\frac{4-\bar{\omega}_{2}^{2}}{4-(\bar{\omega}_{1}+\bar{\omega}_{2})^{2}}\right]\right.\\&\left.-\frac{3}{2\bar{\omega}_{1}\bar{\omega}_{2}}\ln\left[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4}\right]\right\},\end{aligned} \quad (32) \] 

and the dimensionful constant prefactor reads

 \[ \Pi_{0}^{i n s.}=\frac{N_{f}e^{2}\mathcal{M}^{(2)}}{4\pi\mu^{2}}. \quad (33) \] 

in which  \( N_{f} = 4 \)  stands for the spin-valley degeneracy. The properties of universal function  \( \Lambda(\omega_{1}, \omega_{2}) \)  are explored in Ref. [46] at zero and finite electronic temperature  \( T_{e} \) .

## B. Light-induced retarded self-energy

For the retarded coupling, we have the Feynman diagrams depicted in Fig. 1(e-i), among which only diagrams shown in panels (e), (h), and (i) of Fig. 1 are non-zero in our effective model analysis. The symmetry of our low-energy model results in constraints for the non-vanishing elements of  \( \Pi_{abcd}^{ret} \) , as  \( \Pi_{xxxx}^{ret} = \Pi_{yyyy}^{ret} \) ,  \( \Pi_{xxyy}^{ret} = \Pi_{yyxx}^{ret} \) ,  \( \Pi_{xyxy}^{ret} = \Pi_{yxxy}^{ret} \) , and  \( \Pi_{xyxy}^{ret} = \Pi_{yxxy}^{ret} \) . Accordingly, the polarization dependence of the retarded coupling reads

 \[ \dot{\mathcal{G}}^{r e t.}(\Omega)=E_{0}^{2}\Pi_{I}^{r e t.}\dot{I}+E_{0}^{2}\begin{bmatrix}\Pi_{Z}^{r e t.}\cos(2\theta)&\Pi_{X}^{r e t.}sin(2\theta)\\ \Pi_{X}^{r E t.}sin(20)&\Pi_{Z}^{r e t.}\cos(20)\end{bmatrix}, \quad (34) \] 

where for a given light field frequency \(\omega\) and at phonon frequency \(\Omega\), we define

 \[ \begin{aligned}&\Pi_{I,Z}^{ret.}(\omega,-\omega,\Omega)=\frac{\Pi_{xxxx}^{ret.}\pm\Pi_{xyyy}^{ret.}}{2},\\&\Pi_{X}^{ret.}(\omega,-\omega,\Omega)=\frac{\Pi_{xyyx}^{ret.}+\Pi_{xyxy}^{ret.}}{2}.\\ \end{aligned} \quad (35) \] 

The + and - signs in the above relation refer to  \( \Pi_{I}^{ret} \)  and  \( \Pi_{Z}^{ret} \) , respectively. The three contributions from three diagrams Fig. 2a,d,e can be collected as follows

 \[ \begin{align*}\Pi_{\xi}^{ret.}=&I,Z,X(\omega_{1},\omega_{2},\omega_{3})=\Pi_{0}^{ret.}\Big\{\Pi_{\xi}^{\mathrm{square}}(\omega_{1},\omega_{2},\omega_{3})+\\ \alpha\Big[\Pi_{\xi}^{\mathrm{bubble}-\Theta}(\omega_{1},\omega_{2},\omega_{3})+\Pi_{\xi}^{\mathrm{bubble}-\Delta}(\omega_{1},\omega_{2},\omega_{3})\Big]\Big\}.\end{align*} \quad (36) \] 

In the low-energy model, we obtain vanishing contributions for the triangle diagrams shown in Fig. 1f,g. The detailed derivation and analytical expressions of the above nonlinear response functions at zero electronic temperature are given in Appendix B. Notice the constant factors

 \[ \Pi_{0}^{r e t.}=\frac{N_{f}(e\mathcal{M}^{(1)})^{2}}{24\pi(\hbar\Gamma_{e})\mu^{2}},\quad\alpha=\frac{\hbar\Gamma_{e}}{(18\gamma_{0}^{2}/\gamma_{1})}. \quad (37) \] 

Since  \( 18\gamma_{0}^{2}/\gamma_{1}\approx10^{2}eV \)  and  \( \hbar\Gamma_{e} \)  is usually less than tens of meV, we have  \( \alpha\ll1 \)  for realistic value of scattering rate  \( \hbar\Gamma_{e} \) . Therefore, we safely neglect the contribution of bubble diagrams relative to the square diagram. Considering the square diagram, our microscopic calculation gives  \( \Pi_{xxxx}^{ret.}=\Pi_{xxyy}^{ret.} \)  and  \( \Pi_{xyxy}^{ret.}=-\Pi_{xyyx}^{ret.} \) . Consequently, we obtain

 \[ \Pi_{I}^{r e t.}=\Pi_{x x x x}^{r e t.}\approx\Pi_{I}^{\mathrm{s q u a r e}}\quad\mathrm{a n d}\quad\Pi_{Z}^{r e t.}=\Pi_{X}^{r e t.}=0. \quad (38) \] 

In Fig. 2, we illustrate real and imaginary parts of  \( \Pi_{I}^{ret.} \)  at zero and finite electronic temperature  \( T_{e} \) . At
 
![](./images/867774263942185493_5.jpg)

![](./images/867774263942185493_6.jpg)

![](./images/867774263942185493_7.jpg)

FIG. 3. Adiabatic and non-adiabatic spectral functions of optically dressed shear phonons. Panels (a) and (b) illustrate the results obtained within the adiabatic and non-adiabatic models, respectively. In panel (c), we depict the spectral function obtained after neglecting the imaginary part of  \( \Pi_{f}^{ret}(\Omega) \) . The shear phonons' splitting is depicted at different values of the light field amplitude in the unit of V/nm. The splitting is almost the same in both adiabatic and non-adiabatic models. However, the linewidth and peak values are different in the two models. We set  \( \mu = 200meV \) ,  \( \hbar\Gamma_{e} = 5meV \) ,  \( \hbar\Gamma_{p} = 0.5meV \) ,  \( T_{e} = 100K \) ,  \( \hbar\Omega_{0} = 3.9meV \)  and  \( \theta = 0 \)  in this figure.

very low temperatures, the imaginary part is finite only in a narrow frequency window close to the interband optical transition gap  \( 2|\mu| \)  where the width of the frequency window is given by the shear phonon frequency  \( 2\Omega_{0} \) . The real part of  \( \Pi_{f}^{ret} \)  shows logarithmic cusps at optical transition edges for  \( \hbar\omega = 2\mu \)  and  \( \hbar\omega=2\mu\pm\hbar\Omega \) .

We generalize the zero temperature response function  \( \Pi_{abcd}(\varepsilon_{F}, T_{e}=0, \ldots) \)  to finite electronic temperature using the Maldague's formula [46, 56], by integrating over the Fermi energy as follows

 \[ \Pi_{abcd}\big|_{\mu,T_{e}}=\int_{-\infty}^{\infty}d y\frac{\Pi_{abcd}\big|_{\varepsilon_{F}\rightarrow y,T_{e}=0}}{4k_{B}T_{e}\cosh^{2}\left(\frac{y-\mu}{2k_{B}T_{e}}\right)}. \quad (39) \] 

The electronic temperature can reach thousands of Kelvin due to intense and ultrashort laser pulses  \( [57–61] \) . The imaginary part of  \( \Pi_{f}^{ret} \)  is always positive at zero and finite temperatures. We investigate the impact of the electronic temperature, and the result shows an expected reduction of the response for frequencies in the range  \( |\hbar\omega-2|\mu|\leq\hbar\Omega_{0} \)  while outside this range, the response function increases by raising the temperature.

## C. Light-induced phonon splitting and instability

Performing the Fourier transform of the shear phonon displacement vector  \( Q_{a}(t)=\sum_{\Omega}Q_{a}(\Omega)e^{-i\Omega t} \)  in Eq. (18) leads to the equation of motion into the frequency domain

 \[ \sum_{b}\left\{\mathcal{K}_{a b}(\Omega)-(\Omega^{2}+i\Gamma_{p}\Omega)\delta_{a b}\right\}Q_{b}(\Omega)=\frac{\mathcal{F}_{a}^{\mathrm{D}}}{\rho} \quad (40) \] 

where the dynamical matrix of shear modes is dressed by the external light field and given by

 \[ \mathcal{K}_{a b}(\Omega)=\Omega_{0}^{2}\delta_{a b}-\frac{\mathcal{G}_{a b}^{i n s.}}{\rho}-\frac{\mathcal{G}{}_{a b}^{r e t.}(\Omega)}{\rho}. \quad (41) \] 

We write the light-induced phonon self-energy term in a compact form in the unit of a characteristic frequency  \( \nu_{0}=\sqrt{g_{0}/\rho} \)  with  \( g_{0}=\gamma_{3}(eE_{0}/b\mu)^{2} \)  and thus the dynamical matrix reads

 \[ \hat{\mathcal{K}}(\Omega)=\Omega_{0}^{2}\hat{I}-\nu_{0}^{2}\begin{bmatrix}{{{K_{I}+K_{Z}\cos(2\theta)}}}&{{{K_{X}\sin(2\theta)}}} \\{{{K_{X}\operatorname*{s i n}(2\theta)}}}&{{{K_{I}-K_{Z}\cos(2\theta)}}}\end{bmatrix}. \quad (42) \] 

where for given driving field frequency  \( \omega \) , we have

 \[ \begin{aligned}&K_{I}(\Omega)=r_{1}\Pi_{1}^{square}(\omega,-\omega,\Omega),\\&K_{X}=-K_{Z}=r_{0}\Lambda(\omega,-\omega).\\ \end{aligned} \quad (43) \] 

Notice that  \( r_{0} = 3a_{0}^{2}\beta_{3}(1 + \beta_{3})/(4\pi b^{2}) \)  and  \( r_{1} = 3a_{0}^{2}\beta_{3}^{2}\gamma_{3}/(4\pi b^{2}\hbar\Gamma_{e}) \)  are dimensionless parameters. Considering numerical values of  \( \gamma_{3} \)  and  \( \beta_{3} \)  и lattice parameters, we obtain  \( r_{0} \approx 1.738 \)  and  \( r_{1} \approx 455/(\hbar\Gamma_{e}[\mathrm{meV}]) \) . Utilizing the dynamical matrix, we introduce the phonon Green's function dressed by the light field

 \[ \hat{D}(\Omega)=\left[(\Omega^{2}+i\Gamma_{p}\Omega)\hat{I}-\hat{\mathcal{K}}(\Omega)\right]^{-1}. \quad (44) \] 

Therefore, the spectral function of the shear mode is defined as  \( \mathcal{A}(\Omega) = -\mathrm{Im}[\mathrm{Tr}[\hat{D}(\Omega)]]/\pi \) . By defining  \( \nu_{0}^{2}\tilde{K}_{I}(\Omega) = \nu_{0}^{3}K_{I}(\Omega) + i\Gamma_{p}\Omega \)  and considering  \( K_{X} = -K_{Z} \) , we obtain a  \( \theta \) -independent spectral function

 \[ \mathcal{A}(\Omega)=\frac{2}{\pi}\mathrm{I m}\left[\frac{\Omega_{0}^{2}-\Omega^{2}-\nu_{0}^{2}\tilde{K}_{I}(\Omega)}{[\Omega_{0}^{2}-\Omega^{2}-\nu_{0}^{2}\tilde{K}_{I}(\Omega)]^{2}+\nu_{0}^{4}K_{Z}^{2}}\right]. \quad (45) \]
 
![](./images/867774263942185493_8.jpg)

![](./images/867774263942185493_9.jpg)

![](./images/867774263942185493_10.jpg)

![](./images/867774263942185493_11.jpg)

![](./images/867774263942185493_12.jpg)

![](./images/867774263942185493_13.jpg)

FIG. 4. Light-induced shear phonon splitting and instability. Panel (a) and (b) shows the mode splitting as a function of the light field amplitude at laser frequency  \( \hbar\omega = 3\mu \)  and two different values of electronic temperature. Panel (c) illustrates the frequency dependence of dynamically renormalized shear modes at field amplitude  \( E_{0} = 0.1V/nm \)  and  \( T_{e} = 300K \) . Panel (d) indicates the shear phonon frequencies versus the electronic temperature at  \( \hbar\omega = 2\mu \)  and  \( E_{0} = 0.1V/nm \) . Panel (e) shows the field dependence of shear phonon linewidth at  \( \hbar\omega = 3\mu \)  and  \( T_{e} = 300K \) . Panel (f) manifests the laser frequency dependence of the critical field amplitude at which phonon modes become unstable. We set  \( \mu = 200meV \) ,  \( \hbar\Gamma_{p} = 0.1meV \) ,  \( \hbar\Gamma_{e} = 5meV \)  and  \( \hbar\Omega_{0} = 3.9meV \)  in this figure.

For displacive Raman force analysis and rigid shear displacement, we only need to know the dynamical matrix at  \( \Omega=0 \) , which corresponds to the adiabatic component of the spectral function. In the adiabatic approximation [62], Green's function is obtained by setting the phonon frequency to zero in the dynamical matrix  \( \mathcal{K}(\Omega=0) \) :

 \[ \hat{D}^{\mathrm{a d}}(\Omega)=\left[(\Omega^{2}+i\Gamma_{p}\Omega)\hat{I}-\hat{\mathcal{K}}(\Omega=0)\right]^{-1}. \quad (46) \] 

We calculate the spectral function for both adiabatic and non-adiabatic models, and the results are depicted in Fig. 3a,b. Both models predict a splitting of degenerate shear modes due to the impact light field based on the nonlinear Raman mechanism. This comparison shows that the adiabatic approximation nicely predicts the same value for splitting phonon modes in the non-adiabatic formalism. However, the two methods differ for the linewidth and the spectral weight peak value. In particular, in Fig. 3c, we neglect the imaginary part of  \( \Pi_{I}^{ret}(\Omega) \) , which results in sharper peaks coinciding with the spectral peaks in the adiabatic model. According to this analysis, we can safely consider an adiabatic approximation by setting  \( \Omega = 0 \)  in the dynamical matrix  \( \hat{\mathcal{K}}(\Omega = 0) \)  to discuss the light-induced shear mode splitting and instability at which phonon frequency vanishes. In this case, we diagonalize the adiabatic dynamical matrix and obtain the normal shear phonon modes in a linear superposition of two Cartesian modes. Eventually, the normal mode frequencies read

 \[ \left(\frac{\Omega_{\pm}}{\Omega_{0}}\right)^{2}=1-\xi^{2}K_{I}(0)\pm\xi^{2}|K_{Z}|. \quad (47) \] 

Note that  \( \xi = \nu_{0}/\Omega_{0} \)  is a dimensionless parameter, and both  \( K_{I}(0) \)  and  \( K_{Z} \)  are real numbers. Since  \( K_{I}(\Omega) \)  is a complex number, its imaginary part induces a field-dependent renormalization of the phonon linewidth that follows

 \[ \frac{\Gamma_{\pm}}{\Gamma_{p}}=1+\frac{\nu_{0}^{2}}{\Gamma_{p}\Omega_{\pm}}\mathrm{I m}[K_{I}(\Omega_{\pm})]. \quad (48) \]
 

There are some qualitative features in the field-dependent phonon frequency and linewidth: (i) First, our perturbative analysis is primarily valid for small enough  \( \xi \) ; therefore, we have  \( \Omega_{\pm} > 0 \)  in the best validity range of our formalism. However, we can predict the case  \( \Omega_{\pm} = 0 \)  at critical field amplitudes  \( E_{\pm} \)  for which the shear mode becomes unstable that can facilitate an optically driven structural phase transition of the vdW material via the change in the staking order. (ii) For  \( K_{I}(0) = 0 \)  the splitting of two modes is symmetric and  \( \Omega_{+} \)  is always non-zero while  \( \Omega_{-} \)  vanishes at  \( \nu_{0} = \Omega_{0}/\sqrt{|K_{Z}|} \) . (iii) For  \( |K_{Z}| \ll |K_{I}(0)| \) , phonons remain degenerate at a larger or smaller frequency relative to  \( \Omega_{0} \)  for  \( K_{I}(0) < 0 \)  or  \( K_{I}'(0) > 0 \) , respectively. If  \( K_{I}(0) > 0 \) , phonon modes get softened ( \( \Omega_{\pm} \to 0 \) ) at a critical field amplitude leading to  \( \nu_{0} = \Omega_{0}/\sqrt{K_{I}(0)} \) . (iv) Since  \( \operatorname{Im}[K_{I}(\Omega_{\pm})] > 0 \)  as shown in Fig. 3c, we obtain a field-induced broadening of spectral function due to the optically enhanced electron-phonon scattering.

We illustrate the normal mode frequency in Fig. 4a,b as a function of the incident field intensity at two different electronic temperature values manifesting the quadratic dependence on the field amplitude. Fig. 4a shows that two normal modes conversely evolve where  \( \Omega_{+} \)  ( \( \Omega_{-} \) ) increases (decreases) by raising the field amplitude  \( E_{0} \) . The diverging evolution of two phonon modes' frequency in opposite directions becomes a converging trend with negative renormalization and phonon softening at higher electronic temperatures. This is because  \( K_{I}(0) \)  enhances by raising the temperature, and thus, it becomes larger than  \( K_{Z} \)  leading to a converging trend for both  \( \Omega_{\pm} \)  versus field amplitude  \( E_{0} \) . Intriguingly, at a critical value of  \( E_{0} \) , we predict a vanishing value for  \( \Omega_{\pm} = 0 \) , and by a further increase of  \( E_{0} \)  the phonon frequency becomes imaginary  \( \Omega_{\pm}^{2} < 0 \)  indicating a structural instability. As a result of this light-induced instability, atomic layers can easily slide to emerge in other stable or metastable staking orders.

In Fig. 4c, we show the frequency dependence of the normal modes' energies at room temperature showing the non-monotonic profile with a strong dependence on the light frequency. In the sub-gap regime, the phonon frequency drops to zero, then becomes unstable for a range of frequencies around interband transition edge  \( \hbar\omega = 2\mu \) . This is because the real part of  \( \Pi_{I}^{ret} \)  is enhanced around  \( \hbar\omega = 2\mu \)  as depicted in Fig. 2c. Further increasing the laser frequency makes  \( \Omega_{\pm}^{2} \)  positive and thus stable again. The phonon modes' splitting is stronger at higher laser frequency where  \( K_{I}(0) \)  becomes less relevant than  \( K_{Z} \) . Fig. 4d depicts the temperature dependence of the normal mode frequencies at the interband transition edge  \( \hbar\omega = 2|\mu| \)  and for a field amplitude  \( E_{0} = 0.1V/nm \) . The real part of  \( \Pi_{I}^{ret} \)  is larger at lower temperatures, making both shear modes unstable. By raising the electronic temperature, phonon modes become stable again, and by a further increase in temperature, the renormalization of phonon frequency starts to converge. In addition to the field-dependent phonon frequency, we obtain a robust enhancement of phonon linewidth shown in Fig. 4e, due to the photon-mediated amplification of electron-phonon scattering. Finally, we investigate the frequency dependence of critical electric fields  \( E_{\pm} \)  at which phonon modes  \( \Omega_{\pm} \)  become unstable. Fig. 4f shows that the critical fields  \( E_{\pm} \)  increase by raising the laser frequency.

Considering the nonlinear Raman force, one can further manipulate shear phonon renormalization and its impact on rigid shear displacement  \( \mathbf{Q}_{0} = \langle \mathbf{Q}(t) \rangle_{\mathrm{time-average}} \)  that reads

 \[ \mathbf{Q}_{0}=-\frac{1}{\rho}\hat{D}(\Omega=0)\cdot\mathcal{F}^{D}. \quad (49) \] 

where  \( F^{D} \)  is the displacive Raman shear force in bilayer graphene [46]. One can transform to the normal mode basis where the dynamical matrix is diagonal for which one finds the rigid shift  \( Q_{0}^{\pm} = F_{\pm}^{D} / \rho \Omega_{\pm}^{2} \)  for two normal shear phonon modes where  \( F_{\pm}^{D} \)  are the displacive Raman force components along the normal mode vibrational directions. For the case of  \( \theta = 0 \) , two normal modes  \( Q_{+} \) and  \( Q_{-} \) correspond to vibration along x and y direction, respectively. Therefore, the nonlinear Raman force mechanism modulates the light-induced rigid shear displacement via the optically driven renormalization of shear phonon frequency.

## V. CONCLUSION AND OUTLOOK

In conclusion, we present a complete quantum theory incorporating coherent dressing of electrons and phonons perturbatively. Unlike Floquet theory, the validity of our approach based on Green's function method is for a wide range of driving field frequencies. We apply the formal theory to the coherent optical engineering of shear phonons in bilayer graphene. We obtained strong renormalization of shear phonons' frequency that time-resolved spectroscopy of shear phonons can probe in pump-probe experiments [43, 45, 63–65]. In particular, we predict a light-induced non-thermal instability of shear vibration modes that can facilitate nondestructive coherent engineering lattice structure in layered materials. Our theory can be applied to other types of phonon modes in heterostructures of layered materials, which involve relative twists of layers. Having a coherent control of shear phonon dynamics provides an optical switching of polar metals, moiré ferroelectrics, and superconductivity in the heterostructures of layered quantum materials [66–74]. For intense incident laser, there is a saturation effect of the light-induced displacement usually observed in experimental measurements of coherent phonon displacement amplitude. This effect is due to the saturation of the optical absorption that can be explained via a saturable absorption process described by the third-order optical conductivity and a nonlinear force forth-order in the electric field amplitude, e.g.,  \( F \propto EE^{*}EE^{*} \) . The saturation effect analysis is beyond the scope of this manuscript and will be discussed elsewhere.
 

[1] K. Ishioka, M. Hase, M. Kitajima, L. Wirtz, A. Rubio, and H. Petek, Phys. Rev. B 77, 121402 (2008).

[2] Y. Murakami, P. Werner, N. Tsuji, and H. Aoki, Phys. Rev. B 91, 045128 (2015).

[3] P. C. Hohenberg and B. I. Halperin, Rev. Mod. Phys. 49, 435 (1977).

[4] P. E. Dolgirev, M. H. Michael, A. Zong, N. Gedik, and E. Demler, Phys. Rev. B 101, 174306 (2020).

[5] Z. Sun and A. J. Millis, Phys. Rev. X 10, 021028 (2020).

[6] T. Huber, S. O. Mariager, A. Ferrer, H. Schäfer, J. A. Johnson, S. Grübel, A. Lübcke, L. Huber, T. Kubacka, C. Dornes, C. Laulhe, S. Ravy, G. Ingold, P. Beaud, J. Demsar, and S. L. Johnson, Phys. Rev. Lett. 113, 026401 (2014).

[7] F. Giorgianni, T. Cea, C. Vicario, C. P. Hauri, W. K. Withanage, X. Xi, and L. Benfatto, Nature Physics 15, 341 (2019).

[8] A. de la Torre, D. M. Kennes, M. Claassen, S. Gerber, J. W. McIver, and M. A. Sentef, Rev. Mod. Phys. 93, 041002 (2021).

[9] C. Vaswani, L.-L. Wang, D. H. Mudiyanselage, Q. Li, P. M. Lozano, G. D. Gu, D. Cheng, B. Song, L. Luo, R. H. J. Kim, C. Huang, Z. Liu, M. Mootz, I. E. Perakis, Y. Yao, K. M. Ho, and J. Wang, Phys. Rev. X 10, 021013 (2020).

[10] T. Oka and H. Aoki, Phys. Rev. B 79, 081406 (2009).

[11] A. P. Itin and M. I. Katsnelson, Phys. Rev. Lett. 115, 075301 (2015).

[12] H. Aoki, N. Tsuji, M. Eckstein, M. Kollar, T. Oka, and P. Werner, Rev. Mod. Phys. 86, 779 (2014).

[13] M. Lejman, G. Vaudel, I. C. Infante, P. Gemeiner, V. E. Gusev, B. Dkhil, and P. Ruello, Nature Communications 5, 4301 (2014).

[14] T. F. Nova, A. S. Disa, M. Fechner, and A. Cavalleri, Science 364, 1075 (2019).

[15] J. G. Horstmann, H. Böckmann, B. Wit, F. Kurtz, G. Storeck, and C. Ropers, Nature 583, 232 (2020).

[16] A. S. Disa, T. F. Nova, and A. Cavalleri, Nature Physics 17, 1087 (2021).

[17] M. Henstridge, M. Först, E. Rowe, M. Fechner, and A. Cavalleri, Nature Physics 18, 457 (2022).

[18] P. H. Tan, W. P. Han, W. J. Zhao, Z. H. Wu, K. Chang, H. Wang, Y. F. Wang, N. Bonini, N. Marzari, N. Pugno, G. Savini, A. Lombardo, and A. C. Ferrari, Nature Materials 11, 294 (2012).

[19] A. C. Ferrari and D. M. Basko, Nature Nanotechnology 8, 235 (2013).

[20] X. Zhang, W. P. Han, J. B. Wu, S. Milana, Y. Lu, Q. Q. Li, A. C. Ferrari, and P. H. Tan, Phys. Rev. B 87, 115413 (2013).

## ACKNOWLEDGMENT

I acknowledge the support from the Swedish Research Council (VR Starting Grant No. 2018-04252). Nordita is partially supported by Nordforsk. I am grateful to E. Cappelluti and J. Hofmann for the valuable discussion and feedback.

[21] H. Zeng, B. Zhu, K. Liu, J. Fan, X. Cui, and Q. M. Zhang, Phys. Rev. B 86, 241301 (2012).

[22] K. H. Michel and B. Verberck, Phys. Rev. B 78, 085424 (2008).

[23] K. H. Michel and B. Verberck, Phys. Rev. B 85, 094303 (2012).

[24] Y. Zhao, X. Luo, H. Li, J. Zhang, P. T. Araujo, C. K. Gan, J. Wu, H. Zhang, S. Y. Quek, M. S. Dresselhaus, and Q. Xiong, Nano Letters 13, 1007 (2013).

[25] G. Wang, X. Li, Y. Wang, Z. Zheng, Z. Dai, X. Qi, L. Liu, Z. Cheng, Z. Xu, P. Tan, and Z. Zhang, The Journal of Physical Chemistry C 121, 26034 (2017).

[26] G. Pizzi, S. Milana, A. C. Ferrari, N. Marzari, and M. Gibertini, ACS Nano 15, 12509 (2021).

[27] M. Y. Zhang, Z. X. Wang, Y. N. Li, L. Y. Shi, D. Wu, T. Lin, S. J. Zhang, Y. Q. Liu, Q. M. Liu, J. Wang, T. Dong, and N. L. Wang, Phys. Rev. X 9, 021036 (2019).

[28] S. Ji, O. Gränäs, and J. Weissenrieder, ACS Nano 15, 8826 (2021).

[29] E. J. Sie, C. M. Nyby, C. D. Pemmaraju, S. J. Park, X. Shen, J. Yang, M. C. Hoffmann, B. K. Ofori-Okai, R. Li, A. H. Reid, S. Weathersby, E. Mannebach, N. Finney, D. Rhodes, D. Chenet, A. Antony, L. Balicas, J. Hone, T. P. Devereaux, T. F. Heinz, X. Wang, and A. M. Lindenberg, Nature 565, 61 (2019).

[30] M. Born, K. Huang, and M. Lax, American Journal of Physics 23, 474 (1955).

[31] G. Lanzani, G. Cerullo, and S. De Silvestri, Coherent Vibrational Dynamics (CRC Press, 2007).

[32] T. Dekorsy, G. C. Cho, and H. Kurz, “Coherent phonons in condensed media,” in Light Scattering in Solids VIII: Fullerenes, Semiconductor Surfaces, Coherent Phonons, edited by M. Cardona and G. Güntherodt (Springer Berlin Heidelberg, Berlin, Heidelberg, 2000) pp. 169–209.

[33] M. Hase, M. Kitajima, A. M. Constantinescu, and H. Petek, Nature 426, 51 (2003).

[34] K. Ishioka, M. Hase, M. Kitajima, and H. Petek, Applied Physics Letters 89, 231916 (2006).

[35] H. J. Zeiger, J. Vidal, T. K. Cheng, E. P. Ippen, G. Dresselhaus, and M. S. Dresselhaus, Phys. Rev. B 45, 768 (1992).

[36] T. Pfeifer, T. Dekorsy, W. Kütt, and H. Kurz, Applied Physics A 55, 482 (1992).

[37] A. V. Kuznetsov and C. J. Stanton, Phys. Rev. Lett. 73, 3243 (1994).

[38] A. V. Kuznetsov and C. J. Stanton, Phys. Rev. B 51, 7555 (1995).

[39] T. E. Stevens, J. Kuhl, and R. Merlin, Phys. Rev. B 65, 144304 (2002).
 

[40] G. A. Garrett, T. F. Albrecht, J. F. Whitaker, and R. Merlin, Phys. Rev. Lett. 77, 3661 (1996).

[41] R. Merlin, Solid State Communications 102, 207 (1997).

[42] J. Zhang, J. Han, G. Peng, X. Yang, X. Yuan, Y. Li, J. Chen, W. Xu, K. Liu, Z. Zhu, W. Cao, Z. Han, J. Dai, M. Zhu, S. Qin, and K. S. Novoselov, Light: Science & Applications 9, 174 (2020).

[43] D. Soranzio, M. Peressi, R. J. Cava, F. Parmigiani, and F. Cilento, Phys. Rev. Research 1, 032033 (2019).

[44] T. Fukuda, K. Makino, Y. Saito, P. Fons, A. V. Kolobov, K. Ueno, and M. Hase, Applied Physics Letters 116, 093103 (2020).

[45] P. Hein, S. Jauernik, H. Erk, L. Yang, Y. Qi, Y. Sun, C. Felser, and M. Bauer, Nature Communications 11, 2613 (2020).

[46] H. Rostami, Phys. Rev. B 106, 155405 (2022).

[47] M. S. Dresselhaus, G. Dresselhaus, and A. Jorio, Group theory: application to the physics of condensed matter (Springer Science & Business Media, 2007).

[48] G. D. Mahan, Many-particle physics (Springer US, 1995).

[49] T. P. Devereaux and R. Hackl, Rev. Mod. Phys. 79, 175 (2007).

[50] E. McCann and V. I. Fal'ko, Phys. Rev. Lett. 96, 086805 (2006).

[51] H. Rostami and R. Asgari, Phys. Rev. B 88, 035404 (2013).

[52] E. McCann and M. Koshino, Reports on Progress in Physics 76, 056503 (2013).

[53] K. Ishikawa and T. Ando, Journal of the Physical Society of Japan 75, 084713 (2006).

[54] E. Cappelluti and G. Profeta, Phys. Rev. B 85, 205436 (2012).

[55] D. M. Basko, New Journal of Physics 11, 095011 (2009).

[56] G. Giuliani and G. Vignale, Quantum theory of the electron liquid (Cambridge university press, 2005).

[57] C. H. Lui, K. F. Mak, J. Shan, and T. F. Heinz, Phys. Rev. Lett. 105, 127404 (2010).

[58] A. Tomadin, D. Brida, G. Cerullo, A. C. Ferrari, and M. Polini, Phys. Rev. B 88, 035430 (2013).

[59] D. Brida, A. Tomadin, C. Manzoni, Y. J. Kim, A. Lombardo, S. Milana, R. R. Nair, K. S. Novoselov, A. C. Ferrari, G. Cerullo, and M. Polini, Nature Communications 4, 1987 (2013).

[60] A. Tomadin, S. M. Hornett, H. I. Wang, E. M. Alexeev, A. Candini, C. Coletti, D. Turchinovich, M. Kläi, M. Bonn, F. H. L. Koppens, E. Hendry, M. Polini, and

K.-J. Tielrooij, Science Advances 4, eaar5313 (2018), https://www.science.org/doi/pdf/10.1126/sciadv.aar5313.

[61] F. Andreatta, H. Rostami, A. G. Cabo, M. Bianchi, C. E. Sanders, D. Biswas, C. Cacho, A. J. H. Jones, R. T. Chapman, E. Springate, P. D. C. King, J. A. Miwa, A. Balatsky, S. Ulstrup, and P. Hofmann, Phys. Rev. B 99, 165421 (2019).

[62] F. Giustino, Rev. Mod. Phys. 89, 015003 (2017).

[63] S. Ulstrup, J. C. Johannsen, F. Cilento, J. A. Miwa, A. Crepaldi, M. Zacchigna, C. Cacho, R. Chapman, E. Springate, S. Mammadov, F. Fromm, C. Raidel, T. Seyller, F. Parmigiani, M. Grioni, P. D. C. King, and P. Hofmann, Phys. Rev. Lett. 112, 257401 (2014).

[64] L. Luo, D. Cheng, B. Song, L.-L. Wang, C. Vaswani, P. M. Lozano, G. Gu, C. Huang, R. H. J. Kim, Z. Liu, J.-M. Park, Y. Yao, K. Ho, I. E. Perakis, Q. Li, and J. Wang, Nature Materials 20, 329 (2021).

[65] F. Giorgianni, M. Udina, T. Cea, E. Paris, M. Caputo, M. Radovic, L. Boie, J. Sakai, C. W. Schneider, and S. L. Johnson, Communications Physics 5, 103 (2022).

[66] Z. Zheng, Q. Ma, Z. Bi, S. de la Barrera, M.-H. Liu, N. Mao, Y. Zhang, N. Kiper, K. Watanabe, T. Taniguchi, J. Kong, W. A. Tisdale, R. Ashoori, N. Gedik, L. Fu, S.-Y. Xu, and P. Jarillo-Herrero, Nature 588, 71 (2020).

[67] C. R. Woods, P. Ares, H. Nevison-Andrews, M. J. Holwill, R. Fabregas, F. Guinea, A. K. Geim, K. S. Novoselov, N. R. Walet, and L. Fumagalli, Nature Communications 12, 347 (2021).

[68] Y. Kenji, W. Xirui, W. Kenji, T. Takashi, and J.-H. Pablo, Science 372, 1458 (2021).

[69] V. S. M., W. Y., C. W., N. I., W. K., T. T., S. E., U. M., H. O., and B. S. M., Science 372, 1462 (2021).

[70] Z. Fei, W. Zhao, T. A. Palomaki, B. Sun, M. K. Miller, Z. Zhao, J. Yan, X. Xu, and D. H. Cobden, Nature 560, 336 (2018).

[71] S. Pankaj, X. Fei-Xiang, S. Ding-Fu, Z. Dawei, T. E. Y., H. A. R., and S. Jan, Science Advances 5, eaax5080.

[72] W. X. Zhou and A. Ariando, Japanese Journal of Applied Physics 59, SI0802 (2020).

[73] W. Qin and A. H. MacDonald, Phys. Rev. Lett. 127, 097001 (2021).

[74] J. Liang, D. Yang, J. Wu, J. I. Dadap, K. Watanabe, T. Taniguchi, and Z. Ye, Phys. Rev. X 12, 041005 (2022).

[75] H. Rostami, M. I. Katsnelson, G. Vignale, and M. Polini, Annals of Physics 431, 168523 (2021).
 

## Appendix A: Instantaneous susceptibility

Considering the contribution of  \( \Delta_{abcd}^{(2)} \) , the instantaneous coupling consists of three contributions

 \[ \bar{\chi}_{a b c d}^{i n s.}(\omega_{1},\omega_{2})=\bar{\chi}_{a b c d}^{t r i a n g l e}(\omega_{1},\omega_{2})+\bar{\chi}_{a b c d}^{b u b b l e-\gamma}(\omega_{1},\omega_{2})+\bar{\chi}_{a b c d}^{b u b b l e-\Theta}(\omega_{1},\omega_{2}) \quad (A1) \] 

In the following subsections, we calculate the values of each diagram for the instantaneous susceptibility.

## 1. Calculation of  \( \bar{\chi}_{abcd}^{triangle} \)  for the diagram depicted in Fig. 1a

The triangle diagram Fig. 1a can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and two-phonon-electron matrix-element  \( \hat{\mathcal{M}}_{ab}^{(2)} \)  and paramagnetic current operator  \( \hat{j}_{c}, \hat{j}_{d} \) :

 \[ \chi_{abcd}(i\omega_{m_{1}},i\omega_{m_{2}})=\sum_{\mathcal{P}}\frac{1}{\mathcal{S}}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{i k_{n}}\mathrm{T r}\left[\mathcal{M}_{a b}^{(2)}(\mathbf{k})\hat{G}(\mathbf{k},i k_{n})\hat{j}_{c}(\mathbf{k})\hat{G}(\mathbf{k},i k_{n}+i\omega_{m_{1}})\hat{j}_{d}(\mathbf{k})\hat{G}(\mathbf{k},i k_{n}+i\omega_{m_{1}}+i\omega_{m_{2}})\right] \quad (A2) \] 

where the trace operator  \( \operatorname{Tr}[\ldots] \)  sum over all spinor degree of freedom,  \( \beta = 1/k_{\mathrm{B}}T_{e} \) ,  \( i k_{n} \)  ( \( i\omega_{m} \) ) stands for the fermionic (bosonic) Matsubara frequency. The intrinsic permutation symmetry is enforced by  \( \sum_{D} \)  for the exchange of photon frequencies and corresponding tensorial index:  \( (c, m_{1}) \leftrightarrow (d, m_{2}) \) . From now on, we adopt a short-hand notation  \( i k_{n} \rightarrow n \)  and  \( i\omega_{m} \rightarrow m \)  for the sake of simplicity. The electronic Green's function is given as follows

 \[ \hat{G}(\mathbf{k},i k_{n})=[i k_{n}-\hat{H}_{\mathbf{k}}]^{-1}. \quad (A3) \] 

Because of the inversion symmetry, the response tensor elements with odd Cartesian index x and y vanishes  \( \chi_{xxxy} = \chi_{xxyx} = \chi_{yyxy} = \chi_{\gamma yyx} = \chi_{\alpha yxx} = \chi_{xyyy} = \chi_{yxx} = \chi_{\gamma yxy} = 0 \) . This symmetry consideration is confirmed by an explicit calculation based on the low-energy two-band model. The remaining tensor elements are also related to each other due to the rotation symmetry of the system:

 \[ -\chi_{xxxx}=-\chi_{yyyy}=\chi_{xxyy}=\chi_{yyxx}=\chi_{xyyx}=\chi_{xyxy}=\chi_{yxxy}=\chi_{1}. \quad (A4) \] 

After performing the integration on the azimuthal angle of electronic wave vector k and using the low-energy dispersion  \( \epsilon_{k}=\hbar^{2}k^{2}/2m \)  and kdk= \( (m/\hbar^{2})d\epsilon \)  we find

 \[ \begin{align*}\chi_{1}(m_{1},m_{2})=\left(\frac{N_{f}\mathcal{M}^{(2)}}{2\pi}\right)\left(\frac{e}{m}\right)^{2}\left(\frac{m}{\hbar^{2}}\right)\int_{0}^{\infty}d\epsilon\frac{1}{\beta}\sum_{n}\\ \frac{8\epsilon^{2}\xi(n)(2\epsilon^{2}-\xi(m_{1}+n)^{2}-\xi(m_{2}+n)^{2})\xi(m_{1}+m_{2}+n)}{(\epsilon^{2}-\xi(n)^{2})(\epsilon^{2}-\xi(m_{1}+n)^{2})(\epsilon^2-\xi(m_{2}+n)^{2})( \epsilon^2-\xi( m_{1}+m_{2}+n)^{2})}.\end{align*} \quad (A5) \] 

where  \( \xi(n)=\mu+n \) . After performing Matsubara summation, integrating over  \( \epsilon \)  at zero temperature and analytical continuation  \( m_{i}\rightarrow\omega_{i}+i0^{+} \) , we find

 \[ \chi_{1}(\omega_{1},\omega_{2})=\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{4\pi\hbar^{2}}\Biggl\{A_{1}\ln[4\epsilon^{2}-\omega_{1}^{2}]+A_{2}\ln[4\epsilon^{2}-\omega_{2}^{2}]+A_{3}\ln[4\epsilon^{2}-(\omega_{1}+\omega_{2})^{2}]\Biggr\}_{\epsilon\rightarrow\mu}^{\epsilon\rightarrow\infty}. \quad (A6) \] 

Here by  \( \omega_{i} \)  we mean  \( \hbar\omega_{i}+i0^{+} \)  and  \( A_{i} \)  factors read

 \[ A_{1}=\frac{\omega_{1}(\omega_{1}+2\omega_{2})}{\omega_{2}(\omega_{1}+\omega_{2})},\quad A_{2}=\frac{\omega_{2}(\omega_{2}+2\omega_{1})}{\omega_{1}(\omega_{1}+\omega_{2})},\quad A_{3}=-1-(A_{1}+A_{2}). \quad (A7) \] 

By subtracting the zero-frequency contribution and after some simplifications, we find

 \[ \chi_{1}(\omega_{1},\omega_{2})-\chi_{1}(0,0)=\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{4\pi\hbar^{2}}\Biggl\{A_{1}\ln\left[\frac{4\epsilon^{2}-\omega_{1}^{2}}{4\epsilon^{2}-(\omega_{1}+\omega_{2})^{2}}\right]+A_{2}\ln\left[\frac{4\epsilon^{2}-\omega_{2}^{2}}{4\epsilon^{2}-(\omega_{1}+\omega_{2})^{2}}\right]-\ln\left[\frac{4\epsilon^{2}-(\omega_{1}+\omega_{2})^{2}}{4\epsilon^{2}}\right]\Biggr\}_{\epsilon\rightarrow\mu}^{\epsilon\rightarrow\infty}. \quad (A8) \] 

Eventually, we obtain  \( \chi_{1}^{\mathrm{triangle}}(\omega_{1},\omega_{2})=\chi_{1}(\omega_{1},\omega_2)-\chi_{1}(0,0) \)  as follows

 \[ \bar{\chi}_{1}^{\mathrm{t r i a n g l e}}(\omega_{1},\omega_{2})=\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{4\pi\hbar^{2}}\Biggl\{\ln\left[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\right]-A_{1}\ln\left[\frac{4\mu^{2}-\omega_{1}^{2}}{4\mu^{2}-(\omega_{1}+\omega_{2})^{2}}\right]-A_{2}\ln\left[\frac{4\mu^{2}-\omega_{2}^{2}}{4\mu^{2}-(\omega_{1}+\omega_{2})^{2}}\right]\Biggr\}. \quad (A9) \]
 

## 2. Calculation of  \( \bar{\chi}_{abcd}^{bubble-\gamma} \)  for the diagram depicted in Fig. 1b

The bubble diagram Fig. 1b can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, n) \) , electron-phonon matrix-element  \( \hat{\mathcal{M}}_{ab}^{(2)} \)  and the Raman vertex  \( \hat{\gamma}_{cd} \) :

 \[ \chi_{a b c d}(m_{1},m_{2})=-\frac{1}{S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{T r}\left[\mathcal{M}_{a b}^{(2)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\gamma}_{c d}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1}+m_{2})\right] \quad (A10) \] 

The overall minus sign originates from the standard rules of Feynman diagrams  \( [48] \) , also see  \( [75] \) . Similar to the previous diagram, we have  \( \chi_{xxxy} = \chi_{xxyx} = \chi_{yyxy} = \chi_{\gamma yyx} = \chi_{\chi yxx} = \chi_{xyyy} = \chi_{yxxx} = \chi_{yyxy} = 0 \) . The other non-vanishing tensor elements read

 \[ -\chi_{xxxx}=-\chi_{yyyy}=\chi_{xxyy}=\chi_{yyxx}=\chi_{xyyx}=\chi_{xyxy}=\chi_{yxxy}=\chi_{yxxy}=\chi_{2}. \quad (A11) \] 

After performing the integration on the azimuthal angle of electronic wave vector k and using the low-energy dispersion  \( \epsilon_{k}=\hbar^{2}k^{2}/2m \)  and  \( kdk=(m/\hbar^{2})d\epsilon \)  we find

 \[ \chi_{2}(m_{1},m_{2})=N_{f}\frac{m}{\hbar^{2}}\frac{e^{2}\mathcal{M}^{(2)}}{2\pi m}\int_{0}^{\infty}d\epsilon\frac{1}{\beta}\sum_{n}\frac{2\xi(n)\xi(m_{1}+m_{2}+n)}{(\epsilon^{2}-\xi(n)^{2})(\epsilon^{2}-\xi(m_{1}+m_{2}+n)^{2})}. \quad (A12) \] 

After performing the summation on the Matsubara frequency n and subtracting the zero-frequency contribution, we find

 \[ \chi_{2}(\omega_{1},\omega_{2})-\chi_{2}(0,0)=-\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{8\pi\hbar^{2}}\left\{\ln[\frac{4\epsilon^{2}-(\omega_{1}+\omega_{2})^{2}}{4\epsilon^{2}}]\right\}_{\epsilon\rightarrow\mu}^{\epsilon\rightarrow\infty}. \quad (A13) \] 

Finally, we obtain

 \[ \bar{\chi}_{2}^{bubble-\gamma}(\omega_{1},\omega_{2})=\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{8\pi\hbar^{2}}\ln\left[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\right]. \quad (A14) \] 

## 3. Calculation of  \( \bar{\chi}_{abcd}^{bubble-\Theta} \)  for the diagram depicted in Fig. 1c

The bubble diagram Fig. 1c can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, n) \) , 1-photon-electron-phonon vertex  \( \hat{\Theta}_{abc}^{(2)} \)  and the paramagnetic current  \( \hat{j}_{d} \) . Considering the permutation symmetry, we have

 \[ \begin{align*}\chi_{abcd}(m_{1},m_{2})=&-\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{abc}^{(2)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{j}_{d}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{2})\right]\\&-\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{abd}^{(2)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{j}_{c}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1})\right].\end{align*} \quad (A15) \] 

Using the isotropic approximation for the PEP vertex given in Eq. (6) and after performing the integration on the azimuthal angle of electronic wave vector k, we obtain a vanishing result for all tensor elements. Therefore, within our low-energy model analysis, the mix of photon-electron-phonon coupling does not contribute to the Raman force:

 \[ \bar{\chi}_{abcd}^{bubble-\Theta}(\omega_{1},\omega_{2})=0. \quad (A16) \] 

## 4. The sum of all diagrams for the instantaneous coupling

Similar to the Raman force case, we obtain  \( \bar{\chi}^{ins.}(\omega_{1},\omega_{2})=\bar{\chi}_{1}(\omega_{1},\ω_{2})+\bar{\chi}_{2}(\ω_{1},\ω_{1}) \) . One main difference is that instead of  \( \mathcal{M}^{(1)} \)  we have  \( \mathcal{M}(2) \) :

 \[ \begin{align*}\bar{\chi}_{xxxx}^{ins.}(\omega_{1},\omega_{2})&=\frac{N_{f}\mathcal{M}^{(2)}e^{2}}{4\pi\hbar^{2}}\left\{\frac{3}{2}\ln\left[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\right]-\frac{\omega_{1}(\omega_{1}+2\omega_{2})}{\omega_{2}(\omega_{1}+\omega_{2})}\ln\left[\frac{4\mu^{2}-\omega_{1}^{2}}{4\mu^{2}-(\omega_{1}+\omega_{2})^{2}}\right]\right.\\&\left.-\frac{\omega_{2}(\omega_{2}+2\omega_{1})}{\omega_{1}(\omega_{1}+\omega_{2})}\ln\left[\frac{4\mu^{2}-\omega_{2}^{2}}{4\mu^{2}-(\omega_{1}+\omega_{2})^{2}}\right]\right\}.\end{align*} \quad (A17) \]
 

Finally, by considering a linear polarized incident electric field  \( \mathbf{E}(t)=E_{0}(\hat{\mathbf{x}}\cos\theta+\hat{\mathbf{y}}\sin\theta)e^{-i\omega t}+c.c \) , we find

 \[ \hat{\mathcal{G}}^{i n s.}(\omega_{1},\omega_{2})=\Pi_{x x x}^{i n s.}(\omega_{1},\omega_{2})E_{0}^{2}\begin{bmatrix}-\cos(2\theta)&\sin(2\theta)\\ \sin(2\theta)&\cos(2\theta)\end{bmatrix}. \quad (A18) \] 

The rectified part of  \( \hat{G}^{ins.} \)  is obtained after setting  \( \omega_{1}=\hbar(\omega+i0^{+}) \)  and  \( \omega_{2}=\hbar(-\omega+i0^{+}) \)  where  \( \omega \)  is the incident laser frequency and  \( \Gamma_{e} \)  stands for the effective scattering rate of electrons.

## Appendix B: Retarded susceptibility

The retarded coupling is given in terms of five different diagram

 \[ \begin{aligned}\bar{\chi}_{a b c d}^{r e t.}(\omega_{1},\omega_{2},\omega_{3})&=\bar{\chi}_{a b c d}^{s q u a r e}(\omega_{1},\omega_{2},\omega_{3})+\bar{\chi}_{a b c d}^{t r i a n g l e-\gamma}(\omega_{1},\omega_{2},\omega_{3})+\bar{\chi}_{a b c d}^{t r i a n g l e-\Theta}(\omega_{1},\omega_{2},\omega_{3})\\&\quad+\bar{\chi}_{a b c d}^{b u b b l e-\Theta}(\omega_{1},\omega_{2},\omega_{3})+\bar{\chi}_{a b c d}^{b u b b l e-\Delta}(\omega_{1},\omega_{2},\omega_{3}).\end{aligned} \quad (B1) \] 

In the following, we calculate the explicit expression of each contribution using standard Kubo's formalism at zero electronic temperature.

## 1. Calculation of  \( \bar{\chi}_{abcd}^{square} \)  for the diagram depicted in Fig. 1e

The square diagram Fig. 1e can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and two-phonon-electron matrix-element  \( \hat{\mathcal{M}}_{a}^{(1)} \) ,  \( \hat{\mathbf{\mathcal{M}}}_{b}^{(1)} \)  and paramagnetic current operators  \( \hat{j}_{c} \) ,  \( \hat{j_{d}} \) :

 \[ \begin{align*}\chi_{abcd}(m_{1},m_{2},m_{3})&=\frac{1}{3!}\sum_{\mathcal{P}}\frac{1}{S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\mathcal{M}}_{a}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\mathcal{M}}_{b}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{3})\hat{j}_{c}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{3}+m_{1})\right.\\&\left.\hat{j}_{d}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{3}+m_{1}+m_{2})\right].\end{align*} \quad (B2) \] 

Note that  \( \sum_{P} \)  stands to ensure the intrinsic permutation symmetry. Because of the inversion symmetry, the response tensor elements with odd Cartesian index x and y vanishes  \( \chi_{xxxx} = \chi_{xxyx} = \chi_{yyxy} = \chi_{yyyy} = \chi_{xyxx} = \chi_{xxyy} = \chi_{yxxy} = \chi_{xyyy} = 0 \) . Accordingly, there are only four independent tensor elements

 \[ \chi_{xxxx}=\chi_{yyyy},\chi_{xxyy}=\chi_{yyxx},\chi_{xyxy}=\chi_{xyyx},\chi_{xyyx}=\chi_{yxxy}. \quad (B3) \] 

By performing a straightforward algebra similar to what was discussed in the previous subsection, one can obtain the four non-vanishing tensor elements in the following form:

 \[ \begin{aligned}&\chi_{xxxx}(\omega_{1},\omega_{2},\omega_{3})=\chi_{xxyy}(\omega_{1},\omega_{2},\omega_{3})=\frac{N_{f}}{24\pi}\left(\frac{e\mathcal{M}^{(1)}}{h}\right)^{2}\times\\ &-\left[\frac{4\omega_{1}\omega_{2}\left(\omega_{1}^{2}+(\omega_{2}+\omega_{3})\omega_{1}+\omega_{3}\left(\omega_{2}+\omega_{3}\right)\right)}{\left(\omega_{1}+\omega_{2}\right)\omega_{3}\left(\omega_{1}+\omega_{3}\right)\left(\omega_{2}+\omega_{3}\left)\right)\left(\omega_{\mathrm{l}}+\omega_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{1}}{2|\mu|+\omega_{1}}\right]\right.\\ &\left.-\frac{4\omega_{1}\omega_{2}\left(\omega_{2}^{2}+\omega_{3}\omega_{2}+\omega_{3}^{2}+\omega_{1}\left(\omega_{2}+\omega_{3}\right)\right)}{\left(\omega_{1}+\omega_{2}\right)\omega_{3}\left(\omega_{1}+\omega_{3}\right)\left(\omega_{2}+\omega_{3}\left)\right)\left(\omega_{\mathrm{l}}+\omega_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{2}}{2|\mu|+\omega_{2}}\right]\right.\\ &\left.+\frac{4\omega_{3}\left(\left(\omega_{2}+\omega_{3}\right)\omega_{1}^{2}+\left(\omega_{2}^{2}+3\omega_{3}\omega_{2}+\omega_{3}^{2}\right)\omega_{1}+\omega_{2}\omega_{3}\left(\omega_{2}+\omega_{3}\right)\right)}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}\right)\left(\omega_{1}+w_{3}\right)\left(\nu_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{3}}{2|\mu|+\omega_{3}}\right]\right.\\ &\left.-\frac{4\left(\omega_{1}+\omega_{3}\right)\left(\omega_{1}\left(\omega_{3}-\omega_{2}\right)+\omega_{3}\left(\omega_{2}+\omega_{3}\right)\right)}{\omega_{1}\omega_{2}\omega_{3}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{1}-\omega_{3}}{2|\mu|+\omega_{1}+\omega_{3}}\right]\right.\\ &\left.-\frac{4\left(\omega_{2}+\omega_{3}\right)\left(\omega_{1}\left(\omega_{3}-\omega_{2}\right)+\omega_{3}\left(\omega_{2}+\omega_{3}\right)\right)}{\omega_{1}\omega_{2}\omega_{3}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{2}-\omega_{3}}{2|\mu|+\omega_{2}+\omega_{3}}\right]\right.\\ &\left.+\frac{4\omega_{3}\left(\omega_{1}^{3}+2\left(\omega_{2}+\omega_{3}\right)\omega_{1}^{2}+\left(2\omega_{2}^{2}+3\omega_{3}\omega_{2}+\omega_{3}^{2}\right)\omega_{1}+\omega_{2}\left(\omega_{2}+\omega_{3}\right)^{2}\right)}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}\right)\left(\omega_{1}+w_{3}\right)\left(\nu_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{1}-\omega_{2}-\omega_{3}}{2|\mu|+\omega_{1}+\omega_{2}+\omega_{3}}\right]\right\},\end{aligned} \quad (B4) \]
 

and

 \[ \begin{aligned}&\chi_{xyxy}(\omega_{1},\omega_{2},\omega_{3})=-\chi_{xyyx}(\omega_{1},\omega_{2},\omega_{3})=\frac{N_{f}}{24\pi}\left(\frac{e\mathcal{M}^{(1)}}{\hbar}\right)^{2}\left\{\frac{4\omega_{1}}{{\omega_{2}}\left(\omega_{1}+\omega_{2}+2\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{1}}{2|\mu|+\omega_{1}}\right]\right.\\ &-\frac{4\omega_{2}\left(\omega_{1}+\omega_{2}+2\omega_{3}\right)}{\omega_{1}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\omega_{3}}\ln\left[\frac{2|\mu|-\omega_{2}}{2|\mu|+\omega_{2}}\right]+\frac{4\left(\omega_{1}-\omega_{2}\right)\omega_{3}}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}\ln\left[\frac{2|\mu|-\omega_{3}}{2|\mu|+\omega_{3}}\right]\\ &-\frac{4\left(\omega_{1}^{2}-\omega_{2}^{2}\right)\left(\omega_{1}+\omega_{2}+2\omega_{3}\right)}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\omega_{3}}\ln\left[\frac{2|\mu|-\omega_{1}-\omega_{2}}{2|\mu|+\omega_{1}+\omega_{2}}\right]\\ &-\frac{4\left(\omega_{1}+\omega_{3}\right)\left(\omega_{1}^{2}+\left(\omega_{2}+\omega_{3}\right)\omega_{1}-\omega_{2}\omega_{3}\right)}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\omega_{3}}\ln\left[\frac{2|\mu|-\omega_{1}-\omega_{3}}{2|\mu|+\omega_{1}+\omega_{3}}\right]\\ &+\frac{4\left(\omega_{2}+\omega_{3}\right)\left(\omega_{1}\left(\omega_{2}-\omega_{3}\right)+\omega_{2}\left(\omega_{2}+\omega_{3}\right)\right)}{\omega_{1}\omega_{2}\left(\omega_{1}+\omega_{2}+\omega_{3}\right)\omega_{3}}\ln\left[\frac{2|\mu|-\omega_{2}-\omega_{3}}{2|\mu|+\omega_{2}+\omega_{3}}\right]\\ &+\frac{4\left(\omega_{1}-\omega_{2}\right)\left(\omega_{1}+\omega_{2}+\omega_{3}\right)}{\omega_{1}\omega_{2}\omega_{3}}\ln\left[\frac{2|\mu|-\omega_{1}-\omega_{2}-\omega_{3}}{2|\mu|+\omega_{1}+\omega_{2}+\omega_{3}}\right]\Bigg\}.\\ \end{aligned} \quad (B5) \] 

For the short hand notation we adapt  \( \omega_{i} \)  for  \( \hbar(\omega_{i}+i0^{+}) \)  in the above relations.

## 2. Calculation of  \( \tilde{\chi}_{abcd}^{triangle-\gamma} \)  for the diagram depicted in Fig. 1f

The triangle diagram Fig. 1f can be written in terms of electronic Green’s function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and electron-phonon matrix-element  \( \hat{\mathcal{M}}_{a}^{(1)} \) ,  \( \hat{\mathbf{\mathcal{M}}}_{b}^{(1)} \)  and diamagnetic current operator  \( \hat{\gamma}_{cd} \) :

 \[ \chi_{a b c d}(m_{1},m_{2},m_{3})=-\sum_{\mathcal{P}}\frac{1}{\mathcal{S}}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{T r}\left[\hat{\mathcal{M}}_{a}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\mathcal{M}}_{b}^{(1)}\hat{G}(\mathbf{k},n+m_{1})\hat{\gamma}_{c d}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1}+m_{2}+m_{3})\right] \quad (B6) \] 

Using the isotropic approximation model Hamiltonian and after performing the integration on the azimuthal angle of electronic wave vector k, we obtain a vanishing result for all tensor elements. Therefore, within our low-energy model analysis, we have

 \[ \chi_{a b c d}^{t r i a n g l e-\gamma}(\omega_{1},\omega_{2},\omega_{3})=0. \quad (B7) \] 

## 3. Calculation of  \( \tilde{\chi}_{abcd}^{triangle-\Theta} \)  for the diagram depicted in Fig. 1g

The triangle diagram Fig. 1g can be written in terms of electronic Green’s function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and photon-electron-phonon matrix-element  \( \hat{\Theta}_{ac}^{(1)} \) , electron-phonon matrix-element  \( \hat{\mathcal{M}}_{b}^{(1)} \)  and paramagnetic current operator  \( \hat{j}_{d} \) :

 \[ \begin{align*}\chi_{abcd}(m_{1},m_{2},m_{3})=&\sum_{\mathcal{P}}\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{ac}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\mathcal{M}}_{b}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1})\hat{j}_{d}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1}+m_{3})\right]\\&+\sum_{\mathcal{P}}\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{ad}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\mathcal{M}}_{b}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1})\hat{j}_{c}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1}+m_{2})\right].\end{align*} \quad (B8) \] 

Using the isotropic approximation model Hamiltonian and after performing the integration on the azimuthal angle of electronic wave vector k, we obtain a vanishing result for all tensor elements. Therefore, within our low-energy model analysis, we have

 \[ \chi_{a b c d}^{t r i a n g l e-\Theta}(\omega_{1},\omega_{2},\omega_{3})=0. \quad (B9) \]
 

## 4. Calculation of  \( \bar{\chi}_{abcd}^{bubble-\Theta} \)  for the diagram depicted in Fig. 1h

The triangle diagram Fig. 1h can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and photon-electron-phonon matrix-element  \( \hat{\Theta}_{ac}^{(1)} \) :

 \[ \begin{align*}\chi_{abcd}(m_{1},m_{2},m_{3})=&\sum_{\mathcal{P}}\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{ac}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\Theta}_{bd}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{2}+m_{3})\right]\\&+\sum_{\mathcal{P}}\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Theta}_{ad}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\Theta}_{bc}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{1}+m_{3})\right].\end{align*} \quad (B10) \] 

Similar to the square diagram the only non-vanishing tensor elements are given by  \( \chi_{xxxx} = \chi_{yyyy} \) ,  \( \chi_{xxyy} = \chi_{xyyx} = \chi_{yxyx} \) ,  \( \chi_{xyyx} = \chi_{yxyx} \) . The straightforward algebra similar to what was discussed earlier, one can obtain the four non-vanishing tensor elements in the following form:

 \[ \bar{\chi}_{xxxx}(\omega_{1},\omega_{2},\omega_{3})=C_{\Theta}\Biggl\{\ln\Big[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{1}+\omega_{3})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{2}+\omega_{3})^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B11) \] 

 \[ \bar{\chi}_{x x y y}(\omega_{1},\omega_{2},\omega_{3})=C_{\Theta}\Biggl\{-\ln\Big[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{1}+\omega_{3})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{2}+\omega_{3})^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B12) \] 

 \[ \bar{\chi}_{x y y x}(\omega_{1},\omega_{2},\omega_{3})=C_{\Theta}\Biggl\{\ln\Big[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\Big]-\\ \ln\Big[1-\frac{(\omega_{1}+\omega_{3})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{2}+\omega_{3})^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B13) \] 

 \[ \bar{\chi}_{x y x y}(\omega_{1},\omega_{2},\omega_{3})=C_{\Theta}\Biggl\{\ln\Big[1-\frac{(\omega_{1}+\omega_{2})^{2}}{4\mu^{2}}\Big]+\\ \ln\Big[1-\frac{(\omega_{1}+\omega_{3})^{2}}{4\mu^{2}}\Big]-\\ \ln\Big[1-\frac{(\omega_{2}+\omega_{3})^{2}}{4\mu^{2}}\Big]\Biggr\}. \quad (B14) \] 

where

 \[ C_{\Theta}=\frac{N_{f}m[\Theta^{(1)}]^{2}}{24\pi\hbar^{2}}. \quad (B15) \] 

## 5. Calculation of  \( \bar{\chi}_{abcd}^{bubble-\Delta} \)  for the diagram depicted in Fig. 1i

The triangle diagram Fig. 1i can be written in terms of electronic Green's function  \( \hat{G}(\mathbf{k}, ik_{n}) \)  and photon-electron-phonon matrix-element  \( \hat{\Delta}_{ac}^{(1)} \)  and electron-phonon matrix-element  \( \hat{\mathcal{N}}_{b}^{(1)} \) :

 \[ \chi_{5,abcd}(m_{1},m_{2},m_{3})=\sum_{\mathcal{P}}\frac{1}{2S}\sum_{\mathbf{k}}\frac{1}{\beta}\sum_{n}\mathrm{Tr}\left[\hat{\Delta}_{acd}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n)\hat{\mathcal{N}}_{b}^{(1)}(\mathbf{k})\hat{G}(\mathbf{k},n+m_{3})\right] \quad (B16) \] 

Similar to the square diagram the only non-vanishing tensor elements are given by  \( \chi_{xxxx} = \chi_{yyyy} \) ,  \( \chi_{xxyy} = \chi_{yxyx} \) ,  \( \chi_{xyyx} = \chi_{yxyx} \) ,  \( \chi_{xyyx} = \chi_{yxyx} \) . The straightforward algebra similar to what was discussed earlier, one can obtain the four non-vanishing tensor elements in the following form:

 \[ \bar{\chi}_{xxxx}(\omega_{1},\omega_{2},\omega_{3})=-\frac{3C_{\Delta}}{2}\Biggl\{\ln\Big[1-\frac{\omega_{1}^{2}}{4\mu^{2}}\Big]+\ln\Big[1-\frac{\omega_{2}^{2}}{4\mu^{2}}\Big]+\ln\Big[1-\frac{\omega_{3}^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B17) \] 

 \[ \bar{\chi}_{xxyy}(\omega_{1},\omega_{2},\omega_{3})=-\frac{C_{\Delta}}{2}\Biggl\{-\ln\Big[1-\frac{\omega_{1}^{2}}{4\mu^{2}}\Big]-\ln\Big[1-\frac{\omega_{2}^{2}}{4\mu^{2}}\Big]+\ln\Big[1-\frac{\omega_{3}^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B18) \] 

 \[ \bar{\chi}_{xyxy}(\omega_{1},\omega_{2},\omega_{3})=-\frac{C_{\Delta}}{2}\Biggl\{\ln\Big[1-\frac{\omega_{1}^{2}}{4\mu^{2}}\Big]-\ln\Big[1-\frac{\omega_{2}^{2}}{4\mu^{2}}\Big]-\ln\Big[1-\frac{\omega_{3}^{2}}{4\mu^{2}}\Big]\Biggr\}, \quad (B19) \] 

 \[ \bar{\chi}_{xyyx}(\omega_{1},\omega_{2},\omega_{3})=-\frac{C_{\Delta}}{2}\Biggl\{-\ln\Big[1-\frac{\omega_{1}^{2}}{4\mu^{2}}\Big]+\ln\Big[1-\frac{\omega_{2}^{2}}{4\mu^{2}}\Big]-\ln\Big[1-\frac{\omega_{3}^{2}}{4\mu^{2}}\Big]\Biggr\}. \quad (B20) \]
 

where

 \[ C_{\Delta}=\frac{N_{f}m\Delta^{(1)}\mathcal{M}^{(1)}}{24\pi\hbar^{2}}. \quad (B21) \] 

Since  \( \Delta^{(1)}\mathcal{M}^{(1)}=[\Theta^{(1)}]^{2} \) , we have  \( C_{\Delta}=C_{\Theta} \) .
 
