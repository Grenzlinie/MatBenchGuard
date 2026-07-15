# Origin and Detection of Microstructural Clustering in Fluids with Spatial-Range Competitive Interactions

Ryan B. Jadrich,∗ Jonathan A. Bollinger,∗ Keith P. Johnston, and Thomas M. Truskett†
McKetta Department of Chemical Engineering, University of Texas at Austin, Austin, Texas 78712, USA
(Dated: July 27, 2021)

Fluids with competing short-range attractions and long-range repulsions mimic dispersions of charge-stabilized colloids that can display equilibrium structures with intermediate range order (IRO), including particle clusters. Using simulations and analytical theory, we demonstrate how to detect cluster formation in such systems from the static structure factor and elucidate links to macrophase separation in purely attractive reference fluids. We find that clusters emerge when the thermal correlation length encoded in the IRO peak of the structure factor exceeds the characteristic lengthscale of interparticle repulsions. We also identify qualitative differences between the dynamics of systems that form amorphous versus micro-crystalline clusters.

## I. INTRODUCTION

Complex fluids frequently possess one or more frustrating interaction lengthscales that, regardless of origin, generate micro- to mesoscale structural heterogeneity. Archetypical examples include microemulsions [1], block copolymers [2, 3], confined fluids [4, 5], and colloidal dispersions, including proteins [6–11], wherein the surfactant size, block length, pore size, and screened electrostatic repulsions set the respective length scales of frustration. Despite their contextual differences, all exhibit similar transitions between homogeneous fluid states and emergent heterogeneous phases with density correlations characterized by intermediate range order (IRO), typically identified by the presence of a pre-peak at low but finite $k$ in the static structure factor $S(k)$ [12].

In the case of a pore-glass confined binary fluid system [13], the experimental emergence of IRO has been rationalized via the behavior of the fluid thermal correlation length $\xi_T$, which quantifies the range of correlated concentration fluctuations and the associated IRO peak width in $S(k)$. In particular, it was demonstrated that the crossover in the temperature-density $(T-\rho)$ plane from dispersed fluid to strong IRO corresponds to the conditions at which $\xi_T$ reaches the pore size, i.e., the characteristic frustrating lengthscale. Such conditions enable strong, preferential segregation of the wall-attracted species from the other component which, in turn, migrates into the pore centers. Additionally, the IRO $(T-\rho)$ crossover conditions corresponded to state points close to where the unconfined fluid reference system would otherwise exhibit liquid-liquid macrophase segregation.

Here, we extend thermal correlation length concepts to a simple model system characterized by IRO: the short-range attractive, long-range repulsive (SL) fluid, which mimics charge-stabilized colloids with van der Waals, depletion, and/or hydrophobic attractions. Various studies have demonstrated that the long-range repulsive interaction suppresses macrophase separation—which would occur for strong short-range attractions alone—in favor of IRO structures including clusters [14–18]. However, an ongoing challenge has been to distinguish between generic IRO (i.e., presence of *any* pre-peak) and clustering specifically, particularly in a way accessible to experiments [12, 17]. One such criterion [17] suggests that clustering emerges when the IRO peak reaches a magnitude $S(k_{SL}^*) \geq 2.7$; this bears similarity to the empirical Hansen-Verlet single-phase rule for tracing macroscopic freezing boundaries in simple fluids [19].

Section II presents the SL models under consideration and the simulation protocol and theoretical methodology used to characterize their behaviors. In Section III we propose a new conceptual framework and accurate criterion for clustering: namely, clusters form when the thermal correlation length $\xi_T$ encoded in the IRO pre-peak of $S(k)$ exceeds the characteristic lengthscale of the frustrating interparticle repulsive interaction. We find that this criterion also bolsters previously proposed connections between emergent IRO in SL fluids and macroscopic phase separation in corresponding reference attractive (RA) models [17] lacking long-range repulsions. Finally, we show that the criterion makes useful predictions for fluids that form either amorphous or micro-crystalline clusters, despite striking qualitative differences in the dynamic behaviors of these two types of systems. The paper concludes in Section IV with a brief summary of our results and their relevance to experiment.

## II. METHODS

Various SL interaction models are known to exhibit IRO; here we consider a canonical example given by the pairwise potential [14]
$$
\varphi_{SL}(x) \equiv 4\epsilon(x^{-2\alpha} - x^{-\alpha}) + A\frac{e^{-x/\xi_R}}{x/\xi_R} \tag{1}
$$
where $x = r/d$ is a non-dimensionalized particle separation, $d$ is the measure of particle size, $\epsilon$ quantifies the attractive strength, and $A$ and $\xi_R$ respectively characterize the repulsion magnitude and range. We set $\alpha = 100$ in Eq. 1 to mimic archetypical colloids governed

∗ Contributed equally
† truskett@che.utexas.edu

by core repulsions with an attraction ranges of $O(1\%)$ of the core diameter induced via depletant effects. The long-ranged Yukawa tail mimics screened electrostatic interactions common to charge-stabilized suspensions. The corresponding RA potentials [17] are defined by $\varphi_{R A}(x) \equiv H(x_{0}-x) \varphi_{S L}(x)$, where $H$ is the Heaviside step function and $x_{0}$ is the nearest point for $x>1$ where $\varphi_{S L}(x)$ is zero, which eliminates the repulsive tail.

Model SL fluids defined by Eq. 1 can lose stability to micro-crystalline cluster phases at high attraction strengths [14], in contrast to many experimental systems of interest (e.g., proteins) that do not easily crystallize. To study the latter, we also examine a simple ternary mixture of SL particles designed to frustrate crystalliza- tion. The mixture pair potentials are described by

$$
\varphi_{S L \mid i, j}(x_{i, j}) \equiv 4[\epsilon+(1-2 \delta_{i, j}) \Delta_{\epsilon}](x_{i, j}^{-2 \alpha}-x_{i, j}^{-\alpha})+A \frac{e^{-x_{i, j} / \xi_{R}}}{x_{i, j} / \xi_{R}}
$$

where $\delta_{i, j}$ is the Kronecker delta, $i, j=-1,0,1$ corre spond to small, medium $(d=1)$, and large particles respectively, $x_{i, j} \equiv x-(1 / 2)(i+j) \Delta_{d}$, and pertur bative parameter shifts to interaction size and energy, $\Delta_{d}=0.158$ and $\Delta_{\epsilon}=0.25$, help to thwart crystalliza tion and promote mixing, respectively. We use systems comprising $20 \%$ small, $60 \%$ medium, and $20 \%$ large par ticles. This combination of $\Delta_{d}$ and composition repre sents a three-component approximation of $10 \%$ polydis persity in particle size.

In examining both models, we set various combi- nations of the repulsive range $\xi_{R}$ and the thermally non-dimensionalized repulsive strength $\beta A$ (where $\beta=$  $1 / k_{B} T$ and $k_{B}$ is the Boltzmann constant) while varying the non-dimensionalized attractive strength $\beta \epsilon$ . This treatment mimics systems for which the short- and long-range aspects of constituent interactions are ap- proximately orthogonal, such as colloids with screening lengths set by particle-solvent interactions and attrac- tions tuned via introduction of depletants [18].

To generate equilibrium particle configurations, weperform 3D molecular dynamics simulations of $N=$ 2960 particles interacting via Eqns. 1 and 2 in the NVT ensemble with periodic boundary conditions using LAMMPS [20]. Due to the steepness of the repulsion, we use an integration time-step of 0.0005, and due to the long-range repulsion, we include interactions out to a cut-off distance of $r_{cut }=8.0$ . For all state points, the temperature is fixed at $k_{B} T=1.0$ via a Nosé-Hoover thermostat with time-constant $\tau=1.0$ . We calculate the structure factor $S(k)$ from simulations by numerical Fourier Transform (FT) inversion of the radial distribu- tion function $g(r)$ . To determine whether state points are fluid, clustered, or percolating, we calculate cluster size distributions (CSDs), which quantify the probabilis- tic formation of $n$ -particle aggregates, where particles are considered part of the same aggregate if their cen- ters are within the narrow range of the attractive well.Similar to other studies $[14,15,17,18]$ , a system is considered clustered with aggregates of preferred size $n^{*}$ by the presence of a local maxima in the CSD at $n^{*}$  occurring in the range $1 \ll n^{*} \ll N$ , and is consid ered percolated (at the level of the box) by a CSD peak comprised of all particles, i.e., $n^{*} \simeq N$ .

![](./images/867757041916051881_1.jpg)

FIG. 1. (Color online). (a) Structure factors $S(k)$ for refer ence attractive (RA, red dashed) and short-range attractive long-range repulsive (SL, blue solid) fluids at packing frac- tion $\phi=0.125$ for repulsions with ranges $\xi_{R}$ and strengths BA. Curves are derived from integral equation theory, wherethe $\xi_{R}=10$ curves are shown for attraction $\beta \epsilon=4.35$  and the $\xi_{R}=2$ curves (shifted vertically) are shown for $\beta \epsilon=4.75$ . (b,c) $S(k)$ curves from (a) replotted to highlight $k \to 0$ behaviors. (d) Fourier transforms $\beta \omega(k)$ of the po tentials from (a) with $\xi_{R}=2$ curves shifted vertically. (e) RA and SL potentials $\beta \varphi(r)$ for the $\xi_{R}=2$ case.

To obtain analytical results for a broader range of po- tentials, we also derive theoretical thermodynamic and pair structure results via the Ornstein-Zernike (OZ) in- tegral equation relation $h(k) \equiv c(k)+\rho c(k) h(k)$ , where h(k) = FT[g(r)-1], c(k) = FT[c(r)], g(r) is the ra- dial distribution function, $c(r)$ is the direct correlation function and $\rho$ is the number density. The OZ rela tion is closed via the Percus- Yevick hard sphere ref- erence, non-linear optimized random phase approxima-tion, $c(r) \approx \exp [-\beta \varphi(r)]-1+G(r)$ , where $G(r)=0$  for $r>d$ while for $r \leq d$ it is optimized to enforce $h(r)=-1$ (thus, we approximate Eqn. 1 with a literal hard core for $r \leq d$ ) [21]. In carrying out these calcula tions, we consider only the Eqn. 1 potential since non- crystalline states are avoided due to the enforcement of homogeneity. This closure yields a spinodal locus at all densities, an important feature for the RA cases.

### III. RESULTS AND DISCUSSION

To begin our discussion, we first consider the behav- ior of the structure factor $S(k)$ for SL fluids with differ ent relative (integrated) repulsive strengths and corre-

sponding RA systems (see Fig. 1a-c) as predicted from integral equation theory. The two SL fluids exhibit pre-peaks characteristic of IRO at wavelengths $k_{SL}^{*} > 0$, indicating preferential structuring on microscopic lengthscales of $2\pi/k_{SL}^{*} \approx 12.6d$ and $5.0d$, respectively. In contrast, for the RA fluids lacking long-range repulsions, the short-range attractions drive ordering on the macroscopic lengthscale, corresponding to the peak at $k_{RA}^{*}=0$. Crucially, we see that for the very weak repulsive case $(\xi_R = 10, \beta A = 5 \times 10^{-4})$ , the $S(k)$ for the SL fluid traces the RA curve down to low-$k$, supporting the conceptual notion of SL fluids as perturbations to underlying RA fluids for which only the principal ordering lengthscale has been shifted.

To understand why one should naturally expect SL fluids to aggregate on smaller lengthscales than their RA counterparts, we examine in Fig. 1(d) the Fourier space analogs of the SL and RA pair potentials, $\omega(k) = \text{FT}[\varphi_0(r)]$, where $\varphi_0(r) = H(r-d)\varphi(r)$. Viewing the potentials in this way makes explicit the idea that structural oscillations of different lengthscales are weighted by the energy profile $\omega(k)$, which is evidenced by the close reciprocal correspondence between basins in $\omega(k)$ (Fig. 1(d)) and peaks in $S(k)$ (Fig. 1(a)). This connection can also be made more formal by considering microstate configurational energies (see Appendix A).

Moving beyond the above discussion concerning generic IRO, we demonstrate in Fig. 2 that particle clustering emerges when the thermal correlation length $\xi_T$ surpasses the characteristic lengthscale of interparticle repulsion $\xi_R$. Here, we estimate $\xi_T$ from the well-known $S(k)$ approximation (inverse expansion) near $k^{*}$ [21]:

$$
S(k) \equiv \frac{S(k^{*})}{1+(k-k^{*})^2 d^2 \xi_T^2} \tag{3}
$$

That $\xi_T$ is a correlation length is evident by considering the real-space form of Eqn. 3, $\lim_{r \to \infty} [g(r)-1] \propto r^{-1} \exp[-r/d\xi_T] \cos[rk^{*}-\theta]$, where $g(r)$ is the radial distribution function, $\theta$ is a constant, and $\xi_T$ gives the characteristic decay-length of static correlations while the cosine term reflects modulated structure. In practice, $\xi_T$ can be extracted from $S(k)$ by fitting $S(k^{*})/S(k)$ to the form $1+(k-k^{*})^2 d^2 \xi_T^2$ about $k^{*}$.

In Fig. 2(a), we catalog the phase behavior as a function of attractive strength $\beta\epsilon$ for various packing fractions $\phi$. It is evident that for the lower-density isochores, the $\xi_T \geq \xi_R$ criterion demarcates when clustering begins in our polydisperse system, as indicated by a characteristic CSD peak with increasing attractions (Fig. 2(c)) and reflected by a growing IRO pre-peak in $S(k)$ (Fig. 2(d)). As is intuitively expected and seen by others [15, 17, 22], for denser isochores like $\phi=0.250$, it is challenging to identify precisely when "clustering" begins because the CSD indicates box-wide percolation (geometrically merged clusters) even down to relatively low $\beta\epsilon$. Fig. 2(a) also shows that correlation lengths of monodisperse and polydisperse systems coincide upon approach to the $\xi_T=\xi_R$ threshold, where this boundary also approximately identifies where the monodisperse fluid loses stability with respect to formation of micro-crystalline clusters.

![](./images/867757041916051881_2.jpg)

FIG. 2. (Color online). (a) Symbols show thermal correlation lengths $\xi_T$ for SL simulations of polydisperse (filled) and monodisperse (unfilled) systems with attractive strengths $\beta\epsilon$ and packing fractions $\phi=0.050, 0.125$, and $0.250$. Symbol shapes indicate whether the state point is dispersed fluid (triangles), clustered (circle), or percolated (diamond), and the horizontal dashed line indicates $\xi_T=\xi_R$. Solid lines show $\xi_T$ calculated via theory. (b) Phase behavior calculated via theory for potentials from (a), including RA macrophase spinodal (red unfilled squares); SL curves (blue filled squares) corresponding to $\xi_T=2$ and $\xi_T=5$; and $S(k_{SL}^{*})=2.7$ curve (black x). ‘L+G’ indicates liquid-gas coexistence, ‘C’ indicates clustered phase, and ‘F’ indicates fluid phase. (c) Cluster size distributions indicating probability $p(n)$ of $n$-particle cluster formation and (d) $S(k)$ profiles from polydisperse simulations at $\phi=0.125$.

In Fig. 2(b), we also examine phase behaviors for the SL and RA fluids derived for a wider $\beta\epsilon-\phi$ parameter space via theory, which reveals close correspondence between the SL $\xi_T=\xi_R$ boundary and the spinodal associated with RA macrophase separation. Their similar shapes (and, in this case, locations), suggest that the SL $\xi_T=\xi_R$ boundary echoes the RA thermodynamic instability, where the frustrating repulsion has erased (or highly suppressed) liquid-gas coexistence in favor of clustering. (We also include the $\xi_T=5$ curve to demonstrate the general propagation of the RA spinodal shape with increasing $\beta\epsilon$.) As a further comparison, the empirical clustering condition $S(k_{SL}^{*}) \geq 2.7$ is also shown.

![](./images/867757041916051881_3.jpg)

FIG. 3. (Color online). (a) Phase diagrams calculated via theory, comprising RA macrophase spinodals (unfilled red symbols) and SL $\xi_{T}=\xi_{R}$ curves (filled blue symbols) for $\xi_{R}=10$ and two repulsive strengths $\beta A$. (b) RA spinodals and curves along which $S(k_{SL}^{*})=2.7$ (filled black symbols) for same systems as in (a). (c) Phase diagram calculated via theory comprising RA macrophase spinodal (unfilled red triangles); SL curves corresponding to macrophase spinodal at low $\phi$ (right-pointing blue triangles) and $\xi_{T}=\xi_{R}=2$ at high $\phi$ (left-pointing blue triangles); and disorder line (purple squares) in the fluid region (see text). 'L+G' indicates liquid-gas coexistence, 'C' indicates clustered phase, and 'F' indicates fluid phase.

While it lies within similar proximity to the RA spin- odal, it possesses a noticeably different, shallower con- tour.

To elucidate deeper connections between the contours in Fig. 2(b), we explore in Fig. 3 whether the $\xi_{T}=\xi_{R}$ and RA spinodal boundaries truly converge for ultra- weak repulsions, which might be expected if the latter can be considered a natural weak-repulsion limit of the former. In Fig. 3(a-b), we examine two potentials with different repulsive strengths: for $\beta A=1 \times 10^{-2}$, the re pulsion is evidently "strong" and there is no overlap be- tween the $\xi_{T}=\xi_{R}$ and RA spinodal boundaries (note: this highlights that these boundaries do not generally overlap as in Fig. 2(b)). However, as repulsion strength is lowered to $\beta A \leq 1 \times 10^{-5}$, the two curves collapse and become truly indistinguishable, reflecting a deep SL-RA connection. In Fig. 3(b), we also show corre- sponding $S(k_{SL}^{*})=2.7$ curves. Clear discrepancies in shape are apparent when comparing the RA spinodals and the $S(k_{SL}^{*})=2.7$ boundaries, and the two types of curves increasingly move apart as $\beta A$ is reduced.

To further generalize the connection of the RA spin- odal to the phase behaviors of SL systems, we con- sider in Fig. 3(c) a less long-ranged weak repulsion $(\xi_{R}=2, \beta A=5 \times 10^{-3})$, which exhibits intriguing properties: a true SL spinodal separation occurs for $\phi \leq 0.09$, while for higher volume fractions there is a $\xi_{T}=\xi_{R}$ clustering boundary. The low-density fluid also exhibits a disorder line, below which the IRO peak is present and above which the IRO peak transitions to a $k_{SL}^{*}=0$ peak. The intimate correspondence between the SL boundaries and the RA spinodal further reflects that the condition $\xi_{T}=\xi_{R}$ reflects a muted thermo dynamic instability, which for very weak repulsions can also emerge within the SL fluid itself.

![](./images/867757041916051881_4.jpg)

FIG. 4. (Color online). Cluster phase simulation snap- shots of polydisperse (a) and monodisperse (b) systems at $\phi=0.125$ with attractive strength $\beta \epsilon=5.2$ and repulsions defined by $\xi_{R}=2$ and $\beta A=0.20$. Particles comprising a single cluster (determined at time $t$) are rendered opaque in their positions at times $t$ (left) and $t'=t+\Delta t$ (right). The lag time is $\Delta t=25 \tau_{d}$, where $\tau_{d}=d^{2}/D$ is the characteristic time for $d=1$ particles to diffuse and $D$ is the long-time bulk diffusion coefficient determined via mean-squared dis- placements. Colors correspond to small, medium $(d=1)$, and large particles, which are shaded yellow, red, and blue, respectively. Visualizations created with VMD [23].

Finally, we consider the morphologies and lifetimes of the clusters that form in polydisperse and monodisperse SL systems. Clusters in the former exhibit amorphous and irregular shapes, as exemplified by the simulation snapshots in Fig. 4(a), which correspond to the sys- tem in Fig. 2 at conditions slightly above the clustering transition. Here, it is evident based on the time-lag snapshots that the clusters are transient and contin- uously redistribute particles to create new clusters at the expense of others. By significantly increasing the attractive strength $\beta \epsilon$, one can eventually observe ar- rested, percolating, amorphous gels as exemplified by the simulation snapshots for $\phi=0.125$ systems in Fig.5. Interestingly, our model gels may be thermoreversible with no local crystallinity, possibly providing a simpler alternative to valence-limited gel-formers [24]. Ther-

moreversibility is highly desired to facilitate fabrication of massively reconfigurable, reversible materials.

In contrast, monodisperse systems at similar attraction strengths can undergo highly regular clustering via local crystallization, as exemplified in Figure 4(b). While the crystalline nature of such simulated clusters has been observed previously by others [14, 15, 18], we do note that the relatively weaker repulsion examined here drives formation of much larger clusters that are more obviously crystalline in nature. The crystalline clusters are relatively static objects once formed, as demonstrated by the time-lag snapshots, in direct contrast to the amorphous clusters.

![](./images/867757041916051881_5.jpg)

FIG. 5. (Color online). Cluster phase simulation snapshots of polydisperse systems at $\phi = 0.125$ with various attractive strengths $\beta\epsilon$ and repulsions defined by $\xi_R = 2$ and $\beta A = 0.20$. In all snapshots, particles comprising a single cluster (determined at time $t$) are rendered opaque in their positions at time $t$. For cases (a) and (b) that are not gelled, the same particles are also shown in their positions at $t' = t+\Delta t$. The lag time in (a) and (b) $\Delta t = 25\tau_d$, where $\tau_d = d^2/D$ is the characteristic time for $d = 1$ particles to diffuse and $D$ is the long-time bulk diffusion coefficient determined via mean-squared displacements. For cases (c) and (d), the configurations are dynamically arrested and $\tau_d$ cannot be practically measured within the timescale of simulations. Colors correspond to small, medium ($d=1$), and large particles, which are shaded yellow, red, and blue, respectively. Visualizations created with VMD [23].

## IV. CONCLUDING REMARKS
In closing, we have presented a new framework for understanding and detecting cluster phases in SL fluids based on the thermal correlation length $\xi_T$. This framework should prove useful for probing micro-structural transitions in diverse systems governed by frustrated interactions, e.g., lattice spin models with opposing nearest-neighbor and higher-order couplings. We have also presented the first non-microcrystallizing SL fluid, which exhibits amorphous transient clusters; this should prove useful for examining the (zeroth order) physics of real dispersions known to be resistant to crystallization, e.g., proteins.

Finally, we remark that the $\xi_T = \xi_R$ clustering criterion can be implemented in experiments provided that, in addition to extracting $\xi_T$ from an $S(k)$ profile (described earlier), one can also obtain a reasonable measure of the repulsive lengthscale between particles $\xi_R$. For systems accurately described by simple screening models, $\xi_R$ can be directly estimated. Otherwise, one can first obtain the $r$-space total correlation function $h(r)$ via an inverse FT of $S(k)$. Likewise, one can calculate the direct correlation function $c(k) = \rho^{-1} - [\rho S(k)]^{-1}$ and then obtain its $r$-space equivalent $c(r) = \text{FT}^{-1}[c(k)]$, which provides information about the interparticle interactions because $\lim_{r \to \infty} c(r) \approx \varphi(r)$ [21]. By plotting $\ln\{|rh(r)|\}$ and $\ln\{|rc(r)|\}$ versus $r$ (where $|x|$ is the absolute value of $x$) and comparing their (negative) slopes, one directly compares the range of interparticle correlations (as captured by $\xi_T$) and the characteristic range of the interparticle interactions, respectively. Thus, given an $S(k)$ profile exhibiting an IRO peak, if $\ln\{|rh(r)|\}$ decays more slowly than $\ln\{|rc(r)|\}$, then the $\xi_T$ associated with IRO exceeds the characteristic (repulsive) lengthscale $\xi_R$.

## ACKNOWLEDGMENTS
This work was partially supported by the National Science Foundation (1247945), the Welch Foundation (F-1696), and the Gulf of Mexico Research Initiative. We acknowledge the Texas Advanced Computing Center (TACC) at The University of Texas at Austin for providing HPC resources.

## APPENDIX A: FOURIER-SPACE CONNECTIONS BETWEEN $\omega(k)$ AND $S(k)$
An $N$ particle configuration $[\mathbf{r}_i]$ that does not violate the hard core constraint is weighted according to the Boltzmann factor $\exp[-\beta\Omega([\mathbf{r}_i])]$, where:
$$
\Omega([\mathbf{r}_i]) \equiv \frac{1}{2} \sum_{i \neq j=1}^N \varphi_0(|\mathbf{r}_i - \mathbf{r}_j|) \tag{A1}
$$
is the total potential energy due to the non-hard-core portion of the pair potential $\varphi_0(r)$. Eqn. A1 can be

recast using the definition of the 3D dirac delta function $\delta(\mathbf{x})$:

$$
\Omega([\mathbf{r}_{i}]) \equiv \frac{1}{2} \sum_{i \neq j=1}^{N} \int d\mathbf{R}_{1} \int d\mathbf{R}_{2} \delta(\mathbf{r}_{i} - \mathbf{R}_{1}) \varphi_{0}(|\mathbf{R}_{1} - \mathbf{R}_{2}|) \delta(\mathbf{r}_{j} - \mathbf{R}_{2}) \tag{A2}
$$

Since Eqn. A2 is a convolution with respect to $\mathbf{R}_{1}$ and $\mathbf{R}_{2}$, it can be recast as a single integral in Fourier space using the Fourier transformed potential $\omega(k) \equiv \text{FT}[\varphi_{0}(r)]$:

$$
\Omega([\mathbf{r}_{i}]) \equiv \frac{1}{2} \sum_{i \neq j=1}^{N} \frac{1}{(2\pi)^{3}} \int d\mathbf{k} e^{-i\mathbf{k} \cdot \mathbf{r}_{i}} \omega(k) e^{i\mathbf{k} \cdot \mathbf{r}_{j}} \tag{A3}
$$

Moving the sum inside the integral in Eqn. A3 and using the definition of the non-ensemble averaged total correlation function,

$$
\tilde{h}(k; [\mathbf{r}_{i}]) \equiv (\rho N)^{-1} \sum_{i \neq j=1}^{N} \exp[-i\mathbf{k} \cdot (\mathbf{r}_{i} - \mathbf{r}_{j})] \tag{A4}
$$

one can subsequently write

$$
\Omega([\mathbf{r}_{i}]) = \frac{N \rho}{2(2\pi)^{3}} \int d\mathbf{k} \omega(k) \tilde{h}(k; [\mathbf{r}_{i}]) \tag{A5}
$$

which makes explicit the role $\omega(k)$ plays in favoring $[\mathbf{r}_{i}]$ states possessing certain oscillatory structural correlations. Namely, any thermodynamically favorable configuration $[\mathbf{r}_{i}^{*}]$, as weighted by $\exp[-\beta \Omega([\mathbf{r}_{i}])]$, is captured by the equilibrium average total correlation function $h(k) \approx \tilde{h}(k; [\mathbf{r}_{i}^{*}])$. In turn, $\omega(k)$ sets the energetic "preference" for configurations structured at certain wavelengths $k$, which appear as peaks in the structure factor since $S(k) \equiv 1 + \rho h(k)$.

[1] D. Langevin, Accounts of Chemical Research **21**, 255 (1988), http://dx.doi.org/10.1021/ar00151a001.

[2] E. Helfand, Accounts of Chemical Research **8**, 295 (1975), http://dx.doi.org/10.1021/ar50093a002.

[3] I. W. Hamley, "Introduction to block copolymers," in *Developments in Block Copolymer Science and Technology* (John Wiley & Sons, Ltd, 2004) pp. 1–29.

[4] M. Cynthia Goh, W. Goldburg, and C. Knobler, Phys. Rev. Lett. **58**, 1008 (1987).

[5] R. B. Jadrich and K. S. Schweizer, Phys. Rev. Lett. **113**, 208302 (2014).

[6] A. Yethiraj and A. van Blaaderen, Nature **421**, 513 (2003).

[7] A. Stradner, H. Sedgwick, F. Cardinaux, W. C. K. Poon, S. U. Egelhaaf, and P. Schurtenberger, Nature **432**, 492 (2004).

[8] L. Porcar, P. Falus, W.-R. Chen, A. Faraone, E. Fratini, K. Hong, P. Baglioni, and Y. Liu, J. Phys. Chem. Lett. **1**, 126 (2010), http://dx.doi.org/10.1021/jz900127c.

[9] K. P. Johnston, J. A. Maynard, T. M. Truskett, A. U. Borwankar, M. A. Miller, B. K. Wilson, A. K. Dinin, T. A. Khan, and K. J. Kaczorowski, ACS Nano **6**, 1357 (2012), http://dx.doi.org/10.1021/nn204166z.

[10] T. Lafitte, S. K. Kumar, and A. Z. Panagiotopoulos, Soft Matter **10**, 786 (2014).

[11] D. Sararuf, F. Roosen-Runge, M. Grimaldo, F. Zanini, R. Schweins, T. Seydel, F. Zhang, R. Roth, M. Oettel, and F. Schreiber, Soft Matter **10**, 894 (2014).

[12] Y. Liu, L. Porcar, J. Chen, W.-R. Chen, P. Falus, A. Faraone, E. Fratini, K. Hong, and P. Baglioni, J. Phys. Chem. B **115**, 7238 (2011), http://dx.doi.org/10.1021/jp109333c.

[13] S. Schemmel, D. Akcakayiran, G. Rother, A. Brulet, B. Farago, T. Hellweg, and G. H. Findenegg, MRS Proceedings **790**, 1 (2003), http://dx.doi.org/10.1557/PROC-790-P7.2.

[14] F. Sciortino, S. Mossa, E. Zaccarelli, and P. Tartaglia, Phys. Rev. Lett. **93**, 055701 (2004).

[15] J. C. F. Toledano, F. Sciortino, and E. Zaccarelli, Soft Matter **5**, 2390 (2009).

[16] J.-M. Bomont, J.-L. Bretonnet, D. Costa, and J.-P. Hansen, J. Chem. Phys. **137**, 011101 (2012).

[17] P. D. Godfrin, N. E. Valadez-Perez, R. Castaneda-Priego, N. J. Wagner, and Y. Liu, Soft Matter **10**, 5061 (2014).

[18] E. Mani, W. Lechner, W. K. Kegel, and P. G. Bolhuis, Soft Matter **10**, 4479 (2014).

[19] J. P. Hansen and L. Verlet, Phys. Rev. **184**, 151 (1969).

[20] S. Plimpton, J. Comput. Phys. **117**, 1 (1995).

[21] J.-P. Hansen and I. R. McDonald, *Theory of Simple Liquids*, 3rd ed. (Academic Press, New York, NY, USA, 2006).

[22] N. E. Valadez-Perez, R. Castaneda-Priego, and Y. Liu, RSC Adv. **3**, 25110 (2013).

[23] W. Humphrey, A. Dalke, and K. Schulten, J. Molec. Graphics **14**, 33 (1996).

[24] B. Ruzicka, E. Zaccarelli, Z. L., R. Angelini, M. Sztucki, A. Moussaïd, T. Narayanan, and F. Sciortino, Nature Mat. **10**, 56 (2011).