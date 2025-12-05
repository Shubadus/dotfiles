#!/usr/bin/env bash
gamemode_processes=$(gamemodelist | awk 'NR>1 {print $6}')
process_count=$($gamemode_processes | wc -l)
