#!/bin/bash

session="Fermat"

tmux new-session -d -s $session

tmux rename-window -t 0 Code
tmux send-keys -t Code 'zsh' C-m 'clear' C-m 'nvim' C-m

tmux new-window -t $session:1 -n 'Execute'

tmux new-window -t $session:2 -n 'Git'
tmux send-keys -t 'Git' 'lazygit' C-m

tmux new-window -t $session:3 -n 'Shell'

tmux attach-session -t $session:2
