#!/usr/bin/python3

import itertools
import pathlib
import sys

from debian_linux.config_v2 import Config


class Main(object):
    def __init__(self, dir, arch, featureset, flavour):
        self.args = dir, arch, featureset, flavour

        config_dirs = [
            pathlib.Path('debian/config'),
            pathlib.Path('debian/config.local'),
        ]
        top_config = Config.read_orig(config_dirs).merged
        arch_config = next(
            ac
            for ac in itertools.chain.from_iterable(
                kac.debianarchs for kac in top_config.kernelarchs)
            if ac.name == arch
        )
        fs_config = next(fsc for fsc in arch_config.featuresets
                         if fsc.name == featureset)
        self.config = next(fc for fc in fs_config.flavours
                           if fc.name == flavour)

    def __call__(self):
        fail = 0

        for c in ():
            fail |= c(self.config, *self.args)(sys.stdout)

        return fail


if __name__ == '__main__':
    sys.exit(Main(*sys.argv[1:])())
