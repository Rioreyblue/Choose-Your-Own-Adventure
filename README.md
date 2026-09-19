# Choose Your Own Adventure

Interactive branching stories. Enter a theme, the backend generates a story tree with an LLM, and the frontend lets you play through the choices.

```
Choose-Your-Own-Adventure/
  frontend/   React + Vite UI
  backend/    FastAPI + SQLite + LLM generation
```

## Features

- Theme → generate a full choose-your-own-adventure tree
- Async job: create story, poll status, then play
- Branching choices with endings (win / lose)
- Restart a story or generate another

## Local setup

Run **both** services. Frontend proxies `/api` to the backend.

### Backend (`:8000`)

```bash
cd backend
# activate your venv / uv env
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Docs: http://127.0.0.1:8000/docs
- Needs a `.env` with `DATABASE_URL` and your LLM API settings

### Frontend (`:5173`)

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

`frontend/src/util.js` uses `API_BASE_URL = "/api"`. Vite forwards that to `http://localhost:8000`.

## Routes

| URL | What |
|-----|------|
| `/` | Enter theme, start generation |
| `/story/:id` | Play story by id |

## API (main bits)

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/api/stories/create` | Start generation (returns `job_id`) |
| `GET` | `/api/jobs/{job_id}` | Poll status / `story_id` |
| `GET` | `/api/stories/{id}/complete` | Full story tree for play |

## If it fails

- **ECONNREFUSED :8000** — backend not running
- **Generate stuck / no spinner progress** — check Vite terminal proxy errors and backend logs
- Smoke-test the API: `GET http://127.0.0.1:8000/api/stories/1/complete`
