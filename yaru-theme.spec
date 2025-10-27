#
# spec file for package yaru-theme
#
# Copyright (c) 2024 mantarimay
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   yaru
Name:           yaru-theme
Version:        25.10.3
Release:        0
Summary:        Yaru theme from the Ubuntu community
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
URL:            https://github.com/ubuntu/yaru
Source:         %{url}/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.59
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This is the theme shaped by the community on the Ubuntu hub.

%package -n gnome-shell-theme-yaru
Summary:        Yaru GNOME Shell Theme
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       gnome-shell-extension-user-theme
Suggests:       gtk3-metatheme-yaru
Suggests:       gtk4-metatheme-yaru
Suggests:       yaru-icon-theme
Suggests:       sound-theme-yaru
Suggests:       yaru-theme
Supplements:    (gnome-shell and theme-yaru)

%description -n gnome-shell-theme-yaru 

This package contains GNOME Shell Theme.

%package -n gtk2-metatheme-yaru
Summary:        GTK+ 2 support for the Yaru Gtk Theme
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
Requires:       gtk2-engine-murrine
Requires:       gtk2-theming-engine-adwaita

%description -n gtk2-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

%package -n gtk3-metatheme-yaru
Summary:        GTK+ 3 support for the Yaru Gtk Theme
License:        GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC-BY-SA-4.0
Requires:       gtk3

%description -n gtk3-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

%package     -n gtk4-metatheme-yaru
Summary:        GTK+ 4 support for the Yaru GTK Theme
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
Requires:       gtk4

%description -n gtk4-metatheme-yaru
This is the theme shaped by the community on the Ubuntu hub.

%package -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA-4.0
Requires:       hicolor-icon-theme >= 0.17
Requires:       humanity-icon-theme >= 0.6.16

%description -n yaru-icon-theme
This is the theme shaped by the community on the Ubuntu hub.

This package contains the icon theme.

%package -n sound-theme-yaru
Summary:        Yaru sound theme
License:        CC-BY-SA-4.0
Supplements:    (sound and theme-yaru)

%description -n sound-theme-yaru
This is the theme shaped by the community on the Ubuntu hub.

This package contains the sound theme following the XDG theming
specification.

%package     -n yaru-gtksourceview-theme
Summary:        Yaru GtkSourceView theme
License:        CC-BY-SA-4.0

%description -n yaru-gtksourceview-theme
This is the theme shaped by the community on the Ubuntu hub.

This package contains the GtkSourceView theme.

%prep
%setup -q -n %{_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

rm  %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
    %{buildroot}%{_datadir}/xsessions/Yaru-xorg.desktop \
    %{buildroot}%{_datadir}/wayland-sessions/Yaru.desktop \
    %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

%fdupes %{buildroot}%{_datadir}/themes/Yaru*/
%fdupes %{buildroot}%{_datadir}/gnome-shell/theme/Yaru*/
%fdupes %{buildroot}%{_datadir}/icons/Yaru*/
%fdupes %{buildroot}%{_datadir}/sounds/Yaru/
%fdupes %{buildroot}%{_datadir}/*gtksourceview*

%files -n gnome-shell-theme-yaru
%doc AUTHORS CONTRIBUTING.md README.md
%{_datadir}/themes/Yaru*/metacity-1/
%{_datadir}/gnome-shell/modes/yaru.json
%{_datadir}/gnome-shell/theme/Yaru*/
%{_datadir}/themes/Yaru-*/index.theme
%{_datadir}/themes/Yaru-dark/gnome-shell
%{_datadir}/themes/Yaru/gnome-shell
%{_datadir}/themes/Yaru/index.theme
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/modes
%dir %{_datadir}/gnome-shell/theme
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-blue-dark
%dir %{_datadir}/themes/Yaru-blue
%dir %{_datadir}/themes/Yaru-dark
%dir %{_datadir}/themes/Yaru-magenta-dark
%dir %{_datadir}/themes/Yaru-magenta
%dir %{_datadir}/themes/Yaru-olive-dark
%dir %{_datadir}/themes/Yaru-olive
%dir %{_datadir}/themes/Yaru-prussiangreen-dark
%dir %{_datadir}/themes/Yaru-prussiangreen
%dir %{_datadir}/themes/Yaru-purple-dark
%dir %{_datadir}/themes/Yaru-purple
%dir %{_datadir}/themes/Yaru-red-dark
%dir %{_datadir}/themes/Yaru-red
%dir %{_datadir}/themes/Yaru-sage-dark
%dir %{_datadir}/themes/Yaru-sage
%dir %{_datadir}/themes/Yaru-wartybrown-dark
%dir %{_datadir}/themes/Yaru-wartybrown
%dir %{_datadir}/themes/Yaru-yellow-dark
%dir %{_datadir}/themes/Yaru-yellow

%files -n gtk2-metatheme-yaru
%{_datadir}/themes/Yaru-*/gtk-2.0/
%{_datadir}/themes/Yaru/gtk-2.0/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n gtk3-metatheme-yaru
%{_datadir}/themes/Yaru-*/gtk-3.*/
%{_datadir}/themes/Yaru/gtk-3.*/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n gtk4-metatheme-yaru
%{_datadir}/themes/Yaru-*/gtk-4.*/
%{_datadir}/themes/Yaru/gtk-4.*/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n yaru-icon-theme
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/icons/Yaru*/

%files -n sound-theme-yaru
%license COPYING* LICENSE_CCBYSA
%doc debian/changelog AUTHORS CONTRIBUTING.md README.md
%{_datadir}/sounds/Yaru/

%files -n yaru-gtksourceview-theme
%{_datadir}/gtksourceview-*/styles/Yaru*.xml
%dir %{_datadir}/gtksourceview-2.0
%dir %{_datadir}/gtksourceview-2.0/styles
%dir %{_datadir}/gtksourceview-3.0
%dir %{_datadir}/gtksourceview-3.0/styles
%dir %{_datadir}/gtksourceview-4
%dir %{_datadir}/gtksourceview-4/styles
%dir %{_datadir}/gtksourceview-5
%dir %{_datadir}/gtksourceview-5/styles
%dir %{_datadir}/libgedit-gtksourceview-300
%dir %{_datadir}/libgedit-gtksourceview-300/styles
%{_datadir}/libgedit-gtksourceview-300/styles/Yaru{,-dark}.xml

%changelog
