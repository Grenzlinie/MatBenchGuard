# Modeling the Effect of Piezoceramic Hysteresis in Structural Vibration Control

M. Bulent Ozer and Thomas J. Royston*

Dept. of Mechanical Engineering, Univ. of Illinois at Chicago

## ABSTRACT

Dielectric hysteresis in piezoceramic transducers can degrade their performance in structural vibration control applications. Different hysteresis models have been applied to piezoelectric transducers, including those based on Preisach, Jiles-Atherton and Ishlinskii concepts. Relationships between these and other models, new experimental identification schemes and multi-term describing function representations of some of them are reviewed. Then, system equations that incorporate the hysteretic behavior are formulated for two pedagogical smart structural systems: a passively shunted / actively driven PZT wafer on (1) a simply supported thin plate and (2) a simply supported thin beam. The effect of PZT hysteresis on optimized passive and hybrid vibration control strategies is evaluated.

Keywords: hysteresis, piezoceramics, smart structure, vibration control, Preisach, Ishlinskii, Krasnosel'skii and Pokrovskii

## 1. INTRODUCTION

Both reversible nonlinearity and significant irreversible nonlinearity in the form of dielectric hysteresis are present in piezoceramic transducers, such as those based on lead zirconate (PZT). Hysteresis can have a detrimental effect on the performance of the piezoceramic in smart structural position and vibration control applications. Hysteresis can cause multiple output states for a given input state, frustrating open-loop control, and can generate unwanted amplitude-dependent phase shifts and harmonic distortion, which reduce the effectiveness of feedback control. On the other hand, hysteresis could potentially be harnessed as a means of unwanted vibratory energy dissipation in passive or hybrid control scenarios.

In order to appropriately assess the impact of, compensate for and potentially utilize piezoceramic transducer nonlinearities in the smart structural position or vibration control problem, a suitable system model is needed. For design robustness, parameters used in this model should be obtainable from studies on the individual components that make up the complex structural system, such as the individual transducers and elements of the structure. Additionally, the overall system model formulation should be computationally efficient to enable rapid simulations for parametric design studies and to enable real-time control or hysteresis compensation using model-reference, adaptive feedforward or other types of control strategies.

A number of different hysteresis models have been proposed for piezoelectric and other so-called smart materials, such as magnetostrictives and shape memory alloys. The interest here is confined to causal models that can be identified experimentally, can be formulated with finite dimensionality and for which an inverse exists, making them potentially useful in a hysteresis control strategy. Models that have been applied and which possess these qualities include finite-dimensional versions of the classical Preisach hysteresis model (CPM) $^{1-3}$, Ishlinskii hysteresis model (IM) $^{4-8}$, Krasnosel'skii / Pokrovskii hysteresis model (KP) $^{9-10}$, and Jiles-Atherton hysteresis model (JA) $^{11-12}$. In this article, some of the relationships between these models as applied to piezoceramics are reviewed and some extensions and generalizations of the Ishlinskii model are presented. Note, our scope here is limited to rate-independent and temperature independent hysteresis. This is an approximation to some degree for piezoceramics, as has been noted in recent studies by Smith et al. $^{13-14}$.

Specifically, for this article the following objectives are established:
(1) Formulate a constitutive model for the "two-dimensional" piezoceramic (PZT) wafer that incorporates reversible (anhysteretic) and irreversible (hysteretic) nonlinearity.
(2) Review and introduce expanded formulations of several of the most common finite-dimensional, causal, invertible hysteresis models and the relationships between them, as applied to piezoceramics. (Extensions to the authors' previous work on Ishlinskii models and their identification and representation as multi-term describing functions are included.)
(3) Integrate the nonlinear PZT model into the coupled dynamic equations of the overall system consisting of a simply supported plate or beam and electrically shunted PZT wafer bonded to the plate for passive or hybrid vibration control.
(4) Numerically simulate the coupled system equations to evaluate the impact of hysteresis.

* troyston@uic.edu; phone 312-413-7951; fax 312-413-0447; http://acoustics.me.uic.edu

Smart Structures and Materials 2001: Modeling, Signal Processing, and Control in Smart Structures,
Vittal S. Rao, Editor, Proceedings of SPIE Vol. 4326 (2001) © 2001 SPIE · 0277-786X/01/$15.00

## 2. RATE-INDEPENDENT HYSTERESIS IN PLANAR PIEZOCERAMIC DEVICES

Consider a thin monolithic piezoceramic (PZT) wafer with geometry depicted in Fig. 1. Often, these types of devices are adhered to plate-like structures and used for passive and/or active vibration or structural acoustic control. In such configurations, it is approximated that $T_3 = D_1 = D_2 = E_1 = E_2 = 0$ and the resulting "two-dimensional" electroelastic constitutive equations may be expressed as follows under the assumption that the wafer is isotropic within the wafer plane ("1" and "2" directions with identical properties):

$$
\mathrm{T}_{1}=\frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}^{2}}\left(\mathrm{~S}_{1}+\mathrm{v}_{\mathrm{pz}} \mathrm{S}_{2}\right)-\mathrm{h}_{31} \mathrm{D}_{3}, \quad \mathrm{~T}_{2}=\frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}^{2}}\left(\mathrm{~S}_{2}+\mathrm{v}_{\mathrm{pz}} \mathrm{S}_{1}\right)-\mathrm{h}_{32} \mathrm{D}_{3}, \quad \mathrm{E}_{3}=-\mathrm{g}_{31} \mathrm{~T}_{1}-\mathrm{g}_{32} \mathrm{~T}_{2}+\left\{\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}\right\}. \tag{1a-c}
$$

Here, the variables are mechanical stress T, electric displacement D, mechanical strain S and electric field E. Superscripts D and T refer to "at constant" electrical displacement or mechanical stress, respectively, and numerical subscripts refer to geometric direction (see Fig. 1). Coefficients $\mathrm{E}_{\mathrm{pz}}$, $\mathrm{v}_{\mathrm{pz}}$, h, g, and $\beta$ refer to the elastic modulus, Poisson's ratio, two piezoelectric constants, and the dielectric impermeability, respectively. Note that "1-dimensional" formulation of the constitutive relations can be extracted from equation (1a-c). If, for example, $T_2 = 0$ and one is only interested in the relation between variables in the 1 and 3 direction, then:

$$
\mathrm{T}_{1}=\frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}^{2}}\left(\mathrm{~S}_{1}+\mathrm{v}_{\mathrm{pz}} \mathrm{S}_{2}\right)-\mathrm{h}_{31} \mathrm{D}_{3}, \quad \mathrm{E}_{3}=-\mathrm{g}_{31} \mathrm{~T}_{1}+\left\{\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}\right\}. \tag{2a-b}
$$

A number of studies have shown that, even at relatively low electrical and/or mechanical stress levels, piezoelectric ceramics exhibit substantial rate-independent nonlinear behavior, primarily hysteretic, in their electroelastic interaction which is not accounted for in a linear formulation of the electroelastic equations for the material. In the above equations (1c, 2b) nonlinear behavior in the PZT is denoted in the dielectric relation by use of the brackets {}. In other words, in these equations $\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}$ is an input to a nonlinear operation that yields the output $\left\{\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}\right\}$.

These equations (1a-c, 2a-b) agree with experimental observations of PZT reported in the literature. For example, Goldfarb and Celanovic $^{4}$ observed that the applied electrical displacement (D) vs. strain (S) relation under zero stress (T) was reversible, but that applied electric field (E) vs. S under zero T was not. They also observed that the mechanical stress-strain relation under constant electric displacement was reversible whereas the relation under constant electric field was hysteretic. Damjanovic et al. $^{15}$ observed that the applied stress vs. electrical displacement relation was hysteretic.

Regardless of whether one is interested in the "1-dimensional" or "2-dimensional" formulation the hysteretic behavior requires only a scalar description. There is a single input quantity $\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}$ and a single output quantity $\left\{\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}\right\}$ that equals $(\mathrm{E}_{3}+\mathrm{g}_{31} \mathrm{~T}_{1}+\mathrm{g}_{32} \mathrm{~T}_{2})$, whether or not $T_2 = 0$. In Section 3 various hysteresis models are reviewed and introduced that may describe this scalar relation. For the sake of brevity and generality, $\beta_{33}^{\mathrm{T}} \mathrm{D}_{3}$ will simply be denoted as $\beta^{\mathrm{T}} \mathrm{D}$ and $(\mathrm{E}_{3}+\mathrm{g}_{31} \mathrm{~T}_{1}+\mathrm{g}_{32} \mathrm{~T}_{2})$ will simply be denoted as E. In other words, the relationship is $\mathrm{E}=\left\{\beta^{\mathrm{T}} \mathrm{D}\right\}$. Also as an alternative, one may choose to make E the input and D the output: $\mathrm{D}=\{\mathrm{E}\}^{-1} / \beta^{\mathrm{T}}$. Often, one controls E (or a portion of it); so, it is the input to the system and D is the output. But, sometimes a model for the relationship is needed with D as the input and E as the output in order to apply some form of inverse compensation to the system.

![](./images/812376298885218304_1.jpg)

Fig. 1. Schematic of piezoceramic (PZT-5H) monolithic wafer. Nickel electrode sputtered on "3" sides. Dimensions in millimeters.

![](./images/812376298885218304_2.jpg)

Fig. 2. Preisach hysteresis relay operator, $\gamma_{xy}[\mathrm{u}(\mathrm{t})]$.

## 3. MODELS FOR RATE-INDEPENDENT HYSTERESIS IN PIEZOCERAMICS

### 3.1 Classical Preisach Hysteresis Model
The classical Preisach model has been applied by a number of researchers to piezoceramics $^{1-3,16}$. A detailed description of it and other Preisach models can be found in the text by Mayergoyz $^{17}$. Put simply, the classical Preisach model (CPM) combines the outputs of independent bi-stable relays to form its output according to the formula:

$$
\mathrm{f}(\mathrm{t})=\iint_{\mathrm{x} \geq \mathrm{y}} \mu(\mathrm{x}, \mathrm{y}) \gamma_{\mathrm{xy}}[\mathrm{u}(\mathrm{t})] \mathrm{dxdy}.
\tag{3}
$$

Here, f(t) is the output, u(t) is the input, $\mu$(x,y) is the weight function and $\gamma_{xy}$ is the simple hysteresis relay operator whose value is determined by the input operation depicted in Fig. 2. And, x and y correspond to up and down switching values of the input, respectively.

There are two key properties of a hysteretic relationship that are necessary and sufficient for that relationship to be considered classical Preisach. These are the *wiping-out* condition and the *congruency* condition. It has been explicitly shown in previous studies that some PZT-based devices used in structural vibration and acoustic control do satisfy these properties, at least at moderate drive levels sufficiently below saturation and at sufficiently low bandwidth to avoid significant rate- and temperature-dependent effects: 1-3 piezoceramic $^{7,16}$, monolithic wafer $^{6}$.

The *wiping-out* property, can be stated as follows. Any sequence of extrema of the input can be reduced to a sequence with decreasing excursions between subsequent extrema without any change in the output. This is accomplished by removing (wiping-out) any pair of subsequent extrema whenever the final value of the input exits the interval between them. Closure of minor hysteresis loops is a direct consequence of the wiping-out property. The wiping-out property is shown schematically in Fig. 3a. Take u as the current input value. As shown in Fig. 3a, in the case of the maximum values, $u_1$ and $u_2$ are wiped-out by $u_3$ and $u_4$ is wiped out by $u_5$. In regard to minimum values, $l_1$ and $l_2$ are wiped-out by $l_3$ and $l_4$ is wiped out by $l_5$. Therefore, extrema sets of the input that are needed to calculate the current output value f are $\{u_0,l_0\}$, $\{u_3,l_3\}$, $\{u_5,l_5\}$, $\{u_6,l_6\}$, and $\{u_7,u\}$. The *congruency* property can be stated as follows. All minor hysteresis loops having the same reversal values of the input, but possibly different prior history, are congruent. The congruency property is shown schematically in Fig. 3b. Congruency means that the difference $d_1$ of the upper minor loop with the input variation between $u_1$ and $u_2$ are the same as the difference $d_2$ of the lower minor loop with the input variation between $u_1$ and $u_2$.

Since hysteresis describes rate-independent irreversible thermodynamic processes, any hysteresis relation can be viewed as a mathematical mapping between a sequence of input extrema and the output. The effect of each input extremum on the output determines the exact nature of the hysteresis relation. For the Preisach model, the effect of each input extremum can be analyzed through the wiping-out and congruency properties. The wiping-out property allows the reduction of any given sequence of input extrema to a sequence with gradually diminishing input excursions. The congruency property guarantees that every input extremum in the resulting sequence can be treated as if it was the first and only extremum to occur. Thus, the set of all inputs with only a single extremum predicts the output in general. Using this fact, Mayergoyz $^{17}$ concluded that the Preisach model is any scalar hysteresis relation that exhibits wiping-out and minor loop congruency. In other words, these two properties are necessary and sufficient if a hysteresis relation is to be represented by the Preisach model. Also based on the above arguments, Mayergoyz $^{17}$ developed an experimental identification scheme and a means of calculating irreversible hysteretic energy losses due to arbitrary input time histories.

![](./images/812376298885218304_3.jpg)

Fig. 3. Main properties of the classical Preisach hysteresis model. a) Wiping-out property. b) Congruency property.

### 3.2 Ishlinskii Hysteresis Models

**Description and relation to the CPM.** A generalized finite-dimensional Ishlinskii hysteresis model (GIM) is schematically represented in Fig. 4 in terms of a mechanical system. (Note, in some prior publications⁶·⁸, this type of model has been referred to as a generalized Maxwell resistive capacitor model (GMRC).) Referring to Fig. 4, the model may be implemented as follows:
$$
\mathrm{E}=\operatorname{GIM}\left\{\beta^{\mathrm{T}} \mathrm{D}\right\}
\tag{4a}
$$
$$
\text{with } \operatorname{GIM}\left\{\beta^{\mathrm{T}} \mathrm{D}\right\}=\sum_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{E}_{\mathrm{rc}}^{(\mathrm{i})} \text{ where}
$$
for i = 1, ..., n - 1
$$
\begin{aligned}
& \text { if }\left|\beta^{\mathrm{T}(\mathrm{i})}\left(\mathrm{D}-\mathrm{D}_{\mathrm{b}}^{(\mathrm{i})}\right)\right|<\mathrm{e}_{\mathrm{rc}}^{(\mathrm{i})} \text { then } \mathrm{E}_{\mathrm{rc}}^{(\mathrm{i})}=\beta^{\mathrm{T}(\mathrm{i})}\left(\mathrm{D}-\mathrm{D}_{\mathrm{b}}^{(\mathrm{i})}\right) \\
& \text { otherwise } \mathrm{E}_{\mathrm{rc}}^{(\mathrm{i})}=\mathrm{e}_{\mathrm{rc}}^{(\mathrm{i})} \operatorname{Sign}[\dot{\mathrm{D}}] \text { and } \mathrm{D}_{\mathrm{b}}^{(\mathrm{i})} \text { is set such that }\left|\beta^{\mathrm{T}(\mathrm{i})}\left(\mathrm{D}-\mathrm{D}_{\mathrm{b}}^{(\mathrm{i})}\right)\right|=\mathrm{e}_{\mathrm{rc}}^{(\mathrm{i})}
\end{aligned}
\tag{4b}
$$
and for i = n
$$
\mathrm{E}_{\mathrm{rc}}^{(\mathrm{n})}=\beta^{\mathrm{T}(\mathrm{n})} \mathrm{D}+\mathrm{f}(\mathrm{D}).
\tag{4c}
$$

Here, f(D) denotes any 1 to 1 reversible mapping of D. The terms $\beta^{\mathrm{T}}$, $\mathrm{e}_{\mathrm{N}}$, $\mu$, $\mathrm{e}_{\mathrm{rc}}$, and $\mathrm{D}_{\mathrm{b}}$ may be viewed as electrical analogies to a mechanical spring stiffness, normal force, Coulomb friction coefficient, the force due to Coulomb friction and the displacement from an equilibrium position of a massless slider, respectively. The component f(D) accounts for a reversible nonlinear "spring stiffness" effect. If f(D) = 0, a simpler Ishlinskii hysteresis model (IM) is recovered. (In some prior publications, this is referred to as a Maxwell resistive capacitor (MRC) hysteresis model⁴·⁸·¹⁶.)

![](./images/812376298885218304_4.jpg)

Fig. 4. Generalized Ishlinskii hysteresis model (GIM). a) Equivalent mechanical analogy. b) Input-output relation for n=2 and f(D)=0 (IM).

In previous studies, it has been established that the IM and its inverse are particular cases of the classical Preisach hysteresis model (CPM)⁷. (Indeed, the basic IM unit or operator is an elementary stop hysteron, as defined in the magnetics literature¹⁸·¹⁹. Others have specifically referred to it as an Ishlinskii operator²⁰.) Also, in previous studies, a means of calculating irreversible hysteretic energy loss for arbitrary input time histories was formulated based on the IM's equivalence to the CPM⁷. Like the IM, each component of the GIM also satisfies the two necessary and sufficient conditions for it to be considered a classical Preisach model, the *wiping out* property and the property of *congruent* minor loops. The slide elements of the GIM are identical to those of the IM. The only difference is that now, the reversible element (i = n) is nonlinear. But, a reversible element trivially satisfies congruency and wiping out. Since no hysteretic energy loss is associated with the reversible element of the GIM, its hysteretic energy loss for arbitrary input time histories can be calculated in the same way as they are calculated for the IM⁶.

Now, consider a GIM model in which f(D) is a polynomial function of the following form:
$$
\mathrm{f}(\mathrm{D})=\beta^{\mathrm{T}(\mathrm{n})}\left[\alpha_{2} \mathrm{D}^{2}+\alpha_{3} \mathrm{D}^{3}+\alpha_{4} \mathrm{D}^{4}+...\right],
\tag{5a}
$$
such that
$$
\mathrm{E}_{\mathrm{rc}}^{(\mathrm{n})}=\beta^{\mathrm{T}(\mathrm{n})}\left[\mathrm{D}+\alpha_{2} \mathrm{D}^{2}+\alpha_{3} \mathrm{D}^{3}+\alpha_{4} \mathrm{D}^{4}+...\right].
\tag{5b}
$$

It is noted that any continuous reversible function (with continuous derivatives) can be represented in polynomial form using a Taylor Series expansion.

Since the GIM is a classical Preisach model (CPM), it is uniquely defined by its first order transition (reversal) curves. These are graphically represented by the Everett function
$$\mathrm{F}(\mathrm{x}, \mathrm{y})=\frac{1}{2}\left(\mathrm{f}_{\mathrm{x}}-\mathrm{f}_{\mathrm{xy}}\right),\tag{6}$$
which exists within the Preisach triangle T(x, y) shown in Fig. 5. The parameters that form the Everett function are obtained by first monotonically increasing the input (D) from negative saturation to x obtaining the output (E) denoted $f_x$. Then, the input (D) is monotonically decreased to y obtaining the output (E) denoted $f_{xy}$. For the GIM model of equations (4-5), the Everett function takes the following form:
$$
\begin{aligned}
\mathrm{F}(\mathrm{x}, \mathrm{y})= & \frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})}\left[(\mathrm{x}-\mathrm{y})+\alpha_{2}\left(\mathrm{x}^{2}-\mathrm{y}^{2}\right)+\alpha_{3}\left(\mathrm{x}^{3}-\mathrm{y}^{3}\right)+\alpha_{4}\left(\mathrm{x}^{4}-\mathrm{y}^{4}\right)+\ldots\right]+\frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})}\left\{(\mathrm{x}-\mathrm{y})-\left(\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right) \mathrm{H}\left[\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right]\right\} \\
= & \frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})}\left[1+\alpha_{2}(\mathrm{x}+\mathrm{y})+\alpha_{3}\left(\mathrm{x}^{2}+\mathrm{xy}+\mathrm{y}^{2}\right)+\alpha_{4}\left(\mathrm{x}^{2}+\mathrm{y}^{2}\right)(\mathrm{x}+\mathrm{y})+\ldots\right](\mathrm{x}-\mathrm{y}) \\
& +\frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})}\left\{(\mathrm{x}-\mathrm{y})-\left(\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right) \mathrm{H}\left[\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right]\right\}
\end{aligned},\tag{7a}
$$
where $\mathrm{H}[\lambda]$ denotes the Heaviside function with
$$\mathrm{H}[\lambda]=\left\{\begin{array}{l}
1 \ \lambda>0 \\
0 \ \lambda<0
\end{array}.\tag{7b}\right.$$

![](./images/812376298885218304_5.jpg)
![](./images/812376298885218304_6.jpg)

Fig. 5. Functional relationships of classic Preisach representation of IM hysteresis model. a) Weighting function $\mu(x,y)$. b) Everett function F(x,y) based on first order transition curves.

**Experimental Model Identification.** A method for identification of best-fit IM and GIM models for a given experimental hysteretic relation is developed based on the fact that they are classical Preisach models and by using the Everett function, which can be determined experimentally for any input-output relation. Of course, a reasonable fit will only exist if the experimental data does satisfy the two necessary and sufficient conditions, *congruency* and *wiping-out*, for it to be represented by a classical Preisach model. Given that these conditions are satisfied, one can proceed by first implementing a coordinate transformation on the Preisach triangle to $\mathrm{x}_{\mathrm{h}}$ and $\mathrm{x}_{\mathrm{v}}$, which are denoted on Fig. 5 and related to x and y by the following expressions:
$$\mathrm{x}_{\mathrm{h}}=(\mathrm{x}+\mathrm{y}) / \sqrt{2} \text { and } \mathrm{x}_{\mathrm{v}}=(\mathrm{x}-\mathrm{y}) / \sqrt{2}.\tag{8a-b}$$

Next, equation (7) is evaluated in the Preisach triangle along the line $\mathrm{x}_{\mathrm{v}}=\mathrm{w}_{1} / \sqrt{2}$ (i.e. $\mathrm{x}=\mathrm{y}+\mathrm{w}_{1}$):
$$
\begin{aligned}
\mathrm{F}\left(\mathrm{x}_{\mathrm{h}}, \mathrm{x}_{\mathrm{v}}=\mathrm{w}_{1} / \sqrt{2}\right) & =\frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})} \mathrm{w}_{1}\left[1+\alpha_{2}(2)^{1 / 2} \mathrm{x}_{\mathrm{h}}+\alpha_{3}\left(\frac{3}{2} \mathrm{x}_{\mathrm{h}}^{2}+\frac{\mathrm{w}_{1}^{2}}{4}\right)+\alpha_{4}\left((2)^{1 / 2} \mathrm{x}_{\mathrm{h}}^{3}+(2)^{3 / 2} \mathrm{x}_{\mathrm{h}} \mathrm{w}_{1}^{2}\right)+\ldots\right]+\frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})} \mathrm{w}_{1} \\
& =\frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}} \beta^{\mathrm{T}(\mathrm{i})} \mathrm{w}_{1}+\frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})} \mathrm{w}_{1}\left[\begin{array}{l}
\left(\alpha_{3} \frac{\mathrm{w}_{1}^{2}}{4}+\alpha_{5} \frac{\mathrm{w}_{1}^{4}}{16}+\mathrm{O}\left[\mathrm{w}_{1}^{6}\right]\right)+\left((2)^{1 / 2} \alpha_{2}+(2)^{3 / 2} \alpha_{4} \mathrm{w}_{1}^{2}+\mathrm{O}\left[\mathrm{w}_{1}^{4}\right]\right) \mathrm{x}_{\mathrm{h}} \\
+\left(\frac{3}{2} \alpha_{3}+\frac{1}{8} \alpha_{5} \mathrm{w}_{1}^{2}+\mathrm{O}\left[\mathrm{w}_{1}^{4}\right]\right) \mathrm{x}_{\mathrm{h}}^{2}+\left((2)^{1 / 2} \alpha_{4}+\mathrm{O}\left[\mathrm{w}_{1}^{2}\right]\right) \mathrm{x}_{\mathrm{h}}^{3}+\ldots
\end{array}\right]
\end{aligned}.\tag{9}
$$

If $w_1$ is chosen sufficiently small, then $\alpha_{\#} w_1^{\mathrm{p}} \ll 1$ where $\mathrm{p}>1$ and the above equation simplifies to:

$$
\mathrm{F}\left(\mathrm{x}_{\mathrm{h}}, \mathrm{x}_{\mathrm{v}}=\mathrm{w}_{1} / \sqrt{2}\right) \approx \frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}} \beta^{\mathrm{T}(\mathrm{i})} \mathrm{w}_{1}+\frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})} \mathrm{w}_{1}\left[\left((2)^{1 / 2} \alpha_{2}\right) \mathrm{x}_{\mathrm{h}}+\left(\frac{3}{2} \alpha_{3}\right) \mathrm{x}_{\mathrm{h}}^{2}+\left((2)^{1 / 2} \alpha_{4}\right) \mathrm{x}_{\mathrm{h}}^{3}+\left(\frac{5}{4} \alpha_{5}\right) \mathrm{x}_{\mathrm{h}}^{4}+\ldots\right].(10)
$$

Note that for a symmetric relationship, $\alpha_{2}=\alpha_{4}=\alpha_{6}=\ldots=0$ and the general expression will be:

$$
\mathrm{F}\left(\mathrm{x}_{\mathrm{h}}, \mathrm{x}_{\mathrm{v}}=\mathrm{w}_{1} / \sqrt{2}\right) \approx \frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}} \beta^{\mathrm{T}(\mathrm{i})} \mathrm{w}_{1}+\frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})} \mathrm{w}_{1} \sum_{\mathrm{j}=1}^{\mathrm{M}}\left[\frac{2 \mathrm{j}+1}{2^{\mathrm{j}}} \alpha_{2 \mathrm{j}+1} \mathrm{x}_{\mathrm{h}}^{2 \mathrm{j}}\right],
\tag{11}
$$

where M denotes the order of the polynomial used in f(D). Along the line $\mathrm{x}_{\mathrm{v}}=\mathrm{w}_{1} / \sqrt{2}$ one can perform a least squares polynomial curve fit and extract the values of $\sum_{\mathrm{i}=1}^{\mathrm{n}} \beta^{\mathrm{T}(\mathrm{i})}, \beta^{\mathrm{T}(\mathrm{n})} \alpha_{2}, \beta^{\mathrm{T}(\mathrm{n})} \alpha_{3}$, etc. up to the desired level of accuracy using either equations (9), (10) or (11), depending on the situation (symmetric or nonsymmetric) and again, the desired level of accuracy.

Once such a polynomial has been determined, an approximation to f(D) which shall be called $\overline{\mathrm{f}}$ (D) can be created. Using the input history to form the original Everett function, F(x,y), an Everett function $\mathrm{F}_{\mathrm{ml}}(\mathrm{x}, \mathrm{y})$ based on $\overline{\mathrm{f}}$ (D) alone can be constructed and subtracted from $\mathrm{F}(\mathrm{x}, \mathrm{y})$ to obtain $\mathrm{F}_{\mathrm{IM}}(\mathrm{x}, \mathrm{y})$:
$$
\mathrm{F}_{\mathrm{IM}}(\mathrm{x}, \mathrm{y})=\mathrm{F}(\mathrm{x}, \mathrm{y})-\mathrm{F}_{\mathrm{ml}}(\mathrm{x}, \mathrm{y}).
\tag{12}
$$

The subscript IM is chosen since this resulting Everett function will have the properties of an IM model (if the GIM model was a reasonable approximation for the particular experimental hysteresis relationship in the first place). If $\overline{\mathrm{f}}(\mathrm{D}) \approx \mathrm{f}(\mathrm{D})$, then

$$
\mathrm{F}_{\mathrm{IM}}(\mathrm{x}, \mathrm{y}) \approx \frac{1}{2} \sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})}\left\{(\mathrm{x}-\mathrm{y})-\left(\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right) \mathrm{H}\left[\mathrm{x}-\mathrm{y}-\mathrm{w}_{\mathrm{i}}\right]\right\}+\frac{1}{2} \beta^{\mathrm{T}(\mathrm{n})}(\mathrm{x}-\mathrm{y}).
\tag{13}
$$

For $\mathrm{F}_{\mathrm{IM}}$, lines in the Preisach triangle that are parallel to the $\mathrm{x}-\mathrm{y}$ line have a constant value. A method to experimentally identify the unknown parameters given $\mathrm{F}_{\mathrm{IM}}(\mathrm{x}, \mathrm{y})$ and assigned values for $\mathrm{w}_{\mathrm{i}} \mathrm{i}=1, \ldots, \mathrm{n}-1$ directly follows. The methodology presented here assumes that $\left|\mathrm{x}_{\max }\right|=\left|\mathrm{y}_{\min }\right|$ but can be easily generalized. It also assumes that the Preisach triangle $\mathrm{T}(\mathrm{x}, \mathrm{y})$ is divided by $\mathrm{n}$ lines parallel to the $\mathrm{x}=\mathrm{y}$ line that are equally separated in distance with the $\mathrm{n}^{\text {th }}$ line intersecting the point $(\mathrm{x}, \mathrm{y})=$ $\left(\mathrm{x}_{\max },-\mathrm{x}_{\max }\right)$. Thus, values for $\mathrm{w}_{\mathrm{i}}$ are chosen in equal increments in length and given by the following:

$$
\mathrm{w}_{\mathrm{i}}=\frac{\mathrm{i} 2}{\mathrm{n}} \mathrm{x}_{\max } \quad \mathrm{i}=1, \ldots, \mathrm{n}.
\tag{14}
$$

Note here that greater accuracy will be achieved as $\mathrm{n}$ is increased since the discretization of the Preisach plane will be more refined. Additionally, larger $\mathrm{n}$ means that $\mathrm{w}_{1}$ will be smaller and the approximations of equations $(10-11)$ will be more reasonable. So, for $\mathrm{F}_{\mathrm{IM}}(\mathrm{x}, \mathrm{y})$, it is possible to average its values along lines parallel to the $\mathrm{x}=\mathrm{y}$ line at distances $\mathrm{w}_{\mathrm{i}}$ from the $\mathrm{x}$ $=\mathrm{y}$ line. These averaged values will be denoted:

$$
\mathrm{F}_{\mathrm{x}_{\mathrm{i}}^{\prime}}=\frac{1}{\sqrt{2}\left(2 \mathrm{x}_{\max }-\mathrm{w}_{\mathrm{i}}\right)} \int_{\mathrm{y}_{\min }}^{\mathrm{x}_{\max }} \mathrm{F}_{\mathrm{IM}}\left(\mathrm{x}^{\prime}, \mathrm{x}^{\prime}-\mathrm{w}_{\mathrm{i}}\right) \mathrm{dx}^{\prime}, \quad \text { with } \quad \mathbf{F}_{\mathbf{x}^{\prime}}=\left[\begin{array}{c}
\mathrm{F}_{\mathrm{x}_{1}^{\prime}} \\
\vdots \\
\mathrm{F}_{\mathrm{x}_{\mathrm{n}}^{\prime}}
\end{array}\right].
\tag{15a-b}
$$

Equations (13-15) may be written in the following form, solving for the vector $\boldsymbol{\beta}^{\mathbf{T}}$ of the unknown IM elastic coefficients:

$$
\boldsymbol{\beta}^{\mathbf{T}}=\left[\begin{array}{c}
\beta^{\mathrm{T}(1)} \\
\vdots \\
\beta^{\mathrm{T}(\mathrm{n})}
\end{array}\right]=\frac{\mathrm{n}}{\mathrm{x}_{\max }}\left[\begin{array}{ccccc}
1 & 1 & \cdots & 1 & 1 \\
1 & 2 & \cdots & 2 & 2 \\
\vdots & \vdots & 3 & \cdots & 3 \\
1 & 2 & \vdots & \ddots & \vdots \\
1 & 2 & 3 & \cdots & \mathrm{n}
\end{array}\right]^{-1} \mathbf{F}_{\mathbf{x}^{\prime}}.
\tag{16}
$$

Upon determining the elastic coefficients, the sliding constants can be determined using the following.

$$
\mathrm{e}_{\mathrm{rc}}^{(\mathrm{i})}=\frac{\mathrm{ix}_{\max }}{\mathrm{n}} \beta^{\mathrm{T}(\mathrm{i})} \quad \mathrm{i}=1, \ldots, \mathrm{n}-1.
\tag{17}
$$

Note that a value for $\mathrm{e}_{\mathrm{rc}}^{(\mathrm{n})}$ is not needed as this is not used in equation (4).

Periodic excitation - response simulation tools. For computational analysis and design studies, it is useful to have the IM and GIM models represented in terms of multi-term describing functions. This is developed here for the case that the system is subjected to periodic excitation and response. Take a single IM elasto-slide element. Considering D as an input and $D_{b}^{(i)}$ as an output, one approach to formulating the describing function is to note that the kinematic relationship is the same as that of an elementary backlash element, shown in Fig. 6a. The describing function representation of a system with backlash is available in the literature $^{21}$. The first order describing function expression for a sinusoidal input of amplitude D is:

$$
\operatorname{Desc}_{1}=\frac{2 \cdot \mathrm{j}}{\pi \cdot \mathrm{D}}\left(\int_{0}^{\frac{\pi}{2}}\left(\mathrm{D} \cdot \sin (\psi)-\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \psi} \cdot \mathrm{d} \psi+\int_{\frac{\pi}{2}}^{\psi_{1}}\left(\mathrm{D}-\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \psi} \cdot \mathrm{d} \psi+\int_{\psi_{1}}^{\pi}\left(\mathrm{D} \cdot \sin (\psi)+\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \psi} \cdot \mathrm{d} \psi\right),
\tag{18a}
$$

where $\quad \psi_{1}=\pi-\arcsin \left(1-2 \mu \mathrm{e}_{\mathrm{N}} / \beta^{\mathrm{T}} / \mathrm{D}\right)$.
\tag{18b}

![](./images/812376298885218304_7.jpg)

![](./images/812376298885218304_8.jpg)

Fig. 6. a) System with backlash characteristics. b) Comparison of single and multi-term describing functions for single IM slide element. Response to sinusoidal input. Key: IM, 3-term, 1-term describing function.

Accounting for stationary behavior of $D_{b}$ during start-up one obtains:
$$
\text { for } \mathrm{D}<\mu \mathrm{e}_{\mathrm{N}} / \beta^{\mathrm{T}}, \quad \quad \operatorname{Desc}_{1}=0.
\tag{19a}
$$

$$
\text { for } \mathrm{D}>\mu \mathrm{e}_{\mathrm{N}} / \beta^{\mathrm{T}}, \quad \quad \operatorname{Desc}_{1}=\frac{\frac{\pi}{2}-\arcsin \left(\frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}-1\right)+\left(1-\frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}\right) \cdot \sqrt{2 \frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}-\left(\frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}\right)^{2}}}{\pi}-\frac{\mathrm{j} \cdot\left(2 \frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}-\left(\frac{\frac{2 \mu \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}}{\mathrm{D}}\right)^{2}\right)}{\pi}.
\tag{19b}
$$

Accuracy can be improved by using higher order (multi-harmonic) describing functions. The expression for the $\mathrm{k}^{\text {th }}$ order describing function is:

$$
\operatorname{Desc}_{\mathrm{k}}=\frac{2 \cdot \mathrm{j}}{\pi \cdot \mathrm{D}}\left(\int_{0}^{\frac{\pi}{2}}\left(\mathrm{D} \cdot \sin (\psi)-\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \mathrm{k} \cdot \psi} \cdot \mathrm{d} \psi+\int_{\frac{\pi}{2}}^{\psi_{1}}\left(\mathrm{D}-\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \mathrm{k} \cdot \psi} \cdot \mathrm{d} \psi+\int_{\psi_{1}}^{\pi}\left(\mathrm{D} \cdot \sin (\psi)+\frac{\mu \cdot \mathrm{e}_{\mathrm{N}}}{\beta^{\mathrm{T}}}\right) \cdot \mathrm{e}^{-\mathrm{j} \mathrm{k} \cdot \psi} \cdot \mathrm{d} \psi\right).
\tag{20}
$$

Due to space constraints, the lengthy analytical evaluation of this integral is omitted. Using expression (20) any higher order describing function can be computed. Fig. 6b illustrates the improvement in response as additional higher order terms are included.

For the GIM, the describing function representation must also account for the reversible nonlinear term f(D). For the case that $\mathrm{f}(\mathrm{D})=\alpha_{3} \beta^{\mathrm{T}(\mathrm{n})} \mathrm{D}^{3}$, a cubic non-linearity, the describing function is:

$$
\begin{aligned}
&\left\{\beta^{\mathrm{T}} \cdot \mathrm{D}\right\}=\sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})} \cdot\left(\mathrm{D}_{1} \cdot \sin (\omega \mathrm{t})-\mathrm{D}_{1} \cdot\left(\operatorname{Desc}_{\mathrm{i}}^{1}\left(\mathrm{D}_{1}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (\omega \mathrm{t})+\operatorname{Desc}_{\mathrm{i}}^{3}\left(\mathrm{D}_{1}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (3 \omega \mathrm{t})+...+\operatorname{Desc}_{\mathrm{i}}^{\mathrm{n}}\left(\mathrm{D}_{1}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (\mathrm{n} \omega \mathrm{t})\right)\right)+\\
&\sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})} \cdot\left(\mathrm{D}_{3} \cdot \sin (3 \omega \mathrm{t})-\mathrm{D}_{3} \cdot\left(\operatorname{Desc}_{\mathrm{i}}^{1}\left(\mathrm{D}_{3}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (3 \omega \mathrm{t})+\operatorname{Desc}_{\mathrm{i}}^{3}\left(\mathrm{D}_{3}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (9 \omega \mathrm{t})+...+\operatorname{Desc}_{\mathrm{i}}^{\mathrm{n}}\left(\mathrm{D}_{3}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (3 \mathrm{n} \omega \mathrm{t})\right)\right)+...+\quad \cdot(21) \\
&\sum_{\mathrm{i}=1}^{\mathrm{n}-1} \beta^{\mathrm{T}(\mathrm{i})} \cdot\left(\mathrm{D}_{\mathrm{n}} \cdot \sin (\mathrm{n} \omega \mathrm{t})-\mathrm{D}_{\mathrm{n}} \cdot\left(\operatorname{Desc}_{\mathrm{i}}^{1}\left(\mathrm{D}_{\mathrm{n}}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (\mathrm{n} \omega \mathrm{t})+\operatorname{Desc}_{\mathrm{i}}^{3}\left(\mathrm{D}_{\mathrm{n}}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin (3 \mathrm{n} \omega \mathrm{t})+...+\operatorname{Desc}_{\mathrm{i}}^{\mathrm{n}}\left(\mathrm{D}_{\mathrm{n}}, \frac{\mathrm{e}_{\mathrm{rc}}^{\mathrm{i}}}{\beta^{\mathrm{T}(\mathrm{i})}}\right) \cdot \sin \left(\left(\mathrm{n}^{2} \omega \mathrm{t}\right)\right)\right)\right) \\
&+\beta^{\mathrm{T}(\mathrm{n})}\left(\mathrm{D}_{1} \cdot \sin (\omega \mathrm{t})+\mathrm{D}_{3} \cdot \sin (3 \omega \mathrm{t})+...+\mathrm{D}_{\mathrm{n}} \cdot \sin (\mathrm{n} \omega \mathrm{t})\right)+\left(\beta^{\mathrm{T}(\mathrm{n})} \cdot \alpha_{3}\right) \cdot\left(\mathrm{D}_{1} \cdot \sin (\omega \mathrm{t})+\mathrm{D}_{3} \cdot \sin (3 \omega \mathrm{t})+...+\mathrm{D}_{\mathrm{n}} \cdot \sin (\mathrm{n} \omega \mathrm{t})\right)^{3}
\end{aligned}
$$

In the above equation $D_{i}$ is the amplitude of the $i^{\text {th }}$ harmonic term.

### 3.3 Krasnosel'skii and Pokrovskii hysteresis models

Relation to CP, IM and GIM hysteresis models. In several articles⁹⁻¹⁰ a formulation for hysteresis in smart materials was presented that, like the IM and GIM models, was based on the weighted summation of a finite series of basic hysteretic operators relating input to output. A specific form of the generalized play operator of Krasnosel'skii and Pokrovskii was employed as the kernel function. This operator, denoted the KP operator, possesses invertability and can be identified experimentally. A weighted version of the kernel function applied to piezoceramics is given by the following equation and is depicted in Fig. 7.

$$\mathrm{E}=\mathrm{KP}\left\{\beta^{\mathrm{T}} \mathrm{D}\right\},\tag{22}$$

with

$$
\mathrm{KP}\left\{\beta^{\mathrm{T}} \mathrm{D}\right\}=\left\{
\begin{array}{cc}
1 / 2 \beta^{\mathrm{T}}\left(\alpha_{2}-\alpha_{1}\right) & \mathrm{u}>\alpha_{2} \\
\max \left\{\mathrm{u}_{\mathrm{p}}, \beta^{\mathrm{T}}\left(\mathrm{u}-1 / 2\left[\alpha_{1}+\alpha_{2}\right]\right)\right\} & \dot{\mathrm{u}}>0, \alpha_{1}-\mathrm{w}<\mathrm{u}<\alpha_{2} \\
\min \left\{\mathrm{u}_{\mathrm{p}}, \beta^{\mathrm{T}}\left(\mathrm{u}+\mathrm{w}-1 / 2\left[\alpha_{1}+\alpha_{2}\right]\right)\right\} & \dot{\mathrm{u}}<0, \alpha_{1}-\mathrm{w}<\mathrm{u}<\alpha_{2} \\
-1 / 2 \beta^{\mathrm{T}}\left(\alpha_{2}-\alpha_{1}\right) & \mathrm{u}<\alpha_{1}-\mathrm{w}
\end{array}
\right..\tag{23}
$$

Here, $u_p$ refers to the previous value of u and "max" and "min" indicate that the maximum or minimum of the two values in the bracket should be used, respectively. A hysteresis model based on a finite linear summation of these operators, with different $\alpha_{1(\mathrm{i})}$, $\alpha_{2(\mathrm{i})}$, $\beta^{\mathrm{T}(\mathrm{i})}$ and $\mathrm{w}_{\mathrm{i}}$ values is referred to as a discretized KP model. Such a model satisfies wiping out and congruency and consequently is a classical Preisach model (CPM). The Preisach weighting function and Everett function for a single KP kernel are shown in Fig. 8; the Preisach weighting function is:

$$\mu(\mathrm{x}, \mathrm{y})=\frac{1}{2} \beta^{\mathrm{T}(1)} \delta\left[\mathrm{x}-\mathrm{y}-\mathrm{w}_{1}\right] \mathrm{H}\left[\mathrm{x}_{2}-\mathrm{x}\right] \mathrm{H}\left[\mathrm{x}-\mathrm{x}_{1}\right].\tag{24}$$

![](./images/812376298885218304_9.jpg)

Fig. 7. Input – output relation for the KP hysteresis operator.

![](./images/812376298885218304_10.jpg)

Fig. 8. Functional relationships of classic Preisach representation of KP hysteresis model. a) Weighting function $\mu(\mathrm{x}, \mathrm{y})$. b) Everett function $\mathrm{F}(\mathrm{x}, \mathrm{y})$ based on first order transition curves.

Note that there are similarities between this model and the IM and GIM models. Indeed, an IM elasto-slide element can be constructed from two elementary KP kernels. Consider eq. (4a) with n = 2 valid for $-\mathrm{y}_{\min }<\mathrm{D}<\mathrm{x}_{\max }$. This is equivalent to:

$$\mathrm{KP}_{\mathrm{r}}\left\{\left(\beta^{\mathrm{T}(1)}+\beta^{\mathrm{T}(2)}\right) \mathrm{D}\right\}-\mathrm{KP}\left\{\beta^{\mathrm{T}(1)} \mathrm{D}\right\},\tag{25}$$

where $\alpha_{2}=\mathrm{x}_{\max }, \alpha_{1}-\mathrm{w}=-\mathrm{y}_{\min }$, and for $\mathrm{KP}_{\mathrm{r}}, \mathrm{w}=0$, while for KP, $\mathrm{w}=2 \mathrm{e}_{\mathrm{rc}} / \beta^{\mathrm{T}(1)}$. Also, an equivalent to the basic element of the GIM can be formed from a single KP kernel in parallel with a reversible nonlinear function. Now consider eq. (4a) with $\mathrm{n}=2, \mathrm{f}(\mathrm{D})=\beta^{\mathrm{T}(2)}\left\lfloor\alpha_{2} \mathrm{D}^{2}+\alpha_{3} \mathrm{D}^{3}+\alpha_{4} \mathrm{D}^{4}+...\right\rfloor$ valid for $-\mathrm{y}_{\min }<\mathrm{D}<\mathrm{x}_{\max }$. This is equivalent to:

$$\mathrm{KP}_{\mathrm{r}}\left\{\left(\beta^{\mathrm{T}(1)}+\beta^{\mathrm{T}(2)}\right) \mathrm{D}\right\}-\mathrm{KP}\left\{\beta^{\mathrm{T}(1)} \mathrm{D}\right\}+\mathrm{f}(\mathrm{D}).\tag{26}$$

So, like the GIM, this modified KP model can have as a "backbone" curve any continuous reversible 1 to 1 mapping function. Beyond this though, the domain of hysteresis relationships that can be modeled using the KP operator is broader than that of the IM or GIM as defined above in Section 3.2. The KP operator can be used to represent a wider range of variations on the Preisach triangle / Everett plane in that lines parallel to $\mathrm{x}=\mathrm{y}$ throughout the Preisach triangle can be multi-valued. But then, such a variation can be achieved with a modified IM model if the input – output relation indicated in Fig. 4b was altered such that it is a 1 to 1 mapping when the input lied outside of some values $\alpha_{1}-\mathrm{w}$ and $\alpha_{2}$.

### 3.4 The Jiles–Atherton–Smith Hysteresis Model

Description and relation to other hysteresis models. In recent reports by Smith et al. $^{11-12}$, the Jiles-Atherton (JA) differential model for hysteresis in magnetism has been adapted to ferroelectric and piezoelectric materials. This Jiles-Atherton-Smith (JAS) model, as it is referred to here, like its counterpart the JA model, is developed from a substantially more physics-based argument as opposed to the CP, IM and KP models described above, which are more phenomenological. In Smith's adaptation, instead of electric displacement D, the scaler dielectric relationship is formulated in terms of electric polarization P along with electric field E:

$$
\begin{align}
\mathrm{E}_\mathrm{e} = \mathrm{E} + \alpha\mathrm{P}_\mathrm{irr}, \quad \mathrm{P}_\mathrm{an} = \mathrm{P}_\mathrm{s}\tanh(\mathrm{E}_\mathrm{e}/\mathrm{a}) \text{ or } \mathrm{P}_\mathrm{s}[\coth(\mathrm{E}_\mathrm{e}/\mathrm{a}) - \mathrm{a/E}_\mathrm{e}], \quad \mathrm{P}_\mathrm{rev} = \mathrm{c(P}_\mathrm{an} - \mathrm{P}_\mathrm{irr}), \tag{27a-c} \\
\mathrm{P} = \mathrm{P}_\mathrm{rev} + \mathrm{P}_\mathrm{irr}, \quad \frac{\mathrm{dP}_\mathrm{irr}}{\mathrm{dE}} = \overline{\delta}\frac{\mathrm{P}_\mathrm{an} - \mathrm{P}_\mathrm{irr}}{\mathrm{k}\delta - \alpha(\mathrm{P}_\mathrm{an} - \mathrm{P}_\mathrm{irr})}, \tag{27d-e}
\end{align}
$$

where

$$
\overline{\delta} =
\begin{cases}
1 & (\mathrm{P}_\mathrm{an} - \mathrm{P}_\mathrm{irr})/[\mathrm{k}\delta - \alpha(\mathrm{P}_\mathrm{an} - \mathrm{P}_\mathrm{irr})]>0 \\
0 & \text{otherwise}.
\end{cases}
\quad \text{and } \delta \equiv \text{sign}[\mathrm{dE}]. \tag{27f}
$$

Here, subscripts "irr", "an", and "rev" denote the irreversible, anhysteretic and reversible portions of the polarization. The constants $\alpha$, a, c, k, and $\mathrm{P}_\mathrm{s}$ that define the model are, for the most part, theoretically related to specific physical quantities: $\alpha$ quantifies the amount of dipole coupling; "a" incorporates thermal effects; c is an empirical parameter assessing the relative importance of the anhysteretic to irreversible behavior; k is a macroscopic average of the energy required to break pinning sites; and, $\mathrm{P}_\mathrm{s}$ is the saturation polarization. Also, Smith et al. $^{12}$ describe how this model, which is symmetric as presented above, can be modified to describe asymmetric behavior by assigning bias values to the polarization $(\mathrm{P}_0)$ and field $(\mathrm{E}_0)$. A means of identifying the five constants based on experimental data is also described$^{12}$.

Due to the differential nature of this model and the use of P instead of D, comparisons with the previously-discussed hysteresis models do not directly follow. Several authors have suggested (but not strictly proven) a relationship between the CP and JA models for magnetic materials$^{22-24}$. Such relationships ought to hold for JAS and CP models for ferroelectric materials. When saturation effects are not present (e.g. at very low field levels), the JA model will generate a Preisach weighting function $\mu$(x,y) that is proportional to the exponential of (y-x)/2k. Thus, lines parallel to the x = y line will have the same value in the Preisach triangle. This suggests that the JA (and possibly JAS) model(s) may be exactly represented in terms of infinite dimensional integral IM or KP models and approximated in terms of finite-dimensional IM or KP models.

But, to the best of the authors' knowledge, it has not been proven in a strict sense that the JA or JAS models satisfy the necessary and sufficient conditions (wiping out and congruency) for them to be considered CP models in the first place, particularly when saturation effects are evident. Specifically, congruency and the closure of minor loops are not strictly guaranteed. (But then, congruency is not a property that is strictly observed in electromagnetic hysteresis studies$^{20}$, for which the JA model was originally formulated). The precise relationship between the JA and JAS models and the CP and other models is material for future study. Perhaps, as one reference point of comparison, it is noted that both the generalized IM and KP models (GIM and GKP) as defined above, like the JA and JAS models, explicitly delineate a reversible, continuous nonlinear backbone curve. However, for the GIM and GKP models this anhysteretic and reversible response curve is essentially decoupled from the hysteretic (irreversible) operators, being linearly summed with them to form the output. But, for the JAS model, the reversible, anhysteretic and irreversible portions of the solution are not linearly separable.

Periodic excitation - response simulation tools. At the present time, the authors have not developed a describing function representation of the JA or JAS hysteresis models. However, other researchers have successfully devised a numerical multi-term harmonic balance representation of the JA model for efficient computational simulations of periodically-excited complex electrical circuits with embedded magnetic elements$^{25}$. This could logically be extended to systems with ferroelectric elements described by the JAS hysteresis model.

## 4. INTEGRATING THE 2-D PZT WAFER INTO THE SMART STRUCTURAL SYSTEM

### 4.1 Constitutive nonlinear equations for a simply-supported plate and hybridly shunted PZT Wafer
The system under consideration is schematically shown in Fig. 9. For the derivation of the equations of motion of the electro-elastic continuum, it is assumed that the transverse displacement w(x,t) is the same for the PZT wafer and plate and that there is perfect bonding between them. The PZT is shunted through a RL circuit (resistance R and inductance L) and driven by a voltage source $V_c(t)$ and a mechanical point force F(t). In order to derive the governing equations, Hamilton's principle can be applied. A detailed derivation can be found in Ozer and Royston²⁶. Here, the results are given:

$$
[\mathbf{M}] \ddot{\mathbf{q}}+[\mathbf{C}] \dot{\mathbf{q}}+[\mathbf{K}] \mathbf{q}+\frac{1}{2} \mathrm{~J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right)\left(\int_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \boldsymbol{\Phi}_{\mathrm{x}}\left.\right|_{\mathrm{x}_{1}} ^{\mathrm{x}_{2}} \mathrm{dy}+\int_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \boldsymbol{\Phi}_{\mathrm{y}}\left.\right|_{\mathrm{y}_{1}} ^{\mathrm{y}_{2}} \mathrm{dx}\right) \frac{\mathrm{Q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}=\mathrm{F}(\mathrm{t}) \boldsymbol{\Phi}\left(\mathrm{x}_{\mathrm{f}}, \mathrm{y}_{\mathrm{f}}\right),
\tag{28}
$$

$$
\begin{aligned}
\mathrm{L} \ddot{\mathrm{Q}}+ & \mathrm{R} \dot{\mathrm{Q}}+\mathrm{h}_{\mathrm{pz}}\left(2 \mathrm{~g}_{31} \mathrm{~h}_{31}\right) \frac{\mathrm{Q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}+\left\{\beta_{33}^{\mathrm{T}} \frac{\mathrm{Q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}\right\} \\
& +\frac{1}{2} \mathrm{~J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right)\left(\int_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \boldsymbol{\Phi}_{\mathrm{x}}^{\mathrm{T}}\left.\right|_{\mathrm{x}_{1}} ^{\mathrm{x}_{2}} \mathrm{dy}+\int_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \boldsymbol{\Phi}_{\mathrm{y}}^{\mathrm{T}}\left.\right|_{\mathrm{y}_{1}} ^{\mathrm{y}_{2}} \mathrm{dx}\right) \frac{\mathbf{q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}=\mathrm{V}_{\mathrm{c}}(\mathrm{t})
\end{aligned},
\tag{29}
$$

$$
\text{where } \mathrm{J}_{2}=\frac{1}{2}\left(\left(\frac{\mathrm{h}_{\mathrm{pl}}}{2}+\mathrm{h}_{\mathrm{pz}}\right)^{2}-\left(\frac{\mathrm{h}_{\mathrm{pl}}}{2}\right)^{2}\right), \quad \text{and} \quad \boldsymbol{\Phi}=\left[\sin \left(\frac{\mathrm{m} \pi}{\mathrm{L}_{\mathrm{pl}}} \mathrm{x}\right) \sin \left(\frac{\mathrm{n} \pi}{\mathrm{b}_{\mathrm{pl}}} \mathrm{y}\right)\right], \mathrm{m}, \mathrm{n}=1,2,....
\tag{30a-b}
$$

Here, $\mathbf{q}$ is the vector of generalized displacements and $[\mathbf{M}], [\mathbf{K}]$, and $[\mathbf{C}]$ are finite dimensional mass, stiffness, and damping matrices, respectively for the plate and patch geometry that were obtained using a Rayleigh-Ritz approximation. The electric charge Q is related to the electric displacement D = Q/(x₂-x₁)(y₂-y₁); here, xᵢ and yᵢ define the PZT wafer geometry (Fig. 9). Only equation (29) is nonlinear; but, eqs. (28-29) are coupled. Note that this formulation is independent of which hysteresis function is used to describe dielectric nonlinearity. Clearly also, for periodic excitation / response studies, the above set of equations are easily represented in the frequency domain, if a multi-term describing function or harmonic balance representation of the dielectric hysteresis is available.

### 4.2 Constitutive nonlinear equations for a simply-supported beam and hybridly shunted PZT wafer.
The above equations can be simplified to the case of a simply-supported beam and hybridly shunted PZT wafer if the shape function is not dependent on y. This results in the following set of equations:

$$
[\mathbf{M}] \ddot{\mathbf{q}}+[\mathbf{C}] \dot{\mathbf{q}}+[\mathbf{K}] \mathbf{q}+\mathrm{J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right) \frac{\left[\boldsymbol{\Phi}_{\mathrm{x}}\left(\mathrm{x}_{2}\right)-\boldsymbol{\Phi}_{\mathrm{x}}\left(\mathrm{x}_{1}\right)\right]}{2\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)} \mathrm{Q}=\mathrm{F}(\mathrm{t}) \boldsymbol{\Phi}\left(\mathrm{x}_{\mathrm{f}}\right)
$$

$$
\mathrm{L} \ddot{\mathrm{Q}}_{\mathrm{a}}+\mathrm{R} \dot{\mathrm{Q}}_{\mathrm{a}}+\mathrm{h}_{\mathrm{pz}}\left[\left\{\beta_{33}^{\mathrm{T}} \frac{\mathrm{Q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right) \cdot\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}\right\}+\frac{2 \mathrm{~h}_{31} \mathrm{~g}_{31} \mathrm{Q}}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right) \cdot\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}\right]+\mathrm{J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right) \frac{\left[\boldsymbol{\Phi}_{\mathrm{x}}\left(\mathrm{x}_{2}\right)-\boldsymbol{\Phi}_{\mathrm{x}}\left(\mathrm{x}_{1}\right)\right]^{\mathrm{T}}}{2\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)} \mathbf{q}=\mathrm{V}_{\mathrm{c}}(\mathrm{t})
$$

$$
\text{where} \quad \varphi_{\mathrm{x}}(\mathrm{x})=\left[\sin \left(\mathrm{m} \pi \mathrm{x} / \mathrm{L}_{\mathrm{b}}\right)\right], \mathrm{m}=1,2,....
\tag{31-33}
$$

![](./images/812376298885218304_11.jpg)

Fig. 9. Simply-supported plate with hybridly-shunted PZT.

<table>
<tbody>
<tr>
<td colspan="6">Isotropic steel plate: $\rho_{pl}=7800$ kg/m³, $v_{pl}=0.3$, $E_{pl}=2x10^{10}$ N/m²<br>Plate dimensions (mm): $L_{pl}=560$, $b_{pl}=270$, $h_{pl}=1.5$<br>PZT 5-H: $\rho_{pz}=7800$ kg/m³, $v_{pz}=0.4$, $E_{pz}=1x10^{11}$ N/m²,<br>$g_{31}=-10.1x10^{-3}$ volt-m/N, $h_{31}=-1.35x10^{9}$ volt/m<br>PZT dimensions (mm): $L_{pz}=b_{pz}=72.4$, $h_{pz}=0.267$<br>PZT position (mm): $x_1=27.3$, $x_2=99.7$, $y_1=10$, $y_2=82.4$<br>Forcing position (mm): $x=250$, $y=50$<br>Measurement position (mm): $x_m=279.4$, $y_m=133.3$</td>
</tr>
<tr>
<td>$\beta_{33}^{T(i)} × 10^{-6}$</td>
<td colspan="5">3.0868, 2.3188, 1.8356, 1.418, 16.7796</td>
</tr>
<tr>
<td>$e_{rc}^{(i)}$ (n = 5)</td>
<td colspan="5">0.8996, 1.3515, 1.6048, 1.6529, $\infty$</td>
</tr>
<tr>
<td>Mode</td>
<td>Nat. Freq.</td>
<td>Damp. rat.</td>
<td>L* (Henry)</td>
<td colspan="2">R* (Ohm)</td>
</tr>
<tr>
<td>1,1</td>
<td>61.04</td>
<td>0.0061</td>
<td>19.07</td>
<td colspan="2">370</td>
</tr>
<tr>
<td>2,1</td>
<td>94.02</td>
<td>0.0021</td>
<td>8.07</td>
<td colspan="2">393</td>
</tr>
<tr>
<td>3,1</td>
<td>152.55</td>
<td>0.0017</td>
<td>3.07</td>
<td colspan="2">342</td>
</tr>
</tbody>
</table>

Table 1. Example case parameter values.

## 5. EFFECT OF HYSTERESIS ON THE PASSIVE AND HYBRID SMART STRUCTURE

Theoretical developments in the previous sections lay the framework to investigate nonlinearity in passive and hybrid structural vibration control scenarios. First, vibration control is considered using a passive electrical shunt. Optimization of the shunting circuit parameters is accomplished based on an assumption of linearity. Then, the effect of the nonlinearity is investigated via the developed model, using the IM hysteresis model that was experimentally identified for a PZT-5H wafer⁶, under the assumption that the wafer is isotropic within the wafer plane ("1" and "2" directions with identical properties). Next, the optimal hybrid (active source + passive shunt) control scheme is devised, again based on the underlying assumption of linearity; performance under nonlinear conditions is then considered.

### 5.1 Passive system optimization
The nonlinear hysteretic operator is ignored in eq. (29) and dielectric impermeability is assumed linear. The optimally tuned inductance and resistive value are then given by:

$$
\mathbf{L}^{*}=[\mathbf{K}]^{-1}[\mathbf{M}] \frac{\mathrm{h}_{\mathrm{pz}}\left(\beta_{33}^{\mathrm{T}}+2 \mathrm{~h}_{31} \mathrm{~g}_{31}\right)}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}, \mathbf{R}^{*}=\sqrt{[\mathbf{K}]^{-1}[\mathbf{M}] \frac{\mathrm{h}_{\mathrm{pz}}\left(\beta_{33}^{\mathrm{T}}+2 \mathrm{~h}_{31} \mathrm{~g}_{31}\right)}{\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)} \frac{\mathrm{J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right)\left(\int_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \boldsymbol{\Phi}_{\mathrm{x}}^{\mathrm{T}} \mathrm{I}_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \mathrm{dy}+\int_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \boldsymbol{\Phi}_{\mathrm{y}}^{\mathrm{T}} \mathrm{I}_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \mathrm{dx}\right)}{2\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)}}.(34-35)
$$

![](./images/812376298885218304_12.jpg)

Fig. 10. Optimized passive and hybrid control cases. Plate transverse response at $(x_{m}, y_{m})=(0.279,0.133) m$ due transverse disturbance force at $(x, y)=(0.25,0.05) m$. Key:
—— no shunt or active control voltage (open circuit), - -
- - optimized passive LR shunt, — — optimized hybrid case with LR shunt and optimal $V_{c}$.

The optimal shunting parameter values based on equations (34-35) are given in Table 1, along with the specific example case dimensions and physical constants. Typical vibration suppression results with optimal LR circuits were simulated as shown in Fig. 10 for the first mode ($V_{c}=0, f(x,t)≠0$). Here, the disturbance excitation is harmonic and what is shown is the system response using a single-term describing function representation of the IM hysteresis. For the lower disturbance amplitude, the nonlinear system response matches that predicted by the linearized system. But, as the disturbance amplitude increases, the nonlinear system response changes and the electrical shunt circuit becomes less effective in attenuating the resonant response.

### 5.2 Hybrid system optimization
Next active-passive (hybrid) vibration control was considered for the case of a harmonic point disturbance in the vicinity of the first mode of vibration. The optimal control voltage can be determined based on an assumption of linearity. Referring to equations (28-29), $q_{1}$, the first modal displacement can theoretically be kept at zero if the voltage amplitude is set to the following, where F is the amplitude of the force disturbance:

$$
\mathrm{V}_{\mathrm{c}}^{*}=\mathrm{F}\left(-\mathrm{L} \omega^{2}+\mathrm{j} \omega \mathrm{R}+\mathrm{h}_{\mathrm{p}}\left[\frac{\beta_{33}^{\mathrm{T}}+2 \mathrm{~h}_{31} \mathrm{~g}_{31}}{\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)}\right]\right) \bigg/\left(\mathrm{J}_{2}\left(\mathrm{~h}_{31}+\mathrm{g}_{31} \frac{\mathrm{E}_{\mathrm{pz}}}{1-\mathrm{v}_{\mathrm{pz}}}\right)\left(\int_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \Phi_{\mathrm{x}(1)}^{\mathrm{T}} \mathrm{I}_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \mathrm{dy}+\int_{\mathrm{x}_{1}}^{\mathrm{x}_{2}} \Phi_{\mathrm{y}(1)}^{\mathrm{T}} \mathrm{I}_{\mathrm{y}_{1}}^{\mathrm{y}_{2}} \mathrm{dx}\right) \bigg/ 2\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)\left(\mathrm{y}_{2}-\mathrm{y}_{1}\right)\bigg). \quad(36)
$$

Fig. 10 compares the response of the nonlinear system simulation for the case of no shunting, optimized passive shunting only, and the hybrid system with optimized passive shunting and an active control voltage. For the lowest force disturbance amplitude, the responses match those predicted by a linearized simulation. But again, due to the inherent piezoceramic nonlinearity, there is diminished performance of the hybrid control system as the disturbance amplitude increases.

## 6. CONCLUSION

In this study, different hysteresis models that have been applied to piezoelectric transducers, including those based on Preisach, Jiles-Atherton and Ishlinskii concepts, were reviewed. Relationships between these and other models, new experimental identification schemes and multi-term describing function representations of some of them were developed, with particular emphasis on the Ishlinskii-type models. Then, system equations that incorporate the hysteretic behavior were presented for two pedagogical smart structural systems: a passively shunted / actively driven PZT wafer on (1) a simply supported thin plate and (2) a simply supported thin beam. The adverse effect of PZT hysteresis on optimized passive and hybrid vibration control strategies was demonstrated for the simply-supported plate configuration.


## ACKNOWLEDGEMENTS

The research support of the National Science Foundation [Grant # 9733565, Project monitor: A. Flatau] and the Office of Naval Research [Grant # N00014-99-1-0342, Project monitor: L. Couchman] is acknowledged.

## REFERENCES

1.  D. Hughes and J. T. Wen, "Preisach modeling of piezoceramic and shape memory alloy hysteresis," *Smart Materials and Structures*, **6**, pp. 287 – 300, 1997.
2.  P. Ge and M. Jouaneh, "Tracking control of a piezoceramic actuator," *IEEE Trans. on Control Systems Technology*, **4**, pp. 209 – 216, 1996.
3.  P. Ge and M. Jouaneh, "Generalized Preisach model for hysteresis nonlinearity of piezoceramic actuators," *Precision Engineering*, **20**, pp. 99 – 111, 1997.
4.  M. Goldfarb and N. Celanovic, "A lumped parameter electromechanical model for describing the nonlinear behavior of piezoelectric actuators," *ASME J. of Dyn. Sys., Meas. and Control*, **119**, pp. 478 – 485, 1997.
5.  T. J. Royston and B. H. Houston, "Modeling and Measurement of Nonlinear Dynamic Behavior in Piezoelectric Ceramics with Application to 1-3 Composites," *J. of the Acous. Soc. of America* **104**, pp. 2814 – 2827, 1998.
6.  S.-H. Lee and T. J. Royston, "Modeling piezoceramic transducer hysteresis in the structural vibration control problem," *J. of the Acous. Soc. of America*, **108**, pp. 2843 – 2855, 2000.
7.  S.-H. Lee, T. J. Royston and G. Friedman, "Modeling and compensation of hysteresis in piezoceramic transducers for vibration control," *J. of Intel. Mat. Sys. and Structures* – accepted, 2001. (Also in *Proc. of ASME IMECE*, AD-59, pp. 11 – 18, 1999)
8.  S.-H. Lee, M. B. Ozer and T. J. Royston, "Hysteresis models for piezoceramic transducers," *J. of Material Processing and Manufacturing Science* – accepted, 2001.
9.  G. Webb, D. Lagoudas, and A. Kurdila, "Hysteresis modeling of SMA Actuators for control applications," *J. of Intel. Mat. Sys. and Structures*, **9**, pp. 432 – 447, 1998.
10. G. Webb, A. Kurdila, and D. Lagoudas, "Adaptive hysteresis model for model reference control with actuator hysteresis," *J. of Guidance, Control, and Dynamics*, **23**, pp. 459 – 465, 2000.
11. R. C. Smith and C. L. Hom, "A domain wall theory for ferroelectric hysteresis," CRSC Technical Report CRSC-TR99-1, 1999.
12. R. C. Smith and Z. Ounaies, "A domain wall model for hysteresis in piezoelectric materials," CRSC Technical Report CRSC-TR99-33, 1999.
13. R. C. Smith and C. L. Hom, "A temperature-dependent constitutive model for relaxor ferroelectrics," CRSC Technical Report CRSC-TR00-26, 2000.
14. R. C. Smith, Z. Ounaies and R. Wieman, "A model for rate-dependent hysteresis in piezoceramic materials operating at low frequencies," CRSC Technical Report CRSC-TR00-02, 2000.
15. D. Damjanovic, "Stress and frequency dependence of the direct piezoelectric effect in ferroelectric ceramics," *J. of Appl. Phys.*, **82**, pp. 1788 – 1797, 1997.
16. T. J. Royston, S.-H. Lee and G. Friedman, "Comparison of Two Rate-Independent hysteresis models with Application to Piezoceramic Transducers," *Proc. of 1999 ASME Design Engineering Technical Conference Symposium on Nonlinear Response of Hysteretic Oscillators*, VIB-8082, ASME, Las Vegas, NV, 1999.
17. I. D. Mayergoyz, *Mathematical Models of Hysteresis*, Springer-Verlag, New York, 1991.
18. G. Miano, C. Serpico and C. Visone, "A new model of magnetic hysteresis, based on stop hysterons: an application to the magnetic field diffusion," *IEEE Trans. on Magnetics*, **32**, pp. 1132 – 1135, 1996.
19. S. Bobbio, G. Miano, C. Serpico and C. Visone, "Models of magnetic hysteresis based on play and stop hysterons," *IEEE Trans. on Magnetics*, **33**, pp. 4417 – 4426, 1997.
20. J. W. Macki, P. Nistri and P. Zecca, "Mathematical models for hysteresis," *SIAM Review*, **35**, pp. 94 – 123, 1993.
21. A. Gelb and W. E. vander Velde, *Multiple Input Describing Functions and Non-Linear System Design*, McGraw-Hill, New York, 1968.
22. M. Pasquale, V. Basso, G. Bertotti, D. C. Jiles and Y. Bi, "Domain-wall motion in random potential and hysteresis modeling," *J. of Appl. Phys.*, **83**, pp. 6497 – 6499, 1998.
23. M. Pasquale, G. Bertotti, D. C. Jiles and Y. Bi, "Application of the Preisach and Jiles-Atherton models to the simulation of hysteresis in soft magnetic alloys," *J. of Appl. Phys.*, **85**, pp. 4373 – 4375, 1999.
24. L. Dupre, R. van Keer and J. A. A. Melkebeek, "Identification of the relation between the material parameters in the Preisach model and in the Jiles-Atherton hysteresis model," *J. of Appl. Phys.*, **85**, pp. 4376 – 4378, 1999.
25. V. Rizzoli, D. Masotti and F. Mastri, "General-purpose analysis of nonlinear circuits containing saturating/hysteretic inductors by the harmonic-balance technique," *IEEE Trans. on Magnetics*, **31**, pp. 2290 – 2303, 1995.
26. M. B. Ozer and T. J. Royston, "Effect of piezoceramic hysteresis on passive and adaptive structural acoustic control of a simply supported plate," *Proc. of 2001 Design Engineering Technical Conference Symposium on Hysteresis in Active and Adaptive Vibration Control*, accepted for publication, ASME, Pittsburgh, PA, 2001.