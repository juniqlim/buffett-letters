---
title: Buffett Letters
---

워런 버핏의 서한 원문과 한글 번역. 저장소: [juniqlim/buffett-letters](https://github.com/juniqlim/buffett-letters)

{% assign sections = "partnership-letters/markdown-ko/|파트너십 서한 (한글),shareholder-letters/markdown-ko/|주주서한 (한글),partnership-letters/markdown/|파트너십 서한 (원문),shareholder-letters/markdown/|주주서한 (원문)" | split: "," %}
{% for s in sections %}{% assign parts = s | split: "|" %}{% assign pages = site.pages | where_exp: "p", "p.path contains parts[0]" | sort: "path" %}{% if pages.size > 0 %}
## {{ parts[1] }}

{% for p in pages %}[{{ p.name | remove: ".md" }}]({{ p.url | relative_url }}){% unless forloop.last %} · {% endunless %}{% endfor %}
{% endif %}{% endfor %}
