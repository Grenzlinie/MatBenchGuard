
# Study of a Nonlocal Density scheme for electronic–structure calculations

Maurizia Palummo \( ^{(a)} \) , Giovanni Onida \( ^{(a)} $ , Rodolfo Del Sole \( ^{(a)} \) , Massimiliano Corradini \( ^{(a)} $ 

(a) Istituto Nazionale per la Fisica della Materia - Dipartimento di Fisica dell' Università di

Roma Tor Vergata

Via della Ricerca Scientifica, I-00133 Roma, Italy

Lucia Reining \( ^{(b)} \) 

(b) Laboratoire des Solides Irradiés, UMR7642 CNRS – CEA, École Polytechnique, F-91128

Palaiseau, France

(October 23, 2018)

## Abstract

An exchange-correlation energy functional beyond the local density approximation, based on the exchange-correlation kernel of the homogeneous electron gas and originally introduced by Kohn and Sham, is considered for electronic structure calculations of semiconductors and atoms. Calculations are carried out for diamond, silicon, silicon carbide and gallium arsenide. The lattice constants and gaps show a small improvement with respect to the LDA results. However, the corresponding corrections to the total energy of the isolated atoms are not large enough to yield a substantial improvement for the cohesive energy of solids, which remains hence overestimated as in the LDA.
 

## I. INTRODUCTION

Calculations based on the Kohn-Sham  \( [1] \)  formulation of density functional theory (DFT) \( [2] \)  have become a prominent tool in condensed matter physics. Current work is dominated by local density approximation (LDA) studies, in which the exchange-correlation potential is a local function of the density  \( [1,3] \) .

Despite its enormous success, the local density approximation has some shortcomings which motivated the increasing interest in approaches beyond it, like the Generalized Gradient Approximation (GGA)  \( [4,5] \) , the average-density approximation (ADA), and the weighted density approximation (WDA)  \( [6] \) . However, at present none of these methods has replaced the simpler local density scheme, because they do not always yield systematic and consistent improvements with respect to the LDA, and because, except the GGA, they could not be implemented in a computationally tractable fashion.

It is therefore worthwhile to carry out electronic structure calculations using other approximations for the exchange-correlation energy functional. Kohn and Sham  \( [1] \)  proposed, together with the LDA, a correction to it which is exact up to the second order in the density fluctuations with respect to the average electron density n; hence it is appropriate for weakly inhomogeneous systems. It involves, as a basic ingredient, the exchange correlation kernel of the homogeneous electron gas,  \( K_{xc}^{heg}(\vec{r}-\vec{r}^{\prime}) \) , describing the change of the exchange-correlation potential at  \( \vec{r} \)  induced by a density change at  \( \vec{\tau}^{\prime} \) . This functional was ruled out since Gunnarson and al.  \( [6] \)  showed that different choices of how to include higher order terms may lead to very different results for the total energy in strongly inhomogeneous systems.

In fact this functional has never been applied to real solids, while the LDA became the state-of-the-art of total-energy and band-structure calculations. Keeping into account that several realistic parametrizations of  \( K_{xc}^{heg} \)  based on Quantum Monte Carlo (QMC) calculations are now available, we think that the relative simplicity of this non-LDA (NLD) functional, and its avoiding gradient expansions to treat inhomogeneity, suggest a further
 

attempt to apply it to solids.

In Section II we describe in detail the NLDA functional and we propose a derivation which eliminates some arbitrariness in the treatment of higher-order density fluctuations. The choice which we adopt minimizes the error in the case of strongly inhomogeneous systems. In section III we describe the calculations performed for bulk silicon, diamond, silicon carbide and gallium arsenide, and the results of total energy calculations for atoms and pseudoatoms, as well as for a surface. The conclusions are drawn in Section IV.

## II. NLDA EXCHANGE-CORRELATION ENERGY FUNCTIONAL

In this Section we derive a correction to the LDA exchange-correlation (XC) energy for a weakly inhomogeneous system. Although the final result will be coincident with a NLDA XC functional introduced by Kohn and Sham [1], the derivation given here is different. It suggests a wider validity range of the resulting functional, and renders the choice of how to include higher orders less arbitrary.

Let us consider the exchange-correlation potential  \(  V_{xc}(\vec{r})  \)  in a weakly inhomogeneous system. We can write:

 \[ V_{x c}([n],\vec{r})=V_{x c}^{L D A}(n(\vec{r}))+\int d\vec{r}^{\prime}K_{x c}(\vec{r},\vec{r}^{\prime})[n(\vec{r}^{\prime})-n(\vec{r})]+.... \quad (1) \] 

where

 \[ K_{x c}(\vec{r},\vec{r}^{\prime})=\frac{\delta V_{x c}([n],\vec{r})}{\delta n(\vec{r}^{\prime})} \quad (2) \] 

is the functional derivative of the XC potential with respect to the density. The first term on the right-hand side of (1) is obtained assuming, as in the LDA, that the electron density  \( n(\vec{r}^{\prime}) \)  is constant, equal to  \( n(\vec{r}) \) . The second term is an expansion of  \( V_{xc}([n],\vec{r}) \)  to first-order in  \( [n(\vec{r}^{\prime}) - n(\vec{r})] \) , while higher-order terms are neglected. Calculating  \( V_{xc}([n],\vec{r}) \)  up to the first-order in  \( [n(\vec{r}^{\prime}) - n(\vec{r})] \) ,  \( K_{xc}(\vec{r},\vec{r}^{\prime}) \)  can be approximated at the zero-order level, namely by using the homogeneous electron-gas (HEG) form:
 

 \[ V_{x c}([n],\vec{r})=V_{x c}^{L D A}(n(\vec{r}))+\int d\vec{r}^{\prime}K_{x c}^{h e g}(\vec{r}-\vec{r}^{\prime};\tilde{n}(\vec{r},\vec{r}^{\prime}))[n(\vec{r}^{\prime})-n(\vec{r})]+.....\; \quad (3) \] 

where  \(  K_{xc}^{heg}(\vec{r} - \vec{r}'; \tilde{n}(\vec{r}, \vec{r}'))  \)  is the XC kernel (2) for the HEG (jellium) of density  \(  \tilde{n}(\vec{r}, \vec{r}')  \) . Strictly speaking,  \(  \tilde{n}(\vec{r}, \vec{r}')  \)  should be taken equal to  \(  n(\vec{r})  \) . However, any choice in the range between  \(  n(\vec{r})  \)  and  \(  n(\overrightarrow{r})  \)  will not alter the resulting XC potential to first order in  \(  n(\vec{r}) - n(\vec{r}')  \) . The choice of  \(  \tilde{n}(\vec{r}, \vec{r}')  \)  will be discussed below.

The next problem to solve is to find the XC-energy functional  \( E_{xc}[n] \)  whose functional derivative  \( \delta E_{xc}/\delta n(r) \)  yields the XC-potential (3). If  \( \tilde{n}(\vec{r},\vec{r}') \)  is a symmetric function of  \( \vec{r} \)  and  \( \vec{r}' \) , we can easily show that the functional

 \[ E_{x c}[n]=E_{x c}^{L D A}[n]-\frac{1}{4}\int d\vec{r}\int d\vec{\imath}^{\prime}K_{x c}^{h e g}(\vec{r}-\vec{\imath}^{\prime};\tilde{n}(\vec{r},\vec{\imath}^{\ prime}))[n(\vec{r}^{\prime})-n(\vec{r})]^{2} \quad (4) \] 

yields the following XC-potential:

 \[ \begin{align*}V_{xc}([n],\vec{r})&=V_{xc}^{LDA}(n(\vec{r}))+\int d\vec{r}^{\prime}K_{xc}^{heg}(\vec{r}-\vec{r}^{\prime};\tilde{n}(\vec{r},\vec{r}^{\prime}))[n(\vec{r}^{\prime})-n(\vec{r})]\\-(1/4)\int d\vec{r}^{\prime \prime}\int d\vec{r}\frac{dK_{xc}^{heg}(\vec{r}^{\prime \prime}-\vec{r}^{\prime};\tilde{n}(\vec{r}^{\prime \prime},\vec{r}^{\prime}))}{dn}\frac{\delta\tilde{n}(\vec{r}^{\prime \prime},\vec{r}^{\prime})}{\delta n(\vec{r})}[n(\vec{r}^{\prime})-n(\vec{r}^{\ prime})]^{2}.\end{align*} \quad (3a) \] 

The XC-correlation potential (3a) is coincident with our starting point (3) up to terms of first order in the density variation  \(  n(\vec{r}') - n(\vec{r})  \) . Hence the XC-energy functional (4) is consistent up to the second order in  \(  [n(\vec{r}') - n(\vec{r})]  \)  with the XC-potential (3).

The exchange-correlation energy functional (4) becomes equal to the NLDA of Kohn and Sham if the density argument in  \( K_{xc}^{heg} \) ,  \( \tilde{n}(\vec{r},\vec{r}') \) , is replaced by the average electron density n. Previous derivations of it were based on a partial summation of the gradient expansion [1], or on assuming weak density fluctuations around the average density [7]. The present derivation is based on less restrictive assumptions: considering in fact that the XC kernel is generally of short range in  \( |\vec{r}-\vec{r}'| \)  (according to Hubbard's expression [8], we expect that it decays after a few reciprocal Fermi wavevectors), the density variation  \( [n(\vec{r}')-n(\vec{r})] \)  must be small within this range, in order to allow the neglect of higher-order terms. We refer to this situation as to weak inhomogeneity on the scale of the non-locality range of  \( K_{xc}^{heg}(\vec{r}-\vec{r}';n) \) , or shortly as to weak inhomogeneity.
 

If we consider an inhomogeneous system, the density argument in the HEG XC kernel in (4) has some arbitrariness: in fact, since the expression is valid up to the second order in density fluctuations, the XC kernel has to be correct to zeroth order in it. This means that in principle any density close to  \( n(\vec{r}) \)  and  \( n(\vec{\tau}) \)  can be used therein. The simplest choices which preserve the symmetry in  \( \vec{r} \)  and  \( \vec{r}^{\prime} \)  are: (i)  \( n[(\vec{r} + \vec{r}^{\prime})/2] \)  and (ii)  \( [n(\vec{r}) + n(\vec{r}^{\prime})]/2 \) . Choice (ii) is consistent with the ansatz (1), where the LDA term is understood as the zero order contribution of an expansion around constant density, and the second term is a linear expansion of the XC potential at  \( \vec{r} \)  in the change of the density at any point  \( \vec{r}^{\prime} \) , from the value assumed in the LDA term,  \( n(\vec{r}) \) , to the actual value  \( n(\vec{\tau}^{\prime}) \) . In a common Taylor expansion, the derivative would be calculated at the initial point  \( \tilde{n}(\vec{r}, \vec{r}^{\prime}) = n(\vec{r}) \) . This choice would however not satisfy the symmetry requirement on  \( \tilde{n}(\vec{r}, \vec{r}^{\prime}) \) . Moreover, one can be easily convinced that the error is smaller if the derivative is calculated at the central point of the interval, namely at  \( (n(\vec{r}) + n(\vec{r}^{\prime}))/2 \) . If the function is truly linear, the derivatives at these two points are obviously equal and both points yield the exact result. Calculating the derivative at the central point of the interval, however, yields the exact result also in the case of a quadratic function. Choice (i), on the other hand, has also been discussed in Ref. [6], where it has been demonstrated that it can lead to very different results in the cases of strongly inhomogeneous systems, and even to infinite values of the XC energy. Choice (i) is in fact ruled out by our derivation, since  \( n(1/2(\vec{r} + \vec{r}^{\prime})) \)  has no reason to lie in the density range of  \( n(\vec{r}) \)  and  \( n(\vec{\tau}^{\prime}) \) . Since the failure of (i) has however been proposed as an argument against the use of the functional, we analyze below the reasons of such different results and we show that choice (ii) not only is consistent with our derivation, but also minimizes the error in real systems with respect to choice (i).

The main source of error is that  \( K_{xc}^{heg}(\vec{r}-\vec{r}^{\prime};n) \)  becomes of long range when n is vanishingly small. This is understood on the ground of self-interaction arguments [6] and occurs even in the simplest model of  \( K_{xc}^{heg}(\vec{r}-\vec{r}^{\prime};n) \) , namely Hubbard's model [8]. No relevant error occurs in (4) when both  \( \vec{r} \)  and  \( \vec{r}^{\prime} \)  are in regions of small electron density, since in this case the factor  \( [n(\vec{r}^{\prime})-n(\vec{r})]^{2} \)  vanishes. Serious errors can instead occur when  \( \vec{r} \)  (or  \( \vec{r}^{\prime} \) ) is in a
 

region of small density, while  \( \vec{r}^{\prime} \)  (or  \( \vec{r} \) ) is in a region of relevant density. If we make choice (i),  \( n[(\vec{r}^{\prime}+\vec{r}^{\prime})/2] \)  may happen to be also small, and the resulting kernel of long range. A very big wrong contribution may be added to the XC energy in this case. If, on the other hand, we make choice (ii), the density appearing in the kernel,  \( [n(\vec{r})+n(\vec{r}^{\prime})]/2 \)  is non-vanishing and  \( K_{xc}^{hex}(\vec{r}^{\prime}-\vec{r}^{\prime};n) \)  is of short range in all relevant cases. We can still get a wrong contribution to the XC energy, but certainly smaller in absolute value than that of choice (i).

We adopt hence choice (ii) in the functional (4). The residual error can be checked a posteriori by comparing the expectation values over the electron wavefunctions of the XC potentials of eq.(3) and (3a) (with  \( (n(\vec{r}) + n(\vec{r}^{\prime}))/2 \)  in place of  \( \tilde{n}(\vec{r}, \vec{r}^{\prime}) \) ): if the assumption of weak inhomogeneity is valid, they must be very close to each other. We verified that this is not the case for atoms, but it is true for the analyzed semiconductors. The deep reason for this is that electrons in valence or lower conduction states, which are of interest in most electronic-structure calculations, have very small probabilities of being found in regions of small charge density, where wrong contributions to the XC functional can be generated as described above. In any case we used form (3a), which is fully consistent with our ansatz (4) for the XC energy.

The XC kernel  \(  K_{xc}^{hex}(q;n)  \)  of the HEG (Fourier transformed from  \( \vec{r}-\vec{r}^{\prime} \)  to  \( \vec{q} \) ) is strictly related to the so-called static local-field factor  \(  G(q;n) : K_{xc}^{hex}(q;n) = -(4\pi e^{2}/q^{2})G(q;n)  \) . We have carried out numerical calculations using different forms of  \(  G(q;n)  \) : i) a Hubbard-like form, i.e.  \(  G(q;n) = q^{2}/2(q^{2} + q_{TF}^{2}(n))  \) , where  \(  q_{TF}(n)  \)  is the Thomas Fermi wavevector at density n; ii) two more realistic models for  \(  G(q;n)  \) , the first based on the known asymptotic behaviors of  \(  G(q;n)  \)  for small and large q, and on approximate calculations in between –the model of Ichimaru and Utsumi [9] (IU)–, and the second based on a parametrization of QMC data by of Moroni and Senatore [10], recently proposed by some of us (CPOD) [11].

The last two models of  \(  G(q; n)  \)  differ mainly in the asymptotic behavior for large q (which in the IU model fails to reproduce the exact result, i.e.  \(  G(q; n) \sim q^{2}  \) ), and in the presence, in the IU model, of a logarithmic singularity for  \( q = 2q_{f} \)  ( \( q_{f} \)  is the Fermi wavevector), which
 

does not appear in the CPOD  \(  G(q; n)  \) . (For a more detailed discussion of these differences, see Ref. [11].) The resulting XC kernels in real space are quite similar, as shown in Fig. 1, where they are plotted for  \( r_{s} = 2 \) . In the first case, the presence of oscillations due to the logarithmic singularity leads to a more difficult convergence of the integrals, without affecting very much the final results. Hence, in the following we adopt the CPOD parametrization.

## III. RESULTS

## A. Bulk systems

Self-consistent electronic structure calculations were carried out using pseudopotentials and a plane wave basis. We generated the pseudopotentials on a numerical grid, using the method proposed by Troullier and Martins  \( [12] \)  for Silicon and Diamond, while for Ga and As we followed the scheme introduced by Hamann  \( [13,14] \) . All the pseudopotentials were used in the fully separable representation of Kleinman and Bylander  \( [15] \) , after having checked that no ghost-state is generated. In the case of GaAs non linear core corrections were included  \( [16] \) . Plane-wave basis sets with a cutoff of 18 Rydberg for Silicon, 20 Ryd for GaAs, and 40 Ryd for Diamond and Silicon Carbide are needed to achieve good convergence. Ten special points  \( [17] \)  were used in Brillouin Zone integrations.

The NLDA XC functional (4) and the XC potentials (3) and (3a) were calculated by integration in real space (on a grid of  \( 16 \times 16 \times 1 \)  points for Si, GaAs and Diamond, and of  \( 24 \times 24 \times 1 \)  points for SiC), with a cutoff  \( r_{c} \)  in  \( |\vec{r} - \vec{r'}| \) . Fig. 2 shows the convergence of the total energy of Si (we plot the correction to the LDA value), as a function of  \( r_{c} \) , for the two more realistic forms, IU and CPOD, of  \( K_{xc}^{heg} \) . The results are very similar, but the integrals calculated with the second model converge faster with respect to  \( r_{c} \) . Clearly the computational effort for the integration increases linearly with the number of grid points used to calculate the integrals. However, two factors contribute in limiting the numerical effort requested by the present NLDA method:
 

i) the convergence with  \( r_{c} \)  is fast, showing the short range character of  \( K_{xc}^{heg} \)  both for silicon and for the other materials considered;

ii) since, as we verified, self-consistency effects are very small, all the calculations can be done starting from the LDA wavefunctions and converge to the true NLDA ground-state in a very small number of iterations.

We have checked the validity of the assumption of weak inhomogeneity, by calculating, in the case of Silicon and Diamond, the expectation values of both the XC potentials (3) and (3a): they differ by less than 0.01 eV, showing that terms of second order in the density variations are negligible in the XC potential, and therefore that Si and Diamond are weakly inhomogeneous systems in the sense discussed in Section II. The same is true for cubic SiC, since the energy changes between NLDA and LDA are of the same order as in Si. However in the case of GaAs, where the effect of the large core charge density is partially taken into account through the non linear core corrections, the differences are as large as 0.3 eV, which suggests that the density argument should be chosen more carefully. In principle the pseudopotentials used must be generated carrying out atomic calculations within the same NLDA scheme as that used in the solid calculation. However, it would be simpler to employ the ready-to-use LDA pseudopotentials, under the assumption that exchange-correlation effects on the pseudopotential are scheme independent. We carried out our calculations using both pseudopotentials, generated within the LDA and the NLDA schemes. The results, discussed below, turn out to be very similar.

In Table I we show the ground state properties obtained for the materials examined: it is evident that all relevant quantities change very little with respect to the LDA. The equilibrium lattice constants increase slightly, while the bulk modulus decreases for Si, C and SiC and increases for GaAs. The small changes of the ground state properties obtained for the materials studied are somehow comforting, in view of the fact that gradient corrections sometimes overcorrect LDA results  \( [19,20] \) . In a recent paper by Fuchs at al.  \( [5] \) , a new set of GGA results for different solid compounds are reported, and the role of core-valence exchange-correlation is investigated. These data show that when LDA-generated pseudopo-
 

tentials are used with GGA XC functionals and nonlinear core corrections are ignored, the aforementioned overcorrection of GGA results with respect to LDA does not occur (see Tables V and VI of Ref. [5] for diamond and silicon, respectively). The overcorrections appear instead if the pseudopotentials are consistently generated within the GGA scheme. In conclusion, when we generate consistently the pseudopotentials in the new NLDA scheme, the NLDA ground state properties remain very close to the LDA results, while overcorrections of the lattice constants occur in the case of consistent GGA calculations.

For all the materials considered the NLDA electronic structures (calculated at the same lattice parameter using NLDA pseudopotentials) show slight differences with respect to the LDA band structure with a general very small increase of the gaps. The values of the main gaps with both the LDA and NLDA schemes are shown in Tab.II

The fourth column of tab. III shows the NLDA correction to the ground state total energy (per atom) of the solid, which is always decreased with respect to the LDA, both using LDA or NLDA pseudopotentials. For Silicon this energy lowering agrees with QMC results obtained by Fahy et al. in ref. [22], while for diamond QMC yields a total energy slightly less negative than the LDA one, at variance with our results [22]. But in view of the uncertainty still present in the total energy obtained from different QMC calculations (mostly due to the usage of a pseudopotential generated within the DFT-LDA and to the variational character of the wavefunctions, see for example the results shown in refs [22], [23], [24]), we believe that the discrepancies of the order of a few tenths of an eV per atom are acceptable.

For the silicon case we also calculated the NLDA total energy using Hubbard's model of  \( K_{xc}^{heg}(\vec{r}-\vec{r}^{\prime},n) \) . It is clear from eq. (4) that, in this case, the XC NLDA functional is positively definite, since the Hubbard's  \( K_{xc}^{heg} \)  is always negative. In fact we found an increase of the total energy per atom of about 1.5 eV. On the other hand it is reasonable that, if the total energy increases, the gap between the filled and the empty states closes. This is indeed our result: the direct gap using Hubbard's  \( K_{xc} \)  is 0.6 eV smaller than the LDA value. These very different results show that it is very important to use a good description of  \( K_{xc} \) .
 

## B. Atoms

In order to obtain the cohesive energy of solids one also has to calculate the atomic energies using the same XC functional. This is a stringent test, since the condition of weak inhomogeneity is hardly fulfilled in atoms. We start carrying out all-electron calculations for a number of atoms. In Tab. IV we compare the results obtained for the ground state energy of some neutral atoms in the LDA and NLDA schemes with the "experimental" values based on the compilation of Veillard and Clementi ([25] as reported in ref. [26]), and with recent GGA results [27]. The NLDA correction increases with the size of the atoms, but, at variance with the GGA method, it is generally not enough to correct the LDA underestimation of the binding energy.

The reason of this failure is evident in Fig. 3, where the NLDA  \( V_{xc} \)  potential of the Neon atom is shown together with the LDA and GGA ones. The differences are clear: there is a region, at intermediate distances from the nucleus, where the NLDA XC potential becomes more negative than the LDA potential, but at large distance it remains substantially equal, with no correction to the wrong (exponential) decay of the LDA  \( V_{xc}(r) \) . The GGA has this shortcoming too, but compensates for it in the region near the nucleus, where  \( V_{xc}^{GGA} \)  is more attractive than our and the LDA  \( V_{xc} \) . Whether or not  \( V_{xc}^{GGA} \)  is closer to the true exchange-correlation potential than ours in this region is not clear at present. It is possible that the good agreement between GGA and "exact" total energies of atoms is a consequence of the cancelation of two errors, namely the lack of the Coulombic tail at long range, and a possible overactractive behavior at small distances, the reciprocal cancellation of these two errors being optimized by the suitable choice of parameters made within the GGAs.

In order to compute the cohesive energies, both atoms and solids must be treated on the same footing, i.e. using the same pseudopotential. Hence, we generated the pseudopotent-
 

tials including the NLDA exchange correlation energy and applied the NLDA functional to pseudoatoms, in order to have a consistent approach in the atomic and solid calculations. In Fig.4 we report the Silicon pseudopotentials, within the LDA and the NLDA scheme: the curves obtained in the two schemes look quite similar, the main differences being confined to the core region r < 1 a.u. In this region, which is not really important for the computation of matrix elements, being weighted by the  \( r^{2}dr \)  volume element, the NLDA pseudopotential are slightly less attractive than the LDA one. Less evident, but more important are the differences for r > 1 a.u., where the NLDA curves are slightly deeper than the LDA ones.

The ground state total energies obtained in the LDA and NLDA schemes for the pseudoatoms considered here are compared in Tab.III. In our NLDA calculations the atoms are always treated as spin unpolarized systems, assuming that any contribution of spin polarization is well described at the local spin density (LSD) level. (This conjecture is substantiated by Fuchs et al.'s calculations  \( [5] \) , where spin-polarization energies calculated within GGA and LSD differ by about 0.1 eV.) Little improvement with respect to LDA is obtained for the total energies, so that the calculated cohesive energies, quoted in Table I, do not improve substantially.

## C. Surfaces

Although the inclusion of the NLDA functional introduced here do not show strong differences with respect to the LDA for the two limit cases, bulk and atomic systems, for the sake of completeness we also report briefly the results obtained for a surface.

We calculated the ground state energy and the equilibrium structure of the 2x1 reconstruction of Si(100) using both the standard LDA and the NLDA functional. Using NLDA a decrease of the total energy of 0.12 eV/atom, which is of the same order as the one obtained in bulk silicon, is obtained. The equilibrium geometry does not show any appreciable difference with respect to that obtained using the LDA exchange and correlation potential.
 

## IV. CONCLUSIONS

An old non-LDA exchange-correlation functional, originally derived by Kohn and Sham for weakly inhomogeneous systems, has been implemented for usage in electronic structure calculations. A new derivation, and a well defined treatment of higher-order fluctuations, have been devised, suggesting that this functional should be reliable for systems with slow, rather than weak, density variations (i.e. with density variations smooth on the scale of the inverse Fermi wave vector). NLDA results for the lattice constant of Si, diamond, cubic SiC and GaAs are slightly better than the LDA ones when compared with experiment. The overcorrection characteristic of the Generalized Gradient Approximations is avoided. Negligible changes with respect to LDA have been found also for a surface, Si(100)2x1.

On the other hand, the application of the XC functional to atoms (pseudoatoms) improves the total energies only partially (slightly) with respect to the LDA values. Hence, no substantial improvement comes out for the cohesive energy of solids. The reason for this failure is probably due to the fact that the Coulombic long-range tail of  \( V_{xc} \) , which is important in the case of atoms, is still lacking.

In general, we obtain changes with respect to LDA which are smaller than those needed to match the experimental values. This is a consequence of the conservative ansatz made about the density argument in eqs. (3) and (4), meant to avoid long-range components of  \( K_{xc} \)  and possible divergences of the XC energy. Even though this goal has been obtained, the NLDA part of the XC potential is generally underestimated. This leads to important discrepancies with experiments in the case of atoms, whose binding energies are not fully corrected with respect to the LDA. However, in some cases, e.g. for bulk semiconductors, the present description is closer to reality than other approaches.
 

## V. ACKNOWLEDGEMENTS

We acknowledge useful discussions with R. Resta and G. Senatore in the early stage of this work. Computer resources on an Origin 2000 system were granted by INFM and CINECA (Interuniversity Consortium of the Northeastern Italy for Automatic Computing) under the account cmpmpi0. We are grateful to S. Goedecker for providing us an efficient code for Fast Fourier Transforms  \( [28,29] \) . This work was supported in part by the European Community programme “Human Capital and Mobility” (Contract No. ERB CHRX CT930337).
 

## REFERENCES

[1] W. Kohn and L. J. Sham, Phys. Rev. 140, A 1133 (1965)

[2] P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964)

[3] D.M. Ceperley and B.J. Alder, Phys. Rev. Lett. 45, 566 (1980); J.P. Perdew, A. Zunger, Phys. Rev. B 23, 5048 (1981)

[4] J.P. Perdew, Phys. Rev. Lett. 55, 1665 (1985); A. D. Becke, Phys. Rev. A 38, 3098 (1988); D.C. Langreth, M.J. Mehl, Phys. Rev. Lett. 47, 446 (1981), J.P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1997).

[5] M. Fuchs, M. Bockstedte, E. Pehlke, and M. Scheffler, Phys. Rev. B 57, 2134 (1998) and references therein

[6] O. Gunnarson, M. Johnson and B. I. Lundqvist, Phys. Rev. B 20, 3136 (1979)

[7] L. J. Sham, Phys. Rev. B 7, 4357 (1973)

[8] J. Hubbard, Proc. R. Soc. London Ser. A 243, 336 (1958)

[9] S. Ichimaru and K. Utsumi, Phys. Rev. B 24, 7385 (1981)

[10] S. Moroni, D. M. Ceperley, and G. Senatore, Phys. Rev. Lett. 75, 689 (1995)

[11] M. Corradini, R. Del Sole, G. Onida, M. Palummo, Phys. Rev. B 57, 14569 (1998).

[12] N. Trouiller, J.L. Martins, Phys. Rev. B 43, 1993 (1991)

[13] D. R. Hamann, Phys. Rev. B 40, 2980 (1989)

[14] M. Fuchs, M. Scheffler, Comput. Phys. Commun., to be published

[15] L. Kleinman, D.M. Bylander, Phys. Rev. Lett. 48 1425 (1982)

[16] S. Louie, S. Froyen, M. L. Cohen, Phys. Rev. B 26 1738 (1982)

[17] H. J. Monkurst, J. D. Pack, Phys. Rev. B 13 5188 (1976)
 

[18] R. W. Godby, M. Schlüter and L. J. Sham, Phys. Rev. B 37, 10159 (1988)

[19] A. Garcia, C. Elsasser, J. Zhu, and S. G. Louie, Phys. Rev. B 46, 9829 (1992), and references therein

[20] A. Dal Corso, S. Baroni, and R. Resta, Phys. Rev. B 49, 5323 (1984)

[21] S.G.Louie, S. Froyen, M.L.Cohen, Phys. Rev. B 26, 1738 (1982)

[22] S. Fahy, X. W. Wang, and S. G. Louie, Phys. Rev. B 42, 3503 (1990)

[23] X.P. Li, D. M. Ceperley, R. M. Martin Phys. Rev. B 10929 1991

[24] B. Kralik, P. Delaney, S. Louie Phys Rev. Lett 80, pag. 4253 (1998)

[25] A. Veillard, E. Clementi, J. Chem Phys. 49, 2415 (1968)

[26] M.T. Carroll, R.F.W. Bader, S.H. Vosko, J. Phys. B 20 3599 (1987)

[27] A. Dal Corso, A. Pasquarello, A. Baldareschi and R. Car, Phys. Rev. B 53, 1180 (1996)

[28] S. Goedecker, Comp. Phys. Commun. 76, 294 (1993).

[29] S. Goedecker, SIAM Journal on Scientific Computing 18, 1605 (1997).
 

## FIGURES

FIG. 1. XC kernels of the homogeneous electron gas,  \( K_{xc}(R) \) , according to the model of Ichimaru and Utsumi (full line) and to the parametrization of QMC data of ref. [11] (dashed line), as a function of  \( R = r * k_{F} \) .

FIG. 2. Convergence of NLDA correction as a function of  \( r_{c} \)  in bulk silicon, using the model of Ichimaru and Utsumi (full line) and the parametrization of QMC data of ref. [11] (dashed line).

FIG. 3. The XC LDA potential (full line) compared with the potential obtained including self-consistently the NLDA correction (dashed line) and with the GGA potential (dotted line) for the Ne atom.

FIG. 4. Unscreened pseudopotentials within the NLDA (dashed lines) and LDA (full lines) for Silicon.
 

## TABLES

TABLE I. Ground state properties of the bulk silicon, diamond and silicon carbide and Gallium Arsenide as obtained in LDA and NLDA calculations. The first column indicates the XC scheme used to generate the pseudopotentials, the second one the scheme employed for the XC energy of the solid.

<table><tr><td></td><td>potential</td><td>Exc</td><td>a0(au)</td><td>B0(Mbar)</td><td>Eb(eV)</td></tr><tr><td rowspan="4">Si</td><td>LDA</td><td>LDA</td><td>10.17</td><td>.98</td><td>5.31</td></tr><tr><td>LDA</td><td>NLDA</td><td>10.19</td><td>.97</td><td>5.33</td></tr><tr><td>NLDA</td><td>NLDA</td><td>10.19</td><td>.95</td><td>5.28</td></tr><tr><td>Exp.</td><td></td><td>10.26</td><td>.99</td><td>4.63</td></tr><tr><td rowspan="4">C</td><td>LDA</td><td>LDA</td><td>6.73</td><td>4.51</td><td>8.63</td></tr><tr><td>LDA</td><td>NLDA</td><td>6.74</td><td>4.44</td><td>8.49</td></tr><tr><td>NLDA</td><td>NLDA</td><td>6.75</td><td>3.93</td><td>8.46</td></tr><tr><td>Exp.</td><td></td><td>6.74</td><td>4.42</td><td>7.37</td></tr><tr><td rowspan="4">SiC</td><td>LDA</td><td>LDA</td><td>8.15</td><td>2.25</td><td>7.42</td></tr><tr><td>LDA</td><td>NLDA</td><td>8.15</td><td>2.14</td><td>7.47</td></tr><tr><td>NLDA</td><td>NLDA</td><td>8.16</td><td>2.00</td><td>7.35</td></tr><tr><td>Exp.</td><td></td><td>8.24</td><td>2.3</td><td>6.34</td></tr><tr><td rowspan="4">GaAs</td><td>LDA</td><td>LDA</td><td>10.55</td><td>0.77</td><td>4.00</td></tr><tr><td>LDA</td><td>NLDA</td><td>10.63</td><td>0.89</td><td>3.95</td></tr><tr><td>NLDA</td><td>NLDA</td><td>10.60</td><td>0.85</td><td>4.01</td></tr><tr><td>Exp.</td><td></td><td>10.68</td><td>0.75</td><td>3.26</td></tr></table>
 

TABLE II. Main direct gaps (eV) for the bulk silicon, diamond and Gallium Arsenide as obtained in LDA and NLDA calculations at fixed lattice parameter ( \( a_{0} = 10.16 \) , 6.74 and 10.6 respectively).

<table><tr><td></td><td></td><td>LDA</td><td>NLDA</td></tr><tr><td rowspan="3">Si</td><td>\( \Gamma \)</td><td>2.57</td><td>2.60</td></tr><tr><td>X</td><td>3.57</td><td>3.63</td></tr><tr><td>L</td><td>2.86</td><td>2.90</td></tr><tr><td rowspan="3">C</td><td>\( \Gamma \)</td><td>5.62</td><td>5.70</td></tr><tr><td>X</td><td>11.21</td><td>11.32</td></tr><tr><td>L</td><td>11.32</td><td>11.39</td></tr><tr><td rowspan="3">GaAs</td><td>\( \Gamma \)</td><td>.39</td><td>.38</td></tr><tr><td>X</td><td>3.99</td><td>4.01</td></tr><tr><td>L</td><td>2.05</td><td>2.06</td></tr></table>
 

TABLE III. List of total energy and cohesive energy changes with respect to the LDA results, due to the use of NLDA scheme for the considered materials. (the LDA spin correction for total energy of pseudoatoms is included). The first column indicates the XC scheme used to generate the pseudopotential, the second one the scheme employed for the XC energy of the pseudo atom.

<table><tr><td></td><td>potential</td><td>Exc</td><td>\( \delta E_{at} \)</td><td>\( \deltaE_{sol} \)</td><td>\(  \delta E_{coh}  \)</td></tr><tr><td>Si</td><td>LDA</td><td>NLDA</td><td>-0.09</td><td>-0.11</td><td>+ 0.02</td></tr><tr><td></td><td>NLDA</td><td>NLDA</td><td>-0.31</td><td>-0.28</td><td>-0.03</td></tr><tr><td>C</td><td>LDA</td><td>NLDA</td><td>-0.57</td><td>-0.43</td><td>-0.14</td></tr><tr><td></td><td>NLDA</td><td>NLDA</td><td>-0.70</td><td>-0.54</td><td>-0.16</td></tr><tr><td>SiC</td><td>LDA</td><td>NLDA</td><td></td><td>-0.38</td><td>+0.05</td></tr><tr><td></td><td>NLDA</td><td>NLDA</td><td></td><td>-0.57</td><td>-0.07</td></tr><tr><td>GaAs</td><td>LDA</td><td>NLDA</td><td>-0.35 (As); -3.51 (Ga)</td><td>-1.88</td><td>-0.05</td></tr><tr><td></td><td>NLDA</td><td>NLDA</td><td>-0.36 (As); -1.72 (Ga)</td><td>-1.03</td><td>+0.01</td></tr><tr><td></td><td>-0.005</td><td></td><td></td><td></td><td></td></tr></table>
 

TABLE IV. Ground state total energy (Hartree) of some atoms from He to Argon, obtained in the LDA and NLDA schemes, and compared with the experimental values. Each calculated total energy includes the spin polarization corrections obtained in the LDA scheme.

<table><tr><td colspan="5">g.s. energy (a.u.)</td></tr><tr><td></td><td>LDA</td><td>NLDA</td><td>GGA</td><td>EXP</td></tr><tr><td>\( ^{4}Be \)</td><td>-14.44</td><td>-14.51</td><td>-14.64</td><td>-14.67</td></tr><tr><td>\( ^{6}C \)</td><td>-37.46</td><td>-37.62</td><td>-37.78</td><td>-37.84</td></tr><tr><td>\( ^{8}O \)</td><td>-74.50</td><td>-74.81</td><td>-74.99</td><td>-75.07</td></tr><tr><td>\( ^{10}Ne \)</td><td>-128.18</td><td>128.77</td><td>-128.94</td><td>-128.96</td></tr><tr><td>\( ^{11}Na \)</td><td>-161.38</td><td>-162.11</td><td>-162.25</td><td>-162.26</td></tr><tr><td>\( ^{14}Si \)</td><td>-288.09</td><td>-289.23</td><td>-289.33</td><td>-289.34</td></tr><tr><td>\( ^{18}Ar \)</td><td>-525.65</td><td>-527.59</td><td>-527.54</td><td>-527.56</td></tr></table>
 
![](./images/867759613011820690_1.jpg)

 
![](./images/867759613011820690_2.jpg)

 
![](./images/867759613011820690_3.jpg)

 
![](./images/867759613011820690_4.jpg)

 
