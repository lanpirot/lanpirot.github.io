<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9">
  <xsl:output method="html" encoding="UTF-8" indent="yes"
    doctype-system="about:legacy-compat"/>

  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>Sitemap &#8211; Alexander Boll</title>
        <link rel="stylesheet" href="/assets/css/style.css"/>
        <style>
          main { max-width: 52rem; }
          .sitemap-meta {
            color: var(--muted);
            font-size: 0.9rem;
            margin: 0 0 2rem;
          }
          table.sitemap {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95rem;
          }
          table.sitemap th,
          table.sitemap td {
            text-align: left;
            padding: 0.55rem 0.5rem;
            border-bottom: 1px solid var(--rule);
            vertical-align: top;
          }
          table.sitemap th {
            font-weight: 600;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 0.75rem;
            border-bottom: 1px solid var(--rule);
          }
          table.sitemap td.url { word-break: break-all; }
          table.sitemap td.date {
            color: var(--muted);
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
          }
          table.sitemap tr:hover td { background: var(--hover); }
        </style>
      </head>
      <body>
        <main>
          <h1>Sitemap</h1>
          <p class="sitemap-meta">
            This is an XML sitemap intended for search engines.
            <xsl:text> </xsl:text>
            <xsl:value-of select="count(s:urlset/s:url)"/> URLs listed.
            <xsl:text> </xsl:text>
            <a href="/">Back to home &#8594;</a>
          </p>
          <table class="sitemap">
            <thead>
              <tr>
                <th>URL</th>
                <th>Last modified</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="s:urlset/s:url">
                <xsl:sort select="s:loc"/>
                <tr>
                  <td class="url">
                    <a href="{s:loc}">
                      <xsl:value-of select="s:loc"/>
                    </a>
                  </td>
                  <td class="date">
                    <xsl:value-of select="substring(s:lastmod, 1, 10)"/>
                  </td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
