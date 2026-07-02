SECURITY_KEYWORDS = [
    "attack",
    "armed robbery",
    "robbery",
    "kidnap",
    "kidnapping",
    "terror",
    "terrorism",
    "explosion",
    "riot",
    "protest",
    "violence",
    "shooting",
    "gunmen",
    "military",
    "police",
    "fire",
    "flood",
    "earthquake",
    "piracy",
    "smuggling",
    "illegal mining",
    "cyber attack",
    "hacking",
    "fraud",
    "bandit",
    "conflict",
    "clash"
]


def is_security_incident(title):
    """
    Returns True if the news title contains
    any security-related keyword.
    """

    title = title.lower()

    for keyword in SECURITY_KEYWORDS:
        if keyword in title:
            return True

    return False