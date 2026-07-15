# Electrostatic Theory of Metal Whiskers
V. G. Karpov*

Department of Physics and Astronomy, University of Toledo, Toledo, Ohio 43606, USA
(Received 29 January 2014; revised manuscript received 25 March 2014; published 15 May 2014)

Metal whiskers often grow across leads of electric equipment and electronic package causing current leakage or short circuits and raising significant reliability issues. The nature of metal whiskers remains a mystery after several decades of research. Here, the existence of metal whiskers is attributed to the energy gain due to electrostatic polarization of metal filaments in the electric field. The field is induced by surface imperfections: contaminations, oxide states, grain boundaries, etc. A proposed theory provides closed form expressions and quantitative estimates for the whisker nucleation and growth rates, explains the range of whisker parameters and effects of external biasing, and predicts statistical distribution of their lengths.

DOI: 10.1103/PhysRevApplied.1.044001

## I. INTRODUCTION
Metal whiskers are hairlike protrusions observed at surfaces of some metals; tin and zinc examples are illustrated in Fig. 1 [1–6]. In spite of being omnipresent and leading to multiple failure modes in electronic industry, the mechanism behind metal whiskers remains unknown after more than 60 years of research. While some con- sensus, at a qualitative level, is that whiskers represent a stress relief phenomenon, that never led to any quantitative description including order-of-magnitude estimates of whisker parameters. A theory of metal whiskers presented here is consistent with many published observations and provides quantitative analytical results.

As a brief survey of relevant data [1–10], it should be noted that whiskers grow up to approximately 1–10 mm in length and vary from approximately 1 nm to approximately 30 $\mu$m in diameter. Their parameters are characterized by broad statistical distributions: side by side with fast grow- ing whiskers there can be others, on the same surface, whose growth is much slower or completely stalled. The metal surface conditions play a significant role. In particu- lar, oxide structure and various contaminations are impor- tant factors determining whisker concentration, growth rate, and dimensions. The metal grain size appears to be less significant for small grains (nanometers to a few microns), while whiskers are unlikely for very large grains; recrystallization can be of importance [11]. Various addi- tives can have significant effects on whisker growth such as, e.g., a small concentration of Pb strongly suppressing tin whiskering. Electric bias is reported to exponentially increase whisker growth rate [8,12,13], which is attributed to the effects of electric current, although other publications reported no bias effect on whisker growth [14] and even the negative effect of bias suppressed whiskering [15]. A common observation is that whiskers grow from the root rather than from the tip, and the material required for their growth is supplied from large distances through long range surface diffusion rather than from a narrow neighboring proximity; there is no surrounding dent formed in the course of whisker growth. A comprehensive review of experimental data on the most studied tin whiskers before the year 2003 was given in a monograph [16]; Refs. [17–20] provide a more recent summary.

Multiple attempts to understand the mechanisms of whisker growth (see, e.g., Refs. [21–24]) revolved around the role of surface stresses relived by whisker production, dislocation effects, and oxygen reactions. It is shown [19,25] that stress gradients along with certain assumption about system parameters can explain tin whisker growth rates but not their existence, shapes, and statistics. Overall, these attempts have not lead to verifiable quantitative predictions.

The mechanism proposed here is qualitatively different as it is driven by the existence of a strong enough electric field $E$ above the metal surface. The field is generally due to surface imperfections, such as oxide, ion contaminations, local stresses, and interfacial states. The appearance of whiskers is described as the electric field induced nucle- ation. It is triggered by the energy gain $F_E = -\mathbf{p} \cdot \mathbf{E}$ due to the induced whisker dipole $\mathbf{p} = \alpha \mathbf{E}$ in the electric field $E$,

![](./images/814753776488415233_1.jpg)

FIG. 1. Scanning electron microscope (SEM) pictures of tin (left) and zinc (right) whiskers. Courtesy of the NASA Electronic Parts and Packaging (NEPP) Program [6].

*victor.karpov@utoledo.edu

where $\alpha$ is the polarizability. The latter dipole is anomalously strong for the needle shaped metallic particles that serve as the whiskers' nuclei.

This paper is organized as follows. It starts with a purely qualitative discussion in Sec. II that explains without any math the model and the logic of the paper. Section III describes the field induced nucleation of whiskers estimating their initial dimensions and nucleation rates. Random electric fields responsible for whisker nucleation are described in Sec. IV. They turn out to be different at small, intermediate, and large distances. The kinetic of whisker growth is analyzed in Sec. V. Sections VI and VII discuss, respectively, the phenomenon of long-range surface diffusion related to whisker growth and statistical distributions of whisker lengths. Numerical estimates in Sec. VIII prove that the proposed theory is in at least semiquantitative agreement with the data. The conclusions in Sec. IX list this theory's successes and problems.

## II. QUALITATIVE DESCRIPTION

This section presents a simplified "low resolution" guide through subsequent consideration, some parts of which present inevitable distracting details. It provides a brief summary of this paper's approach and results.

(1) The model is based on the concept of strong electric fields, $E \lesssim 1$ MV/cm, in the submicron proximity of metal surfaces. As explained below, such fields can be generated by various surface imperfections including some grain orientations, oxides, dislocations, or chemical contamination. The phenomenon of whisker nucleation and growth is attributed to the electrostatic energy gain due to strong polarization of needle shaped metal particles.

(2) Being overall neutral these metal surfaces are composed of oppositely charged patches formed as a result of electron redistribution minimizing the system free energy. The patches are characterized by certain surface charge density and dimensions $L \sim 1$-$10\ \mu$m.

(3) The conception of whiskers is described based on the earlier developed theory of field induced nucleation that predicts needle shaped embryos $h \lesssim$ 100 nm in length and $d \sim 1$ nm in diameter.

(4) Following the nucleation is the growth stage where whiskers increase their length by accretion of material at their bases. The growth kinetics described in this paper are different for whisker lengths below and above the characteristic charge patch dimension $L$. In particular, growth rates turn out to be extremely low for short ($h < L$) whiskers. However, they abruptly increase when whiskers overgrow the patch dimension $L$, after which the growth rate remains on average constant.

(5) In the course of growing at $h \gg L$, whiskers encounter rare local regions of abnormally low electric fields where its further growth is blocked. The statistics of these regions determines the whisker length statistics. It is derived to be close to log-normal.

(6) Overall, the conclusions below are at least semiquantitatively consistent with the available data. Some features remain to be understood, and some experimental verification suggested.

## III. FIELD INDUCED NUCLEATION

The electrostatic energy gain in the electric field can be represented as [26-28]
$$
F_E = -\varepsilon\alpha E^2, \tag{1}
$$
where $\varepsilon$ is the dielectric permittivity of the surrounding medium. This energy gain is independent of the sign of the electric field, outwards or towards the surface, as illustrated in Fig. 2. In this section, we consider field induced nucleation in a uniform field. Complications due to the field nonuniformity will be discussed in Sec. IV.

The polarizability $\alpha$ is a maximum in the longitudinal direction illustrated in Fig. 2; it is by approximately the factor of $(h/d)^2 \gg 1$ greater than the particle volume $\pi(d/2)^2h$ that serves as a standard measure of polarizability in electrostatics. The mechanism of that enhancement can be understood as follows. Under electric field $E$, a metallic needle will accumulate at its ends opposite charges of absolute values $q \sim Eh^2$, just sufficient to cancel out the field inside the needle. They correspond to the dipole moment $p \sim qH \sim Eh^3 \sim EV(h/d)^2$, where $V \sim hd^2$ is the particle volume.

A more accurate result for needle polarizability (Ref. [29], p. 17) is given by
$$
\alpha \approx \frac{h^3}{3\Lambda}, \quad \text{with } \Lambda \equiv \ln(4h/d)-7/3. \tag{2}
$$

Strictly speaking, Eq. (2) is valid for the case of extremely anisotropic particles with $\Lambda \gg 1$; in what follows, it serves as a simple approximation for even moderately anisotropic structures with $\Lambda \gtrsim 1$. Note that the concept of energy gain in Eqs. (1) and (2) has been successfully used to describe the field induced nucleation of metal particles [30-38].

![](./images/814753776488415233_2.jpg)

FIG. 2. Sketch of two whiskers of length $h$ and diameter $d$ on a metal surface with local electric fields $\mathbf{E}$ (of opposite directions) inducing the dipole moments $\mathbf{p}$.

Side by side with the electrostatic energy gain, there is energy loss due to an increase in the surface area, $F_S = \pi d h \sigma$, where $\sigma$ is the surface tension. The total change in free energy due to whisker formation is given by

$$
F(h)=-\frac{h^{3}}{3 \Lambda} \varepsilon E^{2}+\pi d h \sigma. \tag{3}
$$

It is a maximum,

$$
\max F(h)=W(E) \equiv \frac{2}{3} \pi \sigma d \sqrt{\frac{\pi \sigma \Lambda d}{\varepsilon E^{2}}}, \tag{4}
$$

when

$$
h=h_{0}(E) \equiv \sqrt{\frac{\pi \sigma \Lambda d}{\varepsilon E^{2}}}. \tag{5}
$$

Here we treat a logarithmically weak dependence $\Lambda(h)$ as a constant.

The barrier $W$ and its corresponding length $h_0$ shown in Fig. 3 have the same meaning as the nucleation barrier and radius in the classical nucleation theory [26]. In particular, a whisker becomes stable and keeps growing when its length exceeds $h_0$, so it overcomes the barrier.

Along the lines of standard nucleation theory, the characteristic nucleation time is given by

$$
\tau=\tau_{0} \exp \left(\frac{W}{k T}\right). \tag{6}
$$

Here, the preexponential $\tau_0$ remains rather poorly determined in the framework of the existing classical nucleation theory, possibly leading to many orders of magnitude deviations from the data [39–42]. Its often used values range in the interval $\tau_{0} \sim 10^{-13}-10^{-8}$ s.

As seen from Eq. (4), the nucleation barrier $W$ is field dependent. Since the field is a random variable, the nucleation times are distributed in the exponentially broad interval. One other immediate prediction is that external fields (added to the existing random fields) can exponentially accelerate whisker nucleation.

In Eqs. (3)–(5), we tacitly assume a certain diameter $d$ of the needle shaped nucleus. Both the nucleation barrier and length decrease as $d$ decreases; hence, the smallest possible $d$ are the most favorable. Realistically, $d$ must be greater than some minimum value $d_0$ determined by extraneous requirements, such as sufficient conductivity to support a large dipole energy or sufficient mechanical integrity. Based on data for other types of systems undergoing field induced nucleation, it is estimated that a reasonable minimum diameter is in the subnanometer range [30–38]. Lacking more concrete information, we assume here $d_0 \lesssim 1$ nm. In the region $d > d_{\text{min}}$, the free energy is substantially larger than described by Eq. (3), since the energy reducing effect of the electric field cannot be manifested by such thin particles. The region $d = d_0$ can be approximated by a potential wall. Following substantiation in the previous work [30–38], we consider nucleation along the path $d = d_0$; alternative paths that start from the origin introduce only insignificant numerical factors. Correspondingly, we use $d \lesssim 1$ nm in Eqs. (3)–(5) above as a rough approximation.

![](./images/814753776488415233_3.jpg)

FIG. 3. Free energy of a whisker vs its length.

Using the latter approximation, Eqs. (4) and (5) enable one to estimate the nucleation barrier and length. The energy $\sigma$ in these equations depends on which type of surface is essential. Considering, for example, tin whiskers, the macroscopically averaged value [43,44] is $\sigma \sim 500$ dyn/cm, while the grain boundary related values can be as low as $\sigma \sim 100$ dyn/cm, Ref. [45], and even $\sigma = 30$ dyn/cm, Ref. [46]. Along with approximations $\Lambda \sim \varepsilon \sim 1$, and $E = 1$ MV/cm, these values yield $W \sim$ 1–10 eV and $h_0 \sim 10$ nm. Such $W$ are in the ballpark of nucleation barriers known for various processes [26]. Also, the underlying assumption of $h/d \gg 1$ is justified by the latter result for $h_0$. Therefore, the field induced nucleation appears a conceivable mechanism of metal whisker conception.

In the existing literature [21,47], the terminology of whisker nucleation is used as a qualitative statement discriminating between the stages of whisker conception and subsequent evolution. The approach in Eqs. (3)–(5) provides a quantitative basis for the concept of nucleation. It is triggered by the energy gain of metal whisker due to their polarization in the surface electric field.

## IV. THE ELECTRIC FIELD DISTRIBUTION
### A. Surface electric field: Charged patches

Significant electric fields above metal surface can arise from spatial variations of the work function [48] depending on multiple imperfections in structure and composition. At first glance, the existence of such fields may appear contradictory. Indeed, free electrons in metals have a tendency to screen electric charge fluctuations, thereby suppressing electric fields. However, as explained next, the role of free electrons is exact opposite: their ability to move underlies the electric charge variations.

To avoid any misunderstanding, it should be emphasized that it is not the condition of local electroneutrality, but rather that of minimum free energy that determines the

044001-3

electric charge (and other parameters) distributions. The electrons will always move to minimize the system free energy; this movement leads to nonuniform charge distributions in nonhomogeneous systems. In other words, not only are the existence of surface electric fields and their corresponding electric charge variations fully consistent with the concept of free electrons, but it is due to free electrons that different local regions of a metal can exchange electric charges minimizing the system free energy.

It follows from the latter consideration that some structural or compositional inhomogeneities are needed for the electric charge redistribution triggering whisker growth. Grain structure can be one (but not the only) example of such inhomogeneities. This example is consistent with the general observation that whiskers are unlikely on metal surfaces built of very large grains, and that the presence of grain boundaries can be essential [11]. Before pointing at more specific factors behind electric field variations, the following general examples (i)–(iii) are aimed at illustrating the underlying physics.

(i) Consider local stresses (due to grain boundaries, dislocations, or external loads) modulating interatomic distances in a metal, thus making some local regions denser than the others. Because of these local variations, some regions will present deeper potential wells for the electrons (a phenomenon known as the deformation potential). Should these regions be mutually independent, the Fermi level positions would vary between them. However, because they are connected, the free electrons will move to level out the Fermi level across the entire system, thus minimizing the system free energy. As a result, the above regions become electrically charged.

(ii) Spatial variations in chemical composition of alloys would similarly result in modulations of work function, which will be leveled out in the course of electron redistribution creating local electric fields similar to the previous example.

(iii) The extreme case of the latter modulation is presented by a contact of different metals with unequal work functions. The free electrons will move between these metals to equalize their Fermi levels. This redistribution makes the metals electrically charged. The same phenomenon underlies the existence of Schottky barriers and $p$-$n$ junctions in semiconductors. In the case of metal couples, it is known as the source of the galvanic action that occurs when two electrochemically dissimilar metals are in contact and a conductive path occurs for electrons and ions to move from one metal to the other. Furthermore, one can imagine a binary mixture of chemically different metal grains where the balance of Fermi energy makes the grains of two types charged oppositely.

More specifically, the regions of different surface potential (patches) may be due to the polycrystallinity of a metal: the work function will vary between regions of specific grain orientations by typically a few tenths of a volt; these different grain orientations will be qualitatively similar to the above example (iii) of binary metal mixtures. Patch structure may also arise from the presence of adsorbed elements and compounds; that contamination is qualitatively similar to the above mentioned example (ii) of the chemical composition variations. Certain features of surface morphology, particularly, its roughness, may result in the electron redistribution caused by the corresponding modulations of microscopic structure parameters similar to the above example (i). They can be caused by dislocations [49], stress induced spots of different structure phases [50], or general electric deformation coupling [51] in combination with stress induced buckling [52,53]. Local charges due to stress induced oxide cracking or ion trapping under the whisker growing layer (say, Sn on Cu substrate) are conceivable sources of the above considered surface electric fields as well. Therefore, a surface that is ideally electrically uniform may acquire electric surface structure.

Here, we assume a simple model of uncorrelated charge patches on a metal surface characterized by two parameters: characteristic electron surface charge density $ne$ (electrons per cm$^2$), and the linear dimension $L$. In reality, the charge distribution in patches can be nonuniform, possibly concentrating along grain boundaries or other structural imperfections. However, these conceivable complications fall beyond the present scope.

Patch structured electric fields near metal surfaces have been found in multiple work (see, e.g., Refs. [48,54–57], and references therein). The measurements reveal the work function fluctuations of approximately 0.5 eV induced by $L \sim 10$ $\mu$m patches in some metals [48]. These figures are consistent with a rather general knowledge that the charged surface state concentration of $n \gtrsim 10^{12}$ cm$^{-2}$ is not unusual for many materials [58]. The corresponding field strength is given by

$$
E = E_0 \equiv 4\pi en/\varepsilon \gtrsim 10^6 \ \text{V/cm}, \tag{7}
$$

where $e$ is the electron charge. This field can be directed either up or downwards in Fig. 2 extending over the characteristic distance $L$ above the surface. The above simple expression fails in the regions of both short and large distances as explained next.

### B. High charge densities and short nuclei

The applicability of Eq. (7) is limited by the condition of continuous charge distribution $n\pi r^2 \gg 1$, where $r$ is the distance above the surface. As applied to the nucleation theory in Sec. III, this limitation implies a large enough


![](./images/814753776488415233_4.jpg)

FIG. 4. The perpendicular electric field component $\mathbf{E}$ at small distance $r$ from the metal surface. Gray circles represent point surface charges with the average intercharge distance $n^{-1/2} > r$

nucleus height, $nh_0^2 \gg 1$, since $h_0$ is derived under the assumption of uniform field $E = E_0$ created by a continuous surface charge distribution. With Eq. (5) in mind, this inequality leads to the condition

$$
n < n_c \equiv \frac{\sigma\Lambda\varepsilon d}{16e^2}. \tag{8}
$$

If the surface charge density $n$ exceeds $n_c$, then the embryo height predicted by Eq. (5) turns out to be shorter than the intercharge distance $n^{-1/2}$, and the approximation of uniform field fails.

In the opposite limiting case, $n \gg n_c$, the perpendicular field component (Fig. 4) can be approximated by the sum of contributions from the nearest point charge $e$ and all other charges described in continuous approximation by the density $ne$,

$$
E \approx \frac{e}{\varepsilon r^2} + \int_{n^{-1/2}}^\infty \frac{2\pi nerxdx}{(x^2 + r^2)^{3/2}} = \frac{e}{\varepsilon r^2} + E_0 r\sqrt{n}, \tag{9}
$$

where $E_0$ is given by Eq. (7). For the purely Coulomb contribution, the field induced polarization charge in a metal embryo would be confined to short distances; hence, the embryo height does not contribute to the electrostatic energy gain. (This conclusion can be more rigorously proven by modification of the known treatment of the uniform field polarization in Ref. [29] described in Appendix A.)

The second term in Eq. (9) creates the energy gain similar to that in Eq. (3). The difference is that now the acting field is linear in height $h$ due to its proportionality to $r$ in Eq. (9). Therefore, the electric field $E$ in Eq. (3) should be replaced with $E_0 hn^{-1/2}/2$ (averaged over the embryo length), which makes the electrostatic energy gain proportional to $h^5$. As a result, the nucleation barrier for short embryos in systems with $n > n_c$ can be presented in the form

$$
W = W(E_0)\left(\frac{n}{n_c}\right)^{1/4}, \quad \text{when } n > n_c, \tag{10}
$$

where $W(E_0)$ is defined in Eq. (4) with $E = E_0$.

Note that Eq. (10) predicts $W \propto n^{-3/4}$, since $W(E_0) \propto E_0 \propto n$. Equation (4) describes how the nucleation barrier decreases with surface charge density slightly slower than predicted by the baseline model of the uniform field in Eq. (4). Because $(n/n_c)^{1/4}$ is a relatively weak dependence derived in otherwise rather approximate theory, for the sake of simplicity, we will set the latter factor to unity, thus using, in what follows, Eq. (4) in the entire range of surface charge densities.

### C. Large distances and random fluctuations

As illustrated in Fig. 5, at distances $r \gg L$, the contributions of oppositely charged patches mostly cancel each other, and the field is due to a random excess number $\Delta N$ of the patches of a certain sign close enough to the point of observation. Taking the latter point at height $r$ above the surface, the charged patches in a domain of radius $r$ beneath will generate more or less perpendicular random field. Therefore, $\Delta N \sim \sqrt{N} \sim r/L$, where $N \sim r^2/L^2$ is the average number of patches in the domain of radius $r$. Hence, one can estimate the absolute value of the field as

$$
E \sim \frac{\Delta N ne L^2}{r^2} \sim E_0 \frac{L}{r}. \tag{11}
$$

The corresponding contribution to free energy is then given by [cf. Eqs. (1) and (2)]

$$
F_E = -\frac{\varepsilon E_0^2 h L^2}{3\Lambda}, \quad \text{when } h \gg L. \tag{12}
$$

The angular distribution of field $\mathbf{E}$ at these distances becomes quite random. The maximum angle of $90^\circ$ between $\mathbf{E}$ and the surface normal corresponds to the case when the positive and negative random charges are as far away from each other as possible (i.e., on the opposite halves of the circle in Fig. 5); hence, the angular distribution ranging from $0^\circ$ to $90^\circ$ with a maximum somewhere in between.

The field will vary not only in the lateral directions, but with the distance to the surface above any given spot as well. This variation happens because the contributing

![](./images/814753776488415233_5.jpg)

FIG. 5. Sketch of the patched area domain of radius $r$ where + and – represent positively and negatively charged patches (shown in dash) of characteristic linear dimension $L$ each. The thick arrow represents the random field vector at distance $r$ along the domain axis.

random charge configurations change with that distance.
Based on the interpretation in Fig. 5, the field $E$ will change considerably over distances of the order of $r$. In particular, the characteristic length of fluctuations increases linearly with $r$. It should be understood, however, that the angular distribution of fields can be significantly different from the observed angular distribution of whiskers. The latter dis- tribution is determined by the kinetic of growth of crystalline structures in random fields, which nontrivial problem is beyond the present scope.

Far enough from the surface, the field in Eq. (11) becomes very low giving up to the background (thermal) electric field. Its time average is given by

$$
\left\langle E_{T}^{2}\right\rangle=4 \pi \sigma_{\mathrm{SB}} T^{4} / c \sim 20 \mathrm{~V}^{2} \mathrm{~cm}^{-2}.\qquad(13)
$$

Here $\sigma_{\mathrm{SB}}$ is the Stefan-Boltzmann constant, $c$ is the speed of light, and we chose the temperature $T \sim 300 \mathrm{~K}$. Comparing the results in Eqs. (11) and (13) yields the overplay distance

$$
r_{c} \sim L \frac{E_{0}}{E_{T}}.\qquad(14)
$$

For the above used numerical values, $r_{c} \sim 10 \mathrm{~cm}$ is far beyond the whiskers length domain. However, it falls into that domain, shrinking to, e.g., $r_{c} \sim 0.1 \mathrm{~mm}$, for the case of high enough temperatures, low surface charge densities, or small patches, say, $L \sim 100 \mathrm{~nm}$. Since thermal radiation is polarized parallel to the surface [59], it is expected that whiskers in that region will evolve mostly parallel to the surface as well.

## V. WHISKER GROWTH

### A. General formalism

Whisker growth occurs through the process of many elemental acts of accretion. Such multistep processes are described by the Fokker-Planck approach (see, e.g., Ref. [60], pp. 89, 90, and 428) with statistical distribution $f(h, d)$, such that $f(h, d) d h d d$ is the number of whiskers with height and diameter in the intervals $(h, h+d h)$ and $(d, d+d d)$, respectively. The Fokker-Planck equation takes the form

$$
\frac{\partial f}{\partial t}=-\frac{\partial s_{h}}{\partial h}-\frac{\partial s_{d}}{\partial d}.\qquad(15)
$$

Here, $s_{h}$ and $s_{d}$ are the components of the flux in the whisker dimensions space $(\mathrm{s}^{-1} \mathrm{~cm}^{-3})$,

$$
s_{h}=-A_{h} f-B_{h d} \frac{\partial f}{\partial d}-B_{h h} \frac{\partial f}{\partial h},\qquad(16)
$$

$$
s_{d}=-A_{d} f-B_{d h} \frac{\partial f}{\partial h}-B_{d d} \frac{\partial f}{\partial d}.\qquad(17)
$$

The kinetic coefficients are defined as follows:
$$
\begin{aligned}
A_{h} & =\tilde{A}_{h}+\frac{\partial B_{h d}}{\partial d}, & A_{d} & =\tilde{A}_{d}+\frac{\partial B_{d h}}{\partial h}, \\
\tilde{A}_{h} & =\sum_{i} \delta h_{i} / t, & \tilde{A}_{d} & =\sum_{i} \delta d_{i} / t, \\
B_{h h} & =\sum_{i j} \delta h_{i} \delta h_{j} / \delta t, & B_{d d} & =\sum_{i j} \delta d_{i} \delta d_{j} / \delta t, \\
B_{h d} & =B_{d h}=\sum_{i j} \delta h_{i} \delta d j / \delta t, & & (18)
\end{aligned}
$$

where $\delta h_{i}$ and $\delta d_{i}$ are random changes in $h$ and $d$ at a step $i$ in the course of whisker growth over time $\delta t$.

Two boundary conditions to Eq. (15) are $f(r=0)=0$ and $f(r=\infty)=0$. They reflect the facts that very thin filaments cannot exist due to certain extraneous limitations such as loss of conductivity or mechanical instability, and that only finite radii are achievable over finite times $t$.

The approximation of independent height and diameter evolution below, means $B_{h d}=B_{d h}=0$. To further simplify the analysis, the two remaining coefficient are set equal, $B_{h h}=B_{d d} \equiv B$. Relaxing these limitations leads to more cumbersome results without new qualitative features.

The $A$ coefficients are connected with $B$ by a relationship which follows from the fact that $s_{h}=s_{d}=0$ for the equilibrium distribution $f_{0}(h, d) \propto \exp [-F(h, d) / k T]$, where $F$ is the free energy. This requirement yields

$$
s_{h}=-B f_{0} \frac{\partial}{\partial h}\left(\frac{f}{f_{0}}\right), \quad s_{d}=-B f_{0} \frac{\partial}{\partial d}\left(\frac{f}{f_{0}}\right). \quad(19)
$$

Using Eq. (19) for $s$, multiplying Eq. (15) by $h$, integrating from 0 to $\infty$ by parts, and noting that $\int f h d h=\langle h\rangle$, yields $\partial\langle h\rangle / \partial t=\langle\partial F / \partial h\rangle$ (angle brackets denote averages). Neglecting fluctuations in the ensemble of nominally identical filaments enables one to approximate $\langle F\rangle=F(\langle h\rangle)$ and $\langle\partial F / \partial h\rangle=\partial\langle F\rangle / \partial\langle h\rangle$. Similar transformations apply to the $d$ dependence. Omitting for brevity the angular brackets, one finally obtains

$$
\frac{\partial h}{\partial t}=-b \frac{\partial F}{\partial h}, \quad \frac{\partial d}{\partial t}=-b \frac{\partial F}{\partial d}, \quad \text { with } b=\frac{B}{k T}. \quad(20)
$$

These equations have the standard meaning of the relations between the (growth) velocities and the (thermodynamic) forces $-\partial F / \partial h,-\partial F / \partial d$, with the Einstein relation between the mobility $b$ and diffusion $B$.

$B$ can be estimated as $\nu a^{2} \exp (-F_{B} / k T)$, where $\nu$ is the characteristic atomic frequency (approximately $10^{13} \mathrm{~s}^{-1}$ ), $a$ is the characteristic interatomic distance, $F_{B}$ is the kinetic phase transformation barrier, $k$ is Boltzmann's constant, and $T$ is the temperature. Assuming $B$ of the order of the diffusion coefficient $D$ of species dominating whisker growth, it can be estimated based on the available data; otherwise $B$ remains a parameter of this theory.

044001-6

The averaged description in Eqs. (20) can apply as long as it is not affected by rare events terminating or exponentially slowing whisker growth. These events take place when whisker tips reach random local regions of abnormally low fields. They present barriers to whisker growth, since the electrostatic energy gain there is suppressed, while surface related energy loss remains. The statistics of these rear events and its corresponding distribution of whisker lengths are described in Sec. VII below.

### B. Limiting cases
Integrating Eq. (20) with $F=-F_E$ (i.e., neglecting surface energy far enough from the nucleation barrier) and $F_E$ from Eqs. (1) and (12), and treating $\Lambda$ as a constant, yields
$$
\begin{aligned}
h & \approx \frac{h_0}{1-t / t_0}, & d & \approx \sqrt{d_0^2+\left(h^2-h_0^2\right) / \Lambda}, \\
t_0 & \equiv \frac{3 \Lambda}{b \varepsilon E_0^2 h_0}, & & \text { when } h \ll L,
\end{aligned}
\tag{21}
$$
and
$$
\begin{aligned}
h & =L \frac{t}{t_L}, & d & \approx L / \sqrt{\Lambda}, \\
t_L & \equiv \frac{3 \Lambda}{b \varepsilon E_0^2 L}, & & \text { when } r_c \gg h \gg L.
\end{aligned}
\tag{22}
$$

We recall that underlying these results is the approximation $\Lambda \gg 1$. Finally, in the region of yet larger lengths, $h \gg r_c$, the whiskers will grow uniformly, as predicted by Eq. (22) where $E_0^2$ is replaced with $\left\langle E_r^2\right\rangle$.

The result in Eq. (22) changes numerically when more accurate expressions (A6) and (B3) from Appendixes A and B are used for the free energy $F_E$. The growth rate from Eq. (22) acquires then an additional coefficient to become
$$
\frac{d h}{d t} \approx \frac{L}{t_L} \ln \left(\frac{4 t}{t_L}\right), \quad \text { with } \quad t_L \equiv \frac{32 \pi(\Lambda+4 / 3)}{b \varepsilon E_0^2 L}. \tag{23}
$$

Figure 6 presents the predicted temporal dependence of whisker growth rate where the limiting results must be sewed at $h \sim L$, i.e., $t \sim t_0$. In that poorly described region, the two predicted limiting case rates match in the order of magnitude. Indeed, setting $h \sim L$ in Eq. (21) yields $1-t / t_0 \sim h / L$, which results in the same $d h / d t$ as provided by Eq. (22).

However, the details of the latter sewing remain unknown. Assuming a hump in the sewing region would make Fig. 6 resembling the real time data from Ref. [61]. Even without that hump, Fig. 6 reproduces the observation of many authors that whisker growth starts abruptly from some time instance ($t_0$ in this work notations) to continue at constant rate; the numerical estimates are given in Sec. VIII.

The above description of whisker growth is essentially one dimensional. A phenomenon of whisker growth in a labyrinth of random electric fields is beyond the scope of this work.

![](./images/814753776488415233_6.jpg)

FIG. 6. Sketch of the whisker growth rates vs time. Solid lines represent the two limiting cases given by Eqs. (21) and (22) within the domains of their applicability ($h \ll L$ and $h \gg L$, respectively). The dashed curves are formal solutions of Eqs. (21) and (22) beyond that domains where they must be sewed. The dash-dotted line shows a hypothetical sewing that would fit the observations of Ref. [61].

## VI. LONG RANGE DIFFUSION
The fact that whiskers grow from their roots without forming any surrounding dents is commonly interpreted as a result of long range uniform drift of material towards whisker roots. That interpretation is experimentally verified (see, e.g., Refs. [8,62]).

The drift necessity follows naturally from the electrostatic theory here. Indeed, taking into account that $E \propto n$, the electrostatic energy related to surface charge density $n$ is proportional to the surface integral $\int n^2 d A$. The latter quantity must be a minimum under the condition of charge conservation, $\int n d A=$ const. It is straightforward to see that the required conditional minimum takes place when $n=$ const, i.e., surface charge is distributed uniformly within its occupied domain. Assuming that charges are tightly pinned to the surface material, the system should maintain uniform material density; hence, long range drift.

The integral laws of minimum energy and charge conservation above do not specify the underlying forces. In addition to the long range Coulomb, there must be some short range forces tightly binding surface charges to surface material and making it move along. A hydrodynamic drag appears to be a conceivable mechanism of such coupling. It is qualitatively similar to a flow caused by a dense enough array of particles pushed through a viscous fluid. This hypothesis remains to be verified at a more quantitative level.

## VII. WHISKER STATISTICS
As explained in the end of Sec. VA above, whisker growth is blocked in the local regions of anomaly low electric field. Because these regions have random locations,

![](./images/814753776488415233_7.jpg)

FIG. 7. Sketches of the coordinate dependencies of random electric field $E(h)$ (top), random functional $\xi \equiv \int_{0}^{h} E(x) d x$ and its square (middle), and free energies: surface contribution $F_{S}$, electrostatic contribution $F_{E}$, and their sum $F=F_{E}+F_{S}$. The vertical dashed line marks the point of $\xi=0$ of $F_{E}$ flattening that gives rise to a barrier $W_{B}$ blocking the whisker growth. The barrier $W$ is the same as in Fig. 3.

this blockage will result in broad statistical distributions of whisker lengths. The observed distributions of this kind are best approximated as log-normal [10,63,64]. Their analytical form is derived here.

As shown in Appendix A [Eq. (A6)], the electrostatic energy gain of a whisker in a nonuniform field $E(x)$ can be presented in the form

$$
F_{E}(h)=-\frac{1}{4 \Lambda} \int_{0}^{h} \xi^{2} d x, \quad \xi(x) \equiv \int_{0}^{x} E\left(x^{\prime}\right) d x^{\prime}. \quad(24)
$$

Because fields $E$ are random, $F_{E}(h)$ becomes a random functional giving rise to barriers in the total free energy $F=F_{E}+F_{S}$ as illustrated in Fig. 7.

Taking into account surface energy, $F_{S}=\sigma \pi d h$, the barrier condition $d F / d h=0$ reduces to $\xi^{2}(h)=4 \Lambda \sigma \pi d$ much below its average, $\xi^{2} \ll\left\langle\xi^{2}\right\rangle$. Such $\xi^{2}$ correspond to flat portions in the dependence $F_{E}(h)$ where the surface contribution slope $\sigma \pi d$ dominates free energy; this observation is reflected in Fig. 7.

The typical block barriers whisker growth during the time of experiment. Indeed, they correspond to the characteristic length scale of field variation of the order of $h$ [see the discussion after Eq. (12)], which leads to the estimate $W_{B} \sim \pi d h \sigma \gtrsim 100 \mathrm{eV}$. On the other hand, we assume long enough times of experiment, during which the average growth rates from Eqs. (21) and (22) allow whisker lengths to reach the regions of blocking barriers.

With the latter assumption, the distribution of whisker lengths can be approximated by the distribution of coordinates of their blocking barriers. It is given by the probability density $g\left(\xi^{2}\right)$ for the random quantity $\xi^{2}$ in a close proximity of $\xi^{2}=0$. As a square of integral over large distances, $\xi^{2}$ can be thought of as a sum of large number of random contributions. According to the central limit theorem, such random quantities are described by the Gaussian distribution

$$
g\left(\xi^{2}\right)=\frac{1}{\sqrt{2 \pi \Delta}} \exp \left[-\frac{\left(\xi^{2}-\left\langle\xi^{2}\right\rangle\right)^{2}}{2 \Delta}\right],\qquad(25)
$$

where angular brackets represent averaging and $\Delta=\left\langle\xi^{4}\right\rangle-$ $\left(\left\langle\xi^{2}\right\rangle\right)^{2}$ is the dispersion.

The momenta $\left\langle\xi^{2}\right\rangle$ and $\left\langle\xi^{4}\right\rangle$ depend on distance $h$ to the metal surface. They can be evaluated based on statistical properties of surface charge fluctuations, which we assume to be uncorrelated at distances exceeding the patch size $L$. Using the corresponding results for $\left\langle\xi^{2}\right\rangle$ and $\left\langle\xi^{4}\right\rangle$ from Appendix B, the probabilistic distribution of whisker lengths takes the form

![](./images/814753776488415233_8.jpg)

FIG. 8. Left: Probabilistic distributions of Eq. (26) for two different values of the numerical parameter $\gamma$. Right: Comparison between probabilistic distribution of Eq. (26) (open circles) and a log-normal fitting curve (solid line).

$$
\begin{aligned}
g(h) & =\frac{1}{\sqrt{2 \pi \Delta(h)}} \exp \left[-\frac{\left(\left\langle\xi^{2}(h)\right\rangle\right)^{2}}{2 \Delta(h)}\right] \\
& =\beta \frac{h}{L} \exp \left\{-\gamma\left[\frac{h}{L} \ln \left(\frac{\left(1+\sqrt{1+(h / L)^{2}}\right]^{2}}{4 \sqrt{1+(h / L)^{2}}}\right)\right]^{2}\right\}.
\end{aligned}
$$
(26)

Here the unknown numerical coefficients $\beta$ and $\gamma$ should not be too different from unity.

The distribution of Eq. (26) is illustrated in Fig. 8. It is a maximum at $h / L \approx \exp (1 / \sqrt{2 \gamma})$ with half-width $\delta(h / L) \approx$ $(\ln 2)(2 \gamma)^{-1 / 4} \exp [1 /(4 \gamma)]$. The log-normal distribution fit is demonstrated in the same figure is in agreement with the experimental statistics [10,63,64].

Two significant limitations underlying Eq. (26) are that of the 1D model of whisker evolution and the infinitely blocking barriers. Relaxing either of them would allow additional whisker growth.

### VIII. NUMERICAL ESTIMATES AND DISCUSSION

Numerical estimates of nucleation parameters are given in Sec. III. Here we estimate the parameters of whisker growth. Using the diffusion coefficient for tin [62] $D \sim$ $10^{-18} \mathrm{~cm}^{2} \mathrm{~s}^{-1}$ and assuming $D=B$ gives for the mobility $b \sim 4 \times 10^{-5} \mathrm{~cm}^{2} \mathrm{~s}^{-1} \mathrm{erg}^{-1}$. Substituting the latter numerical values along with $E_{0} \sim 1 \mathrm{MV} / \mathrm{cm}, h_{0} \sim 10 \mathrm{~nm}$, and $\Lambda=1-3$, Eq. (21) yields $t_{0} \sim(0.3-1) \times 10^{5} \mathrm{~s}$. This estimate is in fair agreement with the data [61,64] on the incubation period preceding constant growth rate (cf. Fig. 6).

For a reasonable patch size $L \sim 3 \mu \mathrm{m}$, the growth rate predicted by Eq. (22) turns out to be 2 orders of magnitude higher than the observed $d h / d t \sim 1 \AA / \mathrm{s}$. This discrepancy can be due to oversimplifications related to the 1D random field treatment. Using more accurate Eq. (23) decreases $d h / d t$ by at least 1 order of magnitude bringing it closer to the data.

The latest stage of whisker growth above critical length $r_{c}$ is described by the characteristic time that is by the factor $E_{0}^{2} /\left\langle E_{T}^{2}\right\rangle \sim 10^{5}$ longer than $\tau_{L}$, i.e., $t_{T} \sim 10^{7}-10^{8} \mathrm{~s}$. This value agrees with the observations that whiskers typically stop growing in a year or so. (Blocking barriers introduced in Sec. VII can provide an alternative explanation of that observation.)

Reasonable agreement with statistical data can be demonstrated by using again $L \sim 3 \mu \mathrm{m}$ and assuming $\gamma \sim 0.1-0.2$. In that case, the curves in Fig. 8 become close to the published statistical data [10,63,64].

Because a significant effort was spent to understand metal whiskers in terms of mechanical stresses, recrystallization, dislocations, etc., it should be noted that the present theory does not rule out these factors. Furthermore, they can be a part of the picture presented in two major aspects. First, they can create local spots of unfavorable energy configurations capable of relaxing through the mechanism of field induced nucleation. That belongs in the general settings of inhomogeneous nucleation strongly facilitated by imperfections and inhomogeneities. Second, local spots of stress, grain boundaries, or dislocations can be sources of surface charge leading to the field induced nucleation as discussed in Sec. IV above.

The above estimates lead to the following scenario of whisker evolution. (i) Stage 1: whiskers nucleate in a subsecond to days time interval (reflecting fluctuations in nucleation barriers due to the local field fluctuations); their dimensions upon nucleation are $h \sim 10 \mathrm{~nm}$ and $d \sim 1 \mathrm{~nm}$, with predominant orientation perpendicular to the metal surface. (ii) Stage 2: Whiskers grow up to the patch size, say $L \sim 3-10 \mu \mathrm{m}$, more or less perpendicular to the surface, with some deviations especially towards patch edges. This process takes a much longer time $t_{0} \sim 10^{4}-10^{5} \mathrm{~s}$ that can be experimentally identified as the whisker incubation time. The growth rate at this stage is very low for almost entire time interval $t_{0}$, with drastic acceleration in the nearest proximity of $t_{0}$ (see Fig. 6). (iii) Stage 3: Whiskers grow way above patch size $L \sim 3-10 \mu \mathrm{m}$ at constant rate $L / t_{L}$ possibly with some degree of winding or kinking (beyond the current theory). At this stage, random field configurations induced by uncorrelated patch charges make growth rates of individual whiskers fluctuating, some of them blocked. The random distribution of blocking barriers determines the statistical distribution of whisker lengths. (iv) Stage 4: If whiskers grow above lengths where feeding by thermal radiation dominates, they evolve further in lateral directions parallel to the metal surface.

### IX. CONCLUSIONS

The above theory describes metal whiskers as a result of metal nucleation and growth in random electric fields induced by charged patches on metal surfaces. The underlying approaches are typical of the physics of phase transitions and disordered systems. This work presents the first whisker theory yielding simple analytical results more or less consistent with the observations. The successes, the remaining questions, and possible experimental verifications of this work theory are summarized next.

#### A. What is understood

(1) Why whiskers are metallic: high (metallic) electric polarizability is required for sufficient energy gain due to whisker formation in external (surface) electric fields.

(2) Why whiskers grow more or less perpendicular to the surface: such are the dominating directions of the surface electric field.

(3) Why whisker parameters are broadly statistically distributed: this reflects fluctuations in metal surface

fields induced by mutually uncorrelated charged patches.

(4) Correlation between whiskers and versatile mor- phology factors, such as (i) grains whose orientation is different from the major orientation of the tin film, (ii) dislocations and dislocation loops, and (iii) mechanical stresses capable of surface buckling, surface contaminations; all related to local surface charges and their induced electric fields. Some metals are more prone to develop whiskers because they can easier form charged patches by absorbing ions, and creating dislocations, grain boundaries, or stresses.

(5) Why external electric bias can significantly accel- erate whisker growth: external electric fields in- crease the nucleation and growth rates.

(6) Why the characteristic whisker evolution follows a certain pattern: a long incubation period followed by an almost constant growth rate that eventually saturates. The predicted incubation time and sub- sequent growth rate agree with the observations.

(7) Why whisker parameters are broadly distributed statistically. The predicted distribution of whisker lengths is close to the observed log-normal statistics.

### B. What is not understood
(1) The microscopic nature of whiskers, their correla- tion with specific surface defects, chemical aspects of whisker development.

(2) The role of whisker crystalline structure in their evolution process.

(3) Whisker growth in 3D random electric field. This process includes whisker winding and kinking.

(4) Possible role of surface (or grain boundary) diffusion limiting whisker growth.

(5) Possible hydrodynamic drag moving surface material uniformly along with ions.

(6) Interwhisker interactions limiting their concentration and affecting growth.

### C. Possible experimental verification
The predicted dependencies of nucleation and growth kinetics vs electric field, temperature, and controlled contamination could be verified experimentally.

(1) Whisker nucleation and growth in external electric fields. This process can be attempted in either flat capacitor configuration or for a whisker inside scanning electron microscope (SEM) where the electric field is readily controlled. In both cases, care should be taken to avoid significant Joule heating and/or electron drag effects, i.e., using voltage rather than current power source.

(2) Whisker nucleation and growth under controlled contamination of metal surface with solutions of charged nanoparticles.

(3) Whisker nucleation and growth under the conditions of strong surface electric fields induced by surface plasmon polariton excitations [65]. This technique could be used for controlled growth of metal nano- wires of desirable parameters on metal surfaces.

(4) Applications to modern large area thin film photo- voltaic technology where whiskers can shunt through the device thereby causing significant reli- ability concerns (which has not been sufficiently addressed yet). Properly replacing those device metal contacts or surface treatments mitigating whisker growth can improve the device reliability and stability with respect to shunting.

In the end, it should be noted that this work presents rather a sketch of theory in its infancy, pointing at important factors and providing order-of-magnitude estimates, yet not developed enough to quantitatively describe whisker evo- lution and statistics in a random electric field. Further effort is called upon to develop this approach.

### ACKNOWLEDGMENTS
The author is grateful to D. Shvydka, A. V. Subashiev, I. V. Karpov, E. Chason, and D. Susan for useful discus- sions. The NASA Electronic Parts and Packaging (NEPP) Program is greatly appreciated for granting permission to use Fig. 1. This work was performed under the auspices of the NSF Grant No. 1066749.

### APPENDIX A: NONUNIFORM POLARIZATION
Following the approach in Ref. [29], p. 17, the electro- static energy gain of a rectilinear metal filament of length $h$ and radius $a \ll h$ in a nonuniform electric field $E(x)$ is given by
$$
F_{E}=(1 / 2) \int_{0}^{h} \varphi(x) \tau(x) d x, \quad \text { (A1) }
$$
where $\tau$ is the field induced charge density and $\varphi(x)=$ $-\int_{0}^{x} E d x$ is the electric potential. The condition of constant potential on the surface of the filament is
$$
\begin{gathered}
-\int E d x+\frac{1}{2 \pi} \int_{0}^{2 \pi} \int_{0}^{h} \frac{\tau\left(x^{\prime}\right) d x^{\prime} d \phi}{R}=0, \\
R=\sqrt{\left(x-x^{\prime}\right)^{2}+4 a^{2} \sin ^{2}(\phi / 2)},
\end{gathered}
$$
where $\phi$ is the angle between planes passing through the axis of the cylinder and through two points on its surface at a distance $R$ apart. We divide the integral into two parts, putting $\tau(x')=\tau(x)+[\tau(x')-\tau(x)]$. Since $h \gg a$, we have for points not too near the ends of the rod,
$$
\frac{\tau(x)}{2 \pi} \iint \frac{d x^{\prime} d \phi}{R} \approx \tau(x) \log \left(\frac{4\left(l^{2}-x^{2}\right)}{a^{2}}\right). \quad \text { (A3) }
$$

044001-10

Thus,
$$
\int_{0}^{x} E d x=\tau(x) \log \left(\frac{4\left(h x-x^{2}\right)}{a^{2}}\right)+\int_{0}^{h} \frac{\tau\left(x^{\prime}\right)-\tau(x)}{\left|x^{\prime}-x\right|} d x^{\prime}.
\tag{A4}
$$

It follows then that $\tau(x)$ is almost proportional (with logarithmic accuracy) to $\int_{0}^{x} E d x$; it can be sought in the form $\tau=A \int_{0}^{x} E d x$ that should be substituted into Eq. (A4). Noting that the integral in Eq. (A4) is dominated by the proximity $x^{\prime}=x$ and representing the integrand numerator as $E(x)(x-x^{\prime})$, one finally gets
$$
\tau(x)=\frac{\int_{0}^{x} E(x) d x}{\log \left[4\left(h x-x^{2}\right) / a^{2}\right]-2}.
\tag{A5}
$$

Substituting the latter expression and assuming as in the body of the text that $\Lambda \gg 1$, the electrostatic free energy becomes
$$
F_{E}(h)=-\frac{1}{4(\Lambda+4 / 3)} \int_{0}^{h}\left(\int_{0}^{x} E\left(x^{\prime}\right) d x^{\prime}\right)^{2} d x, \quad(\mathrm{A} 6)
$$
where $\Lambda$ is defined in Eq. (2). This result reproduces the above used $F_{E} \propto-h^{3}$ and $F_{E} \propto-h$ for the cases of $h \ll L$, $E=$ const and $h \gg L, E \propto 1 / x$, respectively; also, it justifies the claim in Sec. IV B that the point charge caused polarization does not impact the electrostatic energy gain.

## APPENDIX B: RANDOM VARIABLE $\xi^{2}$

Here we evaluate the parameters of statistical distribution of Eq. (25), $\left\langle\xi^{2}\right\rangle$ and $\Delta=\left\langle\xi^{4}\right\rangle-\left(\left\langle\xi^{2}\right\rangle\right)^{2}$. The required averaging gives
$$
\begin{aligned}
\left\langle\xi^{2}\right\rangle & =\left\langle\left(\int_{0}^{h} d r \int d^{2} \rho \frac{e n(\boldsymbol{\rho}) r}{\left(r^{2}+\rho^{2}\right)^{3 / 2}}\right)^{2}\right\rangle \\
& =\int d^{2} \rho \int d^{2} \rho^{\prime} \frac{e^{2}\left\langle n(\boldsymbol{\rho}) n\left(\boldsymbol{\rho}^{\prime}\right)\right\rangle}{\left(\rho^{2}+h^{2}\right)^{1 / 2}\left(\rho^{\prime 2}+h^{2}\right)^{1 / 2}}. \quad(\mathrm{B} 1)
\end{aligned}
$$

Here, $\boldsymbol{\rho}$ and $\boldsymbol{\rho}^{\prime}$ are two-dimensional radius vectors in the plane of surface charge; $d^{2} \rho$ and $d^{2} \rho^{\prime}$ are elemental areas. Assuming uncorrelated random charge patches, one can write
$$
e^{2}\left\langle n(\boldsymbol{\rho}) n\left(\boldsymbol{\rho}^{\prime}\right)\right\rangle=C_{1} \delta\left(\boldsymbol{\rho}-\boldsymbol{\rho}^{\prime}\right),
\tag{B2}
$$
where $\delta$ stands for the Dirac delta function, and $C_{1}$ is a constant. Its order of magnitude estimate is $C_{1} \sim\left\langle(n e L)^{2}\right\rangle$. The delta-function representation remains adequate when $\rho \gg L$, where $L$ is the linear dimension of a charged patch. Substituting the latter correlation function into Eq. (B1) and performing integration over $\rho$ from $L$ to $\infty$ yields
$$
\left\langle\xi^{2}\right\rangle=2 \pi C_{1} \ln \left[\frac{\left(L+\sqrt{L^{2}+h^{2}}\right)^{2}}{4 L \sqrt{L^{2}+h^{2}}}\right].
\tag{B3}
$$

For the region of $h \gg L$, Eq. (B3) simplifies to $\left\langle\xi^{2}\right\rangle=C_{1} \ln (h / 4 L)$.

Similarly, $\left\langle\xi^{4}\right\rangle$ can be reduced to the integral over area elements $d^{2} \rho d^{2} \rho^{\prime} d^{2} \rho^{\prime \prime} d^{2} \rho^{\prime \prime \prime}$ with the integrand
$$
\frac{\left\langle n(\boldsymbol{\rho}) n\left(\boldsymbol{\rho}^{\prime}\right) n\left(\boldsymbol{\rho}^{\prime \prime}\right) n\left(\boldsymbol{\rho}^{\prime \prime \prime}\right)\right\rangle}{\left(\rho^{2}+h^{2}\right)^{1 / 2}\left(\rho^{\prime 2}+h^{2}\right)^{1 / 2}\left(\rho^{\prime \prime 2}+h^{2}\right)^{1 / 2}\left(\rho^{\prime \prime \prime 2}+h^{2}\right)^{1 / 2}}.
$$

Here, $\langle n\rangle=0$; hence, finite contributions to the integral arise from the product of two pair averages $e^{2}\left\langle n(\boldsymbol{\rho}) n\left(\boldsymbol{\rho}^{\prime}\right)\right\rangle$ given in Eq. (B2), and from the correlation function $e^{4}\left\langle n(\boldsymbol{\rho}) n\left(\boldsymbol{\rho}^{\prime}\right) n\left(\boldsymbol{\rho}^{\prime \prime}\right) n\left(\boldsymbol{\rho}^{\prime \prime \prime}\right)\right\rangle=C_{2} \delta\left(\boldsymbol{\rho}-\boldsymbol{\rho}^{\prime}\right) \delta\left(\boldsymbol{\rho}-\boldsymbol{\rho}^{\prime \prime}\right) \delta\left(\boldsymbol{\rho}-\boldsymbol{\rho}^{\prime \prime \prime}\right)$. The former product cancels out with $\left\langle\xi^{2}\right\rangle^{2}$ in the definition of dispersion $\Delta$. The latter term yields
$$
\Delta=2 \pi C_{2} h^{-2}.
\tag{B4}
$$

The order of magnitude estimate for the coefficient is $C_{2} \sim|n e|^{4} L^{6}$. Therefore, the dispersion is relatively small,
$$
\frac{\left(\left\langle\xi^{2}\right\rangle\right)^{2}}{\Delta} \sim\left[\frac{h}{L} \ln \left(\frac{h}{4 L}\right)\right]^{2} \gg 1.
\tag{B5}
$$

[1] NASA Goddard Space Flight Center tin whisker homepage, http://nepp.nasa.gov/whisker.

[2] http://www.calce.umd.edu/lead-free/other/BRUSSE_ACI .pdf.

[3] NASA Goddard Space Flight Center tin whisker homepage, http://nepp.nasa.gov/whisker/other_whisker.

[4] J. R. Barnes, Bibliography for tin whiskers, zinc whiskers, cadmium whiskers, indium whiskers, and other conductive metal and semiconductor whiskers, 2013, http://www .dbicorporation.com/whiskbib.htm.

[5] NASA Goddard Space Flight Center tin whisker homepage, http://nepp.nasa.gov/whisker/reference/tech_papers/2012- Panashchenko-IPC-Art-of-Metal-Whisker-Appreciation .pdf.

[6] NASA Goddard Space Flight Center tin whisker homepage, http://nepp.nasa.gov/whisker/photos/index.html.

[7] R. Shetty, Electrodeposited tin properties and their effect on component finish reliability, in Proceedings of the 2004 International Conference on Business of Electronic Product Reliability and Liability, http://ieeexplore.ieee.org/xpl/ mostRecentIssue.jsp?punumber=9146, p. 29.

[8] E. R. Crandall, Factors governing thin whisker growth, Ph.D. thesis, Auburn University, Auburn, Alabama, 2012, http://ldfcoatings.com/articles/ErikaCrandall.pdf.

[9] T. Munson and P. Solis, Metal whiskers: Does surface contamination have an effect of whisker formation?, http://www.ipcoutlook.org/pdf/metal_whiskers_does_surface_ contamination_ipc.pdf.

[10] T. Fang, M. Osterman, and M. Pecht, Statistical analysis of tin whisker growth, Microelectron. Reliab. 46, 846 (2006).

[11] P. Sarobol, J. P. Koppes, W. H. Chen, P. Sub, J. E. Blendell, and C. A. Handwerker, Recrystallization as a nucleation mechanism for whiskers and hillocks on thermally cycled Sn-alloy solder films, Mater. Lett. 99, 76 (2013).

[12] S. H. Liu, C. Chen, P. C. Liu, and T. Chou, Tin whisker growth driven by electrical currents, J. Appl. Phys. 95, 7742 (2004).

[13] Y. W. Lin, Y. S. Lai, Y. L. Lin, and C. R. Kao, Effect of UBM thickness on the mean time to failure of flip-chip solder joints under electromigration, J. Electron. Mater. 37, 96 (2008).

[14] R. D. Hilty, N. Corman, and H. Herrmann, Electrostatic fields and current-flow impact on whisker growth, IEEE Trans. Electron. Packag. Manuf. 28, 75 (2005).

[15] M. A. Ashworth, G. D. Wilcox, R. L. Higginson, R. J. Heath, and C. Liu, Effect of direct current and pulse plating parameters on tin whisker growth from tin electrodeposits on copper and brass substrates, Trans. Inst. Met. Finish. 91, 260 (2013).

[16] G. T. Galyon, Annotated tin whisker bibliography and anthology, 2003, http://thor.inemi.org/webdownload/ newsroom/TW_biblio-July03.pdf.

[17] W. J. Choi, G. Galyon, K.-N. Tu, and T. Y. Lee, The structure and kinetics of tin-whisker formation and growth on high tin content finishes, in Handbook of Lead-Free Solder Technology for Microelectronic Assemblies, edited by K. J. Puttlitz and K. A. Slater (Marcel Dekker, Inc., New York, Basel, 2004), p. 147.

[18] Y. Zhang, Tin whisker discovery and research, in Soldering in Electronics, edited by K. Suganuma (Marcel Dekker, Inc., New York, 2004), p. 121.

[19] K. N. Tu, J. O. Suh, and A. T. Wu, Tin whisker growth on lead-free solder finishes, in Lead-Free Solder Interconnect Reliability, edited by D. Shangguan (ASM International, Materials Park, OH, 2005), p. 851.

[20] D. Bunyan, M. A. Ashworth, G. D. Wilcox, R. L. Higgin- son, R. J. Heath, and C. Liu, Tin whisker growth from electroplated finishes: A review, Trans. Inst. Met. Finish. 91, 249 (2013).

[21] K. Nakai, T. Sakamoto, S. Kobayashi, M. Takamizawa, K. Murakami, and M. Hino, A model for nucleation of tin whisker through dislocation behavior, J. Phys. Conf. Ser. 165, 012089 (2009).

[22] M. Sobiech, U. Welzel, E. J. Mittemeijer, W. Hgel, and A. Seekamp, Driving force for Sn whisker growth in the system CuSn, Appl. Phys. Lett. 93, 011906 (2008).

[23] J. Smetana, Theory of tin whisker growth: The end game, IEEE Trans. Electron. Packag. Manuf. 30, 11 (2007).

[24] M. W. Barsoum, E. N. Hoffman, R. D. Doherty, S. Gupta, and A. Zavaliangos, Driving force and mechanism for spontaneous metal whisker formation, Phys. Rev. Lett. 93, 206104 (2004).

[25] U. Lindborg, A model for the spontaneous growth of zinc, cadmium and tin whiskers, Acta Metall. 24, 181 (1976).

[26] D. Kaschiev, Nucleation: Basic Theory with Applications (Butterworth-Heinemann, Oxford, Amsterdam, 2000).

[27] V. B. Warshavsky and A. K. Shchekin, The effects of the external electric feld in thermodynamics of formation of dielectric droplet, Colloids Surf. A 148, 283 (1999).

[28] J. O. Isard, Calculation of the influence of an electric field on the free energy of formation of a nucleus, Philos. Mag. 35, 817 (1977).

[29] L. D. Landau, I. M. Lifshitz, and L. P. Pitaevskii, Electro- dynamics of Continuous Media (Pergamon, Oxford, New York, 1984).

[30] V. G. Karpov, Y. A. Kryukov, S. D. Savransky, and I. V. Karpov, Nucleation switching in phase change memory, Appl. Phys. Lett. 90, 123504 (2007).

[31] V. G. Karpov, Y. A. Kryukov, I. V. Karpov, and M. Mitra, Field induced nucleation in glasses, Phys. Rev. B 78, 052201 (2008).

[32] I. V. Karpov, M. Mitra, D. Kau, G. Spadini, Y. A. Kryukov, and V. G. Karpov, Evidence of pulse induced nucleation in phase change memory, Appl. Phys. Lett. 92, 173501 (2008).

[33] V. G. Karpov, Y. A. Kryukov, I. V. Karpov, and M. Mitra, Crystal nucleation in phase change memory, J. Appl. Phys. 104, 054507 (2008).

[34] M. Nardone, V. G. Karpov, C. Jackson, and I. V. Karpov, Unified model of nucleation switching, Appl. Phys. Lett. 94, 103509 (2009).

[35] M. Nardone and V. G. Karpov, Nucleation of metals by strong electric fields, Appl. Phys. 100, 151912 (2012).

[36] M. Nardone and V. G. Karpov, Phenomenological theory of non-photochemical laser induced nucleation, Phys. Chem. Chem. Phys. 14, 13601 (2012).

[37] V. G. Karpov, M. Nardone, and N. I. Grigorchuk, Plasmonic mediated nucleation of nanoparticles, Phys. Rev. B 86, 075463 (2012).

[38] V. G. Karpov, M. Nardone, and A. V. Subashiev, Plasmonic mediated nucleation of resonant nanocavities, Appl. Phys. Lett. 101, 031911 (2012).

[39] P. F. James, Kinetics of crystal nucleation in silicate glasses, J. Non-Cryst. Solids 73, 517 (1985).

[40] E. D. Zanotto and P. F. James, Experimental tests of the classical nucleation theory for glasses, J. Non-Cryst. Solids 74, 373 (1985).

[41] M. C. Weinberg, E. D. Zanotto, and S. Manrich, Classical nucleation theory with a size dependent surface tension, Phys. Chem. Glasses 33, 99 (1992).

[42] K. F. Kelton, Crystal nucleation in liquids and glasses, in Solid State Physics, edited by H. Ehrenreich and D. Turnbull (Academic Press, Boston, 1991), Vol. 45, p. 75.

[43] B. B. Alchagirov, O. I. Kurshev, and T. M. Taova, Surface tension of tin and its alloys with lead, Russ. J. Phys. Chem. A 81, 1281 (2007).

[44] C. M. Rice, A determination of the surface tension of tin in the solid state, M.S. thesis, University of Missouri, Rolla, Missouri, 1949.

[45] K. T. Aust and B. Chalmers, The specific energy of crystal boundaries in tin, Proc. R. Soc. A 204, 359 (1950).

[46] H. Saka, Y. Nishikawa, and T. Imura, Melting temperature of In particles embedded in Al Matrix, Philos. Mag. A 57, 895 (1988).

[47] J. Cheng, P. T. Vianco, B. Zhang, and J. C. M. Li, Nucle- ation and growth of tin whiskers, Appl. Phys. Lett. 98, 241910 (2011).

[48] J. B. Camp, T. W. Darling, and R. E. Brown, Macroscopic variations of surface potentials of conductors, J. Appl. Phys. 69, 7126 (1991).

[49] S. Yin, D. Y. Li, and R. Bouchard, Effects of strain rate of prior deformation on corrosion and corrosive wear of AISI 1045 steel in a 3.5 pct NaCl solution, Metall. Mater. Trans. A 38A, 1032 (2007).

[50] J. Namahoot, Effect of deformation on corrosion of Al-Mn alloys, Ph.D. thesis, Metallurgy and Materials School of Engineering, The University of Birmingham, 2004, http://etheses.bham.ac.uk/108/1/Namahoot05PhD.pdf.

[51] B. I. Kolodii, Theoretical investigation of the interaction of a deformed metal with a corrosion medium, Mater. Sci. 36, 884 (2000).

[52] B. Balakrisnan, C. C. Chum, M. Li, Z. Chen, and T. Cahyadi, Fracture toughness of Cu-Sn intermetallic thin films, J. Electron. Mater. 32, 166 (2003).

[53] G. K. Wertheim, D. M. Riffe, J. E. Rowe, and P. H. Curtin, Crystal field splitting and charge flow in the buckled-dimer reconstruction of Si, Phys. Rev. Lett. 67, 120 (1991).

[54] J. Labaziewicz, Y. Ge, D. R. Leibrandt, S. X. Wang, R. Shewmon, and I. L. Chuang, Phys. Rev. Lett. 101, 180602 (2008).

[55] G. H. Low, P. F. Herskind, and I. L. Chuang, Finite-geometry models of electric field noise from patch potentials in ion traps, Phys. Rev. A 84, 053425 (2011).

[56] E. Bano, T. Ouisse, L. Di Cioccio, S. Karmann, Surface potential fluctuations in metaloxidesemiconductor capaci- tors fabricated on different silicon carbide polytypes, Appl. Phys. Lett., 65, 2723 (1994).

[57] R. Dubessy, T. Coudreau, and L. Guidoni, Electric field noise above surfaces: A model for heating-rate scaling law in ion traps, Phys. Rev. A 80, 031402R (2009).

[58] S. M. Sze, Physics of Semiconductor Devices (Wiley, New York, 1981).

[59] S. M. Rytov, Theory of electric fluctuations and thermal radiation, electronics research directorate, Air Force Cambridge Research Center, Air Research and Development Command, U.S. Air Force, 1959.

[60] E. M. Lifshitz and L. P. Pitaevskii, Physical Kinetics (Elsevier, Amsterdam, Boston, 2008).

[61] N. Jadhav, E. Buchovecky, E. Chason, and A. Bower, Real-time SEM/FIB studies of whisker growth and surface modification, J. Miner. Met. Mater. Soc. 62, 30 (2010).

[62] T. A. Woodrow, Tracer diffusion in whisker prone tin platings, in Proceedings of SMTA International Conference, Rosemont, IL, 2006 (SMTA International, Edina, MN, 2006), pp. 1-50.

[63] L. Panashchenko, Evaluation of environmental tests for tin whisker assessment, M.S. thesis, University of Maryland, 2009, http://hdl.handle.net/1903/10021.

[64] D. Susan, J. Michael, R. P. Grant, B. McKenzie, and W. G. Yelton, Morphology and growth kinetics of straight and kinked tin whiskers, Metall. Mater. Trans. A 44, 1485 (2013).

[65] S. A. Maier, Plasmonics: Fundamentals and Applications (Springer, New York, 2007).

044001-13