# Phase diagram and phase transitions of the adsorbate system $S/Ru(0001)$: a Monte Carlo study of a lattice gas model

G. M. Xiong $^{1}$, C. Schwennicke $^{2}$, H. Pfnür $^{2}$, H.-U. Everts $^{3}$

$^{1}$ Department of Physics, Chengdu University of Science and Technology, Sichuan, Chengdu 610065, People's Republic of China
$^{2}$ Institut für Festkörperphysik, Universität Hannover, Appelstrasse 2, D-30167 Hannover, Germany
$^{3}$ Institut für Theoretische Physik, Universität Hannover, Appelstrasse 2, D-30167 Hannover, Germany

Received: 6 January 1997 / Revised version: 27 May 1997

Abstract. We investigate the phase diagram and the critical properties of the adsorbate system sulphur/ruthenium(0001) in the coverage region $0 < \Theta < 1/3$ using Monte Carlo simulations of a lattice gas model on a triangular lattice. From experiments it is known that for low coverages an island phase appears in the phase diagram of this system at low temperatures. To capture this feature we include in our lattice gas model a weak third neighbour attraction in addition to the repulsive first and second neighbour forces. The phase diagram obtained from simulations of this model is in very good agreement with the experimental phase diagram. The critical properties of the lattice gas model are found to be compatible with the results of experiments on the system sulphur/ruthenium(0001). Finer details of the phase diagram, e. g. the location of tricritical points, which may be difficult to assess experimentally will also be discussed.

PACS: 07.05.Tp; 64.60.Cn; 68.35.Rh

## I. Introduction

Chemisorbed adsorbates on single-crystal surfaces are a suitable testing ground for models and computations concerned with phase transitions in two dimensions. If the adsorption sites are well defined and if the adsorption induced surface relaxation is negligible, lattice gas models provide an appropriate description of the kinetics of such systems in the submonolayer regime. Under these circumstances the comparison of experimental data with the results of simulations of the appropriate lattice gas model provides detailed information about the effective lateral interactions between the adsorbed particles. Experimentally, chemisorbates have been studied extensively, partly because of their technological importance, but in the main because of the interest in the variety of structural phase transitions that can be observed in them. Examples of such studies, where the abovementioned conditions for a lattice gas description have been checked carefully are, however, quite rare. One of the systems which have been investigated thoroughly with regard to these conditions is the adsorbate $S/Ru(0001)$ [1-4]. LEED measurements have revealed unambiguously that for coverages $0 < \Theta \leq 1/3$ the

![](./images/812464033478213634_1.jpg)

Fig. 1. Experimental phase diagram of the system $S/Ru(0001)$ [2]. $A$: coexistence of $p(2 \times 2)$ islands and lattice gas; $B$: $p(2 \times 2)$ phase; $C$: coexistence of $p(2 \times 2)$ and $(\sqrt{3} \times \sqrt{3})R30^{\circ}$ phases; $D$: $(\sqrt{3} \times \sqrt{3})R30^{\circ}$ phase; $E_1$ $\{E_2\}$: coexistence of lattice gas and $p(2 \times 2)$ $\{(\sqrt{3} \times \sqrt{3})R30^{\circ}\}$ phase; $E$: domain wall phase (not considered in the present simulation)

$S$ atoms are exclusively attached to the threefold coordinated $h. c. p.$ sites of the $Ru(0001)$ surface. (The coverage is defined as the number of adsorbed $S$ atoms per surface $Ru$ atom). No measurable surface relaxation has been detected in this coverage region.

The section of the experimental phase diagram relevant for the present study (see [2]) is shown in Fig. 1. Apart from the two homogeneous ordered phases $p(2 \times 2)$ and $(\sqrt{3} \times \sqrt{3})R30^{\circ}$ which occur around the ideal coverages $\Theta = 1/4$ (region $B$) and $\Theta = 1/3$ (region $D$), respectively, four coexistence regions have been observed for $\Theta < 1/3$. For low coverage, $\Theta < 1/4$, and low temperatures, islands of $p(2 \times 2)$ phase coexist with the disordered phase (region $A$). Most prominent in the phase diagram of this system is the extended coexistence region of the two ordered structures $p(2 \times 2)$ and $(\sqrt{3} \times \sqrt{3})R30^{\circ}$ (region $C$). At higher

temperatures this last coexistence region splits into two separate coexistence regions $E_1$ and $E_2$ in which the majority phases of region $C$, $p(2\times 2)$ or $(\sqrt{3}\times\sqrt{3})R30^\circ$, respectively, coexist with the disordered phase. Further interesting structures appear for coverages $\Theta>1/3$. However, for these higher coverages the f.c.c. sites of the $Ru$ surface are increasingly occupied by $S$ atoms. In addition, lattice relaxation has been shown to become important in the domain wall phase (region $E$) [5]. For these reasons a description of the system by a simple lattice gas model for $\Theta>1/3$ would require additional multi-particle interactions [6] which were not considered in our study.

The work we report here complements an earlier simulation study of the system $S/Ru(0001)$ by Sandhoff et al. [7]. In this earlier study a very simple lattice gas model containing only first and second neigbour interactions was shown to be sufficient to reproduce the experimental phase diagram qualitatively in the coverage interval $1/4\leq\Theta\leq1/3$ and for temperatures $T>200K$. It is apparent, however, that this simple model is unable to reproduce the island phase $A$ which appears for low coverages and low temperatures in the experimental phase diagram. A weak attractive third neighbour between the $S$ atoms is necessary to stabilize this phase, and we shall include such a force in our simulations. Furthermore, to achieve an even better agreement with the experiment than in [7] and to clarify finer details of the phase diagram we extend our simulations to considerably larger system sizes than those considered in [7].

In the next section the lattice gas model we use and a few technicalities of the simulations will be discussed. Section 3 contains our results for the phase diagram and for the critical properties of the lattice gas model. We close with a discussion and a brief summary (Sect. 4).

## II. The model

The lattice gas model which we study in this paper is

$$
H_{LG}=\phi_1\sum_{nn}c_ic_j+\phi_2\sum_{nnn}c_ic_j+\phi_3\sum_{nnnn}c_ic_j
\tag{1}
$$

Here, $c_i=0,1$ is the occupation variable of the lattice site $i$, and the sums run over pairs of first ($nn$), second ($nnn$) and third ($nnnn$) neighbour sites of a triangular lattice with $N\times N$ sites. Positive, i. e. repulsive, first and second neighbour interactions $\phi_1$ and $\phi_2$ stabilize the $p(2\times 2)$ structure at $\Theta=1/4$, while the existence of the $(\sqrt{3}\times\sqrt{3})$ structure requires that $\phi_1/\phi_2<1/5$, see [8]. In our simulations we set $\phi_1=1$ which implies that all energies are measured in units of $\phi_1$. With regard to earlier work [7,9] we choose $\phi_2=\phi_1/10$. The magnitude of $\phi_3$ can then be determined by fitting the computed ratio of the transition temperatures at the ideal coverages $\Theta=1/4$ and $\Theta=1/3$ to the experimental value. This yields $\phi_3\simeq-0.02\phi_1$.

To determine the critical points and to find the characteristics of the phase transitions we calculate the specific heat $c$ and the susceptibility $\chi$ in our simulations,

$$
c_N=\frac{N^2}{k_BT}(<\varepsilon^2>_N-<\varepsilon>_N^2),
\tag{2}
$$

$$
\chi_N=\frac{N^2}{k_BT}(<\Psi^2>_N-<\Psi>_N^2),
\tag{3}
$$

where $\varepsilon$ is the energy per site, and $\Psi$ is the order parameter. $<\cdots>_N$ denotes an MC average over an $N\times N$ cell of the triangular lattice with periodic boundary conditions. In the calculation of the susceptibility appropriate order parameters $\Psi_{p(2\times 2)}$ and $\Psi_{\sqrt{3}\times\sqrt{3}}$ have to be used in (3) for the two different ordered structures of the system. Explicit expressions for $\Psi_{p(2\times 2)}$ and $\Psi_{\sqrt{3}\times\sqrt{3}}$ can be found in the literature [10,11].

The ratios $\alpha/\nu$ and $\gamma/\nu$ of critical exponents were obtained from a finite size analysis of $c_N$ and $\chi_N$. We simulated systems with linear sizes $N$ varying between $N=24$ and $N=96$ in steps of 12 (this step size had to be chosen to avoid frustration of the two different periodic structures by the periodic boundary conditions.) The phase diagram was obtained from simulations of the largest system $N=96$. Most of the simulations were performed with Glauber kinetics [12], i. e. without conservation of the particle number. In these simulations the average particle number is controlled by the term $-\mu\sum_{i=1}^{N^2}c_i$ with $\mu$ the chemical potential, which was added to the Hamiltonian equation (1). Then the coverage is obtained as $\Theta(T,\mu)=\frac{1}{N^2}\sum_{i=1}^{N^2}<c_i>_N$. In the $\Theta-T$ diagram lines of constant chemical potential (dotted lines in Fig. 2) were generated by increasing the temperature in steps of 0.0005 to 0.001 (in units of $\phi_1/k_B$) depending on the slope of the resulting lines. (For the sake of brevity we shall call them $\mu$-lines in the following.) Each data point was obtained from $6\cdot10^5$ to $1.2\cdot10^6$ MC sweeps depending on the distance of $T$ from criticalities. With Glauber kinetics it is difficult to tune to coverages within coexistence regions. Therefore, we we also used Kawasaki kinetics [13] for several constant coverages to determine details of the phase diagram.

## III. Phase diagram and critical properties

The $T-\Theta$ phase diagram, as it is obtained from simulations of the $96\times96$ site lattice cell, is shown in Fig. 2. The labeling of the different regions is in correspondence with the labeling of the experimental phase diagram, Fig. 1. The $\mu$-lines shown in this figure correspond to decreasing values of $|\mu|=-\mu$ from left to right. Dashed lines are the loci of second order transitions between the ordered phases and the disordered phase. They were obtained by connecting the positions of the specific heat maxima on the $\mu$-lines. Solid lines are boundaries of coexistence regions.

The leftmost $\mu$-line (labeled 1) corresponds to $\mu=-1.65$. While for $\mu\leq-1.65$ the system is always disordered, the island phase appears when the chemical potential is increased to $\mu=-1.647$. This is evident from the behaviour of the corresponding $\mu$-line (labeled 2). For low temperature this line starts at the coverage $\Theta=1/4$ where the system is in the ordered $p(2\times 2)$ phase. With increasing temperature the coverage decreases abruptly along this line until the system reaches the disordered lattice gas phase. The $\Theta$ interval in which this line is (almost) horizontal is the coexistence region of $p(2\times 2)$ and of disordered lattice gas phase. For $\mu<-1.647$ the coexistence region widens, but

![](./images/812464033478213634_2.jpg)

Fig. 2. Simulated phase diagram; areas are labeled in correspondence with Fig. 1. Solid lines: boundaries of coexistence regions. Dashed lines: critical lines. Dotted lines: lines of constant chemical potential $\mu$ ($\mu$-lines, see main text). Critical point($\circ$): $P_{c}^{D}$ ($\Theta_{c}^{D}=1/3$, $T_{c}^{D} \simeq 0.187$); Tricritical points ($\bullet$): $P_{tr}^{A}$ ($\Theta_{tr}^{A} \simeq 0.21$, $T_{tr}^{A} \simeq 0.07$), $P_{tr}^{B}$ ($\Theta_{tr}^{B}=1/4$, $T_{tr}^{B} \simeq 0.189$) and $P_{tr}^{D}$ ($\Theta_{tr}^{D} \simeq 0.327$, $T_{tr}^{D} \simeq 0.185$). Eutectic point ($\diamondsuit$): $P_{eut}$ ($\Theta_{eut} \simeq$ 0.292, $T_{eut} \simeq 0.158$)

![](./images/812464033478213634_3.jpg)

Fig. 3. Temperature dependence of the specific heat at constant chemical potential in the low coverage region. (Labels (3), (4) and (5) are the labels of the corresponding $\mu$-lines in Fig. 2.) Irregular behaviour occurs in the temperature interval in which the $\mu$-lines cross the coexistence region $A$

it becomes impossible to obtain $\mu$-lines for such values of $\mu$ since the temperature cannot be tuned finely enough. The solid line which limits region $A$ in Fig. 2 is a crude estimate of the boundary of this coexistence region. The left branch connects the left end-points of the straight-lined sections of the $\mu$-lines. The right branch is the $\mu$-line with $\mu=-1.62$. In simulations using Kawasaki kinetics we have found no traces of coexisting phases above this line. The behaviour of the specific heat on $\mu$-lines with $\mu \leq-1.62$ is shown in Fig. 3. While, for $\mu=-1.62$, the specific heat still exhibits a single maximum, it develops irregular structures for $\mu<-1.62$, which indicate the presence of the coexistence

<table>
<caption>Table 1. Ratios of critical exponents obtained from simulations. Exact results are included for comparison</caption>
<tbody><tr><td>$\mu$</td><td>$\Theta$</td><td>$\alpha/\nu$</td><td>$\gamma/\nu$</td></tr>
<tr><td>-1.5</td><td rowspan="3">$<\frac{1}{4}$</td><td>0.528</td><td>–</td></tr>
<tr><td>-1.35</td><td>0.921</td><td>–</td></tr>
<tr><td>-1.14</td><td>1.065$\pm$0.040</td><td>1.763$\pm$0.041</td></tr>
<tr><td colspan="2">$q=4$ Potts</td><td>1</td><td>7/4=1.75</td></tr>
<tr><td>-1.0</td><td rowspan="3">$>\frac{1}{4}$ $<\frac{1}{3}$</td><td>1.13</td><td>–</td></tr>
<tr><td>-0.94</td><td>1.67</td><td>–</td></tr>
<tr><td>-0.93</td><td>1.26</td><td>–</td></tr>
<tr><td>-0.75</td><td>$\frac{1}{3}$</td><td>0.529$\pm$0.044</td><td>1.540$\pm$0.058</td></tr>
<tr><td rowspan="2">q=3 Potts</td><td>crit.</td><td>2/5=0.4</td><td>26/15=$1.\overline{73}$</td></tr>
<tr><td>tricrit.</td><td>10/7$\simeq$1.43</td><td>38/21$\simeq$1.81</td></tr>
</tbody></table>

phase. The lower end-point of the critical line which separates the $p(2 \times 2)$ from the disordered phase is the position of the specific heat maximum for $\mu=-1.62$. This point is our estimate of the position of the tricritical point $P_{tr}^{A}$ on the boundary of the coexistence region $A$.

In perfect agreement with the experimental findings the simulated phase diagram exhibits a wide coexistence region of the $p(2 \times 2)$ and the $(\sqrt{3} \times \sqrt{3})$ structure (region $C$). As has been described by Sandhoff et al. [7], in this region hexagonal droplets of the minority phase $((\sqrt{3} \times \sqrt{3})$ for $\Theta<0.292$, $p(2 \times 2)$ for $\Theta>0.292)$ form within the majority phase. In Fig. 2 it is seen that the $\mu$-lines $e$ and $e_{1}$ which bound region $C$ closely approximate $T=$ const. lines at the top of this region. This demonstrates the quality of our simulation: according to Gibbs's phase rule the upper boundary of region has to be a $T=$ const. line. Regions $E_{1}$ and $E_{2}$ are two further coexistence regions in which the majority phases of region $C$ coexist with disordered lattice gas. The three coexistence regions $C$, $E_{1}$ and $E_{2}$ meet at an eutectic point $P_{eut}$ [7]. Similarly as with region $A$, the solid lines which bound the regions $E_{1}$, $E_{2}$ in Fig. 2 were constructed by connecting the endpoints of the straight-lined sections of the $\mu$-lines which cross these regions.The regions $E_{1}$ and $E_{2}$ end in tricritical points $P_{tr}^{B}$ and $P_{tr}^{D}$. Their precise location in the phase diagram will be the subject of further discussion below.

In Table 1 we list our results for the ratios $\alpha/\nu$ and $\gamma/\nu$ of critical exponents of the lattice-gas model, (1). For comparison we also include the exact values of $\alpha/\nu$ and $\gamma/\nu$ for the critical and the tricritical $q=4$ and $q=3$ Potts models in Table 1 (critical and tricritical exponents are identical for the $q=4$ Potts model [18]). These numerical results were determined from the size dependence of the maxima of the specific heat, $c_{N}^{max} \sim N^{\alpha/\nu}$, and of the susceptibility $\chi_{N}^{max} \sim N^{\gamma/\nu}$ [15]. Since we work with Glauber kinetics, i. e. at constant chemical potential, Fisher renormalization [16] is not needed in the determination of the critical exponents away from the ideal coverages $\Theta=1/4$ and $\Theta=1/3$. At the ideal coverages the phase transitions of the system are predicted to be in the $q=4$ ($\Theta=1/4$) or in the $q=3$ ($\Theta=1/3$) Potts universality class [14]. For $\Theta=1/4$ our results are in very good agreement with this prediction. In fact, in this case the inclusion of the larger system ($N=96$) has led to an improvement over the results of previous simulations which were based on smaller sizes [1,7]. In contrast with this, our results for $\Theta=1/3$ deviate

significantly from the $q=3$ Potts values. Within the limits of uncertainty, they agree with the corresponding results of [1,3,7], i. e. our extended simulation confirms these earlier results. Remarkably, in the experimental values for $\gamma$ and $\nu$, which have been determined in LEED experiments on the system $S/Ru(0001)$ [3], one finds the same tendency as in our results: the agreement between experimental values and the theoretical predictions for $\gamma/\nu$ is better for the transition of the $p(2\times 2)$ phase $(\Theta=1/4)$ than for the transition of the $(\sqrt{3}\times\sqrt{3})$ phase $(\Theta=1/3)$.

On the left hand boundary of region $B$ (dashed line in Fig. 2) the transition of the $p(2\times 2)$ phase is continuous: the specific heat scales as $c_N^{max}\sim N^{\alpha/\nu}$ with the system size $N$. The transition should be in the $q=4$ Potts universality class along this line. Contrary to this expectation we find a rather drastic decrease of $\alpha/\nu$ from the $q=4$ Potts value with $\Theta$ decreasing from $\Theta=1/4$. Most probably, for low coverages $\alpha/\nu$ is underestimated in our simulations because of insufficiently long MC runs: in the diluted region interaction events between lattice gas particles become rare so that extremely long runs would be necessary to simulate the thermodynamic fluctuations in the low coverage regime.

In the region between the ideal coverages, $1/4<\Theta<$ $1/3$, the ratio $\alpha/\nu$ is seen to increase beyond its values at the ideal coverages. This is to be expected, since in this coverage interval the order-disorder transition is of first order so that according to the scaling prediction $c_N^{max}$ and $\chi_N^{max}$ should diverge as $N^2$ with the system size [17]. The deviations from the expected value $\alpha/\nu=2$ show that even with our largest system $N=96$ we have not yet reached the scaling regime.

In order to estimate the location of the tricritical points $P_{tr}^B$, $P_{tr}^D$ we employed two different methods.

(i) Following [7] we computed the coverage fluctuations
$$
\Delta\Theta:=\frac{N^2}{k_BT}(<\Theta^2>_N-<\Theta>_N^2) \tag{4}
$$
for temperatures varying along several $\mu$-lines which cross the coexistence regions $E_1$ or $E_2$. As has been discussed in [7], $\Delta\Theta$ will be structureless for a second order transition whereas it develops a sharp peak, whose height increases with the system size, inside the coexistence region of a first order transition. On approach to the tricritical end-point of a coexistence region the coverage fluctuations decrease, but for a finite system some incipient structure should still be visible in $\Delta\Theta$ at the end-point. In Fig. 4a,b we display $\Delta\Theta$ as obtained from the system size $N=96$ for several values of $\mu$ which correspond to the $\mu$-lines labeled $a-d$ and $a_1-e_1$, respectively, in Fig. 2. In these figures the graphs labeled $a$ and $a_1$ correspond to the ideal coverages of the $p(2\times 2)$ and the $(\sqrt{3}\times\sqrt{3})$ phase, respectively. It is seen that while $\Delta\Theta$ is completely structureless at the transition temperature $T_c^D$ of the $(\sqrt{3}\times\sqrt{3})$ phase (graph $a_1$), some structure remains at the transition temperature $T_{tr}^B$ of the $p(2\times 2)$ phase (graph $a$). This suggests that the transition of the $p(2\times 2)$ phase is tricritical at the ideal coverage $\Theta=1/4$, whereas the $(\sqrt{3}\times\sqrt{3})$ phase undergoes a normal second order transition at $\Theta=1/3$. The small peak in the graph labeled $b_1$ in Fig. 4b indicates that the coexistence region $E_2$ extends to the immediate vicinity of the critical point $P_c^D$. From the position of this peak we estimate $\Theta_{tr}^D\simeq 0.327$, $T_{tr}^D\simeq 0.185$ as the location of the tricritical end-point of the coexistence region $E_2$.

![](./images/812464033478213634_4.jpg)

Fig. 4a,b. Coverage fluctuations at constant chemical potential in the coexistence regions $E_1$ (Fig. 4a) and $E_2$ (Fig. 4b). Labels $a-d$ and $a_1-e_1$ are the labels of the corresponding $\mu$-lines in Fig. 2

(ii) At the transition temperature of a first-order transition the two phases of the system which coexist will generically have different internal energies. In an MC run with the temperature fixed at the transition temperature the system will therefore jump back and forth between these energies. In this situation the probability $\mathscr{P}(E,E+\Delta E)$ of finding the system in an energy interval $[E,E+\Delta E]$ in a long MC run will exhibit two maxima, one at each of the two energies of the coexisting phases. By contrast, for a second order transition $\mathscr{P}$ will have a single maximum. For a finite system there is no sharp distinction between a transition that is weakly first-order and a second-order transition. Thus one might expect to see remnants of the double-maximum structure of $\mathscr{P}(E,E+\Delta E)$ in MC runs performed at a tricritical point. Graphs of $\mathscr{P}(E,E+\Delta E)$ for $\Theta=1/4$ are shown in Fig. 5a. Indeed, the energy distribution develops a double maximum at the critical temperature, i. e. $\mathscr{P}(E,E+\Delta E)$ shows remnants of the two phases that constitute the ad-

![](./images/812464033478213634_5.jpg)

Fig. 5a,b. Probability distributions of the energy, $\mathscr{P}(E, E+\Delta E)$, in the vicinity of the transition temperatures of (a) the $p(2 \times 2)$ phase $(\Theta=0.25)$ and (b) the $(\sqrt{3} \times \sqrt{3})$ phase $(\Theta=0.33)$. (Plots were generated by setting $\Delta=0.001$ in the simulations)

jacent coexistence region $E_{1}$. This lends strong support to the above suggestion that the tricritical endpoint $P_{t r}^{B}$ of this coexistence region is located precisely at the ideal coverage $\Theta=1 / 4$. To check the validity of this criterion for tricritical- ity we also computed $\mathscr{P}(E, E+\Delta E)$ at and in the vicinity of the transition point $P_{c}^{D}$ of the $(\sqrt{3} \times \sqrt{3})$ phase at the ideal coverage, see Fig. 5b. The absence of a double max- imum structure in the energy distribution at the transition temperature $T_{c}^{D}$ fully confirms our previous conclusion that the order-disorder transition of this phase at $\Theta=1 / 3$ is a normal second order transition.

## IV. Discussion and summary
Our simulation study has revealed that a lattice-gas model with repulsive first and second neighbour forces and with a weak third neighbour attraction reproduces in detail the ex- perimental phase diagram of the adsorbate system $S / Ru(0001)$ in the coverage region $0<\Theta<1 / 3$. Our model, (1), contains two adjustable parameters, $\phi_{2} / \phi_{1}$ and $\phi_{3} / \phi_{1}$. With the values we have chosen for these parameters the relative po- sitions of the tricritical point $P_{t r}^{B}$ , of the critical point $P_{c}^{D}$ and of the eutectic point $P_{e u t}$ in the simulated phase dia gram agree within $5 \%$ with the relative positions of the cor responding points in the experimental phase diagram. The simulated value of the temperature ratio $T_{t r}^{A} / T_{t r}^{B}$ of the tri critical points $P_{t r}^{B}$ and $P_{t r}^{A}$ is, however, $25 \%$ below the ex perimental value, i. e. the island phase $A$ extends to higher temperatures than predicted by the simulation. As has been mentioned earlier, the simulation of the lattice gas model is less reliable in the low-temperature low coverage-region, where the island phase occurs, than for higher temperatures and coverages. Therefore, the discrepancy between the ex- perimental boundary of the island phase and the boundary obtained in the simulations is more likely to be due to in- sufficiencies of the simulations than to an inadequacy of the lattice gas model.

The critical properties of the order-disorder transitions of the system $S / Ru(0001)$ at the ideal coverages $\Theta=1 / 4,1 / 3$ have been the subject of a recent experimental study [3]. In this study, the critical exponents $\beta, \gamma$ and $\nu$ were de termined by spot-profile analysis of high resolution LEED data. The experimental values for the ratio $\gamma / \nu$ are compat ible with the results obtained in the present simulation studyfor the phase transitions of the $p(2 \times 2)$ and the $(\sqrt{3} \times \sqrt{3})$  structures. Deviations of the experimentally determined ex-ponents from the theoretically predicted $q=3$ and $q=4$  Potts exponents were attributed to finite size effects caused by steps on the substrate surface. In the present work we find a significant difference in the deviations of the simulated ex- ponents from the theoretical predictions for the two phase transitions. While for the transition of the $p(2 \times 2)$ phase the simulated ratios $\alpha / \nu$ and $\gamma / \nu$ are in very good agreement with the theoretically predicted $q=4$ Potts exponents, there are significant deviations of the simulated values for these ratios from the theoretical prediction for the transition of the $(\sqrt{3} \times \sqrt{3})$ phase which should belong to the $q=3$ Potts uni versality class. It is worth noting that the experimental results show exactly the same behaviour. The theoretical predic- tions are based on Landau-Ginzburg-Wilson Hamiltonians, and these Hamiltonians capture the physics of the underly- ing microscopic Hamiltonians only in the limit of diverging correlation lengths $\xi$ . For finite $\xi$ corrections to these LGW Hamiltonians have to be taken into account whose magni- tude depend on the structure of the underlying microscopic model. Therefore, the different deviations of the simulated ratios $\alpha / \nu, \gamma / \nu$ from the theoretical predictions for the two phase transitions suggest that, while the lattice gas model,(1), is well approximated by the leading order LGW Hamil-tonian in the critical region of the $p(2 \times 2)$ phase, corrections play a significant role in the critical region of the $\sqrt{3} \times \sqrt{3}$  phase. Since both experimental results and simulations agree quite well with respect to the critical properties, the model used seems to be quite realistic for the low coverage regime.

Summarizing, in the coverage range $\Theta<1 / 3$ , both the phase diagram and the critical properties of the system S/Ru(0001) could be quantitatively simulated by a lattice gas model containing only two parameters. Considering the full phase diagram of the system $S / Ru(0001)$ , occupation of the second threefold site and considerable adsorbate in-

duced relaxations require much more complicated models, as mentioned. Given the mostly local nature of the chemi- cal bond formed in this system [5], however, there seems to be a good chance that most properties of the phase diagram even at high coverages can be quantitatively described by a lattice gas model, which includes multi-site interactions, but still contains coverage independent interaction parameters.

The simulations have been carried out on the Cray YMP-EL of the Re- gionales Rechenzentrum Niedersachsen. We would like to thank R. Bock- horst for program optimization. G. M. X.'s research has been supported in part by the National Natural Science Foundation of China.

## References

1. Sokolowski, M.: Doctoral Thesis, TU München(1992)
2. Dennert, R., Sokolowski, M., Pfnür, H.: Surf. Sci. **271**, 1 (1992)
3. Sokolowski, M., Pfnür, H.: Phys. Rev. B **49**, 7716 (1994)
4. Sokolowski, M., Pfnür, H.: Phys. Rev. B **51**, 15 742 (1995)
5. Jürgens, D., Schwennicke, C., Pfnür, H.: Surf. Sci. **381**, 174 (1997)
6. Persson, B.N.J.: Surf. Sci. Rep. **15**, 1 (1992)
7. Sandhoff, M., Pfnür, H., Everts, H.-U.: Europhys. Lett. **25**, 105 (1994)
8. Walker, J.S., Schick, M.: Phys. Rev. B **20**, 2088 (1979)
9. Glosli, J., Plischke, M.: Can. J. Phys. **6**, 1515 (1983)
10. Dünweg, B., Milchev, A., Rikvold, P.A.: J. Chem. Phys. **94**, 3985 (1991)
11. Sandhoff, M., Pfnür, H., Everts, H.-U.: Surf. Sci. **280**, 185 (1993)
12. Binder, K., Heermann, D.W.: Monte Carlo Simulation in Statistical Physics, an Introduction. Berlin, Heidelberg: Springer 1988
13. Kawasaki, K.: Kinetics of Ising Models. In: Domb, C., Green, M. S. (eds.) Phase Transitions and Critical Phenomena, Vol. **2**, p.443. New York: Academic Press 1972
14. Schick, M.: Progr. Surf. Sci. **11**, 245 (1981)
15. Nightingale, M.P.: Physica A **83**, 561 (1976); Barber, M.N.: Finite Size Scaling. In: Domb, C., Lebowitz, J.L. (eds.) Phase Transitions and Critical Phenomena, Vol. 8. New York: Academic Press 1983
16. Fisher, M.E.: Phys. Rev. **176**, 257 (1968)
17. Challa, M.S.S., Landau, D.P., Binder, K.: Phys. Rev. B **34**, 1841 (1986)
18. Wu, F.Y.: Rev. Mod. Phys. **54**, 235 (1982)