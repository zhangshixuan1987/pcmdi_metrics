import os

import cdutil

################################################################################
#  OPTIONS ARE SET BY USER IN THIS FILE AS INDICATED BELOW BY:
################################################################################

generate_sftlf = True

regional = "n"

custom_regional = "y"

case_id = "v20240810"

MIP = "cmip6"
exp = "amip"

# Set path to the required data (customized)
para_path = "/lcrc/group/acme/ac.szhang/acme_scratch/pcmdi_metrics/e3sm_setup"
output_path = "/lcrc/group/acme/ac.szhang/acme_scratch/data/pcmdi"
para_region_file = "/lcrc/group/acme/ac.szhang/acme_scratch/pcmdi_metrics/e3sm_setup/custom_region_definition.json"

debug = False
cmec = True
ext = ".nc"  # ".xml"

user_notes = "Provenance and results"

metrics_in_single_file = "n"  #  'y' or 'n'

# SAVE INTERPOLATED MODEL CLIMATOLOGIES ?
save_test_clims = True

# if variables in files are different from the vars[] indicated below
# you can set the varname_in_test_data
# varname_in_test_data
#################################################################
simulation_description_mapping = {
    "creation_date": "creation_date",
    "tracking_id": "tracking_id",
}

# define regions
# regions_specs = json.load(open(para_region_file))
if regional == "y":
    regions_specs = {
        "Nino34": {
            "value": 0.0,
            "domain": cdutil.region.domain(
                latitude=(-5.0, 5.0), longitude=(190.0, 240.0)
            ),
        },
        "ocean": {"value": 0.0, "domain": cdutil.region.domain(latitude=(-90.0, 90))},
        "land": {"value": 100.0, "domain": cdutil.region.domain(latitude=(-90.0, 90))},
        "ocean_50S50N": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(-50.0, 50)),
        },
        "ocean_50S20S": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(-50.0, -20)),
        },
        "ocean_20S20N": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(-20.0, 20)),
        },
        "ocean_20N50N": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(20.0, 50)),
        },
        "ocean_50N90N": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(50.0, 90)),
        },
        "90S50S": {
            "value": None,
            "domain": cdutil.region.domain(latitude=(-90.0, -50)),
        },
        "50S20S": {
            "value": None,
            "domain": cdutil.region.domain(latitude=(-50.0, -20)),
        },
        "20S20N": {"value": None, "domain": cdutil.region.domain(latitude=(-20.0, 20))},
        "20N50N": {"value": None, "domain": cdutil.region.domain(latitude=(20.0, 50))},
        "50N90N": {"value": None, "domain": cdutil.region.domain(latitude=(50.0, 90))},
        "NH": {"value": None, "domain": cdutil.region.domain(latitude=(0.0, 90))},
        "SH": {"value": None, "domain": cdutil.region.domain(latitude=(-90.0, 0))},
        "NHEX_ocean": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(0.0, 90)),
        },
        "SHEX_ocean": {
            "value": 0.0,
            "domain": cdutil.region.domain(latitude=(-90.0, 0)),
        },
        "NHEX_land": {
            "value": 100.0,
            "domain": cdutil.region.domain(latitude=(20.0, 90)),
        },
        "SHEX_land": {
            "value": 100.0,
            "domain": cdutil.region.domain(latitude=(-90.0, -20.0)),
        },
    }
    #       'GLOBAL' : {"value":0.,'domain':cdutil.region.domain(latitude=(-90.,90.))},
    regions = {
        "tas": [None, "land", "ocean", "ocean_50S50N", "NHEX_land", "SHEX_land"],
        "tauu": [None, "ocean_50S50N"],
        "tauv": [None, "ocean_50S50N"],
        "psl": [None, "ocean", "ocean_50S50N", "NHEX_ocean", "SHEX_ocean"],
        "sfcWind": [None, "ocean", "ocean_50S50N", "NHEX_ocean", "SHEX_ocean"],
        "ts": [None, "ocean", "ocean_50S50N", "NHEX_ocean", "SHEX_ocean"],
        "tos": [None],
    }

# USER CUSTOMIZED REGIONS
if regional == "n":
    regions_specs = {
        "global": {},
        "NH": {"domain": {"latitude": (0.0, 90.0)}},
        "SH": {"domain": {"latitude": (-90.0, 0.0)}},
        "NHEX": {"domain": {"latitude": (30.0, 90.0)}},
        "SHEX": {"domain": {"latitude": (-90.0, -30.0)}},
        "TROPICS": {"domain": {"latitude": (-30.0, 30.0)}},
        "90S50S": {"domain": {"latitude": (-90.0, -50.0)}},
        "50S20S": {"domain": {"latitude": (-50.0, -20.0)}},
        "20S20N": {"domain": {"latitude": (-20.0, 20.0)}},
        "20N50N": {"domain": {"latitude": (20.0, 50.0)}},
        "50N90N": {"domain": {"latitude": (50.0, 90.0)}},
        "ocean_NH": {"value": 0.0, "domain": {"latitude": (0.0, 90.0)}},
        "ocean_SH": {"value": 0.0, "domain": {"latitude": (-90.0, 0.0)}},
        "land_NH": {"value": 100, "domain": {"latitude": (0.0, 90.0)}},
        "land_SH": {"value": 100, "domain": {"latitude": (-90.0, 0)}},
        "land_NHEX": {"value": 100, "domain": {"latitude": (30.0, 90.0)}},
        "land_SHEX": {"value": 100, "domain": {"latitude": (-90.0, -30.0)}},
        "land_TROPICS": {"value": 100, "domain": {"latitude": (-30.0, 30.0)}},
        "land": {"value": 100},
        "ocean": {"value": 0},
        "ocean_NHEX": {"value": 0, "domain": {"latitude": (30.0, 90.0)}},
        "ocean_SHEX": {"value": 0, "domain": {"latitude": (-90.0, -30.0)}},
        "ocean_TROPICS": {"value": 0, "domain": {"latitude": (-30.0, 30.0)}},
        "ocean_50S50N": {"value": 0.0, "domain": {"latitude": (-50.0, 50.0)}},
        "ocean_50S20S": {"value": 0.0, "domain": {"latitude": (-50.0, -20.0)}},
        "ocean_20S20N": {"value": 0.0, "domain": {"latitude": (-20.0, 20.0)}},
        "ocean_20N50N": {"value": 0.0, "domain": {"latitude": (20.0, 50.0)}},
        "ocean_50N90N": {"value": 0.0, "domain": {"latitude": (50.0, 90.0)}},
        "ocean_90S50S": {"value": 0.0, "domain": {"latitude": (-90.0, -50.0)}},
        # Modes of variability
        "NAM": {"domain": {"latitude": (20.0, 90.0), "longitude": (-180.0, 180.0)}},
        "NAO": {"domain": {"latitude": (20.0, 80.0), "longitude": (-90.0, 40.0)}},
        "SAM": {"domain": {"latitude": (-20.0, -90.0), "longitude": (0.0, 360.0)}},
        "PNA": {"domain": {"latitude": (20.0, 85.0), "longitude": (120.0, 240.0)}},
        "PDO": {"domain": {"latitude": (20.0, 70.0), "longitude": (110.0, 260.0)}},
        "AMO": {"domain": {"latitude": (0.0, 70.0), "longitude": (-80.0, 0.0)}},
        # Monsoon domains for Wang metrics
        # All monsoon domains
        "AllMW": {"domain": {"latitude": (-40.0, 45.0), "longitude": (0.0, 360.0)}},
        "AllM": {"domain": {"latitude": (-45.0, 45.0), "longitude": (0.0, 360.0)}},
        # North American Monsoon
        "NAMM": {"domain": {"latitude": (0.0, 45.0), "longitude": (210.0, 310.0)}},
        # South American Monsoon
        "SAMM": {"domain": {"latitude": (-45.0, 0.0), "longitude": (240.0, 330.0)}},
        # North African Monsoon
        "NAFM": {"domain": {"latitude": (0.0, 45.0), "longitude": (310.0, 60.0)}},
        # South African Monsoon
        "SAFM": {"domain": {"latitude": (-45.0, 0.0), "longitude": (0.0, 90.0)}},
        # Asian Summer Monsoon
        "ASM": {"domain": {"latitude": (0.0, 45.0), "longitude": (60.0, 180.0)}},
        # Australian Monsoon
        "AUSM": {"domain": {"latitude": (-45.0, 0.0), "longitude": (90.0, 160.0)}},
        # Monsoon domains for Sperber metrics
        # All India rainfall
        "AIR": {"domain": {"latitude": (7.0, 25.0), "longitude": (65.0, 85.0)}},
        # North Australian
        "AUS": {"domain": {"latitude": (-20.0, -10.0), "longitude": (120.0, 150.0)}},
        # Sahel
        "Sahel": {"domain": {"latitude": (13.0, 18.0), "longitude": (-10.0, 10.0)}},
        # Gulf of Guinea
        "GoG": {"domain": {"latitude": (0.0, 5.0), "longitude": (-10.0, 10.0)}},
        # North American monsoon
        "NAmo": {"domain": {"latitude": (20.0, 37.0), "longitude": (-112.0, -103.0)}},
        # South American monsoon
        "SAmo": {"domain": {"latitude": (-20.0, 2.5), "longitude": (-65.0, -40.0)}},
        "Nino34": {
            "value": 0.0,
            "domain": {"latitude": (-5.0, 5.0), "longitude": (190.0, 240.0)},
        },
    }

    default_regions = ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"]
    regions = {
        None: [
            None,
        ],
    }
    if custom_regional == "y":
        regions = {
            "rltcre": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rstcre": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rlut": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rlutcs": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsdt": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rtmt": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rmt": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rlds": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rldscs": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rlus": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsds": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsdscs": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsus": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsuscs": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsut": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "rsutcs": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "hfls": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "hfss": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ua": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ta": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "pr": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "prsn": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "prw": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ts": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "tas": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "tauu": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "tauv": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "psl": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "sfcWind": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "evspsbl": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ta200": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ta850": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ua200": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "ua850": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "va200": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "va850": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "zg500": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "zg700": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "wa500": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "clivi": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "clwvi": [
                "global",
                "land",
                "ocean",
                "ocean_20S20N",
                "20S20N",
                "NH",
                "SH",
                "ocean_SH",
                "land_SH",
                "90S50S",
                "50S20S",
            ],
            "tos": [
                "ocean",
                "ocean_20S20N",
                "ocean_NH",
                "ocean_SH",
                "ocean_90S50S",
                "ocean_50S20S",
            ],
            "sic": [
                "ocean",
                "ocean_20S20N",
                "ocean_NH",
                "ocean_SH",
                "ocean_90S50S",
                "ocean_50S20S",
            ],
            "sos": [
                "ocean",
                "ocean_20S20N",
                "ocean_NH",
                "ocean_SH",
                "ocean_90S50S",
                "ocean_50S20S",
            ],
        }

    if custom_regional == "n":
        regions = {
            "rlut": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rlutcs": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsds": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rlds": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rldscs": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsdt": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsus": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsuscs": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsut": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rsutcs": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rtmt": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rmt": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rltcre": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "rstcre": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "hfls": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "hfss": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "tauu": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "tauv": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "evspsbl": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "sfcWind": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "psl": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "tas": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "uas": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "vas": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "ts": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "pr": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "prsn": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "prw": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "ua850": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "ua200": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "va850": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "va200": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "ta200": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "ta850": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "zg500": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "sos": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "tos": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "amoc": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
            "sic": ["global", "land", "NH", "SH", "NHEX", "SHEX", "TROPICS"],
        }

## USER CAN CUSTOMIZE REGIONS VALUES NAMES
regions_values = {"land": 100.0, "ocean": 0.0}

# INTERPOLATION OPTIONS
target_grid = "2.5x2.5"  # OPTIONS: '2.5x2.5' or an actual cdms2 grid object
targetGrid = target_grid
target_grid_string = "2p5x2p5"
regrid_tool = "esmf"  # "regrid2"  #'esmf' #'regrid2' # OPTIONS: 'regrid2','esmf'
regrid_method = "regrid2"  #'conservative'  #'linear'  # OPTIONS: 'linear','conservative', only if tool is esmf
regrid_tool_ocn = "esmf"  # OPTIONS: "regrid2","esmf"
regrid_method_ocn = (
    "conservative"  # OPTIONS: 'linear','conservative', only if tool is esmf
)

#######################################
metrics_output_path = os.path.join(
    output_path, "metrics_results", "mean_climate", MIP, exp, "%(case_id)/"
)  # All SAME FILE

########################################
# DIRECTORY WHERE TO PUT INTERPOLATED MODELS' CLIMATOLOGIES
diagnostics_output_path = os.path.join(
    output_path, "diagnostic_results", "mean_climate", MIP, exp, "%(case_id)/"
)

test_clims_interpolated_output = diagnostics_output_path

# if regional == "n":
#    num_workers = 20  # 17
#    granularize = ["vars"]
