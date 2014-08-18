mock: clean prepare
	mbt

rpmbuild: clean prepare
	mbt --buildstyle=rpmbuild

clean:
	rm -rf BUILD BUILDROOT SRPMS RPMS SOURCES/composer.phar

prepare:
	mkdir -p BUILD RPMS/noarch SRPMS SOURCES
	curl -s -z SOURCES/composer.phar -o SOURCES/composer.phar https://getcomposer.org/composer.phar
	php SOURCES/composer.phar --no-ansi --version | sed -E 's/.*([0-9]{4})-([0-9]{2})-([0-9]{2}).*/\1\2\3/' > SOURCES/version.txt
	test -s SOURCES/version.txt || { echo "Failed to get Composer version number"; exit 1; }
