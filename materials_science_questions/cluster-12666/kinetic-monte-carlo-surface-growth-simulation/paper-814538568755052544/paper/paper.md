# Polymer Surface Transport Is a Combination of in-Plane Diffusion and Desorption-Mediated Flights
Dapeng Wang, $^{\dagger}$ Huai-Ying Chin, $^{\dagger}$ Chunlin He, Mark P. Stoykovich, and Daniel K. Schwartz*

Department of Chemical and Biological Engineering, University of Colorado, Boulder, Colorado 80309, United States

Supporting Information

## ABSTRACT:
Previous studies of polymer motion at solid/liquid interfaces described the transport in the context of a continuous time random walk (CTRW) process, in which diffusion switches between desorption-mediated "flights" (i.e., hopping) and surface-adsorbed waiting-time intervals. However, it has been unclear whether the waiting times represented periods of complete immobility or times during which molecules engaged in a different (e.g., slower or confined) mode of interfacial transport. Here we designed high-throughput, single-molecule tracking measurements to address this question. Specifically, we studied polymer dynamics on either chemically homogeneous or nanopatterned surfaces (hexagonal diblock copolymer films) with chemically distinct domains, where polymers were essentially excluded from the low-affinity domains, eliminating the possibility of significant continuous diffusion in the absence of desorption-mediated flights. Indeed, the step-size distributions on homogeneous surfaces exhibited an additional diffusive mode that was missing on the chemically heterogeneous nanopatterned surfaces, confirming the presence of a slow continuous mode due to 2D in-plane diffusion. Kinetic Monte Carlo simulations were performed to test this model and, with the theoretical in-plane diffusion coefficient of $D_{2D} = 0.20\ \mu m^2/s$, we found a good agreement between simulations and experimental data on both chemically homogeneous and nanopatterned surfaces.

![](./images/814538568755052544_1.jpg)

Polymer dynamics at solid/liquid interfaces is broadly relevant to applications including heterogeneous catalysis, thin-film formation processes, blocking strategies in enzyme-linked immunosorbent assays, and so on. $^{1-6}$ Thanks to advances in microscopy methods in the last two decades, $^{7,8}$ polymer dynamics at solid/liquid interfaces have been characterized at the single-molecule level using fluorescence correlation spectroscopy (FCS), $^{9-13}$ molecular tracking, $^{14}$ high-speed atomic force microscopy (HS-AFM), $^{15}$ or using ensemble methods such as fluorescence recovery after photobleaching (FRAP) $^{16-18}$ and evanescent-wave dynamic light scattering. $^{19}$ Interestingly, enormous discrepancies in the magnitude of the surface diffusion coefficient $(D_{\parallel})$ have been measured using different methods. For example, studies have reported $D_{\parallel}$ of rhodamine, 10 kg/mol polyethylene glycol (PEG) and 100 kg/mol poly(2-vinylpyridine) in the range of $5-15\ \mu m^2/s$ using FCS, $^{10,11,20}$ which is only a factor of 10-100 smaller than the corresponding bulk diffusion coefficients. However, $D_{\parallel}$ measured by FRAP and HS-AFM for similar probe molecules indicated that $D_{\parallel}$ was decelerated by 5 or 6 orders of magnitude relative to solution-phase diffusion. $^{18,21}$ These discrepancies suggest that different techniques are sensitive to distinct populations of diffusing species. Indeed, molecular tracking studies from independent laboratories have identified multiple populations, including one that is apparently immobile during the experimentally accessible time window. $^{18,22}$ The remainder of the adsorbed polymers exhibit continuous time random walks (CTRW) in which diffusion switches between flights and apparently immobile waiting-time periods. $^{23-26}$ Interestingly, the diffusion coefficient of the flying mode is similar to that reported by FCS, $^{10,27}$ suggesting that these seemingly diverse results could potentially be reconciled if the apparently immobile CTRW waiting-times actually comprise slow in-plane diffusion as measured using FRAP and HS-AFM.

Here, we designed single-molecule tracking experiments to test the hypothesis above. Specifically, in order to distinguish the putative slow in-plane (2D) diffusion from apparent motion due to noisy images, we compared polymer diffusion on chemically homogeneous surfaces and surfaces with periodic nanostructures comprised of chemically distinct domains; the latter surface was designed to eliminate the possibility of slow 2D diffusion. In contrast to previous studies, $^{28-34}$ we employed nanostructures with very small length scales (~30 nm), so the periodicity of the pattern could not be resolved. However, the affinity of the "tracer" molecules was such that they adsorbed only on very small disconnected domains and could not move from one domain to another without a desorption-mediated flight. By comparing this motion to diffusion on homogeneous surfaces, we were able to identify and characterize the true in-plane diffusive mode.

The nanopatterned surfaces comprised self-assembled diblock copolymer thin films. In particular, polystyrene-b-

Received: March 4, 2016

Accepted: March 22, 2016

poly(methyl methacrylate) (PS-b-PMMA) thin films with varying PS fractions were used to fabricate hexagonally patterned surfaces with isolated cylindrical PS domains (PS-hexagonal) and lamellar surfaces with alternating domains in a fingerprint texture. $^{35-39}$ Additional experimental details are described in the Supporting Information (SI). Figure 1a shows a scanning electron microscope (SEM) image of a self-assembled PS-b-PMMA block copolymer thin film (molecular weights of PS and PMMA are 20 and 50 kg/mol, respectively) with PS domains arranged on a hexagonal lattice. In this case, the block copolymer features visible on the film surface persist through the film, as induced by the application of a neutral-wetting brush that causes the domain interfaces to be oriented perpendicular to the substrate. The mean diameter and the nearest neighbor lattice spacing of the PS domains were estimated to be $32 \pm 3$ and $41 \pm 3$ nm from the SEM images. For this hexagonal phase, the PS volume fraction was 32%, as determined from the molecular weight ratio of the PS-b-PMMA precursor. Increasing the PS volume fraction led to a change in the surface morphology from hexagonal to lamellar. Moreover, subtle changes in the composition of the symmetric block copolymers were used to change the long-range domain connectivity of the lamellar films. $^{38,39}$ SEM images of thin films with PS or PMMA continuous lamellar morphologies are shown in Figure S1.

![](./images/814538568755052544_2.jpg)

Figure 1. (a) Representative SEM image of the PS-hexagonal surface. The PS and PMMA domains appear as light and dark gray, respectively. The scale bar represents 100 nm. (b) Schematic representation of adsorbed dextran chains (red) on a nanopatterned PS-hexagonal surface. The gray circles and turquoise matrix indicate PS domains and the continuous PMMA phase, respectively. The 2D in-plane motion of dextran molecules is confined within the isolated PS domains.

The fluorescently labeled tracer molecules, dextran with a molecular weight of 10 kg/mol, were carefully chosen over other polymeric tracers because they exhibited an extreme contrast in affinity between PS and PMMA surfaces. The hydrodynamic radius of 10 kg/mol dextran is approximately 2 nm. $^{40}$ Therefore, the calculated diffusion coefficient of the dextran in aqueous solutions is $110\ \mu\text{m}^2/\text{s}$ based on the Stokes−Einstein equation. In fact, at the concentration used in these experiments $(10^{-11}\ \text{M})$, corresponding to a steady state surface coverage of 0.006 molecules per $\mu\text{m}^2$, a measurable steady state coverage of dextran was observed on PS surfaces, but we were unable to observe significant amounts of dextran on PMMA surfaces. Total internal reflection fluorescence microscopy (TIRFM) was used to record trajectories of individual tracer molecules at the interface between aqueous solutions and the self-assembled block copolymer thin films or chemically homogeneous PS surfaces. As previously reported, the positions of identified objects in consecutive images were connected to construct molecular trajectories using a custom-developed algorithm. $^{41}$ For each surface, approximately $10^4$ trajectories overall (with surface residence times longer than 1

![](./images/814538568755052544_3.jpg)

Figure 2. (a) Representative trajectories of 10 kg/mol dextran (residence time 2 s) on a PS-hexagonal surface. (b) Representative trajectories on a PS-hexagonal surface exhibiting the lateral position of dextran versus time. Kymographs of a dextran molecule on (c) a PS-hexagonal surface or (d) a homogeneous PS surface. All scale bars represent $0.5\ \mu\text{m}$. The color bars on the right indicate the fluorescence intensity in arbitrary units.

s) were accumulated immediately after injecting the sample into the flow cell, likely minimizing aging effects on the observed trajectories. $^{42,43}$ Even so, trajectories were divided into mobile and apparently immobile groups. In the analysis presented below, we attempted to eliminate trajectories that were entirely immobile, and focused on the 1000–3000 mobile trajectories on each surface. The details of the experiments are described in the SI.

Figure 2a shows a representative group of trajectories on PS- hexagonal surfaces. The surface dynamics of dextran exhibited intermittent motion with occasional long flights alternating with periods of apparent immobility, consistent with previous studies (Figure 2b). $^{18,26,44}$ Interestingly, when we compared the diffusion between hexagonally patterned and homogeneous PS surfaces, we found small but significant differences in these "apparent immobile periods". Examples are shown in the form of kymographs in Figure 2c,d. Specifically, the intensity- weighted centroids of a dextran molecule on a PS-hexagonal surface remained in the same position as time progressed (Figure 2c), while centroids on a homogeneous PS surface deviated by more than one pixel from frame to frame (Figure 2d). Additional examples are shown in Figure S2.

To provide a more quantitative picture of these differences, we calculated the self-part of the van Hove correlation function $G(\Delta x, \Delta t),^{45}$ which indicates the probability that a polymer chain executes a displacement with absolute distance $\Delta x$ along the $x$ or $y$ coordinate in a time interval $\Delta t$ (each two- dimensional displacement, $r$, was decomposed into its components in the $x$ and $y$ directions). Because these distributions were very similar on nanopatterned surfaces with hexagonal and lamellar morphologies, we plotted only the distributions of dextran on pure PS and PS-hexagonal surfaces in Figure 3 for clarity; data on all surfaces are shown in Figure S3.

Qualitatively, the shapes of $G(\Delta x, 0.1$ s) could be divided into multiple regions, including narrow peaks at short distances corresponding to the immobile steps (the width of the short- distance peak did not change as a function of $\Delta t$, see Figure S4) and extended tails representing the statistics of long flights. The presence of long flights on PS-hexagonal surfaces (where PS domains were disconnected) indisputably indicated that the long jumps were desorption-mediated (with an approximate bulk diffusion coefficient of $110 \ \mu m^2/s$). $^{46-52}$ Interestingly, as indicated by the tails of the distributions, long flights were more frequently observed on PS-hexagonal surfaces compared to PS surfaces. As previously proposed, $^{53}$ a given flight may comprise multiple excursions (i.e., "hops") through the liquid phase, and ends only when the molecule successfully readsorbs. Thus, the longer flights on PS-hexagonal surfaces were presumably due to the reduced probability of readsorption on the PS-hexagonal surfaces (since the dextran was extremely unlikely to adsorb on PMMA regions) resulting in additional hops prior to readsorption. This is also consistent with the results of the simulations described below. Importantly, by comparing $G(\Delta x$, 0.1 s) on different surfaces (Figures 3 and S3), we were able to identify the existence of an additional regime that has not been previously observed. $^{18,26}$

![](./images/814538568755052544_4.jpg)

Figure 3. Step-size distribution $G(\Delta x, 0.1$ s) of 10 kg/mol dextran on the surface of chemically homogeneous PS (black squares) or PS- hexagonal surfaces (red circles). The symbols denote the experimental data. The solid lines represent the simulation results with 1 (black), 2 (red), or 3 (gray) parameters in Table S1, using the model described in the main text.

It is interesting to consider the underlying mechanism resulting in the difference of $G(\Delta x, 0.1$ s) in the intermediate region, that is, the higher probability of displacements 100–600 nm in length on the homogeneous PS surfaces. In principle, several mechanisms could be at play. Because polymer surface dynamics are known to exhibit CTRW statistics with periods of apparent immobility and frequent long jumps, a difference in the distribution of waiting time intervals $(\tau_{des})$ between two consecutive jumps could potentially result in a change in the form of $G(\Delta x, 0.1$ s); we directly tested this possibility by constructing the waiting time distributions. Here we used a threshold distance, $0.5 \ \mu m$, based on empirical observations in Figure 3, to define desorption-mediated flights. Figure 4a shows waiting-time distributions of dextran molecules on nano- patterned and homogeneous surfaces. Visually, the waiting- time distributions on both surfaces were almost identical (as expected, given that dextran is expected to adsorb almost entirely on PS regions of the patterned surfaces) and could be empirically described using two power-law regimes for short and long time intervals. The apparent power-law exponents at short waiting-time regimes were 1.0 and 0.9 on PS and PS- hexagonal surfaces, respectively. The power-law exponents for the long waiting-time regimes were equal to 2.2 on both surfaces. Thus, the waiting time statistics were essentially identical on homogeneous and nanopatterned surfaces, suggesting that this was not the source of the significant differences in the step-size distributions (Figure 3). This conclusion was further verified using kinetic Monte Carlo simulations as described below.

Another mechanism that could potentially explain the behavior of $G(\Delta x, 0.1$ s) in the intermediate region involves a difference in the distribution of relatively short desorption- mediated flights. This was tested by comparing the step size distributions on different nanopatterned surfaces, i.e. hexagonal vs lamellar, where the PS area fraction varied in the range 0.32–0.51. In principle, the statistics of this type of flight should be related to the PS surface fraction, since readsorption is likely to occur only on PS surface regions. However, this change in the PS surface area fraction did not result in significant differences between the corresponding step-size distributions (see Figure S3 and discussion in the Supporting Information), suggesting that this was only a modest effect in this regime, and that the


![](./images/814538568755052544_5.jpg)

Figure 4. (a) Distribution of waiting times $\tau_{\text{des}}$ between jump events on homogeneous PS (squares) and PS-hexagonal (cycles) surfaces. Solid lines correspond to the power law fits in the short and long time regimes. Distributions of standard deviation of position in each waiting-time period on (b) homogeneous PS and (c) PS-hexagonal surfaces.

high incidence of intermediate steps on homogeneous PS surfaces was not due to short desorption-mediated flights.

Having eliminated the possibilities associated with the conventional CTRW model, the most likely explanation for the enhancement of $G(\Delta x, 0.1\ \text{s})$ in the intermediate region for homogeneous PS surfaces involves the presence of true in-plane surface diffusion where the dextran chains are not confined to small PS domains. In contrast, on nanopatterned surfaces, the presence of the continuous PMMA regions limits in-plane diffusion to occur within individual PS domains (see SI, Page S6). In particular, on a PS-hexagonal surface, in-plane motion of a dextran molecule would be confined within an isolated 30 nm PS domain, and the dextran molecule could move to another PS domain only via a desorption-mediated flight (see Figure 1b). Therefore, comparing the intermediate part of $G(\Delta x, 0.1\ \text{s})$ on pure PS and nanopatterned surfaces provides direct information about the true in-plane diffusion. Notably, this scenario is in good agreement with previous theoretical work predicting that surface diffusion comprises both desorption-mediated flights and in-plane diffusion. $^{48,51}$

To study the in-plane diffusion, we carefully analyzed the molecular trajectories within the waiting-time periods, again using a threshold distance of $0.5\ \mu\text{m}$ to define flights. We calculated the standard deviation of positions within each waiting-time period to quantify the positional variation, and determined the distributions of these data for nanopatterned PS-hexagonal and homogeneous PS surfaces. We found that the distribution of standard deviations on the nanopatterned surfaces (Figures 4c and S5) had only a single major peak centered at a value of approximately 25 nm, which is consistent with the localization uncertainty in our experiments (and the size of isolated PS domains), indicating that the molecular position during most waiting-time periods was either completely immobile or confined within an individual PS domain. In contrast, the distribution of standard deviations on the homogeneous PS surface (Figure 4b) was bimodal with a peak centered at 25 nm indicating immobility within some waiting periods and a broad peak at larger distances indicating the presence of in-plane diffusion in other waiting periods. This supported our hypothesis that the putative in-plane diffusion was suppressed by the presence of nanostructures on the PS-hexagonal surfaces. By defining an empirical threshold of 0.095 $\mu\text{m}$ in Figure 4b, we estimated that approximately 40% of the waiting-time periods were immobile.

These observations provide strong support for the existence of a new mode of surface diffusion that involves the 2D in-plane motion of adsorbed polymers (Figure 1b). However, given the complexity of the surface diffusion mechanisms, comprising immobile periods, in-plane diffusion and desorption-mediated flights of all lengths, it is difficult to extract the effective diffusion coefficient associated with in-plane motion directly from the experimental data. To make a quantitative comparison between this model and the data, therefore, we performed 2D lattice kinetic Monte Carlo simulations that incorporated both desorption-mediated jumps and in-plane diffusion (with a diffusion coefficient $D_{2\text{D}}$) within the context of a CTRW model. The strategy was to identify universal parameters that accurately described the trajectory statistics on both homogeneous PS and nanopatterned PS-hexagonal surfaces.

The simulations were designed to closely mimic experimental conditions. In the simulations, each lattice site, which could be either PS or PMMA, represented an area of $0.01 \times 0.01\ \mu\text{m}^2$ within the $100 \times 100\ \mu\text{m}^2$ two-dimensional lattice. For PS-hexagonal surfaces, nonoverlapping PS domains were stochastically placed on the matrix with a surface fraction of 32%. We used the criterion that the mobile dextran molecules could only occupy lattice sites corresponding to PS. CTRW simulations were performed in analogy with previous work, $^{22}$ where waiting times alternated with desorption-mediated flights. Briefly, the duration of a particular waiting time was drawn from the power-law distribution $\psi(\tau) \sim \tau^{-\alpha}$ with a power-law exponent $\alpha$ of 1.20 and 1.18 for homogeneous PS and PS-hexagonal surfaces, respectively (see SI for details). In contrast with previous work, where molecules were assumed to be immobile during a waiting-time period, in these simulations a given waiting time was comprised of either immobility or in-plane diffusion (within connected domains of PS sites), consistent with the empirical observations described above. The in-plane diffusion was assumed to be Gaussian, $^{54}$ with a displacement probability of $G_{\text{s}}(r, \Delta t) = (1/\sqrt{4\pi D_{2\text{D}}\Delta t})\cdot\exp(-r^2/4D_{2\text{D}}\Delta t)$ where $r$ represents displacement in a time interval of $\Delta t$. Consistent with previous work, $^{22}$ desorption-mediated hops

were modeled using two-dimensional on-lattice random walks with a flight-length drawn from the power law function $f(r) \sim r^{-\beta}$ with a universal step-size power-law exponent $\beta = 1.30$ (see SI for details), based on our experimental observations. For each sampled flight of $r$, the molecule executed a random walk on the square lattice with an appropriate number of steps $n = r^2/0.0001$ to explore a distance $r$ (on average), disregarding the local nanostructures on the lattice matrix. Therefore, on a nanopatterned surface, the final step of the flight may end on a PMMA site. In this case, it was assumed that the molecule did not readsorb, but instead executed another flight with a newly sampled $r$ until the last step resided on a PS site. In the simulation, the only adjustable parameter was $D_{2D}$, while the rest of parameters were designed to be similar to experimentally measured values. We found that a value of $D_{2D} = 0.20\ \mu\text{m}^2/\text{s}$ in the simulations resulted in very good agreement between the experiments and simulations on both surfaces (see lines in Figure 3). We note that the simulations were sensitive to the $D_{2D}$ value. We were able to obtain good agreement with experimental observations only for values of $D_{2D}$ in the range $0.18$-$0.22\ \mu\text{m}^2/\text{s}$. This further supported our model, and was consistent with the conclusion that true in-plane diffusion had a relatively slow diffusion coefficient of $D_{2D} = 0.20\ \mu\text{m}^2/\text{s}$ in some waiting-time periods. Therefore, the suppression of this in-plane diffusion on nanopatterned surface, is sufficient to understand the differences in the step-size distributions on the various surfaces. Moreover, we studied the effect of the parameter $\alpha$ in $\psi(\tau)$ on the shape of step-size distributions. In particular, when we increased the parameter $\alpha$ from $1.18$ to $1.20$ in the waiting time distribution, $\psi(\tau)$, the simulation did not produce satisfactory fits for dextran on homogeneous PS surfaces (the gray line in Figure 3). Importantly, this scenario indicated that the difference in step-size distribution could not be described by simply varying the waiting time distribution.

In summary, we designed high-throughput single-molecule tracking measurements to study polymer dynamics on either chemically homogeneous or nanopatterned surfaces with chemically distinct domains, where polymers were essentially excluded from the low-affinity domains, eliminating the possibility of significant continuous (i.e., nonhopping) diffusion. We found that the step-size distributions on homogeneous surfaces exhibited an additional diffusive mode that was missing on nanopatterned surfaces, which was attributed to the presence of a slow continuous mode due to 2D in-plane diffusion. Kinetic Monte Carlo simulations were performed to test this model, and using an in-plane diffusion coefficient of $D_{2D} = 0.20\ \mu\text{m}^2/\text{s}$, we found good agreement between simulations and experimental data on both chemically homogeneous and nanopatterned surfaces. These findings help resolve the discrepancy between previous studies using disparate methods and provide renewed insight into polymer transport on solid/liquid interfaces, which are more complicated than conventional wisdom suggests. $^{55-57}$

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acsmacrolett.6b00183.

Experimental and simulation details and additional supporting figures (PDF).

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: daniel.schwartz@colorado.edu.

### Author Contributions
†These authors contributed equally to this manuscript (D.W. and H.-Y.C.).

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This work was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, under Award #DE-SC0001854.

## REFERENCES
(1) O'Shaughnessy, B.; Vavylonis, D. *Europhys. Lett.* **1999**, 45, 638−644.
(2) Kenna, J.; Major, G.; Williams, R. J. *Immunol. Methods* **1985**, 85, 409−419.
(3) De Gennes, P.-G. *Scaling Concepts in Polymer Physics*; Cornell University Press: Ithaca, NY, 1979; pp 33−35.
(4) Zaid, I. M.; Lomholt, M. A.; Metzler, R. *Biophys. J.* **2009**, 97, 710−721.
(5) Palyulin, V. V.; Chechkin, A. V.; Metzler, R. *Proc. Natl. Acad. Sci. U. S. A.* **2014**, 111, 2931−2936.
(6) Cai, Y.; Schwartz, D. K. *ACS Appl. Mater. Interfaces* **2016**, 8, 511−520.
(7) Montiel, D.; Yang, H. *Laser Photonics Rev.* **2010**, 4, 374−385.
(8) Meijering, E.; Dzyubachyk, O.; Smal, I. *Methods Enzymol.* **2012**, 504, 183−200.
(9) Sukhishvili, S. A.; Chen, Y.; Muller, J. D.; Gratton, E.; Schweizer, K. S.; Granick, S. *Nature* **2000**, 406, 146−146.
(10) Wang, W.; Zhang, C.; Wang, S.; Zhao, J. *Macromolecules* **2007**, 40, 9564−9569.
(11) Zhao, J.; Granick, S. *Macromolecules* **2007**, 40, 1243−1247.
(12) Wong, J. S. S.; Hong, L. A.; Bae, S. C.; Granick, S. *Macromolecules* **2011**, 44, 3073−3076.
(13) Cooper, J. T.; Harris, J. M. *Anal. Chem.* **2014**, 86, 7618−7626.
(14) Kastantin, M.; Walder, R.; Schwartz, D. K. *Langmuir* **2012**, 28, 12443−12456.
(15) Casuso, I.; Khao, J.; Chami, M.; Paul-Gilloteaux, P.; Husain, M.; Duneau, J. P.; Stahlberg, H.; Sturgis, J. N.; Scheuring, S. *Nat. Nanotechnol.* **2012**, 7, 525−529.
(16) Hansen, R. L.; Harris, J. M. *Anal. Chem.* **1995**, 67, 492−498.
(17) Xu, L.; Kozlovskaya, V.; Kharlampieva, E.; Ankner, J. F.; Sukhishvili, S. A. *ACS Macro Lett.* **2012**, 1, 127−130.
(18) Yu, C.; Guan, J.; Chen, K.; Bae, S. C.; Granick, S. *ACS Nano* **2013**, 7, 9735−9742.
(19) Fytas, G.; Anastasiadis, S. H.; Seghrouchni, R.; Vlassopoulos, D.; Li, J. B.; Factor, B. J.; Theobald, W.; Toprakcioglu, C. *Science* **1996**, 274, 2041−2044.
(20) Wang, S. Q.; Jing, B. X.; Zhu, Y. X. *RSC Adv.* **2012**, 2, 3835−3843.
(21) Sanchez, H.; Suzuki, Y.; Yokokawa, M.; Takeyasu, K.; Wyman, C. *Integr. Biol.* **2011**, 3, 1127−1134.
(22) Wang, D. P.; He, C. L.; Stoykovich, M. P.; Schwartz, D. K. *ACS Nano* **2015**, 9, 1656−1664.
(23) Sancho, J.; Lacasta, A.; Lindenberg, K.; Sokolov, I.; Romero, A. *Phys. Rev. Lett.* **2004**, 92, 250601.
(24) Lubelski, A.; Sokolov, I.; Klafter, J. *Phys. Rev. Lett.* **2008**, 100, 250602.
(25) Burov, S.; Jeon, J. H.; Metzler, R.; Barkai, E. *Phys. Chem. Chem. Phys.* **2011**, 13, 1800−1812.
(26) Skaug, M. J.; Mabry, J.; Schwartz, D. K. *Phys. Rev. Lett.* **2013**, 110, 256101.
(27) Chin, H. Y.; Wang, D. P.; Schwartz, D. K. *Macromolecules* **2015**, 48, 4562−4571.

(28) Tierno, P.; Johansen, T.; Fischer, T. *Phys. Rev. Lett.* **2007**, 99, 038303.

(29) Tierno, P.; Sagués, F.; Johansen, T. H.; Sokolov, I. M. *Phys. Rev. Lett.* **2012**, 109, 070601.

(30) He, K.; Khorasani, F. B.; Retterer, S. T.; Thomas, D. K.; Conrad, J. C.; Krishnamoorti, R. *ACS Nano* **2013**, 7, 5122−5130.

(31) He, K.; Retterer, S. T.; Strijanto, B. R.; Conrad, J. C.; Krishnamoorti, R. *ACS Nano* **2014**, 8, 4221−4227.

(32) Skaug, M. J.; Lacasta, A. M.; Ramirez-Piscina, L.; Sancho, J. M.; Lindenberg, K.; Schwartz, D. K. *Soft Matter* **2014**, 10, 753−759.

(33) Mabry, J. N.; Kastantin, M.; Schwartz, D. K. *ACS Nano* **2015**, 9, 7237−7247.

(34) Kisley, L.; Brunetti, R.; Tauzin, L. J.; Shuang, B.; Yi, X. Y.; Kirkeminde, A. W.; Higgins, D. A.; Weiss, S.; Landes, C. F. *ACS Nano* **2015**, 9, 9158−9166.

(35) Bates, F. S.; Fredrickson, G. H. *Annu. Rev. Phys. Chem.* **1990**, 41, 525−557.

(36) Han, E.; Stuen, K. O.; Leolukman, M.; Liu, C. C.; Nealey, P. F.; Gopalan, P. *Macromolecules* **2009**, 42, 4896−4901.

(37) Bang, J.; Jeong, U.; Ryu, D. Y.; Russell, T. P.; Hawker, C. J. *Adv. Mater.* **2009**, 21, 4769−4792.

(38) Campbell, I. P.; Lau, G. J.; Feaver, J. L.; Stoykovich, M. P. *Macromolecules* **2012**, 45, 1587−1594.

(39) Diederichsen, K. M.; Brow, R. R.; Stoykovich, M. P. *ACS Nano* **2015**, 9, 2465−2476.

(40) Armstrong, J.; Wenby, R.; Meiselman, H.; Fisher, T. *Biophys. J.* **2004**, 87, 4259−4270.

(41) Walder, R.; Kastantin, M.; Schwartz, D. K. *Analyst* **2012**, 137, 2987−2996.

(42) Schulz, J. H.; Barkai, E.; Metzler, R. *Phys. Rev. Lett.* **2013**, 110, 020602.

(43) Schulz, J. H.; Barkai, E.; Metzler, R. *Phys. Rev. X* **2014**, 4, 011028.

(44) Tauzin, L. J.; Shuang, B.; Kisley, L.; Mansur, A. P.; Chen, J. X.; de Leon, A.; Advincula, R. C.; Landes, C. F. *Langmuir* **2014**, 30, 8391−8399.

(45) Wang, D. P.; Hu, R. F.; Skaug, M. J.; Schwartz, D. K. *J. Phys. Chem. Lett.* **2015**, 6, 54−59.

(46) Bychuk, O. V.; O'Shaughnessy, B. *J. Chem. Phys.* **1994**, 101, 772−780.

(47) Bychuk, O.; O'Shaughnessy, B. *Phys. Rev. Lett.* **1995**, 74, 1795−1798.

(48) Chechkin, A. V.; Zaid, I. M.; Lomholt, M. A.; Sokolov, I. M.; Metzler, R. *J. Chem. Phys.* **2011**, 134, 204116.

(49) Bénichou, O.; Loverdo, C.; Moreau, M.; Voituriez, R. *Rev. Mod. Phys.* **2011**, 83, 81−129.

(50) Klafter, J.; Sokolov, I. M. *First Steps in Random Walks: From Tools to Applications*; Oxford University Press: Oxford, U.K., 2011; pp 36−51.

(51) Chechkin, A. V.; Zaid, I. M.; Lomholt, M. A.; Sokolov, I. M.; Metzler, R. *Phys. Rev. E* **2012**, 86, 041101.

(52) Weltz, J. S.; Schwartz, D. K.; Kaar, J. L. *ACS Nano* **2016**, 10, 730−738.

(53) Mabry, J. N.; Schwartz, D. K. *J. Phys. Chem. Lett.* **2015**, 6, 2065−2069.

(54) Netz, R. R.; Andelman, D. *Phys. Rep.* **2003**, 380, 1−95.

(55) O'Shaughnessy, B.; Vavylonis, D. *J. Phys.: Condens. Matter* **2005**, 17, R63−R99.

(56) Bénichou, O.; Grebenkov, D.; Levitz, P.; Loverdo, C.; Voituriez, R. *Phys. Rev. Lett.* **2010**, 105, 150606.

(57) Guérin, T.; Bénichou, O.; Voituriez, R. *Nat. Chem.* **2012**, 4, 568−573.