---
layout: default
title: CV — Alexander Boll
description: Curriculum Vitae of Alexander Boll, Postdoctoral Researcher at the Software Engineering Group, University of Bern.
permalink: /cv/
---

{%- assign s = site.data.site -%}

<section id="cv-header" class="cv-header">
  <h1>{{ s.name }}</h1>
  <p class="role">{{ s.role }} · <a href="{{ s.affiliation_url }}">{{ s.affiliation }}</a> · {{ s.location }}</p>
  <p class="cv-contact">
    {%- for link in site.data.socials -%}
      {%- if link.icon == "email" or link.icon == "linkedin" or link.icon == "github" or link.icon == "orcid" or link.icon == "scholar" or link.icon == "dblp" -%}
        <a href="{{ link.url }}"{% unless link.icon == "email" %} rel="me noopener" target="_blank"{% endunless %}>{{ link.name }}</a>{% unless forloop.last %} · {% endunless %}
      {%- endif -%}
    {%- endfor -%}
  </p>
  <p class="cv-print-hint no-print">Tip: use your browser's <em>Print</em> dialog to save this page as a PDF.</p>
</section>

<section id="cv-experience">
  <h2>Experience</h2>
  <ul class="cv-list">
    <li>
      <div class="when">Jan 2026 – present</div>
      <div class="what">
        <strong>Postdoctoral Researcher</strong>, Software Engineering Group, University of Bern
        <ul>
          <li>Prototype development (MATLAB, Python, Java)</li>
          <li>Writing and reviewing research papers</li>
          <li>Supervision of BSc, MSc, and co-supervision of PhD students</li>
          <li>Teaching support and exam assessment</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Jan 2022 – Dec 2025</div>
      <div class="what">
        <strong>Doctoral Researcher</strong>, Software Engineering Group, University of Bern
        <ul>
          <li>Prototype development (MATLAB, Python, Java)</li>
          <li>Writing and reviewing research papers</li>
          <li>Exam assessment and proctoring</li>
          <li>Literature research</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Jul 2024 – Dec 2024</div>
      <div class="what">
        <strong>Research Developer</strong>, University of Duisburg-Essen / Gesellschaft für Informatik
        <ul>
          <li>Contributor to the DFG project <a href="https://nfdixcs.org/">NFDIxCS</a></li>
          <li>Prototyping for model-based use cases</li>
          <li>Writing and reviewing research papers</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Jun 2019 – Dec 2021</div>
      <div class="what">
        <strong>Research Associate</strong>, Humboldt University of Berlin (Model-Driven Software Engineering)
        <ul>
          <li>Contributor to the DFG project SimuComp</li>
          <li>Prototype development (Python, Java)</li>
          <li>Writing and reviewing research papers</li>
          <li>Exam assessment and proctoring</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Oct 2015 – May 2019</div>
      <div class="what">
        <strong>Student Research Assistant</strong>, Fraunhofer AISEC
        <ul>
          <li>Java, Docker, CI, Bash, VirtualBox</li>
          <li>Programming, software testing and configuration</li>
          <li>Research, risk analysis, and documentation</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Mar 2014 – Sep 2014</div>
      <div class="what">
        <strong>Student Assistant</strong>, Ctb Camtec GmbH
        <ul>
          <li>Web development (HTML, CSS, PHP) and VB programming</li>
          <li>Windows Server, mail server, VMware administration</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Sep 2009 – Sep 2011</div>
      <div class="what">
        <strong>Tutor</strong>, Humboldt University of Berlin (Algorithms and Complexity)
        <ul>
          <li>Designed and graded exercises and exams</li>
          <li>Led tutorial sessions</li>
        </ul>
      </div>
    </li>
    <li>
      <div class="when">Oct 2007 – May 2009</div>
      <div class="what">
        <strong>Student Assistant / Tutor</strong>, TU Berlin (Industrial Information Technology)
        <ul>
          <li>Implemented evolutionary algorithms in C++</li>
          <li>Led tutorials for "Introduction to C++ for Engineers"</li>
          <li>Reviewed course materials, exercises, and exams</li>
        </ul>
      </div>
    </li>
  </ul>
</section>

<section id="cv-education">
  <h2>Education</h2>
  <ul class="cv-list">
    <li>
      <div class="when">Jun 2019 – Dec 2025</div>
      <div class="what">
        <strong>Dr. rer. nat. (PhD) in Computer Science</strong>, University of Bern<br>
        Thesis: <em>Bridging the Data Desert: Mitigating Challenges of Model Accessibility in Simulink Research</em><br>
        Advisor: Prof. Dr. Timo Kehrer · Defended Dec 2025 · <a href="https://doi.org/10.48549/7066">doi.org/10.48549/7066</a>
      </div>
    </li>
    <li>
      <div class="when">Oct 2006 – Feb 2019</div>
      <div class="what">
        <strong>Diplom / M.Sc. in Computer Science</strong>, Humboldt University of Berlin<br>
        Final grade 1.3 · Thesis: <em>Formale Instanzverifikation zertifizierender verteilter Algorithmen</em>
      </div>
    </li>
    <li>
      <div class="when">1997 – 2006</div>
      <div class="what">
        <strong>Abitur</strong>, Rosa-Luxemburg-Oberschule, Berlin-Pankow · Final grade 1.6
      </div>
    </li>
  </ul>
</section>

<section id="cv-publications">
  <h2>Publications</h2>
  <p class="cv-note">Authored name in <strong>bold</strong>. Full list below; preprints and satirical pieces excluded.</p>

  {%- assign journals = site.data.publications | where: "type", "journal" -%}
  {%- assign conferences = site.data.publications | where: "type", "conference" -%}
  {%- assign theses = site.data.publications | where: "type", "thesis" -%}

  <h3>Journal Articles</h3>
  <ol class="cv-pubs">
    {%- for pub in journals -%}
      <li>
        {{ pub.authors | replace: "Alexander Boll", "<strong>Alexander Boll</strong>" }}.
        "{{ pub.title }}".
        <em>{{ pub.venue }}</em>, {{ pub.year }}.
        {%- if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi:{{ pub.doi }}</a>.{% endif -%}
        {%- if pub.award %} <span class="cv-award">{{ pub.award }}.</span>{% endif -%}
      </li>
    {%- endfor -%}
  </ol>

  <h3>Conference &amp; Workshop Papers</h3>
  <ol class="cv-pubs">
    {%- for pub in conferences -%}
      <li>
        {{ pub.authors | replace: "Alexander Boll", "<strong>Alexander Boll</strong>" }}.
        "{{ pub.title }}".
        <em>{{ pub.venue }}</em>, {{ pub.year }}.
        {%- if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi:{{ pub.doi }}</a>.{% endif -%}
        {%- if pub.award %} <span class="cv-award">{{ pub.award }}.</span>{% endif -%}
      </li>
    {%- endfor -%}
  </ol>

  <h3>Theses</h3>
  <ol class="cv-pubs">
    {%- for pub in theses -%}
      <li>
        {{ pub.authors | replace: "Alexander Boll", "<strong>Alexander Boll</strong>" }}.
        "{{ pub.title }}".
        <em>{{ pub.venue }}</em>, {{ pub.year }}.
        {%- if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi:{{ pub.doi }}</a>.{% endif -%}
      </li>
    {%- endfor -%}
  </ol>
</section>

<section id="cv-supervision">
  <h2>Student Supervision</h2>
  <ul class="cv-list">
    {%- for item in site.data.supervision -%}
      <li>
        <div class="when">{{ item.year }}</div>
        <div class="what">
          <strong>{{ item.student }}</strong> ({{ item.type }}) — {{ item.title }}
          {%- if item.cosupervisor %}<br><span class="muted">Co-supervised with {{ item.cosupervisor }}</span>{% endif -%}
        </div>
      </li>
    {%- endfor -%}
  </ul>
</section>

<section id="cv-teaching">
  <h2>Teaching</h2>
  <ul class="cv-list">
    {%- for item in site.data.teaching -%}
      <li>
        <div class="when">{{ item.years | join: ", " }}</div>
        <div class="what">
          <strong>{{ item.course }}</strong>, {{ item.institution }}<br>
          <span class="muted">{{ item.role }}</span>
        </div>
      </li>
    {%- endfor -%}
  </ul>
</section>

<section id="cv-service">
  <h2>Service</h2>
  <ul class="cv-list">
    {%- for item in site.data.service -%}
      <li>
        <div class="when">{{ item.year }}</div>
        <div class="what">
          <strong>{{ item.role }}</strong>, {% if item.url %}<a href="{{ item.url }}">{{ item.venue }}</a>{% else %}{{ item.venue }}{% endif %}
        </div>
      </li>
    {%- endfor -%}
  </ul>

  <h3>Reviewing</h3>
  <ul class="cv-reviewing">
    {%- for year in site.data.reviewing -%}
      <li>
        <strong>{{ year.year }}:</strong>
        {%- for v in year.venues -%}
          {{ v.name }}{% if v.count > 1 %} ({{ v.count }}){% endif %}{% unless forloop.last %}, {% endunless %}
        {%- endfor -%}
      </li>
    {%- endfor -%}
  </ul>
</section>

<section id="cv-skills">
  <h2>Skills</h2>

  <h3>Programming Languages</h3>
  <p><strong>Regular use:</strong> Java, Python, C++, Coq, MATLAB, Simulink</p>
  <p><strong>Occasional:</strong> C, Haskell, Tamarin, Xtext, R, JavaScript, HTML, Prolog, Pascal</p>

  <h3>Languages</h3>
  <ul class="cv-plain">
    <li>German — native</li>
    <li>English — fluent (11 months in New Zealand)</li>
    <li>French — B1 (written)</li>
    <li>Portuguese — A2</li>
    <li>Japanese — A2</li>
  </ul>

  <h3>Interests</h3>
  <ul class="cv-plain">
    <li>Bouldering</li>
    <li>Chess (Elo ~1800)</li>
    <li><a href="https://projecteuler.net/">Project Euler</a> — 200+ problems solved (top 0.2%)</li>
  </ul>
</section>
