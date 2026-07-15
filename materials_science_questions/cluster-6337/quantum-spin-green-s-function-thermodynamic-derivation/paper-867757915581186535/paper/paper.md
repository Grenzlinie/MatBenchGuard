
# Quantum phases in mixtures of fermionic atoms

C. Ates

Max-Planck-Institut für Physik Komplexer Systeme

D-01187 Dresden, Germany

K. Ziegler

Institut für Physik, Universität Augsburg

D-86135 Augsburg, Germany

(Dated: November 25, 2018)

## Abstract

A mixture of spin-polarized light and heavy fermionic atoms on a finite size 2D optical lattice is considered at various temperatures and values of the coupling between the two atomic species. In the case, where the heavy atoms are immobile in comparison to the light atoms, this system can be seen as a correlated binary alloy related to the Falicov-Kimball model. The heavy atoms represent a scattering environment for the light atoms. The distributions of the binary alloy are discussed in terms of strong- and weak-coupling expansions. We further present numerical results for the intermediate interaction regime and for the density of states of the light particles. The numerical approach is based on a combination of a Monte-Carlo simulation and an exact diagonalization method. We find that the scattering by the correlated heavy atoms can open a gap in the spectrum of the light atoms, either for strong interaction or small temperatures.
 

## INTRODUCTION

Recent experimental progress in preparing and measuring clouds of ultracold atoms in magnetic traps has opened a new way of studying bosonic and fermionic many-particle quantum states. Among them are condensed and Mott-insulating states of bosons in optical lattices (see e. g. [1], [2], [3], [4]). In comparison with similar studies in solid-state physics, atomic clouds enable us to design new many-particle systems by mixing different types of atoms [5], [6], [7]. These mixtures can form new quantum states due to the competition between the different types of atoms. In this paper we propose a mixture of light fermionic (e.g.  \( {}^{6} \) Li) atoms and heavy fermionic (e.g.  \( {}^{40} \) K) atoms, and study its low-temperature behavior in a (finite) optical lattice. We assume that the cloud of this mixture is prepared in a magnetic trap such that the atoms are spin polarized.

The difference of the masses of the two types of atoms implies two different and well-separated time scales for their tunneling processes through the optical lattice. The relatively fast tunneling processes of the light atoms sets the relevant scale for the dynamics of the mixture. In contrast, the relatively slow tunneling processes of the heavy atoms are dynamically irrelevant and lead only to statistical fluctuations which drive the system towards equilibrium. The latter will be discussed by the fact that the heavy particles form Ising-like (para-, ferro- and antiferromagnetic) states. They provide a scattering environment for the light atoms. Formally, this physical picture leads to the Falicov-Kimball model which has been used to describe complex solid-state systems  \( [8, 9, 10, 11, 12] \) . A numerical study of the two-dimensional Falicov-Kimball model, based on exact diagonalization, has revealed the possibility of a discontiguous transition between ordered and disordered phases  \( [10] \) . In the following we will use analytic methods as well as a combination of exact diagonalization and Monte-Carlo simulations to study large two-dimensional clusters for a better understanding of the underlying physics.

The paper is organized as follows: In Sect. 2 the model is briefly discussed, based on a functional-integral representation. A mapping to a binary-alloy model is described in Sect. 3. This gives the foundation for our analytic treatment, based on weak- and strong-coupling expansions, and for the construction of our numerical method. The numerical approach is used to evaluate the distribution of the heavy atoms and the density of states of the light atoms.
 

## THE MODEL

The atomic degrees of freedom are given in second quantization by local creation and annihilation operators. In the case of spin-polarized fermionic atoms we use  \( c_{r}^{\dagger} \)  ( \( c_{r} \) ) and  \( f_{r}^{\dagger} \)  ( \( f_{r} \) ) as the creation (annihilation) operators for the light and the heavy fermionic atoms, respectively, where r denotes the coordinates of the site in the optical lattice. The light atoms can tunnel with tunneling rate  \( \bar{t} \) , and we assume that the tunneling rate of the heavy atoms is so small that we can neglect it. Moreover, there is only a local interaction between the atoms in the optical lattice, i.e. only atoms in the same potential well notice each other. Since the atoms are spin-polarized fermions, there can be at most one atom per sort in each potential well, thanks to Pauli's principle. The interaction strength between light and heavy atoms is U. This allows us to write the many-particle Hamiltonian as

 \[ H=-\bar{t}\sum_{\langle r,r^{\prime}\rangle}c_{r}^{\dagger}c_{r^{\prime}}+\sum_{r}\left[-\mu(c_{r}^{\dagger}c_{r}+f_{r}^{\dagger}f_{r})+U f_{r}^{\dagger}f_{\tau}c_{r}^{\dagger}c_{\tau}\right], \quad (1) \] 

where  \( \langle r,r'\rangle \)  means pairs of nearest-neighbor lattice sites. We have assumed the same chemical potential  \( \mu \)  for both types of atoms. This may not be very general but will serve for the purpose of studying competing quantum phases in the atomic mixture. The model defined in Eq. (1) is also known as the spinless Falicov-Kimball model [8, 9, 10, 11, 12]. It is known to describe ordered phases and phase transitions for correlated electronic systems and was recently investigated intensively in the limit of infinite dimensions [9]. We will study this model in the following for a finite lattice, using a correlated binary-alloy (CBA) approach.

## Functional-Integral Representation

A grand-canonical ensemble of a mixture of light and heavy fermionic atoms at the inverse temperature  \( \beta = 1/k_{B}T \)  can be defined by the partition function

 \[ Z=\mathrm{T r e}^{-\beta H}, \] 

where Tr is the trace with respect to all many-particle states in the optical lattice. The Green’s function for the propagation of a light particle in the background formed by the heavy atoms in imaginary time t is

 \[ G(r,t;r^{\prime},0)=\frac{1}{Z}\mathrm{T r}\Big[e^{-(\beta-t)H}c_{r}e^{-t H}c_{r^{\prime}}^{\dagger}\Big]. \]
 

These expressions can also be written in terms of a functional integral on a Grassmann algebra [13]. For the latter the integration over a Grassmann field  \( \Psi_{\sigma}(r,t) \)  and its conjugate  \( \bar{\Psi}_{\sigma}(r,t) \)  ( \( \sigma = c, f \) ) is given as a linear mapping from a Grassmann algebra to the complex numbers. At a space-time point  \( (r,t) \)  we have for integers  \( k, l \geq 0 \) 

 \[ \int[\bar{\Psi}_{\sigma}(r,t)]^{k}[\Psi_{\sigma}(r,t)]^{\prime}d\Psi_{\sigma}(r,\tau)d\bar{\Psi}_{\sigma}(r,\tau)=\delta_{k,1}\delta_{l,1}. \] 

The partition function Z of the grand-canonical ensemble then reads

 \[ Z=\int\exp(-S)\mathcal{D}[\Psi_{f},\Psi_{c}] \quad (2) \] 

with the action

 \[ S=\sum_{r,t,\sigma}\bar{\Psi}_{\sigma}(r,t)[\Psi_{\sigma}(r,t)-\Psi_{\sigma}(r,\tau-\Delta)]+\Delta\sum_{t}H[\bar{\Psi}_{\sigma}(r,t),\Psi_{\sigma}(r,\tau-\Delta)] \quad (3) \] 

and the product measure

 \[ \mathcal{D}[\Psi_{f},\Psi_{c}]=\prod_{r,t,\sigma}d\Psi_{\sigma}(r,t)d\bar{\Psi}_{\sigma}(r,t). \] 

The Green’s function of light atoms is

 \[ G(r,t;r^{\prime},t^{\prime})=\langle\Psi_{c}(r,t)\bar{\Psi}_{c}(r^{\prime},t^{\prime})\rangle. \quad (4) \] 

The discrete time is used with  \( t = \Delta, 2\Delta, \ldots, \beta \) , implying that the limit  \( \Delta \rightarrow 0 \)  has to be taken in the end and  \( \beta' = \beta/\Delta \)  is the number of time steps.  \( \bar{\Psi}_{\sigma}(r,t) \)  and  \( \Psi_{\sigma}(r,t) $  are independent Grassmann fields which satisfy antiperiodic boundary conditions in time  \( \Psi_{\sigma}(r,\beta + \Delta) = -\Psi_{\sigma}(r, \Delta) \)  and  \( \bar{\Psi}_{\sigma}(r,\beta + \Delta) = -\bar{\Psi}_{\sigma}(\tau, \Delta) \) . For the subsequent calculations it is convenient to rename  \( \Psi_{\sigma}(r,t) \rightarrow \Psi_{\sigma}(t,\tau + \Delta) \)  because then the Grassmann field appears with the same time in the Hamiltonian of the action (3).

## THE CORRELATED BINARY ALLOY

The functional integration in Z and G can be performed in several steps, beginning with the integration of the heavy atomic field  \( \Psi_{f} \) , introducing the Ising spins and finally integrating the light atomic field  \( \Psi_{c} \)  [15]. The details of this procedure are described in Appendix A. As a result we obtain for the partition function

 \[ Z=\sum_{\{S(r)\}}Z(\{S_{r}\}) \]
 

with

 \[ Z(\{S_{r}\})=\bar{\mu}^{\beta^{\prime}}\sum_{r}(1+S(r))/2\det(-\partial_{t}+\bar{\mu}+\hat{t}-(U^{\prime}/2\bar{\mu})(1+S)). \quad (5) \] 

The parameters are  \( U' = \Delta U \) ,  \( \bar{\mu} = 1 + \Delta\mu \) , and  \( \hat{t} \)  is the tunneling term multiplied by  \( \Delta \) . Moreover,  \( \partial_{t} \)  is the time-shift operator. The Ising spin  \( S(r) \)  corresponds with a local occupation number  \( n_{f}(r) \)  of the heavy atoms as

 \[ n_{f}(r)=[1+S(r)]/2. \] 

The Green’s function is now an averaged resolvent

 \[ G=\langle(-\partial_{t}+\bar{\mu}+\hat{t}-(U^{\prime}/2\bar{\mu})(1+S))^{-1}\rangle_{\mathrm{I s i n g}}, \quad (6) \] 

where the average  \( \langle\ldots\rangle_{Ising} \)  is taken with respect to the distribution

 \[ P(\{S(r)\})=\frac{Z(\{S_{r}\})}{\sum_{\{S(r)\}}Z(\{S_{r}\})}. \quad (7) \] 

The partition function can also be written as

 \[ Z=\sum_{\{S(r)\}}\bar{\mu}^{\beta^{\prime}}\sum_{r}(1+S(r))/2\det[1+\{\bar{\mu}+\hat{t}-(U^{\prime}/2\bar{\mu})(1+S)\}^{\beta^{\prime}}]. \quad (8) \] 

The distribution is not  \( Z_{2} \)  invariant (i.e. invariant under a change  \( S(r) \to -S(r) \) ), except for a half-filled lattice (i.e.  \( \mu = U/2 \) ).

The representation of the Green’s function in Eq. (6) is our main analytic result. It means that the light particles tunnel through the optical lattice where they are scattered by the heavy particles. The distribution of the heavy particles is given by the distribution shown in Eq. (7). The latter depends on the temperature but also on the parameters of the light particles like  \( \bar{t} \)  and the coupling U between the light and the heavy particles. This reflects the intimate relationship between the two types of particles. In other words, the light particles move in a random potential formed by the heavy particles. This randomness, formally expressed by the Ising spins, is correlated and can be called correlated binary alloy (CBA). There is a correlation length which diverges at the phase transitions of the Ising system. In the subsequent investigation we will study these phases and their implications for the properties of the light particles.

The symmetric matrix  \( \bar{\mu}-\hat{t}+(U^{\prime}/2\bar{\mu})(1+S) \)  can be diagonalized with eigenvalues  \( 1-\Delta\lambda_{j} \) . Then the determinant in Eq. (8) is for  \( \Delta\sim0 \) 

 \[ \det[1+\{\bar{\mu}+\hat{t}-(U^{\prime}/2\bar{\mu})(1+S)\}^{\beta^{\prime}}]\sim\prod_{j}(1+e^{-\beta\lambda_{j}}). \]
 

Since the matrix depends on the fluctuating Ising spins, it is difficult to determine the eigenvalues. One way to get an idea about the physics of this model is to study the asymptotic regimes of strong and weak coupling, another one is to use a numerical diagonalization procedure. Both approaches shall be applied subsequently.

## Approximations of the CBA Distribution

The distribution was studied in the case of strong coupling (i.e. the tunneling (or  \( U^{-1} \) ) expansion) in a number of papers [14, 15]. It leads at half-filling to an Ising model with  \( Z_{2} \)  symmetry. In the following we study the CBA distribution in weak and strong-coupling approximations as well as numerically by a Monte-Carlo simulation. The density of states of the light atoms are evaluated by a numerical procedure.

## System without Tunneling

The absence of the  \( Z_{2} \) -symmetry can be observed already in the absence of tunneling. Then we have in the limit  \( \Delta \rightarrow 0 \) 

 \[ P_{0}(\{S(r)\})=\prod_{r}\frac{e^{\beta\mu(1+S(r))/2}+e^{\beta[\mu+(\mu-U)(1+S(r))/2]}}{1+2e^{\beta\mu}+e^{\beta(2\mu-U)}} \] 

which is  \( Z_{2} \)  invariant only for  \( \mu = U/2 \) . The average spin is shown in Fig. 1 and its asymptotic low-temperature behavior is

 \[ \langle S\rangle=\frac{e^{\beta(2\mu-U)}-1}{1+2e^{\beta\mu}+e^{\beta(2\mu-U)}}\sim\left\{\begin{aligned}&-1&\mu<0\\ &0&0\leq\mu<U\\ &1/3&\mu=U\\ &1&U<\mu\end{aligned}\right.. \] 

Thus only for  \( 0 < \mu < U \)  the Ising state is paramagnetic. The other regimes are ferromagnetic. In terms of the configurations of the heavy atoms there are no heavy atoms for  \( \mu < 0 \)  and a heavy atom at each site for  \( \mu > U \) . In the intermediate regime  \( 0 < \mu < U \)  we anticipate that the coupling of neighboring Ising spins, caused by a non-zero tunneling rate  \( \bar{t} \) , will lead to ordered Ising spins at low temperatures.
 
![](./images/867757915581186535_1.jpg)

FIG. 1: Average spin for a system without tunneling: U = 1 and  \( \beta = 10 \) .

## Tunneling Expansion

The effect of a weak tunneling rate can be evaluated in terms of a perturbation theory with respect to  \( \bar{t} \) . Moreover, we take the limit  \( \Delta \rightarrow 0 \)  and consider the asymptotic regime of low temperatures (i.e.  \( \beta \sim \infty \) ). If we include tunneling terms up to order  \( O(\bar{t}^{2}) \)  we get for  \( \mu = U/2 \)  the Ising model with nearest-neighbor spin interaction:

 \[ P_{s}(\{S(r)\})=\frac{\exp\left[-\beta\frac{\bar{t}^{2}}{2U}\sum_{\langle r,r^{\prime}\rangle}S(r)S(r^{\prime})+o(\bar{t}^{3})\right]}{\sum_{\{S(r)=\pm1\}}\exp\left[-\beta\frac{\bar{t}^{2}}{2U}\sum_{\langle r,r^{\prime}\rangle}S(r)S(r^{\prime})+o(\bar{t}^{3})\right]}. \quad (9) \] 

This model has an antiferromagnetic low-temperature phase.

The spin-spin coupling is exponentially small in  \( \beta \)  for  \( \mu < 0 \)  and  \( \mu > U \)  but of order  \( \bar{t}^{2}/U \)  for  \( 0 < \mu < U \) . In particular, we can distinguish three different regimes:

 \[ \mu<0:\quad P_{s}(\{S\})\propto\exp\Big[-\beta\frac{|\mu|}{2}\sum_{r}S(r)+o(\bar{t}^{3})\Big], \] 

 \[ 0<\mu<U:\ P_{s}(\{S\})\propto\exp\Big[\frac{\beta^{2}\bar{t}^{2}}{8}e^{-\beta U/2}\sinh[\beta(\mu-U/2)]\sum_{r}S(r)-\beta\frac{\bar{t}^{2}}{4U}\sum_{<r,r^{\prime}>}S(r)S(r^{\prime})+o(\bar{t}^{3})\Big] \] 

and

 \[ U<\mu:\quad P_{s}(\{S\})\propto\exp\Big[\beta\frac{\mu-U}{2}\sum_{r}S(r)+o(\bar{t}^{3})\Big]. \] 

Besides the two ferromagnetic regimes for  \( \mu < 0 \)  and  \( \mu > U \)  we have the intermediate regime  \( 0 < \mu < U \)  with antiferromagnetic ordering. There is an exponentially small magnetic field
 

for  \( \mu \neq U/2 \)  which breaks the  \( Z_{2} \)  symmetry. As we approach  \( \mu = 0 \)  or  \( \mu = U \)  the magnetic field becomes larger. There is a first order transition from the antiferro- to a ferromagnetic phase when the magnetic field starts to dominate the spin-spin interaction. This can be seen in a simple mean-field approximation.

## The Weak-coupling Limit

In the case of weak coupling we can perform an expansion in terms of the coupling parameter U. This gives in leading order an uncorrelated binary alloy:

 \[ P_{w}(\{S(r)\})=\prod_{r}\frac{e^{\beta(\mu-U g)S(r)/2}}{\sum_{S(r)=\pm1}e^{\beta(\mu-U g)S(r)/2}}, \] 

where  \( \epsilon(k) \)  is the dispersion of the tunneling term and

 \[ g(\mu)=\int\Theta(\epsilon(k)+\mu)\frac{d^{d}k}{(2\pi)^{d}}, \] 

i.e.  \( 0 \leq g \leq 1 \) . Thus the Ising groundstate for weak coupling is ferromagnetic. In particular,

 \[ \langle S\rangle=\tanh(\beta(\mu-U g(\mu))/2). \] 

## The Density of States

The density of states (DOS) for the light particles can be obtained from the diagonal elements of the Green’s function in Eq. (6). Its qualitative behavior depends strongly on the state of the heavy particles: In the case of a ferromagnetic state the DOS shows a single band, for the antiferromagnetic state it has a gap. For a paramagnetic state of the heavy particles the form of the DOS is less obvious. We have calculated the DOS numerically for a  \( 18 \times 18 \)  square lattice with open boundaries. For this purpose we have generated configurations of the Ising spins according to the distribution function in Eq. (7), using the Metropolis algorithm. Typical configurations with large statistical weight are shown in Figs. 2 - 5 for different values of the physical parameters U,  \( \mu \) , and  \( \beta \) .

For a given configuration  \( \{S(r)\} \)  of Ising spins the Hamiltonian

 \[ h=\hat{t}-\frac{U}{2}S \]
 
![](./images/867757915581186535_2.jpg)

FIG. 2: Paramagnetic Ising-spin configuration for  \( \bar{t}=1 \) , U=3,  \( \mu=U/2 \) , and  \( \beta=3 \) . White (black) squares refer to sites (un)occupied with a heavy atom.

![](./images/867757915581186535_3.jpg)

FIG. 3: Mixture of para- and antiferromagnetic Ising-spin textures for  \( \bar{t}=1 \) , U=3,  \( \mu=U/2 \) , and  \( \beta=7 \) 

is diagonalized. From the eigenvalues  \( \lambda_{k}(\{S(r)\}) \)  the DOS of h is calculated as

 \[ D(E,\{S(r)\})=\frac{1}{N\pi}\sum_{k=1}^{N}\delta\left(E-\lambda_{k}(\{S(r)\})\right)\quad, \quad (10) \] 

where N is the number of lattice sites. Finally, the DOS related to the Green’s function in Eq. (6) is determined by averaging over L = 100 spin configurations:

 \[ D(E)=\frac{1}{L}\sum_{\{S(r)\}}D(E,\{S(r)\})\quad. \quad (11) \]
 
![](./images/867757915581186535_4.jpg)

FIG. 4: Antiferromagnetic Ising-spin configuration for  \( \bar{t}=1 \) , U=3,  \( \mu=U/2 \) , and  \( \beta=14 \) 

![](./images/867757915581186535_5.jpg)

FIG. 5: Ferromagnetic Ising-spin configuration for  \( \bar{t}=1 \) , U=8,  \( \mu=0.8U \) , and  \( \beta=14 \) 

In the following the hopping rate is set to  \( \bar{t}=1 \) .

Fig. 6 shows the DOS of the light particles for U = 3 and half filling (i. e.  \( \mu = U/2 \) ) at different temperatures. For small  \( \beta \) , i. e. high temperatures, the system shows a gapless metallic band, which is symmetric around the Fermi level, and the Ising spins form a paramagnetic state. The DOS is slightly suppressed at the band center due to the interaction between the light and the heavy atoms. When the temperature is decreased, the Ising spins start to order antiferromagnetically, i. e. the heavy atoms create a chessboard-like phase with empty sites. This is accompanied by the formation of a gap around the Fermi level and a strong enhancement of the DOS at the inner band edges. Very similar results were
 
![](./images/867757915581186535_6.jpg)

![](./images/867757915581186535_7.jpg)

![](./images/867757915581186535_8.jpg)

![](./images/867757915581186535_9.jpg)

FIG. 6: DOS for U = 3,  \( \mu = U/2 \)  (half filling) and different temperatures. First row:  \( \beta = 3 \) ,  \( \beta = \)  7. Second row:  \( \beta = 10 \) ,  \( \beta = \)  14.

found in a dynamical cluster approximation on an  \( 8 \times 8 \)  cluster [16].

The high-temperature regime of the system at half filling is depicted in Fig. 7 for various interaction strengths U. For small interaction the DOS shows a metallic band and is peaked around the Fermi level. For increasing U this peak gets suppressed and a band splitting to two symmetric bands occurs. The spectral weight within these subbands is highest at their center. A further increase of U leads to a shift of the lower and upper band to lower and higher energies, respectively.

Figure 8 shows the DOS in the low-temperature regime for two values of the interaction strength  \( (U = 3 \) , solid and U = 8, dashed) and different values of the chemical potential. For the latter the distribution (7) has no  \( Z_{2} \)  symmetry, i.e. is not invariant under a global spin flip  \( S \rightarrow -S \) . Near half filling the heavy atoms order in a chessboard configuration. This behavior is stabilized for larger deviations from  \( \mu = U/2 \)  when the interaction strength is increased. As  \( \mu \)  deviates even further from U/2 the Ising spins start to order ferromagnetically. The spectral weight locally shifts to the center of each subband and globally shifts from the lower to the upper band. For the completely ordered Ising spins the lower band disappears and the system has only one band.
 
![](./images/867757915581186535_10.jpg)

![](./images/867757915581186535_11.jpg)

![](./images/867757915581186535_12.jpg)

![](./images/867757915581186535_13.jpg)

FIG. 7: DOS for  \( \beta = 3 \)  at various values of the interaction U and half-filling ( \( \mu = U/2 \) ). First row: U = 1, U = 4, . Second row: U = 6, U = 8.

## CONCLUSIONS

A mixture of light and heavy fermionic atoms is studied as a system in which the light atoms live in a correlated disordered environment. This environment is formed by the heavy atoms. The disorder is given by fluctuating Ising spins with a complex temperature-dependent distribution. This distribution is  \( Z_{2} \)  (spin-flip) invariant only at half filling (i.e.  \( \mu = U/2 \) ) but has a broken spin-flip symmetry for  \( \mu \neq U/2 \) . This symmetry breaking favors an Ising spin  \( S_{r} = -1 \)  at low density (i.e.  \( \mu < 0 \) ) and  \( S_{r} = 1 \)  at high density (i.e.  \( \mu > U \) ). There is an intermediate regime where an antiferromagentic (staggered) Ising-spin configuration is favored. Scattering on these configurations opens a gap in the band of the light atoms.

Acknowledgement:

This work was supported by the Sonderforschungsbereich 484.

[1] D. Jaksch et al., Phys. Rev. Lett. 81, 3108 (1998)
 
![](./images/867757915581186535_14.jpg)

![](./images/867757915581186535_15.jpg)

![](./images/867757915581186535_16.jpg)

![](./images/867757915581186535_17.jpg)

FIG. 8: DOS for  \( \beta = 14 \) , U = 3 (solid), U = 8 (dashed) and different values of the chemical potential. First row:  \( \mu = 0.6U \) ,  \( \mu = -0.7U \) . Second row:  \( \mu = 0.8U \) ,  \( \mu = -0.9U \) .

[2] M. Greiner et al., Nature (London) 415, 39 (2002)

[3] T. Stöferle et al, Phys. Rev. Lett. 92, 130403 (2004)

[4] B. Paredes et al., Nature (London) 429, 277 (2004)

[5] B. DeMarco and D. S. Jin, Science 285, 1703 (1999)

[6] W. Ketterle, D.S. Durfee, and D.M. Stamper-Kurn, in Bose-Einstein condensation in atomic gases, Proceedings of the International School of Physics Enrico Fermi, Course CXL edited by M. Inguscio, S. Stringari and C.E. Wieman (IOS Press, Amsterdam 1999), pp. 67-176

[7] S. Jochim et al., Science 302, 2101 (2003)

[8] L.M. Falicov and J.C. Kimball, Phys. Rev. Lett. 22, 997 (1969)

[9] J.K. Freericks and V. Zlatić, Rev. Mod. Phys. 75, 1333 (2003)

[10] P. Farkasovsky, Z.Phys. B 102, 91 (1997)

[11] Fradkin, E., 1991, Field Theories of Condensed Matter Systems (Addison - Wesley: Redwood City).

[12] Gebhard, F., 1997, The Mott Metal-Insulator Transition (Springer-Verlag: Berlin).

[13] Negele, J.W. and Orland, H., 1988, Quantum Many - Particle Systems (Addison - Wesley: New York).
 

[14] Ch. Gruber, N. Macris, A. Messager, and D. Ueltschi, J. Stat. Phys. 86, 57 (1997)

[15] K. Ziegler, Phil. Mag. B 82 7, 839-853 (2002)

[16] M.H. Hettler et al., Phys. Rev . B 61, 12739 (2000)

## A. Appendix

## A.1. Integration of the Heavy Atoms

It is possible to integrate out the field  \( \Psi_{f} \)  of the heavy atoms in Eqs. (2) and (4), since it appears in S only as a quadratic form:

 \[ S=S_{c}+S_{f}+S_{I} \] 

with

 \[ S_{c}=\sum_{t}\Big\{\sum_{r}[\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t+\Delta)-\bar{\mu}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t)]-\tau\sum_{\langle r,r^{\prime}\rangle}\bar{\Psi}_{c}(r,t)\Psi_{c}(r^{\prime},t)\Big\} \] 

 \[ S_{f}=\sum_{t}\Big\{\sum_{r}[\bar{\Psi}_{f}(r,t)\Psi_{f}(r,t+\Delta)-\bar{\mu}\bar{\Psi}_{f}(r,t)\Psi_{f}(r,t)]\Big\}. \] 

The interaction between the two types of atoms is given by

 \[ S_{I}=U^{\prime}\sum_{r,t}\bar{\Psi}_{f}(r,t)\Psi_{f}(r,t)\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t). \] 

The integration over the Grassmann field  \( \Psi_{f} \)  in Z gives a space-diagonal determinant

 \[ \int e^{-S_{f}-S_{I}}\prod_{r,t}d\Psi_{f}(r,t)d\bar{\Psi}_{f}(r,t)=\det(-\partial_{t}+\bar{\mu}-U^{\prime}\bar{\Psi}_{c}\Psi_{c}), \quad (12) \] 

where  \( \partial_{t} \)  is the time-shift operator

 \[ \partial_{t}\Psi(r,t)=\left\{\begin{aligned}&\Psi(r,t+\Delta)&\Delta\leq t<\beta\\ &-\Psi(r,\Delta)&\quad t=\beta\end{aligned}\right.. \] 

The second equation is a consequence of the antiperiodic boundary condition of the Grassmann field.

## A.2. Expansion with Ising Spins

The partition function is now a functional integral of the c-Grassmann field

 \[ Z=\int e^{-S_{c}}\mathrm{d e t}(-\partial_{t}+\bar{\mu}-U^{\prime}\bar{\Psi}_{c}\Psi_{c})\mathcal{D}[\Psi_{c}]=\int e^{-S_{c}}\prod_{r}\Big[1+\prod_{t}(\bar{\mu}-U^{\prime}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t))\Big]\mathcal{D}[\Psi_{c}]. \]
 

The product can be expanded in terms of Ising spins  \( \{S(r)=\pm1\} \)  [15] as

 \[ \prod_{r}\left[1+\prod_{t}(\bar{\mu}-U^{\prime}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t))\right]=\sum_{\{S(r)=\pm1\}}\prod_{r}\prod_{t}[\bar{\mu}-U^{\prime}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t)]^{\frac{1+S(r)}{2}}. \] 

This reads with  \( I = \frac{1+S}{2} \)  as

 \[ =\sum_{\{S(r)=\pm1\}}\prod_{r}\bar{\mu}^{\beta^{\prime}\mathbf{I}(r)}e^{-(U^{\prime}/\bar{\mu})\mathbf{I}(r)\sum_{t}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t)}. \] 

Now the partition function Z can be expressed by a summation over configurations of Ising spins as

 \[ Z=\sum_{\{S(r)=\pm1\}}Z(\{S(r)\}) \] 

with

 \[ Z(\{S(r)\})=\int e^{-S c}\prod_{r}\bar{\mu}^{\beta^{\prime}\mathbf{I}(r)}e^{-(U^{\prime}/\bar{\mu})\mathbf{I}(r)\sum_{t}\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t)}\mathcal{D}[\Psi_{c}]. \quad (13) \] 

## A.3. Integration of the Light Atoms

The c-Grassmann field appears only in a quadratic form in the partition function:

 \[ S_{c}^{\prime}=S_{c}+\frac{U^{\prime}}{\bar{\mu}}\sum_{r,t}\mathbf{I}(r)\bar{\Psi}_{c}(r,t)\Psi_{c}(r,t)\equiv\bar{\Psi}_{c}\cdot(\partial_{t}-\bar{\mu}-\hat{t}+\frac{U^{\prime}}{\bar{\mu}}\mathbf{I})\Psi_{c}. \] 

After performing the  \( \Psi_{c} \) -integration we obtain

 \[ Z(\{S_{r}\})=\bar{\mu}^{\beta^{\prime}\sum_{r}\mathbf{I}(r)}\mathrm{d e t}(-\partial_{t}+\bar{\mu}+\hat{t}-\frac{U^{\prime}}{\bar{\mu}}\mathbf{I}). \] 

Following the same procedure for the Green’s function, we obtain for G in Eq. (4) the matrix

 \[ G=\frac{\sum_{\{S(r)\}}(-\partial_{t}+\bar{\mu}+\hat{t}-(U^{\prime}/\bar{\mu})\mathbf{I})^{-1}\bar{\mu}^{\beta^{\prime}}\sum_{r}\mathbf{I}(r)\mathrm{d e t}(-\partial_{t}+\bar{\mu}+\hat{t}-\frac{U^{\prime}}{\bar{\mu}}\mathbf{I})}{\sum_{\{S(r)\}}\bar{\mu}^{\beta^{\prime}}\sum_{r}\mathbf{I}(r)\mathrm{d e t}(-\partial_{t}+\bar{\mu}+\hat{t}-\frac{U^{\prime}}{\bar{\mu}}\mathbf{I})}. \]
 
