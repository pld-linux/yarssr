%include	/usr/lib/rpm/macros.perl
Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		yarssr
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/yarssr/yarssr-2.1.tar.bz2
# Source0-md5:	bb3ff2d2255f8b1c86ce05e413e3cd63
Source1:	%{name}.desktop
URL:		http://yarssr.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gtk2-GladeXML
Requires:	perl-Gtk2-TrayIcon
Requires:	perl-XML-RSS
Requires:	perl-Gnome2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YARSSR is a GTK+/GNOME RSS Reader nested in system tray.

%description -l pl
YARSSR to czytnik informacji RSS dla GTK+/GNOME dzia³aj±cy w
obszarze powiadamiania.

%prep
%setup -q -n %{name}-2.1

%build
%{__make} \
	PREFIX=%{_prefix} \
	LIBDIR=%{perl_vendorarch}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{perl_vendorarch}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Yarssr.pm
%dir %{perl_vendorarch}/Yarssr
%{perl_vendorarch}/Yarssr/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/%{name}/pixmaps
%{_desktopdir}/*
