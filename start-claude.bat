@echo off
echo ========================================
echo Starting Claude Code for Svetlinki Project
echo ========================================
echo.
echo Project Directory: C:\Users\denit\Local Sites\svetlinkielementor
echo.

cd /d "C:\Users\denit\Local Sites\svetlinkielementor"

echo Checking for .mcp.json configuration...
if exist .mcp.json (
    echo [OK] .mcp.json found
) else (
    echo [WARNING] .mcp.json NOT found!
)
echo.

echo Starting Claude Code...
echo Please wait 15-20 seconds for MCP servers to load after startup.
echo.
echo Expected MCP Tools:
echo - wp-elementor-mcp (32 tools)
echo - json-schema-validator (5 tools)
echo - brave-search
echo - playwright (20+ tools)
echo.
echo ========================================

npx claude-code

echo.
echo Claude Code has exited.
pause
