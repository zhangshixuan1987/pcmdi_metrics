# Usage

Adjust `ncpu` in `parallel_driver_cmip.py`

## CMIP5
python -u parallel_driver_cmip.py -p ../param/variability_across_timescales_PS_3hr_params_cmip5.py > ./log/log_parallel.wait_cmip5 &

## CMIP6
python -u parallel_driver_cmip.py -p ../param/variability_across_timescales_PS_3hr_params_cmip6.py  > ./log/log_parallel.wait_cmip6 &