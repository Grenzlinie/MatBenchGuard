Author's Accepted Manuscript

![](./images/813022894006206464_1.jpg)

www.elsevier.com/locate/ceri

The modified Mori-Tanaka scheme for the prediction of the effective elastic properties of highly porous ceramics

S. Misagh Imani, A.M. Goudarzi, Sayed Mahmood Rabiee, Morteza Dardel

PII:
S0272-8842(18)31494-9
DOI:
https://doi.org/10.1016/j.ceramint.2018.06.066
Reference:
CERI18510

To appear in: Ceramics International

Received date: 23 May 2018
Revised date: 8 June 2018
Accepted date: 9 June 2018

Cite this article as: S. Misagh Imani, A.M. Goudarzi, Sayed Mahmood Rabiee and Morteza Dardel, The modified Mori-Tanaka scheme for the prediction of the effective elastic properties of highly porous ceramics, Ceramics International, https://doi.org/10.1016/j.ceramint.2018.06.066

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting galley proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# The modified Mori-Tanaka scheme for the prediction of the effective elastic properties of highly porous ceramics

S. Misagh Imani¹, A.M. Goudarzi¹,*, Sayed Mahmood Rabiee², Morteza Dardel¹

¹ Department of Mechanical Engineering, Babol University of Technology, Babol, Iran
² Department of Materials and Industries Engineering, Babol University of Technology, Babol, Iran

* Corresponding author Email: moazemi.goudarzi@gmail.com

## Abstract

In this paper, two modifications are proposed to be applied to the well-known Mori-Tanaka (MT) scheme to improve its performance in the estimation of the mechanical properties of highly porous ceramic structures containing complicated agglomerates of merged and open-cell spherical pores of different radii. In the first modification, the effect of the merged pores is considered by estimating their number with the theory of geometrical probabilities and treating them as corresponding ellipsoids of the same volume. In the second modification, porous structures containing open pores are treated as a damaged material with reduced load-carrying capacity and the formulations are modified to consider the effect of the open pores. In order to investigate the reliability of the analytical estimations, different groups of artificial porous structures with porosity values ranging from 10% to 90% are constructed by random positioning of the spherical voids of different radii in a representative volume element (RVE) and their effective elastic properties are obtained by means of the finite element method (FEM). For each level of porosity, a total of 30 random structures are examined to assess the variations caused by the statistical nature of the microstructure. Comparison between the findings of the statistical FEM and the analytical results show that the proposed modifications considerably increase the precision of the MT scheme in the estimation of the effective elastic moduli of highly porous materials. Furthermore, unlike the classical MT method, the modified formulations are capable of demonstrating of the probable anisotropy in the effective elastic properties of the porous structures. Good agreement is also observed between the results obtained from the developed formulations and published numerical and experimental observations for ceramic structures.

**Keywords:**
porous ceramics; effective elastic moduli; Mori-Tanaka scheme; the theory of geometrical probabilities; statistical finite element method

### 1. Introduction
Porous ceramics are extensively used in industrial and engineering applications, due to their special properties such as relatively low mass, high specific surface area, low fractional density, resistance to chemical attack, low thermal conductivity, high permeability and resistance to high temperature and thermal cycling [1]. In order to use the full potential of these structures, their mechanical behavior has to be entirely characterized. One of the most well-known approaches to obtain the mechanical properties of the porous structures is the Mori-Tanaka scheme. This method is originally suggested for composite materials but it can also be used to calculate the properties of porous structures, by assigning zero value to the stiffness tensor of one phase (i.e. pore phase) [2].

The application of the MT scheme in the evaluation of the mechanical behavior of porous materials has been reported in numerous studies. Suvorov and Selvadurai [3] estimated the elastic constants of porous materials with randomly-distributed voids of ellipsoidal shape using different methods (including the MT, the differential, the self-consistent and the Kachanov’s schemes). Gong *et al.* [4] extended the MT method to obtain the stiffness tensor of the porous materials containing various kinds of pores with different shapes. They also studied the influence of specimen size by means of a semi-infinite domain mechanics model. Martinez-Ayuso *et al.* [5] used different analytical approaches (including the MT and the self-consistent schemes as well as the Halpin-Tsai and the Hashin-Sthrikman bounds) to calculate the effective elastic moduli of a porous piezoelectric structure. Poh *et al.* [6] used this approach to obtain the properties of a porous composite of carbon nanotube reinforcements embedded in a ceramic matrix. Using the MT scheme, Aguiar *et al.* [7] evaluated the effective properties of porous piezoelectric materials. They also used the proposed method in the evaluation of the effective electroelastic properties of heterogeneous solids with hierarchical structures, such as bones. Phani and Sanyal [8] derived a relation between the shear modulus and Young’s modulus of isotropic porous ceramics based on the MT approach. Soro *et al.* [9] obtained the effective elastic moduli of porous titanium implants at different porosity levels by means of the numerical and experimental methods and validated the findings by the MT scheme. Similar to the aforementioned studies, several works can be found in the literature in which the MT method was used to obtain the mechanical properties of different porous structures [10-14].

The threshold value of the porosity for the applicability of the MT scheme is about 40% [15-17]. Indeed, in the MT formulation, the inclusion phase (i.e. pores) is assumed as a single inclusion embedded in an infinite matrix and subjected to the matrix average strain as far-field strain [18]. It means that the MT scheme does not consider the overlapping of the pores and is only valid for the case of dilute concentration in which the interactions between the pores are neglected and all of the pores are isolated [9,15,19]. By increasing the porosity from this threshold value, because of the percolation of the pores, the precision of the MT method decreases dramatically. However, highly porous structures with interconnected pore network are extensively found in the different applications, such as bone scaffolds [20-28]. Hence, a modification is needed to be applied to the MT scheme to increase its precision in the estimation of the effective elastic moduli of the structures which contain overlapped pores.

The comprehensive investigation of the microstructure of the porous materials reveals that in many of these structures the shape of the pores could be estimated as a single sphere and/or a combination of two (i.e. merged pores) or multiple (i.e. open-cell pores) spheres, as schematically shown in Fig. 1. In this paper, two modifications are proposed to be applied to the MT scheme to treat with the merged and/or open-cell pores existed in the structure. In order to increase the precision of the MT theory for the estimation of the effective elastic moduli of porous materials containing overlapped pores, this method is suggested to be applied differentially. In the proposed differential approach, the number of the merged pores existed in the porous structure is initially estimated by means of the theory of geometrical probabilities and the overlapped pores are then treated as corresponding ellipsoids of the same volume. Moreover, by assuming no load-carrying capacity for the open pores, the formulations are modified to consider the influence of these pores on the effective elastic moduli of the porous structures. Utilizing these modifications will significantly improve the performance of the MT theory in the estimation of the elastic constants of porous materials containing merged and open-cell pores.

For better illustration of the reliability of the proposed modifications, different groups of artificial porous structures with porosity values ranging from 10% to 90% are constructed by random positioning of the spherical voids of different radii in a RVE and their effective elastic properties are obtained by means of the finite element method. Moreover, the effective elastic properties of some porous ceramic structures found in the literature are also used in the current study to show the application of the proposed method in the calculation of the effective properties of the porous ceramics.

To our knowledge, it is for the first time that these modifications are applied to the MT method to improve its performance in the calculation of the effective elastic moduli of highly porous materials. In section two, the

basic formulation of the MT scheme is initially presented and then it is reformulated for porous structures. The above-mentioned modifications as well as the FEM models are also introduced in this section. In the third section, the reliability of the proposed modifications is assessed. In this section, the results obtained from the developed relations are compared with the findings of the numerical simulations. Furthermore, the proposed formulations are used to predict the effective elastic properties of some porous ceramics found in the published papers. The last section of the paper is assigned to the major findings of the present study and the conclusion.

## 2. Formulation

### 2.1. The Mori-Tanaka scheme

Consider a composite material consisting of $n$ phases. According to the MT approach, the effective stiffness tensor $(\mathbf{C}^{c})$ of this material is given as follows [29]:

$$
\mathbf{C}^{c}=\sum_{i=1}^{n} f_{i} \mathbf{C}^{i}: \mathbf{A}^{i} \tag{1}
$$

where $f_{i}$ and $\mathbf{C}^{i}$ denote the volume fraction and the stiffness tensor of phase $i$, respectively, and $\mathbf{A}^{i}$ is the fourth-order strain concentration tensor of phase $i$ which is defined as:

$$
\mathbf{A}^{i}=\mathbf{L}^{i}:\left\{\sum_{i=1}^{n} f_{i} \mathbf{L}^{i}\right\}^{-1} \tag{2}
$$

with:

$$
\mathbf{L}^{i}=\left\{\mathbf{I}+\mathbf{S}^{i}:\left(\mathbf{C}^{m}\right)^{-1}:\left(\mathbf{C}^{i}-\mathbf{C}^{m}\right)\right\}^{-1}, \quad i=1,..., n \tag{3}
$$

where $\mathbf{I}$ is the fourth-order identity tensor, $\mathbf{C}^{m}$ is the stiffness tensor of the matrix phase, and $\mathbf{S}^{i}$ represents the fourth-order Eshelby's tensor of phase $i$. The components of the Eshelby's tensor for elliptical and spherical inclusions embedded in an anisotropic matrix are given in ref. [30].

If inclusions of phase $j$ have different orientations in space, orientation averaging must be used to consider the effect of inclusions alignment on the effective elastic properties of composites. In this situation, $\langle\mathbf{L}^{j}\rangle$ is used instead of $\mathbf{L}^{j}$ in Eq. (2), where angle brackets $\langle\circ\rangle$ show an average over all orientations and we have [31]:

$$
\left\langle\mathbf{L}^{j}\right\rangle=\frac{1}{8 \pi^{2}} \int_{0}^{2 \pi} \int_{0}^{2 \pi} \int_{0}^{\pi} \mathbf{L}^{j}(\theta, \varphi, \psi) \times \sin \theta d \theta d \varphi d \psi \tag{4}
$$

and the components of the fourth-order tensor $\mathbf{L}^{j}$ in the local coordinate system $(L_{mnrs}^{j})$ are transformed to the global coordinate system $(L_{ijkl}^{j})$ by:

$$L_{i j k l}^{j}=Q_{i m} Q_{j n} Q_{k r} Q_{l s} L_{m n r s}^{j}\tag{5}$$

where $\mathbf{Q}$ is defined in terms of the Euler angles, $(\theta, \varphi, \psi)$, as follow:

$$
\mathbf{Q}=\left[\begin{array}{ccc}
(\cos \theta \cos \varphi \cos \psi-\sin \varphi \sin \psi) & (-\cos \theta \cos \varphi \sin \psi-\sin \varphi \cos \psi) & \sin \theta \cos \varphi \\
(\cos \theta \sin \varphi \cos \psi+\cos \varphi \sin \psi) & (-\cos \theta \sin \varphi \sin \psi+\cos \varphi \cos \psi) & \sin \theta \sin \varphi \\
-\sin \theta \cos \psi & \sin \theta \sin \psi & \cos \theta
\end{array}\right]\tag{6}
$$

For the case of porous materials, the structure is considered as a two-phase composite consisting of one solid phase (host material) with the stiffness tensor of $\mathbf{C}^{s}$ and one pore phase with zero stiffness which occupying the remaining space. Hence, we have:

$$f_{1}=\phi\tag{7}$$

$$f_{2}=1-\phi\tag{8}$$

$$\mathbf{C}^{1}=\mathbf{0}\tag{9}$$

$$\mathbf{C}^{2}=\mathbf{C}^{s}\tag{10}$$

whereby $\phi$ denotes the porosity of the porous material which represents the volume fraction of pores per unit volume of the host material. After some simplifications, the MT relation, Eq. (1), for this structure can be expressed in the following form:

$$\mathbf{C}^{p}=(1-\phi) \mathbf{C}^{s}\left(\phi \mathbf{L}^{\phi}+(1-\phi) \mathbf{I}\right)^{-1}\tag{11}$$

where $\mathbf{C}^{p}$ is the stiffness tensor of the porous structure and:

$$\mathbf{L}^{\phi}=\left(\mathbf{I}-\mathbf{S}^{\phi}\right)^{-1}\tag{12}$$

and the fourth-order Eshelby tensor $\mathbf{S}^{\phi}$ depends on the host material elastic constants and pores shape. Equation (11) is the simplified version of the MT formulation which can be used to obtain the effective elastic properties of the porous structures.

### 2.2. The modification of the Mori-Tanaka scheme to consider the effect of the merged and open-cell spherical pores of different radii

The modifications are applied in four different steps. In the first step, the formulation of the MT scheme is expressed in a way that the radius and the number of the pores are appeared in the relations. In the second step, the number of the isolated and merged pores existed in the porous structure is approximated through the use of the theory of geometrical probabilities. In the third step, the MT scheme is applied in a stepwise manner to

consider the effect of merged pores. Finally, in the fourth step, the relations are modified to consider the effect of open-cell pores.

### 2.2.1. First step: New expression for the Mori-Tanaka relation

The new expression of the MT scheme is first obtained for the case spherical pores of the same radius and then extended for the structures containing pores of different radii. By assuming the equal value $r$ for the radius of the pores existed in the structure and dilute concentration condition, the porosity $\phi$ in Eq. (11) can be expressed as:

$$
\phi=N \frac{4}{3} \pi r^{3} \tag{13}
$$

where $N$ is the total number of the pores existed in the porous structure. Substituting Eq. (13) into Eq. (11) yields:

$$
\mathbf{C}^{p}=\left(1-\frac{4}{3} \pi \Gamma\right) \mathbf{C}^{s}\left(\frac{4}{3} \pi \Gamma \mathbf{L}^{\phi}+\left(1-\frac{4}{3} \pi \Gamma\right) \mathbf{I}\right)^{-1} \tag{14}
$$

where $\Gamma$ is the concentration parameter and it is defined as:

$$
\Gamma=N r^{3} \tag{15}
$$

Equation (14) is a new form of the MT formulation for the porous structures with spherical pores of the same radius in which the radius and the number of the pores are appeared in the relation.

Now, a porous structure consisting of spherical pores of $n$ various radii is considered. The pores are assumed to be arranged in increasing order as follow:

$$
r_{i+1}>r_{i}, \quad \forall i=1, \ldots, n, \quad r_{1}=r_{\text {min }}, \quad r_{n}=r_{\text {max }} \tag{16}
$$

For this porous structure, distributions of pores by size can be defined by a relative frequency function. The relative frequency of pores of radius $r_{i}$ is defined as:

$$
p_{i}=\frac{N_{i}}{N}, \quad i=1, \ldots, n \tag{17}
$$

where $N_{i}$ is the number of the pores of radius $r_{i}$ existed in the porous structure. After some manipulations, the total number of the existed pores, i.e. $N$, can be expressed as:

$$
N=\sum_{i=1}^{n} N_{i}=\frac{3 \phi}{4 \pi \sum_{i=1}^{n} p_{i} r_{i}^{3}} \tag{18}
$$

In order to obtain the elastic constants of this porous structure, pores of different radii are added differentially to the host material, and Eq. (14) is used at each step to calculate the effective elastic properties of

the medium where only holes with smaller sizes are present. It should be noted that in the differential application of the MT relation, the corresponding porosity relating to each pore radius must be clarified. Indeed, when the pores of radius $r_i$ are added to the host material, only the pores with smaller size $(r < r_i)$ exist in the porous structure. In this situation the value of the porosity should be determined according to the present porous medium which contains only the pores with radius less than or equal to $r_i$. Hence, instead of the conventional porosity $\phi$, instantaneous porosity $\phi_i'$ is used for this case which is defined as follow [32]:

$$
\phi_{i}{ }^{\prime}=\frac{V_{i}}{V_{0}+V_{1}+V_{2}+\cdots+V_{i}}=\frac{V_{i}}{1-\sum_{j>i} V_{j}}=\frac{\frac{4}{3} \pi N_{i} r_{i}^{3}}{1-\frac{4}{3} \pi \sum_{j>i} N_{j} r_{j}^{3}}, \quad i=1,..., n
\tag{19}
$$

where $V_i$ ($i=1,...,n$) denotes the volume occupied by the pores of radius $r_i$, and $V_0$ is the volume of the host material. The instantaneous porosity $\phi_i'$ shows the volume fraction of the pores of radius $r_i$ per unit volume of the current porous material. Consequently, the concentration parameter is given by:

$$
\Gamma_{i}=\frac{N_{i} r_{i}^{3}}{1-\frac{4}{3} \pi \sum_{j>i} N_{j} r_{j}^{3}}, \quad i=1,..., n
\tag{20}
$$

The stepping form of the MT method is now expressed as follow:

$$
\mathbf{C}_{i}^{p}=\left(1-\frac{4}{3} \pi \Gamma_{i}\right) \mathbf{C}_{i-1}^{p}\left(\frac{4}{3} \pi \Gamma_{i} \mathbf{L}_{i}^{\phi}+\left(1-\frac{4}{3} \pi \Gamma_{i}\right) \mathbf{I}\right)^{-1}, \quad i=1,..., n
\tag{21}
$$

and:

$$
\mathbf{C}_{0}^{p}=\mathbf{C}^{s}
\tag{22}
$$

with $\mathbf{L}_{i}^{\phi}$ is given by:

$$
\mathbf{L}_{i}^{\phi}=\left(\mathbf{I}-\mathbf{S}_{i}^{\phi}\right)^{-1}
\tag{23}
$$

where $\mathbf{S}_{i}^{\phi}$ depends on $\mathbf{C}_{i-1}^{p}$ and the shape of the pores at step $i$.

Consider a porous structure consisting of isolated spherical pores of $n$ various radii. To obtain the equivalent stiffness tensor of this structure, initially, the pores with the smallest radius, i.e. $r_1 = r_{min}$, are added to the host material with stiffness tensor of $\mathbf{C}^s$. Adding these pores to the host material leads to a reduction in its effective elastic moduli, and the corresponding stiffness tensor of the resulting porous structure $\mathbf{C}_{1}^{p}$ can be obtained by Eq. (21). The current porous structure with stiffness tensor of $\mathbf{C}_{1}^{p}$ is now considered as a new host material and the second group of the pores with the radius of $r_2$ is added to it. Again, Eq. (21) is used to compute the corresponding stiffness tensor of the resulting porous structure, i.e. $\mathbf{C}_{2}^{p}$. This procedure will be repeated for all of

the pores until the stiffness tensor of the whole porous structure $\mathbf{C}_{n}^{p}$ is obtained. The proposed modeling procedure is schematically shown in Fig. 2.

#### 2.2.2. Second step: Calculation of the number of the isolated and merged pores existed in the porous structure

In order to consider the effect of the merged pores, first of all the isolated pores should be separated from the overlapped ones. For this purpose, the number of the merged pores should be initially approximated which is accomplished by means of the theory of geometrical probabilities. Two spherical pores with different radius $r_{i}$ and $r_{j}$ ($r_{i} \leq r_{j}$) are considered here. These two pores will overlap with each other if the distance between their centers lies between $r_{i}$ and $r_{i}+r_{j}$. The probability of this happening is [33]:

$$
\operatorname{Pr}[r_{i}<\delta<r_{i}+r_{j}]=\int_{r_{i}}^{r_{i+r_{j}}} f(\delta) d \delta \tag{24}
$$

where $\delta$ is the distance between the centers of the spherical pores and $f(\delta)$ is the probability density function (PDF) of $\delta$. The PDF of distance $\delta$ between two points which are placed randomly inside the volume $V$ is given by [34]:

$$
f(\delta)=\frac{4 \pi \delta^{2}}{V} \tag{25}
$$

By substituting Eq. (25) into Eq. (24), the probability that these pores overlap with each other is obtained as:

$$
\operatorname{Pr}[r_{i}<\delta<r_{i}+r_{j}]=\frac{4 \pi\left(\left(r_{i}+r_{j}\right)^{3}-r_{i}^{3}\right)}{3 V} \tag{26}
$$

The number $N_{i j}^{merged}$ of pores of radius $r_{j}$ which may overlap a spherical pore of radius $r_{i}$ is given by [34]:

$$
N_{i j}^{merged}=\operatorname{Pr}[r_{i}<\delta<r_{i}+r_{j}] × N_{i} × N_{i j}=\frac{4 \pi\left(\left(r_{i}+r_{j}\right)^{3}-r_{i}^{3}\right)}{3 V} × N_{i} × N_{i j} \tag{27}
$$

where $N_{i j}$ is the amount of pairs of pores of different radius $r_{i}$ and $r_{j}$ and it is given as follow:

$$
N_{i j}= \begin{cases}\frac{N_{i}}{2} & i=j \\ min (N_{i}, N_{j}) & i \neq j\end{cases} \tag{28}
$$

It should be mentioned that for the case of a porous structure containing merged spherical pores of the same radius $r$, the probability relation (24) is defined as [33]:

$$
\operatorname{Pr}[\delta<r]=\int_{0}^{r} f(\delta) d \delta=\frac{4 \pi r^{3}}{3 V} \tag{29}
$$

and the number $N^{merged}$ of pores of radius $r$ which may overlap with each other is given by:

$$
N^{merged} = Pr[\delta < r] \times \frac{N^2}{2} = \frac{2\pi r^3 N^2}{3V} \tag{30}
$$

### 2.2.3. Third step: Modification of the Mori-Tanaka scheme to consider the effect of merged pores

The main idea of the proposed modification is to add the spherical pores of different radii to the host material in a stepwise manner. In this stepping scheme, the changes of the stiffness tensor caused by adding the isolated pores are calculated by means of Eqs. (21) and (22). For the case of overlapped pores, these pores are initially substituted by corresponding ellipsoids of the same volume and then Eqs. (21) and (22) are used to obtain the resulting stiffness tensor.

Consider a porous structure consisting of $N$ spherical voids of $n$ various radii. To obtain the equivalent stiffness tensor of this structure through the use of the proposed stepping scheme, initially the number of the merged and isolated pores existed in the porous structure should be estimated. To this end, the number of the spherical pores of radius $r_i$ ($i = 1, 2, ..., n$) which may overlap with the pores of radius $r_j$ (i.e. $N_{ij}^{merged}$) is calculated by Eq. (27) for any $r_j \geq r_i$. The number of isolated pores of radius $r_i$ (i.e. $N_i^{isolated}$) is then obtained by subtracting the amount of the spheres involved in the overlapped pairs from the total number of the pores of radius $r_i$ (i.e. $N_i$). The stepping scheme begins by adding the isolated pores of radius $r_1$ ($i = 1$) to the host material with stiffness tensor of $\mathbf{C}^s$. Adding these pores to the host material declines its effective elastic moduli and the corresponding stiffness tensor of the resulting porous structure $\mathbf{C}_{1,0}^p$ can be obtained by Eq. (21). The current porous structure with the stiffness tensor of $\mathbf{C}_{1,0}^p$ is now considered as a new host material. Thereafter, the merged spherical pores of radius $r_1$ and $r_j$ ($j \geq 1$) are added to the present host material step by step. At each step, the overlapped pairs are initially substituted by the corresponding ellipsoids of the same volume and then Eq. (21) is used to compute the corresponding stiffness tensor of the resulting porous structure, i.e. $\mathbf{C}_{1,j}^p$. At the end of this differential procedure, the current porous structure with stiffness tensor of $\mathbf{C}_{1,n}^p$ is considered as a new host material and the second group of the isolated pores with radius of $r_2$ following by the merged spherical pores of radius $r_2$ and $r_j$ ($j \geq 2$) are added to the present host material step by step and Eq. (21) is used at each step to compute the corresponding stiffness tensor of the resulting porous structure. This procedure will be repeated for all of the pores until the stiffness tensor of the porous structure which only contains isolated and merged pores (i.e. $\mathbf{C}_{merged}^p$) is obtained.

### 2.2.4. Fourth step: Modification of the Mori-Tanaka scheme to consider the effect of open-cell pores

The influence of the open-cell pores on the mechanical properties of the porous structure is more significant than that of the merged ones. The presence of the open pores in the structure causes a considerable reduction in a load-carrying capacity of the material. Kusoglu *et al.* [35] developed a micromechanical model to obtain the mechanical properties of the porous membranes. They considered no load-carrying capacity for the porous sections of the structure and proposed a relation to obtain the Young's modulus of the material only by considering its non-porous volume. It can be interpreted from their method that in a structure containing a damaged part with reduced load-carrying capacity, the load is transferred only by the non-damaged part of the structure and the damaged volume can be neglected. By considering the volume occupied by the open-cell pores as a damaged section of the structure, the following relation is proposed here, based on the work done by Kusoglu *et al.* [35], to modify the value of the Young's modulus of the porous materials by taking into account the effect of open-cell pores:

$$
E_{open}=E_{merged}\left(1-\frac{A_{open}}{A_{total}}\right) \tag{31}
$$

where $E_{open}$ is the Young's modulus of the whole porous structure, $E_{merged}$ is the Young's modulus of the porous structure which only contains isolated and merged pores and it is obtained from the previous section, $A_{open}$ is the cross-sectional area of the material which is occupied by the open pores, and $A_{total}$ is the total cross-sectional area of the structure. By considering a uniform spatial distribution for pores, Eq. (31) can be expressed as follow:

$$
E_{open}=E_{merged}(1-\phi_{open}) \tag{32}
$$

where $\phi_{open}$ is the value of the open porosity of the structure which can be obtained from the experimental data. The proposed algorithm is depicted in Fig. 3.

### 2. 3. Determination of the pore size distribution

Pore size distribution of a porous structure can be obtained by different approaches such as experimental methods and image-based techniques. Moreover, some continuous distribution functions based on the Gaussian distribution are widely used to estimate the distribution of pores by size. One of the most common distribution functions is the normal distribution which is defined as follows:

$$
f(r)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\left(\frac{(\mu-r)^{2}}{2 \sigma^{2}}\right)}, \quad r \in\left[r_{min}, r_{max}\right] \tag{33}
$$

where $\mu$ and $\sigma$ are, respectively, the mean (average) and the standard deviation of the distribution and defined as:

$$
\mu=\frac{1}{n}\left(\sum_{i=1}^{n} r_{i}\right)
\tag{34}
$$

$$
\sigma=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(r_{i}-\mu\right)^{2}}
\tag{35}
$$

For modeling purposes, the relative frequency of pores of radius $r_i$, *i.e.* $p_i$, is assumed to be equal to $f(r_i)$ and the discretization of the radii is done as follow:

$$
r_{i}=r_{m i n}+\Delta r(i-1), \quad i=1,..., n
\tag{36}
$$

where:
$$
\Delta r=\frac{r_{max}-r_{min}}{n-1}
\tag{37}
$$

### 2.4. Finite element modeling of random microstructures
Different groups of artificial porous structures with different porosity values ranging from 10% to 90% are constructed in the present paper to statistically investigate the reliability of the proposed relations. These models are created by random positioning of the spherical voids of different radii in a representative volume element (RVE) and their effective elastic properties are obtained by means of the FEM [36]. To assess the variations caused by the statistical nature of the microstructure, a total of 30 random structures are examined for each level of porosity.

The size of the RVE for each model is $1 \times 1 \times 1\ mm^{3}$ and the diameter of the pores lies between $20\ \mu m$ and $200\ \mu m$. These values are selected in accordance with ref. [37] to satisfy the RVE concept requirements.

Furthermore, in each model, the number $n$ of various pores radii is equal to 5 and a normal distribution function is used to define the distributions of pores by size. The typical models used in computations are shown in Fig. 4. The commercial finite element software ABAQUS (Abaqus Inc., Pawtucket, RI, USA) is used to compute the effective elastic constants of the porous structures. All of the models are meshed using tetrahedral elements. The porous structures are assumed to be made of stainless steel with the properties given in Table 1. Boundary conditions for the FEM models are selected according to the protocol given in ref. [36].

### 3. Results and discussion
In this section, the findings of the FEM simulations are used to assess the reliability of the proposed modifications. Furthermore, the modifications described above are used to predict the effective elastic properties

of some porous ceramics found in the published numerical and experimental papers. It should be noted that we used three models to calculate the elastic moduli of the structures: (i) the classical Mori-Tanaka scheme (MT), (ii) the Mori-Tanaka scheme which is enabled to consider the effect of the merged pores (MMT), and (iii) the Mori-Tanaka scheme which is enabled to consider the effect of the merged and open-cell pores (OMT).

Moreover, pore size distribution is considered based on the information given in the corresponding paper and whenever data about the relative frequency function is not available, a normal distribution function is used to determine the distributions of pores by size. Furthermore, the elastic properties of different materials used in this study are given in Table 1.

### 3.1. Validation of the proposed models

The results obtained from the FEM simulations are used here to validate the proposed modifications. Table 2 gives the mean and the standard deviation values obtained by FEM simulations for the effective Young's modulus of the artificial porous structures. Furthermore, the mean effective Young's modulus values of the porous structures obtained by numerical simulations are compared with the findings of the MT, MMT and OMT approaches in different porosities in Fig. 5. Results confirm the reliability of the proposed relations. Our findings show that for the structures with porosities up to 30%, which only contain isolated pores, the results obtained by the MT method are acceptable and the corresponding relative error between the results obtained by the FEM and MT methods is less than 10%. However, for higher level of porosity values, a considerable amount of the merged pores appears in the structure, and hence the MMT scheme is the appropriate model to approximate the effective elastic moduli of the porous structures. The obtained results show that for the structures with the porosity values greater than or equal to 60%, the value of the relative error of the MT and MMT methods becomes unacceptable. Because of the formation of a large amount of the agglomerates of open-cell pores in the structures at these high levels of porosities, the best estimation of the elastic properties can be achieved by the OMT approach. According to our findings, the accuracy of the OMT method increases as the porosity increases. In this regard, the absolute value of the relative error for these structures decreases from 21% to 10% as the porosity increases from 60% to 90% by using the OMT method.

### 3.2. Application of the proposed modifications in calculation of the effective elastic moduli of the porous ceramics

In order to show the application of the proposed modifications in calculation of the effective elastic properties of the porous ceramics, experimental data presented in refs. [41,42,44,45] are used here as case studies. The comparison between the reported values for the Young's modulus of the porous piezoelectric ceramics with different porosities with the predictions of the MT, MMT and OMT methods is presented in Fig. 6. As shown in this figure, there is no significant difference between the findings of the MT, MMT and OMT approaches in low porosities. However, the amount of the merged pores exists in the porous material increases as the porosity rises and the results obtained by the MMT method are in a better agreement with the experimental data. At porosities greater than 40%, because of the construction of the complicated agglomerates of open-cell pores in the structure, the results obtained by of the OMT approach agree well with the experimental findings.

Figure 7 compares the experimental values reported by Adachi and Sakka [42] for the Young's modulus of porous $\mathrm{SiO}_{2}$ glass ceramic samples with the porosities up to $75 \%$ with the findings of the present paper. Results show that in high porosities, because of the presence of the complicated agglomerates of merged and open-cell pores in the sample, the conventional micromechanical approaches, such as the classical MT scheme, are not able to properly approximate the effective elastic moduli of porous ceramics. However, according to this figure, the model which is able to take into account the effect of the open-cell pores (i.e. the OMT model) is the best one to predict the effective elastic moduli of these kinds of porous structures. Furthermore, in low porosities, the results obtained by the MT scheme and its modifications are almost the same which means the absence or presence of the small amount of the merged and open pores in the structure.

The application of the aforementioned modifications in the calculation of the Young's modulus of the porous ceramics is further investigated by comparing the results obtained by Chen et al. [44] with the predictions of the MT, MMT and OMT methods presented in this study as shown in Fig. 8. Chen et al. [44] fabricated some porous ceramic films with different porosities and obtained their elastic moduli by means of the numerical (FEM) and experimental (nanoindentation) methods. As shown in this figure, in the porosity of $15 \%$, because of the absence or presence of the small amount of the merged pores in the structure, the results obtained by the MT and MMT methods are almost the same and the values of the Young's modulus obtained by these methods are in good agreement with the values reported by Chen et al. [44]. However, the accuracy of the MT method decreases as the porosity increases. In the porosity of $24 \%$, a considerable amount of the merged pores exists in the sample, and hence the assumption of dilute concentration is not acceptable. Thus, the MMT method gives a more accurate estimation than the MT and OMT approaches. In the porosity of $38 \%$, percolation of the voids

starts and increasingly open pores are formed. For porosities larger than 38%, any predictions made by the MT and MMT models would result in large errors while the OMT method gives a reasonable estimation of the Young's modulus.

Table 3 presents the value of the Young's modulus of the porous LSCF ceramic films calculated by means of our different modeling approaches and compares the findings with those obtained by numerical simulations [45]. According to this table, the OMT approach gives an improved fit to the data of the Young's modulus. Results indicate that the value of the relative error for the OMT method does not exceed from 10.5% while the average value of the relative errors is about 49.4% and 45.6% for the MT and MMT schemes, respectively. This is expectable since as stated by Chen *et al.* [45], these structures had interconnected pore networks.
Furthermore, by increasing the porosity, the precision of the MT and MMT methods decreased while the accuracy of the OMT method increased. As mentioned in ref. [45], in the high porosity values, more percentage of pores in the structure interconnected with each other and the value of the tortuosity for the pore phase decreased. As a result, the structure became increasingly interconnected and less twisted. Results obtained in this study confirm these observations. According to our findings, as the value of the porosity increases from 32% to 59%, the absolute value of the relative error increases from 38.3% to 57.8% and from 35.7% to 53.2%, for the MT and MMT approaches, respectively. However, for the case of OMT scheme, increasing the porosity value from 32% to 59% decreases the absolute value of the relative error from 10.2% to 3.2%. This is because of the construction of the complicated agglomerates of open-cell pores in the structure which reduces the value of the tortuosity, and hence the precision of the OMT method increases.

It is worthy to note that the MT method is not able to simulate the anisotropy of a structure containing the spherical pores. However, the MMT and OMT approaches are capable of demonstrating of the anisotropy in the elastic modulus. Indeed, substitution of the overlapped pores by the corresponding ellipsoids causes a difference in the values obtained for the Young's modulus in diverse directions as demonstrated in Fig. 9. In this figure, the numerical values reported by Chen *et al.* [44] for the Young's modulus of a porous ceramic with the porosity of 44.6% in different directions are compared with the predictions of different methods presented in the current study. As shown in this figure, a small anisotropy appears in the results for the case of MMT and OMT models.

## 4. Conclusion

Prediction of the effective elastic moduli of the porous structures is of great interest and micromechanical approaches, such as the well-known Mori-Tanaka scheme, are widely used to characterize the mechanical

properties of these structures in recent years. In this paper, two modifications are applied to the Mori-Tanaka scheme to increase its precision in the estimation of the mechanical properties of the porous materials containing complicated agglomerates of merged and open-cell spherical pores of different radii. Findings of the current paper show that the MT method is appropriate for the porous structures with low porosities which only contain isolated pores whilst for the structures with moderate porosities which contain a considerable amount of the merged pores and for highly porous materials with a large amount of agglomerates of open-cell pores, the MMT and OMT schemes give the reasonable approximations, respectively. The reliability of the proposed relations is further investigated by means of the finite element method. Results obtained from the statistical analysis of the artificial porous structures show that the MT, MMT and OMT approaches are suitable for the porosity range of up to 30%, 30% to 60% and more than 60%, respectively. Furthermore, unlike the classical Mori-Tanaka method, the modified formulations are capable of demonstrating of the probable anisotropy in the effective elastic properties of the porous structures. Good agreement of the obtained results with the published empirical observations for porous ceramics underlines the potential of the proposed methods in characterization of the microstructure-property relation of the porous ceramic structures.

## Conflict of Interest

The authors declare that there is no conflict of interest regarding the publication of this paper. Furthermore, this research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

1. G. Pia, L. Casnedi, M. Ionta, U. Sanna, On the elastic deformation properties of porous ceramic materials obtained by pore-forming agent method, Ceram. Int. 41 (2015) 11097–11105.

2. A. Fritsch, C. Hellmich, P. Young, Micromechanics-derived scaling relations for poroelasticity and strength of brittle porous polycrystals, J. Appl. Mech. 80 (2013) 020905.

3. A.P. Suvorov, A.P.S. Selvadurai, Effective medium methods and a computational approach for estimating geomaterial properties of porous materials with randomly oriented ellipsoidal pores, Comput. Geotech. 38 (2011) 721-730.

4. S. Gong, Z. Li, Y.Y. Zhao, An extended Mori-Tanaka model for the elastic moduli of porous materials of finite size, Acta Mater. 59 (2011) 6820-6830.

5. G. Martinez-Ayuso, M.I. Friswell, S. Adhikari, H.H. Khodaparast, H. Berger, Homogenization of porous piezoelectric materials, Int. J. Solids Struct. 113-114 (2017) 218-229.

6. L. Poh, C. Della, S. Ying, C. Goh, Y. Li, Micromechanics model for predicting effective elastic moduli of porous ceramic matrices with randomly oriented carbon nanotube reinforcements, AIP Adv. 5 (2015) 097153.

7. A.R. Aguiar, J. Bravo-Castillero, U.P. da Silva, Application of Mori-Tanaka method in 3-1 porous piezoelectric medium of crystal class 6, Int. J. Eng. Sci. 123 (2018) 36-50.

8. K.K. Phani, D. Sanyal, The relations between the shear modulus, the bulk modulus and Young's modulus for porous isotropic ceramic materials, Mater. Sci. Eng. A 490 (2008) 305-312.

9. N. Soro, L. Brassart, Y. Chen, M. Veidt, H. Attar, M.S. Dargusch, Finite element analysis of porous commercially pure titanium for biomedical implant application, Mater. Sci. Eng. A 725 (2018) 43-50.

10. M.I. El Ghezal, Y. Maalej, I. Doghri, Micromechanical models for porous and cellular materials in linear elasticity and viscoelasticity, Comput. Mater. Sci. 70 (2013) 51-70.

11. V. Tajeddini, C.H. Lin, A. Muliana, M. Levesque, Average electro-mechanical properties and responses of active composites, Comput. Mater. Sci. 82 (2014) 405-414.

12. L. Dormieux, D. Kondo, Stress-based estimates and bounds of effective elastic properties: The case of cracked media with unilateral effects, Comput. Mater. Sci. 46 (2009) 173-179.

13. P. Koudelka, T. Doktor, J. Valach, D. Kytyr, O. Jirousek, Effective elastic moduli of closed-cell aluminum foams-Homogenization method, U.P.B. Sci. Bull., Series D 75 (2013) 161-170.

14. Y. Zhu, G. Dui, A model considering hydrostatic stress of porous NiTi shape memory alloy, Acta Mech. Solida Sin. 24 (2011) 289-298.

15. C.F. Dunant, B. Bary, A.B. Giorla, C. Peniguel, J. Sanahuja, C. Toulemonde, A. Tran, F. Willot, J. Yvonnet, A critical comparison of several numerical methods for computing effective properties of highly heterogeneous materials, Adv. Eng. Softw. 58 (2013) 1-12.

16. S. Tagliabue, E. Rossi, F. Baino, C. Vitale-Brovarone, D. Gastaldi, P. Vena, Micro-CT based finite element models for elastic properties of glass-ceramic scaffolds, J. Mech. Behav. Biomed. Mater. 65 (2017) 248-255.

17. S. Torquato, Random Heterogeneous Materials, Microstructure and macroscopic properties, Springer, New York, 2002.

18. Y. Benveniste, A new approach to the application of Mori-Tanaka's theory in composite materials, Mech. Mater. 6 (1987) 147-157.

19. J.J. Timothy, G. Meschke, A cascade continuum micromechanics model for the effective elastic properties of porous materials, Int. J. Solids Struct. 83 (2016) 1–12.

20. F. Heidari, M. Razavi, M.E. Bahrolooom, M. Tahiri, L. Tayebi, Investigation of the mechanical properties and degradability of a modified chitosan-based scaffold, Mater. Chem. Phys. 204 (2018) 187–194.

21. K. Khoshroo, T.S. Jafarzadeh Kashi, F. Moztarzadeh, M. Tahriri, H.E. Jazayeri, L. Tayebi, Development of 3D PCL microsphere/TiO₂ nanotube composite scaffolds for bone tissue engineering, Mater. Sci. Eng. C 70 (2017) 586–598.

22. S. Amirkhani, R. Bagheri, A.Z. Yazdi, Manipulating failure mechanism of rapid prototyped scaffolds by changing nodal connectivity and geometry of the pores, J. Biomech. 45 (2012) 2866–2875.

23. S. Amirkhani, R. Bagheri, A.Z. Yazdi, Effect of pore geometry and loading direction on deformation mechanism of rapid prototyped scaffolds, Acta Mater. 60 (2012) 2778–2789.

24. S.M. Rabiee, A. Mozaffari, A. Fathi, Investigation of hydroxyapatite dicalcium phosphate scaffold properties using a Lamarckian immune neural network, Int. J. Comput. Appl. Technol. 53 (2016) 323–335.

25. K. Rahmani-Monfard, A. Fathi, S.M. Rabiee, Three-dimensional laser drilling of polymethyl methacrylate (PMMA) scaffold used for bone regeneration, Int. J. Adv. Manuf. Technol. 84 (2016) 2649–2657.

26. S.M. Rabiee, F. Moztarzadeh, H. Salimi-Kenari, M. Solati-Hashjin, S.M.J. Mortazavi, Study of biodegradable ceramic bone graft substitute, Adv. Appl. Ceram. 107 (2008) 199–202.

27. S.M. Naga, H.F. El-Maghraby, E.M. Mahmoud, M.S. Talaat, A.M. Ibrhim, Preparation and characterization of highly porous ceramic scaffolds based on thermally treated fish bone, Ceram. Int. 41 (2015) 15010–15016.

28. C.W. Chang, Y.R. Wu, K.C. Chang, C.L. Ko, D.J. Lin, W.C. Chen, In vitro characterization of porous calcium phosphate scaffolds capped with crosslinked hydrogels to avoid inherent brittleness, Ceram. Int. 44 (2018) 1575–1582.

29. A. Fritsch, C. Hellmich, L. Dormieux, Ductile sliding between mineral crystals followed by rupture of collagen crosslinks: Experimentally supported micromechanical explanation of bone strength, J. Theor. Biol. 260 (2009) 230–252.

30. T. Mura, Micromechanics of Defects in Solids, second ed., Martinus Nijhoff, Dordrecht, 1987.

31. J. Schjødt-Thomsen, R. Pyrz, The Mori-Tanaka stiffness tensor: diagonal symmetry, complex fibre orientations and non-dilute volume fractions, Mech. Mater., 33 (2001) 531–544.

32. Y. Qing-Sheng, T. Xu, Y. Hui, A stepping scheme for predicting effective properties of the multi-inclusion composites, Int. J. Eng. Sci. 45 (2007) 997–1006.

33. C. Forbes, M. Evans, N. Hastings, B. Peacock, Statistical Distributions, fourth ed., Wiley, New Jersey, 2011.

34. P. Armitage, An overlap problem arising in particle counting, Biom. 36 (1949) 257-266.

35. A. Kusoglu, M.H. Santare, A.M. Karlsson, S. Cleghorn, W.B. Johnson, Micromechanics model based on the nanostructure of PFSA membranes, J. Polym. Sci. Part B: Polym. Phys., 46 (2008) 2404-2417.

36. H. Richter, Mote3D: an open-source toolbox for modelling periodic random particulate microstructures, Model. Simul. Mater. Sci. Eng. 25 (2017) 035011.

37. W.J. Drugan, J.R. Willis., A micromechanics-based nonlocal constitutive equation and estimates of representative volume element size for elastic composites, J. Mech. Phys. Solids 44 (1996) 497-524.

38. S.M. Imani, A.M. Goudarzi, P. Valipour, M. Barzegar, J. Mahdinejad, S.E. Ghasemi, Application of finite element method to comparing the NIR stent with the Multi-Link stent for narrowings in coronary arteries, Acta Mech. Solida Sin. 28 (2015) 605-612.

39. S.M. Imani, A.M. Goudarzi, S.E. Ghasemi, A. Kalani, J. Mahdinejad, Analysis of the stent expansion in a stenosed artery using finite element method: Application to stent versus stent study, Proc. IMechE Part H: J. Eng. Med. 228 (2014) 996-1004.

40. M. Imani, A.M. Goudarzi, D.D. Ganji, A.L. Aghili, The comprehensive finite element model for stenting: The influence of stent design on the outcome after coronary stent placement, J. Theor. Appl. Mech. 51(2013) 639-648.

41. F. Craciun, C. Glassi, E. Roncari, A. Filippi, G. Guidarelli, Electro-elastic properties of porous piezoelectric ceramics obtained by tape casting, Ferroelectr. 205 (1998) 49-67.

42. T. Adachi, S. Sakka, Dependence of the elastic moduli of porous silica gel prepared by the sol-gel method on heat-treatment, J. Mater. Sci. 25 (1990) 4732-4737.

43. C. Yu, S. Ji, Q. Li, Effects of porosity on seismic velocities, elastic moduli and Poisson's ratios of solid materials and rocks, J. Rock Mech. Geotech. Eng. 8 (2016) 35-49.

44. Z. Chen, X. Wang, F. Giuliani, A. Atkinson, Microstructural characteristics and elastic modulus of porous solids, Acta Mater. 89 (2015) 268-277.

45. Z. Chen, X. Wang, F. Giuliani, A. Atkinson, Analyses of microstructural and elastic properties of porous SOFC cathodes based on focused ion beam tomography, J. Power Sources 273 (2015) 486-494.

Fig. 1. Schematic illustration of the cross-section of the porous structure containing isolated, merged and open-cell spherical pores of different radii.

Fig. 2. Schematic illustration of the proposed step-by-step procedure to enable the Mori-Tanaka scheme to consider different sizes for spherical pores.

Fig. 3. Flowchart of the proposed algorithm to predict the effective elastic properties of a porous structure containing merged and open-cell spherical pores of different radii.

Fig. 4. The typical models used in computations with (a) isolated, (b) merged and (c) open-cell spherical pores.

Fig. 5. Comparison between the mean values obtained by numerical simulations for the effective Young's modulus (GPa) of the porous structures with different porosities and the findings of the MT, MMT and OMT approaches.

Fig. 6. Comparison between the results obtained in this study by means of the MT, MMT and OMT schemes and the experimental values reported by Craciun *et al.* [41] for the Young's modulus (GPa) of the porous piezoelectric ceramics with different porosities.

Fig. 7. Comparison between the results obtained in this study by means of the MT, MMT and OMT schemes and the experimental values reported by Adachi and Sakka [42] for the Young's modulus (GPa) of the porous SiO₂ glass ceramic samples with different porosities.

Fig. 8. Comparison between the results obtained in this study by means of the MT, MMT and OMT schemes and the values reported by Chen *et al.* [44] for the Young's modulus (GPa) of the porous LSCF ceramic films with different porosities obtained by nanoindentation and finite element methods.

Fig. 9. Comparison between the results obtained in this study by means of the MT, MMT and OMT schemes and the numerical values reported by Chen *et al.* [44] for the Young's modulus (GPa) of a porous ceramic film with the porosity of 44.6%.

![](./images/813022894006206464_2.jpg)

![](./images/813022894006206464_3.jpg)

![](./images/813022894006206464_4.jpg)

![](./images/813022894006206464_5.jpg)

![](./images/813022894006206464_6.jpg)

![](./images/813022894006206464_7.jpg)

![](./images/813022894006206464_8.jpg)

![](./images/813022894006206464_9.jpg)

![](./images/813022894006206464_10.jpg)

![](./images/813022894006206464_11.jpg)

![](./images/813022894006206464_12.jpg)

Table 1. Elastic properties of different materials used in this study

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>Young's modulus (GPa)</th>
      <th>Poisson's ratio</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Stainless steel</td>
      <td>193</td>
      <td>0.27</td>
      <td>[38-40]</td>
    </tr>
    <tr>
      <td>Piezoelectric ceramics</td>
      <td>667</td>
      <td>0.3</td>
      <td>[41]</td>
    </tr>
    <tr>
      <td>SiO₂ glass ceramic</td>
      <td>72.5</td>
      <td>0.3</td>
      <td>[42,43]</td>
    </tr>
    <tr>
      <td>LSCF ceramic</td>
      <td>175</td>
      <td>0.31</td>
      <td>[44,45]</td>
    </tr>
  </tbody>
</table>

Table 2. The mean and the standard deviation (S.D.) values obtained by numerical simulations for the effective Young's modulus (GPa) of the porous structures with different porosities.

<table>
<thead>
<tr>
<th>Porosity (%)</th>
<th>10</th>
<th>20</th>
<th>30</th>
<th>40</th>
<th>50</th>
<th>60</th>
<th>70</th>
<th>80</th>
<th>90</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mean (GPa)</td>
<td>155.78</td>
<td>120.93</td>
<td>91.39</td>
<td>59.26</td>
<td>36.38</td>
<td>20.61</td>
<td>8.31</td>
<td>3.08</td>
<td>0.73</td>
</tr>
<tr>
<td>S.D. (GPa)</td>
<td>4.67</td>
<td>4.03</td>
<td>3.29</td>
<td>2.81</td>
<td>2.28</td>
<td>1.53</td>
<td>0.83</td>
<td>0.12</td>
<td>0.03</td>
</tr>
</tbody>
</table>

Table 3. Comparison between the results obtained in this study by means of the MT, MMT and OMT schemes and the numerical values reported by Chen et al. [45] for Young's modulus (GPa) of the porous LSCF ceramic films with different porosities.

<table>
<thead>
<tr>
<th>Porosity (%)</th>
<th>Numerical [45]</th>
<th>MT</th>
<th>MMT</th>
<th>OMT</th>
</tr>
</thead>
<tbody>
<tr>
<td>32</td>
<td>56</td>
<td>90.8</td>
<td>87.2</td>
<td>62.4</td>
</tr>
<tr>
<td>38</td>
<td>44</td>
<td>78.5</td>
<td>75.6</td>
<td>48.6</td>
</tr>
<tr>
<td>41</td>
<td>38</td>
<td>73.7</td>
<td>69.3</td>
<td>42.5</td>
</tr>
<tr>
<td>46</td>
<td>31</td>
<td>65.2</td>
<td>60.9</td>
<td>34.4</td>
</tr>
<tr>
<td>51</td>
<td>29</td>
<td>57.5</td>
<td>52.1</td>
<td>27.4</td>
</tr>
<tr>
<td>55</td>
<td>23</td>
<td>51.3</td>
<td>46.1</td>
<td>21.3</td>
</tr>
<tr>
<td>59</td>
<td>19</td>
<td>45.1</td>
<td>40.6</td>
<td>18.4</td>
</tr>
</tbody>
</table>