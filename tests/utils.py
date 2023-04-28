import os
import platform
import resource
import subprocess
import time

import pytest
from io import StringIO

# some of the instances will need us to be able to return the stdout
# and/or stderr objects, so that they can be used in code later
# additionally, some of the checks for stdout and stderr are non-standard, so
# it would probably be easier to just return the objects

# 2 methods: both check the passed in expected values, but one returns the
# objects in a tuple

def inner_check(rc, stdout, stderr, expected_rc, expected_stdout, expected_stderr) -> bool:
    result = True
    if (expected_rc != None):
        result = result and (rc == expected_rc)

    if (expected_stdout != None):
        result = result and (stdout.read() == expected_stdout)
    
    if (expected_stderr != None):
        result = result and (stderr.read() == expected_stderr)

    return result

# Execute command on guest and compare output with some expected values.
def check_command(ssh, command, expected_rc=None, expected_stderr=None,
                  expected_stdout=None) -> bool:
    
    rc, stdout, stderr = ssh.execute_command(command)

    return inner_check(rc, stdout, stderr, expected_rc, expected_stdout, expected_stderr)

def check_command_with_return(ssh, command, expected_rc=None,
                              expected_stderr=None, expected_stdout=None
                              ) -> tuple[bool, int, StringIO, StringIO]:
    
    rc, stdout, stderr = ssh.execute_command(command)
    result = inner_check(rc, stdout, stderr, expected_rc, expected_stdout, expected_stderr)

    return result, rc, stdout, stderr
