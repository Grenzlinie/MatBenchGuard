# Metallic inductive and capacitive grids: theory and experiment

B. K. Minhas, W. Fan, K. Agi, S. R. J. Brueck, and K. J. Malloy

Center for High Technology Materials, 1313 Goddard SE, Albuquerque, New Mexico 87106

Received August 1, 2001; revised manuscript received December 10, 2001; accepted January 29, 2002

We present theoretical modeling and experimental validation of both capacitive (dot) and inductive (hole) metallic crossed gratings in the mid-infrared (2–5 $\mu$m). The gratings are fabricated by use of interferometric lithography and modeled by use of rigorous coupled-wave analysis. Our experimental and numerical investigations of the transmittance spectra of these gratings suggest that, as in inductive grids, the behavior of capacitive grids is described by the coupling of the incident light into surface plasma waves. © 2002 Optical Society of America

OCIS codes: 050.1220, 050.1950.

## 1. INTRODUCTION

Crossed gratings, of which metallic grids are special cases, find application across the electromagnetic spectrum. They are used in the microwave regime as filters and for making efficient antennas. $^{1}$ In the far infrared, they find applications as beam splitters and mirrors. $^{2}$ Their use as filters $^{3,4}$ and solar selective surfaces $^{5}$ in the visible and near infrared has also been demonstrated. Recently there has been interest in the behavior of subwavelength-aperture metallic crossed gratings $^{6}$ (inductive or hole grids in particular) in the visible with potential applications for novel optoelectronic devices. In that study the important features of the transmission spectra of subwavelength inductive grids were characterized on the basis of a wave-vector conservation model. The authors, adopting a kinematic approach, showed that the salient spectral features of the experimentally measured transmittance correspond to the coupling of incident radiation to surface plasma waves (SPWs). $^{6}$ Although this method explains the wavelength position of the experimental features, a rigorous diffraction model is necessary to quantitatively describe all experimental features and as a tool for crossed grating design. The importance of this approach is underscored by the recent work of Heinzel et al., $^{7}$ Martin-Moreno et al., $^{8}$ and Popov et al., $^{9}$ in which the behavior of metallic crossed gratings was analyzed with vector diffraction models. Reference 7 presented experimental results and numerical modeling [based on rigorous coupled-wave analysis (RCWA) $^{10}$] for periodically structured metal surfaces with potential applications as filters in thermophotovoltaic systems. Martin-Moreno et al. $^{8}$ and Popov et al. $^{9}$ specifically examined the behavior of metallic subwavelength hole arrays. Reference 8 treated the electromagnetic fields in the metallic inductive grids by use of surface-impedance boundary conditions, and Ref. 9 employed the Fourier modal method. $^{11}$ Both of these papers analyzed the experimental work of Ebbesen et al. $^{6}$ and attempted to explain the mechanism of unusually high transmittance through metallic, subwavelength-aperture inductive grids. However, to the best of our knowledge, rigorous numerical modeling of finite-conductivity capacitive grids along with experimental verification has not yet been presented (McPhedran et al. $^{12}$ and Botten et al. $^{13}$ have numerically modeled perfectly conducting capacitive grids by use of a rigorous modal approach).

In this paper we present a rigorous diffraction model validated by experimental data for both inductive (hole) and capacitive (dot) subwavelength, metallic crossed gratings under normal plane-wave illumination. We present the effects of varying grating parameters on the mid-IR transmittance spectrum. The paper is organized as follows. First, we briefly explain the fabrication and experimental characterization of crossed gratings. This is followed by a description of the numerical model. Then we discuss the coupling of incident radiation into SPWs for inductive grids and show that similar coupling also occurs for capacitive grids. Coupling in SPWs for both kinds of gratings are described by use of the rigorous diffraction model. Finally, we demonstrate the experimental verification of the diffraction model by modeling gratings with varying parameters.

## 2. FABRICATION AND EXPERIMENTAL CHARACTERIZATION

The gratings used to validate the modeling were fabricated with interferometric lithography and lift-off pattern transfer. A double-polished silicon sample is used as a substrate material as it is transparent in the 2–5-$\mu$m wavelength regime. After the substrate is coated with photoresist, interferometric lithography $^{14}$ is used to expose the pattern. Developing the photoresist and metallization by e-beam evaporation of gold follows. The final step is an acetone jet lift-off, which leaves the desired pattern.

Experimental characterization of these structures is done with Fourier-transform IR (FTIR) spectroscopy with an unpolarized light source. All the results presented in this paper are normal-incidence transmittance spectra

normalized to the system response without any sample. The error associated with the magnitude of the FTIR response was estimated to be 2% from measurements on standard samples, whereas the repeatability of measurements on the crossed-grating samples was within 3%.

## 3. MODELING
We use vector diffraction theory to model these subwavelength metallic inductive and capacitive grids. A commonly used approach to vector diffraction modeling expands the electromagnetic fields in the various regions in terms of Fourier series. This approach is variously known as RCWA,¹⁰ the coupled-wave method, or the Fourier modal method (FMM).¹⁵,¹⁶ In our numerical model we have followed the approach used in Ref. 10 and will use the term RCWA.

The numerical treatment of crossed gratings by use of RCWA has been carried out previously¹⁷,¹⁸ and will not be detailed here for the sake of brevity. However, below we discuss the important features of our implementation of the RCWA-based numerical model.

### A. Finite Conductivity of the Gratings
Crossed gratings are modeled in the microwave regime by taking the metallic scatterers to have infinite conductivity.¹⁹⁻²¹ Although this approximation works well at microwave frequencies, in which metals have very high conductivity, its use for the visible and ultraviolet spectral region is clearly inappropriate. In the IR spectral region, the suitability of the infinite-conductivity approximation is uncertain. We avoid these questions by using a rigorous diffraction model, which takes into account the finite conductivity of the gratings. This approach comes at a high computational cost.

Since the late 1970’s, significant work has been done in modeling crossed gratings with finite conductivity. Derrick et al.,²² Petit,²³ and Harris et al.²⁴ proposed a model based on a coordinate transformation; Vincent²⁵ used a finite-difference method; and Bruno and Reitich²⁶ employed a variation-of-boundaries method. More recently, Kettunen et al.²⁷ presented numerical results for metallic inductive grids based on RCWA. Their modeling was done principally for the case of rectangular scatterers. Here we present modeling based on RCWA for finite-conductivity rectangular as well as circular metallic scatterers, arranged in a square lattice on a silicon substrate.

### B. Finite Substrate Effects
The results presented in this paper are for the normal incidence transmittance spectra of metallic crossed gratings placed on a silicon substrate. The spectral range of interest is 2–5 $\mu$m, in which silicon is practically transparent. Clearly, assuming the silicon substrate to be infinite in this regime (as is commonly done in grating diffraction modeling) is not justified because of multiple reflections taking place within the high-index substrate. The thickness of the substrate is much larger than the coherence length of the incident light for the chosen experimental conditions; therefore the appropriate way to model the substrate is to do incoherent addition of the diffracted orders inside the substrate.

Previous work based on this approach has been done for one-dimensional gratings by Chateau et al.²⁸ and Li.²⁹ Here we extend the approach used by Li²⁹ to model diffraction from crossed gratings made on a thick transparent substrate.

As this has not been presented elsewhere to the best of our knowledge, we briefly outline this method as it applies to our situation. With reference to Fig. 1(a), consider a linearly polarized plane wave of unit amplitude incident on the grating. The expressions for the electric field in the incident and transmitted media are given as

#### (i) Incident medium:
##### (a) Incident field:
$$
\mathbf{E}^{0}(x, y, z)=\left(e_{x}, e_{y}, e_{z}\right) f_{00}(x, y) \exp \left(-j k_{z 0} z\right).
$$

##### (b) Diffracted field:
$$
\begin{aligned}
\mathbf{E}^{i}(x, y, z)= & \sum_{m, n}\left(R_{x m n}, R_{y m n}, R_{z m n}\right) \\
& \times f_{m n}(x, y) \exp \left(j k_{i, z m n} z\right).
\end{aligned}
$$

#### (ii) Transmitted medium:
$$
\begin{aligned}
\mathbf{E}^{t}(x, y, z)= & \sum_{m, n}\left(T_{x m n}, T_{y m n}, T_{z m n}\right) \\
& \times f_{m n}(x, y) \exp \left(-j k_{t, z m n} z\right).
\end{aligned}
$$

Here
$$
\begin{aligned}
\left(e_{x}, e_{y}, e_{z}\right)= & (\cos \psi \cos \theta \cos \phi-\sin \psi \sin \phi, \\
& \cos \psi \cos \theta \sin \phi+\sin \psi \cos \phi, \\
& -\cos \psi \sin \theta), \quad \text { (1a) }
\end{aligned}
$$

![](./images/811971762639077377_1.jpg)

Fig. 1. (a) Definition of the incident angles, (b) labels for the intensities carried by the propagating orders used in the finite-substrate calculations, and (c) on-axis diffraction orders included in the finite-substrate model.

$$
\begin{aligned}
\mathbf{k}^{0} & =\left(k_{x 0}, k_{y 0}, k_{z 0}\right) \\
& =k(\cos \phi \sin \theta, \sin \phi \sin \theta, \cos \phi), \\
f_{m n}(x, y) & \\
& =\exp \left[-j\left(k_{x m} x+k_{y n} y\right)\right], \\
k_{x m} & =k_{x 0}-m \frac{2 \pi}{d_{x}}, \quad k_{y n}=k_{y 0}-n \frac{2 \pi}{d_{y}}, \\
m, n & =0, \pm 1, \pm 2, \ldots,
\end{aligned}
$$

$$
\begin{aligned}
& k_{l, z m n} \\
& \quad= \begin{cases}\left(k^{2} n_{l}^{2}-k_{x m n}^{2}-k_{y m n}^{2}\right)^{1 / 2}, & k^{2} n_{l}^{2} \geqslant\left(k_{x m}^{2}+k_{y n}^{2}\right) \\
-j\left(k_{x m n}^{2}+k_{y m n}^{2}-k^{2} n_{l}^{2}\right)^{1 / 2}, & k^{2} n_{l}^{2}<\left(k_{x m}^{2}+k_{y n}^{2}\right)\end{cases} \\
& \quad \text { for } l=i, t. \quad (2)
\end{aligned}
$$

Here $k=2 \pi / \lambda$, $\lambda$ is the free-space wavelength, $n_i$ and $n_t$ are the indices of the incident and the transmitted media, respectively, and $d_x$ and $d_y$ are the periodicities along the $x$ and $y$ directions, and the definitions of various incident angles are shown in Fig. 1(a). It may be noted that we define the polarization angle $\psi$ such that with $\psi=0$ the electric field lies in the plane of incidence and with $\psi$ $=90$ the electric field is normal to the plane of incidence.

Figure 1(b) shows the various power densities (or intensities) in the incident medium and silicon substrate. Here $I_{00}^i$ is the intensity corresponding to the incident plane-wave illumination, $D_{p q}^s$ is the intensity of the $(p, q)$ propagating order diffracted away from the grating in the substrate, and $I_{p q}^s$ is the intensity of the $(p, q)$ propagating order incident on the grating after reflection from the back of the substrate. Diffraction efficiencies for $I_{00}^i$ corresponding to normal plane-wave illumination are calculated with the electric field polarized along the $x$ axis and taking the silicon substrate to be infinitely thick. The diffraction efficiency for an order diffracted in the substrate resulting from $I_{00}^i$ is denoted as $\eta_{m n}^i$. Similarly, the diffraction efficiencies corresponding to $I_{p q}^s$ are calculated by taking the incident medium to be silicon and with $\theta_{p q}, \phi_{p q}$ as obtained from Eqs. (1) and (2). The polarization angle $\psi_{p q}$ for $I_{p q}^s$ is discussed later in this subsection. Each order $I_{p q}^s$, incident from silicon, results in orders diffracted in silicon with diffraction efficiencies denoted by $\eta_{m n, p q}^s$. Following Ref. 29, we can write the diffracted intensity in the silicon substrate in matrix-vector form as

$$
\mathbf{D}^{s}=\boldsymbol{\eta}^{i} I_{00}^{i}+\eta^{s} \mathbf{I}^{s}. \quad (3)
$$

Here for our case $\mathbf{D}^{s}$ is a vector having components $D_{m n}^s$, i.e., diffracted power density in the $(m, n)$ diffracted order; $I_{00}^i$ is a scalar; $\mathbf{I}^{s}$ is a vector with $I_{p q}^s$ as components; $\boldsymbol{\eta}^{i}$ is the diffraction-efficiency vector with components $\eta_{m n}^i$; and $\eta^{s}$ is the diffraction-efficiency matrix with components $\eta_{m n, p q}^s$. An efficient way to calculate the diffraction-efficiency vector and matrix is to use the scattering-matrix algorithm with full recursion. $^{30}$ We have implemented this algorithm for numerical modeling of crossed gratings.

Now the intensity of the field incident from the silicon substrate $I_{p q}^s$ is simply the product of $D_{p q}^s$ and $\rho_{p q}^s$. Here $\rho_{p q}^s$ is reflectance from the back side of the substrate for the appropriate $\theta_{p q}, \phi_{p q}$, and $\psi_{p q}$. Therefore we can write

$$
\mathbf{D}^{s}=\left(I-\eta^{s} \rho^{s}\right)^{-1} \boldsymbol{\eta}^{i} I_{00}^{i}. \quad (4)
$$

Here $\rho^{s}$ is a diagonal matrix with elements $\rho_{p q}^s$. Once $\mathbf{D}^{s}$ is calculated, the power density in the transmitted medium, consisting only of the zeroth order for the situations considered here, is simply obtained by multiplying $D_{00}^s$ with $\tau_{00}^s$, where $\tau_{00}^s$ is transmittance of the silicon substrate corresponding to $\theta_{00}, \phi_{00}, \psi_{00}=0$.

The evaluation of polarization angle $\psi_{p q}$ for $I_{p q}^s$ requires more careful attention. Unlike the well-known TE-TM case discussed for one-dimensional gratings, $^{28,29}$ plane waves diffracted from two-dimensional periodic structures are, in general, elliptically polarized. For the work discussed in this paper, we confine our attention to first-order diffraction [with orders lying along either the $x$ or the $y$ axis, as shown in Fig. 1(c)], leaving the general case for a future report. The situation shown in Fig. 1(c) is similar to a classically mounted one-dimensional grating with incident TE or TM polarization. Since our incident electric field is polarized along the $x$ axis ($\psi=0$, by our definition), the polarization angle for orders diffracted along the $x$ and $y$ axes will be 0 (TM) and 90 (TE) deg, respectively. So $\psi_{p q}=0$ for $q=0$, and $\psi_{p q}=90$ for $p$ $=0$.

To further study the usefulness of incorporating finite-substrate effects, we model the transmittance spectra of capacitive grids for the 2-5-$\mu$m wavelength range using both the infinite-substrate model (ISM) and the finite-substrate model (FSM). Our numerical simulations show that while the FSM is necessary to compare with the experimental measurements quantitatively, the ISM captures the essential features of the transmittance spectra.

In this paper, because of computational constraints, we use the simpler ISM to numerically study the behavior of crossed gratings and use the FSM whenever we compare the numerical modeling with the experimental measurements.

### C. Convergence of the Numerical Model

Our RCWA-based numerical model incorporates the changes suggested by $\mathrm{Li}^{11}$ to improve the convergence of the algorithm. We now discuss the convergence behavior of this algorithm for the ISM and the FSM.

For normal plane-wave illumination in the ISM, we take advantage of the symmetry of the configuration $^{31}$ to reduce the numerical size of the problem. Specifically, for normal incidence, the equivalence of the positive and negative Fourier coefficients allows reduction of the size of the matrix in the eigenvalue problem from $2(2 N$ $+1)^{2}$ by $2(2 N+1)^{2}$ to $2(N+1)^{2}$ by $2(N+1)^{2}$, where $N$ is the number of positive or negative spatial harmonics for both the dielectric function and the field expansion. This reduction allows the algorithm to be implemented on a personal computer for reasonably high values of $N$.

Validating the performance of any numerical algorithm is an essential part of establishing the utility of the algorithm. Unlike the situation for one-dimensional gratings in which the convergence properties of RCWA for metallic

gratings have been well established, $^{32,33}$ little is known of the behavior of two-dimensional RCWA algorithms. First, we considered energy balance and reciprocity as well-known criteria for the accuracy of our numerical model and indicative of the convergence error. $^{23}$ Our model satisfies the energy-balance criterion to machine precision for lossless crossed gratings, and we find the error in reciprocity to be within 1% for square lattices having rectangular metallic scatterers. These checks are necessary but not sufficient criteria to guarantee the accuracy of the numerical model. $^{17,34}$

To further study the convergence of the numerical model, we also analyzed the behavior of diffraction efficiency in a given diffracted order versus number of retained spatial harmonics. This pragmatic approach has been used previously. $^{11}$ Toward this end, we examined the numerically calculated diffraction efficiency for the transmitted zeroth order of capacitive grids as a function of the mode number $N$ up to the maximum number of modes as allowed by our computational resources. Figure 2 shows the results for the case of circular scatterers. As may be noted from the figure, the change in diffraction efficiency from $N = 14$ to $N = 15$ is approximately 2% for this particular set of grating parameters. For the range of grating parameters considered here, we expect the diffraction efficiency to vary similarly as a function of $N$. In the results shown in this paper we have used $N = 15$ for numerical modeling of the ISM.

For the FSM, the diffraction orders propagating in the substrate are obliquely incident on the grating from the substrate side. The grating configuration in this case is no longer symmetric, and, unlike for the ISM, we cannot reduce the numerical size of the eigenvalue problem. We expect the convergence error to be larger in the FSM as computational constraints require use of a smaller value of $N$, limited to 10 in our situation. For the same parameters used in the ISM, Fig. 2 shows that the change in diffraction efficiency from $N = 9$ to $N = 10$ is approximately 5%. Given the lack of rigorous criteria to evaluate convergence for the RCWA algorithm, we assume that the error will behave similarly for other grating parameters. However, the ultimate validation of the two-dimensional RCWA is measured by its agreement with the experimental results presented later in this paper.

![](./images/811971762639077377_2.jpg)

Fig. 2. Convergence behavior of the ISM and the FSM for circular gold scatterers placed on a silicon substrate. The wavelength $\lambda$ of the normally incident illumination is $4.3\ \mu$m, and, referring to the inset, $\Lambda = 1.24\ \mu$m, $d = 0.6\ \mu$m, $h = 0.1\ \mu$m, and the index of gold at $\lambda = 4.3\ \mu$m is (2.94, $-$26.45). A 100 $\times$ 100 grid is used to approximate the periodic unit cell.

## 4. SURFACE PLASMA WAVES AND CROSSED GRATINGS

Surface plasma wave phenomena associated with one-dimensional gratings have been extensively studied. $^{23,35}$ For modest-depth gratings, two related phenomena are observed as a function of wavelength: (1) A redistribution of energy as a diffraction order switches from propagating to evanescent (Wood's anomalies at $\lambda = \Lambda/m$, where $\lambda$ is the wavelength, $\Lambda$ is the grating period, and $m$ is the appropriate grating order), which typically appears as a cusp in the energies in the various orders; (3) a resonant coupling to the surface plasma wave (taking energy out of the propagating orders) at a wavelength slightly longer than Wood's anomaly wavelength. Whereas the position of the cusp is set by the diffraction equation and is independent of the material details, the SPW coupling resonance position, strength, and linewidth depends on both the grating and the material parameters (for a review, see Petit $^{23}$ and Hessel and Oliner $^{36}$).

It has been experimentally $^{6}$ demonstrated that inductive grids, or metal films perforated with subwavelength hole arrays, have a higher transmittance than that predicted by single-aperture theory. $^{37}$ Transmittance efficiencies showing a 1000-fold increase $^{37}$ are observed in subwavelength inductive grids when compared with the results of single-aperture theory. This phenomenon is attributed to the resonant coupling of the incident light to the SPW. The wavelength at which SPW coupling occurs is described by wave-vector conservation, which is a kinematic model that is essentially identical to that used successfully in the one-dimensional grating case. This model, which gives the in-plane momentum necessary to couple to SPWs, explains the wavelength-dependent features of the experimental data. However, a detailed analysis of the magnitude and variation of the coupling requires a rigorous diffraction model. We apply both the kinematic model and RCWA to study metallic crossed gratings.

To illustrate, consider first the surface plasma wave equation that gives the momentum-conservation condition necessary to couple normally incident radiation to an infinite metal sheet $^{38}$:
$$
k_{\parallel} = \frac{2\pi}{\lambda}\text{Re}\left( \frac{\epsilon_{\text{me}}\epsilon_{\text{d}}}{\epsilon_{\text{me}} + \epsilon_{\text{d}}} \right)^{1/2}. \tag{5}
$$

Here $k_{\parallel}$ is the projection of the incident wave vector parallel to the dielectric-metal interface, $\lambda$ is the wavelength of incident light, and $\epsilon_{\text{me}}$ and $\epsilon_{\text{d}}$ are the complex permittivities of the metal and the incident medium, respectively. A metal film periodically perforated with holes can be considered as a perturbation of smooth metal film, and Eq. (5) may be used to determine the coupling to surface plasma waves for inductive grids. For the special

case of a square lattice and normally incident radiation,
$k_{\parallel}$ is given as $(2\pi/\Lambda)(m^{2}+n^{2})^{1/2}$, where $\Lambda$ is the pitch of
the grating and $m$, $n$ are integers (at least one of which is
nonzero). Substituting into Eq. (5), we get$^{37}$

$$
\frac{\lambda_{m,n}}{\Lambda} = \frac{1}{(m^{2}+n^{2})^{1/2}} \mathrm{Re} \left[ \frac{\epsilon_{\mathrm{me}} \epsilon_{\mathrm{d}}}{(\epsilon_{\mathrm{me}} + \epsilon_{\mathrm{d}})} \right]^{1/2}. \tag{6}
$$

The dielectric medium in this equation is either the su-
perstrate (assumed to be air) or the substrate (silicon).
The air-metal interface and the substrate-metal inter-
face will each provide a set of $(m,n)$ for Eq. (6) corre-
sponding to air-metal SPW coupling and substrate-
metal SPW coupling.$^{39}$

As noted above, a phenomenon closely associated with
the appearance of SPW coupling in metallic gratings is
known as Wood's anomaly.$^{40}$ This is the condition in
which the wave vector of a given grating order becomes
tangent to the grating plane and is marked by rapid
variations in the intensity of the remaining orders. The
wavelength condition for Wood's anomalies for normally
incident illumination on a crossed grating is given as$^{37}$

$$
\frac{\lambda_{m,n}}{\Lambda} = \left[ \frac{\epsilon_{\mathrm{d}}}{(m^{2}+n^{2})} \right]^{1/2}. \tag{7}
$$

Here $\epsilon_{\mathrm{d}}$ is the permittivity of the superstrate or substrate,
and, accordingly, the air and silicon interfaces each give a
set of Wood's anomalies. From Eqs. (6) and (7), it may be
noted that for metallic gratings where $|\epsilon_{\mathrm{me}}| \gg \epsilon_{\mathrm{d}}$ the
wavelength conditions for SPW coupling and Wood's
anomalies are extremely close.

Now let us consider the case of a patterned gold film on
a silicon substrate with a pitch of $1.2\ \mu\mathrm{m}$. Equation (6)
predicts coupling to the $(0,\pm1)$ or $(\pm1,0)$ substrate-metal
SPW at $\lambda = 4.16\ \mu\mathrm{m}$. The results of the RCWA model
for inductive grids are presented in Fig. 3, which shows
the transmittance and absorptance of a grid with a thick-
ness of $0.1\ \mu\mathrm{m}$ and a square air aperture of $0.36\ \mu\mathrm{m}^{2}$.
The absorptance $A$ is simply given by

$$
A = 1 - \sum_{d} R_{d} - \sum_{d} T_{d}. \tag{8}
$$

where $R_{d}$ and $T_{d}$ are the diffraction efficiencies for order
$d$ in the incident and the transmitted media, respectively.
The modeling presented in this figure takes the substrate
to be infinite, includes the dispersion of the dielectric
function of gold,$^{41}$ and takes the index of silicon to be 3.44
for a $2$-$5$-$\mu\mathrm{m}$ wavelength range. Also, the transmittance
is defined to be the sum of diffraction efficiencies in all the
transmitted orders. Figure 3 also shows the absorptance
of a homogeneous $0.1$-$\mu\mathrm{m}$-thick gold film on a silicon sub-
strate; the difference between the absorptance spectra of
the inductive grid and a gold film is indicative of the
power carried by SPWs. From Fig. 3 it may be seen that
the SPW wavelength as calculated from Eq. (6) matches
the rigorous diffraction model well, although the exact
wavelengths of SPW coupling are offset slightly from
those given by Eq. (6) [e.g., for the $(0,1)$ substrate-metal
coupling, the transmittance reaches a maximum at $\lambda$
$= 4.28\ \mu\mathrm{m}$ instead of $\lambda = 4.16\ \mu\mathrm{m}$]. Note that we take
the transmittance maximum as the SPW coupling
wavelength.$^{39}$ A possible reason for this wavelength dif-
ference as obtained from wave-vector conservation [Eq.
(6)] and RCWA is the fact that Eq. (6) is a perturbation on
the SPW dispersion relation for homogeneous metal films
and therefore can describe the SPW coupling wavelength
only approximately. Also shown in Fig. 3 are examples of
the air-metal SPW (denoted by solid vertical lines),
substrate-metal SPW (shown by solid vertical lines), and
Wood's anomalies for the incident and transmitted media
(denoted by dashed vertical lines). For the case of induc-
tive grids, we generally observe well-defined transmit-
tance minima and maxima corresponding to Wood's
anomalies and SPW coupling, respectively.$^{39}$

![](./images/811971762639077377_3.jpg)

Fig. 3. Transmittance and SPW coupling for an inductive grid
with square air holes in gold on a silicon substrate. Referring to
the inset, $\Lambda = 1.2\ \mu\mathrm{m}$, $d = 0.6\ \mu\mathrm{m}$, and $h = 0.1\ \mu\mathrm{m}$. Wave-
length resolution for the numerical modeling is $0.02\ \mu\mathrm{m}$, and the
index of silicon is taken as 3.44, independent of wavelength.
The locations of SPW coupling for air-metal and silicon-metal
are obtained from Eq. (6) and are labeled by solid vertical lines.
The locations of Wood's anomalies are obtained from Eq. (7) and
are labeled by dashed vertical lines. Also shown in the figure is
the absorptance of a $0.1$-$\mu\mathrm{m}$-thick gold film on a silicon substrate.

We now study the applicability of the kinematic model
to capacitive grids. Clearly, some additional evidence is
necessary to apply Eq. (6), as, unlike the inductive grids
in which a continuous metal film periodically perforated
with holes allows for extended conduction, the capacitive
grids are metal islands having no conduction between
them. It remains to be shown that SPWs are established
in capacitive grids.

One of the important features of SPWs is the energy
carried by these surface waves near the coupling wave-
lengths. This is evident for inductive grids in Fig. 3, in
which we observe maxima in the absorptance spectrum
near the location of SPW coupling. Figure 3 also shows
that the energy carried by the SPW occurs in a narrow
spectral band. Furthermore, the features associated
with Wood's anomalies and SPW coupling affect the
transmittance spectrum differently; Wood's anomalies oc-
cur as minima in transmittance, whereas SPW coupling
occurs as maxima in transmittance. Also note that the
wavelengths of Wood's anomalies [as defined by Eq. (7)]
and of the SPW coupling [as defined by Eq. (6)] are almost
superimposed. We now examine the absorptance spec-
trum of capacitive grids. Figure 4 shows the transmit-

![](./images/811971762639077377_4.jpg)

Fig. 4. Transmittance and SPW coupling for a capacitive grid with square gold scatterers on a silicon substrate. Referring to the inset, $\Lambda = 1.2\ \mu\text{m}$, $d = 0.6\ \mu\text{m}$, and $h = 0.1\ \mu\text{m}$. The wavelength resolution of numerical modeling is $0.02\ \mu\text{m}$, and the index of silicon is taken as 3.44 for all wavelengths. The locations of SPW coupling for air-metal and silicon-metal are obtained from Eq. (6) and are labeled by solid vertical lines. The locations of Wood's anomalies are obtained from Eq. (7) and are labeled by dashed vertical lines. Apart from the (0, 1) substrate-metal SPW, coupling to higher-order SPWs is quite weak for this particular capacitive grid and is only visible as discontinuity in the slope of the transmittance spectrum. Also shown is the absorptance of $0.1$-$\mu\text{m}$-thick gold film on a silicon substrate.

tance and absorptance for a capacitive grid having a pitch of $\Lambda = 1.2\ \mu\text{m}$ and a grating thickness of $0.1\ \mu\text{m}$ with square gold scatterers of area $0.36\ \mu\text{m}^2$. From the absorptance curve in Fig. 4, we observe SPW-like features near the (0, 1) substrate-metal coupling; also, in contrast to the previous inductive grid, the energy carried by these plasmalike waves is spread over a wider spectral band, which may be indicative of high damping of these plasmalike waves. The transmittance spectrum of this capacitive grid, unlike that of the inductive grid, does not show well-defined minima and maxima near the locations of Wood's anomalies and of SPW coupling, respectively. Instead, the features associated with Wood's anomalies and SPWs influence the transmittance spectrum in a similar manner; they are characterized either by a minimum in the transmittance spectrum [as shown in Fig. 4 for (0, 1) substrate-metal coupling] or by points of inflection in the transmittance spectrum (as shown in Fig. 4 for higher-order substrate-metal coupling). The absorptance spectrum of the capacitive grid shows a maximum that suggests its behavior may be described in terms of SPW coupling.

## 5. CAPACITIVE AND INDUCTIVE GRIDS

From Figs. 3 and 4, we observe that surface plasma wave features occur for both capacitive and inductive grids. We experimentally verify our modeling by fabricating inductive and capacitive grids of the same pitch and grating thickness. The transmittance spectra for these structures are shown in Figs. 5 and 6 along with the results of numerical computations. Here in the numerical model we are taking into account the finite thickness of the silicon substrate (FSM). The FSM has a larger convergence error than the ISM; furthermore, the size of the circular scatterers is determined by scanning electron microscopy (SEM), which also introduces some measurement error. To account for these factors, we carry out a mean-square fit between the experimental and the numerical data. Whereas the numerical model assumes illumination with a normally incident, linearly polarized plane wave, experimental characterization of inductive and capacitive grids is done with an unpolarized source in the FTIR.

![](./images/811971762639077377_5.jpg)

Fig. 5. Comparison between experimental and rigorous modeling results for transmission through an inductive grid of circular air holes in gold on a silicon substrate. Here $\Lambda = 1.24\ \mu\text{m}$, $h = 0.1\ \mu\text{m}$, and the air-hole diameter obtained from both the SEM measurement and the mean square fitting of the numerical model to the data is $0.40\ \mu\text{m}$. The wavelength step used for the numerical modeling is $0.025\ \mu\text{m}$, and modeling is limited to the wavelength region in which only the on-axis diffraction orders propagate in the silicon substrate. A $100\times 100$ grid is used to approximate the periodic unit cell.

![](./images/811971762639077377_6.jpg)

Fig. 6. Experimental and rigorous modeling results for transmittance through a capacitive grid of circular gold scatterers on a silicon substrate. Here $\Lambda = 1.24\ \mu\text{m}$, $h = 0.1\ \mu\text{m}$, and the diameters of the gold scatterers obtained from the SEM measurement is $0.76\ \mu\text{m}$ and from the mean-square fitting of the numerical model to the experimental data is $0.75\ \mu\text{m}$. The wavelength resolution for the numerical model is $0.025\ \mu\text{m}$, and modeling is done for the on-axis diffraction orders propagating in the silicon substrate. A $100\times 100$ grid is used to approximate the periodic unit cell.

The transmittance or reflectance spectra of square lattices under normal plane-wave illumination are polarization independent. $^{2}$

Figures 5 and 6 show that the experiment and the numerical model are in reasonably good agreement. Furthermore, the inductive and capacitive grids display surface plasma wave features at approximately the same wavelengths, but the strength and shape of surface plasma wave coupling is quite different for each of them. For inductive grids the amount of light transmitted away from the SPW resonance is small, and changes in the transmittance spectrum are sharp and narrow at the coupling wavelengths. In contrast, in capacitive grids we note a gradual change in transmittance near the wavelengths of SPW coupling. One of the reasons is a dependence on the grid fill factor for capacitive and inductive grids, $\mathrm{FF}_{C}$ and $\mathrm{FF}_{I}$, defined as

$$
\mathrm{FF}_{C}=\frac{\pi}{4}\left(\frac{d}{\Lambda}\right)^{2} \tag{9}
$$

for circular scatterers in capacitive grids and as

$$
\mathrm{FF}_{I}=1-\frac{\pi}{4}\left(\frac{d}{\Lambda}\right)^{2} \tag{10}
$$

for circular air holes in an inductive grid. Here $d$ is the diameter of circular scatterers for capacitive grids or of the air holes for inductive grids. The structures shown in Figs. 5 and 6 have a fill factor of $91.8\%$ for the inductive grid and $29.5\%$ for the capacitive grid. Also, for this particular inductive grid (shown in Fig. 5), the absolute efficiency of transmittance (obtained by dividing the fraction of light transmitted by the fraction of the surface area occupied by holes) $^{6}$ at positions of maxima is $\sim 0.25$. This is much less than that observed by Ebbesen et al. $^{6}$ for the case of subwavelength hole arrays in silver films made on a quartz substrate. This apparent discrepancy is a candidate for further study, although one of the reasons for the discrepancy may be the high-index silicon substrate used in this study. For the capacitive grid (shown in Fig. 6), it may be noted the wavelength location of the SPW coupling is offset between the experimental data and the numerical modeling; this difference is attributed to convergence error in the FSM.

## 6. FILL FACTOR STUDY

We experimentally and numerically investigated the dependence of the $(0,1)$ substrate-metal SPW coupling as a function of the fill factor for capacitive grids. All samples were $0.1$-$\mu$m-thick circular gold scatterers on a silicon substrate and had a pitch of $1.24$ $\mu$m. Figure 7 shows the dependence of the experimental and the numerical transmittance at $\lambda = 4.3$ $\mu$m on the fill factor. For the modeling, the fill factor is varied by our changing the diameter of circular gold scatterers from $0.4$ to $0.9$ $\mu$m in steps of $0.05$ $\mu$m. Numerical modeling for capacitive grids of different fill factors is done by use of the FSM, and a mean-square fit was not performed for the modeled and experimental measurements. SEM measurements are done to determine the size of the circular gold scatterers, and the transmittance spectra are obtained by use of FTIR. We note from Fig. 7 that the convergence error in the FSM appears as discontinuous variations in the slope of the numerically calculated transmittance. Nevertheless, the model and the experiment display the same trend, specifically, transmittance through the grid at the wavelength of the $(0,1)$ substrate-metal SPW coupling ($\lambda = 4.3$ $\mu$m in this case) decreases monotonically with fill factor.

![](./images/811971762639077377_7.jpg)

Fig. 7. Experimental and numerically calculated dependence of transmittance through a capacitive grid with the fill factor. The transmittance is shown for the case of $(0,1)$ substrate-metal SPW coupling at $\lambda = 4.3$ $\mu$m. Referring to the inset in Fig. 4, the fill factor for a capacitive grid is given as $(\pi/4)(d/\Lambda)^{2}$. The grid consisted of circular gold scatterers on a silicon substrate and had a pitch of $1.24$ $\mu$m and a thickness of $0.1$ $\mu$m. A $100$ $\times$ $100$ grid is used to approximate the periodic unit cell. Note the noise in numerically calculated transmittance that is due to convergence error in the FSM. The insets in the figure also show SEM images of capacitive grids with fill factors of (a) $10.8\%$, (b) $19.6\%$, and (c) $34.3\%$.

## 7. CONCLUSION

We have experimentally validated numerical results based on RCWA for metallic inductive and capacitive grids in the mid-IR. We find that the features in the transmittance spectrum of both inductive and capacitive grids are defined by coupling to surface plasma waves and that the RCWA algorithm adequately describes both the position and the magnitude of these features. A systematic study of the behavior of capacitive grids as a function of fill factor showed that transmittance decreases monotonically with fill factor at the wavelength of SPW coupling.

## ACKNOWLEDGMENTS

This research was supported by the Defense Advanced Research Projects Agency. B. Minhas thanks Lifeng Li of Tsinghua University, China, and Pasi Vahimaa of the University of Joensuu, Finland, for help with the debugging stage of the diffraction code.

## REFERENCES

1. T. K. Wu, “Frequency selective surface and grid array,” in Wiley Series in Microwave and Optical Engineering (Wiley, New York, 1995).

2. R. Ulrich, "Far-infrared properties of metallic mesh and its complementary structure," Infrared Phys. **7**, 37–55 (1967).

3. S. Peng and G. M. Morris, "Experimental demonstration of resonant anomalies in diffraction from two-dimensional gratings," Opt. Lett. **21**, 549–551 (1996).

4. S. Peng and G. M. Morris, "Resonant scattering from two-dimensional gratings," J. Opt. Soc. Am. A **13**, 993–1005 (1996).

5. C. M. Horwitz, "A new solar selective surface," Opt. Commun. **11**, 210–212 (1974).

6. T. W. Ebbesen, H. J. Lezec, H. F. Ghaemi, T. Thio, and P. A. Wolff, "Extraordinary optical transmission through sub-wavelength hole arrays," Nature **391**, 667–669 (1998).

7. A. Heinzel, V. Boerner, A. Gombert, B. Blasi, V. Wittwer, and J. Luther, "Radiation filters and emitters for the NIR based on periodically structured metal surfaces," J. Mod. Opt. **47**, 2399–2419 (2000).

8. L. Martin-Moreno, F. J. Garcia-Vidal, H. J. Lezec, K. M. Pellerin, T. Thio, J. B. Pendry, and T. W. Ebbesen, "Theory of extraordinary optical transmission through sub-wavelength hole arrays," Phys. Rev. Lett. **86**, 1114–1117 (2001).

9. E. Popov, M. Nevière, S. Enoch, and R. Reinisch, "Theory of light transmission through subwavelength periodic hole arrays," Phys. Rev. B **62**, 16100–16108 (2000).

10. M. G. Moharam, E. B. Grann, and D. A. Pommet, "Formulation for stable and efficient implementation of the rigorous coupled-wave analysis of binary gratings," J. Opt. Soc. Am. A **12**, 1068–1076 (1995).

11. L. Li, "New formulation of the Fourier modal method for crossed surface-relief gratings," J. Opt. Soc. Am. A **14**, 2758–2767 (1997).

12. R. C. McPhedran, D. H. Dawes, L. C. Botten, and N. A. Nicorovici, "On-axis diffraction by perfectly conducting capacitive grids," J. Electromagn. Waves Appl. **10**, 1085–1111 (1996).

13. L. C. Botten, R. C. McPhedran, N. A. Nicorovici, and A. B. Movchan, "Off-axis diffraction by perfectly conducting capacitive grids: modal formulation and verification," J. Electromagn. Waves Appl. **12**, 847–882 (1998).

14. X. Chen, S. H. Zaidi, and S. R. J. Brueck, "Interferometric lithography of sub-micrometer sparse hole arrays for field-emission display applications," J. Vac. Sci. Technol. B **14**, 3339–3349 (1996).

15. E. Noponen and J. Turunen, "Eigenmode method for electromagnetic synthesis of diffractive elements with three-dimensional profiles," J. Opt. Soc. Am. A **11**, 2494–2502 (1994).

16. R. Brauer and O. Bryngdahl, "Electromagnetic diffraction analysis of two-dimensional gratings," Opt. Commun. **100**, 1–5 (1993).

17. S. Peng and G. M. Morris, "Efficient implementation of rigorous coupled-wave analysis for surface-relief gratings," J. Opt. Soc. Am. A **12**, 1087–1096 (1995).

18. M. G. Moharam, "Coupled-wave analysis of two-dimensional dielectric gratings," in *Holographic Optics: Design and Applications*, I. Cindrich, ed., Proc. SPIE Proc. SPIE **883**, 8–11 (1988).

19. C.-C. Chen, "Transmission through a conducting screen perforated periodically with apertures," IEEE Trans. Microwave Theory Tech. **18**, 627–632 (1970).

20. R. Mittra, C. H. Chan, and T. Cwik, "Techniques for analyzing frequency selective surfaces—a review," Proc. IEEE **76**, 1593–1615 (1988).

21. R. C. McPhedran and D. Maystre, "On the theory and solar application of inductive grids," Appl. Phys. **14**, 1–20 (1977).

22. G. H. Derrick, R. C. McPhedran, D. Maystre, and M. Nevi`ere, "Crossed gratings: a theory and its applications," Appl. Phys. **18**, 39–52 (1979).

23. R. Petit, *Electromagnetic Theory of Gratings*, Vol. 22 of *Topics in Current Physics* (Springer-Verlag, Berlin, 1980).

24. B. Harris, T. W. Preist, J. R. Sambles, R. N. Thorpe, and R. A. Watts, "Optical response of bigratings," J. Opt. Soc. Am. A **13**, 2041–2049 (1996).

25. P. Vincent, "A finite-difference method for dielectric and conducting crossed gratings," Opt. Commun. **26**, 293–296 (1978).

26. O. P. Bruno and F. Reitich, "Numerical solution of diffraction problems: a method of variation of boundaries. III. Doubly periodic gratings," J. Opt. Soc. Am. A **10**, 2551–2562 (1993).

27. V. Kettunen, M. Kuittinen, J. Turunen, and P. Vahimaa, "Spectral filtering with finitely conducting inductive grids," J. Opt. Soc. Am. A **15**, 2783–2785 (1998).

28. N. Chateau, J. P. Hugonin, B. Guldimann, and P. Chavel, "Two-wave diffraction of quasi-monochromatic light by a volume grating deposited on a thick transparent plate," Opt. Commun. **103**, 444–452 (1993).

29. L. Li, "Calculation of diffraction efficiencies of a grating made on a thick transparent plate," Opt. Commun. **160**, 15–21 (1999).

30. L. Li, "Formulation and comparison of two recursive matrix algorithms for modeling layered diffraction gratings," J. Opt. Soc. Am. A **13**, 1024–1035 (1996).

31. P. Lalanne and D. Lemercier-Lalanne, "On the effective medium theory of subwavelength periodic structures," J. Mod. Opt. **43**, 2063–2085 (1996).

32. L. Li and C. W. Haggans, "Convergence of the coupled-wave method for metallic lamellar diffraction gratings," J. Opt. Soc. Am. A **10**, 1184–1189 (1993).

33. P. Lalanne and G. M. Morris, "Highly improved convergence of the coupled-wave method for TM polarization," J. Opt. Soc. Am. A **13**, 779–784 (1996).

34. R. Petit and G. Tayeb, "On the use of the energy balance criterion as a check of validity of computations in grating theory," *Application and Theory of Periodic Structures, Diffraction Gratings, and Moire Phenomena III*, J. M. Lerner, ed., Proc. SPIE **815**, 2–10 (1988).

35. M. C. Hutley, *Diffraction Gratings* (Academic, New York, 1982).

36. A. Hessel and A. A. Oliner, "A new theory of Wood's anomalies on optical gratings," Appl. Opt. **4**, 1275–1297 (1965).

37. T. J. Kim, T. Thio, T. W. Ebbesen, D. E. Grupp, and H. J. Lezec, "Control of optical transmission through metals perforated with subwavelength hole arrays," Opt. Lett. **24**, 256–258 (1999).

38. H. Raether, *Surface Plasmons on Smooth and Rough Surfaces and on Gratings* (Springer-Verlag, Berlin, 1988).

39. T. Thio, H. F. Ghaemi, H. J. Lezec, P. A. Wolff, and T. W. Ebbesen, "Surface-plasmon-enhanced transmission through hole arrays in Cr films," J. Opt. Soc. Am. B **16**, 1743–1748 (1999).

40. R. W. Wood, "On a remarkable case of uneven distribution of light in a diffraction grating spectrum," Philos. Mag. **4**, 396–402 (1902).

41. E. D. Palik, *Handbook of Optical Constants of Solids*, Academic Press Handbook Series (Academic, Orlando, Fla., 1985).