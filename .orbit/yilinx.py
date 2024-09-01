import sys, os

# Handle command-line arguments
PROG_SRAM = bool(sys.argv.count('--sram') > 0)
PROG_FLASH = bool(sys.argv.count('--flash') > 0)

# Get environment variables set by orbit for this particular build
BLUEPRINT = os.environ.get("ORBIT_BLUEPRINT")
OUTPUT_PATH = os.environ.get("ORBIT_OUT_DIR")
TOP_LEVEL = os.environ.get("ORBIT_TOP_NAME")

synth_order = []
constraints_file = None

# Parse the blueprint file created by orbit
with open(BLUEPRINT) as blueprint:
    rules = blueprint.readlines()
    for r in rules:
        fileset, lib, path = r.strip().split('\t')
        if fileset == 'VHDL':
            synth_order += [(lib, path)]
        if fileset == 'PINOUT':
            constraints_file = path
    pass

# Run the Yilinx tool from synthesis to bistream generation
for (lib, path) in synth_order:
    print('YILINX:', 'synthesizing file ' + str(path) + ' into ' + str(lib) + '...')

print('YILINX:','performing place-and-route...')

# Read the Yilinx design constraints file to map pins to I/O top-level ports.
if constraints_file != None:
    with open(constraints_file, 'r') as ydc:
        mapping = [x.strip().split('=') for x in ydc.readlines()]
    for pin, port in mapping:
        print('YILINX:', 'mapping pin ' + str(pin) + ' to port ' + str(port) + '...')
    pass

print('YILINX:', 'generating bitstream...')

BIT_FILE = TOP_LEVEL + '.bit'
with open(BIT_FILE, 'w') as bitstream:
    for byte in [bin(b)[2:] for b in bytes(TOP_LEVEL, 'utf-8')]:
        bitstream.write(byte)

print('YILINX:','bitstream saved at: '+ str(OUTPUT_PATH + '/' + BIT_FILE))

# Optionally allow the user to program the FPGA using flash or SRAM configuration
if PROG_FLASH == True and PROG_SRAM == False:
    print('YILINX:', 'programming bitstream to flash...')
elif PROG_SRAM == True:
    print('YILINX:', 'programming bitstream to SRAM...')