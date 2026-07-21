# Evidence for cascade overlap and grain boundary enhanced amorphization in silicon carbide irradiated with Kr ions

X. Wang $^{a}$, L. Jamison $^{b}$, K. Sridharan $^{a,b,c}$, D. Morgan $^{a,b,c}$, P.M. Voyles $^{b,c}$, I. Szlufarska $^{a,b,c,*}$

$^{a}$ Department of Engineering Physics, University of Wisconsin, Madison, WI 53706, USA
$^{b}$ Materials Science Program, University of Wisconsin, Madison, WI 53706, USA
$^{c}$ Department of Materials Science and Engineering, University of Wisconsin, Madison, WI 53706, USA

---

## ARTICLE INFO
**Article history:**
Received 30 April 2015
Revised 28 July 2015
Accepted 28 July 2015
Available online 8 August 2015

**Keywords:**
Silicon carbide
High-resolution electron microscopy
Grain boundaries
Radiation
Interstitial starvation

---

## ABSTRACT
Evolution of amorphous domains in silicon carbide with 1 MeV $Kr^{2+}$ irradiation is investigated using high-resolution transmission electron microscopy and simulations. An unusual morphology of highly curved crystalline/amorphous boundaries is observed in the images, which is identified as a result of cascade overlap and reproduced by a coarse-grained model informed by atomistic simulations. Comparison of local amorphization fractions near grain boundaries and within grain interiors provides experimental evidence for the interstitial starvation mechanism in SiC for the first time. As a competing effect to defect sinks, interstitial starvation increases the rate of local amorphization near grain boundaries and reduces the radiation resistance of nanocrystalline silicon carbide.

© 2015 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

---

## 1. Introduction
Silicon carbide (SiC) has attracted considerable attention in the nuclear industry because of its outstanding properties, such as high-temperature stability, chemical inertness, high thermal conductivity and low neutron absorption cross-section [1]. In order to meet the reliability requirements during long-term service in a nuclear reactor, a material must be highly resistant to radiation damage. This is because radiation creates numerous point defects and defect clusters that accumulate and lead to the degradation of the material properties [2]. One of the responses of SiC to irradiation is radiation-induced amorphization (RIA) [3]. RIA reduces the hardness, elastic modulus and thermal conductivity of SiC and is accompanied by swelling of the material [4-6].

The mechanism for RIA in SiC has been extensively studied by both experimental and theoretical approaches [7-13]. Amorphization can proceed either homogeneously or heterogeneously [3]. In homogeneous amorphization, point defects accumulate progressively in the system until crystalline order is lost. This process is sometimes modeled as involving point defects raising the energy of the system until a critical energy density is reached, at which point the system transforms to a more stable amorphous state spontaneously [14]. For heterogeneous amorphization, several possible mechanisms have been proposed, including cascade overlap, direct impact/defect stimulated growth (DI/DS) at crystalline/amorphous (c/a) boundaries and a nucleation and growth model. The cascade overlap model assumes that irradiation produces regions of high defect concentration, i.e., displacement cascades, and the overlap of these cascades leads to localized amorphization. In contrast, in the DI/DS model, local disordered regions are formed directly by the incident particles and further growth at c/a interfaces is stimulated by the diffusion of generated defects. The amorphous phase may also nucleate and grow near extended defects, such as dislocations and grain boundaries. Experimentally, the amorphization fraction of SiC by ion irradiation has been measured as a function of irradiation dose [7-10]. The amorphization fraction - irradiation dose curve has a sigmoidal-like shape, which is consistent with all three mechanisms mentioned above. Molecular dynamics (MD) simulations have revealed that the completely amorphous state can be reached after generating a number of 10 keV Si or C atom recoils in a SiC crystal, which implies that an overlap of the displacement cascades may lead to the final c-a transition [12,15]. However, MD simulations also found the formation of nanoscale amorphous domains after a direct impact of 50 keV Au ions with SiC, suggesting that direct amorphization is also a possible mechanism for heavier irradiation ions [13].

Despite many studies dedicated to this topic, a complete understanding of the microscopic mechanism governing the c-a

---
* Corresponding author at: 1509 University Avenue, Madison, WI 53706, USA.
E-mail address: szlufarska@wisc.edu (I. Szlufarska).

http://dx.doi.org/10.1016/j.actamat.2015.07.070
1359-6454/© 2015 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

transition remains elusive, as the detailed amorphization process is likely to depend on the irradiation species, their energy, the sample temperature and the nano/microstructure of the SiC. Moreover, these effects are not necessarily independent of each other. Of particular interest is to understand how the specific amorphization mechanism is affected by the presence of grain boundaries (GBs). This interest is driven by recent efforts devoted to improving radiation tolerance by refining the grain size of SiC to the nanometer regime [16–21]. Nanocrystalline (nc) materials have a high volume fraction of GBs, which act as sinks for point defects generated during irradiation [22]. As a result one can expect nc materials to be more efficient at annealing radiation-induced damage. Indeed experiments found that nc SiC showed a higher dose to amorphization than single crystal SiC irradiated with high energy electron and Si ions [16,17]. Interestingly, however, reduction in radiation resistance of SiC due to grain refinement was also reported based on several irradiation experiments using 1 MeV Si, 2 MeV Au and 1 MeV Kr ions [18,20,21]. What is particularly puzzling is that the same low pressure chemical vapor deposited (LPCVD) nc SiC was used in Refs. [16] and [17] (showing improved resistance to amorphization) and in Ref. [21] (showing a decreased resistance). It appears that the answer to the question whether nc covalent ceramics have superior or inferior resistance depends not only on the nano/microstructural features (GBs, stacking faults, dislocation density, etc.), but also on the irradiation type. A summary of experimental results on the effects of radiation type and temperature on RIA in SiC can be found in Ref. [21]. The seemingly contradictory effects of grain refinement on resistance to amorphization reported in the literature also imply that GBs may play multiple roles in amorphization and general radiation damage process. Understanding the complex nature of RIA is important for utilizing nano-engineering to design materials with superior radiation resistance.

High-resolution transmission electron microscopy (HRTEM) provides insight into the role of GBs in RIA, since HRTEM can be used for direct observation of the evolution of nano/microstructural features during irradiation. For instance, Ishimaru et al. used in situ HRTEM to observe structural changes during electron irradiation of 3C-SiC with nanolayered planar defects [23]. It was shown that after receiving the same dose, GBs were highly damaged and disordered while the intragranular regions on both sides of the GB maintained crystalline order. This result suggested that irradiation-induced defects were preferentially trapped at GBs, driving amorphization in that region. For ion irradiation, Snead et al. analyzed the shape and orientation of the amorphized areas in single crystal 3C-SiC implanted with 0.56 MeV Si⁺ [24]. Amorphous islands (or amorphous pockets), typically 10 nm in width and more than 30 nm in length, were formed in the region beyond the damage peak where the sample was only partially amorphized. These pockets had an elongated shape with the major axis aligned parallel to the surface of the specimen, regardless of the direction of the incident ion. The authors hypothesized that the orientation preference was either due to the strain field introduced by the amorphization or the free surface of the sample. However, the effects of microstructure (e.g., GBs) during the ion irradiation were not investigated.

In the present study, we use HRTEM to investigate the morphology of amorphous regions in polycrystalline 3C-SiC irradiated with Kr ions and to determine the role that GBs play in RIA. An unusual morphology with a very fine structure of highly curved c/a boundaries is found in the partially amorphized sample. To understand how such morphology can arise, we have developed a coarse-grained model for damage evolution, which reproduces the experimental observations based on the combined effects of cascade overlap and the two-dimensional projection inherent to HRETM. By comparing the c/a morphologies at GBs and within the grain interiors, the complex effects of GBs on the amorphization process are investigated. Our analysis is enabled by development of a new algorithm for automatic identification of the amorphous regions in HRTEM images. Our analysis demonstrates the existence of the "interstitial starvation" in SiC, which proposes that preferential annihilation of interstitials at the GBs leaves behind excess vacancies that lead to amorphization. This mechanism was previously only postulated to occur in SiC based on simulations [25]. The influence of the dual role of GBs as sinks for point defects and as a source for interstitial starvation on the radiation resistant of nanocrystalline material is also discussed.

## 2. Experiment

To obtain partially amorphous SiC samples, in-situ $Kr^{2+}$ irradiation was conducted using the IVEM-Tandem facility at the Argonne National Laboratory. The TEM samples were prepared from polycrystalline CVD 3C-SiC sourced from Rohm & Hass with grain sizes ranging from 1 μm to 5 μm. The ion beam energy was 1 MeV and the flux was $6.25 \times 10^{11}$ ions/cm²s. The irradiation temperature was measured by a thermocouple within the heated specimen stage and the temperature was controlled at 100 °C, which is below the RIA critical temperature in SiC. During irradiation, electron diffraction patterns of the sample were recorded periodically and were used to determine the degree of crystallinity of the sample. The sample was regarded as fully amorphous when diffraction spots disappeared and only diffuse rings remained. The irradiation fluence for complete amorphization was $1.30 \times 10^{15}$ ions/cm², corresponding to a dose of 1.35 dpa (displacement per atom). Another sample was then irradiated to half of the dose to amorphization (0.675 dpa) and therefore was considered partially amorphous. SRIM ("Stopping and Range of Ions in Matter") code was used to calculate the number of displacements per incident Kr ion as a function of specimen depth, and the average displacement number within the sample thickness was used to convert the fluence to dose in dpa [26]. Detailed settings for SRIM calculation are described in Section 3.1. For additional thinning, the partially amorphous sample was ion milled on both sides with Fischione 1050 set at 600 V for 15 min after the irradiation. Detailed procedures for sample preparation and irradiation experiment can be found in Refs. [17] and [21].

Ex-situ HRTEM images were taken using FEI Tecnai F30 microscope operated at 300 kV using the twin pole piece and with objective aperture radius of 47.3 mrad. Fig. 1 shows typical HRTEM images of an unirradiated sample and a sample that received half of the dose to amorphization. The insets show the corresponding selected area diffraction patterns (SADP). For the unirradiated sample, the HRTEM image has clearly visible columns of atoms (or lattice fringes) in the entire area of the image and the SADP shows only sharp crystalline diffraction spots. In the image of the partially amorphous sample, amorphous domains of mottled contrast are mixed with crystalline domains with periodic lattice fringes and the SADP contains diffuse rings indicative of amorphous material in addition to crystalline spots.

In order to quantify the c/a fractions and boundaries, we have developed an automated analysis method that is free from observer bias to distinguish consistently the amorphous and crystalline regions in all HRTEM images. The procedure consists of three steps, which are illustrated in Figs. 2-4, respectively. In Step I, we Fourier filter the image, retain only the crystalline spots in the Fourier transform and then do the inverse Fourier transform (Fig. 2). The goal of this Fourier filtering step is to preserve the intensity of the crystalline part of the image while eliminating the intensity of the amorphous part. In Step II, we calculate the local standard deviation of the filtered intensity. The filtered image is divided into

![](./images/814604255141822464_1.jpg)

Fig. 1. HRTEM images of (a) unirradiated 3C-SiC sample (b) sample received half of the dose to amorphization. Insets at the right corner of each image represent selected area diffraction patterns (SADP) for the perspective sample.

![](./images/814604255141822464_2.jpg)

Fig. 2. Fourier filtering of the HRTEM images: (a) original image, (b) FFT, (c) crystalline spots preserved by using a mask, (d) inverse FFT.

![](./images/814604255141822464_3.jpg)

Fig. 3. (a) Part of the Fourier filtered image (Fig. 2d) showing the positions of an amorphous square (labeled B) and a crystalline square (labeled C). Intensity histogram of (b) the amorphous square B and (c) the crystalline square C.

small squares and the intensity standard deviation of each small square is calculated. The standard deviation value is then interpreted as an index for the crystallinity. For a square located in an amorphous region, the distribution of pixel intensity is unimodal (Fig. 3b) and the standard deviation is low. However, for a square in a crystalline area with lattice fringes, the intensity distribution is bimodal because lattice fringes consist of both bright and dark strips (Fig. 3c) and therefore the standard deviation is high. It is worth noting that the square must be large enough to cover at least one dark and one bright lattice fringe otherwise the brightness distribution of the crystalline square will not be bimodal. We used squares 11 pixels to 14 pixels (corresponding to 2.5–3.2 Å) on a side, depending on the magnification and the lattice spacing of the HRTEM images. In step III, we select a standard deviation threshold (SDₜₕ) that distinguishes crystalline and amorphous regions. This is achieved by fitting the histogram of standard deviation values to the sum of two Gaussian functions, one for the amorphous contribution and the other for the crystalline

contribution, using Nelder-Mead non-linear iterative fitting method. For all the HRTEM images in the following discussion, the $\chi^{2}$ test shows the histogram of standard deviation values satisfies the fitted distribution at a 2.5% significance level and the adjusted $R^{2}$ of the fit is above 99%. Fig. 4 shows an example standard deviation fit. The standard deviation threshold is defined as $\text{SD}_{\text{th}} = \text{SD}_{1} + \eta_{\text{th}} \times (\text{SD}_{2} - \text{SD}_{1})$, where $\text{SD}_{1}$ and $\text{SD}_{2}$ is the peak position of amorphous and crystalline Gaussians respectively. $\eta_{\text{th}}$ is an adjustable parameter between 0 and 1, so $\text{SD}_{1} < \text{SD}_{\text{th}} < \text{SD}_{2}$. Image squares with $\text{SD} > \text{SD}_{\text{th}}$ are labeled crystalline while squares with $\text{SD} < \text{SD}_{\text{th}}$ are labeled amorphous. We choose $\eta_{\text{th}} = 0.8$ as it gives the best match between the c/a morphology generated by the processing code and human judgment applied to the HRTEM images. The same $\eta_{\text{th}}$ value is used for processing of all images. Varying $\eta_{\text{th}}$ from 0.7 to 0.9 results in variation of the amorphization fraction of the images by about 9%, but it does not change the trend of degrees of amorphization between different images, or the general features of the c/a morphology on which our conclusions are based.

To validate the method, one original HRTEM image of the partially amorphous SiC sample is compared with its processed image showing the c/a morphology in Fig. 5. In the HRTEM image (Fig. 5a), the c/a boundary determined by eye is shown by the white dashed lines. In the processed image (Fig. 5b), the white domains are identified as crystalline by the algorithm and the black domains are identified as amorphous. The two morphologies are generally consistent with each other with only a few small discrepancies.

## 3. Results

### 3.1. Morphology of the partially amorphous sample

The morphology of the c/a domains offers clues to the mechanisms that govern amorphization. We analyzed a number of HRTEM images taken both near to and away from GBs. Fig. 6a shows a low magnification bright field image illustrating the types of locations where the HRTEM images were obtained. The black bands within the grains are bend contours. The discontinuity of the bands indicates different crystallographic orientations on both sides of the white dotted lines, which is a GB. SADPs show the beam direction $\boldsymbol{b}$ is near [011] for the grain on the left (Fig. 6b) and near $[1\overline{1}2]$ for the grain on the right (Fig. 6c). The positions where HRTEM images were taken are marked with white squares. To avoid any influence by the GB, the image positions within the grain are at least 100 nm away from the GB. Fig. 7 shows three typical HRTEM images and the corresponding c/a morphologies determined using the automated procedure. One dramatic feature of the morphologies is the irregular shape of the amorphous regions surrounded by winding, highly curved c/a boundaries. Taken at face value, this "dendritic" morphology is surprising. From the perspective of thermodynamics, the c/a boundaries contribute excess interfacial energy to the system, so their total areas should be minimized in order to lower the system energy. This minimization would result in rounded shapes of amorphous domains with smooth, low curvature c/a boundaries (similar to the large amorphous pockets observed in SiC by Snead et al. [24]), not the structure shown in Fig. 7.

The apparent morphology in Fig. 7 is a result of cascade overlap and the two-dimensional projection inherent to HRTEM, which we have demonstrated using a coarse-grained model of the amorphous pocket morphological evolution informed by SRIM and atomistic simulations. SRIM software is used to determine the number of primary knock-on atoms (PKAs) and their energies during irradiation with 1 MeV Kr ions. SRIM is a Monte Carlo simulation toolkit describing the collision process of ions with a target material [26]. In our calculation, the sample thickness is set to 50 nm, based on electron energy loss spectroscopy (EELS) measurement of the TEM sample. According to the experimental Kr ion fluence $(6.5 \times 10^{14} \text{ ions/cm}^2)$, 14,412 incident Kr ions impact a $47 \text{ nm} \times 47 \text{ nm}$ region (the size of HRTEM image in Fig. 7). The displacement energy of Si and C is set to 35 eV and 21 eV, respectively [14,16]. SRIM simulations indicate that all Kr ions pass through the sample with only a small amount of energy deposited. This result is not particularly surprising since the range of 1 MeV $\text{Kr}^{2+}$ in SiC (the distance traveled by the incident ion before it loses all its kinetic energy to the host material) is about $3.8 \,\mu\text{m}$, which is much larger than the 50 nm sample thickness. Table 1 lists the number and energy distributions of generated PKAs. It can be seen that the majority of PKAs have very low kinetic energy (<1 keV) and less than 1% PKAs have energy larger than 50 keV.

These generated PKAs further collide with atoms in SiC and create displacement cascades. This process has been extensively studied by MD simulations [11,27,28]. According to such simulations, low energy PKAs (a few keV or less) are only able to create a few isolated point defects [27]. Medium range energies of PKAs (tens of keV) usually create a so-called collision cascade, which consists of clusters of vacancies, interstitials and antisite defects with a spatial range on the order of nanometers [28]. For PKAs with higher energy (e.g., 50 keV), simulations reported multiple branches of the cascades, each similar in size to cascades in the medium energy

![](./images/814604255141822464_4.jpg)

Fig. 4. Histogram of intensity standard deviation values of small squares. Blue dots are experimental values. Green line is the fitted amorphous Gaussian and red line is the fitted crystalline Gaussian. Black line is the sum of two Gaussians. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/814604255141822464_5.jpg)

Fig. 5. Comparison of c/a morphologies in (a) the original HRTEM image with hand-drawn boundaries and (b) the image after processing. In (a) the c/a boundaries are shown as white dashed lines. In (b) white and black domains are crystalline and amorphous regions, respectively. The two images have the same magnification.

![](./images/814604255141822464_6.jpg)

Fig. 6. (a) Bright field image showing locations of the HRTEM images (marked as squares) with respect to a GB (marked as dotted line). Vector b indicates the nearest low- index zone of each grain. (b) SADP of grain A and (c) SADP of grain B.

range of PKAs [11]. As discussed in the introduction, MD simula- tions of Gao et al. found that the irradiated region became com- pletely amorphous after the overlap of 112 cascades of 10 keV Si or C PKAs [12]. In addition, the direct amorphization mechanism seems to be only important for heavy ions since no such directly amorphized region was found within the cascade of 50 keV Si PKA [13]. As the PKAs in our experiment are either Si or C recoils, the possibility of direct amorphization is not included in our model.

These findings from SRIM and MD simulations are incorporated into a coarse-grain model simulating the evolution of the amor- phous domains. In this model, the SiC sample is represented by a three dimensional (3D) square lattice of $217 \times 217 \times 230$ points separated $2.18\ \mathring{A}$ apart, so the density of lattice points is equal to the atomic density of SiC and the dimension of the matrix is the same as the dimension shown in the HRTEM images $(47\ \text{nm} \times 47\ \text{nm} \times 50\ \text{nm})$. As the exact relation between the PKA energy and the resulting cascade size is currently unknown in SiC, we take the size of a displacement cascade created by a 10 keV PKA as a unit and assume that the effective number of unit cascades for a given PKA is proportional to its energy. For example, a 20 keV PKA creates two unit cascades while a 5 keV PKA creates half of the unit cascade. Therefore the total PKAs during the $\text{Kr}^{2+}$ irradiation would create $7.89 \times 10^{4}$ unit cascades in the sample. Here only cascades that have PKA energies larger than 1 keV are counted. Even though the low energy PKAs account for a substan- tial fraction in total PKA population, they only generate a few point defects each. These point defects form a homogeneous background, which is not expected to contribute to the heterogeneous morpho- logical features of the c/a boundary. Based on Gao et al.'s simula- tions [28], the affected region of a 10 keV displacement cascade(one unit) is approximated as an ellipsoid with semi-principle axes $a = b = 2.6\ \text{nm}$ and $c = 5.2\ \text{nm}$, where the $c$ axis is parallel to the incident direction of Kr ions.

Cascade overlap is simulated by introducing elliptical cascades into the SiC matrix at random positions. A lattice point in the 3D matrix is considered to belong to an amorphous region after more than 112 cascades take place at that point. After irradiation, the sample matrix is projected onto the plane perpendicular to the incident beam as in HRTEM. An important parameter in making a projected image is the minimum amorphous volume fraction, $x_{\text{am}}$, in the 3D structure that is necessary for the 2D domains to appear as "amorphous" in the HRTEM images. Based on a series of image calculations using multislice method, Miller et al. [29] found that a sample could be up to thirty percent amorphous before the lattice periodicity in the HRTEM image was disrupted, and that a complete loss of lattice fringes occurred when the crys- talline volume fraction dropped below twenty percent. Based on these findings, we choose $x_{\text{am}} = 80\%$. Fig. 8 shows the final mor- phology generated for samples irradiated with $\text{Kr}^{2+}$ up to half of

![](./images/814604255141822464_7.jpg)

Fig. 7. (a–c) Original HRTEM images. (d–f) Corresponding images of the c/a morphologies from automated processing. In (d–f), white and black domains are crystalline and amorphous regions, respectively. All panels have the same magnification. These images correspond to the regions designated by white squares in Fig. 6. A larger version of these HRTEM images with clear lattice fringes can be found in Fig. S1 in Supplementary materials.

<table>
<caption>Table 1: Number and energy distribution of PKAs generated by 1 MeV Kr²⁺ in a 50 nm-thick SiC.</caption>
<thead>
<tr>
<th>PKA energy</th>
<th>PKA number</th>
<th>Fraction of PKAs</th>
</tr>
</thead>
<tbody>
<tr>
<td>In total</td>
<td>333,764</td>
<td>100.00%</td>
</tr>
<tr>
<td>0 keV–1 keV</td>
<td>274,786</td>
<td>82.33%</td>
</tr>
<tr>
<td>1 keV–10 keV</td>
<td>46,796</td>
<td>14.02%</td>
</tr>
<tr>
<td>10 keV–50 keV</td>
<td>9134</td>
<td>2.74%</td>
</tr>
<tr>
<td>&gt;50 keV</td>
<td>3048</td>
<td>0.91%</td>
</tr>
</tbody>
</table>

the dose to amorphization (0.675 dpa). The irregular shape of amorphous regions and the winding c/a boundaries in the simulated morphologies agree well with the experimental results shown in Figs. 5 and 7. Variation of $x_{am}$ between 70% and 90% only affects the area ratio of amorphous to crystalline regions, not the qualitative features of the c/a boundaries. These simulations show that cascade overlap is the governing mechanism for amorphization under Kr²⁺ irradiation. Combined with 2D projection, cascade overlap is responsible for the observed dendrite-like c/a morphology. With this understanding, we investigated previously published HRTEM images of irradiated SiC and found similar morphologies in images reported by Cabrero et al. of the partially amorphous region just before the damage peak in 3C SiC irradiated by 76 MeV Kr ions [5]. Although the nature and origins of the morphologies were not discussed in that reference, we believe they are due to similar processes as seen in the present work. In fact, at the depth where their HRTEM image was taken (about 8 μm from the irradiated surface), the electronic interactions and nuclear interactions between incident ions and target materials are about the same. Interestingly, according to SRIM calculation, it means that the kinetic energy of the Kr ions has decreased to about 1 MeV at that depth, which is comparable to the Kr energy used in our study.

### 3.2. Grain boundary effect on local amorphization ratio

Comparison of the c/a morphology at the GBs (Fig. 7b and e) and within grain interiors (Fig. 7a, c, d, and f) shows qualitatively that the amorphous domains are concentrated near the GB into a band of higher amorphization fraction. More quantitatively, the area fractions of amorphous domains in HRTEM images near and far from four different GBs are summarized in Table 2. The first and third columns contain values from images on both sides of the GB, and the second column shows the amorphization fraction from images that contain a GB. For locations 3 and 4, three images were taken at nearby positions for the same grain or GB, so the table

![](./images/814604255141822464_8.jpg)

Fig. 8. c/a morphology simulated using a coarse-grained model. White and black colors represent crystalline and amorphous regions, respectively. Simulations correspond to experimental conditions of 1 MeV Kr²⁺ irradiation with fluence = 6.5 × 10¹⁴ ions/cm².

### Table 2
Comparison of the areal amorphization fraction in HRTEM images with and without GB. Uncertainties for location 3 and 4 are the standard deviation over three nearby images.

|            | Grain A   | GB        | Grain B   | Grain orientation       |
|------------|-----------|-----------|-----------|-------------------------|
| Location 1 | 53%       | 64%       | 52%       | $[01\overline{1}]//[\overline{1}1\overline{2}]$ |
| Location 2 | 55%       | 66%       | 59%       | $[011]//[011]$          |
| Location 3 | $53\pm1\%$| $62\pm2\%$| $51\pm1\%$| $[011]//[011]$          |
| Location 4 | $51\pm1\%$| $62\pm1\%$| $50\pm5\%$| $[\overline{1}11]//[\overline{1}1\overline{2}]$ |

reports the mean and standard deviation of amorphization frac- tions for the three images. Images containing a GB always have a higher amorphization fraction than those within the grain interi- ors, implying that GBs increase the rate of amorphization in their vicinity. This phenomenon can be seen more clearly from the local amorphization fraction of narrow strips parallel to the GB. Fig. 9 shows the amorphization fraction within a 3 nm wide strip, $\Phi_{\text{am}}$, as a function of the strip's position in each HRTEM image. In Fig. 9b, the peak value of $\Phi_{\text{am}}$ is nearly 80% right at the GB and $\Phi_{\text{am}}$ gradually decreases on both sides. Similar data for the grain interior shows no such peak or gradient (Fig. 9a and c). The $\Phi_{\text{am}}$ profiles indicate that the enhancing effect of GBs on the amor- phization process is highly localized. At approximately 15–25 nm away from GB, $\Phi_{\text{am}}$ has already decreased close to the average amorphization fractions of grain interiors on both sides. It should be emphasized that the "amorphization fraction" here refers to area fraction of amorphous domains, not the volume amorphiza- tion fraction in a 3D sample. As demonstrated in Ref. [29], the rela- tionship between area fraction and volume fraction is monotonic but not linear. In addition, the exact area fraction value also depends on the criterion defining the "amorphous domains" (e.g., the parameter $\eta_{\text{th}}$). Therefore it would be difficult to determine quantitatively the volume amorphization fraction simply based on the 2D projections. However, the key point is that all the images from different locations on the sample show the same trend, as long as the same image processing method is applied. Therefore the local enhancement of amorphization by a GB is a real phe- nomenon, rather than an artifact introduced by the image processing.

The locally enhanced amorphization due to GBs seems contra- dictory given that GBs typically act as defect sinks. In fact, depleted zones of defects are often observed near GBs in metals [30]. There are several possible explanations for the unexpected effect of the GBs. First, the GBs might increase the defect production rate/sur- vival efficiency and therefore more defects would appear near GBs. This effect has been studied by MD simulations of radiation damage in SiC bicrystals with both low angle and high angle GBs [31,32]. It was found that defect production in GB regions was increased because the local disorder lowered the threshold dis- placement energies. However, the GB width (estimated to be about 4.92 Å in Ref. [31]) is much narrower than the affected region shown in our HRTEM images (about 15–25 nm). For defect produc- tion in crystalline regions adjacent to GBs, it was demonstrated that the defect production was largely unaffected by the presence of a GB and was independent of the GB type. Therefore the first hypothesis cannot explain the locally enhanced amorphization near GBs. A second possibility is that the amorphous phase might nucleate at the GBs and then grow into the grain. If this mechanism were dominant, a continuous amorphous band extending from the GB plane into grains on both sides of the GB would be expected. However, such bands are not found in the HRTEM images. Instead, amorphous domains can be seen as more networked along the GB as shown in Fig. 7e. Also, the amorphization fraction grad- ually decreases from the highest value at the GB to a lower value in the grain interior (Fig. 9b). Thus the nucleation and growth of the amorphous phase at the GBs cannot explain the locally enhanced amorphization.

The third possible explanation is interstitial starvation, which results from the high-energy barrier for recombination of C Frenkel pairs and the different diffusivities of self-interstitials and vacancies [25]. After initial intracascade recombination, the surviving radiation-induced interstitials and vacancies can be annihilated either by migrating to defect sinks, or by defect recom- bination. According to ab initio calculations [25,33], the barrier for a C interstitial and vacancy to recombine is as high as 0.90 eV. Therefore this recombination reaction is not activated in our irra- diation experiment and annihilation at defect sinks (e.g., GBs) becomes the dominant process in healing C point defects. Meanwhile, the migration barrier for C interstitials is much smaller (0.60 eV) than for C vacancies (3.66 eV). GBs are sinks for mobile C interstitials but not for immobile vacancies at the experimental temperature of 100 °C. The imbalance between the annihilation of C vacancies and interstitials results in an excess of vacancies near GBs. The excess vacancies accumulate as the irradiation con- tinues and drive the regions adjacent to the GBs into the amor- phous phase. The gradient of the vacancy density causes a gradient in the amorphization fraction as a function of distance from the GB. The interstitial starvation mechanism has been theo- retically predicted by rate theory calculations in SiC [25], and a similar effect in Si was also observed experimentally by Atwater et al. [34]. However, to our best knowledge, no experimental evi- dence for interstitial starvation phenomenon has been previously reported in SiC.

A simplified rate theory calculation is conducted here to demonstrate that interstitial starvation explains the $\Phi_{\text{am}}$ peak and gradient we observe. The one-dimension rate theory model is described by [25]

$$\frac{dc_{\text{i}}(x,t)}{dt}=D_{\text{i}}\nabla^{2}c_{\text{i}}(x,t)+G-Rc_{\text{i}}(x,t)c_{\text{v}}(x,t) \tag{1}$$

$$\frac{dc_{\text{v}}(x,t)}{dt}=D_{\text{v}}\nabla^{2}c_{\text{v}}(x,t)+G-Rc_{\text{i}}(x,t)c_{\text{v}}(x,t) \tag{2}$$

Here subscripts $i$ and $v$ stand for interstitial and vacancy, respectively, and $c(x,t)$ is the defect concentration at irradiation time $t$ at position $x$ in the grain. Four kinds of point defect, intersti- tials and vacancies of Si and C, are considered so there are four par- tial differential equations in total. $G$ stands for defect generation rate, which is defined as

$$G=\Gamma\eta\alpha_{\text{n}} \tag{3}$$

$\Gamma$ is the dose rate, which is $6.48\times10^{-4}$ dpa/s in the in-situ $\text{Kr}^{2+}$ irradiation. $\eta$ is the intracascade recombination rate (set to 0.8) and $\alpha_{\text{n}}$ is the generation fraction of defect type $n$. $R$ stands for the reaction rate of vacancy-interstitial recombination, which has the general form [35,36]

$$R=4\pi r_{\text{c}}(D_{\text{i}}+D_{\text{v}})\text{ for }E_{\text{m}}\gg E_{\text{r}} \tag{4}$$

$$R=4\pi r_{\text{c}}(D_{\text{i}}+D_{\text{v}})\exp\left(\frac{E_{\text{m}}^{\text{fast}}-E_{\text{r}}}{k_{\text{B}}T}\right)\text{ for }E_{\text{m}}\approx\text{ or }<E_{\text{r}} \tag{5}$$

In Eqs. (4) and (5) $r_{\text{c}}$ is the recombination reaction radius, $E_{\text{r}}$ is the reaction energy barrier, $E_{\text{m}}$ is the migration barrier and $E_{\text{m}}^{\text{fast}}$ is the migration barrier for the faster defect of the two defects par- ticipating in the recombination reaction. The parameter values used in this calculation are summarized in Table 3, all of which are taken from Refs. [25] and [33]. To be consistent with experi- mental conditions, the grain size is assumed to be 1 μm and the irradiation is performed over 1040 s (which corresponds to 0.675 dpa). As boundary conditions, the defect concentrations at GBs

![](./images/814604255141822464_9.jpg)

Fig. 9. Local amorphous area fraction ($\Phi_{\text{am}}$) in 3 nm strips as a function of the strip position (x) in HRTEM images. The position of the GB in (b) is marked by an arrow. Horizontal dotted lines in (a) and (c) indicate the average amorphization ratio in HRTEM images of grain A and B.

Table 3
Parameter values used in the rate theory calculations (from Ref. [25,36]). "I" stands for interstitial and "V" stands for vacancy.

|       | $D$/cm²/s       | $E_{\text{m}}$/eV | $\Delta E_{\text{x}}$/eV | $a_{\text{n}}$ | $E_{\text{i}}$/eV | $r_{\text{c}}$/nm |
|-------|-----------------|-------------------|--------------------------|----------------|-------------------|-------------------|
| Si, I | $2.08 \times 10^{-14}$ | 0.83              | 8.745                    | 0.075          | 0.03              | 0.63              |
| Si, V | $2.70 \times 10^{-36}$ | 2.40              | 4.966                    |                |                   |                   |
| C, I  | $1.09 \times 10^{-12}$ | 0.60              | 6.953                    | 0.435          | 0.90              | 0.21              |
| C,V   | $2.47 \times 10^{-53}$ | 3.66              | 4.193                    |                |                   |                   |

are set equal to zero throughout the entire calculation. The initial interstitial and vacancy concentrations are assumed to be zero as well. We use the excess energy $\Delta E$ as a function of the calculated defect concentration to estimate of the degree of amorphization. $\Delta E$ is the sum of extra energy contributions from all four kinds of point defects to the system

$$
\Delta E = \sum \Delta E_{\text{x}} c_{\text{x}} \tag{6}
$$

In Eq. (6), $\Delta E_{\text{x}}$ is the energy gained by introducing one point defect and x stands for interstitial or vacancy of either C or Si. The values of $\Delta E_{\text{x}}$ are obtained from Ref. [25] and summarized in Table 3. In the model the sample is regarded as completely amorphous when $\Delta E$ equals the energy difference between the amorphous and crystalline phase ($\Delta E_{\text{am}}$). We choose $\Delta E_{\text{am}} = 0.6$ eV/atom based on previous MD simulations [37].

Fig. 10 shows $\Delta E$ as a function of position in a 1 $\mu$m grain. In the middle region of the grain, $\Delta E$ is low (less than 0.1 eV) because of the mutual recombination of interstitials and vacancies. $\Delta E$ increases sharply close to GBs since a significant fraction of interstitials diffuse to the GB and leave behind copious unrecombined vacancies. As shown in the inset of Fig. 10, the conditions $\Delta E = \Delta E_{\text{am}}$ is met at about 6 nm from a GB, and $\Delta E = 0.5 \ \Delta E_{\text{am}}$ occurs at about 22 nm. The distribution of $\Delta E$ implies that interstitial starvation could produce an affected region tens of nanometers wide, similar to the width observed in our experiments (Fig. 9b). It is worth pointing out that the high energy barrier for C Frenkel pair recombination ($E_{\text{r}} = 0.90$ eV) plays a critical role in determining the size of the affected region. If we assume there is no barrier for the recombination, then $\Delta E = 0.5 \Delta E_{\text{am}}$ would occur at the distance of only about 0.3 nm from a GB, which means that without recombination barriers there would be no interstitial starvation. One should of course keep in mind that the exact size of the affected region by interstitial starvation may change due to the uncertainties of the parameters in the model (defect diffusivity, reaction barriers, etc.) and in the experiments. Nevertheless this calculation shows that interstitial starvation can produce effects on the scale of the experimentally observed peak and gradient of amorphization fraction near a GB.

![](./images/814604255141822464_10.jpg)

Fig. 10. Excess energy $\Delta E$ as a function of position within a 1 $\mu$m grain. GBs are located at x = 0 nm and 1000 nm. In the inset we show a magnification of the left part of the curve in order to clearly show the position where $\Delta E = \Delta E_{\text{am}} = 0.6$ eV/atom and $\Delta E = 0.5 \Delta E_{\text{am}} = 0.3$ eV/atom.

## 4. Additional discussion and conclusions

Understanding gained from our study has important implications for the question regarding whether refining the grain size to nanometer scale will improve the resistance of SiC to RIA. Previous experiments found that the same nc SiC exhibited a superior resistance compared to microcrystalline or single crystal SiC when irradiated with 1.25 MeV electrons and 2 MeV Si ions, but inferior resistance when irradiated with 1 MeV Kr ions [16,17,21]. Current explanations for the performance discrepancy are mostly focused on the material microstructures. Increased resistance to RIA has been attributed to the higher volume fraction of GBs acting as defect sinks. Decreased resistance to RIA has been attributed to the high GB fraction increasing the free energy of the material, which makes the system less stable and more susceptible to amorphization. Although these arguments are perhaps valid, they are insufficient to explain the different behaviors of the same nanocrystalline materials under different irradiation conditions. The coupling between different amorphization mechanisms and the material microstructures demonstrated here helps shed light on this mystery. Due to their light mass, electrons are only able to generate isolated Frenkel pairs. These point defects migrate, accumulate and finally lead to amorphization. For this type of amorphization process, defect annihilation at GBs becomes more efficient when the grain size is smaller (because of a larger volume fraction of GBs) and this is the dominant factor in improving the material resistance. However, as revealed by the HRTEM images and morphology simulations in this study, cascade overlap is the governing amorphization mechanism for heavy ion irradiation, such as Kr. Within the highly disordered region, or displacement cascade, there are both point defects and a large number of defect clusters. These defect clusters are very stable and much less mobile than point defects, which make it difficult for the clusters to be

annihilated at GBs. Light ions, like Si, are less effective in transferring kinetic energy to PKAs due to their lower mass. As mentioned earlier, low energy PKAs tend to produce dispersed point defects rather than concentrated displacement cascades, so amorphization by light ions may be driven more by defect accumulation, which is similar to the case for electrons. In addition to the different amorphization mechanisms, interstitial starvation may also play a substantial role in determining the RIA resistance of nc SiC by enhancing the local amorphization process near GB. This effect is probably negligible for materials with large grains (because it is limited to the regime of about 20 nm on either side of the GB), but it would become significantly more important when the grain size is refined. GBs suppress RIA (increase resistance) because they act as sinks for point defects, but also facilitate the amorphization process because of the interstitial starvation. A balance of the two competing effects could lead to an intermediate grain size that maximizes the radiation resistance of SiC.

In summary, the amorphization mechanism in SiC with Kr ion irradiation is investigated by both HRTEM and coarse-grained simulation methods. It is demonstrated that the unique morphology of the partially amorphous sample results from the overlap of displacement cascades, which is the governing amorphization mechanism under heavy ion irradiation. The different amorphization mechanisms may help explain different behaviors of nc SiC irradiated with different irradiation species. By comparing local amorphization fractions near GBs and in grain interior, the interstitial starvation phenomenon is identified, which might become a considerable deteriorating effect for nanocrystalline SiC when the grain size is small enough.

## Acknowledgments
The authors acknowledge the US Department of Energy Basic Energy Sciences for funding this research (Fund number DE-FG02-08ER46493). The authors also gratefully acknowledge use of facilities and instrumentation supported by NSF through the University of Wisconsin Materials Research Science and Engineering Center (DMR-1121288). The electron microscopy with *in situ* irradiation was accomplished at Argonne National Laboratory at the IVEM-Tandem Facility, a U.S. Department of Energy Facility funded by the DOE Office of Nuclear Energy, operated under Contract No. DE-AC02-06CH11357 by UChicago Argonne, LLC.

## Appendix A. Supplementary data
Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.actamat.2015.07.070.

## References
[1] L.L. Snead, T. Nozawa, Y. Katoh, T.S. Byun, S. Kondo, D.A. Petti, Handbook of SiC properties for fuel performance modeling, J. Nucl. Mater. 371 (2007) 329–377.
[2] Y. Katoh, L.L. Snead, I. Szlufarska, W.J. Weber, Radiation effects in SiC for nuclear structural applications, Curr. Opin. Solid St M 16 (2012) 143–152.
[3] W.J. Weber, Models and mechanisms of irradiation-induced amorphization in ceramics, Nucl. Instrum. Methods B 166 (2000) 98–106.
[4] V.I. Ivashchenko, P.E.A. Turchi, V.I. Shevchenko, Simulations of the mechanical properties of crystalline, nanocrystalline, and amorphous SiC and Si, Phys Rev B 75 (2007) 085209.
[5] J. Cabrero, F. Audubert, R. Pailler, A. Kusiak, J.L. Battaglia, P. Weisbecker, Thermal conductivity of SiC after heavy ions irradiation, J. Nucl. Mater. 396 (2010) 202–207.
[6] M. Ishimaru, I.T. Bae, A. Hirata, Y. Hirotsu, J.A. Valdez, K.E. Sickafus, Volume swelling of amorphous SiC during ion-beam irradiation, Phys. Rev. B 72 (2005) 024116.
[7] W.J. Weber, L.M. Wang, N. Yu, The irradiation-induced crystalline-to-amorphous phase transition in alpha-SiC, Nucl. Instrum. Methods Phys. Res. B 116 (1996) 322–326.
[8] E. Wendler, A. Heft, W. Wesch, Ion-beam induced damage and annealing behaviour in SiC, Nucl. Instrum. Methods Phys. Res. B 141 (1998) 105–117.
[9] W. Bolse, Formation and development of disordered networks in Si-based ceramics under ion bombardment, Nucl. Instrum. Methods Phys. Res. B 141 (1998) 133–139.
[10] W. Bolse, Amorphization and recrystallization of covalent tetrahedral networks, Nucl. Instrum. Methods Phys. Res. B 148 (1999) 83–92.
[11] F. Gao, W.J. Weber, Atomic-scale simulation of 50 keV Si displacement cascades in beta-SiC, Phys. Rev. B 63 (2001) 054101.
[12] F. Gao, W.J. Weber, R. Devanathan, Defect production, multiple ion-solid interactions and amorphization in SiC, Nucl. Instrum. Methods Phys. Res. B 191 (2002) 487–496.
[13] W.J. Weber, F. Gao, R. Devanathan, W. Jiang, C.M. Wang, Ion-beam induced defects and nanoscale amorphous clusters in silicon carbide, Nucl. Instrum. Methods Phys. Res. B 216 (2004) 25–35.
[14] C. Jiang, M.J. Zheng, D. Morgan, I. Szlufarska, Amorphization driven by defect-induced mechanical instability, Phys. Rev. Lett. 111 (2013) 155501.
[15] F. Gao, W.J. Weber, Cascade overlap and amorphization in 3C-SiC: defect accumulation, topological features, and disordering, Phys. Rev. B 66 (2002) 024106.
[16] Y.W. Zhang, M. Ishimaru, T. Varga, T. Oda, C. Hardiman, H.Z. Xue, Y. Katoh, S. Shannon, W.J. Weber, Nanoscale engineering of radiation tolerant silicon carbide, Phys. Chem. Chem. Phys. 14 (2012) 13429–13436.
[17] L. Jamison, M.J. Zheng, S. Shannon, T. Allen, D. Morgan, I. Szlufarska, Experimental and ab initio study of enhanced resistance to amorphization of nanocrystalline silicon carbide under electron irradiation, J. Nucl. Mater. 445 (2014) 181–189.
[18] W. Jiang, H. Wang, I. Kim, Y. Zhang, W.J. Weber, Amorphization of nanocrystalline 3C-SiC irradiated with Si+ ions, J. Mater. Res. 25 (2010) 2341–2348.
[19] W. Jiang, H. Wang, I. Kim, I.T. Bae, G. Li, P. Nachimuthu, Z. Zhu, Y. Zhang, W.J. Weber, Response of nanocrystalline 3C silicon carbide to heavy-ion irradiation, Phys. Rev. B 80 (2009) 161301(R).
[20] W.L. Jiang, L. Jiao, H.Y. Wang, Transition from irradiation-induced amorphization to crystallization in nanocrystalline silicon carbide, J. Am. Ceram. Soc. 94 (2011) 4127–4130.
[21] L.S. Jamision, S. Shannon, I. Szlufarska, Temperature and irradiation species dependence of radiation response of nanocrystalline silicon carbide, J. Mater. Res. 29 (2014) 2871–2880.
[22] X.M. Bai, A.F. Voter, R.G. Hoagland, M. Nastasi, B.P. Uberuaga, Efficient annealing of radiation damage near grain boundaries via interstitial emission, Science 327 (2010) 1631–1634.
[23] M. Ishimaru, Y.W. Zhang, S. Shannon, W.J. Weber, Origin of radiation tolerance in 3C-SiC with nanolayered planar defects, Appl. Phys. Lett. 103 (2013) 033104.
[24] L.L. Snead, S.J. Zinkle, J.C. Hay, M.C. Osborne, Amorphization of SiC under ion and neutron irradiation, Nucl. Instrum. Methods Phys. Res. B 141 (1998) 123–132.
[25] N. Swaminathan, D. Morgan, I. Szlufarska, Role of recombination kinetics and grain size in radiation-induced amorphization, Phys. Rev. B 86 (2012) 214110.
[26] J.F. Ziegler, Srim-2003, Nucl. Instrum. Methods Phys. Res. B 219 (2004) 1027–1036.
[27] J.M. Perlado, L. Malerba, A. Sanchez-Rubio, T.D. de la Rubia, Analysis of displacement cascades and threshold displacement energies in beta-sic, J. Nucl. Mater. 276 (2000) 235–242.
[28] R. Devanathan, W.J. Weber, T.D. de la Rubia, Computer simulation of a 10 keV Si displacement cascade in SiC, Nucl. Instrum. Methods Phys. Res. B 141 (1998) 118–122.
[29] M.L. Miller, R.C. Ewing, Image simulation of partially amorphous materials, Ultramicroscopy 48 (1993) 203–237.
[30] S. Kondo, Y. Katoh, L.L. Snead, Analysis of grain boundary sinks and interstitial diffusion in neutron-irradiated SiC, Phys. Rev. B 83 (2011) 075202.
[31] N. Swaminathan, P.J. Kamenski, D. Morgan, I. Szlufarska, Effects of grain size and grain boundaries on defect production in nanocrystalline 3C-SiC, Acta Mater. 58 (2010) 2843–2853.
[32] N. Swaminathan, M. Wojdyr, D.D. Morgan, I. Szlufarska, Radiation interaction with tilt grain boundaries in beta-SiC, J. Appl. Phys. 111 (2012).
[33] M.J. Zheng, N. Swaminathan, D. Morgan, I. Szlufarska, Energy barriers for point-defect reactions in 3C-SiC, Phys. Rev. B 88 (2013) 054105.
[34] H.A. Atwater, W.L. Brown, Grain-boundary mediated amorphization in silicon during ion irradiation, Appl. Phys. Lett. 56 (1990) 30–32.
[35] N. Swaminathan, D. Morgan, I. Szlufarska, Ab initio based rate theory model of radiation induced amorphization in beta-SiC, J. Nucl. Mater. 414 (2011) 431–439.
[36] T.R. Waite, General theory of bimolecular reaction rates in solids and liquids, J. Chem. Phys. 28 (1958) 103–106.
[37] R. Devanathan, F. Gao, W.J. Weber, Amorphization of silicon carbide by carbon displacement, Appl. Phys. Lett. 84 (2004) 3909–3911.