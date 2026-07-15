Continuum Mech. Thermodyn. (2009) 20: 411–427
DOI 10.1007/s00161-008-0089-6

ORIGINAL ARTICLE

G. Vivier · H. Trumel · F. Hild

# On the stored and dissipated energies in heterogeneous rate-independent systems: theory and simple examples

Received: 18 March 2008 / Accepted: 24 November 2008 / Published online: 6 January 2009
© Springer-Verlag 2008

Abstract The aim of the present work is to determine the amount of dissipated and stored energies in structures containing frictional cracks and elasto-plastic zones. The proposed theory combines micromechanical and thermodynamic tools to calculate both energies. Using simple examples, it is shown that the Taylor–Quinney coefficient is not a constant, and can be much less than the values usually considered (i.e. close to unity).

Keywords Thermodynamics · Micromechanics · Frictional cracks · Plasticity · Dissipation

PACS 83.10.Ff · 83.10.Gr · 83.80.Ab

## 1 Introduction

A wide variety of engineering and fundamental problems involves thermodynamic issues linked to dissipation and energy storage. The well known phenomenon of dissipative or self heating, which occurs especially during dynamic loading, induces a large spectrum of consequences, spanning from thermal hardening in the case of strong shock compaction of porous bodies [1] to various microstructural changes, such as dynamic recrystallization [2], phase transitions [3], or chemical reactions in energetic [4] and non-energetic [5] materials. Thermal softening often occurs, and may induce catastrophic events, such as adiabatic shear failure in metals [6].

The concept of thermodynamic affinity, or thermodynamic force, is also of great concern when seen as a driving force for irreversible mechanisms, be they related to energy storage during hardening processes or to energy release during softening ones. Many models use this concept in the formulation of evolution laws for irreversible processes, such as strain hardening, crack growth, or phase transitions, for example. The concept is particularly salient for localized phenomena, such as the propagation of adiabatic shear bands [7], seismic events [8] or meteorite impacts known to induce rock melting by large-scale friction on faults, and produce characteristic rock structures (pseudotachylytes) after cooling [9].

At least three distinct kinds of quantities must be distinguished, namely immediately recoverable elastic energy, stored energy, not fully recoverable by unloading, and dissipated energy. As they are strongly inter-linked through the two principles of thermodynamics, determining dissipation or energy storage represents the same problem, viewed from two different standpoints. In practise, a correct evaluation of dissipation, for

Communicated by W. H. Müller

G. Vivier · F. Hild
LMT Cachan (UMR CNRS 8535), ENS Cachan, CNRS, Université Paris 6, PRES Université Paris Sud,
61 avenue du Président Wilson, 94235 Cachan Cedex, France
E-mail: vivier@lmt.ens-cachan.fr
E-mail: hild@lmt.ens-cachan.fr

H. Trumel (⊗)
CEA, DAM Le Ripault, 37260 Monts, France
E-mail: herve.trumel@cea.fr

instance, needs also a correct evaluation of the other two components. Formulated differently, this addresses the question of the full determination of the thermodynamic potential.

The question of stored energy is the object of a recent renewal of interest. Since Taylor and Quinney [10] and their first "cold work energy" measurements, various authors attempted to address this question experi- mentally in metals [11-14] and polymers [15-17], by using a variety of techniques, ranging from calorimetry, embedded thermocouples, infrared thermography to ultra fast pyrometry. Two quantities are generally derived from thermal measurements, and should be carefully distinguished. The ratio of dissipated to plastic power, of differential nature, corresponds to the Taylor Quinney coefficient. This ratio may exceed unity, and may even reach values as high as 2, in the case of localization processes [17]. This means that for such paths, the stored energy is possibly released and contributes to instantaneous dissipation. This is an important issue, since the driving force for localized band propagation takes the form of an energy release rate [18-22], in which the stored energy contribution might represent a significant part. The second above-mentioned quantity, of integral nature, is the ratio of dissipated to plastic energies. This ratio is never greater than unity, and can be much lower. For example, Rittel [17] measured values as low as 0.4 in polycarbonate for this integral ratio. Both coefficients are clearly strain and strain-rate dependent, and may vary quite strongly, as reported by most of the above-mentioned authors.

Stored energy is often thought of as related to plasticity and hardening. However, quasi-brittle materials are also capable of storing energy. Although this class of materials behaves in an elastic and damageable manner by microcrack growth and opening at low confining pressure, a brittle to ductile transition is observed at higher confinement, for which they display an elasto-plastic like behavior with strain hardening. This represents a macroscopic manifestation of energy storage, known to be associated with frictional stresses on closed micro- cracks. Hence, dislocation motion or twinning in metals and polymers and frictional microcracks induce very similar consequences at the macroscopic level, and a unified thermodynamic description is desirable. This is all the more the case that quasi-brittle materials may also involve grain plasticity at high confining pressure (see for example the recent illustrative work of Wei and Anand [23]).

An interesting engineering problem is represented by energetic materials ignition under dynamic loading. It has been known for long [4] that these materials (i.e. explosives and solid propellants) ignite by heterogeneous self heating, the so-called "hot spot process". Although the exact mechanisms have not been identified yet, it is strongly suspected [24-26] that frictional microcracks play a decisive role in the ignition process. Many energetic materials display a concrete-like microstructure and quasi-brittle behavior, hence falling in the scope of the present discussion. This problem is similar to that of friction induced explosion in grain silos, except for the granular nature of the media at stake. The prediction of ignition by hot spot heating needs predicting dissipation and thus energy storage. Moreover, it is well known that energy storage induces Bauschinger-like effects in quasi-brittle materials. Reverse frictional sliding, associated with energy release, could also induce ignition during unloading.

Energy storage is known to be linked to material heterogeneity [27-29], in the form of dislocation for- ests in metals or the so-called "microsheared domains" in glassy polymers. This is most of all the case for polycrystals [14,27,30], semi-crystalline polymers, composites or microcracked materials [28] at a higher spatial scale, where material property discontinuities play a major role. In any of these cases, energy storage description is linked to microstructure details. It thus appears that the stored energy must be evaluated using a micromechanical approach, this consequently also standing for free energy and dissipation.

Such a combined thermodynamic and micromechanical approach is particularly suited in the field of dam- age mechanics, and has already provided very interesting micromechanically-based models [31,32]. However, most available micromechanical tools are related to microcracked homogeneous elastic media, which rep- resents a somewhat strong simplification for the description of many engineering or natural materials. The present paper addresses the question of a micromechanically-based thermodynamic model development for heterogeneous elastic materials containing elasto-plastic defects and cracks. It proposes a theoretical meth- odology, generalizing the work of Andrieux et al. [33] to strongly heterogeneous materials and structures. For the present analysis, viscous processes will be excluded and set aside for future work. Further restrictive assumptions are also considered, namely infinitesimal isothermal strains and non interactions between cracks and elasto-plastic parts.

The fundamentals of the approach are described in Sect. 2, which establishes micro to macro relationships for stresses, strains, and proposes the concept of virtual elastically unloaded state for determining the stored energy. The approach is then applied in Sect. 3 to very simple structures, and compared with numerical results provided by the ABAQUS Standard finite element code. In order to keep tractable results, some simplifica- tions are made, but are shown numerically not to entail the predictions accuracy. This methodology is to be

applied to an elementary heterogeneous cell, representative of a plastic-bonded explosive, in a forthcoming paper.

## 2 Theory

### 2.1 Overall stresses and strains

Let us consider a domain $\Omega$, containing perfectly bonded elasto-plastic zones, closed and open cracks, and otherwise made of several perfectly bonded elastic phases (Fig. 1). Following Andrieux et al. [33], the stress-based effective moduli (or Hill–Mandel [34,35]) approach is adopted herein. Hence, a supposedly uniform overall stress $\boldsymbol{\Sigma}$ is applied to the external boundary $\Phi$ of the domain $\Omega$, such that

$$
\boldsymbol{\Sigma} \cdot \boldsymbol{\nu} = \boldsymbol{\sigma} \cdot \boldsymbol{\nu} \quad \text{on } \Phi \tag{1}
$$

where $\boldsymbol{\sigma}$ stands for the microscopic stress tensor, and $\boldsymbol{\nu}$ is the outer unit normal to $\Phi$. Then, neglecting inertial and body forces, the following relationship applies

$$
\boldsymbol{\Sigma} = \frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}(\mathbf{x}) \mathrm{d}V \tag{2}
$$

in which $\mathbf{x}$ is the position vector of any point, and $V$ is the volume of the domain $\Omega$.

Overall strains are defined using the macro-homogeneity relationship

$$
\boldsymbol{\Sigma} : \mathbf{E} = \frac{1}{V} \int_{\Phi} (\boldsymbol{\sigma}(\mathbf{x}) \cdot \boldsymbol{\nu}) \cdot \mathbf{u}(\mathbf{x}) \mathrm{d}S \tag{3}
$$

where $\mathbf{u}(\mathbf{x})$ is the microscopic displacement field. Using (1), Eq. (3) yields

$$
\mathbf{E} = \frac{1}{V} \int_{\Phi} \mathbf{u}(\mathbf{x}) \boxtimes \boldsymbol{\nu} \mathrm{d}S \tag{4}
$$

in which the symbol $\boxtimes$ denotes the symmetrized tensorial product. This relationship may also be put in the more intuitive form

$$
\mathbf{E} = \frac{1}{V} \int_{\Omega} \boldsymbol{\epsilon}(\mathbf{x}) \mathrm{d}V + \frac{1}{V} \int_{\Gamma} \mathbf{u}(\mathbf{x}) \boxtimes \mathbf{n} \mathrm{d}S \tag{5}
$$

where $\boldsymbol{\epsilon}(\mathbf{x})$ is the infinitesimal microscopic strain tensor, defined for all points where the displacement $\mathbf{u}(\mathbf{x})$ is differentiable, and $\mathbf{n}$ is the local unit vector normal to internal surfaces denoted collectively by $\Gamma$. Thus, the overall strain is made up of two contributions, namely, the average of microscopic strains and displacement jumps on internal surfaces. For the sake of simplicity, the spatial dependence of microscopic fields will be dropped throughout the remainder of this paper.

![](./images/811877752046092289_1.jpg)

Fig. 1 Definition of the domain $\Omega$ and dissipative mechanisms

### 2.2 Stresses and strains decomposition

Let us consider the loading case illustrated by Fig. 2a. Point $\mathbf{B}$ is an arbitrary state, characterized by microscopic stresses $\boldsymbol{\sigma}$ and overall stress $\boldsymbol{\Sigma}$. Apply a purely elastic unloading until the overall stress vanishes, thus reaching point $\mathbf{C}$ [36,37]. Since it is well known that elasto-plastic media may exhibit reverse yielding and quasi-brittle media reverse frictional sliding, this unloading path is in general a virtual one.

The state at point $\mathbf{C}$ is characterized by a residual stress field $\boldsymbol{\sigma}^{i}$. Since no external load is applied at this point, this field satisfies the condition

$$
\boldsymbol{\sigma}^{i} \cdot \boldsymbol{v}=\mathbf{0} \quad \text { on } \Phi
$$

thus implying that $\boldsymbol{\sigma}^{i}$ is a self-balanced field

$$
\frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{i} \mathrm{~d} V=\mathbf{0}
$$

This internal stress field is associated with a displacement field $\mathbf{u}^{i}$ and with a strain field $\boldsymbol{\epsilon}^{i}$ wherever $\mathbf{u}^{i}$ is differentiable (Fig. 2b). Owing to the infinitesimal strain and displacement assumption, the classical additive decomposition stands

$$
\boldsymbol{\epsilon}^{i}=\boldsymbol{\epsilon}_{e}^{i}+\boldsymbol{\epsilon}_{p}^{i}
$$

the elastic part being related to internal stresses by

$$
\boldsymbol{\epsilon}_{e}^{i}=\mathbb{C}^{-1}: \boldsymbol{\sigma}^{i}
$$

where $\mathbb{C}$ is the local elastic stiffness tensor. The displacement field $\mathbf{u}^{i}$ may be discontinuous on crack lips.

Since the path $\mathbf{B C}$ is purely elastic, the superposition principle applies (Fig. 2b)

$$
\boldsymbol{\sigma}=\boldsymbol{\sigma}^{i}+\boldsymbol{\sigma}^{\star}
$$

where $\boldsymbol{\sigma}^{\star}$ is the microscopic stress field induced by applying the overall stress, provided plasticity and frictional slip on crack lips are frozen. This field satisfies the boundary condition

$$
\boldsymbol{\sigma}^{\star} \cdot \boldsymbol{v}=\boldsymbol{\Sigma} \cdot \boldsymbol{v} \quad \text { on } \Phi
$$

Since tractions $\boldsymbol{\sigma}^{\star} \cdot \mathbf{n}$ are continuous across elastic and elasto-plastic boundaries, across closed cracks and vanish across open cracks, the following relationship stands

$$
\boldsymbol{\Sigma}=\frac{1}{V} \int \boldsymbol{\sigma}^{\star} \mathrm{d} V
$$

The field $\boldsymbol{\sigma}^{\star}$ is associated with displacement and strain fields $\mathbf{u}^{\star}$ and $\boldsymbol{\epsilon}^{\star}$, respectively, such that

$$
\boldsymbol{\epsilon}^{\star}=\mathbb{C}^{-1}: \boldsymbol{\sigma}^{\star}
$$

![](./images/811877752046092289_2.jpg)

Fig. 2 Stress paths and corresponding displacement decompositions

Since all dissipative processes are frozen along the path $\mathbf{CB}$, the field $\mathbf{u}^\star$ is continuous across closed cracks and elastic and elasto-plastic boundaries, but remains discontinuous across open cracks.

Applying the macro-homogeneity condition to these fields yields the overall elastic strain

$$
\mathbf{E}^{\star}=\frac{1}{V} \int_{\Phi} \mathbf{u}^{\star} \otimes \boldsymbol{\nu} \mathrm{d} S=\frac{1}{V} \int_{\Omega} \boldsymbol{\epsilon}^{\star} \mathrm{d} V+\frac{1}{V} \int_{\Gamma} \mathbf{u}^{\star} \otimes \mathbf{n} \mathrm{d} S
\tag{14}
$$

Using the additivity assumption (8) and the total overall strain definition (4), Eq. (14) becomes

$$
\mathbf{E}^{i}=\mathbf{E}-\mathbf{E}^{\star}=\frac{1}{V} \int_{\Phi} \mathbf{u}^{i} \otimes \mathbf{n} \mathrm{d} S
\tag{15}
$$

such that elasto-plastic additive decomposition follows for overall strains, and

$$
\mathbf{E}^{i}=\frac{1}{V} \int_{\Omega}\left(\boldsymbol{\epsilon}_{e}^{i}+\boldsymbol{\epsilon}_{p}^{i}\right) \mathrm{d} V+\frac{1}{V} \int_{\Gamma} \mathbf{u}^{i} \otimes \mathbf{n} \mathrm{d} S
\tag{16}
$$

Note that the inelastic overall strain contains elastic strain contributions together with local inelastic ones. These elastic contributions are induced by plastic straining and by frictional sliding on closed cracks.

The elastic virtual path $\mathbf{CB}$ can also be decomposed as follows (Fig. 2b). From point $\mathbf{B}$, let us follow a virtual elastic unloading path in which the open cracks are frozen until the fully unloaded point $\mathbf{D}$ is reached. Along $\mathbf{BD}$, the medium behaves as the uncracked material. Then, using again the superposition principle, the stress field $\boldsymbol{\sigma}^{\star}$ decomposes into

$$
\boldsymbol{\sigma}^{\star}=\boldsymbol{\sigma}^{\mathrm{ref}}+\boldsymbol{\sigma}^{d}
\tag{17}
$$

and so do the corresponding displacement and strain fields $\mathbf{u}^{\star}$ and $\boldsymbol{\epsilon}^{\star}$

$$
\mathbf{u}^{\star}=\mathbf{u}^{\mathrm{ref}}+\mathbf{u}^{d}
\tag{18}
$$

$$
\boldsymbol{\epsilon}^{\star}=\boldsymbol{\epsilon}^{\mathrm{ref}}+\boldsymbol{\epsilon}^{d}
\tag{19}
$$

As previously, the fields $\boldsymbol{\sigma}^{\mathrm{ref}}$ and $\boldsymbol{\sigma}^{d}$ are such that

$$
\boldsymbol{\Sigma} \cdot \boldsymbol{\nu}=\boldsymbol{\sigma}^{\mathrm{ref}} \cdot \boldsymbol{\nu} \quad \text { on } \Phi
\tag{20}
$$

$$
\boldsymbol{\sigma}^{d} \cdot \boldsymbol{\nu}=\mathbf{0} \quad \text { on } \Phi
\tag{21}
$$

which implies that

$$
\boldsymbol{\Sigma}=\frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{\mathrm{ref}} \mathrm{d} V
\tag{22}
$$

and that $\boldsymbol{\sigma}^{d}$ is a self-balanced stress field

$$
\frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{d} \mathrm{d} V=\mathbf{0}
\tag{23}
$$

Using again the macro-homogeneity condition for the fields $\boldsymbol{\sigma}^{\mathrm{ref}}$, $\mathbf{u}^{\mathrm{ref}}$ and $\boldsymbol{\epsilon}^{\mathrm{ref}}$ and the property that $\mathbf{u}^{\mathrm{ref}}$ is continuous throughout the body yields the following definition

$$
\mathbf{E}^{\mathrm{ref}}=\frac{1}{V} \int_{\Omega} \boldsymbol{\epsilon}^{\mathrm{ref}} \mathrm{d} V
\tag{24}
$$

Similar arguments as previously provide the additive decomposition

$$
\mathbf{E}^{\star}=\mathbf{E}^{\mathrm{ref}}+\mathbf{E}^{d}
\tag{25}
$$

where

$$
\mathbf{E}^{d}=\frac{1}{V} \int_{\Phi} \mathbf{u}^{d} \otimes \boldsymbol{\nu} \mathrm{d} S=\frac{1}{V} \int_{\Omega} \boldsymbol{\epsilon}^{d} \mathrm{d} V+\frac{1}{V} \int_{\Gamma} \mathbf{u}^{d} \otimes \mathbf{n} \mathrm{d} S
\tag{26}
$$

In this expression, the last term only applies on open cracks, since the path $\mathbf{CD}$ is elastic, the field $\mathbf{u}^{d}$ is continuous across closed cracks.

### 2.3 Energies and dissipation

In a purely mechanical context (i.e. assuming isothermal processes), the free energy of the system at point $\mathbf{B}$ is defined by

$$
\Psi = \frac{1}{V} \int_{\Omega} \frac{1}{2} \boldsymbol{\sigma}: \mathbb{C}^{-1}: \boldsymbol{\sigma} \, \mathrm{d}V
\tag{27}
$$

Using the decomposition of stresses (10), this expression becomes

$$
\Psi = \frac{1}{V} \int_{\Omega} \frac{1}{2} \boldsymbol{\sigma}^{i}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{i} \, \mathrm{d}V + \frac{1}{V} \int_{\Omega} \frac{1}{2} \boldsymbol{\sigma}^{\star}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{\star} \, \mathrm{d}V + \frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{i}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{\star} \, \mathrm{d}V
$$

The last term of the right-hand side of this expression

$$
\widehat{W} = \frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{i}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{\star} \, \mathrm{d}V = \frac{1}{V} \int_{\Omega} \boldsymbol{\sigma}^{i}: \boldsymbol{\epsilon}^{\star} \, \mathrm{d}V
\tag{28}
$$

vanishes, due to (7) and to the fact that $\boldsymbol{\sigma}^{i} \cdot \mathbf{n} \cdot \mathbf{u}^{\star}$ either vanishes on open cracks or remains continuous on closed ones.

One then obtains the following additive decomposition of the overall free energy

$$
\Psi = W^{i} + W^{\star}
\tag{29}
$$

in a stored energy

$$
W^{i} = \frac{1}{V} \int_{\Omega} \frac{1}{2} \boldsymbol{\sigma}^{i}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{i} \, \mathrm{d}V
\tag{30}
$$

and a recoverable one

$$
W^{\star} = \frac{1}{V} \int_{\Omega} \frac{1}{2} \boldsymbol{\sigma}^{\star}: \mathbb{C}^{-1}: \boldsymbol{\sigma}^{\star} \, \mathrm{d}V
\tag{31}
$$

This expression may also be put in the following form

$$
W^{\star} = \frac{1}{2} \boldsymbol{\Sigma}: \mathbf{E}^{\star}
\tag{32}
$$

Combining the classical isothermal expression of the Clausius–Duhem inequality with Eq. (32) yields the well-known expression of dissipation

$$
\mathcal{D} = \boldsymbol{\Sigma}: \dot{\mathbf{E}}^{i} - \dot{W}^{i}
\tag{33}
$$

Hence, the expression of dissipation is obtained in a micromechanical way by combining Eqs. (2), (5), and (30).

With these quantities, two Taylor-Quinney coefficients are defined. First, the differential coefficient $\beta^{d}$

$$
\beta^{d} = \frac{\mathcal{D}}{\boldsymbol{\Sigma}: \dot{\mathbf{E}}^{i}} = \frac{\mathcal{D}}{\mathcal{D} + \dot{W}^{i}}
\tag{34}
$$

and second, the integral coefficient

$$
\beta^{\mathrm{int}} = \frac{W^{d}}{W^{d} + W^{i}}
\tag{35}
$$

where $W^{d}$ is the dissipated energy. Both coefficients evaluate the relative amount of power or energy that are stored or dissipated by irreversible processes.

## 3 Simple case studies

The general relationships derived in Sect. 2 are in principle designed for application to homogenization problems. This is what will be done in a forthcoming paper on a plastic-bonded explosive [38], in view of studying the above-mentioned problem of ignition under low velocity impacts. For the present case, however, the theory will be applied for demonstration purposes on much simpler structures, loaded by homogeneous external stresses. The objective here is twofold. The first one consists in showing how a thermodynamics-based overall model can be built. The second one is to seek simplified formulations of local fields, necessary for the theory to remain tractable, but sufficient to capture the salient thermodynamical features of the overall response of the dissipative heterogeneous media at stake.

### 3.1 The case of plasticity

The following unidimensional example is the simplest way to illustrate the previous developments. The medium (Fig. 3) is composed of two beams of length $\ell$ and of cross section $\ell^{2}$ in perfect contact. The lower one is purely elastic, with a modulus $K_{1}$, whereas the upper one is elastic-perfectly plastic with a modulus $K_{2}$ and a yield stress $\sigma_{y 2}$. The load $\Sigma$ is applied to the whole structure, whose total strain is $E$. The system is represented by the rheological analog given in Fig. 3, in which the total displacement is $u$, and $g$ is the plastic slip in the upper beam.

In a first step, let the inelastic strain $g$ be prescribed in the upper beam in the absence of any external stress, which corresponds to the virtual path $\boldsymbol{O D}$ of Fig. 2a. In this state, the overall strain is $E^{i}$, and the internal stresses are $\sigma_{1}^{i}$ and $\sigma_{2}^{i}$ in the lower and upper beams respectively, given by

$$
\sigma_{1}^{i}=K_{1} E^{i}=-\sigma_{2}^{i}
$$

in which the inelastic strain $E^{i}$ is given by

$$
E^{i}=\frac{u^{i}}{\ell}=\frac{K_{2}}{K_{1}+K_{2}} \frac{g}{\ell} \tag{36}
$$

In a second step, the external load $\Sigma$ is applied. Since the stress $\sigma_{2}$ in the lower beam must be equal to $\sigma_{y 2}$,

$$
\sigma_{2}^{\star}=\sigma_{y 2}-\sigma_{2}^{i}
$$

The external load $\Sigma$ is linked to the overall elastic strain $E^{\star}$ by

$$
\Sigma=K_{\mathrm{eq}} E^{\star}
$$

where $K_{\mathrm{eq}}$ is the overall elastic modulus given by $K_{\mathrm{eq}}=\left(K_{1}+K_{2}\right) / 2$. Then, $\sigma_{2}^{\star}=K_{2} E^{\star}$, and the resulting constitutive law is

$$
\Sigma=\frac{K_{\mathrm{eq}}}{K_{2}}\left(\sigma_{y 2}+K_{1} E^{i}\right)
$$

![](./images/811877752046092289_3.jpg)

Fig. 3 Elasto-plastic composite structure

In order to derive the free energy, let us consider the stress state in the upper (elastic) beam

$$
\sigma_{1}=\sigma_{1}^{i}+\sigma_{1}^{\star}
$$

$$
\sigma_{1}^{i}=K_{1} E^{i}
$$

$$
\sigma_{1}^{\star}=K_{1} E^{\star}
$$

and in the lower beam

$$
\sigma_{2}=\sigma_{2}^{i}+\sigma_{2}^{\star}
$$

$$
\sigma_{2}^{i}=-K_{1} E^{i}
$$

$$
\sigma_{2}^{\star}=K_{2} E^{\star}
$$

The elastic energy, expressed by $W^{\star}=\frac{1}{2}(V_{1} \frac{\{\sigma_{1}^{\star}\}^{2}}{K_{1}}+V_{2} \frac{\{\sigma_{2}^{\star}\}^{2}}{K_{2}})$, with $V_{1}=V_{2}=\ell^{3}$, and $V=V_{1}+V_{2}$, reads

$$
W^{\star}=\frac{1}{2} V \frac{\Sigma^{2}}{K_{\mathrm{eq}}}=\frac{1}{2} V K_{\mathrm{eq}}\left(E-E^{i}\right)^{2}
$$

whereas the stored energy, expressed by $W^{i}=\frac{1}{2}(V_{1} \frac{\{\sigma_{1}^{i}\}^{2}}{K_{1}}+V_{2} \frac{\{\sigma_{2}^{i}\}^{2}}{K_{2}})$, becomes

$$
W^{i}=\frac{1}{2} V \frac{K_{1}}{K_{2}} K_{\mathrm{eq}}\left(E^{i}\right)^{2} \tag{37}
$$

Hence, the free energy is given by

$$
\Psi=W^{\star}+W^{i}=\frac{1}{2} V K_{\mathrm{eq}}\left(E-E^{i}\right)^{2}+\frac{1}{2} V \frac{K_{1}}{K_{2}} K_{\mathrm{eq}}\left(E^{i}\right)^{2} \tag{38}
$$

The classical framework of the thermodynamics of irreversible processes [39–41] can then be used to derive the expressions of the macroscopic stress and dissipation from the following relationships

$$
\Sigma=\frac{\partial \Psi}{\partial E}
$$

$$
\mathcal{D}=X \dot{E}^{i}
$$

where $X=-\frac{\partial \Psi}{\partial E^{i}}$ is the thermodynamic force conjugate to the internal variable $E^{i}$. For monotonic loading, it is straightforward to show that $\Sigma=K_{\mathrm{eq}} \frac{K_{1} E^{i}+\sigma_{2 y}}{K_{2}}$. Reporting in Eq. (38) and derivating with respect to $E^{i}$ yields

$$
X=V \frac{K_{\mathrm{eq}}}{K_{2}} \sigma_{y 2}
$$

The dissipation is then given by

$$
\mathcal{D}=V \frac{K_{\mathrm{eq}}}{K_{2}} \sigma_{y 2} \dot{E}^{i} \tag{39}
$$

and the Taylor-Quinney coefficients become

$$
\beta^{d}=\frac{1}{1+\frac{K_{1}}{\sigma_{y 2}} E^{i}}, \quad \beta^{\mathrm{int}}=\frac{1}{1+\frac{K_{1}}{2 \sigma_{y 2}} E^{i}} \tag{40}
$$

In order to validate this very simple analysis, a numerical exercice is performed using the finite element code ABAQUS Standard with $K_{1}=1$ GPa, $K_{2}=5$ GPa, $\sigma_{y 2}=30$ MPa, and $\ell=1$ m. Figure 4 gives a comparison between theory and calculations, in terms of stress-strain response, whereas Fig. 5 shows the same comparison in energetic terms. It appears that the match in excellent, which is not surprising considering the very simple structure (and behavior) at stake, but lends confidence in the analysis.

![](./images/811877752046092289_4.jpg)

Fig. 4 Stress–strain response of the elasto-plastic composite structure

![](./images/811877752046092289_5.jpg)

Fig. 5 Energetic response of the elasto-plastic composite structure

The differential Taylor-Quinney coefficient is recast as

$$
\beta^{d}=\frac{1}{1+\frac{K_{1}}{K_{2}} \frac{E^{i}}{\epsilon_{y 2}}} \tag{41}
$$

involving elastic property contrast and inelastic global strain normalized to the strain at yield of the elasto-plastic beam. This expression also reads

$$
\beta^{d}=\frac{1}{1+\frac{H}{K_{e q}} \frac{E^{i}}{\epsilon_{y 2}}} \tag{42}
$$

where $H = \frac{\partial \Sigma}{\partial E^{i}}$ is the hardening modulus. This formulation shows that the higher the hardening modulus, the more rapidly the Taylor-Quinney coefficient decreases with inelastic strain. However, Eqs. (40), (41) or (42) show that the Taylor-Quinney coefficient, for this elasto-plastic structure, decreases from an initial value of 1, towards zero, and is thus not constant. The decrease of this coefficient should not be understood as a decrease of dissipation. It is only the dissipated part of the inelastic work that decreases, not the dissipated energy, that increases linearly with inelastic strain, as shown by Eq. (39) and Fig. 5b. It can also be noticed that the main part of the stored energy lies in the elastic beam, since the elastic deformation of the elasto-plastic beam is constant due to yielding.

### 3.2 The case of friction

The case of friction is also analyzed through a very simple medium, illustrated in Fig. 6. The system is made of two elastic beams of equal length $\ell_{x}$, of sections $S_{1}$ and $S_{2}$, and of elastic stiffnesses $K_{1}$ and $K_{2}$. The lower one, referred to as beam 1, is fixed at $x=0$, whereas the upper one is not. A confining pressure $-p$ is applied on the lateral section of the upper beam, and the friction coefficient is $\rho$. The analysis is carried out analytically through a one-dimensional representation of fields along the $x$ coordinate only, as before, other dependencies being neglected. Sliding is allowed on the contact surface, and the contact stress $\tau=\rho p$ is assumed to be uniform on the sliding part of the contact surface. During a real loading, stress mismatches develop along the interface until the friction limit is reached, and frictional sliding begins. This occurs from the beginning of the load. At a given stress state, the contact surface is divided into a sliding part (denoted by $f_{d}$ in Fig. 6) and a non-sliding one. Hence, the sliding surface is analogous to a frictional crack that propagates towards the right end of the structure, and whose tip is located at $x=D$. The internal stress fields are illustrated in Fig. 7. Beginning with the virtually unloaded state $\mathbf{C}$ (i.e. sliding frozen from point $\mathbf{B}$), the local equilibrium of beam 2 reads

$$
\sigma_{2}^{i}(x+\mathrm{d} x)-\sigma_{2}^{i}(x)=\tau \ell_{z} \mathrm{~d} x
$$

This expression is integrated into

$$
\sigma_{2}^{i}(x)=\frac{\tau \ell_{z}}{S_{2}}(x-D)
$$

which accounts for the condition $\sigma_{2}^{i}(D)=0$, in the virtual state $\mathbf{C}$, no external stress is applied. Then, the local equilibrium of the medium becomes

$$
S_{1} \sigma_{1}^{i}+S_{2} \sigma_{2}^{i}=0
$$

such that

$$
\sigma_{1}^{i}(x)=-\frac{\tau \ell_{z}}{S_{1}}(x-D)
$$

Let us note that $\sigma_{2}^{i}(0)=-\tau \ell_{z} D / S_{2}$, such that the residual stress in beam 2 is nonzero on the beam free surface. This justifies the denomination of virtual unloaded state, which can only be obtained by prescribing a

![](./images/811877752046092289_6.jpg)

Fig. 6 Frictional composite structure

![](./images/811877752046092289_7.jpg)

Fig. 7 Internal stress fields: a in the virtually unloaded state C, b resulting from the external load on the virgin medium, and c in the loaded state B

stress on the beam internal free surface, and not from the exterior. This constitutes an internal variable driven process. The inelastic strain $E^{i}$ is given by

$$
E^{i}=\frac{u^{i}(D)}{\ell_{x}}=\frac{\int_{0}^{D} \epsilon_{1}^{i}(x) \mathrm{d} x}{\ell_{x}}=\frac{\tau l_{z} D^{2}}{2 K_{1} S_{1} \ell_{x}}
\tag{43}
$$

In Eq. (43), the inelastic strain is obtained from the value of the displacement $u$ on the external boundary. The same result is obtained by using Eq. (16), i.e. using internal strains and displacement jumps. The second part of the load, i.e. the virtual elastic path, induces the elastic stresses

$$
\sigma_{1}^{\star}=K_{1} E^{\star}=\frac{K_{1}}{K_{\mathrm{eq}}} \Sigma
$$

$$
\sigma_{2}^{\star}=K_{2} E^{\star}=\frac{K_{2}}{K_{\mathrm{eq}}} \Sigma
$$

where the global stiffness $K_{\text {eq }}$ is, as before, given by $K_{\text {eq }}=\frac{K_{1} S_{1}+K_{2} S_{2}}{S_{1}+S_{2}}$. The stress at the free-surface in beam 2 (i.e. $\sigma_{2}^{\star}(0)+\sigma_{2}^{i}(0)$ ) must vanish, which imposes the additional condition

$$
\Sigma=\frac{\tau \ell_{z} K_{\mathrm{eq}}}{S_{2} K_{2}} D
$$

It is now possible to calculate the stored energy $W^{i}=S_{1} \int_{0}^{D} \frac{\left\{\sigma_{1}^{i}\right\}^{2}}{K_{1}} \mathrm{~d} x+S_{2} \int_{0}^{D} \frac{\left\{\sigma_{2}^{i}\right\}^{2}}{K_{2}} \mathrm{~d} x$

$$
W^{i}=\frac{2}{3} V K_{\mathrm{eq}} \frac{\left(E^{i}\right)^{2}}{d}
\tag{44}
$$

where $V=(S_{1}+S_{2})\ell_{z}$ is the total volume of the structure, and $d$ is defined by [28,29,33]

$$
d=\frac{K_{2} S_{2} D}{K_{1} S_{1} \ell_{x}}
\tag{45}
$$

The elastic energy reads

$$
W^{\star}=\frac{1}{2} V \frac{\Sigma^{2}}{K_{\mathrm{eq}}}
$$

Hence, the free energy becomes

$$
\Psi=\frac{1}{2} V K_{\mathrm{eq}}\left(E-E^{i}\right)^{2}+\frac{2}{3} V K_{\mathrm{eq}} \frac{\left(E^{i}\right)^{2}}{d} \tag{46}
$$

In this case, the free energy $\psi$ has the same form as in the plastic case (38), but is corrected by the damage-like variable $d$, which accounts for a new irreversible process, namely the propagation of the frictional crack. Then, the dissipation is given by

$$
\mathcal{D}=X \dot{E}^{i}+Y \dot{d}
$$

where the thermodynamic forces associated with $E^{i}$ and $d$ are defined by

$$
\begin{aligned}
&X=-\frac{\partial \Psi}{\partial E^{i}} \\
&Y=-\frac{\partial \Psi}{\partial d}
\end{aligned} \tag{47}
$$

The dissipated energy becomes

$$
W^{d}=\frac{2}{3} V K_{\mathrm{eq}} \frac{\left(E^{i}\right)^{2}}{d}
$$

and therefore, the Taylor-Quinney coefficients are given by

$$
\beta^{d}=\frac{1}{2}, \quad \beta^{\mathrm{int}}=\frac{1}{2} \tag{48}
$$

As before, analytical predictions are compared with numerical results with $K_{1}=1$ GPa, $K_{2}=10$ GPa, $\ell_{x}=0.5$ m, $l_{y}=0.01$ m, and $\ell_{z}=0.1$ m. Mesh size independence was checked. The simulations are performed in three steps. The confining pressure is first applied. Then, the tensile load is applied up to a pre-selected value. Then, the surfaces in contact are tied together during unloading, so that no reverse friction occurs. Although the theory and the numerical model do not employ the same virtual paths, they lead to remarkably close results, as illustrated by Figs. 8 and 9. The small discrepancies displayed in Fig. 9a and c are commented upon in the next section. It is remarkable that the Taylor-Quinney coefficient is constant and independent of the geometrical details of the system, and of its stiffnesses as well. The fact that it remains equal to a half means that a large amount of energy is stored during loading, and that taking a Taylor-Quinney coefficient close to unity would severely overestimate the temperature field. Conversely, the stored energy is likely to be at least partially released during unloading. In this respect unloading could be a quite significant process regarding internal heating.

![](./images/811877752046092289_8.jpg)

Fig. 8 Stress-strain response of the frictional composite structure

![](./images/811877752046092289_9.jpg)

Fig. 9 Energetic response of the frictional composite structure

### 3.3 Combining plasticity and friction

A slightly more involved case is studied now. The same structure as in Fig. 6 is considered, except that the upper beam is now elasto-plastic with a yield stress $\sigma_{y 2}$. The beginning of the loading process is identical to the frictional case of Sect. 3.2, but now yielding occurs when $\sigma_{2}^{max }=\sigma_{y 2}^{\prime}$, where $\sigma_{y 2}^{\prime}$ accounts for the effect of confining stress $-p$

$$
\sigma_{y 2}=\frac{1}{\sqrt{2}} \sqrt{\left(\sigma_{y 2}^{\prime}+p\right)^{2}+p^{2}+\sigma_{y 2}^{2}}
\tag{49}
$$

At the onset of yielding in the upper beam, the length $D$ of the frictional zone is $D=D_{1}$, and it is shown that

$$
\sigma_{y 2}^{\prime}=\frac{\tau \ell_{z}}{S_{2}} D_{1}
$$

whereas the inelastic strain is given by

$$
\mathrm{E}^{i}=\mathrm{E}_{1}^{i}=\frac{\tau \ell_{z} D_{1}^{2}}{2 K_{1} S_{1} \ell_{x}}=\frac{S_{2}}{K_{1} S_{1}} \frac{D_{1}}{2 \ell_{x}} \sigma_{y 2}^{\prime}
\tag{50}
$$

If the internal virtual stress $\sigma_{0}$ increases, friction stops and is replaced by yielding in the upper beam. This situation is illustrated by the internal stress fields of Fig. 10. Then, the inelastic strain $\mathrm{E}_{1}^{i}$ is supplemented by $\mathrm{E}_{2}^{i}$

$$
\mathrm{E}^{i}=\mathrm{E}_{1}^{i}+\mathrm{E}_{2}^{i}
$$

given by

$$
\mathrm{E}_{2}^{i}=\frac{S_{2}}{K_{1} S_{1}}\left(-\sigma_{0}-\sigma_{y 2}^{\prime}\right)
$$

![](./images/811877752046092289_10.jpg)

Fig. 10 Internal stresses in the upper beam of the frictional-plastic composite structure

![](./images/811877752046092289_11.jpg)

Fig. 11 Stress-strain response of the frictional-plastic composite structure

The stored energy then becomes

$$
W^{i}=\frac{2 V}{3} \frac{K_{\mathrm{eq}}}{d_{1}}\left(\mathrm{E}_{1}^{i}{ }^{2}+\mathrm{E}_{2}^{i} \frac{D_{1}}{\ell_{x}}\left(\frac{3}{4} \mathrm{E}_{2}^{i}+\frac{3}{2} \mathrm{E}_{1}^{i}\right)\right)
$$

where $d_{1}$ is given by

$$
d_{1}=\frac{K_{2} S_{2} D_{1}}{K_{1} S_{1} \ell_{x}}
$$

and the dissipated energy reads

$$
W^{d}=\frac{2}{3} V K_{\mathrm{eq}} \frac{\left(\mathrm{E}_{1}^{i}\right)^{2}}{d_{1}}+\frac{V K_{\mathrm{eq}}}{K_{2}}\left(1+\frac{D_{1}}{2 \ell_{x}}\right) \sigma_{y 2}^{\prime} \mathrm{E}_{2}^{i}
$$

These analytical results are then compared with simulations using $\sigma_{y 2}=1.5 \mathrm{GPa}$, i.e. $\sigma_{y 2}^{\prime}=1.327 \mathrm{GPa}$ in Figs. 11 and 12. Again, the match between analytical and numerical results is good. Particularly illustrative is Fig.12c, showing the transition between friction, associated with a value of one half of the Taylor-Quinney coefficient, and plasticity, involving much higher values. The discrepancies already observed in the preceding section are still present in Figs. 11a and 12. Figure 13a shows the longitudinal stress fields in the composite structure in the loaded state (upper view) and in the virtual unloaded state (lower view). As expected, these

![](./images/811877752046092289_12.jpg)

Fig. 12 Energetic response of the frictional-plastic composite structure

![](./images/811877752046092289_13.jpg)

Fig. 13 Illustration of two-dimensional effects

fields display a regular longitudinal gradient in the largest part of the structure. However, this state is perturbed by a two-dimensional effect near the left edge of the upper beam. This is accompanied by complex transverse stress fields, as shown in Fig. 13b, similar to a crack tip-like stress field. Hence, as long as the size of this

perturbed zone is comparable to the size of the frictional length, a two-dimensional effect is perceived at the macroscopic scale. This effect vanishes as the frictional length grows, and the analytical result is recovered.

## 4 Conclusion
The framework given herein combines scale transitions and continuum thermodynamics, in the limit of the isothermal assumption. It is used to *derive* the stored part of the free energy, which is most of the time *postulated*. The illustrations given above are useful to understand the thermodynamic mechanisms of energy storage. A more realistic scheme is developed in a forthcoming paper, in relation to explosive ignition, for which the self-heating phenomenon is crucial.

The goal of this paper is to establish the framework for calculating stored and dissipated energies in heterogeneous structures or representative volume elements. However, the present homogenization theory is not complete. Although a general formulation is given for the inelastic strains, the definition of additional overall internal variables was eluded, and is the subject of ongoing work.

As a final remark, the major assumptions are the time-independent character of the constituents behavior and the limitation to isothermal processes, which limit the field of application of the present work. Extending it to viscous non-isothermal processes should be the next steps, and will strongly enhance the interest of the theory.

### Acknowledgments
The authors acknowledge useful discussions with Prof. F. A. Leckie on the subject of the present paper. This work was funded by a CEA grant.

## References
1. Al'tshuler, L.V.: Use of shock waves in high pressure physics. Soviet Phys. Uspekhi **8**(1), 52–91 (1965)
2. El Wahabi, M., Gavard, L., Montheillet, F., Cabrera, J.M., Prado, J.M.: Effect of initial grain size on dynamic recrystallization in high purity austenitic stainless steels. Acta Mater. **53**, 4605–4612 (2005)
3. Abeyaratne, R., Knowles, J.K.: Impact-induced phase transitions in thermoelastic solids. Phil. Trans. R. Soc. Lond. A **355**, 843–867 (1997)
4. Bowden, F.P., Yoffe, A.F.: Initiation and Growth of Explosion in Liquids and Solids. Cambridge University Press, Cambridge, UK (1952)
5. Chen, H.C., Lasalvia, J.C., Nesterenko, V.F., Meyers, M.A.: Shear localization and chemical reaction in high strain, high strain-rate deformation of Ti–Si mixture powders. Acta Mater. **46**(9), 3033–3046 (1998)
6. Marchand, A., Duffy, J.: An experimental study of the formation process of adiabatic shear bands in a structural steel. J. Mech. Phys. Solids **36**(3), 251–283 (1988)
7. Dinzart, F., Molinari, A.: Structure of adiabatic shear bands in thermo-viscoplastic materials. Eur. J. Mech. A/Solids **17**, 923–938 (1998)
8. Wu, L., Liu, S., Wu, Y., Wang, C.: Precursors for rock fracturing and failure. Part I. IRR image abnormalities. Int. J. Rock Mech. Mining Sci. **43**, 473–482 (2006)
9. Bjornerud, M., McLoughlin, J.F.: Pressure-related feedback processes in the generation of pseudotachylytes. J. Struct. Geol. **26**, 2317–2323 (2004)
10. Taylor, G.I., Quinney, H.: The latent energy remaining in a metal after cold working. Proc. R. Soc. Lond. A **143**, 307–326 (1934)
11. Chrysochoos, A., Maisonneuve, O., Martin, G., Caumon, H., Chezeaux, J.-C.: Plastic and dissipated work and stored energy. Nucl. Eng. Des. **114**, 323–333 (1989)
12. Mason, J.J., Rosakis, A.J., Ravichandran, G.: On the strain and strain rate dependence of the fraction of plastic work converted to heat: an experimental study using high speed infrared detectors and the Kolsky bar. Mech. Mater. **17**, 135–145 (1994)
13. Kapoor, R., Nemat-Nasser, S.: Determination of temperature rise during high strain rate deformation. Mech. Mater. **27**, 1–12 (1998)
14. Oliferuk, W., Maj, M., Raniecki, B.: Experimental analysis of energy storage rate components during tensile deformation of polycrystals. Mater. Sci. Eng. A **374**, 77–81 (2004)
15. Adams, G.W., Farris, R.J.: Latent energy of deformation of amorphous polymers. 1. Deformation calorimetry. Polymer **30**, 1824–1828 (1989)
16. Hasan, O.A., Boyce, M.C.: Energy storage during inelastic deformation of glassy polymers. Polymer **34**, 5085–5092 (1993)
17. Rittel, D.: On the conversion of plastic work to heat during high strain rate deformation of glassy polymers. Mech. Mater. **31**, 131–139 (1999)
18. Chrysochoos, A., Louche, H.: An infrared image processing to analyse the calorific effects accompanying strain localisation. Int. J. Eng. Sci. **38**, 1759–1788 (2000)
19. Bonnet-Lebouvier, A.-S., Molinari, A., Lipinski, P.: Analysis of the dynamic propagation of adiabatic shear bands. Int. J. Solids Struct. **39**(16), 4249–4269 (2002)
20. Ranc, N., Wagner, D.: Some aspects of Portevin-Le Chatelier plastic instabilities investigated by infrared pyrometry. Mater. Sci. Eng. A **394**(1–2), 87–95 (2005)

21. Rittel, D., Wang, Z.G., Merzer, M.: Adiabatic shear failure and dynamic stored energy of cold work. Phys. Rev. Lett. **96**, 075502 (2006)

22. Yang, Y., Wang, B.F.: Dynamic recrystallization in adiabatic shear band in titanium. Mater. Lett. **60**(17–18), 2198–2202 (2006)

23. Wei, Y., Anand, L.: On micro-cracking, inelastic dilatancy, and the brittle–ductile transition in compact rocks: a microme- chanical study. Int. J. Solids Struct. **45**, 2785–2798 (2008)

24. Field, J.E., Swallow, G.M., Heavens, S.M.: Ignition mechanisms of explosives during mechanical deformation. Proc. R. Soc. Lond. A **382**, 231–244 (1992)

25. Dienes, J.K.: A unified theory of flow, hot spots, and fragmentation, with an application to explosive sensitivity. In: Davison, L., Grady, D.E., Shahinpoor, M. (eds.) High Pressure Shock Compression of Solids II, pp. 366–398. Springer, Berlin (1996)

26. Bennett, J.G., Haberman, K.S., Johnson, J.N., Asay, B.W., Henson, B.F.: A constitutive model for the non-shock ignition and mechanical response of high explosives. J. Mech. Phys. Solids **46**(12), 2303–2322 (1998)

27. Bever, M.B., Holt, D.L., Titchener, A.L.: The stored energy of cold work. In: Chalmers, B., Christian, J.W., Massalski, T.B. (eds.) Prog. Mat. Sci., vol. 17. Pergamon Press, NY, USA (1973)

28. Burr, A., Hild, F., Leckie, F.A.: Micromechanics and continuum damage mechanics. Arch. Appl. Mech. **65**, 437–456 (1995)

29. Boudon-Cussac, D., Hild, F., Pijaudier-Cabot, G.: Tensile damage in concrete: analysis of an experimental technique. J. Eng. Mech. ASCE **125**(8), 906–913 (1999)

30. Aravas, N., Kim, K.-S., Leckie, F.A.: On the calculations of the stored energy of cold work. ASME J. Eng. Mater. Tech- nol. **112**, 465–470 (1990)

31. Halm, D., Dragon, A.: An anisotropic model of damage and frictional sliding for brittle materials. Eur. J. Mech. A/Solids **17**(3), 439–460 (1998)

32. Pensée, V., Kondo, D., Dormieux, L.: Micromechanical analysis of anisotropic damage in brittle materials. J. Eng. Mech. **128**(8), 889–897 (2002)

33. Andrieux, S., Bamberger, Y., Marigo, J.-J.: Un modèle de matériau microfissuré pour les bétons et les roches. J. Méc. Théor. Appl. **5**, 471–513 (1986)

34. Hill, R.: The essential structure of constitutive laws for metal composites and polycrystals. J. Mech. Phys. Solids **15**, 79–95 (1967)

35. Mandel, J.: Contribution théorique à l’étude de l’écrouissage et des lois de l’écoulement plastique. In: Becker, E., (ed.) Proc. 11th Int. Cong. Appl. Mech. Springer, Berlin, RFA, pp. 502–509 (1964)

36. Volterra, V.: Sur l’équilibre des corps élastiques multiplement connexes. Annales Scientifiques de l’Ecole Normale Supéri- eure, Paris (France) **24**, 401–518 (1907)

37. Love, A.E.H.: The Mathematical Theory of Elasticity. Cambridge University Press, Cambridge (1927)

38. Vivier, G., Hild, F., Labrunie, M., Lambert, P., Trumel, H.: Studying and modelling a pressed HMX-based energetic material. In: 17th DYMAT Tech. Meeting, September 6–7. Cambridge, UK (2007)

39. Coleman, B.D., Gurtin, M.E.: Thermodynamics with internal state variables. J. Chem. Phys. **47**(2), 597–613 (1967)

40. Germain, P., Nguyen, Q.S., Suquet, P.: Continuum thermodynamics. ASME J. Appl. Mech. **50**, 1010–1020 (1983)

41. Lemaitre, J., Chaboche, J.-L.: Mechanics of Solid Materials. Cambridge University Press, Cambridge (1990)