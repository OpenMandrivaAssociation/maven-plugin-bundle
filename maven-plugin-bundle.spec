%{?_javapackages_macros:%_javapackages_macros}
%global site_name maven-bundle-plugin

Name:           maven-plugin-bundle
Version:        2.3.7
Release:        14%{?dist}
Group:		System/Libraries
Summary:        Maven Bundle Plugin
License:        ASL 2.0
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/felix/%{site_name}-%{version}-source-release.tar.gz

Patch0:         %{site_name}-dependency.patch
Patch1:         %{site_name}-unreported-exception.patch

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.mockito:mockito-all)

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%patch0 -p1
%patch1 -p1

# remove bundled stuff
#rm -rf src/main/java/org/apache/maven

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-14
- Add build-requires on mockito

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-12
- Update to current packaging guidelines

* Thu Feb 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-11
- Remove unneeded R and BR: maven-wagon

* Fri Jul 26 2013 Tomas Radej <tradej@redhat.com> - 2.3.7-10
- Fixed release number

* Wed Jul 17 2013 Tomas Radej <tradej@redhat.com> - 2.3.7-9
- Updated source address (error 404)

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-8
- Add missing BR: maven-plugin-testing-harness

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-7
- Re-enable tests

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.7-3
- Add kxml2 to pom as a dependency

* Mon Apr 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-2
- Add missing BuildRequires

* Wed Feb 29 2012 Jaromir Capik <jcapik@redhat.com> 2.3.7-1
- Update to 2.3.7

* Thu Jan 19 2012 Jaromir Capik <jcapik@redhat.com> 2.3.6-3
- Bundled maven sources readded (they seem to change the behaviour)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Jaromir Capik <jcapik@redhat.com> 2.3.6-1
- Update to 2.3.6

* Mon Dec 19 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-3
- Minimal aqute-bndlib VR set to 1.43.0-2 (older ones are broken)

* Mon Nov 14 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-2
- OBR plugin readded (it's been merged to the bundle plugin)

* Mon Oct 24 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-1
- Update to 2.3.5

* Tue Oct 17 2011 Jaromir Capik <jcapik@redhat.com> 2.0.0-11
- aqute-bndlib renamed to aqute-bnd

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-10
- Do not depend on maven2.

* Thu Feb 10 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-9
- BR maven-surefire-provider-junit4.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-7
- BR/R felix-parent.

* Thu Sep 9 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-5
- Fix BuildRequires.

* Fri Sep 18 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-4
- Add missing Requires.

* Wed Sep 9 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-3
- BR doxia-sitetools.

* Mon Sep 7 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-2
- Fix BR/Rs.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Initial import.

