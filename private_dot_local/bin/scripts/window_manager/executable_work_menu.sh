work_menu() {
  result=$(printf "Confluence\nJira\nSalesForce" | fuzzel --dmenu --minimal-lines --namespace="menu" --width=14 --prompt="Work Menu: ")
  case $result in
  *Jira*)
    result=$(fuzzel --dmenu --prompt-only="Jira Case Search: ")
    if [[ "$result" ]]; then
      xdg-open "https://vocera.atlassian.net/browse/$result"
    fi
    ;;
  *SalesForce*)
    result=$(fuzzel --dmenu --prompt-only="SalesForce Search: ")
    if [[ "$result" ]]; then
      xdg-open "https://google.com/maps/dir/?api=1&destination=$result"
    fi
    ;;
  *Confluence*)
    result=$(fuzzel --dmenu --prompt-only="Confluence Search: ")
    if [[ "$result" ]]; then
      xdg-open "https://vocera.atlassian.net/wiki/search?text=$result"
    fi
    ;;
  "") exit 0 ;;
  *) xdg-open "https://google.com/search?q=$(echo "$result" | sed "s/ /+/")" ;;
  esac
}

work_menu
