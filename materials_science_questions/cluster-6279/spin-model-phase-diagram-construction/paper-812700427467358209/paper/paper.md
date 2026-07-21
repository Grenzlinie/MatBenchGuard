# Phase diagram and critical properties of the (1+1)-dimensional Ashkin-Teller model

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1984 J. Phys. A: Math. Gen. 17 1531

(http://iopscience.iop.org/0305-4470/17/7/021)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 134.99.128.41
This content was downloaded on 22/12/2013 at 17:23

Please note that [terms and conditions apply].

J. Phys. A: Math. Gen. 17 (1984) 1531-1545. Printed in Great Britain

# Phase diagram and critical properties of the (1+1)-dimensional Ashkin-Teller model

F Iglói and J Sólyom

Central Research Institute for Physics, H-1525 Budapest, POB 49, Hungary

Received 28 September 1983

Abstract. The (1+1)-dimensional Ashkin-Teller model is studied by the renormalisation group method and by the finite lattice extrapolation technique. The possible phases and their boundaries in an extended space of couplings are determined from the degeneracy structure of the low-lying levels in the thermodynamic limit. The critical behaviour is investigated for ferromagnetic couplings using increasing block sizes in the renormalisation transformation. The line of fixed points and its bifurcation at the Potts fixed point is studied.

## 1. Introduction

Recently we have witnessed a growing interest in the study of the Hamiltonian version of two-dimensional (2D) lattice spin models. By taking the time-continuum limit the classical 2D models can be mapped onto one-dimensional (1D) quantum problems, where external fields are introduced, and the strength of these fields plays the role of the temperature (for a review see Kogut 1979). The reason for dealing with the Hamiltonian version of the models is that approximate treatments are sometimes easier in 1D and in most cases the anisotropy in the 2D models is irrelevant for the critical properties. For example the 2D Ising model is equivalent to the 1D Ising model in a transverse field for any value of the couplings. On the other hand the 2D Potts model is equivalent to its Hamiltonian version only in the self-dual point (Stephen and Mittag 1972), but the critical properties of the two models are the same. For several models, however, there is no rigorous justification of such an equivalence. Moreover in the anisotropic limit the signs of the different couplings can be changed separately and the Hamiltonian version can have a complicated phase structure. In these cases it is interesting to investigate the 1D models for their own sake.

One of the most interesting of these models is the Ashkin-Teller model. The 2D classical model has several conjectured and exact relations for its rather rich phase structure (line of continuously varying critical indices, bifurcation point in the phase diagram, lines of Ising critical behaviour) (Knops 1975, Kadanoff 1977). The Hamiltonian version shows the same behaviour for appropriately chosen couplings and, in addition to that, has an even richer phase structure for antiferromagnetic couplings. As was shown by Kohmoto et al (1981), there exists on the antiferromagnetic side a surface of critical behaviour, the border of which consists of lines of Kosterlitz-Thouless transition points, and a line of first-order transition points. This phase diagram was

0305-4470/84/071531+15$02.25 © 1984 The Institute of Physics 1531

obtained from mapping the Ashkin-Teller model onto the exactly soluble six-vertex model for special values of the couplings and by studying the effect of different operators that appear as perturbation. The results were also confirmed by high-temperature series expansion, although, especially near the bifurcation point, the series estimates differ somewhat from the conjectured values.

In this paper the renormalisation group technique and the finite size extrapolation method will be applied to a more general Hamiltonian version of the Ashkin-Teller model to determine the boundaries of the phases numerically, and the type of critical behaviour.

In the renormalisation group technique a self-dual transformation is applied to obtain the phase diagram for ferromagnetic couplings. The phase structure is similar to that of the restricted model studied by Kohmoto *et al* (1981). The critical behaviour is studied by this transformation and by non-dual block transformation by increasing the number of spins in a block. The calculated critical properties show slow convergence to the conjectured values.

Better results are obtained in the finite size extrapolation method, where the energy of the ground state and the first excited states of rings (up to six spins per ring) were determined. From these data the phase diagram and the value of the correlation length exponent could be calculated to quite a good accuracy. At the bifurcation point of the phase diagram, where the model is equivalent to the four-state Potts model, the finite lattice extrapolation predicts a value for the exponent $\nu$ much closer to the conjectured value than other extrapolation procedures, since we use information from an extended space of couplings. Along the line of continuously varying critical indices, the error of the extrapolation is small for $-0.6 \leqslant \lambda_2/\lambda_1 \leqslant 0.6$ and the critical indices are very close to the conjectured ones. In the antiferromagnetic region the extrapolation procedure gives further evidence for the existence of a 'critical fan'.

The content of the paper is as follows. In $\S 2$ the formulation of the Hamiltonian version of the Ashkin-Teller model is given and the structure of the low-lying levels which are relevant both in the renormalisation group (RG) transformation and the finite size scaling method is discussed. In $\S \S 3$ and 4 the results of the RG transformation and the finite lattice extrapolation are presented, respectively. Finally, $\S 5$ contains a short discussion.

### 2. Formalism

First the Hamiltonian version of the Ashkin-Teller model is presented. In the classical Ashkin-Teller model the system can be at any lattice site in any of the four possible states, denoted by $|1\rangle$, $|2\rangle$, $|3\rangle$ and $|4\rangle$. The energy of the system depends on the nearest-neighbour configuration. The interaction energy between neighbouring spins is $-\frac{1}{2}\lambda_1$ for the $|11\rangle$, $|22\rangle$, $|33\rangle$ and the $|44\rangle$ configurations, $\frac{1}{2}\lambda_1$ for the $|13\rangle$ and $|24\rangle$ configurations, while it is $\frac{1}{2}\lambda_2$ for the $|12\rangle$, $|23\rangle$, $|34\rangle$ and the $|41\rangle$ configurations. In what follows in this section all energies will be shifted by $-\frac{1}{4}\lambda_2$ in order to simplify some of the formulae.

In the anisotropic model the couplings are different in the horizontal and vertical directions. Denoting these two directions by $x$ and $\tau$, the couplings are $\lambda_1^x$, $\lambda_2^x$, $\lambda_1^\tau$ and $\lambda_2^\tau$. The Hamiltonian version is obtained from the time-continuum limit, when the lattice spacing in the $\tau$ direction goes to zero, while at the same time the couplings $\lambda_1^\tau$ and $\lambda_2^\tau$ go to infinity. The Hamiltonian, which is the transfer matrix in this limit,

will contain spin flip terms, in addition to the usual classical energy term. The Hamil- tonian can be written (Sólyom 1981) in the form

$$
H=H_{\lambda}+H_{h}
\tag{2.1}
$$

where $H_{\lambda}$ is the classical energy which depends on the neighbouring configurations, while the transverse field term, which flips the spins, can be characterised by two couplings $h_{1}$ and $h_{2}$ and is given by the relations

$$
\begin{aligned}
&H_{h}|1\rangle=-h_{1}|2\rangle-h_{2}|3\rangle-h_{1}|4\rangle \\
&H_{h}|2\rangle=-h_{1}|1\rangle-h_{1}|3\rangle-h_{2}|4\rangle \\
&H_{h}|3\rangle=-h_{2}|1\rangle-h_{1}|2\rangle-h_{1}|4\rangle \\
&H_{h}|4\rangle=-h_{1}|1\rangle-h_{2}|2\rangle-h_{1}|3\rangle.
\end{aligned}
\tag{2.2}
$$

In the Ising spin representation the Hamiltonian has the form

$$
H_{\lambda}=-\frac{1}{4} \lambda_{1} \sum_{j}\left(\sigma_{j}^{z} \sigma_{j+1}^{z}+\tau_{j}^{z} \tau_{j+1}^{z}\right)-\frac{1}{4} \lambda_{2} \sum_{j} \sigma_{j}^{z} \sigma_{j+1}^{z} \tau_{j}^{z} \tau_{j+1}^{z}
\tag{2.3}
$$

and

$$
H_{h}=-h_{1} \sum_{j}\left(\sigma_{j}^{x}+\tau_{j}^{x}\right)-h_{2} \sum_{j} \sigma_{j}^{x} \tau_{j}^{x}.
\tag{2.4}
$$

The states $|1\rangle,|2\rangle,|3\rangle$ and $|4\rangle$ correspond to $\sigma^{z}=1, \tau^{z}=1 ; \sigma^{z}=1, \tau^{z}=-1 ; \sigma^{z}=-1$, $\tau^{z}=-1$ and $\sigma^{z}=-1, \tau^{z}=1$ respectively.

Sometimes it is more convenient to use the following linear combinations of the states:

$$
\begin{aligned}
&\left|1^{\prime}\right\rangle=\frac{1}{2}(|1\rangle+|2\rangle+|3\rangle+|4\rangle) \\
&\left|2^{\prime}\right\rangle=\frac{1}{2}(|1\rangle+\mathrm{i}|2\rangle-|3\rangle-\mathrm{i}|4\rangle) \\
&\left|3^{\prime}\right\rangle=\frac{1}{2}(|1\rangle-|2\rangle+|3\rangle-|4\rangle) \\
&\left|4^{\prime}\right\rangle=\frac{1}{2}(|1\rangle-\mathrm{i}|2\rangle-|3\rangle+\mathrm{i}|4\rangle)
\end{aligned}
\tag{2.5}
$$

which are eigenstates of $H_{h}$:

$$
\begin{array}{ll}
H_{h}\left|1^{\prime}\right\rangle=-\left(2 h_{1}+h_{2}\right)\left|1^{\prime}\right\rangle, & H_{h}\left|2^{\prime}\right\rangle=h_{2}\left|2^{\prime}\right\rangle \\
H_{h}\left|3^{\prime}\right\rangle=\left(2 h_{1}-h_{2}\right)\left|3^{\prime}\right\rangle, & H_{h}\left|4^{\prime}\right\rangle=h_{2}\left|4^{\prime}\right\rangle.
\end{array}
\tag{2.6}
$$

In this representation the Ashkin-Teller coupling part will flip the neighbouring spins, e.g.:

$$
\begin{aligned}
&H_{\lambda}\left|1^{\prime} 1^{\prime}\right\rangle=-\frac{1}{4} \lambda_{1}\left|2^{\prime} 4^{\prime}\right\rangle-\frac{1}{4} \lambda_{2}\left|3^{\prime} 3^{\prime}\right\rangle-\frac{1}{4} \lambda_{1}\left|4^{\prime} 2^{\prime}\right\rangle \\
&H_{\lambda}\left|2^{\prime} 4^{\prime}\right\rangle=-\frac{1}{4} \lambda_{1}\left|1^{\prime} 1^{\prime}\right\rangle-\frac{1}{4} \lambda_{1}\left|3^{\prime} 3^{\prime}\right\rangle-\frac{1}{4} \lambda_{2}\left|4^{\prime} 2^{\prime}\right\rangle \\
&H_{\lambda}\left|3^{\prime} 3^{\prime}\right\rangle=-\frac{1}{4} \lambda_{2}\left|1^{\prime} 1^{\prime}\right\rangle-\frac{1}{4} \lambda_{1}\left|2^{\prime} 4^{\prime}\right\rangle-\frac{1}{4} \lambda_{1}\left|4^{\prime} 2^{\prime}\right\rangle \\
&H_{\lambda}\left|4^{\prime} 2^{\prime}\right\rangle=-\frac{1}{4} \lambda_{1}\left|1^{\prime} 1^{\prime}\right\rangle-\frac{1}{4} \lambda_{2}\left|2^{\prime} 4^{\prime}\right\rangle-\frac{1}{4} \lambda_{1}\left|3^{\prime} 3^{\prime}\right\rangle.
\end{aligned}
\tag{2.7}
$$

Similar relations hold for the states $\left|1^{\prime} 2^{\prime}\right\rangle,\left|2^{\prime} 1^{\prime}\right\rangle,\left|3^{\prime} 4^{\prime}\right\rangle$ and $\left|4^{\prime} 3^{\prime}\right\rangle$, for $\left|1^{\prime} 3^{\prime}\right\rangle,\left|2^{\prime} 2^{\prime}\right\rangle$, $\left|3^{\prime} 1^{\prime}\right\rangle$ and $\left|4^{\prime} 4^{\prime}\right\rangle$ as well as for $\left|1^{\prime} 4^{\prime}\right\rangle,\left|2^{\prime} 3^{\prime}\right\rangle,\left|3^{\prime} 2^{\prime}\right\rangle$ and $\left|4^{\prime} 1^{\prime}\right\rangle$.

A different representation of the Hamiltonian uses the angles $\theta_{i}=0, \frac{1}{2} \pi, \pi, \frac{3}{2} \pi$ for the states $|1\rangle,|2\rangle,|3\rangle$ and $|4\rangle$ respectively. The spin flip terms are given in terms of

the operators $p_i$ which act as
$$\exp(\mathrm{i}n\ p_i)|\theta_i\rangle=|\theta_i+\frac{1}{2}n\pi\rangle. \tag{2.8}$$

In this representation the Hamiltonian has the form
$$\mathcal{H}=-\sum_{j}\left[\frac{1}{2}\lambda_{1}\cos(\theta_{j}-\theta_{j+1})+\frac{1}{4}\lambda_{2}\cos 2(\theta_{j}-\theta_{j+1})\right]-\sum_{j}\left(2h_{1}\cos p_{j}+h_{2}\cos 2p_{j}\right). \tag{2.9}$$

In deriving this model the couplings $\lambda_1$, $\lambda_2$, $h_1$ and $h_2$ are all free. Special restrictions can be obtained if the time-continuum limit is taken in a special way. E.g. Kohmoto *et al* (1981) use the model where
$$\lambda_{2}/\lambda_{1}=h_{2}/h_{1}. \tag{2.10}$$

This plane contains most of the interesting features of the classical model, and in a special case can be mapped onto the exactly solved $XXZ$ model. Their model has two variables $\beta$ and $\lambda$, and the following correspondence is true with our variables:
$$h_{1}=1, \quad h_{2}=\lambda, \quad \frac{1}{4}\lambda_{1}=\beta, \quad \frac{1}{4}\lambda_{2}=\lambda\beta. \tag{2.11}$$

A different time-continuum limit was used by Drugowich de Felicio and Köberle (1982) in their study of the critical behaviour of the Ashkin-Teller model. They assumed $h_2=0$ where many interesting features are missing.

The RG transformation showed that the (2.10) plane is not an invariant plane, therefore in the RG method the whole form of the Hamiltonian was used. However, in the finite size scaling calculation for the sake of simplicity we also confine ourselves to the surface $\lambda_{2}/\lambda_{1}=h_{2}/h_{1}$.

In what follows the excitation spectrum of the Hamiltonian will be studied. It is an important, preliminary task, since in the Hamiltonian study the lower-lying states play a central role.

First of all it can be seen from the representation of the Hamiltonian given in (2.5)-(2.7) that the eigenstates belong to four orthogonal subspaces, characterised by the sum of the spins along a chain modulo 4. Thus the states $|1'1'\dots1'\rangle$, $|2'1'\dots1'\rangle$, $|3'1'\dots1'\rangle$ and $|4'1'\dots1'\rangle$ belong to different subspaces which will be called 1st, 2nd, 3rd and 4th subspace, respectively. It is easily seen that the 2nd and 4th subspaces are degenerate since the Hamiltonian is invariant under the overall change $|2'\rangle\leftrightarrow|4'\rangle$. The $k$th energy level of the $i$th subspace will be denoted by $E_{i,k}$.

Let us now turn to the symmetry classification of the low-lying states of finite chains using both periodic boundary condition and free ends. In each subspace the lowest-lying levels are either symmetric (in the case of periodic boundary condition they have momentum $k=0$, while for a free chain they have left-right symmetry) or antisymmetric (they have momentum $k=\pi$ in the case of periodic boundary condition, while for a free chain they are antisymmetric under reflection to the centre of the chain). A superscript s or a denotes whether the state is symmetric or antisymmetric.

According to the degeneracy structure and sequence of low-lying levels four different regions can be distinguished in the space of couplings. In this paper we look at $\lambda_1>0$ only, allowing the other couplings to have both positive and negative values. For chains with even number of sites the energy differences are even functions of $h_1$ and therefore results for $h_1>0$ only will be shown. Figure 1 shows a sketch of the different regions calculated for the simplest case of two spins on a chain with periodic boundary condition. The location of the boundaries between these regions depends on the size

![](./images/812700427467358209_1.jpg)

Figure 1. Regions in the space of couplings with different sequence and degeneracy for the low-lying energy levels.

of the chain and on the boundary condition. In the thermodynamic limit, however, the same phase diagram is recovered, irrespective of the boundary condition.

The level sequence in the different regions is as follows:

(1) Four low-lying states can be separated from the rest of the states having higher energy. These four states belong to the four different subspaces and they are all symmetric. The lowest level belongs always to the 1st subspace. For the sequence of the other three levels there are two possibilities:

$$\text{(1a) } E_{1,1}^{\mathrm{s}}<E_{3,1}^{\mathrm{s}}<E_{2,1}^{\mathrm{s}}=E_{4,1}^{\mathrm{s}} \tag{2.12}$$

or

$$\text{(1b) } E_{1,1}^{\mathrm{s}}<E_{2,1}^{\mathrm{s}}=E_{4,1}^{\mathrm{s}}<E_{3,1}^{\mathrm{s}}. \tag{2.13}$$

The two regions are separated by a surface where $E_{2,1}^{\mathrm{s}}=E_{3,1}^{\mathrm{s}}=E_{4,1}^{\mathrm{s}}$ i.e. the behaviour is Potts-like. In the plane $h_{1}=0$ below region (1a) the two lowest levels become degenerate, i.e. $E_{1,1}^{\mathrm{s}}=E_{3,1}^{\mathrm{s}}<E_{2,1}^{\mathrm{s}}=E_{4,1}^{\mathrm{s}}$.

(2) In this region it is not possible to separate four low-lying states. The lowest level is still a non-degenerate $E_{1,1}^{\mathrm{s}}$, but the next two levels are both doubly degenerate. One of them is $E_{2,1}^{\mathrm{s}}=E_{4,1}^{\mathrm{s}}$, the other is $E_{3,1}^{\mathrm{a}}=E_{1,2}^{\mathrm{s}}$, i.e. an antisymmetric state from the third subspace is now lower in energy as the symmetric state and it is degenerate with the second symmetric state of the 1st subspace, or it is $E_{2,2}^{\mathrm{s}}=E_{4,2}^{\mathrm{s}}$, depending on the values of the couplings.

(3) In this region the lowest level is two-fold degenerate, $E_{1,1}^{\mathrm{s}}=E_{3,1}^{\mathrm{a}}$ or $E_{1,1}^{\mathrm{a}}=E_{3,1}^{\mathrm{s}}$, depending on whether the length of the chain $N$ is $N=4 l$ or $N=2(2 l+1)$, where $l$ is integer.

The last region is the simplest. The two-fold degenerate ground state can easily be constructed and an antiferromagnetic ordering can easily be demonstrated. This will be done in $\S 4$ by using finite chain results.

The situation is more complicated in the other regions, where in the thermodynamic limit new degeneracies may arise. In region (1) where the four lowest levels of a finite segment of chain can be mapped onto a new object with the Ashkin-Teller symmetry,

renormalisation group transformation can be used to determine the phase boundaries and critical behaviour, while in region (2) where renormalisation would lead to a much more complicated model, finite size scaling will be used.

## 3. Renormalisation group transformation

In the renormalisation group transformation for quantum spin systems (for a review see Pfeuty *et al* 1982) the Hamiltonian is split into an unperturbed part containing non-interacting cells of spins and a perturbation containing the intercell couplings. In the RG transformation the low-lying levels of a cell are mapped onto the states of a new object which will be the new cell variable. A simple RG transformation into a Ashkin-Teller like model which has the symmetries of the original model is possible in region (1) only and we will restrict ourselves to this domain. Even in this domain the results are not very reliable near the boundary to region (2), where the next level comes close to the four low-lying ones and can influence the critical behaviour. We will present the results in the sector where all couplings are positive since this sector is invariant under the RG transformation. The other parts of region (1) do not show any new structure; they can be mapped onto the above sector by the RG transformation.

Depending on the choice how the Hamiltonian is split, different RG transformations can be defined. In this paper we will consider two of them. A self-dual RG transforma- tion which conserves the duality is used to determine the phase structure, while the block transformation method is used to determine the critical indices. In the last method different sizes of the blocks were used in the transformation, in order to see the convergence and to obtain evidence from the series of results for the existence of a line of fixed points.

### 3.1. Duality conserving decimation

This type of RG transformation for the Ising model has been proposed by Fernandez- Pacheco (1979) and later was used for the Potts model by Horn *et al* (1980), Hu (1980), Sólyom and Pfeuty (1981), Iglói and Sólyom (1983b). The Ashkin-Teller model being also a self-dual model, the transformation can also be used. In this paper we apply the method for the simplest case with two spins in a cell. The non-interacting cells are chosen such that every second spins are fixed in a given state and they interact with their left neighbour only. The non-fixed spins are eliminated by the RG procedure. In the calculation of the state of a cell the representation in terms of states $|1\rangle$, $|2\rangle$, $|3\rangle$ and $|4\rangle$ is convenient to use.

Fixing one end spin for example in the state $|1\rangle$, the eigenfunction of the cell has the form:

$$
\Psi_{1}=\left(a_{1}|1\rangle+a_{2}|2\rangle+a_{3}|3\rangle+a_{4}|4\rangle\right)|1\rangle. \tag{3.1}
$$

The coefficients and the energies are determined by the eigenvalue problem:

$$
\left|\begin{array}{cccc}
-E-\frac{1}{2} \lambda_{1} & -h_{1} & -h_{2} & -h_{1} \\
-h_{1} & -E+\frac{1}{2} \lambda_{1} & -h_{1} & -h_{2} \\
-h_{2} & -h_{1} & -E+\frac{1}{2} \lambda_{1} & -h_{1} \\
-h_{1} & -h_{2} & -h_{1} & -E+\frac{1}{2} \lambda_{2}
\end{array}\right|=0. \tag{3.2}
$$

In region (1) the lowest eigenstate is
$$
\Psi_{1}^{\mathrm{s}}=\frac{1}{\sqrt{1+2 a_{1}^{2}+a_{2}^{2}}}\left\{|1\rangle+a_{1}|2\rangle+a_{2}|3\rangle+a_{1}|4\rangle\right\}|1\rangle \tag{3.3}
$$
where the coefficients are given by
$$
\begin{aligned}
&a_{1}=\frac{\left(-E_{0}-\frac{1}{2} \lambda_{1}\right) h_{1}+h_{1} h_{2}}{\left(-E_{0}+\frac{1}{2} \lambda_{2}-h_{2}\right) h_{2}+2 h_{1}^{2}} \\
&a_{2}=\frac{-E_{0}-\frac{1}{2} \lambda_{1}+h_{2}}{-E_{0}+\frac{1}{2} \lambda_{1}+h_{2}}
\end{aligned} \tag{3.4}
$$
and $E_{0}$ is the lowest eigenvalue of (3.2). Similarly, if the end spin is fixed in another state, the lowest-energy cell state is
$$
\Psi_{2}^{\mathrm{s}}=\frac{1}{\sqrt{1+2 a_{1}^{2}+a_{2}^{2}}}\left\{a_{1}|1\rangle+|2\rangle+a_{1}|3\rangle+a_{2}|4\rangle\right\}|2\rangle \tag{3.5}
$$
or
$$
\Psi_{3}^{\mathrm{s}}=\frac{1}{\sqrt{1+2 a_{1}^{2}+a_{2}^{2}}}\left\{a_{2}|1\rangle+a_{1}|2\rangle+|3\rangle+a_{1}|4\rangle\right\}|3\rangle \tag{3.6}
$$
or
$$
\Psi_{4}^{\mathrm{s}}=\frac{1}{\sqrt{1+2 a_{1}^{2}+a_{2}^{2}}}\left\{a_{1}|1\rangle+a_{2}|2\rangle+a_{1}|3\rangle+|4\rangle\right\}|4\rangle. \tag{3.7}
$$

These states will be identified as the four states of the cell-spin.

The recursion relations for the different couplings can be obtained from the condition that all matrix-elements between these low-lying states should be the same before and after the transformation:
$$
\begin{aligned}
&h_{1}^{\prime}=h_{1} \frac{2 a_{1}+2 a_{1} a_{2}}{1+2 a_{1}^{2}+a_{2}^{2}}, \quad h_{2}^{\prime}=h_{2} \frac{2 a_{2}+2 a_{1}^{2}}{1+2 a_{1}^{2}+a_{2}^{2}} \\
&\lambda_{1}^{\prime}=\lambda_{1} \frac{1-a_{2}^{2}}{1+2 a_{1}^{2}+a_{2}^{2}}, \quad \lambda_{2}^{\prime}=\lambda_{2} \frac{1-2 a_{1}^{2}+a_{2}^{2}}{1+2 a_{1}^{2}+a_{2}^{2}}.
\end{aligned} \tag{3.8}
$$

These recursion relations have three types of trivial fixed point solutions yielding three different phases in region (1). The regions of attraction of these fixed points are shown in figure 2.

(I) Paramagnetic region—the couplings scale to $h_{1}=$ arbitrary, $h_{2}=$ arbitrary, $\lambda_{1}=$ $0, \lambda_{2}=0$. The corresponding ground-state of the Hamiltonian is unique; all the spins are in the $|1 '\rangle=\frac{1}{2}(|1\rangle+|2\rangle+|3\rangle+|4\rangle)$ state.

(II) Partially ordered region—the couplings scale to $h_{1}=0, h_{2}=$ arbitrary, $\lambda_{1}=0$, $\lambda_{2}=$ arbitrary. The ground state is two-fold degenerate; it is $\Pi_{i}(1 / \sqrt{2})\left(|1\rangle_{i}+|3\rangle_{i}\right)$ or $\Pi_{i}(1 / \sqrt{2})\left(|2\rangle_{i}+|4\rangle_{i}\right)$.

(III) Fully ordered region—the couplings scale to $h_{1}=0, h_{2}=0, \lambda_{1}=$ arbitrary, $\lambda_{2}=$ arbitrary. All the spins are in the same state, but it can be any of the four states and therefore the ground state is four-fold degenerate.

The critical surfaces which separate the different phases are characterised by the following non-trivial fixed points.

![](./images/812700427467358209_2.jpg)

Figure 2. Phase diagram of the Hamiltonian Ashkin-Teller model for all couplings positive. The model is paramagnetic in region I, partially ordered in region II and ferromagnetically ordered in region III. $I_1$, $I_2$, $I_3$ and P give the locations of the non-trivial fixed points of the self-dual RG transformation.

(i) The points of the surface separating the paramagnetic and the fully ordered region scale to: $h_1=0$, $h_2=0$, $\lambda_1=0$, $\lambda_2=0$, with however

$$
h_1/\lambda_1=0.25, \quad h_2/\lambda_1=0, \quad \lambda_2/\lambda_1=0. \tag{3.9}
$$

It is an Ising like fixed point denoted by $I_1$ in figure 2. The thermal eigenvalue is 2, the corresponding critical exponent $\nu$ is 1.

(ii) The points of the critical surface separating the paramagnetic and the partially ordered region scale to: $h_1=0$, $\lambda_1=0$, $\lambda_2=0$, $h_2=$ arbitrary, with however

$$
h_1/\lambda_2=0.125, \quad \lambda_1/\lambda_2=0. \tag{3.10}
$$

It is also an Ising like fixed point denoted by $I_2$. The thermal eigenvalue is 2, the critical exponent $\nu$ is 1.

(iii) The points of the surface separating the fully ordered region and the partially ordered region scale to: $h_1=0$, $h_2=0$, $\lambda_1=0$, $\lambda_2=$ arbitrary, with however

$$
h_1/\lambda_1=0, \quad h_2/\lambda_1=0.5. \tag{3.11}
$$

It is also an Ising like fixed point denoted by $I_3$, the dual of the fixed point (ii).

(iv) The points of the line where the three phases coexist scale to: $h_1=0$, $h_2=0$, $\lambda_1=0$, $\lambda_2=0$, with however

$$
h_1/\lambda_1=0.25, \quad h_2/\lambda_1=0.25, \quad \lambda_2/\lambda_1=1. \tag{3.12}
$$

This is the critical point of the four-state Potts model denoted by P in figure 2. The thermal eigenvalue is 2.5, the critical exponent $\nu$ is 0.756, not very close to the conjectured $\nu=\frac{2}{3}$.

The structure of the phase diagram and the character of the fixed points are in agreement with the result obtained by Knops (1975) for the 2D classical Ashkin-Teller model. Our results can also be compared on the $h_1/h_2=\lambda_1/\lambda_2$ surface to that calculated by Kohmoto et al (1981). The boundaries of the different phases on this surface are

also sketched in figure 2. In the three-phase region the border lines are dual to each other, and even in this simple approximation agree fairly well with the values given by Kohmoto *et al.* Our approximate RG method, however, fails to indicate what is known from mapping to the six-vertex model, that the fixed points $I_1$ and P are connected by a line of fixed points with continuously varying critical indices. The results can be improved by using larger and larger cells in the transformation. Our earlier calculation on the Potts model (Iglói and Sólyom 1983b) showed, however, that the convergence of the results of the self-dual RG transformation is extremely slow and it is very doubtful whether it is possible to extrapolate from those values. On the other hand, the results of the block-transformation method converge faster to the conjectured values. Therefore, we used this method for the Ashkin-Teller model, to obtain some evidence for the existence of a line of fixed points.

### 3.2. Block-transformation method

In this type of the RG transformation, the unperturbed part of the Hamiltonian contains all the field terms and the intra-block couplings, while the perturbation is the coupling between neighbouring blocks. The recursion equations for the simplest case with two spins per cell have been derived in an earlier paper by one of the authors (Sólyom 1981). It was shown there that for the Ashkin-Teller model, like for other self-dual models, the block-transformation is dual to the decimation transformation and therefore the two transformations give equivalent results for the critical behaviour.

Starting with the Hamiltonian with four couplings $\lambda_1$, $\lambda_2$, $h_1$ and $h_2$ the RG transformation generates two new couplings denoted by $x$ and $y$, but further renormalisation steps will not increase the number of couplings. Instead of equation (2.7), the action of $H_\lambda$ on pairs of spins should be given as
$$
\begin{aligned}
&H_\lambda|1'1'\rangle=-\frac{1}{4}\lambda_1|2'4'\rangle-\frac{1}{4}\lambda_2|3'3'\rangle-\frac{1}{4}\lambda_1|4'2'\rangle \\
&H_\lambda|2'4'\rangle=-\frac{1}{4}\lambda_1|1'1'\rangle-\frac{1}{4}x^2\lambda_1|3'3'\rangle-\frac{1}{4}y^2\lambda_2|4'2'\rangle \\
&H_\lambda|3'3'\rangle=-\frac{1}{4}\lambda_2|1'1'\rangle-\frac{1}{4}x^2\lambda_1|2'4'\rangle-\frac{1}{4}x^2\lambda_1|4'2'\rangle \\
&H_\lambda|4'2'\rangle=-\frac{1}{4}\lambda_1|1'1'\rangle-\frac{1}{4}y^2\lambda_2|2'4'\rangle-\frac{1}{4}x^2\lambda_1|3'3'\rangle
\end{aligned}
\tag{3.13}
$$
or
$$
\begin{aligned}
&H_\lambda|1'2'\rangle=-\frac{1}{4}\lambda_1|2'1'\rangle-\frac{1}{4}y\lambda_2|3'4'\rangle-\frac{1}{4}x\lambda_1|4'3'\rangle \\
&H_\lambda|2'1'\rangle=-\frac{1}{4}\lambda_1|1'2'\rangle-\frac{1}{4}x\lambda_1|3'4'\rangle-\frac{1}{4}y\lambda_2|4'3'\rangle \\
&H_\lambda|3'4'\rangle=-\frac{1}{4}y\lambda_2|1'2'\rangle-\frac{1}{4}x\lambda_1|2'1'\rangle-\frac{1}{4}x^2\lambda_1|4'3'\rangle \\
&H_\lambda|4'3'\rangle=-\frac{1}{4}x\lambda_1|1'2'\rangle-\frac{1}{4}y\lambda_2|2'1'\rangle-\frac{1}{4}x^2\lambda_1|3'4'\rangle
\end{aligned}
\tag{3.14}
$$
and similar relations for the other combinations of neighbouring spins. The unrenormalised value of $x$ and $y$ is $x=y=1$.

We have performed the calculations with $N=2$, 3 and 4 sites in the blocks in region (1) of the $\lambda_1$, $\lambda_2$, $h_1$, $h_2$ coupling space starting with $x=y=1$. The phase structure of the model is similar to that shown in figure 2 obtained by a different RG transformation, only the locations of the critical surfaces are somewhat different. The trivial fixed points characterising the three phases are as follows.

(I) $h_1=$ arbitrary, $h_2=$ arbitrary, $\lambda_1=0$, $\lambda_2=0$, $x=0$, $y=0$. This gives rise to a paramagnetic state.

(II) $h_{1}=0$, $h_{2}=$ arbitrary, $\lambda_{1}=0$, $\lambda_{2}=$ arbitrary, $x=1$, $y=1$ gives a partially ordered state.

(III) $h_{1}=0$, $h_{2}=0$, $\lambda_{1}=$ arbitrary, $\lambda_{2}=$ arbitrary, $x=1$, $y=1$ is the fixed point of the fully ordered state.

The non-trivial fixed points separating the three different phases are
(i) $h_{1}=0$, $h_{2}=0$, $\lambda_{1}=0$, $\lambda_{2}=0$, $x=1$, $y=1$ with however $h_{1}/\lambda_{1}=\frac{1}{4}a$, $h_{2}/\lambda_{1}=0$, $\lambda_{2}/\lambda_{1}=0$
(ii) $h_{1}=0$, $\lambda_{1}=0$, $\lambda_{2}=0$, $h_{2}=$ arbitrary, $x=0$, $y=0$ with however $h_{1}/\lambda_{2}=\frac{1}{8}a$, $\lambda_{1}/\lambda_{2}=0$
(iii) $h_{1}=0$, $h_{2}=0$, $\lambda_{1}=0$, $\lambda_{2}=$ arbitrary, $x=1$, $y=1$ with however $h_{2}/\lambda_{1}=\frac{1}{2}a$, $h_{1}/\lambda_{1}=0$
(iv) $h_{1}=0$, $h_{2}=0$, $\lambda_{1}=0$, $\lambda_{2}=0$, $x=y=$ finite, with however $\lambda_{2}/\lambda_{1}=1$, $h_{2}/h_{1}=1$, $h_{1}/\lambda_{1}=\frac{1}{4}b$
where $a$ and $b$ are numbers of the order of unity.

Their values are given in table 1 together with the critical exponent $\nu$ calculated from largest eigenvalues $\lambda_{t}$ of the linearised recursion relations near the fixed points by the relation $\nu=\log N/\log \lambda_{t}$ where $N$ is the size of the block. Both for the Ising and the Potts fixed points $\nu$ converges to the exactly known or conjectured values. The three Ising like fixed points show the same behaviour.

Table 1. The position of the fixed points, and the correlation length critical exponent $\nu$ at the fixed points of the Ashkin-Teller model for different size of the blocks used in the RG transformation. $\lambda_{t2}$ denotes the next to leading eigenvalue at the fixed points (i) and (iv).

<table>
<tbody><tr><td colspan="2"></td><td>$N=2$</td><td>$N=3$</td><td>$N=4$</td><td>Exact or conjectured</td></tr>
<tr><td rowspan="3">Ising-like fixed points</td><td>$a$</td><td>1.277</td><td>1.155</td><td>1.105</td><td>1</td></tr>
<tr><td>$\nu$</td><td>1.48</td><td>1.31</td><td>1.24</td><td>1</td></tr>
<tr><td>$\lambda_{t2}$</td><td>0.81</td><td>0.71</td><td>0.70</td><td>1</td></tr>
<tr><td rowspan="4">Potts fixed points</td><td>$b$</td><td>1.189</td><td>1.152</td><td>1.136</td><td>1</td></tr>
<tr><td>$x=y$</td><td>1.193</td><td>1.212</td><td>1.219</td><td></td></tr>
<tr><td>$\nu$</td><td>1.03</td><td>0.90</td><td>0.85</td><td>$\frac{2}{3}$</td></tr>
<tr><td>$\lambda_{t2}$</td><td>1.18</td><td>1.32</td><td>1.44</td><td>1</td></tr>
</tbody></table>

The existence of a line of fixed points should show up in the existence of a marginal operator, i.e. the second largest eigenvalue $\lambda_{t2}$ should converge to unity. Unfortunately this tendency is not seen from the limited number of points given in table 1.

### 4. Finite size scaling

In the past few years finite size scaling has become a powerful tool in investigating 1D quantum systems (Hamer and Barber 1981). This method requires the solution of the eigenvalue problem for finite rings. If the mass gap, i.e. the energy difference between the ground state and the first excited state, is $G_{N}(K)$, where $N$ is the size of the ring, and $K$ is the coupling, then the location of a conventional phase transition

point is the limit of $K_{N}^{\mathrm{c}}$ values, at which the scaled gap ratio is unity:

$$
(N-1) G_{N-1}\left(K_{N}^{\mathrm{c}}\right) / N G_{N}\left(K_{N}^{\mathrm{c}}\right)=1. \tag{4.1}
$$

This procedure assumes that at the critical point the energy gap vanishes as $1/N$.

If a system exhibits a line or a surface of critical points, then this region is characterised by the property that everywhere on this surface the scaled gap goes to a finite value:

$$
\lim _{N \rightarrow \infty} N G_{N}(K)=\text { finite. } \tag{4.2}
$$

This behaviour has to be contrasted to that of a non-critical system, where the scaled gap tends to zero or infinity, in the high-temperature or low-temperature phases, respectively.

The critical indices can also be determined by finite size scaling. The correlation length critical exponent $\nu$ can be calculated from the slope of the Callan-Symanzik $\beta$-function at the critical point. For the $\beta$-function the form proposed by Roomany and Wyld (1981) is used:

$$
\beta_{N}(K) / K=\ln \left[N G_{N}(K) /(N-1) G_{N-1}(K)\right] / K \frac{\mathrm{d}}{\mathrm{d} K} \ln \left[G_{N}(K) G_{N-1}(K)\right] \ln \left(\frac{N}{N-1}\right). \tag{4.3}
$$

Note that the gap $G$ calculated in this paper is proportional to the couplings while Roomany and Wyld used the dimensionless gap. This explains the form given in (4.3).

In the following the result of finite size scaling on the Ashkin-Teller model is presented. As mentioned before the surface given by (2.10) contains the Potts point and goes through all the possible phases in the phase diagram, therefore we will present the results only for this characteristic plane of the total coupling space. At first the phase diagram, then the critical exponent will be discussed.

### 4.1. Phase diagram

The extrapolated phase diagram is drawn in figure 3. Besides the three phases which have appeared in region (1) in the renormalisation group treatment, there are two new regions: the 'critical fan' denoted by V, and the antiferromagnetically ordered region denoted by IV. Notice that this phase diagram is the same as that given by Kohmoto *et al* (1981).

The parameter $\beta$ used by them is $\beta=\lambda_{1} / 4 h_{1}$ in the language of this paper. The boundaries in the phase diagram where only conventional second-order transitions take place (i.e. for $\lambda_{2} / \lambda_{1}>-1 / \sqrt{2}$ ) were determined from extrapolating the finite-lattice phase transition points defined by equation (4.1). To illustrate the accuracy of the procedure the scaled gaps for a fixed value of $\lambda_{2} / \lambda_{1}$ as a function of $h_{1} / \lambda_{1}$ are shown for different chain lengths in figure 4. The crossing points which determine the critical value of $h_{1} / \lambda_{1}$ are shown in figure 5. The broken curves were obtained by calculating the mass gap between the 1st and the 2nd (or 4th) subspace, while the dotted curves represent the transition between the 1st and 3rd subspaces.

For $-1 / \sqrt{2}<\lambda_{2} / \lambda_{1} \leqslant 1$ there is only one transition point; all the four lowest-energy levels become degenerate in the thermodynamic limit at the same point $h_{1} / \lambda_{1}=\frac{1}{4}$, as self-duality would require.

![](./images/812700427467358209_3.jpg)

Figure 3. Phase diagram obtained from finite lattice extrapolation for couplings restricted to the surface $\lambda_2/\lambda_1=h_2/h_1$. For points without error bar the error is smaller than the size of the point.

![](./images/812700427467358209_4.jpg)

Figure 4. Scaled gap function $NG_N$ for $\lambda_2/\lambda_1=$ -0.55 for different chain lengths $N$ as a function of $h_1/\lambda_1$. The gap is calculated between the second and first subspaces.

For $\lambda_2/\lambda_1>1$, however, there is a partially ordered phase, where only the 1st and the 3rd subspaces are degenerate, and at the phase boundaries the degeneracy changes by a factor of two. The error in the extrapolation (shown by error bars in figure 3) is rather small, unless we are close to the critical fan. In the three-phase region, crosses show the result of the self-dual RG-method presented in $\S 3$. Finally we mention that the boundaries of the three-phase region can be rather well approximated by the following function:

$$
\begin{aligned}
&(h_1/\lambda_1)_u=\frac{1}{4}+\frac{1}{8}(\lambda_2/\lambda_1)\exp[-2/(\lambda_2/\lambda_1-1)] \\
&(h_1/\lambda_1)_l=(h_1/\lambda_1)_u^{-1}
\end{aligned} \tag{4.4}
$$

where $(h_1/\lambda_1)_u$ and $(h_1/\lambda_1)_l$ denote the upper and lower lines respectively.

When $\lambda_2/\lambda_1<0$ but $\lambda_2/\lambda_1>-1/\sqrt{2}$ the scaled gap functions tend to a finite value for one value of $h_1/\lambda_1$, only, as seen in figure 4. However as $\lambda_2/\lambda_1$ approaches $-1/\sqrt{2}$ the slope of the scaled gap functions at the transition point goes to zero. Just at $\lambda_2/\lambda_1=-1/\sqrt{2}$ the slope of the extrapolated curve is zero, indicating a phase transition of infinite order i.e. a Kosterlitz-Thouless transition. For $-1<\lambda_2/\lambda_1<-1/\sqrt{2}$ there exists an interval in $h_1/\lambda_1$ where condition (4.2) is fulfilled, i.e. the $\beta$-function will vanish identically. How this 'critical fan' develops as the chain length increases can be seen in figure 6. For large values of $h_1/\lambda_1$ the scaled gap goes to infinity, for small values of $h_1/\lambda_1$ it goes to zero. In between there is a region where the scaled gap tends to a finite value. The boundaries of this region are characterised by the fact that the scaled gap has zero slope, i.e. at the boundary of the 'critical fan' the transition is of the Kosterlitz-Thouless type. The critical fan occupies part of region (2) where new degeneracies occur with respect to region (1), but it extends also partly into region (1).

When $\lambda_2/\lambda_1=-1$ the critical fan extends to the whole $h_1/\lambda_1$ line, but a level crossing occurs along this line giving rise to an antiferromagnetically ordered state beyond it. The two-fold degenerate ground state is

$$
\Psi_{\pm}=\prod_{i}(|2'\rangle\mp|4'\rangle)_{2i}(|2'\rangle\pm|4'\rangle)_{2i+1} \tag{4.5}
$$

![](./images/812700427467358209_5.jpg)

Figure 5. Critical couplings in the $\lambda_2/\lambda_1=h_2/h_1$ plane satisfying (4.1) for different chains. The broken curves are calculated from the gap between the 1st and 2nd subspaces, while the dotted ones from the gap between the 1st and 3rd subspaces.

![](./images/812700427467358209_6.jpg)

Figure 6. Scaled gap function $NG_N$ for $\lambda_2/\lambda_1=$ -0.75 for different chain lengths. An extended critical region develops between the points where the scaled gap has zero slope.

taking the upper or lower signs, respectively. The energy per site is

$$
E_{0}=h_{2}+\frac{1}{4} \lambda_{2}. \tag{4.6}
$$

As noted by Kohmoto et al, the transition into the antiferromagnetic state is of KDP type. Although there is a level crossing which gives rise to a latent heat, the energy gap in the antiferromagnetic region vanishes as $\lambda_2/\lambda_1\rightarrow-1$, i.e. the corresponding correlation length diverges. For $h_1/\lambda_1=\frac{1}{4}$ e.g. the following simple form holds for the first excitations into the second and third subspaces

$$
\begin{aligned}
& \Delta E_{2}\left(\lambda_{2} / \lambda_{1}\right)=2\left[\left(\lambda_{2} / \lambda_{1}\right)^{2}-1\right]^{1 / 2} \\
& \Delta E_{3}\left(\lambda_{2} / \lambda_{1}\right)=2 \Delta E_{2}\left(\lambda_{2} / \lambda_{1}\right).
\end{aligned} \tag{4.7}
$$

### 4.2. The critical exponent $\nu$

In the three-phase region the transitions are of Ising type with $\nu=1$. In the Potts point, however, and for $\lambda_2/\lambda_1<1$, $\nu$ should be different and vary continuously. Since in this part of the phase space the $\lambda_2$ direction is marginal when $h_1$ has its critical value, the $\nu$ exponent can be obtained from the slope of the Callan-Symanzzyk $\beta$-function (4.3) in the $h_1$ direction

$$
\beta\left(h_{1} / \lambda_{1}\right) \approx \frac{1}{2} \nu^{-1}\left[\left(h_{1} / \lambda_{1}\right)-\left(h_{1} / \lambda_{1}\right)_{\mathrm{c}}\right] /\left(h_{1} / \lambda_{1}\right)_{\mathrm{c}}. \tag{4.8}
$$

The results obtained from the finite lattice $\beta$-functions are shown in figure 7. The region beyond $\lambda_2/\lambda_1=1$ has no meaning as a critical exponent because $\nu$ here is not calculated from a fixed point, but these values can serve as guides how to extrapolate in the Potts fixed point. As can be seen in figure 7 the $1/\nu(\lambda_2/\lambda_1)$ curves go to unity for large $\lambda_2/\lambda_1$. For a range above $\lambda_2/\lambda_1=1$ they increase roughly linearly with a slope proportional to $[N(N-1)]^{1/2}$, then bend over to a decreasing curve, having zero slope at $\lambda_2/\lambda_1=1$. If the extrapolation to $N\rightarrow\infty$ is done from the values at $\lambda_2/\lambda_1=1$, one would get a value $\nu=\frac{3}{4}$ for the four-state Potts model. If, however, use is made of the region $\lambda_2/\lambda_1>1$ and one extrapolates the straight part of the $1/\nu(\lambda_2/\lambda_1)$ curve to $\lambda_2/\lambda_1=1$ and takes the limit of these points, since the region where the bending

![](./images/812700427467358209_7.jpg)

Figure 7. Finite lattice results for the critical exponent $\nu$. The broken curve is the result obtained from the analogy with the six-vertex model.

occurs shrinks to zero with increasing $N$, we get

$$
\nu(\lambda_2/\lambda_1=1)=\frac{2}{3}\pm0.03 \tag{4.9}
$$

in good agreement with the conjectured values.

In the region $\lambda_2/\lambda_1<1$ the finite lattice results for $\nu$ converge fast to the exact value only for $\lambda_2/\lambda_1<0.6$-$0.7$ where $1/\nu$ is a concave function, but due to the bending around $\lambda_2/\lambda_1=1$ the convex part is not obtained correctly. The good convergence breaks down again at the other end of the critical line where the critical fan appears.

### 5. Discussion

In the present paper the Hamiltonian version of the 2D Ashkin-Teller model was studied assuming ferromagnetic coupling for the two-spin coupling (in the spin representation (2.3)) in the spatial direction, but allowing for arbitrary couplings for the other terms. It was shown that the phase diagram is simply an extension of the phase diagram derived by Kohmoto et al (1981) for a particular surface in the coupling space, i.e. no new phases appear.

The boundaries in the phase diagram were determined partially by renormalisation group transformation, partially by using finite size extrapolation techniques. The finite chain results converge well except for the boundaries of the critical fan, which in the extended coupling space is a more extended object. Since everywhere inside this region the scaled gap is finite, the boundaries cannot be located as well as for an ordinary second-order transition, where the scaled gap is finite at a single point only.

The renormalisation group treatment does not give very good results for the critical behaviour at the Potts point and along the critical line going out of the Potts point. Using finite size scaling, however, much better accuracy is achieved if the critical behaviour is studied in the extended space of couplings and the Potts point is approached only after the $N\rightarrow\infty$ limit was performed already. The importance of the order of limit in finite size procedure has already been pointed out by the authors (Iglói and Sólyom 1983a) in another study of first-order transitions. It will be shown in a separate publication that the critical line in the Ashkin-Teller model can be obtained more easily if the model is further generalised and the Ashkin-Teller limit is taken only after the thermodynamic limit of the generalised model has been performed.

## References

Drugowich de Felicio J H and Köberle R 1982 *Phys. Rev.* **B 25** 511

Fernandez-Pacheco A 1979 *Phys. Rev.* **B 19** 3173

Hamer C J and Barber M N 1981 *J. Phys. A: Math. Gen.* **14** 241

Horn D, Karliner M and Yankielowicz S 1980 *Nucl. Phys.* **B 170** FS1 467

Hu B 1980 *J. Phys. A: Math. Gen.* **13** L321

Iglói F and Sólyom J 1983a *J. Phys. C: Solid State Phys.* **16** 2833
—— 1983b *Phys. Rev.* **B 28** 2785

Kadanoff L P 1977 *Phys. Rev. Lett.* **39** 903

Knops H J F 1975 *J. Phys. A: Math. Gen.* **8** 1508

Kogut J 1979 *Rev. Mod. Phys.* **51** 659

Kohmoto M, den Nijs M and Kadanoff L P 1981 *Phys. Rev.* **B 24** 5229

Pfeuty P, Jullien R and Penson K A 1982 *Real Space Renormalization* ed T W Burkhardt and J M J van Leeuwen (Berlin: Springer) p 119

Roomany H K and Wyld H W 1981 *Phys. Rev.* **B 23** 1357

Sólyom J 1981 *Phys. Rev.* **B 24** 230

Sólyom J and Pfeuty P 1981 *Phys. Rev.* **B 24** 218

Stephen M J and Mittag L 1972 *Phys. Lett.* **41A** 357