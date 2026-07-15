Chaos, Solitons & Fractals 44 (2011) 241-247

![](./images/811676941370261505_1.jpg)

Contents lists available at ScienceDirect

Chaos, Solitons & Fractals
Nonlinear Science, and Nonequilibrium and Complex Phenomena
journal homepage: www.elsevier.com/locate/chaos

![](./images/811676941370261505_2.jpg)

# The transition from fracton to phonon states in a Sierpinski triangle lattice

E.L. da Rocha*, C.R. da Cunha

Departamento de Engenharia Elétrica, Universidade Federal de Santa Catarina, Florianópolis-SC 88040-900, Brazil

---

## ARTICLE INFO

Article history:
Received 15 July 2010
Accepted 5 February 2011
Available online 4 March 2011

---

## ABSTRACT

Lattice dynamics of a Sierpinski triangle submitted to different levels of disorder was studied via atomistic Green's functions. It was found that there is a critical level of disorder that separates two regions of thermal transport. The first is characterized by a fast destruction of fracton states and the formation of spatially extended phonon states. The second region is characterized by a transition from extended to localized phonon states as predicted by the Anderson model.

© 2011 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Fractals can be understood as geometric entities that show scale invariant structural properties [1]. Its concept [2] provides a mathematical framework to describe several structural aspects of nature that otherwise could appear to be only random. Such patterns can usually be characterized by self-similarity, scale invariance and a fractional dimension. Condensed matter systems such as polymers, porous media and colloids are examples of materials that can show statistical self-similar behavior such as that of random fractals [3].

More recently, complex structures at the nanoscale regime have shown fractal geometry. For instance the growth of monolayers of poly (ethylene oxide) at high temperatures can exhibit fractal geometry [4]. Some other structures such as aerogels [5] show distinctive properties such as nearly ideal electrical, acoustic and thermal insulations [6]. These properties are credited in part to their fractal structure.

Amongst the fractal structures, the Sierpinski triangle can be constructed by iteratively dividing each triangle of a figure into three new self-contacting triangles of the same size. The resulting fractal has Hausdorff dimension of 1.585 and has important scientific and technological implications. For instance, some molecules such as bis-terpyridine can be self assembled into a Sierpinski pattern [7]. Moreover, integrated antennas constructed in a Sierpinski triangle shape have been used to improve their performance [8].

Materials with fractal geometry typically have localized vibrations whose quantization is referred to as a fracton [9]. The presence of fractons in a material can cause anomalous diffusion [10] with square mean displacement obeying a power law related to its fractal dimension [3,9]. Therefore, the propagation of phonons is reduced, causing a limited thermal conductivity. A similar behavior can be found in disorder materials. For instance, phonon localization has been observed in asymmetric disordered harmonic chains causing thermal rectification [11].

Here, we use the atomistic Green's function formalism to study the transition from fracton to phonon states in a Sierpinski triangle lattice submitted to different levels of structural disorder. The transmission function, local density of states and correlation properties are studied.

## 2. Theory and method

Some fractal structures such as the Sierpinski gasket have recursive definitions that allow for exact calculations on infinite lattices. For instance, the Schrödinger equation has been solved exactly for this structure using a recursive scheme [19]. Some similar calculations have been performed for hierarchical structures using a renormalization group approach [20]. Nonetheless, exact calculations for randomly disordered structures are usually difficult. On the other hand, the computational time required for

* Corresponding author.
E-mail addresses: edroaldo@gmail.com (E.L. da Rocha), creq@eel.ufsc.br (C.R. da Cunha).

0960-0779/$ - see front matter © 2011 Elsevier Ltd. All rights reserved.
doi:10.1016/j.chaos.2011.02.002

numerical simulations grows exponentially with the self-similarity level of the fractal. Therefore, our calculations were performed numerically on finite lattices with self-similarity levels up to six, which can be completed in a couple of months with our current technology.

We produce fractals with different levels of disorder. Our disorder is defined as rewiring the bonds of each site of the fractal with probability p, avoiding self-connections and duplicates. This is exactly the procedure used by Watts and Strogatz to produce random graphs with small-world properties [17]. In the limiting case when p is zero we have a regular fractal structure, whereas when p is one we have an Erdös-Rényi random graph [18].

An ensemble of different configurations was produced for each level of disorder. The number of elements of each ensemble was a number that kept the simulation time tolerable. For self-similarity level three we used two hundred samples, whereas for self-similarity level four we used one hundred samples, for self-similarity five we used twenty samples and for self-similarity six we used one sample.

Our investigation of phonon transport using atomistic Green's functions is comprised of several steps. First, harmonic tensors are generated to describe the harmonic connections between many atomic degrees of freedom. This step uses the equilibrium atomic positions and an harmonic interatomic potential energy model. Then, the Green's functions are evaluated using the harmonic matrices to compute the frequency dependent phonon transmission functions as the phonon source is connected to different random sites of the fractal. Again, the number of sites was such that kept the simulation time tolerable. Thus, we used twelve points for self-similarity level three, ten points for self-similarity four, eight points for self-similarity five and four points for self-similarity level six.

Integration is performed over a finite frequency spectrum for specific temperatures in order to calculate the heat flux between contacts. The thermal conductance is obtained by the ratio of the heat flux to the gradient of temperature. It is important to note that the finite frequency spectrum may be a source of simulation errors. Other sources are numerical truncation, limited resolution in resolving small clusters, the limited size of the ensembles and the very nature of disorder.

A model configuration of the fractal nanodevice attached to one-dimensional phonon source and drain is showed in Fig. 1. The phonon source has a reservoir temperature $T_s$, while the drain has a temperature $T_d$. The phonon drain is fixed to a specific region of the fractal while the source is applied to several random sites to compute the phonon transmission function.

### 2.1. Formalism

In the atomistic Green's function [12], atom groups and their interactions are represented by a dynamical matrix, defined in terms of an interatomic potential U. This potential can assume different forms, as for example, the harmonic Harrison interatomic potential [13] and the Stillinger-Weber (SW) potential [14] popularly used to study phonon transport in Si lattices [15].

Here we are not interested in specific properties of an individual material. Rather, our purpose is to analyze general properties of fractal geometries. Thus, we simplify the interatomic potential as a general spring Hooke potential between sites. Therefore, we are able to find the dynamical matrix directly via lattice dynamics. The Langrangian operator of our system is given by:

$$
L=\frac{1}{2} m \sum_{i} \dot{u}_{i}^{2}+\frac{1}{4} \sum_{i \neq j} k_{i j}\left(u_{i}-u_{j}\right)^{2}, \tag{1}
$$

where m is the mass of each site, $u_n$ is the displacement from the equilibrium of the nth site position and $k_{ij}$ is a spring constant. In our model, we normalize the ratio between the spring constant and the mass as a constant. We apply the Euler-Lagrange equation to this system in order to get the following equation of motion in the frequency domain:

$$
\frac{k}{m} \sum_{j \neq i} k_{i j}\left(u_{i}-u_{j}\right)=\omega^{2} u_{i}. \tag{2}
$$

The dynamical matrix can be extracted directly from the above equation for the index j spanning the positions where the site i is connected to.

### 2.2. Green's functions

The dynamical matrix is used to calculate the retarded Green's function:

$$
G\left(\omega^{2}\right)=\left[\omega^{2} I-K\left(\omega^{2}\right)-\Sigma_{S}\left(\omega^{2}\right)-\Sigma_{D}\left(\omega^{2}\right)\right]^{-1}, \tag{3}
$$

where $\Sigma_{n}(\omega^{2})$ is a self-energy matrix that describes the coupling of the nano device to the contacts of the source and drain and K is the dynamical matrix. The self-energies are those of a monatomic linear chain where the non-null element is given by [16]:

![](./images/811676941370261505_3.jpg)

Fig. 1. A model configuration of the fractal lattice attached to one-dimensional phonon source and drain.

$$
\Sigma_{n n}=\frac{i}{\left[\omega_{0}^{2}-\left(\omega^{2}-\omega_{0}\right)^{2}\right]^{\frac{1}{2}}},
\tag{4}
$$

where $\omega_{0}$ is a natural frequency of oscillation of the wire, which we normalize to a fixed value so that it produces a good coupling to our structure.

Once the Green's function and the self-energies are calculated, the mean phonon transmission function per point of the fractal is obtained from:

$$
T\left(\omega^{2}\right)=\frac{1}{N} \sum_{n>1}^{N} \operatorname{Tr}\left(\Gamma_{S} G^{R} \Gamma_{D} G^{A}\right).
\tag{5}
$$

We also calculate a transmission sum over all computed frequencies as an initial estimate of the thermal conductance. The average local density of states (ALDoS) over an energy range can be found directly from the retarded Green's function as:

$$
L_{x}=\frac{-1}{\pi E} \sum_{\epsilon}^{E} \operatorname{Img}\left\{G^{R}(x, x, \epsilon)\right\}.
\tag{6}
$$

### 2.3. Correlations

We calculate three types of correlation functions. First, we computed the Pearson product-moment correlation between the mean ALDoS with different levels of disorder and the ALDoS without disorder:

$$
C_{1}(r)=\frac{\sum_{i=1}^{n}\left(L_{i}^{o}-\bar{L}^{o}\right)\left(L_{i}^{r}-\bar{L}^{r}\right)}{\sqrt{\left[\sum_{i=1}^{n}\left(L_{i}^{o}-\bar{L}^{o}\right)^{2}\right]\left[\sum_{i=1}^{n}\left(L_{i}^{r}-\bar{L}^{r}\right)^{2}\right]}},
\tag{7}
$$

where the subscript $r$ denotes the disorder level and the subscript $o$ denotes the absence of structural disorder. The curves show an exponential dependence of the form $C_{1}(r) \sim e^{-r / \xi}$, where $\xi$ we define as a disorder correlation level. This parameter can be used as an estimate of how much disorder the system can tolerate before statistically becoming a different state.

We then used the correlation sum to estimate the correlation integral of the transmission curves:

$$
C_{2}(\varepsilon)=\frac{1}{N^{2}} \sum_{\omega_{i}^{2}>\omega_{j}^{2}}^{N} \Theta\left(\varepsilon-\left\|T\left(\omega_{i}^{2}\right)-T\left(\omega_{j}^{2}\right)\right\|\right).
\tag{8}
$$

These curves show an exponential dependence of the form $C_{2}(\varepsilon)=\varepsilon^{v}$, where $v$ is the correlation dimension. Finally, we calculate the pair correlation function $\left(C_{3}\right)$ of each ALDoS at different levels of disorder. This is algorithmically calculated as the probability of finding two points separated by a distance $r$ whose ALDoS are less than $5 \%$ different. We use this correlation function to obtain the average size of clusters via:

$$
C_{4}(r)=\frac{\sum_{i=0}^{N} i C_{3}^{r}(i)}{\sum_{i=0}^{N} C_{3}^{r}(i)}.
\tag{9}
$$

As with the previous correlation functions, the average size of clusters also has an exponential decay dependence of the form $C_{4}(r) \sim e^{-r / \zeta}$, where $\zeta$ we define as a disorder localization length. This parameter can be used as an estimate of localization as the disorder level is varied.

## 3. Results and discussion

Fig. 2 shows the local density of states for disorder levels of 0, 20, 40 and 60%. The disorder correlation length $(\xi)$ for the Sierpinski triangle at self-similarity level six is 2.83. This implies that small levels of disorder should be enough to break the formation of fractonic structures in the average local density of states and move the system to a regime of phononic states.

In order to verify this, we produced a map of average density of states (ADOS) for different levels of disorder as shown in Fig. 3. Indeed, this map visually shows that there is a more distributed density of states over frequencies for small levels of disorder.

This could indicate a transition from a fractal density of states distributed over all frequencies to a regime of phonon states. Fig. 4 shows the correlation dimension $(v)$ for these curves at different self-similarity levels. The figure shows that for small levels of disorder, as the self-similarity level increases, the correlation dimension of the density of states tends to peak at a value near the unity, indicating a transition in topology from a fractal (self-similar segments in the ADOS) to an Euclidean space (a plane curve in the ADOS). This also shows the onset of formation of phonon bands. As the disorder level is further raised, the density of states progressively has its correlation dimension reduced until it enters a regime of statistical fractal geometry near a disorder level of 20%. This regime shows low frequency phonon bands.

Fig. 5 shows the average cluster size, which increases rapidly for small levels of disorder. This could indicate that although we are introducing disorder in the system, there may be a better coupling between points in the fractal as the fractonic states are broken and percolating clusters are formed in the ALDoS - a behavior similar to the small-world effect. This result is somewhat different from what Anderson localization predicts for regular geometries. Soon after reaching the disorder correlation length, the average cluster size begins to reduce, implying a progressively increase in localization. In this situation Anderson localization seems to be more adequate. This analysis suggests that the transition from a fractal to Euclidean topology is related to an increase in connectivity of the network, whereas the transition from Euclidean to statistical fractal topology is related to a reduction of the cluster size that happens as a result of disorder.

We further explore this behavior in Fig. 6 where we produce a map of the transmission for different levels of disorder for a self-similarity level of six. Again it is clear that there is a different behavior for disorder levels smaller than approximately 20%. In this window there is a participation of transmission from a broad range of frequencies whereas for higher disorder levels the transmission seems to be more localized at lower frequencies.

Fig. 7 shows the correlation dimension for the transmission curves. Small lattices seem to be more affected by disorder, as there is only one significant peak for very low disorder levels. This correlates well with a rapid decreasing cluster size observed in these lattices. A differ-

![](./images/811676941370261505_4.jpg)

Fig. 2. Local density of states for the Sierpinksi triangle with a self-similarity level six submitted to disorder levels of (a) 0%, (b) 20%, (c) 40% and (d) 60%.

![](./images/811676941370261505_5.jpg)

Fig. 3. Map of density of states for the Sierpinski triangle with self-similarity level six as a function of $\omega^{2}$ and the disorder level. Higher density of states are darker.

ent behavior is observed for medium size lattices. Small levels of disorder tend to form bands of transmission (increase in the correlation dimension), implying that the system moved from a fractonic to a spatially extended phononic regime. This happens up to disorder levels close to 20% where the correlation dimension is reduced, implying that the system entered a regime of localized phonons as predicted by the Anderson model. This agrees with the previous analysis as we see the formation of clusters in the ALDoS that increases the coupling between different sites and then a transition from Euclidean to statistical fractal topology after a critical point near 20%.

Fig. 8 shows the transmission sum for all four lattice sizes. In all cases, the transmission sums only show

![](./images/811676941370261505_6.jpg)

Fig. 4. The correlation dimension for the curves of density of states obtained at different levels of disorder for self-similarity levels (a) 3, (b) 4, (c) 5 and (d) 6. The major ticks indicate a measure of dimensionality 0 for the curve immediately above and 1 for the curve immediately below.

![](./images/811676941370261505_7.jpg)

Fig. 5. The relative average cluster size within the Sierpinski triangle at different levels of disorder for self-similarity levels (a) 3, (b) 4, (c) 5 and (d) 6. The major ticks indicate the position of the smallest cluster (0 %) for the curve immediately above and the biggest cluster (100 %) for the curve immediately below.

features for disorder levels smaller than approximately 20%. This implies that the thermal conductance in Sierpinski lattices is mainly governed by fractons and extended phonons generated by small levels of disorder.

## 4. Conclusions

We investigate the dynamical behavior of a Sierpinski triangle geometry via atomistic Green's functions. Results

![](./images/811676941370261505_8.jpg)

Fig. 6. Map of the average transmission function within different points of a Sierspinki triangle with self-similarity level six as a function of $\omega^2$ and the disorder level.

![](./images/811676941370261505_9.jpg)

Fig. 7. The correlation dimension for the transmission curves obtained at different levels of disorder for self-similarity levels (a) 3, (b) 4, (c) 5 and (d) 6. The major ticks indicate a measure of dimensionality 0 for the curve immediately above and 1 for the curve immediately below.

suggest that small levels of disorder are enough to break fractonic states and take the system to a regime of ex- tended phonon states. After a critical disorder level the sys- tem enters a regime of statistical fractal geometry where most of the thermal transport is performed by phonons which are progressively more localized as the disorder is increased. Anderson localization theory seems to be appro- priate to describe the thermal transport for the statistical

![](./images/811676941370261505_10.jpg)

Fig. 8. The transmission sums obtained at different levels of disorder for self-similarity levels (a) 3, (b) 4, (c) 5 and (d) 6. The minimum and maximum of all plots are $10^{-2}$ and $10^{2}$ respectively.

fractal geometry, however it can be further explored for pure fractal geometries.

### Acknowledgements

The authors would like to acknowledge the Brazilian council for the progress of science and technology (CNPq) and the agency for graduate enhancement (CAPES) for funding this work.

### References

[1] Orbach R. Dynamics of fractal networks. Science 1986;231:814-9.

[2] Mandelbrot BB. The fractal geometry of nature. New York: W.H. Freeman; 1983.

[3] Ma D, Stoica AD, Wang X-L. Power-law scaling and fractal nature of medium-range order in metallic glasses. Nat Mater 2009;8:1629-34.

[4] Ma Z. Fractal crystal growth of poly(ethylene oxide) crystals from its amorphous monolayers. polymer 2008;49:1629-34.

[5] Mohanan JL, Arachchige IU, Brock SL. Porous semiconductor chalcogenide aerogels. Science 2005;307:397-400.

[6] Casas L, Roig A, Rodriguez E, Molins E, Tejada J, Sort J. Silica aerogel-iron oxide nanocomposites: structural and magnetic properties. J Non-Cryst Solids 2001;285:37-43.

[7] Newkome GR, Wang P, Moorefield CN, Cho TJ, Mohapatra P, Li S, et al. Nanoassembly of a fractal polymer: a molecular Sierpinski "hexagonal gasket. Science 2006;312:1782-5.

[8] Kingsley N, Anagnostou DE, Tentzeris M, Papapolymerou J. Rf mems sequentially reconfigurable Sierpinski antenna on a flexible organic substrate with novel dc-biasing technique. J Microelectromech syst 2007;16:1185-92.

[9] Alexander S, Orbach R. Density of states on fractals: fractons. Le Journal de Physique-Lettres 1982;43:625-31.

[10] Vlahos L, Isliker H, Kominis Y, Hizanidis K. Normal and anomalous diffusion: a tutorial. Order Chaos 2008; Available from arXiv:0805.0419v1.

[11] Hopkins PE, Serrano JR. Phonon localization and thermal retification in asymetric harmonic chains using nonequilibrium green's function formalism. Phys Rev B 2009;80:201408-11.

[12] Zhang W, Fisher T, Mingo N. The atomistic green's function method: an efficient simulation approach for nanoscale phonon transport. Numer Heat Transfer Part B: Fundam 2007;48:333-49.

[13] Harrison WA. Electronic structure and properties of solids: the physics of the chemical bond. Publications: Dover; 1989.

[14] Stillinger FH, Weber TA. Computer simulation of local order in condensed phases of silicon. Phys Rev B 1985;31:5262-71.

[15] Zhang W, Mingo N, Fisher TS. Simulation of phonon transport across a non-polar nanowire junction using an atomistic green's function method. Phys Rev B 2007;76:195429-38.

[16] Economou E. Green functions in quantum physics. Springer; 2006.

[17] Watts DJ, Strogatz SH. Collective dynamics of 'small-world' networks. Nature 1998;393:440-2.

[18] Erdös P, Rényi A. On random graphs I. Publ Math 1959;6:290-7.

[19] Domany E, Alexander S, Bensimon D, Kadanoff LP. Solutions to the Schrödinger equation on some fractal lattices. Phys Rev B 1983;28:3110-23.

[20] Schwalm WA, Reese CC, Wagner CJ, Schwalm MK. Explicit green functions for hierarchical lattices. Phys Rev B 1994;49:16650.