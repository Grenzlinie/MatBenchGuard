![](./images/812056687568486401_1.jpg)

Materials Science and Engineering A 443 (2007) 178-184

![](./images/812056687568486401_2.jpg)
www.elsevier.com/locate/msea

# A computational thermodynamics approach to the Gibbs-Thomson effect

Sina Shahandeh *, Said Nategh

Department of Material Science and Engineering, Sharif University of Technology, Tehran, Iran

Received 1 June 2006; received in revised form 9 August 2006; accepted 10 August 2006

## Abstract

In two-phase system, curvature of interface leads to increase of solute concentration in matrix. This effect plays a significant role in solidification, precipitation, nucleation and growth and coarsening. There are number of models and formulas for Gibbs-Thomson effect in binary alloys. In this paper with the help of CALPHAD calculations, new approach for describing this effect in binary and multicomponent systems is proposed. In this generalized method no traditional simplifying assumption are considered and this yield to more accurate result for Gibbs-Thomson phenomenon. This model is compared with previous formulas in some case alloying systems.

© 2006 Elsevier B.V. All rights reserved.

**Keywords:** Interface boundary; Gibbs-Thomson effect; Phase equilibria; CALPHAD

---

## 1. Introduction

In the presence of two phases, one can define equilibria that determine equilibrium concentration at the interface. Generally, many parameters can alter this equilibrium. One of them is pressure, when internal pressure of one phase increases the Gibbs energy of it will increase too and this will change equilibria. This pressure can be caused by interface curvature and consequently the equilibrium concentration of two phases at interface will be changed. This effect first was observed for small liquid particles in equilibrium with gas by Thomson (Lord Kelvin) [1]. Then Gibbs [2], Ostwald [3] and Freundlich [4] formulated a relation for change of concentration around small curved particles. From that time up until now several authors have suggested other formulations for the Gibbs-Thomson effect, especially in recent years when the need for more accurate data came out. New phase transformation and structural evolution models for important phenomena like nucleation, growth, coarsening, etc., depend on this effect. Therefore, an accurate model for Gibbs-Thomson effect can help us to have better microstructural evolution models. In addition, this effect is a new way to estimate interfacial energy of precipitates [5,6] and this computational thermodynamics model can prepare more accurate results for interfacial energy. At the knowledge of present authors, until now there is no accurate theory for Gibbs-Thomson effect in concentrated multicomponent alloys. In this model based on increase in Gibbs energy of precipitate due to curvature, the phase equilibria is calculated and the equilibrium concentration of phases at interface can be found. This method also can be generalized into multicomponent alloys.

In this article, first we briefly review previous models and compare them with respect to their assumption and simplification. Then the novel method for description of the Gibbs-Thomson effect in binary and ternary alloys will be described. Finally, some pertinent result of this effect, including phase boundary movement and concentration increase path in multicomponent alloys will be described.

## 2. Analytical models for dilute binary alloys

Increase of solvent atom at the curved interface is caused by additional free energy. This extra energy comes from internal pressure of the second phase (β):

$$
\Delta G_{r}=\int_{P_{0}}^{P(r)} V_{\mathrm{m}}^{\beta} \mathrm{d} P \tag{1}
$$

where $V_{\mathrm{m}}$ is molar volume of second phase. The pressure $P(r)$ compensates the surface tension at the curved interface. The force balance is shown in Fig. 1. The pressure in β phase must be more than pressure of the α phase in order to balance the force of the surface tension on small element ds. For simplicity, the principal curvatures of interface element are assumed the same

---

* Corresponding author. Fax: +98 21 66 162 712.
E-mail address: sinashahandeh@yahoo.com (S. Shahandeh).

0921-5093/$ - see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.msea.2006.08.062

![](./images/812056687568486401_3.jpg)
![](./images/812056687568486401_4.jpg)

Fig. 1. (a) Small element of interface between α and β phases. (b) Cross-section of element and balance of tension force and internal pressure.

$(\kappa_1=\kappa_2)$. By balancing the force in normal direction of ds, it can be written:

$$
2\pi(r \sin \mathrm{d}\theta)(\sigma_{\alpha\beta} \sin \mathrm{d}\theta)=\pi(r \sin \mathrm{d}\theta)^2 P_r \Rightarrow P_r=\frac{2\sigma_{\alpha\beta}}{r} \quad (2)
$$

where $\sigma_{\alpha\beta}$ is energy of $\alpha-\beta$ interface. If the volume change of β phase by this pressure is negligible, by substituting $P_r$ in Eq. (1):

$$
\Delta G_r=\frac{2\sigma_{\alpha\beta} V_{\mathrm{m}}^{\beta}}{r} \quad (3)
$$

The simple Gibbs-Thomson equation can be derived by some assumptions that in general case are unreasonable for solid-state system. For example, the β must be pure B and the α must be dilute ideal phase, in this condition the additional free energy is completely due to the increase of activity (partial pressure) of B in the matrix:

$$
\begin{aligned}
\Delta G_{r} & =\mu_{\mathrm{B}}^{\beta}(r)-\mu_{\mathrm{B}}^{\beta}(\infty)=\mu_{\mathrm{B}}^{\alpha}(r)-\mu_{\mathrm{B}}^{\alpha}(\infty) \\
& =R T \ln \left(\frac{a_{\mathrm{B}}^{\alpha}(r)}{a_{\mathrm{B}}^{\alpha}(\infty)}\right)
\end{aligned} \quad (4)
$$

Since the α is assumed to be ideal solution, Eq. (4) can be simplified to:

$$
X_{\mathrm{B}}^{\alpha}(r)=X_{\mathrm{B}}^{\alpha}(\infty) \exp \left(\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}\right) \quad (5)
$$

This equation is only applicable for unary and binary liquid-vapor systems where $X_{\mathrm{B}}^{\alpha}$ should be replaced by $P_{\mathrm{g}}$ [7]. Unfortunately, despite its large inaccuracy many authors have used this equation or even linerized approximation of it.

Based on molar Gibbs free energy diagrams, Hillert [8] proposed another relation for Gibbs-Thomson effect in dilute binary alloys. It relates additional Gibbs energy of β to the concentration change of α:

$$
\begin{aligned}
\mathrm{d} G^{\beta} & =X_{\mathrm{A}}^{\beta} \mathrm{d} \mu_{\mathrm{A}}^{\beta}+X_{\mathrm{B}}^{\beta} \mathrm{d} \mu_{\mathrm{B}}^{\beta} \rightarrow \Delta G_{r} \\
& =X_{\mathrm{A}}^{\beta}\left(\mu_{\mathrm{A}}^{\beta}(r)-\mu_{\mathrm{A}}^{\beta}(\infty)\right)+X_{\mathrm{B}}^{\beta}\left(\mu_{\mathrm{B}}^{\beta}(r)-\mu_{\mathrm{B}}^{\beta}(\infty)\right) \\
& =\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{r}
\end{aligned} \quad (6)
$$

At the equilibrium state; $\mu_{i}^{\beta}=\mu_{i}^{\alpha}$ and $\mu_{i}=R T \ln \gamma_{i} X_{i}$, consequently:

$$
\begin{aligned}
& \left(1-X_{\mathrm{B}}^{\beta}\right) \ln \left(\frac{\gamma_{\mathrm{A}}^{\alpha}(r) X_{\mathrm{A}}^{\alpha}(r)}{\gamma_{\mathrm{A}}^{\alpha}(\infty) X_{\mathrm{A}}^{\alpha}(\infty)}\right)+X_{\mathrm{B}}^{\beta} \ln \left(\frac{\gamma_{\mathrm{B}}^{\alpha}(r) X_{\mathrm{B}}^{\alpha}(r)}{\gamma_{\mathrm{B}}^{\alpha}(\infty) X_{\mathrm{B}}^{\alpha}(\infty)}\right) \\
& \quad=\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}
\end{aligned} \quad (7)
$$

where $\gamma_{i}(r)$ is activity coefficient of element i in concentration $X_{i}(r)$. Because solutions are dilute the $\gamma_{i}$ is constant, therefore, Gibbs-Thomson equation for dilute alloys can be written as:

$$
\left(1-X_{\mathrm{B}}^{\beta}\right) \ln \left(\frac{1-X_{\mathrm{B}}^{\alpha}(r)}{1-X_{\mathrm{B}}^{\alpha}(\infty)}\right)+X_{\mathrm{B}}^{\beta} \ln \left(\frac{X_{\mathrm{B}}^{\alpha}(r)}{X_{\mathrm{B}}^{\alpha}(\infty)}\right)=\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}
$$

Qian [9] proved this relation by use of free energy tangent construction. Perez proposed another proof [10] and similar relation for compound precipitates is given in ref. [11]. Eq. (8) can simplify when concentration changes are small in comparison with equilibrium concentration; $(X_{\mathrm{B}}(r)-X_{\mathrm{B}}(\infty))/X_{\mathrm{B}}(\infty)\ll1$. This relation is [12]:

$$
X_{\mathrm{B}}^{\alpha}(r)=X_{\mathrm{B}}^{\alpha}(\infty) \exp \left(\frac{1-X_{\mathrm{B}}^{\alpha}(\infty)}{X_{\mathrm{B}}^{\beta}(\infty)-X_{\mathrm{B}}^{\alpha}(\infty)} \frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}\right) \quad (9)
$$

The comparison of these relations and other simplified formulas are given in refs. [9,10].

### 3. Analytical models for concentrated binary alloys

Eliminating the assumption of dilute alloy (constant activity coefficient) leads to better results for Gibbs-Thomson effect. As will be shown in Section 4, there is a considerable discrepancy between dilute solution models and real alloy models that depends on thermodynamic behavior of the system.

In these models, thermodynamic properties of solutions are considered. For simple case when $(X_{\mathrm{B}}(r)-X_{\mathrm{B}}(\infty))/X_{\mathrm{B}}(\infty)\ll1$ is satisfied for both first and second phase, simple relation can be derived [13,14]:

$$
X_{\mathrm{B}}^{\alpha}(r)=X_{\mathrm{B}}^{\alpha}(\infty)\left(1+\frac{1-X_{\mathrm{B}}^{\alpha}(\infty)}{X_{\mathrm{B}}^{\beta}(\infty)-X_{\mathrm{B}}^{\alpha}(\infty)} \frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r e_{\mathrm{B}}^{\alpha}\left(X_{\mathrm{B}}^{\alpha}(\infty)\right)}\right)
$$

where $e_{\mathrm{B}}^{\alpha}$, the Darken factor, is a function of $X_{\mathrm{B}}^{\alpha}$ and is given by:

$$
e_{\mathrm{B}}^{\alpha}\left(X_{\mathrm{B}}^{\alpha}\right)=1+\left(\frac{\partial \ln \gamma_{\mathrm{B}}^{\alpha}}{\partial \ln X_{\mathrm{B}}^{\alpha}}\right)
\tag{11}
$$

Martin and Doherty [14] proposed another relation that does not include the simplicity of the small concentration changes and is more realistic:

$$
\begin{aligned}
& \ln \left(\frac{X_{\mathrm{B}}^{\alpha}(r)}{X_{\mathrm{B}}^{\alpha}(\infty)}\right)=\left(\frac{1-X_{\mathrm{B}}^{\alpha}(r)}{X_{\mathrm{B}}^{\beta}(\infty)-X_{\mathrm{B}}^{\alpha}(\infty)} \frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}\right) \\
& \quad-\ln \left(\frac{\gamma_{\alpha}\left(X_{\mathrm{B}}^{\alpha}(r)\right)}{\gamma_{\alpha}\left(X_{\mathrm{B}}^{\alpha}(\infty)\right)}\right)
\end{aligned}
\tag{12}
$$

This implicit relation is a nonlinear equation that could be solved to obtain $X_{\mathrm{B}}^{\alpha}(r)$. This relation is applicable in all ranges of radius and concentration increase. Based on the Gibbs–Duhem relations Qian and Lim derived another formula for Gibbs–Thomson effect [15]. It is similar to Eq. (8), but thermodynamic behavior of solutions is included in Darken factor and the simplification for ideality is not considered:

$$
\begin{aligned}
& \left(1-X_{\mathrm{B}}^{\beta}\right) \ln \left(\frac{1-X_{\mathrm{B}}^{\alpha}(r)}{1-X_{\mathrm{B}}^{\alpha}(\infty)}\right)+X_{\mathrm{B}}^{\beta} \ln \left(\frac{X_{\mathrm{B}}^{\alpha}(r)}{X_{\mathrm{B}}^{\alpha}(\infty)}\right) \\
& \quad=\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r e_{\mathrm{B}}^{\alpha}\left(X_{\mathrm{B}}^{\alpha}(\infty)\right)}
\end{aligned}
\tag{13}
$$

Eq. (13) is derived on the hypothesis that the darken factor is independent of $X_{\mathrm{B}}^{\alpha}$. This is only true for solutions that have approximately linear partial excess free energy versus solute concentration $(\bar{G}_{\mathrm{B}}^{\mathrm{xs}}=R T \ln \gamma_{\mathrm{B}}^{\alpha} \approx a+b X_{\mathrm{B}}^{\alpha})$. For obtaining better relation, one can integrate Eq. (10) of ref. [15] with variable Darken factor:

$$
\begin{aligned}
& \int_{X_{\mathrm{B}}^{\alpha}(\infty)}^{X_{\mathrm{B}}^{\alpha}(r)}\left(\frac{X_{\mathrm{B}}^{\beta}-X_{\mathrm{B}}^{\alpha}}{1-X_{\mathrm{B}}^{\alpha}}\right) \frac{1}{X_{\mathrm{B}}^{\alpha}} e_{\mathrm{B}}^{\alpha} \mathrm{d} X_{\mathrm{B}}^{\alpha}=\int_{P^{\beta}(\infty)}^{P^{\beta}(r)} \frac{V_{\mathrm{m}}^{\beta}}{R T} \mathrm{~d} P^{\beta} \\
& \quad=\frac{2 \sigma_{\alpha \beta} V_{\mathrm{m}}^{\beta}}{R T r}
\end{aligned}
\tag{14}
$$

The Darken factor can be simply computed from $G^{\alpha}$ function by derivation. After integrating Eq. (14), an equation consists of $X_{\mathrm{B}}^{\alpha}(r)$ will be obtained. This nonlinear equation should be solved for each interface curvature to calculate concentration in matrix. It is interesting that, as it is plotted in Fig. 3 for the case of Pb–Sn system, Eq. (14) completely coincide with Eq. (12) and basic Eq. (7), though they are derived by different methods.

The limitation of Eqs. like (12) and (14) is only due to the assumption of constant concentration for the second phase. When additional energy of curved interface alters the equilibria, both concentration of matrix and second phase will change. This can be easily recognized from Gibbs energy curves tangent construction ([9]; Fig. 2) except when the second phase is a stoichiometric compound (example of $\mathrm{Fe}_{3} \mathrm{C}$ in Section 4).

This remaining assumption can also be eliminated. By increase of interface curvature the energy of precipitate will rise. If one, calculate the phase equilibria or equilibrium concentration, this can be concluded in Gibbs–Thomson effect. This is analytically impossible to find out the solution of nonlinear equation of equilibria between two phases even in binary alloys. Therefore, one can use CALPHAD methods.

![](./images/812056687568486401_5.jpg)

Fig. 2. Free energy of mixing for fcc matrix, bct particles and liquid phases in Pb–Sn alloy. Squares and circles are equilibrium concentration at flat and curved (50 nm radius) interface, respectively. Note to the change of precipitate composition after curvature (free energy) increase.

## 4. CALPHAD model for binary alloys

The accurate results for Gibbs–Thomson effect can be found by calculation of phase equilibria with additional free energy of curved interface. For two-phase system, this equilibrium condition can be found by solving two nonlinear equations:

$$
\left\{\begin{array}{l}
\mu_{\mathrm{A}}^{\alpha}=\mu_{\mathrm{A}}^{\beta} \\
\mu_{\mathrm{B}}^{\alpha}=\mu_{\mathrm{B}}^{\beta}
\end{array}\right.
\tag{15}
$$

where $\mu_{i}^{\alpha}$ and $\mu_{i}^{\beta}$ are chemical potential of compound $i$ in $\alpha$ and $\beta$ phase. These quantities can be calculated from these relations:

$$
\begin{aligned}
& \mu_{\mathrm{A}}^{\alpha}=\Delta G_{\mathrm{mix}}^{\alpha}-X_{\mathrm{B}} \frac{\partial \Delta G_{\mathrm{mix}}^{\alpha}}{\partial X_{\mathrm{B}}}, \quad \mu_{\mathrm{B}}^{\alpha}=\Delta G_{\mathrm{mix}}^{\alpha}+X_{\mathrm{A}} \frac{\partial \Delta G_{\mathrm{mix}}^{\alpha}}{\partial X_{\mathrm{B}}} \\
& \mu_{\mathrm{A}}^{\beta}=\Delta G_{\mathrm{mix}^{*}}^{\beta}-X_{\mathrm{B}} \frac{\partial \Delta G_{\mathrm{mix}^{*}}^{\beta}}{\partial X_{\mathrm{B}}}, \quad \mu_{\mathrm{B}}^{\beta}=\Delta G_{\mathrm{mix}^{*}}^{\beta}+X_{\mathrm{A}} \frac{\partial \Delta G_{\mathrm{mix}^{*}}^{\alpha}}{\partial X_{\mathrm{B}}}
\end{aligned}
\tag{16}
$$

where $\Delta G_{\mathrm{mix}^{*}}^{\beta}=\Delta G_{\mathrm{mix}}^{\beta}(r=\infty)+\Delta G_{\text {excess }}(r)$ (the summation of excess energy of Gibbs–Thomson effect and mixing free energy of second phase with flat interface). $\Delta G_{\text {mix }}^{\alpha, \beta}$ is characteristic of thermodynamic behavior of $\alpha$ and $\beta$ phases and can be obtained from experimental works and CALPHAD optimization and even first principle calculation. They are collected in different databases and software packages [e.g. 16,17]. In order to find a relation between curvature and concentration the algorithm is this; first additional free energy imposed by the curved interface, $\Delta G_{\text {excess }}(r)$, must be found from Eq. (3). For each $r$ the $\Delta G_{\mathrm{mix}^{*}}^{\beta}$ in Eq. (16) is calculated and with $\Delta G_{\text {mix }}^{\alpha}$ is substituted into Eq. (16). Then chemical potentials are calculated and Eq.

![](./images/812056687568486401_6.jpg)

Fig. 3. Models proposed for the Gibbs-Thomson effect for Sn-rich precipitate in Pb-rich matrix in Pb-Sn binary alloy at 150 °C.

(16) should be solved. Consequently, in each $r$, particular equilibrium concentration at interface will be found, respectively.

For illustration purpose, the example of Sn-rich BCT particles in Pb-rich FCC matrix is given. Thermocalc® software [16] was used to calculate $\Delta G_{\text{mix}}^{\text{fcc,bct}}$. The original thermodynamic data for Pb-Sn alloy is taken from ref. [19]. The interfacial energy was assumed 235 mJ/mol [18] and molar volume of precipitates is $16.26 \times 10^{-6} \, \text{m}^3/\text{mol}$ (density of Sn is $7.3 \, \text{g/cm}^3$), thus for instance, particles with 20 nm radius have internal pressure of 23.5 MPa because of their interface tension. This pressure causes 382.11 J/mol additional free energy for the precipitates. The raised up Gibbs energy curve for bct precipitate is shown in Fig. 2.

Because of this additional energy, equilibrium concentration that is found by Eq. (15) is changed for both matrix and precipitates. Hence, we did not consider the assumption of constant concentration for the second phase in this method and this leads to reaching the generalized description of Gibbs-Thomson effect. For this alloy at 150 °C different results of different models are plotted in Fig. 3. As it is obvious, there is considerable discrepancy between dilute and concentrated alloy models. The reason is that, in this system the matrix concentration is high (~20 at.%) and solutions have significant deviation from ideal behavior, so this alloy is selected as an example of concentrated solutions.

For stoichiometric compound precipitates, the concentration of second phase cannot change, therefore, the assumption of constant composition can be naturally fulfilled. However, different models will show different result if the matrix phase has concentrated solution behavior. In dilute solutions such as carbon in the bcc ferrite in Fe-C, the concentration of carbon in equilibrium with cementite at 690 °C is $6.077 \times 10^{-2}$ at.%. The molar volume of $\text{Fe}_3\text{C}$ is $7.0434 \times 10^{-6} \, \text{m}^3/\text{mol}$ and interfacial energy is assumed to be $0.174 \, \text{J/m}^2$ [10]. Darken factor in this concentration is 1.0037, very close to 1, the factor of dilute (Henry) solution. Consequently, all modes that were proven by tangent construction or Gibbs-Dohem relation should be identical. Fig. 4 illustrates that all concentrated models and computational thermodynamics model almost coincide with Hillert dilute solution model. However, because Gibbs-Thomson formula (Eq. (5)) has false assumption for second phase; $X_{\text{B}}^{\beta} = 1$ [10], it shows significant difference. Compare this case with Pb-Sn system with $X_{\text{B}}^{\alpha} = 19.29$ at% and $e_{\text{B}}^{\alpha} = 0.487$ that difference between concentrated and dilute modes is considerable but because $X_{\text{B}}^{\beta} = 0.98 \approx 1$ the Hillert and Gibbs-Thomson model is almost similar in Pb-Sn alloys.

![](./images/812056687568486401_7.jpg)

Fig. 4. Increase of C atoms concentration in bcc ferrite with decrease in radius of cementite particles at 690 °C in Fe-C alloy, predicted from different models.

## 5. CALPHAD model for multicomponent alloys

The advantage of this computational thermodynamics approach is that it can be simply generalized into multicomponent systems. Different method for finding equilibria should be used. First, Gibbs free energy of solutions must be known:

$$
\begin{aligned}
\Delta G_{\text{mix}}^{\alpha} &= f_{\alpha}(X_{\text{B}}^{\alpha}, X_{\text{C}}^{\alpha}, \dots) \\
\Delta G_{\text{mix}}^{\beta} &= f_{\beta}(X_{\text{B}}^{\beta}, X_{\text{C}}^{\beta}, \dots)
\end{aligned} \tag{17}
$$

where $f_{\alpha,\beta}$ are solutions thermodynamic behavior functions, whether they are expressed by simple algebraic relation for regular solutions or complicated sublattice models for intermetallic compounds. The additional energy of second phase because of curvature $(\Delta G_{\text{excess}}(r))$ is calculated from Eq. (3). Then with these data, the phase equilibria in each radius can be found by total energy minimization. In constant temperature the optimization function is:

$$
\begin{aligned}
G_{\text{Total}}(&X_{\text{B}}^{\alpha}, X_{\text{C}}^{\alpha}, \dots, X_{\text{B}}^{\beta}, X_{\text{C}}^{\beta}, \dots) \\
&= x_{\text{f}}^{\alpha} \Delta G_{\text{mix}}^{\alpha} + x_{\text{f}}^{\beta}(\Delta G_{\text{mix}}^{\beta} + \Delta G_{\text{excess}}(r))
\end{aligned} \tag{18}
$$

![](./images/812056687568486401_8.jpg)

Fig. 5. Tangent construction in three-component system. Rectangles represent Gibbs free energy surface. M, P, O is $\alpha$ and $\beta$ phase boundary and alloy composition respectively. Dotted line is direction that composition of $\beta$ should be on it (optimization constrain).

where $x^{\alpha}$ and $x_{\mathrm{f}}^{\beta}$ are molar fraction of $\alpha$ and $\beta$ phase in the system and can be found by lever rule in multicomponent alloys [20,21]:

$$
\begin{aligned}
x_{\mathrm{f}}^{\alpha} & =\frac{\left[\left(X_{\mathrm{B}}^{\beta}-X_{\mathrm{B}}^{\text {alloy }}\right)^{2}+\left(X_{\mathrm{C}}^{\beta}-X_{\mathrm{C}}^{\text {alloy }}\right)^{2}+\cdots\right]^{1 / 2}}{\left[\left(X_{\mathrm{B}}^{\beta}-X_{\mathrm{B}}^{\alpha}\right)^{2}+\left(X_{\mathrm{C}}^{\beta}-X_{\mathrm{C}}^{\alpha}\right)^{2}+\cdots\right]^{1 / 2}} \\
x_{\mathrm{f}}^{\beta} & =\frac{\left[\left(X_{\mathrm{B}}^{\text {alloy }}-X_{\mathrm{B}}^{\alpha}\right)^{2}+\left(X_{\mathrm{C}}^{\text {alloy }}-X_{\mathrm{C}}^{\alpha}\right)^{2}+\cdots\right]^{1 / 2}}{\left[\left(X_{\mathrm{B}}^{\beta}-X_{\mathrm{B}}^{\alpha}\right)^{2}+\left(X_{\mathrm{C}}^{\beta}-X_{\mathrm{C}}^{\alpha}\right)^{2}+\cdots\right]^{1 / 2}}
\end{aligned}
\tag{19}
$$

where $X_{i}^{\text {alloy }}$ is the molar fraction of component $i$ in the alloy. In each interface curvature (radius), the $G_{\text {Total }}$ is a function of two phases composition. It means generally in $n$-component system $G_{\text {Total }}$ is $2(n-1)$ variable function. By minimization of this function, the equilibrium composition of the phases in each radius can be found.

An important point is that by determining composition of one phase, optimization constrain will impose on the composition of another phase. This is because in two-phase region, two-phase boundary points and alloy point should pass through a lever rule line (Fig. 5) [20,21]. This condition for ternary alloys can be written as:

$$
\frac{X_{\mathrm{B}}^{\alpha}-X_{\mathrm{B}}^{\text {alloy }}}{X_{\mathrm{C}}^{\alpha}-X_{\mathrm{C}}^{\text {alloy }}}=\frac{X_{\mathrm{B}}^{\alpha}-X_{\mathrm{B}}^{\beta}}{X_{\mathrm{C}}^{\alpha}-X_{\mathrm{C}}^{\beta}}
\tag{20}
$$

The slope of MO should be equal to the slope of MP in Fig. 5. Same relation can be derived for more than three components.

As an example, Gibbs-Thomson effect in $\mathrm{M}_{7} \mathrm{C}_{3}$ carbide and austenite in $\mathrm{Fe}-\mathrm{Cr}-\mathrm{C}$ alloys at $870{ }^{\circ} \mathrm{C}$ is discussed. Thermodynamic properties of solutions were obtained from PTERN database of Thermocalc $^{\circledR}$ software. Gibbs free energy of austenite phase in Fe-rich portion of phase diagram was interpolated by spline mesh from more than 1000 points. Gibbs energy of $\mathrm{M}_{7} \mathrm{C}_{3}$ also extracted in 500 points and this data was used as a $\Delta G_{\text {mix }}^{\alpha, \beta}$ by interpolation in each composition. Expressing Gibbs free energy functions by spline curves has no problem in numerical analysis, therefore, here we did not determine $\Delta G_{\text {mix }}$ function by a formula and directly use Thermocalc values. Inside PTERN database, this function is determined by thermodynamic models such as sublattice model [22], etc. Indeed, there is no difference between values of function, whether they are calculated from formula or accurate spline interpolation. A comprehensive review on CALPHAD method is given in ref. [22]. However, as described above, we used special approach for calculating total energy function and its minimum. Code was developed in MATLAB $^{\circledR}$ software.

![](./images/812056687568486401_9.jpg)

Fig. 6. Gibbs free energy of austenite and $\mathrm{M}_{7} \mathrm{C}_{3}$ carbide at $870{ }^{\circ} \mathrm{C}$. Alloy point is shown by circles at $\mathrm{Fe}-12 \mathrm{Cr}-10 \mathrm{C}$ (at\%). Markers in austenite and $\mathrm{M}_{7} \mathrm{C}_{3}$ energy surface show the equilibrium concentration after energy optimization. Similar calculation is preformed for carbide with $10 \mathrm{~nm}$ interface radius. Consequently, equilibrium composition change in both matrix and precipitates.

In this system, because $\mathrm{M}_{7} \mathrm{C}_{3}$ is assumed stoichiometric phase with a constant carbon concentration of 0.3 atomic frac-

![](./images/812056687568486401_10.jpg)

Fig. 7. Increase of equilibrium concentration of austenite by increase in interface curvature of $\mathrm{M}_{7} \mathrm{C}_{3}$ carbides in three $\mathrm{Fe}-\mathrm{Cr}-\mathrm{C}$ alloys at $870{ }^{\circ} \mathrm{C}$. The $y$-axis is concentration ratio of matrix in equilibrium with curved and flat interface. Curves with arrow are for carbon and without arrow are for chromium.

<table>
<caption>Table 1 Equilibrium composition of matrix at flat and curved interface with \( r = 10 \, \text{nm} \)</caption>
<thead>
<tr>
<th>\( X^{\text{alloy}} \)</th>
<th>\( X_{\text{C}}^{\text{fcc}} \)
(\( r = \infty \))</th>
<th>\( X_{\text{Cr}}^{\text{fcc}} \)
(\( r = \infty \))</th>
<th>\( X_{\text{C}}^{\text{fcc}} \)
(\( r = 10 \, \text{nm} \))</th>
<th>\( X_{\text{Cr}}^{\text{fcc}} \)
(\( r = 10 \, \text{nm} \))</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fe–0.1C–0.1Cr</td>
<td>0.0344</td>
<td>0.0230</td>
<td>0.0482 (40.1)</td>
<td>0.0328 (42.6)</td>
</tr>
<tr>
<td>Fe–0.1C–0.15Cr</td>
<td>0.0228</td>
<td>0.0397</td>
<td>0.0296 (29.8)</td>
<td>0.0444 (11.8)</td>
</tr>
<tr>
<td>Fe–0.1C–0.2Cr</td>
<td>0.0110</td>
<td>0.0561</td>
<td>0.0206 (87.2)</td>
<td>0.0703 (25.3)</td>
</tr>
</tbody>
</table>

Numbers in brackets indicate percent of increase in concentration.

tion, \( \Delta G_{\text{mix}}^{\beta} \) in Fig. 5 simplified to a line with constant "C" composition. Therefore, from constrain Eq. (20), \( X_{\text{Cr}}^{\text{M}_7\text{C}_3} \) will be found. In fact, because carbon content is fixed to 0.3, the intersection of lever rule line and \( \Delta G_{\text{mix}}^{\text{M}_7\text{C}_3} \) curve defines concentration of chromium in \( \text{M}_7\text{C}_3 \). The remaining variables for optimization are composition of austenite matrix:

$$
\begin{aligned}
& G_{\text{Total}}(X_{\text{C}}^{\text{fcc}}, X_{\text{Cr}}^{\text{fcc}}) = x_{\text{f}}^{\text{fcc}} \Delta G_{\text{mix}}^{\text{fcc}}(X_{\text{C}}^{\text{fcc}}, X_{\text{Cr}}^{\text{fcc}}) \\
& + x_{\text{f}}^{\text{M}_7\text{C}_3}(\Delta G_{\text{mix}}^{\text{M}_7\text{C}_3}(0.3, X_{\text{Cr}}^{\text{M}_7\text{C}_3}) + \Delta G_{\text{excess}}(r))
\end{aligned}
\tag{21}
$$

where \( x_{\text{f}}^{\text{fcc}} \) and \( x_{\text{f}}^{\text{M}_7\text{C}_3} \) are molar fraction of phases that are obtained from Eq. (19).

Fig. 6 shows the \( \Delta G_{\text{mix}} \) of two phase. A lever rule line (tieline) is also plotted from Gibbs energy surface of fcc phase to Gibbs energy curve of \( \text{M}_7\text{C}_3 \).

By developing these optimization code one is able to calculate effect of interface curvature and its additional energy on phase equilibria. \( \text{M}_7\text{C}_3 \) particles have pseudo-hexagonal structure containing 56 iron atoms and 24 carbon atoms in a unit cell with lattice parameters \( a = 1.3982 \, \text{nm} \) and \( c = 0.4506 \, \text{nm} \) [23]. Therefore, its molar volume is \( V_{\text{m}}^{\text{M}_7\text{C}_3} = 17.22 \times 10^{-6} \, \text{m}^3/\text{mol} \). There are various reports about surface energy of carbides in steels. Here, an average of \( 400 \, \text{mJ}/\text{m}^2 \) [24] is assumed.

Gibbs free energy of \( \text{M}_7\text{C}_3 \) with an interface radius of 10 nm will increase by 1337 J/mol. As shown in Fig. 6, the new \( \Delta G_{\text{mix}}^{\text{M}_7\text{C}_3} \) will alter the equilibrium and cause increase of solute concentration in austenite matrix. For example, in alloy Fe–10C–12Cr (at%) the \( (X_{\text{C}}^{\text{fcc}}, X_{\text{Cr}}^{\text{fcc}}) \) changes from (2.971, 2.884) at% to (3.850, 3.520) at% by decrease of precipitates radius to 10 nm.

![](./images/812056687568486401_11.jpg)

Fig. 8. Calculated phase boundary of austenite and austenite \( + \text{M}_7\text{C}_3 \) in different carbide interface curvature at \( 870 \, ^\circ\text{C} \). Tie lines of two-phase region at flat interface also plotted. Marked curves are equilibrium composition of austenite in different alloys. As it is shown each mark is rely on its specific boundary from \( r = \infty \) to 10 nm.

![](./images/812056687568486401_12.jpg)

Fig. 9. Two composition increase paths for two different Fe–C–Cr alloys at \( 870 \, ^\circ\text{C} \). Equilibrium between austenite and \( \text{M}_7\text{C}_3 \) is calculated. Increase of 2 at% Cr in alloy composition cause considerable increase in concentration difference between 10 nm curved interface and flat interface in austenite witch is the driving force for coarsening.

Obviously, at two phase region in three or more compound systems equilibrium concentration of phases vary with changing of alloy composition (degree of freedom rule). This makes Gibbs–Thomson effect in multicomponent alloys more complicated. In each alloy point, bevahior of increasing concentration is different.

If one repeat above calculations for different interface radius, dependency of matrix concentration on interfacial curvature could be found. This is generalization of Gibbs–Thomson effect in multicomponent alloys. Fig. 7 shows the ratio of concentration increase, \( X_{\text{i}}^{\text{fcc}}(r)/X_{\text{i}}^{\text{fcc}}(\infty) \), in three different alloys. In each alloy two phases are in equilibrium with specific composition and each of them has its own Gibbs–Thomson behavior.

As it is shown in Fig. 7, it is difficult to propose analytical model for multicomponent alloys that express all of these special increasing curves depending on system and equilibrium phases composition (Table 1).

By considering two-phase region in phase diagram, decrease of interface radius will change phase boundaries. Fig. 8 illustrates this phenomenon. For calculation of phase boundaries movement, one should find equilibrium composition of phases in different alloy point by optimization of Eq. (18) in each interface radius.

In Fig. 8 alloy composition changes from Fe–10C–5Cr to Fe–10C–21Cr (at%) and phase equilibria is calculated in different \( \text{M}_7\text{C}_3 \) interface radius from \( \infty \) to 10 nm. Concentration curves for different alloys shown in Fig. 7 are also plotted in their position.

By considering other neighbor phases like \( \text{Fe}_3\text{C} \), \( \text{M}_{23}\text{C}_6 \), … a new phase diagrams for small particle radius can be obtained.

Indeed, Gibbs-Thomson effect changes all phase boundaries and invariant points.

## 6. Gibbs-Thomson effect paths in composition space

This concept is interesting that in multicomponent systems, one can come up with the idea of defining a "path" for the concentration increase. The effect of one alloying element on the thermodynamic properties of other elements and surface of Gibbs free energy can alter the path that the concentration at curved interface changes through it. This effect is important in alloy design for high temperature applications that coarsening occurs. For example, in Fig. 9 "concentration increase paths" are plotted for two alloys. In Fe-10C-20Cr (at%), the rate of concentration increase is higher than Fe-10C-18Cr. This type of variation with the effect of multicomponent diffusion could be used to design more optimized alloy systems for coarsening resistant materials. That would be the aim of future works.

## 7. Summary and conclusion

The effect of internal pressure caused by interface curvature on equilibrium concentration (Gibbs-Thomson effect) was discussed here. Several formulations for dilute and concentrated alloys were compared with a computational thermodynamics model. Eqs. (7), (12) and (14) are identical and show better consistency with CALPHAD approach because it contains thermodynamic behavior of solution in both flat and curved interface concentration in form of activity coefficients ($\gamma_{\alpha}(X_{B}^{\alpha}(\infty))$, $\gamma_{\alpha}(X_{B}^{\alpha}(r))$) and variable Darken factor. However, others have only constant Darken factor in concentration of flat interface.

Computational thermodynamics model is the most general form and it does not use any assumption, which is necessary for derivation of other formulas like constant precipitate concentration and especial thermodynamics behavior for solutions. Calculation of phase equilibria in different interface radius in ternary alloys was used to demonstrate a Gibbs-Thomson effect in multicomponent alloys. Special behaviors such as moving of phase boundary and concentration increase path are also introduced in this work. For completely exact assessment of Gibbs-Thomson effect in solid state, better models can be developed that includes anisotropy of interface energy and variation of it by concentration change at interface. Coherency stress around precipitates also changes the matrix free energy. In addition, there is a dire need for experimental results for Gibbs-Thomson effect and better estimation of interface energies.

This accurate evaluation of Gibbs-Thomson effect especially in multicomponent alloys could lead to better results for coarsening and other microstructure evolution modes.

## Acknowledgements

S. Sh is grateful to M. Mirjalili for interesting and helpful discussions, especially for his inspiring ideas about melting point change in nanometer scale particles. Helpful suggestions and comments from reviewers are also acknowledged.

## References

[1] W. Thomson (Lord Kelvin), Phil. Mag. 42 (4) (1871) 448.
[2] J.W. Gibbs, Am. J. Sci. Ser. 3 (16) (1878) 441.
[3] W. Ostwald, Z. Phys. Chem. 34 (1900) 495.
[4] H. Freundlich, Colloid and Capillary Chemistry, Dutton, New York, 1923.
[5] J. Miyake, M.E. Fine, Acta Metall. Mater. 40 (1992) 733.
[6] B. Noble, S.E. Bray, Mater. Sci. Eng. A266 (1999) 80.
[7] W. Wu, G.H. Nancollas, J. Solution Chem. 27 (6) (1998).
[8] M. Hillert, in: H.I. Aaronson (Ed.), Lectures on the Theory of Phase Transformations, TMS-AIME, New York, NY, 1975, pp. 51-81.
[9] M. Qian, Metall. Mater. Trans. 33A (2002) 1283.
[10] M. Perez, Scripta Mater. 52 (2005) 709.
[11] M. Qian, L.C. Lim, Scripta Mater. 39 (10) (1998) 1451.
[12] R.K. Trivedi, in: H.I. Aaronson (Ed.), Lectures on the Theory of Phase Transformations, TMS-AIME, New York, NY, 1975, pp. 51-81.
[13] G.R. Purdy, Met. Sci. J. 5 (1971) 81-85.
[14] J.W. Martin, R.D. Doherty, Stability of Microstructure in Metallic Systems, Cambridge University Press, 1976.
[15] M. Qian, L.C. Lim, Metall. Mater. Trans. 31A (2000) 2659.
[16] J. Anderson, T. Helander, L. Hoglund, P. Shi, B. Sundman, Calphad 26 (2) (2002) 273-312.
[17] R.H. Davies, A.T. Dinsdale, J.A. Gisby, J.A. Robinson, M. Martin, Calphad 26 (2) (2002) 229-271.
[18] D. Gupta, K. Vieregge, W. Gust, Acta Mater. 47 (1) (1999) 5-12.
[19] A.T. Dinsdale, Calphad 15 (4) (1991) 317-425.
[20] D.R.F. West, N. Saunders, Ternary Phase Diagrams in Material Science, third ed., Maney Pub., 2002.
[21] A. Prince, Alloy Phase Equilibria, Elsevier Publishing Co., 1966.
[22] N. Saunders, A.P. Miodowink, CALPHAD (Calculation of Phase Diagrams): A Comprehensive Guide, Elsevier Science Ltd., 1998.
[23] D.V. Shtansky, K. Nakai, Y. Ohmori, Acta Mater. 47 (4) (1999) 1105-1115.
[24] G. Schneider, Inden, Acta Mater. 53 (2005) 519-531.