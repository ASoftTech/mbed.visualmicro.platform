#!/usr/bin/python3
"""Script for generating build.txt from mbed cli"""

from pybuild.Targets import Targets
from pybuild.Helper import Helper

# This script reads in the list of supported / unsupported platforms from the mbed cli tool and outputs a boards.txt file
# This is for use with Visual Micro.
# The genertic target doesn't specify a target board for situations where a custom target is in use
# Note that the executor module needs to be installed via pip for running external commands

class Builder(object):

    def main(self):

        # Run the mbed deploy command to pull down any needed libraries for the DummyProject
        print("Running mbed deploy to download libs")
        cmd = Helper.run_cmd(['mbed', 'deploy'],'./DummyProject')

        # Get a list of supported targets
        supp_tgts = Targets.get_supported_targets()
        supp_tgts.insert(0, "Mbed Generic")

        # Constuct boards.txt for supported platforms
        Helper.generate_boardstxt("supp", "../../Micro Platforms/mbed_os_52/hardware/arm-supported/boards.txt", supp_tgts)

        # Get a list of unsupported targets
        unsupp_tgts = Targets.get_unsupported_targets()
        unsupp_tgts.insert(0, "Mbed Generic")

        # Constuct boards.txt for supported platforms
        Helper.generate_boardstxt("unsupp", "../../Micro Platforms/mbed_os_52/hardware/arm-unsupported/boards.txt", unsupp_tgts)

        return
 

if __name__ == "__main__":
    Builder().main()
