
# Liquid-vapour phase behaviour of a symmetrical binary fluid mixture

N. B. Wilding

Department of Physics and Astronomy, The University of Edinburgh, Edinburgh EH9 3JZ, U.K.

F. Schmid

Institut für Physik, Johannes Gutenberg Universität, Staudinger Weg 7, D-55099 Mainz, Germany.

P. Nielaba

Institut für Physik, Johannes Gutenberg Universität,
Staudinger Weg 7, D-55099 Mainz, Germany.
and Institut für Theoretische Physik, Universität des Saarlands,
Postfach 151150, D-66041 Saarbrücken, Germany.

Using Monte-Carlo simulation and mean field calculations, we study the liquid-vapour phase diagram of a square well binary fluid mixture as a function of a parameter  \( \delta \)  measuring the relative strength of interactions between particles of dissimilar and similar species. The results reveal a rich variety of liquid-vapour coexistence behaviour as  \( \delta \)  is tuned. Specifically, we uncover critical end point behaviour, a triple point involving a vapour and two liquids of different density, and tricritical behaviour. For a certain range of  \( \delta \) , the mean field calculations also predict a 'hidden' (metastable) liquid-vapour binodal.

PACS numbers 64.60Fr, 64.70.Fx, 05.70.Jk

## I. INTRODUCTION

One of the principal deficiencies in our understanding of liquid mixtures is the nature of the link between the microscopic description of the system and its macroscopic phase behaviour. For simple single component fluids, the phase diagram topology is relatively insensitive to the microscopic properties of the molecules and exhibits (even in systems with strong anisotropies or long ranged interactions) a liquid-vapour first order line terminating at a critical point. By contrast, in binary mixtures, the interplay between the constituent components leads to a wealth of intriguing phase behaviour  \( [1,2] \)  depending on the relative sizes of the molecules and the strengths of their interactions.

Although the various possible phase diagram topologies have been placed into a number of categories  \( [1] \) , it is not well understood (even at the mean field level) precisely which microscopic features are responsible for yielding a given topology. Also unclear is the extent to which critical fluctuations affect the structure of the phase diagram i.e. whether the neglect of correlations in many analytical theories yields qualitatively (as well as quantitatively) incorrect phase diagrams. The task of accurately and reliably deriving the full phase behaviour of a fluid mixture from knowledge of its microscopic interactions therefore remains a great challenge.

Evidently, an accurate description of the phase behaviour of a simple binary fluid model, would provide a useful benchmark against which current and future liquid-state theories could be tested. In the present work, we furnish such a description by means of Monte Carlo simulations of a simple continuum model, the results of which we compare with mean field calculations. For reasons of computational tractability, we consider a symmetrical binary fluid model, i.e. one in which the two pure components A and B are identical and only the interactions between particles of dissimilar species differ. Notwithstanding its simplicity, however, the model turns out to reveal a rich variety of interesting phase behaviour.

## II. BACKGROUND

The phase diagram of a symmetrical binary fluid mixture is spanned by three thermodynamic fields  \( (T,\mu,h) \) , where T is the temperature,  \( \mu \)  is the overall chemical potential coupling to the total density, and h is an ordering field coupling to the relative concentrations of the two fluid components which we assume are allowed to fluctuate. In this work we shall restrict our attention to the phase behaviour in the symmetry plane h=0, i.e. we stipulate that on average the numbers of A and B particles are equal. Additionally we shall assume that similar species interactions are energetically more favourable than dissimilar species interactions. This latter condition provides for a consolute point (critical demixing transition) at some finite temperature  \( T_{c} \) . For temperatures  \( T<T_{c} \) , there is coexistence between an A-rich liquid and a B-rich liquid, while for  \( T>T_{c} \) , the system comprises a homogeneous mix of A and B particles. Precisely at  \( T_{c} \) , the system will be characterised by strong critical concentration fluctuations.
 

between the A-rich and B-rich phases. Such a demixing transition is analogous to that occurring at the critical point of a simple spin- \( \frac{1}{2} \)  Ising model. The difference for an off-lattice fluid, however, is that the demixing temperature depends on the density. Consequently one obtains a critical line of consolute points  \( T_{c}(\rho) \)  [or  \( T_{c}(u) \) ], which is commonly referred to as the ' \( \lambda \)  line'.

In addition to exhibiting consolute critical behaviour, binary fluids can also exhibit liquid-vapour (LV) coexistence, in much the same way as does a single component fluid. It transpires, however, that the LV phase behaviour of binary mixtures is considerable richer than that of simple fluids. This difference is traceable to the additional ingredient of concentration fluctuations, which couple to the density fluctuations and which can radically alter the LV phase behaviour. Since concentration fluctuations are strongest on the  \( \lambda \)  line, one expects that alterations to the LV coexistence behaviour will be greatest where this line approaches the LV coexistence curve.

Perhaps not surprisingly, binary fluids mixtures are not the only fluid systems in which first order phase coexistence behaviour is influenced by the proximity of a critical line. The earliest sightings of such effects appears to have been in analytical studies of various lattice-based fluid models  \( [3-5] \) . Some time later, a detailed Landau theory study of a model for sponge phases in surfactant solution  \( [6] \) , revealed a rich variety of first order phase behaviour as the path of the  \( \lambda \)  line was varied. More recently, similar behaviour was uncovered in extensive mean field and density functional theory investigations of a number of symmetrical continuum fluid models, namely the classical Heisenberg spin fluid  \( [7-10] \) , a dipolar fluid model  \( [11,12] \) , and the van der Waals-Potts fluid  \( [13] \) .

Despite dealing with ostensibly quite distinct models, the gross features of the mean field phase behaviour emerging from these studies appear to be essentially model-independent. This behaviour is illustrated schematically in fig. 1 and involves three possible LV phase diagram topologies, depending on the path of the critical line relative to the LV line. To describe this behaviour we shall employ the language of the symmetrical binary fluid. In so doing, we anticipate the result of sections III and IV, namely that the same scenario is played out in this case too. Of course, to obtain the corresponding behaviour for other systems, eg. the magnetic or dipolar fluids, one need only substitute the appropriate nomenclature e.g. 'mixed fluid' → 'paramagnetic fluid'.

![](./images/867746509511197440_1.jpg)

![](./images/867746509511197440_2.jpg)

![](./images/867746509511197440_3.jpg)

FIG. 1. Schematic representation of the three types of phase diagram for a symmetrical binary fluid mixture in the density-temperature plane, as described in the text. The full curve is the first order liquid-vapour coexistence envelope, while the dashed curve is the  \( \lambda \)  line of critical demixing transitions.

Fig. 1a depicts schematically the mean field phase diagram obtained when the model parameters are chosen such that the  \( \lambda \)  line approaches the first order phase boundary well below the liquid-vapour critical point. In such a situation, the  \( \lambda \)  line intersects the LV line at a critical end point (CEP). At the CEP, a critical liquid coexists with a non-critical vapour. Below the CEP temperature one finds a triple line in which a vapour coexists.
 

with an A-rich liquid and a B-rich liquid. Owing to the symmetry, these two liquids have the same density.

Alternatively, for different model parameters, the  \( \lambda \)  line may intersect the LV line at the liquid-vapour critical point [fig 1c]. Under such conditions, phase coexistence between the vapour and the mixed fluid is preempted by the demixed fluid phase. One then obtains a tricritical point [14,15] in which three phases (a vapour, an A-rich liquid, a B-rich liquid) simultaneously become critical.

The intermediate situation is shown in fig. 1b, and occurs when the  \( \lambda \)  line approaches the LV line at a temperature somewhat (but not greatly) below the liquid-vapour critical temperature. In this case, the phase diagram combines the features of the previous two cases. One finds a triple point in which a vapour coexists with a mixed liquid at intermediate density and a demixed liquid of higher density [16]. Above the triple point temperature, a demixed vapour and a demixed liquid coexist at low and moderate densities, becoming identical above the liquid-vapour critical point. At higher densities, a mixed liquid and the demixed liquid coexist, becoming identical at a tricritical point.

That the scenario described above is generic to a range of apparently distinct fluid models (eg. dipolar, magnetic and binary fluids), is perhaps slightly surprising at first sight. On closer examination, however, it becomes clear that the model differences are only skin-deep. All the systems in which this behaviour has yet been identified, can, in essence, be regarded as fluids in which each particle carries an internal degree of freedom, eg. a spin or dipolar moment. The symmetrical binary fluid model shares this behaviour because the particle species label is analogous to a two-state 'spin' variable.

Notwithstanding the substantial body of analytical evidence supporting the scenario of phase behaviour shown in fig. 1, it must necessarily be regarded as somewhat tentative given the notorious inability of mean field theories to account accurately for critical behaviour below the upper critical dimension. In view of this, independent corroboration by computer simulation is clearly desirable and necessary. In recent times, such studies have indeed started to appear.

The first simulations to study the confluence of a critical demixing line and a first order LV line sought to elucidate the behaviour when the intersection occurs at the LV critical point, i.e. at a tricritical point [cf. fig. 1c]. Investigations of a two-dimensional spin fluid [17] demonstrated that the tricritical point properties are identical to those of the 2D Blume-Capel model, as one might expect on universality grounds. Other studies, this time focusing on the 3D classical Heisenberg fluid  \( [10,18] \)  and spin- \( \frac{1}{2} \)  quantum fluids  \( [19–21] \) , mapped the LV phase envelope and the  \( \lambda \)  line around the tricritical point and compared the results with mean field calculations. Modest agreement was found.

As regards the situation shown in fig. 1a and 1b, there is a still a paucity of simulation data. This is presumable traceable to the practical difficulties associated with studying first order phase coexistence deep within the two phase region. The basic problem is the ergodic (free energy) barrier to sampling both coexisting phases in a single simulation. This barrier arises because the phase space path leading from one pure phase to another necessarily passes through interfacial configurations of large free energy, having a concomitantly low statistical weight. Such configurations occur only very rarely in a standard Monte Carlo (MC) simulation. Fortunately, however, a recently introduced biased-sampling technique known as multicanonical preweighting [22] allows one to negotiate this barrier, and thus obtain accurate estimates of coexistence properties [23]. The efficacy of the method for investigating fluid phase coexistence was first demonstrated in [24]. Very recently, it has also been employed to study critical end point behaviour in a Lennard-Jones binary fluid model [25], [cf. fig. 1a]. In this study, the intersection with the  \( \lambda \)  line was shown to engender a singularity in the first order phase boundary—in accord with earlier theoretical predictions [26]. For the LV phase envelope, this singularity is manifest as a bulge in the liquid branch density (as indicated schematically in fig. 1a).

Thus while fragments of the picture of LV behaviour in symmetrical fluids have been set in place by simulation, much clearly remains to be done before a reliable and comprehensive overview emerges. In particular, no evidence has yet been reported for the existence of the triple point behaviour shown schematically in fig. 1b. There has also been no systematic simulation study of the full range of LV phase behaviour for a single model. Consequently little reliable information exists concerning the manner in which one type of phase diagram evolves into another.

In the present work we have attempted to remedy this situation by performing a systematic MC simulation study of the LV phase behaviour of a binary fluid mixture. The model studied has an interparticle potential of the square-well form:

 \[ \begin{aligned}U(r)&=\infty\quad&r<\sigma\\U(r)&=-J\quad&\sigma\leq r<1.5\sigma\\Ur)&=0\quad&r\geq1.5\sigma\end{aligned} \quad (2.1) \] 

Here r is the particle separation, J is the well depth or interaction strength, and  \( \sigma \)  is the hard-core radius. In general there will be a number of different interaction strengths  \( J^{AA}, J^{BB}, J^{AB} \)  depending on the respective species of the interacting particles. However, in the symmetrical case with which we shall be concerned, one has simply

 \[ \begin{aligned}&J^{AA}(r)=J^{BB}(r)=J(r)\\&J^{AB}(r)=\delta J(r).\\ \end{aligned} \quad (2.2) \] 

The parameter  \( \delta = J_{AB}/J \leq 1 \)  determines the degree to which interactions between dissimilar species are less favourable than similar species interactions. Since  \( \delta \)  is the only free model parameter, it controls the complete range of possible phase behaviour.
 

Using MC simulation we obtain the liquid-vapour phase behaviour of this system for a range of values of  \( \delta \) . The results are compared with explicit mean field model calculations in order to assess the latter's ability to reproduce the actual phase behaviour. Landau theory calculations are also reported which furnish physical insight into the general mechanisms by which the coupling of density and concentration fluctuations engender the various types of observed phase behaviour. Additionally we calculate (both explicitely for our model and within Landau theory) the spinodal lines of the phase diagram. This reveals that for a certain range of  \( \delta \)  there exists a 'hidden' or metastable binodal, the presence of which is expected to have implications for the system dynamics.

The remainder of our paper is organised as follows. In section III we detail the explicit mean-field and general Landau theory calculations for the phase diagram as a function of  \( \delta \) . The Monte Carlo simulation results for the liquid-vapour phase behaviour are presented in section IV. Finally, in section V we conclude by comparing the simulation and mean field results, and discussing prospects for future work.

## III. MEAN-FIELD CALCULATIONS

In this section we present two complementary mean field studies of symmetrical binary mixtures. The first is an explicit investigation of the square-well binary mixture model, also studied by simulation in section IV. The second is a general Landau theory treatment aimed at obtaining physical insight into the origin of the various phase diagram topologies.

## A. Explicit model calculations

Let us consider a binary fluid in which the two particle species A and B interact via the symmetrical square-well potential of equations 2.1 and 2.2. For analysis purposes it will prove useful to decompose this potential into a hard-sphere component plus a short ranged attractive part. To this end we rewrite equation 2.1 as

 \[ U(r)=U_{H S}(r)+J(r), \quad (3.1a) \] 

where

 \[ \begin{aligned}&U_{HS}(r)=\infty\quad&r<\sigma\\&U_{HS}(r)=0\quad&otherwise\\ \end{aligned} \quad (3.1b) \] 

and

 \[ \begin{aligned}&J(r)=\text{—}J\quad&\sigma\leq r\leq1.5\sigma\\&J(r)=\text{—}0\quad&otherwise.\\ \end{aligned} \quad (3.1c) \] 

For a binary fluid, the interaction between two particles depends on their respective species. To deal with this we introduce a two-state species variable  \( s_{i} \)  taking the value  \( s_{i}=1(-1) \)  when the ith particle is of type A (B). The total configurational energy can then be written

 \[ \begin{align*}\Phi^{N}(\{r,s\})&=\sum_{(i<j)}U_{HS}(r_{ij})+\sum_{(i<j)}J(r_{ij})(1+s_{i}s_{j})/2\\&+\sum_{(i<j)}\delta J(r_{ij})(1-s_{i}s_{j})/2.\end{align*} \quad (3.2) \] 

To obtain the liquid-vapour phase envelope and the  \( \lambda \)  line, we adopt an approach similar to that employed in references [27–29,21,17,30]. In the thermodynamic limit, the (Helmholtz) free energy density  \( f(\rho,T) \)  as a function of the number density  \( \rho = N/V \)  and temperature T, is given by:

 \[ f(\rho,T)=\lim_{V\rightarrow\infty}\frac{-1}{\beta V}\ln tr\left[\exp\left(-\beta\Phi^{N}\right)\right]. \quad (3.3) \] 

Now, within the mean field approximation, one assumes an interaction between an A-type particle and an effective field:

 \[ h_{A}=J^{+}+(J^{-}/N)\sum_{i>1}s_{i}=J^{+}+J^{-}m, \quad (3.4) \] 

and an interaction between a B-type particle and an effective field

 \[ h_{B}=J^{+}-(J^{-}/N)\sum_{i>1}s_{i}=J^{+}-J^{-}m. \quad (3.5) \] 

Here,  \( J^{\pm} \)  are effective potentials and  \( m = (N_{A} - N_{B}) / (N_{A} + N_{B}) \) . Since the coordination number in the fluid is density dependent, we make the approximation:

 \[ J^{\pm}=-\rho\int d^{3}r\frac{J^{A A}(r)\pm J^{A B}(r)}{2}g(r), \quad (3.6) \] 

where the fluid correlation function  \(  g(r)  \)  is taken from the Percus-Yevick solution for hard spheres [31].

The mean field configurational energy is then

 \[ \begin{align*}\Phi_{MF}^{N}(\{r,s\})&=U_{HS}(r_{ij})\\&\quad-\frac{1}{4}\sum_{i=1}^{N}\left[h_{A}(1+s_{i})+h_{B}(1-s_{i})\right]\end{align*} \quad (3.7) \] 

from which the free energy at constant T follows as :

 \[ \begin{align*}f_{MF}(\rho)&=\lim_{V\to\infty}\frac{-1}{\beta V}\ln tr\left[\exp\left(-\beta\Phi_{MF}^{N}\right)\right]\\&=f_{HS}(\rho)-\rho\frac{J^{+}}{2}\\&+\min_{m}\left[\frac{J^{-}\rho m^{2}}{2}-\frac{\rho}{\beta}\ln2\cosh\left(\beta J^{-}m\right)\right].\end{align*} \quad (3.8) \] 

Here  \( f_{HS}(\rho) \)  is the free energy of a reference system comprising a hard-sphere single component fluid. The third term of the right hand side of eqn. (3.8) is minimised for
 

 \[ m=\tanh\left[\beta J^{-}m\right]. \quad (3.9) \] 

As  \( f(\rho) \)  is not always a convex function of the density, we take the convex envelope in order to find the coexistence densities for the first order LV transition.

We also wish to obtain the phase diagram in the  \( \mu-T \)  plane. To achieve this one needs to consider the grand potential  \( f(\rho) + \mu\rho \) , with  \( \mu \)  the chemical potential. Minimising this yields the pressure:

 \[ p(\rho,\mu)=\min_{\rho^{\prime}}\left[-f(\rho^{\prime})+\mu\rho^{\prime}\right]. \quad (3.10) \] 

The coexistence chemical potential is then found by demanding equality of both the chemical potential and the pressure in the coexisting phases.

The resulting phase diagrams in the  \( \rho-T \)  plane are shown in fig. 2a-2d, with the  \( \mu-T \)  phase diagrams shown as insets. For large values of  \( \delta < 1 \)  we find a LV coexistence region and a  \( \lambda \)  line at high densities which intersects the LV line at a critical end point. The CEP induces an anomaly or kink in the liquid branch density which is clearly visible in fig. 2a. This anomaly is the mean field remnant of the specific heat-like singularity studied theoretically and computationally in references [26,25]. Because the mean field specific heat exhibits a jump rather than a divergence at criticality, the anomaly takes the form of an abrupt change in the gradient of the liquid branch  \( d\rho_{l}/dT \) . If fluctuations are taken into account, however,  \( d\rho_{l}/dT \)  diverges at the CEP [25].

As  \( \delta \)  is reduced, the CEP anomaly grows until at around  \( \delta = 0.7 \)  a small peak emerges [cf. fig 2b]. The point at which this occurs constitutes a tricritical end point as discussed in subsection III B. On further reduction of  \( \delta \) , the peak develops until the situation shown in fig. 2c is attained. Here the first order coexistence envelope displays a triple point at which a vapour coexists with a mixed liquid at intermediate density and a demixed liquid of higher density. Above the triple point temperature, a vapour and a demixed liquid coexist at low and moderate densities, merging at the liquid-vapour critical point. At higher densities a mixed liquid and the two symmetrical demixed liquids coexist, becoming identical at a tricritical point.

If  \( \delta \)  is reduced further still, one reaches a point (for  \( \delta < 0.605 \) ), at which the triple point temperature equals the LV critical point temperature. Thereafter, the liquid-vapour critical point is lost and only a tricritical point remains, as shown for the case  \( \delta = 0.57 \)  in fig. 2d. No further topological changes in the phase diagram are observed as  \( \delta \)  is reduced to zero.

![](./images/867746509511197440_4.jpg)

![](./images/867746509511197440_5.jpg)

![](./images/867746509511197440_6.jpg)

 
![](./images/867746509511197440_7.jpg)

FIG. 2. Mean field phase diagrams in the  \( \rho-T \)  plane for various  \( \delta \) , as described in the text. (a)  \( \delta=0.72 \) , (b)  \( \delta\approx0.70 \) , (c)  \( \delta=0.65 \) , (d)  \( \delta\approx0.57 \) . The insets show the corresponding phase diagrams in the  \( \mu-T \)  plane. Full lines represent first order phase coexistence and dashed curves represent the  \( \lambda \)  line. The demixed fluid (DF), mixed fluid (MF) and vapour (V) phases are also marked.

Although the liquid-vapour critical point disappears from the equilibrium phase diagram for  \( \delta < 0.605 \) , it is interesting to note that it nevertheless remains in metastable form for some range of  \( \delta \) . This is illustrated in fig. 3a which shows the phase diagram for  \( \delta = 0.57 \)  together with the three spinodals delineating the limits of metastability of the demixed fluid, mixed fluid and vapour (marked  \( S_{1} \) ,  \( S_{2} \)  and  \( S_{3} \) ). Also shown is the 'hidden binodal' for coexistence between a vapour and a demixed liquid, calculated by neglecting the coupling of the concentration to the density. Clearly for this value of  \( \delta \) , the hidden binodal and the liquid-vapour critical point (at which it terminates) both lie within the metastable region. For smaller  \( \delta \lesssim 0.45 \) , however, the metastable critical point moves outwith the limit of metastability and the hidden binodal is lost [fig. 3b]. Although the phases corresponding to the hidden binodal are not observable at equilibrium, they are expected to influence the dynamical properties of the system. We return to this point in more detail in subsection III B.

![](./images/867746509511197440_8.jpg)

![](./images/867746509511197440_9.jpg)

FIG. 3. (a) Liquid-vapour phase envelope in the  \( \rho-T \)  plane for  \( \delta = 0.57 \) . Also shown are the spinodals  \( S_{1} \) ,  \( S_{2} \)  and  \( S_{3} \)  and the 'hidden' binodal as described in subsections III A and III B. (b) The phase envelope and spinodals for  \( \delta = 0.45 \) , by which point the metastable LV critical point has been lost.

## B. General Landau theory considerations

We now turn to analyse the system from a more general point of view. Clearly we are dealing with a two order parameter problem, i.e. the density  \( \rho = N/V \)  and the number difference order parameter  \( m = (N_{A} - N_{B})/N \) . In a symmetrical fluid, the Hamiltonian has to be invariant under sign reversal of m. The Landau expansion of the grand potential thus takes the general form

 \[ \begin{aligned}F=a\frac{(\rho-\rho_{0})^{2}}{2}+\frac{(\rho-\rho_{\mathrm{0}})^{4}}{4}-\mu(\rho-\rho_{0})\\+\ A\frac{m^{2}}{2}+\frac{m^{4}}{4}-\frac{B}{2}m^{2}(\rho-\rho_{0}),\end{aligned} \quad (3.11) \] 

where  \( \mu \)  is the chemical potential, and  \( \rho_{0} \)  is a reference density in the liquid-vapour coexistence region, chosen such that the cubic term  \( \propto (\rho - \rho_{0})^{3} \)  vanishes. An expansion of this type has been discussed in a different context by Roux et al [6]; it applies generally to fluids with an
 

additional Ising like ordering tendency. In the case of Heisenberg type ordering, e.g., in a ferromagnetic fluid, the Landau expansion looks very similar with m simply replaced by the vector  \( \vec{m} \) , and many of the conclusions drawn below still hold. The liquid-vapour critical point of the mixed fluid is found at a = 1, and could the fluid be kept at fixed density  \( \rho_{0} \) , it would demix or order at A = 0.

Phase diagrams of such fluids are often discussed in terms of an 'interaction ratio' R, comparing the strength of the ordering or demixing tendency in the fluid with the overall attractive interactions between particles  \( [7,9,10] \) . R corresponds to  \( 1 - \delta \)  in our model, to J/K in the Blume-Emery-Griffiths model  \( [35] \) , to the dipole moment m in reduced units in  \( [12] \)  and to  \( 1/T_{c}^{0} \)  in Reference  \( [11] \) . It is generally found that increasing R drives the phase behaviour from the topology depicted in fig 1a via 1b towards 1c, i.e. a critical end point turns into a tricritical point, which moves up in temperature, until the liquid-vapour critical point disappears in the region of coexistence between demixed and mixed liquid phases.

Although the interaction ratio appears to be an influential quantity, it is important to note that the basic factor driving the phase behaviour is the coupling between the two order parameters. In eq (3.11), it is described by the last term. At B=0, no tricritical point can be expected, regardless of the interaction ratio. Therefore, in what follows we shall analyse the phase behaviour in terms of the coupling strength rather than the interaction ratio. The relation between the two will be discussed later.

We will focus on the transition from a topology with a critical end point to one with a tricritical point, and assume that we are well below the liquid-vapour critical temperature, a < 0. It is then convenient to rescale the Landau expansion eqn (3.11) such that

 \[ F=\theta\frac{\hat{m}^{2}}{2}+\frac{\hat{m}^{4}}{4}-\frac{\varrho^{2}}{2}+\frac{\varrho_{4}}{4}-\hat{\mu}\varrho+\kappa(1-\varrho)\hat{m}^{2}, \quad (3.12) \] 

where  \( \hat{\mu}=\mu/(\sqrt{-a})^{3} \) ,  \( \varrho=(\rho-\rho_{0})/\sqrt{-a} \) ,  \( \hat{m}=m/\sqrt{-a} $ , and F is written in units of  \( a^{2} \) . The parameter  \( \kappa=B/2\sqrt{-a} \)  then describes the effective coupling between the order parameter and the density. The parameter  \( \theta=A/(-a)-2\kappa \)  is temperature-like:  \( \theta\propto(T-T_{CEP}) \) , where  \( T_{CEP} \)  is the temperature of the (stable or unstable) critical demixing point at fixed density  \( \varrho=1 \) . The phase behaviour is found by minimising F with respect to  \( \hat{m} \)  and  \( \varrho \) .

At  \( \kappa=0 \) , the ordering behaviour and the liquid-vapour phase separation decouple and do not affect one another. One finds coexistence of a liquid ( \( \varrho=1 \) ) and a vapour ( \( \varr-ho=-1 \) ) at  \( \hat{\mu}=0 \) , and these phase boundaries are crossed by the critical ordering ( \( \lambda \) ) line at  \( \theta=0 \) . If a small coupling  \( \kappa \)  is turned on, the ordering temperature increases with the density:

 \[ \theta_{c}(\varrho)=2\kappa(\varrho-1). \quad (3.13) \] 

Thus the  \( \lambda \)  line shifts at the LV coexistence line. Technically, the Landau expansion (3.12) predicts two critical end points, one on the liquid side at  \( \theta = 0 \) , and one on the vapour side at  \( \theta = -4\kappa \) . In all fluids studied so far, only the upper one has been seen. Situations with two CEPs are however encountered when a critical line intersects a liquid-solid coexistence region [7,12].

Next we study the stability of the demixed liquid phase. The order parameter in the homogeneous demixed liquid takes the value  \( \hat{m}^{2} = \theta_{c}(\varrho) - \theta \) . The determinant of the stability matrix there is given by  \( 4\hat{m}^{2}((3\varrho^{2} - 1)/2 - \kappa^{2}) \) . Hence the demixed phase becomes unstable for  \( \varrho < \varrho_{c} \) , with the spinodal line

 \[ \varrho_{c}=\sqrt{(2\kappa^{2}+1)/3}. \quad (3.14) \] 

A tricritical point is found when the spinodal line intersects the critical line (3.13). This requires  \( \varrho_{c} > 1 \) , i.e. the coupling  \( \kappa \)  has to be larger than a limiting value  \( \kappa_{0} = 1 \) . The tricritical point is then located at

 \[ \theta_{t}=\theta_{c}(\varrho_{c})\quad and\quad\varrho_{t}=\varrho_{c} \quad (3.15) \] 

 \[  or\quad\hat{\mu}_{t}=\frac{2}{3}\sqrt{\frac{1+2\kappa^{2}}{3}}\left(\kappa^{2}-1\right). \quad (3.16) \] 

We conclude that the coupling  \( \kappa \)  between the order parameter and the density determines the topology of the phase diagram. If  \( \kappa \)  exceeds  \( \kappa_{0} \) , the topology switches from one with a critical end point [fig. 1a] to one with a tricritical point [fig. 19]. From a physical point of view,  \( \kappa \)  basically reflects the correlations between order parameter and density. For example, the response of the average order parameter to a change of chemical potential in the demixed liquid phase is given by

 \[ \frac{\partial\hat{m}}{\partial\hat{\mu}}\propto\langle\hat{m}\varrho\rangle-\langle\hat{m}\rangle\langle\varrho\rangle\propto\kappa\frac{(\theta_{c}-\theta)^{-\zeta}}{\varrho-\varrho_{c}}, \quad (3.17) \] 

where the exponent  \( \zeta \)  is given by  \( \zeta = 1/2 \)  in mean field theory. (Scaling arguments yield  \( \zeta = (\gamma + \alpha)/2 \) , where  \( \gamma \)  and  \( \alpha \)  are the usual Ising critical exponents of the order parameter susceptibility and the specific heat).

It is instructive to investigate the relationship between  \( \kappa \)  and the interaction ratio R. When R increases, the critical end point temperature  \( T_{CEP} \)  moves closer to the liquid-vapour critical temperature  \( T_{c0} \) . Assuming  \( a \propto (T_{c0} - T) \) , this implies that the effective coupling  \( \kappa \propto \sqrt{1/(T_{c0} - T)} \)  increases also, and diverges as  \( T_{CEP} \)  approaches  \( T_{c0} \) . As long as there is any coupling between the density and the order parameter (i.e. B > 0 in eq.(3.11)), tuning R has the effect of tuning the coupling. Thus our arguments are supported by our own explicit model calculations and by the results quoted earlier [7,9–12,35].

Next we discuss the implications for the LV phase boundary. The small coupling limit  \( \kappa < \kappa_{0} \)  has been studied in detail in ref. [25]. In chemical potential space, the critical end point induces a weak singularity in the first order liquid-vapour line [26],
 

 \[ \mu(T)=\mu_{r e g}(T)-U|t|^{2-\alpha}, \quad (3.18) \] 

where  \( \mu_{reg}(T) \)  is an analytical function of the temperature T,  \( t = (T - T_{CEP})/T_{CEP} \)  and U is a critical amplitude. In the Landau theory framework,  \( \mu_{reg} \)  is simply given by  \( \mu_{REG} = \hat{\mu}_{REG} \equiv 0 \) .

The density of the vapour phase at coexistence behaves in a similar way

 \[ \rho_{g}(T)=\rho_{g,r e g}(T)-V_{g}|t|^{2-\alpha}, \quad (3.19) \] 

whereas the density of the liquid phase shows the marked hump indicated in fig. 1a, given by [25]

 \[ \rho_{l}(T)=\rho_{l,r e g}(T)-V_{l}|t|^{1-\alpha}. \quad (3.20) \] 

In the strong coupling limit,  \( \kappa > \kappa_{0} \) , one deals with the simple case in which two first order lines meet at a triple point. One thus expects a kink in  \( \mu(T) \)  and in  \( \rho_{g}(T) \) , and the density of  \( \rho_{l}(T) \)  jumps to the coexisting demixed liquid phase [cf. fig. 2c]. The two regimes meet at  \( \kappa = \kappa_{0} \) , where the critical end point turns into a tricritical end point (TEP) [36] (cf. fig 2b). Within our Landau theory, we have calculated the phase boundaries in the vicinity of a tricritical end point. Since we expect that  \( \kappa \)  varies with temperature, we consider a path  \( \kappa = \kappa_{0} + K\theta \) , where  \( \theta \propto (T - T_{TEP}) \)  as defined above. Our results to leading order in  \( \theta \)  are summarised as follows: For the chemical potential of the liquid vapour line, we find

 \[ \hat{\mu}=0\quad(\theta>0),\qquad\hat{\mu}=-(\left|\theta\right|/3)^{3/2}\quad(\theta<0). \quad (3.21) \] 

The rescaled densities of the vapour phase (spectator phase,  \( \varrho_{-} \) ) and the liquid phase ( \( \varrho_{+} \) ) are given by

 \[ \varrho_{\mp}=\mp1\qquad(\theta>0) \] 

 \[ \frac{\varrho_{-}}{\varrho_{+}}=\frac{-1}{1}+\frac{1/2\left(\left|\theta\right|/3\right)^{3/2}}{\left(\left|\theta\right|\right/3)^{1/2}}\qquad(\theta<0). \quad (3.22) \] 

Note that these results agree with the arguments presented in [25] if one inserts  \( \alpha_{t}=1/2 \) , the mean field value of the exponent  \( \alpha \)  at the tricritical point. Mean field theory is expected to yield the correct tricritical behaviour in our system, since the upper critical dimension of a tricritical point is  \( d_{u}=3 \) .

We close this subsection with a discussion of 'hidden' parts of the phase diagram. To this end, we return to eqn 3.11 and perform a general stability analysis. We consider the demixed phase at  \( m = [A - B(\rho - \rho_{0})]^{1/2} \)  and the mixed phase at m = 0.

The conditions for stability of the demixed phase have already been discussed earlier. One finds a spinodal at

 \[ \rho-\rho_{0}=\pm S_{1}\quad with\quad S_{1}^{*}=\sqrt{(B^{2}-2a)/6}, \quad (3.23) \] 

which is equivalent to eqn. 3.14 in non-rescaled units. For  \( |\rho - \rho_{0}| < S_{1}^{*} \) , the demixed phase becomes unstable with respect to phase separation into a demixed liquid and a vapour.

In the present context, the stability of the mixed liquid phase is more interesting. The stability analysis yields two spinodals: At

 \[ |\rho-\rho_{0}|<\pm S_{2}^{*}\quad,\quad S_{2}^{*}=\sqrt{-a/3}, \quad (3.24) \] 

the demixed liquid phase is unstable with respect to phase separation into a demixed liquid and its vapor, and at

 \[ \rho-\rho_{0}>S_{3}^{*}=A/B, \quad (3.25) \] 

it becomes unstable with respect to demixing. As long as A > 0 and the coupling B is sufficiently small, there exists a region on the high density side of the fluid,  \( \rho > \rho_{0} \) , where the mixed liquid phase can be metastable or even stable

 \[ \sqrt{-a/3}<\rho-\rho_{0}<A/B \] 

In that case, a binodal can be found at  \( |\rho - \rho_{0}| = \sqrt{-a} \) , which may be stable or hidden in the metastable region.

The spinodals and the hidden binodal are indicated in fig. 3. Note that both the coefficients a and A depend roughly linearly on the temperature T. This explains the linear form of  \( S_{2} \)  in the density-temperature plane as opposed to the parabolic form of  \( S_{3} \) .

The hidden binodal disappears completely as soon as  \( A \leq 0 \)  at a = 0, i.e., as soon as the spinodal  \( S_{3} \)  meets  \( S_{2} \)  at the 'hidden critical point' or beyond (at  \( \rho < \rho_{0} \) ). This criterion is independent of the coupling B. The strength of coupling thus has no influence on the appearance of a hidden binodal. It does however affect the range of metastability of the hidden binodal, i.e., the temperature interval before it is lost by intersecting the spinodal  \( S_{2} \) .

Of course, the concepts of spinodals and metastability only really make sense within a mean field treatment, and strictly speaking lose their physical meaning as soon as fluctuations are taken into account. However, a discussion of the metastable and unstable regions is still useful in the context of the dynamical properties of the system. Consider, for instance, a binary fluid with interactions corresponding to the situation shown in fig. 3a, at density  \( \rho = \rho_{0} \) , which is quenched from some high temperature into the coexistence region slightly below the 'metastable critical point'. One can then expect 'two-stage demixing'. In the first stage, the fluid will separate into domains of vapour and mixed liquid, and the separation of these domains will be accelerated by the driving force of gravitation. In the second stage, the liquid phase will slowly demix, and droplets of demixed liquid will additionally nucleate from the vapour phase. If the interactions of the fluid correspond to the situation depicted in fig. 3b, on the other hand, no intermediate stage will appear and the fluid will demix and phase separate simultaneously.
 

## IV. MONTE-CARLO STUDIES

## A. Simulation details

Many features of the simulation techniques employed in the present study have previously been detailed elsewhere  \( [37,24,17] \) . Accordingly, we confine the description of our methodology to its barest essentials, except where necessary to detail a new aspect.

We assume our system to be contained in volume  \( L^{3} \)  and to be thermodynamically open so that the total number density and concentration can fluctuate. The associated (grand canonical) partition function is:

 \[ \mathcal{Z}_{L}=\sum_{N=0}^{\infty}\sum_{\{s_{i}\}}\prod_{i=1}^{N}\left\{\int d\vec{r}_{i}\right\}e^{-\beta\left[\Phi\left(\{\vec{r},s\}\right)+\mu N\right]} \quad (4.1) \] 

Here, the species label  \( s_{i} = 1, -1 \)  denotes respectively the two particle species A and B,  \( N = N_{A} + N_{B} \)  is the total particle number,  \( \beta = 1/k_{B}T \)  is the inverse temperature and  \( \mu \)  is the chemical potential. The configurational energy density  \( \Phi \)  is given by

 \[ \Phi(\{\vec{r},s\})=\sum_{i j}U(r_{i j},s_{i}s_{j}) \quad (4.2) \] 

where the symmetrical square-well interparticle potential U is defined in eqs. 2.1 and 2.2.

Grand canonical Monte Carlo (MC) simulations were performed using a standard Metropolis algorithm  \( [38,24] \) . The MC scheme comprises two types of operations:

1. Particle insertions and deletions.

2. Particle identity transformations:  \( A \rightarrow B \) ,  \( B \rightarrow A \) 

Since particle positions are sampled implicitly via the random particle transfer step, no additional translation algorithm is required.

To simplify identification of particle interactions, we employed a linked list scheme [38]. This involves partitioning the periodic simulation space of volume  \( L^{3} \)  into  \( l^{3} \)  cubic cells, each of linear dimension the interaction range, i.e.  \( L/l = 1.5 \) . We chose to study two system sizes corresponding to l = 8 and l = 10, containing, at LV coexistence, approximate average particle numbers  \( \langle N \rangle = 550 \)  and 1100 respectively. Equilibration periods of up to  \( 2 \times 10^{6} \)  MCS were employed and sampling frequencies were 100 MCS for the l = 8 system to 150 MCS for the l=10 system. Production runs amounted to  \( 2 \times 10^{7} \)  MCS for the l=8 and  \( 5 \times 10^{7} \)  MCS for the l=10 system size. At coexistence, the average acceptance rate for particle transfers was approximately 10%, while for spin flip attempts the acceptance rate was approximately 40%.

In this work we wish to explore the parameter space spanned by the three variables  \( (\mu,T,\delta) \) . To accomplish this, without having to perform a very large number of simulations, we employed the histogram reweighting technique [39]. Use of this technique permits histograms obtained at one set of model parameters to be reweighted to yield estimates appropriate to another set of model parameters. To enable simultaneous reweighting in all three fields  \( \mu,T,\delta \) , one must sample the conjugate observables  \( (\rho,u,ud) \) , with  \( \rho=N/V \)  the number density,  \( u=\Phi/V \)  the configurational energy density, and  \( u_{d} \)  that part of u associated with interactions between dissimilar particle species. In addition to these variables, we have also accumulated the quantity  \( \tilde{m}=(N_{A}-N_{B})/V=\rho m \)  which gives a measure of the degree of A-B ordering in the system.

As mentioned in the introduction, standard GCE simulations, deep within the LV coexistence region, are hampered by the large free energy barrier separating the two coexisting phases. This barrier leads to metastability effects and prohibitively long correlation times. To circumvent this difficulty, we have employed the multicanonical preweighting method  \( [22] \)  which encourages the simulation to sample the interfacial configurations of intrinsically low probability. This is achieved by incorporating a suitably chosen weight function in the MC update probabilities. The weights are subsequently 'folded out' from the sampled distribution to yield the correct Boltzmann distributed quantities. Use of this method permits the direct measurement of the distribution of observables at first order phase transitions, even when these distributions span many decades of probability. Details concerning the implementation of the techniques can be found in references  \( [22,17] \) .

## B. Method and results

Using the multicanonical simulation scheme, we have obtained the density distribution  \(  p(\rho)  \)  for a number of states close to the LV coexistence curve, and for a number of choices of  \( \delta \) . We begin, by probing the regime of critical end point behaviour.

On the basis of the mean field results of sec. III, CEP behaviour is expected to occur for large  \( \delta < 1 \) . For  \( \delta \lesssim 1 \) , the CEP will occur at very low temperatures relative to the LV critical point (i.e.  \( T \ll T_{c0} \) ), but will move to higher temperatures as  \( \delta \)  is reduced. At some point as  \( \delta' \)  is reduced, the phase diagram is predicted to evolve into a triple point topology. Thus in seeking to observe CEP behaviour one should aim to set  \( \delta' \)  large and to search at low temperatures. Unfortunately, very low temperatures are associated with high liquid densities at LV coexistence, and these inaccessible to our GCE scheme due to the prohibitively small particle transfer acceptance rate. In fact we find that the largest value of  \( \delta' \)  for which the density fell within the accessible range ( \( \rho \lesssim 0.7 \) ) was  \( \delta = 0.72 \) . Although this value of  \( \delta' \)  is not as large as one might hope to attain, it nevertheless transpires that CEP behaviour occurs. This is demonstrated in fig. 4.
 

which shows the liquid and vapour coexistence densities for this value of  \( \delta \)  obtained as the first moment of the respective peaks of  \( p(\rho) \)  for the l = 8 system size [25]. The data were obtained by reweighting [39] four histograms spanning temperatures in the range  \( T = 0.99 - 1.05 \) , and coexistence was located using the equal peak-weight criterion for  \( p(\rho) \)  [40,24]. Also shown in the figure is the measured locus of the critical line.

![](./images/867746509511197440_10.jpg)

FIG. 4. The liquid-vapour coexistence curve in the  \( \rho-T \)  plane for  \( \delta=0.72 \) , showing the vapour (V), mixed fluid (MF) and demixed fluid (DF) phases. The results were obtained from the measured peak positions of the coexistence density distributions for the l=8 system size. Statistical errors do not exceed the symbol sizes.

Clearly the data of fig. 4 display an anomaly in the liquid branch density close to the intersection point of the  \( \lambda \)  line and the liquid branch (i.e. at the CEP). In the thermodynamic limit, the liquid branch density is expected to exhibit a cusp-like singularity at the CEP, as given in equation 3.20. In our finite-sized system, however, this critical singularity is smeared out and shifted, so that only a rounded depression in the coexistence envelope is visible [25]. Since these aspects of the CEP singularities have recently been discussed in detail elsewhere [25], we shall not pursue them further here. Instead we shall proceed to consider what happens as  \( \delta \)  is made smaller still.

Further reducing  \( \delta \)  continues to shift the CEP closer to the LV critical point. As one reaches  \( \delta = 0.675 \) , however, the phase diagram changes topology. We find that above a certain temperature the liquid peak in  \( p(\rho) \)  decomposes into two peaks. This is shown in fig. 5 for the l = 10 system size at a temperature T = 1.044. Evident from this figure are two closely separated overlapping peaks, the presence of which signifies incipient triple point behaviour. It follows that for this  \( \delta \)  and T, the system lies close to the tricritical end point which heralds entry into the triple point phase diagram topology [cf. fig. 2b]. Actually we believe the TEP lies close to  \( \delta = 0.68 \)  since this is the value at which we first observe the appearance of a shoulder in the liquid peak. In a sufficiently large system, this shoulder would presumably resolve itself into a distinct peak. We have not, however, attempted to pinpoint the location of the TEP more precisely, as this would require a full finite-size scaling analysis—a task beyond the scope of the present study.

![](./images/867746509511197440_11.jpg)

FIG. 5. The measured near-coexistence density distribution  \( p(\rho) \)  for T = 1.044,  \( \delta = 0.675 \)  showing the three-peak structure discussed in the text. The distribution is normalised to unit integrated weight and statistical errors are comparable with the symbol sizes.

Using histogram reweighting, we have monitored the temperature dependence of  \( p(\rho) \)  as  \( \delta \)  is reduced below the value at which the TEP occurs. fig. 6a shows a selection of density distributions for  \( \delta = 0.665 \) , for which a triple point (TP) occurs at some temperature  \( T_{TP} < T_{c0} \) , i.e. below the liquid-vapour critical temperature. The corresponding forms of  \( p(\tilde{m}) \)  are shown in fig. 6b. At the triple point, a demixed liquid coexists with a mixed liquid and its vapour. For  \( T > T_{TP} \) , there is phase coexistence either between the mixed liquid and its vapour, or between the mixed and demixed liquid [cf. fig. 2c]. The liquid-vapour coexistence terminates at the LV critical point, while the mixed-demixed liquid coexistence curve terminates at a tricritical point. From fig. 6a one sees that for  \( \delta = 0.665 \) , the tricritical point temperatures lie slightly below the LV critical point temperature, as evidenced by the fact that on increasing T the liquid peaks merge before the liquid and vapour peaks do so.
 
![](./images/867746509511197440_12.jpg)

![](./images/867746509511197440_13.jpg)

FIG. 6. (a) Coexistence density distributions  \( p(\rho) \)  for  \( \delta = 0.665 \)  at a selection of temperatures spanning the triple point temperature. (b) The corresponding form of  \( p(\tilde{m}) \)  where  \( \tilde{m} = m\rho = (N_{A} - N_{B})/V \) . Lines are guides to the eye. Statistical errors are comparable with the symbol sizes.

The coexistence density distributions for  \( \delta = 0.66 \)  are shown in fig 7a for temperatures spanning the triple point temperature. For this  \( \delta \) , the tricritical point is sufficiently well separated from the LV line that it is possible to distinguish the liquid-vapour and liquid-liquid branches by appropriately tuning the chemical potential. This is demonstrated in fig. 7b which shows  \( p(\rho) \)  for the two coexistence curves at T = 1.058. The different degree of order in the two liquid phases is clearly seen in the distribution  \( p(\tilde{m}) \) , shown in fig. 7c. One notices, however, that both the density distributions show signs of the third phase. This reflects the closeness of the two coexistence curves at this  \( \delta \)  and T, as evidenced by the very small chemical potential difference. Under such conditions, finite-size smearing effects render it difficult to completely isolate two of the three phases.

![](./images/867746509511197440_14.jpg)

![](./images/867746509511197440_15.jpg)

![](./images/867746509511197440_16.jpg)

FIG. 7. (a) Selected coexistence density distributions for  \( \delta = 0.66 \) , spanning the triple point. (b) The density distribution for T = 1.058 for two different values of the chemical potential. (c) The corresponding forms of  \( p(\tilde{m}) \) , where  \( \tilde{m} = m\rho = (N_{A} - N_{B})/V \) . Lines are merely guides to the eye and statistical errors are comparable with the symbol sizes.

Finally in this section, we consider the phase behaviour for  \( \delta = 0.65 \) . Coexistence forms of  \( p(\rho) \)  at selection of temperatures are shown fig 8. One observes that on increasing temperature, the low density vapour peak moves smoothly over to merge with the high density peak of
 

the ordered liquid. At no point is a three-peaked structure visible. This scenario is consistent with the phase behaviour shown schematically in fig. 2d, in which the vapour and the demixed liquid phases merge at a tricritical point.

![](./images/867746509511197440_17.jpg)

FIG. 8. Selected near-coexistence density distributions for  \( \delta = 0.65 \)  at a number of sub-tricritical temperatures. Statistical errors are comparable with the symbol sizes.

## V. DISCUSSION AND CONCLUSIONS

In summary, we have used multicanonical Monte Carlo simulations and histogram reweighting techniques to study how the liquid-vapour phase behaviour of a symmetrical binary mixture depends on  \( \delta \) , the ratio of interaction strengths for dissimilar and similar particle species. For  \( \delta\lesssim1 \) , the phase diagram exhibits a critical end point at temperatures well below the liquid-vapour critical point. Decreasing  \( \delta \)  shifts the critical end point closer to the liquid-vapour critical point. For  \( \delta\approx0.68 \) , however, the critical end point becomes locally unstable, and a triple point occurs in which vapour, a mixed liquid, and a demixed liquid all coexist. For temperatures above the triple point there is coexistence either between a high density demixed fluid and a moderate density mixed fluid, or between a mixed fluid and its vapour. Decreasing  \( \delta \)  still further pushes the triple point to higher temperature, until for  \( \delta<0.65 \)  it eventually equals that of the isotropic liquid-vapour critical point. Thereafter, the mixed liquid phase is preempted by the demixed liquid phase and the liquid-vapour coexistence curve terminates in a tricritical point.

Thus our simulation results confirm the qualitative picture of phase diagram topology emerging from mean field theory as set out in sections II and III. These theories seem quite successful in capturing key features of the behaviour such as the existence of a coexistence curve anomaly at the CEP, the existence of the triple point regime, and the crossover to a purely tricritical regime. Additionally, our Landau theory study of subsection III B provides useful physical insight into the manner in which the coupling of density and concentrations leads to the observed phase behaviour.

In quantitative terms, however, the mean field theories are less reliable. Owing to the neglect of correlations, they predict neither the correct exponents for the coexistence curve singularities at the CEP, nor the shape of the near critical LV coexistence curve. The values they yield for quantities such as the LV critical temperature are also at variance with simulation estimates: e.g. for  \( \delta = 0.72 \)  mean field calculations predict that the LV critical temperature is  \( T_{c0}^{mf} = 1.172 \) , while simulation gives  \( T_{c0}^{sim} = 1.06(1) \) . In view of this, the apparently better agreement between the mean field and simulation estimates of the CEP for  \( \delta = 0.72 \) , i.e.  \( T_{CEP}^{mf} = 1.002 \)  and  \( T_{CEP}^{sim} = 1.02(1) \) , are presumable fortuitous. For 3d tricritical behaviour, mean field theory is at least expected to yield the correct tricritical exponents, since the upper critical dimension for such behaviour is d = 3 [15]. Although we have not attempted to probe the universal aspects of the tricritical behaviour, our results show that estimates for the tricritical temperature are not reproduced by the simulations, at least close to the triple point regime. However, this may partly be the result of crossover effects associated with the relative proximity of the LV critical and tricritical points.

The mean field estimates are also inaccurate regarding the sensitivity of the phase diagram topology to changes in  \( \delta \) . The calculations of section III A predict that the regime of triple point topology lies in the range  \( 0.605 < \delta < 0.708 \) . In contrast, the simulation results show this range to be considerably smaller, namely  \( 0.65 \lesssim \delta \lesssim 0.68 \) . Indeed weir it not for our use of histogram reweighting to scan the phase behaviour as a function of  \( \delta \) , we might easily have missed this regime altogether. Thus it seems that more sophisticated liquid state theories are called for before the goal of accurately predicting the phase behaviour of simple binary fluid models is attained. Presumably any successful theory must be capable of dealing both with the critical and non-critical regimes of the phase diagram. Infact one such theory, the Heirarchical Reference Theory [32] has recently been proposed. It would be interesting to see whether or not it accurately reproduces the phase behaviour of the present model.

With regard to further work on this model, one particularly interesting project would be to investigate the predicted existence of the hidden binodal and associated metastable critical point. The occurrence of metastable critical points was first discussed by Cahn [33], and later found in lattice gas models by Hall and Stell [3]. More recently it has suggested that they occur in colloidal fluids close to the freezing line [34], in dipolar fluids [12], and in models for water [41]. Since the present model offers a computationally tractable system, it might usefully be employed as a test-bed for studying the generic features of the metastable critical point. This could feasibly be achieved by quenching the system from high temperature.
 

into the unstable regime just below the metastable critical point. As described in section III B, this should result in a two-stage demixing process in which the metastable mixed liquid phase appears for a transitory period before eventually demixing at later times.

Additional interesting work would be to look at the equilibrium phase behaviour of the symmetrical mixture as a function of  \( \delta < 0 \) . Landau theory [6] predicts that as  \( \delta \)  is made increasingly negative, the tricritical point transforms first into a double critical end point, before a critical end point emerges on the vapour side of the LV coexistence envelope. It would certainly be worthwhile to assess whether or not this scenario is correct.

## Acknowledgements

NBW thanks A.Z. Panagiotopolous and G. Stell for helpful discussions, and M.E. Cates for bringing reference  \( [6] \)  to his attention. PN thanks the DFG for financial support (Heisenberg foundation). This work was supported by the EPSRC (grant number GR/L91412), the DFG (BMBF grant Number 03N8008C), and the Royal Society of Edinburgh. Computer time on the HLRZ at Jülich is also gratefully acknowledged.

[1] P.H. van Konynenburg and R.L. Scott, Phil. Trans. Roy. Soc., A298 (1980).

[2] J.S. Rowlinson, F.L. Swinton, Liquids and Liquid Mixtures, Butterworth (London, 1982).

[3] C.K. Hall and G. Stell, Phys. Rev. B11, 224 (1975); Phys. Rev. A7, 1679 (1973);

[4] P.C. Hemmer and G. Stell, Phys. Rev. Lett. 24, 1284 (1970).

[5] G. Stell and P.C. Hemmer, J. Chem. Phys. 56, 4274 (1972).

[6] D. Roux, C. Coulon and M.E. Cates, J. Phys. Chem. 96, 4174 (1992).

[7] P.C. Hemmer and D. Imbro, Phys. Rev. A16, 380 (1977).

[8] A. Oukouiss and M. Baus, Phys. Rev. E55, 7242 (1997).

[9] J.M. Tavares, M.M. Telo da Gama, P.I.C. Teixeira, J.J. Weis and M.J.P. Nijmeijer, Phys. Rev. E52, 1915 (1995).

[10] J.-J. Weis, M.J.P. Nijmeijer, J.M. Tavares and M.M. Telo da Gama, Phys. Rev. E55, 436 (1997).

[11] H. Zhang, M. Widom, Phys. Rev. E49, R3591 (1994).

[12] B. Groh and S. Dietrich, Phys. Rev. E50, 3814 (1994); B. Groh and S. Dietrich, Phys. Rev. Lett. 72, 2422 (1994); ibid 74, 2617 (1995).

[13] M.A. Zaluska-Kotur and L.A. Turski, Phys. Rev. A41, 3066 (1990).

[14] The presence of a tricritical point in such a model is traceable to its special symmetry. In general, tricritical behaviour cannot occur in a binary fluid mixture except by accident.

[15] For a general review of tricritical phenomena see I. D. Lawrie and S. Sarbach, in Phase transitions and critical phenomena edited by C. Domb and J.L. Lebowitz (Academic London, 1984), Vol. 8.

[16] Strictly speaking there is 4-phase coexistence since in zero field the demixed liquid comprises an A-rich and a B-rich phase in coexistence. For the case of nonconserved concentration considered here, the demixed liquid generally comprises either a homogeneous A-rich phase or a B-rich phase. Owing to symmetry, both these phases have the same density, and we shall thus regard them as one single liquid phase. Note however, that the two-phase nature of the demixed liquid is important in the context of the tricritical behaviour.

[17] N.B. Wilding and P. Nielaba, Phys. Rev. E53, 926 (1996); N.B. Wilding, J. Phys. Condens. Matter 9, 585 (1997).

[18] E. Lomba, J.-J. Weis, N.G. Almarza, F. Bresme and G. Stell, Phys. Rev. E49, 5169 (1994).

[19] D. Marx, P. Nielaba and K. Binder, Phys. Rev. B47, 7788 (1993).

[20] S. Sengupta, D. Marx and P. Nielaba, Europhys. Lett. 20, 383 (1992).

[21] P. de Smedt, P. Nielaba, J.L. Lebowitz, J. Talbot and L. Dooms, Phys. Rev. A38, 1381 (1988);

[22] B. Berg and T. Neuhaus, Phys. Rev. Lett. 68, 9 (1992). The method is actually a variant of the 'Umbrella Sampling' technique, G.M. Torrie and J.P. Valleau, J. Comp. Phys. 23, 187 (1977).

[23] In principle one could also apply the Gibbs Ensemble simulation method (A.Z. Panagiotopoulos, Mol. Phys. 61, 813 (1987)) to tackle this problem. However, the precision of this method seems to be less than is obtainable from combined use of multicanonical and histogram reweighting techniques (see eg. [24]). It is also not well suited for studying a transition from 2-phase to 3-phase coexistence as occurs on approaching a triple point.

[24] N.B. Wilding, Phys. Rev. E52, 602 (1995).

[25] N.B. Wilding, Phys. Rev. Lett. 78, 1488 (1997); N.B. Wilding, Phys. Rev. E55, 6624 (1997);

[26] M.E. Fisher and P.J. Upton, Phys. Rev. Lett. 65, 2402 (1990). M.E. Fisher and M.C. Barbosa, Phys. Rev. B43, 11177 (1991).

[27] R.M. Stratt, J. Chem. Phys. 80, 5764 (1984);

[28] R.M. Stratt, Phys. Rev. Lett. 53, 1305 (1984);

[29] S.G. Desjardin and R.M. Stratt, J. Chem. Phys. 81, 6232 (1984).

[30] P. Nielaba and S. Sengupta, Phys. Rev. E55, 3754 (1997).

[31] J.-P. Hansen and I.R. McDonald Theory of simple liquids, Academic, London (1986).

[32] A. Parola and L. Reatto, Adv. Phys. 44, 211 (1995).

[33] J.W. Cahn, Trans. Metall. Soc. AIME, 242, 166 (1968).

[34] R.M.L. Evans, W.C.K. Poon and M.E. Cates, Europhys. Lett. 38, 595 (1997); W.C.K Poon, Phys. Rev. E55, 3762 (1997).

[35] M. Blume, V.J. Emery and R.B. Griffiths, Phys. Rev. A 4, 1071 (1971).

[36] In the full space of  \( (T,\mu,h) \) , the tricritical end point terminates a line of tricritical points, see also [6].
 

[37] N.B. Wilding and A.D. Bruce, J. Phys. Condens. Matter. 4, 3087 (1992).

[38] M.P. Allen and D.J. Tildesley Computer simulation of liquids Oxford University Press (1987).

[39] A.M. Ferrenberg and R.H. Swendsen, Phys. Rev. Lett. 61, 2635 (1988); ibid 63, 1195 (1989).

[40] C. Borgs and R. Kotecký, Phys. Rev. Lett. 68, 1734 (1992).

[41] P.H. Poole, T. Grande, F. Sciortino, H.E. Stanley and C.A. Angell, J. Comp. Mat. Sci. 4, 373 (1995); S. Sastry, P.G. Debenedetti, F. Sciortino, H.E. Stanley, Phys. Rev. E53, 6144 (1996).
 
