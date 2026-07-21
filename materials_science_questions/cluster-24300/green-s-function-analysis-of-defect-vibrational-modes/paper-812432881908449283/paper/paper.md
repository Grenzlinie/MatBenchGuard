# Scattering of phonons from a substitutional impurity

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1965 Proc. Phys. Soc. 85 1223

(http://iopscience.iop.org/0370-1328/85/6/322)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 160.36.178.25
This content was downloaded on 19/08/2015 at 15:39

Please note that [terms and conditions apply].

# Scattering of phonons from a substitutional impurity

M. YUSSOUFF and J. MAHANTY

Department of Physics, Indian Institute of Technology, Kanpur, India

MS. received 21st January 1965

Abstract. The scattering of phonons from a substitutional impurity in a simple cubic lattice is studied in detail. The scattering amplitude is expressed in terms of partial waves characterized by the irreducible representations of the point group of the lattice, and the total scattering cross section is found by using the optical theorem. The condition for occurrence of resonances in each partial wave amplitude is investigated. In an appendix, a table of the Green's function integrals for a simple cubic lattice is given.

## 1. Introduction

The study of the scattering of phonons from point defects has attracted the attention of many investigators in recent years (Lifshitz 1956, Takeno 1963, Callaway 1963, Wagner 1964, Callaway 1964), particularly after experimental detection of resonances in scattering cross sections from low temperature thermal conductivity data (Walker and Pohl 1963). The problem is a particular case of the more general one of scattering at point defects of quasi-particles in crystalline solids which has been studied by Callaway (1964). Two features characterize the scattering of quasi-particles. Firstly, the dispersion law giving the $\mathbf{k}$ (wave number) dependence of the single-particle energy reveals the typical band structure involving both an upper and lower bound to the energy-this feature permits the possibility of occurrence of bound states both above and below the band, depending on the nature of the scatterer. Secondly, the interaction due to the scatterer usually possesses the symmetry of the point group of the crystal, rather than the spherical symmetry of potentials studied in the theory of potential scattering. The latter feature necessitates a change in the method of partial wave analysis of the scattering amplitude, which now has to be decomposed in terms of the irreducible representations of the point group of the lattice. The object of this paper is to give an exact solution of the problem of scattering of phonons from a substitutional impurity, which is coupled to nearest neighbours in a simple cubic lattice with force constants that differ from the normal value, and whose mass also differs from that of the normal atoms. We shall study the lattice model used by Montroll and Potts (1955).

## 2. The equation of motion of the lattice with impurity

In the lattice model to be considered here each atom has a mass $M$ and is coupled to its nearest neighbours through central and non-central forces characterized by a force constant $\gamma$, except the impurity atom whose mass is $M+\Delta M$, and which is coupled through force constants $\gamma+\Delta \gamma$. The defect is taken to be at the origin of the coordinate

system and the lattice sites are specified by the integers $(l, m, n)$. The total number of atoms is $N$.

For the perfect lattice the time-independent equations of motion are written in matrix form as
$$
\mathbf{D} \mathbf{U}-M \omega^{2} \mathbf{I} \mathbf{U}=\mathbf{O}
\tag{1}
$$
where, for this simple model, the $3N \times 3N$ matrix $\mathbf{D}$ can be written in the form
$$
\mathbf{D}=\left(\begin{array}{lll}
\mathbf{A} & 0 & 0 \\
0 & \mathbf{A} & 0 \\
0 & 0 & \mathbf{A}
\end{array}\right)
\tag{2}
$$
in which $\mathbf{D}$ is partitioned into $N \times N$ submatrices. The elements of $\mathbf{A}$ are given by
$$
\begin{aligned}
\mathbf{A}\left(l, m, n | l^{\prime}, m^{\prime}, n^{\prime}\right)=& \gamma\left[6 \delta\left(l, l^{\prime}\right) \delta\left(m, m^{\prime}\right) \delta\left(n, n^{\prime}\right)\right. \\
&-\delta\left(m, m^{\prime}\right) \delta\left(n, n^{\prime}\right)\left\{\delta\left(l^{\prime}, l+1\right)+\delta\left(l^{\prime}, l-1\right)\right\} \\
&-\delta\left(l, l^{\prime}\right) \delta\left(n, n^{\prime}\right)\left\{\delta\left(m^{\prime}, m+1\right)+\delta\left(m^{\prime}, m-1\right)\right\} \\
&-\delta\left(l, l^{\prime}\right) \delta\left(m, m^{\prime}\right)\left\{\delta\left(n^{\prime}, n+1\right)+\delta\left(n^{\prime}, n-1\right)\right\}].
\end{aligned}
\tag{3}
$$

The $3N$-dimensional vector $\mathbf{U}$ can also be partitioned into the form
$$
\mathbf{U}=\left(\begin{array}{l}
\mathbf{X} \\
\mathbf{Y} \\
\mathbf{Z}
\end{array}\right)
\tag{4}
$$
where $\mathbf{X}, \mathbf{Y}, \mathbf{Z}$ are $N$-dimensional vectors each having components with indices $(l, m, n)$. $X(l, m, n)$ stands for the displacement from equilibrium of the $(l, m, n)$ atom in the $x$ direction. Since $\mathbf{A}$ is a cyclic matrix its eigenvectors $\Phi(\mathbf{k})$ have the components
$$
\Phi(\mathbf{k} | l, m, n)=N^{-1 / 2} \exp \left\{i\left(k_{1} l+k_{2} m+k_{3} n\right)\right\}
\tag{5}
$$
and the corresponding frequency (squared) is
$$
\omega^{2}(\mathbf{k})=\frac{2 \gamma}{M}\left(3-\sum_{j=1}^{3} \cos k_{j}\right).
\tag{6}
$$

In this model the defect does not couple the displacement components, so that we need to study its effect on the $x$ displacements only. The effect on $y$ and $z$ displacements will be the same. The equation of motion for the $x$ displacements can be written as
$$
\mathbf{A X}-M \omega^{2} \mathbf{I X}=+\mathbf{P X}
\tag{7}
$$
where the perturbation matrix $\mathbf{P}$ has non-vanishing elements only when the indices correspond to the defect site or its nearest neighbours. The only non-vanishing elements are
$$
\begin{aligned}
\mathbf{P}(0,0,0 | 0,0,0) &=(\Delta \gamma)\left(\frac{\Delta M}{\Delta \gamma} \omega^{2}-6\right) \\
\mathbf{P}( \pm 1,0,0 | 0,0,0) &=\mathbf{P}(0, \pm 1,0 | 0,0,0)=\mathbf{P}(0,0, \pm 1 | 0,0,0) \\
&=\mathbf{P}(0,0,0 | \pm 1,0,0)=\mathbf{P}(0,0,0 | 0, \pm 1,0)=\mathbf{P}(0,0,0 | 0,0, \pm 1)=\Delta \gamma \\
\mathbf{P}( \pm 1,0,0 | \pm 1,0,0) &=\mathbf{P}(0, \pm 1,0 | 0, \pm 1,0)=\mathbf{P}(0,0, \pm 1 | 0,0, \pm 1)=-\Delta \gamma.
\end{aligned}
\tag{8}
$$


The solution of equation (7) outside the unperturbed band will give the discrete frequencies corresponding to bound states in potential scattering. The scattering state solutions are obtained for values of $\omega^2$ within the unperturbed band, and can be written as satisfying an equation of the form

$$
\mathbf{X}=\mathbf{X}^{(0)}-\mathbf{G P X} \tag{9}
$$

where

$$
-\mathbf{G}=\left(\mathbf{A}-M \omega^{2} \mathbf{I}\right)^{-1} \tag{10}
$$

and $\mathbf{X}^{(0)}$ is an unperturbed solution having the same eigenvalue as $\mathbf{X}$. In a large lattice, since the frequencies form a continuum, it is always possible to find $\mathbf{X}^{(0)}$ and $\mathbf{X}$.

Formally, the solution of equation (9) can be written in the form

$$
\mathbf{X}=\mathbf{X}^{(0)}-(\mathbf{I}+\mathbf{G P})^{-1} \mathbf{G P} \mathbf{X}^{(0)}. \tag{11}
$$

### 3. The solution for the scattering amplitude
The number of non-vanishing elements of the perturbation matrix is determined by the range of the interaction due to the defect and the lattice structure. We can therefore write $\mathbf{P}$ in a partitioned form

$$
\mathbf{P}=\left(\begin{array}{ccccc}
\mathbf{p} & 0 & 0 & \ldots & 0 \\
0 & 0 & 0 & \ldots & 0 \\
\cdot & \cdot & \cdot & \cdot \cdot \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \cdot \cdot & \cdot \\
0 & 0 & 0 & \ldots & 0
\end{array}\right) \tag{12}
$$

where the submatrix $\mathbf{p}$ is the only non-vanishing submatrix of $\mathbf{P}$. Similarly we can partition $\mathbf{G}$ and $\mathbf{X}$:

$$
\mathbf{G}=\left(\begin{array}{ccccc}
\mathbf{g} & \mathbf{g}_{12} & \mathbf{g}_{13} & \ldots \\
\mathbf{g}_{21} & \mathbf{g}_{22} & \mathbf{g}_{23} & \ldots \\
\cdot & \cdot & \cdot & \\
\cdot & \cdot & \cdot &
\end{array}\right) \tag{13}
$$

and

$$
\mathbf{X}=\left(\begin{array}{c}
\mathbf{x} \\
\mathbf{x}_{1} \\
\mathbf{x}_{2} \\
\cdot \\
\cdot
\end{array}\right) \tag{14}
$$

where the position and dimension of the submatrix $\mathbf{g}$ corresponds to that of $\mathbf{p}$, and $\mathbf{x}$ is the subspace of $\mathbf{X}$ which is acted upon by $\mathbf{p}$.

We can now define a vector $\mathbf{S}$, such that

$$
\mathbf{S}=\mathbf{P X}=\left(\begin{array}{c}
\mathbf{p x} \\
0 \\
0 \\
\cdot \\
\cdot
\end{array}\right) \equiv\left(\begin{array}{c}
\mathbf{s} \\
0 \\
0 \\
\cdot \\
\cdot
\end{array}\right). \tag{15}
$$

If we now write equation (9) in the partitioned form, we have

$$
\begin{pmatrix}
\mathbf{x} \\
\mathbf{x}_{1} \\
\mathbf{x}_{2} \\
\vdots \\
\vdots
\end{pmatrix}
=
\begin{pmatrix}
\mathbf{x}^{(0)} \\
\mathbf{x}_{1}^{(0)} \\
\mathbf{x}_{2}^{(0)} \\
\vdots \\
\vdots
\end{pmatrix}
-
\begin{pmatrix}
\mathbf{g} & \mathbf{g}_{12} & \cdots \\
\mathbf{g}_{21} & \mathbf{g}_{22} & \cdots \\
\vdots & \vdots & \ddots \\
\vdots & \vdots & \ddots
\end{pmatrix}
\begin{pmatrix}
\mathbf{s} \\
0 \\
0 \\
\vdots \\
\vdots
\end{pmatrix}.
\tag{16}
$$

Multiplying both sides of equation (16) from the left by $\mathbf{P}$, we have the following reduced equation for $\mathbf{s}$:
$$
\mathbf{s} = \mathbf{s}^{(0)} - \mathbf{p g s}
\tag{17}
$$
where
$$
\mathbf{s}^{(0)} = \mathbf{p x}^{(0)}.
\tag{18}
$$

Solving equation (17) and substituting in equation (16), we obtain the complete solution of equation (9). The advantage of this procedure is that equation (17) involves vectors of a small number of dimensions, so that the solution of this equation is considerably simpler than that of equation (9). In the particular case that we will consider in the next section $\mathbf{s}$ will be a seven-dimensional vector.

Equation (17) can be written as
$$
(\mathbf{I} + \mathbf{p g})\mathbf{s} = \mathbf{s}^{(0)} = \mathbf{p x}^{(0)}.
\tag{19}
$$

If, as is usually the case, $\mathbf{p}$ and $\mathbf{g}$ have the symmetry of the point group of the lattice, they can both be block-diagonalized by a unitary transformation. We can thus write
$$
\mathbf{V}^{+}(\mathbf{I} + \mathbf{p g})\mathbf{V} = \mathbf{T}
\tag{20}
$$
where $\mathbf{T}$ is the block-diagonalized form of $\mathbf{I} + \mathbf{p g}$ and $\mathbf{V}$ is a unitary matrix which can be constructed from the symmetries of $\mathbf{p}$. Hence equation (19) can be written as
$$
\mathbf{V T V}^{+}\mathbf{s} = \mathbf{p x}^{(0)}
$$
or
$$
\mathbf{s} = \mathbf{V T}^{-1}\mathbf{V}^{+}\mathbf{p x}^{(0)}.
\tag{21}
$$

Since the block-diagonal matrix $\mathbf{T}$ has small submatrices along the diagonal, its inverse occurring in equation (21) can be found easily. Thus $\mathbf{T}^{-1}$ can be written as
$$
\mathbf{T}^{-1} = \begin{pmatrix}
\mathbf{M}_{1}^{-1} & 0 & 0 & \cdots \\
0 & \mathbf{M}_{2}^{-1} & 0 & \cdots \\
\vdots & \vdots & \vdots & \ddots \\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
= \sum_{\nu=1}^{h} \mathbf{T}_{\nu}^{-1}
\tag{22}
$$
where
$$
\mathbf{T}_{\nu}^{-1} = \begin{pmatrix}
0 & 0 & 0 & 0 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \cdots \\
0 & \cdot & 0 & 0 & \cdots \\
0 & \cdot & 0 & \mathbf{M}_{\nu}^{-1} & \ddots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
\tag{23}
$$
and $h$ is the number of submatrices in the block-diagonal form of $\mathbf{T}$. Using equation (22) in (21), we obtain
$$
\mathbf{s} = \sum_{\nu=1}^{h} \mathbf{V T}_{\nu}^{-1}\mathbf{V}^{+}\mathbf{p x}^{(0)} = \sum_{\nu=1}^{h} \mathbf{s}_{\nu}
\tag{24}
$$
where
$$
\mathbf{s}_{\nu} = \mathbf{V T}_{\nu}^{-1}\mathbf{V}^{+}\mathbf{p x}^{(0)}.
$$

We can now express the solution of equation (9) in the form

$$
\mathbf{X}=\mathbf{X}^{(0)}-\sum_{\nu=1}^{h} \mathbf{G} \mathbf{S}_{\nu}
\tag{25}
$$

where

$$
\mathbf{S}_{\nu}=\left(\begin{array}{c}
\mathbf{s}_{\nu} \\
0 \\
0 \\
\vdots \\
\vdots
\end{array}\right)
$$

i.e. the only non-vanishing components of the $N$-dimensional vector $\mathbf{S}_{\nu}$ are those corresponding to the components of $\mathbf{s}_{\nu}$.

Equation (25) is the analogue of the familiar partial wave analysis result of the theory of potential scattering. Here the number of terms is finite and equals the number of sub-matrices in the block-diagonal form of $\mathbf{p}$, which in turn depends on the range of the interaction due to the impurity and the point group of the crystal. In component form, equation (25) can be written as

$$
X(l, m, n)=X^{(0)}(l, m, n)-\sum_{\nu=1}^{h} \sum_{\alpha, \beta, \mu} \mathbf{G}(l, m, n \mid \alpha, \beta, \mu) S_{\nu}(\alpha, \beta, \mu)
\tag{26}
$$

where the indices $\alpha, \beta, \mu$ refer to the lattice sites affected by the perturbation and the summation is over all of them.

The elements of $\mathbf{G}$ are well known (Montroll and Potts 1955), and are given by

$$
\mathbf{G}\left(l, m, n \mid l^{\prime}, m^{\prime}, n^{\prime}\right)=-\frac{1}{M(2 \pi)^{3}} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \frac{\exp (i \mathbf{k} . \mathbf{R}) d^{3} k}{\omega^{2}(\mathbf{k})-\omega^{2}-i \epsilon}
\tag{27}
$$

where $R_{1}=l^{\prime}-l, R_{2}=m^{\prime}-m, R_{3}=n^{\prime}-n$. Then equation (26) reduces to

$$
\begin{aligned}
X(l, m, n) & =X^{(0)}(l, m, n) \\
& +\frac{1}{(2 \pi)^{3} M} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} \frac{\exp \left\{i\left(k_{1} l+k_{2} m+k_{3} n\right)\right\} d^{3} k}{\omega^{2}(\mathbf{k})-\omega^{2}-i \epsilon} \sum_{\nu=1}^{h} F_{\nu}(\mathbf{k})
\end{aligned}
\tag{28}
$$

where $F_{\nu}(\mathbf{k})$ are some trigonometric functions of the components of $\mathbf{k}$, obtainable from equations (27) and (26) once the structure of $\mathbf{S}_{\nu}$ is known.

The asymptotic form of equation (28) for large distances from the impurity can be obtained by the method of stationary phase (Koster and Slater 1954), and is given by

$$
X(\mathbf{R})=X^{(0)}(\mathbf{R})+\frac{1}{2 \pi} \sum_{\mathbf{k}_{0}} \frac{\exp (i \mathbf{k} . \mathbf{R})}{R} g\left(\mathbf{k}_{0}\right) \sum_{\nu} F_{\nu}\left(\mathbf{k}, \mathbf{k}_{0}\right)
\tag{29}
$$

where

$$
g\left(\mathbf{k}_{0}\right)=\frac{1}{2 \gamma}\left(\frac{\sin ^{2} k_{01}+\sin ^{2} k_{02}+\sin ^{2} k_{03}}{\sin ^{2} k_{01} \cos k_{02} \cos k_{03}+\sin ^{2} k_{02} \cos k_{01} \cos k_{03}+\sin ^{2} k_{03} \cos k_{01} \cos k_{02}}\right)^{1 / 2}
\tag{30}
$$

and $\mathbf{k}_{0}$ is a solution of the equation $\omega^{2}(\mathbf{k})=\omega^{2}$, with $\left.\nabla_{k} \omega^{2}(\mathbf{k})\right|_{\mathbf{k}_{0}}$ having the direction of $\mathbf{R}$, whose components are $l, m, n$. Thus $\mathbf{k}_{0}$ defines the direction of the scattered wave whereas $\mathbf{k}$ defines the direction of the incident wave.

## 4. The partial wave analysis for the specific model

The unitary transformation matrix $\mathbf{V}$ corresponding to the model under consideration can be obtained by group theoretic methods. The point group symmetry of the lattice is $O_{\mathrm{h}}$, and the reducible representation generated by the displacements of the seven affected lattice sites can be reduced in the usual notation to $2 A_{1 \mathrm{~g}}+F_{1 \mathrm{u}}+E_{\mathrm{g}}$. The explicit form of $\mathbf{V}$ has been given by Wolfram and Callaway (1963) in connection with their treatment of the problem of the scattering of spin waves from an impurity in a simple cubic crystal. Using this form of $\mathbf{V}$, the matrix $\mathbf{I}+\mathbf{g p}$ can be block-diagonalized into submatrices corresponding to the representations $A_{1 \mathrm{~g}}, F_{1 \mathrm{u}}$ and $E_{\mathrm{g}}$ respectively. The first leads to 'S-type' partial waves, the second to 'P-type' and the third to 'D-type' respectively. We thus have only three partial waves in this problem.

In the following, the results are expressed in terms of Green's function integrals which can be written as (Wolfram and Callaway 1963)

$$
I(p, q, r)=i^{p+q+r+1} \int_{0}^{\infty} J_{p}(t) J_{q}(t) J_{r}(t) \exp (-i E t) d t
$$

where $E=3-M \omega^{2} / 2 \gamma$ and $p, q, r$ are integers.

The general method of $\S 3$, when applied to this model, gives the following explicit forms for the $\mathbf{M}_{\nu}{ }^{-1}$ occurring in equation (23):

$$
\mathbf{M}_{1}{ }^{-1}=\frac{\Delta \gamma}{F_{\mathrm{S}}}\left(\begin{array}{cc}
Q & -\sqrt{ } 6 H \\
-\sqrt{ } 6\left(C_{0}-E_{0}\right) & 1 / \Delta \gamma+A C_{0}+6 E_{0}
\end{array}\right)
$$

$$
\mathbf{M}_{2}{ }^{-1}=\mathbf{M}_{4}{ }^{-1}=\mathbf{M}_{5}{ }^{-1}=1 / F_{\mathbf{P}}
$$

$$
\mathbf{M}_{3}{ }^{-1}=\mathbf{M}_{6}{ }^{-1}=1 / F_{\mathrm{D}}
$$

where

$$
\begin{aligned}
F_{\mathrm{S}}=1+ & \frac{\Delta \gamma}{2 \gamma}\{I(2,0,0)+7 I(0,0,0)+4 I(1,1,0)-12 I(1,0,0)\} \\
& -\frac{\Delta M}{2 \gamma} \omega^{2} I(0,0,0)+\frac{\Delta M}{2 \gamma} \frac{\Delta \gamma}{2 \gamma} \omega^{2}\left[6 I^{2}(1,0,0)\right. \\
& -I(0,0,0)\{4 I(1,1,0)+I(2,0,0)+I(0,0,0)\}]
\end{aligned}
$$

$$
F_{\mathrm{P}}=1+\frac{\Delta \gamma}{2 \gamma}\{I(0,0,0)-I(2,0,0)\}
$$

$$
F_{\mathrm{D}}=1+\frac{\Delta \gamma}{2 \gamma}\{I(0,0,0)+I(2,0,0)-2 I(1,1,0)\}
$$

$$
A=\frac{\Delta M}{\Delta \gamma} \omega^{2}-6
$$

$$
H=A E_{0}+C_{0}-\frac{1}{2 \gamma}\{4 I(1,1,0)+I(2,0,0)\}
$$

$$
Q=\frac{1}{\Delta \gamma}+6 E_{0}-C_{0}+\frac{1}{2 \gamma}\{4 I(1,1,0)+I(2,0,0)\}
$$

$$
E_{0}=-\frac{1}{2 \gamma} I(1,0,0)
$$

$$
C_{0}=-\frac{1}{2 \gamma} I(0,0,0).
$$

Using the expressions for $\mathbf{M}_{\nu}{ }^{-1}$, equation (29) can be written in the form
$$
X(\mathbf{R})=X^{(0)}(\mathbf{R})+f\left(\mathbf{k}, \mathbf{k}_{0}\right) \frac{\exp (i \mathbf{k} \cdot \mathbf{R})}{R \sqrt{ } N}
\tag{33}
$$
where $f(\mathbf{k}, \mathbf{k}_{0})$ is the scattering amplitude. The angle between the incident wave vector $\mathbf{k}$ and the final wave vector $\mathbf{k}_{0}$ is the scattering angle. In terms of partial wave amplitudes,
$$
f\left(\mathbf{k}, \mathbf{k}_{0}\right)=f_{\mathrm{S}}\left(\mathbf{k}, \mathbf{k}_{0}\right)+f_{\mathrm{P}}\left(\mathbf{k}, \mathbf{k}_{0}\right)+f_{\mathrm{D}}\left(\mathbf{k}, \mathbf{k}_{0}\right).
$$

The S-wave amplitude is
$$
\begin{aligned}
f_{\mathrm{S}}\left(\mathbf{k}, \mathbf{k}_{0}\right)= & \frac{g\left(\mathbf{k}_{0}\right)}{2 \pi} \frac{1}{F_{\mathrm{S}}}\left[\Delta M \omega^{2}-6 \Delta \gamma+\frac{\Delta \gamma \Delta M \omega^{2}}{2 \gamma}\{4 I(1,1,0)\right. \\
& +I(2,0,0)+I(0,0,0)\}+2 \Delta \gamma\left\{1-\frac{\Delta M \omega^{2}}{2 \gamma} I(1,0,0)\right\}\left\{\sum_{\imath=1}^{3} \cos k_{\imath}+\sum_{i=1}^{3} \cos k_{0 \imath}\right\} \\
& \left.-\frac{2 \Delta \gamma}{3}\left\{1-\frac{\Delta M \omega^{2}}{2 \gamma} I(0,0,0)\right\}\left\{\sum_{i=1}^{3} \cos k_{\imath}\right\}\left\{\sum_{\imath=1}^{3} \cos k_{0 \imath}\right\}\right].
\tag{34a}
\end{aligned}
$$

The P-wave amplitude is
$$
f_{\mathrm{P}}\left(\mathbf{k}, \mathbf{k}_{0}\right)=-\frac{2 g\left(\mathbf{k}_{0}\right)}{2 \pi} \frac{\Delta \gamma}{F_{\mathrm{P}}}\left[\sin k_{1} \sin k_{01}+\sin k_{2} \sin k_{02}+\sin k_{3} \sin k_{03}\right].
\tag{34b}
$$

The D-wave amplitude is
$$
\begin{aligned}
f_{\mathrm{D}}\left(\mathbf{k}, \mathbf{k}_{0}\right)= & -\frac{g\left(\mathbf{k}_{0}\right)}{2 \pi} \frac{\Delta \gamma}{3 F_{\mathrm{D}}}\left\{3\left(\cos k_{2}-\cos k_{3}\right)\left(\cos k_{02}-\cos k_{03}\right)\right. \\
& \left.+\left(2 \cos k_{1}-\cos k_{2}-\cos k_{3}\right)\left(2 \cos k_{01}-\cos k_{02}-\cos k_{03}\right)\right\}.
\tag{34c}
\end{aligned}
$$

When the substitutional impurity is an isotope the P- and D-wave amplitudes vanish and the S-wave amplitude remains in the form
$$
f_{\mathrm{S}}\left(\mathbf{k}, \mathbf{k}_{0}\right)=\frac{g\left(\mathbf{k}_{0}\right)}{2 \pi} \frac{1}{F_{\mathrm{S}}} \Delta M \omega^{2}.
$$

## 5. Resonances in the scattering cross section

A resonance in the scattering cross section will occur for that value of the frequency at which the denominator of any of the partial wave amplitudes vanishes. Since the denominators contain $F_{\mathrm{S}}, F_{\mathrm{P}}$ and $F_{\mathrm{D}}$, it is sufficient for us to investigate the circumstances when these functions vanish.

In general $F_{\mathrm{S}}, F_{\mathrm{P}}$, and $F_{\mathrm{D}}$ are complex functions of $E$ which is defined according to equation (31). Within the band $-3 \leqslant E \leqslant 3$ and for specific choice of $\Delta \gamma / \gamma$ and $\Delta M / M$ one would obtain a resonance for
$$
\text{real part of }F=0
$$
and the level width $\Gamma=\mathscr{I} F /(\mathscr{R} F)^{\prime}$ small and positive. Here the prime denotes the derivative with respect to $\omega^{2}$. The real and imaginary parts of the $F$ functions are given

below in terms of the quantities
$$
C(p, q, r)=\int_{0}^{\infty} \cos (E t) J_{p}(t) J_{q}(t) J_{r}(t) d t \tag{35a}
$$
and
$$
S(p, q, r)=\int_{0}^{\infty} \sin (E t) J_{p}(t) J_{q}(t) J_{r}(t) d t. \tag{35b}
$$

A table of these integrals is given in the appendix. The real and imaginary parts of the $F$ functions are
$$
\begin{aligned}
\mathscr{R} F_{\mathrm{S}}= & 1-\frac{\Delta M}{M}(3-E) S(0,0,0)+\frac{\Delta \gamma}{2 \gamma}\{7 S(0,0,0) \\
& +12 C(1,0,0)-4 S(1,1,0)-S(2,0,0)\} \\
& +\frac{\Delta \gamma}{2 \gamma} \frac{\Delta M}{M}(3-E)\left[6\left\{C^{2}(1,0,0)-S^{2}(1,0,0)\right\}\right. \\
& -C(0,0,0)\{4 C(1,1,0)+C(2,0,0)-C(0,0,0)\} \\
& +S(0,0,0)\{4 S(1,1,0)+S(2,0,0)-S(0,0,0)\}]
\end{aligned} \tag{36a}
$$

$$
\begin{aligned}
\mathscr{I} F_{\mathrm{S}}= & -\frac{\Delta M}{M}(3-E) C(0,0,0)+\frac{\Delta \gamma}{2 \gamma}\{7 C(0,0,0)-12 S(1,0,0) \\
& -4 C(1,1,0)-C(2,0,0)\}+\frac{\Delta \gamma}{2 \gamma} \frac{\Delta M}{M}(3-E)[-12 C(1,0,0) S(1,0,0) \\
& +C(0,0,0)\{4 S(1,1,0)+S(2,0,0)-S(0,0,0)\} \\
& +S(0,0,0)\{4 C(1,1,0)+C(2,0,0)-C(0,0,0)\}]
\end{aligned} \tag{36b}
$$

$$
\mathscr{R} F_{\mathrm{P}}=1+\frac{\Delta \gamma}{2 \gamma}\{S(0,0,0)+S(2,0,0)\} \tag{37a}
$$

$$
\mathscr{I} F_{\mathrm{P}}=\frac{\Delta \gamma}{2 \gamma}\{C(0,0,0)+C(2,0,0)\} \tag{37b}
$$

$$
\mathscr{R} F_{\mathrm{D}}=1+\frac{\Delta \gamma}{2 \gamma}\{S(0,0,0)+2 S(1,1,0)-S(2,0,0)\} \tag{38a}
$$

$$
\mathscr{I} F_{\mathrm{D}}=\frac{\Delta \gamma}{2 \gamma}\{C(0,0,0)+2 C(1,1,0)-C(2,0,0)\}. \tag{38b}
$$

With these one can study the resonance condition for given values of $\Delta M / M$ and $\Delta \gamma / \gamma$. In figure 1 the value of $E$ for resonance is plotted against $\Delta M / M$ for the S-wave scattering part, for various values of $\Delta \gamma / 2 \gamma$. In figure 2 the value of $E$ for resonance is plotted against $\Delta \gamma / 2 \gamma$ for the P- and D-wave scattering parts. If the sign of $\Delta \gamma / 2 \gamma$ is reversed in figure 2, the corresponding $E_{\mathrm{R}}$ simply reverses the sign having the magnitude intact.

## 6. The scattering cross section and its long wavelength limit

The total scattering cross section $\sigma_{\mathrm{T}}$ can be found by using the optical theorem

$\sigma_{\mathrm{T}}=(4 \pi / k) \mathscr{I}$(forward scattering amplitude). This theorem is completely general (Schiff 1954) and applies even to the scattering by non-central potentials.

The forward scattering amplitude found by using equations (34) applies to phonons polarized in one of the $x$, $y$ or $z$ directions. For such a phonon incident along one of the

![](./images/812432881908449283_1.jpg)

Figure 1. $E_{\mathrm{R}}$ is plotted against the parameter $\Delta M / M$ for the S-wave part.

![](./images/812432881908449283_2.jpg)

Figure 2. $E_{\mathrm{R}}$ is plotted against the parameter $\Delta \gamma / 2 \gamma$. Curve 1 is for the P-wave part and curve 2 is for the D-wave part. Identical curves exist for $\Delta \gamma / 2 \gamma$ positive but then $E_{\mathrm{R}}$ is negative.

crystallographic axes, $[1,0,0]$ say, $\mathbf{k}=(k, 0,0)$ and $\mathbf{k}_{0}=\left(k_{0}, 0,0\right)$ for the forward scattering amplitude, so that $g(\mathbf{k}_{0})=1 / 2 \gamma$. The scattering cross section in this case can be expressed in units of $a^{2}$, where $a$ is the lattice constant, as

$$
\begin{aligned}
\sigma_{\mathrm{T}}=\frac{1}{\gamma k} & {\left[\frac{1}{\left|F_{\mathrm{S}}\right|^{2}}\left\{\mathscr{I} D \mathscr{R} F_{\mathrm{S}}-\mathscr{R} D \mathscr{I} F_{\mathrm{S}}\right\}\right.} \\
& \left.+\frac{2 \Delta \gamma}{\left|F_{\mathrm{P}}\right|^{2}} \sin k \sin k_{0}\left(\mathscr{I} F_{\mathrm{P}}\right)-\frac{4 \Delta \gamma}{3\left|F_{\mathrm{D}}\right|^{2}}(\cos k-1)\left(\cos k_{0}-1\right) \mathscr{I} F_{\mathrm{D}}\right]
\end{aligned} \tag{39}
$$

where $\mathscr{R} F_{\mathrm{S}}, \mathscr{I} F_{\mathrm{S}}, \mathscr{I} F_{\mathrm{P}}$ and $\mathscr{I} F_{\mathrm{D}}$ are given by equations (36), (37) and (38), and

$$
\begin{aligned}
D=\Delta M \omega^{2} & -6 \Delta \gamma+\Delta M \omega^{2} \frac{\Delta \gamma}{2 \gamma}\{4 I(1,1,0)+I(2,0,0)+I(0,0,0)\} \\
& +2 \Delta \gamma\left\{1-\frac{\Delta M \omega^{2}}{2 \gamma} I(1,0,0)\right\}\left\{(2+\cos k)+\left(2+\cos k_{0}\right)\right\} \\
& -\frac{2}{3} \Delta \gamma\left\{1-\frac{\Delta M \omega^{2}}{2 \gamma} I(0,0,0)\right\}(2+\cos k)\left(2+\cos k_{0}\right).
\end{aligned} \tag{40}
$$

The real and imaginary parts of $D$ can be expressed in terms of $C(p, q, r)$ and $S(p, q, r)$ given by equations (35) and whose values are tabulated in the appendix.

In the special case when the substitutional impurity is an isotope $\Delta\gamma = 0$, so that $D = \Delta M\omega^{2}$ and $F_{\mathrm{S}} = 1-(\Delta M\omega^{2}/2\gamma)I(0,0,0)$, which leads to the result

$$
\sigma_{\mathrm{T}}=\frac{1}{\gamma k} \frac{(\Delta M)^{2}}{2 \gamma} \frac{\omega^{4}}{\left|F_{\mathrm{S}}\right|^{2}} \mathscr{I}\{I(0,0,0)\} \quad \text { in units of } a^{2}.
\tag{41}
$$

In the long wavelength limit

$$
\frac{1}{2 \gamma} \mathscr{I}\{I(0,0,0)\}=\frac{1}{2 \gamma} C(0,0,0)=\frac{k}{4 \pi \gamma}=\frac{k}{4 \pi M \omega_{0}^{2}}
\tag{42}
$$

where $\omega_{0}^{2}=\gamma / M$, and then equation (41) becomes

$$
\sigma_{\mathrm{T}}=\frac{1}{4 \pi}\left(\frac{\Delta M}{M}\right)^{2} \frac{\omega^{4}}{\omega_{0}^{4}} \frac{1}{\left|F_{\mathrm{S}}\right|^{2}} \text { in units of } a^{2}.
\tag{43}
$$

This is exactly the result obtained by Callaway (1963) and shows the Rayleigh type of scattering. The scattering is purely S-wave type.

In the general case the long wavelength limit of $\sigma_{\mathrm{T}}$ can be found by noting that in this limit, which also corresponds to the low frequency limit,

$$
\mathscr{I}\{I(p, q, r)\}=\frac{\omega}{2 \pi \omega_{0}}-\frac{\omega^{3}}{12 \pi \omega_{0}^{3}}\left(p^{2}+q^{2}+r^{2}\right)
\tag{44}
$$

up to the order of $\omega^{3}$. It follows that

$$
C(0,0,0)=\frac{\omega}{2 \pi \omega_{0}}
\tag{45a}
$$

$$
S(1,0,0)=\frac{\omega}{2 \pi \omega_{0}}-\frac{\omega^{3}}{12 \pi \omega_{0}^{3}}
\tag{45b}
$$

$$
C(1,1,0)=-\frac{\omega}{2 \pi \omega_{0}}+\frac{\omega^{3}}{6 \pi \omega_{0}^{3}}
\tag{45c}
$$

and

$$
C(2,0,0)=-\frac{\omega}{2 \pi \omega_{0}}+\frac{\omega^{3}}{3 \pi \omega_{0}^{3}}.
\tag{45d}
$$

In this long wavelength limit $\sigma_{\mathrm{T}}$ can be written as

$$
\begin{aligned}
\sigma_{\mathrm{T}}= & \frac{1}{\gamma k}\left\{\frac{1}{\left|F_{\mathrm{S}}\right|^{2}}\left(\mathscr{I} D \mathscr{R} F_{\mathrm{S}}-\mathscr{R} D \mathscr{I} F_{\mathrm{S}}\right)\right. \\
& \left.+\frac{2 \Delta \gamma}{\left|F_{\mathrm{P}}\right|^{2}} k k_{0}\left(\mathscr{I} F_{\mathrm{P}}\right)+\frac{\Delta \gamma}{3\left|F_{\mathrm{D}}\right|^{2}} k_{0}{ }^{2} k^{2}\left(-\mathscr{I} F_{\mathrm{D}}\right)\right\}
\end{aligned}
$$

where the quantity $D$ now becomes

$$
\begin{aligned}
D= & \Delta M \omega^{2}-\frac{\Delta \gamma}{6} k^{2} k_{0}{ }^{2}+\frac{\Delta \gamma \Delta M \omega^{2}}{2 \gamma}\{4 I(1,1,0)+I(2,0,0) \\
& +7 I(0,0,0)-12 I(1,0,0)\}+\frac{\Delta \gamma \Delta M \omega^{2}}{2 \gamma}\{I(1,0,0)-I(0,0,0)\}\left(k^{2}+k_{0}{ }^{2}\right).
\end{aligned}
\tag{47}
$$

Thus, in this limit, $\sigma_{\mathrm{T}}$ can be computed using equations (46) and (47), and it is found that the contribution from D-type waves is zero up to terms of the order of $\omega^{6}$. Retaining terms up to the order of $\omega^{4}$, which happens to be the lowest order in $\omega$ for which the cross section is non-zero, the total scattering cross section contributed by S- and P-type waves is given by

$$
\begin{aligned}
\sigma_{\mathrm{T}}= & \frac{1}{4 \pi}\left(\frac{\Delta M}{M}\right)^{2} \frac{\omega^{4}}{\omega_{0}{ }^{4}} \frac{1}{\left|F_{\mathrm{S}}\right|^{2}}\left\{1+b_{1}\left(\frac{\Delta \gamma}{\gamma}\right)+b_{2}\left(\frac{\Delta \gamma}{\gamma}\right)^{2}\right\} \\
& +\frac{1}{3 \pi}\left(\frac{\Delta \gamma}{\gamma}\right)^{2} \frac{\omega^{4}}{\omega_{0}{ }^{4}} \frac{1}{\left|F_{\mathrm{P}}\right|^{2}} \text { in units of } a^{2}
\end{aligned}
$$

where the numerical constants $b_{1}$ and $b_{2}$ are found to have the values
$$b_{1}=2 \cdot 292, \quad b_{2}=1 \cdot 298.$$

These results show that in the long wavelength limit the scattering cross section is proportional to $\omega^{4}$, showing Rayleigh type scattering for the cases when changes in the mass or the force constant or both are involved. For the general case involving both the mass and the force constant changes, the scattering cross section is contributed by both the S- and P-type waves, and for the case of change in force constant only (isobar case) the scattering is purely P-wave type. However, in the general case the change in force constant affects the scattering by S-type waves, whereas the change in mass does not affect the scattering by P-type waves in the long wavelength limit.

The relaxation time $\tau_{\mathrm{D}}$ for scattering by defect, following Callaway (1963), can be shown to be given by

$$
\begin{aligned}
\tau_{\mathrm{D}}{ }^{-1}=\frac{\omega^{4} a^{3} c(1-c)}{v^{3}}[ & \frac{1}{4 \pi}\left(\frac{\Delta M}{M}\right)^{2}\left\{1+b_{1}\left(\frac{\Delta \gamma}{\gamma}\right)+b_{2}\left(\frac{\Delta \gamma}{\gamma}\right)^{2}\right\} \frac{1}{\left|F_{\mathrm{S}}\right|^{2}} \\
& \left.+\frac{1}{3 \pi}\left(\frac{\Delta \gamma}{\gamma}\right)^{2} \frac{1}{\left|F_{\mathrm{P}}\right|^{2}}\right]
\end{aligned}
$$

where $c$ is the concentration of the type of defect under consideration and $v$ is the velocity of sound. This result is the general case involving both $\Delta M$ and $\Delta \gamma$. It leads to the possibility of defining two 'defect scattering parameters' $A_{\mathrm{S}}$ and $A_{\mathrm{P}}$, such that equation (49) can be put in the form

$$
\tau_{\mathrm{D}}{ }^{-1}=\omega^{4}\left(\frac{A_{\mathrm{S}}}{\left|F_{\mathrm{S}}\right|^{2}}+\frac{A_{\mathrm{P}}}{\left|F_{\mathrm{P}}\right|^{2}}\right).
$$

Here the quantity $A_{\mathrm{S}}$ is obtained if one multiplies the defect scattering parameter $A$ of Callaway by a factor $1+b_{1}(\Delta \gamma / \gamma)+b_{2}(\Delta \gamma / \gamma)^{2}$. The denominators in equation (50) can be evaluated by using equations (36), (37), (44) and (45), together with the result given in the appendix.

## Acknowledgments

This research is supported by the U.S. National Bureau of Standards through a research contract. The authors are indebted to Professor I. N. Rabinowitz of the IIT Computer Center for advice on the computational aspects of the problem.

## Appendix

The Green functions for a simple cubic lattice with nearest-neighbour interactions can be expressed in terms of the integrals $C(p, q, r)$ and $S(p, q, r)$ defined in equation (35). We have evaluated $C(0, 0, 0), S(0, 0, 0), C(1, 0, 0), S(1, 0, 0), C(1, 1, 0), S(1, 1, 0), C(2, 0, 0)$ and $S(2, 0, 0)$ by numerical integration on the IBM 1620 computer, and the results are given in the table. Simpson's rule with an interval of 0·01 has been used and the upper limit is taken at 50. The estimated error is within five per cent.

### Table of integrals

<table>
  <tr>
    <th>E</th>
    <th>S(000)</th>
    <th>C(000)</th>
    <th>C(100)</th>
    <th>S(100)</th>
    <th>S(110)</th>
    <th>C(110)</th>
    <th>S(200)</th>
    <th>C(200)</th>
  </tr>
  <tr>
    <td>0·0000</td>
    <td>0·0000</td>
    <td>0·8954</td>
    <td>0 3365</td>
    <td>0·0000</td>
    <td>0·0000</td>
    <td>0·1887</td>
    <td>0·0000</td>
    <td>0 1575</td>
  </tr>
  <tr>
    <td>0·1000</td>
    <td>0·0377</td>
    <td>0·8963</td>
    <td>0·3353</td>
    <td>0 0299</td>
    <td>0 0186</td>
    <td>0·1883</td>
    <td>0·0288</td>
    <td>0 1537</td>
  </tr>
  <tr>
    <td>0·2000</td>
    <td>0·0746</td>
    <td>0·8977</td>
    <td>0·3317</td>
    <td>0·0598</td>
    <td>0·0368</td>
    <td>0·1866</td>
    <td>0·0580</td>
    <td>0 1432</td>
  </tr>
  <tr>
    <td>0·3000</td>
    <td>0·1117</td>
    <td>0 8982</td>
    <td>0 3255</td>
    <td>0·0897</td>
    <td>0·0548</td>
    <td>0·1831</td>
    <td>0·0859</td>
    <td>0 1279</td>
  </tr>
  <tr>
    <td>0·4000</td>
    <td>0·1516</td>
    <td>0·8977</td>
    <td>0 3163</td>
    <td>0 1196</td>
    <td>0·0732</td>
    <td>0 1778</td>
    <td>0·1095</td>
    <td>0 1074</td>
  </tr>
  <tr>
    <td>0·5000</td>
    <td>0·1957</td>
    <td>0·8982</td>
    <td>0 3039</td>
    <td>0 1497</td>
    <td>0·0923</td>
    <td>0 1714</td>
    <td>0·1269</td>
    <td>0 0799</td>
  </tr>
  <tr>
    <td>0·6000</td>
    <td>0·2433</td>
    <td>0·9010</td>
    <td>0·2879</td>
    <td>0·1802</td>
    <td>0 1115</td>
    <td>0·1643</td>
    <td>0·1380</td>
    <td>0 0441</td>
  </tr>
  <tr>
    <td>0·7000</td>
    <td>0·2944</td>
    <td>0·9044</td>
    <td>0 2680</td>
    <td>0 2110</td>
    <td>0·1306</td>
    <td>0·1558</td>
    <td>0·1420</td>
    <td>0 0016</td>
  </tr>
  <tr>
    <td>0·8000</td>
    <td>0·3535</td>
    <td>0·9056</td>
    <td>0·2424</td>
    <td>0 2414</td>
    <td>0·1507</td>
    <td>0·1450</td>
    <td>0·1333</td>
    <td>−0 0446</td>
  </tr>
  <tr>
    <td>0·9000</td>
    <td>0·4338</td>
    <td>0·9030</td>
    <td>0·2064</td>
    <td>0·2708</td>
    <td>0·1756</td>
    <td>0·1314</td>
    <td>0 0972</td>
    <td>−0 0933</td>
  </tr>
  <tr>
    <td>1·0000</td>
    <td>0·6046</td>
    <td>0·8708</td>
    <td>0·1350</td>
    <td>0 2902</td>
    <td>0 2267</td>
    <td>0·1064</td>
    <td>−0·0390</td>
    <td>−0 1184</td>
  </tr>
  <tr>
    <td>1·1000</td>
    <td>0·6297</td>
    <td>0·6965</td>
    <td>0·1057</td>
    <td>0·2554</td>
    <td>0·2241</td>
    <td>0·0373</td>
    <td>−0·0420</td>
    <td>0 0019</td>
  </tr>
  <tr>
    <td>1·2000</td>
    <td>0·6250</td>
    <td>0·6153</td>
    <td>0·0866</td>
    <td>0 2461</td>
    <td>0·2109</td>
    <td>0·0019</td>
    <td>−0·0188</td>
    <td>0 0328</td>
  </tr>
  <tr>
    <td>1·3000</td>
    <td>0·6167</td>
    <td>0·5567</td>
    <td>0·0694</td>
    <td>0·2412</td>
    <td>0·1961</td>
    <td>0·0241</td>
    <td>0·0045</td>
    <td>0 0425</td>
  </tr>
  <tr>
    <td>1·4000</td>
    <td>0·6066</td>
    <td>0·5077</td>
    <td>0·0534</td>
    <td>0 2368</td>
    <td>0·1803</td>
    <td>0 0456</td>
    <td>0·0263</td>
    <td>0 0438</td>
  </tr>
  <tr>
    <td>1·5000</td>
    <td>0·5974</td>
    <td>0·4638</td>
    <td>0·0378</td>
    <td>0 2319</td>
    <td>0·1642</td>
    <td>0·0639</td>
    <td>0·0439</td>
    <td>0 0409</td>
  </tr>
  <tr>
    <td>1·6000</td>
    <td>0·5900</td>
    <td>0·4249</td>
    <td>0·0219</td>
    <td>0 2266</td>
    <td>0·1481</td>
    <td>0 0794</td>
    <td>0 0565</td>
    <td>0 0340</td>
  </tr>
  <tr>
    <td>1·7000</td>
    <td>0·5835</td>
    <td>0·3909</td>
    <td>0·0060</td>
    <td>0·2215</td>
    <td>0·1318</td>
    <td>0 0923</td>
    <td>0 0651</td>
    <td>0 0231</td>
  </tr>
  <tr>
    <td>1·8000</td>
    <td>0·5764</td>
    <td>0·3605</td>
    <td>−0·0091</td>
    <td>0·2162</td>
    <td>0·1151</td>
    <td>0·1028</td>
    <td>0·0714</td>
    <td>0 0096</td>
  </tr>
  <tr>
    <td>1·9000</td>
    <td>0·5687</td>
    <td>0·3318</td>
    <td>−0 0235</td>
    <td>0·2101</td>
    <td>0·0979</td>
    <td>0·1113</td>
    <td>0·0752</td>
    <td>−0 0042</td>
  </tr>
  <tr>
    <td>2·0000</td>
    <td>0·5615</td>
    <td>0·3039</td>
    <td>−0 0377</td>
    <td>0 2026</td>
    <td>0·0803</td>
    <td>0 1179</td>
    <td>0·0755</td>
    <td>−0 0176</td>
  </tr>
  <tr>
    <td>2·1000</td>
    <td>0·5554</td>
    <td>0·2776</td>
    <td>−0·0521</td>
    <td>0·1943</td>
    <td>0·0624</td>
    <td>0·1228</td>
    <td>0 0719</td>
    <td>−0 0309</td>
  </tr>
  <tr>
    <td>2·2000</td>
    <td>0·5497</td>
    <td>0·2531</td>
    <td>−0 0664</td>
    <td>0·1856</td>
    <td>0·0443</td>
    <td>0·1257</td>
    <td>0 0650</td>
    <td>−0 0445</td>
  </tr>
  <tr>
    <td>2·3000</td>
    <td>0·5435</td>
    <td>0·2297</td>
    <td>−0·0800</td>
    <td>0 1761</td>
    <td>0·0261</td>
    <td>0·1266</td>
    <td>0 0560</td>
    <td>−0 0574</td>
  </tr>
  <tr>
    <td>2·4000</td>
    <td>0·5369</td>
    <td>0·2062</td>
    <td>−0·0929</td>
    <td>0·1649</td>
    <td>0·0075</td>
    <td>0 1251</td>
    <td>0·0446</td>
    <td>−0 0679</td>
  </tr>
  <tr>
    <td>2·5000</td>
    <td>0·5310</td>
    <td>0·1820</td>
    <td>−0·1058</td>
    <td>0 1517</td>
    <td>−0·0113</td>
    <td>0·1210</td>
    <td>0·0299</td>
    <td>−0 0754</td>
  </tr>
  <tr>
    <td>2·6000</td>
    <td>0·5261</td>
    <td>0·1576</td>
    <td>−0·1192</td>
    <td>0·1367</td>
    <td>−0·0309</td>
    <td>0·1141</td>
    <td>0 0116</td>
    <td>−0 0800</td>
  </tr>
  <tr>
    <td>2·7000</td>
    <td>0·5214</td>
    <td>0·1332</td>
    <td>−0·1326</td>
    <td>0 1198</td>
    <td>−0·0507</td>
    <td>0 1041</td>
    <td>−0 0095</td>
    <td>−0 0813</td>
  </tr>
  <tr>
    <td>2·8000</td>
    <td>0·5159</td>
    <td>0·1069</td>
    <td>−0·1448</td>
    <td>0·0997</td>
    <td>−0·0702</td>
    <td>0·0895</td>
    <td>−0 0322</td>
    <td>−0 0770</td>
  </tr>
  <tr>
    <td>2·9000</td>
    <td>0·5090</td>
    <td>0·0743</td>
    <td>−0·1555</td>
    <td>0 0718</td>
    <td>−0·0889</td>
    <td>0·0659</td>
    <td>−0 0561</td>
    <td>−0 0615</td>
  </tr>
  <tr>
    <td>3·0000</td>
    <td>0·4926</td>
    <td>0·0000</td>
    <td>−0·1559</td>
    <td>0 0000</td>
    <td>−0·0977</td>
    <td>0·0000</td>
    <td>−0 0727</td>
    <td>−0 0000</td>
  </tr>
  <tr>
    <td>3·1000</td>
    <td>0·4300</td>
    <td>0·0000</td>
    <td>−0·1076</td>
    <td>0·0000</td>
    <td>−0·0556</td>
    <td>0·0000</td>
    <td>−0·0364</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·2000</td>
    <td>0·3994</td>
    <td>−0·0000</td>
    <td>−0·0893</td>
    <td>0 0000</td>
    <td>−0·0418</td>
    <td>0·0000</td>
    <td>−0·0262</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·3000</td>
    <td>0·3768</td>
    <td>−0·0000</td>
    <td>−0·0778</td>
    <td>0 0000</td>
    <td>−0·0342</td>
    <td>0·0000</td>
    <td>−0 0210</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·4000</td>
    <td>0·3578</td>
    <td>0·0000</td>
    <td>−0·0689</td>
    <td>0 0000</td>
    <td>−0·0289</td>
    <td>0·0000</td>
    <td>−0 0172</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·5000</td>
    <td>0·3410</td>
    <td>0 0000</td>
    <td>−0·0613</td>
    <td>0 0000</td>
    <td>−0·0244</td>
    <td>0·0000</td>
    <td>−0·0141</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·6000</td>
    <td>0·3264</td>
    <td>0·0000</td>
    <td>−0·0550</td>
    <td>0 0000</td>
    <td>−0·0206</td>
    <td>0·0000</td>
    <td>−0·0117</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·7000</td>
    <td>0·3136</td>
    <td>0·0000</td>
    <td>−0·0501</td>
    <td>0·0000</td>
    <td>−0·0178</td>
    <td>0·0000</td>
    <td>−0 0102</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·8000</td>
    <td>0·3022</td>
    <td>0·0000</td>
    <td>−0·0461</td>
    <td>0 0000</td>
    <td>−0·0160</td>
    <td>0·0000</td>
    <td>−0·0090</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>3·9000</td>
    <td>0·2916</td>
    <td>0·0000</td>
    <td>−0·0425</td>
    <td>0 0000</td>
    <td>−0·0145</td>
    <td>0·0000</td>
    <td>−0 0079</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>4·0000</td>
    <td>0·2818</td>
    <td>0·0000</td>
    <td>−0·0391</td>
    <td>0·0000</td>
    <td>−0·0128</td>
    <td>0·0000</td>
    <td>−0 0069</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>4·1000</td>
    <td>0·2728</td>
    <td>0·0000</td>
    <td>−0·0361</td>
    <td>0 0000</td>
    <td>−0·0113</td>
    <td>0·0000</td>
    <td>−0·0061</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>4·2000</td>
    <td>0·2645</td>
    <td>0·0000</td>
    <td>−0·0337</td>
    <td>0·0000</td>
    <td>−0·0101</td>
    <td>0·0000</td>
    <td>−0·0056</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>4·3000</td>
    <td>0·2569</td>
    <td>0·0000</td>
    <td>−0 0315</td>
    <td>0 0000</td>
    <td>−0·0094</td>
    <td>0·0000</td>
    <td>−0 0051</td>
    <td>0 0000</td>
  </tr>
  <tr>
    <td>4·4000</td>
    <td>0·2496</td>
    <td>0·0000</td>
    <td>−0·0295</td>
    <td>0 0000</td>
    <td>−0 0087</td>
    <td>0 0000</td>
    <td>−0·0046</td>
    <td>0 0000</td>
  </tr>
</table>

### Table of integrals (cont.)

<table>
  <thead>
    <tr>
      <th>E</th>
      <th>S(000)</th>
      <th>C(000)</th>
      <th>C(100)</th>
      <th>S(100)</th>
      <th>S(110)</th>
      <th>C(110)</th>
      <th>S(200)</th>
      <th>C(200)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4·5000</td>
      <td>0·2428</td>
      <td>0 0000</td>
      <td>−0·0275</td>
      <td>0·0000</td>
      <td>−0·0079</td>
      <td>0·0000</td>
      <td>−0·0041</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>4·6000</td>
      <td>0 2364</td>
      <td>0·0000</td>
      <td>−0·0258</td>
      <td>0·0000</td>
      <td>−0·0070</td>
      <td>0·0000</td>
      <td>−0·0038</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>4·7000</td>
      <td>0·2304</td>
      <td>0 0000</td>
      <td>−0 0243</td>
      <td>0·0000</td>
      <td>−0·0065</td>
      <td>0·0000</td>
      <td>−0·0035</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>4·8000</td>
      <td>0·2248</td>
      <td>0 0000</td>
      <td>−0·0230</td>
      <td>0·0000</td>
      <td>−0·0061</td>
      <td>0·0000</td>
      <td>−0·0032</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>4·9000</td>
      <td>0·2193</td>
      <td>0·0000</td>
      <td>−0·0217</td>
      <td>0·0000</td>
      <td>−0·0058</td>
      <td>0·0000</td>
      <td>−0·0029</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·0000</td>
      <td>0 2142</td>
      <td>0·0000</td>
      <td>−0·0204</td>
      <td>0·0000</td>
      <td>−0·0053</td>
      <td>0·0000</td>
      <td>−0·0027</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·1000</td>
      <td>0 2094</td>
      <td>0·0000</td>
      <td>−0·0192</td>
      <td>0·0000</td>
      <td>−0·0047</td>
      <td>0·0000</td>
      <td>−0·0025</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·2000</td>
      <td>0·2048</td>
      <td>0·0000</td>
      <td>−0·0183</td>
      <td>0·0000</td>
      <td>−0·0044</td>
      <td>0·0000</td>
      <td>−0·0024</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·3000</td>
      <td>0·2004</td>
      <td>0·0000</td>
      <td>−0 0174</td>
      <td>0·0000</td>
      <td>−0·0043</td>
      <td>0·0000</td>
      <td>−0·0022</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·4000</td>
      <td>0·1961</td>
      <td>0·0000</td>
      <td>−0·0165</td>
      <td>0·0000</td>
      <td>−0·0041</td>
      <td>0·0000</td>
      <td>−0·0020</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·5000</td>
      <td>0·1921</td>
      <td>0·0000</td>
      <td>−0·0156</td>
      <td>0·0000</td>
      <td>−0·0037</td>
      <td>0·0000</td>
      <td>−0·0019</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·6000</td>
      <td>0·1883</td>
      <td>0·0000</td>
      <td>−0·0148</td>
      <td>0·0000</td>
      <td>−0·0034</td>
      <td>0·0000</td>
      <td>−0·0018</td>
      <td>0 0000</td>
    </tr>
    <tr>
      <td>5·7000</td>
      <td>0·1846</td>
      <td>0·0000</td>
      <td>−0·0141</td>
      <td>0·0000</td>
      <td>−0·0032</td>
      <td>0·0000</td>
      <td>−0·0017</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·8000</td>
      <td>0·1811</td>
      <td>0·0000</td>
      <td>−0·0135</td>
      <td>0·0000</td>
      <td>−0·0031</td>
      <td>0·0000</td>
      <td>−0·0016</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>5·9000</td>
      <td>0·1776</td>
      <td>0·0000</td>
      <td>−0·0128</td>
      <td>0·0000</td>
      <td>−0·0030</td>
      <td>0·0000</td>
      <td>−0·0014</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6 0000</td>
      <td>0·1744</td>
      <td>0·0000</td>
      <td>−0·0121</td>
      <td>0·0000</td>
      <td>−0·0027</td>
      <td>0·0000</td>
      <td>−0·0014</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·1000</td>
      <td>0 1713</td>
      <td>0·0000</td>
      <td>−0·0116</td>
      <td>0·0000</td>
      <td>−0·0025</td>
      <td>0·0000</td>
      <td>−0·0013</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·2000</td>
      <td>0·1683</td>
      <td>0·0000</td>
      <td>−0·0111</td>
      <td>0·0000</td>
      <td>−0·0024</td>
      <td>0·0000</td>
      <td>−0·0013</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6 3000</td>
      <td>0·1653</td>
      <td>0·0000</td>
      <td>−0·0106</td>
      <td>0·0000</td>
      <td>−0·0024</td>
      <td>0·0000</td>
      <td>−0·0012</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·4000</td>
      <td>0·1625</td>
      <td>0·0000</td>
      <td>−0·0101</td>
      <td>0·0000</td>
      <td>−0·0023</td>
      <td>0·0000</td>
      <td>−0·0011</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·5000</td>
      <td>0·1598</td>
      <td>0·0000</td>
      <td>−0·0096</td>
      <td>0·0000</td>
      <td>−0·0021</td>
      <td>0·0000</td>
      <td>−0·0010</td>
      <td>0 0000</td>
    </tr>
    <tr>
      <td>6·6000</td>
      <td>0·1572</td>
      <td>0·0000</td>
      <td>−0·0092</td>
      <td>0 0000</td>
      <td>−0·0019</td>
      <td>0·0000</td>
      <td>−0·0010</td>
      <td>0 0000</td>
    </tr>
    <tr>
      <td>6·7000</td>
      <td>0·1547</td>
      <td>0·0000</td>
      <td>−0 0088</td>
      <td>0·0000</td>
      <td>−0·0018</td>
      <td>0·0000</td>
      <td>−0·0009</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·8000</td>
      <td>0 1522</td>
      <td>0·0000</td>
      <td>−0·0085</td>
      <td>0·0000</td>
      <td>−0·0018</td>
      <td>0·0000</td>
      <td>−0·0009</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>6·9000</td>
      <td>0·1498</td>
      <td>0·0000</td>
      <td>−0·0080</td>
      <td>0·0000</td>
      <td>−0·0018</td>
      <td>0·0000</td>
      <td>−0·0008</td>
      <td>0·0000</td>
    </tr>
    <tr>
      <td>7 0000</td>
      <td>0 1475</td>
      <td>0·0000</td>
      <td>−0·0076</td>
      <td>0·0000</td>
      <td>−0·0016</td>
      <td>0·0000</td>
      <td>−0 0008</td>
      <td>0·0000</td>
    </tr>
  </tbody>
</table>

The range of the parameter $E$ extends from 0 to 7, and the integrals are evaluated at intervals of 0·1. The table is thus more exhaustive than the one given by Wolfram and Callaway (1963), and corrects an error in their value of $C(1, 1, 0)$ at $E = 3\cdot0$.

### References

CALLAWAY, J., 1963, *Nuovo Cim.*, **29**, 883-91.
—— 1964, *J. Math. Phys.*, **5**, 783-98.
KOSTER, G. F., and SLATER, J. C., 1954, *Phys. Rev.*, **96**, 1208-23.
LIFSHITZ, I. M., 1956, *Nuovo Cim. (Suppl. No. 4)*, **3**, 716-34.
MONTROLL, E. W., and POTTS, R. B., 1955, *Phys. Rev.*, **100**, 525-43.
SCHIFF, L. I., 1954, *Progr. Theor. Phys., Japan*, **11**, 288-90.
TAKENO, S., 1963, *Progr. Theor. Phys., Japan*, **29**, 191-205.
WAGNER, M., 1964, *Phys. Rev.*, **133**, A750-8.
WALKER, C. T., and POHL, R. O., 1963, *Phys. Rev.*, **131**, 1433-42.
WOLFRAM, T., and CALLAWAY, J., 1963, *Phys. Rev.*, **130**, 2207-17.