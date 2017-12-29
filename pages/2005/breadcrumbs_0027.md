date: 2005-11-28
title: 'a fly-by of XACML'
published: True
tags: ['breadcrumbs']

Somebody listed SAML+XACML as an access control model, and I asked for a summary, as contrasted with the unix user/group/world model. The summary was, <q>XACML is an access control rules language; you can write rules about access and credentials</q>. So I'm taking a look at <a href="http://xml.coverpages.org/xacml.html">XACML</a>

ugh... urn:oasis:names:tc:xacml:2.0:policy

<a href="http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xacml">xacml TC in OASIS</a>

<a href="http://docs.oasis-open.org/xacml/2.0/access_control-xacml-2.0-core-spec-os.pdf">XACML 2.0 spec (PDF)</a>

section 3.3 Policy language model looks nice... it's a UML diagram; pretty straightforwardly translated to OWL

reading the XACML spec... typical XML-base spec... table of contents enumerates the syntactic elements. semantics isn't visible from TOC

ah... semantics is found in section 7. Functional requirements
