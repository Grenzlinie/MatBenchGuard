# Soft Matter

**PAPER**

View Article Online
View Journal

![](./images/812701268244955137_1.jpg)

Cite this: DOI: 10.1039/c9sm02022e

Received 10th October 2019,
Accepted 13th December 2019

DOI: 10.1039/c9sm02022e

rsc.li/soft-matter-journal

## Stability dependence of local structural heterogeneities of stable amorphous solids

Alireza Shakerpoor, Elijah Flenner* and Grzegorz Szamel

The universal anomalous vibrational and thermal properties of amorphous solids are believed to be related to the local variations of the elasticity. Recently it has been shown that the vibrational properties are sensitive to the glass's stability. Here we study the stability dependence of the local elastic constants of a simulated glass former over a broad range of stabilities, from a poorly annealed glass to a glass whose stability is comparable to laboratory exceptionally stable vapor deposited glasses. We show that with increasing stability the glass becomes more uniform as evidenced by a smaller variance of local elastic constants. We find that, according to the definition of local elastic moduli used in this work, the local elastic moduli are not spatially correlated.

## 1 Introduction

The vibrational modes and the low temperature thermal properties of amorphous solids are sharply different from those of their crystalline counterparts. $^{1-4}$ The uniform structure of crystals allows for the description of the low frequency modes as if it were a classical elastic body whose properties are governed by the elastic moduli, which forms the basis of the Debye model for the density of states. This description leads a $T^{3}$ increase of the specific heat for crystalline solids due to the increase of the density of the vibrational modes as the square of the frequency $\omega$. Recently it was shown that the low frequency vibrational modes of amorphous solids can be divided into a Debye term and an excess contribution that increases as the fourth power of the frequency. $^{5,6}$ The excess modes are spatially quasi-localized. Their spatial extent and density decrease with increasing stability. The quasi-localized character of excess modes suggests that there might be a spatially varying local elasticity.

Indeed, there is a large body of evidence for the existence of spatially varying local elastic constants in amorphous solids. $^{7-19}$ To explain a plateau observed in the thermal conductivity around 10 K for many dielectric amorphous solids, a Rayleigh like scattering of sound waves was assumed. $^{1,4}$ This assumption posits scattering from uncorrelated defects that are much smaller than the wavelength of the sound wave, and these defects would naturally give rise to local variations of the elasticity. Further theoretical analysis assuming local variations of the elasticity reproduces the $\omega^{4}$ excess in the vibrational density of states and predicts the Rayleigh scaling $k^{4}$ (where $k$ is a wavevector) of sound attenuation. $^{6,20-22}$ The $k^{4}$ scaling of sound attenuation was questioned in a computer simulation study $^{13}$ and a logarithmic correction to the Rayleigh scaling was proposed. This correction was rationalized in terms of a power law decay of the spatial correlations of the local elasticity. However, other simulation studies $^{6,22,23}$ suggest that the logarithmic correction either exists only for a narrow range of wavevectors (frequencies) or this correction is only a good description of the crossover region between the high and low wavevector (frequency) behavior of sound attenuation.

Pogna et al. $^{19}$ examined sound attenuation in geologically hyperaged, ultrastable amber within the framework of fluctuating elasticity theory to establish a link between stability and the local variation of the elastic constants. They fitted the predictions of the theory for the vibrational density of states to the experimental data and in this way obtained estimates of the relative variance of the local elastic constants and of a length scale characterizing their spatial variation. They concluded that there was a reduction in the variation of the elastic constants by around 6% and an increase of the characteristic length scale of around 22% in the hyperaged amber compared to a liquid cooled sample. Thus, increasing stability seemingly narrows the distribution of elastic constants and increases the range of their correlations.

However, in a very recent simulational study Caroli and Lemaître $^{14}$ argued that the fluctuating elasticity theory does not describe well sound attenuation in amorphous solids. They based this conclusion on two results. First, they showed that the fluctuating elasticity theory predicts the $k^{4}$ Rayleigh scattering-like sound damping whereas their simulations were consistent with a logarithmic correction. Second, they measured the parameters that enter into the fluctuating elasticity theory in simulations, used them to calculate sound attenuation, and compared these predictions with sound attenuation observed in the same simulations. They found that the predicted sound attenuation is two orders of magnitude smaller than the observed one. The second fact implies that the

Department of Chemistry, Colorado State University, Fort Collins, Colorado 80523,
USA. E-mail: flennere@gmail.com

This journal is © The Royal Society of Chemistry 2019
Soft Matter

fluctuating elasticity theory severely underestimates the mag- nitude of the sound attenuation even if one were to argue that the logarithmic correction is an intermediate, finite wavevector feature and the sound attenuation can be described within the Rayleigh scattering picture.

We note that it is difficult to directly probe local variations of the elasticity in experiments, $^{17}$ which forced Pogna et al. to treat the relative variance of the local shear modulus as a fitting parameter. In contrast, simulations are able to calculate local elastic constant using several different methods. $^{7,13,22}$ Lerner demonstrated that the sample to sample fluctuations of the shear modulus decreased with increasing stability for a model glass former, $^{24}$ but did not examine the local elastic constants. Mizuno, Mossa, and Barrat found that the width of the distribution of local elastic constant correlates with sound attenuation. $^{12}$ For their study, they continu ously transformed a crystal into an amorphous solid by continuously changing the size ratio of a binary mixture. Using the same technique they also demonstrated that the thermal conductivity, the lifetime of acoustic modes, and the local elastic heterogeneity are correlated. $^{8}$ This investigation, however, does not mimic the experi mental procedure of Pogna et al. $^{19}$ who studied the stability dependence of sound attenuation. Importantly, in the work of Mizuno, Mossa, and Barrat the system is changed systematically in order to establish the correlations between the transport and acoustic properties and the variation of local elastic constants.

Here we examine the dependence of local elastic moduli of a simulated polydisperse glass former on its stability. We partition the system into different box sizes $w$ and determine the distribution of local elastic moduli for four values of $w$. We find that the width of the distribution decreases with increasing stability. However, using our definition of the local elastic moduli, we find that the local elastic moduli are uncorrelated in space.

## 2 Methods

### 2.1 Molecular dynamics simulations

We studied a system of $N=48000$ and $N=192000$ polydisperse repulsive particles in a cubic box of volume $V$ with periodic boundaries in 3D. The pair potential is given by

$$
U\left(r_{i j}\right)= \begin{cases}\varepsilon\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{12}+v\left(r_{i j}\right), & \frac{\sigma_{i j}}{r_{i j}}<r_{\mathrm{cut}} \\ 0, & \frac{\sigma_{i j}}{r_{i j}} \geq r_{\mathrm{cut}}\end{cases}
\tag{1}
$$

with

$$
v\left(r_{i j}\right)=c_{0}+c_{2}\left(\frac{r_{i j}}{\sigma_{i j}}\right)^{2}+c_{4}\left(\frac{r_{i j}}{\sigma_{i j}}\right)^{4}.
\tag{2}
$$

The distance between particle $i$ and particle $j$ is $r_{i j}=|\mathbf{r}_{i}-\mathbf{r}_{j}|$,
$\sigma_{i j}=\frac{\sigma_{i}+\sigma_{j}}{2}(1-e|\sigma_{i}-\sigma_{j}|)$ where the mixing parameter $e=0.2.^{6,25}$ The size of an individual particle $\sigma$ is given by the probability distribution

$$
P(\sigma)=\frac{A}{\sigma^{3}}
\tag{3}
$$

where $\sigma \in[0.73,1.63]$ and zero otherwise. The coefficients $c_{0}, c_{2}$, and $c_{4}$ are chosen to guarantee the continuity of the potential up to the second derivative at the cutoff distance $r_{\text {cut }}=1.25$. This choice of system inhibits crystallization due to the poly- dispersity and fractionation due to the non-additive mixing rule, while allowing the swap Monte Carlo algorithm to equilibrate to low temperatures. $^{25}$ We present the results in reduced units with $\varepsilon$ being our unit of energy, the average of $\sigma=\sigma_{0}$ being our unit of length, and $\sqrt{m \sigma_{0}^{2} / \varepsilon}$ being the unit of time.

For each parent temperature $T_{\mathrm{p}} \in[0.062,0.200]$ we studied 4 independent initial configurations at number density $\rho=1$. Each configuration was first equilibrated at its parent temperature and then quenched to an inherent structure via the conjugate gradient algorithm. For reference, for our system the mode- coupling temperature $T_{\mathrm{MCT}} \approx 0.108$ and the glass transition temperature $T_{\mathrm{g}} \approx 0.072.^{25}$ The equilibration was done using the swap Monte Carlo algorithm that combines conventional MonteCarlo moves with particle swaps. $^{25-27}$

After quenching, we ran very low temperature $N V T$ molec ular dynamics simulations using LAMMPS $^{28,29}$ code to which we added the interaction potential for the present model. The time step for all of MD simulations was $\mathrm{d} t=0.02$. We first ran short equilibration runs at $T=10^{-5}$ in an $N V T$ ensemble using a Nosé-Hoover thermostat. We then ran $N V T$ production runs. Their length was determined by the time needed for to decorr- elate a term involving the local and global stress $\langle\sigma_{\alpha \beta}^{m} \sigma_{\gamma \delta}\rangle$, which was identified as a slowly decorrelating term and discussed by Mizuno et al. $^{7}$ This term is defined in Section 2.2. We did not observe any finite size effects, but, consistently with the obser- vation made in ref. 7, much longer production runs are needed for larger systems. For a system of $N=48000$ particles, which was mainly used to perform the elastic modulus calculations in this study, the length of the production runs time was $\Delta t=3 \times 10^{5}$, which corresponds to $1.5 \times 10^{7}$ time steps. The results shown in the paper are for the $N=48000$ particle system unless otherwise specified. We observed very infrequent jumps in the energy and the pressure even at the very low temperature that we used, $T=10^{-5}$. We attribute these jumps to transitions between the locally stable minima. In the analysis we only use a continuous portion of the trajectory that excludes the energy jumps.

### 2.2 Elastic modulus calculations

To measure the local elastic response, the system is equally partitioned into cells of size $w=3.30,4.54,6.05$, and 12.11. Several methods have been proposed to define and calculate the local elastic constants. Here we use the so-called "fully local" approach described by Mizuno, Mossa, and Barrat. $^{7}$ This approach was also used in other studies. $^{8,12,16}$ For each box $m$ the volume averaged stress tensor is calculated as:

$$
\sigma_{\alpha \beta}^{m}=-\rho^{m} T \delta_{\alpha \beta}+\frac{1}{w^{3}} \sum_{i<j} \frac{\partial U\left(r^{i j}\right)}{\partial r^{i j}} \frac{r_{\alpha}^{i j} r_{\beta}^{i j}}{r^{i j}} \frac{q_{m}^{i j}}{r^{i j}}
\tag{4}
$$

where, $\rho^{\mathrm{m}}$ is the local number density of cell $\mathrm{m}, T$ is the temperature, $\delta$ is the Kronecker delta and $r_{i j}=|\mathbf{r}_{i}-\mathbf{r}_{j}|$.

The parameter $q_{m}^{ij}$ is the segment of the line joining $\mathbf{r}_{i}$ and $\mathbf{r}_{j}$ that lies within the box $m$. We use Greek subscripts to denote the Cartesian coordinates $(\alpha,\beta,\gamma,\delta = x,y,z)$ and Roman superscripts to denote particle labels. The global stress tensor is given by:

$$
\sigma_{\alpha \beta}=\frac{1}{V} \sum_{m} w^{3} \sigma_{\alpha \beta}^{m}=-\hat{\rho} T \delta_{\alpha \beta}+\frac{1}{V} \sum_{i<j} \frac{\partial U\left(r^{i j}\right)}{\partial r^{i j}} \frac{r_{\alpha}^{i j} r_{\beta}^{i j}}{r^{i j}}. \tag{5}
$$

We first calculate the local modulus $C_{\alpha \beta \gamma \delta}^{m}$ given by

$$
\begin{aligned}
C_{\alpha \beta \gamma \delta}^{m} &=C_{\alpha \beta \gamma \delta}^{A m}-C_{\alpha \beta \gamma \delta}^{N m} \\
&=C_{\alpha \beta \gamma \delta}^{B m}+C_{\alpha \beta \gamma \delta}^{C m}+C_{\alpha \beta \gamma \delta}^{K m}-C_{\alpha \beta \gamma \delta}^{N m} \\
C_{\alpha \beta \gamma \delta}^{B m} &=\frac{1}{w^{3}}\left\langle\sum_{i<j}\left(\frac{\partial^{2} U}{\partial r^{i j^{2}}}-\frac{1}{r^{i j}} \frac{\partial U}{\partial r^{i j}}\right) \frac{r_{\alpha}^{i j} r_{\beta}^{i j} r_{\gamma}^{i j} r_{\delta}^{i j}}{r^{i j^{2}}} \frac{q_{m}^{i j}}{r^{i j}}\right\rangle \\
C_{\alpha \beta \gamma \delta}^{C m} &=-\frac{1}{2}\left[2\left\langle\sigma_{\alpha \beta}^{m}\right\rangle \delta_{\gamma \delta}-\left\langle\sigma_{\alpha \gamma}^{m}\right\rangle \delta_{\beta \delta}\right. \\
&\quad\left.-\left\langle\sigma_{\alpha \delta}^{m}\right\rangle \delta_{\beta \gamma}-\left\langle\sigma_{\beta \gamma}^{m}\right\rangle \delta_{\alpha \delta}-\left\langle\sigma_{\beta \delta}^{m}\right\rangle \delta_{\alpha \gamma}\right] \\
C_{\alpha \beta \gamma \delta}^{K m} &=2\left\langle\hat{\rho}^{m}\right\rangle T\left(\delta_{\alpha \gamma} \delta_{\beta \delta}+\delta_{\alpha \delta} \delta_{\beta \gamma}\right) \\
C_{\alpha \beta \gamma \delta}^{N m} &=\frac{V}{T}\left(\left\langle\sigma_{\alpha \beta}^{m} \sigma_{\gamma \delta}^{m}\right\rangle-\left\langle\sigma_{\alpha \beta}^{m}\right\rangle\left\langle\sigma_{\gamma \delta}^{m}\right\rangle\right),
\end{aligned} \tag{6}
$$

where $C_{\alpha \beta \gamma \delta}^{A m}$ is the affine contribution and $C_{\alpha \beta \gamma \delta}^{N m}$ is the non-affine contribution. While the non-affine contribution vanishes in perfect crystalline systems at zero temperature, it has a magnitude comparable to the affine term in amorphous systems. $^{30}$ The brackets $\langle\cdots\rangle$ denotes an ensemble average. The Born contribution $C_{\alpha \beta \gamma \delta}^{B m}$ to the affine term stems from the uniform displacement of all particles and it determines the instantaneous elastic modulus under such displacements. $^{9}$ The $C_{\alpha \beta \gamma \delta}^{C m}$ term is due to the initial stress having a finite value. $^{7}$ The $C_{\alpha \beta \gamma \delta}^{K m}$ term is the kinetic energy contribution to the local elastic modulus tensor. Compared to the Born and the non-affine terms, the kinetic energy contribution to the elastic constant is negligible.

As described by Mizuno et al., $^{7}$ the local bulk modulus $K^{m}$ is defined from the pressure-volume change and the five shear moduli $G_{1}^{m}, \ldots, G_{5}^{m}$, are defined from two pure shear and three simple shear deformations. These moduli are given by the following linear combinations of $C_{\alpha \beta \gamma \delta}^{m}$

$$
\begin{aligned}
K^{m} &=\left(C_{x x x x}^{m}+C_{y y y y}^{m}+C_{z z z z}^{m}+C_{x x y y}^{m}+C_{y y x x}^{m}+C_{x x z z}^{m}+C_{z z x x}^{m}+C_{y y z z}^{m}+C_{z z y y}^{m}\right) / 9 \\
G_{1}^{m} &=\left(C_{x x x x}^{m}+C_{y y y y}^{m}-C_{x x y y}^{m}-C_{y y x x}^{m}\right) / 4 \\
G_{2}^{m} &=\left[C_{x x x x}^{m}+C_{y y y y}^{m}+4 C_{z z z z}^{m}+C_{x x y y}^{m}+C_{y y x x}^{m}-2\left(C_{x x z z}^{m}+C_{z z x x}^{m}+C_{y y z z}^{m}+C_{z z y y}^{m}\right)\right] / 12 \\
G_{3}^{m} &=C_{x y x y}^{m} \\
G_{4}^{m} &=C_{x z x z}^{m} \\
G_{5}^{m} &=C_{y z y z}^{m}.
\end{aligned} \tag{7}
$$

The moduli are averaged over MD configurations that are separated by $t=0.5$, i.e. over $6 \times 10^{5}$ time steps.

## 3 Results

Shear and bulk moduli describe the elastic response of the system to a small deformation. In simulations one can determine these moduli through a deformation, or utilize the thermodynamic equations summarized in eqn (6) and (7) for the whole system, i.e. when the system is only partitioned into one box. Here, we partition the system into several boxes and determine distributions of the moduli. We expect that the averages of these distributions should be equal to the values of the moduli obtained from deformation. To check this, we calculated the averages of the moduli for different box sizes $w$ and compared these results to the shear and bulk moduli obtained from deformation.

Shown in Fig. 1 are the shear modulus (left axis) and the bulk modulus (right axis) obtained from deforming the system (lines) and from the averages of the distributions of the local moduli (symbols) for different box sizes. Up to the mode

![](./images/812701268244955137_2.jpg)

Fig. 1 Macroscopic shear (red line) and bulk (black line) moduli obtained by deforming the zero temperature (quenched) configurations as functions of the parent temperature. The symbols show the averages of the local shear and bulk moduli for different box sizes. The errorbars for the local moduli averages, not shown here, are smaller than or comparable to the size of the symbols.

![](./images/812701268244955137_3.jpg)

Fig. 2 The dependence of the Born and fluctuation terms on the parent temperature. Inset: Rescaled data for the bulk fluctuation term. Both Born and fluctuation terms decrease with decreasing parent temperature, for both shear (a) and bulk (b) moduli.

coupling temperature $T_{\mathrm{MCT}}$ the global shear modulus $G$ changes very little with decreasing parent temperature $T_{\mathrm{p}}$. Below $T_{\mathrm{MCT}}$ it increases with decreasing $T_{\mathrm{p}}$, reaching a value approximately $27\%$ larger at the lowest parent temperature used. In contrast, the global bulk modulus $K$ monotonically decreases with decreasing $T_{\mathrm{p}}$, reaching a value $7\%$ smaller at the lowest parent temperature than at $T_{\mathrm{MCT}}$. The averages of the local shear $G^{\mathrm{m}}$ and bulk $K^{\mathrm{m}}$ moduli for different box sizes are very close to the moduli obtained from deformation. We do find, however, that at the largest parent temperature the averages of the shear moduli are slightly larger than the value obtained from deformation, with the difference increasing systematically with decreasing box size.

We note that, as shown in Fig. 2, for both of the global shear and the global bulk moduli the Born and fluctuation terms in $C_{\alpha\beta\gamma\delta}$ decrease with decreasing $T_{\mathrm{p}}$. For the shear modulus, the fluctuation term decreases faster with decreasing $T_{\mathrm{p}}$ than the Born term, and this leads to the increase in the shear modulus since the two terms are the same order of magnitude. However, for the bulk modulus the fluctuation term is an order of magnitude smaller than the Born term, and thus a decrease in the Born term leads to a decrease of the bulk modulus.

Although the average shear and bulk moduli are approxi- mately independent of the box width $w$, one would expect to find some box width dependence of the width of the moduli distributions. The dependence of the width of the distribution relative on the box size is an important parameter in the fluctuating elasticity theory. Mizuno *et al.* found that the distributions of the individual shear moduli are almost identical and presented distributions averaged over the indivi- dual components. We found that the same fact is true for our system and also present distributions of the shear moduli averaged over the individual components.

Shown in Fig. 3 are probability distributions of the local shear modulus $G^{\mathrm{m}}$ calculated for (a) $w=12.114$, (b) $w=6.057$, (c) $w=4.543$, and (d) $w=3.303$ for three parent temperatures $T_{\mathrm{p}}=0.062$ (circles), $0.085$ (squares), and $0.2$ (triangles). We note that we observe no finite size effects, which we demonstrate in the inset to Fig. 3(d) by calculating the distribution for $N=48000$ and $N=192000$ for a box of the same size. However, as discussed in ref. 7, the $\langle\sigma_{\alpha\beta\sigma_{\gamma\delta}}^{\mathrm{m}}\rangle$ term converges very slowly for large systems. To characterize the width we fit the distributions to a Gaussian distribution, $A\exp\{-0.5(G-G_{0})^{2}/\sigma^{2}\}$, where $G_{0}$ is the average shear modulus and $\sigma$ is the standard deviation. The fits are shown as continuous lines in the figures. For all box sizes, including the smallest one with $w=3.303$ that only contains $\simeq36$ particles, the shear moduli distributions are well described by Gaussian distributions.

![](./images/812701268244955137_4.jpg)

Fig. 3 Distributions of local shear moduli for different box sizes: (a) $w=$ 12.114, (b) $w=6.057$, (c) $w=4.542$, (d) $w=3.303$. Each panel shows distributions for three different parent temperature, circles, $T_{\mathrm{p}}=0.062$, squares, $T_{\mathrm{p}}=0.085$ and triangles $T_{\mathrm{p}}=0.200$. The solid lines show Gaussian fits to the distributions.

We can see two trends. First, with increasing stability the distribution becomes narrower. This is easily seen since the peak of the distribution increases with decreasing width due to normalization of the distributions. Therefore, with increasing stability the glass becomes more uniform, in the sense that the local shear moduli vary less between different boxes. The other trend is that the width becomes broader with decreasing box size. This result is intuitively expected.

One noticeable property of some of these distributions is the appearance of regions with negative moduli. The regions with negative moduli are characterized as domains where the deforming force and the resulting response are in opposite directions, $^{31}$ which suggests that these domains are unstable. However, with such small domains it is questionable if continuum elasticity is a valid description. $^{30}$ Overall, at each box size the distributions with higher averages and smaller standard

![](./images/812701268244955137_5.jpg)

Fig. 4 Distributions of local bulk moduli for different box sizes: (a) $w =$ 12.114, (b) $w =$ 6.057, (c) $w =$ 4.542, (d) $w =$ 3.303. Each panel shows distributions for three different parent temperature, circles, $T_{\rm p} = 0.062$, squares, $T_{\rm p} = 0.085$ and triangles $T_{\rm p} = 0.200$. The solid lines show Gaussian fits to the distributions.

deviations (i.e. the distributions of $T_{\rm p} = 0.062$) represent the more stable structure.$^{15}$

We also examined the distribution of the bulk modulus $K^{\rm m}$, Fig. 4 for the same three parent temperature $T_{\rm p}$ and box sizes $w$. We also find that the width of the distribution of $K^{\rm m}$ decreases with decreasing parent temperature and increases with decreasing box size. The lines in the figures are fits to a Gaussian distribution. Again, these results points to the bulk modulus becoming more uniform with an increase of the stability. Since the bulk modulus is 3.5 to 5.5 times larger than the shear modulus (depending on stability), the change in the relative size of the distribution $\sigma_{\Gamma}/\Gamma$, where $\Gamma = G$ or $K$ is much less for the bulk modulus.

We summarize the parent temperature and box size dependence of the standard deviation of the distributions of the local moduli in Fig. 5. The closed symbols are the results for the shear moduli and the open symbols are results for the bulk modulus. The increase in $\sigma_{G^m}$ upon decreasing the box of size from $w = 12.114$ to $w = 3.303$ is a factor of 5.5 for $T_{\rm p} = 0.2$ and 5.8 for $T_{\rm p} = 0.062$. Similarly, the decrease of $\sigma_{G^m}$ with parent temperature for a fixed box size is 31% for $w = 12.114$ and 35% for $w = 3.303$.

Within fluctuating elasticity theory,$^{20,32,33}$ the heterogeneity of local shear modulus is characterized by the disorder parameter $\gamma_{\rm G}$, $\gamma_{\rm G} = \rho w^3 \sigma_{G^m}{}^2/\langle G^m \rangle{}^2$. We calculated this parameter for the different box sizes. We found that the disorder parameter varies with box size. For our most stable glass, $T_{\rm p} = 0.062$, $\gamma_{\rm G} = 1.24$ for $w = 12.1$ and $\gamma_{\rm G} = 0.90$ for $w = 3.3$. These two values of the disorder parameters differ by approximately 38%. This box size dependence of the disorder parameter originates from slower than $w^{-3}$ decay of the variance $\sigma_{G^m}{}^2$ upon increasing the box size $w$. It makes it unclear if $\gamma_{\rm G}$ is a proper parameter to be used as input to a theory of sound attenuation in glasses. We note that Lerner$^{24}$ found that a quantity which should be equivalent to the square root of the variance (see eqn (18) of ref. 24) of the sample-to-sample fluctuations of the shear modulus decreases with the size of the system as $N^{-1/2}$. The difference between our results and those of ref. 24 suggests that the distribution of local shear modulus calculated for a given sample might be different from the distribution of sample-to-sample fluctuations of the shear modulus calculated for the whole system.

![](./images/812701268244955137_6.jpg)

Fig. 5 Dependence of the standard deviation of the local shear, $\sigma_{G^m}$, and bulk moduli, $\sigma_{K^m}$, on the parent temperature. The solid lines and filled symbols show $\sigma_{G^m}$ and the dashed lines and open symbols show $\sigma_{K^m}$. The standard deviation $\sigma_{G^m}$ increases by 67% for our smallest box size $w = 3.303$ and 50% for our largest box size $w = 12.114$. The standard deviation $\sigma_{K^m}$ increases by 33% for our smallest box size and 7.1% for our largest box size. Since $K > G$, this signifies a much larger relative change in $\sigma_{G^m}$ than $\sigma_{K^m}$.

The disorder parameter does increase dramatically with decreasing stability for a fixed box size. The disorder parameter increases by a factor of 3.4–3.9, depending on box size, when we compare our most stable glass, $T_{\rm p} = 0.062$, to our least stable glass, $T_{\rm p} = 0.2$. For our least stable glass, disorder parameters are of similar magnitude as those found by Mizuno, Ruocco, and Mossa$^{34}$ in their $T = 0$ glass.

We note that the change in the variation of the local elastic moduli, i.e. of the heterogeneity of the local elasticity, with the changing stability found in this work is much larger than that estimated by Pogna *et al.* for hyperaged amber. In the latter study a decrease of only 5% was estimated upon a very large increase in the stability. We note that the change in the variation of the elastic constants reported by Pogna *et al.* was obtained indirectly, by fitting measured vibrational densities of states to the predictions of the fluctuating elasticity theory. Thus, the accuracy of their inferred change of the variation of the local elastic moduli depends on accuracy of the fluctuating elasticity model that they used. We find that there is probably a

![](./images/812701268244955137_7.jpg)

Fig. 6 Panel (a) shows the spatial correlations of the shear modulus G for a 3000 particle system and for our most stable glass, $T_p$ = 0.062. The vertical lines indicate the box sizes. At these points the trivial correlations disappear. Panel (b) illustrates the correlation parameter $\Psi_G^{m,n}$ (circles) and $\Psi_K^{m,n}$ (squares) for the box sizes w = 6.075 (black), 4.542 (red), and 3.028 (blue) as a function of parent temperature (N = 48 000). The correlation parameter is small and there is no clear box size or parent temperature dependence.

stronger dependence of the variation of the elastic constants on the glass' stability than that inferred from fluctuating elasticity theory.

To characterize the spatial correlations of local shear moduli, which also enter into the fluctuating elasticity theory,²¹ we calculated the correlation function

$$
g_{\mathrm{GG}}(r)=\sum_{m} \sum_{n}\left(\left\langle G^{m} G^{n}\right\rangle-\left\langle G^{m}\right\rangle\left\langle G^{n}\right\rangle\right) \delta\left(r-\left|\mathbf{r}_{m}-\mathbf{r}_{n}\right|\right), \quad (8)
$$

where $\mathbf{r}_{n}$ is the coordinate for the center of a box used to calculate the elastic moduli. We used 3000 particle systems to calculate $g_{\mathrm{GG}}(r)$ and checked that the calculation was consistent with results for 48 000 particle systems. It is important to recognize the fact that the boxes used in this calculation may overlap (in order to get results for distances r smaller than the box size). Thus, boxes may share some of the same particles and their elastic moduli are necessarily correlated. Therefore, there are trivial correlations in $g_{\mathrm{GG}}(r)$ due to overlapping boxes. We show $g_{\mathrm{GG}}(r)$ for our most stable glass, $T_p$ = 0.062, for four different box sizes w. We find that $g_{\mathrm{GG}}(r)$ decays to near zero at the size of the box, which is indicated by the vertical lines in the figure. This implies that only the trivial correlations exist.

To explore further if there are spatial correlations for the shear modulus and the bulk modulus at every temperature and every box size, we calculate the cross correlations of neighboring non-overlapping boxes. To this end we calculate the correlation parameter

$$
\Psi_{\Gamma}^{m, n}=\left\langle\left(\frac{\Gamma^{m}-\Gamma}{\sigma_{\Gamma^{m}}}\right)\left(\frac{\Gamma^{n}-\Gamma}{\sigma_{\Gamma^{n}}}\right)\right\rangle_{m} \quad (9)
$$

where, $\langle\cdots\rangle_{m}$ denotes an average over all the boxes and box n is one of the six nearest neighbors of box m and $\Gamma=G$ or $K$. A correlation parameter close to 0 indicates no significant correlation and a value of 1 indicates perfect correlation. In Fig. 6(b) we show $\Psi_G$ (circles) and $\Psi_K$ (squares) for box sizes of w = 6.075 (black), 4.542 (red), and 3.028 (blue). The values of $\Psi_\Gamma$ are all close to zero and there are no noticeable trends with box size or parent temperature. This leads us to conclude that the elastic moduli, calculated using this fully local approach, do not exhibit any spatial correlations. We also examined correlations of $G_n^m$ where $n=1...5$ found in eqn (7) and found the same trends, i.e. only trivial correlations. We note that there are other methods to calculate local elastic moduli,⁷ and these other methods may indicate that the moduli are spatially correlated.

This conclusion is at odds with the result of Gelin et al.¹³ who reported that the elastic correlations decayed as $r^{-2}$ for a two dimensional glass-forming system different from the system used here. We note that Gelin et al. used a different way to define local elastic moduli. However, Mizuno and Ikeda²² utilized the same method as Gelin et al. for yet another, different two dimensional system and found that the stress correlations decay as $r^{-2}$, but the elastic moduli correlations does not show the same long range correlations.

## 4 Conclusions

We examined the structural heterogeneities, including local and global elastic moduli, of glassy systems prepared from parent systems equilibrated at different initial temperatures. Our calculations showed that the glass has a rather mild 27% increase of the local shear modulus, and a smaller 7% decrease on local bulk modulus compared to their values at the mode-coupling temperature with decreasing parent temperature. More importantly, we found that the local shear and the local bulk moduli become more uniform with decreasing parent temperature and thus stability of the glass. This finding is consistent with the recent report on the stability and sound attenuation of stable glasses.³⁵ Sound attenuation increases with an increase in the fluctuations of the local elasticity, and hence with a decrease of the stability. Our results are in qualitative agreement with fluctuating elasticity theory,²⁰,³²,³³ which predicts an increase of sound attenuation and the observed Rayleigh-like $k^4$ scaling for small wavevectors.²²,³⁵

Our results are also qualitatively consistent with recent experimental work by Pogna et al. on hyperaged amber,¹⁹ which

showed that the elastic matrix becomes more homogeneous with increased stability, corresponding to a smaller $T_p$ and a narrower moduli distribution in our study. However, we find that the local moduli are not spatially correlated. Pogna *et al.* inferred a 22% increase in the length scale characterizing elastic correlations. The same work reported on an increase of the elastic moduli fluctuation length scale in the more stable amorphous medium. This result, however, remains at variance with the findings of our study, where there is no discernible length scale associated with elasticity and there is no long range decay of elastic correlations. The lack of long range decay is also at odds with the study of Gelin *et al.*,¹³ but agrees with the conclusions of Mizuno and Ikeda.²²

Our results suggest that the current version of fluctuating elasticity theory is not a quantitatively accurate description of sound attenuation and the boson peak in amorphous solids, even though it makes qualitatively accurate predictions. A similar conclusion was drawn by Caroli and Lemaître,¹⁴ who developed a full tensorial fluctuating elasticity theory and found that it underestimates the sound attenuation by about two orders of magnitude. Further theoretical work is warranted to properly describe the interplay of sound attenuation and elastic hetero- geneities. Additionally, Mizuno and Ikeda found that elastic moduli correlations may be system dependent.²² Therefore, different systems should be examined to establish the universality of the results reported here and in other papers. In particular, we note that the polydisperse system studied here is designed to suppress crystallization, and hence some fluctuations may be suppressed compared to more standard binary mixtures.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
A. S., E. F., and G. S. acknowledge funding from NSF DMR-1608086.

## Notes and references
1 R. C. Zeller and R. O. Pohl, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1971, **4**, 2029–2041.
2 R. B. Stephens, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1973, **8**, 2896–2905.
3 M. P. Zaitlin and A. C. Anderson, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1975, **12**, 4475–4486.
4 R. O. Pohl, X. Liu and E. Thompson, *Rev. Mod. Phys.*, 2002, **74**, 991–1013.
5 H. Mizuno, H. Shiba and A. Ikeda, *Proc. Natl. Acad. Sci. U. S. A.*, 2017, **114**, 9767–9774.
6 L. Wang, A. Ninarello, P. Guan, L. Berthier, G. Szamel and E. Flenner, *Nat. Commun.*, 2019, **10**, 26.
7 H. Mizuno, S. Mossa and J.-L. Barrat, *Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys.*, 2013, **87**, 042306.
8 H. Mizuno, S. Mossa and J.-L. Barrat, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2016, **94**, 144303.
9 K. Yoshimoto, T. S. Jain, K. V. Workum, P. F. Nealey and J. J. de Pablo, *Phys. Rev. Lett.*, 2004, **93**, 175501.
10 M. Tsamados, A. Tanguy, C. Goldenberg and J.-L. Barrat, *Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys.*, 2009, **80**, 026112.
11 F. Léonforte, A. Tanguy, J. P. Wittmer and J.-L. Barrat, *Phys. Rev. Lett.*, 2006, **97**, 055501.
12 H. Mizuno, S. Mossa and J.-L. Barrat, *Proc. Natl. Acad. Sci. U. S. A.*, 2014, **111**, 11949–11954.
13 S. Gelin, H. Tanaka and A. Lemaître, *Nat. Mater.*, 2016, **15**, 1177–1181.
14 C. Caroli and A. Lemaître, *Phys. Rev. Lett.*, 2019, **123**, 055501.
15 Y. Fan, T. Iwashita and T. Egami, *Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys.*, 2014, **89**, 062313.
16 H. Mizuno, S. Mossa and J.-L. Barrat, *Europhys. Lett.*, 2013, **104**, 56001.
17 H. Wagner, D. Bedorf, S. Küchemann, M. Schwabe, B. Zhang, W. Arnold and K. Samwer, *Nat. Mater.*, 2011, **10**, 439–442.
18 H. Mizuno, L. E. Silbert and M. Sperl, *Phys. Rev. Lett.*, 2016, **116**, 068302.
19 E. A. A. Pogna, A. I. Chumakov, C. Ferrante, M. A. Ramos and T. Scopigno, *J. Phys. Chem. Lett.*, 2019, **10**, 427–432.
20 W. Schirmacher, G. Ruocco and T. Scopigno, *Phys. Rev. Lett.*, 2007, **98**, 025501.
21 W. Schirmacher, C. Tomaras, B. Schmid, G. Baldi, G. Viliani, G. Ruocco and T. Scopigno, *Condens. Matter Phys.*, 2010, **13**, 23606.
22 H. Mizuno and A. Ikeda, *Phys. Rev. E*, 2018, **98**, 062612.
23 A. Moriel, G. Kapteijns, C. Rainone, J. Zylberg, E. Lerner and E. Bouchbinder, 2019, *arXiv:1905.03378*.
24 E. Lerner, *J. Non-Cryst. Solids*, 2019, **522**, 119570.
25 A. Ninarello, L. Berthier and D. Coslovich, *Phys. Rev. X*, 2017, **7**, 021039.
26 T. S. Grigera and G. Parisi, *Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys.*, 2001, **63**, 045102.
27 R. Gutiérrez, S. Karmakar, Y. G. Pollack and I. Procaccia, *Europhys. Lett.*, 2015, **111**, 56009.
28 http://lammps.sandia.gov.
29 S. Plimpton, *J. Comput. Phys.*, 1995, **119**, 1–19.
30 A. Tanguy, J. P. Wittmer, F. Leonforte and J.-L. Barrat, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2002, **66**, 174205.
31 R. S. Lakes, T. Lee, A. Bersie and Y. C. Wang, *Nature*, 2001, **410**, 565–567.
32 W. Schirmacher, *Europhys. Lett.*, 2006, **73**, 892–898.
33 A. Marruzzo, W. Schirmacher, A. Fratalocchi and G. Ruocco, *Sci. Rep.*, 2013, **3**, 1407.
34 H. Mizuno, G. Ruocco and S. Mossa, 2019, *arXiv:1905.10235v1*.
35 L. Wang, L. Berthier, E. Flenner, P. Guan and G. Szamel, *Soft Matter*, 2019, 7018–7025.