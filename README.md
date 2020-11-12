

# TurboCharge

Official Website : www.turbocharge.dev

A turbocharged way of installing all the packages you would ever want! Turbocharge automatically tests if the installed packages are working correctly for you on MacOS, Linux And Windows!

### Avaliability

TurboCharge currently supports Windows, MacOS And Debian-Based Operating Systems. 
It uses a backend of apt, snap, brew and chocolatey, giving you a seamless and enjoyable experience!

## Installation

Turbocharge can be installed using PyPI:

```
pip3 install turbocharge
```

Warning: The below line of code is deprecated, and is not recommended:

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

Note: Make sure that there is no space between each of the package names after and before the `,`.

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
turbo update <package_name>
```

Search for a package avaliable in TurboCharge using:

```
turbo search <keyword>
```

Clean unnecesarry data from packages using TurboCharge with

```
turbo clean
```

Get the current version of TurboCharge with

```
turbo --version
```
