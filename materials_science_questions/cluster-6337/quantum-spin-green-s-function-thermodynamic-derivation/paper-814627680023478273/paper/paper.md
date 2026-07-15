# Open Heisenberg chain under boundary fields: A magnonic logic gate
Gabriel T. Landi*
Departamento de Ciências Naturais e Humanas, Universidade Federal do ABC, 09210-580 Santo André, Brazil

Dragi Karevski
Institut Jean Lamour, Department P2M, Groupe de Physique Statistique, Université de Lorraine, CNRS, Boîte Postale 70239, F-54506 Vandoeuvre les Nancy Cedex, France

(Received 29 January 2015; revised manuscript received 23 April 2015; published 20 May 2015)

We study the spin transport in the quantum Heisenberg spin chain subject to boundary magnetic fields and driven out of equilibrium by Lindblad dissipators. An exact solution is given in terms of matrix product states, which allows us to calculate exactly the spin current for any chain size. It is found that the system undergoes a discontinuous spin-valve-like quantum phase transition from ballistic to subdiffusive spin current, depending on the value of the boundary fields. Thus, the chain behaves as an extremely sensitive magnonic logic gate operating with the boundary fields as the base element.

DOI: 10.1103/PhysRevB.91.174422
PACS number(s): 75.10.Pq, 02.30.Ik, 05.60.Gg, 75.10.Jm

## I. INTRODUCTION
One of the fundamental issues in condensed-matter physics is the determination of macroscopic parameters from the underlying microscopic properties. For systems in equilibrium, the Gibbsian approach gives an elegant solution since it depends only on the underlying microscopic energy spectrum. However, even if substantial progress has recently been made in understanding nonequilibrium systems, in particular through the so-called fluctuation theorems [1–5], no such approach is available for systems in a nonequilibrium steady state (NESS), characterized by the existence of steady currents. This forces one to resort to a full dynamical calculation in order to extract steady-state parameters. Such difficulty is inherent in nonequilibrium systems, dating back to Drude's calculation of the electrical conductivity of metals in 1900 [6]. As another example, we note the recent discussions concerning the microscopic derivation of Fourier's law in insulating crystals [7–11].

A more thorough understanding of the NESS is also essential for the development of several applications in phononics [12–14], spintronics [15–18], and magnonics [19,20]. We point, in particular, to two recent remarkable papers by Chumak et al. [20] and Oltscher et al. [18]. In Ref. [20] the authors report on a magnonic logic gate, where the magnon current is adjusted by controlling the number of magnon scattering processes induced by an auxiliary magnon injector (the base). In a different setting the authors in Ref. [18] study the transport of spin-polarized current in a two-dimensional electron gas. They observe the existence of a ballistic spin flow, in stark disagreement with classical predictions.

The transport properties reported in Refs. [18,20] both involve the presence of a NESS. Moreover, they share in common the fact that they cannot be explained by classical theories, thus requiring a full quantum treatment. On the theoretical side, these quantum NESSs are usually implemented on one-dimensional lattice spin systems coupled to external reservoirs [14,21–30]. The effect of the reservoirs is quite often described by a nonunitary Lindblad dynamical equation [31,32]. However, these models, being quantum many-body problems, can seldom be solved exactly, and from a numerical point of view they can usually be solved only for small lattices.

The purpose of this paper is to study the transport properties in the NESS of the one-dimensional Heisenberg chain coupled to two Lindblad reservoirs at each end that is also subject to magnetic fields at its boundaries. Remarkably, the steady state of this model is exactly expressible in terms of a matrix product state [26,27] involving operators satisfying the SU(2) algebra (in the case of an XXZ chain this generalizes to the quantum $U_q$[SU(2)] algebra [27]). This provides a method to compute the steady-state spin current $J$ for any chain size [28]. We will show that depending on the strength of the applied magnetic field, $J$ may undergo a discontinuous spin-valve-like quantum phase transition from ballistic to subdiffusive [$J \sim 1/N^2$; see Fig. 3(d) below]. As we shall discuss, the origin of this transition is related to the entrapment of magnons inside the chain caused by the boundary fields, which, in turn, increase the number of magnon scattering events. We argue that our system may be used as an extremely sensitive magnonic logic gate operating with an external magnetic field as the base element.

## II. DESCRIPTION OF THE MODEL
We consider the isotropic Heisenberg spin-1/2 chain with $N$ sites described by the Hamiltonian

$$
H = \frac{1}{2} \sum_{i=1}^{N-1} \left( \sigma_i^x \sigma_{i+1}^x + \sigma_i^y \sigma_{i+1}^y + \sigma_i^z \sigma_{i+1}^z \right) + h \left( \sigma_1^z - \sigma_N^z \right),
\tag{1}
$$

where the $\sigma$'s are the usual Pauli matrices. The last term describes the Zeeman interaction experienced by the boundary spins with a field pointing in the $z$ direction on the first site and in the $-\boldsymbol{n}_v = (\sin\theta, 0, -\cos\theta)$ direction on the last site. Note that with this parametrization the boundary fields point in opposite directions when $\theta = 0$.

The chain is coupled to two reservoirs at each end such that its density matrix $\rho$ is governed by the Lindblad master

*gtlandi@gmail.com

1098-0121/2015/91(17)/174422(6)
174422-1
©2015 American Physical Society

![](./images/814627680023478273_1.jpg)

FIG. 1. (Color online) Schematic drawing of the dissipators $D_{L,R}(\rho)$ (black solid arrows) and the boundary fields $h$ (red dashed arrows) acting on the first and last spins of the chain. In (a) the fields are in the same direction as the dissipators ($h>0$), and in (b) the fields act in directions opposite to the dissipators ($h<0$).

equation [32],
$$
\frac{d \rho}{d t}=-i[H, \rho]+D_{L}(\rho)+D_{R}(\rho), \quad(2)
$$
where the left and right dissipators $D_{L(R)}$ are given by
$$
D_{\alpha}(\rho)=\sum_{r= \pm} 2 K_{r}^{\alpha} \rho K_{r}^{\alpha \dagger}-\left\{K_{r}^{\alpha \dagger} K_{r}^{\alpha}, \rho\right\}, \quad(3)
$$
with $K_{ \pm}^{L}=\sqrt{\gamma(1 \mp f)} \sigma_{ \pm}^{ \pm}$ and $K_{ \pm}^{R}=\sqrt{\gamma(1 \mp f)} \sigma_{N}^{v \pm}$ and where $\sigma_{N}^{v \pm}$ are the ladder operators in the $n_{v}$ direction. Explicitly, one has $\sigma_{N}^{v-}=(\cos \theta \sigma_{N}^{x}-i \sigma_{N}^{y}+\sin \theta \sigma_{N}^{z}) / 2$ for the lowering operator and the adjoint expression for the raising one.

The forcing term $f \in[0,1]$ describes the polarization of the spin reservoirs and is related to a reservoir inverse temperature $\beta$ by $f=\tanh (\beta)$. At $f=1$ (zero temperature) the left bath corresponds to a perfect magnon source, pumping magnons into the system at a rate $\gamma$, while the right dissipator is a perfect drain, absorbing magnons at the same rate. We shall concentrate mostly on $f=1$, although $f<1$ will be discussed briefly. Note that when $h>0(<0)$ the boundary fields point in the same (opposite) direction as the dissipators (Fig. 1).

### III. OUTLINE OF THE MATRIX PRODUCT STATE SOLUTION

The unique NESS attained by the system at long times is the solution of Eq. (2) with $d \rho / d t=0$:
$$
i[H, \rho]=D_{L}(\rho)+D_{R}(\rho). \quad(4)
$$

At $f=1$ the exact solution was found in Ref. [27] in terms of a matrix product state (MPS), as we now outline. The first step is to note that since $\rho$ is a Hermitian positive semidefinite operator, we may use the following parametrization:
$$
\rho=\frac{S S^{\dagger}}{\operatorname{tr}\left(S S^{\dagger}\right)}. \quad(5)
$$

For a Heisenberg chain made of $N$ spin-1/2 sites, the operator $S$ lives in the Hilbert space $\mathfrak{H}=\mathbb{C}^{2^{N}}$.

We now use the ansatz that $S$ can be described by a matrix product state:
$$
S=\left\langle\phi\left|\Omega^{\otimes N}\right| \psi\right\rangle, \quad(6)
$$
where $\Omega$ is a $2 \times 2$ matrix with operator-valued entries
$$
\Omega=\left(\begin{array}{cc}
S_{z} & S_{+} \\
S_{-} & -S_{z}
\end{array}\right)=S_{z} \sigma^{z}+S_{+} \sigma^{+}+S_{-} \sigma^{-}. \quad(7)
$$

The operators $S_{a}$ live in an auxiliary space $\mathfrak{A}$ so that $\Omega^{\otimes N} \in$ $\mathfrak{H} \otimes \mathfrak{A}$. After contracting with $|\phi\rangle$ and $|\psi\rangle$ we recover $S \in \mathfrak{H}$. From the bulk structure of the Hamiltonian (1), it can be shown that if Eq. (6) is to be a solution, then the operators $S_{a}$ must obey the $\mathrm{SU}(2)$ algebra:
$$
\left[S_{z}, S_{ \pm}\right]= \pm S_{ \pm}, \quad(8)
$$
$$
\left[S_{+}, S_{-}\right]=2 S_{z}. \quad(9)
$$

The proper representation of the algebra to be explicitly used in the MPS solution is specified by a complex representation parameter $p$ which is fixed by substituting Eqs. (6) and (5) into the steady-state equation (4) and solving the resulting equations. It turns out that it is fixed by a lowest-weight condition: $\langle\phi| S_{z}=p\langle\phi|$, where $\langle\phi| \equiv\langle 0|$ is a lowest-weight state of the representation. Explicitly, in terms of a semi-infinite set of states $\{|n\rangle\}_{n=0}^{\infty}$ one has the irreducible representations
$$
S_{z}=\sum_{n=0}^{\infty}(p-n)|n\rangle\langle n|, \quad(10)
$$
$$
S_{+}=\sum_{n=0}^{\infty}(n+1)|n\rangle\langle n+1|, \quad(11)
$$
$$
S_{-}=\sum_{n=0}^{\infty}(2 p-n)|n+1\rangle\langle n|. \quad(12)
$$

Notice that for half-integer values of $p$ these representations reduce to the usual finite-dimensional representations of $\mathrm{SU}(2)$. In the present case, the representation parameter turns out to be
$$
p=\frac{i}{2(\gamma-i h)}, \quad(13)
$$
which fixes the associated infinite-dimensional representation of $\mathrm{SU}(2)$. The right state $|\psi\rangle$ over which $\Omega^{\otimes N}$ is evaluated is given by the coherent state
$$
|\psi\rangle=\sum_{n=0}^{\infty} \psi^{n}\left(\begin{array}{c}
2 p \\
n
\end{array}\right)|n\rangle, \quad \psi=-\tan (\theta / 2). \quad(14)
$$

Including these results in Eqs. (6) and (5) gives a complete solution for the density matrix of the steady state.

From this general solution it is possible to compute the expectation value of any local observable [28], the most important of which is the spin current $J_{i}$ leaving site $i$ toward site $i+1$. It is defined from the continuity equation
$$
\frac{d\left\langle\sigma_{i}^{z}\right\rangle}{d t}=J_{i-1}-J_{i},
$$

where
$$J_{i}=\left\langle\sigma_{i}^{x} \sigma_{i+1}^{y}-\sigma_{i}^{y} \sigma_{i+1}^{x}\right\rangle.$$

These equations are valid for $i=2, \ldots, N-1$. Slightly different equations apply to the boundaries. In the steady state $d\langle\sigma_{i}^{z}\rangle/dt = 0$, which gives
$$J_{1}=J_{2}=\cdots=J_{N}:=J.$$

The expectation value of an arbitrary observable $A$ may be computed as
$$\langle A\rangle=\operatorname{tr}(A \rho)=\frac{\operatorname{tr}\left(S^{\dagger} A S\right)}{\operatorname{tr}\left(S^{\dagger} S\right)}.$$

Our strategy will be to first trace over the Hilbert space and write everything in terms of expectation values on the auxiliary space. But note that $S$ and $S^{\dagger}$ will each contain an auxiliary space. So when we write $SS^{\dagger}$, we must double our auxiliary space. That is, we write
$$S S^{\dagger}=\left\langle 0,0\left|\Omega(p) \Omega^{\mathrm{T}}\left(p^{*}\right)\right| \psi, \psi^{*}\right\rangle,$$
where $\Omega(p)$ and $\Omega^{\mathrm{T}}(p^{*})$ act on different auxiliary spaces. Moreover, $|\psi^{*}\rangle$ is defined as $|\psi\rangle$ in Eq. (14), but with $p^{*}$ instead of $p$. Similarly, $\Omega^{\mathrm{T}}(p^{*})$ is defined in a way similar to Eq. (7):
$$\Omega^{\mathrm{T}}\left(p^{*}\right):=T_{z} \sigma^{z}+T_{+} \sigma^{-}+T_{-} \sigma^{+},$$
where the operators $T_{a}$ are defined with $p^{*}$ instead of $p$. Moreover, they commute with $S_{a}$ since they act on different auxiliary spaces.

Next define
$$B_{a}=\operatorname{tr}\left[\sigma^{a} \Omega(p) \Omega^{\mathrm{T}}\left(p^{*}\right)\right], \quad a \in\{0, x, y, z\}.\qquad(15)$$

Explicitly, we have
$$B_{0}=2 S_{z} T_{z}+S_{+} T_{+}+S_{-} T_{-},\qquad(16)$$

$$B_{x}=\left(S_{-}-S_{+}\right) T_{z}+S_{z}\left(T_{-}-T_{+}\right),\qquad(17)$$

$$B_{y}=i\left[S_{z}\left(T_{-}+T_{+}\right)-\left(S_{-}+S_{+}\right) T_{z}\right],\qquad(18)$$

$$B_{z}=S_{+} T_{+}-S_{-} T_{-}.\qquad(19)$$

The spin current may then be written as
$$J_{i}=\frac{1}{Z(N)}\left\langle 0,0\left|B_{0}^{i-1}\left[B_{x}, B_{y}\right] B_{0}^{N-i-1}\right| \psi, \psi^{*}\right\rangle,$$
where $Z(N)$ is the normalization constant,
$$Z(N)=\operatorname{tr}(\rho)=\left\langle 0,0\left|B_{0}^{N}\right| \psi, \psi^{*}\right\rangle.\qquad(20)$$

The explicit computation of $Z(N)$ requires constructing the matrix
$$\left(B_{0}\right)_{k, \ell}=2|p-k|^{2} \delta_{k, \ell}+\ell^{2} \delta_{k, \ell-1}+|2 p-\ell|^{2} \delta_{k, \ell+1}.$$

We then have
$$Z(N)=\sum_{k=0}^{N}\left(B_{0}^{N}\right)_{0, k} \tan ^{2 k}(\theta / 2)\left|\left(\begin{array}{c}
2 p \\
k
\end{array}\right)\right|^{2}.$$

In particular, when $\theta=0$, one has simply $Z(N)=(B_{0}^{N})_{0,0}$.

It can be further shown that
$$\left[B_{x}, B_{y}\right]=2 i\left(T_{z}-S_{z}\right) B_{0}$$
and that $T_{z}-S_{z}$ commutes with $B_{0}$. This reflects the translational symmetry of $J_{i}$ in the steady state. Hence, making use of Eq. (10), we arrive at
$$J=\frac{2 \gamma}{\gamma^{2}+h^{2}} \frac{Z(N-1)}{Z(N)}.\qquad(21)$$

This is the required formula for the steady-state magnetization flux. In the present model $J$ is a function of only $N, h, \gamma$, and $\theta$. Equation (21) must be computed for each $N$. Even though this may be done exactly, the formulas become extremely cumbersome for large sizes. On the other hand, computing $J$ numerically is now a trivial task.

Also of interest is the magnon density $\langle n_{i}\rangle=(1+\langle\sigma_{i}^{z}\rangle)/2$. A calculation similar to that above leads to
$$\left\langle\sigma_{i}^{z}\right\rangle=\frac{\left\langle 0,0\left|B_{0}^{i-1} B_{z} B_{0}^{N-i}\right| \psi, \psi^{*}\right\rangle}{Z(N)}.\qquad(22)$$

## IV. RESULTS

We now discuss the behavior of $J$ as a function of $N, h, \gamma$, and $\theta$. The focus will be on the case $f=1$, for which the MPS solution is valid. However, the case $f<1$ will be discussed briefly.

We begin with $\theta=0$ and $h=0$. The spin current as a function of $N$ and $\gamma$ is presented in Fig. 2. In order to interpret these results, recall that magnons are constantly being pumped at the left source, then propagate through the lattice, and are eventually collected in the right drain. The spin current is then simply proportional to the number of magnons being collected at the right drain. This number depends on two things: (i) the number of magnons being injected per unit time in the left source, which is proportional to $\gamma$, and (ii) the magnon scattering events during the trip to the right drain. In standard electrical conduction (e.g., in Drude's model), the electrons scatter with lattice imperfections or phonons. Since the number of scattering agents scales proportionally to $N$, we then have a diffusive current $J \sim 1/N$. In our case the magnons do not scatter with lattice imperfections. They either travel through unimpeded, or they participate in four-magnon scattering events (where two magnons scatter, producing two new magnons in the process [33]). When $\gamma$ is sufficiently

![](./images/814627680023478273_2.jpg)

FIG. 2. (Color online) Spin current $J$ for $f=1$, $\theta=0$, and $h=0$. (a) $J$ vs $\gamma$ for different sizes $N$. (b) $J$ vs $N$ for different values of $\gamma$. The dotted black line has a slope of $-2$.

![](./images/814627680023478273_3.jpg)

FIG. 3. (Color online) Spin current $J$ as a function of the boundary fields $h$ with $f=1$ and $\theta=0$. (a) $N^{2}J$ vs $h$ for $\gamma=1$ and different values of $N$. (b) $J/\gamma$ vs $h$ for $N=100$ and different values of $\gamma$ around $\gamma^{*}=1/N=0.01$. (c) and (d) $J/\gamma$ vs $h$ for $\gamma=10^{-5}$ and different values of $N$. The dashed lines in (d) correspond to Eq. (24).

small, the density of magnons in the chain is very small, thus making these events very rare. In this case $J$ will increase with $\gamma$ and will also be independent of $N$, i.e., ballistic. This is clearly observed in Fig. 2(a), where we see that the curves for different $N$ overlap when $\gamma$ is small. Conversely, in the high $\gamma$ limit the number of magnons, and hence the number of scattering events, will be significant. In this regime it is found [28] that $J$ is subdiffusive, behaving as $J\sim1/N^{2}$. The reason for this is that by doubling the size of the chain, we quadruple the number of four-magnon scattering events. As shown in Ref. [28], the transition between the ballistic and subdiffusive regimes occurs at

$$
\gamma^{*} \simeq \frac{1}{N}. \tag{23}
$$

A clear example of this transition is seen in the curve for $\gamma=10^{-2}$ in Fig. 2(b), where the regime changes abruptly from $J\sim1$ to $J\sim N^{-2}$ exactly at $N=100$.

Next we discuss the behavior for nonvanishing boundary fields, $h\neq0$, still keeping $\theta=0$. In Fig. 3(a) we present $N^{2}J$ vs $h$ for $\gamma=1$ (subdiffusive, high magnon density). As can be seen, even for moderately small sizes, the curves start to scale very well according to $J\sim1/N^{2}$. In this scaling region we have found that the current is very well described by

$$
J \simeq \frac{\pi^{2}}{\gamma N^{2}} \frac{1}{1+\frac{2 h}{\gamma^{2} N}+\frac{h^{2}}{\gamma^{2}}}, \tag{24}
$$

which is illustrated by the dashed line in Fig. 3(a). Note also that $J$ is asymmetric with respect to $h$; that is, the spin current is rectified [14].

![](./images/814627680023478273_4.jpg)

FIG. 4. (Color online) Spin current $J$ vs $h$ when $f<1$, computed using the exact diagonalization of Eq. (2) for $N=6$. (a) $\gamma=10^{-5}$. (b) $\gamma=1$. The dotted black lines correspond to the MPS solution when $f=1$.

The changes which occur as we reduce $\gamma$ below $\gamma^{*}$ are illustrated in Fig. 3(b), where we plot $J/\gamma$ vs $h$ for $N=100$ and different values of $\gamma$. As can be seen, there is a drastic behavioral transition from a bell-shaped structure at $\gamma>\gamma^{*}$ to a plateau at $\gamma<\gamma^{*}$. This plateau is illustrated in more detail in Figs. 3(c) and 3(d) for $\gamma=10^{-5}$ and different sizes. As can be seen, the plateau region is asymmetric with respect to $h$ and independent of size. It corresponds to the ballistic behavior of the spin current. As the field is increased, however, one eventually observes an abrupt transition to a much lower spin current. For positive fields the transition is continuous, whereas for negative fields it is discontinuous (strictly speaking, it is only discontinuous in the thermodynamic limit). The critical field where the plateau transition occurs is found from the simulations to be $h^{*}\simeq-5/N$. We also call attention to the fact that outside the plateau region, $J$ is again well described by Eq. (24), as illustrated by the dashed lines in Fig. 3(d). This indicates that for large fields the behavior is again subdiffusive.

The results presented so far were obtained from the exact MPS steady state, which is valid only at $f=1$ (zero temperature). However, the rich behavior of the current observed for $f=1$ also survives at finite temperatures, i.e., for $f<1$. This can be seen in Fig. 4, where we report the current $J$ vs $f$ as obtained from the exact numerical diagonalization [14] of Eq. (2) for $N=6$. The current as seen from the numerics shows basically the same features as in the MPS case: a bell-shaped behavior at high $\gamma$ and a sharp plateau at low $\gamma$ (for this small

![](./images/814627680023478273_5.jpg)

FIG. 5. (Color online) Small size effects in the spin current. (a) $J/\gamma$ vs $Nh$ for $\gamma=10^{-5}$ and different values of $N$. (b) $J/\gamma$ vs $Nh$ for $N=15$ and different values of $\gamma$.

174422-4

![](./images/814627680023478273_6.jpg)

FIG. 6. (Color online) $J$ vs $h$ for $N=500$ and different values of $\theta$ (as defined in Fig. 1). (a) $\gamma=10^{-4}$ and (b) $\gamma=1$.

size the plateau is not yet completely formed). In Fig. 4 we also plot the MPS solution when $f=1$ to illustrate the perfect agreement between both methods.

The gradual formation of the plateau as the size of the system increases in illustrated in Fig. 5(a). In Fig. 5(b) we show the changes which occur as one changes $\gamma$ when $N=15$. As can be seen in both images and in Fig. 3(c), when $N$ is small, the current presents a series of irregular and sharp resonances when $h<0$, at positions which vary with $N$ (such peaks have been observed recently in Ref. [34]). It is important to note, however, that these peaks appear only for $\gamma \leqslant 1 / N^{2}$ and therefore become vanishingly small for any moderately large size. This can be seen, for instance, by comparing the curves with $\gamma=10^{-4}$ and $\gamma=10^{-2}$ in Fig. 5(b). Both are practically identical, except for the peaks, which are present only when $\gamma=10^{-4}$. Note also that it follows from Eq. (21) that $J$ is bounded, so these cannot be $\delta$ peaks.

We consider now the case with a general twisting angle $\theta \in[0, \pi]$. Figure 6(a) shows $J$ vs $h$ for different values of $\theta$ with fixed size $N=500$ and $\gamma=10^{-4}$. As expected, $J \rightarrow 0$ as $\theta \rightarrow \pi$. However, remarkably, even for values of $\theta$ close to the undriven situation $\theta=\pi$, one still observes high values of $J$ for negative values of $h$, in a plateau region that shrinks as $\theta \rightarrow \pi$. Thus, by monitoring the twisting angle $\theta$, one can fine-tune the high-current plateau width. For completeness, we also show the behavior for large $\gamma$ in Fig. 6(b).

## V. DISCUSSION AND CONCLUSIONS

The remarkable and sharp transitions observed in the spin current, from ballistic (inside) to subdiffusive (outside the plateau), as the magnitude $|h|$ of the boundary fields is increased suggest that sufficiently high fields act as scattering barriers, impeding magnons from flowing through the system, from source to drain. This can also be seen by looking at the magnon density profile $\langle n_{i}\rangle=(1+\langle\sigma_{i}^{z}\rangle)/2$ plotted in Fig. 7 for $N=500, \gamma=10^{-5}$, and $\theta=0$. The red solid curve in Fig. 7(a) corresponds to the profile in the plateau (ballistic) region of Fig. 3(d). In this case, the distribution is flat, with $\langle n_{i}\rangle \simeq 1/2$, characteristic of a maximal current state. On the other hand, outside the plateau the profile is sine shaped, characteristic of the subdiffusive regime [26]. The transition between the two profiles is discontinuous for $h<0$ [Fig. 7(a)] and continuous for $h>0$ [Fig. 7(b)]. Hence, we conclude that the density of magnons inside the chain may also be adjusted by changing the boundary field $h$. Chumak et al. [20] used a similar idea to construct their magnonic logic gate. But in their case an additional source of magnons was responsible for changing the magnon current and the magnon density. Consequentially, the transition between the on and off states was in their case quite smooth. Here we see an extremely abrupt transition, thus being potentially more suited for a logic gate.

![](./images/814627680023478273_7.jpg)

FIG. 7. (Color online) Magnon density profile $\langle n_{i}\rangle=(1+$ $\langle\sigma_{i}^{z}\rangle)/2$ for different values of $h$, with $N=500, \gamma=10^{-5}$, and $\theta=0$. (a) $h<0$ near the plateau transition [see Fig. 3(d)]. (b) $h>0$.

In what concerns an experimental realization of the present idea, it is important to note that even though we studied a very specific situation, the underlying physical principles of our results are very general, based only on the entrapment of magnons by magnetic fields. Hence, similar results should be obtained in different field configurations which maintain the same principles. Most magnonic circuits are constructed using yttrium iron garnet (YIG), [19,35], which is well described by the Heisenberg model, albeit with a different spin value. The Lindblad generators then represent microstrip antennas which are used to generate and collect magnons [19,20]. Even though the Lindblad dissipators have been extensively used in the past to study open quantum systems, we are unaware of any papers mentioning this specific application of them as describing the injection and collection of magnons.

The energy and time units of the problem are set by the constant $\mathcal{J}$, which should appear in the first term of Eq. (1) but which we have throughout set as unity. According to Ref. [35], $\mathcal{J} \sim 10^{-22}$ J. The pumping rate $\gamma$ (measured in magnons per second) should operate below the critical value $\gamma^{*}$, which, in the correct units, reads $\gamma^{*}=\mathcal{J}/\hbar N \sim 10^{12}/N$ Hz. This gives the optimal value of $\gamma$ below which the flux should be ballistic. Letting $h=\mu_{B}B$, where $\mu_{B}$ is the Bohr magnetron, we find that the critical magnetic field $B^{*}$ where

the plateau transition occurs is, in correct units, $|B^{*}|(\mathrm{T}) \simeq \mathcal{J}/\mu_B N \simeq 10/N$. Hence, for any reasonable values of $N$, very small magnetic fields may suffice to induce the plateau transition.

In summary we have studied the quantum Heisenberg chain driven by two Lindblad baths and subject to two magnetic fields acting on each boundary. An exact solution was given in terms of matrix product states, which enables one to calculate local observables for any chain size. The system is seen to undergo a discontinuous transition from ballistic to subdiffusive spin current as a function of the field intensity. Thus, the system may function as an extremely sensitive magnonic logic gate using the boundary fields as the base.

## ACKNOWLEDGMENTS
The authors would like to acknowledge the São Paulo Research Foundation (FAPESP) and SPIDER for the financial support.

[1] D. J. Evans, E. G. D. Cohen, and G. P. Morriss, Phys. Rev. Lett. **71**, 2401 (1993); D. J. Evans and D. J. Searles, Phys. Rev. E **50**, 1645 (1994).

[2] G. Gallavotti and E. G. D. Cohen, Phys. Rev. Lett. **74**, 2694 (1995); J. Stat. Phys. **80**, 931 (1995);

[3] C. Jarzynski, Phys. Rev. Lett. **78**, 2690 (1997); Phys. Rev. E **56**, 5018 (1997); J. Stat. Phys. **98**, 77 (2000).

[4] G. E. Crooks, J. Stat. Phys. **90**, 1481 (1998); Phys. Rev. E **61**, 2361 (2000).

[5] P. Talkner, E. Lutz, and P. Hänggi, Phys. Rev. E **75**, 050102 (2007); P. Talkner, M. Campisi, and P. Hänggi, J. Stat. Mech. (2009) P02025; M. Campisi, P. Hänggi, and P. Talkner, Rev. Mod. Phys. **83**, 771 (2011).

[6] P. Drude, Ann. Phys. (Berlin, Ger.) **306**, 566 (1900).

[7] Z. Rieder, J. L. Lebowitz, and E. Lieb, J. Math. Phys. **8**, 1073 (1967).

[8] M. Bolsterli, M. Rich, and W. M. Visscher, Phys. Rev. A **1**, 1086 (1970).

[9] D. Manzano, M. Tiersch, A. Asadian, and H. J. Briegel, Phys. Rev. E **86**, 061118 (2012); A. Asadian, D. Manzano, M. Tiersch, and H. J. Briegel, *ibid.* **87**, 012109 (2013).

[10] G. T. Landi and M. J. de Oliveira, Phys. Rev. E **87**, 052126 (2013); **89**, 022105 (2014).

[11] D. Karevski and T. Platini, Phys. Rev. Lett. **102**, 207207 (2009); T. Platini, R. J. Harris, and D. Karevski, J. Phys. A **43**, 135003 (2010).

[12] M. Terraneo, M. Peyrard, and G. Casati, Phys. Rev. Lett. **88**, 094302 (2002); B. Li, L. Wang, and G. Casati, *ibid.* **93**, 184301 (2004).

[13] C. W. Chang, D. Okawa, A. Majumdar, and A. Zettl, *Science* **314**, 1121 (2006).

[14] G. T. Landi, E. Novais, M. J. de Oliveira, and D. Karevski, Phys. Rev. E **90**, 042142 (2014).

[15] S. A. Wolf, D. D. Awschalom, R. A. Buhrman, J. M. Daughton, S. von Molnár, M. L. Roukes, A. Y. Chtchelkanova, and D. M. Treger, *Science* **294**, 1488 (2001).

[16] S. Murakami, N. Nagaosa, and S.-C. Zhang, *Science* **301**, 1348 (2003).

[17] I. Žutić, J. Fabian, and S. Sarma, Rev. Mod. Phys. **76**, 323 (2004).

[18] M. Oltscher, M. Ciorga, M. Utz, D. Schuh, D. Bougeard, and D. Weiss, Phys. Rev. Lett. **113**, 236602 (2014).

[19] A. A. Serga, A. V. Chumak, and B. Hillebrands, J. Phys. D **43**, 264002 (2010).

[20] A. V. Chumak, A. A. Serga, and B. Hillebrands, *Nature Commun.* **5**, 4700 (2014).

[21] M. Bandyopadhyay and D. Segal, Phys. Rev. E **84**, 011151 (2011).

[22] G. Benenti, G. Casati, T. Prosen, D. Rossini, and M. Žnidarič, Phys. Rev. B **80**, 035110 (2009).

[23] M. Žnidarič, Phys. Rev. Lett. **106**, 220601 (2011); Phys. Rev. B **88**, 205135 (2013).

[24] T. Prosen and M. Žnidarič, Phys. Rev. B **86**, 125118 (2012).

[25] J. J. Mendoza-Arenas, S. Al-Assam, S. R. Clark, and D. Jaksch, J. Stat. Mech. (2013) P07007; J. J. Mendoza-Arenas, T. Grujic, D. Jaksch, and S. R. Clark, Phys. Rev. B **87**, 235130 (2013).

[26] T. Prosen, Phys. Rev. Lett. **107**, 137201 (2011); **106**, 217206 (2011).

[27] D. Karevski, V. Popkov, and G. M. Schütz, Phys. Rev. Lett. **110**, 047201 (2013).

[28] V. Popkov, D. Karevski, and G. M. Schütz, Phys. Rev. E **88**, 062118 (2013).

[29] V. Popkov and R. Livi, *New J. Phys.* **15**, 023030 (2013).

[30] Y. Yan, C.-Q. Wu, and B. Li, Phys. Rev. B **79**, 014207 (2009); L. Zhang, Y. Yan, C.-Q. Wu, J.-S. Wang, and B. Li, *ibid.* **80**, 172301 (2009).

[31] G. Lindblad, *Commun. Math. Phys.* **48**, 119 (1976).

[32] H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, New York, 2007), p. 636.

[33] The Heisenberg Hamiltonian prohibits three-magnon events since it conserves the number of excitations [36]. Events involving more than four magnons are, in principle, possible but much less likely. In real systems three-magnon events do exist as a consequence of more complex interactions (e.g., dipolar). However, as shown in Ref. [20], four-magnon events are the most relevant type, at least for YIG.

[34] Z. Lenarič and T. Prosen, Phys. Rev. E **91**, 030103(R) (2015).

[35] R. L. Douglass, Phys. Rev. **120**, 1612 (1960).

[36] A. G. Gurevich and G. A. Melkov, *Magnetization Oscillations and Waves* (CRC Press, Boca Raton, 1996).