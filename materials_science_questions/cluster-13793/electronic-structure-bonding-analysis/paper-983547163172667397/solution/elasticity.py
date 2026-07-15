#!/usr/bin/env python3
"""Voigt‑Reuss‑Hill mechanical properties for hexagonal crystals."""

import math


def voigt_reuss_hill(c11, c12, c13, c33, c44):
    """Return (B_H, G_H) in GPa from the five independent hexagonal elastic constants."""
    # Voigt bounds
    B_V = (2 * (c11 + c12) + c33 + 4 * c13) / 9.0
    G_V = (7 * c11 - 5 * c12 + 2 * c33 - 4 * c13 + 12 * c44) / 30.0

    # Reuss bounds
    numerator_B = (c11 + c12) * c33 - 2 * c13 * c13
    denom_B = c11 + c12 + 2 * c33 - 4 * c13
    B_R = numerator_B / denom_B if denom_B != 0 else 0.0

    denominator_G = 2 * (3 * B_V * c44 * (c11 - c12) +
                         numerator_B * (c11 - c12 + 2 * c44))
    G_R = 5 * numerator_B * (c11 - c12) * c44 / denominator_G if denominator_G != 0 else 0.0

    # Hill average
    B_H = 0.5 * (B_V + B_R)
    G_H = 0.5 * (G_V + G_R)
    return B_H, G_H


def compute_all(c11, c12, c13, c33, c44):
    """Compute isotropic mechanical properties and Vickers hardness."""
    B, G = voigt_reuss_hill(c11, c12, c13, c33, c44)
    # Young's modulus (GPa)
    E = 9 * B * G / (3 * B + G) if (3 * B + G) != 0 else 0.0
    # Poisson's ratio
    v = (3 * B - 2 * G) / (2 * (3 * B + G)) if (3 * B + G) != 0 else 0.0
    # Vickers hardness: Hv = 2 * ( (G/B)^2 * G )**0.585  -  3
    if B > 0:
        K2G = (G / B) ** 2 * G
        Hv = 2 * (K2G ** 0.585) - 3
    else:
        Hv = 0.0
    return {'B': B, 'G': G, 'E': E, 'v': v, 'Hv': Hv}
