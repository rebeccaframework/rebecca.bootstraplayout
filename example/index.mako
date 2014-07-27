<%inherit file="${context['main_template'].uri}"/>
${panel('page_header')}
${panel('breadcrumb', breadcrumb=layout.page_context.breadcrumb)}
${message}
${request.locale_name}
<p>
${h.format_datetime(now, format="full", locale=request.locale_name)}
<p>
${now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
<p>
${h.format_datetime(utcnow, format="full", locale=request.locale_name)}
<p>
${utcnow.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
