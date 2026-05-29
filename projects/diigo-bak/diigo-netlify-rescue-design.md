# Diigo Rescue Service Design (Netlify)

## Assumption

We assume Diigo is defunct (domain suspended, service effectively abandoned) and this service is an emergency, good-faith effort to help users recover their own data.

This is an operational assumption for this rescue effort, not legal advice.

## Goal

Provide a short-lived rescue service for former Diigo users who do not have API keys:

- User enters Diigo username/password.
- Service uses a server-side API key to export all bookmarks.
- User downloads their data (`.ndjson`) immediately.

## Constraints

- Diigo domain/API is unstable.
- Users generally do not have personal API keys.
- Shared API key may be non-rotatable.
- Service must minimize risk when handling credentials.

## Non-Goals

- Long-term hosted bookmark platform.
- Account management for users.
- Data warehousing of user exports.

## High-Level Architecture

1. Static UI (standalone Netlify site)
- Form: username, password.
- "Start export" button.
- Progress display.
- Download links when complete.

2. Netlify Function API
- `POST /.netlify/functions/export-start`
- `GET /.netlify/functions/export-status?id=...`
- `GET /.netlify/functions/export-download?id=...`

3. Background export worker
- Netlify Background Function does paged fetch from Diigo API.
- Writes temporary result to Netlify Blobs (or equivalent short-lived storage).
- Stores only job metadata + encrypted result blob + expiry.

4. Diigo API access
- Server-side secret: `DIIGO_API_KEY`.
- Auth to Diigo with Basic auth from submitted username/password.
- Prefer known working endpoint strategy (host/IP override in runtime code if needed).

Deployment model:

- Separate Netlify site, distinct from madmode.com.
- Source rooted under `projects/diigo-bak/rescue-site/`.
- Manual deploy of that subdirectory only.

## Source Files

Planned implementation files:

- `projects/diigo-bak/rescue-site/index.html`
  - Standalone public explainer page and UI.
- `projects/diigo-bak/rescue-site/static/js/diigo-rescue.js`
  - Browser-side form handling, polling, and download trigger.
- `projects/diigo-bak/rescue-site/netlify/functions/diigo-export-start.js`
  - Validate request, enforce limits, create export job.
- `projects/diigo-bak/rescue-site/netlify/functions/diigo-export-status.js`
  - Return job status/progress.
- `projects/diigo-bak/rescue-site/netlify/functions/diigo-export-download.js`
  - Return NDJSON download for completed job.
- `projects/diigo-bak/rescue-site/netlify/functions/diigo-export-worker.js`
  - Background export worker that pages Diigo API and writes NDJSON blob.
- `projects/diigo-bak/rescue-site/netlify/functions/_diigo-client.js`
  - Shared Diigo API client and pagination logic.
- `projects/diigo-bak/rescue-site/netlify/functions/_rate-limit.js`
  - Per-username limiter and daily cap checks.
- `projects/diigo-bak/rescue-site/netlify/functions/_jobs.js`
  - Job metadata and blob storage helpers.
- `projects/diigo-bak/rescue-site/netlify.toml`
  - Function configuration, env wiring, and any route redirects.

## Data Flow

1. User submits username/password to `export-start`.
2. Service validates anti-abuse checks (captcha/rate limits/token).
3. Service creates job ID and starts background export.
4. Background function pages bookmarks (`start`, `count`) until empty page.
5. Service serializes:
- `bookmarks.ndjson` (one item per line)
6. User polls status endpoint.
7. User downloads files.
8. Job and blobs expire quickly (default: 1 hour).

## Threat Model

Primary risks:

- Credential theft (username/password exposure).
- API key abuse via open endpoint.
- Data leakage between users.
- Service used for brute force attacks.

Secondary risks:

- Excessive costs due to abuse.

## Security Requirements

1. Secret handling
- Keep `DIIGO_API_KEY` only in Netlify env secrets.
- Never echo or return key.

2. Credential handling
- Do not log request bodies.
- Keep username/password only in memory for outbound API calls.
- Zero references after use.
- Do not persist credentials in blobs or metadata.

3. Endpoint protection
- Per-username rate limits.
- Global concurrency cap.
- Netlify platform protections are the fallback for broader abuse events.

4. Data isolation
- Random, unguessable job IDs (>=128 bits).
- Download endpoints require signed, short-lived token.
- Jobs hard-expire and are deleted automatically.

5. Observability without secrets
- Log only: timestamp, hashed username, job state, item counts, error class.
- No raw credentials, no raw Diigo URLs with secrets.

6. Operational controls
- Kill switch env var (`RESCUE_ENABLED=false`).
- Max runtime per job.
- Max bookmark count guard.
- Explicit service sunset date with auto-disable.

7. Mandatory short window
- Default operating window is 3 days.
- Service must refuse new jobs after sunset.
- Re-enable requires manual config change to a new sunset date.

## API Sketch

### `POST /export-start`

Request JSON:

```json
{
  "username": "alice",
  "password": "secret"
}
```

Response:

```json
{
  "jobId": "j_...",
  "statusUrl": "/.netlify/functions/export-status?id=j_..."
}
```

### `GET /export-status?id=...`

Response:

```json
{
  "state": "queued|running|done|error|expired",
  "fetched": 1200,
  "message": "optional"
}
```

### `GET /export-download?id=...`

Response headers:

- `Content-Type: application/x-ndjson`
- `Content-Disposition: attachment; filename="diigo-bookmarks.ndjson"`

## Runtime Strategy for Unstable DNS/TLS

Implement a small transport abstraction:

- Primary: call `https://secure.diigo.com/api/v2/...`.
- Fallback: known-good host/IP strategy if primary fails.
- Surface clear error messages when Diigo backend is unavailable.

Note: exact fallback mechanics depend on runtime network capabilities.

## UX Notes

- Clear warning: "You are trusting this rescue service with your Diigo password."
- Explicit retention policy shown in UI.
- Show estimated export duration and current page count.
- Offer "Download NDJSON" first (stream-friendly).

## Rollout Plan

1. Private alpha (invite-only, 3-5 users).
2. Limited beta (strict daily cap: 50 export starts/day total).

Beyond limited beta is intentionally out of scope for this plan and will
be decided after beta results.

## Feedback Channel

Collect operator/user feedback in:

- https://github.com/dckc/madmode-blog/issues/32

## Sunset Policy

- Config:
  - `RESCUE_START_AT` (UTC timestamp)
  - `RESCUE_SUNSET_AT` (UTC timestamp)
- Constraint:
  - `RESCUE_SUNSET_AT - RESCUE_START_AT <= 72h`
- Runtime behavior:
  - If current time is past `RESCUE_SUNSET_AT`, all `export-start` requests return `410 Gone`.
  - Existing incomplete jobs are cancelled.
- Manual renewal rule:
  - Service does not auto-extend.
  - Operator must deploy a new config with a fresh sunset timestamp.

## Exit Plan

- Disable via kill switch.
- Revoke/remove API key if possible.
- Delete all retained blobs and job metadata.
- Keep only aggregate, non-sensitive metrics.

## Open Questions

1. Is shared-key usage compliant with Diigo API terms?
2. What Netlify runtime networking features are available for host/IP fallback?
3. What is acceptable maximum per-user export size/time?
4. How long should completed exports remain downloadable (15m, 1h, 24h)?
