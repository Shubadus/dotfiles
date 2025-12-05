Socket=$XDG_RUNTIME_DIR/alacritty.sock
# title=${1:-"Alacritty"}
class=${1:-"Alacritty"}
command=${2:-""}

alacritty msg --socket $Socket create-window --class $class -e $command || alacritty --socket $Socket --class $class -e $command
# if [ -n "$2" ]; then
#   alacritty --class $2 -e $1
# else
#   alacritty msg --socket $Socket create-window -e $1 || alacritty --socket $Socket -e $1
# fi
