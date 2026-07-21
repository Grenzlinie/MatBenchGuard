# Generalized commutators and deformation of strong coupling superconductivity

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

1993 J. Phys. A: Math. Gen. 26 4827

(http://iopscience.iop.org/0305-4470/26/19/016)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:
IP Address: 128.83.63.20
The article was downloaded on 22/06/2013 at 18:43

Please note that [terms and conditions apply].

# Generalized commutators and deformation of strong coupling superconductivity

Wei-Yeu Chen and Choon-Lin Ho
Department of Physics, Tamkang University, Tamsui, Taiwan 25137, Republic of China

Received 17 August 1992

**Abstract.** We consider quantum deformation of a strong-coupling superconductivity model based on creation/annihilation operators which satisfy generalized commutator relations. It is found that the nature of the superconducting phase transition can be changed from the usual second-order to a first-order transition, if the deformation parameter exceeds a certain critical value. Metastable normal and superconducting states can exist when the transition is of the first order.

The concept of quantum groups and algebras has its origin in the development of the quantum inverse method and the study of solutions to the Yang-Baxter equation [1]. These new mathematical structures have already found applications in exactly solvable statistical models [2] and in two-dimensional conformal field theories [3]. An interesting development in the theory of quantum groups is the realization of the quantum $SU_q(2)$ algebra in terms of creation and annihilation operators that satisfy a generalized commutator relation characterized by a parameter $q$. Such a harmonic oscillator is generally called a $q$-oscillator in the literature [4]. Many works immediately follow along the same line, including the construction of fermionic $q$-oscillators, and the $q$-oscillator realization of other quantum groups [5].

Although $q$-oscillators are usually treated as a means to realize various quantum groups, they are interesting objects in their own right. They can be viewed as creation and annihilation operators of particles obeying intermediate statistics, i.e. statistics that interpolate between Bose and Fermi statistics. It is therefore natural to study quantized field theory and many-body problems using these oscillators. Such studies, however, do not appear to have been attempted systematically (only a few works appear in the literature [6,7]). The purpose of this paper is to give an example of a $q$-deformed model of superconductivity and to discuss how its property changes according to the degree of deformation.

We consider a $q$-analogue of a strong coupling limit model of superconductivity discussed by Thouless in [8]. The model was first proposed by Wada *et al* and by Anderson [9]. Its Hamiltonian is

$$
H=T \sum_{i}\left(a_{i+}^{\dagger} a_{i+}+a_{i-}^{\dagger} a_{i-}\right)-J \sum_{i} \sum_{j} a_{i+}^{\dagger} a_{i-}^{\dagger} a_{j-} a_{j+} \tag{1}
$$

where $a_{i+}(a_{i+}^{\dagger})$ is the fermionic annihilation (creation) operator for a particle with momentum $i$ and spin up (+), and $a_{i-}(a_{i-}^{\dagger})$ is the fermionic annihilation (creation) operator for a particle with momentum $-i$ and spin down (-). $T$ and $J$ are positive constants. This

model can be exactly solved by transforming (1) into a $SU(2)$ spin model. In the case where $T$ is equal to the chemical potential of the system (which is the case corresponding to the situation considered in the BCS theory), it is found that the system undergoes a second-order phase transition into the superconducting state as the temperature decreases. We shall see later that the nature of the phase transition is changed by quantum deformation.

The operators $a_{i\pm}$ and $a_{i\pm}^{\dagger}$ are now treated as annihilation and creation operators of fermionic $q$-oscillators [5] satisfying the algebra with a real deformation parameter $q \equiv e^{\gamma}$:

$$
\begin{aligned}
&a_{i \pm} a_{i \pm}^{\dagger}+q a_{i \pm}^{\dagger} a_{i \pm}=q^{N_{i \pm}} \\
&a_{i \pm} a_{i \pm}^{\dagger}+q^{-1} a_{i \pm}^{\dagger} a_{i \pm}=q^{-N_{i \pm}} \\
&\left\{a_{i \alpha}, a_{j \beta}\right\}=\left\{a_{i \alpha}^{\dagger}, a_{j \beta}^{\dagger}\right\}=0 \quad \text { for any } i, j, \alpha, \beta(\alpha, \beta= \pm) \\
&\left\{a_{i \alpha}, a_{j \beta}^{\dagger}\right\}=0 \quad \text { for } i \neq j \\
&\left\{a_{i+}, a_{i-}^{\dagger}\right\}=0 \\
&{\left[N_{i \pm}, a_{i \pm}^{\dagger}\right]=a_{i \pm}^{\dagger} \quad\left[N_{i \pm}, a_{i \pm}\right]=-a_{i \pm}.}
\end{aligned}
\tag{2}
$$

Equation (2) implies that

$$
\begin{aligned}
&a_{i \pm}^{\dagger} a_{i \pm}=\frac{q^{N_{i \pm}}-q^{-N_{i \pm}}}{q-q^{-1}} \equiv\left[N_{i \pm}\right] \\
&a_{i \pm} a_{i \pm}^{\dagger}=\frac{q^{1-N_{i \pm}}-q^{N_{i \pm}-1}}{q-q^{-1}} \equiv\left[1-N_{i \pm}\right].
\end{aligned}
\tag{3}
$$

Eigenvalues of $N_{i\pm}$ are either 0 or 1. The Hamiltonian of a $q$-oscillator is given by

$$
\begin{aligned}
H_{i \pm} &\equiv \frac{1}{2}\left(a_{i \pm}^{\dagger} a_{i \pm}-a_{i \pm} a_{i \pm}^{\dagger}\right) \\
&=\frac{1}{2} \frac{q^{h_{i \pm}}-q^{-h_{i \pm}}}{q^{1 / 2}-q^{-1 / 2}} \\
&=\frac{\sinh \gamma h_{i \pm}}{2 \sinh (\gamma / 2)}
\end{aligned}
\tag{4}
$$

where $h_{i\pm} \equiv N_{i\pm} - \frac{1}{2}$.

As pointed out by Floratos [7] (for the case of bosonic $q$-oscillators), the $q$-analogue of the kinetic term of a Hamiltonian is not simply the sum of the Hamiltonian of each oscillator. The reason is this. There is a $U(M)$ symmetry ($M$ is the number of oscillators used to define the theory) in the kinetic part of (1). By simply taking the same form of the kinetic term in (1) for the $q$-oscillators, one does not get the corresponding quantum $U_q(M)$ symmetry in the Hamiltonian. Extending Floratos' construction to the fermionic case, we have to add the Hamiltonians of two $q$-oscillators, e.g. $H_{i+}$ and $H_{i-}$, in the following way

$$
\begin{aligned}
H &=H_{i+} q^{-h_{i-}}+q^{h_{i+}} H_{i-} \\
&=\frac{\sinh \gamma\left(h_{i+}+h_{i-}\right)}{2 \sinh (\gamma / 2)}
\end{aligned}
\tag{5}
$$

in order to preserve the $U_q(2)$ symmetry in this case.

This observation leads us to propose the following $q$-deformed version of the Hamiltonian (1)

$H = H_0 + H_1$

$$
\begin{aligned}
H_{0}= & T \sum_{i} q^{\sum_{j<i}\left(h_{j+}+h_{j-}\right)}\left(H_{i+} q^{-h_{i-}}+q^{h_{i+}} H_{i-}\right) q^{-\sum_{j>i}\left(h_{j+}+h_{j-}\right)} \\
H_{1}= & -J \sum_{i, j} q^{\sum_{k<i}\left(h_{k+}+h_{k-}\right) / 2} a_{i+}^{\dagger} a_{i-}^{\dagger} q^{-\sum_{k>i}\left(h_{k+}+h_{k-}\right) / 2} \\
& \times q^{\sum_{l<j}\left(h_{l+}+h_{l-}\right) / 2} a_{j-} a_{j+} q^{-\sum_{l>j}\left(h_{l+}+h_{l-}\right) / 2}.
\end{aligned}
\tag{6}
$$

It can be easily checked that

$$
H_{0}=T \frac{\sinh \left[\gamma \sum_{i}\left(h_{i+}+h_{i-}\right)\right]}{2 \sinh (\gamma / 2)}
\tag{7}
$$

as desired. The reason for the choice of the form of $H_{1}$ will become clear later.

We now show that the model described by (6) is equivalent to a quantum $SU_{q}(2)$ spin model. First we note that a pair of levels (levels with the opposite momentum and spin) will remain singly occupied, if it is occupied by only one particle at some time. This is so because there is no second particle for the one particle to scatter against, and no pair of particles can scatter into the levels owing to the 'exclusion principle' given by (2). Hence we can exclude all half-filled pairs of the levels from the sum in (6).

Taking the sum in (6) to be over all paired states, one can transform the model into an exactly solvable spin model. First define the operators $s_{i}^{+} \equiv a_{i+}^{\dagger} a_{i-}^{\dagger}, s_{i}^{-} \equiv a_{i-} a_{i+}$ and $s_{i}^{0} \equiv \frac{1}{2}(h_{i+}+h_{i-})$. Clearly $s_{i}^{+}$ and $s_{i}^{-}$ creates and annihilates, respectively, two particles in the $i$th pair of level. They satisfy

$$
\begin{aligned}
& \left(s_{i}^{+}\right)^{2}=\left(s_{i}^{-}\right)^{2}=0 \\
& {\left[s_{i}^{0}, s_{i}^{ \pm}\right]= \pm s_{i}^{ \pm} \quad\left[s_{i}^{+}, s_{i}^{-}\right]=\left[2 s_{i}^{0}\right]} \\
& {\left[s_{i}^{\alpha}, s_{j}^{\beta}\right]=0 \quad \text { for } i \neq j \quad \alpha, \beta=0, \pm .}
\end{aligned}
\tag{8}
$$

Thus the three operators $s_{i}^{0}, s_{i}^{ \pm}$ for the same index $i$ satisfy the quantum algebra $SU_{q}(2)$, and can be viewed as some kind of 'quantum spin' operators. Since $h_{i \pm}=\frac{1}{2}$ or $-\frac{1}{2}$ when $N_{i \pm}=1$ or 0 respectively, we see from the definition of $s_{i}^{0}$ that if the $i$th pair of levels is occupied (unoccupied) the corresponding 'spin' is up (down). We can add these spins as follows

$$
\begin{aligned}
& S^{0} \equiv \sum_{i} s_{i}^{0}=\frac{1}{2} \sum_{i}\left(h_{i+}+h_{i-}\right) \\
& S^{ \pm} \equiv \sum_{i} q^{\sum_{j<i} s_{j}^{0}} s_{i}^{ \pm} q^{-\sum_{j>i} s_{j}^{0}} .
\end{aligned}
\tag{9}
$$

These total spin operators again satisfy the $SU_{q}(2)$ quantum algebra. It is now obvious that (6) can be rewritten as

$$
H=T \frac{\sinh 2 \gamma S^{0}}{2 \sinh (\gamma / 2)}-J S^{+} S^{-}.
\tag{10}
$$

This shows the equivalence of the original Hamiltonian and a $SU_q(2)$ spin model.

The Hamiltonian $H$ in (10) can be diagonalized. The simultaneous eigenvalues of $S^0$ and $S^+S^-$ are $m$ and $[j+m][j-m+1]$ respectively, where $m$, $j$ are integers or half-integers ($m=-j,-j+1,...,j-1,j$). If the total number of completely filled and completely unfilled pairs of levels is $B$, then the largest value of $j$ is $j=\frac{1}{2}B$, and the total number of ways of making $j=\frac{1}{2}B-r$ is
$$
\frac{B!}{r!(B-r)!}-\frac{B!}{(r-1)!(B-r+1)!}=\frac{B!(B-2r+1)}{r!(B-r+1)!}. \tag{11}
$$

Suppose there are $D$ completely filled pairs in the system. Then $m=D-\frac{1}{2}B$. The eigenvalue of $H$ with $J=\frac{1}{2}B-r$ and $m=D-\frac{1}{2}B$ is
$$
E_{jm}=T\frac{\sinh 2\gamma(D-B/2)}{2\sinh(\gamma/2)}-J[D-r][B-r-D+1]. \tag{12}
$$

The condition $-j\leqslant m\leqslant j$ implies that $r$ is no greater than either $D$ or $B-D$. The degeneracy of this level is given by (11). For fixed $B$ and $D$, the ground state corresponds to $r=0$, and is non-degenerate.

Now that we have the complete energy spectrum of the system, we may proceed to study its statistical mechanical property. Suppose there are $Q$ half-filled pairs of levels. Then the total number of pairs in the system is $K=B+Q$. There are $K!/Q!(K-Q)!$ ways of choosing the $Q$ pairs, and $2^Q$ ways of filling one particle into each of them. The energy of each single particle is $T$ according to (1). The grand partition function is [10]
$$
\begin{aligned}
\mathcal{Z}=&\sum_{Q=0}^{K}\sum_{r=0}^{(K-Q)/2}\sum_{D=r}^{K-Q-r}\frac{2^Q K!(K-Q-2r+1)}{Q!r!(K-Q-r+1)!}\exp\left\{-\beta\left[T\frac{\sinh 2\gamma(D-B/2)}{2\sinh(\gamma/2)}\right.\right.\\
&\left.\left.-J\frac{\sinh\gamma(D-r)\sinh\gamma(K-Q-r-D+1)}{(\sinh\gamma)^2}-\mu(2D+Q)\right]\right\}. \tag{13}
\end{aligned}
$$

Here $\mu$ is the chemical potential. We are only interested in the case with $\mu=T$ which corresponds to superconductivity [8].

The sum in (13) is very difficult to evaluate, even in the non-deformed case. If the deformation parameter $\gamma$ is very small, we can adopt Thouless' argument. The region over which the sum is taken is a tetrahedron bounded by the planes $Q=0$, $r=0$, $D=r$, and $D+Q+r=K$. The number of points in this tetrahedron is equal to its volume $K^3/12$. If $\mathcal{Z}_0$ is the maximal value of the summand of (13), then we have $\mathcal{Z}_0<\mathcal{Z}<\mathcal{Z}_0K^3/12$. Since physical quantities are found from $\ln\mathcal{Z}/V$, where $V$ is the volume of the system, we can therefore take $\mathcal{Z}_0$ as a very good approximation of $\mathcal{Z}$. The error goes at most as $V^{-1}\ln V$, as the number of pairs $K$ is supposed to be proportional to the volume. To find the state of the system with the lowest free energy, it is sufficient to find the maximum of the summand. Setting the first derivatives of the summand with respect to $r$, $Q$ and $D$ to zero, one finds that the extremum of the summand occur at points satisfying
$$
\sqrt{\frac{K}{r}}-1=\exp\left\{\frac{1}{2}\beta J\frac{\gamma}{(\sinh\gamma)^2}\sinh\left[\gamma K\left(1-2\sqrt{\frac{r}{K}}\right)\right]\right\} \tag{14a}
$$

$$
Q=2(\sqrt{Kr}-r) \tag{14b}
$$

$$
2\beta\mu-\beta\gamma T\frac{\cosh\gamma(K-Q-2D)}{\sinh(\gamma/2)}+\beta\gamma J\frac{\sinh\gamma(K-Q-2D)}{\sinh^2\gamma}=0. \tag{14c}
$$

In the limiting case $\gamma \to 0$, (14a) and (14c) reduce to

$$
\sqrt{\frac{K}{r}}-1=\exp \left\{\frac{1}{2} \beta J K\left(1-2 \sqrt{\frac{r}{K}}\right)\right\} \tag{15a}
$$

$$
K-Q-2 D=0. \tag{15b}
$$

Equations (15), together with (14b), are the equations given in [8]. It is easy to see that $\sqrt{r / K}=\frac{1}{2}$ is always a solution to (15a) (and (14a) as well). This point, given by $(r=K / 4, Q=K / 2, D=K / 4)$, is just on the edge of the tetrahedron allowed for $r, Q$ and $D$, and is related to the 'normal' state of the system [8]. As the temperature decreases, the maximum stays at the same point until $\beta$ exceeds some critical value $\beta_{\mathrm{c}}$, after which the maximum lies inside the tetrahedron $(r<K / 4)$. This new maximum is taken to be related to the 'superconducting' state of the system. The critical temperature can be easily found by putting $\sqrt{r / K}=\frac{1}{4}-\delta$ into (15a), where $\delta$ is an infinitesimally small positive number. The result is $\beta_{\mathrm{c}} J K=4$. The phase transition is second order in nature.

For very small, but finite deformation parameter $\gamma$, one must solve (14). Let $w \equiv \sqrt{r / K}$, (14a) becomes

$$
F(w) \equiv \exp \left\{\frac{1}{2} \beta J K \frac{\gamma}{K(\sinh \gamma)^{2}} \sinh [\gamma K(1-2 w)]\right\}-\frac{1}{w}+1=0. \tag{16}
$$

Of course, as mentioned previously, $w=\frac{1}{2}$ (i.e. $\sqrt{r / K}=\frac{1}{4}$) is always a solution to (16). For sufficiently small $\gamma$, the only solution of (14c) which has the solution $w=\frac{1}{2}$ staying within the tetrahedron is again (15b) (remembering that we are only interested in the situation where $\mu=T$ ). So we have $D=\frac{1}{2}(K-Q)$ and $Q=2 K w(1-w)$. The zeros of $F(w)$ are found from the intersection of $F(w)$ and the $w$-axis.

The results are summarized as follows. For very small $\gamma$, the behaviour of the system as its temperature changes is essentially the same as in the non-deformed case $(\gamma=0)$ described previously. In figure 1 we show the graphs of $F(w)$ at various values of $\beta J K$ for the case of $\gamma=0.00018$ and $K=7000$. When $\beta J K<4$, the zero is always at $M_{1}\left(w=\frac{1}{2}\right)$, which is the maximum as can be checked from the second derivatives of the summand at this point. This is the 'normal' state. But as $\beta J K$ increases beyond $\beta_{\mathrm{c}} J K=4$, the maximum $M_{2}$ moves away from $M_{1}$ towards $w=0$. The point $M_{2}$ represents the 'superconducting' state.

![](./images/812462049853440001_1.jpg)

Figure 1. Graphs of $F(w)$ for $\gamma=0.00018, K=7000$ and $\beta J K$ equal to: (1) 2.0000; (2) 3.9000; (3) 4.7000.

If the deformation parameter $\gamma$ is increased further, while keeping the number of levels $K$ fixed, we find that there exists a critical value $\gamma_{\mathrm{c}}$ beyond which the nature of the phase transition changes: the transition becomes first order. Figure 2 shows the graphs of $F(w)$ for the case of $\gamma=0.0003\left(>\gamma_{\mathrm{c}}=0.0002\right)$ and $K=7000$. For high enough temperatures (small $\beta J K$ ), the maximum is again at $M_{1}\left(w=\frac{1}{2}\right)$. When $\beta J K$ approaches $\beta_{1} J K=3.5330$, an 'inflexion' point $I$ develops. As $\beta J K$ increases further, $I$ bifurcates into a new local maximum $M_{2}$ and a saddle point $S$. At $\beta_{2} J K=3.6475$, the values of the summand at $M_{1}$ and $M_{2}$ become equal. This is a first-order transition point. We note that the critical temperature is higher for larger $\gamma\left(\beta_{2} J K<4\right)$. For $\beta J K>\beta_{2} J K$, the system is in the 'superconducting' state $M_{2}$, and the saddle point $S$ moves towards $M_{1}$. The existence of two local maximum also indicates that metastable states are possible. Here $M_{1}$ represents the metastable 'normal' state that could occur when the temperatures of the system is being lowered, and $M_{2}$ the metastable 'superconducting' state when the temperature is being increased.

![](./images/812462049853440001_2.jpg)

Figure 2. Graphs of $F(w)$ for $\gamma=0.00030, K=7000$ and $\beta J K$ equal to: (1) 3.2000; (2) 3.5000; (3) 3.5330; (4) 3.6000; (5) 4.0000.

For fixed $\gamma$, we also find that the number of pairs of levels can affect the phase transition. There exists a critical value of $K, K_{\mathrm{c}}$, beyond which the phase transition changes from second order to first order. For instance, we find numerically that $K_{\mathrm{c}}=2830$ for $\gamma=0.0005$.

To conclude, we have studied a $q$-analogue of the strong-coupling superconductivity model discussed by Thouless. It is found that the deformation of the oscillator algebra can change the nature of superconducting phase transition from the usual second order to first order, and that metastable normal and metastable superconducting states are allowed in

the first-order transition. Critical temperature is higher for larger deformation. One might interpret these results as follows. From (5) or (7) one sees that the $q$-deformed kinetic term is not free as it was when there is no deformation. Hence the effect of deformation can be viewed as 'turning' on some kind of effective interaction among the paired normal oscillators. This interaction has the tendency to change the nature of superconducting transition, and its strength increases according to the degree of deformation and the number of paired states.

## Acknowledgments
One of us (C-LH) would like to thank the staff of the Institute of Physics at the Academia Sinica for allowing him to use their computing facilities. This work is supported in part by the Republic of China grant NSC81-0208-M032-502.

## References
[1] Drinfeld V G 1987 *Proc. Int. Congr. Mathematics (1986)* vol 1 (Berkeley, CA: University of California Press) p 708
Jimbo M 1986 *Lett. Math. Phys.* **11** 247

[2] de Vega H J 1989 *Int. J. Mod. Phys. A* **4** 2371

[3] Alvarez-Gaume L, Gomez C and Sierra G 1989 *Nucl. Phys. B* **319** 155

[4] Biedenham L C 1989 *J. Phys. A: Math. Gen.* **22** L873
Macfarlane A J 1989 *J. Phys. A: Math. Gen.* **22** 4581

[5] Ng Y J 1990 *J. Phys. A: Math. Gen.* **23** 1023
Lee C-R 1990 *Chinese J. Phys.* **28** 381
Chaichan M and Kulish R 1990 *Phys. Lett.* **234B** 72
Kulish P P and Damaskinsky E V 1990 *J. Phys. A: Math. Gen.* **23** L415
Hayashi T 1990 *Commun. Math. Phys.* **127** 129
Frappat L, Sorba P and Sciarrino A 1991 *J. Phys. A: Math. Gen.* **24** L179
Parthasarathy R and Viswanathan K S 1991 *J. Phys. A: Math. Gen.* **24** 613

[6] Greenberg O W 1990 *Phys. Rev. Lett.* **64** 705; 1991 *Phys. Rev. D* **43** 4111; 1992 *Physica* **180A** 419
Fivel D I 1990 *Phys. Rev. Lett.* **65** 3361
Zagier D 1992 *Commun. Math. Phys.* **147** 199
Stanciu S 1992 *Commun. Math. Phys.* **147** 211
Speicher R 1992 Generalized statistics of macroscopic fields *Preprint* Institut für Angewandte Mathematik, University of Heidelberg
Yu T and Wu Z 1992 Construction of the Fock-like space for quons *Preprint* Jilin University

[7] Floratos E G 1991 *J. Phys. A: Math. Gen.* **24** 4739

[8] Thouless D J 1960 *Phys. Rev.* **117** 1256

[9] Wada Y, Takano F and Fukuda N 1958 *Progr. Theor. Phys.* **19** 597
Anderson P W 1958 *Phys. Rev.* **112** 1900

[10] Distribution functions (i.e. mean occupation number) of $q$-oscillators have been obtained in:
Lee C-R and Yu J-P 1990 *Phys. Lett.* **150A** 63
Ge M-L and Su G 1991 *J. Phys. A: Math. Gen.* **24** L721
(We prefer to proceed from the partition function, since we know the complete spectrum of the system.)