#!/usr/bin/python3
"""Script for generating build.txt from mbed cli"""

from executor import ExternalCommand

# This script reads in the list of supported platforms from the mbed cli tool and outputs a boards.txt file
# This is for use with Visual Micro.
# The genertic target doesn't specify a target board for situations where a custom target is in use
# Note that the executor module needs to be installed via pip for running external commands

class Builder(object):

    def main(self):

        # Run the mbed deploy command to pull down any needed libraries for the DummyProject
        #print("Running mbed deploy to download libs")
        #cmd = self.run_cmd(['mbed', 'deploy'],'./DummyProject')

        # Run the mbed compile command against a dummy project that's setup to get a list of supported targets
        print("Running mbed config to pull supported platforms")
        cmd = self.run_cmd(['mbed', 'compile', '-S'],'./DummyProject')

        # Parse the output from the command
        list1 = self.get_targets(cmd.decoded_stdout)

        # Constuct boards.txt file in memory
        txt = '\n'
        txt += "# Used for custom targets\n"
        txt += "# where we need to set the target board as part of the local mbed config\n"
        txt += "mbed_os_generic.name=Mbed Generic\n"
        txt += "mbed_os_generic.mcu=\n\n"
        
        for item in list1:
            boardname = "mbed_os_" + item.lower()
            txt += boardname + "." + "name=" + item + "\n"
            txt += boardname + "." + "mcu=-m " + item + "\n\n"

        with open("boards.txt", 'w') as f:
            f.write(txt)
        return


    def get_targets(self, input):
        arr1 = str(input).split('\n')
        arr2 = []
        for item in arr1:
            if str(item).startswith('|') == True:
                if str(item).startswith('| Target') == False:
                    arr2.append(item)
        arr3 = []
        for item in arr2:
            split_items = str(item).split('|')
            target = str(split_items[1]).strip()
            arr3.append(target)
        return arr3


    def run_cmd(self, cmdarray, workdir, comms = None):
        """Run a command on the shell"""      
        cmd = ExternalCommand(*cmdarray, capture=True, capture_stderr=True, async=True, shell=False, directory=workdir)
        cmd.start()
        last_out = ''
        last_err = ''
        while cmd.is_running:
            new_out = cmd.decoded_stdout.replace(last_out, '')
            new_err = cmd.decoded_stderr.replace(last_err, '')
            last_out += new_out
            last_err += new_err
            new_out = new_out.replace(u"\u2018", "'").replace(u"\u2019", "'")
            new_err = new_err.replace(u"\u2018", "'").replace(u"\u2019", "'")
            if new_out != '': print(new_out, end='')
            if new_err != '': print(new_err, end='')

        if cmd.returncode != 0:
            raise RuntimeError('Failure to run command')
        return cmd

if __name__ == "__main__":
    Builder().main()
