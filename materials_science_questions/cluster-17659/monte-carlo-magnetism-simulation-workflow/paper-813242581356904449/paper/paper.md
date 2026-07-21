# PHYSICAL REVIEW LETTERS

## Volume 58 19 JANUARY 1987 Number 3

## Applications of the Kakutani Metric to Real-Space Renormalization

E. J. Brody
Department of Physics, University of Tokyo, Hongo, Tokyo 113, Japan
(Received 16 July 1986)

Kadanoff transformations are discussed in terms of a metric in the space of Gibbs measures. Direct Monte Carlo computation of this metric is illustrated by trial calculations for small Ising systems. Applications to gauge-field quantization are suggested.

PACS numbers: 05.50.+q, 11.10.Gh, 11.15.Ha, 64.60.-i

If $p(x_i)$ and $q(x_i)$ are probability distributions on a discrete set $X=\{x_i\}$, the quantity
$$
\rho(p,q)=\sum_{i}\left[p(x_i)q(x_i)\right]^{1/2} \tag{1}
$$
is obviously well defined. When $dp$ and $dq$ are arbitrary probability measures on a measurable space $(X,\mathcal{B})$, definition (1) can be naturally extended by choosing any measure $dr$ such that $dp$ and $dq$ are absolutely continuous with respect to $dr$ (e.g., $dr=dp+dq$), and defining
$$
\begin{aligned}
\rho(dp,dq)&\equiv\int_{x}\sqrt{dp}\sqrt{dq}\\
&\equiv\int_{x}(dp/dr)^{1/2}(dq/dr)^{1/2}dr,
\end{aligned}
$$
where $dp/dr$ and $dq/dr$ denote the respective Radon-Nikodym derivatives (in most applications, just probability densities). One easily verifies that (1) $\rho(dp,dq)$ is independent of the choice of $dr$; (2) $0\leq\rho(dp,dq)\leq1$; (3) $\rho(dp,dq)=1$ if and only if $dp=dq$; (4) $\rho(dp,dq)=0$ if and only if $dp\perp dq$ (i.e., $p$ and $q$ are concentrated on disjoint sets); (5) $\Delta(dp,dq)^2\equiv1-\rho(dp,dq)$ defines a metric, $^{1,2}$ called the *Kakutani distance* (KD), in the space of all probability measures on $(X,\mathcal{B})$. Consider two Hamiltonians $S(\sigma)$ and $T(\sigma)$ defined on a configuration space $\Sigma=\{\alpha\}$, and suppose that some convenient Liouville measure $dr(\sigma)$ is defined over a suitable Borel field $\mathcal{B}$ in $\Sigma$. Specifically, $dr(\sigma)$ might be Lebesque measure on a Euclidean space, or the Haar measure on a locally compact group, etc. Suppose that the Gibbs measures $dp(\sigma)$ and $dq(\sigma)$ are defined by the respective Boltzmann factors $e^{-S(\sigma)}$ and $e^{-T(\sigma)}$ relative to $dr(\sigma)$. Then, after the introduction of the mean Hamiltonian $U\equiv(S+T)/2$, straightforward manipulation yields
$$
\begin{aligned}
\rho(p,q)&=\int\left\{\left[e^{-S(\sigma)}\left(\int e^{-S(\sigma)}dr(\sigma)\right)^{-1}\right]\left[e^{-T(\sigma)}\left(\int e^{-T(\sigma)}dr(\sigma)\right)^{-1}\right]\right\}^{1/2}dr(\sigma)\\
&=Z_u/(Z_SZ_T)^{1/2}=1/\left(\langle e^{(T-S)/2}\rangle_u\langle e^{(S-T)/2}\rangle_u\right)^{1/2},
\end{aligned}
\tag{2}
$$
where $Z_u$, $Z_S$, $Z_T$ denote the obvious partition functions and $\langle\ldots\rangle_u$ denotes the average with respect to the Boltzmann weight $e^{-u}$. Thus $\rho(p,q)$ can be computed by weighted Monte Carlo (MC) sampling relative to $U$, *provided* that both $S$ and $T$ are known, and the rate of convergence will be satisfactory, provided that the differences $|S(\sigma)-T(\sigma)|$ are not unduly great. As an example, when one passes through a critical point in the parameter space of a statistical model, one expects a rather abrupt change in the properties of the Gibbs measure. The two-dimensional Ising model has the well-known critical inverse temperature $\beta=\ln(1+\sqrt{2})/2\sim0.44$. Confining myself to multiples of the nearest-

© 1987 The American Physical Society

neighbor Hamiltonian, I computed the KD between the measures $dp_{\beta}$ and $dp_{\beta'}$ corresponding to the values $\beta=(0.1)n$ and $\beta'=(0.1)(n+1)$, respectively, for $n=1,2,\ldots,6$ on a periodic $8\times8$ Ising lattice, using a heat-bath algorithm. After a cold start (i.e., all spins up) followed by 10000 random site selections for each pair $(\beta,\beta')$, the results were as follows (two runs for each pair of values):

<table>
  <thead>
    <tr>
      <th>$n$</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$\Delta_{8\times8}(dp_{\beta},dp_{\beta'})^{2}$</th>
      <td>0.25<br>0.32</td>
      <td>0.51<br>0.43</td>
      <td>0.54<br>0.50</td>
      <td>0.47<br>0.42</td>
      <td>0.33<br>0.27</td>
      <td>0.00<br>0.00</td>
    </tr>
  </tbody>
</table>

For a hot start (completely random configuration) the corresponding results were as follows:

<table>
  <thead>
    <tr>
      <th>$n$</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$\Delta_{8\times8}(dp_{\beta},dp_{\beta'})^{2}$</th>
      <td>0.21<br>0.24</td>
      <td>0.51<br>0.47</td>
      <td>0.53<br>0.61</td>
      <td>0.35<br>0.44</td>
      <td>0.30<br>0.28</td>
      <td>0.38<br>0.35</td>
    </tr>
  </tbody>
</table>

Although the statistical errors were large, as might be expected from the small sample, roughly equivalent to $(10000/64)\sim156$ sweeps, there is a clear indication of a peak in the range $\beta=0.2$ to 0.4, suggesting a significant change in this vicinity. The anomalous results for the cold value $n=6$ after a hot start were undoubtedly due to excessively slow relaxation effects. The exact values computed from the partition functions in formula (2), with the use of the Onsager solution, $^{3}$ are (for $8\times8$ and $4\times4$ lattices)

<table>
  <thead>
    <tr>
      <th>$n$</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$\Delta_{8\times8}(p_{\beta},p_{\beta'})^{2}$</th>
      <td>0.16</td>
      <td>0.20</td>
      <td>0.33</td>
      <td>0.35</td>
      <td>0.11</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>$\Delta_{4\times4}(p_{\beta},p_{\beta'})^{2}$</th>
      <td>0.05</td>
      <td>0.07</td>
      <td>0.10</td>
      <td>0.07</td>
      <td>0.03</td>
      <td>0.01</td>
    </tr>
  </tbody>
</table>

The finite-size effect is, significantly, most pronounced for $n=4$. For $\beta=(0.01)n$ and $\beta'=(0.01)(n+1)$ in the range $n=1,2,\ldots,9$, with the use of the same algorithm with a cold start and 10000 random site selections, the results for a $4\times4$ lattice were

<table>
  <thead>
    <tr>
      <th>$n$</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$\Delta_{4\times4}^{2}(\text{MC})$</th>
      <td>0.00055</td>
      <td>0.00058</td>
      <td>0.00058</td>
      <td>0.00057</td>
      <td>0.00059</td>
      <td>0.00057</td>
      <td>0.00052</td>
      <td>0.00063</td>
      <td>0.00067</td>
    </tr>
    <tr>
      <th>$\Delta_{4\times4}^{2}(\text{exact})$</th>
      <td>0.00040</td>
      <td>0.00040</td>
      <td>0.00040</td>
      <td>0.00041</td>
      <td>0.00041</td>
      <td>0.00041</td>
      <td>0.00042</td>
      <td>0.00043</td>
      <td>0.00043</td>
    </tr>
  </tbody>
</table>

These figures show that, for high temperatures (or strong couplings), reasonably good accuracy can be consistently obtained even with moderate-sized samples.

Starting with a given Hamiltonian $S_0$ on a configuration space $\Sigma_{\Lambda_0}$ associated with an arbitrary lattice $\Lambda_0$, the application of an arbitrary decimation procedure yields a new lattice $\Lambda$ and a renormalized Hamiltonian $T$ on $\Sigma_{\Lambda}$. To compare the respective measures $dq$ and $dp$ on $\Sigma_{\Lambda}$ defined by $T$ and another given Hamiltonian $S$ (ordinarily of the same form as $S_0$), we can compute the quantity $\rho$ in formula (2) by using a MC procedure $M_u$ to generate configurations in accordance with the Boltzmann weight $e^{-u}$. Unfortunately, the explicit form of $T$ is generally unknown and at each step of the Markov chain $M_u$ the quantity $e^{-T}$ must be determined by simple random sampling (or possibly some more sophisticated but also more laborious technique for computing partition functions). The approximate value of $e^{-T}$ is determined at each step by fixing the current configuration $\sigma'$ of the decimated lattice $\Lambda$, randomly varying the sites (or links, etc.) of the residual lattice $\Lambda_0\setminus\Lambda$ in accordance with the basic Liouville measure $dr$, thus obtaining a sequence $\{\sigma_i\}\subset\Sigma_{\Lambda_0}$ such that $f(\sigma_i)=\sigma'$ (where $f$ denotes the decimation map), and calculation of the sum

$$
e_{N}^{-T}=\sum_{i=1}^{N}e^{-S(\sigma_i)}. \tag{3}
$$

A normalization factor is not required, since this would cancel in the product under the square root in formula (2), and since the Markov chain $M_u$ depends only upon the relative weights $e^{-u}\equiv e^{-(S+T)/2}$, which are unaffected by a multiplicative factor. The accuracy of the approximation improves with increasing $N$ and the sum eventually converges (modulo normalization) to the true value of $e^{-T}$. By definition (1) and the concavity of the square root function, $\Delta_N$ is clearly a monotonic decreasing function of $N$. Thus by using small values of $N$ one can obtain an upper bound on the distance $\Delta$ and thereby, when appropriate, establish that the parameter values under consideration are indeed close to the true values determined by the renormalization flow. Greatest efficiency will be obtained when $\Lambda_0\setminus\Lambda$ is small, since $\Sigma_{\Lambda_0\setminus\Lambda}$ will then be small, giving better accuracy for a given $N$ in (3), and $|S(\sigma)-T(\sigma)|$ will also be small, hence the convergence of the averages in (2) will be rapid.

For a one-dimensional periodic Ising chain with decimation factor 2, the relation between the original inverse temperature $\beta$ and the renormalized value $\beta'$ is $\beta'=(\ln\cosh2\beta)/2$. The program was applied to a periodic four-spin chain for the values $\beta=0.1$ and $\beta'=(\ln\cosh2\beta)/2\sim0.0099$, again with use of a heat-bath algorithm with a cold start. With use of $N=10$ in formula (3), the KD after 6000 random site selections was $\Delta(p_{\beta'},q_{\beta})^{2}=0.00076$, and continued to display a slow monotonic decrease. For the values $\beta_0=\beta_1=0.1$, which of course do not correspond under this decimation, the KD obtained under the same conditions after 8100 random site selections was $\Delta(p_{\beta_1},q_{\beta_0})^{2}=0.00469$, and

was then slowly fluctuating in that neighborhood. The exact formula for the KD is, in this case,
$$
\Delta\left(p_{\beta_{2}}, q_{\beta_{1}}\right)^{2}=1-\frac{e^{-\beta_{2}}+e^{\beta_{2}} \cosh 2 \beta_{1}}{\left\{\left[1+\left(\cosh 2 \beta_{1}\right)^{2}\right] 2 \cosh 2 \beta_{2}\right\}^{1 / 2}}.
$$

For $\beta_{2}=\beta_{1}^{i}=\left(\ln \cosh 2 \beta_{1}\right) / 2$, the above formula vanishes identically, as it should, and for $\beta_{2}=\beta_{1}=0.1$, we have $\Delta^{2}=0.00399$. Thus the two KD computed by MC simulation are quite close to the precise distances. However, in the present case the number $N=10$ is actually 2.5 times the number of configurations $2^{\left|\Lambda_{0} \backslash \Lambda\right|}$ (i.e., $2^{2}=4$) of the residual lattice, whereas in more realistic calculations $N$ might be only a very small fraction of $2^{\left|\Lambda_{0} \backslash \Lambda\right|}$; hence the resulting error could be considerably greater. Nevertheless, as was pointed out above, an upper bound to the distance can always be obtained.

Rather than performing separate computations for various given pairs of parameter values, the location of pairs corresponding under the renormalization map (and, in particular, fixed points) could be facilitated by devising a single program whereby the system follows a Markov chain in the parameter space simultaneously with the random walk in configuration space, i.e., the transition probabilities of the chain are continuously (or rather sequentially) varied by feedback from the current value of the KD in accordance with an appropriate optimal control technique. The author is now working on a trial program of this type for one-dimensional Ising chains.

The present method is analogous to that originally suggested by Wilson, $^{4}$ utilizing the comparison of correlation functions to locate fixed points. However, the complete specification of a probability distribution generally requires the knowledge of an infinite number of correlation functions. Even if these could all be effectively computed for the two distributions in question, their respective differences will vary, and there is no obvious method of combining them into a single criterion for proximity, but the KD provides such a criterion in the form of a single intuitively meaningful number. In principle, the present procedure could be iterated for an arbitrary number of steps and the $n$-fold renormalized Gibbs measures $e^{H_{n}}$ successively compared with the $e^{H_{n+1}}$. Only at the final stage, when the distance $\Delta\left(e^{H_{n}}, e^{H_{n+1}}\right)$ becomes and remains sufficiently small (an indication, by the Cauchy criterion, that the system is close to a fixed point) would it be necessary to calculate correlation functions, etc., in order to specify the approximate fixed-point Hamiltonian. One need not keep track of proliferating interactions, etc., during the intermediate calculations, and the same applies to order parameters such as Wilson loops, etc. For ordinary spin systems and gauge systems with compact groups, all the dynamical variables are bounded; hence convergence in the sense of the KD ensures convergence of all correlation functions, since, if $M=\sup _{\sigma}|f(\sigma)|$, a simple manipulation with use of the Schwarz inequality yields

$$
\left|\langle f(\sigma)\rangle_{p}-\langle f(\sigma)\rangle_{q}\right|^{2}=\left|\int f(\sigma)[d p(\sigma)-d q(\sigma)]\right|^{2} \leq M^{2}[2+2 \rho(p, q)][2-2 \rho(p, q)] \leq 8 M^{2} \Delta(p, q)^{2}.
$$

The various actions used in lattice-gauge theory, e.g., Wilson, Manton, heat kernel, etc., $^{5}$ all yield the same action in the formal continuum limit, but may possibly lead to different measures in the quantized theory. $^{6}$ It would be interesting to compare these actions by computing the distances between the corresponding measures induced on a sequence of finite lattices with appropriately adjusted coupling constants, and this could be done with use of the MC procedure described above.

By an obvious refinement, the KD can be computed for measures restricted to any subset of the configuration space which happens to be of particular interest, e.g., monopoles, vortices, etc., thus providing more delicate comparisons of topological behavior (for various temperatures or different basic Hamiltonians) than could be achieved by merely counting monopoles, etc. Also, the KD can be applied to the study of the renormalization flow induced by the decimation of random lattices $^{7,8}$; details will be presented in a subsequent paper.

Since there are an infinite number of possible metrics on any nontrivial space of probability distributions, the reader may well question the justification for choosing this particular one. Although simplicity and computability are important considerations, the main reason actually lies far deeper than this. The Taylor expansion of the KD between two probability distributions depending upon a finite-dimensional parameter $\beta=\left(\beta^{i}\right)$, with densities $p(\sigma, \beta)$ and $p(\sigma, \beta+\Delta \beta)$ relative to some underlying measure $d r(\sigma)$, is

$$
\begin{aligned}
\Delta^{2}\left(P_{\beta}, P_{\beta+\Delta \beta}\right) & =\int\left[p(\sigma, \beta+\Delta \beta)^{1 / 2}-p(\sigma, \beta)^{1 / 2}\right]^{2} d r(\sigma) \\
& =\frac{1}{4}\left(\int\left[\partial \ln p(\sigma, \beta) / \partial \beta^{i}\right]\left[\partial \ln p(\sigma, \beta) / \partial \beta^{j}\right] p(\sigma, \beta) d r(\sigma)\right)\left(\Delta \beta^{i}\right)\left(\Delta \beta^{j}\right)+\cdots ;
\end{aligned}
$$

hence the local metric tensor induced by the KD is just the Fisher information matrix, and the classical Cramer-Rao theorem $^{9}$ shows that this metric tensor plays a special role in the geometry of probability spaces. From this viewpoint, the intrinsic velocity of renormalization flow, in terms of the vector parameter $\beta^{i}$ and the scale factor $\lambda$, is not $|d \beta| / d \lambda=\left(d \beta^{i} d \beta^{i}\right)^{1 / 2} / d \lambda$, but rather $v=\left(g_{i j} d \beta^{i} d \beta^{j}\right)^{1 / 2} / d \lambda$. Thus, e.g., for a one-dimensional Ising chain with $N$ spins

(no external field) since $^{10}$

$$
d\beta/d\lambda = (\cosh\beta)(\sinh\beta)\ln\tanh\beta
$$

and $g_{11}(\beta)=(N-1)/\cosh^{2}\beta$, we have $v=(N-1)^{1/2}$ $\times(\sinh\beta)\ln\tanh\beta$, which $\to 0$ as $\beta\to\infty$, whereas $d\beta/d\lambda\to-\frac{1}{2}$. A theoretical discussion of information geometry in connection with classical thermodynamics and the foundations of quantum mechanics may be found in a paper of Ingarden. $^{11}$ As pointed out above, the MC computation of the global KD works best for short distances; hence it is not surprising that the MC computation of the local metric tensor and associated Riemann curvature is still easier, in fact, these quantities can be simply expressed in terms of correlation functions of order $\leq 6$. Results of such computations will be presented in a subsequent paper.

The author gratefully acknowledges the assistance of Professor A. Arima, Professor K. Yazaki, Professor M. Iri, Professor H. Miyazawa, and Dr. S. Miyashita.

$^{1}$D. X. Xia, *Measure and Integration Theory on Infinite- dimensional Spaces* (Academic, New York, 1971), and refer- ences cited therein.

$^{2}$E. J. Brody, Z. Wahrsche. Verw. Gebiete $\textbf{20}$, 217 (1971), and references cited therein.

$^{3}$A. E. Ferdinand and M. E. Fisher, Phys. Rev. $\textbf{185}$, 832 (1969).

$^{4}$R. H. Swendsen, in *Real Space Renormalization*, edited by T. W. Burkhardt and J. M. J. van Leeuwen (Springer, Berlin, 1982), and references cited therein.

$^{5}$M. Creutz, *Quarks, Gluons and Lattices* (Cambridge Univ., Cambridge, England, 1983), and references cited therein.

$^{6}$E. Seiler, *Gauge Field Theories as a Problem of Construc- tive Quantum Field Theory and Statistical Mechanics* (Springer, Berlin, 1982).

$^{7}$N. H. Christ, R. Friedberg, and T. D. Lee, Nucl. Phys. $\textbf{B202}$, 89 (1982), and $\textbf{B210 [FS 6]}$, 310, 337 (1982).

$^{8}$T. D. Lee, in *Shelter Island II*, edited by S. Weinberg and E. Witten (MIT Press, Cambridge, Mass., 1985).

$^{9}$S. Amari, *Differential-geometrical Methods in Statistics* (Springer, Berlin, 1985).

$^{10}$L. P. Kadanoff, Rev. Mod. Phys. $\textbf{49}$, 267 (1977).

$^{11}$R. S. Ingarden, Int. J. Eng. Sci. $\textbf{19}$, 1609 (1981).