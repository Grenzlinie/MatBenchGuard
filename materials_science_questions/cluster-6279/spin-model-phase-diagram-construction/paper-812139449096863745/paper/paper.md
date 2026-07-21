PHYSICAL REVIEW E 72, 021709 (2005)

# Monte Carlo simulation of a strongly coupled $XY$ model in three dimensions

Rasool Ghanbari¹ and Farhad Shahbazi²

¹Department of Physics, Islamic Azad University, Majlesi branch, 86315/111, Isfahan, Iran
²Department of Physics, Isfahan University of Technology, 84156, Isfahan, Iran

(Received 24 January 2005; revised manuscript received 14 April 2005; published 25 August 2005)

Many experimental studies, over the past two decades, have constantly reported a critical behavior for the transition from the smectic-$A$ phase of liquid crystals to the hexatic-$B$ phase with non-$XY$ critical exponents. However, according to symmetry arguments this transition must belong to the $XY$ universality class. Using an optimized Monte Carlo simulation technique based on the multihistogram method, we have investigated the phase diagram of a coupled $XY$ model, proposed by Bruinsma and Aeppli [Phys. Rev. Lett. 48, 1625 (1982)], in three dimensions. The simulation results demonstrate the existence of a tricritical point for this model, in which two different orderings are established simultaneously. This result verifies the accepted idea that the large specific heat anomaly exponent observed for the SmA-Hex$B$ transition could be due to the occurrence of this transition in the vicinity of a tricritical point.

DOI: 10.1103/PhysRevE.72.021709
PACS number(s): 61.30.−v, 64.70.Md, 64.60.Kw

## I. INTRODUCTION

According to the Kosterlitz, Thouless, Halperin, Nelson, and Young (KTHNY) theory [1–3], two-dimensional systems during the melting transition from solid to isotropic liquid go through an intermediate phase called the hexatic phase for systems that have sixfold (hexagonal) symmetry in their crystalline ground state. This hexatic phase displays short range positional order, but quasi long range bond-orientational order, which is different from the true long range bond-orientational and quasi long range positional order in 2D solid phases. It is known that for two-dimensional systems, the transition from the isotropic liquid to hexatic phase could be either a KT transition or a first order transition [4].

The idea of the hexatic phase was first applied to three-dimensional systems by Birgeneau and Lister, who showed that some experimentally observed smectic liquid crystal phases, consisting of stacked two-dimensional (2D) layers could be physical realizations of 3D hexatics [5]. Assuming that the weak interaction between smectic layers could make the quasi long range order of two-dimensional layers truly long ranged, they suggest that the 3D hexatic phases in highly anisotopic systems possess short range positional and true long range bond-orientational order.

The first signs of the existence of the hexatic phase in three-dimensional systems were observed in x-ray diffraction studies of the liquid crystal compound 65OBC($n$-alkyl-4-$m$-alkoxybiphenyl-4-carboxylate, $n$=6, $m$=5) [6,7], where a hexagonal pattern of diffuse spots was found in the intensity of scattered x rays. In addition to this hexagonal pattern, it was also found that some broader peaks appeared in the diffracted intensity which indicate the onset of another ordering. These broad peaks are related to packing of molecules according to a herringbone structure perpendicular to the smectic layer stacking direction. The accompanying long range hexatic and short range herringbone orders make this phase a physically rich phase, which simply is called the hexatic-$B$ (Hex$B$) phase. When temperature is decreased, the Hex$B$ phase transforms via a first order phase transition into the crystal-$E$ (Cry$E$) phase, which exhibits both long range positional and long range herringbone orientational orders. Subsequently, it was found that other components in the $nm$OBC homologous series (like 37OBC and 75OBC) and a number of binary mixtures of $n$-alkyl-4'-$n$-decycloxybiphenyl-4-carboxylate [$n$(10)OBC] with $n$ ranging from 1 to 3 and also the compound 4-propionyl-4'-$n$-heptanoyloxyazo-benzene (PHOAB) represent the SmA-Hex$B$ transition, which later was found to be clearly first order.

Due to the sixfold symmetry of the hexatic phase, the corresponding order parameter is defined by $\Psi_6=|\Psi_6|\exp(i6\psi_6)$. The U(1) symmetry of $\Psi_6$ implies that the SmA-Hex$B$ transition is a member of the $XY$ universality class. However, heat capacity measurements on bulk samples of 65OBC [6,8] and other calorimetric studies on many other components in the $nm$OBC homologous series [6,9] have yielded very sharp specific heat anomalies near the SmA-Hex$B$ transition with no detectable thermal hysteresis and with a very large value for the heat capacity critical exponent, $\alpha\approx0.6$. These results indicate that this is a continuous (second order) phase transition, but not belonging to the 3D $XY$ universality class, for which the specific heat critical exponent is nearly zero ($\alpha\approx-0.007$ [11]). On the other hand, the other static critical exponents determined from thermal conductivity ($\eta$=-0.19) and birefringence experiments ($\beta$=0.19) [6] all differ from the 3D $XY$ values, indicating a different phase transition with probably a different universality class.

It is also interesting to mention that the same heat capacity measurement studies of (truly two-dimensional) two-layer free standing films of different $nm$OBC compounds result in a second order SmA-Hex$B$ transition, described by the heat capacity exponent $\alpha\approx0.3$ [6,10]. This is obviously in contrast with the usual broad and nonsingular specific heat hump of the KT transition in the 2D $XY$ model, suggesting that the SmA-Hex$B$ transition cannot be described simply by a unique $XY$ order parameter.

The unusual aspects of the SmA-Hex$B$ transition in two and three dimensions have attracted the interests of physi-

1539-3755/2005/72(2)/021709(9)/$23.00
021709-1
©2005 The American Physical Society

cists in the past two decades. The first theoretical attack on this problem was done by Bruinsma and Aeppli (BA) [12] who formulated a Ginzburg-Landau theory that included both hexatic and herringbone order. Because of the broad- ness of the x-ray diffracted peaks associated with herring- bone order (which is the reason for it being short range), they considered an $XY$ order parameter with twofold symmetry for herringbone ordering $[\Phi_{2}=|\Phi_{2}| \exp (i 2 \phi_{2})]$ and also based on symmetry arguments, they made a minimal coupling be- tween the hexatic and herringbone order parameters as $V_{hex-her }=h Re(\Psi_{6}^{*} \Phi_{2}^{3})$ . Microscopically, the origin of this cou pling could be the anisotropy present in liquid crystal mo- lecular structures [13,14].

In the mean field approach the results of Bruinsma and Aeppli indicate that the SmA-Hex$B$ transition should be con- tinuous. However one-loop renormalization calculations show that short range molecular herringbone correlations coupled to the hexatic ordering drive this transition first or- der, and it becomes second order at a tricritical point [12]. This result indicates the existence of two tricritical points,one for the transition between the SmA phase $(\Psi=0, \Phi=0)$  and the stacked hexatic phase $(\Psi \neq 0, \Phi=0)$ , and another for the transition between the SmA phase and the phase possess- ing both hexatic and herringbone order $(\Psi \neq 0, \Phi \neq 0)$ . Therefore, they concluded that the occurrence of a phase transition near a tricritical point, with heat capacity exponent $\alpha=0.5$ , would be a good explanation for the large heat ca pacity exponents observed in the experiments. Recently, the renormalization-group (RG) calculation of the BA model has been revised in [15], which resulted in finding another non- trivial fixed point missed in the original work of Bruinsma and Aeppli. But it has been shown that this new fixed point is unstable in one-loop level (order of $\epsilon$ ), which indicates that this fixed point does not represent a phase transition. Im- provement of this calculation to two-loop level (order of $\epsilon^{2}$ ), although it makes the new fixed point stable, gives a small and negative value for the corresponding heat capacity anomaly exponent [16], which indicts that this critical point cannot explain the experimental results. However, the limi- tations of RG methods, which mostly rely on perturbation expansions, make them insufficient for accessing the strong coupling regimes where one expects some different behavior to appear. For this purpose, numerical simulations would be useful.

The first numerical simulations for investigating the na- ture of the SmA-Hex$B$ transition in 2D systems were done by Jiang et al., who used a model consisting of a 2D lattice of coupled $XY$ spins based on the BA Hamiltonian in the strong coupling limiting [17-19]. Their simulation results suggest the existence of a type of phase transition in which two dif- ferent orderings are simultaneously established through a continuous transition with heat capacity exponent $\alpha \sim 0.3$ , in good agreement with experimental values.

The success of the BA model in two dimensions and also the absence of any numerical simulation in three dimensions were our motivations to investigate numerically the three- dimensional BA model in the strong coupling limit. To do this, we employ a high resolution Monte Carlo simulation based on the multihistogram method.

The rest of this paper is organized as follows. In Sec. II, we introduce the model Hamiltonian and give a brief intro- duction to the optimized Monte Carlo method based on mul- tiple histograms and also some methods for analyzing the Monte Carlo data, to determine the order of transitions. The simulation results and discussion are given in Sec. III and conclusions appear in Sec. IV.

## II. MONTE CARLO SIMULATION

### A. Model Hamiltonian

Recalling the sixfold symmetry of hexatic order and two- fold symmetry of herringbone order, the Hamiltonian which describes both orderings ought to be invariant with respect tothe transformations $\Phi \to \Phi+n \pi$ and $\Psi \to \Psi+m(2 \pi / 6)$  where $n$ and $m$ are integers. Thus to lowest order in $\Psi$ and $\Phi$ , one can write the following Hamiltonian for the BAmodel:
$$
\begin{aligned}
H= & -J_{1} \sum_{\langle i j\rangle} \cos \left(\Psi_{i}-\Psi_{j}\right)-J_{2} \sum_{\langle i j\rangle} \cos \left(\Phi_{i}-\Phi_{j}\right) \\
& -J_{3} \sum_{i} \cos \left(\Psi_{i}-3 \Phi_{i}\right),
\end{aligned}\qquad(1)
$$
where the coefficients $J_{1}$ and $J_{2}$ are the nearest-neighbor cou pling constants for the bond-orientational order $(\Psi)$ and her ringbone order $(\Phi)$ , respectively. The coefficient $J_{3}$ denotes the coupling strength between these two types of order at the same 3D lattice site. We are interested in situations in which $\Psi$ and $\Phi$ are coupled strongly. Therefore we fixed $J_{3}=3.0$ , larger than both $J_{1}$ and $J_{2}$ for all the simulations. Let us assume $J_{1}>J_{2}$ ; so for sufficiently high temperatures (say $T$ >J3), the system is in the completely disordered phase. For T1<T<J3, the system remains disordered but the phases of the two order parameters become coupled through the herringbone-hexatic coupling term $J_{3}$ . At mean field level, for $T_{c 2}<T<T_{c 1}$ , bond-orientational order is established through a continuous $X Y$ transition and the ordered state cor responds to $\Psi_{i} \approx \Psi_{j}$ for all sites $i$ and $j$ , producing three degenerate minima for the free energy. So for this range of temperatures the BA Hamiltonian describes a system with the symmetry of the three-state Potts model, and since the ordering transition for the three-state Potts model is first or- der in 3D, the transition between the pure hexatic and hexatic plus herringbone phases $(\Psi \neq 0, \Phi \neq 0)$ should be first order at $T_{c 2}$ . Thus for $J_{2}<J_{1}<J_{3}$ the model exhibits an $X Y$ transi tion at $T_{c 1}$ and a three-state Potts-like transition upon de creasing the temperature down to $T_{c 2}$ [19]. For $J_{2}>J_{1}$ , the herringbone order would be established first and cause the corresponding field $\Phi$ to take nearly the same value for all sites. Because of this, the coupling term $J_{3}$ acts like a field on $\Psi$ and so the hexatic order parameter takes a nonzero value.

From the above discussions, the phase diagram of the BA model, at the mean field level, consists of three phase tran- sitions: (1) a second order transition from a disordered to a hexatic phase, (2) a second order transition from a disordered to a locked phase consisting of hexatic plus herringbone or- ders, and (3) a first order transition from the hexatic to hexatic plus herringbone phases.

To obtain a qualitative picture of the transitions and also the approximate location of the critical points, we first do

![](./images/812139449096863745_1.jpg)

FIG. 1. Temperature dependence of specific heat for $J_1$=1.0, $J_2$=0.5, and $J_3$=3.0. The points between $T$=1.35 and 1.2 have been derived using multihistogram methods (see the text).

low resolution simulations. The simulations were carried out using a standard Metropolis spin-flipping algorithm with six lattice sizes ($L$=6,7,8,,9,10,12). During each simulation step, the angles $\Psi_i$ and $\Phi_i$ were treated as unconstrained, continuous variables. The random-angle rotations ($\Delta\Psi_i$ and $\Delta\Phi_i$) were adjusted in such a way that roughly 50% of the attempted angle rotations were accepted. To ensure thermal equilibrium, 100 000 Monte Carlo steps (MCS) per spin were used for each temperature and 200 000 MCS were used for data collection.

We have obtained the heat capacity data as a function of temperature, shown in Fig. 1 for $J_1$=1.0 and $J_2$=0.5, and for $J_2$=0.7,0.8,0.9,1.2 in Fig. 2. Near the lower temperature transition point ($1.2<T<1.35$) the calculated data were obtained by optimized reweighting using five histograms near $T$=1.25 (Sec. III). From the preceding discussion, it is clear that the small broad peak near $T$=2.2 signals the $XY$ transition due to the $J_1$ term, while the sharp peak located at $T$ $\sim$1.25 is expected to signal a transition into a state of three-state Potts symmetry. The same simulations based on a single-spin-flipping algorithm, whose results are represented in Fig. 2, show that the first peak ($XY$ transition) disappears for $J_2>0.9$ and therefore only one transition occurs for those values of $J_2$, which verifies that for these values of $J_2$, the transition from the disordered to the herringbone phase simultaneously induces hexatic ordering.

To determine the location of the transition temperatures and other thermodynamic quantities such as specific heat near the transition points we need to use high resolution methods. For this purpose we used the multiple-histogram reweighting method proposed by Ferrenberg and Swendsen [20], which makes it possible to obtain accurate data over the transition region from just a few Monte Carlo simulations.

### B. Histogram method

The central idea behind the histogram method is to build up information on the energy probability density function $P_\beta(E)$, where $\beta$=$1/T$ is the inverse temperature (in units with $k_B$=1). A histogram of $H_\beta(E)$ which is the number of spin configurations generated between $E$ and $E+\delta E$, $P_\beta(E)$, is defined as

$$
P_{\beta}\left(E_{i}\right)=\frac{H_{\beta}\left(E_{i}\right)}{Z_{\beta}},\qquad(2)
$$

where

$$
Z_{\beta}=\sum_{i} H_{\beta}\left(E_{i}\right).\qquad(3)
$$

On the other hand we know that $P_\beta(E_i)$ is proportional to the Boltzmann weight $\exp(-\beta E_i)$, as

$$
P_{\beta}\left(E_{i}\right)=\frac{g\left(E_{i}\right) \exp \left(-\beta E_{i}\right)}{Z_{\beta}},\qquad(4)
$$

in which $g(E_i)$ is the density of states with energy $E_i$ and is independent of temperature. By knowing the probability distributions at a specific temperature, we can derive the density of states and find the probability distribution of energy at any temperature $\beta'$ as follows:

$$
P_{\beta^{\prime}}\left(E_{i}\right)=\frac{P_{\beta}\left(E_{i}\right) \exp \left[\left(\beta-\beta^{\prime}\right) E_{i}\right]}{\sum_{j} P_{\beta}\left(E_{j}\right) \exp \left[\left(\beta-\beta^{\prime}\right) E_{j}\right]}.\qquad(5)
$$

In principle, $P_\beta(E)$ only provides information on the energy distribution of nearby temperatures. This is because the counting statistics in the wings of the distribution $H_\beta(E)$, far from the average energy at temperature $T$, will be poor.

To improve the estimation for the density of states, one can take data at more than one temperature and combine the resultant histograms so as to take advantage of the regions where each provides the best estimate for the density of states. This method has been studied by Ferrenberg and Swendsen, who presented an efficient way for combining the histograms [20]. Their approach relies on first determining the characteristic relaxation time $\tau_j$ for the $j$th simulation and using this to produce a weighting factor $g_j$=$1+2\tau_j$. The overall probability distribution at coupling $K$=$\beta J$ obtained from $n$ independent simulations, each with $N_j$ configurations, is then given by

![](./images/812139449096863745_2.jpg)

FIG. 2. Temperature dependence of specific heat for $J_1$=1.0, $J_3$=3.0, and $J_2$=0.7,0.8,0.9,1.2.

$$
P_{K}(E)=\frac{\left(\sum_{j=1}^{n} g_{j}^{-1} H_{j}(E)\right) e^{-K E}}{\sum_{j=1}^{n} N_{j} g_{j}^{-1} e^{-K_{j} E-f_{j}}},
\tag{6}
$$

where $H_j(E)$ is the histogram for the $j$th simulation and the factors $f_j$ are chosen self-consistently using Eq. (6) and
$$
e^{f_{j}}=\sum_{E} P_{K_{j}}(E).
\tag{7}
$$

Thermodynamic properties are determined, as before, using this probability distribution, but now the results will be valid over a much wider range of temperatures than for any single histogram. In addition, this method gives an expression for the statistical error of $P_K(E)$ as
$$
\delta P_{K}(E)=\left(\sum_{j=1}^{n} g_{j}^{-1} H_{j}(E)\right)^{-1 / 2} P_{K}(E),
\tag{8}
$$
from which it is clear that the statistical error will be reduced when more MC simulations are added to the analysis [20,21].

### C. Order of the transition
One of the main problems in Monte Carlo data analysis of phase transitions is determining the order of the transition. Strong first order transitions will show marked discontinuities in thermodynamic quantities such as the internal energy and the order parameter and present no real problems. Weakly first order transition are much more difficult to recognize. To understand the situation, consider a first order phase transition in an infinitely extended system, for which the correlation length reaches a finite value $\xi_c$ at the transition point where the phase of the system changes discontinuously. If $\xi_c$ is too large, i.e., $\xi_c \gg L$ where $L$ is the linear size of the system on which the simulation is being done, then the system will appear to be in the critical region of a continuous transition and it will be very difficult to detect the discontinuities. However, during the past decades, there have been significant advances in overcoming this problem. Below we list a number of techniques for detecting a first order transition: (1) discontinuities in the internal energy and the order parameter; (2) hysteresis in the internal energy and the order parameter; (3) double peaks in the probability density function $P(E)$; (4) the divergence of specific heat as $L^d$, where $d$ is the spatial dimension; (5) decreasing the half-width of the specific heat peak like $L^{-d}$; (6) the size dependence of the minima of the Binder fourth energy cumulant
$$
U_{L}=1-\frac{\left\langle E^{4}\right\rangle}{3\left\langle E^{2}\right\rangle},
\tag{9}
$$
whose value approaches $2/3$ for a continuous transition and some nontrivial value $U^* < 2/3$ at a first order transition [22].

The first method as previously mentioned, is inefficient for weakly first order transitions. The second and third methods are based on the fact that the state of a given system representing a first order transition, during its evolution, may be trapped, for a relatively long time, in some local minima of the free energy (called metastable states). These two methods are also unreliable because if the free energy barrier is small enough, both phases will be sampled within the time scale of the simulation, and then no hysteresis will be observed. The second reason is that double peaks in the probability density function have also been observed near continuous transitions in finite systems, for example, in the four-state Potts model in two dimensions. So the first three methods, although efficient for the case of strongly first order transitions, are nor suitable to investigate weakly first order transitions. Methods (4) and (5) are results of the discontinuity of the internal energy at first order phase transitions. Since the specific heat is obtained as the derivative of the internal energy with respect to temperature, we expect that it presents a $\delta$-function singularity at the transition point. This causes the specific heat peak to diverge as $L^d$, while its half-width narrows as $L^{-d}$. Consequently, for the specific heat peak and transition temperature, we will have the following behaviors at a first order phase transition:
$$
C_{max}(L)=c_{1}+c_{2} L^{d},
\tag{10}
$$

$$
T_{c}(L)=T_{c}(\infty)+A L^{-d}.
\tag{11}
$$

The coefficient $c_2$ in Eq. (10) is related to latent heat per site through the following relation [23]:
$$
c_{2}=\frac{\left(e_{1}-e_{2}\right)^{2}}{4 T_{c}^{2}},
\tag{12}
$$
where $e_1$ and $e_2$ are the values of the energy per site at the transition point of a first order phase transition. For a continuous phase transition, where the correlation length grows as $\xi \sim |T-T_c|^{-\nu}$ near a critical point, the behaviors of these two quantities are as
$$
C_{max}(L)=c_{1}+c_{2} L^{\alpha / \nu},
\tag{13}
$$

$$
T_{c}(L)=T_{c}(\infty)+A L^{-1 / \nu},
\tag{14}
$$
in which $\alpha$ is the specific heat singularity exponent.

Method (6) is a test for the Gaussian nature of the probability density function $P(E)$ at $T_c$. For a continuous transition, $P(E)$ is expected to be Gaussian at as well as away from $T_c$. For a first order transition, $P(E)$ will be double peaked in the infinite lattice size limit; hence the deviation from Gaussian tends to cause the minimum of $U_L$, $U^*$, to be less than $2/3$ as $L \to \infty$. $U^*$ is related indirectly to the latent heat. This is like the method (3) but much more sensitive, in the sense that small splittings in $P(E)$ for the infinite system that do not result in a double peak for small lattices can be detected. Another advantage of this technique is that the minimum of $U_L$ is expected to approach $2/3$ or $U^*$ as a power law in $L$, thus allowing one to extrapolate to $L=\infty$ as [23]
$$
U_{min}(L)=\frac{2}{3}-\left(e_{1} / e_{2}-e_{2} / e_{1}\right)^{2} / 12+B L^{-d}+O\left(L^{-2 d}\right).
\tag{15}
$$

Equation (15) implies that


![](./images/812139449096863745_3.jpg)

FIG. 3. Binder's fourth energy cumulant for $J_1$=1.0, $J_2$=0.8, and $J_3$=3.0. High temperature minima are near the transition from the isotropic to hexatic phase while the low temperature minima indicate the transition from the hexatic to hexatic+herringbone state.

$$
U^{*}=\frac{2}{3}-\left(e_{1} / e_{2}-e_{2} / e_{1}\right)^{2} / 12. \qquad (16)
$$

For weakly first order transitions where the latent heat per site is too small $(\Delta e=e_1 - e_2 \ll e_1)$, we can write

$$
U^{*} \approx \frac{2}{3}-(\Delta e / e)^{2} / 3. \qquad (17)
$$

As an example we have used the multihistogram method (at least ten histograms were combined for each lattice size) to calculate the temperature dependence of $U_L$ for $J_1$=1.0, $J_2$=0.8, and $J_3$=3.0 depicted in Fig. 3, in which two minima exist for all values of the linear lattice size ($L$ =6,7,8,9,10,12). The right or high temperature minima indicate the transition from disorder to the hexatic phase for which, we will show in what follows, $U^*$=2/3, indicating a second order phase transition. The left or low temperature minima represent the transition from the hexatic to the hexatic plus herringbone phase. For this transition, however, $U^*$ turns out to be less than 2/3 (Table I) showing that it is a first order transition.

TABLE I. Second order transitions. Calculated values $U^*$ are obtained from fitting to Eq. (15), $T_c$ from Eq. (11), and $\alpha/\nu$ from Eq. (13).

<table>
  <thead>
    <tr>
      <th>$J_2$</th>
      <th>$U^*$</th>
      <th>$T_c$</th>
      <th>$\alpha/\nu$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.5</td>
      <td>0.66656(34)</td>
      <td>2.16(4)</td>
      <td>$-0.15(13)$</td>
    </tr>
    <tr>
      <td>0.6</td>
      <td>0.66648(20)</td>
      <td>2.17(3)</td>
      <td>$-0.13(10)$</td>
    </tr>
    <tr>
      <td>0.7</td>
      <td>0.66648(31)</td>
      <td>2.16(5)</td>
      <td>$-0.17(15)$</td>
    </tr>
    <tr>
      <td>0.8</td>
      <td>0.66653(15)</td>
      <td>2.13(4)</td>
      <td>$-0.13(12)$</td>
    </tr>
    <tr>
      <td>0.85</td>
      <td>0.66655(30)</td>
      <td>2.16(4)</td>
      <td></td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>0.66660(8)</td>
      <td>2.46(3)</td>
      <td>$-0.10(3)$</td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>0.66664(15)</td>
      <td>2.53(6)</td>
      <td>$-0.10(7)$</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>0.66665(10)</td>
      <td>2.60(4)</td>
      <td>$-0.11(9)$</td>
    </tr>
  </tbody>
</table>

![](./images/812139449096863745_4.jpg)

FIG. 4. Size dependence of Binder fourth energy cumulant minima, calculated by optimized reweighting for $J_1$=1.0, $J_2$=0.7, and $J_3$=3.0. Transition from (a) isotropic to hexatic phase (second order), and (b) hexatic to hexatic+herringbone phase (first order). Solid lines represent fits to Eq. (15).

Since no hysteresis, discontinuities, or double peaked $P(E)$ were observed in our simulation, we proceed to determine the order of the transition by scaling of the specific heat with lattice size and the determination of $U^*$, which is the most reliable method.

### III. RESULTS AND DISCUSSION

In our work, at least five histograms were combined for each lattice size for different temperatures near $T_c$. For each histogram, we performed $5\times10^5$ MCS for equilibration and $1\times10^6$ for data collection, while 10-20 Monte Carlo sweeps were discarded between successive measurements to decrease the correlation between them. Because the energy spectrum is continuous, the data list obtained from a simulation is basically a histogram with one entry per energy value. In order to use the histogram method efficiently, we divide the energy range $E\leq0$ into 20 000 and 200 000 bins and reconstructed the histograms. The results of the two binnings agreed with each other within statistical errors. Therefore we chose 20 000 bins throughout our simulation. In all simulations we fixed $J_1$=1.0 and $J_3$=3.0 and changed the values of $J_2$ from 0.5 to 1.3.

Starting from $J_2$=0.5, for all lattice sizes, we observed two peaks in specific heat and two minima in the Binder fourth energy cumulant vs temperature in the cooling run

![](./images/812139449096863745_5.jpg)

FIG. 5. Size dependence of the specific heat maxima $C_{max}$ calculated by optimized reweighting for $J_1$=1.0, $J_2$=0.7, and $J_3$=3.0. Transition from (a) isotropic to hexatic phase, and (b) hexatic to hexatic+herringbone phase. Solid lines represent fits to Eq. (13) for (a) and Eq. (10) for (b).

![](./images/812139449096863745_6.jpg)

FIG. 6. Scaling of the effective transition temperatures with lattice size for $J_1$=1.0, $J_2$=0.7, and $J_3$=3.0. The $T_c$'s were obtained from the location of the maxima of specific heat and minima of the Binder fourth energy cumulant. Transition from (a) isotropic to hexatic phase, and (b) hexatic to hexatic+herringbone phase. The solid lines represent fits to Eq. (14) for (a) and Eq. (11) for (b).

(see Figs. 1 and 3). By increasing the value of $J_2$ those two peaks and minima get closer to each other. As for $J_2$=0.8 the first peak changes to be like a shoulder, while the two minima continue to be well separated. This behavior can be traced until $J_2$=0.9 for which the two transitions merge with each other. For $J_2 \geqslant$0.9, also one peak and a minimum are obtained, suggesting that $J_2$=0.9 can be considered as a critical end point in our simulation, above which only one transition from the disordered to the hexatic+herringbone phase would occur.

In what follows, we discuss separately the three transitions: (1) isotropic-hexatic, (2) hexatic-hexatic +herringbone (locked phase), and (3) isotropic-hexatic +herringbone.

### A. Isotropic-hexatic transition

Using the Binder fourth energy cumulant to determine the order of transition, we found that for all of those transitions for $J_2$=0.5,0.6,0.7,0.8,0.85, the minimum value of $U_L(U^*)$ tends to 2/3 within the statistical error of the simulation. For example in Fig. 4(a) we have plotted $U_L$ vs $L^{-3}$ for $J_2$=0.7. The best fitting of the data to Eq. (15), by using the least squares procedure, shows that $U^*$=0.666 47(31), which is equal to 2/3 within one standard deviation. This is true for all isotropic-hexatic transition points (Table I). These results show that to the resolution of our simulation all of these transitions are second order.

To calculate the critical exponents we used the scaling relation of the maximum values of heat capacity per site ($C_{max}$) versus lattice sizes. The small range of the values of $C_{max}$ (i.e., 2.54 for $L$=6 to 3.0 for $L$=12 for $J_2$=0.7) measured for all points along this critical line is characteristic of transitions with a cusp singularity in the specific heat with $\alpha \sim 0$. Figure 5(a) shows the best fit to $C_{max}$ as a power law in lattice size [Eq. (13)], representing $\alpha/\nu$=-0.17(15) with relatively large error. However, the calculating of the exact values of the critical exponent is not our main purpose, What is important for us is this point that this transition line shows no universality class other than $XY$ universality.

For calculation of the critical temperatures, we used the power law relation (14) for fitting the effective transition temperatures achieved by determining the location of the specific heat maxima and Binder cumulant minima [Fig. 6(a)]. All the calculated quantities discussed above, for this transition line, are listed in Table I.

<table>
<caption>TABLE II. First order transitions. Calculated values of straight line slope $c_2$ are obtained from fitting the data to Eq. (10), $U^*$ from Eq. (15), $T_c$ from Eq. (11), and discontinuity of energy per site ($\Delta e$) from averaging between Eqs. (12) and (17).</caption>
<thead>
<tr>
<th>$J_2$</th>
<th>$c_2$</th>
<th>$U^*$</th>
<th>$T_c$</th>
<th>$\Delta e$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>0.00353(35)</td>
<td>0.66630(10)</td>
<td>1.254(3)</td>
<td>0.159(16)</td>
</tr>
<tr>
<td>0.7</td>
<td>0.00332(15)</td>
<td>0.66587(11)</td>
<td>1.705(1)</td>
<td>0.209(24)</td>
</tr>
<tr>
<td>0.8</td>
<td>0.00230(8)</td>
<td>0.6660(30)</td>
<td>1.930(9)</td>
<td>0.185(37)</td>
</tr>
<tr>
<td>0.9</td>
<td>0.00225(28)</td>
<td>0.66558(31)</td>
<td>2.110(8)</td>
<td>0.210(19)</td>
</tr>
<tr>
<td>0.95</td>
<td>0.00264(90)</td>
<td>0.66574(35)</td>
<td>2.186(4)</td>
<td>0.213(39)</td>
</tr>
<tr>
<td>1.0</td>
<td>0.00267(50)</td>
<td>0.66476(10)</td>
<td>2.283(7)</td>
<td>0.252(29)</td>
</tr>
</tbody>
</table>

### B. Hexatic to hexatic+herringbone transition

The transition from the hexatic phase with long range $XY$ order to the hexatic+herringbone phase, which possesses the three-state Potts symmetry, is known to be in the three-state Potts universality class in 3D and hence weakly first order. This is verified by the procedure discussed in the previous subsection. Figures 4(b), 5(b), and 6(b) show the size dependence of $U_L$, $C_{max}$, and $T_c$ for $J_2$=0.7. As can be seen $U^*$=0.665 78(10) which is less than 2/3 within one standard deviation. The latent heat per site averaged from Eqs. (12) and (17) is derived to be about 0.21 in units of $J_1$. The calculated quantities for other values of $J_2$ (0.5,0.8,0.90) has been listed in Table II. In the resolution of our simulation, $J_2$=0.9 is the end point of the isotropic-hexatic critical line [20,21].

### C. Isotropic to hexatic+herringbone transition

For $J_2>0.9$ only one transition would appear, in which the hexatic and herringbone orders are established simulta- neously. It can be seen from the data listed in Tables I and II that this transition is first order for $J_2$=0.9,0.95,1.0, while it changes to second order for $J_2$=1.1,1.2,1.3. The size dependence of $U_L$, $C_{max}$, and $T_c$ for $J_2$=1.0 and $J_2$=1.2, together with the best fits to the data, are shown in Figs. 7–12. As it is seen from Table I, all specific heat exponents calculated for $J_2>1.1$ are negative and equal to the measurement errors, suggesting that all belong to the same universality class. The other important result here is the existence of a tricritical point located between $J_2$=1.0 and $J_2$=1.1. In Fig. 13 the phase diagram of the BA Hamiltonian, obtained from Monte Carlo simulation, has been depicted.

![](./images/812139449096863745_7.jpg)

FIG. 7. Size dependence of Binder fourth energy cumulant minima, calculated by optimized reweighting for $J_1$=1.0, $J_2$=1.0, and $J_3$=3.0 at the transition point from isotropic to hexatic+herringbone phase. Solid line represents fit to Eq. (15); the obtained value $U^*$=0.664 75(10)<2/3 indicates a first order transition.

![](./images/812139449096863745_8.jpg)

FIG. 8. Size dependence of the specific heat maxima $C_{max}$ calculated by optimized reweighting for $J_1$=1.0, $J_2$=1.0, and $J_3$=3.0 at the transition point from isotropic to hexatic+herringbone phase. Solid line represents fit to Eq. (10).

![](./images/812139449096863745_9.jpg)

FIG. 9. Scaling of the effective transition temperatures with lattice size, for $J_1$=1.0, $J_2$=1.0, and $J_3$=3.0. The $T_c$’s were obtained from the location of the maxima of specific heats and minima of Binder fourth energy cumulants. Solid lines represent fit (11).

### IV. CONCLUSION

In summary, employing the optimized Monte Carlo simulation based on the multihistogram method, we investigated the phase diagram associated with the Hamiltonian suggested by Bruinsma and Aeppli, which consists of two coupled $XY$ order parameters (indicating hexatic and short range herringbone orders), in the regime where the two order parameters are coupled strongly. The simulation reveals three distinct

![](./images/812139449096863745_10.jpg)

FIG. 10. Size dependence of Binder fourth energy cumulant minima, calculated by optimized reweighting for $J_1$=1.0, $J_2$=1.2, and $J_3$=3.0. Solid line represents fit to Eq. (15).

phases for this model. According to the simulation results, the transition from isotropic to only hexatic phase remains second order all over on this transition line, ruling out the existence of any tricritical point on this line. It is also found that the transition from the hexatic to locked phase (hexatic +herringbone) is always weakly first order. These two transition lines meet each other at a critical end point characterized by $J_2/J_1$=0.9 and $T_c/J_1$=2.110(8). For $J_2/J_1>0.9$, however, only one transition occurs from the isotropic to the locked phase whose order is found to be weakly first order up to $J_2/J_1$=1.0 and turned to second order for $J_2/J_1\geqslant1.1$, for which all calculated specific heat exponents are negative and equal within the simulation errors. It shows that all these continuous transitions are in the same universality class. However, for the interval $1.0<J_2/J_1<1.1$, there may be the possibility that the heat capacity critical exponent ($\alpha$) exhibits an evolution from being negative for $J_2/J_1$=1.1 to a large positive value near $J_2/J_1$=1.0. Checking this idea requires more accurate and higher resolution simulations to determine the critical exponents and is the subject of our present research.

![](./images/812139449096863745_11.jpg)

FIG. 11. Size dependence of the specific heat maxima $C_{max}$ calculated by optimized reweighting for $J_1$=1.0, $J_2$=1.2, and $J_3$=3.0 at the transition point from isotropic to hexatic+herringbone phase. Solid line represents fit to Eq. (13), indicating a second order transition with negative value for specific heat anomaly exponent $\alpha$.

![](./images/812139449096863745_12.jpg)

FIG. 12. Scaling of the effective transition temperatures with lattice size for $J_1$=1.0, $J_2$=1.2, and $J_3$=3.0. The $T_c$'s were obtained from the location of the maxima of specific heats and minima of Binder fourth energy cumulants. Solid lines represent fit (14) with value 0.69(3) for exponent $\nu$.

The last result then also suggests the existence of a tricritical point between $J_2/J_1$=1.0 and $J_2/J_1$=1.1, providing a plausible explanation for large heat capacity anomaly exponents, observed in the experiments, in terms of the occurrence of a SmA-HexB transition (which in our simulation is represented as a transition from the disorder phase to a phase consisting of both long range hexatic and short range herringbone orders), near this tricritical point. Knowing that $d$=3 is the upper critical dimension for the tricritical point, the deviation of the experimentally measured heat capacity exponent ($\alpha$$\sim$0.6) from the mean field value $\alpha$=0.5 may be related to the logarithmic corrections arising from marginal fluctuations at the tricritical point. However, while it is a convincing argument, the question remains why seven different liquid crystal compounds $nm$OBC and five binary mixtures $n$(10)OBC, with very different SmA-HexB temperature

![](./images/812139449096863745_13.jpg)

FIG. 13. Schematic of the phase diagram obtained from simulation. Transition temperatures (in units of $J_1$) versus $J_2/J_1$. Three phases, isotropic, hexatic, and hexatic+herringbone, are shown and the dashed lines are just representing the separation of the distinct phases. The region specified by the circle is the tricritical region where the order of the transition changes from being first order for $J_2/J_1$=1.0 to second order for $J_2/J_1$=1.1.

ranges (which affect the coupling of two order types) yield approximately the same value $\alpha \approx 0.6$ and should all be in the immediate vicinity of a particular thermodynamic point.

As an open problem, we address the study of the weak coupling model which might be important for the case of the Sm$A$-Hex$B$ transition in a mixture of 3(10)OBC and PHOAB that possesses a very large temperature range for the Hex$B$ phase above the crystallization temperature to the Cry$E$ phase, yet exhibits the same unusual critical exponents [6].

Another important issue is the possibility of the existence of long range herringbone order in a system with long range orientational order and short range translational order, as suggested by thin film heat capacity data [6].

We finally hope that our work will motivate further theoretical, numerical, and experimental investigations of this very interesting problem.

## ACKNOWLEDGMENTS

We would like to thank M. J. P. Gingras for very useful comments and discussions. F.S. was financially supported in part by IUT Grant No. 1PHB821.

[1] J. M. Kosterlitz and D. J. Thouless, J. Phys. C 6, 1181 (1973); J. M. Kosterlitz, ibid. 7, 1046 (1974).

[2] B. I. Halperin and D. R. Nelson, Phys. Rev. Lett. 41, 121 (1978); D. R. Nelson and B. I. Halperin, Phys. Rev. B 19, 2457 (1979).

[3] A. P. Young, Phys. Rev. B 19, 1855 (1979).

[4] K. J. Strandburg, Rev. Mod. Phys. 60, 161 (1988).

[5] R. J. Birgeneau and J. D. Lister, J. Phys. (Paris), Lett. 39, L339 (1978).

[6] C. C. Huang and T. Stoebe, Adv. Phys. 42, 343 (1993); T. Stoebe and C. C. Huang, Int. J. Mod. Phys. B 9, 2285 (1995).

[7] R. Pindak et al., Phys. Rev. Lett. 46, 1135 (1981).

[8] C. C. Huang et al., Phys. Rev. Lett. 46, 1289 (1981).

[9] T. Pitchford et al., Phys. Rev. A 32, R1938 (1985).

[10] T. Stoebe, C. C. Huang, and J. W. Goodby, Phys. Rev. Lett. 68, 2944 (1992).

[11] J. C. LeGuillou and J. Zinn Justin, J. Phys. (Paris), Lett. 46, L137 (1985).

[12] R. Bruinsma and G. Aeppli, Phys. Rev. Lett. 48, 1625 (1982).

[13] M. J. P. Gingras, P. C. W. Holdworth, and B. Bergersen, Europhys. Lett. 9, 539 (1989); Phys. Rev. A 41, 3377 (1990); 41, 6786 (1990).

[14] M. J. P. Gingras, P. C. W. Holdworth, and B. Bergersen, Mol. Cryst. Liq. Cryst. 204, 177 (1991).

[15] M. Kohandel, M. J. P. Gingras, and J. P. Kemp, Phys. Rev. E 68, 041701 (2003).

[16] F. Shahbazi and M. J. P. Gingras (unpublished).

[17] I. M. Jiang et al., Phys. Rev. E 48, R3240 (1993).

[18] I. M. Jiang, T. Stoebe, and C. C. Huang, Phys. Rev. Lett. 76, 2910 (1996).

[19] I. M. Jiang and C. C. Huang, Physica A 221, 104 (1995).

[20] A. M. Ferrenberg and R. H. Swendsen, Phys. Rev. Lett. 63, 1195 (1989).

[21] D. P. Landau and K. Binder, A Guide to Monte Carlo Simulations in Statistical Physics (Cambridge University Press, Cambridge, U.K., 2000).

[22] M. S. S. Challa, D. P. Landau, and K. Binder, Phys. Rev. B 34, 1841 (1986).

[23] J. Lee and J. M. Kosterlitz, Phys. Rev. B 43, 3265 (1991).