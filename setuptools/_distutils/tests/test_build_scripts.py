"""Tests for distutils.command.build_scripts."""

import os

from distutils.command.build_scripts import build_scripts
from distutils.core import Distribution
from distutils import sysconfig

from distutils.tests import support


class TestBuildScripts(support.TempdirManager):
    def test_default_settings(self):
        cmd = self.get_build_scripts_cmd("/foo/bar", [])
        assert not cmd.force
        assert cmd.build_dir is None

        cmd.finalize_options()

        assert cmd.force
        assert cmd.build_dir == "/foo/bar"

    def test_build(self):
        source = self.mkdtemp()
        target = self.mkdtemp()
        expected = self.write_sample_scripts(source)

        cmd = self.get_build_scripts_cmd(
            target, [os.path.join(source, fn) for fn in expected]
        )
        cmd.finalize_options()
        cmd.run()

        built = os.listdir(target)
        for name in expected:
            assert name in built

    def get_build_scripts_cmd(self, target, scripts):
        import sys

        dist = Distribution()
        dist.scripts = scripts
        dist.command_obj["build"] = support.DummyCommand(
            build_scripts=target, force=1, executable=sys.executable
        )
        return build_scripts(dist)

    def write_sample_scripts(self, dir):
        self.write_script(
            dir,
            "script1.py",
            (
                "#! /usr/bin/env python2.3\n"
                "# bogus script w/ Python sh-bang\n"
                "pass\n"
            ),
        )
        self.write_script(
            dir,
            "script2.py",
            ("#!/usr/bin/python\n" "# bogus script w/ Python sh-bang\n" "pass\n"),
        )
        self.write_script(
            dir,
            "shell.sh",
            ("#!/bin/sh\n" "# bogus shell script w/ sh-bang\n" "exit 0\n"),
        )
        return ["script1.py", "script2.py", "shell.sh"]

    def write_script(self, dir, name, text):
        f = open(os.path.join(dir, name), "w")
        try:
            f.write(text)
        finally:
            f.close()

    def test_version_int(self):
        source = self.mkdtemp()
        target = self.mkdtemp()
        expected = self.write_sample_scripts(source)

        cmd = self.get_build_scripts_cmd(
            target, [os.path.join(source, fn) for fn in expected]
        )
        cmd.finalize_options()

        # http://bugs.python.org/issue4524
        #
        # On linux-g++-32 with command line `./configure --enable-ipv6
        # --with-suffix=3`, python is compiled okay but the build scripts
        # failed when writing the name of the executable
        old = sysconfig.get_config_vars().get('VERSION')
        sysconfig._config_vars['VERSION'] = 4
        try:
            cmd.run()
        finally:
            if old is not None:
                sysconfig._config_vars['VERSION'] = old

        built = os.listdir(target)
        for name in expected:
            assert name in built
