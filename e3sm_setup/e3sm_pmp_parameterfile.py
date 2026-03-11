import datetime
import json
import os
import sys

import cdutil

ver = datetime.datetime.now().strftime("v%Y%m%d")
# Set path to the required data (customized)
pcmdi_par_path = "/lcrc/group/acme/ac.szhang/acme_scratch/pcmdi_metrics/e3sm_setup"
pcmdi_data_path = "/lcrc/group/acme/ac.szhang/acme_scratch/data/pcmdi"
pcmdi_out_path = "/lcrc/group/acme/ac.szhang/acme_scratch/data/pcmdi"
pcmdi_clim_path = pcmdi_data_path + "/model/clim"
pcmdi_fixed_path = pcmdi_data_path + "/model/fixed"
pcmdi_month_path = pcmdi_data_path + "/mondel/monthly"

################################################################################
#  OPTIONS ARE SET BY USER IN THIS FILE AS INDICATED BELOW BY:
################################################################################
case_id = "v20240710"
mip = "cmip6"
exp = "amip"
mipvar = "rmt"
regional = "y"
user_notes = "Provenance and results"
realization = "all"
cmec = True
ext = ".nc"  # ".xml"
tableId = "atm"

# Observations to use at the moment
# "default" or "alternate"
reftag = "all"
refset = "default"

# SIMULATION PARAMETER
period = "198501-201412"
clim_ver = "v20240108"
gen_sftlf = False
save_clim = True

# SAVE INTERPOLATED MODEL CLIMATOLOGIES ?
save_test_clims = True  # True or False

# if variables in files are different from the vars[] indicated below
# you can set the varname_in_test_data
# varname_in_test_data

#################################################################

# LIST OF MODEL VERSIONS TO BE TESTED - WHICH ARE EXPECTED TO BE PART OF CLIMATOLOGY FILENAME
var_json = os.path.join(pcmdi_par_path, "all_mip_model_clim_info_PCMDI.json")
all_mods_dic = json.load(open(var_json))
if mipvar in all_mods_dic.keys():
    test_data_set = all_mods_dic[mipvar][mip][exp]
else:
    test_data_set = all_mods_dic["ts"][mip][exp]

test_data_set.sort()

print(len(test_data_set), " ", test_data_set)

print("----------------------------------------------------------------")

simulation_description_mapping = {
    "creation_date": "creation_date",
    "tracking_id": "tracking_id",
}

#####################
# WITHOUT PARALLELIZATION

"""
vars = ['pr','rltcre','rstcre','rt','rst','rlut','tauu','tauv']
vars = ['psl','tauu','tauv','tas','ta_850','ta_200','ua_850','ua_200','va_850','va_200','zg_500','pr','rltcre','rstcre','rt','rst','rlut']
vars = ['tas','rlut','pr','ta_850','ta_200','ua_850','ua_200','va_850','va_200','zg_500']
"""
if regional == "y":
    vars = [
        "tas",
        "ts",
        "psl",
        "tauu",
        "tauv",
        "evspsbl",
        "sfcWind",
        "ta850",
        "ta200",
        "ua850",
        "ua200",
        "va850",
        "va200",
        "zg500",
        "zg700",
        "wa500",
        "pr",
        "prw",
        "hfss",
        "hfls",
        "prsn",
        "rltcre",
        "rstcre",
        "rtmt",
        "rmt",
        "rlut",
        "rlutcs",
        "rlds",
        "rldscs",
        "rlus",
        "rsdt",
        "rsus",
        "rsuscs",
        "rsut",
        "rsutcs",
        "sic",
        "sos",
        "tos",
    ]

#####################
# WITH PARALLELIZATION

"""
vars = [['psl',],['pr',],['prw',],['tas',],['uas',],['vas',],['sfcWind',],['tauu'],['tauv']]
#vars = [['ta_850',],['ta_200',],['ua_850',],['ua_200',],['va_850',],['va_200',],['zg_500']]
vars = [['rlut',],['rsut',],['rsutcs',],['rlutcs',],['rsdt',],['rsus',],['rsds',],['rlds',],['rlus',],['rldscs',],['rsdscs']]
"""
# ALL BUT NOT tas ts psl sfcwind tauu tauv
if regional == "n":
    vars = [
        [
            "pr",
        ],
        [
            "prw",
        ],
        [
            "uas",
        ],
        [
            "vas",
        ],
        [
            "ta850",
        ],
        [
            "ta200",
        ],
        [
            "ua850",
        ],
        [
            "ua200",
        ],
        [
            "va850",
        ],
        [
            "va200",
        ],
        [
            "zg500",
        ],
        [
            "rlut",
        ],
        [
            "rsut",
        ],
        [
            "rsutcs",
        ],
        [
            "rlutcs",
        ],
        [
            "rsdt",
        ],
        [
            "rsus",
        ],
        [
            "rsds",
        ],
        [
            "rlds",
        ],
        [
            "rlus",
        ],
        [
            "rldscs",
        ],
        [
            "rsdscs",
        ],
        [
            "rltcre",
        ],
        [
            "rstcre",
        ],
        [
            "rtmt",
        ],
    ]

# vars = [['pr',],['rlut',],]
# vars = [['ts',],['psl',]]
# vars = ['ts']

# MODEL SPECIFC PARAMETERS
# model_tweaks = {
#    # Keys are model accronym or None which applies to all model entries
#    None: {
#        ## Variables name mapping
#        "variable_mapping": {"rlwcrf1": "rlutcre1"},
#    },
#    "GFDL-ESM2G": {
#        "variable_mapping": {"tos": "tos"},
#    },
# }

regions_specs = {
    "NH": {"domain": cdutil.region.domain(latitude=(0.0, 90))},
    "SH": {"domain": cdutil.region.domain(latitude=(-90.0, 0))},
    "NHEX": {"domain": cdutil.region.domain(latitude=(30.0, 90))},
    "SHEX": {"domain": cdutil.region.domain(latitude=(-90.0, -30))},
    "TROPICS": {"domain": cdutil.region.domain(latitude=(-30.0, 30))},
    "global": {},
    "90S50S": {"domain": cdutil.region.domain(latitude=(-90.0, -50))},
    "50S20S": {"domain": cdutil.region.domain(latitude=(-50.0, -20))},
    "20S20N": {"domain": cdutil.region.domain(latitude=(-20.0, 20))},
    "20N50N": {"domain": cdutil.region.domain(latitude=(20.0, 50))},
    "50N90N": {"domain": cdutil.region.domain(latitude=(50.0, 90))},
    "ocean_NH": {"value": 0.0, "domain": cdutil.region.domain(latitude=(0.0, 90))},
    "ocean_SH": {"value": 0.0, "domain": cdutil.region.domain(latitude=(-90.0, 0))},
    "land_NH": {"value": 100, "domain": cdutil.region.domain(latitude=(0.0, 90))},
    "land_SH": {"value": 100, "domain": cdutil.region.domain(latitude=(-90.0, 0))},
    "land_NHEX": {"value": 100, "domain": cdutil.region.domain(latitude=(30.0, 90))},
    "land_SHEX": {"value": 100, "domain": cdutil.region.domain(latitude=(-90.0, -30))},
    "land_TROPICS": {
        "value": 100,
        "domain": cdutil.region.domain(latitude=(-30.0, 30)),
    },
    "land": {
        "value": 100,
    },
    "ocean_NHEX": {"value": 0, "domain": cdutil.region.domain(latitude=(30.0, 90))},
    "ocean_SHEX": {"value": 0, "domain": cdutil.region.domain(latitude=(-90.0, -30))},
    "ocean_TROPICS": {"value": 0, "domain": cdutil.region.domain(latitude=(30.0, 30))},
    "ocean": {
        "value": 0,
    },
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
    "ocean_90S50S": {
        "value": 0.0,
        "domain": cdutil.region.domain(latitude=(-90.0, -50)),
    },
    # Modes of variability
    "NAM": {"domain": cdutil.region.domain(latitude=(20.0, 90), longitude=(-180, 180))},
    "NAO": {"domain": cdutil.region.domain(latitude=(20.0, 80), longitude=(-90, 40))},
    "SAM": {"domain": cdutil.region.domain(latitude=(-20.0, -90), longitude=(0, 360))},
    "PNA": {"domain": cdutil.region.domain(latitude=(20.0, 85), longitude=(120, 240))},
    "PDO": {"domain": cdutil.region.domain(latitude=(20.0, 70), longitude=(110, 260))},
    "AMO": {"domain": cdutil.region.domain(latitude=(0.0, 70), longitude=(-80, 0))},
    # Monsoon domains for Wang metrics
    # All monsoon domains
    "AllMW": {
        "domain": cdutil.region.domain(latitude=(-40.0, 45.0), longitude=(0.0, 360.0))
    },
    "AllM": {
        "domain": cdutil.region.domain(latitude=(-45.0, 45.0), longitude=(0.0, 360.0))
    },
    # North American Monsoon
    "NAMM": {
        "domain": cdutil.region.domain(latitude=(0.0, 45.0), longitude=(210.0, 310.0))
    },
    # South American Monsoon
    "SAMM": {
        "domain": cdutil.region.domain(latitude=(-45.0, 0.0), longitude=(240.0, 330.0))
    },
    # North African Monsoon
    "NAFM": {
        "domain": cdutil.region.domain(latitude=(0.0, 45.0), longitude=(310.0, 60.0))
    },
    # South African Monsoon
    "SAFM": {
        "domain": cdutil.region.domain(latitude=(-45.0, 0.0), longitude=(0.0, 90.0))
    },
    # Asian Summer Monsoon
    "ASM": {
        "domain": cdutil.region.domain(latitude=(0.0, 45.0), longitude=(60.0, 180.0))
    },
    # Australian Monsoon
    "AUSM": {
        "domain": cdutil.region.domain(latitude=(-45.0, 0.0), longitude=(90.0, 160.0))
    },
    # Monsoon domains for Sperber metrics
    # All India rainfall
    "AIR": {
        "domain": cdutil.region.domain(latitude=(7.0, 25.0), longitude=(65.0, 85.0))
    },
    # North Australian
    "AUS": {
        "domain": cdutil.region.domain(
            latitude=(-20.0, -10.0), longitude=(120.0, 150.0)
        )
    },
    # Sahel
    "Sahel": {
        "domain": cdutil.region.domain(latitude=(13.0, 18.0), longitude=(-10.0, 10.0))
    },
    # Gulf of Guinea
    "GoG": {
        "domain": cdutil.region.domain(latitude=(0.0, 5.0), longitude=(-10.0, 10.0))
    },
    # North American monsoon
    "NAmo": {
        "domain": cdutil.region.domain(
            latitude=(20.0, 37.0), longitude=(-112.0, -103.0)
        )
    },
    # South American monsoon
    "SAmo": {
        "domain": cdutil.region.domain(latitude=(-20.0, 2.5), longitude=(-65.0, -40.0))
    },
    "Nino34": {
        "value": 0.0,
        "domain": cdutil.region.domain(latitude=(-5.0, 5.0), longitude=(190.0, 240.0)),
    },
}

# USER CUSTOMIZED REGIONS
if regional == "y":
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

if regional == "n":
    default_regions = ["global", "NHEX", "SHEX", "TROPICS"]
    regions = {
        None: [
            None,
        ],
    }
    regions = {
        "rlut": [None, "global", "NHEX", "SHEX", "TROPICS"],
        "tas": [None, "global", "NHEX", "SHEX", "TROPICS"],
        "ts": [None, "global", "NHEX", "SHEX", "TROPICS"],
    }

## USER CAN CUSTOMIZE REGIONS VALUES NAMES
regions_values = {"land": 100.0, "ocean": 0.0}

# SAVE INTERPOLATED MODEL CLIMATOLOGIES ?
save_test_clims = save_clim  # True or False

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

# DATA LOCATION: MODELS, OBS AND METRICS OUTPUT
# ---------------------------------------------
# Templates for climatology files
verd = "*"
filename_template = (
    mip
    + "."
    + exp
    + ".%(model_version).%(realization)"
    + ".mon.%(variable)."
    + period
    + ".AC."
    + clim_ver
    + ".nc"
)

# Templates for MODEL land/sea mask (sftlf)
# filename template for landsea masks ('sftlf')
# sftlf_filename_template = "/work/gleckler1/processed_data/cmip5_fixed_fields/sftlf/sftlf_%(model_version).nc"
generate_sftlf = True  # ESTIMATE LAND SEA MASK IF NOT FOUND
sftlf_filename_template = "sftlf_%(model_version).nc"
if generate_sftlf:
    sftlf_filename_template = os.path.join(
        pcmdi_data_path,
        "model",
        "fixed",
        "sftlf",
        tableId,
        mip + "." + exp + ".%(model).fx.sftlf.nc",
    )

## ROOT PATH FOR MODELS CLIMATOLOGIES
test_data_path = os.path.join(
    pcmdi_data_path, "model", "clim", mip, exp, clim_ver, "%(variable)/"
)

# Observations to use at the moment "default" or "alternate"
ref = reftag
reference_data_set = [refset]  # ["default"]

## ROOT PATH FOR OBSERVATIONS
reference_data_path = os.path.join(pcmdi_data_path, "observations", "clim/")
observation_file = os.path.join(
    pcmdi_par_path, "obsinfo_PCMDI_clims_byVar_catalogue_v20240104.json"
)

custom_observations = os.path.abspath(observation_file)
print("CUSTOM OBS ARE ", custom_observations)
if not os.path.exists(custom_observations):
    sys.exit()

#######################################
metrics_output_path = os.path.join(
    pcmdi_out_path, "metrics_results", "mean_climate", mip, exp, "%(case_id)/"
)  # All SAME FILE
########################################
# DIRECTORY WHERE TO PUT INTERPOLATED MODELS' CLIMATOLOGIES
diagnostics_output_path = os.path.join(
    pcmdi_out_path,
    "diagnostic_results",
    "interpolated_model_clims",
    mip,
    exp,
    "%(case_id)/",
)

# if regional == "n":
#    num_workers = 20  # 17
#    granularize = ["vars"]
