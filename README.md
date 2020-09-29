# TurboCharge

A turbocharged way of installing all the packages you would ever want! Turbocharge automatically tests if the installed packages work are working correctly for you!

## Installation

Turbocharge can be installed using PyPI:
```
pip3 install turbocharge==3.0.6
```

Warning: The below line of code is deprecated, and is not recommended:
```
pip install turbocharge
```

Then, run this command:
```
echo "export PATH="/home/{username}/.local/bin:$PATH"" >> ~/.bashrc
```

## Documentation

Install a package with TurboCharge using

```
turbo install <package_name>
```

Install multiple packages with TurboCharge using
```
turbo install <package1,package2,package3>
```

Uninstall a package with TurboCharge using
```
turbo remove <package_name>
```

Uninstall multiple packages with TurboCharge using
```
turbo remove <package1,package2,package3>
```


Note: Make sure that there is no space between each of the package names after and before the ```,```.

List all installable packages with TurboCharge using
```
turbo list
```

List all installed packages with TurboCharge using
```
turbo local
```

Update an installed package with TurboCharge using
```
turbocharge update <package_name>
```

Search for a package avaliable in TurboCharge using:
```
turbocharge search <keyword>
```

Clean unnecesarry data from packages using TurboCharge with
```
turbo clean
```

Work in progress...
