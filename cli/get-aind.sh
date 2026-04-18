#!/usr/bin/env bash
# Install the aind CLI — AI for Non-Developers project manager
# Usage: curl -fsSL https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main/cli/get-aind.sh | bash

set -euo pipefail

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

REPO="lufermalgo/ai-for-non-developers"
PACKAGE="aind @ git+https://github.com/${REPO}.git#subdirectory=cli"

# ── Banner ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${CYAN}${BOLD}  aind — AI for Non-Developers${NC}"
echo -e "  ${DIM}Installing project manager CLI...${NC}"
echo ""

# ── Python version check ────────────────────────────────────────────────────
check_python() {
    local py
    py=$(command -v python3 2>/dev/null || command -v python 2>/dev/null || true)
    if [[ -z "$py" ]]; then
        echo -e "  ${RED}✗ Python 3.10+ is required but not found.${NC}"
        echo -e "  ${DIM}Install it from https://python.org and re-run.${NC}\n"
        exit 1
    fi
    local ver
    ver=$("$py" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    local major minor
    major=$(echo "$ver" | cut -d. -f1)
    minor=$(echo "$ver" | cut -d. -f2)
    if [[ "$major" -lt 3 || ("$major" -eq 3 && "$minor" -lt 10) ]]; then
        echo -e "  ${RED}✗ Python 3.10+ required (found $ver).${NC}\n"
        exit 1
    fi
    echo -e "  ${GREEN}✓${NC} Python $ver"
}

# ── Install via uv tool ─────────────────────────────────────────────────────
install_uv() {
    echo -e "  ${DIM}Using uv tool install...${NC}"
    uv tool install "$PACKAGE" --force -q
    echo -e "  ${GREEN}✓${NC} Installed via uv"
}

# ── Install via pipx ────────────────────────────────────────────────────────
install_pipx() {
    echo -e "  ${DIM}Using pipx install...${NC}"
    pipx install "$PACKAGE" --force -q
    echo -e "  ${GREEN}✓${NC} Installed via pipx"
}

# ── Install via pip --user ───────────────────────────────────────────────────
install_pip() {
    local py
    py=$(command -v python3 2>/dev/null || command -v python)
    echo -e "  ${DIM}Using pip install --user...${NC}"
    "$py" -m pip install --user --quiet "$PACKAGE"
    echo -e "  ${GREEN}✓${NC} Installed via pip"
    # Warn if ~/.local/bin not in PATH
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo -e "\n  ${YELLOW}⚠${NC}  Add to your shell profile:"
        echo -e "  ${DIM}export PATH=\"\$HOME/.local/bin:\$PATH\"${NC}"
    fi
}

# ── PATH verify ──────────────────────────────────────────────────────────────
verify() {
    if command -v aind &>/dev/null; then
        local ver
        ver=$(aind --version 2>/dev/null || echo "")
        echo -e "  ${GREEN}✓${NC} aind is ready${ver:+ ($ver)}\n"
        echo -e "  ${BOLD}Next:${NC} go to your project folder and run:"
        echo -e "  ${CYAN}  aind init${NC}\n"
    else
        echo -e "\n  ${YELLOW}⚠${NC}  aind installed but not in PATH yet."
        echo -e "  ${DIM}Restart your shell or add the bin dir to PATH.${NC}\n"
    fi
}

# ── Main ─────────────────────────────────────────────────────────────────────
check_python

if command -v uv &>/dev/null; then
    install_uv
elif command -v pipx &>/dev/null; then
    install_pipx
else
    install_pip
fi

verify
