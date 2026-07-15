## Full length article
# A mean-field model of static recrystallization considering orientation spreads and their time-evolution

A. Després $^{a,c,*,}$ M. Greenwood $^{b}$, C.W. Sinclair $^{a}$

$^{a}$ Department of Materials Engineering, The University of British Columbia, 309-6350 Stores Road, Vancouver, Canada
$^{b}$ Natural Resources Canada, CanmetMATERIALS, Hamilton, ON L8P 0A5, Canada
$^{c}$ Univ. Grenoble Alpes, Grenoble INP, SIMaP, Grenoble F-38000, France

---

### ARTICLE INFO

**Article history:**
Received 11 May 2020
Revised 30 July 2020
Accepted 4 August 2020
Available online 18 August 2020

**Keywords:**
Recrystallization
Abnormal growth
Anisotropy
Vertex

---

### ABSTRACT

In this paper, we develop a mean-field model for simulating the microstructure evolution of crystalline materials during static recrystallization. The model considers a population of individual cells (i.e. grains and subgrains) growing in a homogeneous medium representing the average microstructure properties. The average boundary properties of the individual cells and of the medium, required to compute growth rates, are estimated statistically as a function of the microstructure topology and of the distribution of crystallographic orientations. Recrystallized grains arise from the competitive growth between cells. After a presentation of the algorithm, the model is compared to full-field simulations of recrystallization performed with a 2D Vertex model. It is shown that the mean-field model predicts accurately the evolution of boundary properties with time, as well as several recrystallization parameters including kinetics and grain orientations. The results allow one to investigate the role of orientation spreads on the determination of boundary properties, the formation of recrystallized grains and recrystallization kinetics. The model can be used with experimentally obtained inputs to investigate the relationship between deformation and recrystallization microstructures.

Crown Copyright © 2020 Published by Elsevier Ltd on behalf of Acta Materialia Inc. All rights reserved.

---

## 1. Introduction

In most models of static and dynamic recrystallization, recrystallized grains arise from a competitive growth of subgrains or cells pre-existing in the deformed microstructure [1-9]. In high stacking fault energy materials, the force driving the growth of subgrains comes almost entirely from the interfacial tension of the subgrain network (e.g. aluminium alloys [5]), while the energy stored in tangled dislocations plays a more important role as the stacking fault energy decreases (e.g. silver and nickel [2], copper [2,6,8]). While the micro-mechanisms at the origin of recrystallization are well known, the conditions leading to the development of recrystallized grains of particular orientations, and their incidence on the kinetics, remain difficult to identify.

This challenge is to a great extent due to the large number of features involved in recrystallization. Deformed grains contain of the order of $10^5$ subgrains [5], out of which a handful turn into recrystallized grains during annealing. State-of-the-art full-field models (e.g. phase field, Vertex dynamics, level-set) can simulate this many subgrains [10,11], but this is still insufficient to confidently predict recrystallization kinetics, grain size and crystallographic texture. As a result, the most significant applications of full-field models to recrystallization remain restricted to comparison with analytical model predictions [4,7] or to parametric studies on the role of some initial microstructure parameters [3,12].

Mean-field models are computationally more efficient than full-field models, but are limited by additional assumptions. In the early model of Bailey and Hirsch [1,2], a subgrain is considered as a potential recrystallized grain when its radius exceeds the value where its inward capillary pressure is overcome by the outward pressure induced by its neighbours. This model was extended by Zurob et al. [6] to predict the incubation period during which future recrystallized grains grow normally compared to the rest of the microstructure. This approach, however, misses the fact that every growing subgrain satisfies the Bailey-Hirsch criterion [1,2]. Meeting the Bailey-Hirsch criterion is necessary but insufficient for a subgrain to become a grain in the recrystallized state. In two separate publications, Humphreys [13], and Rollett and Mullins [14] proposed an approach that considers that a recrystallized grain forms when the growth rate of a subgrain relative to the average is positive. Notably, the model highlights the role of heterogeneous subgrain size and boundary properties on

---

* Corresponding author at: Department of Materials Engineering, The University of British Columbia, 309-6350 Stores Road, Vancouver, Canada.
E-mail address: arthur.despres@alumni.ubc.ca (A. Després).

https://doi.org/10.1016/j.actamat.2020.08.013
1359-6454/Crown Copyright © 2020 Published by Elsevier Ltd on behalf of Acta Materialia Inc. All rights reserved.

![](./images/812578757805080577_1.jpg)
![](./images/812578757805080577_2.jpg)
![](./images/812578757805080577_3.jpg)

the onset of recrystallization. Despite a few interesting applications to experimental cases [5,15], and comparisons to full-field simulations [4,16], this approach remains much less popular than those relying on the Bailey-Hirsch criterion (e.g. [8,9,17,18]).

As the microstructural heterogeneities giving rise to recrystallization develop during prior deformation, substantial efforts have also been made to simulate recrystallization from outputs of crystal plasticity models. In these cases, heterogeneities of subgrain size and disorientation have been attributed to inter-granular contrast of slip activity (estimated by Taylor factors) [19], resolved shear stress [20], and intragranular disorientation levels [21]. These approaches generally focus on predicting the texture out of these heterogeneities while ignoring the recrystallization kinetics.

In this paper, we propose an extended mean-field model that builds on the approaches described above. In our approach, a discrete population of subgrains evolves according to classic cellular growth laws, with a time-integration scheme implemented to update the microstructural parameters. The recrystallized grains are identified based on a size threshold. The model extends beyond classic mean-field approaches by accounting for the variation of subgrain properties with crystallographic orientation by tracking the moments of several boundary property distributions. As a result, recrystallization kinetics and recrystallized grain orientations are predicted together. This model is tested against full-field vertex simulations of subgrain growth and its extension to predicting experimental results is discussed.

The paper starts by briefly introducing the methodology used for Vertex simulations. This serves to also familiarize the reader with the topology of the microstructures investigated. Next, the mean-field model is introduced. In the following sections, the ability of the mean-field model to reproduce the full-field simulations is shown, with a discussion on the strengths, weaknesses and areas for further improvement.

## 2. Full-field simulations

The conditions simulated in this work by the full-field model can be viewed as the recrystallization of a deformed grain in a high stacking fault energy material (e.g. an aluminium alloy or a ferritic steel). These will provide a means to validate the mean-field model in a configuration where the boundary properties and the topology of the microstructure are very well known. Yet, some differences with experiments will be noticed: (i) the dimensionality of the microstructure, (ii) the absence of spatial correlations between subgrain orientations, and (iii) the absence of large scale heterogeneities. These aspects will be discussed later in this work.

### 2.1. 2D Vertex dynamics

The 2D Vertex model simulations were performed following the methods described in [22-24]. In this model, grain and subgrain boundaries are discretized into vertices located at triple junctions and along boundaries, and the velocities of each vertex calculated as a function of the capillary forces exerted by its adjoining segments. Topological transformations account for the removal of boundaries when two triple junctions meet [22], when cells become smaller than a critical size [22], or when contacts between colliding boundaries occur [23,24]. A single empirical coefficient controls the triggering of these transformations which, if set small enough, does not influence the results [22-24].

If differences in volumetric energy across boundaries are neglected, the evolution of the boundary network is controlled by the microstructure topology, the boundary energies (inducing capillary forces) and their mobilities. As in previous work on recrystallization [4,13,25], the boundary energy and mobility are assumed to be functions of the boundary disorientation¹ angle $\theta$. For the purposes of this study the boundary energy $\gamma(\theta)$ is taken to obey the Read-Shockley equation [27]:

$$
\gamma(\theta)=
\begin{cases}
\gamma_{c} \frac{\theta}{\theta_{c}}\left(1-\ln \frac{\theta}{\theta_{c}}\right) & \text { if } \theta \leq \theta_{c} \\
\gamma_{c} & \text { if } \theta>\theta_{c}
\end{cases} \tag{1}
$$

Where $\gamma_{c}$ is a constant, $\theta_{c}$ is a cut-off angle set to $15^{\circ}$ to simulate a high angle boundary. The boundary mobility $\mu(\theta)$ was set to follow the empirical relation [13,25]:

$$
\mu(\theta)=\mu_{c}\left(1-e^{-B\left(\frac{\theta}{\theta_{c}}\right)^{\eta}}\right) \tag{2}
$$

Where $\mu_{c}$ is a constant, $B=5$ and $\eta=4$, following classic work on aluminium alloys [13,25].

![](./images/812578757805080577_4.jpg)

Fig. 1. (a) In dots, an orientation spread represented in the quaternion vector space. The trivariate normal distribution is also represented, with $\sigma_{(0)}^{ref}$ the standard deviation in the three directions. (b) The distribution of disorientation angles $\omega$ for an isotropic spread $\sigma_{(0)}^{ref}=3.5^{\circ}$.

### 2.2. Microstructure construction

The starting subgrain microstructures were constructed by Voronoi tessellation with periodic boundary conditions. Each Voronoi cell constitutes a subgrain, while the whole microstructure can be considered as the interior of a deformed grain. A first relaxation of the microstructure was performed by setting all boundary mobilities and energies equal, until the subgrain radii reached the self-similar distribution associated with normal growth (i.e. for 2 dimensional microstructures a Rayleigh distribution with maximum around 2 times the mean radius [22,28,29]). The results presented in this paper were obtained from averages of 6 simulations performed with $2.5 \times 10^{4}$ subgrains in this 'as-relaxed' state. The recrystallization kinetics does not vary significantly between the simulations. This procedure was implemented only to increase the number of recrystallized grain orientations sampled.

Each subgrain in the 'as-relaxed' microstructure was assigned a crystallographic orientation assuming cubic symmetry and no spatial correlation. Orientations are described here by their disorientation relative to an arbitrary reference orientation, and denoted in quaternion vector part $\delta \boldsymbol{r}^{ref}=(r_{1}, r_{2}, r_{3})^{ref} \sin (\omega / 2)$, with $(r_{1}, r_{2}$, $r_{3})^{ref}$ the disorientation axis and $\omega$ the disorientation angle. This notation is commonly used to describe orientations spread around the mean orientation of deformed grains [21,30,31]. The initial orientations are drawn from a trivariate normal distribution along the principal directions $\delta \boldsymbol{r}_{1}, \delta \boldsymbol{r}_{2}, \delta \boldsymbol{r}_{3}$ of the reference frame. The distribution is centered on (0, 0, 0) and controlled through an isotropic

---
¹ Following the standard terminology [26], a misorientation is defined as a rotation (described by an axis and an angle) that transforms one crystalline orientation into another. The disorientation is the misorientation having the smallest rotation angle out of all misorientations allowed by the crystal symmetry.

![](./images/812578757805080577_5.jpg)

Fig. 2. (a) initial microstructure simulated with Vertex dynamics for a spread $\sigma^{ref}$=3.5°. (b) same microstructure at 50% recrystallization. In the bottom right corner, separated from the top right corner by the diagonal line, recrystallized grains are highlighted in brighter colors. Only half of the microstructure appears on the figures.

standard deviation $\sigma_{(0)}^{ref}$, set identical in the three directions. It remains a trivariate normal distribution as long as the largest disorientation vectors (imposed by $\sigma_{(0)}^{ref}$) do not exceed the bounds of the orientation space set by the symmetry of the crystal. By convention, we consider only positive disorientation angles with the vector direction carried by the sign of the rotation axis. A representation of the reference disorientation distribution is shown in Fig. 1. An example of a relaxed microstructure is shown in Fig. 2a.

As the reference disorientation vectors follow a trivariate normal distribution, their norms follow a Maxwell distribution and in the limit of small angles so too does the distribution of reference disorientation angles $\omega$ (Fig. 1b). This kind of distribution provides a good first order approximation to orientation spreads found experimentally within deformed grains [30,32,33]. In a similar way, boundary disorientations (i.e. disorientations calculated between pairs of spatially adjacent cells) are denoted $\delta r^{b}=(r_{1}, r_{2}, r_{3})^{b}\sin(\theta/2)$. As the cell orientations are spatially uncorrelated, the distribution of boundary disorientation angles also follows a Maxwell distribution² [21,32,33].

Adopting a definition used in previous work [4,12], recrystallized grains are defined as subgrains whose equivalent area radius is greater or equal to eight times the mean radius in the relaxed microstructure. Fig. 2b shows the microstructure at 50% recrystallized fraction. The exact value of the threshold recrystallized grain radius does not influence the comparison of the results as it will be set the same for the full-field and mean-field models.

## 3. The mean-field model of cellular growth

Following the approach of Humphreys [13] and Rollett and Mullins [14], the microstructure is considered in the mean-field model as a set of grains and subgrains embedded in a homogeneous medium representing the average properties of the microstructure. Growth rates of grains and subgrains are calculated from classic capillary growth laws, and a time-integration scheme is used to update the microstructure. At each time step, the mean boundary energies and mobilities required to compute growth rates are estimated from the moments of the boundary disorientation angle distribution. Here, the mean (first moment) and variance (centered second moment) of the disorientation angle distribution are estimated in a statistical sense from knowledge of the orientation spread and of potential spatial correlations between orientations. This approach differs from most traditional mean-field models, where boundaries properties are fixed from the start and recrystallized grains explicitly associated with a generic high angle boundary [2,6,9,21]. By considering the role of orientation spread on the determination of boundary properties, this model allows the recrystallization kinetics and recrystallized grain orientations to evolve together.

### 3.1. Growth equations and time integration

We consider a set of individual cells characterized by radius $R_{(i,t)}$, mean boundary energy $\Gamma_{(i,t)}$ and mean boundary mobility $M_{(i,t)}$, embedded in a homogeneous medium of properties $\bar{R}_{(t)}$ and $\bar{\Gamma}_{(t)}$. The subscript $i$ denotes the cell index, and $t$ is the simulation time. Cells comprise all grains and subgrains in the microstructure, the same laws being applied to all objects. At $t=0$, the input radii correspond to the measurements in the as-relaxed full-field microstructure. On the other hand, the assignment of unique boundary properties to cells having multiple neighbours is one major approximation of this model, and will be treated below. Assuming that the above defined cell properties are known, the growth rate of a two dimensional cell is given by Rollett [14]:

$$
\frac{d R_{(i,t)}}{d t}=\frac{M_{(i,t)} \Gamma_{(i,t)}}{R_{(i,t)}}\left(\frac{a_{(i,t)} n_{(i,t)}}{6}-1\right) \tag{3}
$$

Where $n_{(i,t)}$ is the number of sides (or neighbours) of the cell, and $a_{(i,t)}=6 \sin ^{-1}\left(\bar{\Gamma}_{(t)} / 2 \Gamma_{(i,t)}\right) / \pi \leq 3$ accounts for the effect of boundary curvature on the growth rate. For two-dimensional microstructures, a linear relation can be assumed between the number of sides of a cell and its size such that $n_{(i,t)}=3\left(1+R_{(i,t)} / \bar{R}_{(t)}\right)$

² A Maxwell distribution of disorientation angles is a natural consequence of the operation of three orthogonal slip systems during plastic deformation [32,33]. Experimentally, the boundary disorientation angle distribution in fcc metals has is closer to a Rayleigh distribution [34], implying the domination of slip by two slip systems [33]

[14,35]. The growth rate equation is thus reduced to³ [14]:

$$
\frac{d R_{(i, t)}}{d t}=\frac{M_{(i, t)} \Gamma_{(i, t)}}{2 R_{(i, t)}}\left(a_{(i, t)}\left(1+\frac{R_{(i, t)}}{\bar{R}_{(t)}}\right)-2\right)
\tag{4}
$$

Then each cell radius is updated by integrating Eq. (4) with Eu- ler's method $R_{(i, t+d t)}=R_{(i, t)}+\frac{d R_{(i, t)}}{d t} \Delta t$. The microstructure coars- ening kinetics scales with the magnitude of the boundary mobility and energy laws $\mu_{c}$ and $\gamma_{c}$. The model's predictions were found insensitive to the choice of $\Delta t$ so long as the average increase in cell area per time increment remained below ~ 1%. Then, recrys- tallized grains are identified, as in the full-field simulations, based on a critical radius $R_{(i, t)} \geq R_{r x}=8 \bar{R}_{(0)}$.

After each time increment, the smallest cells and those of neg- ative radius are removed in order to maintain a constant total simulation area. This procedure is implemented to compensate for the fact that Eq. (4) (or Eq. (3)) does not intrinsically insure area conservation (i.e. $\sum_{i=1}^{n_{g}(t)} R_{(i, t+d t)} \frac{d R_{(i, t)}}{d t} \neq 0$ ). To correct this discrep ancy, one may further refine the contribution of the homogeneous medium to the growth rates [36], but this does not change the re- sults presented below. The total change in area was not more than8% and only transient; the total simulation area returns back to its original value before the onset of recrystallization. A reader wish- ing to replicate the prediction will notice the transient nature of this behaviour.

### 3.2. Boundary properties
To compute the growth rates in Eq. (4), one needs to know the mean boundary energy terms $\Gamma_{(i, t)}$ and $\bar{\Gamma}_{(i, t)}$ and mean mobility M(i.t). Here, we estimate them in two steps. First the moments of the boundary disorientation angle distribution are estimated sta- tistically from those associated with the reference disorientation distribution (i.e. the orientation spread) and from assumptions on the spatial correlations. Then, boundary properties are calculated assuming Taylor series expansion of the energy and mobility laws about the mean boundary disorientation angles.

First, the moments of the reference disorientation distribution are calculated in a statistical sense. As such, they carry no informa- tion on the neighbour to neighbour disorientations. The first mo- ment is (0, 0, 0) since orientations are centered on the average.The second moment is a 3x3 matrix given by Pantleon [31]:

$$
<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}=\frac{1}{n_{g}(t)} \sum_{i=1}^{n_{g}(t)} \delta \boldsymbol{r}_{(i)}^{r e f} \otimes \delta \boldsymbol{r}_{(i)}^{r e f}
\tag{5}
$$

Where $< >_{(t)}$ denotes the average of the quantity within brackets at time $t, \otimes$ is the dyadic product, and the sum runs over the $n_{g}(t)$ orientations. $^{4}$ Since the first moment is null, the second moment is also the covariance matrix of the distribu- tion. Its eigenvalues provide the square of the standard deviations(σ1), σ2), σ3)) of spread in the principal directions of the refer- ence frame. With an isotropic spread $\sigma_{(t)}^{r e f}=\sigma_{(t)}^{1}=\sigma_{(t)}^{2}=\sigma_{(t)}^{3}$.

Next, one can estimate the moments of the boundary disori- entation vector distribution from those associated with reference disorientations. Zecevic et al. [21] have shown that when the refer- ence disorientation vectors follow a trivariate normal distribution, the second moment of the boundary disorientation vector distri- bution for a cell of reference disorientation $\delta r_{(i)}^{r e f}$ can be expressedby:

$$
<\delta \boldsymbol{r}^{b} \otimes \delta \boldsymbol{r}^{b}>_{(i, t)}=\delta \boldsymbol{r}_{(i)}^{r e f} \otimes \delta \boldsymbol{r}_{(i)}^{r e f}+\left(<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}^{-1}+\frac{1}{\alpha} \boldsymbol{I}\right)^{-1}
\tag{6}
$$

Where $I$ is a $3 \times 3$ identity matrix, and $\alpha$ is the variance of a spatial correlation function of Gaussian form. This parame- ter ranges from 0 for high spatial correlation (i.e. when grains and subgrains of similar orientation are most likely to be adjacent) to+∞ for no correlation. For our case, where we assume no spatial correlations between orientations, $\alpha \to+\infty$ , and Eq. (6) simplifiesto:

$$
<\delta \boldsymbol{r}^{b} \otimes \delta \boldsymbol{r}^{b}>_{(i, t)}=\delta \boldsymbol{r}_{(i)}^{r e f} \otimes \delta \boldsymbol{r}_{(i)}^{r e f}+<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}
\tag{7}
$$

In Eqs. (6) and (7), the first term on the right represents the shift of the cell orientation from the reference frame, while the second term is the covariance matrix of the boundary disorien- tation distribution. In the case of Eq. (7), the covariance matrices of the reference and boundary disorientation vectors are identical, and the isotropic spread of the boundary disorientation distribu- tion becomes $\sigma_{(i, t)}^{b}=\sigma_{(t)}^{r e f}$ .

As the boundary disorientation vectors follow a trivari- ate normal distribution with non-zero mean, the variable $\Theta_{(i, t)}=\sqrt{\delta r_{(i, t)}^{b} \cdot \delta r_{(i, t)}^{b}} / \sigma_{(i, t)}^{b}$ follows a non-central $\chi$ distribution[37]. In addition, in the hypothesis of small angles, $\theta_{(i, t)} \approx$  $2 \sqrt{(\delta r_{(i, t)}^{b} \cdot \delta r_{(i, t)}^{b})}$ . With $\theta_{(i, t)}$ and $\Theta_{(i, t)}$ being proportional, the moments of the boundary disorientation angle distributions can be expressed as a function of the moments of the $\chi$ distribution forthe variable $\Theta_{(i, t)}$ :

$$
<\theta>_{(i, t)}=2 \sigma_{(i, t)}^{b} \sqrt{\frac{\pi}{2}} I_{1 / 2}^{(1 / 2)}\left(-\frac{\left(\kappa_{(i, t)}\right)^{2}}{2}\right)
\tag{8}
$$

$$
<\theta^{2}>_{(i, t)}=\left(2 \sigma_{(i, t)}^{b}\right)^{2}\left(3+\left(\kappa_{(i, t)}\right)^{2}\right)
\tag{9}
$$

Where $I_{1 / 2}^{(1 / 2)}$ is the Laguerre function of coefficients 1 / 2 and(1/2) (see Appendix B), and $\kappa_{(i, t)}$ is a scaling parameter defined by:

$$
\kappa_{(i, t)}=\frac{\sqrt{\delta \boldsymbol{r}_{(i)}^{r e f} \cdot \delta \boldsymbol{r}_{(i)}^{r e f}}}{\sigma_{(i, t)}^{b}} \approx \frac{\omega}{2 \sigma_{(i, t)}^{b}}
\tag{10}
$$

The approximation on the right side of the equation holds for small angles, and is shown only to highlight the dependency on the disorientation angle $\omega$ . Since the isotropic spread $\sigma_{(i, t)}^{b}$ is the same for all cells and equal to $\sigma_{(t)}^{r e f}$ , the parameter $\kappa_{(i, t)}$ is constant for a given reference disorientation angle $\omega$ .

The same method can be used to estimate the moments of the boundary disorientation vector distribution taken over the whole microstructure. This distribution is centered on (0, 0, 0), and itssecond moment is [21]:

$$
\begin{gathered}
<\delta \boldsymbol{r}^{b} \otimes \delta \boldsymbol{r}^{b}>_{(\forall i, t)}=\left(<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}^{-1}+\frac{1}{\alpha} \boldsymbol{I}\right)^{-1} \\
<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}^{-T}\left(<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}^{-1}+\frac{1}{\alpha} \boldsymbol{I}\right)^{-T} \\
+\left(<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}^{-1}+\frac{1}{\alpha} \boldsymbol{I}\right)^{-1}
\end{gathered}
\tag{11}
$$

Where $(\forall i)$ indicates that the average is now taken for all cells in the microstructure, and -T is the inverse of the transpose ma- trix. Considering, again, that $\alpha \to+\infty$ , Eq. (11) simplifies to:

$$
<\delta \boldsymbol{r}^{b} \otimes \delta \boldsymbol{r}^{b}>_{(\forall i, t)}=2<\delta \boldsymbol{r}^{r e f} \otimes \delta \boldsymbol{r}^{r e f}>_{(t)}
\tag{12}
$$

---
$^{3}$ We provide in Appendix A a similar expression of growth rates for microstruc tures in 3 dimensions.
$^{4}$ Weighting the second moment based on size, i.e. $\frac{1}{\sum_{i=1}^{n_{g}(t)} R_{(i, t)}} \sum_{i=1}^{n_{g}(t)} R_{(i, t)} \delta r_{i}^{r e f} \otimes$ δrref did not lead to improved predictions.

The isotropic spread of boundary disorientation vectors for the whole microstructure is thus equal to $\sigma_{(\forall i,t)}^{b}=\sqrt{2}\sigma_{(t)}^{ref}$. Since the distribution is centered on $(0,0,0)$, $\kappa_{(\forall i,t)}=0$, and the first and second moments of boundary disorientation angles follow$^{5}$:

$$
<\theta>_{(\forall i,t)}=2\sigma_{(\forall i,t)}^{b}\sqrt{\frac{\pi}{2}}L_{1/2}^{(1/2)}(0) \tag{13}
$$

$$
<\theta^{2}>_{(\forall i,t)}=12\left(\sigma_{(\forall i,t)}^{b}\right)^{2} \tag{14}
$$

Finally, the mean boundary energies and mobilities can be estimated from the moments of the boundary disorientation angle distributions. Expressing the mobility and energy laws by a second order Taylor series about the mean boundary disorientations gives the mean boundary mobilities and energies:

$$
\begin{aligned}
M_{(i,t)}=&<\mu(\theta)>_{(i,t)}=\mu\left(<\theta>_{(i,t)}\right) \\
&+\frac{\mu^{\prime \prime}\left(<\theta>_{(i,t)}\right)}{2}\left(<\theta^{2}>_{(i,t)}-\left(<\theta>_{(i,t)}\right)^{2}\right)
\end{aligned} \tag{15}
$$

$$
\begin{aligned}
\Gamma_{(i,t)}=&<\gamma(\theta)>_{(i,t)}=\gamma\left(<\theta>_{(i,t)}\right) \\
&+\frac{\gamma^{\prime \prime}\left(<\theta>_{(i,t)}\right)}{2}\left(<\theta^{2}>_{(i,t)}-\left(<\theta>_{(i,t)}\right)^{2}\right)
\end{aligned} \tag{16}
$$

$$
\begin{aligned}
\bar{\Gamma}_{(t)}=&<\gamma(\theta)>_{(\forall i,t)}=\gamma\left(<\theta>_{(\forall i,t)}\right) \\
&+\frac{\gamma^{\prime \prime}\left(<\theta>_{(\forall i,t)}\right)}{2}\left(<\theta^{2}>_{(\forall i,t)}-\left(<\theta>_{(\forall i,t)}\right)^{2}\right)
\end{aligned} \tag{17}
$$

As will be shown below, the second order terms are not necessary to capture the main trends of the microstructure evolution, but they substantially increase the accuracy of the prediction. The second derivatives of the mobility and energy functions are provided in Appendix C.

### 3.3. Algorithm

First, the model reads as input a list of subgrains characterized by their radii and orientations. Since an orientation is characterized by at least three parameters regardless of the representation space, the total is four parameters per subgrain. From the list of subgrain orientations, the reference orientation is computed as well as the reference disorientations. The initial simulation area is obtained from the sum of all subgrain areas in the input microstructure. In this case study, the input files were generated from the cell parameters of the relaxed Vertex microstructures. Other potential sources of input will be discussed below.

Next, the time iteration loop is started. From time $t$ to $t+dt$, the following sequence is executed:

1.  Identify the recrystallized grains based on the size criterion.
2.  Calculate the mean boundary properties $M_{(i,t)}$ and $\Gamma_{(i,t)}$ for each cell, and $\bar{\Gamma}_{(t)}$ for the whole microstructure using Eqs. (15), (16) and (17).
3.  Calculate the growth rate of each cell using Eq. (4).
4.  Integrate the growth rates over a time increment to update the cell radii. The new cell radii are representative of the microstructure at time $t+dt$.
5.  Remove the cells of negative radius and the smallest cells of positive radius so as to minimize the difference between the initial microstructure area and the sum of cell areas at $t+dt$.
6.  Update the average radius.

The only model parameter is the variance of the spatial correlation function $\alpha$, set to $+\infty$ (no correlation) in this case. The parameters controlling the boundary energy and mobility laws were set identical to the full-field simulation. Any other mobility and energy laws can be implemented as long as they are differentiable to the second order. This implementation is called the complete mean-field model for the rest of the paper.

## 4. Results

In this section, the mean-field model predictions are compared to a full-field simulation of recrystallization realized with an initial orientation spread of $\sigma_{(0)}^{ref}$=$3.5^{\circ}$. This value is in the range of experimental measurements in deformed polycrystalline materials [38,39]. The initial subgrain number density is denoted $\rho_{0}$. This parameter is used as a normalizing factor in much of the subsequent analysis.

To highlight the role of the different components of the mean-field model to the prediction of recrystallization parameters, four different ways of calculating the boundary properties are compared:

1.  Using only mean boundary disorientation angles (i.e. $0^{\text{th}}$ order Taylor series expansion), kept fixed with time and calculated initially at $t=0$.
2.  Using time-updated mean boundary disorientation angles.
3.  Using means and variances of the boundary disorientation angles (i.e. $2^{\text{nd}}$ order Taylor series expansion), kept fixed with time and calculated initially at $t=0$.
4.  Using time-updated means and variances of the boundary disorientation angles (i.e. complete model).

### 4.1. Prediction of recrystallization kinetics

To illustrate the influence of boundary properties and their time-evolution on the microstructure, Fig. 3 compares the full-field simulation of recrystallization kinetics to the four variants of the mean-field simulations. The recrystallized fraction $X$ is defined as the area of recrystallized grains divided by the total simulation area. The dotted grey line shows the predicted kinetics when the boundary properties are calculated using mean disorientation an-

![](./images/812578757805080577_6.jpg)

Fig. 3. Comparison of the recrystallization kinetics predicted by the mean- and full-field models. Time is normalized by $1/(\mu_{c}\gamma_{c}\rho_{0})$. Full-field simulations performed with the Vertex model appear as points (F-F.). Grey lines denote mean-field predictions made using only mean disorientation angles, either fixed (M-F.1) or time-updated (M-F.2). Black lines denote mean-field predictions made using means and variances of the disorientation angles, either fixed (M-F.3) or time-updated (M-F.4, i.e. complete model).

$^{5}$ Note than when $\kappa=0$, the $\chi$ distribution coincides with the Maxwell distribution cited earlier.

![](./images/812578757805080577_7.jpg)
![](./images/812578757805080577_8.jpg)

Fig. 4. Comparison of a) the recrystallized grain density $\rho_{rx}$ and b) the mean recrystallized grain radius $< R >_{rx}$ predicted by the mean- and full-field models. Time is normalized by $1/(\mu_{c}\gamma_{c}\rho_{0})$, recrystallized grain density by $\rho_{0}$ and recrystallized grain radius by the threshold recrystallized grain radius $R_{rx}$. Full-field simulations performed with the Vertex model appear as points (F-F.). Grey lines denote mean-field predictions made using only mean disorientation angles, either fixed (M-F.1) or time-updated (M-F.2). Black lines denote mean-field predictions made using means and variances of the disorientation angles, either fixed (M-F.3) or time-updated (M-F.4, i.e. complete model).

gles and are not updated with time. As a result, the recrystalliza- tion kinetics are overpredicted compared to the full-field simula- tion. Hurley and Humphreys arrived at the same result with simi- lar assumptions in their mean-field model [40]. The solid grey line shows results obtained when the boundary properties are calcu- lated using mean disorientation angles, but under the conditions that they are updated with time. The mean-field model predictions are not significantly improved.

A much better agreement is found between full-field and mean- field simulations when boundary energies and mobilities are cal- culated using both the means and variances of the boundary disorientation angle distributions (solid and dotted black lines). Updating the boundary properties is beneficial but of second order for the prediction of kinetics. In this case, the time at50% recrystallized fraction is predicted with less than 2% er- ror between the full-field simulation and the mean-field model prediction. Neither expanding the series expansion beyond the2nd order in Eqs. (15), (16) and (17), nor performing the se- ries expansion directly on growth rates significantly improved the predictions.

The same analysis is performed in Fig. 4 for the recrystallized grain density and size. These parameters are of interest as they di- rectly determine the recrystallization kinetics. Fig. 4a shows that the best agreement with the full-field simulation in terms of re- crystallized grain density $\rho_{rx}$ is obtained with the complete mean field model (solid black line). The differences between the full-field simulation and the four mean-field model predictions mirror those of the recrystallization kinetics shown in Fig. 3. In particular, one can see that only using the mean boundary disorientation angles to predict boundary properties (grey lines) significantly overpre- dicts the number of recrystallized grains and the time required for their appearance. This helps to explain the overpredicted kinetics in Fig. 3. The decrease in recrystallized grain density predicted by all implementations at long times corresponds to the coarsening of the recrystallized grain structure at the end of recrystallization. This non-monotonic evolution has been observed experimentally in aluminium alloys by Perryman et al. [41]. One may further re- mark that the ratio of recrystallized grains to initial subgrain den- sity is quite high ( $\sim 2$ out of $10^{3}$ for the full-field simulations) compared to 'a handful' out of $10^{5}$ stated in the introduction. This can be attributed to the fact that the initial full-field microstruc- ture is less heterogenous than that of most experimentally de- formed materials.

Fig. 4 b shows that the complete mean-field model (solid black line) predicts correctly the mean recrystallized grain radius $< R>_{rx}$ . One may notice that the implementations relying only on mean boundary disorientation angles (grey lines) yield even better predictions. This results from the faster predicted recrystallization kinetics, which translates the curve of recrystallized grain radius towards short times.

### 4.2. Prediction of recrystallized grain orientations

While the time evolution of boundary properties influences only moderately the recrystallization kinetics, it is a critical aspect for determining the recrystallized grain orientations. To illustrate this, Fig. 5 compares the distribution of grain and subgrain orien- tations predicted by the full-field model and by the two imple- mentations of the mean field model using means and variances of boundary disorientation angle distributions (i.e. $2^{nd }$ Taylor se ries expansion with fixed and updated boundary properties). As the orientation spread is isotropic, orientations can be plotted as a function of their reference disorientation angle $\omega$ . For the full field simulations (Fig. 5a), a preferential development of orienta- tions with large reference disorientation angle (i.e. with approxi- mately $\omega \geq 5^{\circ}$ ) in the recrystallized grains is observed. The ori entations that develop with highest fraction exhibit a compromise between fraction in the initial microstructure and magnitude of the disorientation angle. Without updating the boundary proper- ties with time, the mean-field model poorly captures this evolution(Fig. 5b). The agreement is improved when updating the properties with time (Fig. 5c). While in this case the mode of the distribution for the recrystallized grains is still lower than that simulated by the full-field model, the range of disorientation angles is very well captured.

In summary, the complete mean-field model yields the best predictions of recrystallization kinetics and grain orientations while also giving a good representation of the evolution of the mean recrystallized grain size. This implementation is kept for all following analyses.

![](./images/812578757805080577_9.jpg)

Fig. 5. Area fraction of grains and subgrains as a function of their reference disorientation angle $\omega$. (a) Full-field simulation, (b) mean-field simulation considering means and variances of boundary disorientation angle distribution fixed at their initial values, (c) mean-field model considering means and variances of boundary disorientation angle distribution updated with time. The initial microstructure dataset (in black) includes all grains and subgrains regardless of recrystallization, and is identical for (a), (b) and (c). The recrystallized grain datasets (red and blue) include only the recrystallized grains at specific recrystallized fractions. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

### 4.3. Prediction of boundary properties

To evaluate the success of the mean-field model in predicting boundary properties, one can directly track them in the full-field and complete mean-field models. Fig. 6 shows that the evolution of the first and second moments of the boundary disorientation angle distribution is well captured by the mean-field model. Both moments evolve in a non-monotonic way, comparable to experimental observations⁶ The magnitudes are well captured by the mean-field model, although the second moment tends to be underpredicted at longer times.

The same analysis is conducted in Fig. 7 for the boundary properties of individual cells as a function of their reference disorientation angle $\omega$. Again, the evolutions simulated by the full-field model are generally well reproduced by the mean-field model. Fig. 7a shows that the mean boundary disorientation evolution flattens for cells with a large reference disorientation angle $\omega$. This is explained by the fact that the second moment of the cell boundary distribution becomes less sensitive to the reference disorientation distribution as its own reference disorientation increases (see Eq. (7)). One can also notice, as in the previous figure, the strong relation between the evolution of the first and second moments of boundary disorientation (in Fig. 7a and b).

Overall, the non-monotonic evolution of boundary disorientation angles induces similar trends in the boundary energies and mobilities. Fig. 7c shows that the mean boundary mobility for orientations with small and large reference disorientation angles $\omega$ are well captured by the mean-field model while the mobility of those with intermediate angles is less well predicted. In Fig. 7d, the mean boundary energy are well predicted for the full range of reference disorientation angle, with again larger discrepancies for cells of intermediate disorientation angle.

⁶ Huang and Humphreys [25] reported a decrease of the mean boundary disorientation during annealing of a deformed aluminium monocrystal. Mishin et al. [42] showed a similar decrease then increase of the density of high angle boundaries during static recrystallization of a polycrystalline aluminium alloy.

![](./images/812578757805080577_10.jpg)

Fig. 6. (a) first moment and (b) square root of the second moment of the boundary disorientation distribution as a function of time. Time is normalized by $1/(\mu_{c}\gamma_{c}\rho_{0})$. Points are calculated from the list of boundary properties in the full-field simulation, while lines are the mean-field model predictions.

![](./images/812578757805080577_11.jpg)

Fig. 7. Cell boundary properties as a function of time for three intervals of reference disorientation angle $\omega$. (a) first moment and (b) square root of the second moment of the boundary disorientation angle distribution, (c) mean boundary mobility, (d) mean boundary energy. Time is normalized by $1/(\mu_{c}\gamma_{c}\rho_{0})$. Points are calculated from the list of boundary properties in the Vertex simulation, while lines are the mean-field predictions. The lines are calculated at the means of the reference disorientation angle intervals indicated on plot (d).

## 5. Discussion

### 5.1. Comments on the prediction of recrystallization kinetics

Fig. 3 has shown that the prediction of recrystallization kinetics by the mean-field model is particularly sensitive to the definition of boundary properties. Kinetics are overpredicted when consid- ering only the mean boundary disorientation angles to calculate the mean boundary mobilities and energies, in agreement with the previous attempt of Hurley and Humphreys [40]. The mean- field model prediction reaches a good agreement with the full- field simulation only by including the contribution of the variances of the boundary disorientation angle distributions. This improve- ment is due to the assumed boundary mobility and energy laws. Indeed, the second derivatives of the boundary energy and mobil- ity laws used for calculating the $2^{nd }$ order terms are mostly nega tive as a function of the disorientation angle $(\gamma^{\prime \prime}(\theta)$ is negative for $0^{\circ}<\theta<15^{\circ}$ and null above, $\mu^{\prime \prime}(\theta)$ is negative above $\sim 9^{\circ}$ , see Appendix C), thus reducing the predicted mean boundary proper- ties and growth rates for the majority of the recrystallized grains.

Most mean-field models of recrystallization are known to strongly overpredict the density of recrystallized grains. Making the assumption of a site saturation of recrystallized grains, Hur- ley and Humphreys have reported ratios of 2 to 3 between their model's prediction and experimental measurements at $50 \%$ recrys tallization [40]. In models relying on the Bailey-Hirsch criterion, the overprediction of recrystallized grain density is often hidden by assuming that only a fraction of the potential recrystallized grains actually nucleates. This is obtained either by multiplying the Bailey Hirsch criterion itself [18] or the number of subgrains meeting the Bailey-Hirsch criterion by fitting constants [6,17,43]. The present results suggest that accounting for the distribution of boundary properties and its time evolution provides a more physical solution to this problem.

One may remark, however, that the complete mean-field model still exhibits discrepancies in predicting the recrystallized grain density (solid black line in Fig. 4a). This may be caused by as- sumptions regarding the calculation of growth rates and boundary properties, but it may also be inherent to the mean-field formula- tion. As already suggested by Zurob et al. [6], the first recrystallized grains are likely to arise from locations where the energy, and thus the driving force, is higher than the average. Following this argu- ment, mean-field models should have a tendency to underpredict the time at which the first recrystallized grains appear. With the progress of recrystallization and the growth of grains, this effect should become less significant.

### 5.2. Boundary dynamics during annealing

One can understand the time-evolution of boundary properties shown in Figs. 6 and 7 by considering a schematic microstruc- ture composed of A and B subgrains. The A subgrains form the largest fraction of the microstructure, while the B subgrains pos- sess orientations which are far from the average. Fig. 8a illustrate the case of a small B subgrain embedded in an environment of A subgrains. Due to its size and its high angle boundaries, the B sub- grain shrinks and disappears, inducing a decrease in boundary dis- orientation angles associated with the A subgrains. By extension, it also slows down the average subgrain growth rates of the A sub- grains and prevents them from growing beyond their first neigh- bour and reaching the critical recrystallized grain size. This evolu- tion is analogous to the concept of orientation pinning sometimes invoked to explain texture development during recrystallization of aluminium alloys [44,45].

By contrast, in Fig. 8b the B subgrain is large enough (and has enough neighbours) to grow at the expense of the A subgrains.

![](./images/812578757805080577_12.jpg)

Fig. 8. Schematic microstructure of A and B subgrains, with (a) a small B subgrain shrinking. (b) a large B subgrain growing. High angle boundaries separate the A and B subgrains, while low angles separate subgrains of the same population.

As the environment of A subgrains remains, the boundary prop- erties of the B subgrain do not change with time. Due to the in- verse relation between growth rate and subgrain radius (Eq. 4), the shrinkage of small subgrains with high angle boundaries domi- nates the microstructure evolution during the early time of anneal- ing (Fig. 8a). Once these grains have disappeared, the large sub- grains grow and may turn into recrystallized grains surrounded by high angle boundaries (Fig. 8b). The improved prediction of the re- crystallized grain orientations in the complete mean-field model(Fig. 5c) results from taking account of this non-monotonic bound- ary dynamics. One can finally remark that reviews often make an explicit relation between the onset of recrystallization and the development of high angle boundaries [9,46,47]; in the present model, this situation results naturally from the dynamics of sub- grains in contact with high angle boundaries.

### 5.3. Possible effects of orientation spatial correlations

In the mean-field model presented above, spatial correlations between orientations have been introduced through the parame- ter $\alpha$ , which expresses the probability for grains and subgrains to share similar orientations with their neighbours [21]. As it is fixed for the whole microstructure, it cannot take account of large scale heterogeneities, like those found at deformed grain boundaries or shear bands. Fig. 9a shows that as $\alpha$ increases, i.e. as correlations vanish, the mean boundary disorientation angle increases towards a constant value. The synthetic full-field microstructures presented above were constructed to have no spatial correlations in the ini- tial state, thus motivating $\alpha$ to be $+\infty$ .

On the other hand, spatial correlations induced by disloca- tion slip are commonly observed experimentally in deformed mi- crostructures [48,49]. These correlations lower the average disori- entation between adjacent subgrains, but vanish beyond a few sub- grains in distance. This explains why the average boundary disori- entation is much higher in this study $(7.8^{\circ}$ at $t=0)$ than in pre vious experimental work $(1^{\circ} \sim 2^{\circ}[33], 2^{\circ} \sim 4^{\circ}[25])$ , while at the same time the orientation spread is in the range of experimental measurements. Fig. 9b suggests that the presence of spatial corre- lations, simulated by selecting lower values of $\alpha$ , would slow down the recrystallization kinetics. The consideration of this type of spa- tial correlations would also induce stronger variations of the pre- dicted time-evolution of the boundary properties.

It is also interesting to notice that spatial correlations may de- velop even if there are none at the initial state. Orientation pinning is one example where the local configuration of the microstruc- ture affects the evolution of boundary properties. In Fig. 8a, the B central subgrains shrinks because of its size and of its environ- ment of A subgrains. Thus, removal of the B subgrains preferen-

![](./images/812578757805080577_13.jpg)
![](./images/812578757805080577_14.jpg)

Fig. 9. (a) First moment of the boundary disorientation angle distribution $<\theta>^{(vi,t)}$ as a function of $\alpha$. (b) Effect of $\alpha$ on the prediction of recrystallization kinetics for the microstructure shown earlier.

![](./images/812578757805080577_15.jpg)

Fig. 10. Comparison of the mean boundary disorientation angle with the mean uncorrelated disorientation angle calculated from the Vertex microstructure.

tially brings the A subgrains in contact and induces spatial correlations. As shown by Fig. 10, this scenario is supported by measurements on the Vertex microstructure. In this figure, the mean boundary disorientation angle, measured from the list of boundary disorientation angles in the Vertex microstructure, is compared to the mean uncorrelated disorientation angle. To account for differences in cell size, the mean uncorrelated disorientation angle is calculated as follows: (i) each cell is paired with another cell selected at random, (ii) the number of pairs per cell is set proportional to its perimeter, and (iii) the mean uncorrelated disorientation angle is calculated as the mean disorientation angle between all the pairs. The deviation at long times between the mean boundary disorientation angle and the mean uncorrelated disorientation angle indicates the development of spatial correlations, in a way that could be accounted for by the parameter $\alpha$. The orientation spread remains in any case the most important factor for determining the boundary properties, but the influence of building spatial correlations could become stronger with more heterogeneous microstructures.

### 5.4. Merits and potential of the model

One can see this model as a first step towards the combined prediction of recrystallization kinetics and texture in deformed polycrystals. In conventional mean-field models, recrystallization is driven by the macroscopic stored energy while effects from heterogeneities of crystallographic nature are usually ignored. Here, orientations play an important role on the microstructure evolution and can be output at any time of the simulation. In order to extend the model to the prediction of recrystallization in polycrystals, an additional scheme is required to account for the competitive growth between recrystallized grains coming from different parent deformed grains. A first order approach would be to consider the microstructure as a composite of several sub-regions evolving independently, as implemented in previous models for simulating recrystallization of heterogeneous materials [50,51].

The principal merit of the mean-field model compared to full-field equivalents is its computational speed (few seconds vs. several hours on a laptop for the simulations presented in this paper). This must not be neglected as the number of subgrains that one needs to simulate to obtain one recrystallized grains is very large ( $\sim 10^{3}$ to 1 in Fig. 4a). It is unlikely that full-field models will perform accurately for microstructures that better replicate the experimental measurement, i.e. having a higher degree of heterogeneity that in the present work.

As a concluding remark, we emphasize that the mean-field model has been constructed with the aim to make it applicable to experimental cases. Orientations spreads [30,31,38,52], subgrain sizes [30,53] and initial spatial correlations [48,49] can all be measured using EBSD for example. These parameters can also be estimated from crystal-plasticity simulations [19-21]. Future implementations could also introduce effects from microstructural heterogeneities, like shear bands, transition bands and deformed grain boundaries, following approaches adopted elsewhere [31,43].

## 6. Conclusion

A mean-field model was developed to simulate the time evolution of microstructures during static recrystallization. This model essentially simulates the growth of a population of subgrains contained in well recovered deformed grains, and identifies subgrains above a size threshold as recrystallized grains. At each time increment, the subgrain growth rates are calculated from classical cellular growth laws. The mean subgrain boundary energy and mobility are estimated statistically from knowledge of the orientation spread and of potential spatial correlations between orientation. The orientation spreads considered in this paper are not

far from experimental measurements. The model input can be obtained from experimental or synthetic microstructures.

The mean-field model presented here allows one to predict at the same time the recrystallization kinetics and recrystallized grain orientations. The results highlight the significant contribution of the orientation spread and its time-evolution to the determination of boundary properties, the progress of recrystallization and the selection of recrystallized grain orientations. Future work is underway to compare the mean-field model predictions to experimental data.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

The authors express their thanks to Jean-Denis Mithieux and Francis Chassagne for numerous and fruitful discussions on the topic of recrystallization. © Her Majesty the Queen in Right of Canada, as represented by the Minister of Natural Resources, 2020.

## Appendix A. Growth equations for 3 dimensional microstructures

The growth rate of a 3 dimensional cell embedded in a cellular structure of uniform boundary energy and mobility is given by the MacPherson-Srolovitz equation [54]:

$$
\frac{d V}{d t}=-2 \pi M \Gamma\left(\mathcal{L}-\frac{1}{6} \mathcal{M}\right) \tag{A.1}
$$

Where $V$ is the cell volume, $M$ and $\Gamma$ are its boundary mobility and energy, $\mathcal{L}$ is so called mean width of the cell, and $\mathcal{M}=\sum_{i=1}^{\eta_{l}} l_{i}$ is the sum of the cell edge length, running over the $\eta_{l}$ edges. For simplicity, we omit subscripts associated with time or cell index. This equation assumes that the turning angles at the cell edges are all at equilibrium and equal to $\pi / 3$, as in the 2 dimensional case.

To account for heterogeneous boundary properties, the second right term in parenthesis in Eq. A.1 can be replaced by $1 /(2 \pi) \sum_{i=1}^{\eta_{l}} \xi l_{i}$, with $\xi$ the equilibrium turning angle measured at the cell edges (see [54,55]). In a mean-field environment, $\xi$ is the same for all cell edges, and the growth rate is given by:

$$
\frac{d V}{d t}=-2 \pi M \Gamma\left(\mathcal{L}-\frac{\xi}{2 \pi} \mathcal{M}\right) \tag{A.2}
$$

When all boundaries have equal energy, $\xi=\pi / 3$, and Eq. A.2 reduces to Eq. A.1.

The mean width $\mathcal{L}$ can be calculated from formulas given in Ref. [54]. It takes a value of $4 R$ for a sphere. It is possible to show that it is strictly above $4 R$ for polyhedrons at constant volume, with $R$ the volume equivalent radius. Zhang et al. [56] found on a 3D microstructure obtained by diffraction contrast tomography that the grain mean width follows on average:

$$
\mathcal{L} \approx 5 R \tag{A.3}
$$

Drawing analogies between the MacPherson-Srolovitz equation and the Hillert equation, they suggested the sum of edges lengths to follow a quadratic relation with the volume equivalent radius. After rearranging the relation proposed in the original publication to make it dependent on the cell radius [56]:

$$
\mathcal{M} \approx 6\left(3 R+\frac{16 R^{2}}{9 \bar{R}}\right) \tag{A.4}
$$

The work of Glicksman et al. [57], showing for some solids that $\xi \mathcal{M}$ varies roughly linearly with $\xi$, suggests by induction that $\mathcal{M}$ can be considered independent of $\xi$. Finally, inserting Eq. A.3 and Eq. A.4 in Eq. A.2, and expressing growth rate in terms of the cell radius, one obtains:

$$
\frac{d R}{d t}=\frac{M \Gamma}{2 R}\left(a\left(3+\frac{16 R}{9 \bar{R}}\right)-5\right) \tag{A.5}
$$

Which is the same form as Eq. (4) used for 2 dimensional microstructures. When boundary energy is uniform, $a=1$ and Eq. A.5 reduces to the classical Hillert equation for 3 dimensional microstructures [35].

## Appendix B. Generalized Laguerre function

A review of the generalized Laguerre polynomials and functions has been written by Mirevski and Boyadjiev [58]. Laguerre functions are solutions of the Laguerre differential equation with fractional coefficients. First, the binomial coefficient with real arguments $\alpha$ and $\beta$ is defined as [58]:

$$
\left(\begin{array}{l}
\alpha \\
\beta
\end{array}\right)=\frac{\Gamma(1+\alpha)}{\Gamma(1+\beta) \Gamma(1+\alpha-\beta)} \tag{B.1}
$$

Where $\Gamma$ is, for this particular equation, the gamma function. Laguerre functions are expressed by the series expansion [58]:

$$
L_{v}^{(\alpha)}(x)=\left(\begin{array}{c}
v+\alpha \\
v
\end{array}\right) \sum_{k=0}^{\infty} \frac{(-v)(-v+1) \ldots(-v+k-1)}{(\alpha+1)(\alpha+2) \ldots(\alpha+k)} \frac{(-x)^{k}}{k!} \tag{B.2}
$$

For $v=1 / 2$ and $\alpha=1 / 2$, the right term is reduced to:

$$
L_{1 / 2}^{(1 / 2)}(x)=\left(\begin{array}{c}
1 \\
1 / 2
\end{array}\right) \sum_{k=0}^{\infty} \frac{1}{1-4 k^{2}} \frac{(-x)^{k}}{k!} \tag{B.3}
$$

In the simulations conducted for this work, the parameter $\kappa$ taken as argument of the Laguerre function remained between 0 and 6. Fig. B.11 shows that the series has converged in the interval [0 6] for $k$ interrupted around 50. Other ways to calculate the function are to use the built in Laguerre functions existing in standard programming languages, or to use an abacus made from one of the two previous options.

![](./images/812578757805080577_16.jpg)

Fig. B.11. Evolution of $L_{1 / 2}^{(1 / 2)}(-\kappa^{2} / 2)$ as a function of $\kappa$. The series expansion is compared to the Matlab built-in function.

## Appendix C. Second derivatives of the energy and mobility laws

The second derivative of the Huang-Humphreys law (Eq. (2)) is expressed by:
$$
\mu^{\prime \prime}(\theta)=\frac{\mu_{c} B \eta}{\theta_{c}^{2 \eta}} e^{-B\left(\theta / \theta_{c}\right)^{\eta}}\left(-B \eta \theta^{2 \eta-2}+\theta_{c}^{\eta}(\eta-1) \theta^{\eta-2}\right) \tag{C.1}
$$

The second derivative of the Read-Shockley equation (Eq. (1)) is discontinuous at $\theta=\theta_{c}$. It was choosen to express it as:
$$
\gamma^{\prime \prime}(\theta)= \begin{cases}-\frac{\gamma_{c}}{\theta_{c}^{2} \theta} & \text { if } \theta \leq \theta_{c} \\ 0 & \text { if } \theta>\theta_{c}\end{cases} \tag{C.2}
$$

The effect of this discontinuity on the calculation of boundary energy is negligible since $\gamma^{\prime \prime}(\theta)$ already converges towards 0 in its first section.

## References

[1] J.E. Bailey, Electron microscope observations on the annealing processes occur- ring in cold-worked silver, Philos. Mag. 5 (56) (1960) 833-842, doi:10.1080/14786436008241221.

[2] J.E. Bailey, P.B. Hirsch, The recrystallization process in some polycrystalline metals, Proc. R. Soc. Lond. A: Math. Phys. Eng. Sci. 267 (1328) (1962) 11-30, doi:10.1098/rspa.1962.0080.

[3] D. Weygand, Y. Brechett, J. Lépinoux, On the nucleation of recrystallization by a bulging mechanism: a two-dimensional vertex simulation, Philos. Mag. Part B 80 (11) (2000) 1987-1996, doi:10.1080/13642810008216521.

[4] E.A. Holm, M.A. Miodownik, A.D. Rollett, On abnormal subgrain growth and the origin of recrystallization nuclei, Acta Mater. 51 (9) (2003) 2701-2716, doi:10.1016/S1359-6454(03)00079-X.

[5] P.J. Hurley, F.J. Humphreys, Modelling the recrystallization of single-phase alu-minium, Acta Mater. 51 (13) (2003) 3779-3793, doi:10.1016/S1359-6454(03)00192-7.

[6] H.S. Zurob, Y. Bréchet, J. Dunlop, Quantitative criterion for recrystallization nu- cleation in single-phase alloys: prediction of critical strains and incubation times, Acta Mater. 54 (15) (2006) 3983-3990, doi:10.1016/j.actamat.2006.04.028.

[7] S. Wang, E.A. Holm, J. Suni, M.H. Alvi, P.N. Kalu, A.D. Rollett, Modeling the recrystallized grain size in single phase materials, Acta Mater. 59 (10) (2011) 3872-3882, doi:10.1016/j.actamat.2011.03.011.

[8] J. Favre, D. Fabrègue, A. Chiba, Y. Bréchet, Nucleation of recrystallization in fine-grained materials: an extension of the Bailey-Hirsch criterion, Philos. Mag. Lett. 93 (11) (2013) 631-639, doi:10.1080/09500839.2013.833352.

[9] K. Huang, R.E. Logé, A review of dynamic recrystallization phenomena in metallic materials, Mater. Des. 111 (2016) 548-574, doi:10.1016/j.matdes.2016.09.012.

[10] C. Mießen, N. Velinov, G. Gottstein, L.A. Barrales-Mora, A highly efficient 3D level-set grain growth algorithm tailored for ccNUMA architecture, Modell. Simul. Mater. Sci. Eng. 25 (8) (2017) 084002, doi:10.1088/1361-651X/aa8676. Publisher: IOP Publishing

[11] E. Miyoshi, T. Takaki, M. Ohno, Y. Shibuta, S. Sakane, T. Shimokawabe, T. Aoki, Ultra-large-scale phase-field simulation study of ideal grain growth, npj Com- put. Mater. 3 (1) (2017) 1-6, doi:10.1038/s41524-017-0029-8. Number: 1 Pub- lisher: Nature Publishing Group

[12] Y. Suwa, Y. Saito, H. Onodera, Phase-field simulation of recrystallization based on the unified subgrain growth theory, Comput. Mater. Sci 44 (2) (2008) 286-295, doi:10.1016/j.commatsci.2008.03.025.

[13] F.J. Humphreys, A unified theory of recovery, recrystallization and grain growth, based on the stability and growth of cellular microstructures-i. the ba- sic model, Acta Mater. 45 (10) (1997) 4231-4240, doi:10.1016/S1359-6454(97)00070-0.

[14] A. Rollett, On the growth of abnormal grains, Scr. Mater. 36 (9) (1997) 975-980, doi:10.1016/S1359-6462(96)00501-5.

[15] M.A. Razzak, M. Perez, T. Soumail, S. Cazottes, M. Frotey, A simple model for abnormal grain growth, ISIJ Int. 52 (12) (2012) 2278-2282, doi:10.2355/ isijinternational.52.2278.

[16] M. Syha, D. Weygand, Conditions for the occurrence of abnormal grain growth studied by a 3 d vertex dynamics model, 2012. https://www.scientific.net/MSF.715-716.563

[17] J.W.C. Dunlop, Y.J.M. Bréchet, L. Legras, H.S. Zurob, Modelling isothermal and non-isothermal recrystallisation kinetics: application to Zircaloy-4, J. Nucl. Mater. 366 (1) (2007) 178-186, doi:10.1016/j.jnucmat.2006.12.074.

[18] O. Beltran, K. Huang, R.E. Logé, A mean field model of dynamic and post- dynamic recrystallization predicting kinetics, grain size and flow stress, Com- put. Mater. Sci. 102 (2015) 293-303, doi:10.1016/j.commatsci.2015.02.043.

[19] L. Kestens, J.J. Jonas, Modeling texture change during the static recrystallization of interstitial free steels, Metall. Mater. Trans. A 27 (1) (1996) 155-164, doi:10.1007/BF02647756.

[20] H.R. Wenk, G. Canova, Y. Bréchet, L. Flandin, A deformation-based model for recrystallization of anisotropic materials, Acta Mater. 45 (8) (1997) 3283-3296, doi:10.1016/S1359-6454(96)00409-0.

[21] M. Zecevic, R.A. Lebensohn, R.J. McCabe, M. Knezevic, Modelling recrystal- lization textures driven by intragranular fluctuations implemented in the vis- coplastic self-consistent formulation, Acta Mater. 164 (2019) 530-546, doi:10.1016/j.actamat.2018.11.002.

[22] D. Weygand, Y. Bréchet, J. Lépinoux, A vertex dynamics simulation of grain growth in two dimensions, Philos. Mag. Part B 78 (4) (1998) 329-352, doi:10.1080/13642819808206731.

[23] K. Piekos, J. Tarasiuk, K. Wierzbzanowski, B. Bacroix, Generalized vertex model of recrystallization - application to polycrystalline copper, Comput. Mater. Sci. 42 (4) (2008) 584-594, doi:10.1016/j.commatsci.2007.09.014.

[24] Y. Mellbin, H. Hallberg, M. Ristinmaa, A combined crystal plasticity and graph- based vertex model of dynamic recrystallization at large deformations, Mod- ell. Simul. Mater. Sci. Eng. 23 (4) (2015) 045011, doi:10.1088/0965-0393/23/4/045011.

[25] Y. Huang, F.J. Humphreys, Subgrain growth and low angle boundary mobility in aluminium crystals of orientation {110}(001), Acta Mater. 48 (8) (2000) 2017-2030, doi:10.1016/S1359-6454(99)00418-8.

[26] O. Engler, V. Randle, Introduction to Texture Analysis: Macrotexture, Microtex- ture, and Orientation Mapping, 2nd, CRC Press, 2009.

[27] W.T. Read, W. Shockley, Dislocation models of crystal grain boundaries, Phys. Rev. 78 (3) (1950) 275-289, doi:10.1103/PhysRev.78.275.

[28] N.P. Louat, On the theory of normal grain growth, Acta Metall. 22 (6) (1974)721-724, doi:10.1016/0001-6160(74)90081-9.

[29] D.J. Srolovitz, M.P. Anderson, P.S. Sahni, G.S. Grest, Computer simulation of grain growth-II. Grain size distribution, topology, and local dynamics, Acta Metall. 32 (5) (1984) 793-802, doi:10.1016/0001-6160(84)90152-4.

[30] J.C. Glez, J. Driver, Orientation distribution analysis in deformed grains, J. Appl. Cryst. 34 (3) (2001) 280-288, doi:10.1107/S0021889801003077.

[31] W. Pantleon, Retrieving orientation correlations in deformation structures from orientation maps, Mater. Sci. Technol. 21 (12) (2005) 1392-1396, doi:10.1179/147328405X71657.

[32] A. Miodownik Mark, S. Peter, J. Srolovitz David, A. Holm Elizabeth, Scaling of dislocation cell structures: diffusion in orientation space, Proc. R. Soc. Lond. Series A: Math. Phys. Eng. Sci. 457 (2012) (2001) 1807-1819, doi:10.1098/rspa.2001.0794.

[33] W. Pantleon, N. Hansen, Dislocation boundaries-the distribution function of disorientation angles, Acta Mater. 49 (8) (2001) 1479-1493, doi:10.1016/ S1359-6454(01)00027-1.

[34] D.A. Hughes, D.C. Chrzan, Q. Liu, N. Hansen, Scaling of misorientation an-gle distributions, Phys. Rev. Lett. 81 (21) (1998) 4664-4667, doi:10.1103/PhysRevLett.81.4664.

[35] M. Hillert, On the theory of normal and abnormal grain growth, Acta Metall.13 (3) (1965) 227-238, doi:10.1016/0001-6160(65)90200-2.

[36] G. Abbruzzese, K. Lücke, A theory of texture controlled grain growth-i. deriva- tion and general discussion of the model, Acta Metall. 34 (5) (1986) 905-914, doi:10.1016/0001-6160(86)90064-7.

[37] J.H. Park, Moments of the generalized rayleigh distribution, Q. Top Q. Appl. Math. 19 (1) (1961) 45-49, doi:10.1090/qam/119222.

[38] S. Krog-Pedersen, J.R. Bowen, W. Pantleon, Quantitative characterization of the orientation spread within individual grains in copper after tensile deformation, Int. J. Mater. Res. 100 (3) (2009) 433-438, doi:10.3139/146.110032.

[39] A. Després, M. Zecevic, R.A. Lebensohn, J.D. Mithieux, F. Chassagne, C.W. Sin- clair, Contribution of intragranular misorientations to the cold rolling tex- tures of ferritic stainless steels, Acta Mater. 182 (2020) 184-196, doi:10.1016/j.actamat.2019.10.023.

[40] P.J. Hurley, F.J. Humphreys, The application of EBSD to the study of substruc- tural development in a cold rolled single-phase aluminium alloy, Acta Mater.51 (4) (2003) 1087-1102, doi:10.1016/S1359-6454(02)00513-X.

[41] E.C.W. Perryman, Recrystallization characteristics of superpurity base Al-mg al- loys containing 0 to 5 pct mg, Trans. AIME (1955) 369-378.

[42] O.V. Mishin, A. Godfrey, D. Juul Jensen, N. Hansen, Recovery and recrystalliza- tion in commercial purity aluminum cold rolled to an ultrahigh strain, Acta Mater. 61 (14) (2013) 5354-5364, doi:10.1016/j.actamat.2013.05.024.

[43] F. Lefevre-Schlick, Y. Brechet, H.S. Zurob, G. Purdy, D. Embury, On the activation of recrystallization nucleation sites in Cu and Fe, Mater. Sci. Eng.: A 502 (1) (2009) 70-78, doi:10.1016/j.msea.2008.10.015.

[44] O. Engler, On the influence of orientation pinning on growth selection of recrystallisation, Acta Mater. 46 (5) (1998) 1555-1568, doi:10.1016/ S1359-6454(97)00354-6.

[45] D.J. Jensen, K. Mehnert, Orientation pinning during growth, in: Grain Growth in Polycrystalline Materials 3, Minerals, Metals and Materials Society, 1998, pp. 251-262.

[46] R.D. Doherty, D.A. Hughes, F.J. Humphreys, J.J. Jonas, D. Juul Jensen, M.E. Kass- ner, W.E. King, T.R. McNellely, H.W. McQueen, A.D. Rollett, Current issues in re- crystallization: a review, Mater. Sci. Eng.: A 238 (2) (1997) 219-274, doi:10.1016/S0921-5093(97)00424-3.

[47] Y. Bréchet, G. Martin, Nucleation problems in metallurgy of the solid state: recent developments and open questions, Comptes Rendus de Physique 7 (9-10) (2006) 959-976, doi:10.1016/j.crhy.2006.10.014.

[48] W. Pantleon, D. Stoyan, Correlations between disorientations in neighbouring dislocation boundaries, Acta Mater. 48 (11) (2000) 3005-3014, doi:10.1016/ S1359-6454(00)00083-5.

[49] A. Borbély, C. Maurice, D. Piot, J.H. Driver, Spatial characterisation of the ori- entation distributions in a stable plane strain-compressed cu crystal: a statis- tical analysis, Acta Mater. 55 (2) (2007) 487-496, doi:10.1016/j.actamat.2006.08.043.

[50] A. Rollett, D. Srolovitz, R. Doherty, M. Anderson, Computer simulation of re- crystallization in non-uniformly deformed metals, Acta Metall. 37 (2) (1989) 627-639, doi:10.1016/0001-6160(89)90247-2.

[51] M. Kühbach, G. Gottstein, L.A. Barrales-Mora, A statistical ensemble cellular automaton microstructure model for primary recrystallization, Acta Mater. 107 (2016) 366-376, doi:10.1016/j.actamat.2016.01.068.

[52] F. Bachmann, R. Hielscher, P.E. Jupp, W. Pantleon, H. Schaeben, E. Wegert, In- ferential statistics of electron backscatter diffraction data from within indi-vidual crystalline grains, J. Appl. Cryst. 43 (6) (2010) 1338-1355, doi:10.1107/ S002188981003027X.

[53] F.J. Humphreys, Review grain and subgrain characterisation by electron backscatter diffraction, J. Mater. Sci. 36 (16) (2001) 3833-3854, doi:10.1023/A:1017973432592.

[54] R.D. MacPherson, D.J. Srolovitz, The von Neumann relation generalized to coarsening of three-dimensional microstructures, Nature 446 (7139) (2007) 1053-1055, doi:10.1038/nature05745.

[55] T. Le, Q. Du, A generalization of the three-dimensional Macpherson-Srolovitz formula, Commun. Math. Sci. 7 (2) (2009) 511-520.

[56] J. Zhang, Y. Zhang, W. Ludwig, D. Rowenhorst, P.W. Voorhees, H.F. Poulsen, Three-dimensional grain growth in pure iron. part i. statistics on the grain level, Acta Mater. 156 (2018) 76-85, doi:10.1016/j.actamat.2018.06.021.

[57] M.E. Glicksman, P.R. Rios, D.J. Lewis, Mean width and caliper characteris- tics of network polyhedra, Philos. Mag. 89 (4) (2009) 389-403, doi:10.1080/14786430802651513.

[58] S.P. Mirevski, L. Boyadjiev, On some fractional generalizations of the Laguerre polynomials and the Kummer function, Comput. Math. Appl. 59 (3) (2010) 1271-1277, doi:10.1016/j.camwa.2009.06.037.