from pybuild.Helper import Helper

class Targets(object):
    """description of class"""

    def get_supported_targets():
        """Get a list of Supported Targets from mbed"""

        # Run the mbed compile command against a dummy project that's setup to get a list of supported targets
        print("Running mbed config to pull supported platforms")
        cmd = Helper.run_cmd(['mbed', 'compile', '-S'],'./DummyProject')
        list1 = Targets.parse_compile_output(cmd.decoded_stdout)
        return list1

    def parse_compile_output(input):
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

    def get_unsupported_targets():
        """Get a list of Unsupported Targets from mbed"""

        print("Running make.py to pull all platforms")
        cmd = Helper.run_cmd(['C:\Python27\python.exe', 'make.py', '--help'],'./DummyProject/mbed-os/tools')
        unsupp_tgts = Targets.parse_make_output(cmd.decoded_stdout)
        supp_tgts = Targets.get_supported_targets()

        for item in supp_tgts:
            unsupp_tgts.remove(item)
        return unsupp_tgts

    def parse_make_output(input):
        """This returns all targets supported and unsupported"""
        arr1 = str(input).split('\n')
        arr2 = []
        capture = False
        for item in arr1:
            if str(item).startswith('  -m MCU, --mcu MCU') == True:
                capture = True
            if str(item).startswith('  -t TOOLCHAIN, --tool TOOLCHAIN') == True:
                capture = False
                break
            if capture == True:
                tmpstr = str(item)
                tmpstr = tmpstr.replace("  -m MCU, --mcu MCU     build for the given MCU (", "")
                tmpstr = tmpstr.replace(")", "")
                tmpstr = tmpstr.replace("\r", "").strip()
                arr2.append(tmpstr)

        arr3 = []
        for item in arr2:
            split1 = item.split(",")
            arr3 += split1
        arr4 = []
        for item in arr3:
            if item != "":
                arr4.append(item.strip())
        return arr4
