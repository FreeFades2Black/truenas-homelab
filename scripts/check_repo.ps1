$requiredFiles = @(
    "README.md",
    "docker-compose.yml",
    "values.yaml"
)

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$missing = @()

foreach ($file in $requiredFiles) {
    if (-not (Test-Path (Join-Path $repoRoot $file))) {
        $missing += $file
    }
}

if ($missing.Count -gt 0) {
    Write-Host "Missing expected files:"
    foreach ($item in $missing) {
        Write-Host " - $item"
    }
}
else {
    Write-Host "Repository structure looks good."
}
