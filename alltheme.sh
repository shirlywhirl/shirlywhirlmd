#!/bin/bash

main() {
    local start_dir="$(pwd)"
    local ip_addr="$(hostname -I | cut -f 1 -d ' ')"
    local port=4000
    for theme in $(bundle list --name-only | grep -E 'jekyll-theme|minima')
    do
        cp -R . "../$theme"
        echo "theme: $theme" >> ../"$theme"/_config.yml
        cd "../$theme" || exit 1
        bundle exec jekyll  s -Vt -H "$ip_addr" -P "$port" >> jekyll_log_"$theme".log 2>&1 &
        ((port++))
        cd "$start_dir" || exit 1
    done

}


main "$@"
