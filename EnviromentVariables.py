#!/usr/bin/env python3.7

import os

stage = os.getenv["STAGE", default="dev"].upper()

output = f"We're running in {stage}"

if stage.startwith("PROD"):
    output = "DANGER!!!  - " + output

print(output)