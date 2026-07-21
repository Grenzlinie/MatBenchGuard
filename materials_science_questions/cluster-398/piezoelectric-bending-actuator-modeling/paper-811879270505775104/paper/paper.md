# A Two-State Piezoelectric Model for Outer Hair Cell Motility

K. H. Iwasa
Biophysics Section, Laboratory of Cellular Biology, National Institute on Deafness and Other Communication Disorders, National
Institutes of Health, Bethesda, Maryland 20892 USA

ABSTRACT Recent studies have revealed that voltage-dependent length changes of the outer hair cell are based on charge
transfer across the membrane. Such a motility can be explained by an "area motor" model, which assumes two states in the
motor and that conformational transitions involve transfer of motor charge across the membrane and mechanical displace-
ments of the membrane. Here it is shown that the area motor is piezoelectric and that the hair cell that incorporates such a
motor in its lateral membrane is also piezoelectric. Distinctive features of the outer hair cell are its exceptionally large
piezoelectric coefficient, which exceeds the best known piezoelectric material by four orders of magnitude, and its prominent
nonlinearity due to the discreteness of motor states.

## INTRODUCTION

The outer hair cell is one of the mechanosensory cells in the
cochlea and is indispensable for fine tuning of the ear
(Mountain, 1980; Liberman and Dodds, 1984). Besides
sensory hairs, this cell has a cell body with a motility
(Brownell et al., 1985; Ashmore, 1987) fast enough to
follow changes in the membrane potential at auditory fre-
quencies (Dallos and Evans, 1995; Frank et al., 1999).
Having transduction mechanisms in both directions makes
the cell a key element in the feedback loop in the cochlea
that enhances the frequency selectivity and broadens the
dynamic range of the ear.

Recent studies have revealed that the motility of this cell
is based on a membrane motor that directly uses electrical
energy (Ashmore, 1989; Iwasa, 1993; Dallos et al., 1993).
This membrane motor has two or more conformations that
differ in mechanical and electrical states (Iwasa, 1994).
Each of these conformational differences is a familiar fea-
ture of membrane transport proteins: Charge transferable
across the membrane during conformational changes is sim-
ilar to gating charges of ion channels (Armstrong and Beza-
nilla, 1973; Heinemann et al., 1992). Differences in the
membrane area in these states are similar to those in mech-
anosensory channels (Sukharev et al., 1999).

Because the conformations have differences in both prop-
erties, conformational transitions accompany charge trans-
fer across the membrane and mechanical displacement of
the membrane. Thus, electrical and mechanical changes are
coupled, analogous to piezoelectricity. Indeed, attempts
have been made to describe the lateral membrane of the
outer hair cell as a piezoelectric material (Mountain and
Hubbard, 1994; Tolomeo and Steele, 1995). However, these
reports assumed that piezoelectric response was primarily
linear to the electric field, whereas the response of the cell
saturates with respect to the membrane potential. In addi-
tion, the cellular structure was not adequately addressed.

The present paper addresses the question of how outer
hair cell motility compares with piezoelectricity. It also
attempts to clarify how phenomenological parameters that
describe the properties of the cell as a whole are related to
more microscopic variables that characterize the motor and
the cell membrane.

In the first part of the paper, analytical relationships
between microscopic and macroscopic quantities are de-
rived. That is followed by an attempt to determine micro-
scopic parameters by sorting out existing experimental data.
Then these microscopic parameters are used to obtain mac-
roscopic parameters, which are then compared with exper-
imental values. The last step serves as a consistency test.

The present treatment differs from earlier versions of an
"area motor" model (Iwasa, 1994; Iwasa and Adachi, 1997)
in providing analytical relationships between the micro-
scopic and macroscopic quantities and thereby clarifying
the piezoelectric nature of the motor.

## PIEZOELECTRICITY

Before describing the hair cell system, let us review a
standard description of piezoelectricity. In a piezoelectric
material, a mechanical displacement and an electric dis-
placement are coupled. Such a property can be described by
a coupling term in the free energy. In a simple one-dimen-
sional case, the free energy $G$ of a piezoelectric material can
be given by (Ikeda, 1990)

$$
G(E, F)=G(0,0)+\frac{1}{2} c_{11} E^{2}+c_{12} E F+\frac{1}{2} c_{22} F^{2}, \tag{1}
$$

where $E$ is the electric field and $F$ the force applied. The
state $E=F=0$ represents equilibrium. The first term is the
electrical energy and the last term is the mechanical energy.
The middle term represents the coupling energy.

The stress-strain relationships are obtained by taking
partial derivatives of Eq. 1. Electrical displacement $Q$ and

---
Received for publication 18 January 2001 and in final form 2 August 2001.
Address reprint requests to Kuni H. Iwasa, National Institutes of Health,
Biophysics Section, Bldg 50, Rm 4152, 50 South Drive, MSC-8027,
Bethesda, MD 20892-8027. Tel.: 301-496-3987; Fax: 301-480-0827; E-
mail: iwasa@nih.gov.
© 2001 by the Biophysical Society
0006-3495/01/11/2495/12 $2.00

mechanical displacement $L$ are then represented, respectively, by

$$
Q = \frac{\partial G}{\partial E} = c_{11}E + c_{12}F,
$$

$$
L = \frac{\partial G}{\partial F} = c_{12}E + c_{22}F.
$$

The coupling terms in those two equations use the same coefficient $c_{12}$ because they originate from the same free energy term. This symmetry in the coupling coefficients is the reciprocal relationship, characteristic of piezoelectricity. It distinguishes piezoelectricity from other kinds of electromechanical coupling such as electrostriction and electrokinetic effect.

This system is conveniently characterized by the piezoelectric coefficient $c_{12}$, which gives the magnitude of mechanoelectric coupling, and the coupling coefficient $k$ (Ikeda, 1990), which describes the fraction of energy that is converted from one form to another,

$$
k^{2} = \frac{c_{12}^{2}}{c_{11}c_{22}}, \tag{2}
$$

and cannot exceed unity. The piezoelectric coefficient $c_{12}$ of typical piezoelectric substance such as quartz or Rochelle salt is constant in a relatively wide range of electric field $E$ (Ikeda, 1990).

## TWO-STATE MEMBRANE MOTOR

To describe the hair cell system, let us start by examining unit properties of a membrane motor. Because a membrane motor cannot exist on its own and needs to be incorporated into a membrane to function, unit properties practically means the properties of a single motor unit incorporated into an infinitely large isotropic membrane. Under this condition, conformational transitions of the motor do not affect the motor's environment.

The membrane motor in the outer hair cell has been described by a two-state model. In its simplest form, two states of a motor unit differ in their charge by $\Delta q$ and their cross-sectional area in the membrane (area motor model) by $\Delta a$. They are subjected to isotropic membrane tension $T_{\text{m}}$ (Fig. 1),

$$
\begin{aligned}
\Delta G_{\text{i}} &= G_{1} - G_{\text{s}} \\
&= \Delta G_{0} - \Delta q \cdot V_{\text{m}} - \Delta a \cdot T_{\text{m}}. \tag{3}
\end{aligned}
$$

Here, $G_{1}$ is the free energy of the state with larger membrane area (extended state) and $G_{\text{s}}$ is that of smaller membrane area (compact state). $\Delta G_{0}$ is a constant and the membrane potential is $V_{\text{m}}$. The probability of the extended state $P_{\ell}$ is expressed by

$$
P_{\ell} = \frac{\exp[-\beta \Delta G_{\text{i}}]}{1 + \exp[-\beta \Delta G_{\text{i}}]}. \tag{4}
$$

![](./images/811879270505775104_1.jpg)

FIGURE 1 A two-state membrane motor and its displacements. (A) Cross sections of the motor in the two states. Transitions between the states are accompanied by transfer of charge $\Delta q$ across the plasma membrane and mechanical displacements. (B) A schematic illustration of the motor's area changes. $\Delta a_{z}$ and $\Delta a_{\text{c}}$ are area changes in the axial $(z)$ direction and the circumferential $(c)$ direction, respectively. The rectangular shape of the motor in the illustration is for simpler illustration and does not constitute an assumption.

Here, $\beta = 1/(k_{\text{B}}T)$, where $k_{\text{B}}$ is the Boltzmann constant and $T$ is the temperature.

For describing a membrane system, the membrane potential $V_{\text{m}}$ substitutes for the electric field $E$ because membrane thickness is implicitly assumed constant. The average charge $Q$ and the average area $A$ of the motor may then be represented by,

$$
Q = \Delta q \cdot P_{\ell} + Q_{\text{s}},\quad A = \Delta a \cdot P_{\ell} + A_{\text{s}},
$$

where the subscript $s$ indicates those quantities that correspond to the compact state.

Due to their $P_{\ell}$-dependent terms, both $Q$ and $A$ are nonlinear with respect to the membrane potential $V_{\text{m}}$ and to tension $T_{\text{m}}$. Here, changes in response to small increments in these variables are examined. Increments $\delta Q$ and $\delta A$ that correspond to an increment $\delta V_{\text{m}}$ in the membrane potential and an increment $\delta T_{\text{m}}$ in membrane tension are

$$
\delta Q = a_{11}\delta V_{\text{m}} + a_{12}\delta T_{\text{m}} + C_{0}\delta V_{\text{m}}, \tag{5}
$$

$$
\delta A = a_{21}\delta V_{\text{m}} + a_{22}\delta T_{\text{m}} + \kappa \delta T_{\text{m}}, \tag{6}
$$

with

$$
a_{11} = \beta \Delta q^{2}P_{\ell}(1 - P_{\ell}), \tag{7}
$$

$$
a_{12} = a_{21} = \beta \Delta a \Delta q P_{\ell}(1 - P_{\ell}), \tag{8}
$$

$$
a_{22} = \beta \Delta a^{2}P_{\ell}(1 - P_{\ell}). \tag{9}
$$

$C_0$ and $\kappa$ are, respectively, the membrane capacitance and the area compliance of the compact state. For the sake of simplicity, we have assumed that the area compliance is the same in the two states, although the two states may differ in their stiffness. This simplifying assumption is justified at least as an approximation because an experimental exami- nation showed that the effect of different stiffness in the two sates is insignificant for membrane motility (Adachi et al., 2000).

The terms $a_{12}$ and $a_{21}$ represent coupling. Because charge transfer and area changes of the motor are coupled, changes in the membrane potential that induce charge movement result in area changes. Reciprocally, changes in tension result in charge movement. The reciprocal relationship $a_{12}=a_{21}$ indicates that the coupling is piezoelectric.

The membrane capacitance of the motor consists of the regular (or linear) membrane capacitance $C_0$ and a nonlinear membrane capacitance $a_{11}$, which has a bell-shaped mem- brane potential dependence. Likewise, the area compliance of the motor consists of two parts, the structural area com- pliance $\kappa$, which is voltage independent, and an area com- pliance $a_{22}$, which has also a bell-shaped membrane poten- tial dependence. These voltage-dependent terms are due to the voltage and tension sensitivity of the motor.

The coupling coefficient $k$ of the motor is then given by

$$
k^{2}=\frac{a_{12}^{2}}{\left(a_{11}+C_{0}\right)\left(a_{22}+\kappa\right)}. \tag{10}
$$

The value for the coupling coefficient $k$ increases up to unity as the relative significance of the linear capacitance $C_0$ and that of the area compliance $\kappa$ decrease. The coefficient $k$ also depends on the value of the membrane potential and tension through $P_\ell$. The coupling coefficient has a maxi- mum at $P_\ell = 0.5$, where the nonlinear capacitance peaks. Numerical values for the coefficients are examined later.

As will be shown below, the actual motor is in a mem- brane with anisotropic tension. In such a system, the term $\Delta a \cdot T_{\mathrm{m}}$ is replaced by the scalar product of the displacement vector and the stress vector.

## MEMBRANE MOTOR IN A CYLINDRICAL CELL

Now we incorporate the membrane motor into a cylindrical cell at a finite concentration. To make the description of such a composite system simple, a number of assumptions has been made (Iwasa, 1994; Iwasa and Adachi, 1997). They are: 1) end effects can be ignored, 2) the total strains are sums of elastic strains and motor strains, 3) the elastic property of the motor is the same as the rest of the lateral membrane, and 4) the volume of the cell is kept constant.

### Basic equations

In the following, the theory is briefly described using con- stitutive equations. The elastic tension is balanced with tension due to pressure $P$ and tension due to an external axial force $F_z$. Due to the cylindrical geometry of the cell, the constitutive equations for the lateral membrane are given for tension in the axial direction $z$ and the circumfer-ential direction $c$:

$$
d_{1} \epsilon_{z}^{\prime}+c \epsilon_{\mathrm{c}}^{\prime}=T_{z}=\frac{1}{2} R P+\frac{F_{z}}{2 \pi R}, \tag{11}
$$

$$
c \epsilon_{z}^{\prime}+d_{2} \epsilon_{\mathrm{c}}^{\prime}=T_{\mathrm{c}}=R P. \tag{12}
$$

Here, $R$ is the radius of the cylinder and $d_1$, $d_2$, and $c$ are elastic moduli. It is assumed that the elastic strains $\epsilon_z'$ and $\epsilon_{\mathrm{c}}'$ are small. These equations assume that end effects can be ignored. In addition, it should be noticed that the tension is not isotropic. Not only does the effect of external axial force result in anisotropy, but the effect of pressure is anisotropic as well.

The total strains $(\epsilon_z, \epsilon_{\mathrm{c}})$ and the elastic strains $(\epsilon_z', \epsilon_{\mathrm{c}}')$ are related by assumptions 2 and 3. Thus,

$$
\epsilon_{z}=\epsilon_{z}^{\prime}+n \Delta a_{z} P_{\ell}, \tag{13}
$$

$$
\epsilon_{\mathrm{c}}=\epsilon_{\mathrm{c}}^{\prime}+n \Delta a_{\mathrm{c}} P_{\ell}, \tag{14}
$$

where the second terms on the right-hand side represent motor displacements, with $n$ the number density of the motor in the lateral membrane, $\Delta a_z$ and $\Delta a_{\mathrm{c}}$ the component of the area difference between the two states (Fig. 1), and $P_\ell$ the fraction of the state with larger membrane area. The mechanical part of the free energy difference is understood as the scalar product of the tension vector and displacement vector. If the stiffness of the motor is different from the rest of the cell, additional terms that depend on the membrane fraction of the motor must appear in the above equations.

The fraction $P_\ell$ is represented by

$$
P_{\ell}=\frac{\exp \left[-\beta \Delta G_{\mathrm{c}}\right]}{1+\exp \left[-\beta \Delta G_{\mathrm{c}}\right]}, \tag{15}
$$

where $\beta=1/(k_{\mathrm{B}}T)$ with Boltzmann's constant $k_{\mathrm{B}}$ and the temperature $T$. The free energy difference $\Delta G_{\mathrm{c}}$ in the two motor states depends on the membrane potential and mem- brane tension and is given by

$$
\Delta G_{\mathrm{c}}=\Delta G_{0}-\Delta q \cdot V_{\mathrm{m}}-\Delta a_{z} \cdot T_{z}-\Delta a_{\mathrm{c}} \cdot T_{\mathrm{c}}. \tag{16}
$$

Because membrane tension is anisotropic, the free energy difference is more complicated than in the isotropic case (i.e., Eq. 3).

So far, the number of equations is two because $P_\ell$ is determined by Eqs. 15 and 16 and goes into Eqs. 13 and 14. Eqs. 13 and 14 are used to eliminate $\epsilon_z'$ and $\epsilon_{\mathrm{c}}'$ in Eqs. 11 and 12. Those equations are, for example, to be solved for a given membrane potential $V_{\mathrm{m}}$ and external axial force $F_z$. Then the undetermined variables are three: the axial strain $\epsilon_z$, the circumferential strain $\epsilon_{\mathrm{c}}$, and pressure $P$.

The additional condition is the constant volume condition (assumption 4), which can be expressed by

$$
\epsilon_{\mathrm{z}}+2 \epsilon_{\mathrm{c}}=\epsilon_{\mathrm{v} 0}. \tag{17}
$$

Because we assume that the strains are small, the volume strain is expressed by $\epsilon_{\mathrm{z}}+2 \epsilon_{\mathrm{c}}$. The value $\epsilon_{\mathrm{v} 0}$ is due to static internal pressure of the cell at the resting membrane potential. With the constant volume condition, the number of independent variables is two, because $\epsilon_{\mathrm{c}}$ is expressed by $\epsilon_{\mathrm{z}}$.

## Effect of voltage and axial force

Now, let us describe the system for a set of values for $V_{\mathrm{m}}$ and $F_{\mathrm{z}}$. An effect of the motor incorporated into the cell membrane is that the motor, which changes tension, is reciprocally affected by tension, creating a self-consistency condition. It turns out that the problem is how to determine the motor variable $P_{\ell}$.

With Eqs. 11-14 and 17, it is possible to eliminate $R P$ and $\epsilon_{\mathrm{c}}$ to express $\epsilon_{\mathrm{z}}$ as a function of $P_{\ell}$,

$$
\epsilon_{\mathrm{z}}=\frac{2 g F_{\mathrm{z}}}{\pi R}+b_{0}+b_{1} n P_{\ell}, \tag{18}
$$

with density of motor $n$ and constants,

$$
\begin{gathered}
b_{0}=g \epsilon_{\mathrm{v} 0}\left(2 c-d_{2}\right), \\
b_{1}=2 g\left[\Delta a_{\mathrm{z}}\left(2 d_{1}-c\right)+\Delta a_{\mathrm{c}}\left(2 c-d_{2}\right)\right], \tag{19} \\
g=\frac{1}{4 d_{1}-4 c+d_{2}}. \tag{20}
\end{gathered}
$$

The axial strain $\epsilon_{\mathrm{z}}$ depends on the membrane potential $V_{\mathrm{m}}$ through $P_{\ell}$, which describes the motor state. The load-free amplitude is determined by $b_{1} n$ because the motor state variable $P_{\ell}$ changes between 0 and 1 . The cell strain $\epsilon_{\mathrm{z}}$ and the axial compliance of the cell depends on the first term and the last term of Eq. 18, because the motor state $P_{\ell}$ depends on axial force $F_{\mathrm{z}}$.

The motor variable $P_{\ell}$ is determined by the free energy difference $\Delta G_{\mathrm{c}}$ with Eq. 15, and the free energy difference is, in turn, given by Eq. 16. With Eqs. 12-14 and 17, circumferential tension $T_{\mathrm{c}}$ is expressed by $\epsilon_{\mathrm{z}}$ and $P_{\ell}$. Axial tension $T_{\mathrm{z}}$ is a sum of $T_{\mathrm{c}} / 2$ and externally applied axial tension (see Eqs. 11 and 12). These substitutions give rise to

$$
\Delta G_{\mathrm{c}}=-\Delta q V_{\mathrm{m}}-b_{1} F_{\mathrm{z}}+\left(b_{2} / \beta\right) P_{\ell}+b_{3}, \tag{21}
$$

with

$$
b_{2}=\beta g n\left(d_{1} d_{2}-c^{2}\right)\left(\Delta a_{\mathrm{z}}+2 \Delta a_{\mathrm{c}}\right)^{2}. \tag{22}
$$

Here, $g$ is defined by Eq. 20, and $b_{3}$ is a constant that involves $\Delta G_{0}$ and $\epsilon_{\mathrm{v} 0}$. The factor $b_{2}$ determines the effect of the motor on itself because the presence of the term $b_{2} P_{\ell}$ imposes a self-consistency condition.

![](./images/811879270505775104_2.jpg)

FIGURE 2 Effect of $b_{2}$ on the membrane potential dependence of $P_{\ell}$ and its derivative. $(A)$ Voltage dependence of $P_{\ell}$ and its voltage derivative. The motor variable $P_{\ell}$ is determined by Eq. 23 with $F_{\mathrm{z}}=0$. The voltage derivative is $\alpha \beta \Delta q P_{\ell}(1-P_{\ell})$, where $\alpha$ is defined by Eq. 29. Solid lines, $b_{2}=0.9$; broken lines, $b_{2}=0$. The condition $b_{2}=0$ leads to the two-state Boltzmann function for $P_{\ell}$. The two values for $b_{2}$ are intended to show the extremes. A realistic value for $b_{2}$ is $\sim 0.3$. $\Delta q=$ 0.9 e. The scale of $P_{\ell}$ is on the left and the scale of $\mathrm{d} P_{\ell} / \mathrm{d} V$ is on the right. The unit of $\mathrm{d} P_{\ell} / \mathrm{d} V$ is $\mathrm{V}^{-1}$. $(B)$ Comparison of voltage dependences of $\alpha \beta P_{\ell}(1-P_{\ell})$ for $b_{2}=0.9$ and $b_{2}=0$. Peak heights are normalized. Solid line, $b_{2}=0.9, \Delta q=0.9$ e; broken line, $b_{2}=0, \Delta q=$ 0.74 e, and translated along the axis of abscissas. These comparisons show that $P_{\ell}$, which is determined by Eq. 23, can be approximated a two-state Boltzmann function, provided that the charge $\Delta q$ is adequately adjusted.

By substituting $\Delta G_{\mathrm{c}}$ in Eq. 15 with Eq. 21, an equation for $P_{\ell}$ is obtained:

$$
\beta \Delta q V_{\mathrm{m}}+\beta b_{1} F_{\mathrm{z}}=b_{2} P_{\ell}-\ln \left(\frac{1}{P_{\ell}}-1\right)+b_{3}. \quad(23)
$$

With this equation, $P_{\ell}$ is obtained for a given set of the membrane potential $V_{\mathrm{m}}$ and axial force $F_{\mathrm{z}}$. The equation shows that $P_{\ell}$ can be treated as an inverse function of $V_{\mathrm{m}}$ or of $F_{\mathrm{z}}$. For example, for a fixed value of the axial force $F_{\mathrm{z}}$, the membrane potential $V_{\mathrm{m}}$ and the motor state $P_{\ell}$ correspond one-to-one, and $V_{\mathrm{m}}$ is readily determined for a given value of $P_{\ell}$. If we impose a condition $b_{2}=0$, which excludes the effect of the motor on itself, Eq. 23 turns into a Boltzmann function that expresses $P_{\ell}$. The voltage dependence of $P_{\ell}$ is illustrated in Fig. 2.

### Response to small changes in $V_{\mathrm{m}}$ and $F_{\mathrm{z}}$

Now let us consider the effect of small changes in the membrane potential and axial force on membrane charge and the cell length. An increment $\delta Q$ in charge and an increment $\delta L$ in the length of the cell due to $\delta V_{\mathrm{m}}$ and $\delta F_{\mathrm{z}}$ can be represented by

$$
\delta Q=N q \delta P_{\ell}+C_{\mathrm{lin}} \delta V_{\mathrm{m}},
$$

$$
\begin{aligned}
\delta L & =L \delta \epsilon_{z} \\
& =\frac{2 g L}{\pi R} \delta F_{z}+b_{1} n L \delta P_{\ell}.
\end{aligned}
$$

Here, the first term in $\delta Q$ is the voltage derivative of motor charge $N q P_{\ell}$. The second term is due to the regular (or linear) membrane capacitance $C_{\text {lin }}$ of the cell. The equation for $\delta L$ is derived from Eq. 18.

An increment in $P_{\ell}$ due to small changes in the membrane potential and axial force can be obtained by using Eq. 23. The substitution of the resulting expression for $\delta P_{\ell}$ in the above equations leads to

$$
\delta Q=c_{11} \delta V_{\mathrm{m}}+c_{12} \delta F_{\mathrm{z}},\qquad(24)
$$

$$
\delta L=c_{21} \delta V_{\mathrm{m}}+c_{22} \delta F_{\mathrm{z}},\qquad(25)
$$

where $\delta Q$ is an increment of charge, $\delta L$ is an increment of the axial length of the cell, and $F_{z}$ is axial force applied to the cell.

The coefficients are given by

$$
c_{11}=\alpha \beta N \Delta q^{2} P_{\ell}\left(1-P_{\ell}\right)+C_{\text {lin }},\qquad(26)
$$

$$
c_{12}=c_{21}=\alpha \beta n L \Delta q b_{1} P_{\ell}\left(1-P_{\ell}\right),\qquad(27)
$$

$$
c_{22}=\frac{L}{2 \pi R}\left[4 g+\alpha \beta n b_{1}^{2} P_{\ell}\left(1-P_{\ell}\right)\right],\qquad(28)
$$

where $g, b_{1}$, and $b_{2}$ are defined by Eqs. 20-22. The factor $\alpha$ is

$$
\alpha=\frac{1}{1+b_{2} P_{\ell}\left(1-P_{\ell}\right)}.\qquad(29)
$$

The reciprocal relationship $c_{12}=c_{21}$ is automatically satisfied. Of the coefficients, $c_{11}$ is the membrane capacitance and $c_{22}$ is the axial compliance. The coefficient $c_{11}$ includes the linear capacitance $C_{\text {lin }}$ and the contribution of motor charge to the capacitance. The coefficient $c_{22}$ likewise includes both the passive compliance, which is $2 g \leq /(\pi R)$, and the contribution of the motor to the compliance. The coupling coefficient $k$ is given by

$$
k^{2}=\frac{c_{12}^{2}}{c_{11} c_{22}}.\qquad(30)
$$

Eqs. 26-28 show that the coefficients $c_{11}, c_{12}(=c_{21})$, and $c_{22}$ consist of constants and terms that are proportional to $\alpha P_{\ell}(1-P_{\ell})$. That means that these coefficients have similar membrane potential dependences if their constant terms are excluded. Ratios of these coefficients, such as $c_{12}/c_{22}$ and $k$, however, do not have the same voltage dependences, although they share the peak potential and appear similar (Fig. 3).

### Effect of motor on itself

The factor $\alpha$ that is given by Eq. 29 does not appear in coefficients $a_{11}, a_{12}$, and $a_{22}$ of an isolated motor. This factor arises from a self-consistency condition when the motor is incorporated into a cell.

The partial derivative of Eq. 23 with respect to $V_{\mathrm{m}}$ gives rise to

$$
\frac{\partial P_{\ell}}{\partial V_{\mathrm{m}}}=\alpha \beta \Delta q P_{\ell}\left(1-P_{\ell}\right),
$$

which contains the factor $\alpha$. The departure of this factor from unity indicates the effect of the motor on itself. It is a result of the motor being incorporated into a cell.

This effect is essentially negative cooperativity. Depolar- ization decreases $P_{\ell}$ and decreases membrane area, resulting in increased pressure, which in turn increases membrane tension. An increase in membrane tension favors the ex- tended state. These interactions thus reduce the motor's sensitivity to the membrane potential. The effect of this factor is illustrated in Fig. 2. The self-consistency condition reduces the sharpness of the motor's dependence on $V_{\mathrm{m}}$ and $F_{\mathrm{z}}$, while it keeps the normalized dependence of $P_{\ell}$ on $V_{\mathrm{m}}$ or on $F_{\mathrm{z}}$ relatively unchanged. The partial derivative of $P_{\ell}$ with respect to $F_{\mathrm{z}}$ likewise yields the factor $\alpha$.

## EXAMINATION OF EXPERIMENTAL DATA

To test the validity of the model, experimental data are briefly examined here. First, the values for the parameters are determined from the their directly relevant experiments. Second, the quantities that characterize piezoelectricity are estimated for the membrane motor and for the cell as a whole. Third, the predicted cellular coefficients are compared with experimental data, which are not used for determining the parameters.

### Determination of parameters

#### Elasticity

The elastic moduli $d_{1}, d_{2}$, and $c$ can be determined by the stress-strain relationships obtained during the application of pressure (Iwasa and Chadwick, 1992) and axial force (Iwasa and Adachi, 1997). A typical set of values is $d_{1}=0.046$, $d_{2}=0.068$, and $c=0.046$ N/m (Iwasa and Adachi, 1997). Although reports on stress-strain relationship during pressure application are consistent (Iwasa and Chadwick, 1992;

![](./images/811879270505775104_3.jpg)

FIGURE 3 The membrane potential dependence of coefficients $c_{11}$, $c_{12}$, and $c_{22}$. The functional forms of these coefficients are given by Eqs. 26-28 and 30. The values for the parameters are given in Table 1 and Table 2. (4) The membrane capacitance $c_{11}$ (solid line) and the axial stiffness $c_{22}$ (broken line). The plots are normalized. The peak value of $c_{11}$ is $3.7 \times$ $10^{-11} \mathrm{C}$ and the peak value of $c_{22}$ is $118 \mathrm{~m} / \mathrm{N}$. (B) $c_{12}$ and $c_{12} / c_{22}$. The plots are normalized. The peak value for $c_{12}$ is $2.0 \times 10^{-5} \mathrm{~m} / \mathrm{V}$ (or equivalently $\mathrm{C} / \mathrm{N}$ ). The peak value for $c_{12} / c_{22}$ is $1.7 \times 10^{-7} \mathrm{~N} / \mathrm{V}$. (C) The coupling coefficient $k$.

Adachi et al., 2000), reports on the axial stiffness vary in a range between 40 and 750 nN per unit strain (Holley and Ashmore, 1988; Hallworth, 1995; Iwasa and Adachi, 1997; Frank et al., 1999; He and Dallos, 2000). The value for the elastic moduli used here corresponds to 500 nN per unit strain, or $1 \times 10^{2} \mathrm{~m} / \mathrm{N}$ for a $50-\mu \mathrm{m}$-long hair cell, which is close to values found in three recent reports (Iwasa and Adachi, 1997; Frank et al., 1999; He and Dallos, 2000).

## Motor parameters

The motor parameters can be determined primarily based on membrane capacitance measurements. Shifts of voltage depen- dence of the membrane capacitance provide a condition that $\Delta a_{\mathrm{z}}+2 \Delta a_{\mathrm{c}}$ is about $2 \mathrm{~nm}^{2}$ (Iwasa, 1994; Adachi et al., 2000). This value is consistent with Kakehata and Santos-Sacchi (1995) and is larger than Gale and Ashmore's (1994) estimate of $\sim 0.4 \mathrm{~nm}^{2}$. Because the effect of stretching the membrane is not considered in obtaining these values, it is possible that these values could be underestimates (Iwasa, 1993). Rounded hair cells after trypsin treatment have isotropic tension and give a value $4 \mathrm{~nm}^{2}$ for $\Delta a_{\mathrm{z}}+\Delta a_{\mathrm{c}}$ (Adachi and Iwasa, 1999). Detached patches of the lateral membrane should also have isotropic tension. An estimate of $2.4 \mathrm{~nm}^{2}$ is reported from the pressure sensitivity of the membrane capacitance of detached patches (Gale and Ashmore, 1997). Some caution may be needed to interpret these values. Although the motor is insen- sitive to trypsin treatment, trypsin treatment might change the properties of the motor. The estimate based on detached patch involves uncertainty in determining the curvature of the mem- brane patch. I choose a set $\Delta a_{\mathrm{z}}=4.5 \mathrm{~nm}^{2}, \Delta a_{\mathrm{c}}=-0.75 \mathrm{~nm}^{2}$ that corresponds to $\Delta a_{\mathrm{z}}+2 \Delta a_{\mathrm{c}}=3 \mathrm{~nm}^{2}$ and $\Delta a_{\mathrm{z}}+\Delta a_{\mathrm{c}}=$ $3.75 \mathrm{~nm}^{2}$.

The charge $\Delta q$ and the density $n$ of the motor can be determined by two methods. One method uses the mem- brane capacitance of sealed patches formed on the lateral wall of the cell. The other method uses the membrane capacitance of the whole cell. The values obtained from sealed membrane patches for the charge $\Delta q$ are 0.99 e (Gale and Ashmore, 1997) and $\sim 0.8$ e (Dong and Iwasa, 2001). The density $n$ estimated was $8.4 \times 10^{3} \mu \mathrm{m}^{-2}$ (Gale and Ashmore, 1997).

The charge and the number of the motor units in the whole cell have been determined by fitting the voltage dependence of the membrane capacitance, using the equation,

$$
\begin{aligned}
C\left(V_{\mathrm{m}}\right)= & \beta \tilde{N} \Delta \tilde{q}^{2} \frac{\exp \left[-\beta \Delta \tilde{q}\left(V_{\mathrm{m}}-V_{0}\right)\right]}{\left(1+\exp \left[-\beta \Delta \tilde{q}\left(V_{\mathrm{m}}-V_{0}\right)\right]\right)^{2}} \\
& +C_{\text {lin }}, \quad (31)
\end{aligned}
$$

where $V_{0}$ is the voltage that maximizes the capacitance, and $C_{\text {lin }}$ is the linear capacitance of the cell. Although Eq. 31 should be equivalent to $c_{11}$, it does not have the factor $\alpha$. Thus it is based on an assumption that the motor behaves as if it is isolated. Nonetheless it should fit experimental data reasonably well as shown in Fig. 2. Thus, Eq. 31 is a phenomenological equation and the quantities marked with $\sim$, such as $\Delta \tilde{q}$ and $\tilde{N}$, which are obtained by fitting with this equation, are apparent ones.

![](./images/811879270505775104_4.jpg)

FIGURE 4 The relationship between $b_2$ and $\tilde{b}_2$ (solid line). Deviations from the broken line indicate the importance of the correction indicated by Eq. A1.

The reported values for $\Delta \tilde{q}$ range from 0.7 to 1.0 e (Ashmore, 1990; Santos-Sacchi, 1991; Iwasa, 1993; Kake- hata and Santos-Sacchi, 1995; Tunstall et al., 1995; Adachi et al., 2000). The number $\tilde{N}$ of the motor increases with the cell length. It is thus more conveniently described by the density $\tilde{n}$, which ranges from $7.5 \times 10^3$ to $10 \times 10^3$ $\mu$m$^{-2}$ (Huang and Santos-Sacchi, 1993; Tunstall et al., 1995; Santos-Sacchi et al., 1998; Adachi et al., 2000).

Errors by using an approximate Eq. 31 can be obtained with Eq. A1 in the Appendix. If $\tilde{n} = 9 \times 10^3$ $\mu$m$^{-2}$, the parameter values that we have chosen leads to $\tilde{b}_2 = 0.29$. Eq. A1, in turn, yields $b_2 = 0.27$. That means $\Delta q$ is about 7% larger than $\Delta \tilde{q}$ and $n$ is about 7% lower than $\tilde{n}$ (Fig. 4). Those differences are not very large, but they are still appreciable. I choose 0.9 e for the motor charge $q$ and $9 \times$ $10^3$ $\mu$m$^{-2}$ for the motor density $n$ in the numerical evalu- ation. The experimental and adopted values for the motor parameters are summarized in Table 1.

## Piezoelectric and coupling coefficients

In the following, to examine how efficiently the cell uses the motor elements in its membrane, the coefficients for the motor in isolation and those for the motor in the cell are compared numerically.

### Isolated motor

First, the coupling coefficient of the isolated motor is ex- amined using the values for parameters that was described earlier. $\Delta q = 0.9$ e, where e is the electronic charge, and $\Delta a = 3.75$ nm$^2$. The maximum mechanoelectric coupling coefficient is at $P_\ell = 0.5$. The maximum value for the piezoelectric coefficient $a_{12}$ is $3.3 \times 10^{-17}$ Cm/N. If the characteristic length of the isolated motor is 10 nm, this value corresponds to $3.3 \times 10^{-5}$ C/N.

To determine the coupling coefficient, the membrane capacitance and the area compliance of the motor are re- quired. The membrane capacitance of the motor states can be estimated by assuming that the membrane area of the motor is approximated by a circle 10 nm in diameter and the specific capacitance of $0.8$ $\mu$Fcm$^{-2}$. The model assumes that the elastic moduli of the motor are the same in the two states and are the same as the rest of the lateral membrane. It is easily shown that the area compliance of a motor state responding to isotropic tension is given by $A_\text{s}(d_1 + d_2 - 2c)/(d_1d_2 - c^2)$ with $A_\text{s}$ representing the area of the motor. These assumptions lead to 0.40 for the coupling coefficient $k$ for the chosen set of parameters.

There are two possible sources of error in the coupling coefficient $k$ due to these assumptions. First, although the distribution and the density of 10-nm particles in the lateral membrane of the outer hair cell roughly agree with the distri- bution and the density of the motor, the number density of the motor could be twice as large as 10-nm particles. That means the area of the motor could be overestimated by a factor 2. Second, the specific capacitance of $\sim$0.8 $\mu$Fcm$^{-2}$ is for lipid bilayers and membrane proteins, which tend to be thicker than lipid bilayers and could have lower values for the specific capacitance. If the regular membrane capacitance of the motor is reduced two-fold, $k = 0.43$ is obtained.

### Cell as a whole

The coefficients given by Eqs. 26-28 depend on the size of the cell, because the charge transfer $\delta Q$ and length change $\delta L$ given by Eqs. 24 and 25 are extensive quantities. Values for the coefficients for a cell with length $L$ of 50 $\mu$m at $P_\ell =$ 0.5, which maximizes $P_\ell(1 - P_\ell)$. The radius $R$ of the cell is assumed to be 5 $\mu$m.

The coefficients are voltage dependent (Fig. 3) and their maximum values are,

$$c_{11}(\text{max}) - C_{\text{lin}} \approx 1.7 \times 10^{-11}\ \text{(C)},$$

$$c_{12}(\text{max}) \approx 2.0 \times 10^{-5}\ \text{(m/V or C/N)},$$

$$c_{22}(\text{max}) \approx 118\ \text{(m/N)}.$$

<table>
<caption>TABLE 1 Motor parameters</caption>
<thead>
<tr>
<th></th>
<th>Unit</th>
<th>Measured</th>
<th>Used</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Delta a_z + 2\Delta a_c$</td>
<td>nm$^2$</td>
<td>2,$^\text{a}$ 0.4$^\text{b}$</td>
<td>3</td>
</tr>
<tr>
<td>$\Delta a_z + \Delta a_c$</td>
<td>nm$^2$</td>
<td>4,$^\text{c}$ 2.4$^\text{d}$</td>
<td>3.75</td>
</tr>
<tr>
<td>$\Delta q$</td>
<td>e</td>
<td>0.99,$^\text{d}$ 0.8$^\text{e}$</td>
<td>0.9</td>
</tr>
<tr>
<td>$\Delta \tilde{q}$</td>
<td>e</td>
<td>$(0.7 - 1.0)^\text{a,f,g}$</td>
<td>0.84*</td>
</tr>
<tr>
<td>$n$</td>
<td>$10^3$ $\mu$m$^{-2}$</td>
<td></td>
<td>9</td>
</tr>
<tr>
<td>$\tilde{n}$</td>
<td>$10^3$ $\mu$m$^{-2}$</td>
<td>$(7.5 - 10)^\text{a,h}$</td>
<td>9.6*</td>
</tr>
</tbody>
</table>

$^\text{a}$Iwasa (1993), Kakehata and Santos-Sacchi (1995).
$^\text{b}$Gale and Ashmore (1994).
$^\text{c}$Adachi and Iwasa (1999).
$^\text{d}$Gale and Ashmore (1997).
$^\text{e}$Dong et al. (2000).
$^\text{f}$Tunstall et al. (1995), Adachi et al. (2000).
$^\text{g}$Ashmore (1990), Santos-Sacchi (1991).
$^\text{h}$Huang and Santos-Sacchi (1993), Santos-Sacchi et al. (1998).
*After correction as described in the text.

Here, the axial compliance of the cell consists of two terms, of which one is constant and the other dependent on $P_\ell$. The constant term is 94 m/N. The linear part of the membrane capacitance of the 50-$\mu$m-long cell is $\sim$20 pF. Thus, the maximum values of the coupling coefficient $k$ for the cell is $\sim$0.31, somewhat smaller but still comparable to the one for an isolated motor.

## Consistency tests
Although experimental values for a number of quantities have been used to determine the theoretical parameters, there remain a number of experimentally determined quantities that are still unused. Comparing experimental values and the predicted values for these quantities can be used to examine the consistency of the model.

In the following, the magnitudes of those quantities are examined for testing consistency. Because the voltage dependences of these quantities, i.e., the sharpness of the dependence and shifts, have been used to determine the parameters, these properties are not useful for testing the model.

## Amplitude and $c_{12}$
Eq. 18 shows that the load-free relative amplitude is $b_1n$, where $b_1$ is defined by Eq. 19, because $P_\ell$ varies from 0 to 1. The chosen set of parameter values gives 0.05 for the relative amplitude, which agrees with 5%, the upper limit of the reported values (Ashmore, 1987; Santos-Sacchi and Dilger, 1988; Adachi et al., 2000).

The piezoelectric coefficient $c_{12}$ can be directly determined by
$$
\left(\frac{\delta L}{\delta V_{\mathrm{m}}}\right)_{\mathrm{F}_{z}}=c_{12},
$$
which is derived from Eq. 12. The value expected for a cell $50\ \mu$m in length, the expected value is 20 nm/mV. The experimental value for $c_{12}$ is $\sim$25 nm/mV for a cell $50\ \mu$m long (Ashmore, 1987; Santos-Sacchi and Dilger, 1988; Adachi et al., 2000) and in reasonable agreement.

## Ratio $c_{12}/c_{22}$
From Eq. 25, isometric force can be obtained by putting $\delta L=0$,
$$
\left(\frac{\delta F_{z}}{\delta V_{\mathrm{m}}}\right)_{\mathrm{L}}=-\frac{c_{12}}{c_{22}},
$$
the maximum value expected is $c_{12}(\text{max})/c_{22}(\text{max})$, which is $0.19\ \mathrm{nN/\mu m}$. Experimental values obtained are between 20 pN/mV (Hallworth, 1995; Frank et al., 1999) and 0.1 nN/mV (Iwasa and Adachi, 1997).

An alternative expression for the ratio $c_{12}/c_{22}$ is,
$$
\left(\frac{\delta Q}{\delta L}\right)_{\mathrm{V}_{\mathrm{m}}}=\frac{c_{12}}{c_{22}}.
$$

Experimental values for this quantity determined by charge transfer induced by cell displacements is between 0.03 and $0.1\ \mathrm{pC/\mu m}$. These values are equivalent to 0.03 and 0.1 nN/mV (Gale and Ashmore, 1994). These comparisons show that the expected value of $0.19\ \mathrm{nN/\mu m}$ is about two-fold larger than the largest experimental values.

This difference could be attributed to underestimating the axial compliance $c_{22}$ because the predicted value for $c_{12}$ is not larger than experimental data. There are two possible reasons for underestimating the axial compliance. One possible factor is underestimating the voltage dependence of the axial stiffness, and the other may be due to the value used for the axial compliance at $-75$ mV used to determine the elastic moduli.

## The axial compliance $c_{22}$
The model assumes that the elastic moduli is unaffected by the membrane potential. Nonetheless the axial compliance of the cell is voltage dependent, as Eq. 28 indicates. For the parameter values chosen, the axial compliance is $\sim$26% higher than its minimum at $P_\ell=0.5$, where $c_{12}$ also has its maximum. This effect has been taken into account to obtain $c_{12}/c_{22}$. Experimental data (He and Dallos, 1999, 2000) show that the axial compliance is $\sim$50% larger at $-20$ mV, where $c_{12}$ maximizes, than at $-75$ mV. Thus, the somewhat larger experimental values for the voltage dependence of the axial compliance may not have significant effect on the values for the force generation $c_{12}/c_{22}$, although it does bring the numbers closer.

Another possibility is that the value for the axial compliance is underestimated. Indeed, the predicted value for the ratio $c_{21}/c_{22}$ agrees with experimental values of 0.1 nN/mV or $0.1\ \mathrm{pC/\mu m}$ by adopting a value 200 m/N for the axial compliance at $-75$ mV for determining the elastic moduli. However, such an argument disregards the strong correlation between the compliance and force production in individual data sets (Table 2). A larger force production is observed in cells with lower compliance. For those reasons, it is likely that the model tends to underestimate the axial coefficients $c_{22}$, leading to some overestimation of the ratio $c_{12}/c_{22}$.

## DISCUSSION
Piezoelectric models for describing the voltage-dependent motility of the outer hair cell have been reported earlier (Mountain and Hubbard, 1994; Tolomeo and Steele, 1995). The present work clarifies a number of issues left out in those earlier reports, which are based on a formal piezo-

<table><thead><tr><td></td><td>Unit</td><td>Measured</td><td>Used</td><td>Expected</td></tr></thead><tbody><tr><td>$\epsilon_{z}/P$</td><td>$10^{-2}/kPa$</td><td>$-6.6,^{*a}-7^{b}$</td><td>7*</td><td>_</td></tr><tr><td>$\epsilon_{t}/P$</td><td>$10^{-2}/kPa$</td><td>$13^{b}$</td><td>13*</td><td>_</td></tr><tr><td>$c_{22}^{\ddagger}$</td><td>$10^{2}m/N$</td><td>$1,^{*c}1.6,^{d}1.7,^{e}$ $(4-12),^{f}18^{g}$</td><td>1*</td><td></td></tr><tr><td>$c_{12}^{+\frac {1}{4}}$</td><td>$10^{-5}m/V$</td><td>$2^{a,h,i}$</td><td>_</td><td>2</td></tr><tr><td></td><td>$10^{-5}C/N$</td><td>$2^{k}$</td><td>_</td><td>2</td></tr><tr><td>$c_{12}/c_{22}^{+}$</td><td>$10^{-8}N/V$</td><td>$10,^{c}(0.3-5.3),^{d}$ $(0.01-0.2)^{f}$</td><td>_</td><td>17</td></tr><tr><td></td><td>$10^{-8}C/m$</td><td>$(3-10),^{j}7^{k}$</td><td>_</td><td>17</td></tr></tbody></table>

$^{a}$Adachi et al. (2000).
$^{b}$Iwasa and Chadwick (1992).
$^{c}$Iwasa and Adachi (1997).
$^{d}$Frank et al. (1999).
$^{e}$He and Dallos (2000).
$^{f}$Hallworth (1995).
$^{g}$Holley and Ashmore (1988).
$^{h}$Ashmore (1987).
$^{i}$Santos-Sacchi and Dilger (1988).
$^{j}$Gale and Ashmore (1994).
$^{k}$Dong and Iwasa (2001).
*Value at ~−75 mV.
†Value at maximum.
‡Normalized to 50-μm-long cell.

electric description, by relating a two-state membrane motor model with the formal thermodynamic description. One issue that previous treatments had not addressed concerns the nonlinear characteristics of the hair cell motility, which is a natural consequence of a two-state model. Another issue is to clarify the relationship between the motor mechanism and the effect of incorporating the motor into the cell membrane. However, the most significant feature of the present treatment is in relating the cell function to its un- derlying molecules, which are likely to undergo discrete conformational transitions common with most functional proteins. Such issues cannot be adequately addressed by simply introducing adjustable parameters to simulate the nonlinearity (Spector et al., 1999).

## Physical identity of the motor
A basic assumption of the present model is that the mem- brane motor is a protein or a cluster of proteins, similar to any other functional membrane proteins, which undergo conformational transitions. These transitions involve trans- fer of charge across the membrane and changes in its membrane area.

The density of the functional motor units has been ob- tained from experimental data on the membrane capaci- tance. It is similar to the density of 10-nm particles (Gulley and Reese, 1977; Kalinec et al., 1992; Frolenkov et al., 1998) in the lateral membrane of the outer hair cell deter- mined by electron microscopy. A detailed comparison seems to suggest that the stoichiometry of the functional unit to those membrane particles is 2:1 rather than 1:1 (Santos-Sacchi et al., 1998). Because it is well established that membrane proteins have subunits and subunits can transfer charge independent of each other, the exact stoichi- ometry does not challenge the validity of the assumption.

Perhaps the observation most supportive of the idea that the motor is a membrane protein is that prestin, a membrane protein specific to the outer hair cell, confers a prominent nonlinear component to the membrane capacitance and volt- age-sensitive motility in kidney cells transfected with the mRNA that encodes the protein (Zheng et al., 2000). The significance of prestin was further confirmed recently by a report that prestin that is expressed in a number of mammalian cells shows tension sensitivity similar to the motor in the hair cell membrane (Ludwig et al., 2001). This observation indi- cates that the membrane protein constitutes the essential part of the motor, consistent with the model described here.

## Properties of the motor
The present model is designed to have a minimal number of parameters, all of which can be determined from experi- mental data. Experimental data unused for determining the parameters can then be used to test the consistency of the model. The attempt of minimizing the number of parame- ters may lead to oversimplification, in which the model is unable to explain some experimental observations. In the following, attention will be paid to whether such conflicts, if they exist, are fundamental.

### Number of motor states
The present model assumes that the motor has two states. Although there is no direct evidence that the motor has two states, most experimental data are consistent with the as- sumption. One such example is current noise (Iwasa, 1997; Dong et al., 2000). Current-charge fluctuation can indicate the quantized unit of charge that is transferred across the membrane if such an experiment has sufficient time reso- lution (Heinemann et al., 1992). However, it has been shown that the current-noise spectrum of motor-charge fluc- tuation has a characteristic frequency that exceeds 30 kHz, too high for such an analysis. The spectrum is explained equally well by either a two-state model or a three-state model (Dong et al., 2000).

### Electrical properties
The model assumes that the membrane capacitance does not depend on the motor state. This would be a crude approx- imation when some details of conformational transition are considered. The membrane capacitance of the extended state must be larger then that of the compact state because the extended state has a larger membrane area. A larger membrane area would mean less thickness because the volume is most likely conserved. The reduced thickness

also contributes to increases the capacitance. This effect could be offset by a reduction in the surface area of the rest of the membrane because a pressure decrease accompanies the motor's transition into the extended state. A recent report (Santos-Sacchi and Navarrete, 2001) indicates that the increase in the motor capacitance is dominant.

## Elastic properties
For the sake of simplicity, the model assumes that the stiffness of the motor does not depend on the states and that it is the same as the rest of the membrane. With this assumption, the model still shows that the axial compliance is increased by the motor activity. However, there is no reason that the extended and compact conformations should have the same elastic moduli.

The question of whether changes in the stiffness con- stitutes a significant part of the motile mechanism has been addressed by measuring the pressure dependence of the amplitude of voltage-dependent length changes. The absence of such an effect excludes stiffness changes as a major part of the motile mechanism (Adachi et al., 2000). The present model can explain the voltage dependence of the axial stiffness (He and Dallos, 1999, 2000) in the range between $-70$ and $-20$ mV (Iwasa, 2000). None- theless the predicted change in the axial compliance is biphasic, maximizing at $\sim-20$ mV, and differs from the experimental data, which show monotonous increase with rising voltage.

Such experimental data could be explained by assuming the elastic moduli of the cell membrane depend on the motor state. The simplest of such assumptions would be that the elastic moduli changes while maintaining their mutual ratios. To describe details of elasticity changes, the lateral membrane must be modeled as a composite structure. Such a treatment would be far more complex than the present paper.

## Connectivity with the cortical cytoskeleton
The present model assumes a series connection of the elastic element and the motor element, i.e., Eqs. 13 and 14. It is not immediately clear that the microscopic structure of the lateral wall, in which the cortical cytoskeleton and the motor-containing plasma membrane run parallel, intermit- tently linked by pillars, supports such a series connection if the stiffness of the wall is primarily determined by the cytoskeleton. Although such a result was obtained by con- sidering membrane bending in the cell axis assisted by the cortical cytoskeleton (Raphael et al., 2000), the approach requires assuming numerous parameter values, which are hard to determine. It turns out that membrane bending (flexoelectricity) also belongs to piezoelectricity because it satisfies the reciprocal relationship (Petrov, 1999). How- ever, the expected significance of the cortical cytoskeleton for motile activity does not appear to be consistent with the experimental observation that the motile machinery remains virtually unaffected by dissolving the cytoskeleton (Adachi and Iwasa, 1999).

## Comparison with piezoelectric material
The most striking feature of the electromechanical coupling in the outer hair cell is in its piezoelectric coefficient $c_{12}$, which is $\sim 25\ \mu$C/N. This value is four orders of magnitude greater than the best piezoelectric material, which has 2.5 nC/N (Park and Shrout, 1997). Values for more common piezoelectrics range from 2 to 4 pC/N for quartz to $\sim 550$ pC/N for Rochelle salt (Ikeda, 1990).

The coupling coefficients $k$ of 0.31 for the outer hair cell and $\sim 0.4$ for of its motor are, however, mid-range among common piezoelectric materials that range from 0.1 for quartz up to 0.76 for Rochelle salt. The main factor that makes the coupling coefficient of the outer hair cell unex- ceptional despite its enormous piezoelectric coefficient is its mechanical compliance, which is extremely large compared with inorganic materials.

## CONCLUSIONS
In this paper, a two-state area motor model for the outer hair cell is presented. The model results in nonlinear piezoelec- tricity for the motor and for the cell that incorporates such a motor into its plasma membrane. The model transparently relates various motile properties of the cell. A critical test for the theory is whether the piezoelectric reciprocal rela- tionship is satisfied by the cell. A recent preliminary study shows that the reciprocal relationship is indeed satisfied (Dong and Iwasa, 2001). The lower bound of the coupling coefficient of the motor is expected to be between 0.4 and 0.43. The coupling coefficient of the whole cell in its axial direction is $\sim 0.31$. The value is expected to be higher for basal cells, which have higher density of the motor. These values indicate that the outer hair cell has extremely effec- tive electromechanical coupling not only in its molecular motor but as a composite structure as well.

## APPENDIX
How good are values for the motor charge and density obtained from experiments using the phenomenological Eq. 31? This problem is ad- dressed here. The first term of Eq. 31 is phenomenological because it assumes that the factor $\alpha$, which represents the effect of motor on itself, is unity, the same condition as the motor being isolated. The charge $\tilde{q}$ and the number $\tilde{N}$ of the motor determined with curve fit should satisfy the two conditions,

$$
\frac{N\Delta q^{2}}{1+b_{2}/4}=\tilde{N}\Delta \tilde{q}^{2},\quad N\Delta q=\tilde{N}\Delta \tilde{q}.
$$

Piezoelectric Coupling in Hair Cells

Namely the maximum capacitance and the total motor charge must agree with true values. These conditions lead to formulas that relate the apparent values with true values of the two parameters,

$$
\Delta q=\tilde{q}\left(1+\frac{1}{4} b_{2}\right), \quad N=\frac{\tilde{N}}{1+b_{2} / 4}.
$$

Here, $b_{2}$ is defined by Eq. 22. It is proportional to the number $N$ of the motor in the membrane. By defining $\tilde{b}_{2}$, which is the counterpart that is proportional to the apparent number $\tilde{N}$, the relationship between $N$ and $\tilde{N}$ can be rewritten with $b_{2}$ and $\tilde{b}_{2}$,

$$
b_{2}=2\left(\sqrt{1+\tilde{b}_{2}}-1\right). \tag{A1}
$$

From this correction on the density, the motor charge can be corrected because the total charge must agree.

REFERENCES

Adachi, M., and K. H. Iwasa. 1999. Electrically driven motor in the outer hair cell: effect of a mechanical constraint. Proc. Natl. Acad. Sci. U.S.A. 96:7244-7249.

Adachi, M., M. Sugawara, and K. H. Iwasa. 2000. Effect of turgor pressure on outer hair cell motility. J. Acoust. Soc. Am. 108:2299-2306.

Armstrong, C. M., and F. Bezanilla. 1973. Currents related to movement of the gating particles of the sodium channels. Nature. 242:459-461.

Ashmore, J. F. 1987. A fast motile response in guinea-pig outer hair cells: the molecular basis of the cochlear amplifier. J. Physiol. (Lond.) 388:323-347.

Ashmore, J. F. 1989. Transducer motor coupling in cochlear outer hair cells. In Cochlear Mechanics: Structure, function, and Models. J. P. Wilson and D. T. Kemp, editors. Plenum, 107-114.

Ashmore, J. F. 1990. Forward and reverse transduction in guinea-pig outer hair cells: the cellular basis of the cochlear amplifier. Neurosci. Res. Suppl. 12:S39-S50.

Brownell, W., C. Bader, D. Bertrand, and Y. Ribaupierre. 1985. Evoked mechanical responses of isolated outer hair cells. Science. 227:194-196.

Dallos, P., and B. Evans. 1995. High-frequency motility of outer hair cells and the cochlear amplifier. Science. 267:2006-2009.

Dallos, P., R. Hallworth, and B. N. Evans. 1993. Theory of electrically driven shape changes of cochlear outer hair cells. J. Neurophys. 70:299-323.

Dong, X. X., D. Ehrenstein, and K. H. Iwasa. 2000. Fluctuation of motor charge in the lateral membrane of the cochlear outer hair cell. Biophys. J. 79:1876-1882.

Dong, X. X., and K. H. Iwasa. 2001. Charge displacement in the outer hair cell membrane elicited by external axial force. Assoc. Res. Otolaryngol. Abstr. 24:161.

Frank, G., W. Hemmert, and A. W. Gummer. 1999. Limiting dynamics of high-frequency electromechanical transduction of outer hair cells. Proc. Natl. Acad. Sci. U.S.A. 96:4420-4425.

Frolenkov, G. I., M. Atzori, F. Kalinec, F. Mammano, and B. Kachar. 1998. The membrane-based mechanism of cell motility in cochlear outer hair cells. Mol. Biol. Cell. 9:1961-1968.

Gale, J. E., and J. F. Ashmore. 1994. Charge displacement induced by rapid stretch in the basolateral membrane of the guinea-pig outer hair cell. Proc. Roy. Soc. (Lond.) B Biol. Sci. 255:233-249.

Gale, J. E., and J. F. Ashmore. 1997. The outer hair cell motor in membrane patches. Pflügers Arch. Eur. J. Physiol. 434:267-271.

Gulley, R. L., and T. S. Reese. 1977. Regional specialization of the hair cell plasmalemma in the organ of corti. Anat. Rec. 189:109-124.

Hallworth, R. 1995. Passive compliance and active force generation in the guinea pig outer hair cell. J. Neurophysiol. 74:2319-2328.

He, D. Z. Z., and P. Dallos. 1999. Somatic stiffness of cochlear outer hair cells is voltage-dependent. Proc. Natl. Acad. Sci. U.S.A. 96:8223-8228.

He, D. Z. Z., and P. Dallos. 2000. Properties of voltage-dependent somatic stiffness of cochlear outer hair cells. J. Assoc. Res. Otolaryngol.1:64-81.

Heinemann, S. H., F. Conti, and W. Stühmer. 1992. Recording of gating currents from xenopus oocytes and gating noise analysis. Methods Enzymol. 207:353-368.

Holley, M. C., and J. F. Ashmore. 1988. A cytoskeletal spring in cochlear outer hair cells. Nature. 335:635-637.

Huang, G., and J. Santos-Sacchi. 1993. Mapping the distribution of the outer hair cell motility sensor by electrical amputation. Biophys. J.65:2228-2236.

Ikeda, T. 1990. Fundamentals of Piezoelectricity. Oxford University Press.

Iwasa, K. H. 1993. Effect of stress on the membrane capacitance of the auditory outer hair cell. Biophys. J. 65:492-498.

Iwasa, K. H. 1994. A membrane model for the fast motility of the outer hair cell. J. Acoust. Soc. Am. 96:2216-2224.

Iwasa, K. H. 1997. Current noise spectrum and capacitance due to the membrane motor of the outer hair cell: theory. Biophys. J. 73:2965-2971.

Iwasa, K. H. 2000. Effect of membrane motor on the axial stiffness of the cochlear outer hair cell. J. Acoust. Soc. Am. 107:2764-2766.

Iwasa, K. H., and M. Adachi. 1997. Force generation in the outer hair cell of the cochlea. Biophys. J. 73:546-555.

Iwasa, K. H., and R. S. Chadwick. 1992. Elasticity and active force generation of cochlear outer hair cells. J. Acoust. Soc. Am. 92:3169-3173.

Kakehata, S., and J. Santos-Sacchi. 1995. Membrane tension directly shifts voltage dependence of outer hair cell motility and associated gating charge. Biophys. J. 68:2190-2197.

Kalinec, F., M. Holley, K. H. Iwasa, D. J. Lim, and B. Kachar. 1992. A membrane-based force generation mechanism in auditory sensory cells. Proc. Natl. Acad. Sci. U.S.A. 89:8671-8675.

Liberman, M. C., and L. W. Dodds. 1984. Single neuron labeling and chronic cochlear pathology. III. stereocilia damage and alterations of threshold tuning curves. Hearing Res. 16:55-74.

Ludwig, J., D. Oliver, N. Frank, A. W. Gummer, and B. Fakler. 2001. Reciprocal electromechanical properties of rat prestin: the motor mole-cule from rat outer hair cells. Proc. Natl. Acad. Sci. U.S.A. 98:4178-4183.

Mountain, D. C. 1980. Changes in endolymphatic potential and crossed olivocochlear bundle stimulation alter cochlear mechanics. Science. 210:71-72.

Mountain, D. C., and A. E. Hubbard. 1994. A piezoelectric model of outer hair cell function. J. Acoust. Soc. Am. 95:350-354.

Park, S. E., and T. R. Shrout. 1997. Ultrahigh strain and piezoelectric behavior in relaxor based ferroelectric single crystal. J. Appl. Phys.82:1804-1811.

Petrov, A. G. 1999. Lyotropic States of Matter: Molecular Physics and Living Matter Physics. Gordon and Breach, New York.

Raphael, R. M., A. S. Popel, and W. E. Brownell. 2000. A membrane bending model of outer hair cell electromotility. Biophys. J. 78:2844-2862.

Santos-Sacchi, J. 1991. Reversible inhibition of voltage-dependent outer hair cell motility and capacitance. J. Neurophysiol. 11:3096-3110.

Santos-Sacchi, J., and J. P. Dilger. 1988. Whole cell currents and mechan-ical responses of isolated outer hair cells. Hearing Res. 65:143-150.

Santos-Sacchi, J., S. Kakehata, T. Kikuchi, Y. Katori, and T. Takasaka.1998. Density of motility-related charge in the outer hair cell of the guinea pig is inversely related to best frequency. Neurosci. Lett. 256:155-158.

Santos-Sacchi, J., and E. G. Navarrete. 2001. The outer hair cell's linear

Biophysical Journal 81(5) 2495-2506

capacitance is nonlinear. *Assoc. Res. Otolaryngol Midwinter Meeting Abstracts.* 24:72-73.

Spector, A., W. E. Brownell, and A. S. Popel. 1999. Nonlinear active force generation by cochlear outer hair cell. *J. Acoust. Soc. Am.* 105:2414-2420.

Sukharev, S. I., W. J. Sigurdson, C. Kung, and F. Sachs. 1999. Energetic and spatial parameters for gating of the bacterial large conductance mechanosensitive channel, $m_{\rm scL}$. *J. Gen. Physiol.* 113:525-540.

Tolomeo, J. A., and C. R. Steele. 1995. Orthotropic piezoelectric properties of the cochlear outer hair cell wall. *J. Acoust. Soc. Am.* 97:3006-3011.

Tunstall, M. J., J. E. Gale, and J. F. Ashmore. 1995. Action of salicylate on membrane capacitance of outer hair cells from the guinea-pig cochlea. *J. Physiol. (Lond.).* 485:739-752.

Zheng, J., W. Shen, D. Z.-Z. He, K. B. Long, L. D. Madison, and P. Dallos. 2000. Prestin is the motor protein of cochlear outer hair cells. *Nature.* 405:149-155.
