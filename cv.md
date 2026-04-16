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
    {%- assign contacts = site.data.socials | where_exp: "l", "l.icon != 'pgp'" -%}
    {%- for link in contacts -%}
      <a href="{{ link.url }}"{% unless link.icon == "email" %} rel="me noopener" target="_blank"{% endunless %}>{{ link.name }}</a>{% unless forloop.last %} · {% endunless %}
    {%- endfor -%}
  </p>
</section>

<section id="cv-summary">
  <h2>Research Summary</h2>
  <p>Postdoctoral researcher in software engineering, working on merge conflict resolution and software variability, with a strong track record in model-based software engineering — particularly MATLAB/Simulink. My research develops practical tools (SMOKE, GRANDSLAM, ScoutSL) that lower the barrier to empirical research in model-based engineering, and studies how developers can be better supported in everyday version-control workflows.</p>
</section>

<section id="cv-experience">
  <h2>Experience</h2>
  <div class="cv-foldable">
    <details>
      <summary>
        <span class="when">Jan 2026 – present</span>
        <span class="what"><strong>Postdoctoral Researcher</strong>, Software Engineering Group, University of Bern</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Prototype development (MATLAB, Python, Java)</li>
        <li>Writing and reviewing research papers</li>
        <li>Supervision of BSc, MSc, and co-supervision of PhD students</li>
        <li>Teaching support and exam assessment</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Jan 2022 – Dec 2025</span>
        <span class="what"><strong>Doctoral Researcher</strong>, Software Engineering Group, University of Bern</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Prototype development (MATLAB, Python, Java)</li>
        <li>Writing and reviewing research papers</li>
        <li>Exam assessment and proctoring</li>
        <li>Literature research</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Jul 2024 – Dec 2024</span>
        <span class="what"><strong>Research Developer</strong>, University of Duisburg-Essen / Gesellschaft für Informatik</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Contributor to the DFG project <a href="https://nfdixcs.org/">NFDIxCS</a></li>
        <li>Prototyping for model-based use cases</li>
        <li>Writing and reviewing research papers</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Jun 2019 – Dec 2021</span>
        <span class="what"><strong>Research Associate</strong>, Humboldt University of Berlin (Model-Driven Software Engineering)</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Contributor to the DFG project SimuComp</li>
        <li>Prototype development (Python, Java)</li>
        <li>Writing and reviewing research papers</li>
        <li>Exam assessment and proctoring</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Oct 2015 – May 2019</span>
        <span class="what"><strong>Student Research Assistant</strong>, Fraunhofer AISEC</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Java, Docker, CI, Bash, VirtualBox</li>
        <li>Programming, software testing and configuration</li>
        <li>Research, risk analysis, and documentation</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Mar 2014 – Sep 2014</span>
        <span class="what"><strong>Student Assistant</strong>, Ctb Camtec GmbH</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Web development (HTML, CSS, PHP) and VB programming</li>
        <li>Windows Server, mail server, VMware administration</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Sep 2009 – Sep 2011</span>
        <span class="what"><strong>Tutor</strong>, Humboldt University of Berlin (Algorithms and Complexity)</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Designed and graded exercises and exams</li>
        <li>Led tutorial sessions</li>
      </ul>
    </details>
    <details>
      <summary>
        <span class="when">Oct 2007 – May 2009</span>
        <span class="what"><strong>Student Assistant / Tutor</strong>, TU Berlin (Industrial Information Technology)</span>
        <span class="chev">{% include icon.html name="chevron" %}</span>
      </summary>
      <ul>
        <li>Implemented evolutionary algorithms in C++</li>
        <li>Led tutorials for "Introduction to C++ for Engineers"</li>
        <li>Reviewed course materials, exercises, and exams</li>
      </ul>
    </details>
  </div>
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
        Advisor: Dr. Kim Völlinger · Final grade 1.3 (<em>sehr gut</em> / very good; German scale where 1.0 is best, 4.0 is lowest pass)<br>
        Thesis: <em>Formale Instanzverifikation zertifizierender verteilter Algorithmen</em>
      </div>
    </li>
    <li>
      <div class="when">1997 – 2006</div>
      <div class="what">
        <strong>Abitur</strong>, Rosa-Luxemburg-Oberschule, Berlin-Pankow · Final grade 1.6 (<em>gut</em> / good; German scale, 1.0 best)
      </div>
    </li>
  </ul>
</section>

<section id="cv-awards">
  <h2>Awards</h2>
  <ul class="cv-plain">
    <li>
      <strong>Distinguished Paper Award</strong>, EASE 2024 —
      <a href="https://seg.inf.unibe.ch/news/2024/05/23/ease-2024-distinguished-paper-award/">for "Towards Semi-Automated Merge Conflict Resolution: Is It Easier Than We Expected?"</a>
    </li>
  </ul>
</section>

<section id="cv-publications">
  <h2>Publications</h2>
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

  <h3>Conferences</h3>
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

<section id="cv-talks">
  <h2>Invited Talks &amp; Presentations</h2>
  <ul class="cv-list">
    <li>
      <div class="when">May 2026</div>
      <div class="what">"GRANDSLAM: Linearly Scalable Model Synthesis" at ICST 2026</div>
    </li>
    <li>
      <div class="when">Sep 2024</div>
      <div class="what">"SMOKE: Simulink Model Obfuscator Keeping Structure" at MODELS 2024</div>
    </li>
    <li>
      <div class="when">Jun 2024</div>
      <div class="what">"Towards Semi-Automated Merge Conflict Resolution: Is It Easier Than We Expected?" at EASE 2024</div>
    </li>
    <li>
      <div class="when">Oct 2023</div>
      <div class="what">"ScoutSL: An Open-Source Simulink Search Engine" and "EvoSL: A Large Open-Source Corpus of Changes in Simulink Models &amp; Projects" at MODELS 2023</div>
    </li>
    <li>
      <div class="when">Jun 2020</div>
      <div class="what">"On the Replicability of Experimental Tool Evaluations in Model-Based Development" at ICSMM 2020</div>
    </li>
  </ul>
</section>

<section id="cv-grants">
  <h2>Funded Research Projects</h2>
  <ul class="cv-list">
    <li>
      <div class="when">Oct 2023 – Sep 2027</div>
      <div class="what">
        <strong>Merge++</strong> — SNSF-funded research project on merge conflict resolution (<a href="https://data.snf.ch/grants/grant/219719">SNSF grant 219719</a>, PI: Timo Kehrer)<br>
        <span class="muted">Contributed substantially to the successful grant proposal.</span>
      </div>
    </li>
  </ul>
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
        <strong>{{ year.year }}:</strong>&nbsp;
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
  <p><strong>Regular use:</strong> Java, Python, C++, MATLAB, Simulink</p>
  <p><strong>Occasional:</strong> C, Coq, Haskell, Tamarin, Xtext, R, JavaScript, HTML, Prolog, Pascal</p>

  <h3>Languages</h3>
  <ul class="cv-plain">
    <li>German — native</li>
    <li>English — fluent</li>
    <li>French — B1 (written)</li>
    <li>Portuguese — A2</li>
    <li>Japanese — A2</li>
  </ul>

</section>

<section id="cv-memberships">
  <h2>Professional Memberships</h2>
  <ul class="cv-plain">
    <li>ACM — Association for Computing Machinery</li>
    <li>IEEE — Institute of Electrical and Electronics Engineers</li>
  </ul>
</section>

<script>
(function () {
  var details = document.querySelectorAll('.cv-foldable details');
  var prior = [];
  window.addEventListener('beforeprint', function () {
    prior = Array.from(details).map(function (d) { return d.open; });
    details.forEach(function (d) { d.open = true; });
  });
  window.addEventListener('afterprint', function () {
    details.forEach(function (d, i) { d.open = prior[i] || false; });
  });
})();
</script>
