# THE CLASSICAL ONE-DIMENSIONAL HEISENBERG MAGNET IN AN EXTERNAL MAGNETIC FIELD. TRANSFER MATRIX FORMALISM AS AN APPLICATION OF RENORMALIZATION GROUP THEORY "AVANT LA LETTRE"

TH.W. RUIJGROK $\neq$

Instituut voor Theoretische Physica, Rijksuniversiteit te Utrecht, The Netherlands

and

TH. NIEMEIJER

Laboratorium voor Technische Natuurkunde, Technische Hogeschool Delft, The Netherlands

Received 19 February 1976

The classical one-dimensional Heisenberg magnet is treated in the context of renormalization theory. This treatment is shown to be equivalent to the usual transfer matrix approach. If the chain consists of $N$ spins, the original hamiltonian will, upon repeated application of the renor malization transformation, be transformed into $N$ uncoupled spins described by $N$ identical one particle hamiltonians, $H_{eff }$, which depends upon the original interaction and field.

The results of Blume, Heller and Lurie $^{1}$ ), who treated the same problem in a completely clas sical way, will be discussed in the light of our results.

## 1. Statement of the problem
Although physical systems of one-dimension have seemed to be of rather academic interest until some years ago, though they formed an excellent testing ground for theories for more realistic problems, lately it has become clear that na- ture has provided us with a large number of crystals in which there are more or less isolated chains (i.e. one-dimensional) of magnetic ions. For a review of much experimental $^{2}$ ) and theoretical $^{3}$ ) work on these systems, the references cited should be consulted. Many other references, also containing neutron scattering results, are cited in ref. 1.

$\neq$ Mailing address: Sorbonnelaan 4, De Uithof, Utrecht, The Netherlands.

Not only static, but also dynamical aspects of these magnetic chains have been studied. Sometimes specific models, such as the quantum-mechanical $X-Y$ model are accessible to exact calculations of static⁵) and dynamic⁶) properties; on the other hand, sometimes they are almost completely inaccessible to the calculation of any property, such as the antiferromagnetic, isotropic linear Heisenberg chain.

In the case of the classical ferro- or antiferromagnetic, isotropic linear Heisen- berg chain, defined by
$$
-\beta \mathscr{H}_{N}=K \sum_{i=1}^{N}\left(S_{i} \cdot S_{i+1}-1\right)+k \sum_{i=1}^{N}\left(S_{i}^{z}-1\right)
\tag{1}
$$
one can find exact expressions for the thermodynamic behaviour and the static spin-spin correlations for the special case that the external field $k=0$. The same can be done for the case of a logarithmic potential, giving rise to a phase transi- tion (to be published). "Classical" in this context means that the quantities $S_{i}$ are to be regarded as classical unit vectors. Notice that for future convenience terms of value $-1$ have been added behind both summation signs in (1) and that a factor $-1 / k_{\mathrm{B}} T$ has been absorbed in the coupling constant and the magnetic field (in the conventional notation one would have $K=-J / k_{\mathrm{B}} T$ and $k=-\mu H / k_{\mathrm{B}} T$, so $K<0$ corresponds to ferromagnetic and $K>0$ to antiferromagnetic coupling; $H$ is the external magnetic field and $\mu$ the magnetic moment).

For $k \neq 0$ the problem of finding the free energy of the system defined by (1) is no longer analytically solvable in elementary functions⁸) (at least it can be shown to be equivalent to a nonseparable differential equation of two variables) and one has to resort to numerical methods. It can easily be shown¹,⁹) that the problem of finding the free energy of the system defined by (1) is equivalent to finding the largest (for $T \neq 0$) non-degenerate eigenvalue of the linear integral equation
$$
\int \mathrm{d} S_{2} \exp \left[K\left(S_{1} \cdot S_{2}-1\right)+k\left(S_{1}^{z}+S_{2}^{z}-2\right) / 2\right] \psi_{l, m}\left(S_{2}\right)=\lambda_{l} \psi_{l, m}\left(S_{1}\right). \quad (2)
$$

We shall come back to this in section 3.

In a preceding paper¹⁰), the present authors obtained a rapidly convergent series for the free energy of the classical spin chain in the absence of an external field, i.e. (1) with $k=0$, through the use of an exact renormalization group. The rapidity of the convergence of the series could be checked against the exact solution provided by ref. 7. The renormalization group approach to (1) for $k \neq 0$ was only formally given in ref. 10 and the authors want to return to this problem for several reasons.

Firstly, because it can be shown that the system (1), upon repeated application of the exact renormalization group to be adopted, is transformed into a single spin determined by an effective hamiltonian $H_{\text {eff }}$, or, equivalently, that the original

system (1) is equivalent to $N$ non-interacting spins, each described by the effective hamiltonian $H_{\text{eff}}(K, k)$, for which an explicit expression shall be given. The latter property probably holds for all systems for which the problem of finding the free energy reduces to finding the largest eigenvalue of a linear integral equation like (2). The fact that $H_{\text{eff}}$ does explicitly depend upon the original interactions $K$ and $k$, which is quite different from the fixed point idea, is a direct reflection of the physical fact that the magnetization per spin, $m$, is invariant under the renor- malization transformation to be adopted. That, again is a direct consequence of the fact that this particular renormalization transformation is a decimation trans- formation $^{11}$ ) and as such automatically a so-called linear transformation $^{12}$ ). We shall prove the invariance of the magnetization per spin for the system defined by (1) under our particular renormalization transformation but the proof can easily be extended to any linear renormalization transformation on Heisenberg or Ising spin systems. In fact, numerical evidence for this was already found by Subbarao $^{13}$ ).

The second reason for returning to (1) is that the particular form of $H_{\text{eff}}(K, k)$, that is found, and the way it is defined shed light on the numerical results of ref. 1, in particular the fact that for many values of the interaction parameters the Lange- vin function for the magnetization is found, features that otherwise might not have been well understood.

Thirdly, a direct connection with the transfer matrix method as adapted to systems like (1), leading to eq. (2), is indicated. It is hoped that this connection can be extended to systems of higher dimension, in particular to the two-dimen- sional Ising model.

## 2. The renormalization transformation; the effective hamiltonian: results and the connection with the transfer matrix method

We shall now construct a renormalization transformation for the classical Heisenberg chain in the presence of an external field. With that aim we introduce the expression:

$$
A_{0}\left(S_{1}, S_{2}\right)=\exp \left[K\left(S_{1} \cdot S_{2}-1\right)+k\left(S_{1}^{z}+S_{2}^{z}-2\right) / 2\right]. \tag{3}
$$

Then of course we can write

$$
Q_{2 N}(K, k)=\int \cdots \int \mathrm{d} S_{1} \cdots \mathrm{d} S_{2 N} \prod_{i=1}^{2 N} A_{0}\left(S_{i}, S_{i+1}\right), \tag{4}
$$

and from the partition function (4) the free energy per spin $f(K, h)$ is calculated as

$$
\beta f(K, k)=\hat{f}(K, k)=-\lim _{N \rightarrow \infty} \frac{1}{2 N} \ln Q_{2 N}(K, k) \tag{5}
$$

(cyclical boundary conditions).

As in ref. 10 we now define a new interaction and thereby a renormalization transformation through eqs. (6), (7) and (8):

$$
A_{n+1}\left(S_{1}, S_{2}\right)=\frac{\int \mathrm{d} S A_{n}\left(S_{1}, S\right) A_{n}\left(S, S_{2}\right)}{\int \mathrm{d} S A_{n}^{2}(S, \hat{z})}
\tag{6}
$$

where $\hat{z}$ is the unit vector in the $z$-direction, and

$$
A_{n}\left(S_{1}, S_{2}\right)=\exp \left[K_{n}\left(S_{1}, S_{2}\right)+\frac{1}{2} k_{n}\left(S_{1}\right)+\frac{1}{2} k_{n}\left(S_{2}\right)-K-k\right]
\tag{7}
$$

furthermore we define $g_{n}$ as

$$
\mathrm{e}^{g_{n}}=\mathrm{e}^{K+k} \int \mathrm{d} S A_{n}^{2}(S, \hat{z}),
\tag{8}
$$

with $K_{1}(1)=K(1)=\bar{K}$. By eq. (8) $g_{n}$ is uniquely determined by $K_{n}$ and $k_{n}$.

Obviously $A_{0}\left(S_{1}, S_{2}\right)$ is symmetric, so is $A_{n}$ by induction and $A_{n}(\hat{z}, \hat{z})=1$.
If the polar and azimuthal angles of $S_{i}$ are denoted by $\theta_{i}$ and $\phi_{i}$ respectively one immediately observes that $A_{n}\left(S_{1}, S_{2}\right)$ is invariant when both spins are rotated about the same angle $\phi$ and that $A_{n}\left(S_{1}, S_{2}\right)$ also is invariant for an interchange of $\phi_{1}$ and $\phi_{2}$ so accordingly we may write

$$
A_{n}\left(\theta_{1}, \theta_{2} ; \phi_{1}, \phi_{2}\right)=\sum_{m=-\infty}^{\infty} B_{m}^{(n)}\left(\theta_{1}, \theta_{2}\right) \exp \left\{\mathrm{i} m\left(\phi_{1}-\phi_{2}\right)\right\}.
\tag{9}
$$

One observes from the preceding that $B_{m}^{(n)}$ is symmetric in $\theta_{1}$ and $\theta_{2}$ and only even $m$'s appear in the summation (9). Substituting eq. (9) into eq. (6) we obtain

$$
B_{m}^{(n+1)}\left(\theta_{1}, \theta_{2}\right)=\frac{\int_{0}^{\pi} \sin \theta \mathrm{d} \theta B_{m}^{(n)}\left(\theta_{1}, \theta\right) B_{m}^{(n)}\left(\theta, \theta_{2}\right)}{\sum_{m=-\infty}^{\infty} \int_{0}^{\pi} \sin \theta \mathrm{d} \theta\left\{B_{m}^{(n)}(\theta, 0)\right\}^{2}}.
\tag{10}
$$

In the case of (1) we have

$$
\begin{aligned}
B_{m}^{(0)}= & \frac{1}{2 \pi} \int_{0}^{\pi} A_{0}\left(\theta_{1}, \theta_{2}, \phi\right) \mathrm{e}^{-\mathrm{i} m \phi} \mathrm{d} \phi=I_{m}\left(K \sin \theta_{1} \sin \theta_{2}\right) \\
& \times \exp \left[K\left(\cos \theta_{1} \cos \theta_{2}-1\right)+k\left(\cos \theta_{1}+\cos \theta_{2}-2\right) / 2\right]
\tag{11}
\end{aligned}
$$

and specifically

$$
B_{m}^{(0)}\left(\theta_{1}, 0\right)=\delta_{m, 0} \exp \left[K\left(\cos \theta_{1}-1\right)+k\left(\cos \theta_{1}-1\right) / 2\right].
\tag{12}
$$

The property $B_{m}^{(n)}\left(\theta_{1}, 0\right)=0$ if $m \neq 0$ is conserved under iteration, and so only the term $B_{0}^{(n)}$ contributes to (8), since only $\hat{z}$ appears, and from now on we shall suppress the lower index.

Thus the actual renormalization transformation reduces to the following two eqs. (13) and (14)
$$B^{(n+1)}\left(\theta_{1}, \theta_{2}\right)=\frac{\int_{0}^{\pi} \sin \theta \mathrm{d} \theta B^{(n)}\left(\theta_{1}, \theta\right) B^{(n)}\left(\theta, \theta_{2}\right)}{\int_{0}^{\pi} \sin \theta \mathrm{d} \theta\left\{B^{(n)}(\theta, 0)\right\}^{2}}\qquad(13)$$

$$\mathrm{e}^{g_{n}}=2 \pi \mathrm{e}^{K+k} \int_{0}^{\pi} \sin \theta \mathrm{d} \theta\left\{B^{(n)}(\theta, 0)\right\}^{2}\qquad(14)$$
with the initial condition
$$\begin{aligned}
B^{(0)}\left(\theta_{1}, \theta_{2}\right)= & I_{0}\left(K \sin \theta_{1} \sin \theta_{2}\right) \\
& \times \exp \left[K\left(\cos \theta_{1} \cos \theta_{2}-1\right)+k\left(\cos \theta_{1}+\cos \theta_{2}-2\right) / 2\right].(15)
\end{aligned}$$

Obviously $g_{n} \to K+k+\ln 4 \pi$ .

With eq. (4) we can write
$$Q_{2 N}(K, k)=\mathrm{e}^{N g(K, k)} Q_{N}\left(K_{1}, k_{1}\right)\qquad(16)$$
from which follows
$$\hat{f}(K, k)=-\frac{1}{2} g(K, k)+\frac{1}{2} \hat{f}\left(K_{1}, k_{1}\right).\qquad(17)$$

As in ref. 10, repeated application of the renormalization transformation (4) leads to the following expression for the free energy
$$\hat{f}(K, k)=-\sum_{n=0}^{M} \frac{g_{n}}{2^{n+1}}+\frac{\hat{f}\left(K_{M+1}, k_{M+1}\right)}{2^{M+1}}\qquad(18)$$
where $M$ is the number of iterations.

It is immediately seen that
$$\lim _{n \rightarrow \infty} B^{(n)}\left(\theta_{1}, \theta_{2}\right) \equiv B\left(\theta_{1}, \theta_{2}\right)=f\left(\theta_{1}\right) f\left(\theta_{2}\right)\qquad(19)$$
is a fixed point of the transformation: substitution of (19) into (13) yields
$$f\left(\theta_{1}, \theta_{2}\right)=\frac{f\left(\theta_{1}\right) f\left(\theta_{2}\right)}{f^{2}(0)} \frac{\int_{0}^{\pi} \sin \theta \mathrm{d} f^{2}(\theta)}{\int_{0}^{\pi} \sin \theta \mathrm{d} f^{2}(\theta)}\qquad(20)$$

This is true only when $f^{2}(0)=1$ , which holds because the normalization $A_{n}(\hat{z}, \hat{z})$  $=1$ implies $f(0)=1$ .

In practice the iteration (13) has been performed by an $N(=16)$ gaussian integration which means that $B^{(n)}$ takes the form of an $N \times N$ matrix. The fixed

point $B_{ij}=f(i)f(j)$ usually was reached within 5 to 10 steps, depending on the value of the parameters. When $B^{(n)}(\theta_{1}, \theta_{2})$ has reached its fixed point the spins are no longer interacting but each is described by the same effective hamiltonian $H_{eff}$ that can be constructed as follows. We return to (4) for $N$ spins

$$
Q_{N}(K, k)=\int \cdots \int \mathrm{d} \boldsymbol{S}_{1} \cdots \mathrm{d} \boldsymbol{S}_{N} A_{0}\left(\boldsymbol{S}_{1}, \boldsymbol{S}_{2}\right) \cdots A_{0}\left(\boldsymbol{S}_{N}, \boldsymbol{S}_{1}\right)
\tag{21}
$$

$$
\hat{f}=-\lim _{N \rightarrow \infty} \frac{1}{N} \log Q_{N}.
\tag{22}
$$

Now consider $A_{0}(S_{1}, S_{2})$ as the kernel of an integral equation

$$
\int A_{0}\left(\boldsymbol{S}_{1}, \boldsymbol{S}\right) \psi_{l, m}\left(\boldsymbol{S}_{1}\right) \mathrm{d} \boldsymbol{S}_{1}=\lambda_{l} \psi_{l, m}(\boldsymbol{S}), \quad m=1,2, \ldots, c_{l}
\tag{23}
$$

where $c_{l}$ is the degeneracy of the $l$th eigenvalue. Since $A_{0}(S_{1}, S_{2})$ as given by eq. (3) is symmetric, positive-definite and of Hilbert-Schmidt type, the largest eigenvalue is non-degenerate (except perhaps at $T=0$!). According to Fredholm theory we can write

$$
A_{0}\left(\boldsymbol{S}_{1}, \boldsymbol{S}_{2}\right)=\sum_{l m} \lambda_{l} \psi_{l, m}\left(\boldsymbol{S}_{1}\right) \psi_{l, m}^{*}\left(\boldsymbol{S}_{2}\right)
\tag{24}
$$

and so we have

$$
Q_{N}=\sum_{l} c_{l} \lambda_{l}^{N}=\lambda_{0}^{N}\left[c_{0}+\sum_{l=1}^{\infty} c_{l}\left(\frac{\lambda_{l}}{\lambda_{0}}\right)^{N}\right] \rightarrow \hat{f}=-\ln \lambda_{0}
\tag{25}
$$

as was already stated in the context of eq. (2). On the other hand we have upon substituting (24) into (21)

$$
Q_{N}=\sum_{l, m} \int \cdots \int \mathrm{d} \boldsymbol{S}_{1} \cdots \mathrm{d} \boldsymbol{S}_{N} \lambda_{l}\left|\psi_{l, m}\left(\boldsymbol{S}_{1}\right)\right|^{2}\left|\psi_{l, m}\left(\boldsymbol{S}_{2}\right)\right|^{2} \cdots \lambda_{l}\left|\psi_{l, m}\left(\boldsymbol{S}_{N}\right)\right|^{2}
\tag{26}
$$

which yields, since the $\psi_{l, m}$'s can be chosen to be orthonormal

$$
Q_{N} \rightarrow \lambda_{0}^{N}\left[\int \mathrm{d} \boldsymbol{S}\left|\psi_{0}(\boldsymbol{S})\right|^{2}\right]^{N}
\tag{27}
$$

so

$$
\mathscr{H}_{\text {eff }}=-\ln \lambda_{0}-\ln \left|\psi_{0}(\boldsymbol{S})\right|^{2}.
\tag{28}
$$

If $\psi_{0}(x), x=\cos \theta$, it does not depend on the angle $\phi$. Each eigenfunction of $A_{0}(S_{1}, S_{2})$ is also an eigenfunction of $A_{n}(S_{1}, S_{2})$ as is easily shown, only the values of $\lambda_{l}(K, k)$ may change. So now we have given a direct physical interpreta tion of the eigenfunction of the integral eq. (23): After a few iterations of the re normalization transformation (4) the system has gone over into a system of non-

![](./images/812446091659182080_1.jpg)

Fig. 1. $H_{eff}$ for $K=1.0$ for $k=0.0; 0.2; 0.4; 0.6; 0.8$ and 1.0, respectively the curves 0, 1, 2, 3, 4 and 5, versus $S^{z}$.

![](./images/812446091659182080_2.jpg)

Fig. 2. $H_{eff}$ for $K=5.0$ for $k=0.0; 1.0; 2.0; 3.0; 4.0$ and 5.0, respectively the curves 0. 1, 2, 3, 4 and 5, versus $S^{z}$.

![](./images/812446091659182080_3.jpg)

**Fig. 4.** $H_{\text{eff}}$ for $K = -1.0$ for $k = 0.0; -0.2; -0.4; -0.6; -0.8$ and $-1.0$, respectively the curves 0, 1, 2, 3, 4 and 5, versus $S^z$.

![](./images/812446091659182080_4.jpg)

**Fig. 3.** $H_{\text{eff}}$ for $K = -5.0$ and $k = 0.0; -1.0; -2.0; -3.0; -4.0$ and $-5.0$, respectively the curves 0, 1, 2, 3, 4, 5, versus $S^z$.
Note the qualitative difference from the curves in fig. 1, 2 and 4.

interacting spins, each described by the effective hamiltonian (28). This effective hamiltonian, which by rotational invariance depends only on $S^{z}$, has been plotted for several values of $K$ and $k$ in figs. 1, 2, 3 and 4. A striking result is that in most cases, except e.g. $K=5.0, k>2.0$ or $J / H>2.5, H_{eff }$ depends almost inearly on $S^{z}$ and the magnetization is automatically given by the Langevin function.

Now it is also clear what the connection of this renormalization group is with the transfer matrix method. In essence, they are exactly the same: *For the renor- malization approach one constructs successive transformations (13) and (14) start- ing with $A_{0}(S_{1}, S_{2})$ from which a rapidly converging series (18) for the free energy is formed, whereas for the transfer matrix method $A_{0}(S_{1}, S_{2})$ is the kernel of the integral equation of which the highest eigenvalue directly yields the free energy $\hat{f}=-\ln \lambda_{0}$ and the corresponding eigenfunction defines an effective hamiltonian according to (28).

As has already been remarked, the fact, that $H_{eff }(K, k)$ depends on the initial parameters, finds its physical reflection in the property that the magnetization per spin is conserved under this decimation transformation.

*Proof of the invariance of the magnetization.* Let $m$ be the magnetization per spin for the original system of $2 N$ spins and $m^{\prime}$ the magnetization per spin after the first renormalization transformation. So by (4) we have

$$
\begin{aligned}
m^{\prime}= & \frac{1}{N} \int \cdots \int\left(\sum_{i=1}^{N} S_{i}^{\prime z}\right) \prod_{j=1}^{N} A_{1}\left(S_{2 j}^{\prime}, S_{2(j+1)}^{\prime}\right) \mathrm{d} S_{2 j}^{\prime} \\
& \times\left\{\int \cdots \int \prod_{j=1}^{N} A_{1}\left(S_{2 j}^{\prime}, S_{2(j+1)}^{\prime}\right) \mathrm{d} S_{2 j}^{\prime}\right\}^{-1} \\
= & \frac{1}{N} \int \cdots \int\left(\sum_{i=1}^{N} S_{i}^{\prime z}\right) \prod_{j=1}^{N} A_{0}\left(S_{2 j}^{\prime}, S_{2 j+1}^{\prime}\right) A_{0}\left(S_{2 j+1}^{\prime}, S_{2 j+2}^{\prime}\right) \mathrm{d} S_{2 j}^{\prime} \mathrm{d} S_{2 j+1}^{\prime} \\
& \times\left\{\int \cdots \int \prod_{j=1}^{N} A_{0}\left(S_{2 j}^{\prime}, S_{2 j+1}^{\prime}\right) A_{0}\left(S_{2 j}^{\prime}, S_{2(j+1)}^{\prime}\right) \mathrm{d} S_{2 j}^{\prime} \mathrm{d} S_{2 j+1}^{\prime}\right\}^{-1} \quad(29)
\end{aligned}
$$

since $S_{i}^{\prime}$ can be identified with $S_{i}$ and since there is translational invariance (fac tor 2), this equals

$$
\begin{aligned}
= & \frac{1}{2 N} \int \cdots \int\left(\sum_{i=1}^{2 N} S_{i}^{z}\right) \prod_{j=1}^{2 N} A_{0}\left(S_{j}, S_{j+1}\right) \mathrm{d} S_{j} \\
& \times\left\{\int \cdots \int \prod_{j=1}^{2 N} A_{0}\left(S_{j}, S_{j+1}\right) \mathrm{d} S_{j}\right\}^{-1}=m
\end{aligned}
$$

or $m^{\prime}=m$. Since the magnetization is invariant under the first renormalization transformation it is by induction invariant under any iteration of this transforma- tion.

### 3. Discussion of the results

Blume, Heller and Lurie¹) have treated the classical Heisenberg chain in an external field by solving the integral eq. (23) numerically. For simplicity we shall adapt their notation to ours. As we have seen in eq. (10) the integration over $\phi$ can be performed explicitly, and they obtain the integral equation $(\cos \theta_{1}=x$, $\cos \theta_{2}=x')$

$$
\begin{aligned}
2 \pi \int_{-1}^{1} & \mathrm{~d} x^{\prime} \exp \left[K\left(x x^{\prime}-1\right)+k\left(x+x^{\prime}-2\right) / 2\right] I_{m}\left\{K\left[\left(1-x^{2}\right)\left(1-x^{\prime 2}\right)\right]^{\frac{1}{2}}\right\} \\
& \times \psi_{l, m}\left(x^{\prime}\right)=\lambda_{l} \psi_{l, m}(x).
\end{aligned}\tag{31}
$$

The integral over $x'$ is performed by $N_{\mathrm{I}}$-point gaussian integration, using the expression

$$
\int_{-1}^{1} f(x) \mathrm{d} x \simeq \sum_{j=1}^{N_{\mathrm{I}}} w_{j} f\left(x_{j}\right)\tag{32}
$$

where the weights $w_{j}$ and the zeros $x_{j}$ of the Legendre polynomials are tabulated $^{14}$ ). Introducing

$$
\phi_{i}^{l, m}=w_{i}^{\frac{1}{2}} \psi_{l, m}\left(x_{i}\right)\tag{33}
$$

and

$$
\begin{aligned}
H_{i j}= & \left(w_{i} w_{j}\right)^{\frac{1}{2}} \exp \left[K\left(x x^{\prime}-1\right)+k\left(x+x^{\prime}-2\right) / 2\right] \\
& \times I_{0}\left\{K\left[\left(1-x^{2}\right)\left(1-x^{\prime 2}\right)\right]^{\frac{1}{2}}\right\}
\end{aligned}
$$

(where $m=0$ has been chosen because the eigenfunction belonging to the largest eigenvalue has no nodes). $H_{i j}$ is a symmetric matrix and (31) turns approximately into a matrix eigenvalue problem

$$
\sum_{j=1}^{N_{\mathrm{I}}} H_{i j} \phi_{j}^{l, m}=\lambda_{l} \phi_{i}^{l, m}.\tag{34}
$$

In ref. $1 N_{\mathrm{I}}$ is taken to be 16 (as in our calculations) and convergence to seven significant figures for all values of $K$ and $k$ for which calculations were done is obtained. We obtain agreement up to seven significant figures when the integral in (10) is calculated with an $N_{\mathrm{I}}=16$ point calculation and the free energy is calculated by the renormalization transformation via the series (18). So, for the thermodynamic properties of (1) there is a complete agreement with ref. 1, and there is no need to go further into that.

TH.W. RUIJGROK AND TH. NIEMEIJER

Apart from a numerical determination of $\lambda_{0}$, Blume et al. used a variational approximation for finding $\lambda_{0}$ by using an appropriately chosen trial function for $\psi_{0}$. In fact they choose
$$\psi_{0}(x)=\mathrm{e}^{b x}\qquad(35)$$
with $b$ as variational parameter, since this form is correct for $k=0$ ($b=0$) and $K=0$ ($b=k / 2$). After some calculations they then find for the magnetization per spin
$$m_{\mathrm{var}}=\operatorname{coth} 2 b-\frac{1}{2 b}\qquad(36)$$
without remarking that this is precisely the Langevin function for uncoupled clas- sical spins. From our renormalization results it is of course directly clear that this should be so, since inserting (35) into (28) yields
$$\mathscr{H}_{\mathrm{eff}}=-\lambda_{0}-\ln \left(\mathrm{e}^{b x}\right)^{2}=-\lambda_{0}-2 b x\qquad(37)$$
which is nothing but a Zeeman energy, apart from the factor $\lambda_{0}$ that does not in fluence the magnetization, which automatically gives rise to a Langevin function for the magnetization. The factor 2 in (36) is due to the squaring in eq. (37).

From figs. 1, 2 and 4 it is seen from the straightness of the lines that the choice $\psi_{0}(x)=e^{b x}$ is quite good for the ranges of $K$ and $k$ that we have considered. It is only in fig. $3, K=-5.0$ , i.e. low temperatures and antiferromagnetic coupling, that a marked deviation from the linear behaviour becomes apparent somewherebetween curves 1 and 2 . For curve 1 we have $\mu H / J=\frac{1}{3}$ and for curve $2, \mu H / J$  $=\frac{2}{3}$ , so deviations from the linear behaviour are found for $\mu H / J >rsim 0.3$ , whereas,on the contrary, Blume et al. claim that deviations are to be expected for $\mu H / J$  $\lesssim 1$ .

In the same computer program we have fitted $H_{eff }$ with the method of least squares by a parabola
$$H_{\mathrm{eff}} \simeq a x^{2}+b x+c.\qquad(38)$$

The standard error of this estimate is given by the expression
$$\chi=\left[\frac{1}{27} \sum_{i=1}^{30}\left(H_{\mathrm{eff}}\left(x_{i}\right)-a x_{i}^{2}-b x_{i}-c_{i}\right)\right]^{\frac{1}{2}}.\qquad(39)$$

The numerator preceding the summation sign is the number of points $x_{i}$ , viz.30 equidistant points on the interval $[-1,+1]$ minus the number of fitting para meters, i.e. 3. In fig. 5 we have plotted a, b and c for K = 1.0 and -1.0 versus k in the interval $[0,1]$ , obviously $b \gg a$ . In fig. 6 we have plotted a, b and c for

$K = 5.0$ and $-5.0$ versus $k$ in the interval $k = [0, 5]$. Here one can see by the enhanced value of $a$ compared to $b$ that $H_{\text{eff}}$ begins to look more like a part of a parabola than a straight line. In table I we give the maximum value of $\chi$ as a function of $k$ in the interval under consideration for the values $K = 5.0, 1.0, -1.0, -5.0$.

![](./images/812446091659182080_5.jpg)

Fig. 5. The fitting parameters $a_j$, $b_j$ and $c_j$, where $j = \pm 1$, for $H_{\text{eff}} \simeq a_j S^{z^2} + b_j S^z + c_j$, for $K = j$, versus $k$.

<table>
<caption>TABLE I
The value of $\chi$ where the parabolic fit is worst</caption>
<thead>
<tr>
<th>$K$</th>
<th>$k$ for $\chi(k)_{\text{max}}$</th>
<th>$\chi$</th>
</tr>
</thead>
<tbody>
<tr>
<td>5.0</td>
<td>5.0</td>
<td>0.167</td>
</tr>
<tr>
<td>1.0</td>
<td>1.0</td>
<td>$0.118 \times 10^{-3}$</td>
</tr>
<tr>
<td>$-1.0$</td>
<td>1.0</td>
<td>$0.272 \times 10^{-4}$</td>
</tr>
<tr>
<td>$-5.0$</td>
<td>5.0</td>
<td>0.091</td>
</tr>
</tbody>
</table>

It can be seen from the smallness of the number $\chi$ in table I that the parabolic fit is quite good. Blume et al. arrive at the same conclusion after "cumbersome" calculations, namely that it is best to take $\exp(-ax^2 - bx)$ as a trial function for the largest eigenfunction of eq. (23) and determine an upperbound for $\lambda_0$ by

varying $a$ and $b$. This is obviously what we have done explicitly in figs. 5 and 6 in the context of the renormalization theory. Once $a$, $b$ and $c$ are known it is an easy matter to determine the magnetization and susceptibility analytically.

![](./images/812446091659182080_6.jpg)

Fig. 6. The fitting parameters $a_{i}$, $b_{i}$ and $c_{i}$, where $i=\pm 5$, for $H_{\text{eff}} \sim a_{i}S^{z^{2}}+b_{i}S^{z}+c_{i}$, for $K=i$, versus $k$.

## References
1) M.Blume, P.Heller and N.A.Lurie, Phys. Rev. **B11** (1975) 4483.
2) L.J.de Jongh and A.R.Miedema, Adv. Phys. **23** (1974) 1.
J.Skalyo Jr., G.Shirane, J.A.Friedberg and H.Kobayashi, Phys. Rev. **B2** (1970) 4632.
M.T.Hutchings, G.Shirane, R.J.Birgenau and S.L.Holt, Phys. Rev. **B5** (1972) 1999.

3) See *e.g.* E. H. Lieb and D. C. Mattis, Mathematical Physics in One Dimension (Academic Press, New York, 1966).

5) E. Lieb, T. D. Schultz and D. C. Mattis, Ann. of Phys. **16** (1961) 407.

6) Th. Niemeijer, Physica **36** (1967) 377.

7) M. E. Fisher, Amer. J. Phys. **32** (1964) 343.

8) A. K. Rajagopal, Proc. Indian Acad. Sci. **A78** (1973) 13.

9) G. S. Joyce, Phys. Rev. **155** (1967) 478.

10) Th. Niemeijer and Th. W. Ruijgrok, Physica **88A** (1975) 174.

11) L. P. Kadanoff and A. H. Houghton, Phys. Rev. **B11** (1975) 377.

12) T. L. Bell and K. G. Wilson, Phys. Rev. **B10** (1974) 3935.

13) Subbarao, Phys. Rev. (1976) preprint.

14) Handbook of Mathematical Functions, M. Abramowitz and I. A. Stegun, eds. (N.B.S., Washington, 1964).

15) B. R. Martin, Statistics for Physicists, (Academic Press, New York, 1971).