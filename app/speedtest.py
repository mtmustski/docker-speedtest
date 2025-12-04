import json
import os
import subprocess


def check_eula_accepted():
    """Check if user has accepted the Ookla EULA via environment variable."""
    return os.environ.get("SPEEDTEST_ACCEPT_EULA", "").lower() == "true"


def run_speedtest():
    """
    Run the Ookla speedtest-cli and return parsed results.

    Returns:
        dict: Speed test results with download, upload, ping, and server info
              or error information if the test fails.
    """
    if not check_eula_accepted():
        return {
            "error": True,
            "message": "You must accept the Ookla EULA by setting SPEEDTEST_ACCEPT_EULA=true"
        }

    try:
        result = subprocess.run(
            ["speedtest", "--format=json", "--accept-license"],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            return {
                "error": True,
                "message": result.stderr or "Speed test failed"
            }

        data = json.loads(result.stdout)

        # Convert speeds from bits/s to Mbps
        download_mbps = data.get("download", {}).get("bandwidth", 0) * 8 / 1_000_000
        upload_mbps = data.get("upload", {}).get("bandwidth", 0) * 8 / 1_000_000

        return {
            "error": False,
            "download": round(download_mbps, 2),
            "upload": round(upload_mbps, 2),
            "ping": round(data.get("ping", {}).get("latency", 0), 2),
            "server": {
                "name": data.get("server", {}).get("name", "Unknown"),
                "location": data.get("server", {}).get("location", "Unknown"),
                "country": data.get("server", {}).get("country", "Unknown")
            },
            "result_url": data.get("result", {}).get("url", "")
        }

    except subprocess.TimeoutExpired:
        return {
            "error": True,
            "message": "Speed test timed out after 120 seconds"
        }
    except json.JSONDecodeError:
        return {
            "error": True,
            "message": "Failed to parse speed test results"
        }
    except FileNotFoundError:
        return {
            "error": True,
            "message": "speedtest-cli not found. Please install it first."
        }
    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }
