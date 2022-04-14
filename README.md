# Annealing helpers

Fast compiled (and tiny) module to calculate the equivalent annealing time at a target temperature from an annealing time at a reference temperature.
The parametrisation is based on http://mmoll.web.cern.ch/mmoll/thesis/ .

Setup
=================
```
pip3 install git+https://github.com/jkiesele/annealing_helpers
```
(requires cmake)

Usage
================

```
from annealing_helpers import equiv_annealing_time
# all temperatures in degree Celsius
time_at_target_temperature = equiv_annealing_time(reference_temperature, reference_time, target_temperature, relative_precision = 1e-06)
```
