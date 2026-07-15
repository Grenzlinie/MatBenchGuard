# Phase-field modeling of the discontinuous precipitation reaction

Lynda Amirouche $^{a,b}$, Mathis Plapp $^{b}$

$^{a}$Laboratoire de Physique Théorique, Faculté de Physique, U. S. T. H. B., BP 32,
El-Alia, BabEzzouar, 16311, Alger, Algeria

$^{b}$Physique de la Matière Condensée, École Polytechnique, CNRS, 91128 Palaiseau,
France

---

## Abstract
A multi-phase-field model for the description of the discontinuous precipitation reaction is formulated which takes into account surface diffusion along grain boundaries and interfaces as well as volume diffusion. Simulations reveal that the structure and steady-state growth velocity of spatially periodic precipitation fronts strongly depend on the relative magnitudes of the diffusion coefficients. Steady-state solutions always exist for a range of interlamellar spacings that is limited by a fold singularity for low spacings, and by the onset of tip-splitting or oscillatory instabilities for large spacings. A detailed analysis of the simulation data reveals that the hypothesis of local equilibrium at interfaces, used in previous theories, is not valid for the typical conditions of discontinuous precipitation.

Key words: phase field modeling, precipitation, grain boundary diffusion, phase transformation kinetics, microstructure
PACS: 81.30.Mh, 64.70.kd, 05.70.Ln

---

## 1 Introduction
The discontinuous precipitation reaction is a solid-state transformation during which a supersaturated mother phase $\alpha_0$ decomposes into a two-phase structure consisting of the depleted $\alpha$ phase and lamellar precipitates of a new phase $\beta$. This reaction takes place at a moving grain boundary, which indicates that the rate-limiting step is the diffusion of solute along grain boundaries and interfaces. The resulting characteristic lamellar microstructure has been observed in a large number of different alloy systems [1].

Numerous theories have been proposed to predict the precipitate growth velocity and the interlamellar spacing as a function of the processing conditions

Preprint submitted to Elsevier
9 November 2018

and the alloy thermodynamics [2,3,4] (see also [1] and references therein), but the direct comparison of these predictions to experimental data is made difficult by the fact that the process is extremely complex and controlled by a large number of parameters which are often not precisely known. In this situation, direct numerical simulations of the discontinuous precipitation reaction can help to reach a better understanding of this phenomenon: if a reasonably realistic model can be investigated in detail, the simulation data can be used to test the theories and to clarify whether their basic assumptions are valid.

The phase-field method, which is by now a well-established simulation tool both in crystal growth and phase transformations [5,6], is ideally suited for this purpose. In phase-field models, the local state of matter is described by one or several order parameters (the phase fields), and interfaces are represented by rapid variations of these fields over a characteristic length scale $W$. By choosing $W$ small enough, all the details on the length scale of the microstructure can be properly treated. The evolution equations for the fields are obtained from the principles of out-of-equilibrium thermodynamics, and therefore only a small number of assumptions is needed to obtain a fully consistent model for discontinuous precipitation. Whereas a closely related phenomenon, the so-called discontinuous spinodal decomposition that takes place at moving grain boundaries, has recently been investigated by a phase-field model [7], to our best knowledge no previous phase-field study of discontinuous precipitation is available.

Here, we develop a phase-field model for the discontinuous precipitation reaction by modifying a recent model for eutectic solidification [8,9]. We use the multi-phase-field approach [10,11,12], in which each phase (or grain) is described by one phase field. We restrict our attention to isothermal growth in a simple binary alloy; extensions of the model to more complicated situations are straightforward.

We then carry out simulations and vary systematically the parameters of the model to investigate under which conditions steady-state growth of spatially periodic lamellar precipitate arrays is possible. In particular, we study the influence of lamellar spacing, alloy composition, and interfacial parameters (surface tensions and surface diffusivities) on the growth velocity. As a guideline, we use insights from a detailed recent sharp-interface model developed by Brener and Temkin [4]. We confirm qualitatively several features predicted by this model, in particular the importance of the contact angles between the interfaces at the trijunction point and the decisive role of solute diffusion along the interphase boundaries behind the growth front. However, the values of the precipitate growth velocity obtained from our simulations do not agree with the theoretical predictions, and the shape of the velocity-vs-spacing curves obtained here strongly differs from the ones obtained in Ref. [4]. A detailed analysis of the simulation data reveals the main reason for this discrepancy:

the local equilibrium hypothesis used in the sharp-interface models is not valid for diffuse interphase boundaries in the presence of strong surface diffusion. We believe that this effect is generic, and we develop a criterion that clarifies under which conditions it becomes important.

We also observe a new instability that occurs for large spacings and leads to oscillatory growth, reminiscent of the oscillatory patterns found in eutectic solidification [13,14]. This could be related to the "stop and go" motion of discontinuous precipitation cells observed in several alloy systems [1].

The remainder of this paper is organized as follows: in Sec. 2, we present the phase-field model and relate its parameters to the ones used in conventional sharp-interface theories. In Sec. 3, we give a few details about our simulation procedures. Results are presented in Sec. 4, followed by a discussion in Sec. 5 and a conclusion in Sec. 6.

## 2 Model

### 2.1 Phase-field formulation

We seek to construct a model that can reproduce the phenomenon of dis- continuous precipitation but remains as simple as possible. Therefore, we will make a number of simplifying assumptions:

(1) We consider isothermal processing of a binary A-B alloy and suppose that the lattice constant is independent of composition. This allows us to disregard elastic effects. As a consequence, both the thermodynamics and the kinetics of the model are governed by the composition field only.
(2) We assume that there is no grain boundary segregation. Then, grain boundaries exhibit motion by curvature only (no solute drag effects).
(3) We choose a particularly simple alloy thermodynamics by assuming that the free energy densities of the two phases involved ($\alpha$ and $\beta$) are simple parabolas of equal curvature.

All of these assumptions could be relaxed by constructing a more general phase-field model along the lines of previous works [5], but this would consid- erably complicate the analysis.

Our approach is based on a phase-field model for two-phase solidification that has been presented in detail in Refs. [8,9]. Each of the three involved phases - the mother phase $\alpha_0$, the depleted $\alpha$ phase and the precipitate phase $\beta$ - is described by one phase field $p_i$ which represents the local volume fraction

3

of the corresponding phase. The phase fields are hence constrained by the condition

$$
p_{\alpha_{0}}+p_{\alpha}+p_{\beta}=1 \tag{1}
$$

for all space points.

The alloy thermodynamics is described by free energy densities $f_{\alpha}(C)$ and $f_{\beta}(C)$, where $C$ is the alloy composition (atomic fraction of B atoms). The mother phase $\alpha_{0}$ and the depleted $\alpha$ phase have different crystallographic orientations and are separated by a grain boundary, but are thermodynamically identical. For the fixed processing temperature, two-phase equilibrium is characterized by the equilibrium compositions $C_{\alpha}$ and $C_{\beta}$ and the equilibrium chemical potential $\mu_{e q}$. For simplicity, we make the transformation $\mu \rightarrow \mu-\mu_{e q}$ and $f_{i} \rightarrow f_{i}-\mu_{e q} C \ (i=\alpha, \beta)$, which shifts the equilibrium chemical potential to zero. Next, we assume that the free energy densities are parabolic around the equilibrium compositions,

$$
f_{\alpha}=\frac{A}{2}\left(C-C_{\alpha}\right)^{2} \quad \text { and } \quad f_{\beta}=\frac{B}{2}\left(C-C_{\beta}\right)^{2}, \tag{2}
$$

where $A$ and $B$ are constants of dimension energy per unit volume. It turns out that the construction of the model is particularly simple if we set $A=B$, which means that the two parabolas have equal curvatures. Since we are interested here in generic features of discontinuous precipitation, there is no harm in making this choice. We then define a scaled composition $c$ by

$$
c=\frac{C-C_{\alpha}}{C_{\beta}-C_{\alpha}}. \tag{3}
$$

The free energy densities, expressed in this variable, are then

$$
f_{\alpha}(c)=\frac{1}{2} H_{c} c^{2} \quad \text { and } \quad f_{\beta}(c)=\frac{1}{2} H_{c}(c-1)^{2}, \tag{4}
$$

where $H_{c}=A\left(C_{\beta}-C_{\alpha}\right)^{2}$.

The starting point for defining the dynamics is a free energy functional which depends on the phase fields and the concentration field,

$$
F[\mathbf{p}, c]=\int \frac{1}{2} K \sum_{i}\left|\vec{\nabla} p_{i}\right|^{2}+H_{p} f_{T W}(\mathbf{p})+\frac{1}{2} H_{c}[c-g(\mathbf{p})]^{2}, \tag{5}
$$

where $K$ and $H_{p}$ are constants of dimension energy per length and energy per volume, respectively, $\mathbf{p} \equiv\left\{p_{\alpha}, p_{\alpha_{0}}, p_{\beta}\right\}$ is the set of phase fields, the sum

runs over all phases $(i = \alpha_0, \alpha, \beta)$, and $f_{TW}$ and $g$ are dimensionless functions that depend only on the phase fields. The former, $f_{TW}$, creates a potential landscape for the phase fields with three distinct minima, corresponding to the three phases (for phase $i$, $p_i = 1$ and the other phase fields are zero). Its expression is

$$
f_{TW} = \sum_{i} p_{i}^{2}\left(1-p_{i}\right)^{2}+a_{\alpha} p_{\alpha_{0}}^{2} p_{\beta}^{2}\left(2 p_{\alpha_{0}} p_{\beta}+3 p_{\alpha}+6 p_{\alpha}^{2}\right). \tag{6}
$$

With $a_{\alpha}=0$, the potential is symmetric with respect to the exchange of any two phases, which implies that the surface tensions of all interfaces are equal. The term proportional to $a_{\alpha}$ breaks this symmetry and modifies the surface tension of the $\alpha_0$-$\beta$ interface without modifying the others (see below for more details). The function

$$
g(\mathbf{p})=\frac{1}{4} p_{\beta}^{2}\left\{15\left(1-p_{\beta}\right)\left[1+p_{\beta}-\left(p_{\alpha_{0}}-p_{\alpha}\right)^{2}\right]+p_{\beta}\left(9 p_{\beta}^{2}-5\right)\right\} \tag{7}
$$

couples the phase fields to the scaled composition. It satisfies $g(p_{\beta}=1)=1$ and $g(p_{\beta}=0)=0$. Therefore, the last term in the free energy functional is identical to the free energy of the $\alpha$ and $\beta$ phases for $p_{\beta}=0$ and $p_{\beta}=1$, respectively.

It is convenient to introduce a dimensionless free energy functional by dividing the free energy density by the constant $H_p$, which yields

$$
\mathcal{F}=\int \frac{1}{2} W^{2} \sum_{i}\left|\vec{\nabla} p_{i}\right|^{2}+f_{TW}(\mathbf{p})+\frac{1}{2} \tilde{\lambda}[c-g(\mathbf{p})]^{2}, \tag{8}
$$

where $W=\sqrt{K / H_{p}}$ is the characteristic length scale of the diffuse interfaces, and $\tilde{\lambda}=H_{c} / H_{p}$ is the ratio of the energy scales associated with the phase-field and concentration contributions in the free energy.

The evolution of the phase fields and the concentration field is obtained from this free energy functional by variational derivatives. We have

$$
\tau \frac{\partial p_{i}}{\partial t}=-\left.\frac{\delta \mathcal{F}}{\delta p_{i}}\right|_{\sum_{i} p_{i}=1}, \tag{9}
$$

where $\tau$ is the relaxation time for the phase fields. The functional derivative on the right hand side has to be evaluated taking into account the constraint on the phase fields, which can be done using a Lagrange multiplier as detailed

in Ref. [9]. For the concentration field, we have the standard conservation law,

$$
\partial_{t} c=\vec{\nabla} \cdot\left(M(\mathbf{p}) \vec{\nabla} \frac{\delta \mathcal{F}}{\delta c}\right),\tag{10}
$$

where $\delta \mathcal{F} / \delta c \equiv \mu$ is the chemical potential, and $M(\mathbf{p})$ is the mobility of the solute. The latter is written as

$$
M(\mathbf{p})=D(\mathbf{p}) / \tilde{\lambda},\tag{11}
$$

where $D(\mathbf{p})$ is the local diffusivity. It is easy to verify from Eqs. (8) and (10) that this choice yields Fick's law in the bulk. For simplicity, we assume that the volume diffusion coefficient $D_{v}$ is the same for the $\alpha$ and $\beta$ phases. In contrast, it is important to include different surface diffusion coefficients for each surface. We define

$$
D(\mathbf{p})=D_{v}+4 p_{\alpha_{0}} p_{\alpha} D_{b}+4 p_{\alpha_{0}} p_{\beta} D_{b}^{\alpha_{0} \beta}+4 p_{\alpha} p_{\beta} D_{b}^{\alpha \beta},\tag{12}
$$

where $D_{b}$ is the grain boundary diffusion coefficient and $D_{b}^{\alpha_{0} \beta}$ and $D_{b}^{\alpha \beta}$ are the surface diffusion coefficients for the interphase boundaries between the precipitate and the supersaturated and depleted $\alpha$ phases, respectively. This form of the surface diffusivity terms is motivated by the fact that the product $p_{i} p_{j}$ is zero in the bulk phases and has a maximum value of $1 / 4$ at the center of the interface (where $p_{i}=p_{j}=1 / 2$).

### 2.2 Relation to sharp-interface models

The model being completely specified, let us now relate its parameters to the quantities that usually appear in sharp-interface theories. To this end, it is useful to give a few more details on the properties of this phase field model; for a more exhaustive discussion, see Ref. [9].

The free energy functional is constructed such that $p_{k}=0$ is a stable solution along each $i-j$ interface both at equilibrium and out of equilibrium, which means that each two-phase interface can be described by a single phase-field variable: since $p_{k}=0, p_{i}$ or $p_{j}$ can be eliminated using the constraint $p_{\alpha}+$ $p_{\alpha_{0}}+p_{\beta}=1$. Furthermore, the special form chosen for the coupling between the concentration and phase fields yields a particularly simple expression for the chemical potential,

$$
\mu=\frac{\delta \mathcal{F}}{\delta c}=\tilde{\lambda}[c-g(\mathbf{p})].\tag{13}
$$

For an equilibrium interface, we have $\partial_t p_i = 0$ for all phase fields, and the chemical potential is constant. Let us first examine a grain boundary, that is, an interface between the $\alpha$ and $\alpha_0$ phases. Since according to the above properties, $p_\beta = 0$ along the whole interface, we have $g(\mathbf{p}) \equiv 0$ and hence $\mu$ constant implies $c$ constant: there is no grain boundary segregation.

Next, consider a planar interphase boundary between phases $\alpha_0$ and $\beta$. Since we have $p_\alpha \equiv 0$, $\mu$ can be expressed as a function of $c$ and one of the phase fields, say $p_\beta$. This yields

$$
\mu = \tilde{\lambda} \left[ c - g_\beta(p_\beta) \right] \tag{14}
$$

with $g_\beta(p) = p^3(10 - 15p + 6p^2)$. The equation for the phase field $p_\beta$ for a planar interface normal to the $x$ direction becomes

$$
0 = \partial_t p_\beta = W^2 \partial_{xx} p_\beta - f_\beta'(p_\beta) - \mu g_\beta'(p_\beta) \tag{15}
$$

with $f_\beta(p) = 2p^2(1 - p)^2 \left[ 1 + a_\alpha p(1 - p) \right]$; the equivalent equation for the $\alpha$-$\beta$ interface can be obtained by omitting the term proportional to $a_\alpha$. Since the chemical potential is equal to zero at two-phase equilibrium, all terms depending on $c$ disappear from Eq. (15), which hence becomes an equation for the phase field only. Our phase-field model has been specifically designed to achieve this exact decoupling, which is not a general property of multi-phase-field models [11]. For $a_\alpha = 0$, the solution of Eq. (15) is the standard hyperbolic tangent profile; for $a_\alpha \neq 0$, a modified equilibrium front profile $p_\beta^0(x)$ is obtained. In both cases, the equilibrium concentration profile can then be obtained from Eq. (14) as $c(x) = g_\beta(p_\beta^0(x))$.

Several consequences arise from the structure of the model: first, the surface tensions of the interfaces can be calculated from the phase-field part of the free energy alone; therefore, the surface tensions are independent of the concentration. They can be calculated by standard procedures in the form of an integral,

$$
\sigma_{\alpha_0 \beta} = 2\sqrt{2} W H_p \int\limits_0^1 p(1 - p)\sqrt{1 + a_\alpha p(1 - p)} dp, \tag{16}
$$

where $\sigma_{\alpha \beta}$ and the grain boundary energy $\sigma_{gb}$ are obtained by setting $a_\alpha = 0$, which yields $\sigma_{\alpha \beta} = \sigma_{gb} = W H_p \sqrt{2}/3$. In the present study, we restrict ourselves to the case where these two surface energies are equal; however, the general case can be easily treated by adding another term to the free energy functional (see Ref. [9]). Furthermore, standard calculations yield the Gibbs-Thomson

relation for the $\alpha$-$\beta$ and $\alpha_0$-$\beta$ interfaces,

$$
\mu_{\mathrm{int}}=d_{\alpha \beta} \kappa, \tag{17}
$$

$$
\mu_{\mathrm{int}}=d_{\alpha_{0} \beta} \kappa, \tag{18}
$$

where $\kappa$ is the interface curvature (counted positive when the $\beta$ domain is convex) and the capillary lengths are given by

$$
d_{i \beta}=\frac{\sigma_{i \beta}}{H_{c}}=\frac{\sigma_{i \beta}}{\partial f^{2} / \partial c^{2}} \quad\left(i=\alpha, \alpha_{0}\right). \tag{19}
$$

Since there is no grain boundary segregation (and hence no solute drag effect), grain boundaries exhibit the standard motion by curvature,

$$
V_{n}=-\sigma_{g b} M_{g b} \kappa \tag{20}
$$

where $V_n$ is the normal velocity of the grain boundary, and the grain boundary mobility is given by

$$
M_{g b}=\frac{W}{\tau H_{p}}. \tag{21}
$$

Note that the product $\sigma_{g b} M_{g b}$ has the dimension of a diffusion coefficient and scales as $W^{2} / \tau$; this is actually the diffusion coefficient that appears in the equations of motion for the phase fields.

Finally, let us comment on the surface diffusion coefficients. In the standard picture of grain boundary diffusion, a grain boundary or interface is seen as a region of well-defined width $\delta$ in which the diffusivity markedly differs from the bulk value; the diffusivity hence formally has a jump at the sharp boundary of the interface zone. In contrast, in the phase-field picture the transition between bulk and "surface" value is smooth. To make contact between the two pictures, it is useful to proceed via a Gibbs construction, as illustrated in Fig. 1. In the upper panel, the profiles of the phase fields in an $\alpha$-$\beta$ interface are shown. In the lower panel, the diffusivity function for $D_{v}=0.05$ and $D_{b}^{\alpha \beta}=1$ is displayed together with a step function that has a certain width $\delta$ which is defined by the relation

$$
D_{b}^{\alpha \beta} \delta=\int_{-\infty}^{\infty} d x\ D[\mathbf{p}(x)]-D_{v}, \tag{22}
$$

that is, the step function and the smooth diffusivity function represent the same total *excess diffusivity* with respect to the bulk value. For the standard

![](./images/867750305683472636_1.jpg)

Fig. 1. Relation between the diffusivity function of the phase-field model and the conventional sharp-interface picture. See text for details.

hyperbolic tangent $(a_{\alpha}=0)$, we obtain analytically $\delta=2 \sqrt{2} W$; for $a_{\alpha} \neq 0$, the value of $\delta$ has to be obtained numerically.

Let us briefly comment on how the model parameters can be determined to simulate a given alloy system. The constant $H_{c}$ is fixed by thermodynamics, since it depends only on the free energy curve and the equilibrium compositions. The capillary lengths can be obtained from this constant and the surface tensions. The latter also fixes the product $W H_{p}$ through Eq. (16). The interface thickness $W$ can either be fixed using structural information, or treated as a free parameter; in both cases, once a value for $W$ is fixed, the parameters $H_{p}, K=W^{2} H_{p}$ and $\tilde{\lambda}=H_{c} / H_{p}$ are fixed. Regarding the surface diffusivities, usually only their product with $\delta$ is known. However, once $W$ chosen in the model, $\delta$ can be calculated from Eq. (22), and thus the value of the surface diffusivities can be fixed. Finally, $\tau$ can be determined through Eq. (21) from the value of the grain boundary mobility.

It is convenient to non-dimensionalize the equations. We choose as units of length, time, and free energy density $W, \tau$, and $H_{p}$. In the final model equations, the only remaining parameters are the constant $a_{\alpha}$ in $f_{T W}$ which influences the surface tension of the $\alpha_{0}-\beta$ interface, the constant $\tilde{\lambda}$, and the dimensionless solute diffusion coefficients; for example, the scaled grain boundary diffusion coefficient $\tilde{D}_{b}$ reads

$$
\tilde{D}_{b}=\frac{D_{b} \tau}{W^{2}}=\frac{D_{b}}{W H_{p} M_{g b}}. \tag{23}
$$

![](./images/867750305683472636_2.jpg)

Fig. 2. Sketch of the geometry of the simulation box. Half of a precipitate is simulated, with reflection boundary conditions on all sides, except ahead on the growth front, where the concentration and the phase fields are kept fixed to the values corresponding to the supersaturated $\alpha_0$ phase. The lateral box size is $L/2$, where $L$ is the interlamellar spacing. The dashed lines indicate the limits of the diffuse interfaces. The drawing is not to scale: in most of the simulations, the interfaces are thinner.

Note that this dimensionless combination can be related to the dimensionless parameter $\beta$ of Cahn's theory [2]. For simplicity, we will drop the tildes for the remainder of the paper.

## 3 Simulation setup and parameters

The equations for the phase fields and the concentration are discretized using finite-difference formulas, and integrated in time using an explicit Euler algorithm. Since we are interested in this study in strictly periodic lamellar arrays only, we can take advantage of the planes of symmetry which are present in the center of each lamella, and compute only half of a lamella pair, as sketched in Fig. 2, with reflection boundary conditions at the lateral sides. The lamellar spacing $L$ is hence fixed by the size of the simulation box.

We start our simulations from a flat grain boundary in contact either with a round precipitate of $\beta$ phase, or with a pre-existing $\beta$ lamella. The values of the concentrations are initially set to the equilibrium values in the $\alpha$ and $\beta$ phase ($c=0$ and 1, respectively), and to the chosen supersaturation $\Delta$ in the $\alpha_0$ phase ($c=\Delta$). In order to speed up the simulations, the box is relatively small in the growth direction and is moved periodically to maintain the growth front in its center. The box size is always large enough to obtain results that are independent of the box size. The growth velocity of the precipitate and

the grain boundary are monitored as a function of time. Once a steady state is obtained, it can be used as an initial condition for subsequent runs with different parameters. This considerably speeds up the convergence to steady-state solutions.

Since we are interested in generic features of discontinuous precipitation, we make some reasonable choices for the parameters rather than to attempt to model a particular alloy system. We set $\tilde{\lambda} = 1$, which yields a ratio of capillary lengths and interface thickness of order unity. For the choice of surface tensions and surface diffusivities, we take into account some findings of Ref. [4] which helps to narrow down the field of investigation. First, the contact angles at the trijunction point have to be such that the $\beta$ precipitate is convex along the entire $\alpha$-$\beta$ interface. For a steady state with a flat grain boundary such as depicted in Fig. 2, this is equivalent to the requirement that the angle between the grain boundary and the $\alpha$-$\beta$ interface has to be smaller than $90^\circ$. The physical foundation of this condition is relatively easy to understand: if the $\alpha$-$\beta$ interface develops overhangs, in a steady-state solution this implies that the overhanging parts of $\beta$ have to dissolve behind the front. However, since at least some parts of this interface have to be concave, they have a lower chemical potential than the surrounding flat or convex parts of the interface, which implies that $\beta$ should grow rather than dissolve. This is indeed what we observe in simulations where the aforementioned condition is not satisfied: the $\beta$ precipitate grows sideways and slows down; no steady-state growth is reached.

The conditions on the surface tensions can be obtained from Young's law at the trijunction point. In our model, $\sigma_{\alpha\beta} = \sigma_{gb}$, and hence we must have $\sigma_{\alpha_0\beta}/\sigma_{gb} > 2\cos(\pi/4) = \sqrt{2}$. We choose $a_\alpha = 9$, which yields $\sigma_{\alpha_0\beta} = 0.7856 H_p W = 1.666 \sigma_{gb}$. A consequence of this choice which has some practical implications is that the $\alpha_0$-$\beta$ interface is thinner than the others. This forces us to use a rather fine discretization of $\Delta x = 0.4 W$. Even with this value, some grid effects remain visible, but a further refinement does not appreciably change the simulation results.

The parameters we focus on in this investigation are the diffusivities $D_v$, $D_b$, $D_b^{\alpha_0\beta}$, and $D_b^{\alpha\beta}$. Of the surface diffusivities, the first two ones control the flux of solute along the growth front, whereas the latter controls the diffusion in the interface *behind* the front. In Ref. [4], it was found that the value of $D_b^{\alpha\beta}$ has a strong influence on the front velocity, and steady-state solutions could be found only below a critical value for $D_b^{\alpha\beta}$. Therefore, we decided to always set $D_b = D_b^{\alpha_0\beta}$, but to keep $D_b^{\alpha\beta}$ as an independent parameter. There are thus three relevant independent diffusion coefficients that need to be investigated: $D_v$, $D_b$, and $D_b^{\alpha\beta}$.


![](./images/867750305683472636_3.jpg)

Fig. 3. Left: snapshot of a simulation with $D_v = 1$ and $D_b = D_b^{\alpha_0^\beta} = D_b^{\alpha\beta} = 0$. Middle: $D_v = 10^{-6}$, $D_b = D_b^{\alpha_0^\beta} = 1$ and $D_b^{\alpha\beta} = 6\times 10^{-3}$. We recall that all diffusion coefficients are scaled according to Eq. (23). Right: blowup of the front region; the arrows represent the diffusion currents. In all cases, $\Delta = 0.8$ and $L/W = 64$.

## 4 Results

### 4.1 General remarks

In our simulations, we have identified two distinct regimes: growth limited by volume diffusion and by surface diffusion. To illustrate the difference, we show in Fig. 3 two representative snapshots of steady-state precipitates correspond- ing to the two regimes. In the bulk-diffusion limited case, the diffusion field extends far into the bulk of the mother phase, and the precipitate is pointy, that is, the curvature is greatest at the precipitate tip. In contrast, in the surface-diffusion limited case, the precipitate is much flatter, and the diffusion field is localized in the vicinity of the interfaces. The latter point is further il- lustrated by the plot to the right, which shows a map of the diffusion currents. Globally, the growth is much faster in the bulk-diffusion limited case.

### 4.2 Bulk-diffusion limited growth

Since the rate-limiting step in discontinuous precipitation is surface diffusion, we will present here only our most important findings about the bulk-diffusion- limited regime; more details will be given elsewhere.

Let us first consider the purely bulk-diffusion-limited case, that is, $D_v = 1$ and $D_b = D_b^{\alpha_0^\beta} = D_b^{\alpha\beta} = 0$. Note that with our definition of the surface diffusivity,


zero surface diffusivity simply means that the diffusivity in the interface region is the same as in the bulk. In this limit, the problem is closely related to the growth of a crystalline finger in a channel, which has been considered in numerous studies of solidification [15,16]. Indeed, if the precipitates grow from the mother phase without the presence of the grain boundary and hence of the second grain, the two problems are completely equivalent. For crystal growth in a channel, it is known [15,16] that steady states can only exist for a channel width exceeding a critical value which depends on the supersaturation. At this critical width, the branch of stable steady-state solutions exhibits a fold singularity: it merges with a second branch of unstable solutions. For a channel width (which is equivalent to the spacing here) above this value, the growth velocity first increases with increasing width, goes through a maximum, and then decreases until the steady-state fingers become unstable against tip-splitting.

We observe qualitatively the same behavior, but the values of the growth velocity also depend on the properties of the grain boundary. In particular, the grain boundary mobility plays an important role. In the snapshot picture of Fig. 3, it can be seen that the grain boundary is slightly curved. If the grain boundary mobility is changed at fixed growth velocity, according to Eq. (20) the curvature of the grain boundary and hence the contact angles at the trijunction are modified; this, in turn, modifies the shape of the precipitate tip and the surrounding diffusion field. When the grain boundary becomes more sluggish, $D_{v}>1$ (we recall that the scaled diffusion coefficient is proportional to the ratio of the solute diffusivity and the grain boundary mobility), it falls even further behind the precipitate tip than shown in the snapshot of Fig. 3, and the shape of the precipitate tip approaches the one of a crystalline finger in a channel. In contrast, when the grain boundary mobility is increased ($D_{v}<$ 1), the curvature of the grain boundary decreases and the precipitate becomes flatter, which leads to a lower growth velocity. Below a certain critical value of $D_{v}$ that depends on the spacing $L$, no steady-state growth is possible. If, in addition, surface diffusion is included for otherwise unchanged parameters, the growth velocity always increases, but the qualitative behavior described above remains unchanged.

### 4.3 Surface-diffusion limited growth

The more relevant case for the description of discontinuous precipitation is growth limited by surface diffusion, which occurs when $D_{v} \ll D_{b}$. In addition, as will be shown in more detail below, we must have $D_{b}^{\alpha \beta} \ll D_{b}$. Globally, the growth velocities are much slower than in the bulk-diffusion limited case, and therefore the grain boundary mobility has no noticeable influence in this regime (the curvature of the grain boundary always remains small).

![](./images/867750305683472636_4.jpg)

Fig. 4. Steady-state velocity versus lamellar spacing for different supersaturations. $D_b = D_b^{\alpha_0\beta}=1$, $D_b^{\alpha\beta}=10^{-3}$, $D_v=10^{-6}$. Lengths are scaled by the capillary length $d\equiv d_{\alpha_0\beta}=0.7856W$, and times by $d^2/D_b$.

For fixed diffusion coefficients, the precipitate growth velocity $V$ depends on the spacing $L$ and the supersaturation $\Delta$. In Fig. 4, we plot the growth velocity versus spacing for different supersaturations. As for bulk-diffusion limited growth, the velocity-versus-spacing curve has a maximum for a certain spacing. For low spacing, the curve ends with a diverging slope at a finite value of the growth velocity. This indicates that the lower limit for steady-state spacing corresponds to a fold singularity, as predicted in Ref. [4]. For spacings below this critical value, no steady-state solution can be found any more. Instead, the growth front velocity decreases with time and the precipitate grows in the lateral direction. For spacings larger than the maximum velocity spacing, $V$ decreases with increasing spacing until an instability is reached: all of the precipitate velocity, the precipitate width and the velocity of the grain boundary start to oscillate until the dynamics reaches an oscillatory limit cycle, as illustrated in Fig. 5.

For a fixed spacing, the velocity increases monotonously with the supersaturation, but no simple scaling law was found. Note that, for fixed spacing, steady-state growth is possible only in a range of supersaturations, the minimum and maximum values of which are set by the fold singularity and the onset of the oscillatory instability, respectively. All characteristic spacings (the minimum spacing, the maximum velocity spacing, and the spacing for the onset of the oscillations) increase with decreasing supersaturation. Since simulations are quite time-consuming due to the slow growth velocities, we have not investigated even lower supersaturations, which would be necessary to determine the scaling of the characteristic spacings with supersaturation.

![](./images/867750305683472636_5.jpg)

Fig. 5. Velocity of the grain boundary as a function of time for $\Delta=0.8$ and $L/d=152.75$; $D_b=D_b^{\alpha_0\beta}=1$, $D_b^{\alpha\beta}=10^{-3}$, $D_v=10^{-6}$. The velocity starts to oscillate, and the amplitude of the oscillation saturates after some time: the system has reached a limit cycle.

![](./images/867750305683472636_6.jpg)

Fig. 6. Steady-state velocity as a function of the surface diffusivity of the $\alpha$-$\beta$ interface, $D_b^{\alpha\beta}$. The other parameters are: $\Delta=0.8$, $L/d=81.5$, $D_b=D_b^{\alpha_0\beta}=1$,$D_v=10^{-6}$.

Next, we investigate the influence of the surface diffusivity in the interphase boundary *behind* the growth front on the precipitate growth velocity: $D_b^{\alpha\beta}$ is varied while all the other parameters and the spacing are kept constant. In agreement with the predictions of Ref. [4], Fig. 6 reveals that the growth velocity decreases with increasing $D_b^{\alpha\beta}$; above a certain critical value, no steady-

![](./images/867750305683472636_7.jpg)

Fig. 7. Steady-state velocity as a function of the bulk diffusivity. The other parameters are: $\Delta=0.8$, $L/d=81.5$, $D_b=D_b^{\alpha_0\beta}=1$,$D_b^{\alpha\beta}=10^{-3}$.

state solutions exist any more. In contrast, no new behavior appears when the value of $D_b^{\alpha\beta}$ is lowered; it can even be set to zero.

A surprising behavior is observed when $D_v$ is increased, as shown in Fig. 7. Contrary to what one might expect, an increase of the bulk diffusivity slows down growth. Above a critical value of $D_v$, no steady-state solution exists any more. This is especially noteworthy because it implies that there is no continuous branch of solutions which links the surface-diffusion-limited and the bulk-diffusion-limited regimes.

### 4.4 Comparison to sharp-interface models

In order to compare our simulation results to the predictions of the sharp-interface theory, we have solved numerically the complete system of equations developed in Ref. [4] that implicitly gives the velocity as a function of spacing; the values of the supersaturation attainable in our simulations are too high for the explicit closed-form approximations given in Ref. [4] to be applicable. The comparison of the predicted to the simulated growth velocities reveals that some features of our results are qualitatively well predicted by the theory: (i) the existence of a fold singularity that sets a lower limit for the spacing, (ii) the initial increase of velocity with increasing spacing, and (iii) the strong influence of the surface diffusivity in the interphase boundary behind the front on the growth velocity. However, there are also some strong discrepancies: the occurrence of a maximum velocity at a well-defined spacing

![](./images/867750305683472636_8.jpg)

Fig. 8. Curvature of the $\alpha$-$\beta$ interface and chemical potential at the interface as
a function of the vertical coordinate $y$. The chemical potential obtained from the
local equilibrium assumption is also shown.

and the subsequent decrease of the velocity with increasing spacing, as well
as the occurrence of the oscillatory instability, are not captured by the theory
of Ref. [4]. Moreover, there are important differences in the magnitudes of the
velocities and spacings: the theory predicts growth velocities that are about
40 to 50 times larger than the ones observed in our simulations, whereas the
minimum steady-state spacing found in our simulations is about three times
larger than the predicted one.

It is interesting to investigate what is the reason for these discrepancies. To
this end, we choose to analyze one particular simulation and to check which
ingredients of the sharp-interface theory are a good description of our simula-
tions, and which have to be revised. We focus on the $\alpha$-$\beta$ interface, since the
solution of the complete free boundary problem in Ref. [4] provides a partic-
ularly simple prediction for its shape: the curvature of the interface decreases
exponentially with the distance from the trijunction point, $\kappa \propto \exp[q(y - y_t)]$,
where $y_t$ is the $y$ coordinate of the trijunction point, and $q$ is the inverse of a
decay length, which can be related to the model parameters [4]. In Fig. 8 we
plot the interface curvature as a function of $y$ and find indeed an exponential
decay.

The sharp-interface model assumes local equilibrium at the $\alpha$-$\beta$ interface ac-
cording to Eq. (17). The solute diffusion along the interface is then driven
by the curvature gradient, which creates a chemical potential gradient. To
check these assumptions, we extract the chemical potential at the center of

![](./images/867750305683472636_9.jpg)

Fig. 9. Plot of various quantities as a function of $x$ for a $y$ coordinate corresponding to a position halfway between the trijunction point and the lower system boundary. See text for details.

the interface and find indeed an exponential decay, as expected. However, the curvature and the chemical potential extracted from our simulations are not in agreement with the Gibbs-Thomson law of local equilibrium, Eq. (17).

To get a more detailed picture, we plot in Fig. 9 a profile of various quantities along a horizontal line that cuts through the $\alpha$-$\beta$ interface at some distance behind the trijunction point. The current density in the $y$ direction is shown as a dash-dotted line. Since the bulk diffusion is very slow, this current is close to zero in both the $\alpha$ and $\beta$ phases. It exhibits a peak in the diffuse interface, with a negative sign: this is the surface current which is driven by the curvature gradient along the $\alpha$-$\beta$ interface from the trijunction region to the region far behind the front where the interface is flat. The shape of the peak is as expected from the diffusivity function shown in Fig. 1, which indicates that the general picture of a smooth "surface current density" is correct.

The chemical potential, shown as a full line, has smooth variations in both bulk phases and is positive. This profile is essentially set by the growth history: since bulk diffusion is slow, the concentration (and hence the chemical potential) remains approximately at the value it had immediately after the passage of the growth front. In contrast, $\mu$ strongly varies in the interface region and exhibits a "dip": in the center of the interface, it is below the value predicted by the Gibbs-Thomson relation, whereas in the regions adjacent to the bulk it is above. Thus, not only the chemical potential in the interface does not satisfy the Gibbs-Thomson relation, but even the concept of a uniform "interface chemical potential" cannot be maintained.

18

Qualitatively, this "dip" in the chemical potential is due to the fact that solute can be rapidly transported along the interface, and hence the chemical potential can change much faster in the center of the interface than in the bulk. Since the chemical potential of a flat interface is zero, and hence lower than any value occurring in the bulk, the diffusion along the interface "drains" solute from the surrounding bulk. Note that, as a consequence, the local values of the chemical potential are history-dependent, even inside the diffuse interface where the diffusion is fast. This can be recognized in Fig. 9, in which the position of the center of the interface is marked by a vertical dotted line. Clearly, the "dip" in the chemical potential is asymmetric. This can be explained by the fact that this interface has moved slightly "to the right" (toward increasing $x$) since the passage of the trijunction point. Therefore, the points on the left side of the interface have already been drained by the surface current, whereas the points to the right have not.

## 5 Discussion

### 5.1 Influence of the diffusivities

One of the surprising results of the present study is that the two regimes where growth is limited by bulk and surface diffusion, respectively, seem to be distinct in the sense that we have found no continuous family of solutions connecting them.

A possible explanation comes from the geometric constraints. Let us first examine growth limited by surface diffusion and suppose furthermore that there is no diffusion in the $\alpha$-$\beta$ interface behind the growth front. Then, the growth of the $\beta$ precipitate requires that solute is transported from the $\alpha$ to the $\beta$ lamella along the growth front; a current of solute atoms must hence flow from the center of the grain boundary to the center of the $\beta$ lamella (from right to left in Fig. 2). Even though the local equilibrium assumption is not valid, Fig. 8 shows that the local chemical potential still increases with curvature. Hence, such a current can flow only if the curvature decreases from the sides to the center of the $\beta$ lamellae; as a consequence, the curvature must exhibit a minimum in the center of the $\beta$ lamella.

The decrease of the growth velocity with the increase of the diffusivity in the $\alpha$-$\beta$ interface is easily understood: when diffusion along this interface takes place, a part of the solute atoms is drained toward the flat parts of the interface far behind the growth front where the chemical potential is lowest; this material is lost for the forward growth of the precipitate, and the surface current to the center of the $\beta$ lamella decreases.


When bulk diffusion is allowed, there is an alternative diffusion path through the volume, which on first thought should accelerate growth. However, dif- fusion in the bulk also leads to morphological instability: the concentration gradients are enhanced around protruding parts of the interface, which hence advance faster than flat parts, leading eventually (in the regime limited by volume diffusion) to the emergence of cellular precipitates which exhibit a maximum of curvature at the tip. A possible explanation of the decrease of the growth velocity with increasing bulk diffusivity is that the bulk diffusion leads to an increase of curvature at the precipitate tip, which decreases the driving force for lateral surface diffusion. The two diffusion mechanisms hence play antagonistic roles. We found steady states only when one of these mech- anisms is strongly dominant over the other. However, we have only explored a small part of the parameter space spanned by $L$, $\Delta$, $D_v$, $D_b$, and $D_b^{\alpha\beta}$, and hence we cannot exclude that there is a path which connects the two types of solutions. Further studies are needed to clarify this point.

### 5.2 Breakdown of local equilibrium

To understand the breakdown of local equilibrium, let us revisit some of the fundamental ideas behind the local equilibrium assumption. The concept of "local equilibrium" implies that there is a separation of length and time scales: in a small part of the system, some fast processes can establish and maintain a local thermodynamic equilibrium, whereas the entire system evolves on large length scales and slow time scales. This provides "adiabatic" changes in the boundary conditions on the small scale. In the case considered here, namely slow bulk diffusion and fast surface diffusion, these definitions become am- biguous. Indeed, since the diffusivity rapidly falls to a small value in the bulk, it takes much longer for a solute atom to diffuse from one side of an interface to the other than to diffuse along the interface by a distance which is much larger than the interface thickness.

Therefore, the "small volume element" to be considered for local equilibrium is strongly anisotropic. To be more precise, consider the diffusion times asso- ciated with diffusion across and along the interfaces, $t_\perp$ and $t_\parallel$,

$$
t_\perp = \frac{W^2}{D_v} \tag{24}
$$

$$
t_\parallel = \frac{l^2}{D_b}. \tag{25}
$$

We have used the value of the bulk diffusivity in the first expression because the rate-limiting step for diffusion across the interface is the crossing of the

outer regions of the interface where the diffusivity is the lowest and almost equal to the bulk diffusivity. In the second expression, $l$ is an as of yet unknown length scale. Equating the two time scales, we obtain

$$
l=W \sqrt{\frac{D_{b}}{D_{v}}} ; \quad(26)
$$

obviously, $l$ can be much larger than $W$.

The concept of local equilibrium remains valid only if the "external conditions" - here, the curvature and interface velocity - remain almost constant over this distance. The characteristic length scale for variations of curvature and interface velocity is the lamellar spacing $L$; hence we obtain the condition

$$
W \sqrt{\frac{D_{b}}{D_{v}}} \ll L \quad(27)
$$

for the validity of local equilibrium.

In our simulations, $\sqrt{D_{b} / D_{v}}=10^{3}$, whereas typical system sizes are $L \sim 50 \mathrm{~W}$; therefore, this condition is not satisfied. To check whether this corresponds to a real experimental situation, we consider the alloy Al-Zn which has been extensively studied [17]. In the temperature range between 400 and 500 K, spacings are of the order 100 nm, and growth velocities of the order $10^{-7} \mathrm{~m} / \mathrm{s}$. The bulk diffusion coefficient varies from $\sim 10^{-16}$ to $\sim 10^{-19} \mathrm{~m}^{2} / \mathrm{s}$, whereas the triple product $s \delta D_{b}$, where $s$ is the segregation factor, is of order $10^{-20}-10^{-21}$ $\mathrm{m}^{3} / \mathrm{s}$. Assuming $s \approx 1$ and $\delta=1 \mathrm{~nm}$, the ratio $D_{b} / D_{v}$ ranges from $10^{8}$ to $10^{5}$. Even for the latter value, the condition for local equilibrium is not satisfied. This shows that the breakdown of local equilibrium found here is likely to occur for typical experimental conditions.

Another way of reaching the same conclusion is the following: in steady-state growth, the characteristic length scale for the bulk diffusion field is the diffu- sion length $l_{D}=D_{v} / V$. For the values of $D_{v}$ and $V$ given above, the length scale ranges from $10^{-9}$ to $10^{-12} \mathrm{~m}$, which means that it is comparable to or even smaller than the typical thickness of an interface. Furthermore, the time for diffusion across an interface given by Eq. (24) is comparable to or larger than the time an interface needs to advance by once its thickness. In solidifica- tion, it is well known that solute trapping occurs under these conditions, which leads to a breakdown of local equilibrium. The condition for the occurrence of solute trapping is

$$
\frac{W V}{D_{v}}>1, \quad(28)
$$


which is satisfied for the values cited above.

The breakdown of local equilibrium discovered here is thus very similar to solute trapping in solidification. Our findings can therefore be re-stated in a different way: even though surface diffusion is faster and controls the growth velocity of the precipitates, the quantity that controls local equilibrium at interfaces is the low bulk diffusion coefficient. Therefore, non-equilibrium effects at interfaces cannot be neglected even at the slow growth velocities of discontinuous precipitation.

To avoid confusion, it should be mentioned that of course since Cahn's work [2]
it is known that the concentrations in the volume of the transformed material are not equal to the equilibrium concentrations. However, in all existing theories [2,3,4] it is assumed that the local concentration in the grain boundary and the interfaces can be related to the concentration in the volume of the adjacent growing material by the local equilibrium assumption.

Since our results show that this assumption is generally not valid, it is not surprising that none of the existing theories agrees with our simulation results. However, Fig. 9 shows that the system behaves, at least to some degree, as predicted by theory, but not with the right value of the coefficients. This explains why comparisons of experimental data with theoretical predictions where at least one quantity is treated as an adjustable parameter can yield reasonable agreement [1].

## 5.3 Oscillatory motion

Oscillatory instabilities are well known from cellular and eutectic solidification in thin samples [13,14]. They occur, like the instability observed here, for spacings larger than some critical spacing which depends on the alloy system, the composition, and the processing conditions. The oscillations are collective, that is, numerous cells or lamellae oscillate in phase over a large area of the solidification front. Since we have only performed here simulations for a single lamella, it is not clear whether an extended discontinuous precipitation front exhibits such collective or rather an irregular, chaotic behavior. In solidification, the coupling between neighboring elements is provided by the diffusion field in the liquid; surface diffusion should provide a much weaker coupling. Large-scale simulations will be needed to elucidate this point.

A "jerky" or "stop and go" motion during discontinuous precipitation has been observed in several alloy systems, including Al-Zn [18]. The oscillatory motion observed in our simulations could be an explanation for these observations. More detailed data, both from simulations and experiments, are needed to clarify this issue.

## 6 Conclusion

We have developed a phase-field model for discontinuous precipitation and performed simulations to study the influence of various parameters on the growth velocity of strictly periodic lamellar arrays. Our most important find- ings are that (i) for given growth conditions and composition, steady-state solutions exist for a range of spacings, (ii) the minimum spacing is given by a limit point beyond which no steady-state solution exists any more, (iii) an oscillatory instability occurs for large interlamellar spacings, which leads to a non-constant growth velocity, and (iv) the breakdown of local equilibrium, an effect analogous to solute trapping in solidification, cannot be neglected in discontinuous precipitation.

These results demonstrate that our phase-field model is a promising tool to elucidate many open questions on discontinuous precipitation. Particularly in- teresting points are the extension of our work to lower supersaturations and to growth fronts with several precipitates, as well as the further investigation of the oscillatory instability. To achieve these goals in a reasonable simulation time, more efficient numerical schemes should be used. In particular, adap- tive meshing seems a promising strategy since the main diffusion fluxes are concentrated along the interfaces. Another important question concerns the influence of elastic strains on the discontinuous precipitation reaction [19]. It is straightforward to include such effects in multi-phase-field models [20], but the computational complexity is dramatically increased, which makes a systematic study quite challenging.

Our results also reveal that a fully quantitative modeling of discontinuous precipitation is a challenging task. As predicted by Ref. [4], the growth velocity depends sensitively on the angles at the trijunction points and the diffusivity in the interphase boundary behind the growth front; these parameters are generally unknown, and difficult to obtain from experiments. A possible way out would be to use atomistic simulations to obtain the input parameters for the phase-field model, as already pioneered in solidification [21].

## Acknowledgments

L. A. acknowledges financial support through a stipend by the Ministère de l'Enseignement Supérieur et de la Recherche Scientifique (Algeria).

### References

[1] Manna I, Pabi SK, Gust W. Int. Mat. Rev. 2001;46:53

[2] Cahn JW. Acta Metall. 1959;7:18

[3] Klinger LM, Brechet YJM, Purdy GR. Acta Mater. 1997;45:5005

[4] Brener EA, Temkin DE. Acta Mater. 1999;47:3759

[5] Chen LQ. Annu. Rev. Mater. Res. 2002;32:113

[6] Boettinger WJ, Warren JA, Beckermann C, Karma A. Annu. Rev. Mater. Res. 2002;32:163

[7] Ramanarayan H, Abinandanan TA. Acta Mater. 2004;52:921

[8] Folch R, Plapp M. Phys. Rev. E 2003;68:010602(R)

[9] Folch R, Plapp M. Phys. Rev. E 2005;72:011602

[10] Steinbach I, Pezzolla F, Nestler B, Seeßelberg M, Prieler R, Schmitz GJ, Rezende JLL. Physica D 1996;94:135

[11] Nestler B, Garcke H, Stinner B. Phys. Rev. E 2005;71:041609

[12] Eiken J, Böttger B, Steinbach I. Phys. Rev. E 2006;73:066122

[13] Karma A, Sarkissian A. Metall. Mat. Trans. A 1996;27:635

[14] Ginibre M, Akamatsu S, Faivre G. Phys. Rev. E 1997;56:780

[15] Brener EA, Geilikman MB, Temkin DE. Zh. Eks. Teor. Fiz. 1988;94:241

[16] Brener EA, Müller-Krumbhaar H, Saito Y, Temkin DE. Phys. Rev. 1993;47:1151

[17] Yang CF, Sarkar G, Fournelle RA. Acta Metall. 1988;36:1511

[18] Abdou S, Sol'orzano G, El-Boragy M, Gust W, Predel B. Scripta Mater. 1996;34:1431

[19] Brener EA, Temkin DE. Acta Mater. 2003;51:797

[20] Steinbach I, Apel M. Physica D 2006;217:153

[21] Hoyt JJ, Asta M, Karma A. Mat. Sience Eng. R 2003;41:121