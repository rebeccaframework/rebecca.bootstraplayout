<div class="panel ${panel_style}">
  %if panel.heading:
  <div class="panel-heading">
    ${panel.heading}
  </div>
  %endif
  <div class="panel-body">
    ${panel.contents}
  </div>
  %if panel.footer:
  <div class="panel-footer">
    ${panel.footer}
  </div>
  %endif
</div>
