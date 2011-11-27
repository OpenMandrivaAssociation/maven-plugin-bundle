Name:           maven-plugin-bundle
Version:        2.0.0
Release:        9
Summary:        Maven Bundle Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/maven-bundle-plugin-2.0.0-project.tar.gz
BuildRequires: aqute-bndlib >= 0.0.363
BuildRequires: plexus-utils >= 1.4.5
BuildRequires: felix-osgi-obr
BuildRequires: kxml
BuildRequires: maven-shared-dependency-tree >= 1.1-3
BuildRequires: maven-wagon >= 1.0-0.2.b2
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin 
BuildRequires: maven-jar-plugin 
BuildRequires: maven-javadoc-plugin 
BuildRequires: maven-plugin-plugin 
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin >= 2.3
BuildRequires: maven-surefire-provider-junit >= 2.3
BuildRequires: maven-doxia-sitetools
BuildRequires: felix-parent
Requires: aqute-bndlib >= 0.0.363
Requires: plexus-utils >= 1.4.5
Requires: felix-osgi-obr
Requires: kxml
Requires: maven2
Requires: maven-archiver
Requires: maven-shared-dependency-tree
Requires: maven-wagon
Requires: plexus-archiver
Requires: plexus-containers-container-default
Requires: felix-parent

BuildArch: noarch


%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n maven-bundle-plugin-%{version}

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/maven-bundle-plugin-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.felix maven-bundle-plugin %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

