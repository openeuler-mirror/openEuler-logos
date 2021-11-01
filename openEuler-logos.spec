%global codename verne

Name:           openEuler-logos
Version:        1.0
Release:        7
Summary:        openEuler-related icons and pictures
License:        Licensed only for approved usage, see COPYING for details. 
Source0:        openEuler-logos-%{version}.tar.xz
BuildArch:      noarch
Requires(post): coreutils

Provides:       gnome-logos = %{version}-%{release} system-logos = %{version}-%{release}
Provides:       openEuler-logos = %{version}-%{release}
# We carry the GSettings schema override, tell that to gnome-desktop3
Provides:       system-backgrounds-gnome

%description
The openEuler-logos package (the "Package") contains files created by the
openEuler Project.

%prep
%setup -q

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/backgrounds/
for i in backgrounds/*.jpg backgrounds/*.png backgrounds/default.xml; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.background.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/desktop-backgrounds-default.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
done

for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  install -d -m 755  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 ${i} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
done

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

# save some dup'd icons
hardlink -v %{buildroot}/

%post
touch --no-create %{_datadir}/icons/hicolor || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%license COPYING
%{_datadir}/backgrounds/*
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/gnome-background-properties/*.xml
%{_datadir}/plymouth/themes/charge/*
%{_datadir}/pixmaps/*
%{_datadir}/anaconda/boot/*
%{_datadir}/anaconda/pixmaps/rnotes/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Wed Sep 22 2021 chenchen <chen_aka_jan@163.com> - 1.0-7
- fix hardlink command cannot be found

* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Wed Dec 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix in specs

* Mon Dec 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:delete the provides

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update the files of rpm

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update install openEuler logo

* Thu Aug 15 2019 openEuler Buildteam <buildteam@openEuler.org> - 1.0-1
- Package init


