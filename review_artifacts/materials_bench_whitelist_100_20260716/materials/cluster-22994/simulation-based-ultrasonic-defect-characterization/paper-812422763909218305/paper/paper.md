# Advances in techniques for the ultrasonic monitoring of the cleanliness of steel

Cite as: AIP Conference Proceedings 509, 1441 (2000); https://doi.org/10.1063/1.1306204
Published Online: 16 November 2000

Y. Guo, C. Spore, F. J. Margetan, R. B. Thompson, and A. Ahmad

![](./images/812422763909218305_1.jpg)
![](./images/812422763909218305_2.jpg)

![](./images/812422763909218305_3.jpg)

AIP Conference Proceedings 509, 1441 (2000); https://doi.org/10.1063/1.1306204
509, 1441

© 2000 American Institute of Physics.

ADVANCES IN TECHNIQUES FOR THE ULTRASONIC MONITORING OF THE
CLEANLINESS OF STEEL

Y. Guo, C. Spore, F. J. Margetan, and R. B. Thompson
Center for Nondestructive Evaluation
Iowa State University
Ames, IA 50011

A. Ahmad
Eaton Corporation, Innovation Center
Southfield, MI 48037

INTRODUCTION

Ultrasonic techniques are of considerable interest in characterizing the cleanliness of steel billet. As compared to metallographic techniques, their ability to rapidly sample significant volumes of material in a nondestructive fashion is particularly attractive.

In this work we describe the use of physically based models of an ultrasonic pulse/echo inspection process to guide technique optimization for detecting inclusions through cylindrical surfaces in steel bar stock. Models are used for three purposes. Beam models are used to select transducer focal properties that will be minimally affected by the cylindrical geometry of the billet surface, which acts to defocuses the beam in a plane perpendicular to the billet axis. Flaw response models are used to predict the strength of echoes from undesirable inclusions, in particular those consisting of highly brittle material such as alumina ($Al_2O_3$) which can lead to premature failure. Microstructural response models are used to predict backscattered grain noise levels for microstructures of a given type and grain size. The flaw response and noise predictions combine to yield estimates of the minimum detectable inclusion size. This information can be used to guide the pre-inspection heat treatment which determines the final microstructure.

As an example of the integrated use of these tools, we discuss two competing designs for a system to inspect 3-inch diameter cylindrical billet used for the manufacture of gears. One design uses a standard, spherically-focused transducer; the other uses a bi-cylindrically focused transducer designed to better inspect the zone where gear teeth will later be machined. We will assume that the inclusions are alumina "stringers" whose elongation direction is aligned with the billet axis. Our main goal is to estimate stringer detectability for both the standard and optimized transducers.

INITIAL EXPERIMENTAL STUDIES AND MODEL VALIDATION

The motivation for our initial experimental studies is as follows. Spherically focused probes are often used in immersion inspections, and, for normal incidence through a flat entry surface, produce circular beam spots in the metal. However, in the case of normal incidence on a cylindrical surface, the surface curvature acts to defocus and distort the beam, thus broadening the images of stringers in the circumferential direction in rotational C-scans. We want to observe this broadening by comparing C-scans acquired through flat and curved surfaces,0 and then determine whether our beam model properly accounts for surface curvature effects.

CP509, *Review of Progress in Quantitative Nondestructive Evaluation*, edited by D. O. Thompson and D. E. Chimenti
© 2000 American Institute of Physics 1-56396-930-0/00/$17.00

A specimen was cut from a 2.5-inch diameter cylinder of 1018 steel, as shown in Fig. 1(a). Inclusions in the specimen could be imaged through either flat surface ① or curved surface ②. Fig. 1(b) depicts the SONIX ultrasonic immersion system used to perform C-scans of the semi-cylindrical test specimen. Both rotational (y, $\theta$) and rectangular (x, y) C-scans were performed using a 15 MHz, broadband, spherically-focused transducer having a nominal 0.5" diameter and 3.5" focal length. The transducer had been characterized by the beam-mapping method of Ref. [1], and determined to have an effective diameter of 0.48 inches and a geometrical focal length in water of 3.80 inches.

Fig. 2 displays a rotational C-scan acquired through the curved surface of the semi-cylinder with the beam focused about 3/8 inch (10 mm) below the surface. In the image, the B/W shading represents the peak-to-peak amplitude of the RF echo seen within an "arrive time" gate of interest. In this case the gate extended from 1.8 $\mu$s to 5.0 $\mu$s after the front-wall echo, corresponding to metal depths of 5 to 15 mm. A number of inclusions can be seen in the C-scan, and their images tend to be quite broad in the rotational direction. A important question is whether this broad appearance is due to beam defocusing effects, or are the inclusions themselves broad in the lateral direction?

The broadening is likely due to beam effects, because images of the same inclusions are much narrower in C-scans acquired through the flat entry surface, as illustrated in Figure 3. In comparing the rotational and linear C-scans, we have "matched" the horizontal scales to insure that the arc length of beam travel at the depth of the defect in Figure 2 is the same as the linear length of travel in Figure 3. Note that Figures 2 and 3 also contain predicted defect images made using the

![](./images/812422763909218305_4.jpg)

Figure 1. (a) Specimen geometry and (b) measurement system.

![](./images/812422763909218305_5.jpg)

Figure 2. Example of a rotational C-scan. The beam is focused at the depth of the indicated inclusion. (Distance in the $\theta$ direction has been scaled to the length of the arc containing the inclusion.)

![](./images/812422763909218305_6.jpg)

Figure 3. Example of a rectangular C-scan. The beam was normal to and focused 1.5 cm below the flat entry surface.

Gauss-Hermite beam model [2]. In the model calculation, the stringer diameter is assumed to be negligible compared to the beam diameter and the stringer echo is assumed to be proportional to the incident $|pressure|^2$ at 15 MHz integrated along the stringer length. The measured and predicted images are then scaled to have same peak brightness.

These results indicate that: (1) surface curvature acts to broaden inclusion images in the rotational direction; and (2) model predictions for broadening agree well with experiments. This suggests using the beam model to design a better transducer lens that can compensate for the defocusing effect of surface curvature and hence improve the lateral resolution.

## TRANSDUCER LENS OPTIMIZATION

The Gauss-Hermite beam model was used to design an optimized lens for a 15-MHz transducer having a (nominally) 0.5"-diameter circular element. The object was to determine appropriate geometric focal lengths, Fx and Fy, in the xz and yz planes of Figure 1b, respectively. Three design approaches were considered, each yielding different {Fx, Fy} values: (1) maximizing the on-axis pressure amplitude at a specified inspection depth in the solid; (2) having the minimum beam waist locations in the xz and yz planes as near as possible to the specified inspection depth; and, (3) trying to best reproduce the amplitude-vs-depth profile that a spherically focused probe would produce beneath a flat entry surface. The first two methods each had an undesirable consequence, namely that the focal maximum did not occur at the depth specified in the fitting procedure. For example, if one adjusts the lens parameters to maximize the value of the on-axis pressure amplitude at some specific metal depth, $Z'$, the peak in the resulting pressure-amplitude-vs-depth curve does not occur at depth $Z'$. Although the amplitude is as large as possible at depth $Z'$, it is even larger at some other depth. Similarly, if the lens parameters are adjusted to position the minimum beam diameters at depth $Z'$, the peak on-axis pressure again occurs at some depth other than $Z'$. This is because the minimum diameter point (defined as the full width at half maximum) does not exactly coincide with the point of peak on-axis pressure. For these reasons, we settled on fitting method 3, which directly uses the pressure-amplitude-vs-depth curve and consequently always positions the focal maximum at or very near the desired depth.

As an example, consider the design of an optimized transducer for inspecting 3-inch diameter bar stock when the region of greatest interest is the first 2/5 inches below the cylindrical surface. We consequently want to focus the beam approximately 1/5 of an inch below the surface. We begin with a commercially available 15-MHz, spherically-focused probe having a nominal 0.5" diameter and 2.5" focal length. We refer to this as our "existing probe". By mapping the transducer's axial profile in water and then adjusting the Gauss-Hermite model parameters to best reproduce the profile data [1], we determined the effective diameter and geometrical focal length of

the existing probe to be 0.51" and 2.93", respectively. For the existing probe, we then used the beam model to calculate the $|{\rm pressure}|^2$-vs-depth profile in steel for a normal-incidence inspection through a flat entry surface. The assumed inspection waterpath was 1.97", so as to place the focal maximum at the desired 1/5" depth. For the curved-surface inspection, we then adjusted Fx, Fy, and the water path in an attempt to best reproduce the amplitude-vs-depth profile obtained for the flat-surface case (discounting the effects of water attenuation). The focal lengths of the optimized probe were found to be Fx=2.25 and Fy=2.58 inches, with an associated waterpath of 1.61". For comparison, we similarly determined the optimum water path (again with goal of reproducing the amplitude-vs-depth profile through a flat surface) for the existing probe when using it for inspections through the curved surface (2.08 inches). In all of the above calculations, the speeds of longitudinal sound in water and steel were taken to be 0.149 cm/μs and 0.590 cm/μs, respectively.

Fig. 4 shows calculated on-axis and lateral $|{\rm pressure}|^2$ profiles in steel for three cases, i.e., existing probe through the flat interface (case 1), existing probe (optimized waterpath) through the curved interface (case 2), and optimized probe through the curved interface (case 3). The profiles for case 3 are similar to those of case 1, indicating that the design criteria were sucessfully implemented.

As was done earlier in Figs. 2-3, we then used the model to calculate C-scan images for hypothetical inspections of flat and curved steel specimens. In this case we assumed a single 3-mm-long thin stringer located 0.21 inches below the entry surface. The results for our three cases are shown in Fig. 5. For the images in the first row, a fixed scale for converting amplitude to gray-scale intensity was used so that we can directly compare absolute signal strengths. For the three images in the second row, the model gain was adjusted for each to produce the same maximum gray-scale intensity. This allows us to better compare the resolutions in the rotational (horizontal) direction . Comparing the use of the existing and optimized transducers for inspections through the curved surface, we find a 3 dB improvement in signal strength and 25% improvement in lateral resolution for the optimized probe.

## ESTIMATES OF MINIMUM DETECTABLE INCLUSION SIZE

We will now use models to estimate the minimum dectectable stringer size for inspections using the existing and optimized transducers. In steel bar stock, inclusions of aluminum oxide (alumina or $\mathrm{Al_2O_3}$) are a primary concern, so we will assume that the model defects are cylindrical, polycrystalline alumina "stringers" of various diameters and lengths. Before the models can be applied, pertinent ultrasonic properties of steel bar stock must be known. These include the longitudinal-wave velocity, attenuation, and backscattered grain noise Figure-of-Merit (FOM). The latter is a measure of the noise-generating capacity of the material, and is equal to the square root of the grain-noise backscatter coefficient [3]. The three ultrasonic properties can be obtained through the series of immersion measurements illustrated in Fig. 6, details of which can be found in

![](./images/812422763909218305_7.jpg)
(a) On-axis profile

![](./images/812422763909218305_8.jpg)
(b) Lateral profile (0.21" deep)

Figure 4. Predicted on-axis $|{\rm pressure}|^2$ profiles in steel at 15-MHz for three model cases.

![](./images/812422763909218305_9.jpg)

Figure 5. Calculated C-scan images of an ideal stringer in steel for inspections using the existing and optimized transducers.

references [4, 5]. Velocity is determined by measuring specimen thickness and times-of-flight for successive back-wall echoes. To measure attenuation, we compare spectral amplitudes of the first back wall echoes of a rectangular steel specimen and a fused-quartz reference block. To measure the grain noise FOM, we compare spatially averaged spectra of grain noise signals to the spectrum of a fused-quartz back-wall echo.

Heat treatment is often performed on bar stock specimens prior to inspection to decrease the mean grain size, hence lowering backscattered grain noise levels and improving inspectability. Specimens of 3''-diameter, 8620 steel bar stock were obtained prior to and after heat treatment. Their microstructures at corresponding depths are shown in Fig. 7. The front-wall and back-wall surfaces were machined flat to facilitate the UT property measurements in the radial direction. Measured L-wave velocities were 0.590 cm/µs before heat treatment and 0.591 cm/µs after heat treatment. Measured attenuation and grain noise FOM are shown as functions of frequency in Fig. 8; note that both are reduced substantially by heat treatment as expected.

Having measured the basic UT properties of the metal, we are now in position to use existing models to estimate signal/noise ratios (SNR) for inspection of 3''-diameter cylindrical stock containing hypothetical alumina stringers. Two models are used. A "flaw signal" model [6] is used to calculate the A-scan echo from a given inclusion. The model uses a modified Born approximation, and requires a numerical integration of the incident pressure field over the flaw volume. A backscattered noise model [7] is then used to compute statistical properties of the competing grain noise. The noise model uses a single-scattering approximation, and assumes that the observed RF noise is an incoherent summation of echoes from all insonified grains. Both

![](./images/812422763909218305_10.jpg)

Figure 6. Experimental set-ups for measuring basic ultrasonic properties of steel bar stock.

![](./images/812422763909218305_11.jpg)
![](./images/812422763909218305_12.jpg)

(a) Before Heat Treatment
(b) After Heat Treatment

Figure 7. 8620 steel bar stock microstructure (darker regions are chromium rich)

![](./images/812422763909218305_13.jpg)
![](./images/812422763909218305_14.jpg)

(a) Attenuation
(b) Grain noise

Figure 8. Measured UT properties of 3-inch diameter 8620 steel bar stock.

models treat incident broadband pulses. Here we define the SNR as illustrated in Figure 9: the ratio of the peak-to-peak amplitude of the stringer echo (in the absence of noise) to the spatially-averaged peak-to-peak noise voltage (in the absence of a defect) seen within a time gate of interest. In this case the time gate has a 2-µs duration centered on the defect echo. The SNR can then be obtained by taking the ratio of the flaw signal amplitude and the mean grain noise level.

The flaw signal model requires the density and sonic velocities of the alumina inclusion material. For alumina polycrystalline aggregates, the sound speeds can be estimated by taking the Voigt average of the single-crystal elastic constants. The following values, taken from Ref. [8] were used in our work: 1.1293 cm/µs for the longitudinal-wave speed; 0.7092 cm/µs for the shear-wave speed, and 3.97 g/cm³ for the inclusion density. In our model calculations we assume the inclusion is an alumina cylindrical "stringer" whose elongation direction is parallel to the axis of the 3"-diameter steel cylinder in which it resides. We inspect through the curved surface at normal incidence using the "existing" and "optimized" transducers of the previous section. In each case, the center of the inclusion is assumed to lie along the central ray of the incident sonic beam.

Fig. 10a compares calculated S/N ratios for the two transducers as functions of inclusion diameter for stringers of a fixed length (0.2") and depth (0.22"). Figure 10b compares S/N ratios as functions of flaw depth for stringers of fixed length (0.2") and diameter (3.3 mils). S/N ratios are seen to be comparable for the two inspections. From graphs such as those shown in Figure 10 we can estimate the minimum detectable inclusion size. For example, let us define detectability as S/N > 5. Then, for our heat-treated bar stock, we would expect to detect "ideal" cylindrical stringers with diameters ≥ 3 mils, so long at they were located near the focal zone of either transducer and had lengths of a few several mm or more.

![](./images/812422763909218305_15.jpg)

Figure 9. Meaning of signal-to-noise ratio (S/N).

![](./images/812422763909218305_16.jpg)

(a) SNR vs. inclusion diameter

![](./images/812422763909218305_17.jpg)

(b) SNR vs. flaw depth

Figure 10. Predicted signal-to-noise ratios for inspection of 3″ cylindrical bar stock after heat treatment.

## CONCLUSIONS

In conclusion, we have demonstrated the use of models to optimize ultrasonic inspections of cylindrical steel bar stock, to predict C-scan images of "stringer" inclusions, and to estimate associated signal-to-noise ratios. For one example involving the inspection of heat-treated, 3″-diameter, 8620 stock, we designed an optimized lens for a 15 MHz circular transducer. As compared to a spherically-focused transducer of the same diameter, we found a 3 dB improvement in signal strength for stringers in the focal zone and a 25% improvement in resolution in the rotational direction. S/N ratios for thin alumina stringers were comparable for the two probes, and we estimated that ideal stringers with diameters greater that 3 mils could be readily detected in the focal zone of either probe. When a spherically-focused transducer is used, the defocusing effect of the cylindrical surface generally causes a reduction in our ability to detect small interior defects. This reduction tends to worsen when: (1) the radius of curvature of the surface is reduced; and (2) the inspection depth is increased. In our example, the surface curvature is not severe relative to the beam diameter at the entry point, and the inspection depth is not large. Consequently, optimizing the transducer lens produces only a modest improvement in inspectability. Note that the procedures outlined in this paper provide a method for estimating the minimum detectable stringer diameter, as a function of the microstructural noise level. In future work, it should be possible to relate the minimum detectable diameter directly to grain size.

## ACKNOWLEDGEMENTS

The authors wish to thank Dr. C. P. Chiou for his great help in the use of his flaw response model. This work was supported by the NSF Industry/University Cooperative Research program.

## REFERENCES

1.  I. Yalda, P. D. Panetta, F. J. Margetan, and R. B. Thompson, "Characterization of Ultrasonic Focused Transducers Using Axial Scans and C-scans", in *Review of Progress in QNDE, 16A*, D. O. Thompson and D. E. Chimenti, Eds., (Plenum Press, New York, 1997), pp. 927-934.

2.  B. P. Newberry and R. B. Thompson, "A Paraxial Theory for the Propagation of Ultrasonic Beams in Anisotropic Solids", *J. Acoust. Soc. Am.* 85, (1989), pp. 2290-2300.

3.  F. J. Margetan, R. B. Thompson, and I.Yalda, "Modeling Ultrasonic Microstructural Noise in Titanium Alloys", in *Review of Progress in QNDE, 12B*, D. O. Thompson and D. E. Chimenti, Eds., (Plenum Press, New York, 1993), pp. 1735-1742.

4.  P. D. Panetta, F. J. Margetan, I. Yalda, and R. B. Thompson, "Ultrasonic Attenuation Measurements in Jet-Engine Titanium Alloys", in *Review of Progress in QNDE, 15B*, D. O. Thompson and D. E. Chimenti, Eds., (Plenum Press, New York, 1996), pp. 1525-1532.

5.  F. J. Margetan, R. B. Thompson, I. Yalda, and Y. K. Han, *Detectability of Small Flaws in Advanced Engine Alloys*, Center for NDE, Iowa State University, July 1993.

6.  C. P. Chiou, F. J. Margetan, R. B. Thompson, and B. Boyd, "Development of Ultrasonic Models for Hard-Alpha Inclusions in Titanium Alloys", in *Review of Progress in QNDE, 16B*, D. O. Thompson and D. E. Chimenti, Eds., (Plenum Press, New York, 1997), pp. 1529-1536.

7.  F. J. Margetan, I. Yalda, and R. B. Thompson, "Predicting Gated-Peak Grain Noise Distributions for Ultrasonic Inspections of Metals", in *Review of Progress in QNDE, 15B*, D. O. Thompson and D. E. Chimenti, Eds., (Plenum Press, New York, 1996), pp. 1509-1516.

8.  G. Simmons and H. Wang, *Single Crystal Elastic Constants and Calculated Aggregate Properties: A HANDBOOK*, $2^\text{nd}$ Edition, The M.I.T. Press, Cambridge, Massachusetts, 1971.