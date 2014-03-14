SublimeLinter-contrib-tlec
================================

Live TLE syntax check for your mounted linux-based virtual machine running epages6, hosted on a Mac OS X.

## Installation
SublimeLinter 3 must be installed in order to use this plugin.

### Linter installation
Before using this plugin, you must ensure that `tlec` is installed on your system. To install `tlec`, do the following:

1. Copy `tlec` file from the repo to a folder in the PATH (e.g. `/usr/local/bin`) 

1. Copy `tlec.pl` to `$EPAGES` on all your virtual machines
   ```
   <package manager> install tlec
   ```


**Note:** This plugin requires a configured copy of the `Flakes` plugin.


## Development

Port the OSX-specific parts to Linux and Windows. 

## See also ...

... our SublimeLinter-contrib-perl-epages6 plugin for live $PERL syntax checking.



