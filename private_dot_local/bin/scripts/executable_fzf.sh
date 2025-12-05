#!/bin/sh
fzf_args=(
  --multi
  --preview 'yay -Sii {1}'
  --preview-label='alt-p: toggle description, alt-j/k: scroll, tab: multi-select'
  --preview-label-pos='bottom'
  --preview-window 'down:65%:wrap'
  --bind 'alt-p:toggle-preview'
  --bind 'alt-d:preview-half-page-down,alt-u:preview-half-page-up'
  --bind 'alt-k:preview-up,alt-j:preview-down'
  --color 'pointer:green,marker:green'
  # --bind="j:down,k:up,s:jump,p:toggle-preview"
  # --bind="h:backward-char,l:forward-char,e:forward-word,b:backward-word"
  # --bind="d:clear-query"
  # --bind='y:execute(echo {} | xsel -b)'
  # --bind="E:preview-half-page-down,U:preview-half-page-up"
  # --bind="c:cancel,x:forward-char+backward-delete-char"
  # --bind="X:backward-delete-char"
  # --bind="start:enable-search+unbind(e,j,s,p,h,l,é,b,d,y,E,U,c,x,X,i,a,A,I)"
  # --bind="i:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)"
  # --bind="a:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+forward-char"
  # --bind="A:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+end-of-line"
  # --bind="I:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+beginning-of-line"
  # --bind="esc:disable-search+rebind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)"
  # --bind="®:backward-kill-word,change:top,backward-eof:abort"
)
fzf "${fzf_args[@]}" "$@"
