# Monte Carlo study of the spin-glass phase of the site-diluted dipolar Ising model

Juan J. Alonso¹,*\ and Julio F. Fernández²,†

¹Física Aplicada I, Universidad de Málaga, 29071 Málaga, Spain
²Instituto de Ciencia de Materiales de Aragón, CSIC–Universidad de Zaragoza, 50009 Zaragoza, Spain

(Received 15 October 2009; revised manuscript received 16 January 2010; published 11 February 2010)

By tempered Monte Carlo simulations, we study site-diluted Ising systems of magnetic dipoles. All dipoles are randomly placed on a fraction $x$ of all $L^3$ sites of a simple cubic lattice, and point along a given crystalline axis. For $x_c < x \leq 1$, where $x_c \simeq 0.65$, we find an antiferromagnetic phase below a temperature which vanishes as $x \to x_c$ from above. At lower values of $x$, we find an equilibrium spin-glass (SG) phase below a temperature given by $k_B T_{sg} \simeq x \varepsilon_d$, where $\varepsilon_d$ is a nearest-neighbor dipole-dipole interaction energy. We study (a) the relative mean-square deviation $\Delta_q^2$ of $|q|$, where $q$ is the SG overlap parameter and (b) $\xi_L/L$, where $\xi_L$ is a correlation length. From their variation with temperature and system size, we determine $T_{sg}$. In the SG phase, we find (i) the mean values $\langle |q| \rangle$ and $\langle q^2 \rangle$ decrease algebraically with $L$ as $L$ increases, (ii) double peaked, but wide, distributions of $q/\langle |q| \rangle$ appear to be independent of $L$, and (iii) $\xi_L/L$ rises with $L$ at constant $T$ but extrapolations to $1/L \to 0$ give finite values. All of this is consistent with quasilong-range order in the SG phase.

DOI: 10.1103/PhysRevB.81.064408
PACS number(s): 75.10.Nr, 75.10.Hk, 75.40.Cx, 75.50.Lk

## I. INTRODUCTION

The collective behavior of spin systems in which magnetic dipole-dipole interactions dominate has become the subject of considerable attention. These systems are rare in nature, although some ferroelectrics,¹ and magnetic crystals such as $LiHoF_4$, an insulating magnetic salt, have been known for decades to be well described by models of magnetic dipoles.²⁻⁴ Much of the renewed interest in systems of interacting dipoles comes from the experimental realization of magnetic nanoparticle⁵ arrays⁶,⁷ and of crystals of organometallic molecules.⁸ In these systems, particles up to some thousand Bohr magnetons behave as single spins. When closely packed in crystalline arrangements, dipolar interactions between them may induce magnetic ordering.⁷,⁹

Anisotropy also plays an important role in ordering dipolar systems. The barrier energies $E_a$ that must be overcome by spins in order to reverse their direction are often somewhat larger than the relevant dipolar energies $E_d$. Then, collective effects can be observed when thermal energies are not sufficiently large to completely freeze spins directions. Their main effect is then to force spins to point up or down along the easy magnetization axis.¹⁰ Crystalline Ising dipolar systems (IDSs) are then reasonable models.² These systems are clearly frustrated since two different dipoles give rise to magnetic fields at any given site that are not in general collinear. Not surprisingly, IDSs are very sensitive to their spatial arrangement. Early work by Luttinger and Tisza established which type of magnetic order arises at low temperature for IDSs in each of the cubic lattices.¹¹ More recently, we have obtained similar results by much simpler methods.¹² For instance, BCC-like and $LiHoF_4$-like crystals are ferromagnetic ordered but antiferromagnetic (AF) order obtains on simple cubic (SC) lattices. Competition between different interactions brings about a more exotic magnetic order, known as “spin ice,”¹³ in diamond crystals.

Whether disorder in IDSs, together with the geometric frustration that comes with the dipolar interactions give rise to a thermodynamic spin-glass (SG) phase, is an interesting question.¹⁴ Many experiments¹⁵ as well as numerical simulations¹⁶ have shown that assemblies of classical magnetic moments placed at random, such as in frozen ferrofluids and diluted ferroelectric materials, exhibit the time-dependent behavior, such as nonexponential relaxation and aging,¹⁷ that is expected from SGs. However, search for evidence for the existence of an equilibrium SG phase has been hampered by the extremely slow relaxation that is inherent to these systems. In recent papers, we have given numerical evidence that supports the existence of an equilibrium SG phase in IDSs with randomly oriented axes both in fully occupied¹⁸ and in partially occupied SC lattices.¹⁹

Site dilution is a rather simple way to introduce disorder in experimental realizations of IDS. Some early attempts to find a SG phase in $Eu_xSr_{1-x}S$ led to negative results.²⁰ By far the most scrutinized system for the last two decades has been $LiHo_xY_{1-x}F_4$. In it, magnetic $Ho^{3+}$ ions are substituted, with little distortion, by nonmagnetic $Y^{3+}$ ions.³ A strong uniaxial anisotropy forces all spins to point up or down along the same axis at low temperatures. This parallel-axis-dipolar (PAD) system orders ferromagnetically a low-temperature phase above $x_c \simeq 0.25$. Below $x_c$, transitions from a paramagnetic to a SG phase have been reported,²¹⁻²³ but the opposite conclusion, that no such transition takes place, has been reached in Ref. 24. The issue is further obscured by quantum effects that may take place at $x \ll 1$.²⁵

Theoretical results suggest that diluted PAD models undergo a SG transition at low concentrations. An earlier study of bond-diluted Ising systems with long-range interactions (including the dipolar case) found that SG order may exist at low temperatures in the limit of weak concentration.²⁶ Mean-field calculations for site-diluted PAD systems in FCC and BCC lattices predicted a SG phase for concentrations $0 < x < x_c$ where $x_c$ is the value above which ferromagnetic order ensues.²⁷ More recently, Edwards-Anderson- (EA-) type²⁸ models with power-law decaying interactions $J_{ij} \sim 1/r_{ij}^\sigma$ have been studied.²⁹,³⁰ A one-dimensional Ising spin-glass model has been found to have a nonzero temperature SG phase transition for $\sigma < 1$.³⁰ A three-dimensional (3D) Ising system

<table><caption>Table I. Spin-glass transition temperature for PAD systems. NIL is entered where a transition has been concluded not to take place. For LiHo$_x$Y$_{1-x}$F$_4$, we let $d$=5.175 Å, hence the mean number of spins in volume $d^3$ is $n_d$=1.926$x$ [since unit cells of LiHoYF$_4$ are 5.175$\times$5.175$\times$10.75 Å$^3$ large and have four Ho ions each (Ref. 3)]; furthermore, $\varepsilon_d$=0.214 K (Ref. 34). On simple cubic lattices, we let $d=a$, hence $n_d$=$x$. $\chi_3$ is the nonlinear susceptibility, and $\nu$ is the critical exponent for the correlation length.</caption>
<tr><th colspan="6">On LiHoYF$_4$-type lattices</th></tr>
<tr><td>Ref.</td><td>Method</td><td>$x$</td><td>$n_d\varepsilon_d$ (K)</td><td>$k_BT_{sg}/n_d\varepsilon_d$</td><td>$\nu$</td></tr>
<tr><td>21</td><td>$\chi_3$</td><td>0.167</td><td>0.069</td><td>1.9</td><td></td></tr>
<tr><td>22</td><td>$\chi_3$</td><td>0.045</td><td>0.019</td><td>2.3</td><td></td></tr>
<tr><td>23</td><td>$\chi_3$</td><td>0.167</td><td>0.069</td><td>3.1</td><td></td></tr>
<tr><td>24</td><td>$\chi_3$</td><td>0.165</td><td>0.068</td><td>NIL</td><td></td></tr>
<tr><td>24</td><td>$\chi_3$</td><td>0.045</td><td>0.019</td><td>NIL</td><td></td></tr>
<tr><td>31</td><td>MC</td><td>0.06</td><td>0.025</td><td>NIL</td><td></td></tr>
<tr><td>31</td><td>MC</td><td>0.12</td><td>0.049</td><td>NIL</td><td></td></tr>
<tr><td>32</td><td>MC</td><td>0.125</td><td>0.052</td><td>1.8</td><td>1.3</td></tr>
<tr><td>32</td><td>MC</td><td>0.0625</td><td>0.026</td><td>1.6</td><td>1.3</td></tr>
<tr><th colspan="6">On simple cubic lattices</th></tr>
<tr><td>Ref.</td><td>Method</td><td>$x$</td><td></td><td>$k_BT_{sg}/n_d\varepsilon_d$</td><td>$\nu$</td></tr>
<tr><td>33</td><td>MC</td><td>0.045, 0.12, 0.20</td><td></td><td>NIL</td><td></td></tr>
<tr><td>Here</td><td>MC</td><td>0.35</td><td></td><td>1.0(1)</td><td>0.95</td></tr>
<tr><td>Here</td><td>MC</td><td>0.20</td><td></td><td>1.0(1)</td><td>0.95</td></tr>
</table>

with Ruderman-Kittel-Kasuya-Yosida interactions (that decay with $1/r_{ij}^3$) have been predicted to lie in the same universality class as the 3D Ising Edwards-Anderson model with short-range interactions. $^{29}$

Numerical methods have provided conflicting answers to the question of the existence of a SG phase in site-diluted PAD models. Biltmo and Henelius$^{31}$ have calculated that the ferromagnetic phase of LiHo$_x$Y$_{1-x}$F$_4$ extends down to $x$$\simeq$0.24 but found no SG phase at low temperatures for $x$$<$$x_c$. $^{31}$ This is in contradiction with another Monte Carlo (MC) simulation for the same system that finds a SG transition for concentrations $x$=0.065 and 0.125. $^{32}$ Numerical work has also been done on a PAD model on a SC lattice, using a Wang-Landau MC method. $^{33}$ No transition was found for $x$$\leq$0.2.

Here we also simulate a PAD model on a SC lattice. Our justification for working with a SC lattice is as follows. Whereas such systems order AF in fully occupied SC lattices, $^{11,12}$ instead of ferromagnetically, as in the LiHoY$_4$ lattice, the physics of PAD systems is not expected to depend on lattice structure for $x$$\ll$1. A continuum should then lead to the same behavior. Furthermore, rescaling distance $r$ as $r$$\rightarrow$$r/\rho^{1/3}$, where $\rho$ is the spatial density of spins, is no different from redefining dipolar energies by $\varepsilon_d$$\rightarrow$$\rho\varepsilon_d$, since dipolar interactions decay as $r^{-3}$. Now, consider $k_BT_{sg}/n_d\varepsilon_d$ for any lattice structure, where $k_B$ is Boltzmann's constant, $T_{sg}$ is the SG transition temperature, $n_d$ is the number of magnetic dipoles within a $d^3$ volume, and $\varepsilon_d$ is the smallest possible dipolar energy two parallel dipoles that are a distance $d$ apart can have. Clearly, $k_BT_{sg}/n_d\varepsilon_d$ must be independent of lattice structure for $x$$\ll$1. This enables us to compare results for SC and LiHoF$_4$ lattices, or any other lattice, for $x$$\ll$1. Such a comparison is made in Table I.

The main aim of this paper is to find, by means of MC simulations, whether an equilibrium SG phase exists in site-diluted systems of dipoles, which are placed at random on the sites of a SC lattice and point up or down along a chosen principal axis. Since in the limit of low-concentrations details of the lattice are expected to become irrelevant, our results have direct connection with the experimental and numerical work mentioned above. In this regard, we follow along the lines of Ref. 32. But we aim to go further. It is our purpose to also find whether the SG phase of the PAD model behaves marginally, that is, it has quasilong-range order [as the $XY$ model$^{35}$ in two-dimensional (2D)], or whether it has spatially-extended states, $^{36}$ as in the droplet$^{37}$ and replica-symmetry-breaking$^{38}$ pictures of the SG phase.

The plan of the paper is as follows. In Sec. II we define the model, give details on how we apply the parallel tempered Monte Carlo (TMC) algorithm, $^{39}$ in order to get equilibrium results. We also define the quantities we calculate, including the spin overlap$^{28}$ $q$, and $\xi_L$, often referred to as a "correlation length."$^{40-42}$ In Sec. III we give results for the dipolar AF phase we obtain for $x$$>$$x_c$, where $x_c$$\simeq$0.65, as well as for its nature and boundary. In Sec. IV, we give numerical results we have found for (i) $q$ distributions and (ii) $\xi_L/x$ within the following $x$ and $T$ ranges, $0.2\leq$$x$$<$0.65 and $0.6x\leq$$T$$\leq$1.5$x$. In Sec. V A we examine the evidence we have in favor of the existence of a paramagnetic to SG phase transition when $x$$<$$x_c$, and find that the transition

temperature is given by $k_BT_{sg}\simeq x\varepsilon_d$, where $\varepsilon_d$ is a nearest- neighbor dipole-dipole interaction energy which is defined in Sec. II. In order to study the nature of the SG phase, we examine the following evidence in Sec. V B: (i) the mean values $\langle|q|\rangle$ and $\langle q^2\rangle$ decrease algebraically with $L$ as $L$ increases, (ii) double-peaked, but wide, distributions of $q/\langle|q|\rangle$ appear to be independent of $L$, and (iii) $\xi_L/L$ rises with $L$ at constant $T$ but extrapolates to finite values as $1/L\rightarrow0$. We provide a specific example of spatial correlation functions which decay algebraically with distance but lead to $\xi_L/L$ curves that spread out with $L$ (for finite values of $L$) as $T$ decreases below $T_{sg}$, in rough agreement with our MC results for $\xi_L/L$. All of this is consistent with quasilong-range order in the SG phase. In Sec. V C we find the best pair of values for $T_{sg}$ and $\nu$, to have curves $\xi_L/L$ for various values of $L$ collapse onto a single curve if plotted vs $(T/T_{sg}-1)L^{1/\nu}$ over the $T>T_{sg}$ range. The values given in Table I are obtained.

## II. MODEL, METHOD, AND MEASURED QUANTITIES

### A. Model

We consider site-diluted systems of Ising magnetic dipoles on a SC lattice. All dipoles point along the $z$ axis of the lattice. Each site is occupied with probability $x$. The Hamiltonian is given by
$$
\mathcal{H}=\frac{1}{2}\sum_{ij}T_{ij}\sigma_i\sigma_j, \tag{1}
$$
where the sum is over all occupied sites $i$ and $j$ except $i=j$, $\sigma_i=\pm1$ on any occupied site $i$
$$
T_{ij}=\varepsilon_a(a/r_{ij})^3(1-3z_{ij}^2/r_{ij}^2), \tag{2}
$$
where $r_{ij}$ is the distance between $i$ and $j$ sites, $z_{ij}$ is the $z$ component of $r_{ij}$, $\varepsilon_a$ is an energy, and $a$ is the SC lattice constant. In the following we give all temperatures and energies in terms of $\varepsilon_a/k_B$ and $\varepsilon_a$, respectively. Hence, $k_BT/n_a\varepsilon_a=T/x$ from here on.

This model is clearly an Ising model with long-range interactions where bond strengths $T_{ij}$ are determined by the dipole-dipole terms. Note that $T_{ij}$ signs are not distributed at random but depend only on the orientation of vectors $\mathbf{r}_{ij}$ on a SC lattice. This is to be contrasted with a *random-axes* dipolar (RAD) model, (Ref. 18) in which Ising dipoles point along directions $\mathbf{n}_i=(n_i^\alpha,\alpha=1,2,3)$ that are chosen at random by sorting two independent random numbers for each site, introducing randomness on bond strengths $T_{ij}^{\alpha\beta}$. This is why PADs exhibit AF order at high concentration in contrast with RADs, that do not. $^{18}$

### B. Method

We use periodic boundary conditions (PBC). As is usual for PBC, think of a periodic arrangement of replicas that span all space beyond the system of interest. These replicas are exact copies of the Hamiltonian and of the spin configuration of the system of interest. Details of the PBC scheme we use can be found in Ref. 12. We let a spin on site $i$ interact through dipolar fields with all spins within an $L$ $\times L\times L$ cube centered on it. No interactions with other spins are taken into account. This introduces an error which we show in Appendix to vanish as $L\rightarrow\infty$, regardless of whether the system is in the paramagnetic, AF or SG phase. There is, therefore, no effect on the thermodynamic limit of the system of interest here. (The result we obtain in Appendix is not applicable to an inhomogeneous ferromagnetic phase or critical region that may obtain on other lattices.)

In order to bypass energy barriers that can trap a system's state at low temperatures in the glassy phase we have used the parallel TMC algorithm. $^{39,43}$ We apply the TMC algorithm as follows. We run in parallel a set of $n$ identical systems at equally spaced temperatures $T_i$, given by $T_i=T_0$ $-i\Delta T$ where $i=0,...,n-1$ and $\Delta T>0$. By *identical* we mean here that all $n$ systems have the same quenched distribution of empty sites, though each system starts from an independently chosen initial condition. We apply the TMC algorithm to any given system in two steps. In the first step, system $i$ evolves independently for eight MC sweeps under the standard single-spin-flip Metropolis algorithm. $^{44}$ (Owing to dipolar interactions, the MC sweep time scales as $N^2$, where $N$ is the number of spins.) We update all dipolar fields throughout the system every time a spin flip is accepted. In the second step, we give system $i$ a chance to exchange states with system $i+1$ evolving at a lower temperature $T_i-\Delta T$. We accept exchanges with probability $P=1$ if $\delta E=E_i-E_{i+1}<0$, and $P=\mathrm{exp}(-\Delta\beta\delta E)$ otherwise, where $\Delta\beta=1/T_{i+1}-1/T_i$. The cycle is complete when $i$ has been swept from 0 to $n$ $-2$. Thus, we associate eight MC sweeps with each cycle. For the simulation to converge at low temperatures it is important to choose $\Delta T$ small enough to allow frequent state exchanges between systems. This will often be fulfilled if $\Delta\beta\Delta E\lesssim1$. The required condition, $\Delta T\lesssim T/\sqrt{Nc}$, follows for $\Delta T$ where $c$ is the specific heat per spin. Then, we obtain appropriate values for $\Delta T$ from inspection of plots of the specific heat vs $T$. $^{18}$ We find it helpful to have the highest temperature $T_0$ at least twice as large as what we expect to be the transition temperature between the paramagnetic and the ordered phase for obtaining equilibrium results in the ordered phase.

In our simulations the $n$ identical systems start from completely disordered spins configurations. We need equilibration times $t_0$ of at least $4\times10^6$ MC sweeps for $x\le0.7$ for systems with a number dipoles $N\ge200$ (see at the end of this sections for details on how we choose $t_0$). Thermal averages come from averaging over the time range $[t_0,2t_0]$. We further average over $N_r$ samples with different realizations of disorder. Values of the parameters for all TMC runs are given in Table I.

### C. Measured quantities

We next specify the quantities we calculate. We obtain the specific heat from the temperature derivative of the energy. For the staggered magnetization, we define, as befits a PAD model on a SC lattice $^{12}$

$$
m=N^{-1} \sum_{i} \sigma_{i}(-1)^{x(i)+y(i)},
\tag{3}
$$

where $x(i)$ and $y(i)$ are the space coordinates of site $i$. We calculate the probability distribution $P_{m}$ as well as the moments
$$
m_{n} \equiv\left\langle|m|^{n}\right\rangle
\tag{4}
$$
for $n=1,2$, where $\langle\cdots\rangle$ stand for averages over time and over a number $N_{r}$ of system samples with different quenched disorder. Unless otherwise stated, time averages are performed over a time range $t_{0}<t<2 t_{0}$ and $t_{0}$ is chosen as specified below in order to ensure equilibrium. We make use of these moments to calculate the staggered susceptibility and the mean square deviation of $|m| / m_{1}$, that is,
$$
\Delta_{m}^{2}=\frac{m_{2}}{m_{1}^{2}}-1.
\tag{5}
$$

In order to spot SG behavior, we also calculate the EdwardsAnderson overlap parameter $^{28}$
$$
q=N^{-1} \sum_{j} \phi_{j},
\tag{6}
$$
where
$$
\phi_{j}=\sigma_{j}^{(1)} \sigma_{j}^{(2)},
\tag{7}
$$
where $\sigma_{j}^{(1)}$ and $\sigma_{j}^{(2)}$ are the spins on site $j$ of identical replicas (1) and (2) of the system of interest. As usual, identical replicas have the same Hamiltonian and are at the same temperature but are in uncorrelated states. Clearly, $q$ is a measure of the spin-configuration overlap between the two replicas. As we do for $m$, we calculate the probability distribution $P_{q}$ as well as the moments $q_{1}=\langle|q|\rangle$ and $q_{2}=\langle q^{2}\rangle$, in analogy to Eq. (4). The SG susceptibility $\chi_{s g}$ is given by $N q_{2}$. Finally, we also make use of the relative mean-square deviation of $q, \Delta_{q}^{2}=q_{2} / q_{1}^{2}-1$.

We need to make sure that equilibrium is reached before we start taking measurements. To this end, we define a timedependent spin overlap $\tilde{q}$ not between pairs of identical systems but between spin configurations of the same system at two different times $t_{0}$ and $t_{1}=t_{0}+t$ of the same TMC run
$$
\tilde{q}\left(t_{0}, t\right)=N^{-1} \sum_{j} \sigma_{j}\left(t_{0}\right) \sigma_{j}\left(t_{0}+t\right).
\tag{8}
$$

Let $\tilde{q}_{2}\left(t_{0}, t\right)=\left\langle\left[\tilde{q}\left(t_{0}, t\right)\right]^{2}\right\rangle$. Suppose thermal equilibrium is reached long before time $t_{0}$ has elapsed. Then, $\tilde{q}_{2}\left(t_{0}, t\right) \rightarrow q_{2}$ at some time $t$ long before $t=t_{0}$. Plots of $\tilde{q}_{2}\left(t_{0}, t\right)$ vs $t$, for $10^{-6} t_{0}<t<t_{0}$, for $t_{0}=10^{7}$ MC sweeps, are shown in Fig. 1 for $x=0.20$ and various values of $T$. Plots of $q_{2}$, obtained by averaging $q^{2}$ over time, not starting at $t=t_{0}$, as we do everywhere else in order to obtain equilibrium values, but starting at $t=0$, from an initial random spin configuration, are also shown in Fig. 1 for comparison. Note that both quantities do become approximately equal when $t \gtrsim 10^{5}$ MC sweeps. In order to obtain equilibrium results, we have always chosen sufficiently large values of $t_{0}$ to make sure that $\tilde{q}_{2}\left(t_{0}, t\right)$ $\rightarrow q_{2}$ long before $t=t_{0}$. All values of $t_{0}$ and $N_{r}$ are given in Table II.

![](./images/811807406823571456_1.jpg)

FIG. 1. (Color online) Semilog plots of $\tilde{q}_{2}(t_{0}, t)$ and $q_{2}$ vs time $t$ (in MC sweeps) for systems of $8 \times 8 \times 8$ spins at the values of $T$ shown in the figure. Here, $q_{2}$ comes from averages of $q^{2}$ over time, starting at $t=0$ from an initial random spin configuration. Here, $t_{0}$ $=10^{7}$ MC sweeps. A data point at time $t$ stands for an average over a time interval $[t, 1.2 t]$ and over $10^{3}$ system samples.

As has become customary in SG work, $^{40-42}$ we calculate quantity $\xi_{L}$
$$
\xi_{L}^{2}=\frac{1}{4 \sin ^{2}(k / 2)}\left[\frac{\left\langle q^{2}\right\rangle}{\left\langle|q(\mathbf{k})|^{2}\right\rangle}-1\right],
\tag{9}
$$
where
$$
q(\mathbf{k})=N^{-1} \sum_{j} \phi_{j} e^{i \mathbf{k} \cdot \mathbf{r}_{j}},
\tag{10}
$$
where $\mathbf{r}_{j}$ is the position of site $j$ and $\mathbf{k}=(2 \pi / L, 0,0)$. Recall this system is anisotropic, interactions along the spin axes are twice as large as in a perpendicular direction. We have found this direction of $\mathbf{k}$ (perpendicular to all spin directions) to be more convenient to work with than the direction along the spin axes.

Note that replacement of $\exp (i \mathbf{k} \cdot \mathbf{r}_{j})$ by $1-i \mathbf{k} \cdot \mathbf{r}_{j}$ gives
$$
\xi_{L}^{2}=\frac{\sum_{i j}\left[\mathbf{k} \cdot\left(\mathbf{r}_{i}-\mathbf{r}_{j}\right)\right]^{2}\left\langle\phi_{i} \phi_{j}\right\rangle}{8 \sin ^{2}(k / 2) \sum_{i j}\left\langle\phi_{i} \phi_{j}\right\rangle}.
\tag{11}
$$

This is right in the $\xi_{L} / L \rightarrow 0$ limit. The above equation clearly shows that $\xi_{L}$ is then (up to a multiplicative constant) the spatial correlation length (in the $k$ direction) of $\langle\phi_{0} \phi_{r}\rangle$. Therefore, we can think of $\xi_{\infty}$, the $L \rightarrow \infty$ limit of $\xi_{L}$, as the correlation length of a macroscopic system in the paramagnetic phase. In a condensed phase, on the other hand, condensate fluctuations generally take place over finite lengths $\bar{\xi}$, but $\xi_{L} / L \rightarrow \infty$ as $L \rightarrow \infty$ if there is strong long-range order, that is, if $\langle\phi_{0} \phi_{r}\rangle$ does not vanish as $r \rightarrow \infty$. One would have to replace $\phi$ by $\phi-\langle\phi\rangle$ in Eq. (9) in order to relate $\xi_{\infty}$ to $\bar{\xi}$. Following current usage, we shall nevertheless refer to $\xi_{L}$ as "the correlation length." In contrast with $P_{q}$ and its first moments, $\xi_{L}$ takes into account spatial variations in the EA overlap $q$ and is yet another probe for detecting a SG transition. $^{40-42}$

TABLE II. Parameters of the tempered MC simulations. $x$ is the probability that any given site is occupied by a magnetic dipole; $L$ is the linear lattice size; $\Delta T$ is the temperature step in the TMC runs; $T_o$ and $T_n$ are the highest and the lowest temperatures, respectively; $N_r$ is the number of (quenched) disordered samples; and a number $t_0$ of MC sweeps are made before any measurements are taken. The measuring time interval is $[t_0,2t_0]$ in every case.

---

$x$=0.20, $\Delta T$=0.02, $T_0$=0.8

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.06</td>
    <td>0.06</td>
    <td>0.06</td>
    <td>0.12</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>8500</td>
    <td>3800</td>
    <td>1000</td>
    <td>800</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$5\times10^7$</td>
    <td>$5\times10^7$</td>
    <td>$5\times10^7$</td>
    <td>$5\times10^7$</td>
  </tr>
</table>

---

$x$=0.35, $\Delta T$=0.05, $T_0$=2.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
    <td>12</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.05</td>
    <td>0.05</td>
    <td>0.05</td>
    <td>0.275</td>
    <td>0.35</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>9000</td>
    <td>5000</td>
    <td>1100</td>
    <td>380</td>
    <td>200</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
  </tr>
</table>

---

$x$=0.50, $\Delta T$=0.05, $T_0$=2.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.1</td>
    <td>0.05</td>
    <td>0.05</td>
    <td>0.35</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>1000</td>
    <td>650</td>
    <td>500</td>
    <td>300</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$5\times10^5$</td>
    <td>$5\times10^5$</td>
    <td>$4\times10^6$</td>
    <td>$10^7$</td>
  </tr>
</table>

---

$x$=0.60, $\Delta T$=0.1, $T_0$=2.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.20</td>
    <td>0.30</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>1400</td>
    <td>500</td>
    <td>800</td>
    <td>300</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
  </tr>
</table>

---

$x$=0.65, $\Delta T$=0.1, $T_0$=3.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.30</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>1400</td>
    <td>900</td>
    <td>1400</td>
    <td>540</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
  </tr>
</table>

---

$x$=0.70, $\Delta T$=0.1, $T_0$=3.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.30</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>750</td>
    <td>200</td>
    <td>100</td>
    <td>100</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$10^6$</td>
  </tr>
</table>

---

$x$=0.75, $\Delta T$=0.1, $T_0$=3.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>1000</td>
    <td>200</td>
    <td>100</td>
    <td>100</td>
  </tr>
  <tr>
    <td>$t_0$</td>
    <td>$4\times10^6$</td>
    <td>$4\times10^6$</td>
    <td>$2\times10^6$</td>
    <td>$10^6$</td>
  </tr>
</table>

---

$x$=0.80, $\Delta T$=0.1, $T_0$=3.0

<table>
  <tr>
    <td>L</td>
    <td>4</td>
    <td>6</td>
    <td>8</td>
    <td>10</td>
  </tr>
  <tr>
    <td>$T_n$</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
    <td>0.10</td>
  </tr>
  <tr>
    <td>$N_r$</td>
    <td>600</td>
    <td>200</td>
    <td>220</td>
    <td>100</td>
  </tr>
</table>

<table>
<caption>TABLE II. (Continued.)</caption>
<tr>
<td>$t_{0}$</td>
<td>$4\times 10^{6}$</td>
<td>$4\times 10^{6}$</td>
<td>$10^{6}$</td>
<td>$10^{6}$</td>
</tr>
</table>

### III. AF PHASE

Our main results for the PAD model are summarized in the phase diagram exhibited in Fig. 2. A thermally driven second-order transition takes place at the phase boundary between the paramagnetic and AF phases. The phase boundary meets the $T=0$ line at $x\simeq 0.65$. We shall refer to the value of $x$ at this point as $x_{c}$.

In this section we report the numerical evidence for the paramagnetic-AF transition. $^{45}$ Results having to do with the spin glass are given in the next section.

The AF phase is defined by the staggered magnetization, as given in Eq. (3). We illustrate in Fig. 3(a) how the staggered magnetization $m_{1}$ behaves with temperature for $x$ =0.8. This is in sharp contrast to the behavior of $m_{1}$ for small $x$, where an AF phase does not exist. Such behavior is exhibited in Fig. 3(b). Note that $m_{1}$ appears to decrease as $N$ increases even at low $T$. We obtain similar results for the staggered magnetization for other values of $x$ (shown in Fig. 2) below $x_{c}$. This is our first piece of evidence for the nonexistence of an AF phase below some $x_{c}$ and that $x_{c}\sim 0.6$. We return to this point in the discussion of Fig. 4.

Plots of the specific heat $C$ vs $T$ are shown in the insets of Figs. 3(a) and 3(b). Note the sharp variation in $C$ vs $T$ near $T=1.5$, in Fig. 3(a), as one expects from a paramagnetic-AF phase transition. Note also how, as one expects for a paramagnetic-SG transition, $C$ varies smoothly for a smaller value of $x$, in Fig. 3(b).

For further information about the extent of the AF phase, we now examine how $m$ varies with $N$ for some values of $x$ and of $T$. Compare the log-log plots of $m_{2}$ versus the number of dipoles $N$ on Figs. 4(a) and 4(b), respectively. The data points in Fig. 4(a) are consistent with a second-order phase transition from a magnetically disordered phase, above $T$ $=1.2(1)$, for which $Nm_{2}=O(1)$, to a strong long-range order below $T=1.2(1)$, where $m_{2}=O(1)$. Note that $m_{2}\sim 1/N^{p}$ at $T=1.2$. From the definition of $\eta$ (see Sec. V B or Ref. 46), $3p=1+\eta$ follows, which gives $\eta=0.05$. We are however not too interested here in such details of the critical behavior on the $T=T_{\text{AF}}(x)$ line. In Fig. 4(b), $m_{2}$ vs $N$ plots show faster than algebraic decay with $N$. This shows we are then beyond the bounds of the AF phase. We have followed this criterion as a first approach in establishing the boundary of the AF phase. Plots of $m_{1}$ (instead of $m_{2}$) vs $N$ show the same qualitative behavior.

We draw more quantitative results about the AF phase boundary from the behavior of the relative uncertainty $\Delta_{m}^{2}$. We first outline how we expect $\Delta_{m}^{2}$ to behave as a function of $T$ and $x$ in the various magnetic phases. It clearly follows from its definition in Eq. (5) that $\Delta_{m}^{2}\to 0$ as $N\to\infty$ in the AF phase. It also follows immediately from the law of large numbers that, in the paramagnetic phase, $\Delta_{m}^{2}\to\pi/2-1$ as $N\to\infty$. These two statements imply that curves of $\Delta_{m}^{2}$ vs $T$ for various values of $N$ cross at the phase boundary between the paramagnetic and AF phases. We make use of this fact to quantitatively determine the AF-paramagnet phase boundary. The same criterion can be applied to the AF-SG phase boundary. To see why this is so, note that, the plots shown in Fig. 4(b) for $x=0.5$ suggest $m_{2}\to N^{-1}$ as $N\to\infty$, even at low temperatures, that is, well within the SG phase. Plots of $\Delta_{m}^{2}$ vs $T$ are shown in Figs. 5(a) and 5(b) for $x=0.7$ and 0.6, respectively. The signature of an AF phase below $T\simeq 1.2$ clearly shows up in Fig. 5(a). We have thus established all points of the AF phase boundary shown in Fig. 2 for $x$

![](./images/811807406823571456_2.jpg)

FIG. 2. (Color online) Phase diagram of the PAD model. $\bigcirc$ stand for the Néel temperature $T_{\text{AF}}$ and $\blacksquare$ stand for the SG transition temperature $T_{sg}$. $\diamondsuit$ stand for maxima value of $x$ for which $m_{2}$ decreases as $N$ increases for each of three fixed values of $T$. The full line for the phase boundary between the paramagnetic and AF phases is a fit to the data points, given by, $T_{\text{AF}}\simeq 3.8(x-x_{c})^{0.4}$, where $x_{c}=0.65$. The straight dashed line is for $T_{sg}=xe_{a}$. In the inset, $m_{2}$ versus $x$ for $T=0.4$. $\bigcirc$, $\square$, $\diamondsuit$, and $\bigtriangleup$, stand for $L=10$, 8, 6, and 4, respectively.

![](./images/811807406823571456_3.jpg)

FIG. 3. (Color online) (a) Staggered magnetization $m_{1}$ vs $T$ for $x=0.8$. Icons $\bigcirc$, $\square$, $\diamondsuit$, and $\bigtriangleup$ stand for $L=10$, 8, 6, and 4, respectively. Lines are only guides to the eye. Note $m_{1}$ grows with $L$ at low temperature, consistently with an AF phase. In the inset, specific heat vs $T$ for the same values of $x$ and of system sizes. The sharp variation $C$ with respect to $T$ near $T=1.5$ is consistent with an AF phase transition thereon. (b) Same as in (a) but for $x=0.6$. Note (i) $m_{1}$ decreases with $L$ at all temperatures, consistently with the nonexistence of an AF phase and (ii) a rounded specific heat, consistent with a SG transition. In all panels, error bars are smaller than symbol sizes.

![](./images/811807406823571456_4.jpg)

FIG. 4. (Color online) (a) Log-log plots of $m_2$ versus $N$ for $x$ =0.7 and the values of $T$ shown. Continuous lines are guides to the eye, except for the straight line over the data points for $T$=1.2, which is for $1/N^{0.35}$. A dashed line shows the slope one expects for a macroscopic paramagnet. (b) Same as in (a) but for $x$=0.5. In all panels, error bars are smaller than symbol sizes.

$\geq 0.7$. For the low-temperature portion of the phase boundary (near $x$=0.65) this procedure is not very effective. From Fig. 5(b), we infer that the AF boundary line must drop to a $T$=0 value at some $x>0.60$. The three data points shown for $x\simeq 0.65$ and $T<1$ are obtained from plots such as the one shown in the inset of Fig. 2 for $T$=0.4.

### IV. SG PHASE

In this section, we report numerical results we draw from tempered MC calculations for $q_2$, for distributions of $q$, and for $\xi_L$. Because we expect, from the argument given in Sec. I, lattice-independent behavior for $x\ll 1$, we emphasize the results we have obtained for the two smallest values of $x$ we have dealt with, $x$=0.2 and $x$=0.35 (that is, $x\simeq 0.3x_c$ and $x\simeq 0.54x_c$).

A plot of $q_2$ versus $T$ is shown in Fig. 6. Note that $q_2$ decreases as $N$ increases, even at low temperatures. We have found similar behavior for other values of $x$ satisfying $x\lesssim x_c$. Inspection of this figure raises the question of whether $q_2$ vanishes as $L\rightarrow\infty$. In order to advance in this direction, we do log-log plots of $q_2$ vs $N$, which we show in Figs. 7(a)-7(c), for the values of $x$ shown therein. The data points in these three figures seem consistent with, $q_2\sim N^{-p}$ for $T/x\lesssim 1$, where $3p=1+\eta$, as follows from the definition of $\eta$ in Sec. V B (see also Ref. 46). $\chi^2$ values for $q_2\sim N^{-p}$ fits to sets of data points, for $T/x\lesssim 1$ (for which they are appropri-

![](./images/811807406823571456_5.jpg)

FIG. 5. (Color online) (a) Plots of $\Delta_m^2$ vs $T$, for $x$=0.7. $\bullet$, $\square$, $\diamond$, and $\times$ are for $L$=10, 8, 6, and 4, respectively. Lines are guides to the eye. The thick dashed line is for the macroscopic paramagnetic limit $\pi/2-1$. (b) Same as in (a) but for $x$=0.6. (c) Plots of $\Delta_q^2$ vs $T$, for $x$=0.7. Symbols are as in (a). (d) Same as in (c) but for $x$=0.6. Error bars are shown only where they are larger than symbol sizes.

![](./images/811807406823571456_6.jpg)

FIG. 6. (Color online) Semilog plots of $q_2$ versus $T$ for $x$=0.2 and $L$=10 ($\bigcirc$), $L$=8 ($\square$), $L$=6 ($\diamond$), and $L$=4 ($\triangleright$). All error bars are smaller than symbol sizes.

![](./images/811807406823571456_7.jpg)

FIG. 7. (Color online) (a) Plots of $q_2$ versus the number of dipoles $N$ for $x$=0.5. $\bigcirc$, $\square$, $\diamond$, $\triangleright$, $\triangle$, $\nabla$, $\triangleleft$, and $\blacksquare$ stand for $T$ =0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, and 0.8, respectively. Lines are guides to the eyes. (b) Same as in (a) but for $x$=0.35. $\bigcirc$, $\square$, $\diamond$, $\triangleright$, $\triangle$, $\nabla$, and $\triangleleft$, stand for $T$=0.25, 0.3, 0.35, 0.4, 0.45, 0.5, and 0.6, respectively. (c) Same as in (a) but for $x$=0.2. $\bigcirc$, $\square$, $\diamond$, $\triangleright$, $\triangle$, $\nabla$, $\triangleleft$, and $\blacksquare$, stand for $T$=0.12, 0.14, 0.16, …, 0.22, 0.26, and 0.30. For all data, we have checked that, within errors, $\widetilde{q}_2$=$q_2$. Clearly, data point sets for larger temperatures deviate from the straight dashed lines shown (implying faster than a power of $1/L$ decay) while sets for lower temperatures do not. Error bars are shown only where they are larger than the icon sizes. For each set of points with given $x$ and $T$ values, $\chi^2$ values for straight line fits, as well as the largest error, are given in Table III.

TABLE III. $\chi_{r}^{2}$ values for two-parameter $q_{2}=c / N^{p}$ fits to sets of data points for $q_{2}$ vs $T$ displayed in Figs.
7(a)-7(c). As usual, we define $\chi_{r}^{2}=\chi^{2} / d f$, where $d f$ is the number of data points in each set minus the number
of fitting parameters (2, here). The largest errors $\Delta q_{2}$ of $q_{2}$ from all data points for each $x$ and $T$ are also
given.

<table>
<thead>
  <tr>
    <th colspan="3">x=0.50</th>
    <th colspan="3">x=0.35</th>
    <th colspan="3">x=0.20</th>
  </tr>
  <tr>
    <th>T</th>
    <th>$\chi_{r}^{2}$</th>
    <th>$\Delta q_{2}$</th>
    <th>T</th>
    <th>$\chi_{r}^{2}$</th>
    <th>$\Delta q_{2}$</th>
    <th>T</th>
    <th>$\chi_{r}^{2}$</th>
    <th>$\Delta q_{2}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.10</td>
    <td>1.29</td>
    <td>0.01</td>
    <td>0.20</td>
    <td>0.21</td>
    <td>0.008</td>
    <td>0.12</td>
    <td>0.28</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.20</td>
    <td>0.84</td>
    <td>0.01</td>
    <td>0.30</td>
    <td>0.70</td>
    <td>0.01</td>
    <td>0.14</td>
    <td>0.22</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.30</td>
    <td>0.91</td>
    <td>0.01</td>
    <td>0.35</td>
    <td>0.38</td>
    <td>0.02</td>
    <td>0.16</td>
    <td>0.15</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.40</td>
    <td>0.96</td>
    <td>0.008</td>
    <td>0.40</td>
    <td>0.52</td>
    <td>0.012</td>
    <td>0.18</td>
    <td>0.08</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.50</td>
    <td>0.12</td>
    <td>0.006</td>
    <td>0.45</td>
    <td>1.70</td>
    <td>0.008</td>
    <td>0.20</td>
    <td>0.03</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.60</td>
    <td>0.46</td>
    <td>0.004</td>
    <td>0.50</td>
    <td>3.50</td>
    <td>0.004</td>
    <td>0.22</td>
    <td>0.12</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>0.70</td>
    <td>1.96</td>
    <td>0.004</td>
    <td>0.60</td>
    <td>15.09</td>
    <td>0.003</td>
    <td>0.26</td>
    <td>1.24</td>
    <td>0.008</td>
  </tr>
  <tr>
    <td>0.80</td>
    <td>2.20</td>
    <td>0.003</td>
    <td></td>
    <td></td>
    <td></td>
    <td>0.30</td>
    <td>3.38</td>
    <td>0.006</td>
  </tr>
</tbody>
</table>

ate) as well as for $T / x \geq 1$ (for which they are not appropriate), are given in Table III. Plots of $q_{1}$ vs $N$ show the same qualitative behavior. All of this is in accordance with quasilong-range order. We return to this point below and in Sec. V B.

Reading off values of $p$ from plots shown in Figs. 7(a)-7(c), we obtain $\eta$ for $x \leq 0.5$ and various values of $T$. The relation $\eta=-1+a_{x}(T / x)^{2}$ fits the data rather well for all $T / x \leq 1$, if we let $a_{x}=0.76,0.98,1.18$ for $x=0.2,0.35,0.5$, respectively. In order to be able to conclude that $\eta(T_{s g})$ varies with $x$, we would need to know $T_{s g}$ within an error of 10%. Unfortunately, we find below (in Sec. V A) an error in $T_{s g}$ which is not much smaller than 10%.

For higher values of $T / x, q_{2}$ vs $N$ curves downwards, as expected for the paramagnetic phase. Approximate values of $T_{s g}$ can thus be obtained from such plots but more accurate methods are given below. It is reassuring to see in Figs. 7(a)-7(c), the values of $\widetilde{q}_{2}$ we have obtained agree, within errors, with the values for $q_{2}$.

We next give distributions of $q$ we have found. We make use of a normalized distribution $P_{q}(q_{r})$, where $q_{r}=q / q_{1}$. In macroscopic paramagnets, $q_{r}$ is expected to be normally distributed, as follows from the law of large numbers and the fact that spin-spin correlation lengths are then finite. On the other hand, $P_{q}=[\delta(q_{r}-1)+\delta(q_{r}-1)] / 2$, where $\delta$ is the Dirac delta function, in a SG phase, according to the droplet picture of SGs. $^{37}$ Plots of $P_{q}$ vs $q_{r}$ are shown for $x=0.2$ in Figs. 8(a)-8(c). Clearly, $P_{q}(q_{r})$ drifts with system size in Fig. 8(a), for $T=0.28$. Our results are consistent with $P_{q}(q_{r}) \to (1 / \pi) \exp (-q_{r}^{2} / \pi)$ as $N \to \infty$, which is in accordance with a paramagnetic phase. On the other hand, we find for lower temperatures double-peaked distributions in Figs. 8(b) and 8(c) that are fairly broad and, within errors, do not change with $N$. This is contrary to the prediction of the droplet-model theory of SGs. From these graphs we conclude that $0.16<T_{s g}<0.26$ for $x=0.2$. Analogous plots for $x=0.35$ (not shown) give $0.30<T_{s g}<0.45$.

Results for the scale-free quantity $\Delta_{q}^{2}$ follow. Recall that, as explained for $\Delta_{m}^{2}, \Delta_{q}^{2} \to \pi / 2-1$ as $N \to \infty$ in the paramagnetic phase, vanishes when there is strong long-range order, and goes, at the critical temperature, to some intermediate value that is size independent. This is as shown in Fig. 5(c) for $x=0.7$ where curves for various values of $N$ cross at $T_{\mathrm{AF}}$. Figures 5(a) and 5(c) look rather similar because $q$ and $m$ are not qualitatively different in the AF phase. This is not so for $x<x_{c}$, where there is no AF order. Figures 5(b) and 5(c) for $x=0.6$ show that, within errors, curves of $\Delta_{q}^{2}$ vs $T$ for different system sizes merge (not cross) near $T=0.65$ while $\Delta_{m}^{2}$ increases with $N$ for all temperatures. Similarly, $\Delta_{q}^{2}$ vs $T$ curves merge, for $x=0.65$, near $T=0.75$ (not shown). Plots of $\Delta_{q}^{2}$ vs $T / x$ are shown in Figs. 9(a)-9(c) for lower concentrations.

![](./images/811807406823571456_8.jpg)

FIG. 8. (Color online) (a) Plots of the probability distribution $P_{q}$ versus $q / q_{1}$ for $x=0.2$ and $T=0.28$. $\bigcirc, \square$, and $\times$ are for $L=10,8$, and 6, respectively. The thick dashed line is for the Gaussian distribution that ensues for a paramagnet in the macroscopic limit. (b) Same as in (a) but for $T=0.16$. (c) Same as in (a) but for $T=0.12$. Error bars are shown wherever they are larger than symbol sizes.

![](./images/811807406823571456_9.jpg)

FIG. 9. (Color online) (a) Plots of $\Delta_q^2$ vs $T/x$, for $x$=0.5. $\bigcirc$, $\square$, $\Diamond$, and $\times$ are for $L$=10, 8, 6, and 4, respectively. (b) Same as in (a) but for $x$=0.35. (c) Same as in (a) but for $x$=0.2. (d) Plots of $\Delta_q^2/\Delta_q^2(4)$ vs $T$ for $x$=0.5. Symbols are as in (a). (e) Same as in (d) but for $x$=0.35. (f) Same as in (d) but for $x$=0.2. In panels (a), (b), and (c), all error bars are smaller than symbol sizes.

We notice that curves in Figs. 9(a)-9(c) differ only slightly. This follows from the argument given in Sec. I, which shows that all physical quantities for three- dimensional dipolar systems can only be functions of $T/x$ for $x\ll 1$. The data points in Fig. 9 show that $\Delta_q^2\rightarrow \pi/2-1$ as $N\rightarrow \infty$, for $T/x\gtrsim 1$, as expected for the paramagnetic phase.

Curves for $\Delta_q^2$ vs $T$ seem to merge at a lower temperature, near $T/x$=0.9. However, closer scrutiny shows that these curves actually cross, albeit at very small glancing angles. This can be appreciated in Figs. 9(d)-9(f), where plots of the ratios $\Delta_q^2(L)/\Delta_q^2(4)$ vs $T$ are given for various values of $L$, for $x$=0.5, $x$=0.35, and $x$=0.2, respectively. Note that the weak dependence of $\Delta_q^2$ with system size at low temperatures is in accordance with our result that $P_q(q_r)$ does not change appreciably with system size below $T_{sg}$. This point is further elaborated in Sec. V B

Following the lead of Refs. 40 and 41, who have found that $\xi_L/L$ (defined in Sec. II C) crosses at $T_{sg}$ and spreads out as $T$ decreases below $T_{sg}$ for the EA model in 3D, we next examine how $\xi_L/L$ behaves for the PAD model. As pointed out in Sec. I and Table I, this has already been done for the PAD model on a $\text{LiHo}_x\text{Y}_{1-x}\text{Y}_4$ lattice by Kam and Gingras. $^{32}$ As we also point out in Sec. I, we aim to explore the behavior of the PAD model, not only near $T_{sg}$ but also deep into the SG phase. Recall that $\xi_L$ becomes a true correlation length when $\xi_L/L\ll 1$. Then, in the paramagnetic phase, $\xi_L/L\sim O(1/L)$, therefore decreasing as $L$ increases. At $T$=$T_{sg}$, $\xi_L/L$ must become independent, as expected for a scale-free quantity. The inferences one can make about the nature of the condensed phase from the behavior of $\xi_L$ where $T<T_{sg}$ is the subject of Sec. V B. Without further comment, we next report our results. Plots of $\xi_L/L$ versus $T/x$ are shown in Figs. 10(a) and 10(b) for $x$=0.35 and 0.2, respectively. Note that curves spread out above and below $T/x$ $\sim 1$. For $x$=0.35, curves for all $L$ cross at $T_{sg}/x$=0.95(5). On the other hand, the temperatures where pairs of curves for lengths $L_2$ and $L_1$ cross for $x$=0.2 decrease as lengths $L_2$ and $L_1$ increase [see Fig. 10(b)], pointing to a $T_{sg}/x\lesssim 1.1$.

![](./images/811807406823571456_10.jpg)

FIG. 10. (Color online) (a) Semilog plots of (a) $\xi_L/L$ versus $T/x$ for $x$=0.35, and $L$=10 ($\blacksquare$), $L$=8 ($\bullet$), $L$=6 ($\Diamond$), and $L$=4 ($\blacktriangle$). Dashed line follows from $1/L\rightarrow 0$ straight line extrapolations in the plots shown in Fig. 12(a) for $T<T_{sg}$. Continuous lines are guides to the eye. (b) Same as in (a) but for $x$=0.2. All error bars are smaller than symbol sizes.

## V. EXISTENCE AND NATURE OF THE SG PHASE

In this section we examine the numerical results given in the previous section. We (i) arrive at values for $T_{sg}$ as a function of $x$, (ii) show that weak long-range order is consistent with our results for the SG phase, and (iii) draw values for the critical exponent $\nu$ for various values of $x$.

### A. Value of $T_{sg}$

Recall first that $\Delta_q^2$ vs $T$ curves for different values of $L$ are supposed to come together as $T$ approaches $T_{sg}$ from above. This behavior is exhibited in Figs. 9(a)-9(c). A closer view of how such curves actually meet at $T$=$T_{sg}$ is offered in Figs. 9(d)-9(f), where plots of $y(L,4)$ versus $T/x$, where $y(L,L')=\Delta_q^2(L)/\Delta_q^2(L')$, are shown. One aims to find the $L$ $\rightarrow \infty$ and $L'\rightarrow \infty$ limit of $y(L,L')$=1, which gives the value of $T_{sg}$. We find that $y(L,L')$=1 at values of $T/x$ that increase with $L$ and $L'$, which is reassuring, because it shows that $T_{sg}$ does not vanish. Furthermore, we draw the following lower bounds from the plots in Figs. 9(d)-9(f), $T_{sg}/x$ $\gtrsim 0.95,0.8,0.95$, for $x$=0.5,0.35,0.20, respectively.

We obtain a complementary determination of $T_{sg}$ from the intersection of $\xi_L/L$ vs $T$ curves. This is as is sometimes done for the EA (Refs. 40-42) and PAD (Ref. 32) models. We obtain, from Fig. 10(a), $T_{sg}/x\approx 0.95$ for $x$=0.35. In Fig.

![](./images/811807406823571456_11.jpg)

FIG. 11. (Color online) (a) Plots of distributions $P_q$ versus $q/q_1$ for $x$=0.2 and the shown values of $L$ and $T$. Error bars are shown only where they are larger than symbol sizes. (b) Plots of $T_g/x$ versus $N$ for the shown values of $x$. The thick dashed line stands for the $N^{-1/2}$ behavior obtained in Ref. 33.

10(b), we see that $\xi_L/L$ vs $T$ curves meet at decreasingly smaller values of $T$ as $L$ increases. We thus obtain $T_{sg}/x$ $\leqslant 1.1$ for $x$=0.2. From these two complementary determinations, we arrive at: $T_{sg}/x=1.0(1)$ for $x\lesssim0.5$.

An aside follows about the result by Snider and Yu, $^{33}$ that $T_{sg}=0$ for $x$=0.045, 0.12, or 0.2. This is, of course, in clear contradiction with our results. Their conclusions come from their work with the Wang-Landau$^{47}$ variation in the MC algorithm. Their evidence is from plots of $T_g$ versus $N$, where $T_g$ is the temperature at which $P_q$ becomes flattest. This procedure makes sense because $T_g\rightarrow T_{sg}$ as $N\rightarrow\infty$. They found $T_g$ to vanish as $N^{-1/2}$ for several $x$ values, including $x$=0.2. We now repeat this procedure using our own data, including the ones for $x$=0.2. In Fig. 11(a) we plot the flattest distributions we found for $x$=0.2 and $L$=4, 8, and 10. Note in passing that all scaled distributions coincide and have therefore the same value of $\Delta_q^2$. Plots of the values of $T_g/x$ we have obtained for $x$=0.5, 0.35, and 0.2 are shown in Fig. 11(b). Our data points are in clear contrast to the $T_g\sim N^{-1/2}$ trend of Ref. 33 and point to $T_{sg}/x\simeq1$. Whether this disagreement comes from using a different Monte Carlo method, or from the unusual definition of $q$ in Ref. 33, we do not know.

### B. Marginal behavior

Here we discuss how various pieces of evidence (including crossings of $\xi_L/L$ vs $T$ curves) lead us to the conclusion that the SG phase of the PAD model behaves marginally. That is to say, that $\langle q^2\rangle\rightarrow0$ and $\chi_{sg}\rightarrow\infty$ in the macroscopic limit.

The variation in $\langle q^2\rangle$ with $L$ for various temperatures, exhibited in Figs. 7(a)-7(c), has already been considered in Sec. IV. For all $x<x_c$, $T<T_{sg}$, and all system sizes we have studied, we find no deviation from $\langle q^2\rangle\sim L^{-(1+\eta)}$. Nor do we find any size dependence in $P_q(q_r)$. This is illustrated in Figs. 8(b) and 8(c), and is in accordance with the behavior of the distribution of the magnetization that is observed$^{19}$ in the condensed phase of the 2D $XY$ model. Note that the variation in $\Delta_q^2$ with system size is a measure of the variation in $P_q(q_r)$. The very small changes we have observed in $\Delta_q^2$ as $L$ varies
![](./images/811807406823571456_12.jpg)

FIG. 12. (Color online) (a) Semilog plots of $\xi_L/L$ versus $1/L$ for $x$=0.35, and $T/x$=0.143 ($\bullet$), $T/x$=0.286 ($\blacksquare$), $T/x$=0.571 ($\Diamond$), $T/x$=0.857 ($\blacktriangledown$), $T/x$=1.00 ($\blacktriangle$), $T/x$=1.14 ($\lozenge$), $T/x$=1.43 ($\square$), $T/x$=1.71 ($\bigcirc$), and $T/x$=2.00 ($	riangledown$). (b) Same as in (a) but for $x$=0.20, and $T/x$=0.300 ($\bullet$), $T/x$=0.500 ($\blacksquare$), $T/x$=0.700 ($\Diamond$), $T/x$=1.00 ($\blacktriangledown$), $T/x$=1.10 ($\blacktriangle$), $T/x$=1.30 ($\lozenge$), $T/x$=1.50 ($\square$), $T/x$=2.00 ($\bigcirc$), and $T/x$=2.50 ($	riangledown$). All errors are: between 2% and 3% in (a), and between 2% and 4% in (b), and are thus hidden behind the icons. In both (a) and (b), the straight dashed lines give $\chi_r^2<1$ fitting values, except for $T/x$=1.0 in (b), for which $\chi_r^2$=3.3.

in the PAD model for all $T\leq T_{sg}$ turn out to be smaller than the corresponding changes in the $XY$ model.$^{19}$ This is, of course, in marked contrast with the behavior one expects of the corresponding quantity for a strongly ordered system, such as the droplet model of SGs or an ordinary ferromagnet, in which $\Delta_q^2\rightarrow0$ in the macroscopic limit of the ordered phase. Neither do our results fit into a replica-symmetry-breaking (RSB) scenario, $^{38}$ in which $q_2$ does not vanish as $L\rightarrow\infty$ and would have $P_q(q_r)$ changing with system size since $P_q(q)$ is wide and does not change with system size in the SG phase.

We now analyze the data we have for $\xi_L$. First, we outline how we expect $\xi_L/L$ to spread out as $T$ decreases below $T_{sg}$ in various SG scenarios.

### 1. Condensate with short-range order fluctuations

In such a SG phase, $q_2\neq0$ and $\langle\varphi_0\varphi_r\rangle-\langle\varphi_0\rangle\langle\varphi_r\rangle$ would be short ranged. This would fit into the droplet model of spin glasses.$^{37}$ It then follows straightforwardly from its definition [Eq. (9)] that $\xi_L^2/L^2\sim L^d$. Here, $d$=3, and there is nothing in the plots of $\xi_L/L$ vs $1/L$, which are shown in Figs. 12(a) and 12(b), to suggest that $\xi_L^2/L^2\sim L^3$ at any nonzero temperature.

### 2. Condensate with long-range order fluctuations

Let $\langle A\rangle_q$ be the thermal average of $A$ over all states with a given $q$ value. Clearly, $\langle A\rangle=\int\langle A\rangle_qP_qdq$. Assume $q_2\neq0$, and $\int[\langle\varphi_0\varphi_r\rangle_q-q^2]P_qdq=G(r)$, where

$$
G(r) \equiv \frac{A}{r^{d-2+\eta}} \tag{12}
$$

for $r \gg a$, where $A$ is a constant. This behavior fits in with the RSB picture. $^{38}$ Then, it follows from its definition [Eq. (9)] that $\xi_{L}^{2} / L^{2} \sim L^{1+\eta}$. Recall, from Sec. IV, that $\eta \simeq-1$ $+\left(T / T_{s g}\right)^{2}$ in the SG phase. Evidence for $\xi_{L}^{2} / L^{2} \sim L^{1+\eta}$ appears neither in Fig. 12(a) nor in Fig. 12(b).

### 3. Marginal behavior

Then, $q_{2}=0$ and $\left\langle\varphi_{0} \varphi_{r}\right\rangle=G(r)$. This is as in the Kosterlitz Thouless theory $^{35}$ of the 2D $X Y$ model. It then follows straightforwardly from the definition of $\xi_{L} / L$ that $\xi_{L} / L$ becomes independent of $L$ for very large $L$. This is precisely the outcome from $1 / L \rightarrow 0$ extrapolations of the straight lines shown in Figs. 12(a) and 12(b) for all $T / x \leq 1$.

Note also in Figs. 12(a) and 12(b) that curves for $\xi_{L} / L$ vs $1 / L$ become steeper as $T$ decreases below $T / x \simeq 1$. Now, recall from above that $q_{2} \neq 0$ implies $\xi_{L}^{2} / L^{2} \sim L^{d}$ and $\xi_{L}^{2} / L^{2}$ $\sim L^{1+\eta}$, for short- and long-range fluctuations from the condensate. Note further that $|1+\eta|$ decreases as $T$ decreases. This would lead to $\xi_{L} / L$ vs $1 / L$ curves which do not become steeper as $T$ decreases below $T / x \simeq 1$, which is in clear contradiction with the observed behavior. This is an additional piece of evidence for quasilong-range order.

Thus, the most straightforward interpretation of the data shown in Figs. 12(a) and 12(b) leads us to suspect that the SG phase in the PAD model behaves marginally. This might seem to be in contradiction to the fact that $\xi_{L} / L$ curves do cross, as shown in Fig. 10, and that, as pointed out in Ref. $41, \xi_{L} / L$ vs $T$ curves merge, not cross, for the 2D $X Y$ model, as $T \rightarrow T_{s g}$ from above. (Indeed, no crossings occur for even much smaller 2D $X Y$ systems than the ones for which data points are shown in Ref. 41). We next give a specific example in order to illustrate how both merging and spreading out as $T$ decreases below $T_{s g}$ can take place, depending on some details in $G(r)$.

We first calculate $\xi_{L} / L$ from $\left\langle\varphi_{0} \varphi_{r}\right\rangle=G(r)$ and Eq. (12) for all $r$ except that $G(r)=1$ for all $r \leq 1$. To proceed, we let $A=0.67$ for $T \leq T_{s g}$ but not too close to $T=0$, where one expects $A=1$. We are not interested here in the $T>T_{s g}$ range but we nevertheless then let $A \rightarrow A e^{-r / \xi_{\infty}}, \xi_{\infty}=7\left(T / T_{s g}-1\right)^{-\nu}$, and $\nu=1$, which is roughly the value we obtain below (see Sec. V C). We make use of $\eta=-1+\left(T / T_{s g}\right)^{2}$, which we have found in Sec. IV. Finally, in order to be able to make comparisons with our MC results, which we have obtained for periodic boundary conditions, we let in Eq. (12)

$$
r \rightarrow Q^{-1}\left[\sum_{\alpha=1}^{3} \sin ^{2}\left(Q r_{\alpha}\right)\right]^{1 / 2}, \tag{13}
$$

where $Q=\pi / L$ and $\mathbf{r}=\left(r_{1}, r_{2}, r_{3}\right)$. Straightforward numerical implementation of Eq. (9) yields the data points that are plotted in Fig. 13. Note the resemblance between Fig. 13 and Figs. 10(a) and 10(b) which follow from our MC calculations.

Merging of $\xi_{L} / L$ curves at $T=T_{s g}$ as $T$ decreases is obtained for all $L \geq 4$ if, instead of $A=0.667$, we let $3 A=3$ $-\left(T / T_{s g}\right)^{2}$. Note that $A\left(T_{s g}\right)=0.667$ and $A(0)=1$. If, on the other hand, one lets $3 A=3-\left(T / T_{s g}\right)^{s}$ and $0<s \leq 0.2$, which satisfies the same end-point conditions, one obtains plots for $\xi_{L} / L$ vs $T$ which look much like the ones shown in Figs. 10.

![](./images/811807406823571456_13.jpg)

FIG. 13. (Color online) Semilog plots of $\xi_{L} / L$ vs $T / x$ from Eq. (12) for the shown values of $L$. In Eq. (12), we let $A=0.67$ and $\eta$ $=-1+\left(T / T_{s g}\right)^{2}$.

To summarize, all our data (including spreading out of $\xi_{L} / L$ curves as $T$ decreases below $T_{s g}$ ) are consistent with marginal behavior in which the correlation length diverges at $T_{s g}$ as in a conventional phase transition, but weak-long range order occurs below $T_{s g}$, as in the 2D $X Y$ model.

### C. $\nu$ exponent

In accordance with the above, we look for the values of $\nu$ and $T_{s g}$ which best collapse $\xi_{L} / L$ vs $\left(T / T_{s g}-1\right) L^{1 / \nu}$ plots for various values of $L$ into a single curve for temperatures above $T_{s g}$. The best results, exhibited in Figs. 14(a) and 14(b), for $x=0.35$ and $x=0.20$, are obtained with $T_{s g} / x$ $=1.0(1)$ and $\nu=0.95$. Note the data points scatter below $T_{s g}$. This is as expected, and is consistent with quasilong-range order in the SG phase since $\xi_{L} / L$ becomes independent of $L$ then for sufficiently large $L$. Note that, as in the EA model, $^{42}$ $L=4$ seems to be too small to scale properly.

### VI. DISCUSSION

By tempered Monte Carlo calculations, we have studied an Ising model on a simple cubic lattice. There are only dipole-dipole interactions. Spins (randomly) occupy only a fraction $x$ of all lattice sites. We have calculated the entire phase diagram of the system. It is shown in Fig. 2. We have also provided strong evidence for the existence a SG phase for $0<x<x_{c}$, where $x_{c}=0.65(5)$. The SG transition temperature is given by $T_{s g}(x) \simeq x$. We have argued in Sec. I that this result carries over into other lattices if (i) $x \ll 1$ and (ii) we replace the latter expression for $T_{s g}$ by $k_{B} T_{s g}=n_{d} \varepsilon_{d}$ (see Table I). How we have arrived a this conclusion is described in Sec. V A.

We have not dwelt on the applicability of our MC results to experiments. That is beyond the scope of this paper. We nevertheless make a few comments. Recall first that, as we argue in Sec. I, lattice structure is of no consequence for very dilute PAD models. Then, $T_{s g}$ as well as the temperature $T_{m}$

![](./images/811807406823571456_14.jpg)

FIG. 14. (Color online) (a) Semilog plots of $\xi_L/L$ versus $(T/T_{sg}-1)L^{1/\nu}$ for $x=0.35$, $T_{sg}=0.345$, $\nu=0.95$, and the shown values of $L$. (b) Same as in (a) but for $x=0.20$, $T_{sg}=0.21$, $\nu=0.95$, and the shown values of $L$. Recall that scaling is expected only for $T/T_{sg}-1>0$. In both panels, all error bars are somewhat smaller than the icon sizes.

where the specific heat takes its maximum value can only depend (as in the MC simulations of Ref. 31) on $n_d\varepsilon_d$ (see Table I). We notice in Table I values for $T_{sg}$ do not fully comply with this rule. In addition, in very dilute $\text{LiHo}_x\text{Y}_{1-x}\text{F}_4$ systems, $T_m$ hardly changes with $x.^{22}$ There are several sources for the discrepancies between experiments on very dilute $\text{LiHo}_x\text{Y}_{1-x}\text{F}_4$ and the PAD model. Quantum effects seem to play a role in experiments on very dilute $\text{LiHo}_x\text{Y}_{1-x}\text{F}_4$ systems. $^{25}$ This is not too surprising since tunneling can become relevant when barrier energies become overwhelmingly large. However, we do not expect small perturbations that bring about tunneling and concomitant time-dependent effects to have a significant effect on equilibrium properties, which is the subject of this paper. In addition, exchange couplings among nearest-neighbor spins $^{31,48}$ are disregarded in the PAD model we study. Note, however that the effect of nearest-neighbor interactions must vanish as $x\rightarrow0$. Clustering of the spatial distribution of dipoles can also lead to discrepancies. $^{25}$ None of the above can however account for (i) the numerical differences between the MC results (see Table I) of Tam and Gingras, $^{32}$ and ours, nor can they account for the more serious discrepancy with (ii) Ref. 33, which we discuss in some detail in Sec. V A. Numerical (not too large) discrepancies notwithstanding, our results support the ones from Tam and Gingras $^{32}$ that the dilute PAD model does have a SG phase. On the other hand, for the roots of the discrepancies with experimental results (see Table I) on dilute $\text{LiHo}_x\text{Y}_{1-x}\text{F}_4$ systems, we have no clear picture.

As for the nature of the SG phase, all of our results are consistent with quasilong-range order. Full details are given in Sec. V B. We know of no previous study of the nature of the SG phase of the PAD model with which to compare our results. (Only the critical behavior of a PAD model is examined in Ref. 32.) On the other hand, our conclusion for the PAD model can be compared with and one drawn for the EA model in Refs. 40-42. They are both based on the behavior of $\xi_L/L$ vs $T$ curves for various values of $L$. The conclusions differ, not so much because of the data but because we have looked at the data differently (see Sec. V B and Refs. 40-42).

ACKNOWLEDGMENTS

For different helpful comments, we are grateful to Amnon Aharony, Michael E. Fisher, and Jacques Villain. We are specially indebted to J. V. for kindly reading the manuscript. We are indebted to the Centro de Supercomputación y Bioinformática and to the Applied Mathematics Department both at University of Málaga, and to Institute Carlos I at University of Granada for much computer time. Finally, we thank financial support from Grant No. FIS2006-00708 from the Ministerio de Ciencia e Innovación of Spain.

APPENDIX: WHY WE DO NOT DO EWALD SUMS

We consider site-diluted systems of Ising magnetic dipoles in a cubic box of $L^3$ sites on a SC lattice. All dipoles point along the $z$ axis of the lattice. Each site is occupied with probability $x$. We assume thermal equilibrium. We show two things in this appendix. We first show that the contribution $\Delta h$ to the magnetic field $h$ at the center of such box, coming from a periodic arrangement of replicas that span all space beyond the system of interest (the "outer space") within an arbitrarily large cube which is centered on the system of interest, vanishes as $L\rightarrow\infty$ if the system is not in a ferromagnetic phase or close to its Curie temperature. More specifically, we show that if $\langle s_i s_j\rangle-\langle s_i\rangle\langle s_j\rangle$ is short ranged and the system is homogeneous (including antiferromagnetically ordered states) then

$$
\langle\Delta h^2\rangle\rightarrow0 \tag{A1}
$$

as $L\rightarrow\infty$, where $\langle\cdots\rangle$ stands for an average over both a canonical ensemble and (site occupation) disorder. Note that we are not imposing the condition that $\langle s_i s_j\rangle^2-\langle s_i\rangle^2\langle s_j\rangle^2$ be short ranged, and recall (1) that, in general, $\sum_j\langle s_i s_j\rangle-\langle s_i\rangle\langle s_j\rangle=T\chi_m$, where $\chi_m$ is the magnetic susceptibility per site and (2) that $T\chi_m\lesssim1$ for spin glasses. Equation (A1) clearly indicates that thermodynamic limits can be obtained from Monte Carlo calculations for systems of various sizes in which contributions from the outer space are disregarded. Finally, explicit numerical evidence, Fig. 15, to this effect is also given.

To begin, let $h=\sum_j T_{ij}s_j$ ($\Delta h=\sum_j T_{ij}s_j$) be the sum is over all occupied sites within (outside) a cubic box of $L\times L\times L$ sites, centered on $i$. Therefore

$$
\Delta h^2=\sum_{n,m} T_{in}T_{im}s_n s_m, \tag{A2}
$$

where the double sum is over all occupied sites in the outer space. Let

![](./images/811807406823571456_15.jpg)

FIG. 15. (Color online) Semilog plots of $\Delta \xi_{L}/L$ vs $T/x$, where the $\Delta \xi_{L}/L$ is the difference between correlation lengths we report in this paper and correlation lengths that obtain when Ewald sums are included for $x{=}0.35$, ($\blacklozenge$) $L{=}4$ and ($\blacksquare$) $L{=}8$. These data points follow from averages over $10^{4}$ and $5{\times}10^{3}$ systems samples, for $L{=}4$ and $L{=}6$, respectively. The same sample realizations were used for the calculations with and without Ewald sums.

$$
f(\mathbf{r}_{\mathbf{n}})=\sum_{\mathbf{j}} \frac{\varepsilon_{a} \mathbf{a}^{3}}{\left|\mathbf{r}_{\mathbf{n}}+\mathbf{R}_{\mathbf{j}}\right|^{3}}\left[1-\frac{3\left(\mathbf{z}_{\mathbf{n}}+\mathbf{Z}_{\mathbf{j}}\right)^{2}}{\left|\mathbf{r}_{\mathbf{n}}+\mathbf{R}_{\mathbf{j}}\right|^{2}}\right], \tag{A3}
$$

where $\mathbf{R}_{\mathbf{j}}$ is the position of the outer $j$th box, $\mathbf{r}_{\mathbf{n}}$ is the $n$th site's position with respect to the center of the box, and the sum is over all outer boxes. Equation (A2) then becomes

$$
\Delta h^{2}=\sum_{n,m} f(\mathbf{r}_{n}) f(\mathbf{r}_{m}) s_{n} s_{m}, \tag{A4}
$$

where the sum is over all occupied sites within our system of interest. We now replace $s_{n}$ by $\langle s_{n}\rangle{+}\delta s_{n}$, and similarly for $s_{m}$, in the equation above. Now, it can be checked straightforwardly (i) that $\sum_{m} f(\mathbf{r}_{m})\langle s_{n}\rangle{=}0$ if $\langle s_{n}\rangle$ is either independent of $n$ (which would not hold for a ferromagnet with domains) and (ii) that $\sum_{m} f(\mathbf{r}_{m})\langle s_{n}\rangle{\to}0$ as $L{\to}\infty$ if $\langle s_{n}\rangle$ follows an antiferromagnetic order (which, for up and down spins with dipolar interactions on a SC lattice, is a checkerboardlike arrangement of up and down ferromagnetic columns). Performing thermal and disorder averages over the above equation, one then obtains

$$
\langle\Delta h^{2}\rangle \to \sum_{n,m} f(\mathbf{r}_{n}) f(\mathbf{r}_{m})\langle\delta s_{n} \delta s_{m}\rangle \tag{A5}
$$

as $L{\to}\infty$. Now, $f(\mathbf{r})$ varies smoothly within the system, whence

$$
\langle\Delta h^{2}\rangle \to \sum_{n}\left[f(\mathbf{r}_{n})\right]^{2} \sum_{m}\langle\delta s_{n} \delta s_{m}\rangle \tag{A6}
$$

if $\langle\delta s_{n} \delta s_{m}\rangle{\approx}0$ unless $|\mathbf{r}_{n}{-}\mathbf{r}_{m}|{\ll}L$. Finally, $\sum_{n}[f(\mathbf{r}_{n})]^{2}{=}x b \varepsilon_{a}^{2}/L^{3}$, where $b{\approx}7.6$ if $L{\gg}1$, as follows straightforwardly by numerical integration. Replacement of $\sum_{m}\langle\delta s_{n} \delta s_{m}\rangle$ by $T \chi_{m}$ gives Eq. (A1) if $\chi_{m}$ is finite. For all the parameters used in our MC calculations, we have found that $T \chi_{m}{\lesssim}1$.

The difference $\Delta \xi_{L}/L$ between the correlation lengths we report and the ones obtained when Ewald sums$^{49}$ are included, for two system sizes, are exhibited in Fig. 15. The same sample realizations were used for the calculations with and without Ewald sums. This explains why we can show in Fig. 15 values for $\Delta \xi_{L}/L$ that are smaller than the statistical errors given for $\xi_{L}/L$ (see Fig. 12) for $L{=}6$. The results are clearly consistent with a $\Delta \xi_{L}/L$ that vanishes in the thermodynamic limit.

*jjalonso@uma.es
†jefe@unizar.es
$^{1}$W. Luo, S. R. Nagel, T. F. Rosenbaum, and R. E. Rosensweig, Phys. Rev. Lett. 67, 2721 (1991).
$^{2}$S. J. Knak Jensen and K. Kjaer, J. Phys.: Condens. Matter 1, 2361 (1989).
$^{3}$D. H. Reich, B. Ellman, J. Yang, T. F. Rosenbaum, G. Aeppli, and D. P. Belanger, Phys. Rev. B 42, 4631 (1990).
$^{4}$J. A. Griffin, M. Huster, and R. J. Folweiler, Phys. Rev. B 22, 4370 (1980).
$^{5}$R. P. Cowburn, Philos. Trans. R. Soc. London, Ser. A 358, 281 (2000); R. J. Hicken, ibid. 361, 2827 (2003).
$^{6}$R. F. Wang, C. Nisoli, R. S. Freitas, J. Li, W. McConville, B. J. Cooley, M. S. Lund, N. Samarth, C. Leighton, V. H. Crespi, and P. Schiffer, Nature (London) 439, 303 (2006); G. A. Held, G. Grinstein, H. Doyle, S. Sun, and C. B. Murray, Phys. Rev. B 64, 012408 (2001).
$^{7}$S. A. Majetich and M. Sachan, J. Phys. D 39, R407 (2006).
$^{8}$D. Gateschi and R. Sessoli, in Magnetism: Molecules to Materials, edited by J. S. Miller and M. Drillon (Wiley-VCH, Weinheim, 2002), Vol. III, Chap. 3.
$^{9}$A. Morello, F. L. Mettes, F. Luis, J. F. Fernández, J. Krzystek, G. Aromí, G. Christou, and L. J. de Jongh, Phys. Rev. Lett. 90, 017206 (2003); A. Morello, F. L. Mettes, O. N. Bakharev, H. B. Brom, L. J. de Jongh, F. Luis, J. F. Fernández, and G. Aromí, Phys. Rev. B 73, 134406 (2006); V. F. Puntes, P. Gorostiza, D. M. Aruguete, N. G. Bastus, and A. P. Alivisatos, Nature Mater. 3, 263 (2004); M. Evangelisti, A. Candini, A. Ghirri, M. Af fronte, G. W. Powell, I. A. Gass, P. A. Wood, S. Parsons, E. K. Brechin, D. Collison, and S. L. Heath, Phys. Rev. Lett. 97, 167202 (2006); Y. Takagaki, C. Herrmann, and E. Wiebicke, J. Phys.: Condens. Matter 20, 225007 (2008); M. Georgescu, J. L. Viota, M. Klokkenburg, B. H. Erne, D. Vanmaekelbergh, and P. A. Zeijlmans van Emmichoven, Phys. Rev. B 77, 024423 (2008); K. Yamamoto, S. A. Majetich, M. R. McCartney, M. Sachan, S. Yamamuro, and T. Hirayama, Appl. Phys. Lett. 93, 082502 (2008).
$^{10}$T. F. Rosenbaum, J. Phys.: Condens. Matter 8, 9759 (1996).
$^{11}$J. Luttinger and L. Tisza, Phys. Rev. 72, 257 (1947).
$^{12}$J. F. Fernández and J. J. Alonso, Phys. Rev. B 62, 53 (2000).
$^{13}$A. P. Ramirez, A. Hayashi, A. Cava, R. J. Siddharthan, and B. S. Shastry, Nature (London) 399, 333 (1999); S. T. Bramwell and M. P. J. Gingras, Science 294, 1495 (2001).
$^{14}$For an interesting point, see, Sec. II of J. Villain, Z. Phys. B 33, 31 (1979).
$^{15}$T. Jonsson, J. Mattsson, C. Djurberg, F. A. Khan, P. Nordblad, and P. Svedlindh, Phys. Rev. Lett. 75, 4138 (1995); F. Bert, V. Dupuis, E. Vincent, J. Hammann, and J. P. Bouchaud, ibid. 92,

167203 (2004); G. G. Kenning, G. F. Rodriguez, and R. Orbach, ibid. 97, 057201 (2006).

16J. O. Andersson, C. Djurberg, T. Jonsson, P. Svedlindh, and P. Nordblad, Phys. Rev. B 56, 13983 (1997); J. García-Otero, M. Porto, J. Rivas, and A. Bunde, Phys. Rev. Lett. 84, 167 (2000); M. Ulrich, J. García-Otero, J. Rivas, and A. Bunde, Phys. Rev. B 67, 024416 (2003); S. Russ and A. Bunde, ibid. 75, 174445 (2007).

17Y. Sun, M. B. Salamon, K. Garnier, and R. S. Averback, Phys. Rev. Lett. 91, 167206 (2003).

18J. F. Fernández, Phys. Rev. B 78, 064404 (2008).

19J. F. Fernández and J. J. Alonso, Phys. Rev. B 79, 214424 (2009).

20J. Kötzler and G. Eiselt, Phys. Rev. B 25, 3207 (1982); J. Köt- zler, G. Hesse, H. P. Tödter, and G. Eiselt, Z. Phys. B: Condens. Matter. 68, 451 (1987).

21W. Wu, D. Bitko, T. F. Rosenbaum, and G. Aeppli, Phys. Rev. Lett. 71, 1919 (1993).

22J. A. Quilliam, S. Meng, C. G. A. Mugford, and J. B. Kycia, Phys. Rev. Lett. 101, 187204 (2008).

23C. Ancona-Torres, D. M. Silevitch, G. Aeppli, and T. F. Rosen- baum, Phys. Rev. Lett. 101, 057201 (2008).

24P. E. Jönsson, R. Mathieu, W. Wernsdorfer, A. M. Tkachuk, and B. Barbara, Phys. Rev. Lett. 98, 256403 (2007).

25D. H. Reich, T. F. Rosenbaum, and G. Aeppli, Phys. Rev. Lett. 59, 1969 (1987); S. Ghosh, R. Parthasarathy, T. F. Rosenbaum, and G. Aeppli, Science 296, 2195 (2002); S. Ghosh, T. F. Rosenbaum, G. Aeppli, and S. Coppersmith, Nature (London) 425, 48 (2003); M. Schechter and P. C. E. Stamp, Phys. Rev. B 78, 054438 (2008).

26M. J. Stephen and A. Aharony, J. Phys. C 14, 1665 (1981).

27H.-J. Xu, B. Bergersen, F. Nidermayer, and Z. Ràcz, J. Phys.: Condens. Matter 3, 4999 (1991).

28S. F. Edwards and P. W. Anderson, J. Phys. F 5, 965 (1975).

29A. J. Bray, M. A. Moore, and A. P. Young, Phys. Rev. Lett. 56, 2641 (1986).

30H. G. Katzgraber and A. P. Young, Phys. Rev. B 67, 134410 (2003); 72, 184416 (2005); H. G. Katzgraber, D. Larson, and A. P. Young, Phys. Rev. Lett. 102, 177205 (2009).

31A. Biltmo and P. Henelius, Phys. Rev. B 76, 054423 (2007); 78, 054437 (2008).

32K. M. Tam and M. J. P. Gingras, Phys. Rev. Lett. 103, 087202 (2009).

33J. Snider and C. C. Yu, Phys. Rev. B 72, 214203 (2005).

34P. B. Chakraborty, P. Henelius, H. Kjonsberg, A. W. Sandvik, and S. M. Girvin, Phys. Rev. B 70, 144411 (2004).

35J. M. Kosterlitz and D. J. Thouless, J. Phys. C 6, 1181 (1973); J. M. Kosterlitz, ibid. 7, 1046 (1974); see also, J. V. José, L. P. Kadanoff, S. K. Kirkpatrick, and D. R. Nelson, Phys. Rev. B 16, 1217 (1977); J. Villain, J. Phys. (Paris) 36, 581 (1975); J. F. Fernández, M. F. Ferreira, and J. Stankiewicz, Phys. Rev. B 34, 292 (1986); H. G. Evertz and D. P. Landau, ibid. 54, 12302 (1996).

36J. Sinova, G. Canright, and A. H. MacDonald, Phys. Rev. Lett. 85, 2609 (2000); J. Sinova, G. Canright, H. E. Castillo, and A. H. MacDonald, Phys. Rev. B 63, 104427 (2001).

37D. S. Fisher and D. A. Huse, J. Phys. A 20, L1005 (1987); D. A. Huse and D. S. Fisher, ibid. 20, L997 (1987); D. S. Fisher and D. A. Huse, Phys. Rev. B 38, 386 (1988).

38G. Parisi, Phys. Rev. Lett. 43, 1754 (1979); 50, 1946 (1983); for reviews, see M. Mézard, G. Parisi, and M. A. Virasoro, SG Theory and Beyond (World Scientific, Singapore, 1987); E. Marinari, G. Parisi, and J. J. Ruiz-Lorenzo, in Spin Glasses, edited by K. H. Fischer and J. A. Hertz, (Cambridge University Press, Cambridge, 1991); E. Marinari, G. Parisi, F. Ricci- Tersenghi, J. J. Ruiz-Lorenzo, and F. Zuliani, J. Stat. Phys. 98, 973 (2000).

39E. Marinari and G. Parisi, Europhys. Lett. 19, 451 (1992); K. Hukushima and K. Nemoto, J. Phys. Soc. Jpn. 65, 1604 (1996).

40M. Palassini and S. Caracciolo, Phys. Rev. 82, 5128 (1999).

41H. G. Ballesteros, A. Cruz, L. A. Fernandez, V. Martin-Mayor, J. Pech, J. J. Ruiz-Lorenzo, A. Tarancon, P. Tellez, C. L. Ullod, and C. Ungil, Phys. Rev. B 62, 14237 (2000).

42H. G. Katzgraber, M. Körner, and A. P. Young, Phys. Rev. B 73, 224432 (2006).

43A short justification for the TMC rule can be found in J. F. Fernán- dez and J. J. Alonso, Modeling and Simulation of New Materi- als, AIP Conference Proceedings Vol. 1091, edited by J. Marro, P. L. Garrido, and P. I. Hurtado (AIP, New York, 2009), pp. 151-161.

44N. A. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, J. Chem. Phys. 21, 1087 (1953).

45For a study of the paramagnetic-AF phase transition, as well as properties of the AF phase, on fully occupied SC lattices, see Ref. 12 and J. F. Fernández, Phys. Rev. B 66, 064423 (2002).

46M. E. Fisher, in Critical Phenomena: Proceedings of a Confer- ence, Washington, DC April 1965, edited by M. S. Green and J. V. Sengers (U.S. Govt. Office, Washington, 1966); Rev. Mod. Phys. 70, 653 (1998).

47F. Wang and D. P. Landau, Phys. Rev. Lett. 86, 2050 (2001).

48G. Mennenga, L. J. de Jongh and W. J. Huiskamp, J. Magn. Magn. Mater. 44, 59 (1984).

49P. Ewald, Ann. Phys. 369, 253 (1921).
