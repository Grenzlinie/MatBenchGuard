
# The optimal Boson energy for superconductivity in the Holstein model

Chungwei Lin \( ^{*} \) , Bingnan Wang, and Koon Hoo Teo

Mitsubishi Electric Research Laboratories, 201 Broadway, Cambridge, MA 02139, USA

(Dated: September 16, 2021)

We examine the superconducting solution in the Holstein model, where the conduction electrons couple to the dispersionless Boson fields, using the Migdal-Eliashberg theory and Dynamical Mean Field Theory. Although different in numerical values, both methods imply the existence of an optimal Boson energy for superconductivity at a given electron-Boson coupling. This non-monotonous behavior can be understood as an interplay between the polaron and superconducting physics, as the electron-Boson coupling is the origin of the superconductor, but at the same time traps the conduction electrons making the system more insulating. Our calculation provides a simple explanation on the recent experiment on sulfur hydride, where an optimal pressure for the superconductivity was observed. The validities of both methods are discussed.

PACS numbers: 74.20.-z, 74.20.Fg, 74.25.Kc

## I. INTRODUCTION

Since the discovery of superconductivity by Onnes  \( [1] \) , countless efforts have been dedicated to understanding the microscopic origin of the phenomena, as well as to searching/synthesizing materials of high superconducting critical temperatures  \( (T_{c}) \) . Based on the microscopic theories, the superconductors are classified as “conventional” and “unconventional” superconductors. The former class can be well described by the BCS (Bardeen-Cooper-Schrieffer) theory  \( [2-4] \)  or its variants  \( [5] \) , whereas the latter class is still controversial in its microscopic mechanisms  \( [6] \) . The unconventional superconductors include the layered materials such as cuprates  \( [7, 8] \)  and iron-based materials  \( [9-11] \) . The multi-orbital nature and strong electron correlation intrinsically complicate the problem, as there can be several competing phases  \( [12, 13] \) . For this reason, searches of unconventional high temperature superconductors are mainly based on “perturbing the existing superconductors” (via doping, applying pressure, interfacing with other materials … etc) and “exhausting all possible compounds”  \( [14] \) . The searches of conventional high temperature superconductors, on the other hand, are essentially guided by the BCS theory, or by the more realistic Eliashberg model  \( [15-21] \) , which is different from BCS theory in its explicit inclusion of the phonon (or the Boson in general) degrees of freedom. In the Eliashberg model, the origin of the effective electron-electron attraction is the electron-phonon coupling, and the main factor against superconductivity, the Coulomb repulsion, is treated at a semi-empirical level by one parameter  \( [17, 21, 22] \) . Therefore, the key to enhance  \( T_{c} \)  is to control the phonon-related parameters – the Debye frequency and the electron-phonon coupling. Recent experiments on sulfur hydride, whose motivation behind is to increase the Debye frequency by using light elements (H) and applying high pressure, exhibit a record superconducting  \( T_{c} \)  at 203 K  \( [23] \) . The strong enhancement of superconducting  \( T_{c} \)  in the mono-layer FeAs or FeSe on  \( SrTiO_{3} \)  substrate is deeply related to the interfacial optical phonon mode  \( [11, 24-27] \) . Attempts of using Boson other than phonons, such as the plasma in meta-materials, to mediate the electron-electron attraction also appear promising  \( [28, 29] \) .

The Holstein model  \( [30] \) , where the conduction electrons couple to the dispersionless Boson fields, is the simplest model that captures the physics of conventional superconductors. In this work, we examine the superconducting solution in Holstein model, using the Migdal-Eliashberg (ME) theory  \( [15, 16] \)  and the Dynamical Mean Field Theory (DMFT)  \( [31–34] \)  with the exact diagonalization (ED) impurity solver. This model has been intensely studied  \( [35–47] \) , but relatively few explicitly break the gauge symmetry to obtain the superconducting solution  \( [48, 49] \) . Although different in numerical values, both ME and DMFT imply the existence of an optimal Boson energy for superconductivity at a given electron-Boson coupling. The existence of the optimal Boson energy can be expected from the BCS theory – if we take the cutoff energy as the Boson energy  \( \Omega \) , and the effective electron-electron attraction as  \( -g^{2}/\Omega \)  (an estimate from the second-order perturbation) with g being the electron-Boson coupling, the superconducting gap behaves as  \( \Delta(\Omega) \sim \Omega \exp[-(g^{2}/\Omega)D_{0}] \)  with  \( D_{0} \)  the electron density of states at the Fermi energy. The ME theory
 

actually gives a very similar behavior. The DMFT, however, gives different ground state under some parameter regimes, as it captures the polaron effect, where the Boson that mediates the electron-electron attraction can make the system insulating. The DMFT calculation also elucidates the relationship between the polaron solution and the superconducting solution.

The rest of the paper is organized as follows. In Section II we describe the Holstein model and the two methods – the ME theory and DMFT – to obtain the superconducting solutions. We provide a simple picture that is emerged from DMFT, on how the Boson field can lead to the superconducting solution. In Section III, we present our main results, compare them to those in the literature, and discuss their validities and implications. Finally a brief conclusion is given in Section IV.

![](./images/867770674649760111_1.jpg)

FIG. 1: (a) The Holstein model in real space: each local electron couples to an external Boson field. Each dashed line represents the electron-Boson coupling. (b) The only Feynman diagram included in the Migdal-Eliashberg theory, with the lattice Green's function  \( \tilde{G}(\mathbf{k}, i\omega_{n}) \)  solved self-consistently. (c) The auxiliary impurity model in DMFT. Instead of solving the lattice problem where each local orbital couples to an external Boson field, DMFT iteratively solves an impurity problem where only the impurity orbital couples to the external Boson field. (d) The picture emerged from the DMFT calculation. If the doubly-occupied and zero-occupied impurity orbitals are degenerate or close in energy for the local Hamiltonian, introducing a coupling between these two local states by breaking the particle conservation further lowers the energy via producing a "binding" combination of these two states.

## II. HOLSTEIN MODEL AND SOLVERS

In this section we introduce the Holstein model, and the two solvers we used – the ME theory and DMFT – to solve this model. The expressions of the main observables, including the superconducting gap and the pairing amplitude, are given. Several hints of the existence of the optimal Boson energy for superconductivity will be highlighted.

## A. Holstein model and superconducting gap

The Holstein model is given by

 \[ \begin{align*}H&=H_{elec}+H_{ph}+H_{e-ph}\\&=\sum_{\mathbf{k}}\varepsilon_{\mathbf{k}}(c_{\mathbf{k},\uparrow}^{\dagger}c_{\mathbf{k},\uparr}+c_{\mathbf{k},\downarrow}^{\dagger}c_{\mathbf{k},\downarrow})+\Omega\sum_{\mathbf{k}}a_{\mathbf{k}}^{\dagger}a_{\mathbf{k}}+\frac{g}{\sqrt{N}}\sum_{\mathbf{k},\mathbf{q}}(c_{\mathbf{k}+\mathbf{q},\uparrow}^{\dagger}c_{\mathbf{k},\uparr}+c_{\mathbf{k}+\mathbf{q},\downarrow}^{\dagger}c_{\mathbf{k},\downarrow})(a_{\mathbf{q}}+a_{\mathbf{q}}^{\dagger}-a_{\mathbf{q}}^{\prime}).\end{align*} \quad (1) \] 

Here  \( c_{k,\sigma} \)  represents the Fermion degree of freedom, whereas  \( a_{k} \)  represents the Boson degree of freedom. In Eq. (1), we can rewrite  \( H_{ph} \)  and  \( H_{e-ph} \)  in the real-space coordinate as

 \[ H_{p h}+H_{e-p h}=\Omega\sum_{i}a_{i}^{\dagger}a_{i}+g\sum_{i,\sigma}(c_{i,\sigma}^{\dagger}c_{i,\sigma}-1)(a_{i}+a_{i}^{\dagger}). \quad (2) \] 

This form is more natural for DMFT calculations. The Holstein model in the real-space representation is illustrated in Fig. 1(a). In this work, we shall consider the conduction band of semicircular density of states (DOS)  \( \nu(\varepsilon)= \)
 

 \( \sqrt{4t^{2}-\varepsilon^{2}}/(2\pi t^{2}) \) . This corresponds to the Bethe lattice of infinite dimension, a limit where the DMFT result becomes exact. The bandwidth is fixed at 4t with t=1, and all energy scales, including the electron-Boson coupling g and the Boson energy  \( \Omega \) , are measured in t. We only show the results at half filling, and the -1 in  \( (c_{i,\sigma}^{\dagger}c_{i,\sigma}-1) \)  of Eq. (2) ensures that the Boson field is at its ground state when the local occupation is 1 (half-filled) [43].

To obtain the superconducting solutions, both ME theory and DMFT self-consistently determine the Nambu Green's functions at the Matsubara frequencies. Defining a Nambu spinor as  \( \Psi_{\mathbf{k}}^{\dagger} = (c_{\mathbf{k},\uparrow}^{\dagger}, c_{-\mathbf{k},\downarrow}) \) , the lattice Green function (a  \( 2 \times 2 \)  matrix) on the imaginary-time axis and at the Matsubara frequency is given by

 \[ \begin{align*}\hat{G}(\mathbf{k},\tau)&=-T\langle\Psi_{\mathbf{k}}(\tau)\Psi_{\mathbf{k}}^{\dagger}(0)\rangle=\begin{pmatrix}G(\mathbf{k},\tau)&F(\mathbf{k},\tau)\\F(\mathbf{k},\gamma^{*}&-G(-\mathbf{k},-\tau)\end{pmatrix}\\&\Rightarrow\hat{G}(\mathbf{k},i\omega_{n})=\begin{pmatrix}G(\mathbf{k},i\omega_n)&F(\mathbf{k},i \omega_n)\\F^{*}(\mathbf{k},i\omega_n)&-G(-\mathbf{k},-i\omega_n)\end{pmatrix}\end{align*} \quad (3) \] 

where  \( \langle...\rangle \)  represents the ground state expectation value. Using Pauli matrices

 \[ \sigma_{1}=\begin{pmatrix}{{{0}}}&{{{1}}} \\{{{1}}}&{{{0}}}\end{pmatrix},\sigma_{2}=\begin{pmatrix}{{{0}}}&{{{-i}}} \\{{{i}}}&{{{0}}}\end{pmatrix},\sigma_{3}=\begin{pmatrix}{{{1}}}&{{{0}}} \\{{{0}}}&{{{-1}}}\end{pmatrix}, \quad (4) \] 

the self-energies and the lattice Green’s functions are parameterized as

 \[ \begin{align*}\hat{\Sigma}(\mathbf{k},i\omega_{n})&=i\omega_{n}[1-Z(\mathbf{k},i\omega_{n})]\hat{\sigma}_{0}+\chi(\mathbf{k},i\omega_{n})\hat{\sigma}_{3}+\phi(\mathbf{k},i\omega_{n})\hat{\sigma}_{1}+\phi_{2}(\mathbf{k},i\omega_{n})\hat{\sigma}_{2}\\\hat{G}^{-1}(\mathbf{k},i\omega_{n})&=\hat{G}_{0}^{-1}(\mathbf{k},i\omega_{n})-\hat{\Sigma}(\mathbf{k},iomega_{n})\\&=i\omega_{n}Z(\mathbf{k},i\omega_{n})\hat{\sigma}_{0}-[\varepsilon_{\mathbf{k}}+\chi(\mathbf{k},i\omega_{n})]\hat{\sigma}_{3}-\phi(\mathbf{k},i\omega_{n})\hat{\sigma}_{1}-\phi_{2}(\mathbf{k},i\omega_{n})\hat{\sigma}_{2}.\end{align*} \quad (5) \] 

with  \( \hat{G}_{0}(\mathbf{k},i\omega_{n}) \)  being the non-interacting Green's function. Without loss of generality, we can choose  \( \phi_{2}=0 \) , and the task is to determine  \( Z(\mathbf{k},i\omega_{n}) \) ,  \( \phi(\mathbf{k},i\mathbf{\omega}_{n}) \) , and  \( \chi(\mathbf{k},i\mathbf{\omega}_{n}) \)  self-consistently using some approximation.

When the lattice Green’s function are obtained, its poles determine the single-particle excitations. From Eq. (5), the poles are determined by (with the analytical continuation  \( i\omega_{n} \rightarrow \omega \) )

 \[ -\left[\omega Z(\mathbf{k},\omega)\right]^{2}+\left[\varepsilon_{\mathbf{k}}+\chi(\mathbf{k},\omega)\right]^{2}+\phi^{2}(\mathbf{k},\omega)=0. \quad (6) \] 

For the normal state  \( (\phi=0) \) , the poles are given by  \( \omega=\pm[\varepsilon_{\mathbf{k}}+\chi(\mathbf{k},\omega)]/Z(\mathbf{k},\omega) \) , which are simply the quasi-particle (quasi-hole) excitations. For the non-zero  \( \phi \) , the excitation occurs at  \( \omega=\pm\sqrt{[\varepsilon_{\mathbf{k}}+\chi(\mathbf{k},\omega)]^{2}+\phi(\mathbf{k},\omega)^{2}}/Z(\mathbf{k},\omega) \) . When neglecting the k dependence (an approximation we are using in this paper), the superconducting gap is obtained by energy difference  \( |\omega_{+}-\omega_{-}| \) , with  \( \omega_{\pm}=\pm\phi(\omega)/Z(\omega) \) . Keeping only the constant term of Z and  \( \phi \) , the gap is approximately

 \[ \frac{\Delta}{2}=\frac{\phi}{Z}(\omega=0)\approx\frac{\phi(i\omega_{0})}{Z(i\omega_{0})}, \quad (7) \] 

where  \( Z(0) \approx Z(i\omega_{0}) \)  and  \( \phi(0) \approx \phi(i\omega_{0}) \)  are used. In addition to the superconducting gap, the superconductivity can also be characterized by the pairing amplitude  \( \Psi \) 

 \[ \Psi\equiv\langle c_{i,\uparrow}c_{i,\downarrow}\rangle=T\sum_{n}\phi(i\omega_{n}). \quad (8) \] 

Note that  \( \Psi \)  is a dimensionless quantity, whose amplitude is always smaller than one. Eq. (7) and Eq. (8) will be used to characterize the superconducting state.

## B. Migdal-Eliashberg theory

The Migdal-Eliashberg theory is formulated in the momentum space. It keeps only the “Fock” contribution in the self energies [see Fig. 1(b) for the diagrammatic representation]:

 \[ \hat{\Sigma}(\mathbf{k},i\omega_{n})=-T\sum_{\mathbf{k}^{\prime},n^{\prime}}\hat{\sigma}_{3}\hat{G}(\mathbf{k}^{\prime},i\omega_{n})\hat{\sigma}_{3}\times|g(\mathbf{k},\mathbf{k}^{\prime})|^{2}D(\mathbf{k}-\mathbf{k}^{\prime},i\omega_{n}-i\omega_{n^{\prime}}), \quad (9) \]
 

 \( \hat{G}^{od} \)  is the off-diagonal part of the Green's function,  \( g(\mathbf{k},\mathbf{k}^{\prime}) \)  is the coupling that annihilates an electron of momentum k and creates an electron of momentum  \( k^{\prime} \) , and  \( D(\mathbf{k},i\omega_{n}) \)  is the Boson Green's function. Substituting Eq. (9) into Eq. (5), we obtain the equation for  \( Z(\mathbf{k},i\omega_{n}) \) ,  \( \phi(\mathbf{k},i\mathbf{\omega}_{n}) \) , and  \( \chi(\mathbf{k},i\mathbf{\omega}_{n}) \)  as

 \[ [1-Z(\mathbf{k},i\omega_{n})]i\omega_{n}=-T\sum_{\mathbf{k}^{\prime},n^{\prime},\lambda}|g(\mathbf{k},\mathbf{k}^{\prime},\lambda)|^{2}D_{\lambda}(\mathbf{k}-\mathbf{k}^{\prime},i\omega_{n}-i\omega_{n^{\prime}})\frac{i\omega_{n^{\prime}}\mathcal{Z}(\mathbf{k}^{\prime},i\omega_{n^{\prime}})}{-\Theta(\mathbf{k}^{\prime},i\omega_{n^{\prime}})}, \quad (10a) \] 

 \[ \chi(\mathbf{k},i\omega_{n})=-T\sum_{\mathbf{k}^{\prime},n^{\prime},\lambda}|g(\mathbf{k},\mathbf{k}^{\prime},\lambda)|^{2}D_{\lambda}(\mathbf{k}-\mathbf{k}^{\prime},i\omega_{n}-i\omega_{n^{\prime}})\frac{[\varepsilon_{\mathbf{k}^{\prime}}+\chi(\mathbf{k}^{\prime},i\omega_{n^{\prime}})]}{-\Theta(\mathbf{k}^{\prime},i\omega_{n^{\prime}})}, \quad (10b) \] 

 \[ \phi(\mathbf{k},i\omega_{n})=T\sum_{\mathbf{k}^{\prime},n^{\prime},\lambda}|g(\mathbf{k},\mathbf{k}^{\prime},\lambda)|^{2}D_{\lambda}(\mathbf{k}-\mathbf{k}^{\prime},i\omega_{n}-i\omega_{n^{\prime}})\frac{\phi(\mathbf{k}^{\prime},i\omega_{n^{\prime}})}{-\Theta(\mathbf{k}^{\prime},i\omega_{n^{\prime}})}, \quad (10c) \] 

where  \( \Theta(\mathbf{k},i\omega_{n})=[\omega_{n}Z(\mathbf{k},i\mathbf{\omega}_{n})]^{2}+\varepsilon(\mathbf{k})^{2}+\phi(\mathbf{k},i\mathbf{\omega}_{n})^{2}+\chi(\mathbf{k},i\omega_{n})^{2} \) . For the Holstein model defined in Eq. (1), we have  \( g(\mathbf{k},\mathbf{k}^{\prime})=g \)  and  \( D(\mathbf{q},\omega)=-\frac{2\Omega}{\omega^{2}+\Omega^{2}} \) . We further simplify the equation by neglecting the momentum dependence, i.e.  \( Z(\mathbf{k},i\omega_{n})\to Z(i\omega_{n})\equiv Z_{n} \) ,  \( \phi(\mathbf{k},i\omega_{n})\to\phi(i\omega_{n})\equiv\phi_{n}\chi(\mathbf{k},i\omega_{n})\to\chi(i\omega_{n})\equiv\chi_{n} \) , and obtain the coupled equations

 \[ \begin{align*}[\omega_{n}Z_{n}]&=\sum_{n^{\prime}}-K(n,n^{\prime})[\omega_{n^{\prime}}Z_{n^{\prime}}]+\omega_{n}\\ \chi_{n}&=+K(n,n^{\prime})\chi_{n^{\prime}}+C_{n}\\ \phi_{n}&=\sum_{n^{\prime}}-K(n,n^{\prime})\phi_{n^{\prime}}\end{align*} \quad (11) \] 

with  \( K(n,n') = -Tg^{2}\frac{2\Omega}{\Omega^{2} + (\omega_{n} - \omega_{n'})^{2}} \times \sum_{\mathbf{k}} \frac{1/N}{\Theta(\mathbf{k}, \omega_{n'})} \) ,  \( C_{n} = +Tg^{2}\frac{2\Omega}{\Omega^{2} + (\omega_{n} - \omega_{n'})^{2}} \times \sum_{\mathbf{k}} \frac{\varepsilon(\mathbf{k})/N}{\Theta(\mathbf{k}, \omega_{n'})} \) , and  \( \Theta(\mathbf{k}, i\omega_{n}) = (\omega_{n}Z_{n})^{2} + \varepsilon^{2}(\mathbf{k}) + \phi_{n}^{2} + \chi_{n}^{2} \) . With the semicircular DOS  \( \nu(\varepsilon) = \sqrt{4t^{2} - \varepsilon^{2}/(2\pi t^{2})} \) ,  \( K(n,n') \)  and  \( C_{n} \)  are evaluated by

 \[ \begin{align*}K(n,n^{\prime})&=-Tg^{2}\frac{2\Omega}{\Omega^{2}+(\omega_{n}-\omega_{n^{\prime}})^{2}}\times\int d\varepsilon\frac{\nu(\varepsilon)}{\Theta(\varepsilon,i\omega_{n^{\prime}})},\\C_{n}&=+Tg^{2}\frac{2\Omega}{\Omega^{2}+(\omega_{n}-\omega_{n^{\prime}})^{2}}\times\int d\varepsilon\nu(\varepsilon)\frac{\varepsilon-\mu}{\Theta(\varepsilon,i\omega_{n^{\prime}})},\end{align*} \quad (12) \] 

with  \( \Theta(\varepsilon,i\omega_{n})=(\omega_{n}Z_{n})^{2}+(\varepsilon-\mu)^{2}+\phi_{n}^{2}+\chi_{n}^{2} \) . We solve Eq. (11) by iteration. The zero-temperature results obtained by using T=0.001 and keeping 4000 Matsubara frequencies; the results are checked against those obtained using lower temperature and keeping more Matsubara frequencies. Three comments about Eq. (11) are worth noting. First, by linearizing Eq. (11) ( \( \phi_{n} \)  components),  \( \det[K(n,n^{\prime})+I]=0 \)  determines the critical temperature  \( T_{c} \) . Second, due to the neglect of momentum dependence in the self energy, we expect the superconducting gap obtained using the approximation is under-estimated. Finally, as the magnitudes of  \( K(n,n^{\prime}) \)  are small at both small and large  \( \Omega \) , Eq. (11) suggests a optimal  \( \Omega \)  for the superconductivity. At this stage it is simply a mathematical observation, and we shall give a more physical discussion on Section II.D and Section III.A.

## C. Dynamical mean field theory

Dynamical mean field theory [32, 50] fully captures the local interaction via an auxiliary impurity model, and determines the impurity-bath hybridization parameters by equating the lattice local Green's function to the impurity Green's function [see Fig.1(c) for an illustration]. For the superconducting solution, the impurity model is

 \[ \begin{align*}H_{imp,SC}=\varepsilon_{d}\sum_{\sigma}c_{1,\sigma}^{\dagger}c_{1,\sigma}+\sum_{p=1}^{N}t_{sc,p}(c_{p,\uparrow}^{\dagger}c_{p,\downarrow}^{\dagger}+h.c.)+\sum_{p=2,\sigma}^{N}t_{p}[c_{1,\sigma}^{\dagger}c_{p,\sigma}+h.c.]+\sum_{p=2,\sigma}^{N}\varepsilon_{p}c_{p,\sigma}^{\dagger}c_{p,\sigma}\\ +g(n_{1,\uparrow}+n_{1,\downarrow}-\alpha)(a+a^{\dagger})+\Omega a^{\dagger}a,\end{align*} \quad (13) \] 

which explicitly breaks the particle conservation via the term  \( t_{sc,p}(c_{p,\uparrow}^{\dagger}c_{p,\downarrow}^{\dagger}+h.c.) \) . We have assumed site 1 to be the impurity site. We use exact diagonalization (ED) [51] for the impurity problem, and consider the zero-temperature solution. Due to computational cost, we include five bath orbitals (totally six orbitals including the impurity), which
 

is shown to be sufficient for the attractive Hubbard model [52]. As the particle number is not conserved, the impurity problem is solved in the grand-canonical ensemble. The details can be found in Ref. [52], and we point out one aspect specific to the Boson degree of freedom. As the model includes both Fermions and Bosons, the Hilbert space of Eq. (13) is defined as  \( |m\rangle_{e} \otimes |n\rangle_{ph} \) . The electronic state  \( |m\rangle_{e} \)  is a Fock state built from creating the Bogoliubov particles on the  \( |0\rangle \equiv \Pi_{p}c_{p,\downarrow}^{\dagger}|\mathrm{vac}\rangle \) , i.e.  \( |m\rangle_{e} = \Pi_{i}\gamma_{i}^{\dagger}|0\rangle \)  (with Bogoliubov orbitals  \( \gamma_{i}^{\dagger} \)  being composed of  \( c_{\uparrow}^{\dagger} \)  and  \( c_{\downarrow} \) ), whereas the phonon state is built from  \( |n\rangle_{ph} \sim (a^{\dagger})^{n}|0\rangle_{ph} \) . In principle, there are infinite number of phonon states; in practice we keep  \( n_{max} \)  phonon states ( \( |n\rangle_{ph} \)  with  \( n = 0 \)  to  \( n_{max} - 1 \) ) such that the converged result does not change for  \( n_{max} \to n_{max} + 5 \) . A simple criterion is that  \( n_{max}\Omega \)  is much larger than all relevant energy scales such as bandwidth and electron-Boson coupling, therefore the smaller the Boson energy  \( \Omega \)  is, the more phonon states one needs to keep. For this reason the parameter space of small  \( \Omega \)  is difficult to reach. Typically we use  \( n_{max} \)  ranging from 20 to 40. Two technical details are also noted. First, in the calculation, an effective temperature is needed, and we choose  \( T_{eff} = 0.01 \) , based on which 1000 Matsubara frequencies are kept. Second, we use configuration interaction impurity solver [52–56] in the early self-consistency iterations, which significantly accelerates the convergence.

We complete the discussion by examining how the coupling to a Boson field can lead to the superconducting solution in DMFT, as the electron-electron attraction may not be obvious in the model. In the impurity model [Eq. (13)], double and zero occupation on the impurity orbital result in phonon Hamiltonians of  \( \pm g(a+a^{\dagger}) + \Omega a^{\dagger}a = -\frac{g^{2}}{12} + \Omega(a^{\dagger} \pm g/2)(a \pm g\Omega) \) . Regardless of the sign of g, they both gain energy of  \( -g^{2}/\Omega \) . If we ignore the Boson dynamics and use the semiclassical impurity solver [57–59], the system is trapped in one of the minimum and we obtain a polaron solution – half of the lattice sites are doubly occupied and half the them empty. The superconducting state, which allows a direct coupling between these two local minimum whose local occupations are differed by two, further lowers the energy via producing a “binding” combination of these two states. This picture, emerged from the DMFT formalism that emphasizes the local physics, connects the polaron solution and superconducting solution, and is illustrated in Fig. 1(d).

## D. Polaron and superconductivity

We conclude this section by associating the polaron and superconducting effects to different components of the Green's function, based on which these two effects can be quantified. In Eq. (5), the superconductivity is characterized by the off-diagonal component  \( \phi \) , whereas the polaron effect by the diagonal component Z. The superconducting part is straightforward, as  \( \phi \)  directly relates to the pairing amplitude. For the polaron part, we first note that 1/Z is the quasi-particle weight, which is always between 0 and 1 [60]. Smaller 1/Z leads to a smaller spectral weight near the Fermi energy ( \( E_{F} \) , which is zero in our convention). The coupling to Bosons tends to slow the electron motion (regardless of its spin), as the excited Bosons “drag” the electron motion. This polaron effect makes the system more insulating, and results in the large Z and the reduced spectral function. The polaron effect is expected to become stronger when the Boson is easier to excite, which happens at smaller Boson energies  \( \Omega \) . Our simulations (both ME theory and DMFT) indeed give a larger Z in these regions [see Fig. 2(b)]. As the reduction in DOS is against superconductivity, a reduction of superconductivity at smaller  \( \Omega \)  is expected, and is indeed observed for both methods [see Section III.A].

## III. RESULTS AND DISCUSSION

In this section we show the numerical results and discuss their implications. For both Migdal-Eliashberg theory and DMFT, the superconducting gap  \( [\phi/Z, Eq. (7)] \)  and the pairing amplitude  \( [\Psi, Eq. (8)] \)  are shown. For DMFT, the computed spectral functions are also shown.

## A. Superconducting gap, pairing amplitude, and spectral functions

Fig. 2(a) shows the (half) superconducting gap as a function of Boson energy at the half filling. The electron-boson coupling is fixed at g = 0.6. We find that there exists an optimal Boson energy  \( \Omega_{opt} \)  for the superconducting gap, which is around  \( \Omega_{opt} \sim 0.4 \)  for these parameters. The ME theory, although resulting in different numerical values,
 
![](./images/867770674649760111_2.jpg)

(a)

![](./images/867770674649760111_3.jpg)

(b)

FIG. 2: (a) The half gap, computed from both DMFT and Migdal-Eliashberg theory, as a function of Boson energy for the Holstein model at half filling. The electron-boson coupling g = 0.6. For both Migdal-Eliashberg theory and the DMFT, there exists an optimal Boson energy  \( \Omega_{opt} \)  for the superconducting gap:  \( \Omega_{op} \sim 0.4 \)  for DMFT;  \( \Omega_{opt} \sim 0.15 \)  for the Eliashberg theory. The DMFT predicts a larger gap than the Migdal-Eliashberg theory at large  \( \Omega \) . (b)  \( Z(i\omega_{0}) \)  (black, left y-axis) and  \( \phi(i\omega_{0}) \)  (red, right y-axis) as a function of Boson energies, obtained from DMFT (solid curves) and the ME theory (dashed).  \( \phi(i\omega_{0}) \)  of ME theory are multiplied by 10 to fit the scale. When  \( \Omega \)  decreases, both  \( Z(i\omega_{0}) \)  and  \( \phi(i\omega_{0})^{-1} \)  increase. The ME theory gives a milder behavior compared to DMFT.

![](./images/867770674649760111_4.jpg)

FIG. 3: The pairing amplitude,  \( \Psi \equiv \langle d_{\uparrow} d_{\downarrow} \rangle \) , as a function of the Boson energy  \( \Omega \) . Results obtained from both DMFT and Eliashberg theory are shown. The shape similar the superconducting gap [Fig. 2(a)] is observed.

exhibits the same non-monotonous behavior, with the optimal Boson energy at  \( \Omega_{opt} \sim 0.15 \) . To analyze the origin of the non-monotonous behavior, Fig. 2(b) shows  \( Z(i\omega_{0}) \)  and  \( \phi(i\omega_{0})^{-1} \)  (whose ratio determines the gap amplitude) as a function of Boson energies. The ME theory results in the similar but milder  \( Z(i\omega_{0}) \)  and  \( \phi(i\omega_{0})^{-1} \)  behavior. At very large  \( \Omega \)  ( \( \Omega \gg \Omega_{opt} \) ), both polaron and superconducting effects are weak ( \( Z(i\omega_{0}) \sim 1 \)  and  \( \phi(i\omega_{0}) \sim 0 \) ), because the Boson energy is too large and has little effects on the ground state property. When  \( \Omega \)  decreases, both  \( Z(i\omega_{0}) \)  and  \( \phi(i\omega_{0})^{-1} \)  increase, but at different rates. At larger  \( \Omega \)  ( \( \Omega \gtrsim \Omega_{opt} \) ),  \( \phi(i\omega_{0})^{-1} \)  grows faster, leading to increasing gap amplitudes. At smaller  \( \Omega \)  ( \( \Omega \lesssim \Omega_{opt} \) ),  \( Z(i\omega_{0})^{-1} \)  grows faster, leading to decreasing gap amplitudes. As  \( \Omega \to 0 \)  (only obtained using ME theory), both  \( Z(i\omega_{0})^{-1} \)  and  \( \phi(i\omega_{0}) \)  diverge, with the former being much faster. From our discussion in Section II.D, the decreasing superconducting gap below  \( \Omega_{opt}^{-1} \)  is the consequence that the polaron effect starts to dominate over the superconductivity at small  \( \Omega \) . Fig. 3 provides the pairing amplitude  \( \Psi(\equiv \langle d_{\uparrow} d_{\downarrow} \rangle) \)  as a function of the Boson energy  \( \Omega \) , and the shape similar the superconducting gap is seen. The spectral functions at half filling for g = 0.6 are provided in Fig. 4(a). As the Boson energy decreases, the spectral function first develops a dip [61] around the Fermi energy, indicating the superconducting state, and then keeps on decreasing in value due to the increasing polaron effect [Z in Fig. 2(b)]. We emphasize that both  \( \phi \)  and Z lead to a reduction in the spectral function near  \( E_{F} \) , and it is not easy
 

to distinguish the polaron from the superconducting effect from the spectral function alone. An explicit evaluation of Z and  \( \phi \)  to separate these two effects. To confirm that the dip around zero for  \( \Omega > \Omega_{opt} \)  is indeed caused by the superconductivity, not by the error caused by including only five bath orbitals, Fig. 4(b) presents the spectral function computed  \( \varepsilon \) 

![](./images/867770674649760111_5.jpg)

(a)

![](./images/867770674649760111_6.jpg)

(b)

FIG. 4: (a) The spectral function for  \( \Omega = 0.6 \) , 0.5, 0.4 and 0.36 at half filling. A dip around zero is the indication of superconducting gap. As  \( \Omega \)  decreases, and the superconducting gap becomes more apparent. Below the optimal Boson energy ( \( \Omega = 0.36 \) ), the DOS keeps on decreasing because of the increasing Z [Fig. 2(b)], which is a consequence of the strong polaron effect. (b) The spectral function for  \( \Omega = 0.5 \)  at fillings of 1 (solid curve with shaded region) and 0.8. A dip around zero is seen for both cases.

![](./images/867770674649760111_7.jpg)

FIG. 5:  \( \sqrt{\left(\Omega+a^{\dagger}\right)^{2}/\Omega} \) , which measures the Boson field fluctuation, as a function of the Boson energy  \( \Omega \) . This value increases upon decreasing  \( \Omega \) .

## B. Limitations of solvers and comparison to other methods

There are two dimensionless parameters that govern the validity of the ME theory – one  \( \Omega/E_{F} \)  and  \( \lambda=\frac{q^{2}}{2t} \) . The former is derived from the Midgal theory [16, 20, 21] which gives the condition where the vertex correction can be neglected; the later is obtained from DMFT [38, 39], and is proportional to  \( \left.\frac{\partial\Sigma(\omega)}{\partial\omega}\right|_{\omega=0} \)  obtained from ME theory [21]. Both parameters have to be small for ME theory to work. Roughly, the small  \( \lambda \)  guarantees the correct ground state, and the small  \( \Omega/E_{F} \)  gives the correct excitations [39]. Note that small  \( \lambda \)  implies that ME theory is not valid for any given g at small enough  \( \Omega \) . As DMFT becomes exact in the infinite-dimension limit, we use it as a reference to see when and how the ME theory breaks down. As expected, the gaps obtained from ME theory and DMFT become closer when  \( \lambda \)  is small (larger  \( \Omega \)  at a given g). When  \( \lambda \)  is large, ME theory does not properly capture the polaron effect and thus gives the (wrong) superconducting ground state. Without considering the superconducting
 

solution, Ref. [38] determines the critical value  \( \lambda_{c} \)  is of order one, above which the system becomes insulating. From Fig. 2(a) and Fig. 3, we see that below  \( \Omega\sim0.33 \) , the superconducting amplitude becomes negligible and the system is in the polaron state. As the ME theory predicts the superconducting state for all  \( \Omega \) , our calculation results in a  \( \lambda_{c}\approx\frac{0.6^{2}}{0.33\times1}\approx1.1 \) , above which the ME theory gives the wrong ground state. We have done the calculations for g=0.3, 0.4 and 0.5 (not shown), and the resulting  \( \lambda_{c} \)  are all around 1. Our DMFT calculations thus extend the criterion given in Refs. [38, 39] to the superconducting solution.

We also examine the harmonic Boson potential at small  \( \Omega \) . We first represent the Boson field as a simple harmonic oscillator, i.e.  \( \Omega(a^{\dagger}a+1/2)=\frac{p^{2}}{2m}+\frac{m\Omega^{2}}{2}x^{2} \)  (the convention  \( \hbar\equiv1 \)  is used), with x a distortion field. In this representation the distortion  \( x=\frac{1}{\sqrt{2m\Omega}}(a^{\dagger}+a) \) , and  \( \sqrt{\langle(x^{2})^{2}\rangle}\sim\sqrt{\langle(a+a^{\dagger})^{2}\rangle/\Omega} \)  characterizes the distortion fluctuation.  \( \sqrt{\langle(a+a^{\dagger})^{2}\rangle/\Omega} \)  as a function of  \( \Omega \)  is given in Fig. 5, which clearly shows a divergent behavior at small  \( \Omega \) . Note that the diverging behavior in Z and  \( \phi \)  [Fig. 2(b)], and the diverging behavior of  \( \sqrt{\langle(a+a^{\dagger})^{2}\rangle/\Omega} \)  [Fig. 5] happen at the same  \( \Omega \) , which signals the polaron insulating phase. When  \( \sqrt{\langle x^{2}\rangle} \)  is comparable to the lattice constant or the inter-electron distance, the validity of the quadratic potential may not be sufficient.

We now compare our results to those in the literature. We first discuss the DMFT results using other impurity solvers, including the Hirsch-Fye [62] Quantum Monte Carlo (QMC) [35–37], the second order perturbation in phonon propagators [36], the semiclassical solver [57, 59], the path integral [38], the diagrammatic expansion [39], and the continuous-time QMC [34, 49]. The Hirsch-Fye QMC is formally exact, and works efficiently at high temperature [35–37]. The critical temperatures for charge density wave (CDW) and superconducting phases are determined by the divergence of the corresponding susceptibilities. The ED solver used here is for zero-temperature phases, and a direct comparison cannot be made. An investigation on CDW order at zero temperature is worthwhile. We notice that in the large  \( \lambda \)  limit, DMFT yields the polaron insulating solution, which can easily lead some CDW order as the local occupation prefers either zero or two electrons. In this sense, the DMFT phase diagram is consistent with the results from the QMC calculation, where the CDW phase happens at small  \( \Omega \)  regime whereas superconductivity at large  \( \Omega \) , regime [35]. The semiclassical solver [57, 59] neglects the Boson dynamics, and captures only the polaron but not the superconducting physics. The analysis based on path integral [38] and diagrammatic expansion [39] identifies an important dimensionless parameter  \( \lambda = g^{2}/(\Omega t) \) , and our results (discussed in the first paragraph in this Section) are fully consistent with these results. In the parameter regime where both  \( \Omega \)  and g are comparable to the bandwidth, the bipolaron effect becomes important [63], and several phases such as supersolid, CDW, and superconducting states, along with a quantum critical point are obtained [49]. We do not explore the parameter regime, but it is the regime where the ED solver is applicable. Finally we note that in the two-dimensional electronic system, a weak electron-phonon coupling can lead to the CDW order that can coexist with the superconducting state [46, 47, 64]. The CDW order exhibited in this case originates mainly from the nesting of the band, but has nothing to do with the specific form the local interaction.

## C. Connection to the recent high-pressure experiment

In 2015, Drozdov et. al. shows that applying a high pressure to on sulfur hydride  \( \left(\mathrm{H}_{2}\mathrm{S}\right) \)  can enhance the superconducting  \( T_{c} \)  up to 203K, and the isotope effect (replacing hydrogen by deuterium and tritium reduces  \( T_{c} \) ) further confirms that it is the phonon-mediated conventional superconductor [23]. One of their findings is that there is an optimal pressure for the superconductivity, above which the superconducting  \( T_{c} \)  starts to decrease. Our calculation suggests a simple explanation for this non-monotonous behavior as a function of pressure, under the following three (reasonable) assumptions: (i) the Boson energy  \( \Omega \)  considered in the Holstein model corresponds to the Debye frequency (multiplied by  \( \hbar \) ); (ii) applying a pressure increases the Debye frequency; and (iii) the electron-phonon coupling does not change significantly (within 10%) upon applying the pressure. The isotope effect, which lowers the Debye frequency via increasing the atomic masses, lowers the superconducting  \( T_{c} \) . This well-known behavior corresponds to the Boson energy smaller than the optimal  \( \Omega_{opt} \) . When the applied pressure is too large such that the Debye frequency passes its optimal value, the superconducting  \( T_{c} \)  again decreases. We emphasize that the optimal pressure can also be caused by other physics – for example, the Coulomb repulsion becomes stronger upon increasing the pressure, and leads to a reduction of superconducting  \( T_{c} \) . Our calculation cannot tell which one is the main mechanism. However, it does imply that an optimal pressure exists even without invoking the Coulomb repulsion. To quantitatively see how superconductivity is affected by a Hubbard U is worthy of further investigations.
 

## IV. CONCLUSION

In this work we examine the superconducting solution in the Holstein model with semicircular density of states, using both the Migdal-Eliashberg theory and Dynamical Mean Field theory. The impurity model associated with DMFT is solved using the exact diagonalization. Although different in numerical values, both methods imply that for a given electron-Boson coupling there exists an optimal Boson energy for superconductivity. By analyzing the Green's function, this non-monotonous behavior originates from the interplay between superconducting and polaron effects. At large  \( \Omega \) , the polaron effect is small so the superconducting gap increases upon lowering  \( \Omega \) . Below certain  \( \Omega \) , the polaron effect starts to dominate and therefore reduces the superconductivity by making the system less metallic (reducing the DOS around the Fermi energy). In terms of many-body solvers, our DMFT results explicitly confirm that in the small  \( \Omega \)  limit, the ME theory breaks down by getting the wrong ground state. This result was already obtained in the calculations without breaking symmetries [38, 39], and here we extend this statement to the superconducting solution. Our calculation provides a simple explanation on the recent experiment on sulfur hydride, where a optimal pressure for the superconductivity was observed [23]. Searching Boson degrees of freedom (other than the phonons) to mediate the electron-electron attraction can be a promising approach to enhance the superconducting temperature.

## Acknowledgement

We thank Qi Chen and Prabhakar Bandaru for helpful discussions, and Andrew Millis for very insightful comments.

[1] H. K. Onnes, Commun. Phys. Lab. Univ. Leiden: 120b (1911).

[2] L. N. Cooper, Phys. Rev. 104, 1189 (1956), URL http://link.aps.org/doi/10.1103/PhysRev.104.1189.

[3] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys. Rev. 106, 162 (1957), URL http://link.aps.org/doi/10.1103/PhysRev.106.162.

[4] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys. Rev. 108, 1175 (1957), URL http://link.aps.org/doi/10.1103/PhysRev.108.1175.

[5] D. Kirzhnits, E. Maksimov, and D. Khomskii, Journal of Low Temperature Physics 10, 79 (1973), ISSN 0022-2291, URL http://dx.doi.org/10.1007/BF00655243.

[6] A. Mann, Nature 475, 280 (2011).

[7] J. G. Bednorz and K. A. Müller, Zeitschrift für Physik B Condensed Matter 64, 189 (1986), ISSN 1431-584X, URL http://dx.doi.org/10.1007/BF01303701.

[8] A. Damascelli, Z. Hussain, and Z.-X. Shen, Rev. Mod. Phys. 75, 473 (2003), URL http://link.aps.org/doi/10.1103/RevModPhys.75.473.

[9] Y. Kamihara, H. Hiramatsu, M. Hirano, R. Kawamura, H. Yanagi, T. Kamiya, and H. Hosono, JACS 128, 10012 (2006), http://dx.doi.org/10.1021/ja063355c, URL http://dx.doi.org/10.1021/ja063355c.

[10] Y. Kamihara, T. Watanabe, M. Hirano, and H. Hosono, JACS 130, 3296 (2008), http://dx.doi.org/10.1021/ja800073m, URL http://dx.doi.org/10.1021/ja800073m.

[11] J.-F. Ge, Z.-L. Liu, C. Liu, C.-L. Gao, D. Qian, Q.-K. Xue, Y. Liu, and J.-F. Jia, Nat Mater 14, 285 (2015), URL http://dx.doi.org/10.1038/nmat4153.

[12] E. Dagotto, Rev. Mod. Phys. 66, 763 (1994).

[13] M. Imada, A. Fujimori, and Y. Tokura, Rev. Mod. Phys. 70, 1039 (1998), URL http://link.aps.org/doi/10.1103/RevModPhys.70.1039.

[14] H. Hosono, K. Tanabe, E. Takayama-Muromachi, H. Kageyama, S. Yamanaka, H. Kumakura, M. Nohara, H. Hiramatsu, and S. Fujitsu, Science and Technology of Advanced Materials 16, 033503 (2015), URL http://stacks.iop.org/1468-6996/16/i=3/a=033503.

[15] G. M. Eliashberg, JEPT 11, 696 (1960).

[16] A. B. Migdal, JEPT 7, 996 (1958).

[17] P. Morel and P. W. Anderson, Phys. Rev. 125, 1263 (1962), URL http://link.aps.org/doi/10.1103/PhysRev.125.1263.

[18] P. B. Allen and R. C. Dynes, Phys. Rev. B 12, 905 (1975), URL http://link.aps.org/doi/10.1103/PhysRevB.12.905.

[19] G. Bergmann and D. Rainer, Z. Phys. 263, 59 (1973).

[20] G. Grimvall, The electron-phonon interaction in metal (North-Holland Publishing Company, 1981).
 

[21] P. B. Allen and B. Mitrovic, Solid State Physics 37, 1 (1983).

[22] W. L. McMillan, Phys. Rev. 167, 331 (1968), URL http://link.aps.org/doi/10.1103/PhysRev.167.331.

[23] A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, Nature 525, 73 (2015), URL http://dx.doi.org/10.1038/nature14964.

[24] W. Qing-Yan, L. Zhi, Z. Wen-Hao, Z. Zuo-Cheng, Z. Jin-Song, L. Wei, D. Hao, O. Yun-Bo, D. Peng, C. Kai, et al., Chin. Phys. Lett. 29, 037402 (2012), URL http://stacks.iop.org/0256-307X/29/i=3/a=037402.

[25] J. J. Lee, F. T. Schmitt, R. G. Moore, S. Johnston, Y.-T. Cui, W. Li, M. Yi, Z. K. Liu, M. Hashimoto, Y. Zhang, et al., Nature 515, 245 (2014).

[26] L. Rademaker, Y. Wang, T. Berlijn, and S. Johnston, New Journal of Physics 18, 022001 (2016), URL http://stacks.iop.org/1367-2630/18/i=2/a=022001.

[27] Y. Wang, K. Nakatsukasa, L. Rademaker, T. Berlijn, and S. Johnston, Superconductor Science and Technology 29, 054009 (2016), URL http://stacks.iop.org/0953-2048/29/i=5/a=054009.

[28] V. N. Smolyaninova, B. Yost, K. Zander, M. S. Osofsky, H. Kim, S. Saha, R. L. Greene, and I. I. Smolyaninov, Sci. Rep. 4, 7321 (2014), URL http://dx.doi.org/10.1038/srep07321.

[29] I. I. Smolyaninov and V. N. Smolyaninova, Phys. Rev. B 91, 094501 (2015), URL http://link.aps.org/doi/10.1103/PhysRevB.91.094501.

[30] T. Holstein, Ann. Phys. 8, 325 (1959).

[31] A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Rev. Mod. Phys. 68, 13 (1996).

[32] G. Kotliar and D. Vollhardt, Physics Today 57 (2004).

[33] T. Maier, M. Jarrell, T. Pruschke, and M. H. Hettler, Rev. Mod. Phys. 77, 1027 (2005).

[34] E. Gull, A. J. Millis, A. I. Lichtenstein, A. N. Rubtsov, M. Troyer, and P. Werner, Rev. Mod. Phys. 83, 349 (2011), URL http://link.aps.org/doi/10.1103/RevModPhys.83.349.

[35] J. K. Freericks, M. Jarrell, and D. J. Scalapino, Phys. Rev. B 48, 6302 (1993), URL http://link.aps.org/doi/10.1103/PhysRevB.48.6302.

[36] J. K. Freericks and M. Jarrell, Phys. Rev. B 50, 6939 (1994), URL http://link.aps.org/doi/10.1103/PhysRevB.50.6939.

[37] J. K. Freericks and M. Jarrell, Phys. Rev. Lett. 75, 2570 (1995), URL http://link.aps.org/doi/10.1103/PhysRevLett.75.2570.

[38] P. Benedetti and R. Zeyher, Phys. Rev. B 58, 14320 (1998), URL http://link.aps.org/doi/10.1103/PhysRevB.58.14320.

[39] A. Deppel and A. J. Millis, Phys. Rev. B 65, 224301 (2002), URL http://link.aps.org/doi/10.1103/PhysRevB.65.224301.

[40] G. Wellein and H. Fehske, Phys. Rev. B 56, 4513 (1997), URL http://link.aps.org/doi/10.1103/PhysRevB.56.4513.

[41] G. Kalosakas, S. Aubry, and G. P. Tsironis, Phys. Rev. B 58, 3094 (1998), URL http://link.aps.org/doi/10.1103/PhysRevB.58.3094.

[42] D. Meyer, A. C. Hewson, and R. Bulla, Phys. Rev. Lett. 89, 196401 (2002), URL http://link.aps.org/doi/10.1103/PhysRevLett.89.196401.

[43] P. Werner and A. J. Millis, Phys. Rev. Lett. 99, 146404 (2007), URL http://link.aps.org/doi/10.1103/PhysRevLett.99.146404.

[44] G. De Filippis, V. Cataudella, E. A. Nowadnick, T. P. Devereaux, A. S. Mishchenko, and N. Nagaosa, Phys. Rev. Lett. 109, 176402 (2012), URL http://link.aps.org/doi/10.1103/PhysRevLett.109.176402.

[45] Y. Murakami, P. Werner, N. Tsuji, and H. Aoki, Phys. Rev. B 91, 045128 (2015), URL http://link.aps.org/doi/10.1103/PhysRevB.91.045128.

[46] M. Vekić, R. M. Noack, and S. R. White, Phys. Rev. B 46, 271 (1992), URL http://link.aps.org/doi/10.1103/PhysRevB.46.271.

[47] S. Sykora, A. Hbsch, and K. W. Becker, EPL (Europhysics Letters) 85, 57003 (2009), URL http://stacks.iop.org/0295-5075/85/i=5/a=57003.

[48] J. P. Hague, Journal of Physics: Condensed Matter 17, 5663 (2005), URL http://stacks.iop.org/0953-8984/17/i=37/a=005.

[49] Y. Murakami, P. Werner, N. Tsuji, and H. Aoki, Phys. Rev. Lett. 113, 266404 (2014), URL http://link.aps.org/doi/10.1103/PhysRevLett.113.266404.

[50] G. Kotliar, S. Y. Savrasov, K. Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti, Rev. Mod. Phys. 78, 865 (2006).

[51] A. Liebsch and I. Ishida, Journal of Physics: Condensed Matter 24 (2012).

[52] C. Lin and A. A. Demkov, Phys. Rev. B 88, 035123 (2013), URL http://link.aps.org/doi/10.1103/PhysRevB.88.035123.

[53] D. Zgid, E. Gull, and G. K.-L. Chan, Phys. Rev. B 86, 165128 (2012).

[54] C. Lin and A. A. Demkov, Phys. Rev. B 90, 235122 (2014), URL http://link.aps.org/doi/10.1103/PhysRevB.90.235122.

[55] A. Go and A. J. Millis, Phys. Rev. Lett. 114, 016402 (2015), URL http://link.aps.org/doi/10.1103/PhysRevLett.114.016402.

[56] C. Lin and A. A. Demkov, Phys. Rev. B 92, 155135 (2015), URL http://link.aps.org/doi/10.1103/PhysRevB.92.155135.

[57] A. J. Millis, R. Mueller, and B. I. Shraiman, Phys. Rev. B 54, 5389 (1996), URL http://link.aps.org/doi/10.1103/PhysRevB.54.5389.

[58] S. Okamoto, A. Fuhrmann, A. Comanac, and A. J. Millis, Phys. Rev. B 71, 235113 (2005), URL http://link.aps.org/doi/10.1103/PhysRevB.71.235113.
 

[59] C. Lin and A. J. Millis, Phys. Rev. B 79, 205109 (2009), URL http://link.aps.org/doi/10.1103/PhysRevB.79.205109.

[60] G. D. Mahan, Many-Particle Physics 3rd edition (Kluwer Academic/Plenum publisher, New York, 2000).

[61] Due to the small number of bath orbitals, the zero DOS cannot be observed in the calculation.

[62] J. E. Hirsch and R. M. Fye, Phys. Rev. Lett. 56, 2521 (1986), URL http://link.aps.org/doi/10.1103/PhysRevLett.56.2521.

[63] A. S. Alexandrov, J. Ranninger, and S. Robaszkiewicz, Phys. Rev. B 33, 4526 (1986), URL http://link.aps.org/doi/10.1103/PhysRevB.33.4526.

[64] R. T. Scalettar, N. E. Bickers, and D. J. Scalapino, Phys. Rev. B 40, 197 (1989), URL http://link.aps.org/doi/10.1103/PhysRevB.40.197.
 
