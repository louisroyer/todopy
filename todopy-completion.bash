#/usr/bin/env bash
_todopy_completions()
{
	case "${COMP_WORDS[1]}" in
		edit|create) COMPREPLY=();;
		commit) COMPREPLY=($(compgen -W "'all'" "${COMP_WORDS[2]}"));;
	*) COMPREPLY=($(compgen -W "edit commit create" "${COMP_WORDS[1]}"));;
	esac
}
complete -F _todopy_completions todopy
