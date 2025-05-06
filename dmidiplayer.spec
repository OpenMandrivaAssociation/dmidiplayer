Summary:		Multi-platform MIDI File Player
Name:		dmidiplayer
Version:		1.7.5
Release:		1
License:		GPLv3+
Group:		Sound
Url:		https://sourceforge.net/projects/dmidiplayer/
Source0:	https://sourceforge.net/projects/dmidiplayer/files/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:		cmake >= 3.16
BuildRequires:		git
BuildRequires:		gzip-utils
# Needed for docs, but not provided yet
#BuildRequires:	 pandoc
BuildRequires:		pbzip2
BuildRequires:		uchardet
BuildRequires:		qt6-qttools-linguist-tools
BuildRequires:		pkgconfig(drumstick-file) >= 2.10
BuildRequires:		pkgconfig(drumstick-rt)
BuildRequires:		pkgconfig(drumstick-widgets)
BuildRequires:		pkgconfig(Qt6Core) >= 6.2
BuildRequires:		pkgconfig(Qt6Core5Compat)
BuildRequires:		pkgconfig(Qt6Gui)
BuildRequires:		pkgconfig(Qt6PrintSupport)
BuildRequires:		pkgconfig(Qt6Widgets)
BuildRequires:		pkgconfig(uchardet) >= 0.0.8

%description
Drumstick MIDI File Player: a Qt-only replacement for Kmid2.
Some key features:
* MIDI Output to hardware MIDI ports, or any other Drumstick back-end.
* Transpose song tonality between -12 and +12 semitones.
* Change MIDI volume level (using MIDI CC7).
* Scale song speed between half and double tempo.
* Lyrics, Piano Player and MIDI Channels views.
* Supports MID/KAR (Standard MIDI Files) and WRK (Cakewalk) file formats.

%files
%doc ChangeLog LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/net.sourceforge.%{name}.desktop
%{_datadir}/metainfo/net.sourceforge.%{name}.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Building docs now requires pandoc and we don't have it yet...
%cmake -DUSE_QT5=OFF -DBUILD_DOCS=OFF
%make_build


%install
%make_install -C build

# Fix gzipped-svg-icon
(
cd %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
zcat %{name}.svgz > %{name}.svg && rm -f %{name}.svgz
)
