date: 2005-11-21
title: 'RDF Calendar, GRDDL, Microformats, and all that at XML2005 in Atlanta'
published: True
tags: ['breadcrumbs', 'quality']

  <p>My talk was:</p>

  <ul>
    <li class="vevent">
      <abbr class="status" title="CONFIRMED">@</abbr> <abbr class=
      "dtstart" title="2005-11-16T14:45-0500">2:45 on Weds</abbr>
      <abbr class="dtend" title="2005-11-16T15:30-0500">:</abbr>
      <a class="summary url" id="we_lb4" href=
      "http://2005.xmlconference.org/program/wednesday#lb4" name=
      "we_lb4">Semantic Web Calendaring: RDF Calendar, hCalendar,
      and GRDDL</a>

      <div class="description">
        <p>I spent a lot of time preparing my slides,
        <cite><a href="http://www.w3.org/2002/12/cal/mash/slides">Semantic
        Web Data Integration with hCalendar and GRDDL</a></cite>,
        but at show-time, there were still too many. I had to
        basically skip over the cool OWL DL consistency checking
        example that I spent the better part of two days putting
        together, but I'm OK with that; the more basic points were
        more important.</p>
      </div>
    </li>
  </ul>

  <p>I unfortunately didn't leave any time for questions, but I had
  some interesting follow-up conversations:</p>

  <ul>
    <li>Somebody asked about using GRDDL and RDF to <b>track
    relationships between specs</b>, products that support them,
    and all that. I recalled that when the folks that run the
    <a href="http://registry.oasis-open.org/index.jsp">OASIS
    standards registry</a> contacted W3C, we told them we prefer a
    more decentralized approach: each organization publishes stuff
    about their own standards, in RDF, and anybody can aggregate
    it. <a href="http://www.w3.org/2001/04/roadmap/">TimBL's
    roadmap diagrams</a> show one approach. It is somewhat
    bit-rotten, but we have an <a href=
    "http://www.w3.org/2002/01/tr-automation/">automated system</a>
    in production for publishing basic title/author/date/version
    metadata about our specs and we're adding more stuff over time;
    e.g. which WG produced the spec (for patent policy reasons),
    comment due dates, etc. I told him this had come up in <a href=
    "http://lists.w3.org/Archives/Public/spec-prod/">spec-prod</a>;
    while I'm happy for the discussion to go there, my impression
    that it had come up there before was wrong. <em class="vtodo">I
    hope to organize my thoughts on this near <a href=
    "http://esw.w3.org/topic/NormativeReferences">NormativeReferences
    in the QA/ESW wiki</a> and re-kindle discussion in spec-prod or
    qa-ig.</em></li>

    <li>At lunch, somebody brought up my slide about email headers
    in RDF and asked if thunderbird has RDF support like mozilla
    and firefox. <em class="vtodo">I don't know, but I hope to find
    out. DanBri? Anyone?</em></li>
  </ul>

  <p>On the non-technical front, <b>jamming with <a rel="met" href=
  "http://lamammals.blogspot.com/">Len Bullard</a> was a blast</b>.
  We had a fascinating discussion of DRM and the recording industry
  where I relayed AaronSw's viewpoint that any model based on
  scarcity is uninteresting. Len says Prince is no longer
  independent, which contradicts the impression I got from studying
  <a href="http://en.wikipedia.org/wiki/Prince_%28artist%29">Prince
  in Wikipedia</a> recently. <em>Len says the big customer ripie
  for SemWeb technology is transit, at least as much as
  intelligence. Gotta look into that</em>.</p>

  <p>Later in the evening Len brought out a fake book and <a rel=
  "met" href=
  "http://2005.xmlconference.org/presenters/bios_ag#coates">Tony</a>
  and <a href="http://www.laurenwood.org/anyway/">Lauren</a> and
  <a rel="met" href="http://www.xmlgrrl.com/blog/">Eve</a> and
  <a href="http://recycledknowledge.blogspot.com/">John</a> sang
  and I tried to accompany them on Len's guitar. I was having so
  much fun that I raised a sizeable blood-blister on my strumming
  hand before I noticed. I think we did OK with <cite>Annie's
  Song</cite> as well as mangling lots of Beatles and such.</p>

  <p>Then Len took the guitar and Eve asked him to play <cite>Angel
  from Montgomery</cite> by Bonnie Raitt. When he said he didn't
  know it, I was able to use my sidekick to find <a href=
  "http://www.geocities.com/raitt_bonnie/tab-a1.html?200515">chords
  and lyrics</a> and since it was your basic three chord number, he
  picked it up in no time.</p>

  <p>As to the conference program...</p>

  <div>
    <h2>Tue 15 Nov</h2>

    <ul>
      <li class="vevent" id="tu_">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T09:00-0500">09:00</abbr><abbr class="dtend"
        title="2005-11-15T09:45-0500">.</abbr><a class=
        "summary url" href=
        "http://2005.xmlconference.org/program/tuesday">Opening
        Keynote: From Atoms to OWLs the new ecology of the Semantic
        Web</a>

        <div class="description">
          <p>Jonathan Robie said Jim made 5 or 6 points in this
          talk that had been obscure, at best, in earlier talks on
          the Semantic Web in RDF. <a href=
          "http://www.understandingxml.com/archives/2005/11/keynote_from_at.html">
          Kurt Cagle's notes</a> don't seem to show them.</p>

          <p>Unfortunately, the DAWG teleconference started at 9:30
          and missing it would have delayed the WG by several
          weeks, so I ducked out.</p>
        </div>
      </li>

      <li class="vevent" id="tu_8">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T11:45-0500">11:45</abbr><abbr class="dtend"
        title="2005-11-15T12:30-0500">.</abbr><a class=
        "summary url" href=
        "http://2005.xmlconference.org/program/tuesday#8">Handling
        Math in Real-World Workflows: Practical Lessons</a>

        <div class="description">
          <p>What jumped out at me was that <b>primary school
          publishers are hot on MathML content markup for reasons
          of accessibility</b>. It's good to hear that the theory
          that higher levels of semantic abstraction contribute to
          accessability plays out in practice.</p>

          <p>I asked if XSL-FO was on the map in this world of
          production math workflows, but he said no, not
          really.</p>

          <p>I wanted to ask <q>what would you change about mathml
          if you had a time machine?</q> but didn't find the right
          moment.</p>
        </div>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T14:00-0500">14:00</abbr><abbr class="dtend"
        title="2005-11-15T14:45-0500">.</abbr><a class=
        "summary url" id="tu_10" href=
        "http://2005.xmlconference.org/program/tuesday#10" name=
        "tu_10">Modeling Methods and Artifacts for Crossing the
        Data/Document Divide</a>

        <div class="description">
          <div style=
          "float: right; margin-left: 10px; margin-bottom: 10px;">
            <a href="http://www.flickr.com/photos/roland/64285676/"
            title="photo sharing"><img src=
            "http://static.flickr.com/35/64285676_60d48518d7_m.jpg"
            alt="" style="border: solid 2px #000000;" /></a><br />
            <span style=
            "font-size: 0.9em; margin-top: 0px;"><a href=
            "http://www.flickr.com/photos/roland/64285676/">KlaasBals
            XML 2005 - 9</a><br />
            Originally uploaded by <a href=
            "http://www.flickr.com/people/roland/">roland</a>.</span>
          </div>

          <p>He had this great slide (5 of 37) showing that
          business data goes from narrative documents (catalogs) to
          transaction data (orders) and back to narrative (support
          docs) and that data models need to cross them.</p>

          <p>An HL7 person asked <q>how important is it to trace
          back from document to data model?</q> which prompted me
          to add <a href=
          "http://www.w3.org/2002/12/cal/mash/slides#(18)">a
          slide</a> to my talk to make the point about how GRDDL
          lets you get from narrative documents back to UML-like
          models.</p>
        </div>
      </li>

      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T14:00-0500">14:00</abbr><abbr class="dtend"
        title="2005-11-15T14:45-0500">.</abbr><a class=
        "summary url" id="tu_9" href=
        "http://2005.xmlconference.org/program/tuesday#9" name=
        "tu_9">Federated Identity Management: An Overview of
        Concepts and Standards</a>

        <div class="description">
          <p>I really wanted to get this overview from Eve, but I
          got caught in a hallway conversation or something and
          missed it. I picked up some of how Liberty works from the
          next talk. ID-FF looks an awful lot like OpenID. I wonder
          what's the difference.</p>
        </div>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T14:45-0500">14:45</abbr><abbr class="dtend"
        title="2005-11-15T15:30-0500">.</abbr><a class=
        "summary url" id="tu_13" href=
        "http://2005.xmlconference.org/program/tuesday#13" name=
        "tu_13">Liberty Federation Deployment Case Study</a>

        <div class="description">
          <p>This showed real-world deployment of federated
          identity services remarkably like the ones we discuss in
          the <a href="http://www.policyawareweb.org/">PAW
          project</a>. I asked a lot of questions about the
          details, and the answers were quite reasonable.
          Afterward, I said to Eve and Yvonne, <q>Would you slow
          down? We're trying to pitch many of these ideas to
          research funders. If you deploy them all in commercial
          settings, where will we be? ;-)</q></p>

          <p>At some point, she mentioned government rules where
          authorization data was considered sensitive but
          authentication data was not. <em class="vtodo">I hope to
          get more details about that.</em></p>
        </div>
      </li>

      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T14:45-0500">14:45</abbr><abbr class="dtend"
        title="2005-11-15T15:30-0500">.</abbr><a class=
        "summary url" id="tu_lb4" href=
        "http://2005.xmlconference.org/program/tuesday#lb4" name=
        "tu_lb4">Microsoft's Language Integrated Query and XML</a>

        <div class="description">
          <p>I heard this was a great talk; both the content and
          the presentation. <em class="vtodo">I hope to get notes
          from Norm, Michael, and others who were there.</em></p>
        </div>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T16:00-0500">16:00</abbr><abbr class="dtend"
        title="2005-11-15T16:45-0500">.</abbr><a class=
        "summary url" id="tu_20" href=
        "http://2005.xmlconference.org/program/tuesday#20" name=
        "tu_20">The Atom Publishing Protocol: Publishing Web
        Content with XML and HTTP</a>

        <div class="description">
          <p>Most of the <a href=
          "http://bitworking.org/projects/XML2005/presentation/atom-publishing-protocol.html">
          stuff he presented</a> looked familiar; looks like not
          much has changed since the last time I saw Joe give a
          talk on the Atom protocol. He mentioned <q>great article
          by Udell on URIs</q>... ah... <cite><a href=
          "http://www.byte.com/tangled/">Tangled in the
          threads</a></cite> seems to be a column that Udell used
          to write for Byte. <em class="vtodo">Anybody got a
          pointer to the article Joe was talking about? I'd like to
          cite it among the <a href=
          "http://www.w3.org/2001/tag/em27">TAG educational
          materials</a></em>.</p>
        </div>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr><abbr class=
        "dtstart" title=
        "2005-11-15T16:45-0500">16:45</abbr><abbr class="dtend"
        title="2005-11-15T17:30-0500">.</abbr><a class=
        "summary url" id="tu_24" href=
        "http://2005.xmlconference.org/program/tuesday#24" name=
        "tu_24">Remixing RSS - past, present and future</a>

        <p class="description">An interesting perspective of the
        development of blogging. At their booth, I discovered
        bryght is a big drupal shop. I asked them about in-browser
        <a href=
        "http://esw.w3.org/topic/ImmersiveHypertextEditing">direct-manipulation
        editing</a>; they're big on <a href=
        "http://drupal.org/project/tinymce">TinyMCE</a>.</p>
      </li>

      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr><abbr class=
        "dtstart" title="2005-11-15T16:00-0500">16:00</abbr>
        <abbr class="dtend" title=
        "2005-11-15T16:45-0500">.</abbr><a class="summary url" id=
        "tu_18" href=
        "http://2005.xmlconference.org/program/tuesday#18" name=
        "tu_18">Names, Namespaces, XML Languages and XML Definition
        Languages</a>

        <div class="description">
          <p>I think Henry alluded to this paper in <a href=
          "http://www.w3.org/2001/tag/2005/09/22-tagmem-minutes.html#item02">
          a TAG discussion of XMLVersioning-41 in Edinburgh</a>. I
          was looking forward to getting it presented
          conference-style, but I guess I can read the paper and
          discuss it in the TAG.</p>
        </div>
      </li>
    </ul>
  </div>

  <div>
    <h2>Wed 16 Nov</h2>

    <ul>
      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-16T11:45-0500">11:45</abbr> <abbr class="dtend"
        title="2005-11-16T12:30-0500">.</abbr> <a class=
        "summary url" id="we_5" href=
        "http://2005.xmlconference.org/program/wednesday#5" name=
        "we_5">On Language Creation</a>

        <p class="description">missed this in the panic of
        preparing for my talk. Darn.</p>
      </li>

      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-16T11:45-0500">11:45</abbr> <abbr class="dtend"
        title="2005-11-16T12:30-0500">.</abbr> <a class=
        "summary url" id="we_8" href=
        "http://2005.xmlconference.org/program/wednesday#8" name=
        "we_8">Native XML Scripting with ECMAScript for XML
        (E4X)</a>

        <p class="description">missed this in the panic of
        preparing for my talk. Darn.</p>
      </li>

      <li class="vevent"><abbr class="status" title=
      "CONFIRMED">@</abbr> <abbr class="dtstart" title=
      "2005-11-16T14:00-0500">14:00</abbr> <abbr class="dtend"
      title="2005-11-16T14:45-0500">.</abbr> <a class="summary url"
      id="we_lb3" href=
      "http://2005.xmlconference.org/program/wednesday#lb3" name=
      "we_lb3">XSL Transform Self-Documentation</a></li>

      <li class="vevent">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-16T16:00-0500">16:00</abbr> <abbr class="dtend"
        title="2005-11-16T16:45-0500">.</abbr> <a class=
        "summary url" id="we_lb5" href=
        "http://2005.xmlconference.org/program/wednesday#lb5" name=
        "we_lb5">XML, REST, and SOAP at Yahoo</a>

        <p class="description">Wanted to follow up on the <a href=
        "http://www.parand.com/say/index.php/2005/10/13/speaking-at-xml-conf-2005-nov-16th/#comments">
        conversation we started briefly in his blog</a> but it was
        scheduled against a SPARQL session. Had to settle for a
        brief hand-shake and card exchange.</p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-16T16:00-0500">16:00</abbr> <abbr class="dtend"
        title="2005-11-16T16:45-0500">.</abbr> <a class=
        "summary url" id="we_19" href=
        "http://2005.xmlconference.org/program/wednesday#19" name=
        "we_19">SQL, XQuery, and SPARQL: What's wrong with this
        picture?</a>

        <p class="description">What looked like a SPARQL-bashing
        session turned into a pretty good SPARQL tutorial. Jim
        Melton, who has been doing SQL standards work for over 20
        years and sharing that experience in the XQuery WG for
        several years, took a close look at SPARQL, prompted by
        some nifty results by some folks using RDF/OWL in drug
        discovery. Even though he was "strongly encouraged" to
        conclude that SPARQL was obviated by SQL and XQuery, his
        conclusion was that it has a place.</p>
      </li>
    </ul>
  </div>

  <div>
    <h2>Thu 17 Nov</h2>

    <ul>
      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T09:00-0500">09:00</abbr> <abbr class="dtend"
        title="2005-11-17T09:45-0500">.</abbr> <a class=
        "summary url" id="th_lb1" href=
        "http://2005.xmlconference.org/program/thursday#lb1" name=
        "th_lb1">Describing Web Applications</a>

        <p>missed the talk but spent some time noodling on <a href=
        "http://esw.w3.org/topic/WebDescriptionProposals">WebDescriptionProposals
        in the ESW wiki</a>. <em class="vtodo">I hope to study WADL
        more closely.</em></p>
      </li>

      <li class="vevent" style="background: #e0e0e0"><abbr class=
      "status" title="TENTATIVE">*</abbr> <abbr class="dtstart"
      title="2005-11-17T09:00-0500">09:00</abbr> <abbr class=
      "dtend" title="2005-11-17T09:45-0500">.</abbr> <a class=
      "summary url" id="th_3" href=
      "http://2005.xmlconference.org/program/thursday#3" name=
      "th_3">Semantics and Security: Applying RDF and OWL to
      Defense and Security Challenges</a></li>

      <li class="vevent" style="background: #e0e0e0">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T11:00-0500">11:00</abbr> <abbr class="dtend"
        title="2005-11-17T11:45-0500">.</abbr> <a class=
        "summary url" id="th_12" href=
        "http://2005.xmlconference.org/program/thursday#12" name=
        "th_12">The Impact of XML on Contract Law and the Volume of
        Contract Litigation</a>

        <p class="description">I didn't get to see Jane Winn's talk
        (though it won an award and <em class="vtodo">I look
        forward to reading the paper</em>), but after Bob G.
        introduce me to her in the exhibit hall, we had a
        fascinating discussion of the social side of open source
        and open standards. There's some seminal paper on
        charismaric leadership that she's supposed to be sending
        me. I asked for a pointer, but it seems to come from the
        pre-Web world of paper and fax machines.</p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T11:00-0500">11:00</abbr> <abbr class="dtend"
        title="2005-11-17T11:45-0500">.</abbr> <a class=
        "summary url" id="th_9" href=
        "http://2005.xmlconference.org/program/thursday#9" name=
        "th_9">Unit Testing in XSLT 2.0</a>

        <p class="description">Some comments on XSLT 1.0 were
        pushed back a la <q>but wer're just doing a transformation
        language for stylesheets, not a general-purpose programming
        language.</q> Maybe so, but clearly XSLT 2.0 is
        sufficiently general purpose to build unit testing
        harnesses.</p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T11:45-0500">11:45</abbr> <abbr class="dtend"
        title="2005-11-17T12:30-0500">.</abbr> <a class=
        "summary url" id="th_13" href=
        "http://2005.xmlconference.org/program/thursday#13" name=
        "th_13">Automated mass production of XSLT stylesheets</a>

        <p class="description">Using a spreadsheet as a way to
        communicate design requirements and even decisions from
        users to developers and/or straight to the machine. Cute.
        Reminds me of <a href=
        "http://www.advogato.org/person/connolly/diary.html?start=22">
        my own work on using spreadsheets as an RDF authoring
        tool.</a></p>
      </li>

      <li class="vevent">
        <abbr class="status" title="TENTATIVE">*</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T14:00-0500">14:00</abbr> <abbr class="dtend"
        title="2005-11-17T14:45-0500">.</abbr> <a class=
        "summary url" id="th_lb5" href=
        "http://2005.xmlconference.org/program/thursday#lb5" name=
        "th_lb5">"Just" Use XML</a>

        <p class="description">His <a href=
        "http://www.intertwingly.net/blog/2005/11/17/Just-Use-XML">slides</a>
        have great stuff on pitfalls of XML, unicode, dateTime,
        etc.; filed it under <a rel="tag" href=
        "http://del.icio.us/connolly/quality">quality</a></p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T14:45-0500">14:45</abbr> <abbr class="dtend"
        title="2005-11-17T15:30-0500">.</abbr> <a class=
        "summary url" id="th_21" href=
        "http://2005.xmlconference.org/program/thursday#21" name=
        "th_21">A Generalized Grammar for Three-way XML
        Synchronization</a>

        <p class="description">This was much less relevant to
        <a href="http://www.w3.org/DesignIssues/Diff">our work on
        RDF diff/sync</a> than I thought it might be, but trick of
        using <b>SVG animation to show differences between
        images</b> was really cool.</p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T16:00-0500">16:00</abbr> <abbr class="dtend"
        title="2005-11-17T16:45-0500">.</abbr> <a class=
        "summary url" id="th_25" href=
        "http://2005.xmlconference.org/program/thursday#25" name=
        "th_25">Using XSL, XForms and UBL together to create
        complex forms with visual fidelity</a>

        <p class="description">I have missed so many chances to
        soak up XForms at a conference... I finally made the time
        for this one, but it turned out to me more about
        XSL-FO.</p>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T16:45-0500">16:45</abbr> <abbr class="dtend"
        title="2005-11-17T17:30-0500">.</abbr> <a class=
        "summary url" id="th_29" href=
        "http://2005.xmlconference.org/program/thursday#29" name=
        "th_29">Enterprise-level Web Form Applications with XForms
        and XFDL</a>

        <div class="description">
          <p><a href=
          "http://www.flickr.com/photos/roland/64287365/"><img style="text-align: right"
          src=
          "http://static.flickr.com/25/64287365_a88bb44af8_t.jpg"
          alt="John Boyer at XML2005" /></a> John Boyer is an
          XForms WG co-chair, as well as doing DSig stuff. He's now
          at IBM, since they acquired Pure Edge. Hendler got the
          two of us together in the hall to discuss some connection
          between XForms and SPARQL... something about using XForms
          in the role that XSLT plays in handling SPARQL results.
          Hmm.</p>

          <p>John asked that we "don't think of a Form as just the
          typical name/address or pizza order form"; likewise, he
          asked us to put aside our notion of table. But I didn't
          get a firm feel for what we're supposed to put in thier
          places, except that a form can be a blackjack game.</p>
        </div>
      </li>

      <li class="vevent">
        <abbr class="status" title="CONFIRMED">@</abbr>
        <abbr class="dtstart" title=
        "2005-11-17T20:00-0500">20:00</abbr> <abbr class="dtend"
        title="2005-11-17T21:00-0500">.</abbr> <a class=
        "summary url" id="th_keynote" href=
        "http://2005.xmlconference.org/program/thursday#keynote"
        name="th_keynote">Closing Keynote: Everyone's using XML,
        but does anyone care?</a>

        <p class="description">Very entertaining. On Web services,
        he said <q>we've got this little pea of xml under all these
        layers and only a true xml princess can feel it.</q></p>
      </li>
    </ul>
  </div>
