![](./images/811966159929737218_1.jpg)

Available online at www.sciencedirect.com

![](./images/811966159929737218_2.jpg)

Computational Materials Science 42 (2008) 306-315

COMPUTATIONAL
MATERIALS
SCIENCE

www.elsevier.com/locate/commatsci

# Selecting designs with high resistance to overstress failure initiated by flaws

## M.T. Todinov *

Department of Mechanical Engineering and Mathematical Sciences, School of Technology, Oxford Brookes University, Wheatley, Oxford OX33 1HX, United Kingdom

Received 28 March 2007; accepted 20 July 2007
Available online 14 September 2007

### Abstract

A powerful new technology is proposed for creating reliable and robust designs, characterized by a high resistance to failure. The new technology is based on a new mixed-mode failure criterion, and computationally very efficient simulation technique for calculating the probability of failure of a component with complex shape.

The new technology handles design alternatives with complex shape and arbitrary loading. For each design shape or a loading alter- native, a finite element model is created by using a standard finite element package. Next, a specially designed postprocessor reads the output files from the static stress analyses and calculates the probability of failure associated with each design alternative. Finally, the design alternative characterised by the smallest probability of failure is selected.

Limitations of existing approaches to statistics of failure locally initiated by flaws are also discussed. Central to the traditional approaches is the assumption that the number density of the critical flaws is a power function of the applied stress. In this paper, on the basis of counter-examples, we show that for a material with flaws, the power law assumption does not hold in common cases, such as spherical flaws in a homogeneous matrix.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Flaws; Defects; Probability; Statistics; Failure; Fracture; Brittle fracture; Local approach

---

## 1. Introduction

An important factor affecting failures of components and structures is the presence of flaws due to processing, manufacturing or mechanical damage during service. Pres- ence of flaws leads to failures at relatively low applied stres- ses and fracture toughness replaces strength as the relevant material property. Assuming that the weakest-link princi- ple holds, failure occurs if for at least a single flaw, the local load exceeds the local strength.

In order to select a design alternative characterized by a high resistance to overstress failure locally initiated by flaws, the probability of failure associated with number of design alternatives must be assessed. There exist a number of approaches related to determining the probability of failure initiated by flaws, the suitability of which will be discussed in detail.

### 1.1. Weibull approach

Suppose that a component with volume $V$ is subjected to uniaxial tension (Fig. 1) and $n_{\text{cr}}(\sigma)$ is the number density of the critical flaws which cause failure at the loading stress $\sigma$. Suppose also that the volume $V$ has been divided into $n$ incremental volumes $\Delta V$ (Fig. 1).

If the flaw locations follow a homogeneous Poisson pro- cess, the probability that an incremental volume $\Delta V$ will contain a critical flaw is $n_{\text{cr}}(\sigma)\Delta V$. The probability $R$ that the entire volume $V$ will survive the loading stress $\sigma$ equals the probability that all incremental volumes $\Delta V$ will sur- vive the applied stress $\sigma$:

---

* Tel.: +44 1865 48 3546.
E-mail address: mtodinov@brookes.ac.uk

0927-0256/$ - see front matter © 2007 Elsevier B.V. All rights reserved.
doi:10.1016/j.commatsci.2007.07.031

![](./images/811966159929737218_3.jpg)

Fig. 1. Uniaxial tensile loading of a homogeneous component.

$$
\begin{aligned}
R & =\left(1-n_{\mathrm{cr}}(\sigma) \Delta V\right)^{n}=\exp \left(n \ln \left[1-n_{\mathrm{cr}}(\sigma) \Delta V\right]\right) \\
& \approx \exp \left(-n_{\mathrm{cr}}(\sigma) V\right)
\end{aligned}
$$

because for $\Delta V \approx 0, \ln [1-n_{\mathrm{cr}}(\sigma) \Delta V] \approx-n_{\mathrm{cr}}(\sigma) \Delta V$ and $V=n \times \Delta V$.

In order to use Eq. (1), an expression for the number density of the critical flaws $n_{\mathrm{cr}}(\sigma)$ as a function of the applied stress is required. The empirical relationship

$$
n_{\mathrm{cr}}(\sigma)=\left(\frac{\sigma-\sigma_{\mathrm{u}}}{\sigma_{0}}\right)^{m}
$$

is commonly assumed (Weibull, [1]), where the threshold value $\sigma_{u}$, the Weibull modulus $m$ and the Weibull scale parameter $\sigma_{0}$ are constants. Often, $\sigma_{u}=0$ is assumed which ensures some conservatism in the calculations.

For the probability of failure $p_{\mathrm{f}}(\sigma)$ of a component with volume $V$ subjected to a constant stress magnitude $\sigma$, the equation

$$
p_{\mathrm{f}}(\sigma)=1-\exp \left(-V\left(\sigma / \sigma_{0}\right)^{m}\right)
$$

is obtained.

Despite that the Weibull model [1] has been criticized for lack of physical basis and for being 'pure statistics' (Lamon, [2]), for a homogeneous material it can be defended.

### 1.2. Batdorf and Crose approach

An attempt to build a more physically based model was made by Batdorf and Crose [3]. The essence of this model can be captured if a specimen with volume $V$ is considered, subjected to uniaxial tension and containing randomly oriented microcracks. According to the Batdorf and Crose [3] model, the failure probability $\mathrm{d} p$ of an incremental volume $\Delta V$ with a stress in the infinitesimal interval $\sigma_{\text {cr }} \sigma_{\text {cr }}+\mathrm{d} \sigma_{\text {cr }}$ is

$$
\mathrm{d} p=\frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}} \Delta V \frac{\Omega\left(\Sigma, \sigma_{\mathrm{cr}}\right)}{4 \pi}
$$

where $\Delta V$ is the incremental volume, $N(\sigma_{\text {cr }})$ is the number density of the cracks with a critical stress (the stress at which a crack becomes unstable) less than or equal to $\sigma_{\text {cr }}, \frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}} \Delta V$ is the number of cracks in the elementary volume $\Delta V$ having a critical stress between $\sigma_{\text {cr }}$ and $\sigma_{\text {cr }}+\mathrm{d} \sigma_{\text {cr }}, \Omega$ is the solid angle defining all orientations for which the stress component normal to the crack plane is greater than $\sigma_{\text {cr }}$ and $\Sigma$ denotes the applied stress state. For cracks following a homogeneous Poisson process, $\frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}} \Delta V$ is the probability that there will be a crack in the elementary volume $\Delta V$ with a critical stress in the infinitesimal interval $\sigma_{\text {cr }}, \sigma_{\text {cr }}+d \sigma_{\text {cr }}$ and $\frac{\Omega\left(\Sigma, \sigma_{\text {cr }}\right)}{4 \pi}$ is the probability that the crack will be oriented in such a way that the normal stress to it will be greater than $\sigma_{\text {cr }}$ and will therefore cause failure. If the loading stress is $\sigma$, the probability of failure of the volume $\Delta V$ is obtained by integrating:

$$
\delta p_{\mathrm{f}}(\sigma)=\Delta V \int_{0}^{\sigma} \frac{\Omega\left(\Sigma, \sigma_{\mathrm{cr}}\right)}{4 \pi} \frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}}
$$

The probability of survival of the volume $V$ is given by

$$
R=\left[1-\delta p_{\mathrm{f}}(\sigma)\right]^{V / \Delta V},
$$

which is a product of the survival probabilities $1-\delta p_{\mathrm{f}}(\sigma)$ of all volumes $\Delta V$, whose number is $n=V / \Delta V$.

Since expression (6) can be approximated by

$$
R=\exp \left(-V \int_{0}^{\sigma} \frac{\Omega\left(\Sigma, \sigma_{\mathrm{cr}}\right)}{4 \pi} \frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}}\right)
$$

the probability of failure of the loaded volume $V$ becomes

$$
p_{\mathrm{f}}(\sigma)=1-\exp \left(-V \int_{0}^{\sigma} \frac{\Omega\left(\Sigma, \sigma_{\mathrm{cr}}\right)}{4 \pi} \frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}}\right)
$$

Bathdorf and Crose [3] demonstrated that for uniaxial tension, their theory was equivalent to Weibull's. In the Batdorf and Crose model, only the tensile stress normal to the crack plane has been accounted for.

### 1.3. Multiaxial elemental strength approach

Weakest-link theories pertinent to fracture of brittle materials (Evans [4]; Evans and Jones [5]) assume flaw locations following a homogeneous Poisson process which permits the probability $\delta p_{\mathrm{f}}(\sigma)$ that a flaw will exist in the incremental volume $\Delta V$, with strength not greater than the applies stress $\sigma$, to be presented as

$$
\delta p_{\mathrm{f}}(\sigma)=\Delta V \int_{0}^{\sigma} g(v) \mathrm{d} v
$$

where $g(v) \mathrm{d} v$ is the number of flaws per unit volume with strength between $v$ and $v+\mathrm{d} v$. The integral $\int_{0}^{\sigma} g(v) \mathrm{d} v$ gives the number of flaws per unit volume with strength smaller or equal than $\sigma$. The probability of survival of the component with volume $V$ is then a product of the survival probabilities $1-\delta p_{\mathrm{f}}(\sigma)$ characterizing the incremental volumes. In the limit, $\Delta V \rightarrow 0$, and the probability of failure $p_{\mathrm{f}}(\sigma)$ of the entire component becomes

$$
p_{\mathrm{f}}(\sigma)=1-\exp \left[-\int_{V} \mathrm{~d} V \int_{0}^{\sigma} g(v) \mathrm{d} v\right]
$$

Andreasen [6] reduced the Batdorf and Crose equation to Eq. (10) and demonstrated that the Batdorf approach and the multiaxial elemental strength approach are equivalent for any common fracture criterion. He concluded that previously reported differences are a result from different choices regarding the equivalent stresses and do not stem from fundamental differences in the two approaches.

An application of the Batdorf and Crose model and the multiaxial elemental strength model for life prediction of structural components has been demonstrated by Duffy

et al. [7]. Nemeth [8] also used the Batdorf theory to predict the reliability of ceramic and graphite components under generalised loads. The software developed (CARES/Life) incorporated the principle of independent action, and the Batdorf and Crose approach.

## 2. Analysis of the existing approaches to statistics of failure locally initiated by flaws with respect to selecting design alternatives with a high resistance to failure initiated by flaws

As can be verified from Eqs. (1)-(3), the Weibull model is equivalent to
$$
p_{\mathrm{f}}(\sigma)=1-\exp \left[-n_{\mathrm{cr}}(\sigma) V\right]
\tag{11}
$$
where $n_{\mathrm{cr}}(\sigma)$ is the number density of critical flaws causing failure at loading stress $\sigma$. (A critical flaw is a flaw which will initiate failure with certainty, at loading stress $\sigma$.)

In the Weibull model (3), for the number density of the critical flaws, the power function $n_{\mathrm{cr}}=\left(\sigma / \sigma_{0}\right)^{m}$ has been assumed. In the elemental strength model, the product $\mathrm{d} V \int_{0}^{\sigma} g(v) \mathrm{d} v$ gives the expected number of defects with strength smaller than or equal to $\sigma$, in the infinitesimal volume $\mathrm{d} V$. Integrating this product over the entire volume $V$ of the specimen gives the expected number of critical defects in the volume $V$. Consequently, the elemental strength model can also be reduced to Eq. (11).

The integral $\int_{0}^{\sigma} \frac{\Omega\left(\Sigma, \sigma_{\mathrm{cr}}\right)}{4 \pi} \frac{\mathrm{d} N\left(\sigma_{\mathrm{cr}}\right)}{\mathrm{d} \sigma_{\mathrm{cr}}} \mathrm{d} \sigma_{\mathrm{cr}}$ in the Batdorf and Crose model (8) is, in fact, the number density of the critical flaws. Consequently, the Batdorf and Crose model can also be reduced to Eq. (11).

The Danzer and Lube [9] model
$$
p_{\mathrm{f}}=1-\exp \left(-\overline{N}_{\mathrm{c}}\right)
\tag{12}
$$
where $\overline{N}_{\mathrm{c}}$ is the expected number of defects with critical size in the stressed volume is also equivalent to Eq. (11) because $\overline{N}_{\mathrm{c}}=n_{\mathrm{cr}} V$.

As a result, all considered models reduce to Eq. (11) where the main parameter $n_{\mathrm{cr}}$ is the number density of the critical flaws, which is not a measurable quantity. Consequently, an assumption is required about the dependence $n_{\mathrm{cr}}=n_{\mathrm{cr}}(\sigma)$ of the number density of critical flaws on the magnitude of the loading stress. What can be determined by using direct counting (for surface defects), ultrasonic inspection, radiography, quantitative metallography or dissolving the matrix, is the actual number density of the flaws. In order to determine the number density of flaws $N\left(\sigma_{\mathrm{cr}}\right)$ with strength not greater than $\sigma_{\mathrm{cr}}$ (which is not a directly measurable quantity), Batdorf and Heinisch [10] assumed a power function of the type $N\left(\sigma_{\mathrm{cr}}\right)=k \sigma_{\mathrm{cr}}^{m}$. This is a convenience assumption made to analyse failure data complying with the two-parameter Weibull distribution. Similarly, a power law relationship $g(\sigma)=k \sigma^{m}$ has been adopted by Lamon and Evans [11]. Again, this is a 'convenience assumption' which does not seem to have any physical basis.

From experimental data related to uniaxial tension, three-point flexure test, four-point flexure test, expanded ring tensile test and biaxial strength tests, Evans and Jones [5] derived expressions for the dependence of the expected number density of critical defects on the applied stress. The derived expressions were different - uniquely dependent on the type of test, the specimen size and geometry. Gerguri et al. [12] also reported that the calculated Weibull modulus depended on the specimen geometry - in particular on whether the specimen has a notch or not. For notched graphite bars, a value $m=29$ was obtained, which was almost three times higher than the value $m=10$ obtained for unnotched bars. Similar results were obtained for silicon nitride bars. Furthermore, the experimental findings of Gerguri et al. [12] also highlighted the limitations of the Weibull statistics approach in the case of notched specimens characterised by a small zone of stress intensification. At this scale, the stressed volume is small and the material cannot be assumed to be homogeneous/quasi-homogeneous.

Here we give a counterexample where the power function is inappropriate for approximating the stress dependence of the number density of critical flaws. The counterexample involves a homogeneous matrix containing spherical second-phase particles which crack easily due to the maximum local tensile stress. The microcracks will be treated as Griffith cracks and the fracture stress is given by (Anderson, [13]):
$$
\sigma_{\mathrm{c}}=\left(\frac{\pi E \gamma_{\mathrm{p}}}{\left(1-v^{2}\right) D}\right)^{1 / 2}
\tag{13}
$$
where $D$ is the diameter of the particle, $\gamma_{\mathrm{p}}$ is the plastic work required to create a unit area of fracture surface in the matrix, $E$ and $v$ are the modulus of elasticity and the Poisson's ratio for the matrix, respectively. This failure criterion can also be presented as
$$
\sigma_{\mathrm{c}}=\frac{A}{\sqrt{D}}
\tag{14}
$$
where $A$ is a constant. Suppose that the flaws in the volume $V$ follow a homogeneous Poisson process with number density $\lambda=0.12 \mathrm{~cm}^{-3}$. If the size of the volume is $V=10 \mathrm{~cm}^{3}$, for a specified uniaxial tension with magnitude $\sigma$, the number density of the critical flaws in the volume $V$ is
$$
n_{\mathrm{cr}}(\sigma)=\lambda \times P\left(\sigma_{\mathrm{c}} \leqslant \sigma\right)
\tag{15}
$$
where $P\left(\sigma_{\mathrm{c}} \leqslant \sigma\right)$ is the probability that the critical stress will be smaller than the loading stress. Since $\sigma_{\mathrm{c}} \leqslant \sigma$ is equivalent to $D \geqslant A^{2} / \sigma^{2}$, the number density of the critical flaws can also be presented as
$$
n_{\mathrm{cr}}(\sigma)=\lambda \times P\left(D \geqslant A^{2} / \sigma^{2}\right)
\tag{16}
$$
If the diameter of the particles follows a Gaussian distribution with mean $\mu_{\mathrm{D}}$ and standard deviation $\sigma_{\mathrm{D}}$, for the probability $P\left(D \geqslant A^{2} / \sigma^{2}\right)$, the expression
$$
P\left(D \geqslant A^{2} / \sigma^{2}\right)=\Phi\left(\frac{\mu_{\mathrm{D}}-A^{2} / \sigma^{2}}{\sigma_{\mathrm{D}}}\right)
\tag{17}
$$

is valid, where $\Phi(\bullet)$ is the cumulative standard normal distribution. For a constant $A=32,700 \times 10^{6}$ and diameter $D$ of the flaws following a normal distribution with mean $\mu_{\mathrm{D}}=300 \mu \mathrm{m}$ and standard deviation $\sigma_{\mathrm{D}}=35 \mu \mathrm{m}$, a dependence is obtained for the number density of critical flaws as a function of the applied stress (Fig. 2).

As can be verified from the graph, the dependence tends asymptotically to the actual number density of flaws and cannot be approximated by a power law of the type $n_{\mathrm{cr}}(\sigma)=k \sigma^{m}$. Consequently, in this case, the power function approximation of the critical flaws number density is not valid.

Clearly, the number density of critical flaws can be presented as

$$
n_{\mathrm{cr}}(\sigma)=\lambda \times F_{\mathrm{c}}
$$

where $\lambda$ is the actual number density of all flaws in the material and $F_{\mathrm{c}}$ is the probability that a flaw will initiate failure given that it is present with certainty in the component. In order to reflect the fact that it is related to a single flaw, this probability can also be referred to as 'conditional individual probability of initiating failure'. In the discussed counterexample, the probability $F_{\mathrm{c}}$ is given by Eq. (19):

$$
F_{\mathrm{c}}=\Phi\left(\frac{\mu_{\mathrm{D}}-A^{2} / \sigma^{2}}{\sigma_{\mathrm{D}}}\right)
$$

which is the probability $P(D \geqslant A^{2} / \sigma^{2})$ that the diameter $D$ of the flaw will be greater than the critical diameter $D_{\mathrm{cr}}=A^{2} / \sigma^{2}$ corresponding to a magnitude $\sigma$ of the loading stress. Unlike the critical flaw number density $n_{\mathrm{cr}}$, the conditional probability $F_{\mathrm{c}}$ is physically based, because the critical diameter $D_{\mathrm{cr}}=A^{2} / \sigma^{2}$ has been obtained from a failure criterion reflecting the controlling failure mechanism.

Here we consider another counterexample featuring a dependence of the number of critical flaws on the acting stress, which cannot be described by a power law. Suppose for simplicity, that for a plate subjected to a uniaxial stress,

![](./images/811966159929737218_4.jpg)

Fig. 2. Number density of critical flaws as a function of the applied stress $\sigma$ (MPa) built for a specimen with volume $V=10 \mathrm{~cm}^{3}$.

![](./images/811966159929737218_5.jpg)

Fig. 3. (a) A plate subjected to a uniaxial tension, containing flaws of equal size and random orientation and (b) dependence of the variation of the number of critical flaws on the magnitude of the applied stress.

a number of cuts with the same size are present on the surface. In the case of identical flaws, the instability of a flaw is determined solely by its orientation. Suppose for simplicity that if the normal stress $\sigma_{n}$ to the plane of the flaw exceeds a particular critical value $\sigma_{\mathrm{cr}}$, the flaw will initiate failure (Fig. 3a).

The condition for instability is therefore $\sigma_{n}=|\sigma \cos \theta| \geqslant \sigma_{\mathrm{cr}}$. If the orientation angle can accept any value from 0 to $2 \pi$, the probability $P(\sigma_{n} \geqslant \sigma_{\mathrm{cr}})$ that $\sigma_{n}=|\sigma \cos \theta| \geqslant \sigma_{\mathrm{cr}}$ will be fulfilled is given by

$$
P\left(\sigma_{\mathrm{n}} \geqslant \sigma_{\mathrm{cr}}\right)=\frac{4 \times \arccos \left(\sigma_{\mathrm{cr}} / \sigma\right)}{2 \pi}
$$

Suppose also that the expected number of flaws is $\lambda S=1000$ where $S$ is the surface area and $\lambda$ is the surface number density of the flaws. The expected number of critical flaws $\bar{N}_{\mathrm{cr}}$ is then given by $\bar{N}_{\mathrm{cr}}=\lambda S \times P(\sigma_{n} \geqslant \sigma_{\mathrm{cr}})$. Plotting the dependence $\bar{N}_{\mathrm{cr}}$ versus the applied stress $\sigma$ results in the curve shown in Fig. $3 \mathrm{~b}$ ($\sigma_{\mathrm{cr}}=50 \mathrm{MPa}$). As can be verified, with increasing the magnitude of the acting stress, the curve asymptotically tends to the expected number of flaws $\lambda S=1000$ and cannot be described by a power law.

### 3. An alternative to the traditional approaches based on the power law

The outlined limitations associated with traditional statistical theories of locally initiated failure demonstrate that they are not suitable for a comparative reliability measure aimed to assess design alternatives in terms of their resistance to failure initiated by flaws. These drawbacks are

easily avoided by a model recently proposed in Refs. [14] and [15] for determining the probability of failure initiated by flaws.

The probability of failure initiated by flaws with number density $\lambda$ in a loaded component with volume $V$, has been derived to be
$$
p_{\text{flaws}} = 1 - \exp(-\lambda V F_{\text{c}}) \tag{21}
$$
where $F_{\text{c}}$ is the conditional individual probability of triggering failure characterising a single flaw, given that it resides in the component/structure. If no flaws exist in the material or their expected number $\lambda$ per unit volume is very small, $\lambda \approx 0$, the probability $p_{\text{flaws}}$ in Eq. (21) is approximately equal to zero ($p_{\text{flaws}} \approx 0$). We need to point out that Eq. (21) estimates only the component of the total probability of failure of the volume $V$ which is initiated by flaws.

During the derivation of Eq. (21) (Ref. [14]), only failure initiated by flaws has been considered. Consequently, with increasing stress, the probability of failure initiated by flaws $p_{\text{flaws}}$ does not tend to unity but to the probability $1 - \exp(-\lambda V)$ (as it should) that at least a single flaw will be captured in the component volume $V$ (Fig. 4a).

Eq. (21) cannot be used to estimate the probability of failure $p_{\text{M}}$ of a matrix without flaws. This probability can, for example, be estimated by the Weibull distribution which seems to give satisfactory results for the probability of failure of homogeneous material. The total probability $p_{\text{total}}$ of failure, related to the stressed volume $V$, can be presented as
$$
p_{\text{total}} = 1 - p_{\text{M}}^{0} \times p_{\text{flaws}}^{0} \tag{22}
$$
where $p_{\text{M}}^{0}$ is the probability of no failure of the matrix and $p_{\text{flaws}}^{0}$ is the probability that failure will not be initiated by flaws.

This follows from the following probabilistic argument. The total probability of failure of volume $V$ is equal to $1 -$ the probability of no failure of the volume $V$. Failure does not occur if it is not initiated by flaws and if it is not initiated by the matrix. As a result, the probability of no failure is a product of the probability of no failure
$$
p_{\text{M}}^{0} = \exp(-V(\sigma/\sigma_{0})^{m}) \tag{23}
$$
of the matrix (the Weibull distribution is used), and the probability
$$
p_{\text{flaws}}^{0} = \exp(-\lambda V F_{\text{c}}) \tag{24}
$$
that failure will not be initiated by flaws ( Eq. (21) is used). As a result, the probability of failure becomes
$$
p_{\text{total}} = 1 - \exp\left[-V\left(\lambda F_{\text{c}} + (\sigma/\sigma_{0})^{m}\right)\right] \tag{25}
$$

As can be verified from Eq. (25), with increasing the stress magnitude $\sigma$, the total probability of failure related to the volume $V$ approaches unity (Fig. 4b).

Eq. (21) is valid not only for a constant stress, but also for a loaded component/structure with complex shape for which the stress tensor varies in magnitude and sign, from point to point inside. With different magnitudes of the loading forces which alter the stress state of the component/structure, the conditional individual probability $F_{\text{c}}$ varies too. The method for determining the conditional individual probability $F_{\text{c}}$ is based on combining a Monte Carlo simulation and a failure criterion [14,15]. For a specified number of Monte Carlo simulation trials, random locations are generated in the component/structure. At each random location with coordinates $(x,y,z)$, a random orientation and random size are sampled for the flaw. A failure criterion $\Phi(x,y,z) \geqslant 0$ is then applied for the sampled random location, orientation and size to check whether the flaw will initiate fracture. The aim is to collect statistical information from all parts of the component volume, locally stressed in different ways. This is necessary to estimate the conditional individual probability $F_{\text{c}}$. The conditional individual probability of triggering fracture $F_{\text{c}}$ characterising a single flaw is estimated by dividing the number of simulations $N_{\text{f}}$ in which the flaw 'has initiated' fracture to the total number $N$ of Monte Carlo simulation trials ($F_{\text{c}} \approx N_{\text{f}}/N$). Once $F_{\text{c}}$ has been estimated, it is plugged into the equation to determine the probability of overstress fracture of the component. The method works irrespective of the geometry and type of loading of the component.

As can be verified from the described method, the conditional individual probability $F_{\text{c}} = E(I)$ is equal to the

![](./images/811966159929737218_6.jpg)

Fig. 4. With increasing the applied stress: (a) the probability of failure due to initiation from flaws approaches the probability $1 - \exp(-\lambda V)$ that at least a single flaw will reside in the stressed volume $V$ and (b) the total probability of failure of the volume $V$ approaches unity.

expected value $E(I)$ of the failure indicator function, $I$ defined as:
$$
I=
\begin{cases}
1, & \text{if } \Phi(x,y,z) \geqslant 0 \text{ (failure)} \\
0, & \text{if } \Phi(x,y,x) < 0 \text{ (no failure)}
\end{cases}
\tag{26}
$$

Since the flaw number density $\lambda$ and the volume $V$ are real physical quantities, unlike the traditional statistical theories based on the number density of the critical flaws, Eq. (21) is physically based.

The equation is based on a failure criterion and does not require assumptions regarding the stress dependence of the number density $n_{\text{cr}}$ of critical flaws. It is a powerful alternative to the traditional statistical theories with respect to determining the component of the total probability of failure which is caused by flaws. In the case where the conditional individual probability $F_{\text{c}}$ can indeed be approximated by a power function of the type $F_{\text{c}}=k\sigma^{m}$, the equation transforms into the Weibull distribution. In the general case of a homogeneous matrix containing flaws however, such approximation is not necessarily valid.

### 4. A mixed-mode criterion for crack initiation at a spherical flaw

For the special case of brittle fracture initiated from an existing flaw whose shape can be approximated well by a penny-shaped crack, a mixed-mode coplanar strain-energy release rate criterion has been proposed by Paris and Sih [19]:
$$
G=\frac{\left(1-v^{2}\right) K_{\mathrm{I}}^{2}}{E}+\frac{\left(1-v^{2}\right) K_{\mathrm{II}}^{2}}{E}+\frac{(1+v) K_{\mathrm{III}}^{2}}{E},
\tag{27}
$$
used also by Evans [4].

In Eq. (27), $G$ is the strain-energy release rate; $K_{\mathrm{I}}, K_{\mathrm{II}}$ and $K_{\mathrm{III}}$ are the three stress-intensity factors corresponding to the three basic loading modes which are functions of the stress magnitude and crack geometry; $E$ is the elastic modulus and $v$ is the Poisson ratio. Again, the local principal stresses calculated at the flaw's location act as remote stresses.

Fracture, according to this criterion occurs if the value of the strain energy release rate $G$ exceeds the critical strain-energy release rate $G_{\mathrm{c}}$ for the material. This criterion is based on the assumption that planar penny-shaped cracks propagate along their initial planes if $G>G_{\mathrm{c}}$. Nuismer [20] proposed a solution for the case where the propagation of the existing crack does not occur in the initial crack plane.

Here we propose a criterion related to the case where the crack does not yet exist. The fracture criterion given by Eq. (13) is of this type but it is based on the maximum tensile stress only (mode I type of loading) and does not reflect the contribution of the shear stress in mode II type of loading which can be significant for materials with anisotropy. Following Dowling [16], a successful fracture criterion must also predict mixed-mode fracture data of the type quoted by Broek [17] where fracture is controlled by mode I and mode II crack opening. Mode II type of loading is important for materials characterised by anisotropy, where the fracture toughness is significantly reduced in particular directions or along particular planes and the crack propagation occurs along these directions/planes. Good examples are the delamination and the longitudinal splitting due to anisotropy, fiber/matrix debonding.

Accordingly, in cases where the fracture toughness $K_{\text{Ic}}$ and $K_{\text{IIc}}$ characterising the material in mode I and mode II type of loading are known, the empirical mixed-mode criterion (Dowling [16]) can be used:
$$
\left(K_{\mathrm{I}} / K_{\mathrm{Ic}}\right)^{2}+\left(K_{\mathrm{II}} / K_{\mathrm{IIc}}\right)^{2}=1
\tag{28}
$$
where $K_{\mathrm{I}}$ and $K_{\mathrm{II}}$ are the stress-intensity factors characterising the crack-like defect. In cases where only the fracture toughness $K_{\text{Ic}}$ is known or where $K_{\text{IIc}} \gg K_{\text{Ic}}$ holds, the empirical criterion $K_{\mathrm{I}} / K_{\mathrm{Ic}}=1$ can be used.

The empirical criterion (28) fits very well the mixed-mode failure data quoted by Broek [17]. For a penny-shaped crack, $K_{\mathrm{I}}=\frac{2}{\pi} \sigma_{n} \sqrt{\pi a}$ (Williams, [18]) and (Anderson, [13]) where $\sigma_{n}$ is the stress normal to the crack plane and $\tau$ is the shear stress acting in the crack plane. As a result, the mixed-mode criterion (28) can also be presented as
$$
\sigma_{n}^{2} \theta+\tau^{2} \gamma=1
\tag{29}
$$
where $\theta=\frac{4}{\pi K_{\mathrm{Ic}}^{2}} a$ and $\gamma=\frac{v^{2} \pi}{K_{\mathrm{IIc}}^{2}} a$ are constants depending on the size ' $a$ ' of the flaw and the fracture toughness of the matrix characterising mode I and mode II crack opening. For a flaw with spherical shape, finding the plane along which the annular crack will develop reduces to finding the orientation for which the expression
$$
A\left(t_{1}, t_{2}\right)=\sigma_{n}^{2} \theta+\tau^{2} \gamma
\tag{30}
$$
has a maximum with respect to the direction cosines $t_{1}, t_{2}$ and $t_{3}$ ($t_{1}^{2}+t_{2}^{2}+t_{3}^{2}=1$), and checking whether this maximum is equal to or greater than one ($\max A(t_{1},t_{2}) \geqslant 1$).

Expressing the normal and shear stress acting on the crack plane by the principal stresses $\sigma_{1} \geqslant \sigma_{2} \geqslant \sigma_{3}$ and direction cosines $t_{1}, t_{2}$ and $t_{3}$ of the plane normal, (Fig. 5) gives:
$$
\sigma_{n}=t_{1}^{2} \sigma_{1}+t_{2}^{2} \sigma_{2}+t_{3}^{2} \sigma_{3}
\tag{31}
$$
$$
\tau=\left[\left(\sigma_{1}-\sigma_{2}\right)^{2} t_{1}^{2} t_{2}^{2}+\left(\sigma_{2}-\sigma_{3}\right)^{2} t_{2}^{2} t_{3}^{2}+\left(\sigma_{1}-\sigma_{3}\right)^{2} t_{1}^{2} t_{3}^{2}\right]^{1 / 2} \quad(32)
$$

Therefore, in order to find $\max_{t_{1},t_{2}} A(t_{1}, t_{2})$ in Eq. (30), the function:
$$
\begin{aligned}
A\left(t_{1}, t_{2}\right)= & {\left[t_{1}^{2} \sigma_{1}+t_{2}^{2} \sigma_{2}+\left(1-t_{1}^{2}-t_{2}^{2}\right) \sigma_{3}\right]^{2} \theta } \\
& +\left[\left(\sigma_{1}-\sigma_{2}\right)^{2} t_{1}^{2} t_{2}^{2}+\left(\sigma_{2}-\sigma_{3}\right)^{2} t_{2}^{2}\left(1-t_{1}^{2}-t_{2}^{2}\right)\right. \\
& \left.+\left(\sigma_{1}-\sigma_{3}\right)^{2} t_{1}^{2}\left(1-t_{1}^{2}-t_{2}^{2}\right)\right] \gamma
\end{aligned}
\tag{33}
$$
obtained by using Eqs. (31) and (32) is to be maximised with respect to $t_{1}$ and $t_{2}$ in the closed domain $t_{1}^{2}+t_{2}^{2} \leqslant 1$. The local extrema can be found by using the necessary conditions

![](./images/811966159929737218_7.jpg)

Fig. 5. Normal and shear stress components acting on the potential crack plane $A_{1}A_{2}A_{3}$.

$$
\frac{\partial A\left(t_{1}, t_{2}\right)}{\partial t_{1}}=0 ; \quad \frac{\partial A\left(t_{1}, t_{2}\right)}{\partial t_{2}}=0
\tag{34}
$$

leading to the non-linear system
$$
t_{1}\left[\left(\sigma_{1}-\sigma_{3}\right) t_{1}^{2}+\left(\sigma_{2}-\sigma_{3}\right) t_{2}^{2}-\frac{1}{2}\left(\sigma_{1}-\sigma_{3}\right)-\sigma_{n}(\theta / \gamma)\right]=0
\tag{35}
$$

$$
t_{2}\left[\left(\sigma_{1}-\sigma_{3}\right) t_{1}^{2}+\left(\sigma_{2}-\sigma_{3}\right) t_{2}^{2}-\frac{1}{2}\left(\sigma_{2}-\sigma_{3}\right)-\sigma_{n}(\theta / \gamma)\right]=0
\tag{36}
$$

with a trivial solution $t_{1}=t_{2}=0$, where $\sigma_{n}$ is given by Eq. (31). The value $A(t_{1},t_{2})$ corresponding to the trivial solution is obtained from Eq. (33) by a direct substitution:
$$
A(0,0)=\theta \sigma_{3}^{2}
$$

In order to find the non-trivial solutions of system (35), (36), let us assume that $\theta \neq \gamma$. The rest of the stationary points of function (33), needed to determine all local extrema are among the non-trivial solutions of system (35), (36). Since there are no solutions of the system for $t_{1}$ and $t_{2}$ both non-zero if $\sigma_{1} \neq \sigma_{2}$, the non-trivial solutions can be obtained by putting $t_{1} \neq 0,t_{2}=0$ and $t_{1}=0,t_{2} \neq 0$. At the stationary points:
$$
t_{1} \equiv t_{1}^{*}= \pm \sqrt{\frac{1 / 2+\frac{\sigma_{3}}{\sigma_{1}-\sigma_{3}}(\theta / \gamma)}{1-\theta / \gamma}}, \quad t_{2} \equiv t_{2}^{*}=0
\tag{37}
$$

two equal local extrema (maxima) of expression (33) exist. The magnitude of the local maxima is
$$
A_{\max }=\frac{1}{(1-\theta / \gamma)^{2}}\left(\frac{\left(\sigma_{1}+\sigma_{3}\right)^{2}}{4} \theta+\left(\frac{\sigma_{1}-\sigma_{3}}{2}+\frac{\theta \sigma_{3}}{\gamma}\right)\left(\frac{\sigma_{1}-\sigma_{3}}{2}-\frac{\theta \sigma_{1}}{\gamma}\right) \gamma\right)
\tag{38}
$$

The global maximum of expression (33) is attained either at some of the solutions of the non-linear system (35),(36) or at the boundary of the domain $0 \leqslant t_{1} \leqslant 1$, $0 \leqslant t_{2} \leqslant \sqrt{1-t_{1}^{2}}$ ($t_{1}^{2}+t_{2}^{2} \leqslant 1$). Since $t_{1}$ and $t_{2}$ cannot be both non-zero, the boundary is defined by $t_{1}= \pm 1$, $t_{2}=0$ and $t_{1}=0$, $t_{2}= \pm 1$. Since $A(+1,0)=A(-1,0)$, $A(0,+1)=A(0,-1)$, the check of function values on the boundary of the domain where $t_{1}$ and $t_{2}$ vary, reduces to a check at points $t_{1}=1,t_{2}=0$ and $t_{1}=0,t_{2}=1$ on the domain. The values $A(1,0)$ and $A(0,1)$ are obtained by a direct substitution in Eq. (33)
$$
A(1,0)=\theta \sigma_{1}^{2} ; \quad A(0,1)=\theta \sigma_{2}^{2}
\tag{39}
$$

Finally, the global maximum is determined from a comparison of four values: the local maximum $A_{\max }$ from Eq. (38), the value $A(0,0)=\theta \sigma_{3}^{2}$, the value $A(1,0)=\theta \sigma_{1}^{2}$ and the value $A(0,1)=\theta \sigma_{2}^{2}$ whichever is the largest.

The closed-form solutions have been verified by a specially designed computer program for determining the global maximum of expression (33). Here is a test example assuming material characterised by $K_{\text {Ic }}=45 \mathrm{MPa} \sqrt{m}$, $K_{\text {IIc }}=31.5 \mathrm{MPa} \sqrt{m}$. A weak globular brittle flaw which cracks easily has been assumed, with diameter $2a=600 \mu \mathrm{m}$. The principal stresses characterising the flaw location are $\sigma_{1}=1500 \mathrm{MPa}$, $\sigma_{2}=400 \mathrm{MPa}$ and $\sigma_{3}=-610 \mathrm{MPa}$.

The calculated numerical values for the constants $\theta=\frac{4}{\pi K_{\mathrm{Ic}}^{2}} a$ and $\gamma=\frac{Y^{2}}{K_{\mathrm{IIc}}^{2}} a$ are $\theta \approx 0.19 \times 10^{-6} \mathrm{MPa}^{-2}$ and $\gamma \approx 0.95 \times 10^{-6} \mathrm{MPa}^{-2}$. For the shape factor $Y$, $Y \approx 1$ has been assumed.

A global maximum $\max A(t_{1},t_{2})=1.1$ of expression (33) attained at $t_{1}^{*}= \pm 0.746$, $t_{2}=0$ was found by the specially developed program. These values were confirmed by substituting the numerical values of the parameters in the closed-form solutions.

Now let us assume that $\theta=\gamma$. Maximising
$$
G\left(t_{1}^{*}, t_{2}^{*}\right)=K_{\mathrm{I}}^{2} \theta+K_{\mathrm{II}}^{2} \theta
\tag{40}
$$

is reduced to maximising $K_{\mathrm{I}}^{2}+K_{\mathrm{II}}^{2}$, equivalent to maximising
$$
\begin{aligned}
A\left(t_{1}, t_{2}\right)= & \sigma_{n}^{2}+\tau^{2}=\left[t_{1}^{2} \sigma_{1}+t_{2}^{2} \sigma_{2}+\left(1-t_{1}^{2}-t_{2}^{2}\right) \sigma_{3}\right]^{2} \\
& +\left[\left(\sigma_{1}-\sigma_{2}\right)^{2} t_{1}^{2} t_{2}^{2}+\left(\sigma_{2}-\sigma_{3}\right)^{2} t_{2}^{2}\left(1-t_{1}^{2}-t_{2}^{2}\right)\right. \\
& \left.+\left(\sigma_{1}-\sigma_{3}\right)^{2} t_{1}^{2}\left(1-t_{1}^{2}-t_{2}^{2}\right)\right]^{1 / 2}
\end{aligned}
\tag{41}
$$

Again, the local extrema can be found by using the necessary conditions (34), leading to the non-linear system
$$
t_{1}\left[\frac{1}{2}\left(\sigma_{1}-\sigma_{3}\right)+\sigma_{3}\right]=0
\tag{42}
$$

$$
t_{2}\left[\frac{1}{2}\left(\sigma_{2}-\sigma_{3}\right)+\sigma_{3}\right]=0
\tag{43}
$$

with the only (trivial) solution $t_{1}=t_{2}=0$ and no non-trivial solutions. The global maximum of $A(t_{1},t_{2})=\sigma_{n}^{2}+\tau^{2}$ is attained either at $t_{1}=t_{2}=0$ or at the boundary $t= \pm 1,0$ or $t=0, \pm 1$. Again, $A(+1,0)=A(-1,0)$ and $A(0,+1)=A(0,-1)$. Consequently, the global maximum is determined from a comparison of three values: the value $A(0,0)=\sigma_{3}^{2}$, the value $A(1,0)=\sigma_{1}^{2}$ and the value $A(0,1)=\sigma_{2}^{2}$ whichever is largest.

### 4.1. Application of the new criterion for conservative design calculations

The proposed analytical criterion for crack initiation can also be applied in a traditional deterministic design

based on fracture mechanics, to determine for a flaw of given size, at a particular location, whether an unstable crack will be initiated. A criterion based on the maximum principal tensile stress may lead to a non-conservative design if the material is anisotropic. Given the stress tensor components $(\sigma_x, \sigma_y, \sigma_z, \tau_{xy}, \tau_{yz}, \tau_{zx})$ at the location characterised by the largest stresses and the largest possible flaw size $a_{\text{max}}$, the procedure for applying the new criterion involves the following steps:

1. Solving the cubic equation
$$\sigma_{\mathrm{p}}^{3}-I_{1} \sigma_{\mathrm{p}}^{2}+I_{2} \sigma_{\mathrm{p}}-I_{3}=0$$
with respect to $\sigma_{\mathrm{p}}$, where $I_{1}=\sigma_{x}+\sigma_{y}+\sigma_{z}$, $I_{2}=\sigma_{x} \sigma_{y}+\sigma_{y} \sigma_{z}+\sigma_{z} \sigma_{x}-\tau_{x y}^{2}-\tau_{y z}^{2}-\tau_{z x}^{2}$, and $I_{3}=\sigma_{x} \sigma_{y} \sigma_{z}-\sigma_{x} \tau_{y z}^{2}-\sigma_{y} \tau_{z x}^{2}-\sigma_{z} \tau_{x y}^{2}+2 \tau_{x y} \tau_{y z} \tau_{z x}$ are the stress invariants, yields the principal stresses $\sigma_{1}, \sigma_{2}$ and $\sigma_{3}$.

2. The second step involves determining the maximum of $A(t_{1}, t_{2})=\sigma_{n}^{2} \theta+\tau^{2} \gamma$ where $\theta=\frac{4}{\pi K_{\mathrm{Ic}}^{2}} a_{\mathrm{max}}$ and $\gamma=\frac{\gamma^{2} \pi}{K_{\mathrm{IIc}}^{2}} a_{\mathrm{max}}$ are constants depending on the size $a_{\text{max}}$ of the Worst- case flaw. This maximum is obtained by following the procedure described in the previous section. The maximum is compared to unity and if $\max \{A(t_{1}, t_{2})\}>1$, the flaw is unstable and will initiate failure. Thus, following the numerical example from the previous section, the obtained global maximum $\max A(t_{1}, t_{2})=1.1$ indicates that the flaw with diameter $600\ \mu\text{m}$ is unstable and will initiate failure.

## 5. A new technology for selecting designs and loading associated with increased resistance to brittle failure initiated by flaws

The new mixed-mode failure criterion and Eq. (21) were used as a basis of a new technology for comparing design alternatives and selecting the alternative characterised by the highest resistance to overstress failure. The new technology involves four basic steps.

1. The same material properties for the compared design alternatives (fracture toughness $K_{\text{Ic}}$ and $K_{\text{IIc}}$) and the same number density and size distribution of flaws are assumed for the compared design alternatives.
We need to point out that the flaw number densities and the flaw size distributions do not have to be the real number densities and size distributions in the material. The assumed number density $\lambda$ of the flaws and their size distribution are used for comparing the failure resistance of the design alternatives.The design modifications affect only the shape of the components but the material is the same.

An advantage of the proposed method for selecting designs is that it does not require precise knowledge of the size distribution of flaws and the material properties. These are usually characterised by a great deal of uncertainty. Because the method is comparative, the same material properties and size distribution of flaws can be used for all design alternatives, which essentially blocks out uncertainty associated with the material properties and the population of internal flaws.

2. For each design alternative, a finite element solution is produced. In the output file, the principal stresses at the centroids of all finite elements as well as the volumes of the finite elements are listed.

3. The probabilities of failure associated with each design alternative are calculated by using the method outlined in Section 3.

For a specified number of Monte Carlo simulation trials, random locations are generated in the component. At each random location with coordinates $(x,y,z)$, a random flaw size is sampled from the flaw size distribution. The mixed-mode fracture criterion outlined in Section 4 is then applied for the generated random location and size of the flaw to check whether the flaw will initiate fracture.

The candidate values for a global maximum of the criterion (28) are the local maximum:
$$
\begin{aligned}
& A_{\text{max}} \\
& \quad=\frac{1}{(1-\theta / \gamma)^{2}}\left(\frac{\left(\sigma_{1}+\sigma_{3}\right)^{2}}{4} \theta+\left(\frac{\sigma_{1}-\sigma_{3}}{2}+\frac{\theta \sigma_{3}}{\gamma}\right)\left(\frac{\sigma_{1}-\sigma_{3}}{2}-\frac{\theta \sigma_{1}}{\gamma}\right) \gamma\right),
\end{aligned}
$$
and the values $A(0,0)=\theta \sigma_{3}^{2}$, $A(1,0)=\theta \sigma_{1}^{2}$ and $A(0,1)=\theta \sigma_{2}^{2}$ whichever is the largest.

If the global maximum exceeds unity then failure is present and the failure simulation counter is incremented. The simulation then continues with generating another random location for the flaw.

The conditional individual probability of triggering fracture $F_{\text{ci}}$ characterising a single flaw in the $i$th design alternative is estimated by dividing the number of simulations $N_{\text{fi}}$ in which the flaw 'has initiated' fracture to the total number $N$ of Monte Carlo simulation trials $(F_{\text{ci}} \approx N_{\text{fi}}/N)$. Once $F_{\text{ci}}$ has been estimated, it is plugged into the equation $p_{\text{fi}}=1-\exp(-\lambda V_{i} F_{\text{ci}})$ to estimate the probability of failure charcterising the $i$th design alternative.

4. The probabilities of overstress failure characterising the separate design alternatives are compared and the design alternative characterised by the smallest probability of failure is selected.

Following the described steps, a postprocessor was written in C++ for assessing the resistance of designs to overstress failure initiated by flaws. Essential parts of the postprocessor are two blocks: a block for reading the output data file from the ABAQUS software package for finite element analysis and a block for calculating the probability of failure. For each finite element, the first block extracts the principal stresses characterising the centroid of the element and its volume. The second block performs the actual simulation to determine the conditional individual probability of failure initiated by a flaw. According to the

![](./images/811966159929737218_8.jpg)

Fig. 6. Two design alternatives of a fixed bracket, loaded by an uniformly distributed pressure of the same magnitude.

discussion in Section 3, in order to determine this probabil- ity, it is assumed that the flaw exists in the volume of the component with certainty. A random selection of the flaw is made by a random selection of a finite element, with probability proportional to its volume. The algorithm for this selection is based on creating a cumulative array dur- ing the phase involving reading the volumes of the finite elements from the ABAQUS data file. The cumulative array is ordered in ascending order, and each of its compo- nents contains the sum of the finite element volumes with smaller index. A uniformly distributed random number $u_V$ in the range $(0, V)$ is generated first, where $V$ is the total volume of the component. A binary search in the ordered cumulative array identifies the index of the finite element selected by the uniformly distributed random number $u_V$. The process of random selection resembles spinning a rou- lette wheel whose sectors have different size. In this process, each finite element is selected with probability proportional to its size.

After selecting a random location, a random size for the flaw is generated by sampling its size distribution and the mixed-mode failure criterion described in Section 4 is applied to check whether the flaw will be unstable. The number of simulations during which the flaw has initiated failure is divided by the total number of simulations to determine the conditional probability of failure $F_c$ initiated by a single flaw given that it resides in the component. This probability, substituted in Eq. (21) then yields the probabil- ity of failure of the component.

### 5.1. Selecting a component shape associated with the largest resistance to overstress failure initiated by flaws

The calculations are illustrated by the example in Fig. 6 which involves two fixed brackets with dimensions shown in the figure, loaded in exactly the same way (uniformly dis- tributed pressure of magnitude $166.7\ \text{N/mm}^2$ over an area of $20\ \text{mm} \times 30\ \text{mm}$). The assumed size distribution of the flaws is log-normal. All dimensions in the figure are in mil- limetres. The mean of the logarithms of the actual size of the flaws is $\mu_{\ln}=5\ \mu\text{m}$ with a standard deviation $\sigma_{\ln}=$ 0.5. A random flaw size is obtained by first generating a random number $u_{\ln}$ following the Gaussian distribution with mean $\mu_{\ln}$ and standard deviation $\sigma_{\ln}$. The actual, log- normally distributed flaw size $D$ is obtained by exponenti- ating the random number $u_{\ln}$: $D = \exp(u_{\ln})$. (The flaw size $D$ is log-normally distributed because its logarithm is nor- mally distributed).

Finally, the fracture toughness of the material has been specified to be $K_{Ic}=25\ \text{MPa}\sqrt{m}$ and $K_{IIc}=21\ \text{MPa}\sqrt{m}$. The parameter $\lambda$ (expected number density of flaws) has been assumed to be the same for both brackets: $\lambda_A = \lambda_B=2$ defects per $\text{cm}^3$. Since the volumes of the brackets are $V_A=49.89\ \text{cm}^3$ and $V_B=44.4\ \text{cm}^3$ respec- tively, the expected number of flaws in the brackets are $\lambda_A \times V_A \approx 100$ and $\lambda_B \times V_B \approx 89$.

For the two designs, conditional individual probabilities $F_{cA}=0.0032$ and $F_{cB}=0.000223$ have been estimated from 1000,000 Monte Carlo simulation trials. Substituting these probabilities in Eq. (21) resulted in $p_{\text{flaws},A}=1-$ $\exp(-\lambda_A V_A F_{cA})=0.27$ and $p_{\text{flaws},B}=1-\exp(-\lambda_B V_B$ $F_{cB})=0.019$ for the probability of failure. As can be veri- fied, design '$B$' is characterised by a probability of failure approximately fourteen times smaller than the probability of failure characterising design '$A$'.

## 6. Conclusions

1. A comparative method has been proposed for selecting designs with high resistance to overstress failure initiated by flaws. The method is based on an equation proposed earlier, a new mixed-mode failure criterion for crack ini- tiation from spherical flaws and efficient simulation algorithm for determining the probability of failure ini- tiated by flaws.
2. Because the proposed approach is comparative, the same set of material properties and size distribution of flaws can be used for all design alternatives. This

essentially blocks out uncertainty associated with the material properties and the actual population of internal flaws.

3. A new mixed-mode criterion for crack initiation on spherical flaws has been derived in cases where the crack does not exist and its potential plane can be oriented in any direction. The proposed analytical criterion of crack initiation can be applied in conservative design calcula- tions, to determine for a spherical defect of a given size, at a particular location, whether an unstable crack will be initiated.

4. The existing statistical theories of brittle fracture specify the probability of fracture as a function of the number density of the critical defects, which has no physical basis, cannot be measured directly and needs to be determined from failure data. In cases where this quan- tity is determined from mechanical tests, the evaluated quantity is a function of the type of test, the size of the component and component geometry.

5. In order to determine the probability of failure initiated by flaws, the traditional statistical theories rely on a power function for the stress dependence of the number density of critical flaws. For inhomogeneous material containing flaws, the counter-examples developed in the paper demonstrate common cases where the power function is inappropriate for describing the stress depen- dence of the number density of the critical flaws.

## References

[1] W. Weibull, Journal of Applied Mechanics 18 (1951) 293-297.

[2] J. Lamon, Journal of the American Ceramics Society 71 (2) (1988) 106-112.

[3] S.B. Batdorf, J.G. Crose, Journal of Applied Mechanics 41 (1974) 459-464.

[4] A.G. Evans, Journal of the American Ceramic Society 61 (1978) 302-308.

[5] A.G. Evans, R.L. Jones, Journal of the American Ceramic Society 61 (1978) 157-160.

[6] J.H. Andreasen, Journal of the American Ceramics Society 76 (11) (1993) 2933-2935.

[7] S. Duffy, L.A. Janosik, A.Wereszak, B. Schenk, A. Suzuki, J. Lamon, D.J. Thomas, Life prediction of structural components, in: Proceed- ings of the 28th Annual Cocoa Beach Conference and Exposition on Advanced Ceramics and Composites, Ceramics and Components in Energy Conversion Systems Symposium, 28 January 2004.

[8] N.N. Nemeth, Predicting the reliability of ceramic and graphite components under generalized loads with CARES/Life, in: Proceed- ing of the 6th International Nuclear Graphite Specialist Meeting, Chamonix, September, 18-21, 2005.

[9] R. Danzer, T. Lube, Fracture Mechanics of Ceramics 11 (1996) 425-439.

[10] S.B. Batdorf, M.L. Heinisch Jr., Journal of the American Ceramic Society 61 (1978) 355-358.

[11] J. Lamon, A.G. Evans, Journal of the American Ceramics Society 66 (3) (1983) 177-182.

[12] S. Gerguri, L.J. Fellows, J.F. Durodola, N.A. Fellows, A.R. Hutchinson, T. Dickerson, Applied Mechanics and Materials 1-2 (2004) 113-119.

[13] T.L. Anderson, Fracture Mechanics: Fundamentals and Applica- tions, Taylor and Francis, 2005.

[14] M.T. Todinov, Computational Materials Science 32 (2005) 156-166.

[15] M.T. Todinov, Probabilistic Engineering Mechanics 22 (2007) 12-21.

[16] N.E. Dowling, Mechanical Behaviour of Materials, second ed., Prentice Hall, 1999.

[17] D. Broek, Elementary Engineering Fracture Mechanics, fourth ed., Kluwer Academic Pubs., Dordrecht, 1986.

[18] M.L. Williams, Journal of Applied Mechanics 24 (1957) 109-114.

[19] P.C. Paris, G.C. Sih, Stress analysis of cracks. in: Fracture Toughness Testing and Its Application, American Society for Testing and Materials, Annual Meeting, 67th, Chicago, 21-26 June,1964-1965.

[20] R.J. Nuismer, International Journal of Fracture 11 (2) (1975) 245-250.