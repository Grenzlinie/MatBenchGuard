# Process of irreversible nucleation in multilayer growth. II. Exact results in one and two dimensions
Paolo Politi$^{1,*}$ and Claudio Castellano$^{2,\dagger}$

$^{1}$Istituto Nazionale per la Fisica della Materia, Unità di Firenze, Via G. Sansone 1, 50019 Sesto Fiorentino, Italy
$^{2}$Istituto Nazionale per la Fisica della Materia, Unità di Roma I, and Dipartimento di Fisica, Università di Roma "La Sapienza," Piazzale Aldo Moro 2, 00185 Roma, Italy

(Received 29 October 2001; published 27 September 2002)

We study irreversible dimer nucleation on top of terraces during epitaxial growth in one and two dimensions, for all values of the step-edge barrier. The problem is solved exactly by transforming it into a first passage problem for a random walker in a higher-dimensional space. The spatial distribution of nucleation events is shown to differ markedly from the mean-field estimate except in the limit of very weak step-edge barriers. The nucleation rate is computed exactly, including numerical prefactors.

DOI: 10.1103/PhysRevE.66.031606
PACS number(s): 64.60.Qb, 68.55.Ac, 68.35.Fx, 05.40.Fb

## I. INTRODUCTION
The understanding of how atomistic processes influence morphology at large scales is of fundamental importance for controlled growth of crystalline films via deposition techniques. The irreversible nucleation of immobile dimers, giving rise to new terraces, is a key process for the growth of a high symmetry surface. In the preceding paper [1] we have shown that for the nucleation on top of existing terraces, the usual mean-field (MF) theory [2,3] is equivalent to considering particles as noninteracting: i.e., not feeling each other even if they are on the same lattice site, so that they can meet several times before leaving the terrace. Mean-field theory (MFT) counts all these fictitious nucleation events and therefore leads to an overestimate of the nucleation rate $\omega$, which in most cases is a very poor approximation of the correct results. For the spatial distribution of nucleation events we have shown in Ref. [1] that a substantial discrepancy between the mean-field and exact results is expected, because fictitious nucleations beyond the first one always dominate in $d=1$ and $d=2$.

In this paper we go beyond mean-field theory and present a series of exact results. We calculate the spatial $[P(n)]$ and temporal $[Q(t)]$ distributions of nucleation events. The quantity $Q(t)$ is the probability that two atoms meet a time $t$ after deposition of the second atom and it is formally defined in Eq. (3). The evaluation of $P$ and $Q$ allows the determination of the total probability $W$ that two atoms meet and this allows the exact computation of the nucleation rate $\omega$.

The solution of the problem is obtained by mapping the diffusion of two particles on a $d$-dimensional terrace into the motion of a single random walker in $d'=2d$ dimensions. The statistics of meeting events between the two adatoms (nucleations) is then obtained as the solution of a suitable first passage problem for the $d'$-dimensional random walker. In $d=1$ the problem can be treated analytically in full detail, leading to closed form expressions for all quantities of interest. In $d=2$ one can easily obtain the results numerically, with arbitrary accuracy.

Results indicate that the spatial distribution of nucleation sites is very different from the mean-field estimate in the limit of strong Ehrlich-Schwoebel barriers, both in $d=1$ and $d=2$. In the opposite limit of zero or weak barriers instead, the difference between the mean-field estimate and the exact result is, for reasonable terrace sizes, quite surprisingly small. The temporal distribution of nucleation events decays slowly for short times and later exponentially. Finally, the calculation of the nucleation rate $\omega$ is completed by the rigorous determination of the nucleation probability $W=\sum_n P(n)$. This confirms that MFT is safely applicable only for weak barriers in $d=2$ and gives the exact expressions for $\omega$ that must be used instead of the MF approximate ones.

The paper is organized as follows. In Sec. II the model for irreversible nucleation is presented and the fundamental quantities needed in the rest of the paper are introduced. The method for the solution of the problem is also outlined. Sections III and IV are devoted to the presentation of the exact results obtained in $d=1$ and $d=2$, respectively. In Sec. V these results are discussed and interpreted in physically intuitive terms. The conclusions and the perspectives of this work can be found in Sec. VI.

Some of the most important results have been presented previously in Ref. [4].

## II. THE PROBLEM AND THE METHOD OF SOLUTION
In this section we briefly recall the basic concepts of irreversible dimer nucleation along with some results, obtained in the first paper [1], that will be needed in the following.

We consider particles deposited onto a crystalline terrace of size $L$, modeled as a discrete lattice (a square lattice in $d=2$). The flux of particles is uncorrelated, uniform and of intensity $F$, so that the average interarrival time is $\tau_{dep}=(FL^d)^{-1}$. Once on the terrace, an adatom hops at rate $(\Delta t)^{-1}=2dD$ to a randomly chosen nearest neighbor, until it either meets another adatom or leaves the terrace.

This last process can be hindered by the additional Ehrlich-Schwoebel (ES) barrier [5] reducing interlayer transport to a rate $2dD'$: the ES length $\ell_{\text{ES}}=(D/D'-1)a_0$ measures the strength of the barrier (in the following the lattice constant $a_0$ is used as unit length).

The average time spent by a single adatom on the terrace is the residence time and depends on $L$ and $\ell_{\text{ES}}$,

*Present address: Istituto di Fisica Applicata "Nello Carrara," Consiglio Nazionale delle Ricerche, Via Panciatichi, 56/30, 50127 Firenze, Italy. Email address: politi@ifac.cnr.it
$^{\dagger}$Email address: castella@pil.phys.uniroma1.it

---
1063-651X/2002/66(3)/031606(15)/$20.00
66 031606-1
©2002 The American Physical Society

$$
\tau_{res}=(\beta L+\alpha \ell_{\mathrm{ES}}) L / D. \tag{1}
$$

In the limit $\ell_{\mathrm{ES}}=0$, $\tau_{res}$ is equal to $\tau_{tr}$, the average time needed by an adatom to reach the terrace boundary. Depending on the value of $\ell_{\mathrm{ES}}$, three different regimes may occur: (i) Zero or weak barriers $(\tau_{tr} \simeq \tau_{res} \ll \tau_{dep})$; (ii) strong barriers $(\tau_{tr} \ll \tau_{res} \ll \tau_{dep})$; (iii) infinite barriers $(\tau_{tr} \ll \tau_{dep}$ $\ll \tau_{res})$.

Particles are deposited according to an exponential distribution of interarrival times: $P_{\mathrm{dep}}(\tau)=\tau_{dep}^{-1} \exp (-\tau / \tau_{dep})$. This implies that all quantities should be computed for a generic interarrival time $\tau$ and then the results should be averaged over $P_{\mathrm{dep}}(\tau)$. However, we have shown in Ref. [1] that this is equivalent to considering two particles deposited simultaneously, one with distribution $p_{n}^{U}=1 / L^{d}$ and the other with an effective distribution
$$
p_{n}^{\mathrm{eff}}=\frac{\tau_{res}}{\tau_{dep}+\tau_{res}} p_{n}^{S}, \tag{2}
$$
where $p_{n}^{S}$ is the normalized solution of the discrete stationary diffusion equation in the presence of a constant flux. For infinite barriers (regime iii) $p_{n}^{\mathrm{eff}}=p_{n}^{S}=1 / L^{d}$. For strong but finite barriers (regime ii) $p_{n}^{\mathrm{eff}}=(\tau_{res} / \tau_{dep}) p_{n}^{S}$ $=(\tau_{res} / \tau_{dep}) 1 / L^{d}$. In the limit of zero or weak barriers (regime i) $p_{n}^{\mathrm{eff}}=(\tau_{res} / \tau_{dep}) p_{n}^{S}$ where $p_{n}^{S}$ has a parabolic shape that vanishes at the edges, reflecting the presence of absorbing boundaries.

Nucleation of dimers takes place when particles are on adjacent lattice sites; here we will assume instead that a dimer is formed when two particles are on the same site: this avoids useless mathematical complications without modifying the physics of the nucleation process.

The physical quantities we are interested in are $P(n)$, $Q(t)$, and $\omega$.

(1) $P(n)$ is the spatial distribution of nucleation events, computed for two adatoms deposited at the same time with normalized distributions $p^{S}$ (the first) and $p^{U}$ (the second). $P^{(N)}(n)$ is its normalized version.

(2) The distribution $Q(t)$ is the probability that a nucleation event occurs at time $t$, if the two adatoms have been deposited at time zero. $Q(t)$ is not considered within the standard mean-field theory.

$P(n)$ and $Q(t)$ are derived from the same quantity, the probability $R(n,t)$ that a nucleation event occurs on site $n$ at time $t$,
$$
P(n)=\sum_{t} R(n, t), \quad Q(t)=\sum_{n} R(n, t). \tag{3}
$$

We can also define $W$, the probability that two atoms meet before leaving the terrace: it is clearly related to $P(n)$ and $Q(t)$, because
$$
W \equiv \sum_{n, t} R(n, t)=\sum_{n} P(n)=\sum_{t} Q(t). \tag{4}
$$

$W$ is equal to 1 for large or infinite barriers [regimes (ii) and (iii)], but it differs from unity in regime (i). The normalized spatial distribution is clearly $P^{(N)}(n)=P(n)/W$.

(3) The nucleation rate $\omega$ is the total number of nucleation events that occur on the whole terrace per unit time. It is related to $P(n)$ or $Q(t)$ via $W$,
$$
\omega=F L^{d} \frac{\tau_{res}}{\tau_{dep}+\tau_{res}} W. \tag{5}
$$

$P(n)$ and $Q(t)$ (and then $W$) depend on the normalized initial distributions for the two adatoms. Therefore, they have the same expressions in regime (ii) and (iii), where $p_{n}^{S}$ is just a constant. From Eq. (5) instead, one immediately realizes that $\omega$ has different expressions in each of the three regimes.

We also consider an artificial model where adatoms are independent diffusing particles. They do not stop when they meet and each encounter is considered as a (fictitious) nucleation. As shown in Ref. [1], this model gives exactly the same results as mean-field theory.

The computation of the quantities of interest requires the evaluation of $R(n,t)$. Since we consider irreversible dimer formation, $R(n,t)$ is the probability that two particles diffusing on a $d$-dimensional terrace meet for the first time on site $n$ at time $t$. A method for treating the diffusion of two particles is to take their $d+d$ coordinates as the coordinates of a single random walker diffusing on a $d'=2d$-dimensional hypercubic terrace. In this picture a nucleation event corresponds to the $d'$-dimensional walker reaching the $d$-dimensional hyperplane where the coordinates of the two particles are equal. The irreversibility of dimer formation implies that an absorbing boundary condition must be imposed on this $d$-dimensional hyperplane. The probability of dimer formation $R(n,t)$ is then given by the probability current orthogonal to the hyperplane.

More specifically, in $d=1$ we pass from two walkers of coordinates $n$ and $m$ to a single walker on a square terrace. Nucleation occurs when the walker reaches the diagonal of such a terrace $(n=m)$. In $d=2$ we must consider a single walker in a four-dimensional space whose coordinates are $(n_{1},m_{1},n_{2},m_{2})$ and the hyperplane is now a bidimensional plane defined by the conditions $n_{1}=n_{2}$ and $m_{1}=m_{2}$.

In this way we have reduced the dimer nucleation problem to a first passage problem [6]. The solution of such a problem [7] is possible analytically in $d=1$ (Sec. III) and numerically in higher dimensions (Sec. IV).

### III. RESULTS IN ONE DIMENSION

When the system is one dimensional, the two adatoms are mapped into a two-dimensional walker hopping inside a square lattice of size $L$ with probability $p_{m,n}(t)$ to be in site $(m,n)$ at time $t$. Assuming that, when two adatoms are present, one of them, randomly chosen, moves once every time unit, the discrete evolution equation for $p_{m,n}(t)$ is
$$
\begin{aligned}
p_{m,n}(t+1)= & \frac{1}{4}\left[p_{m+1,n}(t)+p_{m-1,n}(t)+p_{m,n+1}(t)\right. \\
& \left.+p_{m,n-1}(t)\right],
\end{aligned} \tag{6}
$$
where the discrete time unit corresponds now to a physical time $\Delta t=1/(2d'D)=1/(4dD)$.


The indices $m,n$ vary between 1 and $L$, but in order to use Eq. (6) for all terrace sites it is useful to introduce fictitious sites in $m=0,L+1$ and $n=0,L+1$. In this way, boundary conditions are easily written for generic values of the ES barrier: $p_{0,n}=ap_{1,n}$, $p_{L+1,n}=ap_{L,n}$, $p_{m,0}=ap_{m,1}$, $p_{m,L+1}$ $=ap_{m,L}$, where $a=\ell_{\rm ES}/(1+\ell_{\rm ES})$. They apply at any time and for all edge sites. There is also an additional boundary condition along the square diagonal

$$
p_{n,n}(t)=0,\ n=1,\dots,L, \tag{7}
$$

because the two adatoms stop diffusing when they meet. The initial condition is $p_{m,n}(0)=p_m^U p_n^S$, but it is also correct to write $p_{m,n}(0)=p_m^S p_n^U$. In order to obtain a spatial distribution $P(n)$ that is properly symmetrical with respect to the center of the terrace we use the symmetrized expression

$$
p_{m,n}(0)=\frac{1}{2}\bigl[p_m^U p_n^S+p_m^S p_n^U\bigr]. \tag{8}
$$

The basic quantity we want to compute, the nucleation probability on site $n$ at time $t+1$, is

$$
\begin{aligned}
R(n,t+1)=&\frac{1}{4}\bigl[p_{n+1,n}(t)+p_{n-1,n}(t)+p_{n,n+1}(t)\\
&+p_{n,n-1}(t)\bigr]. \tag{9}
\end{aligned}
$$

In the case of noninteracting particles, the boundary condition along the diagonal is dropped and Eq. (9) is replaced by

$$
R(n,t)=p_{n,n}(t). \tag{10}
$$

An explicit analytic solution of the problem, both for interacting and noninteracting particles, is possible in the limits of zero and infinite ES barriers and will be presented in detail below. As remarked in Sec. II, for $P$, $Q$, and $W$ only two distinct regimes exist, and $\ell_{\rm ES}=0,\infty$ are their representative limits.

### A. Zero barriers [regime (i)]
When no ES barrier is present, $\ell_{\rm ES}=0$ and $a=0$. Hence the boundary conditions are simply $p_{0,n}=p_{L+1,n}=p_{m,0}$ $=p_{m,L+1}=0$, indicating that edges are absorbing boundaries. In the limit $\ell_{\rm ES}=0$ the normalized stationary distribution is

$$
p_n^S=\frac{6}{L(L+1)(L+2)}n(L+1-n). \tag{11}
$$

#### 1. Noninteracting adatoms
By separating space and time variables in a way perfectly analogous to the treatment of a single particle [1], we find the general solution of Eq. (6),

![](./images/812452544222593024_1.jpg)

FIG. 1. Normalized spatial distribution $P^{(N)}(n)$ for $d=1$ and $\ell_{\rm ES}=0$. Empty circles are for interacting particles, full circles for noninteracting particles (mean-field theory). $L=100$ in the main part, $L=20$ in the inset.

$$
\begin{aligned}
p_{m,n}(t)=&\sum_{k,j=1}^L B_{kj}\frac{1}{2^t}\Bigg[\cos\left(\frac{k\pi}{L+1}\right)\\
&+\cos\left(\frac{j\pi}{L+1}\right)\Bigg]^t\sin\left(\frac{mk\pi}{L+1}\right)\sin\left(\frac{nj\pi}{L+1}\right), \tag{12}
\end{aligned}
$$

where the coefficients $B_{kj}$ are

$$
B_{kj}=\left(\frac{2}{L+1}\right)^2\sum_{m,n=1}^L p_{m,n}(0)\sin\left(\frac{mk\pi}{L+1}\right)\sin\left(\frac{nj\pi}{L+1}\right). \tag{13}
$$

Given the explicit form (8) of $p_{m,n}(0)$, the coefficients $B_{kj}$ are (see Ref. [1])

$$
B_{kj}=A_k^U A_j^S \tag{14}
$$

$$
\begin{aligned}
=&\frac{12}{L^2(L+1)^3(L+2)}\frac{\sin\left(\frac{k\pi}{2}\right)\sin\left(\frac{j\pi}{2}\right)}{\sin\left[\frac{k\pi}{2(L+1)}\right]\sin^3\left[\frac{j\pi}{2(L+1)}\right]}\\
&\times\sin\left[\frac{Lk\pi}{2(L+1)}\right]\sin\left[\frac{Lj\pi}{2(L+1)}\right] \tag{15}
\end{aligned}
$$

and this allows the evaluation of all the quantities of interest.

*Nucleation sites.* The spatial distribution of nucleation sites is

$$
P_{\rm NI}(n)=\sum_{t=0}^{\infty} R(n,t)=\sum_{t=0}^{\infty} p_{n,n}(t). \tag{16}
$$

Its normalized version $P_{\rm NI}^{(N)}(n)$ is plotted in Fig. 1. As proven in Ref. [1] within a continuum formalism, it is equal to the mean-field distribution. This result can be easily proven analytically in a discrete lattice as well.

Nucleation times. The distribution of nucleation times is given by

$$
\begin{aligned}
Q_{\mathrm{NI}}(t) & =\sum_{n=1}^{L} p_{n, n}(t) \\
& =\sum_{k, j=1}^{L} B_{k j}\left\{\frac{1}{2}\left[\cos \left(\frac{k \pi}{L+1}\right)+\cos \left(\frac{k \pi}{L+1}\right)\right]\right\} \sum_{n=1}^{L} \sin \left(\frac{n k \pi}{L+1}\right) \sin \left(\frac{n j \pi}{L+1}\right) \\
& =\frac{L+1}{2} \sum_{k=1}^{L} B_{k k} \cos ^{t}\left(\frac{k \pi}{L+1}\right)
\end{aligned}
$$

and it is plotted in Fig. 2. To find analytically the behavior of $Q_{\mathrm{NI}}(t)$ for large $L$, we rewrite it in the following form:

$$
Q_{\mathrm{NI}}(t)=\frac{L+1}{2} \sum_{k=1}^{L} B_{k k} \exp \left[t \ln \cos \left(\frac{k \pi}{L+1}\right)\right]. \quad(20)
$$

The coefficients $B_{k k}$ diverge for small $k$ as $k^{-4} \ (B_{k k}$ $\simeq 192 /[\pi^{4} k^{4}(L+1)(L+2) L^{2}])$ , so that the dominant contribution to the sum for large $L$ comes from the first mode $k$ $=1$. Expanding the small argument of the cosine this gives

$$
Q_{\mathrm{NI}}(t) \sim \exp \left[-\frac{t}{2}\left(\frac{\pi}{L+1}\right)^{2}\right], \quad(21)
$$

which is exactly the exponential decay appearing in Fig. 2.

Nucleation rate. Let us first compute $W_{\mathrm{NI}}=\sum_{n} P(n)$ $=\sum_{t} Q(t)$ that for noninteracting particles is not a probability but the total number of times the two adatoms meet before leaving the terrace ($W_{\mathrm{NI}}$ can be larger than 1),

$$
W_{\mathrm{NI}}=\frac{L+1}{2} \sum_{k=1}^{L} \frac{B_{k k}}{1-\cos \left(\frac{k \pi}{L+1}\right)}. \quad(22)
$$

Using the explicit form of $B_{k k}$ , we obtain

$$
W_{\mathrm{NI}}=\frac{3}{L^{2}(L+1)^{2}(L+2)} \sum_{k=1}^{L} \frac{\sin ^{2}\left(\frac{k \pi}{2}\right) \sin ^{2}\left(\frac{L k \pi}{2(L+1)}\right)}{\sin ^{6}\left(\frac{k \pi}{2(L+1)}\right)}.
$$

For large $L$ the dominant contribution is provided by the term with $k=1$ , which gives

$$
\begin{aligned}
W_{\mathrm{NI}} & \simeq \frac{3}{L^{2}(L+1)^{2}(L+2)}\left[\frac{2(L+1)}{\pi}\right]^{6}=3\left(\frac{2}{\pi}\right)^{6} \frac{(L+1)^{4}}{L^{2}(L+2)} \\
& \simeq 0.2 L. \quad(24)
\end{aligned}
$$

Hence the total nucleation rate is

$$
\omega_{\mathrm{NI}} \simeq F L \frac{\tau_{r e s}}{\tau_{d e p}} 3\left(\frac{2}{\pi}\right)^{6} \frac{(L+1)^{4}}{L^{2}(L+2)}. \quad(25)
$$

Using the explicit expression [1] $\tau_{res}=\tau_{tr}=L^{2}/(12D)$ , and considering only the leading order in $L$, we find

$$
\omega_{\mathrm{NI}} \simeq \frac{1}{4}\left(\frac{2}{\pi}\right)^{6} \frac{F^{2} L^{5}}{D}. \quad(26)
$$

### 2. Interacting adatoms
For interacting adatoms it is possible to take advantage of the noninteracting solution (12) by using a trick: we pass from the initial condition $p_{m,n}(0)$ [given in Eq. (8)] to an auxiliary antisymmetric initial condition

$$
\tilde{p}_{m, n}(0)=\left\{\begin{array}{rll}
p_{m, n}(0) & \text { for } & m<n \\
0 & \text { for } & m=n \\
-p_{n, m}(0) & \text { for } & m>n,
\end{array} \quad(27)\right.
$$

which satisfies the boundary condition $\tilde{p}_{n,n}=0$ along the diagonal.

![](./images/812452544222593024_2.jpg)

FIG. 2. The temporal distribution $Q(t)$ for $d=1$ and $L=100$. From top to bottom, data are for noninteracting particles ($\ell_{\text{ES}}=\infty$ and $\ell_{\text{ES}}=0$) and interacting particles ($\ell_{\text{ES}}=\infty$ and $\ell_{\text{ES}}=0$). The main part of the figure highlights the power-law decay for short times (log-log plot): the solid line goes as $t^{-1/2}$. The inset highlights the exponential decay for long times (ln-log plot).

Let us observe that the dynamics given in Eq. (6) con- serves the parity of the spatial distribution, because
$$
\begin{array}{r}
\tilde{p}_{m, n}(0)=-\tilde{p}_{n, m}(0) \Rightarrow B_{k j}=-B_{j k} \Rightarrow \tilde{p}_{m, n}(t)=-\tilde{p}_{n, m}(t). \\
(28)
\end{array}
$$

This means that if we start with an antisymmetric distri- bution $\tilde{p}_{m, n}(0)=-\tilde{p}_{n, m}(0)$ , the boundary condition $\tilde{p}_{n, n}(t)$ =0 is obeyed for all times: the two triangles $(m>n)$ and(m<n) are dynamically disconnected. The solution of Eq.(6) is therefore still given by Eq. (12), since the boundary condition is fully taken into account by the value of the coefficients $B_{k j}$ , which depends on the antisymmetric form of $\tilde{p}_{m, n}(0)$ .

The coefficients $B_{k j}$ are given by
$$
B_{k j}=\left(\frac{2}{L+1}\right)^{2} \sum_{m, n=1}^{L} \tilde{p}_{m, n}(0) \sin \left(\frac{m k \pi}{L+1}\right) \sin \left(\frac{n j \pi}{L+1}\right).
$$

In this expression we can decompose the summation $\sum_{m, n}$ as∑m<n+∑m>n, in the latter interchange the dumb indices n, m, and exploit the antisymmetry of $\tilde{p}_{m, n}(0)$ . We finally obtain
$$
\begin{aligned}
B_{k j}= & \left(\frac{2}{L+1}\right)^{2} \sum_{m<n} p_{m, n}(0)\left\{\sin \left(\frac{m k \pi}{L+1}\right) \sin \left(\frac{n j \pi}{L+1}\right)\right. \\
& \left.-(k \Leftrightarrow j)\right\} \equiv\left[B_{k j}^{<}-B_{j k}^{<}\right],
\end{aligned}\qquad(30)$$
where
$$B_{k j}^{<}=\left(\frac{2}{L+1}\right)^{2} \sum_{m<n} p_{m, n}(0) \sin \left(\frac{m k \pi}{L+1}\right) \sin \left(\frac{n j \pi}{L+1}\right). \quad(31)$$

The evaluation of $B_{k j}$ is here less straightforward than in the noninteracting case. In particular, some sums are not eas- ily performed explicitly. This makes difficult the presentation of explicit results. Therefore in the following we will present only the general results, leaving the coefficients $B_{k j}$ indi cated.
Nucleation sites. Since the regions m<n and m>n are equivalent, the probability of a nucleation event on site n at time t+1>0 is given by $R(n, t+1)=\frac{1}{2}[\tilde{p}_{n, n+1}(t)$  $+\tilde{p}_{n-1, n}(t)]$ , while for t=0 nucleations occur because both adatoms are deposited on the same site, i.e., with probability Pn.n(0). The spatial distribution of nucleation sites is there- fore
$$\begin{aligned}
P(n)= & p_{n, n}(0)+\frac{1}{2} \sum_{t=0}^{\infty}\left[\tilde{p}_{n, n+1}(t)+\tilde{p}_{n-1, n}(t)\right] \quad(32) \\
= & p_{n, n}(0)+\frac{1}{2} \sum_{k, j=1}^{L} \frac{B_{k j}}{1-\frac{1}{2}\left[\cos \left(\frac{k \pi}{L+1}\right)+\cos \left(\frac{j \pi}{L+1}\right)\right]} \\
& \times\left\{\sin \left(\frac{n k \pi}{L+1}\right) \sin \left[\frac{(n+1) j \pi}{L+1}\right]\right. \\
& \left.+\sin \left[\frac{(n-1) k \pi}{L+1}\right] \sin \left(\frac{n j \pi}{L+1}\right)\right\}
\end{aligned}\qquad(33)$$
 and the normalized distribution $P^{(N)}(n)$ is presented in Fig.1. The plot clearly shows that the spatial distribution is very similar to the mean-field result $P_{NI}^{(N)}(n)$ , although a small discrepancy exists (see the discussion in Sec. V A).
Nucleation times. The distribution of nucleation times for interacting particles is
$$Q(0)=\sum_{n=1}^{L} p_{n, n}(0),\qquad(34)$$

$$Q(t+1>0)=\sum_{n=1}^{L} \frac{1}{2}\left[\tilde{p}_{n, n+1}(t)+\tilde{p}_{n-1, n}(t)\right].\qquad(35)$$

Once summed, the two terms in Eq. (35) are equal. Hence,
$$\begin{aligned}
Q(t+1>0) & =\sum_{n=1}^{L} \tilde{p}_{n-1, n}(t) & & (36) \\
& =\sum_{k, j=1}^{L} B_{k j} C_{k j}\left\{\frac{1}{2}\left[\cos \left(\frac{k \pi}{L+1}\right)+\cos \left(\frac{j \pi}{L+1}\right)\right]\right\}^{t}, & & (37)
\end{aligned}$$
 where the coefficients $C_{k j}$ are
$$\begin{aligned}
C_{k j} & =\sum_{n=1}^{L} \sin \left[\frac{k \pi(n-1)}{L+1}\right] \sin \left(\frac{j \pi n}{L+1}\right) & & (38) \\
& =\frac{1}{2}\left\{\cos \left[\frac{k \pi}{L+1}+\frac{L(j-k) \pi}{2(L+1)}\right] \sin \left[\frac{(j-k) \pi}{2}\right] \operatorname{cosec}\left[\frac{(j-k) \pi}{2(L+1)}\right]-\cos \left[-\frac{k \pi}{L+1}+\frac{L(j+k) \pi}{2(L+1)}\right] \sin \left[\frac{(j+k) \pi}{2}\right] \operatorname{cosec}\left[\frac{(j+k) \pi}{2(L+1)}\right]\right\}. & & (39)
\end{aligned}$$


$Q(t)$ is shown in Fig. 2. For short times it decays slowly (as $t^{-1/2}$), while it goes down exponentially for large times. In Appendix A we show in detail that the behavior of $Q(t)$ for short and long times can be derived explicitly in the case of two adatoms with uniform initial distributions, for which the coefficients $B_{kj}$ are explicitly known: for $t\ll 2L^{2}/\pi^{2}$ we find

$$
Q(t)\simeq \frac{8}{L\pi^{5/2}\sqrt{t/2}}, \tag{40}
$$

and for $t\gg 2L^{2}/\pi^{2}$,

$$
Q(t)\simeq \frac{80}{9\pi^{2}L^{2}}\exp\left[ -\frac{5t}{4}\left( \frac{\pi}{L+1}\right) ^{2}\right]. \tag{41}
$$

No qualitative change is expected if one atom is initially distributed according to $p_{n}^{S}$ rather than $p_{n}^{U}$: only prefactors are expected to be different and this is confirmed by the behavior shown in Fig. 2.

Nucleation rate. The probability $W$ of a nucleation event is

$$
W=\frac{1}{L}+\sum_{k,j=1}^{L}\frac{B_{kj}C_{kj}}{1-\frac{1}{2}\left[ \cos\left( \frac{k\pi}{L+1}\right) +\cos\left( \frac{j\pi}{L+1}\right) \right] }. \tag{42}
$$

In Appendix A we prove that for large $L$, $W$ goes to a constant. This constant is found numerically to be roughly equal to 0.47. Hence, for large $L$, the nucleation rate is

$$
\omega=FL\frac{\beta L^{2}}{D}FLW\simeq 0.04\frac{F^{2}L^{4}}{D}. \tag{43}
$$

### B. Strong and infinite barriers [regimes (ii) and (iii)]

With infinite ES barriers, $\ell_{\text{ES}}=\infty$ and $a=1$. Step edges are perfectly reflecting barriers and boundary conditions are $p_{1,n}=p_{0,n}$, $p_{L,n}=p_{L+1,n}$, $p_{m,1}=p_{m,0}$, $p_{m,L}=p_{m,L+1}$. The normalized stationary distribution is simply $p_{n}^{S}=p_{n}^{U}=1/L$, because the distribution of the first adatom is still flat when the second arrives.

The general solution for a two-dimensional walker is now

$$
p_{m,n}(t)=\sum_{k,j=0}^{L-1}B_{kj}\frac{1}{2^{t}}\left[ \cos\left( \frac{k\pi}{L}\right) +\cos\left( \frac{j\pi}{L}\right) \right] ^{t}X_{k}(m)X_{j}(n), \tag{44}
$$

where

$$
X_{k}(n)=\tan\left( \frac{k\pi}{2L}\right) \sin\left( \frac{nk\pi}{L}\right) +\cos\left( \frac{nk\pi}{L}\right) \tag{45}
$$

and the coefficients are

$$
B_{kj}=\frac{1}{N_{k}N_{j}}\sum_{m,n=1}^{L}p_{m,n}(0)X_{k}(m)X_{j}(n) \tag{46}
$$

with ($\delta_{k0}$ is the Kronecker symbol)

$$
N_{k}=\frac{L}{2}\left[ 1+\tan^{2}\left( \frac{k\pi}{2L}\right) \right] (1+\delta_{k0}). \tag{47}
$$

### 1. Noninteracting adatoms

The case with noninteracting adatoms is completely trivial for infinite barriers. At any time, $p_{m,n}(t)=1/L^{2}$ so that the spatial and temporal distributions of nucleation events are constant. The total number of nucleation events $W_{\text{NI}}$ is clearly infinite.

### 2. Interacting adatoms

In a way analogous to the case with zero barriers, we consider antisymmetric initial conditions and we obtain

$$
\begin{aligned}
B_{kj}&=\frac{1}{N_{k}N_{j}}\sum_{m<n}p_{m,n}(0)\{X_{k}(m)X_{j}(n)-(k\Leftrightarrow j)\} \\
&\equiv [B_{kj}^{\leq}-B_{jk}^{\leq}], \tag{48}
\end{aligned}
$$

where

$$
B_{kj}^{\leq}=\frac{1}{N_{k}N_{j}}\sum_{m<n}p_{m,n}(0)X_{k}(m)X_{j}(n). \tag{49}
$$

More explicitly ($p_{m,n}(0)=1/L^{2}$),

$$
\begin{aligned}
B_{kj}^{\leq}=&\frac{1}{L^{2}N_{k}N_{j}}\sum_{n=1}^{L}X_{j}(n)\sum_{m=1}^{n-1}X_{k}(m) \tag{50} \\
=&\frac{1}{L^{2}N_{k}N_{j}}\sum_{n=1}^{L}\Bigg[ \tan\left( \frac{j\pi}{2L}\right) \sin\left( \frac{nj\pi}{L}\right) \\
&+\cos\left( \frac{nj\pi}{L}\right) \Bigg] \sum_{m=1}^{n-1}\left[ \tan\left( \frac{k\pi}{2L}\right) \sin\left( \frac{mk\pi}{L}\right) +\cos\left( \frac{mk\pi}{L}\right) \right].
\tag{51}
\end{aligned}
$$

Nucleation sites. The distribution of nucleation sites is given by

$$
\begin{aligned}
P(n)=&p_{n,n}(0)+\frac{1}{2}\sum_{t=0}^{\infty}[\tilde{p}_{n,n+1}(t)+\tilde{p}_{n-1,n}(t)] \tag{52} \\
=&\frac{1}{L^{2}}+\frac{1}{2}\sum_{k,j=0}^{L-1}\frac{B_{kj}}{1-\frac{1}{2}\left[ \cos\left( \frac{k\pi}{L+1}\right) +\cos\left( \frac{j\pi}{L+1}\right) \right] } \\
&\times [X_{k}(n)X_{j}(n+1)+X_{k}(n-1)X_{j}(n)] \tag{53}
\end{aligned}
$$

and it is plotted in Fig. 3 [in this case $P^{(N)}(n)$ and $P(n)$ coincide, since $W=1$]. The distribution has a rounded peak in the middle of the terrace and vanishes towards the boundaries.

![](./images/812452544222593024_3.jpg)

FIG. 3. Normalized spatial distribution $P^{(N)}(n)$ for $d=1$ and $\ell_{\mathrm{ES}}=\infty$. Empty circles are for interacting particles, full circles for noninteracting particles (mean-field approximation). $L=100$ in the main part, $L=20$ in the inset.

The above expression for $P(n)$ is exact, but it is not easy to use in applications. A simpler, approximate, expression is therefore highly desirable. In Sec. V A we show that $P(n)$ is well fitted by a hyperbolic cosine. Up to the normalization factor,

$$
P(n)=\cosh (\pi)-\cosh \left[\pi\left(\frac{2 n}{L+1}-1\right)\right]. \quad(54)
$$

In Fig. 4 we compare exact and approximate distributions: the agreement is fair already for relatively small sizes and very good for large sizes.

Nucleation times. As in the case with no barriers, we have

$$
Q(0)=\sum_{n=1}^{L} p_{n, n}(0),\qquad(55)
$$

$$
Q(t+1>0)=\sum_{n=1}^{L} \tilde{p}_{n-1, n}(t).\qquad(56)
$$

![](./images/812452544222593024_4.jpg)

FIG. 4. Comparison of the normalized spatial distribution $P^{(N)}(n)$ for $d=1$ and $\ell_{\mathrm{ES}}=\infty$ (circles) with the approximate formula (54) (solid line). $L=128$ (main), $L=16$ (inset).

Using the expression for $\tilde{p}_{m, n}(t)$,

$$
Q(0)=\frac{1}{L},\qquad(57)
$$

$$
Q(t+1>0)=\sum_{k, j=0}^{L-1} B_{k j} C_{k j}\left\{\frac{1}{2}\left[\cos \left(\frac{k \pi}{L}\right)+\cos \left(\frac{j \pi}{L}\right)\right]\right\}^{t},
$$

where the coefficients $C_{k j}$ are now

$$
C_{k j}=\sum_{n=1}^{L} X_{k}(n-1) X_{j}(n).\qquad(59)
$$

The form of $Q(t)$ is shown in Fig. 2. The decay is the same as for zero barriers: for short times it decays as $t^{-1 / 2}$ and for large times exponentially. Physically intuitive interpretations of these behaviors are discussed in Sec. V B.

Nucleation rate. Since $W=1$, the nucleation rate in regime (ii) is

$$
\omega(L)=F L \frac{\tau_{r e s}}{\tau_{d e p}}=\frac{F^{2} L^{3} \ell_{\mathrm{ES}}}{2 D},\qquad(60)
$$

while in regime (iii) it is simply

$$
\omega(L)=F L=\frac{1}{\tau_{d e p}}.\qquad(61)
$$

### C. Intermediate barriers

For intermediate values of the barriers, i.e., values of $a$ between 0 and 1, an explicit analytic solution of the problem is not possible, even for noninteracting adatoms. This is a direct consequence of the lack of an explicit solution for intermediate barriers even in the case of a single particle (Ref. [1]). Nevertheless the problem can easily be solved numerically for any $\ell_{\mathrm{ES}}$, through direct calculation of the dynamical evolution of $p_{m, n}(t)$, which determines $R(n, t)$ and all the quantities of interest.

The systematic error in the results, due to the integration of Eq. (6) up to a finite time, is fully negligible for realistic values of $L$: the probability $Q(t)$ that nucleation occurs at time $t$ decays exponentially for large $t$ and consequently the systematic error can easily be made exceedingly small. All numerical results presented in this paper can be considered virtually exact.

As expected, the results for intermediate barriers smoothly interpolate between the two limits of zero or infinite barriers, $\ell_{\mathrm{ES}} / L$ being the only relevant parameter.

The spatial distribution of nucleation events $P^{(N)}(n)$ is presented in Fig. 5 for $L=50$ and several values of $\ell_{\mathrm{ES}}$ $(\ell_{\mathrm{ES}}=0,10,50,250)$. Even a small value $\ell_{\mathrm{ES}} / L=1 / 5$ changes in a notable way the distribution $P^{(N)}(n)$. The tem-

![](./images/812452544222593024_5.jpg)

FIG. 5. Normalized spatial distribution $P^{(N)}(n)$ for $d=1$ and $L=50$. Empty circles are for interacting particles, full circles for noninteracting particles (MFT). $\ell_{\text{ES}}=0$ (top left), $\ell_{\text{ES}}=10$ (top right), $\ell_{\text{ES}}=50$ (bottom left), $\ell_{\text{ES}}=250$ (bottom right).

poral distribution $Q(t)$ smoothly interpolates between the two limit behaviors presented in Fig. 2.

## IV. RESULTS IN TWO DIMENSIONS

When the terrace is two dimensional the motion of two adatoms can be mapped into a four-dimensional problem for a single random walker: $p_{m_{1},n_{1},m_{2},n_{2}}(t)$ is the probability of finding one atom on site $(m_{1},n_{1})$ and the other in $(m_{2},n_{2})$ at time $t$. Such a probability obeys the equation of motion

$$
\begin{aligned}
p_{m_{1},n_{1},m_{2},n_{2}}(t+1)= & \frac{1}{8}[ p_{m_{1}+1,n_{1},m_{2},n_{2}}(t)+p_{m_{1}-1,n_{1},m_{2},n_{2}}(t) \\
& +p_{m_{1},n_{1}+1,m_{2},n_{2}}(t)+p_{m_{1},n_{1}-1,m_{2},n_{2}}(t) \\
& +p_{m_{1},n_{1},m_{2}+1,n_{2}}(t)+p_{m_{1},n_{1},m_{2}-1,n_{2}}(t) \\
& +p_{m_{1},n_{1},m_{2},n_{2}+1}(t) \\
& +p_{m_{1},n_{1},m_{2},n_{2}-1}(t) ]
\end{aligned}
\tag{62}
$$

with the boundary condition $p_{\widetilde{n}+\widetilde{\delta}}=ap_{\widetilde{n}}$, where $\widetilde{n}$ is any edge site of the four-dimensional hypercube and $(\widetilde{n}+\widetilde{\delta})$ is a nearest neighbor outside the cube. The initial condition is

$$
p_{m_{1},n_{1},m_{2},n_{2}}(0)=\frac{1}{2}[ p_{m_{1},n_{1}}^{U}p_{m_{2},n_{2}}^{S}+p_{m_{1},n_{1}}^{S}p_{m_{2},n_{2}}^{U} ],
\tag{63}
$$

where, as usual, $p_{m,n}^{U}=1/L^{2}$ is the uniform initial distribution in two dimensions and $p_{m,n}^{S}$ is the normalized stationary solution of the discrete diffusion equation in $d=2$.

### A. Zero barriers [regime (i)]

#### 1. Noninteracting adatoms

For noninteracting adatoms the computation of the quantities of interest proceeds along the same lines as in the one-dimensional case. The general solution of the equation of motion for the four-dimensional random walker is

$$
\begin{aligned}
p_{m_{1},n_{1},m_{2},n_{2}}(t)= & \sum_{k_{1},j_{1},k_{2},j_{2}=1}^{L}B_{k_{1}j_{1}k_{2}j_{2}}\frac{1}{4^{t}}\left[ \cos\left( \frac{k_{1}\pi}{L+1} \right)+\cos\left( \frac{j_{1}\pi}{L+1} \right)+\cos\left( \frac{k_{2}\pi}{L+1} \right)+\cos\left( \frac{j_{2}\pi}{L+1} \right) \right]^{t} \\
& \times\sin\left( \frac{m_{1}k_{1}\pi}{L+1} \right)\sin\left( \frac{n_{1}j_{1}\pi}{L+1} \right)\sin\left( \frac{m_{2}k_{2}\pi}{L+1} \right)\sin\left( \frac{n_{2}j_{2}\pi}{L+1} \right),
\end{aligned}
\tag{64}
$$

where the coefficients $B_{k_{1}j_{1}k_{2}j_{2}}$ are

$$
\begin{aligned}
B_{k_{1}j_{1}k_{2}j_{2}}= & \left( \frac{2}{L+1} \right)^{4}\sum_{m_{1},n_{1},m_{2},n_{2}=1}^{L}p_{m_{1},n_{1},m_{2},n_{2}}(0) \\
& \times\sin\left( \frac{m_{1}k_{1}\pi}{L+1} \right)\sin\left( \frac{n_{1}j_{1}\pi}{L+1} \right)\sin\left( \frac{m_{2}k_{2}\pi}{L+1} \right) \\
& \times\sin\left( \frac{n_{2}j_{2}\pi}{L+1} \right).
\end{aligned}
\tag{65}
$$

Given the initial condition (63), the coefficients $B_{k_{1}j_{1}k_{2}j_{2}}$ are of the form

$$
B_{k_{1}j_{1}k_{2}j_{2}}=A_{k_{1}j_{1}}^{U}A_{k_{2}j_{2}}^{S},
\tag{66}
$$

where $A_{kj}^{(U,S)}$ are the coefficients of the expansion of $p_{m,n}^{(U,S)}$ (see Ref. [1]).

The probability $R(m,n,t)$ of a (fictitious) nucleation event at time $t$ on site $(m,n)$ is given by $p_{m,n,m,n}(t)$.

Nucleation sites. The spatial distribution of nucleation sites is

$$
P_{\text{NI}}(m,n)=\sum_{t=0}^{\infty}R(m,n,t)=\sum_{t=0}^{\infty}p_{m,n,m,n}(t)
\tag{67}
$$

and its normalized version is reported in Fig. 6 [we plot it along the diagonal of the square terrace, $P_{\text{NI}}^{(N)}(n,n)$].

Nucleation times. The distribution of nucleation times is

$$
\begin{aligned}
Q_{\mathrm{NI}}(t)= & \sum_{m, n=1}^{L} p_{m, n, m, n}(t) \\
= & \sum_{k_{1}, j_{1}, k_{2}, j_{2}=1}^{L} B_{k_{1} j_{1} k_{2} j_{2}}\left\{\frac { 1 } { 4 } \left[\cos \left(\frac{k_{1} \pi}{L+1}\right)+\cos \left(\frac{j_{1} \pi}{L+1}\right)+\cos \left(\frac{k_{2} \pi}{L+1}\right)\right.\right. \\
& \left.\left.+\cos \left(\frac{j_{2} \pi}{L+1}\right)\right]\right\}^{t} \sum_{m, n=1}^{L} \sin \left(\frac{m k_{1} \pi}{L+1}\right) \sin \left(\frac{m k_{2} \pi}{L+1}\right) \sin \left(\frac{n j_{1} \pi}{L+1}\right) \sin \left(\frac{n j_{2} \pi}{L+1}\right) \\
= & \left(\frac{L+1}{2}\right)^{2} \sum_{k_{1}, j_{1}=1}^{L} B_{k_{1} j_{1} k_{1} j_{1}}\left\{\frac{1}{2}\left[\cos \left(\frac{k_{1} \pi}{L+1}\right)+\cos \left(\frac{j_{1} \pi}{L+1}\right)\right]\right\}^{t}
\end{aligned}
$$

and it is plotted in Fig. 7. For large times, only the most slowly decaying mode $k_{1}=1, j_{1}=1$ contributes to the sum, yielding

$$
Q_{\mathrm{NI}}(t) \sim \exp \left[t \ln \cos \left(\frac{\pi}{L+1}\right)\right] \simeq \exp \left[-\frac{t}{2}\left(\frac{\pi}{L+1}\right)^{2}\right].
$$

Nucleation rate. The total number of times the two adatoms meet before leaving the terrace is

$$
\begin{aligned}
W_{\mathrm{NI}} & =\sum_{m, n=1}^{L} P_{\mathrm{NI}}(m, n) \\
& =\left(\frac{L+1}{2}\right)^{2} \sum_{k_{1}, j_{1}=1}^{L} \frac{B_{k_{1} j_{1} k_{1} j_{1}}}{1-\frac{1}{2}\left[\cos \left(\frac{k_{1} \pi}{L+1}\right)+\cos \left(\frac{j_{1} \pi}{L+1}\right)\right]}.
\end{aligned}
$$

For large values of $L$ only the mode $(1,1,1,1)$ dominates the sum, so

$$
\begin{aligned}
W_{\mathrm{NI}} & \simeq\left(\frac{L+1}{2}\right)^{2} \frac{B_{1111}}{1-\frac{1}{2}\left[\cos \left(\frac{\pi}{L+1}\right)+\cos \left(\frac{\pi}{L+1}\right)\right]} \\
& \simeq \frac{2}{\pi^{2}}\left(\frac{L+1}{L}\right)^{6}
\end{aligned}
$$

and the total nucleation rate is

$$
\omega_{\mathrm{NI}} \simeq F L^{2} \frac{\tau_{r e s}}{\tau_{d e p}}\left(\frac{2}{\pi^{2}}\right)\left(\frac{L+1}{L}\right)^{6}.
$$

Using the expression $\left(\tau_{r e s} \simeq 2^{5} / \pi^{6}\right)\left(L^{2} / D\right)$ derived in Ref. [1], the leading term in $L$ is

$$
\omega_{\mathrm{NI}} \simeq \frac{64}{\pi^{8}} \frac{F^{2} L^{6}}{D}.
$$

![](./images/812452544222593024_6.jpg)

FIG. 6. Normalized spatial distribution $P^{(N)}(n, n)$ along the diagonal for $d=2, L=32$ and $\ell_{\mathrm{ES}}=0$. Empty circles are for interacting particles, full circles for noninteracting particles.

![](./images/812452544222593024_7.jpg)

FIG. 7. The temporal distribution for $d=2$ and $L=40$. In the main part $1 / Q(t)$ is plotted vs $t$ to highlight the logarithmic decay for short times. From top to bottom, data are for noninteracting particles $(\ell_{\mathrm{ES}}=\infty$ and $\ell_{\mathrm{ES}}=0)$ and interacting particles $(\ell_{\mathrm{ES}}=\infty$ and $\ell_{\mathrm{ES}}=0)$. The solid line goes as $\ln (t / t_{0})$ [i.e., $Q(t) \sim 1 / \ln (t / t_{0})]$. The inset shows the exponential decay of $Q(t)$ for long times.

![](./images/812452544222593024_8.jpg)

FIG. 8. Normalized spatial distribution $P^{(N)}(n,n)$ along the diagonal for $d=2$, $L=32$, and $\ell_{\text{ES}}=\infty$. Empty circles are for interacting particles, full circles for noninteracting particles.

### 2. Interacting adatoms
At odds with what happens for the one-dimensional case, the trick of using an initial condition antisymmetric with respect to particle interchange cannot be used in two dimensions for taking into account the interaction between particles. The physical reason is that in two dimensions two particles can swap their position without meeting. As a consequence, the configuration space cannot be split into two dynamically disconnected regions, because the condition $p_{m,n,m,n}(t)=0$ holds on a two-dimensional plane that does not divide the four-dimensional configuration space into separate domains. Hence it is not possible to implement the additional boundary condition $p_{m,n,m,n}(t)=0$ by choosing the initial condition to be antisymmetric. We have not been able to overcome this problem analytically and therefore for the interacting case we resort to the numerical solution of Eq. (62), which is easily performed, and gives virtually exact results (see Sec. III C). The results for $P^{(N)}(n,n)$ and $Q(t)$ are presented in Figs. 6 and 7, respectively. The spatial distribution as given by MF theory agrees with exact results even better than in $d=1$; the short time decay for $Q(t)$ does not follow a power law but rather a logarithmic one [$Q(t)$ $\sim 1/\ln(t/t_0)$].

For what concerns the total nucleation rate we find numerically $W\simeq0.25/\ln(L/1.3)$ and this implies
$$
\omega \simeq 0.008 \frac{F^{2}}{D} \frac{L^{6}}{\ln (L / 1.3)}. \tag{76}
$$

### B. Strong and infinite barriers [regimes (ii) and (iii)]
The results for $Q(t)$ are presented in Fig. 7 and those for $P^{(N)}(m,n)$ in Figs. 8 and 9. The spatial distribution along the diagonal (Fig. 8) behaves much in the same way as in $d$ $=1$; a qualitatively similar behavior is found along different directions (Fig. 9). A deeper analysis is deferred to Sec. V A.

The total number of nucleation events $W$ is clearly 1 and this implies, in regime (ii)

![](./images/812452544222593024_9.jpg)

FIG. 9. Normalized spatial distribution $P^{(N)}$ for $d=2$, $L=32$ and $\ell_{\text{ES}}=0$. Full circles are for noninteracting particles. Empty symbols are for interacting particles: along the diagonal (circles), along one edge (squares), and in the middle, parallel to one edge (diamonds).

$$
\omega=F L^{2} \frac{\tau_{r e s}}{\tau_{d e p}}=\frac{F^{2} L^{5} \ell_{\mathrm{ES}}}{4 D} \tag{77}
$$

and in regime (iii)
$$
\omega=F L^{2}=\frac{1}{\tau_{d e p}}. \tag{78}
$$

For intermediate barriers, the results for $P^{(N)}(n,n)$ are presented in Fig. 10. As in $d=1$, the spatial distribution interpolates between the two limits of zero and infinite barriers. As already remarked for the one-dimensional case, a relatively small ES barrier $(\ell_{\text{ES}}/L=1/5)$ remarkably affects the spatial distribution.

![](./images/812452544222593024_10.jpg)

FIG. 10. Normalized spatial distribution $P^{(N)}(n,n)$ along the diagonal for $d=2$ and $L=20$. Empty circles are for interacting particles, full circles for noninteracting particles. $\ell_{\text{ES}}=0$ (top left), $\ell_{\text{ES}}=4$ (top right), $\ell_{\text{ES}}=20$ (bottom left), $\ell_{\text{ES}}=100$ (bottom right).

## V. DISCUSSION OF THE RESULTS

### A. The spatial distribution

The form of the spatial distribution of nucleation sites has been presented in the previous two sections both in one and two dimensions and for all values of the ES barrier. Some remarks are in order.

As expected [1], we find that the mean-field assumption for the distribution of nucleation sites is *in general not exact* both in one and in two dimensions, for all values of $\ell_{\text{ES}}$ and for all $L$. The origin of the discrepancy between the exact form of $P(n)$ and the MF counterpart is clear: the mean-field approximation is equivalent to considering particles as noninteracting, i.e., taking into account not only the first nucleation event between the particles, but also all subsequent encounters between them that would occur should they keep diffusing after meeting.

Although not exactly the same, the mean-field distribution is however *a very good approximation* of the true spatial distribution, for zero or weak ES barriers, particularly in $d=2$. This result is somewhat striking, if we consider that the ratio $W_{\text{NI}}/W$ is proportional to $L$ in $d=1$ [Eq. (24)] and to $\ln L$ in $d=2$ [Eq. (73)]. Hence the relative weight of successive nucleations diverges for growing $L$; nevertheless $P_{\text{NI}}(n)$ is very close to $P(n)$, indicating that the distribution of all nucleation events following the first one is very similar to the distribution of the first.

Things are radically different for large ES barriers. In this case the discrepancy between MF and true distributions is remarkable. Also this result is somewhat counterintuitive. Particles are distributed uniformly at the beginning and each of them would remain like that forever in the absence of the other: this is the reason why the spatial distribution $P_{\text{NI}}$ for noninteracting particles is uniform. The interaction between particles breaks this uniformity. Consider, for example, the one-dimensional case. The nucleation probability on site $n$ close to the center of the terrace, is the sum of the statistical weight of all pairs of random walks (one for each particle) with the constraint that they intersect for the first time in $n$. If the site $n$ is close to an edge, one of these walks is reflected by the boundary and the weight of walks intersecting for the first time in $n$ is strongly reduced.

An “entropic” mechanism is present for weak barriers as well: in this case nucleation close to an edge is made difficult by adsorbing boundaries, which reduce the probability to find an atom close to the steps. For weak barriers $P(n)$ is peaked around the middle of the terrace also because the initial distribution for one atom is not uniform, but parabolic.

Notice however that for infinite barriers the mean-field distribution, which includes the contribution of successive encounters, is completely flat. This indicates that, even if it is relatively unusual for particles to meet close to edges, once this happens they tend to meet there several times and this restores uniformity in the distribution of all nucleation events.

In Eq. (54) we have proposed an approximate expression for the distribution $P(n)$ in the limit of infinite ES barriers. It has been derived assuming a behavior as an hyperbolic cosine
$$
P(n)=a_{0}\left[a_{1}-\cosh \left(a_{2} n-a_{3}\right)\right]\qquad(79)
$$
and imposing that $P(n)$ is symmetrical with respect the center of the terrace $(a_{3}/a_{2}=(L+1)/2)$ and that $P(0)=P(L+1)=0$ $[a_{1}=\cosh(a_{3})]$. The former condition is obvious, and the latter derives from the numerical evidence that $P(1)/P[(L+1)/2]$ goes to zero for increasing $L$. Once both conditions have been imposed, we obtain
$$
P(n)=a_{0}\left[\cosh a_{3}-\cosh \left(\frac{2 a_{3} n}{L+1}-a_{3}\right)\right].\qquad(80)
$$

There is only one fit parameter, $a_{3}$, because $a_{0}$ is constrained by the normalization condition for $P(n)$. From a nonlinear curve fitting for relatively small $L$ we can extrapolate that $a_{3}(L)$ tends to a constant value of order 3.11 as $L$ grows. We have, somewhat arbitrarily, set $a_{3}(\infty)$ equal to $\pi$.

### B. The temporal distribution

The results for the temporal distribution of nucleation events $Q(t)$ show in all cases a slow decay for short times (as a power law in $d=1$, logarithmic in $d=2$) followed by an exponential decrease for larger times. This behavior has been obtained by solving exactly, analytically or numerically, the evolution equation for the particles on the terrace. Its physical meaning is clarified further by rederiving these results by means of more transparent but less rigorous arguments: the decay for short times is interpreted in terms of first passage properties of random walks in an unbounded space; the long time decay is the combined effect of the exponentially decreasing probability that both particles are still on the terrace at time $t$ and the probability that they have not yet met.

Let us first discuss the behavior at short times and consider the relative coordinate of the two particles as the coordinate of a fictitious particle $C$: nucleation occurs when $C$ reaches the origin. The initial spatial distribution probability for $C$ $[\rho_{\text{C}}(r)]$ is a function of $\rho_{A}$ and $\rho_{B}$ complicated by the presence of boundaries. However, we are interested in the behavior for short times, i.e., times such that particles are not affected by the presence of terrace edges. Therefore we can assume an initial spatial distribution $\rho_{\text{C}}(r)$ uniform in a region of linear size $L$ around the origin $(\rho_{\text{C}}=1/L^{d})$ and zero outside. The irrelevance of boundaries in the short time regime is confirmed by Figs. 2 and 7: $Q(t)$ has the same behavior, independently of step-edge barriers.

We now define $F(r,t)$ as the first passage probability in $r$ at time $t$ starting from the origin at time zero. The probability that atom $A$, leaving from $r$ at $t=0$ arrives for the first time in the origin at time $t$ is clearly $F(-r,t)$, so that
$$
Q(t)=\sum_{r} \rho_{\text{C}}(r) F(-r,t).\qquad(81)
$$

Let us also define $P(r,t)$ as the probability that a particle is in $r$ at time $t$, being at the origin at time zero. At $t=0$ we have $P(r,0)=\delta_{r,0}$ and $F(r,0)=0$. $P(r,t)$ and $F(r,t)$ are connected by [8]

$$
P(r, t)=\sum_{\tau=0}^{t} F(r, \tau) P(0, t-\tau). \qquad (82)
$$

We write Eq. (82) for spatial argument $-r$, multiply both sides by $\rho_{\mathrm{C}}(r)$,
$$
\rho_{\mathrm{C}}(r) P(-r, t)=\sum_{\tau=0}^{t} \rho_{\mathrm{C}}(r) F(-r, \tau) P(0, t-\tau) \quad (83)
$$
and sum over $r$,
$$
\sum_{r} \rho_{\mathrm{C}}(r) P(-r, t)=\sum_{\tau=0}^{t} Q(\tau) P(0, t-\tau). \qquad (84)
$$

At short times $P(r, t)$ is negligible in the region where $\rho_{\mathrm{C}}(r)$ vanishes. Therefore we can take $\rho_{\mathrm{C}}$ out of the summation and use the normalization of $P(-r, t)$, obtaining
$$
\frac{1}{L^{d}}=\sum_{\tau=0}^{t} Q(\tau) P(0, t-\tau). \qquad (85)
$$

In $d=1$, we pass to the continuum in time $[P(0, t-\tau)$ $=1 /(t-\tau)^{1 / 2}]$,
$$
\frac{1}{L}=\int_{0}^{t} d \tau \frac{Q(\tau)}{(t-\tau)^{1 / 2}} \qquad (86)
$$
and setting $\tau=t s$, we obtain
$$
\frac{1}{L}=t^{1 / 2} \int_{0}^{1} d s \frac{Q(t s)}{(1-s)^{1 / 2}}, \qquad (87)
$$
which implies $Q(t) \sim t^{-1 / 2}$.

In two dimensions we separate the term $\tau=t$ in Eq. (85),
$$
\frac{1}{L^{2}}=\int_{0}^{t-1} d \tau \frac{Q(\tau)}{t-\tau}+Q(t) \qquad (88)
$$

$$
=\int_{0}^{1-1 / t} d s \frac{Q(t s)}{1-s}+Q(t) \qquad (89)
$$

$$
\simeq Q(t) \int_{0}^{1-1 / t} \frac{d s}{1-s}+Q(t) \qquad (90)
$$

$$
\simeq Q(t)[1+\ln t] \qquad (91)
$$
and we obtain $Q(t) \sim 1 /(1+\ln t)$.

In conclusion, at short times $Q(t)$ decays as a power law $[Q(t) \sim 1 / \sqrt{t}]$ in $d=1$ and logarithmically $[Q(t)$ $\sim 1 / \ln (t / t_{0})]$ in $d=2$.

Let us consider now the behavior for long times. The probability that a single adatom remains on the terrace up to time $t$ is (see Ref. [1]) $S(t) \sim \exp (-\alpha_{S} t)$. In $d=1$ one has $\alpha_{S}=\frac{1}{2}[\pi /(L+1)]^{2}$ for zero barriers and $\alpha_{S}=0$ for infinite barriers. It is better to introduce a continuous time notation.
The time step for a single particle is $\Delta t=1 /(2 d D)$, while for two particles diffusing on the same terrace it is $\Delta t$ $=1 /(4 d D)$, so that
$$
S(t) \sim \exp \left(-2 \alpha_{S} d D t\right). \qquad (92)
$$

The probability that two adatoms will meet at time $t$ decays as
$$
Q(t) \sim \exp \left(-4 \alpha_{Q} d D t\right). \qquad (93)
$$

In Sec. III we determined that for noninteracting particles $\alpha_{Q}=\frac{1}{2}[\pi /(L+1)]^{2}$ for zero barriers and $\alpha_{Q}=0$ for infinite barriers, while for interacting particles $\alpha_{Q}=\frac{5}{4}(\pi /(L+1))^{2}$ for zero barriers and $\alpha_{Q}=\frac{1}{4}(\pi / L)^{2}$ for infinite barriers.

All these findings are simply rationalized by the following argument. We define $G(t)$ as the probability that two ada toms confined on the terrace will meet for the first time at time $t$: it is therefore equal to $Q(t)$ in the limit of infinite barriers. For long times,
$$
G(t) \sim \exp \left(-4 \alpha_{G} d D t\right). \qquad (94)
$$

We claim that, for interacting adatoms, $Q(t)$ is given by the probability that each of the two adatoms is still on the terrace times the probability that they meet for the first time at time $t$,
$$
Q(t) \sim S^{2}(t) G(t) \quad \Rightarrow \quad \alpha_{Q}=\alpha_{S}+\alpha_{G}. \qquad (95)
$$

In the noninteracting case, clearly $G(t)$ does not play any role. Then
$$
Q(t) \sim S^{2}(t) \quad \Rightarrow \quad \alpha_{Q}=\alpha_{S}. \qquad (96)
$$

If we neglect the differences between $L$ and $L+1$ at the denominators of $\alpha_{Q}$, the relations (95) and (96) are both verified in the limits $\ell_{\mathrm{ES}}=0$ and $\ell_{\mathrm{ES}}=\infty$.

In $d=2$ the value of $\alpha_{Q}$ is not known analytically. However, relations (95) and (96) have been verified numerically.

### C. The nucleation rate

In this paper we have computed exactly the scaling of the nucleation rate in all regimes, in $d=1$ and $d=2$, for both the noninteracting (mean-field) and the interacting case. The results confirm those of Ref. [1], where the rigorous calcula tion of $W$ was lacking. Mean-field theory overestimates the nucleation rate by a factor that scales, in regime (i) (zero or weak barriers), as $L$ in $d=1$ and $\ln L$ in $d=2$. In the limit of strong barriers [regime (ii)] the error scales as $\ell_{\mathrm{ES}}$ in $d=1$ and as $\ell_{\mathrm{ES}} / L$ in $d=2$. Notice that the latter is a large quan tity, since in this regime $\ell_{\mathrm{ES}} \gg L$. For infinite barriers [regime (iii)] the mean-field picture trivially breaks down. Hence mean-field theory is generally strongly inaccurate, except in two dimensions for weak barriers; however, even in this case logarithmic corrections render $\omega_{\mathrm{MF}}$ not completely reliable.

Our treatment allows the evaluation not only of exponents, but also of prefactors. In particular, this is performed analytically for zero or strong barriers in $d=1$ [Eqs. (43) and (60)] and for strong barriers in $d=2$ [Eq. (77)], while for
031606-12

<table>
<caption>Table I. Value of the nucleation rate $\omega$, including the correct prefactors. In regime (iii) of infinite barriers, $\omega=(FL^d)^{-1}$.</caption>
<tbody><tr><td></td><td>$d=1$</td><td>$d=2$</td></tr>
<tr><td>Weak barriers</td><td rowspan="2">$\omega\approx0.4\frac{F^2L^4}{D}$</td><td rowspan="2">$\omega\approx0.008\frac{F^2L^6}{D\ln(L/1.3)}$</td></tr>
<tr><td>[regime (i)]</td></tr>
<tr><td>Strong barriers</td><td rowspan="2">$\omega=\frac{1}{2}\frac{F^2L^3\ell_{\text{ES}}}{D}$</td><td rowspan="2">$\omega=\frac{1}{4}\frac{F^2L^5\ell_{\text{ES}}}{D}$</td></tr>
<tr><td>[regime (ii)]</td></tr>
</tbody></table>

$d=2$ and no barriers we have evaluated the prefactor numerically. For reference, we report in Table I the value of the nucleation rate in the different cases.

Finally, we want to remark that in $d=1$ for zero barriers, not only the asymptotic behavior for large $L$, but also the exact value of $\omega$ for any $L$ can be determined analytically. One just needs to perform the sum of $L^2$ terms [Eq. (42)].

## VI. CONCLUSIONS
In this paper and in the preceding one [1] we have presented a rather complete study of the problem of irreversible dimer nucleation on top of terraces during epitaxial growth. We have analyzed in detail the mean-field approach to this problem, identified its weaknesses and provided a physical interpretation for them. Then we have solved the problem, by analytical means or (when needed) numerically. In this way we have derived exact results for the spatial and temporal distributions of nucleation events and for the total nucleation rate.

We believe that these results provide a relevant contribution to the investigation of crystal growth from both the experimental and the theoretical point of view.

The dependence of the nucleation rate $\omega$ on the terrace size $L$ and the ES length $\ell_{\text{ES}}$ is a crucial piece of information for the interpretation of experimental results, for example, the evaluation of the Ehrlich-Schwoebel barrier. The mean-field approximation has been widely used so far: as already pointed out [9], this introduces a systematic underestimate of the strength of the ES barrier. The exact expressions for $\omega$, derived in this work, must replace the MF approximate formulas for a correct interpretation of experimental data.

From the theoretical point of view, also the spatial distribution plays an important role. Sometimes, "mesoscopic" models are used to describe the growth process in the submonolayer regime [10] or in the multilayer regime [11]. The rule for dimer formation must be supplemented with the spatial distribution $P(n)$ of nucleation sites: as we have argued, if additional step-edge barriers are not negligible, exact results are completely different from mean-field predictions.

Let us finally mention some possible extensions of the present work. In this paper and in the preceding one [1], we have discussed irreversible nucleation on top of compact terraces: it is therefore natural to wonder what occurs if these hypotheses are relaxed.

The possibility of dimer dissociation introduces new time scales: the average lifetimes of all unstable $j$ clusters $(2\leqslant j\leqslant i^*+1)$. Within the framework presented in this paper, this problem is mapped into the random walk of a particle in a suitable high-dimensional space with, in general, a spatially varying diffusion coefficient. This inhomogeneity reflects the fact that unstable $j$ clusters diffuse and break up with rates different from the single adatom diffusion coefficient. In many cases the full solution is therefore beyond reach, even numerically (unless $i^*$ and $L$ are very small).

However, in the simplest cases, our approach may still be fruitful. Let us consider for example $i^*=2$ and $d=1$: three particles must meet (in the same lattice site) in order to nucleate a stable trimer. When two particles meet they form a dimer that dissociates after a typical time $\tau_{dis}$. If $\tau_{dis}$ is much smaller than all other time scales, two adatoms diffuse as if they were noninteracting, the $3d$ walker diffuses isotropically and we must just consider its irreversible passage along the diagonal $(x_1=x_2=x_3)$. The same applies for generic $d$ and $i^*$ as long as dissociation times of unstable clusters are small. This case is also of interest to test recent scaling approaches [12] valid in the same limit $(\tau_{dis}\to0)$.

The second natural extension of the present work consists in considering nucleation on top of fractal islands instead of compact ones. The framework of our method remains unchanged.

A further extension is to take into account the possibility of reevaporation of deposited particles.

*Note added in proof.* We have recently [13] extended the model, discussed in this and in the preceding paper, to take into account the nonuniformity of the Ehrlich-Schwoebel barrier at the step edge, because of the existence of kinks, and the nonuniformity of the incoming flux, because of steering effects.

## APPENDIX: ASYMPTOTIC BEHAVIORS OF THE TEMPORAL DISTRIBUTION IN $d=1$
In this Appendix we present some detailed results for the one-dimensional case with zero ES barriers and both adatoms having a uniform initial distribution. This is, of course, not physically sensible, since the effective initial distribution of the second adatom has a parabolic form for $\ell_{\text{ES}}=0$. However, contrary to the physically sensible case, the evaluation of the coefficients $B_{kj}^{<}$ is not difficult and this allows an explicit analytic evaluation of the behavior of $Q(t)$, which will differ from the realistic one only in the prefactors.

A simple, although lengthy, evaluation of the coefficients leads to
$$
B_{kj}^{<}=\frac{2}{(L+1)^2L^2}\left[\cot\left(\frac{1}{2}\frac{k\pi}{L+1}\right)S_1-\operatorname{cosec}\left(\frac{1}{2}\frac{k\pi}{L+1}\right)S_2\right],
\tag{A1}
$$
where
$$
S_1=\sin\left(\frac{L}{2}\frac{j\pi}{L+1}\right)\sin\left(\frac{j\pi}{2}\right)\operatorname{cosec}\left(\frac{1}{2}\frac{j\pi}{L+1}\right)
\tag{A2}
$$
and

$$
\begin{aligned}
S_{2}= & \frac{1}{2} \sin \left[-\frac{1}{2} \frac{k \pi}{L+1}+\frac{(j+k) \pi}{2}\right] \sin \left[\frac{L(j+k) \pi}{2(L+1)}\right] \operatorname{cosec}\left[\frac{j+k}{2} \frac{\pi}{L+1}\right]+\frac{1}{2} \sin \left[\frac{1}{2} \frac{k \pi}{L+1}+\frac{(j-k) \pi}{2}\right] \\
& \times \sin \left[\frac{L(j-k) \pi}{2(L+1)}\right] \operatorname{cosec}\left[\frac{j-k}{2} \frac{\pi}{L+1}\right].
\end{aligned}
\tag{A3}
$$

We now want to calculate the temporal distribution
$$
\begin{aligned}
Q(t+1>0) & =\sum_{n=1}^{L} \tilde{p}_{n-1, n}(t) & & \text { (A4) } \\
& =\sum_{k, j=1}^{L} B_{k j} C_{k j}\left\{\frac{1}{2}\left[\cos \left(\frac{k \pi}{L+1}\right)\right.\right. & & \\
& \left.\left.+\cos \left(\frac{j \pi}{L+1}\right)\right]\right\}^{t}, & & \text { (A5) }
\end{aligned}
$$
where the coefficients $C_{k j}$ are given in Eq. (38).

In the limit of large $L$, the coefficients $C_{k j}$ are nonvanishing only for odd $j-k$ (except for $k=j$, but $B_{k k}=0$ ) and their value is
$$
C_{k j}=-k\left(\frac{1}{j-k}+\frac{1}{j+k}\right)=\frac{2 k j}{k^{2}-j^{2}}. \tag{A6}
$$

In the same limit
$$
S_{1}=\frac{2 L}{j \pi} \sin ^{2} \frac{j \pi}{2}, \tag{A7}
$$

$$
S_{2}=\frac{L}{\pi} \frac{2 j}{j^{2}-k^{2}}. \tag{A8}
$$

Therefore,
$$
B_{k j}^{<}=\frac{8}{L^{2} k \pi^{2}}\left[\frac{1}{j} \sin ^{2} \frac{j \pi}{2}-\frac{j}{j^{2}-k^{2}}\right], \tag{A9}
$$
and after some algebra
$$
B_{k j}=\frac{8}{\pi^{2} L^{2}} \frac{1}{j k}\left[(-1)^{k}+\frac{k^{2}+j^{2}}{k^{2}-j^{2}}\right] \tag{A10}
$$
and
$$
B_{k j} C_{k j}=\frac{16}{\pi^{2} L^{2}}\left[\frac{(-1)^{k}}{k^{2}-j^{2}}+\frac{k^{2}+j^{2}}{\left(k^{2}-j^{2}\right)^{2}}\right]. \tag{A11}
$$

The dominant contribution to $Q(t)$ comes from $j=k-1$ or $j=k+1$,
$$
B_{k, k \pm 1} C_{k, k \pm 1}=\frac{16}{\pi^{2} L^{2}}\left[\frac{(-1)^{k}}{\mp 2 k-1}+\frac{2 k^{2} \pm 2 k+1}{(\mp 2 k-1)^{2}}\right]. \tag{A12}
$$

Hence
$$
\begin{aligned}
Q(t) \simeq & \frac{16}{\pi^{2} L^{2}}\left\{\sum_{k=1}^{L-1}\left[\frac{(-1)^{k}}{-2 k-1}+\frac{2 k^{2}+2 k+1}{(-2 k-1)^{2}}\right] \exp \left[-\frac{t}{4}\left(\frac{\pi}{L+1}\right)^{2}\left(2 k^{2}+2 k+1\right)\right]+\sum_{k=2}^{L}\left[\frac{(-1)^{k}}{2 k-1}+\frac{2 k^{2}-2 k+1}{(2 k-1)^{2}}\right]\right. \\
& \left.\times \exp \left[-\frac{t}{4}\left(\frac{\pi}{L+1}\right)^{2}\left(2 k^{2}-2 k+1\right)\right]\right\}.
\end{aligned}
\tag{A13}
$$

We neglect the first term in both sums and approximate the sums according to the Euler-Maclaurin formula:
$$
\sum_{k=1}^{L} f_{k}=\int_{1}^{L} d k f(k)+\frac{1}{2}\left[f_{1}+f_{L}\right]. \tag{A14}
$$

Since in this case $f_{L} \ll f_{1}$, we neglect $f_{L}$,
$$
\begin{aligned}
Q(t) \simeq & \frac{16}{\pi^{2} L^{2}}\left\{\int_{1}^{L-1} d k \frac{2 k^{2}+2 k+1}{(-2 k-1)^{2}} \exp \left[-\frac{t}{4}\left(\frac{\pi}{L+1}\right)^{2}\left(2 k^{2}+2 k+1\right)\right]+\frac{5}{9} \exp \left[-\frac{5 t}{4}\left(\frac{\pi}{L+1}\right)^{2}\right]+\int_{2}^{L} d k \frac{2 k^{2}-2 k+1}{(2 k-1)^{2}}\right. \\
& \left.\times \exp \left[-\frac{t}{4}\left(\frac{\pi}{L+1}\right)^{2}\left(2 k^{2}-2 k+1\right)\right]\right\}.
\end{aligned}
\tag{A15}
$$

The integrals can be evaluated by considering for the integrand the limit for large $k$, and one obtains

$$
\begin{aligned}
Q(t) \simeq & \frac{8}{\pi^{2} L^{2}} \frac{L}{\pi \sqrt{t / 2}}\left[\int_{\pi \sqrt{t / 2} / L}^{\pi \sqrt{t / 2}} d x e^{-x^{2}}+\int_{2 \pi \sqrt{t / 2} / L}^{\pi \sqrt{t / 2}} d x e^{-x^{2}}\right] \\
& +\frac{80}{9 \pi^{2} L^{2}} \exp \left[-\frac{5 t}{4}\left(\frac{\pi}{L+1}\right)^{2}\right].
\end{aligned}
\tag{A16}
$$

The upper limit of the integrals can be shifted to $\infty$,

$$
\begin{aligned}
Q(t) \simeq & \frac{8}{\pi^{3} L \sqrt{t / 2}}\left[\int_{\pi \sqrt{t / 2} / L}^{\infty} d x e^{-x^{2}}+\int_{2 \pi \sqrt{t / 2} / L}^{\infty} d x e^{-x^{2}}\right] \\
& +\frac{80}{9 \pi^{2} L^{2}} \exp \left[-\frac{5 t}{4}\left(\frac{\pi}{L+1}\right)^{2}\right].
\end{aligned}
\tag{A17}
$$

If $t \ll (2L^2/\pi^2)$ each integral goes to $\sqrt{\pi}/2$ and the first term prevails on the exponential; in the limit $t \gg (2L^2/\pi^2)$ the opposite is true. So, $Q(t) \simeq 8/(L\pi^{5/2}\sqrt{t/2})$ for $t \ll (2L^2/\pi^2)$ and $Q(t) \simeq 80/9\pi^2L^2\exp(-5t/4[\pi/(L+1)]^2)$ for $t \gg (2L^2/\pi^2)$.

By summing $Q(t)$ over $t$ one obtains $W$.

$$
\begin{aligned}
W & \simeq \int_{0}^{2 L^{2} / \pi^{2}} d t Q(t)=\int_{0}^{2 L^{2} / \pi^{2}} d t \frac{8}{L \pi^{5 / 2} \sqrt{t / 2}} \\
& \simeq \frac{32}{\pi^{7 / 2}} \simeq 0.58 \ldots
\end{aligned}
\tag{A18}
$$

[1] P. Politi and C. Castellano, preceding paper, Phys. Rev. E $\textbf{66}$, 031605 (2002).

[2] J.A. Venables, Phys. Rev. B $\textbf{36}$, 4153 (1987); J.A. Venables, G.D.T. Spiller, and M. Hanbücken, Rep. Prog. Phys. $\textbf{47}$, 399 (1984).

[3] J. Tersoff, A.W. Denier van der Gon, and R.M. Tromp, Phys. Rev. Lett. $\textbf{72}$, 266 (1994).

[4] C. Castellano and P. Politi, Phys. Rev. Lett. $\textbf{87}$, 056102 (2001).

[5] G. Ehrlich and F.G. Hudda, J. Chem. Phys. $\textbf{44}$, 1039 (1966); R.L. Schwoebel and E.J. Shipsey, J. Appl. Phys. $\textbf{37}$, 3682 (1966); R.L. Schwoebel, ibid. $\textbf{40}$, 614 (1969); K. Kyuno and G. Ehrlich, Surf. Sci. $\textbf{383}$, L766 (1997).

[6] S. Redner, *A Guide to First-Passage Processes* (Cambridge University Press, Cambridge, 2001).

[7] We are not aware of previously published solutions of the present problem. The most similar one we have found in literature is the problem of two interacting particles moving in one dimension with one absorbing boundary. See M.E. Fisher, J. Stat. Phys. $\textbf{34}$, 667 (1984).

[8] B.D. Hughes, *Random Walks and Random Environments* (Clarendon Press, Oxford, 1995).

[9] J. Krug, P. Politi, and T. Michely, Phys. Rev. B $\textbf{61}$, 14037 (2000).

[10] C. Ratsch, M.F. Gyure, S. Chen, M. Kang, and D.D. Vvedensky, Phys. Rev. B $\textbf{61}$, R10 598 (2000).

[11] I. Elkinani and J. Villain, J. Phys. $\textbf{I 4}$, 949 (1994); P. Politi and J. Villain, Phys. Rev. B $\textbf{54}$, 5114 (1996).

[12] S. Heinrichs, J. Rottler, and P. Maass, Phys. Rev. B $\textbf{62}$, 8338 (2000); J. Krug, Eur. Phys. J. B $\textbf{18}$, 713 (2000).

[13] P. Politi and C. Castellano (unpublished).