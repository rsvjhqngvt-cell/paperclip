param(
    [string]$BaseUrl = "http://127.0.0.1:3100",
    [int]$TimeoutSeconds = 240
)

$ErrorActionPreference = "Stop"

function Test-Endpoint {
    param([string]$Url)
    try {
        $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 5
        return [pscustomobject]@{ Ok = $true; Code = $resp.StatusCode; Body = $resp.Content }
    } catch [System.Net.WebException] {
        $code = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { 0 }
        return [pscustomobject]@{ Ok = $false; Code = $code; Body = $_.Exception.Message }
    } catch {
        return [pscustomobject]@{ Ok = $false; Code = 0; Body = $_.Exception.Message }
    }
}

Write-Host "[paperclip-health] target=$BaseUrl timeout=${TimeoutSeconds}s"

$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
$health = $null
while ((Get-Date) -lt $deadline) {
    $health = Test-Endpoint "$BaseUrl/api/health"
    if ($health.Ok -and $health.Code -eq 200) { break }
    Start-Sleep -Seconds 3
}

if (-not $health.Ok -or $health.Code -ne 200) {
    Write-Host "[paperclip-health] FAIL: /api/health did not return 200 within ${TimeoutSeconds}s" -ForegroundColor Red
    Write-Host "  last response: $($health.Code) $($health.Body)"
    exit 1
}

Write-Host "[paperclip-health] /api/health 200" -ForegroundColor Green
Write-Host "  $($health.Body)"

$root = Test-Endpoint "$BaseUrl/"
if (-not $root.Ok -or $root.Code -ne 200) {
    Write-Host "[paperclip-health] WARN: GET / returned $($root.Code)" -ForegroundColor Yellow
} else {
    $isHtml = $root.Body -match "<!DOCTYPE html>"
    if ($isHtml) {
        Write-Host "[paperclip-health] / serves UI HTML 200" -ForegroundColor Green
    } else {
        Write-Host "[paperclip-health] WARN: / responded 200 but is not HTML" -ForegroundColor Yellow
    }
}

$favicon = Test-Endpoint "$BaseUrl/favicon.ico"
if ($favicon.Ok -and $favicon.Code -eq 200) {
    Write-Host "[paperclip-health] /favicon.ico 200" -ForegroundColor Green
} else {
    Write-Host "[paperclip-health] WARN: /favicon.ico returned $($favicon.Code)" -ForegroundColor Yellow
}

Write-Host "[paperclip-health] OK" -ForegroundColor Green
exit 0
