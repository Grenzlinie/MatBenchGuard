# Investigation on the efficiency and accuracy of methods for calculating melting temperature by molecular dynamics simulation

YangChun Zou, ShiKai Xiang*, ChengDa Dai

National Key Laboratory for Shock Wave and Detonation Physics Research, Institute of Fluid Physics, China Academy of Engineering Physics, Mianyang 621900 Sichuan, People's Republic of China

---

## ARTICLE INFO

**Keywords:**
Melting temperature
Free energy
Nucleation

## ABSTRACT

Finding the efficient and accurate schemes to calculate the melting temperature is important for molecular dynamics simulation. We propose a modified void method based on heterogeneous nucleation to validly calculate the melting temperature from solid-liquid coexistence state. It decreases the degree of superheating in the conventional voids method. The efficiency and accuracy of five methods (i.e., hysteresis method, two phase coexistence method, the interface pinning method, the Frenkel-Ladd path method and the modified void method) have been discussed in detail. The calculated results of hysteresis method strongly depend on heating/cooling rate. For the nonequilibrium thermodynamic integration method, the calculated accuracy is consistent with the interface pinning method for monoatomic Cu. For the modified void method the calculated results agree with the nonequilibrium thermodynamic integration method.

---

### 1. Introduction

Melting temperature ($T_{\rm M}$) is one of the important properties for metal materials and is associated with the first-order phase transition [1-8]. In 1910, the Lindemann criterion has been proposed [9], which predicts melting arises when the vibration of atom reaches the limit of instability. After that, Born considered melting occurs when the shear modulus disappears [10]. Over the past few decades, many methods have been exploited to efficiently and accurately determine $T_{\rm M}$ by molecular dynamics (MD) simulation. The first approach to find melting temperature is based on observing the change of structure of system with temperature, such as hysteresis method [5,6,11], two phase coexistence method [12-15] and conventional voids method [16-21]. According to the rigid thermodynamics definition of melting temperature $G_{\rm solid}\ (P, T_{\rm M}) = G_{\rm liquid}\ (P, T_{\rm M})$, several methods, for instance the Frenkel-Ladd path method [22,23], the pseudo-supercritical path method [24-26], the interface pinning method [27,28] and the small-size solid-liquid method [29], have been developed to calculate either absolute Gibbs free energy for solid and liquid phases or free energy difference between solid and liquid [30,31]. In general, the accuracy of free energy methods is higher than direct simulation methods, but the former's procedures are more complicated.

To investigate the melting behaviour of metal materials, the most simple simulation approach is to heat solid phase until melting (HUM) [32-34]. When the volume of system changes suddenly with increasing temperature, the corresponding temperature $T_+$ is regarded as $T_{\rm M}$, but $T_+$ is always higher than melting temperature. When system is cooled from liquid to crystalline, the homologous crystallized temperature $T_-$ is lower than $T_{\rm M}$. According to classic nucleation theory (CNT) [35,36], the hysteresis phenomena (melting or crystallization) can be explained by nucleation free energy barrier. To empirically assess melting temperature by combining $T_+$ and $T_-$, hysteresis method has been established, i.e., $T_{\rm M}^{\rm hys} = T_+ + T_- - \sqrt{T_+T_-}$[5,6]. However, more simulation time is required to obtain reliable $T_+$ and $T_-$ and the accuracy of result is limited by empirical verdict without explicit thermodynamics significance.

Compared with homogeneous nucleation, the degree of hysteresis can be decreased by introducing heterogeneous interface (i.e., solid-liquid) because interface can reduce nucleation free energy barrier between solid and liquid phases [1,37]. Based on this mind, two phase coexistence methods have been developed [14,38,39]. There are at least three simulation approaches [37,40] to equilibrate solid-liquid structure. The first approach is called the constant pressure and constant temperature (NPT) simulation. The initial solid-liquid configuration is equilibrated at different temperatures and same pressure. If temperature is not $T_{\rm M}$, the final state of system is either pure solid or pure liquid, owing to the thermostat and interface. The second approach is named as the constant volume and constant temperature

---

*Corresponding author.
E-mail address: skxiang@caep.cn (S. Xiang.)

https://doi.org/10.1016/j.commatsci.2019.109156
Received 14 May 2019; Received in revised form 2 July 2019; Accepted 20 July 2019
Available online 19 October 2019
0927-0256/ © 2019 Published by Elsevier B.V.

(NVT) simulation [41]. The stress anisotropy problem ($P_{xx} \neq P_{yy} \neq P_{zz}$) may occur due to large interfacial contact stress between solid and liquid phases. Third, the solid-liquid system is performed in the constant pressure and constant enthalpy (NPH) ensemble [42]. In this way, the stress anisotropy problem will be solved since three chief components of the stress tensor can be regulated to match the given pressure [14].

The Frenkel-Ladd (FL) path method based on the thermodynamic integration [22,23,43] was used to compute free energy difference between interested system and reference system. The method assigns a specific path with coupling parameter $\lambda$ to connect Hamiltonian between interested and reference systems. The accuracy of Frenkel-Ladd path method is very precise, owing to quantitative free energy and no nucleation problem. Many previous configuration parameters should be carefully examined, for example, the size of simulation box, simulation time and integration path, to reduce integration errors.

Recently, Ulf R. Pedersen [27] proposed so-called interface pinning method. Based on fixed solid-liquid structure, it sets up a relationship between order parameter $Q(\mathbf{R})$ and chemical potential difference $\Delta \mu$ between solid and liquid at fixed pressure and temperature. The method has been successfully applied to find melting point of Lennard-Jones model. However, the method ignores the disorder of solid-liquid interface and interfacial free energy is considered as a constant. This assumption may affect the accuracy of free energy difference. Hong et al. [29] developed a small-size solid-liquid method based on the statistical probability. The free energy difference between solid and liquid phases can be extracted from the probability distribution of final pure solid and liquid at fixed temperature and pressure, i.e., $N_{liquid}/N_{solid} = \exp(-\beta G^{l-s})$, where $N_{liquid}$ and $N_{solid}$ are the numbers of thoroughgoing liquid and thoroughgoing solid in the final states, respectively. The melting temperature is ascertained as $N_{liquid}/N_{solid} = 1$. The reliability of ratio completely depends on the number of simulation.

The defects, for example interstitial, dislocation and voids, were demonstrated to be beneficial to melting [44-49] because of low free energy barrier. Based on this fact, the conventional void method has been developed. The simulation routines of conventional void method can be divided into two steps. First, create a void in cubic simulation box. Second, continuously heat the void system in the NPT ensemble. The estimated melting temperature is evaluated to be the temperature at which a discontinuous transition in system properties such as potential energy, volume or order parameter. With increasing size of void, observed melting temperature tends to a constant [26], and then the constant is regarded as the $T_M$. The procedures of this method are extremely brief and only have two steps. Nevertheless, the estimated melting temperature is observational without thermodynamics principle.

In this paper, we propose a modified void method to calculate melting temperature. Meanwhile, the efficiency and accuracy of five different methods (i.e., the hysteresis method, the two-phase coexistence method, the interface pinning method, the nonequilibrium thermodynamic integration method and the modified void method) for calculating melting temperature are compared systematically. The rest of the paper is organized as follows. The detailed methods and simulation procedures are described in Section 2. The discussions of results for five methods have been shown in Section 3.

## 2. Methods and simulation details

In this work, we have investigated monoatomic Cu with face-centered cubic (FCC) crystal and binary Ni-Zr compound with B2 phase. The interatomic interactions were given by embedded-atom method (EAM) developed by Mishin et al. [50] for Cu and Mendelev et al. [51] for Ni-Zr compound respectively. The FCC unit cell consists of four atoms with lattice constant $a_0 = 3.615$ Å The molecular dynamics simulation procedures were implemented by large-scale atomic/molecular massively parallel simulator (LAMMPS) software package [52]. The three dimensional periodic boundary conditions were deployed. The velocity-Verlet integrator was chosen as time integrator. The timestep was set to 1 femtosecond (fs). The temperature was controlled by Nosé-Hoover thermostat [53] with a damping time scale of 100 fs for the hysteresis method, two phase method, modified void method and the interface pinning method. For the nonequilibrium thermodynamic integration method, the Langevin thermostat [54] was used with same damping time. The pressure was regulated by the Parrinello-Rahman barostat [55] and relaxed in 1000 fs for the hysteresis method, two phase method, modified void method and the interface pinning method.

### 2.1. Hysteresis method

The simulation procedures consist of two steps. First, the system is gradually heated from initial temperature $T_i$ to final temperature $T_{fin}$ at fixed pressure. Subsequently, the temperature is successively cooled from $T_{fin}$ to $T_i$. In this work, $T_+$ and $T_-$ can be obtained at where the volume of system is discontinuous. The calculated melting temperature is evaluated by the estimator [6]

$$
T_{M}^{hys}=T_{+}+T_{-}-\sqrt{T_{+} T_{-}}. \tag{1}
$$

To evaluate melting temperature of Cu at ambient pressure, $15 \times 15 \times 15$ supercell with $N = 13500$ was constructed as simulation box. To study calculated accuracy, the different heating rates 100 K/ns, 800 K/ns, 1600 K/ns and 3000 K/ns were performed from $T_i = 600$ K to $T_{fin} = 1900$ K; The tactic of cooling was same as heating process. The trajectory of volume vs. temperature has been recorded for each timestep to monitor transition temperature $T_+$ and $T_-$. The melting results will be shown in Section 3.1.

### 2.2. Two-phase method

For two phase simulation, we employed a handy procedure which was presented by Vitaly et al. [37]. A rectangular parallelepiped simulation box with 16000 atoms for Cu was created. The procedures can be described as follows. First, simulation box is equilibrated at given pressure $P_n$ and estimated temperature $T_{es}$. Second, the position and velocity of half atoms along Z axis of system are fixed, and the other half atoms are heated to higher temperature $T_h$ in the $NP_{zz}$ T ensemble. Third, high temperature atoms are cooled from $T_h$ to $T_{es}$ in the $NP_{zz}$ T ensemble. Fourth, whole system is allowed to relax in the NPH ensemble at $P_n$. If the final state is solid-liquid coexistence configuration, calculated $T_M$ can be extracted from the statistical temperature. Otherwise, repeat above simulation procedures.

The dependence of calculated melting temperature on finite size has been explored for Cu, i.e., $N = 1000, 2000, 4116, 8000, 12,000$ and 16,000. The estimated temperatures $T_{es}$ and $T_h$ were set to 1400 K and 1800 K, respectively. The "flying ice cube" problem [56] can be solved by subtracting the center of mass velocity of system in each timestep in this study. The instantaneous temperature at fourth stage was recorded for each timestep. It is interesting to attend to the relation between the accuracy of calculated melting temperature and computational effort. The standard deviation

$$
\sigma=\sqrt{\frac{\sum_{i=1}^{M}\left(T_{i}-\langle T\rangle\right)^{2}}{M}} \tag{2}
$$

was used to assess the relation with various sampling steps $M$ with different system sizes. Twenty independent two-phase simulations were implemented. The melting temperature of binary Ni-Zr compound with B2 phase has also been computed by this method.

### 2.3. Interface pinning method

The solid-liquid configuration at given pressure and temperature can be pinned by introducing a additional harmonic potential into system, i.e., $U_{add}(R)=\frac{k}{2}[Q(R)-b]^{2}$, where $k$ is the spring constant, $Q(R)$ is the global order parameter, and $b$ is the anchor constant. The new potential of solid-liquid system $U'$ can be written as [27]

$$
U'(R)=U(R)+\frac{k}{2}[Q(R)-b]^{2}, \tag{3}
$$

where $U(R)$ is the original potential. Based on an assumption that the free energy of interface is independent of interfacial position and shape, the chemical potential difference $\Delta \mu$ at given temperature and pressure under $U(R)$ can be calculated by [28]

$$
\Delta \mu_{s-l}=-\frac{k \Delta Q}{N}\left[\langle Q\rangle^{\prime}-b\right], \tag{4}
$$

where $\langle Q\rangle^{\prime}$ is the statistical average under $U'(R)$, $\Delta Q=Q_{s}-Q_{l}$, $Q_{s}$ and $Q_{l}$ are order parameter of pure solid and pure liquid under $U(R)$ respectively and $b=\frac{Q_{s}-Q_{l}}{2}$. We configured $Q(R)=|N^{1 / 2} \sum_{m=1}^{N} \exp (-i h \cdot R_{m})|$, where $N$ is the number of particle, $h$ is wave vector and $R_{m}$ is the position of $m$th particle. For a $x \times y \times z$ ($x=y<z$) supercell, the simulation steps of calculating $\Delta \mu$ can be described as follows: (1) compute lattice constant $a_{s}$ for solid at given pressure and temperature in the NPT ensemble; (2) determine $Q_{s}$ and $Q_{l}$ with $h=\begin{pmatrix}\frac{4 \pi}{a_{s}}, 0,0\end{pmatrix}$ in the $NP_{zz} T$ ensemble when lattice constant of supercell is $a_{s}$; (3) create a solid-liquid structure with lattice constant $a_{s}$ along $x$ and $y$ directions and simulate the system in the $NP_{zz} T$ ensemble to obtain $\langle Q\rangle^{\prime}$ under $U'(R)$. In terms of Eq. (4), $\Delta \mu$ can be obtained.

In order to examine the impact of tortuous interface on calculated accuracy, different orthorhombic supercells, i.e., $5 \times 5 \times 10$, $10 \times 10 \times 20$, $10 \times 10 \times 40$, $20 \times 20 \times 80$, have been examined at 1500 K and ambient pressure for Cu. The value of $k$ was chosen as the half of the number of crystal plane along $z$ axis. Once $\Delta \mu$ is achieved, the melting temperature can be found by iteration of temperature $T^{(j+1)}=T^{(j)}+\frac{\Delta \mu^{(j)}}{\Delta s^{(j)}}$ until $T^{(j+1)}=T^{(j)}$ at given pressure, where $\Delta s$ is the entropy difference between solid and liquid. The efficiency of finding melting temperature was checked with different initial temperatures, i.e., 1400 K, 1500 K and 1600 K. For copper, the melting entropy is about $1.2 k_{B}$, which indicates that an error of 0.1 meV/atom in $\Delta \mu$ can cause an error of $\sim 1$ K estimated melting temperature [57]. Hence, estimated melting temperature was found when $\Delta \mu$ converged to 0.0001 eV/atom. The standard deviation of $Q$ was treated as statistical error. Ten independent simulation procedures for this method have been performed. The melting temperature of binary Ni-Zr compound with B2 phase has also been computed.

### 2.4. Nonequilibrium thermodynamic integration (NETI) method

The Gibbs free energy $G$ as a function of temperature $T$ with constant pressure $P$ can be depicted in terms of the Gibbs-Helmholtz equation [31]

$$
\frac{G(P, T)}{T}-\frac{G_{i}\left(P, T_{i}\right)}{T_{i}}=-\int_{T_{i}}^{T} \frac{\langle H\rangle_{N P T}}{T^{2}} d T, \tag{5}
$$

where $T_{i}$ is an interested temperature, $H$ is the enthalpy, and $\langle\ldots\rangle_{N P T}$ denotes the NPT ensemble average. The melting temperature $T_{M}$ is determined at where $G_{\text {solid }}(P, T_{M})=G_{\text {liquid }}(P, T_{M})$. At the right of Eq. (5), the integrations for solid and liquid are easily calculated, respectively, by following steps: first, perform a set of NPT ensemble simulations to get the enthalpy $\langle H\rangle_{N P T}$ with different temperatures and constant pressure; second, fit these $\langle H\rangle_{N P T}$ values as a second-order function of temperature $T$, i.e., $H(T)=c_{2} T^{2}+c_{1} T+c$.

Subsequently, the free energy $G_{i}$ can be expressed as

$$
G_{i}=F_{i}\left(V, T_{i}\right)+P V, \tag{6}
$$

where $F_{i}$ is the Helmholtz free energy and $V$ is the volume. In general, through a linear Hamiltonian-interpolation path associated with a coupling parameter $\lambda$ the Hamiltonian of system $\mathrm{H}(\lambda)$ changes from the interested Hamiltonian $\mathrm{H}_{i}$ to the reference Hamiltonian $\mathrm{H}_{r}$, i.e.,

$$
\mathrm{H}(\lambda)=(1-\lambda) \mathrm{H}_{i}+\lambda \mathrm{H}_{r}, \tag{7}
$$

where $\lambda$ is from 0 to 1. Along this path, the Helmholtz free energy difference $\Delta F$ between $F_{i}$ corresponding to the $\mathrm{H}_{i}$ (i.e., $\lambda=0$) and $F_{r}$ corresponding to the $\mathrm{H}_{r}$ (i.e., $\lambda=1$) at same thermodynamics state can be estimated by equilibrium thermodynamic integration method [58], i.e.,

$$
\Delta F=W_{r e v}=F_{r}-F_{i}=\int_{\lambda=0}^{\lambda=1}\left\langle\frac{\partial H}{\partial \lambda}\right\rangle_{\lambda} d \lambda, \tag{8}
$$

where $\langle\ldots\rangle_{\lambda}$ denotes the canonical ensemble average at specific coupling parameter $\lambda$, $\frac{\partial H}{\partial \lambda}=\mathrm{H}_{r}-\mathrm{H}_{i}$ is the so-called driving-force, and $W_{r e v}$ is the reversible work.

Nevertheless, in this work, an efficient nonequilibrium thermodynamic integration strategy was utilized to estimate free energy difference $\Delta F$ [59]. The estimator [60]

$$
\Delta F=W_{r e v}=\overline{W}_{i r r e v}-\overline{W}_{d i s}, \tag{9}
$$

where

$$
W_{i r r e v}=\int_{0}^{t_{s}} d t \frac{d \lambda(t)}{d t}\left(\frac{\partial H}{\partial \lambda}\right)_{\lambda(t)}, \tag{10}
$$

with $\overline{W}_{i r r e v}$ is the averaged irreversible work and $\overline{W}_{d i s}$ is the averaged dissipated, in which $\lambda(t)$ continuously switches with time $t$ from 0 to $t_{s}$. A valid function form for $\lambda(t)$ has been defined in Refs. [61]. If $\lambda$ (from 0 $\rightarrow 1$ and $1 \rightarrow 0$) switches slowly with time so that the change of state of system close to quasi-static process, according to the linear response theory, $\overline{W}_{d i s}^{0 \rightarrow 1}=\overline{W}_{d i s}^{1 \rightarrow 0}$. Hence, the $F$ is calculated by [60]

$$
\Delta F=F_{r}-F_{i}=W_{r e v}=\frac{1}{2}\left(\overline{W}_{i r r e v}^{0 \rightarrow 1}-\overline{W}_{i r r e v}^{1 \rightarrow 0}\right), \tag{11}
$$

where $\overline{W}_{i r r e v}^{0 \rightarrow 1}$ is the average forward irreversible work ($\lambda$ $0 \rightarrow 1$) and $\overline{W}_{i r r e v}^{1 \rightarrow 0}$ is the backward irreversible work ($\lambda$ $0 \rightarrow 1$). Combined with Eq. (6) and (11), $G_{i}$ can be written as

$$
G_{i}\left(P, T_{i}\right)=F_{r}-\frac{1}{2}\left(\overline{W}_{i r r e v}^{0 \rightarrow 1}-\overline{W}_{i r r e v}^{1 \rightarrow 0}\right)+P V. \tag{12}
$$

To calculate free energy of solid phase, the Frenkel-ladd method [22] was implemented to switch the intersted system to the Einstein crystal, i.e., $\mathrm{H}_{r}=\mathrm{H}_{E}=\sum_{i=1}^{N} \frac{p_{i}}{2 m}+\frac{1}{2} \varkappa \sum_{i=1}^{N}\left(r_{i}-r_{i 0}\right)^{2}$, where $r_{i}$ and $p_{i}$ are position and momentum of particle $i$ respectively, and $\varkappa$ is the spring constant. The free energy of Einstein crystal has been analysed [62]. Recently, a novel Uhlenbeck-Ford model (UFM) [63,64] has been demonstrated that it is a convenient reference system for liquid phase. The UF model is defined as

$$
U_{\mathrm{UF}}=-\frac{p}{\beta} \ln \left(1-e^{-\left(\frac{r}{\sigma}\right)^{2}}\right), \tag{13}
$$

where $\beta=\left(k_{B} T\right)^{-1}$, $\sigma$ is a scale parameter, $r$ is an inter-particle distance, and $p$ is a scaling factor that controls the strength of interactions. The free energy of UFM can be written as

$$
F_{\mathrm{UFM}}=F_{i g}+F_{e x c}, \tag{14}
$$

where $F_{i g}$ is the ideal-gas free energy and $F_{e x c}$ is the excess free energy. The $F_{e x c}$ can be represented as

$$
F_{\mathrm{UFM}}^{e x c}\left(x, T\right)=k_{B} T \sum_{n=1}^{\infty} \frac{\widetilde{B}_{n+1}(p)}{n} x_{n}, \tag{15}
$$

where $x = b\rho$, $\rho$ is the number density of system, $b=\frac{1}{2}(\pi\sigma^{2})^{3/2}$, and the $\widetilde{B}_{n+1}(p)$ are reduced virial coefficients. The free energy of ideal-gas has been analysed [65] and a set of precise values $F_{\text{UFM}}^{\text{exc}}$ have been calculated for $p = 1, 25, 50, 75$ and 100 with $x$ from 0 to 4 [63]. Therefore, the UF liquid model was chosen as reference system of liquid phase in this study.

To evaluate the efficiency and accuracy of this method, we calculated melting temperature of Cu at ambient pressure $P = 1$ atm. A FCC simulation box with $N = 4000$ atoms was established. A series of independent NPT ensemble simulations were implemented with the Nosé-Hoover thermostat and the Parrinello-Rahman barostat. For solid, the range of temperature was from 900 to 1500 K with 20 K interval; for liquid, the range was from 1200 to 1700 K. For each NPT simulation, the simulation time was set as 100 ps. On the other hand, the interested temperatures $T_{i}$ for solid and liquid were set as 1000 K and 1600 K, respectively. The choices of spring constant $\kappa$ of Einstein crystal and $p$ and $\sigma$ of UF model have been discussed in Section 3.4. The cutoff for UF liquid model was set as $4\sigma$. Switching processes ($\lambda0 \to 1$ and $1 \to 0$) were performed in the NVT ensemble. To keep system with zero total linear momentum in switching process, the Langevin thermostat was employed [60]. A set of switching time $t_{s}=0.1, 0.2, 0.3, 0.4, 0.6, 0.8$ and 1 ns (ns) were implemented. To obtain average irreversible work of solid and liquid, respectively, twenty independent switching processes for both forward and backward directions were performed. The melting temperature of binary Ni-Zr compound with B2 phase has also been estimated.

### 2.5. Modified void method

For the conventional void method, the simulation routines can be described as following steps: first, create a cubic simulation box with a void. second, heat void system in the NPT ensemble until melting, and then monitor the change of the volume of system with temperature. As the volume of system suddenly changed with temperature, the corresponding temperature $T_{c}$ is regarded as estimated melting temperature. Considering size-effect of void the final estimated melting temperature is obtained at where $T_{c}$ doesn't vary with increasing size of void. We noticed that the result of melting temperature is completely based on empirical observation without specified thermodynamics basis.

Generally, a void is conductive to lowering the nucleation free energy barrier (e.g. solid $\to$ liquid), and it means that nucleation rate will rise. Hence, we proposed so-called modified void method based on heterogeneous nucleation to validly calculate melting temperature from solid-liquid coexistence state. The initial configuration, a rectangular parallelepiped ($L_{x}=L_{y}<L_{z}$) FCC supercell is constructed. The simulation procedures can be divided into three steps: first, a perfect lattice with a given initial temperature runs in the NPH ensemble until equilibrium; second, create a cubic void by deleting atoms from the center of simulation box; third, the void system is continuously performed in the NPH ensemble to obtain equilibrium state. The advantage of the NPH ensemble is that the three chief components of stress tensor can be regulated to match the given pressure. Usually, the equilibrium state of system may has three types (i.e., solid phase, solid-liquid coexistence phase or liquid phase). If the enthalpy of system is proper, steady solidliquid coexistence phase can be achieved.

In order to identify final configuration of system, a bond orientational order parameter $Q_{l}$ based on spherical harmonic function was implemented to distinguish the atom whether solid profile or liquid profile [7]. The range of the $Q_{l}$ is from 0 to 1. The spherical harmonic order parameters is defined as [66]

$$
\bar{Y}_{l m}=\frac{1}{n n n} \sum_{j=1}^{n n n} Y_{l m}\left[\theta\left(r_{i j}\right), \varphi\left(r_{i j}\right)\right],
\tag{16}
$$

where $nnn$ is the number of nearest neighbors, $Y_{lm}$ is the spherical harmonics function and the angles $\theta$ and $\varphi$ are the standard spherical polar angles defining the direction of the bond vector $\mathbf{r}_{ij}$. The bond orientational order parameter $Q_{l}$ for per atom is defined as

$$
Q_{l}=\sqrt{\frac{4 \pi}{2 l+1} \sum_{m=-l}^{m=l} \bar{Y}_{l m} \bar{Y}_{l m}^{*}},
\tag{17}
$$

where $l(1,2,...,n)$ is degree and $m = -l,...,0,...,l$. Here, we chose $Q_{6}(l = 6)$ as the specific local order parameter formula because it has good performance in the supercooled regime [27,67].

The impact of void and simulation box size on estimated melting temperature has been researched. We constructed $5 \times 5 \times 40$ FCC unit cells of Cu with different void sizes $1 \times 1 \times 1$ (14 atoms), $2 \times 2 \times 2$ (63 atoms) and $3 \times 3 \times 3a_{0}^{3}$ (172 atoms). In order to evaluate finite size effect, various simulation boxes $5 \times 5 \times 10$, $5 \times 5 \times 40$ and $5 \times 5 \times 80$ simulation boxes with 63 void atoms were examined. The estimated melting temperature $T_{\text{M}}$ was obtained from last 100 ps. The relationship between the efficiency of nucleation and the orientation of void has been investigated, i.e., $[100] \times [010] \times [001]$, $[110] \times [\overline{1}10] \times [001]$, $[100] \times [03\overline{1}] \times [013]$, $[11\overline{2}] \times [1\overline{1}0] \times [111]$, $[4\overline{7}1] \times [2\overline{1}1] \times [113]$ orientations. The time-dependent average order parameter of atom $Q_{6}$ was utilized to monitor formation of liquid. Ten independent simulations for modified void method were performed.The melting temperature of binary Ni-Zr compound with B2 phase has also been achieved by this method. The results have been displayed in Section 3.5.

## 3. Results and discussions

### 3.1. The melting temperature from hysteresis method

The relationships between the volume of per atom $V$ and instantaneous temperature $T$ with different heating-cooling rates at ambient pressure are plotted in Fig. 1. As shown Fig. 1, observational $T_{+}$ increases with increasing heating rate, nevertheless, $T_{-}$ dramatically drops. For 100 K/ns rate loop process, the discontinuity of heating and cooling $V$ are observed at ~1602 K and ~890 K with ~20 K errors, respectively. However, for 3000 K/ns rate loop, $T_{+} \sim 1640$ K is higher than 1602 K, and $T_{-} \sim 611$ K is lower than 890 K. The detailed parameters are listed in Table 1. These results show that the observed transition temperature strongly depends on heating/cooling rate. In fact, the heating/cooling processes are nonequilibrium. Whether melting or crystallization requires enough time to absorb or release energy to nucleation. Higher rate results in lower energy transmission between system and thermostat and significant hysteresis effect. Compared with estimated temperature 1239 K for $t_{total}=0.9$ ns, the estimated temperature increases with increasing simulation time. The estimated temperature 1295 K with walltime 60.3 h is slightly improved

![](./images/812718903720411137_1.jpg)

Fig. 1. The volume-temperature hysteresis loops with different heating/cooling rates at ambient pressure for monoatomic Cu.

<table><caption>Table 1
The observed up-bound temperature $T_+$ (K) and low-bound temperature $T_-$ (K), estimated melting temperatures $T_{\text{M}}^{\text{cs}}$ (K), total simulation time $t_{\text{total}}$ (ns) and walltime (hours) with 16 CPU cores with different heating/cooling rates (K/ns) with errors for monoatomic Cu.</caption>
<thead>
<tr>
<th>Rate</th>
<th>$T_+$</th>
<th>$T_+$</th>
<th>$T_{\text{M}}^{\text{cs}}$</th>
<th>$t_{\text{total}}$</th>
<th>walltime</th>
</tr>
</thead>
<tbody>
<tr>
<td>100</td>
<td>1602</td>
<td>890</td>
<td>1295 $\pm$ 20</td>
<td>26</td>
<td>56.8</td>
</tr>
<tr>
<td>800</td>
<td>1621</td>
<td>803</td>
<td>1284 $\pm$ 30</td>
<td>3.3</td>
<td>7.2</td>
</tr>
<tr>
<td>1600</td>
<td>1633</td>
<td>733</td>
<td>1273 $\pm$ 30</td>
<td>1.8</td>
<td>3.8</td>
</tr>
<tr>
<td>3000</td>
<td>1640</td>
<td>611</td>
<td>1239 $\pm$ 30</td>
<td>0.9</td>
<td>2</td>
</tr>
</tbody>
</table>

related to 1284 K with walltime 7.5 h. These results indicate that the convergence of accuracy is limited by empirical observation even with more simulation time. Although the procedure of hysteresis method is handy, the calculated accuracy is naturally low. Hence, the estimated melting temperature only can be as a rough reference to $T_{\text{M}}$ for monoatomic. For binary Ni-Zr compound, we have used 800 K/ns heating/cooling rate to perform hysteresis method with $N = 3456$. However, we have not observed discontinuous volume and solidification in the cooling process (Supplementary Material Fig. S1). It suggests that this method can't capture complicated interactions of Ni-Zr system. Thus, the empirical hysteresis formula is not suitable for multi-composition system.

### 3.2. The melting temperature from two phase method

The calculated melting temperatures of different system sizes with NVE and NPH ensembles are exhibited in Fig. 2(a). For both NVE and NPH ensembles, the calculated melting temperature decreases with increasing the number of atom. When $N < 8000$, the calculated temperature for NVE ensemble is obviously different with NPH. Nevertheless, when $N > 8000$, the difference becomes small and the calculated melting temperature converges to ~1324 K. It indicates that the impact of different ensembles on calculated melting temperature can be solved with large system size.

In order to evaluate relationship between calculated accuracy and efficiency, the dependence of statistical errors on simulation time and system size are displayed in Fig. 2(b). The standard deviation of system $N = 1000$ is quickly drops with time from 0.05 ns to 0.15 ns and then converges to ~32. For $N = 16000$, the value of standard deviation converges to ~7.8 as simulation time $> 0.7$ ns. We found that $\sigma(T)$ decreases with increasing system size and the corresponding convergence rate drops. In general, small system has large statistical errors owing to large fluctuation of interface. For large system, small statistical errors were achieved due to small interfacial influence. The calculated accuracy is mainly limited by interfacial size and simulation time. The cost of walltimes is ~1.2 h with 0.7 ns timesteps for $N = 8000$ and ~2.8 h with 0.7 ns for $N = 16000$, respectively. These results demonstrate that calculated efficiency of two phase mainly yields to system size. The melting temperature of Ni-Zr compound with B2 phase has also been calculated. Compared with monoatomic Cu, more simulation time was required to achieve equilibrium configuration for binary system. We have estimated the melting temperature ~1403 $\pm$11 K from last 0.2 ns with total simulation time 2 ns.

### 3.3. The melting temperature from interface pinning method

The convergence of chemical potential difference related to size of interface and simulation box has been summarized in Table 2. For $5 \times 5 \times 10$, the statistical order parameter $Q' = 10.5732$ with $k = 5$ and for $k = 10$, $Q' = 10.5554$. It shows the final structure of system for two different $k$ is similar. However, the corresponding chemical potential difference 0.0158071 eV/atom for $k = 5$ is about half of $k = 10$. For $k = 20$, the $Q'$ and $\Delta\mu$ are 10.6825 and 0.0163 eV/atom respectively. To understand these results, we checked the final steady configurations for different $k$. The initial solid-liquid configuration can not be pinned and turns into pure liquid phase for $k = 5$ and 10; for $k = 20$, coexsitence phase is pinned. As shown in Fig. 3, for small system, the fluctuation of interfacial atom is intense and the interfacial distance is short. The small anchor constant $k$ can not restrict the fluctuation of interface. The solid-liquid interface easily overlap each other and then vanish. The disappearance of interface will lead to enormous errors for estimating chemical potential difference. With the area of solid-liquid interface and interfacial distance increasing, the change of $\Delta\mu$ converges to 0.001 eV/atom. The result indicates that the dependence of interface free energy on disordered interface can be reduced by creating larger interfacial area, as shown in Fig. 3. The calculated accuracy of the interface pinning method yields finite-size effect. The other error of $\Delta\mu$ comes from statistical deviation of $Q'c$. The standard deviation $\sigma(Q')$ was examined and is less than ~0.002, which suggests that the error of chemical potential difference is ~0.0005 eV/atom, and the errors of estimated melting temperature is $\sim \pm 5$ K.

![](./images/812718903720411137_2.jpg)

Fig. 2. (a) Calculated melting temperature versus the system size for monoatomic Cu. (b) Convergence of the standard deviation of temperature $\sigma$ ($T$) versus simulation time and system size for monoatomic Cu.

The efficiency of finding melting temperature has been investigated in $N = 16000$ system. The chemical potential difference $\Delta\mu$ between solid and liquid as a function of temperature with different initial temperatures has been plotted in Fig. 4. The results show that the final temperature tend to ~1315 K, and $\Delta\mu$ converges to 0.0001 eV/atom for different initial temperatures. With initial temperatures 1400 K and 1500 K, one iteration step was implemented. However, with 1600 K

<table>
<caption>Table 2
The parameters calculated by interface pinning method with different system sizes at 1500 K and ambient pressure for monoatomic Cu.</caption>
<thead>
<tr>
<th>Box size</th>
<th>$k$(eV/Å²)</th>
<th>$a_s$(Å)</th>
<th>$N$</th>
<th>$Q_s$</th>
<th>$Q_l$</th>
<th>$\Delta Q$</th>
<th>$b$</th>
<th>$\langle Q\rangle'$</th>
<th>$\Delta\mu$ (eV/atom)</th>
<th>time (ns)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$5 × 5 × 10$</td>
<td>5</td>
<td rowspan="3">3.727</td>
<td rowspan="3">1000</td>
<td rowspan="3">22.5151</td>
<td rowspan="3">1.0738</td>
<td rowspan="3">21.4413</td>
<td rowspan="3">10.72065</td>
<td>10.5732</td>
<td>0.0158071</td>
<td>0.38</td>
</tr>
<tr>
<td>10</td>
<td>10.5551</td>
<td>0.0354950</td>
<td>0.38</td>
</tr>
<tr>
<td>20</td>
<td>10.6825</td>
<td>0.0163576</td>
<td>0.38</td>
</tr>
<tr>
<td>$10 × 10 × 20$</td>
<td>20</td>
<td>3.727</td>
<td>8000</td>
<td>63.3108</td>
<td>0.9728</td>
<td>62.3380</td>
<td>31.169</td>
<td>31.0599</td>
<td>0.0170037</td>
<td>0.54</td>
</tr>
<tr>
<td>$10 × 10 × 40$</td>
<td>40</td>
<td>3.727</td>
<td>16000</td>
<td>87.696</td>
<td>0.9823</td>
<td>86.7137</td>
<td>43.3569</td>
<td>43.277</td>
<td>0.0173139</td>
<td>0.83</td>
</tr>
<tr>
<td>$20 × 20 × 80$</td>
<td>80</td>
<td>3.727</td>
<td>128000</td>
<td>247.707</td>
<td>0.9068</td>
<td>246.8002</td>
<td>123.4001</td>
<td>123.286</td>
<td>0.0175989</td>
<td>0.96</td>
</tr>
</tbody>
</table>

![](./images/812718903720411137_3.jpg)

Fig. 3. The impact of disordered interface on interfacial free energy. The green and blue circles denote solid particle and liquid particle, respectively.

![](./images/812718903720411137_4.jpg)

Fig. 4. The efficiency for finding melting temperature with different initial temperatures for Cu. $\Delta\mu$ is the chemical potential difference between solid and liquid.

initial temperature we executed two iteration steps to obtain $\Delta\mu = 0.0003$ eV/atom at 1316.5 K. It indicates that using the iteration strategy is efficient to find melting temperature. The cost of walltime to perform one iteration step is $\sim$2.4 h with 16 CPU cores and $N = 16000$. For binary Ni-Zr system with $N = 6144$ and $k = 40$ eV/Å², the estimated melting temperature is $\sim$1392 $\pm$ 5 K at ambient pressure, and this result agrees with the two phase method, as shown in Table 4. On the other hand, owing to the ignored contributions of disordered interface to free energy, it may result in overestimating melting temperature for binary system.

### 3.4. The melting temperature from nonequilibrium thermodynamic integration (NETI) method

As shown in Fig. 5 (a), the fitted enthalpy as a second-order function of temperature $T$ for monoatomic Cu at ambient pressure has been plotted. The fitted parameters $c_2$, $c_1$ and $c$ are $5.23\text{E}-8$ eV/K², $1.87\text{E}-4$ eV/K and $-3.508$ eV for solid phase and $-1.35\text{E}-8$ eV/K², $3.75\text{E}-4$ eV/K and $-3.517$ eV for liquid phase. For solid, the spring constant of Einstein crystal $\varkappa$ has been optimized by $3k_BT/\langle(\Delta r)^2\rangle$, in which $\langle(\Delta r)^2\rangle$ is the mean-square displacement (MSD) of interested system. The MSD and optimized $\varkappa$ are $0.087$ Å² and $2.97$ eV/Å² at $T = 1000$ K and $P = 1$ atm, respectively. These parameters make the fluctuation of the driving force $\frac{\partial H}{\partial\lambda}$ as small as possible and avoid appearance of first order phase transition in the switching process. For liquid, the effects of $p$ and $\sigma$ on driving force have been shown in Fig. 5 and Fig. 6(d). The results show that $p = 25$ makes the UF model too soft, and forces the particles close to each other. It will result in the divergence of driving force near $\lambda = 1$. At $p = 50$ and 100, this problem can be eliminated, and the variation of driving force is smooth over the entire interval $\lambda$. Similarly, if the length scale $\sigma$ is too small, the divergence issue comes out, as shown in Fig. 6(d). For this case, a reasonable value for the $\sigma$ is $2.0$ Å, and it shows a slowly varying driving force. Thus, corresponding cutoff for UF liquid model was set as $8$ Å. Combined with above discussions, the $p$ and $\sigma$ were chosen as 50 and $2.0$ Å, respectively, and it gives a smooth fluctuation of the driving force with coupling parameter $\lambda$.

![](./images/812718903720411137_5.jpg)

Fig. 5. The fitted enthalpy of per atom as a function of temperature based on $H(T) = c_2T^2 + c_1T + c$: (a) for monoatomic Cu; (b) for binary Ni-Zr compound.

The systematic errors and statistical errors using non-equilibrium approach along forward and backward directions have been investigated. According to thermodynamics principle, the forward free energy ($\lambda$ 0 to 1) is regarded as a lower bound of Gibbs free energy, and backward is an upper bound (1 to 0). The average $\frac{\partial H}{\partial\lambda}$ as a function of $\lambda$ for $t_s = 0.2$ ns are exhibited in Fig. 6(d) and Fig. 6(b) for solid and liquid, respectively. The results suggest that upper bound of free energy close to lower bound. It means that free energy can be located in a extremely narrow range with minor errors. Generally, the systematic errors mainly come from limited length of simulation time, and statistical errors come from limited simulation times. To reduce statistical errors, each free energy was calculated by averaging twenty independent switching processes for forward and backward directions. As shown in Fig. 7(a), the forward $\mu(1000\text{K},1\text{atm}) = -3.93219$ eV/atom, and backward $\mu = -3.93202$ eV/atom with $t_s = 0.2$ ns for solid. The free energy difference $\mu_{\text{FB}}$ between forward and backward directions converges to 0.001 eV/atom. In Fig. 7(b), the $\mu_{\text{FB}}$ converges to 0.0001 eV/

![](./images/812718903720411137_6.jpg)

Fig. 6. (a) and (b) are the averaged driving force $\frac{\partial H}{\partial \lambda}$ as a function of $\lambda$ with switching time 0.2 ns using nonequilibrium thermodynamic integration strategy for solid and liquid for monoatomic Cu, respectively. (c) Driving force $\frac{\partial H}{\partial \lambda}$ as a function of $\lambda$ for different values $p$ with $\sigma=2 \mathring{A}$ for monoatomic Cu. (d) Driving force $\frac{\partial H}{\partial \lambda}$ as a function of $\lambda$ for different values $\sigma$ with $p=50$ for monoatomic Cu.

![](./images/812718903720411137_7.jpg)

Fig. 7. Convergence of Gibbs free energy using nonequilibrium thermodynamic integration method to compute chemical potential $\mu$ with different switching time $t_{s}$ at $P=1$ atm for monoatomic Cu: (a) for solid at $T=1000$ K; (b) for liquid at $T=1600$ K. The systematic error introduced by the dissipation inherent of the nonequilibrium approach is easily eliminated by averaging the results of the forward and backward switching. The dash line denotes the average Gibbs free energy obtained from $t_{s}=1$ ns.

![](./images/812718903720411137_8.jpg)

Fig. 8. Calculated Gibbs free energy of per atom $G$ as a function of temperature for both solid and liquid: (a) for monoatomic Cu; (b) for binary Ni-Zr compound.

atom for liquid. With increasing $t_{s}$, the value of $\mu_{\mathrm{FB}}$ becomes small for both solid and liquid. The results indicate that systematic errors can be effectively reduced by increasing switching time. In addition, the arithmetic average values of free energy between forward and backward directions were computed for $t_{s}=0.1,0.2,0.3,0.4,0.6,0.8$ and 1 ns. The change of average free energy is small and converges to 1E-5 eV/ atom with $t_{s}$ from 0.2 ns to 1 ns. It indicates that using arithmetic average value is valid to reduce statistical errors and systematic errors for the nonequilibrium thermodynamic integration method. The average strategy utilizes less switching time to obtain accurate free energy results. Using switching time $t_{s}=0.2$ ns is enough to obtain accurate free energy for both solid and liquid. The Gibbs free energy of per atom as a function of temperature for Cu has been shown in Fig. 8(a). The corresponding melting temperature is determined at $\sim 1316 \pm 3$ K with systematic errors and statistical errors. This result is consistent with the interface pining method $1315 \pm 5$ K. For nonequilibrium thermodynamic integration method, the degree of fluctuation of the driving force is mainly factor which impacts on calculated accuracy for free energy. Because it determines the accuracy of integration. The calculated efficiency mainly depends on reference systems. For the Einstein crystal, the total cost of walltime is ~22 min for each switching process (both forward and backward directions) with 16 CPU cores. For the UF liquid model, the walltime is ~1 h. The estimated melting temperature calculated from this method successfully avoids

![](./images/812718903720411137_9.jpg)

Fig. 9. (a) The equilibrium temperature $T_{\mathrm{E}}$ as a function of the enthalpy of per atom $H_{\mathrm{p}}$ for the $5 \times 5 \times 40$ FCC unit cells with $2 \times 2 \times 2 a_{0}^{3}$ cubic void at ambient pressure for monoatomic $\mathrm{Cu}$, and the error bar denotes the statistical error. (b) Comparison of estimated melting temperatures with different sizes of cubic void $L \times L \times L a_{0}^{3}$ for conventional void method and modified void method for monoatomic $\mathrm{Cu}$.

nucleation problem compared with hysteresis method. The fitted enthalpy as a second-order function of temperature $T$ for binary Ni-Zr at ambient pressure has been shown in Fig. 7(b). The corresponding Gibss free energy as a function of temperature $T$ is displayed in Fig. 8(b), and the melting temperature has been determined at $\sim 1351 \pm 3 \mathrm{~K}$.

### 3.5. The melting temperature from modified void method

A perfect FCC lattice $5 \times 5 \times 40$ ( $N=4000$ atoms) system with $2 \times 2 \times 2 a_{0}^{3}$ cubic void (63 atoms) at different initial temperatures and ambient pressure have been investigated by the modified void method. The relationship of the enthalpy of per atom $H_{\mathrm{p}}$ and equilibrium temperature $T_{\mathrm{E}}$ is shown in Fig. 9(a). The standard deviation is regarded as statistical error. Apparently, the profiles of $T_{\mathrm{E}}-H_{\mathrm{p}}$ can be divided into three stages. First, $T_{E}$ monotonically increase with $H_{\mathrm{p}}$ until $H_{\mathrm{p}}$ $\sim-3.15 \mathrm{eV} /$ atom; next, the profile of curve becomes rather flat; finally, $T_{\mathrm{E}}$ slightly drops and grows with $H_{\mathrm{p}}$ increasing. The equilibrium properties of system are related to structure of system. In view of tendency of $T_{\mathrm{E}}-H_{\mathrm{p}}$, the structure of system is solid atomic configuration for initial stage; the structure is solid-liquid coexistence state for flat stage; for final stage, the structure is liquid state. As shown in Fig. 9(b), the estimated melting temperatures of conventional void method are always higher than modified void method with different sizes of void. When volume of system changed suddenly, the structure of system changed from solid phase to complete liquid phase with conventional void method. In this case, the system needs a higher temperature to get enough energy to melt. However, the modified void method can successfully achieve intermediate phase (i.e., solid-liquid coexistence state).

To further examine structure profile for final stage, we plotted the order parameter and density number profile along $Z$ axis at $(-3.11 \mathrm{eV} /$ atom, $1328 \mathrm{~K})$ point, as shown in Fig. 10. Ordinarily, the atomic density number fluctuates with large amplitude in solid phase, while it fluctuates with relatively small amplitude in liquid phase. The green line fluctuates intensely from $21 \AA$ to $92 \AA$ along $Z$ axis. Moreover, the profile of order parameter $Q_{6}$ is presented by slicing system along $Z$ axis. The order parameter is $\sim 0.48$ from $22 \AA$ to $90 \AA$ and is $\sim 0.37$ in the rest region. The results are consistent with density number profile.

According to heterogeneous melting theory [68], the void can lower nucleation free energy barrier and benefit to form liquid nucleation.

![](./images/812718903720411137_10.jpg)

Fig. 10. The profile of density number and order parameter $Q_{6}$ vs. the distance along $Z$ axis at $1 \mathrm{~ns}$ with $\left(H_{\mathrm{p}}, T_{\mathrm{E}}\right)=(-3.11 \mathrm{eV} /$ atom, $1328 \mathrm{~K})$ for $\mathrm{Cu}$.

The NPH ensemble has been used since it can ensure final state with isotropic stress along three chief direction (i.e., $P_{x x}=P_{y y}=P_{z z}$ ) [69]. The quantity of enthalpy determines the ratio of solid phase over liquid phase. Consequently, the calculated melting temperature is ascertained by averaging $T_{\mathrm{E}}$ from flat stage and is $\sim 1327 \pm 14 \mathrm{~K}$ at ambient pressure. The result is in accordance with two phase method and the nonequilibrium thermodynamic integration method.

To investigate the impact of finite size of void on $T_{\mathrm{E}}$, different cubic void sizes were created in the $5 \times 5 \times 40$ system. In Fig. 11(a), $T_{\mathrm{E}}$ monotonously increases with $H_{\mathrm{p}}$ from -3.16 to $-3.11 \mathrm{eV} /$ atom for $1 \times 1 \times 1$ void. It means system maintains solid configuration. However, solid-liquid phase is achieved for $2 \times 2 \times 2$ and $3 \times 3 \times 3$ void systems. At $H_{\mathrm{p}}=-3.11 \mathrm{eV} /$ atom, $T_{\mathrm{E}}=1458 \mathrm{~K}$ for $1 \times 1 \times 1$ void system is higher than $1327 \mathrm{~K}$ for $3 \times 3 \times 3$. Small void is hard to be liquid nucleation because of higher nucleation free energy barrier. It is noteworthy that $2 \times 2 \times 2$ (only 63 defect atoms) void system validly explore solid-liquid field of materials as soon as possible without superheating.

Different system sizes with same cubic void were researched, as shown in Fig. 11(b). The width of flat region for $5 \times 5 \times 10$ system is more narrow than $5 \times 5 \times 40$ and $5 \times 5 \times 80$. For $H_{\mathrm{p}} \sim-3.07 \mathrm{eV} /$ atom, $T_{\mathrm{E}}=1215 \mathrm{~K}$ for $5 \times 5 \times 10$ system is lower than $1330 \mathrm{~K}$ for $5 \times 5 \times 80$ system. The structures for $5 \times 5 \times 10$ and $5 \times 5 \times 80$ are liquid and solid-liquid phases, respectively. In small system size, the distances between interfaces are very short and thermal fluctuation of atom is large. Therefore, interfaces are easy to overlap with each other, and then solid-liquid phase turns into supercooling liquid. In reality, the problem attributes to finite size. For $5 \times 5 \times 40$ system, it is enough to solve this case. In the light of above results, we suggest that the ratio between void size over system size is round $1.5 \%$.

Understanding how to create void to efficiently lower the free energy barrier is important. Different orientations of void have been constructed, as shown in Fig. 12. The volume of cubic void is $738 \AA^{3}$. The average order parameter of atom versus simulation time has been recorded. In Fig. 13, different orientation void systems undergo three processes: nucleation, growing and equilibrium. In Fig. 13(a), the time of forming a critical nucleus is $\sim 9$ ps. While, for $[11 \overline{2}] \times[1 \overline{1} 0] \times[111]$ void orientation the time is minimum $\sim 5$ ps. For $[100] \times[03 \overline{1}] \times[013]$ orientation, the nucleation time has max value $\sim 19$ ps. The increment of potential energy $3.58 \mathrm{eV} /$ atom along $[11 \overline{2}] \times[1 \overline{1} 0] \times[111]$ is less than $3.85 \mathrm{eV} /$ atom along $[100] \times[010] \times[001]$ orientation. Generally, a void is primarily a matter of affecting the entropy. For FCC structure, $\{111\}$ crystal plane is the close packed plane. As void orientation is along $[11 \overline{2}] \times[1 \overline{1} 0] \times[111]$, the contribution of void to the entropy is maximum corresponding to the lowest free energy barrier and the least nucleation time. These results show that the height of free energy barrier is associated with the orientation of void. The melting temperature of binary Ni-Zr compound has also been examined with 20 deleted atoms for $N=6144$ by the modified void method. We successfully obtained estimated melting temperature $\sim 1398 \pm 10 \mathrm{~K}$ with

![](./images/812718903720411137_11.jpg)

Fig. 11. (a) Comparison of the equilibrium temperature $T_{\mathrm{E}}$ as a function of the enthalpy of per atom $H_{\mathrm{p}}$ for the system $5 \times 5 \times 40$ FCC unit cells with different void sizes $(1 \times 1 \times 1,2 \times 2 \times 2$ and $3 \times 3 \times 3 a_{0}^{3})$. (b) Comparison of the equilibrium temperature $T_{\mathrm{E}}$ as a function of the enthalpy of per atom $H_{\mathrm{p}}$ for different simulation boxes $(5 \times 5 \times 10,5 \times 5 \times 40$ and $5 \times 5 \times 80$ FCC unit cells) with same cubic void $2 \times 2 \times 2 a_{0}^{3}$. The black dot line indicates a sketch to infinite system.

![](./images/812718903720411137_12.jpg)

Fig. 12. The schematic diagram for creating different orientations of cubic void by rotating void around center point.

equilibrium solid-liquid coexistence state. This result is consistent with two phase method and interface pinning method.

The comparison for calculated melting temperatures and corresponding calculated efficiency of five methods for monoatomic Cu have been summarized in Table 3. For the hysteresis method, much simulation time was need to improve accuracy of $T_{+}$and $T_{-}$. It originates from observational transition temperatures and empirical formula. Two phase method creates an interface between solid and liquid. It effectively reduces the free energy barrier. The calculated accuracy and efficiency are limited by system size. The fluctuation of solid-liquid interface may result in statistical errors. Compared with the hysteresis method, two phase method is more accurate due to steady solid-liquid coexistence phase. The interface pinning method displays a high calculated accuracy and efficiency due to accurate free energy difference. Using large simulation box effectively lower the impact of wiggly interface on free energy. For each simulation, The cost of walltime is only $2.4 \mathrm{~h}$ with total simulation time $0.83 \mathrm{~ns}$. The calculated errors of free energy difference is less than $\sim 0.0005 \mathrm{eV} /$ atom which corresponds to $\pm 5 \mathrm{~K}$. Using optimized integration parameters and path can avoid nucleation process and reduce integration error for nonequilibrium thermodynamic integration method. Combined with nonequilibrium simulation and average strategy, the calculated efficiency is extremely improved. Using $0.2 \mathrm{~ns}$ switching time is enough to obtain chemical potential difference $0.0001 \mathrm{eV} /$ atom at $T=1316 \mathrm{~K}$. This result is consistent with the interface pinning method $1315 \mathrm{~K}$. Table 3 shows that efficiency of nonequilibrium thermodynamic integration method is slightly higher than the interface pinning method. The modified void

![](./images/812718903720411137_13.jpg)

Fig. 13. The average order parameter $Q_{6}$ of atom versus time along different void orientations.

<table><thead><tr><th>Method</th><th>N</th><th>W</th><th>ttotal</th><th>walltime</th><th>TM</th></tr></thead><tbody><tr><td>hysteresis</td><td>13500</td><td>10</td><td>260</td><td>568</td><td>1295 ± 30</td></tr><tr><td>two phase</td><td>8000</td><td>20</td><td>14</td><td>56</td><td>1324 ± 15</td></tr><tr><td>interface pinning</td><td>16000</td><td>10</td><td>8.3</td><td>24</td><td>1315 ± 5</td></tr><tr><td>NETI</td><td>4000</td><td>20</td><td>24.8</td><td>30.2</td><td>1316 ± 3</td></tr><tr><td>modified void</td><td>3937</td><td>10</td><td>20</td><td>13.4</td><td>1327 ± 12</td></tr></tbody></table>

Table 3
The number of particle $N$, the independent simulation times $W$, the total simulation time $t_{total}(\mathrm{ns})$, the total walltime (hours) with 16 CPU cores and calculated melting temperature $T_{\mathrm{M}}(\mathrm{K})$ at ambient pressure for different methods for Cu.

<table><caption>Table 4
The number of particle $N$, the independent simulation times $W$, the total simulation time $t_{total}$(ns), the total walltime (hours) with 16 CPU cores and calculated melting temperature $T_M$ (K) at ambient pressure for different methods for binary Ni-Zr compound with B2 phase.</caption>
<thead>
<tr>
<th>Method</th>
<th>$N$</th>
<th>$W$</th>
<th>$t_{total}$</th>
<th>walltime</th>
<th>$T_M$</th>
</tr>
</thead>
<tbody>
<tr>
<td>hysteresis</td>
<td>3456</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>two phase</td>
<td>6144</td>
<td>10</td>
<td>20</td>
<td>70</td>
<td>$1403\pm11$</td>
</tr>
<tr>
<td>interface pinning</td>
<td>6144</td>
<td>10</td>
<td>14</td>
<td>40</td>
<td>$1392\pm5$</td>
</tr>
<tr>
<td>NETI</td>
<td>3456</td>
<td>10</td>
<td>12.75</td>
<td>28</td>
<td>$1351\pm3$</td>
</tr>
<tr>
<td>modified void</td>
<td>6084</td>
<td>10</td>
<td>20</td>
<td>68</td>
<td>$1398\pm10$</td>
</tr>
</tbody>
</table>

method can validly obtain melting temperature ~1327 K. The calculated efficiency has been promoted compared with two phase method.

The estimated melting temperatures of binary Ni-Zr compound for different methods have been listed in Table 4. Due to long diffusion time to solidification for binary system, it is difficult to observe discontinuous volume with limited simulation time. Hence, the empirical hysteresis formula is not suitable to Ni-Zr system. The calculated melting temperatures of two phase method, interface pinning method and modified void method are consistent with each other. The $T_M = 1351\pm3$ K calculated from nonequilibrium thermodynamic integration method is slightly less than above three methods. For the modified void method, the cost of walltime is 6.8 h with 2 ns and $N = 6084$ for one simulation. Its calculated efficiency closes to two phase method, but is higher than interface pinning method and nonequilibrium thermodynamic integration. The nonequilibrium thermodynamic integration exhibits the highest calculated efficiency among five methods.

## 4. Conclusions

In this paper, we have systematically compared the efficiency and accuracy of calculating melting temperature among five methods (i.e., hysteresis method, two phase method, the nonequilibrium thermodynamic integration method, the interface pinning method and the modified void method). The accuracy of hysteresis is the lowest due to empirical formula and observed $T_+$ and $T_-$. It is not suitable to binary system. For two phase method, the stress tensor of interface may result in anisotropic pressure in small size system. The interface pinning method may be wrong in the small system due to intense interfacial fluctuation. For monoatomic Cu, the influence of wiggle interface on free energy can be ignored by using large system. Nevertheless, this method may overestimate melting temperature for binary Ni-Zr compound due to noticeable wiggle of interface. The nonequilibrium thermodynamic integration method directly calculates free energy difference between solid and liquid phases. The optimal integration parameters effectively avoid presence of the first-order phase transition in the switching process. Combined with forward and backward simulation directions, the calculated accuracy has been promoted. This method is suitable to monoatomic Cu and binary Ni-Zr compound. We have proposed a modified void method based on heterogeneous nucleation to validly calculate the melting temperature. The modified void method displays high efficiency to calculate melting temperature for Cu. It utilizes void to decrease free energy barrier to fast get liquid nucleus and achieve the steady solid-liquid coexistence phase. For Ni-Zr compound, more simulation time was needed to obtain equilibrium distribution of Zr and Ni atoms. We have also explored the relationship between nucleation efficiency and the orientation of void for Cu. The least nucleation time ~5 ps was observed along $[1\overline{1}2]\times[1\overline{1}0]\times[111]$ orientation.

### CRediT authorship contribution statement

YangChun Zou: Formal analysis, Investigation, Writing - original draft.
ShiKai Xiang: Conceptualization, Writing - review & editing
ChengDa Dai: Funding acquisition, Project administration.

### Conflict of interest

The authors declare that there is no conflict of interests regarding the publication of this article.

### Acknowledgments

This research was supported by grants from the Development Foundation of China Academy of Engineering Physics (No. 2015B0101004), the Science Challenge Project (No. TZ2016001), the National Natural Science Foundation of China (No. 11602251), and the NSAF Foundation (No. U1730248). The authors wish to thank M. I. Mendelev for useful discussions.

### Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, athttps://doi.org/10.1016/j.commatsci.2019.109156.

### References

[1] A.B. Belonoshko, N.V. Skorodumova, A. Rosengren, B. Johansson, Phys. Rev. B 73 (2006) 012201.
[2] R. Cahn, Nature 413 (2001) 582.
[3] B.J. Siwick, J.R. Dwyer, R.E. Jordan, R.J.D. Miller, Science (New York, N.Y.) 302 (2003) 1382.
[4] Z.H. Jin, P. Gumbsch, K. Lu, E. Ma, Phys. Rev. Lett. 87 (2001) 055703.
[5] L. Zheng, Q. An, Y. Xie, Z. Sun, S.N. Luo, J. Chem. Phys. 127 (2007) 164503.
[6] S.N. Luo, A. Strachan, D.C. Swift, J. Chem. Phys. 120 (2004) 11640.
[7] A. Samanta, M. Tuckerman, T. Yu, E. Weinan E, Science 346 (2014) 729.
[8] D.S. Ivanov, L.V. Zhigilei, Phys. Rev. Lett. 98 (2007) 195701.
[9] F.A. Lindemann, Phys. Z 11 (1910) 609.
[10] M. Born, J. Chem. Phys. 7 (1939) 591.
[11] Y.W. Tang, J. Wang, X.C. Zeng, J. Chem. Phys. 124 (2006) 236103.
[12] J.R. Morris, C.Z. Wang, K.M. Ho, C.T. Chan, Phys. Rev. B 49 (1994) 3109.
[13] E. Schwegler, M. Sharma, F. Gygi, G. Galli, Proc. Natl. Acad. Sci. 105 (2008) 14779.
[14] J. Wang, S. Yoo, J. Bai, J.R. Morris, X.C. Zeng, J. Chem. Phys. 123 (2005) 036101.
[15] S.V. Starikov, V.V. Stegailov, Phys. Rev. B 80 (2009) 220104.
[16] S. Alavi, D.L. Thompson, Mol. Simul. 32 (2006) 999.
[17] P.M. Agrawal, B.M. Rice, L. Zheng, G.F. Velardez, D.L. Thompson, J. Chem. Phys. B 110 (2006) 5721.
[18] S. Alavi, D.L. Thompson, J. Chem. Phys. 122 (2005) 154704.
[19] H. Feng, J. Zhou, Y. Qian, J. Chem. Phys. 135 (2011) 144501.
[20] Y. Zhang, E.J. Maginn, J. Chem. Phys. 136 (2012) 144116.
[21] P.M. Agrawal, B.M. Rice, D.L. Thompson, J. Chem. Phys. 118 (2003) 9680.
[22] D. Frenkel, A.J.C. Ladd, J. Chem. Phys. 81 (1984) 3188.
[23] D. Alfè, G.D. Price, M.J. Gillan, Phys. Rev. B 65 (2002) 165118.
[24] G. Grochola, J. Chem. Phys. 120 (2004) 2122.
[25] D.M. Eike, J.F. Brennecke, E.J. Maginn, J. Chem. Phys. 122 (2005) 014115.
[26] D.M. Eike, E.J. Maginn, J. Chem. Phys. 124 (2006) 164503.
[27] U.R. Pedersen, F. Hummel, G. Kresse, G. Kahl, C. Dellago, Phys. Rev. B 88 (2013) 094101.
[28] U.R. Pedersen, J. Chem. Phys. 139 (2013) 104102.
[29] Q.J. Hong, A. van de Walle, J. Chem. Phys. 139 (2013) 094114.
[30] D. Alfè, Phys. Rev. B 79 (2009) 060101.
[31] M.S. Sellers, M. Lisal, J.K. Brennan, Phys. Chem. Chem. Phys. 18 (2016) 7841.
[32] S.C. Wang, G.M. Zhang, H.F. Liu, H.F. Song, J. Chem. Phys. 138 (2013) 134101.
[33] Z.Y. Zeng, C.E. Hu, L.C. Cai, X.R. Chen, F.-Q. Jing, J. Chem. Phys. 109 (2011) 043503.
[34] Z.L. Liu, L.C. Cai, X.R. Chen, F.Q. Jing, Phys. Rev. B 77 (2008) 024103.
[35] M. Volmer, A. Weber, Phys. Chem. 119 (1926) 277.
[36] R. Becker, W. Döring, Ann. Phys. 416 (1935) 719.
[37] V.S. Dozhdikov, A.Y. Basharin, P.R. Levashov, J. Chem. Phys. 137 (2012) 054502.
[38] D. Alfè, Phys. Rev. Lett. 94 (2005) 235701.
[39] D. Buta, M. Asta, J.J. Hoyt, J. Chem. Phys. 127 (2007) 074703.
[40] D.C. Rapaport, The Art of Molecular Dynamics Simulations, Cambridge University Press, 1997.
[41] S.W. Watt, J.A. Chisholm, W. Jones, S. Motherwell, J. Chem. Phys. 121 (2004) 9565.
[42] A. Laio, S. Bernard, G. Chiarotti, S. Scandolo, E. Tosatti, Science (New York, N.Y.) 287 (2000) 10270.
[43] D. Frenkel, B. Smit, Understanding Molecular Simulation: From Algorithms to Applications, Academic Press, San Diego, 2002.
[44] S.F. Edwards, M. Warner, Philos. Mag. 40 (1979) 257.
[45] R. Lipowsky, Phys. Rev. Lett. 57 (1986) 2876.

[46] G. Ciccotti, M. Guillopé, V. Pontikis, Phys. Rev. B 27 (1983) 5576.

[47] E.V. Safonova, Y.P. Mitrofanov, R.A. Konchakov, A.Y. Vinogradov, N.P. Kobelev, V.A. Khonik, J. Phys.: Condensed Matter 28 (2016) 215401.

[48] R.W. Cahn, Nature 323 (1986) 668.

[49] A. Alsayed, M. Islam, J. Zhang, P. Collings, A. Yodh, Science (New York, N.Y.) 309 (2005) 1207.

[50] Y. Mishin, M.J. Mehl, D.A. Papaconstantopoulos, A.F. Voter, J.D. Kress, Phys. Rev. B 63 (2001) 224106.

[51] S.R. Wilson, M.I. Mendelev, Philos. Mag. 95 (2015) 224.

[52] S. Plimpton, J. Comput. Phys. 117 (1995) 1. [link]. http://lammps.sandia.gov.

[53] G.J. Martyna, D.J. Tobias, M.L. Klein, J. Chem. Phys. 101 (1994) 4177.

[54] T. Schneider, E. Stoll, Phys. Rev. B 17 (1978) 1302.

[55] M. Parrinello, A. Rahman, J. Appl. Phys. 52 (1981) 7182.

[56] C.H. Stephen, K.Z.T. Robert, E.C. Thomas, J. Comput. Chem. 19 (1998) 726.

[57] L.F. Zhu, B. Grabowski, J. Neugebauer, Phy. Rev. B 96 (2017) 224202.

[58] M. de Koning, A. Antonelli, S. Yip, Phys. Rev. Lett. 83 (1999) 3973.

[59] M. de Koning, A. Antonelli, Phys. Rev. B 55 (1997) 735.

[60] R. Freitas, M. Asta, M. de Koning, Comput. Matt. Sci. 112 (2016) 333.

[61] M. de Koning, A. Antonelli, Phys. Rev. E 53 (1996) 465.

[62] C. Vega, E. Sanz, J.L.F. Abascal, E.G. Noya, J. Phys.: Condensed Matter 20 (2008) 153101.

[63] L.R. Paula, R. Freitas, R. Azevedo, K.M. De, J. Chem. Phys. 145 (2016) 50.

[64] R.P. Leite, P.A. Santos-Flárez, M.D. Koning, Phys. Rev. E 96 (2017) 032115.

[65] R. Paula Leite, M. de Koning, Comput. Matt. Sci. 159 (2019) 316.

[66] P.J. Steinhardt, D.R. Nelson, M. Ronchetti, Phys. Rev. B 28 (1983) 784.

[67] W. Mickel, S.C. Kapfer, G.E. Schröder-Turk, K. Mecke, J. Chem. Phys. 138 (2013) 044501.

[68] P.M. Winkler, G. Steiner, A. Vrtala, H. Vehkamäki, M. Noppel, K.E.J. Lehtinen, G.P. Reischl, P.E. Wagner, M. Kulmala, Science 319 (2008) 1374.

[69] S. Yoo, X.C. Zeng, J.R. Morris, J. Chem. Phys. 120 (2004) 1654.