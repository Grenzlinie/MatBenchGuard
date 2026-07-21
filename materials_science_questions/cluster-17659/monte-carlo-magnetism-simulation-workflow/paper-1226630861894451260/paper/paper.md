# Numerical simulations on the $4d$ Heisenberg spin glass

Barbara COLUZZI

October 1994

Dipartimento di Fisica, Università di Roma La Sapienza,
P. Aldo Moro 2, 00185 Roma, Italy

coluzzi@romal.infn.it

## Abstract
We study the $4d$ Heisenberg spin glass model with Gaussian nearest-
neighbor interactions. We use finite size scaling to analyze the data. We
find a behavior consistent with a finite temperature spin glass transition. Our
estimates for the critical exponents agree with the results from $\varepsilon$-expansion.

PACS Numbers 7510N-0270
Preprint Roma1 $n^o$ 1054

The lower critical dimension $d_l$ of the short range models remains one of the most controversial questions in the spin glass [1]-[3] theory. In the last ten years a consis- tent number of works has been devoted to studying the Ising model, which seems to be [4, 5] very close to $d_l$ in $d=3$. In the case of the short range isotropic Heisenberg spin glass, the conclusions of various computer simulations in $d=3$ [6,7] agree that the system is below $d_l$. Using domain wall renormalization group techniques, it was argued [2,3] that $d_l=4$ for this model. To our knowledge, there are no previous numerical simulations on the $4d$ Heisenberg spin glass apart from an early work by Stauffer and Binder [8], which studied the time dependence of the Edward Ander- son order parameter [9] $q_{EA}(t)$ for vector spin glasses from $d=2$ to $d=6$. They observed a change in the behavior of the Heisenberg model in $d=4$ but concluded that probably there was no finite $T$ phase transition.

We have studied the $4d$ isotropic Heisenberg spin glass model with Gaussian nearest-neighbor interactions. We have simulated small lattices (with linear size from $L=3$ to $L=5$), using finite size scaling to analyze the data. Our main conclusion is that $d=4$ seems to be well above the $d_l$ of the model.

After defining the model and the quantities we have measured, we present a theoretical estimate for critical exponents obtained from $\varepsilon$-expansion results [10] and we discuss the computer simulations in some details. Finally, we present the numerical results and the conclusions.

The Hamiltonian of the model is given by

$$
\mathcal{H}[\vec{\sigma}] \equiv-\frac{1}{2} \sum_{i, j=1}^{V} J_{i j} \vec{\sigma}_{i} \vec{\sigma}_{j}
\tag{1}
$$

where the spins $\{\vec{\sigma}_{i}\}$ belong to the unit three-dimensional sphere. The sum runs over the nearest-neighbor pairs in a simple hypercubic lattice with periodic boundary conditions and size $V=L^{4}$. The interactions $J_{i j}$ are quenched independent random variables with a symmetric Gaussian distribution

$$
P\left(J_{i j}\right)=\frac{1}{\sqrt{2 \pi}} e^{-J_{i j}^{2} / 2}
\tag{2}
$$

The spin glass correlation function can be defined as

$$
G_{S G}(r) \equiv \frac{1}{2 V} \sum_{\left|\vec{r}_{i}-\vec{r}_{j}\right|=r} \overline{<\vec{\sigma}_{i} \vec{\sigma}_{j}>^{2}}
\tag{3}
$$

where $<(\cdot)>$ means thermodynamic average and $\overline{(\cdot)}$ means average over samples.


In the thermodynamic limit, in the paramagnetic phase, for distances $r >> \xi_{SG}$ we expect $G_{SG}(r) \propto e^{-r/\xi_{SG}}$, where we have introduced the spin glass correlation length $\xi_{SG}$. The divergence of $\xi_{SG}$ when the critical temperature $T_c$ is approached,

$$
\xi_{SG} \propto (T-T_c)^{-\nu} \tag{4}
$$

is characterized by the critical exponent $\nu$. The power law decay of the correlation function for large $r$ at the critical point,

$$
G_{SG}(r) \propto \frac{1}{r^{d-2+\eta}} \tag{5}
$$

is described by the anomalous dimension $\eta$.

In order to understand the behavior of the model, it is interesting to introduce two independent replicas of the system, with the same disorder configuration. Since we are dealing with a vector spin glass, the overlap is a second-rank tensor in spin space. We can define

$$
q^{\mu\nu} \equiv \frac{1}{V} \sum_{i=1}^V \sigma_i^\mu \tau_i^\nu \tag{6}
$$

where $\{\vec{\sigma}\}$ and $\{\vec{\tau}\}$ are the spins of the two replicas and $\mu, \nu=1,3$ refer to spin components. In our case the system is completely isotropic, therefore we expect to deal with one spin glass order parameter $q$. It is convenient [3] to consider the rotational invariant quantity

$$
Q \equiv \sqrt{\frac{1}{3} \sum_{\mu,\nu=1}^3 (q^{\mu\nu})^2} \tag{7}
$$

The order parameter probability distribution $P(q)$ is correspondingly given by

$$
P(q) \equiv \overline{< \delta(q-Q) >} \tag{8}
$$

One of the quantities we have calculated is the spin glass susceptibility, defined as

$$
\chi_{SG}(L,T) \equiv \frac{3}{V} \overline{< \left( \sum_{i=1}^V \vec{\sigma}_i \vec{\tau}_i \right)^2 >} \tag{9}
$$

It can be easily verified that this definition is equivalent to $\chi_{SG} \equiv 3V \overline{< q^2 >}$, the factor 3 having been inserted to obtain $\lim_{T \to \infty} \chi_{SG}(L,T)=1$, like in the Ising case. In the thermodynamic limit we expect the spin glass susceptibility to diverge when $T_c$ is approached from the paramagnetic phase as

$$
\chi_{SG}(T) \propto (T-T_c)^{-\gamma} \tag{10}
$$

where, by hyperscaling, $\gamma=(2-\eta)\nu$.

If $T_c = 0$ and the system is below $d_l$, we still expect $\xi_{SG}(T)$ and $\chi_{SG}(T)$ to behave near the critical point according to (4) and (10) respectively, diverging with power laws. We expect exponential divergences for $d \to d_l$, because $\nu,\gamma \to \infty$ in this limit. In the $3d$ Ising spin glass the difficulty in distinguishing between the system being at or above $d_l$ [4] is correlated to the large value of $\nu$ obtained from finite size scaling analysis. We will see that this seems not to be the case in our model.

The Binder parameter has proved very successful to establish the presence or the absence of a finite $T$ phase transition. Its definition for the Ising spin glass model [11] can be easily extended to the Heisenberg case. In the high temperature region, where we can neglect interactions, the $q^{\mu\nu}$ are approximately independent variables with the same symmetric Gaussian distribution of width $\sim V^{-1/2}$. The function

$$
g(L,T)\equiv\frac{1}{2}\left(11-9\frac{\overline{<q^4>}}{\left(\overline{<q^2>}\right)^2}\right)
\tag{11}
$$

is a dimensionless parameter defined so that $g \leq 1$. From an explicit calculation, we have obtained $g \sim 1/V$ for $T \to \infty$. In the thermodynamic limit we expect therefore $g(T)=0$ above $T_c$ and $g(T)=1$ for $T=0$. If there is a $T=0$ singularity we expect the curves of $g(L,T)$ against $T$ for different $L$ to come together as $T \to 0$, while for a finite $T$ transition we expect them to intersect at $T_c$, which allows to locate the critical point quite precisely.

The mean field spin glass critical temperature $T_c^{MF}$ for $m$-component spins belonging to the unit sphere, with coordination number $z$ and $\overline{J_{ij}^2}=1$, is approximately, for large $z$, $T_c^{MF} \simeq \sqrt{z}/m$. In our case $m=3$ and $z=8$, so

$$
T_c^{MF} \simeq 0.94
\tag{12}
$$

This value is a reasonable upper limit to the temperature range in which we can expect a phase transition.

If there is a nonzero $T_c$, the behavior of the system at the transition point is characterized by two independent critical exponents. We have obtained a theoretical estimate for the spin glass correlation length exponent $\nu$ and the anomalous dimension $\eta$ from $\varepsilon$-expansion results. This is possible in the Heisenberg case because the coefficients, calculated to the third order by Green [10], show the expected oscillatory behavior:

$$
\begin{aligned}
\eta &= -0.2\,\varepsilon + 7.733\cdot 10^{-2}\,\varepsilon^2 - 7.8127\cdot 10^{-2}\,\varepsilon^3 + O(\varepsilon^4) \\
\nu^{-1}-2+\eta &= -1.2\,\varepsilon + 1.164\,\varepsilon^2 - 1.4735\,\varepsilon^3 + O(\varepsilon^4)
\end{aligned}
\tag{13}
$$

<table>
  <tbody>
    <tr>
      <td colspan="2">$\nu$</td>
      <td colspan="2">$\eta$</td>
    </tr>
    <tr>
      <td>0.7096</td>
      <td>0.8657</td>
      <td>-0.2256</td>
      <td>-0.4945</td>
    </tr>
    <tr>
      <td>0.8224</td>
      <td></td>
      <td>-0.2976</td>
      <td></td>
    </tr>
  </tbody>
</table>

Table 1: $\nu$ and $\eta$ from the corresponding $\mathcal{P}[N,D]$, $N$ being the row and $D$ the column index.

where $\varepsilon = d_u - d = 6 - d$, $d_u = 6$ being the upper critical dimension of short range spin glass models.

We have used the simple resummation method of the Padé approximants, in which the series is replaced by the ratio $\mathcal{P}[N,D]$ of a polynomial of degree $N$ to one of degree $D$. The values obtained for $\varepsilon = 2$ are presented in [Tab. 1]. By comparing results from $\mathcal{P}[1,2]$ and $\mathcal{P}[2,1]$ we can estimate, for the $4d$ Heisenberg spin glass,
$$
\nu \simeq 0.8 \quad \eta \simeq -0.4 \tag{14}
$$
with a larger uncertainty on the value of $\eta$.

We have simulated hypercubic lattices in $4d$ with periodic boundary conditions and linear sizes $L = 3, 4$ and $5$. The number of samples is 400, 200 and 100, respectively. Simulations have been performed in the region $T \leq 1$, down to $T = 0.4$ for $L = 3$, to $T = 0.45$ for $L = 4$ and to $T = 0.5$ for $L = 5$. We will see that $T = 0.5$ seems to be very close to the $T_c$ of our model.

In order to thermalize our samples, we have used Simulated Tempering [12]-[14], already proved very efficient for Ising spin glasses [5, 15]. The system, in our case consisting of two independent replicas, is allowed to change temperature between a fixed set of $\{\beta_n\}$, where we can take for simplicity $\beta_{n+1} > \beta_n$, $\beta = 1/T$ becoming a dynamical variable. The stationary probability distribution for the configuration $C$ at $\beta_n$ is given by
$$
P_{\infty}(C, n) \propto e^{-\mathcal{H}_{tot}[C, n]} \quad \mathcal{H}_{tot}[C, n] \equiv \beta_n \mathcal{H}[C] - g_n \tag{15}
$$
where we have defined the extended Hamiltonian $\mathcal{H}_{tot}[C, n]$, $\{g_n\}$ being a set of arbitrary numbers chosen $a$ priori. After reaching the equilibrium, the system moves between the $\{\beta_n\}$ remaining at the equilibrium. In order to obtain the same stationary probability for all the different temperatures we have to take $g_n = \beta_n F_n$, $F_n$ being the total free energy at $\beta_n$. This means that, for $n' = n \pm 1$, at the first order in $\Delta \beta = (\beta_{n'} - \beta_n)$:
$$
\Delta \mathcal{H}_{tot} = \Delta \beta \mathcal{H} - (g_{n'} - g_n) \simeq \Delta \beta \left( \mathcal{H} - \frac{1}{2}(< \mathcal{H}_{n'} > + < \mathcal{H}_n >) \right) \tag{16}
$$


where $\mathcal{H}$ is the instantaneous value and $<\mathcal{H}_n>$ is the statistical expectation value at $\beta_n$ of the total energy.

Our Simulated Tempering steps are just Monte Carlo steps at the end of which the system is allowed to change temperature, the new $\beta_n$ suggested being $\beta_{n\pm1}$ with equal probability. Obviously during the MC step the two replicas evolve indepen- dently. Since we are dealing with a model with continuous degrees of freedom, there is an arbitrary parameter in the Metropolis algorithm, corresponding to the maxi- mum rotation angle $\theta_{max}$ permitted to single spins in one step. We have chosen $\theta_{max}$ in order to obtain the acceptance as close to $1/2$ as possible.

We have been careful in fixing the set of temperatures for the different sizes. Two contiguous values of $\beta_n$ have to be as different as possible to help in decorre- lating without making too small the corresponding transition probability. We have used as a basic criterion the condition that there was a non-negligible overlap in the values of the energy computed at contiguous $\beta_n$ for each sample. In our case this was verified by choosing equidistant temperatures, with $\Delta T = 0.1$ for $L = 3$ and $\Delta T = 0.05$ for $L = 4$ and $5$. In order to perform simulations down to lower temperatures, particularly in the $L = 5$ case, it would be necessary to decrease $\Delta T$ with a considerable greater amount of computer time.

We have used a slow cooling procedure to take the system near the equilibrium at the lowest temperature. Statistics were collected over the last part of the about $3000\ L\ \beta_n^2$ MC steps at each temperature, to evaluate approximately the corre- sponding $<\mathcal{H}_n>$. The next about $70000$ for $L=3$, $200000$ for $L=4$ and $400000$ for $L=5$ Simulated Tempering steps were used to thermalize the system and to improve iteratively [15] the estimates for the $\{g_{n'}-g_n\}$. Finally, all the quantities we were interested in were calculated in the last part of the Simulated Tempering cycle, of about $140000$ steps for $L=3$, half a million steps for $L=4$ and more than a million steps for $L=5$.

In Simulated Tempering, we can estimate the statistical expectation value $<\mathcal{O}_n>$ of an observable $\mathcal{O}$ at $\beta_n$ as

$$
<\mathcal{O}_{n}>=\frac{1}{\mathcal{N} \overline{f_{n}}} \sum_{t} \mathcal{O}(t) \delta_{\beta(t) \beta_{n}} \quad f_{n} \equiv \frac{1}{\mathcal{N}} \sum_{t} \delta_{\beta(t) \beta_{n}} \tag{17}
$$

where we have defined the frequency $f_n$ observed at $\beta_n$, $\mathcal{N}$ being the total number of steps. With the given choice for the $\{g_n\}$, we expect $f_n \simeq 1/n_T$, $n_T$ being the total number of temperatures considered (in our case, $n_T=7$ for $L=3$ and $n_T=8$ for $L=4$ and $5$). The closeness of the $f_n$ observed at different temperatures represents one of the main verifications that Simulated Tempering works well. In the last part of the cycle we have obtained $\max\{f_n\}<4\min\{f_n\}$ for each sample, the $\overline{f_n}$ being compatible with the expected values for the different $n_T$. We have also checked

how many $n_e$ times the system was moving from one extreme to the other of the temperature range, obtaining for each sample $n_e > 100$ in the $L=3$ case and $n_e > 200$ for $L=4$ and 5, reasonably large values for the system really exploring the entire phase space.

In order to check thermalization, besides verifying that the $< q^{\mu\nu} >$ were compatible with zero for each sample, we have divided the last part of the Simulated Tempering cycle in five equal intervals, checking that the various computed quantities show no evident drifts. This was verified also for the spin glass susceptibility (9) and the fourth moment of the $P(q)$ (8) in the $L=5$ case.

The simulations have taken in all about 6 months of Dec3000-workstation.

Our numerical results for the spin glass susceptibility (9) and the Binder parameter (11) are presented in [Fig. 1] and [Fig. 2] respectively. The behavior of the curves of $g(L,T)$ as a function of $T$ for the different lattice sizes strongly suggests the presence of a finite $T$ spin glass transition, the noncoincidence of the intersection points being presumably due to systematic corrections to finite size scaling. In order to confirm that curves really splay out below the critical point, as expected in the presence of long range spin glass order, it would be obviously preferable to obtain data on the $g(L,T)$ down to lower temperatures and for larger lattice sizes.

If scaling is satisfied, near $T_c$ we expect
$$
\chi_{S G}(L, T)=L^{2-\eta} \tilde{\chi}_{S G}\left(\left(T-T_{c}\right) L^{1 / \nu}\right) \tag{18}
$$
$$
g(L, T)=\tilde{g}\left(\left(T-T_{c}\right) L^{1 / \nu}\right) \tag{19}
$$
where $\tilde{\chi}_{S G}$ and $\tilde{g}$ are scaling functions while $\nu$ and $\eta$ are respectively the spin glass correlation length exponent (4) and the anomalous dimension (5) previously defined.

From the $\chi_{S G}$ scaling law (18), using a standard three-parameter fitting routine, we have obtained
$$
T_{c}=0.50 \pm 0.06 \quad \nu=0.61 \pm 0.08 \quad 2-\eta=1.8 \pm 0.5 \tag{20}
$$
while requiring that the Binder parameter data scale according to equation (19), with a more simple two-parameter fit, we have found
$$
T_{c}=0.52 \pm 0.02 \quad \nu=0.89 \pm 0.06 \tag{21}
$$

In [Fig. 3] and [Fig. 4] we present the corrispondent scaling plots. It must be emphasized that statistical errors quoted here are just a delimitation of the range of values beyond which our data do not scale well. Systematic errors due to corrections to finite size scaling cannot easily be evaluated but could be quite important, because of the small lattice sizes considered.

Our results agree well with a nonzero $T_c$ for the $4d$ short range Heisenberg spin glass (1), giving in this case of Gaussian nearest-neighbor interactions (2) the value $T_c \simeq 0.5$, that is however well below the $T_c^{MF} \simeq 0.94$ (12) of the model.

Systematic corrections to finite size scaling may explain the discrepancy between the estimates for $\nu$ obtained from the $\chi_{SG}$ (20) and the Binder parameter (21) respectively. Our most significant result is nevertheless that $\nu$ seems to be not large, being both values smaller than 1. As we have already pointed out, a large value of $\nu$ would suggest the system being at $d \simeq d_l$, since we espect $\nu, \gamma \to \infty$ for $d \to d_l$. In this case, therefore, the result $\nu < 1$ is consistent with the short range Heisenberg spin glass model being well above $d_l$ in $d=4$.

Comparing the two estimates for $\nu$, we can obtain the approximate value $\nu \simeq 0.75$, that agrees well with the theoretical estimate (14) $\nu \simeq 0.8$. From the hyperscaling law $\alpha=2-d\ \nu$ we can also estimate the corresponding value of $\alpha$, describing the critical behavior of the specific heat. We find $\alpha \simeq -1$, accidentally not far from the mean field value.

Finally, our statistics are inadequate to obtain a significant estimate for $\eta$. The value found from the $\chi_{SG}$ data (20), $2-\eta=1.8\pm 0.5$, is however compatible with the theoretical estimate (14) $\eta \simeq -0.4$, even if not in good agreement.

We have simulated small lattices, with a rather small amount of computer time. More accurate simulations are necessary in order to confirm the presence of a finite $T$ phase transition in the $4d$ short range Heisenberg spin glass model, improving our estimates for critical exponent. Simulated Tempering seems to be highly suitable for this purpose. It might be also interesting to devote some attention to the behavior of the $P(q)$, to our knowledge not yet extensively studied in the case of short range vector models.

I am deeply indebted to G. Parisi for his continuous support. I would also like to thank E. Marinari for many helpful discussions, A. Baldassarri, F. Ritort and J. J. Ruiz for their useful suggestions.

## References

[1] M. Mezard, G.Parisi and M. A. Virasoro, *Spin Glass Theory and Beyond*, World Scientific (Singapore, 1987).

[2] K. H. Fischer and J. A. Hertz, *Spin Glasses*, Cambridge University Press (Cambridge, 1991).

[3] K. Binder and A. P. Young, *Spin Glasses: Experimental Facts, Theoretical Concepts and Open Questions*, Rev. Mod. Phys. **58**, 801 (1986).

[4] E. Marinari, G. Parisi and F. Ritort, *On the 3d Ising Spin Glass*, J. Phys. **A** (Math. Gen.) **27**, 2687 (1994).

[5] E. Marinari, G. Parisi and F. Ritort, in preparation.

[6] J. A. Olive, A. P. Young and D. Sherrington, *Computer Simulation of the Three-Dimensional Short-Range Heisenberg Spin Glass*, Phys. Rev. **B 9**, 6341 (1986).

[7] F. Matsubara, T. Iyota and S. Inawashiro, *Effect of Anisotropy on a Short-Range $\pm J$ Heisenberg Spin Glass in Three Dimension*, Phys. Rev. Lett. **67**, 1458 (1991).

[8] D. Stauffer and K. Binder, *Order Parameters for n-Vector Spin Glasses in d Dimensions*, Z. Phys. **B** (Condensed Matter) **41**, 237 (1981).

[9] S. F. Edwards and P. W. Anderson, *Theory of Spin Glasses*, J. Phys. **F 5**, 965 (1975).

[10] J. E. Green, *$\varepsilon$-Expansion for the Critical Exponents of a Vector Spin Glass*, J. Phys. **A** (Math. Gen.) **17**, L43 (1985).

[11] R. N. Bhatt and A. P. Young, *Serch for a Transition in the Three-Dimensional $\pm J$ Ising Spin- Glass*, Phys. Rev. Lett. **54**, 924 (1985).

[12] B. A. Berg and T. Neuhaus, *Multicanonical algorithms for first order phase transitions*, Phys. Lett. **B 267**, 249 (1991).

[13] B. A. Berg and T. Celik, *New Approach to Spin-Glass Simulations*, Phys. Rev. Lett. **69**, 2292 (1992).

[14] E. Marinari and G. Parisi, *Simulated Tempering: a New Monte Carlo Scheme*, Europhys. Lett. **19**, 451 (1992).

[15] W. Kerlerm and P. Rehberg, *Simulated-Tempering Approach to Spin-Glass Simulations*, preprint cond-mat 9402049.

![](./images/1226630861894451260_1.jpg)

Figure 1: The spin glass susceptibility $\chi_{SG}$ as a function of $\beta$ for the different lattice sizes. Lines are only to join neighboring points.

![](./images/1226630861894451260_2.jpg)

Figure 2: The Binder parameter $g$ as a function of $T$ for the different lattice sizes. Lines are only to join neighboring points.

![](./images/1226630861894451260_3.jpg)

Figure 3: The scaled spin glass susceptibility $\chi_{SG}/L^{2-\eta}$ as a function of the scaled reduced temperature $(T-T_c)L^{1/\nu}$. The line is just guide to the eye.

![](./images/1226630861894451260_4.jpg)

Figure 4: The Binder parameter $g$ as a function of the scaled reduced temperature $(T-T_c)L^{1/\nu}$. The line is just guide to the eye.
