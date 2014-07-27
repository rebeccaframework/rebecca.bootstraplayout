<%inherit file="${context['main_template'].uri}"/>
${panel('page_header')}
${panel('breadcrumb', breadcrumb=layout.page_context.breadcrumb)}
${h.literal(message)}
<p>
${h.format_datetime(now, format="full", locale="ja")}
<p>
${now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
<p>
${h.format_datetime(utcnow, format="full", locale="ja")}
<p>
${utcnow.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
