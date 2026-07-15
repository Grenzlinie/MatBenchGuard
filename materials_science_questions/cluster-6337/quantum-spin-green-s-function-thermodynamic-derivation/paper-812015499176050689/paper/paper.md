Journal of Statistical Physics, Vol. 127, No. 2, April 2007 (© 2007)
DOI: 10.1007/s10955-006-9213-9

# $Q$-Dependent Susceptibilities in Ferromagnetic Quasiperiodic $Z$-Invariant Ising Models

Helen Au-Yang $^{1,2}$ and Jacques H.H. Perk $^{1,2}$

Received September 17, 2004; accepted May 19, 2006
Published Online: February 10, 2007

We study the $q$-dependent susceptibility $\chi(\mathbf{q})$ of a series of quasiperiodic Ising models on the square lattice. Several different kinds of aperiodic sequences of couplings are studied, including the Fibonacci and silver-mean sequences. Some identities and theorems are generalized and simpler derivations are presented. We find that the $q$-dependent susceptibilities are periodic, with the commensurate peaks of $\chi(\mathbf{q})$ located at the same positions as for the regular Ising models. Hence, incommensurate everywhere-dense peaks can only occur in cases with mixed ferromagnetic–antiferromagnetic interactions or if the underlying lattice is aperiodic. For mixed-interaction models the positions of the peaks depend strongly on the aperiodic sequence chosen.

**KEY WORDS:** Ising model, $Z$-invariance, quasiperiodicity, golden ratio, silver mean, correlation functions, wavevector-dependent susceptibility.

## 1. INTRODUCTION

In our most recent paper, $^{(1)}$ we have studied the $q$-dependent susceptibility $\chi(\mathbf{q})$ for a $Z$-invariant ferromagnetic Ising model on Penrose tiles. (The $\chi(\mathbf{q})$ is in many ways equivalent to the structure function determining diffraction patterns.) We have found that $\chi(\mathbf{q})$ is aperiodic and has incommensurate peaks which are everywhere dense, though only a limited number of them are visible at temperatures far away from the critical temperature. This is very different from the behavior of $\chi(\mathbf{q})$ in Fibonacci Ising models defined on regular lattices, $^{(2,3)}$ where $\chi(\mathbf{q})$ is periodic and has only commensurate peaks located at the same positions as for the regular Ising models when the couplings between the spins are ferromagnetic.

---
$^{1}$ Department of Physics, Oklahoma State University, Stillwater, OK 74078-3072, USA.
$^{2}$ Supported in part by NSF Grant No. PHY 01-00; e-mail: jhhp@jperk.phy.obstate.edu.

265
0022-4715/07/0400-0265/0 © 2007 Springer Science+Business Media, LLC

The periodicity of $\chi(\mathbf{q})$, when the lattice is regular, is due to the fact that we may write

$$
k_{\mathrm{B}} T \chi\left(q_{x}, q_{y}\right)=\sum_{l, m} \mathrm{e}^{\mathrm{i}\left(q_{x} l+q_{y} m\right)} C(l, m) \tag{1.1}
$$

where the average of the connected correlation function for two spins with fixed separations $(l, m)$ is

$$
C(l, m)=\lim _{\mathcal{L} \rightarrow \infty} \frac{1}{\mathcal{L}^{2}} \sum_{l^{\prime}, m^{\prime}}\left[\left\langle\sigma_{l^{\prime}, m^{\prime}} \sigma_{l^{\prime}+l, m^{\prime}+m}\right\rangle-\left\langle\sigma_{l^{\prime}, m^{\prime}}\right\rangle\left\langle\sigma_{l^{\prime}+l, m^{\prime}+m}\right\rangle\right]. \tag{1.2}
$$

in which $\mathcal{L}$ denotes the number of rows and columns in the lattice, so that $\mathcal{L}^{2}$ is the total number of spins. Since $l$ and $m$ are integers, it is easily seen from (1.1) that the $q$-dependent susceptibilities for such cases are periodic with periods $2 \pi$ in $q_{x}$ and $q_{y}$. When the lattice structure is quasi-periodic, as in the case of the Penrose tiles studied in our previous paper, $^{(1)}$ it is not possible to split the summation in the susceptibility in this way and $\chi(\mathbf{q})$ is no longer periodic.

In this paper, we want to examine the $q$-dependent susceptibility of some other aperiodic ferromagnetic Ising models defined on regular lattices, to find out if the Fibonacci Ising models are different from other more general aperiodic models.

To be more specific, we consider the $Z$-invariant inhomogeneous Ising model $^{(2-6)}$ defined on a rectangular lattice as shown in Fig. 1, and let either one of the sequences of rapidities, $(u_{n})_{n \in \mathbb{Z}}$ or $(v_{m})_{m \in \mathbb{Z}}$ or both, be certain aperiodic sequences. In doing so, we shall derive a number of properties for these sequences which are part of the main results of this paper.

As before, the edge interactions are parametrized by (see Fig. 2)

$$
\begin{aligned}
& \sinh \left(2 K\left(u_{i}, v_{j}\right)\right)=k \operatorname{sc}\left(u_{i}-v_{j}, k^{\prime}\right)=\operatorname{cs}\left(\lambda+v_{j}-u_{i}, k^{\prime}\right), \\
& \sinh \left(2 \bar{K}\left(u_{i}, v_{j}\right)\right)=\operatorname{cs}\left(u_{i}-v_{j}, k^{\prime}\right)=k \operatorname{sc}\left(\lambda+v_{j}-u_{i}, k^{\prime}\right),
\end{aligned} \tag{1.3}
$$

where $\lambda \equiv K(k^{\prime})$ is the complete elliptic integral of the first kind, $k$ and $k^{\prime}=$ $\sqrt{1-k^{2}}$ are the elliptic moduli, which are temperature variables, and they are the same for all couplings.

## 2. QUASI-PERIODIC SEQUENCES

Quasi-periodic sequences were first used—within the related context of the study of the specific heat of layered Ising models—by Tracy. $^{(7,8)}$ Even though the particular sequences used by Tracy $^{(8)}$ may all be interesting, for some technical reasons we shall consider here only the aperiodic sequences which were studied

![](./images/812015499176050689_1.jpg)

Fig. 1. The lattice of a two-dimensional $Z$-invariant Ising model: The rapidity lines on the medial graph are represented by oriented dashed lines. The positions of the spins are indicated by small black circles, the positions of two of the dual spins by white circles.

by de Bruijn. $^{(9)}$ Let

$$
\alpha_{j} \equiv \frac{1}{2}\left[(j+1)+\sqrt{(j+1)^{2}+4}\right], \quad \text { for } j=0,1,2, \ldots,\tag{2.4}
$$

such that $\alpha_{0}=(1+\sqrt{5}) / 2$ is the golden ratio and $\alpha_{1}=1+\sqrt{2}$ is the silver mean.
Define for each $j$ a sequence $(p_{j}(n))_{n \in \mathbb{Z}}$,

$$
p_{j}(n) \equiv\left\lfloor\gamma+(n+1) / \alpha_{j}\right\rfloor-\left\lfloor\gamma+n / \alpha_{j}\right\rfloor,\tag{2.5}
$$

![](./images/812015499176050689_2.jpg)

Fig. 2. (a) Horizontal coupling $K_{i j}=K(u_{i}, v_{j})$; (b) Vertical coupling $\bar{K}_{i j}=\bar{K}(u_{i}, v_{j})$.

where $\lfloor x \rfloor$ is the largest integer $\leq x$, and $\gamma$ is a real number. In this paper, $\gamma$ is chosen such that $\gamma + m/\alpha_j$ does not equal an integer for any $m$. Consequently, the sequence in (2.5) is not changed when the floor ($\lfloor x \rfloor$) in (2.5) is replaced by ceiling or roof ($\lceil x \rceil$: smallest integer $\geq x$). For the silver mean sequence $(p_1(n))_{n \in \mathbb{Z}}$, we choose $\gamma \neq m + l\sqrt{2}$ for all integers $m$ and $l$. More generally, it is sufficient to require that $\gamma$ is not a solution of a quadratic equation with integer coefficients.

It is shown by de Bruijn$^{(9)}$ that the $(p_j(n))_{n \in \mathbb{Z}}$ are sequences of 0's and 1's, which may also be easily shown by rewriting (2.5) as
$$
p_j(n) = \lfloor x_n + 1/\alpha_j \rfloor, \quad x_n = \{\gamma + n/\alpha_j\}, \tag{2.6}
$$
after decomposing $\gamma + n/\alpha_j$ into its integer and fractional parts, i.e.,
$$
\gamma + (n+1)/\alpha_j = \lfloor \gamma + n/\alpha_j \rfloor + \{\gamma + n/\alpha_j\} + 1/\alpha_j, \tag{2.7}
$$
$$
\{x\} \equiv x - \lfloor x \rfloor, \quad 0 \leq \{x\} < 1. \tag{2.8}
$$

Since $\alpha_j > 1$ and therefore $0 \leq x_n + 1/\alpha_j < 2$, it follows that $p_j(n) = 0$ if $0 \leq x_n + 1/\alpha_j < 1$ and $p_j(n) = 1$ if $1 \leq x_n + 1/\alpha_j < 2$. As $j$ increases (and so does $\alpha_j$), the corresponding sequences $(p_j(n))_{n \in \mathbb{Z}}$ contain increasing numbers of zeros. In fact, for fixed $j$, the $p_j$'s can be separated into blocks of $j+1$ digits (a one followed by $j$ zeros) or $j+2$ digits (a one followed by $j+1$ zeros). Furthermore, it is also shown by de Bruijn$^{(9)}$ that the production rule of replacing each 1 in a sequence $p_j$'s by a 1 followed by $j+1$ zeros and replacing each 0 by a 1 followed by $j$ zeros produces a new sequence of $p_j'$'s of the form (2.5) with $\gamma \to \gamma'$ and $\gamma' = -\{\gamma\}/\alpha_j$.

All these sequences are known to be aperiodic. Thus, if we let $u_m = u_\mathrm{A}$ for $p_j(m) = 1$, and $u_m = u_\mathrm{B}$ for $p_j(m) = 0$, then the sequence of line variables or rapidities $(u_m)_{m \in \mathbb{Z}}$ is related to the sequence $(p_j(m))_{m \in \mathbb{Z}}$, and therefore is also quasiperiodic. For $j=0$, the $p_0(m)$'s and the corresponding $u_m$'s are Fibonacci sequences, and this case we have studied earlier.$^{(2,3,7)}$ Likewise, we may also associate a sequence of rapidities $(v_n)_{n \in \mathbb{Z}}$ to the sequence $(p_j(n))_{n \in \mathbb{Z}}$. In this way, we can construct several quasiperiodic $\mathbb{Z}$-invariant Ising models on the square lattice.

In order to calculate the average of the connected correlation functions, $C(l, m)$ given by (1.2), we need to generalize a result of Tracy$^{(7)}$ for Fibonacci sequences. Tracy$^{(8)}$ mentions also some other quasi-periodic sequences, for which—as far as we know—the corresponding theorems are not yet available. But we can generalize his result to general $j>0$ while simplifying his proof at the same time.

Averages: Following Tracy, $^{(7)}$ we let $N(n, m)$ be the number of 1's in the subsequence $p_j(m), \dots, p_j(m+n-1)$ which is also the number of $u_\mathrm{A}$'s in the subsequence $u_m, \dots, u_{m+n-1}$.

Because the only allowed values of $p_j(n)$ are either 1 or 0, the number of 1's among these $n$ consecutive terms of $p_j$'s is

$$
\begin{aligned}
N(n, m) & =\sum_{\ell=0}^{n-1} p_{j}(m+\ell)=\left\lfloor\gamma+(m+n) / \alpha_{j}\right\rfloor-\left\lfloor\gamma+m / \alpha_{j}\right\rfloor \\
& =\left\lfloor x_{m}+n / \alpha_{j}\right\rfloor=\left\lfloor x_{m}+\left\{n / \alpha_{j}\right\}\right\rfloor+\left\lfloor n / \alpha_{j}\right\rfloor,
\end{aligned}\tag{2.9}
$$

where $x_m$ is defined in (2.6) and $0 \leq x_m < 1$. Since $0 \leq x_m + \{n/\alpha_j\} < 2$, we find

$$
N(n, m)= \begin{cases}\left\lfloor n / \alpha_{j}\right\rfloor & \text { for } x_{m}+\left\{n / \alpha_{j}\right\}<1, \\ \left\lfloor n / \alpha_{j}\right\rfloor+1 & \text { for } x_{m}+\left\{n / \alpha_{j}\right\} \geq 1.\end{cases}\tag{2.10}
$$

Noting that $1/\alpha_j$ is irrational, we find from Kronecker's theorem$^{(10)}$ that as $m$ varies from $-\infty$ to $\infty$, the $x_m$'s in (2.6) are distributed everywhere dense and uniformly between 0 and 1. Thus the probability of finding an $x_m$ with $x_m < 1 - \{n/\alpha_j\}$ is $1 - \{n/\alpha_j\}$, whereas the probability of $x_m \geq 1 - \{n/\alpha_j\}$ is $\{n/\alpha_j\}$. Consequently, we have proved the following theorem:

**Theorem 1.** An infinite quasiperiodic sequence $(u_m)_{m \in \mathbb{Z}}$ defined by $u_m = u_\text{A}$ if $p_j(m) = 1$ and $u_m = u_\text{B}$ if $p_j(m) = 0$ with the $p_j$'s given by (2.5) contains blocks of a single $u_\text{A}$ followed by either $j$ or $j+1$ $u_\text{B}$'s. The number of $u_\text{A}$'s among $n$ consecutive $u$'s is either $\left\lfloor n/\alpha_j \right\rfloor$ with probability $1 - \{n/\alpha_j\}$ or $\left\lfloor n/\alpha_j \right\rfloor + 1$ with probability $\{n/\alpha_j\}$.

We have thus generalized the result of Tracy$^{(7)}$ for Fibonacci sequences (with $j=0$) to other cases ($j>0$), while also simplifying the proof.

**Sequences of Three Objects.** Since each $p_j$ sequence is quasiperiodic, if we shift a $p_j$ sequence by a certain number of digits and subtract the shifted sequence from the original one, the resulting sequence is also quasi-periodic, having three different values: 1, 0 and $-1$. Moreover, as a $p_j$ sequence consists of blocks of $j+1$ digits with a one followed by $j$ zeros or blocks of $j+2$ digits with a one followed by $j+1$ zeros, we find for $j \neq 0$ or $\alpha_j \neq (1+\sqrt{5})/2$, that two consecutive terms in the original $p_j$ sequence cannot be simultaneously 1. Consequently, if we let

$$
q_{j}(\ell)=p_{j}(\ell+1)-p_{j}(\ell), \quad \ell \in \mathbb{Z},\tag{2.11}
$$

the average number of 1's (or $-1$'s) among $n$ consecutive numbers can be easily evaluated. In this paper, we restrict ourselves to the sequences (2.11) with $j \geq 1$. Therefore, we work out the needed probabilities next.

As it is indeed impossible to have both $p_j(\ell+1)$ and $p_j(\ell)$ equal to 1, we find $q_j(\ell)=1$ if $p_j(\ell+1)=1$; $q_j(\ell)=-1$ if $p_j(\ell)=1$, and 0 otherwise when $p_j(\ell+1)=p_j(\ell)=0$. Now we let $u_m = u_\text{A}$ if $q_j(m)=1$, $u_m = u_\text{B}$ if $q_j(m)=0$, and $u_m = u_\text{C}$ if $q_j(m)=-1$. Consequently, the sequence of rapidities $u_m$ is related to the sequence $q_j(m)$, and is therefore also quasiperiodic.

Let the number $N_{\mathrm{A}}(n, m), (N_{\mathrm{B}}(n, m)$ or $N_{\mathrm{C}}(n, m))$ denote the number of 1's, (0's or $-1$'s) in the subsequence $q_{j}(m), \ldots, q_{j}(m+n-1)$, which is also the number of $u_{\mathrm{A}},(u_{\mathrm{B}}$ or $u_{\mathrm{C}})$ in the subsequence $u_{m}, \ldots, u_{m+n-1}$. Since the number of 1's in $q_{j}(m), \ldots, q_{j}(m+n-1)$ is equivalent to the number of 1's in $p_{j}(m+1), \ldots, p_{j}(m+n)$, we find

$$
\begin{aligned}
N_{\mathrm{A}}(n, m) & =\left\lfloor\gamma+(n+m+1) / \alpha_{j}\right\rfloor-\left\lfloor\gamma+(m+1) / \alpha_{j}\right\rfloor \\
& =\left\lfloor x_{m+1}+n / \alpha_{j}\right\rfloor \\
& = \begin{cases}\left\lfloor n / \alpha_{j}\right\rfloor & \text { for } x_{m+1}<1-\left\{n / \alpha_{j}\right\}, \\
\left\lfloor n / \alpha_{j}\right\rfloor+1 & \text { for } x_{m+1} \geq 1-\left\{n / \alpha_{j}\right\}.\end{cases}
\end{aligned}
\tag{2.12}
$$

cf. (2.9) and (2.10). Likewise, the number of $-1$'s in the new subsequence $q_{j}(m), \ldots, q_{j}(m+n-1)$ is equivalent to the number of 1's in the original $p_{j}(m), \ldots, p_{j}(m+n-1)$, and we find

$$
\begin{aligned}
N_{\mathrm{C}}(n, m) & =\left\lfloor\gamma+(n+m) / \alpha_{j}\right\rfloor-\left\lfloor\gamma+m / \alpha_{j}\right\rfloor \\
& =\left\lfloor x_{m}+n / \alpha_{j}\right\rfloor \\
& = \begin{cases}\left\lfloor n / \alpha_{j}\right\rfloor & \text { for } x_{m}<1-\left\{n / \alpha_{j}\right\}, \\
\left\lfloor n / \alpha_{j}\right\rfloor+1 & \text { for } x_{m} \geq 1-\left\{n / \alpha_{j}\right\}.\end{cases}
\end{aligned}
\tag{2.13}
$$

Since the total must be $n$, we have

$$
N_{\mathrm{B}}(n, m)=n-N_{\mathrm{A}}(n, m)-N_{\mathrm{C}}(n, m). \tag{2.14}
$$

Using (2.6), we find

$$
x_{m+1}=\left\{x_{m}+1 / \alpha_{j}\right\}= \begin{cases}x_{m}+1 / \alpha_{j} & \text { for } x_{m}+1 / \alpha_{j}<1, \\ x_{m}+1 / \alpha_{j}-1 & \text { for } x_{m}+1 / \alpha_{j} \geq 1.\end{cases} \tag{2.15}
$$

In view of the above, let us write

$$
\begin{aligned}
& N_{\mathrm{A}}(n, m)=\left\lfloor n / \alpha_{j}\right\rfloor+\mu, \quad \text { with } \mu=0 \text { or } 1, \\
& N_{\mathrm{C}}(n, m)=\left\lfloor n / \alpha_{j}\right\rfloor+v, \quad \text { with } v=0 \text { or } 1.
\end{aligned}
\tag{2.16}
$$

Equations (2.12), (2.13), and (2.15) determine the proper choices of $\mu$ and $v$ as functions of $x_{m}$ and $\{n / \alpha_{j}\}$. This is illustrated in Fig. 3 for the case $j=1$; the situation is qualitatively the same for all $j \geq 1$. We remind ourselves that the $x_{m}$ defined in (2.6) is everywhere dense and uniformly distributed in $[0,1)$, as $m$ runs from $-\infty$ to $\infty$. Consequently, the choice $v=0$ is seen from (2.13) and (2.10) to correspond to the segment in $[0,1]$ where the inequality $0 \leq x_{m}<1-\{n / \alpha_{j}\}$ is satisfied, while $v=1$ is given by its complement satisfying $1-\{n / \alpha_{j}\} \leq x_{m}<1$. Using (2.15), we find $0 \leq x_{m+1}<1-\{n / \alpha_{j}\}$ is equivalent to both $1-1 / \alpha_{j} \leq x_{m}<2-\{n / \alpha_{j}\}-1 / \alpha_{j}$ and $0 \leq x_{m}<1-\{n / \alpha_{j}\}-1 / \alpha_{j}$. Since $0 \leq x_{m}<1$, the second inequality cannot be satisfied if $1-\{n / \alpha_{j}\}-1 / \alpha_{j}<0$, which

![](./images/812015499176050689_3.jpg)
![](./images/812015499176050689_4.jpg)
![](./images/812015499176050689_5.jpg)

Fig. 3. The regions of $x_m$ where $N_\text{A}(n,m)=\lfloor n/\alpha_j\rfloor+\mu$ and $N_\text{C}(n,m)=\lfloor n/\alpha_j\rfloor+\nu$ are shown for the silver-mean case $j=1$. The segments where $\mu$ or $\nu=0$ are indicated by thick white strips, while the segments where $\mu$ or $\nu=1$ are indicated by narrow shaded strips. The $\mu$-strips are below and the $\nu$-strips on top.

is the defining condition for Fig. 3(c); here $\mu=0$ is the segment where $1-1/\alpha_j\leq x_m<2-\{n/\alpha_j\}-1/\alpha_j$; its complement $\mu=1$, however, consists of two disjunct segments. Cases with $1-\{n/\alpha_j\}-1/\alpha_j>0$ are shown in Fig. 3(a) and (b); here $\mu=0$ consists of two disjunct segments satisfying $1-1/\alpha_j\leq x_m<1$ or $0\leq x_m<1-\{n/\alpha_j\}-1/\alpha_j$, while its complement $\mu=1$ is now just one segment given by $1-\{n/\alpha_j\}-1/\alpha_j\leq x_m<1-1/\alpha_j$.

Let $P(\mu',\nu')$, for $\mu',\nu'=0,1$, denote the joint probability for having both $N_\text{A}(n,m)=\lfloor n/\alpha_j\rfloor+\mu'$ and $N_\text{C}(n,m)=\lfloor n/\alpha_j\rfloor+\nu'$. Then $P(\mu',\nu')$ is the total length of the intersection of the segment or segments where $\mu=\mu'$ with the segment where $\nu=\nu'$. The results are different for the three different regions of $\{n/\alpha_j\}$. We find

$$
\left.
\begin{aligned}
P(0,0)&=1-2\{n/\alpha_j\} \\
P(1,0)&=P(0,1)=\{n/\alpha_j\} \\
P(1,1)&=0
\end{aligned}
\right\} \quad \text{if } \{n/\alpha_j\}\leq1/\alpha_j, \tag{2.17}
$$

$$
\left.
\begin{aligned}
P(0,0)&=1-\{n/\alpha_j\}-1/\alpha_j \\
P(1,0)&=P(0,1)=1/\alpha_j \\
P(1,1)&=\{n/\alpha_j\}-1/\alpha_j
\end{aligned}
\right\} \quad \text{if } 1/\alpha_j\leq\{n/\alpha_j\}\leq1-1/\alpha_j, \tag{2.18}
$$

$$
\left.
\begin{aligned}
P(0,0)&=0 \\
P(1,0)&=P(0,1)=1-\{n/\alpha_j\} \\
P(1,1)&=2\{n/\alpha_j\}-1
\end{aligned}
\right\} \quad \text{if } \{n/\alpha_j\}\geq1-1/\alpha_j. \tag{2.19}
$$

Remark. Both Theorem 1 for the two-object case and Eqs. (2.17) through (2.19) for the three-object case have a reflection symmetry under the formal replacement $n\to-n$, $(n>0)$. Since $\alpha_j$ is irrational, this means we have to replace $\{n/\alpha_j\}\to\{-n/\alpha_j\}=1-\{n/\alpha_j\}$, so that $P(\mu,\nu)\to P(1-\mu,1-\nu)$. Also, $-\lfloor-n/\alpha_j\rfloor=\lceil n/\alpha_j\rceil=\lfloor n/\alpha_j\rfloor+1$, and (2.17) is to be replaced by $N_\text{A}(-n,m)=\lfloor n/\alpha_j\rfloor+1-\mu$, $N_\text{C}(-n,m)=$

$\lfloor n/\alpha_j \rfloor +1 - \nu$. Therefore, we indeed have that the probability distribution is invariant under reflections. It is also translationally invariant, as (2.17)-(2.19) are independent of $m$.

## 3. CORRELATIONS

The spin-spin correlation function in the inhomogeneous $Z$-invariant Ising model has been shown by Baxter $^{(4)}$ to depend only on the elliptic modulus $k$ and the rapidity variables, $u$'s and $v$'s, of rapidity lines that are sandwiched between the two spins. Particularly, for $-l \leq m \leq l$, when the arrows of all these relevant rapidity lines are pointing to the same side of the line joining the two spins (see Fig. 1), we have-according to the rule in Ref. 5 -the result

$$
\left\langle\sigma_{j, k} \sigma_{j+l, k+m}\right\rangle=g_{2 l}\left(u_{j-k+1}, \ldots, u_{l-m+j-k}, v_{j+k}, \ldots, v_{l+m+j+k-1}\right), \quad(3.20)
$$

$$
\left\langle\mu_{j, k} \mu_{j+l, k+m}\right\rangle=g_{2 l}^{*}\left(u_{j-k+1}, \ldots, u_{l-m+j-k}, v_{j+k+1}, \ldots, v_{l+m+j+k}\right), \quad(3.21)
$$

while for $-m \leq l \leq m$, when the arrows of the vertical rapidity lines and the arrows of the horizontal rapidity lines are pointing to opposite sides of the joining line, we find

$$
\begin{aligned}
& \left\langle\sigma_{j, k} \sigma_{j+l, k+m}\right\rangle \\
& \quad=g_{2 m}\left(u_{j-k+l-m+1}, \ldots, u_{j-k}, \lambda+v_{j+k}, \ldots, \lambda+v_{l+m+j+k-1}\right), \quad(3.22)
\end{aligned}
$$

$$
\begin{aligned}
& \left\langle\mu_{j, k} \mu_{j+l, k+m}\right\rangle \\
& \quad=g_{2 m}^{*}\left(u_{j-k+l-m+1}, \ldots, u_{j-k}, \lambda+v_{j+k+1} \ldots, \lambda+v_{l+m+j+k}\right), \quad(3.23)
\end{aligned}
$$

Here $\lambda \equiv \mathrm{K}\left(k^{\prime}\right)$ is a complete elliptic integral of the first kind. Note that the explicit dependence of $\lambda, g$ and $g^{*}$ on the elliptic modulus $k$ is dropped, but it should still be understood to be implicitly present. Also, the $\mu \equiv \sigma^{*}$ stand for dual spins on the dual lattice, which is at the dual temperature.

As pointed out first by Baxter, $^{(4)}$ the universal functions $g_{2 l}$ and $g_{2 l}^{*}$ have "permutation symmetry" (meaning they are invariant under all permutations of the rapidities) and the "difference property" (which implies a translation invariance when shifting all the rapidities by the same amount $v^{(0)}$ ). The functions $g_{2 l}$ and $g_{2 l}^{*}$ for $l>1$ can be obtained iteratively. $^{(2,3,5)}$ The final technical point is to explain how the averaging in (1.2) is done.

### 3.1. Averaging

In this paper, we shall consider quasiperiodic sequences which are either sequences of two objects:
$$
u_{m}= \begin{cases}u_{\mathrm{A}} & \text { if } p_{j}(m)=1, \\ u_{\mathrm{B}} & \text { if } p_{j}(m)=0,\end{cases} \quad v_{m}= \begin{cases}v_{\mathrm{A}} & \text { if } p_{j}(m)=1, \\ v_{\mathrm{B}} & \text { if } p_{j}(m)=0,\end{cases}\quad (3.24)
$$
for fixed $j \geq 0$, or sequences of three objects:
$$
u_{m}= \begin{cases}u_{\mathrm{A}} & \text { if } q_{j}(m)=1, \\ u_{\mathrm{B}} & \text { if } q_{j}(m)=0, \\ u_{\mathrm{C}} & \text { if } q_{j}(m)=-1,\end{cases} \quad v_{m}=v, \quad j \geq 1.\quad (3.25)
$$

To evaluate $C(l, m)$ and $C^{*}(l, m)$ for $|m| \leq l$, we use (3.20) and (3.21). It is easily seen from these equations that there are $l - m$ horizontal rapidity lines $u$ and $l + m$ vertical lines $v$ sandwiched between the two spins.

For the two-object sequences in (3.24), we find from Theorem 1 that the number of $u_{\mathrm{A}}$'s among the $l - m$ consecutive $u$'s is either $\lfloor s\rfloor$ with probability $1 - \{s\}$ or $\lfloor s\rfloor + 1$ with probability $\{s\}$ where $s=(l - m)/\alpha_{j}$, while the number of $v_{\mathrm{A}}$'s among the $l + m$ consecutive $v$'s is either $\lfloor r\rfloor$ with probability $1 - \{r\}$ or $\lfloor r\rfloor + 1$ with probability $\{r\}$ in which $r=(l + m)/\alpha_{j}$. Consequently, the averaged connected correlation function in (1.2) for $|m| \leq l$ becomes
$$
\begin{aligned}
C(l, m)= & (1-\{s\})(1-\{r\}) \bar{g}[\lfloor s\rfloor, l-m-\lfloor s\rfloor,\lfloor r\rfloor, l+m-\lfloor r\rfloor] \\
& +(1-\{s\})\{r\} \bar{g}[\lfloor s\rfloor, l-m-\lfloor s\rfloor,\lfloor r\rfloor+1, l+m-\lfloor r\rfloor-1] \\
& +\{s\}(1-\{r\}) \bar{g}[\lfloor s\rfloor+1, l-m-\lfloor s\rfloor-1,\lfloor r\rfloor, l+m-\lfloor r\rfloor] \\
& +\{s\}\{r\} \bar{g}[\lfloor s\rfloor+1, l-m-\lfloor s\rfloor-1,\lfloor r\rfloor+1, l+m-\lfloor r\rfloor-1] \\
- & \langle\sigma\rangle^{2},
\end{aligned}\quad (3.26)
$$
where
$$
s \equiv(l-m) / \alpha_{j}, \quad r \equiv(l+m) / \alpha_{j},\quad (3.27)
$$
$$
\begin{aligned}
& \bar{g}\left[m_{3}, m_{2}, m_{1}, m_{0}\right] \\
& \quad \equiv g(\overbrace{u_{\mathrm{A}}, \ldots, u_{\mathrm{A}}}^{m_{3}}, \overbrace{u_{\mathrm{B}}, \ldots, u_{\mathrm{B}}}^{m_{2}}, \overbrace{v_{\mathrm{A}}, \ldots, v_{\mathrm{A}}}^{m_{1}}, \overbrace{v_{\mathrm{B}}, \ldots, v_{\mathrm{B}}}^{m_{0}})
\end{aligned}\quad (3.28)
$$
and $\langle\sigma\rangle=0$, as $T \geq T_{\mathrm{c}}$. The averaged correlation $C^{*}(l, m)$ of the disorder variables, which is also the correlation function for $T \leq T_{\mathrm{c}}$, can be obtained from the above equations simply by replacing $g$ by $g^{*}$ and $\langle\sigma\rangle$ by $\left(1-k^{-2}\right)^{1 / 8}$.

For the three-object sequences in (3.25), the numbers of $u_{\mathrm{A}}$'s and $u_{\mathrm{C}}$'s among the $l - m$ consecutive $u$'s are given by (2.12) and (2.13), and the averaged connected correlation in (1.2) can be evaluated using (2.17) through (2.19). We find,

for $\{s\} \leq 1/\alpha_j$,

$$
\begin{aligned}
C(l, m)= & (1-2\{s\}) \tilde{g}[\lfloor s\rfloor, l-m-2\lfloor s\rfloor,\lfloor s\rfloor, l+m] \\
& +\{s\} \tilde{g}[\lfloor s\rfloor, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor+1, l+m] \\
& +\{s\} \tilde{g}[\lfloor s\rfloor+1, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor, l+m] \\
& -\langle\sigma\rangle^{2},
\end{aligned}
\tag{3.29}
$$

where

$$
\begin{aligned}
& \tilde{g}\left[m_{3}, m_{2}, m_{1}, m_{0}\right] \\
& \quad \equiv g(\overbrace{u_{\mathrm{A}}, \ldots, u_{\mathrm{A}}}^{m_{3}}, \overbrace{u_{\mathrm{B}}, \ldots, u_{\mathrm{B}}}^{m_{2}}, \overbrace{u_{\mathrm{C}}, \ldots, u_{\mathrm{C}}}^{m_{1}}, \overbrace{v, \ldots, v}^{m_{0}}).
\end{aligned}
\tag{3.30}
$$

For $1/\alpha_j \leq \{s\} \leq 1-1/\alpha_j$, we find

$$
\begin{aligned}
C(l, m)= & \left(1-\{s\}-1 / \alpha_{j}\right) \tilde{g}[\lfloor s\rfloor, l-m-2\lfloor s\rfloor,\lfloor s\rfloor, l+m] \\
& +\left(1 / \alpha_{j}\right) \tilde{g}[\lfloor s\rfloor, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor+1, l+m] \\
& +\left(1 / \alpha_{j}\right) \tilde{g}[\lfloor s\rfloor+1, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor, l+m] \\
& +\left(\{s\}-1 / \alpha_{j}\right) \tilde{g}[\lfloor s\rfloor+1, l-m-2\lfloor s\rfloor-2,\lfloor s\rfloor+1, l+m] \\
& -\langle\sigma\rangle^{2},
\end{aligned}
\tag{3.31}
$$

whereas, for $\{s\} \geq 1-1/\alpha_j$,

$$
\begin{aligned}
C(l, m)= & (1-\{s\}) \tilde{g}[\lfloor s\rfloor, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor+1, l+m] \\
& +(1-\{s\}) \tilde{g}[\lfloor s\rfloor+1, l-m-2\lfloor s\rfloor-1,\lfloor s\rfloor, l+m] \\
& +(2\{s\}-1) \tilde{g}[\lfloor s\rfloor+1, l-m-2\lfloor s\rfloor-2,\lfloor s\rfloor+1, l+m] \\
& -\langle\sigma\rangle^{2}.
\end{aligned}
\tag{3.32}
$$

Again, the formulae for $C^{*}(l, m)$ are similar, cf. the discussion below (3.28). Also, it is easily verified that we have the general inversion symmetry

$$
C(-l,-m)=C(l, m), \quad C^{*}(-l,-m)=C^{*}(l, m),
\tag{3.33}
$$

valid for all values of $l$ and $m$. Hence, we have now the results for $|m| \leq|l|$.

To evaluate $C(-m, l)$ and $C^{*}(-m, l)$ for $|m| \leq l$, we let $l \to -m$ and $m \to l$ in (3.22) and (3.23), and find that there are $l+m$ horizontal lines $u$ and $l-m$ vertical lines $v$ sandwiched between the two spins.

If $u_{m}$ and $v_{n}$ are given by (3.24), Theorem 1 can again be used to find the average number of $u_{\mathrm{A}}$'s among the $l+m$ consecutive $u$'s and the average number of $v_{\mathrm{A}}+\lambda$'s among the $l-m$ consecutive $v$'s. As a consequence the averaged

connected correlation function in (1.2) for $|m| \leq l$ becomes

$$
\begin{aligned}
C(-m, l)= & (1-\{r\})(1-\{s\}) g^{\prime}[\lfloor r\rfloor, l+m-\lfloor r\rfloor,\lfloor s\rfloor, l-m-\lfloor s\rfloor] \\
& +\{r\}(1-\{s\}) g^{\prime}[\lfloor r\rfloor+1, l+m-\lfloor r\rfloor-1,\lfloor s\rfloor, l-m-\lfloor s\rfloor] \\
& +(1-\{r\})\{s\} g^{\prime}[\lfloor r\rfloor, l+m-\lfloor r\rfloor,\lfloor s\rfloor+1, l-m-\lfloor s\rfloor-1] \\
& +\{r\}\{s\} g^{\prime}[\lfloor r\rfloor+1, l+m-\lfloor r\rfloor-1,\lfloor s\rfloor+1, l-m-\lfloor s\rfloor-1] \\
& -\langle\sigma\rangle^{2}, \quad(3.34)
\end{aligned}
$$

where

$$
\begin{aligned}
& g^{\prime}\left[m_{3}, m_{2}, m_{1}, m_{0}\right] \\
& \equiv g(\overbrace{u_{\mathrm{A}}, \ldots, u_{\mathrm{A}}}^{m_{3}}, \overbrace{u_{\mathrm{B}}, \ldots, u_{\mathrm{B}}}^{m_{2}}, \overbrace{\lambda+v_{\mathrm{A}}, \ldots, \lambda+v_{\mathrm{A}}}^{m_{1}}, \overbrace{\lambda+v_{\mathrm{B}}, \ldots, \lambda+v_{\mathrm{B}}}^{m_{0}}).
\end{aligned}
$$

For the three-object sequences in (3.25), the average numbers of $u_{\mathrm{A}}$'s and $u_{\mathrm{C}}$'s among the $l+m$ consecutive $u$'s are given by (2.17) through (2.19). For $|m| \leq l$ and $\{r\} \leq 1 / \alpha_{j}$, we find

$$
\begin{aligned}
C(-m, l)= & (1-2\{r\}) \tilde{g}^{\prime}[\lfloor r\rfloor, l+m-2\lfloor r\rfloor,\lfloor r\rfloor, l-m] \\
& +\{r\} \tilde{g}^{\prime}[\lfloor r\rfloor, l+m-2\lfloor r\rfloor-1,\lfloor r\rfloor+1, l-m] \\
& +\{r\} g[\lfloor r\rfloor+1, l+m-2\lfloor r\rfloor-1,\lfloor r\rfloor, l-m] \\
& -\langle\sigma\rangle^{2}, \quad(3.36)
\end{aligned}
$$

while, for $1 / \alpha_{j} \leq\{r\} \leq 1-1 / \alpha_{j}$,

$$
\begin{aligned}
C(-m, l)= & \left(1-\{r\}-1 / \alpha_{j}\right) \tilde{g}^{\prime}[\lfloor r\rfloor, l+m-2\lfloor r\rfloor,\lfloor r\rfloor, l-m] \\
& +\left(1 / \alpha_{j}\right) \tilde{g}^{\prime}[\lfloor r\rfloor, l+m-2\lfloor s\rfloor-1,\lfloor r\rfloor+1, l-m] \\
& +\left(1 / \alpha_{j}\right) \tilde{g}^{\prime}[\lfloor r\rfloor+1, l+m-2\lfloor r\rfloor-1,\lfloor r\rfloor, l-m] \\
& +\left(\{r\}-1 / \alpha_{j}\right) \tilde{g}^{\prime}[\lfloor r\rfloor+1, l+m-2\lfloor r\rfloor-2,\lfloor r\rfloor+1, l-m] \\
& -\langle\sigma\rangle^{2}, \quad(3.37)
\end{aligned}
$$

whereas, for $\{r\} \geq 1-1 / \alpha_{j}$,

$$
\begin{aligned}
C(-m, l)= & (1-\{r\}) \tilde{g}^{\prime}[\lfloor r\rfloor, l+m-2\lfloor r\rfloor-1,\lfloor r\rfloor+1, l-m] \\
& +(1-\{r\}) \tilde{g}^{\prime}[\lfloor r\rfloor+1, l+m-2\lfloor r\rfloor-1,\lfloor r\rfloor, l-m] \\
& +(2\{r\}-1) \tilde{g}^{\prime}\lfloor r\rfloor+1, l+m-2\lfloor r\rfloor-2,\lfloor r\rfloor+1, l-m] \\
& -\langle\sigma\rangle^{2}, \quad(3.38)
\end{aligned}
$$

where

$$
\begin{aligned}
\tilde{g}^{\prime} & {\left[m_{3}, m_{2}, m_{1}, m_{0}\right] } \\
& \equiv g(\overbrace{u_{\mathrm{A}}, \ldots, u_{\mathrm{A}}}^{m_{3}}, \overbrace{u_{\mathrm{B}}, \ldots, u_{\mathrm{B}}}^{m_{2}}, \overbrace{u_{\mathrm{C}}, \ldots, u_{\mathrm{C}}}^{m_{1}}, \overbrace{\lambda+v, \ldots, \lambda+v}^{m_{0}}). \quad (3.39)
\end{aligned}
$$

In view of (3.33) and the discussion below (3.28), we have now obtained a complete set of formulae for $C(l, m)$ and $C^{*}(l, m)$. We can use difference equations to obtain, by iteration, all needed $g$'s and $g^{*}$'s. The details of such calculations are in our previous work, $^{(3,11)}$ and will not be presented here. Since the various $g[m_{3}, m_{2}, m_{1}, m_{0}]$'s are obtained iteratively from $g$'s and $g^{*}$'s with smaller $m_{i}$'s, it is necessary to evaluate the $g[m_{3}, m_{2}, m_{1}, m_{0}]$'s for almost all $m_{i}$ such that $0 \leq m_{i} \leq N$ even though for each fixed $\alpha_{j}$, only a fraction of these $g$'s are needed. In spite of powerful modern computers, these calculations are still quite time consuming. Therefore, it is more economical to obtain the correlations for all different $j$'s studied in one shot.

In the next section we shall be a little more specific. If the four above rapidities $(u_{\mathrm{A}}, u_{\mathrm{B}}, v_{\mathrm{A}}, v_{\mathrm{B}})$ or $(u_{\mathrm{A}}, u_{\mathrm{B}}, u_{\mathrm{C}}, v)$ are chosen to be multiples of $\lambda / 4$ in a certain way (details will be given later), we can use the permutation property to arrange the rapidities in $g$ and $g^{*}$ in descending order, and then use the difference property to make the smallest rapidity identically equal to zero. Then, all functions $g$ and $g^{*}$ in (3.28), (3.35), (3.30) and (3.39) can be brought to the form

$$
g\left[m_{3}, m_{2}, m_{1}, m_{0}\right]=g\left(\overbrace{\frac{3}{4} \lambda, \ldots, \frac{3}{4} \lambda}^{m_{3}}, \overbrace{\frac{1}{2} \lambda, \ldots, \frac{1}{2} \lambda}^{m_{2}}, \overbrace{\frac{1}{4} \lambda, \ldots, \frac{1}{4} \lambda}^{m_{1}}, \overbrace{0, \ldots, 0}^{m_{0}}\right),
$$

possibly permuting the $m_{i}$'s.

## 4. WAVEVECTOR-DEPENDENT SUSCEPTIBILITY

Since the correlation functions decay exponentially $(T \neq T_{\mathrm{c}})$, we need to put all the terms that have approximately the same order of magnitude together. More specifically we write

$$
\bar{\chi}\left(q_{x}, q_{y}\right) \equiv k_{\mathrm{B}} T \chi\left(q_{x}, q_{y}\right)=C(0,0)+2 \sum_{l=1}^{\infty} S_{l}, \quad(\text { with } C(0,0)=1),
$$

$$
S_{l}=\sum_{m=1-l}^{l}\left[C(l, m) \cos \left(q_{x} l+q_{y} m\right)+C(-m, l) \cos \left(-q_{x} m+q_{y} l\right)\right], \quad(4.41)
$$

where $S_{l}$ contains the correlations of the top and right edges of the square whose four corners are $( \pm l, \pm l)$. The above cosines result from the use of the inversion symmetry (3.33) in order to include the contributions of the other two edges. For

$T$ away from $T_{\mathrm{c}}$, only a few $S_{l}$ for $l$ small are numerically significant. As $T \rightarrow T_{\mathrm{c}}$, more and more terms need be included. This way the $q$-dependent susceptibility can now be evaluated for different cases.

### 4.1. Sequences of Two Objects, Example I

We shall first consider some quasiperiodic sequences of two objects. Let the sequence of rapidity lines be defined by (3.24) with the particular values
$$
u_{\mathrm{A}}=3 \lambda / 4, \quad u_{\mathrm{B}}=2 \lambda / 4, \quad v_{\mathrm{A}}=\lambda / 4, \quad v_{\mathrm{B}}=0. \tag{4.42}
$$

Comparing (3.28) and (3.35) with (3.40), we find
$$
\bar{g}\left[m_{3}, m_{2}, m_{1}, m_{0}\right]=g\left[m_{3}, m_{2}, m_{1}, m_{0}\right],
$$
$$
g^{\prime}\left[m_{1}, m_{0}, m_{3}, m_{2}\right]=g\left[m_{3}, m_{2}, m_{1}, m_{0}\right], \tag{4.43}
$$
where the permutation property and the difference property $^{(4)}$ are used for the second identity. Now, comparing (3.26) with (3.34), we find
$$
C(-m, l)=C(l, m), \quad C^{*}(-m, l)=C^{*}(l, m). \tag{4.44}
$$

From (4.44), we find that the $q$-dependent susceptibility must have fourfold rotational symmetry.

We can calculate the $q$-dependent susceptibility for fixed $T \neq T_{\mathrm{c}},(k \neq 1)$, to arbitrary precision using an algorithm of polynomial complexity. For this purpose, we use quadratic difference equations $^{(2,3,5,6,11)}$ to numerically evaluate the averaged correlation functions given by (3.26), (4.43) and (4.44) for $T>T_{\mathrm{c}}$, and replace $g$ and $\langle\sigma\rangle \equiv 0$ by $g^{*}$ and $\langle\sigma\rangle=\left(1-k^{-2}\right)^{1 / 8}$ for $T<T_{\mathrm{c}}$. We have used Maple software for this, as higher and higher precision arithmetic is needed closer and closer to $T_{\mathrm{c}}$. Substituting the results into (4.41), we obtain the $q$-dependent susceptibility at different temperatures. We shall present our results mostly in density plots to get an overview of the full $\left(q_{x}, q_{y}\right)$-dependence. Our results, however, are far more accurate than these plots suggest.

In Fig. 4, we show four density plots of $1 / \chi(\mathbf{q})$ for $j=0,1,2$ or 3 and $-2 \pi<$ $q_{x}, q_{y}<2 \pi$, at the one temperature $T>T_{\mathrm{c}}$ for which the above- $T_{\mathrm{c}}$ correlation length $\xi \approx 8 .^{3}$ (In the density plots, darker means a relatively larger value of $\chi(\mathbf{q})$, and $\mathrm{x} \equiv q_{x}, \mathrm{y} \equiv q_{y}$.) We find that there is no incommensurate behavior, for all different values of $\alpha_{j}$ with $j \geq 0$ and at arbitrary temperature. The peaks of $\chi(\mathbf{q})$ are at the commensurate positions of the ordinary Ising model, i.e. $\left(q_{x}, q_{y}\right)=$

---
$^{3}$ More precisely, $\xi$ is the row correlation length of the uniform and symmetric square-lattice Ising model with the same value of modulus $k=\left(\cosh ^{2}\left(\frac{1}{2} \xi^{-1}\right) \pm\left[\cosh ^{4}\left(\frac{1}{2} \xi^{-1}\right)-1\right]^{1 / 2}\right)^{2}$, with minus for $T>T_{\mathrm{c}}$. For $T<T_{\mathrm{c}}$, we must choose plus, while $\xi$ is then twice the actual row correlation length. $^{(12)}$

![](./images/812015499176050689_6.jpg)

(a) golden ratio: $j=0$ and $\alpha_0=(\sqrt{5}+1)/2$

![](./images/812015499176050689_7.jpg)

(b) silver mean: $j=1$ and $\alpha_1=\sqrt{2}+1$

![](./images/812015499176050689_8.jpg)

(c) $j=2$ and $\alpha_2=(\sqrt{13}+3)/2$

![](./images/812015499176050689_9.jpg)

(d) $j=3$ and $\alpha_3=\sqrt{5}+2$

Fig. 4. Density plots of $1/\chi(q_x, q_y)$ for cases when the sequences of rapidities $(u_m)$ and $(v_m)$ are quasiperiodic sequences of two objects given by (3.24) and (4.42) at $k=0.83791870 (\xi\approx8), T>T_\text{c}$. There is no significant $j$-dependence.

$(2\pi m, 2\pi n)$ where $m$ and $n$ are any integers. We also find that $\chi(\mathbf{q})$ is indeed invariant under $90^\circ$ rotation.

To look at the situation more quantitatively, making sure that there are indeed no incommensurate peaks, we can study $\chi(0, q)$ and $\chi(q, q)$. We have plotted $\chi(q, q)$ versus $q$ for $j=0,\dots,4$ and $T<T_\text{c}$ in Fig. 5(a), and also for $T>T_\text{c}$ in Fig. 5(b). As $j$ increases, there are more B type of rapidity lines. This in turn means more weak bonds are present in the system. Therefore, as $j$ increases, the peaks in the susceptibility decrease, as shown in these plots. The changes are very small, however. The plots clearly show no indication of incommensurate peaks. The behavior of $\chi(\mathbf{q})$ for $T>T_\text{c}$ is not much different from the behavior at $T<T_\text{c}$, except that the peaks are sharper.

![](./images/812015499176050689_10.jpg)

(a) $T < T_{\rm c}$: $k = 4.2309029$

![](./images/812015499176050689_11.jpg)

(b) $T > T_{\rm c}$: $k = 0.2363561688$ ($\xi = 1$)

Fig. 5. Plots of $\chi(q,q)$ versus $\mathrm{x} \equiv q$ for the cases given by (3.24) and (4.42) and $j=0, \ldots, 4$. The curves for $j=0$ have the highest value at $q=0$, and the peaks decrease in magnitude as $j$ increases.

We could give more density plots for different temperatures and also for temperatures below and above $T_{\rm c}$. But those plots would not be much different from Fig. 4. We find that as $T \to T_{\rm c}$, the peaks of $\chi(\mathbf{q})$ become sharper. Also, the peaks of $\chi(\mathbf{q})$ for $T > T_{\rm c}$ are sharper than those for $T < T_{\rm c}$, as the correlation length above $T_{\rm c}$ is only half in length compared to the one at the dual temperature below $T_{\rm c}.^{(12)}$ But it is hard to read that off from a density plot.

### 4.2. Sequences of Two Objects, Example II

Instead of (4.42), we may also choose
$$
u_{\mathrm{B}}=3 \lambda / 4, \quad u_{\mathrm{A}}=2 \lambda / 4, \quad v_{\mathrm{B}}=\lambda / 4, \quad v_{\mathrm{A}}=0. \tag{4.45}
$$

Comparing (3.28) and (3.35) with (3.40) again, we find
$$
\begin{aligned}
\bar{g}\left[m_{2}, m_{3}, m_{0}, m_{1}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right], \\
g^{\prime}\left[m_{0}, m_{1}, m_{2}, m_{3}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right].
\end{aligned} \tag{4.46}
$$

It is easily seen that (4.44) still holds, so that $\chi(\mathbf{q})$ still has 4-fold rotation symmetry. The behaviors of $\chi(\mathbf{q})$ are essentially the same as in the previous case, except that the peaks become sharper as $j$ increases.

### 4.3. Sequences of Two Objects, Example III

If we let
$$
u_{\mathrm{A}}=3 \lambda / 4, \quad u_{\mathrm{B}}=2 \lambda / 4, \quad v_{\mathrm{B}}=\lambda / 4, \quad v_{\mathrm{A}}=0, \tag{4.47}
$$

![](./images/812015499176050689_12.jpg)

(a) golden ratio: $j=0$ and $\alpha_0=(\sqrt{5}+1)/2$

![](./images/812015499176050689_13.jpg)

(b) silver mean: $j=1$ and $\alpha_1=\sqrt{2}+1$

![](./images/812015499176050689_14.jpg)

(c) $j=2$ and $\alpha_2=(\sqrt{13}+3)/2$

![](./images/812015499176050689_15.jpg)

(d) $j=3$ and $\alpha_3=\sqrt{5}+2$

Fig. 6. Density plots of $1/\chi(q_x,q_y)$ for the cases defined by (3.24) and (4.47) at $T>T_c$, $k=0.49127583$ ($\xi\approx2$). The susceptibility is like the one of the rectangular Ising model, as can be seen with some effort, with peaks still at the commensurate positions.

then

$$
\begin{aligned}
\bar{g}[m_3,m_2,m_0,m_1] &= g[m_3,m_2,m_1,m_0], \\
g'[m_0,m_1,m_3,m_2] &= g[m_3,m_2,m_1,m_0].
\end{aligned} \tag{4.48}
$$

Consequently, (4.44) no longer holds. As a result, $\chi(\mathbf{q})$ behaves more like that of the rectangular Ising lattice, which is not invariant under $90^\circ$ rotations, but still has only commensurate peaks. Density plots are shown in Fig. 6.

### 4.4. Sequences of Three Objects, Example IV

We now let the sequence of rapidity lines be defined by (3.25) and let
$$
u_{\mathrm{A}}=3 \lambda / 4, \quad u_{\mathrm{B}}=2 \lambda / 4, \quad u_{\mathrm{C}}=\lambda / 4, \quad v=0. \tag{4.49}
$$

Comparing (3.30) and (3.39) with (3.40), we obtain
$$
\begin{aligned}
\tilde{g}\left[m_{3}, m_{2}, m_{1}, m_{0}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right], \\
\tilde{g}^{\prime}\left[m_{0}, m_{3}, m_{2}, m_{1}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right].
\end{aligned} \tag{4.50}
$$

We evaluate the $\chi(\mathbf{q})$ in (4.41) by substituting this equation into (3.29), (3.31), (3.32), (3.36), (3.37) and (3.38). The probabilities for the three-object sequence given by (2.17) through (2.19) are quite complicated. Nevertheless, we find similar behavior for all different $j$'s and temperatures. There is no incommensurate behavior-the peak of the susceptibility $\chi(\mathbf{q})$ is at the commensurate position of the ordinary Ising model, $(q_{x}, q_{y})=(0,0)$, and repeated periodically with periods $2\pi$.

In Fig. 7, four density plots are presented for $T<T_{\mathrm{c}}$ at $k=1.1934332$ and for $j=1,\dots,4$. We again find that $\chi(\mathbf{q})$ decreases as $j$ increases. Since only the $(u_{m})$ sequence is aperiodic, the distortion due to the quasiperiodicity on $\chi(\mathbf{q})$ is along the diagonal. In this particular case, we find that the two diagonals are the symmetry axes of $\chi(\mathbf{q})$.

### 4.5. Sequences of Three Objects, Example V

If instead of (4.49), we let
$$
u_{\mathrm{A}}=3 \lambda / 4, \quad u_{\mathrm{C}}=2 \lambda / 4, \quad u_{\mathrm{B}}=\lambda / 4, \quad v=0, \tag{4.51}
$$
then
$$
\begin{aligned}
\tilde{g}\left[m_{3}, m_{1}, m_{2}, m_{0}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right], \\
\tilde{g}^{\prime}\left[m_{0}, m_{3}, m_{1}, m_{2}\right] & =g\left[m_{3}, m_{2}, m_{1}, m_{0}\right].
\end{aligned} \tag{4.52}
$$

The resulting $q$-dependent susceptibility is less symmetric. Four density plots at $T<T_{\mathrm{c}}, k=1.1934332$, are shown in Fig. 8 for $j=1,\dots,4$. Again we only find commensurate peaks.

## 5. A MIXED CASE

We have examined quasiperiodic Ising lattices on a square lattice, whose interactions are quasiperiodic and ferromagnetic, and we have found very similar commensurate behaviors.

![](./images/812015499176050689_16.jpg)

![](./images/812015499176050689_17.jpg)

![](./images/812015499176050689_18.jpg)

![](./images/812015499176050689_19.jpg)

Fig. 7. Density plots of $1/\chi(q_x, q_y)$ for cases when only $(u_m)$ is a quasi-periodic sequence. They are given by (3.25) and (4.49) at $T < T_\mathrm{c}$, $k = 1.1934332$. Again the peaks are only at the commensurate positions. They are elongated in a diagonal direction.

Things change dramatically if we consider mixed cases with both ferro- and antiferromagnetic interactions, as we already know from our previous work that there will be many incommensurate peaks within the unit cell as the temperature moves close to the critical value. $^{(2,3)}$ There is one new aspect: The results, especially the positions of the many incommensurate peaks, are heavily dependent on the value of $j$. We shall illustrate this with one example based on some ideas of Sec. 5 of Ref. 2 where several $j = 0$ cases have been studied.

Unlike the ferromagnetic case, we can now construct an example starting from the symmetric square-lattice Ising model and flipping the signs of the couplings by site-dependent gauge transformations. Using Theorem 1, Eqs. (5.17) and (5.18)

![](./images/812015499176050689_20.jpg)

**(a) silver mean:** $j = 1$ and $\alpha_1 = \sqrt{2} + 1$

![](./images/812015499176050689_21.jpg)

**(b)** $j = 2$ and $\alpha_2 = (\sqrt{13} + 3)/2$

![](./images/812015499176050689_22.jpg)

**(c)** $j = 3$ and $\alpha_3 = \sqrt{5} + 2$

![](./images/812015499176050689_23.jpg)

**(d)** $j = 4$ and $\alpha_4 = (\sqrt{29} + 5)/2$

Fig. 8. Density plots of $1/\chi(q_x, q_y)$ for the cases given by (3.25) and (4.51) at $T < T_\mathrm{c}, k = 1.1934332$.
Still the peaks of $\chi(q_x, q_y)$ are at the commensurate positions. The peaks are now elongated and a
slight dependence on $j$ may be observed.

of Ref. 2 are now replaced by

$$
\begin{aligned}
\phi^{(j)}(m) & =(-1)^{\lfloor m / \alpha_{j}\rfloor}\left(1-2\left\{m / \alpha_{j}\right\}\right), \\
& =\sum_{l=-\infty}^{\infty} \frac{\mathrm{e}^{2 \pi \mathrm{i}(l+1 / 2) m / \alpha_{j}}}{(l+1 / 2)^{2} \pi^{2}}=\phi^{(j)}(-m).
\end{aligned}\tag{5.53}
$$

Choosing a model aperiodic in both diagonal directions as in Sec. 5.6 of
Ref. 2, the averaged connected correlation function now becomes

$$
C^{(\mathrm{c})}(l, m)=\phi^{(j)}(l+m) \phi^{(j)}(l-m) C_{0}^{(\mathrm{c})}(l, m),\tag{5.54}
$$

with $C_{0}^{(\mathrm{c})}(l, m)$ the connected pair-correlation function of the square-lattice Ising model. This implies that $\chi(\mathbf{q})$ has many incommensurate peaks within the unit cell, and is given by

$$
\chi\left(q_{x}, q_{y}\right)=\sum_{l=-\infty}^{\infty} \sum_{m=-\infty}^{\infty} \frac{\chi_{0}\left(q_{x}+2 \pi(l+m+1) / \alpha_{j}, q_{y}+2 \pi(l-m) / \alpha_{j}\right)}{(l+1 / 2)^{2}(m+1 / 2)^{2} \pi^{4}},
$$

(5.55)

with $\chi_{0}(\mathbf{q})$ the wavevector-dependent susceptibility of the regular square-lattice Ising model.

Density plots are given in Fig. 9 for four cases with correlation length $\xi \approx 16$. Clearly, the results depend strongly on $j$. The case $j=3$ is the most different as it almost looks like the periods have been halved. This can be explained easily since $2 \pi / \alpha_{3} \approx \pi / 2$.

## 6. CONCLUSIONS

From the current work and our previous papers $^{(1-3)}$ we can draw several conclusions:

- The wavevector-dependent susceptibilities $\chi(\mathbf{q})$ of models, whose spin sites are on regular lattices, are always periodic. This includes cases when the interactions between the spins are quasi-periodic.
- When the interactions between spins are quasiperiodic, but strictly ferromagnetic, $\chi(\mathbf{q})$ has only commensurate peaks, with behavior very similar to that of the regular Ising model.
- The $q$-dependent susceptibilities $\chi(\mathbf{q})$ of models on regular periodic lattices can have everywhere-dense incommensurate peaks in every unit cell, but only for cases for which the interactions between spins are mixed with both ferro- and antiferromagnetic couplings present. $^{(2,3)}$
- When the lattice is quasiperiodic—such as a $Z$-invariant Ising model on Penrose tiles-$\chi(\mathbf{q})$ is no longer periodic but quasiperiodic and exhibits everywhere-dense incommensurate peaks, even for the case of purely ferromagnetic couplings. Only few of these peaks are visible within a given limited area of $\mathbf{q}$-space when the temperature is far away from the critical temperature. The number of visible peaks increases as $T$ approaches $T_{\mathrm{c}} \cdot{ }^{(1)}$

There are many other quasiperiodic sequences. Still we have examined a variety of cases and believe that the above conclusions are quite generic.

It may be interesting to consider the $q$-dependent susceptibility $\chi(\mathbf{q})$ of the $Z$-invariant Ising model on the labyrinth $^{(13-15)}$ for which the distances between the spins are also aperiodic. To obey the symmetry, the couplings of pairs of spins must be related to the distances between the spins. When the distances are equal,

![](./images/812015499176050689_24.jpg)

(a) golden ratio: $j=0, \alpha_{1}=(\sqrt{5}+1) / 2$

![](./images/812015499176050689_25.jpg)

(b) silver mean: $j=1, \alpha_{1}=\sqrt{2}+1$

![](./images/812015499176050689_26.jpg)

(c) $j=2$, i.e. $\alpha_{1}=(\sqrt{13}+3) / 2$

![](./images/812015499176050689_27.jpg)

(d) $j=3$, i.e. $\alpha_{3}=\sqrt{5}+2$

Fig. 9. Density plots of $1 / \chi(q_{x}, q_{y})$ for the mixed case for four values of $j,(j=0,..., 3)$ , with $q_{x}$
and $q_{y}$ in the interval $(-\pi, \pi)$ and $k=0.915398728 \cdots$ . Now there are many incommensurate peaks
and their positions depend strongly on $j$ . The principal peaks are at $( \pm q_{j}, 0),(0, \pm q_{j})$ , with $q_{0}=$
$2 \pi(1-1 / \alpha_{0})=2.39996 \cdots, q_{1}=2 \pi / \alpha_{1}=2.60258 \cdots, q_{2}=2 \pi / \alpha_{2}=1.90239 \cdots, q_{3}=2 \pi / \alpha_{3}=$
$1.48325 \cdots$ . This last value is close to $\pi / 2$ , which is reflected in figure (d).

the corresponding couplings must be chosen to be equal. Since the coupling $K$ and
$\bar{K}$ in a $Z$ -invariant model are related by (1.4), our preliminary efforts in this regard
have not been successful, but the model deserves further investigation. One thing
we can predict: The $q$-dependent susceptibility $\chi(\mathbf{q})$, for the Ising model on the
labyrinth, can no longer be periodic, and its peaks should be at incommensurate
positions.

## ACKNOWLEDGMENTS

We are most thankful to Dr. M. Widom for his interest in using exactly solvable models to study quasicrystals. This work has been supported by NSF Grant PHY 01-00041.

## REFERENCES

1. H. Au-Yang and J. H. H. Perk, Wavevector-dependent susceptibility in $Z$-invariant pentagrid Ising model. *J. Stat. Phys.* DOI: 10.1007/s10955-006-9212-x (2006).
2. H. Au-Yang, B.-Q. Jin and J. H. H. Perk, Wavevector-dependent susceptibility in quasiperiodic Ising models. *J. Stat. Phys.* 102:501–543 (2001).
3. H. Au-Yang and J. H. H. Perk, Wavevector-dependent susceptibility in aperiodic planar Ising models, in *MathPhys Odyssey 2001: Integrable Models and Beyond*, M. Kashiwara and T. Miwa, eds. (Birkhäuser, Boston, 2002), pp. 1–21.
4. R. J. Baxter, Solvable eight vertex model on an arbitrary planar lattice. *Phil. Trans. R. Soc. Lond. A* 289:315–346 (1978).
5. H. Au-Yang and J. H. H. Perk, Critical correlations in a $Z$-invariant inhomogeneous Ising model, *Physica A* 144:44–104 (1987).
6. J. H. H. Perk, Quadratic identities for Ising correlations. *Phys. Lett. A* 79:3–5 (1980).
7. C. A. Tracy, Universality class of a Fibonacci Ising model. *J. Stat. Phys.* 51:481–490 (1988).
8. C. A. Tracy, Universality classes of some aperiodic Ising models. *J. Phys. A* 11:L603–L605 (1988).
9. N. G. de Bruijn, Sequences of zeros and ones generated by special production rules. *Indagationes Mathematicae* 84:27–37 (1981).
10. G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 4th edition (Oxford University Press, London, 1960), Ch. XXIII Kronecker’s Theorem.
11. H. Au-Yang and J. H. H. Perk, Correlation functions and susceptibility in the $Z$-invariant Ising model, in *MathPhys Odyssey 2001: Integrable Models and Beyond*, M. Kashiwara and T. Miwa, eds. (Birkhäuser, Boston, 2002), pp. 23–48.
12. B. M. McCoy and T. T. Wu, *The Two-Dimensional Ising Model* (Harvard Univ. Press, Cambridge, Mass., 1973).
13. M. Baake, U. Grimm and R. J. Baxter, A critical Ising model on the labyrinth. *Intern. J. Mod. Phys. B* 8:3579–3600 (1994).
14. U. Grimm, M. Baake and H. Simon, Ising spins on the labyrinth, in *Proc. of the 5th International Conference on Quasicrystals*, C. Janot and R. Mosseri, eds. (World Scientific, Singapore, 1995), pp. 80–83.
15. U. Grimm and M. Baake, Aperiodic Ising models, in *The Mathematics of Long-Range Aperiodic Order*, R. V. Moody, ed. (Kluwer, Dordrecht, 1997), pp. 199–237.