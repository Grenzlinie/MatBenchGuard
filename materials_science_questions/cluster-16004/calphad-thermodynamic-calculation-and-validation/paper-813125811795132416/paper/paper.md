![](./images/813125811795132416_1.jpg)

Pergamon

Calphad Vol. 19, No. 3, pp. 245-277, 1995
Copyright © 1995 Elsevier Science Ltd
Printed in Great Britain. All rights reserved
0364-5916/95 $9.50 + 0.00

0364-5916(95) 00025-9

General algorithm, its mathematical basis and computer autonomic
program for calculation of phase diagrams of binary systems,
containing p disordered phases of variable and q phases of
constant compositions at $(p,q) \leq 10$

Udovsky A.L.*, Karpushkin V.N.** , Kozodaeva E.A***

*Baykov A.A. Institute of Metallurgy, Academy of Sciences
Leninsky Pr. 49, Moscow, 117334, Russia
**Institute of problems of information transformation, Russia
***VNIIGeosystem, Russia

(Presented at CALPHAD XXIII, Madison, USA, June 1994)

Abstract.

The method of thermodynamic calculation of binary phase diagrams
(2PD), containing p disordered phases of variable composition and q
phases of constant composition for case $(p,q) \leq 10$ was constructed in
this paper. In this method 1) the definition of all possible solutions
of phase equilibrium equations system (PEES) was realized; 2) the
separation of PEES' roots or tie-line's ends at (T,P)=const was con-
ducted; 3) the original algorithm for calculation of PEES' roots was
constructed and programmed and theorems about this algorithm conver-
gence and about behaviour of this convergence were formulated and -
proved; 4) the algorithm for autonomic selection of thermodynamically
stable tie- lines was constructed and thereby calculating process T-x
phase diagrams was automated. Some examples of using this method for
calculation of binary phase diagrams for Cr-W, Ni-W, Ni-Al and Ni-Cr
are reported here.

Introduction

There are two classes of problems in the field of thermodynamic
calculation of binary phase diagrams (2PD). For solving of problems
from the $1^{st}$ class it needs to calculate 2PD based on defined depen-
dence of thermodynamic functions from temperature T and composition x
for all competing phases which are contained in the considered system.

Original version received on 14 June 1994, Revised version in June 1995

molar thermodynamic Gibbs energy of heterogeneous systems with
allowance for material balance for enclosed system and about 2
accessory of tie-line's ends to feasible values regions.

The aim of this paper is a description of constructed method (and
it's programming realization) for the calculation of thermodynamically
stable 2PD, containing p disordered phases of variable and q phases of
constant composition at (p,q)≤10. This method resolves named above
limitations 2)-5) above referring of methods of the $1^{st}$ direction. It
is important that a method of calculation of equilibrium between two
different phases in binary systems may be applied for wide class of
models, even though its programming implementations uses different
representation of exess thermodynamic Gibbs energy (TGE) for phases of
variable composition in polynomial form on x (composition) and T (tem-
perature).

### Thermodynamic definition of a problem.

We shall consider an enclosed binary system containing p disor-
dered solutions (p≤10). Their molar thermodynamic Gibbs energy (MTGE)
may be written in the next form:

$$
\begin{align*}
G^{\alpha}(x,T) &= R*T*[x*Ln(x)+(1-x)*Ln(1-x)]+(1-x)*G^{\alpha}(0,T)+x*G^{\alpha}(1,T)+ \\
&+E_{G}{}^{\alpha}(x,T) \tag{1}
\end{align*}
$$

$$
\begin{align*}
E_{G}{}^{\alpha}(x,T)&=x*(1-x)*\sum_{k=1}^{n^{\alpha}} \sum_{l=1}^{m^{\alpha}} a_{kl}^{\alpha}*x^{k-1}*T^{l-1}, \tag{2} \\
&n^{\alpha}<4, m^{\alpha}<3, \alpha=1,2,\dots,p.
\end{align*}
$$

The system may also contain q phases of constant composition (q≤10)
MTGE of which the Gibbs energy may be written as:

$$
\begin{align*}
\Delta G^{\gamma}(x^{\gamma},T)&\equiv G^{\gamma}(x^{\gamma},T)-(1-x^{\gamma})*G^{\gamma}(0,T)-X^{\gamma}*G^{\gamma}(1,T)= \\
=\sum_{k=1}^{r^{\gamma}} b_{k}^{\gamma}*T^{k-1}&+b_{0}^{\gamma}*T*Ln(T); \quad \gamma=1,2,\dots,q; \ r^{\gamma}<6; \ x^{\gamma}=\text{const}. \tag{3}
\end{align*}
$$

Analyzing expression (1),(2) it may be note that each of phases of
variable composition allows separation to 3 "domes" inclusive in coor-
dinates x - $G^{\alpha}(x,T)$, where T=const. It was be proved in [5] that phase

equilibrium equations system in case of equilibrium between isomorphic solutions:

$$
\left. \frac{\partial G^{\alpha}}{\partial x} \right|_{x^{\alpha}} = \left. \frac{\partial G^{\alpha'}}{\partial x} \right|_{x^{\alpha'}} \quad , \quad (T,P)=\text{cnst},
$$

$$
\left. G^{\alpha}(x^{\alpha}, T)-x^{\alpha} * \frac{\partial G^{\alpha}}{\partial x} \right|_{x^{\alpha}} = \left. G^{\alpha'}(x^{\alpha'}, T)-x^{\alpha'} * \frac{\partial G^{\alpha'}}{\partial x} \right|_{x^{\alpha'}} \tag{4}
$$

is invariant relative to algebra transformation:

$$
\Phi(x, T)=\tilde{G}(x, T)-A(T)*x-B(T), \quad \tilde{G}(x, T)\equiv G^{\alpha}(x, T), \tag{5}
$$

and also algorithm for solving PEES (4) (U-algorithm) was formulated in [6]. U-algorithm was generalized in case of equilibrium between two phases of variable composition in a binary system [7] and between n - phases in n-component system [8]:

$$
\left. \frac{\partial \tilde{G}}{\partial x} \right|_{x^{\alpha}} = \left. \frac{\partial \tilde{G}}{\partial x} \right|_{x^{\beta}} \quad , \quad (T,P)=\text{const},
$$

$$
\left. \tilde{G}^{\alpha}(x^{\alpha}, T)-x^{\alpha} * \frac{\partial \tilde{G}^{\alpha}}{\partial x} \right|_{x^{\alpha}} = \left. \tilde{G}^{\beta}(x^{\beta}, T)-x^{\beta} * \frac{\partial \tilde{G}^{\beta}}{\partial x} \right|_{x^{\beta}} \tag{6}
$$

where

$$
\tilde{G}(x, T)=
\begin{cases}
G^{\alpha}(x, T), & x \leq z^{\alpha\beta}, \\
G^{\beta}(x, T), & x \geq z^{\alpha\beta},
\end{cases}
$$

$z^{\alpha\beta}$- is root of equation $G^{\alpha}(z, T)=G^{\beta}(z, T)$, T=const. In compact form the U-algorithm may be written as:

$$
\left. \frac{\partial \Phi_{s+1}}{\partial x} \right|_{x^{\alpha}} = \frac{\Phi_{s}(x_{s}^{\beta}, T)- \Phi_{s}(x_{s}^{\alpha}, T)}{x_{s}^{\beta} - x_{s}^{\alpha}} , \ T=\text{const}, \ x_{s}^{\alpha} \neq x_{s}^{\beta}, \tag{7}
$$

here s - is an iteration number:

$$
\Phi_{s}(x)=\Phi_{s-1}(x)-A_{s-1}*\left[x-\eta_{s-1}^{1}\right], \tag{7a}
$$

$$
A_{s-1}= \frac{\Phi_{s-1}(\eta_{s-1}^{2})-\Phi_{s-1}(\eta_{s-1}^{1})}{\eta_{s-1}^{2}- \eta_{s-1}^{1}}, \tag{7b}
$$

where $\eta_{s-1}^{1}$ and $\eta_{s-1}^{2}$ - are roots of equations (7c):

$$
\left. \frac{\partial \Phi_{s-1}}{\partial x} \right|_{\eta_{s-1}^{1}} = 0,\ \left. \frac{\partial^{2} \Phi_{s-1}}{\partial x^{2}} \right|_{\eta_{s-1}^{1}} >0,\ \left. \frac{\partial \Phi_{s-1}}{\partial x} \right|_{\eta_{s-1}^{2}} =0,\ \left. \frac{\partial^{2} \Phi_{s-1}}{\partial^{2} x} \right|_{\eta_{s-1}^{2}} >0, \tag{7c}
$$

At first iteration we have:

$$
\Phi_{0}(x)\equiv \tilde{G}(x,T),\ T=\text{const}, \tag{7d}
$$

$$
A_{0}= \frac{1}{2} * \left( \left. \frac{\partial G^{\beta}}{\partial x} \right|_{z^{\alpha \beta}} - \left. \frac{\partial G^{\alpha}}{\partial x} \right|_{z^{\alpha \beta}} \right) \tag{7e}
$$

The PEES (6) by transformation (5) breaks down into two equations (7) and (7c); it is important that on the $(s-1)^{th}$ iteration values $\eta_{s-1}^{1}$ and $\eta_{s-1}^{2}$ are sought as roots of equations (7c) or as local minima of the general function $\Phi_{s-1}$ defined by (5) or (7a)-(7c).

In the case of equilibrium between one phase of variable composition ($\alpha$-phase) and one phase of constant composition ($\beta$-phase) the system (6) transforms in one equation:

$$
G^{\alpha}(x^{\alpha}, T)-G^{\beta}(x^{\beta}, T)=\left. \frac{\partial G^{\alpha}}{\partial x} \right|_{x^{\alpha}}*(x^{\alpha}-x^{\beta}), \quad x^{\beta}=\text{const},
$$

and system (7)-(7e) transforms in:

$$
\left. \frac{\partial \Phi_{s+1}}{\partial x} \right|_{x_{s+1}^{\alpha}} = \frac{\Phi_{s}(x^{\beta}, T)-\Phi_{s}(x_{s}^{\alpha}, T)}{x^{\beta}-x_{s}^{\alpha}} ,
$$

where

$$
\Phi_{s}(x)=\Phi_{s-1}(x)-A_{s-1} *\left[x-\eta_{s-1}^{1}\right], \quad A_{s-1}=\frac{G^{\beta}\left(x^{\beta}\right)-\Phi_{s-1}\left(\eta_{s-1}^{1}\right)}{x^{\beta}-\eta_{s-1}^{1}} ,
$$

$$
\left. \frac{\partial \Phi_{s-1}}{\partial x} \right|_{\eta_{s-1}^{1}}=0,\ \left. \frac{\partial^{2} \Phi_{s-1}}{\partial x^{2}} \right|_{\eta_{s-1}^{1}} >0,\ \Phi_{0}(x)=G^{\alpha}(x)-(1-x)*G^{\alpha}(0)-x*G^{\alpha}(1),
$$

T=const, s - is an iteration number.

Thus this method of the thermodynamic calculation of 2PD con- taining p disordered phases of variable and q phases of constant com-position may be represented in view of the several steps:

1) from a set of MTGE (Molar Thermodynamic Gibbs energy) for phases of variable composition at T=const the "minimum-function" $\tilde{G}(x, T)$ is constructed: $\tilde{G}(x, T)=\min _{1 \leq i \leq p}\left\{G^{i}(x, T) ; 0 \leq x \leq 1\right\}, T=$ const;

2) regions of monotony for $\partial \tilde{G} / \partial x$ function are obtained;

3) determination of feasible values regions for tie-line's ends in case of two-phase equilibrium for $\tilde{G}(x)$ function is carried out;

4) all of possible tie-lines ends lying in feasible values regions named above are constructed (by U-algorithm);

5) selection of thermodynamically stable tie-lines (conodes) is con- ducted.

Steps 1) - 5) are repeated at the each new value of temperature T defined in cycle with constant step $\Delta T$. A more detailed description of this algorithm is given below.

### The mathematical basis of U-algorithm.

From the preceding paragraph it follows that the U-algorithm is a central part in the consruction of 2PD. This algorithm was formulated for the case of equilibrium between two phases of variable composition and

for equilibrium between one phase of variable and one phase of cons- tant compositions. Let us consider the U-algorithm in the case of equilibria between two disordered solutions.

Lemma Let $\Phi:[A,B]\to R$. Suppose there are segments $[a_1,b_1],[a_2,b_2]$, such that $A<a_1<b_1<a_2<b_2<B$, $\Phi\in C^k[a_j,b_j],\ j=1,2,\ k\geq2$, $\frac{\partial^2\Phi}{\partial x^2}>0$ on segments $[a_j,b_j],\ j=1,2$ and there are points $c_1,c_2$, such that $\left.\frac{\partial\Phi}{\partial x}\right|_{c_1}=\left.\frac{\partial\Phi}{\partial x}\right|_{c_2}$ and $a_j<c_j<b_j,\ j=1,2$.

Then there are $p,q$: $a_1\leq p<c_1<q\leq b_1$ and function $\varphi:[p,q]\to[a_2,b_2]$, such that $\varphi\in C^{k-1}[p,q],\left.\frac{d\Phi}{dx}\right|_{z}=\left.\frac{d\Phi}{dx}\right|_{\varphi(z)}$ for all $z\in[p,q]$,and function $\varphi$ is eversible on segment $[p,q]$.

Let $\Psi(x)=[\Phi(x)-\Phi(\varphi(x))]/(x-\varphi(x))$; $y,\ \varphi(y)-$ are ends of tie - line (suppose it exists ) then we have the next theorem.

### Theorem 1 (about convergence of iterative process)
Let function $\Phi(x)$ satisfies Lemma. Let $y\in[p,q]$ and $\psi(x)=\left.\frac{d\Phi}{dx}\right|_{y}$, where $p,q,\psi$ and $\varphi(y)$ are defined in Lemma. Suppose either:

$$1)\left.\frac{d^2\Phi}{dx^2}\right|_{y}=\left.\frac{d^2\Phi}{dx^2}\right|_{\varphi(y)},\ \Phi\in C^3[a_j,b_j],\ j=1,2.$$

or

$$2)\left.\frac{d^2\Phi}{dx^2}\right|_{y}=\left.\frac{d^2\Phi}{dx^2}\right|_{\varphi(y)},\ \left.\frac{d^3\Phi}{dx^3}\right|_{y}>\left.\frac{d^3\Phi}{dx^3}\right|_{\varphi(y)},\ \Phi\in C^4[a_j,b_j],\ j=1,2.$$

Then there is vicinity $U$ of point $y$ such that: if the first two appro- ximations of U-algorithm $x_1,x_2$ lie in this vicinity $U$ then sequences $x_1,x_2,...,x_n$ monotonously converges to point $y$. In case 1) degree of convergence is greater or equal 2, and in case 2) degree of convergence is greater or equal 3.

### Theorem 2. (about convergence speed of U-algorithm)
Let $\Phi$ satisfies Lemma. Let $s-$ is the least whole number such that

$\left.\frac{d^{s} \psi}{d x^{s}}\right|_{y} \neq 0$, $s>2$. Suppose that $s$=2k (even number) or $s$=2k+1and$\left.\frac{d^{s} \psi}{d x^{s}}\right|_{y}>0$, where $k$ is a whole natural number. Let $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$ - is a sequence of U-algorithm approximations. Then there is vicinity U of point y such that if $x_{1}, x_{2} \in U$, then $x_{1}, x_{2}, \ldots, x_{n}$ monotonously converges to point y with speed s>2. Let $s=2 k+1,\left.\frac{d^{s} \psi}{d x^{s}}\right|_{y}<0$. Suppose there is $\varepsilon>0$ with the next properties:

if $M=\inf _{|x-y|<\varepsilon}\left|\frac{d^{2} \Phi}{d x^{2}}\right|, Q=\sup _{1|x-y|<\varepsilon}\left|\frac{d^{2} \Phi}{d x^{2}}\right|$, then $\varepsilon^{2 k} * Q / M<1$. Then there is $\varepsilon>0$ such that if $|x_{n}-y|<\varepsilon_{1}$ at $n \geq 1$, then there are $d_{1}$ and $d_{2}$ such that $|y-d_{1}| 1<\varepsilon$, $d_{1}+d_{2}=2 y$ and sequences $t_{r}=x_{2 r} d_{1}, T_{r}=x_{2 r+1} d_{2}$ at $r \infty$ with speed equal or more then $(2 k+1)^{2}$ and

$$
\left.\frac{d \Phi}{d x}\right|_{d_{1}}=\psi\left(d_{2}\right), \quad\left.\frac{d \Phi}{d x}\right|_{d_{2}}=\psi\left(d_{1}\right).
$$

Let us consider an equilibrium between one phase of variable and one phase of constant composition. Let y be an end of tie-line (we suppose that this tie-line exists), a be a composition for the phase of constant composition (a=const).

### Theorem 3 (about convergence of U-algorithm)
Let $\Phi:[c, d] R, \Phi \in C^{2}[c, d], \frac{d^{2} \Phi}{d x^{2}}>0$ on segment $[c, d], a \notin[c, d]$. Let $c<y<d$ (y- is a desired end of tie-line). Then there is vicinity U of point y such that y - is unique end of tie-line in vicinity U and if $x_{1}, x_{2} \in U$ then sequence $x_{1}, x_{2}, \ldots, x_{n}$ is monotonously converges to point y with speed equal or more then 2. And if d < a, then $x_{2}<\ldots<x_{n}<\ldots<y$, if a < c then $x_{2}>\ldots>x_{n}>\ldots>y$.

### Comparison of U-algorithm with Newton method.

Let us compare U-algorithm with the standard algorithm having square speed of convergence (for example, Newton method) as a example of search of zero for the next function $\nu(x)$:

one time on the each iteration, and in Newton method for search $\varphi(x_{n})$
this equation isn't solved at all.

### Algorithm for autonomic calculation of thermodynamically stable phase diagrams of binary systems

For convenience let us introduce some definitions and conven-
tional signs. We shall distinguish the next types of two-phase equili-
bria: equilibrium of type 1⊗1 - is an equilibrium between two disorde-
red phases of variable composition; equilibrium of type 1⊗0 or 0⊗1 -
is an equilibrium between one phase of variable and one phase of -
constant compositions; and equilibrium of type 0⊗0 - is an equilibrium
between two phases of constant composition.

We suppose that MTGE for phases of variable and constant composi-
tion are written in form (1)-(3). We introduce also a concept of -
possible two - phase equilibrium for equilibrium of type 1⊗1: phase
equilibrium equations system (6) have a solution (or equilibrium -
between i and j phases is possible), if intersection of sets $[m_{i},M_{i}]$
and $[m_{j},M_{j}]$ is not empty: $[m_{i},M_{i}] \cap [m_{j},M_{j}] \neq \emptyset$, where

$$
\begin{aligned}
& m_{i}=\min _{x \in\left[r^{i}, r^{i+1}\right]} \tilde{G}_{x}^{\prime}, \quad M_{i}=\max _{x \in\left[r^{i}, r^{i+1}\right]} \tilde{G}_{x}^{\prime}, \\
& m_{j}=\min _{x \in\left[r^{j}, r^{j+1}\right]} \tilde{G}_{x}^{\prime}, \quad M_{j}=\max _{x \in\left[r^{j}, r^{j+1}\right]} \tilde{G}_{x}^{\prime},
\end{aligned}
$$

$[r^{i}, r^{i+1}],[r^{j}, r^{j+1}]$ - are the i-th and j-th segments of monotony for -
function G, where $\tilde{G}_{xx}''>0$ (further we shall give more detailed descrip-
tion of this segments).

Metastable two-phase equilibrium for equilibrium of type 1⊗1, 0⊗1 and
0⊗0 we shall call any solution of PEEKS (6) (it conventional sign is
$G_{k \otimes l}^{i,j}$; i,j- are indexes of competing phases; k,l - are indentifiers of
equilibrium type).

Local-stable two-phase equilibrium between fixed type of equilibrium
we shall call the minimum from metastable two-phase equilibria of -
named type:
$\bar{G}_{k \otimes l}^{m,n=min} G_{i,j \otimes l}^{i,j}$ (here the type of two-phase equilibrium is fixed). -

Global-stable two-phase equilibrium we call minimum between all of local-stable equilibria:

$$
\hat{\mathrm{G}}^{\mathrm{m}, \mathrm{n}}=\min _{\mathrm{p} \odot \mathrm{q}} \min _{\mathrm{k} \odot \mathrm{l}} \min _{\mathrm{i}, \mathrm{j}} \mathrm{G}_{\mathrm{k} \odot \mathrm{l}}^{\mathrm{i}, \mathrm{j}}
$$

(here minimum is taken over all types $k \odot l$ of two-phase equilibria between all local-stable two-phase equilibria).

We give detailed description of algorithm for construction of thermodynamically stable phase diagram (2PD), containing p disordered phases of variable and q phases of constant compositions at $(p,q)<10$. This algorithm consists of the following steps:
1) input data - values p and q; parameters of stability (PS) and - interactive parameters (PI) for all competing phases, and also inden- tifiers of all phases, values of compositions for phases of constant composition and array of temperatures $\{T_{i}\}$, ( each of them is necessary in order to calculate phase diagram) - are defined;
2) Value $T=T_{i}$ from array of temperatures named above is fixed;
3) In case of $p>1$ the next function is constructed:

$$
\tilde{G}(x)=\min _{1 \leq i \leq p}\left\{G^{i}(x, T) ; 0<x<1\right\}
$$

At first points $z^{i j}$ in pairs of intersection of thermodynamic poten- tials for phases of variable composition are sought as solutions of corresponding equations:

$$
G^{i}(z, T)=G^{j}(z, T), \quad i=1,2, \ldots, p-1, \quad j=i+1, \ldots, p.
$$

Array of points $\{z^{i j}\}$ produced by such way is arranged in increasing order:

$$
0<z^{1}<z^{2}<\ldots<z^{k}<1.
$$

On each of the constructed segments $\left[z^{j}, z^{j+1}\right]$ thermodynamic potential having on this segment a minimum value is selected:

$$
\tilde{G}(x)=\min _{1<i<p}\left\{G^{i}(x, T) ; x\left(\left[z^{j}, z^{j+1}\right]\right),\right.
$$

$$
j=0,1, \ldots, k ; \quad z^{j}=0, \quad z^{k+1}=1.
$$

In case of p=1 we have:

$$\tilde{G}(x, T) \equiv G^{p}(x, T).$$

In this case step 3 is missed and we go to step 5.

4) All of segments $[z^{j}, z^{j+1}]$ produced on step 3 are looked over; if
$$\tilde{G}=G^{i}(x) \quad \text { for } x \in\left[z^{j}, z^{j+1}\right]$$
and
$$\tilde{G}=G^{i}(x) \quad \text { for } x \in\left[z^{j+1}, z^{j+2}\right],$$
then segments $[z^{j}, z^{j+1}]$ and $[z^{j+1}, z^{j+2}]$ are "sticked" together in one segment $[z^{j}, z^{j+2}]$.

For example, in case equilibrium between 3 phases of variable compo- sition (Picture 1) point $z^{1}$ is a solution of equation $G^{\beta}(z)=G^{\gamma}(x)$, and points $z^{2}$ and $z^{3}$ - are solutions of equation $G^{\alpha}(z)=G^{\gamma}(x)$, thereby we have 4 segments: $[0, z^{1}],[z^{1}, z^{2}],[z^{2}, z^{3}],[z^{3}, 1]$. But on segments $[0, z^{1}]$ and $[z^{1}, z^{2}] \alpha$-phase is stable, thereby segments $[0, z^{1}]$ and $[z^{1}, z^{2}]$ are "sticked" together in one segment $[0, z^{2}]$. Particularly, in this case we have:

$$
\tilde{G}(x, T)=\left\{\begin{array}{ll}
G^{\alpha}(x, T), & 0 \leq x<z^{2}, \\
G^{\gamma}(x, T), & z^{2} \leq x \leq z^{3}, \\
G^{\alpha}(x, T), & z^{3}<x \leq 1.
\end{array} \quad \text { T=const. }\right.
$$

5) Knowing, what MTGE is minimal on segment $[z^{j}, z^{j+1}]$, we test: do points of inflection of this potential lie on this segment or not? We solve the next equation:
$$\frac{\partial^{2} G^{\alpha_{j}}}{\partial x^{2}}=0, \quad x \in[0,1],$$
and produce an array of roots to this equation: $x_{inf}^{\alpha_{j, 1}}, x_{inf}^{\alpha_{j, 2}},... x_{inf}^{\alpha_{j, 1}}$. We arrange it in increasing order and test: what elements of this - array are lie on segment $[z^{j}, z^{j+1}]$? If $x_{inf}^{\alpha_{j, k}}$ does not lie on segment $[z^{j}, z^{j+1}]$ for all $k=1,2,..., L$, then segment $[z^{j}, z^{j+1}]$ is not changed and we go to step 6. In another case we test: what kind of point of inflection for potential $G^{\alpha_{j}}(x)$ is the point $x_{inf}^{\alpha_{j, k}}$ - even or non-even?

If $X_{\text{inf}}^{\alpha_{j,k}}$ is a non-even point of inflection for $G^{\alpha_{j}}(x)$ potential, then we change right boundary of segment - $[z^{j},X_{\text{inf}}^{\alpha_{j,k}}]$ and test: does the preceding point of inflection $X_{\text{inf}}^{\alpha_{j,k-1}}$ lie on segment $[z^{j},z^{j+1}]$ or not?
If $X_{\text{inf}}^{\alpha_{j,k-1}}$ lie on this segment then we have make just one more segment - $[X_{\text{inf}}^{\alpha_{j,k-1}},X_{\text{inf}}^{\alpha_{j,k}}]$ otherwise we have segment $[z^{j},X_{\text{inf}}^{j}]$ and go to step 6.

If $X_{\text{inf}}^{\alpha_{j,k}}$ is even the point of inflection for $G^{\alpha_{j}}(x)$ potential we - change the left boundary of segment - $[X_{\text{inf}}^{\alpha_{j,k}},z^{j+1}]$ and test: does the point of inflection $X_{\text{inf}}^{\alpha_{j,k+1}}$ lie on segment $[z^{j},z^{j+1}]$ or not?

Suppose, $X_{\text{inf}}^{\alpha_{j,k+1}} \in[z^{j},z^{j+1}]$ then we changed the right boundary too and produce segment $[X_{\text{inf}}^{\alpha_{j,k}},X_{\text{inf}}^{\alpha_{j,k+1}}]$ and go to step 6. Otherwise $X^{\alpha_{j,k+1}} \notin [z^{j},z^{j+1}]$ segment $[z^{j},z^{j+1}]$ we change on $[X_{\text{inf}}^{\alpha_{j,k}},z^{k+1}]$ and also go to step 6. We note that region $[X_{\text{inf}}^{\alpha_{j,k}},X_{\text{inf}}^{\alpha_{j,k+1}}]$, when $X_{\text{inf}}^{\alpha_{j,k}}$ is a non-even point of inflection for $G^{\alpha_{j}}(x)$ potential, is not considered, - because it isn't region of allowable values for ends of tie-lines. As a result of execution of this step we produce segments of monotony for function $\tilde{G}_{x}$, on which $\tilde{G}_{xx}>0$ and this segments are regions of allowable values for tie-line ends. We shall designate this segments $[r^{j},r^{j+1}]$, where $j=1,2,\dots,M$. At Picture 1 as example we can see - equilibrium between two phases of variable composition.

Points $X_{\text{inf}}^{\alpha,1}$ and $X_{\text{inf}}^{\alpha,2}$ - are points of inflection for potential $G^{\alpha}(x)$.
We shade regions of composition, which are not regions of allowable values for tie-line ends.

6. We examine all phases of constant composition having composition - values $x^{k}$ and energy values $y^{k}=G^{k}(x^{k},T)$ respectively. From this array we throw away those, for wich at $T=T_{i}$: $\tilde{G}(x^{k})<G^{k}(x^{k})=y^{k},k=1,2,\dots,q$. We keep only those phases of constant composition for which the Gibbs energy lies lower then function $\tilde{G}(x)$ at $T=T_{i}$ (m - is their number);

7) A break up of function $\tilde{G}_{x}$ monotony segments, constructed on step 5 on which $\tilde{G}_{xx}>0$ by phases of constant composition produced after step 6. We test: does the composition value $x^{k}$ for the k-th phase of constant composition lies on segment $[r^{j},r^{j+1}]$ (here $k=1,2,\dots q$; $j=1,2,\dots,M$) or not?
If it lie on this segment, then segment $[r^{j},r^{j+1}]$ is broken on two

![](./images/813125811795132416_2.jpg)
![](./images/813125811795132416_3.jpg)

Pic.1. A scheme of concentration dependences at T=const of FGE for 3 phases
( $\alpha$, $\beta$ and $\gamma$ ) in binary system; $z^{1}, z^{2}$ and $z^{3}-$ are the roots of equations
$\Delta G^{\beta}(z)=\Delta G^{\gamma}(z), \Delta G^{\gamma}(z)=\Delta G^{\alpha}(z)$.

Pic.2. Concentration dependences at T=const of FGE for 2 competing phases
( $\alpha$ and $\beta$ ) ; $r^{3}=z^{1}$ and $r^{4}=z^{2}$ - are roots of $\Delta G^{\alpha}(x)=\Delta G^{\beta}(x) ; r^{2}=x_{inf}^{\alpha, 2}$, and
$r^{5}=x_{inf}^{\alpha, 2}-$ are points of inflection of $G^{\alpha}(x)$; segments on which there are no
ends of tie-lines (conodes) are shaded.

![](./images/813125811795132416_4.jpg)

Pic.3. Concentration dependence of FGE for $\alpha$-phase at T=const; $x_{0}^{k}$ and
$x_{0}^{k+1}-$ are values for the k-th and (k+1)-th phases of constant composition;
$x_{prom }$ - is root of equation $d \varphi / dx=0 ; x_{min}^{1}$ and $x_{min}^{2}$ - are "dummy" points
of minimum.

segments: $[r^j, x^k]$ and $[x^k, r^{j+1}]$. But if there are many values $x^k, x^{k+1}, ..., x^{k+L}$ on segment $[r^j, r^{j+1}]$ then we have:

$$[r^j, x^k], [x^k, x^{k+1}], ..., [x^{k+L}, r^{j+1}].$$

And if there is not anything on segment $[r^j, r^{j+1}]$ then this segment is not changed. Let us designate a number of segments constructed on this step as $m_1$: $[\hat{r}^j, \hat{r}^{j+1}],\ j=1,2,...,m_1$.

8) In case m>1, when a number of phases of constant composition is more then 1 (after step 6), we construct all metastable conodes of type $1 \oplus 1$ and select from them a local-stable conodes. As a result we produce enveloping curve $G_{0 \oplus 0}(x)$. If m=1 then this step is not produced.

9) On each segment $[\hat{r}^j, \hat{r}^{j+1}]$ (see step 7) a point of minimum of $\tilde{G}(x)$ function, is sought that is necessary condition for begining of const- ruction tie-lines of type $1 \oplus 1$ or $0 \oplus 1$ by U-algorithm. It may be that there is point of minimum on segment:

$$\left.rac{\partial^2 \tilde{G}}{\partial x^2}ight|_{x^i_{min}}>0,\qquad\left.rac{\partial \tilde{G}}{\partial x}ight|_{x^i_{min}}=0,$$

or not:

$$\left.rac{\partial^2 \tilde{G}}{\partial x^2}ight|_{x \in [\hat{r}^j, \hat{r}^{j+1}]}>0,\qquad\left.rac{\partial \tilde{G}}{\partial x}ight|_{x \in [\hat{r}^j, \hat{r}^{j+1}]}\neq0$$

As a "dummy" point of minimum we choose the left or right boundary of segment $[\hat{r}^j, \hat{r}^{j+1}]$ on which value of $\tilde{G}(x)$ is minimal:

$$X_{min}=\left\{
egin{array}{ll}
\hat{r}^j,\ \text{if}\ \tilde{G}(\hat{r}^j,T)<\tilde{G}(\hat{r}^{j+1},T) \
\hat{r}^{j+1},\ \text{if}\ \tilde{G}(\hat{r}^j,T)>\tilde{G}(\hat{r}^{j+1},T)
\end{array}
ight.\quad T=\text{const}.$$

Separately we consider a case when there is intersection $\tilde{G}(x)$ with one of segments of $G_{0 \oplus 0}(x)$. Suppose,

$$v(x)=\tilde{G}(x)-k*x-b,$$

$$
k=\frac{G_{f}^{i}\left(x_{0}^{i}\right)-G_{f}^{i+1}\left(x_{0}^{i+1}\right)}{x_{0}^{i}-x_{0}^{i+1}}
$$

$$
b=G_{f}^{i}\left(x_{0}^{i}\right)-k * x_{0}^{i}
$$

here $x_{0}^{i}$ - is a composition value for the i-th phase of constant composition (in this case $x_{0}^{i} \equiv \hat{r}^{i} ; x_{0}^{i+1}=\hat{r}^{i+1}$ ), $G_{f}^{i}\left(x_{0}^{i}\right)$ - is a potential value in this point. The function $\varphi(x)$, defined above is considered on segment $\left[x_{0}^{i}, x_{0}^{i+1}\right] \equiv\left[\hat{r}^{i}, \hat{r}^{i+1}\right]$. We search all roots of equation

$$
\frac{d \varphi}{d x}=0, \quad x \in\left[\hat{r}^{i}, \hat{r}^{i+1}\right]
$$

Suppose $x_{\text {prom }}$ - is a root of this equation\& If $\varphi\left(x_{\text {prom }}\right)<0$, then $\tilde{G} \cap$ $G_{\Omega \oplus 0} \neq \emptyset$ and segment $\left[\hat{r}^{i}, \hat{r}^{i+1}\right]$ by point $x_{\text {prom }}$ is broken on two segments: $\left[r^{i}, x_{\text {prom }}\right]$ and $\left[x_{\text {prom }}, \hat{r}^{i+1}\right]$. On each of constructing segments we solve an equation:

$$
\varphi(x)=0
$$

As a result we have points of intersection $\tilde{G}$ with $G_{0 \oplus 0}$ and remember them as a "dummy" points of minimum. This case is illustrated in - Picture 3; points of intersection $\tilde{G} \cap G_{0 \oplus 0}$ ("dummy" points of minimum) are designated as $x_{\min }^{1}$ and $x_{\min }^{2}$.

10) The search of possible two-phase equilibria of type 1@1 between the $i$-th and $j$-th phases on segments $\left[\hat{r}^{i}, \hat{r}^{i+1}\right]$ and $\left[\hat{r}^{j}, \hat{r}^{j+1}\right]$ correspondently is carried out; here $i=1,2, \ldots m_{1}-1, ; j=i+1, \ldots, m_{1}$.

11) On this step construction of meta-stable conodes of types 1@1 and 1@0 and selection of thermodynamically stable two-phase conodes is implemented. Let us designate: $x_{\min }^{i}$ - is the $i$-th point of minimum (see step 9), $x^{k}$ - is the k-th composition value for corresponding phase of constant composition (see step 8) $x \in G_{0 \oplus 0}$. At first $i=1$ and $j=1$.

11.a) Let $x_{\min }^{i}<x^{k}$, then we construct all of metastable conodes of type $1 \oplus 0$, emerging from $x_{\min }^{i}$, and select from them a local-stable conode $\bar{G}_{1 \oplus 0}^{i, 1}$. Then we construct all of meta-stable conodes of type 1@1, also emerging from point $x_{\min }^{i}$ and select from them a local-stable conode $\bar{G}_{1 \oplus 1}^{i, j}$. Later we choose intermediate point $x^{*}$, in which functions $\bar{G}_{1 \oplus 0}^{i, 1}$

and $\bar{G}_{1 \oplus 1}^{i, j}$ are defined and examine stability condition. If $\bar{G}_{1 \oplus 0}^{i, l}(x^{*})<\bar{G}_{1 \oplus 1}^{i, j}(x^{*})$, (it means that $\bar{G}_{1 \oplus 0}^{i, l}$ is stable) then it's coordinates are remembered. Then we search the first point of minimum lying on the right side of $x^{l}$ (let n be it's number) and go to step 11.b, taking $x_{min}^{i}$ on a value $x_{min}^{n}$, and $x^{k}-$ on a value $x^{l}$.

If $\bar{G}_{1 \oplus 0}^{i, l}(x^{*})>\bar{G}_{1 \oplus 1}^{i, j}(x^{*})$ (it means that $\bar{G}_{1 \oplus 1}^{i, j}$ is stable) we also remember it's coordinates as coordinates of global-stable conode, then we -search the first composition value lying on the right side of $x_{min}^{i}$ (let m be it's number) and go to step 11.a, taking $x_{min}^{i}$ on a value $x_{min}^{j}$, and $x^{k}$ on a value $x^{m}$.

11.b) Let $x_{min}^{i}>x^{k}$ , then we construct all meta-stable conodes of type $0 \oplus 1$ , emerging from point $x^{k}$ and select a local-stable conode - $\bar{G}_{1 \oplus 0}^{k, j}$, (here j - is a number of corresponding to a point of minimum). We - examine, does the next composition value lie between $x^{k}$ and $x_{min}^{j}$ or not? If $x^{k}<x_{min}^{j}<x^{k+1}$ , then we choose intermediate point $x^{*}$, where functions $\bar{G}_{0 \oplus 1}^{k, j}(x)$ and $\bar{G}_{0 \oplus 0}^{k, k+1}(x)$ are defined, and we test stability condition.

If $\bar{G}_{0 \oplus 1}^{k, j}(x^{*})<\bar{G}_{0 \oplus 0}^{k, k+1}(x^{*})$ ( it means that $\bar{G}_{0 \oplus 1}^{k, j}(x)$ is stable), then we remember their coordinates and search the first composition value for the phase of constant composition lying on the right side of $x_{min}^{j}$ (let n be a number of such value) and go to step 11.a, taking $x_{min}^{i}$ on a value $x_{min}^{j}$, and $x^{k}$ on a value $x^{n}$. If $\bar{G}_{0 \oplus 1}^{k, j}(x^{*})>\bar{G}_{0 \oplus 0}^{k, k+1}(x^{*})$ (it means that $\bar{G}_{0 \oplus 0}^{k, k+1}$ is stable ) we remember it's coordinates and go to step 11.b, taking $x_{min}^{i}$ on a value $x_{min}^{j}$, and $x^{k}$ on a value $x^{k+1}$. But if $x^{k}<x^{k+1}<x_{min}^{j}$, then coordinates of $\bar{G}_{0 \oplus 0}^{k, k+1}$ are remembered and we go to step 11.a, taking $x_{min}^{i}$ on a value $x_{min}^{j}$, and $x^{k}$ on a value $x^{k+1}$.

12) Construction phases of constant composition lie higher than $\tilde{G}(x)$, if $q=0$ or if construction of meta-stable conodes on step 11 finished on construction of $0 \oplus 1$ conode and there are no phases of constant - composition) and selection of global-stability from them are carried out on this step.

13) Temperature T takes on a new value from temperature array $\{T_{i}\}$, $T=T_{i+1}$, and we go to step 3 again.

14) As a result of this algorithm we have:
1) a number of global-stable conodes at $T=T_{i}$;

2) compositions of phase boundaries and indentifiers of thermodyna- mically stable phases.

We note that this algorithm may be used for construction of - thermodynamic stable phase diagrams, containing only p disordered - phases of variable composition and for construction of binary phase diagrams, containing p disordered phases of variable and q phases of constant composition.

### Examples of algorithm application

1. One example is the construction of a thermodynamic stable binary phase diagram of Ni-Al system based on lattice stability and interac- tion parameters, which were produced by L.Kaufman [9], this - illustrates the algorithm work. In Picture 4 the whole phase diagram of this system is represented. We consider equilibrium between 3 - disordered phases of variable composition: L-(liquid), FCC- and BCC- phases (p=3) and 3 phases of constant composition - chemical - compounds: $Ni_{0.75}Al_{0.25}$ , $Ni_{0.4}Al_{0.6}$ , $Ni_{0.25}Al_{0.75}$ (q=3). Let us take a several temperature sections of this phase diagram (see at Pict.5).
At $T_{1}$=700 K (Picture 5.a).

It is convenient to designate $FCC=\gamma$ and $BCC=\beta$ phases. In Picture 5.a you can see the molar thermodynamic Gibbs energy for the competing phases at this temperature. After execution step 3 we have: $z^{1}$, $z^{2}-$ are the roots of equation $G^{\gamma}(z)=G^{\beta}(z)$; $T=T_{1}$ and

$$
G\left(x, T_{1}\right)=\left\{\begin{array}{l}
G^{\gamma}\left(x, T_{1}\right), \quad 0<x \leq z^{1}, \\
G^{\beta}\left(x, T_{1}\right), \quad z^{1} \leq x \leq Z^{2}, \quad T_{1}=\text { const. } \\
G^{\gamma}\left(x, T_{1}\right), \quad z^{2}<x \leq 1.
\end{array}\right.
$$

Since there are no points of inflection for any MTGE on [0,1], so - after step 5 we obtain:

$$
\begin{aligned}
& r^{1}=0 ; r^{2}=z^{1} ; \\
& r^{3}=z^{1} ; r^{4}=z^{2} ; \\
& r^{5}=z^{2} ; r^{6}=1.
\end{aligned}
$$

![](./images/813125811795132416_5.jpg)

Pic.4. Phase diagram of Ni-Al system, calculated from parameters of lattice stability and interactions for excess MTGE (Liquid),FCC (γ)- and BCC (β) - phases, and also on stability parameters of Ni, Al and chemical compounds $Ni_3Al$, $Ni_2Al_3$ and $NiAl_3$, obtained in [9].

Execution of step 6 gets us the next results:
$x^1$=0.25 ($Ni_{0.75}Al_{0.25}$); $x^2$=0.6 ($Ni_{0.4}Al_{0.6}$); $x^3$=0.75 ($Ni_{0.25}Al_{0.75}$).

According to step 7 we break segments $[\hat{r}^i,\hat{r}^{i+1}]$ by phases of constant composition and obtain dividing of segment [0,1] on 6 segments:
1) $\hat{r}^1$=0; $\hat{r}^2$=$z^1$ $[0,z^1]$, is stable $\gamma$-phase,
2) $\hat{r}^3$=$z^1$; $\hat{r}^4$=$x^1$ $[z^1,x^1]$, is stable $\beta$-phase,
3) $\hat{r}^5$=$x^1$; $\hat{r}^6$=$x^2$ $[x^1,x^2]$, is stable $\beta$-phase,
4) $\hat{r}^7$=$x^2$; $\hat{r}^8$=$x^3$ $[x^2,x^3]$, is stable $\beta$-phase,
5) $\hat{r}^9$=$x^3$; $\hat{r}^{10}$=$z^2$ $[x^3,z^2]$, is stable $\beta$-phase,
6) $\hat{r}^{11}$=$z^2$; $\hat{r}^{12}$=1  $[z^2,1]$, is stable $\gamma$-phase.

According to step 8 we construct $G_{0 \otimes 0}(x)$ for all phases of constant composition, which is defined in this case only on two segments: $[x^1,x^2]$ and $[x^2,x^3]$.

On earch of 6 segments $[\hat{r}^i,\hat{r}^{i+1}]$ we search points of minimum (step 9) and we have 6 such points:
$$0 < x^1_{\text{min}} < x^2_{\text{min}} < ... < x^6_{\text{min}} < 1$$

$$x_{min}^{1}=z^{1}\in [0,z^{1}]$$

$$x_{min}^{2}=x^{1}\in [z^{1},x^{1}]$$

$$x_{\min }^{3} \in\left[x^{1}, x_{\text {prom }}\right], x_{\text {prom }}-\text { is a root of } \frac{d \varphi}{d x}=0,$$

$$x_{min}^{4}\in [x_{prom},x^{2}]$$

$$x_{min}^{5}=x^{3}\in [x^{3},z^{2}]$$

$$x_{min}^{6}=z^{2}\in [z^{2},1]$$

Later we search possible two-phase equilibria (step 10) for equilib- rium of $1 \otimes 1$ type and go to step 11. Since $x_{min}^{1}<x^{1}$ , then we execute11.a and obtain global-stable conode of $1 \otimes 0$ type, ends of which lies between $x_{min }^{1}$ and $x^{1}$ ; then we move on to 11.b and obtain global-stable conode of $0 \otimes 1$ type, ends of which lie between $x^{1}$ and $x_{min }^{3}$ ; we move on to 11.a and obtain global-stable conode of $1 \otimes 0$ type, ends of which lie between $x_{min }^{4}$ and $x^{2}$ ; move on to 11.b, but since $x^{2}<x^{3}=x_{min }^{5}$ , then we remember as a global-stable conode of $0 \otimes 0$ type with coordinates $[x^{2}, x^{3}]$ and move on to 11.b again, and we obtain global-stable conode of $0 \otimes 1$ type, ends of which lie between $x^{3}$ and $x_{min }^{6}$ . As a result $T=700 ~K$ we have 5 global-stable conodes (tie-lines):

1) $x^{\gamma / \gamma+1}=0.110408 ; x^{1}=0.25$ ;
2) $x^{1}=0.25 ; x^{1+\beta / \beta}=0.381279$ ;
3) $x^{\beta / \beta+2}=0.424394 ; x^{2}=0.6$ ;
4) $x^{2}=0.6 ; x^{3}=0.75$ ;
5) $x^{3}=0.75 ; x^{3 / 3+A l}=0.9999439$ .

At $T_{2}=1200 ~K$ (Picture 5.b).

After execution step 3 we have: $z^{1}$ - is root of equation $G^{\gamma}(z)=G^{\beta}(z)$ and $z^{2}$ - is root of $G^{\beta}(z)=G^{L}(z)$ , therefore

$$G\left(x, T_{2}\right)=\left\{\begin{array}{ll}
G^{\gamma}\left(x, T_{2}\right), & 0<x \leq z^{1}, \\
G^{\beta}\left(x, T_{2}\right), & z^{1} \leq x \leq Z^{2}, \quad T_{2}=\text { const. } \\
G^{L}\left(x, T_{2}\right), & z^{2}<x \leq 1.
\end{array}\right.$$

![](./images/813125811795132416_6.jpg)

Pic.5. Concentration dependences at 700 K (a), 1200 K (b) and 1500 K (c) of MTGE for phases of variable composition $(L,\beta,\gamma)$ and phases of constant composition $(Ni_{0.75}Al_{0.25},Ni_{0.4}Al_{0.6},Ni_{0.25}Al_{0.75})$ in Ni-Al system

and $z^{2}$ - is root of $G^{\beta}(z)=G^{L}(z)$, therefore

$$
\tilde{G}(x, T_{2})=
\begin{cases}
G^{\gamma}(x, T_{2}), & 0<x \leq z^{1}, \\
G^{\beta}(x, T_{2}), & z^{1} \leq x \leq Z^{2}, \\
G^{L}(x, T_{2}), & z^{2}<x \leq 1.
\end{cases} \quad T_{2}=\text{const}.
$$

Execution of step 5 is analogous to the preceding example $T_{1}=700$ K:
$$
\begin{aligned}
& r^{1}=0 ; \quad r^{2}=z^{1} ; \\
& r^{3}=z^{1} ; r^{4}=z^{2} ; \\
& r^{5}=z^{2} ; r^{6}=1.
\end{aligned}
$$

Execution of step 6 leads to omitting of the 3-d compound: $Ni_{0.25} Al_{0.75}$, since it's Gibbs energy lies higher than $\tilde{G}(x, T_{2})$ (see at Pic.5.b). Only two compounds $x^{1}=0.25$ and $x^{2}=0.6$ ( $Ni_{0.75} Al_{0.25}$ and $Ni_{0.4} Al_{0.6}$ ). After breaking (step 7) of segments $[r^{i}, r^{i+1}]$ by phases of constant composition we obtain:
1) $\hat{r}^{1}=0 ; \hat{r}^{2}=z^{1}\left[0, z^{1}\right]$, is stable $\gamma$-phase,
2) $\hat{r}^{3}=z^{1} ; \hat{r}^{4}=x^{1}\left[z^{1}, x^{1}\right]$, is stable $\beta$-phase,
3) $\hat{r}^{5}=x^{1} ; \hat{r}^{6}=x^{2}\left[x^{1}, x^{2}\right]$, is stable $\beta$-phase,
4) $\hat{r}^{7}=x^{2} ; \hat{r}^{8}=z^{2}\left[x^{2}, z^{2}\right]$, is stable $\beta$-phase,
5) $\hat{r}^{9}=z^{2} ; \hat{r}^{10}=1\left[z^{2}, 1\right]$, is stable L-phase.

According to step 8 we construct $G_{0 \oplus 0}(x)$ which consists of only one segment: $[x^{1}, x^{2}]$. On each of 5 segments $[\hat{r}^{i}, \hat{r}^{i+1}]$ we search for points of minimum (step 9). In this case there are 6 points of minimum, since on segment $[x^{1}, x^{2}]$ lie 2 "dummy" points of minimum obtained as roots of equation $\varphi(x)=0$. Therefore:

$$
0<x_{\text {min }}^{1}<x_{\text {min }}^{2}<\ldots<x_{\text {min }}^{6}<1
$$

$$
x_{\text {min }}^{1}=z^{1} \in\left[0, z^{1}\right]
$$

$$
x_{\text {min }}^{2}=x^{1} \in\left[z^{1}, x^{1}\right]
$$

$$
x_{\text {min }}^{3} \in\left[x^{1}, x_{\text {prom }}\right], x_{\text {prom }}-\text { is root } \frac{d \varphi}{d x}=0,
$$

$$x_{min}^{4} \in [x_{prom}, x^{2}]$$

$$x_{min}^{5}=x^{2} \in [x^{2}, z^{2}]$$

$$x_{min}^{6}=z^{2} \in [z^{2}, 1]$$

Later search of possible two-phase equilibria (step 10) for equilibria of $1 \odot 1$ type is carried out. Construction and selection of global-stable conodes (step 11) begins in this case on step 11.a, because $x_{min}^{1}<x^{1}$ - there is global-stable conode of type $1 \odot 0$ ends of which lie between $x_{min}^{1}$ and $x^{1}$; then we go to 11.b and have global-stable conode of $0 \odot 1$ type with ends lying between $x^{1}$ and $x_{min}^{3}$; we go to 11.a again and obtain global-stable conode of $1 \odot 0$ type with ends lying between $x_{min}^{4}$ and $x^{2}$; after execution 11.b we obtain global-stable conode of $0 \odot 1$ type with ends lying between $x^{2}$ and $x_{min}^{6}$. So we have 4 global-stable conodes at $T_{2}=1200$ K:

1) $x^{\gamma / \gamma+1}=0.148048085 ; x^{1}=0.25$;

2) $x^{1}=0.25 ; x^{1+\beta / \beta}=0.3574774$;

3) $x^{\beta / \beta+2}=0.48315199 ; x^{2}=0.6$;

4) $x^{2}=0.6 ; x^{2 / 2+L}=0.802026195$.

At $T_{3}=1500$ K (Picture 5.c)
Execution of step 3 gets us the next function $\tilde{G}(x)$:

$$
\tilde{G}\left(x, T_{3}\right)=
\begin{cases}
G^{\gamma}\left(x, T_{3}\right), & 0<x \leq z^{1}, \\
G^{\beta}\left(x, T_{3}\right), & z^{1} \leq x \leq z^{2}, \\
G^{L}\left(x, T_{3}\right), & z^{2}<x \leq 1.
\end{cases}
\quad T_{3}=\text{const}.
$$

where $z^{1}$- is root of $G^{\gamma}(z)=G^{\beta}(z)$, and $z^{2}$- is root of $G^{\beta}(z)=G^{L}(z)$.

Execution of step 5 is analogous to preceding example :

$$r^{1}=0 ; r^{2}=z^{1} ;$$

$$r^{3}=z^{1} ; r^{4}=z^{2} ;$$

$$r^{5}=z^{2} ; r^{6}=1.$$

But on step 6 two compounds $Ni_{0.4}Al_{0.6}$ and $Ni_{0.25}Al_{0.75}$ are expected, because their Gibbs energies lie higher than constructed function $\tilde{G}(x)$ (see at Pic.5.c). Execution of step 7 is also analogous to the prece- ding example. Division of segments $[r^{i}, r^{i+1}]$ gets us the next results:

1) $\hat{r}^{1}=0$; $\hat{r}^{2}=z^{1} \ [0,z^{1}]$, is stable $\gamma$-phase,
2) $\hat{r}^{3}=z^{1}$; $\hat{r}^{4}=x^{1} \ [z^{1},x^{1}]$, is stable $\beta$-phase,
3) $\hat{r}^{5}=x^{1}$; $\hat{r}^{6}=z^{2} \ [x^{1},z^{2}]$, is stable $\beta$-phase,
4) $\hat{r}^{7}=z^{2}$; $\hat{r}^{8}=1 \ [z^{2},1]$, is stable L-phase.

Step 8 is expected, because at this temperature there is only one - thermodynamically stable compound - $(Ni_{0.75}Al_{0.25})$. After search of minimum points we obtain:

$$
0 < x_{min}^{1} < x_{min}^{2} < ... < x_{min}^{4} < 1
$$

$$
x_{min}^{1}=z^{1} \in [0,z^{1}]
$$

$$
x_{min}^{2}=x^{1} \in [z^{1},x^{1}]
$$

$$
x_{min}^{3} \in [x^{1},z^{2}]
$$

$$
x_{min}^{4} \in [z^{2},1].
$$

Later we search for possible two-phase equilibria between equilibria of $1 \odot 1$ type and go to step 11. At first we execute 11.a, because $x_{min}^{1}<x^{1}-$ and obtain global-stable conode of $1 \odot 0$ type with ends lying between $x_{min}^{1}$ and $x^{1}$; after 11.b we also have global-stable conode of $0 \odot 1$ type with ends lying between $x^{1}$ and $x_{min}^{3}$; at last we go to step 12, because there is only one stable compound at this temperature and obtain global-stable conode of $1 \odot 1$ type with ends lying between $x_{min}^{3}$ and $x_{min}^{4}$. As a result we have 3 global-stable conodes at this temperature $T_{3}=1500$ K:

1) $x^{\gamma / \gamma+1}=0.1839456$; $x^{1}=0.25$;
2) $x^{1}=0.25$; $x^{1+\beta / \beta}=0.31850038$;
3) $x^{\beta / \beta+L}=0.5942148$; $x^{\beta+L / L}=0.642003313$.


### Applications of the constructed program to the calculation of phase diagrams of several binary systems.

The calculation method for the construction of thermodynamically stable binary phase diagrams defined above, has been used by the - authors successfully for solving of direct and reverse problems. A whole set of autonomic programs was constructed for IBM PC based on this method. This set of programs allows us to calculate phase diagrams of different types: phase diagrams, containing only disordered phases of variable composition and diagrams, containing phases of variable and constant compositions. We want to illustrate our method and give some examples of its application.

1. Calculation of the miscibility gap of BCC-solutions in Cr - W sys- tem (Picture 6 - we have immiscibility within one disordered phase of variable composition) was carried out after reverse problem solving and calculating of interaction parameters for BCC-phase on the basis of experimental data on phase equilibria ( see [10] ).

2. As a test for this program the authors calculated the phase diagram of Al-Si system using lattice stability and interaction parameters for liquid, FCC- phases and solid solution with diamond structure on base of Si from [12]. Results are represented in Picture 7a-7b (7a - the whole phase diagram, 7b - part of this diagram for alloys rich in Si. Please, pay attention that the scale in picture 7b was increased in 5000 times on comparison with picture 7a; and accuracy of calculations for tie-lines ends is $10^{-8}$).

3. Construction of part of the binary phase diagram of Ni - W system (equilibrium between Liquid, FCC and BCC phases) was also carried out after solution of reverse problem and calculation of interaction para- meters for all named phases based on experimental data for phase equi- libria and thermodynamic properties of FCC-solutions ( also see [10], Picture 8).

4. Calculation of phase diagram of Ni-Cr system (equilibrium between Liquid, FCC and BCC phases) was also carried out after reverse problem solving and searching interactive parameters for all competing phases with using of experimental data on phase equilibria and thermodynamic properties of L, Fcc and Bcc phases ( see [11], Picture 9).

5. Calculation of Ni-Al phase diagram (Picture 4) was carried out on literature data from [9].

![](./images/813125811795132416_7.jpg)

Pic.6. Calculated curve of immiscibility of BCC-solutions in Cr-W - system and experimental points [10].

![](./images/813125811795132416_8.jpg)

Pic.7a. Calculated phase diagram of Al-Si system (equilibrium of - liqiud, FCC- phases and solid solution on base of Si with diamond - structure). Pic.7b. A part of calculated phase diagram of Al-Si for alloys rich in Si.

![](./images/813125811795132416_9.jpg)

Pic.8. Comparison of results of thermodynamic calculation of optimized experimental data on phase equilibria and chemical potential W for FCC - solutions on base of Ni [10] with experimental data (points) for the Ni - W system.

![](./images/813125811795132416_10.jpg)

Pic.9. Results of optimized calculation [11] of phase diagram of the Ni - Cr system, equilibrium between Liquid, FCC ($\gamma$) and BCC ($\alpha$) phases was considered.

### References.

1. L. Kaufman, H. Bernstein, "Computer calculation of phase diagrams", Academic Press, New York (1970).

2. M. Hillert, "Some viewpoints on the use of a computer for calcu- lating phase diagrams", Physica, V.103B, N 1, p.31 (1981).

3. I. Ansara, "Comparison of methods for thermodynamic calculation of phase diagrams", Intern. Metals. Rev., N 1, p.20 (1979).

4. J.N. Barbier, P.Y. Chevalier, I. Ansara, "A general method of cal- culating phase equilibria in a multicomponent system by means of a hill -climbing minimization procedure", Thermochim. Acta, V.70, p.173 (1983).

5. A.L. Udovsky, "Thermodynamic calculations of phase diagrams of - metallic systems", in "Phase diagrams in materials", Kiev, IPM Ukraine Academy of Sciences, p.36 (1979).

6. A.L. Udovsky,"Computer simulation of phase diagrams, thermodynamic properties and structure of the multicomponents systems", Academy - Sciences Review, USSR, Metalls, N 2, p.136 (1990).

7. A.L. Udovsky, V.N. Karpushkin, E.K. Rodionova, "About convergence of one algorithm of thermodynamic calculation of phase equilibria in binary systems", V All-Union School "Application of mathematical - methods for description and investigation of phisico-chemical equilib- ria", Novosibirsk, Nauka, p.14 (1985) (in Russian).

8. V.N. Karpushkin,"Algorithm of search of general tangent hyper- plane", Successes of Mathematical Sciences, v.41, N 4, p.207 (1986) (in Russian).

9. L. Kaufman, H. Nesor, "Coupled phase diagrams and thermochemical data for transition metal binary systems - $V^{*}$", Calphad, V.2, N 4, p.325 (1978).

10. A.L. Udovsky, E.A. Nikishina, "Solution of reverse problems with using of phase diagrams topology by method of direct optimization in systems Cr-W and Ni-W", VI All-Union School ""Application of mathema- tical methods for description and investigation of physico-chemical equilibria", Novosibirsk, Nauka, part 2, p.44 (1989) (in Russian).

11. A.L. Udovsky , E.A. Kozodaeva, "An optimized calculation of phase diagram and thermodynamic properties of the Ni-Cr system", Calphad, V.17, N 1, p.17 (1993).

12. P.Dorner, E.Th.Henig, H.Krieg, H.L.Lukas, G.Petzov. CALPHAD, v.4, N 4, p.241 (1980).

### Appendix I.

#### 1. Prepositions of theorems 1.1. and 1.2.

Let $f_1: [a_1,b_1] \Rightarrow \mathbb{R}$, $f_2: [a_2,b_2] \Rightarrow \mathbb{R}$ are strict convex and smooth functions, $a_1< b_1 < a_2 < b_2$. Let $f^{(k)}(x)$ denote k-derivatives of function $f$ in the point $x$; $f^{(k)}(g(x))$ is $f^{(k)}(\bar{x})$, where $\bar{x}=g(x)$.

Suppose, that there exist points $y$ and $z$:
$$f_1^{(1)}(y) = f_2^{(1)}(z) = (f_1(y) - f_2(z))*(y - z)^{-1},\ a_1< y < b_1,\ a_2< z < b_2,$$
$(y,z)$ are coordinates of ends of the tie-line.

From the theorem about the implicit function we get: there exists a strictly monotone function $\varphi:[p,q] \Rightarrow [a_2,b_2]$ with $f_1^{(1)}(x) = f_2^{(1)}(\varphi(x))$; $z = \varphi(y)$ for all $p \leq x \leq q$. There is one of four pair cases:
$p = a_1$or $\varphi(p) = a_2$; $q = b_1$or $\varphi(q) = b_2$.

Let $\Psi(x) = (f_1(x) - f_2(\varphi(x)))*(x - \varphi(x))^{-1}$.

The definition of algorithm is the following: $f_1^{(1)}(x_{n+1}) = \Psi(x_n)$.
This algorithm is converging locally to the point $y$ with the speed $\ge 2$.
This follows from the article [8].

Theorem 1.1. Let $s$ be the minimum natural number with a property of $f_1^{(s)}(y) \neq f_2^{(s)}(\varphi(y))$. Then $s \geq 2$, there exists in the neighborhood $v$ of the point $y$ with a property: for all $x_1 \in v$ the sequence $x_n$ belongs to $v$ and is converging to $y$ with the speed of $s$.

1. Let us suppose that $s$ is even.
A) if $f_1^{(s)}(y) > f_2^{(s)}(\varphi(y))$, then the sequence $x_n$ gets down monotonically at $n \geq 2$.
B) if $f_1^{(s)}(y) < f_2^{(s)}(\varphi(y))$, then the sequence $x_n$ gets up monotonically at $n \geq 2$.

2. Let us suppose that $s$ is odd.
A) if $f_1^{(s)}(y) > f_2^{(s)}(\varphi(y))$, then the sequence $x_n$ is monotone at $n \geq 1$.
B) if $f_1^{(s)}(y) < f_2^{(s)}(\varphi(y))$, then $(x_n - y)*(x_{n+1}- y)\leq 0$ at $n \geq 1$.

Let $Q = \{ x:\ p\leq x\leq q\}$.

Theorem 1.2. Suppose, that $f_1^{(1)}(q) \geq \Psi(x) \geq f_1^{(1)}(p)$ for all $x \in Q$; $f_1^{(2)}(x) \neq f_2^{(2)}(\varphi(x))$, if $x \neq y$. Let $s$ be the minimum natural number with - the property: $f_1^{(s)}(y) \neq f_2^{(s)}(\varphi(y))$ and either A) $s = 2k$, or B) $s = 2k+1$, $f_1^{(s)}(y) > f_2^{(s)}(\varphi(y))$.

Then the sequence $x_n$ is converging with a speed of $s$ to the point $y$ for any $x \in Q$. In case A)the sequence $x_n$ is monotone at $n \geq 2$.

In case B)the sequence $x_n$ is monotone at $n \geq 1$.

Remark 1.3. The condition $f_1^{(1)}(q) \geq \Psi(x)\geq f_2^{(1)}(p)$ for all $x \in Q$ is

equivalent to the fact that algorithm is defined for all $x \in Q$.

Remark 1.4. If $f_{1}^{(i)}(y)=f_{2}^{(i)}(\varphi(y))$ with $i \geq 2$, then the algorithm is converging locally to $y$ with a speed greater than every positive number.

### 2.Proofs of theorems 1.1 and 1.2.

#### Lemma 2.1.
1. $\Psi^{(1)}(x)=(1-\varphi^{(1)}(x))*(f_{1}^{(1)}(x)-\Psi(x))*(x-\varphi(x))^{-1}$.
2. $f_{1}^{(1)}(y)=\Psi(y)$.
3. $\Psi^{(1)}(y)=0$.
4. Let $\varphi^{(1)}(y)=1$, then $\Psi^{(2)}(y)=0$, $\Psi^{(3)}(y)=\{2\varphi^{(2)}(y)*f_{1}^{(2)}(y)\}*\{\varphi(y)-y\}^{-1}$.
5. Let $f_{1}^{(2)}(y)\neq f_{2}^{(2)}(\varphi(y))$, then $\{f_{1}^{(2)}(y)-f_{2}^{(2)}(\varphi(y))\}*\Psi^{(2)}(y)>0$.

The proof of lemma 2.1. The statements 1,2,3,4 are obvious. Let us prove statement 5. We know: $f_{1}^{(2)}(y)=\varphi^{(1)}(y)*f_{2}^{(2)}(\varphi(y))$. Now we get: if $f_{1}^{(2)}(y)>f_{2}^{(2)}(\varphi(y))$, then $\varphi^{(1)}(y)>1$; if $f_{1}^{(2)}(y)<f_{2}^{(2)}(\varphi(y))$, then $\varphi^{(1)}(y)<1$.

Consider $\Psi^{(2)}(y)=(1-\varphi^{(1)}(y))*f_{1}^{(2)}(y)/(y-\varphi(y))$.

If $f_{1}^{(2)}(y)>f_{2}^{(2)}(\varphi(y))$, then $\varphi^{(1)}(y)>1$, $\Psi^{(2)}(y)>0$,
if $f_{1}^{(2)}(y)<f_{2}^{(2)}(\varphi(y))$, then $\varphi^{(1)}(y)<1$, $\Psi^{(2)}(y)<0$.

#### Proposition 2.2. Let $f_{1}^{(r)}(y)=f_{2}^{(r)}(\varphi(y))$ be with $2 \leq r \leq i$.
Let $f_{1}^{(i+1)}(y)\neq f_{2}^{(i+1)}(\varphi(y))$, then $\Psi^{(r)}(y)=0$ with $2 \leq r \leq i$,
$\{f_{1}^{(i+1)}(y)-f_{2}^{(i+1)}(\varphi(y))\}*\Psi^{(i+1)}(y)>0$.

The proof of the proposition 2.2 follows from lemma 2.3 and 2.4.

#### Lemma 2.3. 1.Let $f_{1}^{(r)}(y)=f_{2}^{(r)}(\varphi(y))$ be at $2 \leq r \leq t$.
2. Let $f_{1}^{(t+1)}(y)\neq f_{2}^{(t+1)}(\varphi(y))$, then $\varphi^{(t)}(y)=1$, $\varphi^{(j)}(y)=0$
at $2 \leq j \leq t-1$; $\{f_{1}^{(t+1)}(y)-f_{2}^{(t+1)}(\varphi(y))\}*\varphi^{(t)}(y)>0$.

The proof of the lemma 2.3. Let us differentiate $1,\dots,t$ times the identity $f_{1}^{(1)}(x)=f_{2}^{(1)}(\varphi(x))$. From conditions
$f_{1}^{(r)}(y)=f_{2}^{(r)}(\varphi(y))$ with $2 \leq r \leq t$ we get equations:
$f_{1}^{(2)}(y)=f_{2}^{(2)}(\varphi(y))*\varphi^{(1)}(y),\dots$,
$f_{1}^{(\nu+1)}(y)=\varphi^{(\nu)}(y)*f_{2}^{(2)}(\varphi(y))+\dots+(\varphi^{(1)}(y))^{\nu}*f_{2}^{(\nu+1)}(\varphi(y))$, where
$2 \leq \nu \leq t-1$.

From these equations, strict convex of function $f_{2}$ and conditions
$f_{1}^{(r)}(y)=f_{2}^{(r)}(\varphi(y))$, where $2 \leq r \leq t$, we obtain $\varphi^{(1)}(y)=1$, $\varphi^{(\nu)}(y)=0$,
where $2 \leq \nu \leq t-1$. Now we get
$f_{1}^{(t+1)}(y)=\varphi^{(t)}(y)*f_{2}^{(2)}(\varphi(y))+f_{2}^{(t+1)}(\varphi(y))$

continuous function. Suppose that there exists point $y$: $f^{(1)}(y)= \{f(y)-$ $c\} /(y-d)$, where $a < y < b$, $b < d$; $c$, $d$ are parameters of the line chemi- cal compound, $y$ and $d$ are coordinates of ends of the tie-line. Let $\Psi(x)=$ $(f(x)-c) /(x-d)$. The definition of algorithm is following $f^{(1)}(x_{n+1})=$ $\Psi(x_{n})$. From the paper [8] we have: the algorithm is converging locally with the speed $\geq 2$.

Theorem 3.1. Suppose, that $f^{(1)}(b) \geq \Psi(x) \geq f^{(1)}(a)$ with every $x_{1} \in[a, b]$, then the sequence $x_{n}$ is converging to the $y$ with a speed of 2.
The sequence $x_{n}$ is getting up with $n \geq 2$ monotonically.

Remark 3.2. If $d < a$, then the sequence $x_{n}$ is getting down with $n \geq 2$ strictly and is converging to the point $y$ with a speed of 2.

Remark 3.3. Algorithm is converging locally to $y$ without condition $f^{(1)}(b) \geq \Psi(x) \geq f^{(1)}(a)$ for all $x \in[a, b]$. This condition is equal to another one: algorithm is defined for all $x \in[a, b]$.

The proof of theorem 3.1.

Lemma 3.4. 1.Let $f^{(1)}(x)=\Psi(x)$, then $x=y$.
2. Let $\Psi^{(1)}(x)=0$, then $x=y$.

The proof of lemma 3.4. From the definition of a strict convex and a tie-line we obtain : the tie-line is unique. Let us note: $\Psi^{(1)}(x)=\{f^{(1)}(x)-\Psi(x)\}/(x-d)$. Lemma 3.4 is proved.

Lemma 3.5. Function $\Psi$ is getting up with $a \leq x \leq y$ and is getting down with $y \leq x \leq b$ strictly monotonically.

The proof of lemma 3.5. We have $\Psi^{(1)}(y)=0$,
$\Psi^{(2)}(y)=f^{(2)}(y)/(y-d)-2*\Psi^{(1)}(y)/(y-d)=f^{(2)}(y)/(y-d)$, i.g. $y$ is the strict maximum of the function $\Psi$ in Q. From proposition 2 of the lemma3.4 we get lemma 3.5. Let $x_{1}<y$, then $f^{(1)}(x_{2})=\Psi(x_{1})<\Psi(y)=f^{(1)}(y)$, i.g. $x_{2}<y$. Let $x_{1}>y$, then $f^{(1)}(x_{2})=\Psi(x_{1})<\Psi(y)=f^{(1)}(y)$, i.g. $x_{2}<y$.

Lemma 3.6. For all $a \leq x < y$ we have $f^{(1)}(x)<\Psi(x)$.
For all $y < x \leq b$ we have $f^{(1)}(x)>\Psi(x)$.

The proof of lemma 3.6.

Let $q(x)=f^{(1)}(x)-\Psi(x)$, then $q^{(1)}(y)=f^{(2)}(y)>0$.
From proposition 1 of lemma 3.4 we obtain lemma 3.6.

Let $x_{1}<y$, then $f^{(1)}(x_{2})=\Psi(x_{1})>f^{(1)}(x_{1})$ and $x_{2}>x_{1}$.
Now we have proved, that the sequence $x_{n}$ is getting up with $n \geq 2$ strict monotonically. From proposition 1 of the lemma 3.4 we conclude that $x_{n}$ is converging to the $y$. We have: $\Psi^{(2)}(y)=f^{(2)}(y)/(y-d)<0$, i.g. the algorithm is converging to the $y$ with a speed of 2.