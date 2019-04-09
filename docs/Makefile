# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

api:
	sphinx-apidoc -f -e -H "Python API" --ext-autodoc --ext-coverage --ext-githubpages -o api/python ../python/PyKomoran /\*tests\*/
	javasphinx-apidoc -f --title "Java API" -o api/java/ ../java/src/main/java/kr/co/shineware/nlp/pykomoran/

docs:
	make clean
	make -B api
	make html

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
