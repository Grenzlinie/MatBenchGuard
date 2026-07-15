# An Extension of a Kinetic Theory of Polymer Crystallization through the Exclusion of Negative Barriers

Jerry I. Scheinbeim, Louis Petrone, and Brian A. Newman*

Department of Mechanics and Materials Science, Rutgers University, Piscataway, New Jersey 08855-0909

Received March 12, 1991; Revised Manuscript Received September 29, 1992

ABSTRACT: The simplest version of the Lauritzen-Hoffman (LH) model of polymer crystallization, which applies to infinitely long model polymer molecules crystallizing on an existing substrate of infinite width, is reexamined. The mathematical expressions for the model free energy barriers are observed to take on negative values at high supercooling. Since such negative barriers appear to be physically unrealizable for the crystallization process, the LH model is extended by imposing a mathematical constraint on the expressions for the barriers, to forbid them from ever being negative. The extended model contains one parameter $\gamma$ which varies from 0 to 1 and is analogous to the parameter $\psi$ of the LH model. For all values of $\gamma$ less than 1, the extended model predicts a finite lamellar thickness at every supercooling; moreover, this thickness, at large undercooling, decreases monotonically with increasing undercooling, in agreement with experiment but in marked contrast to the LH model which exhibits the well-known $\delta l$ catastrophe. The relative insensitivity of the calculated lamellar thicknesses to the parameter $\gamma$ supports the use of $\gamma=0$ as a first approximation for mathematical convenience in practice.

## I. Introduction

Recently, the crystallization of poly(vinylidene fluoride) ($\text{PVF}_2$) in the presence of high electric fields has been studied both experimentally and theoretically. Of the four well-known crystalline forms $\alpha, \beta, \gamma$, and $\delta$ (or II, I, III, and IV) of $\text{PVF}_2$, the phase with the largest spontaneous polarization and potential for applications is the $\beta$-phase. Crystallization of $\text{PVF}_2$ from a concentrated solution of tricresyl phosphate in the presence of a high electric field was observed$^1$ to produce $\beta$-phase crystals, with dipoles oriented in the field direction, during the initial stages of crystallization followed by the growth of unoriented $\alpha$-phase crystals (nonpolar) as crystallinity increased and the tricresyl phosphate content decreased by evaporation. The decrease in tricresyl phosphate content and subse- quent crystal growth behavior suggests that the local electric field in the solution region changes. Other experimental and theoretical$^{2,3}$ studies of crystallization of $\text{PVF}_2$ from the melt in the presence of a high static electric field have been made and were found to give $\gamma$-phase crystals which however did not show crystal orientation. As part of the continuing effort to understand the structure-property relationships of $\text{PVF}_2$ and because of its practical importance, our ultimate goal-despite the complexity of the system described-is to develop a theory or model which can account for its crystallization behavior from concentrated solutions in the presence of an electric field.

As in the case of isothermal crystallization of $\alpha$- and $\gamma$-phases from the melt in an electric field,$^3$ a theory of isothermal crystallization of $\alpha$-, $\beta$-, and $\delta$-phases from concentrated solution in an electric field would be based on "classical" and "polymer" theories of nucleation and growth in the absence of an applied field. Most impor- tantly, the nucleation barrier or activation free energy barrier for nucleation would certainly be different in the presence of the field than in its absence; and this barrier has been seen to be of fundamental importance in the theories of polymer crystallization, the simplest of which is the LH or Lauritzen-Hoffman theory.$^{4,5}$ One possibly unrealistic feature which seems to have been incorporated into the LH theory in order to simplify it is that the nucleation barrier is not constrained in the theory to take on only nonnegative values.$^6$ The word "barrier" connotes a positive quantity, and, furthermore, the LH theory is based on transition state theory in which the barrier corresponds to an intermediate configuration or transition state of the system which is at a free energy maximum relative to some initial and final states of the system.$^9$ Moreover, the LH theory exhibits, in contrast with experiment, the $\delta l$ catastrophe wherein the calculated average lamellar thickness $l$ suddenly passes through a minimum and becomes infinite at a temperature $T_c$, corresponding to a moderately large undercooling; and, in fact, the nucleation barrier in this theory is positive for all $T > T_c$, is zero at $T = T_c$, and is negative for all $T < T_c$ for the special case which Lauritzen and Hoffman$^{4,5}$ have recently considered. Therefore, prior to developing an extension of the LH theory which would involve ascer- taining the effect of an electric field on the nucleation barrier, we try to extend the LH theory to larger under- cooling by incorporating into it the assumption that free energy barriers cannot be negative. Note that, unlike in the LH theory of polymer crystallization, barriers in classical nucleation theory are never negative; however, the classical theory does not explicitly take into account polymer chain folding, and, for that reason, we have not yet considered modifying the Marand and Stein theory$^2$ of crystallization from the melt to treat the $\text{PVF}_2$/tricresyl phosphate crystallizing solution.

The remainder of this paper is organized as follows. In section II, the LH model is described. The kinetic treatment of the LH model is given in section III. The rate constants needed for this treatment are determined in section IV. Next, our extension of the LH model is described in section V; the conditions which determine the sign of $\Delta \phi_1$, the free energy of formation of that portion of a model polymer molecule which crystallizes first on an existing crystal, are found in section VI. A summary of the expressions for the barriers in our model is given in section VII along with the expressions for the average lamellar thickness. In section VIII, the variable trans- formations required as a preliminary to numerical inte- gration are introduced. Results and discussion appear in section IX, and conclusions are given in section X.

## II. The Lauritzen-Hoffman Model

The model to be extended is one version$^{4,5}$ of the well- known Lauritzen-Hoffman (LH) model of polymer crys-

tallization. Our description of this version is as follows.
The model polymer molecules are assumed to be infinitely long and crystallize on an existing crystalline face or substrate which is assumed to be infinitely wide (i.e., the fact that its width is finite is ignored). A sequence of length $l$ of polymer segments of width $a$ and thickness $b$ as well as the volume associated with that sequence-which is taken to be a parallelepiped of length $l$, width $a$, and thickness $b$-is designated as a stem. Only stems of length $l$ can crystallize on an existing face of length $l$, but the length $l$, the lamellar thickness, can vary from crystal to crystal. Any sequence of length $l$ of segments of a model molecule can be placed first on a given face and, upon placement, is designated as the first stem. The free energy of formation of the first stem is

$$\Delta \phi_{1}-\Delta \phi_{0} \equiv \Delta \phi_{1}-0 \quad \text { or } \quad \Delta \phi_{1}=2 a b \sigma_{\mathrm{e}}{ }^{\prime}+2 b l \sigma-a b l \Delta f$$

where $\Delta f>0$ is the free energy of fusion per unit volume at a temperature $T$ below the melting point $T_{\mathrm{m}}{ }^{\circ}$ of the model polymer (i.e., of a crystal of very large $l$ ) and $\Delta f=$ 0 at $T=T_{\mathrm{m}}{ }^{\circ}$; where $\sigma$ is the lateral surface free energy per unit area (i.e., that associated with the surfaces of area $b l$ and $a l$ of a stem); and where $\sigma_{\mathrm{e}}{ }^{\prime}$ is the surface free energy per unit area associated with the cilium that protrudes through each of the surfaces of area $a b$ of the first stem. Recently, ${ }^{4-7} \sigma_{\mathrm{e}}{ }^{\prime}$ has been assumed to be zero; generally, one can assume $^{11}$ that $0 \leq \sigma_{\mathrm{e}}{ }^{\prime} \leq \sigma_{\mathrm{e}}$. All surface free energies per unit area in the model are assumed to be independentof $T$ and $l$. (See Figure 2a of ref 4 or Figure 22 of ref 5.) The placement of each subsequent stem involves (1) the destruction of the cilium associated with one of the surfaces of area $a b$ of an adjacent stem already crystallized, (2) an adjacent reentry and the formation of a tight fold associated with two surfaces of area $a b$, and (3) the formation of a cilium associated with the remaining surface of area $a b$ of the stem being placed. Only adjacent reentry and hence only tight folding is incorporated in this version of the model.

The free energy of formation of the $\nu$ th stem $(\nu>1)$ is therefore

$$\Delta \phi_{\nu}-\Delta \phi_{\nu-1}=-a b \sigma_{\mathrm{e}}{ }^{\prime}+2 a b \sigma_{\mathrm{e}}+a b \sigma_{\mathrm{e}}{ }^{\prime}-a b l \Delta f$$

or

$$\Delta \phi_{\nu}-\Delta \phi_{\nu-1}=2 a b \sigma_{\mathrm{e}}-a b l \Delta f \equiv-E$$

where $\Delta \phi_{\nu}$ is the free energy of formation of a group of $\nu$ stems (relative to $\Delta \phi_{0}=0$ ) where $\sigma_{\mathrm{e}}$ is the surface free energy per unit area associated with half of a fold. Iteration of $\Delta \phi_{\nu}=\Delta \phi_{\nu-1}-E(\nu>1)$ gives

$$
\begin{aligned}
\Delta \phi_{\nu} & =\Delta \phi_{1}-(\nu-1) E \\
& =2 b l \sigma+2 a b \sigma_{\mathrm{e}}{ }^{\prime}-2 a b \sigma_{\mathrm{e}}+\nu a b\left(2 \sigma_{\mathrm{e}}-l \Delta f\right)
\end{aligned}
$$

In order that stem additions subsequent to the placement of the first stem be thermodynamically favorable, i.e., in order that they would in fact occur, one must impose the constraint $-E<0$ and consequently $l>2 \sigma_{\mathrm{e}} / \Delta f$. Stems of smaller length are unstable and disappear. By contrast, $\Delta \phi_{1}$ can be positive, zero, or negative; $E>0$ guarantees that $\Delta \phi_{\nu}<0$ will occur for finite $\nu$. Note the sign conventions for $\Delta \phi_{1}$ and $E$.

### III. Kinetic Treatment of the Lauritzen-Hoffman Model

Our description of the kinetic treatment $^{4,5}$ of the LH model is as follows. The following assumptions are made:

1. Assume that transition state theory can be utilized to describe the kinetics of the LH model of polymer crystallization.

2. Assume that the formation (crystallization) of a single stem is an elementary process or elementary reaction, that the destruction (melting) of a single stem is an elementary process or elementary reaction, and that transition state theory can be applied to these two elementary processes with a single transition state corresponding to a relative free energy maximum or barrier thus occurring between each two integral values of $\nu$ on a plot of $\Delta \phi_{\nu}$ vs $\nu$.

3. Assume that only one stem at a time can be formed or destroyed.

The kinetic problem is to derive an expression for the net rate $S_{\nu}(l, T)$ at which stems of length $l$ (and width $a$ ) pass over or surmount the $\nu$ th free energy barrier at temperature $T$. The problem requires consideration of the set of connected elementary reactions

$$0 \underset{B_{1}}{\stackrel{A_{0}}{\rightleftarrows}} 1 \underset{B}{\stackrel{A}{\rightleftarrows}} 2 \underset{B}{\stackrel{A}{\rightleftarrows}} 3 \underset{B}{\stackrel{A}{\rightleftarrows}} 4 \cdots$$

where $A$ is the rate constant for the forward reaction $\nu \rightarrow$ $\nu+1(\nu \geq 1)$ and $B$ is that for the reverse reaction $\nu+1$ $\rightarrow \nu(\nu \geq 1)$, and where $A_{0}$ and $B_{1}$ are the analogous rate constants for the $\nu=0 \rightleftarrows \nu=1$ reactions. Solution of this problem in the steady-state approximation gives

$$S_{\nu}(l, T)=\frac{N_{0} A_{0}(A-B)}{A-B+B_{1}} \equiv S(l, T)$$

for all $\nu$, where $N_{0}$ is the number of sites or locations available for the placement of a first stem. The total net rate at which stems (i.e., the net rate including stems of all possible values of $l$ ) pass over the $\nu$ th barrier at temperature $T$ is given, for all $\nu$, by

$$S_{\text {Total }}(T)=\sum_{l=l_{1}}^{\infty} S(l, T)$$

where $l_{1}$ is the smallest allowed value of $l$ which satisfies the constraint $l>2 \sigma_{\mathrm{e}} / \Delta f$. Note that $l$ is a discrete variable-the smallest increment in $l$ that can be made is the monomer repeat length $l_{\mathrm{u}}$. To find $l_{1}$, first write $l=$ $m l_{\mathrm{u}}$, where $m$ is a positive integer. Then $l>2 \sigma_{\mathrm{e}} / \Delta f$ implies $m>\left(2 \sigma_{\mathrm{e}} / \Delta f\right) / l_{\mathrm{u}}$; that is, $m$ is greater than or equal to the smallest integer greater than $\left(2 \sigma_{\mathrm{e}} / \Delta f\right) / l_{\mathrm{u}}$, and, therefore, $l_{1}=[1+\operatorname{INT}(X)] l_{\mathrm{u}}$, where $X \equiv\left(2 \sigma_{\mathrm{e}} / \Delta f\right) / l_{\mathrm{u}}$ and $\operatorname{INT}(X)$ designates the integer part of $X$. Substituting $l_{\mathrm{u}}=2 \sigma_{\mathrm{e}} /$ $X \Delta f$ into the expression for $l_{1}$ gives $l_{1}=[(1+\operatorname{INT}(X)) /$ $X]\left(2 \sigma_{\mathrm{e}} / \Delta f\right)$. To a good approximation, $(1+\operatorname{INT}(X)) / X$ $\approx 1$ (i.e., $X$ is sufficiently greater than 1 ) so that $l_{1} \approx 2 \sigma_{\mathrm{e}} /$ $\Delta f$.

Finally, one assumes that $\sum_{l=l_{1}}^{\infty} S(l, T) \approx 1 / l_{\mathrm{u}} \int_{l_{1}}^{\infty} S(l, T) d l$; and the kinetically-determined average lamellar thickness is then given by

$$l(T)=\frac{\int_{l_{1}}^{\infty} l S(l, T) d l}{\int_{l_{1}}^{\infty} S(l, T) d l}$$

### IV. Determination of the Rate Constants

To obtain expressions for $A_{0}, B_{1}, A$, and $B$, one must first determine expressions for the free energy barriers for the relevant reactions $\nu \rightleftarrows \nu+1(\nu \geq 0)$. Let $E_{1}$ be the free energy barrier to the destruction of the first stem; then $\Delta \phi_{1}+E_{1}$ is the barrier to the formation of the first stem in order that $\left(\Delta \phi_{1}+E_{1}\right)-E_{1}=\Delta \phi_{1}$. Let $E_{2}$ be the free energy barrier to the formation of each subsequent stem; then $E+E_{2}$ is the barrier to the destruction of each such stem in order that $\left(E+E_{2}\right)-E_{2}=E$. Now, one does not know the free energy barrier to the formation of the first

stem. At least, one does know that it depends on what length $l'$ of a fully adsorbed stem of length $l$ actually crystallizes before the barrier is surmounted. If $l' = 0$, then none of the free energy of crystallization (i.e., $-abl\Delta f$) is released before the barrier is surmounted, and clearly, $\Delta \phi_{1}+E_{1}=2ab\sigma_{e}'+2bl\sigma$ and $E_{1}=abl\Delta f$. In general, then, for $0\leq l'\leq l$

$$
\begin{align*}
\Delta \phi_{1}+E_{1}&=2ab\sigma_{e}'+2bl\sigma - abl'\Delta f \quad \text{and}\\
E_{1}&=ab(l-l')\Delta f
\end{align*}
$$

Since $l'$ is unknown, a parameter $\psi \equiv l'/l$ with $0\leq \psi \leq 1$ is introduced in order that all possible so-called apportionments of the free energy of fusion $abl\Delta f$ between the rate constants for the formation and destruction of a first stem (i.e., for the forward and reverse reactions $0\rightleftarrows 1$) can be considered. Thus

$$
\begin{align*}
\Delta \phi_{1}+E_{1}&=2ab\sigma_{e}'+2bl\sigma-\psi abl\Delta f \quad \text{and}\\
E_{1}&=(1-\psi)abl\Delta f.
\end{align*}
$$

Note that the greater the amount $\psi abl\Delta f$ of the free energy of fusion which is in fact "apportioned" (i.e., the greater the value of $\psi$ or $l'$), the smaller the value of both $\Delta \phi_{1}+$ $E_{1}$ and $E_{1}$ (for a given $l$ and $T$). A very similar interpretation of $\psi$ has been discussed recently. $^{7}$

Similarly, for each subsequent stem, let $l''$ ($0\leq l''\leq l$) be the length of a fully adsorbed stem which actually crystallizes before the barrier to the formation of the stem is surmounted. Then

$$
E_{2}=2ab\sigma_{e}-abl''\Delta f \quad \text{and} \quad E+E_{2}=ab(l-l'')\Delta f
$$

Define the apportionment parameter $\hat{\psi} \equiv l''/l$ with $0\leq \hat{\psi}$ $\leq 1$ so that

$$
E_{2}=2ab\sigma_{e}-\hat{\psi} abl\Delta f \quad \text{and} \quad E+E_{2}=(1-\hat{\psi})abl\Delta f.
$$

Finally, utilizing transition state theory

$$
\begin{align*}
A_{0}&=\frac{kT}{h}e^{-(\Delta \phi_{1}+E_{1}+\Delta \hat{F})/kT}\equiv \beta e^{-(\Delta \phi_{1}+E_{1})/kT}\\
B_{1}&=\beta e^{-E_{1}/kT};\quad A=\beta e^{-E_{2}/kT};\quad B=\beta e^{-(E+E_{2})/kT}
\end{align*}
$$

where $\Delta \hat{F}$ is the contribution to each barrier as a result of retardations in the transport of a polymer chain through the liquid to the substrate or vice versa. Note that $B/A$ does not depend on $\hat{\psi}$ and that $B_{1}/A_{0}$ does not depend on $\psi$ as required.

### V. Extension of the Lauritzen-Hoffman Model

As implied throughout the above discussion, the application of transition state theory to the elementary processes of single stem formation and destruction presumes that there is a single relative free energy maximum $^{9}$ or barrier between each two integral values of $\nu$ on a plot of $\Delta \phi_{\nu}$ vs $\nu$. Consequently, $\Delta \phi_{1}+E_{1}, E_{2}$, and $E+E_{2}$ should never be negative. Clearly, $E_{1}=(1-\psi)abl\Delta f$ and $E+E_{2}=(1-\hat{\psi})abl\Delta f$ are never negative; however, the expressions given above for $\Delta \phi_{1}+E_{1}$ and $E_{2}$ can be negative. In fact, $E_{2}$, for example, is negative for all $l$ such that $2\sigma_{e}/\hat{\psi}\Delta f < l$ for a given $\Delta f, \hat{\psi}$, and $\sigma_{e}$. We propose to extend the LH model by incorporating into the model the assumption that free energy barriers cannot be negative; i.e., only apportionments of the free energy of fusion which result in a nonnegative barrier will be allowed.

In order to incorporate this constraint into the model, first note that $\Delta \phi_{1}+E_{1}=2ab\sigma_{e}'+2bl\sigma-\psi abl\Delta f$ is never negative when $\Delta \phi_{1}$ is positive since then $abl\Delta f < 2ab\sigma_{e}'$ $+2bl\sigma$ always holds and $\psi abl\Delta f < 2ab\sigma_{e}'+2bl\sigma$ follows.
However, when $\Delta \phi_{1}$ is negative, the expression $2ab\sigma_{e}'+$ $2bl\sigma-\psi abl\Delta f$ can be negative. The requirement that $\Delta \phi_{1}$ $+E_{1}\geq 0$ hold when $\Delta \phi_{1}$ is negative implies that one is not allowed to apportion all of the free energy of fusion $abl\Delta f$ when $\Delta \phi_{1}$ is negative. If the amount $\psi abl\Delta f$ of the free energy of fusion which is apportioned were to exceed $2ab\sigma_{e}'$ $+2bl\sigma$, then $\Delta \phi_{1}+E_{1}$ would be negative. The maximum amount which can be apportioned is indeed $2ab\sigma_{e}'+2bl\sigma$, and therefore one has, when $\Delta \phi_{1}<0$

$$
\Delta \phi_{1}+E_{1}=\xi(2ab\sigma_{e}'+2bl\sigma)
$$

where $\xi$ is an apportionment parameter with $0\leq \xi \leq 1$. Using $(\Delta \phi_{1}+E_{1})-E_{1}=\Delta \phi_{1}$ or $E_{1}=(\Delta \phi_{1}+E_{1})-\Delta \phi_{1}$ gives

$$
\begin{align*}
E_{1}=\xi(2ab\sigma_{e}'+2bl\sigma)-(2ab\sigma_{e}'+2bl\sigma - abl\Delta f)=\\
abl\Delta f-(1-\xi)(2ab\sigma_{e}'+2bl\sigma)
\end{align*}
$$

Observe that the requirement that $\Delta \phi_{1}+E_{1}\geq 0$ holds when $\Delta \phi_{1}$ is negative is equivalent to the physically realistic requirement that the barrier $E_{1}$ to the destruction of the first stem cannot be smaller than the free energy increase $(-\Delta \phi_{1})$ that occurs upon its destruction. Note that $abl\Delta f$ $-(2ab\sigma_{e}'+2bl\sigma)=-\Delta \phi_{1}$. Also, this physically realistic requirement implies that an adsorbed first stem cannot completely crystallize before the barrier to the formation of that stem is surmounted, i.e., that the upper limit on $l'$ is less than $l$ when $\Delta \phi_{1}$ is negative. This upper limit on $l'$ is determined later. For $\Delta \phi_{1}>0$, the expressions $\Delta \phi_{1}$ $+E_{1}=2ab\sigma_{e}'+2bl\sigma+\psi abl\Delta f$ and $E_{1}=(1-\psi)abl\Delta f$ still hold with $0\leq \psi \leq 1$ and $0\leq l'\leq l$.

At this point, a simple change of variable is introduced for convenience. Define $\lambda \equiv 1-\xi$ with $0\leq \lambda \leq 1$.

Now observe that, although the free energy of fusion is $abl\Delta f$ when $\Delta \phi_{1}$ is positive or negative, the free energy of fusion which can be apportioned is $abl\Delta f$ when $\Delta \phi_{1}$ is positive but is $(2ab\sigma_{e}'+2bl\sigma)$ when $\Delta \phi_{1}$ is negative. Also, the free energy of fusion that is in fact apportioned is $\psi abl\Delta f$ when $\Delta \phi_{1}$ is positive but is $\lambda(2ab\sigma_{e}'+2bl\sigma)$ when $\Delta \phi_{1}$ is negative. Clearly then, the fraction of the free energy of fusion which can be apportioned that is apportioned is $\psi$ when $\Delta \phi_{1}$ is positive but is $\lambda$ when $\Delta \phi_{1}$ is negative. If we always choose the same value for $\lambda$ and $\psi$, then, over the whole range of values for $\Delta \phi_{1}$, the fraction of the free energy of fusion which can be apportioned has the same value. Let $\gamma$ denote any particular value which is chosen for both $\psi$ and $\lambda$, where $0\leq \gamma \leq 1$.

Note that equal values of $\psi$ and $\lambda$ do not imply the same value of $l'$ (except when $\Delta \phi_{1}=0$, as will become evident); as usual $\psi \equiv l'/l$ but an expression for $\lambda$ in terms of $l'$ or vice versa remains to be obtained. In our approach, then, $l'$ depends at least on the sign of $\Delta \phi_{1}$, and yet we utilize only one parameter, $\gamma$—the fraction of the free energy of fusion which can be apportioned that is apportioned—which is a constant over the whole range of values for $\Delta \phi_{1}$.

In summary, the barriers in terms of the apportionment parameter $\gamma$ are

$$
\left.
\begin{align*}
\Delta \phi_{1}+E_{1}&=(1-\gamma)(2ab\sigma_{e}'+2bl\sigma)\\
E_{1}&=abl\Delta f-\gamma(2ab\sigma_{e}'+2bl\sigma)
\end{align*}
\right\} \quad \text{for } \Delta \phi_{1}\leq 0
$$

$$
\left.
\begin{align*}
\Delta \phi_{1}+E_{1}&=2ab\sigma_{e}'+2bl\sigma-\gamma abl\Delta f\\
E_{1}&=(1-\gamma)abl\Delta f
\end{align*}
\right\} \quad \text{for } \Delta \phi_{1}\geq 0
$$

where we now observe that $(1-\gamma)(2ab\sigma_{e}'+2bl\sigma)=2ab\sigma_{e}'$ $+2bl\sigma-\gamma abl\Delta f$ when $\Delta \phi_{1}=0$; i.e., $\Delta \phi_{1}+E_{1}$ is a continuous

function of $l$ and $\Delta f$ at the points $(l, \Delta f)$ for which $\Delta \phi_{1}=$
0. Note that the greater the value of the apportionment parameter $\gamma$, the smaller the value of both $\Delta \phi_{1}+E_{1}$ and $E_{1}$.

An expression of $l'$ is not needed in order to evaluate $S_{\text{Total}}(T)$ and $l(T)$. However, an expression for $l'$ in terms of $\lambda$ and vice versa will be derived in order to see how $l'$ depends on other quantities in our model. Given $\Delta \phi_{1}+E_{1}=(1-\lambda)(2ab\sigma_{e}'+2bl\sigma)$ for $\Delta \phi_{1}<0$, one can first find $\psi$ when $\Delta \phi_{1}<0$ holds in terms of $\lambda$ by equating the expressions
$$(1-\lambda)(2ab\sigma_{e}'+2bl\sigma)=2ab\sigma_{e}'+2bl\sigma-\psi abl\Delta f$$
whence
$$\psi=\lambda\left(\frac{2ab\sigma_{e}'+2bl\sigma}{abl\Delta f}\right)$$
or
$$\psi=\lambda(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$$

Clearly, equating these expressions and expressing $\psi$ when $\Delta \phi_{1}<0$ in terms of $\lambda$ are valid since decreasing $2ab\sigma_{e}'+2bl\sigma$ by an amount $\psi abl\Delta f$ must be equivalent to decreasing $2ab\sigma_{e}'+2bl\sigma$ by $\lambda(2ab\sigma_{e}'+2bl\sigma)$. Note that the expression $(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$ is always less than 1 when $\Delta \phi_{1}$ is negative. To see this, simply observe that $\Delta \phi_{1}<0$ implies $2ab\sigma_{e}'+2bl\sigma<abl\Delta f$ and then divide both sides of this inequality by $abl\Delta f$. But $\psi \equiv l'/l$ for all values of $\Delta \phi_{1}$ so that
$$l'=\lambda l(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$$

Note that since $\lambda$ cannot exceed 1, the largest possible value of $l'$, i.e., the upper limit on $l'$, is $l(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$ for $\Delta \phi_{1}<0$; as mentioned previously, this upper limit is indeed less that $l$ for $\Delta \phi_{1}<0$.

For completeness, one can also find $\lambda$ when $\Delta \phi_{1}>0$ holds in terms of $\psi$ by equating the expressions
$$(1-\lambda)(2ab\sigma_{e}'+2bl\sigma)=2ab\sigma_{e}'+2bl\sigma-\psi abl\Delta f$$
whence
$$\lambda=\frac{\psi}{(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)}$$

Clearly, equating these expressions and expressing $\lambda$ when $\Delta \phi_{1}>0$ in terms of $\psi$ are valid since decreasing $2ab\sigma_{e}'+2bl\sigma$ by an amount $\psi abl\Delta f$ must be equivalent to decreasing $2ab\sigma_{e}'+2bl\sigma$ by $\lambda(2ab\sigma_{e}'+2bl\sigma)$. Here again, $\psi \equiv l'/l$, and $\lambda=(l'/l)(1/(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f))$. Note that $(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$ is always greater than 1 when $\Delta \phi_{1}$ is positive.

In summary, then, for $\Delta \phi_{1} \leq 0$, one chooses a value from 0 to 1 for the parameter $\gamma$, whence $\lambda=\gamma$, and then calculates $\psi=\lambda(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$. For $\Delta \phi_{1} \geq 0$, one chooses a value from 0 to 1 for the parameter $\gamma$, whence $\psi=\gamma$, and then calculates $\lambda=\psi/(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$. Thus
$$\left.
\begin{array}{l}
\lambda=\gamma \\
\psi=\lambda(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)
\end{array}
\right\} \text{ for } \Delta \phi_{1} \leq 0$$

$$\left.
\begin{array}{l}
\psi=\gamma \\
\lambda=\frac{\psi}{(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)}
\end{array}
\right\} \text{ for } \Delta \phi_{1} \geq 0$$

For all $\Delta \phi_{1}$, one can calculate $l'$ from $l'=\psi l$ or from $l'=\lambda l(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$.

Incidentally, the constraint $2ab\sigma_{e}'+2bl\sigma-\psi abl\Delta f \geq 0$ combined with $0 \leq \psi \leq 1$ implies that the inequality
$$0 \leq \psi \leq \text{ the smaller of 1 and } (2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)$$
must be satisfied, and clearly our theory has satisfied it. Similarly, the constraint $abl\Delta f-\lambda(2ab\sigma_{e}'+2bl\sigma) \geq 0$ combined with $0 \leq \lambda \leq 1$ implies that the inequality
$$0 \leq \lambda \leq \text{ the smaller of 1 and } \frac{1}{(2\sigma_{e}'/l\Delta f+2\sigma/a\Delta f)}$$
must be satisfied, and clearly our theory has satisfied it.

The approach developed above can readily be applied to incorporate into the model the constraint that $E_{e}$ be nonnegative. Here, $E_{2}=2ab\sigma_{e}-\hat{\psi} abl\Delta f$ can be negative when $E$ is positive, and $E$ is always positive (except when $l=2\sigma_{e}/\Delta f$, which gives $E=0$). The requirement $E_{2} \geq 0$ implies that one is not allowed to apportion all of the free energy of fusion $abl\Delta f$. If the amount $\hat{\psi} abl\Delta f$ which is apportioned were to exceed $2ab\sigma_{e}$, then $E_{2}$ would be negative. Therefore, one has $E_{2}=\eta 2ab\sigma_{e}$ where $\eta$ is an apportionment parameter with $0 \leq \eta \leq 1$. $E+E_{2}=-2ab\sigma_{e}+abl\Delta f+\eta 2ab\sigma_{e}=abl\Delta f-(1-\eta)2ab\sigma_{e}$. For convenience, make the change of variable $\theta \equiv 1-\eta$ with $0 \leq \theta \leq 1$ so that for all $l$ and $\Delta f$
$$E_{2}=(1-\theta)(2ab\sigma_{e}) \text{ and } E+E_{2}=abl\Delta f-\theta(2ab\sigma_{e})$$

Observe that the barrier $E+E_{2}$ to the destruction of the second and each subsequent stem cannot be smaller than the free energy increase $E$ that occurs upon its destruction, which implies that an adsorbed second or subsequent stem cannot completely crystallize before the barrier to the formation of the stem is surmounted, i.e., that the upper limit, determined below, on $l''$ is less than $l$.

To find an expression for $l''$ in terms of $\theta$, one first finds $\hat{\psi}$ in terms of $\theta$ by equating the expressions for $E_{2}$; i.e.
$$(1-\theta)(2ab\sigma_{e})=2ab\sigma_{e}-\hat{\psi} abl\Delta f$$
whence
$$\hat{\psi}=\theta(2\sigma_{e}/l\Delta f)$$

Clearly, equating these expressions and expressing $\hat{\psi}$ in terms of $\theta$ are valid since decreasing $2ab\sigma_{e}$ by an amount $\hat{\psi} abl\Delta f$ must be equivalent to decreasing $2ab\sigma_{e}$ by $\theta(2ab\sigma_{e})$. Note that the constraint $2ab\sigma_{e}-\hat{\psi} abl\Delta f \geq 0$ implies that the inequality $0 \leq \hat{\psi} \leq 2\sigma_{e}/l\Delta f$ must be satisfied; since 0 $\leq \theta \leq 1$ holds, we have indeed satisfied this inequality. Also note that $2\sigma_{e}/l\Delta f$ is always less than or equal to 1 since $l \geq 2\sigma_{e}/\Delta f$ has been established. (Incidentally, $2ab\sigma_{e}-\hat{\psi} abl\Delta f \geq 0$ does not imply constraints $l \leq 2\sigma_{e}/\hat{\psi} \Delta f$, $\Delta f$ $\leq 2\sigma_{e}/\hat{\psi} l$, or $\sigma_{e} \geq \hat{\psi} l\Delta f/2$.) Finally, recalling that $\hat{\psi}=l''/l$ and substituting above gives $l''=\theta(2\sigma_{e}/\Delta f)$.

In the special case $\gamma=\theta=0$, our model reduces to the case $\psi=\hat{\psi}=0$ of the LH model which permits negative barriers for nonzero $\psi$.

## VI. Determination of the Sign of $\Delta \phi_{1}$

At this point, one needs to determine when $\Delta \phi_{1}$ is positive, zero, and negative. Now $\Delta \phi_{1}=2ab\sigma_{e}'+2bl\sigma-abl\Delta f \geq 0$ implies $bl(2\sigma-a\Delta f) \geq -2ab\sigma_{e}'$; and there are three cases to consider.

Case a: $2\sigma-a\Delta f>0$ or $\Delta f<2\sigma/a$. Then the inequality $l>-2ab\sigma_{e}'/[b(2\sigma-a\Delta f)]$ is always satisfied since $l$ is always greater than zero, and hence $\Delta \phi_{1}>0$ holds.

Case b: $2\sigma-a\Delta f=0$ or $\Delta f=2\sigma/a$. Then $\Delta \phi_{1}=2ab\sigma_{e}'$, which is always positive or zero depending on $\sigma_{e}'$.

Thus, combining cases a and b, we have $\Delta \phi_{1} \geq 0$ for all $l$ when $\Delta f \leq 2\sigma/a$, where $\Delta \phi_{1}=0$ when both $\sigma_{e}'=0$ and $\Delta f=2\sigma/a$.

Case c: $2\sigma-a\Delta f<0$ or $\Delta f>2\sigma/a$. Then $\Delta\phi_1\geq0$ implies
$-bl(a\Delta f-2\sigma)\geq-2ab\sigma_e'$ or $l\leq(2\sigma_e'/\Delta f)/(1-2\sigma/a\Delta f)\equiv l_0$.
Thus, when $\Delta f>2\sigma/a$, $\Delta\phi_1\geq0$ holds for $l\leq l_0$, and $\Delta\phi_1$
$\leq0$ holds for $l\geq l_0$. (Observe that as $\Delta f\to2\sigma/a$ from
values greater than $2\sigma/a$, $l_0\to\infty$.) There is, however, one
further condition to consider here. Recall that $l\geq2\sigma_e/\Delta f$
has been established. If $l_0<2\sigma_e/\Delta f$ holds, then $l>l_0$ holds
and consequently $\Delta\phi_1<0$ would hold for all $l$. To
determine when $l_0<2\sigma_e/\Delta f$ holds, simply write $(2\sigma_e'/\Delta f)/$
$(1-2\sigma/a\Delta f)<2\sigma_e/\Delta f$, and noting that $2\sigma/a\Delta f<1$, rearrange
this inequality to get $2\sigma/a\Delta f<(\sigma_e-\sigma_e')/\sigma_e$. Now, if $\sigma_e\leq$
$\sigma_e'$, this inequality would be $2\sigma/a\Delta f<0$, which is never
satisfied; hence, $l_0<2\sigma_e/\Delta f$ never occurs when $\sigma_e\leq\sigma_e'$. If
$\sigma_e>\sigma_e'$, $l_0<2\sigma_e/\Delta f$ occurs when $\Delta f>(2\sigma/a)[\sigma_e/(\sigma_e-\sigma_e')]$.
Thus, if $\sigma_e>\sigma_e'$ and $2\sigma/a<\Delta f\leq(2\sigma/a)[\sigma_e/(\sigma_e-\sigma_e')]$, $\Delta\phi_1$
$\geq0$ holds for $l\leq l_0$ and $\Delta\phi_1\leq0$ holds for $l\geq l_0$, but for
$\Delta f>(2\sigma/a)[\sigma_e/(\sigma_e-\sigma_e')]$, $\Delta\phi_1<0$ holds for all $l$.

### VII. Expression for $S_{\text{Total}}(T)$ and $l(T)$

If $\sigma_e\leq\sigma_e'$, our model with no negative barriers has
$$\text{(1) } \Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\gamma abl\Delta f \quad \text{for } \Delta f\leq2\sigma/a$$

$$\text{(2) } \Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\gamma abl\Delta f \quad \text{for } \Delta f>2\sigma/a \text{ and } l\leq l_0$$

$$\text{(2) } \Delta\phi_1+E_1=(1-\gamma)(2ab\sigma_e'+2bl\sigma) \quad \text{for } \Delta f>2\sigma/a \text{ and } l\geq l_0$$

and if $\sigma_e>\sigma_e'$
$$\text{(1) } \Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\gamma abl\Delta f \quad \text{for } \Delta f\leq2\sigma/a$$

$$\text{(2) } \Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\gamma abl\Delta f \quad \text{for } 2\sigma/a<\Delta f\leq\frac{2\sigma}{a}\left(\frac{\sigma_e}{\sigma_e-\sigma_e'}\right) \text{ and } l\leq l_0$$

$$\text{(2) } \Delta\phi_1+E_1=(1-\gamma)(2ab\sigma_e'+2bl\sigma) \quad \text{for } 2\sigma/a<\Delta f\leq\frac{2\sigma}{a}\left(\frac{\sigma_e}{\sigma_e-\sigma_e'}\right) \text{ and } l\geq l_0$$

$$\text{(3) } \Delta\phi_1+E_1=(1-\gamma)(2ab\sigma_e'+2bl\sigma) \quad \text{for } \Delta f>\frac{2\sigma}{a}\left(\frac{\sigma_e}{\sigma_e-\sigma_e'}\right)$$

The purpose of categories (1)-(3) will be seen shortly.

When $\Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\gamma abl\Delta f$, $E_1=(1-$
$\gamma)abl\Delta f$, which we call case I.

When $\Delta\phi_1+E_1=(1-\gamma)(2ab\sigma_e'+2bl\sigma)$, $E_1=abl\Delta f-$
$\gamma(2ab\sigma_e'+2bl\sigma)$, which we call case II.

One always has
$$E_2=(1-\theta)(2ab\sigma_e)$$

$$E+E_2=-2ab\sigma_e+abl\Delta f+E_2=abl\Delta f-\theta2ab\sigma_e$$

Also
$$S(l,T)=\frac{N_0A_0(1-B/A)}{1-B/A+B_1/A}$$
where $B/A=e^{-E/kT}$, $B_1/A=e^{-(E_1-E_2)/kT}$, and $A_0=$
$\beta e^{-(\Delta\phi_1+E_1)/kT}$.

Abbreviate $c'\equiv2ab\sigma_e'/kT$, $c\equiv2ab\sigma_e/kT$, and $\alpha\equiv2\sigma/$
$a\Delta f$, and recall $l_1=2\sigma_e/\Delta f$. Then $c/l_1=ab\Delta f/kT$, $\alpha c/l_1=$
$2b\sigma/kT$, and $E/kT=-c+(c/l_1)l$.

For case I
$$\frac{\Delta\phi_1+E_1}{kT}=\frac{2ab\sigma_e'}{kT}+\frac{2bl\sigma}{kT}-\frac{\gamma abl\Delta f}{kT}=c'+\frac{c}{l_1}(\alpha-\gamma)l$$

$$\frac{E_1-E_2}{kT}=\frac{(1-\gamma)abl\Delta f}{kT}-\frac{(1-\theta)2ab\sigma_e}{kT}=$$
$$\frac{c}{l_1}(1-\gamma)l-(1-\theta)c$$

For case II
$$\frac{\Delta\phi_1+E_1}{kT}=\frac{(1-\gamma)(2ab\sigma_e'+2bl\sigma)}{kT}=$$
$$(1-\gamma)c'+\frac{\alpha c}{l_1}(1-\gamma)l$$

$$\frac{E_1-E_2}{kT}=\frac{abl\Delta f-\gamma(2ab\sigma_e'+2bl\sigma)}{kT}-\frac{(1-\theta)2ab\sigma_e}{kT}=$$
$$\frac{c}{l_1}(1-\alpha\gamma)l-\gamma c'-(1-\theta)c$$

For case I
$$S_{\text{I}}(l,T)=\frac{\beta N_0e^{-c'}e^{-(\alpha-\gamma)cl/l_1}(1-e^ce^{-cl/l_1})}{1-e^ce^{-cl/l_1}+e^{(1-\theta)c}e^{-(1-\gamma)cl/l_1}}$$

For case II
$$S_{\text{II}}(l,T)=\frac{\beta N_0e^{-(1-\gamma)c'}e^{-(1-\gamma)\alpha cl/l_1}(1-e^ce^{-cl/l_1})}{1-e^ce^{-cl/l_1}+e^{(1-\theta)c}e^{\gamma c'}e^{-(1-\alpha\gamma)cl/l_1}}$$

For any $\Delta f$ in category (1), then
$$S_{\text{Total}}^{(1)}(T)=\frac{1}{l_u}\int_{l_1}^{\infty}S_{\text{I}}(l,T)dl \quad \text{and}$$
$$l^{(1)}(T)=\frac{\int_{l_1}^{\infty}lS_{\text{I}}(l,T)dl}{\int_{l_1}^{\infty}S_{\text{I}}(l,T)dl}$$

For any $\Delta f$ in category (2), then
$$S_{\text{Total}}^{(2)}(T)=\frac{1}{l_u}\int_{l_1}^{l_0}S_{\text{I}}(l,T)dl+\frac{1}{l_u}\int_{l_0}^{\infty}S_{\text{II}}(l,T)dl$$
and
$$l^{(2)}(T)=\frac{\int_{l_1}^{l_0}lS_{\text{I}}(l,T)dl+\int_{l_0}^{\infty}lS_{\text{II}}(l,T)dl}{\int_{l_1}^{l_0}S_{\text{I}}(l,T)dl+\int_{l_0}^{\infty}S_{\text{II}}(l,T)dl}$$

For any $\Delta f$ in category (3), then
$$S_{\text{Total}}^{(3)}(T)=\frac{1}{l_u}\int_{l_1}^{\infty}S_{\text{II}}(l,T)dl \quad \text{and}$$
$$l^{(3)}(T)=\frac{\int_{l_1}^{\infty}lS_{\text{II}}(l,T)dl}{\int_{l_1}^{\infty}S_{\text{II}}(l,T)dl}$$

For purposes of comparison, the LH model which
permits negative barriers has, for all $l$ and $\Delta f$
$$\Delta\phi_1+E_1=2ab\sigma_e'+2bl\sigma-\psi abl\Delta f \quad \text{and}$$
$$E_2=2ab\sigma_e-\hat{\psi}abl\Delta f$$
so that
$$\frac{E_1-E_2}{kT}=(1-\psi+\hat{\psi})\frac{c}{l}l-c$$

and
$$
S^{(\mathrm{LH})}(l, T)=\frac{\beta N_{0} e^{-c^{\prime}} e^{-(\alpha-\psi) c l / l_{1}}\left(1-e^{c} e^{-c l / l_{1}}\right)}{1-e^{c} e^{-c l / l_{1}}+e^{c} e^{-(1-\psi+\dot{\psi}) c l / l_{1}}}
$$
and
$$
S_{\text {Total }}^{(\mathrm{LH})}(l, T)=\frac{1}{l_{\mathrm{u}}} \int_{l_{\mathrm{i}}}^{\infty} S^{(\mathrm{LH})}(l, T) d l \quad \text { and }
$$
$$
I^{(\mathrm{LH})}(T)=\frac{\int_{l_{1}}^{\infty} l S^{(\mathrm{LH})}(l, T) d l}{\int_{l_{1}}^{\infty} S^{(\mathrm{LH})}(l, T) d l}
$$

As is the case in the LH model, our model has two parameters. The most logical choice for $\theta$ is $\theta=\gamma$; however, even with $\theta=\gamma$, our integrals cannot be evaluated analytically. There seems to be no special case (other than $\theta=\gamma=0$ ) for which they could be evaluated analytically. At this point then, we proceed without setting $\theta=\gamma$.

### VIII. Evaluation of the $S_{\text {Total }}(T)$ and $I(T)$, The Variable Transformations for the Numerical Integrations

The required numerical integrations were easily performed interactively on the VAX using the IMSL subroutine DQDAGS. $^{10}$ Integrals to be evaluated using DQDAGS cannot have an infinite limit of integration. One way to proceed before using DQDAGS is to make a change of integration variable. Although DQDAGS can integrate functions with end-point singularities (when the end points are finite), a change of variable which results in a transformed integrand, which is bounded at all points including the finite end points in the new range of integration, is preferable to a change of variable which yields an improper integral albeit with finite integration limits. For each of the integrals appearing in $S_{\text {Total }}^{(1)}(T)$, $S_{\text {Total }}^{(2)}(T)$, and $S_{\text {Total }}^{(3)}(T)$, a variable transformation which resulted in a proper integral was in fact found. The same transformations did not transform the corresponding integrals in the numerators of $I^{(1)}, I^{(2)}(T)$, and $I^{(3)}(T)$ into proper integrals; however, the transformed integrands were of the form $(-\ln x) f(x)$ with the singularity resulting only from the factor $\ln x$ as $x \rightarrow 0$. This end-point singularity could be handled by DQDAGS.

Consider first the integral in $S_{\text {Total }}^{(1)}(T)$. The variable transformation consists of defining
$$
x \equiv e^{(1-\gamma) c} e^{-(1-\gamma) c l / l_{1}}
$$
Note that $x(l \rightarrow \infty)=0$; the constant $e^{(1-\gamma) c}$, i.e., the $l$-independent factor, is chosen so that $x\left(l=l_{1}\right)=1$. Solving for $l$ in terms of $x$ gives $l=l_{1}[1-\ln x /(1-\gamma) c]$ provided $\gamma \neq 1$. Then $d l=-l_{1} /(1-\gamma) c(1 / x) \mathrm{d} x$. Furthermore, $e^{-(\alpha-\gamma) c l / l_{1}}=e^{-(\alpha-\gamma) c} x^{(\alpha-\gamma) /(1-\gamma)}, e^{-c l / l_{1}}=e^{-c} x^{1 /(1-\gamma)}$, and $e^{-(1-\gamma) c l / l_{1}}$ $=e^{-(1-\gamma) c} x$ so that
$$
\begin{aligned}
& S_{\text {Total }}^{(1)}(T)= \\
& \quad \frac{\beta N_{0}}{l_{\mathrm{u}}} \frac{e^{-c^{\prime}} e^{-(\alpha-\gamma) c} l_{1}}{(1-\gamma) c} \int_{0}^{1} \frac{x^{(\alpha-\gamma) /(1-\gamma)}\left(1-x^{1 /(1-\gamma)}\right)}{1-x^{1 /(1-\gamma)}+e^{(1-\theta) c} e^{-(1-\gamma) c} x}\left(\frac{1}{x}\right) \mathrm{d} x
\end{aligned}
$$

Simplying gives
$$
S_{\text {Total }}^{(1)}(T)=\frac{\beta N_{0}}{l_{\mathrm{u}}} \frac{e^{-c^{\prime}} e^{-(\alpha-\gamma) c} l_{1}}{(1-\gamma) c} \int_{0}^{1} \frac{x^{(\alpha-1) /(1-\gamma)}\left(1-x^{1 /(1-\gamma)}\right)}{1-x^{1 /(1-\gamma)}+e^{-(\theta-\gamma) c} x} \mathrm{~d} x
$$

This is one of the integrals that was evaluated numerically by DQDAGS. Designate the integrand above as $f_{1}(x)$.

Using the same variable transformation to evaluate the numerator of $I^{(1)}(T)$ gives
$$
\begin{aligned}
I^{(1)}(T)=\frac{\int_{0}^{1} l_{1}\left[1-\frac{(\ln x)}{(1-\gamma) c}\right] f_{1}(x) \mathrm{d} x}{\int_{0}^{1} f_{1}(x) \mathrm{d} x}= \\
l_{1}+\frac{l_{1}}{(1-\gamma) c} \frac{\int_{0}^{1}(-\ln x) f_{1}(x) \mathrm{d} x}{\int_{0}^{1} f_{1}(x) \mathrm{d} x}
\end{aligned}
$$

Next, using the transformation on the integral $\int_{l_{1}}^{l_{0}} S_{\mathrm{I}}$ $(l, T) d l$ appearing in $S_{\text {total) }}^{(2)}(T)$ gives
$$
\int_{l_{1}}^{l_{0}} S_{\mathrm{I}}(l, T) \mathrm{d} l=\beta N_{0} \frac{e^{-c^{\prime}} e^{-(\alpha-\gamma) c} l_{1}}{(1-\gamma) c} \int_{x_{0}}^{1} f_{1}(x) \mathrm{d} x
$$
where
$$
x_{0} \equiv x\left(l=l_{0}\right)=e^{(1-\gamma) c} e^{-(1-\gamma) c l_{0} / l_{1}}=e^{(1-\gamma) c} e^{-(1-\gamma) c^{\prime} /(1-\alpha)}
$$
with $l_{0} \equiv 2 \sigma_{\mathrm{e}}^{\prime} /(1-\alpha) \Delta f$ as defined previously. Similarly, the integral $\int_{l_{1}}^{l_{0}} l S_{\mathrm{I}}(l, T) d l$ appearing in $I^{(2)}(T)$ becomes
$$
\begin{aligned}
& \int_{l_{1}}^{l_{0}} l S_{\mathrm{I}}(l, T) \mathrm{d} l= \\
& \frac{\beta N_{0} e^{-c^{\prime}} e^{-(\alpha-\gamma) c} l_{1}}{(1-\gamma) c}\left\{l_{1} \int_{x_{0}}^{1} f_{1}(x) \mathrm{d} x+\frac{l_{1}}{(1-\gamma) c} \int_{x_{0}}^{1}(-\ln x) f_{1}(x) \mathrm{d} x\right\}
\end{aligned}
$$

A different transformation is made on the integral $\int_{l_{0}}^{\infty} S_{\mathrm{II}}(l, T) d l$ also appearing in $S_{\text {Total }}^{(2)}(T)$. Here, define
$$
x \equiv e^{(1-\gamma)\left(c-c^{\prime}\right)} e^{-(1-\gamma) \alpha c l / l_{1}}
$$
Again $x(l \rightarrow \infty)=0$; the constant $e^{(1-\gamma)\left(c-c^{\prime}\right)}$ is chosen so that $x\left(l=l_{0}\right)=x_{0}$, which is given above. Solving for $l$ gives $l=$ $\left(l_{1} / \alpha c\right)\left[c-c^{\prime}-(\ln x) /(1-\gamma)\right]$ provided $\gamma \neq 1$. Then $\mathrm{d} l=$ $-l_{1} /(1-\gamma) \alpha c(1 / x) \mathrm{d} x$. Furthermore, $e^{-(1-\gamma) \alpha c l / l_{1}}=e^{-(1-\gamma)\left(c-c^{\prime}\right)} x$, $e^{-c l / l_{1}}=e^{-\left(c-c^{\prime}\right) / \alpha} x^{1 /(1-\gamma) \alpha}$, and $e^{-(\alpha-\gamma) c l / l_{1}}=e^{-\left(c-c^{\prime}\right)(1-\alpha \gamma) / \alpha}$ $x^{(1-\alpha \gamma) /(1-\gamma) \alpha}$. Substituting gives
$$
\begin{aligned}
\int_{l_{0}}^{\infty} S_{\mathrm{II}}(l, T) \mathrm{d} l=\frac{\beta N_{0} e^{-(1-\gamma) c^{\prime}} e^{-(1-\gamma)\left(c-c^{\prime}\right)} l_{1}}{(1-\gamma) \alpha c} & × \\
\int_{0}^{x_{0}} x(1 & \left.-e^{c} e^{-\left(\left(c-c^{\prime}\right) / \alpha\right)} x^{1 /(1-\gamma) \alpha}\right)\left(\frac{1}{x}\right) \mathrm{d} x /\left[1-\right. \\
e^{c} e^{-\left(\left(c-c^{\prime}\right) / \alpha\right)} x^{1 /(1-\gamma) \alpha} & \left.+e^{(1-\theta) c} e^{\gamma c^{\prime}} e^{-\left(\left(c-c^{\prime}\right) / \alpha\right)(1-\alpha \gamma)} x^{(1-\alpha \gamma) /(1-\gamma) \alpha}\right]= \\
& \frac{\beta N_{0} e^{-(1-\gamma) c} l_{1}}{(1-\gamma) \alpha c} \int_{0}^{x_{0}} 1-e^{c} e^{-\left(c-c^{\prime} / \alpha\right)} x^{1 /(1-\gamma) \alpha} \mathrm{d} x / \\
& {\left[1-e^{c} e^{-\left(\left(c-c^{\prime}\right) / \alpha\right)} x^{1 /(1-\gamma) \alpha}+e^{-(\theta-\gamma) c} e^{c} e^{-\left(\left(c-c^{\prime}\right) / \alpha\right)} x^{(1-\alpha \gamma) /(1-\gamma) \alpha}\right] }
\end{aligned}
$$

Designate the integrand above as $f_{2}(x)$. Similarly, the integral $\int_{l_{0}}^{\infty} l S_{\mathrm{II}}(l, T) d l$ appearing in $I^{(2)}(T)$ becomes
$$
\begin{aligned}
\int_{l_{0}}^{\infty} l S_{\mathrm{II}}(l, T) \mathrm{d} l=\frac{\beta N_{0} e^{-(1-\gamma) c} l_{1}}{(1-\gamma) \alpha c} & \left\{\frac{\left(c-c^{\prime}\right)}{\alpha c} l_{1} \int_{0}^{x_{0}} f_{2}(x) \mathrm{d} x+\right. \\
& \left.\frac{l_{1}}{(1-\gamma) \alpha c} \int_{0}^{x_{0}}(-\ln x) f_{2}(x) \mathrm{d} x\right\}
\end{aligned}
$$

Thus
$$
\begin{aligned}
S_{\text {Total }}^{(2)}(T)=\left(\frac{\beta N_{0}}{l_{\mathrm{u}}} \frac{e^{-c^{\prime}} e^{-(\alpha-\gamma) c} l_{1}}{(1-\gamma) c} \int_{x_{0}}^{1} f_{1}(x) \mathrm{d} x\right)+ \\
\left(\frac{\beta N_{0}}{l_{\mathrm{u}}} \frac{e^{-(1-\gamma) c} l_{1}}{(1-\gamma) \alpha c} \int_{0}^{x_{0}} f_{2}(x) \mathrm{d} x\right)
\end{aligned}
$$

and
$$
l^{(2)}(T)=\frac{\left(\frac{1}{\beta N_{0}} \int_{l_{1}}^{l_{0}} l S_{\mathrm{I}}(l, T) \mathrm{d} l\right)+\left(\frac{1}{\beta N_{0}} \int_{l_{0}}^{\infty} l S_{\mathrm{II}}(l, T) \mathrm{d} l\right)}{\frac{l_{\mathrm{u}}}{\beta N_{0}} S_{\text {Total }}^{(2)}(T)}
$$
with the appropriate expressions for the integrals and $S_{\text {Total }}^{(2)}(T)$ to be substituted above.

Finally, consider the integral in $S_{\text {Total }}^{(3)}(T)$. The variable transformation to be made on this integral is
$$
x \equiv e^{(1-\gamma) \alpha c} e^{-(1-\gamma) \alpha c l / l_{1}}
$$
Again $x(l \to \infty)=0$ and the constant $e^{(1-\gamma) \alpha c}$ is chosen so that $x(l=l_{1})=1$. Solving for $l$ gives $l=l_{1}[1-(\ln x) /(1-\gamma) \alpha c]$ provided $\gamma \neq 1$. Then $\mathrm{d} l=-[l_{1} /(1-\gamma) \alpha c](1 / x) \mathrm{d} x$. Furthermore, $e^{-(1-\gamma) \alpha c l / l_{1}}=e^{-(1-\gamma) \alpha c} x$, $e^{-c l / l_{1}}=e^{-c} x^{1 /(1-\gamma) \alpha}$, and $e^{-(1-\alpha \gamma) c l / l_{1}}=e^{-(1-\alpha \gamma) c} x^{(1-\alpha \gamma) /(1-\gamma) \alpha}$ so that
$$
\begin{aligned}
S_{\text {Total }}^{(3)}(T)= & \frac{\beta N_{0}}{l_{\mathrm{u}}} \frac{e^{-(1-\gamma)\left(c^{\prime}+\alpha c\right) l_{1}}}{(1-\gamma) \alpha c} \times \\
& \int_{0}^{1} \frac{\left(1-x^{1 /(1-\gamma) \alpha}\right)}{1-x^{1 /(1-\gamma) \alpha}+e^{-\theta c} e^{\gamma\left(c^{\prime}+\alpha c\right)} x^{(1-\alpha \gamma) /(1-\gamma) \alpha}} \mathrm{d} x
\end{aligned}
$$

Designate the integrand above as $f_{3}(x)$. Using the same transformation to evaluate the numerator of $l^{(3)}(T)$ gives
$$
l^{(3)}(T)=l_{1}+\frac{l_{1}}{(1-\gamma) \alpha c} \frac{\int_{0}^{1}(-\ln x) f_{3}(x) \mathrm{d} x}{\int_{0}^{1} f_{3}(x) \mathrm{d} x}
$$

## IX. Results and Discussion

A VAX FORTRAN program was written to evaluate the required mathematical expressions. All calculations were done with double precision using the model parameter values given in Figure 3 of ref 4; namely, $a=b=5 \times 10^{-8}$ $\mathrm{cm}, \sigma=10 \mathrm{erg} / \mathrm{cm}^{2}, \sigma_{\mathrm{e}}=100 \mathrm{erg} / \mathrm{cm}^{2}, T_{\mathrm{m}}{ }^{\circ}=500 \mathrm{~K}, \Delta h$ $=3 \times 10^{9} \mathrm{ergs} / \mathrm{cm}^{3}$, and $\Delta f=\left(T_{\mathrm{m}}{ }^{\circ}-T\right) \Delta h / T_{\mathrm{m}}{ }^{\circ}$, where $\Delta h$ is the enthalpy of fusion at $T=T_{\mathrm{m}}{ }^{\circ}$. The average lamellar thickness calculated from the LH model is independent of $\sigma_{\mathrm{e}}{ }^{\prime}$; this is true for our model only for $\Delta f \leq 2 \sigma / a$, however. Other quantities such as $S_{\text {Total }}(T)$ do depend on $\sigma_{\mathrm{e}}{ }^{\prime}$ even in the LH model, and physically, $^{11}$ one expects $0 \leq \sigma_{\mathrm{e}}{ }^{\prime} \leq$ $\sigma_{\mathrm{e}}$. In the case $\sigma_{\mathrm{e}}{ }^{\prime} \equiv 0$, our model is slightly simpler, for then
$$
\left.\begin{array}{c}
\Delta \phi_{1}+E_{1}=2 b l \sigma-\gamma a b l \Delta f \\
E_{1}=(1-\gamma) a b l \Delta f
\end{array}\right\} \quad \Delta f \leq 2 \sigma / a
$$

$$
\left.\begin{array}{c}
\Delta \phi_{1}+E_{1}=(1-\gamma) 2 b l \sigma \\
E_{1}=a b l \Delta f-\gamma 2 b l \sigma
\end{array}\right\} \quad \Delta \phi>2 \sigma / a
$$

Let us investigate our model in detail for the case $\sigma_{\mathrm{e}}{ }^{\prime}=$ 0 first; this is also the somewhat arbitrary choice for $\sigma_{\mathrm{e}}{ }^{\prime}$ made for the calculations $s^{1,2}$ for the LH model. For the values of $a, \sigma, T_{\mathrm{m}}{ }^{\circ}$, and $\Delta h$ given above, the temperature $T^{*}$ for which $\Delta f=2 \sigma / a$ is $T^{*}=433^{1} /{ }_{3} \mathrm{~K}$.

Given the parameter values above and now with the choice $\theta=\gamma$, the calculated average lamellar thickness vs temperature curves ( $l$ vs $T$ ) are plotted in Figure 1a for the selected values of $\gamma=0,1 / 4$, and $1 / 2$. (Results for $\gamma>$ $1 / 2$ will be discussed later.) Some of the data used to construct these plots are given in Table I. (For $\Delta f \leq 2 \sigma / a$, the average lamellar thickness is given by the expression for $l^{(1)}(T)$ given previously, and, for $\Delta f>2 \sigma / a$, it is given by the expression for $l^{(3)}(T)$ also given previously.) Clearly, $l$ decreases monotonically with decreasing $T$ in agreement with typical experimental behavior. For most supercoolings, the magnitude of the $l$ values is on the order of 25-125 Å, which is quite reasonable. Note that, at least for all values of $\Delta f>2 \sigma / a, l$ at a given $T$ increases with increasing $\gamma$. Also, the numerical results shown in Figure 1a indicate that $l$ vs $T$ is relatively insensitive to the value of $\gamma$.

![](./images/812292486662717442_1.jpg)

Figure 1. (a) Plots of average lamellar thickness (Å) vs temperature (K) for $\gamma=0,1 / 4$, and $1 / 2$, each with $\sigma_{e}{ }^{\prime}=0$ and $\theta$ $=\gamma$. See section IX for $a, b, \sigma, \sigma_{\mathrm{e}}, T_{\mathrm{m}}{ }^{\circ}$, and $\Delta h$ which are the same for all of the figures. At $T=433^{1} /{ }_{3} \mathrm{~K}$ (i.e., $=2 \sigma / a$ ), $\Delta \phi_{1}$ $=0$. For $T \geq 433^{1} /{ }_{3} \mathrm{~K}, \Delta \phi_{1} \geq 0$ and $\psi=\gamma$ and $\lambda=\gamma(a \Delta f / 2 \sigma)$. For $T \leq 433^{1} /{ }_{3} \mathrm{~K}, \Delta \phi_{1} \leq 0$ and $\psi=\gamma(2 \sigma / a \Delta f)$ and $\lambda=\gamma$. (b) Plots of average lamellar thickness (Å) vs temperature (K) for $\psi=0$, $1 / 4,1 / 3$, and $1 / 2$, each with $\hat{\psi}=\psi$, reproduced from the LauritzenHoffman Model. $^{1}$ Plots are independent of $\sigma_{\mathrm{e}}{ }^{\prime}$.

For comparison, we have reproduced part of Figure $3 b$ of ref 1 as our Figure $1 b$, which shows the LH model $l$ vs $T$ curves with $\hat{\psi}=\psi$ for the selected values of $\psi=0,1 / 4$, $1 / 3$, and $1 / 2$. Some of the data which we calculated in order to construct these plots are given in Table II. The LH model $\psi=0$ curve is identical to our $\gamma=0$ curve. For $\Delta f$ $\leq 2 \sigma / a$, each of the LH model " $\psi$ curves" is qualitatively similar but not quantitatively identical to its corresponding " $\gamma$ curve" presented in Figure 1a. Recall that the quantitative difference arises from the fact that the barrier $E_{2}$

**Table I**
Average Lamellar Thickness (Å) as a Function of
Temperature (K) for $\gamma = 0$ and for $\gamma = 1/2$, Each with $\sigma_{e}' = 0$
and $\theta = \gamma^{a}$

| temp (K) | $\psi = \gamma = 0$ | $\gamma = 1/2$ | temp (K) | $\psi = \gamma = 0$ | $\gamma = 1/2$ |
|----------|---------------------|----------------|----------|---------------------|----------------|
| 485.000  | 234.383             | 235.303        | 355.000  | 29.433              | 33.176         |
| 480.000  | 178.390             | 179.781        | 350.000  | 28.540              | 32.225         |
| 475.000  | 144.660             | 146.556        | 345.000  | 27.700              | 31.329         |
| 470.000  | 122.074             | 124.507        | 340.000  | 26.907              | 30.484         |
| 465.000  | 105.867             | 108.867        | 335.000  | 26.157              | 29.683         |
| 460.000  | 93.652              | 97.253         | 330.000  | 25.446              | 28.924         |
| 455.000  | 84.105              | 88.342         | 325.000  | 24.772              | 28.201         |
| 450.000  | 76.429              | 81.344         | 320.000  | 24.130              | 27.513         |
| 445.000  | 70.115              | 75.762         | 315.000  | 23.518              | 26.855         |
| 440.000  | 64.826              | 71.267         | 310.000  | 22.935              | 26.226         |
| 435.000  | 60.328              | 67.641         | 305.000  | 22.377              | 25.624         |
| 430.000  | 56.451              | 63.528         | 300.000  | 21.843              | 25.045         |
| 425.000  | 53.072              | 59.481         | 295.000  | 21.332              | 24.489         |
| 420.000  | 50.100              | 55.988         | 290.000  | 20.841              | 23.953         |
| 415.000  | 47.463              | 52.941         | 285.000  | 20.369              | 23.437         |
| 410.000  | 45.105              | 50.259         | 280.000  | 19.915              | 22.938         |
| 405.000  | 42.984              | 47.877         | 275.000  | 19.479              | 22.456         |
| 400.000  | 41.064              | 45.744         | 270.000  | 19.057              | 21.990         |
| 395.000  | 39.316              | 43.821         | 265.000  | 18.651              | 21.537         |
| 390.000  | 37.718              | 42.077         | 260.000  | 18.258              | 21.099         |
| 385.000  | 36.251              | 40.484         | 255.000  | 17.878              | 20.673         |
| 380.000  | 34.897              | 39.023         | 250.000  | 17.511              | 20.259         |
| 375.000  | 33.644              | 37.676         | 245.000  | 17.155              | 19.856         |
| 370.000  | 32.480              | 36.429         | 240.000  | 16.809              | 19.463         |
| 365.000  | 31.396              | 35.270         | 235.000  | 16.475              | 19.081         |
| 360.000  | 30.382              | 34.188         |          |                     |                |

$^{a}$ See Figure 1a. See section IX for $a, b, \sigma, \sigma_{e}, T_{m}{}^{\circ}$, and $\Delta h$, which
are the same for all of the tables.

has been constrained to be nonnegative; i.e., $E_{2} = (1 -$
$\theta)2ab\sigma_{e}$. For $\Delta f > 2\sigma/a$, however, the LH model $\psi$ curves
are in marked contrast to the $\gamma$ curves; in particular, for
each $\psi$ curve, $\bar{l}$ approaches infinity asymptotically as $\Delta f$
approaches $2\sigma/\psi a$. This is the behavior which is known
as the $\Delta l$ catastrophe.

One point is worth emphasizing here, namely, the
relationship between $\gamma$ and $\psi$. In both our model and the
LH model, $\psi \equiv l'/l$, but this ratio in the LH model is a
constant, whereas in our model

$$
\psi =
\begin{cases}
\gamma\left(\dfrac{2\sigma_{e}'}{l\Delta f} + \dfrac{2\sigma}{a\Delta f}\right) & \Delta\phi_{1} \leq 0 \\
\gamma & \Delta\phi_{1} \geq 0
\end{cases}
$$

For the case $\sigma_{e}' = 0$, this becomes

$$
\psi =
\begin{cases}
\gamma \dfrac{2\sigma}{a\Delta f} & \Delta f \geq 2\sigma/a \\
\gamma & \Delta f \leq 2\sigma/a
\end{cases}
$$

Now, for any given $\psi$, say $\psi_{j}$, $\bar{l}$ in the LH model is infinite
for all $\Delta f \geq 2\sigma/\psi_{j}a$; and for all $\Delta f \geq 2\sigma/\psi_{j}a$, there is no finite
value of $\bar{l}$ for any $\psi \geq \psi_{j}$. Equivalently, a value of $\psi \geq \psi_{j}$
is not possible for a chain-folded system for all $\Delta f \geq 2\sigma/$
$\psi_{j}a$; that is, high values of $\psi$ do not lead to chain-folded
polymer crystals at high enough supercooling according
to the LH model. Experiment, however, gives chain-folded
crystals at high supercooling with an average lamellar
thickness that decreases monotonically with decreasing
temperature. As we have seen, our one-parameter (i.e., $\gamma$)
model with $\sigma_{e}' = 0$ does reproduce this high-supercooling
behavior. Yet, high values of $\psi$, i.e., of the ratio $l'/l$, are
not associated with our high-supercooling, chain-folded
systems. To see this, first introduce the dimensionless
quantity $x$, where $0 < x < 1$. Then for any $\Delta f = 2\sigma/xa$,
$\psi = \gamma(2\sigma/a\Delta f) = \gamma x$. Since $\gamma$ cannot exceed $1, \psi$ in our
model cannot exceed $x_{j}$ for any $\Delta f \geq 2\sigma/x_{j}a$, where $x_{j}$ is
any given value of $x$. But this is exactly what was found
for $\psi$ in the LH model, i.e., that a value of $\psi$ greater than
or equal to $\psi_{j}$ is not possible for any $\Delta f \geq 2\sigma/\psi_{j}a$. Thus,
for $\Delta f > 2\sigma/a$, our model, through the imposition of the
constraint that barriers be nonnegative, places exactly the
same upper limit, $2\sigma/a\Delta f$, on our $\psi$ that is predicted for $\psi$
in the LH model. However, for $\Delta f > 2\sigma/a$, our model,
unlike the LH model, predicts $\bar{l}$ vs $T$ in qualitative
agreement with experiment.

**Table II**
Average Lamellar Thickness (Å) as a Function of
Temperature (K) for $\psi = 1/2$ with $\hat{\psi} = \psi$, Reproduced from
the Lauritzen-Hoffman (LH) Model $^{4,a}$

| temp (K) | LH $\psi = 1/2$ | temp (K) | LH $\psi = 1/2$ | temp (K) | LH $\psi = 1/2$ |
|----------|-----------------|----------|-----------------|----------|-----------------|
| 485.000  | 235.785         | 440.000  | 70.789          | 400.000  | 58.577          |
| 480.000  | 180.224         | 435.000  | 67.037          | 395.000  | 60.458          |
| 475.000  | 146.926         | 430.000  | 64.009          | 390.000  | 64.019          |
| 470.000  | 124.780         | 425.000  | 61.610          | 385.000  | 70.494          |
| 465.000  | 109.027         | 420.000  | 59.786          | 380.000  | 82.999          |
| 460.000  | 97.290          | 415.000  | 58.519          | 375.000  | 112.171         |
| 455.000  | 88.251          | 410.000  | 57.832          | 370.000  | 232.547         |
| 450.000  | 81.124          | 405.000  | 57.800          | 365.000  | $\infty$        |
| 445.000  | 75.412          |          |                 |          |                 |

$^{a}$ Data are independent of $\sigma_{e}'$. See Figure 1b.

Thus, the selected calculations done for our model
indicate that, for the case $\sigma_{e}' = 0$, our model does not
exhibit an infinite average lamellar thickness. Most
importantly, our model predicts $\bar{l}$ vs $T$ curves which are
monotonically decreasing with decreasing $T$ in agreement
with experiment. That is, we have successfully extended
the LH model to higher supercooling. Also, this success,
coupled with the numerical results shown in Figure 1a,
significantly increases our confidence in using $\gamma = 0$ as a
first approximation for mathematical convenience in
practice. $^{7}$ Finally, our results show that the $\Delta l$ catastrophe
of the LH theory is related to the failure to exclude negative
barriers and moreover that the LH approach to polymer
crystallization is in itself valid for high supercooling-given
that negative barriers are forbidden. Prior to this work,
the LH approach had always been described as one which
is invalid at high supercooling.

One set of results with $\theta \neq \gamma$ is presented in Table III.
Here we see that, for $\gamma = 1/2$ and $\theta = 1$, the calculated $\bar{l}(T)$
differ only slightly from the case with $\gamma = 1/2$ and $\theta = 1/2$.

Next, we investigated our model for $\sigma_{e}' \neq 0$. (Recall
that $\bar{l}$ for the LH model is independent of $\sigma_{e}'$ and that our
model is independent of $\sigma_{e}'$ for $\Delta f \leq 2\sigma/a$.) Using the
same values for $a, b, \sigma, \sigma_{e}, T_{m}{}^{\circ}$, and $\Delta h$ as above and again
with $\theta = \gamma$, $\bar{l}$ vs $T$ curves for $\sigma_{e}' = 0, 60, 100$, and 150
$\mathrm{erg/cm^{2}}$-each with $\gamma = 1/2$-are plotted together in Figure
2. Some of the $\sigma_{e}' \neq 0$ data used to construct these plots
are given in Table IV (and the $\sigma_{e}' = 0$ data has been seen
previously in Table I). From Figure 2, we see that $\bar{l}$
decreases monotonically with decreasing $T$ for $0 < \sigma_{e}' \leq$
$\sigma_{e}$ as well as for $\sigma_{e}' = 0$ and that $\bar{l}$ vs $T$ is relatively insensitive
to the value of $\sigma_{e}' \leq \sigma_{e}$. Thus our conclusions made
immediately above for the case $\sigma_{e}' = 0$ are valid when $0$
$\leq \sigma_{e}' \leq \sigma_{e}$. For $\sigma_{e}' = 150 \mathrm{erg/cm^{2}}$, there is a relative
minimum in $\bar{l}$ vs $T$ near $T = 405 \mathrm{K}$, and the curve passes
through a small and "diffuse" relative maximum at a lower
temperature. Recall that one expects $0 \leq \sigma_{e}' \leq \sigma_{e}$ so that,
with $\sigma_{e} = 100 \mathrm{erg/cm^{2}}, \sigma_{e}' = 150 \mathrm{erg/cm^{2}}$ may not be realistic

![](./images/812292486662717442_2.jpg)

Figure 2. Plots of average lamellar thickness (Å) vs temperature (K) for $\sigma_{\mathrm{e}}=0,60,100$, and $150 \mathrm{ergs} / \mathrm{cm}^{2}$, each with $\theta=\gamma=1 / 2$. Each open circle designates the point $\left(l_{0}, T_{0}\right)$ at which $\Delta \phi_{1}(l, T)$ $=0$. For $T \geq T_{0}, \Delta \phi_{1} \geq 0, \psi=\gamma$, and $\lambda=\gamma(a b l \Delta f /(2 a b \sigma_{\mathrm{e}}{ }^{\prime}+2 b l \sigma)$. For $T \leq T_{0}, \Delta \phi_{1} \leq 0, \psi=\gamma(2 \sigma_{\mathrm{e}}{ }^{\prime} / l \Delta f+2 \sigma / a \Delta f)$, and $\lambda=\gamma$.

<table>
<caption>Table III Average Lamellar Thickness (Å) as a Function of Temperature (K) for $\gamma=1 / 2, \theta=1$, and $\sigma_{\mathrm{e}}{ }^{\prime}=0$</caption>
<thead>
  <tr>
    <th>temp (K)</th>
    <th>$\theta=1$, $\gamma=1/2$</th>
    <th>temp (K)</th>
    <th>$\theta=1$, $\gamma=1/2$</th>
    <th>temp (K)</th>
    <th>$\theta=1$, $\gamma=1/2$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>495.000</td>
    <td>675.848</td>
    <td>405.000</td>
    <td>46.332</td>
    <td>315.000</td>
    <td>26.716</td>
  </tr>
  <tr>
    <td>490.000</td>
    <td></td>
    <td>400.000</td>
    <td></td>
    <td>310.000</td>
    <td></td>
  </tr>
  <tr>
    <td>485.000</td>
    <td>230.877</td>
    <td>395.000</td>
    <td>42.690</td>
    <td>305.000</td>
    <td>25.516</td>
  </tr>
  <tr>
    <td>480.000</td>
    <td></td>
    <td>390.000</td>
    <td></td>
    <td>300.000</td>
    <td></td>
  </tr>
  <tr>
    <td>475.000</td>
    <td>142.184</td>
    <td>385.000</td>
    <td>39.639</td>
    <td>295.000</td>
    <td>24.405</td>
  </tr>
  <tr>
    <td>470.000</td>
    <td></td>
    <td>380.000</td>
    <td></td>
    <td>290.000</td>
    <td></td>
  </tr>
  <tr>
    <td>465.000</td>
    <td>104.542</td>
    <td>375.000</td>
    <td>37.036</td>
    <td>285.000</td>
    <td>23.373</td>
  </tr>
  <tr>
    <td>460.000</td>
    <td></td>
    <td>370.000</td>
    <td></td>
    <td>280.000</td>
    <td></td>
  </tr>
  <tr>
    <td>455.000</td>
    <td>84.037</td>
    <td>365.000</td>
    <td>34.779</td>
    <td>275.000</td>
    <td>22.407</td>
  </tr>
  <tr>
    <td>450.000</td>
    <td></td>
    <td>360.000</td>
    <td></td>
    <td>270.000</td>
    <td></td>
  </tr>
  <tr>
    <td>445.000</td>
    <td>71.460</td>
    <td>355.000</td>
    <td>32.796</td>
    <td>265.000</td>
    <td>21.501</td>
  </tr>
  <tr>
    <td>440.000</td>
    <td></td>
    <td>350.000</td>
    <td></td>
    <td>260.000</td>
    <td></td>
  </tr>
  <tr>
    <td>435.000</td>
    <td>63.333</td>
    <td>345.000</td>
    <td>31.035</td>
    <td>255.000</td>
    <td>20.646</td>
  </tr>
  <tr>
    <td>430.000</td>
    <td></td>
    <td>340.000</td>
    <td></td>
    <td>250.000</td>
    <td></td>
  </tr>
  <tr>
    <td>425.000</td>
    <td>56.368</td>
    <td>335.000</td>
    <td>29.454</td>
    <td>245.000</td>
    <td>19.836</td>
  </tr>
  <tr>
    <td>420.000</td>
    <td></td>
    <td>330.000</td>
    <td></td>
    <td>240.000</td>
    <td></td>
  </tr>
  <tr>
    <td>415.000</td>
    <td>50.779</td>
    <td>325.000</td>
    <td>28.022</td>
    <td>235.000</td>
    <td>19.067</td>
  </tr>
  <tr>
    <td>410.000</td>
    <td></td>
    <td>320.000</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

but is examined in order to explore the model predictions as a function of $\sigma_{\mathrm{e}}{ }^{\prime}$.

The relationship between $\gamma$ and $\psi$ with $\sigma_{\mathrm{e}}{ }^{\prime} \neq 0$ is worth emphasizing at this point. In doing so, one difference between the cases $\sigma_{\mathrm{e}}{ }^{\prime}=0$ and $\sigma_{\mathrm{e}}{ }^{\prime} \neq 0$ will be found; namely, $\psi$ can exceed $\psi_{j}$ for some $\Delta f \geq 2 \sigma / \psi_{j} a$ when $\sigma_{\mathrm{e}}{ }^{\prime} \neq 0$. To reiterate, in both our model and the LH model, $\psi \equiv l^{\prime} / l$, but this ratio in the LH model is a constant, whereas in our model

$$
\psi(l, T)=
\begin{cases}
\gamma\left(\frac{2 \sigma_{\mathrm{e}}{ }^{\prime}}{l \Delta f}+\frac{2 \sigma}{a \Delta f}\right) & \Delta \phi_{1}(l, T) \leq 0 \\
\gamma & \Delta \phi_{1}(l, T) \geq 0
\end{cases}
$$

where the notations $\psi(l, T)$ and $\Delta \phi_{1}(l, T)$ emphasize here the dependence of $\psi$ and $\Delta \phi_{1}$ and $l$ and $T$. (The $T$ dependence, of course, enters through $\Delta f$.) Recalling the conditions which govern the sign of $\Delta \phi_{1}$ then gives, when $\sigma_{\mathrm{e}}>\sigma_{\mathrm{e}}{ }^{\prime}$

$$
\psi(l, T)=
\begin{cases}
\gamma\left(\frac{2 \sigma_{\mathrm{e}}{ }^{\prime}}{l \Delta f}+\frac{2 \sigma}{a \Delta f}\right) &
\begin{cases}
\text { for all } l \text { when } \Delta f>\frac{2 \sigma}{a}\left(\frac{\sigma_{\mathrm{e}}}{\sigma_{\mathrm{e}}-\sigma_{\mathrm{e}}{ }^{\prime}}\right) \\
\text { for } l \geq l_{0} \text { when } \frac{2 \sigma}{a}<\Delta f \leq \frac{2 \sigma}{a}\left(\frac{\sigma_{\mathrm{e}}}{\sigma_{\mathrm{e}}-\sigma_{\mathrm{e}}{ }^{\prime}}\right)
\end{cases} \\
\gamma &
\begin{cases}
\text { for } l \geq l_{0} \text { when } \frac{2 \sigma}{a}<\Delta f \leq \frac{2 \sigma}{a}\left(\frac{\sigma_{\mathrm{e}}}{\sigma_{\mathrm{e}}-\sigma_{\mathrm{e}}{ }^{\prime}}\right) \\
\text { for all } l \text { when } \Delta f \leq \frac{2 \sigma}{a}
\end{cases}
\end{cases}
$$

and when $\sigma_{\mathrm{e}} \leq \sigma_{\mathrm{e}}{ }^{\prime}$

$$
\psi(l, T)=
\begin{cases}
\gamma\left(\frac{2 \sigma_{\mathrm{e}}{ }^{\prime}}{l \Delta f}+\frac{2 \sigma}{a \Delta f}\right) & \text { for } l \geq l_{0} \text { when } \Delta f>2 \sigma / a \\
\gamma &
\begin{cases}
\text { for } l \leq l_{0} \text { when } \Delta f>2 \sigma / a \\
\text { for all } l \text { when } \Delta f \leq 2 \sigma / a
\end{cases}
\end{cases}
$$

where $l_{0}=(2 \sigma_{\mathrm{e}}{ }^{\prime} / \Delta f) /(1-2 \sigma / a \Delta f)$. Furthermore, on an $l$ vs $T$ curve, one has

$$
\psi(\bar{l}, T)=
\begin{cases}
\gamma\left(\frac{2 \sigma_{\mathrm{e}}{ }^{\prime}}{\bar{l} \Delta f}+\frac{2 \sigma}{a \Delta f}\right) & \Delta \phi_{1}(\bar{l}, T) \leq 0 \\
\gamma & \Delta \phi_{1}(\bar{l}, T) \geq 0
\end{cases}
$$

where the conditions which govern the sign of $\Delta \phi_{1}(\bar{l}, T)$ are those given above for $\Delta \phi_{1}(l, T)$ but with $l$ replaced by $\bar{l}$. Therefore, the temperature $T_{0}$ of a point $\left(l_{0}, T_{0}\right)$ on an $l$ vs $T$ curve and at which $\Delta \phi_{1}(\bar{l}, T)=\Delta \phi_{1}\left(l_{0}, T_{0}\right)=0$ is the solution to the following nonlinear algebraic equation in the one unknown $T$

$$
l^{(2)}(T)=l_{0}
$$

or

$$
\frac{\int_{l_{1}}^{l_{0}} l S_{\mathrm{I}} \mathrm{d} l+\int_{l_{0}}^{\infty} l S_{\mathrm{II}} \mathrm{d} l}{\int_{l_{1}}^{l_{0}} S_{\mathrm{I}} \mathrm{d} l+\int_{l_{0}}^{\infty} S_{\mathrm{II}} \mathrm{d} l}=\frac{2 \sigma_{\mathrm{e}}{ }^{\prime} / \Delta f}{1-2 \sigma / a \Delta f}
$$

If $\sigma_{\mathrm{e}}>\sigma_{\mathrm{e}}{ }^{\prime}, T_{0}$ will correspond to a value of $\Delta f$ in the range $2 \sigma / a<\Delta f \leq(2 \sigma / a)\left(\sigma_{\mathrm{e}} /\left(\sigma_{\mathrm{e}}-\sigma_{\mathrm{e}}{ }^{\prime}\right)\right)$, but if $\sigma_{\mathrm{e}} \leq \sigma_{\mathrm{e}}{ }^{\prime}, T_{0}$ will correspond to a value of $\Delta f$ in the range $\Delta f>2 \sigma / a$.

Rather than attempt to solve the above equation iteratively, one simply plots the left-hand side $l^{(2)}(T)$ vs $T$ and the right-hand side $l_{0}(T)$ vs $T$ on the same graph, and $T_{0}$ is given by a point of intersection of the two curves. Note that, as $\Delta f$ approaches $2 \sigma / a$ from values greater than $2 \sigma / a, l_{0}$ approaches infinity and that $l_{0}$ decreases monotonically with decreasing $T$ for $\Delta f>2 \sigma / a$. For each of the $l$ vs $T$ curves with $\sigma_{\mathrm{e}}{ }^{\prime} \neq 0$, we found one point of intersection $\left(l_{0}, T_{0}\right)$, which is designated on each curve by an open circle. We also found that $l^{(2)}(T)>l_{0}$ holds when $T<T_{0}$ and that $l^{(2)}(T)<l_{0}$ holds when $T>T_{0}$. Thus, $\Delta \phi(l, T)<$ 0 holds for $T<T_{0}$ and $\Delta \phi(l, T)>0$ holds for $T>T_{0}$. Our

<table>
<caption>Table IV Average Lamellar Thickness (Å) as a Function of Temperature (K) for $\sigma_e' = 60, 100$, and $150\ \text{ergs/cm}^2$, Each with $\theta = \gamma = ^{1}/_{2}$ (See Figure 2)</caption>
<thead>
<tr>
<th>temp (K)</th>
<th>$\sigma_e' = 60$</th>
<th>$\sigma_e' = 100$</th>
<th>$\sigma_e' = 150$</th>
</tr>
</thead>
<tbody>
<tr>
<td>485.000</td>
<td>235.303</td>
<td>235.303</td>
<td>235.303</td>
</tr>
<tr>
<td>480.000</td>
<td>179.781</td>
<td>179.781</td>
<td>179.781</td>
</tr>
<tr>
<td>475.000</td>
<td>146.556</td>
<td>146.556</td>
<td>146.556</td>
</tr>
<tr>
<td>470.000</td>
<td>124.507</td>
<td>124.507</td>
<td>124.507</td>
</tr>
<tr>
<td>465.000</td>
<td>108.867</td>
<td>108.867</td>
<td>108.867</td>
</tr>
<tr>
<td>460.000</td>
<td>97.253</td>
<td>97.253</td>
<td>97.253</td>
</tr>
<tr>
<td>455.000</td>
<td>88.342</td>
<td>88.342</td>
<td>88.342</td>
</tr>
<tr>
<td>450.000</td>
<td>81.344</td>
<td>81.344</td>
<td>81.344</td>
</tr>
<tr>
<td>445.000</td>
<td>75.762</td>
<td>75.762</td>
<td>75.762</td>
</tr>
<tr>
<td>440.000</td>
<td>71.267</td>
<td>71.267</td>
<td>71.267</td>
</tr>
<tr>
<td>435.000</td>
<td>67.641</td>
<td>67.641</td>
<td>67.641</td>
</tr>
<tr>
<td>430.000</td>
<td>64.735</td>
<td>64.735</td>
<td>64.735</td>
</tr>
<tr>
<td>425.000</td>
<td>62.454</td>
<td>62.454</td>
<td>62.454</td>
</tr>
<tr>
<td>420.000</td>
<td>60.723</td>
<td>60.743</td>
<td>60.743</td>
</tr>
<tr>
<td>415.000</td>
<td>59.214</td>
<td>59.577</td>
<td>59.584</td>
</tr>
<tr>
<td>410.000</td>
<td>57.306</td>
<td>58.874</td>
<td>59.005</td>
</tr>
<tr>
<td>405.000</td>
<td>54.856</td>
<td>58.337</td>
<td>58.984</td>
</tr>
<tr>
<td>400.000</td>
<td>52.149</td>
<td>57.582</td>
<td>59.533</td>
</tr>
<tr>
<td>395.000</td>
<td>49.469</td>
<td>56.411</td>
<td>60.296</td>
</tr>
<tr>
<td>390.000</td>
<td>46.971</td>
<td>54.852</td>
<td>60.919</td>
</tr>
<tr>
<td>385.000</td>
<td>44.708</td>
<td>53.035</td>
<td>61.120</td>
</tr>
<tr>
<td>380.000</td>
<td>42.683</td>
<td>51.095</td>
<td>60.800</td>
</tr>
<tr>
<td>375.000</td>
<td>40.874</td>
<td>49.136</td>
<td>60.003</td>
</tr>
<tr>
<td>370.000</td>
<td>39.252</td>
<td>47.220</td>
<td>58.842</td>
</tr>
<tr>
<td>365.000</td>
<td>37.791</td>
<td>45.385</td>
<td>57.434</td>
</tr>
<tr>
<td>360.000</td>
<td>36.466</td>
<td>43.648</td>
<td>55.882</td>
</tr>
<tr>
<td>355.000</td>
<td>35.253</td>
<td>42.015</td>
<td>54.261</td>
</tr>
<tr>
<td>350.000</td>
<td>34.136</td>
<td>40.486</td>
<td>52.625</td>
</tr>
<tr>
<td>345.000</td>
<td>33.100</td>
<td>39.056</td>
<td>51.009</td>
</tr>
<tr>
<td>340.000</td>
<td>32.131</td>
<td>37.719</td>
<td>49.436</td>
</tr>
<tr>
<td>335.000</td>
<td>31.219</td>
<td>36.468</td>
<td>47.918</td>
</tr>
<tr>
<td>330.000</td>
<td>30.358</td>
<td>35.295</td>
<td>46.462</td>
</tr>
<tr>
<td>325.000</td>
<td>29.541</td>
<td>34.194</td>
<td>45.072</td>
</tr>
<tr>
<td>320.000</td>
<td>28.766</td>
<td>33.159</td>
<td>43.746</td>
</tr>
<tr>
<td>315.000</td>
<td>28.028</td>
<td>32.183</td>
<td>42.485</td>
</tr>
<tr>
<td>310.000</td>
<td>27.324</td>
<td>31.262</td>
<td>41.286</td>
</tr>
<tr>
<td>305.000</td>
<td>26.652</td>
<td>30.390</td>
<td>40.145</td>
</tr>
<tr>
<td>300.000</td>
<td>26.009</td>
<td>29.564</td>
<td>39.059</td>
</tr>
<tr>
<td>295.000</td>
<td>25.392</td>
<td>28.778</td>
<td>38.025</td>
</tr>
<tr>
<td>290.000</td>
<td>24.799</td>
<td>28.031</td>
<td>37.040</td>
</tr>
<tr>
<td>285.000</td>
<td>24.229</td>
<td>27.318</td>
<td>36.101</td>
</tr>
<tr>
<td>280.000</td>
<td>23.681</td>
<td>26.637</td>
<td>35.204</td>
</tr>
<tr>
<td>275.000</td>
<td>23.152</td>
<td>25.985</td>
<td>34.346</td>
</tr>
<tr>
<td>270.000</td>
<td>22.641</td>
<td>25.360</td>
<td>33.526</td>
</tr>
<tr>
<td>265.000</td>
<td>22.147</td>
<td>24.760</td>
<td>32.740</td>
</tr>
<tr>
<td>260.000</td>
<td>21.669</td>
<td>24.184</td>
<td>31.986</td>
</tr>
<tr>
<td>255.000</td>
<td>21.206</td>
<td>23.628</td>
<td>31.263</td>
</tr>
<tr>
<td>250.000</td>
<td>20.756</td>
<td>23.093</td>
<td>30.567</td>
</tr>
<tr>
<td>245.000</td>
<td>20.320</td>
<td>22.576</td>
<td>29.898</td>
</tr>
<tr>
<td>240.000</td>
<td>19.896</td>
<td>22.076</td>
<td>29.253</td>
</tr>
<tr>
<td>235.000</td>
<td>19.484</td>
<td>21.593</td>
<td>28.631</td>
</tr>
</tbody>
</table>

final result is that, on an $\bar{l}$ vs $T$ curve

$$
\psi=
\begin{cases}
\gamma\left(\frac{2\sigma_{e}'}{\bar{l}\Delta f}+\frac{2\sigma}{a\Delta f}\right) & 0<T\leq T_{0} \\
\gamma & T_{0}\leq T<T_{m}{}^{\circ}
\end{cases}
$$

Note that if the dimensionless quantity $x$, $0<x<1$, is again introduced by writing $\Delta f=2\sigma/xa$, then $\psi=\gamma x((a\sigma_{e}'/\bar{l}\sigma)+1)$ so that, unlike the case $\sigma_{e}'=0$, $\psi$ can exceed $x_{j}$ for some $\Delta f\geq2\sigma/x_{j}a$, where $x_{j}$ is any given value of $x$.

Now, upon proceeding to consider results for $\gamma>^{1}/_{2}$, our basic conclusions—especially the fact that we have removed the $\Delta l$ catastrophe at high supercooling—remain intact; however, we do not obtain $\bar{l}$ vs $T$ curves which are monotonically decreasing for all $T$ when $\gamma$ is "sufficiently" large. Using the same values for $a$, $b$, $\sigma$, $\sigma_{e}$, $T_{m}{}^{\circ}$, and $\Delta h$ as previously and again with $\theta=\gamma$ and $\sigma_{e}'=0$, the calculated

![](./images/812292486662717442_3.jpg)

Figure 3. Plots of average lamellar thickness (Å) vs temperature (K) for $\gamma=^{1}/_{2},^{3}/_{4},0.90$, and 0.95, each with $\sigma_{e}'=0$ and $\theta=\gamma$. As in Figure 1a, $\Delta\phi_{1}=0$ at $T=433^{1}/_{3}$ K. (b) Plots of average lamellar thickness (Å) vs temperature (K) for $\psi=^{1}/_{2},^{3}/_{4},0.90$, and 0.95, each with $\hat{\psi}=\psi$, reproduced from the Lauritzen-Hoffman model.¹ Plots are independent of $\sigma_{e}'$.

$\bar{l}$ vs $T$ curves for the selected values of $\gamma=^{1}/_{2},^{3}/_{4},0.90$, and 0.95 are plotted in Figure 3a, and the curve for $\gamma=$ 0.99 appears in Figure 4. Some of the data used to construct these plots are given in Table V. The effect of $\gamma$ on $\bar{l}$ as a function of $T$ is readily apparent. First, the curve for $\gamma=^{1}/_{2}$ appears, on closer examination, to exhibit a discontinuity or break in its slope at the temperature $T^{*}$ $=433(1/3)$ K for which $\Delta f=2\sigma/a$. (This statement will be qualified later.) As for $\gamma=^{1}/_{2}$, $\bar{l}$ for $\gamma=^{3}/_{4},0.90,0.95$, and 0.99 does decrease with decreasing $T$ for all $T$ for which $\Delta f>2\sigma/a$, and there appears to be a break in the slope of $\bar{l}$ vs $T$ at $T=T^{*}$. Unlike for $\gamma=^{1}/_{2}$, the higher $\gamma$ curves pass through a relative minimum at a temperature for which $\Delta f<2\sigma/a$; the temperature $T_{*}$ at which this minimum occurs increases with $\gamma$ (for $\gamma=^{3}/_{4}$, it occurs between $T=440$ and $433^{1}/_{3}$ K and so can hardly be seen on the plot). Also, over the interval $T<T_{*}$, $\bar{l}$ vs $T$ is at

![](./images/812292486662717442_4.jpg)

Figure 4. Plots of average lamellar thickness (Å) vs temperature (K) for $\theta = \gamma = 0.99$ and $\sigma_{e}' = 0$. As in Figure 1a, $\Delta \phi_{1} = 0$ at $T = 433^{1}/_{3}$ K.

<table>
<caption>Table V<br>Average Lamellar Thickness (Å) as a Function of Temperature (K) for $\gamma = 0.90$ with $\sigma_{e}' = 0$ and $\theta = \gamma$ (See Figure 3a)</caption>
<thead>
<tr>
<th>temp (K)</th>
<th>$\gamma = 0.90$</th>
<th>temp (K)</th>
<th>$\gamma = 0.90$</th>
<th>temp (K)</th>
<th>$\gamma = 0.90$</th>
</tr>
</thead>
<tbody>
<tr>
<td>485.000</td>
<td>236.013</td>
<td>400.000</td>
<td>89.529</td>
<td>315.000</td>
<td>61.519</td>
</tr>
<tr>
<td>480.000</td>
<td>180.939</td>
<td>395.000</td>
<td>86.992</td>
<td>310.000</td>
<td>60.352</td>
</tr>
<tr>
<td>475.000</td>
<td>148.300</td>
<td>390.000</td>
<td>84.676</td>
<td>305.000</td>
<td>59.210</td>
</tr>
<tr>
<td>470.000</td>
<td>127.027</td>
<td>385.000</td>
<td>82.538</td>
<td>300.000</td>
<td>58.090</td>
</tr>
<tr>
<td>465.000</td>
<td>112.435</td>
<td>380.000</td>
<td>80.545</td>
<td>295.000</td>
<td>56.992</td>
</tr>
<tr>
<td>460.000</td>
<td>102.279</td>
<td>375.000</td>
<td>78.673</td>
<td>290.000</td>
<td>55.913</td>
</tr>
<tr>
<td>455.000</td>
<td>95.475</td>
<td>370.000</td>
<td>76.905</td>
<td>285.000</td>
<td>54.853</td>
</tr>
<tr>
<td>450.000</td>
<td>91.672</td>
<td>365.000</td>
<td>75.225</td>
<td>280.000</td>
<td>53.809</td>
</tr>
<tr>
<td>445.000</td>
<td>91.275</td>
<td>360.000</td>
<td>73.622</td>
<td>275.000</td>
<td>52.782</td>
</tr>
<tr>
<td>440.000</td>
<td>96.119</td>
<td>355.000</td>
<td>72.087</td>
<td>270.000</td>
<td>51.769</td>
</tr>
<tr>
<td>435.000</td>
<td>112.616</td>
<td>350.000</td>
<td>70.612</td>
<td>265.000</td>
<td>50.770</td>
</tr>
<tr>
<td>430.000</td>
<td>117.625</td>
<td>345.000</td>
<td>69.190</td>
<td>260.000</td>
<td>49.784</td>
</tr>
<tr>
<td>425.000</td>
<td>109.730</td>
<td>340.000</td>
<td>67.817</td>
<td>255.000</td>
<td>48.810</td>
</tr>
<tr>
<td>420.000</td>
<td>103.882</td>
<td>335.000</td>
<td>66.486</td>
<td>250.000</td>
<td>47.847</td>
</tr>
<tr>
<td>415.000</td>
<td>99.316</td>
<td>330.000</td>
<td>65.194</td>
<td>245.000</td>
<td>46.895</td>
</tr>
<tr>
<td>410.000</td>
<td>95.563</td>
<td>325.000</td>
<td>63.938</td>
<td>240.000</td>
<td>45.953</td>
</tr>
<tr>
<td>405.000</td>
<td>92.353</td>
<td>320.000</td>
<td>62.714</td>
<td>235.000</td>
<td>45.021</td>
</tr>
</tbody>
</table>

a relative maximum at $T = T^{*}$. Finally, note that $\bar{l}$ vs $T$ curves for $0.99 < \gamma < 1$ are qualitatively similar to the $\gamma = 0.99$ curve and do not exhibit an infinite average lamellar thickness. The numerical integrations in the expressions for $\bar{l}^{(1)}(T)$ and $\bar{l}^{(3)}(T)$ could not be done for $\gamma \equiv 1$ as a result of the factor $(1 - \gamma)$ appearing in various denominators.

For comparison, we have reproduced part of Figure 3b of ref 1 as our Figure 3b, which shows the LH model $\bar{l}$ vs $T$ curves with $\hat{\psi} = \psi$ for the selected values of $\psi = ^{1}/_{2}, ^{3}/_{4}, 0.90$, and 0.95. Some of the data which we calculated in order to construct these plots are given in Table VI. These LH model $\psi$ curves exhibit the $\Delta l$ catastrophe as $\Delta f$ approaches $2\sigma/\psi a$, as do all LH curves for $0.95 < \psi \leq 1$. The curves for $0.95 < \psi \leq 1$ are similar to the $\psi = 0.95$ curve; since integrations can be done analytically in the LH model when $\hat{\psi} = \psi$, $\bar{l}$ vs $T$ for $\psi \equiv 1$ was able to be obtained.¹

![](./images/812292486662717442_5.jpg)

Figure 5. Plots of average lamellar thickness (Å) vs temperature (K) for $\sigma_{e}' = 0, 60, 100$, and $150$ ergs/cm², each with $\theta = \gamma = ^{3}/_{4}$. As in Figure 2, each open circle identifies the temperature $T_{0}$ at which $\Delta \phi_{1}(\bar{l}, T) = 0$.

<table>
<caption>Table VI<br>Average Lamellar Thickness (Å) as a Function of Temperature (K) for $\psi = 0.90$ with $\hat{\psi} = \psi$, Reproduced from the Lauritzen-Hoffman (LH) Model¹⁴</caption>
<thead>
<tr>
<th>temp (K)</th>
<th>LH $\phi = 0.90$</th>
<th>temp (K)</th>
<th>LH $\phi = 0.90$</th>
<th>temp (K)</th>
<th>LH $\phi = 0.90$</th>
</tr>
</thead>
<tbody>
<tr>
<td>485.000</td>
<td>237.166</td>
<td>460.000</td>
<td>103.129</td>
<td>440.000</td>
<td>93.098</td>
</tr>
<tr>
<td>480.000</td>
<td>182.177</td>
<td>455.000</td>
<td>95.962</td>
<td>435.000</td>
<td>105.777</td>
</tr>
<tr>
<td>475.000</td>
<td>149.552</td>
<td>450.000</td>
<td>91.560</td>
<td>430.000</td>
<td>160.924</td>
</tr>
<tr>
<td>470.000</td>
<td>128.225</td>
<td>445.000</td>
<td>90.139</td>
<td>425.000</td>
<td>∞</td>
</tr>
<tr>
<td>465.000</td>
<td>113.507</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$^{a}$ Data are independent of $\sigma_{e}'$. See Figure 3b.

Thus, for high enough $\gamma$, our $\sigma_{e}' = 0$ model $\bar{l}$ vs $T$ curves appear to have a break in slope at $T = T^{*}$. We suspect that there is indeed a break in slope at $T = T^{*}$ because the relation

$$
\psi = 
\begin{cases}
\gamma \ \dfrac{2\sigma}{a\Delta f} & \Delta f \geq 2\sigma/a \\
\gamma & \Delta f \leq 2\sigma/a
\end{cases}
$$

implies that $\mathrm{d}\psi/\mathrm{d}T$ is discontinuous at $\Delta f = 2\sigma/a$; however, we have not evaluated $\mathrm{d}\bar{l}/\mathrm{d}T$ at $\Delta f = 2\sigma/a$. The break in slope is apparently indiscernible up to $\gamma$ values of about $^{1}/_{2}$, where the slope of $\bar{l}$ vs $T$ has the same sign (positive) regardless of whether the point $\Delta f = 2\sigma/a$ is approached from values of $\Delta f$ higher or lower than $2\sigma/a$. As $\gamma$ increases, however, the break becomes pronounced with the concomitant appearance of a relative maximum in $\bar{l}$ at $T = T^{*}$ and a relative minimum in $\bar{l}$ at $T = T_{*}$; necessarily then, the slope of $\bar{l}$ vs $T$ as $\Delta f$ approaches $2\sigma/a$ from values less than $2\sigma/a$ becomes negative. We will refer to this undesirable behavior, manifest at high values of $\gamma$, as the $\bar{l}$ anomaly. Unlike the $\Delta l$ catastrophe in the LH model, the relative maximum in $\bar{l}$ vs $T$, as noted above, always appears at $\Delta f = 2\sigma/a$ for all values of $\gamma$ given that $\sigma_{e}' = 0$.

Next, we consider $\sigma_{e}' \neq 0$ for high values of $\gamma$. The $\bar{l}$ vs $T$ curves for $\sigma_{e}' = 0, 60, 100$, and $150$ ergs/cm²—each with $\gamma = ^{3}/_{4}$—are presented in Figure 5. The curves pass through a common relative minimum between $T = 440$ and $433^{1}/_{3}$ K (for which $\Delta f < 2\sigma/a$), and then each curve rises and passes through a relative maximum, that

![](./images/812292486662717442_6.jpg)

Figure 6. Plots of average lamellar thickness (Å) vs temperature
(K) for $\sigma_{e}{}' = 0, 60, 100$, and $150\ \text{ergs/cm}^2$, each with $\theta = \gamma = 0.90$.
As in Figure 2, each open circle identifies the temperature $T_0$ at
which $\Delta \phi_1(\bar{l}, T) = 0$.

maximum being relatively higher and occurring at higher
$\Delta f$ the larger the value of $\sigma_{e}{}'$. At each maximum, there
would appear to be a break in the slope of $\bar{l}$ vs $T$. Having
passed through its maximum, each curve decreases mono-
tonically with decreasing $T$ thereafter.

One should be careful to note that what appears to be
a break in the slope of $\bar{l}$ vs $T$ when $\sigma_{e}{}' \neq 0$ is probably not
a break in slope; $d\bar{l}^{(2)}(T)/dT$ should be continuous for all
relevant $T$. Whether a break in the slope of $\bar{l}$ vs $T$ occurs
at $\Delta f = 2\sigma/a$ when $\sigma_{e}{}' \neq 0$ as was presumed true for $\sigma_{e}{}'$
$= 0$ cannot be determined conclusively from the appear-
ance of the graphs, although the break appears to be absent.

Qualitatively similar $\bar{l}$ vs $T$ curves are obtained for $\gamma =$
0.9 and $\sigma_{e}{}' = 0, 60, 100$, and $150\ \text{ergs/cm}^2$, as is shown in
Figure 6. See also Table VII. The relative maxima are
higher and "sharper" than the corresponding $\gamma = 3/4$ curves,
and they have moved to higher temperature. For $\gamma =$
0.99, the analogous curves, shown in Figure 7, exhibit $\bar{l}$
values which are unrealistically large as well as maxima
which are extremely "sharp".

Thus, from the graphs, we see that the $\bar{l}$ anomaly
becomes more pronounced but moves to higher temper-
ature as $\gamma$ increases for a fixed nonzero value of $\sigma_{e}{}'$. That
is, although the relative maximum in $\bar{l}$ vs $T$ can appear at
some $\Delta f > 2\sigma/a$ when $\sigma_{e}{}'$ is nonzero, the maximum becomes
less pronounced as it moves to lower temperature upon a
decrease in $\gamma$. Our model, then, does not fail at high
supercooling but does exhibit anomalous behavior for
temperatures corresponding to values of $\Delta f$ "just" greater
and "just" less than $2\sigma/a$. This undesirable behavior is
pronounced for large values of $\gamma$ and is more pronounced
for larger values of $\sigma_{e}{}'$ for a given $\gamma$.

We can easily rationalize mathematically how our
calculated $\bar{l}$ vs $T$ curves can rise with decreasing $T$ for
some $\Delta f > 2\sigma/a$ when $\sigma_{e}{}'$ is nonzero. Recall that the
expression for $\bar{l}^{(2)}(T)$, namely

$$
\bar{l}^{(2)}(T)=\frac{\int_{l_{1}}^{l_{0}} l S_{\mathrm{I}}(l, T) d l+\int_{l_{0}}^{\infty} l S_{\mathrm{II}}(l, T) d l}{\int_{l_{1}}^{l_{0}} S_{\mathrm{I}}(l, T) d l+\int_{l_{0}}^{\infty} S_{\mathrm{II}}(l, T) d l}
$$

contains two different integrands $S_{\mathrm{I}}(l, T)$ and $S_{\mathrm{II}}(l, T)$.
Depending on $\sigma_{e}{}', \gamma$, and $T$, the contribution of the integrals
involving $S_{\mathrm{I}}(l, T)$ to $\bar{l}^{(2)}(T)$ may outweigh the contribution
of the integrals involving $S_{\mathrm{II}}(l, T)$, and, in some cases, our
calculations show that to a very good approximation

$$
\bar{l}^{(2)}(T) \approx \frac{\int_{l_{1}}^{l_{0}} l S_{\mathrm{I}}(l, T) d l}{\int_{l_{1}}^{l_{0}} S_{\mathrm{I}}(l, T) d l} \quad \text{with } l_0 \text{ approaching infinity}
$$

But this is our expression for $\bar{l}^{(1)}(T)$ for the interval $\Delta f \leq$
$2\sigma/a$, and the results of our calculations using $\bar{l}^{(1)}(T)$ have
been found to differ little from results using $\bar{l}^{(\mathrm{LH})}(T)$, i.e.,
the LH theory. Not unexpectedly then, $\bar{l}^{(2)}(T)$ can increase
with decreasing $T$ for some $\Delta f > 2\sigma/a$. We note that the
numerator of $S_{\mathrm{I}}(l, T)$, like the numerator of $S^{(\mathrm{LH})}(l, T)$,
contains the factor $A_{0}=e^{-\sigma'} e^{-b l(2 \sigma-a \Delta f) / k T}$, the form of which
has been associated with$^{10}$ increases in $\bar{l}$ with decreasing
$T$.

<table>
<caption>Table VII<br>Average Lamellar Thickness (Å) as a Function of<br>Temperature (K) for $\sigma_{e}{}' = 60, 100$, and $150\ \text{ergs/cm}^2$, Each<br>with $\theta = \gamma = 0.90$ (See Figure 6)</caption>
<thead>
  <tr>
    <th>temp (K)</th>
    <th>$\sigma_{e}{}' = 60$</th>
    <th>$\sigma_{e}{}' = 100$</th>
    <th>$\sigma_{e}{}' = 150$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>485.000</td>
    <td>236.013</td>
    <td>236.013</td>
    <td>236.013</td>
  </tr>
  <tr>
    <td>480.000</td>
    <td>180.939</td>
    <td>180.939</td>
    <td>180.939</td>
  </tr>
  <tr>
    <td>475.000</td>
    <td>148.300</td>
    <td>148.300</td>
    <td>148.300</td>
  </tr>
  <tr>
    <td>470.000</td>
    <td>127.027</td>
    <td>127.027</td>
    <td>127.027</td>
  </tr>
  <tr>
    <td>465.000</td>
    <td>112.435</td>
    <td>112.435</td>
    <td>112.435</td>
  </tr>
  <tr>
    <td>460.000</td>
    <td>102.279</td>
    <td>102.279</td>
    <td>102.279</td>
  </tr>
  <tr>
    <td>455.000</td>
    <td>95.475</td>
    <td>95.475</td>
    <td>95.475</td>
  </tr>
  <tr>
    <td>450.000</td>
    <td>91.672</td>
    <td>91.672</td>
    <td>91.672</td>
  </tr>
  <tr>
    <td>445.000</td>
    <td>91.275</td>
    <td>91.275</td>
    <td>91.275</td>
  </tr>
  <tr>
    <td>440.000</td>
    <td>96.119</td>
    <td>96.119</td>
    <td>96.119</td>
  </tr>
  <tr>
    <td>435.000</td>
    <td>112.616</td>
    <td>112.616</td>
    <td>112.616</td>
  </tr>
  <tr>
    <td>430.000</td>
    <td>174.477</td>
    <td>176.464</td>
    <td>176.575</td>
  </tr>
  <tr>
    <td>425.000</td>
    <td>201.468</td>
    <td>297.598</td>
    <td>429.985</td>
  </tr>
  <tr>
    <td>420.000</td>
    <td>167.419</td>
    <td>248.786</td>
    <td>364.401</td>
  </tr>
  <tr>
    <td>415.000</td>
    <td>144.110</td>
    <td>205.816</td>
    <td>292.407</td>
  </tr>
  <tr>
    <td>410.000</td>
    <td>128.691</td>
    <td>177.388</td>
    <td>245.551</td>
  </tr>
  <tr>
    <td>405.000</td>
    <td>117.747</td>
    <td>157.689</td>
    <td>213.621</td>
  </tr>
  <tr>
    <td>400.000</td>
    <td>109.503</td>
    <td>143.241</td>
    <td>190.563</td>
  </tr>
  <tr>
    <td>395.000</td>
    <td>103.012</td>
    <td>132.137</td>
    <td>173.106</td>
  </tr>
  <tr>
    <td>390.000</td>
    <td>97.724</td>
    <td>123.283</td>
    <td>159.389</td>
  </tr>
  <tr>
    <td>385.000</td>
    <td>93.301</td>
    <td>116.014</td>
    <td>148.284</td>
  </tr>
  <tr>
    <td>380.000</td>
    <td>89.520</td>
    <td>109.905</td>
    <td>139.076</td>
  </tr>
  <tr>
    <td>375.000</td>
    <td>86.231</td>
    <td>104.670</td>
    <td>131.286</td>
  </tr>
  <tr>
    <td>370.000</td>
    <td>83.324</td>
    <td>100.111</td>
    <td>124.586</td>
  </tr>
  <tr>
    <td>365.000</td>
    <td>80.723</td>
    <td>96.086</td>
    <td>118.740</td>
  </tr>
  <tr>
    <td>360.000</td>
    <td>78.366</td>
    <td>92.490</td>
    <td>113.578</td>
  </tr>
  <tr>
    <td>355.000</td>
    <td>76.210</td>
    <td>89.245</td>
    <td>108.971</td>
  </tr>
  <tr>
    <td>350.000</td>
    <td>74.218</td>
    <td>86.289</td>
    <td>104.820</td>
  </tr>
  <tr>
    <td>345.000</td>
    <td>72.363</td>
    <td>83.577</td>
    <td>101.051</td>
  </tr>
  <tr>
    <td>340.000</td>
    <td>70.621</td>
    <td>81.071</td>
    <td>97.602</td>
  </tr>
  <tr>
    <td>335.000</td>
    <td>68.974</td>
    <td>78.739</td>
    <td>94.427</td>
  </tr>
  <tr>
    <td>330.000</td>
    <td>67.408</td>
    <td>76.559</td>
    <td>91.485</td>
  </tr>
  <tr>
    <td>325.000</td>
    <td>65.912</td>
    <td>74.510</td>
    <td>88.746</td>
  </tr>
  <tr>
    <td>320.000</td>
    <td>64.477</td>
    <td>72.574</td>
    <td>86.182</td>
  </tr>
  <tr>
    <td>315.000</td>
    <td>63.097</td>
    <td>70.740</td>
    <td>83.773</td>
  </tr>
  <tr>
    <td>310.000</td>
    <td>61.765</td>
    <td>68.993</td>
    <td>81.500</td>
  </tr>
  <tr>
    <td>305.000</td>
    <td>60.477</td>
    <td>67.325</td>
    <td>79.347</td>
  </tr>
  <tr>
    <td>300.000</td>
    <td>59.227</td>
    <td>65.728</td>
    <td>77.301</td>
  </tr>
  <tr>
    <td>295.000</td>
    <td>58.013</td>
    <td>64.193</td>
    <td>75.351</td>
  </tr>
  <tr>
    <td>290.000</td>
    <td>56.831</td>
    <td>62.714</td>
    <td>73.487</td>
  </tr>
  <tr>
    <td>285.000</td>
    <td>55.678</td>
    <td>61.287</td>
    <td>71.700</td>
  </tr>
  <tr>
    <td>280.000</td>
    <td>54.551</td>
    <td>59.905</td>
    <td>69.982</td>
  </tr>
  <tr>
    <td>275.000</td>
    <td>53.448</td>
    <td>58.566</td>
    <td>68.329</td>
  </tr>
  <tr>
    <td>270.000</td>
    <td>52.367</td>
    <td>57.264</td>
    <td>66.733</td>
  </tr>
  <tr>
    <td>265.000</td>
    <td>51.307</td>
    <td>55.998</td>
    <td>65.190</td>
  </tr>
  <tr>
    <td>260.000</td>
    <td>50.265</td>
    <td>54.763</td>
    <td>63.695</td>
  </tr>
  <tr>
    <td>255.000</td>
    <td>49.241</td>
    <td>53.558</td>
    <td>62.244</td>
  </tr>
  <tr>
    <td>250.000</td>
    <td>48.233</td>
    <td>52.380</td>
    <td>60.834</td>
  </tr>
  <tr>
    <td>245.000</td>
    <td>47.240</td>
    <td>51.226</td>
    <td>59.462</td>
  </tr>
  <tr>
    <td>240.000</td>
    <td>46.261</td>
    <td>50.096</td>
    <td>58.124</td>
  </tr>
  <tr>
    <td>235.000</td>
    <td>45.295</td>
    <td>48.987</td>
    <td>56.819</td>
  </tr>
</tbody>
</table>

## X. Conclusions
We have constructed a model of polymer crystallization
which extends the LH theory by excluding negative free

![](./images/812292486662717442_7.jpg)

Figure 7. Plots of average lamellar thickness (Å) vs temperature (K) for $\sigma_{e}{}' = 0, 60, 100$, and 150 ergs/cm², each with $\theta = \gamma = 0.99$. For $\sigma_{e}{}' = 0, 60, 100$, and 150 ergs/cm², $T_0 = 433^{1}/_{3}, 432.2, 432.1$, and 432.0 K, respectively. As in Figure 2, $T_0$ is the temperature at which $\Delta \phi_1(l,T) = 0$.

energy barriers, and we have shown that the $\Delta l$ catastrophe of the LH theory is related to the failure to exclude these negative barriers. Our results show that the new model is more consistent with experimental behavior at very high supercooling.

Our results with $\sigma_{e}{}' = 0$ clearly indicate that the $l$ anomaly in our model—and in part the $\Delta l$ catastrophe of the LH theory—are associated with the interval $\Delta f \leq 2\sigma/a$ and are thus connected to the expression $\Delta \phi_1 + E_1 = 2ab\sigma_{e}{}'$
$+ 2bl\sigma - \gamma abl\Delta f$. The $l$ anomaly also appears to be connected to this expression even when $\sigma_{e}{}' \neq 0$, i.e., even when the maximum in $l$ vs $T$ occurs at a temperature for which $\Delta f$ exceeds $2\sigma/a$. Although high values for $\gamma$ and $\psi$ are considered unrealistic as has been elucidated⁶ recently, however, there is no guarantee that the LH theory as well as our extension of it has not failed to incorporate an as yet unknown constraint or feature which would improve the model results at high $\gamma$ values. For example, high $\gamma$ values may be unrealistic, but the $l$ values for high $\gamma$ from an improved model may simply be unrealistically large but nevertheless monotonically decreasing with decreasing $T$ for all $T$.

In conclusion, we hope to extend our modification of the LH approach to polymer crystallization to treat the interesting systems which interact with an applied electric field.

## References and Notes
(1) Scheinbeim, J. I.; Newman, B. A.; Sen, A. *Macromolecules* **1986**, 19, 1454.
(2) Marand, H. L.; Stein, R. S.; Stack, G. M. *J. Polym. Sci., Polym. Phys. Ed.* **1988**, 26, 1361.
(3) Marand, H. L.; Stein, R. S. *J. Polym. Sci., Polym. Phys. Ed.* **1989**, 27, 1089.
(4) Lauritzen, J. I., Jr.; Hoffman, J. D. *J. Appl. Phys.* **1973**, 44, 4340.
(5) Hoffman, J. D.; Davis, G. T.; Lauritzen, J. I., Jr. In *Treatise on Solid State Chemistry*; Hannay, N. B., Ed.; Plenum Press: New York, 1976; Vol. 3, Chapter 7, pp 497−614.
(6) Sanchez, I. C.; Di Marzio, E. A. *J. Chem. Phys.* **1971**, 55, 893.
(7) Hoffman, J. D.; Miller, R. L. *Macromolecules* **1989**, 22, 3038.
(8) Frank, F. C.; Tosi, M. *Proc. R. Soc. London* **1961**, *A263*, 323.
(9) Turnbull, D.; Fisher, J. C. *J. Chem. Phys.* **1949**, 17, 71.
(10) *USER'S MANUAL-MATH/LIBRARY-FORTRAN Subroutines for Mathematical Applications*; IMSL, Inc.: Houston, TX, 1987; Chapter 4, pp 561−568.
(11) Hoffman, J. D.; Frolen, L. J.; Ross, G. S.; Lauritzen, J. I., Jr. *J. Res. Natl. Bur. Stand.* **1975**, *79A*, 671.
(12) Sanchez, I. C. *J. Macromol. Sci., Rev. Macromol. Chem.* **1974**, *C10*, 113−148.