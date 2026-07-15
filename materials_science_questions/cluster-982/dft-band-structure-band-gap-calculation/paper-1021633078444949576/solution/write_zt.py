import json, sys

output_path = sys.argv[1]

data = {
  "gamma-Pb2SSe": {
    "n-type": {
      "300K": {
        "ZT": 0.29,
        "Seebeck_coeff_muV_K": 196.9,
        "electrical_cond_Ohm_m": 17612,
        "power_factor_W_mK2_e-3": 0.683,
        "electronic_thermal_cond_W_mK": 0.083,
        "lattice_thermal_cond_W_mK": 0.623,
        "carrier_concentration_cm2": 2.6e11
      },
      "800K": {
        "ZT": 1.24,
        "Seebeck_coeff_muV_K": 253.8,
        "electrical_cond_Ohm_m": 8322,
        "power_factor_W_mK2_e-3": 0.536,
        "electronic_thermal_cond_W_mK": 0.107,
        "lattice_thermal_cond_W_mK": 0.238,
        "carrier_concentration_cm2": 3.8e11
      }
    },
    "p-type": {
      "300K": {
        "ZT": 1.36,
        "Seebeck_coeff_muV_K": 247.1,
        "electrical_cond_Ohm_m": 63276,
        "power_factor_W_mK2_e-3": 3.863,
        "electronic_thermal_cond_W_mK": 0.232,
        "lattice_thermal_cond_W_mK": 0.623,
        "carrier_concentration_cm2": 3.6e12
      },
      "800K": {
        "ZT": 3.52,
        "Seebeck_coeff_muV_K": 297.2,
        "electrical_cond_Ohm_m": 19693,
        "power_factor_W_mK2_e-3": 1.739,
        "electronic_thermal_cond_W_mK": 0.157,
        "lattice_thermal_cond_W_mK": 0.238,
        "carrier_concentration_cm2": 3.4e12
      }
    }
  },
  "gamma-Pb2STe": {
    "n-type": {
      "300K": {
        "ZT": 1.04,
        "Seebeck_coeff_muV_K": 240.1,
        "electrical_cond_Ohm_m": 13015,
        "power_factor_W_mK2_e-3": 0.750,
        "electronic_thermal_cond_W_mK": 0.060,
        "lattice_thermal_cond_W_mK": 0.156,
        "carrier_concentration_cm2": 1.4e11
      },
      "800K": {
        "ZT": 2.76,
        "Seebeck_coeff_muV_K": 369.6,
        "electrical_cond_Ohm_m": 5446,
        "power_factor_W_mK2_e-3": 0.744,
        "electronic_thermal_cond_W_mK": 0.119,
        "lattice_thermal_cond_W_mK": 0.097,
        "carrier_concentration_cm2": 2.3e11
      }
    },
    "p-type": {
      "300K": {
        "ZT": 2.96,
        "Seebeck_coeff_muV_K": 289.9,
        "electrical_cond_Ohm_m": 31618,
        "power_factor_W_mK2_e-3": 2.657,
        "electronic_thermal_cond_W_mK": 0.114,
        "lattice_thermal_cond_W_mK": 0.156,
        "carrier_concentration_cm2": 1.8e12
      },
      "800K": {
        "ZT": 5.33,
        "Seebeck_coeff_muV_K": 339.9,
        "electrical_cond_Ohm_m": 10543,
        "power_factor_W_mK2_e-3": 1.218,
        "electronic_thermal_cond_W_mK": 0.086,
        "lattice_thermal_cond_W_mK": 0.097,
        "carrier_concentration_cm2": 2.7e12
      }
    }
  },
  "gamma-Pb2SeTe": {
    "n-type": {
      "300K": {
        "ZT": 1.05,
        "Seebeck_coeff_muV_K": 242.1,
        "electrical_cond_Ohm_m": 13351,
        "power_factor_W_mK2_e-3": 0.782,
        "electronic_thermal_cond_W_mK": 0.061,
        "lattice_thermal_cond_W_mK": 0.163,
        "carrier_concentration_cm2": 1.2e11
      },
      "800K": {
        "ZT": 2.85,
        "Seebeck_coeff_muV_K": 325.8,
        "electrical_cond_Ohm_m": 5399,
        "power_factor_W_mK2_e-3": 0.573,
        "electronic_thermal_cond_W_mK": 0.099,
        "lattice_thermal_cond_W_mK": 0.062,
        "carrier_concentration_cm2": 1.7e11
      }
    },
    "p-type": {
      "300K": {
        "ZT": 3.22,
        "Seebeck_coeff_muV_K": 301.6,
        "electrical_cond_Ohm_m": 32865,
        "power_factor_W_mK2_e-3": 2.989,
        "electronic_thermal_cond_W_mK": 0.116,
        "lattice_thermal_cond_W_mK": 0.163,
        "carrier_concentration_cm2": 1.5e12
      },
      "800K": {
        "ZT": 6.88,
        "Seebeck_coeff_muV_K": 357.3,
        "electrical_cond_Ohm_m": 9828,
        "power_factor_W_mK2_e-3": 1.255,
        "electronic_thermal_cond_W_mK": 0.084,
        "lattice_thermal_cond_W_mK": 0.062,
        "carrier_concentration_cm2": 1.4e12
      }
    }
  }
}

with open(output_path, 'w') as f:
    json.dump(data, f, indent=2)
