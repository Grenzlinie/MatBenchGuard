DOI 10.1007/s11182-016-0771-2

Russian Physics Journal, Vol. 59, No. 2, June, 2016 (Russian Original No. 2, February, 2016)

# GROWTH SIMULATION AND STRUCTURE ANALYSIS OF
OBLIQUELY DEPOSITED THIN FILMS

B. A. Belyaev, $^{1,2,3}$ A. V. Izotov, $^{1,2}$ and P. N. Solovev $^{1}$

UDC 538.975

Based on the Monte Carlo method, a model of growth of thin films prepared by oblique angle deposition of particles is constructed. The morphology of structures synthesized by simulation is analyzed. To study the character of distribution of microstructural elements (columns) in the film plane, the autocorrelation function of the microstructure and the fast Fourier transform are used. It is shown that with increasing angle of particle incidence, the film density monotonically decreases; in this case, anisotropy arises and monotonically increases in the cross sections of columns, and the anisotropy of distribution of columns in the substrate plane also increases.

Keywords: oblique angle deposition, simulation of film growth, Monte Carlo method.

## INTRODUCTION

Over the last few years thin-film magnetic nanostructures have increasingly been employed as controllable media for the development of superhigh frequency (microwave) devices with electrically tunable characteristics. As an example, thin magnetic films and layered structures can be mentioned, whose microwave properties depend on the applied external magnetic field. Based on films with high magnetic permeability in the microwave range, filters, phase shifters [1], magnetometers of weak quasi-stationary and high-frequency fields [2], and other microwave devices [3] are constructed. In this case, the search for technological conditions allowing high-quality samples with required reproducible characteristics to be obtained is under way [4].

The oblique deposition is the well-known method that allows the properties of thin-film samples prepared by deposition of fluxes of substance on the substrate to be controlled [5]. The tilt of the direction of atomic flux from the normal to the substrate plane during deposition cases the self-shading effect, that is, the impossibility of atoms being deposited to occupy the region shaded by previously deposited particles [6, 7]. As a result of competition between the processes of geometrical shading and surface diffusion in the film, a clearly pronounced columnar inhomogeneous microstructure is formed under certain deposition conditions. The anisotropy on the microstructural level leads to the anisotropy of some physical parameters of films: mechanical, electric, optical, and magnetic [8, 9]. These special features are used to prepare samples possessing unique qualities. For example, permalloy films can have very high uniaxial anisotropy depending on the deposition angle, which can be useful for some microwave applications [10, 11]. At the same time, in [12, 13] it has been shown recently that the presence of oriented inhomogeneities in the bulk of a $Fe_3Si$ thin film, arising due to oblique angle deposition of silicon, gives rise to the mechanism of relaxation of magnetic fluctuations with anisotropic behavior, which is of great interest for spintronics applications.

L. V. Kirensky Institute of Physics of the Siberian Branch of the Russian Academy of Sciences, Krasnoyarsk, Russia, e-mail: solap@ya.ru; $^{2}$ Siberian Federal University, Krasnoyarsk, Russia, e-mail: iztv@mail.ru; $^{3}$ Siberian State Aerospace University Named after Academician M. F. Reshetnev, Krasnoyarsk, Russia, e-mail: belyaev@iph.krasn.ru.
Translated from Izvestiya Vysshikh Uchebnykh Zavedenii, Fizika, No. 2, pp. 120–125, February, 2016. Original article submitted October 16, 2015.

1064-8887/16/5902-0301 ©2016 Springer Science+Business Media New York

![](./images/811268557022167040_1.jpg)

Fig. 1. Schematic pattern of principles of simulating the deposition process comprising cubic particle 1 moving toward the substrate at the angle $\alpha$ to its normal, shaded region 2 inaccessible for the incident particle, and diffusion of just deposited particle 3 (a). Surfaces $(x-y)$ and cross-section cuts $(z-y)$ of films simulated for the indicated deposition angles $\alpha$ (b).

To use effectively the obliquely deposited films in the above-indicated applications, it is important to understand physical mechanisms that determine the dependences of the film microstructure on the deposition conditions. Experimental determination of these mechanisms is a complex problem, since the microscopy methods (electron or atomic-force microscopy) allow only two-dimensional patterns of the film surface or of its cut along a certain direction to be recorded. At the same time, many obliquely deposited films possess poorly ordered internal microstructure, and study of the two-dimensional projection of a three-dimensional sample, as is the case for crystal samples, cannot provide trustworthy information on its morphology.

### 1. SIMULATION OF THE THIN FILM GROWTH PROCESS

To obtain the data on the bulk structure of film samples, numerical simulation of their growth was used. At present the methods of molecular dynamics in which the condensation of particles is considered by calculating their interatomic interactions [14] are the most exact ones. Unfortunately, such approaches call for large computing time; therefore, great difficulties arise when synthesizing objects of sufficiently large sizes [15]. An alternative is simulation of the film deposition process by the Monte Carlo method that allows one to simulate growth of rather large films even on a personal computer [16]. However, to simulate objects possessing structures close to those observed experimentally, the initial model parameters must be chosen carefully.

In the present work, a dependence of the film morphology on the angle of atomic flux incidence was investigated by the Monte Carlo method. Based on the principles outlined in [17, 18], a model of thin film growth was constructed in the package $MATLAB$. As shown in Fig. $1a$, the simulation region is the spatial lattice consisting of cubic cells each of which can be occupied by a deposited particle. The particle size (the length of the cubic cell edge) is designated by $\Delta$.

The deposition process was the following. Cubic particles with arbitrary $(x-y)$ initial plane coordinates successively started to move along linear trajectories at a preset angle $\alpha$ to the substrate surface generated in advance (it was covered by the single layer completely filled with particles). In this case, the initial height (coordinate $z$) of each particle is established to be only several cells of the simulation region higher than the current maximal height of the film.

In the actual deposition process, before collision with the film surface the particle being deposited deviates from a linear trajectory as a result of short-range interatomic interaction with surface atoms [19, 20]. This effect can be considered in the model to a certain degree if we assume that the particle being deposited can join the film surface with a certain probability even in the case in which there are empty cells between the surface and the particle. We used the following two conditions under which the particle stopped motion and joined the film: 1) the deposited particle with

100% probability stopped motion if at least one from the nearest cells (26 cells surrounding the particle) was occupied and 2) if among the cells following the nearest ones at least one was occupied, the particle being deposited with 50% probability joined the occupied cell (if several such cells were occupied, the deposited particle could equiprobably join one of them).

After particle joining, the algorithm that simulated limited diffusion corresponding to the first zone of structural model [9] was executed. The diffusion algorithm is based on the model of random walk and consists of following steps. Vacancies (empty cells) are searched among the nearest cells surrounding the particle that has just deposited. The particle hops in one of the vacancies. Then empty cells are searched again around the new position of the particle, and the particle hops again in one of them. Such hopping is repeated \(S\) times. The probability of vacancy occupation by a particle depends on the number of occupied cells surrounding this vacancy, since the binding energy of an atom in an actual physical system is the greater, the larger the number of its neighbors. As is well known, the surface diffusion of atoms is described by the Arrhenius law [16]. Then the probability \(P_{i \to j}\) of particle hopping from the \(i\)th cell to the \(j\)th cell can be expressed as follows [17]:

$$
P_{i \to j}=\frac{\exp \left(\gamma N_{j}\right)}{\sum_{j_{\text {total }}} \exp \left(\gamma N_{j}\right)},
\tag{1}
$$

where \(N_{j}\) is the number of neighbors surrounding the \(j\)th vacancy and \(\gamma\) is a constant whose physical meaning is explained below. Summation is performed over all vacancies (\(j_{\text{total}}\)) surrounding the \(i\)th cell in which the diffusing particle is localized. It is important to note also that two-dimensional (\(x$-$y\)) periodic boundary conditions were used in the deposition model.

From the physical viewpoint, the constant \(\gamma\) can be considered proportional to the ratio of the surface energy to the energy caused by the film temperature. It is obvious that the number of hops \(S\) characterizes the distance at which the particle can move before it will be buried under other particles. This in turn is determined by a large number of the deposition parameters, including the sample temperature, deposition rate, etc. In relatively simple deposition models of the Monte Carlo method the given parameters, as a rule, are disregarded; therefore, the initial model parameters are conventionally assigned based on a comparison of the physical properties of structures obtained by simulation with the properties of experimental films [16, 17]. In this work, we adjusted the diffusion parameters so that the porosity of the simulated structures was close to the porosity of permalloy (Ni-Fe) films prepared by deposition on unheated substrates [21]. As a result, it was found that \(S = 5\) and \(\gamma = 0.45\).

## 2. STRUCTURE AND CHARACTERISTICS OF OBLIQUELY DEPOSITED FILMS

The special features of the internal structure of obliquely deposited films were investigated for model structures with sizes \(256\ (x) \times 256\ (y) \times 80\ (z)\ \Delta\). Since the Monte Carlo method is based on stochastic processes, ten independent depositions of films were considered for each particle incidence angle \(\alpha\) to increase the reliability of the results obtained. We first analyzed the calculated integral film parameter – the specific density \(\rho\) whose dependence on the particle deposition angle \(\alpha\) is shown in Fig. \(2a\) by solid curves. To exclude the influence of inhomogeneities, the density was calculated by averaging over the film thickness in the range \(1\Delta < z < 64\Delta\). It can be seen that the density decreases with \(\alpha\); however, it changes slightly up to \(\alpha \approx 45^\circ\), and then sharply decreases. The results obtained are in qualitative agreement with experimental measurements of the density of films prepared from different materials that demonstrate the general tendency of porosity increase with the deposition angle [22]. As an example, Fig. \(2a\) shows the measured specific density of Ge films [17]. It is important to note that in each case, the behavior of the curve \(\rho(\alpha)\) was determined not only by the concrete deposited substance, but also depended on the deposition conditions.

Patterns of structures obtained by simulation shown in Fig. 1 help us to elucidate the established dependences of the density on the deposition angle. From the figures illustrating the film cross section along the \(z$-$y\) plane parallel to the plane of particle incidence it can be seen that columnar microstructure is formed under conditions of oblique angle

![](./images/811268557022167040_2.jpg)

Fig. 2. Dependences of the specific film density ρ on the deposition angle α. Results of simulation are shown by small circles, and experimental data [17] for the Ge film are shown by small triangles (a). The dependence of the average distance D between columns in the film plane on the deposition angle α retrieved from the FFT spectra is shown in Fig. 1b. In the inserts, the central regions of the FFT spectra are shown for the indicated α values (b).

deposition, the degree of film porosity increases, and columns become more pronounced. For large glancing angles the film deposition ceases to be continuous, namely, islet structure consisting of tilted columns almost disconnected from each other is formed.

To analyze the character of distribution of columns in the plane of the film and to estimate the average distance between the columns, we used the fast Fourier transform (FFT). Since the simulated structure represents the three-dimensional matrix comprising zeros and units (cells empty or occupied by particles), any cut through the x–y plane is a two-dimensional matrix with M columns and N rows. The direct discrete two-dimensional Fourier transform has the form [23]

$$
F_{p, q}=\frac{1}{M N} \sum_{m=1}^{M} \sum_{n=1}^{N} f_{m, n} \exp \left[2 \pi i\left(\frac{p m}{M}+\frac{q n}{N}\right)\right], \tag{2}
$$

where the function $f_{m,n}$ is equal to zero if the cell (m, n) is not occupied by a particle and unity if it is occupied and p and q are spatial frequencies. The spectra were calculated for each film layer in the x–y plane and then averaged.

The calculated moduli of the Fourier spectrum (Fig. 2b) are shaped as inhomogeneous diffusion rings. Such distribution confirms the absence of long-range order, but indicates the existence of the dominant distance between the columns, which is reflected as a fundamental spatial frequency in the FFT spectrum. In this case, the diffusivity of rings indicate the degree of inhomogeneity in column distribution. However, for $\alpha>70^{\circ}$ the shape of rings changes from round to ellipsoidal one, which demonstrates a quasi-ordered distribution of columns in the film plane for large deposition angles, with preferred direction oriented approximately along the deposition plane. The spatial frequency corresponding to the maximal amplitude of the FFT spectrum is inversely proportional to the dominant distance between the columns. The average distances D between the columns were calculated from the average radial profiles of the FFT rings [24]. The obtained dependences of D on the deposition angle are shown in Fig. 2. It can be seen that for deposition angles $\alpha<55^{\circ}$ the distances between the columns are almost identical; however, then they quickly increase and as a whole, correlate with the density of the structure.

Another important structural characteristic of the obliquely deposited films is the shape of columns that can be estimated from the two-dimensional autocorrelation function G defined by the following expression [25]:

$$
G\left(k_{m}, k_{n}\right)=\sum_{m=1}^{M} \sum_{n=1}^{N} h(m, n) × h\left(m+k_{m}, n+k_{n}\right), \tag{3}
$$

![](./images/811268557022167040_3.jpg)

Fig. 3. Dependence of the correlation lengths $\xi_x$ and $\xi_y\cos\beta$ on the deposition angle $\alpha$. The central part of the surface of the autocorrelation function calculated for $\alpha=45^\circ$ (a) is shown in the insert of Fig. $3a$. Dependence of the ratio of the correlation lengths $\xi_x/\xi_y\cos\beta$ and of the column tilt angle $\beta$ on the deposition angle $\alpha$ is shown in Fig. $3b$.

where the function $h\ (m,\ n)$ is equal to zero if the cell $(m,\ n)$ is empty and is equal to unity if the cell is occupied by a particle, and $k_m$ and $k_n$ are shears along the columns and rows, respectively.

By analogy with calculations of the Fourier spectra, the autocorrelation function was calculated in the film plane for each layer and then averaged. The contour of the autocorrelation function near its central maximum (Fig. $3a$) is a direct visualization of the average column shapes in the film plane. Calculations demonstrated that generally this contour has an ellipsoidal form with the main axes directed up and down with respect to the deposition plane. Thus, two characteristic parameters can be distinguished, namely, the correlation lengths $\xi_x$ and $\xi_y$ equal to the widths at half central maximum along the $x$ and $y$ directions [25]. The correlation lengths $\xi_x$ and $\xi_y$ allow the average column sizes in the $x$-$y$ plane to be estimated. It should be considered that at oblique angle deposition, the columns are tilted to the film plane, and their tilt angle $\beta$ with the normal to the film plane increases with the deposition angle (Fig. $3b$). From this it follows that the average cross-section size of columns in the direction $y$ is equal to $\xi_y\cos\beta$.

Figure $3a$ shows the dependences of the correlation lengths $\xi_x$ and $\xi_y\cos\beta$ on the deposition angle $\alpha$. It can be seen that with increasing deposition angle, the average column sizes in the $x$ and $y$ direction evolve differently. For $\alpha\leq20^\circ$, $\xi_x$ and $\xi_y\cos\beta$ are approximately identical; however, then they behave oppositely: $\xi_x$ increases, for $\alpha\approx60^\circ$ reaches a maximum of $\sim9\Delta$, and then monotonically decreases, while $\xi_y\cos\beta$ with increasing $\alpha$ smoothly decreases and saturates after $\alpha\approx75^\circ$. These results demonstrate that the column cross sections are inhomogeneous and depend strongly on the deposition angle. The dependence of the ratio of the correlation lengths $\xi_x/\xi_y\cos\beta$ on the angle $\alpha$ shown in Fig. $3b$ helps us to estimate the inhomogeneity or *elongation* of columns. It can be seen that for $\alpha<20^\circ$ the cross section of columns is almost a circle, since the ratio $\xi_x/\xi_y\cos\beta$ is close to unity, that is, the columns in the cross section are isotropic. However, then the ratio $\xi_x/\xi_y\cos\beta$ linearly increases with $\alpha$, which testifies to the occurrence and monotonic increase of the column anisotropy that reaches a maximum ($\xi_x/\xi_y\cos\beta\approx1.66$) at $\alpha\approx65^\circ$. A small decrease in the degree of anisotropy of the column shape with further increase in $\alpha$ was observed only for $\alpha>85^\circ$.

The established dependences of the sample morphology on the deposition angle are the result of balance between the two mechanisms determining the film structure: the limited surface diffusion and the trajectory of particle incidence. Indeed, the continuity of the film during oblique angle deposition is violated stronger in the direction parallel to the deposition direction, since the shaded region for particles arriving on the film surface during film growth increases mainly along the direction of the incident particle flux. Because of the limited diffusion, the shaded regions cannot be occupied completely by the particles. Thus, the self-shading effect is only amplified with increasing tilt angle of the beam of incident particles from the normal to the film plane. Thus, associations of columns orthogonal to the deposition plane are formed. The termination of the increase of the structural anisotropy for $\alpha>65^\circ$ is apparently

caused by low film density that leads to smaller probability of association during growth of the neighboring columns since diffusing particles not always can overcome the distance between them.

## CONCLUSIONS

Thus, in this work the model of obliquely deposited thin film growth has been suggested based on the Monte Carlo method. Results of investigating the microstructure of films obtained for different angles of particle incidence were presented. It was demonstrated that with increasing angle of particle incidence, the film density monotonically decreased. This was accompanied by a significant increase in the anisotropy of column cross sections as well as by the increase in the anisotropy of column distribution in the substrate plane. The application of the autocorrelation function of the microstructure and of the fast Fourier transform allowed us not only the character of changes of the microstructural element distribution (tilted columns), but also their average shape significantly depending on the particle deposition angle to be analyzed.

The approach to the simulation of the process of oblique film deposition suggested here allowed the dynamics of film formation to be investigated, and the evolution of its morphology with increasing thickness to be traced. In this case, it should be noted that over the last few years, with the advent of methods of numerical analysis (micromagnetic and electrodynamic), a possibility arose to investigate physical properties of objects considering their complex structure [26, 27]. The combination of methods of simulating the structural and physical properties is the theoretical tool that allows the dependences of the film parameters on their deposition conditions to be investigated. This is very important for the manufacture of samples with the sought-after characteristics.

This work was supported in part by State Assignment for R&D A3.528.2014K of Ministry of Education and Science of the Russian Federation to Siberian Federal University in 2014.

## REFERENCES

1.  B. A. Belyaev, A. V. Izotov, A. A. Leksikov, *et al.*, Izv. Vyssh. Uchebn. Zaved., Fiz., **53**, No. 9/2, 163–165 (2010).
2.  A. N. Babitskii, B. A. Belyaev, G. V. Skomorokhov, *et al.*, Tech. Phys. Lett., **41**, No. 4, 324–327 (2015).
3.  R. E. Camley, Z. Celinski, T. Fal, *et al.*, J. Magn. Magn. Mat., **321**, 2048 (2008).
4.  B. A. Belyaev, A. V. Izotov, S. Ya. Kiparisov, and G. V. Skomorokhov, Phys. Sol. State, **50**, No. 4, 676–683 (2008).
5.  B. A. Belyaev, A. V. Izotov, and P. N. Solovev, Physica, **B481**, 86–90 (2016).
6.  D. O. Smith, M. S. Cohen, and G. P. Weiss, J. Appl. Phys., **31**, 1755 (1960).
7.  L. Abelmann and C. Lodder, Thin Solid Films, **305**, 1 (1997).
8.  M. Suzuki, J. Nanophotonics, **7**, 073598 (2013).
9.  M. M. Hawkeye and M. J. Brett, J. Vac. Sci. Tech., **A25**, 1317 (2007).
10. Z. Xiaoqiang, W. Zhenkun, *et al.*, J. Magn. Magn. Mat., **324**, 2899 (2012).
11. N. Phuoc and C. K. Ong, J. Phys., **D46**, 485002 (2013).
12. I. Barsukov, R. Meckenstock, J. Lindner, *et al.*, IEEE Trans. Magn., **46**, 2252 (2010).
13. I. Barsukov, R. Meckenstock, J. Lindner, *et al.*, Phys. Rev., **B85**, 014420 (2012).
14. J. Seo, H.-Y. Kim, and J.-S. Kim, Phys. Rev., **B71**, 075414 (2005).
15. B. C. Hubartt, X. Liu, and J. G. Amar, J. Appl. Phys., **114**, 083517 (2013).
16. T. Karabacak, J. Nanophotonics, **5**, 052501 (2011).
17. M. Suzuki and Y. Taga, J. Appl. Phys., **90**, 5599 (2001).
18. T. Smy, D. Vick, M. J. Brett, *et al.*, J. Vac. Sci. Tech., **A18**, 2507 (2000).
19. S. Muller-Pfeiffer, H. Kranenburg, and J. C. Lodder, Thin Solid Films, 1992, **213**, 143 (2000).
20. R. Alvarez, L. Gonzalez-Garcia, *et al.*, J. Phys., **D44**, 385302 (2011).
21. M. Yamanaka and R. Ueda, J. Phys. Soc. Jpn., **21**, 1607 (1966).

22. M. M. Hawkeye, M. Taschuk, and M. J. Brett, Glancing Angle Deposition of Thin Films, Wiley, UK (2014).

23. L. I. Kveglis and V. B. Kashkin, Dissipative Structures in Thin Nanocrystal Films: A Monograph [in Russian], Publishing House of Siberian Federal University, Krasnoyarsk (2011).

24. C. Buzea, G. Beydaghyan, C. Elliott, and K. Robbie, Nanotechnology, **16**, 1986 (2005).

25. J. L. Bubendorff, G. Garreau, and S. Zabrocki, Surf. Sci., **603**, 373 (2009).

26. D. Vick and M. J. Brett, J. Vac. Sci. Tech., **A24**, 156 (2006).

27. C. Charles, N. Martin, and M. Devel, Surf. Coat. Techn., **276**, 136 (2015).