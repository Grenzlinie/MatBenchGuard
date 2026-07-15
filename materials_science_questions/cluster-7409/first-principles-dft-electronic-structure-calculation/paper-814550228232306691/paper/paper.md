# Investigating Orientational Defects in Energetic Material RDX Using First-Principles Calculations

Anirban Pal, $^\dagger$ Vincent Meunier, $^\ddagger$ and Catalin R. Picu*,†

$^\dagger$Department of Mechanical, Aerospace and Nuclear Engineering and $^\ddagger$Department of Physics, Applied Physics, and Astronomy, Rensselaer Polytechnic Institute, Troy, New York 12180, United States

Supporting Information

**ABSTRACT:** Orientational defects are molecular-scale point defects consisting of misaligned sterically trapped molecules. Such defects have been predicted in $\alpha$-RDX using empirical force fields. These calculations indicate that their concentration should be higher than that of vacancies. In this study we confirm the stability of a family of four orientational defects in $\alpha$-RDX using first-principles calculations and evaluate their formation energies and annealing barrier heights. The charge density distribution in the defective molecules is evaluated and it is shown that all four orientational defects exhibit some level of charge reduction at the midpoint of the N$-$N bond, which has been previously related to the sensitivity to initiation of the material. We also evaluate the vibrational spectrum of the crystal containing orientational defects and observe band splitting relative to the perfect crystal case. This may assist the experimental identification of such defects by Raman spectroscopy.

![](./images/814550228232306691_1.jpg)

## 1. INTRODUCTION

Energetic materials find widespread applications in military and civilian domains, such as in mining and infrastructure development. Explosives, propellants, and fuels all belong to this class of materials, making it a multibillion-dollar industry. Owing to their long history of interest, some of these materials have been widely studied with a specific focus on developing an understanding of their initiation and detonation processes. $^{1,2}$

Molecular crystals such as HMX (cyclotetramethylene tetranitramine), RDX (cyclotrimethylene trinitramine), and PETN (pentaerythritol tetranitrate) are among the most widely used energetic materials. Although the exact mechanism of detonation in these crystals is not fully understood, the formation of "hot-spots" as an intermediary step in low impact initiation is a well-accepted perspective $^{3-5}$ and has been recently observed. $^{6}$ Hot spots are regions of localized energy, which, if sufficiently large and long-lasting, $^{7,8}$ can serve as nucleation points for ignition and subsequent combustion. Some insight on the molecular mechanisms involved in hot spot formation was provided by Coffey and Sharma, $^{9}$ where atomic force microscopy (AFM) images of an RDX crystal surface, following a hammer impact test, showed molecules that were displaced and reoriented in all directions. It is important to note that it is easier to form hot spots in real (imperfect/impure) crystals and materials, where any heterogeneity or crystal defect can serve as an energy localizing site. $^{10,11}$ In direct initiation mechanisms, defects can provide favorable sites for electronically excited states via local band gap reduction, which can then lead to molecular dissociation. $^{12-14}$

Similar to covalent and ionic monatomic crystals, molecular crystals exhibit a variety of defects, such as dislocations, stacking faults, grain boundaries, twins, vacancies, and impurities. $^{15}$ When constituent molecules lack a center of symmetry, molecular crystals can also exhibit orientational disorder, $^{16}$ thereby allowing for the possibility of orientational point defects, caused by molecules reorienting and misaligning themselves in an otherwise perfect lattice. These defects may be formed during crystal growth or thermodynamically at higher temperatures. $^{15}$ Orientational defects have been investigated previously in nitromethane, $^{17}$ and in FOX-7 and TATB$^{18}$ in the context of mimicking the local environment near dislocation cores, stacking faults and grain boundaries.

Orientational defects in $\alpha$-RDX have been studied using the Smith-Bharadwaj (SB) potential in a previous study, $^{19}$ where the authors indicate the existence of four possible stable defects. The annealing barriers of these defects were found to be low suggesting low concentrations in bulk. However, the defect energies were found to be lower than the vacancy formation energy, suggesting that the presence of such defects might be more likely than that of vacancies.

Although the experimental confirmation of the presence of such defects is difficult, one can develop a more precise understanding of their fundamental properties using accurate calculations. In this work, we use ab initio methods to evaluate the energy and stability of the defects reported previously. The methods used are described in section 2. In section 3, we employ first-principles density functional theory to verify the existence of such defects and evaluate their formation energies

Received: January 18, 2016
Revised: March 3, 2016

and annealing barriers. This is followed by a study of the electronic structures to estimate their effect on impact sensitivity in the context of direct initiation mechanisms. The vibrational spectra for all four defects are also computed in an attempt to determine whether Raman spectroscopy can be used to detect the defect states. Section 4 discusses the possible implications and roles that the defects might have in real crystals, in the context of mechanical deformation and reaction initiation.

## 2. METHOD
For many years, traditional density functional theory (DFT) has been deemed inadequate when dealing with molecular crystals, particularly because of its inability to accurately account for long-range electron dispersion forces (e.g., van der Waals interactions).$^{20}$ In RDX these interactions are the primary intermolecular cohesive forces, and hence previous studies have failed to report accurate crystal volumes and bulk moduli.$^{21}$ However, owing to the significant recent developments in DFT-based methods to accurately describe London dispersion,$^{22,23}$ it is now possible to provide a quantitative description of volumetric and elastic properties of $\alpha$-RDX.$^{21}$

All calculations were performed using plane wave DFT with projector augmented-wave (PAW) pseudopotentials$^{24,25}$ and the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional,$^{26}$ implemented within the generalized gradient approximation (GGA) in VASP.$^{27-29}$ For accurately describing the van der Waals interactions, the DFT-D2 method of Grimme was employed.$^{30,31}$

The $\alpha$-RDX unit cell containing 168 atoms and exhibiting Pbca space group symmetry was used as the simulation cell (Figure 1). Crystallographic data were obtained from experimental results,$^{32}$ and the lattice constants and ions were allowed to relax to their ground-state energy. To minimize computation costs associated with structural relaxation, a single $k$-point ($\gamma$ only) was used. This is reasonable as the unit cell is large and bands are narrow (low dispersion in reciprocal space).

![](./images/814550228232306691_2.jpg)

Figure 1. Unit cell of $\alpha$-RDX has Pbca space group symmetry and eight molecules. Key: carbon, black; nitrogen, blue; oxygen, red; hydrogen, gray.

The relaxed lattice constants were found to be within 1% of lattice constants (Table 1) extrapolated to zero Kelvin from finite temperature data measured using neutron diffraction.$^{32}$ The extrapolation was performed using experimental thermal expansion coefficients (eq 1, units of $^\circ\text{C}^{-1}$) in the principal directions.$^{33}$ The expressions in eq 1 ($T$ in $^\circ\text{C}$) are best fits to data pertaining to the range of temperatures ($-$160 to +140 $^\circ\text{C}$).

<table>
<caption>Table 1. Experimental 300 K Lattice Constants$^{32}$ and Thermal Expansion Coefficients$^{33}$ Used To Compute an Estimate of the 0 K Lattice Constants Which Are Then Compared to Those Obtained from DFT Calculations$^a$</caption>
<thead>
<tr>
<th>lattice constants (Å)</th>
<th>measured (300 K)</th>
<th>$\int_{0}^{3000} \alpha(T - 273) dT$ (using (1))</th>
<th>extrapolated to 0 K</th>
<th>computed (DFT)</th>
<th>% diff</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ [100]</td>
<td>13.182</td>
<td>1.00427</td>
<td>13.126</td>
<td>13.202</td>
<td>+0.58</td>
</tr>
<tr>
<td>$b$ [010]</td>
<td>11.574</td>
<td>1.01648</td>
<td>11.386</td>
<td>11.351</td>
<td>$-$0.31</td>
</tr>
<tr>
<td>$c$ [001]</td>
<td>10.709</td>
<td>1.01203</td>
<td>10.582</td>
<td>10.680</td>
<td>+0.93</td>
</tr>
</tbody>
</table>

$^a$The computed lattice constants are within 1% of the 0 K extrapolated values.

$$
\begin{aligned}
\alpha_{a}(T) &= 2.439 \times 10^{-5} + 8.42 \times 10^{-8}T - 2.58 \times 10^{-10}T^{2} \\
& \quad - 5.59 \times 10^{-15}T^{4} \\
\alpha_{b}(T) &= 8.531 \times 10^{-5} + 6.73 \times 10^{-8}T - 1.29 \times 10^{-12}T^{3} \\
& \quad - 4.79 \times 10^{-15}T^{4} + 1.01 \times 10^{-16}T^{5} \\
\alpha_{c}(T) &= 7.391 \times 10^{-5} + 2.073 \times 10^{-7}T \\
& \quad + 3.17 \times 10^{-10}T^{2} + 7.9 \times 10^{-15}T^{4} \\
& \quad + 1.02 \times 10^{-16}T^{5}
\end{aligned} \tag{1}
$$

The defects have been chosen to be identical to those determined previously using empirical potentials.$^{19}$ The entire structure was then relaxed to an energy tolerance of $10^{-4}$ eV and a force tolerance of $10^{-3}$ eV/Å. This procedure was repeated for all four defects previously identified.$^{19}$ The corresponding relaxed defect structures are shown in Figure 2. The detailed structures (including atomic positions) of the defects are provided in the Supporting Information. Although the DFT relaxed defects are qualitatively similar to those

![](./images/814550228232306691_3.jpg)

Figure 2. Structure of defects A–D in the [001] projection, after relaxation using first principles. Detailed structures of the defects are provided in the Supporting Information.

predicted by MD previously,¹⁹ some differences are observed. To highlight the difference, the structures of one of the defects predicted with DFT and with the SB potential are superimposed in the [001] projection in Figure 3, where the rigid

![](./images/814550228232306691_4.jpg)

Figure 3. Two configurations of defect C predicted using dispersion-corrected DFT (color and thicker wireframe) and using the SB potential [13] (black and white and thinner wireframe) in the [001] projection. The two predictions are qualitatively similar. Differences in bond lengths are provided (Supporting Information).

body translation between them has been removed. Vibrational properties were computed using the PHONOPY module.³⁴ The electronic density of states and band gap were calculated using the B3LYP hybrid functional at the $\gamma$ point,³⁵,³⁶ and charge distribution plots were obtained using VESTA.³⁷

## 3. RESULTS
### 3.1. Formation Energy and Barriers.
We computed transition paths and energy barriers using the nudged elastic band (NEB) method.³⁸,³⁹ To this end, we supplied an initial path from which the chain-of-states is relaxed. Choosing an initial path can be challenging, except in simple cases such as diffusion in monatomic crystals, where a linear interpolation between the initial and final NEB states suffices. For the type of defects presented here, a linear interpolation would cause some of the interpolated images to have highly deformed geometries and may produce overlaps, thereby serving as poor initial paths. Because the NEB method can only find a relaxed reaction path close to the initial one, making a good choice of an initial path is therefore crucial.

To determine the initial transition paths, atomistic models using the Smith−Bharadwaj (SB) potential⁴⁰ and representing the structures of interest were developed. The defect molecules were placed in the rotated state and were allowed to return to the perfect crystal state in molecular dynamics (MD) simulations. The MD paths were sampled to produce replicas for the NEB simulations. To find the saddle point accurately, the climbing image method was used. The models and procedures used here are similar to those used in previous calculations.¹⁹ The transition paths are sampled with 16 intermediate replicas which were relaxed with DFT. The resulting energetic states of the replicas, and hence the energy profile of the transition path are shown in Figure 4. The starting and final states correspond to the defect and perfect crystal configurations, respectively. All defects displayed high formation barriers and low annealing barriers. The defect barriers and their energies are shown in Table 2.

![](./images/814550228232306691_5.jpg)

Figure 4. Transition path energies for defects A−D. The left ends of the plots correspond to the various defect states, whereas the right end corresponds to the perfect crystal. Defect C (green circles) has the lowest formation energy ($E_{\text{F}}$) of 1.11 eV (energy difference between replicas 0 and 17) and the highest annealing barrier ($E_{\text{A}}$) of 0.27 eV (height of path energy maximum, replica 6, from replica 0).

<table>
<caption>Table 2. Defect Annealing Barriers ($E_{\text{A}}$) and Formation Energies ($E_{\text{F}}$) Computed Using DFT and SB Potential¹⁹</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">DFT</th>
<th colspan="2">SB potential¹⁹</th>
</tr>
<tr>
<th>$E_{\text{A}}$ (eV)</th>
<th>$E_{\text{F}}$ (eV)</th>
<th>$E_{\text{A}}$ (eV)</th>
<th>$E_{\text{F}}$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>0.23</td>
<td>1.60</td>
<td>0.08</td>
<td>1.70</td>
</tr>
<tr>
<td>B</td>
<td>0.084</td>
<td>1.45</td>
<td>0.2</td>
<td>1.48</td>
</tr>
<tr>
<td>C</td>
<td>0.27</td>
<td>1.11</td>
<td>0.34</td>
<td>1.08</td>
</tr>
<tr>
<td>D</td>
<td>0.11</td>
<td>1.23</td>
<td>0.3</td>
<td>1.29</td>
</tr>
<tr>
<td>vacancy</td>
<td></td>
<td>1.71</td>
<td></td>
<td>1.72</td>
</tr>
</tbody>
</table>

*a*Defect C has the lowest $E_{\text{F}}$ and the highest $E_{\text{A}}$ among all the orientational defects.

In the previous study,¹⁹ the defect energies and annealing barriers were computed using the SB potential, which is an empirical potential with energy terms expressing the contributions from bonds, angles, dihedrals, impropers, van der Waals, and electrostatic interactions. This potential, originally parametrized using quantum chemistry calculations to reproduce conformational geometries and energies for HMX and DDMD (dimethyl(dinitromethyl)diamine), was found to reproduce structural, elastic, and thermal properties of crystalline $\alpha$-RDX reasonably well. The defect energetics obtained using this potential is reported in the "SB potential" column of Table 2. Defect C exhibited the lowest formation energy of 1.08 eV and the highest annealing barrier of 0.34 eV. Additionally, all defect energies were lower than the vacancy formation energy in the crystal (1.71 eV), which was computed using DFT and a similar model and methods.

The error associated with using a single $k$-point ($\gamma$ only) was estimated by computing the formation energies for all defects using a finer $5 \times 5 \times 5$ mesh and the same energy cutoff. They were found to be 1.62 eV (+1.25%), 1.47 eV (+1.38%), 1.10 eV (−0.9%), and 1.25 eV (+1.63%) for defects A−D, respectively. The small errors (shown in parentheses) indicate that single-$\gamma$ point calculations are reasonably accurate. Although the size effect is difficult to ascertain owing to the prohibitive expense of studying larger supercells, a model composed of $2 \times 2 \times 2$ unit cells and containing defect C was relaxed and the formation energy was calculated to be 1.21 eV. This is 0.1 eV above the value obtained with the $1 \times 1 \times 1$ unit cell model, which indicates a weak size effect.

![](./images/814550228232306691_6.jpg)

Figure 5. Configurations of the rotating and surrounding molecules along the transition path of defect C. The images are given in the [001] projection and the numbers correspond to the replica numbers indicated on the horizontal axis of Figure 4. State 0 corresponds to the relaxed defect structure, whereas state 15 is close to the perfect crystal structure.

Defect energies computed using first-principles display a very similar trend compared to those obtained using the SB potential. This agreement is somewhat surprising as one would not expect a classical empirical potential to agree with ab initio results especially for distorted molecules. However, one can interpret this agreement to conclude that the defects do not incorporate sufficient charge redistribution to deviate significantly from the results of the point-charge based empirical models. In fact, no local or global chemistry is modified during the process and weakly binding forces are known to be fairly well represented with parametrized potentials. However, the barriers display some difference, but defect C is again found to have the largest annealing barrier of 0.27 eV, and the lowest formation barrier (1.11 eV) in agreement with the MD predictions. Snapshots corresponding to the transition path of defect C are shown in Figure 5. The orientational defect energies are all below the vacancy formation energy of 1.71 eV, which agrees well with the SB result as well as previous calculations.⁴¹

3.2. Electronic Properties. Electronic excitations can provide a mechanism leading to bond dissociation, either via direct excitation to a dissociated state or via excitation to a bound state in which the activation energy for bond dissociation is lowered.⁴² In this context, the HOMO− LUMO gap or the band gap is of primary importance. The gap is very sensitive to the pressure and the presence of defects such as vacancies and dislocations.¹⁴ Laser experiments in α- RDX revealed that initiation could be caused by direct excitation at 2.35 eV and at modest pressures, indicating that such absorption could be associated with the presence of defects.¹³ In this section we evaluate the effect of the orientational defects on band structure.

The electronic density of states was computed near the Fermi level using Gaussian smearing with a width of 0.01 eV. The electronic band gap for the perfect crystal was found to be 5.25 eV, much higher the experimental value of 3.4 eV,⁴³ and close to previous computational results.⁴⁴,⁴⁵ The above discrepancy between computational and experimental values has been attributed to the presence of defects, particularly dislocations, which produce local energy levels in the gap.⁴⁴ The perfect crystal band gap was reduced to 4.90, 4.80, 5.01, and 4.86 eV when defects A, B, C, and D, respectively, are present (Figure 6).

![](./images/814550228232306691_7.jpg)

Figure 6. Electronic density of states for crystals with defects and the perfect crystal case. The gap reduces from 5.25 eV corresponding to the perfect crystal to 4.90, 4.80, 5.01, and 4.86 eV, respectively, for defects A−D, respectively, and is unaccompanied by the formation of states in the forbidden gap.

We now discuss how charge density is redistributed in the misoriented molecule. This is particularly important in the context of initiation as several studies have established correlations linking sensitivity to various descriptions of the electron charge distribution, such as electrostatic potentials,⁴⁶,⁴⁷ electro-negativities,⁴⁸,⁴⁹ partial charges,⁵⁰ and bond orders.⁵¹⁻⁵³ A comprehensive study comparing the performance of some of these measures in estimating energetic molecule sensitivity,⁵⁴ found that such measures were often not versatile enough to handle different classes of energetic molecules. However, they found that localized regions of electron deficiency over covalent bonds were characteristic of sensitive CHNO explosives.⁵⁴

It has been established that thermal decomposition in solid α-RDX begins with N−N bond scission.⁵⁵ Therefore, we examine in detail how electronic charge is distributed in the N− NO₂ region of the defects. Although in the isolated molecule all N−N bonds are identical, this is not the case for a molecule in the crystal due to the different environments of the three N−N bonds of the respective molecules (two NO₂ groups are axial

whereas one is equatorial in the perfect crystal). If charge deficiency over the N−N bond is considered to be an indicator of sensitivity, one needs to only focus on the most charge deficient N−N bond in the defects. In addition, because only one $NO_2$ group is lost per molecule during decomposition,56 the N−N bond with the least covalent character can be expected to constitute the initial fission center.

Figure 7 shows the charge distribution over 2-D slices of the most deficient $N-NO_2$ groups for the defective and perfect molecules. For the perfect case (labeled E), the charge density along an axial $N-NO_2$ group (most deficient) is shown, and one can see that the electron density at the midpoint of the N−N bond is nonzero. However, all four defects (A−D) show some charge deficiency at the midpoints of the $N-NO_2$ bonds, suggesting that these defects may be more sensitive to decomposition. More quantitatively, in the perfect crystal (E) the minimum density along the N−N bond is 0.327 e Bohr⁻³. For the defects A−D, the N−N electron density minimums are 0.309, 0.288, 0.318, and 0.301 e Bohr⁻³, respectively. The molecules surrounding the defects do not show significant deviations in their electron density minima relative to the perfect crystal case.

![](./images/814550228232306691_8.jpg)

Figure 7. Electron charge distribution across the most charge deficient $N-NO_2$ bonds in the perfect crystal (E) and defect (A−D) molecules. The color scales from 0 to 1.32 (Bohr⁻³) with contours at 0.45−1.20 in multiples of 0.15. All defects display density reduction at the midpoint of the N−N bond, with defect B having the largest deficiency.

### 3.3. Vibrational Properties.
To estimate how defects can affect thermal properties, the vibrational densities of states for unit cells considered above with and without defects were computed. The presence of defects did not yield significant differences in the vibrational density of states in comparison to the perfect crystal case, which indicates that the effect of such defects on thermal capacity and conductivity is expected to be low. However, because the defects perturb the crystal structure locally, one may expect changes in the phonon frequencies.

It is also interesting to inquire whether the defects described here can be observed by Raman spectroscopy. The perfect crystal structure presents many normal modes and, to simplify the discussion, we focus on a few frequencies that give intense Raman peaks in the perfect crystal (Table 3). The first four H−C−H stretching modes in Table 3 are indicated by arrows in

<table>
<caption>Table 3. A Few Raman Frequencies That Were Chosen for Comparison<sup>a</sup></caption>
<thead>
<tr>
<th colspan="3">from ref 57</th>
<th>current work</th>
</tr>
<tr>
<th>experiment (cm⁻¹)</th>
<th>calculated (cm⁻¹) (scaled)</th>
<th>mode assignment</th>
<th>calculated (cm⁻¹) (unscaled)</th>
</tr>
</thead>
<tbody>
<tr>
<td>3076</td>
<td>3071</td>
<td>H−C−H stretching (asymmetric)</td>
<td>3129</td>
</tr>
<tr>
<td>3067</td>
<td>3035</td>
<td>H−C−H stretching (asymmetric)</td>
<td>3125, 3113</td>
</tr>
<tr>
<td>3003</td>
<td>2984</td>
<td>H−C−H stretching (symmetric)</td>
<td>3050</td>
</tr>
<tr>
<td>2949</td>
<td>2944</td>
<td>H−C−H stretching (symmetric)</td>
<td>2979</td>
</tr>
<tr>
<td>885</td>
<td>875</td>
<td>ring breathing</td>
<td>926−932</td>
</tr>
</tbody>
</table>

<sup>a</sup>The experimental values and mode assignments are reproduced from a previous study.57

Figure 8. The first three columns are taken from ref 57 and are compared to the frequencies computed in the current work.

![](./images/814550228232306691_9.jpg)

Figure 8. Splitting of high frequency Raman active modes (H−C−H modes) in the presence of defects. The modes corresponding to the defective crystals are shown in color, whereas the position of the modes of the perfect crystal are shown in black and are indicated by arrows. Defect C, which has the lowest formation energy, exhibits the highest amount of band splitting.

The incorporation of defects in the unit cell lowers the overall symmetry of the system, thereby splitting the characteristic Raman frequencies. It is conjectured that the best Raman signature of the defects should be provided by the high frequency H−C−H stretching modes because it is observed that band splitting occurs over a small frequency range in the presence of defects. Figure 8 shows the band structure in the vicinity of six normal modes of the perfect crystal (indicated by arrows and black bands) in the frequency range 2925−3150 cm⁻¹. Defect C leads to the highest amount of splitting, with frequencies spreading to as low as 2932 cm⁻¹. The other defects also lead to significant spreading. Another mode of interest is the ring breathing mode whose characteristic frequency was determined experimentally to be 885 cm⁻¹ and reproduced in this work in the range 926−932 cm⁻¹. This mode disappears in all the defect unit cells, suggesting a lowering of this

characteristic Raman intensity when a high concentration of such defects is present. These results correspond to a concentration of defects of 12.5%, as considered in the models used in this study. This value is much higher than the expected concentration of such defects in real crystals and is imposed here by the rather small size of the simulation cell, which in turn is mandated by computational power limitations. The intensity of the respective Raman lines scales with the defect concentration. This issue is discussed further in the next section.

## 4. DISCUSSION
Orientational defects, previously studied using empirical potentials, were investigated using first-principles density functional theory in $\alpha$-RDX. The formation energy values obtained were found to agree well with previous results indicating that classical potentials may be adequate in treating such defects.

This is a consequence of the relatively strong intramolecular bonding in RDX, which resists significant charge redistribution even when the molecule is misaligned and distorted. Some charge redistribution is, however, observed, and the Bader partial charges for the defects have been provided in the Supporting Information. The annealing barriers correspond to a single transition path obtained using molecular dynamics, and therefore the possibility of alternate pathways and the estimation of free energy barriers remains open. The relatively high formation energies suggest low concentrations of such defects in the bulk, implying that these defects may not play an important role in homogeneous perfect crystals. Real crystals, however, are inhomogeneous and comprise a variety of point, line, and planar defects. It would be interesting to see if such defects are more likely to form near other crystal defects. It has been shown that these molecules can deform/rotate to accommodate high strains at dislocation cores and stacking faults. $^{19}$ However, it may be redundant to call such rotated molecules individual defects if they do not exist independently. It was hypothesized in the same paper that such defects could slow down or even stop dislocation motion if they happened to exist on an active glide plane. Further studies would be required to investigate if such defects are more or less likely to form near free surfaces, pores, inclusions, and shear bands.

The importance of such defects in the context of sensitivity is more interesting. Because N-N bond breaking is the first step in thermal decomposition of the $\alpha$-phase, a different molecular environment could lower the energy required to break the bond, thereby increasing sensitivity. Quantum-chemical calculations performed by Kuklja have shown that molecules near the surface require less energy than in the bulk to break the N- $NO_2$ bond. $^{58}$ We took an indirect approach to the sensitivity problem and plotted the charge distribution along the most electron-deficient N-N bond in the defects, and found defect B to be the most deficient with a density reduction of 0.04 Bohr$^{-3}$. The electronic band gaps were also lowered by up to 15% in the presence of defects, which could further enable dissociation via electronic excitations. These two pictures suggest that alternative or defective crystal environments can offer suitable sites for hot spot initiation via lower N-N bond dissociation energies. The influence of pressure on the band gap of such defects would be a topic for future investigation.

To characterize the vibrations of such defects, normal-mode frequencies of the defect structures were calculated and compared with those of the perfect case. All defects exhibited splitting of $CH_2$ frequencies due to lower symmetries, with defect C exhibiting the largest range. The ring breathing mode was found to disappear for all the defects. Such characterization may prove difficult at elevated temperatures because experimental Raman peaks corresponding to $CH_2$ vibrations may be insufficiently sharp to permit differentiation between a perfect crystal and one having orientational defects. It may also be difficult to differentiate these defects from other line and planar defects, based on Raman spectra alone. These difficulties are compounded by the fact that band intensities scale with the defect concentration. Therefore, a coupled experimental and simulation effort is required to determine the optimal defect identification method.

## 5. CONCLUSION
In this work, four orientational defects in $\alpha$-RDX have been studied using first-principles DFT calculations. These defects are stable and their formation energies have been calculated to be between 1.23 and 1.60 eV, which are lower than that of vacancies (1.71 eV). Their annealing barriers, estimated using NEB, were low (0.08−0.23 eV). The defects caused a reduction in the electronic band gap by 0.24−0.45 eV, and a reduction in the electronic density at the midpoint of N-N bonds. The structural distortions caused by these defects caused sufficient splitting of the highest frequency Raman active modes.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jpca.6b00574.

Detailed structures of the rotational defects and the computed Bader partial charges for each atom on the rotated molecule. Figure S1, reference perfect RDX molecule. Table S1, positions of perfect molecule. Tables S2−S5, displacements of all atoms of the rotated molecules. Table S6, bond lengths. (PDF)

## AUTHOR INFORMATION
### Corresponding Author
*Catalin R. Picu. E-mail: picuc@rpi.edu. Phone: +1 518 276 2195.

### Author Contributions
The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
All simulations were performed at the Centre for Computational Innovations (CCI) at Rensselaer Polytechnic Institute. A. Pal thanks Dr. Liangbo Liang and Dr. Neerav Kharche for providing technical advice for DFT calculations. The authors gratefully acknowledge the support from the Army Research Office through grant W911NF-09-1-0330.

## REFERENCES
(1) Politzer, P.; Murray, J. S. *Energetic Materials Part 1. Decomposition, Crystal and Molecular Properties*; Elsevier: Amsterdam, 2003.
(2) Politzer, P.; Murray, J. S. *Energetic Materials Part 2. Detonation, Combustion*; Elsevier: Amsterdam, 2003.

(3) Bowden, F. P.; Yoffe, A. D. *Initiation and Growth of Explosion in Liquids and Solids*; Cambridge University Press: New York, 1985.

(4) Urtiew, P. A.; Tarver, C. M. Shock Initiation of Energetic Materials at Different Initial Temperatures (Review). *Combust., Explos. Shock Waves* **2005**, 41, 766−776.

(5) Tarver, C. M.; Chidester, S. K. On the Violence of High Explosive Reactions. *J. Pressure Vessel Technol.* **2005**, 127, 39−48.

(6) You, S.; Chen, M.-W.; Dlott, D. D.; Suslick, K. S. Ultrasonic Hammer Produces Hot Spots in Solids. *Nat. Commun.* **2015**, 6, 6581.

(7) Field, J. E.; Bourne, N. K.; Palmer, S. J. P.; Walley, S. M.; Sharma, J.; Beard, B. C. Hot-Spot Ignition Mechanisms for Explosives and Propellants [and Discussion]. *Philos. Trans. R. Soc., A* **1992**, 339, 269−283.

(8) Botcher, T. R.; Ladouceur, H. D.; Russell, T. P. Pressure Dependent Laser Induced Decomposition of RDX. *AIP Conference Proceedings*; AIP Publishing: Melville, NY, 1998; Vol. 429, pp 989−992.

(9) Coffey, C. S.; Sharma, J. Lattice Softening and Failure in Severely Deformed Molecular Crystals. *J. Appl. Phys.* **2001**, 89, 4797−4802.

(10) Armstrong, R. W.; Ammon, H. L.; Elban, W. L.; Tsai, D. H. Investigation of Hot Spot Characteristics in Energetic Crystals. *Thermochim. Acta* **2002**, 384, 303−313.

(11) Holian, B. L.; Germann, T. C.; Maillet, J.-B.; White, C. T. Atomistic Mechanism for Hot Spot Initiation. *Phys. Rev. Lett.* **2002**, 89, 285501.

(12) Kuklja, M. M.; Stefanovich, E. V.; Kunz, A. B. An Excitonic Mechanism of Detonation Initiation in Explosives. *J. Chem. Phys.* **2000**, 112, 3417−3423.

(13) Barry Kunz, A.; Kuklja, M. M.; Botcher, T. R.; Russell, T. P. Initiation of Chemistry in Molecular Solids by Processes Involving Electronic Excited States. *Thermochim. Acta* **2002**, 384, 279−284.

(14) Kuklja, M. M.; Aduev, B. P.; Aluker, E. D.; Krasheninin, V. I.; Krechetov, A. G.; Mitrofanov, A. Y. Role of Electronic Excitations in Explosive Decomposition of Solids. *J. Appl. Phys.* **2001**, 89, 4156−4166.

(15) Wright, J. D. *Molecular Crystals*, 2nd ed.; Cambridge University Press: Cambridge, U.K., 1995.

(16) Craig, D. P.; Ogilvie, J. F.; Reynolds, P. A. Calculated Molecular Orientational Disorder in Anthracene Crystals. *J. Chem. Soc., Faraday Trans. 2* **1976**, 72, 1603−1612.

(17) Reed, E. J.; Joannopoulos, J. D.; Fried, L. E. Electronic Excitations in Shocked Nitromethane. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2000**, 62, 16500−16509.

(18) Kuklja, M.; Rashkeev, S. Modeling Defect-Induced Phenomena. In *Static Compression of Energetic Materials*; Peiris, S., Piermarini, G., Eds.; Shock Wave and High Pressure Phenomena; Springer: Berlin, Heidelberg, 2008; pp 291−326.

(19) Pal, A.; Picu, R. C. Rotational Defects in Cyclotrimethylene Trinitramine (RDX) Crystals. *J. Chem. Phys.* **2014**, 140, 044512.

(20) Byrd, E. F. C.; Scuseria, G. E.; Chabalowski, C. F. An Ab Initio Study of Solid Nitromethane, HMX, RDX, and CL20: Successes and Failures of DFT. *J. Phys. Chem. B* **2004**, 108, 13100−13106.

(21) Shimojo, F.; Wu, Z.; Nakano, A.; Kalia, R. K.; Vashishta, P. Density Functional Study of 1,3,5-Trinitro-1,3,5-Triazine Molecular Crystal with van Der Waals Interactions. *J. Chem. Phys.* **2010**, 132, 094106.

(22) Berland, K.; Cooper, V. R.; Lee, K.; Schröder, E.; Thonhauser, T.; Hyldgaard, P.; Lundqvist, B. I. Van Der Waals Forces in Density Functional Theory: A Review of the vdW-DF Method. *Rep. Prog. Phys.* **2015**, 78, 066501.

(23) Klimeš, J.; Michaelides, A. Perspective: Advances and Challenges in Treating van Der Waals Dispersion Forces in Density Functional Theory. *J. Chem. Phys.* **2012**, 137, 120901.

(24) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1994**, 50, 17953−17979.

(25) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1999**, 59, 1758−1775.

(26) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, 77, 3865−3868.

(27) Kresse, G.; Hafner, J. Ab Initio Molecular-Dynamics Simulation of the Liquid-Metal-Amorphous-Semiconductor Transition in Germa- nium. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1994**, 49, 14251−14269.

(28) Kresse, G.; Furthmüller, J. Efficiency of Ab-Initio Total Energy Calculations for Metals and Semiconductors Using a Plane-Wave Basis Set. *Comput. Mater. Sci.* **1996**, 6, 15−50.

(29) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1996**, 54, 11169−11186.

(30) Grimme, S. Accurate Description of van Der Waals Complexes by Density Functional Theory Including Empirical Corrections. *J. Comput. Chem.* **2004**, 25, 1463−1473.

(31) Grimme, S. Semiempirical GGA-Type Density Functional Constructed with a Long-Range Dispersion Correction. *J. Comput. Chem.* **2006**, 27, 1787−1799.

(32) Choi, C. S.; Prince, E. The Crystal Structure of Cyclo- trimethylenetrinitramine. *Acta Crystallogr., Sect. B: Struct. Crystallogr. Cryst. Chem.* **1972**, 28, 2857−2862.

(33) Cady, H. H. Coefficient of Thermal Expansion of Pentaery- thritol Tetranitrate and Hexahydro-1,3,5-Trinitro-S-Triazine (RDX). *J. Chem. Eng. Data* **1972**, 17, 369−371.

(34) Togo, A.; Oba, F.; Tanaka, I. First-Principles Calculations of the Ferroelastic Transition between Rutile-Type and $CaCl_2$-Type $SiO_2$ at High Pressures. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2008**, 78, 134106.

(35) Becke, A. D. Density-functional Thermochemistry. III. The Role of Exact Exchange. *J. Chem. Phys.* **1993**, 98, 5648−5652.

(36) Lee, C.; Yang, W.; Parr, R. G. Development of the Colle-Salvetti Correlation-Energy Formula into a Functional of the Electron Density. *Phys. Rev. B: Condens. Matter Mater. Phys. Phys.* **1988**, 37, 785−789.

(37) Momma, K.; Izumi, F. VESTA 3 for Three-Dimensional Visualization of Crystal, Volumetric and Morphology Data. *J. Appl. Crystallogr.* **2011**, 44, 1272−1276.

(38) Henkelman, G.; Jónsson, H. Improved Tangent Estimate in the Nudged Elastic Band Method for Finding Minimum Energy Paths and Saddle Points. *J. Chem. Phys.* **2000**, 113, 9978−9985.

(39) Henkelman, G.; Uberuaga, B. P.; Jónsson, H. A Climbing Image Nudged Elastic Band Method for Finding Saddle Points and Minimum Energy Paths. *J. Chem. Phys.* **2000**, 113, 9901−9904.

(40) Smith, G. D.; Bharadwaj, R. K. Quantum Chemistry Based Force Field for Simulations of HMX. *J. Phys. Chem. B* **1999**, 103, 3570−3575.

(41) Kuklja, M. M.; Kunz, A. B. Ab Initio Simulation of Defects in Energetic Materials. Part I. Molecular Vacancy Structure in RDX Crystal. *J. Phys. Chem. Solids* **2000**, 61, 35−44.

(42) Dlott, D. D. Fast Molecular Processes in Energetic Materials. In *Theoretical and Computational Chemistry*. In *Energetic Materials Part 2. Detonation, Combustion*; Politzer, P., Murray, S., Eds.; Elsevier: Amsterdam, 2003; Vol. 13, Chapter 6, pp 125−191.

(43) Marinkas, P. L. Luminescence of Solid Cyclic Polynitramines. *J. Lumin.* **1977**, 15, 57−67.

(44) Kuklja, M. M.; Kunz, A. B. Electronic Structure of Molecular Crystals Containing Edge Dislocations. *J. Appl. Phys.* **2001**, 89, 4962−4970.

(45) Perger, W. F. Calculation of Band Gaps in Molecular Crystals Using Hybrid Functional Theory. *Chem. Phys. Lett.* **2003**, 368, 319−323.

(46) Murray, J. S.; Lane, P.; Politzer, P. Relationships between Impact Sensitivities and Molecular Surface Electrostatic Potentials of Nitroaromatic and Nitroheterocyclic Molecules. *Mol. Phys.* **1995**, 85, 1−8.

(47) Murray, J. S.; Lane, P.; Politzer, P. Effects of Strongly Electron- Attracting Components on Molecular Surface Electrostatic Potentials: Application to Predicting Impact Sensitivities of Energetic Molecules. *Mol. Phys.* **1998**, 93, 187−194.

G
DOI: 10.1021/acs.jpca.6b00574
J. Phys. Chem. A XXXX, XXX, XXX−XXX

(48) Mullay, J. A Relationship between Impact Sensitivity and Molecular Electronegativity. *Propellants, Explos., Pyrotech.* **1987**, *12*, 60−63.

(49) Mullay, J. Relationships between Impact Sensitivity and Molecular Electronic Structure. *Propellants, Explos., Pyrotech.* **1987**, *12*, 121−124.

(50) Zhang, C.; Shu, Y.; Huang, Y.; Zhao, X.; Dong, H. Investigation of Correlation between Impact Sensitivities and Nitro Group Charges in Nitro Compounds. *J. Phys. Chem. B* **2005**, *109*, 8978−8982.

(51) Xiao, H.-M.; Fan, J.-F.; Gu, Z.-M.; Dong, H.-S. Theoretical Study on Pyrolysis and Sensitivity of Energetic Compounds: (3) Nitro Derivatives of Aminobenzenes. *Chem. Phys.* **1998**, *226*, 15−24.

(52) Fan, J.; Gu, Z.; Xiao, H.; Dong, H. Theoretical Study on Pyrolysis and Sensitivity of Energetic Compounds. Part 4. Nitro Derivatives of Phenols. *J. Phys. Org. Chem.* **1998**, *11*, 177−184.

(53) Jianfen, F.; Heming, X. Theoretical Study on Pyrolysis and Sensitivity of Energetic Compounds. (2) Nitro Derivatives of Benzene. *J. Mol. Struct.: THEOCHEM* **1996**, *365*, 225−229.

(54) Rice, B. M.; Hare, J. J. A Quantum Mechanical Investigation of the Relation between Impact Sensitivity and the Charge Distribution in Energetic Molecules. *J. Phys. Chem. A* **2002**, *106*, 1770−1783.

(55) Wight, C. A.; Botcher, T. R. Thermal Decomposition of Solid RDX Begins with Nitrogen-Nitrogen Bond Scission. *J. Am. Chem. Soc.* **1992**, *114*, 8303−8304.

(56) Botcher, T. R.; Wight, C. A. Explosive Thermal Decomposition Mechanism of RDX. *J. Phys. Chem.* **1994**, *98*, 5441−5444.

(57) Infante-Castillo, R.; Pacheco-Londoño, L. C.; Hernández- Rivera, S. P. Monitoring the $\alpha \rightarrow \beta$ Solid−solid Phase Transition of RDX with Raman Spectroscopy: A Theoretical and Experimental Study. *J. Mol. Struct.* **2010**, *970*, 51−58.

(58) Kuklja, M. M. Thermal Decomposition of Solid Cyclotri- methylene Trinitramine. *J. Phys. Chem. B* **2001**, *105*, 10159−10162.