ORIGINAL PAPER

# On the application of the Arlequin method to the coupling of particle and continuum models

Paul T. Bauman · Hachmi Ben Dhia ·
Nadia Elkhodja · J. Tinsley Oden ·
Serge Prudhomme

Received: 16 May 2007 / Accepted: 30 March 2008 / Published online: 14 May 2008
© Springer-Verlag 2008

## Abstract
In this work, we propose to extend the Arlequin framework to couple particle and continuum models. Three different coupling strategies are investigated based on the $L^{2}$ norm, $H^{1}$ seminorm, and $H^{1}$ norm. The mathematical properties of the method are studied for a one-dimensional model of harmonic springs, with varying coefficients, coupled with a linear elastic bar, whose modulus is determined by simple homogenization. It is shown that the method is well-posed for the $H^{1}$ seminorm and $H^{1}$ norm coupling terms, for both the continuous and discrete formulations. In the case of $L^{2}$ coupling, it cannot be shown that the Babuška–Brezzi condition holds for the continuous formulation. Numerical examples are presented for the model problem that illustrate the approximation properties of the different coupling terms and the effect of mesh size.

## Keywords
Multiscale modeling · Domain decomposition ·
Lagrange multipliers · Numerical methods ·
Atomistic-continuum coupling

---

P. T. Bauman (⊗) · J. T. Oden · S. Prudhomme
Institute for Computational Engineering and Sciences,
The University of Texas at Austin, Austin, TX, USA
e-mail: pbauman@ices.utexas.edu

J. T. Oden
e-mail: oden@ices.utexas.edu

S. Prudhomme
e-mail: serge@ices.utexas.edu

H. B. Dhia · N. Elkhodja
Laboratoire de Mécanique des Sols, Structures et Matériaux,
Ecole Centrale de Paris, Châtenay-Malabry, France
e-mail: hachmi.ben-dhia@ecp.fr

N. Elkhodja
e-mail: nadia.elkhodja@ecp.fr

---

## 1 Introduction

Multiscale modeling at the nanoscale has been the focus of many investigations and discussion in recent years (see, e.g., survey articles [11,13]). With the development of faster supercomputers, scientists can now contemplate simulating complex systems spanning a large range of scales that were previously considered intractable. Nevertheless, fully resolved atomistic and molecular simulations still remain out of reach with current computer resources for engineering systems of practical interest. There is obviously a need for algorithms that can couple different models, such as continuum and molecular models, for the simulation of multiscale problems.

We propose here to extend the Arlequin framework of Ben Dhia [3–7] to problems that involve both an atomistic model and a continuum model. The Arlequin framework introduces an overlapping region in which the two models are coupled using Lagrange multipliers. Several related methodologies have been previously proposed [9,14,18]. In particular, the bridging domain method of Belytschko and Xiao presents many similar features to the Arlequin method and was numerically investigated in [2,19].

In this paper, we examine in detail the mathematical properties of such a method when applied to a one-dimensional model of harmonic springs, with varying stiffness coefficients, coupled with a linear elastic bar. Our objective is to investigate three different coupling strategies based on the $L^{2}$ norm, the $H^{1}$ seminorm, and the $H^{1}$ norm. We show that the $H^{1}$ seminorm and $H^{1}$ norm coupling yield well-posed problems for the continuous and discrete formulations. However, we are not able to show that the Babuška–Brezzi condition holds in the case of the $L^{2}$ norm coupling: only simply matching the displacements is not enough for the development of a robust coupling method. We also provide a priori

![](./images/811921743445753857_1.jpg)

error estimates for the discrete problem and illustrate our theoretical results with several simple numerical examples. Reference [12], brought to the attention of the authors upon finishing the writing of the present paper, presents a similar study for the coupling of two continuum models. In that paper, several numerical examples are shown for $L^{2}$ and $H^{1}$ coupling terms as well as different weighting functions in the coupling terms. Many of the numerical results are analogous to those shown here, but no mathematical results are given. One major difference between the two papers is that we are interested here in coupling highly heterogeneous particle models with homogeneous continuum models. Our ultimate objective in the investigation of such coupling algorithms is to extend ideas of goal-oriented error estimation and adaptation [15,16] to control the size and position of the overlapping region so as to deliver highly accurate simulations.

The paper is organized as follows: following this brief introduction, we introduce the particle model, the continuum model, and briefly describe the Arlequin algorithm. In Sect. 3, we prove that the Arlequin problem is well-posed as established by Theorem 1. We show in Sect. 4 that the discrete formulation of the Arlequin method leads to a well-posed problem as well. Section 5 describes a few numerical experiments followed by conclusions in Sect. 6.

## 2 Model problems
In this section, we introduce the coupled model problem to be studied. First, the discrete model is introduced with accompanying notation, then, the continuum approximation, and finally, the coupled Arlequin model. Mathematical rigor is postponed until Sect. 3.

### 2.1 Particle model
We are interested here in a system of $n + 1$ particles that are connected by $n$ harmonic springs of various strength $k_{i}>0$ and equilibrium length $l_{i},i = 1,\ldots,n$. The initial position of the particles are denoted by $x_{i}$ and the system undergoes displacements $w_{i}$ when subjected to force $f$ applied at $x_{n}$ (Fig. 1). The potential energy of such a system is given by

$$
E_{d}(w)=\frac{1}{2}\sum_{i=1}^{n}k_{i}\left(w_{i}-w_{i-1}\right)^{2}-f w_{n}\tag{1}
$$

![](./images/811921743445753857_2.jpg)

Fig. 1 System of $n + 1$ particles connected with $n$ harmonic springs

The particles are assumed to be ordered so that $x_{i-1}<x_{i}$ and the particle on the left end of the chain to be fixed, i.e., $w_{0}=0$. We then introduce $\mathbb{R}_{0}^{n+1}=\{z\in\mathbb{R}^{n+1}:z_{0}=0\}$.

Equilibrium states of such a system, denoted $w\in\mathbb{R}_{0}^{n+1}$, can be obtained by minimizing the potential energy:

$$
E_{d}(w)=\min_{z\in\mathbb{R}_{0}^{n+1}}E_{d}(z)\tag{2}
$$

Thus, $w$ are stationary points of $E_{d}(z)$ and satisfy

$$
\lim_{\theta\rightarrow0}\frac{1}{\theta}\left(E_{d}(w+\theta z)-E_{d}(w)\right)=0\quad\forall z\in\mathbb{R}_{0}^{n+1}
$$

In other words, the displacements $w\in\mathbb{R}_{0}^{n+1}$ at equilibrium are given by

$$
\sum_{i=1}^{n}k_{i}\left(w_{i}-w_{i-1}\right)\left(z_{i}-z_{i-1}\right)=f z_{n}\quad\forall z\in\mathbb{R}_{0}^{n+1}\tag{3}
$$

Problem (3) is equivalent to:

$$
\begin{aligned}
&w_{0}=0\\
&\left(k_{1}+k_{2}\right)w_{1}-k_{2}w_{2}=0\\
&-k_{i}w_{i-1}+\left(k_{i}+k_{i+1}\right)w_{i}-k_{i+1}w_{i+1}=0\quad1 < i < n\\
&-k_{n}w_{n-1}+k_{n}w_{n}=f
\end{aligned}\tag{4}
$$

and the system of equations can be represented more compactly in matrix form as

$$
A w=f\tag{5}
$$

where $f^{T}=(0,\ldots,0,f)$ and

$$
A=\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & \ldots & 0\\
0 & k_{1}+k_{2} & -k_{2} & 0 & 0 & \ldots & 0\\
0 & -k_{2} & k_{2}+k_{3} & -k_{3} & 0 & \ldots & 0\\
& & & \ddots & & &\\
& & & & \ddots & &\\
0 & \ldots & \ldots & 0 & -k_{n-1} & k_{n-1}+k_{n} & -k_{n}\\
0 & \ldots & \ldots & 0 & 0 & -k_{n} & k_{n}
\end{bmatrix}\tag{6}
$$

The matrix $A$ is symmetric positive definite and induces the norm $\|z\|=\sqrt{z^{T}A z}$ on $\mathbb{R}^{n+1}$.

### 2.2 Continuum model
One possible approximation of the particle model is a linear elastic continuum. Here, the system of springs can be replaced by an elastic bar on domain $\Omega$, with length $L$, modulus

![](./images/811921743445753857_3.jpg)

Fig. 2 Elastic bar of length L with modulus E and loaded under traction T

![](./images/811921743445753857_4.jpg)

Fig. 3 Homogenization of spring model on a representative cell

$E$, and subjected to traction $T = f/A$, $A$ being the cross-sectional area of the bar. The displacement in the bar is denoted by $u$; see Fig. 2.

The total energy of this system is given by

$$
E_{c}=\int_{\Omega} \frac{A}{2} \sigma(x) \varepsilon(x) d x-A T(L) u(L)
\tag{7}
$$

Here the material is supposed to obey Hooke's law $\sigma=E \varepsilon$ and, using $\varepsilon=u^{\prime}$, we have

$$
E_{c}=\int_{\Omega} \frac{A E}{2}\left(u^{\prime}\right)^{2} d x-A T(L) u(L)
\tag{8}
$$

To obtain the elastic modulus, we simply consider a representative cell of springs (Fig. 3) so that, in a system consisting of a periodic array of two springs with stiffness $k_{1}, k_{2}$ and equilibrium length $l_{1}, l_{2}$, we get

$$
A E=\frac{k_{1} k_{2}}{k_{1}+k_{2}}\left(l_{1}+l_{2}\right)
\tag{9}
$$

The modulus of elasticity $E$ is derived here by equating the energy in the representative cell with the energy one would obtain if a linear elasticity model were used. For simplicity, we will implicitly take $A$ equal to unity.

As with the spring model, the equilibrium state for the continuum model is found by minimizing the energy (8).

![](./images/811921743445753857_5.jpg)

Fig. 4 Arlequin model that replaces the particle model with a combined particle and spring model

This minimization yields the following problem:

$$
\boxed{
\begin{aligned}
& \text { Find } u \in V=\left\{v \in H^{1}(\Omega): v(0)=0\right\} \text { such that: } \\
& \quad \int_{\Omega} E u^{\prime} v^{\prime} d x=T(L) v(L) \quad \forall v \in V
\end{aligned}
}
\tag{10}
$$

### 2.3 Coupling scheme

We recall that our objective is to couple the particle model with the continuum model on $\Omega$. The continuum model is selected in region $\Omega_{c}=\left(0, x_{b}\right)$ while the particle model is chosen in domain $\Omega_{d}=\left(x_{a}, L\right)$ such that $\Omega=\Omega_{c} \bigcup \Omega_{d}$ and $\Omega_{o}=\Omega_{c} \bigcap \Omega_{d}=\left(x_{a}, x_{b}\right),\left|\Omega_{o}\right| \neq 0$. We will refer to $\Omega_{o}$ as the overlap region. We denote by $\left|\Omega_{c}\right|,\left|\Omega_{d}\right|$, and $\left|\Omega_{o}\right|$, the length of domains $\Omega_{c}, \Omega_{d}$, and $\Omega_{o}$, respectively. The particle model has been reduced from $n+1$ to $m+1$ particles that are connected by $m$ harmonic springs, supposedly with $m \ll n$. See Fig. 4.

The main idea of the Arlequin method is to modify the energies as follows:

$$
\begin{aligned}
& \hat{E}_{c}=\int_{\Omega_{c}} \alpha_{c}(x) \frac{E}{2}\left(u^{\prime}\right)^{2} d x \\
& \hat{E}_{d}=\frac{1}{2} \sum_{i=1}^{m} \alpha_{i} k_{i}\left(w_{i}-w_{i-1}\right)^{2}-f w_{m}
\end{aligned}
\tag{11}
$$

where we have introduced the weighting coefficients $\alpha_{i}$ and $\alpha_{c}$, such that:

$$
\begin{aligned}
& \alpha_{c}(x)+\alpha_{d}(x)=1 \quad \forall x \in \Omega \\
& \alpha_{c}(x)= \begin{cases}1 & \forall x \in \Omega_{c} \backslash \Omega_{o} \\
0 & \forall x \in \Omega_{d} \backslash \Omega_{o}\end{cases} \\
& \alpha_{i}=\alpha_{d}\left(\frac{1}{2}\left(x_{i}+x_{i-1}\right)\right), \quad i=1, \ldots, m
\end{aligned}
\tag{12}
$$

In the overlap region $\Omega_{o}$, the coefficient $\alpha_{c}$ (and thus $\alpha_{d}$ ) can be chosen in different ways. Some intuitive and apparently

![](./images/811921743445753857_6.jpg)

![](./images/811921743445753857_7.jpg)

Fig. 5 Plot of different functions used for $\alpha_c$ and $\alpha_d$

attractive candidates are (Fig. 5):

$$
\begin{aligned}
& \alpha_{c}(x)=\frac{1}{2} \quad \forall x \in \Omega_{o} \\
& \alpha_{c}(x)=1-\frac{\left(x-x_{a}\right)}{x_{b}-x_{a}} \quad \forall x \in \Omega_{o} \\
& \alpha_{c}(x)=\frac{-\left(x-x_{b}\right)^{2}\left(2 x-3 x_{a}+x_{b}\right)}{\left(x_{a}-x_{b}\right)^{3}} \quad \forall x \in \Omega_{o}
\end{aligned}
\tag{13}
$$

where $x_a$ and $x_b$ denote the left and right end point of $\Omega_o$.

In the overlap region, the main idea is to constrain the displacements $u$ and $w$ to be "equal" in some appropriate measure. In order to do so, the first step is to convert the discrete displacements $w$ into a displacement field $\Pi w$ that can be compared to $u$ on $\Omega_o$. The natural way to do this is to take $\Pi$ as the linear interpolation operator. Other interpolation schemes are possible, but we only consider the linear interpolant in the present work.

Thus, the "energy" generated by the mismatch of $u$ and $\Pi w$ on $\Omega_o$ is

$$
\|u-\Pi w\|^{2}=\int_{\Omega_{o}} \beta_{1}(u-\Pi w)^{2}+\beta_{2}(u-\Pi w)^{\prime 2} d x \quad(14)
$$

where $(\beta_1, \beta_2)$ are non-negative weight parameters. These can also be chosen so as to scale the two terms in the integral. For example, $(\beta_1, \beta_2)=(1,0)$ refers to the $L^2$ norm, $(\beta_1, \beta_2)=(0,1)$ to the $H^1$ seminorm, and $(\beta_1, \beta_2)=(1,1)$ to the $H^1$ norm on $\Omega_o$.

The coupled problem consists of finding $u$ and $w$, in appropriate spaces $V_c$ and $V_d$, respectively (defined below), that minimizes the total energy and satisfies the constraint $\|u-\Pi w\|=0$, i.e.,

$$
\hat{E}(u, w)=\hat{E}_{d}(w)+\hat{E}_{c}(u)=\min _{\substack{v \in V_{c}, z \in V_{d} \\\|v-\Pi z\|=0}}\left(\hat{E}_{d}(z)+\hat{E}_{c}(v)\right)
\tag{15}
$$

Introducing the coupling term

$$
b(\lambda,(u, w))=\int_{\Omega_{o}} \beta_{1} \lambda(u-\Pi w)+\beta_{2} \lambda^{\prime}(u-\Pi w)^{\prime} d x
\tag{16}
$$

the minimization problem (15) can be recast into the following saddle point problem:

$$
\min _{v \in V_{c}, z \in V_{d}} \max _{\mu \in M}\left(\hat{E}_{d}(z)+\hat{E}_{c}(v)+b(\mu,(v, z))\right)
\tag{17}
$$

where $M$ is an appropriate space for the Lagrange multipliers. We now pose this problem precisely and analyze the details of its mathematical properties.

## 3 Mathematical analysis of the coupled formulation

Let $V_c=\{v \in H^1(\Omega_c): v(0)=0\}$ and $V_d=\{z \in \mathbb{R}^{m+1}\}$ be the vector spaces of test functions for the continuum and discrete models, respectively, and let $\Pi$ be the linear interpolant $\Pi: V_d \to H^1(\Omega_o)$. In what follows, we will not distinguish a function $v \in V_c$ from its restriction to the space $H^1(\Omega_o)$. We also define the vector space for the Lagrange multipliers as:

$$
M=
\begin{cases}
L^{2}\left(\Omega_{o}\right), & \text { if } \beta_{2}=0 \\
H^{1}\left(\Omega_{o}\right) / \mathbb{R}, & \text { if } \beta_{1}=0 \\
H^{1}\left(\Omega_{o}\right), & \text { otherwise }
\end{cases}
\tag{18}
$$

with associated norm:

$$
\|\mu\|_{M}=\sqrt{\int_{\Omega_{o}} \beta_{1} \mu^{2}+\beta_{2} \mu^{\prime 2} d x}
$$

Let the average of $z$ on $\Omega_o$ be denoted as:

$$
\bar{z}=\sum_{i=1}^{n_{o}} \frac{l_{i}}{\left|\Omega_{o}\right|} \frac{z_{i}+z_{i-1}}{2}
$$

where $n_o$ is the number of springs on $\Omega_o$. *The restrictive assumption that is made here is that the overlap region exactly coincides with a given set of complete springs. In other words, the domain $\Omega_o$ is not allowed to only cover part of a spring.*

We also introduce the seminorm $|\cdot|_{V_d}$ on $V_d$ as:

$$
|z|_{V_{d}}=\sqrt{\sum_{i=1}^{m} k_{i}\left(z_{i}-z_{i-1}\right)^{2}}
$$

The norms on $V_c$ and $V_d$ are then chosen as:

$$
\begin{aligned}
& \|v\|_{V_{c}}=\sqrt{\int_{\Omega_{c}} E\left|v^{\prime}\right|^{2} d x} \\
& \|z\|_{V_{d}}=\sqrt{|z|_{V_{d}}^{2}+\delta \bar{z}^{2}}
\end{aligned}
\tag{19}
$$

where $\delta$ is a dimensionally consistent weighting constant that we define below.

![](./images/811921743445753857_8.jpg)

We now introduce the product space $X = V_c \times V_d$ with pairs of $X$ denoted for example as $U = (u, w)$, $V = (v, z)$, and with norm:

$$
\|V\|_X = \sqrt{\|v\|_{V_c}^2 + \|z\|_{V_d}^2} \tag{20}
$$

and define the kernel space of $b(\cdot, \cdot)$ as the subspace of $X$ such that:

$$
X_0 = \{ V \in X : b(\mu, V) = 0 \quad orall \mu \in M \} \tag{21}
$$

We wish to solve the following saddle point problem:

Find $U \in X$, $\lambda \in M$ such that:
$$
L(U, \lambda) = \inf_{V \in X} \sup_{\mu \in M} L(V, \mu) \tag{22}
$$

where the Lagrangian reads:

$$
L(V, \mu) = \frac{1}{2}a(V, V) + b(\mu, V) - l(V)
$$

$$
\begin{aligned}
a(U, V) =& \int_{\Omega_c} \alpha_c E u' v' dx \\
&+ \sum_{i=1}^m \alpha_i k_i (w_i - w_{i-1}) (z_i - z_{i-1}) \tag{23}
\end{aligned}
$$

$$
b(\mu, V) = \int_{\Omega_o} \beta_1 \mu(v - \Pi z) + \beta_2 \mu'(v - \Pi z)' dx
$$

$$
l(V) = f z_m
$$

The saddle point problem (22) can be recast as:

$$
\boxed{
\begin{aligned}
\text{Find } U \in X,\ \lambda \in M \text{ such that:} \\
a(U, V) + b(\lambda, V) = l(V)\ \ \forall V \in X \\
b(\mu, U) = 0\ \ \ \ \ \forall \mu \in M
\end{aligned}
} \tag{24}
$$

Problem (24) is well posed for $\beta_1 \geq 0$ and $\beta_2 > 0$. This result immediately follows from results in Ben Dhia and Rateau [4,5]. Nevertheless, we choose to present here a detailed proof with the main objective of explicitly deriving the constants associated with the problem in order to study the influence of parameters such as the geometrical and material properties, the coupling parameters $\beta_1$ and $\beta_2$, or length of the overlap domain on the coupled solutions. Proofs of continuity of the forms $a(\cdot, \cdot)$, $b(\cdot, \cdot)$, and $l(\cdot)$ are relatively straightforward and provided for completeness in Appendix B. We show below that $a(\cdot, \cdot)$ is coercive and that the coupling term $b(\cdot, \cdot)$ satisfies the Babuška–Brezzi condition [1,8]. Technical lemmas are presented in Appendix A. We conclude the section by a theorem for the well-posedness of Problem (24), summarize the continuity and inf-sup constants, and identify from this analysis "optimal" constants $\beta_1$, $\beta_2$, and $\delta$.

Lemma 1 (Coercivity of a) Let $\alpha_c$ and $\alpha_d$ be constant or linear functions defined by $(13)_1$ and $(13)_2$. Then, with above notation and definitions, there exists a constant $\gamma_a > 0$ such that:

$$
\inf_{U \in X_0} \sup_{V \in X_0} \frac{|a(U, V))|}{\|U\|_X \|V\|_X} > \gamma_a
$$

$$
\sup_{U \in X_0} a(U, V) > 0 \quad orall V \in X_0, V 
eq 0
$$

with
$$
\gamma_a = 
\begin{cases}
\gamma_1 & \text{if } \beta_1 = 0 \\
\gamma_1 \min\left( \frac{1}{2}, \frac{E|\Omega_o|}{\delta|\Omega_c|^2} \right) & \text{if } \beta_1 > 0
\end{cases}
$$

and
$$
\gamma_1 = \frac{1}{2} \min_i \left( \frac{E}{k_i l_i}, \frac{k_i l_i}{E} \right)
$$

Proof It suffices to show that $a(\cdot, \cdot)$ is coercive on $X_0$. Let $V = (v, z) \in X_0$. We first show that

$$
a(V, V) \geq \gamma_1 \left( \|v\|_{V_c}^2 + |z|_{V_d}^2 \right)
$$

where $\gamma_1$ is a constant that depends on $\alpha_c$ and $\alpha_d$ being constant or linear.

By definition of the bilinear form, and the fact that $\alpha_c = 1$ on $\Omega_c \setminus \Omega_o$ and $\alpha_d = 1$ on $\Omega_d \setminus \Omega_o$, we have

$$
\begin{aligned}
a(V, V) =& \int_{\Omega_c} \alpha_c E(v')^2 dx + \sum_{i=1}^m \alpha_i k_i (z_i - z_{i-1})^2 \\
=& \int_{\Omega_c \setminus \Omega_o} E(v')^2 dx + \sum_{i=n_o+1}^m k_i (z_i - z_{i-1})^2 \\
&+ \int_{\Omega_o} \alpha_c E(v')^2 dx + \sum_{i=1}^{n_o} \alpha_i k_i (z_i - z_{i-1})^2
\end{aligned}
$$

We then divide the overlap terms in half:

$$
\begin{aligned}
&\int_{\Omega_o} \alpha_c E(v')^2 dx + \sum_{i=1}^{n_o} \alpha_i k_i (z_i - z_{i-1})^2 \\
&= \frac{1}{2} \left( \int_{\Omega_o} \alpha_c E(v')^2 dx + \sum_{i=1}^{n_o} \alpha_i k_i (z_i - z_{i-1})^2 \right) \\
&+ \frac{1}{2} \left( \int_{\Omega_o} \alpha_c E(v')^2 dx + \sum_{i=1}^{n_o} \alpha_i k_i (z_i - z_{i-1})^2 \right)
\end{aligned}
$$

Next, we examine the continuum term and the discrete term and show how they should be recombined. We use the fact

![](./images/811921743445753857_9.jpg)

that $X_0$ consists of functions $v$ and vectors $z$ such that $v=\Pi z$ on $\Omega_o$ (and therefore $v'=(\Pi z)'$), and
$$
(\Pi z)'=\frac{z_i-z_{i-1}}{l_i}, \quad \forall x \in\left(x_{i-1}, x_i\right)
$$

Then,
$$
\begin{aligned}
\frac{1}{2} \int_{\Omega_{o}} \alpha_{c} E\left(v^{\prime}\right)^{2} d x &=\frac{1}{2} \sum_{i=1}^{n_{o}} \int_{x_{i-1}}^{x_{i}} \alpha_{c} E\left(\frac{z_{i}-z_{i-1}}{l_{i}}\right)^{2} d x \\
&=\frac{1}{2} \sum_{i=1}^{n_{o}} E\left(\frac{z_{i}-z_{i-1}}{l_{i}}\right)^{2} \int_{x_{i-1}}^{x_{i}} \alpha_{c} d x \\
& \geq \frac{1}{2} \min _{i}\left(\frac{E}{k_{i} l_{i}}\right) \sum_{i=1}^{n_{o}}\left(1-\alpha_{i}\right) k_{i}\left(z_{i}-z_{i-1}\right)^{2}
\end{aligned}
$$

Repeating the same procedure in opposite order on the discrete term, we have
$$
\frac{1}{2} \sum_{i=1}^{n_{o}} \alpha_{i} k_{i}\left(z_{i}-z_{i-1}\right)^{2} \geq \frac{1}{2} \min _{i}\left(\frac{k_{i} l_{i}}{E}\right) \int_{\Omega_{o}}\left(1-\alpha_{c}\right) E\left(v^{\prime}\right)^{2} d x
$$

Substituting the previous two expressions into the original expression and using the fact that $\alpha_c+\alpha_d=1$ gives
$$
\begin{aligned}
a(V, V) \geq & \int_{\Omega_{c} \setminus \Omega_{o}} E\left(v^{\prime}\right)^{2} d x+\sum_{i=n_{o}+1}^{m} k_{i}\left(z_{i}-z_{i-1}\right)^{2} \\
& +\frac{1}{2} \min \left(1, \min _{i}\left(\frac{E}{k_{i} l_{i}}\right)\right) \sum_{i=1}^{n_{o}} k_{i}\left(z_{i}-z_{i-1}\right)^{2} \\
& +\frac{1}{2} \min \left(1, \min _{i}\left(\frac{k_{i} l_{i}}{E}\right)\right) \int_{\Omega_{o}} E\left(v^{\prime}\right)^{2} d x \\
\geq & \gamma_{1}\left(\|v\|_{V_{c}}^{2}+|z|_{V_{d}}^{2}\right)
\end{aligned}
$$
and
$$
\gamma_{1}=\frac{1}{2} \min _{i}\left(\frac{E}{k_{i} l_{i}}, \frac{k_{i} l_{i}}{E}\right)
$$

Now, if $\beta_1=0$, the result is immediate with $\gamma_a=\gamma_1$. If $\beta_1$ is nonzero, we observe that the term $|z|_{V_d}$ vanishes for all constant vectors $z$ in $V_d$. Applying Poincaré inequality (cf. Lemma A-1), we get
$$
\begin{aligned}
a(V, V) & \geq \gamma_{1}\left(\frac{1}{2}\|v\|_{V_{c}}^{2}+\frac{1}{2}\|v\|_{V_{c}}^{2}+|z|_{V_{d}}^{2}\right) \\
& \geq \gamma_{1}\left(\frac{1}{2}\|v\|_{V_{c}}^{2}+\frac{E}{\left|\Omega_{c}\right|^{2}}\|v\|_{L^{2}\left(\Omega_{c}\right)}^{2}+|z|_{V_{d}}^{2}\right)
\end{aligned}
$$

Then using Lemma A-2, the fact that $X_0$ consists of those functions $v$ and vectors $z$ such that $v=\Pi z$, which implies $\overline{\Pi z}=\bar{z}$, we observe that
$$
\|v\|_{L^{2}\left(\Omega_{c}\right)}^{2} \geq\|v\|_{L^{2}\left(\Omega_{o}\right)}^{2} \geq \bar{v}^{2}\left|\Omega_{o}\right|=\bar{z}^{2}\left|\Omega_{o}\right|
$$

Thus, it follows that:
$$
\begin{aligned}
a(V, V) & \geq \gamma_{1}\left(\frac{1}{2}\|v\|_{V_{c}}^{2}+|z|_{V_{d}}^{2}+\frac{E\left|\Omega_{o}\right|}{\delta\left|\Omega_{c}\right|^{2}} \delta \bar{z}^{2}\right) \\
& \geq \gamma_{a}\|V\|_{X}^{2}
\end{aligned}
$$
where
$$
\gamma_{a}=\gamma_{1} \min \left(\frac{1}{2}, \frac{E\left|\Omega_{o}\right|}{\delta\left|\Omega_{c}\right|^{2}}\right)
$$
which completes the proof.
口

Remark 1 Above proof also holds for the case $\alpha_c=\alpha_d=$ $1 / 2$, however it can be shown that the constant $\gamma_1$ simply reduces in that case to $\gamma_1=1 / 2$.

Remark 2 Although we used the strong condition $v=\Pi z$ in second part of the proof, the weaker condition $\bar{v}=\overline{\Pi z}$ could have been used. This becomes important in the proof of discrete coercivity, which is addressed later in the paper.

Remark 3 We have not proven the case where $\alpha_c, \alpha_d$ are cubic functions $(13)_3$. We believe that this case yields coercivity and could be proven with more sophisticated techniques.

Lemma 2 (Inf-sup condition for $b$) Let $\beta_2>0$. Then, with the above notation and definitions, there exists a constant $\gamma_b>0$ such that:
$$
\inf _{\mu \in M} \sup _{V \in X} \frac{|b(\mu, V)|}{\|\mu\|_{M_{1}}\|V\|_{X}}>\gamma_{b}
$$
with
$$
\gamma_{b}= \begin{cases}\sqrt{\frac{\beta_{2}}{E}} & \beta_{1}=0 \\ \sqrt{\frac{\beta_{2}}{E}} \min \left(\sqrt{\frac{\beta_{1}\left|\Omega_{o}\right| E}{2 \delta \beta_{2}}}, \sqrt{\frac{E}{E+\delta\left|\Omega_{o}\right|}}\right) & \beta_{1}>0\end{cases}
$$

Proof This proof follows the proof given in [4,5]. It is sufficient to show that
$$
\sup _{V \in X} \frac{|b(\mu, V)|}{\|V\|_{X}}>\gamma_{b}\|\mu\|_{M} \quad \forall \mu \in M
$$

Since $\mu \in M, \mu(x_a)$ is well defined and denoted by $\mu_a$. Let $\hat{\mu}=\mu-\mu_a$. We introduce the extension operator $S(\mu)$ : $\mu \in M \rightarrow \hat{v} \in V_c$ such that $\hat{v}=\hat{\mu}$ on $\Omega_o$, and $\hat{v}=0$ on $\Omega_c \setminus \Omega_o$. Furthermore, let $\hat{z}$ be the constant vector $\hat{z}=\mu_a$. Thus, taking $\hat{V}=(\hat{v}, \hat{z})$ we get
$$
\sup _{V \in X} \frac{|b(\mu, V)|}{\|V\|_{X}} \geq \frac{|b(\mu, \hat{V})|}{\|\hat{V}\|_{X}}=\frac{\|\mu\|_{M}^{2}}{\|\hat{V}\|_{X}}
$$

It suffices to show that $\|\mu\|_{M} /\|\hat{V}\|_{X}$ is greater than a positive constant independent of $\mu$. Using the definition of $\|\cdot\|_{X}$, we have
$$
\|\hat{V}\|_{X}^{2}=\int_{\Omega_{o}} E\left(\mu^{\prime}\right)^{2} d x+\delta \mu_{a}^{2}=E|\mu|_{H^{1}\left(\Omega_{o}\right)}^{2}+\delta \mu_{a}^{2}
$$

![](./images/811921743445753857_10.jpg)

Thus, if $\beta_1 = 0$, we can fix $\mu_a = 0$, and

$$\|\hat{V}\|_{X}^{2}=E \int_{\Omega_{o}} \mu^{\prime 2} d x=\frac{E}{\beta_{2}}\|\mu\|_{M}^{2}$$

The inf-sup constant is then equal to $\gamma_{b}=\sqrt{\beta_{2} / E}$.

If $\beta_1 > 0$, we can bound $\mu_a$ in terms of $\|\mu\|_{L^{2}(\Omega_{o})}$ and $|\mu|_{H^{1}(\Omega_{o})}^{2}$. Using the Poincaré inequality (since $\hat{\mu}=0$ at $x=x_a$), we get

$$
\begin{aligned}
\int_{\Omega_{o}} \mu_{a}^{2} d x &=\int_{\Omega_{o}}(\mu-\hat{\mu})^{2} d x \leq 2 \int_{\Omega_{o}} \mu^{2}+\hat{\mu}^{2} d x \\
& \leq 2\|\mu\|_{L^{2}\left(\Omega_{o}\right)}^{2}+\left|\Omega_{o}\right|^{2}|\hat{\mu}|_{H^{1}\left(\Omega_{o}\right)}^{2} \\
&=2\|\mu\|_{L^{2}\left(\Omega_{o}\right)}^{2}+\left|\Omega_{o}\right|^{2}|\mu|_{H^{1}\left(\Omega_{o}\right)}^{2}
\end{aligned}
$$

Since
$$\int_{\Omega_{o}} \mu_{a}^{2} d x=\left|\Omega_{o}\right| \mu_{a}^{2}$$
we arrive at the inequality:
$$\mu_{a}^{2} \leq \frac{2}{\left|\Omega_{o}\right|}\|\mu\|_{L^{2}\left(\Omega_{o}\right)}^{2}+\left|\Omega_{o}\right||\mu|_{H^{1}\left(\Omega_{o}\right)}^{2}$$

Thus, substituting the bound for $\mu_a$, we conclude that

$$
\begin{aligned}
\|\hat{V}\|_{X}^{2} & \leq \frac{2 \delta}{\left|\Omega_{o}\right|}\|\mu\|_{L^{2}\left(\Omega_{o}\right)}^{2}+\left(E+\delta\left|\Omega_{o}\right|\right)|\mu|_{H^{1}\left(\Omega_{o}\right)}^{2} \\
& \leq \max \left(\frac{2 \delta}{\beta_{1}\left|\Omega_{o}\right|}, \frac{E+\delta\left|\Omega_{o}\right|}{\beta_{2}}\right)\|\mu\|_{M}^{2}
\end{aligned}
$$

and, therefore,

$$
\gamma_{b}=
\begin{cases}
\sqrt{\frac{\beta_{2}}{E}} & \beta_{1}=0 \\
\sqrt{\frac{\beta_{2}}{E}} \min \left(\sqrt{\frac{\beta_{1}\left|\Omega_{o}\right| E}{2 \delta \beta_{2}}}, \sqrt{\frac{E}{E+\delta\left|\Omega_{o}\right|}}\right) & \beta_{1}>0
\end{cases}
$$

and the proof is complete.
$\square$

Remark 4 We are not able to show the case for which $\beta_2 = 0$. Indeed, $M$ would be the space $L^{2}(\Omega_{o})$ and the extension operator $S(\lambda)$ is not defined in this case. This stems from the fact that the space $L^{2}(\Omega_{o})$ is not contained in $H^{1}(\Omega_{o})$.

From the continuity and coercivity of $a(\cdot, \cdot)$, from the continuity of $l(\cdot)$, and from the continuity and inf-sup condition of $b(\cdot, \cdot)$ (see Lemmas B-1, B-2, B-3, and Lemmas 1 and 2), we have the following theorem.

Theorem 1 Let $\beta_1 \geq 0$ and $\beta_2 > 0$ and let $\alpha_c$ and $\alpha_d$ be constant or linear. Then, problem (24) is well-posed, in the sense that it admits a unique solution and that the solution depends continuously on the data.

Finally, we summarize the constants obtained from conti- nuity, coercivity, and B–B condition in Tables 1, 2 and 3. In an effort to obtain optimality with respect to the constants, we

<table>
<caption>Table 1 Constants from continuity conditions</caption>
<tbody>
<tr class="odd">
<td>$M_a$</td>
<td>$1$</td>
</tr>
<tr class="even">
<td>$M_b$</td>
<td>$\sqrt{2} \max \left( \sqrt{\frac{\beta_1 |\Omega_c|^2 + 2\beta_2}{2E}}, \sqrt{\frac{\beta_1 |\Omega_o|}{\delta}}, \sqrt{\frac{\beta_1 |\Omega_o|^2 + 2\beta_2}{2 \min_i k_i l_i}} \right)$</td>
</tr>
<tr class="odd">
<td>$M_l$</td>
<td>$2|f| \max \left( \frac{1}{\sqrt{\delta}}, \frac{1}{\sqrt{\min_i k_i}} \right)$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Constants from coercivity and B–B conditions for the case $\beta_1 = 0$</caption>
<tbody>
<tr class="odd">
<td>$\gamma_a$</td>
<td>$\frac{1}{2} \min_i \left( \frac{E}{k_i l_i}, \frac{k_i l_i}{E} \right)$</td>
</tr>
<tr class="even">
<td>$\gamma_b$</td>
<td>$\sqrt{\frac{\beta_2}{E}}$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3 Constants from coercivity and B–B conditions for the case $\beta_1 > 0$</caption>
<tbody>
<tr class="odd">
<td>$\gamma_a$</td>
<td>$\frac{1}{2} \min_i \left( \frac{E}{k_i l_i}, \frac{k_i l_i}{E} \right) \min \left( \frac{1}{2}, \frac{E |\Omega_o|}{\delta |\Omega_c|^2} \right)$</td>
</tr>
<tr class="even">
<td>$\gamma_b$</td>
<td>$\sqrt{\frac{\beta_2}{E}} \min \left( \sqrt{\frac{\beta_1 |\Omega_o| E}{2 \delta \beta_2}}, \sqrt{\frac{E}{E + \delta |\Omega_o|}} \right)$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4 Choice for the parameters $\beta_1, \beta_2$, and $\delta$</caption>
<tbody>
<tr class="odd">
<td>$\beta_1$</td>
<td>$\frac{2E}{|\Omega_c|^2}$</td>
</tr>
<tr class="even">
<td>$\beta_2$</td>
<td>$E$</td>
</tr>
<tr class="odd">
<td>$\delta$</td>
<td>$\frac{E |\Omega_o|}{|\Omega_c|^2}$</td>
</tr>
</tbody>
</table>

choose specific values for $\beta_1, \beta_2$, and $\delta$. In particular, we want $\beta_1, \beta_2$, and $\delta$ to be dimensionally consistent in their respective terms while also optimizing the continuity constants (i.e., not depending on the size of the domains). Table 4 summarizes the choice for the parameters $\beta_1, \beta_2$, and $\delta$ and Table 5 shows the resulting constants.

Remark 5 Note that the constants $M_b$ and $\gamma_d$ in Table 5 are bounded above and below, respectively, by observing that $|\Omega_o| \leq |\Omega_c|$. Then:

$$M_{b} \leq \sqrt{2} \max \left(1, \sqrt{\frac{E}{\min _{i} k_{i} l_{i}}}\right) \tag{26}$$

$$\gamma_{b} \geq \frac{1}{2}$$

Since $M_a$ and $\gamma_a$ are independent of $|\Omega_o|$ we can conclude that the size of the overlap region will have only mild effects on the accuracy and stability of the problem. However, from this analysis, we see that the major influence of the size will be in the constant $M_l$ which increases as $|\Omega_o|$ decrases.

![](./images/811921743445753857_11.jpg)

<table><caption>Table 5 Rescaled constants for continuity, coercivity, and B–B stability for the case $\beta_1 > 0$</caption>
| $M_a$ | $1$ |
| --- | --- |
| $M_b$ | $\sqrt{2} \max \left(1, \sqrt{\frac{E}{2 \min_i k_i l_i} \left(1 + \frac{|\Omega_o|^2}{|\Omega_c|^2}\right)}\right)$ |
| $M_l$ | $2 | f | \max \left(\frac{|\Omega_c|}{\sqrt{E |\Omega_o|}}, \frac{1}{\sqrt{\min_i k_i}}\right)$ |
| $\gamma_a$ | $\frac{1}{4} \min_i \left(\frac{E}{k_i l_i}, \frac{k_i l_i}{E}\right)$ |
| $\gamma_b$ | $\sqrt{\frac{|\Omega_c|^2}{|\Omega_c|^2 + |\Omega_o|^2}}$ |
</table>

Problem may arise if the spring stiffness varies rapidly from one spring to the other and that the size of $|\Omega_o|$ is taken too small, say much smaller than the representative cell; a situation which in general is avoided from common sense. Recent numerical experiments, presented for example in [17], have indeed confirmed that the influence of $|\Omega_o|$ on the error in the approximation remains in general small.

## 4 Discrete formulation of the coupled model

Let $V_c^h$ and $M^h$ be finite element subspaces of the vector spaces $V_c$ and $M$, respectively, and let $X^h$ be the product space $X^h = V_c^h \times V_d$. More precisely, the subspace $V_c^h$ consists of piecewise linear continuous functions defined by the set of nodes $x_i = i h$, $i = 0, \dots, N^e$, where $N^e$ denotes the number of elements in the mesh. For the subspace $M^h$, we are faced with several choices since the elements associated with $V_c^h$ and $M^h$ do not have to match (case (a) in Fig. 6). However, for the sake of simplicity here, we will only consider three special cases for $M^h$ (see Fig. 6, cases (b), (c), and (d)):

1.  **"Particle coupling"**: Each node of the mesh associated with $M^h$ coincides with the position of one particle on $\Omega_o$ and vice-versa (case (b) in Fig. 6).
2.  **"Continuum coupling"**: The elements of the mesh associated with $M^h$ are exactly identical with those of $V_c^h$ on $\Omega_o$ (case (c) in Fig. 6).
3.  **"RVE coupling"**: The element size $h$ for the continuum solution are chosen arbitrarily from the equilibrium length $l$ of the particles, but the elements for $M^h$ are equal to the size, denoted $\varepsilon$, of the representative volume element (RVE) (case (d) in Fig. 6). The continuum coupling can then be viewed as a subcase of this case.

Finally, we write $U_h = (u_h, w_h)$ and $V_h = (v_h, z)$ and introduce the space $X_0^h$ as:

![](./images/811921743445753857_12.jpg)

Fig. 6 Finite element discretization of $\Omega_c$ and $\Omega_o$ ($\boldsymbol{l}$ = nodes on $\Omega_c$, $\boldsymbol{\times}$ = nodes on $\Omega_d$, $\boldsymbol{\bullet}$ = particles on $\Omega_d$)

$$
X_0^h = \left\{ V_h \in X^h : b \left( \mu_h, V_h \right) = 0 \quad \forall \mu_h \in M^h \right\} \tag{27}
$$

Then, problem (24) is approximated as follows:

> Find $U_h \in X^h$, $\lambda_h \in M^h$ such that:
> $$
> \begin{aligned}
> a \left( U_h, V_h \right) + b \left( \lambda_h, V_h \right) & = l \left( V_h \right) \quad \forall V_h \in X^h \tag{28} \\
> b \left( \mu_h, U_h \right) & = 0 \quad \forall \mu_h \in M^h
> \end{aligned}
> $$

Remark 6 Although $V_d$ is a finite-dimensional space and, consequently does not need to be discretized using finite elements, we will use the notation $w_h$ to denote the solution of the particle model in (28) to emphasize that $w_h$ indirectly depends on the choice of $V_c^h$ and $M^h$.

### 4.1 Existence and uniqueness of solutions

In this section, we prove that the discretized Problem (28) is well-posed. We shall review the lemmas of the previous section in order to highlight the differences between the "continuous" and "discrete" problems. We omit consideration of continuity of $a(\cdot, \cdot)$, $b(\cdot, \cdot)$, and $l(\cdot)$ as they follow trivially (since $X^h \subset X$ and $M^h \subset M$).

One difficulty in analyzing the discretized saddle point problems is due to the fact that the kernel space $X_0^h$ is not a subset of $X_0$.

Lemma 3 (Coercivity of a) Let $\alpha_c = \alpha_d = 1/2$. Then, with the above notation and definition, there exists a constant $\gamma_a^h > 0$ such that:

$$
\inf_{U_h \in X_0^h} \sup_{V_h \in X_0^h} \frac{a\left(U_h, V_h\right)}{\left\|U_h\right\|_X\left\|V_h\right\|_X} \geq \gamma_a^h
$$

with $\gamma_a^h = \gamma_a$.

Proof The proof is actually similar to the one shown in Lemma 1. We just provide here a sketch of it.

We observe that functions $V_h = (v_h, z)$ in $X_0^h$ satisfy

$$
b(\mu_h, V_h) = 0, \quad \forall \mu_h \in M^h
$$

i.e.,

$$
\begin{aligned}
& \int_{\Omega_o} \beta_1 v_h \mu_h + \beta_2 v_h' \mu_h' dx \\
& \quad = \int_{\Omega_o} \beta_1(\Pi z) \mu_h + \beta_2(\Pi z)' \mu_h' dx, \quad \forall \mu_h \in M^h
\end{aligned}
$$

In other words, given a function $z \in V_d$, $v_h$ is simply viewed as the projection of $\Pi z$ on $V_c^h$ if $M^h = V_c^h$. Take $\mu_h = 1$ on $\Omega_o$; then, if $\beta_1 \neq 0$,

$$
\int_{\Omega_o} v_h dx = \int_{\Omega_o} (\Pi z) dx, \quad \forall \mu_h \in M^h
$$

The averages of $v_h$ and $\Pi z$ on $\Omega_o$ are equal but the functions are not necessarily identical unlike the continuous case. However, if every particle on $\Omega_o$ coincides with a node of $M^h$ (case (b) in Fig. 6), then $v_h = \Pi z$. If not, only the equality of averages, as above, is necessary to show coercivity if $\beta_1 \neq 0$ (see Remark 2). In the case where $\beta_1 = 0$, coercivity of the bilinear form is immediate.
□

Remark 7 We do not show here coercivity of $a(\cdot, \cdot)$ in the case where $\alpha_c$ and $\alpha_d$ are linear. The proof is of course straightforward when using the particle coupling and essentially follows the proof of Lemma 1 since $v_h = \Pi z$. However, in the general case, the proof becomes very technical as the elements of the space $X_0^h$ are not simple.

Lemma 4 (Inf-Sup condition for b) With above notation and definitions, there exists a constant $\gamma_b^h > 0$:

$$
\inf_{\mu_h \in M^h} \sup_{V_h \in X^h} \frac{b\left(\mu_h, V_h\right)}{\left\|\mu_h\right\|_M\left\|V_h\right\|_X} \geq \gamma_b^h
$$

Proof Let $\mu_h \in M^h$. Similarly to the continuous case, we need to show that

$$
\sup_{V_h \in X^h} \frac{\left|b\left(\mu_h, V_h\right)\right|}{\left\|V_h\right\|_X} \geq \gamma_b^h\left\|\mu_h\right\|_M
$$

with $\gamma_b^h > 0$ independent of $\mu_h$. We consider the two cases:

1.  **Continuum/RVE coupling:** In this case, given $\mu_h \in M^h$, we can always find a function $\hat{v}_h \in V_c^h$ such that $\hat{v}_h = \mu_h - \mu_a$ on $\Omega_o$ and $\hat{v}_h = 0$ on $\Omega_c \setminus \Omega_o$, where $\mu_a = \mu_h(x_a)$. Furthermore, we can select $\hat{z} = \mu_a$ so that $\hat{V}_h = (\hat{v}_h, \hat{z})$. Thus,

$$
\sup_{V_h \in X^h} \frac{\left|b\left(\mu_h, V_h\right)\right|}{\left\|V_h\right\|_X} \geq \frac{\left|b\left(\mu_h, \hat{V}_h\right)\right|}{\left\|\hat{V}_h\right\|_X}
$$

The proof then follows the one in Lemma 2 and we conclude here that $\gamma_b^h = \gamma_b$.

2.  **Particle coupling:** In this case, we can always find a vector $\hat{z} \in V_d$ such that $\Pi \hat{z} = \mu_h$ on $\Omega_o$. On $\Omega_d \setminus \Omega_o$, $\hat{z}$ is chosen as a constant vector so that $\hat{V}_h = (0, \Pi \hat{z})$.
Then:

$$
\sup_{V_h \in X^h} \frac{\left|b\left(\mu_h, V_h\right)\right|}{\left\|V_h\right\|_X} \geq \frac{\left|b\left(\mu_h, \hat{V}_h\right)\right|}{\left\|\hat{V}_h\right\|_X} = \frac{\left\|\mu_h\right\|_M^2}{\|\hat{z}\|_{V_d}}
$$

We just need to show that $\|\mu_h\|_M / \|\hat{z}\|_{V_d}$ is greater than a positive constant. Since $\hat{z}$ is constant on $\Omega_d \setminus \Omega_o$, we have (using Lemma A-2):

$$
\begin{aligned}
\|\hat{z}\|_{V_d}^2 & = \sum_{i=1}^{n_o} k_i\left(\hat{z}_i - \hat{z}_{i-1}\right)^2 + \delta\left(\sum_{i=1}^{n_o} \frac{l_i}{\left|\Omega_o\right|}\left(\frac{\hat{z}_i + \hat{z}_{i-1}}{2}\right)\right)^2 \\
& \leq \max_i k_i l_i\left|\mu_h\right|_{H^1(\Omega_o)}^2 + \delta \bar{\mu}_h^2
\end{aligned}
$$

If $\beta_1 = 0$, we can fix $\bar{\mu}_h = 0$ so that:

$$
\|\hat{z}\|_{V_d}^2 \leq \max_i k_i l_i\left|\mu_h\right|_{H^1(\Omega_o)}^2 = \frac{\max_i k_i l_i}{\beta_2}\left\|\mu_h\right\|_M^2
$$

and $\gamma_b^h = \sqrt{\beta_2 / \max_i k_i l_i}$.
If $\beta_1$ is non-zero, then using Lemma A-2, we get

$$
\begin{aligned}
\|\hat{z}\|_{V_d}^2 \leq & \max_i k_i l_i\left|\mu_h\right|_{H^1(\Omega_o)}^2 + \frac{\delta}{\left|\Omega_o\right|}\left\|\mu_h\right\|_{L^2(\Omega_o)}^2 \\
\leq & \max \left(\frac{\delta}{\beta_1\left|\Omega_o\right|}, \frac{\max_i k_i l_i}{\beta_2}\right) \\
& \quad \times\left(\beta_1\left\|\mu_h\right\|_{L^2(\Omega_o)}^2 + \beta_2\left|\mu_h\right|_{H^1(\Omega_o)}^2\right) \\
= & \max \left(\frac{\delta}{\beta_1\left|\Omega_o\right|}, \frac{\max_i k_i l_i}{\beta_2}\right)\left\|\mu_h\right\|_M^2
\end{aligned}
$$

which completes the proof with:

$$
\gamma_b^h = \min\left(\sqrt{\frac{\beta_1\left|\Omega_o\right|}{\delta}}, \sqrt{\frac{\beta_2}{\max_i k_i l_i}}\right)
$$

□

![](./images/811921743445753857_13.jpg)

Remark 8 We note that in the discrete case, the bilinear form $b(\cdot, \cdot)$ does satisfy the inf-sup condition if $\beta_2 = 0$. Indeed, we can in this case bound the term $|\mu_h|_{H^1(\Omega_o)}$ by $\|\mu_h\|_{L^2(\Omega_o)}$ using an inverse inequality. However, the inf-sup constant would be dependent on the mesh size $h$, and would go to zero as $h$ tends to zero.

Remark 9 We also note here that, as pointed out by Ben Dhia and Rateau [7], the discretization of the Lagrange multiplier space cannot be finer than the discretization of the continuum model and the particle spacing. This can be seen from the proof since we would not be able to find a $v_h$ or $\Pi z$ that is an extension of $\mu_h$ since it is possible $v_h \neq \mu_h$ in $\Omega_o$.

Finally, the following theorem follows from the continuity on $X^h$ and coercivity on $X_0^h$ of $a(\cdot, \cdot)$, from the continuity of $l(\cdot)$ on $X^h$, and from the continuity and inf-sup condition of $b(\cdot, \cdot)$ on $M^h \times X^h$ (see Lemmas B-1, B-2, B-3, and Lemmas 3 and 4):

Theorem 2 Problem (28) with $\beta_1 \geq 0$ and $\beta_2 > 0$ and with $\alpha_c, \alpha_d$ constant or linear is well-posed, in the sense that the solution to (28) exists, is unique, and depends continuously on the data. Moreover, all constants are independent of $h$.

### 4.2 A priori error estimates

For completeness, we state the following a priori error estimate. The proof follows exactly that of the traditional mixed finite element error estimate [10].

Theorem 3 Let $(u, w, \lambda) \in V_c \times V_d \times M$ be the solutions to (24) and let $(u_h, w_h, \lambda_h) \in V_c^h \times V_d \times M^h$ be the solutions to (28). Then,
$$
\begin{aligned}
\left\|(u-u_h, w-w_h)\right\|_X & \leq C_1 \inf _{v_h \in V_c^h}\left\|u-v_h\right\|_{V_c} \\
& +C_2 \inf _{\mu_h \in M^h}\left\|\lambda-\mu_h\right\|_M \\
\left\|\lambda-\lambda_h\right\|_M & \leq C_3 \inf _{v_h \in V_c^h}\left\|u-v_h\right\|_{V_c}+C_4 \inf _{\mu_h \in M^h}\left\|\lambda-\mu_h\right\|_M
\end{aligned}
$$
where
$$
\begin{aligned}
& C_1=\left(1+\frac{M_a}{\gamma_a^h}\right)\left(1+\frac{M_b}{\gamma_b^h}\right), C_2=\frac{M_b}{\gamma_a^h} \\
& C_3=\frac{M_a}{\gamma_b^h}\left(1+\frac{M_a}{\gamma_a^h}\right)\left(1+\frac{M_b}{\gamma_b^h}\right), \\
& C_4=\left(1+\frac{M_b}{\gamma_b^h}+\frac{M_a M_b}{\gamma_a^h \gamma_b^h}\right)
\end{aligned}
$$

## 5 Numerical examples

In all the following experiments, we consider the domain $\Omega=(0,3)$. Moreover, the force $f_m$ applied at $x_m$ is chosen in such a way that the displacement at the right end of the domain, when using the continuum model everywhere in $\Omega$, is equal to unity. In what follows, we restrict ourselves to the cases where the equilibrium lengths of the springs are all equal.

### 5.1 Uniform springs coefficients with $\alpha_c, \alpha_d$ constant

In the first set of experiments, we consider uniform springs such that $k=k_i=1, i=1, \ldots, m$. In this simple case, the solutions of the spring model and of the equivalent continuum model in all of $\Omega$ are linear. The continuum model is used in the subdomain $\Omega_c=(0,2)$ while the particle model is used in $\Omega_d=(1,3)$ and the weight coefficients $\alpha_c$ and $\alpha_d$ are chosen to be $1/2$ in the overlap region. There are $m=8$ springs in $\Omega_d$, i.e., nine particles. The equilibrium length of each spring is then given by $l=l_i=0.25$. We discretize the continuum region with $N^e=4$ elements. Because the springs are uniform, the representative cell used to derive the corresponding Young's modulus $E$ is constituted of only one spring. Then
$$
E=k l=1 \times 0.25=0.25\qquad(29)
$$

We first consider the case where the two models are coupled via a particle coupling, that is, the finite element space $M^h$ for the Lagrange multipliers is dictated by the particles. As expected, this coupling ensures that the solutions of the Arlequin problem (28) are linear and that the continuum part exactly coincides with the particle solution over the overlap region in the three cases corresponding to the $L^2$ norm, $H^1$ seminorm, and $H^1$ norm couplings (Fig. 7). In these and subsequent plots, the initials LM refers to Lagrange multiplier. The solution at $x=3$ is equal to unity in the three cases.

We repeat above experiment using this time a continuum coupling, i.e., the elements in $M^h$ are the same as in $V_c^h$ on the overlap region. The coupling is therefore "weaker" than in the preceding experiment. The computed displacement at $x=3$ is now $z_m=1$ for the $H^1$ seminorm coupling, but $z_m=1.01042$ in the other two cases (see Fig. 8).

### 5.2 Non-uniform stiffness coefficients with $\alpha_c, \alpha_d$ constant

In more general settings, we are interested in problems in which the spring coefficients are not necessarily uniform but possibly randomly distributed. As a simple test case, we consider here a periodic distribution of springs with two spring stiffness constants $k_1=100$ and $k_2=1$. We have for $m$ even:
$$
\begin{aligned}
& k_{2 j-1}=k_1 \quad j=1, \ldots, m / 2 \\
& k_{2 j}=k_2 \quad j=1, \ldots, m / 2
\end{aligned}\qquad(30)
$$

![](./images/811921743445753857_14.jpg)

![](./images/811921743445753857_15.jpg)

Fig. 7 Uniform spring coefficients with particle coupling and $\alpha_c$, $\alpha_d$ constant. The three graphs correspond to $L^2$ norm, $H^1$ seminorm, and $H^1$ norm coupling cases

![](./images/811921743445753857_16.jpg)

Fig. 8 Uniform spring coefficients with continuum coupling and $\alpha_c$, $\alpha_d$ constant

As before, we consider the following geometry and discretization data: $\Omega_c=(0,2)$, $\Omega_d=(1,3)$ $m=8$, and $N^e=4$. The equilibrium length of the springs is once again equal to $l=l_i=0.25$. It follows that the Young's modulus is given by, using a representative cell (or representative volume element, RVE) made of two consecutive springs:

$$
E=\frac{k_1k_2}{k_1+k_2}2l=\frac{100}{101}0.5=0.49505 \tag{31}
$$

Figure 9 shows the Arlequin solutions in the case of particle coupling. It is not surprising that we find $z_m=0.691822$ in the three cases of coupling since such a coupling is necessarily too constraining.

In this problem, it is clear that the elements in $M_h$ should not be smaller than the representative cell used to derive the continuum model. For the continuum coupling, we see that the size of the elements in $M_h$ is equal to the size of one representative cell, i.e., $h=2l=0.5$. Figure 10 shows

![](./images/811921743445753857_17.jpg)

![](./images/811921743445753857_18.jpg)

Fig. 9 Periodic distribution of spring coefficients with particle coupling and $\alpha_c$, $\alpha_d$ constant. The three graphs correspond to $L^2$ norm, $H^1$ seminorm, and $H^1$ norm coupling cases

![](./images/811921743445753857_19.jpg)

Fig. 10 Periodic distribution of spring coefficients with continuum coupling and $\alpha_c$, $\alpha_d$ constant

the results when using continuum coupling. We observe that $z_m = 1$ for the $H^1$ seminorm coupling, but $z_m = 1.08727$ and $z_m = 1.08710$ for the $L^2$ and $H^1$ norm coupling, respectively. We note here that in the $H^1$ seminorm case, the constant modes of $V_d$ are fixed by setting $z_0$ to be equal to the displacement $u_h$ at $x_a$.

Remark 10 We observe in Fig. 10 a slight change in the slope of the continuum displacement $u$. This variation can be interpreted by writing the equilibrium equation at the interfacial point $x_a$. We have:

$$
\left.E \frac{d u}{d x}\right|_{x_{a}^{-}}=\left.\alpha_{c} E \frac{d u}{d x}\right|_{x_{a}^{+}}+\alpha_{d} k_{1} l_{1} \frac{w_{1}-w_{0}}{l_{1}} \tag{32}
$$

Because $\alpha_d = 1/2$ here, and thus does not vanish at $x_a$, nothing guarantees that the two derivatives should be the same on the left and right sides of $x_a$. This issue is therefore inherent to the choice $\alpha_c$ and $\alpha_d$ constant and should be

![](./images/811921743445753857_20.jpg)

![](./images/811921743445753857_21.jpg)

Fig. 11 Same as Fig. 10 but with $\alpha$ linear

![](./images/811921743445753857_22.jpg)

Fig. 12 Same as Fig. 10 but with $\alpha$ cubic

improved by the use of linear or cubic weight coefficients (see next subsection). Note that this was also observed in [12].

### 5.3 Influence of the weight coefficient $\alpha$

In this subsection, we study the effect of using linear and cubic weight coefficients. We consider here the same case as the one studied in the previous subsection with continuum coupling. We show in Figs. 11 and 12 the results with $\alpha$ linear and cubic, respectively. We now observe that the change in slope in the continuum displacement $u$ is no longer visible for the $L^{2}$ and $H^{1}$ norm couplings. However, a variation is the slope has appeared for the $H^{1}$ seminorm coupling. We do not have an explanation for this behavior at this time.

The linear and cubic cases apparently provide similar results to the naked eye. Actually, there exists a slight difference. Indeed, the displacements of the particle at $x_{m}$ with the $L^{2}$ and $H^{1}$ norm couplings are $z_{m}=1.04084$ for the linear case and $z_{m}=1.03707$ for the cubic case. These values are nevertheless greatly improved over the constant case for which approximately $z_{m}=1.087$.

![](./images/811921743445753857_23.jpg)

![](./images/811921743445753857_24.jpg)

Fig. 13 Same as Fig. 11 but with $h=l/2$ and element size for the Lagrange multiplier (LM) equal to $2l=\varepsilon$

## 5.4 Representative volume element

Our objective in this subsection is to show that the mesh size $h$ for the continuum solution can be chosen arbitrarily from the equilibrium length $l$ of the particles, but that it is important to select the size of the elements for the Lagrange multiplier at least equal to the size, denoted $\varepsilon$, of the representative cell or volume element. Note that the continuum coupling case then becomes a subcase of this configuration. We show in Fig. 13 the results with $\alpha$ linear when $h=l/2$ and the

<table>
<caption>Table 6 Displacements $z_m$ at $x=3$ for various mesh sizes and coupling types</caption>
<thead>
<tr>
<th>$h$</th>
<th>$L^2$ norm</th>
<th>$H^1$ seminorm</th>
<th>$H^1$ norm</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1.04084</td>
<td>0.994358</td>
<td>1.04084</td>
</tr>
<tr>
<td>1/2</td>
<td>1.04084</td>
<td>0.964384</td>
<td>1.04084</td>
</tr>
<tr>
<td>1/4 – 1/32</td>
<td>0.930203</td>
<td>0.930203</td>
<td>0.930203</td>
</tr>
</tbody>
</table>

The equilibrium length of each spring is $l=0.0625$

meshsizes for the Lagrange multiplier is equal to $\varepsilon$, which in this problem is simply $2l$. The results are exactly identical to the results obtained in Fig. 11 for the $L^2$ and $H^1$ norm couplings. However, the behavior of the continuum solution in the overlap region when using the $H^1$ seminorm coupling has the tendency to follow that of the particle solution. This is attributed to the fact that this type of coupling does not constrain enough the two displacement fields. In our opinion, the $H^1$ seminorm coupling should not be retained as a useful candidate for this type of simulations.

## 5.5 Influence of mesh size

In this section, we study the effect of the mesh size on the Arlequin solution. The equilibrium length of the springs is the same as in Sect. 5.2 and we vary the size of the elements in $V_c^h$ from $h=1$ to $h=1/32$. The stiffness of the springs is the same as in Sect. 5.2 and we consider here the continuum coupling.

We collect in Table 6 the displacements at $x=3$ for the different mesh sizes $h$ and coupling types based on the $L^2$ norm, $H^1$ seminorm, and $H^1$ norm. Here the weight coefficients $\alpha_c$ and $\alpha_d$ are chosen linear. For the $L^2$ and $H^1$ norms, the displacement at $x=3$ are constant for every value of $h$ until $h=1/4$ and then the value remains constant again. This shows that the solution is exact for every $h\leq1/4$ (i.e., the spacing of the particles), while for $h>1/4$, the "average" solution is linear and is resolved exactly with linear elements. For the $H^1$ seminorm, the results improve as $h$ decreases. Here, the solution is not exact due to the constant chosen (i.e., the solution match a point) so, as the mesh is refined, the constraint becomes enforced more exactly, until $h\leq1/4$ where the solution becomes exact.

We show in Figs. 11 and 14 the Arlequin solution and Lagrange multiplier, respectively, for $h=1/2$. The same results for the case $h=1/8$ are shown in Figs. 15 and 16 and then for $h=1/32$ in Figs. 17 and 18. Note that the Lagrange multipliers are constant for the $L^2$ and $H^1$ norms cases, and smooth for the $H^1$ seminorm coupling when $h=1/2$. For the $L^2$ norm, we observe that the Lagrange multiplier $\mu_h$ displays larger and larger variations as the mesh is refined. This result is commensurate with our theoretical results in the sense that the discrete inf-sup constant goes to zero linearly with $h$ if $\beta_2$ is set to zero. Note also how the linear $\alpha$ is reflec-

![](./images/811921743445753857_25.jpg)

![](./images/811921743445753857_26.jpg)

Fig. 14 Lagrange multiplier solution in the case $l=1/4$ and $h=1/2$ using the continuum coupling and $\alpha$ linear

![](./images/811921743445753857_27.jpg)

Fig. 15 Arlequin solution in the case $l=1/4$ and $h=1/8$ using the continuum coupling and $\alpha$ linear

ted in the character of the Lagrange multiplier solution - at the interface of the overlap and discrete domains, the Lagrange multiplier solution is zero when $h\leq1/4$.

## 5.6 Reconstruction of solutions

In the overlap region, the Arlequin method produces two solutions, one corresponding to the continuum model and the other to the particle model. Neither of these two solu- tions represents the solution of the problem at hand. It seems natural here to reconstruct a displacement field by combining the two solutions on the overlap region. This can be done in two ways. In the first one, we reconstruct a displacement field as follows:

$$
\hat{u}(x)=\alpha_{c} u_{h}(x)+\alpha_{d} \Pi z(x), \quad \forall x \in \Omega_{o} \tag{33}
$$

In the second one, a displacement vector is reconstructed as:

$$
\hat{z}_{i}=\alpha_{c} u_{h}\left(x_{i}\right)+\alpha_{d} z_{i}, \quad \forall i=1, \ldots, n_{o} \tag{34}
$$

![](./images/811921743445753857_28.jpg)

![](./images/811921743445753857_29.jpg)

Fig. 16 Lagrange multiplier solution in the case $l=1/4$ and $h=1/8$ using the continuum coupling and $\alpha$ linear

![](./images/811921743445753857_30.jpg)

Fig. 17 Arlequin solution in the case $l=1/4$ and $h=1/32$ using the continuum coupling and $\alpha$ linear

We show in Fig. 19 the Arlequin solution and reconstruc-ted solution in the case where a continuum coupling and $H^{1}$ norm coupling, along with constant weight coefficients $\alpha_{c}$ and $\alpha_{d}$, are used. Here $N^{e}=2$, and there are eight springs distributed over each element. We observe that the recons-tructed solution is discontinuous at both end points of the overlap domain and that the displacements display a rela-tively erratic behavior in $\Omega_{o}$. We show the same results in Fig. 20 with linear weight coefficients and the respective solutions look much better.

## 6 Conclusions

We have presented in this paper a technique to couple a par-ticle model with a continuum model. The proposed approach is essentially an extension of the Arlequin framework which had been previously developed to couple partial differential equation systems of different scales. We have given a detailed mathematical analysis of the coupled one-dimensional pro-blem and shown that the problem is well-posed when constant weight coefficients and linear coefficients are chosen in the

![](./images/811921743445753857_31.jpg)

![](./images/811921743445753857_32.jpg)

Fig. 18 Lagrange multiplier solution in the case $l=1/4$ and $h=1/32$ using the continuum coupling and $\alpha$ linear

overlap domain. However, it is not possible to show that the inf-sup condition is satisfied when using a coupling constraint based on the $L^2$ norm. This tells us that it is insufficient to enforce a constraint on the displacements only; this fact is actually observed experimentally as the Lagrange multiplier converges in this case to a distribution. We have also presented one-dimensional numerical examples with the objective of showing that the proposed approach was well suited to solve problems in which the spring constants in the particle model could be non-uniformly distributed. In particular, we considered a periodic system of two springs for which it is straightforward to derive an equivalent continuum model. We showed that the method produced satisfactory results as long as the mesh size used to discretize the Lagrange multiplier space was at least larger than (a multiple of) the size of the representative cell defined to compute the Young's modulus for the continuum model.

![](./images/811921743445753857_33.jpg)

Fig. 19 Arlequin solution and reconstructed solution using a continuum coupling for the Lagrange multiplier and the $H^1$ norm coupling with $\alpha$ constant

The present study of the Arlequin method for the coupling of particle and continuum models is by no means complete. This is a very preliminary work and numerous issues related to the method need to be addressed. For example, one question is whether we can define a coupling constraint that is explicitly dependent on the size of the representative cell (RVE) so that the formulation becomes fully independent of the mesh size. It would also be interesting to see how this method behaves in the case of nonlinear problems, for example, by considering potentials of the Lennard-Jones type. Finally, a major and important study will be to investigate the use of the method for problems in dimensions two and three and for time-dependent problems. We shall strive to address these issues and propose answers to these questions in forthcoming papers.

![](./images/811921743445753857_34.jpg)

![](./images/811921743445753857_35.jpg)

Fig. 20 Arlequin solution and reconstructed solution using a conti- nuum coupling for the Lagrange multiplier and the $H^{1}$ norm coupling with $\alpha$ linear

Acknowledgments S. Prudhomme would like to thank Denis Au- bry for the kind invitation to visit Ecole Centrale de Paris, France, during the Spring of 2006, where this work was initiated. P. T. Bauman acknowledges the support of the DOE Computational Science Graduate Fellowship. Support of this work by DOE under contract DE-FG02-05ER25701 is gratefully acknowledged.

## Appendix A: Technical Lemmas

We first recall without proof the classical Poincaré inequality in one dimension:

### Lemma A-1 (Poincaré Inequality)
Let $v \in H^{1}(\Omega_{c})$. Then
$$
\|v\|_{L^{2}\left(\Omega_{c}\right)}^{2} \leq \frac{\left|\Omega_{c}\right|^{2}}{2}|v|_{H^{1}\left(\Omega_{c}\right)}^{2} \leq \frac{\left|\Omega_{c}\right|^{2}}{2 E}\|v\|_{V_{c}}^{2}
\tag{35}
$$

### Lemma A-2
Let $v \in H^{1}(\Omega_{o})$ and let $\bar{v}$ be the average of $v$ on $\Omega_{o}$, i.e.,
$$
\bar{v}=\frac{1}{\left|\Omega_{o}\right|} \int_{\Omega_{o}} v d x
$$

Then
$$
\left|\Omega_{o}\right| \bar{v}^{2} \leq\|v\|_{L^{2}\left(\Omega_{o}\right)}^{2} \leq\left|\Omega_{o}\right| \bar{v}^{2}+\frac{\left|\Omega_{o}\right|^{2}}{2}|v|_{H^{1}\left(\Omega_{o}\right)}^{2}
$$

Proof Let $v \in H^{1}(\Omega_{o})$. We note that
$$
\begin{aligned}
\int_{\Omega_{o}}(v-\bar{v})^{2} d x &=\int_{\Omega_{o}} v^{2}-2 v \bar{v}+\bar{v}^{2} d x \\
&=\|v\|_{L^{2}\left(\Omega_{o}\right)}^{2}-2 \bar{v} \int_{\Omega_{o}} v d x+\bar{v}^{2}\left|\Omega_{o}\right| \\
&=\|v\|_{L^{2}\left(\Omega_{o}\right)}^{2}-\bar{v}^{2}\left|\Omega_{o}\right|
\end{aligned}
$$

The first inequality follows by observing that the integral on the left hand side is necessarily non-negative.

Let $\Omega_{o}$ be represented as the interval $(x_{a}, x_{b})$. Since $v$ is continuous on $\Omega_{o}$, we know that there exists $\bar{x}, x_{a} \leq \bar{x} \leq x_{b}$ such that $v(\bar{x})=\bar{v}$. We pose $v=\bar{v}+y$. Then
$$
\begin{aligned}
\|v\|_{L^{2}\left(\Omega_{o}\right)}^{2} &=\int_{\Omega_{o}}(\bar{v}+y)^{2} d x \\
&=\int_{\Omega_{o}} \bar{v}^{2} d x+2 \bar{v} \int_{\Omega_{o}} y d x+\int_{\Omega_{o}} y^{2} d x \\
&=\bar{v}^{2}\left|\Omega_{o}\right|+\int_{\Omega_{o}} y^{2} d x
\end{aligned}
$$
as the average of $y$, by definition, is simply zero. Moreover, since $y$ vanishes at $\bar{x}$ in $\Omega_{o}$, we can use the Poincaré inequality to find the bound:
$$
\int_{\Omega_{o}} y^{2} d x \leq \frac{\left|\Omega_{o}\right|^{2}}{2}|v|_{H^{1}\left(\Omega_{o}\right)}^{2}
$$
which completes the proof.
口

### Lemma A-3
Let $z \in \mathbb{R}^{n_{o}+1}$ and let $\bar{z}$ be the average of $z$ on $\Omega_{o}$. Then
$$
z_{n_{0}}^{2} \leq 2 \bar{z}^{2}+2 \sum_{i=1}^{n_{0}}\left(z_{i}-z_{i-1}\right)^{2}
$$

Proof Let $\bar{z}_{i}, i=1, \ldots, n_{o}$ be defined as:
$$
\bar{z}_{i}=\frac{l_{i}}{\left|\Omega_{o}\right|} \frac{z_{i}+z_{i-1}}{2}
$$

Thus,
$$
\begin{aligned}
\bar{z}_{i} &-\frac{l_{i}}{\left|\Omega_{o}\right|} \frac{z_{i}-z_{i-1}}{2} \\
&=\frac{l_{i}}{\left|\Omega_{o}\right|} z_{i-1}=\frac{l_{i}}{\left|\Omega_{o}\right|}\left(z_{n_{0}}-\sum_{k=i}^{n_{0}}\left(z_{k}-z_{k-1}\right)\right)
\end{aligned}
$$

![](./images/811921743445753857_36.jpg)

that is:
$$
\frac{l_i}{\left|\Omega_o\right|} z_{n_0}=\bar{z}_i-\frac{l_i}{\left|\Omega_o\right|}\left(\frac{z_i-z_{i-1}}{2}-\sum_{k=i}^{n_0}\left(z_k-z_{n_0}\right)\right)
$$

Summing over all terms in $i=1, \ldots, n_0$, and noting that $\sum \bar{z}_i=\bar{z}$ and $\sum_i l_i=\left|\Omega_o\right|$, we get:
$$
\begin{aligned}
z_{n_0} & =\bar{z}-\sum_{i=1}^{n_0} \frac{l_i}{\left|\Omega_o\right|}\left(\frac{z_i-z_{i-1}}{2}-\sum_{k=i}^{n_0}\left(z_k-z_{k-1}\right)\right) \\
& =\bar{z}+\sum_{i=1}^{n_0}\left[\frac{1}{\left|\Omega_o\right|}\left(\left(\sum_{k=1}^{i-1} l_k\right)+\frac{l_i}{2}\right)\right]\left(z_i-z_{i-1}\right)
\end{aligned}
$$

Therefore
$$
\begin{aligned}
\left|z_{n_0}\right| & \leq|\bar{z}|+\sum_{i=1}^{n_0}\left[\frac{1}{\left|\Omega_o\right|}\left(\left(\sum_{k=1}^{i-1} l_k\right)+\frac{l_i}{2}\right)\right]\left|z_i-z_{i-1}\right| \\
& \leq|\bar{z}|+\sum_{i=1}^{n_0}\left|z_i-z_{i-1}\right|
\end{aligned}
$$
which yields the desired result, using the fact that $(a+b)^2 \leq$ $2\left(a^2+b^2\right) a, b \in \mathbb{R}$.
口

## Appendix B: Proof of Lemmas for the continuous problem

### B.1 Continuity of $a$

**Lemma B-1** Let $a(\cdot, \cdot)$ be the bilinear form defined in (23). Then, for all $U=(u, w), V=(v, z) \in X$, there exists a constant $M_a>0$ such that:
$$
|a(U, V)| \leq M_a\|U\|_X\|(V)\|_X
$$
with $M_a=1$.

Proof From Cauchy-Schwarz and Hölder inequalities, we get
$$
\begin{aligned}
|a(U, V)| & \leq \int_{\Omega_c} \alpha_c E\left|u^{\prime}\right|\left|v^{\prime}\right| d x+\sum_{i=1}^m \alpha_i k_i\left|w_i-w_{i-1}\right|\left|z_i-z_{i-1}\right| \\
& \leq C_1\|u\|_{V_c}\|v\|_{V_c}+C_2|w|_{V_d}|z|_{V_d}
\end{aligned}
$$
where $C_1=\max _x\left(\alpha_c\right)=1$ and $C_2=\max _i\left(\alpha_i\right)=1$. From the definition of the norm in $V_d$, we then have:
$$
|a(U, V)| \leq\|u\|_{V_c}\|v\|_{V_c}+\|w\|_{V_d}\|z\|_{V_d} \leq\|U\|_X\|V\|_X
$$
and $M_a=1$.
口

### B.2 Continuity of $b$

**Lemma B-2** Let $b(\cdot, \cdot)$ be as defined in (23). Then, for all $\mu \in M, V=(v, z) \in X$, there exists a constant $M_b>0$ such that:
$$
|b(\mu, V)| \leq M_b\|\mu\|_M\|V\|_X
$$
with
$$
\begin{aligned}
M_b= & 2 \max \\
& \times\left(\sqrt{\frac{\beta_1\left|\Omega_c\right|^2+2 \beta_2}{2 E}}, \sqrt{\frac{\beta_1}{\delta}\left|\Omega_o\right|}, \sqrt{\frac{\beta_1\left|\Omega_o\right|^2+2 \beta_2}{2 \min _i k_i l_i}}\right)
\end{aligned}
$$

Proof By making use of Poincaré inequality (35) and the fact that $(a+b)^2 \leq 2\left(a^2+b^2\right), \forall a, b \in \mathbb{R}$, we get:
$$
\begin{aligned}
|b(\mu, V)| & \leq\|\mu\|_M\|v-\Pi z\|_M \\
& \leq\|\mu\|_M\left(\|v\|_M+\|\Pi z\|_M\right) \\
& \leq \sqrt{2}\|\mu\|_M \sqrt{\|v\|_M^2+\|\Pi z\|_M^2}
\end{aligned}
$$

Now,
$$
\begin{aligned}
\|v\|_M^2 & =\beta_1\|v\|_{L^2\left(\Omega_o\right)}^2+\beta_2|v|_{H^1\left(\Omega_o\right)}^2 \\
& \leq \beta_1\|v\|_{L^2\left(\Omega_c\right)}^2+\beta_2|v|_{H^1\left(\Omega_c\right)}^2 \\
& \leq \frac{\beta_1\left|\Omega_c\right|^2+2 \beta_2}{2 E}\|v\|_{V_c}^2
\end{aligned}
$$

In the same way, using Lemma A-2 and the fact that $\Pi z$ is a piecewise linear continuous function, we have
$$
\begin{aligned}
\|\Pi z\|_M^2 & =\beta_1\|\Pi z\|_{L^2\left(\Omega_o\right)}^2+\beta_2|\Pi z|_{H^1\left(\Omega_o\right)}^2 \\
& \leq \beta_1\left|\Omega_o\right| \bar{z}^2+\left(\beta_1 \frac{\left|\Omega_o\right|^2}{2}+\beta_2\right)|\Pi z|_{H^1\left(\Omega_o\right)}^2 \\
& \leq \frac{\beta_1}{\delta}\left|\Omega_o\right| \delta \bar{z}^2+\left(\frac{\beta_1\left|\Omega_o\right|^2+2 \beta_2}{2 \min _i k_i l_i}\right)|z|_{V_d}^2 \\
& \leq \max \left(\frac{\beta_1}{\delta}\left|\Omega_o\right|, \frac{\beta_1\left|\Omega_o\right|^2+2 \beta_2}{2 \min _i k_i l_i}\right)\|z\|_{V_d}^2
\end{aligned}
$$

We combine above results and find
$$
|b(\mu, V)| \leq M_b\|\mu\|_M\|V\|_X
$$
with:
$$
M_b=2 \max \left(\sqrt{\frac{\beta_1\left|\Omega_c\right|^2+2 \beta_2}{2 E}}, \sqrt{\frac{\beta_1}{\delta}\left|\Omega_o\right|}, \sqrt{\frac{\beta_1\left|\Omega_o\right|^2+2 \beta_2}{2 \min _i k_i l_i}}\right)
$$
口

### B.3 Continuity of $l$

**Lemma B-3** Let $l(\cdot)$ be as defined in (23). Then, for all $V \in$ $X$, there exists a constant $M_l>0$ such that:
$$
|l(V)| \leq M_l\|V\|_X
$$
with
$$
M_l=2|f| \max \left(\frac{1}{\sqrt{\delta}}, \frac{1}{\sqrt{\min _i k_i}}\right)
$$

![](./images/811921743445753857_37.jpg)

Proof From definition of $l(\cdot)$, we have, with $V=(v,z)$:

$$
\begin{aligned}
|l(V)| & \leq\left|f z_{m}\right| \leq|f|\left|z_{m}\right| \leq|f|\left|z_{n_{o}}+\sum_{i=n_{o}+1}^{m}\left(z_{i}-z_{i-1}\right)\right| \\
& \leq|f| \sqrt{2 z_{n_{o}}^{2}+2 \sum_{i=n_{o}+1}^{m}\left(z_{i}-z_{i-1}\right)^{2}}
\end{aligned}
$$

Using Lemma A-3 yields:

$$
\begin{aligned}
|l(V)| & \leq|f| \sqrt{4 \bar{z}^{2}+4 \sum_{i=1}^{n_{o}}\left(z_{i}-z_{i-1}\right)^{2}+2 \sum_{i=n_{o}+1}^{m}\left(z_{i}-z_{i-1}\right)^{2}} \\
& \leq|f| \sqrt{\frac{4}{\delta} \delta \bar{z}^{2}+\frac{4}{\min _{i} k_{i}} \sum_{i=1}^{m} k_{i}\left(z_{i}-z_{i-1}\right)^{2}} \\
& \leq 2|f| \sqrt{\max \left(\frac{1}{\delta}, \frac{1}{\min _{i} k_{i}}\right)\left(|z|_{V_{d}}^{2}+\bar{z}^{2}\right)}
\end{aligned}
$$

It follows that

$$|l(V)| \leq M_{l}\|z\|_{V_{d}} \leq M_{l}\|(v,z)\|_{X}=M_{l}\|V\|_{X}$$

with

$$M_{l}=2|f| \max \left(\frac{1}{\sqrt{\delta}}, \frac{1}{\sqrt{\min _{i} k_{i}}}\right)$$

$\square$

## References

1. Babuška I (1973) The finite element method with Lagrangian multipliers. Numer Math 20:179–192

2. Belytschko T, Xiao SP (2003) Coupling methods for continuum model with molecular model. Int J Multiscale Comput Eng 1(1):115–126

3. Ben Dhia H (1998) Multiscale mechanical problems: the Arlequin method. C R Acad Sci Paris Sér IIB 326(12):899–904

4. Ben Dhia H (2006) Global local approaches: the Arlequin framework. Eur J Comput Mech 15(1–3):67–80

5. Ben Dhia H, Rateau G (2001) Mathematical analysis of the mixed Arlequin method. C R Acad Sci Paris Sér I 332:649–654

6. Ben Dhia H, Rateau G (2002) Application of the Arlequin method to some structures with defects. Rev Eur Eléments Finis 332:649–654

7. Ben Dhia H, Rateau G (2005) The Arlequin method as a flexible engineering design tool. Int J Numer Meth Eng 62(11):1442–1462

8. Brezzi F (1974) On the existence, uniqueness and approximation of saddle-point problems arising from Lagrange multipliers. RAIRO Anal Numér 8(R-2):129–151

9. Broughton JQ, Abraham FF, Bernstein N, Kaxiras E (1999) Concurrent coupling of length scales: methodology and application. Phys Rev B 60(4):2391–2403

10. Ern A, Guermond JL (2004) Theory and practice of finite elements. Springer, New York

11. Fish J (2006) Bridging the scales in nano engineering and science. J Nanoparticle Res 8(6):577–594

12. Guidault P, Belytschko T (2007) On the $L^{2}$ and the $H^{1}$ couplings for an overlapping domain decomposition method using Lagrange multipliers. Int J Numer Meth Eng 70(3):322–350

13. Liu WK, Karpov EG, Zhang S, Park HS (2004) An introduction to computational nanomechanics and materials. Comput Methods Appl Mech Eng 193:1529–1578

14. Miller RE, Tadmor EB (2002) The quasicontinuum method: overview, applications, and current directions. J Comput Aided Des 9:203–239

15. Oden JT, Prudhomme S, Romkes A, Bauman P (2006) Multi-scale modeling of physical phenomena: adaptive control of models. SIAM J Sci Comput 28(6):2359–2389

16. Prudhomme S, Bauman PT, Oden JT (2006) Error control for molecular statics problems. Int J Multiscale Comput Eng 4(5-6):647–662

17. Prudhomme S, Ben Dhia H, Bauman PT, Elkhodja N, Oden JT (2008) Computational analysis of modeling error for the coupling of particle and continuum models by the arlequin method. Computer Methods in Applied Mechanics and Engineering (To appear)

18. Wagner GJ, Liu WK (2003) Coupling of atomistic and continuum simulations using a bridging scale decomposition. J Comput Phys 190:249–274

19. Xiao SP, Belytschko T (2004) A bridging domain method for coupling continua with molecular dynamics. Comput Methods Appl Mech Eng 193:1645–1669

![](./images/811921743445753857_38.jpg)