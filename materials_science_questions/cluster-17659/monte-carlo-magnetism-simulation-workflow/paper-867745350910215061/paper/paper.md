
# Application of the Projected Dynamics Method to an Anisotropic Heisenberg Model

S. J. Mitchell \( ^{1,2} \) , M. A. Novotny \( ^{2} \) , José D. Muñoz \( ^{3,4} \) 

 \( ^{1} \) Center for Materials Research and Technology

and Department of Physics,

Florida State University, Tallahassee, Florida 32306-4351, USA

 \( ^{2} \) Supercomputer Computations Research Institute,

Florida State University, Tallahassee, Florida 32306-4130, USA

 \( ^{3} \) Institute for Computer Applications 1,

University of Stuttgart, D-70569 Stuttgart, Germany

 \( ^{4} \) Permanent address: Dpto. de Física, Univ. Nacional de Colombia, Bogota D.C., Colombia

Received 20 August 1999
Revised 20 August 199

The Projected Dynamics method was originally developed to study metastable decay in ferromagnetic discrete spin models. Here, we apply it to a classical, continuous Heisenberg model with anisotropic ferromagnetic interactions, which evolves under a Monte Carlo dynamic. The anisotropy is sufficiently large to allow comparison with the Ising model. We describe the Projected Dynamics method and how to apply it to this continuous-spin system. We also discuss how to extract metastable lifetimes and how to extrapolate from small systems to larger systems.

## 1. Introduction

Metastability is a ubiquitous physical phenomenon in which a system remains near a local free-energy minimum, even though there exists a global minimum with lower free energy. If initially near this local free-energy minimum, the system remains in the vicinity until a long sequence of improbable thermal fluctuations drive it over a free-energy barrier and into the global free-energy minimum. The time scale associated with this sequence of improbable events can be very long \( ^{1,2,3} \) , and efficient dynamic simulation methods are necessary to conquer the very long time scales \( ^{3} \) . We discuss here how to extend the Projected Dynamics (PD) method \( ^{4,5,6,7} \) , which was originally developed for ferromagnetic discrete spin models, to classical, continuous spin systems like the Heisenberg model with anisotropic ferromagnetic interactions.

The basic concept of the PD method is to project the high-dimensional Markov process in configuration space, which describes the metastable decay in microscopic detail, onto a one-dimensional Markov process in a slow variable. We choose this variable to be the z component of the total magnetization,  \( M_{z} \) . For the ferromag
 

netic Ising model, or the ferromagnetic Heisenberg model with sufficient anisotropy in the z direction, below the critical temperature, the free energy projected onto  \( M_{z} \)  is symmetric about  \( M_{z}=0 \)  in zero applied field, and it displays two equal minima. When a magnetic field  \( \vec{H}=H_{z}\hat{z} \)  is applied, this symmetry is broken. The global free-energy minimum is the stable well, in which the majority of the spins are aligned parallel with the external field, while the local minimum is the metastable well, in which the majority of the spins are anti-parallel with the field.

To study the time scale for the system to escape from the metastable well, the system is prepared with all spins aligned in the  \( \pm\hat{z} \)  direction for times t < 0. This initial state corresponds to the stable well for  \( H_{z} = +\infty \) . At time t = 0, the field is instantaneously reversed to a finite negative value, and the system is evolved under a Monte Carlo dynamic. The system quickly relaxes to the bottom of the metastable well, in the vicinity of which it remains until thermal fluctuations drive it over the saddle point and into the stable well. We define the escape time  \( \tau \)  as the time (in Monte Carlo steps per spin, MCSS) required for the system to first reach  \( M_{z} = 0 \) . We define the lifetime of the metastable state as  \( \langle\tau\rangle \) , the escape time averaged over many statistically independent escapes.

For the Ising model, or the Heisenberg model with sufficiently large z anisotropy, in two or three dimensions, the dominant mechanism to escape the metastable well at small fields is by nucleation and growth of droplets of the stable phase within a background of the metastable phase \( ^{1,8,9,10,11,12} \) . If R is the radius of a droplet of the stable phase, we can define a critical droplet radius  \( R_{c} \) . Subcritical droplets,  \( R < R_{c} \) , are dominated by the tendency to minimize surface free energy and tend to shrink. Super-critical droplets,  \( R > R_{c} \) , are dominated by the tendency to minimize bulk free energy and tend to grow. For critical droplets,  \( R = R_{c} \) , the probabilities to grow and shrink are equal. We also define \( ^{8} \)  the typical separation between critical droplets as  \( R_{0} \) .

For the Ising model, four different droplet regimes have been found \( ^{8} \)  as the strength of the external field is varied for a system of fixed linear size L. In the coexistence regime,  \( L < R_{c} \) , the system is not large enough to contain a complete critical droplet. In the single droplet (SD) regime,  \( R_{0} \gg L \gg R_{c} \) , only one droplet of the stable phase nucleates and grows to take over the system. In the multi-droplet (MD) regime,  \( R_{0} \ll L \) , many droplets nucleate and grow to take over the system. In the strong-field (SF) regime,  \( R_{c} \approx 1 \)  spin, the droplet picture is no longer useful.

Figure 1 shows  \( \langle\tau\rangle \)  for the anisotropic kinetic Heisenberg model studied in this paper (see Sec. 2 for definition) with L = 16 as a function of  \( 1/|H_{z}| \) . The SD, MD, and SF regimes are labeled. Because of the long time scales, we were unable to simulate at very weak fields where the coexistence regime is expected. When plotted in this way, the data in the SD and MD regimes should asymptotically fall on straight lines. Neglecting prefactors in the nucleation rate, the Kolmogorov-Johnson-Mehl-Avrami (KJMA) theory \( ^{1,2,8,13} \)  of independent droplet nucleation and growth predicts that the ratio of the slopes in the SD and MD regimes should be
 
![](./images/867745350910215061_1.jpg)

Fig. 1. The metastable lifetime for  \( J_{x}=J_{y}=1 \) ,  \( J_{z}=2 \) , T=1, and L=16. The circles indicate the lifetimes measured directly by simulating 1000 escapes. The squares indicate the lifetimes measured by the PD method with 1000 escapes. The error bars indicate the statistical error in only the direct measurement of the lifetime (circles). The ratio of the slopes of the two lines is approximately 2.5. The strong field (SF), multi-droplet (MD), and single droplet (SD) regimes are labeled.

 \( d+1 \) , where d = 2 is the spatial dimension of the spin lattice. The difference between our measured ratio of the slopes of 2.5 and the expected value of 3 is the result of non-exponential prefactors in the nucleation rate \( ^{8} \) . The decay is characterized by widely different time scales in the three regimes. The PD method provides a way to understand and conquer these disparate time scales.

This paper is organized in the following way. Section 2 introduces the ferromagnetic Heisenberg model with anisotropic interactions and the Monte Carlo dynamic. Section 3 describes the PD method. Section 4 discusses how to extrapolate to larger system sizes. Section 5 gives a summary of our results and a brief discussion of possibilities for future work.

## 2. Model

We consider a two-dimensional, square array of three-dimensional, classical, Heisenberg (XYZ) spins with anisotropic ferromagnetic interactions. The Hamiltonian is given by

 \[ \mathcal{H}=-\sum_{\langle i j\rangle}(J_{x}s_{i x}s_{j x}+J_{y}s_{i y}s_{j y}+J_{z}s_{i z}s_{j z})-\vec{H}\cdot\sum_{i}\vec{s}_{i}, \quad (1.1) \] 

where  \( \vec{s}_{i} \)  refers to the  \( i^{th} \)  Heisenberg spin,  \( \sum_{i} \)  is a sum over all spins,  \( \vec{H} \)  is the
 

magnetic field,  \( J_{x} \) ,  \( J_{y} \) , and  \( J_{z} \)  are the interactions in the x, y, and z directions respectively, and  \( \sum_{\langle ij\rangle} \)  is a sum over all nearest-neighbor pairs. For all systems studied here, we choose  \( J_{x} = J_{y} = 1 \) ,  \( J_{z} = 2 \) , and  \( \vec{H} = H_{z}\hat{z} \)  where  \( \hat{z} \)  is perpendicular to the plane containing the spins and  \( H_{z} < 0 \) . All systems studied were  \( L \times L \)  squares with L = 16 or 32 and periodic boundary conditions.

The system is evolved with a Monte Carlo dynamic after the field reversal discussed in the previous section. There is a unique choice of deterministic microcanonical spin dynamic \( ^{14} \) . However, since any dynamic satisfying detailed balance will give the correct equilibrium distribution, there is no unique choice of Monte Carlo dynamic \( ^{9,10,11,12} \) . In this work, we use the following Monte Carlo dynamic. First, choose a spin location i at random. Call  \( \vec{s}_{old} \)  the current orientation of spin i. Next, randomly choose a new trial orientation  \( \vec{s}_{new} \)  for spin i, uniformly distributed over the solid angle by choosing the polar angle  \( \phi \)  uniformly on the interval  \( [0, 2\pi) \)  and choosing  \( \cos(\theta) \)  uniformly on  \( [-1, +1] \) . The trial spin  \( \vec{s}_{new} \)  is either accepted or rejected as the next orientation for spin i according to the Glauber acceptance probability.

 \[ P(\vec{s}_{n e w}|\vec{s}_{o l d})=\{1+\exp\left[\beta(E_{n e w}-E_{o l d})\right]\}^{-1}, \quad (1.2) \] 

where  \( \beta=(k_{B}T)^{-1} \)  and  \( E_{new} \)  and  $ E_{old} are the energies of the system with the new and old spin orientations respectively. The temperature is represented by T, and  \( k_{B}=1 \)  is Boltzmann's constant. In these simulations, we use T=1, which is below the critical temperature  \( T_{c} \) . Using the maximum of the specific heat and the susceptibility of the z component of the magnetization, we found that for the anisotropy used here,  \( T_{c}\approx1.75 \) .

## 3. Projected Dynamics Method

As shown in Fig. 1, metastable lifetimes can be extremely long. Thus, simulations of metastable decay require fast algorithms \( ^{3} \) . However, since we are studying the dynamic behavior of the system under the Monte Carlo dynamic defined above, we cannot speed up the simulation by techniques that alter the dynamic. Thus conventional fast equilibrium algorithms, like cluster updates \( ^{15,16,17} \) , are not acceptable, and a different approach is needed.

The dynamic behavior of the system is a random walk in the configuration space of  \( 2L^{2} \)  continuous degrees of freedom. The essence of the PD method is to project this Markov process onto a Markov process in the one-dimensional  \( M_{z} \)  space. It is important to point out that the actual walk through  \( M_{z} \)  space is not Markovian. There are memory terms, but neglecting these memory terms appears to be a very reasonable approximation. To define the random walk in  \( M_{z} \)  we should measure the transition probabilities per Monte Carlo step (mcs) between each  \( M_{z} \)  state and every other  \( M_{z}^{\prime} \)  state. However, since there is a continuum of  \( M_{z} \)  states for the Heisenberg model, this is not possible. Therefore, we must lump  \( M_{z} \)  states together.
 

into discrete, coarse-grained states, or bins, and measure the transition probabilities between these bins. In the Ising model, for which the PD method was originally developed \( ^{4} \) , the  \( M_{z} \)  states are discrete, and no coarse-graining is required.

To simplify the projected Markov process, we further impose that the bins be large enough that only transitions between neighboring bins are possible. The largest possible change in  \( M_{z} \)  that can occur during one mcs is  \( \pm2 \) , corresponding to  \( \vec{s}_{i} = -\hat{z} \rightarrow \vec{s}_{i'} = +\hat{z} \)  or vice versa. Thus, we divide the  \( M_{z} \)  space into  \( L^{2} \)  equal bins of width 2. We define an index or bin number for the lumped states as  \( n = \operatorname{Int}[(L^{2} - M_{z})/2] \) , such that the n = 0 bin includes the states  \( M_{z} \in [-L^{2}, -L^{2} + 2) \)  and the  \( n = L^{2} - 1 \)  bin includes the states  \( M_{z} \in [L^{2} - 2, L^{2}) \) . The  \( n = L^{2} \)  bin contains only the  \( M_{z} = L^{2} \)  state. With this choice of binning, only transitions from bin n to bins  \( n + 1 \)  and n - 1 are possible in one mcs. We define the growth probability  \( g(n)/L^{2} \)  as the probability of undergoing a transition from n to  \( n + 1 \)  in one mcs. Analogously, the shrinkage probability  \( s(n)/L^{2} \)  is the probability of undergoing a transition from n to n - 1 in one mcs. We define the escape time as the time to first enter the bin  \( n = n_{stop} \) . For an escape time cut-off of  \( M_{z} = 0 \) ,  \( n_{stop} = L^{2}/2 \) .

Before discussing how to measure the growth and shrinkage probabilities, it is useful to return to our discussion of droplet theory. For the fields and anisotropy studied here, most spins are either approximately aligned or approximately anti-aligned with the magnetic field. The number of spins nearly aligned with the field approximates the number of stable spins in the system. When a droplet of the stable phase nucleates, the width of the domain wall is on the order of one lattice spacing. To a rough approximation (exact for Ising) \( ^{6} \) , the  \( M_{z} \)  bin index n gives the number of stable spins in the system, such that n = 0 corresponds to all spins in the metastable phase and  \( n = n_{stop} = L^{2}/2 \)  corresponds to about 1/2 of the spins in the metastable phase. The growth,  \( g(n)/L^{2} \) , and shrinkage,  \( s(n)/L^{2) \) , probabilities are then the probabilities that the volume of the stable phase will grow or shrink respectively.

There are two aspects to measuring the growth and shrinkage probabilities. First, we must generate a series of sample configurations for each lumped  \( M_{z} \)  state. Second, we must measure the growth and shrinkage probabilities for each sample configuration. The simplest and most straight forward way to generate the sample configurations is simply to perform dynamic simulations of many escapes. The growth and shrinkage probabilities are then obtained by integrating over all the spins in the configuration and averaging over configurations.

There are several ways to obtain these probabilities for a single configuration. Since we have an analytic expression for the probability density function for the orientations of a single spin (the Glauber probability with a normalization constant), one might be inclined to analytically integrate this distribution function to find the probability that a single spin will move the configuration into the next bin after one mcs. The Broad Histogram method \( ^{18,19,20,21} \)  uses a similar analytic analysis tool for
 

measuring the density of states in equilibrium. Unfortunately, we have been unable to analytically perform the necessary double integrations. These integrals could be calculated numerically by the trapezoidal method or by some other numerical method, but because these integrals must be calculated for every spin each mcs, numerical methods are too computationally intensive for practical use in this case. There are also too many parameters to construct look-up tables of reasonable size. Therefore, we use a very simple counting method, i.e. a Monte Carlo integration over spins and configurations.

To calculate the growth and shrinkage probabilities by the counting method, we simply perform the dynamic Monte Carlo simulation and keep track of the bin number of the current configuration. We record the number of mcs spent in bin n  \( (H_{n}) \) , as well as the number of times the system jumped from bin n into bins  \( n+1 \)   \( (G_{n}) \)  and  \( n-1 \)   \( (S_{n}) \) . The Monte Carlo estimates for the growth and shrinkage probabilities are then  \( g(n)/L^{2}=G_{n}/H_{n} \)  and  \( s(n)/L^{2}=S_{n}/H_{n} \) . It is important to note that all methods for obtaining the growth and shrinkage probabilities should give identical results in the limit of an infinite number of samples.

Figure 2 shows the growth and shrinkage probabilities for  \( H_{z} = -0.9 \)  and L = 16, obtained from 1000 escapes with  \( n_{stop} = 237 \) . The most obvious features are the three crossings where the growth and shrinkage probabilities are equal. Each crossing corresponds to an extremum in the projected free-energy landscape \( ^{4,7} \) . From left to right, the crossings give the locations of the bottom of the metastable well, the saddle point and the bottom of the stable well. The location of the saddle point is extremely difficult to find by any other method but is given quite simply by the PD method. The noise in the growth and shrinkage probabilities could be reduced with better statistics, but this data is adequate to obtain very reasonable values of the average lifetime  \( \langle\tau\rangle \) .

To compute the lifetime from the growth and shrinkage probabilities, we first compute the residence time  \( h(n) \) , which is the average number of MCSS that the system spends in bin n per escape. The average lifetime can be found with the following recursive relations \( ^{4,5,6} \) :

 \[ \begin{aligned}h(n_{stop}-1)\ &=\ &\frac{1}{g(n_{stop}-1)},\\h(n)\ &=\ &\frac{1+s(n+1)h(n+1)}{g(n)},\\\langle\tau\rangle\ &=\ &\sum_{n=0}^{n_{stop}-1}h(n).\end{aligned} \quad (3.1) \] 

Higher moments of  \( \tau \)  can be found in a similar way \( ^{4,22} \) .

Figure 1 shows a comparison of  \( \langle\tau\rangle \)  measured directly by averaging  \( \tau \)  over 1000 escapes with the measurement from the growth and shrinkage probabilities. Although the growth and shrinkage probabilities give useful information, simply mea-
 
![](./images/867745350910215061_2.jpg)

Fig. 2. The growth (solid line) and shrinkage (dashed line) probabilities for  \( J_{x}=J_{y}=1 \) ,  \( J_{z}=2 \) , T=1 and L=16 at  \( H_{z}=-0.9 \)  measured from 1000 escapes with  \( n_{stop}=237 \) . The three crossings from left to right correspond to the bottom of the metastable well, the saddle point, and the bottom of the stable well.

suring them is no faster than measuring  \( \langle\tau\rangle \)  by direct simulation with the same number of escapes. However, measurements of the average lifetime can be performed more quickly if we extrapolate the growth and shrinkage probabilities to larger system sizes.

## 4. Size Extrapolation

Given  \(  g(V, n)  \)  and  \(  s(V, n)  \(  for a system of  \) V = L^{2} $  spins, we can extrapolate to find  \(  g(2V, n)  \)  and  \(  s(2V, n).  \)  The following relations \( ^{4} \)  are used to extrapolate from  \( V \rightarrow 2V \) :

 \[ g(2V,n)\approx\frac{\sum_{i=0}^{n}h(V,n-i)h(V,i)[g(V,n-i)+g(V,i)]}{\sum_{i=0}^{n}h(V,n-i)h(V,i)}, \quad (3.2) \] 

 \[ s(2V,n)\approx\frac{\sum_{i=0}^{n}h(V,n-i)h(V,i)[s(V,n-i)+s(V,i)]}{\sum_{i=0}^{n}h(V,n-i)h(V,i)}, \quad (3.3) \] 

where  \( n \in [0, V/2] \)  insures that the late-time approach to the stable phase does not alter the extrapolated probabilities. These relationships can be applied recursively for even larger systems.

Figure 3 shows the growth and shrinkage probabilities for L = 32 and  \( H_{z} = -0.9 \) , obtained by direct simulation of 1000 escapes for the L = 32 system and by extrapolating twice from L = 16. For L = 16,  \( n_{stop} = L^{2}/2 = 128 \) . However, the
 
![](./images/867745350910215061_3.jpg)

Fig. 3. The growth (solid line) and shrinkage (dashed line) probabilities for  \( J_{x}=J_{y}=1 \) ,  \( J_{z}=2 \) , T=1 and L=32 at  \( H_{z}=-0.9 \)  measured directly from simulating 1000 escapes. The heavy solid lines indicate the growth and shrinkage probabilities for L=32, obtained by extrapolating twice from L=16, which only extends to bin n=128, denoted by the vertical dotted line.

extrapolated growth and shrinkage probabilities are only reasonable for  \( n \leq V/2 \)  for the smallest V used in the extrapolation. Thus, we must use  \( n_{stop} = 128 \)  for L = 32, even though this does not correspond to  \( M_{z} = 0 \)  for the L = 32 system. With the cut-off bin  \( n_{stop} = 128 \) ,  \( \langle \tau \rangle = 277 \)  MCSS from the extrapolated probabilities and  \( \langle \tau \rangle = 295 \pm 15 \)  MCSS from the direct measurement of the  \( 32^{2} \)  lattice also with  \( n_{stop} = 128 \) . Using this extrapolation we have saved a factor of about four in simulation time.

Additional simulation time may be saved in computing  \( h(n) \)  for different stopping bins. Since  \( h(n) \(  depends on  \) n_{stop} \( , without knowledge of  \) g(n) \(  and  \) s(n) \( , a new simulation must be performed to calculate  \) h(n) \(  for different  \) n_{stop} $ . However,  \( g(n) \)  and  \( s(n) \)  are independent of  \( n_{stop} \) , within statistical error, and therefore, once  \( g(n) \)  and  \( s(n) \)  have been obtained for a large value of  \( n_{stop} \) ,  \( h(n) \)  is easily calculated for any smaller cut-off.

## 5. Summary

In summary, we have shown that the droplet picture \( ^{1,2,8,9,10,11,12} \)  provides a reasonable description for the Heisenberg model with the anisotropic ferromagnetic interactions used here. We have also shown that the metastable escape is well described by the projected Markov process in the one-dimensional  \( M_{z} \)  space. We have applied the PD method over a wide range of fields and obtained very good
 

estimates of the average lifetimes. Extrapolations to larger system sizes have also been shown to be accurate. Such extrapolations reduce the amount of computer time required to perform the simulations.

It was found for discrete spin models \( ^{3,5,6,7} \)  that forcing the system to escape from the metastable well by inserting a wall moving in the  \( M_{z} \)  space, gave accurate estimates of the average lifetime and allowed speed-ups of several orders of magnitude in computer time. By forcing the system to escape, lifetimes could be measured at weaker fields (longer lifetimes) than were previously accessible. Future work on the Heisenberg model will attempt to extend the range of fields accessible in a reasonable amount of computer time by application of assisted escape methods similar to the forced escaped methods used for the discrete models.

Still another way to save computational time in metastable decay of discrete spin models is by extrapolation to weak fields, and hence to long lifetimes \( ^{4} \) . Utilizing this technique for our continuous model would require us to obtain the functional form for the single spin flip growth and shrinkage probabilities, requiring that we are able to perform the Broad Histogram \( ^{18,19,20,21} \)  type double integrations described in Sec. 3.

## Acknowledgment

The authors would like to thank G. Brown, G. Korniss and P. A. Rikvold for useful discussions. Supported in part by the NSF through grant number DMR-9871455, the Supercomputer Computations Research Institute which is funded by the U.S. Department of Energy and the State of Florida, the Center for Materials Research and Technology, and the National Energy Research Scientific Computing Center.

## References

1. P. A. Rikvold and B. M. Gorman, in Annual Reviews of Computational Physics I, edited by D. Stauffer (World Scientific, Singapore, 1994), pp. 149-191.

2. P. A. Rikvold, M. A. Novotny, M. Kolesik, and H. L. Richards, in Dynamical Properties of Unconventional Magnetic Systems, NATO Science Series E, volume 349, editors A. T. Skjeltorp and D. Sherrington, p 307, (Kluwer, Dordrecht, 1998).

3. M. A. Novotny, Int. J. Mod. Phys. C, this volume.

4. M. Kolesik, M. A. Novotny, P. A. Rikvold, and D. M. Townsley, in Computer Simulations in Condensed Matter Physics X, editors D. P. Landau, K. K. Mon, and H.-B. Schüttler, p. 246 (Springer-Verlag, Heidelberg, 1998).

5. M. Kolesik, M. A. Novotny, and P. A. Rikvold, Phys. Rev. Lett. 80, 3384 (1998).

6. M. A. Novotny, M. Kolesik, and P. A. Rikvold, Computer Phys. Commun. preprint cond-mat/9811039, in press (1999).

7. M. Kolesik, M. A. Novotny, and P. A. Rikvold, Mater. Res. Soc. Symp. Proc. 492, 313 (1998).

8. P. A. Rikvold, H. Tomita, S. Miyashita, and S. W. Sides, Phys. Rev. E 49, 5080 (1994).
 

9. S. T. Chui, J. Appl. Phys. 79, 4951 (1996).

10. S. T. Chui, J. Magn. Magn. Mater. 168, 9 (1997).

11. D. Hinzke and U. Nowak, Phys. Rev. B. 58, 265 (1998).

12. U. Nowak and D. Hinzke, J. Appl. Phys. 85, 4337 (1999).

13. R. A. Ramos, P. A. Rikvold, and M. A. Novotny, Phys. Rev. B 59, 9053 (1999), and references cited therein.

14. D. P. Landau, Int. J. Mod. Phys. C, this volume.

15. R. H. Swendsen and J. S. Wang, Phys. Rev. Lett. 58, 86 (1987).

16. U. Wolff, Phys. Rev. Lett. 62, 361 (1989).

17. L. Chayes and J. Machta, Physica A. 239, 542 (1997), Physica A. 254, 477 (1998).

18. P. M. C. Oliveira and T. J. P. Penna, Braz. J. of Phys. 26, 677 (1996).

19. J. S. Wang, Eur. Phys. J. B. 8, 287 (1999).

20. José D. Muñoz and Hans J. Herrmann. preprint cond-mat/9810024.

21. José D. Muñoz and Hans J. Herrmann. In Computer Simulation Studies in Condensed Matter Physics XII, edited by D. P. Landau, S. P. Lewis, and H. B. Schüttler, (Springer, Heidelberg, in press).

22. J. Lee, M. A. Novotny, and P. A. Rikvold, Phys. Rev. E. 52, 356 (1995).
 
