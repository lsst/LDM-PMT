#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sphinx configuration file
# see metadata.yaml in this repo for to update document-specific metadata

import os
from documenteer.designdocs import configure_sphinx_design_doc

# Ingest settings from metadata.yaml and use documenteer's
# configure_sphinx_design_doc to build a Sphinx configuration that is
# injected into this script's global namespace.
metadata_path = os.path.join(os.path.dirname(__file__), 'metadata.yaml')
with open(metadata_path, 'r') as f:
    confs = configure_sphinx_design_doc(f)
g = globals()
g.update(confs)

# Configure the latex conversion. We need to use the standard LSST style
# file which does not use \author or \maketitle.
# All the required information is in the "html_context" dict
context = confs["html_context"]

# Form author string for latex
authlist = context["author_list"]
authors = ", ".join(a.replace(" ", "~") for a in authlist)

# is this a draft? How do we tell if this is on master branch?
docstatus = "draft"

latex_docclass = {'manual': 'lsstdoc'}
latex_elements = {'maketitle': "\\renewcommand{\\releasename}{}\\mktitle\n",
                  'papersize': 'DM,SDP',
                  'preamble': r"""
\setDocTitle{\color[rgb]{0.16,0.42,0.57} \sf %s}
\setDocAuthor{%s}
\setDocRef{%s}
\setDocDate{%s}
\setDocCompact{true}
\setDocRevision{%s}
\setDocIssue{%s}
\setDocStatus{%s}
                  """ % (context["doc_title"],
                         authors,
                         context["doc_id"],
                         confs["today"],
                         confs["version"],
                         confs["version"],
                         docstatus), }
latex_toplevel_sectioning = "section"
latex_keep_old_macro_names = False
