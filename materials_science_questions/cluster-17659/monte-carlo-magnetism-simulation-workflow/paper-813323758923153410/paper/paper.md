Domain dynamics and fluctuations in artificial square ice at finite temperatures

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2012 New J. Phys. 14 035014

(http://iopscience.iop.org/1367-2630/14/3/035014)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 137.30.242.61
This content was downloaded on 01/06/2015 at 15:34

Please note that terms and conditions apply.

![](./images/813323758923153410_1.jpg)

# Domain dynamics and fluctuations in artificial square ice at finite temperatures

Z Budrikis$^{1,2,8}$, K L Livesey$^{1,3}$, J P Morgan$^{4}$, J Akerman$^{4,5}$, A Stein$^{6}$, S Langridge$^{7}$, C H Marrows$^{4}$ and R L Stamps$^{2}$

$^{1}$ School of Physics, The University of Western Australia, 35 Stirling Hwy, Crawley 6009, Australia
$^{2}$ SUPA School of Physics and Astronomy, University of Glasgow, Glasgow G12 8QQ, UK
$^{3}$ Department of Physics and Energy Science, University of Colorado, Colorado Springs, CO 80918, USA
$^{4}$ School of Physics and Astronomy, University of Leeds, Leeds LS2 9JT, UK
$^{5}$ Instituto de Sistemas Optoelectrónicos y Microtecnología (ISOM), Universidad Politécnica de Madrid
$^{6}$ Center for Functional Nanomaterials, Brookhaven National Laboratory, Upton, NY 11973, USA
$^{7}$ ISIS, Rutherford Appleton Laboratory, Chilton OX11 0QX, UK

E-mail: zoe.budrikis@gmail.com

New Journal of Physics 14 (2012) 035014 (20pp)
Received 16 December 2011
Published 20 March 2012
Online at http://www.njp.org/
doi:10.1088/1367-2630/14/3/035014

Abstract. The thermally driven formation and evolution of vertex domains is studied for square artificial spin ice. A self-consistent mean-field theory is used to show how domains of ground state ordering form spontaneously, and how these evolve in the presence of disorder. The role of fluctuations is studied using Monte Carlo simulations and analytical modelling. Domain wall dynamics are shown to be driven by a biasing of random fluctuations towards processes that shrink closed domains, and fluctuations within domains are shown to generate isolated small excitations, which may stabilize as the effective temperature is lowered. Domain dynamics and fluctuations are determined by interaction strengths, which are controlled by inter-element spacing. The role of interaction strength is studied via experiments and Monte Carlo simulations. Our mean-field model is applicable to ferroelectric 'spin' ice, and we show that features similar

$^{8}$ Author to whom any correspondence should be addressed.

New Journal of Physics 14 (2012) 035014
1367-2630/12/035014+20$33.00

© IOP Publishing Ltd and Deutsche Physikalische Gesellschaft

to those of magnetic spin ice can be expected, but with different characteristic temperatures and rates.

### Contents

1.  Introduction 2
2.  Magnetization processes in mean-field approximation 4
3.  Fluctuations and disorder 8
    3.1. Spacing and interaction strength . . . . . . . . . . . . . . . . . . . . . . . 12
    3.2. Fluctuations and clusters . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.  Conclusion 16
Acknowledgments 17
Appendix. Ferroelectric ice 17
References 19

## 1. Introduction

Artificial spin ices [1] are constructed as finite arrays of elongated magnetic dots whose magnetizations are assumed to be well approximated by Ising spins. The stray magnetostatic fields of each island mediate interactions, which are frustrated by geometry. These systems are called ‘ices’ because minimization of the magnetostatic energy leads to behaviour resembling that governed by the ice rule for the ground state of solid water, i.e. two-in, two-out spin configurations [2].

The geometry of artificial spin ices can be controlled to a large extent [3–7], and resulting magnetic configurations can be imaged directly using techniques such as magnetic force microscopy [1, 8–11], x-ray photoemission electron microscopy [5, 12, 13] and Lorentz transmission electron microscopy [4, 14]. Most studies have been conducted at room temperature with relatively large, thermally stable magnetic elements. This thermal stability is enforced by choosing island volumes large enough that the barrier to magnetization reversal, primarily associated with shape anisotropy, is much higher than room temperature, so that dynamics can only be induced by applying a magnetic field. Spatial studies are then conducted with the system in a steady state configuration.

Because the focus to date has been on athermal systems, very little is known about how two-dimensional (2D) spin ice arrays respond to thermal fluctuations. Recent reports provide evidence that there are magnetic features visible in as-grown arrays that form during early stages of growth [10], namely long-range ground state ordering, with well-defined domain walls and small clusters representing configurational excitations above the ground state. The origin of the ordering and excitations was argued to be thermal. In another recent work, thermal loss of macro-spin order was reported in a square artificial spin ice patterned $\delta$-doped Pd(Fe) film [15].

From a theoretical perspective, simulation studies [16] of an analogue of square ice constructed from charged colloids in double-well optical traps reveal a freezing transition as the temperature is reduced relative to the height of the barriers between pairs of wells. The same authors also find [17] that strong thermal noise is required to alter the hysteretic behaviour of the system. Recently, Monte Carlo simulations of magnetic square ice have been presented [18],

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_2.jpg)

Figure 1. (a) Examples of each of the four vertex types. The symbols in the centres of vertices I–III are used later in the text to indicate the vertex type. (b) Geometry of the square artificial spin ice in this paper. Finite range interactions are assumed and indicated on the diagram.

which indicate a sharp peak in the specific heat and a peak in the density of closed loops of spins flipped against the ground state at approximately the same temperature. Work has also been done to characterize the dynamics during quenches of generalized vertex models [19].

In this paper, we discuss configurational dynamics of square artificial spin ice in terms of macro-domain growth and boundary movements at finite temperatures. The picture we present is one in which domain boundaries can flow, and also form channels over which magnetically charged vertices move. We find that a domain of ground state configuration should, in the absence of disorder, spontaneously grow until it fills the array in a finite system. We show also that thermal fluctuations can accelerate domain boundary movement and create clusters similar to those observed experimentally.

We restrict our attention to square array geometries in this work. Spin configurations can be completely specified by vertex arrangements, and for the present work, we use spin or vertex descriptions interchangeably for configurational and energy states. The concept of vertices provides a useful nomenclature for discussing spin configurations [1, 8, 16, 20, 21], effective temperatures of field-driven demagnetization [22, 23] and dynamics [11, 24–26]. We will use vertex descriptions almost exclusively in what follows. In the square lattice, there are 16 distinct vertex configurations, which can be classified into four groups, types I–IV, on the basis of magnetic charge and total moment. The groups are ordered on the basis of energy. Examples of each type are shown in figure 1(a). The ground state corresponds to a complete chessboard tiling of the two type I vertices and is twofold degenerate.

The structure of the paper is as follows. In the next section, we describe the general features of domain dynamics in the presence of quenched disorder, using a mean field theory, with reference to conventional magnetic field and zero-field cooling experiments. We then discuss the effects of thermal fluctuations and strength of coupling using Monte Carlo simulations. These results are compared to experiments. We also discuss how thermal fluctuations can create small cluster excitations above the ground state, which can be understood using statistical arguments. Throughout this work, we see that type I domain formation and growth are general phenomena, a result that is corroborated by simulation results for artificial 'spin' ice in ferroelectric media, which we discuss in the appendix.

## 2. Magnetization processes in mean-field approximation

Magnetic elements are approximated as block Ising spins and arranged on a finite 2D square lattice, as shown in figure 1(b). The importance of long-range dipolar interactions for correlations has been a topic of investigation [13, 20, 27–29], but our simulations suggest that shortcomings of the finite-range interaction approximations are significant only in idealized perfect systems. In the models used throughout the main text of this paper, we consider only the three nearest-neighbour interactions: $J_{\mathrm{n}}$, $J_{\mathrm{nn}}$ and $J_{\mathrm{nnn}}$ in a point dipole model. The square array geometry can be thought of as two sets of parallel lines of elements, with the sets aligned at $90^\circ$ to each other. The $J_{\mathrm{nn}}$ accounts for interactions along each line and the $J_{\mathrm{nnn}}$ couples elements from adjacent parallel lines. The $J_{\mathrm{n}}$ couples elements from the two different sets. These couplings are indicated schematically by dashed lines in figure 1(b). In the appendix, we provide results for a ferroelectric ice where all point dipoles in the array are summed over, and find qualitatively similar results to those presented in this section.

The energy of a magnetic element is determined by the local interactions and any applied fields, $H$. Denoting the magnetic moment at site $i$ by $m_i$, reversal of $m_i$ will occur when
$$
\epsilon_{\mathrm{c}}<\mu_{\mathrm{B}} m_{i} H+m_{i} \cdot \sum_{j \neq i} J_{i, j}\left\langle m_{j}\right\rangle . \tag{1}
$$

Here, $\mu_{\mathrm{B}}$ is the Bohr magneton, $\langle m_i\rangle$ is the mean-field thermal average moment at site $i$ and $\epsilon_{\mathrm{c}}$ is an energy barrier to reversal. We suppose that the energy barrier to reversal is proportional to the anisotropy responsible for the Ising-like behaviour of the magnetic elements. In the mean-field approximation this is
$$
\epsilon_{\mathrm{c}}=\frac{1}{2} m_{i} K\left\langle m_{i}\right\rangle, \tag{2}
$$
where $K$ represents an anisotropy barrier. Each magnetic element is assumed to behave as a single 'soft' macrospin, with a total moment that depends on the temperature. We approximate the temperature behaviour of an element's moment by the Langevin function $L(x)$:
$$
\left\langle m_{j}\right\rangle=L\left[\beta\left(\mu_{\mathrm{B}} H+\frac{1}{2} K\left\langle m_{j}\right\rangle+\sum_{k \neq j} J_{j, k}\left\langle m_{k}\right\rangle\right)\right] . \tag{3}
$$
$\beta$ is the inverse temperature $1/(k_{\mathrm{B}} T)$, where $k_{\mathrm{B}}$ is the Boltzmann constant.

Previous studies have shown that, in field-driven dynamics, a perfect system allows nucleation of type I domains on a type II background through type III vertex dynamics that start at array edges where moments have fewer neighbours and therefore lower reversal thresholds [25]. Local variations in the coupling or reversal barrier parameters can facilitate nucleation processes to start inside the array, leading to less sensitivity to the array boundaries [21, 30, 31]. In a simple model for switching barriers, the barrier height is proportional to the element volume. One would expect that during early stages of deposition of material, the element thicknesses are distributed over a range, leading to a spread in switching field values. Furthermore, significant distributions in switching fields have been observed experimentally in fully grown, athermal artificial spin ice [12, 31–34] and switching field disorder has been shown to give similar outcomes in numerical simulations as do other disorder types [35]. We use this as a motivation for describing disorder in terms of the reversal barriers. We assume the barriers to vary randomly in an interval $\Delta$ centred about $K$, that is, $[K-\Delta/2, K+\Delta/2]$.

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

The mean-field model allows one to examine the stability of the ground state relative to temperature but cannot capture correlations such as those involved in avalanche processes, and such processes will be discussed later. Initially, all moments are assumed to be of unit magnitude in some specified configuration. In the present model, an element $i$ is picked at random and the time-averaged reduction of its magnetization is calculated according to (3). If the magnetization state becomes unstable, that is, if (1) is satisfied, then $m_i$ is set to $-m_i$. The process is repeated by choosing a new moment at random, and the iterations continue until a steady state is found such that no $m_i$ value changes by more than $10^{-4}$.

Reduced units used throughout the paper are defined so that $|m_i| \leqslant 1$, $J_{\text{n}} = 1.5J_0$, $J_{\text{nn}} = 0.7J_0$ and $J_{\text{nnn}} = 0.3J_0$. The reversal barrier has been chosen to be, in reduced units, $K = 10J_0$. Arrays consist of 640 vertices, array boundaries are taken to be 'open' boundaries for which the edge elements have only three nearest neighbours and corner elements have two nearest neighbours, as shown in figure 1(b).

The stability of the type I ground state can be studied by starting the system at low temperature with a complete type I tiling and then increasing the temperature. The critical temperature can be calculated within mean-field theory from the average magnetization of an element in a type I tiling, which obeys

$$
\langle m \rangle = \coth \left( \beta h_{\text{loc}} \langle m \rangle \right) - 1/\left( \beta h_{\text{loc}} \langle m \rangle \right), \tag{4}
$$

where $h_{\text{loc}} = 2(2J_{\text{n}} - J_{\text{nn}} + J_{\text{nnn}}) + \frac{1}{2}K$. The critical temperature $T_{\text{c}}$ is given by $1/\beta = h_{\text{loc}}/3$, to first-order approximation. Using the parameters listed above, $T_{\text{c}} = 3.4T_0$, where $T_0 = J_0/k_{\text{B}}$.

Because changes in magnetic configurations are driven by instabilities only, in the mean-field model, the transition is very sharp with a well-defined critical temperature in a perfect system without disorder. Disorder broadens the transition region in temperature, and leads to the formation of domains of the two different possible type I tilings separated by type II and III chains. Examples are shown in figure 2 for type I populations $n_1$ as functions of temperature for different disorders $\Delta$. The population shown is the sum of both type I tiling possibilities. Other authors also report a broad melting transition in a thermal ice prepared in a magnetized (type II vertex tiling) state [15].

With disorder, a sharp initial reduction occurs in $n_1$ near the critical temperature, corresponding to the nucleation and growth of domains. This is followed by a long tail in which the total population of type I vertices approaches the value $n_1 = 1/8$, corresponding to the high-temperature limit in which each of the 16 possible vertices appear with equal probability. Note that the transition temperature goes to the expected value of $3.4T_0$ as $\Delta \to 0$.

Also shown in figure 2 is the type I population that evolves from a random vertex configuration starting at low temperature. This is analogous to the 'zero-field cooled' state of a ferromagnet that, initially at some temperature above the ordering temperature, has been quenched to low temperature. In the mean-field model, a state with large type I domains immediately evolves at low temperature if $K$ is sufficiently small relative to the $J$. The $n_1$ populations grow with increasing temperature as other vertices become unstable.

This growth of domains occurs through the elimination of small domains and clusters. An example is shown in figure 3, where vertex configurations at two steps during the numerical iteration are shown. The temperature is $T_0$ and disorder $\Delta = 0.1$. Green squares represent type I vertices. The blue arrows are type II vertices and their directions indicate the orientation of the local type II moment. The light and dark red crosses represent the two charge flavours of the type III vertices.

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_3.jpg)

Figure 2. Thermal reduction of type I population $n_1$ starting from a random configuration (open symbols) and starting from a perfect ground state (solid symbols). Disorder is introduced through random variations in individual barriers to reversal. The disorder strengths used are $\Delta=0.2$ (circles), $\Delta=0.4$ (squares) and $\Delta=0.8$ (triangles). Thermal effects are calculated in a self-consistent mean-field approximation. The total population of all type I vertices is shown as a function of reduced temperature for different amounts of disorder. For each disorder value, the evolution is traced starting from low temperature for a uniform single domain of type I and a random configuration. The transition temperature approaches the expected value $3.4T_0$ in the limit of no disorder. Disorder broadens the transition considerably.

The first image (left) is taken after 100 iterations after an initially random configuration of moments. Already a well-defined type I domain structure has formed. The domains are separated by chains composed of type II and III vertices with net magnetic moment and charge, and the energy of their formation acts as a surface tension on the type I domains. For this reason, the chains tend towards straight in the limit of no disorder, since corners lengthen the chain and can involve type III's. The second image (right) shows the evolution after 100 additional iterations. The longest chains have shifted slightly, and positions of the type III vertices within the chains have changed. Most notably, the smallest domains have vanished, and other small domains are reduced in size. Note that type IV vertices are highly unstable and do not survive past the first few iterations.

The reduction in size and eventual annihilation of small domains is the result of an energetic biasing of random domain wall motion towards motion that makes walls shorter by moving closed walls inwards. Dynamics on a type I/type II vertex background—such as domain wall motion—can be described in terms of type III vertex motion [11, 24, 25]. There are therefore two energy costs associated with dynamics: the cost of creating type III vertices and the cost of their propagation. The latter cost is approximately zero in processes where the vertex populations are conserved. For example, in figure 4(a), type III vertices on the domain wall can move at approximately zero cost by flipping the circled spins, to yield the configuration shown in figure 4(b). Accordingly, the lowest-energy mode of domain wall motion is the propagation of type III vertices that have formed at random positions during wall creation. These random

![](./images/813323758923153410_4.jpg)

Figure 3. Example configurations during numerical iteration of the self-
consistent mean-field algorithm. Green regions are type I domains. Blue arrows
indicate type II vertices and point in the direction of the vertex net moment. Red
crosses are type III vertices. The left panel shows a configuration found after
100 iteration loops begun from a random configuration at temperature $T_0$ and no
disorder. The right panel is generated 100 iteration loops later. The box in each
panel indicates a closed domain that has shrunk over the course of the evolution.

fluctuations do not favour either growth or shrinking of domains on average. The existence of
random fluctuations leads us to speculate that an analogy to creep motion [36] may be possible.

The cost of type III vertex creation depends on the local spin configuration, and is lowest
at corners in the domain walls. For example, in figure 4(c), the easiest spin to flip is the circled
spin at the domain wall corner, which can flip to create a type III vertex pair. The resulting type
III vertices can propagate at approximately zero cost by moving along the domain wall, flipping
a diagonal chain of spins on the inside of the wall. This process moves the domain wall inwards,
as illustrated in figure 4(d). Such sequences of type III creation and propagation are the domain
wall motion mechanism with second-lowest energy cost. Thus, over time, the wall motion is
biased so that despite random fluctuations, all closed domains will disappear.

As a final comment on the mean field results, the local fields along the element
magnetizations are weakened within the chains, compared to the fields in regions of lower-
energy type I vertices. In the mean-field model, this leads to a suppression of the magnetization
in the elements participating in the chains. The magnitude of the suppression depends upon the
temperature and can be very large as one nears $T_c$. This effect is shown by the vector magnitude
map in figure 5. The magnitude of element magnetization is shown in greyscale, with black
being unity and white being small. The domain pattern corresponds to the configuration shown
in the second panel of figure 3. One sees that the moment is considerably reduced within the
chains and especially for small clusters. We note that instabilities occur when the moment of
individual elements vanish and these are most likely to occur in the type II walls.


![](./images/813323758923153410_5.jpg)

Figure 4. ((a), (b)) Random domain wall fluctuations driven by type III vertex motion. The circled spins in (a) can flip at approximately zero cost to yield the configuration shown in (b). ((c), (d)) Domain shrinking by type III vertex creation and propagation. The corner of the domain wall provides a type III nucleation site, shown as the circled spin in (c). Once nucleated, the type III vertex can propagate at approximately zero energy cost, shrinking the darker blue domain, as seen in (d). The arrows representing spins are colour-coded light green and dark blue according to which type I domain they belong to. Vertex types are indicated by symbols: type I, II and III vertices are represented as circles, arrows and crosses, respectively.

### 3. Fluctuations and disorder

The energy differences between configurations are often small, even for configurations that are very different. For this reason, single spin flips can drive avalanches that lead to large configurational changes and strongly modify vertex populations as domains evolve. To capture these dynamics, we turn to Monte Carlo simulations.

The model is based as before on the point dipole approximation assumed for the mean-field model. The form of the energy used is the same, but evolution is described using a heat bath algorithm, rather than a simple critical field defined by (3). Additionally, we consider the case of a large Curie temperature so that the effective block moments are insensitive to temperature.

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_6.jpg)

Figure 5. The reduction of magnetic moment at finite temperatures is largest within type II and III chains bounding type I domains. Here a greyscale plot of the moment is shown for the second example configuration of figure 3. Dark signifies large moment and white signifies small moment. The dark regions correspond to type I domains, whereas the moment is dramatically reduced in the domain walls.

In this limit the energy used for the heat bath algorithm is

$$
\epsilon=m_{j}\left(\mu_{\mathrm{B}} H+\frac{1}{2} K m_{j}+\sum_{k \neq j} J_{j, k} m_{k}\right), \tag{5}
$$

where now all magnetizations have fixed magnitude as in an Ising model, with $|m_{i}|=1$. The barrier to reversal is determined by the anisotropy constant $K$. The parameters used are the same as those for the mean-field model. The results shown below were made with 10 000 Monte Carlo steps at each temperature and averaged over 20 realizations of disorder at each disorder strength.

As in the mean-field calculation, the role of disorder is largely to broaden the transition. Example heating curves are shown in figure 6, where thermal evolutions of ground state and random tilings are shown for different disorder strengths $\Delta$. The most striking feature, in comparison to the analogous mean-field results shown in figure 2, is the smooth behaviour of the population at the transition and the rounding in the transition region. We note that the transition away from ground state order, signified by the intersection of the field-cooled and zero-field-cooled curves, occurs at a temperature consistent with previous findings of Möller and Moessner [20], who give the transition temperature as $2.55T_{0}$, in our units.

The dependence on disorder is also less dramatic than in the mean-field case. In both mean-field and Monte Carlo simulations, the spatial distribution of switching barriers is weakly


![](./images/813323758923153410_7.jpg)

Figure 6. Thermal fluctuation effects in an artificial square ice calculated using Monte Carlo and shown as a function of temperature. The total population of all type I vertices, $n_1$, is shown as a function of reduced temperature for different amounts of disorder. Disorder strengths used are $\Delta=0$ (circles), $\Delta=0.4$ (squares) and $\Delta=0.8$ (triangles). For each disorder value, the evolution is traced starting from low temperature for a uniform single domain of type I (solid symbols) and a random configuration (open symbols). At high temperatures the population tends towards $1/8$, the value expected for a random sampling of the 16 possible vertex types.

connected to the final distribution of domains and chains. An analysis of the distribution of $K$ values shows that there is a propensity for chains to locate on strong pinning sites, where $K$ is large, and for weak pinning sites to lie more frequently inside domains. This result can be expected because domains grow via thermally activated spin flips. Growth is accomplished through distortions of chains and chains will pin at sites where $K$ values are too large to allow thermally driven element magnetization flips. Also, as a consequence, the final resulting domain configuration at a given temperature displays rough chains for large $\Delta$ values and flat segmented chains for low $\Delta$ values. Similar segmented domain walls have been observed in Monte Carlo studies of an ideal 16-vertex model with vertex weights consistent with square artificial spin ice energetics [19].

Differences between Monte Carlo and mean field results appear because of how thermal fluctuations drive domain growth. Fluctuations allow the system to explore dynamical pathways different from those dictated by a stability analysis and are therefore quite significant in determining the final domain configuration. At temperatures below the transition, the dominant paths tend towards the lower-energy, single-domain state.

An example evolution is shown in figure 7, using the colour scheme defined in figure 3. Four configurations are shown at constant temperature $T=T_0$, starting with a random initial configuration. The first three configurations are taken after 1000, 2000 and 3000 steps. The fourth configuration (in the bottom right-hand corner) is taken after 10 000 Monte Carlo steps. The amount of disorder in this example was small relative to both $K=10J_0$ and $J_n=1.5J_0$, with $\Delta=0.1$. One sees the slow growth of one type I domain at the expense of another, through the motion and deformation of type II and III chains. The dynamics is equivalent to that seen

![](./images/813323758923153410_8.jpg)

Figure 7. Different stages in the evolution of a vertex configuration as calculated using Monte Carlo simulations. Green regions are type I domains. Blue arrows indicate type II vertices and red crosses are type III vertices. The first three panels show configurations after 1000, 2000 and 3000 steps for a temperature of $T_0$ and disorder $\Delta=0.1$. The initial state was random. The final panel shows the configuration after 10 000 steps. Note that small clusters and domains disappear as large domains grow at the expense of smaller domains.

with the mean-field model. Note that here also type IV vertices do not survive the first few Monte Carlo steps unless interactions are weak (as with large spacings).

In addition to our mean-field and Monte Carlo simulations, we have imaged vertex configurations in as-grown samples and found domain structures similar to those in simulations. An example magnetic force microscopy (MFM) image is shown in figure 8, where domain walls, which carry net moment, are clearly visible on the approximately neutral background of type I domains. The sample imaged here was previously studied in terms of ground state ordering and thermal excitations [10], and consists of an array of nominally $280 \times 85 \times 26 \, \text{nm}^3$ Permalloy islands, with a 3 nm Ti buffer and a 2.5 nm Al cap. Full details of sample fabrication

![](./images/813323758923153410_9.jpg)

Figure 8. MFM image of an as-grown square artificial spin ice, with a lattice constant of 400 nm, relative to island dimensions of $280 \times 85\ \text{nm}^2$. Red and blue colours indicate magnetic poles, and domain walls and small excitations are clearly visible on a ground state background. Two examples of small cluster excitations are indicated by boxes. The image has been false-coloured using the software package WSxM [37]. Note that islands in this image are at $45^\circ$ to the islands in other figures in this paper.

are given elsewhere [10], but the key point is that islands are formed by deposition of Permalloy through gaps in a nanopatterned resist mask, so that island thicknesses—and hence barriers to magnetization reversal—grow over time.

In simulation, the values shown in the figure were obtained after a finite number of Monte Carlo steps, and the effect of temperature, relative to the local coercive field, is to control the rate at which $n_1$ changes. In the experiment, the deposition rate relative to temperature probably controls the rate at which $n_1$ changes. We suggest that domain configurations found in the simulation and the experiment can both be interpreted as snapshots in time of a thermally driven evolution. We note that a difference between the simulations shown in this example and the experiment does exist, in that the as-grown samples support small clusters of flipped spins. We discuss this further in section 3.2.

### 3.1. Spacing and interaction strength

The preponderance of type I vertices in domain structures is a consequence of the higher energies needed to form other vertex types and the corresponding lower probability for their creation. The probability for reversing a moment depends upon the size of local fields relative to thermal energy. This ratio also determines the rate at which domains can grow.

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_10.jpg)

Figure 9. (a) The average number of type I vertices as a function of interaction strength scaling $s$ at a temperature of $T=T_0$ for different strengths of disorder, as simulated using Monte Carlo. Increasing disorder leads to greater stability for other vertex types relative to the ground state. The $n_1$ population tends toward unity as the simulation time is increased in all cases, but very slowly when disorder is strong. (b) Experimental results for type I populations as determined from as-grown samples for arrays grown with different lattice spacings. The populations are shown as a function of $1/r^3$, where $r$ is the lattice spacing, which is proportional to the interaction strength. The populations are averaged over a number of images (typically 5 or 6) taken across each continuous pattern of 0.5 mm by 0.5 mm total area, and the errors are the standard errors over these.

An example from Monte Carlo simulations is shown in figure 9(a). Here the type I population is shown as a function of interaction strength. The interaction strength is scaled by a factor $s$ such that $J_\alpha \to s J_\alpha/J_0$ for each of the three interactions $\alpha$. Temperature is fixed at $T_0$ in all cases. Several different disorder strengths were studied and the simulations were run for 100 000 steps at each spacing. The $n_1$ population tends to unity as the interaction strength increases, although the rate at which this occurs depends on disorder strength. For strong disorder, the rate is lowest. We note also that there were no significant type IV populations observed, although the population did increase with increasing disorder.

We have also measured statistics of the vertex-type populations for as-grown samples with different lattice constants. In these studies, the dimensions of individual elements were held constant at $270 \times 115 \times 25\ \text{nm}^3$, but the lattice constant was varied from 400 to 600 nm. In this way the interaction strength should decrease, roughly like $1/r^3$, where $r$ is the lattice constant. Results are shown in figure 9(b), where the $n_1$ population is given as a function of $1/r^3$. All samples in the series consist of $0.5 \times 0.5\ \text{mm}^2$ continuous arrays of Permalloy islands grown on a 2 nm Ti buffer, with no capping layer, and were fabricated in a single batch, to ensure that fabrication parameters were consistent across the series and so avoid problems with quantitative reproducibility (such as those mentioned in [10]).

Both figures 9(a) and (b) show that the type I populations increase with increasing interaction. In principle one should be able to extract estimates of interaction energies as a function of spacing from the experimentally measured $n_1$. However, inspection of figure 9(a) shows that one also needs to know the amount of disorder before a prediction for $n_1$ can be

![](./images/813323758923153410_11.jpg)

Figure 10. Example of 2 and 3 spin-flip cluster excitations on a type I background. The arrows represent island moments, with the flipped spins shown as bold red arrows. The vertex configurations are also shown with type I, II and III vertices represented as circles, arrows and crosses, respectively.

made. The disorder can be expected to be strongly dependent on details of the sample growth and design [34].

### 3.2. Fluctuations and clusters

The role of disorder is subtle. On the one hand, disorder in $K$ leads to randomness in the chains. On the other, disorder also facilitates fluctuations and leads to the appearance of small clusters of type II and III excitations, examples of which are illustrated in figure 10. In Monte Carlo simulations, these fluctuations usually appear and disappear quite rapidly (in Monte Carlo step time), but can also lead to structures that may persist through several Monte Carlo steps. Experimentally, as-grown samples are seen to exhibit frozen-in fluctuations, as seen in figure 8. In previous studies, it was shown that the population of clusters decays approximately exponentially with their energy, which was given as evidence for thermally driven processes occurring during sample growth [10]. In simulations of field-annealed square ices realized in nanostructured superconductors, small structures can only exist independently of domain walls when sufficient disorder is present [21].

An analytical description of the nucleation, growth and decay of an isolated cluster provides insight into the distribution of experimentally observed clusters. As seen in figure 10, clusters can be thought of as connected lines of spin flips against the ground state. The lines may branch. In our analytical model, the growth and decay of clusters proceeds by single spin flips that extend or shorten these lines. For example, the left-hand cluster shown in figure 10 can evolve into the right-hand cluster and vice versa. For simplicity, we neglect disjoint clusters: large clusters cannot evolve into two smaller clusters.

Under the assumption that clusters are excitations above the ground state that are nucleated by random thermal spin flips, we start with an initial perfect ground state and study the temperature-dependent evolution of small clusters of up to four spin flips. The clusters may be grouped by their topology (and hence energy). There are 25 groups of such clusters: apart from the ground state, there is one distinct cluster of one flip, two clusters of two flips, five of three flips and 16 of four flips. These groups include clusters that contain type IV vertices, but these high-energy clusters are suppressed relative to those containing only type II and III vertices.

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_12.jpg)

Figure 11. Population versus energy above the ground state (in units of $u = \mu_0 m^2/(4\pi r^3)$, where $m$ is the island moment and $r$ is the lattice spacing) for cluster excitations of up to four spin flips. As indicated in the legend, data are shown from experiment (these were previously published in [10]), the master equations (6) and Boltzmann factors. The labels indicate the mnemonics used in [10]. The labels 4+ and 4t are in parentheses to indicate that those clusters were not observed experimentally in [10]. Error bars on the experimental data correspond to the square root of the population of each cluster type.

The processes of cluster growth and decay are transitions between the groups of clusters, and can be described by a master equation for the probability, $P(A)$, of a cluster having topology $A$:

$$
\mathrm{d}P(A,t)/\mathrm{d}t = \sum_{B} \Big(G(B \to A)v(B \to A)P(B,t) - G(A \to B)v(A \to B)P(A,t)\Big), \tag{6}
$$

where the sum runs over all cluster topologies that a cluster of type $A$ can evolve to or from by a single spin flip. $G(A \to B)$ is a multiplicity that takes into account the number of ‘pathways’ from $A$ to $B$ and depends on the numbers of orientationally distinct clusters with a given topology and the number of clusters of topology $A$ that can evolve into a particular cluster of topology $B$. The rate $v(A \to B)$ is given by the Arrhenius-law factor

$$
v(A \to B) = f \exp(-(\epsilon_{\rm c} - \epsilon_{\rm dip})/k_{\rm B} T). \tag{7}
$$

$\epsilon_{\rm c} - \epsilon_{\rm dip}$ gives the energy cost of a spin flip to grow or shrink a cluster on a type I background. $\epsilon_{\rm c}$ is an arbitrary anisotropy barrier whose exact value does not affect the steady-state cluster probabilities. In this model, disorder in anisotropy barriers is neglected and $\epsilon_{\rm c}$ is constant always. $\epsilon_{\rm dip}$ is the energy of the spin prior to flipping, due to point–dipole interactions among near neighbours ($J_{\rm n}$, $J_{\rm nn}$ and $J_{\rm nnn}$). The attempt frequency $f$ does not affect the steady-state probabilities.

The 25 coupled equations of the form (6) can be solved numerically, with an initial condition that the system is in the ground state: $P(\varnothing, t=0) = 1$, $P(i, t=0) = 0, \forall i \neq \varnothing$, where $\varnothing$ represents the ground state. The steady-state probabilities of all clusters that do not contain type IV vertices, normalized to the experimentally observed population of the excitation 1 (i.e. a single spin flip), are plotted in figure 11 as a function of their energy difference with the ground state (as given in [10]). The agreement between theory and experiment is remarkable.

The figure shows the solution at $k_{\rm B} T = 2.96u$, the temperature at which the exponential decay that best fits the theoretical results matches the exponential decay of experimental data.

The energy scale $u = \mu_0 m^2/(4\pi r^3)$, where $r$ is the lattice spacing and the moment $m = MV$, where $M = 860 \times 10^3\,\mathrm{A}\,\mathrm{m}^{-1}$ is the magnetization and $V$ is the island volume. The clusters that contain type IV vertices are not shown, but apart from two exceptions they all have populations less than half of the lowest population shown. This is consistent with experiments [10], where such clusters are not seen and it was concluded such clusters were highly improbable. The exceptions are a type III—type IV—type III line and a type III—type IV—type II—type III cluster, which both have predicted populations of $\sim 2$.

For comparison, the figure also shows populations predicted from Boltzmann factors of the form $g \exp(-dE/k_{\mathrm{B}}T)$. The degeneracy $g$ of a cluster topology is determined by the number of distinguishable ways a particular shape can be rotated and reflected, as well as a factor of 2 (equal for all clusters) to account for the possibility of a global spin flip. $dE$ is the cluster's energy above the ground state, taken from [10]. The ratio of interaction strength to temperature has been tuned to match the exponential decay to that of the experimental data, giving a ratio of $k_{\mathrm{B}}T = 8.18u$.

In experiments, configurations are frozen in as the island volume becomes large enough that shape anisotropy barriers suppress island magnetization reversal. The ratio of temperature to nearest-neighbour coupling can be compared for the master equations and the Boltzmann distribution by estimating the thickness at which freezing-in occurred from the two models. If we estimate the temperature during growth to be 350 K, then the nearest-neighbour interaction is $2.4 \times 10^{-21}\,\mathrm{J}$ for the master equation and $5.9 \times 10^{-22}\,\mathrm{J}$ for the Boltzmann factors. For Morgan *et al*'s $280 \times 85\,\mathrm{nm}^2$ islands, the estimated interaction strengths correspond to thicknesses of 3.5 nm (master equation) and 1.7 nm (Boltzmann factors). Both these estimates are of the same order of magnitude as the estimate of $\sim 1\,\mathrm{nm}$ given in [10]. Recently, a phase diagram for thermal ordering as a function of thickness and lattice constant has been constructed [38].

Interestingly, while the Boltzmann factors and the solutions to (6) both agree well with the experimental data, the Boltzmann factors agree best for the excitations 1, 2L, 3Z and 4Z, while the solutions to (6) fit better for the other clusters. For example, the 'pathway' $1 \to 2\mathrm{L} \to 3\mathrm{U} \to 4\mathrm{O}$ leads to a stable configuration, 4O. In (6), we have truncated the maximum cluster size to four flips, making 4O very stable. However, even without this approximation, the energy cost of adding an extra spin flip to 4O is high and the cluster is stable. Thus, the 4O cluster is in some sense a 'sink' of probability and has higher probability than would be expected from Boltzmann factors, which is captured by the master equations.

Finally, we note that the master equations (6) explicitly assume an initial ground state configuration and treat small excitations as having nucleated and grown on this background before being frozen by increasing island switching barriers. The clusters in the as-grown samples of Morgan *et al* might also be interpreted as regions which have fallen out of equilibrium during the effective cooling of an initially random configuration. While we have not explicitly tested such a possibility, the agreement of the master equations with experiment gives further evidence for the picture of nucleating and growing clusters.

## 4. Conclusion

Vertices in artificial spin ice are local configurations of magnetizations that can be thought of to some extent as classically emergent objects analogous to quasiparticles, able to move and interact according to well-defined rules dictated by the lattice geometry. We have shown that domains of ground state vertices form spontaneously in the square lattice. Domain boundaries

New Journal of Physics **14** (2012) 035014 (http://www.njp.org/)

are defined by chains of type II vertices, along which type III vertices can appear, move and drive the growth of one domain at the expense of another.

We have shown that these domain dynamics occur with rates that depend on temperature and the strengths of interactions between elements. Effects of disorder have been studied and shown to affect mainly the average size and growth rate of domains, while not modifying significantly the fundamental processes involved. A comparison to experimental results was obtained from as-grown samples for which interelement spacing was varied. The experiment and simulations are essentially different in that element thicknesses are changing with time in the experiment, whereas temperature is changed in the simulation. Nevertheless, similarities between populations for the type I ground states were observed between experiment and simulation, suggesting that the as-grown samples are behaving somewhat as frozen snapshots of magnetic ordering within the arrays occurring as described by the simulations presented here.

In addition to domain wall motion, there is also the possibility that an element will flip within a domain. Reversal of a single element in a type I configuration creates a pair of oppositely charged type III vertices. Additional reversals lead to clusters of type II and type III vertices that may persist for some time. We have calculated the probabilities of occurrence of small clusters as a function of their energy and shown that one obtains a distribution in quantitative agreement with that reported recently from experiments [10].

Lastly, we have shown that all the features of domain formation and growth can be obtained with a generic mean field model. This leads us to suggest the possibility of creating artificial spin ice using ferroelectric media and we have provided an example in the appendix using parameters appropriate for bulk $PbTiO_3$. In this example, we also showed that models using full dipole sums over a lattice of point dipoles produce the same qualitative results as a model using a severely truncated sum.

## Acknowledgments
The authors acknowledge the Australian Research Council and University of Glasgow for support. ZB acknowledges funding from the Hackett Foundation. JPM and CHM acknowledge EPSRC and the Centre for Materials Physics and Chemistry at STFC for funding. This research was carried out in part at the Center for Functional Nanomaterials, Brookhaven National Laboratory, which is supported by the US Department of Energy, Office of Basic Energy Sciences, under contract no. DE-AC02-98CH10886.

## Appendix. Ferroelectric ice
Our discussion so far has been within the context of magnetic spin ice, although our results have general applicability to a number of different systems. We illustrate this with a return to the mean-field model and now discuss domain growth within the context of the Landau–Ginzburg theory for ferroelectrics.

A second-order Landau–Ginzburg model is used to calculate the electric dipole moment of an island $i$, given the effective electric field $\mathbf{E}$ at that point. Each dipole is assumed to lie along only one axis, parallel to the long axis of that island. The ferroelectric free energy density $F$ at island position $\mathbf{r}_i$ is given by
$$
F(i)=\frac{\alpha}{2} P^{2}(i)+\frac{\beta}{4} P^{4}(i)-\mathbf{E}(i) \cdot \mathbf{P}(i), \tag{A.1}
$$

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

where $\mathbf{P}$ is the electric polarization and $\alpha = A(T - T_{\mathrm{c}})$ and $\beta$ are the Landau parameters for the material. $\mathbf{P}(i)$ is assumed to lie parallel to the element long axis. A point dipole approximation is again used with the electric dipole associated with island $i$ denoted as $\mathbf{p}_{i}=V \mathbf{P}(i)$, where $V$ is the volume of an element and $\mathbf{P}(i)$ is assumed to be uniform across the element.

Unlike the previous mean-field theory, in this model we calculate the electric field at position $i$ by superposing contributions from all other elements (approximated as point dipoles) in the square lattice. The number of elements used is sufficiently small that one can use the simple summation

$$
\mathbf{E}\left(i^{\prime}\right)=\sum_{i \neq i^{\prime}} \frac{1}{4 \pi \epsilon_{0} \epsilon}\left(3 \frac{\left(\mathbf{r}_{i^{\prime}}-\mathbf{r}_{i}\right)\left[\left(\mathbf{r}_{i^{\prime}}-\mathbf{r}_{i}\right) \cdot \mathbf{p}_{i}\right]}{\left|\mathbf{r}_{i^{\prime}}-\mathbf{r}_{i}\right|^{5}}-\frac{\mathbf{p}_{i}}{\left|\mathbf{r}_{i^{\prime}}-\mathbf{r}_{i}\right|^{3}}\right). \tag{A.2}
$$

Minimization of (A.1) will, for a range of $\mathbf{E}$ values, give two solutions for $p_{i}$ with opposite sign. One can show simply from (A.1) that the energy barrier separating the two solutions disappears when

$$
\frac{\mathbf{E}(i) \cdot \mathbf{p}_{i}}{p_{i}}>\frac{2 \alpha^{3 / 2}}{\sqrt{27} \beta^{1 / 2}}. \tag{A.3}
$$

This is the condition for the stability of an element's polarization orientation. When this condition is fulfilled, the polarization is reversed. As in the previous mean field model, this procedure is iterated through a system of elements at a fixed temperature until a steady state is reached.

Parameters used for the simulations are: $T_{\mathrm{c}}=1100 \mathrm{~K}, A=7.5 \times 10^{5} \mathrm{C}^{-2} \mathrm{~m}^{2} \mathrm{~N} \mathrm{~K}^{-2}$ and $\beta=2.4 \times 10^{9} \mathrm{C}^{4} \mathrm{~m}^{6} \mathrm{~N}$. These parameters give a polarization in zero field and at room temperature $P=\sqrt{(\alpha / \beta)}=0.5 \mathrm{C} \mathrm{m}^{-2}$, which is typical of $\mathrm{PbTiO}_{3}$ in bulk [39] and is quite accurate for elements that are over $100 \mathrm{~nm}$ long. It should be noted that the Landau expansion (A.1) should strictly speaking be to sixth order, to most accurately model the ferroelectric phase transition [39], but we neglect the $P^{6}$ terms here for simplicity. Results are given for a $20 \mu \mathrm{m}^{2}$ sample with $N=50$ islands along one edge (4900 islands and 2401 vertices). A spacing of $400 \mathrm{~nm}$ between island centres is assumed. The starting configuration for an iteration is taken to be islands having polarization with constant magnitude $P_{i}=\left(\frac{\alpha}{\beta}\right)^{1 / 2}$, with random alignments along element axes.

The energy barrier with these parameters for flipping an element polarization is much larger than the thermal energy, for most temperatures below the Curie point, so reversal via thermal fluctuations occurs only in the vicinity of $T_{\mathrm{c}}$.

The general features observed in the magnetic system are also found for the ferroelectric system. Starting from a macroscopically unpolarized state at low temperature, the effect of increasing temperature is to increase the number of type I vertices. As before, domains of type I's form, separated by chains of type II and III vertices. Effects of disorder are also completely analogous.

Finally, we note that domains grow at temperatures approaching $T_{\mathrm{c}}$, as also found for the magnetic system. An example of the average Type I domain size is shown in figure A.1 for three temperatures. The error bars correspond to the spread in sizes calculated over ten different initial configurations.

It is useful to note that it is possible to define a relaxational dynamics based on the effective field $-\frac{\partial F}{\partial \mathbf{p}_{i}}$. The iteration process can thus be related directly to a real-time dynamics. In this sense, the numerical iteration method is a time evolution and these simulations provide a feeling

New Journal of Physics 14 (2012) 035014 (http://www.njp.org/)

![](./images/813323758923153410_13.jpg)

Figure A.1. The average size of a connected region (domain) of type I vertices as a function of temperature as calculated using a self consistent Landau-Ginzburg model with parameters appropriate for $PbTiO_3$. The error bars show one standard deviation.

of the effect that different cooling rates may have on a system. If the system is cooled faster than the islands' polarization can respond, then a higher number of unfavourable type II and III vertices will be frozen into the artificial ferroelectric ice. This is interesting because these domain walls form without the presence of disorder and have a density depending on the history of the system.

### References
[1] Wang R F *et al* 2006 **Nature** ***439*** 303

[2] Pauling L 1935 *J. Am. Chem. Soc.* ***57*** 2680

[3] Tanaka M, Saitoh E, Miyajima H, Yamaoka T and Iye Y 2006 *Phys. Rev. B* ***73*** 052411

[4] Qi Y, Brintlinger T and Cumings J 2008 *Phys. Rev. B* ***77*** 094418

[5] Mengotti E, Heyderman L J, Fraile Rodríguez A, Bisig A, Guyader L L, Nolting F and Braun H B 2008 *Phys. Rev. B* ***78*** 144402

[6] Li J, Ke X, Zhang S, Garand D, Nisoli C, Lammert P, Crespi V H and Schiffer P 2010 *Phys. Rev. B* ***81*** 092406

[7] Li J, Zhang S, Bartell J, Nisoli C, Ke X, Lammert P E, Crespi V H and Schiffer P 2010 *Phys. Rev. B* ***82*** 134407

[8] Ke X, Li J, Nisoli C, Lammert P E, McConville W, Wang R F, Crespi V H and Schiffer P 2008 *Phys. Rev. Lett.* ***101*** 037205

[9] Remhof A, Schumann A, Westphalen A, Zabel H, Mikuszeit N, Vedmedenko Y, Last T and Kunze U 2008 *Phys. Rev. B* ***77*** 134409

[10] Morgan J P, Stein A, Langridge S and Marrows C H 2011 *Nature Phys.* ***7*** 75

[11] Morgan J P, Stein A, Langridge S and Marrows C H 2011 *New J. Phys.* ***13*** 105002

[12] Mengotti E, Heyderman L J, Fraile Rodríguez A, Nolting F, Hügli R V and Braun H B 2011 *Nature Phys.* ***7*** 68

[13] Rougemaille N *et al* 2011 *Phys. Rev. Lett.* ***106*** 057209

[14] Phatak C, Petford-Long A K, Heinonen O, Tanase M and De Graef M 2011 *Phys. Rev. B* ***83*** 174431

[15] Kapaklis V *et al* 2011 arXiv:1108.1092

[16] Libál A, Reichhardt C and Olson Reichhardt C J 2006 *Phys. Rev. Lett.* ***97*** 228302

[17] Libál A, Reichhardt C and Olson Reichhardt C J 2011 arXiv:1108.3584

[18] Silva R C, Nascimento F S, Mól L A S, Moura-Melo W A and Pereira A R 2012 *New J. Phys.* ***14*** 015008

[19] Levis D and Cugliandolo L F 2012 *Europhys. Lett.* ***97*** 30002

New Journal of Physics **14** (2012) 035014 (http://www.njp.org/)

[20] Möller G and Moessner R 2009 *Phys. Rev. B* **80** 140409

[21] Libál A, Olson Reichhardt C J and Reichhardt C 2009 *Phys. Rev. Lett.* **102** 237004

[22] Nisoli C, Wang R F, Li J, McConville W F, Lammert P E, Schiffer P and Crespi V H 2007 *Phys. Rev. Lett.* **98** 217203

[23] Nisoli C, Li J, Ke X, Garand D, Schiffer P and Crespi V H 2010 *Phys. Rev. Lett.* **105** 047205

[24] Mól L A, Silva R L, Silva R C, Pereira A R, Moura-Melo W A and Costa B V 2009 *J. Appl. Phys.* **106** 063913

[25] Budrikis Z, Politi P and Stamps R L 2010 *Phys. Rev. Lett.* **105** 017201

[26] Mól L A S, Moura-Melo W A and Pereira A R 2010 *Phys. Rev. B* **82** 054434

[27] Möller G and Moessner R 2009 *Phys. Rev. B* **80** 140409

[28] Chern G-W, Mellado P and Tchernyshyov O 2011 *Phys. Rev. Lett.* **106** 207202

[29] Mól L A S, Pereira A R and Moura-Melo W A 2011 *Phys. Lett. A* **375** 2680

[30] Budrikis Z, Politi P and Stamps R L 2011 *Phys. Rev. Lett.* **107** 217204

[31] Budrikis Z, Morgan J P, Akerman J, Stein A, Stamps R L, Politi P, Langridge S and Marrows C H 2011 arXiv:1111.6491

[32] Kohli K K, Balk A L, Li J, Zhang S, Gilbert I, Lammert P E, Crespi V H, Schiffer P and Samarth N 2011 *Phys. Rev. B* **84** 180412

[33] Ladak S, Read D E, Perkins G K, Cohen L F and Branford W R 2010 *Nature Phys.* **6** 359

[34] Daunheimer S, Petrova O, Tchernyshyov O and Cumings J 2011 *Phys. Rev. Lett.* **107** 167201

[35] Budrikis Z, Politi P and Stamps R L 2011 arXiv:1110.1463

[36] Lemerle S, Ferré J, Chappert C, Mathet V, Giamarchi T and Le Doussal P 1998 *Phys. Rev. Lett.* **80** 849

[37] Horcas I, Fernández R, Gómez-Rodríguez J M, Colchero J, Gómez-Herrero J and Baro A M 2007 *Rev. Sci. Instrum.* **78** 013705

[38] Nisoli C 2012 arXiv:1201.2832

[39] Haun M J, Furman E, Jang S J, McKinstry H A and Cross L E 1987 *J. Appl. Phys.* **62** 3331

New Journal of Physics **14** (2012) 035014 (http://www.njp.org/)