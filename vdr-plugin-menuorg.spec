
%define plugin	menuorg
%define name	vdr-plugin-%plugin
%define version	0.4.3
%define rel	3

Summary:	VDR plugin: Reorganizes the main menu
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.e-tobi.net/blog/pages/vdr-menuorg/
Source:		http://www.e-tobi.net/blog/files/vdr-%plugin-%version.tar.gz
Source1:	menuorg.xml.minimum
Patch0:		menuorg-includes.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	libxml++-devel
BuildRequires:	glibmm2.4-devel
Requires:	vdr-abi = %vdr_abi

%description
This plug-in allows to reorganize VDR's main OSD menu. The new menu
structure is read from a XML config file. It's basic format is based
on the format used by the setup plug-in.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

sed -i 's,/var/lib/vdr/plugins,%{_vdr_plugin_cfgdir},' README

%vdr_plugin_params_begin %plugin
# loads the specified xml file
# default: vdrconfigdir/plugins/menuorg.xml
var=CONFIGFILE
param="-c CONFIGFILE"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 %SOURCE1 %{buildroot}%{_vdr_plugin_cfgdir}/menuorg.xml

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO vdr-submenu2menuorg menuorg.xml menuorg.dtd
%config(noreplace) %{_vdr_plugin_cfgdir}/menuorg.xml
