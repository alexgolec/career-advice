# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=-W
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = text
BUILDDIR      = _output
OUTPUTDIR     = docs

# Put it first so that "make" without argument is like "make help".
html: build-sphinx-html install

build-sphinx-html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	@echo 
	@echo Copying output to GitHub docs location
	@echo 
	rm -rf $(OUTPUTDIR)
	cp -r $(BUILDDIR)/html $(OUTPUTDIR)
	touch $(OUTPUTDIR)/.nojekyll

.PHONY: html Makefile.sphinx

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
