param(
    [string]$SourceRoot = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$defaultSourceRoot = Split-Path -Parent $repoRoot
if (-not $SourceRoot) {
    $SourceRoot = $defaultSourceRoot
}
$outDir = Join-Path $repoRoot "knowledge\_generated\inventory"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$source = Resolve-Path $SourceRoot
$repoPath = Resolve-Path $repoRoot

$files = Get-ChildItem -Path $source -Recurse -File |
    Where-Object { -not $_.FullName.StartsWith($repoPath.Path) } |
    ForEach-Object {
        $relative = $_.FullName.Substring($source.Path.Length + 1)
        $top = $relative.Split('\')[0]
        [PSCustomObject]@{
            Top = $top
            RelativePath = $relative
            Extension = $_.Extension.ToLowerInvariant()
            Bytes = $_.Length
            LastWriteTime = $_.LastWriteTime.ToString("s")
        }
    }

$files | Export-Csv -Path (Join-Path $outDir "files.csv") -NoTypeInformation -Encoding UTF8

$files |
    Group-Object Top |
    ForEach-Object {
        [PSCustomObject]@{
            Top = $_.Name
            Files = $_.Count
            MB = [math]::Round((($_.Group | Measure-Object Bytes -Sum).Sum) / 1MB, 2)
        }
    } |
    Sort-Object Files -Descending |
    Export-Csv -Path (Join-Path $outDir "by-top-directory.csv") -NoTypeInformation -Encoding UTF8

$files |
    Group-Object Extension |
    ForEach-Object {
        [PSCustomObject]@{
            Extension = if ($_.Name) { $_.Name } else { "(none)" }
            Files = $_.Count
            MB = [math]::Round((($_.Group | Measure-Object Bytes -Sum).Sum) / 1MB, 2)
        }
    } |
    Sort-Object Files -Descending |
    Export-Csv -Path (Join-Path $outDir "by-extension.csv") -NoTypeInformation -Encoding UTF8

$files |
    Sort-Object Top, RelativePath |
    Export-Csv -Path (Join-Path $outDir "priority-files.csv") -NoTypeInformation -Encoding UTF8

Write-Host "Inventory written to $outDir"
