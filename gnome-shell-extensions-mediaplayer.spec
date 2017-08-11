Name:       gnome-shell-extensions-mediaplayer
Version:    3.24
Release:    1
Summary:    A mediaplayer indicator for gnome-shell
URL:        https://github.com/eonpatapon/gnome-shell-extensions-mediaplayer
License:    GPLv2
BuildArch:  noarch
BuildRequires:   glib2-devel
BuildRequires:   gnome-common
BuildRequires:   intltool
BuildRequires:   pkgconfig
BuildRequires:   meson
BuildRequires:   gettext
Source0:    %{name}-%{version}.tar.xz

%description
gnome-shell-extensions-mediaplayer is a gnome-shell extension for controlling any MPRIS v2.1 capable media player.

This extension will monitor D-Bus for active players and automatically display them in the GNOME Shell's system menu by default.

%prep
%autosetup

%build
./build --zip-file

%install
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/extensions
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0/schemas/
unzip -d mediaplayer@patapon.info mediaplayer@patapon.info.zip
mv mediaplayer@patapon.info/schemas/org.gnome.shell.extensions.mediaplayer.gschema.xml %{buildroot}%{_datarootdir}/glib-2.0/schemas/
cp -r mediaplayer@patapon.info %{buildroot}%{_datarootdir}/gnome-shell/extensions


%post
glib-compile-schemas %{_datarootdir}/glib-2.0/schemas

%files
%{_datarootdir}/gnome-shell/extensions/mediaplayer@patapon.info/*
%{_datarootdir}/glib-2.0/schemas/org.gnome.shell.extensions.mediaplayer.gschema.xml
