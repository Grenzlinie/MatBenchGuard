
# Spin precession in disordered systems: Anomalous relaxation due to heavy tailed field distributions

Falk Scheffler \( ^{(1)} \)  and Philipp Maass \( ^{(1,2)} \) 

(1) Fachbereich Physik, Universität Konstanz, 78457 Konstanz, Germany

(2) Institut für Physik, TU Ilmenau, 98684 Ilmenau, Germany

(October 26, 2001)

We investigate spin precession in the presence of randomly distributed field sources. Their fields  \( h_{i} \)  reorient by thermally activated transitions and decrease as  \( r^{-\mu} \)  with the distance from the spin probe. Based on analytical calculations and scaling arguments we find that the polarization decay of a spin ensemble exhibits a rich behavior characterized by stretched exponentials and power laws with exponents depending on  \( \mu \)  and the dimension d. The anomalous relaxation laws result from heavy tailed local field distributions and are verified by computer simulations. Implications for experiments are pointed out.

PACS numbers: 76.75.+i, 76.20.+q, 76.60.Es

Many experimental probes rely on a precession of a spin S in an external field H.

 \[ \frac{d\mathbf{S}}{d t}=\mathbf{S}\times\mathbf{H}. \quad (1) \] 

Examples are nuclear and electron magnetic resonance (NMR, ESR), muon spin relaxation ( \( \mu \) SR),  \( \beta \) NMR, and quantum optical measurements, where transitions in two-level systems can effectively be described by an equation of type (1). In disordered systems the field H generally exhibits both spatial and temporal fluctuations and the relaxation of an initially polarized spin ensemble is of interest. While traditionally this relaxation dynamics is studied for Gaussian stochastic processes  \( \mathbf{H}(t) \)  [1,2], more complex stochastic processes became of interest recently (see e.g. [3]). Here we will focus on systems, where the second moment  \( \langle H^{2}\rangle \)  of the field distribution diverges. These situations occur, when the field  \( H = \sum_{i} h_{i} \)  results from randomly distributed sources i in d dimensions with a spatial field dependence  \( h_{i} \sim r_{i}^{-\mu} \) ,  \( \mu > d/2 \)  (for dipolar fields, in particular,  \( \mu = 3 \) ).

As an example of practical importance we focus on  \( \mu \) SR in disordered systems of single domain ferromagnetic particles [4,5]. In these systems the clusters perform thermally activated transitions between certain easy magnetization directions with a rate  \( \nu \) , which lead to fluctuations of the magnetic field at the muon site. We will show in this Letter that these fluctuations give rise to a rich anomalous relaxation behavior due to the fact that the random spatial distribution of the cluster moments leads to Lévy type local field distributions. Dependent on how the reorientation rate  \( \nu \)  compares with the characteristic width W of the field distribution and dependent on the number of possible orientations of the cluster moments, we find very different relaxation scenarios. The long time relaxation is given by either power laws or stretched exponentials, where the exponents depend on both  \( \mu \)  and d. The slow relaxations occur even in the absence of cluster interaction effects and in this respect should be contrasted to the relaxation found in spin glass systems [3] or related disordered systems [6] with strongly interacting components.

To be specific, we consider the following model. We place a spin S at the origin of a d-dimensional system that contains randomly oriented point-like clusters with number density n at random positions. A cluster with moment m and position r is assumed to induce a field contribution  \( h = m/r^{\mu} \)  at the probe site. Each moment m changes its orientation to a set of possible other orientations with the rate  \( \nu \) . In particular we study two situations: In the first case only the directions m and -m are possible (uniaxial case), while in the second case there are four additional orientations perpendicular to m corresponding to a cubic symmetry (multiaxial case). Initially the spin is polarized in the z-direction,  \( \mathbf{S} = (0, 0, 1) \) . The task is to solve eq. (1) for a given cluster configuration and a certain realization of the cluster reorientation process and to average this solution over all possible realizations. By finally averaging over all cluster configurations we obtain the spin polarization  \( \langle S_{z}(t) \rangle \)  at time t as measured in experiment. In the following we will discuss the relaxation behavior for the generic situation  \( \mu > d/2 \)  [7].

We start out by focusing on the time regime  \( t \ll \nu^{-1} \) , where the field H can be viewed to be static, and the solution of eq. (1) reads  \(  S_{z}(t) = (H_{z}^{2}/H^{2}) + [1 - (H_{z}^{'2}/H^{2})] \cos(Ht)  \) . By an exact calculation we obtain for the probability density  \(  \psi(\mathbf{H})  \)  of the local field H

 \[ \psi(\mathbf{H})=\frac{1}{2\pi W^{2}H}\operatorname{R e}L_{\frac{d}{n},0}^{\prime}\left(\frac{H}{W}\right), \quad (2) \] 

where  \( ReL_{\alpha,0}^{\prime}(u) \)  denotes the real part of the derivative of the Lévy stable law  \( L_{\alpha,0}(u)=(2\pi)^{-1}\int dk\exp(-iku-|u|^{\alpha}) \)  to the index  \( (\alpha,0) \)  (see e.g. [8]); the characteristic width  \( W=C_{W}mn^{\mu/d} \)  is given by the field associated with the mean distance  \( n^{-1/d} \)  of the clusters times a constant [9]. For large H,  \( 4\pi H^{2}\psi(\mathbf{H})\sim C_{\psi}W^{-1}(H/W)^{-1-d/\mu} \) , implying that  \( \langle H^{2}\rangle \)  does not exist. Averaging  \( S_{z}(t) \)  over  \( \psi(\mathbf{H}) \)  eventually yields
 
![](./images/867771235751166842_1.jpg)

![](./images/867771235751166842_2.jpg)

FIG. 1. Spin polarization  \( \langle S_{z}(t)\rangle \)  as a function of  \( \nu t \)  in the slowly fluctuating case  \( (\nu/W=10^{-3}) \)  for (a) multiaxial and (b) uniaxial cluster moments, and several  \( \mu \)  and d. The symbols refer to the simulations and their assignment is the same in both figures. The dashed lines refer to the exact result (3), while the solid lines are fits according to the long-time behaviors (4,7). The inset in (a) shows, on a semi-logarithmic scale, the exponential long-time relaxation of  \( \langle S_{z}(t)\rangle \)  vs.  \( \nu t \)  that is almost independent of d and  \( \mu \)  (the solid line is drawn as a guide for the eye). The inset in (b) demonstrates the scaling (6) for 4 different radii  \( r_{1}\ll n^{-1/d} \) ,  \( r_{1}=1.0\;(+) \) ,  \( 1.5\;(×) \) ,  \( 2.0\;(*) \) , and  \( 2.5\;(○) \)  in the case  \( \mu=d=3 \) , n=0.01.

 \[ \left\langle S_{z}(t)\right\rangle=\frac{1}{3}+\frac{2}{3}\left[1-\frac{d}{\mu}(W t)^{d/\mu}\right]\exp\left[-(W t)^{d/\pi}\right]. \quad (3) \] 

For  \( d = \mu \) , i.e. in particular for dipolar fields in d = 3, one recovers the Lorentzian Kubo–Toyabe function [1]. As shown in Fig. 1 for different  \( \mu \)  and d, the results from our simulations agree with eq. (3) for  \( \nu t \ll 1 \) . Laws of type (3) have been used in the literature to describe anomalous  \( \mu \) SR line-shapes with  \( d/\mu \neq 1 \) , 2 that neither follow a Lorentzian ( \( d/\mu = 1 \) ) nor Gaussian ( \( d/\mu \approx 2 \) ) behavior (see e.g. [10]). We note, however, that (3) is an exact result and should not be confused with an effective “power Kubo–Toyabe function” [11] that serves as a fitting function.

In the dynamic regime  \( t \gg \nu^{-1} \)  we distinguish between the two cases of slowly or rapidly fluctuating cluster moments, where  \( \nu \ll W \)  or  \( \nu \gg W \) , respectively. In both cases we employ scaling arguments to derive the typical decay rates  \( \Gamma \)  of the spin polarisation. To tackle the problem of averaging over spatial cluster configurations, we consider subensembles of configurations that are specified by fixing the distances of the clusters closest to the spin probe. This concept is motivated by the hierarchy implied by the Lévy statistics, which for the field distribution (2) means that the nth nearest cluster gives a contribution of order  \( n^{\mu/d} \)  times smaller than the closest cluster (see e.g. [12]).

Let us begin with the case  \( \nu\ll W \)  of slowly fluctuating cluster moments, where for the relevant cluster configurations the field H has a magnitude  \( H\gg\nu \)  (other configurations have an exponentially small weight). In a time interval of order  \( \nu^{-1} \)  then, the spin precesses many periods around the local field, whereby  \( S_{z}(t) \)  oscillates around a mean value  \( \bar{S}_{z}(t) \) . The changes of  \( \bar{S}_{\bar{z}}(t) \)  averaged over many realizations of the cluster dynamics determine the decay of spin polarization.
In the multiaxial case, significant changes of H, which occur in a time of order  \( \nu^{-1} \) , alter the axis of precession and  \( \bar{S}_{z}(t) \)  relaxes with a rate proportional to  \( \nu \) . Hence we expect a simple exponential decay

 \[ \langle S_{z}(t)\rangle\sim\exp(-c s t.\nu t), \quad (4) \] 

which is confirmed by our simulations shown in Fig. 1a.

The uniaxial case is more subtle. To see this, we decompose the field H into the contribution  \( h_{1} = m/r_{1}^{\mu} \)  from the nearest cluster at distance  \( r_{1} \)  and the contribution  \( H_{1} \)  from the other clusters,  \( H = h_{1} + H_{1} \) . In the subensemble of all cluster configurations with given  \( r_{1} \) , the variance of  \( H_{1} \)  is

 \[ \langle H_{1}^{2}|r_{1}\rangle=C_{H}h_{1}^{2}\left(\frac{h_{1}}{W}\right)^{-d/\mu}. \] 

For  \( r_{1} \gg n^{-1/d} \) ,  \( h_{1}/W \ll 1 \) , and  \( H_{1} \)  dominates over  \( h_{1} \) . Hence one encounters the same physical situation as in the multiaxial case. For small  \( r_{1} \ll n^{-1/d} \) , however,  \( h_{1} \)  is dominant, so that changes  \( h_{1 \to -h_{1}} \)  essentially revert the direction of precession and leave  \( \bar{S}_{z}(t) \)  unchanged.

In this situation of small  \( r_{1} \ll n^{-1/d} \)  the presence of the contribution  \( H_{1} \)  causes the axis of the field H (irrespective of its direction) to wobble around the  \( \pm h_{1} \) -axis with the rate  \( \nu \)  and an angular amplitude of order  \( H_{1}/h_{1} \) . The wobbling motion together with the much faster precession leads to a diffusive type of motion of  \( \bar{S}_{z}(t) \)  with a diffusion rate  \( \Gamma \sim (H_{1}/h_{1})^{2}\nu \) .

To extract the asymptotic relaxation of the spin polarization we consider the subensemble of all cluster configurations with fixed distances  \( r_{1} \)  and  \( r_{2} \)  of the nearest and second nearest cluster to the spin probe. In the configurations of this subensemble we can decompose  \( H_{1} \)  into  \( h_{2} \)  and  \( H_{2} \) , where  \( h_{2}=m/r_{2}^{\mu} \)  and  \( \langle H_{2}^{2}|r_{2}\rangle \)  satisfies (5) with  \( h_{1} \)  replaced by  \( h_{2} \) . Accordingly, for
 

 \( r_{1}<r_{2}\lesssim n^{-1/d},\ H_{1}^{2}\sim m^{2}/r_{2}^{2\mu} \)  and  \( \Gamma\equiv\Gamma(r_{1},r_{2})\propto(r_{1}/r_{2})^{2\mu}\nu \) , while for  \( r_{2}\gtrsim n^{-1/d}, H_{1}^{2}\sim W^{d/\mu}(m/r_{2}^{\mu})^{2-d/\mu} \)  and  \( \Gamma(r_{1},r_{2})\propto r_{1}^{2\mu}W^{d/\mu}(m/r_{2}^{\mu})^{2-d/\mu}\nu \) . Writing  \( \langle S_{z}(t)|r_{1},r_{2}\rangle\sim\exp[-\Gamma(r_{1},r_{ 2})t] \)  in the subensemble with given  \( r_{1} \)  and  \( r_{2} \) , we can average over the probability density  \( \phi_{2}(r_{2}|r_{1})=S_{d n r_{1}^{d-1}}\exp[-V_{d n}(r_{2}^{d}-r_{1}^{d})] \)  of  \( r_{2} \)  ( \( r_{1}\leq r_{2}<\infty \) ) to obtain [13]

 \[ \left\langle S_{z}(t)|r_{1}\right\rangle\sim\exp\left\{V_{d n r_{1}^{d-1}}c s t.\left[(n^{1/d}r_{1})^{2\mu}\nu t\right]^{d/2\mu}\right\} \quad (6) \] 

for  \( \nu t \gg 1 \)  (and  \( r_{1} \ll n^{-1/d} \) ). We have verified this prediction for various  \( \mu \)  and d by our simulations. One example (for  \( \mu = d = 3 \) ) is shown in the inset of Fig. 1b.

Final averaging over the probability density  \( \phi_{1}(r_{1}) = S_{d}nr_{1}^{d-1}\exp[-V_{d}nr_{i}^{d}] \)  of  \( r_{1} \)  yields

 \[ \langle S_{z}(t)\rangle\sim(\nu t)^{-d/2\mu}. \quad (7) \] 

This slow power law decay is in marked contrast to the exponential decay in the multiaxial case and it is verified in Fig. 1b by our simulations.

Next we discuss the case  \( \nu\gg W \)  of rapidly fluctuating cluster moments. The field H in the relevant cluster configurations now has a magnitude  \( H\ll\nu \)  and the spin rotates only by a small angle in a time interval of order  \( \nu^{-1} \) . This means that the concept of a mean value  \( \bar{S}_{z}(t) \)  is not useful any longer, since the phase of the precession matters. Reorientations of  \( h_{1} \)  are effective for the spin relaxation both in the presence of uniaxial and multiaxial cluster moments.

The small angular changes of the spin lead again to a diffusive type of motion of  \( S_{z}(t) \) . In time  \( \nu^{-1} \)  the angular change is of order  \( H/\nu \)  and the corresponding diffusion rate  \( \Gamma \sim (H/\nu)^{2}\nu \) . Decomposing the field  \( H = h_{1} + H_{1} \)  as before, and taking into account the dominant contributions we thus find  \( \Gamma \equiv \Gamma(r_{1}) \propto \nu^{-1}m^{2}/r_{1}^{2\mu} \)  for  \( r_{1} \lesssim n^{-1/d} \)  and  \( \Gamma(r_{1}) \propto \nu^{-1}W^{d/\mu}(m/r_{1}^{t\mu})^{2-d/\mu} \)  for  \( r_{1} \gtrsim n^{-1/d} \)  [cf. eq. (5)]. We then write  \( \langle S_{z}(t)|r_{1}\rangle \sim \exp[-\Gamma(r_{1})t] \)  for  \( \nu t \gg 1 \)  and  \( r_{1} \gg (m/\nu)^{1/\mu} \)  (for  \( r_{1} \ll (m/\nu)^{1/\mu} \) ,  \( h_{1} \gg \nu \) , i.e. one encounters a situation corresponding to the case of slowly fluctuating cluster moments). This exponential decay of  \( \langle S_{z}(t)|r_{1}\rangle \)  is demonstrated in the inset of Fig. 2 for  \( d = \mu = 3 \)  in the regime  \( r_{1} > n^{-1/d} \) . By averaging over  \( r_{1} \)  we finally obtain

 \[ \langle S_{z}(t)\rangle\sim\exp\left[-c s t.\left(\nu^{-1}W^{2}t\right)^{d/2\mu}\right]. \quad (8) \] 

To perform the average we have used a saddle point approximation, where analogous comments apply as given in [13]. Figure 2 confirms both the scaling with  \( (W^{2}t/\nu) \)  and the stretched exponential decay for the same  \( \mu \)  and d values as in Fig. 1. In the uniaxial case the stretched exponential decay (8) will, at long times, be masked by the much slower power law decay (7) that stems from the rare configurations with  \( h_{1}=m/r_{1}^{\mu}\gg\nu \) .

![](./images/867771235751166842_3.jpg)

FIG. 2. Spin polarization  \( \langle S_{z}(t)\rangle \)  as a function of  \( W^{2}t/\nu \)  in the case of rapidly fluctuating cluster moments  \( [\nu/W=10 \)  (☐), 50 (+), and 100 (×) for  \( d=\mu=3 \) , and  \( \nu/W=10 \)  for the three other combinations of d and  \( \mu \) ]. Data points refer to the simulations and the solid lines are fits according to eq. (8). The inset shows the exponential decay of  \( \langle S_{z}(t)|r_{1}\rangle \)  and the scaling as discussed in the text for 4 different radii  \( r_{1}\gtrsim n^{-1/d} \) ,  \( r_{1}=6.5 \)  (+),  \( 7.0 \)  (×),  \( 7,5 \)  (*), and  \( 8.0 \)  (o) in the case  \( \mu=d=3 \) , and n=0.01 (the solid line is drawn as a guide for the eye).

In summary we have shown that spin precession in the presence of randomly distributed and fluctuating field sources leads to an anomalous relaxation of an initially polarized spin probe, which is characterized by stretched exponentials [eqs. (3,8)] or power laws [eq. (7)]. The deviation from a simple exponential decay are caused by Lévy type local field distributions [eq. (2)]. These render a treatment in terms of Gaussian processes impossible but allowed us to perform an analysis based on subensembles of cluster configurations that are defined with respect to the most dominant contributions to the local field, i.e. the field sources closest to the spin probe.

It is important to stress that a simple mean field type description of the relaxation process would fail, as it was already pointed out by Uemura et al. [2] in the case  \( \mu=d=3 \) . In such a mean field description one might employ a “strong collision approximation” [14], where the field H at the probe site is drawn anew from (2) with the rate  \( \nu \)  (thereby neglecting the fluctuations in the spatial cluster configurations). By scaling arguments similar to those outlined above one can show that this approach leads, for  \( t\gg\nu^{-1} \) , to an exponential relaxation  \( \langle S_{z}(t)\rangle\sim\exp(-\Gamma_{\mathrm{mf}}t) \)  both in the cases of slowly and rapidly fluctuating cluster moments and irrespective of whether the clusters posses only one easy axis or more. For  \( \nu\ll W \) , one obtains  \( \Gamma_{mf}\propto\nu \) , while for  \( \nu\gg W \) ,  \( \Gamma_{mf}\propto\nu(W/\nu)^{d/\mu} \)  [15].

We restricted our treatment here to point clusters with unique moment m and neglected interactions between the moments. As long as the cluster sizes are much smaller than the mean distance  \( n^{-1/d} \) , crossover effects to a Debye like relaxation behavior typical for Gaussian
 

processes should be of minor importance. A broad distribution of cluster sizes, however, may require a refined analysis in the dynamic regime (in the static regime the results remain unchanged except that m in the width W has to be replaced by its average value). To capture the dominant contributions to the local field and to take into account the variation in the jump frequencies (associated with changes in the anisotropy energy), it can be necessary to define the subensembles with respect to both the distance of the clusters nearest to the spin probe and the size of the clusters. Effects due to dispersion in the jump frequencies have been observed, for example, by  \( \mu \) SR in colossal magnetoresistive manganites [16]. Nevertheless, the basic scaling arguments presented in this work would still be applicable and an extension to systems of clusters with differing moments should be straightforward.

Interactions between the cluster moments at high temperatures T can be accounted for by a temperature dependent width  \( W = W(T) \)  in (2) (for an approximate calculation in  \( \mu = d = 3 \) , see [17]). At low temperatures T by contrast, the cluster dynamics cannot be described any longer by a Poisson process with rate  \( \nu \)  (for dipolar systems in d = 2, 3 this occurs for  \( T \lesssim 0.5 m^{2} n^{d/3} \) , see [18,19]). In this low-temperature regime the problem becomes more difficult and the relaxation laws (7,8) may no longer hold true. A non-Poissonian cluster dynamics has recently been encountered in a spin glass also [3].

Having mentioned these limits of our findings, we hope that our work will stimulate further research on the challenging problem of spin precession in disordered systems. Our scaling methods should give deeper insight into the spin relaxation in disordered systems and may be extended to describe  \( \mu \) SR (or  \( \beta \) NMR) in other complex systems, as e.g. spin glasses, structural glasses, amorphous magnets or disordered superconductors.

We should like to thank W. Dieterich and Ch. Nieder-mayer for discussions and gratefully acknowledge financial support by the Sonderforschungsbereich 513 and the Heisenberg program (P.M.) of the Deutsche Forschungsgemeinschaft.

[1] R. Kubo and T. Toyabe, in Magnetic Resonance and Relaxation, edited by R. Blinc (North Holland, Amsterdam, 1967).

[2] Y. J. Uemura, T. Yamazaki, D. R. Harshman, M. Senba, and E. J. Ansaldo, Phys. Rev. B 31, 546 (1985).

[3] A. Keren, P. Mendels, I. A. Campbell, and J. Lord, Phys. Rev. Lett. 77, 1386 (1996); A. Keren, G. Bazalitsky, I. Campbell, and J. S. Lord, Phys. Rev. B 64, 054403 (2001).

[4] R. I. Bewley and R. Cywinski, Phys. Rev. B 58, 11544 (1998).

[5] T. J. Jackson, C. Binns, E. M. Forgan, E. Morenzoni, Ch. Niedermayer, H. Glückler, A. Hofer, H. Luetkens,

T. Prokscha, T. M. Riseman, A. Schatz, M. Birke, J. Litterst, G. Schatz, and H. P. Weber, J. Phys.: Condens. Matter 12, 1399 (2000).

[6] J. van Lierop, D. H. Ryan, Phys. Rev. Lett. 86, 4390 (2001).

[7] For  \( \mu < d/2 \) ,  \( \langle H^{2}\rangle \)  is finite but vanishes in the thermodynamic limit. This yields a Debye like relaxation typical for Gaussian processes but the characteristic relaxation times would depend on the system size.

[8] J.-P. Bouchaud and A. Georges, Phys. Rep. 195, 128 (1990).

[9] Explicit known constants referred to in the text are  \( C_{W}^{d/\mu}=\mu^{-1}S_{d}\int_{0}^{\infty}du\,u^{-1-d/\mu}(1-\sin u/u) \) ,  \( C_{\psi}=2\pi^{-1}\Gamma(2+d/\mu)\sin(\pi d/2\mu) \) ,  \( C_{H}=S_{d}/[(2\mu-d)C_{W}^{d/\mu}] \) , where  \( S_{d}=2\pi^{d/2}/\Gamma(d/2) \)  and  \( V_{d}=S_{d}/d \)  are the surface and volume of the d-dimensional unit sphere, respectively.

[10] W. D. Wu, A. Keren, L. P. Le, G. M. Luke, B. J. Sternlieb, Y. J. Uemura, Phys. Rev. Lett. 72, 3722 (1994).

[11] M. R. Crook, R. Cywinski, J. Phys.: Condens. Matter 9, 1149 (1997).

[12] P. Embrechts, C. Klüppelberg, and Th. Mikosch, Modelling Extremal Events (Springer, Berlin, 1997).

[13] The exponential ansatz  \( \langle S_{z}(t)|r_{1},r_{2}\rangle\sim\exp[-\Gamma(r_{1},r_{20})t] \)  follows from the picture that the relaxation is due to a diffusive motion of  \( \bar{S}_{z}(t) \)  in an interval  \( 0\leq\bar{S}_{z}(t)\leq1 \)  with a reflecting boundary at  \( \bar{S}_{z}=1 \)  and an absorbing boundary at  \( \bar{S}_{z}=0 \) . The averaging over  \( r_{2} \)  gives two contributions, (i)  \( \int_{r_{1}}^{r_{1-d}}dr_{2}\phi_{2}(r_{2}|r_{1})\exp[-cst.(r_{1}/r_{2})^{2\mu}\nu t] \)  that decreases exponentially with time for large t, and (ii)  \( \int_{\infty-1/d}^{\infty}dr_{2}\phi_{2}(r_{2}|r_{1})\exp[-cst.(r_{1}^{2\mu}W^{d/\mu}(m/r_{2}^{d})^{2-d/\mu}\nu t] \)  that yields (6) when employing a saddle point approximation (neglecting power laws in t). For the saddle point approximation to be applicable for all  \( \mu>d/2 \)  one should first do a partial integration and then change the integration variable from  \( r_{2} \)  to  \( 1/r_{2} \) .

[14] R. Kubo, J. Phys. Soc. Jpn. 9, 935 (1954).

[15] A refined ansatz based on the strong-collision approximation has been followed by Uemura et al. [2] for  \( \mu = d = 3 \)  in order to take into account the fluctuations in the spatial cluster configurations. In their approach the local field fluctuations in a given configuration is assumed to be Gaussian distributed but with a configuration dependent standard deviation  \( \Delta \) . The distribution  \( \rho(\Delta) \)  is determined self-consistently by requiring that the superposition of the Gaussians yields the correct Cauchy field distribution of the cartesian components  \( H_{j} \)  of the local field [as it follows from eq. (2) for  \( \mu = d = 3 \) ].

[16] R. H. Heffner, J. E. Sonier, D. E. MacLaughlin, G. J. Nieuwenhuys, G. M. Luke, Y. J. Uemura, W. Ratcliff II, S-W. Cheong, and G. Balakrishnan, Phys. Rev. B 63, 094408 (2001).

[17] C. Held and M. W. Klein, Phys. Rev. Lett. 35, 1783 (1975).

[18] P. Pendzig and W. Dieterich, Solid State Ionics 105, 209 (1998).

[19] B. Rinn, W. Dieterich, and P. Maass, Phil. Mag. B 77, 1283 (1998).
 
