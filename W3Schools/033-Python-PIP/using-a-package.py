# Using a Package

# Install camelcase package first!

# $ pip install camelcase
# Collecting camelcase
#   Downloading camelcase-0.2.tar.gz (1.3 kB)
# Building wheels for collected packages: camelcase
#   Building wheel for camelcase (setup.py) ... done
#   Created wheel for camelcase: filename=camelcase-0.2-py3-none-any.whl size=1789 sha256=179247f4f11dc65dd6b5c71cafe2a931d0bc1054c708b4e354b0400db2b5e754
#   Stored in directory: /home/dstevenson/.cache/pip/wheels/20/1a/a6/5651fe658d5ffd7fcf610723557f7b20a52a71d7e8e1849cb6
# Successfully built camelcase
# Installing collected packages: camelcase
# Successfully installed camelcase-0.2

# Once the package is installed, it is ready to use.

# Import the "camelcase" package into your project.

# Example
# Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))