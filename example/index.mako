<%inherit file="${context['main_template'].uri}"/>
${panel('page_header')}
${panel('breadcrumb', breadcrumb=layout.page_context.breadcrumb)}
<div class="row">
  <div class="col-md-4">
    ${panel('navigationlist', navigationlist=layout.page_context.sidemenu)}
  </div>
  <div class="col-md-8">
    ${message}
    ${request.locale_name}
    <p>
    ${h.format_datetime(now, format="full")}
    <p>
    ${now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
    <p>
    ${h.format_datetime(utcnow, format="full")}
    <p>
    ${utcnow.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
  </div>
</div>
