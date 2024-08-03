"""

    Configuration file for the ChIMES potential energy surface generator (pes_generator.py)

	Don't forget to set PAIR CHEBYSHEV PENALTY SCALING to zero in the parameter file.

"""


CHMS_REPO  = "/Users/becky/Codes/chimes_calculator-myLLfork/"

PARAM_FILE = CHMS_REPO + "/serial_interface/tests/force_fields/published_params.Nitrogen-reshock.2+3+4b.Tersoff.txt"

PAIRTYPES  = [0] # Pair type index for scans, i.e. number after "PAIRTYPE PARAMS:" in parameter file
PAIRSTART  = [0.86] # Smallest distance for scan
PAIRSTOP   = [8.0] # Largest distance for scan
PAIRSTEP   = [0.1] # Step size for scan
