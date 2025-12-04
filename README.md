# Docker Speedtest

A web-based speed test application using Ookla's [speedtest-cli](https://www.speedtest.net/apps/cli), running in Docker.

## Features

- Run internet speed tests on-demand via web interface
- Displays download speed, upload speed, and ping latency
- Shows server information for each test
- Runs in a Docker container

## Quick Start

1. **Accept the Ookla EULA** - Edit `docker-compose.yml` and set:
   ```yaml
   - SPEEDTEST_ACCEPT_EULA=true
   ```

   By setting this to `true`, you accept Ookla's:
    - [EULA](https://www.speedtest.net/about/eula)
    - [Terms](https://www.speedtest.net/about/terms)
    - [Privacy](https://www.speedtest.net/about/privacy)

2. **Build and run:**
   ```bash
   docker-compose up --build
   ```

3. **Access the web interface:**
   ```
   http://localhost:8012
   ```

## Usage

1. Navigate to http://localhost:8012
2. Click "Run Speed Test"
3. Wait for the test to complete (typically 30-60 seconds)
4. View your results

## Environment Variables

| Variable                | Required | Description                                                                  |
|-------------------------|----------|------------------------------------------------------------------------------|
| `SPEEDTEST_ACCEPT_EULA` | Yes      | Set to `true` to accept [Ookla's EULA](https://www.speedtest.net/about/eula) |

## Requirements

- Docker
- Docker Compose

## API

### POST /api/speedtest

Runs a speed test and returns JSON results.

**Response:**

```json
{
  "error": false,
  "download": 150.25,
  "upload": 25.50,
  "ping": 12.5,
  "server": {
    "name": "Server Name",
    "location": "City",
    "country": "Country"
  },
  "result_url": "https://www.speedtest.net/result/..."
}
```

## License

MIT
