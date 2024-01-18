#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp

from config import (
    DOSAGE_RECORD_PATH,
    DELAYS_FILE_PATH,
    DOSES_RECORD_PATH
)

# -->> Tunables <<---------------------


# -->> Definitions <<------------------


# -->> API <<--------------------------

def open_record(): 
    """Open dosage record."""
    sp.run(["code", "-n", DOSAGE_RECORD_PATH], shell=False)

def apply_record(
        delay: float,
) -> None:
    #Add new dosage: 
    with open(DOSES_RECORD_PATH, "at+") as doses: 
        # This record a 1 for the doses file. 
        # Adds a new line, in the normal way; or add the value at the end of the line. 
        # The same applies for delays file, but in this case using the delay parameter of the func. 
            # Here the plan is to pipeline with time_tools.py:parse_input_time():delay
        print(doses)
        a = doses.write('s')
        print(a)

    # Then the idea is that, or bash read and strips the new lines, or just read the complete line" 
    # And those files, (delay and doses) if works with "newline" more easy to do upgrade to .csv file and pandas
        
# -->> Execute <<----------------------


# -->> Export <<-----------------------

if __name__ == "__main__": 
    apply_record(0)
    