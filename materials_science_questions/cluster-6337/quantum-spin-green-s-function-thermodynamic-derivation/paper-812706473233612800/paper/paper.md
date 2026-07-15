# Specific heat of the spin-$\frac{3}{2}$ Blume-Capel model

T. Kaneyoshi and M. Jaščur
Department of Physics, Nagoya University, 464-01 Nagoya, Japan
(Received 28 February 1992)

The specific heat of the spin-$\frac{3}{2}$ Blume-Capel model is investigated by the use of two formulations based on the Ising spin identities and a differential-operator technique. In particular, the specific heat on a honeycomb lattice is examined in detail for the system with a crystal-field constant in the critical region where the ground-state configuration may change from the spin-$\frac{1}{2}$ state to the spin-$\frac{3}{2}$ state. We find many interesting phenomena in the system.

## I. INTRODUCTION

The Blume-Capel (BC) model¹ is a spin-1 Ising model, which presents a rich variety of critical and tricritical phenomena.² The Hamiltonian is given by
$$
H=-\sum_{i, j} J_{i j} S_{i}^{z} S_{j}^{z}-D \sum_{i}\left(S_{i}^{z}\right)^{2}, \tag{1}
$$
where $S_{i}^{z}$ is the spin operator, $J_{i j}$ the exchange interaction, and $D$ the crystal-field interaction constant. The BC model with $S_{i}^{z}=\pm 1$ and 0 has been examined for many years by using various techniques, and has also been used to describe critical phenomena in magnetic systems and in simple and multicomponent fluids.³

On the other hand, it is important that the BC model be extended to higher spin values, such as the spin-$\frac{3}{2}$ BC model with $S_{i}^{z}=\pm \frac{3}{2}$ and $\pm \frac{1}{2}$. Here, for the BC model with a spin value $S$ ($S \geq 1$), one may generally expect the tricritical behavior when the ratio $D/J$ of the crystal-field constant $D$ and the exchange interaction $J$, is less than $-1$. The magnetic properties of the BC model have not been examined in detail especially for the region of $D/J < -1$, while the phase diagrams of a spin-$\frac{3}{2}$ Ising system with quadrupolar interactions has been examined in the mean-field approximation.⁴

Very recently, we have given a statistical-mechanical treatment of the BC model with a higher spin value by the use of both exact Ising spin identities and a differential-operator technique.⁵,⁶ This method, which can include the effects of correlation through the van der Waerden identity, provides results of transition temperature $T_{c}$ which are quite good in comparison with those obtained by using a rigorous treatment for the Bethe lattice at $D=0.0.^{7,8}$ In particular, the phase diagrams and magnetization curves of the spin-$\frac{3}{2}$ BC model were examined. We have found that tricritical behavior does not exist in the spin-$\frac{3}{2}$ BC model and instead the unstable solutions of magnetization $m\left[m=\left\langle S_{i}^{z}\right\rangle\right]$ and quadrupolar moment $q\left[q=\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle\right]$ do exist in the region of $-1.7167 < D/J < -1.0$ for the honeycomb lattice in addition to the stable solutions.

The purpose of this work is to study the specific heat of the spin-$\frac{3}{2}$ BC model within the framework of our formulation⁶ as an improvement over the standard mean-field theory. Then, we pay attention to the region of $D/J < -1.0$. The outline of the work is the following. In Sec. II, we review briefly these two formulations. In Sec. III, the general formulations for evaluating the internal energy and specific heat of the spin-$\frac{3}{2}$ BC model are derived by using these formulations. In Sec. IV, the numerical results of the spin-$\frac{3}{2}$ BC model on a honeycomb lattice ($z=3$) are given, where $z$ is the coordination number. We find many interesting phenomena especially for the system with a value of $D$ in the vicinity of the critical value $(D/J=-z/2)$ where the ground-state configuration may change from $S_{i}^{z}=\pm \frac{1}{2}$ to $S_{i}^{z}=\pm \frac{3}{2}$.

## II. FORMULATION

We consider the spin-$\frac{3}{2}$ BC model. The Hamiltonian is given by (1). Here, the spins $S_{i}^{z}$ located at sites $i$ on a discrete lattice can take the values $\pm \frac{3}{2}$ and $\pm \frac{1}{2}$. The exchange interactions are restricted to the $z$ nearest-neighbor pairs of spins.

The order parameters of the system are the magnetization $m$ and the quadrupolar moment $q$ given by
$$
m=\left\langle S_{i}^{z}\right\rangle \text{ and } q=\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle, \tag{2}
$$
where $\langle \cdots \rangle$ is the thermal expectation value. To evaluate the mean values $\left\langle S_{i}^{z}\right\rangle$ and $\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle$, we start with the exact Ising spin identities.⁵
$$
m=\left\langle S_{i}^{z}\right\rangle=\left\langle f\left(E_{i}\right)\right\rangle \tag{3}
$$
and
$$
q=\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle=\left\langle g\left(E_{i}\right)\right\rangle \tag{4}
$$
with
$$
E_{i}=\sum_{j} J_{i j} S_{j}^{z}, \tag{5}
$$
where the functions $f(x)$ and $g(x)$ are defined by
$$
f(x)=\frac{1}{2} \frac{3 \sinh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \sinh \left(\frac{1}{2} \beta x\right)}{\cosh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \cosh \left(\frac{1}{2} \beta x\right)} \tag{6}
$$
and
$$
g(x)=\frac{1}{4} \frac{9 \cosh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \cosh \left(\frac{1}{2} \beta x\right)}{\cosh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \cosh \left(\frac{1}{2} \beta x\right)} \tag{7}
$$
⁴⁶ 3374
©1992 The American Physical Society

with
$$
\beta=\frac{1}{k_{B} T}. \tag{8}
$$

By the use of the differential-operator technique, $^{9}$ these identities can be transformed into the convenient forms for calculation:
$$
\left\langle S_{i}^{z}\right\rangle=\left.\left\langle e^{E_{i} \nabla}\right\rangle f(x)\right|_{x=0} \tag{9}
$$
and
$$
\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle=\left.\left\langle e^{E_{i} \nabla}\right\rangle g(x)\right|_{x=0}, \tag{10}
$$
where $\nabla=\partial / \partial x$ is a differential operator. Corresponding to the van der Waerden identity
$$
\exp \left(a S_{i}^{z}\right)=\cosh (a / 2)+2 S_{i}^{z} \sinh (a / 2) \text { for } S=\frac{1}{2}, \quad(11)
$$
we can also obtain the identity for $S=\frac{3}{2}$ as
$$
\exp \left(a S_{i}^{z}\right)=A(a)+B(a) S_{i}^{z}+C(a)\left(S_{i}^{z}\right)^{2}+D(a)\left(S_{i}^{z}\right)^{3} \quad(12)
$$
with
$$
\begin{aligned}
& A(a)=\frac{1}{8}\left[9 \cosh (a / 2)-\cosh \left(\frac{3}{2}\right) a\right], \\
& B(a)=\frac{1}{12}\left[27 \sinh (a / 2)-\sinh \left(\frac{3}{2} a\right)\right], \\
& C(a)=\frac{1}{2}\left[\cosh \left(\frac{3}{2} a\right)-\cosh (a / 2)\right], \\
& D(a)=\frac{1}{3}\left[\sinh \left(\frac{3}{2} a\right)-3 \sinh (a / 2)\right],
\end{aligned} \tag{13}
$$
where $a$ is a constant. By using the van der Waerden identity (12), we can rewrite the identities (9) and (10) for the spin-$\frac{3}{2}$ BC model as
$$
\left\langle S_{i}^{z}\right\rangle=\left.\left\langle\prod_{j}\left[A(a)+B(a) S_{j}^{z}+C(a)\left(S_{j}^{z}\right)^{2}+D(a)\left(S_{j}^{z}\right)^{3}\right]\right\rangle f(x)\right|_{x=0} \tag{14}
$$
and
$$
\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle=\left.\left\langle\prod_{j}\left[A(a)+B(a) S_{j}^{z}+C(a)\left(S_{j}^{z}\right)^{2}+D(a)\left(S_{j}^{z}\right)^{3}\right]\right\rangle g(x)\right|_{x=0}, \tag{15}
$$
where $a=J_{i j} \nabla$. These equations are also exact.

At this place, it is not so easy to treat the exact forms of $S=\frac{3}{2}$ because of the complexity of (12), in comparison with the exact form (11) of $S=\frac{1}{2}$. Because of this fact, we have introduced an approximate but generalized van der Waerden identity valid for any spin value in Ref. 5, namely
$$
\exp \left(a S_{i}^{z}\right)=\cosh \left(\frac{\eta}{\alpha} a\right]+\frac{\alpha}{\eta} S_{i}^{z} \sinh \left(\frac{\eta}{\alpha} a\right], \tag{16}
$$
where the parameter $\eta$ is defined by
$$
(\eta / \alpha)^{2}=q=\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle. \tag{17}
$$

The parameter $\alpha$ must be selected as $\alpha=2$ for the half-integer spin $(S=\frac{1}{2}, \frac{3}{2}, \ldots)$ or $\alpha=1$ for the integer spin $(S=1,2, \ldots)$. As is easily understood from the definition (17), the generalized but approximated van der Waerden identity (16) becomes exact for $S=\frac{1}{2}$, since for $S=\frac{1}{2}(17)$ must be given by $\eta / \alpha=\frac{1}{2}$. Using (16), the identities (9) and (10) are given by
$$
\left\langle S_{i}^{z}\right\rangle=\left.\left\langle\prod_{j}\left[\cosh \left(\frac{\eta}{\alpha} J_{i j} \nabla\right]+\frac{\alpha}{\eta} S_{j}^{z} \sinh \left(\frac{\eta}{\alpha} J_{i j} \nabla\right]\right]\right\rangle f(x)\right|_{x=0} \tag{18}
$$
and
$$
\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle=\left.\left\langle\prod_{j}\left[\cosh \left(\frac{\eta}{\alpha} J_{i j} \nabla\right]+\frac{\alpha}{\eta} S_{j}^{z} \sinh \left(\frac{\eta}{\alpha} J_{i j} \nabla\right]\right]\right\rangle g(x)\right|_{x=0}. \tag{19}
$$

Expanding the right-hand side of (14) and (15) [or (18) and (19)], one can obtain the multiple correlation functions. The simplest approximation, $^{9,10}$ and the one most frequently adopted, is to decouple them according to
$$
\left\langle S_{j}^{z}\left(S_{k}^{z}\right)^{2} \cdots S_{l}^{z}\right\rangle \simeq\left\langle S_{j}^{z}\right\rangle\left\langle\left(S_{k}^{z}\right)^{2}\right\rangle \cdots\left\langle S_{l}^{z}\right\rangle \tag{20}
$$
with $j \neq k \neq \cdots \neq l$. Then, the magnetization $m$ and the quadrupolar moment $q$ for the spin-$\frac{3}{2}$ BC model with nearest-neighbor interaction $J$ are given by
$$
m=\left.\left[A(J \nabla)+B(J \nabla) m+C(J \nabla) q+D(J \nabla) r\right]^{z} f(x)\right|_{x=0}, \tag{21}
$$
$$
q=\left.\left[A(J \nabla)+B(J \nabla) m+C(J \nabla) q+D(J \nabla) r\right]^{z} g(x)\right|_{x=0}, \tag{22}
$$

from (14) and (15), and
$$
m=\left.\left[\cosh \left(\frac{\eta}{\alpha} J \nabla\right]+\frac{\alpha}{\eta} m \sinh \left(\frac{\eta}{\alpha} J \nabla\right]\right]^{z} f(x)\right|_{x=0},
$$

$$
q=\left.\left[\cosh \left(\frac{\eta}{\alpha} J \nabla\right]+\frac{\alpha}{\eta} m \sinh \left(\frac{\eta}{\alpha} J \nabla\right]\right]^{z} g(x)\right|_{x=0},
$$

from (18) and (19). Here, the parameter $r$ in (21) and (22)
is defined by
$$
r=\left\langle\left(S_{i}^{z}\right)^{3}\right\rangle. \quad (25)
$$

For the evaluation of (21) and (22), furthermore, one has
to calculate another order parameter $r$, which is also
given by
$$
\begin{array}{r}
r=\left.[A(J \nabla)+B(J \nabla) m+C(J \nabla) q+D(J \nabla) r]^{z} h(x)\right|_{x=0}, \\
(26)
\end{array}
$$
where the function $h(x)$ is given by
$$
h(x)=\frac{1}{8} \frac{27 \sinh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \sinh \left(\frac{1}{2} \beta x\right)}{\cosh \left(\frac{3}{2} \beta x\right)+e^{-2 D \beta} \cosh \left(\frac{1}{2} \beta x\right)}. \quad (27)
$$

Now, for the evaluation of the magnetic properties we
have the two formulations, namely the first formulation
based on (21), (22), and (26) and the second formulation
based on (23) and (24). In fact, the calculations and nu-
merical evaluation of the magnetic properties in the
spin-$\frac{3}{2}$ BC model based on the first formulation are very
complex even for $z=3$ (or honeycomb lattice) in compar-
ison with those of the second formulation. In particular,
the phase diagram (or the transition temperature) can be
obtained by requiring that the magnetization $m$ (or the
order parameter $r$ ) continuously approaches zero, since
there is no tricritical behavior for any $z$ in the spin-$\frac{3}{2}$ BC
model. $^{5}$ Consequently, all terms of the order higher than
linear in $m$ (or $r$ ) can be neglected. Especially for the first
formulation, this leads to a matrix equation. For the
latter discussions, we show the phase diagram of the
spin-$\frac{3}{2}$ BC model with $z=3$ in Fig. $1.^{5}$

As is seen from Fig. 1, the phase diagram expresses
some characteristic behaviors. First, we should notice
that these two formulations lead to almost the same re-
sults; in Fig. 1 the results of the second formulation are
plotted, but the results of the first formulation lie within
the thickness of the solid line. In fact, the first formula-
tion gives
$$
\frac{k_{B} T_{c}}{J}=2.9188 \text { at } D=0.0, \quad (28)
$$
and the second formulation gives
$$
\frac{k_{B} T_{c}}{J}=2.9556 \text { at } D=0.0. \quad (29)
$$

These values may be compared with
![](./images/812706473233612800_1.jpg)

FIG. 1. The variation of $T_{c}$ with $D$ for the spin-$\frac{3}{2}$ Blume
Capel model with $z=3$. The solid line is obtained from the
second formulation based on Eqs. (23) and (24). The result of $T_{c}$
obtained from the three coupled equations (21), (22), (26) lies
within the thickness of the solid line, although the values are
very little smaller than those of the second formulation. The
dashed line given by $D / J=-1.5$ separates the two ordered
phases $(S_{i}^{z}= \pm \frac{1}{2}$ state $)$ and $(S_{i}^{z}= \pm \frac{3}{2}$ state $)$ at $T=0 \mathrm{~K}$.

$$
\frac{k_{B} T_{c}}{J}=2.6044 \text { at } z=3 \quad (30)
$$
for the exact result on a Bethe lattice, although it is ob-
tained only for $D=0.0.^{7}$ In particular, the value of
$k_{B} T_{c} / J$ approaches the two constant values when the
value of $|D|$ becomes large. Physically, the constant
value for $D \to \infty$ comes from the $S_{i}^{z}= \pm \frac{3}{2}$ state $(q=\frac{9}{4})$
and for $D \to -\infty$ it results from the $S_{i}^{z}= \pm \frac{1}{2}$ state
$(q=\frac{1}{4})$. The horizontal line part for $D / J<-2.0$ results
from the $S_{i}^{z}= \pm \frac{1}{2}$ state, so that the transition temperature
is given by $4 k_{B} T_{c} / J=2.104$. The transition temperature
$4 k_{B} T_{c} / J=2.104$ is equivalent to that of the spin-$\frac{1}{2}$ Ising
honeycomb lattice obtained within the framework of the
Zernike approximation [or the decoupling approximation
(20)]. $^{11}$ The change of state from $q=\frac{9}{4}$ to $q=\frac{1}{4}$ happens
in the region of $-2.0<D / J<-1.0$. By comparing the
values of the ground-state energies for $S_{i}^{z}= \pm \frac{3}{2}$ and
$S_{i}^{z}= \pm \frac{1}{2}$, the two ordered phases at $T=0 \mathrm{~K}$ are separated
by $D / J=-z / 2=-1.5$. The dashed line in Fig. 1
denotes the fact. The two phases at $T=0 \mathrm{~K}$ are separat-
ed by a first-order transition line (or dashed line). A
phase diagram similar to Fig. 1 is also obtained in the
mean-field approximation. $^{12}$

### III. INTERNAL ENERGY AND SPECIFIC HEAT

Let us investigate the specific heat of the spin-$\frac{3}{2}$ BC
model. The specific heat is defined by
$$
C=\frac{\partial U}{\partial T}, \quad (31)
$$

where $U$ is the internal energy. The internal energy of the spin-$\frac{3}{2}$ BC model is given by, for the system with nearest-neighbor interaction $J$,
$$U=-J \sum_{i, j}\left\langle S_{i}^{z} S_{j}^{z}\right\rangle-D \sum_{i}\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle\qquad(32)$$
or
$$\frac{U}{N}=-\frac{1}{2}\left\langle E_{i} S_{i}^{z}\right\rangle-D\left\langle\left(S_{i}^{z}\right)^{2}\right\rangle\qquad(33)$$
with
$$E_{i}=J \sum_{\delta} S_{i+\delta}^{z},$$
where $N$ is the total number of magnetic atoms. By using the Ising spin identity and the differential-operator technique, the expectation value $\langle E_{i} S_{i}^{z}\rangle$ can be exactly given by
$$\begin{aligned}
\left\langle E_{i} S_{i}^{z}\right\rangle & =\left.\left\langle E_{i} e^{E_{i} \nabla}\right\rangle f(x)\right|_{x=0} \\
& =\left.\left[\frac{\partial}{\partial y}\left\langle e^{E_{i} y}\right\rangle\right]_{y=\nabla} f(x)\right|_{x=0}.
\end{aligned}\qquad(34)$$

As noted in Sec. II, we can formulate the expectation value $\langle e^{E_{i} y}\rangle$ in the two ways; by using the exact van der Waerden identity (12) and the decoupling approximation(20), Eq. (34) can be written as
$$\begin{aligned}
\left\langle E_{i} S_{i}^{z}\right\rangle= & \frac{J z}{2}\left[-\frac{9}{8} D(J \nabla)+2 A(J \nabla) m\right. \\
& \left.+E(J \nabla) q+2 C(J \nabla) r\right] \\
\times[ & A(J \nabla)+B(J \nabla) m+C(J \nabla) q \\
& \left.+D(J \nabla) r\right]^{z-1} f(x)\left.|_{x=0}\right.
\end{aligned}\qquad(35)$$
with
$$E(J \nabla)=\frac{1}{2}\left\{3 \sinh \left(\frac{3}{2} J \nabla\right)-\sinh [(J / 2) \nabla]\right\}.\qquad(36)$$

On the other hand, applying the generalized van der Waerden identity (16) and the decoupling approximation(20), Eq. (34) is given by
$$\begin{aligned}
\left\langle E_{i} S_{i}^{z}\right\rangle= & z J \frac{\eta}{\alpha}\left[\sinh \left(\frac{J \eta}{\alpha} \nabla\right)+m \frac{\alpha}{\eta} \cosh \left(\frac{J \eta}{\alpha} \nabla\right)\right] \\
& \times\left[\cosh \left(\frac{J \eta}{\alpha} \nabla\right)\right. \\
& \left.+m \frac{\alpha}{\eta} \sinh \left(\frac{J \eta}{\alpha} \nabla\right)\right]^{z-1} f(x)\left.|_{x=0}.\right.
\end{aligned}\qquad(37)$$

Thus, we have also the two formulations for evaluating the internal energy and specific heat of the spin-$\frac{3}{2}$ BC model. For the evaluation, it is necessary to know the temperature dependences of $m, q$, and $r$. For the system with $z=3$, they are numerically studied in Ref. 6. As discussed in the work, the thermal variations of $m$ and $q$ obtained from the two formulations take almost the same forms except the vicinity of $D=-1.5 J$ in Fig. 1.

Now, the internal energy of $z=3$ can be obtained from(37) as follows:
$$\frac{U}{J N}=-\frac{3}{2} \frac{\eta}{\alpha}\left[L_{1}+\left(2 L_{1}+L_{2}\right)\left(\frac{\alpha}{\eta}\right)^{2} m^{2}\right]-\frac{D}{J} q\qquad(38)$$
with
$$\begin{aligned}
& L_{1}=\cosh ^{2}\left(\frac{J \eta}{\alpha}\right) \sinh \left(\frac{J \eta}{\alpha} \nabla\right) f(x)\left.\right|_{x=0}, \\
& L_{2}=\sinh ^{3}\left(\frac{J \eta}{\alpha} \nabla\right) f(x)\left.\right|_{x=0},
\end{aligned}\qquad(39)$$
where the coefficients $L_{1}$ and $L_{2}$ are easily calculated by using a mathematical relation
$$e^{a \nabla} f(x)=f(x+a). \quad(40)$$

Even for $z=3$, however, the internal energy obtained from (35) has an extremely complicated form and hence it will not be reproduced here, although it can be straightforwardly derived after a tedious calculation.

## IV. NUMERICAL RESULTS
In this section, let us study the specific heat and internal energy of the spin-$\frac{3}{2}$ BC model with $z=3$ by solving Eqs. (48) and (35) numerically.

In Fig. 2, we plot the numerical results of $U$ and $C$ as well as the thermal variation of $r$ , when the value of $D$ is fixed at $D=2.0 J$ . In the figure, the solid line is obtained from the first formulation based on (35) and the dashed line is obtained from the second formulation based on(37) [or (45)]. As is seen from the figure, the two formulations give almost the same results for the thermal variations of $C$ and $U$ . As the two formulations are essentially the effective-field theory depending only on $z$ , the specific heat may express the discontinuity at $T=T_{c}$ , although in the high-temperature region $(T>T_{c})$ it takes a finite value. In particular, notice that the correct values of $r=\frac{27}{8}$ and $U / J N=-\frac{63}{8}$ expected at $T=0 ~K$ are satisfied in Fig. 2.

![](./images/812706473233612800_2.jpg)

FIG. 2. The magnetic specific heat and internal energy of the spin-$\frac{3}{2}$ BC model with $z=3$ , when the value of $D$ is fixed at D=2.0J. The solid and dashed lines are, respectively, obtained from the first and second formulations. The solid-dashed line represents the thermal variation of $r$ .

![](./images/812706473233612800_3.jpg)

FIG. 3. The magnetic specific heat of the spin-$\frac{3}{2}$ BC model with $z=3$, when the three values of $D$ are selected in the critical region (see Fig. 1). Here, the solid lines are obtained from the first formulation based on (21), (22), and (26). The dashed lines are obtained from the second formulation based on (23) and (24).

![](./images/812706473233612800_4.jpg)

FIG. 4. The thermal variations of the internal energy (solid or dashed line) and order parameter $r$ (solid-dashed line) in the spin-$\frac{3}{2}$ BC model with $z=3$, when the two values of $D$ are selected in the critical region (see Fig. 1). The solid lines are obtained from the first formulation and the dashed lines are obtained from the second formulation.

Here, a particular attention should be paid to the thermal variations of $C$ and $U$ in the system with a $D$ near the critical value ($D=-1.5J$) of Fig. 1. Figure 3 shows the thermal variations of $C$ in the systems with the three values of $D$, namely $D=-1.5J$, $-1.6J$, and $-2.0J$. The solid and dashed lines are, respectively, obtained by the first and second formulations. As is seen from the figure, many interesting phenomena are found. First, the solid and dashed curves in the system with $D=-2.0J$ give almost the same results and they show the sharp maximum and jump at $T=T_{c}$. Even in the high-temperature region ($T>T_{c}$), the specific heat of the systems with $D=-2.0J$ and $-1.6J$ may exhibit a broad maximum. The high-temperature behavior of $C$ is clearly different from the usual one, namely that of Fig. 2 and curve $c$ in Fig. 3. In particular, different behaviors are observed in the low-temperature region ($T<T_{c}$) of $C$ for the systems with $D=-1.6J$ and $-1.5J$; in each formulation, the specific heat of the system with $D=-1.6J$ shows a broad maximum in the low-temperature region and then takes a jump at $T=T_{c}$. For the system with the critical value $D=-1.5J$, on the other hand, the two formulations give completely different behaviors for the low-temperature variation of the specific heat. That is to say, the two formulations give the same values in the very low-temperature region ($0\leq T/T_{c}\leq0.4$), while they may express different broad maxima in the vicinity of $T/T_{c}=0.5$. With increasing $T$, however, the dashed line (the second formulation) decreases monotonically from the broad maximum and takes a jump at $T=T_{c}$. But, the solid line (the first formulation) decreases from the broad maximum, shows a minimum in the vicinity of $T/T_{c}=0.7$, and then takes another maximum and a jump at $T=T_{c}$.

In order to understand the anomalous phenomena found in Fig. 3, the thermal variations of $r$ and $U$ are depicted in Fig. 4 by taking the two values of $D$, namely $D=-2.0J$ and $-1.5J$. For the curves labeled $a$, the internal energy (solid and dashed lines) and the order parameter (solid-dashed line) take the correct values $U=r=\frac{1}{8}$ at $T=0$ K. Then, the two formulations (solid and dashed lines) give almost the same values for the internal energy. The thermal variation of $r$ exhibits a normal behavior. On the other hand, the solid and dashed lines labeled $b$ may express rather different features, while at $T=0$ K they take the correct value $U=0$ satisfied for $D=-1.5J$. Here, the main difference comes from the following fact: The first formulation (solid line) includes the temperature dependence of $r$, while the effect is not taken into account in the second formulation (dashed line). In fact, the solid-dashed line (or $r$) labeled $b$ in Fig. 4 may express the anomalous temperature dependence, which is clearly in contrast with the normal one, such as the solid-dashed curve labeled $a$ in Fig. 4 or in Fig. 2. That is to say, the thermal variation of $U$ in the region where the anomalous behavior of $r$ is observed is clearly different from that of the dashed line.

### V. CONCLUSIONS

In this work, we have studied the specific heat of the spin-$\frac{3}{2}$ Blume-Capel model on the honeycomb lattice ($z=3$) by the use of the two formulations based on both Ising spin identities and a differential-operator technique. As shown in Figs. 2-4, these formulations give essentially the same behavior for the specific heat and internal energy in the system with a value of $D$, except the critical region where the two configurations ($S_{i}^{z}=\pm\frac{3}{2}$ state) and ($S_{i}^{z}=\pm\frac{1}{2}$ state) are separated by $D/J=-z/2=-1.5$ at $T=0$ K. In particular, we have examined in detail the specific heat and internal energy of the system with a value of $D$ in the critical region. As shown in Fig. 3, many anomalous phenomena are observed in the thermal variation of the specific heat. Here, one should notice that only the stable solutions of $m$ and $q$ are of course selected for the evaluations, although the two (stable and

unstable) solutions of $m$ and $q$ do exist in the region of $-1.7167 < D/J < -1.0$.

A particular attention should be paid to the system with the critical value $(D=-1.5J)$. As depicted in curve $c$ of Fig. 3 and curves $b$ of Fig. 4, the thermal variations of $C$ and $U$ take completely different features in the low-temperature region $(T<T_{c})$, when we apply the two formulations to the problem. However, a broad maximum of $C$ is observed commonly in the vicinity of $T/T_{c}=0.5$ for each formulation. From the theoretical point of view, we have only introduced the decoupling approximation (20) in the first formulation. In the second formulation, on the other hand, we have introduced two approximations, namely the generalized but approximat- ed van der Waerden identity (16) and the decoupling approximation (20). Therefore, the results obtained from the first formulation seem to be reasonable. However, these results pose an important theoretical problem which should be clarified: What is the correct result of the specific heat in the spin-$\frac{3}{2}$ Blume-Capel model with the critical value of $D/J=-z/2$?

Finally, the specific heat of the spin-$\frac{3}{2}$ Blume-Capel model on a honeycomb lattice is examined in this work. The formulations can be applied to the spin-$\frac{3}{2}$ BC model with any $z$ as well as many related Ising spin problems. However, it should be noted that the critical phenomena given in this work are because of the decoupling of (20) of the "mean-field" type.

$^{1}$M. Blume, Phys. Rev. 141, 517 (1966); H. W. Capel, Physics 323, 966 (1966).
$^{2}$T. Kaneyoshi, Physics A 164, 730 (1990).
$^{3}$I. D. Lawrie and S. Sarback, *Phase Transitions and Critical Phenomena*, edited by C. Domb and J. L. Lebowitz (Academic, London, 1988), Vol. 9
$^{4}$J. Sivardiére and M. Blume, Phys. Rev. B 5, 1126 (1972).
$^{5}$T. Kaneyoshi, J. W. Tucker, and M. Jaščur, Physica B (to be published).
$^{6}$T. Kaneyoshi and M. Jaščur, Physica B (to be published).
$^{7}$Y. Tanaka and N. Uryu, J. Phys. Soc. Jpn. 50, 1140 (1981).
$^{8}$J. W. Tucker, J. Magn. Magn. Matter 71, 27 (1987).
$^{9}$R. Honmura and T. Kaneyoshi, J. Phys. C 12, 3979 (1979).
$^{10}$N. Matsudaira, J. Phys. Soc. Jpn. 35, 1593 (1973).
$^{11}$T. Kaneyoshi, I. P. Fittipaldi, and H. Beyer, Phys. Status Solidi B 102, 393 (1980).
$^{12}$F. C. Sábarreto and O. F. DeAlcantara Bonfim, Physica A 172, 378 (1991).