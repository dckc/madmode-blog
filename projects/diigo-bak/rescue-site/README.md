# Diigo Rescue Site

Standalone Netlify site for emergency Diigo bookmark export.

## Required Environment Variables

- `DIIGO_API_KEY`
- `RESCUE_START_AT` (UTC timestamp)
- `RESCUE_SUNSET_AT` (UTC timestamp, <= 72h after start)

Example values (for this week):

- `RESCUE_START_AT=2026-03-07T23:00:00Z` (`2026-03-07 17:00` America/Chicago)
- `RESCUE_SUNSET_AT=2026-03-10T22:00:00Z` (`2026-03-10 17:00` America/Chicago)

## Optional Environment Variables

- `RESCUE_ENABLED` (`true`/`false`, default `true`)
- `DIIGO_KNOWN_IP` (default `54.148.192.94`)
- `MAX_ACTIVE_JOBS` (default `3`)
- `MAX_GLOBAL_STARTS_PER_DAY` (default `50`)
- `MAX_USER_STARTS_PER_DAY` (default `5`)
- `MAX_DOWNLOAD_AGE_MS` (default `3600000`)

## Local Notes

This subproject is separate from the main blog build. Deploy this directory
as its own Netlify site.
