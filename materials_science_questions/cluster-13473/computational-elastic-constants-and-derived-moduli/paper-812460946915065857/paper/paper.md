# On the stability of global non-radial pulsations of neutron stars

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1999 J. Phys. G: Nucl. Part. Phys. 25 107

(http://iopscience.iop.org/0954-3899/25/1/010)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

---

Download details:

IP Address: 137.149.200.5
This content was downloaded on 29/08/2015 at 05:18

Please note that [terms and conditions apply]().

# On the stability of global non-radial pulsations of neutron stars

S I Bastrukov†, F Weber‡ and D V Podgainy†

† Computer Physics Division, LCTA, Joint Institute for Nuclear Research, 141980 Dubna, Russia
‡ Institute for Theoretical Physics, University of Munich, Theresienstrasse 37/III, Munich 80333, Germany

Received 3 November 1997, in final form 14 October 1998

**Abstract.** A neutron star is the cosmic nuclear object in which the energy of gravitational pull is brought to equilibrium by elastic energy stored in the neutron Fermi-continuum. Evidence for the viscoelastic behaviour of a stellar nuclear matter provides a seismological model of pulsar glitches interpreted as a sudden release of the elastic energy. In laboratory nuclear physics, the signatures of viscoelasticity of nuclear matter are found in the current investigations on the collective nuclear dynamics, in which a heavy nucleus is modelled by a spherical piece of viscoelastic Fermi-continuum compressed to the normal nuclear density. It is plausible to expect, therefore, that the motions of self-gravitating nuclear matter constituting the interior of neutron stars should be governed by the equations of an elastic solid, rather than by hydrodynamic equations describing the behaviour of gaseous plasma inside the main sequence stars. In this paper, we present arguments that elastodynamic equations, originally introduced in the context of nuclear collective dynamics, can provide a proper account of elasticity in the large scale motions of neutron matter under its own gravity. Emphasis is placed on mathematical physics underlying the constructive description of the continuum mechanics and the rheology of macroscopic nuclear matter. The capability of the elastodynamic approach is examined by analysis of oscillatory dynamics of a neutron star in the standard homogenous model, operating with a spherical mass of self-gravitating degenerate neutron matter whose viscoelastic behaviour is described in terms of the spheroidal and torsional gravitational-elastic eigenmodes, inherenly related to viscoelasticity. The energy variational principle is utilized to compute the frequencies of viscoelastic gravitational pulsations and their relaxation time. The method is demonstrated for both the idealized homogeneous model and the neutron star models constructed on realistic equations of state. Finally, we derive analytic conditions for the stability of a neutron star to linear elastic deformations accompanying the non-radial pulsations, and discuss the fingerprints of these pulsations in the electromagnetic activity of radiopulsars.

## 1. Introduction

Initiated by the discovery of the first pulsar in 1967 by Hewish *et al* [1], which was interpreted shortly afterwards as a rapidly-spinning strongly-magnetized neutron star, considerable attention has been devoted since then to the study of these cosmic nuclear objects. Today, it is known that neutron stars and white dwarfs constitute probably only two end products in stellar evolution [2–9] which may coexist with another family of collapsed stars made up of strange quark matter. The latter family comprises objects known as compact strange stars [10] and strange dwarfs [11]. Over the years, substantial progress has been achieved in understanding equilibrium properties of self-gravitating hadronic matter (compressed a few times higher than normal nuclear density) constituting the interior of the above sequence of degenerate compact stars [12, 13]. The development of quantitative methods for an adequate

description of the continuum mechanics of condensed matter inside collapsed stars forms an important part in their contemporary study.

With our current knowledge of physics, it is difficult to comprehend that the continuum mechanics of highly-compressed degenerate matter obeys the same hydrodynamic laws of motion as a dilute gaseous plasma inside the main sequence stars. Instead, it is to be expected that the dynamic behaviour of degenerate condensed matter in collapsed stars obeys the laws of motions of an extremely rigid elastic solid. The evidence is provided by the electromagnetic activity of fairly well studied variable white dwarfs, whose temporal variability is associated with non-radial pulsations [5]. In particular, the hundred-second variability of some white dwarfs can be assigned, as suggested in [14, 15], to possible torsional vibrations. From the continuum theory, it is known that torsional oscillations are the most prominent manifestation of elasticity of solid material continuum [16, 17].

The discovery of elastic properties in the behaviour of macroscopic nuclear matter is one of the major landmarks in the current development of both the astrophysics of neutron stars and laboratory nuclear physics. In astrophysics, this understanding has come after observation of jump-like irregularities in pulsed radioemission of neutron stars, known in the literature as glitches. The most plausible suggestion explaining the above restless behaviour of pulsars (such as Vela and Crab) underlies the starquake model interpreting the pulsar glitch as a manifestation of a seismological activity of the neutron star or, more specifically, as a sudden release of elastic and gravitational energies [18-20] (see also [2,4,6,7]). This attitude unambiguously exhibits the fact that a neutron star is a substantial reservoir of elastic and gravitational energies brought to equilibrium [20]. Besides, the presence of a highly intensive magnetic field in the nuclear stellar matter imparts to it a supplementary portion of elastic rigidity [21] which is manifested by Alfvén's essentially transverse oscillations typical of elastodynamic behaviour [22, 23].

In laboratory nuclear physics the elastodynamic behaviour of macroscopic nuclear matter has been understood after the discovery of isoscalar giant multipole resonances to be a common feature of nuclear collective response. Theoretical investigations performed in this direction over the past two decades (see, for instance, [24-37] and references therein) have brought clear insight into the quantum nature of elasticity of nuclear matter. The governing equations modelling macroscopic dynamics of nuclear matter, formulated in the above investigations (reviewed below), reflect strong correlation between the evolution of intrinsic material stresses in the bulk and distortions of the Fermi-distribution in momentum space. In particular, spherically-symmetric distortions of the Fermi-sphere are found to be associated with intrinsic stresses in the compressible Fermi-continuum, resulting in the capability of transmitting zero- temperature longitudinal waves (behaviour typical of both the Fermi-fluid and elastic Fermi- solid). The most important finding of the above investigations is that the incompressible degenerate nuclear matter possesses a shear resistivity which is exhibited by the capability of transmitting a pure transverse zero-temperature wave. The transverse mode demonstrates elastodynamic behaviour of essentially anisotropic intrinsic stresses whose appearance is inherently related with quadrupole deformation of the Fermi-sphere—a feature unique for the elastic Fermi-solid. As we have mentioned, these observations have first been made in the study of nuclear giant resonances whose integral characteristics display a regular mass-number dependence. By modelling a heavy nucleus by a small piece of spin and isospin saturated incompressible Fermi-continuum, it was established that empirical data can be adequately described under the assumption that in the process of resonant response the expenditure of nuclear elastic energy, stored by a nuclear mean field in the shell-structured ordering of nucleons, proceeds by quadrupole deformation of the Fermi-sphere preserving the original single-particle ordering. Induced quadrupole deformations of the Fermi-sphere in the momentum space is accompanied by shear elastic stresses in bulk, and electromagnetic

relaxation of such an elastic response is detected in the nuclear spectrum as a giant isoscalar resonance. The physical significance of this model is that it teaches us how the nucleus can be used to uncover dynamical properties of macroscopic nuclear matter. This model operates with a small spherical mass of radius $R$ of a viscoelastic Fermi-continuum compressed to the normal nuclear density, $\rho$. The elastic shear resistivity is characterized by the shear modulus $\mu=(1/5)\rho v_F^2$ where the Fermi-velocity $v_F$ is taken from the model of a nucleonic Fermi-gas degenerate in spin and isospin. Giant electric $(EL)$ and magnetic $(ML)$ resonances of the multipole order $L\geqslant2$ are described in terms of spheroidal and torsional non-radial vibrations, and their damping as a resultant of shear viscosity whose efficiency is measured by the coefficient of dynamic viscosity, $\eta$. Analytic estimates for the energy, $E=\hbar\omega$, uniquely determined by the frequency of spheroidal $\omega_s$ and torsional $\omega_s$ modes and spread width $\Gamma$ which is determined (in accordance with the uncertainty principle: $\Gamma\cdot\tau=\hbar$) by relaxation time $\tau_s$ and $\tau_t$ are given by

$$
\begin{align*}
E(EL)&=\hbar\omega_s & \omega_s&=\omega_F[(2/5)(2L+1)(L-1)]^{1/2} \\
\Gamma(EL)&=\frac{\hbar}{\tau_s} & \tau_s&=\frac{2}{5}\tau\left(\frac{\omega_F}{\omega_s}\right)^2 \\
E(ML)&=\hbar\omega_t & \omega_t&=\omega_F[(1/5)(2L+3)(L-1)]^{1/2} \\
\Gamma(ML)&=\frac{\hbar}{\tau_t} & \tau_t&=\frac{2}{5}\tau\left(\frac{\omega_F}{\omega_t}\right)^2 \\
\tau&=\frac{\rho R^2}{\eta} & \omega_F&=\left[\frac{5\mu}{\rho R^2}\right]^{1/2}=\frac{v_F}{R}.
\end{align*}
\tag{1.1}
$$

The resultant scaling estimates for the energy $E\sim A^{-1/3}$ ($A$ is the mass number) and for the spread width $\Gamma\sim A^{-2/3}$ (the above expression is equivalent to $\Gamma=gE^2$ with $g=\eta/(2\hbar\mu))$ agree fairly reasonably with data throughout the periodic table. The existing macroscopic treatment of collective nuclear dynamics has many features in common with non-radial elastodynamic vibrations [38,39] of a viscoelastic sphere whose damping is caused by viscosity of nuclear matter. More precisely, the rate of energy dissipation by viscosity is described by the Newtonian law for viscous stresses [21,40]. Besides, the fingerprints of viscoelastic behaviour of macroscopic nuclear matter has also been disclosed in the dynamics of nuclear fusion [41,42] and fission [43] (see also [39]). At the same time, it must be stressed that the physics beyond the elastodynamics of nuclear resonant response is different from that for nuclear fission. The relaxation of resonant excitation is an essentially fast adiabatic process controlled by forces associated with the volume member of nuclear binding energy, whereas the slow adiabatic development of the fission process is dominated by surface forces of nuclear origin and volume Coulomb forces (represented by surface and Coulomb members in the semi-empirical formula for nuclear binding energy). The concluding suggestion of nuclear collective dynamics regarding the rheological properties of nuclear matter can be formulated as follows. If the excitation energy is not enough to induce fluctuations in density, the nuclear Fermi-continuum would display the behaviour generic in a highly-stiff incompressible viscoelastic solid. Otherwise, its behaviour would exhibit features inherent in both the viscous liquid and viscoelastic solid.

Keeping in mind the above findings of both neutron star physics and laboratory nuclear physics, in [44,45] it has been suggested that macroscopic equations, originally introduced within the context of collective dynamics of atomic nuclei, might appear to be a powerful tool for the study of large-scale fluctuations of nuclear matter inside their gigantic stellar counterparts. The present paper continues the investigation begun in [45], where a first attempt has been made to apply the equations of nuclear elastodynamics to the study of the oscillatory

behaviour of neutron stars, and, specifically, to the problem of non-radial pulsations. These pulsations are the only kind of gravitational agitation which is expected in a spherical mass of incompressible self-gravitating matter [46–49]. In [50–55] (see also references therein) non-radial pulsations have been studied in the context of effects of general relativity. The objective of the present paper is to elucidate the problem of non-radial pulsations from the standpoint of rheological properties of the nuclear Fermi-continuum. As compared to a short earlier paper [45], we present here an extensive mathematical treatment of non-radial gravitational-elastic pulsations within equations of nuclear elastodynamics, accentuating the proper choice of boundary conditions to be imposed when computing the frequency and relaxation time of these modes. In doing this, we shall discuss neutron star models made up both of pure neutron matter as well as more realistic models made of a chemically equilibrated nuclear matter.

As we have mentioned, the macroscopic model of nuclear collective dynamics pictures the nucleus as a small mass of the degenerate Fermi-continuum. Therefore, several comments can be made in advance regarding predictions of the model for a spherical mass of neutron star size. First of all, we notice that the value of shear modulus, $\mu \approx 10^{35}$ dyn sm$^{-2}$, for nuclear matter evaluated in the nuclear model is in remarkable agreement with that inferred from the two-component model of the Vela-pulsar starquakes (see [20], section 3.6 p 200). The coefficient of dynamic viscosity, deduced from nuclear data on both fission [57] and giant resonances [33], is estimated as $\eta \approx 10^{10}$ dyn sec sm$^{-2}$. Putting the density $\rho$ equal to the normal nuclear density $\rho_N = 2.8 \times 10^{14}$ g/cm$^3$ and the radius equal to the neutron star radius $R \sim 10^6$ cm, we obtain

$$
\omega \sim \sqrt{\frac{\mu}{\rho R^{2}}} \sim 10^{4} \mathrm{sec}^{-1} \quad \tau \sim \frac{\rho R^{2}}{\eta} \sim 10^{16} \mathrm{sec} \sim 10^{9} \text { years. } \tag{1.2}
$$

These estimates set a scale for the frequency and the relaxation time for a nuclear object of neutron star size. In the theory of stellar pulsations this relaxation time is known as the Kelvin time [49]. The obtained scaling estimate for $\tau$ coincides with an independent estimate presented in [2] for a massive star of mass $M$: $\tau_K \sim 10^{16} (M/M_\odot)^{-1}$ sec [2]. A special comment is deserved for the great shift of frequency from the region of stiff gamma radiation to the region of radio emission (since the frequency is a function of radius). The most remarkable consequence of the above scaling estimate is that the frequency of elastodynamic mode falls into the realm of gravitational frequency $\omega \sim (\rho G)^{1/2}$ which is completely independent of the neutron star size. This exhibits the fact that elastodynamic vibrations interfering with the gravitational ones can lead, as was first noticed in [45], to vibrational instability of a neutron star. Analysis of this instability is a major goal of our study.

This paper is organized as follows. In section 2, we start with the basic equations underlying the continuum approach, which allows one to describe both hydrodynamic and elastodynamic regimes of the motion of a strongly-compressed Fermi-continuum. To shed more light on the origin of the above-mentioned gravitational instability, we present a brief consideration of the Jeans instability attributed to the oscillatory behaviour of unbounded Fermi-continuum under its own gravity. In section 3, the Rayleigh variational principle is adopted to compute the frequency of non-radial gravitational-elastic modes in the Cowling approximation. These modes are specified as spheroidal and torsional ones in accordance with the Lamb classification of eigenmodes of an elastic sphere. The major advantage of the energy variational method is that it allows one to compute the frequency and relaxation time both for spheroidal and torsional eigenmodes on equal footing. The theory of non-radial spheroidal and torsional gravitational-elastic pulsations and their damping by viscosity is presented in sections 4 and 5 respectively. In these sections the criteria for the onset of instability of a neutron star against quadrupole spheroidal and torsional elastic deformations are derived in an

analytic form. In section 6, we briefly summarize our results and discuss possible fingerprints of global gravitational-elastic vibrations in the observable activity of pulsars.

## 2. Governing equations for self-gravitating Fermi-continuum

The model under consideration rests on the statement that the nuclear Fermi-continuum in the presence of its own gravitational field is governed by equations of the form [44,45]:

$$
\frac{\mathrm{d} \rho}{\mathrm{d} t}+\rho \frac{\partial V_{i}}{\partial x_{i}}=0 \tag{2.1}
$$

$$
\rho \frac{\mathrm{d} V_{i}}{\mathrm{d} t}+\frac{\partial P_{i k}}{\partial x_{k}}-\rho \frac{\partial U}{\partial x_{i}}=0 \tag{2.2}
$$

$$
\frac{\mathrm{d} P_{i j}}{\mathrm{~d} t}+P_{i k} \frac{\partial V_{j}}{\partial x_{k}}+P_{j k} \frac{\partial V_{i}}{\partial x_{k}}+P_{i j} \frac{\partial V_{k}}{\partial x_{k}}=0 \tag{2.3}
$$

$$
\Delta U=-4 \pi G \rho \tag{2.4}
$$

where $\rho$ is the density, $V_{i}$ is the mean velocity of elastic displacements, and $P_{i j}$ stands for the tensor of elastic stresses. Having supplemented the continuum equations (2.1)-(2.3) with the equation for gravitational potential (2.4), which is treated in the Newtonian limit, we arrive at a closed system of continuum equations. In this paper, we take the sign of the gravitational force and the left-hand side of the last equation in accordance with the notation of [21].

### 2.1. Elastodynamic and hydrodynamic features in oscillatory behaviour of neutron Fermi-continuum

We start with a brief outline of the linear continuum mechanics built on equations (2.1)-(2.3), accentuating the fact that the rheological behaviour of degenerate Fermi-continuum is strongly correlated with dynamical distortions of the Fermi-distribution. As is known, the rheology of a material is determined by the dynamics of intrinsic stresses and is manifested by oscillatory and relaxation modes. Therefore, as a first step, it might be proper to illuminate the key points distinguishing the hydrodynamic behaviour of fluid substances (liquid and gaseous aggregate states) from the elastodynamic behaviour of stiff materials (a solid aggregate state). In an isotropic inviscid (non-conducting and non-magnetic) fluid, a small-amplitude perturbation is developed with preserving isotropy of the initially isotropic stress. This property is exhibited in the capability of transmitting a solely longitudinal compressional (sound or acoustic) wave. In contrast, perturbation of the elastic continuum is accompanied by spoiling of the isotropy of equilibrium stress. In a compressible elastic solid, the appearance of shear, essentially anisotropic, stresses is exhibited both by longitudinal and transverse waves. An incompressible isotropic elastic matter enables the support of a solely transverse wave due to its shear resistivity.

For instructive purposes, we confine our considerations to a homogeneous and isotropic neutron matter at zero temperature (ignoring for the moment the effects of self-gravity and viscosity). In this case the equilibrium stresses in bulk are completely determined by Fermi-pressure of degenerate neutrons.

$$
P_{i j}=P \delta_{i j} \quad P=\frac{\rho v_{F}^{2}}{5} \quad v_{F}=\frac{\hbar k_{F}}{m}. \tag{2.5}
$$

This form of stresses corresponds to an isotropic, spherically-symmetric, Fermi-distribution of neutrons in the momentum space (where the pressure $P=P(k_{F})$ is pictured by the Fermisphere). Let us show that for the perturbation developed with preserved isotropy of equilibrium

stresses (the case corresponding to spherically-symmetric compressional distortions of the Fermi-distribution)

$$
P_{i j} \rightarrow(P+\delta P) \delta_{i j} \tag{2.6}
$$

the model adequately describes wave motions attributed to an isotropic Fermi-fluid, whereas for the perturbation spoiling the isotropy of equilibrium stresses (whose appearance is inherently related to quadrupole deformation of the Fermi-sphere)

$$
P_{i j} \rightarrow P \delta_{i j}+\delta P_{i j} \tag{2.7}
$$

the model describes the oscillatory behaviour generic in an elastic Fermi-solid. In other words, we intend to show that equations (2.1)-(2.3) linearized with the help of substitution (2.6) describe the hydrodynamic oscillatory regime, whereas linearization of these equations by means of (2.7) describes small-amplitude fluctuations corresponding to the elastodynamic oscillatory regime.

Fermi-liquid oscillatory behaviour. Under a small-amplitude perturbation of a compressible fluid at rest, the density and velocity suffer small increments expressed by

$$
\rho \rightarrow \rho+\delta \rho \quad V_{i} \rightarrow V_{i}(=0)+\delta V_{i}. \tag{2.8}
$$

Making use of the above substitutions, (2.8) and (2.6), in equations (2.1)-(2.3), one has

$$
\frac{\partial \delta \rho}{\partial t}+\rho \frac{\partial \delta V_{i}}{\partial x_{i}}=0 \quad \rho \frac{\partial \delta V_{i}}{\partial t}+\frac{\partial \delta P}{\partial x_{i}}=0 \quad \frac{\partial \delta P}{\partial t}+\frac{5}{3} P \frac{\partial \delta V_{k}}{\partial x_{k}}=0. \tag{2.9}
$$

By performing the derivative with respect to time in the second equation for $\delta V_{i}$, and considering the third equation for $\delta P$, (2.9), we obtain the equation of a longitudinal sound wave

$$
\delta \ddot{\boldsymbol{V}}-c_{L}^{2} \Delta \delta \boldsymbol{V}=0 \quad c_{L}=\sqrt{\frac{5 P}{3 \rho}}=\frac{v_{F}}{\sqrt{3}} \tag{2.10}
$$

expressing the well-known result of the Landau Fermi-liquid theory (see, for instance, [58,59]) which states that the Fermi-liquid at zero temperature is capable of transmitting a sound wave. This wave is characterized by the dispersion-free regime of propagation $\omega=c_{L} k$ (here $k$ is the wave number) with the phase velocity $c_{L}$ (the Landau zero sound). In the classical (Maxwellian) gas, the internal pressure is proportional to the temperature $T$ (the equation of state of a classical gas reads $P=n k T$, where $k$ is the Boltzmann constant). Therefore, at zero temperature no wave motions are expected. This comparison is customarily presented to stress the essentially quantum nature of a zero-sound wave.

Oscillatory modes in elastic Fermi-solid. In contrast to the perfect fluid, an elastic solid perturbation is accompanied by spoiling of the isotropy of equilibrium isotropic stress. Substituting (2.8) and (2.7) into (2.1)-(2.3), one has

$$
\begin{aligned}
& \frac{\partial \delta \rho}{\partial t}+\rho \frac{\partial \delta V_{i}}{\partial x_{i}}=0 \quad \rho \frac{\partial \delta V_{i}}{\partial t}+\frac{\partial \delta P_{i j}}{\partial x_{j}}=0 \\
& \frac{\partial \delta P_{i j}}{\partial t}+P\left[\frac{\partial \delta V_{i}}{\partial x_{j}}+\frac{\partial \delta V_{j}}{\partial x_{i}}+\delta_{i j} \frac{\partial \delta V_{k}}{\partial x_{k}}\right]=0.
\end{aligned} \tag{2.11}
$$

Notice that the basic variable of elastodynamic description is the field of elastic displacements $\boldsymbol{D}(\boldsymbol{r}, t)$ which is related to the fluctuations in velocity $\delta \boldsymbol{V}$ by means of [33]

$$
\delta V_{i}(\boldsymbol{r}, t)=-\dot{D}_{i}(\boldsymbol{r}, t). \tag{2.12}
$$

Inserting (2.12) into the equation for $\delta P_{ij}$, (2.11), we obtain

$$
\delta P_{ij}=P\left(\frac{\partial D_{i}}{\partial x_{j}}+\frac{\partial D_{j}}{\partial x_{i}}+\delta_{ij}\frac{\partial D_{k}}{\partial x_{k}}\right). \tag{2.13}
$$

By comparing this stress tensor with that for stresses subjected to Hooke's law [16,17]

$$
\delta P_{ij}=\mu\left(\frac{\partial D_{i}}{\partial x_{j}}+\frac{\partial D_{j}}{\partial x_{i}}\right)+\lambda\delta_{ij}\frac{\partial D_{k}}{\partial x_{k}} \tag{2.14}
$$

one can conclude that the neutron Fermi-continuum behaves like an isotropic elastic solid in which the modulus of elasticity $\lambda$ and the shear modulus $\mu$ (parameters of Lamé) are equal to each other: $P=\lambda=\mu$. Furthermore, substituting (2.12) and (2.13) into the equation of motion for $\delta V_{i}$, (2.11), one finds that the latter takes the form

$$
\rho\ddot{D}=2P\ \text{grad div}\ D+P\ \Delta D \tag{2.15}
$$

which is identical to the Lamé equation

$$
\rho\ddot{D}=(\lambda+\mu)\text{grad div}\ D+\mu\ \Delta D \tag{2.16}
$$

describing the elastodynamics of small-amplitude deformations of an isotropic perfectly-elastic solid. Having established this correspondence, the oscillatory behaviour of neutron matter can be classified in a manner accepted in the classical theory of elasticity (see, for detail, [17], chapter III, section 22). Accordingly, the Hookean elastic solid is characterized by two modes of wave propagation, namely, by longitudinal and transverse elastodynamic waves of elastic displacements. The longitudinal wave is described by

$$
\ddot{D}-c_{l}^{2}\Delta D=0\quad\text{rot }D=0 \tag{2.17}
$$

and transmitted with the phase velocity

$$
c_{l}=\sqrt{\frac{\lambda+2\mu}{\rho}}=\sqrt{\frac{3}{5}}v_{F}. \tag{2.18}
$$

The transverse wave is governed by

$$
\ddot{D}-c_{t}^{2}\Delta D=0\quad\text{div }D=0. \tag{2.19}
$$

This wave travels with the phase velocity

$$
c_{t}=\sqrt{\frac{\mu}{\rho}}=\frac{v_{F}}{\sqrt{5}}. \tag{2.20}
$$

The very existence of the transverse zero-temperature mode is an agitation unique to an incompressible Fermi-continuum. This is one of the main reasons why the continuum treatment of nuclear (highly incompressible) matter based on equations (2.1)-(2.3) is referred to as nuclear elastodynamics [37]. The essentially quantum nature of the above modes is that they can be excited when the temperature of neutron matter is less than the temperature of degeneration, as is the case for the stellar matter of neutrons stars. It is worth noticing that for an incompressible strongly-condensed Fermi-continuum, the capability of transmitting transverse waves has also been justified in [59] on the basis of the Landau kinetic equation.

### 2.2. Elastodynamic instability of an infinite Fermi-solid under its own gravity

To get a feeling of the vibrational instability in question, we present here a brief consideration of the impact of gravity on the capability of propagating the longitudinal elastodynamic wave

in a compressible Fermi-continuum. For this purpose it is necessary to take into account the equation for fluctuations in a gravitational potential

$$
\Delta \delta U=-4 \pi G \delta \rho \quad \rightarrow \quad \frac{\partial \delta U}{\partial x_{i}}=-4 \pi G \rho D_{i}. \tag{2.21}
$$

and to replace the equation of motion for $\delta V_{i}$, equation (2.11), by the equation

$$
\rho \frac{\partial \delta V_{i}}{\partial t}=-\frac{\partial \delta P_{i j}}{\partial x_{j}}+\rho \frac{\partial \delta U}{\partial x_{i}}. \tag{2.22}
$$

Inserting (2.12), (2.13) and (2.21) into (2.22), we find that Lame's equation (2.16) takes the form

$$
\rho \ddot{\boldsymbol{D}}=(\lambda+2 \mu) \Delta \boldsymbol{D}+4 \pi G \rho^{2} \boldsymbol{D}=3 P \Delta \boldsymbol{D}+4 \pi G \rho^{2} \boldsymbol{D}. \tag{2.23}
$$

The dispersion equation characterizing the propagation of elastodynamic plane-wave perturbation is given by

$$
\omega^{2}=c_{l}^{2} k^{2}-4 \pi G \rho \quad c_{l}^{2}=\frac{3}{5} v_{F}^{2}. \tag{2.24}
$$

It is clearly seen that fluctuations in elastic stresses and in the potential of self-gravity acting destructively result in the instability for all wave numbers

$$
k<k_{J} \quad k_{J}=\left(\frac{4 \pi G \rho}{c_{l}^{2}}\right)^{1 / 2}=\left(\frac{20 \pi}{3} \frac{G \rho}{v_{F}^{2}}\right)^{1 / 2}. \tag{2.25}
$$

This instability should be thought of as an elastodynamic analogue of the gravitational instability discovered by Jeans (see, for instance, [21]) on the basis of hydrodynamic equations for an infinite self-gravitating fluid$\dagger$. When condition (2.25) is fulfilled, a material substance can spontaneously go, under influence of its own gravity, to the state of lower energy with the liberation of thermal energy. It is a goal of the remainder of this paper to explore this kind of vibrational instability for a neutron star modelled by a spherical mass of incompressible nuclear matter.

### 3. Non-radial gravitational-elastic pulsations

For the former, we present a brief outline of the homogeneous model, referred to as the standard stellar model [46]. In the standard model, a neutron star is pictured as a homogeneous spherical heavy mass of incompressible substance condensed to the normal nuclear density in which self-gravity is brought into equilibrium by isotropic stresses, so that the stress tensor is represented as $P_{i k}(r)=P(r) \delta_{i k}$. The local equilibrium, as follows from the above equations, is described by

$$
\boldsymbol{V}=0 \quad \frac{\partial P_{i k}}{\partial x_{k}}=\rho \frac{\partial U}{\partial x_{i}} \quad \Delta U=-4 \pi G \rho. \tag{3.1}
$$

The solutions to (3.1) are well known

$$
U(r)=\frac{2 \pi}{3} G \rho\left(3 R^{2}-r^{2}\right) \quad P(r)=P_{N}(\rho)-(2 \pi / 3) G \rho^{2} r^{2}. \tag{3.2}
$$

$\dagger$ In the case of self-gravitating Fermi-liquid the dispersion equation and Jeans's criterion are given by

$$
\omega^{2}=c_{L}^{2} k^{2}-4 \pi G \rho \quad c_{L}^{2}=\frac{v_{F}^{2}}{3} \quad k<k_{J} \quad k_{J}=\left(12 \pi \frac{G \rho}{v_{F}^{2}}\right)^{1 / 2}.
$$

![](./images/812460946915065857_1.jpg)

Figure 1. The density and pressure profiles for a neutron star of mass $M=1.0M_{\odot}$ as follows from the standard homogeneous (left-hand side) and realistic nonhomogeneous (right-hand side) models.

The central pressure $P(r=0)=P_{N}(\rho)$ is the basic quantity providing information on the equation of state of nuclear matter and, thus, links the physics of neutron stars with nuclear physics. By defining the stellar radius as that radial distance corresponding to the surface free from the gravitational-elastic stress $P(R)=0$, we obtain [45]

$$
R=\left[3 P_{N} /\left(2 \pi \rho^{2} G\right)\right]^{1 / 2} \quad M=(4 \pi / 3) \rho R^{3}. \tag{3.3}
$$

In figure 1, the density and pressure profiles computed within the standard model$\dagger$ are plotted in juxtaposition with the prediction of a model built on a realistic EOS. One sees that in spite of enormous gravity, the standard model provides reasonable fitting of the pressure profile of a non-homogeneous model. In figure 2 we present realistic density and pressure profiles for neutron star models with mass and radius listed in table 2. The latter models have been constructed on the basis of equations of state for chemically equilibrated nuclear stellar matter described in detail in [13].

In this paper, the emphasis is made on global non-radial gravitational-elastic pulsations whose development is not accompanied by fluctuations in density. These large-scale fluctuations of incompressible nuclear matter are primarily sensitive to the non-homogeneous

$\dagger$ The parameters of for a pure neutron matter $P_{N}(\rho)=\frac{2}{3} \mathcal{E}_{N}(\rho)$ can be found in [2].

![](./images/812460946915065857_2.jpg)

Figure 2. Energy density (in units of nuclear matter density, $\epsilon_0 = 140$ MeV/fm$^3$) and pressure versus radial distance for the neutron star models constructed in [13,56].

distribution of gravity and pressure, but not very sensitive to the density. By varying the density in the range $\rho \sim 1$-$3\rho_N$, one finds that the model provides reasonable estimates for the neutron star mass and radius (see table 1 and, also, table 1 of [45]). This allows one to assume that the model of uniform mass distribution would lead to reasonable estimates for vibrational characteristics of a neutron star, too. However, it must be different for radial pulsations, whose development is inherently related with fluctuations in the bulk density. The major physical significance of the standard model is that it allows one to gain an important qualitative insight into large-scale motions generic to nuclear matter, and to illustrate the type of difficulties one must confront in the study of realistic models. In particular, it will guide us in formulating explicit criteria for the vibrational stability of an isolated neutron star to global non-radial gravitational-elastic fluctuations which do not affect the density.

For a spherical mass of incompressible matter under its own gravity, only non-radial oscillations are possible. In the case of a neutron star, such vibrations may be expected to result from the stellar collapse in a supernova explosion which gives birth to a neutron star, or may be induced by the interaction between compact stellar components in a binary system. To compute frequencies of small-amplitude non-radial gravitational-elastic eigenmodes, we take advantage of the energy variational principle [21]. The linearized equations for incompressible

**Table 1.** The neutron star mass $M$ (in units of solar mass $M_\odot$), radius $R$ (km) and period $P_L$ ($\times 10^{-1}$ ms) of spheroidal and torsional non-radial eigenmodes computed on the basis of the standard homogeneous model of a neutron star (equations (4.9) and (5.8)).

<table>
  <thead>
    <tr>
      <th colspan="2">Neutron star model</th>
      <th colspan="3">Spheroidal mode</th>
      <th colspan="3">Torsional mode</th>
    </tr>
    <tr>
      <th>$M/M_\odot$</th>
      <th>$R$ (km)</th>
      <th>$P_2$</th>
      <th>$P_3$</th>
      <th>$P_4$</th>
      <th>$P_2$</th>
      <th>$P_3$</th>
      <th>$P_4$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.89</td>
      <td>12.34</td>
      <td>0.14</td>
      <td>0.11</td>
      <td>0.08</td>
      <td>0.20</td>
      <td>0.14</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>0.95</td>
      <td>12.10</td>
      <td>0.13</td>
      <td>0.10</td>
      <td>0.08</td>
      <td>0.19</td>
      <td>0.13</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>1.00</td>
      <td>11.89</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>0.18</td>
      <td>0.13</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>1.04</td>
      <td>11.70</td>
      <td>0.12</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>0.17</td>
      <td>0.12</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>1.09</td>
      <td>11.54</td>
      <td>0.12</td>
      <td>0.08</td>
      <td>0.07</td>
      <td>0.16</td>
      <td>0.12</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>1.14</td>
      <td>11.38</td>
      <td>0.11</td>
      <td>0.08</td>
      <td>0.06</td>
      <td>0.16</td>
      <td>0.11</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>1.18</td>
      <td>11.24</td>
      <td>0.10</td>
      <td>0.08</td>
      <td>0.06</td>
      <td>0.15</td>
      <td>0.11</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>1.22</td>
      <td>11.12</td>
      <td>0.10</td>
      <td>0.07</td>
      <td>0.06</td>
      <td>0.15</td>
      <td>0.10</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>1.26</td>
      <td>11.00</td>
      <td>0.10</td>
      <td>0.07</td>
      <td>0.06</td>
      <td>0.14</td>
      <td>0.10</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>1.30</td>
      <td>10.89</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>0.06</td>
      <td>0.14</td>
      <td>0.09</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>1.34</td>
      <td>10.78</td>
      <td>0.09</td>
      <td>0.07</td>
      <td>0.05</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>1.37</td>
      <td>10.69</td>
      <td>0.09</td>
      <td>0.06</td>
      <td>0.05</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>1.41</td>
      <td>10.59</td>
      <td>0.09</td>
      <td>0.06</td>
      <td>0.05</td>
      <td>0.13</td>
      <td>0.09</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>1.44</td>
      <td>10.51</td>
      <td>0.09</td>
      <td>0.06</td>
      <td>0.05</td>
      <td>0.12</td>
      <td>0.09</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>1.48</td>
      <td>10.43</td>
      <td>0.09</td>
      <td>0.06</td>
      <td>0.05</td>
      <td>0.12</td>
      <td>0.09</td>
      <td>0.07</td>
    </tr>
  </tbody>
</table>

**Table 2.** The periods $P_L$ ($\times 10^{-1}$ ms) of spheroidal and torsional non-radial eigenmodes for a neutron star model constructed on the basis of realistic EOS for soft and stiff nuclear stellar matter [13].

<table>
  <thead>
    <tr>
      <th colspan="3">Neutron star model</th>
      <th colspan="3">Spheroidal mode</th>
      <th colspan="3">Torsional mode</th>
    </tr>
    <tr>
      <th>EOS</th>
      <th>$M/M_\odot$</th>
      <th>$R$ (km)</th>
      <th>$P_2$</th>
      <th>$P_3$</th>
      <th>$P_4$</th>
      <th>$P_2$</th>
      <th>$P_3$</th>
      <th>$P_4$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HV</td>
      <td>1.0</td>
      <td>14.38</td>
      <td>4.13</td>
      <td>3.02</td>
      <td>2.53</td>
      <td>6.04</td>
      <td>4.38</td>
      <td>3.65</td>
    </tr>
    <tr>
      <td>HV</td>
      <td>1.2</td>
      <td>14.23</td>
      <td>3.69</td>
      <td>2.70</td>
      <td>2.26</td>
      <td>5.40</td>
      <td>3.92</td>
      <td>3.26</td>
    </tr>
    <tr>
      <td>HV</td>
      <td>1.9</td>
      <td>11.28</td>
      <td>1.43</td>
      <td>1.06</td>
      <td>0.89</td>
      <td>2.12</td>
      <td>1.54</td>
      <td>1.28</td>
    </tr>
    <tr>
      <td>$G_{200}^\pi$</td>
      <td>1.2</td>
      <td>11.95</td>
      <td>2.61</td>
      <td>1.95</td>
      <td>1.65</td>
      <td>3.89</td>
      <td>2.86</td>
      <td>2.41</td>
    </tr>
    <tr>
      <td>$G_{200}^\pi$</td>
      <td>1.3</td>
      <td>11.59</td>
      <td>2.33</td>
      <td>1.74</td>
      <td>1.48</td>
      <td>3.47</td>
      <td>2.56</td>
      <td>2.15</td>
    </tr>
    <tr>
      <td>$G_{200}^\pi$</td>
      <td>1.4</td>
      <td>11.03</td>
      <td>1.98</td>
      <td>1.48</td>
      <td>1.26</td>
      <td>2.97</td>
      <td>2.19</td>
      <td>1.85</td>
    </tr>
    <tr>
      <td>UVII</td>
      <td>2.1</td>
      <td>9.20</td>
      <td>0.91</td>
      <td>0.69</td>
      <td>0.59</td>
      <td>1.38</td>
      <td>1.01</td>
      <td>0.85</td>
    </tr>
  </tbody>
</table>

self-gravitating Fermi-continuum are written as follows

$$
\frac{\partial \delta V_{i}}{\partial x_{i}}=0 \tag{3.4}
$$

$$
\rho \frac{\partial \delta V_{i}}{\partial t}+\frac{\partial \delta P_{i j}}{\partial x_{j}}-\rho \frac{\partial \delta U}{\partial x_{i}}=0 \tag{3.5}
$$

$$
\frac{\partial \delta P_{i j}}{\partial t}+P\left(\frac{\partial \delta V_{i}}{\partial x_{j}}+\frac{\partial \delta V_{j}}{\partial x_{i}}\right)+\delta_{i j}\left(\delta V_{k} \frac{\partial P}{\partial x_{k}}\right)=0 \tag{3.6}
$$

$$
\Delta \delta U=0. \tag{3.7}
$$

The condition of energy balance during vibrations is controlled by the equation

$$
\frac{\partial}{\partial t} \int_{v} \frac{1}{2} \rho \delta V^{2} \mathrm{~d} v-\int_{v} \delta P_{i j} \frac{\partial \delta V_{i}}{\partial x_{j}} \mathrm{~d} v+\oint_{s}\left[\delta P_{i j} \delta V_{j}-\rho \delta U \delta V_{i}\right] \mathrm{d} s_{i}=0 \tag{3.8}
$$

which is obtained by scalar multiplication of equation (3.5) with $\delta V_{i}$ and integration over the stellar volume. The next step is to apply Rayleigh's factorization procedure

$$
\delta U(\boldsymbol{r}, t)=\Phi(\boldsymbol{r}) \alpha(t) \quad \delta V_{i}(\boldsymbol{r}, t)=-\xi_{i}(\boldsymbol{r}) \dot{\alpha}(t)
\tag{3.9}
$$

where $\alpha(t)$ (the coordinate of normal vibrations) measures the temporal amplitude of elastic distortions, and $\xi_{i}(\boldsymbol{r})$ is the field of instantaneous elastic displacements, related to the above introduced field $\boldsymbol{D}(\boldsymbol{r}, t)$ by means of $D_{i}(\boldsymbol{r}, t)=\xi_{i}(\boldsymbol{r}) \alpha(t)$. Inserting $\delta V_{i}(\boldsymbol{r}, t)$ from (3.9) into (3.6), one has

$$
\delta P_{i j}(\boldsymbol{r}, t)=\left[P(r)\left(\frac{\partial \xi_{i}(\boldsymbol{r})}{\partial x_{j}}+\frac{\partial \xi_{j}(\boldsymbol{r})}{\partial x_{i}}\right)+\delta_{i j}\left(\xi_{k}(\boldsymbol{r}) \frac{\partial P(r)}{\partial x_{k}}\right)\right] \alpha(t). \quad (3.10)
$$

At this point we stress again that the main goal of the present paper consists of describing the frequencies of global gravitational-elastic vibrations, which are essentially of the volume character. This circumstance is taken into account by imposing the requirement

$$
\left[\rho \delta U-D_{i} \frac{\partial P}{\partial x_{i}}\right]_{r=R}=0.
\tag{3.11}
$$

The latter condition should be considered as an elastodynamic analogue of the Cowling approximation utilized in hydrodynamic calculations of stellar variability. It consists of neglecting perturbations in the gravitational potential. The use of Cowling's approximation is one of the main points which distinguishes our present calculation from that performed in [45].

Substituting (3.9) and (3.10) into (3.8), integrating by parts and taking into account condition (3.11), one finds that the equation of energy balance is replaced by

$$
\frac{\mathrm{d} E}{\mathrm{~d} t}=0 \quad E=\frac{\mathcal{M} \dot{\alpha}^{2}}{2}+\frac{\mathcal{K} \alpha^{2}}{2}
\tag{3.12}
$$

where $E$ is the energy of non-radial gravitational-elastic pulsations. The inertia, $\mathcal{M}$ and stiffness, $\mathcal{K}$ are given by

$$
\mathcal{M}=\int_{v} \rho \xi_{i} \xi_{i} \mathrm{~d} v \quad \mathcal{K}=\frac{1}{2} \int_{v} P\left(\frac{\partial \xi_{i}}{\partial x_{j}}+\frac{\partial \xi_{j}}{\partial x_{i}}\right)^{2} \mathrm{~d} v.
\tag{3.13}
$$

The last equation for the stiffness explicitly exhibits the volume character of stellar elastodynamic oscillations and again emphasizes the fact that linear anisotropic deformations of stellar matter are controlled by Hooke's law [16,17]. It is seen that the solenoidal field (due to the incompressibility) of instantaneous displacements $\xi(\boldsymbol{r})$ is the only quantity that remains to be determined when computing the frequencies of the global non-radial gravitational-elastic eigenmodes whose temporal amplitude, $\alpha$, is a function harmonic in time.

The non-radial modes of a neutron star (modelled by a self-gravitating incompressible mass of elastic Fermi-solid) can be classified, as suggested in [44], by eigenmodes of an elastic sphere. The latter classification is due to Lamb [40]. The fields of elastic displacements are found as two orthogonal (poloidal and toroidal) solutions [39,38] to the vector Laplace equation

$$
\Delta \boldsymbol{D}(\boldsymbol{r}, t)=0 \quad \operatorname{div} \boldsymbol{D}(\boldsymbol{r}, t)=0.
\tag{3.14}
$$

The spheroidal non-radial mode is described by the poloidal solution to (3.14)

$$
\boldsymbol{D}(\boldsymbol{r}, t)=\frac{N_{p}}{L+1} \operatorname{rot} \operatorname{rot} \boldsymbol{r} r^{L} P_{L}(\mu) \alpha(t)=N_{p} \operatorname{grad} r^{L} P_{L}(\mu) \alpha(t) \quad \mu=\cos \theta.
\tag{3.15}
$$

Hereafter, $P_L(\mu)$ is the Legendre polynomial of multipole order $L$. The torsional mode is associated with the solution given by the toroidal field of displacement

$$
\boldsymbol{D}(\boldsymbol{r}, t)=N_{t} \operatorname{rot} \boldsymbol{r} r^{L} P_{L}(\mu) \alpha(t). \tag{3.16}
$$

It is easily seen that fields (3.15) and (3.16) have no radial nodes and, therefore, describe essentially non-radial elastodynamic vibrations. Finally, we are left with formulating the proper boundary conditions for eliminating the arbitrary constants $N_{p}$ and $N_{t}$.

The damping of non-radial elastodynamic pulsations of a neutron star can be described as those resulting from viscosity, which is subjected to the Newtonian law for viscous stresses

$$
\delta \Pi_{i j}(\boldsymbol{r}, t)=-\eta\left(\frac{\partial \delta V_{i}(\boldsymbol{r}, t)}{\partial x_{j}}+\frac{\partial \delta V_{j}(\boldsymbol{r}, t)}{\partial x_{i}}\right). \tag{3.17}
$$

As was mentioned in the introduction, this type of behaviour has been justified in the study of the damping of resonant response of nuclei and, in our opinion, it appears to be unlikely that the validity of this law for viscous stresses becomes unwarranted for their stellar counterparts. In accordance with this assumption, the Euler equation (3.5) should be replaced by the Lamé–Navier–Stokes equation

$$
\rho \frac{\partial \delta V_{i}}{\partial t}+\frac{\partial \delta P_{i j}}{\partial x_{j}}-\rho \frac{\partial \delta U}{\partial x_{i}}=\frac{\partial \delta \Pi_{i j}}{\partial x_{j}}. \tag{3.18}
$$

Making use of the above expounded energy variational principle, one finds that the energy balance equation (3.12) is replaced by the equations

$$
\frac{\mathrm{d} E(\alpha, \dot{\alpha})}{\mathrm{d} t}=F(\dot{\alpha}) \quad E(\alpha, \dot{\alpha})=\frac{\mathcal{M} \dot{\alpha}^{2}}{2}+\frac{\mathcal{K} \alpha^{2}}{2} \quad F(\dot{α})=-\mathcal{G} \dot{\alpha} \tag{3.19}
$$

which describe the rate of energy dissipation by viscosity. Here $F(\dot{\alpha})$ is the Rayleigh dissipative function. The parameter of viscous friction, $\mathcal{G}$, is given by

$$
\mathcal{G}=\frac{\eta}{2} \int_{v}\left(\frac{\partial \xi_{i}}{\partial x_{j}}+\frac{\partial \xi_{j}}{\partial x_{i}}\right)^{2} \mathrm{~d} v. \tag{3.20}
$$

It is convenient to represent (3.19) in the following equivalent form

$$
\ddot{\alpha}+2 \gamma \dot{\alpha}+\omega_{n}^{2} \alpha=0 \quad \omega_{n}^{2}=\frac{\mathcal{K}}{\mathcal{M}} \quad 2 \gamma=\frac{\mathcal{G}}{\mathcal{M}} \tag{3.21}
$$

where $\omega_{n}$ is the eigenfrequency of a normal mode whose relaxation time $\tau$ is given by

$$
\tau=\frac{1}{2 \gamma}=\frac{\mathcal{M}}{\mathcal{G}}. \tag{3.22}
$$

The general solution to equation (3.21) is well known

$$
\alpha(t)=\alpha_{0} \mathrm{e}^{-t / \tau} \cos (\omega t+\phi) \quad \omega=\omega_{n}\left[1-\frac{1}{\left(\omega_{n} \tau\right)^{2}}\right]^{1 / 2} \tag{3.23}
$$

where $\alpha_{0}$ and $\phi$ are some real constants. From the last expression for $\omega$, it follows that the condition ensuring the existence of an oscillatory mode reads

$$
\omega_{n} \tau \gg 1. \tag{3.24}
$$

An extensive discussion of this condition in the context of elastodynamic transverse waves in nuclear matter can be found in [33]. Returning to the above estimates for the frequency and relaxation time (1.2), one sees that this condition is fulfilled.

![](./images/812460946915065857_3.jpg)

Figure 3. Schematic illustration of the quadrupole ($L=2$) and octupole ($L=3$) spheroidal non-radial global vibrations of a neutron star.

## 4. Spheroidal gravitational-elastic mode

Small-amplitude elastic spheroidal deformations of an arbitrary sphere inside a star are described by relations of the form $r_s(\alpha_L)=r[1+\alpha_L P_L(\mu)]$. Figure 3 illustrates the character of spheroidal quadrupole and octupole elastodynamic vibrations. To eliminate the constant $N_p$ in equation (3.15), we impose the following dynamical boundary condition

$$
\left[\rho \Phi-\xi_{k} \frac{\partial P}{\partial x_{k}}\right]_{r=R}=0 \tag{4.1}
$$

which results from Cowling's approximation, equation (3.11). The gravitational potential on the surface of an oscillating star has the form [44]

$$
\Phi=\frac{4 \pi G \rho R^{2}}{(2 L+1)} P_{L}(\mu). \tag{4.2}
$$

Substituting (4.2), (3.15) and (3.2) into (4.1), we find

$$
N_{p}=\frac{3}{L(2 L+1) R^{L-2}}. \tag{4.3}
$$

Spherical components of the poloidal field which corresponds to the spheroidal elastic oscillations are given by

$$
\begin{aligned}
\xi_{r} &=N_{p} r^{L-1} P_{L}(\mu) \\
\xi_{\theta} &=-N_{p}\left(1-\mu^{2}\right)^{1 / 2} r^{L-1} \frac{\mathrm{d} P_{L}(\mu)}{\mathrm{d} \mu} \\
\xi_{\phi} &=0.
\end{aligned} \tag{4.4}
$$

By inserting (4.4) into equations (3.13) and integrating over the solid angle, one finds that the expressions for inertia and stiffness take the form

$$
\begin{aligned}
\mathcal{M} &=4 \pi L N_{p}^{2} \int_{0}^{R} \rho(r) r^{2 L} \mathrm{~d} r \\
\mathcal{K} &=8 \pi N_{p}^{2} L(L-1)(2 L-1) \int_{0}^{R} P(r) r^{2 L-2} \mathrm{~d} r.
\end{aligned} \tag{4.5}
$$

The last representation of $\mathcal{M}$ and $\mathcal{K}$ deserves a special comment. The density $\rho(r)$ and the pressure $P(r)$ profiles entering into equations (4.5) can be considered as input parameters of

the method. Adopting these quantities from realistic stellar models (computed on the basis of realistic equations of state and accounting for modifications of the gravitational field by general relativity theory), the method allows us to obtain reliable estimates for the frequencies of non-radial spheroidal pulsations (gravitational-elastic s-mode)

$$
\omega_{s}(L)=\left[\frac{2(2 L-1)(L-1) \int_{0}^{R} P(r) r^{2 L-2} \mathrm{~d} r}{\int_{0}^{R} \rho(r) r^{2 L} \mathrm{~d} r}\right]^{1 / 2}.
\tag{4.6}
$$

Within the framework of the standard stellar model, the latter integrals (4.5) can be taken analytically†

$$
\mathcal{M}=\frac{27 M R^{2}}{L(2 L+1)^{3}} \quad \mathcal{K}=36 E_{N} \frac{L-1}{L(2 L+1)^{2}}-45 E_{G} \frac{(L-1)(2 L-1)}{L(2 L+1)^{3}}
\tag{4.7}
$$

where

$$
E_{G}=(3 / 5) G M^{2} / R \quad E_{N}=\mathcal{E}_{N} V \quad \mathcal{E}_{N}=\frac{3}{10} \rho v_{F}^{2}
\tag{4.8}
$$

are the total gravitational energy and the internal energy of a star, respectively ($M$ and $V$ are the total mass and volume of the star). Equation (4.7) exhibits the fact that the restoring force of stable global elastodynamic vibrations is dominated by the rigidity of the Fermi-sphere (this shows the quantum origin of elasticity of the nuclear Fermi-matter), which counterbalances contracting stresses that arise from the gravitational pull.

The monopole (that is, essentially radial) mode is excluded because of high incompressibility of the stellar matter. The excitation of dipole poloidal field by elastic displacements might lead to a motion of the star's centre-of-gravity, that is, without changing its intrinsic state. We thus conclude that the quadrupole spheroidal elastic deformation of a neutron star appears as the most likely source by means of which a neutron star may become gravitationally unstable. The standard stellar model leads to the following analytic form for the frequency of gravitational-elastic s-mode:

$$
\begin{gathered}
\omega_{s}^{2}=\omega_{0}^{2}(2 L+1)(L-1)\left[1-\Gamma \frac{5(2 L-1)}{4(2 L+1)}\right] \\
\omega_{0}^{2}=\frac{4 E_{N}}{3 M R^{2}} \quad \Gamma=\frac{E_{G}}{E_{N}}.
\end{gathered}
\tag{4.9}
$$

Here $\omega_{0}$ defines the frequency unit for elastic vibrations of Fermi-continuum ($\omega_{0}^{2}=(2 / 5) \omega_{F}^{2}$ and $\omega_{F}=v_{F} / R$). The parameter $\Gamma$ can be referred to as the parameter of vibrational instability, since $\omega_{s}$ crucially depends on the magnitude of this parameter. The onset of instability of the quadrupole mode $\omega_{s}(L=2)=0$ is expected when $\Gamma$ attains its critical value $\Gamma_{\mathrm{cr}}=4 / 3$. So, we immediately find that the stability of a neutron star to infinitesimally small spheroidal quadrupole deformation requires

$$
\omega_{s}(L=2) \geqslant 0 \quad \rightarrow \quad \Gamma \leqslant \frac{4}{3}.
\tag{4.10}
$$

The latter inequality is fulfilled for all the stellar models listed in tables 1 and 2. In table 1, the numerical estimates for the periods of spheroidal gravitational-elastic pulsations were computed by equation (4.9). Comparing these periods with those obtained in [45], we conclude that the inclusion of surface vibrations does not crucially affect the results of the latter paper.

† The details of calculation of the integrals defining the inertia and stiffness can be found in [39,38].

Calculation of the parameter of viscous friction (3.20) with the field of instantaneous displacements corresponding to the non-radial spheroidal mode (4.4) yields

$$
\mathcal{G}=27 v M \frac{L-1}{L(2 L+1)^{2}} \quad v=\frac{\eta}{\rho} \tag{4.11}
$$

where $v$ stands for the kinematic viscosity. Inserting (4.11) together with inertia given by (4.7) into equation (3.22), one has

$$
\tau_{s}=\frac{\tau_{K}}{(2 L+1)(L-1)} \quad \tau_{K}=\frac{R^{2}}{v}=\frac{\rho R^{2}}{\eta}. \tag{4.12}
$$

Here $\tau_{K}$ is the Kelvin time defining damping of the spheroidal eigenmode by viscosity. The numerical estimate for $\tau_{K}$ is given by (1.2).

### 5. Torsional gravitational-elastic mode

The ability of a star to perform torsional vibrations is the most prominent feature of the elastodynamic behaviour of a stellar continuum. The physical meaning of torsional motions becomes clearer if one represents the velocity field in the following equivalent form [44]:

$$
\delta \boldsymbol{V}(\boldsymbol{r}, t)=[\Omega(\boldsymbol{r}, t) \times \boldsymbol{r}] \tag{5.1}
$$

where

$$
\Omega(\boldsymbol{r}, t)=N_{t} \dot{\alpha}_{L}(t) \operatorname{grad} r^{L} P_{L}(\mu) \tag{5.2}
$$

is the local vector field of angular velocity. The time-dependent amplitude, $\alpha_{L}(t)$, measures the infinitesimal angle of vorticity of the field of elastic displacements about the polar axis. The simplest example is the quadrupole torsional vibration, whose velocity has the components $\delta V_{x}=-\Omega_{z} y, \delta V_{y}=\Omega_{z} x, \delta V_{z}=0$. Formally, this field is similar to the case of rigid-body rotation. However, when one deals with torsion, the angular velocity $\Omega$ is not a uniform vector, but is a vector field with components $\Omega_{x}=0, \Omega_{y}=0, \Omega_{z}=\dot{\alpha} z$. The Cartesian components of the toroidal quadrupole field of torsional displacements are given by $\xi_{x}=-y z, \xi_{y}=x z, \xi_{z}=0$. The corresponding motions are axially symmetric out-of-phase oscillations of the star's northern and southern hemisphere about the polar axis $z$ (see figure 4). The arbitrary constant $N_{t}$ is uniquely defined by the following boundary condition [44]:

$$
\left.\delta \boldsymbol{V}(\boldsymbol{r}, t)\right|_{r=R}=\left[\Omega_{0} \times \boldsymbol{r}\right] \quad \text { with } \quad \Omega_{0}=\dot{\alpha}_{L}(t) \operatorname{grad} P_{L}(\mu) \quad \rightarrow \quad N_{t}=\frac{1}{R^{L-1}}. \tag{5.3}
$$

Spherical components of the toroidal field of torsional elastic displacements are given by

$$
\xi_{r}=0 \quad \xi_{\theta}=0 \quad \xi_{\phi}=N_{t} r^{L}\left(1-\mu^{2}\right)^{1 / 2} \frac{\mathrm{d} P_{L}(\mu)}{\mathrm{d} \mu}. \tag{5.4}
$$

Figure 4 pictures the quadrupole and octupole torsional vibrations. Inserting (5.4) into (3.13) and integrating over the solid angle, we arrive at the following expressions for inertia and stiffness

$$
\begin{aligned}
& \mathcal{M}=4 \pi N_{t}^{2} \frac{L(L+1)}{(2 L+1)} \int_{0}^{R} \rho(r) r^{2 L+2} \mathrm{~d} r \\
& \mathcal{K}=4 \pi N_{t}^{2} L\left(L^{2}-1\right) \int_{0}^{R} P(r) r^{2 L} \mathrm{~d} r.
\end{aligned} \tag{5.5}
$$

![](./images/812460946915065857_4.jpg)

Figure 4. Same as for figure 3, but for the global torsional non-radial gravitational-elastic oscillations.

We stress again that the presented form of the latter two equations permit us to compute the frequency of the gravitational-elastic t-mode

$$
\omega_{t}(L)=\left[\frac{(2 L+1)(L-1) \int_{0}^{R} P(r) r^{2 L} \mathrm{~d} r}{\int_{0}^{R} \rho(r) r^{2 L+2} \mathrm{~d} r}\right]^{1 / 2} \tag{5.6}
$$

of global non-radial torsional oscillations and explore their stability on the basis of realistic models of neutron stars.

In the standard stellar model, we have

$$
\begin{aligned}
& \mathcal{M}=3 M R^{2} \frac{L(L+1)}{(2 L+1)(2 L+3)} \\
& \mathcal{K}=2 E_{N} \frac{L\left(L^{2}-1\right)}{(2 L+1)}-\frac{5}{2} E_{G} \frac{L\left(L^{2}-1\right)}{(2 L+3)}.
\end{aligned} \tag{5.7}
$$

For $L=1$, the mass parameter coincides with the moment of inertia of a rigid uniform sphere $J_{0}=(2 / 5) M R^{2}$. This observation defines the physical meaning of the mass parameter of torsional vibrations, the torsional moment of inertia. From the equation for stiffness, equation (5.7), it follows that the case $L=1$ corresponds to the rigid-body rotation with a constant angular velocity $\Omega$, which is not an eigenmode of the Hamiltonian of non-radial vibrations (3.12). We therefore arrive at the conclusion that the lowest stable torsional vibration has the multipole order $L=2$, as in the case of spheroidal vibrations. Computed in the standard stellar model, the frequency of the global torsional gravitational-elastic oscillations is given by

$$
\omega_{t}^{2}=\frac{1}{2} \omega_{0}^{2}(2 L+3)(L-1)\left[1-\Gamma \frac{5(2 L+1)}{4(2 L+3)}\right] \tag{5.8}
$$

with the natural frequency of elastic vibrations, $\omega_{0}$, and the parameter of vibrational instability, $\Gamma$, defined by (4.9). A neutron star remains stable to infinitesimally small torsional quadruple deformations if and only if

$$
\omega_{t}(L=2) \geqslant 0 \quad \rightarrow \quad \Gamma \leqslant 1.15. \tag{5.9}
$$

In tables 1 and 2, the periods of global torsional gravitational-elastic modes are presented in juxtaposition with those of spheroidal modes computed within the framework of homogenous and realistic models. One sees that periods of s-mode are always higher than those of t-mode.

The parameter of viscous friction, (3.20), computed with the toroidal field of instantaneous displacements (5.4) is found to be

$$
\mathcal{G}=\frac{3}{2} \nu M \frac{L\left(L^{2}-1\right)}{(2 L+1)}. \tag{5.10}
$$

Substituting (5.10) together with the moment of inertia of torsional oscillations (5.7) into equation (3.22), we obtain

$$
\tau_{t}=\frac{2 \tau_{K}}{(2 L+3)(L-1)}. \tag{5.11}
$$

From the obtained analytic estimates for the frequency and relaxation time, it follows that the higher the frequency (multipole degree) of vibration, the shorter its lifetime. The discussion of the fact that the relaxation time characterizing damping of normal modes by the Newtonian viscosity is independent of the restoring force maintaining the equilibrium can be found in [21].

### 6. Summary
In this paper, we present arguments that the elastodynamic treatment of the large-scale motion of highly compressed stellar matter, as it exists in the cores of collapsed stellar objects (like white dwarfs, neutron stars, and hypothetical sequences of strange-matter stars), is a more suitable continuum approach than the one based on the equations of hydrodynamics. The latter is widely utilized in studies of the variability of main-sequence stars whose matter is a loosely dense (liquid or gaseous) plasma.

The primary goal of this paper was to explore the continuum approach based on equations of nuclear elastodynamics to the study of non-radial oscillations of neutron stars, and to obtain criteria for their vibrational stability. It is argued that neutron stars possess two vibrational degrees of freedom, which we classify as spheroidal and torsional gravitational-elastic eigenmodes. The relaxation time of these modes due to the viscosity of nuclear matter is found to be of the order of $10^{9}$ years. The periods of these pulsations calculated for homogeneous neutron star models constitute lower bounds which increase somewhat if the neutron star models are constructed for more realistic equations of state. The vibrational stability of neutron stars imposes a rigorous constraint on the ratio of a star's gravitational energy, $E_{G}$, to its internal energy, $E_{N}$: $E_{G}/E_{N} \leqslant 4/3$. Otherwise, any infinitesimally small perturbation of the equilibrium configuration will lead to stellar explosion (probably, in the form of a break-up of a star into fragments). However, for most cases of physical interest, the above condition seems to be well satisfied and the major conclusion of our analysis is that neutron stars are very stable to small-amplitude quadrupole elastic deformations, no matter whether these are spheroidal or torsional ones.

The total number of currently monitored radiopulsars is of the order of 600, and many of them display restless or noisy behaviour which is detected in the spectrum of radioemission as finer details whose periodicity within the main pulse is of a different timescale. This latter circumstance has been one of the reasons for classifying these pulsars as complex or c-pulsars, to distinguish them from simple or s-pulsars whose spectra do not reveal permanent noisy behaviour [60]. According to our estimates, the periods of global non-radial gravitational-elastic vibrations are $P \sim 0.01$–0.1 ms, i.e. one or two orders of magnitude smaller than the

rotational periods of radio pulsars, which lie in the range between 1.6 ms and 5 s. From this we conclude that the non-radial gravitational oscillations, as well as the radial ones which have been fairly well studied over the years, have nothing to do with the main pulse phenomenon. This may be quite different for the radioemission spectrum of a wide class of above mentioned c-pulsars. The spectra of c-pulsars exhibit characteristic substructures within the pulse window, the physical nature of which, however, is not understood very well. In particular, along with the well recognized interpulse, located approximately at the centre between two main pulses, there are clearly distinguishable subpulses with the length of period $10^{-4}$-$10^{-3}$ seconds. Further inspection of the subpulse window reveals weak peaks of micropulses with periods less than $10^{-4}$ seconds [2,4,60]. Our outcome for the periods of non-radial oscillations, as can be seen from table 1, falls right into this latter window. This supports the hypothesis [47,49] that the weak variability in the radioemission of neutron stars, observable as fine noise in the subpulse region of their spectra, can be assigned to their gravitational pulsations.

## Acknowledgments

The authors are grateful to I Molodtsova, P-Y Lai, S Nedelko, O Streltsova and T Chiueh for encouraging discussions. We would like to thank the anonymous referees for important suggestions and remarks clarifying the physical understanding of the problems touched upon in this paper. The work received partial support from the Heisenberg–Landau program of Russian–German scientific cooperation, grant HL-BLTP-97-98.

## References

[1] Hewish A, Bell S J, Pilkington J D H, Scott P F and Collins R A 1968 *Nature* **217** 709
Hewish A 1970 *Ann. Rev. Astron. Astrophys.* **8** 265

[2] Shapiro S L and Teukolsky S A 1983 *Black Holes, White Dwarfs and Neutron Stars* (New York: Wiley)

[3] Bisnovatyi-Kogan G S 1989 *Physical Problem of Stellar Evolution* (Moscow: Nauka)

[4] Saakian G S 1995 *Physics of Neutron Stars* (Dubna: Joint Institute for Nuclear Research)

[5] Koester D and Chanmungam G 1990 *Rep. Prog. Phys.* **53** 837
Chanmungam G 1992 *Ann. Rev. Astron. Astrophys.* **30** 143

[6] Migdal A B, Voskresensky D N, Sapershtein E E and Troitzky M A 1991 *Pionic Degrees of Freedom in Nuclear Matter* (Moscow: Nauka)

[7] Beskin V S, Gurevich A V and Istomin Ya A 1992 *Physics of the Pulsar Magnetosphere* (Cambridge: Cambridge University Press)

[8] Pines D and Ali Alpar M 1992 *Structure and Evolution of Neutron Stars* ed D Pines, R Tamagaki and S Tsuruta (New York: Addison-Wesley)

[9] Weber F and Glendenning N K 1993 *Astrophysics and Neutrino Physics* (Singapore: World Scientific) p 64

[10] Bodmer A R 1971 *Phys. Rev. D* **4** 1601
Terazawa H 1979 INS-Report-338 (Tokyo: Tokyo University Press)
Witten E 1984 *Phys. Rev. D* **30** 272

[11] Glendenning N K, Kettner Ch and Weber F 1995 *Phys. Rev. Lett.* **74** 3519
Kettner Ch, Weber F, Weigel M K and Glendenning N K 1995 *Phys. Rev. D* **51** 1440

[12] Glendenning N K 1996 *Compact Stars* (Berlin: Springer)

[13] Weber F 1998 *Neutron and quark matter stars as a probe of superdense relativistic matter* (Bristol: Institute of Physics) at press

[14] Hansen C J and Van Horn H M 1979 *Astrophys. J.* **233** 253

[15] Hansen C J 1980 *Nonradial and Nonlinear Stellar Pulsations* ed H A Hill and W A Dziembowski *Lecture Notes in Physics* (Berlin: Springer) p 445

[16] Love A 1945 *Mathematical Theory of Elasticity* (Cambridge: Cambridge University Press)

[17] Landau L D and Lifshits E M 1959 *Theory of Elasticity* (New York: Pergamon)

[18] Baym G, Pethick C J, Pines D and Ruderman M 1969 *Nature* **224** 872
Baym G and Pines D 1971 *Ann. Phys., NY* **66** 816

[19] Ruderman M 1972 *Ann. Rev. Astron. Astrophys.* **10** 427
Baym G and Pethick C J 1975 *Ann. Rev. Astron. Astrophys.* **17** 415

[20] Pines D, Shaham J and Ruderman M A 1974 *IAU Symposium No 53, Physics of Dense Matter* ed C J Hansen (Dordrecht: Reidel)

[21] Chandrasekhar S 1961 *Hydrodynamic and Hydromagnetic Stability* (Oxford: Clarendon)

[22] Hoyle F, Narlikar J V and Wheeler J A 1964 *Nature* **203** 914
Wheeler J A 1966 *Ann. Rev. Astron. Astrophys.* **4** 393

[23] Bastrukov S I, Papoyan V V and Podgainy D V 1996 *JETP Lett.* **64** 637
Bastrukov S I and Podgainy D V 1996 *Phys. Rev. E* **54** 4465
Bastrukov S I and Podgainy D V 1997 *Astronomy Rep.* **41** 813

[24] Bertsch G F 1974 *Ann. Phys., NY* **86** 138
Bertsch G F 1978 *Nuclear Physics with Heavy Ions and Mesons* ed R Balian, M Rho and G Ripka (Amsterdam: North-Holland) vol 1 p 175

[25] Wong C Y Maruhn J A and Welton 1975 *Nucl. Phys. A* **253** 469
Wong C Y and Azziz N 1981 *Phys. Rev. C* **24** 2290

[26] Holzwarth G and Eckart G 1977 *Z. Phys. A* **283** 219
Sagawa H and Holzwarth G, 1978 *Prog. Theor. Phys.* **59** 1213
Holtswarth G Eckart G and Providéncia J P 1981 *Nucl. Phys. A* **364** 1

[27] Nix J R and Sierk A J 1980 *Phys. Rev. C* **21** 396

[28] Kolomietz V M and Tang H H K 1981 *Phys. Scr.* **24** 915
Kolomietz V M 1983 *Sov. J. Nucl. Phys.* **37** 547
Kolomietz V M, Magner A G and Pluiko V A 1993 *Z. Phys. A* **345** 131
Kolomietz V M, Magner A G and Pluiko V A 1993 *Z. Phys. A* **345** 137

[29] Hasse R W, Ghosh G Winter J and Lumbroso A 1982 *Phys. Rev. C* **25** 2271

[30] Stringari S 1983 *Ann. Phys.* **151** 35
Lipparini E and Stringari S 1989 *Phys. Rep.* **174** 105

[31] Wambach J 1988 *Rep. Prog. Phys.* **51** 989

[32] Di Toro M and Russo G 1989 *Z. Phys. A* **331** 381
Di Toro M 1991 *Phys. Part. Nucl.* **22** 385

[33] Kolomietz V M 1990 *Local Density Approximation in Atomic and Nuclear Physics* (Kiev: Naukova Dumka)

[34] Balbutsev E B, Mikhailov I N, Molodtsova I V, Piperova J , Bastrukov S I, Sinichkin V P and Shekhter L Sh 1991 Nuclear collective motion described by the moments of the Wigner distribution function, *Proc. 6th Int. Conf. on Nuclear Reaction Mechanisms (Varenna: Italy)* ed E Gadioli
Balbutsev E B 1991 *Phys. Part. Nucl.* **22** 333

[35] Bastrukov S I and Gudkov V V 1992 *Z. Phys. A* **341** 395
Bastrukov S I, Misicu S and Sushkov A V 1993 *Nucl. Phys. A* **562** 91 (see section 2)
Bastrukov S I and Molodtsova I V 1995 *Phys. Part. Nucl.* **26** 180

[36] Bastrukov S I, Molodtsova I V and Shilov V M 1993 *Int. J. Mod. Phys. E* **2** 731
Bastrukov S I, Molodtsova I V and Shilov V M 1995 *Phys. Rev. C* **25** 1114

[37] Bastrukov S I, Libert J and Molodtsova I V 1997 *Int. J. Mod. Phys. E* **6** 89

[38] Bastrukov S I 1994 *Phys. Rev. E* **49** 3166

[39] Bastrukov S I and Podgainy 1998 *Physica A* **250** 345

[40] Lamb H 1945 *Hydrodynamics* 6th edition (New York: Dover)

[41] Nörenberg W 1983 *Nucl. Phys. A* **409** 191
Nörenberg W 1986 *New Vistas in Nuclear Dynamics* ed Brussard P J and Koch J H (New York: Plenum)
Rhein M *et al* 1992 *Phys. Rev. Lett.* **69** 1340
Rhein M *et al* 1994 *Phys. Rev. C* **49** 250

[42] Mikhailov I N, Mikhailova T I, Di Toro M, Baran V and Brianson Ch 1996 *Nucl. Phys. A* **604** 358

[43] Bastrukov S I, Podgainy D V, Molodtsova I V and Kosenko G 1998 *J. Phys. G: Nucl. Part. Phys.* **24** L1

[44] Bastrukov S I 1993 *Mod. Phys. Lett. A* **8** 711
Bastrukov S I 1996 *Phys. Rev. E* **53** 1917

[45] Bastrukov S I Molodtsova I V Papoyan V V and Weber F 1996 *J. Phys. G: Nucl. Part. Phys.* **22** L33

[46] Ledoux P and Walraven Th 1958 *Handbuch der Physik* ed S Flügge (Berlin: Springer) vol 51 p 353
Ledoux P *Handbuch der Physik* ed S Flügge (Berlin: Springer) vol 51 p 635

[47] Cox J P 1974 *Rep. Prog. Phys.* **37** 563

[48] Unno W, Osaki Y, Ando H and Shibahashi H 1979 *Nonradial Oscillations of Stars* (Tokyo: University Press)

[49] Cox J P 1980 *Theory of Stellar Pulsations* (Princeton: Princeton University Press)

[50] Thorn K S 1969 *Astrophys. J.* **158** 1

Thorn K S 1969 Astrophys. J. **158** 997

[51] Lindblom L and Detweiler S L 1983 Astrophys. J. Suppl. **53** 73

[52] Ipser J R and Managan 1985 Astrophys. J. **292** 517
Ipser J R and Price R H 1991 Phys. Rev. D **43** 1768

[53] Chandrasekhar S and Ferrari V 1991 Proc. Roy. Soc. London A **433** 423
Chandrasekhar S and Ferrari V 1991 Proc. Roy. Soc. London A **434** 449

[54] Cutler C, Lindblom L and Splinter R J 1990 Astrophys. J. **363** 603
Lindblom L 1992 Astrophys. J. **398** 569

[55] Andersson N and Kokkotas K D 1996 Phys. Rev. Lett. **77** 4134

[56] Schaab C, Weber F, Weigel M K and Glendenning N K 1996 Nucl. Phys. A **604** 415

[57] Wieczorek R, Hasse R W and Süssmann 1974 Physics and Chemistry of Fission—Proc. 3rd IAEA Rechester Symposium (IAEA, Vienna, 1973) p 523

[58] Leggett A J 1975 Rev. Mod. Phys. **47** 331

[59] Baym G and Pethick C 1991 Landau Fermi-Liquid Theory (New York: Wiley) section 1.3

[60] Manchester R N and Taylor J H 1977 Pulsars (San Francisco: Freeman)