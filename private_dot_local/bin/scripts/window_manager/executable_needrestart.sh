result=$(needrestart -k | head -n 3 | tr -d "\n")
if [[ $result == "Pending kernel upgrade!" ]]; then
  echo "Reboot required to complete upgrade"
else
  echo ""
fi
