import re

BLACKLISTED_DOMAINS = [
    "malware-testing.com",
    "phishing-example.com",
    "fake-login.net",
    "suspicious-site.org",
    "dangerous-downloads.com",
    "free-crypto-airdrop.net",
    "paypal-security-check.com",
    "steam-gift-free.com",
    "discord-nitro-free.net",
    "update-your-bank-login.com",
    "microsoft-support-alert.com",
    "verify-wallet-now.net",
    "claim-bitcoin-fast.com"
]

SUSPICIOUS_KEYWORDS = [
    "free-money",
    "bitcoin-generator",
    "hack-account",
    "free-crypto",
    "darkweb",
    "free-vbucks",
    "free-nitro",
    "claim-reward",
    "verify-account",
    "bank-login",
    "wallet-recovery",
    "instant-profit",
    "double-your-bitcoin",
    "crypto-airdrop",
    "password-reset",
    "urgent-action",
    "security-alert",
    "confirm-identity",
    "gift-card-generator",
    "admin-access"
]

SUSPICIOUS_TLDS = [
    ".tk",
    ".ml",
    ".ga",
    ".cf",
    ".gq",
    ".xyz",
    ".top",
    ".buzz"
]

SHORTENED_URL_SERVICES = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly"
]

FAKE_BRAND_PATTERNS = [
    r"paypa[l1]",
    r"g[o0]{2}gle",
    r"micr[o0]soft",
    r"amaz[o0]n",
    r"faceb[o0]{2}k",
    r"instagr[a@]m",
    r"disc[o0]rd",
    r"netfl[i1]x",
    r"bank-secure",
    r"wallet-secure"
]

DANGEROUS_FILE_EXTENSIONS = [
    ".exe",
    ".bat",
    ".scr",
    ".vbs",
    ".ps1",
    ".cmd",
    ".jar"
]

KNOWN_SAFE_DOMAINS = [
    "google.com",
    "github.com",
    "microsoft.com",
    "openai.com",
    "wikipedia.org",
    "duckduckgo.com",
    "python.org"
]


def contains_fake_brand(domain):
    domain = domain.lower()

    for pattern in FAKE_BRAND_PATTERNS:
        if re.search(pattern, domain):
            return True

    return False