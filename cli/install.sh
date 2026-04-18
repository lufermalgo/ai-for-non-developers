#!/bin/bash

# ==========================================
# AI for Non-Developers - Universal Installer
# ==========================================

set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

# ── Banner ─────────────────────────────────────────────────────────────────
clear
echo ""
echo -e "${CYAN}${BOLD}"
echo "   █████╗ ██╗    ███╗   ██╗ ██████╗ ███╗   ██╗      ██████╗ ███████╗██╗   ██╗"
echo "  ██╔══██╗██║    ████╗  ██║██╔═══██╗████╗  ██║      ██╔══██╗██╔════╝██║   ██║"
echo "  ███████║██║    ██╔██╗ ██║██║   ██║██╔██╗ ██║█████╗██║  ██║█████╗  ██║   ██║"
echo "  ██╔══██║██║    ██║╚██╗██║██║   ██║██║╚██╗██║╚════╝██║  ██║██╔══╝  ╚██╗ ██╔╝"
echo "  ██║  ██║██║    ██║ ╚████║╚██████╔╝██║ ╚████║      ██████╔╝███████╗ ╚████╔╝ "
echo "  ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═════╝ ╚══════╝  ╚═══╝ "
echo -e "${NC}"
echo -e "  ${DIM}Your idea. Real software. No code required.${NC}"
echo ""

# ── Arrow-key selection ────────────────────────────────────────────────────
arrow_select() {
    local -a options=("$@")
    local selected=0
    local num=${#options[@]}

    _draw_options() {
        for i in "${!options[@]}"; do
            if [ "$i" -eq "$selected" ]; then
                echo -e "   ${GREEN}${BOLD}❯  ${options[$i]}${NC}"
            else
                echo -e "   ${DIM}   ${options[$i]}${NC}"
            fi
        done
    }

    tput civis
    _draw_options

    while true; do
        read -rsn1 key
        if [[ "$key" == $'\x1b' ]]; then
            read -rsn2 seq
            case "$seq" in
                '[A') ((selected > 0)) && ((selected--)) ;;
                '[B') ((selected < num - 1)) && ((selected++)) ;;
            esac
        elif [[ "$key" == "" ]]; then
            break
        fi
        tput cuu "$num"
        _draw_options
    done

    tput cnorm
    ARROW_RESULT=$selected
}

# ── Step 1: Target directory ───────────────────────────────────────────────
TARGET_DIR=$(pwd)
echo -e "  ${WHITE}Project directory:${NC} $TARGET_DIR"
read -p "  Use this directory? [Y/n]: " CONFIRM
CONFIRM=${CONFIRM:-Y}

if [[ "$CONFIRM" =~ ^[Nn]$ ]]; then
    read -p "  Enter the absolute path: " TARGET_DIR
fi

mkdir -p "$TARGET_DIR"

# ── Step 2: Platform selection ─────────────────────────────────────────────
echo -e "\n  ${WHITE}Which AI tool will you be using?${NC}"
echo -e "  ${DIM}Use ↑ ↓ arrows and press Enter${NC}\n"

PLATFORMS=(
    "Gemini CLI / Antigravity   →  GEMINI.md"
    "Claude Code / CoWork       →  CLAUDE.md"
    "OpenCode                   →  AGENTS.md"
    "Other                      →  AGENTS.md"
)

arrow_select "${PLATFORMS[@]}"

case $ARROW_RESULT in
    0) RULE_FILE="GEMINI.md" ;;
    1) RULE_FILE="CLAUDE.md" ;;
    2) RULE_FILE="AGENTS.md" ;;
    *) RULE_FILE="AGENTS.md" ;;
esac

INSTALL_DIR="$TARGET_DIR"

# ── Step 3: Remove previous platform files (idempotency) ───────────────────
for f in "GEMINI.md" "CLAUDE.md" "AGENTS.md"; do
    if [ -f "$TARGET_DIR/$f" ] && [ "$f" != "$RULE_FILE" ]; then
        rm "$TARGET_DIR/$f"
        echo -e "\n  ${YELLOW}✕ Removed previous installation: $f${NC}"
    fi
done

# ── Step 4: Deploy rule file ───────────────────────────────────────────────
TEMPLATE_SRC="$(dirname "$0")/../templates/AGENT.md"

if [ ! -f "$TEMPLATE_SRC" ]; then
    echo -e "\n  ${YELLOW}↓ Downloading template...${NC}"
    curl -sSL "https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main/templates/AGENT.md" \
        -o "$INSTALL_DIR/$RULE_FILE"
else
    cp "$TEMPLATE_SRC" "$INSTALL_DIR/$RULE_FILE"
fi

# ── Step 5: Initialize .aind/ memory files ─────────────────────────────────
AI_DIR="$TARGET_DIR/.aind"
mkdir -p "$AI_DIR/specs/archive"

for f in context.md roadmap.md tasks.md lessons.md; do
    touch "$AI_DIR/$f"
done

if [ ! -s "$AI_DIR/context.md" ]; then
    printf "# Project Context\n\n## Project Overview\nPending discovery...\n" > "$AI_DIR/context.md"
fi

if [ ! -s "$AI_DIR/roadmap.md" ]; then
    printf "# Project Roadmap\n\n## Milestones\n- [ ] Initial Setup & Discovery\n" > "$AI_DIR/roadmap.md"
fi

if [ ! -s "$AI_DIR/tasks.md" ]; then
    printf "# Project Tasks\n\n## Current Focus\n- [ ] Initial discovery of project requirements\n" > "$AI_DIR/tasks.md"
fi

# ── Summary ────────────────────────────────────────────────────────────────
echo -e "\n  ${GREEN}${BOLD}✅ Installation complete!${NC}"
echo -e "  ${DIM}────────────────────────────────────────${NC}"
echo -e "  ${CYAN}Rule file:${NC}  $INSTALL_DIR/$RULE_FILE"
echo -e "  ${CYAN}Memory:${NC}     $TARGET_DIR/.aind/"
echo -e "  ${DIM}────────────────────────────────────────${NC}"
echo -e "\n  ${WHITE}Open your AI tool and say:${NC}"
echo -e "  ${DIM}\"I want to build [your idea]. Let's start.\"${NC}\n"
