# New Approach to Spin-Glass Simulations

Bernd A. Berg $^{(1),(2)}$ and Tarik Celik $^{(1),(a)}$

$^{(1)}$Supercomputer Computations Research Institute, Tallahassee, Florida 32306
$^{(2)}$Department of Physics, The Florida State University, Tallahassee, Florida 32306
(Received 13 April 1992)

We present a recursive procedure to calculate the parameters of the recently introduced multicanonical ensemble and explore the approach for spin glasses. Temperature dependence of the energy, the entropy, and other physical quantities are easily calculable and we report results for the zero-temperature limit. Our data provide evidence that the large $L$ increase of the ergodicity time is greatly improved. The multicanonical ensemble seems to open new horizons for simulations of spin glasses and other systems which have to cope with conflicting constraints.

PACS numbers: 75.10.Nr

The theoretical understanding of spin glasses (for a review, see Ref. [1]) has remained a great challenge. In particular, the low-temperature limit leaves many open questions about the effects of disorder and frustration. For instance, it has remained controversial whether Parisi's [2] mean-field theory provides the appropriate description for 3D spin glasses. The attractive alternative is the droplet model [3], which in turn is equivalent to a one-parameter scaling picture [4]. The simplest spin-glass system to study such questions numerically is the Edwards-Anderson model. In its Ising version it is described by the Hamiltonian
$$
H=-\sum_{\langle i j\rangle} J_{i j} s_{i} s_{j}, \tag{1}
$$
where the sum goes over nearest neighbors and the exchange interactions $J_{i j}=\pm 1$ between the spins $s_{i}=\pm 1$ are quenched random variables. In our investigation we impose the constraint $\sum J_{i j}=0$ for each realization. Recent simulations [5] of the 3D model in a magnetic field support the mean-field picture. However, one may argue that sufficiently low temperatures on sufficiently large systems cannot be reached without destroying the thermodynamic equilibrium [6].

Low-temperature simulations of spin glasses suffer from a slowing down due to energy barriers. To illustrate the problem, let us consider a simple ferromagnet: the 2D Ising model on a $50\times 50$ lattice. In Fig. 1 we give its magnetic probability density versus $\hat{\beta}=T^{-1}$. The two distinct branches below the Curie temperature are associated with free-energy valleys in configuration space, each of which defines a (pure) thermodynamic state. For low enough temperature, spin-glass systems are supposed to split off into many thermodynamic states, separated by similar tunneling barriers as the two pure states of the Ising model. The physics of the barriers is far less understood than in the ferromagnetic case. As detailed finite-size scaling (FSS) studies do not exist, it is unclear to us to what extent these barriers depend on the system size, whereas the temperature dependence has been investigated [1].

Most Monte Carlo (MC) simulations concentrate on importance sampling for the canonical Gibbs ensemble (a notable exception are microcanonical simulations, but for the ergodicity problems on which we focus here they perform even worse than the canonical approach does). We suggest that in a large class of situations, in particular those where canonical simulations face severe ergodicity problems, it is more efficient to reconstruct the Gibbs ensemble from a simulation of a multicanonical ensemble [7] than to simulate it directly. The multicanonical ensemble is attractive for spin-glass investigations, because equilibrium simulations of this ensemble allow us to overcome low-temperature tunneling barriers by connecting back to the high-temperature region.

In canonical simulations configurations are weighted with the Boltzmann factor $P_{B}(E)=\exp (-\hat{\beta} E)$. Here $E$ is the energy of the system under consideration. The resulting canonical probability density is
$$
P_{c}(E) \sim n(E) P_{B}(E), \tag{2}
$$
where $n(E)$ is the spectral density. In order of increasing severity, the problems with canonical spin-glass simulations are the following: (i) Simulations at many tempera-

![](./images/812746105442795521_1.jpg)

FIG. 1. Ising model magnetic probability density from $50\times 50$ lattice.

tures are needed to get an overview of the system. (ii) The normalization in Eq. (2) is lost. It is tedious to cal- culate important physical quantities like the free energy and the entropy. (iii) The low-temperature ergodicity time $\tau_{L}^{f}$ diverges fast with lattice size (either exponential ly or with a high-power law). The relative weights of pure states can only be estimated for small systems.

Let us choose an energy range $E_{min} \leq E \leq E_{max}$ and define for a given function $\beta(E)$ the function $\alpha(E)$ by $\alpha(E-4)=\alpha(E)+[\beta(E-4)-\beta(E)] E, \alpha(E_{max})=0$ . The multicanonical ensemble [7] is then defined by weight factors
$$P_{M}(E)=\exp [-\beta(E) E+\alpha(E)],\qquad(3)$$
where $\beta(E)$ is determined such that for the chosen energy range the resulting multicanonical probability density is approximately flat,
$$P_{\mathrm{mu}}(E)=c_{\mathrm{mu}} n(E) P_{M}(E) \approx \text { const }.\qquad(4)$$

In the present study we take $E_{max }=0[\beta(E) \equiv 0$ for $E ≥E_{max }]$ and $E_{min }=E^{0}$ the ground-state energy of the considered spin-glass realization.

A multicanonical function $\beta(E)$ can be obtained via re cursive MC calculations. One performs simulations $\beta^{n}(E), n=0,1,2,...$ , which yield probability densities $P^{n}(E)$ with medians $E_{median }^{n}$ . For $E<E_{min }^{n}<E_{median }^{n}$ the probability density $P^{n}(E)$ becomes unreliable due to insufficient statistics, caused by the exponentially fast falloff for decreasing $E$ . We start off with $n=0$ and $\beta^{0}(E) \equiv 0$ . The recursion from $n$ to $n+1$ reads
$$\beta^{n+1}(E)= \begin{cases}\beta^{n}(E) \text { for } E \geq E_{\text {median }}^{n} ; \\ \beta^{n}(E)+0.25 \ln \left[P^{n}(E+4) / P^{n}(E)\right] \text { for } E_{\text {median }}^{n}>E \geq E_{\text {min }}^{n} ; \\ \beta^{n+1}\left(E_{\text {min }}^{n}\right) \text { for } E<E_{\text {min }}^{n}.\end{cases}\qquad(5)$$

Here the $n$ th simulation may be constrained to $E$  $<E_{median }^{n-1}$ by rejecting all proposals with energy $E$ > E", but one has to be careful with such bounds in order to maintain ergodicity. The recursion is stopped for $m$ with $E_{min }^{m-1}=E^{0}$ being the ground state. The actuallyencountered average values for $m$ were between $m=2$  $(L=4)$ and $m=10(L=48)$ . For the larger lattices the last recursion steps tend to get computationally intensive and up to about $30 \%$ of the total CPU time was spent on the recursion. Presently we are exploring more sophisti- cated techniques which seem to allow considerable speed ups and gains in stability.

Once the functions $\beta(E)$ and $\alpha(E)$ are fixed, the multi canonical simulation exhibits a number of desirablefeatures:
(i) By reweighting with $\exp [-\hat{\beta} E+\beta(E) E-\alpha(E)]$  the canonical expectation values
$$O(\hat{\beta})=Z(\hat{\beta})^{-1} \sum_{E} O(E) n(E) \exp (-\hat{\beta} E),\qquad(6)$$
 where $Z(\hat{\beta})=\sum_{E} n(E) \exp (-\hat{\beta} E)$ is the partition func tion, can be reconstructed for all $\hat{\beta}$ in an entire range $\beta_{ min } \leq \hat{\beta} \leq \beta_{ max }$ . Here $\beta_{ min }=\beta(E_{ max })$ and $\beta_{ max }=\beta(E_{ min })$  follow from the requirement $E_{ max } \geq E(\hat{\beta}) \geq E_{ min }$ , and $E(\hat{\beta})$ is given by (6) with $O(E)=E$ . With our choice $E_{ max }=0$ and $E_{ min }=E^{0}$ ground state, $\beta_{ min }=0$ and $\beta_{ max }$ = oo follows.
(ii) The normalization constant $c_{mu}$ in Eq. (4) follows from $Z(0)=\sum_{E} n(E)=2^{N}$ , where $N$ is the total number of spin variables. This gives the spectral density and al- lows us to calculate the free energy as well as the entropy.
(iii) We conjecture that the slowing down of canonical low-temperature spin-glass simulations becomes greatly reduced. For the multicanonical ensemble it can be ar- gued [7] that single spin updates cause a 1D random walk behavior of the energy $E$ . As $E_{ max }-E_{ min } \sim V$ , one needs V2 updating steps to cover the entire ensemble. For first-order phase transition the observed slowing down was only slightly worse than this optimal behavior.
As an exercise and to check our code on exact results, we performed a multicanonical simulation of the 2D Isingmodel with $0 \leq \hat{\beta}<\infty$ . We kept the time series of $4 \times 10^{6}$  sweeps and measurements on a $50 \times 50$ lattice and verified that the finite lattice specific-heat results of Ferdinand and Fisher [8] are well reproduced. No difficulties are encountered with the multicanonical ensemble when crossing the phase transition point. To explore the possi- bility of zero-temperature entropy calculations, we used $Z(0)=2^{2500}$ as input and obtained $2.07 \pm 0.22$ for the number of ground states. Figure l is produced from the

![](./images/812746105442795521_2.jpg)

FIG. 2. Multicanonical energy density distribution for one L =48 realization.

simulation of this lattice.

After this test we turned to the 2D Edwards-Anderson spin glass. We performed multicanonical simulations on lattices of size $L$=4, 12, 24, and 48. Up to $L$=24 we investigated ten different realizations per lattice and, due to CPU time constraints, we considered only five realizations for the $L$=48 lattice. The multicanonical energy distribution for one of our $L$=48 realizations is depicted in Fig. 2. The falloff for $-e<0$ is like that of the canonical distribution at $\hat{\beta}=0$. For $0 \leq -e < -e^{0}$ an impressive flatness (about 800 energy entries on the lattice under consideration) is quickly achieved by the recursion (5). Close to the ground state some fluctuations are encountered on which we comment elsewhere [9]. They do not pose problems as long as they can be kept within reasonable limits of approximately 1 order of magnitude. As it is not obvious from the scale of the figure, we would like to remark that the ground state is not the state with the lowest number of entries, but a state close to it.

Table I gives an overview of some of our numerical results. To quantify our discussion of the slowing down, we define the ergodicity time $\tau_{L}^{e}$ as the average number of sweeps needed to move the energy from $E_{\text{max}}$ to $E_{\text{min}}$ and back. A sweep is defined by updating each spin on the lattice once (in the average). For $\beta_{\text{max}}$ we take $\beta(E^{0})$, where it should be noted that due to our computational procedure $\beta(E)$ is a noisy function. The reported values and their error bars are obtained by combining the results from the different realizations, which enter with equal weights. In Fig. 3 we plot the ergodicity time versus lattice size $L$ on a log-log scale. The data are consistent with a straight-line fit ($Q$ denotes the goodness of fit), which gives the finite-size behavior

$$
\tau_{L}^{e} \sim L^{4.4(3)} \text{ sweeps}. \tag{7}
$$

In CPU time this corresponds to a slowing down $\sim V^{3.2(2)}$. The behavior (7) is by an extra volume factor worse than the almost optimal performance we had hoped for. The reasons will be considered elsewhere [9].

We estimate the infinite volume ground-state energy and entropy from FSS fits of the form $f_{L}=f_{\infty}+c/V$. The entropy fit is depicted in Fig. 4, and the energy fit looks similar. Our energy estimate is $e^{0}=-1.394$ $\pm 0.007$, consistent with the previous MC estimate [10] $e^{0}=-1.407 \pm 0.008$ as well as with the transfer matrix result [11] $e^{0}=-1.4024 \pm 0.0012$. Our entropy estimate

<table>
<caption>TABLE I. Overview of some results. For the data points marked with * the statistics for different realizations varies somewhat and average values are given.</caption>
<thead>
  <tr>
    <th>$L$</th>
    <th>Statistics</th>
    <th>$\tau_{L}^{e}$</th>
    <th>$\beta_{\text{max}}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>4</td>
    <td>$10 \times 1\,600\,000$</td>
    <td>$35.3 \pm 2.8$</td>
    <td>$0.75 \pm 0.06$</td>
  </tr>
  <tr>
    <td>12</td>
    <td>$10 \times 760\,000^{*}$</td>
    <td>$2607 \pm 450$</td>
    <td>$1.47 \pm 0.04$</td>
  </tr>
  <tr>
    <td>24</td>
    <td>$10 \times 1\,600\,000$</td>
    <td>$193\,750 \pm 43\,820$</td>
    <td>$2.12 \pm 0.11$</td>
  </tr>
  <tr>
    <td>48</td>
    <td>$5 \times 2\,500\,000^{*}$</td>
    <td>$1\,457\,315 \pm 516\,925$</td>
    <td>$2.22 \pm 0.07$</td>
  </tr>
</tbody>
</table>

![](./images/812746105442795521_3.jpg)

FIG. 3. Ergodicity times vs lattice size on a double log scale.

$s^{0}=0.081 \pm 0.004$ is also consistent with the MC estimate [10] $s^{0}=0.071 \pm 0.007$, but barely consistent with the more accurate transfer matrix result [11] $s^{0}$ $=0.0701 \pm 0.005$.

It is not entirely straightforward to compare multicanonical and standard simulations. For instance, autocorrelation times of multicanonical simulations come out short due to the triviality that the simulation spends most of its time at rather small effective $\beta$ values. Our ergodicity time is a more useful quantity. Although the slowing down (7) is severe, it seems to provide an important improvement when compared with the slowing down which canonical simulations encounter for temperatures below the bifurcation temperature. For $L \geq 24$ canonical simulations [1,12] are unable to equilibrate the systems at the $\beta_{\text{max}}$ values reported in our table since the relaxation time is by far too long. A rough estimate of the canonical ergodicity time may be [1] $\tau_{\text{canonical}}^{e} \sim \text{exp}(C\hat{\beta}-C')$ with $C$ and $C' \approx 11.6$. The scaling with $L$ may then be hidden in the $L$ dependence of our $\beta_{\text{max}}$ values, which is argued to be divergent like $\beta_{\text{max}} \sim \ln(V)$, and this line of reasoning

![](./images/812746105442795521_4.jpg)

FIG. 4. FSS estimate of the infinite volume entropy per spin.

gives a slowing down of a canonical algorithm like $V^{15}$. With $\beta_{\max }=2.12$ (our $L=24$ case) one gets a canonical ergodicity time of order $10^{8}-10^{9}$ when the missing constant is assumed to be of order 1, whereas our $\tau_{24}^{\xi}$ is about $2 \times 10^{5}$.

When one is only interested in ground-state properties, minimization algorithms have to be considered. As a method, simulated annealing [13] stands out because of its generality, although there are more efficient algorithms for special cases, which should be used when appropriate. In simulated annealing the results depend on the cooling rate $r=-\Delta T /$ sweeps. For our model the behavior $e(r)=e^{0}+c r^{1 / 4}$ with $c \approx 0.5$ ( $\Delta T=-0.1$ fixed) is indicated [14]. To find a true ground state, one has to reduce $[e(r)-e^{0}]$ to the order $1 / V$. Assuming that the constant $c$ is volume independent (only the lattice size $100 \times 100$ was considered in [14]), this translates to number of sweeps $\sim V^{4}=L^{8}$, far worse than our Eq. (7). This result is rather amazing as the multicanonical ensemble has eliminated directed cooling and is nevertheless more efficient. If one does not insist on true ground states one can then relax the condition $[e(r)-e^{0}] \sim 1 / V$. For instance, any behavior $[e(r)-e^{0}] \to 0$ with $L \to \infty$ would still give the correct density, and simulated annealing would slow down less dramatically. On the other hand, this would also imply a less stringent multicanonical simulation.

A comparison with the cluster-replica MC algorithm [10] is even less clear cut. The obtained estimates of the ground-state energy and entropy are of an accuracy similar to ours. As one has to simulate many replicas at many $\hat{\beta}$ values a direct comparison is impossible. Clearly, the results reported on slowing down are more promising than ours for the ergodicity time. However, it should be stressed that the multicanonical ensemble is an ensemble and not an algorithm. To try a combination with the cluster-replica MC is an attractive idea.

Our results make clear that the multicanonical approach is certainly a relevant enrichment of the options one has with respect to spin-glass simulations. The similarities of spin glasses to other problems with conflicting constraints [13] suggest that multicanonical simulations may be of value for a wide range of investigations: optimization problems like the traveling salesman, neural networks, protein folding, and others.

We would like to thank Ulrich Hansmann and Thomas Neuhaus for numerous useful discussions. Further, we are indebted to Philippe Backouche, Norbert Schultka, and Unix Guys for valuable help. T.C. was supported by TUBITAK of Turkey and would like to thank Joe Lanutti and SCRI for the warm hospitality extended to him. Our simulations were performed on the SCRI cluster of fast RISC work stations.

After submitting this paper we became aware of work by Marinari and Parisi [15] where similar ideas are pursued.

This research project was partially funded by the Department of Energy under Contracts No. DE-FG05-87ER40319 and No. DE-FC05-85ER2500, and by the NATO Science Program.

(a)On leave of absence from Department of Physics, Hacettepe University, Ankara, Turkey.

[1] K. Binder and A. P. Young, Rev. Mod. Phys. 58, 801 (1986).
[2] G. Parisi, Phys. Rev. Lett. 43, 1754 (1979); J. Phys. A 13, 1101 (1980).
[3] D. A. Fisher and D. A. Huse, Phys. Rev. B 38, 386 (1988).
[4] A. J. Bray and M. A. Moore, in Heidelberg Colloquium on Glassy Dynamics, edited by J. L. van Hemmen and I. Morgenstern, Lecture Notes in Physics Vol. 275 (Springer, New York, 1987).
[5] S. Caracciolo, G. Parisi, S. Patarnello, and N. Sourlas, Europhys. Lett. 11, 783 (1990).
[6] D. A. Fisher and D. A. Huse, J. Phys. I (France) 1, 621 (1991).
[7] B. Berg and T. Neuhaus, Phys. Lett. B 267, 249 (1991); Phys. Rev. Lett. 68, 9 (1992).
[8] A. E. Ferdinand and M. E. Fisher, Phys. Rev. 185, 832 (1969).
[9] B. Berg and T. Celik (to be published).
[10] R. H. Swendsen and J.-S. Wang, Phys. Rev. B 38, 4840 (1988).
[11] H.-F. Cheng and W. L. McMillan, J. Phys. C 16, 7027 (1983).
[12] R. N. Bhatt and A. P. Young, Phys. Rev. B 37, 5606 (1988).
[13] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Science 220, 671 (1983).
[14] G. S. Grest, C. M. Soukoulis, and K. Levin, Phys. Rev. Lett. 56, 1148 (1986).
[15] E. Marinari and G. Parisi, Report No. ROM2F-92-06 1992 (to be published).