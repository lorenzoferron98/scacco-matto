#!/usr/bin/env python3
import sys
from plistlib import FMT_XML, load


def main(argv, argc):
    if argc != 4:
        print("Usage: " + argv[0] + " <manifest> <BDID> <CPID>", file=sys.stderr)
        sys.exit(-1)
    filename = argv[1]
    with open(filename, 'rb') as fp:
        pl = load(fp, fmt=FMT_XML)
    root = pl["BuildIdentities"]
    filtered = [item for item in root
                if int(item["ApBoardID"], 16) == int(argv[2], 16) and int(item["ApChipID"], 16) == int(argv[3], 16) and
                item["Info"]["Variant"] == "Customer Erase Install (IPSW)"][0]
    print("iBSS:                  " + filtered["Manifest"]["iBSS"]["Info"]["Path"])
    print("iBEC:                  " + filtered["Manifest"]["iBEC"]["Info"]["Path"])
    print("iBoot:                 " + filtered["Manifest"]["iBoot"]["Info"]["Path"])
    print("KernelCache:           " + filtered["Manifest"]["KernelCache"]["Info"]["Path"])
    print("LLB:                   " + filtered["Manifest"]["LLB"]["Info"]["Path"])
    print("RestoreRamDisk:        " + filtered["Manifest"]["RestoreRamDisk"]["Info"]["Path"])
    print("Root Filesystem (OS):  " + filtered["Manifest"]["OS"]["Info"]["Path"])
    # https://discord.com/channels/779134930265309195/779156258799878195/1075131502398025770
    print("Touch firmware:        " + filtered["Manifest"]["Multitouch"]["Info"]["Path"])
    print("SEP firmware:          " + filtered["Manifest"]["SEP"]["Info"]["Path"])
    print("Device tree:           " + filtered["Manifest"]["DeviceTree"]["Info"]["Path"])
    print("Apple logo:            " + filtered["Manifest"]["AppleLogo"]["Info"]["Path"])
    print("Static trust cache:    " + filtered["Manifest"]["StaticTrustCache"]["Info"]["Path"])
    print("Hash of the root node: " + filtered["Manifest"]["SystemVolume"]["Info"]["Path"])


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
