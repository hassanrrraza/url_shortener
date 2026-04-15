# Request-derived click metadata. IP + referrer are sensitive; production may hash, drop, or cap retention.
from typing import Optional

from flask import Request

from app.models import ClickAnalytics

REFERRER_MAX_LEN = 500
USER_AGENT_STORE_MAX = 256
CLIENT_IP_MAX_LEN = 45


def client_ip(request: Request) -> Optional[str]:
    xff = request.headers.get('X-Forwarded-For')
    if xff:
        return xff.split(',')[0].strip()[:CLIENT_IP_MAX_LEN] or None
    if request.remote_addr:
        return str(request.remote_addr)[:CLIENT_IP_MAX_LEN]
    return None


def truncated_referrer(request: Request) -> str | None:
    ref = request.headers.get('Referer') or request.headers.get('Referrer') or ''
    ref = ref.strip()
    if not ref:
        return None
    return ref[:REFERRER_MAX_LEN]


def click_context_from_request(request: Request) -> dict:
    ua_header = request.headers.get('User-Agent') or ''
    parsed = ClickAnalytics.parse_user_agent(ua_header)
    ua_stored = (ua_header.strip()[:USER_AGENT_STORE_MAX] if ua_header.strip() else None)
    return {
        'referrer': truncated_referrer(request),
        'ip_address': client_ip(request),
        'device_type': (parsed.get('device_type') or 'Unknown')[:50],
        'browser': (parsed.get('browser') or 'Unknown')[:100],
        'os': (parsed.get('os') or 'Unknown')[:100],
        'user_agent': ua_stored,
    }
