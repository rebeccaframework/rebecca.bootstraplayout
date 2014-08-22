<div class="list-group">
  %for item in navigationlist.items:
  %if item.active:
  <a class="list-group-item active" href="${item.url}">${item.label}</a>
  %else:
  <a class="list-group-item" href="${item.url}">${item.label}</a>
  %endif
  %endfor
</div>
