PHYSICAL REVIEW B 69, 104103 (2004)

# Phase diagram and critical behavior of the spin-1 Baxter-Wu model with a crystal field

M. L. M. Costa, $^{1}$ J. C. Xavier, $^{2}$ and J. A. Plascak $^{1}$

$^{1}$ Departamento de Física, Instituto de Ciências Exatas, Universidade Federal de Minas Gerais, Caixa Postal 702, Belo Horizonte, Minas Gerais 30123-970, Brazil
$^{2}$ Instituto de Física Gleb Wataghin, Unicamp, Caixa Postal 6165, Campinas, São Paulo 13083-970, Brazil

(Received 13 November 2003; published 15 March 2004)

The phase diagram and critical behavior of the spin-1 Baxter-Wu model with a crystal field in two dimensions is explored by renormalization group, conventional finite-size scaling, and conformal invariance techniques. We found that the phase diagram of this model is qualitatively the same as that of the dilute 4-states Potts model, presenting a multicritical point for a finite value of the crystal field, in disagreement with previous work based on finite-size calculations. However, our results indicate that the critical exponents vary continuously along the second-order transition line, differently from the expected behavior of the dilute 4-states Potts model.

DOI: 10.1103/PhysRevB.69.104103
PACS number(s): 64.60.Kw, 64.60.Ak, 64.60.Cn, 75.10.Hk

## I. INTRODUCTION

The Ising model $^{1}$ was the first nontrivial model exactly solvable in two dimensions which exhibits spontaneous symmetry breaking. It became the most popular ferromagnetic model in statistical mechanics and even today is the object of several studies in other contexts such as random systems. $^{2}$ The dynamics of the Ising model is described by the Hamiltonian

$$
H_{I}=-J \sum_{\langle i, j\rangle} s_{i} s_{j}, \quad(1)
$$

where the sum is over all nearest neighbors and the classical spin variables $s_{i}=\pm 1$ are attached at each site $i$ of the lattice. In the mid 1960s, Blume and Capel $^{3}$ proposed an extension of the Hamiltonian (1) to study first-order magnetic phase transitions. Their Hamiltonian is given by

$$
H_{B C}=-J \sum_{\langle i, j\rangle} s_{i} s_{j}+\Delta \sum_{i} s_{i}^{2}, \quad(2)
$$

where $\Delta$ plays the role of a crystal field and in this case the variables $s_{i}$ are classical spin-1 variables taking the values $s_{i}=-1,0,1$.

It is well established that for dimensions $d \geqslant 2$ the BlumeCapel model [Eq. (2)] presents a phase diagram with ordered ferromagnetic and disordered paramagnetic phases separated by a transition line which changes from a second-order character (Ising type) to a first-order one at a tricritical point (see Ref. 4, and references therein). More specifically, in two dimensions, the machinery coming from conformal invariance $^{5,6}$ indicates that at this multicritical point the longrange fluctuations are governed by a conformal field theory with central charge $c=7 / 10.^{4,7,8}$ In this case, all the critical exponents and the whole operator content of the model were obtained $^{8}$ (see also Ref. 4). The generalization to higher spin $S$ of this model has also been studied. $^{4,9-12}$ In particular, results of mean-field theory, $^{11}$ conformal invariance, $^{4}$ and Monte Carlo simulations $^{12}$ predict different phase diagrams for integer or half-odd-integer spins, in contradiction with results based on real-space renormalization groups. $^{9,10}$ Recently, the universality at a double critical end point in the two-dimensional spin-3/2 Blume-Capel model has been analyzed and it was shown that it belongs indeed to the same universality class as the critical line. $^{13}$

Another simple model exactly solvable in two dimensions exhibiting spontaneous symmetry breaking is the Baxter-Wu model. $^{14-16}$ This model is defined on a triangular lattice by the three-spin interaction Hamiltonian

$$
H_{B W}=-J \sum_{\langle i j k\rangle} s_{i} s_{j} s_{k}, \quad(3)
$$

where the sum extends over all elementary triangles of the lattice and $s_{i}=\pm 1$ are Ising variables located at the sites. This model is self-dual $^{17}$ with the same critical temperature as that of the Ising model on a square lattice. The critical behavior of the Baxter-Wu model is governed by a conformal field theory with central charge $c=1,^{15,16}$ and its leading exponents $^{14-16} \alpha=2 / 3, \nu=2 / 3$, and $\eta=1 / 4$ are the same as those of the 4-states Potts model. $^{18}$

In analogy with the Blume-Capel model, in this paper we consider the Baxter-Wu model in the presence of a crystal field. The Hamiltonian of the spin-1 Baxter-Wu model with a crystal field is given by

$$
H=-J \sum_{\langle i j k\rangle} s_{i} s_{j} s_{k}+\Delta \sum_{i} s_{i}^{2}, \quad(4)
$$

where the classical spin variables $s_{i}$, defined in a triangular lattice, take the values $s_{i}=-1,0,1$. Note that when $\Delta \rightarrow-\infty$ only the configurations with $s_{i}=\pm 1$ are allowed, and we recover the pure Baxter-Wu model.

Since we have in the Baxter-Wu model with a crystal field the same kind of competition between the ordered $(\langle s\rangle \neq 0)$ and the disordered phases $(\langle s\rangle=0)$ (which is mediated by the crystal field) as in the Blume-Capel model, we may expect for both models a similar phase diagram, but with different critical behavior. This kind of competition also appears in the dilute $q$-states Potts model. $^{19}$ It is well known that the Baxter-Wu model and the 4-states Potts model have

0163-1829/2004/69(10)/104103(6)/\$22.50
69 104103-1
©2004 The American Physical Society

the same critical exponents (see, for example, Ref. 14). Since the dilution in the 4-states Potts model has the same effect as the crystal field in the Baxter-Wu model, we may expect the critical behavior of both models to be the same. Some previous calculations of the phase diagram of both models have been reported in the literature. Nienhuis et al.,¹⁹ based on a renormalization-group study, indicate that for the dilute 4-states Potts model the phase diagram is similar as that of the Blume-Capel model, i.e., there is a transition line which changes from a second-order character to a first-order one at a multicritical point. In this case, however, the critical behavior is governed by only one fixed point, giving along the second-order line the same exponents as that of the pure 4-states Potts model. On the other hand, Kinzel et al.,²⁰ using finite-size methods, conjectured a different kind of phase diagram for the Baxter-Wu model in the presence of a crystal field. These authors interpreted the changes of the estimated thermal exponents \(y_t\) along the transition line as a signal that a second-order transition should happen only for \(\Delta \to -\infty\) (the pure Baxter-Wu model).

A careful study of the pure Baxter-Wu model has also been done by exploring its Bethe-ansatz solution.¹⁴⁻¹⁶ Using the consequences of conformal invariance, it has been shown¹⁵,¹⁶ that in the absence of dilution (\(\Delta \to -\infty\)) not only the leading critical exponents of the Baxter-Wu model and the 4-states Potts model are identical, but the whole operator content of the models coincides as well. Moreover, the masses of the field theory describing the thermal and magnetic perturbations of both models are also identical.¹⁶ Since the reported effects of the dilution in both systems are different, we decided in this paper to study the effect of dilution (or crystal field) in the Baxter-Wu model in two dimensions using the machinery of conformal invariance and renormalization-group techniques.

This paper is organized as follows. In the following section we present the phase diagram obtained through the mean-field renormalization-group approach. In Sec. III we present the transfer matrix of the model, the relations used in our finite-size studies, as well as the results for the phase diagram. We then close the paper in Sec. IV with a summary and conclusion.

## II. MEAN-FIELD RENORMALIZATION GROUP

The mean-field renormalization group (MFRG)²¹,²² is a powerful phenomenological approach which can provide quite good results in the general study of critical phenomena.²³ It is based on the comparison of the order parameter for different finite lattices in the presence of symmetry-breaking boundary conditions. For a finite cluster of \(N\) spins, and considering the parameters of the Hamiltonian (4), one first computes the magnetization per spin \(m_N(K,D,b)\), where \(K=\beta J\), \(D=\beta \Delta\), and \(b\) is the boundary field, with \(\beta=1/k_B T\) and \(k_B\) the Boltzmann constant. As the boundary field is assumed to be very small one has
$$
m_N(K,D,b)=f_N(K,D)b. \tag{5}
$$

In its simplest version, the MFRG considers two different clusters of \(N'<N\) spins and assumes that the magnetizations scale as
$$
m_{N'}(K',D',b')=\ell^{d-y_H}m_N(K,D,b), \tag{6}
$$
where \(\ell=(N/N')^{1/d}\) is the scaling factor, \(d\) is the dimension of the lattice, and \(y_H\) the magnetic exponent. With the same relation for the boundary fields, namely,
$$
b'=\ell^{d-y_H}b, \tag{7}
$$
and taking into account expansion (5) one has
$$
f_N(K,D)=f_{N'}(K',D'), \tag{8}
$$
which is independent of any scaling factor and is viewed as a renormalization recursion relation from which one gets fixed-point solutions \(K'=K=K_c\) and estimates of correlation length critical exponents \(\nu\) in the subset \(D'=D\).

Another version of the approach considers three different clusters of \(N''\), \(N'\), and \(N\) spins (in increasing order) together with the scaling (6) in such a way that one gets
$$
f_{N'}(K',D')b'=\ell_1^{d-y_H}f_N(K,D)b, \tag{9}
$$
$$
f_{N''}(K'',D'')b''=\ell_2^{d-y_H}f_{N'}(K',D')b', \tag{10}
$$
where the scaling factors are \(\ell_1=(N/N')^{1/d}\) and \(\ell_2=(N'/N'')^{1/d}\). Imposing now that the boundary fields scale not as bulk magnetizations above, but as the surface field we obtain
$$
b'=\ell_1^{y_{hs}}b, \quad b''=\ell_2^{y_{hs}}b', \tag{11}
$$
where \(y_{hs}\) is the surface critical exponent. Equations (9)–(11) are now the renormalization recursion relation between the interaction parameters of the system. The exponent \(d - y_H - y_{hs}\) is then determined self-consistently by imposing further that Eqs. (9) and (10) possess the same fixed point \(K''=K'=K=K_c\) for an invariant subset \(D''=D'=D\) (for further details and a comparison between these two approaches see Refs. 22 and 23). This version of the method is referred as surface bulk MFRG (SBMFRG).

Before applying the MFRG to the spin-1 Hamiltonian, defined by Eq. (4), it is worthwhile to measure the efficiency of the method by first treating the pure spin-1/2 Baxter-Wu model [Eq. (3)], where exact results are available. Since the model exhibits three different ferrimagnetic phases at low temperatures,²⁴ it is supposed, at first sight, that the size of the finite blocks must be such that they will suitably accommodate them in an equivalent way throughout the lattice. These would dramatically restrict the size of the clusters. However, we note that by computing the sublattice magnetizations \(m_A\), \(m_B\), and \(m_C\), by taking three different boundary fields \(b_A\), \(b_B\), and \(b_C\), we obtain the same equations as by considering a homogeneous cluster where \(m_A=m_B=m_C\) and \(b_A=b_B=b_C\). This is not surprising, bearing in mind that the ferromagnetic phase is also coexisting with the other three ferrimagnetic ones at low temperatures. This means that for practical purposes, we can consider only the ferromagnetic arrangement, allowing us to take blocks of any number of

<table><caption>Table I. Results for the pure spin-1/2 Baxter-Wu model according to the MFRG and SBMFRG approaches.</caption>
<tbody><tr><th>$N'-N$</th><th>$k_BT_c/J$</th><th>$\nu$</th></tr>
<tr><td colspan="3">MFRG</td></tr>
<tr><td>6-10</td><td>3.4883</td><td>2.7820</td></tr>
<tr><td>10-15</td><td>2.7349</td><td>1.8987</td></tr>
<tr><td>15-21</td><td>2.5421</td><td>1.5588</td></tr>
<tr><td>21-28</td><td>2.4345</td><td>1.3718</td></tr>
<tr><td>Extrapolated</td><td>2.294(8)</td><td>0.70(6)</td></tr>
<tr><td>exact</td><td>2.2692</td><td>2/3</td></tr>
<tr><td colspan="3">SBMFRG</td></tr>
<tr><td>6-10-15</td><td>1.7200</td><td>1.0688</td></tr>
<tr><td>10-15-21</td><td>2.0794</td><td>1.0806</td></tr>
<tr><td>15-21-28</td><td>2.0907</td><td>0.9957</td></tr>
</tbody></table>

spins. This leads to a huge simplification in the numerical acquisition of the functions $f_N(K)$. For this particular system, the best clusters are those which preserve the symmetry of the original lattice. They are made of symmetric triangles of $N\!=\!6,10,15,21,28$ spins. Although for $N\!=\!6$ we can obtain analytical expressions for $m_6(K,b)$ and $f_6(K)$, for $N\!\geqslant\!10$ all the quantities have to be computed numerically. In Table I, we present the critical temperature and critical exponent obtained according to the usual MFRG and also from the SB-MFRG. It is also possible through the MFRG get an extrapolation. $^{23}$ Note that, for the present case, the extrapolated value is not so close to the exact result. This is, in fact, expected since the MFRG does not reproduce the exact value as the size of the lattices go to infinity. $^{22}$ Although the SBMFRG does, $^{22}$ the present clusters are still too small for us to get a reasonable extrapolation. However, as can be seen from Table I, the temperatures are getting closer to the exact value as the size of the clusters increase. Note that, while the MFRG approaches the expected result from above, the SBMFRG does it from below. A common feature of the present renormalization group is still a worse estimate of the critical exponent when compared to the critical temperature. Nevertheless, in general, a reasonable picture of the criticality of the system is achieved from the approach.

We now proceed to the study of the spin-1 model with crystal-field anisotropy. The same symmetry arguments also apply for this model. However, due to computer time, we were here limited to block sizes $N\!=\!6,10,15$. The phase diagram in the $\delta\!=\!\Delta/J$ versus $k_BT/J$ plane is depicted in Fig. 1 according to both procedures, as well as from the finite-size scaling (FSS) procedure of the following section, and the usual mean-field (MF) approximation. The latter approach is obtained by assuming $m_N\!=\!b$ in Eq. (5), resulting in $f_N\!=\!1$. Except for the FSS, all the lines terminate at some point which is identified as the multicritical point. The first-order transition lines are not possible to be obtained neither from the MFRG nor from the SBMFRG. Comparing with the FSS result, discussed in the following section, we can see that the MFRG overestimates the critical temperature while the surface bulk version underestimates it. This is just what happens in the pure case, as shown in Table I, when compared to the exact critical value. The estimate of the multicritical point is given in Table II. The SBMFRG and MFRG give critical exponents that vary along the second-order critical line. However, this fact, may be just an artifact of these approaches, since there is only one renormalization recursion relation. $^{23}$ In the following section, we analyze in the context of conformal invariance the possibility of the critical exponents vary along the second-order line.

![](./images/812363073149992960_1.jpg)

FIG. 1. (Color online) Phase diagram in the $\delta$ vs $kT/J$ plane for the spin-1 Baxter-Wu model in the presence of a crystal field. Continuum lines are second-order phase transitions and the dashed line is a first-order transition (see the following section). The dot represents the multicritical point. The results are according to the MFRG with two clusters, SBMFRG with three clusters, FSS (see the following section) and MF approximation with one cluster. The sizes of the clusters used are also presented.

### III. FINITE-SIZE SCALING AND CONFORMAL INVARIANCE

The row-to-row transfer matrix $\hat{T}$ of the Hamiltonian (4) in a triangular lattice, with horizontal width $N$, has dimension $3^N{\times}3^N$. Its coefficients $\langle s_1',\dots,s_N'|\hat{T}|s_1,\dots,s_N\rangle$ are the Boltzmann weights generated by the spin configurations $\{s_1,\dots,s_N\}$ and $\{s_1',\dots,s_N'\}$ of adjacent rows. If we con-

<table><caption>Table II. Position of the multicritical point for the curves shown in Fig. 1.</caption>
<tbody><tr><th>$N'-N$</th><th>$k_BT_t/J$</th><th>$\delta_t$</th></tr>
<tr><td colspan="3">MFRG</td></tr>
<tr><td>6-10</td><td>1.1816</td><td>2.1523</td></tr>
<tr><td>10-15</td><td>0.9330</td><td>1.8462</td></tr>
<tr><td colspan="3">SBMFRG</td></tr>
<tr><td>6-10-15</td><td>0.6408</td><td>1.5835</td></tr>
<tr><td colspan="3">MF</td></tr>
<tr><td>6</td><td>0.3133</td><td>0.8141</td></tr>
<tr><td>10</td><td>0.3539</td><td>1.0328</td></tr>
<tr><td>15</td><td>0.4513</td><td>1.1902</td></tr>
<tr><td colspan="3">FSS</td></tr>
<tr><td>3-6-9</td><td>1.2225</td><td>1.3089</td></tr>
</tbody></table>

sider periodic boundary condition in the horizontal direction,
the transfer matrix can be written as
$$
\begin{aligned}
& \left\langle s_{1}, \ldots, s_{N}|\hat{T}| s_{1}^{\prime}, \ldots, s_{N}^{\prime}\right\rangle \\
& \quad=\prod_{j=1}^{N} \exp \left[t^{-1} s_{i+1} s_{i}^{\prime}\left(s_{i}+s_{i+1}^{\prime}\right)-\delta t^{-1} s_{i}^{2}\right],
\end{aligned}\qquad(12)
$$
with $t=k_{B} T / J$ ($k_{B}$ is the Boltzmann constant) and $\delta=D / J$.

The finite-size behavior of the eigenvalues of $\hat{T}$ (Λ₀(N)
>Λ₁(N),...) can be used to determine the critical line and
the critical exponents. $^{5,6,25}$ The critical line $[t_{c}(\delta)]$ is evalu
ated by extrapolating to the bulk limit $(N \to \infty)$ the sequences
$t_{c}(\delta, N)$ obtained by solving
$$G_{N}\left(t_{c}\right) N=G_{N+3}\left(t_{c}\right)(N+3), \quad N=3,6, \ldots, \quad(13)$$
where $G_{N}(t_{c})$ is the mass gap of $H=-\ln \hat{T}$ and is given by
$$G_{N}\left(t_{c}\right)=\ln \left(\frac{\Lambda_{0}(N)}{\Lambda_{1}(N)}\right).$$

The multicritical points are obtained using a heuristic
method, which has already been proved to be effective. $^{4,26}$ In
this case we have to solve simultaneously Eq. (13) for three
different lattice sizes
$$\begin{aligned}
G_{N}\left(t_{c}\right) N= & G_{N+3}\left(t_{c}\right)(N+3)=G_{N+6}\left(t_{c}\right)(N+6), \\
& N=3,6, \ldots.
\end{aligned}\qquad(14)$$

In Eqs. (13) and (14) we restricted the possible finite strip
widths to multiples of 3 in order to preserve the invariance of
the Hamiltonian (4) under the reversal of all spins on any
two sublattices.

As usual, we expect the model to be conformally invariant
in the region of continuous phase transition. This invariance
allows us to infer the critical properties from the finite-size
corrections of the eigenspectrum at $t_{c}.^{5,6}$ The conformal
anomaly $c$ , which labels the universality class of critical be
havior, can be calculated from the large- $N$ behavior of the
ground-state energy of $H=-\ln \hat{T}^{6}$ 
$$\frac{\ln \Lambda_{0}(N)}{N}=\epsilon_{\infty}+\frac{\pi c v_{s}}{6 N^{2}}+o\left(N^{-2}\right),\qquad(15)$$
where $\epsilon_{\infty}$ is the ground-state energy per site in the bulk limit
and $v_{s}=\sqrt{3} / 2$ is the sound velocity. The scaling dimensions
of operators governing the critical fluctuations (related to the
critical exponents) are evaluated from the finite- $N$ correc
tions of the excited states. For each primary operator, with
dimension $x_{\phi}$ , in the operator algebra of the system, there
exists an infinite tower of eigenstates of $H=-\ln \hat{T}$ whose
energy $\ln (\Lambda_{m, m'}^{\phi})$ and momentum $P_{m, m'}^{\phi}$ are given by $^{5}$ 
$$\frac{\ln \Lambda_{m, m^{\prime}}^{\phi}(N)}{N}=\frac{\ln \Lambda_{0}(N)}{N}-\frac{2 \pi v_{s}}{N^{2}}\left(x_{\phi}+m+m^{\prime}\right),$$

$$P_{m, m^{\prime}}^{\phi}=\frac{2 \pi}{N}\left(s_{\phi}+m-m^{\prime}\right),\qquad(16)$$
where $m, m'=0,1,...$ .

A finite-size estimate for the first-order transition line can
be obtained by the same procedure done as in a recent work. $^{4}$ 
At the first-order line of the Baxter-Wu model with a crystal
field, we have the coexistence of five phases, one ordered
ferromagnetically, three ordered ferrimagnetically, and a dis-
ordered one. Consequently, for a given lattice size $N$ we cal
culate the points where the gap corresponding to the fifth
eigenvalue has a minimum. The extrapolation $N \to \infty$ of these
points give us an estimate for the first-order transition line.

In the numerical diagonalization of Eq. (12) we used the
Lanczos method for non-Hermitian matrices. $^{27}$ We also con
sidered the translational symmetry to block diagonalize the
transfer matrix.

In Fig. 1 we show the second-order transition line (con
tinuum line), obtained by solving Eq. (13) for lattice sizes
$N=6$ . As we can see in this figure the second-order transi
tion line also occur for finite values of the crystal field
$(\delta \neq-\infty)$ , differently of the previous results of Kinzel
et al., $^{20}$ where it was conjectured the appearance of the
second-order transition only at $\delta \to -\infty$ . For the pure
Baxter-Wu model $(\delta \to -\infty)$ we obtained $t_{c}^{-1}=0.4408842$ 
for $N=6$ in Eq. (13), which differs only $0.04 \%$ of the exact
value $t_{c}^{-1}=\ln (\sqrt{2}+1) / 2=0.440686...$ . For this reason, it
is a very good approximation to consider $t_{c}(\delta)=t_{c}^{6,9}(\delta)$ .

For the sake of clarity, we present in Table III the finite-
size sequences obtained by solving Eq. (13) for lattice sizes
$N=3$ and $N=6$ . As we can see from this table the conver
gence of $t_{c}$ are better for $\delta>0$ , so we expect that the esti
mates of $t_{c}^{(6,9)}(\delta)$ are better than the corresponding ones in
the region $\delta<0$ . The fast convergence with $N$ indicates that
the corrections to finite size are probably given by a power
law, such as in the pure Baxter-Wu model. In this last case
the corrections are controlled by an operator with dimension
$w=4.^{15}$ 

We have also solved Eq. (14) for $N=3$ , which gives us an
estimate for the multicritical point. In this case we do not
have points to extrapolate, but we believe the estimate of the
multicritical point, the last point in the continuum line in Fig.
1, is not far from the extrapolated one. Our estimate for this
point is $t_{t}=1.2225$ and $\delta_{t}=1.3089$ .

We determined the first-order line minimizing the gap re-
lated with the fifth eigenvalue, as discussed before. The
dashed line shown in Fig. 1 was obtained in this procedure
considering $N=9$ . As we can see in this figure, the first-order
transition line finishes at the multicritical point.

TABLE III. Finite-size data $t_{c}^{N, N+3}$ given by Eq. (13) for the
critical temperature $t_{c}$ for some values of $\delta$ .

<table>
<thead>
  <tr>
    <th>N</th>
    <th>−10</th>
    <th>−1</th>
    <th>1</th>
    <th>1.25</th>
    <th>1.3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>3</td>
    <td>2.246 498</td>
    <td>1.843 818</td>
    <td>1.358 399</td>
    <td>1.251 121</td>
    <td>1.226 940</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2.256 769</td>
    <td>1.849 705</td>
    <td>1.360 144</td>
    <td>1.251 529</td>
    <td>1.227 005</td>
  </tr>
</tbody>
</table>

<table>
<caption>Table IV. Finite-size estimates $c^{N,N+3}$, given by Eq. (17), for the conformal anomaly is shown for some values of $\delta$. The extrapolated results obtained by Eq. (18) are also shown.</caption>
<tbody><tr>
<th>$N$</th>
<td>$-10$</td>
<td>$-1$</td>
<td>$1$</td>
<td>$1.25$</td>
<td>$1.3089$</td>
</tr>
<tr>
<th>$3$</th>
<td>$0.938\ 546$</td>
<td>$0.941\ 169$</td>
<td>$0.954\ 322$</td>
<td>$0.955\ 674$</td>
<td>$0.955\ 047$</td>
</tr>
<tr>
<th>$6$</th>
<td>$0.986\ 393$</td>
<td>$0.986\ 829$</td>
<td>$0.986\ 656$</td>
<td>$0.979\ 694$</td>
<td>$0.975\ 435$</td>
</tr>
<tr>
<th>$\infty$</th>
<td>$1.006$</td>
<td>$1.005$</td>
<td>$0.999$</td>
<td>$0.989$</td>
<td>$0.984$</td>
</tr>
</tbody></table>

In the critical regions of the phase-transition line (continuum curve) the conformal anomaly and the scaling dimensions can be calculated exploring the conformal invariance relations (15) and (16). From Eq. (15) a possible way to extract $c$ is by extrapolating the sequence

$$
\begin{aligned}
c^{N, N+3}= & \frac{12}{\sqrt{3} \pi}\left(\frac{\ln \Lambda_{1,0}(N+3)}{N+3}-\frac{\ln \Lambda_{1,0}(N)}{N}\right) \\
& \times\left(\frac{1}{(N+3)^{2}}-\frac{1}{N^{2}}\right)^{-1},
\end{aligned}
$$

calculated at $t_{c}(\delta)$. In Eq. (17) $\Lambda_{n, p}(N)$ means the $n$th eigenvalue of Eq. (12) with size $N$ in the sector with momentum $p$. Examples of such sequences for the Baxter-Wu model with a crystal field are shown in Table IV. The extrapolated values of $c^{\infty}$ can be obtained from the $N$-large behavior of $c^{N, N+3}(\delta)$, given by

$$
\begin{aligned}
c^{N, N+3}(\delta)= & c^{\infty}-a\left[N^{-w}+(N+3)^{-w}\right] \\
& \times\left[N^{-2}+(N+3)^{-2}\right]^{-1},
\end{aligned}
$$

where $a$ is a constant and $w$ the dominant dimension associated with the operator governing the finite-size corrections. We determine $c^{\infty}$ assuming Eq. (18) exact for $N=3$ and $N$ $=6$ with $w$ given by the pure Baxter-Wu model, i.e., $w=4.^{15}$ We see from Table IV that the conformal anomaly is $c=1$ along the critical line, and apparently even at the multicritical point. This scenario is quite different from that of the Blume-Capel model, where the conformal anomaly changes abruptly from $c=1 / 2$ at the critical line to $c=7 / 10$ at the tricritical point (see Ref. 5), but it is qualitatively similar as that of the dilute 4-states Potts model, $^{19}$ where along the critical line the critical exponents as well as the conformal anomaly do not change. Since we do not have a precise estimate for the multicritical point, we have also calculated $c^{N, N+3}$ for several values of $t_{c}(\delta)$ between $1.2<t_{c}(\delta)$ $<1.4$. We have not seen any abrupt change of the conformal anomaly, such as in the Blume-Capel model. $^{4}$

From Eq. (16) the scaling dimensions $x(n, p)$ related to the $n$th $(n=1,2, \ldots)$ energy in the sector with momentum $p$ can be obtained by extrapolating the sequence

$$
x^{N}(n, p)=\frac{N}{\pi \sqrt{3}} \ln \left(\frac{\Lambda_{1,0}(N)}{\Lambda_{n, p}(N)}\right).
$$

In Table V we show the dimensions $x^{N}(1,0)$ and $x^{N}(2,0)$ for the Baxter-Wu model with a crystal field. Note that $x^{9}(1,0)$

<table>
<caption>Table V. Finite-size scaling dimensions $x^{N}(1,0)$ and $x^{N}(2,0)$ given by Eq. (19) for some values of $\delta$.</caption>
<tbody><tr>
<th> </th>
<th> </th>
<td>$N=9$</td>
<td>$N=6$</td>
<td>$N=3$</td>
</tr>
<tr>
<th rowspan="5">$x^{N}(1,0)$</th>
<th>$\delta=-10$</th>
<td>$0.1236$</td>
<td>$0.1236$</td>
<td>$0.1195$</td>
</tr>
<tr>
<th>$\delta=-1$</th>
<td>$0.1223$</td>
<td>$0.1223$</td>
<td>$0.1184$</td>
</tr>
<tr>
<th>$\delta=1$</th>
<td>$0.1113$</td>
<td>$0.1113$</td>
<td>$0.1093$</td>
</tr>
<tr>
<th>$\delta=1.25$</th>
<td>$0.1048$</td>
<td>$0.1048$</td>
<td>$0.1043$</td>
</tr>
<tr>
<th>$\delta=1.3089$</th>
<td>$0.1026$</td>
<td>$0.1026$</td>
<td>$0.1026$</td>
</tr>
<tr>
<th rowspan="5">$x^{N}(2,0)$</th>
<th>$\delta=-10$</th>
<td>$0.5059$</td>
<td>$0.5147$</td>
<td>$0.6057$</td>
</tr>
<tr>
<th>$\delta=-1$</th>
<td>$0.4897$</td>
<td>$0.4976$</td>
<td>$0.5756$</td>
</tr>
<tr>
<th>$\delta=1$</th>
<td>$0.3644$</td>
<td>$0.3762$</td>
<td>$0.4163$</td>
</tr>
<tr>
<th>$\delta=1.25$</th>
<td>$0.3023$</td>
<td>$0.3207$</td>
<td>$0.3613$</td>
</tr>
<tr>
<th>$\delta=1.3089$</th>
<td>$0.2829$</td>
<td>$0.3037$</td>
<td>$0.3456$</td>
</tr>
</tbody></table>

$=x^{6}(1,0)$ due to Eq. (13) and the fact that we choose $t_{c}(\delta)$ $=t_{c}^{6,9}(\delta)$. At the tricritical point the three entries $x^{N}(1,0)$ are also the same due to Eq. (14). For $\delta \to -\infty$ (the pure Baxter-Wu model) the scaling dimensions $x^{9}(1,0)$ and $x^{9}(2,0)$ differ only $1\%$ from the leading dimensions $x^{9}(1,0)=\frac{1}{8}$ and $x^{9}(2,0)=\frac{1}{2}$ of the pure Baxter-Wu model. As the estimate of the critical line is better in the region $\delta>0$ and the eigenvalues converge faster with the size of the lattice in this region, we believe that our estimates for the scaling dimensions are better in the region $\delta>0$ than the corresponding ones for $\delta<0$, i.e., the estimates $x^{9}(1,0)$ and $x^{9}(2,0)$ must differ by less than $1\%$ from the extrapolated values for $\delta>0$. Note that when we increase the crystal field $\delta$ these values change continuously up to $x^{9}(1,0)\sim 0.10$ and $x^{9}(2,0)\sim 0.28$ at the multicritical point. This scenario is quite different from that of the Blume-Capel model, which is not a surprise since both models are in different universality classes of critical behavior. However it is also distinct from the scenario of the dilute 4-states Potts model, where the scaling dimensions along the critical line are believed to be the same as that of the pure 4-states Potts model. If the dilution had the same role in both models, we should expect for the dilute 4-states Potts a continuous line of fixed point, however this was not found. $^{19}$

## IV. SUMMARY AND CONCLUSION

In this paper we have calculated the phase diagram and critical properties of the spin-1 Baxter-Wu model in the presence of a crystal field. Our results, based on renormalization group, finite-size scaling, and conformal invariance, show a second-order transition line separated from a first-order transition line by a multicritical point. This scenario is in disagreement with that of a previous paper by Kinzel $et$ $al.,^{20}$ where the second-order transition line appears only in the limiting case $\Delta \to -\infty$. The critical behavior was determined by renormalization group and conformal invariance. Despite the phenomenological renormalization group be not so conclusive regarding the critical exponents, the conformal invariance results indicate that along the critical line, and even at the multicritical point, the conformal anomaly is the same as that of the Baxter-Wu model or the 4-states Potts model,

i.e., $c=1$, in agreement with the scenario expected for the dilute 4-states Potts model. However, our results indicate that the scaling dimensions vary continuously with the crystal field. This is an unexpected behavior since the reported results for the dilute 4-states Potts model indicate a constancy of the scaling dimensions along the phase-transition line, $^{19}$ and it is expected that both models belong to the same universality class of critical behavior. This result implies that either contrary to what occurs with thermal and magnetic perturbations the effect of dilution is distinct in the Baxter-Wu and in the 4-states Potts models, or the scenario based in renormalization group for the dilute 4-states Potts model is wrong. It would be interesting to verify our results using different numerical techniques, such as Monte Carlo methods. In fact, a Monte Carlo simulation for the case $\delta$ =0 has already been done and different exponents as those of the pure Baxter-Wu model have been achieved. $^{28}$ Extensive Monte Carlo simulations for $\delta \neq 0$ are in progress and will be present elsewhere.

## ACKNOWLEDGMENTS

J.C.X. would like to acknowledge profitable discussions with M. J. Martins and J. R. G. de Mendonça. He is also indebted to F. C. Alcaraz for suggestions and discussions in part of this work. This work was supported by FAPESP (Grants Nos. 00/02802-7 and 01/00719-8) (J.C.X.), FAPEMIG (M.L.M.C. and J.A.P.), CNPq (M.L.M.C. and J.A.P.), and CAPES (J.A.P.).

---

$^{1}$L. Onsager, Phys. Rev. $\textbf{65}$, 117 (1944).

$^{2}$M.P. Nightingale, in *Finite Size Scaling and Numerical Simulations in Statistical Systems*, edited by V. Privman (World Scientific, Singapore, 1990).

$^{3}$M. Blume, Phys. Rev. $\textbf{141}$, 517 (1966); H.W. Capel, Physica $\textbf{32}$, 966 (1966).

$^{4}$J.C. Xavier, F.C. Alcaraz, D.P. Lara, and J.A. Plascak, Phys. Rev. B $\textbf{57}$, 11 575 (1998).

$^{5}$J.L. Cardy, *Phase Transitions and Critical Phenomena*, edited by C. Domb and J.L. Lebowitz (Academic, New York, 1987), Vol. 11.

$^{6}$H.W.J. Blöte, J.L. Cardy, and M.P. Nightingale, Phys. Rev. Lett. $\textbf{56}$, 742 (1986); I. Affleck, ibid. $\textbf{56}$, 746 (1986).

$^{7}$F.C. Alcaraz, J.R.D. de Felício, R. Köberle, and J.F. Stilck, Phys. Rev. B $\textbf{32}$, 7469 (1985).

$^{8}$D.B. Balbão and J.R. Drugowich de Felício, J. Phys. A $\textbf{20}$, L207 (1987); G.v. Gehlen, ibid. $\textbf{24}$, 5371 (1990).

$^{9}$S.M. de Oliveira, P.M.C. de Oliveira, and F.C. de Sá Barreto, J. Stat. Phys. $\textbf{78}$, 1619 (1995).

$^{10}$A. Bakchich, A. Bassir, and A. Benyoussef, Physica A $\textbf{195}$, 188 (1993).

$^{11}$J.A. Plascak, J.G. Moreira, and F.C. Sá Barreto, Phys. Lett. A $\textbf{173}$, 360 (1993).

$^{12}$J.A. Plascak and D.P. Landau, *Computer Simulation Studies in Condensed Matter Physics XIII*, edited by D.P. Landau, S.P. Lewis, and H.-B. Shuttler (Springer, Berlin, 2000).

$^{13}$J.A. Plascak and D.P. Landau, Phys. Rev. E $\textbf{67}$, 015103(R) (2003).

$^{14}$R.J. Baxter and F.Y. Wu, Phys. Rev. Lett. $\textbf{31}$, 1294 (1973); and Aust. J. Phys. $\textbf{27}$, 357 (1974); R.J. Baxter, ibid. $\textbf{27}$, 369 (1974).

$^{15}$F.C. Alcaraz and J.C. Xavier, J. Phys. A $\textbf{30}$, L203 (1997).

$^{16}$F.C. Alcaraz and J.C. Xavier, J. Phys. A $\textbf{32}$, 2041 (1999).

$^{17}$D. Merlini and C. Gruber, J. Math. Phys. $\textbf{13}$, 1814 (1972); D.W. Wood and H.P. Griffiths, J. Phys. C $\textbf{5}$, L253 (1972).

$^{18}$E. Domany and E.K. Riedel, J. Appl. Phys. $\textbf{49}$, 1315 (1978); F.Y. Wu, Rev. Mod. Phys. $\textbf{54}$, 235 (1982); R.J. Baxter, *Exactly Solved Models in Statistical Mechanics* (Academic, New York, 1982).

$^{19}$B. Nienhuis, A.N. Berker, E.K. Riedel, and M. Schick, Phys. Rev. Lett. $\textbf{43}$, 737 (1979).

$^{20}$W. Kinzel, E. Domany, and A. Aharony, J. Phys. A $\textbf{14}$, L417 (1981).

$^{21}$J.O. Indekeu, A. Maritan, and A.L. Stella, J. Phys. A $\textbf{15}$, L291 (1982).

$^{22}$J.O. Indekeu, A. Maritan, and A.L. Stella, Phys. Rev. B $\textbf{35}$, 305 (1987).

$^{23}$J.A. Plascak, W. Figueiredo, and B.C.S. Grandi, Braz. J. Phys. $\textbf{29}$, 3 (1999).

$^{24}$Let $m_A$ , $m_B$ , and $m_C$ be the density of magnetization of the three sublattices. The three ferrimagnetic phases correspond to a phase where the magnetization $m=(m_A,m_B,m_C)$ has the following values: (i) $m=(+1,-1,-1)$, (ii) $m=(-1,+1,-1)$, and (iii) $m=(-1,-1,+1)$. There is also a ferromagnetic phase at low temperature given by $m=(1,1,1)$.

$^{25}$M.N. Barber, *Phase Transitions and Critical Phenomena*, edited by C. Domb and J.L. Lebowitz (Academic, New York, 1983), Vol. 8.

$^{26}$M.E. Fisher and N. Berker, Phys. Rev. $\textbf{26}$, 2707 (1982); P.A. Rikvold, W. Kinzel, J.D. Gunton, and K. Kaski, Phys. Rev. B $\textbf{28}$, 2686 (1983); H.J. Hermann, Phys. Lett. $\textbf{100A}$, 156 (1984); A.L. Malvezzi, Braz. J. Phys. $\textbf{24}$, 508 (1994).

$^{27}$G.H. Golub and C.F. van Loan, *Matrix Computations*, 3rd ed. (The Johns Hopkins University Press, Baltimore, 1996).

$^{28}$M.L.M. Costa and J.A. Plascak, Brazil. J. Phys. (to be published).