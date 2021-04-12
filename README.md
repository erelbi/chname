# Chname

- C ( Change) h (host) name
- Changes your domain name
- Gtk 3.0 used

## Build-Deb Package

`sudo apt install build-essential git-buildpackage debhelper debmake`

`git clone https://github.com/erelbi/chname.git`

`cd chanme/`

`sudo mk-build-deps -ir`

`gbp buildpackage --git-export-dir=/tmp/build-area -b -us -uc`

The package is built under the **/tmp/build-area/** directory.

## Install

    sudo dpkg -i  /tmp/build-area/chname_1.0_all.deb

## Download Debian Package
<a id="raw-url" href="https://github.com/erelbi/chname/releases/download/0.1/chname_1.0_all.deb">Download</a>

