title: The Sorry State of the Art in Consumer Medical Data Portability
date: 2013-06-22
published: true
tags: [microformats, data, linked data, health, informatics]
summary: My doctor's portal offers data in the standard CCD format;
         What's the shortest path to get that data to my employer's
         health assessment? Copy and paste, one field at a time.

My employment health benefits include a discount if I provide "current
biometric values" such as cholesterol and glucose in a health
assessment questionnaire. My doctor just started giving access to lab
results via a patient portal. The portal even supports download in
[CCD](http://en.wikipedia.org/wiki/Continuity_of_Care_Document)
format:

> As part of U.S. federal incentives for the adoption of electronic
> health records, known as Meaningful Use, the CCD and Continuity of
> Care Record (CCR) were both selected as acceptable extract formats
> for clinical care summaries in the program's first stage. To be
> certified for this federal program, an Electronic Health Record must
> be able to generate a CCD (or equivalent CCR) that has the sections
> of allergies, medications, problems, and laboratory results, in
> addition to patient header information.[6] Several of these sections
> also have mandated vocabularies, such as LOINC for laboratory
> results, according to the federal program.

I'm just back from [i2b2](https://www.i2b2.org/) meetings at Harvard
Medical School, learning about
[SMART](http://smartplatforms.org/)-enabled health information
technology and amazing data-driven advances in treatment of childhood
diseases.

And what was the shortest path to get the data from my doctor's portal
to my employer's health assessment?

Copy and paste, one field at a time.

The health assessment site doesn't support CCDs or anything like it.
Maybe it's because they took one look at what's inside and ran away
screaming. Who could blame them?

      <component>
        <section>
          <templateId root="2.16.840.1.113883.10.20.1.11" />
          <templateId root="2.16.840.1.113883.3.88.11.83.103" />
          <templateId root="1.3.6.1.4.1.19376.1.5.3.1.3.6" />
          <code code="11450-4" codeSystem="2.16.840.1.113883.6.1"
          codeSystemName="LOINC" displayName="Problems" />
		  ...
          <entry typeCode="DRIV">
            <act classCode="ACT" moodCode="EVN">
              <templateId root="" />
              <templateId root="2.16.840.1.113883.3.88.11.83.7" />
              <templateId root="1.3.6.1.4.1.19376.1.5.3.1.4.5.2" />
              <templateId root="1.3.6.1.4.1.19376.1.5.3.1.4.5.1" />
              <id root="XZomV5It-NdyF-BlXK-Fz1A-ZwTQpgeAUiE0" />
              <code nullFlavor="NA" />
              <statusCode code="active" />
              <effectiveTime>
                <low nullFlavor="UNK" />
              </effectiveTime>
              <entryRelationship inversionInd="false"
              typeCode="SUBJ">
                <observation classCode="OBS" moodCode="EVN">
                  <templateId root="" />
                  <templateId root="1.3.6.1.4.1.19376.1.5.3.1.4.5" />
                  <id root="xNr52F8j-QD9W-19Fg-01c1-b96uLHssa0MF" />
                  <code code="55607006"
                  codeSystem="2.16.840.1.113883.6.96"
                  codeSystemName="SNOMED CT"
                  displayName="Problem" />
                  <text>
                    <reference value="#prob3" />
                  </text>
                  <statusCode code="completed" />
                  <effectiveTime>
                    <low nullFlavor="UNK" />
                  </effectiveTime>
                  <value nullFlavor="UNK" xsi:type="CD">
                    <translation code="V70.0" codeSystem=""
                    codeSystemName=""
                    displayName="Physical exam, routine" />
                  </value>
                  <entryRelationship typeCode="REFR">
                    <observation classCode="OBS" moodCode="EVN">
                      <templateId root="" />
                      <code code="" codeSystem=""
                      codeSystemName="LOINC"
                      displayName="STATUS" />
                      <statusCode code="completed" />
                      <value code="" codeSystem=""
                      codeSystemName="SNOMED CT"
                      displayName="Active" xsi:type="CE" />
                    </observation>
                  </entryRelationship>
                </observation>
              </entryRelationship>
            </act>
          </entry>

Whether motivated by good taste or fear of change, there is _some_
respect for the
[humans first microformats principle](http://microformats.org/wiki/humans-first);
the bit I elided above is:

          <title>Problems</title>
          <text>
            <table border="1" width="100%">
              <thead>
                <tr>
                  <th>Problem Type</th>
                  <th>Condition</th>
                  <th>ICD-9 Code</th>
                  <th>Effective Dates</th>
                  <th>OnSet Dates</th>
                  <th>Condition Status</th>
                </tr>
              </thead>
              <tbody>
                ...
                <tr>
                  <td>Problem</td>
                  <td>Physical exam, routine</td>
                  <td>V70.0</td>
                  <td>May 29, 2013</td>
                  <td></td>
                  <td>Active</td>
                </tr>
	            ...
              </tbody>
            </table>
          </text>

That's pretty much what it looks like on the paper documents that the
medical community has been using for decades:

<h2>Problems</h2>
<table border="1" width="100%">
              <thead>
                <tr>
                  <th>Problem Type</th>
                  <th>Condition</th>
                  <th>ICD-9 Code</th>
                  <th>Effective Dates</th>
                  <th>OnSet Dates</th>
                  <th>Condition Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Problem</td>
                  <td>Physical exam, routine</td>
                  <td>V70.0</td>
                  <td>May 29, 2013</td>
                  <td></td>
                  <td>Active</td>
                </tr>
              </tbody>
</table>

It's also useful data: you can paste it into a web form or a
spreadsheet or database tool without losing the structure. After all, the

> ... goal is not adoption alone but 'meaningful use' of EHRs&mdash;that
> is, their use by providers to achieve significant improvements in
> care. &mdash; [Blumenthal and Tavenner, New England Journal of Medicine, 2010](http://www.ncbi.nlm.nih.gov/pubmed/20647183)

I can't help thinking that if interchange were based on simple, visible
tables like that, my doctor's portal vendor woul notice that, for example,
their CCD only contains lab panel names and not the actual labs with values:

<table border="1" width="100%">
  <thead>
    <tr>
      <th>Test</th>
      <th>Attribute</th>
      <th>Value(Normal Range)</th>
      <th>LOINC Code</th>
      <th>Result</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CMP Comp. Metabolic Panel (14)**322000</td>
      <td></td>
      <td>()</td>
      <td></td>
      <td></td>
    <td>May 30, 2013</td>
  </tr>
 </tbody>
</table>

I've toyed with various tools for keeping a personal health record,
and a spreadsheet works pretty well: one sheet (aka table) for problems,
one for meds, one for labs, and so on.

To address the abiguity of short text column headings, we should, of
course, ground the terms in the web using linked data techniques
such as [linked CSV](http://jenit.github.io/linked-csv/)
and [linked data tables](http://www.ldtables.org/wiki/Tutorial).
But even if the global identifiers got stripped, copying a table
of lab values from my doctor's portal into a "paste your Cholesterol
labs" box on the health assessment form should
work just fine.
