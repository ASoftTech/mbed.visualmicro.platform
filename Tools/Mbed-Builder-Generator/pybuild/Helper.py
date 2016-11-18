from executor import ExternalCommand

class Helper(object):
    """Helper Functions"""

    def generate_boardstxt(platform, filepath, listitems):
        """Generate boards.txt file"""
        txt = ""
        for item in listitems:
            if item == "Mbed Generic":
                boardname = "mbed_os_" + platform + "_generic"
                txt += "# Used for custom targets\n"
                txt += "# where we need to set the target board as part of the local mbed config\n"
                txt += boardname + ".name=" + item + "\n"
                txt += boardname + ".build.mcu=\n"
            else:
                boardname = "mbed_os_" + platform + "_" + item.lower()
                txt += boardname + ".name=" + item + "\n"
                txt += boardname + ".build.mcu=-m " + item + "\n"
            txt += boardname + ".upload.tool=openocd\n"
            txt += boardname + ".debug.tool=gdb\n"
            txt += "\n"

        with open(filepath, 'w') as f:
            f.write(txt)
        return


    def run_cmd(cmdarray, workdir, comms = None):
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
