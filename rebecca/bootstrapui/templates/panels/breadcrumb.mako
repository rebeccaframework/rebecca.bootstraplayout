<ol class="breadcrumb">
  %for item in breadcrumb.items:
  %if item.active:
  <li class="active">${item.label}</li>
  %else:
  <li><a href="${item.url}">${item.label}</a></li>
  %endif
  %endfor
</ol>
