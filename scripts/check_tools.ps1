$requiredCommands = @("git", "python", "docker")

foreach ($cmd in $requiredCommands) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        Write-Host "$cmd: installed"
    } else {
        Write-Host "$cmd: missing"
    }
}
