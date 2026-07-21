View Article Online
View Journal

# Soft Matter

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: A. Mascioli, C. J. Burke, M. Q. Giso and T. Atherton, *Soft Matter*, 2017, DOI: 10.1039/C7SM00179G.

![](./images/813106863666102273_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/813106863666102273_2.jpg)

rsc.li/soft-matter-journal

# Percolation transition in the packing of bidispersed particles on curved surfaces $^\dagger$

Andrew M. Mascioli$^a$, Christopher J. Burke$^a$, Mathew Q. Giso$^a$, and Timothy J. Atherton$^{a,b}$

We study packings of bidispersed spherical particles on a spherical surface. The presence of curvature necessitates defects even for monodispersed particles; bidispersity either leads to a more disordered packing for nearly equal radii, or a higher fill fraction when the smaller particles are accomodated in the interstices of the larger spheres. Variation in the packing fraction is explained by a percolation transition, as chains of defects or scars previously discovered in the monodispersed case grow and eventually disconnect the neighbor graph.

## 1 Introduction
Bidispersed mixtures of hard spheres are an important elementary model of a glass transition$^1$: at high temperature and low density they flow freely, while as temperature is reduced they become kinetically arrested and form rigid but highly disordered structures$^2$. At zero temperature and stress, a similar jamming transition to rigidity occurs as a function of density$^{3,4}$ which in 2D tends to occur around a packing fraction of $\Phi=0.84^{5,6}$. Jammed structures exhibit distinctive properties including isostaticity: the average number of inter-particle contacts is the minimum number required for mechanical stability$^7$. Powerful mathematical tools exist$^8$ to classify jammed and glassy packings of hard particles according to a hierarchy, depending on where individual particles, groups or boundary deformations can unjam the system$^9$.

Sphere packings, the high density and zero temperature limit of these processes, have been extensively studied in both 2D and 3D Euclidean space$^{2,4,10,11}$ revealing strong dimensional dependence: 2D monodispersed spheres tend to crystallize readily, because the locally dense hexagonal packing fills space; in 3D the locally dense tetrahedral packing cannot fill space, permitting a random close packed structure that is the subject of much debate$^{12-14}$. Even in 2D, however, disorder can be induced in bidispersed systems. Molecular dynamics simulations have shown that there is a transition from order to disorder as the degree of bidispersity is increased$^{15-18}$, and statistical models of bidispersed particle packings have been used to predict the local features of disordered bidispersed packings$^{19,20}$. The degree of order or disorder can be measured by an order parameter such as the hexatic bond orientational order$^{21}$. An exponentially large number of packings exist between the crystalline and disordered packings in flat space, showing that the glass transition in binary disks is not ideal and that a continuous trade-off between packing fraction and configurational entropy is possible$^{22}$.

Crystalline order is geometrically frustrated on curved surfaces$^{23}$: an incompatibility between the preferred hexagonal symmetry of the crystalline packing and the topology of the surface necessitates a minimal number of defects—particles with a number of neighbors other than 6—to accommodate the curvature. For monodispersed particles, the packings are mainly crystalline with a transition between isolated defects for small particle number and chains of defects or scars akin to grain boundaries in bulk systems that occur above a critical number of particles $N_c\approx110$ and grow with system size$^{24,25}$. The scars may join in asterisk-like motifs$^{25}$ and are aligned by anisotropic curvature$^{26}$. Jammed packings on spheres or spherical codes have recently been studied in multiple dimensions$^{27}$.

In this paper, we determine how curvature affects the packing of bidispersed particles on a spherical surface to establish how the crystalline to disordered transition is affected. We characterize the packing fraction, connectivity and hexatic order parameter as a function of particle number $N$, fraction of large particles $\chi=N_L/N$ and bidispersity $b=(r_1-r_2)/(r_1+r_2)$ where $r_1$ and $r_2$ are the radii of the particles and $r_1\geq r_2$. By identifying topological defects from the neighbor graph we show that variation in these parameters is explained by a percolation transition due to growth and connectivity of the scar network, as well as commensurate local arrangements of particles.

## 2 Model
Packings with high coverage fraction were produced using a surface relaxation algorithm described in the Methods section below. Configurations produced by this procedure are referred to to

---

$^a$Department of Physics and Astronomy, Tufts University, 574 Boston Avenue, Medford, Massachusetts 02155, USA
$^b$Email: timothy.atherton@tufts.edu

![](./images/813106863666102273_3.jpg)

Fig. 1 Packing fraction $\Phi$ as a function of bidispersity $b=(r_1-r_2)/(r_1+r_2)$ where $r_1>r_2$ for different particle numbers $N$ and a fraction $\chi=0.5$ of large particles. The maximum $b=\sqrt{3}-1\approx0.73$, indicated with a vertical dashed line, occurs for an Apollonian packing, i.e. where smaller particles fit in the interstices of the larger particles as depicted in the upper inset. Lower inset: comparison of the packing fraction of arrested (gray) and jammed (black) packings for $N=800$ particles.

as arrested, because they remain metastable if the simulation is restarted; eventually, however, a Monte Carlo move will unjam the arrested configuration, potentially facilitating further relaxation and a consequent increase in the packing fraction. This process occurs in real glasses and is known as aging. Extending a powerful technique due to Donev et al. $^{8}$, we artificially age the arrested structures using a linear program to find and execute an unjamming motion of the particles and further relax the surface. Iterative unjamming and relaxation guides the packing toward a state that is collectively jammed with respect to movement of the particles and further relaxation. As we report elsewhere $^{28}$, the convergence of this procedure is greatly accelerated by preconditioning the packing, attaching a short range repulsive interaction to the particles beyond the hard inter-penetrability constraint and minimizing the corresponding energy by gradient descent. This procedure moves the particles into the center of the feasible region from which the linear program is more effectively able to identify an unjamming motion. Each arrested structure was subjected to this artificial aging process to produce a corresponding ensemble of jammed structures.

For monodispersed particles $^{24}$, neighbors are assigned from a Voronoi tessellation $^{29}$ of the particle centers of mass, partitioning the surface into $N$ polygonal regions closest to a particular particle. Two particles are neighbors if they share an adjacent edge on the Voronoi tessellation. Generalizing this construction to bidispersed particles with a weighted distance fails to uniquely assign all points on the surface to a particle; two proposed alternatives $^{20}$ are the radical tessellation and the navigation map, both of which recover the Voronoi tessellation in the limit of monodispersed spheres. The radical tessellation utilizes the radical plane as a separatrix between each pair of particles; the navigation map partitions the surface into regions closest to the surface of the particles rather than their center of mass. We found little difference between quantities calculated from these constructions and use the radical tessellation exclusively in the remainder of the paper. From the radical tessellation, the adjoint neighbor graph was constructed for each packing and the coordination number determined for each particle.

## 3 Results and Discussion

For each value of bidispersity on the interval $b\in[0,1]$ with a resolution of $\Delta b=0.005$, an ensemble of 20 jammed configurations was generated with $\chi=1/2$ and varying number of particles $N$. The packing fraction $\Phi$, i.e. the fraction of the surface enclosed by the particles, was calculated for each configuration and shown in Fig. 1. For particle numbers above about $N=200$, slight deviations from the monodispersed case immediately introduce disorder and reduce the packing fraction as expected. Above a critical value of bidispersity $b_c\sim0.09$, however, we see a transition and $\Phi$ increases, with an apparent shoulder at $b\approx0.4$, up to a maximum value of $\Phi\approx0.87$ at $b=b_A\approx0.7$ and then decreases as $b\rightarrow1$. For $N<200$, $\Phi$ increases monotonically up to a maximum at a slightly lower value of $b\sim0.6$. In the lower inset of Fig. 1, we compare the packing fraction for 800 particles for the ensemble of arrested and jammed packings. It is clear that the arrested structures are slightly less efficiently packed, but the shape of the plots is identical. We find similar results for other $N$; this correspondence affirms that the trends are geometric in origin rather than due to variation in the performance of the algorithm at different $b$.

The maximum at $b=b_A$ is immediately explicable: it corresponds to the special point at which the smaller particles fit exactly in the interstices between the larger particles, depicted in the upper inset of Fig. 1. We denote this the Apollonian point in reference to the tiling. Packings around and above $b_A$ appear mostly crystalline with the smaller particles separated into the interstices; the packing fraction for $N$ particles at $b=1$ corresponds exactly to that for $N/2$ particles at $b=0$. No such immediate explanation is obvious for the low and medium bidispersity results, which appear to be well mixed; we therefore seek a more detailed understanding of the structure.

One structural measure that reflects the degree to which the packings are locally crystalline is the hexatic order parameter $\psi_6=\langle\exp(i6\theta_i)\rangle$, where the average is taken over the neighboring particles. This is shown calculated from the dataset as a function of $b$ and $N$ in Fig. 2A. A maximum occurs for all $N$ at $b=0$ as expected; the value is reduced for smaller $N$ reflecting the disruption of crystallinity by the curvature. The hexatic order drops with $b$, reaches a minimum around $b\sim0.45$, rises and then forms a plateau above the Apollonian point, albeit at a value significantly lower than the $b=0$ case, because here the large particles have a higher coordination number. Variation in $\psi_6$ is significantly attenuated for low $N$ where the influence of the curvature is stronger.

To see whether hexatic order is replaced by other ordering, we calculated $n$-atic order parameters $\psi_n=\langle\exp(in\theta_i)\rangle$ for $N=1600$ as a function of $b$; the results are plotted in Fig. 2B. In contrast to the hexatic order parameter, $\psi_n$ for $n\neq6$ increases with $b$ from $b=0$; moreover all $\psi_n$ exhibit a plateau above the Apollonian

![](./images/813106863666102273_4.jpg)

Fig. 2 Ordering of the packings. A Hexatic order parameter as a function of bidispersity $b$ for different $N$. B Local order parameters $\psi_{n}$ as a function $b$ for a jammed packing of $N=1600$ particles. Hexatic order dominates except intermediate values of $b$ where eight- and ten-fold order possess maxima. C and D Commensurate configurations with eight and tenfold order that occur at $b=\sqrt{2}-1 \approx 0.41$ and $b=(\sqrt{5}-1) / 2 \approx 0.61$ respectively. E Average coordination number for large-large (solid lines), large-small (dashed lines) and small-small (dotted lines) inter-particle contacts for varying $N$. F Pair correlation function $g(s)$ and G orientational correlation function $g_{6}(s)$, each shown for values of bidispersity $b$ from 0.005 to 0.212 in steps of 0.030.

point confirming the distinct nature of this regime. Several val-
ues, $n=5,8,10,11$ of which 8 and 10 are the most prominent, have
$\psi_{n}$ narrowly greater than $\psi_{6}$ for intermediate values of $b$ and pos-
sess maxima at $b=0.45$ and $b=0.6$ respectively. Examining the
packings, the peak in eightfold order is due to the presence of
octagonally coordinated arrangements: a common and commen-
surate motif, depicted in Fig. 2C, where four large and four small
particles are arranged around a central large particle, is allowed
first for $b=\sqrt{2}-1 \approx 0.41$, which coincides with the position of
the shoulder in the plot of $\Phi(b)$ in Fig. 1. The tenfold peak is
explained by an analogous decagonally coordinated motif, shown
in Fig. 2D, that occurs at $b=(\sqrt{5}-1) / 2 \approx 0.61$. A variety of
other commensurate motifs exist for $b$ around 0.4 with different
mixtures of large and small neighboring particles and appear to
cause the shoulder in $\Phi$. It is interesting to note that decatic
ordering: 10-fold rotational symmetry is incompatible with long
range order and is rarely seen in packings in flat space with the
exception of quasicrystals $^{30-32}$. As long range order is also incom-
patible with curvature, it appears that curvature may promote the
increased 10-fold ordering.

We now examine the coordination number directly. In Fig.
2E, we plot the average coordination number per particle, sep-
arated into large-large, large-small and small-small contacts and
for different $N$. At infinitesimal $b$, each particle has six neigh-
bors, three smaller and three larger on average. With increas-
ing $b$, the number of large-small contacts per particle remains
a constant value of three; larger particles gain more large neigh-
bors while smaller particles lose small contacts. At the Apollonian
point, the smaller particles are surrounded by three larger neigh-
bors, while the larger particles are on average surrounded by six
large neighbors and three smaller neighbors. For $b$ beyond the
Apollonian point $b_{A}$, the coordination numbers remain constant,
consistent with the discussion above where smaller particles are
caged within the interstices of the larger particles. Smaller values
of $N$ follow similar trends, but tend to have lower coordination
numbers.

Finally, we calculated two measures of structural order, the pair
correlation function $g(s)$ and bond orientational correlation func-
tion $g_{6}(s)$, that encode the particle's local environment $^{33}$. Results
are displayed in Fig. 2F and G respectively. The pair correlation
function $g(s)$ for $b=0$ shows persistent peaks at large $s$ indicative
of long range order and a split second peak in agreement with
previous studies in flat space $^{34}$. As bidispersity is increased to
0.06, the split peaks become a single peak, representing the dis-
ruption of local hexagonal packing, but the long range order per-
sists. Proceeding to $b=0.09, g(s)$ is now flat at large $s$, indicating
that the long range order has disappeared. This is the same value
of bidispersity at the minimum in $\Phi$ at $b_{c}$ was observed in Fig. 1
and is our first indication that this minimum is associated with
the disruption of long range order. Above this value of $b, g(s)$ re-
tains short range order, but the correlation length decreases with
$b$. Plots of $g_{6}(s)$ in Fig. 2E show an abrupt drop in the value
of $g_{6}(s)$ for small $s$ at $b=0.06$ and a reduction in the associated
correlation length with increasing $b$. For all values of $b, g_{6}$ ap-
proaches a constant at large $s$; there is no sign of algebraic decay
that would indicate a hexatic phase structure.

![](./images/813106863666102273_5.jpg)

Fig. 3 Percolation transition. A Fraction of particles $1-\phi_{6}$ with coordination number $C \neq 6$ as a function of bidispersity. B Representative defect subgraphs different $b$ illustrating growth and connection of the scar network. C Comparison with random percolation: a fraction $p$ sites are randomly selected on a $b=0, N=800$ neighbor graph. Shown is the fraction of simulations where the selected sites form a connected structure (gray solid line) and the fraction where the non-selected sites retain global connectivity (black solid line). Points show the fraction of simulations where the hexatic (black points) and non-hexatic subgraphs remain connected. D Packing fraction of particles as a function of the non-hexatic fraction $1-\phi_{6}$. Black points have a connected hexatic component; gray points indicate a disconnected hexatic component. E Size of the largest connected component for random percolation (solid lines) and bidispersed neighbor graphs (points). F Fitted fractal dimension of the cluster size as a function of the selected fraction for random percolation (black solid lines) and bidispersed neighbor graphs (black points). The cluster size as a function of selected fraction is also shown for bidispersed neighbor graphs; the vertical gray bar indicates where the cluster size has saturated due to finite system size.

We turn to an alternative measure of crystallinity, the fraction $\phi_{6}$ of particles that possess a coordination number of 6. In Fig. 3A, we plot $1-\phi_{6}$ as a function of bidispersity revealing a transition: as $b$ increases from zero, $1-\phi_{6}$ is approximately constant then rises rapidly above $b=0.05$, reaching a value of $\frac{1}{2}$ at $b=b_{p}=0.15$. Above bidispersity $b \approx 0.5$, a vanishing fraction of particles possess six neighbors. These trends persist for all values of $N$ shown, but $1-\phi_{6}$ is larger at $b=0$ for small $N$ since topology mandates a minimal number of defects.

To understand this transition further, it is necessary to examine the microstructural information encoded in the neighbor graphs, the adjoint graph of the radical tessellation. We crudely separate the crystalline and non-crystalline components by deleting from a neighbor graph all vertices that have six neighbors, yielding the "non-hexatic" subgraph. Illustrative examples of these sub-graphs are depicted in Fig. 3B. For $b=0$ the subgraph consists of small disconnected components corresponding to the previously-studied scars, which are essentially linear in morphology, with a small number of branches. As bidispersity increases to $b=0.1$, just below $b_{p}$, the connected subgraphs are still recognizably scar-like in nature, but have a branching morphology and are substantially longer. By $b=0.14$, close to $b_{p}$, the defect subgraph remains disconnected, but is now dominated by a few large connected graphs that are mostly linear with branches. Finally, above $b_{p}$ at $b=0.2$ the defect subgraph is now mostly a single connected structure with a small number of additional isolated defects; it is no longer branching, but with linear sections that link into a foam-like structure. For $b=0.3$, the defect subgraph retains this structure, but is more densely connected. The gradual growth and long-range connection of the non-hexatic subgraph due to bidispersity is therefore a percolation transition that occurs: As $b$ increases around $b_{p}$, the number of sites participating in the non-hexatic subgraph increases until they form a connected structure.

Percolation transitions are well-studied $^{35,36}$. The canonical formulation is: given a network, and selecting a fraction $p$ sites, what is the probability that one of the selected sites belongs to a long-range connected structure? Clearly, the system under consideration cannot be precisely mapped onto this problem because the neighbor graph changes with $b$. However, by averaging over all particle pairs in Fig. 2B we see that the mean coordination number remains 6 for all $b$. Thus, we examine the canonical percolation problem on the neighbor graph of a monodispersed packing for $N=800$ particles as a proxy. From such a graph, we randomly select a fraction $p$ sites and repeat this procedure to form $n$ trials. Plotted in Fig. 3C is the fraction of trials where the selected components form a connected structure (gray line) and where the remaining components retain their connectivity (black line).

We compare this to the bidispersity percolation transition by the placing the non-hexatic subgraph in correspondence to the selected subgraph in the random percolation model; the selected fraction is therefore $p=1-\phi_{6}$. The fraction of connected hexatic and non-hexatic subgraphs at each value of $p$ is plotted as points in Fig. 3C, showing that the percolation thresholds are in good agreement. In order of increasing $p$: at $p=0.2$, the hexatic subgraph begins to become disconnected, 50% of simulations

have disconnected hexatic subgraphs at $p=0.35$ and the hexatic subgraph is fully disconnected by $p=0.5$. Connection of the non-hexatic subgraph and disconnection of the hexatic subgraph are complementary processes, and hence the traces in Fig. 3C are reflections of one another about $p=0.5$. Consequently, the non-hexatic subgraph starts to become connected at $p=0.5$; is 50% likely to be connected at $p=0.65$ fully connected by $p=0.8$. Using the relation from $1-\phi_{6}$ and $b$ from Fig. 3A, we can map this sequence of events onto values of bidispersity. Hexatic disconnection starts at $b=0.075$, is 50% likely to be connected at $b=0.1$ and complete by $b=0.15$; the non-hexatic component starts to become connected at $b=0.15$, is 50% likely to be connected at $b=0.2$ and fully connected by $b=0.3$ respectively.

The minimum in $\Phi$ at $b_{c}=0.09$, therefore, is associated with disconnection of the hexatic fraction of the neighbor graph, rather than percolation of the scars. We make this explicit in Fig. 3D, which displays $\Phi$ as a function of $1-\phi_{6}$ for each simulation in our dataset, colored by whether the hexatic subgraph remains connected or not.

To further test the correspondence of scar growth and connection to random percolation theory, we also computed the size of the largest connected component of the selected and unselected subgraphs, plotted as solid lines in Fig. 3E. Results from the bidispersed neighbor graphs, using $1-\phi_{6}=p$, are plotted as points in Fig. 3E. There is excellent agreement between the two processes.

Another quantity of interest is the cluster radius $R$,

$$
2R^{2}=\sum_{ij}\frac{d_{ij}^{2}}{n^{2}}, \tag{1}
$$

where the sum is taken over all pairs of particles belonging to a connected cluster, $n$ is the number of sites in the cluster and $d_{ij}$ is the distance between the centroids of two particles $i$ and $j$ in the cluster. Here, we use the arclength distance between two particles rather than the Euclidean distance. Near the percolation threshold, the cluster size scales as the cluster radius as a power law,

$$
n_{c} \propto R^{D}, \tag{2}
$$

where the exponent $D$ is referred to in the percolation literature as the fractal dimension. $D$ is, according to percolation theory, a universal parameter that depends only on the dimensionality of the system and independent of the details of the lattice. In the limit $L \to \infty$, $D \to 1.896$ in 2D and $\approx 2.5$ in $3D^{35}$. Studies in 2D Euclidean space of random packings of bidispersed disks$^{37}$ and dimers$^{38}$ reproduce these predicted values. We calculated cluster radii and corresponding cluster size both from our neighbor graphs of bidispersed packings as well as the random percolation model on a monodispersed graph, and fitted these to a power law. Fig. 3F shows the results for random percolation (black solid lines) and bidispersed neighbor graphs (black points) which are in good agreement. At the percolation point $p=0.65$, the fractal dimension is $\sim 1.86$ which is close to the 2D universal value. The cluster size is also shown as a function of $p$ in 3F, and saturates at $p=0.65$, verifying that this is indeed the percolation point. A more detailed study to establish whether the residual discrepancy in $D$ is due to the curved space is left to future work.

From the strong agreement between connected fraction and fraction belonging to the connected component as a function of $p$ as well as cluster radius scaling, we infer that the qualitative features of the bidispersity percolation transition are well predicted by a random percolation transition on the monodispersed neighbor graph. To test this further, we attempted to disrupt the transition by varying the fraction of large particles $\chi=N_{L}/N$, motivated by the idea that growth of the scars might be prevented if sufficiently few minority particles are present. Results are shown in Fig. 4.

First we examine the effect of stoichiometry on the structure. The packing fraction for several values of $\chi$ is shown in Fig. 4A. Small values of $\chi$ lead to a dramatic enhancement of the packing fraction around the Apollonian point, while the packing fraction is less sensitive to $b$ for $\chi$ close to 1. This might be anticipated because a small number of large particles, the low $\chi$ limit, can create voids in the packings of small particles while a few small particles, the high $\chi$ limit, can be accommodated into the interstices. We performed an additional set of simulations varying $0<\chi<0.3$ rather than $b$ to determine the nature of the maximum in $\Phi$ as a function of stoichiometry. Representative packings from these additional simulations are shown in Supplementary Information Fig. S1.

We also show in Supplementary Information Fig. S2 the neighbor subgraphs for large and small particles. These show interesting clustering behavior of the particles in a few cases: for small fractions of large particles (low $\chi$), large particles are well-dispersed in the small particles, forming chains that grow and connect with increasing $\chi$. For low $\chi$ and high $b$, the smaller particles tend to be localized into the space between the large particles, forming crystalline regions. Finally, when large particles cover most of the surface (high $\chi$), the smaller particles again cluster into the interstices, but only a few particles can fit. We note that our simulations do not enforce a particular degree of mixing, and that previous work indicates a continuous tradeoff between $\Phi$ and configurational entropy is possible$^{22}$; how the curvature affects this tradeoff is left to future work.

The packing fractions plotted in Fig. 4B show that for values of bidispersity $b>0.4$ a maximum exists in $\Phi$ for at some value of $\chi$. The maximum $\Phi=0.912$ found is at around $b=0.85$ and $\chi=0.025$, corresponding to about 20/800 particles. This value is somewhat short of the bidispersed disk lattice in 2D Euclidean space which has $\Phi_{2D}=0.9503$. Visually, this particular packing (displayed in the inset of Fig. 4B) resembles a very disordered low $N$ packing with the interstices filled by smaller particles. Large particles are relatively isolated from one another, making on average only 4 contacts with other large particles, and 12 contacts with small particles. We speculate that values of $\Phi$ even closer to $\Phi_{2D}$ may be achieved by careful tuning of $N$, $b$ and $\chi$.

According to the results shown above in 2B-D for $\chi=0.5$, between the percolation and Apollonian points the packings are influenced by the possibility of symmetric commensurate motifs, leading to a rich sequence of 5,12,11 and 8 fold order replacing hexatic order. In contrast, stoichiometry values away from $\chi=0.5$ seem to suppress this sequence as shown in Fig. 4C which displays the most prominent local order parameter $\psi_{n}$ for each

![](./images/813106863666102273_6.jpg)

Fig. 4 Effect of stoichiometry. A Packing fraction as a function of bidispersity for different number fractions of large particles $\chi=N_{L}/N$; B packing fraction as a function of $\chi$ for different $b$. Inset: Configuration with highest packing fraction found $\Phi=0.912$ at $b=0.85$ and $\chi=0.025$. C Most prominent local order parameter parameter $\psi_{6}$ as a function of $b$ and $\chi$. D Fraction of particles $1-\phi_{6}$ with coordination number $C\neq6$ as a function of $b$ for different $\chi$. The dashed horizontal line represents the critical value from the random percolation model at which the hexatic subgraph becomes totally disconnected. E Representative packings colored by coordination number and F non-hexatic subgraphs shown as a function of $b$ and $\chi$.

value of $b$ and $\chi$. Full plots of the order parameter and coordination number for each $\chi$ are shown in Supplementary Information Fig. S3. For $\chi>0.5$, hexagonal and dodecagonal ordering remain for $\chi=0.7$ and $\chi=0.9$ shows only hexagonal ordering. $\chi=0.3$ preserves five and tenfold ordering and interestingly introduces ninefold order at the Apollonian point. At $\chi=0.1$, only hexagonal order remains below the Apollonian point, with fivefold order dominating above it. Noting that the commensurate motifs shown in 2C and D involve an equal number of small and large particles, it would appear that the suppression of these motifs, and introduction of others, simply reflects the relative abundance of different particle types. For example the ninefold order at $\chi=0.3$ and $b \sim 0.7$ emerges due to commensurate arrangements of 3 large and 6 small particles around a central large particle.

We now turn to the effect of stoichiometry on the percolation transition. The non-hexatic fraction $1-\phi_{6}$ is shown as a function of $b$ for the different $\chi$ tested in Fig. 4D. Also shown as a dashed line at $1-\phi_{6}=0.4$ is the value from the random percolation model (see Fig. 3D) above which the hexatic subgraph is disconnected. The line for $\chi=0.9$ flattens out at high $b$ just below the critical value; the line for $\chi=0.1$ reaches it at a much higher value of $b$ than for $\chi=0.5$. It is therefore expected that the non-hexatic subgraphs for $\chi=0.9$ should not display defect percolation while those for $\chi=0.1$ should percolate around $b \sim 0.4$. Examining the packings themselves, shown in Fig. 4E, together with the non-hexatic subgraphs, shown in Fig. 4F, this is correct. The scars in the $\chi=0.9$ packings indeed elongate with increasing $b$, but never form a connected structure. For $\chi=0.1, b=0.3$ is disconnected while $b=0.5$ forms a connected structure. For intermediate values of $\chi$, the non-hexatic component percolates at a similar value of $b$ to the earlier results for $\chi=0.5$. We therefore conclude that the random percolation model successfully predicts the percolation point of the scars as a function of stoichiometry.

Calculating the fractal dimension at percolation, displayed in supplementary information Fig. S4, we find that $\chi=0.3$ and 0.7 have values ($D=1.84$ and $D=1.83$ respectively) just short of the $\chi=0.5$ value of $D=1.85$; $\chi=0.1$, however, yields a slightly lower value of $D=1.8$. These numbers all fall short of the universal value of $D \rightarrow 1.896$ by an amount consistent with previous studies $^{37}$ due to finite system size. For $\chi=0.1$, the large particles are much larger relative to the radius of curvature at percolation, and it remains possible that the discrepancy is due to the surface curvature. A more finely resolved study of the low $\chi$ regime should be conducted to explore this possibility.

## 4 Conclusion
We have shown that the packing fraction of bidispersed packings of spheres on a spherical surface is determined by three influences: an Apollonian packing for $b \approx 0.73$ where small particles fit into the interstices of large particles produces a global maximum; commensurate configurations of particles yield an inflexion point at $b \approx 0.41$; a minimum at $b \approx 0.1$ is due to the growth and percolation of scars previously observed in the monodispersed case. At this point, the non-hexatic subgraph contains a cluster that percolates throughout the whole structure. Chains of defects or scars are an important feature of crystals on curved surfaces, and our work therefore provides a new control parameter, bidispersity, to vary their length. This might be desirable experimentally, in a col-loidosome for instance, because the scars control the mechanical response and failure point of the system $^{39}$.

By adjusting the ratio of large particles to small particles $\chi$, we have shown that the percolation transition can be shifted in bidispersity and even suppressed entirely for large $\chi$. The growing lengthscale and critical fraction for percolation were found to be in excellent agreement with those for random percolation on the monodispersed neighbor graph, and the fractal dimension of the clusters was also found to be in good agreement with the universal value for 2D percolation accounting for the finite system size.

Around the Apollonian point, varying $\chi$ and $b$ simultaneously permits further enhancement of $\Phi$. The point $b=0.85$ and $\chi=0.025$ had the highest fraction found, $\Phi=0.912$, but we speculate values closer to the 2D bidispersed disk lattice $\Phi_{2 D}=0.9503$ might be found with further tuning. Because we did not enforce a degree of mixing as has been shown to be important in flat space $^{22}$, it is conceivable that for the values of $b$ and $\chi$ investigated, a configuration of higher $\Phi$ might be found. The interplay of curvature, packing fraction and configurational entropy is therefore an important question for future work.

## Methods
Packings with high coverage fraction were produced using a surface relaxation algorithm: $N$ spherical particles are initially placed using random sequential absorption with their centers of mass on a sphere of radius $R=1$. Particles are randomly assigned to two categories corresponding to larger and smaller radii respectively. The simulation proceeds by, first, *diffusion sweeps* where, particles are moved in random order some distance drawn from a Gaussian distribution of width $\sigma=2 r_{1} \times 10^{-3}$ in a random direction along the surface. Moves that cause overlap are rejected. As the packing becomes dense, an adaptive step size is used to reduce the number of moves rejected due to overlap: $\sigma=10\langle s\rangle$, where $\langle s\rangle$ is the geometric mean of the separation between each particle and its three nearest neighbors. Secondly, *surface relaxation* moves slowly decrease the radius of the surface by an amount $\Delta R$, where initially $\Delta R=10^{-5}$. After the surface radius is reduced, particles are projected down onto the nearest point on the surface. After projection, a gradient descent minimization is run on the particles (where the interparticle energy is linear the amount of overlap) until overlap is undone. If overlap can not be undone, the surface relaxation move is undone and particle positions are reset, and simulation continues with $\Delta R$ set to $\Delta R / 2$. 20 diffusion sweeps are carried out between each surface relaxation step. The simulation halts when $\Delta R$ is reduced to $2^{-14}$ times its original value.

## Acknowledgements
The authors are grateful to the Research Corporation for Science Advancement for funding through a Cottrell Award, and Tufts University for an International Travel Grant during which part of this work was completed. TJA is also supported by a CAREER award from the National Science Foundation (award number DMR-1654283).

AMM is grateful to Tufts University for the Steven and Joyce Eliopou- los Summer Scholarship.

## References
1 F. H. Stillinger and P. G. Debenedetti, *Annu. Rev. Condens. Matter Phys.*, 2013, **4**, 263-285.

2 A. Donev, *Journal of Applied Physics*, 2004, **95**, 989-999.

3 M. Cates, J. Wittmer, J.-P. Bouchaud and P. Claudin, *Physical review letters*, 1998, **81**, 1841.

4 A. J. Liu and S. R. Nagel, *Annual Review of Condensed Matter Physics*, 2010, **1**, 347-369.

5 C. O'Hern, S. Langer, A. Liu and S. Nagel, *Physical Review Letters*, 2002, **88**, 075507.

6 C. Reichhardt and C. O. Reichhardt, *Soft matter*, 2014, **10**, 2932-2944.

7 S. Alexander, *Physics Reports*, 1998, **296**, 65-236.

8 A. Donev, S. Torquato, F. H. Stillinger and R. Connelly, *Journal of Computational Physics*, 2004, **197**, 139-166.

9 S. Torquato and F. H. Stillinger, *Journal of Physical Chemistry*, 2001, **105**, 11849-11853.

10 S. Torquato and F. H. Stillinger, *Reviews of Modern Physics*, 2010, **82**, 2633-2672.

11 B. Lubachevsky, F. Stillinger and E. Pinson, *Journal of Statistical Physics*, 1991, **64**, 501-524.

12 S. Torquato, T. M. Truskett and P. G. Debenedetti, *Physical review letters*, 2000, **84**, 2064.

13 A. Donev, S. Torquato, F. H. Stillinger and R. Connelly, *Phys. Rev. E*, 2004, **70**, 043301.

14 R. D. Kamien and A. J. Liu, *Physical review letters*, 2007, **99**, 155501.

15 T. Hamanaka and A. Onuki, *Physical Review E - Statistical, Nonlinear, and Soft Matter Physics*, 2006, **74**, 1-7.

16 W. Vermöhlen and N. Ito, *Phys. Rev. E*, 1995, **51**, 4325-4334.

17 H. Watanabe, S. Yukawa and N. Ito, *Physical Review E - Statistical, Nonlinear, and Soft Matter Physics*, 2005, **71**, 1-4.

18 M. R. Sadr-Lahijany, P. Ray and H. E. Stanley, *Phys. Rev. Lett.*, 1997, **79**, 3206-3209.

19 S. Hilgenfeldt, *Philosophical Magazine*, 2013, **93**, 4018-4029.

20 P. Richard, L. Oger, J. P. Troadec and a. Gervois, *European Physical Journal E*, 2001, **6**, 295-303.

21 D. R. Nelson and B. I. Halperin, *Phys. Rev. B*, 1979, **19**, 2457-2484.

22 A. Donev, F. H. Stillinger and S. Torquato, *Physical review letters*, 2006, **96**, 225502.

23 H. Seung and D. Nelson, *Physical Review A*, 1988, **38**, 1005-1018.

24 A. Bausch, M. Bowick, A. Cacciuto, A. Dinsmore, M. Hsu, D. Nelson, M. Nikolaides, A. Travesset and D. Weitz, *Science (New York, N.Y.)*, 2003, **299**, 1716-1718.

25 M. Bowick, D. Nelson and A. Travesset, *Physical Review B*, 2000, **62**, 8738-8751.

26 C. J. Burke, B. L. Mbanga, Z. Wei, P. Spicer and T. Atherton, *Soft Matter*, 2015, 5872-5882.

27 H. Cohn, Y. Jiao, A. Kumar and S. Torquato, *Geometry & Topology*, 2011, **15**, 2235-2273.

28 C. J. Burke and T. J. Atherton, submitted, 2016, arXiv:1605.09478.

29 F. Aurenhammer, *ACM Computing Surveys (CSUR)*, 1991, **23**, 345-405.

30 D. Shechtman, I. Blech, D. Gratias and J. W. Cahn, *Phys. Rev. Lett.*, 1984, **53**, 1951-1953.

31 S. Fischer, A. Exner, K. Zielske, J. Perlich, S. Deloudi, W. Steurer, P. Lindner and S. Förster, *Proceedings of the National Academy of Sciences*, 2011, **108**, 1810-1814.

32 D. V. Talapin, E. V. Shevchenko, M. I. Bodnarchuk, X. Ye, J. Chen and C. B. Murray, *Nature*, 2009, **461**, 964-967.

33 D. Nelson, *Defects and Geometry in Condensed Matter Physics*, Cambridge University Press, 2002.

34 A. Donev, S. Torquato and F. Stillinger, *Physical Review E*, 2005, **71**, 011105.

35 D. Stauffer and A. Aharony, *Introduction To Percolation Theory*, Taylor & Francis, 1994.

36 G. Grimmett, *Lectures on Probability Theory and Statistics*, Springer, 1997, pp. 153-300.

37 D. He, N. Ekere and L. Cai, *Physical Review E*, 2002, **65**, 061304.

38 Y. Han, J. Lee, S. Q. Choi, M. C. Choi and M. W. Kim, *EPL (Europhysics Letters)*, 2015, **109**, 66002.

39 C. Negri, A. L. Sellerio, S. Zapperi and M. C. Miguel, *Proceedings of the National Academy of Sciences*, 2015, **112**, 14545-14550.