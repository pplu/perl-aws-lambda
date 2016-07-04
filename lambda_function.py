from __future__ import print_function

import repr as reprlib
import json
import subprocess

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    proc = subprocess.Popen(['perl', '-I', 'lib', 'my_func.pl' ],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                            )
    stdout_value, stderr_value = proc.communicate(json.dumps(event))
    print('Output:'  + repr(stdout_value) + repr(stderr_value));
    return json.loads(stdout_value)
