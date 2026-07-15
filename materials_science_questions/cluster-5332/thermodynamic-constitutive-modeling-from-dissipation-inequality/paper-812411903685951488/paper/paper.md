![](./images/812411903685951488_1.jpg)

Computational Materials Science 15 (1999) 464-482

# A non-linear extension of the additivity rule

T. Réti $^{a,*,1}$, I. Felde $^{b}$

$^{a}$ Department of Materials Science and Technology, Bánki Donát Polytechnic, Nepszinhaz u. 8, 1081 Budapest, Hungary
$^{b}$ Bay Zoltán Institute for Materials Science and Technology, Budapest, Hungary

Received 20 April 1999; accepted 15 July 1999

## Abstract
Starting with the traditional Scheil-Cahn additivity principle, a new phenomenological method has been developed for the prediction of the progress of non-isothermal diffusional transformation processes. It is shown, that by formal generalization of the conventional additivity rule, various types of kinetic differential equations can be derived from the same isothermal kinetic law. This new approach is applied to the derivation of Avrami type generalized kinetic functions. They are suitable for the phenomenological description of anisothermal, diffusion-controlled, transformation processes. First, based on computer simulations, fundamental features of generalized kinetic functions derived from extended additivity principle are discussed. Next, practical feasibility of the approach has been demonstrated by estimating the start of austenite/ferrite transformation (i.e. incubation time) in a hypoeutectoid steel during continuous cooling. © 1999 Elsevier Science B.V. All rights reserved.

Keywords: Additivity principle; Kinetics; Transformation

---

## 1. Introduction
The additivity principle plays a decisive role in many fields of material science, not only in modeling of non-isothermal transformation processes but also in the prediction of damage accumulation of various types involved in fatigue, creep and wear phenomena occurring under non-steady-state conditions. A number of publications verify that it is still in the focus of theoretical research [1-10].

The additivity principle was suggested originally by Scheil to predict the start of diffusion-controlled transformations, i.e. the incubation time under non-isothermal conditions [11]. Later its application was extended to a wide range of transformed fractions [12,13].

During the last few decades, several attempts have been made to predict diffusion-based transformation processes with the use of the additivity concept. However, despite numerous successful applications, it has been reported in a number of studies that in certain cases, considering the required accuracy of estimation, predictions based on the additivity rule are not capable to satisfy the expectations [14-21].

Several authors have pointed out that sometimes there are serious discrepancies between the experimentally observed and calculated progress

---
*Corresponding author. Tel.: +361-314-1438; fax: +361-333-6761.
E-mail address: reti@zeus.banki.hu (T. Réti)
$^{1}$ Formerly Research fellow, with the School of Metallurgy and Materials, The University of Birmingham, UK.

0927-0256/99/$ - see front matter © 1999 Elsevier Science B.V. All rights reserved.
PII: S0927-0256(99)00035-X

![](./images/812411903685951488_2.jpg)

of non-isothermal reactions [17–20]. Calculations carried out by the conventional additivity rule occasionally overestimate or underestimate the measured extent of transformations. In detailed investigations, Hawbolt and his co-authors evaluated experimentally the applicability of the additivity principle with respect to the prediction of incubation times [21]. They compared the calculated and experimentally determined austenite/pearlite transformation starts in carbon steel specimens that have been cooled continuously to ambient temperature and claimed poor agreement even when a wide range of cooling rates were employed.

Starting with a non-linear extension of the classical additivity concept, it is the purpose of this paper to establish a new model and a flexible technique for calculation of incubation times and of progress of diffusion-controlled transformations occuring under non-isothermal conditions. First the general aspects of the conventional and the extended additivity principle are analyzed and discussed. Then the applicability of this new approach to derive Avrami type kinetic functions will be demonstrated by calculated results obtained using computer simulation. It will be shown, that novel types of kinetic differential equations can be generated from the same isothermal kinetic function by using the extended additivity rule. The practical feasibility of the method suggested is illustrated by predicting the start of austenite/ferrite transformation in a hypoeutectoid steel.

## 2. Additivity principle and its basic properties

### 2.1. Traditional Scheil–Cahn additivity rule

The additivity rule is considered as a special algorithm for predicting the non-isothermal transformation (CCT curves) on the basis of known isothermal kinetic data (ITT curves). Strictly speaking, the additivity rule provides a mathematical relationship between the transformations that occur under anisothermal conditions and those that occur at constant temperatures [1,5,8,12].

The concept of the Scheil–Cahn additivity rule is based upon the preliminary assumption that the isothermal kinetic function characterizing the transformation process is already known from theoretical models or measurements. The isothermal kinetic function can be formulated in the general form

$$
F(t,y,T)=0, \tag{1}
$$

where $t$ is the time, $y$ the transformed fraction, $T$ the temperature and $F$ is an appropriately selected real function. It is also supposed that $\mathrm{d}y/\mathrm{d}t$ is positive if $t>0$, and Eq. (1) describes the transformation at every constant temperature $T$ for which $T_{\mathrm{min}}\leqslant T\leqslant T_{\mathrm{max}}$ is fulfilled. We assume, that in the case of constant temperature $T$, and for every positive $y$, the inverse function defined as

$$
t=\tau(y,T) \tag{2}
$$

exists. It follows that the function $\tau(y,T)$ is identical to the isothermal time at which the transformation process has reached a certain fraction of completion $y$ at temperature $T$.

Based on the isothermal time $\tau(y,T)$, the concept of the traditional Scheil–Cahn additivity rule which is extended from the incubation period to the whole range of transformation can be formulated as follows: On changing the temperature $T$ as a function of time $t$, the integral

$$
G(t,y)=\int_{0}^{t} \frac{\mathrm{d}t}{\tau(y,T)} \tag{3}
$$

equals unity in that time $t=t_{\mathrm{f}}$ when the fraction transformed reaches the preselected $y$ i.e. $G(t_{\mathrm{f}},y)=1$. In Eq. (3), the function $G$ is referred to as the accumulation function. It is a non-negative monotone increasing function of time for every $y>0$.

To predict the onset of transformation under non-isothermal conditions, the simplified form of Eq. (3) given as

$$
G(t)=\int_{0}^{t} \frac{\mathrm{d}t}{\tau_{\mathrm{in}}(T)} \tag{4}
$$

should be used where $\tau_{\mathrm{in}}(T)$ is the isothermal incubation time. It should be pointed out that Eq. (4) is considered as a special case of Eq. (3), because $\tau_{\mathrm{in}}(T)=\tau(y=0,T)$ by definition.

### 2.2. Relationship between the additivity rule and the semi-additive kinetic differential equations

Besides the additivity rule, there exists another general model for predicting non-isothermal transformation processes. This second type of prediction model relies on the construction of a so-called semi-additive kinetic differential equation which is also generated from a known isothermal kinetic function [22-24]. Because there is a strong correspondence between this second one and the adddtivity rule, analysis of the similarities and differences which are characteristic for the two different concepts of prediction cannot be avoided.

A kinetic differential equation is said to be semi-additive (or autonomous) if it has the form

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=h(y, T). \tag{5}
$$

As it can be seen, the special characteristic of Eq. (5) is that the instantaneous transformation rate is solely a function of the fraction transformed and the transformation temperature.

The semi-additive kinetic differential equation used for prediction purposes is defined as

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=-\frac{\left.\partial F / \partial t\right|_{t=\tau(y, T)}}{\left.\partial F / \partial y\right|_{t=\tau(y, T)}}=\frac{1}{\partial \tau(y, T) / \partial y}. \tag{6}
$$

Analyzing the relationship between the additivity rule and the differential equation (6), the following statement can be proven [2,4,8,13]. Theoretically, the solution of semi-additive differential equation (6) and the use of the additivity rule represented by Eq. (3) lead to identical results if and only if, Eq. (6) can be written in the following factorized form:

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=K_{\mathrm{A}}(T) h_{\mathrm{A}}(y). \tag{7}
$$

Differential equations which can be represented by Eq. (7) are called additive. The main property of additive differential equations is that they are separable with respect to $T$ and $y$. According to the definitions stated above, every additive kinetic differential equation is semi-additive. This means that additive differential equations are a subset of the wider class of semi-additive differential equations. It is easy to verify, that from an isothermal kinetic function represented by Eqs. (1) or (2), an additive kinetic differential equation can be generated only if the equalities

$$
F(t, y, T)=F_{\mathrm{B}}(y)-K_{\mathrm{B}}(T) t=0 \tag{8}
$$

and

$$
\tau(y, T)=\tau_{1}(y) \tau_{2}(T) \tag{9}
$$

are fulfilled.

In order to demonstrate the difference and the similarity between the two models of prediction, consider the following isothermal kinetic function generated from the Avrami's transformation theory [13,25,26]:

$$
y(t)=1-\exp \left\{-\left[K_{1}(T) t^{m_{1}}+K_{2}(T) t^{m_{2}}\right]\right\}. \tag{10}
$$

In Eq. (10) exponents $m_{1}$ and $m_{2}$ are positive constants, $K_{1}$ and $K_{2}$ are temperature-dependent positive functions determined primarily by the nucleation and growth rates of nucleated phases.

In the special case of 3-dimesional nucleation, $m_{1}=3$ and $m_{2}=4$. For spherical crystals with radii growing at a constant rate $G(T)$, functions $K_{1}$ and $K_{2}$ are defined as

$$
K_{1}(T)=\frac{4 \pi}{3} N_{0}(T) G^{3}(T) \tag{11}
$$

and

$$
K_{2}(T)=\frac{\pi}{3} I(T) G^{3}(T), \tag{12}
$$

respectively. In Eqs. (11) and (12), $N_{0}$ is the number of preexisting nuclei per unit volume at time $t=0$, and $I(T)$ is the temperature-dependent nucleation rate per unit volume.

It follows from the formulae listed above, that although inverse function $\tau(y, T)$ exists, it cannot be generated from Eq. (10) in a closed form. Nevertheless, for an arbitrary time-temperature function, differential equation (6) constructed on the basis of Eq. (10) can be solved by a numerical method based on the so-called recursive algorithm [27].

The inverse function $\tau(y, T)$ can be directly generated from Eq. (10), if we assume that $m_{1}=m$ and $m_{2}=2 m$, where $m$ is a positive constant. In this case, we have

$$
\tau(y, T)=\left\{\frac{1}{2 K_{2}}\left[\sqrt{K_{1}^{2}+4 K_{2} \ln \frac{1}{1-y}}-K_{1}\right]\right\}^{1 / m}.
\tag{13}
$$

Based on the use of Eqs. (13) and (6), the following kinetic differential equation can be constructed:

$$
\begin{aligned}
\frac{\mathrm{d} y}{\mathrm{~d} t}= & m(1-y) \sqrt{K_{1}^{2}+4 K_{2} \ln \frac{1}{1-y}} \\
& \times\left\{\frac{1}{2 K_{2}}\left[\sqrt{K_{1}^{2}+4 K_{2} \ln \frac{1}{1-y}}-K_{1}\right]\right\}^{1-1 / m}. \quad(14)
\end{aligned}
$$

As can be stated from Eqs. (13) and (14) this differential equation is semi-additive. Consequently, the additivity rule based on the use of Eq. (13) and the kinetic differential equation (14) will result in different transformed fractions when predicting the non-isothermal transformation process. However, by applying the simplifying assumptions $N_{0}=0$ and $n=2 m$, we have from Eq. (13) as a special case

$$
\tau(y, T)=\left\{\frac{\ln [1 /(1-y)]}{K_{2}(T)}\right\}^{1 / n}. \tag{15}
$$

From this the following kinetic differential equation can be generated:

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=n K_{2}^{1 / n}(1-y)\left[\ln \frac{1}{1-y}\right]^{1-1 / n}. \tag{16}
$$

In practice, Eq. (16) obtained as a special case from differential equation (14) is extensively used for predicting anisothermal diffusion-controlled transformations of various types [2,4,8,9,19,24,27-30].

It is important to note, that due to the simplifying assumption of $N_{0}=0$, differential equation (16) becomes additive. This implies that the additivity rule involving the use of Eq. (15) and the solution of the differential equation (16) will furnish the same results of prediction.

### 2.3. Linearity as a fundamental property of the additivity rule

The conventional additivity principle is characterized by a key property which is termed linearity. The basic concept of linearity can be interpreted on the basis of two-step heat treatment experiments illustrated in Fig. 1. Without any loss of generality, it can be assumed that the transformation process occurs in two consecutive steps at temperatures $T_{\min }$ and $T_{\max }$, and the progress of transformations is characterized by two different time-temperature functions denoted by $T_{\mathrm{a}}(t)$ and $T_{\mathrm{b}}(t)$, respectively. Define the corresponding temperature functions over the time interval $\left[0, t_{\mathrm{f}}\right]$ as follows:

$$
T_{\mathrm{a}}(t)= \begin{cases}T_{\max } & \text { if } 3 t_{\mathrm{f}} / 4 \leqslant t<t_{\mathrm{f}}, \\ T_{\min } & \text { otherwise }\end{cases} \tag{17}
$$

![](./images/812411903685951488_3.jpg)

Fig. 1. Transformation history prediction from results of a two-stepped experiments. (a) Definition of temperature cycles $T_{\mathrm{a}}(t)$ and $T_{\mathrm{b}}(t)$. (b) Corresponding kinetic curves predicted on the basis of additivity principle.

and

$$
T_{\mathrm{b}}(t)= \begin{cases}T_{\max } & \text { if } t_{\mathrm{f}} / 4 \leqslant t<t_{\mathrm{f}} / 2, \\ T_{\min } & \text { otherwise. }\end{cases}
\tag{18}
$$

The transformation paths determined by the corresponding temperature functions are illustrat- ed in Fig. 1a and b. As can be stated, at time $t_{\mathrm{f}}$ the final value of transformed fractions will be iden- tical, that is $y_{\mathrm{f}}=y(t_{\mathrm{f}}, T_{\mathrm{a}})=y(t_{\mathrm{f}}, T_{\mathrm{b}})$, independently of the transformation paths (Fig. 1c). This result follows directly from the additivity rule formulated as

$$
\frac{\Delta t_{\min }}{\tau(y_{\mathrm{f}}, T_{\min })}+\frac{\Delta t_{\max }}{\tau(y_{\mathrm{f}}, T_{\max })}=1,
\tag{19}
$$

where $\Delta t_{\min }=3 t_{\mathrm{f}} / 4$ is the time spent at tempera ture $T_{\min }$, $\Delta t_{\max }=t_{\mathrm{f}} / 4$ is the time spent at temper ature $T_{\max }$, while $\tau(y_{\mathrm{f}}, T_{\min })$ and $\tau(y_{\mathrm{f}}, T_{\max })$ are the corresponding isothermal times to reach reaction fraction $y_{\mathrm{f}}$ at temperatures $T_{\min }$ and $T_{\max }$, respec tively. From the previous considerations it follows that the linearity of the additivity rule means that the final value of reaction fraction depends only on the temperature amplitude spectrum, and inde- pendent of the order of infinitesimal isothermal periods of time. This concept can be readily ex- tended to any arbitrary time-temperature function $T_{\mathrm{x}}(t)$. To do this, introduce a so-called temperature distribution function $\Lambda(T, t_{\mathrm{f}})$ defined as

$$
\Lambda(T, t_{\mathrm{f}})= \begin{cases}0 & \begin{array}{l}
\text { if } T \leqslant T_{\min } \text { and } \\
0<t \leqslant t_{\mathrm{f}},
\end{array} \\
\frac{1}{t_{\mathrm{f}}} \int_{T_{\mathrm{x}}(t) \leqslant T} \mathrm{~d} t & \begin{array}{l}
\text { if } T_{\min }<T \leqslant T_{\max } \text { and } \\
0<t \leqslant t_{\mathrm{f}},
\end{array} \\
1 & \begin{array}{l}
\text { if } T>T_{\max } \text { and } \\
0<t \leqslant t_{\mathrm{f}},
\end{array}
\end{cases}
\tag{20}
$$

where $0<t_{\mathrm{f}} \leqslant t_{\mathrm{F}}$. From this definition it follows that for every fixed time $t_{\mathrm{f}}$, equation $\Lambda(T, t_{\mathrm{f}})$ represents a non-negative monotone increasing function of $T$. Function $\Lambda(T, t_{\mathrm{f}})$ characterizes unambiguously the temperature function $T_{\mathrm{x}}(t)$ in $[0, t_{\mathrm{F}}]$ and satisfies the equality

$$
\int_{T_{\min }}^{T_{\max }} \mathrm{d} \Lambda(T, t_{\mathrm{f}})=1
\tag{21}
$$

for every time $t_{\mathrm{f}}$. The definition and the con struction of temperature distribution functions are illustrated schematically in Fig. 2.

Now, starting with Eq. (20), the additivity rule given by formula (3) can be rewritten in the fol- lowing form

$$
\begin{aligned}
G(t_{\mathrm{f}}, y) & =\int_{0}^{t_{\mathrm{f}}} \frac{\mathrm{d} t}{\tau(y, T)} \\
& =t_{\mathrm{f}} \int_{T_{\min }}^{T_{\max }} \frac{1}{\tau(y, T)} \mathrm{d} \Lambda(T, t_{\mathrm{f}})=1.
\end{aligned}
\tag{22}
$$

![](./images/812411903685951488_4.jpg)

Fig. 2. Schematic diagram illustrating the definition of temperature distribution function. (a) Temperature cycle $T(t)$ defined in the interval $[0, t_{F}]$. (b) Corresponding temperature distribution functions related to times $t=t_{f 1}$ and $t=t_{f 2}$.

Eq. (22) is considered as the general mathematical formulation of linearity attributed to the additivity concept. In fact the integral on the right-hand side is the integral mean value of function $1/\tau(y, T)$ over the interval $[T_{\min}, T_{\max}]$ for every fixed $t_{\mathrm{f}}$.

It must be emphasized that the applicability of formula (22) to predict anisothermal transformations is limited by the fact that the temperature distribution function $\Lambda(T, t_{\mathrm{f}})$ depends also on time $t_{\mathrm{f}}$, therefore it is difficult to estimate it. Consequently, the practical use of Eq. (22) is restricted to calculate the value of reaction fraction $y_{\mathrm{f}}$ at the preselected time $t_{\mathrm{f}}$ only. For computation purposes, Eq. (22) can be used more efficiently in that case, if time-independence of temperature distribution function is assumed. As an example, consider a transformation model describing the growth of a compound layer and assume that this process is represented by the isothermal kinetic function
$$
y(t)=C_{0} t^{C_{1}+C_{2} T}, \tag{23}
$$
where $C_{0}=C_{0}(T)$ is a positive function, $C_{1}$ and $C_{2}$ are positive constants. A special property of kinetic function (23) is that $y \rightarrow \infty$ if time $t$ tends to infinity.

Consider now all the temperature functions which are characterized by a continuous time-independent temperature distribution function defined as
$$
\Lambda_{\mathrm{u}}(T)=\frac{T-T_{\min }}{T_{\max }-T_{\min }}. \tag{24}
$$

As can be seen, $\Lambda_{\mathrm{u}}$ represents a uniform temperature distribution in interval $[T_{\min}, T_{\max}]$. By using the additivity rule, we have
$$
\frac{1}{T_{\max }-T_{\min }} \int_{T_{\min }}^{T_{\max }}\left(\frac{C_{0}}{y}\right)^{1 /\left(C_{1}+C_{2} T\right)} \mathrm{d} T=\frac{1}{t}. \tag{25}
$$

From Eq. (25) the transformation time $t$ as a function of a preselected $y>0$ can be directly computed by means of a numerical method. If the non-isothermal transformation is calculated by using Eq. (25), we have a result which differs theoretically from that predicted by differential equation (6). This is explained by the fact that the differential equation
$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=\left(C_{1}+C_{2} T\right) y\left(\frac{C_{0}}{y}\right)^{1 /\left(C_{1}+C_{2} T\right)} \tag{26}
$$
which is generated from the isotherm kinetic function (23) is not additive (it is only semi-additive). Now, reevaluating the results obtained from the theoretical investigation of two stepped transformation processes, one can observe that temperature functions $T_{\mathrm{a}}(t)$ and $T_{\mathrm{b}}(t)$ given by Eqs. (17) and (18) generate the same temperature distribution function
$$
\Lambda\left(T, t_{\mathrm{f}}\right)=\frac{1}{4} \delta\left(T_{\max }-T\right)+\frac{3}{4} \delta\left(T_{\min }-T\right), \tag{27}
$$
where $\delta$ is the Dirac delta function (see Fig. 1). Since the corresponding temperature distribution functions are identical, the final reaction fractions predicted at time $t_{\mathrm{f}}$ will be also identical, independent of the preliminary thermal history.

From Eqs. (20) and (21), it follows that temperature functions $T_{i}(t)$ $(i=1,2, \ldots)$ defined over $[0, t_{\mathrm{F}}]$ are considered to be equivalent with respect to time $t_{\mathrm{f}}$, for $0<t_{\mathrm{f}} \leqslant t_{\mathrm{F}}$, if they are all characterized by the same temperature distribution function $\Lambda(T, t_{\mathrm{f}})$. Due to linearity, equivalent temperature functions (with respect to time $t_{\mathrm{f}}$) result in identical reaction fraction $y_{\mathrm{f}}$ at time $t_{\mathrm{f}}$. This is illustrated in Fig. 3. As can be observed, at times $t_{\mathrm{f} 1}$ and $t_{\mathrm{f} 2}$, temperature functions $T_{1}(t)$ and $T_{2}(t)$ have identical temperature distribution functions denoted by $\Lambda_{1}(T_{1}, t_{\mathrm{f} 1})$ and $\Lambda_{2}(T_{2}, t_{\mathrm{f} 2})$, respectively. This implies that, for $T_{1}(t)$ and $T_{2}(t)$, the corresponding reaction fractions calculated by the additivity rule at times $t_{\mathrm{f} 1}$ and $t_{\mathrm{f} 2}$ will be also identical. This is illustrated by the two intersection points of the corresponding kinetic curves in Fig. 3c. From previous considerations it is clear that by using the additivity rule, temperature functions with the same temperature distribution function will produce identical reaction fraction $y_{\mathrm{f}}$ at time $t_{\mathrm{f}}$. It can be shown that the converse of this statement is not true. One can easily construct various temperature cycles characterized by non-identical temperature distribution functions which also result in the same reaction fraction $y_{\mathrm{f}}$ at time $t_{\mathrm{f}}$.

As it can be concluded, when predicting the transformation taking place at varying

![](./images/812411903685951488_5.jpg)

Fig. 3. Transformation history prediction based on the use of additivity principle. (a) Definition of piece-wise linear temperature functions $T_{1}(t)$ and $T_{2}(t)$. (b) Corresponding temperature distribution functions $\Lambda_{1}$ and $\Lambda_{2}$ for times $t=t_{f 1}$ and $t=t_{f 2}$. (c) Kinetic curves predicting the progress of transformation for temperature cycle $T_{1}(t)$ and $T_{2}(t)$.

temperature, as a consequence of its linearity, the traditional additivity concept is unable to take into account the complete thermal history. We will

show later that it is possible to generalize the tra- ditional additivity rule in such a way that the lin- earity property can be eliminated.

### 2.4. Additivity rule extended on the basis of state vector concept

It is known that the rate of diffusion-controlled transformation processes are influenced not only by the temperature but by other external parameters (pressure, stress, radiation generated by elementary particles) [31-34]. Inoue and his co-authors have shown that based on the use of an appropriately selected scalar invariant of strength tensor [33,34], the stress field influence on the transformation rate can be directly involved in the classical Avrami model.

The set of parameters which have a decisive effect on the transformation rate can be represented by a state vector given as
$$
\mathbf{T}=\left[T_{1}, T_{2}, \ldots, T_{J}\right]^{\mathrm{t}}. \quad(28)
$$

In accordance with previously outlined considerations, the components of the state vector represent all the possible scalar parameters which can control the progress of the transformation (temperature, pressure, strength, etc.) State vector components are regarded to be continuous functions of time. Consequently, they are represented by a $J$-component vector valued "state-function" $\mathbf{T}(t)$, characterizing unambiguously the path of transformation. Assuming now that $\mathbf{T}$ has constant components, a so-called iso-kinetic function can be defined, which is represented as
$$
F(t, y, \mathbf{T})=0 \quad(29)
$$
or
$$
t=\tau(y, \mathbf{T}). \quad(30)
$$

It is supposed that the inverse function $\tau(y, \mathbf{T})$ exists for every constant $\mathbf{T}$, whose components satisfy the inequalities $T_{\min , j} \leqslant T_{j} \leqslant T_{\max , j}$ for $j=1,2, \ldots, J$. It is obvious that Eqs. (29) and (30) are regarded as generalized versions of isothermal kinetic functions defined by Eqs. (1) and (2). By using Eq. (28), the additivity rule can be reformulated in the following form:
$$
G(t, y)=\int_{0}^{t} \frac{\mathrm{d} t}{\tau(y, \mathbf{T})}. \quad(31)
$$

It is easy to verify, that all the fundamental properties of the traditional additivity rule represented by Eqs. (5)-(9) will still be valid if the temperature function $T(t)$ is replaced by the vector valued state function $\mathbf{T}(t)$. Consequently, when predicting the progress of transformation under non-iso-conditions (i.e. applying a time dependent state function), the use of the additivity rule given by Eq. (31) will furnish the same transformed fraction, as the solution of the extended additive differential equation formulated as
$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=K_{\mathrm{A}}(\mathbf{T}) h_{\mathrm{A}}(y). \quad(32)
$$

As far as the problem of linearity is concerned, the property of linearity will also remain valid even in case of introducing an appropriately constructed $J$-dimensional state vector distribution function defined in a way which is traditionally used in the probability theory.

This non-negative distribution function denoted by $\Lambda(\mathbf{T}, t_{\mathrm{f}})$ is defined in the $J$-dimensional Euclidean space. In analogy to Eqs. (20)-(22), for function $\Lambda(\mathbf{T}, t_{\mathrm{f}})$, the following relations are fulfilled
$$
\begin{aligned}
& \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right)=0 \quad \text { if } \mathbf{T} \rightarrow-\infty, \\
& \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right)=1 \quad \text { if } \mathbf{T} \rightarrow+\infty, \\
& \int_{R_{J}} \mathrm{~d} \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right)=1
\end{aligned}
$$
and
$$
G\left(t_{\mathrm{f}}, y\right)=t_{\mathrm{f}} \int_{R_{J}} \frac{1}{\tau(y, \mathbf{T})} \mathrm{d} \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right)=1,
$$
where $R_{J}$ stands for the $J$-dimensional Euclidean vector space.

Because the integration of differential equation (32) yields
$$
\begin{aligned}
& \int_{0}^{t_{\mathrm{f}}} K_{\mathrm{A}}[\mathbf{T}(t)] \mathrm{d} t=t_{\mathrm{f}} \int_{R_{J}} K_{\mathrm{A}}(\mathbf{T}) \mathrm{d} \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right) \\
& \quad=t_{\mathrm{f}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} K_{\mathrm{A}}\left(T_{1}, T_{2}, \ldots, T_{J}\right) \mathrm{d} \Lambda\left(T_{1}, T_{2}, \ldots, T_{J}, t_{\mathrm{f}}\right)
\end{aligned}
$$
the solution of differential equation (32) can be written as
$$
\begin{aligned}
y\left(t_{\mathrm{f}}\right) & =H^{\mathrm{inv}}\left\{\int_{0}^{t_{\mathrm{f}}} K_{\mathrm{A}}[\mathbf{T}(t)] \mathrm{d} t\right\} \\
& =H^{\mathrm{inv}}\left\{t_{\mathrm{f}} \int_{R_{J}} K_{\mathrm{A}}(\mathbf{T}) \mathrm{d} \Lambda\left(\mathbf{T}, t_{\mathrm{f}}\right)\right\},
\end{aligned}
$$

where $H^{\text{inv}}$ stands for the inverse of function $H(y)$ represented by
$$
H(y)=\int_{0}^{y} \frac{1}{h_{\mathrm{A}}(y)} \mathrm{d} y
\tag{37}
$$
provided that this inverse function exists.

It is worth noting that the integral in Eq. (35) can be easily computed, if $\Lambda(\mathbf{T}, t_{\mathrm{f}})$ can be generated in the factorized form
$$
\Lambda(\mathbf{T}, t_{\mathrm{f}})=\prod_{j=1}^{J} \Lambda_{j}\left(T_{j}, t_{\mathrm{f}}\right).
\tag{38}
$$

### 2.5. A probabilistic interpretation of the additivity principle
Due to the definition of the distribution function $\Lambda(\mathbf{T}, t_{\mathrm{f}})$, and taking into consideration its properties involved in Eqs. (33) and (34), the state vector can be interpreted on the basis of the probability theory for vector valued random variables [35]. Assuming that state vector components are random variables $\eta_{j} \ (j=1,2, \ldots, J)$ and they are represented by a $J$-dimensional random vector
$$
\boldsymbol{\eta}=\left[\eta_{1}, \eta_{2}, \ldots, \eta_{J}\right]^{\mathrm{t}}
\tag{39}
$$
this probabilistic approach implies that Eqs. (34) and (35) can be rewritten in the form
$$
G\left(t_{\mathrm{f}}, y\right)=t_{\mathrm{f}} M\left[\frac{1}{\tau(y, \eta)}, t_{\mathrm{f}}\right]=1
\tag{40}
$$
and
$$
\int_{0}^{t_{\mathrm{f}}} K_{\mathrm{A}}[\mathbf{T}(t)] \mathrm{d} t=t_{\mathrm{f}} M\left[K_{\mathrm{A}}(\eta), t_{\mathrm{f}}\right],
\tag{41}
$$
where $M[X, t_{\mathrm{f}}]$ denotes the mean of a random function $X$ for $t_{\mathrm{f}} \in[0, t_{\mathrm{F}}]$. Eq. (40) is regarded as the probabilistic formulation of the additivity principle.

As a consequence of Eqs. (36) and (40), we have
$$
y\left(t_{\mathrm{f}}\right)=H^{\mathrm{inv}}\left\{t_{\mathrm{f}} M\left[K_{\mathrm{A}}(\eta), t_{\mathrm{f}}\right]\right\}.
\tag{42}
$$

This formula makes it possible to assess the influence of random noises generated by random state vector components (for example, noises caused by temperature oscillations) on the accuracy of predicted reaction fractions.

## 3. Generalized additivity rule
By eliminating the property of linearity, the formula representing the traditional additivity rule can be generalized in the form
$$
G(t, y)=\int_{0}^{t} W\left(t_{\mathrm{u}}, \mathbf{T}, \dot{\mathbf{T}}\right) \frac{S t_{\mathrm{u}}^{s-1}}{[\tau(y, \mathbf{T})]^{s}} \mathrm{~d} t_{\mathrm{u}}.
\tag{43}
$$

In Eq. (43), $S=S(\mathbf{T})$ is an appropriately selected temperature-dependent non-negative real function, and $W=W(t, \mathbf{T}, \dot{\mathbf{T}})$ is a non-negative weighting function for which
$$
\begin{aligned}
& \lim W(t, \mathbf{T}, \dot{\mathbf{T}})=0 \quad \text { if } \dot{\mathbf{T}} \rightarrow-\infty \\
& \lim W(t, \mathbf{T}, \dot{\mathbf{T}})=0 \quad \text { if } \dot{\mathbf{T}} \rightarrow+\infty \\
& W(t, \mathbf{T}, \dot{\mathbf{T}}) \equiv 1 \quad \text { if } \mathrm{d} \mathbf{T} / \mathrm{d} t=\dot{\mathbf{T}}=0
\end{aligned}
\tag{44}
$$
are fulfilled. As a consequence of Eq. (43), the relation between accumulation function $G(t, y)$ and the corresponding transformation rate function $\mathrm{d} y / \mathrm{d} t$ can be represented as
$$
\frac{\partial G}{\partial t}=-\frac{\partial G}{\partial y} \frac{\mathrm{d} y}{\mathrm{~d} t}.
\tag{45}
$$

In the special case when $S(\mathbf{T}) \equiv 1$ and $W(t, \mathbf{T}, \dot{\mathbf{T}}) \equiv 1$, furthermore equality (32) given by $\mathrm{d} y / \mathrm{d} t=K_{\mathrm{A}}(\mathbf{T}) h_{\mathrm{A}}(y)$ is assumed to be valid, from Eq. (45) it follows
$$
-\int_{0}^{t} \frac{\partial G}{\partial y} \frac{\mathrm{d} y}{\mathrm{~d} t} \mathrm{~d} t=1
\tag{46}
$$
for any arbitrary selected $t>0$.

In the following, without loss of generality, it will be assumed that state vector $\mathbf{T}$ has only one component which is identical to the temperature $T$ by definition.

A key property of weighting function $W$ is that it enables to take into account the influence of rate of temperature change on the rate of non-isothermal transformation. It can be defined in several ways. For practical modeling, it can be chosen in the form
$$
W(t, T, \dot{T})= \begin{cases}\exp \{-E|\dot{T}|\} & \text { if }|\dot{T}| \leqslant V_{\max }, \\ 0 & \text { otherwise }\end{cases}
\tag{47}
$$

or more generally
$$
W(t, T, \dot{T})= \begin{cases}\exp \left\{-(E+t \varepsilon)|\dot{T}|\right\} & \text { if }|\dot{T}| \leqslant V_{\max }, \\ 0 & \text { otherwise }\end{cases}
\tag{48}
$$
and
$$
W(t, T, \dot{T})= \begin{cases}1+(E+t \varepsilon)|\dot{T}| & \text { if }|\dot{T}| \leqslant V_{\max }, \\ 0 & \text { otherwise. }\end{cases}
\tag{49}
$$

In Eqs. (47)-(49), $V_{\max }$ is a positive constant, $E$ and $\varepsilon$ are constant or temperature-dependent parameters, $|x|$ stands for the absolute value of variable $x$. As can be stated, if $W(t, T, \dot{T}) \equiv 1$ and $S \equiv 1$ then we have the conventional additivity principle represented by Eq. (3) as a special case.

The most important characteristic of the generalized additivity principle is that its linearity remains valid only in that exceptional case, if $S \equiv 1$ and the temperature function $T(t)$ is assumed to be a piecewise constant function. In any other cases, (when $S(T) \neq 1$ or $W \neq 1$ ) the linearity condition will not be fulfilled.

Due to the elimination of linearity, an important new characteristic feature of the extended additivity concept is obtained, namely it is more sensitive to the thermal history, and able to reflect the influence of thermal path (i.e. the past of the reaction) on the progress of anisothermal transformations in a more adequate manner than the traditional linear additivity principle formulated by either Eqs. (3) or (31).

Considering temperature functions defined by Eqs. (17) and (18) and assuming that $S$ is a positive constant function, it is easy to verify by direct calculations that the predicted non-isothermal reactions for two temperature cycles will result in different transformed fractions at time $t_{\mathrm{f}}$.

From Eq. (43) representing the generalized additivity principle, it is possible to generate the following kinetic differential equation which characterizes the rate of the non-isothermal transformation process
$$
\begin{aligned}
\frac{\mathrm{d} y}{\mathrm{~d} t}= & -\frac{\partial G / \partial t}{\partial G / \partial y}=\frac{W s t^{s-1}}{[\tau(y, T)]^{s}} \\
& \times\left\{\int_{0}^{t} \frac{W s^{2} t_{\mathrm{u}}^{s-1}}{[\tau(y, T)]^{s+1}}\left[\frac{\partial}{\partial y} \tau(y, T)\right] \mathrm{d} t_{\mathrm{u}}\right\}^{-1} . \quad(50)
\end{aligned}
$$

If the isotherm transformation time $\tau(y, T)$ is assumed to be separable with respect to $y$ and $T$, then the solution of differential equation (50) can be easily determined. By using the equality
$$
\tau(y, T)=\tau_{1}(y) \tau_{2}(T)
\tag{51}
$$
differential equation (50) can be transformed to
$$
\begin{aligned}
\frac{\mathrm{d} y}{\mathrm{~d} t}= & W s t^{s-1} \frac{\tau_{1}(y)}{\left[\tau_{2}(T)\right]^{s}} \\
& \times\left\{\left[\frac{\partial}{\partial y} \tau_{1}(y)\right] \int_{0}^{t} \frac{W s^{2} t_{\mathrm{u}}^{s-1}}{\left[\tau_{2}(T)\right]^{s}} \mathrm{~d} t_{\mathrm{u}}\right\}^{-1} .
\end{aligned}
\tag{52}
$$

For further simplification, let us assume that $S$ is a constant function. In that case, Eq. (52) can be reduced to the form
$$
\begin{aligned}
\frac{\mathrm{d} y}{\mathrm{~d} t} & =\frac{W s t^{s-1}}{\left[\tau_{2}(T)\right]^{s}}\left\{\frac{\partial}{\partial y}\left[\tau_{1}(y)\right]^{s}\right\}^{-1} \\
& =\frac{W t^{s-1}}{\left[\tau_{2}(T)\right]^{s}} \frac{\left[\tau_{1}(y)\right]^{1-s}}{\partial \tau_{1}(y) / \partial y} .
\end{aligned}
\tag{53}
$$

Because $S$ is taken as constant, it is possible to generate the solution of differential equation (53) in a closed form
$$
\tau_{1}(y)=\left\{\int_{0}^{t} W\left(t_{\mathrm{u}}, T, \dot{T}\right) \frac{s t_{\mathrm{u}}^{s-1}}{\left[\tau_{2}(T)\right]^{s}} \mathrm{~d} t_{\mathrm{u}}\right\}^{1 / s},
\tag{54}
$$
where $\tau_{1}(0)=0$. Assuming that the inverse function $\tau_{1}^{\text {inv }}$ exists, the final solution can be expressed as
$$
y(t)=\tau_{1}^{\mathrm{inv}}\left\{\left[s \int_{0}^{t} W\left(t_{\mathrm{u}}, T, \dot{T}\right) \frac{t_{\mathrm{u}}^{s-1}}{\left[\tau_{2}(T)\right]^{s}} \mathrm{~d} t_{\mathrm{u}}\right]^{1 / s}\right\} .
\tag{55}
$$

As an interesting consequence, we will show that from the differential equation (53) it is easy to derive the MacCallum-Tanner rate equation which represents an alternative formalism to predict non-isothermal reactions [36,37]. To do this, let us assume that the isothermal transformation process can be described by a differential equation defined by formula (32). By solving Eq. (32) we have
$$
\tau_{1}(y)=\int_{0}^{y} \frac{1}{h_{\mathrm{A}}(y)} \mathrm{d} y
\tag{56}
$$

and
$$
\tau_{2}(T)=\frac{1}{K_{\mathrm{A}}}. \tag{57}
$$

Consider now, a weighting function $W$ selected in the following particular form
$$
W(T, \dot{T})=\left[1+q t \frac{\partial \ln K_{\mathrm{A}}(T)}{\partial T} \dot{T}\right], \tag{58}
$$
where $q=q(t, T)$ is a time and temperature-dependent function. Substitute formulae (56)-(58) into differential equation (53) and assuming that $S$ is equal to unity, in that special case, we obtain
$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=\left[1+q \frac{t}{K_{\mathrm{A}}} \frac{\partial K_{\mathrm{A}}}{\partial T} \dot{T}\right] K_{\mathrm{A}}(T) h_{\mathrm{A}}(y). \tag{59}
$$

The resulted semi-additive differential equation (59) is the non-isothermal extension of Eq. (32) according to the MacCallum-Tanner hypothesis [36]. In the case, where $S$ is an arbitrary positive constant, Eq. (55) results in the following general solution
$$
y(t)=\tau_{1}^{\mathrm{inv}}\left\{\left[s \int_{0}^{t}\left[1+q t \frac{\partial \ln K_{\mathrm{A}}}{\partial T} \dot{T}\right] K_{\mathrm{A}}^{s}(T) t_{\mathrm{u}}^{s-1} \mathrm{~d} t_{\mathrm{u}}\right]^{1 / s}\right\}.
\tag{60}
$$

This is regarded as a possible generalized version of the MacCallum-Tanner rate equation.

The major advantage of using Eq. (55) lies in the fact, that it serves as a basis for the generation of novel kinetic equations from known isothermal kinetic laws. Practically, this means that depending on the particular choice of constant parameter $S$ and weight $W$ we are able to derive a series of non-isothermal kinetic equations of various types.

### 4. Derivation of generalized Avrami type kinetic functions

In order to demonstrate the flexibility of the method outlined we have concentrated our study on the most commonly used Avrami kinetic function defined as
$$
y(t)=1-\exp \left[-K t^{n}\right], \tag{61}
$$
where $n$ is the Avrami exponent, and $K=K(T)$ is a temperature-dependent parameter. Starting with the Avrami function (61) and assuming that $n$ is constant, we have
$$
\tau_{1}(y)=[-\ln (1-y)]^{1 / n}, \tag{62}
$$

$$
\tau_{2}(T)=K^{-1 / n}. \tag{63}
$$

Because Eq. (61) can be represented in the form given by Eq. (51) and $S$ is supposed to be constant, from Eq. (53) we have the kinetic differential equation
$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=W(t, T, \dot{T}) n K^{s / n} t^{s-1}(1-y)\left[\ln \frac{1}{1-y}\right]^{1-s / n}
\tag{64}
$$
as a special case. It should be noted, that at constant temperatures, this differential equation will be independent of parameter $S$. In the case of temperature-dependent Avrami exponent, i.e. $n=n(T)$, equality (51) is not fulfilled. This implies that differential equation (53) results in an integrodifferential equation whose practical application to prediction purposes is rather complicated [9].

Taking into consideration that
$$
\tau_{1}^{\mathrm{inv}}(x)=1-\exp \left[-x^{n}\right] \tag{65}
$$
and by using the general formula (55), the solution of Eq. (64) gives
$$
y(t)=1-\exp \left\{-\left[\int_{0}^{t} K_{\mathrm{R}}\left(t_{\mathrm{u}}, T, \dot{T}, s\right) \mathrm{d} t_{\mathrm{u}}\right]^{n / s}\right\},
\tag{66a}
$$
where
$$
K_{\mathrm{R}}(t, T, \dot{T}, s)=s W(t, T, \dot{T}) K^{s / n} t^{s-1} \tag{66b}
$$
by definition. Eq. (66) is referred to as a generalized non-isotherm Avrami kinetic function. Analysis of Eqs. (64) and (66) leads to the following conclusions.

Starting with measured values of $t, y$ and $\mathrm{d} y / \mathrm{d} t$ obtained from non-isothermal experiments, constant $S$ and weight $W$ can be easily estimated, if parameters $n$ and $K$ are already determined from preliminary isothermal investigations. Assuming that $S$ is constant, and $W$ is defined by Eq. (48), then by taking the logarithmic form of differential

equation (64), unknown parameters $S$, $E$ and $\varepsilon$ can be directly calculated by means of a multivariate linear regression analysis of kinetic data measured under non-isothermal conditions.

In order to facilitate the interpretation of parameter $S$ and weight $W$ in Eqs. (64), (66a) and (66b), introduce function $K_{\mathrm{C}}$ defined as follows:

$$
\begin{aligned}
& K_{\mathrm{C}}(t, y, T, \dot{T}, s) \\
& \quad=W(t, T, \dot{T}) K^{1 / n}\left\{\frac{t K^{1 / n}}{[\ln (1 /(1-y))]^{1 / n}}\right\}^{s-1}. \quad(67)
\end{aligned}
$$

Starting with this formula, differential Eq. (64) can be transformed to the form

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=n K_{\mathrm{C}}(1-y)\left[\ln \frac{1}{1-y}\right]^{1-1 / n}. \quad(68)
$$

The main properties of function $K_{\mathrm{C}}$ are as follows:

(i) By definition, $K_{\mathrm{C}}$ is a positive function, which affects the rate of the anisothermal transformation as a multiplying factor. It can be supposed that $K_{\mathrm{C}}$ is determined primarily by the circumstances of nucleation.

(ii) It is obvious that if the temperature is constant, i.e. $\dot{T}=0$ then $K_{\mathrm{C}}$ will be equal to $K^{(1 / n)}$. On the other hand, if $S=1$ then $K_{\mathrm{C}}=W(t, T, \dot{T}) K^{1 / n}$. Finally, if $W \equiv 1$ and $S \equiv 1$ are fulfilled, this implies that $K_{\mathrm{C}} \equiv K^{(1 / n)}$. In that special case, Eq. (68) is simplified to the additive differential equation

$$
\frac{\mathrm{d} y}{\mathrm{~d} t}=n K^{1 / n}(1-y)\left[\ln \frac{1}{1-y}\right]^{1-1 / n} \quad(69)
$$

which is identical to Eq. (16) derived previously from the general isotherm Avrami law. This is the simplest generalization of the Avrami function for non-isotherm conditions [2,4,9,23,24,28]. It is important to emphasize that in any other cases, $K_{\mathrm{C}}$ will depend on time, temperature, temperature rate and actual value of $y$. Hence, differential equation (64) will not be semi-additive.

(iii) Depending on the particular choice of constant $S$, various types of generalized Avrami equations can be derived. As an example, some of them are listed in Table 1.

## 5. Investigations based on computer simulation

To study and analyze the effect of the particular choice of parameter $S$ and weighting function $W$ on the prediction of non-isothermal transformation curves, investigations have been performed by

<table>
<caption>Table 1 Generalized Avrami type kinetic differential equations and their solutions</caption>
<thead>
<tr>
<th>Selected paramter, $s$</th>
<th>Kinetic differntial equation</th>
<th>Generalised Avrami type kinetic function ($n=\mathrm{const}$, $s=\mathrm{const}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$s=1$</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K^{1 / n}(1-y)\left[\ln \frac{1}{1-y}\right]^{(n-1) / n}$</td>
<td>$y=1-\exp \left\{-\left[\int_{0}^{t} W K^{1 / n} \mathrm{~d} t_{\mathrm{u}}\right]^{n}\right\}$</td>
</tr>
<tr>
<td>$s=n$</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K t^{n-1}(1-y)$</td>
<td>$y=1-\exp \left\{-n\left[\int_{0}^{t} W K t_{\mathrm{u}}^{n-1} \mathrm{~d} t_{\mathrm{u}}\right]\right\}$</td>
</tr>
<tr>
<td>$s=n-1$ ($n \neq 1$)</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K^{(n-1) / n} t^{n-2}(1-y)\left[\ln \frac{1}{1-y}\right]^{1 / n}$</td>
<td>$y=1-\exp \left\{-\left[(n-1) \int_{0}^{t} W K^{(n-1) / n} t_{\mathrm{u}}^{n-2} \mathrm{~d} t_{\mathrm{u}}\right]^{n /(n-1)}\right\}$</td>
</tr>
<tr>
<td>$s=n+1$</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K^{(n+1) / n}(1-y)\left[\ln \frac{1}{1-y}\right]^{-1 / n}$</td>
<td>$y=1-\exp \left\{-\left[(n+1) \int_{0}^{t} W K^{(n+1) / n} t_{\mathrm{u}}^{n} \mathrm{~d} t_{\mathrm{u}}\right]^{n /(n+1)}\right\}$</td>
</tr>
<tr>
<td>$s=2n$</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K^{2} t^{2 n-1}(1-y)\left[\ln \frac{1}{1-y}\right]^{-1}$</td>
<td>$y=1-\exp \left\{-\left[2 n \int_{0}^{t} W K^{2} t_{\mathrm{u}}^{2 n-1} \mathrm{~d} t_{\mathrm{u}}\right]^{1 / 2}\right\}$</td>
</tr>
<tr>
<td>$s=n/2$</td>
<td>$\frac{\mathrm{d} y}{\mathrm{~d} t}=W n K^{1 / 2} t^{n / 2-1}(1-y)\left[\ln \frac{1}{1-y}\right]^{1 / 2}$</td>
<td>$y=1-\exp \left\{-\left[\frac{n}{2} \int_{0}^{t} W K^{1 / 2} t_{\mathrm{u}}^{n / 2-1} \mathrm{~d} t_{\mathrm{u}}\right]^{2}\right\}$</td>
</tr>
</tbody>
</table>

![](./images/812411903685951488_6.jpg)

Fig. 4. Influence of the choice of parameter $S$ on the shape of kinetic curves. Transformation kinetics are calculated by using the generalized additivity rule (cooling rate: 0.38 K/s, $E=0$, $W=1$).

using computer simulations. For simulation pur- poses, kinetic data measured on a low-alloy eutectoid steel during austenite/pearlite transfor- mation were used.

The chemical composition and the heat treat- ment of the steel investigated are given in Ref. [9]. To describe the isothermal austenite/pearlite transformation of steel selected, the Avrami func- tion represented by Eq. (61) was chosen. Parame- ters $K$ and $n$ were estimated by non-linear least square analysis, using the measured reaction fractions obtained from isothermal dilatometric tests [9]. The Avrami exponent was found to be $n=3.4$. The temperature-dependent parameter $K=K(T)$ was approximated by a continuous ex ponential type function defined as

$$
K(T)=\exp \left[A_{0}+A_{1}(T-562)^{2}+\frac{A_{2}}{(T-688)^{2} T}\right],
\tag{70}
$$

where $A_{0}=-14.2144, \quad A_{1}=1.0388 \times 10^{-3}$ and $A_{2}=-8927517$.

![](./images/812411903685951488_7.jpg)

Fig. 5. Influence of the choice of weighting function $W$ on the shape of kinetic curves. Transformation kinetics are calculated by using the generalized additivity rule (cooling rate: 0.38 K/s, $S=1$).

Starting with the generalized kinetic differential equation (64) the austenite/pearlite transformation has been simulated during cooling with a constant cooling rate of $v$. For numerical computations, a cooling curve given as

$$
T(t)=A_{e 1}-v t
\tag{71}
$$

was selected, where $A_{e 1}=688^{\circ} \mathrm{C}$ and $v=0.38 \mathrm{~K} / \mathrm{s}$.

By using weighting function defined by Eq. (47), results obtained by computer simulation are plot- ted in Figs. 4 and 5 for a series of constant values of $S$ and $W$. In the case of $W=1$, Fig. 4 illustrates the influence of the parameter $S$ on the predicted transformation curves for values of $S=3.0,1.5,1$

and 0.75. In Fig. 5 for case of $S=1$, the effect of weighting functions on the predicted non-isothermal kinetic curves is illustrated.

For calculating the weighting function given by Eq. (47), appropriately selected constant values of coefficient $E$ served as a basis. Due to the constant cooling rate, the corresponding values of weighting function $W$ are also constant. Consequently, by choosing values $E=-1.0,-0.5,0,0.5$ and 0.8, computed values of weighting functions are: $W=1.462,1.209,1.000,0.827$ and 0.738 , respectively.

In Figs. 4 and 5, results calculated by applying the traditional additivity rule are demonstrated by kinetic curves with parameters of $S=1$ and $E=0$. As can be seen, the shapes and positions of transformation curves depend strongly on individual values of $S$ and $W$. As can be concluded, by selecting the weight $W$ and parameter $S$ appropriately, result of prediction can be properly modified (or corrected if it is necessary) in accordance with true measured data and by taking into consideration the required accuracy of prediction.

Evaluating the results of simulation, one can conclude that the derivation of function $S=S(T)$ and weight $W$ from pure theoretical considerations seems to be a problematic task which requires further studies. However, it is likely that the interpretation of $S$ and $W$ cannot be simply traced back to well founded physical-metallurgical principles compatible with the traditional theory of non-isothermal transformation kinetics. Parameters $S$ and weight $W$ can be regarded as quantities which are affected by the nucleation rate and/or growth rate of phases nucleated during anisothermal conditions. It is frequently argued that the rate of temperature change $\mathrm{d} T / \mathrm{d} t$ must be included in the reaction rate equation describing the progress of non-isothermal transformations [12,18,36-38]. Cahn has shown that the growth rate $G$ can be considered to be a function of the rate of temperature given in the form

$$
G(T, \dot{T})=G_{0}\left(1+\beta \frac{\mathrm{d} T}{\mathrm{~d} t}\right),
$$

where $G_{0}$ is the growth rate under isothermal condition and $\beta$ is a temperature-dependent parameter [12]. Starting with Eq. (72) a physically reasonable interpretation may be attributed to the weighting function.

## 6. Estimating the onset of austenite decomposition

In the following, the advantage of using the generalized additivity rule defined by Eq. (43) is demonstrated in an example concerning the prediction of the start of austenite/ferrite transformation in a hypoeutectoid steel during continuous cooling. For computation purposes, transformation diagrams of the selected AISI 4340 steel were taken from Ref. [39].

For the steel containing $0.30 \% \mathrm{C}, 0.64 \% \mathrm{Mn}$, $1.0 \% \mathrm{Cr}$ and $0.24 \% \mathrm{Mo}$, the isothermal transformation diagram (ITT diagram) is shown in Fig. 6a. The CCT diagrams in Fig. 6b were computed (dashed lines) and experimentally determined (solid lines). On the calculated CCT diagram, the onset of the austenite/ferrite transformation was

![](./images/812411903685951488_8.jpg)

Fig. 6. Isothermal transformation (upper) and CCT (lower) diagrams for AISI 4130 steel. The onset of austenite/ferrite transformation on the CCT diagram is computed by using the traditional additivity rule (dashed lines) and the generalized additivity rule (dotted lines).

predicted by means of the traditional additivity rule. As can be observed, there is an important discrepancy between the measured and calculated values. In the following it is demonstrated that by applying the generalized additivity rule the start of the austenite/ferrite transformation can be esti- mated with a higher accuracy than by using the traditional additivity principle.

When applying the generalized additivity rule in practice, a key problem is how to select functions $S$ and $W$ and how to estimate them from measured data. As we have already mentioned, when $S$ is supposed to be constant, it may be estimated from differential equation (64) by using regression analysis.

In the case of temperature-dependent $S$, the simplest way of estimating function $S=S(T)$ is to assume that $S$ is a linear function of temperature. In our investigations it was assumed that $W \equiv 1$ and $S$ is defined as
$$
S(T)=S_{0}+S_{1} T,\qquad(73)
$$
where $S_{0}$ and $S_{1}$ are fitting coefficients which can be determined by numerical computational pro- cedure.

The principle of the computational algorithm used is outlined as follows:

(i) As a first step, the isothermal onset of aus- tenite/ferrite transformation has been approxi- mated by an exponential type function defined as
$$
\tau_{\text {in }}(T)=10^{\left(B_{0}+B_{1} U+B_{2} U^{2}\right)},\qquad(74)
$$
where
$$
U=\frac{1}{825-T},\qquad(75)
$$
$\tau_{in }$ is the isothermal incubation time in seconds, $T$  the temperature in degrees Celsius and $B_{0}=0.16095, B_{1}=70.2299$ and $B_{2}=10.0144$ are fitting constants.

(ii) As a second step, it was assumed that the cooling process is characterized by a series of Newtonian cooling curves given as
$$
T_{p}(t)=\left(T_{\mathrm{A}}-T_{\mathrm{R}}\right) \exp \left[-\alpha_{p} t\right]+T_{\mathrm{R}},\qquad(76)
$$
where $T_{A}=800^{\circ} C, T_{R}=20^{\circ} C$ and $\alpha_{p} \ (p=$ 1,2,...,P) are the cooling coefficients ranging from 0.000001 to 0.02.

(iii) As a third step, unknown parameters $S_{0}$  and $S_{1}$ were estimated by using a numerical searching method. For this purpose, an error function formulated as
$$
H_{\mathrm{E}}\left(S_{0}, S_{1}\right)=\sum_{p=1}^{P}\left[T_{m, p}-T_{c, p}\left(S_{0}, S_{1}\right)\right]^{2}\qquad(77)
$$
was used where $T_{m, p}$ are the temperatures of transformation start determined by measurement, while $T_{c, p}=T(t_{c, p}) \ (p=1,2,..., P)$ stand for the temperatures of transformation start calculated by the formula
$$
G(t)=\int_{0}^{t} s \frac{t_{\mathrm{u}}^{s-1}}{\left[\tau_{\mathrm{in}}(T)\right]^{s}} \mathrm{~d} t_{\mathrm{u}}\qquad(78)
$$
taking into consideration the condition $G(t_{c, p})=1$ simultaneously. As can be seen, formula (78) is identical to Eq. (43) if value $y=0$ and W(t, T, T) = 1 are selected as a special case. To estimate the unknown parameters of Eq. (73), er- ror function $H_{E}$ should be minimized with respect to variables $S_{0}$ and $S_{1}$ . This was performed by using numerical computation. As a result of ap- plying the algorithm detailed above, for Eq. (73), we obtained
$$
S(T)=1.083-0.00106 T.\qquad(79)
$$

A comparison between austenite/ferrite transfor- mation starts predicted by using the traditional additivity rule (dashed lines) and the generalized additivity rule (dotted line) is shown in Fig. 6b. As can be stated, in the range of non-isothermal austenite/ferrite transformation, the application of the extended additivity rule produces a better agreement between the calculated and measured CCT curves than using the traditional additivity principle.

## 7. Summary and conclusions

In this paper we examined some possible ways of extending the classical Scheil-Cahn additivity

principle. As a first step of our investigations, two fundamental models devoted to the construction of non-isothermal kinetic functions were analyzed and critically evaluated. The first model (i.e. traditional additivity rule) is represented in the form of a definite integral defined by Eqs. (3) or (31), while the second one relies on the use of a semi-additive (autonomous) differential equation (6) generated from a known isothermal kinetic law. Comparing the two different procedures of prediction, it can be concluded, that both lead to identical results of prediction, if and only if, the kinetic differential equation of reaction is separable in terms of $y$ and $\mathbf{T}$, where $\mathbf{T}$ stands for the state function characterizing the transformation path.

Based on the generalization of the Scheil-Cahn additivity principle, a new phenomenological model for predicting the incubation time and the progress of diffusion-controlled anisothermal transformations has been developed. By introducing non-negative state vector dependent function $S(\mathbf{T})$ and weighting function $W$, the extended non-linear additivity rule is formulated by Eq. (43). It was shown that by selecting $S \equiv 1$ and $W \equiv 1$ in Eq. (43), as a special case the traditional Scheil-Cahn additivity principle can be obtained.

Concerning the choice of functions $S$ and $W$, two questions arise: What physical meaning can be attributed to them, and how to estimate them experimentally ?. It should be emphasized, that a rigorous physical interpretation of the temperature-dependent parameter $S$ and weighting function $W$ is still lacking. However, it is likely that both can be regarded as quantities which are determined by the nucleation and growth rate of phases nucleated under anisothermal conditions. As the second problem is concerned, it is clear that both $S$ and $W$ can be estimated only by performing non-isothermal experiments. The influence of the particular choice of $S$ and $W$ on the shape and position of kinetic curves has been demonstrated by experiments based on computer simulation.

It was verified that, if the transformation time relating to constant state vector $\mathbf{T}$ can be written in the form $\tau(y, \mathbf{T})=\tau_{1}(y) \tau_{2}(\mathbf{T})$ and function $S$ is assumed to be constant, various types of kinetic differential equations and generalized kinetic functions given in closed forms can be derived from the same "iso-kinetic" function, depending on the particular choice of $S$ and $W$. As an example, this concept was applied to the derivation of generalized Avrami type kinetic functions.

A practical application of the generalized additivity rule was illustrated in an example relating to the estimation of the start of austenite/ferrite transformation in a hypoeutectoid steel under continuous cooling conditions. It was found that by using the generalized additivity rule a better agreement between the calculated and measured CCT curves could be obtained than by means of the traditional additivity principle. Although the practical use of the generalized additivity rule was demonstrated for the prediction of the onset of austenite decomposition, it can also be applicable to other thermally activated diffusion-controlled transformation processes.

### Acknowledgements

The financial support of the Ministry of Culture and Education (under Contract Number FKFP 0052/1997) and the Hungarian Academy of Science (under Contract OTKA T21156) is gratefully acknowledged.

### References

[1] I.A. Wierszylłowski, Metall. Trans. A 22 (1991) 993-999.
[2] E.J. Mittemejer, J. Mater. Sci. 27 (1992) 3977-3987.
[3] R.G. Kamat, E.B. Hawbolt, L.C. Brown, J.K. Brimacombe, Metall. Trans. A 23 (1992) 2469-2480.
[4] T. Réti, T. Bell, Y. Sun, A. Bloyce, Mater. Sci. Forum 163-165 (1994) 673-680.
[5] T.T. Pham, E.B. Hawbolt, J.K. Brimacombe, Metall. Trans. A 26 (1995) 1987-1992.
[6] D. Hömberg, IMA J. Appl. Math. 54 (1995) 31-57.
[7] D. Hömberg, Acta Mater. 44 (1996) 4375-4385.
[8] M. Lusk, H.J. Jou, Metall. Mater. Trans. A 28 (1997) 287-291.
[9] T. Reti, L. Horvath, I. Felde, J. Mater. Eng. Performance 6 (1997) 433-442.
[10] M.H. Todinov, Metall. Mater. Trans. B 29 (1998) 269-273.
[11] E. Scheil, Archiv für das Eisenhüttenwesen. 8 (1935) 565-567.
[12] J.W. Cahn, Acta Metal. 4 (1956) 572-575.

[13] J.W. Christian, The Theory of Transformations in Metals and Alloys, Pergamon Press, Oxford, 1975.

[14] G.K. Manning, C.H. Lorig, Trans. AIME 167 (1946) 442–466.

[15] L.D. Jaffe, Trans. AIME 176 (1948) 363–383.

[16] P.T. Moore, J. Iron Steel Inst. 177 (1954) 85–116.

[17] P.K. Agarwal, J.K. Brimacombe, Metall. Trans. B 12 (1981) 121–133.

[18] J.S. Kirkaldy, R.C. Sharma, Scripta Metall. 16 (1982) 1193–1198.

[19] M. Umemoto, K. Horiuchi, I. Tamura, Transactions ISIJ 23 (1983) 690–695.

[20] E.B. Hawbolt, B. Chau, J.K. Brimacombe, Metall. Trans. A 14 (1983) 1803–1815.

[21] E.B. Hawbolt, B. Chau, J.K. Brimacombe, Metall. Trans. A 16 (1985) 565–578.

[22] M. Gergely, T. Reti, Banyasz. Kohasz. Lapok 111 (1978) 439–446.

[23] T. Reti, G. Bobok, M. Gergely, Computing method for non-isothermal heat treatments, in: Proceedings of the International Conference on Heat Treatment '81, The Metals Society, 1983, pp. 91–96.

[24] T. Réti, M. Gergely, P. Tardy, Mater. Sci. Technol. 3 (1987) 365–371.

[25] J. W. Cahn, Trans. AIME, J. Metals, January 1957, p. 140.

[26] A.L. Greer, in: S. Sreeb, H. Warlimont (Eds.), Crystalli- zation Kinetics in Metallic Glasses, Rapid Quenched Metals, Elsevier, Amsterdam, 1985, pp. 215–218.

[27] M. Gergely, T. Réti, J. Heat Treating 5 (2) (1988) 125–140.

[28] T. Kemény, J. Sestak, Thermochim. Acta 110 (1987) 113–129.

[29] T.J.W. De Bruijn, W.A. De Jong, P.J. Van der Berg, Thermochim. Acta 45 (1981) 315–325.

[30] E. Louis, C. Garcia-Cordovilla, J. Thermal. Anal. 29 (1984) 1139–1150.

[31] S. Denis, S. Sjöström, A. Simon, Metall. Trans. A 18 (1987) 1203–1212.

[32] A.J. Fletcher, Thermal Stress and Stress Generation in Heat Treatment, Elsevier, London, 1989.

[33] T. Inoue, Z. Wang, Mater. Sci. Technol. 1 (1985) 845–850.

[34] Z. Wang, T. Inoue, Mater. Sci. Technol. 1 (1985) 899–903.

[35] T.W. Andersen, An Introduction to Multivariate Statistical Analysis, second edition, Wiley, New York, 1984.

[36] J.B MacCallum, J. Tanner, Nature 225 (1970) 1127–1128.

[37] T. Kemeny, Thermochim. Acta 110 (1987) 131–134.

[38] J.B. Leblond, J. Devaux, Acta Metall. 32 (1984) 137–146.

[39] B. Hildenwal, Prediction of the residual stresses created during quenching. Dissertation No. 39, Linköping Univer- sity, S-582 83 Linköping, Sweden, 1979, p. 114.