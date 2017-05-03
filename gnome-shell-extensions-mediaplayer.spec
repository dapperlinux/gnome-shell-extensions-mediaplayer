Name:       gnome-shell-extensions-mediaplayer
Version:    3.22
Release:    9
Summary:    A mediaplayer indicator for gnome-shell
URL:        https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer
License:    GPLv2
BuildArch:  noarch
BuildRequires:   glib2-devel
BuildRequires:   gnome-common
BuildRequires:   intltool
BuildRequires:   pkgconfig
Source0:    %{name}-%{version}.tar.gz

%description
gnome-shell-extensions-mediaplayer is a gnome-shell extension for controlling any MPRIS v2.1 capable media player.

This extension will monitor D-Bus for active players and automatically display them in the GNOME Shell's system menu by default.

%prep
%autosetup

%build
./autogen.sh --prefix=/usr
make

%install
%make_install

%post
glib-compile-schemas /usr/share/glib-2.0/schemas

%files
/usr/share/gnome-shell/extensions/mediaplayer@patapon.info/*
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.mediaplayer.gschema.xml
/usr/share/locale/*
