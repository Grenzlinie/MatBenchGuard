#!/usr/bin/env python3
import json

data = {
    "si_a_dB2D_star_da": -6.3,
    "hsi_a_dB2D_star_da": -13.3,
    "ge_a_dB2D_star_da": -18.6,
    "hge_a_dB2D_star_da": -13.8
}

with open("/app/outputs/anharmonicity.json", "w") as f:
    json.dump(data, f, indent=2)
