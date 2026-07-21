# Quasicritical Behavior and First-Order Transition in the $d=3$ Random-Field Ising Model

A. P. Young${}^{(a)}$
Department of Mathematics, Imperial College, London SW7 2BZ, United Kingdom

and

M. Nauenberg
Department of Physics, University of California, Santa Cruz, California 95064

(Received 19 March 1985)

The three-dimensional random-field Ising model is studied by Monte Carlo simulations on $L \times L \times L$ lattices with $L \leqslant 64$. Our results are completely consistent with there being a ferromagnetically ordered state at low temperatures. For $T \to T_{c}^{+}$, the susceptibility and correlation length have effective exponents similar to the pure two-dimensional Ising model. However, for the random-field values studied, the transition is actually first order, driven by large fluctuations in the disconnected correlation functions. We suggest that the transition is first order, even for arbitrarily small values of the random field.

PACS numbers: 75.10.Hk, 05.50.+q

The effect of a quenched random field on the phase transition in Ising systems has been extensively discussed. In a classic paper Imry and $\mathrm{Ma}^{1}$ showed that an ordered ferromagnetic state would break up into domains when a random field is applied if the space dimension, $d$, is less than 2. This suggests that the lower critical dimension, $d_{L}$, for ferromagnetism in random-field systems is $d_{L}=2$. Their argument has subsequently been refined ${}^{2,3}$ to the extent that there is now a rigorous proof $^{3}$ that the ground state in $d=3$ is ferromagnetic for small random fields. This argument can probably $^{3}$ be extended to prove that ferromagnetism also exists at finite temperatures and so there seems little doubt that $d_{L}=2$. Presumably, then, perturbation theory, according to which the critical behavior is that of a pure system in $d-2$ dimensions, ${ }^{4,5}$ is not applicable in $d=3$, since $d_{L}=1$ for the one-dimensional pure Ising model. It also appears probable that some neutron scattering experiments, $^{6}$ which found that the correlation length, $\xi$, remains finite, can be understood in terms of irreversible effects $^{7}$ and are not, therefore, incompatible with $d_{L}=2$.

Assuming, then, that a finite-temperature transition occurs in $d=3$ one can ask about its critical behavior. Experimentally there is evidence $^{8}$ that this is very similar to the pure two-dimensional Ising model; i.e., there appears to be a dimensionality shift of 1. Despite some interesting ideas $^{9}$ this has not been satisfactorily explained in previous work. ${ }^{10-13}$

Here we describe the results of Monte Carlo simulations of the three-dimensional random-field Ising model (RFIM) on lattices with $N=L^{3}$ spins where most of our data are for $L=64$, much larger than in previous $^{10,11}$ numerical studies. Our main results are as follows. An analysis of our data for the correlation length, $\xi$, and susceptibility, $\chi$, in the region above $T_{c}$ where $\xi<<L$ gives $\chi \propto \xi^{2-\eta}$ and $\chi \propto\left(T-T_{c}\right)^{-\gamma}$ with effective exponents
$$
\begin{aligned}
& \eta=0.25 \pm 0.03, \\
& \gamma=1.7 \pm 0.2,
\end{aligned}\tag{1}
$$
which are compatible with the pure two-dimensional Ising exponents, $\eta=\frac{1}{4}, \gamma=\frac{7}{4}$. The disconnected correlation function $\chi^{\text {dis }}$ at $q=0$ [see Eq. (6) below] diverges more strongly than $\chi$, and defining $\chi^{\text {dis }}$ $\propto \xi^{4-\bar{\eta}}$, Schwartz $^{14}$ has shown that for any continuous field distribution one must have $\bar{\eta} \leqslant 2 \eta$ at a second-order phase transition. Because of universality we argue that this should also apply for the binary distribution, Eq. (4), used here if the transition is second order. Our best estimate by directly calculating the $\chi^{\text {dis }}$ is $\bar{\eta} \sim 0.8$, but with sizable errors, so that this is compatible with $\bar{\eta} \leqslant \frac{1}{2}$ from Eq. (1) and $\bar{\eta} \leqslant 2 \eta$. However, a scaling argument shows that the transition cannot be second order unless $d-4+\bar{\eta}>0$, which, combined with the "Schwartz inequality" $\bar{\eta} \leqslant 2 \eta$, gives
$$
2 \eta \geqslant \bar{\eta}>4-d\tag{2}
$$
as a necessary condition for a second-order transition. This is incompatible with $d=3$ and $\eta$ given by Eq. (1). An alternative possibility is that the transition should be first order. Indeed, cooling to somewhat lower temperatures we find a large discontinuity in the magnetization for $L=64$ and random-field value $h_{R}=1$. Qualitatively we find that the transition is first order down to smaller values of $h_{R}$ as we increase the lattice size. Because of the inconsistency in exponents noted above, we suggest that the transition in an infinite system is first order down to arbitrarily small random fields.

We now describe our calculations and results in

more detail. The Hamiltonian is
$$
H=-\sum_{\langle i, j\rangle} J_{i j} S_{i} S_{j}-\sum_{i} h_{i} S_{i},
\tag{3}
$$
where $S_{i}= \pm 1$, the $J_{i j}$ are nearest-neighbor interactions on an $L \times L \times L$ simple cubic lattice, and the $h_{i}$ are quenched random fields with probability distribution
$$
P\left(h_{i}\right)=\frac{1}{2}\left[\delta\left(h_{i}-h_{R}\right)+\delta\left(h_{i}+h_{R}\right)\right].
\tag{4}
$$

We set the nearest-neighbor interaction equal to unity. Periodic boundary conditions are imposed and the spins are flipped with the "heat bath" (Glauber) probability $[1+\exp (\beta \Delta E)]^{-1}$, where $\Delta E$ is the energy change in the flip. The computations were performed on the distributed array processor (DAP) at Queen Mary College, London, and the program updates $14.6 \times 10^{6}$ spins per second. Frequently one imposes a constraint $\sum h_{i}=0$ (exactly) to improve the statistics. This was not done here because we feel that the net uniform field (of order $N^{-1 / 2}$ ) present with random sampling is an important part of the physics of this problem.

It was found useful to calculate separately the connected correlation function, $\chi(\mathbf{q})$, defined by
$$
\chi(\mathbf{q})=N\left[\left\langle S_{\mathbf{q}} S_{-\mathbf{q}}\right\rangle-\left\langle S_{\mathbf{q}}\right\rangle_{T}\left\langle S_{-\mathbf{q}}\right\rangle_{T}\right]_{\mathrm{av}},
\tag{5}
$$
and the disconnected function
$$
\chi^{\mathrm{dis}}(\mathbf{q})=N\left[\left\langle S_{\mathbf{q}}\right\rangle_{T}\left\langle S_{-\mathbf{q}}\right\rangle_{T}\right]_{\mathrm{av}},
\tag{6}
$$
where we define Fourier transforms by $S_{\mathbf{q}}$ $=N^{-1} \sum S_{i} \exp \left(i \mathbf{q} \cdot \mathbf{R}_{i}\right)$. In these equations $\langle\ldots\rangle_{T}$ denotes a statistical mechanics average for a given set of fields and $[\ldots]_{\mathrm{av}}$ indicates a configurational average over the fields. Note that the structure-factor measure in a scattering experiment is the sum, $\chi(\mathbf{q})+\chi^{\mathrm{dis}}(\mathbf{q})$. Assuming that $\chi(\mathbf{q})$ satisfies a scaling form $\chi^{-1}(\mathbf{q})=\xi^{-(2-\eta)} f(q \xi)$, where, for $q \xi \rightarrow 0$, $f(q \xi) \propto 1+(q \xi)^{2}+\ldots$, one can extract $\xi$ from a plot of $\chi^{-1}(\mathbf{q})$ against $q^{2}$. We find that $\chi(\mathbf{q})$ is selfaveraging provided that $\xi<<L . \quad \chi^{\mathrm{dis}}(\mathbf{q})$ is easily evaluated in mean-field theory (MFT) by treating different wave vectors independently; so, for one field configuration, the result is $N \chi^{2}(\mathbf{q})\left|h_{\mathbf{q}}\right|^{2} / T^{2}$. Since $h_{\mathbf{q}}$ is a Gaussian random variable with zero mean and variance $h_{R}^{2} / N$ it follows that the disconnected function is also a random variable, i.e., it is not selfaveraging. Performing a field average yields the well known "Lorentzian-squared" result $\chi^{\text {dis }}(\mathbf{q})$ $=\left[h_{R} \chi(\mathbf{q}) / T\right]^{2}$ in MFT. It has been shown by Schwartz $^{14}$ that in general $\chi^{\mathrm{dis}}(\mathbf{q}) \geqslant C\left[h_{R} \chi(\mathbf{q}) / T\right]^{2}$, where $C$ is a property of the field distribution, $C=1$ for Gaussian fields, $C$ is finite for any continuous distribution, but $C=0$ for the binary distribution used here, Eq. (4). We expect the wave vector dependence to be given by a scaling form
$$
\chi^{\mathrm{dis}}(\mathbf{q})=\xi^{4-\bar{\eta}} g(q \xi)
\tag{7}
$$
which defines $\bar{\eta}$. The "Schwartz inequality" 14 shows that $\bar{\eta} \leqslant 2 \eta$ at a second-order transition for any continuous field distribution and we expect this also to be true for the distribution used here because of universality. As $\xi \rightarrow \infty$ with finite $\mathbf{q}$ the $\xi$ dependence in Eq. (7) must disappear so that $\chi^{\mathrm{dis}}(\mathbf{q}) \propto q^{-(4-\bar{\eta})}$ at $T_{c}$ if the transition is second order. The local quantity $\left[\left\langle S_{i}\right\rangle^{2}\right]_{\mathrm{av}}$, which is obviously finite, is obtained by integration of $\chi^{\text {dis }}(\mathbf{q})$ over $\mathbf{q}$ which shows that $\bar{\eta}$ must satisfy $d-4+\bar{\eta}>0$, which gives Eq. (2).

Figure 1 shows results for $\chi$ against $(T-3.91) / T$ on a log-log plot for $4.05 \leqslant T \leqslant 6.5, L=16,32$, and 64 , and with $h_{R}=1$. Simulation time depended on size and temperature and was 600000 steps per spin for $L=64, T=4.1$, of which 200000 were discarded for equilibration. We checked that equilibrium was reached by doing several such runs for some of the field configurations, starting the spins (a) all up, (b) all down, and (c) in a random configuration, and checking that the results were independent of initial spin configuration. For one set of fields we checked

![](./images/813316574105567233_1.jpg)

FIG. 1. Plot of the susceptibility, $\chi$, against $(T-3.91) / T$ on a logarithmic scale for $L=16,32$, and 64 , with $h_{R}=1$ and $4.05 \leqslant T \leqslant 6.5$. The temperature of each point is indicated. The number of field configurations averaged over were four for $L=64$ (except for $T=4.1$ where we used ten), sixteen for $L=32$, and 32 for $L=16$. The inset shows $\chi^{-1}(\mathbf{q})$ against $q^{2}$ for $\mathbf{q}=2 \pi(n, 0,0) / L$ with $L=64$ and $n=0,1,2,3$ at $T=4.1$. The data are an average over ten samples. A straight-line fit works very well so that $\xi$, the correlation length, can be extracted from $\chi^{-1}(\mathbf{q})$ $\propto 1+(\xi q)^{2}+\ldots$ as discussed in the text. This gives $\xi=7.45$.

explicitly that we reached the same state (as opposed to
a different state with the same macroscopic properties)
by computing site magnetizations. Taking data in the
range $4.1 \leqslant T \leqslant 5.0$ and using the largest size avail
able for each temperature, we performed a least-
squares fit by $\log \chi$ against $\log [(T-T_{c}) / T]$ obtaining
$T_{c}=3.91 \pm 0.03$, and $\gamma=1.78 \pm 0.05$. Using $(T-T_{c}) /$
$T$ rather than $(T-T_{c}) / T_{c}$ as a scaling variable we find
that the scaling region is substantially extended. If we
use $(T-T_{c}) / T_{c}$ then, from the data with
$4.1 \leqslant T \leqslant 4.6$, we obtain $T_{c}=3.91 \pm 0.03$ and
$\gamma=1.64 \pm 0.15$. Incorporating both of these estimates
gives the effective $\gamma$ value in Eq. (1). The inset to
Fig. 1 shows a plot of $\chi^{-1}(q)$ against $q^{2}$ for $L=64$,
$T=4.1$, and $q=2 \pi(n, 0,0) / 64$ with $n=0,1,2,3$.
From the straight-line fit one finds $\xi=7.45$, in units of
the lattice spacing.

Estimating the critical exponent $\gamma$ necessitates an es
timate of $T_{c}$ but $\eta$ can be obtained without this uncer
tainty from the plot in Fig. 2 of $\chi$ against $\xi$ on a log-log
scale. The data are fitted by a straight line extremely
well with slope (equal to $2-\eta$ ) of $1.75 \pm 0.03$. This
gives our effective value for $\eta$ in Eq. (1). The results
of Figs. 1 and 2 show that as $T$ is reduced the growth
of fluctuations is similar to that in the pure two-
dimensional Ising model, in agreement with experi-
ment. $^{8}$

![](./images/813316574105567233_2.jpg)

FIG. 2. Results for $\chi$ against $\xi$ on a log-log plot for
$L=64$ and 32 with $h_{R}=1$. Also indicated are the tempera
tures for each data point. The number of field configura-
tions averaged over is the same as for Fig. 1. The points are
fitted very well by a straight line with slope of 1.75. Also
shown are data for the disconnected correlation function $\chi^{dis}$
averaged over sixteen field configurations. The inset shows
data for the magnetization, $m$, of a single $L=64$ sample
with $h_{R}=1$. The crosses are the result of successively cool-
ing down with the field fixed. The circles are obtained by
equilibrating in zero field at $T=3.75$ (this point is marked),
applying the field, and successively warming up. 200 000
iterations were performed at each data point of which
100 000 were discarded for equilibration. A first-order tran-
sition is clearly seen.

Figure 2 also shows a log-log plot of $\chi^{dis}(q=0)$
against $\xi$ for $5.0 \geqslant T \geqslant 4.2$ for sixteen field configura
tions for $L=32$ with $h_{R}=1$. The same sets of random
fields were used at each temperature so that the slope
(equal to $4-\bar{\eta}$ ) has smaller errors than the individual
points, which have large error bars (not shown) be-
cause $\chi^{dis}$ is not self-averaging. Given these uncer
tainties and the curvature in the plot, these data are
compatible with $^{14} \ \bar{\eta} \leqslant 2 \eta \cong 0.5$ which, however,
violates the condition $\bar{\eta}>1$, Eq. (2), for a second-
order transition in $d=3$. Assuming that there is a
transition, $^{3}$ we therefore anticipate that it will ultimate
ly be first order.

Motivated by this we took results for the magnetiza-
tion at lower temperatures. Results for a single $L=64$
lattice are shown in the inset to Fig. 2, both for cooling
and for warming. Note that the hysteresis loop occurs
roughly where we estimated $T_{c}$ from extrapolating data
at higher temperatures. On either side of the hys-
teresis loop the results are independent of past history
and so represent equilibrium values. With $L=64$
equilibration is very rapid below the hysteresis loop
but there is evidence $^{15}$ that relaxation times increase
with system size, which may explain why irreversibility
is much more of a problem in experiments. In a finite
system the magnetization is nonzero above the first-
order jump because the random fields make the mag-
netization distribution nonsymmetric. We looked for a
stable state in the middle of the hysteresis loop, but
the system always found one of the two branches
shown independent of initial magnetization. A second
sample shows very similar behavior. Finite-size ef-
fects are important just above the jump, but not below
it, where the correlation length reaches a maximum
value of about eight lattice spacings. For small ran-
dom fields the transition appears continuous even for
$L=64$, which we interpret as a finite-size effect. At
smaller lattice sizes we need larger fields to see a first-
order jump, consistent with earlier Monte Carlo
work $^{10,16}$ on small lattices. We also note that $h_{R}=1$
lies well below the tricritical value predicted $^{17}$ in MFT,
and furthermore, the first-order transition found here
is driven by fluctuations, completely different from
the mechanism in MFT.

To conclude, we find there is a large temperature
range of "quasicritical" behavior with effective ex-
ponents similar to the exponents of the pure two-
dimensional Ising model. This remains to be under-
stood theoretically. However, the two-dimensional
value of $\eta$ violates the necessary condition $2 \eta>1$ for
a second-order transition. We propose, therefore, that
a fluctuation-driven first-order transition occurs in an

infinite system for any nonzero random field. Howev- er, there are alternatives to the hypothesis that the transition is first order for weak random fields. One possibility is that the effective $\eta$ crosses over to a dif ferent value, consistent with $2 \eta>1$, at very small re duced temperatures $(T-T_{c}) / T_{c}$. Another is that $\eta$ depends on the random field $h_{R}$ and becomes greater than $\frac{1}{2}$ for some value $h_{R}<1.0$ where a tricritical point occurs. We note, however, that neutron scatter- ing measurements in Ref. 8 find $\eta \simeq \frac{1}{4}$ for smaller values of the random field and reduced temperature than ours, and so we feel that the first-order transition hypothesis is the most natural.

After the completion of this paper, we learned that recent neutron scattering experiments $^{18}$ on Mn₀.₇₅Zn₀.₂₅F₂ have been interpreted as giving evi- dence for a discontinuity in the transition in weak ran- dom fields.

We should like to thank A. Aharony, D. Belanger, A. U. Bray, V. Jaccarino, A. King, M. E. Fisher, G. Toulouse, and particularly M. Schwartz for stimu- lating discussions, and J. Cardy, K. Binder, and D. Wallace for helpful correspondence and discussions. We are very grateful to the Science and Engineering Research Council, United Kingdom, for generous pro- vision of computer time on the distributed array pro- cessor (DAP), and appreciate technical advice from K.Smith of the DAP support unit. One of us (M.N.) would like to thank the National Science Foundation for support through Grant No. PHY-81-15541.

(a)Address after August 1985: Department of Physics, University of California, Santa Cruz, Cal. 95064.
¹Y. Imry and S. K. Ma, Phys. Rev. Lett. 35, 1399 (1975).
²D. Fisher, J. Frölich, and T. Spencer, J. Stat. Phys. 34,863 (1984).
³J. Imbrie, Phys. Rev. Lett. 53, 1747 (1984).
⁴A. Aharony, Y. Imry, and S. K. Ma, Phys. Rev. Lett. 37,1364 (1976); A. P. Young, J. Phys. C 10, L257 (1977).
⁵G. Parisi and N. Sourlas, Phys. Rev. Lett. 43, 744 (1979).
⁶H. Yoshizawa, R. A. Cowley, G. Shirane, and R. J. Bir- geneau, Phys. Rev. B 31, 4548 (1985); R. J. Birgeneau, R. A. Cowley, G. Shirane, and H. Yoshizawa, J. Stat. Phys.34, 817 (1984).
⁷J. Villain, Phys. Rev. Lett. 52, 1543 (1984); R. Bruinsma and G. Aeppli, Phys. Rev. Lett. 52, 1547 (1984); G. Grin- stein and J. F. Fernandez, Phys. Rev. B 29, 6389 (1984).
⁸D. P. Belanger, A. R. King, and V. Jaccarino, Phys. Rev. B 31, 4538 (1985); D. P. Belanger, A. R. King, V. Jaccarino, and J. L. Cardy, Phys. Rev. B 28, 2522 (1983).
⁹Y. Shapir, Phys. Rev. Lett. 54, 154 (1985).
¹⁰D. P. Landau, H. H. Lee, and W. Kao, J. Appl. Phys. 49,1356 (1978); E. B. Rasmussen, M. A. Novotny, and D. P. Landau, J. Appl. Phys. 53, 1925 (1983).
¹¹D. Andelman, H. Orland, and L. Wijewordhana, Phys. Rev. Lett. 52, 145 (1984); L. Jacobs and M. Nauenberg, Physica (Utrecht) 128A, 529 (1984).
¹²M. Schwartz, to be published.
¹³A. Khurana, F. J. Seco, and A. Houghton, Phys. Rev. Lett. 54, 357 (1985).
¹⁴M. Schwartz and A. Soffer, to be published; M. Schwartz, private communication.
¹⁵D. Stauffer, C. Hortzstein, K. Binder, and A. Aharony, Z. Phys. B 55, 325 (1984).
¹⁶However, for smaller lattices we have found that these first-order jumps are very dependent on the random-field configurations; see also Jacobs and Nauenberg, Ref. 11.
¹⁷A. Aharony, Phys. Rev. B 18, 3318 (1978). Recently, improved mean-field calculations have been carried out byH. Yoshizawa and D. P. Belanger, Phys. Rev. B 30, 5220(1984); by C. Ro, G. S. Gress, C. M. Soukoulis, and K. Levine, Phys. Rev. B 31, 1682 (1985); and by M. Nauen- berg and A. P. Young, unpublished. In our calculations for the RFIM in $d=1,2$, and 3 and those of Yoshizawa and Be langer, one finds a succession of discontinuities in the mag- netization as a function of temperature, corresponding to the formation of domains in this approximation. This differs from the results of Ro et al., who commented that the domain state they find might give rise to a first-order transition. However, it is well known that mean-field ap- proximations which give results independent of dimen- sionality are not a reliable guide to critical behavior.
¹⁸R. J. Birgeneau, R. A. Cowley, G. Shirane, and H. Yosh- izawa, Phys. Rev. Lett. 54, 2147 (1985).