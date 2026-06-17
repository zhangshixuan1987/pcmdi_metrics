import json
import os
import sys

MIP = "cmip6"
exp = "amip"
tableId = "atm"
mipvar = "rmt"
regional = "y"
user_notes = "Provenance and results"
realization = "all"
cmec = True
ext = ".nc"

period = "198501-201412"
clim_version = "v20240701"
realization = "all"

# Set path to the required data (customized)
para_reg_file = "custom_reference_data.json"
para_mod_file = (
    "modinfo_PCMDI-" + MIP + "_clims_byVar_catalogue_" + clim_version + ".json"
)
para_obs_file = "obsinfo_PCMDI_clims_byVar_catalogue_" + clim_version + ".json"
para_file_path = "/lcrc/group/acme/ac.szhang/acme_scratch/pcmdi_metrics/e3sm_setup"
clim_data_path = "/lcrc/group/acme/ac.szhang/acme_scratch/data/pcmdi"
output_path = "/lcrc/group/acme/ac.szhang/acme_scratch/data/pcmdi"
gen_sftlf = False

user_notes = "Provenance and results"
case_id = "v20240810"
# case_id = datetime.datetime.now().strftime("v%Y%m%d")

################################################################################
#  OPTIONS ARE SET BY USER IN THIS FILE AS INDICATED BELOW BY:
################################################################################
cmec = True
ext = ".nc"  # ".xml"

# SIMULATION PARAMETER
save_clim = True

# SAVE INTERPOLATED MODEL CLIMATOLOGIES ?
save_test_clims = True  # True or False

# if variables in files are different from the vars[] indicated below
# you can set the varname_in_test_data
# varname_in_test_data

#################################################################

# LIST OF MODEL VERSIONS TO BE TESTED - WHICH ARE EXPECTED TO BE PART OF CLIMATOLOGY FILENAME
all_mods_dic = json.load(open(os.path.join(para_file_path, para_mod_file)))
if mipvar in all_mods_dic.keys():
    test_data_set = all_mods_dic[mipvar][MIP][exp]
else:
    test_data_set = all_mods_dic["ts"][MIP][exp]

test_data_set.sort()

print(len(test_data_set), " ", test_data_set)

print("----------------------------------------------------------------")

simulation_description_mapping = {
    "creation_date": "creation_date",
    "tracking_id": "tracking_id",
}

regions_specs = json.load(open(os.path.join(para_file_path, para_reg_file)))
default_regions = ["global", "land", "ocean", "SH", "NH", "NHEX", "SHEX", "TROPICS"]
regions = {
    None: [
        None,
    ],
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
## ROOT PATH FOR MODELS CLIMATOLOGIES
test_data_path = os.path.join(
    clim_data_path, "model", "clim", MIP, exp, clim_version, "%(variable)/"
)
# Templates for climatology files
filename_template = (
    MIP
    + "."
    + exp
    + ".%(model_version).%(realization)"
    + ".mon.%(variable)."
    + period
    + ".AC."
    + clim_version
    + ".nc"
)

# Templates for MODEL land/sea mask (sftlf)
# filename template for landsea masks ('sftlf')
# sftlf_filename_template = "/work/gleckler1/processed_data/cmip5_fixed_fields/sftlf/sftlf_%(model_version).nc"
generate_sftlf = gen_sftlf  # ESTIMATE LAND SEA MASK IF NOT FOUND
sftlf_filename_template = "sftlf_%(model_version).nc"
if not generate_sftlf:
    sftlf_filename_template = os.path.join(
        clim_data_path,
        "model",
        "fixed",
        "sftlf",
        tableId,
        MIP + "." + exp + ".%(model).fx.sftlf.nc",
    )

# Observations to use at the moment "default" or "alternate"
reference_data_set = ["default"]  # or "all" or "alternate"
## ROOT PATH FOR OBSERVATIONS
reference_data_path = os.path.join(clim_data_path, "observations", "clim/")
observation_file = os.path.join(para_file_path, para_obs_file)

custom_observations = os.path.abspath(observation_file)
print("CUSTOM OBS ARE ", custom_observations)
if not os.path.exists(custom_observations):
    sys.exit()

#######################################
metrics_output_path = os.path.join(
    output_path, "metrics_results", "mean_climate", MIP, exp, "%(case_id)/"
)  # All SAME FILE
########################################
# DIRECTORY WHERE TO PUT INTERPOLATED MODELS' CLIMATOLOGIES
diagnostics_output_path = os.path.join(
    output_path,
    "diagnostic_results",
    "interpolated_model_clims",
    MIP,
    exp,
    "%(case_id)/",
)

# if regional == "n":
#    num_workers = 20  # 17
#    granularize = ["vars"]
