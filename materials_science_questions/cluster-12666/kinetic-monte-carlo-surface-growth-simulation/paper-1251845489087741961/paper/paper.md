# Morphological Transition: From Meanders to Mound Structures

Marta A. Chabowska$^\mathrm{a}$, Hristina Popova$^\mathrm{b}$, Magdalena A. Załuska-Kotur$^\mathrm{a}$

$^\mathrm{a}$Institute of Physics, Polish Academy of Sciences, Al. Lotnikow 32/46, Warsaw, Poland
$^\mathrm{b}$Institute of Physical Chemistry, Bulgarian Academy of Sciences, Acad. G. Bonchev str., 1113, Sofia, Bulgaria

---

## Abstract

Mound formation on flat and miscut crystal surfaces exhibits distinct growth behaviors. While mound structures are the predominant feature on flat surfaces, miscut surfaces display a smooth transition from meandered patterns to three-dimensional mounds, depending on both internal and external conditions. We investigate this morphological evolution-from meander-like surface patterns to faceted pyramidal structures-using a vicinal Cellular Automata modeling framework. The transition is shown to be governed by the competition between the Ehrlich-Schwoebel barrier and adatom mobility on terraces. Under moderate barrier strengths and sufficiently high terrace diffusivity, the system demonstrates a reversible transition from mounded configurations to regular step meandered patterns. This reveals a complex interplay between kinetic barriers and mass transport. Our simulations cover a wide range of growth conditions, including variations in deposition flux, surface diffusion rates, temperature, and miscut angle. By applying the height-height correlation function, we calculate the correlation lengths along and across the steps and analyze their scaling behavior. These results offer insight into the continuum pathways that connect distinct classes of surface structures and provide a unified framework for describing pattern evolution across different crystal growth regimes.

**Keywords:** Crystal growth, surface patterns, mounding, step meandering, computer simulations, cellular automata, time scaling

---

## 1. Introduction

The spontaneous formation of three-dimensional (3D) surface patterns during epitaxial crystal growth is a subject of longstanding interest, both from a fundamental and technological perspective. Among them, pyramidal mound structures have been observed across a range of material systems [1, 2, 3, 4, 5, 6, 7], and are known to emerge via different mechanisms, such as kinetic instabilities or defect-driven growth processes. Their presence may be beneficial, as in the case of templated self-assembly and nanostructure nucleation, or detrimental when flatness and surface uniformity are desired for device applications.

Understanding how such 3D morphologies develop requires a detailed analysis of the interplay between atomic-scale kinetics and macroscopic growth conditions. Surface orientation, step structure, diffusion anisotropy, and kinetic barriers all contribute to the complexity of pattern formation. On flat crystal surfaces, mound formation often dominates the growth landscape due to the Ehrlich-Schwoebel (ES) barrier, which suppresses downward adatom motion at step edges and promotes vertical mass transport. In contrast, vicinal (miscut) surfaces - characterized by a regular array of atomic steps - support lateral instabilities that can lead to step meandering. These meandered patterns may stabilize into periodic undulations or transition into 3D faceted structures depending on the specific conditions.

For years, scientists have debated the origins of mound formation. In the literature, this topic is approached either analytically [7, 8, 9, 10, 11] or atomistically [7, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19]. One of the first papers on this subject, [8], showed how nonlinear instabilities lead to self-organized mound structures. The authors have demonstrated the slope selection and coarsening mechanisms in epitaxial growth through the use of continuum equations. Similarly, Chakrabarti and Dasgupta [9] proposed a nonlinear instability mechanism that drives mound formation and coarsening. This mechanism offers an alternative to ES-barrier-driven models. Conversely, Rost et al. [10] extended the instability theory to vicinal surfaces, where pre-existing steps along with the existence of step ES barrier change

Email address: galicka@ifpan.edu.pl (Marta A. Chabowska)

the dynamics. They emphasized the competition between smooth step-flow growth and unstable mound formation. Many other publications [13, 14, 15, 16, 17] have considered the same mechanism to be responsible for mound formation. Punyindu Chatraphorn et al. [18] proposed yet another approach, studying models of networks with limited mobility. They demonstrated that mounds can form even in the absence of explicit ES barriers. Two works, [7, 12], stand out among the literature. These works form the backbone of the field by synthesizing kinetic theory, scaling laws, instabilities, and experimental evidence, as well as emphasizing stochastic effects, kinetic roughening, and step-edge barriers. These studies serve as a benchmark references, tying together atomistic processes and continuum descriptions. Today, the consensus is that multiple mechanisms can interact depending on the growth conditions.

A very interesting perspective that is highly relevant to our study is presented by Rost et al. [10] and by Bryan et al. [11]. In the first paper, the authors used continuum models and kinetic Monte Carlo simulations to analyze the instability of step flow during molecular beam epitaxy. They observed transitions from ripples to 3D structures during their studies. In the second paper, the authors used a model based on the Burton, Cabrera, and Frank theory to understand how surface kinetics depend on vapor supersaturation and substrate misorientation angle. The study demonstrated a transition from 3D structures through meanders to step bunches, which depends on the surface misorientation.

Compared to previous studies, the present work focuses on elucidating the transition between two characteristic surface morphologies: regular meandered step patterns and fully developed faceted pyramidal mounds. Such a transition reflects a shift in the dominant physical processes - between terrace diffusion and asymmetries of interlayer kinetic - and is a hallmark of the complex dynamical behavior of growing surfaces. While meandered steps arise from lateral instabilities under moderate anisotropy and diffusion rates [20], pyramidal mounds are typically linked to stronger Ehrlich-Schwoebel barriers and reduced adatom mobility. In this work, we employ a novel method to investigate the transition between these two growth regimes.

To explore the transition from meanders to mounds, we employ a vicinal Cellular Automaton (VicCA) modeling framework, which captures the key kinetic features of step flow growth, including adatom diffusion, attachment kinetics, and step-edge barriers. By tuning the ES barrier and surface diffusion parameters, we investigate the morphological evolution of surfaces under a wide range of conditions. We demonstrate that the competition between downward hopping suppression (controlled by the height of the ES barrier) and adatom mobility on terraces governs the observed surface morphology. Crucially, we find that the transition is reversible: high diffusion rates are able to restore meandered patterns even after mound formation has occurred. This suggests that the system resides near a dynamic equilibrium point, where small changes in kinetic parameters produce qualitatively different morphologies.

To quantitatively characterize the transition, we analyze the evolution of height-height correlation functions, surface roughness, and characteristic lateral and vertical length scales. These measures allow us to distinguish between disordered mound growth, regular meandering, and highly ordered faceted pyramids. We further discuss the scaling behavior of these quantities in relation to diffusion rates and step-edge barriers.

Overall, this study offers a unified framework for understanding the morphological evolution of both flat and vicinal surfaces during epitaxial growth. By linking meander formation and mound growth within a common kinetic picture, we provide insight into how surface structures can be controlled by tuning the growth parameters. These results are relevant for the rational design of surface templates and the development of nanostructured materials via bottom-up fabrication techniques.

## 2. The model

The process of surface dynamics is analyzed using a $(2+1)$D vicinal Cellular Automaton model. This model simulates the growth of a vicinal crystal surface through a combination of Cellular Automaton and Monte Carlo techniques, which together govern the evolution of the surface [20, 21, 22, 23, 24]. The model is divided into two interrelated components, enabling independent control of each of them and enhancing both the efficiency of simulations and the model's adaptability.

The system comprises of two main parts: the bulk crystal and the surface layer populated by diffusing adatoms, which continuously exchange particles during growth. In real materials, these two regions consist of identical atoms capable of moving and rearranging over time. However, during the growth process, atomic movement within the bulk is limited due to strong interatomic bonding and spatial constraints imposed by newly arriving atoms. Crystal growth fundamentally involves the integration of atoms into the bulk structure. Prior to incorporation, atoms are supplied from the surroundings and initially adsorbed randomly onto

the crystal surface. These adsorbed atoms then diffuse along the surface (Fig. 1a) in search of energetically favorable sites. This mobile population of atoms forms what is referred to as the surface cloud. Once an atom reaches a particularly stable position, the probability of its desorption becomes negligible.

The crystal component of the model is constructed on a square lattice. The results presented below are based on simulations initiated from a flat or vicinal surface, the latter composed of monoatomic steps descending from left to right, with an initial terrace width denoted by $l_0$. Periodic boundary conditions are applied along the step edges, while helical periodic boundary conditions are used across the steps to preserve the relative height differences between terraces.

To ensure efficient and fast computations, crystal growth is modeled using Cellular Automaton (CA) rules, which enable parallel processing. At each time step, the CA rules determine which atoms are incorporated into the crystal lattice based on the current configuration of atoms and step positions on the surface. In this model, the most stable incorporation sites are step voids with three neighboring bonds and kinks with two bonds. These specific sites play a crucial role in the vicinal automaton component of the VicCA model. The model assumes that such voids and kinks are filled unconditionally. In contrast, atoms located in less stable positions - such as those with only a single bond to the step or entirely isolated on the terrace - require additional conditions to be met before incorporation is permitted. Consequently, adatoms are allowed to diffuse on top of the terrace or along the step edge until the criteria for stable incorporation are satisfied, effectively enabling control over the step stiffness.

Various methods can be employed to regulate the attachment frequency, such as assigning a low probability of incorporation. Several alternatives were tested, all producing comparable results. Ultimately, we adopted an approach that requires the presence of at least one neighboring particle for successful incorporation (see Fig. 1b). This condition ensures that an adatom is incorporated into a straight step only if another adatom from the diffusing cloud is adjacent to it. The neighboring atom provides an additional bond, thereby stabilizing the attachment and justifying the incorporation process. The process can be viewed as nucleation occurring at the step edge, characterized by a critical nucleus size of two atoms.

The model also allows for independent control of the nucleation process. When nucleation on top of the terrace is suppressed, steps advance regularly, exhibiting bunching or meandering behavior, but true three-dimensional growth does not occur. When nucleation is enabled, a critical nucleus size can be defined, adjusting the difficulty of nucleation. In the simulations presented here, a critical nucleus size of four was chosen. According to the CA rules, if an adatom is surrounded by three other adatoms, it becomes incorporated into the crystal, forming a stable nucleus for subsequent growth. This mechanism enables nucleation and thus the formation of three-dimensional nanostructures. Examples of various configurations leading to adatom incorporation are illustrated in Fig. 1b.

A key component of the model is adatom diffusion, which acts as the fundamental driving force behind surface pattern formation. This process is strongly influenced by the underlying energy potential landscape experienced by the atoms. Drawing on insights from ab initio studies [25, 26, 27, 28], we postulate the existence of a potential well located at the bottom of each step. In our simulations, the depth of this well is kept constant and is denoted by $E_V$ (see Fig. 2a). As demonstrated in [20], both the presence and depth of this potential well play a critical role in triggering and shaping the step meandering process. The overall shape of the surface potential is further modulated by factors such as dangling bonds, surface reconstruction, and additional energy barriers. Particularly relevant to the development of step meanders is the ES barrier, located at the top of the step (Fig. 2b), which hinders adatom crossing the step. The height of this barrier is denoted by $E_{ES}$. It is important to note that the shape of the surface potential - as well as the positions of the potential well $E_V$ and ES barrier $E_{ES}$ - depend on the positions of the steps and shift accordingly with step displacement. As a result, the potential landscape and step morphology become intricately linked, often evolving in a strongly coupled manner.

In the model, adatoms diffuse independently. On flat terraces, jumps occur with uniform probability, except near step edges where local potentials alter the dynamics. The diffusion rate and the degree of step permeability are regulated by the number of diffusion attempts each adatom makes per unit time, denoted by $n_{DS}$. Each adatom attempts to perform $n_{DS}$ jumps, with each movement requiring the adatom to overcome an energy barrier between two consecutive potential wells, and this energy is equal to $E_0$, referred to as a diffusion barrier. In the model studied below, all jumps along terrace, away from steps happen with the same probability given by:

$$
P_0 = e^{-\beta E_0}, \tag{1}
$$

where $\beta = 1/(k_B T)$, $T$ is the temperature, and $k_B$ is

![](./images/1251845489087741961_1.jpg)

Figure 1: A single time step of the simulation procedure consists of the following stages: (1) the diffusion process, (2) the growth update (illustrating different scenarios of adatom incorporation), and (3) the adatom concentration compensation. For the system shown, the number of adatoms must be adjusted to 5 in the last stage of the time step to keep the initial concentration of adatoms constant.

![](./images/1251845489087741961_2.jpg)

Figure 2: Visualization of the potential landscape, including the diffusion barrier $E_0$ and highlighting the potential well at the bottom of the step. Side view of the initial surface with a) only the potential well $E_V$ and b) the additional Ehrlich-Schwoebel barrier $E_{ES}$.

the Boltzmann constant. The diffusion constant can be expressed as $D = a^2 \nu n_{DS} P_0$, where $a$ is the lattice constant, used as a unit of length in our simulations, and $\nu$ is the attempt frequency, usually of order $\nu = 10^{12} - 10^{13} Hz$.

During the simulation, we assume that the fastest processes happens with probability equal to 1, which means that the duration of all processes is normalized by the value of $P_0$. For sites close to steps we have:

$$
\frac{P_V}{P_0} = \left\{ \begin{array}{cc}
e^{-\beta E_V} & \text{out} \\
1 & \text{in}
\end{array} \right. \tag{2}
$$

for jumps out and in the well accordingly, whereas in the presence of an ES barrier, this probability of a jump across the steps is set to

$$
\frac{P_{ES}}{P_0} = \left\{ \begin{array}{cc}
e^{-(\beta E_{ES} + \beta E_V)} & \text{out} \\
e^{-\beta E_{ES}} & \text{in}.
\end{array} \right. \tag{3}
$$

As in traditional Monte Carlo simulations, adatoms that jump, as well as the jump direction, are selected randomly to prevent artificial correlations.

By appropriately combining diffusion mechanisms with CA rules, various aspects of surface dynamics can be systematically investigated. Each simulation step concludes with replenishing the adatom concentration to a fixed value $c_0$, thereby maintaining a constant external flux of incoming atoms (see Fig. 1c).

Unlike conventional Monte Carlo simulations, the VicCA model permits independent control over all parameters. In standard MC simulations, jump probabilities and attachment rates are inherently coupled to interaction strengths. In contrast, the VicCA model decouples step attachment from kink attachment and naturally incorporates additional barriers into the potential landscape. Rather than deriving parameters from interactions among multiple atomic neighbors, VicCA allows these parameters to be specified independently on a site-by-site basis.

However, the calibration of time and temperature scales demands careful attention, as these depend on several factors, including the diffusion barrier height $E_0$, the number of diffusional steps $n_{DS}$, the attempt frequency $\nu$, and the external flux $c_0$. The real-time duration of each VicCA simulation step is given by $\tau = (\nu n_{DS} \exp(-\beta E_0))^{-1}$, while the ratio of diffusion to

external particle flux is expressed as $D/F = a^2n_{DS}/c_0$. Temperature enters explicitly into the jump probabilities, thereby becoming an integral part of the overall timescale. Consequently, temperature indirectly influences the external flux through its effect on the timescale. Basing on the expression for diffusion coefficient $D = a^2vn_{DS} \exp(-\beta E_0)$, and because we realize all jumps along terrace with the same rate 1, we can relate temperature difference to $n_{DS}$ as $\Delta\beta = \ln(n_{DS}^{-1})/E_0$. The larger $n_{DS}$ is, the lower $\beta$ value and larger temperature $T$. Additionally, it is important to note that in all our simulations, potential energies $E_V$ and $E_{ES}$ are measured in units of thermal energy $k_BT$.

## 3. Mound formation

### 3.1. Mound Morphologies on Flat Crystal Surfaces

At the flat surface, initially devoid of any steps, the growth process begins through island nucleation. In subsequent stages, nucleation occurs atop existing islands, and this behavior strongly depends on the height of the ES barrier, $E_{ES}$. A high barrier prevents adatoms from descending to lower layers. As a result, adatom density increases on the island tops, promoting upward growth. The influence of the ES barrier height on the resulting surface morphology is illustrated in Fig. 3. All simulations were performed using the same values of $E_V = 1k_BT$ and $c_0 = 0.01$, and the system was evolved for the same number of simulation steps, $t = 10^6$. Results for different values of $n_{DS}$ are compared along the vertical axis. A clear transition can be observed between $E_{ES} = 2k_BT$ and $E_{ES} = 3k_BT$, which appears consistently across all $n_{DS}$ values. Islands form in all cases, but at lower ES barriers, they remain relatively flat. These flatter islands tend to coalesce rather than grow vertically into mounds or pyramidal structures. Closer examination reveals that $E_{ES} = 1k_BT$ is a particularly distinct case. Although this does not imply a smooth surface potential, the resulting surface morphologies for all diffusion rates defined by $n_{DS}$ are limited to a height of one or, at most, two atomic layers. For $E_{ES} = 2k_BT$, islands with greater vertical structure begin to emerge, though they are still relatively low and flat. Interestingly, new layers tend to form on top only when the uppermost terrace becomes nearly as large as the base layer. In contrast, for all systems with $E_{ES} \geq 3k_BT$, islands grow vertically, developing into three-dimensional pyramidal structures with sharp tops. The morphology of these pyramids is strongly influenced by the surface diffusion rate: higher diffusion rates lead to the formation of larger pyramids with broader, more square-shaped bases, whereas lower diffusion rates result in smaller, steeper pyramids with rounded bases. A more detailed examination of the transition from $E_{ES} = 2k_BT$ toward $E_{ES} = 3k_BT$ is presented in Fig. S1 in the Supplementary Material.

In Fig. 4, we illustrate how the shape and size of the grown structures for $E_{ES} = 3k_BT$ depend on the external flux-represented by $c_0$ - and the parameter $n_{DS}$, which can be interpreted as an effective measure of diffusion rate, increasing with temperature. For each $n_{DS}$ separately, the results correspond to the same total number of deposited monolayers. Consequently, for lower adatom concentrations, the system was allowed to evolve for a proportionally longer time to reach the same growth stage. It is evident that lower flux (smaller $c_0$) and higher temperatures (larger $n_{DS}$) favor the development of larger and more extended surface structures that tend to be relatively flat. Nonetheless, in all investigated cases, the surface consistently evolves into a regular mound-like morphology composed of individual units of varying sizes. Importantly, this results in a well-organized, albeit non-planar, surface structure rather than a rough or disordered one.

### 3.2. Meander-to-Mound Morphological Transition on Vicinal Surfaces

We observe that in all cases where growth takes place on an initially smooth surface, the most favorable mode of morphological evolution is the formation of mounds. In contrast, it is well established that the most effective strategy for achieving smooth, well-ordered crystal growth is to employ miscut (vicinal) surfaces. These surfaces, characterized by a regular array of atomic steps, serve as efficient sinks for adatoms and promote a stable, layer-by-layer growth mode. However, when the external particle flux is too high, even vicinal surfaces may lose their smooth morphology and develop mound-like features instead. Simultaneously, it has been demonstrated that the presence of a potential well at the lower side of a step can trigger a strong meandering instability [20]. In general, the growth mode is sensitive to a number of factors, including kinetic barriers, terrace width, and diffusion rates. In what follows, we show that by tuning only the height of the ES barrier, one can induce a smooth and continuous transformation of surface morphology - from regular meandered patterns to fully developed, faceted pyramidal structures. Furthermore, we investigate how these surface patterns are modulated by additional parameters such as the diffusion rate (quantified in our model by the number of diffusional jumps $n_{DS}$, which can also be interpreted as an effective temperature increase), terrace length,

![](./images/1251845489087741961_3.jpg)

Figure 3: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the height of ES barrier $E_{ES}$ for flat surface, $E_V = 1.0k_BT$ and initial particle concentration $c_0 = 0.01$. System size 300 x 400 (in units of the lattice constant) and number of simulation steps $t = 10^6$.

and the initial concentration of mobile adatoms. Previous studies of meander formation [20] revealed that under certain conditions, localized mounds could begin to form at the crest of meandered structures. In this work, we focus specifically on that transitional regime and provide a detailed analysis of the emergence and evolution of such three-dimensional formations. To promote island growth, we employ a relatively high concentration of mobile adatoms ($c_0 = 0.01$) and explore the resulting surface morphologies over a range of ES barrier heights, $E_{ES}/k_BT \in [0.0, 8.0]$.

Figure 5 presents a representative set of patterns obtained under fixed conditions, showing the progressive morphological evolution as the ES barrier increases. As seen in Fig. 5, in the absence of an ES barrier, the final surface exhibits a regular arrangement of steps, typical of stable vicinal growth. Introducing a small barrier leads to the onset of step meandering, which becomes increasingly pronounced as the barrier height increases. At intermediate barrier values, we observe a qualitative change in surface morphology: the regular meanders give way to the formation of 3D mounds. Further increasing $E_{ES}$ results in enhanced vertical growth and sharper, more faceted pyramidal structures. These observations underline the crucial role of the ES barrier in controlling the transition from two-dimensional instabilities to fully developed three-dimensional surface features. The change in the shape of the surface structures is observed to occur within the range of $E_{ES}$ between 2 and 3. To better understand this transition, we performed a more detailed analysis within this interval of barrier heights. The corresponding results are presented in Figure 6. As evident from the figure, the transition from meandered patterns to pyramidal structures occurs in a continuous and gradual manner. As the height of the ES barrier increases, small islands begin to form on the crests of the meanders. These islands act as nucleation sites for the vertical growth of three-dimensional structures. Initially, the surface exhibits a hybrid morphology-intermediate between meanders and pyramids-as shown in Figures 6c-e. With further increase of $E_{ES}$, the structures become more distinctly three-dimensional, as seen in Figure 5e, marking the full development of faceted pyramidal features.

The transformations discussed above were obtained for a relatively low diffusion rate, with $n_{DS} = 5$. In

![](./images/1251845489087741961_4.jpg)

Figure 4: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the initial particle concentration $c_0$ for flat surface, $E_V = 1.0k_BT$ and $E_{ES} = 3.0k_BT$. The structures are presented for the same number of layers for each $n_{DS}$ separately and equal to 282, 406, 267, 157 layers for $n_{DS}=2,5,10$ and 20 respectively. System size 300 x 400.

Fig. 7, we examine how increasing the number of dif- fusional jumps, $n_{DS}$, affects the resulting surface mor- phologies. Specifically, we investigated the evolution of 3D structures as a function of $n_{DS}$ in the range from 1 to 20. As shown in the top panel of Fig. 7, increasing the diffusion rate has a significant impact on the surface morphology. At low values of $n_{DS}$, the system forms densely packed, steep pyramidal structures. As $n_{DS}$ in- creases, these structures begin to elongate and lose their vertical symmetry. Eventually, for sufficiently high dif- fusion rates, the pattern evolves back into a meander- like configuration. This recovery of meanders at high diffusivity highlights the delicate balance between the ES barrier and adatom mobility in determining the final surface morphology.

### 3.3. Characterization of pattern formation by using the height-height correlation function

The height-height correlation function $C(r)$ is used as a powerful tool for characterizing surface patterns. It measures the average squared height difference between two surface points $i$ and $j$, separated by a distance $r = r_i - r_j$, and is defined as:

$$
\begin{aligned}
C(r) = C(r_i - r_j) &= \langle [h(r_i) - h(r_j)]^2 \rangle = \\
&= \langle [h(x_i, y_i) - h(x_j, y_j)]^2 \rangle.
\end{aligned} \tag{4}
$$

In order to characterize the anisotropic evolution of the surface morphology, it is convenient to evaluate the correlation function along the $x$ and $y$ directions separately using the following expressions:

$$
C_x(x) = \frac{1}{(L_x - x)L_y} \sum_{k=1}^{L_x - x} \sum_{l=1}^{L_y} [h(k + x, l) - h(k, l)]^2, \tag{5}
$$

$$
C_y(y) = \frac{1}{L_x(L_y - y)} \sum_{k=1}^{L_x} \sum_{l=1}^{L_y - y} [h(k, l + y) - h(k, l)]^2, \tag{6}
$$

where $C_x$ and $C_y$ denote the correlation functions in the directions across and along the steps, respectively; $L_x = 300$ and $L_y = 400$ are the system sizes; $x$ and $y$ are distances varying from 1 up to half the system size in the corresponding direction. Each correlation function is averaged over the orthogonal direction, ensuring full sampling of the surface.

![](./images/1251845489087741961_5.jpg)

Figure 5: Structures obtained for $n_{DS}=5$, $c_{0}=0.01$, $l_{0}=10$, $E_{V}=2.0k_{B}T$ and a) $E_{ES}=0.0$, b) $E_{ES}=1.0k_{B}T$, c) $E_{ES}=2.0k_{B}T$, d) $E_{ES}=3.0k_{B}T$, e) $E_{ES}=4.0k_{B}T$. Simulation time $10^{6}$. System size 300 x 400.

![](./images/1251845489087741961_6.jpg)

Figure 6: Structures obtained for $n_{DS}=5$, $c_{0}=0.01$, $l_{0}=10$, $E_{V}=1.0k_{B}T$, and a) $E_{ES}=2.2k_{B}T$, b) $E_{ES}=2.4k_{B}T$, c) $E_{ES}=2.5k_{B}T$, d) $E_{ES}=2.6k_{B}T$, e) $E_{ES}=2.8k_{B}T$. Simulation time $10^{6}$. System size $300 \times 400$.

Two characteristic lengths of the surface morphol-ogy can be extracted from the correlation function: the wavelength $\lambda$ and the amplitude $A$. These quantities describe the lateral periodicity and vertical modulation of the surface, respectively. For meandered structures, the most relevant parameter is the wavelength $\lambda$, whereas mounded structures are characterized by both their lateral size (given by the correlation length) and their amplitude $A$. The wavelength $\lambda$ is determined as the position of the first minimum of $C(r)$, while the amplitude $A$ corresponds to its first maximum. Both quantities are calculated separately along the $x$ and $y$ directions. In addition, the results are averaged over ten independent realizations.

The behavior of correlation functions $C_{x}$ and $C_{y}$, computed along the $x$ and $y$ axes, is presented in the bottom panel of Fig. 7 for structures obtained at different numbers of diffusional jumps $n_{DS}$, varying from 1 to 20. These results correspond to the surface morphologies shown in the top panel of the same figure. As $n_{DS}$ increases, the surface morphology evolves from compact mounds, through an intermediate state, towards well-developed meanders. This transformation is clearly reflected in the correlation functions: initially isotropic mounds exhibit nearly identical $C_{x}$ and $C_{y}$, while intermediate states display similar amplitudes but different correlation lengths. For high $n_{DS}$ values, the functions separate into two distinct behaviors - $C_{y}$ with a pronounced amplitude and wavelength, and $C_{x}$ nearly flat - characteristic of a regular step meandered pattern. Similar shape of the height-height correlation function was shown in Ref. [12] for mounded structures. Additionally, in Fig. S2 in the Supplementary Material we present a comparison of the correlation functions and the corresponding structures grown at different diffusion rates $n_{DS}$ on vicinal and flat surfaces, respectively.

The dependence of the main morphological characteristics $\lambda$ and $A$ on the two key parameters - the Ehrlich-Schwoebel barrier height $E_{ES}$ and the diffusion rate $n_{DS}$ - is summarized in Fig. 8. Three regimes can be identified from these plots: meandered, intermediate, and mounded. In contrast, the analogous dependence obtained for a flat surface (presented in Fig. S3) reveals only the mounded regime. As can be seen, the mounds are characterized with almost the same wavelengths and amplitudes in both directions, typically for isotropic structures. In the intermediate regime, when a mixture of mounds and meanders emerges, both morphological characteristics $\lambda$ and $A$ change drastically and synchronically in both directions. Whereas the regular meanders can be clearly identified in the significant difference between the wavelengths $\lambda_{x}$ and $\lambda_{y}$ along both directions and the small amplitudes, underlining the anisotropic character of the structure.

In addition, the time evolution of the correlation functions for regular mounded, regular meandered and mixed structure is provided in the Supplementary Material (see Fig. S4). Moreover, the time-scaling behavior

![](./images/1251845489087741961_7.jpg)

Figure 7: Top panel: Structures obtained for $c_0 = 0.01$, $l_0 = 10$, $E_V = 1.0k_BT$, $E_{ES} = 3.0k_BT$ and a) $n_{DS} = 1$, b) $n_{DS} = 2$, c) $n_{DS} = 5$, d) $n_{DS} = 10$, e) $n_{DS} = 20$. Bottom panel: Behavior of correlation functions $C_x$ and $C_y$, calculated along x-axis (across steps) and y-axis (along steps) respectively, for different number of diffusional jumps $n_{DS}$ corresponding to the morphological structures presented in the top panel. Simulation time $10^6$. System size 300 x 400.

![](./images/1251845489087741961_8.jpg)

Figure 8: Influence of diffusion rate $n_{DS}$ (a) and Ehrlich-Schwoebel barrier $E_{ES}$ (b) on the main morphological characteristics $\lambda$ and $A$ calculated from correlation functions along x- and y-axis separately. Regions corresponding to different morphological structures are marked in different colors.

of the main characteristic lengths along both directions - the wavelengths $\lambda_x$ and $\lambda_y$, and the amplitudes $A_x$ and $A_y$, is presented for different diffusion rate $n_{DS}$ in Fig. S5 in the Supplementary Material. Their evolution can be described by the following scaling relations:

$$
\lambda \sim t^{1/z}, \tag{7}
$$

$$
A \sim t^{\beta}, \tag{8}
$$

with scaling exponents $1/z$ and $\beta$ listed in Tables 1 and 2, respectively, for structures grown at different diffusion rates $n_{DS}$ on both vicinal and flat surfaces. Note that for meandered structures grown on vicinal surface the correlation function across the step direction exhibits very small amplitude and an ill-defined wavelength (see Fig. 7e, bottom panel). However, $\lambda_y$ and $A_y$ measured along step direction allow for distinguishing the different growth regimes, highlighting the contrasting dynamical evolution of meanders and mounds. According to Ref. [29], in the case of a square lattice, the coarsening exponent - also referred as the dynamic exponent $1/z$ - should be equal to 0.25. Indeed, we obtained this value for a flat surface. Rost et al. claim in their paper [10] that the same value should apply to flat and vicinal surfaces. Based on our results, we observe that this only occurs in mounded and mixed regions. For high values of $n_{DS}$, for which the meanders are observed on vicinal surface, the exponents are obviously different. This is correlated with elongation of the structure in one direction, which causes more distinguishable directions for meanders. Traces of the influence of direction

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">1/z</th>
</tr>
<tr>
<th colspan="2">vicinal surface</th>
<th>flat surface</th>
</tr>
<tr>
<th>$n_{DS}$</th>
<th>$x$</th>
<th>$y$</th>
<th>$x=y$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.33</td>
<td>0.2</td>
<td>0.2</td>
</tr>
<tr>
<td>2</td>
<td>0.33</td>
<td>0.2</td>
<td>0.2</td>
</tr>
<tr>
<td>5</td>
<td>0.5</td>
<td>0.25</td>
<td>0.25</td>
</tr>
<tr>
<td>10</td>
<td>0.5</td>
<td>0.25</td>
<td>0.25</td>
</tr>
<tr>
<td>15</td>
<td>0.75</td>
<td>0.4</td>
<td>0.25</td>
</tr>
<tr>
<td>20</td>
<td>0.75</td>
<td>0.4</td>
<td>0.25</td>
</tr>
</tbody>
</table>

Table 1: The dynamic exponent $1/z$ calculated separately across (x) and along (y) the steps for structures grown at different diffusion rates $n_{DS}$ on vicinal and flat surfaces. The margin of error is 0.05.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">$\beta$</th>
</tr>
<tr>
<th colspan="2">vicinal surface</th>
<th>flat surface</th>
</tr>
<tr>
<th>$n_{DS}$</th>
<th>$x$</th>
<th>$y$</th>
<th>$x=y$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1.8</td>
<td>1.8</td>
<td>1.8</td>
</tr>
<tr>
<td>2</td>
<td>1.8</td>
<td>1.8</td>
<td>1.9</td>
</tr>
<tr>
<td>5</td>
<td>1.25</td>
<td>1.25</td>
<td>2</td>
</tr>
<tr>
<td>10</td>
<td>1.25</td>
<td>1.25</td>
<td>2</td>
</tr>
<tr>
<td>15</td>
<td>1.1</td>
<td>1.1</td>
<td>2</td>
</tr>
<tr>
<td>20</td>
<td>0.75</td>
<td>1.1</td>
<td>2</td>
</tr>
</tbody>
</table>

Table 2: The growth exponent $\beta$ calculated separately across (x) and along (y) the steps for structures grown at different diffusion rates $n_{DS}$ on vicinal and flat surfaces. The margin of error is 0.05.

are also visible in the other two regions, particularly in the mixed region for the vicinal surface. The analysis of the growth exponent $\beta$, which is correlated with the roughening exponent found in the literature, reveals different growth behavior for vicinal surfaces. Mounded structures grow similarly on vicinal and flat surfaces. However, when the growth regime changes to mixed or meandered, the growth exponents also change.

### 3.4. Morphology diagrams

A key observation can be summarized as follows: the meandered surface patterns evolves into a mounded landscape as the height of the ES barrier $E_{ES}$ increases. Remarkably, this trend can be reversed by enhancing the surface diffusion. In other words, a system that develops mounded structures at moderate diffusion rates may revert to a meandered morphology once diffusion becomes sufficiently fast.

This interplay is captured in Fig. 9, which maps the observed surface patterns as a function of the number of diffusional jumps $n_{DS}$ and the ES barrier height $E_{ES}$. As the diagram shows, the critical ES barrier required for the meander-to-mound transition shifts to higher values with increasing $n_{DS}$. For small $E_{ES}$, meandered structures always appear, irrespective of the diffusion rate. The transition line separating the two regimes can be approximately expressed as:

$$
\sqrt{n_{DS}} \exp(-\beta E_{ES}) = \text{const.} \tag{9}
$$

This scaling relation highlights that the destabilizing effect of the ES barrier can be counterbalanced by enhanced adatom mobility. At large $n_{DS}$, a particle can perform many surface jumps before incorporation into the crystal, effectively overcoming even a sizable ES barrier. In this way, higher diffusion not only increases lateral transport but also enhances step permeability, enabling adatoms to cross step edges instead of being trapped. As a result, the system recovers meander-like morphologies instead of mounded ones.

Another key parameter that significantly influences surface nucleation - and therefore plays a central role in pattern formation - is the adparticle density $c_0$. This parameter can be interpreted as the flux of particles arriving at the surface. In Fig. 10, we present how the surface morphology evolves as a function of both the number of diffusional jumps $n_{DS}$ and the initial adparticle concentration $c_0$. The simulation time was normalized such that the same number of monolayers was deposited in each case. The diagram reveals that higher values of $c_0$ tend to promote mound formation, while increasing $n_{DS}$ leads to smoother surfaces and supports the emergence of meandered structures. The transition between these two growth regimes - meanders and mounds - can be approximately described by the relation:

$$
\sqrt{n_{DS}} c_0^{-1} = \text{const.}, \tag{10}
$$

indicating that $c_0$ acts in a manner analogous to the ES barrier. A higher particle flux (i.e., higher $c_0$) reduces the effective mobility of adatoms, favoring mound formation in a way similar to an increased ES barrier. Interestingly, surface patterns located near the transition line (just below the meander-to-mound boundary) exhibit a characteristic and reproducible morphology. These structures typically consist of rectangular mounds, elongated in the direction perpendicular to the steps, indicating a well-defined intermediate regime between meanders and fully developed pyramids.

In all of the previously discussed examples, we kept the depth of the potential energy well fixed at $E_V = 1\ k_BT$. Generally, the primary control parameter governing the transition between meandered and mounded surface morphologies is the height of the ES barrier, $E_{ES}$, rather than the depth of the potential well, $E_V$. However, $E_V$ significantly influences the wavelength of the meanders, as analyzed in detail in Ref.[20]. In

![](./images/1251845489087741961_9.jpg)

Figure 9: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the height of ES barrier $E_{ES}$ for $c_0 = 0.01$, $l_0 = 10$,and $E_V = 1.0k_BT$. Simulation time $10^6$. System size 300 x 400.

Fig.11, we illustrate how variations in the potential well depth affect the shape of mounds and alter the characteristics of the intermediate regime between meanders and mounds. It can be observed that for high diffusion rates (i.e., large $n_{DS}$), the surface remains in a meandered state even at large values of $E_V$. Nevertheless, increasing $E_V$ leads to a noticeable decrease in the meander wavelength and the appearance of secondary wave-like modulations along the sides of the primary finger-like structures. Interestingly, similar meander morphologies are found even at lower diffusion rates, provided the potential well is sufficiently deep. Regular mound-like structures reappear only when the diffusion rate is very low and/or the potential well is shallow.

## 4. Conclusions

In this work, we have systematically investigated surface pattern formation during epitaxial growth, focusing on the transition between meandered and mounded morphologies and vice versa. Using VicCA simulations, we examined how surface evolution depends on four key parameters: the ES barrier height $E_{ES}$, the number of diffusional jumps $n_{DS}$ representing surface mobility, the adatom concentration $c_0$ linked to deposition flux, and the potential well depth $E_V$ reflecting the strength of interatomic interactions. The transition from mounds to meanders is reflected in the anisotropy of the height-height correlation function used for quantitatively describing the surface morphologies.

We showed that increasing $E_{ES}$ suppresses adatom descent, promoting vertical growth and driving the transition from smooth, meandered structures to fully developed pyramidal mounds. This transition occurs gradually and is accompanied by the appearance of intermediate morphologies, such as elongated mounds oriented perpendicular to the steps. The competition between surface diffusion and the ES barrier is decisive: increasing $n_{DS}$ restores meandered structures even at high $E_{ES}$, demonstrating that enhanced surface mobility counteracts kinetic roughening. The transition follows a scaling law of the form $\sqrt{n_{DS}} \exp(-\beta E_{ES}) = \text{const}$. A similar trend is observed with varying adatom flux. Increasing $c_0$ favors mound formation, while higher $n_{DS}$ has the opposite effect, leading to the approximate scaling relation $\sqrt{n_{DS}} c_0^{-1} = \text{const}$. Although $E_V$ does not directly control the meander-to-mound transition, it strongly influences the wavelength and modulation of meander patterns, es-

![](./images/1251845489087741961_10.jpg)

Figure 10: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the initial particle concentration $c_0$ for $l_0 = 10$, $E_V = 1.0k_BT$ and $E_{ES} = 3.0k_BT$. The structures are presented for the same number of layers for each $n_{DS}$ separately and equal to 293, 357, 372, 449 layers for $n_{DS} = 2, 5, 10$ and 20 respectively. System size 300 x 400.

pecially at high diffusion rates.

Altogether, these results reveal that a wide spectrum of surface morphologies - from step patterns and mean- ders to sharp three-dimensional pyramids - can be sys- tematically tuned by adjusting basic growth parameters. In particular, the existence of an intermediate morpho- logical regime offers a potential pathway for nanoscale surface design.

The scaling laws and transitions identified here pro- vide experimentally testable predictions for molecular beam epitaxy (MBE) and related growth techniques. In practice, $E_{ES}$ can be tuned through material choice or surfactant-mediated growth, while $n_{DS}$ and $c_0$ can be controlled by adjusting temperature and deposition flux, respectively. This establishes a direct link between our simulations and realistic experimental conditions, en- abling exploration of the predicted morphological phase diagram.

Future work may extend this study by incorporat- ing additional physical effects such as step permeabil- ity, anisotropic diffusion, or strain. In particular, the coupling between elastic interactions and step mean- dering remains an open problem, with implications for thin-film stress relaxation and pattern selection. Experi- mental validation, for instance through real-time surface imaging, would provide valuable confirmation of our predictions and could ultimately guide the rational de- sign of nanoscale surface architectures via kinetic con- trol.

## Acknowledgments

The authors express their gratitude to The Polish Na- tional Center for Research and Development (grant no. EIG CONCERT-JAPAN/9/56/AtLv-AlGaN/2023), The Bulgarian National Science Fund (grant No. KP-06- DO02/2/18.05.2023), the Polish Academy of Sciences and the Bulgarian Academy of Sciences (grant No. IC-PL/07/2024-2025) for providing financial support. They also extend their thanks to Vesselin Tonchev from the Faculty of Physics at Sofia University and Yoshi- hiro Kangawa from the Research Institute for Applied Mechanics at Kyushu University for their valuable dis- cussions. Most of the calculations were done on HPC facility Nestum (BG161PO003-1.2.05).

![](./images/1251845489087741961_11.jpg)

Figure 11: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the depth of the potential well $E_V$ for $l_0=10$, $c_0=0.01$ and $E_{ES}=3.0k_BT$. Simulation time $10^6$. System size 300 x 400.

### Author contributions: CRediT

Marta A. Chabowska: Conceptualization, Data cura- tion, Formal analysis, Investigation, Methodology, Val- idation, Visualization, Writing - original draft, Writ- ing - review and editing; Hristina Popova: Data cura- tion, Formal analysis, Investigation, Validation, Visual- ization, Writing - original draft, Writing - review and editing; Magdalena A. Załuska - Kotur: Conceptualiza- tion, Formal analysis, Investigation, Methodology, Val- idation, Writing - original draft, Writing - review and editing.

### References

[1] Damilano B., Aristégui R., Teisseyre H., Vézian S., Guigoz V., Courville A., Florea I., Vennéguès P., Bockowski M., Guillet T., Vladimirova M., Molecular beam epitaxy of GaN/AlGaN quantum wells on bulk GaN substrate in the step-flow or step meandering regime: Influence on indirect ex- citon diffusion, J. Appl. Phys. 135 (2024) 095702.

[2] Chou T.-S., Akhtar A., Bin Anooz S., Rehm J., Ernst O., Seyidov P., Fiedler A., Miller W., Galazka Z., Remmele T., Albrecht M., Popp A., Influencing the morphological stability of MOVPE-grown $\beta$-Ga₂O₃ films by O₂/Ga ratio, Appl. Surf. Sci. 660 (2024) 159966.

[3] Wu Y.-Z., Liu B., Li Z.-H., Tao T., Xie Z.-L., Xiu X.-Q., Chen P., Chen D.-J., Lu H., Shi Y., Zhang R., Zheng Y.-D., Homo-epitaxial growth of high crystal quality GaN thin films by plasma assisted - molecular beam epitaxy, J Cryst. Growth 506 (2019) 30 - 35.

[4] Gocalinska A., Rubini S., Pelucchi E., Native ox- ides formation and surface wettability of epitaxial III-V materials: The case of InP and GaAs, Appl. Surf. Sci. 383 (2016) 19-27.

[5] Pandey A., Singh V. K., Dalal S., Bag R. K., Narang K., Kaur D., Raman R., Tyagi R., Effect of two step GaN buffer on the structural and electri- cal characteristics in AlGaN/GaN heterostructure, Vacuum 178 (2020) 109442.

[6] Uesugi K., Kuboya S., Shojiki K., Xiao S., Nakamura T., Kubo M., Miyake H., 263 nm wavelength UV-C LED on face-to-face annealed

sputter-deposited AlN with low screw- and mixed- type dislocation densities, Appl. Phys. Express 15 (2022) 055501. https://doi.org/10.35848/1882-0786/ac66c2

[7] Michely T., Krug J., Islands, mounds and atoms, Springer, Berlin, 2004.

[8] Siegert M., Plischke M., Slope Selection and Coarsening in Molecular Beam Epitaxy, Phys. Rev. Lett. 73 (1994) 1517.

[9] Chakrabarti B., Dasgupta Ch., Mound formation and coarsening from a nonlinear instability in sur- face growth, Phys. Rev. E 69 (2004) 011601.

[10] Rost M., Šmilauer P., Krug J., Unstable epitaxy on vicinal surfaces, Surf. Sci. 369 (1996) 393.

[11] Bryan I., Bryan Z., Mita S., Rice A., Tweedie J., Collazo R., Sitar Z., Surface kinetics in AlN growth: A universal model for the control of sur- face morphology in III-nitrides, J. Cryst. Growth 438 (2016) 81-89.

[12] Evans J. W., Thiel P. A., Bartelt M. C., Morpho- logical evolution during epitaxial thin film growth: Formation of 2D islands and 3D mounds, Surface Science Reports 61 (2006) 1-128.

[13] Bartelt M. C., Evans J. W., Transition to Mul- tilayer Kinetic Roughening for Metal (100) Ho- moepitaxy, Phys. Rev. Lett. 75 (1995) 4250.

[14] Tejedor P., Šmilauer P., Roberts C., Joyce B. A., Surface-morphology evolution during unstable homoepitaxial growth of GaAs(110), Phys. Rev. B 59 (1999) 2341.

[15] Leal F. F., Ferreira S. C., Ferreira S. O., Mod- elling of epitaxial film growth with an Ehrlich- Schwoebel barrier dependent on the step height, J. Phys.: Condens. Matter 23 (2011) 292201.

[16] Schneider J. P., Margetis D., Gibou F., Ratsch Ch., An examination of scaling behavior in unstable epitaxial mound growth via kinetic Monte Carlo simulations, J. Phys.: Condens. Matter 31 (2019) 365301.

[17] Wollschläger J., Larsson M. I., Step barrier ef- fects during early stages of the kinetic roughening of fcc(111) surfaces, J. Vac. Sci. Technol. A 40 (2022) 013210.

[18] Punyindu Chatraphorn P., Toroczkai Z., Das Sarma S., Epitaxial mounding in limited-mobility models of surface growth, Phys. Rev. B 64 (2001) 205407.

[19] Munko F., Cruz Luukkonen C., Carrasco I. S. S., Aarão Reis F. D. A., Oettel M., Island formation in heteroepitaxial growth, Phys. Rev. E 111 (2025) 035501.

[20] Chabowska M. A., Popova H., Załuska-Kotur M. A., Step meandering: Balance between the potential well and the Ehrlich - Schwoebel barrier, Phys. Rev. B 111 (2025) 155401. https://doi.org/10.1103/PhysRevB.111.155401.

[21] Załuska-Kotur M., Popova H., Tonchev V., Step Bunches, Nanowires and Other Vicinal "Creatures" - Ehrlich - Schwoebel Effect by Cellular Automata, Crystals 11 (2021) 1135. https://doi.org/10.3390/cryst11091135.

[22] Chabowska M. A., Załuska-Kotur M. A., Diffusion-Dependent Pattern Formation on Crys- tal Surfaces, ACS Omega 8 (2023) 45779-45786. https://doi.org/10.1021/acsomega.3c06377.

[23] Chabowska M. A., Załuska-Kotur M. A., Surface Patterns Shaped by Additives in Crystals, Vacuum 240 (2025) 114431.

[24] Chabowska M. A., Załuska-Kotur M. A., En- gineering 2D surface patterns with the VicCa model, J. Cryst. Growth 667 (2025) 128245. https://doi.org/10.1016/j.jcrysgro.2025.128245

[25] Ohka T., Akiyama T., Muizz Pradipto A., Naka- mura K., Ito T., Effect of Step Edges on Ad- sorption Behavior for GaN(0001) Surfaces during Metalorganic Vapor Phase Epitaxy: An Ab Initio Study, Cryst. Growth Des. 20 (2020) 4358.

[26] Akiyama T., Ohka T., Nakamura K., Ito T., Ab ini- tio study for adsorption and desorption behavior at step edges of GaN (0001) surface, J. Cryst. Growth 532 (2020) 125410.

[27] Akiyama T., Ohka T., Nagai K., Ito T., Effect of step edges on the adsorption behavior on vici- nal AlN(0001) surface during metal-organic vapor phase epitaxy: An ab initio study, J. Cryst. Growth 571 (2021) 126244.

[28] Akiyama T., Kawamura T., Ab initio study for ad- sorption behavior on AlN(0001) surface with steps

and kinks during metal-organic vapor-phase epi- taxy, Jpn. J. Appl. Phys. 63 (2024) 02SP71.

[29] Golubović L., Levandovsky A., Moldovan D., Interface Dynamics and Far-From-Equilibrium Phase Transitions in Multilayer Epitaxial Growth and Erosion on Crystal Surfaces: Continuum The- ory Insights, East Asian J. Appl. Math. 1 (2011) 297.

## 5. Supplementary Material

In this supplement we provide the additional figures.

Figure **S1** presents a diagram of patterns grown on flat surface as a function of number of diffusional jumps $n_{DS}$ with a more detailed examination of the morphological transition controlled by the height of the Ehrlich-Schwoebel (ES) barrier from $E_{ES}=2k_BT$ toward $E_{ES}=3k_BT$.

Figure **S2** provides a comparison of the correlation functions $C(r)$ calculated along $x$- and $y$-axis separately for three-dimensional (3D) structures grown at different diffusion rates on vicinal and flat surfaces, respectively.

Analyzing the mounded morphologies on flat surface, Figure **S3** demonstrates the influence of the diffusion rate $n_{DS}$ on the main morphological characteristics of mounds, (lateral) wavelength $\lambda$ and (vertical) amplitude $A$, which are calculated from correlation functions along $x$- and $y$-axis separately. Typical of isotropic mounds, each of the characteristics has the same behavior in both directions. However, for large mounds (with lateral size $\lambda$ larger than the half of the system size in particular direction) the finite-size effect of the system must be taken into account causing a small deviation in the results.

Figures **S4** and **S5** present the results obtained for a vicinal surface. Figure **S4** shows the correlation functions $C_x(x)$ and $C_y(y)$ for different time moments $t$ describing the evolution of the surface morphology and the corresponding characteristic lengths along both directions. The separate graphs represent different values of $n_{DS}$ demonstrating the evolution of structures consisting of regular mounds, regular meanders and a mix of both.

Figure **S5** presents the time scaling of the wavelengths $\lambda$ and the amplitudes $A$ in both directions for structures grown at different diffusion rate $n_{DS}$ on vicinal surface. The dynamics of the crystal surface is characterized by scaling exponents describing the increase of the wavelength $\lambda \sim t^{1/z}$ and the increase of the amplitude $A \sim t^\beta$ during the growth process. Note that both scaling exponents, $1/z$ and $\beta$, are measured in different time intervals corresponding to the steadily increase of the particular characteristic length. Initially both wavelengths, $\lambda_x$ and $\lambda_y$, exhibit fast increase in time, while the amplitude stays almost constant and low, which implies mainly lateral growth. Later in time, the amplitude starts to grow drastically, indicating vertical growth and the increase in surface roughness, in contrast to the wavelengths in both directions which remain almost the same. Therefore, coarsening (coalescing) of mounds or meanders is observed in the initial stage of the growth process, and further surface roughening appears in the late stage. Although the scaling dynamics slightly differs in $x$ and $y$ direction, the transition from mounds to meanders by increasing of $n_{DS}$ is reflected in the change of all scaling exponents, such that the dynamic (coarsening) exponent $1/z$ increases and the growth (roughness) exponent $\beta$ decreases simultaneously in both directions.

![](./images/1251845489087741961_12.jpg)

Figure S1: Diagram of different surface patterns presented as a function of number of diffusional jumps $n_{DS}$ dependent on the height of ES barrier $E_{ES}$ for flat surface, $E_V=2.0k_BT$ and initial particle concentration $c_0=0.01$. System size 300 x 400 and number of simulation steps $t=10^6$.

![](./images/1251845489087741961_13.jpg)

Figure S2: Comparison of the correlation functions calculated along $x$- and $y$-axis for 3D structures grown on vicinal and flat surfaces (top and bottom panel, respectively) for different diffusion rates $n_{DS}$ (shown in the legend). Other system parameters are: $c_0=0.01, l_0=10$ (for vicinal surface), $E_V=1k_BT, E_{ES}=3k_BT$, simulation time $10^6$, and system size 300 x 400. The corresponding surface morphologies are also presented.

![](./images/1251845489087741961_14.jpg)

Figure S3: Influence of diffusion rate $n_{DS}$ on the main morphological characteristics $\lambda$ and $A$ calculated along $x$- and $y$-axis separately for mounds grown on flat surface. Other system parameters are: $c_0 = 0.01, E_V = 1k_BT, E_{ES} = 3k_BT$, simulation time $10^6$, and system size 300 x 400.

![](./images/1251845489087741961_15.jpg)

Figure S4: Correlation functions $C_x(x)$ (top panel) and $C_y(y)$ (bottom panel) for vicinal surface presented for different time moments $t$ as indicated in the legend, demonstrating the evolution of mounded structure (in the left, for $n_{DS} = 1$), structure consisting simultaneously of mounds and meanders (in the middle, for $n_{DS} = 5$) and meandered structure (in the right, for $n_{DS} = 20$). Other system parameters are: $c_0 = 0.01, l_0 = 10, E_V = 1k_BT, E_{ES} = 3k_BT$. System size is 300 x 400. Positions of the first minimum and the first maximum of the correlation functions, corresponding to the characteristic lengths $\lambda$ and $A$, are marked on each curve to easily track their evolution.

![](./images/1251845489087741961_16.jpg)

Figure S5: Time scaling of the main characteristic lengths - the wavelengths $\lambda_x$ and $\lambda_y$ (top panel) and the amplitudes $A_x$ and $A_y$ (bottom panel) for structures grown at different diffusion rate $n_{DS}$ on vicinal surface. Time-scaling relations of characteristic lengths and their corresponding scaling exponents are shown in the legends. System parameters are: $c_0=0.01, l_0=10, E_V=1k_BT, E_{ES}=3k_BT$. System size is 300 x 400.