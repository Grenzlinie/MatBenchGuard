
# Correlation Effects in Stochastic Ferromagnetic Systems

Thomas Bose and Steffen Trimper

Institute of Physics, Martin-Luther-University, D-06099 Halle, Germany \( ^{*} \) 

(Dated: June 16, 2018)

## Abstract

We analyze the Landau-Lifshitz-Gilbert equation when the precession motion of the magnetic moments is additionally subjected to an uniaxial anisotropy and is driven by a multiplicative coupled stochastic field with a finite correlation time  \( \tau \) . The mean value for the spin wave components offers that the spin-wave dispersion relation and its damping is strongly influenced by the deterministic Gilbert damping parameter  \( \alpha \) , the strength of the stochastic forces D and its temporal range  \( \tau \) . The spin-spin-correlation function can be calculated in the low correlation time limit by deriving an evolution equation for the joint probability function. The stability analysis enables us to find the phase diagram within the  \( \alpha - D \)  plane for different values of  \( \tau \)  where damped spin wave solutions are stable. Even for zero deterministic Gilbert damping the magnons offer a finite lifetime. We detect a parameter range where the deterministic and the stochastic damping mechanism are able to compensate each other leading to undamped spin-waves. The onset is characterized by a critical value of the correlation time. An enhancement of  \( \tau \)  leads to an increase of the oscillations of the correlation function.

PACS numbers: 75.10.Hk, 05.40.-a, 75.30.Ds, 72.70.+m, 76.60.Es
 

## I. INTRODUCTION

Magnetism can be generally characterized and analyzed on different length and time scales. The description of fluctuations of the magnetization, the occurrence of damped spin waves and the influence of additional stochastic forces are successfully performed on a mesoscopic scale where the spin variables are represented by a continuous spatio-temporal variable [1]. In this case a well established approach is based upon the Landau-Lifshitz equation [2] which describes the precession motion of the magnetization in an effective magnetic field. This field consists of a superposition of an external field and internal fields, produced by the interacting magnetic moments. The latter one is strongly influenced by the isotropic exchange interaction and the magnetocrystalline anisotropy, for a recent review see [3]. The studies using this frame are concentrated on different dynamical aspects as the switching behavior of magnetic nanoparticles which can be controlled by external time-dependent magnetic fields [4] and spin-polarized electric currents [5, 6]. Such a current-induced spin transfer allows the manipulation of magnetic nanodevices. Recently, it has been demonstrated that an electric current, flowing through a magnetic bilayer, can induce a coupling between the layers [7]. Likewise, such a current can also cause the motion of magnetic domain walls in a nanowire [8]. Another aspect is the dynamical response of ferromagnetic nanoparticles as probed by ferromagnetic resonance, studied in [9]. In describing all this more complex behavior of magnetic systems, the Landau-Lifshitz equation has to be extended by the inclusion of dissipative processes. A damping term is introduced phenomenologically in such a manner, that the magnitude of the magnetization  \( \vec{S} \)  is preserved at any time. Furthermore, the magnetization should align with the effective field in the long time limit. A realization is given by [2]

 \[ \frac{\partial\mathbf{S}}{\partial t}=-\gamma[\mathbf{S}\times\mathbf{B}_{\mathrm{e f f}}]-\varepsilon\left[\mathbf{S}\times(\mathbf{S}\times\mathbf{B}_{\mathrm{e f f}})\right]. \quad (1) \] 

The quantities  \( \gamma \)  and  \( \varepsilon \)  are the gyromagnetic ratio and the damping parameter, respectively. An alternative equation for the magnetization dynamics had been proposed by Gilbert [10]. The Gilbert equation yields an implicit form of the evolution of the magnetization. A combination of both equations, called Landau-Lifshitz-Gilbert equation (LLG) will be used as the basic relation for our studies, see Eq. (2). The origin of the damping term as a non-relativistic expansion of the Dirac equation has been discussed in [11] and a generalization of the LLG for conducting ferromagnetics is offered in [12]. The form of the damping seems
 

to be quite general as it has been demonstrated in  \( [13] \)  using symmetry arguments for ferroelectric systems.

As a new aspect let us focus on the influence of stochastic fields. The interplay between current and magnetic fluctuations and dissipation has been studied recently in  \( [14] \) . Via the spin-transfer torque, spin-current noise causes a significant enhancement of the magnetization fluctuations. Such a spin polarized current may transfer momentum to a magnet which leads to a spin-torque phenomenon. The shot noise associated with the current gives rise to a stochastic force  \( [15] \) . In our paper we discuss the interplay between different dissipation mechanisms, namely the inherent deterministic damping in Eq. (1) and the stochastic magnetic field originated for instance by defect configurations giving rise to a different coupling strength between the magnetic moments. Assuming further, that the stochastic magnetic field is characterized by a finite correlation time, the system offers memory effects which might lead to a decoherent spin precession. To that aim we analyze a ferromagnet in the classical limit, i.e., the magnetic order is referred to single magnetic atoms which occupy equivalent crystal positions, and the mean values of their spins exhibit a parallel orientation. The last one is caused by the isotropic exchange interaction which will be here supplemented by a magneto-crystalline anisotropy that defines the direction of the preferred orientation. Especially, we discuss the influence of an uniaxial anisotropy. The coupling between different dissipation mechanisms, mentioned above, leads to pronounced correlations, which are discussed below. Due to the multiplicative coupling of the stochastic field and the finite correlation time the calculation of the spin-spin correlation function is more complicated. To that aim we have to derive an equivalent evolution equation for the joint probability distribution function. Within the small correlation time limit this approach can be fulfilled in an analytical manner. Our analysis is related to a recent paper  \( [16] \)  in which likewise the stochastic dynamics of the magnetization in ferromagnetic nanoparticles has been studied. Further, we refer also to a recent paper  \( [17] \)  where the mean first passage time and the relaxation of magnetic moments has been analyzed. Different to those papers our approach is concentrated on the correlation effects in stochastic system with colored noise.

Our paper is organized as follows: In Sec.II we discuss the LLG and characterize the additional stochastic field. The equations for the single and the two particle joint probability distribution are derived in Sec.III. Using these functions we obtain the mean value of the spin wave variable and the spin-spin correlation function. The phase diagram, based on the
 

stability analysis, is presented in Sec.IV. In Sec.V we finish with some conclusions.

## II. MODEL

In order to develop a stochastic model for the spin dynamics in ferromagnetic systems let us first consider the deterministic part of the equation of motion. We focus on a description based upon the level of Landau-Lifshitz phenomenology [2], for a recent review see [3]. To follow this line we consider a high spin systems in a ferromagnet sufficiently below the Curie temperature. In that regime the dynamics of the magnet are dominated by transverse fluctuations of the spatio-temporal varying local magnetization. The weak excitations, called spin waves or magnons, are determined by a dispersion relation, the wavelength of which should be large compared to the lattice constant a, i.e., the relation  \( q \cdot a \ll 1 \)  is presumed to be satisfied, where q is the wavenumber. In this limit the direction of the spin varies slowly while its magnitude  \( |S| = m_{s} \)  remains constant in time. A proper description for such a situation is achieved by applying the Landau-Lifshitz-Gilbert equation (LLG) [4, 10, 18]. The spin variable is represented by  \( S = m_{s} \hat{n} \) , where  \( \hat{n}(\mathbf{r}, t) \)  is a continuous variable which characterizes the local orientation of the magnetic moment. The evolution equation for that local orientation reads

 \[ \frac{\partial\hat{\mathbf{n}}}{\partial t}=-\frac{\gamma}{1+\alpha^{2}}\hat{\mathbf{n}}\times\left[\mathbf{B}_{\mathrm{e f f}}+\alpha\left[\hat{\mathbf{n}}\times\mathbf{B}_{\mathrm{e f f}}\right]\right]. \quad (2) \] 

The quantities  \( \gamma \)  and  \( \alpha \)  are the gyromagnetic ratio and the dimensionless Gilbert damping parameter, respectively, where  \( \alpha \)  is related to  \( \varepsilon \)  introduced in Eq. (1).  \( B_{eff} \)  is the effective magnetic field that drives the motion of the spin density. Generally, it consists of an internal part originated by the interaction of the spins and an external field. This effective field is related to the Hamiltonian of the system by functional variation with respect to  \( \hat{n} \) 

 \[ \mathbf{B}_{\mathrm{e f f}}=-m_{s}^{-1}\frac{\delta\mathcal{H}}{\delta\hat{\mathbf{n}}}. \quad (3) \] 

In absence of an external field the Hamiltonian can be expressed as [19, 20]

 \[ \begin{aligned}\mathcal{H}&=\int d^{3}\mathbf{r}\left\{w_{ex}+w_{an}\right\},\quad with\\w_{ex}&=\frac{1}{2}m_{s}\kappa\left(\nabla\hat{\mathbf{n}}\right)^{2}\quad and\quad w_{an}=\frac{1}{2}m_{s}\Gamma\sin^{2}\theta.\end{aligned} \quad (4) \] 

Thereby, the constants  \( \kappa \)  and  \( \Gamma \)  denote the exchange energy density and the magneto-crystalline anisotropy energy density. To be more precise,  \( \kappa \propto Ja^{2} \) , J being the coupling
 

strength that measures the interaction between nearest neighbors in the isotropic Heisenberg model [21]. Once again a is the lattice constant. Notice that the form of the exchange energy in the Hamiltonian (4) arises from the Heisenberg model in the classical limit. The quantity  \( \theta \)  represents the angle between  \( \hat{n} \)  and the anisotropy axis  \( \hat{\nu} = (0, 0, 1) \) , where  \( \hat{\nu} \)  points in the direction of the easy axis in the ground state in the case of zero applied external field. Thus, the constant  \( \Gamma > 0 \)  characterizes anisotropy as a consequence of relativistic interactions (spin-orbital and dipole-dipole ones [20]). In deriving Eq. (4) we have used  \( \hat{n}^{2} = 1 \) . Although it is more conventional to introduce the angular coordinates  \( (\theta, \Phi) \)  [2, 4], we find it more appropriate to use Cartesian coordinates. To proceed, we divide the vector  \( \hat{n} \)  into a static and a dynamic part designated by  \( \mu \)  and  \( \varphi \) , respectively. In the linearized spin wave approach let us make the ansatz

 \[ \hat{\mathbf{n}}(\mathbf{r},t)=\boldsymbol{\mu}(\mathbf{r})+\boldsymbol{\varphi}(\mathbf{r},t)=\mu\hat{\boldsymbol{\nu}}+\boldsymbol{\varphi},\quad\mu=\mathrm{c o n s t.}, \quad (5) \] 

where  \( \hat{n}^{2}=1 \)  is still valid. The effective field can now be obtained from Eqs. (3) and (4). This yields

 \[ \mathbf{B}_{\mathrm{e f f}}=\kappa\nabla^{2}\boldsymbol{\varphi}-\Gamma\boldsymbol{\varphi}^{\prime};\qquad\boldsymbol{\varphi}^{\prime}=(\varphi_{1},\varphi_{2},0). \quad (6) \] 

Eq. (2) together with Eqs. (3) and (4) represent the deterministic model for a classical ferromagnet. In order to extend the model let us supplement the effective magnetic field in Eq. (6) by a stochastic component yielding an effective random field  \( B_{eff} = B_{eff} + \eta(t) \) . The stochastic process  \( \eta(t) \)  is assumed to be Gaussian distributed with zero mean and obeying a colored correlation function

 \[ \tilde{\chi}_{i j}(t,t^{\prime})=\langle\eta_{i}(t)\eta_{j}(t^{\prime})\rangle=\frac{\tilde{D}_{i j}}{\tilde{\tau}_{i j}}\exp\left[-\frac{|t-t^{\prime}|}{\tilde{\tau}_{i j}}\right]. \quad (7) \] 

Here,  \( \tilde{D}_{ij} \)  and  \( \tilde{\tau}_{ij} \)  are the noise strength and the finite correlation time of the noise  \( \eta \) . Due to the coupling of the effective field to the spin orientation  \( \hat{n} \)  the stochastic process is a multiplicative one. Microscopically, such a random process might be originated by a fluctuating coupling strength for instance. The situation associated with our model is illustrated in Fig. 1 and can be understood as follows: The stochastic vector field  \( \eta(t) \)  is able to change the orientation of the localized moment at different times. Therefore, fixed phase relations between adjacent spins might be destroyed. Moreover, the  \( \eta(t_{k}) \)  are interrelated due to the finite correlation time  \( \tau \) . The anisotropy axis defines the preferred orientation of the mean value of magnetization. Due to the inclusion of  \( \eta(t) \)  the deterministic Eq. (2) is
 
![](./images/867757382543868675_1.jpg)

FIG. 1. Part of a ferromagnetic domain influenced by stochastic forces for the example of cubic symmetry with lattice constant a. The black spin in the center only interacts with its nearest neighbors (green), where J is a measure for the exchange integral.

transformed into the stochastic LLG. Using Eq. (5) it follows

 \[ \frac{\partial\varphi}{\partial t}=-\frac{\gamma}{1+\alpha^{2}}\left(\boldsymbol{\mu}+\boldsymbol{\varphi}\right)\times\left[\mathbf{B}_{\mathrm{e f f}}+\alpha\left[\left(\boldsymbol{\mu}+\boldsymbol{\varphi}\right)\times\mathbf{B}_{\mathrm{e f f}}\right]\right]. \quad (8) \] 

The random magnetic field is defined by

 \[ \mathbf{B}_{\mathrm{e f f}}=\kappa\nabla^{2}\boldsymbol{\varphi}-\Gamma\boldsymbol{\varphi}^{\prime}+\boldsymbol{\eta}(t), \quad (9) \] 

where  \( \varphi^{\prime} \)  is given in Eq. (6). With regard to the following procedure we suppose the random field to be solely generated dynamically, i.e.,  \( \hat{\mathbf{n}} \times \boldsymbol{\eta}(t) = \boldsymbol{\varphi} \times \boldsymbol{\boldsymbol{\eta}}(t) \) . So far, the dynamics of our model (Eqs. (8) and (9)) are reflected by a nonlinear, stochastic partial differential equation (PDE). Using Fourier transformation, i.e.,  \( \boldsymbol{\psi}(\mathbf{q}, t) = \mathcal{F}\{\boldsymbol{\varphi}(\mathbf{r}, t)\} \)  and introducing the following dimensionless quantities

 \[ \beta=\left(l_{0}q\right)^{2}+1\quad,\quad l_{0}^{2}=\frac{\kappa}{\Gamma}\quad,\quad\omega=\gamma\Gamma\quad,\quad\bar{t}=\omega t\quad,\quad\boldsymbol{\lambda}(t)=\frac{\boldsymbol{\eta}(t)}{\Gamma}, \quad (10) \] 

the components  \( \psi_{i}(\mathbf{q}, t) \)  fulfill the equation

 \[ \frac{d}{d t}\psi_{i}(\mathbf{q},t)=\Omega_{i}(\boldsymbol{\psi}(\mathbf{q},t))+\Lambda_{i j}(\boldsymbol{\psi}(\mathrm{q},t))\boldsymbol{\lambda}_{j}(t). \quad (11) \]
 

The quantity  \( l_{0} \)  is the characteristic magnetic length [22]. The vector  \( \Omega \)  and the matrix  \( \Lambda \)  are given by

 \[ \Omega=\xi\mu\beta\left(\begin{aligned}-\left(\alpha\mu\psi_{1}+\psi_{2}\right)\\ \psi_{1}-\alpha\mu\psi_{2}\\ 0\end{aligned}\right),\qquad\xi=\frac{1}{1+\alpha^{2}}, \quad (12) \] 

and

 \[ \Lambda=\xi\left(\begin{aligned}\alpha\mu\psi_{3}&\quad\psi_{3}\quad-\left(\psi_{2}+\alpha\mu\psi_{1}\right)\\ -\psi_{3}&\quad\alpha\mu\psi_{3}\quad\psi_{1}-\alpha\mu\psi_{2}\\ \psi_{2}&\quad-\psi_{1}\quad0\end{aligned}\right). \quad (13) \] 

For convenience we have substituted  \( \bar{t} \rightarrow t \)  again. The statistical properties of  \( \lambda(t) \)  are expressed as  \( \langle\lambda(t)\rangle = 0 \)  and

 \[ \chi_{k l}(t,t^{\prime})=\langle\lambda_{k}(t)\lambda_{l}(t^{\prime})\rangle=\frac{D_{k l}}{\tau_{k l}}\delta_{k l}\exp\left[-\frac{\mid t-t^{\prime}\mid}{\tau_{k l}}\right]\xrightarrow{\tau_{k l}\rightarrow0}2D_{k l}\delta_{k l}\delta(t-t^{\prime}). \quad (14) \] 

Incidentally, in the limit  \( \tau\to0 \)  the usual white noise properties are recovered. We emphasize that although we regard the long-wavelength limit  \( (a\cdot q\ll1) \) , wave vectors for which  \( l_{0}\cdot q\gg1 \)  (in Eq. (10)) can also occur [22]. But this case is not discussed in the present paper and will be the content of future work. Whereas, in what follows we restrict our considerations to the case  \( q\to0 \)  so that, actually,  \( l_{0}\cdot q\ll1 \)  is fulfilled. Hence, we can set  \( \beta=1 \)  approximately in Eq. (10). Due to the anisotropy the spin wave dispersion relation offers a gap at  \( q=0 \) . Owing to this fact  \( \psi \)  is studied at zero wave vector. For this situation the assumption of a space-independent stochastic force  \( \eta_{i}(t) \) , compare Eq. (7), is reasonable. For non-zero wave vector the noise field should be a spatiotemporal field  \( \eta_{i}((\mathbf{r},t) \) . Because our model is based on a short range interaction we expect that the corresponding noise correlation function is  \( \delta \) -correlated, i.e. instead of (14) we have

 \[ \chi_{k l}(\mathbf{r},t;\mathbf{r}^{\prime},t^{\prime})=\frac{D_{k l}}{\tau_{k l}}\delta_{k l}\exp\left[-\frac{\mid t-t^{\prime}\mid}{\tau_{k l}}\right]2M\delta(\mathbf{r}-\mathbf{r}^{\prime}), \] 

where M is the strength of the spatial correlation. Using this relation we are able to study also the case of small q which satisfies  \( l_{0} \cdot q \ll 1 \) . In the present paper we concentrate on the case of zero wave vector q = 0.
 

## III. CORRELATION FUNCTIONS

In the present section let us discuss the statistical behavior of the basic Eqs. (11)-(14). They describe a non-stationary, non-Markovian process attributed to the finite correlation time. Due to their common origin both characteristics can not be analyzed separately. In the limit  \( \tau \rightarrow 0 \) , Eq. (11) defines a Markovian process which provides also stationarity by an appropriate choice of initial conditions [23]. However, the present study is focused on the effect of nonzero correlation times. To that purpose we need a proper probability distribution function which reflects the stochastic process defined by Eqs. (11)-(14). In deriving the relevant joint probability distribution function we follow the line given in [24], where the detailed calculations had been carried out, see also the references cited therein. In particular, it has been underlined in those papers that in order to calculate correlation functions of type  \( \langle\psi_{i}(t)\psi_{j}(t')\rangle \)  a single probability distribution function  \( P(\psi,t) \)  is not sufficient. Instead of that one needs a joint probability distribution of the form  \( P(\psi,t;\psi',t') \) . Before proceeding let us shortly summarize the main steps to get the joint probability distribution function. To simplify the calculation we assume  \( \tau_{kl} = \tau\delta_{kl} \)  and  \( D_{kl} = D\delta_{kl} \) . Notice that our system has no ergodic properties what would directly allow us to relate the stochastic interferences with temperature fluctuations by means of a fluctuation-dissipation theorem. Based on Eq. (11) the appropriate joint probability distribution is defined by [24, 25], for a more general discussion compare also [26]:

 \[ P(\boldsymbol{\psi},t;\boldsymbol{\psi}^{\prime},t^{\prime})=\langle\delta(\boldsymbol{\psi}(t)-\boldsymbol{\psi})\delta(\boldsymbol{\psi}({t}^{\prime})-\boldsymbol{\psi}^{\prime})\rangle. \quad (15) \] 

Here the average is performed over all realizations of the stochastic process. In defining the joint probability distribution function we follow the convention to indicate the stochastic process by the function  \( \psi(t) \)  whereas the quantity without arguments  \( \psi \)  stands for the special values of the stochastic variable. These values are even realized with the probaility  \( P(\psi, t; \psi', t') \) . The equation of motion for this probability distribution reads according to
 

[24]

 \[ \begin{aligned}&\frac{\partial}{\partial t}P(\boldsymbol{\psi},t;\boldsymbol{\psi}^{\prime},t^{\prime})\\&=-\frac{\partial}{\partial\psi_{i}}\int\limits_{0}^{t}\chi_{jk}(t,t_{1})\left\langle\left[\frac{\delta\psi_{i}(t)}{\delta\lambda_{k}(t_{1})}\right]_{\boldsymbol{\psi}(t)=\boldsymbol{\psi}^{\prime}}\cdot\delta(\boldsymbol{\psi}(t)-\boldsymbol{\psi})\delta(\boldsymbol{\psi}({t}^{\prime})-\boldsymbol{\psi}^{\prime})\right\rangle dt_{1}\\&\quad-\frac{\partial}{\partial\psi_{i}^{\prime}}\int\limits_{0}^{t^{\prime}}\chi_{jk}(t,t_{1})\left\langle\left[\frac{\delta\psi_{i}(t^{\prime})}{\delta\lambda_{k}(t_{1})}\right]_{\boldsymbol{\psi}(t^{\prime})=\boldsymbol{\psi}^{\prime}}\cdot\delta(\boldsymbol{\psi}(t)-\boldsymbol{\psi})\delta(\boldsymbol{\psi}({t}^{\prime})-\boldsymbol{\psi}^{\prime})\right\rangle dt_{1},\end{aligned} \quad (16) \] 

where Novikov’s theorem [27] has been applied. Expressions for the response functions  \( \delta\psi_{i}(t)/\delta\lambda_{k}(t_{1}) \)  and  \( \delta\psi_{i}(t^{\prime})/\delta\lambda_{k}(t_{1}) \)  can be found by formal integration of Eq. (11) and iterating the formal solution. After a tedious but straightforward calculation including the computation of the response functions to lowest order in  \( (t-t_{1}) \)  and  \( (t^{\prime}-t_{1}) \)  can be evaluated of several correlation integrals referring to  \( \chi_{kl} \)  from Eq. (14), Eq. (16) can be rewritten in the limit of small correlation time  \( \tau \)  as

 \[ \begin{align*}\frac{\partial}{\partial t}P_{s}(\boldsymbol{\psi},t;\boldsymbol{\psi}^{\prime},t^{\prime})&=\left\{\mathcal{L}^{0}(\boldsymbol{\psi},\tau)\right.\\&\left.+\exp[-(t-t^{\prime})/\tau]D\frac{\partial}{\partial\psi_{i}}\Lambda_{ik}(\boldsymbol{\psi})\frac{\partial}{\partial\psi_{n}^{\prime}}\Lambda_{nk}(\boldsymbol{\psi}^{\prime})\right\}P_{s}(\boldsymbol{\psi},t;\boldsymbol{\psi}^{\prime},t^{\prime}).\end{align*} \quad (17) \] 

Thereby, transient terms and terms of the form  \( \propto \tau \exp[-(t-t')/\tau] \)  (these terms would lead to terms of order  \( \tau^{2} \)  in Eq. (22)) have been neglected. The result is valid in the stationary case characterized by  \( t \to \infty \)  and  \( t' \to \infty \) , but finite  \( s = t - t' \) . In Eq. (17)  \( L^{0} \)  is the operator appearing in the equation for the single probability density. Following [24, 28] the operator reads

 \[ \begin{align*}\mathcal{L}^{0}(\boldsymbol{\psi},\tau)=&-\frac{\partial}{\partial\psi_{i}}\Omega_{i}(\boldsymbol{\psi})+\frac{\partial}{\partial\psi_{i}^{\prime}}\Lambda_{ik}(\boldsymbol{\psi})\frac{\partial}{\partial\psi_{n}}\left\{D\left[\Lambda_{nk}(\boldsymbol{\psi})-\tau M_{nk}(\boldsymbol{\phi})\right]\right.\\&\left.+D^{2}\tau\left[K_{nkm}(\boldsymbol{\psi})\frac{\partial}{\partial\psi_{l}}\Lambda_{lm}(\boldsymbol{\psi})+\frac{1}{2}\Lambda_{nm}(\boldsymbol{\psi})\frac{\partial}{\partial\psi_{l}^{\prime}}K_{lkm}(\boldsymbol{\psi})\right]\right\},\end{align*} \quad (18) \] 

with

 \[ \begin{aligned}&M_{nk}=\Omega_{r}\frac{\partial\Lambda_{nk}}{\partial\psi_{r}}-\Lambda_{rk}\frac{\partial\Omega_{n}}{\partial\psi_{r}}\\&K_{nlk}=\Lambda_{rk}\frac{\partial\Lambda_{nl}}{\partial\psi_{r}}-\frac{\partial\Lambda{}_{nk}}{\partial\psi_{r}}\Lambda_{rl}.\\ \end{aligned} \quad (19) \] 

The equation of motion for the expectation value  \( \langle\psi_{i}\rangle_{s} \)  can be evaluated from the single probability distribution in the stationary state

 \[ \frac{\partial}{\partial t}P_{s}(\boldsymbol{\psi},t)=\mathcal{L}^{0}P_{s}(\boldsymbol{ \psi},t). \quad (20) \]
 

One finds

 \[ \begin{align*}\frac{d}{dt}\left\langle\psi_{i}(t)\right\rangle_{s}=\left\langle\Omega_{i}\right\rangle_{s}+D\left\langle\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}\big(\Lambda_{nk}-\tau M_{nk}\big)\right\rangle_{s}-D^{2}\tau\left\{\left\langle\frac{\partial}{\partial\psi_{r}}\left(\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}K_{nkm}\right)\Lambda_{rm}\right\rangle_{s}\right.\\+\left.\frac{1}{2}\left\langle\frac{\partial}{\partial\psi_{r}}\left(\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}\Lambda_{nm}\right)K_{rkm}\right\rangle_{s}\right\}.\end{align*} \quad (21) \] 

The knowledge of the evolution equation of the joint probability distribution  \(  P(\psi, t; \psi', t')  \)  due to Eqs. (17) and (18) allows us to get the corresponding equation for the correlation functions. Following again [24], it results

 \[ \begin{align*}\frac{d}{dt}\left\langle\psi_{i}(t)\psi_{j}(t^{\prime})\right\rangle_{s}&=\left\langle\Omega_{i}(\psi(t))\psi_{j}(t^{\prime})\right\rangle_{s}+D\left\langle\left[\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}\big(\Lambda_{nk}-\tau M_{nk}\big)\right]_{t}\psi_{j}(t^{\prime})\right\rangle_{s}\\&-D^{2}\tau\left\{\left\langle\left[\frac{\partial}{\partial\psi_{r}}\left(\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}K_{nkm}\right)\Lambda_{rm}\right]_{t}\psi_{j}(t^{\prime})\right\rangle_{s}\right.\\&\left.+\frac{1}{2}\left\langle\left[\frac{\partial}{\partial\psi_{r}}\left(\frac{\partial\Lambda_{ik}}{\partial\psi_{n}}\Lambda_{nm}\right)K_{rkm}\right]_{t}\psi_{j}(t^{\prime})\right\rangle_{s}\right\}\\&+D\exp\left[-\frac{t-t^{\prime}}{\tau}\right]\left\langle\Lambda_{ik}(\psi(t))\Lambda_{jk}(\psi(t^{\prime}))\right\rangle_{s},\end{align*} \quad (22) \] 

where the symbol  \( \left[\ldots\right]_{t} \)  denotes the quantity  \( \left[\ldots\right] \)  at time t. As mentioned above the result is valid for  \( t, t' \to \infty \)  while  \( s = t - t' > 0 \)  remains finite. The quantities  \( M_{nk} \)  and  \( K_{klm} \)  are defined in Eq. (19). The components  \( \Omega_{i} \)  and  \( \Lambda_{ij} \)  are given in Eqs. (12) and (13). Performing the summation over double-indices according to Eqs. (21) and (22) we obtain the evolution equations for the mean value and the correlation function

 \[ \frac{d}{d t}\left\langle\psi_{i}(t)\right\rangle_{s}=G_{i k}\left\langle\psi_{k}(t)\right\rangle_{s}, \quad (23) \] 

and

 \[ \begin{align*}\frac{d}{ds}\mathcal{C}_{ij}(s)=\frac{d}{ds}\left\langle\psi_{i}(t^{\prime}+s)\psi_{j}(t^{\prime})\right\rangle_{s}=&G_{ik}\left\langle\psi_{k}(t^{\prime}+s)\psi_{j}(t^{\prime})\right\rangle_{s}\\&+D\exp\left[-\frac{s}{\tau}\right]\left\langle\Lambda_{ik}(\psi(t^{\prime}+s))\Lambda_{jk}(\psi(t^{\prime}))\right\rangle_{s}.\end{align*} \quad (24) \] 

Notice, that in the steady state one gets  \( \mathcal{C}_{ij}(t,t') = \mathcal{C}_{ij}'(s) \)  with  \( s = t - t' \) . The matrix components of  \( G_{ik} \)  are given by

 \[ G_{i k}=\begin{pmatrix}{{{-A_{1}}}}&{{{A_{2}}}}&{{{0}}} \\{{{-A_{2}}}}&{{{-A_{1}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{-A_{3}}}}\end{pmatrix}, \quad (25) \]
 

where

 \[ \begin{aligned}&A_{1}=-D^{2}\tau(6\mu^{2}\alpha^{2}-1)\xi^{4}+2\mu^{2}\alpha D\tau\xi^{3}-D(\mu^{2}\alpha^{2}-2)\xi^{2}+\mu^{2}\alpha\xi\\&A_{2}=\frac{1}{2}\mu\alpha D^{2}\tau\left(11-3\mu^{2}\alpha^{2}\right)\xi^{4}+\mu D\tau\left(\mu^{2}\alpha^{2}-1\right)\xi^{3}+3\mu D\alpha\xi^{2}-\mu\xi\\&A_{3}=+D^{2}\tau\left(3\mu^{2}\alpha^{2}+1\right)\xi^{4}-4\mu^{2}\alpha D\tau\xi^{3}+2D\xi^{2},\\ \end{aligned} \quad (26) \] 

and  \( \xi \)  is defined in Eq. (12). At this point let us stress that in the case  \( t' = 0 \)  the term  \( \propto \exp[-(t - t')/\tau] \)  on the rhs. in Eqs. (22) and (24), respectively, would vanish in the steady state, i.e.

 \[ \langle\psi_{i}(t^{\prime}+s)\psi_{j}(t^{\prime})\rangle_{s}\neq\langle\psi_{i}(s)\psi_{j}(0)\rangle_{s}. \] 

The occurrence of such a term is a strong indication for the non-stationarity of our model. An explicit calculation shows, that in general this inequality holds for non-stationary processes [23].

## IV. RESULTS

The solution of Eq. (23) can be found by standard Greens function methods and Laplace transformation. As the result we find

 \[ \left\langle\boldsymbol{\psi}(t)\right\rangle_{s}=\left(\begin{array}{c c c}{e^{-A_{1}t}\cos(A_{2}t)}&{e^{-A_{1}}t\sin(A_{2}t)}&&{0}\\ {-e^{-A_{1}}t\sin(A_{2}t)}&{e^{-A_{1}t}\cos(A_{2}t)}&&{0}\\ {0}&{0}&{e^{-A_{3}t}}\\ \end{array}\right)\cdot\left\langle\boldsymbol{\psi}_{0}\right\rangle_{s}, \quad (27) \] 

where  \( \langle\psi_{0}\rangle_{s}=\langle\psi(t=0)\rangle_{s} \)  are the initial conditions. The parameters  \( A_{1}, A_{3} \)  and  \( A_{2} \)  defined in Eqs. (26) play the roles of the magnon lifetime and the frequency of the spin wave at zero wave vector, respectively. As can be seen in Eq. (26) all of these three parameters are affected by the correlation time  \( \tau \)  and the strength D of the random force. Moreover, the Gilbert damping parameter  \( \alpha \)  influences the system as well. The solution of Eq. (24) for the correlation function in case of  \( t'=0 \)  is formal identical to that of Eq. (27). The more general situation  \( t'\neq0 \)  allows no simple analytic solution and hence the behavior of the correlation function  \( \mathcal{C}(s) \)  is studied numerically. In order to analyze the mean values and the correlation function let us first examine the parameter range where physical accessible solutions exist. In the following we assume  \( \langle\psi_{1}(0)\rangle=\langle\psi_{2}(0)\rangle=\left\langle\psi_{0}\right\rangle \)  and  \( \langle\psi_{3}(0)\rangle=0 \) , since the solutions for  \( \psi_{1}(t) \)  and  \( \psi_{2}(t) \)  on the one hand and  \( \psi_{3}(t) \)  on the other hand are decoupled
 

in Eq. (27). Therefore, spin wave solutions only exist for non-zero averages  \( \langle\psi_{1}(t)\rangle \)  and  \( \langle\psi_{\mathrm{2}}(t)\rangle \) . The existence of such non-trivial solutions are determined in dependence on the noise parameters D and  \( \tau \)  and the deterministic damping parameter  \( \alpha \) . Notice, that the dimensionless quantity  \( D=\tilde{D}/\Gamma \) , i.e., D is the ratio between the strength of the correlation function (Eq. (7)) and the anisotropy field in the original units. The stability of spin wave solutions is guaranteed for positive parameters  \( A_{1} \)  and  \( A_{3} \) . According to Eqs. (26) the phase diagrams are depicted in Fig. 2 within the  \( \alpha-D \)  plane for different values of the correlation time  \( \tau \) . The separatrix between stable and unstable regions is determined by the condition  \( A_{1}=0 \) . The second condition  \( A_{3}=0 \)  is irrelevant due to the imposed initial conditions. As the result of the stability analysis the phase space diagram is subdivided into four regions where region IV does not exist in case of  \( \tau=0 \) , see Fig. 2(a). For generality, we take into account both positive and negative values of D indicating correlations and anti-correlations of the stochastic field. Damped spin waves are observed in the areas I and IV, whereas the sectors II and III reveal non-accessible solutions. In those regions the spin wave amplitude, proportional to  \( \exp[-A_{1}t] \) , tends to infinity which should not be realized, compare Figs. 2(b)-2(d). Actually, a reasonable behavior is observed in regions I and IV. As visible from Fig. 2 damped spin waves will always emerge for D>0 even in the limit of zero damping parameter  \( \alpha \)  and vanishing correlation time  \( \tau \) . This behavior is shown in Fig. 3, where the evolution of  \( \langle\psi_{1}(t)\rangle \)  is depicted for different values of  \( \alpha \) . As can be seen in Fig. 2(a) the solution for D<0 is unlimited and consequently, it should be excluded further. Contrary to this situation, additional solutions will be developed in region IV in case of  \( \tau>0 \)  and simultaneously  \( \alpha=0 \) , see Figs. 2(b)-2(d). Thereby the size of area IV grows with increasing  \( \tau \) . Likewise, the extent of region I decreases for an enhanced  \( \tau \) . However, in the limit of D=0 and consequently for  \( \tau=0 \) , too, only damped spin waves are observed. Immediately on the separations line undamped periodic solutions will evolve, compare the sub-figures in Fig. 2. This remarkable effect can be traced back to the interplay between the deterministic damping and the stochastic forces. Both damping mechanism are compensated mutually which reminds of a kind of resonance phenomenon. The difference to conventional resonance behavior consists of the compensation of the inherent deterministic Gilbert damping and the stochastic one originated from the random field. This statement is emphasized by the fact that undamped periodic solutions do not develop in the absence of stochastic interferences, i.e., D=0. The situation might be interpreted physically as follows: the required energy
 
![](./images/867757382543868675_2.jpg)

(a)  \( \tau = 0 \) 

![](./images/867757382543868675_3.jpg)

(b)  \( \tau = 0.1 \) 

![](./images/867757382543868675_4.jpg)

(c)  \( \tau = 1 \) 

![](./images/867757382543868675_5.jpg)

(d)  \( \tau = 10 \) 

FIG. 2.  \( \alpha - D \)  plane for fixed magnetization  \( \mu = 0.9 \)  and different values of  \( \tau \) .

that enables the system to sustain the deterministic damping mechanisms is delivered by the stochastic influences due to the interaction with the environment. To be more precise, in general, the Gilbert damping enforces the coherent alignment of the spin density along the precession axis. Contrary, the random field supports the dephasing of the orientation of the classical spins. Surprisingly, the model predicts the existence of a critical value  \( \tau = \tau_{c} \geq 0 \)
 
![](./images/867757382543868675_6.jpg)

FIG. 3. Evolution of the mean value  \( \langle\psi_{1}(t)\rangle \) , with  \( \mu=0.9 \) , D=0.1 and  \( \tau=0 \) .  \( \alpha \)  varies from 0 (dash-dotted line), 0.05 (solid line), 0.5 (dotted line) and 1 (dashed line).

depending on  \( \alpha \)  and D which determines the onset of undamped periodic solutions. Notice, that negative values of  \( \tau_{c} \)  are excluded. The critical value is

 \[ \tau_{c}=-\frac{[\mu^{2}\left(\alpha^{3}-D\alpha^{2}+\alpha\right)+2D]\left(1+\alpha^{2}\right)^{2}}{2D\mu^{2}\left(\alpha^{3}-3D\alpha^{2}+\alpha\right)+D^{2}}. \quad (28) \] 

Hence, this result could imply the possibility of the cancellation of both damping processes. Examples according to the damped and the periodic case are displayed in Fig. 4. An increasing  \( \tau \)  favors the damping process as it is visible in Fig. 4(a). Based on estimations obtained for ferromagnetic materials [29] and references therein, the Gilbert damping parameter can range between  \( 0.04 < \alpha < 0.22 \)  in thin magnetic films, whereas the bulk value for Co takes  \( \alpha_{b} \approx 0.005 \) . The phase space diagram in Fig. 2 offers periodic solutions only for values of  \( \alpha \)  larger than those known from experiments. Therefore such periodic solutions seem to be hard to see experimentally. We proceed further by analyzing the behavior of the correlation function by numerical computation of the solution of Eq. (24) with Eqs. (25) and (26). As initial values we choose  \( \mathcal{C}_{ik}(t = t', t') = \mathcal{C}_{ik} (s = 0) = \mathcal{C}_{0} \)  for every combination  \( i, k = \{1, 2, 3\} \) . The results are depicted in Figs. 5 and 6. Inspecting Figs. 5(a)–5(c) one recognizes that an enhancement of the correlation time  \( \tau \)  leads to an increase of the oscillations within the correlation functions  \( C_{1k}, k = \{1, 2, 3\} \) . Moreover, Fig. 5(d) reveals that the oscillatory
 
![](./images/867757382543868675_7.jpg)

(a)

![](./images/867757382543868675_8.jpg)

(b)

FIG. 4. Evolution of the mean values  \( \langle\psi_{1,2}(t)\rangle \) , with  \( \mu=0.9 \) . (a): D=0.1,  \( \alpha=0.005 \)  and  \( \tau \)  varies from 10 (solid line), 1 (dotted line) and 0 (dash-dotted line). (b): D=2,  \( \alpha=1 \)  and  \( \tau=\tau_{c}\approx1.79 \)  (Eq. (28)). The solid line represents  \( \langle\psi_{1}\rangle \)  and the dash-dotted line is  \( \langle\psi_{2}\rangle \) .

behavior of  \( C_{31} \)  seems to be suppressed. Obviously, the decay of the correlation function is enhanced if  \( \tau \)  growths up. The pure periodic case for  \( \tau = \tau_{c} \) , corresponding to Fig. 4(b), is depicted in Fig. 6. Exemplary,  \( C_{12} \)  and  \( C_{31} \)  are illustrated. The behavior of the latter is similar to the damped case, displayed in Fig. 5(d), unless slight oscillations occur. However, if one compares the form of  \( C_{12} \)  in Fig. 5(b) and Fig. 6 the differences are obvious. The amplitude of the correlation function for the undamped case grows to the fourfold magnitude in comparison with  \( C_{0} \) , whereas the damped correlation function approaches zero. Further, a periodic behavior is shown in Fig. 6, and therefore the correlation will oscillate about zero but never vanish for all  \( s = t - t' > 0 \) .

## V. CONCLUSIONS

In this paper we have analyzed the dynamics of a classical spin model with uniaxial anisotropy. Aside from the deterministic damping due to the Landau-Lifshitz-Gilbert equation the system is subjected to an additional dissipation process by the inclusion of a stochastic field with colored noise. Both dissipation processes are able to compete leading to
 
![](./images/867757382543868675_9.jpg)

(a)

![](./images/867757382543868675_10.jpg)

(b)

![](./images/867757382543868675_11.jpg)

(c)

![](./images/867757382543868675_12.jpg)

(d)

FIG. 5. Correlation functions  \( \mathcal{C}_{ik}(s) \)  for  \( \mu = 0.9 \) , D = 0.1 and  \( \alpha = 0.005 \) .  \( \tau \)  takes 0 (dotted line), 1 (solid line) and 10 (dash-dotted line).

a more complex behavior. To study this one we derive an equation for the joint probability distribution which allows us to find the corresponding spin-spin-correlation function. This program can be fulfilled analytically and numerically in the spin wave approach and the small correlation time limit. Based on the mean value for the spin wave component and
 
![](./images/867757382543868675_13.jpg)

FIG. 6. Correlation functions  \( \mathcal{C}_{ik}(s) \)  for  \( \tau = \tau_{c} \approx 1.79 \)  (Eq. (28)),  \( \mu = 0.9 \) , D = 2 and  \( \alpha = 1 \) . The dotted line represents  \( C_{12} \)  and the solid line is  \( C_{31} \) .

the correlation function we discuss the stability of the system in terms of the stochastic parameters, namely the strength of the correlated noise D and the finite correlation time  \( \tau \) , as well as the deterministic Gilbert damping parameter  \( \alpha \) . The phase diagram in the  \( \alpha - D \)  plane offers that the system develops stable and unstable spin wave solutions due to the interplay between the stochastic and the deterministic damping mechanism. So stable solutions evolve for arbitrary positive D and moderate values of the Gilbert damping  \( \alpha \) . Further, we find that also the finite correlation time of the stochastic field influences the evolution of the spin waves. In particular, the model reveals for fixed D and  \( \alpha \)  a critical value  \( \tau_{c} \)  which characterizes the occurrence of undamped spin waves. The different situations are depicted in Fig. 2. Moreover, the correlation time  \( \tau \)  affects the damped spin wave which can be observed in regions I and IV in the phase diagram. If the parameters D and  \( \alpha \)  changes within these regions, an increasing  \( \tau \)  leads to an enhancement of the spin wave damping, cf. Fig. 4(a). The influence of  \( \tau \)  on the correlation functions is similar as shown in Figs. 5(a)-5(c). The study could be extended by the inclusion of finite wave vectors and using an approach beyond the spin wave approximation.
 

## ACKNOWLEDGMENTS

One of us (T.B.) is grateful to the Research Network 'Nanostructured Materials', which is supported by the Saxony-Anhalt State, Germany.
 

[1] L. D. Landau, E. Lifshitz, and L. Pitaevskii, Electrodynamics of continuous media (Pergamon Press, Oxford, 1989).

[2] L. Landau and E. Lifshitz, Zeitschr. d. Sowj. 8, 153 (1935).

[3] Y. Tserkovnyak, A. Brataas, G. E. W. Bauer, and B. I. Halperin, Rev. Mod. Phys. 77, 1375 (2005).

[4] A. Sukhov and J. Berakdar, J. Phys. - Cond. Mat. 20, 125226 (2008).

[5] J. C. Slonczewski, J. Magn. and Mag. Mat. 159, L1 (1996).

[6] L. Berger, Phys. Rev. B 54, 9353 (1996).

[7] S. Urazhdin, Phys. Rev. B 78, 060405 (2008).

[8] B. Krüger, D. Pfannkuche, M. Bolte, G. Meier, and U. Merkt, Phys. Rev. B 75, 054421 (2007).

[9] K. D. Usadel, Phys. Rev. B 73, 212405 (2006).

[10] T. L. Gilbert, IEEE Trans. Magn. 40, 3443 (2004).

[11] M. C. Hickey and J. S. Moodera, Phys. Rev. Lett. 102, 137601 (2009).

[12] S. F. Zhang and S. S. L. Zhang, Phys. Rev. Lett. 102, 086601 (2009).

[13] S. Trimper, T. Michael, and J. M. Wesselinowa, Phys. Rev. B 76, 094108 (2007).

[14] J. Foros, A. Brataas, G. E. W. Bauer, and Y. Tserkovnyak, Phys. Rev. B 79, 214407 (2009).

[15] A. L. Chudnovskiy, J. Swiebodzinski, and A. Kamenev, Phys. Rev. Lett. 101, 066601 (2008).

[16] D. M. Basko and M. G. Vavilov, Phys. Rev. B 79, 064418 (2009).

[17] S. I. Denisov, K. Sakmann, P. Talkner, and P. Hänggi, Phys. Rev. B 75, 184432 (2007).

[18] M. Daniel and M. Lakshmanan, Physica A 120, 125 (1983).

[19] M. Lakshmanan and K. Nakamura, Phys. Rev. Lett. 53, 2497 (1984).

[20] V. G. Bar'Yakhtar, M. V. Chetkin, B. A. Ivanov, and S. N. Gadetskii, Dynamics of Topological Magnetic Solitons: Experiment and Theory (Springer Tracts in Modern Physics) (Springer, 1994).

[21] M. Lakshmanan, T. W. Ruijgrok, and C. J. Thompson, Physica A 84, 577 (1976).

[22] A. M. Kosevich, B. A. Ivanov, and A. S. Kovalev, Phys. Rep. 194, 117 (1990).

[23] A. Hernandez-Machado and M. San Miguel, J. Math. Phys. 25, 1066 (1984).

[24] A. Hernandez-Machado, J. M. Sancho, M. San Miguel, and L. Pesquera, Zeitschr. f. Phys. B 52, 335 (1983).
 

[25] N. G. van Kampen, Braz. J. Phys. 28, 90 (1998).

[26] N. G. van Kampen, Stochastic Processes in Physics and Chemistry (North-Holland, Amsterdam, 1981).

[27] E. A. Novikov, Sov. Phys. JETP 20, 1290 (1965).

[28] H. Dekker, Phys. Lett. A 90, 26 (1982).

[29] Y. Tserkovnyak, A. Brataas, and G. E. W. Bauer, Phys. Rev. Lett. 88, 117601 (2002).
 
