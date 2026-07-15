# A simple methodology for analyzing association effects on response functions via Monte Carlo simulations

P. Gómez-Álvarez, A. Dopazo-Paz, L. Romaní, and D. González-Salgado⁽ᵃ⁾
Department of Applied Physics, University of Vigo, As Lagoas s/n, 32004 Ourense, Spain

(Received 22 July 2010; accepted 14 November 2010; published online 7 January 2011)

A simple methodology was developed to analyze association effects on the thermodynamic response functions for a pure self-associated fluid via Monte Carlo simulations. The procedure essentially involves expressing the residual energy and volume of the fluid in terms of these properties for two hypothetical fluids consisting of monomers and associated molecules, respectively. This allows the thermodynamic response functions to be expressed in a perturbative form as a combination of the values for the property in the monomeric fluid and the contribution of association (the perturbative term). The proposed methodology was used to determine both contributions to the isobaric heat capacity and to the temperature and pressure derivatives of the volume for OPLS methanol along the 50 MPa isobar from 220 to 1500 K. Based on the results, both terms exert a substantial influence on the isobaric heat capacity; by contrast, the association term for the volumetric properties is negligible. These results are consistent with those of a previous work involving simulations with the same model under identical thermodynamic conditions but a different approach. They are also compared with others previously reported in context. Moreover, a comprehensive study of the different types of clusters present in the fluid was performed and the results were related to thermodynamic properties. A strong correlation between the heat capacity of the monomeric fluid and this structural analysis was found. © 2011 American Institute of Physics. [doi:10.1063/1.3524201]

## I. INTRODUCTION
A considerable body of work exists on the physics of associated fluids, which are largely the result of their structural and thermodynamic singularities.¹⁻³⁴ Especially intriguing in this respect is the behavior of their thermodynamic response functions and, specifically, of their isobaric heat capacity. A literature scan for reported data of this type³⁵⁻³⁷ for alkanes, linear and branched alcohols, amines, and thiol series revealed that isobaric heat capacity versus temperature $C_{p}(T)$ curves can (i) be monotonically increasing; (ii) exhibit a shallow minimum; (iii) contain a convex to concave or (iv) concave to convex inflection point (as $T$ increases); or (v) exhibit a maximum. Although attempts at rationalizing these curves date from several decades ago, no unifying description based on association phenomena has to date been reported. In fact, it has been argued³⁸ that no general relationship can provide an accurate description for all types of experimental $C_{p}(T)$ curves. In recent years, a number of variably complex theoretical approaches³⁹⁻⁴⁵ have been used to gain insight into the potential relationship between association at the molecular level and the behavior of thermodynamic response functions, with special emphasis on the isobaric heat capacity.

The most comprehensive work in this field is the analysis by Cerdeiriña *et al.*³⁹,⁴⁰ based on a simple statistical mechanical model: the two-state association model (TSAM). The aim of this work was to provide a unifying description for the behavior of response functions in associated fluids, particularly as regards the above-described features of the isobaric heat capacity. According to the TSAM, each molecule can only be in one of two possible states: associated or dissociated. In the dissociated state, the energy, volume, and entropy per molecule are defined as those of a hypothetical fluid where all the molecules are dissociated, the opposite holding for the associated state. Thus, the energy and the volume of a pure self-associated liquid are calculated from the values for each state and the number of molecules each contains. Thermodynamic response functions are determined from these quantities and expressed as combination of a non-specific term (viz. the value of the property in the dissociated hypothetical fluid) and an association term. To this end, the difference in energy, volume, and entropy per molecule between both states are assumed to be constant, and also the isobaric heat capacity for the dissociated hypothetical fluid, consistent with the Flory theory⁴⁶ for van der Waals fluids. The model parameters are the enthalpy increment per molecule between the dissociated and associated states, the non-specific isobaric heat capacity and the ratio between the degeneracy corresponding to both states. These parameters are obtained by fitting the model to experimental heat capacity values. Application of such a simple model allowed them to accurately describe all types of experimental $C_{p}(T)$ curves; in fact, the shape of a $C_{p}(T)$ curve was found dependent mainly on the association term, which was the greater contributor to this property. On the other hand, the non-specific term was the dominant one for the temperature and pressure derivatives of the volume, $(\partial V/\partial T)_{p}$ and $(\partial V/\partial p)_{T}$, which were scarcely influenced by association. Moreover, the model parameters were very closely correlated with major molecular properties such as the association

⁽ᵃ⁾Author to whom correspondence should be addressed. Electronic mail: dgs@uvigo.es.


energy between molecules, association capability and molecular size. Thus, the molecular mechanisms governing the behavior of these fluids were identified.

Molecular equations of state based on the well-known statistical associating fluid theory (SAFT) have also been used to describe the response functions for associating systems. Worth special note in this respect is the work of Llovell et al. $^{42}$ and Laffitte et al., $^{41}$ who used the Soft-SAFT and SAFT-VR Mie equation of state, respectively. The SAFT theory splits the Helmholtz free energy into three contributions: monomer, chain and association. These two versions of the SAFT equation differ in the type of interactions they consider. Thus, whereas association is expressed via a square-well potential in both cases, dispersive interactions are defined via the Lennard-Jones potential in Soft-SAFT and the Mie potential in SAFT-VR. Both equations were found to accurately predict the experimental values of several response functions. In addition, the association effect on some of these properties was examined. Laffite et al. $^{41}$ found association to be the dominant contribution to the isochoric heat capacity in various linear and branched alcohols. Llovell et al. $^{42}$ obtained identical results for ethanol, but claimed that both chain and association contributions were important in 1-heptanol. Also, isothermal compressibility was scarcely influenced by association.

The increasing computation power made available to scientists has enabled the calculation of second-order thermodynamic derivatives by using molecular simulation, which was unaffordable for decades. To our knowledge, the most comprehensive work on molecular simulation data of response functions is that recently published by Lagache et al., $^{47}$ who calculated heat capacities, isobaric thermal expansivities, isothermal compressibilities and Joule-Thomson coefficients by using the fluctuation method. Molecular simulation techniques provide substantial advantages over theoretical approaches to the analysis of microscopic effects on thermodynamic properties since those don't need most of the approximations involved in theoretical studies. Specifically, molecular simulation allows molecules and their interactions to be characterized more realistically than with molecular theories; as a result, molecular simulation can provide more accurate results and enable studies of a high value. The most salient work on associating systems is that reported by Medeiros et al., $^{43-45}$ who demonstrated the usefulness of the fluctuation method for describing the molecular origin of the main features of the isobaric heat capacity $(C_{p})$, isobaric thermal expansivity $(\alpha_{p})$ and isothermal compressibility $(\kappa_{T})$ - particularly, $C_{p}(T)$ and $\alpha_{p}(T)$ maxima. To this end, they conducted extensive simulations on the 50 MPa isobar over the temperature range 300-800 K and used the fluctuation method to assess the response functions and identify their major contributors (viz. pairwise fluctuations corresponding to the Lennard-Jones energy, electrostatic energy, and volume). Although this method provides no direct information about association effects on response functions, the authors performed a qualitative analysis of the influence of the hydrogen bond on the different pairwise fluctuations and concluded that it was one of the greatest contributors to the heat capacity. This was not the case with $\alpha_{p}$ or $\kappa_{T}$, however, which testifies to the minor importance of association in volumetric properties.

In this work, we used a simple method to easily quantify association effects in a direct manner via Monte Carlo simulations. The main idea is to consider a pure associated fluid as constituted by two hypothetical fluids consisting of monomers and associated molecules, respectively. The properties for both hypothetical fluids are obtained from those of the monomers and associated molecules residing in the pure fluid, respectively. Thus, each property of the pure self-associated fluid, such as energy, volume, or enthalpy, can be expressed in a perturbative way as the sum of two contributions: the monomer and the association term. This decomposition also allows the thermodynamic response functions studied in this work, $C_{p},(\partial V / \partial T)_{p}$, and $(\partial V / \partial p)_{T}$, to be split in a similar way; so the analysis of the different terms is made easily. Extensive Monte Carlo simulations at temperatures from 220 to 1500 K along the supercritical 50 MPa isobar in the $NpT$ ensemble were performed for this purpose. Special routines were required to define when a molecule is associated and its volume. This was accomplished by using the geometric criterion $^{48}$ of H-bond formation and the Voronoi tessellation $^{49}$ for volume calculations. The results, obtained were compared with others previously reported. These routines additionally allowed us to conduct a deep structural analysis of the fluid by characterizing the different types of aggregates present in terms of the number of molecules and bonds. These results were correlated with the behavior of the response functions.

## II. METHODOLOGY
### A. Working equations
As described in the previous section, the pure associated fluid is assumed to be constituted by two hypothetical fluids $A$ and $B$ referring to monomers and associated molecules residing in the pure fluid, respectively. Thus, a configurational property in molar base $M$ of the pure fluid can be assessed from the value of the property in molar base of the two hypothetical fluids $M_{A}$ and $M_{B}$ as follows:
$$
M=x_{A} M_{A}+x_{B} M_{B}, \quad(1)
$$
where $x_{A}$ and $x_{B}$ are the mole fractions. Eq. (1) can be also written in the following perturbative form:
$$
M=M_{A}+M_{a s s}=M_{A}-x_{B} \Delta M, \quad(2)
$$
where the dissociation quantity $\Delta M$ is given by $M_{A}-M_{B}$. In this expression, $M_{A}$ is the reference term and $M_{a s s}=-x_{B} \Delta M$ represents the perturbation due to association. The derivative of $M$ with respect to a parameter $Y$ at a constant $Y^{\prime}$ is
$$
\begin{aligned}
\left(\frac{\partial M}{\partial Y}\right)_{Y^{\prime}} & =\left(\frac{\partial M_{A}}{\partial Y}\right)_{Y^{\prime}}+\left(\frac{\partial M_{a s s}}{\partial Y}\right)_{Y^{\prime}} \\
& =\left(\frac{\partial M_{A}}{\partial Y}\right)_{Y^{\prime}}-\left(\frac{\partial x_{B}}{\partial Y}\right)_{Y^{\prime}} \Delta M-x_{B}\left(\frac{\partial \Delta M}{\partial Y}\right)_{Y^{\prime}}. \quad(3)
\end{aligned}
$$

The first term on the right-hand side of the second equality represents the contribution of the monomer fluid and the last two terms are due to association. As it can be seen, the latter two arise from the variation with $Y$ of both the association mole fraction and the difference in the magnitude between the two fluids (i.e., from molecular jumps between the two fluids and changes in the dissociation property).

Letting $M$ be enthalpy ($H$) or volume ($V$) and $Y$ (or $Y'$) temperature ($T$) or pressure ($p$) allows one to write the following equations:

$$
\begin{aligned}
\left(\frac{\partial H}{\partial T}\right)_{p} &= \left(\frac{\partial H_{A}}{\partial T}\right)_{p} + \left(\frac{\partial H_{ass}}{\partial T}\right)_{p} \\
&= \left(\frac{\partial H_{A}}{\partial T}\right)_{p} - \left(\frac{\partial x_{B}}{\partial T}\right)_{p} \Delta H - x_{B} \left(\frac{\partial \Delta H}{\partial T}\right)_{p}, \quad (4)
\end{aligned}
$$

$$
\begin{aligned}
\left(\frac{\partial V}{\partial T}\right)_{p} &= \left(\frac{\partial V_{A}}{\partial T}\right)_{p} + \left(\frac{\partial V_{ass}}{\partial T}\right)_{p} \\
&= \left(\frac{\partial V_{A}}{\partial T}\right)_{p} - \left(\frac{\partial x_{B}}{\partial T}\right)_{p} \Delta V - x_{B} \left(\frac{\partial \Delta V}{\partial T}\right)_{p}, \quad (5)
\end{aligned}
$$

$$
\begin{aligned}
- \left(\frac{\partial V}{\partial p}\right)_{T} &= - \left(\frac{\partial V_{A}}{\partial p}\right)_{T} - \left(\frac{\partial V_{ass}}{\partial p}\right)_{T} \\
&= - \left(\frac{\partial V_{A}}{\partial p}\right)_{T} + \left(\frac{\partial x_{B}}{\partial p}\right)_{T} \Delta V + x_{B} \left(\frac{\partial \Delta V}{\partial p}\right)_{T}. \quad (6)
\end{aligned}
$$

Splitting the enthalpy of the monomer fluid $(H_A)$ into a combination of the ideal gas enthalpy $(H_A^{id})$ and the residual enthalpy $(H_A^r)$ allows Eq. (4) to be rewritten in a more functional way:

$$
\begin{aligned}
\left(\frac{\partial H^{r}}{\partial T}\right)_{p} &= \left(\frac{\partial H_{A}^{r}}{\partial T}\right)_{p} + \left(\frac{\partial H_{ass}^{r}}{\partial T}\right)_{p} \\
&= \left(\frac{\partial H_{A}^{r}}{\partial T}\right)_{p} - \left(\frac{\partial x_{B}}{\partial T}\right)_{p} \Delta H - x_{B} \left(\frac{\partial \Delta H}{\partial T}\right)_{p} \quad (7)
\end{aligned}
$$

with
$$
\left(\frac{\partial H_{A}^{r}}{\partial T}\right)_{p} = \left(\frac{\partial U_{A}^{r}}{\partial T}\right)_{p} + p \left(\frac{\partial V_{A}}{\partial T}\right)_{p} - R, \quad (8)
$$
where $R$ is the universal gas constant. The three first terms in Eq. (7) shall henceforth be denoted by $C_p^r$, $C_{p,A}^r$, and $C_{p,ass}^r$, respectively, and the last two by $C_{p,ass,1}^r$ and $C_{p,ass,2}^r$, respectively. Eqs. (5)-(8) were used to explore the response functions.

## B. Simulation details

We used the optimized potential for liquid simulations (OPLS) (Ref. 50) to describe methanol molecules. The model is based on the rigid molecule approximation and quantifies intermolecular interactions as the combination of Lennard-Jones and Coulombic interactions between sites. In this model, these ones are located in the methyl group ($\text{CH}_3$) and in the oxygen (O) and in the hydrogen (H) of the hydroxyl group. Two Lennard-Jones centers are assumed to be at the O and $\text{CH}_3$ sites, respectively, and charges are placed in all of them.

Molecular $NpT$ Monte Carlo simulations of OPLS methanol were performed from 220 to 1500 K at 50 MPa in a cubic box under periodic boundary conditions and the minimum image convention. $^{51,52}$ The number of molecules $N$ was set to 256 since it allows simulations to be time-saving and the finite size effects in the response functions to be reduced to an extent similar to the precision of our simulations. A cut-off radius equal to half the cubic side was used for both types of interactions. Usual long-range corrections $^{51,52}$ were used for Lennard-Jones interactions and the reaction field method $^{53-55}$ with conducting boundary conditions (as is usual in moderately and high polar fluids $^{56}$ as methanol) was applied to the electrostatic interactions. It was chosen instead of the also valid Ewald summation method $^{52}$ in order to improve the speed of the runs. Simulations were arranged in cycles of $N$ moves including translation moves, rotation moves and volume changes. The probability of a volume change was set to $1/N$, and that for translation and rotation moves at $(N-1)/(2N)$. The acceptance ratio used was 0.33. The equilibration period was about 750 000 cycles and the production run 7 500 000 cycles. One configuration each five cycles was used to compute averages. A specific routine allowing molecules in the bulk fluid to be classified as monomers or associated was implemented in standard MC code in order to characterize the above-mentioned hypothetical fluids. In addition, the energy and volume for each molecule were calculated; the former was obtained from typical Monte Carlo code, but the volume required using a customized routine. The procedure is described in detail below.

The choice of a specific criterion to decide whether a H-bond is established is somewhat arbitrary. The usual H-bond definitions are based on energetic or geometric criteria. $^{48}$ With alcohols, however, the choice is less crucial than with water since energetic and geometric criteria lead to similar results. $^{57,58}$ We adopted the geometric definition, i.e., a hydrogen bond between two methanol molecules exists if the following conditions are verified: (1) $R_{OO} \leq R_{OO}^T$ (i.e., the distance between the oxygen atoms, $R_{OO}$, is smaller than a threshold value $R_{OO}^T=3.5$ Å); (2) $R_{HO} \leq R_{HO}^T$ (i.e., the distance between the "acceptor" oxygen and the hydrogen corresponding to the molecule of the "donor" oxygen, $R_{HO}$, is smaller than a threshold value $R_{HO}^T=2.6$ Å); and (3) $\phi \leq \phi^T$ (i.e., the $\text{H-O}\cdots\text{O}$ angle, $\phi$, is smaller than a threshold value $\phi^T=30^\circ$). Although the proposed methodology only requires classifying methanol molecules as dissociated or associated, we implemented a specific algorithm capable of evaluating the different types of aggregates present as a function of their size $s$ (number of molecules) and the number of bonds $b$ in order to obtain a more comprehensive structural description.

The volume of a molecule in a given configuration was defined as the volume of the Voronoi polyhedra (VP) associated to the molecule. $^{59}$ By definition, the Voronoi polyhedron of a molecule is the (convex) region of space in which every point is closer to the molecule concerned than to any other one. One immediate inference from this definition is that the VP of a system constitutes a space-filling tessellation which splits the space unequivocally into regions allocated to specific molecules. There was no need to obtain the true VP in order to fulfil our aim: to estimate the volume corresponding to

each particle. In fact, it sufficed to use a grid approximation⁴⁹ involving the following steps: (1) the system was split into boxes with the aid of a grid; (2) each box was assigned to its closest particle; and (3) the set of boxes ascribed to one particle was assumed to approximate its VP. The most obvious — and inefficient — way of performing step three is computing the distance from each box to every particle. Instead, each particle “conquers” the boxes around its previously occupied boxes, beginning with that containing the particle in question. Only when a box is disputed between two particles, it is necessary to evaluate the distances and assign the box to the closest particle. The VP approximation is finished when no free boxes remained.

This methodology allowed us to calculate all average properties required for our study. The properties included the average fraction of molecules belonging to an aggregate of size $s$ and number of bonds $b$, which was denoted by $x(s, b)$; the average residual energy and volume for the monomers $\{U_{mon}^r, V_{mon}\}$, for the molecules belonging to a certain aggregate $\{U_{agg}^r, V_{agg}\}$, and for the total system $\{U_T^r, V_T\}$. Obviously, $U_T^r = U_{mon}^r + U_{agg}^r$ and $V_T = V_{mon} + V_{agg}$. The residual energy and volume in molar base for a given configuration, $\{U^r, V\}$, and the residual energies and volumes in molar base for the hypothetical fluids, $\{U_A^r, V_A\}$ and $\{U_B^r, V_B\}$, were calculated from

$$
U^{r}=\frac{U_{T}^{r}}{N} \cdot N_{a v}, \quad V=\frac{V_{T}}{N} \cdot N_{a v}, \tag{9}
$$

$$
U_{A}^{r}=\frac{U_{m o n}^{r}}{N \cdot x_{A}} \cdot N_{a v}, \quad V_{A}=\frac{V_{m o n}}{N \cdot x_{A}} \cdot N_{a v}, \tag{10}
$$

$$
U_{B}^{r}=\frac{U_{a g g}^{r}}{N \cdot x_{B}} \cdot N_{a v}, \quad V_{B}=\frac{V_{a g g}}{N \cdot x_{B}} \cdot N_{a v}, \tag{11}
$$

where $N_{\text{av}}$ is the Avogadro number, $x_A = x(1,0)$ and $x_B = 1 - x_A$. These properties allowed the residual enthalpies $(H^r, H_A^r$ and $H_B^r)$, and the dissociation volume $(\Delta V)$, energy $(\Delta U)$ and enthalpy $(\Delta H)$, to be estimated. The last two were directly obtained from the residual quantities since they are unaffected by the ideal contribution.

The temperature and pressure derivatives in Eqs. (5)–(8) were calculated as follows. The first step involved determining the derivatives of the magnitudes evaluated as averages (i.e., $U_T^r, V_T, U_{mon}^r, V_{mon}, U_{agg}^r, V_{agg}, x_A$, and $x_B$) by using the fluctuation method.⁴⁵,⁴⁷ Secondly, the derivatives of $U^r$ and $V$(and so $H^r$) were determined immediately from those of $U_T^r$ and $V_T$ whereas the derivatives of $U_A^r, U_B^r, V_A$ and $V_B$ were calculated by using the expression of the derivative of a quotient according to Eqs. (10)–(11). For instance, the temperature derivative of the energy of the monomeric fluid at constant $p$ was obtained as follows:

$$
\left(\frac{\partial U_{A}^{r}}{\partial T}\right)_{p}=\frac{\left(\partial U_{m o n}^{r} / \partial T\right)_{p} \cdot x_{A}-U_{m o n}^{r} \cdot\left(\partial x_{A} / \partial T\right)_{p}}{x_{A}^{2}} \cdot \frac{N_{a v}}{N}. \tag{12}
$$

Finally, the derivatives of the rest of magnitudes $H_A^r, H_B^r$, $\Delta U$, $\Delta V$, and $\Delta H$ were easily obtained from the previous quantities.

## III. RESULTS AND DISCUSSION
### A. Structure
As stated in the previous section, aggregates were classified into groups in terms of size $(s)$ and number of bonds $(b)$. A second classifying procedure was also used to simplify the presentation that involved establishing sets labeled as type 1, type 0, type –1, type –2… corresponding to aggregates with $s - b = 1, 0, -1, -2 \dots$. Thus, linear chains belong to type 1 and cyclic chains to type 0. These aggregates are not the only elements of the type 1 and type 0 sets; for instance, branched structures are included in either. This is a result of the ability of a methanol molecule to form more than two bonds, which is also the origin of the formation of aggregates of type –1, type –2, etc., which are unlikely but not impossible.

Figure 1 shows the variation of the average number of aggregates of size $s$ and number of bonds $b$, $n(s, b) = N \cdot x(s, b)$, with $s$ at selected temperatures from 220 to 600 K. The different “curves” corresponding to type 1, type 0, type –1 and type –2 aggregates are identified with a specific symbol and also a special one is used for monomers to facilitate distinction. As it can be seen, type 0 aggregates are the most likely throughout the size range at the lowest temperature (220 K), where they exhibit a roughly constant value of $n(s, b)$—with provision for uncertainty in our simulations—by exception, $n(s, b)$ is significantly greater at $s = 256$, i.e., the most likely aggregate is a non linear one encompassing all molecules. The second most likely type of aggregate is type 1; by contrast, type –1 aggregates have a minor contribution and type –2 aggregates are virtually absent. The dependence of $n(s, b)$ on $s$ for type 1 aggregates is virtually invariable except at low $s$ values, where it exhibits a maximum at around $s = 15$. As regards monomers, its average number is smaller than the usual values for type 1 and type 0 aggregates.

Raising the temperature causes in significant changes. Thus, the relative significance of type 1 and type 0 aggregates changes gradually: at 240 K, type 1 aggregates prevail at low $s$ values and type 0 aggregates do at high $s$ values; above 260 K, however, type 1 aggregates dominate throughout the size range. Besides, the above-mentioned peak in the “curve” increases with increasing temperature, its position changing from $s = 15$ at 220 K to $s = 6$ between 260 and 300 K. At higher temperatures, the maximum in the curve disappears and $n(s, b)$ decreases with increasing $s$. The type 0 set exhibits a constant $s$ value at 220 K, a near-linear decline from 260 to 300 K, and virtually negligible values above 400 K. Moreover, the “curves” for this aggregate type exhibit two singularities, namely: (1) the probability for the aggregate formed by all molecules ($s = 256$) decreases abruptly with increase in $T$ since this was the dominant type at 220 K but present in virtually negligible proportions above 250 K; and (2) type 0 aggregates of sizes $s = 2$–6 depart from the previous trend between 250 and 300 K [$n(s, b)$ rises from zero at $s = 2$–3 to a maximum at $s = 5$ and then decreases in the above-described linear manner as it is apparent from the inset figures]. Type –1 aggregates lose significance as the temperature is raised. Regarding monomers, $n(1, 0)$ increases significantly with increasing $T$ and monomers are the most likely above 400 K.

![](./images/811688000164462596_1.jpg)

FIG. 1. Average number of molecules $n(s, b)$ in aggregates of size $s$ and number of bonds $b$ as a function of $s$ at selected temperatures. type $1(+)$, type $0(\diamond)$, type-$1(\bigcirc)$, type-$2\ (\triangle)$, and monomers (■). Inset figures are included from 250 to 300 K in order to appreciate clearly the behavior of type 0 aggregates at low sizes.

![](./images/811688000164462596_2.jpg)

FIG. 2. (a) Average number $n$ of molecules belonging to aggregates type $I(+)$, type $0$ $(\diamond)$, type-$I(\bigcirc)$, and type-$2$ $(\Delta)$ as a function of $T$. (b) Mole fractions of monomers $x_A$ ($\blacksquare$) and of associated molecules $x_B$ ($\square$) plotted against $T$.

The results warrant some additional comment. Thus, vir- tually all molecules are in an associated state from 220 K to 300 K; in fact, the average number of monomers at 300 K is about 3.5 out of 256. The major phenomenon in this temper- ature range is the change in significance in the different types of aggregates—the formation of monomers is insubstantial. The situation changes markedly at higher temperatures, how- ever. Thus, above 400 K, the destruction of aggregates to form monomers is significant and their mole fraction rises to about 0.5 at 600 K and 0.9 at 800 K. These facts, i.e., the relative significance between the different types of aggregates, and be- tween dissociated and associated molecules are quite apparent from Figs. 2(a) and 2(b), respectively.

### B. Thermodynamics

Figure 3 shows the variation of $U_A^r$, $U_B^r$, $V_A$, $V_B$, $H_A^r$, $H_B^r$, and their differences ($\Delta U$, $\Delta V$ and $\Delta H$, respectively), as a function of temperature $(T)$. As it can be seen, the resid- ual energies $U_A^r$ and $U_B^r$ increases with increasing tempera- ture and $U_A^r$ takes higher values. This result can be explained as follows: at the lowest temperatures studied, methanol is in a very condensed state where most of its molecules form two hydrogen bonds (one per molecule). The energy of an associated molecule under such conditions is the combina- tion of two factors, namely: the energy of one hydrogen bond and that due to interactions of the molecule in question with others not bonded to it. These quantities were computed during simulations and they both take similar values about $-20$ kJ·mol⁻¹. Obviously, the energy of the monomers can only come from the latter term and is very similar to that for associated molecules, as it is apparent from the figure. As a result, the difference between both energies, $\Delta U$, is roughly the same as the energy of a hydrogen bond under these con- ditions. The effect of temperature on $U_A^r$ and $U_B^r$ is as fol- lows: raising the temperature causes the distances between molecules to increase, thereby also increasing the energy be- tween molecules, i.e., it is made less negative. At very high temperatures, the distance between those molecules not di- rectly bonded is obviously so large that the energy is near- zero. Since this is the only contribution of monomers to the energy, $U_A^r$ exhibits that behavior. On the other hand, $U_B^r$ is determined from this contribution to energy but also from the energy between directly bonded molecules, whose behavior with $T$ is the result of two factors, namely: the number of bonds per molecule tending to $1/2$ by effect of dimerization and the increase in H-bond distance, which makes the energy increase to a limiting value around $-15$ kJ·mol⁻¹ under the geometric criterion used in this work. These facts allow the curve of $U_B^r$ (which tends to about $-7.5$ kJ·mol⁻¹ at high tem- peratures) to be easily interpreted.

As regards $V_A$ and $V_B$, they increase with increasing tem- perature as a consequence of the general increase in system volume; however, the slope of the two “curves” does not coin- cide throughout the temperature range. As per the Voronoi cri- terion, the molecular volume is the space around a molecule where all points are at a closer distance from such a molecule than from any other. Whereas monomers have free space all around, associated molecules can only have it in those spa- tial directions where no hydrogen bond is present. As a re- sult, the volume of the hypothetical fluid of monomers $(V_A)$ is greater than that of associated molecules $(V_B)$; the difference $\Delta V$ between the two comes directly from space forbidden to the associated molecules owing to the presence of hydrogen bonds. The variation of $V_A$, $V_B$ and $\Delta V$ with temperature can be explained in the light of the previous arguments. Thus, at the lowest temperatures studied, methanol is in a highly condensed state with little free space around each molecule. As a result, the average distance between a monomer and its neighbours is essentially similar to the length of a hydrogen bond. For this reason, $V_A$ and $V_B$ take very low, similar val- ues. Raising the temperature increases the system volume, thereby also increasing the free volume for both monomers and associated molecules, as well as their forbidden space. Finally, the enthalpy is related to both energy and vol- ume through the well-known thermodynamic equation; there- fore, its curve shape is consistent with the above-described contributions.

![](./images/811688000164462596_3.jpg)

FIG. 3. (a) Residual energy, volume and residual enthalpy of the monomeric fluid, $U_A^r$, $V_A$, $H_A^r$ (■), and of the fluid of associated molecules, $U_B^r$, $V_B$, $H_B^r$ (□), and the dissociation magnitudes $\Delta U$, $\Delta V$, $\Delta H$ (●) as a function of $T$.

The variation of the response functions and their corresponding contributions with temperature is examined next. The residual isobaric heat capacity $(C_p^r)$ and its respective terms [Eqs. (7)–(8)] are shown in Fig. 4(a). The uncertainty in these magnitudes was estimated to vary from 0.3% at high temperatures to around 3% at lower levels. As it can be seen, the curves for the total quantity and its association contribution are identically shaped; both increase with increasing temperature up to a certain level above which they decrease and approach zero at high temperatures. The curve for the residual heat capacity of the dissociated hypothetical fluid $(C_{p,A}^r)$ is similarly shaped except at low temperatures, where it also exhibits a minimum. As it can be seen, both terms influence the shape of the total residual heat capacity. The association term $(C_{p,ass}^r)$ is more significant at low temperatures and the monomer contribution at higher levels. Interestingly, the position of the maximum differs in the three curves; thus, the maximum of the total residual heat capacity falls in between those for the other two quantities. Therefore, the position of the maximum is affected by both contributions.

The residual heat capacity of the hypothetical fluid of monomers is significantly correlated with the above-described

![](./images/811688000164462596_4.jpg)

FIG. 4. (a) Residual heat capacity $C_p^r$ (○) and its monomer and association contributions, $C_{p,A}^r$ (■) and $C_{p,ass}^r$ (×) as a function of $T$. (b) Residual association heat capacity $C_{p,ass}^r$ (×) and its both terms $C_{p,ass,1}^r$ (♦) and $C_{p,ass,2}^r$ (◇) plotted against $T$.

structural features. The underlying structural fact that occurs while $C_{p,A}^r$ decreases from 220 to 300 K is the change in relative significance between the different types of aggregates and the absence of monomer formation to an appreciable extent. From 300 to 600 K, the increase in $C_{p,A}^r$ coincides with the fast formation of monomers, which, once monomers become the dominant form (above 600 K), is slower and accompanied by a decrease in $C_{p,A}^r$ as a result.

The association term can be split into the two contributions of Eq. (7), namely: $C_{p,ass,1}^r$, which arises from the variation of the mole fraction with temperature (i.e., from molecules jumping between the monomer and associated states), and $C_{p,ass,2}^r$, which is due to the change in $\Delta H$ with temperature and related to the change in H-bond energy through it. Figure 4(b) shows the temperature-dependence of the association heat capacity and the previous two contributions. These quantities were only plotted above 300 K since available data below this level were not accurate enough. As it can be seen, both terms contribute to the total quantity. At low temperatures, the association heat capacity is due mainly to the variation of the mole fraction with the other term prevailing at high temperatures. Figure 5 illustrates the effect of association on the temperature derivative minus the pressure derivative of the volume. The uncertainties in relative terms are similar to the values given for heat capacities. As it can be seen, both properties are dominated by the monomer term, and hence insensitive to association phenomena.

As noted in the Introduction, a number of methods including TSAM, SAFT and molecular simulation have been used to estimate the contribution of association to various thermodynamic response functions. A brief discussion of their results in relation to ours follows.

The theoretical structure of TSAM (Refs. 39 and 40) coincides with that used in this work. Thus, it splits second-order thermodynamic derivatives into two contributions due to the dissociated hypothetical fluid (the non-specific term) and association, respectively. Nevertheless, the quantities involved represent different concepts since hypothetical fluids are defined differently in both approaches. Thus, the dissociated hypothetical fluid in the TSAM mimics a typical fluid following the Flory theory⁴⁶ (i.e., a real fluid in which association never occurs). In this work, the dissociated hypothetical fluid is constructed from the monomers residing in the pure self-associated liquid where association evidently takes place. Therefore, a comparison with the results obtained by TSAM can be misleading. With this constraint in mind, next we summarize the general results of the TSAM for the response functions studied here in order to seek coincidences or discrepancies. As regards the residual heat capacity, the non-specific contribution is considered constant whereas the association term takes the shape of a Schottky peak. Accordingly, the maximum in the residual heat capacity with TSAM comes exclusively from the association term, which is not the case with our approach. Similarly to our results, however, $(\partial V/\partial T)_p$ and $(\partial V/\partial p)_T$ are governed mainly by the term for the dissociated hypothetical fluid.

As stated in the Introduction, the SAFT equation⁶⁰ expresses the residual Helmholtz free energy as a combination of three contributions, namely: monomer, chain and association. One major advantage of using a molecular-based equation is that the different microscopic contributions to the total derivative properties can be split and quantified. Thus, calculating the second-order temperature derivative of the Helmholtz potential allows one to obtain the isochoric heat capacity and its contributions. The isobaric heat capacity can be also determined since it is related to the isochoric one through the well-known thermodynamic relation; however, calculating their contributions is no possible. It is therefore pointless to compare the contributions provided by the SAFT equations with our calculations since they correspond to different properties. In any case, our results and those obtained with the SAFT equations⁴¹,⁴² testify to the significance of association to heat capacities. The second-order volume derivative of the Helmholtz potential can be determined similarly

![](./images/811688000164462596_5.jpg)

FIG. 5. (a) Temperature volume derivative $(\partial V/\partial T)_p$ ($\bigcirc$) and its monomer and association contributions, $(\partial V_A/\partial T)_p$ ($\blacksquare$) and $(\partial V_B/\partial T)_p$ ($\boldsymbol{\times}$) as a function of $T$. (b) Pressure volume derivative $(\partial V/\partial p)_T$ ($\bigcirc$) and its monomer and association contributions, $(\partial V_A/\partial p)_T$ ($\blacksquare$) and $(\partial V_B/\partial p)_T$ ($\boldsymbol{\times}$) plotted against $T$.

to the temperature derivative in order to calculate the inverse of the isothermal compressibility and its contributions. In this case, these results are amenable to comparison with ours and they both indicate that association is not the dominant contribution to this property.

By using the fluctuation method, and splitting the energy into Lennard-Jones and electrostatic interactions, Medeiros *et al.*⁴⁴ determined various response functions in terms of pairwise fluctuations $\langle\delta X\delta Y\rangle$ according to the following expressions:

$$
C_{p}^{r}(T, p)=\frac{1}{k_{B} T^{2}}\left(\begin{array}{c}
\left\langle\left(\delta U^{L J}\right)^{2}\right\rangle+\left\langle\left(\delta U^{e l}\right)^{2}\right\rangle+2\left\langle\left(\delta U^{L J} \delta U^{e l}\right)\right\rangle \\
+2 p\left\langle\left(\delta U^{L J} \delta V\right)\right\rangle+2 p\left\langle\left(\delta U^{e l} \delta V\right)\right\rangle+2 p\left\langle(\delta V)^{2}\right\rangle
\end{array}\right)-N k_{B} \tag{13}
$$

$$
\alpha_{p}=\frac{1}{\langle V\rangle k_{B} T^{2}}\left(\left\langle\left(\delta U^{L J} \delta V\right)\right\rangle+\left\langle\left(\delta U^{e l} \delta V\right)\right\rangle+\left\langle(\delta V)^{2}\right\rangle\right) \quad(14)
$$

$$
\kappa_{T}=\frac{1}{\langle V\rangle k_{B} T}\left\langle(\delta V)^{2}\right\rangle. \tag{15}
$$

where $U^{LJ}$ and $U^{el}$ represent Lennard-Jones and electrostatic energy interactions, respectively, and the brackets denote averages throughout the simulation. These authors found the main contribution to the residual isobaric heat capacity to come from the first three terms (i.e., the energetic terms). The first such term was affected by both hydrogen bond and other interactions, whereas the other two were only influenced by hydrogen bond interactions. Therefore, they found association to play a central role, even though non-bonding interactions exhibited a non-negligible contribution. This result is consistent with ours: both the association term and the monomer fluid term contribute to the total isobaric heat capacity. On the other hand, they concluded that association had little effect on volumetric fluctuations; therefore, as also suggested by our results, the association contribution to the isobaric thermal expansivity and isothermal compressibility is negligible.

### IV. CONCLUSIONS AND OUTLOOK

As shown in this work, the proposed method allows one to gain insight into the microscopic origin of thermodynamic response functions in the context of Monte Carlo simulations. Specifically, it allowed us to determine the monomer and association contributions to the residual isobaric heat capacity, and to the temperature and pressure derivatives of the volume via $NpT$ MC simulations from 220 to 1500 K on the 50 MPa isobar for OPLS methanol. Based on the results, the association term is relevant to the residual heat capacity but has a negligible influence on volumetric properties—they are dominated by the monomer term, which also plays a central role in the residual heat capacity. These results are quite consistent with others of Medeiros *et al.*, who also used MC simulations but approached the problem via the fluctuation method and a qualitative analysis based on the general characteristics of the hydrogen bond. Likewise, a comparison with other works in this field has been made, emphasizing the analogies and differences between them. Finally, a comprehensive study of structural features has been carried out and some correlations with the thermodynamic behavior were found, which were particularly relevant for the isobaric heat capacity of the monomeric fluid.

Now that the proposed methodology has proved suitable for the intended purpose, it could also be applied to a variety of other problems. We are especially interested in three specific cases. One is the temperature-dependence of a pure self-associated liquid in the gas phase (1 bar) going from the ideal gas state (high temperature) to its boiling point since decreasing the temperature over this range causes an abrupt change in its properties (particularly its second-order thermodynamic derivatives). Another potential application is to study methanol at high pressures (around 1 GPa), where an intriguing structural behavior was found. Finally, this procedure could be used to analyze {pure self-associated + inert solvent} mixtures, the rich behavior of which has been well established by experimental techniques and extensively explored with simple models based on the association concept.

## ACKNOWLEDGMENTS
Financial support from Dirección Xeral de I + D da Xunta de Galicia (projects PGIDIT-06-PXIB-3832828-PR and INCITE09E2R383108ES) and Universidad de Vigo (project 08VI-A12) has been greatly appreciated. The authors are grateful to the Ministerio de Educación y Ciencia under the Program Nacional de Formación del Profesorado Universitario (No. AP2007-02165) for supporting the research of P. Gómez-Álvarez and to the Dirección Xeral de Ordenación e Calidade do Sistema Universitario de Galicia from the Consejería de Educación e Ordenación Universitaria-Xunta de Galicia for grant funding to A. Dopazo-Paz. We are also grateful to CESGA (Santiago de Compostela, Spain) for providing access to computing facilities.

$^{1}$O. Mishima and H. E. Stanley, *Nature* **396**, 329 (1998).
$^{2}$P. H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, *Nature* **360**, 324 (1992).
$^{3}$J. R. Errington, P. G. Debenedetti, and S. Torquato, *Phys Rev. Lett.* **89**, 215503 (2002).
$^{4}$J. A. Barker and R. O. Watts, *Mol. Phys.* **26**, 789 (1973).
$^{5}$F. Dolezalek, Z. Phys. Chem. **64**, 727 (1908).
$^{6}$W. E. Acree, *Thermodynamic Properties of Non Electrolyte Solutions* (Academic Press, New York, 1984).
$^{7}$H. Renon and J. M. Prausnitz, *Chem. Eng. Sci.* **22**, 299 (1967).
$^{8}$J. D. Gmehling, D. D. Liu, and J. M. Prausnitz, *Chem. Eng. Sci.* **34**, 951 (1979).
$^{9}$I. Nagata, *Fluid Phase Equil.* **19**, 153 (1985).
$^{10}$H. Wenzel, R. A. S. Moorwood, and M. Baumgärtner, *Fluid Phase Equil.* **9**, 225 (1982).
$^{11}$G. D. Ikonomou and M. D. Donohue, *AIChE J.* **32**, 1716 (1986).
$^{12}$G. D. Ikonomou and M. D. Donohue, *Fluid Phase Equil.* **39**, 129 (1988).
$^{13}$A. Anderko, *Fluid Phase Equil.* **45**, 39 (1989).
$^{14}$A. Anderko, *Fluid Phase Equil.* **50**, 21 (1989).
$^{15}$C. Panayiotou, J. *Phys. Chem.* **92**, 2960 (1989).
$^{16}$C. Panayiotou, *Fluid Phase Equil.* **56**, 171 (1990).
$^{17}$E. A. Guggenheim, *Proc. R. Soc. London Ser. A* **183**, 213 (1945).
$^{18}$E. A. Guggenheim, *Mixtures* (Clarendon, Oxford, 1952).
$^{19}$G. M. Wilson, J. *Amer. Chem. Soc.* **86**, 127 (1964).

$^{20}$H. Renon and J. M. Prausnitz, *AIChE J.* **14**, 135 (1968).
$^{21}$D. Abrams and J. M. Praustnitz, *AIChE J.* **21**, 116 (1975).
$^{22}$J. H. Vera, S. G. Sayegh, and G. A. Radcliff, *Fluid Phase Equil.* **1**, 113 (1977).
$^{23}$C. Panayiotou and I. C. Sanchez, *J. Phys. Chem.* **95**, 10090 (1991).
$^{24}$H. C. Andersen, J. *Chem. Phys.* **59**, 4714 (1973).
$^{25}$H. C. Andersen, J. *Chem. Phys.* **61**, 4985 (1974).
$^{26}$K. Olaussen and G. Stell, J. *Stat. Phys.* **62**, 221 (1991).
$^{27}$M. S. Wertheim, J. *Stat. Phys.* **35**, 35 (1984).
$^{28}$M. S. Wertheim, J. *Stat. Phys.* **42**, 459 (1986).
$^{29}$M. S. Wertheim, J. *Stat. Phys.* **42**, 477 (1986).
$^{30}$M. S. Wertheim, J. *Chem. Phys.* **85**, 2929 (1986).
$^{31}$M. S. Wertheim, J. *Chem. Phys.* **87**, 7323 (1987).
$^{32}$G. Jackson, W. G. Chapman, and K. E. Gubbins, *Mol. Phys.* **65**, 1 (1988).
$^{33}$W. G. Chapman, G. Jackson, and K. E. Gubbins, *Mol. Phys.* **65**, 1057 (1988).
$^{34}$W. G. Chapman, K. E. Gubbins, G. Jackson, and M. Radosz, *Ind. Eng. Chem. Res.* **29**, 1709 (1990).
$^{35}$M. Zabransky, V. Ruzicka, V. Majer, and E. S. Domalski, *Heat Capacity of Liquids. Critical Review and Recommended Values. Monograph Nº 6 Vols. I and II* (American Chemical Society, Washington D. C., 1996); M. Zabransky, V. Ruzicka, and V. Majer, *J. Phys. Chem. Ref. Data* **19**(3), 719 (1990).
$^{36}$M. Zabransky, V. Ruzicka, and E. S. Domalski, *J. Phys. Chem. Ref. Data* **30**(5), 1199 (2001).
$^{37}$*CDATA: Database of Thermodynamics and Transport Properties for Chemistry and Engineering* (GmbH, Berlin, Prague, 1991).
$^{38}$M. Zabransky, M. Bures, and V. Ruzicka, *Thermochim. Acta* **215**, 23 (1993).
$^{39}$C. A. Cerdeiriña, D. González-Salgado, L. Romaní, M. C. Delgado, L. A. Torres, and M. Costas, J. *Chem. Phys.* **120**, 6648 (2004).
$^{40}$C. A. Cerdeiriña, J. Troncoso, D. González-Salgado, G. García-Miaja, G. O. Hernández-Segura, D. Bessieres, M. Medeiros, L. Romaní, and M. Costas, *J. Phys. Chem. B* **111**, 1119 (2007).
$^{41}$T. Lafitte, D. Bessieres, M. M. Piñeiro, and J.-L. Daridon, *J. Chem. Phys.* **124**, 024509 (2006).
$^{42}$F. Llovell and L. F. Vega, *J. Phys. Chem B* **110**, 11427 (2006).
$^{43}$M. Medeiros, *J. Phys. Chem. B* **108**, 2676 (2004).
$^{44}$M. Medeiros, C. O. Armas-Alemán, M. Costas, and C. A. Cerdeiriña, *Ind. Eng. Chem. Res.* **45**, 2150 (2006).
$^{45}$M. M. Piñeiro, C. A. Cerdeiriña, and M. Medeiros, *J. Chem. Phys.* **129**, 014511 (2008).
$^{46}$P. J. Flory, J. *Am. Chem. Soc.* **87**, 33 (1965).
$^{47}$M. Lagache, P. Ungerer, A. Boutin, and A. H. Fuchs, *Phys. Chem. Chem. Phys.* **3**, 4333 (2001).
$^{48}$M. Chalaris and J. Samios, *J. Phys. Chem. B* **103**, 1161 (1999).
$^{49}$J. C. Gil Montoro and J. L. F. Abascal, *J. Phys. Chem.* **97**, 4211 (1993).
$^{50}$W. L. Jorgensen, *J. Phys. Chem* **90**, 1276 (1986).
$^{51}$M. Allen and D. J. Tildesley, *Computer Simulation of Liquids* (Oxford University Press, New York, 1987).
$^{52}$D. Frenkel and B. Smit, *Understanding Molecular Simulation* (Academic, New York, 2002).
$^{53}$L. Onsager, J. *Am. Chern. Soc.* **58**,1486 (1936).
$^{54}$J. A. Barker and R. O. Watts, *Mol. Phys.* **23**, 789 (1973).
$^{55}$M. Neumann, *J. Chem. Phys.* **82**, 5663 (1985).
$^{56}$M. Lísal, W. R. Smith, and I. Nezbeda, *J. Phys. Chem. B* **103**, 10496 (1999).
$^{57}$M. Haughney, M. Ferrario, and I. R. McDonald, *J. Phys. Chem.* **91**, 4935 (1987).
$^{58}$L. Saiz, J. A. Padró, and E. Guàrdia, *J. Phys. Chem.* **101**, 78 (1997).
$^{59}$G. Voronoi and J. Reine, *Angew. Math.* **134**, 198 (1908).
$^{60}$W. G. Chapman, K. E. Gubbins, G. Jackson, and M. Radosz, *Fluid Phase Equil.* **52**, 31 (1989).

The Journal of Chemical Physics is copyrighted by the American Institute of Physics (AIP). Redistribution of journal material is subject to the AIP online journal license and/or AIP copyright. For more information, see http://ojps.aip.org/jcpo/jcpcr/jsp