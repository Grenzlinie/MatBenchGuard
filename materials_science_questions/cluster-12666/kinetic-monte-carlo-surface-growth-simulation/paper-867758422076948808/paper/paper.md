An improved kinetic Monte Carlo model for computational and analytical
investigations of the magnetic properties of finite-size atomic chains

S.V. Kolesnikov*
Faculty of Physics, Lomonosov Moscow State University, Moscow 119991, Russian Federation
(Dated: March 5, 2022)

Two improved kMC models for investigations of the magnetic properties of finite-size atomic
chains are presented. These models take the possible noncollinearity of magnetic moments into
account. The spontaneous remagnetization of ferromagnetic Co chains on Pt(997) surface and
antiferromagnetic Fe chains on Cu₂N/Cu(001) surface is investigated in the framework of our models.
The results are compared with the results of the simple kMC model. It is also shown that a
single domain-wall approximation can be successfully used to estimation of the reversal time of the
magnetization. Therefore, the improved kMC models can be used for analytical calculations as well
as for computer simulations.

Keywords: biatomic chains, magnetic properties, Heisenberg model, single domain-wall approximation

## I. INTRODUCTION

Atomic chains and nanowires are very prospective in
spintronics [1], quantum computing [2], quantum com-
munications [3, 4], and other fields [5] due to its unusual
magnetic properties. The possibility of application of
the atomic chains as bits of information appeared after
the discovery of the giant magnetic anisotropy energy
(MAE) of Co atoms in ferromagnetic atomic chains on
the Pt(997) surface [6, 7]. The possibility of creating and
remagnetization of finite-sized antiferromagnetic chains
was demonstrated for Fe atomic chains on Cu₂N/Cu(001)
surface [8, 9].

Usually, the magnetic properties of the atomic chains
can be satisfactory described in the the framework of
Heisenberg model with uniaxial anisotropy. It is nec-
essary to underline that quantum tunneling is the main
switching mechanism at extremely low temperatures [10].
However, the quantum nature of the atomic magnetic
moments can be neglected at higher temperatures. In
this case the classical Heisenberg model can be applied.
If the external magnetic field is absent then the classical
Heisenberg Hamiltonian can be written in the following
form

$$
H=-\sum_{i>j} J_{i j}\left(\mathbf{s}_{i} \cdot \mathbf{s}_{j}\right)-K \sum_{i}\left(\mathbf{s}_{i} \cdot \mathbf{e}\right)^{2}, \quad(1)
$$

where $\mathbf{s}_{i}$ and $\mathbf{e}$ are the unit vectors of the magnetic
moments of the atoms and the easy axis of magnetiza-
tion, respectively, $K$ is MAE, $J_{i j}=J(\delta_{i, j+1}+\delta_{i, j-1})$
is the exchange energy, $\delta_{i j}$ is Kronecker delta. For the
ferromagnetic chains $J>0$ and for the antiferromag-
netic chains $J<0$. The parameters of the Hamilto-
nian (1) can be found experimentally or calculated from
the first principles by the means of density functional
theory [11] or Korringa-Kohn-Rostoker-Green's function
method [12]. Further investigation of the magnetic prop-
erties of atomic chains can be performed with either the
solution of the Landau-Lifshitz-Gilbert equation [13, 14]
or the Monte Carlo simulations [15].

The simplest kinetic Monte Carlo (kMC) model for in-
vestigation of magnetic properties of atomic chains was
proposed by Li and Liu [16]. This kMC model allows
to calculate the critical temperature, the reversal time of
the magnetization, and the coercive field of ferromagnetic
chains [17-21]. It can be also applied for the investiga-
tion of antiferromagnetic chains [22, 23]. However, the
simplest kMC model [16] assumes that (i) the directions
of all magnetic moments are collinear to the easy axis of
magnetization and (ii) rotation of the magnetic moment
does not influence on the directions of other ones. These
assumptions are very rude, because the metastable states
of ferromagnetic or antiferromagnetic chains can be non-
collinear [24-26].

The main goal of our paper is introducing the im-
proved kMC models which take the noncollinearity of
magnetic moments into account. In Section II we de-
scribe two improved kMC models. The applicability of
these kMC models to real systems (Co on Pt(997) and Fe
on Cu₂N/Cu(001)) are shown in Section III. Section IV
concludes the paper. Some additional remarks about
the calculation of diffusion barriers are presented in Ap-
pendix.

## II. METHODS

This is the most important Section of the paper. Here
we present two novel kMC models which significantly im-
prove computational accuracy. These models take the
noncollinearity of magnetic moments into account. In
Section 3 the results of the presented models will be
compared with the analogous results of the simple kMC
model [16]. So, first of all we remember the simple
kMC model. At the end of this Section the analytical
method [27-30] which allows to estimate the reversal time
of magnetization of atomic chains is shortly discussed.

* kolesnikov@physics.msu.ru

### A. A simple kMC model

The simplest kMC model for investigation of magnetic properties of atomic chains is the model suggested by Li and Liu [16]. It is assumed that all of the magnetic moments are directed either parallel or antiparallel to the easy axis of magnetization $(\mathbf{s}_i \cdot \mathbf{e}) = \pm 1$. Each magnetic moment can be only in two states: it is directed "up" if $(\mathbf{s}_i \cdot \mathbf{e}) = 1$, or "down" if $(\mathbf{s}_i \cdot \mathbf{e}) = -1$. The transition of $i$th magnetic moment from one state to another is its rotation in the plain at the condition that all other magnetic moments are still directed either up or down. In this case the transition rates $\nu_i$ can be easily calculated analytically. If $2K > |h_i|$ then

$$
\nu_i = \nu_0 \exp\left(-\frac{(2K + h_i)^2}{4K k_{\rm B} T}\right), \tag{2}
$$

where $k_{\rm B}$ is the Boltzmann constant, $T$ is the temperature, and $\nu_0 = 10^9$ Hz [6] is the frequency prefactor, $h_i = \sum_j J_{ij}(\mathbf{s}_i \cdot \mathbf{s}_j)$. If $2K \leq |h_i|$, then there is no diffusion barrier between the initial and the final states. The transition rate $\nu_i$ can be calculated [31], as

$$
\nu_i = \nu_0 \frac{\exp(-2h_i/k_{\rm B}T)}{1 + \exp(-2h_i/k_{\rm B}T)}. \tag{3}
$$

### B. An improved kMC model I

The simple kMC model [16] assumes that the directions of all magnetic moments (except one) are frozen. This assumption is the main drawback of the model. In order to overcome this drawback we suggest that the magnetic moments can be noncollinear to each other and the easy axis of magnetization. Thus, we can not manifest that the $i$th magnetic moment is directed up or down. Instead of this the directions of all magnetic moments should be found as a result of minimisation of the magnetic energy of the chain. The minimisation of the magnetic energy can be realised as a relaxation of the directions of the magnetic moments. This process is analogous to finding of relaxed geometry of an atomic system by means of molecular statics. We also can calculate the diffusion barriers between the relaxed states by means of the geodesic nudged elastic band (GNEB) method [32]. The symmetry of the Hamiltonian (1) allows to significantly simplify calculations by usage of XY-model. Important details of molecular statics and GNEB methods in the framework of XY-model are shortly discussed in Appendix.

The thickness of the domain wall can be estimated as $\delta N = \sqrt{J/2K}$ atoms [29, 33]. We can distinguish two different cases: $J \ll K$ and $J \gtrsim K$. Let us discuss the first case. If $J \ll K$ then the thickness of the domain wall is neglectable ($\delta N \ll 1$). Thus, all magnetic moments are slightly collinear to the easy axis of magnetization $(\mathbf{s}_i \cdot \mathbf{e}) \approx \pm 1$. It means that the atomic chain has the same metastable states as in the framework of the simple kMC model [16]. In other words, we can still assume that only one magnetic moment flips at each kMC step. However, instead of the analytical equation (2) we use the general rule of calculations of the transition rate

$$
\nu_i = \nu_0 \exp\left(-\frac{E_i^D}{k_{\rm B}T}\right), \tag{4}
$$

where $E_i^D$ is diffusion barrier calculated by means of GNEB method. This kMC model we will refer as the improved kMC model I. All diffusion barriers are calculated "on the fly" and saved in database. From this point of view the improved kMC model I is analogous to self-learning kMC models widely used for simulation of diffusion processes [34–36].

Let as underline the main features of the improved kMC model I: (i) there are the same metastable states as in the simple kMC model [16], (ii) all diffusion barriers are calculated "on the fly" with GNEB method [32].

### C. An improved kMC model II

Let us discuss the case $J \gtrsim K$. The domain wall has the thickness of several atoms. Thus, the straightforward rotations of single magnetic moments can lead to unstable states. As a consequence, the number of metastable states of the atomic chain is different to one in the framework of the simple kMC model [16]. Therefore, searching the metastable states becomes the important part of the kMC algorithm. There are exact methods of searching the metastable states of finite-size chains [24, 25]. However these methods are hardly applicable to the atomic chains consisting of several tens of atoms because of their very high computational cost in the case of long chains.

Here, we present the following method of searching the metastable states of finite-size chain. First of all we need find all low energy metastable states of an infinite chain. There are four such states (see also Figure 3): clockwise domain wall (CDW), anti-clockwise domain wall (ACDW), clockwise anti-domain wall (CADW), and anti-clockwise anti-domain wall (ACADW). All these states have the same energy. We will refer their as etalon states. Now, we can use the etalon states for searching of metastable states of the finite-size chain. This procedure consist of two steps: (i) constructing of the metastable state from the etalon states, (ii) relaxation of the atomic chain. Each metastable state can be labelled with the the number of etalon states and their positions. So, recognising of any metastable state can be performed by mapping with the etalon states.

At each kMC step one of the following events occurs: (i) formation or disappearance of the etalon states at the edge of the chain, (ii) formation or disappearance of pair of the etalon states (CDW-CADW or ACDW-ACADW), (iii) transition of the etalon state along the chain, and (iv) transition of the clockwise etalon state

to anti-clockwise etalon state or vise versa. All diffusion barriers are calculated "on the fly" by means of GNEB method. This kMC model we will refer as the improved kMC model II.

Let as underline the main features of the improved kMC model II: (i) searching of metastable states by map- ping with etalon states, (ii) existence of clockwise and anti-clockwise states, (iii) all diffusion barriers are calcu- lated "on the fly" with GNEB method [32].

### D. Analytical method

The reversal time of the magnetization of the atomic chain can be easily calculate in the framework of a sin- gle domain-wall approximation [27-30]. The idea of this method is the following. The reversal time of the mag- netization $\tau$ of the atomic chain can be calculate as the average time of the random walk of the domain wall. In the simplest case the random walk of the domain wall is characterized by only three rates: (i) the rate of forma- tion of the domain wall $\nu_{1}$, (ii) the rate of the domain wall disappearance $\nu_{2}$, and (iii) the rate of motion of the domain wall along the chain $\nu_{3}$. To calculate the average time of the random walk of the domain wall the mean rate method can be employed [37, 38].

In the simplest case the reversal time of magnetization of ferromagnetic or antiferromagnetic single-atomic chain can be obtained as

$$
\begin{aligned}
\tau=\frac{1}{n a}\left\{\frac{a}{\nu_{3}}\left(\frac{N-1}{2}\right)\right. & {\left[N-\frac{2(1-2 a)}{1-a}\right]+} \\
& \left.+\frac{1}{\nu_{1}}[N(1-a)-2(1-2 a)]\right\}, \quad(5)
\end{aligned}
$$

where $a=\nu_{3} /(\nu_{2}+\nu_{3}), n=2, N$ is number of atoms in the chain. Equation (5) has been derived in the frame- work of the simple kMC model [16] and can be used with- out any changes in the framework of the improved kMC model I. Here $n$ is the number of states which can form at the edges of the chain: domain wall from the one side of the chain and anti-domain wall from another side of the chain.

In order to use equation (5) in the case of the im- proved kMC model II the following two changes should be applied. First, there are four states (CDW, ACDW, CADW and ACADW) which can form at the edges of the chain. Thus, $n=4$. Second, the etalon states have nonvanishing thickness. Thus, the number $N$ should be replaced by $N_{\text {eff }} \leq N$, where $N_{\text {eff }}-1$ is a number of possible metastable positions of CDW (or another etalon state) in the atomic chain.

### III. RESULTS AND DISCUSSIONS

In order to illustrate applicability of the proposed kMC models to real atomic chains we shortly discuss two sys- tems: Fe chains on $\mathrm{Cu}_{2} \mathrm{~N} / \mathrm{Cu}(001)$ surface and $\mathrm{Co}$ chains on Pt(997) surface.

### A. Antiferromagnetic Fe chains on $\mathrm{Cu}_{2} \mathrm{~N} / \mathrm{Cu}(001)$ surface

According to the experimental study [8], the exchange energies of $\mathrm{Fe}$ atoms are $J=1.3 \pm 0.1 \mathrm{meV}$. In three atomic chain MAE varies from $2.1 \pm 0.1 \mathrm{meV}$ for the edge atoms to $3.6 \pm 0.1 \mathrm{meV}$ for the central atom [9]. For the numerical estimates the following parameters of the Hamiltonian (1) $J=1.3 \mathrm{meV}, K=3.0 \mathrm{meV}$ are chosen. The ratio $K / J \approx 2.3$ and the rotations of sin- gle magnetic moments always lead to new metastable state. The examples of such events in the case of very short Fe chain consisting of $N=5$ atoms are shown in Fig. 1. One can see that the taking the relaxation ef- fects into account leads to decreasing the diffusion barri- ers. Moreover, the diffusion barriers at the edges of the chain are less then the analogous barriers at the middle of the chain. However, the thickness of domain walls is neglectable, all magnetic moments in metastable states are approximately parallel to the easy axis of magnetiza- tion, and the number of metastable states is the same as in the simple kMC model. Therefore, the improved kMC model I can be applied for this system.

![](./images/867758422076948808_1.jpg)

FIG. 1. Diffusion barriers of the rotations of magnetic mo- ments in the case of Fe chain consisting of $N=5$ atoms on $\mathrm{Cu}_{2} \mathrm{~N} / \mathrm{Cu}(001)$ surface: (a) formation of the domain wall at the edge, (b,c) motion of the domain wall along the chain,(d,e) formation of the pair of domain walls. All values are given in meV. The nonrelaxed values (simple kMC model [16]) are given in brackets.

Figure 2 shows the dependencies of the reversal time of the magnetization the Fe chain on $\mathrm{Cu}_{2} \mathrm{~N} / \mathrm{Cu}(001)$ sur face. The results of kMC simulation are averaged over

1000 remagnetisations and shown with points. In order to estimate an influence of the relaxation effect on the re- versal time of the magnetization we compare the results of the simple kMC model (black points) and the improved kMC model I (red points). Everyone can see that the re- laxation effect leads to decrease of the reversal time of the magnetization by the factor $\eta=\tau / \tau_{relaxed } \approx 2-3$ at $T=4-7 ~K$ (Fig 2a). The factor $\eta$ is almost indepen dent on the length of the chain. Indeed, at the current parameters of the Hamiltonian the following inequalitiesare satisfied: $\nu_{1} \ll \nu_{3} \ll \nu_{2}$ . Therefore, the equation (5) can be simplified as

$$
\tau \approx \frac{N-2}{2} \frac{\nu_{2}}{\nu_{1} \nu_{3}}. \quad(6)
$$

At this limit the the reversal time of the magnetization linearly depends on the number of atoms $N$ (Fig 2b), and the factor $\eta$ does not depend on $N$.

![](./images/867758422076948808_2.jpg)

FIG. 2. The dependencies of the reversal time of the magne- tization the Fe chain on $Cu_{2} ~N / Cu(001)$ surface in the frame work the simple kMC model [16] and the improved kMC model I. (a) The temperature dependence of the chain consist- ing of $N=10$ atoms. (b) The dependence on the length of the chain at $T=4 ~K$ . The parameters of the Heisenberg Hamil tonian are the following: $J=1.3 meV$ and $K=3.0 meV$ .

The analytical results obtained with equation (5) are presented in Fig. 2 with solid and dashed lines. In the case of the simple kMC model the equation (2) are used for calculation of the transition rates $\nu_{i}, i=1,2,3$ . In the case of the improved kMC model I we use the equation(4) with the diffusion barriers shown in Fig. 1: $E_{1}^{D}=$ 4.32 meV, E = 1.72 meV, E = 2.76 meV. One can see that our analytical approach gives the same results as the kMC simulations.

## B. Ferromagnetic Co chains on $Pt(997)$ surface
According to the experimental paper [6], the exchange energies of Co atoms are $J \approx 7.5 meV$ and MAE is2.0 ± 0.2 meV. For the numerical estimates we choosethe following parameters of the Hamiltonian (1): $J=$  $7.5 meV$ and $K=2.0 meV$ . The ratio $K / J \approx 0.27$ , and the thickness of the domain wall is not neglectable(ON = J/2K ≈ 1.37). In this case the improved kMC model II can be applied, and the metastable states canbe found as it was described in Section II C. If $N<10$  then there are not metastable states. In this case all magnetic moments flip simultaneously (superparamag- netic regime). If $10 \leq N<22$ then only the single etalon states (CDW, ACDW, CADW and ACADW) can be metastable. If $N=10$ the metastable etalon statescan be located only in the middle of the chain. If $N=22$  then the pair of states CDW-ACADW and CDW-CADW can be metastable. If $N>22$ then all possible pairs of etalon states can be metastable.

![](./images/867758422076948808_3.jpg)

FIG. 3. Possible one-domain wall states of the Co chain on $Pt(997)$ surface in the framework of the improved kMC model II. The central ten atoms of the long chain are shown.

For searching of metastable states we use the etalon states located in the middle of the Co chain consisting of N = 20 atoms. The central ten magnetic moments are shown in Fig. 3. Magnetic moments rotates in XY-plane. It is also assumed that the atoms placed along the $Y$ axis.

The etalon state can not be metastable if it is located very close to the edge of the chain because it has nonvanishing thickness. If $N \geq 12$ then the first metastable etalon state is located between the 6th and 7th atoms of the chain. In other words, five possible position from each side of the chain is unstable. Thus, the number $N$ in equation (5) should be replaced by $N_{\text{eff}} = N - 10$.

![](./images/867758422076948808_4.jpg)

FIG. 4. The dependencies of the reversal time of the magnetization the Co chain on Pt(997) surface in the framework the simple kMC model [16] and the improved kMC model II. (a) The temperature dependence of the chain consisting of $N = 40$ atoms. (b) The dependence on the length of the chain at $T = 10$ K. The parameters of the Heisenberg Hamiltonian are the following: $J = 7.5$ meV and $K = 2.0$ meV.

Figure 4 shows the dependencies of the reversal time of the magnetization the Co chain on Pt(997) surface. The results of kMC simulation are averaged over 1000 remagnetisations and shown with black (the simple kMC model) and red (the improved kMC model II) points. One can see that the relaxation effect leads to drastic decrease of the reversal time of the magnetization by several orders of magnitude at $T = 4 - 30$ K (Fig 4a). In order to understand this effect let as consider the Co chain consisting of $N = 20$ atoms. The diffusion barriers for formation and disappearance of the domain wall at the edge of the chain are $E_1^D = 10.7$ meV and $E_2^D = 3.4 \cdot 10^{-3}$ meV. In the framework of the simple kMC model these events do not have diffusion barriers, and the equation (3) gives a rude estimation of the transition rates: $\nu_1 \approx \nu_0 \exp(-2J/k_{\text{B}}T)$ and $\nu_2 \approx \nu_0$. Comparing the values of $E_1^D$ and $2J = 15$ meV we conclude that the relaxation effect leads to drastic increase of the rate $\nu_1$. The rate $\nu_3$ also dramatically increases. Indeed, the diffusion barrier for transitions of the domain wall along the chain (calculated in the middle of the chain) is $E_3^D = 6.5 \cdot 10^{-3}$ meV. At the same time in the framework of the simple kMC model this barrier has a value of $K = 2.0$ meV.

The reversal time of the magnetization the Co chains linearly increases with the increase of their length (Fig 4b). It is clearly seen form the equation (6) in the case of the simple kMC model. In the frame of the improved kMC model II the following relations take place at $T = 4 - 30$ K: $\nu_1 \ll \nu_2 \approx \nu_3 \approx \nu_0$. In this case the equation (5) can be simplified as $\tau \approx N_{\text{eff}}/4\nu_1$. It is interesting to note that the factor $\eta = \tau/\tau_{\text{relaxed}}$ slightly depends on the length of the Co chain as $\eta \sim (N - 2)/(N - 10)$.

The analytical results obtained with equation (5) are presented in Fig. 4 with solid and dashed lines. In the case of the simple kMC model the equations (2) and (3) are used for calculation of the transition rates $\nu_i$, $i = 1,2,3$. In the case of the improved kMC model II we use the equation (4) with the diffusion barriers $E_1^D$, $E_2^D$, and $E_3^D$ calculated for the Co chain consisting of $N = 20$ atoms and presented above. Fig. 4 clearly shows that the analytical method gives the same results as the kMC simulations.

## IV. CONCLUSION

Summarizing the results presented above we conclude that at all parameters of the Heisenberg Hamiltonian (1) the relaxation of the magnetic moments leads to the decrease of diffusion barriers and, consequently, to the decrease of the reversal time of the magnetization. If $J \ll K$ then the relaxation effect does not influence on the possible number of metastable states of the chain. The example of such system is an antiferromagnetic Fe chain on $\text{Cu}_2\text{N}/\text{Cu}(001)$ surface. The reversal time of the magnetization of this chain decreases by factor 2-3 at $T = 4 - 7$ K. If $J \gtrsim K$, then the relaxation effect leads to the decrease of the effective length of the chain and to the appearance of clockwise and anti-clockwise states. The example of such system is the ferromagnetic Co chain on Pt(997) surface. The reversal time of the magnetization of this chain decreases dramatically by several orders of magnitude at $T = 4 - 30$ K.

The presented improved kMC models can be easily generalized on the case of nonzero external magnetic field or on the case of interaction of the atomic chain with a

STM tip. It is also very important to underline that the analytical approach [27-30] can be successfully used to estimation of the reversal time of the magnetization. The analytical method is incomparably less time-consuming than the kMC simulations, especially in the case of the improved kMC model II. A single domain-wall approxi- mation is valid in a wide range of temperatures from the very low quantum tunneling temperature [10] to the some maximal temperature which close to the critical temper- ature $(T_{max} \lesssim T_{C})$ [27]. Thus, the analytical method can be a power tool for analyzing of magnetic properties of a wide class of atomic chains.

## ACKNOWLEDGEMENTS

The research is carried out using the equipment of the shared research facilities of HPC computing resources at Lomonosov Moscow State University [39, 40]. The inves- tigation is supported by the Russian Science Foundation(Project No. 21-72-20034).

## APPENDIX. GNEB METHOD IN XY-MODEL

Let the atoms placed along the $y$-axis, $x$-axis is the easy axis of magnetization. The spherical angles $\theta_{i}$ and $\phi_{i}$ can be defined the in the following way $(s_{i}=1)$: $(s_{i})_{x}=\cos \theta_{i},(s_{i})_{y}=\sin \theta_{i} \cos \phi_{i},(s_{i})_{z}=\sin \theta_{i} \sin \phi_{i}$. According to the Heisenberg Hamiltonian (1) the mag- netic energy of the chain can by written as

$$
\begin{aligned}
E=-\sum_{i>j} J_{i j}\left(\cos \theta_{i} \cos \theta_{j}+\sin \theta_{i} \sin \theta_{j} \cos \left(\phi_{i}-\phi_{j}\right)\right) & \\
& -K \sum_{i}\left(\cos \theta_{i}\right)^{2}. \quad(7)
\end{aligned}
$$

The necessary conditions of the local extremum or the saddle point is $\partial E / \partial \phi_{i}=0, i=1, \ldots, N$. At the arbi trary $\theta_{i}$ these equations have the solution $\phi_{i}=\phi_{0}$, where $\phi_{0}$ is some constant value. The energy (7) does not de pend on $\phi_{0}$. Thus, we can choose $\phi_{0}=0$. It is so called XY-model.

In the most general case the state of a magnetic system consisting of N magnetic moments specified by 3N pa- rameters. Taking into account the conditions $s_{i}=1, i=$  $1,..., N$ one can choose a $2 ~N$ -dimensional Riemannian manifold instead of 3N-dimensional Euclidean space [32]. In the framework of XY-model the 2N-dimensional Rie- mannian manifold reduces to 1N-dimensional Rieman- nian manifold. The following description of the molec- ular statics and GNEB methods is fully analogous to Ref. [32]. However, instead of singular equations (F.3- F.6) (see [32]) we have very simple equations of a point mass motion on the 1N-dimensional Riemannian mani- fold

$$
\frac{\mathrm{d} v_{i}^{\theta}}{\mathrm{d} t}=\frac{f_{i}^{\theta}}{m}, \quad \frac{\mathrm{d} \theta_{i}}{\mathrm{~d} t}=v_{i}^{\theta},
$$

where $f_{i}^{\theta}$ and $v_{i}^{\theta}$ are projections of the $i$ th force and the $i$ th velocity on the orthogonal unit vector $e_{i}^{\theta}$ in the di rection of increasing $\theta_{i}$ , and $m$ is effective mass. As a result, the searching of metastable states and calcula- tions of diffusion barriers in the framework of XY-model are much more faster than in the general case. This is very important in the case of "on the fly" calculations.

[1] I. Zutic, J. Fabian, S. Das Sarma, Rev. Mod. Phys 76,323 (2004).
[2] N.D. Mermin, Quantum Computer Science: an Introduc- tion (Cambridge University Press, Cambridge, England),2007.
[3] S. Bose, Phys. Rev. Lett 91, 207901 (2003).
[4] H. Verma, L. Chotorlishvili, J. Berakdar, S.K. Mishra, Eur. Phys. Lett. 119, 30001 (2017).
[5] D. J. Choi, N. Lorente, J. Wiebe, K. von Bergmann, A.F. Otte, and A. J. Heinrich, Rev. Mod. Phys 91, 041001(2019).
[6] P. Gambardella, A. Dallmeyer, K. Maiti, M.C. Malagoli,W. Eberhardt, K. Kern, C. Carbone. Nature 416, 301(2002).
[7] P. Gambardella, A. Dallmeyer, K. Maiti, M.C. Malagoli, S. Rusponi, P. Ohresser, W. Eberhardt, C. Carbone, K. Kern, Phys. Rev. Lett. 93, 077203 (2004).
[8] S. Loth, S. Baumann, C.P. Lutz, D.M. Eigler, A.J. Hein- rich, Science 335, 196 (2012).
[9] S. Yan, D.-J. Choi, J.A.J. Burgess, S. Rolf- Pissarczyk, S. Loth, Nat. Nanotechnol. 10, 40 (2015).
[10] J.-P. Gauyacq, N. Lorente, J. Phys.: Condens. Matter27,455301(2015).
[11] W. Kohn, Rev. Mod. Phys. 71, 1253 (1999).
[12] H. Ebert, D. Kodderitzsch, J. Minár, Rep. Prog. Phys.74, 096501 (2011).
[13] L.D. Landau and E. Lifshitz, Phys. Z. Sowjetunion 8, 153(1935).
[14] K. Tao, O.P. Polyakov, V.S. Stepanyuk, Phys. Rev. B93, 161412(R)(2016).
[15] M.E.I. Newman, G.T. Barkema, Monte Carlo methods in statistical physics (Oxford Univ. Press, Oxford), 2001.
[16] Y. Li, B.-G. Liu, Phys. Rev. B 73, 174418 (2006).
[17] J. Li, B.-G. Liu, J. Magn. Magn. Mater. 378 186 (2015).
[18] A.S, Smirnov, N.N. Negulyaev, W. Hergert, A.M. Salet- sky, V.S. Stepanyuk, New J. Phys. 11, 063004 (2009).
[19] Y. Li, B.-G. Liu, Phys. Rev. Lett. 96, 217201 (2006).
[20] K.M. Tsysar, S.V. Kolesnikov, A.M. Saletsky, Chin.

Phys. B **24**, 097302 (2015).

[21] S.V. Kolesnikov, K.M. Tsysar, A.M. Saletsky, Phys. Solid State **57**, 1513 (2015).

[22] D.I. Bazhanov, O.V. Stepanyuk, O.V. Farberovich, V.S. Stepanyuk, Phys. Rev. B **93**, 035444 (2016).

[23] K.M. Tsysar, S.V. Kolesnikov, I.I. Sitnikov, A.M. Saletsky, Mod. Phys. Lett. B **31**, 1750142 (2017).

[24] L. Trallori, Phys. Rev. B **57**, 5923 (1998).

[25] A.P. Popov, A.V. Anisimov, O. Eriksson, N.V. Korodumova, Phys. Rev. B **81**, 054440 (2010).

[26] A.P. Popov, A. Rettori, M.G. Pini, M.G. Pini, Phys. Rev. B **92**, 024414 (2015).

[27] S.V. Kolesnikov, JETP Lett. **103**, 588 (2016).

[28] S.V. Kolesnikov, I.N. Kolesnikova, J. Exp. Theor. Phys. **125**, 644 (2017).

[29] S.V. Kolesnikov, I.N. Kolesnikova, Phys. Rev. B **100**, 224424 (2019).

[30] S.V. Kolesnikov, I.N. Kolesnikova, IEEE Magn. Lett. **10**, 2509105 (2019).

[31] R.J. Glauber, J. Math. Phys. **4**, 294 (1963).

[32] P.F. Bessarab, V.M. Uzdin, H. Jónsson, Comput. Phys. Comm. **196**, 335 (2015).

[33] L.D. Landau, E.M. Lifshitz, Electrodynamics of Continuous Media (Pergamon Press, New York, USA), 1963.

[34] G. Henkelman, H. Jónsson, J. Chem. Phys. **115**, 9657 (2001).

[35] O. Trushin, A. Karim, A. Kara, T.S. Rahman, Phys. Rev. B **72**, 115401 (2005). .

[36] S.V. Kolesnikov, A.L. Klavsyuk, A.M. Saletsky, Surf. Sci. **612**, 48 (2013).

[37] B. Puchala, M.L. Falk, K. Garikipati, J. Chem. Phys. **132**, 134104 (2010).

[38] M. Athenes, P. Bellon, G. Martin, Philos. Mag. A **76**, 565 (1997).

[39] V. Sadovnichy, A. Tikhonravov, V. Voevodin, and V. Opanasenko, Contemporary High Performance Computing: From Petascale toward Exascale (Boca Raton, United States), Chapman Hall/CRC Computational Science, Boca Raton, United States, 283307 (2013).

[40] V. Voevodin, A. Antonov, D. Nikitenko, P. Shvets, S. Sobolev, I. Sidorov, K. Stefanov, V. Voevodin, S. Zhumatiy, Supercomput. Front. Innov. **6**, 4 (2019).