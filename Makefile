RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba observatory-roof-server.spec
	${RPMBUILD} -ba observatory-roof-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-roof.spec
	${RPMBUILD} -ba superwasp-roof-data.spec
	mv build/noarch/*.rpm .
	rm -rf build
