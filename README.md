# URL Shortener API

A production-ready URL shortener built with FastAPI, PostgreSQL, and Redis — containerised with Docker Compose.

## Features
- Shorten any URL to a 6-character code
- Redirect to original URL via short code
- Redis caching — repeated redirects skip the database entirely
- Click analytics per short URL
- Duplicate URL detection — same URL always returns same code
- URL validation — rejects invalid URLs automatically
- Fully containerised with Docker Compose

## Tech Stack
- **FastAPI** — REST API framework
- **PostgreSQL** — persistent storage
- **Redis** — caching layer (TTL: 1 hour)
- **SQLAlchemy** — ORM
- **Docker Compose** — container orchestration

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/shorten` | Shorten a URL |
| GET | `/{code}` | Redirect to original URL |
| GET | `/{code}/stats` | Get click stats for a short code |

## Run Locally
```bash
git clone https://github.com/yourusername/url-shortener
cd url-shortener
docker-compose up --build
```
Visit `http://localhost:8000/docs` for interactive API docs.

## Architecture
- Every redirect checks Redis first before hitting PostgreSQL
- Cache miss stores result in Redis with 1 hour TTL
- Subsequent requests served purely from memory
