CALPHAD: Computer Coupling of Phase Diagrams and Thermochemistry 50 (2015) 118-125

![](./images/814619506335809537_1.jpg)

Contents lists available at ScienceDirect

CALPHAD: Computer Coupling of Phase Diagrams and
Thermochemistry

journal homepage: www.elsevier.com/locate/calphad

![](./images/814619506335809537_2.jpg)

# Thermodynamic description, diffusivities and atomic mobilities in binary Ni-Os system

Juan Chen, Cong Zhang, Jiong Wang, Weimin Chen, Ying Tang, Lijun Zhang*, Yong Du

State Key Laboratory of Powder Metallurgy, Central South University, Changsha 410083, China

![](./images/814619506335809537_3.jpg)

## ARTICLE INFO

Article history:
Received 7 March 2015
Received in revised form
9 June 2015
Accepted 10 June 2015
Available online 16 June 2015

Keywords:
Ni-Os system
Thermodynamics
Diffusion
Atomic mobility
CALculation of PHAse Diagram

## ABSTRACT

A systematical study of thermodynamics and diffusion kinetics in the binary Ni-Os system was per- formed in the present work by means of CALculation of PHAse Diagram (CALPHAD) method supported by key experiments. Based on all the available experimental phase equilibria, a full thermodynamic as- sessment of binary Ni-Os system was conducted. A reasonable set of thermodynamic description for the binary Ni-Os system was obtained. Comparisons between the calculated and the measured phase equilibria showed that most of the experimental information can be satisfactorily accounted for by the present thermodynamic description. Moreover, the interdiffusion coefficients in face-centered cubic (fcc) Ni-Os alloys at 1373, 1473, 1523, 1573 and 1623 K were measured by using five groups of Ni-Os semi- infinite diffusion couples together with the Sauer-Freise method. On the basis of the interdiffusion coefficients from the present work and the literature as well as the presently obtained thermodynamic description, atomic mobilities in fcc Ni-Os alloys were then assessed by means of DIffusion-Controlled TRAnsformation (DICTRA) software package. Comprehensive comparisons between the calculated and the measured diffusivities show that most of the experimental data can be well reproduced by the presently obtained atomic mobilities. In addition, the reliability of the atomic mobilities obtained in the present work were further validated by comparing the model-predicted concentration profiles of fcc Ni-Os diffusion couples with the experimental data.

© 2015 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Owing excellent high-temperature mechanical properties and high resistance to creep and fatigue at elevated temperatures, Ni- based superalloys are widely used in both aviation and land-based gas turbine environments [1,2]. Due to their extensive application in extreme environments, their resistance to creep deformation must be as high as possible [3]. One common strategy is to add the alloying elements with extremely low diffusion coefficients at high temperatures. Re exhibits fairly low diffusion coefficient in Ni al- loys and can significantly improve the creep resistance of the Ni- based superalloys [4]. Thus, Re has been added in both second and third generation of single crystal superalloys. Moreover, it is also confirmed that the fourth generation superalloys should contain Ru. Therefore, in order to improve the performance of superalloys under high temperature environment, efforts should be made to find the suitable alloy elements of which diffusion coefficients are comparable with the Re and Ru [3,5-8]. Recently, Youssef et al. [9] carried out the experimental measurements of the interdiffusion coefficients in Ni-rich fcc Ni-Os alloys (i.e., <10 wt% Os) at 1473-1623 K by means of solid diffusion couple technique coupled with the Sauer-Freise method. According to Youssef et al. [9], the de- termined interdiffusion coefficients in fcc Ni-Os alloys are slightly higher than those in fcc Ni-Re alloys above 1373 K, while lower below 1373 K. As a consequence, Os might be a potential alloying element in the new-generation Ni-based superalloys, and the binary Ni-Os system is thus chosen as the target in the present work.

Moreover, knowledge of both thermodynamic and diffusion characteristics in binary Ni-Os system should be of critical im- portance for comprehensive understanding of the microstructure evolution during preparation and service processes of Ni-based superalloys alloying with Os, which is the basis for further design of the novel Ni-based superalloys. Though several experimental measurements of phase equilibria in binary Ni-Os system are available in the literature [10-15], there has been no any ther- modynamic description for the binary Ni-Os system up to now. As for diffusion part, there is only one report on measurement of interdiffusivities in fcc Ni-Os alloys from Youssef et al. [9]. In order to establish a reliable atomic mobility database for fcc Ni-Os al- loys, more experimental interdiffusivities need to be determined. Consequently, the objectives of the present work are (i) to

* Corresponding author. Fax: +86 731 88710855.
E-mail addresses: xueyun168@gmail.com, lijun.zhang@csu.edu.cn (L. Zhang).

http://dx.doi.org/10.1016/j.calphad.2015.06.001
0364-5916/© 2015 Elsevier Ltd. All rights reserved.

critically evaluate the experimental phase equilibria and diffusivities in the binary Ni-Os system available in the literature, (ii) to measure more interdiffusivities in fcc Ni-Os alloys by employing solid single-phase diffusion couples, (iii) to perform thermodynamic assessment of binary Ni-Os system based on the critically reviewed phase equilibria information by means of CALculation of PHAse Diagram (CALPHAD) technique, and (iv) to evaluate accurate atomic mobilities for fcc Ni-Os alloys by using DIffusion-Controlled TRAnsformation (DICTRA) software package.

## 2. Model description

### 2.1. Thermodynamic models

#### 2.1.1. Unary phases
The Gibbs energy function $G_{i}^{\phi}(T)={ }^{0} G_{i}^{\phi}(T)-H_{i}^{SER}(298.15 \mathrm{~K})$ for the pure element $i$ ($i=\mathrm{Ni}, \mathrm{Os}$) in the phase $\phi$ ($\phi$=liquid, fcc or hcp) can be described as
$$
G_{i}^{\phi}(T)=a+b T+c T \ln T+d T^{2}+e T^{-1}+f T^{3}+g T^{7}+h T^{-9}
\tag{1}
$$
where $H_{i}^{SER}(298.15 \mathrm{~K})$ is the molar enthalpy of the element $i$ at 298.15 K and 1 bar in its standard element reference (SER) state (i.e., fcc for Ni while hcp for Os), and $T$ is the absolute temperature. The last two terms in Eq. (1) are used only outside the ranges of stability, the term $g T^{7}$ for a liquid below the melting point while the term $h T^{-9}$ for solid phases above the melting point. In the present work, the Gibbs free energy functions of pure elements are taken from the SGTE database by Dinsdale [16].

#### 2.1.2. Solution phases
In the binary Ni-Os system, liquid, fcc-(Ni) and hcp-(Os) are modeled as solution phases and their Gibbs energy can be described with the substitutional solution model,
$$
\begin{aligned}
G_{m}^{\phi}= & x_{\mathrm{Ni}} \cdot{ }^{0} G_{\mathrm{Ni}}^{\phi}+x_{\mathrm{Os}} \cdot{ }^{0} G_{\mathrm{Os}}^{\phi}+R T \cdot\left(x_{\mathrm{Ni}} \ln x_{\mathrm{Ni}}^{\phi}+x_{\mathrm{Os}} \ln x_{\mathrm{Os}}^{\phi}\right)+{ }^{E} G_{m}^{\phi} \\
& +\Delta G^{m g, \phi}
\end{aligned}
\tag{2}
$$
where ${ }^{E} G_{m}^{\phi}$ is the excess Gibbs free energy and $\Delta G^{m g, \phi}$ is the magnetic contribution to the Gibbs free energy. The excess Gibbs free energy is usually denoted as a Redlich-Kister polynomial,
$$
{ }^{E} G_{m}^{\phi}=x_{\mathrm{Ni}} \cdot x_{\mathrm{Os}} \cdot \sum_{n=0}^{m}{ }^{n} L_{\mathrm{Ni}, \mathrm{Os}}^{\phi} \cdot\left(x_{\mathrm{Ni}}-x_{\mathrm{Os}}\right)^{n}
\tag{3}
$$
where ${ }^{n} L_{\mathrm{Ni}, \mathrm{Os}}^{\phi}$ is the $n$th interaction parameter between Ni and Os, and can be expressed as
$$
{ }^{n} L_{\mathrm{Ni}, \mathrm{Os}}^{\phi}=a_{n}+b_{n} T
\tag{4}
$$

The interaction coefficients $a_{n}$ and $b_{n}$ ($n=0,1,2...$) are to be evaluated during the optimization process.

The magnetic contribution to the Gibbs energy of fcc-(Ni) phase is also considered in the present work, and can be described by using the model proposed by Hillert and Jarl [17],
$$
\Delta G^{m g, \phi}=R T \ln \left(\beta^{\phi}+1\right) f\left(\tau^{\phi}\right)
\tag{5}
$$
where $\beta^{\phi}$ is the average atomic moment per atom of the alloy expressed in Bohr magnetons, $f(\tau^{\phi})$ a polynomial ($\tau^{\phi}=T / T_{C}$), and $T_{C}$ is the Curie temperature of the phase $\phi$. The parameters $T_{C}$ and $\beta$ are usually expressed as a function of composition[18]:
$$
T_{C}=x_{\mathrm{Ni}} \cdot{ }^{0} T_{C, \mathrm{Ni}}^{\phi}+x_{\mathrm{Os}} \cdot{ }^{0} T_{C, \mathrm{Os}}^{\phi}+x_{\mathrm{Ni}} \cdot x_{\mathrm{Os}} \cdot \sum_{i=0}^{n}{ }^{i} T_{C, \mathrm{Ni}, \mathrm{Os}}^{\phi}\left(x_{\mathrm{Ni}}-x_{\mathrm{Os}}\right)^{i}
\tag{6}
$$

$$
\beta=x_{\mathrm{Ni}} \cdot{ }^{0} \beta_{\mathrm{Ni}}^{\phi}+x_{\mathrm{Os}} \cdot{ }^{0} \beta_{\mathrm{Os}}^{\phi}+x_{\mathrm{Ni}} \cdot x_{\mathrm{Os}} \cdot \sum_{i=0}^{n}{ }^{i} \beta_{\mathrm{Ni}, \mathrm{Os}}^{\phi}\left(x_{\mathrm{Ni}}-x_{\mathrm{Os}}\right)^{i}
\tag{7}
$$
where ${ }^{0} T_{C, A}^{\phi}$ and ${ }^{0} \beta_{A}^{\phi}$, respectively are the Curie temperature and average atomic moment for pure element A (A=Ni or Os), which can be directly taken from Dinsdale [16]. While ${ }^{i} T_{C, \mathrm{Ni}, \mathrm{Os}}^{\phi}$ and ${ }^{i} \beta_{\mathrm{Ni}, \mathrm{Os}}^{\phi}$, respectively ($i=0,1,2...$) are the interaction parameters, which need to be assessed based on the experimental data.

### 2.2. Atomic mobilities

For a multicomponent system, the temporal profile of diffusing species $k$ is given by Fick's law as
$$
\frac{\partial c_{k}}{\partial t}=-\nabla \cdot J_{k} \quad(k=1,..., n)
\tag{8}
$$
where $c_{k}$ is the concentration in moles per volume, and $\nabla$ denotes the divergence operator. In a volume fixed frame of reference, the flux of species $k$ ($J_{k}$) can be expressed as
$$
J_{k}=-\sum_{j=1}^{n-1} \tilde{D}_{k j}^{n} \nabla c_{j}
\tag{9}
$$
where $\tilde{D}_{k j}^{n}$ represents the interdiffusion coefficient, and is related to the flux of element $k$ with the gradient of component $j$ and reference component $n$. In a solution phase, $\tilde{D}_{k j}^{n}$ can be given by
$$
\tilde{D}_{k j}^{n}=\sum_{i}\left(\delta_{i k}-x_{k}\right) x_{i} M_{i}\left(\frac{\partial \mu_{i}}{\partial x_{j}}-\frac{\partial \mu_{i}}{\partial x_{n}}\right)
\tag{10}
$$
where $\delta_{i k}$ is the Kronecker delta ($\delta_{i k}=1$ if $i=k$, otherwise $\delta_{i k}=0$). $x_{i}$ and $\mu_{i}$ are the mole fraction and chemical potential of element $i$, respectively. $M_{i}$ is the so-called atomic mobility for the element $i$.

According to the theory of absolute rate, the atomic mobility for an element $k$ in fcc phase, $M_{k}$, can be divided into a frequency factor $M_{k}^{0}$ and an activation enthalpy $Q_{k}$. Both $M_{k}^{0}$ and $Q_{k}$ are generally dependent on the composition, temperature and pressure. By neglecting the ferromagnetic effect in fcc phase, $M_{k}$ can be expressed as [19,20]
$$
\begin{aligned}
M_{k} & =\frac{1}{R T} \exp \left(\frac{-Q_{k}+R T \ln \left(M_{k}^{0}\right)}{R T}\right) \\
& =\frac{1}{R T} M_{k}^{0} \exp \left(\frac{-Q_{k}}{R T}\right) \\
& =\frac{1}{R T} \exp \left(\frac{\Phi_{k}}{R T}\right)
\end{aligned}
\tag{11}
$$
where $R$ is the gas constant and $T$ is temperature in Kelvin. In the DICTRA treatment, $\Phi_{k}$ for binary alloys can be represented with the Redlich-Kister expansion as
$$
\Phi_{k}=\sum_{i} x_{i} \Phi_{k}^{i}+\sum_{i} \sum_{j>i} x_{i} x_{j}\left[\sum_{r=0}^{m}{ }^{r} \Phi_{k}^{i, j}\left(x_{i}-x_{j}\right)^{r}\right]
\tag{12}
$$
where $\Phi_{k}^{i}$ and ${ }^{r} \Phi_{k}^{i, j}$ are the mobility parameters for pure elements and binary interaction parameters, respectively. They can be either assessed based on various experimental diffusivities or derived based on semi-empirical relations/first-principles calculations.

Assuming that the mono-vacancy atomic exchange is the diffusion mechanism, the tracer diffusion coefficient of the element $k$ can be correlated with its mobility via the Einstein relation
$$
D_{k}^{*}=R T M_{k}
\tag{13}
$$

In the binary Ni-Os system, the tracer diffusivity $D_{k}^{*}$ can be related to the interdiffusion coefficient $\tilde{D}$ by Darken's equation [21]

$$\bar{D}=\left(x_{N i} D_{O s}^{*}+x_{O s} D_{N i}^{*}\right) \phi\tag{14}$$

where $\phi$ is the thermodynamic factor, and can be expressed as

$$\phi=1+\frac{\partial \ln \gamma_{N i}}{\partial \ln x_{N i}}=1+\frac{\partial \ln \gamma_{O s}}{\partial \ln x_{O s}}\tag{15}$$

where $\gamma_{N i}$ and $\gamma_{O s}$ are the activity coefficients of components Ni and Os, respectively.

### 2.3. Semi-empirical model for evaluating self-diffusivities in metastable fcc Os

Since fcc Os is not the most thermodynamically stable phase, it is difficult to obtain the diffusion coefficients of the fcc-(Os) phase through experimental measurements. Moreover, there is no direct report on atomistic simulation of self-diffusion coefficient in fcc-(Os). Fortunately, there exists one piece of information on the first-principles calculation of activation energy for self-diffusion in fcc Os [22]. Thus, based on the first-principles computed activation energy, the frequency prefactor $D_{0}$ for self-diffusion in fcc Os can be estimated on the basis of some semi-empirical correlations between activation energy $(Q)$ and frequency prefactor, as done similarly in our previous work on fcc Pt-Al alloys [23].

According to Askill [24], the simplest correction between activation energy and frequency prefactor is due to Dushman and Langmuir [25]:

$$D_{0}=\frac{Q a^{2}}{N h}\tag{16}$$

where $a$ is the lattice parameter, $N$ is the Avogadro constant, while $h$ is the Plank's constant.

## 3. Review of literature data

### 3.1. Phase equilibria

The available experimental phase diagram and thermodynamic data of the binary Ni−Os system have been reviewed by Nash et al. [26] in 1991. After that, however, some new data have been published. Therefore, there is a need to perform a critical review of all the phase diagram and thermodynamic data of the Ni−Os system available in the literature here. All the data are concisely categorized as follows.

According to Köster et al. [10], the crystallization of the Ni−Os alloys in cast state is of peritectic type, which was confirmed by two-phase microstructures of the specimens through metallography examination. The peritectical crystallization was further validated by measuring the distribution coefficient of Os between solid (Ni) and liquid in the Ni−0.03 at% Os alloy by Samadi et al. [11]. Moreover, Velikanova et al. [12] reported that the peritectic reaction in the Ni−Os system occurs at the temperature of 1773 K, which was measured by means of differential thermal analysis (DTA). The peritectic reaction data from Köster et al. [10] and Velikanova et al. [12] are consistent with each other, and are used in the present optimization.

In addition, Köster et al. [10] also determined the solubility of Os in Ni to be 5 at% at 1273 K and 9.3 at% at 1473 K by using X-ray diffraction (XRD) and microscopic methods. Phillips Jr. et al. [13] reported that the Ni−6.25 at% Os alloy is of fcc-(Ni) single-phase structure at 1477 K by means of microscopy and XRD. Based on the electron probe microanalysis (EPMA) and XRD techniques, Velikanova et al. [12] determined the solubility of Os in Ni to be 9.2 at% at 1473 K and 11.2 at% at 1673 K. All the above-mentioned solubility of Os in Ni [10,12,13] agree with each other and thus are employed in the present optimization. Furthermore, Velikanova et al. [12] reported that the solubility of Ni in Os is 9.2 at% at 1473 K and 11.2 at% at 1673 K on the basis of EPMA and XRD results. Besides, Prigent et al. [14] measured the solubility of Ni in Os to be 11 at% at 1273 K on the basis of EPMA and XRD techniques. Considering that the solubility of Ni in Os determined by the two groups agree with each other in general, the data from Velikanova et al. [12] and Prigent et al. [14] are employed in the present optimization.

As for the Curie temperatures and magnetic moments in the binary Ni−Os system, there are also several investigations available in the literature. Crangle et al. [15] measured the Curie temperatures in fcc-(Ni) by using a thermocouple placed in good thermal contact with the specimen. Besides, Köster et al. [10] also determined the Curie temperatures in fcc-(Ni) single-phase region and fcc-(Ni)+hcp-(Os) two-phase region. Considering that both sets of data are in consistent with each other and also agree with the assessed Curie temperature for pure Ni (i.e., 633 K) by Dinsdale [16], the Curie temperatures measured by Refs. [15,16] are employed in the present assessment. In addition, Crangle et al. [15] also determined the magnetic moments in fcc-(Ni) phase by extrapolating the curve of spontaneous magnetizations against temperature. However, the magnetic moment of pure Ni (i.e., 0.607 μB) determined by Crangle et al. [15] shows a deviation from the assessed average magnetic moment of pure Ni (i.e., 0.52 μB) by Dinsdale [16]. Considering that there is only one set of magnetic moments in fcc-(Ni) phase of the Ni−Os system, such a deviation (i.e., 0.607−0.52=0.087 μB) for pure Ni can be regarded to be a systematic one for the data in fcc-(Ni) phase of the Ni−Os system determined by Crangle et al. [15]. With such a systematic correction (0.087 μB), the magnetic moments determined by Crangle et al. [15] are then used in the present thermodynamic assessment.

### 3.2. Diffusivities in fcc-(Ni) phase

There only exist some experimental reports on self-diffusivities in pure Ni and interdiffusivities in fcc-(Ni) phase of the Ni−Os system. Considering that all the self-diffusivities in pure Ni available in the literature have been critically reviewed in our previous publication [27], the review of self-diffusivities in pure Ni is thus omitted here.

The only existing experimental information on interdiffusivities in fcc Ni−Os alloys is from Youssef et al. [9], who measured the interdiffusion coefficients at 1473−1623 K by using the diffusion couple technique together with the Sauer−Freise method. In order to establish a set of reliable atomic mobility parameters in fcc Ni−Os alloys, the accuracy of the data measured by Youssef et al. [9] needs to be confirmed on one hand, and more experimental data also need to be provided on the other hand. Therefore, the experimental measurement of more experimental interdiffusivities in fcc Ni−Os alloy is to be conducted in the present work.

## 4. Experimental procedure

### 4.1. Sample preparation and microchemical analysis

Ni−Os alloy ingots were prepared in a high purity argon atmosphere using an arc melting furnace (WKDHL-1, Optoelectronics Co., Ltd., Beijing, China), which is equipped with a non-consumable tungsten electrode and a water-cooled copper anode. The pure Ni ingots and Os pieces with purity of 99.99 wt% were used as the raw materials. In order to make sure that the Os pieces are completely dissolved in the Ni ingot, a three-step method was

employed in the present work. Firstly, the same weight amount of Os pieces and Ni ingots were melted together. Then, the rest of Ni ingots were gradually added. After that, the melted alloy ingot was reversed and re-melted for at least 5 times to improve the homogeneity. By using this method, the Ni–Os alloy ingots with Os content of 0.91 at%, 2.76 at%, 4.18 at%, 5.13 at% and 6.09 at% were prepared. The Ni–Os alloy ingots and a high-purity Ni bar were then annealed in sealed quartz tubes at $1573\pm2$ K for 288 ks to further improve their homogeneity and increase the grain size. Subsequently, the annealed Ni–5.13 at% Os ingot and pure Ni bar were cut into blocks with the dimension of $5\times5\times1$ mm³. After being grounded and polished, the Ni–5.13 at% Os and pure Ni blocks were bound together with Mo clamps to form 5 groups of Ni/Ni–5.13 at% Os diffusion couples. The couples were then encapsulated in vacuum quartz tubes and annealed at $1373\pm2$, $1473\pm2$, $1523\pm2$, $1573\pm2$ and $1623\pm2$ K for durations of 493.2, 372.6, 131.4, 158.4 and 43.2 ks, respectively. Finally, the quartz tubes were taken out from the furnace and directly quenched in water. The X-ray diffraction (XRD) powder measurements of all the annealed Ni–Os alloys were performed using Cu-Kα radiation on a X-ray diffractometer (Rigaku D-max/2550 VB+) at 40 kV and 300 mA. The Ni/Ni–5.13 at% Os diffusion couples were further examined by EPMA (JXA-8100, JEOL, Japan) to determine the concentration-distance profiles. The error for concentration measurements is within 1%.

### 4.2. Determination of diffusion coefficients

When a diffusion couple anneals at a certain temperature after a certain time, the interdiffusion occurs and a concentration-distance profile $c_x$ can be obtained. Here, the profiles were obtained by measuring the concentration of the diffusion species at depth $x$ with EPMA, and then the profiles were used to calculate the interdiffusivities $\tilde{D}$. There are several methods which can be used to determine interdiffusion coefficients in binary systems. In the present work, the Sauer-Freise method is used to calculate the interdiffusivities $\tilde{D}$ of fcc Ni-Os alloys,

$$
\tilde{D}=\frac{1}{2 t} \cdot \frac{d x}{d Y_{\mathrm{Os}}} \cdot\left[\left(1-Y_{\mathrm{Os}}\right) \cdot \int_{-\infty}^{x} Y_{\mathrm{Os}} \cdot d x+Y_{\mathrm{Os}} \cdot \int_{x}^{\infty}\left(1-Y_{\mathrm{Os}}\right) \cdot d x\right]
\tag{17}
$$

where $t$ is diffusion time, and $Y_{\text{Os}}$ is the normalized concentration given by

$$
Y_{\mathrm{Os}}=\frac{C_{\mathrm{Os}}-C_{\mathrm{Os}}^{-}}{C_{\mathrm{Os}}^{+}-C_{\mathrm{Os}}^{-}}
\tag{18}
$$

where $C_{\text{Os}}^{-}$ is the concentration of Os at one end of the diffusion couple, while $C_{\text{Os}}^{+}$ is that at the other end of the diffusion couple. $C_{\text{Os}}$ is the concentration at which $\tilde{D}$ is to be evaluated.

## 5. Results and discussion

### 5.1. Thermodynamic part

The XRD patterns of all the prepared 5 binary Ni-Os alloys, i.e., Ni-0.91 at% Os, Ni-2.76 at% Os, Ni-4.18 at% Os, Ni-5.13 at% Os, Ni-6.09 at% Os alloys after homogenization at $1573\pm2$ K for 288 ks are presented in Fig. 1. As indicated in the figure, all the five Ni–Os alloys are in the same fcc single-phase region. Moreover, as the content of Os increases, the characteristic peaks of fcc-(Ni) move to one direction gradually. Table 1 summarizes the lattice parameters for different alloys in the binary Ni–Os system measured in the present work together with those from the literature. As can be seen from the table, for fcc-(Ni) phase, as the concentration of Os dissolved in (Ni) increases, the lattice parameter increases from 0.35241 nm for pure Ni [28] at room temperature to 0.3548(1) nm for the alloys containing 6.09 at% Os at 1573 K. Moreover, the presently obtained concentration-dependent lattice constants of fcc-(Ni) in the binary Ni–Os alloys agree very well with the results from Köster et al. [10].

![](./images/814619506335809537_4.jpg)

Fig. 1. XRD patterns of different Ni–Os alloys Ni-0.91 at% Os, 2.76 at% Os, 4.18 at% Os, 5.13 at% Os, 6.09 at% Os annealed at 1573 K for 288 ks.

<table>
<caption>Table 1 Summary of lattice parameters reported in the literature and measured in the present work for different fcc Ni-Os alloys.</caption>
<thead>
<tr>
<th>Phase</th>
<th>Annealing temperature (K)</th>
<th>Os content (at%)</th>
<th colspan="3">Lattice parameter (nm)</th>
<th>Reference</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>a</th>
<th>b</th>
<th>c</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>(Ni)</td>
<td>298</td>
<td>0</td>
<td>0.35241</td>
<td></td>
<td></td>
<td>[28]</td>
</tr>
<tr>
<td></td>
<td>1573</td>
<td>0.91</td>
<td>0.3532(2)</td>
<td></td>
<td></td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>1473</td>
<td>1</td>
<td>0.3526(5)</td>
<td></td>
<td></td>
<td>[10]</td>
</tr>
<tr>
<td></td>
<td>1573</td>
<td>2.76</td>
<td>0.3541(9)</td>
<td></td>
<td></td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>1473</td>
<td>3.4</td>
<td>0.3537(3)</td>
<td></td>
<td></td>
<td>[10]</td>
</tr>
<tr>
<td></td>
<td>1573</td>
<td>4.18</td>
<td>0.3542(9)</td>
<td></td>
<td></td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>1573</td>
<td>5.13</td>
<td>0.3543(3)</td>
<td></td>
<td></td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>1573</td>
<td>6.09</td>
<td>0.3548(1)</td>
<td></td>
<td></td>
<td>This work</td>
</tr>
</tbody>
</table>

Based on the critically reviewed phase equilibria from the literature as well as those from the present work, the thermodynamic optimization was carried out by using the PARROT module incorporated in the Thermo-Calc software [29,30], which can minimize the sum of the squared differences between the measured and the calculated values. During the optimization, each piece of experimental information was given as a certain weight. For the first step, the mutual solubilities of Os and Ni in the phases fcc-(Ni) and hcp-(Os) were considered. Parameters $a$ and $b$ in Eq. (4) were adjusted based on the experimental data. For the second step, the parameters of liquid phases were employed to reproduce the temperature and compositions of the unique invariant equilibria. For the third step, the Curie temperatures and the magnetic moments (but with a systematic correction) were considered. Finally, the thermodynamic parameters for all phases were adjusted simultaneously by taking into account all of the critically reviewed phase equilibria. The finally obtained thermodynamic parameters are listed in Table 2. As can be seen in Table 2, the $a$ value in hcp-(Os) phase is positive, indicating the repulsive interactions in hcp-(Os) phase. To confirm this fact, the first-principles calculations

<table>
<caption>Table 2<br>Thermodynamic parameters in the Ni–Os system obtained in the present workª.</caption>
<thead>
<tr>
<th>Phase</th>
<th>Thermodynamic parameters</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liquid: (Ni,Os)₁</td>
<td>⁰L<sub>Ni,Os</sub><sup>Liquid</sup> = + 16, 713.57</td>
<td>This work</td>
</tr>
<tr>
<td>fcc: (Ni,Os)₁(Va)₁</td>
<td>⁰L<sub>Ni,Os:Va</sub><sup>Fcc_A1</sup> = − 2744.77 + 16.41T</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>⁰T<sub>C,Ni:Va</sub><sup>Fcc_A1</sup> = + 633</td>
<td>[16]</td>
</tr>
<tr>
<td></td>
<td>⁰T<sub>C,Ni,Os:Va</sub><sup>Fcc_A1</sup> = − 4463.84</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>⁰β<sub>Ni:Va</sub><sup>Fcc_A1</sup> = + 0.52</td>
<td>[16]</td>
</tr>
<tr>
<td></td>
<td>⁰β<sub>Ni,Os:Va</sub><sup>Fcc_A1</sup> = − 3.88</td>
<td>This work</td>
</tr>
<tr>
<td>Hcp: (Ni,Os)₁(Va)₀.₅</td>
<td>⁰L<sub>Ni,Os:Va</sub><sup>Hcp_A3</sup> = + 7655.31 + 14.9T</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>⁰T<sub>Ni:Va</sub><sup>Hcp_A3</sup> = + 633</td>
<td>[16]</td>
</tr>
<tr>
<td></td>
<td>⁰β<sub>Ni:Va</sub><sup>Hcp_A3</sup> = + 0.52</td>
<td>[16]</td>
</tr>
</tbody>
</table>

ª Temperature (T) in Kelvin and Gibbs energy in J/mole-atoms. The Gibbs energies for the pure elements are taken from the compilation by Dinsdale [16].

were also employed in the present work to calculate the enthalpy of mixing for hcp-(Os) phase at ground state. The detail calculation procedure can be referred to the previous work in our group [31], and thus is not described here. The first-principles computed enthalpy of mixing for hcp-(Os) phase is 1180 J/mol. The positive enthalpy of mixing for hcp-(Os) phase at 0 K according to the present first-principles calculations exactly confirms the repulsive interactions in hcp-(Os) phase, validating the reliability of positive a values in hcp-(Os) phase.

The computed Ni–Os phase diagram based on the presently obtained thermodynamic parameters is shown in Fig. 2. As shown in this figure, the present calculations can well reproduce both the literature data [10–14] and the presently obtained data. The calculated temperature of peritectic reaction (liquid+(Os)↔(Ni)) is 1773 K, which is exactly the same with the result due to DTA measurement by [12].

Fig. 3(a) shows the calculated Curie temperatures in the binary Ni–Os system, compared with the experimental data from Köster et al. [10] and Crangle et al. [15] based on the alloys annealed at different temperatures. As can be seen in Fig. 3(a), the calculated Curie temperatures in the single fcc-(Ni) phase of the Ni–Os system decrease as the content of Os increases, and keep as a constant in the two-phase region of fcc-(Ni)+hcp-(Os). This fact is in good agreement with the experimental data [10,15]. While Fig. 3(b) gives the calculated average magnetic moments in fcc-(Ni) single phase of the Ni–Os system in comparison with the experimental data by Crangle et al. [15]. As shown in Fig. 3(b), there exists a gap between the calculated average magnetic moments and the experimental data, which originates from the difference in magnetic moments of pure Ni. If the difference in magnetic moments of pure Ni is taken as the systematic correction (i.e., 0.087 μB), the magnetic moments determined by Crangle et al. [15] can be well reproduced (shown in dash line).

![](./images/814619506335809537_5.jpg)

Fig. 2. Calculated Ni–Os phase diagram, compared with the experimental data from this work and the literature [10–15].

![](./images/814619506335809537_6.jpg)

Fig. 3. Calculated Curie temperatures and magnetic moments for Ni–Os alloys: (a) calculated Curie temperatures compared with the experimental data from Köster et al. [10] and Crangle et al. [15] and (b) calculated magnetic moments compared with the experimental data from Crangle et al. [15].

![](./images/814619506335809537_7.jpg)

Fig. 4. Comparison between the measured and the model-predicted concentration profiles of Ni/Ni-5.13 at% Os diffusion couples annealed at (a) 1373 K, (b) 1473 K, (c) 1523 K, (d) 1573 K and (e) 1623 K.

### 5.2. Diffusion part

Fig. 4 displays the measured concentration-distance profiles of the present Ni/Ni-5.13 at% Os diffusion couples annealed at 1373, 1473, 1523, 1573 and 1623 K. Based on the measured concentration-distance profiles, the interdiffusion coefficients in fcc-(Ni) of the binary Ni-Os system can be calculated by using the Sauer-Freise method, as described in Section 4.2. The finally obtained interdiffusion coefficients at 1373, 1473, 1523, 1573 and 1623 K are presented in Fig. 6. It can be seen from the figure that the presently determined interdiffusivities increase as the temperature increases, and are slightly concentration-dependent. Moreover, the presently obtained interdiffusivities are generally lower than those from Youssef et al. [9], and their differences increase as the concentration of Os increases. Considering the fact that the contribution of boundary diffusion might be included in the higher interdiffusivities, only those interdiffusivities determined in the present work are considered in the present assessment of the mobility parameters.

Angsten et al. [22] computed the activation enthalpy ($Q_k = 527, 833. 6 J/mol$) for self-diffusion in pure fcc Os by using the first-principles calculation. The frequency factor ($D_0$) of self-diffusivities was evaluated by using the semi-empirical relation [25] as shown in Eq. (16). The lattice parameter $a$ utilized in Eq. (16) is $3.866 \times 10^{-10}$ m based on the first-principles work by Wang et al. [32]. The value of frequency factor for self-diffusion in pure fcc Os is then calculated to be $1.96 \times 10^{-4} \mathrm{m}^{2} / \mathrm{s}$.

The optimization of the model parameters in Eqs. (10)-(12) was conducted by means of the PARROT module incorporated in the DICTRA software package [19] based on the diffusivities from the present experiments. The thermodynamic description of the fcc phase in the $Ni-Os$ system was directly taken from the present work (Section 5.1). The assessment procedure of atomic mobilities was conducted in the following steps. In the first step, only the mobility parameters of self- and impurity diffusivities were considered. The mobility parameter for self-diffusion in fcc Ni was directly taken from Zhang et al. [27] because all the experimental data over a wide temperature rang can be reproduced. While the mobility parameter for self-diffusion in metastable fcc Os was set to be the data evaluated by using the first-principle computed data together with the semi-empirical relation in Eq. (16). Due to lack of any experimental information, the mobility parameter for impurity diffusion of Ni in fcc Os was just assumed to be equivalent to that for self-diffusion in pure fcc Os for simplification. The assessment of the mobility parameters for impurity diffusion of Os in Ni was to be carried out based on the corresponding experimental interdiffusivities. In the second step, the interdiffusivities were directly calculated based on the obtained four end-members. Whether the addition of interaction parameters depends on the degree of the fit to the experimental data. It was finally found that only four end members were enough to reproduce the corresponding experimental data well. The finally obtained atomic

<table><caption>Table 3 Summary of atomic mobility parameters of fcc Ni–Os alloys obtained in the present work.</caption>
<thead>
<tr>
<th>Mobility</th>
<th>Parameters</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mobility of Ni</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\phi_{Ni}^{Ni}$</td>
<td>−271, 377.6 − 81.79T</td>
<td>[27]</td>
</tr>
<tr>
<td>$\phi_{Ni}^{Os}$</td>
<td>−527, 833.6 − 70.96T</td>
<td>This work</td>
</tr>
<tr>
<td>Mobility of Os</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\phi_{Os}^{Os}$</td>
<td>−527, 833.6 − 70.96T</td>
<td>This work</td>
</tr>
<tr>
<td>$\phi_{Os}^{Ni}$</td>
<td>−359, 250 − 50.87T</td>
<td>This work</td>
</tr>
</tbody>
</table>

![](./images/814619506335809537_8.jpg)

Fig. 5. Calculated temperature dependence of self-diffusion coefficients of Ni in fcc Ni, self-diffusion coefficients of Os in fcc Os, impurity diffusion coefficients of Ni in fcc Os and impurity diffusion coefficients of Os in fcc Ni, compared with the extrapolated data in the present work.

![](./images/814619506335809537_9.jpg)

Fig. 6. Comparison between the calculated composition-dependent interdiffusion coefficients at 1373–1623 K and the experimental data from this work and Youssef et al. [9]. A constant, M, is added in order to separate the data for different temperatures in the figure.

mobilities in fcc phase of Ni–Os system together with those from the literature are listed in Table 3.

Fig. 5 shows the calculated temperature dependence of self-diffusion coefficients in pure fcc Ni and Os as well as impurity diffusion coefficients of Ni in fcc Os and Os in fcc Ni. As can be seen, the activation enthalpy ($Q_{k}$) of Os in fcc Ni is evaluated to be 359,250 J/mol in the present work, which is in very good agreement with the first-principles computed activation enthalpy (343,380.8 J/mol) by Zacherl [5]. This fact indicates that the obtained atomic mobility of Os in fcc Ni should be reasonable.

Fig. 6 presents the comparison between the calculated interdiffusion coefficients based on the currently obtained atomic mobilities and the experimental data from literature [9] and the present measurements. As is apparently shown in the figure, the calculated interdiffusivities agree well with the experimental data in this work but show a deviation from the literature data [9], which were not utilized in the present assessment.

To further validate the currently obtained atomic mobilities of fcc phase in the Ni–Os system, the comparison between the calculated and the measured concentration-distance profiles in the diffusion couples at different temperatures was also performed. The simulated results for Ni/Ni–5.13 at% Os diffusion couples at 1373, 1473, 1523, 1573 and 1623 K, based on the present atomic mobilities were compared with the corresponding experimental data, as shown in Fig. 4. The detailed annealing conditions can be found in each plot. As can be seen in Fig. 4, all the model-predicted concentration-distance profiles in those diffusion couples on the basis of the currently assessed atomic mobilities are in good agreement with all the experimental data in the present work. It indicates the reliability of the presently obtained mobility parameters of fcc phase.

### 6. Summary

The present work is devoted to systematically studying the thermodynamics and diffusion kinetics in the Ni–Os system via an integration of experiments, semi-empirical correlations, first-principles calculations, and CALPHAD approach. Based on the critically reviewed phase equilibria available in the literature, a self-consistent set of thermodynamic description for the Ni–Os system was obtained. The calculated phase equilibria are in good agreement with the experimental data. By means of the prepared bulk diffusion couples, the concentration-dependent interdiffusion coefficients in fcc Ni–Os alloys were determined at 1373–1623 K. On the basis of the presently obtained experimental diffusion coefficients, the atomic mobilities in fcc phase of the Ni–Os system were assessed by means of the DICTRA software package. Most of the experimental diffusivities in fcc Ni–Os alloys can be well described by the present atomic mobilities. Moreover, the reliability of the currently assessed atomic mobilities parameters were further validated by comparing the model-predicted concentration-distance profiles in the Ni–Os diffusion couples at different temperatures with the experimental data.

### Acknowledgments

The financial support from the National Natural Science Foundation for Youth of China (Grant no. 51301208), the National Natural Science Foundation of China (Grant nos. 51474239 and 51429101), the Hunan Provincial Natural Science Foundation for Youth of China (Grant no. 2015JJ3146), and the National Basic Research Program of China (Grant no. 2014CB644002) is greatly acknowledged. Lijun Zhang acknowledges the support from

Shenghua Scholar Program of Central South University, China. The authors would like to thank Prof. Bo Sundman from INSTN, CEA Saclay, France for helpful discussion on Curie temperatures.

## Appendix A. Supplementary material

Supplementary data associated with this article can be found in the online version at http://dx.doi.org/10.1016/j.calphad.2015.06.001.

## References

[1] H.M. Tawancy, N.M. Abbas, A. Bennett, Role of Y during high temperature oxidation of an M-Cr-Al-Y coating on an Ni-based superalloy, Surf. Coat. Technol. 10 (1994) 68-69.

[2] J.L. He, C.H. Yu, A. Leyland, A.D. Wilson, A. Matthews, A comparative study of the cyclic thermal oxidation of PVD nickel aluminide coatings, Surf. Coat. Technol. 155 (1) (2002) 67-79.

[3] W.Y. Gong, L.J. Zhang, D.Z. Yao, C.G. Zhou, Diffusivities and atomic mobilities in fcc Ni-Pt alloys, Scr. Mater. 61 (2009) 100-103.

[4] M.S.A. Karunaratne, P. Carter, R.C. Reed, Interdiffusion in the face-centred cubic phase of the Ni-Re, Ni-Ta and Ni-W systems between 900 and 1300 °C, Mater. Sci. Eng. A 281 (2000) 229-233.

[5] C.L. Zacherl, A Computational Investigation of the Effect of Alloying Elements on the Thermodynamic and Diffusion Properties of fcc Ni Alloys, with Appli- cation to the Creep Rate of Dilute Ni-X Alloys (Doctoral thesis), Pennsylvania State University, 2012.

[6] M.J.H. Vandal, M.C.L.P. Pleumeekers, A.A. Kodentsov, F.J.J. Vanloo, Intrinsic diffusion and kirkendall effect in Ni-Pd and Fe-Pd solid solutions, Acta Mater. 48 (2000) 385-396.

[7] E. Mabruri, S. Sakurai, Y. Murata, T. Koyama, M. Morinaga, Diffusion and $\gamma'$ phase coarsening kinetics in ruthenium containing nickel based alloys, Mater. Trans. 49 (4) (2008) 792-799.

[8] R.A. Hobbsa, M.S.A. Karunaratne, S. Tina, R.C. Reed, C.M.F. Rae, Uphill diffusion in ternary Ni-Re-Ru alloys at 1000 and 1100 °C, Mater. Sci. Eng. A 460-461 (2007) 587-594.

[9] Y.M. Youssef, P.D. Lee, K.C. Mills, R.C. Reed, On the diffusion behaviour of Os in the binary Ni-Os system, Mater. Sci. Technol. 26 (2010) 1173-1176.

[10] W. Köster, E. Horn, Festschrift aus Anlass des 100-jahrigen Jubilaums der Firma, W.C. Heraeus GmbH, Hanau, 1951, 114-123.

[11] A.A. Samadi, M. Fedoroff, Measurement of the partition coefficient of Ir, Os, and Ru between solid and liquid nickel by zone refining, Scr. Metall. 11 (6) (1977) 599-612.

[12] T.Ya Velikanova, T.G. Mazhuga, O.L. Semenova, P.S. Martsenyuk, V. M. Vereshchaka, Phase diagram of the Ni-Os system, Powder Metall. Met. Ceram. 41 (2002) 5-6.

[13] W.L. Phillips Jr., Mechanical properties of several nickel-platinum group metal alloys, Trans. Metall. Soc. AIME 230 (1964) 526-529.

[14] J. Prigent, J.-M. Joubert, The phase diagrams of the ternary systems La-Ni-M (M=Re, Ru, Os, Rh, Ir, Pd, Ag, Au) in the La-poor region, Intermetallics 19 (2011) 295-301.

[15] J. Crangle, D. Parsons, The magnetization of ferromagnetic binary alloys of cobalt or nickel with elements of the palladium and platinum group, Proc. R. Soc. A 255 (1960) 509-519.

[16] A.T. Dinsdale, SGTE data for pure elements, CALPHAD 15 (4) (1991) 317-425.

[17] M. Hillert, M. Jarl, A model for alloying effects in ferromagnetic metals, CAL- PHAD 2 (1978) 227-238.

[18] L.J. Zhang, Y. Du, H.H. Xu, Z. Pan, Experimental investigation and thermo- dynamic description of the Co-Si system, CALPHAD 30 (2006) 470-481.

[19] J.O. Andersson, J. Ågren, Models for numerical treatment of multicomponent diffusion in simple phases, J. Appl. Phys. 72 (1992) 1350-1355.

[20] B. Jönsson, Ferromagnetic ordering and diffusion of carbon and nitrogen in bcc Cr-Fe-Ni alloys, Z. Metallkd. 85 (7) (1994) 498-501.

[21] L.S. Darken, Diffusion mobility and their interrelation through free energy in binary metallic systems, Trans. AIME 175 (1948) 184-201.

[22] T. Angsten, T. Mayeshiba, H. Wu, D. Morgan, Elemental vacancy diffusion da- tabase from high-throughput first-principles calculations for fcc and hcp structures, New J. Phys. 16 (2014) 015018.

[23] L.J. Zhang, W.Y. Gong, J. Chen, Y. Du, Diffusivities and atomic mobilities in fcc Pt-Al alloys, CALPHAD 46 (2014) 118-123.

[24] J. Askill, Tracer Diffusion Data for Metals, Alloys and Simple Oxides, IFI/Ple- num, New York (1970), p. 19-26.

[25] S. Dushman, I. Langmuir, The diffusion coefficient in solids and its tempera- ture coefficient, Phys. Rev. 20 (1922) 113-117.

[26] P. Nash, Ni-Os (Nickel-Osmium), Phase Diagrams of Binary Nickel Alloys, 1991, 233-234.

[27] L.J. Zhang, Y. Du, Q. Chen, I. Steinbach, Atomic mobilities and diffusivities in the fcc, L12 and B2 phases of the Ni-Al system, Int. J. Mater. Res. 101 (2010) 1461-1475.

[28] H.W. King, Crystal structure of the elements at 25 °C, Bull. Alloy Phase Diagr. 2 (3) (1981) 401-402.

[29] B. Jansson, Computer Operated Methods for Equilibrium Calculations and Evaluation of Thermodynamic Model Parameters (Doctoral thesis), Royal In- stitute of Technology, 1984.

[30] B. Sundman, B. Jansson, J.O. Andersson, The Thermo-Calc databank system, CALPHAD 9 (1985) 153-199.

[31] J. Wang, S.L. Shang, Y. Wang, Z.G. Mei, Y.F. Liang, Y. Du, Z.K. Liu, First-principles calculations of binary Al compounds: enthalpies of formation and elastic properties, CALPHAD 35 (2011) 562-573.

[32] Y. Wang, S. Curtarolo, C. Jiang, R. Arroyave, T. Wang, G. Ceder, L.Q. Chen, Z. K. Liu, Ab initio lattice stability in comparison with CALPHAD lattice stability, CALPHAD 28 (2004) 79-90.