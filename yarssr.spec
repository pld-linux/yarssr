Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		yarssr
Version:	0.1.7
Release:	1
License:	GPL
Group:		Applications/Internet
Source0:	http://dl.sourceforge.net/yarssr/yarssr-%{version}.tar.bz2
# Source0-md5:	b7e4567f1fb2cc6d3aba7e9bf00a3021
URL:		http://laylward.com/yarssr/
BuildRequires:	perl-Gtk2
BuildRequires:	perl-Gtk2-GladeXML
BuildRequires:	perl-Gtk2-TrayIcon
BuildRequires:	perl-XML-RSS
Requires:	perl-Gnome2-VFS
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YARSSR is a GTK+ RSS Reader

%prep
%setup -q

%build
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
#%{_desktopdir}/*
#%{_pixmapsdir}/*
