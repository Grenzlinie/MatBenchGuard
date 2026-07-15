# NONLINEAR ASPECTS OF THE CAHN-HILLIARD EQUATION

Amy NOVICK-COHEN** and Lee A. SEGEL*
Dept. of Applied Mathematics, Weizmann Institute of Science, Rehovot, Israel

Received 28 December 1982
Revised 2 October 1983

This paper treats phase separation within the context of the phenomenological Cahn-Hilliard equation,
$c_t = 
abla \cdot [M(c)
abla (\partial f/\partial c - K
abla^2 c)]$, where $c$ is the concentration, $M(c)$ is the mobility, and $f(c)$ is the homogeneous free energy, which is assumed here to be a fourth degree polynomial. Natural boundary conditions are introduced. The full set of equilibrium solutions is specified. A comparison theorem for stability criteria which was postulated by Langer is proved here within the framework of the natural boundary conditions. Energy methods are used to define and estimate the limit of monotonic global stability. It is pointed out that within the parameter region where the uniform homogeneous state is the only equilibrium solution, there may still exist some internal "excitable" region in which the homogeneous solution possesses growing fluctuations. Furthermore a periodic instability is shown to exist in the metastable region in addition to the well-known nucleation instability.

## 1. Introduction-Derivation of the Cahn-Hilliard equation

### 1.1. Introduction

Numerous attempts have been made in recent years to explain the dynamics of pattern formation via phase transition. Sufficient cooling of a binary solution may lead to phase separation which will proceed in one of two main ways: either by nucle- ation in which sufficiently large nuclei of the second phase appear randomly and grow, or by so-called spinodal decomposition in which the whole solu- tion appears to nucleate at once, and periodic or semi-periodic structure is seen.

Pattern formation resulting from phase transi- tion has been observed in alloys [1], glasses [2], and in polymer solutions [3]. With the aid of improved laboratory techniques, such pattern formation has also been observed in binary liquid mixtures [4]. Here a continuum model due originally to Cahn and Hilliard [5] will be analyzed. Early linear treat- ments of the Cahn-Hilliard equation gave un- physical results, and the Cahn-Hilliard equation to a great extent fell out of favor and was deemed incapable of describing phase transition. The non- linear Cahn-Hilliard equation was for the most part discarded as untreatable. In its place many more involved formulations have been developed in which statistical fluctuations are included. Here we have reverted to the original equation in an attempt to ascertain to what extent the deter- ministic nonlinear continuum model is capable of describing the intricacies of phase separation which have been observed experimentally and theoretically.

Study of the Cahn-Hilliard equation can be re- garded as a useful supplement to the classical pattern-formation stability theory of the Bénard and Taylor problems [6]. The "negative viscosity" destabilizing mechanism occurs in other physical contexts [7] (and perhaps even in ecology - see sec- tion 1.7). Pattern formation via phase transition is important for certain technological applications. On general grounds perhaps the most interesting

* Also at Dept. of Math. Sci., R.P.I., Troy, N.Y. 12181, U.S.A.
**Also at Membrane Filtration Technology, Kiryat Weiz- mann, Rehovot, Israel.

0167-2789/84/$03.00 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

feature of the Cahn-Hilliard equation is its close connection with a "free-energy" or Liapunov func- tional. A long range research goal is to understand the role which such functionals play in determining qualitative behavior of nonlinear partial differential equations in the vicinity of bifurcation points.

We have used a variety of approaches in analyz- ing the Cahn-Hilliard equations. In section 1, a derivation of the Cahn-Hilliard equation is presented and natural boundary conditions deriv- able from the free energy functional are introduced in addition to no-flux boundary conditions. In sec- tion 2 the one-dimensional equilibrium solutions are outlined. It is shown that a whole spectrum of such solutions exists, ranging from symmetric solu- tions which suggest the initial stages of phase tran- sition, to highly asymmetric solutions which sug- gest a two-phase wall-pore coarsened structure. An associated eigenvalue problem criterion for deter- mining stability is stated, and a conjecture of Lan- ger [8] for periodic boundary conditions is proven here for no-flux and natural boundary conditions. In section 3 it is shown via energy integral methods that there exist finite amplitude periodic growing perturbations up to the binodal or coexistence curve, and that an excitable region may occur out- side the binodal in which fluctuations will not decay monotonically towards a uniform equilibrium state. At the inner edge of the metastable region there exist steady state solutions whose period tends to infinity as the edge is approached. These solutions are demonstrated to behave as crucial perturbations in much the same sense that limiting infinite size nuclei perturbations are predicted at this edge by classical nucleation theory [9]. Section4 contains a summary of results and discussion.

### 1.2. Some classical thermodynamic theory

The Cahn-Hilliard equation is based on a con- tinuum model for phase transition in binary sys- tems. In our formulation of this equation, which is equivalent in spirit to the derivation given by Cahn [10], we first present an equation which arises from classical thermodynamic considerations for the interdiffusion of two components A and B. In section 1.5, the formulation is generalized by a phenomenological approach, and the Cahn-Hilliard equation is obtained.

According to the linear phenomenological re- lations of thermodynamics for forces and fluxes [11]
$$J_{\mathrm{A}}=-M_{\mathrm{AA}} \nabla \mu_{\mathrm{A}}-\mathrm{M}_{\mathrm{AB}} \nabla \mu_{\mathrm{B}},\qquad(1.1)$$

$$J_{\mathrm{B}}=-M_{\mathrm{BA}} \nabla \mu_{\mathrm{A}}-M_{\mathrm{BB}} \nabla \mu_{\mathrm{B}},\qquad(1.2)$$
where the $M$'s are mobilities and the $\mu$'s are chemical potentials per unit volume. We select a coordinate system such that the net flux $J$ of component B is equal and opposite to that of component A, and we adopt the simpler notation
$$J=J_{\mathrm{B}}-J_{\mathrm{A}}, \quad c=c_{\mathrm{B}}=1-c_{\mathrm{A}},$$
where the $c$'s refer to concentrations.

Then by using the Gibbs-Duhem relationship
$$(1-c) \nabla \mu_{\mathrm{A}}+c \nabla \mu_{\mathrm{B}}=0, \quad(1.3)$$
one finds that the net flux may be expressed as
$$J=-M \nabla\left(\mu_{\mathrm{B}}-\mu_{\mathrm{A}}\right),\qquad(1.4)$$
where $M$, the mobility, is given by
$$M=\left[(1-c)\left(M_{\mathrm{BB}}-M_{\mathrm{AB}}\right)+c\left(M_{\mathrm{AA}}-M_{\mathrm{BA}}\right)\right].(1.5)$$

$M$ is assumed here to be positive [10]. Since [11]
$$\mu_{B}-\mu_{A}=\frac{\partial f}{\partial c},$$
where $f(c)$ is the free energy per unit volume, (1.4) becomes
$$J=-M \nabla \frac{\partial f}{\partial c}.\qquad(1.6)$$

Imposing mass conservation one obtains from

(1.6)

$$
\frac{\partial c}{\partial t}=\nabla \cdot\left[M \nabla \frac{\partial f}{\partial c}\right]. \tag{1.7a}
$$

Note that if $f(c)$ is a parabola that opens upwards $(f=a_0+a_1c+a_2c^2$, $a_2>0)$ and if $M$ is constant then (1.7a) reduces to the standard diffusion equation. Such a parabolic $f(c)$ corresponds in general, as will be discussed later, to stable thermodynamic conditions where phase separation does not occur and hence where normal diffusion would be expected.

In addition, a conservation of composition constraint will be imposed over the volume $v$ under consideration:

$$
\int_{v} c_{0} \mathrm{~d} v=\int_{v} c(x, t) \mathrm{d} v. \tag{1.7b}
$$

In classical thermodynamics spatial nonhomogeneities are not considered in defining the free energy. Broadly speaking

$$
\begin{aligned}
f= & (\text { heat of mixing/volume) } \\
& -(\text { entropy/volume). }
\end{aligned} \tag{1.8}
$$

Various theoretical expressions for the free energy have been developed. For a discussion of these expressions for polymer solutions see refs. 12 and 13.

### 1.3. Approximation of the free energy as a quartic polynomial in the concentration

Although contemporary molecular expressions for the free energy are becoming more and more involved, we shall employ the simplest nontrivial phenomenological free energy function, a quartic polynomial in the concentration. The cubic term, known to be important in polymers [13] for example, will be included. Thus our free energy will be asymmetric, as opposed to simpler symmetric forms of the free energy, which are often used, wherein the cubic term is omitted.

Our description applies both to alloy solutions and to liquid solutions in the limit in which the elastic strain energy and hydrodynamic flow effects are neglected. For a discussion on the inclusion of higher than quartic terms and other variants, see ref. 14.

The coefficients of the quartic polynomial will be assumed to be temperature dependent. The point at which the two minima of the free energy coalesce is called the critical point; the corresponding temperature is called the critical temperature $T_{\text{crit}}$, and the concentration, the critical concentration $c_{\text{crit}}$ (see fig. 1). At the critical point, the second and third derivatives of the free energy with respect to concentration vanish. The temperature dependence of the coefficients near the critical point can be described by scaling laws [15, 16]; e.g.

$$
\frac{\partial^{2} f}{\partial c^{2}}\left(T, c_{\text{crit}}\right) \propto \epsilon^{\gamma} \quad \text{and} \quad \frac{\partial^{4} f}{\partial c^{4}}\left(T, c_{\text{crit}}\right) \propto \epsilon^{\gamma-2\beta},
$$

where $\epsilon=(T-T_{\text{crit}})/T_{\text{crit}}$ and where $\gamma$ and $\beta$ are non-classical exponents [17]. Throughout this work no explicit form of temperature dependence for the coefficients is assumed. The emphasis of our discussion will not be on the immediate neighborhood of the critical point.

### 1.4. Piecewise constant solutions of the classical equations (1.7)

Under the supposition that the free energy is a quartic polynomial, we shall now analyze the set of

![](./images/812446132159381505_1.jpg)

Fig. 1. A typical phase diagram according to classical thermodynamic theory.

equilibrium solutions of equations (1.7a) and (1.7b). At equilibrium $0=J=M\nabla(\partial f/\partial c)$. Since $M>0$ this implies that

$$
\partial f / \partial c=\text { constant }. \tag{1.9}
$$

Since $\partial f/\partial c$ is a cubic polynomial in the concentration, (1.9) has one or three real solutions.

At equilibrium the total volume must be divided into regions in which the concentration is equal to real solutions of (1.9). The solution will be piece-wise constant, each constant portion belonging to one of the possible phase concentrations. The composition conservation constraint (1.7b) will place a dependence on the amount of each phase which will appear. Thus the net volume fractions of concentrations $c_1, c_2, c_3$ will be prescribed, but their spatial configuration will not. The non-uniqueness of the solution and the discontinuities in the concentration do not a priori disqualify such solutions, but certainly such an equilibrium configuration description is inadequate for detailing phase transitions that give rise to pattern formation with an internally dictated non-random frequency.

### 1.5. The generalized potential

Until now in our formulation of a continuum model for phase transition, effects of spatial inhomogeneity have not been taken into account in the description of the free energy of the system. Hence it is not surprising that all spatial configurations with given volume fractions of given concentrations are energetically equivalent. From the point of entropy this cannot be true. A system with many internal phase subdivisions has more entropy, in addition to the configurational entropy per volume of homogeneous concentration included in (1.8), than does a system which is otherwise equivalent but which has a minimal number of subdivisions.

A method of overcoming this difficulty, via the notion of a generalized potential, has been proposed by Cahn and Hilliard [5] but can be traced to earlier sources [36]. A derivation will be presented here in the same spirit in which it appears in [10]. The derivation of the form of generalized potential from the generalized free energy will be presented in a slightly independent manner that we feel is more illuminating. In particular, the question of boundary conditions seems not to have been explicitly dealt with in the past.

To motivate our presentation, let us return again to our previous considerations and note that if $F$ is the total free energy of a given volume then

$$
F=\int_{v} f(c(\boldsymbol{x})) \mathrm{d} \boldsymbol{x}. \tag{1.10}
$$

If the composition conservation constraint is imposed, then energy extremal configurations satisfy

$$
\frac{\partial f}{\partial c}=\text { constant }. \tag{1.11}
$$

(That is, (1.11) is the Euler-Lagrange equation which characterizes the extrema of (1.10).) Thus the equilibrium of (1.7a) and (1.7b) can be regarded as energy extremals. Let us regard the difference between the total free energy of any configuration $c(\boldsymbol{x})$ and the total free energy of the nearest equilibrium configuration as a measure of the "distance" from equilibrium. Note that

$$
\begin{aligned}
F(c)-F\left(c_{\mathrm{e}}\right) & =\int_{v}\left[f(c)-f\left(c_{\mathrm{e}}\right)\right] \mathrm{d} v \\
& =\int_{v}\left[\frac{\partial f}{\partial c}\left(c_{\mathrm{e}}\right)\left(c-c_{\mathrm{e}}\right)+\mathcal{O}\left[c-c_{\mathrm{e}}\right]^{2}\right] \mathrm{d} v, \quad(1.12)
\end{aligned}
$$

where $c_{\mathrm{e}}$ is the equilibrium concentration. Thus, in near equilibrium situations $\partial f/\partial c$ may be considered to be proportional to the local distance from equilibrium, $f(c)-f(c_{\mathrm{e}})$. In (1.6) the flux is proportional to this distance, which can thus be regarded as a forcing term for the flow of solute.

It appears that a sensible method of extending this approach is by first generalizing the total free

energy to include effects of inhomogeneity and then by proceeding as above to find a generalized "distance" from equilibrium, or equivalently a generalized potential.

As a generalized free energy with gradient effects will necessarily contain higher derivative terms, additional boundary conditions will be required in searching for extremals. No clear physical grounds for selecting boundary conditions are apparent, particularly in view of the requirement for more and more boundary conditions as more and more accurate characterizations of inhomogeneous effects are employed. We propose to meet this difficulty by imposing natural boundary conditions when the variational problem is treated.

The approach to inclusion of inhomogeneous effects as presented by Cahn and Hilliard [5] is by considering the total generalized free energy $\hat{F}$ as the integral over a generalized free energy per unit volume $\hat{f}$, where $\hat{f}$ is now assumed to depend both on the concentration and on its higher derivatives. The function $\hat{f}$ is then expanded in a Taylor series in its higher derivatives about the homogeneous average concentration. Thus
$$
\begin{aligned}
\hat{f}= & \hat{f}(c, 0,0, \ldots)+\sum_{i} L_{i}\left(\partial c / \partial x_{i}\right) \\
& +\sum_{i, j} K_{i j}^{(1)}\left(\partial^{2} c / \partial x_{i} \partial x_{j}\right) \\
& +\frac{1}{2} \sum_{i, j} K_{i j}^{(2)}\left[\left(\partial c / \partial x_{i}\right)\left(\partial c / \partial x_{j}\right)\right]+\text { higher terms },
\end{aligned}
$$
where
$$
\begin{aligned}
& L_{i}=\partial f(c, 0,0, \ldots) / \partial\left(\partial c / \partial x_{i}\right), \\
& K_{i j}^{(1)}=\partial f(c, 0,0, \ldots) / \partial\left(\partial^{2} c / \partial x_{i} \partial x_{j}\right), \\
& K_{i j}^{(2)}=\partial^{2} f(c, 0,0, \ldots) / \partial\left(\partial c / \partial x_{i}\right) \partial\left(\partial c / \partial x_{j}\right).
\end{aligned}
$$

Here $\hat{f}(c, 0,0, \ldots)$ will be identified with the classical free energy of homogeneous concentrations, $f(c)$. Now in liquid binary solutions there is no preferred direction: the media are isotropic. By standard arguments [18], $L_{i}$ must be an isotropic vector and $K_{i j}^{(1)}$ and $K_{i j}^{(2)}$ must be isotropic tensors of order 2 . Thus $L_{i}=0$ while the $K_{i j}$ 's must be multiples of the Kronecker delta, so that
$$
\begin{aligned}
\hat{f}(c, \nabla c, & \left.\nabla^{2} c, \ldots\right)=f(c)+K_{1} \nabla^{2} c+\frac{1}{2} K_{2}(\nabla c)^{2} \\
& + \text { higher terms } ;
\end{aligned}
$$
i.e., the first non-zero correction terms are second order. As a first correction these terms will be included and higher terms neglected, yielding
$$
\hat{F}=\int_{v}\left[f(c)+K_{1} \nabla^{2} c+\frac{1}{2} K_{2}(\nabla c)^{2}\right] \mathrm{d} v. \quad(1.15)
$$

The extremals of (1.15) will be located by variational analysis. A Lagrange multiplier will be utilized in order to take account of the composition conservation constraint.

As noted, natural boundary conditions are to be used here; i.e., through the variational analysis those boundary conditions which minimize the total free energy are to be found. Standard technique shows these natural boundary conditions to be
$$
\frac{\partial c}{\partial n}(x)=0 \text { on the boundary of } v, \quad(1.16)
$$
where $n$ is the unit normal to the boundary.

Now (1.16) implies that the contribution of the second term in (1.15) vanishes. Hence (1.15) may be written as
$$
\hat{F}=\int_{v}\left[f(c)+\frac{1}{2} K(\nabla c)^{2}\right] \mathrm{d} v, \quad(1.17)
$$
where $K=K_{2}$. We will assume in (1.17) that $K>0$, i.e., that there is an energetic price associated with the formation of spatial inhomogeneities. The parameter $K$ can be measured by light scattering [19], and has been expressed in terms of phenomenological variables [20] and in terms of microscopic interaction parameters [21]. Eq. (1.17) is often referred to in the literature as the

Landau-Ginzburg free energy form. It should be noted that (1.17) is only valid in the continuum limit in which molecular detail has been "washed out", and is called a coarse-grain free energy [22].

Returning to the problem of extremals, the Euler-Lagrange equation for (1.17) subject to the natural boundary condition and the composition conservation constraint is given by

$$
\frac{\partial f}{\partial c}-K \nabla^{2} c=\text { constant }. \tag{1.18}
$$

In line with the logic of the simpler continuum model, equilibrium configurations for the generalized model should be extremal; i.e. they should satisfy (1.18).

In order to consider what the generalized forcing term should be, we consider once more the "distance" from equilibrium. By expanding $\hat{f}(c)-\hat{f}(c_{\mathrm{e}})$ around $c(x)$ in a Taylor series, integrating by parts and using the boundary conditions (1.16), we obtain

$$
\begin{aligned}
\hat{F}(c)-\hat{F}(c_{\mathrm{e}})= & \int_{v}[\hat{f}(c)-\hat{f}(c_{\mathrm{e}})] \mathrm{d} v \\
= & \int_{v}\left[\left[\frac{\partial f(c)}{\partial c}-K \nabla^{2} c\right](c-c_{\mathrm{e}})\right. \\
& \left.+\mathcal{O}\left[(c-c_{\mathrm{e}})^{2}\right]\right] \mathrm{d} v.
\end{aligned} \tag{1.19}
$$

Hence in parallel with the discussion of the simpler continuum model,

$$
G(c) \equiv \frac{\partial f(c)}{\partial c}-K \nabla^{2} c, \tag{1.20}
$$

may be considered as a forcing term proportional to the local distance from equilibrium $\hat{f}(c(x))-\hat{f}(c_{\mathrm{e}}(x))$. If previously $\partial f / \partial c$ was considered the chemical potential, now $G(c)$ should be the generalized potential. Setting the flux proportional to the forcing term, as in (1.6), we obtain

$$
J=-M(c) \nabla\left[\frac{\partial f}{\partial c}(c)-K \nabla^{2} c\right]. \tag{1.21}
$$

Note that according to (1.21), equilibrium solutions satisfy the Euler-Lagrange extremal equation (1.18).

By mass conservation the generalized continuum model is now given by

$$
\frac{\partial c}{\partial t}=\nabla \cdot\left[M(c) \nabla\left[\frac{\partial f}{\partial c}(c)-K \nabla^{2} c\right]\right]. \tag{1.22}
$$

In the absence of any accurate information about its behavior as a function of the concentration, $K$ will be assumed to be a constant. On the other hand, $M(c)$ which is known [23] to be highly concentration dependent, will be maintained as a function of the concentration, subject to the condition $M(c)>0$. Lastly, we note that the natural boundary conditions (1.16) were shown to be appropriate for equilibrium configurations. Unless otherwise stated boundary conditions (1.16) will also be imposed on nonequilibrium states, for there seems no justification for proceeding otherwise.

### 1.6. Scaling

Our basic equations will be (1.22) where $M=M(c)>0$ and $K$ is a positive constant, and the composition conservation constraint

$$
\int_{v} c(\boldsymbol{x}, t) \mathrm{d} \boldsymbol{x}=\int_{v} c(\boldsymbol{x}, 0) \mathrm{d} \boldsymbol{x}, \quad \text { for all } t. \tag{1.23}
$$

If $f(c)$ is assumed to be a fourth order polynomial in the concentration,

$$
f(c)=a_{0}+a_{1} c+a_{2} c^{2}+a_{3} c^{3}+a_{4} c^{4}, \tag{1.24}
$$

and if arbitrary perturbations around a uniform homogeneous state $c(x) \equiv c_{0}$ are considered,

$$
c(\boldsymbol{x}, t)=c_{0}+\tilde{c}(\boldsymbol{x}, t), \tag{1.25}
$$

then

$$
\frac{\partial f}{\partial c}\left(c_{0}+\tilde{c}\right)=b_{1}+b_{2} \tilde{c}+b_{3} \tilde{c}^{2}+b_{4} \tilde{c}^{3}, \quad \text { for some } b_{i}.
\tag{1.26}
$$

The equations (1.22) and (1.23) become

$$
\frac{\partial \tilde{c}}{\partial t}=\nabla \cdot\left(M \nabla\left(b_{2} \tilde{c}+b_{3} \tilde{c}^{2}+b_{4} \tilde{c}^{3}-K \nabla^{2} \tilde{c}\right)\right), \quad(1.27)
$$

$$
\int_{v} \tilde{c} \mathrm{~d} v=0,
\tag{1.28}
$$

where

$$
M=M\left(c_{0}+\tilde{c}\right)>0.
$$

While the formulation in terms of the perturbations around the reference concentration $c_{0}$ has simplified the form of the concentration conservation constraint (1.28), the coefficients $b_{i}$ now depend specifically on $c_{0}$. Note that in the formulation, the perturbations $\tilde{c}(x, t)$ have not been assumed to be small, although the free energy has been assumed to be quartic.

The following dimensionless variables are now introduced:

$$
\begin{aligned}
& x^{\prime}=\left[\frac{\left|b_{2}\right|}{K}\right]^{1 / 2} x, \quad t^{\prime}=\frac{M_{0} b_{2}^{2}}{K} t, \\
& c^{\prime}=\frac{\left|b_{4}\right|^{1 / 2}}{\left|b_{2}\right|} \tilde{c}, \quad M^{\prime}(c)=\frac{M\left(c_{0} \tilde{c}\right)}{M_{0}},
\end{aligned}
\tag{1.29}
$$

where $M_{0}=M\left(c_{0}\right)$. (We note that in the new variables, the largest wave-number which grows according to linear theory has been normalized to unity.)

Written in the new variables, but dropping primes, (1.27) and (1.28) become

$$
\partial c / \partial t=\nabla \cdot\left[M(c) \nabla\left[\left(\operatorname{sgn} b_{2}\right) c+B c^{2}+c^{3}-\nabla^{2} c\right]\right],
\tag{1.30}
$$

where $M(c)>0$ and

$$
\int_{v} c \mathrm{~d} v=0.
\tag{1.31}
$$

The influence of the free energy function $f(c)$ now only appears in terms of the parameter $B$, where

$$
B=b_{3} /\left[\left|b_{2}\right| b_{4}\right]^{1 / 2},
\tag{1.32}
$$

and in the sign of $\operatorname{sgn} b_{2}$.

According to common terminology [24], the region designated by $\operatorname{sgn} b_{2}=1$ is subdivided into the "metastable" region and the "stable" region and will be referred to simply as "above the spinodal"; likewise the region designated by $\operatorname{sgn} b_{2}=-1$ is called "unstable" or "subspinodal", see fig. 1. The line where $b_{2}=0$ is called the "spinodal". The line designated by the concentrations at which there exists a double tangent to the free energy curve is called the "binodal".

The source for the terminology "unstable" for the region where $\operatorname{sgn} b_{2}=-1$ can be seen from linear stability theory. The linearized Cahn-Hilliard equation for perturbations $\tilde{c}(x, t)$ around a uniform concentration $c_{0}$ is

$$
\frac{\partial \tilde{c}}{\partial t}=M\left(c_{0}\right) \nabla^{2}\left(\operatorname{sgn} b_{2} \cdot c-\nabla^{2} c\right).
$$

By examining solutions of the form $\mathrm{e}^{\lambda t} \mathrm{e}^{\mathrm{i} k x}$, we obtain the expression for the linear growth rate

$$
-\lambda=M\left(c_{0}\right)\left[k^{4}+\operatorname{sgn} b_{2} \cdot k^{2}\right].
$$

Thus if $\operatorname{sgn} b_{2}=-1$, there exist infinitesimal perturbations which grow, while if $\operatorname{sgn} b_{2}=1$, all infinitesimal perturbations decay. The source of the subdivision of the region above the spinodal into a "metastable" region and a "stable" region will be discussed in section 3.2. For simplicity (1.30) will be referred to as the *Cahn-Hilliard equation for perturbations* (despite the fact that rescaling was not introduced by Cahn and

Hilliard) and will be written finally as

$$
\partial c / \partial t=\nabla \cdot\left[M(c) \nabla\left[ \pm c+B c^{2}+c^{3}-\nabla^{2} c\right]\right],(1.33)
$$

where the $\pm$ sign will be understood to determine the appropriate sign of $b_{2}$ in (1.33).

In any given physical system $M(c)$ and $B$ may in fact be highly temperature and pressure dependent. However if we consider an ideal system which is quenched infinitely fast to some final conditions and then maintained at these conditions, then the entire phase separation process will proceed at fixed temperature and pressure, and time vari- ations of these external parameters will not play a role in the evolution of the system. However, in any realistic physical system quenches are carried out during some finite period of time and the onset of phase separation actually begins before the final quench conditions are reached. Thus the para- metric dependence on pressure and temperature becomes important. This effect is partially ac- counted for in section 3 by allowing the parameter $B$ to be time dependent.

### 1.7. The role of fluctuations
For a review of alternative approaches to spin- odal decomposition, see [25]. There it will be seen that most of the recent descriptions of spinodal decomposition have expressly included the influence of statistical fluctuations in the basic formulation.

It is possible that fluctuations critically influence the system at all times. (This is thought to be true at $(T_{\text{crit}}, c_{\text{crit}})$, but our primary concern is not with behavior near the critical point.) Even so, a study of the underlying deterministic equation serves to consolidate understanding of the influence of fluctuations. For example, it has been suggested by Kawasaki et al. [26] that solutions of the under- lying deterministic equations may serve as the basis for developing an approximate description of the behavior of systems in which fluctuation effects are included.

Another possibility has been put forward [26,27], that the neglect of fluctuations may only be crucial in describing the solution of a system at specific times, namely initially and when the system approaches a global or local free energy minimum. If this is the case, then it is possible to use the deterministic equation throughout the greater part of the evolution of the system, and to introduce fluctuation effects only when necessary.

Often awareness of the effects of fluctuations when they are critical allows one to analyze the behavior of a system without formally including a fluctuation term. Even the simplest linear theories take fluctuations into account at least partially by examining the effects of perturbations on the stability of equilibrium states.

### 1.8. Cahn-Hilliard in biology and in ecology
We note that the Cahn-Hilliard equation has recently been employed in contexts other than that of spinodal decomposition. See for example ref. 28, where this equation appears in connection with non-linear stability phenomena for equations de- scribing slime mold aggregation via chemotaxis. See also ref. 29 where a nonlinear growth inter- action has been added to the Cahn-Hilliard equa- tion in order to describe interaction and diffusion in ecology.

## 2. Determination of the one-dimensional equi- librium solutions
### 2.1. Introduction
In this section, the one-dimensional equilibrium solutions of the unconstrained Cahn-Hilliard equation will be developed explicitly.

### 2.2. Statement of the problem
Since, by hypothesis,

$$
J=-M(c)\left[\nabla\left(\frac{\partial f}{\partial c}-\nabla^{2} c\right)\right], \tag{2.1}
$$

in the one-dimensional case with a quartic free energy

$$
J=-M(c)\left( \pm c+B c^{2}+c^{3}-c_{xx} \right)_x. \tag{2.2}
$$

At equilibrium, $J=0$; since $M(c)>0$, (2.2) yields

$$
0=\left( \pm c+B c^{2}+c^{3}-c_{xx} \right)_x. \tag{2.3}
$$

Integrating, we obtain

$$
c_{xx}=\pm c+B c^{2}+c^{3}-\gamma, \tag{2.4}
$$

where $\gamma$ is a constant.

To interpret (2.4) we recall the generalized chemical potential discussed in section 1.5

$$
G(c)=\frac{\partial f}{\partial c}-\nabla^{2} c. \tag{2.5}
$$

In the one-dimensional case where the free energy is a quartic polynomial, this generalized potential written in the notation of section 1.6 reduces to

$$
G(c)=\pm c+B c^{2}+c^{3}-c_{xx}. \tag{2.6}
$$

Thus, (2.4) is equivalent to

$$
G(c)=\gamma. \tag{2.7}
$$

In other words, equilibrium solutions correspond to those configurations whose generalized chemical potential is spatially uniform.

In addition physical solutions will be required to satisfy the composition conservation condition

$$
\int_{0}^{L} c(x ; \gamma, L) \mathrm{d} x=0, \tag{2.8}
$$

where $L$ is the length of the spatial domain.

We will now adopt the convention that $c(x)$ will be called an *equilibrium solution* if it satisfies both (2.4) and (2.8); if $c(x)$ satisfies (2.4) but it is not clear whether or not it satisfies (2.8), it will be denoted an *unconstrained solution*.

The imposed boundary conditions will depend slightly on the type of region under consideration. For finite regions, $0 \leqslant x \leqslant L$, the natural boundary conditions

$$
c_x(0 ; \gamma)=c_x(L ; \gamma)=0 \tag{2.9}
$$

will be imposed. We observe that if $c(x)$ is any continuous periodic solution with period equal to the interval length $L$ and if $c(x)$ satisfies the composition constraint (2.8) on the interval $L$, then $c(x)$ can be made to satisfy the boundary conditions. This is true since from continuity and from the composition constraint there must exist a point $\hat{x}$ such that $c_x(\hat{x})=0$. By translating our axis such that $x \to x-\hat{x}$, we obtain a solution that satisfies the boundary conditions (2.9).

On infinite regions it is thus natural to consider both those solutions which are periodic with some period $L$ and which satisfy (2.8) over the length of one period and also those solutions which satisfy (2.9) in the limit

$$
\lim_{L \to -\infty} c_x(L ; \gamma)=\lim_{L \to \infty} c_x(L ; \gamma)=0 \tag{2.10}
$$

and which satisfy the conservation constraint

$$
\lim_{L \to \infty} \int_{-L}^{L} c(x) \mathrm{d} x=0 \tag{2.11}
$$

instead of (2.8).

### 2.3. The equilibrium solutions

By multiplying (2.4) by $c_x$ and by integrating once more it is possible to express the resulting first order differential equation in integral form. By reduction to standard form and introduction of Cayley's transformation [30], one can express the resulting integral in terms of Jacobian elliptic functions. We find by this approach that (2.4) yields both a family of bounded periodic solutions and a bounded nonperiodic

solution. The family of periodic solutions is given by
$$
c\left(x ; C_{1}, C_{2}\right)=\frac{\alpha-C_{2}^{1 / 2} \beta \phi}{1-C_{2}^{1 / 2} \phi}, \tag{2.12}
$$
where
$$
\phi=\operatorname{sn}\left[f x, C_{1} C_{2}\right], \quad 0<C_{2}<1, C_{1}>1,0<C_{1} C_{2}<1 ;
$$
$$
\left(\begin{array}{l}
\alpha \\
\beta
\end{array}\right)=-\frac{1}{3} B \pm\left(\begin{array}{c}
-2 C_{2}+1+C_{1} C_{2} \\
2 C_{1}-1-C_{1} C_{2}
\end{array}\right)\left[\frac{\frac{1}{3} B^{2}-\operatorname{sgn} b_{2}}{\left(1+C_{1} C_{2}\right)^{2}-12 C_{1} C_{2}+2\left(C_{1}+C_{2}\right)\left(1+C_{1} C_{2}\right)}\right]^{1 / 2} \tag{2.13}
$$
and
$$
\gamma=\frac{(B / 3)\left(\alpha^{2}+4 \alpha \beta+\beta^{2}\right)+(\alpha+\beta)\left(\operatorname{sgn} b_{2}+\alpha \beta\right)}{2}, \tag{2.14}
$$
$$
L^{2}=\frac{4 K^{2}(k)}{f^{2}}=\frac{8 K(k)\left(1+k^{2}\right)}{\left[\operatorname{sgn} b_{2}+B(\alpha+\beta)+3 \alpha \beta\right]}. \tag{2.15}
$$

We remind the reader that the Jacobian elliptic function sn is actually a one-parameter family of functions, dependent on a parameter which is usually denoted by $k^{2}$. The value of $k^{2}$ is given here by the second expression in the formula for $\phi$ in (2.13), $k^{2}=C_{1} C_{2}$. We thus note that both $k^{2}$ and the period $L$ depend on $C_{1}$ and $C_{2}$. There is also a dependence on the parameter $B$, although we sometimes do not write this explicitly.

The sign of $B$ depends on whether the original concentration $c_{0}$ contained more of the first or of the second component. We observe here that it follows from (2.12) and (2.13) and from the periodicity of the Jacobian elliptic functions that $c\left(x ; B, k^{2}\right)=-c\left(x+x_{0} ;-B, k^{2}\right)$ for some $x_{0}$. Thus there is a one to one correspondence between the periodic equilibrium solutions for $B$ and $-B$. Hence we can limit our consideration to $B \geqslant 0$ without loss of generality.

The function $L=L\left(C_{1}, C_{2}\right)$ defined in (2.15) provides the period which corresponds to the function $c\left(x ; C_{1}, C_{2}\right)$. The functional dependence (2.8) determines which values the parameters $C_{1}$ and $C_{2}$ (or equivalently $C_{2}$ and $k^{2}$ ) may assume, and hence which values $\gamma$ and $L$ may assume. Evaluation of the functional dependence will be treated in the next section. Here we merely note that, given an initial homogeneous concentration $c_{0}$ and given $B$, then for an interval of fixed length $L$ there is a sequence of possible periods which will fit into the interval an integral number of times. Thus, given the initial concentration $c_{0}$ and the region dimensions, a certain subset of the solutions $c\left(x ; B, k^{2}\right)$ satisfies both the boundary conditions (2.9) and the conservation constraint (2.8).

In addition to the family of periodic solutions, for every value of $B$ there is also a nonperiodic solution
$$
c(x)=-\frac{B}{3} \pm\left(\frac{\sqrt{B^{2}}}{3}-\operatorname{sgn} b_{2}\right)^{1 / 2} \tanh \left[\left(\frac{B^{2}}{3}-\operatorname{sgn} b_{2}\right)^{1 / 2} \frac{x}{\sqrt{2}}\right]. \tag{2.16}
$$

This is Van der Waal's tanh solution [8] which corresponds to complete separation into two phases. Note that (2.16) is obtainable from the class of solutions (2.12) by taking $k^{2} \rightarrow 1, C_{2} \rightarrow 0$. We observe that (2.16) satisfies the boundary conditions for infinite regions (2.10) but does not satisfy the boundary conditions for finite regions (2.9) (although the error is exponentially small). We observe, moreover, that (2.16) is capable of satisfying the conservation constraint (2.8) on any finite interval $[0, L]$ by making the appropriate transformation $x \rightarrow x+x_{0}$, however the conservation constraint for infinite regions (2.11) is not satisfied by any such transformation if $B \neq 0$. Thus strictly speaking, (2.16) is not an admissible equilibrium solution for $B \neq 0$.

### 2.4. The functional dependence $C_{2}=C_{2}(k^{2})$

Imposition of the composition conservation constraint on the family of unconstrained equilibrium solutions (2.12) causes $C_{2}$ to be dependent upon $C_{1}$ and hence upon $k^{2}=C_{1}C_{2}(k^{2})$. However the nature of the dependence dictated by (2.8) makes it difficult to express $C_{2}=C_{2}(k^{2})$ explicitly. Hence we obtained the explicit relationship by numerical and analytic approximations. See fig. 2, for a numerically calculated graph of the function $C_{2}=C_{2}(k^{2})$ for various values of $B$.

From the numerical calculations, we know that beneath the spinodal ($\text{sgn }b_{2}=-1$) solutions exist for all values of $k^{2}$. The calculations beneath the spinodal for $k^{2}\ll1$ have also been checked against an expansion about $k^{2}=0$ [25] (appendix B1).

From fig. 2 we can see that above the spinodal ($\text{sgn }b_{1}=1$), non-trivial solutions only exist for $k^{2}$ near 1. It is also clear from fig. 2 that despite the fact that unconstrained solutions exist above the spinodal for $3\leqslant B^{2}\leqslant\infty$, constrained solutions do not appear to exist throughout this whole parameter region. This is also verifiable directly as follows.

![](./images/812446132159381505_2.jpg)

Fig. 2. The expression (2.8) has been calculated for $0.0001\leqslant C_{2}\leqslant1.00$ and $0.00\leqslant k^{2}\leqslant0.997$. Each iso-level corresponds to a $C_{2}-k^{2}$ line of parameters satisfying the conservation constraint for some value of $B^{2}$ above or below the spinodal. The left-most lines correspond to $B^{2}\ll1$, below the spinodal. The right-most lines correspond to $B^{2}$ near 4.5, above the spinodal. Above the spinodal $C_{2}=C_{2}(k^{2})$ is double valued.

The conservation constraint above the spinodal (2.8) may be written as
$$
\begin{aligned}
& \frac{-B / 3}{\sqrt{B^{2} / 3-1}}=\beta_{0}+\left(\alpha_{0}-\beta_{0}\right) \frac{1}{4 K\left(k^{2}\right)} \\
& \quad × \int_{0}^{4 K\left(k^{2}\right)} \frac{\mathrm{d} y}{\left[1-C_{2}^{1 / 2} \operatorname{sn}(y, k)\right]},
\end{aligned}
$$
where $\beta_{0}=\beta(B^{2}=0)$ and $\alpha_{0}=\alpha(B^{2}=0)$. As $B^{2}\to3$, the integral quantities multiplying $(\alpha_{0}-\beta_{0})$ in (2.16) are bounded except possibly in the limit $C_{2}\to1$. By expanding the right-hand side of (2.17) in the neighborhood of $C_{2}=1$, it is possible to show that there is no divergence in this limit ([25], appendix B2). Thus there exists a region $3<B_{\min}^{2}\leqslant B^{2}\leqslant\infty$ in which the conservation constraint is satisfied. Since the left hand side of (2.17) increases monotonically with $B$, it is possible to locate $B_{\min}^{2}$ by locating the minimum value of the right-hand side of (2.17). By numerical estimates we found in this manner that as $C_{2}\to1$, $k^{2}\to1$, $B^{2}\to B_{\min}^{2}=4.5$.

In section 3 it will be demonstrated that $B^{2}=4.5$ demarcates the classical binodal curve. Thus while unconstrained solutions do exist beyond the binodal in the "stable" region of fig. 1, constrained solutions do not. Thus the inclusion of the gradient term does not bring about the existence of non-trivial equilibrium solutions beyond the binodal.

An important observation is that the limiting values $k^{2}\to1$ and $C_{2}\to1$ which give the Van der Waal's solution turn out to be limiting members of the continuous range of parameters $C_{2}(k^{2})$ only for the case $B^{2}=0$. From fig. 3, it is clear that as $k^{2}\to1$, there exist solutions which approach the binodal concentrations, or "complete phase separation". Upon examination of fig. 2, it is seen that as $k^{2}\to1$, there is $C_{2}-k^{2}$ dependence (on the upper branch, above the spinodal) which behaves as $k^{2}=1-\epsilon_{1}$, $C_{2}=k^{2}(1-\epsilon_{2})$ where $\epsilon_{1}\ll\epsilon_{2}$. Expansion of the periodic solution (2.12)-(2.15) in terms

![](./images/812446132159381505_3.jpg)

![](./images/812446132159381505_4.jpg)

![](./images/812446132159381505_5.jpg)

![](./images/812446132159381505_6.jpg)

Fig. 3. Periodic equilibrium solutions below the spinodal at (a) $B=0.5$, (b) $B=4.5$, (c) $B=10.0$, and above the spinodal at (d) $B=4.5$, see inset. In all the figures the amplitude appears to increase monotonically with $k^{2}$, and as $k^{2} \rightarrow 1$ the solutions are seen to approach the completely phase separated solution (2.16). In general, the longer period solutions correspond to larger values of the parameter $k^{2}$. In (a) and (b) (low values of $B^{2}$, below the spinodal) the solutions appear relatively symmetric and rounded as compared to the remaining figures. In (c)-(d) there appear to be two different kinds of solutions with the same period. This arises from the fact that $C_{2}=C_{2}(k^{2})$ is double valued for those parametric regions.

of these asymptotics shows that a non-periodic solution, bounded by the binodal concentrations is approached. The limiting solution is, in fact, identical to the tanh solution (2.16).

### 2.5. The nature of the one-dimensional solutions

Once the $C_{2}=C_{2}(k^{2})$ dependence is known, it is easiest to determine the nature of the solutions by graphing them numerically, see fig. 3.

We wish first to verify that our equilibrium solutions are indeed positive. If we assume that our model is based on a well behaved free energy such that the binodal concentrations (i.e., those concentrations at which there exists a double tangent to the free energy curve) are positive, then it suffices to demonstrate that our solutions remain bounded from above and below by $\tilde{c}_{\mathrm{A}}$ and $\tilde{c}_{\mathrm{B}}$, the binodal concentrations. It is easily shown ([25], section 4.8)

that

$$
\tilde{c}_{\mathrm{A}}=-\frac{B}{3}+\sqrt{\frac{B^{2}}{3}-\operatorname{sgn} b_{2}},
$$

$$
\tilde{c}_{\mathrm{B}}=-\frac{B}{3}-\sqrt{\frac{B^{2}}{3}-\operatorname{sgn} b_{2}}.
$$

The values $\tilde{c}_{\mathrm{A}}$ and $\tilde{c}_{\mathrm{B}}$ are depicted in fig. 4, and appear as the demarcated upper and lower bounds on the solutions in fig. 3.

From knowledge of the dependence $C_{2}=C_{2}(k^{2})$ and of the dependence (2.15) of the period on $C_{2}$ and $k^{2}$, it is possible to determine the range of possible periods available for fixed $B$. Beneath the spinodal, for small values of $B^{2}$ (see fig. 3a), the period increases monotonically with $k^{2}$; the smallest possible period is non-zero and occurs at $k^{2}=0$. As can be seen from fig. 2, at high values of $B^{2}$ below the spinodal and at all values of $B^{2}(>4.5)$ above the spinodal, $C_{2}(k^{2})$ is double valued. This double valuedness can be seen clearly in fig. 3d where two different forms of solutions are depicted. One set appears highly asymmetric and fairly reminiscent of a phase-separated matrix of "pores" and "walls". The other set looks more symmetric and rounded and has an amplitude which decreases with increasing $k^{2}$. In both cases the period increases monotonically with $k^{2}$ for $k^{2} \approx 1$, and in both cases there is a minimum period, which is non-zero for $B^{2} \neq 0$. Thus we see that for any sufficiently large finite interval $[0, L]$, there exists a finite sequence of solutions which satisfy the boundary conditions (2.9).

We note here that it is also easy to see by evaluating the period from (2.15) at $B^{2}=4.5$ above the spinodal in the limit that $C_{2} \to 1, k^{2} \to 1$, that the period diverges as $B^{2} \to B_{\min }^{2}=4.5$. This clarifies an additional aspect of the singular behavior of the value $B^{2}=4.5$. The divergence of the period will be discussed again, in a slightly different context, in the next section.

From fig. 3, we observe that for large $B^{2}$, the solutions look much the same above and below the spinodal. Evaluation of the amplitude of (2.12) for the appropriate parametric values shows that it is singular as $B^{2} \to \infty$, sgn $b_{2}= \pm 1$; i.e., as the spinodal is approached from either above or below the spinodal. This singularity however, results from the singularity of the rescaling factor (1.29), and will not appear when our solutions (2.12) are written in the original variables, if $\partial^{4} f(c_{0}) / \partial c^{4}$ does not vanish. It thus appears that the equilibrium solutions vary smoothly across the spinodal.

Descriptions of one-dimensional equilibrium solutions of the Cahn-Hilliard equations have appeared previously. Langer [8] has discussed the solutions for the symmetric case $B^{2}=0$. Numerical schemes have been used to run the Cahn-Hilliard equation forward in time by Bortz [27] (symmetric case) and deFontaine [31] (non-symmetric cases), among others [32]. These numerical schemes are inherently initial value dependent and may thus be reaching a certain subclass of all possible solutions. Here all possible equilibrium solutions have been designated simultaneously. Of course, determination of which equilibrium solutions will actually appear physically depends on the relative stability of the various solutions.

![](./images/812446132159381505_7.jpg)

Fig. 4. A quartic free energy. The binodal concentrations $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$ lie on a common tangent. Here $c_{i}=c_{0}+\tilde{c}_{i}$.

### 2.6. Stability

An account of the stability of these solutions will be given in a later paper. We remark here that linear stability theory leads to a fourth order non-self-adjoint equation for the perturbations $\tilde{c}(x, t)$ about any equilibrium solution $\bar{c}(x)$:

$$
\frac{\partial \tilde{c}}{\partial t}=\nabla\left[M(\bar{c}) \nabla\left(\left[ \pm 1+2 B \bar{c}+3 \bar{c}^{2}\right] \tilde{c}-\nabla^{2} \tilde{c}\right)\right],(2.18)
$$

with natural and no-flux boundary conditions

$$
\left.J(\text{linearized})\right|_{\text{boundary}}=0,\qquad \left.\frac{\partial c}{\partial n}\right|_{\text{boundary}}=0,
$$

and the constraint $\int_{v} \tilde{c}(\boldsymbol{x}, t) \mathrm{d} v=0$.

Alternative stability criteria arise for the Cahn-Hilliard equation from the underlying generalized free energy $F(c(\boldsymbol{x}, t))$. First, the generalized free energy serves as a Liapounov functional for the Cahn-Hilliard equation [8, 25]:

$$
\frac{\mathrm{d} F}{\mathrm{~d} t} \leqslant 0. \tag{2.19}
$$

Moreover, the second variational problem yields an associated eigenvalue problem for any equilibrium solution $\tilde{c}(\boldsymbol{x})$:

$$
-\nabla^{2} \eta+\left[ \pm 1+2 B \tilde{c}+3 \tilde{c}^{2}\right] \eta=\sigma \eta, \tag{2.20}
$$

with

$$
\left.\frac{\partial \eta}{\partial n}\right|_{\text{boundary}}=0 \quad \text{and} \quad \int_{v} \eta(\boldsymbol{x}) \mathrm{d} v=0.
$$

Here if the smallest eigenvalue is positive (non-negative), then $\tilde{c}(\boldsymbol{x})$ is a strong (weak) relative minimum.

Langer [8] considers solutions of the form $\tilde{c}(\boldsymbol{x}, t)=A(\boldsymbol{x}) \mathrm{e}^{\lambda t}$ to eq. (2.18) where the mobility is assumed to be constant, and discusses the eigenvalue problem for the equation

$$
\lambda A=M \nabla^{2}\left(\left[ \pm 1+2 B \tilde{c}+3 \tilde{c}^{2}\right] A-\nabla^{2} A\right), \tag{2.21}
$$

with periodic boundary conditions. He proceeds to demonstrate that if a certain set of conjugate functions $\{w_{i}\}$ exist to the set of eigenfunctions $\{v\}$ of (2.21)

$$
\nabla^{2} w_{i}=v_{i}, \tag{2.22}
$$

then the smallest eigenvalue of (2.21) is bounded from above by the eigenvalues of (2.20) (with periodic boundary conditions) times a positive quantity. Hence (2.21) has negative eigenvalues if (2.20) has negative eigenvalues. Satisfaction of the conservation constraint by the eigen-functions must be considered here separately.

It turns out that when natural and no flux boundary conditions are considered (for $M=$ constant) instead of periodic boundary conditions, Langer's demonstration may be rigorized. If we limit our consideration to those eigenfunctions $\{v_{i}\}$ of (2.21) which satisfy the conservation constraint on a region $V$ which is assumed to have smooth boundaries,

$$
\int_{v} v_{i} \mathrm{~d} v=0. \tag{2.23}
$$

Then the question of the existence of conjugate functions $\{w_{i}\}$ which satisfy the natural boundary conditions is equivalent to the question of the existence of solutions of the Neumann problem for the Laplace operator for which (2.23) is a necessary and sufficient condition [33]. Indeed, because of the extra degree of freedom inherent in the Neumann problem, the conjugate functions may also be made to satisfy the conservation constraint. The rest of the proof follows as in Langer [8]. Thus stability can be essentially determined from the Liapounov functional and from the associated eigenvalue problem, without further reference to the fourth order non-self-adjoint equation (2.18).

## 3. Estimates on the limit of monotonic global stability

### 3.1. Introduction

In this section, the limit of monotonic global stability is estimated. By definition, beyond the limit of monotonic global stability, all perturbations to the homogeneous solution $c(x)=c_{0}$ decay; the homogeneous solution is the only stable solution. Inside the limit of monotonic global

stability there exists some perturbation to the homogeneous solution which initially grows.

Here, the limit of monotonic global stability will be estimated by an energy criterion. The knowl- edge of the nature and existence of one dimen- sional equilibrium solutions will be critical in the evaluation. It is to be noted that the result will be three dimensional, despite the fact that one dimen- sional solutions are used in its determination. Certain assumptions as to the nature of the mobil- ity function will be required.

It will be shown that if the free energy can be expressed as a quartic polynomial in the concen- tration, then the binodal curve (which distinguishes between the stable and the metastable-unstable regions in classical thermodynamics where gra- dient terms are not taken into account) lies within the limit of monotonic global stability. Further- more, the evaluation of the limit of monotonic global stability (i) gives an estimate on the rate of perturbation decay in the unstable region, (ii) provides reason to conjecture an "excitable" re- gion in which there exist growing fluctuations but in which the only equilibrium solution is the uniform homogeneous state, and (iii) indicates the existence of periodic instabilities throughout the metastable region.

### 3.2. Classical determination of the binodal
In classical thermodynamics the homogeneous solution $c(x) \equiv c_{0}$ is considered to be stable if there does not exist a two-phase configuration whose total free energy (without gradient terms) is lower than the total free energy of the homo- geneous solution. If such a two phase configuration with lower free energy does exist, the original homogeneous solution is considered to be metastable or unstable, depending on whether a finite or infinitesimal concentration change is nec- essary to provide a lower free energy.

We are interested here in the case when the free energy is of the general form depicted in fig. 4. (See section 1.3). Consider two types of points, those such as $c_{1}$ which lie between the common tangent concentrations $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$, and those such as $c_{2}$ which lie outside $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$. Let any volume $V$ of concen tration $c_{1}$ be divided into two volumes $V_{\mathrm{a}}$ and $V_{\mathrm{b}}$ and concentrations $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$, where

$$
V_{\mathrm{A}}=V\left(\frac{c_{\mathrm{b}}-c_{1}}{c_{\mathrm{b}}-c_{\mathrm{a}}}\right), \quad V_{\mathrm{B}}=V\left(\frac{c_{1}-c_{\mathrm{a}}}{c_{\mathrm{b}}-c_{\mathrm{a}}}\right). \tag{3.1}
$$

The conservation laws $V_{\mathrm{A}}+V_{\mathrm{B}}=V$ and $c_{\mathrm{A}} V_{\mathrm{A}}+c_{\mathrm{B}} V_{\mathrm{B}}=c_{1} V$ imply that the free energy of the combined volumes $V_{\mathrm{A}}$ of $c_{\mathrm{a}}$ and $V_{\mathrm{B}}$ of $c_{\mathrm{b}}$ will be less than that of the original volume $V$ of $c_{1}$ if

$$
V\left[\left(\frac{c_{\mathrm{b}}-c_{1}}{c_{\mathrm{b}}-c_{\mathrm{a}}}\right) f\left(c_{\mathrm{a}}\right)+\left(\frac{c_{1}-c_{\mathrm{a}}}{c_{\mathrm{b}}-c_{\mathrm{a}}}\right) f\left(c_{\mathrm{b}}\right)\right]<V f\left(c_{1}\right). \tag{3.2}
$$

Eq. (3.2) indicates that the expression in the square brackets corresponds to a point in fig. 4 located on the common tangent, which lies totally below $f(c_{1})$ for all $c_{1}$.

Let $c_{2}$ be a concentration that lies outside the interval $(c_{\mathrm{a}}, c_{\mathrm{b}})$. If a volume of concentration $c_{2}$ is subdivided, the resulting free energy will be greater than that of the original undivided volume. Hence, the double tangent points define the binodal limit.

By similar arguments it can be shown that if $c_{1}$ is between the points of inflection of $f(c)$ then one does not have to employ the extreme concen- trations $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$ to provide a lower free energy - an infinitesimal change suffices. Thus the inflection points demarcate the spinodal. This is in conformity with remarks made in section 1.6.

### 3.3. Determination of the limit of monotonic global stability
We will now characterize the limit of monotonic global stability for the Cahn-Hilliard equation on a finite region. Since it is desirable to consider the limit of monotonic global stability on an infinite region for the sake of comparison with the classical binodal where finite volume effects are not conventionally

taken into account, the definition will later be appropriately generalized for the infinite region case.

Closed finite regions will be considered, i.e. we will require
$$\left.J\right|_{\text{boundary}}=0.\tag{3.3}$$

The natural boundary conditions discussed in section 1 will also be enforced:
$$\left.\frac{\partial c}{\partial n}\right|_{\text{boundary}}=0.\tag{3.4}$$

The mobility function will be assumed to be a positive non-increasing function of $|c|$ such that
$$\frac{1}{M^{2}(c)}\left(\frac{\mathrm{d} M}{\mathrm{~d} c}\right)^{2}<12 ;\tag{3.5}$$
i.e., $M(c)$ will be non-increasing and
$$M(c) \geqslant M(0) \exp (-\sqrt{12}|c|).$$

The factor 12 arises from an approximation used in proving theorem 3.1, stated below. Enhanced generality will be obtained here by considering the parameter $B$ to be time dependent even when not specifically indicated. As mentioned in section 1, situations where phase separation is somewhat dependent on the manner of cooling can be partially accommodated by including time dependence in the parameter $B$.

In the region below the spinodal, we have demonstrated (as in [10]) that the homogeneous solution $c(x) \equiv c_{0}$ is unstable to infinitesimal perturbations. Hence the limit of monotonic global stability must lie in the region above the spinodal, where eq. (1.33) holds with a positive sign.

The following theorem allows us to provide a mathematical characterization of the limit of monotonic global stability $\bar{B}(L)$. We will consider regions $R_{L}$, where $R_{L}$ is a three dimensional cube of side $L$.

Theorem 3.1. For any given region $R_{L}$, if $c$ is a solution of (1.33), we define $\bar{B}(L)$ by
$$
\begin{aligned}
\frac{1}{\bar{B}(L)} & =\sup _{t \geqslant 0} \max _{c \in H(L)} \frac{-\operatorname{sgn} B \int_{R_{L}} M(c)\left(2 c(\nabla c)^{2}\right) \mathrm{d} v}{\int_{R_{L}} M(c)\left[\left(1+3 c^{2}\right)(\nabla c)^{2}+\left(\nabla^{2} c\right)^{2}\right] \mathrm{d} v} \\
& =\sup _{t \geqslant 0} \max _{c \in H(L)} \frac{[\text { production terms }]}{[\text { dissipation terms }]}.
\end{aligned}\tag{3.6}
$$

Here the class $H(L)$ of admissible $c(x, t)$ will be the closure of the set of all smooth functions that satisfy the composition conservation constraint and boundary conditions (3.3) and (3.4). For $B^{2}<\bar{B}^{2}(L)$ in the region above the spinodal, the "energy" $\epsilon(t)$ of all perturbations $c(x, t)$
$$\epsilon(t) \equiv \int_{R_{L}} \frac{1}{2} c^{2} \mathrm{~d} v\tag{3.7}$$
decays since
$$\epsilon(t) \leqslant \epsilon(0) \exp \left\{-\frac{2 \hat{\Lambda}}{L^{2}} \int_{0}^{t}\left(1-\frac{|B(\tau)|}{\bar{B}(L)}\right) M(\bar{c}(\tau)) \mathrm{d} \tau\right\},\tag{3.8}$$

for some $\hat{\Lambda} \geqslant 2 / 3$, where $M(\tilde{c}(t))$ is the mobility evaluated at some $c(x(t), t)$. Furthermore if $B^{2}(0)>\bar{B}^{2}(L)$, then there exists an admissible initial perturbation $c(x, t)$ such that $\mathrm{d} \epsilon / \mathrm{d} t>0$ at $t=0$.

The method of proof is similar to that given in Joseph [34]. For details, see [25], appendix Cl. Note that if $B^{2}<\bar{B}^{2}(L)$ for all $t$, then all non-zero perturbations decay monotonically to zero and that for $B^{2} \geqslant \bar{B}^{2}(L)$ there exist non-zero perturbations whose energy grows initially. Note also that if the mobility is constant or bounded away from zero then the decay given by (3.8) is actually exponential and a lower bound on the rate of exponential decay can be specified.

Using the definition of $\bar{B}^{2}(L)$. in theorem 3.1 we will now prove that if $\bar{B} \equiv \lim _{L \rightarrow \infty} \bar{B}(L)$, then $4.5 \geqslant \bar{B}^{2} \geqslant 3.0$. Furthermore the classical binodal which corresponds to a quartic polynomial free energy will be shown to lie within the limit of monotonic global stability. Weaker results are given for finite regions. Several lemmas are required.

Lemmas 3.1. Let $R_{L}$ denote a cube whose sides are of length $L$. For any $B^{2} \geqslant 4.5$, there exists a length $L^{*}(B)$ such that for any region $R_{L}$ with $L>L^{*}(B)$, there exists at least one sufficiently smooth equilibrium solution of the Cahn-Hilliard equation which satisfies the boundary conditions (3.3) and (3.4) in the region $R_{L}$.

Proof. From the numerical evidence presented in fig. 2, we know that above the spinodal there exists one branch of solutions of the form (2.12). From the expression for the period $L,(2.15)$, and from the definitions of $\alpha$ and $\beta$ given in (2.13), it is clear that the period depends continuously on the parameters $C_{2}, k^{2}$ and $B$. Thus it is possible to define upper and lower bounds on a continuous range of possible periods at a given $B$.
$$0 \leqslant L_{1}(B) \leqslant L \leqslant L_{2}(B) \leqslant \infty.$$

It is then easy to show that if $L>L^{*}(B)$, where
$$L^{*}(B) \equiv L_{1}(B) L_{2}(B) /\left(L_{2}(B)-L_{1}(B)\right),$$
then there exists a solution with period $\hat{L}, \hat{L} \in[L_{1}(B), L_{2}(B)]$ which will fit an integral number of times into the interval $L$. From the remark in section 2.2 it is clear that by appropriate translation of the axis this solution may be made to conform with the natural boundary conditions.

Lemma 3.2. For all regions $R_{L}$, with $L>L^{*}(B)$ (where $L^{*}(B)$ is defined in lemma 3.1) there exists an equilibrium solution $\tilde{c}(x)$ such that
$$\frac{-\operatorname{sgn} B \int_{R_{L}} M(\tilde{c})\left(2 \tilde{c}(\nabla \tilde{c})^{2}\right) \mathrm{d} v}{\int_{R_{L}} M(c)\left[(1+3 \tilde{c})^{2}(\nabla \tilde{c})^{2}+\left(\nabla \tilde{c}^{2}\right)^{2}\right] \mathrm{d} v}=\frac{1}{|B|} ;$$
hence $\bar{B}^{2}(L)<B^{2}$.

Proof. Since by assumption $L>L^{*}(B)$, then according to lemma 3.1 there exists some sufficiently smooth solution $\tilde{c}(x ; B, k^{2})$ of the Cahn-Hilliard equilibrium equation which fits an integral number of times into the interval $L$ and which satisfies boundary conditions (3.3) and (3.4) on $R_{L}$. Hence $\tilde{c}(x ; B, k^{2}) \in H$. By integration by parts of the Cahn-Hilliard equation and use of the boundary conditions it follows that
$$\int_{R_{L}} M(\tilde{c})\left[\left(1+2 B \tilde{c}+3 \tilde{c}^{2}\right)(\nabla \tilde{c})^{2}+\left(\nabla^{2} \tilde{c}\right)^{2}\right] \mathrm{d} v=0.$$

Thus

$$
\begin{aligned}
\frac{1}{\bar{B}(L)} & \geqslant \max _{c \in H}\left[\frac{-\operatorname{sgn} B \int_{R_{L}} M(c)\left(2 c(\nabla c)^{2}\right) \mathrm{d} v}{\int_{R_{L}} M(c)\left[\left(1+3 c^{2}\right)(\nabla c)^{2}+\left(\nabla^{2} c\right)^{2}\right] \mathrm{d} v}\right] \\
& =\max _{c \in H}\left[\frac{-\operatorname{sgn} B \int_{R_{L}} M(c)\left(2 c(\nabla c)^{2}\right) \mathrm{d} v}{\int_{R_{L}} M(\tilde{c})\left[\left(1+2 B c+3 c^{2}\right)(\nabla c)^{2}+\left(\nabla^{2} c\right)^{2}\right] \mathrm{d} v-\int_{R_{L}} M(c)\left(2 B c(\nabla c)^{2}\right) \mathrm{d} v}\right] \\
& \geqslant \frac{-\operatorname{sgn} B \int_{R_{L}} M(\tilde{c})\left(2 \tilde{c}(\nabla \tilde{c})^{2}\right) \mathrm{d} v}{-\int_{R_{L}} M(\tilde{c})\left(2 B \tilde{c}(\nabla \tilde{c})^{2}\right) \mathrm{d} v}=\frac{1}{|B|}.
\end{aligned}
$$

Hence $\bar{B}^{2}(L) \leqslant B^{2}$.

Lemma 3.3. $\bar{B}^{2}(L) \geqslant 3$ for all $R_{L}$.

Proof. If the Cahn-Hilliard equation (for $\operatorname{sgn} b_{2}=1$)
$$
\partial c / \partial t=\nabla \cdot\left[M(c) \nabla\left[c+c^{2}+B c^{2}+c^{3}-\nabla^{2} c\right]\right]
$$
is multiplied by $c(x, t)$, then integration over some region $R_{L}$ yields
$$
\frac{1}{2} \frac{\mathrm{d}}{\mathrm{d} t} \int_{R_{L}} c^{2} \mathrm{~d} v=-\int_{R_{L}} M(c)\left[\left[1+2 B c+3 c^{2}\right](\nabla c)^{2}+\left(\nabla^{2} c\right)^{2}\right] \mathrm{d} v. \tag{3.12}
$$

The discriminant of $\left[1+2 B c+3 c^{2}\right]$ is $2 \sqrt{B^{2}-3}$; thus, since by hypothesis $M(c)>0$ for all $c$, if $B^{2} \leqslant 3$ then the right-hand side of (3.12) will be negative. Therefore, for $B^{2} \leqslant 3$
$$
\frac{1}{2} \frac{\mathrm{d}}{\mathrm{d} t} \int_{R_{L}} c^{2} \mathrm{~d} v<0
$$
for all regions $R_{L}$ and for all perturbations $c(x)$; i.e., all perturbations decay monotonically.

Combining lemmas 3.2 and 3.3, we obtain that for any finite region $R_{L}$
$$
\left\{\operatorname{lub} B^{2} \mid L^{*}(B)<L\right\} \geqslant \bar{B}^{2}(L) \geqslant 3. \tag{3.9}
$$

This shows that the ability to find and fit equilibrium solutions $c(x ; B, k^{2})$ for $B^{2} \geqslant 4.5$ an integral number of times into the interval $[0, L]$ allows a means of determining an upper bound to the limit of monotonic global stability.

For infinite regions it is easy to prove the following result:

Theorem 3.2. $\left\{\operatorname{lub} B^{2} \mid L^{*}(B)<L\right\} \to 4.5$ as $L \to \infty$; i.e. for infinite regions, $4.5 \geqslant \bar{B}^{2} \geqslant 3$.

Lemma 3.3 and the existence of non-homogeneous equilibrium states in the region $B^{2} \geqslant 4.5$ above the spinodal demonstrated explicitly in the previous two sections suffice to demonstrate a result slightly weaker than theorem 3.2, without resorting to use of the "energy" results of theorem 3.1. This weaker result will be called theorem 3.2*:

Theorem 3.2*. On infinite composition conservative regions (i.e. regions $R_{L}$, with no flux through the boundaries and natural boundary conditions, in the limit as $L \to \infty$) the line $B^{2}=4.5$ in the metastable

regions is "binodal" in this limited sense, that if $B^2 > 4.5$ there exist equilibrium configurations other than the homogeneous state, and if $B^2 < 4.5$ there do not.

The primary weakness of this result is that existence of additional equilibrium states is only really convincing evidence that we are in a two-phase region if some degree of stability of these states can be demonstrated. While the energy results do not prove the stability of the additional state, proof that there is a perturbation which initially grows away from the homogeneous state does disprove monotonic global stability of the homogeneous state there, and tends to indicate that the system may be moving towards some new stable state.

### 3.4. Growing perturbations
The question remains, what exactly are those perturbations, on intervals $R_L$, whose energy grows initially in the region above the spinodal where $B^2 > \bar{B}^2(L)$? At least a partial characterization can be given, in the event that $B^2 > \max\{4.5, \bar{B}^2(L)\}$.

For $B^2 > \max\{\bar{B}^2(L), 4.5\}$ and for some length $L > L^*(B)$ (see lemma 3.1), then from continuity of $L^*(B)$ (see appendix C3 of [25]), there exists some $\hat{B}$ close to $B$, such that $B^2 > \hat{B}^2 > \bar{B}^2$ and such that $L > L^*(\hat{B})$. Consequently, by lemma 3.2 there exists an equilibrium solution $\tilde{c}(x)$ such that
$$
\frac{-\operatorname{sgn} B \int_{R_{L}} M(\tilde{c})\left(2 \tilde{c}(\nabla \tilde{c})^{2}\right) \mathrm{d} v}{\int_{R_{L}} M(\tilde{c})\left[1+3 \tilde{c}^{2}\right](\nabla \tilde{c})^{2}+\left(\nabla^{2} \tilde{c}\right)^{2} \mathrm{~d} v}=\frac{1}{|\hat{B}|}.
$$

By theorem 3.1, $\tilde{c}(x)$ can be used as an initial perturbation whose energy will grow at $t=0$.

In other words, given $B^2 > 4.5$ and given a sufficiently large interval so that $B^2 > \max\{B^2(L), 4.5\}$, then those equilibrium solutions which correspond to some $\hat{B}, B^2 > \hat{B}^2 > 4.5$, and which can be fitted into the interval, will initially grow in energy if imposed as a perturbation on a homogeneous solution. Thus, those equilibrium solutions which fit into an interval, but which are associated with a smaller $B$ parameter than that which actually appears, can serve as growing perturbations.

The following lemma allows us to clarify the connection between the limit of monotonic global stability and the binodal curve:

Lemma 3.4. If the free energy can be expressed as a quartic polynomial in the concentration $c(x)$; then $B^2 = 4.5$ at the "binodal", i.e. at the double tangent to the free energy graph (see fig. 4).

The lemma is proved by direct calculation [appendix A]. It follows that for infinite regions, if the free energy is a quartic polynomial in the concentration, then the classical binodal lies within the limit of monotonic global stability.

We emphasize that the connection between the limit of monotonic global stability and the binodal of classical thermodynamics has only been discussed for the case where the free energy can be expressed as a fourth order polynomial. It is to be expected that similar behavior would result for free energies of a more general form.

### 3.5. Effective limits of monotonic global stability for finite regions
From (3.9) we know that for any region $R_L$
$$\left\{\operatorname{lub} B^{2} \mid L^{*}(B)<L\right\} \geqslant \bar{B}^{2}(L) \geqslant 3,$$
i.e. for finite regions $\bar{B}^2(L)$ may actually be larger than $\bar{B}^2$, and parameter domains which are metastable with respect to infinite regions may be absolutely stable with respect to certain finite regions. As all physically realizable regions are indeed

finite, it becomes important to ascertain how large a region must be in order that it be effectively infinite.

From lemma 3.1, we know that $\bar{L}^{*} = \lim_{B^{2} \to 4.5} L^{*}(B)$ is an upper bound on the smallest side length needed to accommodate exactly at least one sufficiently smooth solution of the Cahn-Hilliard equation as $B^{2} \to 4.5$. Thus it follows from lemma 3.2 and 3.3 that for $L \geqslant \bar{L}^{*}$ the limit of monotonic global stability would have the same bounds, $3.0 \leqslant \bar{B}^{2}(L) \leqslant 4.5$, as it does in the case of an infinite region. For $L < \bar{L}^{*}$, weaker estimates are attainable for $\bar{B}^{2}(L)$ from lemma 3.2. Thus $\bar{L}^{*}$ determines the size of an effectively infinite region.

### 3.6. Discussion

Our results may be summarized by fig. 5. The binodal lies at $B^{2}=4.5$. From classical thermodynamics we know that the binodal distinguishes between the stable region and the metastable region when gradient terms are not taken into account. Thus it would not be surprising if part of the stable region is metastable when gradient terms are taken into account. At least partial understanding of stability when gradient terms are included is attainable through analysis of the limit of monotonic global stability.

The limit of monotonic global stability for infinite regions lies between $B^{2}=4.5$ and $B^{2}=3.0$. For $B^{2} \leqslant 3.0$, we know that all perturbations decay monotonically and globally, and that nonequilibrium solutions exist above $B^{2}=4.5$, but not below it. Thus if there does indeed exist a non-void region between $B^{2}=4.5$ and the limit of monotonic global stability, then in this region if an external source of noise is considered, the initial growth of certain perturbations may cause the homogeneous solution to appear chaotic, even though no new equilibrium solution will be attained. Such an intermediary region will be denoted here as the excitable region. If an excitable region did exist, it would indicate that the transition across the binodal is, like the spinodal, a smooth transition. It would also be an indication that the effect of enhancement of fluctuations in the vicinity of the critical point should also be noticeable, although perhaps much more weakly, just outside the binodal, even far from the critical point. Whether or not the limit of monotonic global stability does indeed coincide with the binodal line $B^{2}=4.5$ must be verified by alternative means.

![](./images/812446132159381505_8.jpg)

Fig. 5. The phase diagram. On the right-hand side, the various regions have been labelled. On the left hand side, the various distinguishing lines and their $B^{2}$ values have been indicated. See text for details.

From section 2.5 we know that as the binodal is approached from within, the period of the equilibrium solutions diverges. In sufficiently large regions where these solutions fit, according to section 3.4 they will act as initially growing perturbations. These growing solutions comprise a periodic instability which may be compared to the well known nucleation instability [35, 9]. In the case of the nucleation instability, nuclei with radius $R > R_{\mathrm{c}}$ are shown to grow in the metastable region where the critical radius $R_{\mathrm{c}}$ diverges as the binodal is approached. Although the periodic instabilities demonstrated here to grow at time $t=0$ may only be transients, they do demonstrate that the periodicity or the enhanced regularity of the subspinodal region, may also be realizable in the metastable region under appropriate conditions.

### 4. Summary and final remarks

The Cahn-Hilliard equation with a Landau-Ginzburg free energy and with no Langevin forcing term has been rescaled and then studied using energy methods. The one-dimensional equilibrium solutions of the Cahn-Hilliard equation have been outlined. It

has been demonstrated that while closed form equilibrium solutions exist in and beyond the two-phase metatable region, imposition of the conservation constraint limits the existence of equi- librium solutions to the region below the binodal curve only. At all points within the binodal curve there exists a range of possible equilibrium solu- tions. As the binodal curve is approached from within, the period of the equilibrium solutions diverges, in accord with what one would expect from nucleation theory. The Van der Waal's tanh equilibrium solution is shown to be a limiting member of the continuous range of equilibrium solutions.

A limit of monotonic global stability is pre- scribed for the Cahn-Hilliard equation via an "energy" defined by the integral over the square of the concentration deviation from the underlying uniform concentration. In the formulation of the limit, $B^{2}$ is taken to be time dependent, thus permitting the finite time effects necessary to pro- duce an actual quenched system to be accounted for. Beyond the limit of monotonic global stability, all perturbations to the uniform state decay mono- tonically, whereas within the limit of monotonic global stability there exist initial conditions which will cause the "energy" to grow initially.

Knowledge of the existence of the one- dimensional equilibrium solutions is crucial in determining the limit of monotonic global stability to lie between the binodal curve and the line $B^{2}=3$. The possibility that the limit of monotonic global stability does not coincide with the binodal curve but rather lies beyond it gives rise to the possibility of a narrow "excitable" region just outside the binodal curve (see fig. 5) where an enhancement of the fluctuation level without the appearance of phase separation would signal the proximity of the two-phase region. The actual existence of such a postulated excitable zone could be tested experimentally, or perhaps theoretically by further determination of the location of the limit of monotonic global stability.

Furthermore, within the framework of the dis- cussion of the nature of the limit of monotonic global stability, it was demonstrated that there exists an additional instability other than the nu- cleation instability within the metastable region. This instability, unlike the nucleation instability, is strictly periodic and is obtainable by imposing the equilibrium solutions which correspond to one value of $B^{2}$ on a system which is thermo dynamically at a lower $B^{2}$. It might be possible to induce this instability experimentally, by quench- ing to one value of $B^{2}$, allowing the system to approach equilibrium, and then requenching the system slightly in the opposite direction so that the system will be located thermodynamically within the binodal curve at a lower value of $B^{2}$.

In summary, the present study of the nonlinear deterministic Cahn-Hilliard equation has illu- minated new aspects of spinodal decomposition. A complete picture of the possible one-dimensional equilibrium configurations has been given. The characteristics of the asymmetric cases $B^{2} \neq 0$ have been demonstrated. Introduction of natural boundary conditions has allowed easy proof of a comparison theorem postulated by Langer be- tween the eigenvalues related to linear stability theory and the eigenvalues of an associated eigen- value problem which arose from the existence of a variational principle. Via energy methods and a study of monotonic global stability, the possibility of an excitable region of fluctuations just outside the binodal curve has been conjectured and a new periodic instability in the metastable region inside the binodal curve has been revealed.

### Acknowledgements

Most of this work formed part of the Ph.D. thesis of A.N-C. in the Department of Applied Mathematics, Weizmann Institute, Rehovot, Is- rael. The work of L.A.S. was partially supported by the U.S. Army Research Office.

## Appendix A
### Proof of Lemma 3.4

Suppose that the free energy is quartic in the concentration $\bar{c}(x, t)$. Then it is easy to see (section 1.6) that in terms of the dimensionless perturbation variable $c(x, t)$,

$$
c(x, t) \equiv \left[ \frac{\partial^4 f(c_0)}{\partial c^4} \bigg/ \frac{\partial^2 f(c_0)}{\partial c^2} \right]^{1/2} \left( \bar{c}(x, t) - c_0 \right).
$$

Above the spinodal, the free energy may be written as

$$
\begin{aligned}
f(c) =& \left[ \left( \frac{\partial^2 f(c_o)}{\partial c^2} \right)^2 \bigg/ \frac{\partial^4 f(c_0)}{\partial c^4} \right] \\
& \times \left( D_0 + D_1 c + \frac{1}{2}c^2 + \frac{1}{3}Bc^3 + \frac{1}{4}c^4 \right). \tag{A.1}
\end{aligned}
$$

By definition a concentration pair, $c_1$ and $c_2$, lie on the binodal if they are on a common tangent, namely if

$$
f'(c_1) = f'(c_2) = \frac{f(c_2) - f(c_1)}{c_2 - c_1}. \tag{A.2}
$$

Solution of (A.1) and (A.2) yields

$$
c_1 = \frac{-B}{3} - \sqrt{B^3 / 3 - 1},
$$

$$
c_2 = \frac{-B}{3} + \sqrt{B^2 / 3 - 1}. \tag{A.3}
$$

Suppose $B > 0$. The concentration which was $c_0$ in the old variables is 0 in the new variables. Thus $c_0$ is within the binodal if

$$
c_1 \leqslant 0 \leqslant c_2. \tag{A.4}
$$

From (A.3) it can be seen that $c_1$ is negative real for $B^2 \geqslant 3$, whereas $c_2$ is positive real for $B^2 > 4.5$, and negative real for $4.5 > B^2 \geqslant 3$. Hence (A.4) holds if $\infty \geqslant B^2 \geqslant 4.5$. Thus $B^2 = 4.5$ when $c_0$ lies at the binodal. The case $B < 0$ follows in the same way.

---

## References

[1] D. De Fontaine, Ultrafine-Grain Metals (Syracuse Univ. Press, New York, 1971) p. 93.
[2] Disc. Faraday Soc., 50, (1970).
[3] C.A. Smolders, J.J. van Aartsen and A. Steenbergen, Kolloid-Z u.Z., Polymere 243 (1971) 14.
[4] A.J. Schwartz, J.S. Huang and W.I. Goldberg, Chem. Phys. 62 (1975) 1847.
[5] J.W. Cahn and J.E. Hilliard, J. Chem. Phys. 28 (1958) 258.
[6] L.A. Segel, in: Non-Equilibrium Thermodynamics - Variational Techniques and Stability, R.J. Donnelly, ed. (Chicago Univ. Press, Chicago, 1966).
[7] Y. Kuramoto and T. Yamada, Prog. Theor. Phys. 55 (1976) 643.
[8] J.S. Langer, Annals of Physics (N.Y.) 65 (1971) 53.
[9] I.M. Lifschitz and V.V. Slyozov, J. Phys. Chem. Solids 19 (1961) 35.
[10] J.W. Cahn and J.E. Hilliard, Act. Metall. 19 (1951) 151.
[11] S.R. De Groot and P. Mazur, Non-Equilibrium Thermo- dynamics (North-Holland, Amsterdam, 1962). pp. 35-41.
[12] L.P. McMaster, Macromolecules 6 (1973) 760.
[13] R. Konigsveld and L.A. Kleinntjens, J. Poly. Sci.: Polymer Symposium 61 (1977) 221.
[14] D. Stauffer, Z. Physik 221 (1969) 122.
[15] J.S. Huang, W.I. Goldburg and A.W. Bierkaas, Phys. Rev. Lett., 32 (1974) 921.
A.J. Schwartz, J.S. Huang and W.I. Goldburg, J. Chem. Phys. 62 (1975) 1847.
[16] K. Binder and H. Müller-Krumbhaar, Phys. Rev. B 9 (1974) 2328.
[17] H.E. Stanley, Introduction to Phase Transition and Crit- ical Phenomena (Oxford Univ. Press, New York, 1971).
[18] L.A. Segel, Mathematics Applied to Continuum Mechan- ics (MacMillan, New York, 1977) pp. 43-46.
[19] J.S. Huang and W.W. Webb, J. Chem. Phys. 50 (1969) 3677.
[20] F.F. Abraham, J. Chem. Phys. 69 (1978) 3462.
[21] K. Binder, Z. Physik 267 (1974) 213.
[22] F.F. Abraham, Phys. Rep. 53 (1979).
[23] K.F. Freed and S.F. Edwards, J. Chem. Phys. 65 (1976) 4103.
[24] J.W. Cahn, Trans. A.I.M.E. 242 (1968) 166.
[25] A. Novick-Cohen, Ph.D. Thesis, Dept. of Appl. Math., Weizmann Institute of Science, Rehovot, Israel, 1982.
[26] K. Kawasaki, M.C. Yalabik and J.D. Gunton, Phys. Rev. A 17 (1978) 455.
[27] A.B. Bortz, J. Stat. Phys. 11 (1974) 181.
[28] J.K. Percus and S. Childress, Mathematical Models in Developmental Biology (Lecture Notes) (Courant Inst. New York, 1978), Chapter 21.
[29] D.S. Cohen and J.D. Murray, J. Math. Bio. 12 (1981) 237.
[30] F. Borman, Introduction to Elliptic Functions (English Universities Press, London, 1953).
[31] D. De Fontaine, Ph.D. Thesis (Northwestern University, Evanston, Illinois, 1967).
[32] M. Hillert, Acta Metallurgica 9 (1961) 525.
[33] G.B. Folland, Introduction to Partial Differential Equa- tions (Princeton Univ. Press, Princeton, 1976).
[34] D.D. Joseph, Stability of Fluid Motions I (Springer, Berlin, 1976).
[35] K. Binder, Phys. Rev. B 15 (1977) 4425.
[36] J.D. van der Waals, Verhandel. Konik. Akad. Weten. Amsterdam 1 (1893) No. 8.