![](./images/811848115148554240_1.jpg)

# Virial coefficients of Lennard-Jones mixtures

Andrew J. Schultz and David A. Kofke

Citation: *The Journal of Chemical Physics* **130**, 224104 (2009); doi: 10.1063/1.3148379
View online: http://dx.doi.org/10.1063/1.3148379
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/130/22?ver=pdfcov
Published by the AIP Publishing

## Articles you may be interested in
Communication: [Virial coefficients and demixing in highly asymmetric binary additive hard-sphere mixtures](http://)
J. Chem. Phys. **138**, 161104 (2013); 10.1063/1.4803097

[Mixing effects in glass-forming Lennard-Jones mixtures](http://)
J. Chem. Phys. **130**, 154505 (2009); 10.1063/1.3106759

[Regarding convergence curve of virial expansion for the Lennard-Jones system](http://)
J. Chem. Phys. **127**, 064507 (2007); 10.1063/1.2754272

[Interfacial tension behavior of binary and ternary mixtures of partially miscible Lennard-Jones fluids: A molecular dynamics simulation](http://)
J. Chem. Phys. **110**, 8084 (1999); 10.1063/1.478710

[On the excess enthalpy and volume of two-component Lennard-Jones fluids in supercritical region: Is the mixture of simple liquids simple?](http://)
J. Chem. Phys. **107**, 3121 (1997); 10.1063/1.474665

![](./images/811848115148554240_2.jpg)

# Virial coefficients of Lennard-Jones mixtures

Andrew J. Schultz and David A. Kofke${}^{\mathrm{a)}}$

Department of Chemical and Biological Engineering, University at Buffalo, The State University
of New York, Buffalo, New York 14260-4200, USA

(Received 27 March 2009; accepted 12 May 2009; published online 10 June 2009)

We report results of calculations of the second through sixth virial coefficients for four prototype Lennard-Jones (LJ) mixtures that have been the subject of previous studies in the literature. Values are reported for temperatures ranging from $T$=0.6 to $T$=10.0, where here the temperature is given units of the LJ energy parameter of one of the components. Thermodynamic stability of the mixtures is studied using the virial equation of state (VEOS) with the calculated coefficients, with particular focus on characterizing the vapor-liquid critical behavior of the mixtures. For three of the mixtures, vapor-liquid coexistence and critical data are available for comparison at only one temperature, while for the fourth we can compare to a critical line. We find that the VEOS provides a useful indication of the presence and location of critical behavior, although in some situations we find need to consider "near-miss" critical behavior, where the classical conditions of criticality are nearly but not exactly satisfied. © 2009 *American Institute of Physics*. [DOI: 10.1063/1.3148379]

## I. INTRODUCTION

Reliable prediction of the properties of mixtures is one of the more important and unresolved challenges in chemical thermodynamics. Most material systems of practical interest are mixtures of two or more species and the vast space of components and proportions that are possible in the formu- lation of mixtures precludes any comprehensive experimen- tal characterization. Thus prediction of mixture properties from some type of model is an essential element of any effort to design and manipulate processes and products.

Often mixtures do not behave in a way that simply in- terpolates the pure-component behaviors and, to capture the key elements that give rise to nontrivial (i.e., nonideal) be- haviors, it is necessary to incorporate some characterization of the molecular features of the component substances. Ex- amples of successful treatments that do this include SAFT (Ref. 1) and COSMO-RS and its derivatives. $^{2}$ Both of these approaches are proving useful in characterizing and predict- ing mixture behavior. Molecular simulation is another tool that can be effective in describing mixture properties using molecular principles. $^{3}$ Unlike "engineering" approaches such as SAFT, simulation admits the use of arbitrarily realistic molecular models, although in practice relatively simple models are employed to minimize the computational ex- pense. This expense makes simulation unwieldy as a design tool, but on the other hand it is extremely versatile as it is, in principle, capable of providing almost any thermophysical property of interest under a very broad range of conditions.

Significant effort has been put into understanding and cataloguing the "global phase diagram," $^{4,5}$ which is a map of all the significant phase behaviors exhibited by a mixture, considering not only the thermodynamic state, but also the parameters of the model. Mixtures of just two components can exhibit a very broad range of phenomena, involving vari- ous combinations or intersections of criticality, multiphase equilibria, azeotropy, immiscibility, and so forth. A compre- hensive characterization of the behaviors can be performed only with an analytic model, in which derivatives and roots can be found through analysis and numerical methods. Ex- periment and even molecular simulation do not lend them- selves easily to this type of study, so to make further progress it can be especially valuable to have molecular-based ana- lytic models of the thermodynamic behavior of mixtures.

The virial equation of state (VEOS) combines some of the appealing features of engineering models and molecular simulation. It is a density expansion written with respect to an ideal-gas reference, and while any thermophysical prop- erty can be expressed in such a series it is the pressure via the VEOS that is most commonly studied and applied. TheVEOS is written as follows: $^{6}$

$$
\beta P/\rho=1+B_{2}\rho+B_{3}\rho^{2}+B_{4}\rho^{3}+\cdots, \tag{1}
$$

where $P$ and $\rho$ are the pressure and number density, respec- tively, $\beta=1/kT$ is the reciprocal temperature in energy units, and $B_{n}$ is the $n$th virial coefficient, which is independent of density. Obviously the VEOS has an analytic form that is readily manipulated and provides numerical results very rap- idly, given values of the coefficients. The virial coefficients connect directly to a molecular model and because it is based on knowledge of interactions between only a few molecules at a time, the VEOS can accommodate more complex, real- istic models than typically used in molecular simulation. Of course it suffers also from the significant limitation that it applies only at low density, but the question of how low the density must be for the virial equation to be relevant has not been addressed in a comprehensive way. This is largely due to the difficulty of calculating high-order virial coefficients, which requires evaluation of many-dimensional integrals over translational, rotational, and internal degrees of freedom of $n$ molecules for the coefficient $B_{n}$. Recent advances permit the calculation of coefficients up to at least $n$=5 for multi-

${}^{\mathrm{a)}}$Electronic mail: kofke@buffalo.edu.

atomic molecules without much difficulty, $^{7-10}$ so we are positioned to investigate the applicability of the VEOS for a broader range of systems. In the present work we examine application to mixtures. Mixture virial coefficients are given exactly as a mole-fraction weighted sum of coefficients involving $n$ molecules in various combinations of the corresponding species. Thus for example, in two-component mixtures, $B_2$ and $B_3$ are

$$
\begin{aligned}
& B_{2}=y_{1}^{2} B_{20}+2 y_{1} y_{2} B_{11}+y_{2}^{2} B_{02}, \\
& B_{3}=y_{1}^{3} B_{30}+3 y_{1}^{2} y_{2} B_{21}+3 y_{1} y_{2}^{2} B_{12}+y_{2}^{3} B_{03},
\end{aligned}
\tag{2}
$$

where $y_k$ is the mole fraction of species $k$, labeled 1 or 2. The coefficients with multiple numerals in their subscripts represent specific species combinations—the first and second subscripts indicate the number of molecules of species 1 and 2, respectively, which interact in defining the coefficient.

Vega $^{11}$ performed some of the most ambitious calculations of mixture virial coefficients to date, as part of a larger set of studies $^{12-14}$ of virial coefficients of molecular systems. His study examines multicomponent mixtures of hard spheres, with as many as ten components. He also examines hard-sphere chains, $^{11,12}$ computing coefficients up to $B_4$ for chain lengths of as much as 100 using an approach in which the different conformations of the chains are viewed as different components of a mixture. Vega advocates a method that calculates the full mixture coefficients $B_n$ at specified compositions, pointing out that if this is done for a sufficient number of mole fractions, one can invert Eq. (2) to determine the elementary coefficients $B_{ij}$. Apart from this work, high-order virial coefficients for mixtures focused on simple potentials. This includes studies of the Gaussian model, $^{15}$ hard spheres, $^{16,17}$ and hard-sphere and square-well mixtures. $^{17}$ Low-order virial coefficients have been determined for some more complex models. Multiple studies of mixture virial coefficients have been performed in the context of solubility in supercritical fluids, which has significance in relation to some separation processes. $^{18-20}$ In various cases the virial coefficients in these studies are given by Taylor-series expansion of an analytic equation of state, empirical correlations, or evaluation of cluster integrals using a model potential. The focus is on behavior at high dilution and the physical quantity of interest is the solute chemical potential. Often it is assumed in these applications that the solvent-phase volumetric properties are given and that other properties related to the solute (e.g., the vapor pressure in its pure condensed form) are known. It is found that the virial equation truncated to third order in the density is inadequate for the purpose, particularly in the (typical) case where the molecular size of the solute is somewhat larger than the solvent. $^{20}$ However, significant improvement is seen when the fourth-order term is added, $^{18}$ so there is some motivation to pursue higher-order terms.

In the present study we examine the ability of the virial expansion to describe volumetric and stability properties of mixtures. We apply VEOS to Lennard-Jones (LJ) models where simulation data for mixture vapor-liquid coexistence are available. We are particularly interested in the ability of VEOS to predict or indicate the location of the critical point.

<table>
<caption>TABLE I. Parameters for the LJ mixtures examined in this work. For all mixtures, the species-1 size and energy parameters $\sigma_{11}$ and $\varepsilon_{11}$ are unity and provide the length and energy scales for the system. The table lists the unlike and species-2 size and energy parameters for the four mixtures in units of the species-1 parameters.</caption>
<thead>
<tr>
<th>Mixture</th>
<th>$\sigma_{12}$</th>
<th>$\sigma_{22}$</th>
<th>$\varepsilon_{12}$</th>
<th>$\varepsilon_{22}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>I</td>
<td>1.0</td>
<td>1.0</td>
<td>0.75</td>
<td>1.0</td>
</tr>
<tr>
<td>II</td>
<td>0.885</td>
<td>0.769</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>III</td>
<td>0.884</td>
<td>0.768</td>
<td>0.773</td>
<td>0.597</td>
</tr>
<tr>
<td>IV</td>
<td>1.0</td>
<td>1.0</td>
<td>$2^{-1/2}$</td>
<td>0.5</td>
</tr>
</tbody>
</table>

It is difficult to obtain such data by molecular simulation as a function of composition, so we do not have much to compare.

In the Sec. II we describe the models and briefly review the methods used to calculate the virial coefficients and identify stability limits. Then in Sec. III we present and discuss results before concluding in Sec. IV.

## II. MODELS AND METHODS

### A. Models

The LJ mixtures that we examined in this study are summarized in Table I. All are two-component mixtures. In this table and in all that follows, except where explicitly indicated otherwise, all quantities are made dimensionless by the species-1 LJ size and energy parameters, $\sigma_{11}$ and $\varepsilon_{11}$. The systems labeled I, II, and III were examined previously and their vapor-liquid equilibrium (VLE) behavior has been reported in two independent studies. $^{21,22}$ Mixture I is a symmetric mixture in which the unlike interactions are weaker than the like interactions, so it displays positive deviations from ideal mixing. In mixture II the energy parameter is the same for all pairs, but the atoms are different sizes and the cross interaction is a simple average of like interactions. Mixture III is a somewhat conventional case of species differing in both size and energy parameters, with Lorentz-Berthelot mixing rules. It is notable in having one component supercritical at the conditions studied previously, so there is a known critical point found in the pressure-composition plane. Mixture IV was examined in a more recent study $^{23}$ and it has atoms of the same size but with different energy parameters. For this system data are known for the critical line in pressure-temperature space joining the critical points of the two pure substances.

### B. Thermodynamic stability

One of the interests in this study is to examine the limits of thermodynamic stability as given by the virial equation for the mixtures and, additionally, to locate the critical point. We can compare the stability limits to the known VLE phase envelope. A meaningful stability limit will lie above the dew-point pressure of the vapor; this test can give us a rough indication of the ability of the VEOS to describe the gas-phase behavior in this region. We can compare critical points with simulation data for two of the model mixtures.

The stability of a system against separation into more than one thermodynamic phase is analyzed by examining the

convexity of the free energy function. There are many equivalent ways to express the conditions of thermodynamic stability and the choice is a matter of convenience. The density and mole fractions are dependent variables in the VEOS, so it is appropriate to work with the Helmholtz representation, for which stability requires $^{24}$

$$
-\left(\frac{\partial \mu_{1}}{\partial N_{1}}\right)_{T, V, N_{2}}\left(\frac{\partial P}{\partial V}\right)_{T, N_{1}, N_{2}}-\left(\frac{\partial P}{\partial N_{1}}\right)_{T, V, N_{2}}^{2}>0. \quad (3)
$$

Through standard manipulation of derivatives, we can convert this to a form in which derivatives are taken with respect to the density and species-1 mole fraction, which are the variables appearing in the VEOS. In these terms, stability can be expressed as

$$
\left(\frac{\partial P}{\partial \rho}\right)_{T, y_{1}}\left(\left(\frac{\partial \mu_{1}}{\partial y_{1}}\right)_{T, \rho}-\frac{1}{\rho}\left(\frac{\partial P}{\partial y_{1}}\right)_{T, \rho}\right)-\frac{1-y_{1}}{\rho^{2}}\left(\frac{\partial P}{\partial y_{1}}\right)_{T, \rho}^{2}>0.
$$

(4)

Apart from additive terms that do not depend on density or composition, the chemical potential according to the VEOS is $^{25}$ (written here for species 1 of a binary mixture)

$$
\begin{aligned}
\beta \mu_{1}= & \ln \left(y_{1} \rho\right)+2 \rho\left(y_{1} B_{20}+y_{2} B_{11}\right) \\
& +\frac{3}{2} \rho^{2}\left(y_{1}^{2} B_{30}+2 y_{1} y_{2} B_{21}+y_{2}^{2} B_{12}\right) \\
& +\frac{4}{3} \rho^{3}\left(y_{1}^{3} B_{40}+3 y_{1}^{2} y_{2} B_{31}+3 y_{1} y_{2}^{2} B_{22}+y_{2}^{3} B_{13}\right)+\cdots.
\end{aligned}
$$

At a spinodal the limit of stability is reached and the inequality given above is instead satisfied as an equality. The locus of such points traces a spinodal curve, which can end at a stable point—the critical point—which further satisfies $^{24}$

$$
\left(\frac{\partial^{2} \mu_{1}}{\partial N_{1}^{2}}\right)_{T, P, N_{2}}=0. \quad (6)
$$

When this is cast in the Helmholtz representation and put in terms of variables and path convenient for application to the VEOS, we have

$$
\begin{aligned}
& \left(\rho \mu_{y y}-P_{y y}\right)+\kappa\left(P_{y}^{2}-3\left(1-y_{1}\right) P_{y y} P_{y}\right)+\kappa^{2}\left(1-y_{1}\right) \\
& \quad \times\left(3 \rho P_{y}^{2} P_{y \rho}-2 P_{y}^{3}\right)-\kappa^{3}\left(1-y_{1}\right) \rho^{2} P_{y}^{3} P_{\rho \rho}=0. \quad (7)
\end{aligned}
$$

Here, the subscripts indicate partial derivatives taken with respect to $y\left(\equiv y_{1}\right)$ and/or $\rho$; also $\kappa \equiv(\partial \rho / \partial P) / \rho$ $=[\rho(\partial P / \partial \rho)]^{-1}$.

### C. Evaluation of virial coefficients

The virial coefficients are given in terms of cluster integrals involving interactions among $n$ molecules for the coefficient $B_{n}{ }^{26}$ The coefficient $B_{2}$ is

$$
B_{2}(T)=-\frac{1}{2 V} \iint f_{12} d \mathbf{r}_{1} d \mathbf{r}_{2}=-\frac{1}{2 V} \boldsymbol{\bullet} \boldsymbol{\bullet}
$$

and $B_{3}$ and $B_{4}$ are (for pairwise-additive potentials)

$$
B_{3}(T)=-\frac{1}{3 V} \iiint f_{12} f_{13} f_{23} d \mathbf{r}_{1} d \mathbf{r}_{2} d \mathbf{r}_{3}=-\frac{1}{3 V} \bigwedge
$$

$$
B_{4}(T)=-\frac{1}{V}\left[\frac{3}{8} \boldsymbol{\square} \boldsymbol{\square}+\frac{3}{4} \boldsymbol{\square}+\frac{1}{8} \boldsymbol{\square} \boldsymbol{\square}\right]
$$

while $B_{5}$ is a sum of ten integrals each involving five molecules. In the integrals, $f_{i j}=\exp \left(-\beta u_{i j}\left(r_{i j}\right)\right)-1$ is the Mayer function, where $u_{i j}$ is the pair potential between molecules labeled $i$ and $j$. For a spherically symmetric potential, this is a function only of the separation $r_{i j}$, as indicated. The points joined by lines are the conventional representation $^{26}$ of cluster integrals in terms of field points each representing the integral of a molecule over the volume and bonds representing the Mayer functions $f_{i j}$ defined on the separation between the two points it joins.

Mayer-sampling Monte Carlo (MSMC) (Ref. 7) is a general approach to calculation of the cluster integrals in which the configurations of the molecules are sampled according to a Markov process, much as is done in a standard Metropolis Monte Carlo (MC) simulation. $^{3}$ Configurations are weighted according to the absolute value of the Mayer-function integral, or sum of integrands for coefficients $B_{n}, n>3$ that are given in terms of more than one cluster integral. The integrals are calculated using ideas derived from methods used to compute the free energy. $^{27}$ In most cases we employ overlap sampling with Bennett's optimization, $^{28}$ for which the working equation in MSMC becomes $^{9}$

$$
\Gamma(T)=\Gamma_{0} \frac{\left\langle\gamma^{\prime} / \pi\right\rangle_{\pi} /\left\langle\gamma_{o s} / \pi\right\rangle_{\pi}}{\left\langle\gamma_{0} / \pi\right\rangle_{\pi 0} /\left\langle\gamma_{o s} / \pi_{0}\right\rangle_{\pi 0}} .
$$

Here we use $\Gamma$ to represent a general cluster integral or virial coefficient, $\gamma$ is the corresponding integrand (or sum of integrands) needed for its calculation, $\pi$ is the function used to weight the sampling of configurations, the subscript $o$ indicates a value for a known reference system, and the angle brackets specify an ensemble average weighted by $\pi$ or $\pi_{0}$. Also $\gamma_{o s}$ is the overlap function, given in terms of the target and reference integrands as

$$
\gamma_{o s}=\frac{\left|\gamma_{0}\right||\gamma|}{\alpha\left|\gamma_{0}\right|+|\gamma|}
$$

where $\alpha$ is a parameter selected to optimize the convergence of the calculation. Additionally, the distribution of computational effort expended between sampling the $\pi$ and $\pi_{0}$ systems is balanced to ensure that their marginal contribution to the stochastic error of the result is equalized. As a reference system we use hard spheres of diameter equal to 1.5 times the LJ $\sigma_{11}$ of the sampled system. The reference integrand $\gamma_{0}$ is the same function as $\gamma$ but with the hard-sphere potential, and the sampling weights are just the absolute value of the integrand, $\pi=|\gamma|$.

Mixture virial coefficients are given by cluster integrals similar to those above for pure substances, except that we must consider variations in which the points are different molecular species. Thus, for example, the unlike-species coefficient in $B_{2}$ is represented

$$
B_{11}=-\frac{1}{2 V} \bullet \boldsymbol{\square}
$$

where the square is used to represent species 2. One of the $B_{3}$ coefficients is

$$
B_{21}=-\frac{1}{3 V} \bigtriangleup
\tag{14}
$$

Each $f$-bond is defined as appropriate to the species of the two points it joins. We need not explicitly consider permutations of the $B_3$ cluster integrals because they are mathematically equivalent—for a given number of species 1 and 2 in the cluster, no matter how they are assigned to the points, the value of the integral represented by the cluster is the same. However, when we consider the mixture cluster integrals involving four molecules, we must consider the permutations and their weights inasmuch as some of the permutations correspond to mathematically distinct integrals. We found it convenient to do this in the following manner. For coefficient $B_{ij}$ we generate all of the diagrams that appear in the expression for the single-component cluster $B_n$, $n=i+j$, and for each diagram we assign $i$ of the points to be species 1 and the remaining $j$ to be species 2. For each of these “base” clusters, we generate all topologically distinct clusters (considering the points as distinguishable) obtained by permuting the points in the cluster, with no regard to the species identity of the points; equivalently we can think of this as permuting the bonds while keeping the species-blind structure of the cluster unchanged. For example, the coefficient $B_{22}$ is evaluated by summing the following clusters (allowing here the points to be made distinguishable by their position as drawn)

$$
\begin{aligned}
B_{22}= & -\frac{1}{8 V}\left[\left(\square+\boldsymbol{\otimes}+\bigotimes\right)\right. \\
& +\left(\boldsymbol{\square}+\boldsymbol{\square}+\boldsymbol{\otimes}+\boldsymbol{\otimes}+\boldsymbol{\bigotimes}+\boldsymbol{\bigotimes}\right) \\
& +\boldsymbol{\bigotimes}]
\end{aligned}
\tag{15}
$$

Although some of the permutations are isomorphs that evaluate to the same value when the integrations are performed, for our calculations we treat all of these permutations as distinct. For any given configuration the molecules can be distinguished by their spatial coordinates, and otherwise, isomorphic diagrams will have distinct values for that configuration. So the calculation of separate averages for isomorphs is not wasteful because they do each add information that is (at least partially) independent. Note in this example that the elementary coefficient $B_{22}$ is multiplied by a factor of 6 when combined to compute the full coefficient $B_4$ as in Eq. (2). One might adopt a convention in which this factor is absorbed in the elementary coefficient, which would cause the expression above to be multiplied by 6. This convention is used in Ref. 11, for example, so one should take care when making such comparisons.

This describes our procedure for generating the diagrams whose sum defines $\gamma$ for the calculation of a particular coefficient $B_{ij}$. With all permutations summed as described above, there is no need to include any other symmetry multipliers. We compute $B_{22}$ and similar terms by evaluating the sum of clusters above via a single MSMC simulation. We do not calculate each diagram separately, because they all are multiplying the same factor, $y_1^2 y_2^2 \rho^4$; the separate values are not needed to apply the mixture VEOS. The coefficient multiplying the entire sum is $-(n-1) / n !$.

We evaluated coefficients for temperatures ranging from $T$=0.6 to 10.0. Temperatures were selected in this interval as needed to provide a good representation of the behavior. An interpolation scheme described elsewhere $^{29}$ was used to evaluate coefficients at temperatures between those where Mayer sampling calculations were performed.

### D. Simulation details
MSMC simulations are performed $^{7}$ in an infinite volume with no periodic boundaries and no truncation of the potential. One molecule is fixed at the origin (effecting the division by $V$ in the formulas above) and the vanishing of $\pi$ at large separations ensures that none of the molecules stray too far from it. For simulations involving three molecules, we performed a separate simulation of $10^9$ steps (where a step represents an attempted MSMC trial) for each mixture coefficient; for coefficients involving four molecules, we performed five independent simulations; for coefficients involving five molecules, we performed eight independent simulations; for coefficients involving six molecules, we performed 10–40 simulations of length $10^8$ steps. The variance of these independent simulations was used to compute confidence limits on the results. We note that simulations of this length may tax the ability of a random number generator to produce uncorrelated random deviates, which can introduce errors in unanticipated ways, so one should (as always) take care to ensure that the random number generator governing the MC process is state-of-the-art. The period of the generator used in this work is about $10^{14}$.

Virial coefficients up to $B_5$ for pure species 1 were taken from Sun and Teja, $^{30}$ while $B_6$ was calculated from MSMC simulations. $^{31}$ Pure species-2 virial coefficients are taken from the same sources, with the temperature scaled by $\varepsilon_{22}$ and the coefficient itself scaled by $\sigma_{22}^{3(n-1)}$. For mixtures where $\varepsilon_{22}$ was not 1, we then obtained pure species-2 virial coefficients at the desired temperatures by interpolation. $^{29}$ Similarly, $B_{12}$ was obtained by scaling temperature by $\varepsilon_{12}$ and the coefficient by $\sigma_{12}^3$.

## III. RESULTS AND DISCUSSION
The expression for the composition-dependent virial coefficient $B_n$ for a binary mixture is given in terms of $(n+1)$ composition-independent coefficients $B_{ij}$, so the full description of the virials $B_2$ to $B_6$ requires evaluation of $25$ $B_{ij}$ coefficients. We did this for four model mixtures, calculating each for about ten temperatures. Thus we performed calculations of approximately 1000 coefficients. Space does not permit us to present all of these data, even graphically, so we give here only representative results for mixture I; the complete set of data is available in electronic form. $^{32}$ These data are presented in Fig. 1, where we plot the $B_{ij}$ coefficients appearing in the virials up to $B_6$. We observed that the mixture coefficients are shifted to the left relative to the pure-species coefficients, which is expected since the mixture epsilon should shift the coefficient behavior to lower temperature.

Several of the following figures present spinodal maps. These plots show in the $y_1$-$\rho$ plane the essential-stability lim-

![](./images/811848115148554240_3.jpg)

FIG. 1. (Color online) Virial coefficients for mixture I for $n$=2–6. Values are made dimensionless by the critical density of the pure LJ fluid (Ref. 23) ($\rho_c$=0.317). Mixture I is symmetric with respect to exchange of the species, so some of the coefficients are identical, as indicated in the legends. Data are presented on a $\sinh^{-1}$ scale. Calculated coefficients are plotted with their 67% confidence limits (which are often smaller than the line thickness) and lines are drawn to join them using an interpolation scheme presented elsewhere (Ref. 29).

its, i.e., the locus of point for which Eq. (4) is satisfied as an equality. We present these curves for temperatures ranging from subcritical to supercritical. At each temperature curves are given for the virial series including terms up to $B_4$ (VEOS4), $B_5$ (VEOS5), and $B_6$ (VEOS6), respectively, to provide information about the degree to which the VEOS is converged at various conditions. To construct these maps, we start at a density and composition where the mixture is stable and then vary density or composition until the spinodal criterion, Eq. (4) (as an equality), is satisfied; this point is noted and used to construct the spinodal line. This process is then repeated with different starting points until we identify a point where the critical criterion, Eq. (7), is also satisfied and the spinodal line is terminated at that point (some exceptions to this procedure for mixtures III and IV are discussed below).

Let us first consider mixture I. Because the pure-species vapor pressures are equal and the unlike interactions promote positive deviations from ideal mixing, the vapor pressure curve goes through a maximum with pressure, ensuring an azeotrope at $y_1$=0.5. Spinodals for mixture I are given in Fig. 2. The curves are symmetric about $y_1$=0.5, consistent with the symmetry of the model parameters. The spinodals at lower temperatures occur at lower densities, toward the left, and convergence of VEOS is good. With increasing temperature the spinodal density increases, the curves move to the right, and some separation is seen between the curves using VEOS to different orders. Below $T$=1.16, for VEOS6 a spin-odal density exists across the entire range of composition. At this temperature a critical point—an azeotropic critical point, $^{5,33}$ in fact—emerges at the equimolar composition and, as the temperature increases this critical point splits into two, each following a sequence of points that terminate lines of metastability that begin with the respective pure species. The locus of all of these points form a line of critical points symmetric about $y_1$=0.5, beginning with the pure-species critical points at $T$=1.31 (according to VEOS6) and dropping continuously to a minimum at $T$=1.16. This behavior is plotted in Fig. 3, which shows the critical line in the $P$-$T$ plane. The line exhibits a cusp at the azeotropic critical point, at which the curve doubles back on itself, following identical $P$-$T$ paths back to each pure component. The cusp is an artifact of the projection onto this plane; in the $P$-$T$-$y_1$ space the critical line is a smooth curve. We note in passing that Munoz and Chimowitz $^{33}$ have shown that at an azeotropic critical point the condition $(\partial P/\partial y_1)_{T,\rho}$=0 will hold (except in unusual cases) and we found that this is true in the case discussed here (results not shown). This result is of particular interest because it suggests that the VEOS can identify a critical azeotrope even though it is not equipped to characterize azeotropy in general. However, the conclusiveness of

![](./images/811848115148554240_4.jpg)

FIG. 2. (Color online) Mixture I spinodals in the composition-density plane. Dotted lines are calculated from VEOS4, solid lines from VEOS5, and dot-dashed lines from VEOS6. Each group of lines from left to right in the figure corresponds to the indicated temperature (in units of $\varepsilon_{11}/k$). Spinodal lines terminate where the critical criterion [Eq. (7)] is satisfied (even though spinodal condition continues to be met at higher density). Black dot-dashed line traversing figure from $y_1$=0 to 1 at the far right is the line of critical points according to VEOS6.

![](./images/811848115148554240_5.jpg)

FIG. 3. Critical line for mixture I in the pressure-temperature plane. Dotted line (circles) is computed from VEOS4, solid line (squares) VEOS5, and dot-dashed line (triangles) VEOS6. Open symbols at left correspond to equimolar mixture and critical lines for each pure substance begin at the right and trace identical curves (owing to the symmetry of the mixture).

![](./images/811848115148554240_6.jpg)

FIG. 4. (Color online) Comparison of mixture I spinodal at T=1.15 to established binodals (Ref. 22) at the same temperature. Dotted and solid lines are computed from VEOS4 and VEOS5, respectively, and end where the VEOS indicates a critical point; the dot-dashed line is computed from VEOS6 and does not exhibit a critical point.

this result is muted by the fact that this equality is a neces- sary consequence of the symmetry of the mixture and it holds for the equimolar mixture at any condition.

MC simulation data are available, which permit us to examine one of the spinodal isotherms in the context of vapor-liquid coexistence data for the mixture. $^{21,22}$ This comparison is presented in Fig. 4. The data are at $T=1.15$ , which is right in the vicinity of the temperature where a critical point emerges at the equimolar composition ( $T=1.15$ is supercritical according to VEOS5 and subcritical according to VEOS6). The likelihood of critical phenomena existing in the vicinity of the azeotrope at this temperature was noted in previous simulation studies. $^{21}$ The spinodals lie above the established vapor-phase binodal, as they must, and are alto- gether consistent with the available coexistence data. At higher pressures the liquid exhibits a miscibility gap, $^{21}$ but this behavior cannot be captured with the virial treatment.

Spinodal maps for mixture II are shown in Fig. 5. For this mixture the species differ only in their size parameters, although the difference is considerable: The volume of a species-1 particle is more than twice that of species 2. The energy parameters are equal for all interactions and conse- quently the range of critical temperatures is rather narrow. The spinodals again start at low temperature toward the left of the figure and shift to the right with increasing tempera- ture. Considering that densities cut roughly in half when res- caled by the species-2 diameters, the VEOS remains valid at the high number densities explored in the lower portion of the plot because this part corresponds to mixtures rich in species 2.

![](./images/811848115148554240_7.jpg)

FIG. 5. (Color online) Same as Fig. 2, but for mixture II.

![](./images/811848115148554240_8.jpg)

FIG. 6. Critical line for mixture II in the pressure-temperature plane. Dotted line (circles) is computed from VEOS4, solid line (squares) VEOS5, and dot-dashed line, VEOS6.

Both pure substances have the same VEOS6 critical point at $T=1.31$ and, at this temperature, the spinodals detach from the pure-species axes at $y_{1}=0$ and $y_{1}=1$ at respective densities, which are in proportion to the molecular vol- ume of each species. Interestingly, in doing this the spinodal curve forms a closed loop, meaning that, after crossing the first spinodal, further increase in density finds another spin- odal that marks a boundary back into a stable phase. We are doubtful however that this behavior is physically meaning- ful, noting that the addition of $B_{6}$ moves the high-density branch of the loop to yet higher density, indicating that the VEOS description is not well converged at the high-density spinodal.

The critical line is presented in Fig. 6. The end points are at the same temperature and because all pair interactions have equal $\varepsilon$ values, the range of temperatures traversed bythe line is quite narrow (the shift of the curve from VEOS5 to VEOS6 is greater than the range covered). The curve moves with increasing pressure from species 1 to species 2, ending at a value that, like the density, is in proportion to the molecular volume. Starting from species 1, the slight de- crease in the critical temperature shows that the addition of smaller but equally energetic molecules to species 1 has the effect of stabilizing the gas. This effect quickly reverses with increasing species-2 mol fraction. From the other end, the addition of larger but equally energetic molecules to pure species 2 immediately destabilizes the gas. The projection of the line onto the pressure- and temperature-composition planes is shown in Fig. 7. The addition of $B_{6}$ does introduce a qualitative change in the shape of the curves, making them noticeably more asymmetric.

Mixture III has a more conventional set of parameters, with species differing in both size and energy parameters and Lorentz-Berthelot mixing rules for the unlike parameters. The estimation of critical points for this mixture suffers from a complication that we did not see in the previous cases. For some of the temperatures the spinodal line does not encoun- ter a point where the critical stability criterion [Eq. (7)] is satisfied. Instead the derivative $(\partial^{2} \mu_{1} / \partial N_{1}^{2})_{T, P, N_{2}}$ goes through an extremum (a positive minimum or a negative maximum) with respect to density before it can cross zero. The derivative $(\partial^{2} \mu_{2} / \partial N_{2}^{2})_{T, P, N_{1}}$ is an alternative indicator of criticality and, on the spinodal, it necessarily has the opposite sign from $(\partial^{2} \mu_{1} / \partial N_{1}^{2})_{T, P, N_{2}}$ , and it too goes through an extre

![](./images/811848115148554240_9.jpg)

FIG. 7. Critical line for mixture II in pressure-composition (top) and temperature-composition (bottom) planes. Dotted line (circles) is computed from VEOS4, solid line (squares) VEOS5, and dot-dashed line VEOS6.

mum, perhaps at a slightly shifted density. The behavior is illustrated in Fig. 8. As the temperature is varied, these derivatives shift and at some point hit the zero line, and do so at the same density, indicating a valid critical point. As the temperature is varied further, the extremum pushes through the zero line, giving rise to two zero-line crossings and thus two critical points. We do not ascribe any significance to the higher-density critical point, because we expect the VEOS to fail as it passes through the nonanalytic critical density, and that its behavior beyond that point is not meaningful. On the other hand, we consider the extremum in $(\partial^{2}\mu_{1}/\partial N_{1}^{2})_{T,P,N_{2}}$ to be notable and perhaps a tentative indicator of criticality that fails to show the bona fide critical point due to the VEOS being insufficiently converged. Thus in the discussion that follows we do not present the higher-density critical point of a pair, but we do indicate points where $(\partial^{2}\mu_{1}/\partial N_{1}^{2})_{T,P,N_{2}}$ exhibits an extremum without crossing zero, which we will call a "near-miss" critical point.

![](./images/811848115148554240_10.jpg)

FIG. 8. Schematic of behavior exhibited by critical-point indicators in mixtures III and IV. Lines are the indicated second derivatives (in arbitrary units) evaluated along the spinodals. The abscissa is a coordinate such as density or mole fraction that measures movement along the spinodal line. Along the spinodal, the two second derivatives are necessarily of opposite sign. The "near-miss" condition occurs when lines turn away from zero before crossing it. Two critical points emerge as temperature is varied. Further changes in temperature may move the second critical point to very high density or see it eliminated entirely.

![](./images/811848115148554240_11.jpg)

FIG. 9. (Color online) Mixture III spinodals in the composition-density plane. Dotted lines are calculated from VEOS4, solid lines from VEOS5, and dot-dashed lines from VEOS6. Each group of lines in the figure corresponds to the indicated temperature (in units of $\varepsilon_{11}/k$). Spinodal lines terminate where the critical criterion [Eq. (7)] is satisfied (even though spinodal condition continues to be met at higher density). The $\times$ symbol indicates the location of a near-miss critical point for VEOS4 and VEOS5, and spinodal lines are drawn past them. Black dot-dashed line at far right is the line of critical points according to VEOS6; the line is drawn thicker at conditions where critical point is given by near-miss criterion (roughly between $y_{1}$=0.01 and 0.6).

Mixture III spinodal maps are drawn in Fig. 9. The aforementioned near-miss critical points according to VEOS4 and VOES5 are marked with an $\times$ symbol and the spinodals are drawn to continue through them (unlike the other cases, where we terminate the spinodal line when the classical conditions of criticality are met). For VEOS6 we draw the full critical line and indicate the near-miss critical region with a thicker line (we do not draw the $\times$ symbols for VEOS6 to help minimize clutter in the figure). In Fig. 10 we show these same spinodals in the pressure-composition plane and we include a comparison to the available simulation data for vapor-liquid coexistence in this mixture. $^{22}$

Comparison to the established coexistence curves at $T$=0.928 in Fig. 10 shows that the near-miss critical point indicated by VEOS does indeed correspond well to a bona fide critical point determined by detailed simulations. This may be a fortunate coincidence, but it does provide some support for the use of the near-miss criterion when trying to estimate the location of critical points from the VEOS. On the other hand, the behavior exhibited in Fig. 9 shows that this approach introduces clear anomalies in the critical lines. The discontinuous changes in the slope of the critical lines seen in Fig. 9 occur because the zero-crossing criterion is replaced by an extremum condition. The overall erratic shape of the curve is perhaps connected to the sensitivity of the critical density (an inflection point) to fine details in the shape of the curve.

In mixture IV the species are the same size (like mixture I) but have energy parameters that obey the conventional geometric-mean mixing rule, $\varepsilon_{12}=(\varepsilon_{11}\varepsilon_{22})^{1/2}$ (like mixture III). Again there is a considerable region in which only the near-miss criterion for estimating the critical point is met. The estimated critical line in the pressure-composition plane

![](./images/811848115148554240_12.jpg)

FIG. 10. (Color online) Spinodals for mixture III in the pressure-composition plane. Top: dotted lines are calculated from VEOS4, solid lines from VEOS5, and dot-dashed lines from VEOS6. Each group of lines in the figure corresponds to the indicated temperature (in units of $\varepsilon_{11}/k$). Termination of lines and use of $\times$ symbol is as in Fig. 9. Bottom: comparison of mixture III spinodal at $T$=0.928 to established binodals (Ref. 22) at the same temperature, with $\times$ symbol indicating the near-miss critical point. Line types are as in top figure.

is shown in Fig. 11. Results from VEOS5 and VEOS6 are in good mutual agreement at lower mole fraction and differ markedly from VEOS4, while at higher mole fractions, VEOS6 departs from the other two. Established data $^{23}$ from molecular simulation are presented for comparison and which, happily enough, show best (albeit imperfect) comparison with VEOS6. The simulation results were computed using mixed-field finite-size scaling techniques that are needed to accommodate the infinite correlation lengths encountered upon approach of the critical point. Given the complications associated with true critical behavior, it is re- markable to see such good agreement with the VEOS calculations, which are based on simulations of no more than six molecules. It would certainly be more gratifying if we were in all cases satisfying the true criteria of criticality in the VEOS application, but at the same time we see that something of practical relevance can be taken from the approximate "near-miss" estimation. This result indicates that the good comparison we saw also with mixture III may not have been a coincidence.

![](./images/811848115148554240_13.jpg)

FIG. 11. Critical line for mixture IV in the pressure-composition plane. Dotted line (circles) is computed from VEOS4; solid line (squares), VEOS5; dot-dashed line (triangles), VEOS6. Line is made thicker and open symbols are used where classical criterion [Eq. (7)] is not satisfied, and critical line is instead eliminated using near-miss critical condition. Symbols indicate temperatures where the virial coefficients were given directly by the Mayer-sampling calculations, and lines connecting them were computed using virial coefficients given by interpolation of the measured coefficients (Ref. 29). In addition, the $\times$ symbols indicate MC simulation data (Ref. 23).

## IV. CONCLUDING REMARKS

Calculation of mixture virial coefficients is no more difficult than calculating the coefficients for the pure substance. The only real complication is the expansion in the number of coefficients needed to fully characterize the behavior. The number of coefficients needed grows with the order of the coefficient $n$ and the number of component species $c$ as $(n+c-1)!/n!/(c-1)!$ (notwithstanding any new symmetries in the clusters). This increase is not a serious obstacle to applications, recognizing that these coefficients can be computed completely independently, so a corresponding increase in available processors can directly remedy any complications.

Identification of criticality (i.e., the problem of locating critical points and lines) is much easier to perform using an analytic equation of state than via studies based on experiment or molecular simulation. This is *a fortiori* when considering the behavior of mixtures, where the expansion of thermodynamic state space introduces a qualitatively new complication with the trial and error that is needed to converge on the location of the critical point. Of course, both experiment and simulation have the benefit of being, if performed with sufficient care, capable of capturing the true, nonanalytic features of the critical behavior. The VEOS, being an analytic equation, is inherently unable to capture the effects of the nonclassical behavior that governs the near-critical system. On the other hand, the VEOS is shown in this work to be sufficiently effective in finding the location of the critical point that it should be considered, if nothing else, as a valuable tool for guiding experiment and simulation studies. Further improvements might be found in the use of crossover methods, $^{34}$ which have been employed in various contexts to correct analytic models by introducing universal scaling properties that fluids exhibit upon approach to a critical point. However in at least some of these methods, knowledge of the location of the critical point is required as an input.

Conclusions about the effectiveness of VEOS for this purpose are only tentative, inasmuch as we studied here only a quite simple model for molecular systems. Various studies of pure-substance criticality with the VEOS shows that it can be effective (particularly in connection to the critical temperature, but less so with respect to the critical density) for multiatomics, such as the normal alkanes $^{8}$ and quadrupolar diatomics, $^{14}$ but application to water $^{9,10}$ (and perhaps other polar molecules) may require further developments. On the other hand, we presently considered a variety of mixture types within the LJ model and saw that the VEOS is effective

to a useful degree in application to all of them. Nevertheless we do not find the introduction of the near-miss critical cri- terion to be a satisfactory means to locate criticality in these systems, even though it shows some effectiveness in this task. Rather we would prefer to develop a reformulation of the virial approach to increase its overall ability to describe dense-gas PVT behavior, so that the correct conditions of criticality can be applied to identify critical points in all cases. This is a larger problem that merits further study and development.

Apart from the application in connection to criticality, the VEOS can be effectively coupled with molecular simu- lation to develop efficient methods for evaluation of equilib- ria of gases with liquids and solids. Methods such as Gibbs ensemble MC (Ref. 35) and Gibbs-Duhem integration $^{36}$ can be combined with an analytic equation of state to yield hy- brid methods that can be more versatile and efficient than the approaches based on direct simulation of both phases. $^{37}$ The VEOS is ideally suited for this task because it is based on the same model that is used in the molecular simulations.

One of the most appealing features of the VEOS in ap- plication to mixtures is its ability to capture rigorously the composition dependence of the equation of state. Required of course is a mixing rule for the intermolecular interactions, but this is much less of a problem than contriving the same at the level of thermodynamic-model parameters. If $ab$ initio methods can be brought to bear on this task, we may see developed a route to first-principles prediction of mixture critical points. Clearly much development is needed before reaching this appealing goal.

## ACKNOWLEDGMENTS
Funding for this research was provided by Grant Nos. CTS-0414439 and CHE-0626305 from the U.S. National Science Foundation and the University at Buffalo School of Engineering and Applied Sciences. Computational support was provided by the University at Buffalo Center for Com- putational Research. Additional resources were provided by the Open Science Grid, which is supported by the National Science Foundation and the U.S. Department of Energy's Office of Science. We are grateful to Dr. Javier Pérez- Pellitero for providing data from Ref. 23 in tabular form.

$^{1}$ W. G. Chapman, K. E. Gubbins, G. Jackson, and M. Radosz, Fluid Phase Equilib. 52, 31 (1989); W. G. Chapman, S. G. Sauer, D. Ting, and A. Ghosh, ibid. 217, 137 (2004); E. A. Muller and K. E. Gubbins, Ind. Eng. Chem. Res. 40, 2193 (2001); I. G. Economou, ibid. 41, 953 (2002).

$^{2}$ A. Klamt, COSMO-RS: From Quantum Chemistry to Fluid Phase Ther- modynamics and Drug Design (Elsevier, Amsterdam, 2005); F. Eckert and A. Klamt, AIChE J. 48, 369 (2002); S. T. Lin and S. I. Sandler, Ind. Eng. Chem. Res. 41, 899 (2002).

$^{3}$ D. Frenkel and B. Smit, Understanding Molecular Simulation: From Al gorithms to Applications, 2nd ed. (Academic, San Diego, 2002).

$^{4}$ P. van Konynenburg and R. L. Scott, Philos. Trans. R. Soc. London, Ser. A 298, 495 (1980); A. Bolz, U. K. Dieters, C. J. Peters, and T. W. de Loos, Pure Appl. Chem. 70, 2233 (1998); J. Kolafa, I. Nezbeda, J. Pav- licek, and W. R. Smith, Fluid Phase Equilib. 146, 103 (1998); J. Kolafa, I. Nezbeda, J. Pavlicek, and W. R. Smith, Phys. Chem. Chem. Phys. 1,4233 (1999); J. Kolafa, ibid. 1, 5665 (1999); D. Furman, S. Dattagupta, and R. B. Griffiths, Phys. Rev. B 15, 441 (1977).

$^{5}$ I. Nezbeda, J. Kolafa, and W. R. Smith, J. Chem. Soc., Faraday Trans.93, 3073 (1997).

$^{6}$ E. A. Mason and T. H. Spurling, The Virial Equation of State (Pergamon, Oxford, 1969).

$^{7}$ J. K. Singh and D. A. Kofke, Phys. Rev. Lett. 92, 220601 (2004); Erra- tum: 95, 249903 (2005).

$^{8}$ A. J. Schultz and D. A. Kofke, "Virial coefficients of model alkanes," J. Chem. Phys. (submitted).

$^{9}$ K. M. Benjamin, A. J. Schultz, and D. A. Kofke, J. Phys. Chem. C 111,16021 (2007); K. M. Benjamin, J. K. Singh, A. J. Schultz, and D. A. Kofke, J. Phys. Chem. B 111, 11463 (2007); K. M. Benjamin, A. J. Schultz, and D. A. Kofke, Ind. Eng. Chem. Res. 45, 5566 (2006).

$^{10}$ K. M. Benjamin, A. J. Schultz, and D. A. Kofke, J. Phys. Chem. B 113,7810 (2009).

$^{11}$ C. Vega, Mol. Phys. 98, 973 (2000).

$^{12}$ C. Vega, J. M. Labaig, L. G. MacDowell, and E. Sanz, J. Chem. Phys.113, 10398 (2000).

$^{13}$ C. Menduina, C. McBride, and C. Vega, Phys. Chem. Chem. Phys. 3,1289 (2001).

$^{14}$ L. G. MacDowell, C. Menduina, C. Vega, and E. de Miguel, J. Chem. Phys. 119, 11367 (2003); L. G. MacDowell, C. Menduina, C. Vega, and E. De Miguel, Phys. Chem. Chem. Phys. 5, 2851 (2003).

$^{15}$ E. Helfand and F. H. Stillinger, J. Chem. Phys. 49, 1232 (1968); A.Baram, M. W. Maddox, and J. S. Rowlinson, Mol. Phys. 76, 1093(1992); A. Baram, M. W. Maddox, and J. S. Rowlinson, ibid. 79, 589(1993).

$^{16}$ C. Barrio and J. R. Solana, J. Chem. Phys. 119, 3826 (2003).

$^{17}$ A. Y. Vlasov, X. M. You, and A. J. Masters, Mol. Phys. 100, 3313(2002).

$^{18}$ C. G. Joslin, C. G. Gray, S. Goldman, B. Tomberli, and W. Li, Mol. Phys.89, 489 (1996).

$^{19}$ T. Boublik, Fluid Phase Equilib. 182, 47 (2001); A. Ewald, W. Jepson, and J. Rowlinson, Faraday Discuss. 15, 238 (1953); B. Tomberli, S. Goldman, and C. G. Gray, Fluid Phase Equilib. 187-188, 111 (2001).

$^{20}$ A. H. Harvey, Fluid Phase Equilib. 130, 87 (1997).

$^{21}$ A. Z. Panagiotopoulos, U. W. Suter, and R. C. Reid, Ind. Eng. Chem. Fundam. 25, 525 (1986).

$^{22}$ M. Mehta and D. A. Kofke, Chem. Eng. Sci. 49, 2633 (1994).

$^{23}$ J. Pérez-Pellitero, P. Ungerer, G. Orkoulas, and A. Mackie, J. Chem. Phys. 125, 054515 (2006).

$^{24}$ J. W. Tester and M. Modell, Thermodynamics and Its Applications, 3rd ed. (Prentice Hall PTR, Upper Saddle River, NJ, 1997).

$^{25}$ J. M. Prausnitz, R. N. Lichtenthaler, and E. G. de Azevedo, Molecular Thermodynamics of Fluid-Phase Equilibria (Prentice-Hall, Englewood Cliffs, 1986).

$^{26}$ D. A. McQuarrie, Statistical Mechanics (Harper & Row, New York,1976); J. P. Hansen and I. R. McDonald, Theory of Simple Liquids, 3rd ed. (Academic, London, 2006).

$^{27}$ D. A. Kofke and D. Frenkel, in Handbook of Molecular Modeling, edited by S. Yip (Kluwer Academic, Dordrecht, 2004); D. A. Kofke, Mol. Phys.102, 405 (2004); Fluid Phase Equilib. 228-229, 41 (2005).

$^{28}$ C. H. Bennett, J. Comput. Phys. 22, 245 (1976).

$^{29}$ A. J. Schultz and D. A. Kofke, Mol. Phys. 107, 1431 (2009).

$^{30}$ T. F. Sun and A. S. Teja, J. Phys. Chem. 100, 17365 (1996).

$^{31}$ A. J. Schultz and D. A. Kofke, "Sixth, seventh and eighth virial coeffi- cients of the Lennard-Jones model," Mol. Phys. (submitted).

$^{32}$ See EPAPS Document No. E-JCPSA6-130-032923 for values of all cal- culated virial coefficients. For more information on EPAPS, see http:// www.aip.org/pubservs/epaps.html.

$^{33}$ F. Munoz and E. H. Chimowitz, J. Chem. Phys. 99, 5438 (1993).

$^{34}$ L. X. Sun, S. B. Kiselev, and J. F. Ely, Fluid Phase Equilib. 233, 204(2005); S. B. Kiselev and D. G. Friend, ibid. 162, 51 (1999); S. B. Kiselev, ibid. 147, 7 (1998); L. Lue and J. M. Prausnitz, J. Chem. Phys.108, 5529 (1998); C. McCabe and S. B. Kiselev, Ind. Eng. Chem. Res.43, 2839 (2004); S. B. Kiselev and J. F. Ely, Fluid Phase Equilib. 252,57 (2007); S. B. Kiselev and J. F. Ely, ibid. 222-223, 149 (2004); S. B. Kiselev and J. F. Ely, ibid. 174, 93 (2000).

$^{35}$ A. Z. Panagiotopoulos, Mol. Phys. 61, 813 (1987); Mol. Simul. 9, 1(1992); in Observation, Prediction and Simulation of Phase Transitions in Complex Fluids, NATO ASI Series C Vol. 460, edited by M. Baus(Kluwer Academic, Dordrecht, 1995).

$^{36}$ D. A. Kofke, Mol. Phys. 78, 1331 (1993); J. Chem. Phys. 98, 4149(1993); Adv. Chem. Phys. 105, 405 (1999).

$^{37}$ M. Mehta and D. A. Kofke, Mol. Phys. 79, 39 (1993).