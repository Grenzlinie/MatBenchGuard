Enhanced auxeticity in Yukawa systems due to introduction of nanochannels in $^{[001]}$-direction

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 Smart Mater. Struct. 25 054007

(http://iopscience.iop.org/0964-1726/25/5/054007)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 198.91.37.2
This content was downloaded on 06/04/2016 at 16:48

Please note that terms and conditions apply.

# Enhanced auxeticity in Yukawa systems due to introduction of nanochannels in [001]-direction

Konstantin V Tretiakov, Paweł M Pigłowski, Krzysztof Hyżorek and
Krzysztof W Wojciechowski¹

Institute of Molecular Physics, Polish Academy of Sciences, Mariana Smoluchowskiego 17, 60-179
Poznań, Poland

E-mail: kvt@ifmpan.poznan.pl (K V Tretiakov) and kww@ifmpan.poznan.pl (K W Wojciechowski)

Received 9 November 2015, revised 19 January 2016
Accepted for publication 1 February 2016
Published 8 April 2016

![](./images/814538201510182912_1.jpg)

## Abstract
A new approach to search for materials with auxetic properties by modifying structures of solids at molecular level has been proposed. The analysis of elastic properties of the face-centered cubic Yukawa crystals with very narrow nanochannels in the [001] crystallographic direction using Monte Carlo simulations in the isothermal-isobaric ensemble has been done. An influence of the size of nanochannels on the value of Poisson's ratio in main crystallographic directions has been studied. It has been shown that the insertion of nanochannels in the system causes a decrease of the Poisson's ratio in the direction [110][1$\overline{1}$0] from $-0.15(2)$ to $-0.29(3)$. That means an amplification of auxetity in the studied system twice as compared to the system without nanochannels.

Keywords: auxetics, nanochannels, Monte Carlo simulations, Yukawa potential, negative Poisson's ratio

(Some figures may appear in colour only in the online journal)

---

## 1. Introduction
Smart materials [1–6] are increasingly finding their applications in the modern industry. Therefore the interest to them is growing up, especially in advanced technologies. One of the new classes of such materials are auxetics [7, 8]. Auxetics or materials with negative Poisson's ratio (the definition of the Poisson's ratio can be found in [9]) have an unusual property—in process of an infinitesimal stretching (compressing) lateral dimensions are increasing (decreasing). Due to this property, these materials are finding applications in the development of devices, machines, sensors, and in other applications [10, 11]. In recent years one can note an increasing interest in research on the new auxetic materials and mechanisms leading to the reduction of the Poisson's ratio [12, 13]. Several mechanisms leading to auxeticity can be distinguished that are either associated with the structure of the system at macroscopic [14] and microscopic [15] level or collective interactions of particles in molecular systems [16].

These ideas were developed in a number of works [17–19]. One of such works relates to the auxetic properties of the system in which particles interact by a hard-core repulsive Yukawa potential (HCRYP) [20]. It has been shown that the considered system is partially auxetic. Here, it is worth to mention that the Yukawa potential [21] is one of well-known potentials in the field of condensed matter. A variety of physical properties have been studied for the Yukawa potential [22–27]. Among others the equation of state of real colloidal systems consisting of charged particles immersed in the electrolyte solution can be described by this model system [22–24].

In this paper a combination of two approaches is proposed. From one side it is well known that the Poisson's ratio strongly depends on the structure of system, and from the other side—that collective interactions of particles in molecular systems can lead to auxeticity. Here, an attempt of

¹ Author to whom any correspondence should be addressed.

structural modification at the molecular level is tested on the system of particles interacting through the HCRYP. In this context the change of the molecular structure by introducing nanochannels in the [001] crystallographic direction of the Yukawa crystal has been done.

The goal of this work is to propose a completely new approach to searching for mechanisms, which lead to auxetic behaviour of materials.

The paper is organized as follows. In section 2, the model and structures of the studied systems, definitions of physical quantities to describe the elastic properties of the system, and details of simulations are provided. In section 3, the analysis of the obtained results with particular attention to size effects and the impact of nanochannels to Poisson's ratio have been presented. In section 4, the summary and conclusions have been done.

## 2. Preliminaries

### 2.1. Model and structures

The considered model consists of $N_{\mathrm{s}}$ particles forming a solid of the face-centered cubic (fcc) structure and interacting with each other via Yukawa potential and $N_{\mathrm{ch}}$ hard spheres that fill an array of channels made in the solid. The resulting $N=N_{\mathrm{s}}+N_{\mathrm{ch}}$ particles are arranged in the crystal. The HCRYP describes the interaction of the $N_{\mathrm{s}}$ particles is as follows

$$
\beta u_{i j}= \begin{cases}\infty, & r_{i j}<\sigma, \\ \beta \varepsilon \frac{\exp \left[-\kappa \sigma\left(r_{i j} / \sigma-1\right)\right]}{r_{i j} / \sigma}, & r_{i j} \geqslant \sigma,\end{cases}
\tag{1}
$$

where $\beta=1 / k_{\mathrm{B}} T$, $k_{\mathrm{B}}$ is a Boltzmann constant, $T$ is the temperature, $\kappa$ is the inverse screening length, $\sigma$ is diameter of particles, $\varepsilon$ is contact potential.

The interaction of particles filling channels ($N_{\mathrm{ch}}$) with each other and with the Yukawa particles is modelled by the hard potential

$$
\beta u_{i j}= \begin{cases}\infty, & r_{i j}<\sigma, \\ 0, & r_{i j} \geqslant \sigma.\end{cases}
\tag{2}
$$

The studied structures with channels are presented in figure 1. Inside the fcc crystal formed by $N$ particles interacting via HCRYP, channels were created by removing $N_{\mathrm{ch}}$ particles. The removed particles were replaced by the hard spheres defined in (2). The channels were oriented in the [001] direction (see figure 1). In the present study two types of nanochannels were considered (**A** and **B**). The type **A** consists of a single chain of particles in a given direction (figure 1(a)), those particles create an axis of the channel. The channel of **B**-type comprises particles of channel A-type and all particles located at the distance of no more than $a/\sqrt{2}$ from the channel axis, where $a$ is the lattice constant (figure 1(b)).

In order to analyse the influence of each type of the channels on the elastic properties, especially on the Poisson's ratio, the concentration of 'channel' particles in the system (or otherwise the concentration of particles filling the channel to all particles in the system) has been defined

$$
c=\frac{N_{\mathrm{ch}}}{N} \times 100 \%.
\tag{3}
$$

This concentration can be changed, e.g., by tuning the distance between channels or their width.

### 2.2. Elasticity

To evaluate the elastic properties of the studied systems the Monte Carlo method in the NpT ensemble with variable shape of the periodic box was used [28-30]. The equilibrium condition for the system in the isothermal-isobaric ensemble is a minimum of the Gibbs free energy. Thus an infinitesimally small elastic deformation of the equilibrium crystal leads to increase of its free energy by [9, 30]

$$
\Delta G=V_{p}\left(\frac{1}{2} B_{i j k l} \varepsilon_{i j} \varepsilon_{k l}+\cdots\right),
\tag{4}
$$

where $V_{p}$ is the volume of the crystal in equilibrium at the pressure $p$, $\varepsilon_{i j}$ is the strain tensor, and $B_{i j k l}$ is the tensor of elastic moduli. It is well known that alternatively the elastic properties of the studied system can be also described completely by the tensor of elastic compliances $S_{i k l m}$, which is strictly related to the tensor $B_{i j k l}$ by the following relation

$$
S_{i k l m} B_{l m p q}=\frac{1}{2}\left(\delta_{i p} \delta_{k q}+\delta_{i q} \delta_{k p}\right).
\tag{5}
$$

In addition, the description of the elastic properties by the compliance tensor was dictated by the fact that the compliance tensor is determined directly from the MC simulations using the Parinello-Rahmann method [30]. In this method, the components of the compliance tensor are found by the analysis of fluctuations of the box matrix. In [28, 29] it has been shown that the strain tensor of the studied system can be expressed by the box matrix tensor $\mathbf{h}$ and the reference box matrix $\mathbf{h}_{0}$ in the following way

$$
\varepsilon=\frac{1}{2}\left(\mathbf{h}_{0}^{-1} \cdot \mathbf{h} \cdot \mathbf{h} \cdot \mathbf{h}_{0}^{-1}-\mathbf{I}\right),
\tag{6}
$$

where $\mathbf{I}$ is the unit matrix and it has been assumed that the matrices $\mathbf{h}$, $\mathbf{h}_{0}$ are symmetric. The elastic compliances read

$$
S_{i j k l}=\left\langle\Delta \varepsilon_{i j} \Delta \varepsilon_{k l}\right\rangle \frac{V_{p}}{k_{B} T},
\tag{7}
$$

where $\langle\cdots\rangle$ means averaging in the NpT ensemble.

The knowledge of all components of $S_{i j k l}$ allows one to calculate the values of the Poisson's ratio in any crystallographic direction. If the studied system is deformed in the direction indicated by the versor $\hat{\mathbf{n}}$ and the reaction of the system on the applied deformation is observed in the direction indicated by the versor $\hat{\mathbf{m}}$ such that $\hat{\mathbf{n}} \cdot \hat{\mathbf{m}}=0$ (figure 2) then

![](./images/814538201510182912_2.jpg)

Figure 1. The fcc structures with nanochannels in [001]-direction. The particles interacting via Yukawa potential are marked in green colour. Red particles show the hard spheres which fill the nanochannels. Structures of studied crystals with (a) the nanochannel of A-type, (b) the nanochannel of B-type, (c) four nanochannels of A-type, (d) four nanochannels of B-type. The first column presents studied systems. The second column represents the projections of systems on XY plane. The third column shows the positions of particles (interacting via HCRYP) which are marked by green points and red particles (hard spheres) belonging to nanochannels.

the Poisson's ratio for this case is [31]

$$
\nu_{n m}=-\frac{\varepsilon_{m}}{\varepsilon_{n}}=-\frac{m_{i} m_{j} S_{i j k l} n_{k} n_{l}}{n_{p} n_{r} S_{p r s t} n_{s} n_{t}}. \tag{8}
$$

### 2.3. Simulation details

In this paper systems consisting of $N=108,256,500,864$ particles with a single channel of one of the types were stu- died. In addition, to test the size dependence of results, sys- tems of $N=2000$ particles and comprising four channels of $\boldsymbol{A}$ or $\boldsymbol{B}$ type (figures 1(c) and (d)) were investigated. For the same purpose, the systems of $N=1000$ and $N=4000$ which are twice longer in $z$-direction than in figures 1(b) and (d) were also considered. In the studied cases, the concentration of 'channel' particles in the system was ranged from $c \approx 0.7 \%$ to $c \approx 14 \%$.

Based on the analysis of parameters $\kappa$ and $\beta$ carried out in previous works [20, 26], in simulations the following values of dimensionless parameters have been used: the inverse screening length $\kappa \sigma=10$, the inverse temperature $\beta \varepsilon=20$, the pressure $P \sigma^{3} \beta=100$.

The method of determination the elastic compliances used in this work is simple, but its convergence is rather slow, so typical lengths of the runs were equal $10^{7}$ cycles MC after

![](./images/814538201510182912_3.jpg)

Figure 2. The direction of the applied deformation is denoted by the versor $\hat{\mathbf{n}}$. The versor $\hat{\mathbf{m}}$ represents the direction in which the reaction of the system is observed. $\alpha$ is the angle between $\hat{\mathbf{m}}$ and the versor which is created by plane $Oxy$ and plane orthogonal to versor $\hat{\mathbf{n}}$.

equilibration ($10^6$ MC cycles). The cut-off at $r_{\rm c}=2.5\sigma$ was used for the interaction potential (1). In all simulations the acceptance ratio of box and particle moves was kept around 30%. The periodic boundary conditions were used in all directions ($x,y,z$).

## 3. Results and discussion

### 3.1. Size effects

Usually, the dependence of the results on the system size is gained by increasing the size of the system and analysing the obtained results with respect to the change. In the case of investigating the system with nanochannels this approach was restricted to comparison of the results obtained for samples with a single nanochannel (which can be thought of as a 'unit cell' of the modified crystal, see figures 1(a) and (b)) and samples obtained by quadrupling them in the $x$-$y$ plane (see figures 1(c) and (d)). Both those systems were then doubled in the $z$-direction, see figure 3. It is clear that all the four systems have the same concentration of 'channel' particles and the same type of nanochannel.

For deformations applied in main crystallographic directions, the Poisson's ratio for any direction defined by the angle $\alpha$ (see figure 2) has been determined. As it can be seen in figure 3, almost the same dependence of the Poisson's ratio on $\alpha$ as for the system of $N=500$ ($c=5\%$) and sample obtained by quadrupling it in the $x$-$y$ plane ($N=2000$, $c=5\%$) as for systems twice larger (longer) in $z$-directions ($N=1000$, $N=4000$, $c=5\%$) were obtained.

This indicates that samples with single nanochannels are representative for Poisson's ratio. It is worth mentioning that similar conclusions were obtained for a number of other systems studied earlier by this method [17, 32].

It should be noted that in the discussed case the whole system consisting of $N=500$ particles is a unit cell of the studied crystal. It can be expected that the introduction of a nanochannel can significantly alter the crystal structure and its stability. This can be expressed, for example, by melting of the studied crystal. The obtained results for crystal comprising four 'unit cells' indicate that for the studied types of nanochannels both the symmetry of the crystal and its stability are well approximated by samples with single channels. Thus, further discussion in this paper is restricted to such samples.

![](./images/814538201510182912_4.jpg)

Figure 3. Comparison of values of the Poisson's ratio of systems with the same concentration ($c=5\%$) and different sizes $N=500$ (solid line), $N=1000$ (long dashed line), $N=2000$ (short dashed line), and $N=4000$ (thick and very short dashed line). Crystallographic directions are indicated above the curves.

### 3.2. Concentration of 'channel' particles in the system

The contribution of the particles filling the channel in a total number of particles affects the properties of the system because hard spheres filling the channel interact in a different way than the Yukawa particles. This effect depends on the concentration of 'channel' particles defined by formula (3). The figure 4 presents the Poisson's ratio in the main crystallographic directions, for any transverse direction and for different channels corresponding to different concentrations. This figure shows that the increase in the concentration of 'channel' particles significantly affects the elastic properties of the investigated crystal, in particular, the Poisson's ratio.

While analysing this figure, one can notice a reduction of Poisson's ratio for $\alpha=0$ in two crystallographic directions [100] and [110] (figures 4(a) and (b)). The particularly interesting is the change of Poisson's ratio in the direction [110]. The observed decrease of Poisson's ratio almost twice amplifies auxeticity in the direction [110][1$\overline{1}$0]. At the same time, it can be observed an increase of anisotropy of the elastic properties in the directions [100] and [110]. In contrast to those, the Poisson's ratio in the direction of [111], is not changed significantly by the introduction of nanochannels and also with increasing concentration of 'channel' particles.

![](./images/814538201510182912_5.jpg)

Figure 4. Poisson's ratio in three main crystallographic directions as a function of transverse direction.

The figure 5 shows the dependence of the Poisson's ratio in the main crystallographic directions for $\alpha = 0, \pi/2$ on concentration of 'channel' particles in the system. Here we see a linear relationship between Poisson's ratio and concentration. It is worth noting that the Poisson's ratio in the direction of $[110][1\overline{1}0]$ in the considered range becomes almost twice as negative (it changes from $-0.15$ to $-0.29$), amplifying the auxeticity in this direction.

![](./images/814538201510182912_6.jpg)

Figure 5. Dependence of the Poisson's ratio in main crystallographic directions on the concentration of 'channel' particles.

## 4. Summary and conclusions

A new approach to the problem of obtaining materials with desired physical properties is proposed here in the aspect of searching for mechanisms leading to auxeticity. The approach is based on structural modifications at the molecular level. The presented results for the examples of Yukawa and hard interactions show its effectiveness and suggest the possibility of much wider use.

Monte Carlo simulations in the NpT ensemble have been carried out to determine the Poisson's ratio in systems with very narrow channels. The elastic properties of the two types of nanochannels have been examined. Quantitative analysis of the concentration of particles forming nanochannel on the value of Poisson's ratio indicates the possibility of decreasing Poisson's ratio in Yukawa systems by modifying structure of crystals, in which very narrow nanochannels have been introduced. The presence of nanochannels in [001]-direction results in almost doubling the negative value of Poisson's ratio (from $-0.15$ to $-0.29$) in $[110][1\overline{1}0]$ direction, with respect to the system without nanochannel. A linear relationship between the Poisson's ratio in the main crystallographic directions and concentration of particles forming nanochannel has been observed.

One should expect that results of the studies will be usefull not only for researchers working in the fields related to the Yukawa and hard sphere potentials.

Closing this work the authors should add that intensive work on the introduction of nanochannels of different thickness in different crystallographic directions of various systems is in progress and its results will be published soon.

## Acknowledgments

This work was supported by the Polish National Science Center grants DEC-2012/05/B/ST3/03255. Part of the calculations was performed at the Poznań Supercomputing and Networking Center (PCSS).

### References

[1] Xie P and Zhang R 2005 *J. Mater. Chem.* **15** 2529–50

[2] Song Y, Wei W and Qu X 2011 *Adv. Mater.* **23** 4215–36

[3] Hu J, Meng H, Li G and Ibekwe S 2012 *Smart Mater. Struct.* **21** 053001

[4] White E M, Yatvin J, Grubbs J B, Bilbrey J A and Locklin J 2013 *J. Polym. Sci. B* **51** 1084–99

[5] Liu Y, Du H, Liu L and Leng J 2014 *Smart Mater. Struct.* **23** 023001

[6] Barbarino S, Saavedra Flores E I, Dayyani I and Friswell M I 2014 *Smart Mater. Struct.* **23** 063001

[7] Evans K E, Nkansah M A, Hutchinson I J and Rogers S C 1991 *Nature* **353** 124–124

[8] Baughman R H 2003 *Nature* **425** 667

[9] Landau L D and Lifshits E M 1993 *Theory of Elasticity* 3rd edn (Oxford: Pergamon Press)

[10] Liu Q 2006 *Literature Review: Materials with Negative Poisson's Ratios and Potential Applications to Aerospace and Defence* Defence Science and Technology Organisation, Common wealth of Australia

[11] Ma Y, Scarpa F, Zhang D, Zhu B, Chen L and Hong J 2013 *Smart Mater. Struct.* **22** 084012

[12] Wojciechowski K W, Scarpa F, Grima J N and Alderson A 2015 *Phys. Status Solidi b* **252** 1421–5 See also references therein

[13] Lim T C 2015 *Auxetic Materials and Structures* (Singapore: Springer)

[14] Almgren R F 1985 *J. Elasticity* **15** 427–30

[15] Lakes R S 1987 *Science* **238** 551

[16] Wojciechowski K W 1989 *Phys. Lett. A* **137** 60–4

[17] Tretiakov K V 2009 *J. Non-Cryst. Solids* **355** 1435

[18] Grima J N, Caruana-Gauci R, Dudek M R, Wojciechowski K W and Gatt R 2013 *Smart Mater. Struct.* **22** 084016

[19] Rossiter J, Takashima K, Scarpa F, Walters P and Mukai T 2014 *Smart Mater. Struct.* **23** 045007

[20] Tretiakov K V and Wojciechowski K W 2014 *Phys. Status Solidi b* **251** 383–7

[21] Hansen J P and McDonald I R 2006 *Theory of Simple Liquids* (Amsterdam: Academic Press)

[22] Azhar F E, Baus M and Ryckaert J P 2000 *J. Chem. Phys.* **112** 5121–6

[23] Auer S and Frenkel D 2002 *J. Phys.: Condens. Matter* **7667** 14

[24] Hynninen A P and Dijkstra M 2003 *Phys. Rev. E* **68** 021407

[25] Heinen M, Holmqvist P, Banchio A J and Nägele G 2011 *J. Chem. Phys.* **134** 44532

[26] Colombo J and Dijkstra M 2011 *J. Chem. Phys.* **134** 154504

[27] van der Linden M N, van Blaaderen A and Dijkstra M 2013 *J. Chem. Phys.* **138** 114903

[28] Parrinello M and Rahman A 1981 *J. Appl. Phys.* **52** 7182–90

[29] Parrinello M and Rahman A 1982 *J. Chem. Phys.* **76** 2662–6

[30] Wojciechowski K W, Tretiakov K V and Kowalik M 2003 *Phys. Rev. E* **67** 036121

[31] Tokmakova S P 2005 *Phys. Status Solidi b* **242** 721–9

[32] Tretiakov K V and Wojciechowski K W 2005 *J. Chem. Phys.* **123** 074509